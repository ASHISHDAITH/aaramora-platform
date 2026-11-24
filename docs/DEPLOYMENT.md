# AARAMORA Deployment and Release Status

**Repository:** [ASHISHDAITH/aaramora-platform](https://github.com/ASHISHDAITH/aaramora-platform)  
**Production URL:** https://aaramora-platform.vercel.app  
**Vercel project:** `aaramora-platform` · `prj_VzSl28VokjdmWzbCHjKvu7ZGgyGA`  
**Last updated:** 24 November 2026

## Current production deployment

- **Deployment:** `dpl_3joScLaijXWdRndiNcBw48itcvJc`
- **Source commit:** `73c49f4182ef6befc37a8b760090acbccec1ebea` on `main`
- **State:** READY · target production
- **Stable alias:** `aaramora-platform.vercel.app`
- **Alias error:** none reported by Vercel.

The Vercel deployment record confirms build readiness and the stable `aaramora-platform.vercel.app` alias is assigned to this deployment. It is not a substitute for manual browser, screen-reader, device, low-bandwidth or clinician review. The web preview fetch in this run could not retrieve page HTML, so no fresh manual live-browser audit is claimed here.

## Current site release

The homepage has five sections and four primary navigation destinations: Get help now, Understand, Tools and Trust. The Sandhya palette uses an opaque paper header and turmeric Kiran light. Original first-party SVG illustrations replace the homepage stock-image requests; versioned brand-film files are served from the repository.

The site includes:
- Get Help page with only Tele-MANAS 14416 and Emergency 112; both show source-check dates.
- Persistent postpartum psychosis emergency warning.
- Pune Access Map with 25 official-page-listed service entries across 10 facilities. It is a directory, not an endorsement or live capacity/quality check.
- Tonight mode, browser-only Safety Plan worksheet, Words Library and printable Appointment Bridge.
- Separate draft Women's Health and Research pages; neither is clinician-approved.
- First-party offline cache for the support page after a first online visit.
- Sitemap, robots.txt, favicon, manifest, Open Graph/Twitter metadata and noindex on draft/utility routes.

No analytics, advertising trackers, server-side health forms, public community, model endpoint or chatbot UI is enabled.

## Latest automated checks

- GitHub content checks: [run 45391042468](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45388240891) — **success**.
- Python test suite: **97 website/content tests and 6 retrieval-only tests passed**.
- Default-deny corpus build: **0 approved RAG entries**, 0 exclusions, LLM disabled.
- Reading Library catalogue validator: completed successfully in the same workflow.
- Official support-source workflow: [run 45387267894](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45387267894) — **success**. It checked three official source URLs: 2 reachable, 0 confirmed dead, 1 inconclusive. The inconclusive result is not treated as evidence that the service is unavailable.
- Support-register tests enforce exactly two public national contacts: 14416 and 112.

## Chatbot / RAG release hold

The AARAMORA Guide is a future feature and remains **disabled**. No model API, inference endpoint, persistent chat log, transcript store or public chat widget is configured.

The prompt v2 and English crisis-response template are review drafts only. The corpus manifest and approved index are empty. The corpus builder is local/offline and only indexes content with named reviewers, current approval, dates, sources and explicit exact-item rights verification. Link-only sources are not ingested.

The current 100-case Hinglish starter set is synthetic and structurally tested in CI. It has **not** been run against an LLM, classifier or deployed safety router. The original RAG design report requires a 300+ multilingual crisis benchmark across English, Hindi, Marathi and Hinglish, plus clinician/safeguarding sign-off before real-user access.

### Remaining launch gates

- Named clinical lead, safeguarding reviewer and engineering owner.
- Written, version-specific clinician and safeguarding approval of the prompt and fixed crisis response.
- Native-language review and clinician approval for Hindi/Marathi crisis text.
- 300+ multilingual crisis benchmark and actual detector evaluation, including review of false negatives.
- Groundedness, abstention, prompt-injection, privacy, PII redaction and JSON validation tests against the exact selected implementation.
- Provider retention/training/region review before any future model call.
- Rate limits, kill switch, incident handling and clear no-live-monitoring disclosure.
- Manual keyboard, screen-reader, zoom, slow-network and human accessibility checks for the current site.

No chatbot beta or public deployment should be enabled until these gates are completed and recorded.


## Latest source updates after the previous production build

The repository now includes:
- Hero-contained quick choices before the film link (four top-level homepage sections).
- Consistent “Was this helpful? Report a problem” email-draft links. The links have no tracking, but no public recipient address is configured.
- Local lexical retrieval-only Phase 2: `scripts/search_reviewed_corpus.py`, with source links and safe abstention. Current approved index remains empty.
- A 301-case synthetic crisis fixture pack across English, Hindi, Marathi and Hinglish. All language/clinical labels are pending human review; it has not been run against a model or detector.

The changes described in this release record are present in `main` at `73c49f4182ef6befc37a8b760090acbccec1ebea` and are included in the READY production deployment above.


## Final release record · 24 November 2026

- **Source commit on main:** `73c49f4182ef6befc37a8b760090acbccec1ebea`.
- **Vercel production deployment:** `dpl_3joScLaijXWdRndiNcBw48itcvJc` · READY.
- **Stable alias:** [https://aaramora-platform.vercel.app](https://aaramora-platform.vercel.app). Vercel lists this alias on the deployment and reports no alias error.
- **GitHub content-check workflow:** [run 45391042468](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45391042468) · success.
- **Automated validation:** 97 website/content/safety tests, 6 local lexical retrieval tests and the 49-entry Reading Library catalogue validator passed.
- **Multilingual crisis fixtures:** 301 synthetic records (67 English, 67 Hindi, 67 Marathi and 100 Hinglish). The tests check fixture structure/counts only; no live detector, classifier or model was evaluated.
- **Pune Access Map:** 25 source-listed service entries across 10 facilities. The directory does not establish live availability, eligibility, fees, service quality or appointment capacity.
- **Support policy:** the public register and pages show only Tele-MANAS 14416 and Emergency 112, each with an official-source check date. Named human sign-off remains pending.
- **RAG:** runtime and model calls remain disabled; the approved corpus is empty and retrieval abstains when no approved passages exist.
- **Manual release gates still open:** fresh live browser inspection of every route, screen-reader/manual keyboard testing, 200% text and 400% zoom/reflow, slow-network/offline device testing and Lighthouse recording for this exact deployment. Prior local Chromium/axe checks are recorded above but do not replace a new full-site review.
- **Human sign-off still open:** clinician, safeguarding, Hindi/Marathi native-language, cultural/religious and independent accessibility review. No automated test or source check is treated as such sign-off.

Vercel's READY state and the matching commit prove deployment/build status, not clinical or WCAG conformance.


## Additive discovery and navigation release · 24 November 2026

- **Production source commit:** `7da5fda5c648ac25477684e9996324e472791385`
- **Vercel production deployment:** `dpl_EwEu3vXSSvSS8J6wQqNEX6JLduxE` · READY
- **Stable alias:** https://aaramora-platform.vercel.app
- **GitHub content-check:** [run 45410648378](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45410648378) · success
- **Automated checks:** 109 website/content/safety tests passed; 6 local lexical retrieval tests passed; 49-record multilingual catalogue validator passed.
- **Navigation:** six shared destinations on all menu-bearing pages. Mobile menu toggles, Escape closes it, outside clicks close it, expanded state is announced, and the active destination is identified.
- **Homepage:** existing four sections and original pathways remain. Added Relationship Corner and Reading Library discovery cards inside the existing pathways area.
- **Relationship Corner:** 40 concept entries and existing reflection/quiz content retained.
- **Reading Library:** 49 catalogue records and all nine original shelves retained. Format filters expose Book, Video, Audiobook, Audio, Article, Blog and Image counts. Counts overlap because records can have multiple formats.
- **Other public data:** Pune Access Map remains 25 provider/government service entries across 10 facilities. It does not confirm live appointments, eligibility, fees or service quality.
- **Support contacts:** public pages show only Tele-MANAS 14416 and Emergency 112. Named human sign-off remains pending.
- **Privacy/safety:** the site remains static and account-free; personal worksheet content is not sent to AARAMORA servers. RAG approved index remains empty and LLM calls disabled.
- **Live smoke checks:** homepage, Relationship Corner, Reading Library, support, wellbeing, Access Map, Tools, Trust, privacy, women’s-health draft, research draft and community concept pages returned HTTP 200. The catalogue JSON, Pune data, shared JS/CSS, service worker, favicon, manifest, original SVG illustrations and pinned film also returned HTTP 200.
- **Live preservation checks:** 40 relationship concepts; nine original Reading Library shelves; 49 catalogue records; 25 Pune service entries and 10 facilities.
- **Open manual gates:** no fresh whole-site visual browser audit, screen-reader run by a human, 200%/400% zoom session, slow-network/offline device test or Lighthouse report is claimed for this release. Clinician, safeguarding, Hindi/Marathi native-language, cultural/religious and independent assistive-technology reviews remain pending.

This is an additive quality release. No original page, relationship concept, reading-library shelf, catalogue record, support route or media file was intentionally deleted.
