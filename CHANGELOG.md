# Changelog

## Unreleased

### Upgrade Backlog Removal (2026-06-10)

- Restored `future-upgrades.md` as a local only file and kept it ignored by Git so it will not be pushed.
- Updated the repository docs to reference the local only backlog file again.

### README Expansion (2026-06-10)

- Rewrote `README.md` with a full project overview: safety model, complete V1 feature descriptions, implementation guide with prompt build order table, Mac mini 2012 prerequisites, planned CLI, config reference, repository file index, and V1 non-goals.

### Repo Assessment And Planning Cleanup (2026-06-10)

- Fixed prompt build order: moved Proposed Changes System to prompt 05 and Shopping List Processor to prompt 06 so the safety layer exists before any processor that depends on it.
- Added six missing V1 features to `future-upgrades.md` Tier 2: Task Extraction, Date And Reminder Detection, Project And Category Auto-Detection, Archive Candidate Detection, Link And Attachment Inventory, and Voice Dictation Cleanup.
- Changed all validation code block labels from `powershell` to `bash` across `GITHUB_SPEC.md` and all numbered prompt files (this tool runs on macOS, not Windows).
- Updated `GITHUB_SPEC.md` repo structure to note that `prompts/` is local only and not present after cloning.
- Updated `GITHUB_SPEC.md` Known Limitations with Mac mini 2012 macOS version range, Python 2.7 default on El Capitan, and direct NoteStore.sqlite access risk.
- Updated `assessment.md` Risks and Open Decisions with Mac mini 2012 macOS specifics and direct SQLite ingestion risk.
- Updated `assessment.md` Overall Assessment and Validation Status to reflect the 2026-06-10 review pass.

## [0.1.0] - Planned

Target: Python package scaffold, CLI shell, config loader, logging, and pytest baseline. See `prompts/01-Scaffold-Python-Project.md`.

- Added `GITHUB_SPEC.md` with repo structure, target machine, safety rules, planned CLI, validation commands, limitations, and maintenance rules.
- Added `future-upgrades.md` with three tiers of possible upgrades.
- Added `completed-upgrades.md` with completed planning and setup work.
- Updated `assessment.md` after the full project assessment to reflect the current tracked planning files and remaining gaps.
- Expanded `assessment.md` with file health, risks, open decisions, validation status, and next actions.
- Updated `README.md` to list the spec and upgrade tracking files.
- Documented the Apple Mac mini 2012 as the target machine where the project will reside and where Apple Notes ingestion must be validated.
- Added `AGENTS.md` with required maintenance rules for `assessment.md`, `CHANGELOG.md`, and upgrade tracking files.
- Added `assessment.md` with the current project status, missing work, risks, validation status, and next action.
- Updated `README.md` to document repository maintenance files and the requirement to update `assessment.md` for every repo change.
- Added `prompts/` to `.gitignore` so local prompt drafts do not get pushed to the repo.
- Expanded `README.md` with a project overview for NotesKeeper and the Apple Notes automation scope.
