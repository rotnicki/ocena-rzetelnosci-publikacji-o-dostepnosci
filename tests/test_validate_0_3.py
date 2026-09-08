#!/usr/bin/env python3
"""Regression tests for the 0.3 draft validator and schemas."""

from __future__ import annotations

import copy
import importlib.util
import json
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
        "type": "ai",
        "name": "model testowy",
        "model_snapshot": "test",
        "reasoning_setting": "not_available",
        "tools": ["web"],
        "memory_access": "nie",
        "project_access": "nie",
        "private_repository_access": "nie",
    }


def scores() -> dict:
    return {letter: 3 for letter in "ABCDEFGHIJKL"}


def valid_result() -> dict:
    return {
        "schema_version": "0.3-draft",
        "analysis_id": "TEST-001-A",
        "methodology": {
            "version": "0.3-draft",
            "identifier": "test-commit",
            "frozen_before_critical_pass": True,
        },
        "publication": {
            "publication_id": "TEST-001",
            "title": "Przykładowa publikacja",
            "authors": ["Autor testowy"],
            "publisher": "Wydawca testowy",
            "outlet": "Serwis testowy",
            "url": "https://example.com/article",
            "published_at": "2026-01-01",
            "updated_at": None,
            "accessed_at": "2026-09-08",
            "analyzed_at": "2026-09-08",
            "language": "pl",
            "publication_type": ["popularyzatorski"],
            "full_text": "tak",
        },
        "materials": [{
            "material_id": "M-001",
            "role": "tresc_glowna",
            "url": "https://example.com/article",
            "accessed_at": "2026-09-08",
            "version": "2026-01-01",
            "immutable": "nie",
            "scope": "całość",
        }],
        "evaluator": evaluator(),
        "audience_profile": {
            "basis": "mieszana",
            "primary_audience": "osoby początkujące",
            "subgroups": ["specjaliści"],
            "assumed_knowledge": ["podstawy dostępności"],
            "popularizing_purpose": True,
            "core_terms": [{
                "term": "WCAG",
                "first_use_location": "akapit 1",
                "explained_or_clear_from_context": True,
                "necessary_for_core": True,
                "comprehension_effect": "termin został wyjaśniony",
            }],
            "unexplained_core_terms_block_nonspecialists": False,
            "expert_assessment_not_user_tested": True,
            "rationale": "Profil wynika z opisu serwisu i treści.",
        },
        "temporal_assessment": {
            "historical_accuracy": "zgodne",
            "historical_rationale": "Ocena według stanu z dnia publikacji.",
            "current_applicability": "zasadniczo_zgodne",
            "current_rationale": "Główny przekaz pozostaje aktualny.",
            "material_changes": ["opublikowano nowszą wersję standardu"],
        },
        "claim_map_confidence": "wysoka",
        "claim_map_confidence_rationale": "Pełna treść była dostępna.",
        "claim_count": 1,
        "claims": [{
            "claim_id": "T-001",
            "claim_match_id": None,
            "location": "akapit 2",
            "text": "Twierdzenie testowe.",
            "category": "T",
            "importance": "wazne",
            "verifiability": "weryfikowalne",
            "result": "zasadniczo_zgodne",
            "result_boundary_rationale": "Lepsze niż częściowo zgodne, ale brak jednego warunku.",
            "confidence": "wysoka",
            "source_ids": ["Z-001"],
            "effect": "Ograniczone doprecyzowanie.",
        }],
        "issues": [{
            "issue_id": "P-001",
            "claim_ids": ["T-001"],
            "summary": "Brak jednego warunku.",
            "proposed_correction": "Dodać warunek.",
            "grouping_rationale": "Jeden błąd i jedna poprawka.",
            "severity": "male",
            "centrality": None,
            "application_risk": None,
            "centrality_test": None,
            "application_risk_test": None,
            "confidence": "wysoka",
            "rationale": "Problem nie zmienia rdzenia.",
        }],
        "issue_counts": {"krytyczne": 0, "duze": 0, "srednie": 0, "male": 1},
        "scores": scores(),
        "score_rationales": {letter: f"Uzasadnienie wymiaru {letter}." for letter in "ABCDEFGHIJKL"},
        "verdict": "rzetelny_z_niewielkimi_zastrzezeniami",
        "verdict_basis_issue_ids": ["P-001"],
        "counterfactual_correction": "ograniczona",
        "verdict_confidence": "wysoka",
        "source_coverage": "pelne",
        "safe_recommendation": "z_niewielkimi_korektami",
        "verdict_rationale": "Rdzeń jest poprawny.",
        "limitations": ["Brak testu z użytkownikami."],
        "sources": [{
            "source_id": "Z-001",
            "title": "Źródło testowe",
            "url": "https://example.com/source",
            "accessed_at": "2026-09-08",
            "version": "1",
        }],
    }


def valid_extract() -> dict:
    return {
        "schema_version": "0.3-draft",
        "analysis_id": "TEST-001-A",
        "publication_id": "TEST-001",
        "methodology": {"version": "0.3-draft", "identifier": "test-commit"},
        "evaluator": evaluator(),
        "material_versions": [{
            "material_id": "M-001",
            "role": "tresc_glowna",
            "url": "https://example.com/article",
            "version": "2026-01-01",
        }],
        "audience_language": {
            "primary_audience": "osoby początkujące",
            "popularizing_purpose": True,
            "unexplained_core_terms_block_nonspecialists": False,
        },
        "claim_count": 1,
        "claim_map_confidence": "wysoka",
        "scores": scores(),
        "issue_counts": {"krytyczne": 0, "duze": 0, "srednie": 0, "male": 1},
        "central_issues": [],
        "central_findings": ["Rdzeń jest poprawny."],
        "verdict": "rzetelny_z_niewielkimi_zastrzezeniami",
        "verdict_confidence": "wysoka",
        "source_coverage": "pelne",
        "counterfactual_correction": "ograniczona",
    }


class ValidatorTests(unittest.TestCase):
    def test_valid_result_and_extract(self) -> None:
        VALIDATOR.validate_result(valid_result())
        VALIDATOR.validate_extract(valid_extract())

    def test_language_caps(self) -> None:
        result = valid_result()
        result["audience_profile"]["unexplained_core_terms_block_nonspecialists"] = True
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_technical_claim_excludes_nd(self) -> None:
        result = valid_result()
        result["scores"]["C"] = "nd"
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_critical_threshold(self) -> None:
        result = valid_result()
        issue = result["issues"][0]
        issue.update({
            "severity": "krytyczne",
            "centrality": "rdzen",
            "application_risk": "srednie",
            "centrality_test": {
                "removal_changes_main_thesis_or_use": True,
                "publication_fulfils_purpose_after_removal": False,
                "rationale": "Problem dotyczy rdzenia.",
            },
            "application_risk_test": {
                "reader_action_likelihood": "wysokie",
                "impact_severity": "powazna",
                "reversibility": "trudna",
                "rationale": "Możliwa jest poważna szkoda.",
            },
        })
        result["issue_counts"] = {"krytyczne": 1, "duze": 0, "srednie": 0, "male": 0}
        with self.assertRaises(VALIDATOR.ValidationError):
            VALIDATOR.validate_result(result)

    def test_schema_files_are_json(self) -> None:
        for path in (
            ROOT / "metodologia" / "0.3" / "wynik.schema.json",
            ROOT / "metodologia" / "0.3" / "wyciag-kalibracyjny.schema.json",
        ):
            with path.open(encoding="utf-8") as source:
                self.assertIsInstance(json.load(source), dict)


if __name__ == "__main__":
    unittest.main()
