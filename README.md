# NotesKeeper

Local Apple Notes organizer and backup tool for macOS. Reads notes safely, backs them up to SQLite, exports to Markdown, detects shopping lists and duplicates, and proposes changes for review before anything in Apple Notes is touched.

Current state: the Python scaffold is in place. The package installs, the `noteskeeper` CLI starts, YAML config loading works, and baseline tests cover the safe defaults. The Apple Notes reader, database engine, Markdown export, processors, review reports, and guarded apply implementation are still pending.

---

## What It Does

NotesKeeper runs on a Mac mini 2012 that has access to the source Apple Notes library. It works in read-only mode by default. Any modification to Apple Notes requires an explicit apply command with writes enabled in the config.

Core capabilities in V1:

- Read Apple Notes metadata and content through a safe ingestion path
- Back up notes and all metadata to a local SQLite database
- Track note versions by content hash so history is never overwritten
- Export backed-up notes to a Markdown vault with YAML frontmatter
- Detect and normalize shopping lists into sorted checkbox format
- Detect exact and near-duplicate notes and checklist items
- Group related notes into consolidation candidates
- Extract action items and convert them to checkbox proposals
- Detect date-sensitive phrases and surface them in a review report
- Auto-classify notes into categories such as Home, Work, Travel, or Shopping Lists
- Flag stale or archive-safe notes as candidates for review
- Inventory URLs, file attachments, and link metadata
- Clean up voice dictation notes and convert them to structured lists
- Stage all proposed changes for manual review before applying anything

---

## Deployment Target

This project runs on and is designed for the **Apple Mac mini 2012**.

- The Mac mini natively supports up to macOS El Capitan (10.11). With unofficial community patches it can reach Monterey (12).
- El Capitan ships with Python 2.7 only. A separate Python 3 install is required before any scaffold work begins.
- All Apple Notes ingestion must be validated on this machine. Development planning can happen from any OS but the tool only runs on macOS.
- Before starting the scaffold, confirm the actual macOS version and Python version on the machine.

---

## Safety Model

NotesKeeper is built around three safety rules that cannot be bypassed without explicit configuration changes.

**Rule 1: Never delete Apple Notes automatically.**
No command in NotesKeeper deletes a note from Apple Notes. Archive candidates and duplicate detections create proposals only.

**Rule 2: Never modify Apple Notes during any read or detection pass.**
Scan, backup, export, and all detection commands are read-only against the source. They write only to the local SQLite database and the local Markdown vault.

**Rule 3: Apply is the only write path, and it is disabled by default.**
The `noteskeeper apply --change-id <id>` command is the only path that can write back to Apple Notes. It requires `apple_notes.allow_writes: true` in the config file. It verifies the original content hash before writing. It records an audit log entry. It supports `--dry-run`.

Every proposed change is stored in SQLite with status tracking. Nothing gets applied until it is reviewed and explicitly approved.

---

## Planned Feature Set

### Apple Notes Ingestion

Reads notes through one of these safe paths:

- AppleScript (preferred for V1)
- Exported Notes folder
- Direct SQLite read of `NoteStore.sqlite` (highest risk, schema is undocumented and version-specific; avoid unless AppleScript is unavailable)

Captured fields per note: title, body, folder, created date, modified date, Apple Notes identifier, checklist items, links, and attachment metadata.

### SQLite Backup Engine

Stores everything in a local SQLite database. Tables include:

```
notes               folders             tags
note_tags           checklist_items     attachments
links               note_versions       processing_runs
consolidation_groups                    consolidation_group_notes
shopping_lists      shopping_list_items proposed_changes
```

Each note gets a content hash. When a note changes, a new row is added to `note_versions`. History is never overwritten.

### Markdown Export

Exports backed-up notes to a configurable local vault path. Each note becomes a Markdown file with YAML frontmatter:

```yaml
title: Walmart List
folder: Shopping
created: 2026-06-10
modified: 2026-06-10
category: Shopping Lists
tags:
  - grocery
  - walmart
source: apple-notes
content_hash: abc123
```

Folder structure mirrors detected categories:

```
NotesVault/
  AI/
  Travel/
  Home/
  Work/
  Shopping Lists/
  Projects/
  Archive/
  Review/
```

### Shopping List Processor

Detects shopping lists by title keywords (Walmart, Kroger, Costco, Grocery, etc.), body shape, and checklist formatting. For each detected list:

- Extracts items
- Removes duplicates
- Normalizes capitalization
- Preserves quantities
- Sorts alphabetically
- Converts to checkbox format

Input:

```
Walmart List
milk
bread
apples 2 bags
eggs
bananas
```

Proposed output:

```markdown
# Walmart List

- [ ] Apples 2 bags
- [ ] Bananas
- [ ] Bread
- [ ] Eggs
- [ ] Milk
```

The processor creates a proposed change. It does not modify the source note.

### Duplicate Detection

Finds:

- Exact duplicate note bodies by content hash
- Notes with identical titles and similar bodies
- Repeated checklist items within a note
- Repeated items across shopping lists

Results go to the review report. No deletions happen automatically.

### Consolidation Engine

Groups related notes by title similarity and keyword overlap. Generates a merged master note proposal that preserves all source sections and adds source references. Source notes are never deleted.

### Task Extraction

Detects action items inside notes and converts them to checkbox proposed changes. Dates in action items are preserved as written.

### Date and Reminder Detection

Flags notes containing date-sensitive phrases such as "appointment", "renew by", "call Friday", or "next week". Surfaces them in the review report. No Calendar or Reminders writes in V1.

### Category Auto-Detection

Classifies notes into categories stored in SQL and Markdown frontmatter:

```
AI, Automation, Travel, Fitness, Health,
Home, Work, Patents, Shopping Lists,
Ideas, Reference, Personal, Archive
```

### Archive Candidate Detection

Flags notes not modified in 180 or more days, empty or near-empty notes, and notes with completed checklists. Creates proposed changes. Nothing is archived automatically.

### Review Reports

Generates Markdown reports in the configured review output path:

```
Review/
  shopping-list-cleanups.md
  consolidation-candidates.md
  duplicate-candidates.md
  archive-candidates.md
  task-candidates.md
  processing-summary.md
```

Each report includes change IDs so a specific proposal can be approved and applied by ID.

---

## Implementation Guide

The project is implemented in phases using a sequence of prompt files stored locally in `prompts/`. That folder is git-ignored and local to each machine. The prompt build sequence is:

| Step | File | What It Builds |
|------|------|----------------|
| 01 | `01-Scaffold-Python-Project.md` | Python package, CLI entry point, config loader, logging, pytest |
| 02 | `02-Build-SQLite-Backup-Engine.md` | Database schema, migrations, repositories, content hashing, versioning |
| 03 | `03-Build-Apple-Notes-Reader.md` | Read-only Apple Notes ingestion, scan and backup commands |
| 04 | `04-Build-Markdown-Export.md` | Markdown vault export with YAML frontmatter |
| 05 | `05-Build-Proposed-Changes-System.md` | Safety layer, proposed changes table, audit log |
| 06 | `06-Build-Shopping-List-Processor.md` | Shopping list detection, normalization, proposals |
| 07 | `07-Build-Duplicate-Detection.md` | Exact and near-duplicate detection |
| 08 | `08-Build-Consolidation-Engine.md` | Related note grouping and merge proposals |
| 09 | `09-Build-Review-Reports.md` | Markdown review report generation |
| 10 | `10-Build-Apply-Command.md` | Guarded apply command with hash verification |
| 11 | `11-Complete-Docs-And-Release-Readiness.md` | Docs, examples, and V1 release readiness check |

Each prompt leaves the repo in a working state with passing tests before the next one runs.

The Proposed Changes System (step 05) intentionally comes before any processor (step 06 onward). All processors that generate note modification candidates depend on the proposed changes layer.

### Current Setup

From the repo root:

```bash
python -m pip install -e ".[dev]"
python -m pytest
noteskeeper --help
noteskeeper status --dry-run
```

On the Mac mini, use `python3` if `python` points to Python 2.

### Mac Mini Checks Before Apple Notes Ingestion

Confirm these on the Mac mini before starting prompt 03:

```bash
sw_vers                  # confirm macOS version
python3 --version        # confirm Python 3 is installed
```

If Python 3 is not installed, install it via Homebrew or the python.org installer before Apple Notes ingestion work begins.

---

## CLI

```bash
noteskeeper init
noteskeeper scan
noteskeeper backup
noteskeeper export-markdown
noteskeeper detect-shopping-lists
noteskeeper detect-duplicates
noteskeeper detect-consolidation
noteskeeper review
noteskeeper apply --change-id 123
noteskeeper status
```

Every command accepts:

```bash
--dry-run        # show what would happen without writing
--verbose        # detailed output
--config ./config.yaml
```

Implemented now:

- `noteskeeper --help`
- `noteskeeper init --dry-run`
- `noteskeeper status --dry-run`
- dry run placeholders for `scan`, `backup`, `export-markdown`, and `review`
- guarded placeholder for `apply --change-id <id>`

Pending:

- real Apple Notes scan
- SQLite backup writes
- Markdown export
- review report generation
- approved apply behavior

---

## Configuration

The config file is YAML. The default path is `./config.yaml`. Override with `--config`.

```yaml
apple_notes:
  read_method: applescript    # applescript | exported_folder | sqlite_direct
  allow_writes: false         # must be true to run noteskeeper apply

backup:
  database_path: ./data/noteskeeper.sqlite3
  markdown_vault_path: ~/OneDrive/NotesVault

processing:
  stale_days: 180
  enable_ai: false
  enable_embeddings: false
  shopping_list_sort: alphabetical
  preserve_originals: true

review:
  output_path: ./review
  require_manual_approval: true
```

`allow_writes` is `false` by default. Set it to `true` only when you intend to run `noteskeeper apply`.

---

## Repository Files

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `AGENTS.md` | Rules for agent-assisted repo work |
| `assessment.md` | Current project status, risks, open decisions, and next actions |
| `CHANGELOG.md` | Shipped change history |
| `GITHUB_SPEC.md` | Detailed repo spec, CLI reference, validation commands, and limitations |
| `pyproject.toml` | Python package metadata, CLI entry point, and pytest settings |
| `config.example.yaml` | Example safe default config |
| `src/noteskeeper/` | Python package source |
| `tests/` | Baseline pytest suite |
| `future-upgrades.md` | Planned upgrades in three tiers |
| `completed-upgrades.md` | Completed work with dates and validation notes |
| `prompts/` | Local-only build prompt sequence (git-ignored, not present after cloning) |

---

## V1 Non-Goals

These are explicitly out of scope for V1:

- Automatic deletion of any Apple Note
- Automatic Calendar event creation
- Automatic Reminders creation
- Cloud sync service
- Web UI
- Mobile app
- Required LLM or AI dependency
- Required embedding database

These are tracked as Tier 3 items in `future-upgrades.md`.

---

## Repository Maintenance Rules

Any change to this repo must update `assessment.md`. Every shipped change must be logged in `CHANGELOG.md`. When an upgrade is implemented, move it from `future-upgrades.md` to `completed-upgrades.md` and log the same change in `CHANGELOG.md`.

Do not close a repo change with stale assessment, changelog, or upgrade tracking files.
