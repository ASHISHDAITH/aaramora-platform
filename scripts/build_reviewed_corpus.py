#!/usr/bin/env python3
"""Build a static RAG index from explicitly approved local passages only.

This is a release-gated offline tool. It does not call an LLM, embed text,
crawl sources, send network requests, or include any entry by default.
"""
from __future__ import annotations
import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "rag-corpus-manifest.json"
OUTPUT = ROOT / "data" / "rag-approved-index.json"
ACCEPTED_LICENSES = {"AARAMORA-OWNED", "CC-BY-4.0"}
REQUIRED = {
    "id", "title", "file", "language", "licenseId", "sources", "owner",
    "reviewer", "reviewedOn", "expiresOn", "approvalStatus",
    "contentStatus", "audience", "tags", "rightsVerified", "rightsReviewer", "rightsCheckedOn"
}

def eligible(entry: dict[str, Any], root: Path, today: date) -> tuple[bool, str]:
    missing = REQUIRED - entry.keys()
    if missing:
        return False, "missing_metadata:" + ",".join(sorted(missing))
    if entry.get("approvalStatus") != "approved":
        return False, "not_signed_approved"
    if entry.get("contentStatus") != "current":
        return False, "not_current"
    if entry.get("licenseId") not in ACCEPTED_LICENSES:
        return False, "rights_not_allowlisted"
    if entry.get("rightsVerified") is not True or not str(entry.get("rightsReviewer", "")).strip():
        return False, "rights_review_missing"
    try:
        rights_checked = date.fromisoformat(entry["rightsCheckedOn"])
    except (TypeError, ValueError):
        return False, "rights_review_date_invalid"
    if rights_checked > today:
        return False, "rights_review_date_in_future"
    if not str(entry.get("owner", "")).strip() or not str(entry.get("reviewer", "")).strip():
        return False, "owner_or_reviewer_missing"
    if not isinstance(entry.get("sources"), list) or not entry["sources"]:
        return False, "sources_missing"
    if not all(isinstance(s, str) and s.startswith("https://") for s in entry["sources"]):
        return False, "source_not_https"
    try:
        reviewed = date.fromisoformat(entry["reviewedOn"])
        expires = date.fromisoformat(entry["expiresOn"])
    except (TypeError, ValueError):
        return False, "invalid_review_dates"
    if reviewed > today:
        return False, "review_date_in_future"
    if expires < today:
        return False, "expired"
    rel = Path(entry["file"])
    if rel.is_absolute() or ".." in rel.parts:
        return False, "unsafe_file_path"
    path = (root / rel).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError:
        return False, "file_outside_repository"
    if not path.is_file():
        return False, "source_file_missing"
    return True, "eligible"

def build(manifest: dict[str, Any], root: Path, today: date) -> dict[str, Any]:
    entries = manifest.get("entries", [])
    if not isinstance(entries, list):
        raise ValueError("entries must be an array")
    accepted = []
    excluded = []
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict):
            excluded.append({"id": None, "reason": "entry_not_object"})
            continue
        identifier = entry.get("id")
        if not identifier or identifier in seen:
            excluded.append({"id": identifier, "reason": "missing_or_duplicate_id"})
            continue
        seen.add(identifier)
        ok, reason = eligible(entry, root, today)
        if not ok:
            excluded.append({"id": identifier, "reason": reason})
            continue
        source_path = (root / entry["file"]).resolve()
        body = source_path.read_text(encoding="utf-8")
        if not body.strip():
            excluded.append({"id": identifier, "reason": "empty_source"})
            continue
        accepted.append({
            "id": identifier,
            "title": entry["title"],
            "language": entry["language"],
            "licenseId": entry["licenseId"],
            "sources": entry["sources"],
            "reviewer": entry["reviewer"],
            "reviewedOn": entry["reviewedOn"],
            "expiresOn": entry["expiresOn"],
            "audience": entry["audience"],
            "tags": entry["tags"],
            "text": body.strip()
        })
    return {
        "schemaVersion": 1,
        "generatedBy": "scripts/build_reviewed_corpus.py",
        "runtimeEnabled": False,
        "llmEnabled": False,
        "builtOn": today.isoformat(),
        "approvedEntryCount": len(accepted),
        "entries": accepted,
        "excluded": excluded,
        "releaseNote": "This index is for internal retrieval evaluation only. It does not enable a public chatbot."
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--today", help="Override ISO date for deterministic tests")
    args = parser.parse_args()
    today = date.fromisoformat(args.today) if args.today else date.today()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    result = build(manifest, ROOT, today)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Approved RAG entries: {result['approvedEntryCount']}; excluded: {len(result['excluded'])}; LLM enabled: no.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
