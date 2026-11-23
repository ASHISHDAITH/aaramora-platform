# AARAMORA Platform

A privacy-first mental-wellbeing and women's-health information and help-navigation platform for India.

**Experience principle:** You do not have to figure everything out today.

This repository contains the AARAMORA static website prototype and the supporting research, visual design, content, safety and QA materials.

## Run the website

Open `index.html` in a modern browser, or run:

```bash
python -m http.server 8000
```

Then visit http://localhost:8000.

No npm install, database, account, remote fonts, analytics, AI API or backend is required for this prototype.

## Visual direction

The homepage follows a warm editorial botanical system: paper ivory, forest green, restrained sage, pale blue, muted lilac and clay accents. Its first screen uses a short plain-language introduction, two clear actions and the 16:9 AARAMORA brand film as the main visual. The primary navigation shows five common destinations and groups secondary links under “More”. Three credited Pexels photographs introduce optional journaling, connection and professional-support pathways. Stock photographs are illustrative only and are not testimonials or representations of actual AARAMORA staff.

See [docs/DESIGN_SYSTEM.md](docs/DESIGN_SYSTEM.md) for color tokens, typography, responsive rules, image credits and video behavior.

## Included experience

- Calm first-visit welcome, optional entry pathways and the fictional Kiran/firefly visual guide.
- India human-support routes, optional pause prompts and low-stimulation Night Help.
- Overthinking Unload, Little Garden, untimed Puzzle Sanctuary, Creative Studio and Safe Corner.
- Mental wellbeing guides covering depression, anxiety, panic, acute stress surges, trauma-related distress, rumination, sleep, burnout, grief and OCD-related experiences.
- Yoga & Breath guide with four study-specific evidence summaries, optional low-intensity practices, safety boundaries and four expandable Hindi/Marathi transcript drafts; no audio has been recorded, and native-language, clinical and qualified yoga-professional review remain pending.
- Relationships corner with 40 searchable concepts, three optional non-diagnostic reflections, a non-scored safety check and practical guidance for different sides of a relationship cycle.
- Check-ins page with a non-scored guide finder, local-only Problem Bench worksheet (not therapy or a clinical service), on-page women's-health appointment planner and printable original two-cycle symptom log.
- Women's-health corner with eight topic areas and the shared “how it may feel / what may help / when to seek support” structure.
- Expanded Reading Library with 23 linked resources across mental-health workbooks, academic/open books, attachment and relationship learning, Hindu/Sikh/Islamic/Christian/Buddhist/Jain sources, regional-language literature, public-domain classics and GitHub discovery indexes. A client-side title/topic/tradition search filters cards without sending queries to a server.
- Resource shelf and future community concept (not a live forum).

## Research and design materials

- `docs/ORIGINAL_RESEARCH_BRIEF.md` — original product concept, candidate sites, feature ideas, sitemap and roadmap.
- `docs/PRODUCT_BLUEPRINT.md` — product role, journeys, scope, governance and roadmap.
- `docs/DESIGN_RESEARCH_AND_DIRECTION.md` and `docs/DESIGN_SYSTEM.md` — design rationale and UI rules.
- `docs/EXPERIENCE_MAP.md` — visitor journeys and information architecture.
- `docs/WOMENS_HEALTH_RESEARCH.md` — women's-health research and review boundaries.
- `docs/MENTAL_WELLBEING_AND_WOMENS_HEALTH_RESEARCH.md` — mental and women's-health source register and evidence caveats.
- `docs/RELATIONSHIPS_RESEARCH.md` and `docs/RELATIONSHIP_CONCEPT_CONTENT_MAP.md` — relationship research and 40-concept glossary map.
- `docs/RELATIONSHIP_QUIZ_SPEC.md` — three reflection tools, safety check, privacy and review gates.
- `docs/HEALTH_TOPIC_CONTENT_STANDARD.md` — shared authoring rules for all health topics.
- `docs/YOGA_AND_BREATH_EVIDENCE.md` — yoga reviews, Friendship Bench and HAP trial notes, WHO licensing, safety and evidence-label rules.
- `docs/YOGA_AND_BREATH_AUDIO_SCRIPTS.md` — four original Hindi/Marathi guided-rest and comfortable-breathing transcript drafts; not approved, recorded or published audio.
- `docs/RESEARCH_SOURCES.md` — source and licensing register.
- `docs/QA_CHECKLIST.md`, `docs/QA_RESULTS.md` and `docs/VALIDATION_NOTES.md` — quality gates, completed checks and remaining reviews.
- `docs/PROBLEM_BENCH_SPEC.md` — implementation, safety and human-delivered-evidence boundaries for the Problem Bench worksheet.\n- `docs/WHO_STRESS_GUIDE_ADAPTATION.md` and `docs/WHO_OUTREACH_DRAFT.md` — original companion draft, WHO adaptation rules and an enquiry letter that has not been sent.\n- `docs/CONTENT_GOVERNANCE.md` and `docs/CORRECTIONS_LOG.md` — roles, correction process, suicide-related editorial rules and scheduled source review.\n- `data/service-links.json` — official India support-route register with source, owner and review dates.\n- `docs/DEPLOYMENT.md` — live Vercel deployment status, verification notes and the remaining Git-integration step.
- `docs/AARAMORA_BRAND_FILM_ASSETS.md` — export manifest, verified file hashes and committed media paths.
- `tests/check_relationships.py`, `tests/check_health_topics.py`, `tests/check_reading_library.py` and `tests/check_multilingual_catalogue.py` — automated static content, safety, source-rights and multilingual catalogue checks.
- `scripts/check_catalogue.py` validates catalogue record structure and required source/rights/review fields; `scripts/check_library_links.py` checks metadata URLs without downloading books.
- `research/benchmark50.csv` — 50-site benchmark candidate list (not a verified rank order).
- `research/mental-health-website-benchmark-report.md` and `research/visual-report.html` — research and visual concept report.
- `assets/` — original Healing Garden, Safe Corner and Thought River SVG illustrations.
- `CONTRIBUTING.md`, `SECURITY.md` and `SAFETY.md` — contribution, privacy and safety rules.

## Product and safety boundaries

This is an early **information and help-navigation prototype**, not therapy, diagnosis, prescribing, telemedicine or emergency response. It cannot promise trauma relief. Activities are optional; the prototype has no accounts, server-side health data, analytics, AI calls or persistent private journals.

Relationship reflection prompts are custom and unvalidated, not attachment-style or relationship diagnoses. The safety check is not a validated abuse risk assessment. Relationship-safety content requires review by a qualified clinician and safeguarding specialist. Each mental-health, relationship and women's-health topic follows a shared how-it-may-feel / what-may-help / when-to-seek-support structure. Health copy requires qualified clinical and native-language review before public release. Crisis resources must be rechecked against official sources at launch. Community remains a future concept until moderation, safeguarding, escalation and privacy operations are in place.

## Privacy

Never commit real user messages, journals, screening answers, health records, participant data, API keys or credentials. Use synthetic fixtures. Never send personal health data to free-tier AI APIs.


## Reading library and copyright rules
- `reading-library.html` provides legal read/download links for explicitly licensed open resources, sacred-text source institutions, public-domain classics, open-access catalogues, publisher/library access to copyrighted relationship books, and title-specific reuse notes.
- `docs/READING_LIBRARY_EXPANSION.md` records the additional workbooks, repositories, scriptures, regional-language sources, edition-level rights, Pexels hero-image credit and catalogue maintenance rules.
- The GitHub source reference for OpenStax is `openstax/OpenStaxOnTheGo`; its repository AGPL licence covers software, while the book asset has its own source licence. The current official OpenStax site is the preferred download source.
- Never bypass DRM, paywalls, private repository permissions, borrowing controls or import copyrighted book copies without permission. A free-to-read page is not automatically a reusable/downloadable file.
- A public GitHub repository or its root licence does not automatically license every bundled third-party book, image or dataset.

- `reading-library.html` also lists focused Noba attachment/relationship modules and a downloadable *Psychology of Human Relations* PDF.
- OpenStax Psychology 2e is linked under its current CC BY-NC-SA 4.0 terms. Its current preface prohibits LLM/AI ingestion without prior written permission. SuttaCentral also asks that its content not be scraped or used to build generative-AI datasets; AARAMORA links to its editions rather than copying them.


## Automated checks
GitHub Actions runs `python -m unittest discover -s tests -p 'check_*.py' -v` on pushes and pull requests. The checks cover core page routes, wellbeing content structure, women's-health consistency, all 40 relationship concepts, optional quiz/privacy requirements, Problem Bench privacy and print boundaries, support links, internal anchors and inline JavaScript syntax on the six site pages. A separate weekly workflow checks official support-source URLs without downloading their page bodies.


## Brand film

The first AARAMORA six-scene brand-film exports are reviewed and committed in Git:
- `assets/brand-film/aaramora-master-16x9.mp4` — 16:9 website master.
- `assets/brand-film/aaramora-instagram-9x16.mp4` — 9:16 Instagram edit.

The supplied `CLEAN_NO_ADDED_AUDIO` file is byte-identical to the landscape master and still contains AAC audio, so it is not a separate silent export. The homepage player uses the landscape master and offers the vertical edit as a separate link. See [the export manifest](docs/AARAMORA_BRAND_FILM_ASSETS.md).

## Live deployment

**Production URL:** https://aaramora-platform.vercel.app

The current public static deployment is marked READY by Vercel and serves six HTML pages (`index.html`, `wellbeing.html`, `relationships.html`, `check-ins.html`, `reading-library.html`, and `yoga-and-breath.html`) plus three SVG assets. The latest production snapshot is commit `ba193318500e06e04c6a506ea3363b3aab552ea7` (Vercel deployment `dpl_2Q3n6GmFCn13Lpizgx93LZJGQ6Wy`, READY) and includes the multilingual Reading Library catalogue, the Yoga & Breath guide and all existing site pages. The production alias is https://aaramora-platform.vercel.app. GitHub-to-Vercel automatic deployment is not connected, so future pushes still require a manual deployment. See [deployment notes](docs/DEPLOYMENT.md).

## Current verification

The latest GitHub Actions content-check run passed on commit `ba193318500e06e04c6a506ea3363b3aab552ea7` ([run 45282847618](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45282847618)). It includes the existing site content/route/JavaScript checks, the Reading Library preservation and rights checks, multilingual catalogue tests, and `scripts/check_catalogue.py`. The metadata-only weekly source-link workflow also passed its initial run ([run 45282656364](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45282656364)). The workflow runs on every push and pull request; see the [GitHub Actions history](https://github.com/ASHISHDAITH/aaramora-platform/actions) for the current run. This is not a browser, screen-reader, clinical or production security certification.

The current production deployment is live at the URL above. A final browser smoke test from a normal visitor session is still required. Deployment does not constitute clinical, safeguarding, accessibility or security approval.


## Multilingual reading catalogue

- `data/library.json` is the reviewed metadata source for the multilingual discovery cards. It contains titles, language tags, source links, access models, rights notes, accessibility metadata and verification dates. It does not contain third-party book text or scans.
- `data/library.schema.json` describes the catalogue record structure and required fields.
- The Reading Library includes filters for language, tradition, access, rights status, reading level and format. Every record displays a source check date and a next-review date.
- Language filters include all 22 Eighth Schedule languages, an expandable set of additional Indian languages, a selected set of global languages, and classical text languages. The language list is a discovery starting point, not a complete census of India's or the world's languages.
- The NDLI entry points to the portal's own language facets. NDLI says downloads depend on the content provider and that it aggregates resources from source institutions. Heritage Scripture Server and GRETIL entries carry their distinct script/edition and scholarly-use notes; BaniDB is linked without copying or integrating Gurbani data.
- The catalogue now contains 26 entries, including 15 edition-specific or language-index additions in Hindi, Marathi, Bengali, Punjabi, Urdu, Odia, Tamil, Gujarati, Kannada, Malayalam, Arabic, French, German, Spanish and Portuguese. Each edition has territory/item-specific rights notes and a visible editorial-review status.
- Native-language, cultural-context and accessibility review are currently pending for catalogue entries. A source-page check is not a native-speaker, legal or religious-context approval.
- GitHub Actions validates metadata on pushes and checks catalogue source links weekly. The link checker uses HEAD/range requests only and does not retrieve book contents.

- The additional set comprises 11 named text editions/folios and 4 source indexes/platforms. The source list distinguishes original-language editions from a selected page/part and from broader discovery catalogues.


### Final live check · 24 November 2026
- Latest production deploy: `dpl_Eeu3YsRJwmC86Zg652mQYriEcvbM` from site commit `a4c2a6a16632914e7fd4f2f20daae3e9a9578cde`, READY.
- 26 catalogue records, 46 original static cards retained, 55 Python tests passed. Live Chromium/axe audit: zero automated WCAG violations; 390px mobile width no horizontal overflow.
- Manual source-link audit: 32 reachable, 0 confirmed dead, 8 inconclusive; these eight need rechecking rather than being treated as broken.
- Native-language, religious/cultural-context and manual screen-reader reviews remain pending.


### Independent review and sign-off pack
- `docs/review/REVIEWER_PACK.md`: assignment requirements and sign-off forms for native-language, cultural/religious, rights and accessibility reviews.
- `docs/review/REVIEW_REGISTER.csv`: one row per catalogue record, with required specialist roles and `not_contacted` status.
- `docs/review/ACCESSIBILITY_MANUAL_TEST_PLAN.md`: NVDA, VoiceOver, TalkBack, keyboard, 320 CSS px/400% zoom, forced-colors and reduced-motion test plan.
- `docs/review/OUTREACH_DRAFTS.md`: unsubmitted academic, cultural and accessibility outreach messages.
- No reviewer or institution has yet accepted a review; all independent human-review fields remain pending. The public contacts are referral leads, not endorsements.
