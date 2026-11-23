#!/usr/bin/env python3
"""Validate AARAMORA's reading-library metadata without fetching or copying book content."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "library.json"
SCHEMA_PATH = ROOT / "data" / "library.schema.json"
HTML_PATH = ROOT / "reading-library.html"

SCHEDULED_LANGUAGES = {
    "Assamese", "Bengali", "Bodo", "Dogri", "Gujarati", "Hindi", "Kannada", "Kashmiri",
    "Konkani", "Maithili", "Malayalam", "Manipuri", "Marathi", "Nepali", "Odia", "Punjabi",
    "Sanskrit", "Santali", "Sindhi", "Tamil", "Telugu", "Urdu",
}
RIGHTS_STATUSES = {
    "item-specific", "source-restricted", "public-domain-edition",
    "open-license", "permission-required",
}
ACCESS_TYPES = {
    "discovery", "read-online", "download-at-source", "audio-download",
    "borrow", "api-read-only",
}
READING_LEVELS = {"all-levels", "introductory", "academic", "primary-source"}
CONTENT_TYPES = {"book", "video", "audiobook", "article", "blog", "image"}


class CatalogueError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CatalogueError(message)


def check_https_url(value: object, label: str) -> None:
    require(isinstance(value, str) and value.startswith("https://"), f"{label}: URL must use HTTPS")
    parsed = urlparse(value)
    require(bool(parsed.netloc), f"{label}: URL has no host")


def check_date(value: object, label: str) -> None:
    require(isinstance(value, str), f"{label}: date must be a string")
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise CatalogueError(f"{label}: invalid ISO date {value!r}") from exc


def main() -> int:
    for path in (DATA_PATH, SCHEMA_PATH, HTML_PATH):
        require(path.is_file(), f"Required file missing: {path.relative_to(ROOT)}")

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    html = HTML_PATH.read_text(encoding="utf-8")

    for field in ("schemaVersion", "lastReviewedAt", "editorialPolicy", "languageGroups", "records"):
        require(field in data, f"Catalogue root is missing {field}")
    check_date(data["lastReviewedAt"], "lastReviewedAt")
    require(isinstance(data["editorialPolicy"], str) and len(data["editorialPolicy"]) >= 20,
            "editorialPolicy must explain the discovery-only / rights approach")
    require(schema.get("type") == "object", "JSON schema must describe an object")
    require("records" in schema.get("required", []), "JSON schema must require records")

    groups = data["languageGroups"]
    require(len(groups) >= 4, "At least four language groups are expected")
    group_ids = set()
    for index, group in enumerate(groups):
        label = f"languageGroups[{index}]"
        for field in ("id", "label", "scope", "languages", "sourceUrls"):
            require(field in group, f"{label} is missing {field}")
        require(group["id"] not in group_ids, f"Duplicate language group id: {group['id']}")
        group_ids.add(group["id"])
        require(len(group["languages"]) == len(set(group["languages"])),
                f"{label} contains duplicate language names")
        require(all(isinstance(item, str) and item.strip() for item in group["languages"]),
                f"{label} contains an empty/non-string language")
        require(group["sourceUrls"], f"{label} needs source URLs")
        for url in group["sourceUrls"]:
            check_https_url(url, f"{label}.sourceUrls")
    scheduled = next((g for g in groups if g["id"] == "india-scheduled"), None)
    require(scheduled is not None, "Missing India Eighth Schedule group")
    require(len(scheduled["languages"]) == 22, "Eighth Schedule group must contain 22 languages")
    require(SCHEDULED_LANGUAGES == set(scheduled["languages"]),
            "Eighth Schedule language names differ from the expected 22")

    records = data["records"]
    require(len(records) >= 10, "Catalogue should contain at least ten source records")
    record_ids = set()
    required_record_fields = {
        "id", "recordType", "title", "editionTitle", "contributors", "traditions",
        "subjects", "languages", "scripts", "editorialReview", "languageCoverageLabel", "readingLevel", "access",
        "rights", "accessibility", "provenance", "verification", "contentTypes",
    }
    for index, record in enumerate(records):
        label = f"records[{index}]"
        missing = sorted(required_record_fields - set(record))
        require(not missing, f"{label} missing fields: {', '.join(missing)}")
        require(record["id"] not in record_ids, f"Duplicate record id: {record['id']}")
        record_ids.add(record["id"])
        require(bool(record["title"].strip()), f"{label}.title is empty")
        require(bool(record["editionTitle"].strip()), f"{label}.editionTitle is empty")
        require(record["readingLevel"] in READING_LEVELS, f"{label} has invalid readingLevel")
        require(isinstance(record["contentTypes"], list) and record["contentTypes"], f"{label}.contentTypes must be a non-empty list")
        require(len(record["contentTypes"]) == len(set(record["contentTypes"])), f"{label}.contentTypes contains duplicate values")
        require(set(record["contentTypes"]).issubset(CONTENT_TYPES), f"{label}.contentTypes contains an unsupported format")
        require(isinstance(record["traditions"], list) and record["traditions"],
                f"{label}.traditions must be a non-empty list")
        require(isinstance(record["languages"], list), f"{label}.languages must be a list")
        require(isinstance(record["scripts"], list), f"{label}.scripts must be a list")
        require(all(isinstance(script, str) and script.strip() for script in record["scripts"]),
                f"{label}.scripts contains an empty/non-string value")
        editorial = record["editorialReview"]
        for field in ("nativeLanguage", "culturalContext", "accessibility", "note"):
            require(field in editorial, f"{label}.editorialReview missing {field}")
        for field in ("nativeLanguage", "culturalContext", "accessibility"):
            require(editorial[field] in {"pending", "reviewed"},
                    f"{label}.editorialReview.{field} must be pending or reviewed")
        require(bool(editorial["note"].strip()), f"{label}.editorialReview.note is empty")

        access = record["access"]
        for field in ("type", "label", "url", "formats", "notes"):
            require(field in access, f"{label}.access missing {field}")
        require(access["type"] in ACCESS_TYPES, f"{label}.access.type is invalid")
        check_https_url(access["url"], f"{label}.access.url")

        rights = record["rights"]
        for field in ("status", "licence", "jurisdiction", "reuse", "notes"):
            require(field in rights, f"{label}.rights missing {field}")
        require(rights["status"] in RIGHTS_STATUSES, f"{label}.rights.status is invalid")
        require(bool(rights["licence"].strip()), f"{label}.rights.licence is empty")
        if rights.get("policyUrl"):
            check_https_url(rights["policyUrl"], f"{label}.rights.policyUrl")

        provenance = record["provenance"]
        require(bool(provenance.get("sourceName", "").strip()), f"{label}.provenance.sourceName is empty")
        check_https_url(provenance.get("sourceUrl"), f"{label}.provenance.sourceUrl")
        for field in ("metadataUrl", "languageCoverageUrl", "policyUrl"):
            if provenance.get(field):
                check_https_url(provenance[field], f"{label}.provenance.{field}")

        accessibility = record["accessibility"]
        for field in ("searchableText", "reflowable", "screenReaderNotes", "formats"):
            require(field in accessibility, f"{label}.accessibility missing {field}")

        verification = record["verification"]
        for field in ("checkedAt", "nextReviewAt", "method"):
            require(field in verification, f"{label}.verification missing {field}")
        check_date(verification["checkedAt"], f"{label}.verification.checkedAt")
        check_date(verification["nextReviewAt"], f"{label}.verification.nextReviewAt")
        require(bool(verification["method"].strip()), f"{label}.verification.method is empty")

    for marker in ('id="language-catalogue"', 'id="catalogue-language"', 'data/library.json'):
        require(marker in html, f"reading-library.html is missing {marker}")
    type_totals = {kind: sum(kind in record["contentTypes"] for record in records) for kind in sorted(CONTENT_TYPES)}
    require(all(type_totals.values()), "All six format categories must have at least one resource")
    print(f"Catalogue valid: {len(records)} catalogue entries, {len(groups)} language groups, "
          f"{len(scheduled['languages'])} scheduled Indian languages, formats={type_totals}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (CatalogueError, json.JSONDecodeError) as exc:
        print(f"Catalogue validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
