from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]

class HomepageReleaseTests(unittest.TestCase):
    def test_homepage_has_four_sections_and_four_primary_destinations(self):
        home = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertEqual(4, home.count("<section"))
        nav = home.split('<nav class="main-nav"', 1)[1].split("</nav>", 1)[0]
        self.assertEqual(4, nav.count("<a "))
        for target in ("get-help.html", "wellbeing.html", "tools.html", "trust.html"):
            self.assertIn(target, nav)

    def test_homepage_assets_are_first_party_and_original(self):
        home = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertNotIn('src="https://', home)
        self.assertNotIn('poster="https://', home)
        for text in ("cdn.jsdelivr.net", "images.unsplash.com", "unsplash.com"):
            self.assertNotIn(text, home)
        for asset in ("assets/illustrations/journal.svg", "assets/illustrations/garden.svg", "assets/illustrations/appointment.svg"):
            self.assertIn(asset, home)
            self.assertTrue((ROOT / asset).is_file())

    def test_homepage_has_open_graph_and_seo_assets(self):
        home = (ROOT / "index.html").read_text(encoding="utf-8")
        for tag in ('property="og:title"', 'property="og:description"', 'property="og:image"', 'name="twitter:card"'):
            self.assertIn(tag, home)
        for file in ("favicon.svg", "manifest.webmanifest", "sitemap.xml", "robots.txt", "service-worker.js"):
            self.assertTrue((ROOT / file).is_file())

    def test_active_pages_share_four_primary_navigation_destinations(self):
        pages = ("get-help.html", "access-map.html", "tools.html", "trust.html", "about.html",
                 "gentle-activities.html", "wellbeing.html", "relationships.html", "check-ins.html",
                 "yoga-and-breath.html", "reading-library.html")
        for filename in pages:
            page = (ROOT / filename).read_text(encoding="utf-8")
            nav = page.split('<nav class="main-nav"', 1)[1].split("</nav>", 1)[0]
            self.assertEqual(4, nav.count("<a "), filename)

    def test_no_unapproved_public_crisis_number_or_blank_alternative(self):
        for path in ROOT.glob("*.html"):
            page = path.read_text(encoding="utf-8")
            self.assertNotIn("1800-89-14416", page, path.name)
            self.assertNotIn("18008914416", page, path.name)
            self.assertNotIn("tel:181", page, path.name)
            self.assertNotIn("14416</a> or .", page, path.name)
        help_page = (ROOT / "get-help.html").read_text(encoding="utf-8")
        self.assertIn("14416", help_page)
        self.assertIn("112", help_page)
        self.assertIn("24 November 2026", help_page)

    def test_crisis_page_is_precached_for_offline_fallback(self):
        worker = (ROOT / "service-worker.js").read_text(encoding="utf-8")
        for resource in ('"/get-help.html"', '"/offline.html"', '"/site.css"', '"/site.js"'):
            self.assertIn(resource, worker)
        self.assertTrue((ROOT / "offline.html").is_file())

    def test_tools_do_not_persist_or_transmit_user_entries(self):
        page = (ROOT / "tools.html").read_text(encoding="utf-8")
        script = (ROOT / "site.js").read_text(encoding="utf-8")
        for feature in ("tonight-toggle", "safety-plan-form", "words-library", "appointment-form", "appointment-bridge"):
            self.assertIn(feature, page)
        for forbidden in ("localStorage", "sessionStorage", "sendBeacon", "XMLHttpRequest"):
            self.assertNotIn(forbidden, script)
        self.assertIn("window.print()", script)

if __name__ == "__main__":
    unittest.main()
