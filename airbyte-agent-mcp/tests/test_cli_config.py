"""Tests for cli_config model."""

from pathlib import Path

from airbyte_agent_mcp.models.cli_config import Config, get_config_dir, set_config_dir


class TestConfigDir:
    def test_set_and_get(self):
        original = get_config_dir()
        try:
            set_config_dir(Path("/tmp/test_config"))
            assert get_config_dir() == Path("/tmp/test_config")
        finally:
            set_config_dir(original)


class TestConfig:
    def test_default_has_installation_id(self):
        cfg = Config()
        assert cfg.installation_id
        assert len(cfg.installation_id) == 36  # UUID format

    def test_two_defaults_have_different_ids(self):
        a = Config()
        b = Config()
        assert a.installation_id != b.installation_id

    def test_save_and_load(self, tmp_path):
        cfg = Config()
        cfg.save(tmp_path)

        loaded = Config.load(tmp_path)
        assert loaded.installation_id == cfg.installation_id

    def test_load_creates_default_when_missing(self, tmp_path):
        cfg = Config.load(tmp_path)
        assert cfg.installation_id
        # File should now exist
        assert (tmp_path / "config.yaml").exists()

    def test_get_is_alias_for_load(self, tmp_path):
        cfg = Config.get(tmp_path)
        assert cfg.installation_id

    def test_save_creates_directories(self, tmp_path):
        cfg = Config()
        nested = tmp_path / "a" / "b"
        cfg.save(nested)
        assert (nested / "config.yaml").exists()
