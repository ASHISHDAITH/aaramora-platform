import json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class HomepageReleaseTests(unittest.TestCase):
    def test_homepage_is_five_section_and_four_destination(self):
        h=(ROOT/"index.html").read_text(encoding="utf-8")
        self.assertEqual(5,len(re.findall(r"<section\\b",h,re.I)))
        nav=re.search(r'<nav class="main-nav"[^>]*>(.*?)</nav>',h,re.I|re.S)
        self.assertIsNotNone(nav)
        self.assertEqual(4,len(re.findall(r"<a\\b",nav.group(1),re.I)))
        for dest in ("get-help.html","wellbeing.html","tools.html","trust.html"):
            self.assertIn(dest,nav.group(1))
    def test_homepage_has_no_remote_media(self):
        h=(ROOT/"index.html").read_text(encoding="utf-8")
        self.assertNotRegex(h,r'(?:src|poster)=["\\']https?://')
        for banned in ("cdn.jsdelivr.net","images.unsplash.com","unsplash.com","@main"):
            self.assertNotIn(banned,h)
        for asset in ("assets/illustrations/journal.svg","assets/illustrations/garden.svg","assets/illustrations/appointment.svg"):
            self.assertIn(asset,h)
            self.assertTrue((ROOT/asset).is_file())
    def test_homepage_social_metadata_and_seo_files(self):
        h=(ROOT/"index.html").read_text(encoding="utf-8")
        for meta in ('property="og:title"','property="og:description"','property="og:image"','name="twitter:card"'):
            self.assertIn(meta,h)
        for asset in ("favicon.svg","manifest.webmanifest","sitemap.xml","robots.txt","service-worker.js"):
            self.assertTrue((ROOT/asset).is_file())
    def test_main_navigation_is_four_destinations_on_active_pages(self):
        pages=["get-help.html","access-map.html","tools.html","trust.html","about.html","gentle-activities.html","wellbeing.html","relationships.html","check-ins.html","yoga-and-breath.html","reading-library.html"]
        for page in pages:
            h=(ROOT/page).read_text(encoding="utf-8")
            nav=re.search(r'<nav class="main-nav"[^>]*>(.*?)</nav>',h,re.I|re.S)
            self.assertIsNotNone(nav,page)
            self.assertEqual(4,len(re.findall(r"<a\\b",nav.group(1),re.I)),page)
    def test_only_two_crisis_numbers_are_published(self):
        pages=[p for p in ROOT.glob("*.html") if p.name not in ("privacy.html",)]
        for p in pages:
            h=p.read_text(encoding="utf-8")
            self.assertNotIn("1800-89-14416",h,p.name)
            self.assertNotIn("18008914416",h,p.name)
            self.assertNotRegex(h,r'href=["\\']tel:181')
        help_page=(ROOT/"get-help.html").read_text(encoding="utf-8")
        for token in ("14416","112","24 November 2026"):
            self.assertIn(token,help_page)
    def test_offline_support_page_is_precached(self):
        sw=(ROOT/"service-worker.js").read_text(encoding="utf-8")
        for item in ('"/get-help.html"','"/offline.html"','"/site.css"','"/site.js"'):
            self.assertIn(item,sw)
        self.assertTrue((ROOT/"offline.html").is_file())
    def test_tools_do_not_persist_or_transmit_personal_entries(self):
        h=(ROOT/"tools.html").read_text(encoding="utf-8")
        js=(ROOT/"site.js").read_text(encoding="utf-8")
        for feature in ("tonight-toggle","safety-plan-form","words-library","appointment-form","appointment-bridge"):
            self.assertIn(feature,h)
        for banned in ("localStorage","sessionStorage","sendBeacon","XMLHttpRequest"):
            self.assertNotIn(banned,js)
        self.assertIn("window.print()",js)
if __name__=="__main__":unittest.main()
