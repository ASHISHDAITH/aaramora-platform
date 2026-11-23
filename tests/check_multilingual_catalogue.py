"""Validation checks for AARAMORA's multilingual source catalogue."""
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "reading-library.html").read_text(encoding="utf-8")
DATA = json.loads((ROOT / "data" / "library.json").read_text(encoding="utf-8"))
SCHEMA = json.loads((ROOT / "data" / "library.schema.json").read_text(encoding="utf-8"))

SCHEDULED = {
    "Assamese", "Bengali", "Bodo", "Dogri", "Gujarati", "Hindi", "Kannada", "Kashmiri",
    "Konkani", "Maithili", "Malayalam", "Manipuri", "Marathi", "Nepali", "Odia", "Punjabi",
    "Sanskrit", "Santali", "Sindhi", "Tamil", "Telugu", "Urdu",
}


class MultilingualCatalogueTests(unittest.TestCase):
    def test_all_22_scheduled_languages_are_available_as_filters(self):
        groups = {group["id"]: set(group["languages"]) for group in DATA["languageGroups"]}
        self.assertEqual(22, len(groups["india-scheduled"]))
        self.assertTrue(SCHEDULED.issubset(groups["india-scheduled"]))

    def test_additional_indian_and_world_language_filters_are_present(self):
        groups = {group["id"]: set(group["languages"]) for group in DATA["languageGroups"]}
        self.assertTrue({"Awadhi", "Bhojpuri", "Garo", "Khasi", "Meitei (Manipuri)", "Mizo", "Tulu"}.issubset(groups["india-additional"]))
        self.assertTrue({"Arabic", "Chinese", "English", "French", "German", "Japanese", "Korean", "Persian", "Russian", "Spanish", "Swahili", "Vietnamese"}.issubset(groups["international"]))
        self.assertTrue({"Pali", "Prakrit", "Tibetan", "Old Javanese"}.issubset(groups["classical"]))

    def test_ndli_language_record_uses_observed_portal_categories(self):
        record = next(item for item in DATA["records"] if item["id"] == "ndli-multilingual-discovery")
        self.assertIn("Awadhi", record["languages"])
        self.assertIn("Bodo", record["languages"])
        self.assertIn("Sinhala", record["languages"])
        self.assertTrue(record["provenance"]["languageCoverageUrl"].startswith("https://"))
        self.assertIn("not proof", record["languageCoverageLabel"])

    def test_every_record_has_source_rights_and_review_dates(self):
        ids = set()
        for record in DATA["records"]:
            with self.subTest(record=record["id"]):
                self.assertNotIn(record["id"], ids)
                ids.add(record["id"])
                self.assertTrue(record["provenance"]["sourceUrl"].startswith("https://"))
                self.assertTrue(record["access"]["url"].startswith("https://"))
                self.assertTrue(record["rights"]["licence"])
                self.assertTrue(record["rights"]["reuse"])
                self.assertRegex(record["verification"]["checkedAt"], r"^\d{4}-\d{2}-\d{2}$")
                self.assertRegex(record["verification"]["nextReviewAt"], r"^\d{4}-\d{2}-\d{2}$")
        self.assertGreaterEqual(len(ids), 10)

    def test_language_group_provenance_is_present(self):
        for group in DATA["languageGroups"]:
            with self.subTest(group=group["id"]):
                self.assertTrue(group["sourceUrls"])
                self.assertTrue(all(url.startswith("https://") for url in group["sourceUrls"]))
        self.assertIn("sourceUrls", SCHEMA["properties"]["languageGroups"]["items"]["properties"])

    def test_restricted_sources_are_link_only(self):
        banidb = next(item for item in DATA["records"] if item["id"] == "banidb-sikh-source")
        self.assertEqual("permission-required", banidb["rights"]["status"])
        self.assertIn("does not copy", banidb["access"]["notes"])
        gretil = next(item for item in DATA["records"] if item["id"] == "gretil-indian-texts")
        self.assertIn("commercial use", gretil["rights"]["reuse"].lower())
        heritage = next(item for item in DATA["records"] if item["id"] == "heritage-scripture-server")
        self.assertIn("Modern translations", heritage["rights"]["reuse"])

    def test_schema_and_page_filters_exist(self):
        self.assertEqual("object", SCHEMA["type"])
        self.assertIn("records", SCHEMA["required"])
        for marker in ("catalogue-language", "catalogue-tradition", "catalogue-access", "catalogue-rights", "catalogue-level", "catalogue-format", "catalogue-results"):
            with self.subTest(marker=marker):
                self.assertIn(f'id="{marker}"', HTML)
        self.assertIn("data/library.json", HTML)

    def test_no_original_section_removed(self):
        for anchor in ("free-downloads", "scripture-shelf", "workbooks-and-articles", "relationship-open-learning", "attachment-books", "faith-wisdom", "novels-and-classics", "github-shelves", "licensing"):
            with self.subTest(anchor=anchor):
                self.assertIn(f'id="{anchor}"', HTML)
        self.assertIn("OpenStax", HTML)
        self.assertIn("Attachment in Adulthood", HTML)
        self.assertIn("Our reuse checklist", HTML)


if __name__ == "__main__":
    unittest.main()
