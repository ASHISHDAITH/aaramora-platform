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
- Initial CI run `45263329157` failed one assertion because the test expected “not statistically significant” while the page correctly said “statistically non-significant”.
- The assertion was corrected and the relationship test expanded to check all 40 concept cards and all three optional reflections.
- Latest CI run: [45266028057](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45266028057), commit `4fe947eaeba87ac0dd4ad09683c8fda09402cf35`, conclusion **success**.
- Result: **18 tests passed**. The workflow runs on push, pull request and manual `workflow_dispatch`.

### Deployment
- No live Aaramora deployment has been verified.
- The connected Vercel Hobby team does not currently list a project linked to `ASHISHDAITH/aaramora-platform`.
- Vercel project lookup/creation through the connected account returned HTTP 403 Forbidden. No project or deployment was created.
- A Vercel GitHub App authorization for this repository, or a user-completed import from the Vercel dashboard, is still required. See `docs/DEPLOYMENT.md`.

### Brand-film binary uploads
- The export manifest is committed, but the two unique MP4 binaries are not in the Git repository.
- The current task workspace did not contain the MP4 files, and the available GitHub write connector supports UTF-8 text rather than direct binary uploads.
- Add the two unique exports from the original local files when available. The duplicate “clean/no added audio” file must not be treated as silent; the manifest records that it is byte-identical to the master and contains AAC audio.

### Remaining release gates
The checks above do not complete the following:
- Browser interaction and visual audit on real Android and iOS devices.
- Keyboard-only and screen-reader tests with NVDA, VoiceOver and TalkBack.
- Formal WCAG 2.2 AA audit for each page, language and state.
- Native-speaker review of English/Hindi/Marathi/Romanised Hindi content as appropriate.
- Qualified clinical review of mental-health, women's-health and crisis copy.
- Safeguarding specialist review of relationship content and safety routing.
- Lived-experience co-design and usability sessions.
- Production privacy/security review and deployed network-traffic verification.
- Final official verification of helplines and referral coverage immediately before launch.


### Inline JavaScript validation added — 24 November 2026
- Added an automated check that extracts each inline JavaScript block from `index.html`, `wellbeing.html`, `relationships.html` and `reading-library.html`, then runs Node.js `--check`.
- GitHub Actions run [45266854917](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45266854917), commit `43483cadf081ffe7e630287ca2fd87faa27da95d`, completed successfully.
- Result: **19 tests passed** (`Ran 19 tests`, `OK`), including the all-pages inline JavaScript syntax check.


## Quiz and self-check research — 24 November 2026
- Added `docs/QUIZ_AND_SELF_CHECK_RESEARCH.md` covering PHQ-9/GAD-7, EPDS, regional validation research, PMOS/PCOS screening guidance, PMDD prospective diaries, endometriosis symptom logs, menopause instrument permissions, adult attachment measures and self-harm risk-score cautions.
- Added `check-ins.html`: optional non-scored guide finder, women's-health appointment preparation and an original blank two-cycle paper log.
- Added `docs/CHECKIN_TOOL_SPEC.md` and linked the page from homepage, mental-wellbeing and relationship navigation.
- The current page does not score clinical instruments, diagnose, assign labels, store answers or send data.
- The new static tests cover optional controls, privacy, support links, print layout, internal anchors and inline JavaScript syntax on all five pages. CI result is pending.
- This is educational UX, not clinical approval. Qualified clinical, safeguarding, language and accessibility review remain required.
