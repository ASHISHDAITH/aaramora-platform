# AARAMORA — Project Memory

**Last updated:** 24 November 2026  
**Current state:** Static website prototype; chatbot and model integration disabled.

## 1. Mission

AARAMORA is an India-first mental-wellbeing and help-navigation website. It helps visitors understand information, try optional low-pressure activities, prepare for appointments and find real human support. Compete on trust, source quality and handoff to people, not engagement.

## 2. Service boundary

AARAMORA is not therapy, diagnosis, prescribing, telemedicine, emergency dispatch, an AI companion or a crisis service. Kiran is a silent visual character, not a chatbot or person. The public site does not promise clinical outcomes.

## 3. Public support policy

Only these national routes are currently displayed:
- Tele-MANAS: **14416**
- Emergency Response Support System: **112**

Both are recorded in `data/service-links.json` with official source URLs, source-check dates, next review dates and sign-off status. A named human reviewer is still pending. Do not re-add any other or alternate number until a named human reviewer has checked the official source, coverage and current access and signed the exact change.

## 4. Product and design

- The repository is a static HTML/CSS/JavaScript prototype. No npm service, database or backend is required to run the current website.
- Main navigation: Get help now, Understand, Tools and Trust.
- Sandhya visual direction: paper ivory, forest green, restrained sage and turmeric glow.
- Kiran remains a small, silent light motif; the turmeric glow dims into amber in Tonight mode.
- The homepage uses first-party illustrations and versioned local media.
- Browser tools are local-only and do not upload entries.
- The support page has a first-party offline cache after the first online visit.
- The Pune Access Map is a source-checked directory, not a ranking or verified capacity/quality claim.

## 5. Content review

Women's-health and research pages are explicitly drafts. Health content must be excluded from retrieval until a named qualified clinician signs the exact content version and its sources, language, review date and expiry are recorded. Hindi and Marathi support labels remain drafts pending native-speaker and clinician review. Source verification is not clinical sign-off.

## 6. Safety rules

Read `SAFETY.md` before changing content or code. Never invent helpline numbers or clinical facts. Do not include self-harm methods or painful substitutes. Do not diagnose or advise on medicines/doses. Never let relationship reflection become partner surveillance, coercion or a verdict about a partner. Privacy and human handoff take priority over feature completeness.

## 7. Chatbot / RAG — last, not live

The AARAMORA Guide is a future feature, **not implemented and not enabled**. Source-controlled planning files:
- `docs/RAG_CHATBOT_IMPLEMENTATION.md`
- `docs/rag/SYSTEM_PROMPT_V2.md`
- `docs/rag/CRISIS_TEMPLATE_REVIEW_DRAFT.md`
- `docs/rag/PROMPT_REVIEW_CHECKLIST.md`
- `scripts/search_reviewed_corpus.py` provides a local lexical retrieval-only Phase 2 path with citations and abstention; no model calls or network requests.
- `tests/fixtures/crisis-multilingual-301-v1.jsonl` contains 301 synthetic cases across English, Hindi, Marathi and Hinglish; all language/clinical labels remain pending human review.
- `docs/RAG_INGESTION_POLICY.md`
- `data/rag-ingestion-policy.json`
- `data/rag-corpus-manifest.json`

Non-negotiables:
1. Deterministic input safety plus an evaluated multilingual classifier runs before generation; risk accumulates within the current session.
2. Crisis signals skip the LLM and return a fixed clinician-approved message. A prompt token is only a defence-in-depth intercept, not the crisis detector.
3. Output groundedness/safety checks run after any future generation; failure is abstention.
4. Only current, signed, clinician-reviewed, rights-verified passages can enter retrieval.
5. Default-deny ingestion. Do not scrape, mass-download or bypass DRM/paywalls/borrowing; keep restricted sources link-only.
6. No accounts, transcript storage, long-term memory, model calls or analytics by default.
7. A public chatbot requires named clinical/safeguarding/engineering owners, an approved crisis script, privacy/provider review, 300+ multilingual crisis tests, jailbreak/groundedness/abstention tests, a kill switch and incident procedures.
8. The 100 Hinglish cases and 301-case multilingual pack are synthetic fixtures only. CI checks structure, not live model/detector behaviour; clinician, safeguarding and language review remain pending.

The corpus manifest is empty and runtime is disabled. The default corpus builder makes no network or model calls and rejects draft, expired, unsigned or rights-unverified sources.

## 8. Working agreements

- Read `brain.md`, `SAFETY.md` and the relevant feature spec before editing.
- Preserve current user-facing safety restrictions.
- Do not mark clinical, legal, cultural, language or accessibility review complete without named written sign-off.
- Do not send real user mental-health data to external models.
- Update documentation and tests with each product/safety change.
- Deploy only after CI passes and inspect the deployed commit; a newer GitHub main branch does not mean Vercel production is updated.


## 9. Latest verified website release · 24 November 2026

- Main commit `73c49f4182ef6befc37a8b760090acbccec1ebea` is deployed to Vercel production as `dpl_3joScLaijXWdRndiNcBw48itcvJc` (READY); stable alias `aaramora-platform.vercel.app`.
- GitHub content-check run `45391042468` passed: 97 website/content tests, 6 retrieval-only tests and the 49-record catalogue validator.
- Multilingual crisis pack: 301 synthetic structural fixtures (67 English, 67 Hindi, 67 Marathi, 100 Hinglish). No live classifier or LLM execution; all native-language, clinical and safeguarding labels remain pending.
- Pune Access Map: 25 official-page-listed service entries across 10 facilities, not an availability or quality ranking.
- Public crisis routes remain exactly 14416 and 112. Named human sign-off is still pending.
- Last small fixes: wellbeing skip link now targets `#main-content`; homepage Find a person card opens the Pune Access Map; offline support fallback includes Quick Exit.
- Do not claim whole-site screen-reader, 200% zoom, slow-network or Lighthouse sign-off from automated CI. Those checks remain open for the exact production version.


## Navigation and discovery quality pass · 24 November 2026

- Preserved all existing pages, sections, relationship concepts, Reading Library catalogue records, book shelves, quizzes, support routes and media assets. No resource data or original shelves were removed.
- Shared navigation now exposes six destinations: Get help now, Understand, Tools, Relationship Corner, Reading Library and Trust. Added responsive Menu panel, Escape-to-close, outside-click close, aria-expanded updates and current-page indication.
- All 16 menu-bearing pages load the shared `site.js`; legacy relationship/check-in menu handlers that referenced removed IDs were retired while their page-specific interaction code remains.
- Homepage retains four sections and the original choice cards, support content and pathways. It adds two discovery cards for Relationship Corner and Reading Library, including the original AARAMORA reading quote.
- Reading Library has seven media-type filters with live item counts (49 catalogue records; counts overlap because sources may have multiple content types). All nine existing reading sections and all 49 records remain.
- Shared menu, homepage discovery, media filter and preservation tests added at `tests/check_navigation_enhancements.py`.
- Current source commit: `cbba9157547dbad3422ac92304b0cbd0660b8d09`.
- GitHub content-check run `45410412093`: success. 109 main website/content/safety tests, 6 lexical retrieval tests and the 49-record multilingual catalogue validator passed.
- Production has not yet been redeployed with this commit. Keep the previous production alias until the exact commit's Vercel deployment is READY and the served-page smoke checks pass.
- This remains a static information/help-navigation prototype. Human clinician, safeguarding, native-language, cultural/religious and independent assistive-technology reviews remain pending. No whole-site WCAG 2.2 AA certification or live AI model evaluation is claimed.


## Additive discovery and navigation release · 24 November 2026

- **Production source commit:** `7da5fda5c648ac25477684e9996324e472791385`
- **Vercel production deployment:** `dpl_EwEu3vXSSvSS8J6wQqNEX6JLduxE` · READY
- **Stable alias:** https://aaramora-platform.vercel.app
- **GitHub content-check:** [run 45410648378](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45410648378) · success
- **Automated checks:** 109 website/content/safety tests passed; 6 local lexical retrieval tests passed; 49-record multilingual catalogue validator passed.
- **Navigation:** six shared destinations on all menu-bearing pages. Mobile menu toggles, Escape closes it, outside clicks close it, expanded state is announced, and the active destination is identified.
- **Homepage:** existing four sections and original pathways remain. Added Relationship Corner and Reading Library discovery cards inside the existing pathways area.
- **Relationship Corner:** 40 concept entries and existing reflection/quiz content retained.
- **Reading Library:** 49 catalogue records and all nine original shelves retained. Format filters expose Book, Video, Audiobook, Audio, Article, Blog and Image counts. Counts overlap because records can have multiple formats.
- **Other public data:** Pune Access Map remains 25 provider/government service entries across 10 facilities. It does not confirm live appointments, eligibility, fees or service quality.
- **Support contacts:** public pages show only Tele-MANAS 14416 and Emergency 112. Named human sign-off remains pending.
- **Privacy/safety:** the site remains static and account-free; personal worksheet content is not sent to AARAMORA servers. RAG approved index remains empty and LLM calls disabled.
- **Live smoke checks:** homepage, Relationship Corner, Reading Library, support, wellbeing, Access Map, Tools, Trust, privacy, women’s-health draft, research draft and community concept pages returned HTTP 200. The catalogue JSON, Pune data, shared JS/CSS, service worker, favicon, manifest, original SVG illustrations and pinned film also returned HTTP 200.
- **Live preservation checks:** 40 relationship concepts; nine original Reading Library shelves; 49 catalogue records; 25 Pune service entries and 10 facilities.
- **Open manual gates:** no fresh whole-site visual browser audit, screen-reader run by a human, 200%/400% zoom session, slow-network/offline device test or Lighthouse report is claimed for this release. Clinician, safeguarding, Hindi/Marathi native-language, cultural/religious and independent assistive-technology reviews remain pending.

This is an additive quality release. No original page, relationship concept, reading-library shelf, catalogue record, support route or media file was intentionally deleted.

## Kiro IDE migration and continuation brief · 24 November 2026

**Primary development environment:** Kiro IDE (vibe-coding workflow).  
**Source of truth:** this Git repository and its reviewed project documentation.  
**Production host:** Vercel, stable alias https://aaramora-platform.vercel.app.  
**Repository:** https://github.com/ASHISHDAITH/aaramora-platform  
**Default branch:** `main`.  
**Migration type:** development-environment handoff only. This is not a framework migration, rewrite, redesign reset or content reset.

### 1. Current baseline to preserve

The latest reported production release is source commit `7da5fda5c648ac25477684e9996324e472791385`, Vercel deployment `dpl_EwEu3vXSSvSS8J6wQqNEX6JLduxE` (READY), with the stable alias above. GitHub content-check run `45410648378` is reported successful.

Preserve all existing source files and content, including:
- The static HTML/CSS/JavaScript architecture and existing routes.
- All six shared navigation destinations: Get help now, Understand, Tools, Relationship Corner, Reading Library and Trust.
- Responsive navigation, Escape handling, outside-click close, `aria-expanded`, active-page indication and Quick Exit.
- The original four homepage sections and pathways, plus the Relationship Corner and Reading Library discovery cards.
- Relationship Corner's 40 concepts, guides, reflection tools, quizzes and safety information.
- Reading Library's 49 catalogue records, all nine original shelves, seven format filters and all source links, rights notes and attribution.
- Pune Access Map's 25 service entries across 10 facilities.
- All illustrations, images, brand-film media, service worker, CSS, JavaScript, manifest, sitemap, tests, scripts, data and research/documentation files.

Counts are preservation baselines, not goals to reduce or replace. Format totals overlap because one catalogue source can carry multiple formats.

### 2. Kiro operating procedure

At the start of each Kiro session:
1. Read `brain.md`, `SAFETY.md`, `README.md`, and `CONTRIBUTING.md`.
2. Read the feature-specific specification, source register, rights note and relevant tests before editing that feature.
3. Inspect `git status`, current branch and latest commit. Do not overwrite or discard uncommitted user work.
4. Inspect the live source files and tests. Treat this memory as project direction, not a substitute for source-code inspection.
5. Write a short implementation plan and identify the exact files expected to change.
6. Make small additive changes. Preserve existing IDs, routes, content, data records, links, attribution and interactions unless a verified defect requires a narrowly scoped correction.
7. Run the relevant focused tests, then the full suite and catalogue/source checks.
8. Review the diff for accidental deletion, weakened safety wording, changed helpline data, removed content, broken links, new third-party calls or exposed private data.
9. Update `brain.md` and relevant feature/QA documentation in the same change.
10. Commit and push only after checking the diff and test output. Never force-push or use destructive Git commands as a shortcut.
11. Vercel production is only updated after a deployment is explicitly triggered and the exact deployed commit is checked. A successful push or GitHub CI run is not proof that production changed.
12. Run live smoke checks on the deployed version before describing it as live.

### 3. Kiro project instructions to maintain

Use this section as the repository-level working contract for Kiro:

- **Enhance, do not replace.** No wholesale rebuild, page deletion, content pruning, route consolidation, framework conversion or visual reset without a separate, explicit user decision.
- **Preserve first.** Before and after each task, verify the counts and presence of the 40 relationship concepts, 49 catalogue records, nine original shelves, 25 Pune service entries and 10 facilities.
- **Static-first.** The current project is a static site. Do not add a backend, database, login, server-side journal, analytics, remote font, model endpoint or third-party runtime dependency merely for convenience.
- **No invented authority.** Do not claim top-1% status, clinical efficacy, WCAG conformance, verified capacity, endorsements, or human review without evidence and named sign-off.
- **Respect project architecture.** Inspect existing shared CSS/JS patterns and test approach before creating abstractions or dependencies.
- **Stay additive and reversible.** Prefer targeted CSS, semantic HTML and small JavaScript changes. Do not replace whole files when a focused patch is sufficient.
- **No silent content changes.** Do not rewrite sacred texts, scripture translations, source titles, clinical content or rights notes without source-specific checks and the required review.
- **No secrets or real disclosures.** Never place API keys, personal journals, health records, real visitor submissions or credentials in source, prompts, logs, screenshots, fixtures or commits.
- **No automatic publishing.** Kiro may prepare and verify a change; production deployment remains a deliberate, separately verified step.

### 4. Safety and public-service invariants

Read `SAFETY.md` before any safety-sensitive change. The site is information and help navigation, not therapy, diagnosis, prescribing, telemedicine, emergency dispatch or an AI companion.

Public national support routes remain exactly:
- Tele-MANAS: **14416**
- Emergency Response Support System: **112**

Do not add or substitute a helpline number without named human review of the official source, current availability, geographic coverage and exact wording, with the change recorded in `data/service-links.json`.

Relationship features must not become partner surveillance, location tracking, coercion, manipulation or a verdict about a person. Respect no-contact and requests for space. Quick Exit must not be described as erasing browser history, network logs or shared-device activity.

The future AARAMORA Guide/RAG remains disabled. The approved retrieval corpus remains empty, and there must be no LLM calls, chatbot UI, transcript storage, accounts or long-term memory unless every release gate in the RAG documents has been met and the user explicitly approves that scope. Never scrape, mass-download, bypass DRM/paywalls/borrowing controls, or ingest restricted sources.

### 5. Commands and verification

The current repo is static and does not require a Node application build to serve locally. A simple local preview is:

```bash
python -m http.server 8000
```

Open `http://localhost:8000`.

The repository's GitHub Actions workflow runs Python unittest discovery:

```bash
python -m unittest discover -s tests -p 'check_*.py' -v
```

Also run the catalogue validator:

```bash
python scripts/check_catalogue.py
```

Run relevant additional checks for service links, library links, retrieval fixtures or inline JavaScript when those areas change. Confirm the commands from the current workflows/scripts before relying on them; do not invent a package manager or build command.

### 6. Open release-quality gates

These remain open unless a dated result and evidence are added:
- Fresh visual review at desktop, tablet and small mobile widths.
- Human NVDA, VoiceOver and TalkBack testing.
- 200% text enlargement and 400% zoom/reflow.
- Slow-network and real-device offline testing.
- Current Lighthouse performance and accessibility reports.
- Qualified clinical, safeguarding, Hindi/Marathi native-language and religious/cultural review.
- Human sign-off on the exact public support-route copy and source register.

Automated tests and Vercel READY status do not close these gates. Do not claim WCAG 2.2 AA certification or clinical approval.

### 7. First Kiro task sequence

1. Open the existing repository folder in Kiro; do not create a new project scaffold.
2. Confirm the checked-out branch and working tree. Make a backup branch before broad multi-file work.
3. Run the existing test suite and catalogue validator before changing anything; record baseline output.
4. Inspect the homepage and shared navigation at desktop, tablet and narrow mobile sizes. Record defects without deleting or simplifying existing content.
5. Continue the open manual quality gates in `docs/review/ACCESSIBILITY_MANUAL_TEST_PLAN.md` and the existing QA documents.
6. Fix issues in small, reviewable batches. Add regression tests for each defect.
7. Verify content-preservation counts and public support routes after every change batch.
8. Update this memory and relevant docs; review the full Git diff.
9. Push to GitHub, verify Actions, and deploy to Vercel only as a deliberate release step.
10. Smoke-test the stable domain and record the exact source commit, deployment ID and results.

### 8. Change log and handoff note

This section records the move to Kiro as the primary coding IDE. It does not assert that Kiro has already opened, indexed, edited, tested or deployed the repository. The next Kiro session must inspect the actual local checkout and current Git state before acting.

**Non-negotiable instruction:** make AARAMORA more polished, coherent, accessible, fast and trustworthy while preserving everything that already exists. Never trade away safety, content, source rights, privacy or working pathways for visual novelty.

## Additive skip-link correction · 24 November 2026

- Verified `relationships.html` had both a legacy `class="skip"` link and the shared `class="skip-link"` link, both targeting the existing `#main` landmark.
- Removed only the redundant legacy link; kept the shared skip link and main landmark unchanged.
- Added a regression assertion in `tests/check_navigation_enhancements.py`.
- This source correction does not claim a human screen-reader or browser test. CI will provide the automated result for the commit.
- No page content, relationship concept, quiz, guide, shelf, catalogue record, service entry, support route or media asset was removed.
