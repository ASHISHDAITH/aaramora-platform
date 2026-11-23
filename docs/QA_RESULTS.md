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
