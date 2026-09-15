import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "kalibracja" / "0.4" / "protokol-B2-przenosnosc-AI.md"
STATUS = ROOT / "kalibracja" / "0.4" / "README.md"


class B2PortabilityPreservationTests(unittest.TestCase):
    def test_protocol_exists_and_keeps_assessments_blocked(self):
        text = PROTOCOL.read_text(encoding="utf-8")
        self.assertIn("oceny B2 nie zostały rozpoczęte", text)
        self.assertIn("Oceny pozostają zablokowane", text)
        self.assertIn("36 ocen", text)

    def test_protocol_names_all_families_and_six_cases(self):
        text = PROTOCOL.read_text(encoding="utf-8")
        for family in ("ChatGPT", "Gemini", "Grok"):
            self.assertIn(family, text)
        self.assertEqual(set(re.findall(r"B2-0[1-6]", text)), {f"B2-0{i}" for i in range(1, 7)})

    def test_protocol_freezes_expected_method_commit(self):
        text = PROTOCOL.read_text(encoding="utf-8")
        self.assertIn("6bc8f21af1fda5f5ba3953970176126641033e12", text)
        self.assertIn("0.3-draft-S1-S15", text)

    def test_status_separates_the_study_from_the_0_3_release(self):
        text = STATUS.read_text(encoding="utf-8")
        self.assertIn("badanie nie zostało rozpoczęte", text)
        self.assertIn("nie było warunkiem wydania 0.3", text)
        self.assertIn("nie jest zatwierdzoną metodologią 0.4", text)

    def test_public_tree_does_not_contain_private_b2_results(self):
        forbidden = {"metryka-przebiegu.json", "manifest-wejscia.json", "SHA256SUMS"}
        public_paths = {path.name for path in ROOT.rglob("*") if path.is_file()}
        self.assertTrue(forbidden.isdisjoint(public_paths))


if __name__ == "__main__":
    unittest.main()
