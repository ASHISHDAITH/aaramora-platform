from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
HOME=(ROOT/"index.html").read_text(encoding="utf-8")
WOMEN=(ROOT/"womens-health.html").read_text(encoding="utf-8")
RESEARCH=(ROOT/"research.html").read_text(encoding="utf-8")
HELP=(ROOT/"get-help.html").read_text(encoding="utf-8")
CHECKINS=(ROOT/"check-ins.html").read_text(encoding="utf-8")
class HealthTopicPlacementTests(unittest.TestCase):
    def test_homepage_has_no_unreviewed_womens_health_or_research_sections(self):
        self.assertNotIn('id="womens-health"',HOME)
        self.assertNotIn("evidence-note",HOME)
        self.assertIn('href="womens-health.html"',HOME)
        self.assertIn('href="research.html"',HOME)
    def test_womens_health_page_is_prominently_marked_draft(self):
        self.assertIn("DRAFT · NOT YET REVIEWED BY A QUALIFIED WOMEN'S-HEALTH CLINICIAN",WOMEN)
        self.assertIn('id="womens-health"',WOMEN)
        for topic in ("PMOS","Endometriosis","Thyroid","anaemia","Preparing for a women's health appointment"):
            self.assertIn(topic.lower(),WOMEN.lower())
    def test_original_womens_health_guides_remain_on_draft_page(self):
        self.assertIn("PMOS",WOMEN)
        self.assertIn("Endometriosis",WOMEN)
        self.assertIn("Thyroid",WOMEN)
        self.assertIn("anaemia",WOMEN.lower())
    def test_research_spotlight_is_separate_and_review_pending(self):
        self.assertNotIn("evidence-note",HOME)
        self.assertNotIn("evidence-note",WOMEN)
        self.assertIn("Research spotlight · review pending",RESEARCH)
        self.assertIn("not an individual risk prediction",RESEARCH.lower())
    def test_postpartum_psychosis_urgent_warning_is_retained(self):
        self.assertIn("postpartum psychosis can be a medical emergency",HOME.lower())
        self.assertIn('id="postpartum-psychosis"',HELP)
        self.assertIn('href="tel:112"',HELP)
    def test_checkins_womens_health_tools_are_marked_draft(self):
        self.assertIn("DRAFT",CHECKINS)
        self.assertIn("CLINICIAN-REVIEWED",CHECKINS)
        self.assertIn("cycle",CHECKINS.lower())
        self.assertIn("appointment",CHECKINS.lower())
if __name__=="__main__":unittest.main()
