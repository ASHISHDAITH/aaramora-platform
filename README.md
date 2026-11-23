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

The homepage follows a warm editorial botanical system: paper ivory, forest green, restrained sage, pale blue, muted lilac and clay accents. The 16:9 AARAMORA brand film sits in the hero as a user-controlled player; three credited Pexels photographs support the optional journaling, connection and professional-support pathways. Stock photographs are illustrative only and are not testimonials or representations of actual AARAMORA staff.

See [docs/DESIGN_SYSTEM.md](docs/DESIGN_SYSTEM.md) for color tokens, typography, responsive rules, image credits and video behavior.

## Included experience

- Calm first-visit welcome, optional entry pathways and the fictional Kiran/firefly visual guide.
- India human-support routes, optional pause prompts and low-stimulation Night Help.
- Overthinking Unload, Little Garden, untimed Puzzle Sanctuary, Creative Studio and Safe Corner.
- Mental wellbeing guides covering depression, anxiety, panic, acute stress surges, trauma-related distress, rumination, sleep, burnout, grief and OCD-related experiences.
- Relationships corner with 40 searchable concepts, three optional non-diagnostic reflections, a non-scored safety check and practical guidance for different sides of a relationship cycle.
- Women's-health corner with eight topic areas and the shared “how it may feel / what may help / when to seek support” structure.
- Reading library with open educational resources, explicit licence notes and publisher links for copyrighted books.
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
- `docs/RESEARCH_SOURCES.md` — source and licensing register.
- `docs/QA_CHECKLIST.md`, `docs/QA_RESULTS.md` and `docs/VALIDATION_NOTES.md` — quality gates, completed checks and remaining reviews.
- `docs/DEPLOYMENT.md` — live Vercel deployment status, verification notes and the remaining Git-integration step.
- `docs/AARAMORA_BRAND_FILM_ASSETS.md` — export manifest, verified file hashes and committed media paths.
- `tests/check_relationships.py` and `tests/check_health_topics.py` — automated static content and safety checks.
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
- `reading-library.html` provides legal read/download links for explicitly licensed open resources and publisher/library access to copyrighted relationship books.
- The GitHub source reference for OpenStax is `openstax/OpenStaxOnTheGo`; its repository AGPL licence covers software, while the book asset has its own source licence. The current official OpenStax site is the preferred download source.
- Never bypass DRM, paywalls, private repository permissions or import copyrighted book copies without permission.
- A public GitHub repository or its root licence does not automatically license every bundled third-party book, image or dataset.

- `reading-library.html` also lists focused Noba attachment/relationship modules and a downloadable *Psychology of Human Relations* PDF.
- OpenStax Psychology 2e is shown under its current CC BY-NC-SA 4.0 terms. Its current preface prohibits LLM/AI ingestion without prior written permission.


## Automated checks
GitHub Actions runs `python -m unittest discover -s tests -p 'check_*.py' -v` on pushes and pull requests. The checks cover core page routes, wellbeing content structure, women's-health consistency, all 40 relationship concepts, optional quiz/privacy requirements, support links, internal anchors and inline JavaScript syntax on all four site pages.


## Brand film

The first AARAMORA six-scene brand-film exports are reviewed and committed in Git:
- `assets/brand-film/aaramora-master-16x9.mp4` — 16:9 website master.
- `assets/brand-film/aaramora-instagram-9x16.mp4` — 9:16 Instagram edit.

The supplied `CLEAN_NO_ADDED_AUDIO` file is byte-identical to the landscape master and still contains AAC audio, so it is not a separate silent export. The homepage player uses the landscape master and offers the vertical edit as a separate link. See [the export manifest](docs/AARAMORA_BRAND_FILM_ASSETS.md).

## Live deployment

**Production URL:** https://aaramora-platform.vercel.app

The current public static deployment is marked READY by Vercel. It contains the four HTML pages and three SVG assets. The MP4 files remain versioned in GitHub and are delivered from the repository CDN URLs. This first deployment was uploaded directly to Vercel from commit `243b51188437d79a901b560df2e21dc573a8f793`; GitHub-to-Vercel automatic deployment is not yet connected, so later Git pushes do not publish automatically. See [deployment notes](docs/DEPLOYMENT.md).

## Current verification

The latest GitHub Actions content-check run passed on the current repository history. It executed 19 Python static tests, including Node.js syntax validation of inline JavaScript on all four site pages. This is not a browser, screen-reader, clinical or production security certification.

The current production deployment is live at the URL above. A final browser smoke test from a normal visitor session is still required. Deployment does not constitute clinical, safeguarding, accessibility or security approval.
