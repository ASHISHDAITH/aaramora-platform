# AARAMORA multilingual reading catalogue

**Catalogue review date: 24 November 2026**

The Reading Library now contains a structured source catalogue in data/library.json. It stores source/edition metadata and links, not third-party book text, scanned files or copied translations.

## Language coverage

The filter groups are designed for discovery, not as a claim that every listed language has a book in every source.

### India · Eighth Schedule

Assamese, Bengali, Bodo, Dogri, Gujarati, Hindi, Kannada, Kashmiri, Konkani, Maithili, Malayalam, Manipuri, Marathi, Nepali, Odia, Punjabi, Sanskrit, Santali, Sindhi, Tamil, Telugu and Urdu.

The Eighth Schedule contains 22 languages. It is not a census of India's living languages.

### Additional Indian-language discovery

Awadhi, Bhojpuri, Garo, Khasi, Meitei (Manipuri), Mizo, Tulu, Bhili/Bhilodi, Gondi, Kurukh, Kokborok, Ho, Haryanvi, Garhwali, Ladakhi, Rajasthani and Chhattisgarhi.

This is an expandable discovery list. Language availability must be checked against the individual source catalogue and edition.

### World-language discovery

The initial 51-language set includes Afrikaans, Amharic, Arabic, Basque, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Filipino/Tagalog, Finnish, French, Galician, German, Greek, Hebrew, Hungarian, Icelandic, Igbo, Indonesian, Irish, Italian, Japanese, Korean, Latvian, Lithuanian, Malay, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Thai, Turkish, Ukrainian, Vietnamese, Welsh, Xhosa and Yoruba, along with Zulu.

This is not an exhaustive language census. New languages can be added once a reliable source collection is identified.

### Classical and scholarly text languages

Pali, Prakrit, Tibetan and Old Javanese are separate discovery tags because they appear in scholarly text repositories.

## Source scope verified for this edition

| Source | Confirmed scope and access | Rights handling |
|---|---|---|
| NDLI language browse | The browse facet includes Assamese, Awadhi, Bengali, Bhojpuri, Dogri, English, Gujarati, Hindi, Kannada, Khasi, Konkani, Maithili, Malayalam, Meitei Mayek, Marathi, Mizo, Nepali, Odia, Punjabi, Sanskrit, Santali, Sinhala, Sindhi, Tamil, Telugu and Urdu. Its school-education page also lists Indian-language content such as Bodo/Boro, Garo and Kashmiri. | NDLI aggregates records from multiple institutions. Downloads are available only where the content provider permits them; a language facet is not a download licence. |
| Heritage Scripture Server, IIT Kanpur | The current interface documents 11 scripts: Assamese, Bengali, Devanagari, Gujarati, Kannada, Malayalam, Odia, Punjabi, Roman (IAST/ISO), Tamil and Telugu. It serves source texts, translations, commentaries and transliterations. | Its May 2026 licence distinguishes ancient Sanskrit moolam from copyrighted modern translations and commentaries. API access requires a key for most endpoints, with rate limits and provenance requirements. |
| GRETIL | Current sections list Sanskrit, Pali, Prakrit, Hindi, Marathi, Tamil, Malayalam, Tibetan and Old Javanese. | The files are strictly for scholarly reference; commercial use is excluded and original rightsholders retain copyright. |
| Wikisource | Multiple language editions and source-text pages. | Work-level and page-level rights, contributor status and translation rights must be checked individually. |
| Project Gutenberg | Public-domain ebook catalogue with a language index. | The exact ebook and local jurisdiction matter; its rights statements are USA-specific. |
| LibriVox | Volunteer audiobook catalogue with a language filter. | Public-domain statement is USA-specific; verify the underlying work and local law elsewhere. |
| Open Library | Bibliographic discovery and controlled digital borrowing. | A catalogue record does not mean free download. Respect lending controls and use the documented API/dump routes. |
| DOAB / OAPEN | Open-access scholarly book discovery and metadata feeds. | OAPEN's metadata feeds are CC0; individual book files have their own publisher licences. |
| OPenn | South Asian manuscript and image records. | Check the exact item's CC0, CC BY or CC BY-SA label before reuse. |
| BaniDB | Gurbani source reader/API. | Linked only. Current terms include full-dataset, update, attribution/logo and contribution obligations for project integration; redistribution and commercial use need written permission. AARAMORA does not ingest its data. |

## Rights and editorial rules

1. Distinguish the original work from a specific translation, transliteration, commentary, edited edition, recording, scan and cover.
2. Store the named translator/editor where available. Do not assign one licence to every language edition of a work.
3. Display access as discovery, read online, download at source, audio, borrowing or API. Do not label all of these as “free download”.
4. Display the source check date and next-review date. Those dates apply to the source page and terms, not every book in a provider collection.
5. Keep cultural descriptions neutral and have relevant language/tradition readers review them before public launch.
6. The banner “For reflection and cultural reading, not as treatment” is an editorial scope statement, not a claim of religious or clinical endorsement.

## Technical implementation

- data/library.json is the catalogue source.
- data/library.schema.json defines the record shape.
- scripts/check_catalogue.py validates required fields and rights/provenance metadata.
- scripts/check_library_links.py performs polite metadata-only HEAD/range checks. It never downloads or parses book content.
- tests/check_multilingual_catalogue.py protects the language groups and rights boundaries.
- .github/workflows/reading-library-link-check.yml runs a weekly source-link review.

The filters remain a discovery tool. A source card appearing for a language does not mean all titles from that institution are available in that language.
