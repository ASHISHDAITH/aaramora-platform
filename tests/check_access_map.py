import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/"data/pune-services.json").read_text(encoding="utf-8"))
class PuneAccessMapTests(unittest.TestCase):
    def test_has_exactly_25_service_entries_and_ten_facilities(self):
        self.assertEqual(25,len(DATA["services"]))
        self.assertEqual(10,len(DATA["facilities"]))
        self.assertEqual(25,DATA["serviceCount"])
    def test_each_service_has_official_source_and_map_url(self):
        facility_ids={f["id"] for f in DATA["facilities"]}
        for s in DATA["services"]:
            self.assertIn(s["facilityId"],facility_ids)
            self.assertTrue(s["officialSourceUrl"].startswith("https://"))
            self.assertTrue(s["mapUrl"].startswith("https://www.google.com/maps/"))
            self.assertEqual("2026-11-24",s["lastSourceCheck"])
    def test_map_discloses_limits_of_source_verification(self):
        page=(ROOT/"access-map.html").read_text(encoding="utf-8")
        self.assertIn("not independently confirmed",page)
        self.assertIn("not a ranking or endorsement",page)
        self.assertIn("civilian eligibility",page)
    def test_directory_is_available_without_javascript(self):
        page=(ROOT/"access-map.html").read_text(encoding="utf-8")
        self.assertEqual(10,page.count('class="facility-card"'))
        self.assertEqual(25,page.count('class="service-card"'))
    def test_no_local_provider_phone_numbers_are_guessed(self):
        raw=json.dumps(DATA)
        self.assertNotIn("tel:",raw)
if __name__=="__main__":unittest.main()
