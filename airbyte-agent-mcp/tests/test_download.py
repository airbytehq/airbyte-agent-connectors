"""Tests for download handling in mcp_server."""

import asyncio
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

import airbyte_agent_mcp.mcp_server as mcp_mod
from airbyte_agent_mcp.mcp_server import _detect_extension, _handle_download


async def _make_async_gen(chunks: list[bytes]):
    for chunk in chunks:
        yield chunk


@pytest.fixture()
def tmp_download_dir(tmp_path):
    download_dir = tmp_path / "downloads"
    with patch.object(mcp_mod, "get_download_dir", return_value=download_dir):
        yield tmp_path


@pytest.fixture()
def mock_connector():
    connector = MagicMock()
    yield connector


async def _fake_save_download(iterator, path):
    """Simplified save_download that writes bytes to a file."""
    file_path = Path(path).resolve()
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "wb") as f:
        async for chunk in iterator:
            f.write(chunk)
    return file_path


class TestHandleDownload:
    def test_saves_async_generator_to_file(self, tmp_download_dir, mock_connector):
        content = b"fake audio content here"
        mock_connector.execute = AsyncMock(return_value=_make_async_gen([content]))

        with patch.object(mcp_mod, "_get_save_download", return_value=_fake_save_download):
            with patch.object(mcp_mod, "_detect_extension", return_value=""):
                result = asyncio.run(_handle_download("call_audio", "download", {}, mock_connector))

        download = result["download"]
        assert download["entity"] == "call_audio"
        assert download["size_bytes"] == len(content)
        assert Path(download["file_path"]).exists()
        assert Path(download["file_path"]).read_bytes() == content

    def test_returns_metadata_with_correct_structure(self, tmp_download_dir, mock_connector):
        mock_connector.execute = AsyncMock(return_value=_make_async_gen([b"data"]))

        with patch.object(mcp_mod, "_get_save_download", return_value=_fake_save_download):
            with patch.object(mcp_mod, "_detect_extension", return_value=""):
                result = asyncio.run(_handle_download("call_video", "download", {"filter": {"callIds": ["123"]}}, mock_connector))

        assert "download" in result
        download = result["download"]
        assert "file_path" in download
        assert "size_bytes" in download
        assert "entity" in download
        assert "message" in download
        assert download["entity"] == "call_video"

    def test_renames_with_detected_extension(self, tmp_download_dir, mock_connector):
        mock_connector.execute = AsyncMock(return_value=_make_async_gen([b"data"]))

        with patch.object(mcp_mod, "_get_save_download", return_value=_fake_save_download):
            with patch.object(mcp_mod, "_detect_extension", return_value=".mp3"):
                result = asyncio.run(_handle_download("call_audio", "download", {}, mock_connector))

        file_path = result["download"]["file_path"]
        assert file_path.endswith(".mp3")
        assert Path(file_path).exists()

    def test_no_extension_when_unrecognized(self, tmp_download_dir, mock_connector):
        mock_connector.execute = AsyncMock(return_value=_make_async_gen([b"unknown"]))

        with patch.object(mcp_mod, "_get_save_download", return_value=_fake_save_download):
            with patch.object(mcp_mod, "_detect_extension", return_value=""):
                result = asyncio.run(_handle_download("call_audio", "download", {}, mock_connector))

        file_path = result["download"]["file_path"]
        assert "." not in Path(file_path).name

    def test_non_async_generator_falls_through(self, tmp_download_dir, mock_connector):
        dict_result = {"status": "ok", "url": "https://example.com/file.mp3"}
        mock_connector.execute = AsyncMock(return_value=dict_result)

        result = asyncio.run(_handle_download("call_audio", "download", {}, mock_connector))
        assert result == dict_result

    def test_multiple_chunks_concatenated(self, tmp_download_dir, mock_connector):
        chunks = [b"chunk1", b"chunk2", b"chunk3"]
        mock_connector.execute = AsyncMock(return_value=_make_async_gen(chunks))

        with patch.object(mcp_mod, "_get_save_download", return_value=_fake_save_download):
            with patch.object(mcp_mod, "_detect_extension", return_value=""):
                result = asyncio.run(_handle_download("call_audio", "download", {}, mock_connector))

        file_path = Path(result["download"]["file_path"])
        assert file_path.read_bytes() == b"chunk1chunk2chunk3"
        assert result["download"]["size_bytes"] == len(b"chunk1chunk2chunk3")

    def test_download_dir_created(self, tmp_download_dir, mock_connector):
        mock_connector.execute = AsyncMock(return_value=_make_async_gen([b"data"]))

        with patch.object(mcp_mod, "_get_save_download", return_value=_fake_save_download):
            with patch.object(mcp_mod, "_detect_extension", return_value=""):
                result = asyncio.run(_handle_download("call_audio", "download", {}, mock_connector))

        download_dir = tmp_download_dir / "downloads"
        assert download_dir.exists()
        assert Path(result["download"]["file_path"]).parent == download_dir

    def test_save_download_error_propagates(self, tmp_download_dir, mock_connector):
        mock_connector.execute = AsyncMock(return_value=_make_async_gen([b"data"]))

        async def failing_save(iterator, path):
            raise OSError("disk full")

        with patch.object(mcp_mod, "_get_save_download", return_value=failing_save):
            with pytest.raises(OSError, match="disk full"):
                asyncio.run(_handle_download("call_audio", "download", {}, mock_connector))

    def test_downloads_scoped_to_org(self, tmp_path, mock_connector):
        org_download_dir = tmp_path / "orgs" / "org-abc" / "downloads"
        mock_connector.execute = AsyncMock(return_value=_make_async_gen([b"data"]))

        with patch.object(mcp_mod, "get_download_dir", return_value=org_download_dir):
            with patch.object(mcp_mod, "_get_save_download", return_value=_fake_save_download):
                with patch.object(mcp_mod, "_detect_extension", return_value=""):
                    result = asyncio.run(_handle_download("call_audio", "download", {}, mock_connector))

        assert org_download_dir.exists()
        assert Path(result["download"]["file_path"]).parent == org_download_dir


class TestDetectExtension:
    def test_returns_empty_for_unknown(self, tmp_path):
        f = tmp_path / "unknown"
        f.write_bytes(b"not a real file format")
        assert _detect_extension(f) == ""

    def test_returns_empty_for_empty_file(self, tmp_path):
        f = tmp_path / "empty"
        f.write_bytes(b"")
        assert _detect_extension(f) == ""

    def test_detects_png(self, tmp_path):
        png_header = b"\x89PNG\r\n\x1a\n" + b"\x00" * 100
        f = tmp_path / "image"
        f.write_bytes(png_header)
        assert _detect_extension(f) == ".png"
