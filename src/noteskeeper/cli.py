from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any, Callable

import yaml

from noteskeeper.config import DEFAULT_CONFIG, load_config
from noteskeeper.logging_config import configure_logging


CommandHandler = Callable[[argparse.Namespace, dict[str, Any]], int]


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose)
    config = load_config(args.config)
    return args.handler(args, config)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="noteskeeper",
        description="Safe local Apple Notes organizer and backup tool.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    _add_command(subparsers, "init", _handle_init, "Create a starter config file.")
    _add_command(subparsers, "scan", _handle_placeholder, "Scan Apple Notes in read only mode.")
    _add_command(subparsers, "backup", _handle_placeholder, "Back up scanned notes to SQLite.")
    _add_command(subparsers, "export-markdown", _handle_placeholder, "Export backed up notes to Markdown.")
    _add_command(subparsers, "review", _handle_placeholder, "Generate review reports.")

    apply_parser = _add_command(
        subparsers,
        "apply",
        _handle_apply,
        "Apply one approved change when writes are enabled.",
    )
    apply_parser.add_argument("--change-id", help="Approved proposed change ID to apply.")

    _add_command(subparsers, "status", _handle_status, "Show current NotesKeeper status.")
    return parser


def _add_command(
    subparsers: argparse._SubParsersAction,
    name: str,
    handler: CommandHandler,
    help_text: str,
) -> argparse.ArgumentParser:
    parser = subparsers.add_parser(name, help=help_text, description=help_text)
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without writing.")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output.")
    parser.add_argument("--config", default="config.yaml", help="Path to the YAML config file.")
    parser.set_defaults(handler=handler)
    return parser


def _handle_init(args: argparse.Namespace, config: dict[str, Any]) -> int:
    target = Path(args.config)
    if args.dry_run:
        print(f"Would create starter config at {target}")
        return 0

    if target.exists():
        print(f"Config already exists: {target}")
        return 0

    target.write_text(yaml.safe_dump(DEFAULT_CONFIG, sort_keys=False), encoding="utf-8")
    print(f"Created starter config: {target}")
    return 0


def _handle_status(args: argparse.Namespace, config: dict[str, Any]) -> int:
    writes_enabled = bool(config["apple_notes"]["allow_writes"])
    print("NotesKeeper status")
    print(f"Config path: {args.config}")
    print(f"Dry run: {args.dry_run}")
    print(f"Apple Notes read method: {config['apple_notes']['read_method']}")
    print(f"Apple Notes writes enabled: {writes_enabled}")
    print(f"SQLite database path: {config['backup']['database_path']}")
    print(f"Markdown vault path: {config['backup']['markdown_vault_path']}")
    return 0


def _handle_apply(args: argparse.Namespace, config: dict[str, Any]) -> int:
    if not args.change_id:
        print("apply requires --change-id")
        return 2

    if args.dry_run:
        print(f"Would apply approved change {args.change_id}")
        return 0

    if not config["apple_notes"]["allow_writes"]:
        print("Apple Notes writes are disabled. Set apple_notes.allow_writes: true to apply changes.")
        return 1

    print("Apply is not implemented yet.")
    return 1


def _handle_placeholder(args: argparse.Namespace, config: dict[str, Any]) -> int:
    if args.dry_run:
        print(f"Would run {args.command}")
        return 0

    print(f"{args.command} is not implemented yet. Run with --dry-run to verify CLI wiring.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
