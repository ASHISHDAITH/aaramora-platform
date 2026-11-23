# First-Visit Design System v2

**Product label:** The platform (final name intentionally unresolved)  
**Audience:** Adults in India, including people arriving under stress, with limited time, low-end Android devices, constrained data, or a preference for English, Hindi, Marathi or Romanised Hindi.  
**Role:** Mental-health information and help navigation. Not therapy, diagnosis, crisis response or an AI companion.

## Design idea

**A little light along the way.** A quiet, editorial garden-path metaphor with one small static light character, provisionally named Kiran. The illustration helps orient visitors; it does not speak, assess them, collect information or signal progress.

## Visual tokens

| Token | Value | Use |
|---|---|---|
| Paper | `#F5F2E9` | Main background |
| Warm surface | `#FFFEFA` | Cards and reading surfaces |
| Forest | `#23483C` | Primary actions / dark support surface |
| Ink | `#203B32` | Main text |
| Muted ink | `#586B62` | Supporting text |
| Sage | `#DCE8DB` | Calm surfaces |
| Pale blue | `#DFE9E8` | Secondary surfaces |
| Lilac | `#EAE4EF` | Occasional accent |
| Clay | `#EAD8CB` | Warm accent |
| Focus | `#1D5E9B` | Visible keyboard focus |

Colours are visual design choices, not treatment or calming claims. Check actual component states for WCAG 2.2 AA contrast. Use 4.5:1 minimum for normal text, 3:1 for large text and relevant non-text UI elements.

## Typography

- Body: system-first sans stack with explicit Devanagari fallback (`Noto Sans Devanagari`).
- Editorial headings: restrained Georgia / serif fallback.
- Body size: 16–18 px; line height around 1.6.
- Reading column: approximately 60–75 characters.
- Test 200% text zoom, Hindi/Marathi shaping, conjuncts and line wrapping.
- Do not rely on a remote font service for critical content.

## Layout and components

- Crisis/help strip is present on every page and has working `tel:` links.
- Sticky header with four predictable routes and a compact language selector.
- Mobile menu has explicit expanded/collapsed state.
- One primary CTA per major section; secondary support route always visible.
- 44×44 px practical touch targets where possible.
- No hover-only functions.
- No autoplay, flashing, parallax, ambient audio or mandatory animation.
- Honor `prefers-reduced-motion`.
- Every page has a skip link, meaningful landmarks, focus styles and descriptive labels.
- Keep a blank-page quick exit, but state clearly that it does not erase browser history, logs or shared-device activity.

## Character: Kiran (provisional)

- Small abstract firefly/light, static vector illustration, non-human.
- Optional decorative guide. Ignore it without losing information.
- No chat, memory, notifications, personal questions, moods, streaks, badges or progress states.
- Do not portray a visitor as broken, trapped, frightened or waiting to be rescued.
- Name/symbolism to be reviewed by Hindi/Marathi speakers and lived-experience co-designers.
- The character is not the platform brand.

## Copy rules

Prefer:
- “You can choose what feels useful.”
- “You can skip this.”
- “Here are a few options.”
- “This information may help you decide what to do next.”
- “This page was reviewed by…”
- “The platform cannot provide emergency help. Here are verified services.”

Avoid:
- “We know exactly how you feel.”
- “You are safe here” as an absolute guarantee.
- “Tell us what happened.”
- “Your healing journey starts now.”
- “Fix your mind.”
- “Complete your recovery.”
- Clinical, trauma-relief or diagnosis promises.
- Fake testimonials and fabricated success stories.

## Privacy and safety defaults

- No account gate for core content or help information.
- No server-side personal mental-health data in v1.
- Diaries and tools must remain local-only after code and network review.
- Do not send real user messages, diary entries, quiz answers or crisis inputs to free inference services.
- No analytics SDKs, heatmaps, ad pixels or retargeting on sensitive routes.
- Crisis information must work if AI, databases, third-party APIs or scripts fail.
- All help services need a source, owner, last-verified date and next-review date.


## Women's Health corner

Add a distinct top-level navigation destination: **Women's health**. Use a warm muted-clay / sage secondary surface, but keep the same typography, focus visibility, readable line length and card system. The corner should not use stock imagery or stereotyped pink/feminine iconography.

Content entry points:
- PMOS (formerly PCOS), using both terms for search during the naming transition.
- Endometriosis.
- Heavy / painful periods, fibroids and adenomyosis.
- PMS / PMDD.
- Perimenopause / menopause.
- Thyroid conditions.
- Iron deficiency / anaemia.
- Postpartum depression, anxiety and urgent postpartum psychosis information.

Each topic follows a consistent pattern: what it is, signs to discuss, what may help, when to seek assessment, what is uncertain, named reviewer, sources and review date.

The design must never imply that clicking a card identifies a diagnosis. No fertility claims, hormone-balancing promises, supplement stacks, medication doses, weight-loss messaging or one-size-fits-all diet advice. Use “what may help” rather than “how to cure / fix / balance hormones”.

Include the PMOS and midlife cognition research spotlight with the observational-evidence caveat. The brain-health study cannot be presented as proof of causation, brain damage or future dementia.