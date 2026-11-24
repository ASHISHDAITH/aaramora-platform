# AARAMORA automated release evidence · 24 November 2026

## Candidate scope

This evidence is for the non-production candidate branch `quality-pass-2026-11-24`. The audited browser/Lighthouse commit was `817be3de1bc64c2c8686dcf0ad019f54964a61be`; the branch subsequently added a Reading Library large-heading wrap adjustment in `12daf77a30caf4c5d5147a4d0942d3b399500ebc`. A new CI run is required for the latest branch head after the accompanying documentation update.

Production was not changed by this quality pass.

## Automated checks passed on the audited commit

- Browser workflow: [GitHub Actions run 45426136282](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45426136282) — success.
- Content/safety workflow: [GitHub Actions run 45426136166](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45426136166) — success.
- 16 menu-bearing pages × 4 CSS viewport widths (1440, 768, 390 and 320 px): **64 checks, zero errors and zero baseline horizontal overflow**.
- Mobile navigation: **12 keyboard checks** covering open, Escape close/focus restoration and outside-pointer close.
- No-JavaScript navigation fallback: **16 of 16 pages passed**.
- Forced-colours + reduced-motion browser preference checks: **4 of 4 passed** on homepage, Get Help, Relationship Corner and Reading Library.
- 200% text-only enlargement emulation: **12 checks passed** across homepage, Get Help, Relationship Corner and Reading Library at 768, 390 and 320 CSS px. This is a DOM/CSS emulation, not a substitute for a real browser text-size or 400% zoom session.
- Throttled-network smoke test: homepage rendered under a 400 ms latency / 128 KiB/s download / 64 KiB/s upload profile; the main heading became visible in 1.24 seconds in the local test environment.
- Offline test: service worker syntax passed; worker activated and controlled the page; offline page, homepage and stylesheet were cached; cached homepage opened with the origin stopped; an uncached URL returned the offline support card (HTTP 200) with both approved `tel:14416` and `tel:112` links.
- Total browser audit errors: **0**.

## Lighthouse results

Eight lab reports were generated: homepage, Get Help, Relationship Corner and Reading Library, each in mobile and desktop profiles.

| Route | Profile | Performance | Accessibility | Best Practices | SEO |
|---|---|---:|---:|---:|---:|
| Homepage | Mobile | 100 | 100 | 100 | 100 |
| Homepage | Desktop | 100 | 100 | 100 | 100 |
| Get Help | Mobile | 100 | 100 | 100 | 100 |
| Get Help | Desktop | 100 | 100 | 100 | 100 |
| Relationship Corner | Mobile | 100 | 100 | 100 | 100 |
| Relationship Corner | Desktop | 100 | 100 | 100 | 100 |
| Reading Library | Mobile | 100 | 100 | 100 | 100 |
| Reading Library | Desktop | 100 | 100 | 100 | 100 |

All audited Lighthouse quality gates were clean: color contrast, label/content-name matching and browser console errors. The audit recorded zero cumulative layout shift in all eight profiles. Representative FCP/LCP were 0.9–1.2 s on mobile and 0.3–0.5 s on desktop in the local lab environment. These are lab measurements, not field data or a guarantee for every device/network. Lighthouse scores are not WCAG conformance or clinical certification.

## Visual screenshot review

A human spot-check was performed on the saved screenshots for:
- Homepage: desktop and mobile.
- Relationship Corner: desktop and mobile.
- Reading Library: desktop and mobile.
- Reading Library at the 200% text-only enlargement emulation.

The spot-check found no obvious page clipping in those captured views after the reflow fixes. It does not constitute a full manual visual review of every page, browser and device.

Evidence artifact: [aaramora-responsive-visual-audit · run 45426136282](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45426136282/artifacts/14934504814). The artifact contains screenshots, machine-readable viewport/navigation/preference/text-resize/offline results, Lighthouse JSON reports and the Lighthouse summary.

## Preserved content and safety constraints

The existing content checks continue to protect the 40 Relationship Corner concepts, 49 Reading Library catalogue records, all nine original Reading Library shelves, 25 Pune service listings across 10 facilities and the approved public support contacts (Tele-MANAS 14416 and Emergency 112). The account-free/static privacy model remains unchanged; the approved RAG corpus remains empty and LLM calls remain disabled.

No original page, relationship guide, quiz, reflection, shelf, catalogue record, source link, rights note, attribution, service listing or media file was intentionally removed.

## Still requiring human or external review

1. Actual screen-reader sessions with NVDA (Windows/Firefox and Windows/Chrome), VoiceOver (macOS/Safari and iOS/Safari), and TalkBack (Android/Chrome).
2. Real browser 200% text resizing and 400% zoom / 320 CSS px checks, including keyboard focus and landscape orientation.
3. Physical Android and iOS testing for offline-after-first-visit and slow-network behaviour.
4. Human visual review across the full site, including tablet and small mobile widths, light and Tonight themes, and real video/media playback.
5. Qualified clinician and safeguarding review of sensitive mental-health and relationship guidance.
6. Qualified native Hindi and Marathi language review, including crisis wording and accessibility phrasing.
7. Cultural/religious review of Hindu, Sikh, Muslim and other tradition-related resources, including rights, attribution and contextual accuracy.

No human tester sign-off, WCAG certification, clinical sign-off or cultural/language approval is claimed. Keep the candidate on preview until the human gates and latest-commit CI are complete. Do not promote it to production as part of this automated pass.


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
