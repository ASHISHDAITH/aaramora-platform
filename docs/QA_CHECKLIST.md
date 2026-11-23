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
- [ ] Sacred-text cards identify the exact source institution and distinguish original-language text from translations, commentaries and digital editions.
- [ ] Tanzil Quran text is kept verbatim with its required source notice; QuranEnc translation conditions are checked per version.
- [ ] Sikher translation/transliteration rights are checked at item level, not inferred from software licensing.
- [ ] Public-domain claims for Project Gutenberg editions include the relevant territory caveat and point to ebook landing pages.
- [ ] World English Bible naming and alteration conditions are preserved.
- [ ] DOAB metadata permissions are not presented as permission to republish the listed books; Open Library borrow controls are respected.
- [ ] The reading-library hero photograph includes photographer/source credit and the original Aaramora quote is not misattributed.
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


## Yoga and breath page release gate
- [ ] Yoga/depression review summaries name population, sample size, comparator and timeframe.
- [ ] Do not imply benefit versus usual care means superiority over active treatments.
- [ ] Study-level evidence badges use the review's own certainty wording; no invented A/B/C/D grade.
- [ ] Page says the specific AARAMORA practices have not been tested as treatments.
- [ ] No promise that yoga cures depression, anxiety, trauma, insomnia or other conditions.
- [ ] No forced deep breathing, rapid breathing, breath retention, rigid counts, extreme poses, eyes-closed requirements or mandatory completion.
- [ ] Clear stop guidance for dizziness, faintness, unusual breathlessness, pain or increased distress.
- [ ] Pregnancy, older age, injuries and medical conditions include advice to seek individual modification guidance.
- [ ] Hindi/Marathi scripts have native-speaker review, clinician review and qualified yoga-professional review before recording.
- [ ] Each audio has an equivalent transcript, visible play/pause/stop, no autoplay and no tracking.
- [ ] No audio file is described as published until the actual reviewed recording is committed and tested.
- [ ] WHO stress-guide derivatives follow CC BY-NC-SA 3.0 IGO, attribution, translation disclaimer and no-endorsement/logo rules.


## Multilingual Reading Library and preservation checks
- [ ] All nine original reading-library sections remain available after catalogue additions.
- [ ] The sticky header has an opaque paper background; no text bleeds through behind navigation.
- [ ] Tele-MANAS 14416 and Emergency 112 are visually grouped on desktop and mobile.
- [ ] Catalogue language filters include the 22 Eighth Schedule languages as a separately labelled constitutional group.
- [ ] Additional Indian and global language filters are labelled as a growing discovery set, not a complete list of all languages.
- [ ] NDLI language tags link to NDLI's current browse facets and its item-specific provider/access rules.
- [ ] Heritage Scripture Server's 11 script options are described as scripts, not mislabelled as 11 translated languages.
- [ ] GRETIL's scholarly-reference-only notice, non-commercial restriction and original-rightsholder copyright are retained.
- [ ] BaniDB remains source-linked only; do not integrate its data until the current service terms and all obligations are reviewed and accepted.
- [ ] Every catalogue record has source, access URL, rights statement, language scope, accessibility notes, verification date and next-review date.
- [ ] Catalogue JSON passes `python scripts/check_catalogue.py` and all tests pass.
- [ ] Weekly metadata-only link-check workflow runs; 403/429/5xx or transient network blocks are reported as inconclusive, not falsely marked dead.
- [ ] The new catalogue never hides or replaces the original static book cards when JavaScript or the JSON file fails.

## Individual multilingual editions · editorial review gate
- [ ] Hindi Ramcharitmanas record remains linked to its exact Hindi Wikisource page; exact source edition and scan rights checked before mirroring.
- [ ] Marathi Jnaneshwari record preserves the source warning about duplicated chapter/passage; compare with a scholarly printed edition before quoting.
- [ ] Bengali Gitanjali 1913 record distinguishes original Bengali edition, English translations, US public-domain statement and other territories.
- [ ] Punjabi Guru Granth Sahib record identifies one selected folio only; separate contributed transcription licence from the underlying scan/source edition.
- [ ] Urdu Diwan-e-Ghalib record separates Wikisource contribution licence from source edition/images.
- [ ] Odia Bhagabata record clearly identifies first Skandha only.
- [ ] Tamil Tirukkural record preserves Project Madurai's full-header redistribution condition.
- [ ] Gujarati, Kannada and Malayalam indexes are identified as catalogues, not blanket reuse permissions.
- [ ] Arabic Safahat free reading/downloading is not represented as a right to mirror Hindawi books.
- [ ] Project Gutenberg French, German, Spanish and Portuguese records keep the USA-specific public-domain caveat.
- [ ] Each catalogue record shows scripts separately from languages where script information is known.
- [ ] Every entry shows native-language, cultural-context and accessibility review status; do not mark pending reviews complete without named human reviewers.
- [ ] Native-language reviewers check script rendering, diacritics, OCR/transcription quality, edition fidelity and search aliases.
- [ ] Religious/tradition reviewers approve descriptions and sacred-use wording before editorial promotion.
