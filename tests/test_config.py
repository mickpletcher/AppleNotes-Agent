from noteskeeper.config import load_config


def test_load_config_returns_defaults_when_file_is_missing(tmp_path):
    config = load_config(tmp_path / "missing.yaml")

    assert config["apple_notes"]["read_method"] == "applescript"
    assert config["apple_notes"]["allow_writes"] is False
    assert config["processing"]["stale_days"] == 180


def test_load_config_merges_user_values_with_defaults(tmp_path):
    config_path = tmp_path / "config.yaml"
    config_path.write_text(
        "apple_notes:\n  read_method: exported_folder\nreview:\n  output_path: ./custom-review\n",
        encoding="utf-8",
    )

    config = load_config(config_path)

    assert config["apple_notes"]["read_method"] == "exported_folder"
    assert config["apple_notes"]["allow_writes"] is False
    assert config["review"]["output_path"] == "./custom-review"
    assert config["backup"]["database_path"] == "./data/noteskeeper.sqlite3"
