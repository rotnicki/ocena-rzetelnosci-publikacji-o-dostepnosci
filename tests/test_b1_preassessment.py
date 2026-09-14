import hashlib
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CALIBRATION = ROOT / "kalibracja" / "0.3"
CANDIDATES = CALIBRATION / "rejestr-kandydatow-B1.md"
CORPUS = CALIBRATION / "rejestr-korpusu-B1.md"


def sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class B1PreassessmentRegistersTest(unittest.TestCase):
    def test_required_public_files_exist(self):
        for name in (
            "protokol-B1.md",
            "dziennik-wyszukiwan-B1.md",
            "rejestr-kandydatow-B1.md",
            "rejestr-korpusu-B1.md",
            "rejestr-odchylen-B1.md",
        ):
            self.assertTrue((CALIBRATION / name).is_file(), name)

    def test_protocol_hash_matches_search_log(self):
        protocol = (CALIBRATION / "protokol-B1.md").read_bytes()
        search_log = (CALIBRATION / "dziennik-wyszukiwan-B1.md").read_text(
            encoding="utf-8"
        )
        match = re.search(
            r"SHA-256 ostatecznie zamrożonego protokołu:\*\* `([0-9a-f]{64})`",
            search_log,
        )
        self.assertIsNotNone(match)
        self.assertEqual(hashlib.sha256(protocol).hexdigest(), match.group(1))

    def test_candidate_pool_counts_urls_and_hashes(self):
        text = CANDIDATES.read_text(encoding="utf-8")
        rows = re.findall(
            r"^\| (P[1-6]-\d{2}) \|(?: [CJ] \|)? \[[^]]+\]\((https://[^)]+)\)"
            r".*?\| `([0-9a-f]{64})` \| ([^|]+) \|$",
            text,
            re.MULTILINE,
        )
        self.assertEqual(24, len(rows))
        self.assertEqual(24, len({candidate_id for candidate_id, *_ in rows}))
        self.assertEqual(24, len({url for _, url, *_ in rows}))

        profiles = {profile: 0 for profile in ("P1", "P2", "P3", "P4", "P5", "P6")}
        status_counts = {"main": 0, "reserve": 0, "other": 0}
        for candidate_id, url, recorded_hash, status in rows:
            profile = candidate_id[:2]
            profiles[profile] += 1
            expected = sha256(f"ocena-0.3-B1-korpus-v1|{profile}|{url}")
            self.assertEqual(expected, recorded_hash, candidate_id)
            if "główna" in status:
                status_counts["main"] += 1
            elif "rezerwowa" in status:
                status_counts["reserve"] += 1
            else:
                status_counts["other"] += 1

        self.assertEqual({profile: 4 for profile in profiles}, profiles)
        self.assertEqual({"main": 12, "reserve": 6, "other": 6}, status_counts)

    def test_p5_main_selection_has_c_and_j_probe(self):
        text = CANDIDATES.read_text(encoding="utf-8")
        selected = re.findall(
            r"^\| P5-\d{2} \| ([CJ]) \|.*?\| główna — B1-\d{2} \|$",
            text,
            re.MULTILINE,
        )
        self.assertEqual(["C", "J"], sorted(selected))

    def test_main_corpus_order_hashes_and_references(self):
        candidate_text = CANDIDATES.read_text(encoding="utf-8")
        corpus_text = CORPUS.read_text(encoding="utf-8")
        candidate_main_urls = set(
            re.findall(
                r"^\| P[1-6]-\d{2} \|(?: [CJ] \|)? \[[^]]+\]\((https://[^)]+)\)"
                r".*?\| główna — B1-\d{2} \|$",
                candidate_text,
                re.MULTILINE,
            )
        )
        rows = re.findall(
            r"^\| (\d+) \| (B1-\d{2}) \| \[[^]]+\]\((https://[^)]+)\)"
            r".*?\| `([0-9a-f]{64})` \| R[1-6] \|$",
            corpus_text,
            re.MULTILINE,
        )
        self.assertEqual(12, len(rows))
        self.assertEqual(list(range(1, 13)), [int(order) for order, *_ in rows])
        self.assertEqual(candidate_main_urls, {url for _, _, url, _ in rows})

        hashes = []
        for _, case_id, url, recorded_hash in rows:
            expected = sha256(f"ocena-0.3-B1-kolejnosc-v1|{case_id}|{url}")
            self.assertEqual(expected, recorded_hash, case_id)
            hashes.append(recorded_hash)
        self.assertEqual(sorted(hashes), hashes)

    def test_reserves_match_candidate_register(self):
        candidate_text = CANDIDATES.read_text(encoding="utf-8")
        corpus_text = CORPUS.read_text(encoding="utf-8")
        candidate_reserve_urls = set(
            re.findall(
                r"^\| P[1-6]-\d{2} \|(?: [CJ] \|)? \[[^]]+\]\((https://[^)]+)\)"
                r".*?\| rezerwowa — R[1-6] \|$",
                candidate_text,
                re.MULTILINE,
            )
        )
        corpus_reserve_urls = set(
            re.findall(
                r"^\| R[1-6] \| \[[^]]+\]\((https://[^)]+)\)",
                corpus_text,
                re.MULTILINE,
            )
        )
        self.assertEqual(6, len(corpus_reserve_urls))
        self.assertEqual(candidate_reserve_urls, corpus_reserve_urls)


if __name__ == "__main__":
    unittest.main()
