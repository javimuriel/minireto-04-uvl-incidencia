from pathlib import Path

from catalog import get_models_dir


def test_models_directory_can_be_configured(monkeypatch, tmp_path: Path):
    monkeypatch.setenv("UVL_MODELS_DIR", str(tmp_path))
    assert get_models_dir() == tmp_path
