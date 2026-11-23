import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PageAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.anchors = []
        self.external_assets = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "a" and a.get("href", "").startswith("#"):
            self.anchors.append(a["href"][1:])
        if tag in {"script", "img", "iframe", "link"}:
            src = a.get("src") or (a.get("href") if tag == "link" else "")
            if src.startswith(("http://", "https://")):
                self.external_assets.append(src)

class RelationshipPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.home = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.page = (ROOT / "relationships.html").read_text(encoding="utf-8")
        cls.parser = PageAudit()
        cls.parser.feed(cls.page)

    def test_home_links_to_relationship_corner(self):
        self.assertIn('href="relationships.html"', self.home)

    def test_safety_gate_and_two_reflection_quizzes_exist(self):
        self.assertIn('id="safety-form"', self.page)
        self.assertIn('id="attachment-quiz"', self.page)
        self.assertIn('id="conflict-quiz"', self.page)
        self.assertIn('id="boundaries-quiz"', self.page)

    def test_quiz_prompts_are_unvalidated_and_not_diagnostic(self):
        self.assertIn("not validated psychological instruments", self.page)
        self.assertIn("cannot diagnose", self.page)
        self.assertEqual(self.page.count('class="concept-item"'), 40)

    def test_internal_anchors_resolve_and_ids_are_unique(self):
        ids = set(self.parser.ids)
        self.assertEqual(len(self.parser.ids), len(ids), "duplicate HTML ids")
        self.assertFalse([x for x in self.parser.anchors if x not in ids])

    def test_no_external_runtime_assets(self):
        self.assertEqual(self.parser.external_assets, [])

    def test_no_personal_data_persistence_or_network_calls(self):
        for token in ["localStorage", "sessionStorage", "XMLHttpRequest", "sendBeacon"]:
            self.assertNotIn(token, self.page)
        self.assertNotRegex(self.page, r"fetch\s*\(")

    def test_three_support_routes_are_visible(self):
        for href in ["tel:112", "tel:181", "tel:14416"]:
            self.assertIn(href, self.page)

if __name__ == "__main__":
    unittest.main()
