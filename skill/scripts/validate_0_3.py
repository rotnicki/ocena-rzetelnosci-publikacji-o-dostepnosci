#!/usr/bin/env python3
"""Validate JSON outputs for methodology 0.3 draft without external packages."""

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
SEVERITIES = {"krytyczne", "duze", "srednie", "male"}
VERDICTS = {
    "rzetelny", "rzetelny_z_niewielkimi_zastrzezeniami",
    "rzetelny_z_istotnymi_zastrzezeniami", "nierzetelny",
    "nie_mozna_rozstrzygnac",
}
ACCESS = {"tak", "nie", "not_available"}


class ValidationError(Exception):
    pass


def fail(path: str, message: str) -> None:
    raise ValidationError(f"{path}: {message}")


def obj(value: object, path: str) -> dict:
    if not isinstance(value, dict):
        fail(path, "oczekiwano obiektu")
    return value


def array(value: object, path: str) -> list:
    if not isinstance(value, list):
        fail(path, "oczekiwano tablicy")
    return value


def exact(value: dict, keys: set[str], path: str) -> None:
    missing = sorted(keys - set(value))
    extra = sorted(set(value) - keys)
    if missing:
        fail(path, f"brak pól: {', '.join(missing)}")
    if extra:
        fail(path, f"nieoczekiwane pola: {', '.join(extra)}")


def text(value: object, path: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(path, "oczekiwano niepustego tekstu")
    return value


def enum(value: object, allowed: set[str], path: str) -> str:
    if value not in allowed:
        fail(path, f"niedozwolona wartość {value!r}")
    return str(value)


def boolean(value: object, path: str) -> bool:
    if not isinstance(value, bool):
        fail(path, "oczekiwano true albo false")
    return value


def url(value: object, path: str) -> str:
    value = text(value, path)
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        fail(path, "oczekiwano pełnego adresu HTTP(S)")
    return value


def text_array(value: object, path: str, *, nonempty: bool = False) -> list:
    values = array(value, path)
    if nonempty and not values:
        fail(path, "tablica nie może być pusta")
    for index, item in enumerate(values):
        text(item, f"{path}[{index}]")
    return values


def validate_scores(value: object, path: str = "scores") -> dict:
    scores = obj(value, path)
    exact(scores, set(DIMENSIONS), path)
    for key in DIMENSIONS:
        score = scores[key]
        if score != "nd" and (
            not isinstance(score, int) or isinstance(score, bool) or not 0 <= score <= 4
        ):
            fail(f"{path}.{key}", "oczekiwano liczby 0–4 albo 'nd'")
    return scores


def validate_evaluator(value: object, path: str = "evaluator") -> None:
    value = obj(value, path)
    keys = {
        "type", "name", "model_snapshot", "reasoning_setting", "tools",
        "memory_access", "project_access", "private_repository_access",
    }
    exact(value, keys, path)
    enum(value["type"], {"czlowiek", "ai", "zespol"}, f"{path}.type")
    for key in ("name", "model_snapshot", "reasoning_setting"):
        text(value[key], f"{path}.{key}")
    text_array(value["tools"], f"{path}.tools")
    for key in ("memory_access", "project_access", "private_repository_access"):
        enum(value[key], ACCESS, f"{path}.{key}")


def validate_counts(value: object, path: str, issues: list | None = None) -> None:
    value = obj(value, path)
    exact(value, SEVERITIES, path)
    for key, count in value.items():
        if not isinstance(count, int) or isinstance(count, bool) or count < 0:
            fail(f"{path}.{key}", "oczekiwano liczby całkowitej nieujemnej")
    if issues is not None:
        actual = Counter(issue["severity"] for issue in issues)
        for key in SEVERITIES:
            if value[key] != actual[key]:
                fail(f"{path}.{key}", f"zadeklarowano {value[key]}, znaleziono {actual[key]}")


def validate_audience(value: object, path: str = "audience_profile") -> dict:
    value = obj(value, path)
    keys = {
        "basis", "primary_audience", "subgroups", "assumed_knowledge",
        "popularizing_purpose", "core_terms",
        "unexplained_core_terms_block_nonspecialists",
        "expert_assessment_not_user_tested", "rationale",
    }
    exact(value, keys, path)
    enum(value["basis"], {"zadeklarowany", "wywnioskowany", "mieszana"}, f"{path}.basis")
    text(value["primary_audience"], f"{path}.primary_audience")
    text_array(value["subgroups"], f"{path}.subgroups")
    text_array(value["assumed_knowledge"], f"{path}.assumed_knowledge")
    boolean(value["popularizing_purpose"], f"{path}.popularizing_purpose")
    boolean(value["unexplained_core_terms_block_nonspecialists"], f"{path}.unexplained_core_terms_block_nonspecialists")
    if value["expert_assessment_not_user_tested"] is not True:
        fail(f"{path}.expert_assessment_not_user_tested", "wartość musi wynosić true")
    text(value["rationale"], f"{path}.rationale")
    term_keys = {
        "term", "first_use_location", "explained_or_clear_from_context",
        "necessary_for_core", "comprehension_effect",
    }
    for index, term in enumerate(array(value["core_terms"], f"{path}.core_terms")):
        term_path = f"{path}.core_terms[{index}]"
        term = obj(term, term_path)
        exact(term, term_keys, term_path)
        text(term["term"], f"{term_path}.term")
        text(term["first_use_location"], f"{term_path}.first_use_location")
        boolean(term["explained_or_clear_from_context"], f"{term_path}.explained_or_clear_from_context")
        boolean(term["necessary_for_core"], f"{term_path}.necessary_for_core")
        text(term["comprehension_effect"], f"{term_path}.comprehension_effect")
    return value


def validate_language_caps(profile: dict, scores: dict, path: str = "scores") -> None:
    blocked = profile["unexplained_core_terms_block_nonspecialists"]
    if blocked and isinstance(scores["H"], int) and scores["H"] > 2:
        fail(f"{path}.H", "przy blokującym żargonie H nie może przekroczyć 2")
    if profile["popularizing_purpose"] and blocked and isinstance(scores["L"], int) and scores["L"] > 2:
        fail(f"{path}.L", "dla niespełnionej funkcji popularyzatorskiej L nie może przekroczyć 2")


def validate_result(data: object) -> None:
    root = obj(data, "root")
    keys = {
        "schema_version", "analysis_id", "methodology", "publication", "materials",
        "evaluator", "audience_profile", "temporal_assessment", "claim_map_confidence",
        "claim_map_confidence_rationale", "claim_count", "claims", "issues", "issue_counts",
        "scores", "score_rationales", "verdict", "verdict_basis_issue_ids",
        "counterfactual_correction", "verdict_confidence", "source_coverage",
        "safe_recommendation", "verdict_rationale", "limitations", "sources",
    }
    exact(root, keys, "root")
    if root["schema_version"] != "0.3-draft":
        fail("schema_version", "oczekiwano '0.3-draft'")
    text(root["analysis_id"], "analysis_id")

    method = obj(root["methodology"], "methodology")
    exact(method, {"version", "identifier", "frozen_before_critical_pass"}, "methodology")
    if method["version"] != "0.3-draft":
        fail("methodology.version", "oczekiwano '0.3-draft'")
    text(method["identifier"], "methodology.identifier")
    boolean(method["frozen_before_critical_pass"], "methodology.frozen_before_critical_pass")

    publication = obj(root["publication"], "publication")
    publication_keys = {
        "publication_id", "title", "authors", "publisher", "outlet", "url",
        "published_at", "updated_at", "accessed_at", "analyzed_at", "language",
        "publication_type", "full_text",
    }
    exact(publication, publication_keys, "publication")
    for key in ("publication_id", "title", "outlet", "accessed_at", "analyzed_at", "language"):
        text(publication[key], f"publication.{key}")
    if publication["publisher"] is not None:
        text(publication["publisher"], "publication.publisher")
    for key in ("published_at", "updated_at"):
        if publication[key] is not None:
            text(publication[key], f"publication.{key}")
    text_array(publication["authors"], "publication.authors")
    text_array(publication["publication_type"], "publication.publication_type", nonempty=True)
    url(publication["url"], "publication.url")
    enum(publication["full_text"], {"tak", "nie", "czesciowo"}, "publication.full_text")

    material_keys = {"material_id", "role", "url", "accessed_at", "version", "immutable", "scope"}
    materials = array(root["materials"], "materials")
    if not materials:
        fail("materials", "wymagany co najmniej jeden materiał")
    material_ids = set()
    for index, material in enumerate(materials):
        path = f"materials[{index}]"
        material = obj(material, path)
        exact(material, material_keys, path)
        material_id = text(material["material_id"], f"{path}.material_id")
        if material_id in material_ids:
            fail(path, "powtórzony material_id")
        material_ids.add(material_id)
        enum(material["role"], {"tresc_glowna", "material_centralny_zewnetrzny", "material_dodatkowy", "material_wylaczony"}, f"{path}.role")
        url(material["url"], f"{path}.url")
        for key in ("accessed_at", "version", "scope"):
            text(material[key], f"{path}.{key}")
        enum(material["immutable"], ACCESS, f"{path}.immutable")
    if not any(item["role"] == "tresc_glowna" for item in materials):
        fail("materials", "brak materiału o roli tresc_glowna")

    validate_evaluator(root["evaluator"])
    profile = validate_audience(root["audience_profile"])

    temporal = obj(root["temporal_assessment"], "temporal_assessment")
    temporal_keys = {"historical_accuracy", "historical_rationale", "current_applicability", "current_rationale", "material_changes"}
    exact(temporal, temporal_keys, "temporal_assessment")
    temporal_values = {"zgodne", "zasadniczo_zgodne", "czesciowo_zgodne", "mylace", "niezgodne", "nierozstrzygniete", "nie_dotyczy"}
    enum(temporal["historical_accuracy"], temporal_values, "temporal_assessment.historical_accuracy")
    enum(temporal["current_applicability"], temporal_values, "temporal_assessment.current_applicability")
    text(temporal["historical_rationale"], "temporal_assessment.historical_rationale")
    text(temporal["current_rationale"], "temporal_assessment.current_rationale")
    text_array(temporal["material_changes"], "temporal_assessment.material_changes")
    enum(root["claim_map_confidence"], CONFIDENCE, "claim_map_confidence")
    text(root["claim_map_confidence_rationale"], "claim_map_confidence_rationale")

    claim_keys = {
        "claim_id", "claim_match_id", "location", "text", "category", "importance",
        "verifiability", "result", "result_boundary_rationale", "confidence", "source_ids", "effect",
    }
    claims = array(root["claims"], "claims")
    if root["claim_count"] != len(claims):
        fail("claim_count", f"zadeklarowano {root['claim_count']}, znaleziono {len(claims)}")
    claim_ids = set()
    for index, claim in enumerate(claims):
        path = f"claims[{index}]"
        claim = obj(claim, path)
        exact(claim, claim_keys, path)
        claim_id = text(claim["claim_id"], f"{path}.claim_id")
        if not re.fullmatch(r"T-[0-9]{3,}", claim_id) or claim_id in claim_ids:
            fail(f"{path}.claim_id", "oczekiwano unikatowego identyfikatora T-NNN")
        claim_ids.add(claim_id)
        if claim["claim_match_id"] is not None:
            text(claim["claim_match_id"], f"{path}.claim_match_id")
        for key in ("location", "text", "result_boundary_rationale", "effect"):
            text(claim[key], f"{path}.{key}")
        enum(claim["category"], {"F", "P", "S", "T", "B", "Z", "I", "O"}, f"{path}.category")
        enum(claim["importance"], {"kluczowe", "wazne", "pomocnicze"}, f"{path}.importance")
        enum(claim["verifiability"], {"weryfikowalne", "czesciowo_weryfikowalne", "nieweryfikowalne"}, f"{path}.verifiability")
        enum(claim["result"], {"zgodne", "zasadniczo_zgodne", "czesciowo_zgodne", "mylace", "niezgodne", "nieweryfikowalne", "nierozstrzygniete"}, f"{path}.result")
        enum(claim["confidence"], CONFIDENCE, f"{path}.confidence")
        text_array(claim["source_ids"], f"{path}.source_ids")

    issue_keys = {
        "issue_id", "claim_ids", "summary", "proposed_correction", "grouping_rationale",
        "severity", "centrality", "application_risk", "centrality_test",
        "application_risk_test", "confidence", "rationale",
    }
    issues = array(root["issues"], "issues")
    issue_ids = set()
    for index, issue in enumerate(issues):
        path = f"issues[{index}]"
        issue = obj(issue, path)
        exact(issue, issue_keys, path)
        issue_id = text(issue["issue_id"], f"{path}.issue_id")
        if not re.fullmatch(r"P-[0-9]{3,}", issue_id) or issue_id in issue_ids:
            fail(f"{path}.issue_id", "oczekiwano unikatowego identyfikatora P-NNN")
        issue_ids.add(issue_id)
        for key in ("summary", "proposed_correction", "grouping_rationale", "rationale"):
            text(issue[key], f"{path}.{key}")
        refs = text_array(issue["claim_ids"], f"{path}.claim_ids")
        unknown = sorted(set(refs) - claim_ids)
        if unknown:
            fail(f"{path}.claim_ids", f"nieznane twierdzenia: {', '.join(unknown)}")
        severity = enum(issue["severity"], SEVERITIES, f"{path}.severity")
        enum(issue["confidence"], CONFIDENCE, f"{path}.confidence")
        if severity in {"krytyczne", "duze"}:
            enum(issue["centrality"], {"rdzen", "istotne_wsparcie", "element_poboczny"}, f"{path}.centrality")
            enum(issue["application_risk"], {"wysokie", "srednie", "niskie"}, f"{path}.application_risk")
            central = obj(issue["centrality_test"], f"{path}.centrality_test")
            exact(central, {"removal_changes_main_thesis_or_use", "publication_fulfils_purpose_after_removal", "rationale"}, f"{path}.centrality_test")
            boolean(central["removal_changes_main_thesis_or_use"], f"{path}.centrality_test.removal_changes_main_thesis_or_use")
            boolean(central["publication_fulfils_purpose_after_removal"], f"{path}.centrality_test.publication_fulfils_purpose_after_removal")
            text(central["rationale"], f"{path}.centrality_test.rationale")
            risk = obj(issue["application_risk_test"], f"{path}.application_risk_test")
            exact(risk, {"reader_action_likelihood", "impact_severity", "reversibility", "rationale"}, f"{path}.application_risk_test")
            enum(risk["reader_action_likelihood"], {"wysokie", "srednie", "niskie"}, f"{path}.application_risk_test.reader_action_likelihood")
            enum(risk["impact_severity"], {"powazna", "zauwazalna", "ograniczona"}, f"{path}.application_risk_test.impact_severity")
            enum(risk["reversibility"], {"trudna", "umiarkowana", "latwa"}, f"{path}.application_risk_test.reversibility")
            text(risk["rationale"], f"{path}.application_risk_test.rationale")
            if severity == "krytyczne":
                if issue["application_risk"] != "wysokie" or issue["confidence"] != "wysoka":
                    fail(path, "problem krytyczny wymaga wysokiego ryzyka i wysokiej pewności")
                if risk["reader_action_likelihood"] != "wysokie" or risk["impact_severity"] != "powazna":
                    fail(f"{path}.application_risk_test", "problem krytyczny wymaga prawdopodobnego działania i poważnego skutku")
        else:
            if issue["centrality"] is not None:
                enum(issue["centrality"], {"rdzen", "istotne_wsparcie", "element_poboczny"}, f"{path}.centrality")
            if issue["application_risk"] is not None:
                enum(issue["application_risk"], {"wysokie", "srednie", "niskie"}, f"{path}.application_risk")

    validate_counts(root["issue_counts"], "issue_counts", issues)
    scores = validate_scores(root["scores"])
    validate_language_caps(profile, scores)
    rationales = obj(root["score_rationales"], "score_rationales")
    exact(rationales, set(DIMENSIONS), "score_rationales")
    for key in DIMENSIONS:
        text(rationales[key], f"score_rationales.{key}")
    if any(claim["category"] == "T" for claim in claims) and scores["C"] == "nd":
        fail("scores.C", "twierdzenie techniczne wyklucza 'nd'")

    verdict = enum(root["verdict"], VERDICTS, "verdict")
    basis = text_array(root["verdict_basis_issue_ids"], "verdict_basis_issue_ids")
    unknown = sorted(set(basis) - issue_ids)
    if unknown:
        fail("verdict_basis_issue_ids", f"nieznane problemy: {', '.join(unknown)}")
    correction = enum(root["counterfactual_correction"], {"ograniczona", "strukturalna", "nie_dotyczy"}, "counterfactual_correction")
    if verdict == "nierzetelny" and not basis:
        fail("verdict_basis_issue_ids", "werdykt nierzetelny wymaga podstawy")
    if verdict == "nierzetelny" and all(
        next(issue for issue in issues if issue["issue_id"] == issue_id)["confidence"] == "niska"
        for issue_id in basis
    ):
        fail("verdict_basis_issue_ids", "problemy o wyłącznie niskiej pewności nie mogą przesądzić o nierzetelności")
    if verdict in {"rzetelny", "rzetelny_z_niewielkimi_zastrzezeniami"} and (
        root["issue_counts"]["krytyczne"] or root["issue_counts"]["duze"]
    ):
        fail("verdict", "ten werdykt nie może współistnieć z problemem dużym lub krytycznym")
    if verdict == "nie_mozna_rozstrzygnac" and correction != "nie_dotyczy":
        fail("counterfactual_correction", "dla tego werdyktu wymagane jest nie_dotyczy")
    enum(root["verdict_confidence"], CONFIDENCE, "verdict_confidence")
    enum(root["source_coverage"], {"pelne", "wystarczajace", "czesciowe", "niewystarczajace"}, "source_coverage")
    enum(root["safe_recommendation"], {"bez_zastrzezen", "z_niewielkimi_korektami", "z_nazwanymi_korektami_lub_zrodlami", "nie_do_praktycznego_uzycia", "nie_mozna_ocenic"}, "safe_recommendation")
    text(root["verdict_rationale"], "verdict_rationale")
    text_array(root["limitations"], "limitations")

    source_keys = {"source_id", "title", "url", "accessed_at", "version"}
    source_ids = set()
    for index, source in enumerate(array(root["sources"], "sources")):
        path = f"sources[{index}]"
        source = obj(source, path)
        exact(source, source_keys, path)
        source_id = text(source["source_id"], f"{path}.source_id")
        if source_id in source_ids:
            fail(path, "powtórzony source_id")
        source_ids.add(source_id)
        for key in ("title", "accessed_at", "version"):
            text(source[key], f"{path}.{key}")
        url(source["url"], f"{path}.url")
    for index, claim in enumerate(claims):
        unknown = sorted(set(claim["source_ids"]) - source_ids)
        if unknown:
            fail(f"claims[{index}].source_ids", f"nieznane źródła: {', '.join(unknown)}")


def validate_extract(data: object) -> None:
    root = obj(data, "root")
    keys = {
        "schema_version", "analysis_id", "publication_id", "methodology", "evaluator",
        "material_versions", "audience_language", "claim_count", "claim_map_confidence",
        "scores", "issue_counts", "central_issues", "central_findings", "verdict",
        "verdict_confidence", "source_coverage", "counterfactual_correction",
    }
    exact(root, keys, "root")
    if root["schema_version"] != "0.3-draft":
        fail("schema_version", "oczekiwano '0.3-draft'")
    text(root["analysis_id"], "analysis_id")
    text(root["publication_id"], "publication_id")
    method = obj(root["methodology"], "methodology")
    exact(method, {"version", "identifier"}, "methodology")
    if method["version"] != "0.3-draft":
        fail("methodology.version", "oczekiwano '0.3-draft'")
    text(method["identifier"], "methodology.identifier")
    validate_evaluator(root["evaluator"])
    material_keys = {"material_id", "role", "url", "version"}
    materials = array(root["material_versions"], "material_versions")
    if not materials:
        fail("material_versions", "wymagany co najmniej jeden materiał")
    for index, material in enumerate(materials):
        path = f"material_versions[{index}]"
        material = obj(material, path)
        exact(material, material_keys, path)
        text(material["material_id"], f"{path}.material_id")
        enum(material["role"], {"tresc_glowna", "material_centralny_zewnetrzny"}, f"{path}.role")
        url(material["url"], f"{path}.url")
        text(material["version"], f"{path}.version")
    audience = obj(root["audience_language"], "audience_language")
    exact(audience, {"primary_audience", "popularizing_purpose", "unexplained_core_terms_block_nonspecialists"}, "audience_language")
    text(audience["primary_audience"], "audience_language.primary_audience")
    boolean(audience["popularizing_purpose"], "audience_language.popularizing_purpose")
    boolean(audience["unexplained_core_terms_block_nonspecialists"], "audience_language.unexplained_core_terms_block_nonspecialists")
    if not isinstance(root["claim_count"], int) or isinstance(root["claim_count"], bool) or root["claim_count"] < 0:
        fail("claim_count", "oczekiwano liczby całkowitej nieujemnej")
    enum(root["claim_map_confidence"], CONFIDENCE, "claim_map_confidence")
    scores = validate_scores(root["scores"])
    validate_language_caps(audience, scores)
    validate_counts(root["issue_counts"], "issue_counts")
    issue_keys = {"issue_id", "severity", "centrality", "application_risk", "confidence"}
    for index, issue in enumerate(array(root["central_issues"], "central_issues")):
        path = f"central_issues[{index}]"
        issue = obj(issue, path)
        exact(issue, issue_keys, path)
        if not re.fullmatch(r"P-[0-9]{3,}", text(issue["issue_id"], f"{path}.issue_id")):
            fail(f"{path}.issue_id", "oczekiwano P-NNN")
        severity = enum(issue["severity"], SEVERITIES, f"{path}.severity")
        enum(issue["centrality"], {"rdzen", "istotne_wsparcie", "element_poboczny"}, f"{path}.centrality")
        enum(issue["application_risk"], {"wysokie", "srednie", "niskie"}, f"{path}.application_risk")
        enum(issue["confidence"], CONFIDENCE, f"{path}.confidence")
        if severity == "krytyczne" and (
            issue["application_risk"] != "wysokie" or issue["confidence"] != "wysoka"
        ):
            fail(path, "problem krytyczny wymaga wysokiego ryzyka i wysokiej pewności")
    text_array(root["central_findings"], "central_findings", nonempty=True)
    enum(root["verdict"], VERDICTS, "verdict")
    enum(root["verdict_confidence"], CONFIDENCE, "verdict_confidence")
    enum(root["source_coverage"], {"pelne", "wystarczajace", "czesciowe", "niewystarczajace"}, "source_coverage")
    enum(root["counterfactual_correction"], {"ograniczona", "strukturalna", "nie_dotyczy"}, "counterfactual_correction")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("result", "extract"))
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        with args.path.open(encoding="utf-8") as source:
            data = json.load(source)
        (validate_result if args.kind == "result" else validate_extract)(data)
    except (OSError, json.JSONDecodeError, ValidationError) as error:
        print(f"BŁĄD: {error}", file=sys.stderr)
        return 1
    print(f"OK: {args.path} ({args.kind}, 0.3-draft)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
