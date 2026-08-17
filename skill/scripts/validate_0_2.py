#!/usr/bin/env python3
"""Validate result or calibration-extract JSON for methodology 0.2 draft."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


DIMENSIONS = tuple("ABCDEFGHIJKL")
CONFIDENCE = {"wysoka", "srednia", "niska"}
VERDICTS = {
    "rzetelny",
    "rzetelny_z_niewielkimi_zastrzezeniami",
    "rzetelny_z_istotnymi_zastrzezeniami",
    "nierzetelny",
    "nie_mozna_rozstrzygnac",
}
SEVERITIES = {"krytyczne", "duze", "srednie", "male"}
CENTRALITIES = {"rdzen", "istotne_wsparcie", "element_poboczny"}
RISKS = {"wysokie", "srednie", "niskie"}
SOURCE_COVERAGE = {"pelne", "wystarczajace", "czesciowe", "niewystarczajace"}
CORRECTIONS = {"ograniczona", "strukturalna", "nie_dotyczy"}
SAFE_RECOMMENDATIONS = {
    "bez_zastrzezen",
    "z_niewielkimi_korektami",
    "z_nazwanymi_korektami_lub_zrodlami",
    "nie_do_praktycznego_uzycia",
    "nie_mozna_ocenic",
}
MATERIAL_ROLES = {
    "tresc_glowna",
    "material_centralny_zewnetrzny",
    "material_dodatkowy",
    "material_wylaczony",
}
CORE_MATERIAL_ROLES = {"tresc_glowna", "material_centralny_zewnetrzny"}
CLAIM_CATEGORIES = {"F", "P", "S", "T", "B", "Z", "I", "O"}
CLAIM_IMPORTANCE = {"kluczowe", "wazne", "pomocnicze"}
VERIFIABILITY = {"weryfikowalne", "czesciowo_weryfikowalne", "nieweryfikowalne"}
CLAIM_RESULTS = {
    "zgodne",
    "zasadniczo_zgodne",
    "czesciowo_zgodne",
    "mylace",
    "niezgodne",
    "nieweryfikowalne",
    "nierozstrzygniete",
}
ACCESS_VALUES = {"tak", "nie", "not_available"}


class ValidationError(Exception):
    pass


def fail(path: str, message: str) -> None:
    raise ValidationError(f"{path}: {message}")


def require_mapping(value: object, path: str) -> dict:
    if not isinstance(value, dict):
        fail(path, "expected object")
    return value


def require_list(value: object, path: str) -> list:
    if not isinstance(value, list):
        fail(path, "expected array")
    return value


def require_keys(value: dict, required: set[str], path: str) -> None:
    missing = sorted(required - set(value))
    if missing:
        fail(path, f"missing keys: {', '.join(missing)}")


def require_nonempty_string(value: object, path: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(path, "expected non-empty string")
    return value


def require_enum(value: object, allowed: set[str], path: str) -> str:
    if value not in allowed:
        fail(path, f"unexpected value {value!r}; allowed: {', '.join(sorted(allowed))}")
    return str(value)


def require_url(value: object, path: str) -> str:
    text = require_nonempty_string(value, path)
    parsed = urlparse(text)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        fail(path, "expected absolute HTTP(S) URL")
    return text


def validate_scores(value: object, path: str = "scores") -> None:
    scores = require_mapping(value, path)
    if set(scores) != set(DIMENSIONS):
        fail(path, "must contain exactly A-L")
    for key in DIMENSIONS:
        score = scores[key]
        if score != "nd" and (not isinstance(score, int) or isinstance(score, bool) or not 0 <= score <= 4):
            fail(f"{path}.{key}", "expected integer 0-4 or 'nd'")


def validate_issue_counts(value: object, issues: list | None = None, path: str = "issue_counts") -> None:
    counts = require_mapping(value, path)
    if set(counts) != SEVERITIES:
        fail(path, "must contain exactly krytyczne, duze, srednie, male")
    for key, count in counts.items():
        if not isinstance(count, int) or isinstance(count, bool) or count < 0:
            fail(f"{path}.{key}", "expected non-negative integer")
    if issues is not None:
        actual = Counter(issue["severity"] for issue in issues)
        for key in SEVERITIES:
            if counts[key] != actual[key]:
                fail(f"{path}.{key}", f"declared {counts[key]}, found {actual[key]}")


def validate_evaluator(value: object, path: str = "evaluator") -> None:
    evaluator = require_mapping(value, path)
    required = {
        "type",
        "name",
        "model_snapshot",
        "reasoning_setting",
        "tools",
        "memory_access",
        "project_access",
        "private_repository_access",
    }
    require_keys(evaluator, required, path)
    require_enum(evaluator["type"], {"czlowiek", "ai", "zespol"}, f"{path}.type")
    for key in ("name", "model_snapshot", "reasoning_setting"):
        require_nonempty_string(evaluator[key], f"{path}.{key}")
    tools = require_list(evaluator["tools"], f"{path}.tools")
    for index, tool in enumerate(tools):
        require_nonempty_string(tool, f"{path}.tools[{index}]")
    for key in ("memory_access", "project_access", "private_repository_access"):
        require_enum(evaluator[key], ACCESS_VALUES, f"{path}.{key}")


def validate_material(value: object, path: str, core_only: bool = False) -> None:
    material = require_mapping(value, path)
    required = {"material_id", "role", "url", "version"}
    if not core_only:
        required |= {"accessed_at", "immutable", "scope"}
    require_keys(material, required, path)
    require_nonempty_string(material["material_id"], f"{path}.material_id")
    allowed_roles = CORE_MATERIAL_ROLES if core_only else MATERIAL_ROLES
    require_enum(material["role"], allowed_roles, f"{path}.role")
    require_url(material["url"], f"{path}.url")
    require_nonempty_string(material["version"], f"{path}.version")
    if not core_only:
        require_nonempty_string(material["accessed_at"], f"{path}.accessed_at")
        require_enum(material["immutable"], {"tak", "nie", "not_available"}, f"{path}.immutable")
        require_nonempty_string(material["scope"], f"{path}.scope")


def unique_ids(items: list[dict], key: str, path: str) -> set[str]:
    ids: list[str] = []
    for index, item in enumerate(items):
        item = require_mapping(item, f"{path}[{index}]")
        ids.append(require_nonempty_string(item.get(key), f"{path}[{index}].{key}"))
    if len(ids) != len(set(ids)):
        fail(path, f"duplicate {key}")
    return set(ids)


def validate_result(data: object) -> None:
    root = require_mapping(data, "root")
    required = {
        "schema_version",
        "analysis_id",
        "methodology",
        "publication",
        "materials",
        "evaluator",
        "claim_count",
        "claims",
        "issues",
        "issue_counts",
        "scores",
        "score_rationales",
        "verdict",
        "verdict_basis_issue_ids",
        "counterfactual_correction",
        "verdict_confidence",
        "source_coverage",
        "safe_recommendation",
        "verdict_rationale",
        "limitations",
        "sources",
    }
    require_keys(root, required, "root")
    if root["schema_version"] != "0.2-draft":
        fail("schema_version", "expected '0.2-draft'")
    require_nonempty_string(root["analysis_id"], "analysis_id")

    methodology = require_mapping(root["methodology"], "methodology")
    require_keys(methodology, {"version", "identifier", "base_identifier", "frozen_before_critical_pass"}, "methodology")
    if methodology["version"] != "0.2-draft":
        fail("methodology.version", "expected '0.2-draft'")
    require_nonempty_string(methodology["identifier"], "methodology.identifier")
    require_nonempty_string(methodology["base_identifier"], "methodology.base_identifier")
    if not isinstance(methodology["frozen_before_critical_pass"], bool):
        fail("methodology.frozen_before_critical_pass", "expected boolean")

    publication = require_mapping(root["publication"], "publication")
    publication_required = {
        "publication_id", "title", "authors", "url", "published_at", "updated_at",
        "accessed_at", "analyzed_at", "language", "publication_type", "full_text",
    }
    require_keys(publication, publication_required, "publication")
    for key in ("publication_id", "title", "accessed_at", "analyzed_at", "language"):
        require_nonempty_string(publication[key], f"publication.{key}")
    require_url(publication["url"], "publication.url")
    require_enum(publication["full_text"], {"tak", "nie", "czesciowo"}, "publication.full_text")
    for key in ("authors", "publication_type"):
        values = require_list(publication[key], f"publication.{key}")
        for index, item in enumerate(values):
            require_nonempty_string(item, f"publication.{key}[{index}]")

    materials = require_list(root["materials"], "materials")
    if not materials:
        fail("materials", "expected at least one material")
    for index, material in enumerate(materials):
        validate_material(material, f"materials[{index}]")
    if not any(material["role"] == "tresc_glowna" for material in materials):
        fail("materials", "missing tresc_glowna")
    unique_ids(materials, "material_id", "materials")

    validate_evaluator(root["evaluator"])

    claims = require_list(root["claims"], "claims")
    if root["claim_count"] != len(claims):
        fail("claim_count", f"declared {root['claim_count']}, found {len(claims)}")
    claim_ids = unique_ids(claims, "claim_id", "claims")
    for index, claim in enumerate(claims):
        path = f"claims[{index}]"
        if not re.fullmatch(r"T-[0-9]{3,}", claim["claim_id"]):
            fail(f"{path}.claim_id", "expected T- followed by at least three digits")
        require_keys(claim, {"claim_match_id", "location", "text", "category", "importance", "verifiability", "result", "confidence", "source_ids", "effect", "claim_id"}, path)
        for key in ("location", "text", "effect"):
            require_nonempty_string(claim[key], f"{path}.{key}")
        if claim["claim_match_id"] is not None:
            require_nonempty_string(claim["claim_match_id"], f"{path}.claim_match_id")
        require_enum(claim["category"], CLAIM_CATEGORIES, f"{path}.category")
        require_enum(claim["importance"], CLAIM_IMPORTANCE, f"{path}.importance")
        require_enum(claim["verifiability"], VERIFIABILITY, f"{path}.verifiability")
        require_enum(claim["result"], CLAIM_RESULTS, f"{path}.result")
        require_enum(claim["confidence"], CONFIDENCE, f"{path}.confidence")
        require_list(claim["source_ids"], f"{path}.source_ids")

    issues = require_list(root["issues"], "issues")
    issue_ids = unique_ids(issues, "issue_id", "issues")
    for index, issue in enumerate(issues):
        path = f"issues[{index}]"
        if not re.fullmatch(r"P-[0-9]{3,}", issue["issue_id"]):
            fail(f"{path}.issue_id", "expected P- followed by at least three digits")
        require_keys(issue, {"issue_id", "claim_ids", "summary", "severity", "centrality", "application_risk", "confidence", "rationale"}, path)
        linked_claims = require_list(issue["claim_ids"], f"{path}.claim_ids")
        unknown_claims = set(linked_claims) - claim_ids
        if unknown_claims:
            fail(f"{path}.claim_ids", f"unknown claims: {', '.join(sorted(unknown_claims))}")
        require_nonempty_string(issue["summary"], f"{path}.summary")
        severity = require_enum(issue["severity"], SEVERITIES, f"{path}.severity")
        require_enum(issue["confidence"], CONFIDENCE, f"{path}.confidence")
        require_nonempty_string(issue["rationale"], f"{path}.rationale")
        if severity in {"krytyczne", "duze"}:
            require_enum(issue["centrality"], CENTRALITIES, f"{path}.centrality")
            require_enum(issue["application_risk"], RISKS, f"{path}.application_risk")
        else:
            if issue["centrality"] is not None:
                require_enum(issue["centrality"], CENTRALITIES, f"{path}.centrality")
            if issue["application_risk"] is not None:
                require_enum(issue["application_risk"], RISKS, f"{path}.application_risk")

    validate_issue_counts(root["issue_counts"], issues)
    validate_scores(root["scores"])
    rationales = require_mapping(root["score_rationales"], "score_rationales")
    if set(rationales) != set(DIMENSIONS):
        fail("score_rationales", "must contain exactly A-L")
    for key in DIMENSIONS:
        require_nonempty_string(rationales[key], f"score_rationales.{key}")

    verdict = require_enum(root["verdict"], VERDICTS, "verdict")
    basis = require_list(root["verdict_basis_issue_ids"], "verdict_basis_issue_ids")
    unknown_issues = set(basis) - issue_ids
    if unknown_issues:
        fail("verdict_basis_issue_ids", f"unknown issues: {', '.join(sorted(unknown_issues))}")
    if verdict == "nierzetelny" and not basis:
        fail("verdict_basis_issue_ids", "nierzetelny requires at least one basis issue")
    correction = require_enum(root["counterfactual_correction"], CORRECTIONS, "counterfactual_correction")
    if verdict == "nie_mozna_rozstrzygnac" and correction != "nie_dotyczy":
        fail("counterfactual_correction", "unresolved verdict requires nie_dotyczy")
    require_enum(root["verdict_confidence"], CONFIDENCE, "verdict_confidence")
    require_enum(root["source_coverage"], SOURCE_COVERAGE, "source_coverage")
    require_enum(root["safe_recommendation"], SAFE_RECOMMENDATIONS, "safe_recommendation")
    require_nonempty_string(root["verdict_rationale"], "verdict_rationale")
    require_list(root["limitations"], "limitations")

    sources = require_list(root["sources"], "sources")
    source_ids = unique_ids(sources, "source_id", "sources")
    for index, source in enumerate(sources):
        path = f"sources[{index}]"
        require_keys(source, {"source_id", "title", "url", "accessed_at", "version"}, path)
        for key in ("title", "accessed_at", "version"):
            require_nonempty_string(source[key], f"{path}.{key}")
        require_url(source["url"], f"{path}.url")
    for index, claim in enumerate(claims):
        unknown_sources = set(claim["source_ids"]) - source_ids
        if unknown_sources:
            fail(f"claims[{index}].source_ids", f"unknown sources: {', '.join(sorted(unknown_sources))}")


def validate_extract(data: object) -> None:
    root = require_mapping(data, "root")
    required = {
        "schema_version", "analysis_id", "publication_id", "methodology", "evaluator",
        "material_versions", "claim_count", "scores", "issue_counts", "central_issues",
        "central_findings", "verdict", "verdict_confidence", "source_coverage",
        "counterfactual_correction",
    }
    require_keys(root, required, "root")
    if root["schema_version"] != "0.2-draft":
        fail("schema_version", "expected '0.2-draft'")
    require_nonempty_string(root["analysis_id"], "analysis_id")
    require_nonempty_string(root["publication_id"], "publication_id")
    methodology = require_mapping(root["methodology"], "methodology")
    require_keys(methodology, {"version", "identifier"}, "methodology")
    if methodology["version"] != "0.2-draft":
        fail("methodology.version", "expected '0.2-draft'")
    require_nonempty_string(methodology["identifier"], "methodology.identifier")
    validate_evaluator(root["evaluator"])
    materials = require_list(root["material_versions"], "material_versions")
    if not materials:
        fail("material_versions", "expected at least one material")
    for index, material in enumerate(materials):
        validate_material(material, f"material_versions[{index}]", core_only=True)
    if not any(material["role"] == "tresc_glowna" for material in materials):
        fail("material_versions", "missing tresc_glowna")
    if not isinstance(root["claim_count"], int) or isinstance(root["claim_count"], bool) or root["claim_count"] < 0:
        fail("claim_count", "expected non-negative integer")
    validate_scores(root["scores"])
    validate_issue_counts(root["issue_counts"])
    central_issues = require_list(root["central_issues"], "central_issues")
    for index, issue in enumerate(central_issues):
        path = f"central_issues[{index}]"
        require_keys(issue, {"issue_id", "severity", "centrality", "application_risk", "confidence"}, path)
        if not re.fullmatch(r"P-[0-9]{3,}", require_nonempty_string(issue["issue_id"], f"{path}.issue_id")):
            fail(f"{path}.issue_id", "expected P- followed by at least three digits")
        require_enum(issue["severity"], SEVERITIES, f"{path}.severity")
        require_enum(issue["centrality"], CENTRALITIES, f"{path}.centrality")
        require_enum(issue["application_risk"], RISKS, f"{path}.application_risk")
        require_enum(issue["confidence"], CONFIDENCE, f"{path}.confidence")
    findings = require_list(root["central_findings"], "central_findings")
    if not findings:
        fail("central_findings", "expected at least one finding")
    for index, finding in enumerate(findings):
        require_nonempty_string(finding, f"central_findings[{index}]")
    verdict = require_enum(root["verdict"], VERDICTS, "verdict")
    require_enum(root["verdict_confidence"], CONFIDENCE, "verdict_confidence")
    require_enum(root["source_coverage"], SOURCE_COVERAGE, "source_coverage")
    correction = require_enum(root["counterfactual_correction"], CORRECTIONS, "counterfactual_correction")
    if verdict == "nie_mozna_rozstrzygnac" and correction != "nie_dotyczy":
        fail("counterfactual_correction", "unresolved verdict requires nie_dotyczy")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=("result", "extract"))
    parser.add_argument("json_file", type=Path)
    args = parser.parse_args()
    try:
        with args.json_file.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        if args.kind == "result":
            validate_result(data)
        else:
            validate_extract(data)
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"OK: {args.json_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
