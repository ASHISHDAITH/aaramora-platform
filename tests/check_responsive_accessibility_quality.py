from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ResponsiveAccessibilityQualityTests(unittest.TestCase):
    def read(self, path):
        return (ROOT / path).read_text(encoding="utf-8")

    def test_mobile_navigation_has_a_no_javascript_fallback(self):
        css = self.read("site.css")
        script = self.read("site.js")
        self.assertIn('html:not(.js-enabled) .main-nav', css)
        self.assertIn('html:not(.js-enabled) .menu-toggle', css)
        self.assertIn('document.documentElement.classList.add("js-enabled")', script)

    def test_menu_supports_escape_outside_pointer_and_breakpoint_changes(self):
        script = self.read("site.js")
        self.assertIn('event.key==="Escape"', script)
        self.assertIn('addEventListener("pointerdown"', script)
        self.assertIn('window.matchMedia("(max-width: 820px)")', script)
        self.assertIn('mobileQuery.addEventListener("change"', script)
        self.assertIn('menu.focus()', script)

    def test_focus_and_contrast_quality_rules_are_present(self):
        css = self.read("site.css")
        self.assertIn('summary:focus-visible', css)
        self.assertIn('[role="button"]:focus-visible', css)
        self.assertIn('.eyebrow,.kicker{color:#506456}', css)
        self.assertIn('.service-meta{color:#526157}', css)
        self.assertIn('.verify{color:#53645A}', css)
        self.assertIn('body[data-theme="tonight"] .verify{color:#D7DCCF}', css)
        self.assertIn('body[data-theme="tonight"] .muted,body[data-theme="tonight"] .service-meta,body[data-theme="tonight"] .verify,body[data-theme="tonight"] .format-count-note{color:#F6F0E1}', css)
        self.assertIn('.support-line,.support-links{', css)
        self.assertIn('gap:8px 12px;flex-wrap:wrap', css)
        self.assertIn('.support-ribbon .support-line a,.support-ribbon .support-links a,.support-ribbon .support-link', css)
        self.assertIn('@media(forced-colors:active)', css)
        self.assertIn('@media(prefers-contrast:more)', css)

    def test_large_text_reflow_keeps_trust_cta_and_closed_footer_panel_in_flow(self):
        css = self.read("site.css")
        self.assertIn(".trust-strip>*{min-width:0;max-width:100%}", css)
        self.assertIn(".trust-cta{white-space:normal}", css)
        self.assertIn(".footer-more:not([open]) .footer-more-panel{display:none}", css)
        self.assertIn("max-width:calc(100vw - 32px)", css)
        self.assertIn(".hero-grid,.hero-grid>*{min-width:0;max-width:100%}", css)
        self.assertIn(".hero-photo img{display:block;width:100%;max-width:100%;min-width:0}", css)
        self.assertIn(".catalog-card h3,.section-head h2{overflow-wrap:anywhere;word-break:normal}", css)

    def test_reduced_motion_and_mobile_reflow_rules_are_present(self):
        css = self.read("site.css")
        self.assertIn('@media(prefers-reduced-motion:reduce)', css)
        self.assertIn('max-width:600px', css)
        self.assertIn('max-width:360px', css)
        self.assertIn('.wrap{width:calc(100% - 26px)}', css)

    def test_head_initializes_navigation_before_styles_to_prevent_mobile_shift(self):
        for page in ROOT.glob("*.html"):
            html = page.read_text(encoding="utf-8")
            head = html[:html.lower().find("</head>")]
            if 'name="viewport"' not in head:
                continue
            marker = '<script>document.documentElement.classList.add("js-enabled");</script>'
            self.assertIn(marker, head, f"{page.name} needs the early JS enhancement marker")
            self.assertLess(head.index('name="viewport"'), head.index(marker))
            first_style = min(
                (pos for pos in (head.find("<style"), head.find('rel="stylesheet"')) if pos >= 0),
                default=len(head),
            )
            self.assertLess(head.index(marker), first_style, f"{page.name} initializes after CSS")

    def test_all_pages_link_the_shared_favicon(self):
        for page in ROOT.glob("*.html"):
            html = page.read_text(encoding="utf-8")
            head = html[:html.lower().find("</head>")]
            self.assertIn('href="/favicon.svg"', head, f"{page.name} is missing the shared favicon")

    def test_lighthouse_contrast_fixes_are_present(self):
        css = self.read("site.css")
        self.assertIn(".hero-foot{color:#526157}", css)
        self.assertIn("#concept-count,.concept-note,.concept-item summary small{color:#526157}", css)
        self.assertIn(".support-ribbon small{color:#4E5F54}", css)
        library = self.read("reading-library.html")
        self.assertIn('badge.textContent=String(count);', library)
        self.assertNotIn('badge.setAttribute("aria-hidden","true")', library)
        self.assertNotIn('button.setAttribute("aria-label",', library)

    def test_common_controls_retain_practical_touch_targets(self):
        css = self.read("site.css")
        self.assertIn('button,.button,.quiet-button,.menu-toggle,.quick-exit,.footer-more summary{min-height:44px}', css)

    def test_relationship_and_reading_library_content_is_unchanged(self):
        relationships = self.read("relationships.html")
        library_page = self.read("reading-library.html")
        library = json.loads(self.read("data/library.json"))
        self.assertEqual(40, relationships.count('class="concept-item"'))
        self.assertEqual(49, len(library["records"]))
        for shelf in (
            "free-downloads", "scripture-shelf", "workbooks-and-articles",
            "relationship-open-learning", "attachment-books", "faith-wisdom",
            "novels-and-classics", "github-shelves", "licensing"
        ):
            self.assertIn('id="' + shelf + '"', library_page)


if __name__ == "__main__":
    unittest.main()
