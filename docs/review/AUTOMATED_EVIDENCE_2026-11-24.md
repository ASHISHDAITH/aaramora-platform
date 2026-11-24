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
