# GitHub Spec

## Project

AppleNotes-Agent is the repository for NotesKeeper.

NotesKeeper is a local Apple Notes organization and backup tool. It is intended to run on the Apple Mac mini 2012 machine that has access to the source Apple Notes data.

## Current Status

The repository is in planning and prompt preparation state.

There is no Python implementation yet.

## Current Repo Structure

```text
AppleNotes-Agent/
├── AGENTS.md
├── assessment.md
├── CHANGELOG.md
├── completed-upgrades.md
├── future-upgrades.md   # local only, git-ignored
├── GITHUB_SPEC.md
├── LICENSE
├── README.md
└── prompts/           # local only, git-ignored
```

The `prompts/` folder is local only and ignored by Git. It will not be present after cloning.
The `future-upgrades.md` file is also local only and ignored by Git.

## Deployment Target

- Apple Mac mini 2012.
- Apple Notes access must be validated on the Mac mini.
- Development planning can happen from Windows.
- Runtime assumptions must be confirmed against the actual macOS and Python versions on the Mac mini before implementation choices are locked.

## Planned V1 Scope

- Read Apple Notes data through a safe read only path.
- Back up notes and metadata to SQLite.
- Track note versions with content hashes.
- Export backed up notes to Markdown.
- Detect and normalize shopping lists.
- Detect duplicate notes.
- Detect consolidation candidates.
- Generate review reports.
- Stage proposed changes before any Apple Notes modification.
- Keep Apple Notes writes disabled by default.

## Safety Rules

- Never delete Apple Notes automatically.
- Never modify Apple Notes during scan, backup, export, detection, or review.
- Require an explicit apply command for any source note change.
- Preserve original content before proposing or applying a change.
- Support dry run behavior for all write capable commands.
- Log shipped repo changes in `CHANGELOG.md`.
- Update `assessment.md` after every repo change.

## Planned CLI

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

Every command should support:

```bash
--dry-run
--verbose
--config ./config.yaml
```

## Planned Validation

After the Python scaffold exists, the baseline validation should be run on the Mac mini:

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest
noteskeeper --help
noteskeeper status --dry-run
```

Mac specific Apple Notes ingestion must also be validated on the Mac mini.

## Known Limitations

- No executable implementation exists yet.
- No tests exist yet.
- Apple Notes ingestion behavior has not been validated on the Mac mini.
- The Mac mini 2012 natively supports up to macOS El Capitan (10.11). Unofficial patches may enable up to Monterey (12). El Capitan ships with Python 2.7 only. Python 3 requires a manual install. The actual macOS version must be confirmed on the machine before scaffold choices are finalized.
- Direct SQLite access to `~/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite` is the highest-risk ingestion option because Apple's Notes schema is undocumented and changes between macOS versions. Prefer AppleScript or exported folder ingestion for V1.
- AI, embeddings, web UI, mobile app, cloud sync, calendar creation, and reminder creation are out of V1 scope.

## Maintenance Rules

- Keep this file current when repo structure, setup, CLI behavior, validation commands, safety rules, or limitations change.
- Keep `assessment.md` current after every repo change.
- Keep `future-upgrades.md`, `completed-upgrades.md`, and `CHANGELOG.md` synchronized.

