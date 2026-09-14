#!/usr/bin/env python3
"""Technical consistency checks for the complete 0.3 draft package."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_skill_copies_match_public_sources(self) -> None:
        pairs = {
            ROOT / "metodologia/0.3/standard.md": ROOT / "skill/references/standard-0.3.md",
            ROOT / "metodologia/0.3/kotwice.md": ROOT / "skill/references/kotwice-0.3.md",
            ROOT / "metodologia/0.3/wynik.schema.json": ROOT / "skill/references/wynik-0.3.schema.json",
            ROOT / "metodologia/0.3/wyciag-kalibracyjny.schema.json": ROOT / "skill/references/wyciag-kalibracyjny-0.3.schema.json",
            ROOT / "metodologia/0.3/porownanie-pary-0.3.schema.json": ROOT / "skill/references/porownanie-pary-0.3.schema.json",
            ROOT / "metodologia/0.3/metryka-0.3.schema.json": ROOT / "skill/references/metryka-0.3.schema.json",
            ROOT / "szablony/0.3/wzor-raportu.md": ROOT / "skill/references/wzor-raportu-0.3.md",
            ROOT / "szablony/0.3/karta-oceny.md": ROOT / "skill/references/karta-oceny-0.3.md",
            ROOT / "szablony/0.3/wzor-porownania.md": ROOT / "skill/references/wzor-porownania-0.3.md",
        }
        for source, copy in pairs.items():
            self.assertEqual(source.read_bytes(), copy.read_bytes(), f"Niezgodna kopia: {copy}")

    def test_internal_skill_links_exist(self) -> None:
        skill_dir = ROOT / "skill"
        content = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", content)
        missing = [link for link in links if "://" not in link and not (skill_dir / link).is_file()]
        self.assertEqual([], missing)

    def test_local_schema_refs_resolve(self) -> None:
        for name in ("wynik.schema.json", "wyciag-kalibracyjny.schema.json", "porownanie-pary-0.3.schema.json", "metryka-0.3.schema.json"):
            schema = json.loads((ROOT / "metodologia/0.3" / name).read_text(encoding="utf-8"))
            definitions = schema.get("$defs", {})

            def visit(value: object) -> None:
                if isinstance(value, dict):
                    reference = value.get("$ref")
                    if isinstance(reference, str) and reference.startswith("#/$defs/"):
                        self.assertIn(reference.removeprefix("#/$defs/"), definitions, f"Nierozwiązane {reference} w {name}")
                    for child in value.values():
                        visit(child)
                elif isinstance(value, list):
                    for child in value:
                        visit(child)

            visit(schema)

    def test_approved_rules_are_present(self) -> None:
        standard = (ROOT / "metodologia/0.3/standard.md").read_text(encoding="utf-8")
        anchors = (ROOT / "metodologia/0.3/kotwice.md").read_text(encoding="utf-8")
        required_standard = [
            "Trudny i specjalistyczny język publikacji nie może sam w sobie stanowić dowodu",
            "minimalną uczciwą naprawę wady",
            "porownanie-pary-0.3.schema.json",
            "fragment albo lokalizacja publikacji → dokładna liczba, kod lub treść źródłowa",
            "poziom centralności, poziom ryzyka zastosowania i krótkie uzasadnienie są obowiązkowe dla wszystkich problemów",
            "Granicę wpisu ustala się według najmniejszego fragmentu",
            "Raport zapisuje liczbę składowych każdego rodzaju",
            "mają wspólną przyczynę, wymagają jednej zasadniczej korekty",
            "`group_l_score`",
            "Każdy element wiedzy koniecznej wskazuje fragment publikacji",
            "musi zostać zapisana jako problem z własnym `issue_id`",
            "Odchylenie jest dopuszczalne wyłącznie w kierunku większej ostrożności",
        ]
        for phrase in required_standard:
            self.assertIn(phrase, standard)
        for phrase in ("A=3", "D=2", "D=3", "G=3", "H=4", "H=3", "H=2", "H=1", "najniższą oceną"):
            self.assertIn(phrase, anchors)

    def test_approved_s9_and_s10_are_implemented(self) -> None:
        standard = (ROOT / "metodologia/0.3/standard.md").read_text(encoding="utf-8")
        schema = json.loads((ROOT / "metodologia/0.3/wynik.schema.json").read_text(encoding="utf-8"))
        temporal = schema["$defs"]["temporalAssessment"]
        self.assertIn("historical_version_reconstructable", standard)
        self.assertIn("historical_version_reconstructable", temporal["required"])
        self.assertNotIn("original_version_available", temporal["required"])
        self.assertNotIn("current_after_update", temporal["properties"]["assessed_historical_version"]["enum"])
        metric_schema = ROOT / "metodologia/0.3/metryka-0.3.schema.json"
        self.assertTrue(metric_schema.is_file())
        self.assertIn("Kanoniczna metryka przebiegu", metric_schema.read_text(encoding="utf-8"))

    def test_t1_and_t2_are_implemented(self) -> None:
        standard = (ROOT / "metodologia/0.3/standard.md").read_text(encoding="utf-8")
        result_schema = json.loads((ROOT / "metodologia/0.3/wynik.schema.json").read_text(encoding="utf-8"))
        summary = (ROOT / "kalibracja/0.3/wyniki-B1.md").read_text(encoding="utf-8")
        self.assertIn("Bieżąca suma SHA-256", standard)
        self.assertIn("historical_version_evidence", result_schema["$defs"]["temporalAssessment"]["required"])
        self.assertIn("32 niezależne oceny", summary)
        self.assertIn("R3 nie uruchomiono", summary)
        self.assertIn("B2 nie zostało rozpoczęte", summary)

    def test_s11_through_s15_are_implemented(self) -> None:
        standard = (ROOT / "metodologia/0.3/standard.md").read_text(encoding="utf-8")
        result_schema = json.loads((ROOT / "metodologia/0.3/wynik.schema.json").read_text(encoding="utf-8"))
        comparison_schema = json.loads((ROOT / "metodologia/0.3/porownanie-pary-0.3.schema.json").read_text(encoding="utf-8"))

        for phrase in (
            "Wymiar C otrzymuje ocenę liczbową tylko wtedy",
            "Wymiar J otrzymuje ocenę liczbową",
            "Każdy problem `srednie` albo `duze` przechodzi ustrukturyzowany test granicy",
            "Kontrola właściwego przedmiotu wymiaru",
            "Przed werdyktem należy rozdzielić",
            "Role zawodowe łączy się w jedną grupę",
        ):
            self.assertIn(phrase, standard)

        for field in (
            "dimension_applicability",
            "dimension_scope_checks",
            "decidability_test",
        ):
            self.assertIn(field, result_schema["required"])
        for field in ("medium_large_boundary_test", "criticality_test"):
            self.assertIn(field, result_schema["$defs"]["issue"]["required"])
        for field in ("applicability_comparison", "decidability_comparison"):
            self.assertIn(field, comparison_schema["required"])

    def test_technical_control_documents_distinguish_historical_and_current_state(self) -> None:
        calibration = ROOT / "kalibracja/0.3"
        for name in (
            "kontrola-techniczna-walidatora-po-pilocie.md",
            "kontrola-techniczna-S1-S8.md",
        ):
            self.assertIn(
                "Dokument historyczny",
                (calibration / name).read_text(encoding="utf-8"),
            )

        current = (calibration / "kontrola-techniczna-S1-S10.md").read_text(encoding="utf-8")
        self.assertIn("Kontrola techniczna wdrożenia S1–S10", current)
        self.assertIn("S9 i S10 są wdrożone", current)
        self.assertIn("Dokument historyczny", current)
        self.assertIn("B1 zostało następnie wykonane i zakończone proceduralnie", current)
        self.assertIn("B2 nie zostało rozpoczęte", current)

        pilot = (calibration / "wyniki-pilota.md").read_text(encoding="utf-8")
        self.assertIn("S1–S10 zostały następnie osobno zatwierdzone i wdrożone", pilot)

        latest = (calibration / "kontrola-techniczna-S1-S15.md").read_text(encoding="utf-8")
        self.assertIn("85/85 poprawnych", latest)
        self.assertIn("T1–T2 oraz S1–S15 są wdrożone", latest)
        self.assertIn("B1 zostało zakończone proceduralnie", latest)
        self.assertIn("B2 nie zostało rozpoczęte", latest)


if __name__ == "__main__":
    unittest.main()
