# RAG prompt evaluation — starter suite

**Status:** Fixtures created; model-level evaluation not run.  
**Date:** 24 November 2026.

## Starter set

`tests/fixtures/hinglish-redteam-v2.jsonl` has 100 synthetic Hinglish messages with expected safety routes.

| Category | Count |
|---|---:|
| Direct self-harm / suicide signal | 20 |
| Indirect risk / hopelessness | 10 |
| Negation / ambiguous risk | 10 |
| Harm-to-others risk | 5 |
| Abuse / immediate danger | 10 |
| Urgent postpartum signs | 5 |
| Acute panic / dissociation / alarming physical symptoms | 10 |
| Ordinary distress / information request | 10 |
| Out-of-scope request | 5 |
| Prompt injection / jailbreak | 15 |
| **Total** | **100** |

All cases are synthetic and contain no real visitor information. Expected routes are proposed labels for review, not validated clinical classifications.

## What CI checks

- Exactly 100 unique fixture records exist.
- Every record is labelled synthetic and Hinglish.
- The set includes jailbreak cases and fixed-crisis cases.
- Prompt text contains the deterministic pre-generation handoff and token fallback.
- The crisis response is explicitly not approved.
- The ingestion policy is default-deny and the corpus manifest is empty.
- The public support register contains only 14416 and 112.

## What has not been tested

There is no model endpoint, deployed detector or chatbot UI in this repository. Therefore these fixtures have **not** been run against an LLM, an Indic classifier or an actual safety router. CI checks the artefacts and release constraints, not model behaviour. Do not describe the prompt as passing a 100-message test.

The source design report requires at least 300 crisis messages across English, Hindi, Marathi and Hinglish, plus retrieval accuracy, groundedness, abstention, adversarial, tone and regression testing. Clinician sign-off is required before real-user exposure. The 100-message Hinglish set is only a starting slice.

## Next evaluation phase

After a model and deterministic detector are selected for internal testing:
1. Review and refine the 100 starter cases with clinicians and safeguarding reviewers.
2. Expand to 300+ multilingual cases, including direct/indirect, negated, sarcastic, coded and long-form messages.
3. Measure recall and investigate every miss; do not publish a recall claim from the starter set.
4. Run jailbreak and prompt-injection cases against the exact prompt/model/corpus build.
5. Test citations against retrieved evidence and verify abstention when no source is approved.
6. Repeat after every prompt, model, corpus, threshold or detector change.


# Multilingual crisis evaluation pack — 301 synthetic starter cases

**Status:** Draft dataset. No detector/model execution or clinician label review has been completed. Hindi, Marathi and Hinglish wording requires native-language review before it can be used as an evaluated benchmark.  
**Prepared:** 24 November 2026.

## Coverage

`tests/fixtures/crisis-multilingual-301-v1.jsonl` combines the existing 100 synthetic Hinglish red-team messages with 67 English, 67 Hindi and 67 Marathi crisis/safety-handoff cases.

| Language/style | Count | Current review status |
|---|---:|---|
| English | 67 | Editorial, clinical and safeguarding labels pending |
| Hindi | 67 | Native-language, clinical and safeguarding review pending |
| Marathi | 67 | Native-language, clinical and safeguarding review pending |
| Hinglish | 100 | Language, clinical and safeguarding review pending |
| **Total** | **301** | **Not validated for live use** |

Coverage includes direct and indirect suicidal language, self-harm urges, harm-to-others risk, abuse/immediate danger, postpartum urgent signs and acute panic/dissociation. The existing Hinglish portion also includes out-of-scope and prompt-injection/jailbreak attempts.

## Limitations

- All messages are synthetic. They are not validated screening items or a clinically representative dataset.
- Provisional expected routes are test hypotheses, not authoritative labels. A clinician and safeguarding reviewer must review every case and investigate likely false positives and false negatives.
- Hindi and Marathi wording must be checked by native speakers from the intended audience. Machine-generated draft text must not be described as reviewed translation.
- The pack has not been run against an LLM, classifier or deployed deterministic safety router. CI checks structure and metadata only.
- Passing fixture-count tests is not a safety-performance result and must not be reported as recall or accuracy.

## Required next evaluation

1. Assign named clinical, safeguarding and language reviewers.
2. Review all 301 messages and route labels; add colloquial, indirect, negated, sarcastic, coded and long-form variants.
3. Implement and evaluate the deterministic pre-generation safety layer against the reviewed cases.
4. Measure recall and inspect every miss; measure false positives and safe handoffs.
5. Run jailbreak/prompt-injection messages against the exact prompt, approved corpus and chosen model in an internal environment.
6. Repeat regression after every prompt, model, corpus, threshold or detector change.

No public chatbot or beta is permitted until the review, evaluation, privacy, incident-response and kill-switch gates are approved in writing.
