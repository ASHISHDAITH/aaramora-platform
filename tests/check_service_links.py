import json
from datetime import date
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/"data/service-links.json").read_text(encoding="utf-8"))
class PublicSupportNumberGateTests(unittest.TestCase):
    def test_only_two_national_services_are_in_the_public_register(self):
        self.assertEqual({r["id"] for r in DATA["records"]},{"tele-manas","erss-112"})
    def test_only_14416_and_112_are_marked_for_public_display(self):
        visible=[n["tel"] for r in DATA["records"] for n in r.get("displayedNumbers",[])]
        self.assertEqual(set(visible),{"14416","112"})
    def test_tele_manas_alternate_number_is_not_in_public_register(self):
        tele=next(r for r in DATA["records"] if r["id"]=="tele-manas")
        self.assertEqual([n["tel"] for n in tele["displayedNumbers"]],["14416"])
        self.assertNotIn("18008914416",json.dumps(DATA))
        self.assertNotIn("1800-89-14416",json.dumps(DATA))
    def test_each_number_has_source_and_review_dates(self):
        for r in DATA["records"]:
            self.assertTrue(r["officialSourceUrl"].startswith("https://"))
            date.fromisoformat(r["lastVerified"])
            date.fromisoformat(r["nextReview"])
    def test_policy_requires_named_human_review_for_additional_numbers(self):
        self.assertIn("named human reviewer",DATA["policy"]["description"].lower())
if __name__=="__main__":unittest.main()
