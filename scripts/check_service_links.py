#!/usr/bin/env python3
"""Check AARAMORA official helpline-source URLs without downloading page bodies."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "data" / "service-links.json"
USER_AGENT = "AARAMORA-Service-Link-Checker/1.0 (official source URLs only)"
TIMEOUT_SECONDS = 12
PAUSE_SECONDS = 0.4
CONFIRMED_DEAD = {404, 410}
RESTRICTED_HEAD = {403, 405, 429, 501}


def load_records() -> list[dict]:
    data = json.loads(REGISTER.read_text(encoding="utf-8"))
    records = data.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("service-links.json must contain a non-empty records array")
    required = {
        "id", "service", "displayedNumbers", "availability", "geography",
        "officialSourceUrl", "lastVerified", "nextReview", "owner", "caveat"
    }
    seen = set()
    for record in records:
        missing = required - record.keys()
        if missing:
            raise ValueError(f"{record.get('id', '<unknown>')} missing fields: {sorted(missing)}")
        if record["id"] in seen:
            raise ValueError(f"duplicate record id: {record['id']}")
        seen.add(record["id"])
        if not record["officialSourceUrl"].startswith("https://"):
            raise ValueError(f"{record['id']} source must use HTTPS")
        if not record["displayedNumbers"]:
            raise ValueError(f"{record['id']} must include at least one displayed number")
        for number in record["displayedNumbers"]:
            if not number.get("display") or not number.get("tel") or not number.get("purpose"):
                raise ValueError(f"{record['id']} has an incomplete number entry")
    return records


def check_url(url: str) -> tuple[str, str]:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/json;q=0.8,*/*;q=0.5",
    }
    try:
        request = Request(url, headers=headers, method="HEAD")
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return "ok", f"HTTP {response.status} · {response.geturl()}"
    except HTTPError as error:
        if error.code in CONFIRMED_DEAD:
            return "dead", f"HTTP {error.code}"
        if error.code not in RESTRICTED_HEAD:
            return "inconclusive", f"HTTP {error.code}"
    except (URLError, TimeoutError, OSError) as error:
        return "inconclusive", f"network issue: {error}"

    # Some official government hosts reject HEAD. Ask for one byte only.
    try:
        range_headers = dict(headers)
        range_headers["Range"] = "bytes=0-0"
        request = Request(url, headers=range_headers, method="GET")
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            response.read(1)
            return "ok", f"HTTP {response.status} · one-byte range · {response.geturl()}"
    except HTTPError as error:
        if error.code in CONFIRMED_DEAD:
            return "dead", f"HTTP {error.code}"
        return "inconclusive", f"HTTP {error.code} (access may be restricted)"
    except (URLError, TimeoutError, OSError) as error:
        return "inconclusive", f"network issue: {error}"


def write_summary(results: list[tuple[str, str, str]]) -> None:
    summary_path = __import__("os").environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    with open(summary_path, "a", encoding="utf-8") as summary:
        summary.write("## AARAMORA official support-source link check\n\n")
        summary.write("Only source URLs were checked. No visitor data or source-page body was downloaded.\n\n")
        summary.write("| Result | Service source | Detail |\n|---|---|---|\n")
        for status, service, detail in results:
            summary.write(f"| {status} | {service} | {detail.replace('|', '/')} |\n")


def main() -> int:
    records = load_records()
    results = []
    for index, record in enumerate(records):
        urls = [record["officialSourceUrl"]]
        secondary = record.get("secondaryOfficialSourceUrl")
        if secondary:
            urls.append(secondary)
        for url in urls:
            status, detail = check_url(url)
            results.append((status, f"{record['service']} · {url}", detail))
            print(f"{status.upper():12} {record['service']} · {url} · {detail}")
            if len(results) < sum(1 + bool(r.get("secondaryOfficialSourceUrl")) for r in records):
                time.sleep(PAUSE_SECONDS)
    write_summary(results)
    dead = [x for x in results if x[0] == "dead"]
    inconclusive = [x for x in results if x[0] == "inconclusive"]
    print(f"\nChecked {len(results)} official source URLs: "
          f"{len(results)-len(dead)-len(inconclusive)} reachable, "
          f"{len(dead)} confirmed dead, {len(inconclusive)} inconclusive.")
    if dead:
        print("Confirmed dead source links require human editorial review.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
