# Aaramora Platform

A privacy-first mental-wellbeing and women's-health information and help-navigation platform for India.

**Experience principle:** You do not have to figure everything out today.

This repository contains the integrated static website prototype and the research, visual design, content, safety and QA materials assembled from the project discussion and supplied source files.

## Run the website

Open `index.html` in a modern browser, or run:

```bash
python -m http.server 8000
```

Then visit http://localhost:8000.

No npm install, database, account, remote fonts, analytics, AI API or backend is required for this prototype.

## Included experience

- Calm first-visit welcome, optional entry pathways and the fictional Kiran/firefly visual guide.
- India human-support routes, optional pause prompts and low-stimulation Night Help.
- Overthinking Unload, Little Garden, untimed Puzzle Sanctuary, Creative Studio and Safe Corner.
- Guided next steps, resource shelf and future community concept (not a live forum).
- Women's Health: PMOS (formerly PCOS), endometriosis, heavy/painful periods, PMS/PMDD, menopause, thyroid, iron deficiency/anaemia and postpartum mental health.\n- Mental wellbeing: depression, anxiety, panic, acute stress surges, trauma/PTSD, rumination, sleep, burnout, grief and OCD-related experiences, each with how it may feel, what may help and when to seek support.\n- Relationships corner: attachment protest, attachment anxiety/avoidance concepts, pursue–withdraw patterns, conflict repair, boundaries, consent, breakups and family pressure, with optional unvalidated self-reflection tools and a safety-first route.\n- Women's health: PMOS (formerly PCOS; PCOD retained as a search alias), endometriosis, menstrual health, menopause, thyroid, iron deficiency and postpartum mental health.

## Research and design materials

- `docs/ORIGINAL_RESEARCH_BRIEF.md` — original product concept, candidate sites, feature ideas, sitemap and roadmap.
- `docs/PRODUCT_BLUEPRINT.md` — complete product role, journeys, feature scope, governance and roadmap.
- `docs/DESIGN_RESEARCH_AND_DIRECTION.md` and `docs/DESIGN_SYSTEM.md` — design rationale and UI rules.
- `docs/EXPERIENCE_MAP.md` — visitor journeys and information architecture.
- `docs/WOMENS_HEALTH_RESEARCH.md` — women's-health research and clinical review boundaries.\n- `relationships.html` — dedicated relationship education corner and in-page reflection quizzes.\n- `wellbeing.html` — mental-health condition guides using the shared feel/help/seek-support pattern.\n- `docs/HEALTH_TOPIC_CONTENT_STANDARD.md` — one shared editorial standard across every health topic.\n- `docs/MENTAL_WELLBEING_AND_WOMENS_HEALTH_RESEARCH.md` — curated sources, limits and current terminology.\n- `docs/RELATIONSHIPS_RESEARCH.md` — curated attachment, conflict, relationship-education and interpersonal-violence references.\n- `docs/RELATIONSHIP_QUIZ_SPEC.md` — quiz design, outputs, privacy and release gates.\n- `docs/RELATIONSHIP_CONCEPT_CONTENT_MAP.md` — 40 concepts, evidence/status notes and practical guidance aligned to the uploaded report.\n- `SAFETY.md` — cross-site safety rules.
- `docs/RESEARCH_SOURCES.md` — source register.
- `docs/QA_CHECKLIST.md`, `docs/QA_RESULTS.md` and `docs/VALIDATION_NOTES.md` — quality gates, checks and remaining reviews.\n- `tests/check_relationships.py` — static checks for relationship page safety, links and privacy boundaries.\n- `tests/check_health_topics.py` — static checks for mental and women's-health topic structure and links.
- `research/benchmark50.csv` — 50-site benchmark candidate list (not a verified ranking).
- `research/mental-health-website-benchmark-report.md` — benchmark shortlist and product strategy.
- `research/visual-report.html` — browser-viewable visual concept report.
- `assets/` — original Healing Garden, Safe Corner and Thought River SVG illustrations.
- `CONTRIBUTING.md` and `SECURITY.md` — contribution and privacy rules.

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
