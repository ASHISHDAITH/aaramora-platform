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


## Additive responsive and accessibility quality pass · 24 November 2026

- Candidate branch: `quality-pass-2026-11-24`, based on the current `main` head `d1a59577896feb4598ce8fe72b44c4cc78cebb91`.
- This is a non-destructive candidate only. It does not deploy to production and does not replace the current Vercel alias.
- Updated `site.css` with refined mobile spacing down to 320 CSS px, stronger small-label contrast, visible focus, larger common targets, forced-colour/high-contrast support, and reduced-motion safeguards.
- Updated `site.js` so mobile navigation has explicit breakpoint-aware state, closes on Escape and outside pointer input, and resets on desktop resize. The page exposes a no-JavaScript mobile-navigation fallback.
- Added `tests/check_responsive_accessibility_quality.py` to check these safeguards and verify the 40 relationship concepts, 49 library records and nine original shelves remain present.
- Added `docs/RELEASE_QUALITY_PASS_2026-11-24.md` with scope, gates and deployment sequence.
- GitHub Actions push run `45414344425` and pull-request run `45414328733` passed on candidate commit `8df9bc415554669c80245521206cc4417f8d64e8`: 115 website/content/safety tests, 6 retrieval-only tests and the 49-entry catalogue validator passed; the RAG index remains empty and LLM calls disabled.
- Human NVDA, VoiceOver, TalkBack, 200%/400% zoom, physical-device offline/slow-network, visual review, Lighthouse and qualified clinical/language/cultural review are still outstanding. No WCAG conformance or clinical sign-off is claimed.
- Do not merge or deploy until CI passes; after merge, deploy the exact commit and repeat live smoke tests. Production remains on the previously verified release until then.


## Responsive browser audit and final ribbon pass · 24 November 2026

- Added shared support-ribbon styling to keep the Tele-MANAS and Emergency contacts visibly separated, consistently styled and easy to tap on the Relationship Corner and other pages.
- Added `.github/workflows/browser-quality.yml` and `scripts/audit_responsive_browser.py`. The browser audit uses Playwright Chromium against all root HTML pages that expose the shared six-link menu.
- Latest candidate commit `747c37c6498260ef5b73deb9a643ab30dfab3103` passed both GitHub workflows: content/safety checks `45416395059` and Chromium browser audit `45416395055`.
- Browser evidence: 16 pages × 4 widths (1440, 768, 390, 320 CSS px) = 64 page/viewport checks; zero horizontal overflow; 12 keyboard navigation checks; Escape closes and restores focus; outside pointer closes; mobile navigation remains visible with JavaScript disabled. Visual screenshots and `results.json` are stored in artifact `14933145020`.
- Automated content/safety suite still verifies 40 relationship concepts, 49 Reading Library catalogue records, nine original shelves, approved support-number policy and catalogue rights/language metadata.
- Still not complete: real NVDA/VoiceOver/TalkBack testing; true browser text-size/400%-zoom sessions; physical Android/iOS checks; slow/offline network testing; Lighthouse audit; named clinician, safeguarding, Hindi/Marathi, and cultural/religious review. No WCAG or clinical sign-off claim.
- Production deployment and stable alias remain untouched; this branch is a preview/review candidate only.



## Latest automated quality evidence · 24 November 2026

- Browser + Lighthouse workflow passed on commit `817be3de1bc64c2c8686dcf0ad019f54964a61be`: [run 45426136282](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45426136282). Content/safety workflow passed: [run 45426136166](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45426136166).
- Browser audit: 16 pages × 4 widths (1440, 768, 390, 320 CSS px) = 64 checks; zero baseline overflow; 12 keyboard-menu checks; 16/16 no-JavaScript fallbacks; 4/4 forced-colours/reduced-motion checks; 12/12 simulated 200% text-resize checks; slow-network and service-worker offline fallback passed; zero errors.
- Lighthouse: eight reports (homepage, Get Help, Relationship Corner and Reading Library, mobile and desktop). Every report scored 100/100 for Performance, Accessibility, Best Practices and SEO. Contrast, label/content-name and console checks clean; CLS 0 in all eight runs.
- Offline service worker had a real parse error fixed; `node --check service-worker.js` is now a CI gate. Offline test proves cached homepage and offline support card load with local origin stopped.
- Human visual spot-check reviewed homepage, Relationship Corner and Reading Library screenshots across desktop/mobile, plus Library at simulated 200% text enlargement.
- Evidence and limits: `docs/review/AUTOMATED_EVIDENCE_2026-11-24.md`. Artifact: [14934504814](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45426136282/artifacts/14934504814).
- Important: those results belong to the cited audited commit. A follow-up Reading Library heading-wrap commit and the evidence documentation were added after it; new CI must pass on the latest branch head before merge/deploy.
- Still open: real NVDA/VoiceOver/TalkBack sessions; actual browser 200%/400% zoom and physical-device testing; visual review of every page/device/theme; clinician, safeguarding, native Hindi/Marathi and cultural/religious review. No WCAG, clinical or cultural sign-off is claimed.
- Production has not been changed. Keep the candidate on preview until the latest commit passes CI and human review gates are recorded.


## Final CI and preview status · 24 November 2026

- Final branch head before this documentation-only status entry: `ce03b725fe4b045a84c52eb111f45b063d6bf14e`.
- Latest content/safety run [45427925139](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45427925139): passed.
- Latest Chromium + Lighthouse run [45427925081](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45427925081): passed on the same commit. It confirmed 64 responsive checks with zero errors, 12 keyboard-menu checks, 16 no-JavaScript fallbacks, 4 preference checks, 12 simulated 200% text-resize checks, slow-network and offline support fallback, and eight Lighthouse reports all scoring 100 in Performance, Accessibility, Best Practices and SEO.
- Latest evidence artifact: [14937965984](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45427925081/artifacts/14937965984).
- Vercel preview: deployment `dpl_Enx61H6gxs72Km94YfLGfeLoZaAF`, state READY, exact source commit `ce03b725fe4b045a84c52eb111f45b063d6bf14e`; URL: https://aaramora-platform-eshn1fcok-httpsgithubcomefigma54-devpp.vercel.app
- Stable branch preview alias: https://aaramora-platform-git-quali-a1d2eb-httpsgithubcomefigma54-devpp.vercel.app
- Production remains unchanged; the existing production deployment is still `dpl_EwEu3vXSSvSS8J6wQqNEX6JLduxE`.
- The execution environment could not independently fetch the generated Vercel hostname for a live HTTP smoke test. Vercel confirms READY state and matching Git metadata; the preview still needs direct browser review by the project owner.
- Human gates remain open: real NVDA/VoiceOver/TalkBack sessions; native browser 200%/400% zoom; physical Android/iOS slow/offline tests; full-site visual review; qualified clinical/safeguarding, native Hindi/Marathi and cultural/religious review. No accessibility or clinical certification is claimed.
