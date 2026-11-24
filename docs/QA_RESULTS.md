# QA Results — Source report, 23 November 2026

## Automated/static checks reported as completed in the supplied bundle
- HTML parsed successfully with BeautifulSoup.
- All in-page anchor targets resolved; no duplicate element IDs found.
- Inline JavaScript passed `node --check`.
- No remote images, scripts, stylesheets, fonts or iframe assets are loaded by the prototype.
- No form submission, `localStorage`, `sessionStorage`, fetch, XMLHttpRequest or analytics code was found.
- Interactive activity panels are client-only and temporary.
- The candidate benchmark CSV contains exactly 50 entries; it is a research shortlist, not a verified rank order.
- The official alternate Tele-MANAS dial code was normalised to `1800-89-14416`; 14416 is also listed.

## Not completed and must not be represented as passed
- Automated browser interaction was attempted, but browser navigation was blocked by the execution environment; interactive behaviour still needs a browser run on the user's machine.
- Full browser/device visual audit on real Android and iOS devices.
- Keyboard-only and screen-reader checks with NVDA, VoiceOver and TalkBack.
- Formal WCAG 2.2 AA audit for every state and language.
- Native-speaker and clinician review of Hindi and Marathi translations.
- Qualified clinical review of all health content, including women's health and crisis language.
- Lived-experience co-design and usability sessions.
- Production privacy/security review and deployed network-traffic verification.
- Final official helpline and emergency-route verification at launch.

## Quick smoke test
1. Open `index.html` directly.
2. Use the skip link and primary navigation.
3. Open Overthinking Unload prompts and clear the note.
4. Add and reset a garden marker.
5. Match pairs in Puzzle Sanctuary and restart.
6. Change a Creative Studio colour and clear the note.
7. Expand women's-health topic cards and review the evidence caveats.
8. Check call links for Tele-MANAS and emergency support.
9. Use mobile navigation at a narrow viewport.
10. Confirm no account or network request is required for any interaction.

## Official India help references in the supplied QA report
- Directorate General of Health Services, National Mental Health Programme: https://www.dghs.mohfw.gov.in/national-mental-health-programme.php — lists 1800-89-14416 and short code 14416.
- Press Information Bureau / Ministry of Health and Family Welfare, 9 October 2026: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2321522&lang=1&reg=3 — confirms 14416 as free, confidential and 24/7.
- Verify all numbers, routing details and emergency information again immediately before release.

**Interpretation:** these are the checks reported in the supplied QA results. They are not an independent full browser, accessibility, clinical or production security certification.


## Follow-up repository QA — 24 November 2026

### Automated CI
- Historical baseline: [run 45266854917](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45266854917), 19 tests, successful.
- Current check-in update: latest main commit `91d361a2d80d5d6f046832a42b34a9bb1832d268`; [GitHub Actions run 45272441074](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45272441074) completed successfully.
- Result: **21 tests passed** (`Ran 21 tests`, `OK`). The new checks cover check-in page content, non-diagnostic/skip/privacy wording, support links, print structure, internal anchors and Node.js syntax on all five HTML pages.
- Workflow runs on pushes, pull requests and manual `workflow_dispatch`.

### Current repository additions
- `check-ins.html`: optional non-diagnostic guide finder, women's-health appointment planner and original blank two-cycle paper log.
- `docs/QUIZ_AND_SELF_CHECK_RESEARCH.md`: clinical screener evidence, regional-language limitations, instrument licensing, self-harm-risk scale cautions and product recommendations.
- `docs/CHECKIN_TOOL_SPEC.md`: privacy, interaction, accessibility and clinical-review boundaries.
- Updated research/source register, product blueprint, quiz specification, QA checklist and README.

### Deployment
- Production alias: https://aaramora-platform.vercel.app
- Latest verified production snapshot at last check: commit `3aef65fdc1f56bc3d9803ac7843ea275910f595e`, Vercel deployment `dpl_Fqfdf9uht4kjBwMnZAaPJ6WkSSjX`, READY.
- The current main branch contains the check-in page, but it is **not in that production snapshot**.
- Attempted production refresh through the connected Vercel tool returned HTTP 403 Forbidden. The connected Vercel sandbox/session endpoint also returned 403, so no CLI session was available. Do not state the new page is live until a new deployment is marked READY and the /check-ins route is visited in a regular browser.
- GitHub-to-Vercel automatic deployments remain unavailable until the Vercel GitHub App has suitable access to this repository. See `docs/DEPLOYMENT.md`.

### Remaining release gates
- Browser/device visual audit, keyboard-only and screen-reader tests.
- Formal WCAG 2.2 AA review across page states and languages.
- Qualified clinical review of mental-health and women's-health content.
- Safeguarding specialist review of relationship content.
- Native-speaker review of Hindi/Marathi/Romanised Hindi.
- Lived-experience co-design, production privacy/security review and current helpline verification.



## Reading Library multilingual release record · 24 November 2026

- GitHub Actions content check: [run 45282847618](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45282847618) — success, including catalogue validator.
- Weekly metadata-only source-link check: [run 45282656364](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45282656364) — success on initial run.
- Vercel production deployment: `dpl_2Q3n6GmFCn13Lpizgx93LZJGQ6Wy`, commit `ba193318500e06e04c6a506ea3363b3aab552ea7` — READY.
- Preserved the nine existing Reading Library sections and all 46 original resource cards; added metadata review stamps without removing existing content.
- Added 11 source records, four language groups, 22 Eighth Schedule languages, additional Indian-language filters and an initial global-language filter set.
- Remaining manual checks: live visitor-side browser smoke test, mobile widths, keyboard-only navigation, screen-reader result announcements, native-speaker review of language names/descriptions, and item-specific religious/tradition review.

## Multilingual edition catalogue expansion · 24 November 2026
- Catalogue expanded from 11 to 26 entries, including 11 named edition/folio/book records and 4 additional language indexes/platforms.
- Every entry now has scripts and editorialReview fields. New edition cards render both script labels and the native/cultural/accessibility review note.
- Tests assert that edition-specific source URLs exist, selected works are not described beyond their linked scope, and restricted sources remain link-only.
- Native-language, cultural-context and item-level accessibility reviews are explicitly pending; they have not been signed off by AARAMORA reviewers.

## Multilingual edition catalogue expansion · 24 November 2026
- Catalogue expanded from 11 to 26 entries, including 11 named edition/folio/book records and 4 additional language indexes/platforms.
- Every entry now has scripts and editorialReview fields. New edition cards render both script labels and the native/cultural/accessibility review note.
- Tests assert that edition-specific source URLs exist, selected works are not described beyond their linked scope, and restricted sources remain link-only.
- Native-language, cultural-context and item-level accessibility reviews are explicitly pending; they have not been signed off by AARAMORA reviewers.


## Problem Bench and Yoga transcript release · 24 November 2026

- Problem Bench added to `check-ins.html` with an optional local-only worksheet, no scores or diagnosis, separate influence/outside-control prompts, options/support/action/review fields and a local print view. It explicitly says it is not a clinical service or the Friendship Bench programme.
- The pre-existing guide finder, women's-health appointment planner and printable cycle log remain in the page.
- Yoga & Breath now renders four expandable draft transcripts: Hindi and Marathi guided rest; Hindi and Marathi comfortable-breathing awareness. They are labelled draft text, not recordings. Target length is 5–7 minutes each.
- The four scripts remain pending native-speaker, clinician and qualified yoga-professional approval. No audio generation job has been submitted and no audio file is published.
- WHO companion is original AARAMORA wording, not copied or translated from WHO. The WHO adaptation plan includes the licence, attribution, no-logo/non-endorsement and third-party-rights rules; outreach is drafted but not sent.
- The current content/JavaScript check passed on commit `a4c2a6a16632914e7fd4f2f20daae3e9a9578cde`: [run 45285497757](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45285497757).
- The multilingual Reading Library source-link check passed on commit `081ca9a4177fec08bbee9cd420d70cc3381975c8`: [run 45285225515](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45285225515). The checker percent-encodes Unicode source paths and only tests metadata URLs, not source text or book files.
- The current Vercel production snapshot is `dpl_CYKUri19P8g1uM4hu5tKHbiiZgjG`, READY, with the stable production alias assigned. This confirms deployment state and file inclusion, not a human clinical, accessibility, device or browser approval.
- Named clinical, safeguarding, yoga and Hindi/Marathi reviewers remain unassigned. Those are launch gates, not tasks that can be truthfully marked complete by an automated build.



## Final production verification · 24 November 2026

- Latest production deployment: `dpl_Eeu3YsRJwmC86Zg652mQYriEcvbM`, source commit `a4c2a6a16632914e7fd4f2f20daae3e9a9578cde`, READY.
- Local source validation: `python scripts/check_catalogue.py` passed for 26 catalogue entries and four language groups.
- Complete Python suite: 55 tests passed.
- GitHub content-check run for current source commit: [45285497757](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45285497757) — success.
- Unicode-aware weekly metadata-link workflow on catalogue/link-checker commit: [45285225515](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45285225515) — success.
- Manual local metadata-only link check: 32 reachable, 0 confirmed dead, 8 inconclusive (provider responses/network/certificate). Recheck those 8 on the next scheduled run.
- Production browser check: four routes HTTP 200; 26 dynamic cards and 46 original static cards; independent language/tradition/access/rights/format/search cases passed; 390px mobile layout has no horizontal overflow; keyboard skip link works; axe-core 4.10.3 reported zero violations and zero incomplete items on the audited Reading Library page.
- Hindi and Marathi Yoga & Breath draft transcript panels are visible in production; their drafts remain unapproved and are not audio recordings.
- Native-language, cultural-context, and manual assistive-technology reviews remain pending for the multilingual catalogue.



## Follow-up hardening and reviewer pack · 24 November 2026
- Fixed runtime language-filter regression: the catalogue now loads `languageAliasesMap` before filtering; it no longer references an out-of-scope fetch variable.
- Verified alias filters in a local production-like Chromium run: Manipuri → NDLI only; Meitei (Manipuri) → NDLI only; French → Monte-Cristo Tome I only; Marathi → GRETIL, NDLI and Jnaneshwari (3).
- Language-specific heading markup now includes BCP 47 `lang` and explicit Urdu RTL with English descriptor LTR.
- External result links and expandable language-group source links use contextual accessible names.
- Keyboard focus scroll padding increased to 180px to leave clearance under the sticky header. Focus auto-scroll was checked after the smooth-scroll movement settled.
- Forced-colors support and minimum 32px header/nav link height are present; reduced-motion preference sets scrolling to auto.
- Local source validator passed for 26 records; complete Python suite: 60 tests passed.
- Local Chromium audit on the candidate commit: 1280/768/390/360/320px widths with no horizontal overflow; axe-core 4.10.3 reported 0 violations (47 rule passes, 0 incomplete); no JavaScript console/page errors; Urdu lang/dir inspected.
- Independent human review remains open. Four reviewer-pack files were added under `docs/review/`; statuses are `pending` / `not_contacted`. No outreach or paid audit has been ordered.



## Support-link touch target and final candidate checks · 24 November 2026
- Increased support-contact target height to 44px and inter-target gap to 24px after a live axe scan flagged the original compact support link at one viewport.
- Local browser re-check at 1440, 390 and 320 CSS px: both support contacts measure 44px high, axe-core 4.10.3 reports 0 violations (47 passes, 0 incomplete), and no horizontal overflow or page/console errors were reported.
- Latest full Python suite after this change: 62 tests passed; catalogue validator passed.
- Human testing remains outstanding as specified in docs/review/ACCESSIBILITY_MANUAL_TEST_PLAN.md.



## Focused skip-link and touch-target recheck · 24 November 2026
- Focused skip link moves into its own flex row in the top bar. It no longer overlays the Tele-MANAS phone target on narrow screens.
- Live-style Chromium + axe-core 4.10.3 with the skip link focused at 1440px, 390px and 320px: zero violations.
- Support links: 44px height, 24px gap; no horizontal overflow at 1440px, 390px or 320px.
- Latest local validation: 26 records, 4 language groups, 22 scheduled Indian languages; 63 Python tests passed.


## Final site and RAG candidate · 24 November 2026

- Production deployment `dpl_8oRcw6Cjs5pRCFr9KHKVbErnouEo` is READY on the stable `aaramora-platform.vercel.app` alias, source commit `c1fd0b89cf28881bdef6755ba5e0e962f4a9c89c`.
- Latest GitHub content-check workflow `45388240891`: success; 85 Python tests passed, catalogue validation passed, empty approved-only corpus build passed.
- Official support-source workflow `45387267894`: success; two source URLs reachable, zero confirmed dead, one inconclusive access response. No number was changed automatically.
- RAG runtime remains disabled, model calls disabled and approved index empty.
- 100 synthetic Hinglish starter messages with jailbreak cases are checked structurally only; they have not been run against a model or classifier.
- Native-language, clinician, safeguarding and independent accessibility approvals remain pending.
- A separate manual live-site browser audit was not completed in this release step; Vercel readiness and CI do not establish that audit.
