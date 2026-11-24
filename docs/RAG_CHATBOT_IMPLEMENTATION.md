# AARAMORA RAG assistant — implementation and release plan

**Status:** Internal planning artefacts only. No chatbot is built, enabled or available to visitors.  
**Last updated:** 24 November 2026  
**Source basis:** Safe RAG Chatbot Design Report (29 October 2026), AARAMORA ROADMAP / SAFETY design notes, and the supplied System Prompt v2 draft.  
**Clinical lead:** Unassigned. **Engineering owner:** to be assigned.

## 1. Release position

The chatbot remains **disabled**. The existing static website and Get Help page are the public human-support route. The repository contains no approved clinical corpus yet, so the retriever must return zero passages until a named reviewer approves content and the rights checks pass.

The supplied v2 prompt is retained as a draft with safety clarifications. A prompt is not a crisis detector, clinical approval or release gate.

## 2. Architecture and execution order

1. **Input safety layer (code + classifier):** runs before any retrieval or model call. Detects explicit/indirect suicide and self-harm signals, harm to others, abuse/immediate danger, acute panic/dissociation and urgent postpartum psychosis signals. Risk accumulates across turns in an ephemeral session latch. If flagged, skip the LLM and return the fixed clinician-approved response.
2. **Query understanding:** detect language (English/Hindi/Marathi/Hinglish), normalise spelling for search only, and redact obvious personal identifiers before any future external model call. Do not ask for identity or precise location.
3. **Rights and clinical eligibility gate:** include only current, signed, clinician-reviewed items with a named reviewer, review date, expiry, sources and a verified reuse licence. Draft, expired, unsigned or rights-ineligible items are excluded before retrieval.
4. **Retrieval-only phase:** begin with local/static lexical search and citations. Do not use an LLM. A future multilingual embedding/rerank phase may be evaluated against a reviewed test set; it is not needed to demonstrate the no-model baseline.
5. **Grounded generation (later, internal only):** only after retrieval accuracy, provider privacy terms, redaction, rate limits, kill switch and clinician approval. The model can use only retrieved context and must cite each factual answer.
6. **Output safety layer:** run after generation; reject unsupported claims, diagnosis, medicine/dose instructions, self-harm content, roleplay, fabricated sources and malformed JSON. Failure means safe abstention.
7. **Human route:** visible 14416 / 112 links, clear statement that chats are not monitored in real time, no claim that the bot can contact services.

## 3. Important refinement to Prompt v2

The requested `[[CRISIS_TEMPLATE]]` token is defence-in-depth only. It is **not** the primary crisis mechanism. The application must detect risk before the model call and bypass the model. If a model returns the token unexpectedly, the router intercepts it and returns the approved fixed template. A crisis token must never appear to the visitor.

The prompt says “no memory”; the controller may retain only a minimal in-memory risk latch for the current conversation so risk cannot disappear when the user changes wording. It must not create a persistent profile, transcript store or cross-session memory.

## 4. Corpus and rights rules

- Default deny. Empty manifest means empty index.
- First-party original passages may be considered only after named clinical review where they contain health/safety information, a clear content owner, exact sources, language and an expiry date.
- Third-party resources must be checked at the exact work, edition, translation, file and territory level. A public link or open licence on platform metadata does not automatically permit text ingestion.
- Link-only / no-ingestion items are listed in `docs/RAG_INGESTION_POLICY.md` and `data/rag-ingestion-policy.json`.
- Never scrape or mass-download sites, bypass DRM/paywalls/borrow limits, or ingest copyrighted books, translations, commentaries or workbooks without explicit permission.
- BCcampus is a candidate only after the exact guide, edition, author, CC BY 4.0 notice and attribution requirements are verified. It is not in the allowlist yet.

## 5. Current status

| Workstream | Status | Release condition |
|---|---|---|
| Prompt v2 | Drafted | Clinical + safeguarding review |
| English crisis response | Draft only | Written clinician approval |
| Hindi/Marathi crisis scripts | Not prepared | Native-speaker + clinician approval |
| Corpus manifest | Empty | Approved and rights-eligible source files |
| Corpus builder | Local/offline only | Tests pass; no external provider |
| Retrieval-only | Not exposed to visitors | Reviewed corpus + retrieval evaluation |
| Model generation | Disabled | Privacy terms, model selection, internal red-team |
| Crisis classifier | Not implemented | Multilingual phrase sets + evaluated classifier |
| 100 Hinglish cases | Synthetic draft fixtures | Run against actual detector/prompt once configured |
| Full crisis benchmark | Not complete | At least 300 cases across four language styles |
| Clinical oversight | Unassigned | Named lead, written approval, incident protocol |

## 6. Evaluation gates

The 100 Hinglish fixtures are a starter red-team set, not evidence of safety and not a substitute for the source plan's 300+ multilingual crisis set. The starter fixtures include explicit and indirect risk, negation/ambiguity, abuse, postpartum signs, panic/dissociation, out-of-scope questions and prompt-injection attempts.

Before any real user:
- build the 300+ English/Hindi/Marathi/Hinglish crisis set including explicit, indirect, sarcastic, coded, negated and long-form messages;
- measure recall and review every miss; “near 100%” is a target, not a claim;
- test retrieval accuracy, citation support, abstention, privacy/PII redaction, prompt injection, roleplay and output format;
- require clinician and safeguarding sign-off on the test set, thresholds and fixed messages;
- run regression after each prompt, model, corpus or threshold change;
- document kill switch, rate limits, incident response and no-live-monitoring disclosure.

No generation-level evaluation has been run yet because no model endpoint is configured. CI currently validates artefact structure, release gates and fixture coverage only.

## 7. Privacy and cost

No accounts, transcript storage, analytics, chat logging or third-party model calls are enabled. Do not send real mental-health disclosures to free-tier AI services. Any future provider must be reviewed for retention, training, subprocessors, regional processing and deletion terms before internal testing. Keep a zero-cost static retrieval path available; free model weights still require compute and do not mean zero operating cost.

## 8. Launch decision

**NO-GO for public chatbot.** Continue static website improvements and clinician review. The static library, support contacts and offline page remain available independently of any future assistant.


## 2A. Phase 2 — local retrieval before any model

The no-model baseline is implemented as `scripts/search_reviewed_corpus.py`. It performs local lexical BM25-style ranking over `data/rag-approved-index.json`, supports a language filter, returns title, excerpt, source URL, licence and review metadata, and has explicit abstention states for empty queries, empty corpora and no matching passages.

Example (internal/offline evaluation only):

```bash
python scripts/search_reviewed_corpus.py "sleep and rest" --language en --limit 5
```

The current corpus manifest and approved index are empty. The expected result today is `no_approved_passages`; this is intentional. No draft page or reading-library link-only source is used as a fallback. The command makes no network, model or embedding calls. It is not exposed as a public chatbot or visitor search UI.

## 6A. Multilingual synthetic benchmark package

The repository now contains `tests/fixtures/crisis-multilingual-301-v1.jsonl`: 301 synthetic cases (67 English, 67 Hindi, 67 Marathi and the existing 100 Hinglish set). It includes self-harm/suicide, indirect risk, harm to others, abuse/immediate danger, postpartum urgent signs, acute panic/dissociation and the original Hinglish out-of-scope/prompt-injection cases.

All labels and wording remain provisional. Hindi and Marathi require native-language review; all expected routes require clinician and safeguarding review. The pack is checked for structure in CI only. It has not been executed against an LLM, classifier or actual safety router, and must not be described as a validated benchmark or model pass.
