from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml


DEFAULT_CONFIG: dict[str, Any] = {
    "apple_notes": {
        "read_method": "applescript",
        "allow_writes": False,
    },
    "backup": {
        "database_path": "./data/noteskeeper.sqlite3",
        "markdown_vault_path": "~/OneDrive/NotesVault",
    },
    "processing": {
        "stale_days": 180,
        "enable_ai": False,
        "enable_embeddings": False,
        "shopping_list_sort": "alphabetical",
        "preserve_originals": True,
    },
    "review": {
        "output_path": "./review",
        "require_manual_approval": True,
    },
}


def load_config(config_path: str | Path = "config.yaml") -> dict[str, Any]:
    path = Path(config_path)
    config = deepcopy(DEFAULT_CONFIG)

    if not path.exists():
        return config

    with path.open("r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle) or {}

    if not isinstance(loaded, dict):
        raise ValueError(f"Config file must contain a YAML mapping: {path}")

    return _deep_merge(config, loaded)


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            _deep_merge(base[key], value)
        else:
            base[key] = value
    return base
