#!/usr/bin/env python3
"""Regression tests for the methodology 0.3 validator and schemas."""

from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "skill" / "scripts" / "validate_0_3.py"
SPEC = importlib.util.spec_from_file_location("validate_0_3", MODULE_PATH)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(VALIDATOR)


def evaluator() -> dict:
    return {
        "type": "ai", "name": "model testowy", "model_snapshot": "test",
        "reasoning_setting": "not_available", "tools": ["web"], "memory_access": "nie",
        "project_access": "nie", "private_repository_access": "nie",
    }


def scores() -> dict:
    return {letter: 3 for letter in "ABCDEFGHIJKL"}


def checked_context() -> list[dict]:
    kinds = [
        "homepage", "about_page", "blog_or_newsletter_description", "newsletter_signup_page",
        "category_or_series_description", "editorial_policy", "author_profile", "publication_promotion",
        "article_reader_cues", "actually_required_knowledge",
    ]
    return [{
        "kind": kind, "status": "sprawdzono", "url": f"https://example.com/{kind}",
        "location": "sekcja testowa", "accessed_at": "2026-09-13", "note": "Sprawdzono.",
    } for kind in kinds]


def valid_result(run: str = "A") -> dict:
    result_scores = scores()
    return {
        "schema_version": "0.3-draft", "analysis_id": f"TEST-001-{run}", "calibration_mode": True,
        "methodology": {"version": "0.3-draft", "identifier": "test-commit", "frozen_before_critical_pass": True},
        "publication": {
            "publication_id": "TEST-001", "title": "Przykładowa publikacja", "authors": ["Autor testowy"],
            "publisher": "Wydawca testowy", "outlet": "Serwis testowy", "url": "https://example.com/article",
            "published_at": "2026-01-01", "updated_at": None, "accessed_at": "2026-09-13",
            "analyzed_at": "2026-09-13", "language": "pl", "publication_type": ["popularyzatorski"], "full_text": "tak",
        },
        "materials": [{
            "material_id": "M-001", "role": "tresc_glowna", "url": "https://example.com/article",
            "accessed_at": "2026-09-13", "version": "2026-01-01", "immutable": "nie", "scope": "całość",
        }],
        "evaluator": evaluator(),
        "publication_context": {
            "outlet_type": {"value": "blog popularyzatorski", "evidence_ids": ["AUD-001"]},
            "outlet_declared_purpose": {"value": "wyjaśnianie dostępności", "evidence_ids": ["AUD-001"]},
            "declared_audiences": {"values": ["osoby początkujące"], "evidence_ids": ["AUD-001"]},
            "reasonably_foreseeable_audiences": {"values": ["praktycy"], "evidence_ids": ["AUD-002"]},
            "additional_relevant_audiences": {"values": [], "evidence_ids": []},
            "article_audiences": {"values": ["osoby początkujące", "praktycy"], "evidence_ids": ["AUD-001", "AUD-002"]},
            "declared_required_knowledge": {"values": [], "evidence_ids": ["AUD-001"]},
            "actually_required_knowledge": {"values": ["podstawy dostępności"], "evidence_ids": ["AUD-002"]},
            "required_knowledge_details": [{"knowledge": "podstawy dostępności", "publication_location": "akapit 2", "effect_without_knowledge": "nie da się wykonać ważnego kroku", "evidence_ids": ["AUD-002"]}],
            "facilitating_knowledge": {"values": [], "evidence_ids": []},
            "evidence": [
                {"evidence_id": "AUD-001", "rank": 1, "kind": "deklaracja wydawcy", "url": "https://example.com/about", "location": "O nas", "accessed_at": "2026-09-13", "excerpt_or_paraphrase": "Blog jest dla początkujących."},
                {"evidence_id": "AUD-002", "rank": 4, "kind": "wskazówka w artykule", "url": "https://example.com/article", "location": "wstęp", "accessed_at": "2026-09-13", "excerpt_or_paraphrase": "Tekst zwraca się do praktyków."},
            ],
            "checked_context_elements": checked_context(), "conflicts": [], "profile_status": "ustalony",
            "profile_confidence": "wysoka", "confidence_rationale": "Istnieje bezpośrednia deklaracja.", "audience_variants": [],
        },
        "audience_profile": {
            "basis": "mieszana", "primary_audience": "osoby początkujące", "subgroups": ["praktycy"],
            "assumed_knowledge": ["podstawy dostępności"], "popularizing_purpose": True,
            "core_terms": [{"term": "WCAG", "first_use_location": "akapit 1", "explained_or_clear_from_context": True, "necessary_for_core": True, "comprehension_effect": "termin wyjaśniony"}],
            "unexplained_core_terms_block_nonspecialists": False, "core_requires_undisclosed_specialist_knowledge": False,
            "core_unrecoverable_without_expert": False,
            "group_comprehension": [
                {"audience": "osoby początkujące", "significant": True, "included_in_article_promise": True, "scope_rationale": "Grupa zadeklarowana.", "group_h_score": 3, "group_l_score": 3, "assumptions": [], "barriers": ["jeden termin"], "evidence_ids": ["AUD-001"]},
                {"audience": "praktycy", "significant": True, "included_in_article_promise": True, "scope_rationale": "Grupa wskazana w tekście.", "group_h_score": 4, "group_l_score": 4, "assumptions": ["praktyka"], "barriers": [], "evidence_ids": ["AUD-002"]},
            ],
            "lowest_significant_group_score": 3, "lowest_significant_group_l_score": 3, "expert_assessment_not_user_tested": True,
            "rationale": "Profil wynika z dowodów miejsca i artykułu.",
        },
        "temporal_assessment": {
            "historical_accuracy": "zgodne", "historical_rationale": "Dostępna wersja pierwotna.",
            "original_version_available": True, "assessed_historical_version": "original", "version_evidence_ids": ["M-001"],
            "historical_confidence": "wysoka", "current_applicability": "zasadniczo_zgodne",
            "current_rationale": "Główny przekaz pozostaje aktualny.", "current_version_basis": "Treść pobrana w dniu dostępu.",
            "material_changes": ["nowsza wersja standardu"],
        },
        "claim_map_confidence": "wysoka", "claim_map_confidence_rationale": "Pełna treść była dostępna.",
        "claim_count": 1,
        "claims": [{
            "claim_id": "T-001", "claim_match_id": None, "location": "akapit 2", "text": "Twierdzenie testowe.",
            "atomization_rationale": "Jedna teza, jeden skutek i jeden zestaw źródeł.",
            "extraction_trace": {"publication_fragment_or_location": "akapit 2", "source_value_code_or_content": "Reguła źródłowa.", "paraphrase": "Twierdzenie testowe.", "verification_source_ids": ["Z-001"], "result": "zasadniczo_zgodne"},
            "category": "T", "importance": "wazne", "verifiability": "weryfikowalne", "result": "zasadniczo_zgodne",
            "result_boundary_rationale": "Lepsze niż częściowo zgodne, ale brak jednego warunku.", "confidence": "wysoka",
            "source_ids": ["Z-001"], "effect": "Ograniczone doprecyzowanie.",
        }],
        "issues": [{
            "issue_id": "P-001", "claim_ids": ["T-001"], "summary": "Brak jednego warunku.",
            "proposed_correction": "Dodać warunek.", "grouping_rationale": "Jeden błąd i jedna poprawka.", "severity": "male",
            "centrality": "element_poboczny", "centrality_rationale": "Nie zmienia rdzenia.",
            "application_risk": "niskie", "application_risk_rationale": "Skutek jest lokalny.",
            "centrality_test": None, "application_risk_test": None, "language_barrier": None,
            "confidence": "wysoka", "rationale": "Problem nie zmienia rdzenia.",
        }],
        "issue_counts": {"krytyczne": 0, "duze": 0, "srednie": 0, "male": 1},
        "scores": result_scores, "score_rationales": {letter: f"Uzasadnienie wymiaru {letter}." for letter in "ABCDEFGHIJKL"},
        "verdict": "rzetelny_z_niewielkimi_zastrzezeniami", "verdict_basis_issue_ids": ["P-001"],
        "counterfactual_correction": "ograniczona", "verdict_confidence": "wysoka", "source_coverage": "pelne",
        "safe_recommendation": "z_niewielkimi_korektami", "safe_recommendation_rationale": None,
        "verdict_rationale": "Rdzeń jest poprawny.",
        "limitations": ["Brak testu z użytkownikami."],
        "sources": [{"source_id": "Z-001", "title": "Źródło testowe", "url": "https://example.com/source", "accessed_at": "2026-09-13", "version": "1"}],
    }


def valid_extract() -> dict:
    return {
        "schema_version": "0.3-draft", "analysis_id": "TEST-001-A", "publication_id": "TEST-001",
        "methodology": {"version": "0.3-draft", "identifier": "test-commit"}, "evaluator": evaluator(),
        "material_versions": [{"material_id": "M-001", "role": "tresc_glowna", "url": "https://example.com/article", "version": "2026-01-01"}],
        "publication_context_summary": {"outlet_type": "blog popularyzatorski", "outlet_declared_purpose": "wyjaśnianie dostępności", "declared_audiences": ["osoby początkujące"], "article_audiences": ["osoby początkujące", "praktycy"], "actually_required_knowledge": ["podstawy dostępności"], "conflicts": [], "profile_status": "ustalony", "profile_confidence": "wysoka"},
        "audience_language": {"primary_audience": "osoby początkujące", "popularizing_purpose": True, "unexplained_core_terms_block_nonspecialists": False, "core_requires_undisclosed_specialist_knowledge": False, "core_unrecoverable_without_expert": False, "group_scores": [
            {"audience": "osoby początkujące", "significant": True, "included_in_article_promise": True, "group_h_score": 3, "group_l_score": 3},
            {"audience": "praktycy", "significant": True, "included_in_article_promise": True, "group_h_score": 4, "group_l_score": 4},
        ]},
        "claim_count": 1, "claim_map_confidence": "wysoka", "scores": scores(),
        "issue_counts": {"krytyczne": 0, "duze": 0, "srednie": 0, "male": 1},
        "issues": [{"issue_id": "P-001", "severity": "male", "centrality": "element_poboczny", "centrality_rationale": "Nie zmienia rdzenia.", "application_risk": "niskie", "application_risk_rationale": "Skutek jest lokalny.", "language_barrier": None, "confidence": "wysoka"}],
        "central_findings": ["Rdzeń jest poprawny."], "verdict": "rzetelny_z_niewielkimi_zastrzezeniami",
        "verdict_confidence": "wysoka", "source_coverage": "pelne", "counterfactual_correction": "ograniczona",
    }


def valid_comparison() -> dict:
    score_rows = [{"dimension": letter, "a_score": 3, "b_score": 3, "exact_agreement": True, "difference": 0, "rationale": "Zgodność."} for letter in "ABCDEFGHIJKL"]
    return {
        "schema_version": "0.3-draft", "comparison_id": "TEST-001-AB", "publication_id": "TEST-001",
        "run_a_id": "TEST-001-A", "run_b_id": "TEST-001-B", "methodology": {"version": "0.3-draft", "identifier": "test-commit"},
        "same_material_version": True, "material_version_rationale": "Ta sama migawka.",
        "audience_profile_comparison": {"outlet_type_agreement": True, "purpose_agreement": True, "declared_audience_agreement": True, "article_audience_agreement": True, "required_knowledge_agreement": True, "confidence_agreement": True, "group_scores": [{"audience": "osoby początkujące", "a_h": 3, "b_h": 3, "a_l": 3, "b_l": 3, "rationale": "Zgodność."}], "rationale": "Profile zgodne."},
        "score_comparison": score_rows,
        "verdict_comparison": {"a_verdict": "rzetelny_z_niewielkimi_zastrzezeniami", "b_verdict": "rzetelny_z_niewielkimi_zastrzezeniami", "agreement": True, "a_counterfactual_correction": "ograniczona", "b_counterfactual_correction": "ograniczona", "rationale": "Zgodność."},
        "claim_matches": [{"relation": "one_to_one", "a_ids": ["T-001"], "b_ids": ["T-001"], "semantic_summary": "To samo twierdzenie.", "result_agreement": "exact", "component_agreement_counts": None, "atomization_difference": "Brak.", "rationale": "Znaczenie zgodne."}],
        "issue_matches": [{"relation": "one_to_one", "a_ids": ["P-001"], "b_ids": ["P-001"], "semantic_summary": "Ten sam problem.", "severity_agreement": "yes", "centrality_agreement": "yes", "risk_agreement": "yes", "grouping_difference": "Brak.", "rationale": "Znaczenie zgodne."}],
        "coverage_metrics": {"a_claims_total": 1, "b_claims_total": 1, "a_issues_total": 1, "b_issues_total": 1, "a_claims_mapped": 1, "b_claims_mapped": 1, "a_issues_mapped": 1, "b_issues_mapped": 1},
        "aggregate_metrics": {"exact_score_agreement": 1.0, "within_one_score_agreement": 1.0, "mean_absolute_score_difference": 0.0, "score_difference_direction": "balanced", "verdict_agreement": True, "one_to_one_claim_result_agreement": 1.0, "all_issue_centrality_agreement": 1.0, "all_issue_risk_agreement": 1.0, "major_critical_centrality_agreement": None, "major_critical_risk_agreement": None, "nd_disagreements": []},
        "disagreements": [], "conclusions": ["Przebiegi są zgodne."],
    }


class ValidatorTests(unittest.TestCase):
    def test_valid_result_extract_and_comparison(self) -> None:
        result_a = valid_result("A")
        result_b = valid_result("B")
        VALIDATOR.validate_result(result_a)
        VALIDATOR.validate_extract(valid_extract(), result_a)
        VALIDATOR.validate_comparison(valid_comparison(), result_a, result_b)

    def test_rejects_duplicate_json_keys(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"schema_version":"0.3-draft","schema_version":"inna"}', encoding="utf-8")
            with self.assertRaises(VALIDATOR.ValidationError):
                VALIDATOR.load_json(path)

    def test_extract_crosscheck_rejects_mismatch(self) -> None:
        extract = valid_extract()
        extract["claim_count"] = 2
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_extract(extract, valid_result("A"))

    def test_extract_crosscheck_allows_shortened_prose(self) -> None:
        extract = valid_extract()
        extract["publication_context_summary"]["outlet_declared_purpose"] = "krótszy opis celu"
        extract["issues"][0]["centrality_rationale"] = "Skrócone uzasadnienie."
        VALIDATOR.validate_extract(extract, valid_result("A"))

    def test_extract_crosscheck_rejects_changed_issue_classification(self) -> None:
        extract = valid_extract()
        extract["issues"][0]["application_risk"] = "srednie"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_extract(extract, valid_result("A"))

    def test_requires_all_ten_context_checks(self) -> None:
        result = valid_result()
        result["publication_context"]["checked_context_elements"].pop()
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_rejects_unknown_audience_evidence(self) -> None:
        result = valid_result()
        result["publication_context"]["declared_audiences"]["evidence_ids"] = ["AUD-999"]
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_rejects_audience_determination_without_evidence(self) -> None:
        result = valid_result()
        result["publication_context"]["declared_audiences"]["evidence_ids"] = []
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_unresolved_profile_requires_two_variants(self) -> None:
        result = valid_result()
        context = result["publication_context"]
        context["profile_status"] = "nieustalony_wiarygodnie"
        context["profile_confidence"] = "niska"
        context["audience_variants"] = []
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_h_is_minimum_for_included_significant_groups(self) -> None:
        result = valid_result()
        result["audience_profile"]["group_comprehension"][0]["group_h_score"] = 2
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_l_is_minimum_for_included_significant_groups(self) -> None:
        result = valid_result()
        result["audience_profile"]["group_comprehension"][0]["group_l_score"] = 2
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_required_knowledge_needs_matching_trace(self) -> None:
        result = valid_result()
        result["publication_context"]["required_knowledge_details"] = []
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_high_audience_confidence_requires_unconflicted_established_profile(self) -> None:
        result = valid_result()
        result["publication_context"]["conflicts"] = [{"summary": "Sprzeczna deklaracja.", "evidence_ids": ["AUD-001"]}]
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)
        result = valid_result()
        result["publication_context"]["profile_status"] = "czesciowo_ustalony"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_language_caps_h_and_l(self) -> None:
        result = valid_result()
        result["audience_profile"]["unexplained_core_terms_block_nonspecialists"] = True
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_active_language_cap_requires_issue_trace(self) -> None:
        result = valid_result()
        profile = result["audience_profile"]
        profile["unexplained_core_terms_block_nonspecialists"] = True
        profile["group_comprehension"][0]["group_h_score"] = 2
        profile["lowest_significant_group_score"] = 2
        result["scores"]["H"] = 2
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)
        barrier = {
            "locations": ["akapit 1"], "audience_groups": ["osoby początkujące"],
            "terms_or_structural_elements": ["niewyjaśniony skrót"], "affected_dimensions": ["H"],
        }
        result["issues"][0]["language_barrier"] = barrier
        VALIDATOR.validate_result(result)
        result = valid_result()
        result["audience_profile"]["core_requires_undisclosed_specialist_knowledge"] = True
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_unrecoverable_core_caps_h_at_one(self) -> None:
        result = valid_result()
        profile = result["audience_profile"]
        profile["core_unrecoverable_without_expert"] = True
        profile["group_comprehension"][0]["group_h_score"] = 2
        profile["lowest_significant_group_score"] = 2
        result["scores"]["H"] = 2
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_claim_trace_must_match_claim(self) -> None:
        result = valid_result()
        result["claims"][0]["extraction_trace"]["paraphrase"] = "Inna parafraza."
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_legal_and_normative_claims_exclude_nd_for_b(self) -> None:
        result = valid_result()
        result["claims"][0]["category"] = "S"
        result["scores"]["B"] = "nd"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_recommendation_excludes_nd_for_i(self) -> None:
        result = valid_result()
        result["claims"][0]["category"] = "Z"
        result["scores"]["I"] = "nd"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_not_applicable_correction_requires_unresolved_verdict(self) -> None:
        result = valid_result()
        result["counterfactual_correction"] = "nie_dotyczy"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_safe_recommendation_cannot_be_less_cautious(self) -> None:
        result = valid_result()
        result["safe_recommendation"] = "bez_zastrzezen"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_stricter_safe_recommendation_requires_rationale(self) -> None:
        result = valid_result()
        result["safe_recommendation"] = "z_nazwanymi_korektami_lub_zrodlami"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)
        result["safe_recommendation_rationale"] = "Niepewność jednego źródła uzasadnia większą ostrożność."
        VALIDATOR.validate_result(result)

    def test_updated_page_without_original_is_unresolved(self) -> None:
        result = valid_result()
        result["publication"]["updated_at"] = "2026-08-01"
        temporal = result["temporal_assessment"]
        temporal["original_version_available"] = False
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_rejects_unknown_temporal_material(self) -> None:
        result = valid_result()
        result["temporal_assessment"]["version_evidence_ids"] = ["M-999"]
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_calibration_requires_centrality_and_risk_for_small_issue(self) -> None:
        result = valid_result()
        result["issues"][0]["centrality"] = None
        result["issues"][0]["centrality_rationale"] = None
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_noncalibration_allows_short_fields_to_be_null_for_small_issue(self) -> None:
        result = valid_result()
        result["calibration_mode"] = False
        issue = result["issues"][0]
        issue["centrality"] = None
        issue["centrality_rationale"] = None
        issue["application_risk"] = None
        issue["application_risk_rationale"] = None
        VALIDATOR.validate_result(result)

    def test_large_issue_requires_full_minimal_repair_test(self) -> None:
        result = valid_result()
        issue = result["issues"][0]
        issue["severity"] = "duze"
        result["issue_counts"] = {"krytyczne": 0, "duze": 1, "srednie": 0, "male": 0}
        result["verdict"] = "rzetelny_z_istotnymi_zastrzezeniami"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_comparison_rejects_duplicate_mapping(self) -> None:
        comparison = valid_comparison()
        comparison["claim_matches"].append(copy.deepcopy(comparison["claim_matches"][0]))
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_comparison(comparison, valid_result("A"), valid_result("B"))

    def test_comparison_rejects_wrong_relation_cardinality(self) -> None:
        comparison = valid_comparison()
        comparison["claim_matches"][0]["relation"] = "one_to_many"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_comparison(comparison, valid_result("A"), valid_result("B"))

    def test_comparison_rejects_missing_identifier(self) -> None:
        comparison = valid_comparison()
        comparison["claim_matches"] = []
        comparison["coverage_metrics"]["a_claims_mapped"] = 0
        comparison["coverage_metrics"]["b_claims_mapped"] = 0
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_comparison(comparison, valid_result("A"), valid_result("B"))

    def test_comparison_rejects_incorrect_aggregate_metric(self) -> None:
        comparison = valid_comparison()
        comparison["aggregate_metrics"]["exact_score_agreement"] = 0.5
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_comparison(comparison, valid_result("A"), valid_result("B"))

    def test_comparison_rejects_different_method_identifier(self) -> None:
        comparison = valid_comparison()
        comparison["methodology"]["identifier"] = "inny-commit"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_comparison(comparison, valid_result("A"), valid_result("B"))

    def test_comparison_rejects_verdict_not_matching_results(self) -> None:
        comparison = valid_comparison()
        comparison["verdict_comparison"]["a_verdict"] = "rzetelny"
        comparison["verdict_comparison"]["agreement"] = False
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_comparison(comparison, valid_result("A"), valid_result("B"))

    def test_comparison_rejects_false_exact_claim_agreement(self) -> None:
        comparison = valid_comparison()
        result_b = valid_result("B")
        result_b["claims"][0]["result"] = "czesciowo_zgodne"
        result_b["claims"][0]["extraction_trace"]["result"] = "czesciowo_zgodne"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_comparison(comparison, valid_result("A"), result_b)

    def test_comparison_accepts_only_declared_adjacent_pairs(self) -> None:
        comparison = valid_comparison()
        comparison["claim_matches"][0]["result_agreement"] = "adjacent"
        comparison["aggregate_metrics"]["one_to_one_claim_result_agreement"] = 0.0
        result_b = valid_result("B")
        result_b["claims"][0]["result"] = "czesciowo_zgodne"
        result_b["claims"][0]["extraction_trace"]["result"] = "czesciowo_zgodne"
        VALIDATOR.validate_comparison(comparison, valid_result("A"), result_b)
        comparison["claim_matches"][0]["result_agreement"] = "different"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_comparison(comparison, valid_result("A"), result_b)

    def test_complex_agreement_counts_determine_result(self) -> None:
        VALIDATOR.validate_component_agreement(
            {"exact": 1, "adjacent": 2, "different": 0, "not_comparable": 0},
            "adjacent", "test",
        )
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_component_agreement(
                {"exact": 1, "adjacent": 2, "different": 0, "not_comparable": 0},
                "exact", "test",
            )

    def test_comparison_rejects_false_issue_agreement(self) -> None:
        comparison = valid_comparison()
        result_b = valid_result("B")
        result_b["issues"][0]["centrality"] = "rdzen"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_comparison(comparison, valid_result("A"), result_b)

    def test_comparison_recalculates_claim_and_issue_metrics(self) -> None:
        comparison = valid_comparison()
        comparison["aggregate_metrics"]["one_to_one_claim_result_agreement"] = 0.5
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_comparison(comparison, valid_result("A"), valid_result("B"))
        comparison = valid_comparison()
        comparison["aggregate_metrics"]["all_issue_risk_agreement"] = 0.5
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_comparison(comparison, valid_result("A"), valid_result("B"))

    def test_schema_files_are_json(self) -> None:
        for name in ("wynik.schema.json", "wyciag-kalibracyjny.schema.json", "porownanie-pary-0.3.schema.json"):
            with (ROOT / "metodologia" / "0.3" / name).open(encoding="utf-8") as source:
                self.assertIsInstance(json.load(source), dict)


if __name__ == "__main__":
    unittest.main()
