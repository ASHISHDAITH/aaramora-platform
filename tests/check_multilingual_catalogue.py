"""Validation checks for AARAMORA's multilingual source catalogue."""
from pathlib import Path
import json
import unittest
from scripts.check_library_links import request_url

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
                self.assertIsInstance(record["scripts"], list)
                self.assertIn(record["editorialReview"]["nativeLanguage"], {"pending", "reviewed"})
                self.assertIn(record["editorialReview"]["culturalContext"], {"pending", "reviewed"})
                self.assertIn(record["editorialReview"]["accessibility"], {"pending", "reviewed"})
                self.assertTrue(record["editorialReview"]["note"])
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

 
    def test_individual_edition_records_cover_specific_languages(self):
        expected = {
            "hi-ramcharitmanas-wikisource": "Hindi",
            "mr-jnaneshwari-wikisource": "Marathi",
            "bn-gitanjali-1913-wikisource": "Bengali",
            "pa-guru-granth-sahib-folio-1": "Punjabi",
            "ur-diwan-e-ghalib-wikisource": "Urdu",
            "or-odia-bhagabata-skandha-1": "Odia",
            "ta-thirukkural-project-madurai": "Tamil",
            "fr-comte-monte-cristo-pg": "French",
            "de-faust-pg": "German",
            "es-don-quijote-pg": "Spanish",
            "pt-os-lusiadas-pg": "Portuguese",
            "ar-safahat-arabic-reading": "Arabic",
        }
        records = {item["id"]: item for item in DATA["records"]}
        for record_id, language in expected.items():
            with self.subTest(record=record_id):
                self.assertIn(record_id, records)
                self.assertIn(language, records[record_id]["languages"])
                self.assertTrue(records[record_id]["provenance"]["sourceUrl"].startswith("https://"))
                self.assertTrue(records[record_id]["editorialReview"]["note"])
        punjabi = records["pa-guru-granth-sahib-folio-1"]
        self.assertIn("not a full-text reader", punjabi["access"]["notes"])
        self.assertIn("not the full scripture", punjabi["languageCoverageLabel"])
        tamil = records["ta-thirukkural-project-madurai"]
        self.assertIn("header page is kept intact", tamil["rights"]["reuse"])
        bengali = records["bn-gitanjali-1913-wikisource"]
        self.assertIn("United States", bengali["rights"]["licence"])
        self.assertIn("worldwide", bengali["rights"]["reuse"])

    def test_language_catalogue_does_not_mark_native_review_as_complete_without_review(self):
        for record in DATA["records"]:
            with self.subTest(record=record["id"]):
                self.assertEqual("pending", record["editorialReview"]["nativeLanguage"])
                self.assertEqual("pending", record["editorialReview"]["culturalContext"])


    def test_unicode_source_urls_are_percent_encoded_for_http_requests(self):
        urls = [
            "https://bn.wikisource.org/wiki/গীতাঞ্জলি_(১৯১৩)",
            "https://mr.wikisource.org/wiki/ज्ञानेश्वरी",
            "https://pa.wikisource.org/wiki/ਪੰਨਾ:Guru_Granth_Sahib_Ji.pdf/1",
            "https://ur.wikisource.org/wiki/دیوان_غالب",
            "https://or.wikisource.org/wiki/ଓଡ଼ିଆ_ଭାଗବତ/୧",
        ]
        for url in urls:
            with self.subTest(url=url):
                encoded = request_url(url)
                self.assertTrue(encoded.isascii())
                self.assertIn("%", encoded)


    def test_native_title_language_metadata_and_rtl_are_rendered(self):
        expected = {
            "hi-ramcharitmanas-wikisource": ("hi", "रामचरितमानस"),
            "mr-jnaneshwari-wikisource": ("mr", "ज्ञानेश्वरी"),
            "bn-gitanjali-1913-wikisource": ("bn", "গীতাঞ্জলি (১৯১৩)"),
            "pa-guru-granth-sahib-folio-1": ("pa", "ਸ੍ਰੀ ਗੁਰੂ ਗ੍ਰੰਥ ਸਾਹਿਬ ਜੀ"),
            "ur-diwan-e-ghalib-wikisource": ("ur", "دیوان غالب"),
            "or-odia-bhagabata-skandha-1": ("or", "ଓଡ଼ିଆ ଭାଗବତ"),
            "ta-thirukkural-project-madurai": ("ta", "திருக்குறள்"),
            "fr-comte-monte-cristo-pg": ("fr", None),
            "de-faust-pg": ("de", None),
            "es-don-quijote-pg": ("es", None),
            "pt-os-lusiadas-pg": ("pt", None),
        }
        records = {item["id"]: item for item in DATA["records"]}
        for record_id, (language, native_title) in expected.items():
            with self.subTest(record=record_id):
                self.assertEqual(language, records[record_id]["titleLanguage"])
                if native_title:
                    self.assertEqual(native_title, records[record_id]["titleNative"])
                    self.assertIn("titleDisplaySuffix", records[record_id])
        self.assertEqual("rtl", records["ur-diwan-e-ghalib-wikisource"]["titleDirection"])
        self.assertIn("titleLanguage", HTML)
        self.assertIn('aria-label="Open official source for ', HTML)

    def test_no_original_section_removed(self):
        for anchor in ("free-downloads", "scripture-shelf", "workbooks-and-articles", "relationship-open-learning", "attachment-books", "faith-wisdom", "novels-and-classics", "github-shelves", "licensing"):
            with self.subTest(anchor=anchor):
                self.assertIn(f'id="{anchor}"', HTML)
        self.assertIn("OpenStax", HTML)
        self.assertIn("Attachment in Adulthood", HTML)
        self.assertIn("Our reuse checklist", HTML)


if __name__ == "__main__":
    unittest.main()
