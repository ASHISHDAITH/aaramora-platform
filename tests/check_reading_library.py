"""Static rights and navigation checks for the Aaramora reading library."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "reading-library.html").read_text(encoding="utf-8")


class ReadingLibraryChecks(unittest.TestCase):
    def test_existing_sections_remain_available(self):
        for anchor in ("free-downloads", "relationship-open-learning", "attachment-books", "github", "licensing"):
            with self.subTest(anchor=anchor):
                self.assertIn(f'id="{anchor}"', HTML)
                self.assertIn(f'href="#{anchor}"', HTML)

    def test_sacred_texts_and_discovery_shelf_exists(self):
        self.assertIn('id="scripture-shelf"', HTML)
        for phrase in ("Bhagavad Gita", "Upanishads", "Guru Granth Sahib", "Japji Sahib", "Sukhmani Sahib", "Quran", "World English Bible", "Dhammapada", "Project Gutenberg", "Standard Ebooks", "Wikisource", "Directory of Open Access Books", "Open Library"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, HTML)

    def test_legal_source_and_rights_notices_are_present(self):
        for url in ("heritage.iitk.ac.in", "sikher.com", "tanzil.net/docs/Text_License", "quranenc.com/en/home/about/conditions", "ebible.org/engwebu/copyright.htm", "gutenberg.org/ebooks/2388", "doabooks.org", "openlibrary.org/developers/api"):
            with self.subTest(url=url):
                self.assertIn(url, HTML)
        for phrase in ("public domain in the United States", "check local copyright law", "must not be altered", "mixture of licences", "metadata is CC0", "borrowing"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, HTML)

    def test_no_bypass_or_unofficial_mirror_language(self):
        for phrase in ("Never bypass DRM", "paywalls", "private repository permissions", "unauthorised copies"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, HTML)

    def test_hero_photo_quote_and_attribution(self):
        self.assertIn("pexels-photo-6873903.jpeg", HTML)
        self.assertIn("Pavel Danilyuk", HTML)
        self.assertIn("Let the page be a pause, not another thing to finish.", HTML)
        self.assertIn('alt="An open vintage book', HTML)

    def test_internal_fragment_links_resolve(self):
        ids = set(re.findall(r'\bid="([^"]+)"', HTML))
        fragments = re.findall(r'href="#([^"]+)"', HTML)
        missing = sorted(set(fragments) - ids)
        self.assertEqual([], missing, f"Unresolved page fragments: {missing}")


if __name__ == "__main__":
    unittest.main()
