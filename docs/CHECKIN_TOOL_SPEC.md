# Check-in and Appointment Tool Specification

**Current scope:** static Aaramora MVP  
**Research basis:** `docs/QUIZ_AND_SELF_CHECK_RESEARCH.md`  
**Page:** `check-ins.html`

## Product role
A low-pressure route finder and preparation space. It helps a visitor select relevant education, organise questions for an appointment and print an original blank two-cycle symptom log. It is not a clinical screener, symptom checker, risk assessment or diagnosis tool.

## Included modules
1. **Guide finder:** optional selection, relevant information page and explanatory note. No score, classification or prediction.
2. **Women's-health appointment planner:** optional concern area, selected experiences, broad duration, daily-life impact and visitor-authored question. Produces a local print view only.
3. **Two-cycle blank paper log:** original rows for date, optional cycle day, symptoms/mood/pain and daily-life impact. It does not copy DRSP or produce a PMDD result.
4. **Human-support links:** 112, Tele-MANAS 14416 and Women Helpline 181 are visible above the tools.
5. **Clinical screener explainer:** why PHQ-9/GAD-7/EPDS are not scored in the static MVP, with links to official sources and clinician workflows.

## Data and privacy
- No form submission, API, network fetch, analytics, localStorage, sessionStorage or AI call.
- Values exist only in page memory while the page remains open.
- The visitor controls printing. Printing can create a paper or PDF copy outside Aaramora.
- Warn against entering sensitive information on a monitored/shared device.
- Quick Exit to about:blank does not erase browser history, network logs or device records.

## Behaviour
- Guide finder has an empty/skip state. No selection is not interpreted as a condition.
- A chosen option routes to one plain-language guide. Result copy says this is a suggestion, not a diagnosis.
- Appointment planner fields are optional; blank values appear as “Not specified”.
- Clear resets all fields and generated result.
- Print view contains only the selected worksheet.
- Cycle log prints two blank 31-row tables, one per cycle, without scale, total or threshold.

## Accessibility
- Semantic headings and landmarks.
- Fieldsets and legends for related options.
- Explicit labels for every form control.
- Visible keyboard focus.
- Result regions use `role="status"` and `aria-live="polite"`.
- Large click targets, responsive one-column layout on small screens and reduced-motion support.
- Printed worksheet uses strong contrast and clear table headers.

## Out of scope
- PHQ-9/GAD-7/EPDS scoring.
- Diagnosis probabilities or severity bands.
- Suicide/self-harm risk score or “low-risk” result.
- PMOS/PCOS, PCOD, endometriosis, PMDD, menopause or postpartum diagnosis quiz.
- ECR-R/ECR-RS attachment-style scoring.
- Upload, account, cloud diary, AI analysis or clinician chat.

## Human review required
Before public health-service claims: qualified women's-health clinician review of the planner and urgent wording; mental-health clinician review of guide links and crisis copy; native-language review; safeguarding review of relationship flow; keyboard/screen-reader/device testing; and privacy review of print behaviour.
