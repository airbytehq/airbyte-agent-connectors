"""Tests for airbyte_api module."""

from unittest.mock import MagicMock, patch

import httpx
import pytest

from airbyte_agent_mcp.airbyte_api import AirbyteApi, AirbyteAuthError, get_api


def _token_response(expires_in: int = 3600) -> dict:
    return {"access_token": "tok_abc", "token_type": "bearer", "expires_in": expires_in}


def _make_api() -> AirbyteApi:
    return AirbyteApi(client_id="cid", client_secret="csec")


class TestClientLifecycle:
    @patch.object(httpx.Client, "close")
    def test_close_closes_http_client(self, mock_close):
        api = _make_api()
        api.close()
        mock_close.assert_called_once()

    @patch.object(httpx.Client, "close")
    def test_context_manager_closes_on_exit(self, mock_close):
        with _make_api() as api:
            assert isinstance(api, AirbyteApi)
        mock_close.assert_called_once()


class TestAuthentication:
    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_authenticates_on_first_call(self, mock_get, mock_post):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        mock_get.return_value = MagicMock(json=lambda: {"id": "123"}, raise_for_status=lambda: None)

        api = _make_api()
        api.get_connector("123")

        mock_post.assert_called_once()
        args = mock_post.call_args
        assert args[1]["json"]["client_id"] == "cid"
        assert args[1]["json"]["client_secret"] == "csec"

    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_caches_token(self, mock_get, mock_post):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        mock_get.return_value = MagicMock(json=lambda: {"id": "123"}, raise_for_status=lambda: None)

        api = _make_api()
        api.get_connector("1")
        api.get_connector("2")

        assert mock_post.call_count == 1  # Only one token request

    @patch("airbyte_agent_mcp.airbyte_api.time.monotonic")
    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_refreshes_expired_token(self, mock_get, mock_post, mock_time):
        mock_post.return_value = MagicMock(json=lambda: _token_response(expires_in=100), raise_for_status=lambda: None)
        mock_get.return_value = MagicMock(json=lambda: {"id": "123"}, raise_for_status=lambda: None)

        # First call at t=0
        mock_time.return_value = 0.0
        api = _make_api()
        api.get_connector("1")
        assert mock_post.call_count == 1

        # Second call at t=50 (token expires at t=40 due to 60s buffer, so expired)
        mock_time.return_value = 50.0
        api.get_connector("2")
        assert mock_post.call_count == 2

    @pytest.mark.parametrize("status_code", [401, 403, 500])
    @patch.object(httpx.Client, "post")
    def test_auth_failure_raises_airbyte_auth_error(self, mock_post, status_code):
        mock_post.return_value = MagicMock(status_code=status_code)
        api = _make_api()
        with pytest.raises(AirbyteAuthError, match=str(status_code)):
            api.get_connector("123")


class TestGetConnectorSource:
    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_returns_response(self, mock_get, mock_post):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        expected = {"id": "abc-123", "name": "My Gong", "source_template": {}, "replication_config": {}}
        mock_get.return_value = MagicMock(json=lambda: expected, raise_for_status=lambda: None)

        result = _make_api().get_connector("abc-123")
        assert result == expected
        assert "/integrations/connectors/abc-123" in mock_get.call_args[0][0]

    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_http_error_propagates(self, mock_get, mock_post):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        resp = httpx.Response(status_code=404, request=httpx.Request("GET", "http://test"))
        mock_get.return_value = resp

        with pytest.raises(httpx.HTTPStatusError):
            _make_api().get_connector("bad-id")


class TestListCustomers:
    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_returns_list(self, mock_get, mock_post):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        items = [{"id": "ws-1", "name": "My Customer"}]
        mock_get.return_value = MagicMock(json=lambda: {"data": items}, raise_for_status=lambda: None)

        result = _make_api().list_customers()
        assert result == items
        assert "/workspaces" in mock_get.call_args[0][0]

    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_http_error_propagates(self, mock_get, mock_post):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        resp = httpx.Response(status_code=403, request=httpx.Request("GET", "http://test"))
        mock_get.return_value = resp

        with pytest.raises(httpx.HTTPStatusError):
            _make_api().list_customers()


class TestListConnectorSources:
    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_returns_list(self, mock_get, mock_post):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        items = [{"id": "c1", "name": "Gong"}, {"id": "c2", "name": "Salesforce"}]
        mock_get.return_value = MagicMock(json=lambda: {"data": items}, raise_for_status=lambda: None)

        result = _make_api().list_connector_sources("ws-123")
        assert result == items
        assert mock_get.call_args[1]["params"] == {"workspace_id": "ws-123"}

    @patch.object(httpx.Client, "post")
    @patch.object(httpx.Client, "get")
    def test_http_error_propagates(self, mock_get, mock_post):
        mock_post.return_value = MagicMock(json=lambda: _token_response(), raise_for_status=lambda: None)
        resp = httpx.Response(status_code=403, request=httpx.Request("GET", "http://test"))
        mock_get.return_value = resp

        with pytest.raises(httpx.HTTPStatusError):
            _make_api().list_connector_sources("ws-bad")


class TestFetchRegistry:
    @pytest.fixture(autouse=True)
    def _clear_cache(self):
        import airbyte_agent_mcp.airbyte_api as mod

        mod._registry_cache = None

    @patch("airbyte_agent_mcp.airbyte_api.httpx.get")
    def test_returns_connectors(self, mock_get):
        items = [{"connector_definition_id": "id-1", "connector_name": "gong"}]
        mock_get.return_value = MagicMock(json=lambda: {"connectors": items}, raise_for_status=lambda: None)

        from airbyte_agent_mcp.airbyte_api import fetch_registry

        result = fetch_registry()
        assert result == items

    @patch("airbyte_agent_mcp.airbyte_api.httpx.get")
    def test_http_error_propagates(self, mock_get):
        mock_get.return_value = httpx.Response(status_code=500, request=httpx.Request("GET", "http://test"))

        from airbyte_agent_mcp.airbyte_api import fetch_registry

        with pytest.raises(httpx.HTTPStatusError):
            fetch_registry()


class TestGetApi:
    def test_returns_api_when_env_set(self, monkeypatch):
        monkeypatch.setenv("AIRBYTE_CLIENT_ID", "cid")
        monkeypatch.setenv("AIRBYTE_CLIENT_SECRET", "csec")
        api = get_api()
        assert isinstance(api, AirbyteApi)

    def test_raises_auth_error_when_missing_client_id(self, monkeypatch):
        monkeypatch.delenv("AIRBYTE_CLIENT_ID", raising=False)
        monkeypatch.setenv("AIRBYTE_CLIENT_SECRET", "csec")
        with pytest.raises(AirbyteAuthError, match="credentials not configured"):
            get_api()

    def test_raises_auth_error_when_missing_client_secret(self, monkeypatch):
        monkeypatch.setenv("AIRBYTE_CLIENT_ID", "cid")
        monkeypatch.delenv("AIRBYTE_CLIENT_SECRET", raising=False)
        with pytest.raises(AirbyteAuthError, match="credentials not configured"):
            get_api()

    def test_raises_auth_error_when_both_missing(self, monkeypatch):
        monkeypatch.delenv("AIRBYTE_CLIENT_ID", raising=False)
        monkeypatch.delenv("AIRBYTE_CLIENT_SECRET", raising=False)
        with pytest.raises(AirbyteAuthError, match="credentials not configured"):
            get_api()
