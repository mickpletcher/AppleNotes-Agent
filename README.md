# AppleNotes-Agent

## Overview

AppleNotes-Agent is the working name for NotesKeeper, an AI assisted Apple Notes organization and knowledge management project. The goal is to keep Apple Notes organized, searchable, backed up, and safe to modify while preserving review before any destructive action.

The system is intended to:

- Read Apple Notes data from macOS using a safe, read only ingestion method
- Detect note types such as shopping lists and project notes
- Back up note content and metadata to SQLite
- Export notes to a searchable Markdown vault for local or OneDrive based backup
- Propose changes before modifying source notes

## Project Focus

The initial version is designed around reliability and auditability. It favors inspection, versioning, and history over automation that rewrites notes without review.

Key areas in scope include:

- Apple Notes ingestion and metadata capture
- SQL backup and version history
- Markdown export with frontmatter
- Shopping list normalization and deduplication
- Note consolidation proposals for related content

## Repository Contents

- `prompts/NotesKeeper-Codex-Build-Prompt.md`: the build prompt that defines the project requirements and expected behavior
- `README.md`: this project overview
- `AGENTS.md`: repository maintenance rules for future agent work
- `assessment.md`: current project status, gaps, risks, validation status, and next actions
- `CHANGELOG.md`: shipped change history

## Status

This repository currently captures the project definition and build prompt. It does not yet contain the implementation for the Apple Notes automation pipeline.

Any repo change must update `assessment.md`. Every shipped change must be logged in `CHANGELOG.md`.
