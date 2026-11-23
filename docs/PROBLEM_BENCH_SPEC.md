# AARAMORA Problem Bench

**Implementation:** `check-ins.html#problem-bench`  
**Added:** 24 November 2026  
**Status:** Prototype feature; clinical/safeguarding review pending

## Purpose

Problem Bench is an optional, private, self-guided worksheet for one everyday problem at a time. It helps a visitor describe a situation, separate what may be within their influence from what may not be, list options, identify support, choose a small action if they wish, and review later.

It is not problem-solving therapy, the Friendship Bench programme, a clinical service, a risk assessment or a validated intervention. It does not use scores, labels, diagnostic questions or automated interpretation.

## Evidence and product boundary

### Friendship Bench, Zimbabwe

Chibanda et al. (2016), JAMA, cluster randomised trial in 24 primary-care clinics in Harare; 573 adults were randomised. The intervention comprised six individual problem-solving therapy sessions delivered by trained, supervised lay health workers plus an optional six-session peer-support programme. At six months the intervention group had fewer depressive symptoms than enhanced usual care; the reported proportion with PHQ-9 scores >=11 was 13.7% versus 49.9%.

Source: https://pubmed.ncbi.nlm.nih.gov/28027368/  
JAMA full text: https://jamanetwork.com/journals/jama/fullarticle/2594719

**Do not infer that those results apply to a website worksheet.** AARAMORA must not call its tool the Friendship Bench, problem-solving therapy, an equivalent programme or an evidence-based treatment.

### Healthy Activity Programme, Goa

Patel et al. (2017), The Lancet, individually randomised trial in ten primary health centres in Goa. 495 adults with moderately severe to severe depression were randomised to enhanced usual care with or without HAP. The structured intervention was delivered by trained lay counsellors. At three months, remission (PHQ-9 <10) was 147/230 (64%) in the HAP plus enhanced-usual-care group and 91/236 (39%) in enhanced usual care alone.

Source: https://pubmed.ncbi.nlm.nih.gov/27988143/  
Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC5236064/

The 12-month follow-up is a follow-up of the same human-delivered programme, not an evaluation of a digital activity planner: https://pmc.ncbi.nlm.nih.gov/articles/PMC5595303/

**Product boundary:** the Little Garden or activity prompts may support a visitor's own planning, but must not be called HAP, behavioural activation therapy or a digital equivalent of the Goa intervention.

## User flow

1. **Name one situation.** Free text, optional, with a short limit and no request for identifying detail.
2. **Separate influence.** Two optional fields: what may be within the visitor's influence and what may be outside it.
3. **Explore options.** The visitor may list options, including doing nothing for now, asking for support or choosing a small practical step.
4. **Find support.** Optional free text for a trusted person, qualified professional or practical resource.
5. **Choose an action.** One small action if it feels safe and realistic; rest or waiting is an acceptable choice.
6. **Choose timing and review.** Optional select fields. No reminders, push notifications or follow-up surveillance.
7. **Prepare / print.** The visitor reviews their own notes and may print or save a PDF locally.

## Safety and privacy

- A clear emergency/help strip appears before the worksheet. Completing the worksheet is never a condition for accessing support.
- Tell visitors before entry that answers remain in the current page, are not stored, uploaded, analysed or sent, and may remain visible on a shared/monitored device.
- No names, phone numbers, addresses or detailed trauma accounts are requested.
- No `localStorage`, `sessionStorage`, cookies, analytics, network APIs, AI calls or URL parameters contain worksheet answers.
- The worksheet cannot assess suicide/self-harm risk, domestic violence, coercion or safeguarding needs.
- If the situation involves immediate danger, suicidal intent, abuse, coercive control or urgent medical needs, the user should not be encouraged to work through the worksheet before seeking human support.
- The worksheet is never presented as suitable for all situations. It may be skipped or cleared at any point.
- Printed notes may expose private information on shared printers. Warn visitors to consider their environment before printing.

## Current implementation checklist

- [x] Optional text fields with length limits.
- [x] Influence / outside-control distinction.
- [x] Options and support fields.
- [x] One small action, optional timing and review.
- [x] Print / save as PDF action.
- [x] Clear form action.
- [x] No score, label or diagnosis output.
- [x] Privacy and emergency boundaries displayed.
- [x] Preserves the guide finder, women's-health planner and cycle log.
- [ ] Clinician review of language and intended use.
- [ ] Safeguarding review of emergency, coercion and monitored-device wording.
- [ ] Hindi and Marathi native-language review.
- [ ] Lived-experience usability testing before any public pilot.

## Governance record

No named clinical lead or safeguarding approver has been assigned in this repository. This feature remains a prototype until the review roles are appointed and sign-off is recorded.