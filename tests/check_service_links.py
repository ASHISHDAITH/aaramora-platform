import json
import re
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "data" / "service-links.json"


class ServiceLinkRegisterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(REGISTER.read_text(encoding="utf-8"))
        cls.records = {item["id"]: item for item in cls.data["records"]}

    def test_critical_india_routes_are_registered(self):
        self.assertEqual(
            set(self.records),
            {"tele-manas", "erss-112", "women-helpline-181"}
        )

    def test_all_records_have_owner_sources_and_review_dates(self):
        for record in self.records.values():
            self.assertTrue(record["owner"])
            self.assertTrue(record["officialSourceUrl"].startswith("https://"))
            date.fromisoformat(record["lastVerified"])
            date.fromisoformat(record["nextReview"])
            self.assertGreaterEqual(
                date.fromisoformat(record["nextReview"]),
                date.fromisoformat(record["lastVerified"])
            )
            self.assertTrue(record["caveat"])

    def test_tele_manas_numbers_match_current_official_record(self):
        numbers = {n["display"]: n["tel"] for n in self.records["tele-manas"]["displayedNumbers"]}
        self.assertEqual(numbers["14416"], "14416")
        self.assertEqual(numbers["1800-89-14416"], "18008914416")

    def test_women_helpline_has_state_coverage_caveat(self):
        record = self.records["women-helpline-181"]
        self.assertIn("West Bengal", record["geography"])
        self.assertIn("West Bengal", record["caveat"])
        self.assertIn("wcd.gov.in", record["officialSourceUrl"])

    def test_register_has_no_visitor_or_health_data_fields(self):
        raw = json.dumps(self.data).lower()
        for forbidden in ("visitor", "phone_number", "address", "symptom", "patient"):
            self.assertNotIn(forbidden, raw)


if __name__ == "__main__":
    unittest.main()
