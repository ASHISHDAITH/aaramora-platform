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
