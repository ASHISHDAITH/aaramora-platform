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
        "text_resize_checks": [],
        "errors": [],
    }
    server = start_server()
    server_stopped = False

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

            # Text-only 200% enlargement emulation on the four key journeys.
            text_selector = "h1,h2,h3,h4,h5,h6,p,a,button,label,input,select,textarea,li,summary,small,span,strong,em,dt,dd,th,td,figcaption,blockquote"
            for filename in ["index.html", "get-help.html", "relationships.html", "reading-library.html"]:
                for width in [768, 390, 320]:
                    text_context = browser.new_context(
                        viewport={"width": width, "height": 900},
                        service_workers="block",
                    )
                    text_context.route(
                        "**/*",
                        lambda route: route.continue_()
                        if route.request.url.startswith(BASE_URL)
                        else route.abort(),
                    )
                    text_page = text_context.new_page()
                    response = text_page.goto(
                        BASE_URL + page_path(filename), wait_until="load", timeout=30000
                    )
                    resize_result = text_page.evaluate(
                        """selector => {
                          const elements = [...document.querySelectorAll(selector)];
                          // Snapshot every original computed size before mutating any parent element.
                          // This prevents inherited child sizes from being accidentally doubled twice.
                          const originalSizes = elements.map(element => ({
                            element,
                            size: Number.parseFloat(getComputedStyle(element).fontSize)
                          }));
                          let enlarged = 0;
                          for (const item of originalSizes) {
                            if (!Number.isFinite(item.size) || item.size <= 0) continue;
                            item.element.style.setProperty("font-size", (item.size * 2) + "px", "important");
                            enlarged += 1;
                          }
                          const overflowingElements = [...document.body.querySelectorAll("*")]
                            .map(element => {
                              const rect = element.getBoundingClientRect();
                              return {
                                tag: element.tagName.toLowerCase(),
                                id: element.id || "",
                                className: typeof element.className === "string" ? element.className : "",
                                text: (element.innerText || element.getAttribute("aria-label") || "").trim().slice(0, 90),
                                left: Math.round(rect.left),
                                right: Math.round(rect.right),
                                width: Math.round(rect.width),
                                clientWidth: element.clientWidth,
                                scrollWidth: element.scrollWidth,
                                display: getComputedStyle(element).display
                              };
                            })
                            .filter(element => element.right > window.innerWidth + 1 || element.left < -1)
                            .slice(0, 16);
                          return {
                            enlargedTextElements: enlarged,
                            documentWidth: document.documentElement.scrollWidth,
                            bodyWidth: document.body.scrollWidth,
                            viewportWidth: window.innerWidth,
                            headingVisible: Boolean(document.querySelector("main h1")?.getClientRects().length),
                            overflowingElements
                          };
                        }""",
                        text_selector,
                    )
                    resize_result.update({"page": filename, "viewport": width, "mode": "text-only 200% emulation"})
                    results["text_resize_checks"].append(resize_result)
                    if response is None or not response.ok:
                        results["errors"].append(f"{filename} at {width}px: 200% text-resize page response was not OK")
                    if resize_result["documentWidth"] > width + 1 or resize_result["bodyWidth"] > width + 1:
                        results["errors"].append(
                            f"{filename} at {width}px: horizontal overflow under 200% text enlargement "
                            f"({resize_result['documentWidth']}px document)"
                        )
                    if not resize_result["headingVisible"]:
                        results["errors"].append(f"{filename} at {width}px: main heading is not visible after text enlargement")
                    if width in [390, 320]:
                        text_page.screenshot(
                            path=str(SCREENSHOT_DIR / f"text-200-{filename.replace('.html','')}-{width}.png"),
                            full_page=True,
                        )
                    text_context.close()

            # Slow-network smoke test with a throttled 3G-like profile.
            slow_context = browser.new_context(
                viewport={"width": 390, "height": 844},
                service_workers="block",
            )
            slow_context.route(
                "**/*",
                lambda route: route.continue_()
                if route.request.url.startswith(BASE_URL)
                else route.abort(),
            )
            slow_page = slow_context.new_page()
            slow_cdp = slow_context.new_cdp_session(slow_page)
            slow_cdp.send("Network.enable")
            slow_cdp.send(
                "Network.emulateNetworkConditions",
                {
                    "offline": False,
                    "latency": 400,
                    "downloadThroughput": 128 * 1024,
                    "uploadThroughput": 64 * 1024,
                    "connectionType": "cellular3g",
                },
            )
            slow_started = time.monotonic()
            slow_response = slow_page.goto(
                BASE_URL + "/", wait_until="domcontentloaded", timeout=60000
            )
            slow_page.locator("main h1").wait_for(timeout=20000)
            slow_elapsed = round(time.monotonic() - slow_started, 2)
            results["slow_network"] = {
                "profile": "400ms latency / 128KBps down / 64KBps up",
                "response_ok": bool(slow_response and slow_response.ok),
                "main_heading_visible": slow_page.locator("main h1").is_visible(),
                "elapsed_seconds_to_domcontentloaded_and_heading": slow_elapsed,
            }
            if not results["slow_network"]["response_ok"] or not results["slow_network"]["main_heading_visible"]:
                results["errors"].append("Homepage did not render its main heading under the throttled network profile.")
            slow_context.close()

            # Install the first-party service worker online, then test its offline cache/fallback.
            offline_context = browser.new_context(
                viewport={"width": 390, "height": 844},
                service_workers="allow",
            )
            offline_page = offline_context.new_page()
            offline_console = []
            offline_page.on(
                "console",
                lambda message: offline_console.append(message.text) if message.type == "error" else None,
            )
            offline_page.on("pageerror", lambda error: offline_console.append(str(error)))
            offline_response = offline_page.goto(
                BASE_URL + "/", wait_until="load", timeout=30000
            )
            worker_response = offline_page.request.get(BASE_URL + "/service-worker.js")
            worker_headers = worker_response.headers
            registration = offline_page.evaluate(
                """async () => {
                  try {
                    const response = await fetch("/service-worker.js", {cache:"no-store"});
                    const source = await response.text();
                    const reg = await navigator.serviceWorker.register("/service-worker.js");
                    return {
                      ok: true,
                      scriptStatus: response.status,
                      scriptType: response.headers.get("content-type"),
                      scriptBytes: source.length,
                      scope: reg.scope,
                      activeState: reg.active ? reg.active.state : null,
                      installingState: reg.installing ? reg.installing.state : null
                    };
                  } catch (error) {
                    return {ok:false, name:error.name, message:error.message, stack:error.stack};
                  }
                }"""
            )
            offline_ready = False
            ready_error = None
            if registration.get("ok"):
                try:
                    offline_page.wait_for_function(
                        "navigator.serviceWorker.controller !== null", timeout=15000
                    )
                    offline_ready = True
                except Exception as error:
                    ready_error = str(error)
            results["offline"] = {
                "online_install_response_ok": bool(offline_response and offline_response.ok),
                "worker_script_status": worker_response.status,
                "worker_script_content_type": worker_headers.get("content-type"),
                "registration": registration,
                "controller_ready": offline_ready,
                "ready_error": ready_error,
                "console_errors": offline_console[:12],
                "cached_assets": {},
                "cached_homepage_available": False,
                "offline_fallback_available": False,
            }
            if not registration.get("ok") or not offline_ready:
                results["errors"].append(
                    "Service worker registration/controller failed: "
                    + json.dumps(results["offline"], ensure_ascii=False)[:1800]
                )
                offline_context.close()
            else:
                cached = offline_page.evaluate(
                    """async () => ({
                      offlinePage: Boolean(await caches.match("/offline.html")),
                      homepage: Boolean(await caches.match("/index.html")),
                      stylesheet: Boolean(await caches.match("/site.css"))
                    })"""
                )
                # Stop the local origin as well as toggling browser offline mode.
                # Chromium can still reach loopback servers during offline emulation.
                server.shutdown()
                server.server_close()
                server_stopped = True
                # Stop the origin only after the service worker has precached its support shell.
                # This avoids localhost network-emulation exceptions and proves the worker cache responds.
                server.shutdown()
                server.server_close()
                server_stopped = True
                offline_context.set_offline(True)
                cached_home_response = offline_page.goto(
                    BASE_URL + "/index.html", wait_until="load", timeout=15000
                )
                cached_home_ok = (
                    cached_home_response is not None
                    and cached_home_response.ok
                    and offline_page.locator("main h1").is_visible()
                )
                fallback_path = "/__offline-audit-never-cached-2026.html"
                fallback_response = offline_page.goto(
                    BASE_URL + fallback_path, wait_until="load", timeout=15000
                )
                fallback_body = offline_page.locator("body").inner_text()
                helpline_14416_links = offline_page.locator('a[href="tel:14416"]').count()
                emergency_112_links = offline_page.locator('a[href="tel:112"]').count()
                fallback_ok = (
                    fallback_response is not None
                    and fallback_response.ok
                    and "Offline support" in offline_page.title()
                    and "Support details saved on this device." in fallback_body
                    and helpline_14416_links > 0
                    and emergency_112_links > 0
                )
                results["offline"]["cached_assets"] = cached
                results["offline"]["cached_homepage_available"] = cached_home_ok
                results["offline"]["fallback_response_status"] = fallback_response.status if fallback_response else None
                results["offline"]["fallback_page_title"] = offline_page.title()
                results["offline"]["fallback_has_support_copy"] = "Support details saved on this device." in fallback_body
                results["offline"]["fallback_helpline_14416_link_count"] = helpline_14416_links
                results["offline"]["fallback_emergency_112_link_count"] = emergency_112_links
                results["offline"]["offline_fallback_available"] = fallback_ok
                if not all(cached.values()):
                    results["errors"].append("The service worker did not cache every required offline support asset.")
                if not cached_home_ok:
                    results["errors"].append("The previously cached homepage did not open offline.")
                if not fallback_ok:
                    results["errors"].append("An uncached page did not fall back to the offline support card with both approved numbers.")
                offline_context.close()

            context.close()
            browser.close()
    finally:
        if not server_stopped:
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
        f"slow-network={'passed' if results.get('slow_network', {}).get('response_ok') else 'failed'}; "
        f"offline={'passed' if results.get('offline', {}).get('offline_fallback_available') else 'failed'}; "
        f"errors={len(results['errors'])}."
    )
    if results["errors"]:
        for error in results["errors"]:
            print("FAIL:", error)
        raise SystemExit(1)
    print("Responsive Chromium checks passed. Screenshots: artifacts/visual-audit/")


if __name__ == "__main__":
    main()
