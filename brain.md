# AARAMORA — Project Memory

**Last updated:** 24 November 2026  
**Current state:** Static website prototype; chatbot and model integration disabled.

## 1. Mission

AARAMORA is an India-first mental-wellbeing and help-navigation website. It helps visitors understand information, try optional low-pressure activities, prepare for appointments and find real human support. Compete on trust, source quality and handoff to people, not engagement.

## 2. Service boundary

AARAMORA is not therapy, diagnosis, prescribing, telemedicine, emergency dispatch, an AI companion or a crisis service. Kiran is a silent visual character, not a chatbot or person. The public site does not promise clinical outcomes.

## 3. Public support policy

Only these national routes are currently displayed:
- Tele-MANAS: **14416**
- Emergency Response Support System: **112**

Both are recorded in `data/service-links.json` with official source URLs, source-check dates, next review dates and sign-off status. A named human reviewer is still pending. Do not re-add any other or alternate number until a named human reviewer has checked the official source, coverage and current access and signed the exact change.

## 4. Product and design

- The repository is a static HTML/CSS/JavaScript prototype. No npm service, database or backend is required to run the current website.
- Main navigation: Get help now, Understand, Tools and Trust.
- Sandhya visual direction: paper ivory, forest green, restrained sage and turmeric glow.
- Kiran remains a small, silent light motif; the turmeric glow dims into amber in Tonight mode.
- The homepage uses first-party illustrations and versioned local media.
- Browser tools are local-only and do not upload entries.
- The support page has a first-party offline cache after the first online visit.
- The Pune Access Map is a source-checked directory, not a ranking or verified capacity/quality claim.

## 5. Content review

Women's-health and research pages are explicitly drafts. Health content must be excluded from retrieval until a named qualified clinician signs the exact content version and its sources, language, review date and expiry are recorded. Hindi and Marathi support labels remain drafts pending native-speaker and clinician review. Source verification is not clinical sign-off.

## 6. Safety rules

Read `SAFETY.md` before changing content or code. Never invent helpline numbers or clinical facts. Do not include self-harm methods or painful substitutes. Do not diagnose or advise on medicines/doses. Never let relationship reflection become partner surveillance, coercion or a verdict about a partner. Privacy and human handoff take priority over feature completeness.

## 7. Chatbot / RAG — last, not live

The AARAMORA Guide is a future feature, **not implemented and not enabled**. Source-controlled planning files:
- `docs/RAG_CHATBOT_IMPLEMENTATION.md`
- `docs/rag/SYSTEM_PROMPT_V2.md`
- `docs/rag/CRISIS_TEMPLATE_REVIEW_DRAFT.md`
- `docs/rag/PROMPT_REVIEW_CHECKLIST.md`
- `scripts/search_reviewed_corpus.py` provides a local lexical retrieval-only Phase 2 path with citations and abstention; no model calls or network requests.
- `tests/fixtures/crisis-multilingual-301-v1.jsonl` contains 301 synthetic cases across English, Hindi, Marathi and Hinglish; all language/clinical labels remain pending human review.
- `docs/RAG_INGESTION_POLICY.md`
- `data/rag-ingestion-policy.json`
- `data/rag-corpus-manifest.json`

Non-negotiables:
1. Deterministic input safety plus an evaluated multilingual classifier runs before generation; risk accumulates within the current session.
2. Crisis signals skip the LLM and return a fixed clinician-approved message. A prompt token is only a defence-in-depth intercept, not the crisis detector.
3. Output groundedness/safety checks run after any future generation; failure is abstention.
4. Only current, signed, clinician-reviewed, rights-verified passages can enter retrieval.
5. Default-deny ingestion. Do not scrape, mass-download or bypass DRM/paywalls/borrowing; keep restricted sources link-only.
6. No accounts, transcript storage, long-term memory, model calls or analytics by default.
7. A public chatbot requires named clinical/safeguarding/engineering owners, an approved crisis script, privacy/provider review, 300+ multilingual crisis tests, jailbreak/groundedness/abstention tests, a kill switch and incident procedures.
8. The 100 Hinglish cases and 301-case multilingual pack are synthetic fixtures only. CI checks structure, not live model/detector behaviour; clinician, safeguarding and language review remain pending.

The corpus manifest is empty and runtime is disabled. The default corpus builder makes no network or model calls and rejects draft, expired, unsigned or rights-unverified sources.

## 8. Working agreements

- Read `brain.md`, `SAFETY.md` and the relevant feature spec before editing.
- Preserve current user-facing safety restrictions.
- Do not mark clinical, legal, cultural, language or accessibility review complete without named written sign-off.
- Do not send real user mental-health data to external models.
- Update documentation and tests with each product/safety change.
- Deploy only after CI passes and inspect the deployed commit; a newer GitHub main branch does not mean Vercel production is updated.


## 9. Latest verified website release · 24 November 2026

- Main commit `73c49f4182ef6befc37a8b760090acbccec1ebea` is deployed to Vercel production as `dpl_3joScLaijXWdRndiNcBw48itcvJc` (READY); stable alias `aaramora-platform.vercel.app`.
- GitHub content-check run `45391042468` passed: 97 website/content tests, 6 retrieval-only tests and the 49-record catalogue validator.
- Multilingual crisis pack: 301 synthetic structural fixtures (67 English, 67 Hindi, 67 Marathi, 100 Hinglish). No live classifier or LLM execution; all native-language, clinical and safeguarding labels remain pending.
- Pune Access Map: 25 official-page-listed service entries across 10 facilities, not an availability or quality ranking.
- Public crisis routes remain exactly 14416 and 112. Named human sign-off is still pending.
- Last small fixes: wellbeing skip link now targets `#main-content`; homepage Find a person card opens the Pune Access Map; offline support fallback includes Quick Exit.
- Do not claim whole-site screen-reader, 200% zoom, slow-network or Lighthouse sign-off from automated CI. Those checks remain open for the exact production version.
