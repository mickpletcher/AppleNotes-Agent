from noteskeeper.cli import main


def test_status_dry_run_uses_safe_defaults(capsys, tmp_path):
    exit_code = main(["status", "--dry-run", "--config", str(tmp_path / "missing.yaml")])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Apple Notes writes enabled: False" in captured.out
    assert "Apple Notes read method: applescript" in captured.out


def test_init_creates_config_from_any_working_directory(capsys, tmp_path, monkeypatch):
    config_path = tmp_path / "config.yaml"
    run_from = tmp_path / "other"
    run_from.mkdir()
    monkeypatch.chdir(run_from)

    exit_code = main(["init", "--config", str(config_path)])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Created starter config" in captured.out
    assert "allow_writes: false" in config_path.read_text(encoding="utf-8")


def test_apply_requires_change_id(capsys, tmp_path):
    exit_code = main(["apply", "--dry-run", "--config", str(tmp_path / "missing.yaml")])

    captured = capsys.readouterr()

    assert exit_code == 2
    assert "apply requires --change-id" in captured.out


def test_scan_dry_run_does_not_require_apple_notes(capsys, tmp_path):
    exit_code = main(["scan", "--dry-run", "--config", str(tmp_path / "missing.yaml")])

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Would run scan" in captured.out
