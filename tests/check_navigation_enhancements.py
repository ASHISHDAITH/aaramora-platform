from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NavigationAndDiscoveryEnhancementTests(unittest.TestCase):
    def read(self, name):
        return (ROOT / name).read_text(encoding="utf-8")

    def main_nav(self, page):
        self.assertIn('<nav class="main-nav"', page, "Main navigation must exist")
        return page.split('<nav class="main-nav"', 1)[1].split("</nav>", 1)[0]

    def test_every_page_with_menu_loads_the_shared_controller(self):
        for path in ROOT.glob("*.html"):
            page = self.read(path.name)
            if 'class="menu-toggle"' not in page:
                continue
            self.assertIn('aria-controls="site-nav"', page, path.name)
            self.assertIn('id="site-nav"', page, path.name)
            self.assertIn('src="/site.js"', page, path.name)

    def test_main_navigation_contains_relationship_and_reading_destinations(self):
        for path in ROOT.glob("*.html"):
            page = self.read(path.name)
            if 'class="menu-toggle"' not in page:
                continue
            nav = self.main_nav(page)
            self.assertEqual(6, nav.count("<a "), path.name)
            self.assertIn('href="relationships.html"', nav, path.name)
            self.assertIn('href="reading-library.html"', nav, path.name)

    def test_current_navigation_destination_is_identified(self):
        targets = {
            "get-help.html": "get-help.html",
            "relationships.html": "relationships.html",
            "reading-library.html": "reading-library.html",
            "tools.html": "tools.html",
            "trust.html": "trust.html",
            "wellbeing.html": "wellbeing.html",
        }
        for filename, target in targets.items():
            nav = self.main_nav(self.read(filename))
            self.assertIn('href="' + target + '" aria-current="page"', nav)

    def test_shared_menu_supports_escape_and_updates_expanded_state(self):
        script = self.read("site.js")
        self.assertIn('event.key==="Escape"', script)
        self.assertIn('menu.setAttribute("aria-expanded","true")', script)
        self.assertIn('menu.setAttribute("aria-expanded","false")', script)
        self.assertIn('menu.textContent="Close"', script)
        self.assertIn('menu.textContent="Menu"', script)

    def test_homepage_exposes_both_existing_learning_destinations(self):
        home = self.read("index.html")
        self.assertIn('href="relationships.html">Explore Relationship Corner', home)
        self.assertIn('href="reading-library.html">Browse the Reading Library', home)
        self.assertIn("40 relationship concepts", home)
        self.assertIn("49 source-linked catalogue entries", home)
        self.assertIn("A book does not ask you to hurry; it simply leaves the next page open.", home)
        self.assertEqual(4, home.count("<section"))

    def test_library_format_filters_display_live_counts(self):
        page = self.read("reading-library.html")
        for kind in ("book", "video", "audiobook", "audio", "article", "blog", "image"):
            self.assertIn('data-content-type="' + kind + '"', page)
        self.assertIn("Counts show catalogue entries for each format.", page)
        self.assertIn('className="kind-count"', page)
        data = json.loads(self.read("data/library.json"))
        self.assertEqual(49, len(data["records"]))
        expected = {"book", "video", "audiobook", "audio", "article", "blog", "image"}
        available = {kind for record in data["records"] for kind in record.get("contentTypes", [])}
        self.assertEqual(expected, available)

    def test_relationship_corner_and_original_reading_shelves_remain(self):
        relationships = self.read("relationships.html")
        library = self.read("reading-library.html")
        self.assertEqual(40, relationships.count('class="concept-item"'))
        self.assertIn("attachment protest", relationships.lower())
        for shelf in ("Free downloads", "Relationship learning", "Attachment books", "Sacred texts", "GitHub source", "Reuse rules"):
            self.assertIn(shelf, library)
        data = json.loads(self.read("data/library.json"))
        self.assertEqual(49, len(data["records"]))

    def test_legacy_page_specific_menu_handlers_are_removed(self):
        for filename in ("relationships.html", "check-ins.html"):
            page = self.read(filename)
            self.assertNotIn('getElementById("menu-toggle")', page)
            self.assertNotIn('getElementById("navlinks")', page)
            self.assertNotIn('getElementById("quick-exit")', page)

if __name__ == "__main__":
    unittest.main()
