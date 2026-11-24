from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class HomepageReleaseTests(unittest.TestCase):
    def test_homepage_has_four_sections_and_six_primary_destinations(self):
        home = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertEqual(4, home.count("<section"))
        self.assertIn('id="hero-choices"', home)
        hero = home.split('<section class="hero"', 1)[1].split("</section>", 1)[0]
        self.assertLess(hero.index('id="hero-choices"'), hero.index('href="about.html"'))
        nav = home.split('<nav class="main-nav"', 1)[1].split("</nav>", 1)[0]
        self.assertEqual(6, nav.count("<a "))
        for target in ("get-help.html", "wellbeing.html", "tools.html", "relationships.html", "reading-library.html", "trust.html"):
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

    def test_active_pages_share_six_primary_navigation_destinations_and_mobile_toggle(self):
        pages = ("get-help.html", "access-map.html", "tools.html", "trust.html", "about.html",
                 "gentle-activities.html", "wellbeing.html", "relationships.html", "check-ins.html",
                 "yoga-and-breath.html", "reading-library.html")
        for filename in pages:
            page = (ROOT / filename).read_text(encoding="utf-8")
            nav = page.split('<nav class="main-nav"', 1)[1].split("</nav>", 1)[0]
            self.assertEqual(6, nav.count("<a "), filename)
            self.assertIn('class="menu-toggle"', page, filename)
            self.assertIn('aria-controls="site-nav"', page, filename)
            self.assertIn('href="relationships.html"', nav, filename)
            self.assertIn('href="reading-library.html"', nav, filename)

    def test_relationship_corner_and_reading_library_are_top_level_routes(self):
        home = (ROOT / "index.html").read_text(encoding="utf-8")
        for target in ("relationships.html", "reading-library.html"):
            self.assertIn('href="' + target + '"', home)
            self.assertTrue((ROOT / target).is_file())

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

    def test_feedback_link_is_untracked_and_discloses_mailto_limit(self):
        for filename in ("index.html","get-help.html","access-map.html","tools.html","trust.html","privacy.html"):
            page=(ROOT/filename).read_text(encoding="utf-8")
            self.assertIn("Was this helpful? Report a problem",page,filename)
            self.assertIn("mailto:?subject=AARAMORA%20problem%20report",page,filename)
        trust=(ROOT/"trust.html").read_text(encoding="utf-8")
        self.assertIn("public recipient address is not configured",trust.lower())

    def test_skip_links_target_a_real_main_landmark_on_every_page(self):
        for path in ROOT.glob("*.html"):
            page=path.read_text(encoding="utf-8")
            match=re.search(r'<a[^>]*class="skip-link"[^>]*href="#([^"]+)"',page)
            if match:
                target=match.group(1)
                self.assertTrue(('id="'+target+'"' in page) or ("id='"+target+"'" in page), path.name)

    def test_find_a_person_pathway_opens_the_pune_access_map(self):
        home=(ROOT/"index.html").read_text(encoding="utf-8")
        before=home.split("<h3>Find a person</h3>",1)[0][-350:]
        self.assertIn('href="access-map.html"',before)
        self.assertIn("25 Pune service listings",home)

    def test_offline_support_card_has_a_quick_exit(self):
        page=(ROOT/"offline.html").read_text(encoding="utf-8")
        self.assertIn('href="about:blank"',page)
        self.assertIn("Quick Exit",page)

if __name__ == "__main__":
    unittest.main()
