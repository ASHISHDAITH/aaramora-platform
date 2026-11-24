# AARAMORA Safety Rules

These rules apply to all content, pages, tools and future interactive features. They take priority over engagement or feature requests.

## 1. Service boundary
AARAMORA provides information and help navigation. It is not therapy, diagnosis, prescribing, telemedicine, emergency response or an AI companion. It must not promise trauma relief or relationship repair.

## 2. Public support routes
- India emergency response: **112**.
- Tele-MANAS: **14416**.
- AARAMORA currently publishes only these two national numbers.
- Any additional or alternate number remains unpublished until a named human reviewer confirms the official source, coverage and current access, records the review date, and signs off.
- Never add a number from memory or copy a historical number from an old planning file into the public UI.
- Keep source, owner, last-verified date, next review date and human sign-off status in `data/service-links.json`.

## 3. Safety messaging
- No graphic detail about suicide, self-harm, sexual violence or trauma.
- No methods or pain/shock substitutes.
- Never shame, blame, threaten, frighten or coerce a visitor.
- Use short, plain, non-promissory language.
- Keep help links visible and working without an account or quiz.
- Do not imply the site or future chat is monitored live.

## 4. Self-reflection quizzes
- Self-reflection only; no diagnosis or treatment decisions.
- Custom prompts must be labelled unvalidated and must not have clinical cutoffs.
- Never label a person or partner as disordered, abusive, narcissistic, avoidant, anxious or toxic from a quiz.
- Any future self-harm/suicide-related item must trigger the reviewed crisis pathway immediately, before any score or result.
- Never use quizzes to determine compatibility, blame, stay/leave or relationship worth.

## 5. Relationship-corner safeguards
- Safety comes before communication or couples-repair advice.
- A Yes or Not sure response to fear, coercion, monitoring, isolation, sexual pressure, threats, stalking or physical harm prioritises private, safety-focused support.
- Do not recommend couples counselling or mutual communication exercises as the default response to abuse or coercive control.
- Never describe jealousy, monitoring, forced password/device access, forced location sharing, isolation, sexual pressure or controlling finances as love.
- Attachment protest is descriptive, not a diagnosis. Repeated contact does not excuse disregarding another person's clear boundary.
- Respect no-contact and requests for space. Do not help bypass blocks, track a partner, monitor online status or manipulate a response.
- Do not ask visitors to describe abuse incidents, upload screenshots, name the other person or disclose detailed relationship history.
- Quick Exit does not erase browser history, network logs or shared-device activity.
- Couples communication content is only for contexts where both people can participate freely and without fear.

## 6. Privacy
No relationship quiz answers or personal disclosures may be sent to the server, analytics, ad networks or AI providers. No chat, public posting, direct messages or partner lookup is included in the current prototype.

## 7. Content governance
Every clinical or safety page needs an author, qualified reviewer, sources, reviewed date and expiry/next-review date. Relationship-safety language requires review by a safeguarding/domestic-violence specialist. Translations require native-speaker and clinician review.

## 8. Community
No live public peer community until trained moderation, report/block, privacy review, safeguarding, escalation protocols and a clinical lead are in place. No algorithmic amplification, follower counts or popularity ranking of distress.

## 9. Future chatbot release gates
- Input safety is deterministic code plus an evaluated classifier, before generation; risk accumulates within the current session.
- Crisis or immediate-danger signals skip the LLM call and return a fixed clinician-approved response.
- Output safety and groundedness checks run after generation; failures become a safe abstention.
- Only signed, current, rights-eligible reviewed passages enter the corpus. Draft/expired/unsigned content is excluded.
- No chat storage, no long-term memory, no third-party model calls or logs by default. No real disclosures to free-tier model APIs.
- A prompt is not a safety layer. A kill switch must leave the static site and help routes intact.
- No public chatbot until clinician and safeguarding sign-off, multilingual evaluation, prompt-injection tests, privacy review and incident procedures are documented.
