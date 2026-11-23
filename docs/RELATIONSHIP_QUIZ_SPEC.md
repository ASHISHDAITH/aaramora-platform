# Relationship Reflection Quiz Specification

## Product status
Two original reflection tools and one non-scored safety check are implemented on `relationships.html`. They are not validated scales, clinical screening instruments or diagnostic tools.

## Quiz A — Attachment protest reflection
Six prompts cover:
1. Urge to send repeated messages/calls after an unanswered message.
2. Checking online status, read receipts or social-media clues.
3. Interpreting delays as rejection without enough context.
4. Indirect tests, hints or withdrawing to trigger pursuit.
5. High-intensity words or breakup threats used to seek a reaction/reassurance.
6. Difficulty focusing until contact or clarity arrives.

Response options: Never / Sometimes / Often.

Result behaviour:
- Display only items marked Sometimes or Often.
- No sum score, attachment style label, severity label, cutoff or diagnosis.
- Encourage separating observable facts from feared interpretations and naming a direct request.
- Note that another person's real inconsistency may matter; users should not automatically blame themselves.

## Quiz B — Conflict pattern reflection
Six prompts cover:
- two pursuing behaviours;
- two withdrawal/avoidance behaviours;
- two repair/pause skills.

Response options: Rarely / Sometimes / Often.

Result behaviour:
- Display only behaviours marked Sometimes or Often.
- Do not assign a “pursuer”, “withdrawer”, anxious, avoidant or toxic identity.
- Explain that conflict is contextual and dyadic.
- Offer a pause-and-return suggestion only for relationships where both people can participate freely.

## Safety check — separate from quiz scoring
Four prompts ask about:
- fear of a partner's reaction to disagreement or leaving;
- monitoring, isolation, financial control or restriction of contacts;
- sexual pressure or pressure to share intimate images;
- threats, intimidation, stalking or physical harm.

Response options: No / Not sure / Yes.

Any Yes or Not sure:
- display a safety-first message and India support routes;
- say this is not a risk assessment or finding about the relationship;
- direct the visitor away from couple-repair exercises and toward private support;
- never ask for incident details or contact the partner.

All No:
- say the check cannot certify safety;
- do not present it as a pass or safe-relationship badge.

## Privacy and technical requirements
- Never transmit answers, use analytics, save to localStorage/sessionStorage, put answers in a URL or send to an AI service.
- Answers exist in the open page only; Reset or page refresh clears them.
- No free-text incident history is required.
- All prompts can be skipped or reset.
- Results are inserted as text nodes, not interpreted HTML.
- Keyboard, screen-reader labels, focus states, reduced motion and mobile layout are required.

## Release gate
A qualified clinician and safeguarding specialist must review the questions, result language and referral pathway. Native Hindi/Marathi reviewers must review translations. Do not add a psychometric score, attachment category or relationship compatibility result without a validated instrument, licensing review and clinical governance.
