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
- Yoga & Breath guide with study-specific evidence summaries, optional low-intensity practices, safety boundaries and Hindi/Marathi transcript drafts pending native-language and clinical/yoga review.
- Relationships corner with 40 searchable concepts, three optional non-diagnostic reflections, a non-scored safety check and practical guidance for different sides of a relationship cycle.
- Check-ins page with a non-scored guide finder, on-page women's-health appointment planner and printable original two-cycle symptom log.
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
- `docs/YOGA_AND_BREATH_AUDIO_SCRIPTS.md` — original Hindi/Marathi guided-rest and comfortable-breathing transcript drafts; not approved or recorded audio.
- `docs/RESEARCH_SOURCES.md` — source and licensing register.
- `docs/QA_CHECKLIST.md`, `docs/QA_RESULTS.md` and `docs/VALIDATION_NOTES.md` — quality gates, completed checks and remaining reviews.
- `docs/DEPLOYMENT.md` — live Vercel deployment status, verification notes and the remaining Git-integration step.
- `docs/AARAMORA_BRAND_FILM_ASSETS.md` — export manifest, verified file hashes and committed media paths.
- `tests/check_relationships.py`, `tests/check_health_topics.py` and `tests/check_reading_library.py` — automated static content, safety and reading-library rights checks.
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
GitHub Actions runs `python -m unittest discover -s tests -p 'check_*.py' -v` on pushes and pull requests. The checks cover core page routes, wellbeing content structure, women's-health consistency, all 40 relationship concepts, optional quiz/privacy requirements, support links, internal anchors and inline JavaScript syntax on all five site pages.


## Brand film

The first AARAMORA six-scene brand-film exports are reviewed and committed in Git:
- `assets/brand-film/aaramora-master-16x9.mp4` — 16:9 website master.
- `assets/brand-film/aaramora-instagram-9x16.mp4` — 9:16 Instagram edit.

The supplied `CLEAN_NO_ADDED_AUDIO` file is byte-identical to the landscape master and still contains AAC audio, so it is not a separate silent export. The homepage player uses the landscape master and offers the vertical edit as a separate link. See [the export manifest](docs/AARAMORA_BRAND_FILM_ASSETS.md).

## Live deployment

**Production URL:** https://aaramora-platform.vercel.app

The current public static deployment is marked READY by Vercel and serves six HTML pages (`index.html`, `wellbeing.html`, `relationships.html`, `check-ins.html`, `reading-library.html`, and `yoga-and-breath.html`) plus three SVG assets. The latest snapshot is commit `05eec4ca64501910ecc2492607cc24f945bb5c48` and includes the Yoga & Breath guide alongside the expanded Reading Library. The production alias is https://aaramora-platform.vercel.app. GitHub-to-Vercel automatic deployment is not connected, so future pushes still require a manual deployment. See [deployment notes](docs/DEPLOYMENT.md).

## Current verification

The latest GitHub Actions content-check run passed after the simplified homepage update. It includes the static content, route and JavaScript checks across all five site pages. The Reading Library static content, route, rights-wording and JavaScript checks passed. The workflow runs on every push and pull request; see the [GitHub Actions history](https://github.com/ASHISHDAITH/aaramora-platform/actions) for the current run. This is not a browser, screen-reader, clinical or production security certification.

The current production deployment is live at the URL above. A final browser smoke test from a normal visitor session is still required. Deployment does not constitute clinical, safeguarding, accessibility or security approval.
