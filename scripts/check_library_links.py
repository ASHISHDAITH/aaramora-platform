#!/usr/bin/env python3
"""Check catalogue source URLs politely; never download or parse book contents."""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit, urlunsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "library.json"
USER_AGENT = "AARAMORA-Library-Link-Checker/1.0 (metadata links only)"
TIMEOUT_SECONDS = 18
PAUSE_SECONDS = 0.5
CONFIRMED_DEAD = {404, 410}


def collect_urls(data: dict) -> list[str]:
    urls = set()
    for group in data.get("languageGroups", []):
        urls.update(group.get("sourceUrls", []))
    for record in data.get("records", []):
        urls.add(record.get("access", {}).get("url", ""))
        urls.add(record.get("rights", {}).get("policyUrl", ""))
        for key in ("sourceUrl", "metadataUrl", "languageCoverageUrl", "policyUrl"):
            urls.add(record.get("provenance", {}).get(key, ""))
    return sorted(url for url in urls if isinstance(url, str) and url.startswith("https://"))


def request_url(url: str) -> str:
    """Percent-encode Unicode path/query characters for HTTP clients."""
    parts = urlsplit(url)
    path = quote(parts.path, safe="/%:@-._~!$&()*+,;=")
    query = quote(parts.query, safe="=&%/:?@!$*()+,;~-._")
    return urlunsplit((parts.scheme, parts.netloc, path, query, parts.fragment))


def safe_console(value: object) -> str:
    """Render original Unicode URLs safely on runners with ASCII stdout."""
    encoding = sys.stdout.encoding or "utf-8"
    return str(value).encode(encoding, errors="backslashreplace").decode(encoding)


def request_status(url: str) -> tuple[str, str]:
    encoded_url = request_url(url)
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/json;q=0.8,*/*;q=0.5",
    }
    try:
        request = Request(encoded_url, headers=headers, method="HEAD")
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return "ok", f"HTTP {response.status} · {response.geturl()}"
    except HTTPError as error:
        if error.code in CONFIRMED_DEAD:
            return "dead", f"HTTP {error.code}"
        if error.code in (403, 405, 429, 501):
            # Some repositories block HEAD; retry with a one-byte range request.
            pass
        else:
            return "inconclusive", f"HTTP {error.code} (not treated as a dead link)"
    except (URLError, TimeoutError, OSError) as error:
        return "inconclusive", f"network issue: {error}"

    try:
        range_headers = dict(headers)
        range_headers["Range"] = "bytes=0-0"
        request = Request(encoded_url, headers=range_headers, method="GET")
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            response.read(1)
            return "ok", f"HTTP {response.status} · range request · {response.geturl()}"
    except HTTPError as error:
        if error.code in CONFIRMED_DEAD:
            return "dead", f"HTTP {error.code}"
        return "inconclusive", f"HTTP {error.code} (access may be restricted)"
    except (URLError, TimeoutError, OSError) as error:
        return "inconclusive", f"network issue: {error}"


def write_summary(lines: list[tuple[str, str, str]]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    with open(summary_path, "a", encoding="utf-8") as summary:
        summary.write("## AARAMORA reading-library link check\n\n")
        summary.write("Only source/rights metadata URLs were checked. No book content was downloaded.\n\n")
        summary.write("| Result | URL | Detail |\n|---|---|---|\n")
        for result, url, detail in lines:
            summary.write(f"| {result} | {url} | {detail.replace('|', '/')} |\n")


def main() -> int:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    urls = collect_urls(data)
    results = []
    for index, url in enumerate(urls):
        status, detail = request_status(url)
        results.append((status, url, detail))
        print(safe_console(f"{status.upper():12} {url} · {detail}"))
        if index + 1 < len(urls):
            time.sleep(PAUSE_SECONDS)
    write_summary(results)
    dead = [item for item in results if item[0] == "dead"]
    inconclusive = [item for item in results if item[0] == "inconclusive"]
    print(f"\nChecked {len(urls)} URLs: {len(results)-len(dead)-len(inconclusive)} reachable, "
          f"{len(dead)} confirmed dead, {len(inconclusive)} inconclusive.")
    if dead:
        print("Confirmed dead links require editorial review.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
