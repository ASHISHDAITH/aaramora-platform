# Deployment Status and Release Path

**Repository:** [ASHISHDAITH/aaramora-platform](https://github.com/ASHISHDAITH/aaramora-platform)  
**Production URL:** https://aaramora-platform.vercel.app  
**Vercel project:** `aaramora-platform` (`prj_VzSl28VokjdmWzbCHjKvu7ZGgyGA`)  
**Latest deployment:** `dpl_E45batFEw39PSg1GKyBkN5gQZRb3`  
**Status:** READY · production · stable alias assigned

## Current release

A public static deployment has been created in the Vercel Hobby workspace. Vercel reports the deployment as READY and assigned the stable `aaramora-platform.vercel.app` alias.

The latest deployment is a static snapshot of commit `a41820fa9bff38eab31054232267242fcbdb8c00` on `main`. It contains:
- `index.html` — simplified navigation, shorter hero copy and the 16:9 brand film in the hero
- `wellbeing.html`
- `relationships.html`
- `check-ins.html`
- `reading-library.html`
- `assets/healing-garden.svg`
- `assets/safe-corner.svg`
- `assets/thought-river.svg`

The brand-film MP4s are committed in GitHub under `assets/brand-film/`. The homepage now shows five common navigation destinations and groups the remaining destinations under “More”; all original links, sections and tools are retained. It uses shorter hero copy and places the 16:9 master in the hero, with the 9:16 version as a separate link. Video playback is user-initiated; it does not autoplay.

The Reading Library now contains nine subject shelves and 23 linked catalogue cards spanning open mental-health workbooks, academic books, relationship learning, Hindu/Sikh/Islamic/Christian/Buddhist/Jain texts, regional-language literature, public-domain classics and GitHub discovery indexes. Its search filters rendered cards in the browser only; it sends no search query to a server and stores no search history. The hero uses a credited Pexels still-life image with an original AARAMORA reading note. It links to source institutions rather than copying third-party books or restricted texts.

The Vercel deployment was created directly from the listed source files because Git repository integration was blocked. The project has Vercel SSO/password deployment protection disabled so the public static site can be visited without membership in the Vercel workspace.

## Remaining Git integration step

The connected Vercel GitHub identity returned `repo_no_access` when linking `ASHISHDAITH/aaramora-platform`, saying it needs admin or write access. GitHub confirms the repository is public and the signed-in GitHub connector can push, but Vercel's connected GitHub App/identity does not currently have the needed access.

Until that is fixed, **new pushes to `main` will not automatically update the live site**. To enable automatic deployments:

1. Open [Vercel project settings](https://vercel.com/httpsgithubcomefigma54-devpp/aaramora-platform/settings/git).
2. In GitHub, install or update the Vercel GitHub App for the account that owns `ASHISHDAITH/aaramora-platform`, and grant it access to this repository.
3. In Vercel, connect the repository to this existing project. Keep the root directory at `./`; this is a static HTML project with no package install or build command.
4. Push a small reviewed commit and confirm Vercel creates a new production deployment automatically.

Do not create another Vercel project just to retry the connection; the current project already owns the production alias.

## Verification notes

- Vercel's deployment API reports `READY`, `target=production`, the stable `aaramora-platform.vercel.app` alias, and `aliasError=null` for deployment `dpl_E45batFEw39PSg1GKyBkN5gQZRb3`.
- Vercel's source-file listing confirms all eight expected HTML/SVG files are present, including `check-ins.html` and the expanded `reading-library.html`.
- The web-fetch/browser environment could not retrieve the new Vercel page, so a full visitor-side browser smoke test remains pending. The deployment API and source-file tree are verified, but do not substitute for opening the page as a visitor. Test all five routes, all nine library section links, search on several sample terms, mobile layout, the Pexels image and brand-film playback in a regular browser.
- Confirm the video CDN returns the complete MP4s in a regular browser and check browser developer tools for failed requests before announcing the site publicly.

## No backend or health-data collection

The current website is a static information/help-navigation prototype. No API keys, database, accounts, server-side journal storage, analytics or AI service are required for this deployment. Do not add forms that collect private health details without a separate privacy/security review.

## Production release gates

A successful static deployment does not mean the platform is clinically approved. Before promoting the site as a health service:
- clinician review of all mental-health and women's-health copy;
- safeguarding review of relationship content and the safety flow;
- native-language review of Hindi and Marathi content;
- keyboard, screen-reader, mobile, low-bandwidth and WCAG 2.2 AA checks;
- privacy/security review and deployed network-traffic inspection;
- current verification of Tele-MANAS, emergency and women's helpline details;
- explicit ownership and review dates for every public resource.

Keep the public description clear: AARAMORA is an information and help-navigation prototype, not therapy, diagnosis, prescribing or an emergency response service.


## Check-ins page

The `check-ins.html` page is included in the current production deployment. It contains the non-diagnostic guide finder, women's-health appointment/print planner and original blank two-cycle symptom log. The latest deployment's Vercel source file listing confirms the page is present. The route should still be checked in a regular browser as part of the visitor-side smoke test.

