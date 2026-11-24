# AARAMORA Reading Library — manual accessibility test plan

Last prepared: 24 November 2026. This is a test plan, not a conformance statement.

## Already checked automatically

- axe-core 4.10.3: zero reported violations in the previous production audit.
- Browser widths 1280, 768, 390, 360 and 320 CSS px: no horizontal overflow in the previous browser audit.
- Keyboard first Tab reaches the skip link and Enter follows it to main content.
- Chromium accessibility tree exposed main, banner, contentinfo, a searchbox, status region and seven named comboboxes.
- Results paragraph uses role=status and aria-live=polite.
- Updated catalogue renders BCP 47 language tags and an explicit RTL wrapper for the Urdu native title.
- Forced-colors and larger focus target CSS fallback rules have been added; re-test in a fresh production browser after deployment.

## Human testing still outstanding

| Environment | Required tester | Minimum task set |
|---|---|---|
| Windows + Firefox + NVDA | NVDA user | Heading/list/landmark navigation; filters; status announcement; source links |
| Windows + Chrome + NVDA | NVDA user | Repeat primary browse/search/filter flow |
| macOS + Safari + VoiceOver | VoiceOver user | Rotor headings/links, language changes, bidi order, details/summary |
| iOS + Safari + VoiceOver | VoiceOver user | Touch exploration, focus order, zoom, language labels |
| Android + Chrome + TalkBack | TalkBack user | Swipe order, activate filters, change language, hear result count |
| Windows high contrast / forced colours | Low-vision user or experienced evaluator | Text/cards, borders, focus and source links |
| Browser 400% zoom or 320 CSS px | Low-vision tester | Reflow, visible focus, no loss of content or actions |
| Reduced-motion preference | Motion-sensitive user/evaluator | No essential content requires motion; no smooth-scroll dependency |

## Test scripts

1. From a fresh load, Tab once. Confirm the skip link is visible. Enter it and confirm main content receives focus or the main landmark is reached.
2. Tab through support links, primary navigation, hero links, search, all filters, clear-filters, sort, language-group details, result actions and footer. No focus trap or lost focus.
3. Type Marathi in search, then select Marathi in the language filter. Confirm results update and the result count is announced. Clear filters and verify the full set returns.
4. Select Manipuri and Meitei (Manipuri) separately. Both should match the NDLI record whose source label uses Manipuri (Meitei).
5. Select Urdu and inspect the Diwan-e-Ghalib heading. The original title should be announced in Urdu context and read right-to-left; the English descriptor must remain left-to-right.
6. Open and close language-group details without a pointer.
7. Confirm every external source link has a distinguishable accessible name, including language-group source links.
8. Inspect the page in screen-reader browse mode. Verify heading levels are logical and each card's title/metadata/source action order is understandable.
9. Test 200% text resize and 400% zoom / 320 CSS-pixel equivalent. No two-axis scroll for ordinary text, no clipped filter labels or result actions.
10. Turn on forced colours/high contrast and reduced motion. Confirm focus and boundaries remain visible and all essential functionality works.
11. Check language/script headings for pronunciation, diacritics and reading direction. A machine language attribute cannot verify text quality.

## Record results

For each run, record tester's name/permission to name publicly, assistive technology and version, OS/browser version, device, viewport/zoom, exact actions, expected/actual, severity, evidence, remediation owner, and re-test date. Do not record personal health information or infer a tester's disability. Use a compensated tester where possible.


## Additional release checks for the 24 November 2026 candidate

- Verify the menu without JavaScript: at 820 CSS px and below, all six navigation destinations must remain visible and the non-functional Menu button must not be presented.
- Verify with JavaScript: toggle with Enter and Space, then use Tab/Shift+Tab through all six destinations; Escape closes and returns focus to Menu; clicking outside closes without stealing focus.
- Resize while the menu is open from mobile to desktop; the nav must return to its desktop layout and the button must report collapsed.
- Repeat at 820, 768, 600, 420, 390, 360 and 320 CSS px. Include landscape and text enlargement, not just viewport resizing.
- Confirm high-contrast and forced-colours modes retain visible boundaries and focus indicators.
- Inspect small metadata labels on both Day and Tonight themes. Automated CSS tokens are not a substitute for checking actual rendered text/background combinations.
- Complete the NVDA, VoiceOver and TalkBack sessions listed above. Record actual browser, OS, assistive-technology and device versions, results, and defects; do not infer human test completion from static tests.



## Latest automated checks · 24 November 2026

The expanded Chromium run passed on audited commit `817be3de1bc64c2c8686dcf0ad019f54964a61be`:
- 16 pages at 1440, 768, 390 and 320 CSS px (64 viewport checks).
- 12 keyboard navigation scenarios, including Escape focus restoration and outside-pointer closing.
- 16/16 mobile no-JavaScript navigation fallbacks.
- 4 forced-colours/reduced-motion preference scenarios.
- 12 automated 200% text-only resize emulations across four core routes at 768, 390 and 320 CSS px; zero horizontal overflow.
- Slow-network and service-worker offline-after-cache tests passed. Offline fallback rendered the offline support card with both approved support phone links.
- Lighthouse produced eight reports and scored 100 for Performance, Accessibility, Best Practices and SEO on all four key routes in mobile and desktop profiles.

Evidence: [workflow 45426136282](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45426136282), artifact [14934504814](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45426136282/artifacts/14934504814), and `docs/review/AUTOMATED_EVIDENCE_2026-11-24.md`.

**Human tests are still required:** run every environment in the matrix above; use actual 200% browser text resize and 400% zoom; test keyboard and focus on physical devices; verify airplane-mode use after a successful online visit and slow-network behavior on Android/iOS; inspect light and Tonight modes; and record tester, versions, actions, expected/actual behavior, defects and re-test. The automated 200% CSS emulation and Lighthouse score do not establish screen-reader usability or WCAG conformance.


## Latest candidate · 24 November 2026

- Preview: https://aaramora-platform-dpgflxktd-httpsgithubcomefigma54-devpp.vercel.app (READY, deployment `dpl_5xRBXxtuiBFWmFQfhvj19SLoyCC7`, commit `78213611bfee1816404d3733e3963a6fda943a6d`).
- Both push and pull-request content and browser workflows passed: content `45433039831` / `45433058356`; browser + Lighthouse `45433039789` / `45433058660`.
- 122 website/content/safety tests, 6 retrieval tests and 49-record catalogue validation passed. Preservation remains: 40 Relationship Corner concepts and nine Reading Library shelves.
- Browser: 64 responsive checks, 12 keyboard, 16 no-JavaScript, 4 preference-mode, 12 large-text reflow; zero page or visible internal overflow; slow-network and service-worker offline checks passed.
- Lighthouse: eight mobile/desktop reports, each scoring 100 for Performance, Accessibility, Best Practices and SEO. Artifact: [14940336195](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45433039789/artifacts/14940336195).
- Production deployment and stable domain unchanged. Real screen-reader, browser-zoom, physical-device, full-site human visual, clinician/safeguarding, native-language and cultural/religious reviews remain open.


## Latest support-language selector pass · 24 November 2026

The latest application-code commit is `c09080565d95782b2db31d15832bb52875b465ba`. Get Help now uses concise English / हिन्दी / मराठी selector labels, while retaining the clear unreviewed Hindi/Marathi draft notice. Pull-request content and browser/Lighthouse checks passed: [45435268537](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45435268537) and [45435268522](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45435268522). Eight Lighthouse reports are 100 across all four categories; expanded browser checks had zero page/internal text overflow. Artifact [14940817314](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45435268522/artifacts/14940817314). Latest READY preview: https://aaramora-platform-pvrg7rl5w-httpsgithubcomefigma54-devpp.vercel.app. Production stays unchanged; all real screen-reader/zoom/device and professional review gates remain open.
