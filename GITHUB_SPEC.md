# GitHub Spec

## Project

AppleNotes-Agent is the repository for NotesKeeper.

NotesKeeper is a local Apple Notes organization and backup tool. It is intended to run on a Mac mini that has access to the source Apple Notes data. The minimum hardware target is Mac mini 2012, with newer Intel and Apple Silicon Mac minis also in scope.

## Current Status

The repository has the initial Python scaffold.

Implemented:

- installable `noteskeeper` package
- `noteskeeper` CLI entry point
- YAML config loader with safe defaults
- logging setup
- baseline pytest suite
- dry run safe CLI placeholders

Not implemented yet:

- SQLite backup engine
- Apple Notes ingestion
- Markdown export
- proposed changes system
- processors
- review reports
- guarded write implementation

## Current Repo Structure

```text
AppleNotes-Agent/
├── AGENTS.md
├── assessment.md
├── CHANGELOG.md
├── completed-upgrades.md
├── config.example.yaml
├── future-upgrades.md   # local only, git-ignored
├── GITHUB_SPEC.md
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── noteskeeper/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       └── logging_config.py
├── tests/
│   ├── test_cli.py
│   └── test_config.py
└── prompts/           # local only, git-ignored
```

The `prompts/` folder is local only and ignored by Git. It will not be present after cloning.
The `future-upgrades.md` file is also local only and ignored by Git.

## Compatibility Target

- Mac mini 2012 or newer.
- Minimum hardware target: Mac mini 2012.
- Newer Intel Mac minis are in scope.
- Apple Silicon Mac minis are in scope when Python dependencies install cleanly.
- Apple Notes access must be validated on the target Mac mini.
- Development planning can happen from Windows.
- Runtime assumptions must be confirmed against the actual macOS and Python versions on the target Mac mini before implementation choices are locked.
- NotesKeeper requires Python 3.9 or newer.

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

Every command should support:

```bash
--dry-run
--verbose
--config ./config.yaml
```

Current behavior:

- `init --dry-run` reports the config file that would be created.
- `init` creates a starter config from `config.example.yaml` when one does not exist.
- `status --dry-run` prints safe default runtime settings.
- `scan`, `backup`, `export-markdown`, and `review` are dry run placeholders.
- `apply` requires `--change-id`; non dry run apply remains blocked unless `apple_notes.allow_writes` is true.

## Validation

Baseline validation:

```bash
python -m pip install -e ".[dev]"
python -m pytest
noteskeeper --help
noteskeeper status --dry-run
```

On the Mac mini, use `python3` if `python` points to Python 2.

Mac specific Apple Notes ingestion must still be validated on the Mac mini.

## Known Limitations

- Only the initial scaffold exists.
- Operational commands are placeholders except `init` and `status`.
- Apple Notes ingestion behavior has not been validated on the Mac mini.
- The Mac mini 2012 natively supports up to macOS El Capitan (10.11). Unofficial patches may enable newer macOS releases. El Capitan ships with Python 2.7 only. Python 3.9 or newer requires a manual install. The actual macOS version must be confirmed on the target Mac before Apple Notes ingestion choices are finalized.
- Newer Mac minis may expose different Apple Notes and AppleScript behavior depending on macOS version.
- Direct SQLite access to `~/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite` is the highest-risk ingestion option because Apple's Notes schema is undocumented and changes between macOS versions. Prefer AppleScript or exported folder ingestion for V1.
- AI, embeddings, web UI, mobile app, cloud sync, calendar creation, and reminder creation are out of V1 scope.

## Maintenance Rules

- Keep this file current when repo structure, setup, CLI behavior, validation commands, safety rules, or limitations change.
- Keep `assessment.md` current after every repo change.
- Keep `future-upgrades.md`, `completed-upgrades.md`, and `CHANGELOG.md` synchronized.
