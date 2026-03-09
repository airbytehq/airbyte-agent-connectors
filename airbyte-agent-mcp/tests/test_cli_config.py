"""Tests for cli_config model."""

import os
from pathlib import Path
from unittest.mock import patch

from airbyte_agent_mcp.models.cli_config import Config, get_config_dir, get_download_dir, get_org_env_path, set_config_dir


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

    def test_default_organization_id_defaults_to_none(self):
        cfg = Config()
        assert cfg.default_organization_id is None

    def test_default_organization_id_save_and_load(self, tmp_path):
        cfg = Config()
        cfg.default_organization_id = "org-abc"
        cfg.save(tmp_path)

        loaded = Config.load(tmp_path)
        assert loaded.default_organization_id == "org-abc"


class TestGetOrgEnvPath:
    def test_returns_correct_path(self):
        original = get_config_dir()
        try:
            set_config_dir(Path("/tmp/test_config"))
            path = get_org_env_path("org-123")
            assert path == Path("/tmp/test_config/orgs/org-123/.env")
        finally:
            set_config_dir(original)

    def test_with_explicit_config_dir(self, tmp_path):
        path = get_org_env_path("org-456", config_dir=tmp_path)
        assert path == tmp_path / "orgs" / "org-456" / ".env"


class TestGetDownloadDir:
    def test_scoped_to_org_when_env_set(self, tmp_path):
        with patch.dict(os.environ, {"AIRBYTE_ORGANIZATION_ID": "org-abc"}):
            path = get_download_dir(config_dir=tmp_path)
        assert path == tmp_path / "orgs" / "org-abc" / "downloads"

    def test_falls_back_when_no_org(self, tmp_path):
        with patch.dict(os.environ, {}, clear=True):
            path = get_download_dir(config_dir=tmp_path)
        assert path == tmp_path / "downloads"

    def test_uses_global_config_dir(self):
        original = get_config_dir()
        try:
            set_config_dir(Path("/tmp/test_config"))
            with patch.dict(os.environ, {"AIRBYTE_ORGANIZATION_ID": "org-xyz"}):
                path = get_download_dir()
            assert path == Path("/tmp/test_config/orgs/org-xyz/downloads")
        finally:
            set_config_dir(original)
