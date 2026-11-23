# Deployment Status and Release Path

**Repository:** [ASHISHDAITH/aaramora-platform](https://github.com/ASHISHDAITH/aaramora-platform)  
**Last checked:** 24 November 2026  
**Current state:** GitHub source is committed; no live URL has been verified.

## What is already working
- The site is a static multi-page HTML/CSS/JS prototype with `index.html`, `wellbeing.html`, `relationships.html` and `reading-library.html`.
- The GitHub Actions content-check workflow is green: 18 Python tests passed on commit `4fe947eaeba87ac0dd4ad09683c8fda09402cf35`.
- No API keys, server, database or paid backend are needed to host the current prototype as a static site.

## Vercel connection blocker
The connected Vercel Hobby workspace currently lists other Git-linked projects, but not this repository. The attempt to look up and create a Git-linked project for `ASHISHDAITH/aaramora-platform` returned HTTP 403 Forbidden. No Vercel project or deployment was created.

This is an account/repository authorization issue, not a website build error. The repository must be made accessible to the Vercel GitHub App / connected GitHub identity.

## Recommended deployment route: Git-connected Vercel project
1. Open [Vercel New Project](https://vercel.com/new/import).
2. Sign in to the Vercel Hobby workspace.
3. If `ASHISHDAITH/aaramora-platform` is not listed, install or update the Vercel GitHub App so it has access to this repository, and confirm the correct GitHub account is connected to Vercel.
4. Import `ASHISHDAITH/aaramora-platform` from `main`.
5. Treat it as a static site / Other framework. The repository root contains `index.html`; there is no npm build or install step required for the prototype.
6. Deploy, then verify all four routes, media requests, mobile navigation and no unexpected network calls.
7. Keep the generated production URL and confirm a new push to `main` creates an automatic deployment.

Vercel describes the repository-import route as the way to keep a stable project URL with automatic deployment on future Git pushes. See [Vercel project import](https://vercel.com/new/import).

## Temporary alternative: Vercel Drop
[Vercel Drop](https://vercel.com/drop) can publish a static folder or ZIP directly on the Hobby plan. It creates a new project for each drop; re-dropping does not update the same project URL. Use this only as a one-off preview, then connect the Git repository for ongoing updates. See [Vercel Drop overview](https://vercel.com/changelog/vercel-drop) and [Vercel's static-site deployment options](https://vercel.com/i/deploy-to-vercel-without-git).

## Binary media still missing from Git
`docs/AARAMORA_BRAND_FILM_ASSETS.md` records the two approved MP4 export paths and checksums. The current working session does not contain the MP4 binaries, and the available GitHub connector only writes UTF-8 text files. Add the two unique files from the original local exports before enabling the homepage brand-film video. Do not upload the duplicate file labelled “clean/no added audio”; the manifest records that it matches the landscape master and contains AAC audio.

## Production release gates
A successful static deploy does not make the platform clinically approved. Before public launch:
- clinician review of all mental-health and women's-health copy;
- safeguarding review of relationship content and the safety flow;
- native-language review of Hindi and Marathi content;
- keyboard, screen-reader, mobile, low-bandwidth and WCAG 2.2 AA checks;
- privacy/security review and deployed network-traffic inspection;
- current verification of Tele-MANAS, emergency and women’s helpline details;
- explicit ownership and review dates for every public resource.
