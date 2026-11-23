# Trauma-Informed and Accessibility QA Checklist

## First viewport
- [ ] Visitor can identify what the service does and does not do within 10 seconds.
- [ ] Human support is visible without scrolling, sign-in or quiz completion.
- [ ] User can leave without explaining why.
- [ ] No forced mood rating, diagnostic language or history form.
- [ ] Language selector is understandable and accurate.

## Choice and agency
- [ ] Every optional interaction can be skipped.
- [ ] No forced breathwork, body scan, eyes-closed instruction or countdown.
- [ ] No score, streak, badge, completion meter or guilt reminder.
- [ ] Character is optional and non-interactive.
- [ ] No fake testimonials or invented clinical claims.
- [ ] Story is clearly fictional and does not describe traumatic events.

## Crisis / support routing
- [ ] Tele-MANAS number and details verified against current official source before launch.
- [ ] Emergency 112 details verified against official ERSS before launch.
- [ ] Links tested on Android and iOS.
- [ ] Every route has the platform boundary statement.
- [ ] Crisis/support route works when JavaScript and APIs are unavailable.
- [ ] Every external help link has owner, source, verified date and next-review date.

## Privacy
- [ ] No analytics, pixels, heatmaps or ad trackers on sensitive pages.
- [ ] No personal health text sent to AI or research APIs.
- [ ] Privacy statements match actual network behaviour and storage code.
- [ ] Quick exit is explained accurately: it does not erase history, logs or shared-device records.
- [ ] Private local tools explain save, export, delete and device-sharing limitations before use.

## WCAG 2.2 AA
- [ ] Normal text contrast at least 4.5:1.
- [ ] Large text contrast at least 3:1.
- [ ] Visible keyboard focus and logical tab sequence.
- [ ] Skip link and semantic landmarks.
- [ ] Labels and instructions for every control.
- [ ] Screen reader checks: NVDA, VoiceOver and TalkBack.
- [ ] Zoom to 200% with no content loss or horizontal scroll.
- [ ] Minimum target size follows WCAG 2.2; aim for 44×44 CSS px where feasible.
- [ ] Reduced-motion preference is honoured.
- [ ] No flashing, auto-playing sound, parallax or decorative animation.
- [ ] Colour is never the only way to convey meaning.

## India / language
- [ ] English / Hindi / Marathi / Romanised Hindi reviewed by native speakers.
- [ ] A clinician fluent in target language reviews health and crisis wording where possible.
- [ ] Test scripts, conjuncts, font fallbacks, line-height and wrapping on Android.
- [ ] Full language routing and `lang` metadata verified.
- [ ] Low-end phone and slow-network tests completed.

## Co-design and usability
- [ ] Paid lived-experience contributors influence decisions throughout discovery, design and evaluation.
- [ ] Participants can skip, pause and withdraw without explanation.
- [ ] Do not ask participants to recount trauma to test a homepage.
- [ ] Test find-human-support, find-a-professional, privacy comprehension, language change, text enlargement and leave-page tasks.
- [ ] Include low digital literacy, low bandwidth and small-screen participants.
- [ ] Measure task success, comprehension and sense of control, not time-on-site or disclosure volume.


## Women's Health content gate
- [ ] PMOS (formerly PCOS) terminology checked against current international consensus; PCOS retained for older literature and search.
- [ ] Midlife brain-health evidence described as observational association, not causation or an individual prognosis.
- [ ] PMOS lifestyle content does not claim that walking, green tea, flax, magnesium, vitamin D or a specific diet cures or “balances hormones”.
- [ ] Condition pages separate symptoms, possible causes, what may help, assessment routes and uncertainty.
- [ ] No card interaction implies diagnosis.
- [ ] No individual medication/dose recommendations or supplement stacks.
- [ ] Menstrual bleeding, pelvic pain and postpartum emergency routes reviewed by a women's-health clinician.
- [ ] Postpartum psychosis wording and urgent route clinically reviewed.
- [ ] English, Hindi, Marathi and Romanised Hindi content reviewed by native speakers; health copy also clinically reviewed.
- [ ] Appointment-preparation worksheet does not send private notes to a server, analytics provider or AI service.

## Relationships corner release gate
- [ ] Relationship page reachable from home navigation and Explore card.
- [ ] Attachment protest is explained as a descriptive concept, not a diagnosis.
- [ ] Custom quizzes are explicitly labelled unvalidated; no scores, cutoffs or attachment labels.
- [ ] Safety check appears before communication advice and quizzes.
- [ ] Any Yes or Not sure routes to private safety support, not couple-repair steps.
- [ ] All No results do not claim the relationship is safe.
- [ ] No quiz data is stored, sent, tracked or placed in URLs.
- [ ] No partner scoring, tracking, block bypassing, compatibility verdict or stay/leave advice.
- [ ] Couples communication suggestions are explicitly limited to situations without coercion or fear.
- [ ] 112, 181 and 14416 verified against official sources before launch; re-check Women Helpline State/UT coverage.
- [ ] Clinician and safeguarding specialist approve content and safety logic.
- [ ] Hindi, Marathi and Romanised Hindi translations reviewed by native speakers and clinicians where possible.


## Universal health-topic guide release gate
- [ ] Every condition guide explains what it is, how it may feel, what may help, and when to seek support.
- [ ] Symptoms are not presented as a diagnosis or definitive checklist.
- [ ] Self-care is distinguished from professional treatment.
- [ ] No medicine dose, supplement stack, cure guarantee or individual treatment instruction.
- [ ] Emerging or mixed research is labelled as such and does not imply causation.
- [ ] Stress surge, panic attack, PTSD, OCD and burnout are distinguished accurately.
- [ ] PMOS terminology, PCOS/PCOD aliases and memory/brain-health caveats are checked.
- [ ] Postpartum psychosis is clearly marked as a medical emergency.
- [ ] Every page has named clinical reviewer, sources, review date and expiry.


## Universal health-topic consistency
- [ ] Every mental and women's-health topic uses a consistent how-it-may-feel / what-may-help / when-to-seek-support structure.
- [ ] Symptoms are possible experiences, not diagnostic checklists.
- [ ] Self-care is separated from clinician-delivered treatment.
- [ ] No drug dose, supplement stack, cure guarantee or personalised treatment instruction.
- [ ] Emerging and mixed evidence is identified as uncertain.
- [ ] PMOS/PCOS terminology and cognition caveats are checked.
- [ ] Postpartum psychosis is marked as an emergency requiring same-day assessment.

## 40-concept relationship library
- [ ] All 40 concepts from the uploaded report appendix are present exactly once.
- [ ] Each concept includes how it may feel, what may help and when to seek support.
- [ ] Research dimensions, clinical overlaps, emerging concepts and popular terms are distinguished.
- [ ] Three optional reflection quizzes remain unscored and non-diagnostic.
- [ ] Unanswered safety-check items are not interpreted as No.
- [ ] Coercive control, threats, stalking and violence route to individual safety support.


## Reading library and content licensing
- [ ] Every downloadable/mirrored book has a verified book-level licence, not just a repository root licence.
- [ ] Attribution, licence URI/version and change notices are visible.
- [ ] NonCommercial and ShareAlike conditions are respected.
- [ ] Third-party images, worksheets, charts and cover rights are checked separately.
- [ ] Copyrighted titles link to official publisher or lawful library access, never unauthorised mirrors.
- [ ] Public GitHub access is not treated as permission to copy bundled books.
- [ ] Re-check official source and edition before publishing any download link.

- [ ] OpenStax Psychology 2e uses current CC BY-NC-SA 4.0 publisher wording and AI-ingestion restriction.
- [ ] BCcampus Capacity to Connect attribution and recommended original-source statement accompany any mirror.
- [ ] Noba modules and Open Oregon textbook show their non-commercial ShareAlike terms.
- [ ] Reading resources link to official publisher pages and direct publisher/repository downloads only.


## Women's-health card consistency
- [ ] All eight women's-health cards include How might this feel day to day? and What may help?
- [ ] All eight cards include a When to seek support section; urgent red flags remain explicit.
- [ ] PMOS mood/cognition information is evidence-qualified and does not claim causation or brain damage.
- [ ] PMOS/PCOS and PCOD wording reflects current naming while preserving familiar search terms.


## Automated test execution
- [ ] GitHub Actions content-checks workflow runs on pushes and pull requests.
- [ ] `python -m unittest discover -s tests -p 'check_*.py' -v` passes before release.


## Inline script syntax
- [ ] Every inline JavaScript block on index, wellbeing, relationships, reading-library and check-ins pages passes `node --check` in CI.
