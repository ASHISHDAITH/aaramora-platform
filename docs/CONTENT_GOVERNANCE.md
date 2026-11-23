# AARAMORA content governance

**Status:** Governance framework drafted; named clinical lead and safeguarding lead are not yet assigned.  
**Last source review:** 24 November 2026  
**Next scheduled source check:** 24 December 2026

## Ownership and approval

| Role | Required responsibility | Current status |
|---|---|---|
| Product/content owner | Page owner, version, sources and expiry tracking | Project owner not named in public site |
| Clinical lead | Approve mental-health claims, exercises, crisis wording and referral logic; may pause any page | **Unassigned** |
| Yoga professional | Approve yoga movement, breath, guided-rest scripts and audio | **Unassigned** |
| Safeguarding reviewer | Review self-harm, violence, coercion, privacy and escalation wording | **Unassigned** |
| Hindi reviewer | Natural Hindi, dialect, accessibility and pronunciation review | **Unassigned** |
| Marathi reviewer | Natural Marathi, regional fit, accessibility and pronunciation review | **Unassigned** |
| Lived-experience reviewers | Paid participation throughout design and evaluation, with opt-out and safeguarding | **Not yet recruited / documented** |

No page should be described as clinically approved until a named reviewer has signed a specific version and the review date is recorded. A reviewer may request a correction or pause at any time.

## Page-level review record

Each health or safety page should display:
- Last source verification date.
- Next scheduled review date.
- Review status (source-check only / clinical review pending / approved version number).
- Named clinical reviewer and role after approval.
- Content owner and correction route.

A source check is not clinical approval. A static website build succeeding is not a health-content sign-off.

## Correction log

The public correction log is maintained in [CORRECTIONS_LOG.md](CORRECTIONS_LOG.md). Do not include visitor names, health details, crisis narratives or other personal data in public issue threads or public logs. The repository currently has no private clinical escalation/contact channel; establish one before inviting users to submit sensitive reports.

## Link freshness

Critical service links are registered in `data/service-links.json` with:
- source organisation and official source URL;
- visible service number;
- last verification date and next review date;
- named editorial owner (to be assigned);
- a non-invasive HTTP link check that does not retrieve content bodies.

The weekly GitHub Actions workflow `.github/workflows/service-links.yml` checks the official-source URLs for Tele-MANAS, ERSS 112 and Women Helpline 181. It treats 404/410 as confirmed dead links; 403, 405, 429, timeouts and other restrictions are inconclusive and require human review, not automatic deletion. The separate `reading-library-link-check.yml` workflow checks reading-catalogue metadata links only. Neither workflow downloads books or changes displayed numbers automatically.

## Crisis and suicide-related communication

- Follow WHO's *Preventing suicide: a resource for media professionals, update 2023*: https://www.who.int/publications/i/item/9789240076846
- Follow Samaritans' guidance for online and public reporting: https://www.samaritans.org/about-samaritans/media-guidelines/media-guidelines-reporting-suicide/
- Do not include methods, locations, graphic detail, sensational framing, glamorisation or simplistic causal narratives.
- Avoid presenting suicide as inevitable, romantic, a solution, or the result of one event.
- Use non-judgemental language, emphasise survival, recovery and routes to human help, and place relevant help details near the content.
- Any copy describing self-harm or suicide requires clinical and safeguarding review before publication.

## Motivation and user agency

Use self-determination theory as a design reference, not a treatment claim:
- **Autonomy:** the visitor chooses, skips, pauses or exits.
- **Competence:** instructions are clear, achievable and allow small steps without streaks, scores or guilt.
- **Relatedness:** connection and human support are visible, not replaced by an automated companion.

Primary source: Deci & Ryan (2000), *The “What” and “Why” of Goal Pursuits: Human Needs and the Self-Determination of Behavior*, https://doi.org/10.1207/S15327965PLI1104_01

## Cultural practice and consultation

Te Whare Tapa Whā is a Māori health model developed by Tā Mason Durie. It is culturally situated and should not be copied as a decorative four-card motif or relabelled as a universal AARAMORA model without Māori-informed collaboration, attribution and review. It may be linked as an educational source with its context intact: https://www.health.govt.nz/maori-health/maori-health-models/te-whare-tapa-wha

For Indian traditions and local languages, commission native-language and culturally informed review rather than relying on automated translation alone. Sacred quotations and translations need edition-level source and rights checks.

## Performance and privacy gates

Before public pilot:
- Run Lighthouse on mobile and desktop; target 95+ where feasible, record actual scores rather than promises.
- Keep first-party HTML and assets lean; measure each page and first-load transfer.
- Verify the site works offline only if an offline mode is explicitly implemented and tested; do not claim offline support before then.
- No third-party trackers, advertising pixels or analytics on sensitive pages.
- Inspect network requests and verify all media are either self-hosted or explicitly disclosed.
- Review CSP, security headers, referrer behaviour and external link policies.
- Run keyboard, screen-reader, reduced-motion, zoom and low-bandwidth testing.
