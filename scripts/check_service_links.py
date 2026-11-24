#!/usr/bin/env python3
"""Check AARAMORA's two public support-source URLs without downloading page bodies."""
from __future__ import annotations
import json
import sys
import time
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]
REGISTER=ROOT/"data"/"service-links.json"
USER_AGENT="AARAMORA-Service-Link-Checker/2.0 (official support sources only)"
TIMEOUT_SECONDS=12
PAUSE_SECONDS=0.4
CONFIRMED_DEAD={404,410}
RESTRICTED_HEAD={403,405,429,501}
ALLOWED_TELS={"14416","112"}

def load_records() -> list[dict]:
    data=json.loads(REGISTER.read_text(encoding="utf-8"))
    records=data.get("records")
    if not isinstance(records,list) or not records:
        raise ValueError("service-links.json must contain a non-empty records array")
    seen=set()
    visible=set()
    for record in records:
        required={"id","name","category","displayedNumbers","officialSourceUrl","lastVerified","nextReview","owner","reviewStatus","humanSignOff","caveat"}
        missing=required-record.keys()
        if missing:
            raise ValueError(f"{record.get('id','<unknown>')} missing fields: {sorted(missing)}")
        if record["id"] in seen:
            raise ValueError(f"duplicate support record id: {record['id']}")
        seen.add(record["id"])
        if not record["officialSourceUrl"].startswith("https://"):
            raise ValueError(f"{record['id']} official source must use HTTPS")
        date.fromisoformat(record["lastVerified"])
        date.fromisoformat(record["nextReview"])
        if not record["displayedNumbers"]:
            raise ValueError(f"{record['id']} must have at least one displayed number")
        for item in record["displayedNumbers"]:
            if not item.get("tel") or not item.get("label"):
                raise ValueError(f"{record['id']} has an incomplete displayed number")
            visible.add(item["tel"])
        if record.get("secondarySourceUrl") and not record["secondarySourceUrl"].startswith("https://"):
            raise ValueError(f"{record['id']} secondary source must use HTTPS")
    if visible != ALLOWED_TELS:
        raise ValueError(f"Public source register must expose only {sorted(ALLOWED_TELS)}, got {sorted(visible)}")
    if seen != {"tele-manas","erss-112"}:
        raise ValueError(f"Unexpected public national contact records: {sorted(seen)}")
    return records

def check_url(url: str) -> tuple[str,str]:
    headers={"User-Agent":USER_AGENT,"Accept":"text/html,application/json;q=0.8,*/*;q=0.5"}
    head_detail="HEAD request did not complete"
    try:
        request=Request(url,headers=headers,method="HEAD")
        with urlopen(request,timeout=TIMEOUT_SECONDS) as response:
            return "ok",f"HTTP {response.status} · {response.geturl()}"
    except HTTPError as error:
        head_detail=f"HEAD HTTP {error.code}"
        if error.code not in CONFIRMED_DEAD|RESTRICTED_HEAD:
            return "inconclusive",f"{head_detail} (not treated as a dead link)"
    except (URLError,TimeoutError,OSError) as error:
        return "inconclusive",f"HEAD network/TLS issue: {error}"
    try:
        range_headers=dict(headers)
        range_headers["Range"]="bytes=0-0"
        request=Request(url,headers=range_headers,method="GET")
        with urlopen(request,timeout=TIMEOUT_SECONDS) as response:
            response.read(1)
            return "ok",f"HTTP {response.status} · one-byte range · {response.geturl()}"
    except HTTPError as error:
        if error.code in CONFIRMED_DEAD:
            return "dead",f"{head_detail}; range request HTTP {error.code}"
        return "inconclusive",f"{head_detail}; range request HTTP {error.code} (access may be restricted)"
    except (URLError,TimeoutError,OSError) as error:
        return "inconclusive",f"{head_detail}; range request network/TLS issue: {error}"

def write_summary(results:list[tuple[str,str,str]]) -> None:
    summary_path=__import__("os").environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    with open(summary_path,"a",encoding="utf-8") as summary:
        summary.write("## AARAMORA official support-source link check\n\n")
        summary.write("Only the two approved national support routes were checked. No visitor data or source-page body was downloaded.\n\n")
        summary.write("| Result | Source | Detail |\n|---|---|---|\n")
        for status,label,detail in results:
            summary.write(f"| {status} | {label} | {detail.replace('|','/')} |\n")

def main() -> int:
    records=load_records()
    urls=[]
    for record in records:
        urls.append((record["name"],record["officialSourceUrl"]))
        secondary=record.get("secondarySourceUrl")
        if secondary:
            urls.append((record["name"]+" secondary",secondary))
    results=[]
    for index,(label,url) in enumerate(urls):
        status,detail=check_url(url)
        results.append((status,f"{label} · {url}",detail))
        print(f"{status.upper():12} {label} · {url} · {detail}")
        if index+1<len(urls):
            time.sleep(PAUSE_SECONDS)
    write_summary(results)
    dead=[item for item in results if item[0]=="dead"]
    inconclusive=[item for item in results if item[0]=="inconclusive"]
    print(f"\nChecked {len(results)} official source URLs: {len(results)-len(dead)-len(inconclusive)} reachable, {len(dead)} confirmed dead, {len(inconclusive)} inconclusive.")
    if dead:
        print("Confirmed dead source links require human editorial review.",file=sys.stderr)
        return 1
    return 0

if __name__=="__main__":
    raise SystemExit(main())
