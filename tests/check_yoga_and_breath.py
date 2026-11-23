import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PageAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.fragments = []
        self.remote_runtime_assets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "a" and attrs.get("href", "").startswith("#"):
            self.fragments.append(attrs["href"][1:])
        if tag in {"script", "img", "iframe", "link"}:
            source = attrs.get("src") or (attrs.get("href") if tag == "link" else "")
            if source.startswith(("http://", "https://")):
                self.remote_runtime_assets.append(source)


class YogaAndBreathPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = (ROOT / "yoga-and-breath.html").read_text(encoding="utf-8")
        cls.home = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.wellbeing = (ROOT / "wellbeing.html").read_text(encoding="utf-8")
        cls.research = (ROOT / "docs" / "YOGA_AND_BREATH_EVIDENCE.md").read_text(encoding="utf-8")
        cls.scripts = (ROOT / "docs" / "YOGA_AND_BREATH_AUDIO_SCRIPTS.md").read_text(encoding="utf-8")
        cls.audit = PageAudit()
        cls.audit.feed(cls.page)

    def test_page_is_linked_from_existing_navigation(self):
        self.assertIn('href="yoga-and-breath.html"', self.home)
        self.assertIn('href="yoga-and-breath.html"', self.wellbeing)

    def test_core_sections_and_evidence_sources_exist(self):
        for section in ("evidence", "practices", "safety"):
            self.assertIn(f'id="{section}"', self.page)
        for url in (
            "pubmed.ncbi.nlm.nih.gov/23922209",
            "pubmed.ncbi.nlm.nih.gov/32423912",
            "pubmed.ncbi.nlm.nih.gov/37032928",
            "pmc/articles/PMC11919030",
        ):
            self.assertIn(url, self.page)

    def test_study_populations_and_comparators_are_distinguished(self):
        for phrase in (
            "12 trials · 619 people",
            "19 studies · 1,080 people",
            "13 studies (632 participants)",
            "2,341 participants in total",
            "active controls",
            "usual care",
            "not a prescription",
        ):
            self.assertIn(phrase, self.page)

    def test_no_diagnostic_or_cure_claim(self):
        lowered = self.page.lower()
        for phrase in ("yoga cures depression", "guaranteed relief", "replace professional care"):
            self.assertNotIn(phrase, lowered)
        self.assertIn("not a cure", lowered)
        self.assertIn("not a substitute", lowered)

    def test_safety_and_agency_are_visible(self):
        for phrase in (
            "stop",
            "dizzy",
            "pregnant",
            "medical condition",
            "eyes open",
            "breath holds",
            "112",
            "14416",
        ):
            self.assertIn(phrase.lower(), self.page.lower())

    def test_letter_grade_rubric_is_not_invented(self):
        self.assertIn("A/B/C/D rubric was not found", self.page)
        self.assertIn("do not invent", self.research.lower())

    def test_hindi_and_marathi_script_drafts_exist_but_are_not_approved(self):
        self.assertIn("नमस्ते", self.scripts)
        self.assertIn("नमस्कार", self.scripts)
        self.assertIn("requires native-speaker", self.scripts)
        self.assertIn("no audio recordings have been created", self.scripts.lower())
        self.assertIn("No audio file is published", self.page)

    def test_page_has_unique_ids_and_resolved_fragments(self):
        ids = set(self.audit.ids)
        self.assertEqual(len(ids), len(self.audit.ids), "duplicate id")
        self.assertFalse(sorted(set(self.audit.fragments) - ids))

    def test_no_external_runtime_assets_or_autoplay(self):
        self.assertEqual([], self.audit.remote_runtime_assets)
        self.assertNotRegex(self.page, r"<audio\b[^>]*\bautoplay")
        self.assertNotRegex(self.page, r"<video\b[^>]*\bautoplay")
        self.assertNotIn("localStorage", self.page)
        self.assertNotIn("sessionStorage", self.page)
        self.assertNotRegex(self.page, r"fetch\s*\(")


if __name__ == "__main__":
    unittest.main()
