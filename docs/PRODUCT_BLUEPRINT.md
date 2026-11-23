# Product Blueprint — A Place to Begin

## Product role
An India-first, multilingual mental-wellbeing information and help-navigation experience. It offers a low-pressure first visit, reviewed information, optional creative activities, a women's-health information corner, and routes to human support. It is not a treatment app, diagnostic tool, emergency channel or AI companion.

## Experience principle
**You do not have to figure everything out today.**

Primary flow: **Arrive → Choose → Explore → Pause or reflect → Find support.** Visitors can skip each step, leave at any time and read information without signing up.

## Main information architecture
1. **Home / first visit:** clear service boundary, public support route and non-demanding welcome.
2. **Explore:** overthinking, stress, sleep, relationships, first appointment and supporter guidance.
3. **A small pause:** optional, non-clinical prompts; no forced breathwork or countdown.
4. **Gentle activities:** private thought unload, garden marker, untimed matching puzzle, creative colour note and Night Help.
5. **Resource shelf:** links to original trusted public resources; future audio/video needs captions and transcripts.
6. **Women's health:** PMOS (formerly PCOS), endometriosis, heavy/painful periods, PMS/PMDD, perimenopause/menopause, thyroid, iron deficiency/anaemia and postpartum depression/anxiety with psychosis red flags.
7. **Find support:** Tele-MANAS and emergency information with source and verification responsibility.
8. **Community plan:** future moderated peer-support concept only; no live user posts or direct messages in v1.
9. **Our promises:** privacy, boundaries, reviewers, sources and correction governance.

## Prototype interactions
### Overthinking Unload
A visitor may enter a thought and reveal reflection prompts. The note is not interpreted, classified, diagnosed, uploaded or retained. Prompts are reflective options, not CBT treatment or a clinical assessment.

### The Little Garden
A visitor adds a small visual marker. No streaks, points, ranking, progress judgement or saved state.

### Puzzle Sanctuary
A four-card matching game is untimed and has no score or leaderboard. It is optional entertainment, not a treatment claim.

### Creative Studio
A visitor chooses a colour and can add a short note. This is a temporary visual expression area, not an assessment.

### Night Help
A low-stimulation route to optional pause choices and human support. It does not claim to manage a crisis.

## Women's-health content governance
The supplied Women's Health Research and Content Plan is the authoritative content brief. Keep current terminology and caveats:
- Display **PMOS (formerly PCOS)** during the terminology transition and keep both terms searchable.
- Do not infer that the name change automatically changes diagnostic criteria or every care recommendation.
- Describe midlife cognition findings as observational associations; do not imply causation, brain damage or an individual prognosis.
- Do not state that particular foods, supplements, tea or activity “balance hormones” or cure PMOS.
- Distinguish symptoms, what may help, when to seek assessment and uncertainty.
- Do not recommend individual medication, dose or supplement regimen.
- Include postpartum psychosis as an urgent medical situation requiring same-day/emergency assessment.
- Every patient-facing article needs a qualified reviewer, review date, next review date, citations and language review.

## Community concept and launch gate
Potential circles include overthinking, anxiety/panic, loneliness, grief, relationships, burnout, women's health and everyday wins. Before any community launch: trained human moderators, report/block, content warnings, escalation plans, safeguarding policy, privacy review, clear peer-support boundaries and lived-experience co-design. No algorithmic amplification of distress, follower counts or popularity sorting.

## Visual direction
Preserve the uploaded design system: warm paper, forest green, sage, pale blue, lilac and clay; editorial serif headings; system-first body type; simple garden-path metaphor; static decorative Kiran light character (provisional). Avoid stereotyped pink women's-health branding, forced animation, autoplay, dark clinical dashboards and borrowed competitor artwork.

## Roadmap
- **Current prototype:** first visit, activities, topic cards, source-based women's-health corner, support route and safety notes.
- **Next design iteration:** guided paths for sleep, asking for help, preparing for appointments and understanding difficult feelings; accessible worksheets and original audio/video with transcripts, clinician review and licensing.
- **Before public pilot:** clinical review, native-language review (Hindi, Marathi, Romanised Hindi), lived-experience co-design, WCAG 2.2 AA audit, device testing, privacy/security review, crisis-route verification, correction process and content expiry/review tracking.
- **Later, only after operational readiness:** moderated peer community and professional directory. No AI companion or sensitive-data collection is included in this prototype.

## Success measures
Measure whether visitors can find a relevant route, understand service boundaries, use controls with keyboard/screen readers, locate human support and understand privacy. Do not optimise for time-on-site, daily streaks, disclosure volume or repeated engagement.


## Relationships corner (added 24 November 2026)

A separate `relationships.html` page is linked from the home navigation and Explore card. It provides plain-language education on attachment protest, attachment anxiety/avoidance dimensions, pursue–withdraw interaction, conflict repair, boundaries, consent, digital trust, breakups and family pressure.

Two original, unvalidated reflection quizzes show only behaviours a visitor marked Sometimes/Often. They provide no score, clinical cutoff, attachment identity, partner score, compatibility result or stay/leave advice. Answers remain in page memory only and are not stored or transmitted.

A non-scored safety check appears before quiz/communication content. Any Yes or Not sure about fear, control, sexual pressure, threats, stalking or physical harm routes to private support and away from joint repair exercises. It cannot certify that a relationship is safe.

See `docs/RELATIONSHIPS_RESEARCH.md`, `docs/RELATIONSHIP_QUIZ_SPEC.md` and root `SAFETY.md`. A qualified clinician and a domestic-violence/safeguarding specialist must approve this content before public release.


## Shared health-topic pattern (24 November 2026)

New pages use a consistent structure: what the term means; how it may feel; what may help; when to seek support; and what remains uncertain. See `wellbeing.html` for depression, anxiety, panic, acute stress surges, trauma/PTSD, rumination, sleep, work burnout, grief/loneliness and OCD-related experiences. The women's-health corner uses the same visitor-facing pattern for PMOS, endometriosis, menstrual issues, PMS/PMDD, menopause, thyroid, anaemia and postpartum mental health.

Use “what may help”, not a cure promise. No self-diagnosis, medication directions or supplement regimens. Research/terminology and clinical caveats are in `docs/MENTAL_WELLBEING_AND_WOMENS_HEALTH_RESEARCH.md`. Universal writing requirements: `docs/HEALTH_TOPIC_CONTENT_STANDARD.md`.


## Shared health-topic content pattern
Across mental wellbeing and women's health, every topic should explain:
- How it may feel day to day.
- What may help, separating supportive habits from evidence-based care.
- When to seek professional or urgent support.
- What remains uncertain where evidence is emerging or mixed.

`wellbeing.html` covers depression, anxiety, panic, acute stress surges, trauma/PTSD, rumination, sleep, burnout, grief and OCD-related experiences. The women's-health corner uses the same structure for PMOS, endometriosis, menstrual concerns, PMS/PMDD, menopause, thyroid, anaemia and postpartum mental health. This is education and help navigation, not diagnosis or a treatment plan.

## 40-concept relationship library
The separate relationship page contains all 40 concepts from the uploaded research report appendix, each with how it may feel, what may help and when to seek support. The library has client-side search and no diagnostic scores. Three optional reflection quizzes remain separate from the non-scored safety check.


## Reading library
A separate `reading-library.html` page provides source-linked open resources, licence information and legitimate publisher/library routes for copyrighted attachment books. Aaramora does not bypass paywalls or mirror unlicensed scans. Each resource shows whether it is CC BY, CC BY-NC-SA, or publisher/library access only.
