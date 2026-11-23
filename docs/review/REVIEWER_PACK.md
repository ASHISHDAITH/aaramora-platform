# AARAMORA Reading Library — independent reviewer pack

Last prepared: 24 November 2026  
Scope: 26 catalogue records, 15 added language-specific editions/indexes, the existing Faith & Wisdom shelf, and multilingual source-language filters.

## Current release state

This pack is a request for independent review, not evidence that review has happened.

- Native-language review: **pending** for every catalogue record.
- Cultural / religious-context review: **pending** for every catalogue record.
- Manual assistive-technology review: **pending** for every catalogue record.
- Rights/legal review: source notes are recorded, but qualified copyright counsel has not signed off on every item.
- No university, scholar, religious institution, accessibility tester or vendor has been contacted or has accepted a review request through this repository update.

The production page has passed automated checks, but automated testing cannot establish translation fidelity, script correctness, sacred-text accuracy, interpretive fairness or real-user accessibility.

## Review work packages

### A. Native-language and edition review

A reviewer must be fluent in the relevant language and competent with the script and genre. For a classical or sacred text, ask for a subject specialist as well as a language editor.

Review each exact source page and, where available, compare it to the cited scan or a recognised printed edition. Record the edition, page/folio/chapter, transcription differences, spelling/diacritic conventions and any uncertainty. Do not silently repair a source transcription in AARAMORA metadata.

Minimum checks:

1. Does the source page actually display the named work and language?
2. Is the title accurate in the original script? Is transliteration distinguishable from the original title?
3. Does the record describe the actual scope correctly (whole book, one volume, one Skandha, one folio, catalogue or provider)?
4. Are names, diacritics, orthography, punctuation and language labels accurate?
5. Does the visible digital text correspond to the scan or cited edition? Record mismatches; do not assume OCR or proofreading is correct.
6. Are the source page's claimed export formats and edition dates still present?
7. Is the English descriptor neutral and accurate? Do not add doctrinal or historical claims that the source page does not support.

### B. Cultural, religious and literary-context review

Use a separate reviewer from the language checker when the entry concerns a sacred text, religious tradition or culturally contested interpretation. The reviewer should be qualified in the relevant tradition or field, and should declare their perspective and any institutional relationship.

Minimum checks:

1. Is the tradition/category label accurate and appropriately scoped?
2. Does the text distinguish scripture, commentary, translation, poem, literary work, devotional text, manuscript and catalogue?
3. Does it avoid presenting one school, sect, denomination or translation as universally authoritative?
4. Does the description avoid devotional endorsement, theological adjudication, proselytising or dismissive framing?
5. Is historical/cultural context supported by a cited source?
6. Are disputed, variant or incomplete textual details explicitly qualified?

For sacred material, do not create substitute passages, paraphrases presented as scripture, or AI-generated verse. Keep the reader on the source's own text and interpretation controls.

### C. Rights and provenance review

A qualified copyright/IP reviewer should inspect each work, edition, translation, commentary, transcription, scan, image, cover and recording separately. Determine the territories in which a specific use is permitted.

Minimum checks:

1. Is the work's author and date accurately identified?
2. Does the licence notice cover the exact file/text or only the platform, metadata or contributors?
3. Are attribution, ShareAlike, NonCommercial, header-retention and no-AI/no-scraping conditions accurately preserved?
4. Is public-domain status territorial rather than treated as global?
5. Is the page only a discovery link, borrowable item, source-side download, API or full-text edition?
6. Is written permission in place for any proposed mirroring or commercial reuse?

Until clear rights are established, AARAMORA should link to the source and must not host a copied file. This review pack is not legal advice.

### D. Manual accessibility review

Use people with disabilities and assistive technologies. Review the live production page and the source destinations separately. A clean axe scan is useful evidence, not WCAG conformance certification.

Suggested coverage:

- Windows: keyboard only and NVDA with Firefox; repeat key flows with Chrome.
- Apple: VoiceOver with Safari on macOS and iOS.
- Android: TalkBack with Chrome.
- Magnification/reflow: 200% text enlargement and 400% browser zoom / 320 CSS-pixel equivalent, with no two-dimensional scrolling for ordinary text.
- Forced-colors/high-contrast mode and reduced-motion preference.
- Script and direction support: Hindi/Marathi/Bengali/Punjabi/Odia/Tamil/Gujarati/Kannada/Malayalam/Urdu/Arabic titles; verify pronunciation, bidi order, punctuation and English descriptor boundaries.

Task sequence:

1. Load the page, use the first Tab, activate “Skip to main content”, and confirm focus reaches main content.
2. Navigate the header, hero links, catalogue search, each select, clear-filters button, sort control, language-group details, result cards and footer using only the keyboard. Check for focus traps and lost focus.
3. Change language and search filters. Confirm the result count is announced and the result list is discoverable; confirm the user's focus is not lost.
4. Inspect headings and landmarks in screen-reader browse mode; verify heading levels are logical and repeated navigation has a name.
5. Open/close language-group details with keyboard and screen reader.
6. Confirm each link name provides enough context to distinguish its destination, especially repeated source links.
7. Confirm language-specific headings have a correct BCP 47 lang value and right-to-left Urdu title direction.
8. At narrow width/zoom, verify no text, controls, status messages or links are clipped, hidden by the sticky header, or require horizontal scrolling.
9. Check visible focus, target size/spacing, contrast in forced colours, and reduced-motion behaviour.
10. Record browser, OS, assistive-technology version, device/viewport, steps, findings and reproducible evidence.

Use W3C WCAG 2.2 references in the checklist: Reflow (1.4.10), Language of Parts (3.1.2), Focus Order (2.4.3), Focus Visible (2.4.7), Focus Not Obscured (2.4.11), Target Size Minimum (2.5.8), and Status Messages (4.1.3). Assess the actual normative criteria; do not infer conformance from short summaries.

## Edition-specific assignment map

| Record | Required language/edition expertise | Additional context review |
|---|---|---|
| hi-ramcharitmanas-wikisource | Hindi/Devanagari; Ramcharitmanas textual editor | Ramayana/Bhakti textual traditions; source preface discusses variants/interpolations |
| mr-jnaneshwari-wikisource | Marathi/Devanagari; Jnaneshwari edition editor | Bhagavad Gita commentary and Warkari/Bhakti context; source page warns about duplication |
| bn-gitanjali-1913-wikisource | Bengali; 1913 Indian Press edition | Tagore scholarship; keep Bengali original distinct from English translation |
| pa-guru-granth-sahib-folio-1 | Punjabi/Gurmukhi and manuscript/transcription collation | Sikh scripture specialist; one selected folio only, not the complete scripture |
| ur-diwan-e-ghalib-wikisource | Urdu/Nastaliq; Diwan edition/editor | Urdu literary history; verify listed sections against source |
| or-odia-bhagabata-skandha-1 | Odia script/literature; first-Skandha edition | Jagannath Das and Odia Vaishnava literature; first Skandha only |
| ta-thirukkural-project-madurai | Tamil classical language and Project Madurai text | Tamil classical literature; preserve Project Madurai file/header conditions |
| gu-wikisource-full-book-index | Gujarati language and Wikisource catalogue navigation | Item-specific review only; an index is not a licensed book |
| kn-wikisource-kannada-portal | Kannada language, proofreading and portal status | Check each source page's proofreading state; portal is not a critical edition |
| ml-wikisource-malayalam-book-list | Malayalam language and bibliography | Copyright-term summary and individual work/scan must be checked by qualified rights reviewer |
| ar-safahat-arabic-reading | Arabic; identify language variety and any regional-language editions | Do not imply publisher-hosted free downloads permit mirroring |
| fr-comte-monte-cristo-pg | French literature; Tome I edition | Dumas/Maquet attribution, edition and territorial rights |
| de-faust-pg | German literature; Part I edition | Identify Part I only; check translation/annotation boundaries |
| es-don-quijote-pg | Spanish literature; exact Project Gutenberg edition | Check edition, spelling and territory |
| pt-os-lusiadas-pg | Portuguese literature; exact Project Gutenberg edition | Check edition, notes and territory |

The 11 institutional/provider records also need scope/rights review. Their language lists are discovery metadata, not claims that every listed institution provides a complete text in every language.

## Sign-off record

Use one record for each work package and exact source edition.

- Catalogue record ID(s):
- Exact source URL and edition/folio:
- Review package: native language / cultural-context / rights / accessibility
- Reviewer name and qualification:
- Affiliation (optional) and conflict-of-interest declaration:
- Review date and source revision/access date:
- Tools (browser, OS, assistive technology, version, if relevant):
- Method and specific page/chapter/folio reviewed:
- Findings and severity:
- Corrections requested:
- Evidence (screenshots, short text snippets, issue IDs; do not copy protected text unnecessarily):
- Decision: approved / approved with changes / not approved / unable to assess
- Conditions and re-review date:
- Explicit permission for AARAMORA to name the reviewer publicly? yes/no

A record can move from pending to reviewed only after the reviewer has completed the relevant package and a maintainer has recorded this evidence. Reviewers do not approve legal rights unless specifically qualified and asked to assess the relevant territory and use.

## Public contact leads (not endorsements or accepted reviewers)

These official institutional and service routes were checked to prepare outreach. No outreach has been sent. Confirm the contact is still current before emailing.

| Scope | Contact route | Why it is relevant |
|---|---|---|
| Indian-language referral across scheduled/additional Indian languages | Central Institute of Indian Languages (CIIL), ada-ciilmys@gov.in, reception +91-821-234-5000; [official contact page](https://www.ciil.org/contact_us) | Government language institute coordinating Indian-language development and research; ask for referrals, not blanket endorsement. |
| Marathi / Jnaneshwari | Savitribai Phule Pune University Department of Marathi, marathi@unipune.ac.in or hodmarathi@unipune.ac.in, office 020-25601342; [official contact page](https://www.unipune.ac.in/dept/fine_arts/marathi/marathi_webfiles/contact.htm) | Language/literature expertise; ask for a Marathi editor and a Jnaneshwari textual specialist if available. |
| Sikh / Punjabi | GNDU Department of Guru Nanak Studies, head.gnstudy@gndu.ac.in; [official university telephone directory](https://www.online.gndu.ac.in/pdf/telephone-directory.pdf) | Academic contact route for Sikh studies; ask for a Gurmukhi/Punjabi transcription reviewer and a separate Sikh scripture/context reviewer. |
| Urdu / Diwan-e-Ghalib | Maulana Azad National Urdu University Department of Urdu, hod.urdu@manuu.edu.in, 040-23532006; [official contact page](https://manuu.edu.in/University/SLLI/Urdu/Contact) | Urdu language and literature review. |
| Arabic | MANUU Department of Arabic, hod.arabic@manuu.edu.in; [official staff directory](https://dde.manuu.edu.in/staff/profiles/languages) | Arabic language/editorial review; not automatically an Islamic-studies endorsement. |
| Odia / Bhagabata | Utkal University Odia Department; [official department page](https://utkaluniversity.ac.in/departments/odia/) | Literature, translation and textual-criticism expertise; request an Odia-language editor and a specialist for the work. |
| Malayalam | Inter-University Centre for Malayalam Language, University of Kerala, iucml@keralauniversity.ac.in, 0471-2305631 / 2305994; [official contact page](https://iucml.keralauniversity.ac.in/contact-us) | Malayalam language/literature and editorial route. |
| Gujarati | Gujarat University Department of Gujarati; [official department page](https://www.gujaratuniversity.ac.in/details/5) | Request a Gujarati bibliographic/editorial reviewer through the department. |
| Human-led accessibility evaluation | BarrierBreak, sales@barrierbreak.com; [accessibility testing service](https://www.barrierbreak.com/web-accessibility-testing/), [contact page](https://www.barrierbreak.com/contact-us/) | Provider describes manual web accessibility testing with testers with disabilities using assistive technologies; request scope and quote. |

No verified institutional reviewer contact is listed yet for French, German, Spanish or Portuguese. Find a current university/language department or qualified native-language editor before outreach. Do not use unverified personal addresses.

## Next release gate

Keep all review statuses pending until signed reports exist. After reviewers respond, make corrections in a separate commit, update the relevant record's review evidence, rerun all tests, and repeat browser and manual assistive-technology checks on the production candidate.
