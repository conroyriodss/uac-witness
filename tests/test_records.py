"""Schema checks for witness records. Standard library only.

Run with `python -m unittest discover -s tests` (CI: .github/workflows/records.yml).

Every records/NNNN-*.json must:
  * parse as JSON, with no duplicate keys at any depth;
  * if it is not a legacy state record, carry a "record" field that equals its NNNN filename prefix;
  * fit a gap-free sequence of numbers starting at 0001.

Published records are never edited, so a defect in one is listed below with its reason instead of being
fixed. Only records already published may be listed; the list is closed.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

RECORDS = Path(__file__).resolve().parents[1] / "records"
NAME = re.compile(r"^(\d{4})-[a-z0-9][a-z0-9-]*\.json$")

# 0001 and 0002 predate the "record" field (state records: at_utc, event, files, seal_log).
LEGACY_NO_RECORD_FIELD = {"0001", "0002"}

# Published defects, kept as published (README, "Timestamps, and the 0006 -> 0008 -> 0009 sequence").
KNOWN_DEFECTS = {
    "0009": "duplicate key 'record': the second value (the path of record 0008) shadows '0009'",
}
KNOWN_DEFECTS_CLOSED_AT = "0009"  # no record after this may be listed


def _strict_load(path: Path):
    return _strict_loads(path.read_text(encoding="utf-8"))


def _strict_loads(text: str):
    dups: list[str] = []

    def hook(pairs):
        seen = set()
        for k, _ in pairs:
            if k in seen:
                dups.append(k)
            seen.add(k)
        return dict(pairs)

    data = json.loads(text, object_pairs_hook=hook)
    return data, dups


def _records():
    return sorted(p for p in RECORDS.iterdir() if p.suffix == ".json")


class TestRecords(unittest.TestCase):
    def test_filenames_are_numbered(self):
        for p in _records():
            self.assertRegex(p.name, NAME, p.name)

    def test_numbering_is_gap_free_and_unique(self):
        nums = [NAME.match(p.name).group(1) for p in _records()]
        self.assertEqual(len(nums), len(set(nums)), "duplicate record number")
        self.assertEqual([int(n) for n in nums], list(range(1, len(nums) + 1)))

    def test_valid_json_unique_keys_and_record_number(self):
        for p in _records():
            num = NAME.match(p.name).group(1)
            with self.subTest(record=num):
                data, dups = _strict_load(p)  # raises on invalid JSON
                self.assertIsInstance(data, dict)
                if num in KNOWN_DEFECTS:
                    self.assertTrue(dups, f"{num} is listed as defective but no longer is")
                    continue
                self.assertEqual(dups, [], f"duplicate keys in {p.name}")
                if num in LEGACY_NO_RECORD_FIELD:
                    self.assertNotIn("record", data)
                else:
                    self.assertEqual(data.get("record"), num, f"record field of {p.name}")

    def test_known_defect_list_is_closed(self):
        for num in KNOWN_DEFECTS:
            self.assertLessEqual(num, KNOWN_DEFECTS_CLOSED_AT, "new records must pass, not be listed")
        self.assertTrue(LEGACY_NO_RECORD_FIELD <= {"0001", "0002"})

    def test_strict_loader_catches_a_duplicate(self):
        # Known-answer check on the detector itself.
        _, dups = _strict_loads('{"a": 1, "b": {"c": 1, "c": 2}}')
        self.assertEqual(dups, ["c"])
        _, dups = _strict_loads('{"a": 1, "b": {"c": 1}}')
        self.assertEqual(dups, [])


if __name__ == "__main__":
    unittest.main()
