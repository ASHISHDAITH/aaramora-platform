import shutil
import subprocess
import tempfile
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


class InlineScriptAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = []
        self._current = None

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            attrs = dict(attrs)
            script_type = attrs.get("type", "").lower()
            if "src" not in attrs and (not script_type or script_type in {"text/javascript", "application/javascript", "module"}):
                self._current = {"type": script_type, "parts": []}

    def handle_data(self, data):
        if self._current is not None:
            self._current["parts"].append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._current is not None:
            self.scripts.append(self._current)
            self._current = None

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

    def test_all_womens_health_cards_have_the_same_guide_pattern(self):
        start = self.home.index('<section class="womens-section" id="womens-health">')
        end = self.home.index('</section>', start)
        section = self.home[start:end]
        cards = section.split('<article class="women-card"')[1:]
        self.assertEqual(len(cards), 8)
        for card in cards:
            self.assertIn("How might this feel day to day?", card)
            self.assertIn("What may help?", card)
            self.assertTrue("When to seek support" in card or "When to seek support and urgent help" in card)

    def test_pmos_terms_and_uncertainty_are_present(self):
        self.assertIn("PMOS", self.home)
        self.assertIn("PCOD", self.home)
        self.assertIn("statistically non-significant", self.home)

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
        self.assertNotRegex(self.rel, r'<(?:input|select|textarea|button)\b[^>]*\srequired(?:\s|>)')

    def test_quizzes_do_not_persist_or_network(self):
        for token in ["localStorage","sessionStorage","XMLHttpRequest","sendBeacon"]:
            self.assertNotIn(token, self.rel)
        self.assertNotRegex(self.rel, r"fetch\s*\(")

    def test_reading_library_and_open_downloads(self):
        library = (ROOT / "reading-library.html").read_text(encoding="utf-8")
        self.assertIn('href="reading-library.html"', self.home)
        self.assertIn("Capacity to Connect", library)
        self.assertIn("Attachment Through the Life Course", library)
        self.assertIn("Psychology of Human Relations", library)
        self.assertIn("CC BY-NC-SA 4.0", library)
        self.assertIn("prior written permission", library)

    def test_support_routes_are_present(self):
        for href in ["tel:112","tel:181","tel:14416"]:
            self.assertIn(href, self.rel)

    def test_wellbeing_internal_anchors_resolve(self):
        ids = set(self.well_audit.ids)
        self.assertEqual(len(self.well_audit.ids), len(ids))
        self.assertFalse([a for a in self.well_audit.anchors if a not in ids])


    def test_inline_javascript_parses_on_all_site_pages(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("Node.js is not installed in this test environment")

        page_names = ["index.html", "wellbeing.html", "relationships.html", "reading-library.html"]
        checked_scripts = 0
        for page_name in page_names:
            html = (ROOT / page_name).read_text(encoding="utf-8")
            parser = InlineScriptAudit()
            parser.feed(html)
            for index, script in enumerate(parser.scripts, start=1):
                source = "".join(script["parts"])
                if not source.strip():
                    continue
                suffix = ".mjs" if script["type"] == "module" else ".js"
                temp_path = None
                try:
                    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=suffix, delete=False) as temp:
                        temp.write(source)
                        temp_path = temp.name
                    result = subprocess.run([node, "--check", temp_path], capture_output=True, text=True, check=False)
                    self.assertEqual(
                        result.returncode, 0,
                        f"{page_name} inline script #{index} failed node --check:\\n{result.stderr or result.stdout}"
                    )
                    checked_scripts += 1
                finally:
                    if temp_path:
                        Path(temp_path).unlink(missing_ok=True)
        self.assertGreater(checked_scripts, 0, "No inline JavaScript blocks were checked")

    def test_relationship_internal_anchors_resolve(self):
        ids = set(self.rel_audit.ids)
        self.assertEqual(len(self.rel_audit.ids), len(ids))
        self.assertFalse([a for a in self.rel_audit.anchors if a not in ids])

if __name__ == "__main__":
    unittest.main()
