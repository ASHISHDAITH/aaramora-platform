from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
HOME=(ROOT/"index.html").read_text(encoding="utf-8")
WOMEN=(ROOT/"womens-health.html").read_text(encoding="utf-8")
RESEARCH=(ROOT/"research.html").read_text(encoding="utf-8")
HELP=(ROOT/"get-help.html").read_text(encoding="utf-8")
CHECKINS=(ROOT/"check-ins.html").read_text(encoding="utf-8")

class HealthTopicPlacementTests(unittest.TestCase):
    def test_homepage_has_no_unreviewed_womens_health_section(self):
        self.assertNotIn('id="womens-health"',HOME)
        self.assertIn('href="/womens-health.html"',HOME)
    def test_womens_health_page_is_prominently_marked_draft(self):
        self.assertIn("DRAFT · NOT YET REVIEWED BY A QUALIFIED WOMEN'S-HEALTH CLINICIAN",WOMEN)
        self.assertIn('id="womens-health"',WOMEN)
        for topic in ("PCOS","endometriosis","thyroid","anaemia","Preparing for an appointment"):
            self.assertIn(topic.lower(),WOMEN.lower())
    def test_original_womens_health_guides_remain_available_as_draft(self):
    def test_research_spotlight_is_separate_and_review_pending(self):
        self.assertNotIn("evidence-note",HOME)
        self.assertIn("Research spotlight · review pending",RESEARCH)
        self.assertIn("not an individual risk prediction",RESEARCH)
    def test_postpartum_psychosis_urgent_warning_is_retained(self):
        self.assertIn("postpartum psychosis can be a medical emergency",HOME.lower())
        self.assertIn('id="postpartum-psychosis"',HELP)
        self.assertIn('href="tel:112"',HELP)
    def test_cycle_and_womens_health_tools_show_review_warning(self):
        self.assertIn("DRAFT, NOT CLINICIAN-REVIEWED",CHECKINS)
        self.assertIn("cycle-log",CHECKINS)
        self.assertIn("womens-health-planner",CHECKINS)
if __name__=="__main__":
    unittest.main()
