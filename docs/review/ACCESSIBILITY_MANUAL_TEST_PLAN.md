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
