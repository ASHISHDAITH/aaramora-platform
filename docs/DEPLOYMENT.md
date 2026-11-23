# Deployment Status and Release Path

**Repository:** [ASHISHDAITH/aaramora-platform](https://github.com/ASHISHDAITH/aaramora-platform)  
**Production URL:** https://aaramora-platform.vercel.app  
**Vercel project:** `aaramora-platform` (`prj_VzSl28VokjdmWzbCHjKvu7ZGgyGA`)  
**Latest deployment:** `dpl_CYKUri19P8g1uM4hu5tKHbiiZgjG`  
**Status:** READY · production · stable alias assigned

## Current release

A public static deployment has been created in the Vercel Hobby workspace. Vercel reports the deployment as READY and assigned the stable `aaramora-platform.vercel.app` alias.

The latest deployment is a static snapshot of commit `a4c2a6a16632914e7fd4f2f20daae3e9a9578cde` on `main`. It contains:
- `index.html` — simplified navigation, shorter hero copy and the 16:9 brand film in the hero
- `wellbeing.html`
- `relationships.html`
- `check-ins.html`
- `reading-library.html`
- `yoga-and-breath.html` — four evidence summaries, optional low-intensity practices, safety notes, and expandable Hindi/Marathi guided-rest and breathing draft transcripts (no audio has been recorded or published)
- `assets/healing-garden.svg`
- `assets/safe-corner.svg`
- `assets/thought-river.svg`

The brand-film MP4s are committed in GitHub under `assets/brand-film/`. The homepage now shows five common navigation destinations and groups the remaining destinations under “More”; all original links, sections and tools are retained. It uses shorter hero copy and places the 16:9 master in the hero, with the 9:16 version as a separate link. Video playback is user-initiated; it does not autoplay.

The Reading Library now contains nine subject shelves and 23 linked catalogue cards spanning open mental-health workbooks, academic books, relationship learning, Hindu/Sikh/Islamic/Christian/Buddhist/Jain texts, regional-language literature, public-domain classics and GitHub discovery indexes. Its search filters rendered cards in the browser only; it sends no search query to a server and stores no search history. The hero uses a credited Pexels still-life image with an original AARAMORA reading note. It links to source institutions rather than copying third-party books or restricted texts.

The Yoga & Breath page is an evidence-honest guide with summaries of four systematic reviews (2013, 2021, 2023 and 2024), optional low-intensity practices, safety boundaries and expandable Hindi/Marathi draft transcripts. Study populations, outcomes, comparators and certainty are distinguished. The page does not claim yoga cures depression or replaces care, and it does not use invented A/B/C/D evidence grades. Four original Hindi/Marathi scripts (guided rest and comfortable breathing) are now displayed on the page and stored in `docs/YOGA_AND_BREATH_AUDIO_SCRIPTS.md`; they target 5–7 minutes and remain draft text. No audio recordings have been submitted or published because a voice selection and the required native-speaker, clinician and qualified yoga-professional reviews remain outstanding.

The Check-ins page now includes the Problem Bench worksheet at `check-ins.html#problem-bench`. It is a local-only, optional, non-scored reflection worksheet, not a clinical service, not problem-solving therapy and not the Friendship Bench programme. The Friendship Bench and Goa HAP evidence is explicitly attributed to trained, supervised human-delivered programmes; their trial outcomes are not applied to AARAMORA's website feature. The existing guide finder, women's-health appointment planner and two-cycle log remain in place.

The WHO stress-guide companion is an original AARAMORA draft, not a translation or copy of the WHO guide and not endorsed by WHO. See `docs/WHO_STRESS_GUIDE_ADAPTATION.md` and the unsent enquiry draft `docs/WHO_OUTREACH_DRAFT.md`. Any true adaptation must follow the WHO licence, attribution, disclaimer, no-logo and third-party-rights requirements.

The official India support-source register is in `data/service-links.json`. Weekly metadata-only URL checks are implemented for Tele-MANAS, ERSS 112 and Women Helpline 181. The WCD source currently notes that 181 coverage excludes West Bengal; the page shows this caveat. Link checks cannot verify staffing, network access or service quality.

Content checks passed on commit `a4c2a6a16632914e7fd4f2f20daae3e9a9578cde` ([run 45285497757](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45285497757)). The reading-library metadata source-link check passed on the preceding code-compatible commit `081ca9a4177fec08bbee9cd420d70cc3381975c8` ([run 45285225515](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45285225515)).

The Vercel deployment was created directly from the listed source files because Git repository integration was blocked. The project has Vercel SSO/password deployment protection disabled so the public static site can be visited without membership in the Vercel workspace.

## Remaining Git integration step

The connected Vercel GitHub identity returned `repo_no_access` when linking `ASHISHDAITH/aaramora-platform`, saying it needs admin or write access. GitHub confirms the repository is public and the signed-in GitHub connector can push, but Vercel's connected GitHub App/identity does not currently have the needed access.

Until that is fixed, **new pushes to `main` will not automatically update the live site**. To enable automatic deployments:

1. Open [Vercel project settings](https://vercel.com/httpsgithubcomefigma54-devpp/aaramora-platform/settings/git).
2. In GitHub, install or update the Vercel GitHub App for the account that owns `ASHISHDAITH/aaramora-platform`, and grant it access to this repository.
3. In Vercel, connect the repository to this existing project. Keep the root directory at `./`; this is a static HTML project with no package install or build command.
4. Push a small reviewed commit and confirm Vercel creates a new production deployment automatically.

Do not create another Vercel project just to retry the connection; the current project already owns the production alias.

## Verification notes

- Vercel's deployment API reports `READY`, `target=production`, the stable `aaramora-platform.vercel.app` alias, and `aliasError=null` for deployment `dpl_E45batFEw39PSg1GKyBkN5gQZRb3`.
- Vercel's source-file listing confirms all nine expected HTML/SVG files are present, including `check-ins.html`, `reading-library.html` and `yoga-and-breath.html`.
- The earlier web-fetch environment could not retrieve the Vercel page. A later headless Chromium visitor-side smoke test and axe-core 4.10.3 scan did run against production; see the latest release section below. Manual NVDA/VoiceOver/TalkBack review, native-language review and clinician/safeguarding review remain outstanding.
- Confirm the video CDN returns the complete MP4s in a regular browser and check browser developer tools for failed requests before announcing the site publicly.

## No backend or health-data collection

The current website is a static information/help-navigation prototype. No API keys, database, accounts, server-side journal storage, analytics or AI service are required for this deployment. Do not add forms that collect private health details without a separate privacy/security review.

## Production release gates

A successful static deployment does not mean the platform is clinically approved. Before promoting the site as a health service:
- clinician review of all mental-health and women's-health copy;
- safeguarding review of relationship content and the safety flow;
- native-language review of Hindi and Marathi content;
- keyboard, screen-reader, mobile, low-bandwidth and WCAG 2.2 AA checks;
- privacy/security review and deployed network-traffic inspection;
- current verification of Tele-MANAS, emergency and women's helpline details;
- explicit ownership and review dates for every public resource.

Keep the public description clear: AARAMORA is an information and help-navigation prototype, not therapy, diagnosis, prescribing or an emergency response service.


## Check-ins page

The `check-ins.html` page is included in the current production deployment. It contains the non-diagnostic guide finder, women's-health appointment/print planner and original blank two-cycle symptom log. The latest deployment's Vercel source file listing confirms the page is present. The route should still be checked in a regular browser as part of the visitor-side smoke test.



## Latest verified production release · 24 November 2026

**Current production deployment:** `dpl_2Q3n6GmFCn13Lpizgx93LZJGQ6Wy`  
**State:** READY · `target=production` · stable alias assigned  
**Source:** `main` at `ba193318500e06e04c6a506ea3363b3aab552ea7`  
**Production alias:** https://aaramora-platform.vercel.app

This release enhances the Reading Library without removing its existing shelves or cards:

- All nine pre-existing Reading Library sections remain present.
- All 46 original static resource cards remain present and each shows a listing-metadata review date. This date is not a legal clearance of every edition; the source terms must still be checked.
- A new multilingual catalogue renders from `data/library.json` using the fields in `data/library.schema.json`.
- Search and filters cover language, tradition, access type, rights status, reading level and format.
- Language groups include 22 Eighth Schedule languages, 17 additional Indian-language discovery terms, 51 initial world-language filters and 4 classical/scholarly language tags. These are discovery aids, not a complete census and not a guarantee that every linked source has a book in every language.
- Eleven institutional/source records include access notes, rights restrictions, provenance, accessibility notes, checked dates and next-review dates.
- BaniDB is linked only; Gurbani data is not copied or integrated. NDLI remains a discovery layer; download permission is determined by each provider. Heritage Scripture Server scripts are distinguished from translation languages, and GRETIL is labelled for scholarly reference only.
- `scripts/check_catalogue.py` validates required record fields. `scripts/check_library_links.py` checks metadata URLs using HEAD/range requests only; it does not download book content. A weekly workflow is configured.

**Automated checks:** GitHub Actions run [45282847618](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45282847618) passed the existing content/safety suite, Reading Library checks, multilingual catalogue tests and catalogue validator. The initial weekly link-check workflow run [45282656364](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45282656364) also passed.

The Vercel API reports the deployment as READY and assigns the stable production alias. This tool could not load the live Vercel HTML/JSON in a normal browser session, so a human visitor-side smoke test of the live filters, source links and small-screen layout remains outstanding. Automated tests are not a substitute for keyboard, screen-reader, clinical, religious/cultural or legal review.


## Edition-level multilingual update · 24 November 2026

The Reading Library catalogue has grown to 26 entries. It now includes exact source pages for the Hindi Ramcharitmanas, Marathi Jnaneshwari, Bengali Gitanjali 1913, one Punjabi Guru Granth Sahib folio, Urdu Diwan-e-Ghalib, the first Skandha of the Odia Bhagabata, Tamil Tirukkural, Gujarati/Kannada/Malayalam book catalogues, the Arabic Safahat platform and four Project Gutenberg editions in French, German, Spanish and Portuguese.

Each card now shows its known writing system separately from language and an explicit editorial-review note. Native-language, cultural-context and source-text accessibility review remain pending. The source pages have not been converted into AARAMORA-hosted book files.

## Edition-level multilingual update · 24 November 2026

The Reading Library catalogue has grown to 26 entries. It now includes exact source pages for the Hindi Ramcharitmanas, Marathi Jnaneshwari, Bengali Gitanjali 1913, one Punjabi Guru Granth Sahib folio, Urdu Diwan-e-Ghalib, the first Skandha of the Odia Bhagabata, Tamil Tirukkural, Gujarati/Kannada/Malayalam book catalogues, the Arabic Safahat platform and four Project Gutenberg editions in French, German, Spanish and Portuguese.

Each card now shows its known writing system separately from language and an explicit editorial-review note. Native-language, cultural-context and source-text accessibility review remain pending. The source pages have not been converted into AARAMORA-hosted book files.


## Live-browser audit of the multilingual library · 24 November 2026

The live Reading Library page, JSON catalogue and JSON schema returned HTTP 200. The browser rendered all 46 original static cards, all 26 catalogue entries and 10 page sections. Independent filters were exercised for Marathi, Sikh, audio access, permission-required rights, academic level, EPUB format and the GRETIL search. At 390px width the page had no horizontal overflow. The first keyboard Tab focused the visible skip link, and Enter moved to main content. Axe-core 4.10.3 reported zero WCAG 2.2 AA/best-practice violations on the audited page (46 passes, no incomplete findings). This was an automated browser/axe scan, not a human NVDA/VoiceOver/TalkBack or native-reader review.


The metadata-only link checker percent-encodes non-ASCII URL paths before making HEAD/range requests. The checker does not parse or download source page bodies or book files.


## Latest production release verification · 24 November 2026

**Vercel deployment:** `dpl_Eeu3YsRJwmC86Zg652mQYriEcvbM`  
**Deployment source:** `main` commit `a4c2a6a16632914e7fd4f2f20daae3e9a9578cde`  
**State:** READY · production target · stable `aaramora-platform.vercel.app` alias assigned.

### Visitor-side verification

A headless Chromium check against the stable production domain confirmed:

- `/reading-library.html`, `/data/library.json`, `/data/library.schema.json`, and `/yoga-and-breath.html` all return HTTP 200.
- The source catalogue contains and renders 26 entries.
- The original 46 static book/resource cards and all original reading shelves remain present.
- The language, tradition, rights, format, access and search filters return expected records in independent cases.
- At 390 CSS-pixel viewport width, there is no horizontal page overflow.
- The keyboard's first Tab reaches the skip link; activating it moves to main content.
- axe-core 4.10.3 reports zero automated WCAG 2.2 AA/best-practice violations on the audited Reading Library page (46 passes, zero incomplete findings).
- All four Hindi/Marathi draft transcript panels are present on the Yoga & Breath page. They remain drafts and are not recordings.

This is an automated browser and axe scan, not a human NVDA, VoiceOver or TalkBack review, and not a formal WCAG conformance statement.

### Source-link audit

The local metadata-only source-link check examined 40 unique source/policy URLs: 32 returned success, 0 were confirmed dead (404/410), and 8 were inconclusive because of provider-side 503 responses, a timeout or a certificate issue. Those 8 are not labelled dead and should be rechecked. The checker percent-encodes Unicode/Indic/Arabic URL paths, uses HEAD first and only a one-byte range retry for selected blocked HEAD requests. It does not retrieve or parse book bodies.

### Human review still required

All catalogue records still show native-language, cultural-context and underlying-source accessibility review as pending. These statuses should remain pending until a named qualified reviewer checks the exact text and edition. Automated accessibility scanning does not review translation fidelity, theological interpretation, cultural phrasing, OCR accuracy or source-edition completeness.



## Candidate release — multilingual filter and reviewer-pack hardening · 24 November 2026

Candidate source commit: `f5a186d19274883e29b832ecd7e24671603b88f0` before this release-note update. The latest local checkout has passed `python scripts/check_catalogue.py` and all 60 Python tests.

Additional candidate browser checks:
- Manipuri and Meitei (Manipuri) aliases each return only the NDLI entry.
- French returns only the French Monte-Cristo edition; Marathi returns three expected records.
- Urdu native title carries `lang="ur"` and `dir="rtl"`; English descriptor remains LTR.
- 1280, 768, 390, 360 and 320 CSS-pixel viewports show no horizontal overflow.
- Forced-colors mode and reduced-motion CSS are enabled; 32px header/navigation targets were measured.
- axe-core 4.10.3 reports zero violations and 47 passes on the local candidate; browser console/page-error list is empty.

Four independent-review files now exist under `docs/review/`. They are reviewer requests and test instructions, not completed reviews. Qualified native-language, cultural/religious, rights and assistive-technology reviewers have not been contacted or signed off. Do not mark those fields reviewed without evidence.



### Support-contact touch target correction · 24 November 2026
The Tele-MANAS and Emergency 112 support links now have a 44px minimum height and 24px gap. This avoids tightly clustered phone links on narrow screens. The latest candidate passes the 62-test Python suite and local axe/viewport checks. Human assistive-technology testing remains pending.



### Focused keyboard state verified · final candidate
A production-like Chromium audit found that the skip link was positioned over the Tele-MANAS target at narrow widths while focused. The focused skip link now occupies its own top-bar row. The target links are 44px high with 24px spacing. Axe-core 4.10.3 returned zero violations/incomplete findings at 1440px, 390px and 320px both with and without the skip link focused. All 63 tests pass.
