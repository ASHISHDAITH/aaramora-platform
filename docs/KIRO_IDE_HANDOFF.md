# Kiro IDE — AARAMORA project handoff

**Status:** Development-environment handoff prepared on 24 November 2026.  
**Primary IDE:** Kiro.  
**Repository:** https://github.com/ASHISHDAITH/aaramora-platform  
**Production:** https://aaramora-platform.vercel.app  
**Project memory:** `brain.md` (read this first).

## Purpose

Continue the existing AARAMORA project in Kiro without replacing its architecture, removing content or changing its safety posture. Kiro is the coding environment; GitHub remains the source of truth; Vercel remains the production host.

This is not a framework migration. The current site is a static HTML/CSS/JavaScript project. Do not scaffold a new app, convert frameworks, introduce a backend or rebuild page routes as part of IDE setup.

## Mandatory reading order

Before making changes, read:

1. `brain.md`
2. `SAFETY.md`
3. `README.md`
4. `CONTRIBUTING.md`
5. The exact feature specification and relevant test files for the requested work.

Use `docs/DEPLOYMENT.md`, `docs/QA_CHECKLIST.md`, `docs/QA_RESULTS.md`, `docs/VALIDATION_NOTES.md`, `docs/review/ACCESSIBILITY_MANUAL_TEST_PLAN.md`, and `docs/RAG_CHATBOT_IMPLEMENTATION.md` where relevant.

## Preservation contract

Never remove or replace existing material just to simplify implementation. Preserve:

- Every existing page, route, section, content item, feature, interaction and original design asset.
- Six navigation destinations: Get help now, Understand, Tools, Relationship Corner, Reading Library and Trust.
- Responsive menu behavior, Escape close, outside-click close, accessible expanded-state announcement, active destination and Quick Exit.
- Four original homepage sections and original pathways, plus both discovery cards.
- 40 Relationship Corner concepts and their existing guides, quizzes, reflections and safety content.
- 49 Reading Library catalogue records and all nine original shelves. Preserve source URLs, rights notes, attribution and review status. There are seven format filters; counts overlap when a record supports multiple formats.
- Pune Access Map's 25 service entries across 10 facilities.
- All current media, brand film, CSS, JavaScript, service worker, data, tests, scripts, workflows and documentation.

Before and after each task, verify these counts and inspect the Git diff for accidental deletions.

## Product and safety boundaries

AARAMORA is an information and human-help-navigation website. It is not therapy, diagnosis, prescribing, telemedicine, emergency dispatch or an AI companion. Do not claim clinical outcomes.

The only current national support routes permitted in public UI are:
- Tele-MANAS: **14416**
- Emergency Response Support System: **112**

Do not add a different number without named human verification of the official source, coverage and current access, and recorded approval in `data/service-links.json`.

No partner surveillance, tracking, coercion, manipulation or relationship verdicts. Respect no-contact and requests for space. Do not claim Quick Exit erases browser history, network logs or shared-device activity.

The future AARAMORA Guide/RAG is disabled. No chatbot, model endpoint, LLM calls, accounts, transcript storage, long-term memory or server-side health data may be enabled unless all documented safety, clinical, safeguarding, privacy, language and engineering release gates are completed and the user explicitly approves.

Do not scrape, mass-download, bypass DRM, paywalls or library-borrowing restrictions. A public link or repository licence does not automatically grant reuse rights for every bundled item.

## Kiro session workflow

1. Inspect `git status`, branch and latest commit. Never discard uncommitted user work.
2. Run baseline checks before edits.
3. Write a short plan and list expected changed files.
4. Make focused, additive and reversible edits. Prefer small patches to full-file replacements.
5. Keep semantic HTML, responsive behavior, keyboard support, reduced-motion preferences and visible focus states.
6. Add/update regression tests for each meaningful defect.
7. Run focused checks, then the full suite and catalogue validator.
8. Review changes for accidental deletion, weakened safety copy, unverified facts, rights violations, external dependencies, privacy regressions and broken internal/external links.
9. Update `brain.md` and relevant documentation in the same change.
10. Commit and push only after reviewing the complete diff.
11. Deploy only as a deliberate release step. A pushed commit or green CI is not proof that Vercel production has changed.
12. After deployment, verify the deployment is READY, confirm the deployed commit, and smoke-test the live site before calling the change live.

Never force-push or use destructive Git commands as a shortcut. Use a backup branch before a broad change set.

## Local preview and checks

This is a static website and does not need an npm install or app build for the current baseline.

Start a local server from the repository root:

```bash
python -m http.server 8000
```

Then open http://localhost:8000.

Run the current Python test suite:

```bash
python -m unittest discover -s tests -p 'check_*.py' -v
```

Run catalogue validation:

```bash
python scripts/check_catalogue.py
```

For relevant changes, also run the matching service-link, library-link, retrieval and JavaScript syntax checks. Confirm exact commands from the current workflows and scripts. Do not invent a build pipeline.

## Quality bar

Aim for a high-quality, calm, distinctive, accessible and fast experience. Do not use visual novelty at the expense of clarity, safety or trust. Avoid forced disclosure, engagement loops, fake testimonials, surprise motion, autoplay, unnecessary animation and decorative UI that competes with urgent support actions.

Open quality gates that must remain visible until actual evidence is recorded:

- Fresh visual review at desktop, tablet and small mobile widths.
- Human NVDA, VoiceOver and TalkBack testing.
- 200% text enlargement and 400% zoom/reflow.
- Slow-network and real-device offline tests.
- Current Lighthouse performance and accessibility reports.
- Qualified clinical and safeguarding review.
- Hindi/Marathi native-speaker and clinical review.
- Religious/cultural-context review.
- Named human review of exact helpline source and copy.

Automated tests, axe results from an earlier build and Vercel READY status do not certify the current release or close human review gates. Do not claim WCAG 2.2 AA certification without a full, current audit.

## First work session in Kiro

1. Open the existing cloned repository folder. Do not start from a blank scaffold.
2. Read the mandatory documents above.
3. Verify branch and working tree.
4. Run baseline tests and catalogue validation; save the output in the working notes.
5. Inspect the site at desktop, tablet and small mobile widths.
6. Make a prioritized defect list without removing or rewriting existing pages or content.
7. Fix one small set at a time and add regression tests.
8. Confirm the preservation counts and public support routes.
9. Review the full diff, update docs, push, verify CI and perform a separately approved Vercel deployment.

## Kiro agent instruction block

Paste this into Kiro's project steering/instructions if you configure one:

> You are the senior engineer maintaining AARAMORA. Read `brain.md`, `SAFETY.md`, `README.md`, `CONTRIBUTING.md` and the relevant feature docs before acting. Work in the existing static HTML/CSS/JavaScript repository. Enhance existing work; do not rebuild, scaffold a new framework, delete pages, remove sections, prune content, replace the design wholesale or add a backend. Preserve all routes, assets, original homepage sections, six navigation destinations, 40 relationship concepts, 49 catalogue records, nine Reading Library shelves, 25 Pune directory entries across 10 facilities, all source/rights notes and existing tests. Public national support numbers are exactly 14416 and 112 unless a named human reviewer approves a documented change. Keep the chatbot/RAG disabled, retrieval corpus empty and no model calls, analytics, accounts or server-side health data. Never invent clinical claims or mark human reviews complete without written sign-off. Make small, additive, reversible changes; add regression tests; run the full test suite and catalogue validator; inspect the entire Git diff; update `brain.md` and relevant docs. Do not force-push or deploy automatically. Production deployment must be deliberate and verified against the exact commit. Your goal is a more polished, clear, accessible, performant and trustworthy AARAMORA while preserving everything that works.

## Handoff integrity

This guide records the intended Kiro workflow. It does not claim that Kiro has already opened the local checkout or executed tests. The next session must inspect the actual local repository state before making changes.
