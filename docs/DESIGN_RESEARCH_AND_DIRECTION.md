# First-Visit Experience — Research & Design Direction

**Status:** Concept direction and static prototype  
**Working product label:** “the platform” (final name remains open)  
**Audience assumption:** Adults in India, including people who may be distressed, overwhelmed, uncertain, low on time, on a low-end phone or more comfortable in Hindi/Marathi/Romanised Hindi.  
**Product boundary:** Mental-health information and help navigation. Not therapy, diagnosis, crisis response or an AI companion.

---

## 1. Design thesis

The first visit should feel like entering a quiet, respectful place where a visitor can orient themselves without having to explain their story.

The promise is not “we will heal you” or “you will feel better in 30 seconds.” A website cannot promise either. The promise is:

> **You do not have to figure everything out today.**
>
> A quiet place to understand what you’re feeling, find one small next step, and connect with real support when you need it.

Success is not maximum time-on-site, daily return or a completed onboarding funnel. Success is that a visitor can quickly find what they came for, understand the service boundaries, feel in control, and reach a relevant human support option when needed.

## 2. What the research supports

### 2.1 Trauma-informed design is a design and governance approach

SAMHSA’s framework identifies safety; trustworthiness and transparency; peer support; collaboration and mutuality; empowerment, voice and choice; and attention to cultural, historical and gender issues. These are not decorative themes: they should influence information architecture, interaction behaviour, privacy, content governance and support pathways.

A 2025 scoping review examined 118 studies of trauma-informed principles in digital technology. It found that digital interventions were not consistently or methodically applying trauma-informed approaches. The review also describes how cognitively demanding, confusing, exclusionary or blaming digital experiences can undermine trust and access. This is a rationale to make the principles explicit and test them, not evidence that a particular colour or animation treats trauma.

**Design implications**
- No forced disclosure, diagnostic self-labelling or personal history form on the landing page.
- Every task has an easy exit, back route or “not now” option.
- Explain what a tool does before inviting someone to use it.
- Never hide safety or help information behind a quiz, account or chat.
- Let users choose a path; don't force a recovery narrative or onboarding sequence.
- Publish clear boundaries, source and review information, privacy practices and correction routes.
- Co-design with people with lived experience, with genuine influence over decisions.

### 2.2 Psychological first aid suggests a human-help pathway, not an AI persona

WHO psychological first aid uses the action principles “Look, Listen and Link”: attend to safety and urgent needs, listen without pressure, and connect people with information and services. This platform is not a psychological first-aid provider, but the principles support a clear information architecture: make the situation legible, do not pressure the user to disclose, and make links to real support easy to find.

### 2.3 Calm technology: respect attention

Calm Technology principles call for the smallest possible attention demand, communication without unnecessary speech, usefulness when systems fail, and the minimum technology required to solve the problem.

**Design implications**
- No auto-playing sound, video, parallax or breathing animation.
- No pulsing red alerts or urgent-looking promotional banners.
- Use whitespace and clear page regions; avoid dense dashboards.
- Make static pages and the crisis/support route work without AI, database or third-party API.
- Make motion optional and honour `prefers-reduced-motion`.
- Every decorative element must earn its place.

### 2.4 Cognitive accessibility matters when someone is overwhelmed

W3C cognitive-accessibility guidance recommends clear hierarchy, obvious safety information, predictable layouts, clear labels, short chunks and language that is easy to understand. WCAG 2.2 provides testable accessibility criteria, including text contrast, resizing, focus visibility and minimum pointer target sizes.

**Design implications**
- One primary action per important section.
- Short sentences and plain words; explain uncommon clinical terms.
- Reuse navigation and component placement across pages.
- Visible focus states and keyboard operation.
- Target at least WCAG 2.2 AA; design practical touch targets around 44×44 CSS pixels where possible.
- Text contrast at least 4.5:1 for normal text and 3:1 for large text; don't rely on colour alone.
- Validate English, Devanagari and Marathi typography, line wrapping, text expansion and screen-reader pronunciation.
- No information should be available only inside an image.

### 2.5 Mental-health apps need trust, privacy and real user involvement

A systematic review of mental-health apps highlighted user experience, privacy and data protection, plain and transparent statements, and the involvement of people with lived experience. A separate systematic review of co-production across 26 studies found that co-production can make interventions more culturally sensitive and acceptable, while identifying power imbalances and inconsistent stakeholder involvement as challenges.

A meta-analysis of 92 RCTs (16,728 participants) found no significant association between persuasive-design principles and either efficacy or engagement. That is a strong reason not to add streaks, guilt-based reminders, artificial scarcity, leaderboard mechanics or engagement loops just because other apps use them.

**Design implications**
- No account gate to read core content or find help.
- Local-first private tools; don't send diary entries, screening answers or crisis text to free AI APIs.
- No ads, sale of personal data, streaks, badges for “progress”, or retention tricks.
- Paid co-design and decision-making roles for lived-experience contributors.
- Public Trust Ledger with content reviewers, review dates, sources, change history and correction process.

### 2.6 Character-led storytelling can make difficult subjects approachable—but don't imitate competitors

Apple's “Behind the Design: Headspace” describes the role of a warm visual identity, approachable style and information organisation in making mindfulness less intimidating. The transferable lesson is to make content approachable and easier to navigate—not to copy Headspace’s orange palette, character style, illustrations, wording or app layout.

Don Norman’s *Emotional Design* distinguishes visceral (first impression), behavioural (how it works) and reflective (what the experience means afterwards) design. For this platform:
- Visceral: quiet, warm, legible visual welcome.
- Behavioural: simple, predictable choices and fast routes.
- Reflective: visitor leaves knowing the platform was honest, respectful and useful.

This is a design lens, not clinical evidence that an interface can regulate a nervous system.

### 2.7 India-specific access is essential

Government of India sources currently identify Tele-MANAS at **14416** and **1800-89-14416** as a free, 24/7 mental-health helpline. A 9 October 2026 Ministry of Health press release states that it is available in multiple languages and operates across all States and Union Territories. The official ERSS site identifies **112** as the pan-India emergency number for police, fire and health emergencies.

The interface should present these as links to real public services, not as a service provided by this platform. Re-verify all numbers, operating details and wording immediately before launch and whenever content is reviewed.

---

## 3. The creative concept

### Working concept: “A little light along the way”

A quiet landscape, a winding path and a small light mark the idea that a visitor does not have to solve everything at once. The light helps them see a next step; it does not promise to make the whole path disappear.

### The character

**Kiran** is a temporary working name for a small firefly/light illustration. It is not the product name and is not approved for final use until native-speaker review.

Character rules:
- The character is a visual guide, not a therapist, person, chatbot, AI companion or substitute for human support.
- It does not ask questions, collect personal information, claim to understand the visitor or say “I know how you feel.”
- It does not send notifications, build a relationship, remember private disclosures or create dependence.
- It appears sparingly: welcome illustration, small chapter markers and occasional static story panels.
- It is optional and can be ignored without losing access to anything.
- Use understated editorial illustration suitable for adults—not a babyish mascot or a cartoon diagnosis.
- Avoid depicting distress, flashbacks, injury, panic, darkness as danger, or a character rescuing a helpless person.
- It is never a progress meter. There are no levels, streaks or “you are healed” endings.
- The name, symbolism, gestures and visual associations must be reviewed by Hindi and Marathi native speakers and people with lived experience.

### Short fictional story

> Some evenings, the path is hard to see.  
> The little light does not ask you to explain why.  
> It does not hurry you or choose your direction.  
> It simply makes the next step easier to find.  
> You can pause here. You can take another path. You can leave and return when you choose.

This is a fictional brand story, not a survivor testimonial, clinical intervention or claim about treatment.

---

## 4. First-visit experience map

### Screen 0 — Arrival: safety and welcome

The first viewport contains:
1. A narrow, calm support line: “Need a real person now? Free, 24/7 support in India: Tele-MANAS 14416. Immediate emergency: call 112.”
2. A simple header with Explore, A small pause, Find support, Our promises and a language selector.
3. The hero headline: “You don’t have to figure everything out today.”
4. One short explanation of what the platform does.
5. Primary CTA: “Find a small next step.”
6. Secondary CTA: “Find support from a person.”
7. Low-pressure link: “I’d rather just look around.”
8. A truthful privacy statement, only after the product implementation has been verified.

Do not make the visitor register, answer a mood quiz, identify a trauma, permit tracking or start a chat.

### Screen 1 — Choice, not interrogation

Heading: “What would help right now?”

Offer five optional entry points:
- I feel overwhelmed.
- I want words for what I’m feeling.
- I’m looking for professional support.
- I’m supporting someone.
- I just want to explore.

Each option routes to useful content. Nothing is recorded simply because the visitor clicked it. Don't convert the selected card into a diagnosis or risk score.

### Screen 2 — Optional moment to settle

Offer alternatives rather than prescribing a single technique:
- Orient visually to ordinary things in the room.
- Notice a stable point of contact if that feels okay.
- Choose a comfortable movement.
- Skip or close the section.

No forced breathwork, body scan, eyes-closed exercise, countdown, heartbeat sound or animation. Some people may find inward attention or breath focus uncomfortable. The page must say they can stop or choose another option.

### Screen 3 — Understand

The Words Library should use plain-language topic pages with:
- A direct answer near the top.
- What is known and what is uncertain.
- Practical, non-prescriptive next steps.
- When to consider professional help.
- Named author/reviewer, sources, last-reviewed date and next review date.
- A clear correction link.

### Screen 4 — Connect

The Appointment Bridge should explain the difference between psychologist, psychiatrist, counsellor and other relevant professionals; show how to prepare for a first appointment; explain cost and access limitations carefully; and link to verified public/private options. It should never promise availability or outcomes that have not been checked.

### Screen 5 — Leave with agency

End each tool or guide with:
- “Would you like to save this?” only where a genuinely private local save is implemented.
- “Find support from a person.”
- “Go back to exploring.”
- No guilt message, streak, forced feedback form or follow-up notification.

---

## 5. Page and navigation architecture

Primary navigation:
- **Explore** — topic and guide library.
- **A small pause** — optional, non-clinical grounding options.
- **Find support** — Appointment Bridge and India Access Map.
- **For someone close to you** — supporter resources.
- **Our promises** — Trust Ledger, privacy, reviewers, content standards and corrections.

Persistent safety route:
- Tele-MANAS 14416 / 1800-89-14416.
- 112 for immediate emergencies.
- A concise statement that the platform is not an emergency or crisis service.

First release should prioritise a small number of excellent, reviewed routes rather than a large catalogue:
1. First visit / welcome.
2. Find support in India.
3. Appointment preparation.
4. Anxiety / stress / overthinking information.
5. Sleep information and a private sleep diary (local-only).
6. Words Library / supporter pages.
7. Trust Ledger and privacy.

---

## 6. Visual design system

### Art direction

**Editorial warmth, quiet landscape, humane simplicity.**

Avoid:
- Hospital dashboards and generic medical icon grids.
- Overused neon gradients, glassmorphism and shiny “AI” aesthetics.
- White-on-pale text, low contrast or tiny disclaimers.
- Full-screen video, autoplay audio or parallax.
- Stock photos of people crying, holding heads or staring out windows.
- Child-like cartoon style or another app’s recognisable mascot system.

### Starter palette (design proposal; test contrast in implementation)

| Token | Hex | Use |
|---|---:|---|
| Paper | `#F5F3EC` | Main page background |
| Warm white | `#FFFEFA` | Cards and reading surfaces |
| Forest ink | `#203A34` | Main text and primary action |
| Muted ink | `#40544D` | Secondary text |
| Sage | `#DCE8DD` | Gentle surfaces |
| Dusk blue | `#DCE7E8` | Secondary illustration surface |
| Soft lilac | `#E8E1EE` | Occasional section accent |
| Clay | `#EAD4C4` | Warm accent |
| Focus blue | `#235B93` | Visible keyboard focus |

Do not assume these colours themselves are therapeutic. The goal is visual coherence and comfort while maintaining legibility. Recalculate actual contrast ratios for every component and state.

### Typography

- Use a highly legible sans family with full Latin and Devanagari coverage.
- Candidate families: Noto Sans + Noto Sans Devanagari, or another properly licensed family with tested Hindi/Marathi shaping.
- Use a restrained serif only for large editorial headings if it remains readable on low-end Android devices.
- Body text: approximately 16–18 px; line height around 1.6.
- Reading width: around 60–75 characters for long-form pages.
- Allow text zoom to 200% without clipped cards, hidden controls or horizontal overflow.
- Test Marathi conjuncts, Hindi punctuation, Hinglish wrapping and screen-reader language metadata.

### Layout and interaction

- Mobile-first, single-column reading flow; responsive split hero on desktop.
- Max reading width approximately 68rem.
- Reusable card radius and borders; use depth sparingly.
- At least 44×44 px practical touch targets where possible.
- Strong visible keyboard focus and logical tab order.
- No hover-only functionality.
- Motion off by default; support reduced-motion preferences.
- Keep all core content useful if JavaScript or remote APIs fail.

---

## 7. Character and illustration direction

Create one original vector illustration family:
- A tiny firefly/light with restrained forms, a warm point of light and a few subtle natural shapes.
- A path built from stones, gentle hills, windows or wayfinding landmarks.
- Human figures, if any, should be diverse and ordinary rather than clinical stock imagery.
- No symbol should imply that a person is broken, lost, weak or needs rescue.
- Don't use visual metaphors of cages, chains, storms, darkness or wounds to represent a visitor's mental state.
- Use the character as a signpost, not a narrator that dominates the interface.
- Maintain a text alternative when illustration conveys meaning; mark purely decorative SVGs as decorative.

All original illustrations must be created for this project or used under clearly checked licence terms. Reference products are for learning, not copying.

---

## 8. Microcopy and content tone

Voice: gentle, grounded, adult, clear, non-clinical where possible, never patronising.

Prefer:
- “You can choose what feels useful.”
- “You can skip this.”
- “Here are a few options.”
- “This information may help you decide what to do next.”
- “This page was reviewed by…”
- “The platform cannot provide emergency help. Here are verified services.”

Avoid:
- “We know exactly how you feel.”
- “Your healing journey starts now.”
- “Fix your mind.”
- “Complete your recovery.”
- “You are safe here” as an absolute guarantee.
- “Tell us what happened.”
- “Your AI friend is always here.”
- Any clinical promise, fear-based hook or diagnosis implied by a card click.

A calm site should not use vague euphemisms where clarity is needed. Explain clinical language in everyday words, and be precise about boundaries and urgency.

---

## 9. Privacy, safety and technical product rules

For the first version:
- No personal mental-health data sent to the server by diary, tools or self-checks.
- No real user messages, diaries, screening answers or crisis inputs sent to OpenRouter, Hugging Face, or other free inference services.
- No analytics SDK or behavioural heatmaps on sensitive flows.
- No advertising, sale of data, retargeting or engagement nudges.
- No account gate for crisis information or the core library.
- Avoid third-party fonts/scripts where they create unnecessary tracking or failure dependencies; self-host licensed assets where feasible.
- Crisis information must be static, reviewed and available if AI, search, hosting integrations or databases fail.
- Any crisis recognition must be implemented and clinically reviewed as deterministic code and service routing—not improvised by a prompt.
- No AI companion in the first release.
- All external help links require a verified source, date checked, owner and next review date.

### Proposed stack (consistent with the existing project direction)

- Next.js App Router + TypeScript.
- Static generation for content pages.
- MDX or structured content with named reviewer, source list, review date and expiry.
- `next-intl` for English, Hindi and Marathi locale routes.
- Local-only storage for private tools in v1.
- No server-side personal health records in v1.
- Keep all API/MCP use in development/research only; never make homepage safety/help routes depend on them.

---

## 10. Research and quality assurance plan

This interface must be co-designed and tested, not approved by the design team alone.

### Participants
- People with lived experience, paid for their time and given genuine decision influence.
- Native Hindi and Marathi speakers, including Romanised Hindi/Hinglish users.
- Clinicians with relevant experience.
- Accessibility testers: keyboard, screen reader, zoom, cognitive access and low-vision use.
- People with low-end phones, constrained data and lower digital literacy.

Participation must be voluntary, consent-based and allow skipping, pausing or withdrawing without explanation. Do not ask participants to disclose traumatic details to test a homepage.

### Usability tasks
1. Find out what the platform is and is not.
2. Find immediate human support without scrolling or signing in.
3. Find a professional and understand what type of help they provide.
4. Find out whether a private note is uploaded or shared.
5. Change language.
6. Increase text size and navigate with keyboard/screen reader.
7. Leave the site without losing control or triggering a follow-up.

### Success measures
- Time and success rate for finding a human help route.
- Correct understanding of platform boundaries.
- Ability to explain privacy handling in their own words.
- Task completion on low-end mobile and constrained data.
- Readability and comprehension across en/hi/mr.
- Accessibility defects and reduced-motion compliance.
- Participant-reported sense of control, not a claim of trauma recovery.

Do not optimize for session length, daily activity, streak completion or emotional disclosure volume.

---

## 11. Prototype status and limitations

`index.html` in this package is a static, responsive first-visit concept with:
- A home-page welcome, navigation and crisis support strip.
- Original SVG light/firefly/landscape artwork.
- A five-option “What would help right now?” section.
- A fictional short story.
- Optional grounding prompt interactions.
- Trust, privacy, support and footer sections.
- Draft English, Hindi and Marathi display strings.
- Reduced-motion and basic accessibility styles.

It is **not production-ready**:
- Hindi and Marathi copy is machine-drafted and requires native-speaker and clinician review.
- The language selector changes only the included homepage strings; full content localisation is not implemented.
- The Tele-MANAS and emergency references must be checked again before release.
- The local-storage privacy promise must be validated against actual code before being published as a promise.
- It has not completed formal WCAG testing, screen-reader testing, user research or clinical review.
- The “Kiran” character name is provisional.
- The final product name remains undecided.

---

## 12. Sources consulted

### Trauma-informed practice and digital design
1. SAMHSA, *Concept of Trauma and Guidance for a Trauma-Informed Approach* (2014): https://library.samhsa.gov/sites/default/files/sma14-4884.pdf
2. Eggleston et al. (2025), *A scoping review of trauma-informed care principles applied in design and technology*: https://doi.org/10.1177/20552076251360925
3. Cao & Hancock (2026), *Trauma informed participatory design: definitions, practices and resources*: https://doi.org/10.1080/15710882.2026.2659838
4. WHO, *Psychological First Aid*: https://iris.who.int/bitstream/handle/10665/379661/9789240101234-eng.pdf

### Digital mental health and co-production
5. Brotherdale et al. (2024), *Co-producing digital mental health interventions: A systematic review*: https://doi.org/10.1177/20552076241239172
6. *Smartphone apps for mental health: systematic review of the literature and five recommendations for clinical translation* (BMJ Open): https://doi.org/10.1136/bmjopen-2024-093932
7. Valentine et al. (2025), *A meta-analysis of persuasive design, engagement, and efficacy in 92 RCTs of mental health apps*: https://doi.org/10.1038/s41746-025-01567-5
8. JMIR (2024), *Evaluation of Digital Mental Health Technologies in the United States: Systematic Literature Review and Framework Synthesis*: https://mental.jmir.org/2024/1/e57401/

### Accessibility and content
9. W3C, *Web Content Accessibility Guidelines (WCAG) 2.2*: https://www.w3.org/TR/WCAG22/
10. W3C WAI, *Help Users Find What They Need*: https://www.w3.org/WAI/WCAG2/supplemental/objectives/o2-find/
11. W3C WAI, *Use Clear and Understandable Content*: https://www.w3.org/WAI/WCAG2/supplemental/objectives/o3-clear-content/
12. W3C WAI, *Animation from Interactions*: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions
13. NHS Digital Service Manual, *Standard for creating health content*: https://service-manual.nhs.uk/content/standard-for-creating-health-content
14. NHS Digital Service Manual, *Design principles*: https://service-manual.nhs.uk/design-system/design-principles

### Emotional and calm technology design
15. Don Norman, *Emotional Design: Why We Love (Or Hate) Everyday Things*: https://www.nngroup.com/books/emotional-design/
16. Don Norman, *Emotional Design: People and Things*: https://jnd.org/emotional-design-people-and-things/
17. Weiser & Brown, *Designing Calm Technology* (Xerox PARC, 1995): https://calmtech.com/papers/designing-calm-technology
18. Calm Tech Institute, *Principles of Calm Technology*: https://www.calmtech.institute/calm-tech-principles
19. Apple Developer, *Behind the Design: Headspace* (2023): https://developer.apple.com/news/?id=fkfnhq8u

### India support and emergency references
20. Ministry of Health and Family Welfare / DGHS, *National Mental Health Programme*: https://www.dghs.mohfw.gov.in/national-mental-health-programme.php
21. Press Information Bureau / Ministry of Health and Family Welfare, Tele-MANAS update (9 October 2026): https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2321522&lang=1&reg=1
22. Government of India, Emergency Response Support System: https://112.gov.in/

**Evidence boundary:** The cited research supports principles such as choice, transparency, co-design, clear structure, accessibility, privacy and restraint. It does not prove that the specific colour palette, firefly, story or hero line will reduce trauma symptoms. Those are creative hypotheses to test with the intended audience.


---

## 13. Women's Health corner (added 23 November 2026)

A new primary navigation destination, Women's health, links physical/reproductive health information with mental wellbeing and human care pathways. Topics include PMOS (formerly PCOS), endometriosis, heavy/painful periods, fibroids/adenomyosis, PMS/PMDD, menopause, thyroid conditions, iron deficiency and postpartum mental health.

The PMOS and midlife cognition section reports the 2024 CARDIA paper as an observational association only. It does not imply causation, brain damage or a personal prediction. The new PMOS name is used alongside PCOS during the evidence and search terminology transition.

Viral “hormone balance” claims are explicitly checked: regular activity and a balanced eating pattern may support general/metabolic health, but no single food, tea, seed or supplement is presented as a PMOS cure or hormone-balancing treatment.

This entire area is draft educational content, not a clinical service. Before publication it requires a qualified women's-health clinician, language review (English/Hindi/Marathi/Romanised Hindi), source revalidation and testing of urgent-care wording. Full evidence notes live in `WOMENS_HEALTH_RESEARCH.md`.