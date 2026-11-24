# AARAMORA Deployment and Release Status

**Repository:** [ASHISHDAITH/aaramora-platform](https://github.com/ASHISHDAITH/aaramora-platform)  
**Production URL:** https://aaramora-platform.vercel.app  
**Vercel project:** `aaramora-platform` · `prj_VzSl28VokjdmWzbCHjKvu7ZGgyGA`  
**Last updated:** 24 November 2026

## Current production deployment

- **Deployment:** `dpl_6q1FeVVVNZjicfRNmH23pnxcrwbm`
- **Source commit:** `b7a830a571ef0809048753431f42aa2c61debef1` on `main`
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

- GitHub content checks: [run 45388240891](https://github.com/ASHISHDAITH/aaramora-platform/actions/runs/45388240891) — **success**.
- Python test suite: **85 tests passed**.
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

These current branch changes must pass CI and then receive a fresh production deployment. The earlier deployment ID below identifies the preceding site build, not these newer changes.
