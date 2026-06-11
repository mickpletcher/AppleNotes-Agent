# Future Upgrades

This file tracks possible upgrades that have not been implemented yet.

When an upgrade is completed, move it to `completed-upgrades.md` and log the change in `CHANGELOG.md`.

## Tier 1: Near Term Foundation

### Python Project Scaffold

- Purpose: Create the installable NotesKeeper package, CLI shell, config loader, logging, and pytest setup.
- Expected files or components affected: `pyproject.toml`, `config.example.yaml`, `src/noteskeeper/`, `tests/`, `README.md`, `GITHUB_SPEC.md`, `assessment.md`, `CHANGELOG.md`.
- Validation needed: install editable package, run pytest, run `noteskeeper --help`, run `noteskeeper status --dry-run`.
- Status: Pending.

### SQLite Backup Engine

- Purpose: Store notes, metadata, versions, processing runs, and safety records in SQLite.
- Expected files or components affected: `src/noteskeeper/database/`, `src/noteskeeper/utils/hashing.py`, `tests/test_database.py`, docs, assessment, changelog.
- Validation needed: database init, insert and update tests, note version tests.
- Status: Pending.

### Read Only Apple Notes Ingestion

- Purpose: Read Apple Notes data safely from the Mac mini without modifying source notes.
- Expected files or components affected: `src/noteskeeper/apple_notes/`, fixtures, tests, `docs/apple-notes-access.md`.
- Validation needed: fixture tests on Windows and live read only scan on the Mac mini.
- Status: Pending.

### Markdown Export

- Purpose: Export backed up notes to a local Markdown vault with YAML frontmatter.
- Expected files or components affected: `src/noteskeeper/export/markdown.py`, path helpers, export tests, docs.
- Validation needed: deterministic export tests and dry run CLI check.
- Status: Pending.

### Proposed Changes Safety Layer

- Purpose: Stage all modifications before any Apple Notes write path can run.
- Expected files or components affected: `src/noteskeeper/safety/`, database schema, review reports, tests.
- Validation needed: proposed change creation tests, dry run behavior tests, audit log tests.
- Status: Pending.

## Tier 2: Processing And Review

### Shopping List Processor

- Purpose: Detect shopping lists, normalize items, remove duplicates, preserve quantities, and create checkbox proposals.
- Expected files or components affected: `src/noteskeeper/processors/shopping_lists.py`, text helpers, tests, review reports.
- Validation needed: shopping list detection, sorting, quantity preservation, duplicate removal, proposed change tests.
- Status: Pending.

### Duplicate Detection

- Purpose: Find exact and near duplicate notes, checklist items, and shopping list items.
- Expected files or components affected: `src/noteskeeper/processors/duplicates.py`, tests, review reports.
- Validation needed: exact hash duplicate tests, near duplicate tests, duplicate report tests.
- Status: Pending.

### Consolidation Engine

- Purpose: Group related notes and create safe merged note proposals.
- Expected files or components affected: `src/noteskeeper/processors/consolidation.py`, database tables, tests, review reports.
- Validation needed: title similarity tests, keyword grouping tests, merged proposal tests.
- Status: Pending.

### Review Reports

- Purpose: Generate deterministic Markdown reports for all proposed changes and candidates.
- Expected files or components affected: `src/noteskeeper/export/review_reports.py`, review output fixtures, tests.
- Validation needed: report generation tests and dry run CLI output.
- Status: Pending.

### Task Extraction

- Purpose: Detect action items inside notes and convert them into checkbox proposed changes without creating Apple Reminders.
- Expected files or components affected: `src/noteskeeper/processors/tasks.py`, proposed changes, review reports, tests.
- Validation needed: action item detection tests, checkbox conversion tests, proposed change creation tests.
- Status: Pending.

### Date And Reminder Detection

- Purpose: Detect dates and time-sensitive phrases in notes and surface them in the review report. No automatic Calendar or Reminders writes in V1.
- Expected files or components affected: `src/noteskeeper/processors/dates.py`, review reports, tests.
- Validation needed: date phrase detection tests, review report output tests.
- Status: Pending.

### Project And Category Auto-Detection

- Purpose: Automatically classify notes into broad categories such as AI, Travel, Fitness, Health, Home, Work, Shopping Lists, Ideas, and Reference. Store category in SQL and Markdown frontmatter.
- Expected files or components affected: `src/noteskeeper/processors/categories.py`, database schema, Markdown export, tests.
- Validation needed: category detection tests, frontmatter output tests.
- Status: Pending.

### Archive Candidate Detection

- Purpose: Detect notes that are likely stale or archive-safe based on age, emptiness, completed checklists, or duplicate status. Generate proposed changes only, no automatic archiving.
- Expected files or components affected: `src/noteskeeper/processors/archive_candidates.py`, proposed changes, review reports, tests.
- Validation needed: staleness detection tests, proposed change tests, dry run tests.
- Status: Pending.

### Link And Attachment Inventory

- Purpose: Extract and store URLs, domains, file attachment names, types, and sizes from notes into the `links` and `attachments` tables.
- Expected files or components affected: `src/noteskeeper/processors/`, database schema, tests.
- Validation needed: URL extraction tests, attachment metadata tests.
- Status: Pending.

### Voice Dictation Cleanup

- Purpose: Detect notes likely created by Siri or mobile dictation and generate proposed changes that convert unpunctuated runs into checkbox lists.
- Expected files or components affected: `src/noteskeeper/processors/`, proposed changes, review reports, tests.
- Validation needed: dictation detection tests, proposed change output tests, dry run tests.
- Status: Pending.

### Guarded Apply Command

- Purpose: Apply one approved change by ID only when writes are explicitly enabled.
- Expected files or components affected: `src/noteskeeper/apple_notes/applescript_writer.py`, safety layer, CLI, tests.
- Validation needed: dry run apply tests, hash mismatch tests, writes disabled tests.
- Status: Pending.

## Tier 3: Later Expansion

### Search And Query Workflow

- Purpose: Add richer local search across backed up notes and Markdown exports.
- Expected files or components affected: database repositories, CLI, docs, tests.
- Validation needed: search query tests and CLI output tests.
- Status: Pending.

### AI Assisted Classification

- Purpose: Add optional AI classification and summarization without making AI a required dependency.
- Expected files or components affected: processors, config, docs, tests.
- Validation needed: disabled by default tests, mocked provider tests, privacy review.
- Status: Pending.

### Embedding Based Similarity

- Purpose: Improve duplicate and consolidation detection with optional embeddings.
- Expected files or components affected: processors, database schema, config, tests.
- Validation needed: deterministic mocked embedding tests and fallback tests.
- Status: Pending.

### Web Review UI

- Purpose: Provide a local review UI for proposed changes.
- Expected files or components affected: new UI app or local server, review APIs, docs, tests.
- Validation needed: UI workflow tests and safety tests.
- Status: Pending.

### Calendar Or Reminder Integration

- Purpose: Convert approved task or date candidates into Calendar or Reminders entries.
- Expected files or components affected: new integration module, config, safety model, tests.
- Validation needed: dry run tests, explicit approval tests, integration tests on the Mac mini.
- Status: Pending.

