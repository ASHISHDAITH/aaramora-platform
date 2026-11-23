"""Static rights, preservation and navigation checks for the Aaramora reading library."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "reading-library.html").read_text(encoding="utf-8")


class ReadingLibraryChecks(unittest.TestCase):
    def test_all_existing_sections_remain_available(self):
        for anchor in (
            "free-downloads", "scripture-shelf", "workbooks-and-articles",
            "relationship-open-learning", "attachment-books", "faith-wisdom",
            "novels-and-classics", "github-shelves", "licensing",
        ):
            with self.subTest(anchor=anchor):
                self.assertIn(f'id="{anchor}"', HTML)

    def test_original_resources_and_reuse_rules_remain(self):
        for phrase in (
            "Capacity to Connect", "Psychology 2e", "Doing What Matters in Times of Stress",
            "Attachment in Adulthood", "Guru Granth Sahib", "Bhagavad", "Quran",
            "World English Bible", "Dhammapada", "Our reuse checklist", "Never bypass DRM",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, HTML)

    def test_existing_hero_and_credit_remain(self):
        self.assertIn("Esra Korkmaz", HTML)
        self.assertIn("A book does not ask you to hurry; it simply leaves the next page open.", HTML)
        self.assertIn('alt="Vintage book pages', HTML)

    def test_catalogue_enhancements_exist(self):
        self.assertIn('id="language-catalogue"', HTML)
        for marker in (
            "catalogue-search", "catalogue-language", "catalogue-tradition",
            "catalogue-access", "catalogue-rights", "catalogue-level",
            "catalogue-format", "catalogue-results", "catalogue-status",
        ):
            with self.subTest(marker=marker):
                self.assertIn(f'id="{marker}"', HTML)
        self.assertIn('fetch(url,{cache:"no-cache"})', HTML)
        self.assertIn('data/library.json', HTML)
        self.assertIn("For reflection and cultural reading, not as treatment.", HTML)

    def test_format_navigation_has_six_clear_resource_categories(self):
        for kind in ("book", "video", "audiobook", "article", "blog", "image"):
            with self.subTest(kind=kind):
                self.assertIn(f'data-content-type="{kind}"', HTML)
                self.assertIn(f'data-content-type-link="{kind}"', HTML)
        self.assertIn("selectedContentType", HTML)
        self.assertIn("kindLabels", HTML)

    def test_header_is_opaque_and_support_contacts_are_grouped(self):
        self.assertIn("background:var(--paper)!important", HTML)
        self.assertIn('class="support-link"', HTML)
        self.assertIn('href="tel:14416"', HTML)
        self.assertIn('href="tel:112"', HTML)


    def test_support_contact_targets_have_separation_for_wcag_target_size(self):
        self.assertIn(".support-links{display:flex;align-items:center;gap:24px;flex-wrap:wrap}", HTML)
        self.assertIn("min-height:44px;padding:5px 12px", HTML)

    def test_support_contacts_keep_44px_minimum_height(self):
        self.assertIn(".top .wrap .support-link{min-height:44px;padding:5px 12px}", HTML)

    def test_focused_skip_link_uses_own_topbar_row(self):
        self.assertIn(".skip-link:focus{position:relative;left:auto;top:auto;display:inline-flex;flex-basis:100%;width:max-content;margin-bottom:4px}", HTML)

    def test_internal_fragment_links_resolve(self):
        ids = set(re.findall(r'\bid="([^"]+)"', HTML))
        fragments = re.findall(r'href="#([^"]+)"', HTML)
        missing = sorted(set(fragments) - ids)
        self.assertEqual([], missing, f"Unresolved page fragments: {missing}")


if __name__ == "__main__":
    unittest.main()
