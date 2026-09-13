#!/usr/bin/env python3
"""Validate methodology 0.3 draft outputs without external packages."""

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
CENTRALITIES = {"rdzen", "istotne_wsparcie", "element_poboczny"}
RISKS = {"wysokie", "srednie", "niskie"}
CLAIM_RESULTS = {
    "zgodne", "zasadniczo_zgodne", "czesciowo_zgodne", "mylace",
    "niezgodne", "nieweryfikowalne", "nierozstrzygniete",
}
VERDICTS = {
    "rzetelny", "rzetelny_z_niewielkimi_zastrzezeniami",
    "rzetelny_z_istotnymi_zastrzezeniami", "nierzetelny",
    "nie_mozna_rozstrzygnac",
}
ACCESS = {"tak", "nie", "not_available"}
CONTEXT_KINDS = {
    "homepage", "about_page", "blog_or_newsletter_description", "newsletter_signup_page",
    "category_or_series_description", "editorial_policy", "author_profile", "publication_promotion",
    "article_reader_cues", "actually_required_knowledge",
}
RELATIONS = {
    "one_to_one", "one_to_many", "many_to_one", "many_to_many", "a_only", "b_only",
}


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


def nullable_text(value: object, path: str) -> None:
    if value is not None:
        text(value, path)


def enum(value: object, allowed: set[str], path: str) -> str:
    if value not in allowed:
        fail(path, f"niedozwolona wartość {value!r}")
    return str(value)


def boolean(value: object, path: str) -> bool:
    if not isinstance(value, bool):
        fail(path, "oczekiwano true albo false")
    return value


def integer(value: object, path: str, minimum: int = 0, maximum: int | None = None) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
        fail(path, f"oczekiwano liczby całkowitej >= {minimum}")
    if maximum is not None and value > maximum:
        fail(path, f"oczekiwano liczby całkowitej <= {maximum}")
    return value


def number(value: object, path: str, minimum: float = 0, maximum: float = 1) -> float:
    if not isinstance(value, (int, float)) or isinstance(value, bool) or not minimum <= value <= maximum:
        fail(path, f"oczekiwano liczby {minimum}–{maximum}")
    return float(value)


def url(value: object, path: str) -> str:
    value = text(value, path)
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        fail(path, "oczekiwano pełnego adresu HTTP(S)")
    return value


def text_array(value: object, path: str, *, nonempty: bool = False, unique: bool = False) -> list[str]:
    values = array(value, path)
    if nonempty and not values:
        fail(path, "tablica nie może być pusta")
    for index, item in enumerate(values):
        text(item, f"{path}[{index}]")
    if unique and len(values) != len(set(values)):
        fail(path, "wartości muszą być unikatowe")
    return values


def validate_scores(value: object, path: str = "scores") -> dict:
    scores = obj(value, path)
    exact(scores, set(DIMENSIONS), path)
    for key in DIMENSIONS:
        score = scores[key]
        if score != "nd":
            integer(score, f"{path}.{key}", 0, 4)
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
        integer(count, f"{path}.{key}")
    if issues is not None:
        actual = Counter(issue["severity"] for issue in issues)
        for key in SEVERITIES:
            if value[key] != actual[key]:
                fail(f"{path}.{key}", f"zadeklarowano {value[key]}, znaleziono {actual[key]}")


def validate_publication_context(value: object, path: str = "publication_context") -> tuple[dict, set[str]]:
    value = obj(value, path)
    keys = {
        "outlet_type", "outlet_declared_purpose", "declared_audiences",
        "reasonably_foreseeable_audiences", "additional_relevant_audiences",
        "article_audiences", "declared_required_knowledge", "actually_required_knowledge",
        "evidence", "checked_context_elements", "conflicts", "profile_status",
        "profile_confidence", "confidence_rationale", "audience_variants",
    }
    exact(value, keys, path)
    evidence_ids: set[str] = set()
    evidence_keys = {"evidence_id", "rank", "kind", "url", "location", "accessed_at", "excerpt_or_paraphrase"}
    for index, item in enumerate(array(value["evidence"], f"{path}.evidence")):
        item_path = f"{path}.evidence[{index}]"
        item = obj(item, item_path)
        exact(item, evidence_keys, item_path)
        evidence_id = text(item["evidence_id"], f"{item_path}.evidence_id")
        if not re.fullmatch(r"AUD-[0-9]{3,}", evidence_id) or evidence_id in evidence_ids:
            fail(f"{item_path}.evidence_id", "oczekiwano unikatowego identyfikatora AUD-NNN")
        evidence_ids.add(evidence_id)
        integer(item["rank"], f"{item_path}.rank", 1, 5)
        for key in ("kind", "location", "accessed_at", "excerpt_or_paraphrase"):
            text(item[key], f"{item_path}.{key}")
        url(item["url"], f"{item_path}.url")

    checked = array(value["checked_context_elements"], f"{path}.checked_context_elements")
    if len(checked) != len(CONTEXT_KINDS):
        fail(f"{path}.checked_context_elements", "wymagane dokładnie 10 elementów kontekstu")
    seen_kinds = set()
    checked_keys = {"kind", "status", "url", "location", "accessed_at", "note"}
    for index, item in enumerate(checked):
        item_path = f"{path}.checked_context_elements[{index}]"
        item = obj(item, item_path)
        exact(item, checked_keys, item_path)
        kind = enum(item["kind"], CONTEXT_KINDS, f"{item_path}.kind")
        if kind in seen_kinds:
            fail(f"{item_path}.kind", "rodzaj elementu występuje więcej niż raz")
        seen_kinds.add(kind)
        status = enum(item["status"], {"sprawdzono", "niedostepne", "nie_odnaleziono", "nie_dotyczy"}, f"{item_path}.status")
        if item["url"] is not None:
            url(item["url"], f"{item_path}.url")
        nullable_text(item["location"], f"{item_path}.location")
        nullable_text(item["accessed_at"], f"{item_path}.accessed_at")
        text(item["note"], f"{item_path}.note")
        if status == "sprawdzono" and (item["url"] is None or item["accessed_at"] is None):
            fail(item_path, "stan sprawdzono wymaga URL i daty dostępu")
    if seen_kinds != CONTEXT_KINDS:
        fail(f"{path}.checked_context_elements", "każdy z 10 rodzajów musi wystąpić dokładnie raz")

    def refs(field: object, field_path: str) -> list[str]:
        identifiers = text_array(field, field_path, unique=True)
        unknown = sorted(set(identifiers) - evidence_ids)
        if unknown:
            fail(field_path, f"nieznane dowody: {', '.join(unknown)}")
        return identifiers

    for key in ("outlet_type", "outlet_declared_purpose"):
        item = obj(value[key], f"{path}.{key}")
        exact(item, {"value", "evidence_ids"}, f"{path}.{key}")
        text(item["value"], f"{path}.{key}.value")
        if not refs(item["evidence_ids"], f"{path}.{key}.evidence_ids"):
            fail(f"{path}.{key}.evidence_ids", "ustalenie wymaga co najmniej jednego dowodu")
    for key in (
        "declared_audiences", "reasonably_foreseeable_audiences", "additional_relevant_audiences",
        "article_audiences", "declared_required_knowledge", "actually_required_knowledge",
    ):
        item = obj(value[key], f"{path}.{key}")
        exact(item, {"values", "evidence_ids"}, f"{path}.{key}")
        values = text_array(item["values"], f"{path}.{key}.values")
        identifiers = refs(item["evidence_ids"], f"{path}.{key}.evidence_ids")
        if values and not identifiers:
            fail(f"{path}.{key}.evidence_ids", "niepuste ustalenie wymaga co najmniej jednego dowodu")

    for index, conflict in enumerate(array(value["conflicts"], f"{path}.conflicts")):
        item_path = f"{path}.conflicts[{index}]"
        conflict = obj(conflict, item_path)
        exact(conflict, {"summary", "evidence_ids"}, item_path)
        text(conflict["summary"], f"{item_path}.summary")
        refs(conflict["evidence_ids"], f"{item_path}.evidence_ids")
    status = enum(value["profile_status"], {"ustalony", "czesciowo_ustalony", "nieustalony_wiarygodnie"}, f"{path}.profile_status")
    confidence = enum(value["profile_confidence"], CONFIDENCE, f"{path}.profile_confidence")
    text(value["confidence_rationale"], f"{path}.confidence_rationale")
    variants = array(value["audience_variants"], f"{path}.audience_variants")
    variant_keys = {"description", "evidence_ids", "h_score", "l_score", "rationale"}
    for index, variant in enumerate(variants):
        item_path = f"{path}.audience_variants[{index}]"
        variant = obj(variant, item_path)
        exact(variant, variant_keys, item_path)
        text(variant["description"], f"{item_path}.description")
        refs(variant["evidence_ids"], f"{item_path}.evidence_ids")
        integer(variant["h_score"], f"{item_path}.h_score", 0, 4)
        integer(variant["l_score"], f"{item_path}.l_score", 0, 4)
        text(variant["rationale"], f"{item_path}.rationale")
    if status == "nieustalony_wiarygodnie":
        if confidence != "niska":
            fail(f"{path}.profile_confidence", "nieustalony profil wymaga niskiej pewności")
        if len(variants) < 2:
            fail(f"{path}.audience_variants", "nieustalony profil wymaga co najmniej dwóch wariantów")
    return value, evidence_ids


def validate_audience(value: object, evidence_ids: set[str], path: str = "audience_profile") -> dict:
    value = obj(value, path)
    keys = {
        "basis", "primary_audience", "subgroups", "assumed_knowledge", "popularizing_purpose",
        "core_terms", "unexplained_core_terms_block_nonspecialists",
        "core_requires_undisclosed_specialist_knowledge", "core_unrecoverable_without_expert",
        "group_comprehension", "lowest_significant_group_score",
        "expert_assessment_not_user_tested", "rationale",
    }
    exact(value, keys, path)
    enum(value["basis"], {"zadeklarowany", "wywnioskowany", "mieszana"}, f"{path}.basis")
    text(value["primary_audience"], f"{path}.primary_audience")
    text_array(value["subgroups"], f"{path}.subgroups")
    text_array(value["assumed_knowledge"], f"{path}.assumed_knowledge")
    for key in (
        "popularizing_purpose", "unexplained_core_terms_block_nonspecialists",
        "core_requires_undisclosed_specialist_knowledge", "core_unrecoverable_without_expert",
    ):
        boolean(value[key], f"{path}.{key}")
    if value["expert_assessment_not_user_tested"] is not True:
        fail(f"{path}.expert_assessment_not_user_tested", "wartość musi wynosić true")
    text(value["rationale"], f"{path}.rationale")
    term_keys = {"term", "first_use_location", "explained_or_clear_from_context", "necessary_for_core", "comprehension_effect"}
    for index, term in enumerate(array(value["core_terms"], f"{path}.core_terms")):
        item_path = f"{path}.core_terms[{index}]"
        term = obj(term, item_path)
        exact(term, term_keys, item_path)
        for key in ("term", "first_use_location", "comprehension_effect"):
            text(term[key], f"{item_path}.{key}")
        boolean(term["explained_or_clear_from_context"], f"{item_path}.explained_or_clear_from_context")
        boolean(term["necessary_for_core"], f"{item_path}.necessary_for_core")
    group_keys = {"audience", "significant", "included_in_article_promise", "scope_rationale", "group_h_score", "assumptions", "barriers", "evidence_ids"}
    groups = array(value["group_comprehension"], f"{path}.group_comprehension")
    if not groups:
        fail(f"{path}.group_comprehension", "wymagana co najmniej jedna grupa")
    included_scores = []
    for index, group in enumerate(groups):
        item_path = f"{path}.group_comprehension[{index}]"
        group = obj(group, item_path)
        exact(group, group_keys, item_path)
        text(group["audience"], f"{item_path}.audience")
        significant = boolean(group["significant"], f"{item_path}.significant")
        included = boolean(group["included_in_article_promise"], f"{item_path}.included_in_article_promise")
        text(group["scope_rationale"], f"{item_path}.scope_rationale")
        h_score = integer(group["group_h_score"], f"{item_path}.group_h_score", 0, 4)
        text_array(group["assumptions"], f"{item_path}.assumptions")
        text_array(group["barriers"], f"{item_path}.barriers")
        refs = text_array(group["evidence_ids"], f"{item_path}.evidence_ids", unique=True)
        unknown = sorted(set(refs) - evidence_ids)
        if unknown:
            fail(f"{item_path}.evidence_ids", f"nieznane dowody: {', '.join(unknown)}")
        if included and not significant:
            fail(item_path, "grupa objęta obietnicą musi być oznaczona jako istotna")
        if significant and not refs:
            fail(f"{item_path}.evidence_ids", "istotna grupa wymaga dowodu")
        if significant and included:
            included_scores.append(h_score)
    if not included_scores:
        fail(f"{path}.group_comprehension", "co najmniej jedna istotna grupa musi być objęta obietnicą artykułu")
    lowest = integer(value["lowest_significant_group_score"], f"{path}.lowest_significant_group_score", 0, 4)
    if lowest != min(included_scores):
        fail(f"{path}.lowest_significant_group_score", f"oczekiwano minimum {min(included_scores)}")
    return value


def validate_language_caps(profile: dict, scores: dict, path: str = "scores") -> None:
    if scores["H"] == "nd" or scores["L"] == "nd":
        fail(path, "po ustaleniu grup H i L muszą mieć oceny liczbowe")
    if scores["H"] != profile["lowest_significant_group_score"]:
        fail(f"{path}.H", "musi równać się minimum H istotnych grup objętych obietnicą")
    if profile["unexplained_core_terms_block_nonspecialists"] and scores["H"] > 2:
        fail(f"{path}.H", "blokujące niewyjaśnione terminy ograniczają H do 2")
    if profile["core_unrecoverable_without_expert"] and scores["H"] > 1:
        fail(f"{path}.H", "rdzeń nieodtwarzalny bez eksperta ogranicza H do 1")
    if profile["popularizing_purpose"] and profile["core_requires_undisclosed_specialist_knowledge"] and scores["L"] > 2:
        fail(f"{path}.L", "niespełniona funkcja popularyzatorska ogranicza L do 2")


def validate_temporal(value: object, publication: dict, material_ids: set[str], path: str = "temporal_assessment") -> None:
    value = obj(value, path)
    keys = {
        "historical_accuracy", "historical_rationale", "original_version_available",
        "assessed_historical_version", "version_evidence_ids", "historical_confidence",
        "current_applicability", "current_rationale", "current_version_basis", "material_changes",
    }
    exact(value, keys, path)
    enum(value["historical_accuracy"], CLAIM_RESULTS, f"{path}.historical_accuracy")
    enum(value["current_applicability"], CLAIM_RESULTS, f"{path}.current_applicability")
    for key in ("historical_rationale", "current_rationale", "current_version_basis"):
        text(value[key], f"{path}.{key}")
    original = boolean(value["original_version_available"], f"{path}.original_version_available")
    assessed = enum(value["assessed_historical_version"], {"original", "archived_update", "current_after_update", "not_reconstructable"}, f"{path}.assessed_historical_version")
    version_evidence_ids = text_array(value["version_evidence_ids"], f"{path}.version_evidence_ids", unique=True)
    unknown = sorted(set(version_evidence_ids) - material_ids)
    if unknown:
        fail(f"{path}.version_evidence_ids", f"nieznane materiały: {', '.join(unknown)}")
    confidence = enum(value["historical_confidence"], CONFIDENCE, f"{path}.historical_confidence")
    text_array(value["material_changes"], f"{path}.material_changes")
    if original and assessed != "original":
        fail(f"{path}.assessed_historical_version", "dostępna wersja pierwotna wymaga wartości original")
    if publication["updated_at"] is not None and not original:
        if assessed != "not_reconstructable" or value["historical_accuracy"] != "nierozstrzygniete":
            fail(path, "brak wersji pierwotnej strony aktualizowanej wymaga not_reconstructable i nierozstrzygniete")
    if assessed in {"archived_update", "current_after_update"} and confidence == "wysoka":
        fail(f"{path}.historical_confidence", "stan bez niezmiennej wersji pierwotnej nie może mieć wysokiej pewności")


def validate_full_test(issue: dict, path: str) -> None:
    central = obj(issue["centrality_test"], f"{path}.centrality_test")
    central_keys = {
        "minimal_honest_repair", "repair_changes_main_thesis_or_use",
        "publication_fulfils_purpose_after_repair", "content_removal_required", "rationale",
    }
    exact(central, central_keys, f"{path}.centrality_test")
    text(central["minimal_honest_repair"], f"{path}.centrality_test.minimal_honest_repair")
    for key in ("repair_changes_main_thesis_or_use", "publication_fulfils_purpose_after_repair", "content_removal_required"):
        boolean(central[key], f"{path}.centrality_test.{key}")
    text(central["rationale"], f"{path}.centrality_test.rationale")
    risk = obj(issue["application_risk_test"], f"{path}.application_risk_test")
    exact(risk, {"reader_action_likelihood", "impact_severity", "reversibility", "rationale"}, f"{path}.application_risk_test")
    enum(risk["reader_action_likelihood"], RISKS, f"{path}.application_risk_test.reader_action_likelihood")
    enum(risk["impact_severity"], {"powazna", "zauwazalna", "ograniczona"}, f"{path}.application_risk_test.impact_severity")
    enum(risk["reversibility"], {"trudna", "umiarkowana", "latwa"}, f"{path}.application_risk_test.reversibility")
    text(risk["rationale"], f"{path}.application_risk_test.rationale")


def validate_result(data: object) -> None:
    root = obj(data, "root")
    keys = {
        "schema_version", "analysis_id", "calibration_mode", "methodology", "publication", "materials",
        "evaluator", "publication_context", "audience_profile", "temporal_assessment", "claim_map_confidence",
        "claim_map_confidence_rationale", "claim_count", "claims", "issues", "issue_counts", "scores",
        "score_rationales", "verdict", "verdict_basis_issue_ids", "counterfactual_correction",
        "verdict_confidence", "source_coverage", "safe_recommendation", "verdict_rationale", "limitations", "sources",
    }
    exact(root, keys, "root")
    if root["schema_version"] != "0.3-draft":
        fail("schema_version", "oczekiwano '0.3-draft'")
    text(root["analysis_id"], "analysis_id")
    calibration = boolean(root["calibration_mode"], "calibration_mode")
    method = obj(root["methodology"], "methodology")
    exact(method, {"version", "identifier", "frozen_before_critical_pass"}, "methodology")
    if method["version"] != "0.3-draft" or method["frozen_before_critical_pass"] is not True:
        fail("methodology", "wymagana zamrożona metodologia 0.3-draft")
    text(method["identifier"], "methodology.identifier")

    publication = obj(root["publication"], "publication")
    publication_keys = {"publication_id", "title", "authors", "publisher", "outlet", "url", "published_at", "updated_at", "accessed_at", "analyzed_at", "language", "publication_type", "full_text"}
    exact(publication, publication_keys, "publication")
    for key in ("publication_id", "title", "outlet", "accessed_at", "analyzed_at", "language"):
        text(publication[key], f"publication.{key}")
    nullable_text(publication["publisher"], "publication.publisher")
    nullable_text(publication["published_at"], "publication.published_at")
    nullable_text(publication["updated_at"], "publication.updated_at")
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
            fail(f"{path}.material_id", "powtórzony identyfikator")
        material_ids.add(material_id)
        enum(material["role"], {"tresc_glowna", "material_centralny_zewnetrzny", "material_dodatkowy", "material_wylaczony"}, f"{path}.role")
        url(material["url"], f"{path}.url")
        for key in ("accessed_at", "version", "scope"):
            text(material[key], f"{path}.{key}")
        enum(material["immutable"], ACCESS, f"{path}.immutable")
    if not any(item["role"] == "tresc_glowna" for item in materials):
        fail("materials", "brak treści głównej")
    validate_evaluator(root["evaluator"])
    _context, evidence_ids = validate_publication_context(root["publication_context"])
    profile = validate_audience(root["audience_profile"], evidence_ids)
    validate_temporal(root["temporal_assessment"], publication, material_ids)
    enum(root["claim_map_confidence"], CONFIDENCE, "claim_map_confidence")
    text(root["claim_map_confidence_rationale"], "claim_map_confidence_rationale")

    source_keys = {"source_id", "title", "url", "accessed_at", "version"}
    source_ids = set()
    for index, source in enumerate(array(root["sources"], "sources")):
        path = f"sources[{index}]"
        source = obj(source, path)
        exact(source, source_keys, path)
        source_id = text(source["source_id"], f"{path}.source_id")
        if source_id in source_ids:
            fail(f"{path}.source_id", "powtórzony identyfikator")
        source_ids.add(source_id)
        for key in ("title", "accessed_at", "version"):
            text(source[key], f"{path}.{key}")
        url(source["url"], f"{path}.url")

    claim_keys = {
        "claim_id", "claim_match_id", "location", "text", "atomization_rationale", "extraction_trace",
        "category", "importance", "verifiability", "result", "result_boundary_rationale", "confidence", "source_ids", "effect",
    }
    claims = array(root["claims"], "claims")
    integer(root["claim_count"], "claim_count")
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
        nullable_text(claim["claim_match_id"], f"{path}.claim_match_id")
        for key in ("location", "text", "atomization_rationale", "result_boundary_rationale", "effect"):
            text(claim[key], f"{path}.{key}")
        enum(claim["category"], {"F", "P", "S", "T", "B", "Z", "I", "O"}, f"{path}.category")
        enum(claim["importance"], {"kluczowe", "wazne", "pomocnicze"}, f"{path}.importance")
        enum(claim["verifiability"], {"weryfikowalne", "czesciowo_weryfikowalne", "nieweryfikowalne"}, f"{path}.verifiability")
        enum(claim["result"], CLAIM_RESULTS, f"{path}.result")
        enum(claim["confidence"], CONFIDENCE, f"{path}.confidence")
        claim_source_ids = text_array(claim["source_ids"], f"{path}.source_ids", unique=True)
        unknown = sorted(set(claim_source_ids) - source_ids)
        if unknown:
            fail(f"{path}.source_ids", f"nieznane źródła: {', '.join(unknown)}")
        trace = obj(claim["extraction_trace"], f"{path}.extraction_trace")
        trace_keys = {"publication_fragment_or_location", "source_value_code_or_content", "paraphrase", "verification_source_ids", "result"}
        exact(trace, trace_keys, f"{path}.extraction_trace")
        for key in ("publication_fragment_or_location", "source_value_code_or_content", "paraphrase"):
            text(trace[key], f"{path}.extraction_trace.{key}")
        if trace["paraphrase"] != claim["text"] or trace["result"] != claim["result"]:
            fail(f"{path}.extraction_trace", "parafraza i wynik muszą odpowiadać głównym polom twierdzenia")
        trace_sources = text_array(trace["verification_source_ids"], f"{path}.extraction_trace.verification_source_ids", unique=True)
        if set(trace_sources) != set(claim_source_ids):
            fail(f"{path}.extraction_trace.verification_source_ids", "lista musi odpowiadać source_ids twierdzenia")

    issue_keys = {
        "issue_id", "claim_ids", "summary", "proposed_correction", "grouping_rationale", "severity",
        "centrality", "centrality_rationale", "application_risk", "application_risk_rationale",
        "centrality_test", "application_risk_test", "confidence", "rationale",
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
        refs = text_array(issue["claim_ids"], f"{path}.claim_ids", unique=True)
        unknown = sorted(set(refs) - claim_ids)
        if unknown:
            fail(f"{path}.claim_ids", f"nieznane twierdzenia: {', '.join(unknown)}")
        severity = enum(issue["severity"], SEVERITIES, f"{path}.severity")
        enum(issue["confidence"], CONFIDENCE, f"{path}.confidence")
        full_required = severity in {"krytyczne", "duze"}
        if calibration or full_required:
            enum(issue["centrality"], CENTRALITIES, f"{path}.centrality")
            enum(issue["application_risk"], RISKS, f"{path}.application_risk")
            text(issue["centrality_rationale"], f"{path}.centrality_rationale")
            text(issue["application_risk_rationale"], f"{path}.application_risk_rationale")
        else:
            if issue["centrality"] is not None:
                enum(issue["centrality"], CENTRALITIES, f"{path}.centrality")
            if issue["application_risk"] is not None:
                enum(issue["application_risk"], RISKS, f"{path}.application_risk")
            nullable_text(issue["centrality_rationale"], f"{path}.centrality_rationale")
            nullable_text(issue["application_risk_rationale"], f"{path}.application_risk_rationale")
        if full_required:
            validate_full_test(issue, path)
        else:
            if (issue["centrality_test"] is None) != (issue["application_risk_test"] is None):
                fail(path, "pełne testy centralności i ryzyka podaje się razem")
            if issue["centrality_test"] is not None:
                validate_full_test(issue, path)
        if severity == "krytyczne":
            risk = issue["application_risk_test"]
            if issue["application_risk"] != "wysokie" or issue["confidence"] != "wysoka":
                fail(path, "problem krytyczny wymaga wysokiego ryzyka i wysokiej pewności")
            if risk["reader_action_likelihood"] != "wysokie" or risk["impact_severity"] != "powazna":
                fail(f"{path}.application_risk_test", "problem krytyczny wymaga prawdopodobnego działania i poważnego skutku")

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
    basis = text_array(root["verdict_basis_issue_ids"], "verdict_basis_issue_ids", unique=True)
    unknown = sorted(set(basis) - issue_ids)
    if unknown:
        fail("verdict_basis_issue_ids", f"nieznane problemy: {', '.join(unknown)}")
    correction = enum(root["counterfactual_correction"], {"ograniczona", "strukturalna", "nie_dotyczy"}, "counterfactual_correction")
    if verdict == "nierzetelny" and not basis:
        fail("verdict_basis_issue_ids", "werdykt nierzetelny wymaga podstawy")
    if verdict == "nierzetelny" and all(next(item for item in issues if item["issue_id"] == issue_id)["confidence"] == "niska" for issue_id in basis):
        fail("verdict_basis_issue_ids", "problemy o wyłącznie niskiej pewności nie mogą przesądzić o nierzetelności")
    if verdict in {"rzetelny", "rzetelny_z_niewielkimi_zastrzezeniami"} and (root["issue_counts"]["krytyczne"] or root["issue_counts"]["duze"]):
        fail("verdict", "ten werdykt nie może współistnieć z problemem dużym lub krytycznym")
    if verdict == "nie_mozna_rozstrzygnac" and correction != "nie_dotyczy":
        fail("counterfactual_correction", "dla tego werdyktu wymagane jest nie_dotyczy")
    enum(root["verdict_confidence"], CONFIDENCE, "verdict_confidence")
    enum(root["source_coverage"], {"pelne", "wystarczajace", "czesciowe", "niewystarczajace"}, "source_coverage")
    enum(root["safe_recommendation"], {"bez_zastrzezen", "z_niewielkimi_korektami", "z_nazwanymi_korektami_lub_zrodlami", "nie_do_praktycznego_uzycia", "nie_mozna_ocenic"}, "safe_recommendation")
    text(root["verdict_rationale"], "verdict_rationale")
    text_array(root["limitations"], "limitations")


def validate_extract(data: object) -> None:
    root = obj(data, "root")
    keys = {
        "schema_version", "analysis_id", "publication_id", "methodology", "evaluator", "material_versions",
        "publication_context_summary", "audience_language", "claim_count", "claim_map_confidence", "scores",
        "issue_counts", "issues", "central_findings", "verdict", "verdict_confidence", "source_coverage",
        "counterfactual_correction",
    }
    exact(root, keys, "root")
    if root["schema_version"] != "0.3-draft":
        fail("schema_version", "oczekiwano '0.3-draft'")
    for key in ("analysis_id", "publication_id"):
        text(root[key], key)
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
    context = obj(root["publication_context_summary"], "publication_context_summary")
    exact(context, {"outlet_type", "outlet_declared_purpose", "declared_audiences", "article_audiences", "actually_required_knowledge", "conflicts", "profile_status", "profile_confidence"}, "publication_context_summary")
    for key in ("outlet_type", "outlet_declared_purpose"):
        text(context[key], f"publication_context_summary.{key}")
    for key in ("declared_audiences", "article_audiences", "actually_required_knowledge", "conflicts"):
        text_array(context[key], f"publication_context_summary.{key}")
    enum(context["profile_status"], {"ustalony", "czesciowo_ustalony", "nieustalony_wiarygodnie"}, "publication_context_summary.profile_status")
    enum(context["profile_confidence"], CONFIDENCE, "publication_context_summary.profile_confidence")
    audience = obj(root["audience_language"], "audience_language")
    audience_keys = {"primary_audience", "popularizing_purpose", "unexplained_core_terms_block_nonspecialists", "core_requires_undisclosed_specialist_knowledge", "core_unrecoverable_without_expert", "group_scores"}
    exact(audience, audience_keys, "audience_language")
    text(audience["primary_audience"], "audience_language.primary_audience")
    for key in ("popularizing_purpose", "unexplained_core_terms_block_nonspecialists", "core_requires_undisclosed_specialist_knowledge", "core_unrecoverable_without_expert"):
        boolean(audience[key], f"audience_language.{key}")
    group_scores = array(audience["group_scores"], "audience_language.group_scores")
    if not group_scores:
        fail("audience_language.group_scores", "wymagana co najmniej jedna grupa")
    included_scores = []
    for index, group in enumerate(group_scores):
        path = f"audience_language.group_scores[{index}]"
        group = obj(group, path)
        exact(group, {"audience", "significant", "included_in_article_promise", "group_h_score"}, path)
        text(group["audience"], f"{path}.audience")
        significant = boolean(group["significant"], f"{path}.significant")
        included = boolean(group["included_in_article_promise"], f"{path}.included_in_article_promise")
        h_score = integer(group["group_h_score"], f"{path}.group_h_score", 0, 4)
        if significant and included:
            included_scores.append(h_score)
    if not included_scores:
        fail("audience_language.group_scores", "brak istotnej grupy objętej obietnicą")
    integer(root["claim_count"], "claim_count")
    enum(root["claim_map_confidence"], CONFIDENCE, "claim_map_confidence")
    scores = validate_scores(root["scores"])
    if scores["H"] != min(included_scores):
        fail("scores.H", "musi równać się minimum H grup istotnych i objętych obietnicą")
    if audience["unexplained_core_terms_block_nonspecialists"] and scores["H"] > 2:
        fail("scores.H", "blokujące terminy ograniczają H do 2")
    if audience["core_unrecoverable_without_expert"] and scores["H"] > 1:
        fail("scores.H", "rdzeń nieodtwarzalny bez eksperta ogranicza H do 1")
    if audience["popularizing_purpose"] and audience["core_requires_undisclosed_specialist_knowledge"] and scores["L"] > 2:
        fail("scores.L", "niespełniona funkcja popularyzatorska ogranicza L do 2")
    issue_keys = {"issue_id", "severity", "centrality", "centrality_rationale", "application_risk", "application_risk_rationale", "confidence"}
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
        enum(issue["severity"], SEVERITIES, f"{path}.severity")
        enum(issue["centrality"], CENTRALITIES, f"{path}.centrality")
        text(issue["centrality_rationale"], f"{path}.centrality_rationale")
        enum(issue["application_risk"], RISKS, f"{path}.application_risk")
        text(issue["application_risk_rationale"], f"{path}.application_risk_rationale")
        enum(issue["confidence"], CONFIDENCE, f"{path}.confidence")
    validate_counts(root["issue_counts"], "issue_counts", issues)
    text_array(root["central_findings"], "central_findings", nonempty=True)
    enum(root["verdict"], VERDICTS, "verdict")
    enum(root["verdict_confidence"], CONFIDENCE, "verdict_confidence")
    enum(root["source_coverage"], {"pelne", "wystarczajace", "czesciowe", "niewystarczajace"}, "source_coverage")
    enum(root["counterfactual_correction"], {"ograniczona", "strukturalna", "nie_dotyczy"}, "counterfactual_correction")


def validate_relation(relation: str, a_ids: list[str], b_ids: list[str], path: str) -> None:
    cardinalities = {
        "one_to_one": (1, 1), "one_to_many": (1, 2), "many_to_one": (2, 1),
        "many_to_many": (2, 2), "a_only": (1, 0), "b_only": (0, 1),
    }
    a_min, b_min = cardinalities[relation]
    if relation in {"one_to_one", "a_only", "b_only"}:
        valid = len(a_ids) == a_min and len(b_ids) == b_min
    else:
        valid = len(a_ids) >= a_min and len(b_ids) >= b_min
    if not valid:
        fail(path, f"liczność identyfikatorów nie odpowiada relacji {relation}")


def validate_comparison(data: object, result_a: dict | None = None, result_b: dict | None = None) -> None:
    root = obj(data, "root")
    keys = {
        "schema_version", "comparison_id", "publication_id", "run_a_id", "run_b_id", "methodology",
        "same_material_version", "material_version_rationale", "audience_profile_comparison", "score_comparison",
        "verdict_comparison", "claim_matches", "issue_matches", "coverage_metrics", "aggregate_metrics",
        "disagreements", "conclusions",
    }
    exact(root, keys, "root")
    if root["schema_version"] != "0.3-draft":
        fail("schema_version", "oczekiwano '0.3-draft'")
    for key in ("comparison_id", "publication_id", "run_a_id", "run_b_id", "material_version_rationale"):
        text(root[key], key)
    boolean(root["same_material_version"], "same_material_version")
    method = obj(root["methodology"], "methodology")
    exact(method, {"version", "identifier"}, "methodology")
    if method["version"] != "0.3-draft":
        fail("methodology.version", "oczekiwano '0.3-draft'")
    text(method["identifier"], "methodology.identifier")
    audience = obj(root["audience_profile_comparison"], "audience_profile_comparison")
    audience_keys = {"outlet_type_agreement", "purpose_agreement", "declared_audience_agreement", "article_audience_agreement", "required_knowledge_agreement", "confidence_agreement", "group_scores", "rationale"}
    exact(audience, audience_keys, "audience_profile_comparison")
    for key in audience_keys - {"group_scores", "rationale"}:
        boolean(audience[key], f"audience_profile_comparison.{key}")
    text(audience["rationale"], "audience_profile_comparison.rationale")
    group_keys = {"audience", "a_h", "b_h", "a_l", "b_l", "rationale"}
    for index, group in enumerate(array(audience["group_scores"], "audience_profile_comparison.group_scores")):
        path = f"audience_profile_comparison.group_scores[{index}]"
        group = obj(group, path)
        exact(group, group_keys, path)
        text(group["audience"], f"{path}.audience")
        for key in ("a_h", "b_h", "a_l", "b_l"):
            if group[key] is not None:
                integer(group[key], f"{path}.{key}", 0, 4)
        text(group["rationale"], f"{path}.rationale")
    score_rows = array(root["score_comparison"], "score_comparison")
    if len(score_rows) != 12:
        fail("score_comparison", "wymagane dokładnie 12 wymiarów")
    seen_dimensions = set()
    for index, row in enumerate(score_rows):
        path = f"score_comparison[{index}]"
        row = obj(row, path)
        exact(row, {"dimension", "a_score", "b_score", "exact_agreement", "difference", "rationale"}, path)
        dimension = enum(row["dimension"], set(DIMENSIONS), f"{path}.dimension")
        if dimension in seen_dimensions:
            fail(f"{path}.dimension", "wymiar występuje więcej niż raz")
        seen_dimensions.add(dimension)
        for key in ("a_score", "b_score"):
            score = row[key]
            if score != "nd":
                integer(score, f"{path}.{key}", 0, 4)
        agreement = boolean(row["exact_agreement"], f"{path}.exact_agreement")
        if agreement != (row["a_score"] == row["b_score"]):
            fail(f"{path}.exact_agreement", "wartość nie odpowiada wynikom")
        expected_difference = None if "nd" in {row["a_score"], row["b_score"]} else abs(row["a_score"] - row["b_score"])
        if row["difference"] != expected_difference:
            fail(f"{path}.difference", f"oczekiwano {expected_difference!r}")
        text(row["rationale"], f"{path}.rationale")
    verdict = obj(root["verdict_comparison"], "verdict_comparison")
    verdict_keys = {"a_verdict", "b_verdict", "agreement", "a_counterfactual_correction", "b_counterfactual_correction", "rationale"}
    exact(verdict, verdict_keys, "verdict_comparison")
    enum(verdict["a_verdict"], VERDICTS, "verdict_comparison.a_verdict")
    enum(verdict["b_verdict"], VERDICTS, "verdict_comparison.b_verdict")
    agreement = boolean(verdict["agreement"], "verdict_comparison.agreement")
    if agreement != (verdict["a_verdict"] == verdict["b_verdict"]):
        fail("verdict_comparison.agreement", "wartość nie odpowiada werdyktom")
    enum(verdict["a_counterfactual_correction"], {"ograniczona", "strukturalna", "nie_dotyczy"}, "verdict_comparison.a_counterfactual_correction")
    enum(verdict["b_counterfactual_correction"], {"ograniczona", "strukturalna", "nie_dotyczy"}, "verdict_comparison.b_counterfactual_correction")
    text(verdict["rationale"], "verdict_comparison.rationale")

    def matches(items: object, path: str, *, issues: bool) -> tuple[list[str], list[str]]:
        a_all: list[str] = []
        b_all: list[str] = []
        required = {"relation", "a_ids", "b_ids", "semantic_summary", "rationale"}
        required |= ({"severity_agreement", "centrality_agreement", "risk_agreement", "grouping_difference"} if issues else {"result_agreement", "atomization_difference"})
        for index, item in enumerate(array(items, path)):
            item_path = f"{path}[{index}]"
            item = obj(item, item_path)
            exact(item, required, item_path)
            relation = enum(item["relation"], RELATIONS, f"{item_path}.relation")
            a_ids = text_array(item["a_ids"], f"{item_path}.a_ids", unique=True)
            b_ids = text_array(item["b_ids"], f"{item_path}.b_ids", unique=True)
            validate_relation(relation, a_ids, b_ids, item_path)
            a_all.extend(a_ids)
            b_all.extend(b_ids)
            text(item["semantic_summary"], f"{item_path}.semantic_summary")
            text(item["rationale"], f"{item_path}.rationale")
            if issues:
                for key in ("severity_agreement", "centrality_agreement", "risk_agreement"):
                    enum(item[key], {"yes", "no", "not_comparable"}, f"{item_path}.{key}")
                text(item["grouping_difference"], f"{item_path}.grouping_difference")
            else:
                enum(item["result_agreement"], {"exact", "adjacent", "different", "not_comparable"}, f"{item_path}.result_agreement")
                text(item["atomization_difference"], f"{item_path}.atomization_difference")
        if len(a_all) != len(set(a_all)):
            fail(path, "identyfikator A występuje więcej niż raz")
        if len(b_all) != len(set(b_all)):
            fail(path, "identyfikator B występuje więcej niż raz")
        return a_all, b_all

    a_claims, b_claims = matches(root["claim_matches"], "claim_matches", issues=False)
    a_issues, b_issues = matches(root["issue_matches"], "issue_matches", issues=True)
    coverage = obj(root["coverage_metrics"], "coverage_metrics")
    coverage_keys = {"a_claims_total", "b_claims_total", "a_issues_total", "b_issues_total", "a_claims_mapped", "b_claims_mapped", "a_issues_mapped", "b_issues_mapped"}
    exact(coverage, coverage_keys, "coverage_metrics")
    for key in coverage_keys:
        integer(coverage[key], f"coverage_metrics.{key}")
    expected_mapped = {"a_claims_mapped": len(a_claims), "b_claims_mapped": len(b_claims), "a_issues_mapped": len(a_issues), "b_issues_mapped": len(b_issues)}
    for key, expected in expected_mapped.items():
        if coverage[key] != expected:
            fail(f"coverage_metrics.{key}", f"oczekiwano {expected}")
    metrics = obj(root["aggregate_metrics"], "aggregate_metrics")
    metric_keys = {"exact_score_agreement", "within_one_score_agreement", "mean_absolute_score_difference", "score_difference_direction", "verdict_agreement", "one_to_one_claim_result_agreement", "all_issue_centrality_agreement", "all_issue_risk_agreement", "major_critical_centrality_agreement", "major_critical_risk_agreement", "nd_disagreements"}
    exact(metrics, metric_keys, "aggregate_metrics")
    for key in ("exact_score_agreement", "within_one_score_agreement"):
        number(metrics[key], f"aggregate_metrics.{key}")
    for key in ("one_to_one_claim_result_agreement", "all_issue_centrality_agreement", "all_issue_risk_agreement", "major_critical_centrality_agreement", "major_critical_risk_agreement"):
        if metrics[key] is not None:
            number(metrics[key], f"aggregate_metrics.{key}")
    if metrics["mean_absolute_score_difference"] is not None:
        number(metrics["mean_absolute_score_difference"], "aggregate_metrics.mean_absolute_score_difference", 0, 4)
    enum(metrics["score_difference_direction"], {"a_higher", "b_higher", "balanced", "not_comparable"}, "aggregate_metrics.score_difference_direction")
    boolean(metrics["verdict_agreement"], "aggregate_metrics.verdict_agreement")
    text_array(metrics["nd_disagreements"], "aggregate_metrics.nd_disagreements", unique=True)
    unknown_dimensions = sorted(set(metrics["nd_disagreements"]) - set(DIMENSIONS))
    if unknown_dimensions:
        fail("aggregate_metrics.nd_disagreements", f"nieznane wymiary: {', '.join(unknown_dimensions)}")
    exact_rate = sum(row["exact_agreement"] for row in score_rows) / len(score_rows)
    within_rate = sum(
        row["a_score"] == row["b_score"] if "nd" in {row["a_score"], row["b_score"]}
        else row["difference"] <= 1
        for row in score_rows
    ) / len(score_rows)
    numeric_differences = [row["difference"] for row in score_rows if row["difference"] is not None]
    mean_difference = (sum(numeric_differences) / len(numeric_differences)) if numeric_differences else None
    nd_disagreements = sorted(
        row["dimension"] for row in score_rows if (row["a_score"] == "nd") != (row["b_score"] == "nd")
    )
    signed_differences = [
        row["a_score"] - row["b_score"] for row in score_rows
        if row["a_score"] != "nd" and row["b_score"] != "nd"
    ]
    expected_direction = "not_comparable"
    if signed_differences:
        signed_sum = sum(signed_differences)
        expected_direction = "a_higher" if signed_sum > 0 else "b_higher" if signed_sum < 0 else "balanced"
    expected_metrics = {
        "exact_score_agreement": exact_rate,
        "within_one_score_agreement": within_rate,
        "mean_absolute_score_difference": mean_difference,
        "score_difference_direction": expected_direction,
        "verdict_agreement": verdict["agreement"],
        "nd_disagreements": nd_disagreements,
    }
    for key, expected in expected_metrics.items():
        actual = metrics[key]
        if isinstance(expected, float):
            if abs(actual - expected) > 1e-9:
                fail(f"aggregate_metrics.{key}", f"oczekiwano {expected}")
        elif actual != expected:
            fail(f"aggregate_metrics.{key}", f"oczekiwano {expected!r}")
    disagreement_keys = {"area", "summary", "likely_source", "effect"}
    for index, item in enumerate(array(root["disagreements"], "disagreements")):
        path = f"disagreements[{index}]"
        item = obj(item, path)
        exact(item, disagreement_keys, path)
        enum(item["area"], {"audience_profile", "score", "verdict", "nd", "atomization", "claim_result", "issue_grouping", "severity", "centrality", "risk", "language", "outlet_fit", "other"}, f"{path}.area")
        for key in ("summary", "likely_source", "effect"):
            text(item[key], f"{path}.{key}")
    text_array(root["conclusions"], "conclusions", nonempty=True)

    if (result_a is None) != (result_b is None):
        fail("comparison", "do kontroli pokrycia trzeba podać oba wyniki A i B")
    if result_a is not None and result_b is not None:
        validate_result(result_a)
        validate_result(result_b)
        if not result_a["calibration_mode"] or not result_b["calibration_mode"]:
            fail("comparison", "oba wyniki muszą należeć do kalibracji")
        if root["run_a_id"] != result_a["analysis_id"] or root["run_b_id"] != result_b["analysis_id"]:
            fail("comparison", "identyfikatory przebiegów nie odpowiadają wynikom")
        if root["publication_id"] != result_a["publication"]["publication_id"] or root["publication_id"] != result_b["publication"]["publication_id"]:
            fail("comparison", "identyfikator publikacji nie odpowiada wynikom")
        expected = {
            "a_claims": {item["claim_id"] for item in result_a["claims"]}, "b_claims": {item["claim_id"] for item in result_b["claims"]},
            "a_issues": {item["issue_id"] for item in result_a["issues"]}, "b_issues": {item["issue_id"] for item in result_b["issues"]},
        }
        actual = {"a_claims": set(a_claims), "b_claims": set(b_claims), "a_issues": set(a_issues), "b_issues": set(b_issues)}
        for key in expected:
            missing = sorted(expected[key] - actual[key])
            extra = sorted(actual[key] - expected[key])
            if missing or extra:
                fail("comparison", f"niepełne mapowanie {key}: brak={missing}, nadmiar={extra}")
        totals = {"a_claims_total": len(expected["a_claims"]), "b_claims_total": len(expected["b_claims"]), "a_issues_total": len(expected["a_issues"]), "b_issues_total": len(expected["b_issues"])}
        for key, expected_value in totals.items():
            if coverage[key] != expected_value:
                fail(f"coverage_metrics.{key}", f"oczekiwano {expected_value}")
        rows = {row["dimension"]: row for row in score_rows}
        for dimension in DIMENSIONS:
            if rows[dimension]["a_score"] != result_a["scores"][dimension] or rows[dimension]["b_score"] != result_b["scores"][dimension]:
                fail(f"score_comparison.{dimension}", "wyniki nie odpowiadają plikom A/B")


def load_json(path: Path) -> object:
    try:
        with path.open(encoding="utf-8") as source:
            return json.load(source)
    except (OSError, json.JSONDecodeError) as error:
        fail(str(path), str(error))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("result", "extract", "comparison"))
    parser.add_argument("path", type=Path)
    parser.add_argument("--result-a", type=Path)
    parser.add_argument("--result-b", type=Path)
    args = parser.parse_args(argv)
    try:
        data = load_json(args.path)
        if args.kind == "result":
            validate_result(data)
        elif args.kind == "extract":
            validate_extract(data)
        else:
            if args.result_a is None or args.result_b is None:
                fail("comparison", "wymagane --result-a i --result-b")
            validate_comparison(data, load_json(args.result_a), load_json(args.result_b))
    except ValidationError as error:
        print(f"BŁĄD: {error}", file=sys.stderr)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
