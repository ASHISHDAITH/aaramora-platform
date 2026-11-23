import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class Audit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.anchors = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "a" and a.get("href", "").startswith("#"):
            self.anchors.append(a["href"][1:])

class WebsiteHealthContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.home = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.well = (ROOT / "wellbeing.html").read_text(encoding="utf-8")
        cls.rel = (ROOT / "relationships.html").read_text(encoding="utf-8")
        cls.well_audit = Audit(); cls.well_audit.feed(cls.well)
        cls.rel_audit = Audit(); cls.rel_audit.feed(cls.rel)

    def test_home_links_to_wellbeing_and_relationships(self):
        self.assertIn('href="wellbeing.html"', self.home)
        self.assertIn('href="relationships.html"', self.home)
        self.assertIn('id="womens-health"', self.home)

    def test_wellbeing_topics_have_consistent_headings(self):
        for topic in ["depression","anxiety","panic","stress","trauma","rumination","sleep","burnout","grief","ocd"]:
            self.assertIn('id="' + topic + '"', self.well)
        for phrase in ["How it may feel","What may help","When to seek support"]:
            self.assertIn(phrase, self.well)

    def test_pmos_terms_and_uncertainty_are_present(self):
        self.assertIn("PMOS", self.home)
        self.assertIn("PCOD", self.home)
        self.assertIn("not statistically significant", self.home)

    def test_all_40_relationship_concepts_are_present(self):
        terms = ["Attachment protest","Hyperactivation","Deactivation","Anxious attachment","Avoidant attachment",
        "Fearful attachment","Secure attachment","Internal working model","Safe haven","Secure base",
        "Proximity seeking","Separation distress","Reassurance seeking","Rejection sensitivity","Hypervigilance",
        "Rumination","Intolerance of uncertainty","Emotional dysregulation","Emotional flooding","Mentalization",
        "Co-regulation","Pursuer–distancer","Demand–withdraw","Protest polka","Negative reciprocity","Stonewalling",
        "Angry withdrawal","Attachment injury","Rupture","Repair","Ambiguous loss","Breakup grief","Relationship OCD",
        "Limerence","Digital surveillance","Jealousy induction","Love bombing","Breadcrumbing","Trauma bonding","Coercive control"]
        for term in terms:
            self.assertIn(term, self.rel)
        self.assertEqual(self.rel.count('class="concept-item"'), 40)

    def test_three_optional_reflections_and_safety_gate(self):
        for form_id in ["safety-form","attachment-quiz","conflict-quiz","boundaries-quiz"]:
            self.assertIn('id="' + form_id + '"', self.rel)
        self.assertNotRegex(self.rel, r'\srequired(?:\s|>)')

    def test_quizzes_do_not_persist_or_network(self):
        for token in ["localStorage","sessionStorage","XMLHttpRequest","sendBeacon"]:
            self.assertNotIn(token, self.rel)
        self.assertNotRegex(self.rel, r"fetch\s*\(")

    def test_support_routes_are_present(self):
        for href in ["tel:112","tel:181","tel:14416"]:
            self.assertIn(href, self.rel)

    def test_wellbeing_internal_anchors_resolve(self):
        ids = set(self.well_audit.ids)
        self.assertEqual(len(self.well_audit.ids), len(ids))
        self.assertFalse([a for a in self.well_audit.anchors if a not in ids])

    def test_relationship_internal_anchors_resolve(self):
        ids = set(self.rel_audit.ids)
        self.assertEqual(len(self.rel_audit.ids), len(ids))
        self.assertFalse([a for a in self.rel_audit.anchors if a not in ids])

if __name__ == "__main__":
    unittest.main()
