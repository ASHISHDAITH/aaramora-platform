# AARAMORA Guide v2 — independent review checklist

**Status:** Review not started. No named clinical lead assigned.

Review the exact text in `SYSTEM_PROMPT_V2.md` and the separate crisis response draft. Do not approve the prompt as a substitute for code safety.

## Clinical / safeguarding review
- [ ] No diagnosis, medication/dose instructions, treatment promises or therapy roleplay.
- [ ] Risk categories cover self-harm/suicide, harm to others, abuse/immediate danger, acute panic/dissociation and urgent postpartum psychosis.
- [ ] Negated, sarcastic, indirect, coded and long-form risk language is reviewed.
- [ ] Crisis handling is performed by deterministic application code before the model call.
- [ ] The model cannot generate or rewrite the clinician-written crisis template.
- [ ] The fixed response is non-probing, non-graphic and does not imply live monitoring.
- [ ] Post-handoff behaviour keeps the fixed human-support panel visible.
- [ ] Human route labels and scope accurately reflect 14416 and 112 only.
- [ ] Women's-health pages marked draft are excluded from retrieval.
- [ ] Relationship content does not produce partner verdicts or unsafe couples-repair guidance.

## Language and inclusion review
- [ ] Hindi review by a named native speaker.
- [ ] Marathi review by a named native speaker.
- [ ] Hinglish red-team cases reviewed for colloquial spellings, code-switching, negation, slang and regional variation.
- [ ] Support route text is understandable without relying on machine translation.
- [ ] LGBTQ+ affirming, disability-aware and culturally respectful language reviewed.

## Privacy / engineering review
- [ ] No long-term memory or transcript storage.
- [ ] Any ephemeral risk latch is session-only and contains the minimum state required.
- [ ] PII redaction and log policy documented before a future model call.
- [ ] Provider retention/training terms reviewed before internal tests.
- [ ] Prompt injection treats both context and user content as untrusted data.
- [ ] JSON parser validates schema; malformed output becomes safe abstention.
- [ ] Output safety and groundedness checks can veto generated text.
- [ ] Rate limits, budget cap, kill switch and incident response are tested.

## Evaluation
- [ ] Review the 100 synthetic Hinglish starter cases.
- [ ] Expand to at least 300 crisis cases across English, Hindi, Marathi and Hinglish, including explicit, indirect, sarcastic, coded, negated and long messages.
- [ ] Measure recall and review every miss. Do not claim near-100% without results.
- [ ] Evaluate groundedness, abstention, source citation, prompt injection, out-of-scope handling, tone and JSON validity.
- [ ] Regression runs after every prompt, model, corpus or threshold change.
- [ ] Clinical and safeguarding sign-off is written and version-specific.

## Sign-off

| Role | Name / credentials | Date | Version/hash | Decision |
|---|---|---|---|---|
| Clinical lead | UNASSIGNED | — | — | PENDING |
| Safeguarding reviewer | UNASSIGNED | — | — | PENDING |
| Hindi reviewer | UNASSIGNED | — | — | PENDING |
| Marathi reviewer | UNASSIGNED | — | — | PENDING |
| Engineering owner | UNASSIGNED | — | — | PENDING |
