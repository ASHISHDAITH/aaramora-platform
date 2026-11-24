# First-Visit Design System v2

**Product name:** AARAMORA  
**Tagline:** A gentle place to begin again.  
**Audience:** Adults in India, including people arriving under stress, with limited time, low-end Android devices, constrained data, or a preference for English, Hindi, Marathi or Romanised Hindi.  
**Role:** Mental-health information and help navigation. Not therapy, diagnosis, crisis response or an AI companion.

## Design idea

**A little light along the way.** A quiet, editorial garden-path metaphor with one small static light character, provisionally named Kiran. The illustration helps orient visitors; it does not speak, assess them, collect information or signal progress.

## Visual tokens

| Token | Value | Use |
|---|---|---|
| Paper | `#F6F3EB` | Main background |
| Warm surface | `#FFFEFA` | Cards and reading surfaces |
| Forest | `#20483D` | Primary actions / dark support surface |
| Ink | `#203C34` | Main text |
| Muted ink | `#64746A` | Supporting text |
| Sage | `#DFE9DE` | Calm surfaces |
| Pale blue | `#E2EBE9` | Secondary surfaces |
| Lilac | `#E7E1EA` | Occasional accent |
| Clay | `#EBD8CC` | Warm accent |
| Gold | `#DDBA76` | Small decorative highlight only |  
| Border | `#D9E1D8` | Quiet outlines and dividers |  
| Focus | `#1E5E91` | Visible keyboard focus |

Colours are visual design choices, not treatment or calming claims. Check actual component states for WCAG 2.2 AA contrast. Use 4.5:1 minimum for normal text, 3:1 for large text and relevant non-text UI elements.

## AARAMORA homepage visual direction

The homepage uses an editorial, botanical direction rather than a generic wellness dashboard:
- Warm paper background, deep forest-green text and primary actions, restrained sage, pale blue, muted lilac and clay.
- Large serif hero typography paired with a system-first sans-serif body stack.
- Spacious section rhythm, soft 24–32 px radii, thin green-grey borders and low-contrast shadows.
- Photography is used in three optional pathway cards: journaling, supportive conversation and a clinician visit. Each image has useful alt text, lazy loading and a visible creator/source credit. Stock images must never be presented as AARAMORA members, testimonials or actual staff.
- The hero brand film is the 16:9 AARAMORA master, 33.325 seconds, with native controls, `preload=none`, `playsinline`, a poster and no autoplay. A separate link opens the 9:16 social edit.
- On smaller screens the hero stacks; pathway cards collapse into one column. The video remains 16:9 with native controls.

The current Pexels photographs are externally served image files. They contain no tracking SDK, but visitor browsers make requests to the image host; a later privacy/performance pass may self-host optimized licensed copies. Retain source, creator and licence metadata if images are replaced.

## Simple-first homepage update

The homepage uses progressive disclosure so first-time visitors see fewer choices at once:
- Keep five common destinations visible: Explore, Mental wellbeing, Relationships, Women's health and Find support.
- Group Gentle activities, Guides, Check-ins & planners, Reading library and Our promises inside a clearly labelled “More” menu. All destinations remain available; this is a grouping change, not feature removal.
- Keep the support ribbon visible at the top.
- Use one short explanation and two clear actions in the hero. The lower-priority “See how AARAMORA works” link remains available.
- Show the 16:9 AARAMORA brand film in the hero with native controls. Do not autoplay. The 9:16 edit remains available as a separate link.
- Use direct headings and short descriptions on the three image-led pathways: Write it down, Talk to someone and Find professional help.
- On mobile, the navigation is a compact Menu control. The grouped destinations remain accessible inside the expanded menu.
- Preserve all page sections, tools, routes, support links, language choices and quick exit. A layout simplification must not delete functionality.

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

## Shared navigation and discovery refinements · 24 November 2026

The shared six-link navigation keeps Relationship Corner and Reading Library directly accessible while retaining Get help now, Understand, Tools and Trust. Its mobile panel is keyboard-operable, exposes expanded state, closes on Escape and outside click, and marks the current destination. The homepage adds two non-destructive discovery cards for relationship learning and reading. Reading Library format chips display live counts across Book, Video, Audiobook, Audio, Article, Blog and Image; counts overlap because a source may have multiple types. Existing reading shelves and the 49-record catalogue remain intact. Menu behavior is centralized in `site.js`; pages with a menu must load that shared controller.
