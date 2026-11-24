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

## Named editions and language-specific indexes · 24 November 2026

The catalogue now contains 26 entries: 11 institutional/source records plus 15 additional language-specific editions or discovery indexes. The records added in this update are:

| Language | Linked record | What the record represents | Rights/access caveat |
|---|---|---|---|
| Hindi | Ramcharitmanas · Hindi Wikisource | A long, page-indexed Hindi text with source-side export options | Confirm the exact source print edition, scan, contributors and page-level terms before reuse. |
| Marathi | Jñāneśvarī / Bhāvārthadīpikā | Dnyaneshwar's Marathi Bhagavad Gita commentary; page links chapters | Source page warns of a duplicated passage/chapter issue. AARAMORA does not claim a critical edition or line-checked transcription. |
| Bengali | Gītāñjali (1913) | Bengali third-edition page, Indian Press, Allahabad | Wikisource identifies the work as public domain in the United States and discusses territorial differences. Page contributions carry Wikimedia terms; do not treat US status as worldwide clearance. |
| Punjabi | Guru Granth Sahib Ji · selected folio 1 | One page from a digitized PDF with Gurmukhi transcription | It is one selected folio, not a full scripture edition. The page states CC BY-SA for contributed transcription; scan/source rights may differ. |
| Urdu | Dīvān-e Ghālib | Urdu Wikisource page with ghazal, qasida, masnavi, rubai and other sections | Page says contributed text uses CC BY-SA; underlying edition and images can have separate rights. |
| Odia | Odia Bhagabata · first Skandha | Jagannath Das's first Skandha page only | Source offers page-level export controls; item rights and text accuracy remain to be checked. |
| Tamil | Tirukkural · Project Madurai UTF-8 | Tiruvalluvar text in Tamil Unicode/UTF-8 | Project Madurai says this exact file may be redistributed if its header page is retained. That condition is not a licence for other editions or translations. |
| Gujarati | Gujarati Wikisource full-book list | Discovery index of full-book titles, authors and genres | Each listed title is a separate rights/edition check. |
| Kannada | Kannada Wikisource portal | Portal lists active projects including Jaimini Bharata and Pampa Bharata | Collection discovery only; individual text, transcription and scan rights must be checked. |
| Malayalam | Malayalam Wikisource book list | Project list of works it describes as out of copyright | The list itself says it is incomplete. Confirm every work, author death date, edition and scan separately. |
| Arabic | Safahat · Hindawi Foundation | Arabic reading platform for books licensed and translated by Hindawi | Hindawi says those books are free to read/download on Safahat. That does not create a right to mirror or republish them. |
| French | Le comte de Monte-Cristo, Tome I | Project Gutenberg eBook 17989 | Project Gutenberg labels this edition public domain in the USA; other territories must be checked. This record is Tome I only. |
| German | Faust: Der Tragödie erster Teil | Project Gutenberg eBook 2229 | US public-domain statement only; later translations, notes and artwork are separate. |
| Spanish | Don Quijote | Project Gutenberg eBook 2000 | US public-domain statement only; local law and the exact edition still matter. |
| Portuguese | Os Lusíadas | Project Gutenberg eBook 3333 | US public-domain statement only; later notes, translation and artwork are separate. |

### Editorial-review status

Every catalogue record exposes an explicit editorial review object. At this release:

- Native-language review: pending.
- Religious/cultural-context review: pending.
- Edition fidelity and transcription comparison: pending where no independent collation is noted.
- Manual accessibility review of the underlying source text: pending.

These statuses must not be changed to reviewed until a named qualified reviewer has checked the specific language/edition and the review has been recorded. A source page check is not native-speaker approval, religious endorsement, clinical approval or legal advice.

### Exact sources

- Hindi Ramcharitmanas: https://hi.wikisource.org/wiki/रामचरितमानस
- Marathi Jñāneśvarī: https://mr.wikisource.org/wiki/ज्ञानेश्वरी
- Bengali Gītāñjali (1913): https://bn.wikisource.org/wiki/গীতাঞ্জলি_(১৯১৩)
- Punjabi selected folio: https://pa.wikisource.org/wiki/ਪੰਨਾ:Guru_Granth_Sahib_Ji.pdf/1
- Urdu Dīvān-e Ghālib: https://ur.wikisource.org/wiki/دیوان_غالب
- Odia Bhagabata first Skandha: https://or.wikisource.org/wiki/ଓଡ଼ିଆ_ଭାଗବତ/୧
- Tamil Tirukkural UTF-8: https://www.projectmadurai.org/pm_etexts/utf8/pmuni0001.html
- Gujarati full-book index: https://gu.wikisource.org/wiki/વિકિસ્રોત:પુસ્તકો
- Kannada Wikisource: https://kn.wikisource.org/wiki/ಮುಖ್ಯ_ಪುಟ
- Malayalam book list: https://ml.wikisource.org/wiki/വിക്കിഗ്രന്ഥശാല:വിക്കിപദ്ധതി/പുസ്തകപ്പട്ടിക
- Arabic Safahat: https://safahat.org/ · Hindawi Foundation information: https://www.hindawi.org/en/about
- French Monte-Cristo I: https://www.gutenberg.org/ebooks/17989
- German Faust Part I: https://www.gutenberg.org/ebooks/2229
- Spanish Don Quijote: https://www.gutenberg.org/ebooks/2000
- Portuguese Os Lusíadas: https://www.gutenberg.org/ebooks/3333



## Seven-format discovery catalogue · 24 November 2026

The original 26 multilingual records remain. The catalogue now contains 49 entries after adding 23 source records. Each entry has required `contentTypes` tags, using one or more of `book`, `video`, `audiobook`, `audio`, `article`, `blog` and `image`. Format tags describe source links, not AARAMORA-hosted content. They can be combined with the existing language, tradition, access, rights, reading-level and file-format filters.

The media shelf includes:
- OpenStax Psychology (the specific edition whose preface names CC BY 4.0), Standard Ebooks, and Centre for Clinical Interventions workbooks.
- PubMed Central's Open Access Subset and DOAJ for article discovery, with article-level rights checks.
- Greater Good and Gottman Institute article collections.
- Creator-linked videos from The School of Life; use the YouTube source page or official embed only.
- LibriVox public-domain audio discovery, World English Bible audio, Gurbani Prakash read-along audio, and Quran.com recitations.
- Tanzil's licensed Arabic text, QuranEnc translation entries, SuttaCentral, and its public GitHub source index.
- Openverse, Wikimedia Commons and the individually credited Pexels book photograph.

See [READING_MEDIA_EXPANSION.md](READING_MEDIA_EXPANSION.md) for source-by-source links, exact contributor attributions and item-level restrictions. No source content is bulk copied into this repository. Native-language, religious/cultural-context and manual accessibility reviews remain pending.


The Audio filter is separate from Audiobooks. Gurbani Prakash, Quran.com, CCI guided-audio resources and podcasts are classified as Audio; LibriVox, eBible.org and Project Gutenberg's audio-book collection are catalogued as Audiobooks where the source provides narrated books. These classifications identify the media form and do not imply permission to copy the recordings.
