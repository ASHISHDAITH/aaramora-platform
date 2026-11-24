# AARAMORA release quality pass · 24 November 2026

## Scope

This is an additive quality pass on the existing static-site release. It does not replace the production version, restructure the content catalogue, or remove any page, section, shelf, relationship concept, support route or media asset.

## Changes in the candidate branch

- Added a clear no-JavaScript fallback for the shared mobile navigation. When JavaScript is unavailable, the navigation remains visible and the inert menu button is hidden.
- Hardened the shared menu controller with breakpoint-aware state, Escape-to-close, outside-pointer close, and state reset when returning to the desktop layout.
- Improved visible keyboard focus for links, buttons, form controls, disclosure summaries and custom button-like controls.
- Increased consistency of practical touch target sizing for common controls.
- Added stronger contrast for several small metadata labels and explicit Tonight-mode text handling.
- Added forced-colours and higher-contrast presentation rules.
- Added 320–360 px / small-mobile layout refinements and retained reduced-motion support.
- Added regression tests for the changes and explicit preservation assertions for the 40 relationship concepts and all 49 library catalogue records across the nine original shelves.

## Verification boundary

The repository test suite is the automated source of truth for this candidate. It can check markup, CSS and JavaScript contracts; it cannot establish that the live site looks correct in every browser, that assistive technology announces every control as intended, or that the experience conforms to WCAG 2.2 AA.

The following remain open and require a human test on the exact deployed commit:

1. Windows + Firefox + NVDA and Windows + Chrome + NVDA.
2. macOS + Safari + VoiceOver, including iOS Safari + VoiceOver.
3. Android Chrome + TalkBack.
4. 200% text resize, 400% zoom / 320 CSS px, forced colours and keyboard-only operation.
5. Real device checks on slow networks and offline after first successful visit.
6. Lighthouse reports and a fresh visual review at desktop, tablet and small-phone widths.
7. Qualified clinical, safeguarding, Hindi/Marathi native-language, and cultural/religious review.

No human review, certification, Lighthouse score, screen-reader sign-off or production deployment is claimed by this change set.

## Preservation gate

Before merge, confirm that the PR contains no deleted files and that the existing content checks continue to validate:
- 40 Relationship Corner concepts.
- 49 Reading Library records and all nine original shelves.
- 25 Pune service entries across 10 facilities.
- Only the currently approved public support numbers, 14416 and 112.

## Release sequence

1. Review this additive branch and its CI results.
2. Merge only after CI passes.
3. Deploy the exact merged commit to Vercel.
4. Confirm the deployment is READY and inspect the served commit.
5. Repeat production smoke checks and complete the human test matrix before making accessibility or clinical quality claims.


## Automated checks on initial implementation commit

The initial candidate commit `8df9bc415554669c80245521206cc4417f8d64e8` passed:
- [GitHub Actions push run 45414344425](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45414344425).
- [GitHub Actions pull-request run 45414328733](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45414328733).
- 115 website/content/safety tests.
- 6 local lexical-retrieval tests.
- 49-record catalogue validation, including 4 language groups and 22 scheduled Indian languages.
- Default-deny RAG output remains empty; no model calls are made.

Later documentation-only commits will trigger the same CI workflow again. Human and production gates above remain open.


## Browser verification · 24 November 2026

The final browser test run on candidate commit `747c37c6498260ef5b73deb9a643ab30dfab3103` passed:
- Content/safety [run 45416395059](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45416395059).
- Chromium responsive [run 45416395055](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45416395055).
- 16 menu-bearing pages at 1440, 768, 390 and 320 CSS px: 64 page/viewport checks and zero horizontal overflow.
- 12 navigation checks: keyboard activation, Escape close with focus restoration, outside-pointer close.
- No-JavaScript mobile navigation fallback.
- The browser workflow uploads homepage, Relationship Corner and Reading Library screenshots, plus machine-readable results: [artifact 14933145020](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45416395055/artifacts/14933145020).

A fresh screenshot review caught and corrected a support-ribbon spacing inconsistency on the Relationship Corner. The two emergency/contact links are now separated and share consistent touch-friendly styling.

**Still open:** true browser zoom and text enlargement sessions; real NVDA/VoiceOver/TalkBack sessions; real devices; slow/offline checks; Lighthouse; clinician/safeguarding and native Hindi/Marathi plus cultural/religious reviews. The Playwright audit does not represent any of these human sign-offs and is not WCAG certification.

Production remains on the last verified production deployment. The candidate branch must be reviewed as a preview; do not promote it until the open manual and human review gates are completed.



## Latest automated release evidence · 24 November 2026

The candidate's browser and Lighthouse automation now passes on audited commit `817be3de1bc64c2c8686dcf0ad019f54964a61be`:

- [Browser + Lighthouse run 45426136282](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45426136282) · success.
- [Content/safety run 45426136166](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45426136166) · success.
- 64 responsive checks across 16 menu-bearing pages and 4 widths; 12 keyboard menu checks; 16 no-JavaScript fallback checks; four forced-colours/reduced-motion checks; 12 simulated 200% text-resize checks; all zero errors.
- Throttled-network and offline-after-cache tests passed. The offline worker's parse error was corrected and a Node syntax gate was added.
- Eight Lighthouse reports: 100 in all four categories for each of the four audited routes in both mobile and desktop profiles.
- Evidence: `docs/review/AUTOMATED_EVIDENCE_2026-11-24.md`; workflow artifact [14934504814](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45426136282/artifacts/14934504814).

The reported 200% text enlargement is automated CSS emulation, not a human browser zoom test. Real 400% zoom, physical-device offline/slow network, screen-reader testing, complete human visual review, clinician/safeguarding review, native Hindi/Marathi review and cultural/religious review remain release gates.

The successful run was on `817be3de1bc64c2c8686dcf0ad019f54964a61be`; the branch then received a Reading Library heading-wrap adjustment and an evidence-doc commit. Both CI workflows must be green on the latest head before merge or deployment. Keep production untouched until the remaining human gates are closed.


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


## Final automated quality pass and preview · 24 November 2026

**Verified application-code commit:** `78213611bfee1816404d3733e3963a6fda943a6d`.

**GitHub Actions:** all four checks passed on this exact commit:
- Push content/safety: [45433039831](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45433039831).
- Push Chromium/Lighthouse: [45433039789](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45433039789).
- Pull-request content/safety: [45433058356](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45433058356).
- Pull-request Chromium/Lighthouse: [45433058660](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45433058660).

**Content, safety and catalogue:**
- 122 website/content/safety tests passed.
- 6 local lexical-retrieval tests passed without model/network calls.
- Catalogue validator passed: 49 entries, 4 language groups, 22 scheduled Indian languages.
- Preservation checks retain 40 Relationship Corner concepts, nine original Reading Library shelves, the original 49 records and their source/rights metadata.
- Approved RAG corpus remains empty and LLM calls remain disabled.

**Browser evidence:**
- 16 menu-bearing pages at 1440, 768, 390 and 320 CSS px: 64 responsive checks.
- 12 keyboard-menu checks.
- 16/16 no-JavaScript mobile navigation checks.
- 4/4 forced-colours and reduced-motion preference checks.
- 12/12 text-only 200% enlargement emulations across homepage, Get Help, Relationship Corner and Reading Library at 768, 390 and 320 CSS px.
- Zero page-level overflow and **zero visible internal text overflow** at the 200% emulation gate.
- Slow-network test passed at 400 ms latency / 128 KiB/s down / 64 KiB/s up; homepage heading visible in 1.26 seconds in the local CI runner.
- Offline service-worker test passed: syntax and registration passed; offline page, homepage and stylesheet cached; cached homepage and unknown-route offline support card loaded after the local origin was stopped; both approved numbers 14416 and 112 were present.
- Browser audit reported zero errors.

**Lighthouse:**
Eight reports (homepage, Get Help, Relationship Corner and Reading Library, mobile and desktop). Every report scored **100** for Performance, Accessibility, Best Practices and SEO. Color-contrast, visible-label/accessibility-name and console-error quality gates passed. CLS was 0 in all eight reports. Reading Library mobile total blocking time measured 20 ms; all other profiles measured 0 ms.

**Evidence artifact:** [aaramora-responsive-visual-audit · run 45433039789](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45433039789/artifacts/14940336195). It includes screenshots, machine-readable viewport / menu / preference / large-text / offline results, and all Lighthouse JSON reports.

**Preview deployment:**
- Vercel deployment `dpl_5xRBXxtuiBFWmFQfhvj19SLoyCC7`, state READY.
- Exact source commit `78213611bfee1816404d3733e3963a6fda943a6d`.
- Preview URL: https://aaramora-platform-dpgflxktd-httpsgithubcomefigma54-devpp.vercel.app
- Branch alias: https://aaramora-platform-git-quali-a1d2eb-httpsgithubcomefigma54-devpp.vercel.app
- Production deployment `dpl_EwEu3vXSSvSS8J6wQqNEX6JLduxE` and the stable production domain remain unchanged.

**Verification limits and remaining human gates:**
- The browser's 200% text check is a DOM/CSS emulation, not a native browser zoom or text-resize session. True 400% zoom / 320 CSS-pixel manual testing is still needed.
- Direct HTTP smoke testing of the generated Vercel hostname could not be completed from the tooling environment. Vercel reports the deployment READY and confirms matching commit metadata; project-owner browser review of the preview is still required.
- Human NVDA, VoiceOver and TalkBack sessions; physical Android/iOS offline/slow-network checks; complete visual review across all routes, widths and themes; and qualified clinical, safeguarding, Hindi/Marathi language and cultural/religious reviews remain open.
- No WCAG certification, clinical approval or cultural/language sign-off is claimed.

This remains a draft, non-production quality candidate. Do not promote it until the human gates are completed and documented.


## Final support-language selector refinement · 24 November 2026

- Latest application-code commit: `c09080565d95782b2db31d15832bb52875b465ba`.
- Get Help language selector labels are concise English / हिन्दी / मराठी; the notice that Hindi and Marathi are draft wording and not yet reviewed by native speakers remains visible.
- This fixes truncation observed in the 200% text enlargement screenshot without implying translation approval.
- The latest pull-request content/safety and browser/Lighthouse runs both passed: [content 45435268537](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45435268537), [browser/Lighthouse 45435268522](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45435268522).
- Browser suite: 64 responsive checks, 12 keyboard navigation, 16 no-JavaScript, 4 preference mode, 12 large-text checks with zero page/internal visible overflow; offline and slow-network passed.
- Lighthouse: eight mobile/desktop route reports all 100 for Performance, Accessibility, Best Practices and SEO.
- Latest report/screenshots artifact: [14940817314](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45435268522/artifacts/14940817314).
- READY preview deployment `dpl_B578m9zgjfP5X5jrypnvphs88jJt`: https://aaramora-platform-pvrg7rl5w-httpsgithubcomefigma54-devpp.vercel.app.
- Production remains unchanged. Human NVDA/VoiceOver/TalkBack, real browser zoom, physical-device tests, complete visual review and qualified clinical/safeguarding/language/cultural reviews remain open.
