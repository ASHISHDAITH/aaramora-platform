from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import threading
import time

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "http://127.0.0.1:8765"
VIEWPORTS = [
    {"name": "desktop", "width": 1440, "height": 1000},
    {"name": "tablet", "width": 768, "height": 1024},
    {"name": "mobile", "width": 390, "height": 844},
    {"name": "narrow-mobile", "width": 320, "height": 740},
]
SCREENSHOT_DIR = ROOT / "artifacts" / "visual-audit"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def start_server():
    server = ThreadingHTTPServer(
        ("127.0.0.1", 8765),
        partial(QuietHandler, directory=str(ROOT)),
    )
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def page_path(path):
    return "/" if path == "index.html" else f"/{path}"


def main():
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    pages = []
    for path in sorted(ROOT.glob("*.html")):
        content = path.read_text(encoding="utf-8")
        if 'class="menu-toggle"' in content and 'class="main-nav"' in content:
            pages.append(path.name)

    if not pages:
        raise SystemExit("No menu-bearing pages were found.")

    results = {
        "base_url": BASE_URL,
        "pages": pages,
        "viewports": [],
        "navigation": [],
        "no_javascript": {},
        "preference_checks": [],
        "errors": [],
    }
    server = start_server()

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            context = browser.new_context(
                viewport={"width": 1440, "height": 1000},
                service_workers="block",
            )
            # Keep the audit deterministic and independent of third-party hosts.
            context.route(
                "**/*",
                lambda route: route.continue_()
                if route.request.url.startswith(BASE_URL)
                else route.abort(),
            )
            page = context.new_page()

            for filename in pages:
                for viewport in VIEWPORTS:
                    page.set_viewport_size(
                        {"width": viewport["width"], "height": viewport["height"]}
                    )
                    response = page.goto(
                        BASE_URL + page_path(filename),
                        wait_until="load",
                        timeout=30000,
                    )
                    if response is None or not response.ok:
                        results["errors"].append(
                            f"{filename} at {viewport['name']}: page response was not OK"
                        )
                        continue
                    page.wait_for_function(
                        "document.documentElement.classList.contains('js-enabled')",
                        timeout=5000,
                    )
                    metrics = page.evaluate(
                        """() => {
                          const width = window.innerWidth;
                          const overflowing = [...document.body.querySelectorAll('*')]
                            .map(el => {
                              const r = el.getBoundingClientRect();
                              return {tag: el.tagName.toLowerCase(),
                                cls: typeof el.className === 'string' ? el.className : '',
                                right: Math.round(r.right), left: Math.round(r.left)};
                            })
                            .filter(x => x.right > width + 1 || x.left < -1)
                            .slice(0, 8);
                          return {
                            viewport: width,
                            documentWidth: document.documentElement.scrollWidth,
                            bodyWidth: document.body.scrollWidth,
                            hasMain: Boolean(document.querySelector('main')),
                            title: document.title,
                            overflowing
                          };
                        }"""
                    )
                    check = {
                        "page": filename,
                        "viewport": viewport["name"],
                        **metrics,
                    }
                    results["viewports"].append(check)
                    if metrics["documentWidth"] > viewport["width"] + 1:
                        results["errors"].append(
                            f"{filename} at {viewport['width']}px overflows to "
                            f"{metrics['documentWidth']}px: {metrics['overflowing']}"
                        )
                    if not metrics["hasMain"] or not metrics["title"]:
                        results["errors"].append(
                            f"{filename} at {viewport['name']}: missing main landmark or title"
                        )

                    nav = page.locator(".main-nav")
                    toggle = page.locator(".menu-toggle")
                    links = nav.locator("a").count()
                    if links != 6:
                        results["errors"].append(
                            f"{filename} at {viewport['name']}: expected 6 nav links, found {links}"
                        )
                    is_mobile = viewport["width"] <= 820
                    if is_mobile and not toggle.is_visible():
                        results["errors"].append(
                            f"{filename} at {viewport['name']}: mobile menu toggle is not visible"
                        )
                    if not is_mobile and toggle.is_visible():
                        results["errors"].append(
                            f"{filename} at {viewport['name']}: desktop menu toggle should be hidden"
                        )
                    if is_mobile and nav.is_visible():
                        results["errors"].append(
                            f"{filename} at {viewport['name']}: mobile menu should start closed"
                        )

                    if is_mobile and filename in {
                        "index.html", "relationships.html", "reading-library.html", "get-help.html"
                    }:
                        toggle.focus()
                        page.keyboard.press("Enter")
                        expanded = toggle.get_attribute("aria-expanded")
                        visible = nav.is_visible()
                        results["navigation"].append({
                            "page": filename,
                            "viewport": viewport["name"],
                            "opened_with_keyboard": expanded == "true" and visible,
                        })
                        if expanded != "true" or not visible:
                            results["errors"].append(
                                f"{filename}: keyboard did not open the mobile navigation"
                            )
                        page.keyboard.press("Escape")
                        closed = (
                            toggle.get_attribute("aria-expanded") == "false"
                            and not nav.is_visible()
                            and toggle.evaluate("(el) => document.activeElement === el")
                        )
                        if not closed:
                            results["errors"].append(
                                f"{filename}: Escape did not close menu and restore focus"
                            )
                        page.mouse.click(viewport["width"] - 5, viewport["height"] - 5)
                        toggle.click()
                        page.mouse.click(viewport["width"] - 5, 200)
                        if nav.is_visible() or toggle.get_attribute("aria-expanded") != "false":
                            results["errors"].append(
                                f"{filename}: outside pointer did not close mobile navigation"
                            )

                    if filename == "index.html":
                        page.screenshot(
                            path=str(SCREENSHOT_DIR / f"home-{viewport['name']}.png"),
                            full_page=True,
                        )
                    if filename in {"relationships.html", "reading-library.html"} and viewport["name"] in {
                        "desktop", "mobile"
                    }:
                        page.screenshot(
                            path=str(SCREENSHOT_DIR / f"{filename.replace('.html','')}-{viewport['name']}.png"),
                            full_page=True,
                        )

            # Verify the mobile navigation fallback across every page, not just the homepage.
            for filename in pages:
                no_js_context = browser.new_context(
                    java_script_enabled=False,
                    viewport={"width": 390, "height": 844},
                    service_workers="block",
                )
                no_js_context.route(
                    "**/*",
                    lambda route: route.continue_()
                    if route.request.url.startswith(BASE_URL)
                    else route.abort(),
                )
                no_js_page = no_js_context.new_page()
                response = no_js_page.goto(
                    BASE_URL + page_path(filename), wait_until="load", timeout=30000
                )
                visible = (
                    response is not None
                    and response.ok
                    and no_js_page.locator(".main-nav").is_visible()
                    and not no_js_page.locator(".menu-toggle").is_visible()
                    and no_js_page.locator(".main-nav a").count() == 6
                )
                results["no_javascript"][filename] = {"mobile_navigation_visible": visible}
                if not visible:
                    results["errors"].append(
                        f"{filename}: six mobile navigation destinations are not exposed without JavaScript"
                    )
                no_js_context.close()

            # Browser preference smoke tests. These check CSS response, not human AT conformance.
            for filename in ["index.html", "get-help.html", "relationships.html", "reading-library.html"]:
                preference_context = browser.new_context(
                    viewport={"width": 390, "height": 844},
                    service_workers="block",
                    reduced_motion="reduce",
                    forced_colors="active",
                )
                preference_context.route(
                    "**/*",
                    lambda route: route.continue_()
                    if route.request.url.startswith(BASE_URL)
                    else route.abort(),
                )
                preference_page = preference_context.new_page()
                response = preference_page.goto(
                    BASE_URL + page_path(filename), wait_until="load", timeout=30000
                )
                preference_result = preference_page.evaluate(
                    """() => ({
                      forcedColors: matchMedia("(forced-colors: active)").matches,
                      reducedMotion: matchMedia("(prefers-reduced-motion: reduce)").matches,
                      scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior,
                      documentWidth: document.documentElement.scrollWidth,
                      viewportWidth: window.innerWidth
                    })"""
                )
                preference_result["page"] = filename
                results["preference_checks"].append(preference_result)
                if response is None or not response.ok:
                    results["errors"].append(f"{filename}: preference-mode page response was not OK")
                if not preference_result["forcedColors"]:
                    results["errors"].append(f"{filename}: forced-colors preference was not emulated")
                if not preference_result["reducedMotion"]:
                    results["errors"].append(f"{filename}: reduced-motion preference was not emulated")
                if preference_result["scrollBehavior"] != "auto":
                    results["errors"].append(f"{filename}: reduced motion did not disable smooth scrolling")
                if preference_result["documentWidth"] > preference_result["viewportWidth"] + 1:
                    results["errors"].append(f"{filename}: overflow in forced-colours/reduced-motion mode")
                preference_context.close()

            context.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()

    (SCREENSHOT_DIR / "results.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8"
    )
    print(
        f"Audited {len(pages)} pages at {len(VIEWPORTS)} widths; "
        f"{len(results['viewports'])} viewport checks; "
        f"{len(results['navigation'])} keyboard menu checks; "
        f"{len(results['no_javascript'])} no-JavaScript fallbacks; "
        f"{len(results['preference_checks'])} preference-mode checks; "
        f"errors={len(results['errors'])}."
    )
    if results["errors"]:
        for error in results["errors"]:
            print("FAIL:", error)
        raise SystemExit(1)
    print("Responsive Chromium checks passed. Screenshots: artifacts/visual-audit/")


if __name__ == "__main__":
    main()
