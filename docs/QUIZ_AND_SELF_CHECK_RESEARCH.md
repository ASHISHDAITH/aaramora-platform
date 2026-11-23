# Quiz, Screening and Self-Check Research for Aaramora

**Research reviewed:** 24 November 2026  
**Purpose:** Decide which interactive questions Aaramora should offer across mental wellbeing, relationships and women's health.  
**Status:** Product/evidence review, not clinical approval or legal advice.

## Executive decision

The current Aaramora MVP should offer **guide-finders, optional self-reflections and appointment-preparation tools**. It should not present a symptom quiz as a diagnosis, calculate condition likelihood, assign mental-health or attachment labels, predict self-harm, or use a cut-off to decide who deserves care.

Clinical screening tools such as PHQ-9, GAD-7 and EPDS have legitimate uses. Safe use depends on target population, language validation, trained interpretation and a reliable follow-up pathway. Aaramora is an information/help-navigation prototype without a clinical team monitoring answers. It should link to official clinician resources rather than offer a scored screening flow.

**Four distinct types of tool**
- **Guide-finder:** “Which information page might help me?” No score or diagnosis.
- **Reflection:** “What pattern have I noticed in my own behaviour?” No psychometric claims or labels.
- **Appointment preparation:** “What do I want a clinician to know or ask?” No medical inference.
- **Clinical screening:** A validated instrument used in an appropriate care setting with a named clinician, response protocol and follow-up. Not part of the current MVP.

## 1. Evidence and instrument review

### Depression and anxiety: PHQ-9 and GAD-7

The official PHQ Screeners site hosts the PHQ and GAD-7 materials and states that the screeners and translations may be reproduced, translated, displayed and distributed without permission. The source describes them as instruments developed for healthcare practice and notes that the PHQ-9 scores nine depression symptom criteria and the GAD-7 seven anxiety symptoms. This is a reproduction permission statement, not evidence that unsupervised online scoring is appropriate for Aaramora.

- Official screener repository and instrument permissions: https://www.phqscreeners.com/select-screener
- NICE adult depression recommendations: https://www.nice.org.uk/guidance/ng222/chapter/recommendations

NICE says a positive response to an identification question should lead to assessment or referral by someone competent to perform a mental-health assessment. A comprehensive assessment should not rely only on symptom count; it should include duration, course, history and functional impact.

For Aaramora:
- Do not calculate PHQ-9 or GAD-7 scores in the static MVP.
- Do not publish severity labels or imply a negative result rules out a condition.
- If a clinical partner later uses an instrument, document exact version, target population, validation evidence, clinician owner and response workflow.
- PHQ-9 item 9 concerns thoughts of death/self-harm. It cannot be treated as an ordinary quiz answer or left without a same-session human response protocol.

### India and language-specific validation

**Marathi PHQ-9 (2026):** Shidhaye et al. report cultural adaptation and psychometric evaluation of a Marathi PHQ-9 against a semi-structured diagnostic interview in a rural Marathi-speaking population in Maharashtra. The PubMed record lists an online article date of 28 August 2026 and a December 2026 journal issue. The authors report AUROC 0.88, internal consistency 0.81 and test-retest ICC 0.81. This is locally relevant validation evidence, but should not be assumed to generalise to all Marathi speakers, urban settings, age groups or other clinical populations. Do not recreate the translated scale or import its threshold without studying the full paper and obtaining clinician approval.

- PubMed: https://pubmed.ncbi.nlm.nih.gov/42663663/
- DOI: https://doi.org/10.1007/s00127-026-03186-1

**Hindi PHQ-9:** A 2023 cultural-equivalence paper focused on Hindi-speaking patients with cancer in community palliative care. A 2025 psychometric evaluation then studied 228 adult cancer patients receiving community palliative care in northern India. Its authors explicitly call for further validation in other regional languages and populations. These studies do not establish universal validity for every Hindi-speaking visitor.

- 2023 cultural adaptation: https://pubmed.ncbi.nlm.nih.gov/37700900/
- 2025 psychometric evaluation: https://pubmed.ncbi.nlm.nih.gov/40837001/

**Hindi EPDS (2026):** A study in 181 mothers at a tertiary hospital, assessed 48 hours to 7 days after childbirth, reported a Hindi EPDS with AUC 0.912 and an optimal cut-off of 9 within that cohort. This is promising postpartum-specific research, but it is a narrow population and very early postpartum period. It is not automatic validation for all postpartum people, all Hindi dialects, antenatal use or general depression screening.

- PubMed: https://pubmed.ncbi.nlm.nih.gov/42813154/
- Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13623259/

**Marathi EPDS:** A 2023 article describes culturally sensitive translation and equivalence work for rural Maharashtra. Read the full paper for the scope of psychometric evidence before inferring diagnostic thresholds or suitability for web administration.

- Study: https://doi.org/10.1016/j.jadr.2022.100458

**GAD-7 Hindi/Marathi:** This review did not establish a specific contemporary validation suitable for every Aaramora audience and setting. This is an evidence gap in this review, not proof that no validation exists. Do not translate the scale in-house and call it validated.

### Perinatal screening: EPDS and PHQ-9

ACOG recommends standardised, validated screening for depression and anxiety in well-woman, prepregnancy, prenatal and postpartum care. It specifically says screening must be implemented with systems for timely assessment/diagnosis, effective treatment, monitoring and follow-up based on severity.

- ACOG patient screening: https://www.acog.org/programs/perinatal-mental-health/patient-screening
- ACOG implementation guide: https://www.acog.org/programs/perinatal-mental-health/implementing-perinatal-mental-health-screening
- ACOG clinical guideline: https://www.acog.org/clinical/clinical-guidance/clinical-practice-guideline/articles/2023/06/screening-and-diagnosis-of-mental-health-conditions-during-pregnancy-and-postpartum

Aaramora must not run an EPDS/PHQ-9 result flow unless it has a named perinatal clinical service, an urgent response protocol and locally appropriate validation. Availability of a questionnaire online is not sufficient.

### PMOS / PCOS and psychological screening

The 2023 international evidence-based PCOS guideline recommends that healthcare professionals screen adults and adolescents with PCOS for depression using regionally validated tools, and adults with PCOS for anxiety using regionally validated tools. Moderate or severe symptoms should lead to further assessment, referral or treatment. It also recommends asking about symptom impact, quality of life, key concerns and management priorities.

This supports Aaramora’s **appointment-preparation planner**, not a DIY PMOS symptom score. The guideline is written using PCOS terminology in its 2023 edition; keep its historical term when citing it, while the website's current naming policy may explain PMOS/PCOS continuity.

- Guideline recommendations: https://pmc.ncbi.nlm.nih.gov/articles/PMC10477934/

### PMDD and cyclical symptoms

The EMA guideline says prospective daily monitoring over two consecutive menstrual cycles is required in its described PMDD diagnostic-study framework. It explains that symptoms are not unique to PMDD and that timing across the premenstrual and post-menstrual phases matters; retrospective recall is not a substitute for prospective observation.

Aaramora may offer an **original blank paper log** for dates, cycle day, symptoms and daily-life impact. It must not reproduce the DRSP, assign a PMDD score or claim that a two-cycle log proves a diagnosis.

- EMA PMDD guideline: https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-treatment-premenstrual-dysphoric-disorder-pmdd_en.pdf

### Endometriosis and pain tracking

NICE recommends telling people with suspected or confirmed endometriosis that keeping a pain and symptom diary can aid discussions with a healthcare professional. It does not say a web symptom quiz diagnoses endometriosis. Aaramora should offer neutral symptom-and-impact notes, not a “Do I have endometriosis?” score.

- NICE endometriosis recommendations: https://www.nice.org.uk/guidance/ng73/chapter/Recommendations

### Menopause questionnaires

The rights holder for the Greene Climacteric Scale says the original and translations were validated for paper administration and have not been adapted for tablet, web or IVR administration. Permission is required, and modified items cannot be represented under that instrument name. Aaramora should not copy this scale into the website.

- RWS licensing and administration FAQs: https://lifesciences.rws.com/greeneclimactericscale/faqs

Provide general information and original appointment notes instead.

### Adult attachment instruments

The ECR-R measures attachment-related anxiety and avoidance. Its author explains that it contains 36 items, reverse-keyed items and separate dimensional scores. The author says no permission is needed for non-commercial research use, but commercial use requires permission. The author also cautions that there is no natural or correct way to assign categorical attachment styles from the two dimensions.

- Author FAQ, instrument description and terms: https://labs.psychology.illinois.edu/~rcfraley/measures/ecrr.htm

Aaramora should keep its three **original, unvalidated reflections** clearly separate from ECR-R/ECR-RS and never call their results “attachment anxiety”, “avoidant”, “secure” or a psychometric profile. The ECR-R source is informative for distinguishing constructs, not a reason to paste its verbatim items into this product.

### Suicide and self-harm risk scores

NICE explicitly says not to use risk-assessment tools/scales to predict future suicide or self-harm repetition, and not to use global low/medium/high risk labels to decide who receives treatment or is discharged. Assessment should focus on the person's needs and immediate/longer-term safety.

Aaramora must not add a suicide-risk quiz, probability, traffic-light score or “low-risk” reassurance. Crisis routes must remain available without a completed questionnaire.

- NICE NG225 recommendations: https://www.nice.org.uk/guidance/NG225/chapter/recommendations

## 2. Review of Aaramora's existing relationship reflections

### Appropriate choices already present
- The relationship page labels its three reflections original and unvalidated.
- It has no score, clinical cut-off, attachment identity, partner rating, compatibility result or stay/leave recommendation.
- The safety check precedes communication advice and reflection tools.
- Unanswered safety items are not treated as No.
- Yes/Not sure prioritises private support rather than couple-repair exercises.
- Answers stay in page memory. The page has no local/session storage, network call or server submission.

### Requirements to preserve
- Keep separate behaviour prompts: connection uncertainty/attachment protest; conflict/pursue–withdraw/repair; boundaries and mutual respect.
- Do not automatically frame a delayed reply as attachment pathology. Consider actual inconsistency, practical constraints, context and mutual responsibilities.
- Results should describe selected themes, never identify a person as anxious/avoidant/secure.
- Respect requests for space and no-contact boundaries. No partner tracking, block bypass, lookup or manipulation advice.
- A negative safety check cannot certify safety.
- Safeguarding specialist review is needed for the questions, result language and safety pathway.

Before any scored relationship assessment is considered, commission a clinician/researcher review of construct, target population, language, measurement validity, permissions, measurement invariance and the risk of blaming a person in an unsafe relationship.

## 3. Recommended quiz/tool architecture

| Level | User-facing tool | Output | MVP decision |
|---|---|---|---|
| 0 | Guide finder | Relevant education page and support options | **Build now** |
| 1 | Self-reflection | User-selected themes and optional next step | **Keep current relationship reflections** |
| 1 | Appointment preparation | User's concerns and questions, printable | **Build now** |
| 1 | Cycle/symptom paper log | Dates, symptoms, cycle timing and impact, no score | **Build now** |
| 2 | Validated clinical screener | Instrument-specific output with clinical follow-up | **Do not implement in current MVP** |
| 3 | Diagnostic assessment | Clinical formulation by qualified professional | **Outside Aaramora's role** |

### Guide-finder design
- Ask: “What would you like help understanding?”
- Choices may include low mood, worry, sudden body alarm, stress, trauma reminders, sleep, repeated thoughts, relationship strain, women's health and “not sure”.
- Return a relevant information page, not a condition label or probability.
- Keep “find a person” and urgent support visible.
- No scoring, countdown, ranking, streaks or forced personal story.

### Appointment-preparation design
Collect only what helps the visitor prepare: broad concern area, what they have noticed, approximate duration, impact on daily life and questions for the clinician. Every field is optional. The static tool holds values in page memory and offers a print/save-as-PDF action. Do not upload, persist, analyse with AI or put health details in the URL.

### Women's-health symptom log
Offer an original blank paper log for dates, optional cycle day, symptoms/mood/pain and impact. It is not a validated instrument and must not generate a PMDD/PMOS/endometriosis result.

## 4. Minimum requirements for every check-in

1. Put “not a diagnosis or clinical test” before the first question.
2. Make every item optional and provide clear skip/reset/leave paths.
3. Explain data handling before asking. Current MVP: in-page memory only; no network, analytics, AI or persistence.
4. Never use colour, icons or wording to imply severity/risk scores.
5. Use semantic fieldsets/legends, explicit labels, keyboard focus, visible instructions and an announced result region.
6. Results describe what the visitor selected, what page may be relevant and what the page cannot determine.
7. Human support and urgent routes remain available without a quiz.
8. Avoid trauma narratives, partner identifiers, screenshots and unnecessary medical history.
9. A negative result or skipped item is not proof that someone is safe or healthy.
10. Screening/diagnosis features require an explicit clinical governance decision.

## 5. Release gates for any future clinical screener

- Named clinical owner and qualified reviewer for the instrument.
- Target age group, population, setting and intended use documented.
- Exact version and reproduction rights recorded.
- Language version validated for the intended population; translation alone is not validation.
- Clinician response, same-session escalation and referral workflow funded and tested.
- Explicit protocol for positive self-harm/suicidality items; no automated low-risk reassurance.
- Accessibility, cognitive testing, native-speaker and privacy/security review completed.
- Users understand a screen is not a diagnosis and can request human care regardless of score.
- Version history, expiry date and content owner recorded.

## 6. Sources and date notes

Sources were checked on 24 November 2026. The Marathi PHQ-9 and Hindi EPDS studies are described with their specific study populations and settings; they are not treated as universal validation. The PHQ website's reproduction permission is distinct from clinical suitability. Where a current regional validation or instrument licence could not be verified, this report says so rather than filling the gap.

The new check-in page does not reproduce any proprietary scale. The two-cycle paper log is original, unscored material.
