# Deployment Status and Release Path

**Repository:** [ASHISHDAITH/aaramora-platform](https://github.com/ASHISHDAITH/aaramora-platform)  
**Production URL:** https://aaramora-platform.vercel.app  
**Vercel project:** `aaramora-platform` (`prj_VzSl28VokjdmWzbCHjKvu7ZGgyGA`)  
**Latest deployment:** `dpl_Fqfdf9uht4kjBwMnZAaPJ6WkSSjX`  
**Status:** READY · production · stable alias assigned

## Current release

A public static deployment has been created in the Vercel Hobby workspace. Vercel reports the deployment as READY and assigned the stable `aaramora-platform.vercel.app` alias.

The refreshed deployment is a static snapshot of commit `3aef65fdc1f56bc3d9803ac7843ea275910f595e` on `main`. It contains:
- `index.html`
- `wellbeing.html`
- `relationships.html`
- `reading-library.html`
- `assets/healing-garden.svg`
- `assets/safe-corner.svg`
- `assets/thought-river.svg`

The brand-film MP4s are committed in GitHub under `assets/brand-film/`. The refreshed homepage places the 16:9 master in the hero and references it through jsDelivr's GitHub CDN. The 9:16 version remains a separate link. Video playback is user-initiated; it does not autoplay. Three image-led pathway cards use free-to-use Pexels stock photography, with creator/source credits and descriptive alt text; those image requests are served externally by Pexels.

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

- Vercel's deployment API reports `READY`, `target=production`, the stable `aaramora-platform.vercel.app` alias, and `aliasError=null`.
- Vercel's source-file listing confirms all seven expected HTML/SVG files are present in the deployment.
- The external browser-fetch tools in the execution environment could not retrieve the Vercel or Pexels image hosts, so an independent visitor-side browser smoke test remains pending. Open the production URL in a regular browser and test each route, internal navigation, mobile layout, image loading, video playback and the vertical-film link.
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


## Check-in page update — committed, not yet deployed
The fifth static page, `check-ins.html`, and its research/specification files are committed to GitHub main at commit `a311edb4d60888e0b82ead814113a734d18811e7`. It contains a non-diagnostic guide finder, women's-health appointment/print planner and original blank two-cycle symptom log. GitHub Actions passed 21 tests, including the new page's inline JavaScript syntax check.

The currently verified Vercel production snapshot remains commit `3aef65fdc1f56bc3d9803ac7843ea275910f595e` and does not contain the new page. An attempt to refresh the existing production project through the connected Vercel deployment API returned HTTP 403 Forbidden; the Vercel sandbox-session API also returned 403. No deployment was created by these attempts. Do not announce `/check-ins.html` as live until Vercel shows a newer READY deployment and the route is tested in a regular browser.

To publish manually from a local clone after GitHub access is available: pull the current `main`, link the local repository to the existing Vercel project with `vercel link --project aaramora-platform --scope httpsgithubcomefigma54-devpp`, then run `vercel deploy --prod`. Confirm the resulting deployment is READY and that `/check-ins` is accessible. GitHub automatic deployments require the Vercel GitHub App to have access to the repository.
