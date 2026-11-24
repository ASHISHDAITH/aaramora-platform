from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
PAGE=(ROOT/"relationships.html").read_text(encoding="utf-8")
class RelationshipSupportTests(unittest.TestCase):
    def test_relationship_resource_page_is_preserved(self):
        self.assertTrue((ROOT/"relationships.html").is_file())
        self.assertIn("relationship",PAGE.lower())
    def test_unapproved_numbers_are_not_public(self):
        for number in ("1800-89-14416","18008914416","tel:181"):
            self.assertNotIn(number,PAGE)
    def test_immediate_danger_route_uses_112(self):
        self.assertIn('href="tel:112"',PAGE)
    def test_mental_health_support_route_uses_14416(self):
        self.assertIn('href="tel:14416"',PAGE)
    def test_shared_navigation_has_six_primary_items(self):
        nav=PAGE.split('<nav class="main-nav"',1)[1].split("</nav>",1)[0]
        self.assertEqual(nav.count("<a "),6)
    def test_support_numbers_have_verification_date(self):
        self.assertIn("Last verified 24 November 2026",PAGE)
if __name__=="__main__":
    unittest.main()
