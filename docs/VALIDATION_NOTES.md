# Prototype Validation Notes

Date: 30 October 2026

Checks completed on the static HTML prototype:
- HTML parser completed without errors.
- All internal `#anchor` links resolve to an element ID.
- Inline JavaScript passed `node --check`.
- No external scripts, images, fonts, stylesheets or iframe assets are loaded.
- Contrast calculations for key pairs: forest text on paper 10.82:1; muted text on paper 5.08:1; white text on forest 10.18:1; pale support copy on forest 7.46:1; focus blue on paper 6.00:1.
- The muted text token meets 4.5:1 on paper; visual component states still need a complete contrast audit.

Not yet completed:
- Browser layout review across real mobile/desktop devices.
- Keyboard-only, NVDA, VoiceOver and TalkBack testing.
- Formal WCAG 2.2 AA audit.
- Native-speaker review of Hindi/Marathi strings.
- Clinician review of health or crisis copy.
- Paid co-design / usability sessions with lived-experience participants.
- Final official verification of all helpline service details before launch.

The prototype is static and contains no backend, analytics, AI inference, form submission or persistence. Do not present it as production-ready.


## Women's Health update validation (23 November 2026)
- Added a dedicated Women's Health section and navigation route.
- Added eight topic cards and expandable information groups.
- Added evidence interpretation for PMOS and midlife cognitive outcomes.
- Added a claim-check panel for viral hormone-balancing statements.
- Added appointment preparation topics and source links.
- All health copy remains an unapproved draft pending clinical and language review.

- HTML parser: passed.
- Women's Health section and homepage / footer links: present; all internal anchors resolve.
- Eight topic cards: present.
- Inline JavaScript: passed `node --check`.
- No third-party script, font, image, stylesheet or iframe dependency.
- Selected contrast checks: forest text on paper 10.82:1; muted text on paper 5.08:1; white on forest 10.18:1; card text on warm white 6.39:1.
- Browser/device, screen-reader, clinician and native-speaker tests remain outstanding.