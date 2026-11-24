# RAG corpus ingestion and source-rights policy

**Status:** Default-deny policy. No source is currently approved for chatbot ingestion.  
**Last updated:** 24 November 2026.

## 1. Default rule

Do not scrape websites, crawl whole repositories, download books in bulk, bypass DRM/paywalls/borrowing limits, or ingest a resource because it is visible or downloadable. Keep a link in the Reading Library when its rights do not clearly permit ingestion.

Each exact source item must record:
- title, creator/author, exact edition/version and source URL;
- language/script and territory;
- exact licence/rights notice and version/date checked;
- permitted use (read, source-side download, borrow, reuse with attribution, link-only, or written permission required);
- named content owner, reviewer, review date and expiry;
- whether clinical/safeguarding review is required and completed;
- approval status and immutable source hash where permitted.

## 2. Permitted first-party candidates

- Original AARAMORA-written passages may be considered when the project owns the text and a named reviewer approves any health/safety content.
- Non-clinical navigation/help pages still require a source/rights check and factual owner.
- No first-party text is automatically approved; the corpus manifest starts empty.

## 3. Explicit link-only / no-ingestion register supplied by the project owner

These resources must remain link-only unless the rights holder provides written permission or a separate exact-item review records an explicit lawful basis. Do not ingest text, translations, commentary, audio or files from them by default.

| Resource | Default action | Reason recorded for this project |
|---|---|---|
| OpenStax Psychology 2e | Link only; no AI ingestion without written permission | Its current preface/terms are recorded in the project notes as requiring written permission for AI use |
| SuttaCentral | Link only | Site request against scraping / AI-dataset use |
| CCI workbooks | Link only | Workbook republication rights are restricted |
| Jain eLibrary | Link only | Personal-use restriction recorded in the project notes |
| Sikher and BaniDB translations | Link only | Controlled / item-level terms; BaniDB service terms require a separate review |
| Quran translations | Link only by default | Translation- and edition-specific rights |
| Gita Supersite translations | Link only by default | Translation- and item-specific rights |

This table records project constraints supplied by the owner. It is not a substitute for legal advice or a current licence audit. If a rights holder changes terms, update this register before any ingestion.

## 4. Candidate requiring exact licence verification

**BCcampus guide (CC BY 4.0):** a potential candidate only. Before ingestion, verify the exact title/guide, edition/version, author, on-page licence, attribution details, third-party exclusions and whether the licence applies to the entire text or only selected elements. Until that record exists, keep it out of the corpus.

## 5. Build-time enforcement

The builder uses a default-deny manifest. It excludes entries unless all of these are true:
1. `approvalStatus = "approved"`;
2. `contentStatus = "current"`;
3. a named reviewer and owner are recorded;
4. reviewed date and future expiry are valid;
5. at least one HTTPS source is recorded;
6. the exact licence is one of the explicitly accepted licence values;
7. the local source file exists and resolves inside the repository;
8. the entry is not marked draft, link-only, withdrawn or permission-pending.

The current manifest is empty; therefore the approved index must remain empty.

## 6. Never

- scrape whole sites or repositories;
- circumvent access controls, DRM, paywalls or borrowing limits;
- copy full books, articles, translations or commentaries into AARAMORA;
- assume public-domain status is worldwide;
- infer rights from a search snippet or another edition;
- let retrieved text issue instructions to the assistant;
- put unreviewed health claims into the corpus.
