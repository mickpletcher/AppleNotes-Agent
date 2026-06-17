# Completed Upgrades

This file tracks upgrades and repo setup work that have been completed.

When an item is completed, remove or mark it complete in `future-upgrades.md`, add it here, and log the change in `CHANGELOG.md`.

## Completed

### Mac Mini Compatibility Scope

- Completed: 2026-06-17.
- Summary: Updated project compatibility from Mac mini 2012 only to Mac mini 2012 or newer, while keeping the 2012 model as the minimum hardware target.
- Files changed: `README.md`, `GITHUB_SPEC.md`, `assessment.md`, `CHANGELOG.md`, `completed-upgrades.md`.
- Validation performed: Reviewed compatibility references across tracked docs with repo search.

### Python Project Scaffold

- Completed: 2026-06-17.
- Summary: Added the installable NotesKeeper package, CLI entry point, YAML config loader, logging setup, safe example config, and baseline pytest suite.
- Files changed: `pyproject.toml`, `config.example.yaml`, `src/noteskeeper/`, `tests/`, `README.md`, `GITHUB_SPEC.md`, `assessment.md`, `CHANGELOG.md`, `future-upgrades.md`.
- Validation performed: Ran `python -m pip install -e ".[dev]"`, `python -m pytest`, `noteskeeper --help`, and `noteskeeper status --dry-run`.

### Project Overview

- Completed: 2026-06-10.
- Summary: Added the initial NotesKeeper overview, scope, status, and deployment target to `README.md`.
- Files changed: `README.md`.
- Validation performed: Reviewed the tracked README content.

### Repository Maintenance Rules

- Completed: 2026-06-10.
- Summary: Added repo rules requiring `assessment.md` updates for every repo change and `CHANGELOG.md` entries for shipped changes.
- Files changed: `AGENTS.md`, `README.md`, `assessment.md`, `CHANGELOG.md`.
- Validation performed: Searched the repo for `assessment.md` and changelog references.

### Local Prompt Build Sequence

- Completed: 2026-06-10.
- Summary: Added local only build prompts for the planned NotesKeeper implementation sequence.
- Files changed: `prompts/`.
- Validation performed: Verified `prompts/` is ignored by Git.

### Planning And Tracking Files

- Completed: 2026-06-10.
- Summary: Added `GITHUB_SPEC.md`, `future-upgrades.md`, and `completed-upgrades.md` so the repo has tracked planning, upgrade, and completion records before implementation starts.
- Files changed: `GITHUB_SPEC.md`, `future-upgrades.md`, `completed-upgrades.md`, `README.md`, `assessment.md`, `CHANGELOG.md`.
- Validation performed: Reviewed tracked files and confirmed references with repo search.
