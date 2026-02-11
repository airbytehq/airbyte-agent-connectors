"""Tests for mcp_server helper functions."""

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import pytest
from pydantic import BaseModel

import airbyte_agent_mcp.mcp_server as mcp_mod
from airbyte_agent_mcp.mcp_server import (
    _INSTRUCTIONS,
    _TRUNCATION_SUFFIX,
    ACTION_DOWNLOAD,
    ACTION_LIST,
    ACTION_SEARCH,
    COLLECTION_ACTIONS,
    ENVELOPE_DATA_FIELD,
    MAX_TEXT_FIELD_CHARS,
    _apply_to_records,
    _compact,
    _drop_fields_from_record,
    _exclude_fields,
    _pick_fields_from_record,
    _require_connector,
    _select_fields,
    _to_dict,
    _transform_response,
    _truncate_long_text,
    current_datetime,
    get_instructions,
)

# --- _to_dict ---


class TestToDict:
    def test_converts_pydantic_model(self):
        class MyModel(BaseModel):
            id: int
            name: str

        model = MyModel(id=1, name="Alice")
        result = _to_dict(model)
        assert result == {"id": 1, "name": "Alice"}
        assert isinstance(result, dict)

    def test_converts_nested_pydantic_model(self):
        class Meta(BaseModel):
            has_more: bool

        class Envelope(BaseModel):
            data: list[dict]
            meta: Meta

        model = Envelope(data=[{"id": 1}], meta=Meta(has_more=False))
        result = _to_dict(model)
        assert result == {"data": [{"id": 1}], "meta": {"has_more": False}}
        assert isinstance(result, dict)
        assert isinstance(result["meta"], dict)

    def test_dict_passthrough(self):
        data = {"id": 1, "name": "Alice"}
        assert _to_dict(data) is data

    def test_scalar_passthrough(self):
        assert _to_dict(42) == 42
        assert _to_dict("hello") == "hello"

    def test_list_passthrough(self):
        data = [1, 2, 3]
        assert _to_dict(data) is data

    def test_select_fields_works_after_to_dict(self):
        class Record(BaseModel):
            id: int
            name: str
            bio: str

        model = Record(id=1, name="Alice", bio="long")
        result = _select_fields(_to_dict(model), ["id", "name"])
        assert result == {"id": 1, "name": "Alice"}

    def test_exclude_fields_works_after_to_dict(self):
        class Record(BaseModel):
            id: int
            name: str
            bio: str

        model = Record(id=1, name="Alice", bio="long")
        result = _exclude_fields(_to_dict(model), ["bio"])
        assert result == {"id": 1, "name": "Alice"}


# --- _compact ---


class TestCompact:
    def test_removes_none_values(self):
        assert _compact({"a": 1, "b": None}) == {"a": 1}

    def test_removes_empty_strings(self):
        assert _compact({"a": "hello", "b": ""}) == {"a": "hello"}

    def test_removes_empty_lists(self):
        assert _compact({"a": [1], "b": []}) == {"a": [1]}

    def test_removes_empty_dicts(self):
        assert _compact({"a": {"x": 1}, "b": {}}) == {"a": {"x": 1}}

    def test_nested_dict(self):
        data = {"user": {"name": "Alice", "bio": None, "tags": []}}
        assert _compact(data) == {"user": {"name": "Alice"}}

    def test_list_of_dicts(self):
        data = [{"id": 1, "x": None}, {"id": 2, "y": ""}]
        assert _compact(data) == [{"id": 1}, {"id": 2}]

    def test_preserves_falsy_but_meaningful_values(self):
        data = {"count": 0, "flag": False, "name": None}
        assert _compact(data) == {"count": 0, "flag": False}

    def test_scalar_passthrough(self):
        assert _compact(42) == 42
        assert _compact("hello") == "hello"

    def test_deeply_nested(self):
        data = {"a": {"b": {"c": None, "d": "ok"}}}
        assert _compact(data) == {"a": {"b": {"d": "ok"}}}

    def test_all_empty_collapses(self):
        data = {"a": None, "b": "", "c": [], "d": {}}
        assert _compact(data) == {}

    def test_nested_dict_empty_after_compaction(self):
        data = {"user": {"name": None, "bio": None}}
        assert _compact(data) == {}

    def test_nested_mixed_empty_after_compaction(self):
        data = {"keep": 1, "drop": {"a": None, "b": ""}}
        assert _compact(data) == {"keep": 1}


# --- _truncate_long_text ---


class TestTruncateLongText:
    def test_short_string_unchanged(self):
        assert _truncate_long_text("short") == "short"

    def test_string_at_limit_unchanged(self):
        text = "x" * MAX_TEXT_FIELD_CHARS
        assert _truncate_long_text(text) == text

    def test_string_over_limit_is_truncated(self):
        text = "x" * (MAX_TEXT_FIELD_CHARS + 100)
        result = _truncate_long_text(text)
        assert result.endswith(_TRUNCATION_SUFFIX)
        assert result.startswith("x" * MAX_TEXT_FIELD_CHARS)

    def test_non_string_unchanged(self):
        assert _truncate_long_text(42) == 42
        assert _truncate_long_text(True) is True

    def test_dict_values_truncated(self):
        data = {"id": 1, "body": "x" * 500}
        result = _truncate_long_text(data)
        assert result["id"] == 1
        assert result["body"].endswith(_TRUNCATION_SUFFIX)
        assert len(result["body"]) < 500

    def test_list_items_truncated(self):
        data = [{"text": "a" * 500}, {"text": "short"}]
        result = _truncate_long_text(data)
        assert result[0]["text"].endswith(_TRUNCATION_SUFFIX)
        assert result[1]["text"] == "short"

    def test_nested_truncation(self):
        data = {"record": {"details": {"notes": "n" * 500}}}
        result = _truncate_long_text(data)
        assert result["record"]["details"]["notes"].endswith(_TRUNCATION_SUFFIX)

    def test_preserves_structure(self):
        data = {"a": 1, "b": [2, 3], "c": {"d": "short"}}
        assert _truncate_long_text(data) == data


# --- _pick_fields_from_record ---


class TestPickFieldsFromRecord:
    def test_picks_top_level_fields(self):
        record = {"id": 1, "name": "Alice", "email": "a@b.com", "bio": "long text"}
        assert _pick_fields_from_record(record, ["id", "name"]) == {"id": 1, "name": "Alice"}

    def test_ignores_missing_fields(self):
        record = {"id": 1, "name": "Alice"}
        assert _pick_fields_from_record(record, ["id", "missing"]) == {"id": 1}

    def test_dot_notation_nested(self):
        record = {"id": 1, "content": {"topics": ["a"], "brief": "summary", "details": "long"}}
        result = _pick_fields_from_record(record, ["id", "content.topics"])
        assert result == {"id": 1, "content": {"topics": ["a"]}}

    def test_multiple_nested_from_same_parent(self):
        record = {"content": {"topics": ["a"], "brief": "b", "details": "c"}}
        result = _pick_fields_from_record(record, ["content.topics", "content.brief"])
        assert result == {"content": {"topics": ["a"], "brief": "b"}}

    def test_nested_field_parent_missing(self):
        record = {"id": 1}
        assert _pick_fields_from_record(record, ["content.topics"]) == {}

    def test_nested_field_parent_not_dict(self):
        record = {"id": 1, "content": "just a string"}
        assert _pick_fields_from_record(record, ["id", "content.topics"]) == {"id": 1}

    def test_non_dict_passthrough(self):
        assert _pick_fields_from_record("scalar", ["id"]) == "scalar"
        assert _pick_fields_from_record(42, ["id"]) == 42

    def test_empty_fields_list(self):
        record = {"id": 1, "name": "Alice"}
        assert _pick_fields_from_record(record, []) == {}

    def test_deeply_nested_dot_notation(self):
        record = {"a": {"b": {"c": "deep", "d": "other"}}}
        result = _pick_fields_from_record(record, ["a.b.c"])
        assert result == {"a": {"b": {"c": "deep"}}}


# --- _select_fields ---


class TestSelectFields:
    def test_list_of_records(self):
        data = [
            {"id": 1, "name": "Alice", "bio": "long"},
            {"id": 2, "name": "Bob", "bio": "long"},
        ]
        result = _select_fields(data, ["id", "name"])
        assert result == [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

    def test_single_record(self):
        data = {"id": 1, "name": "Alice", "bio": "long", "email": "a@b.com"}
        result = _select_fields(data, ["id", "name"])
        assert result == {"id": 1, "name": "Alice"}

    def test_non_dict_passthrough(self):
        assert _select_fields("scalar", ["id"]) == "scalar"
        assert _select_fields(42, ["id"]) == 42

    def test_list_with_nested_fields(self):
        data = [
            {"id": 1, "content": {"topics": ["a"], "brief": "b", "details": "c"}},
        ]
        result = _select_fields(data, ["id", "content.topics"])
        assert result == [{"id": 1, "content": {"topics": ["a"]}}]

    def test_empty_list(self):
        result = _select_fields([], ["id"])
        assert result == []

    def test_search_hit_style_with_data_prefix(self):
        """Test selecting fields from search hits where entity data is nested under 'data' key."""
        hits = [
            {"data": {"id": 1, "name": "Alice", "bio": "long"}, "score": 0.9},
            {"data": {"id": 2, "name": "Bob", "bio": "long"}, "score": 0.8},
        ]
        # Using "data." prefix to select fields inside the data object
        result = _select_fields(hits, ["data.id", "data.name"])
        assert result == [
            {"data": {"id": 1, "name": "Alice"}},
            {"data": {"id": 2, "name": "Bob"}},
        ]


# --- _drop_fields_from_record ---


class TestDropFieldsFromRecord:
    def test_drops_top_level_fields(self):
        record = {"id": 1, "name": "Alice", "bio": "long text", "email": "a@b.com"}
        assert _drop_fields_from_record(record, ["bio", "email"]) == {"id": 1, "name": "Alice"}

    def test_ignores_missing_fields(self):
        record = {"id": 1, "name": "Alice"}
        assert _drop_fields_from_record(record, ["missing"]) == {"id": 1, "name": "Alice"}

    def test_dot_notation_nested(self):
        record = {"id": 1, "content": {"topics": ["a"], "brief": "summary", "details": "long"}}
        result = _drop_fields_from_record(record, ["content.brief", "content.details"])
        assert result == {"id": 1, "content": {"topics": ["a"]}}

    def test_drop_entire_nested_object(self):
        record = {"id": 1, "content": {"topics": ["a"]}, "interaction": {"stats": 42}}
        result = _drop_fields_from_record(record, ["content", "interaction"])
        assert result == {"id": 1}

    def test_nested_field_parent_missing(self):
        record = {"id": 1}
        assert _drop_fields_from_record(record, ["content.brief"]) == {"id": 1}

    def test_nested_field_parent_not_dict(self):
        record = {"id": 1, "content": "just a string"}
        assert _drop_fields_from_record(record, ["content.brief"]) == {"id": 1, "content": "just a string"}

    def test_non_dict_passthrough(self):
        assert _drop_fields_from_record("scalar", ["id"]) == "scalar"
        assert _drop_fields_from_record(42, ["id"]) == 42

    def test_empty_fields_list(self):
        record = {"id": 1, "name": "Alice"}
        assert _drop_fields_from_record(record, []) == {"id": 1, "name": "Alice"}

    def test_deeply_nested_dot_notation(self):
        record = {"a": {"b": {"c": "deep", "d": "other"}}}
        result = _drop_fields_from_record(record, ["a.b.c"])
        assert result == {"a": {"b": {"d": "other"}}}

    def test_mixed_top_and_nested(self):
        record = {"id": 1, "name": "Alice", "content": {"brief": "b", "topics": ["a"]}}
        result = _drop_fields_from_record(record, ["name", "content.brief"])
        assert result == {"id": 1, "content": {"topics": ["a"]}}


# --- _exclude_fields ---


class TestExcludeFields:
    def test_list_of_records(self):
        data = [
            {"id": 1, "name": "Alice", "bio": "long"},
            {"id": 2, "name": "Bob", "bio": "long"},
        ]
        result = _exclude_fields(data, ["bio"])
        assert result == [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

    def test_single_record(self):
        data = {"id": 1, "name": "Alice", "bio": "long", "email": "a@b.com"}
        result = _exclude_fields(data, ["bio", "email"])
        assert result == {"id": 1, "name": "Alice"}

    def test_non_dict_passthrough(self):
        assert _exclude_fields("scalar", ["id"]) == "scalar"
        assert _exclude_fields(42, ["id"]) == 42

    def test_list_with_nested_excludes(self):
        data = [
            {"id": 1, "content": {"topics": ["a"], "brief": "b", "details": "c"}},
        ]
        result = _exclude_fields(data, ["content.brief", "content.details"])
        assert result == [{"id": 1, "content": {"topics": ["a"]}}]

    def test_empty_list(self):
        result = _exclude_fields([], ["bio"])
        assert result == []

    def test_search_hit_style_with_data_prefix(self):
        """Test excluding fields from search hits where entity data is nested under 'data' key."""
        hits = [
            {"data": {"id": 1, "name": "Alice", "bio": "long"}, "score": 0.9},
            {"data": {"id": 2, "name": "Bob", "bio": "long"}, "score": 0.8},
        ]
        # Using "data." prefix to exclude fields inside the data object
        result = _exclude_fields(hits, ["data.bio"])
        assert result == [
            {"data": {"id": 1, "name": "Alice"}, "score": 0.9},
            {"data": {"id": 2, "name": "Bob"}, "score": 0.8},
        ]


# --- _apply_to_records ---


class TestApplyToRecords:
    def test_applies_to_list_items(self):
        data = [{"x": 1}, {"x": 2}, {"x": 3}]
        result = _apply_to_records(data, lambda r: {**r, "y": r["x"] * 2})
        assert result == [{"x": 1, "y": 2}, {"x": 2, "y": 4}, {"x": 3, "y": 6}]

    def test_applies_to_single_record(self):
        data = {"x": 1}
        result = _apply_to_records(data, lambda r: {**r, "y": r["x"] * 2})
        assert result == {"x": 1, "y": 2}

    def test_empty_list(self):
        result = _apply_to_records([], lambda r: r)
        assert result == []

    def test_scalar_passthrough(self):
        result = _apply_to_records("scalar", lambda r: {"transformed": True})
        assert result == {"transformed": True}

    def test_none_passthrough(self):
        result = _apply_to_records(None, lambda r: {"transformed": True})
        assert result == {"transformed": True}


# --- Envelope preservation (simulates execute behavior) ---


class TestEnvelopePreservation:
    """Tests that simulate how execute extracts data, transforms it, and preserves the envelope."""

    def test_list_action_preserves_envelope(self):
        """For list action: extract data, transform, put back with meta preserved."""
        api_response = {
            "data": [
                {"id": 1, "name": "Alice", "bio": "long text", "extra": "stuff"},
                {"id": 2, "name": "Bob", "bio": "more text", "extra": "things"},
            ],
            "meta": {"has_more": True, "cursor": "abc123"},
        }

        # Simulate what execute does
        records = api_response.get("data", [])
        records = _select_fields(records, ["id", "name"])
        records = _truncate_long_text(records)
        records = _compact(records)
        result = {**api_response, "data": records}

        assert result == {
            "data": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}],
            "meta": {"has_more": True, "cursor": "abc123"},
        }

    def test_search_action_preserves_envelope(self):
        """For search action: extract data, transform records, and preserve meta."""
        api_response = {
            "data": [
                {"id": 1, "name": "Alice", "bio": "long"},
                {"id": 2, "name": "Bob", "bio": "text"},
            ],
            "meta": {"has_more": True, "cursor": "xyz"},
        }

        # Simulate what execute does for search
        records = api_response.get("data", [])
        select_fields = ["id", "name"]
        records = _select_fields(records, select_fields)
        records = _truncate_long_text(records)
        records = _compact(records)
        result = {**api_response, "data": records}

        assert result == {
            "data": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}],
            "meta": {"has_more": True, "cursor": "xyz"},
        }

    def test_get_action_returns_transformed_record_directly(self):
        """For get action: no envelope, transform and return record directly."""
        api_response = {"id": 1, "name": "Alice", "bio": "long text", "email": "a@b.com"}

        # Simulate what execute does for get
        result = _select_fields(api_response, ["id", "name"])
        result = _compact(result)

        assert result == {"id": 1, "name": "Alice"}

    def test_list_action_with_exclude_fields(self):
        """For list action with exclude_fields."""
        api_response = {
            "data": [
                {"id": 1, "name": "Alice", "content": {"brief": "b", "details": "long"}},
            ],
            "meta": {"has_more": False},
        }

        records = api_response.get("data", [])
        records = _exclude_fields(records, ["content.details"])
        records = _compact(records)
        result = {**api_response, "data": records}

        assert result == {
            "data": [{"id": 1, "name": "Alice", "content": {"brief": "b"}}],
            "meta": {"has_more": False},
        }


# --- current_datetime ---


class TestCurrentDatetime:
    def test_returns_iso_format(self):
        fixed_time = datetime(2024, 6, 15, 14, 30, 45, tzinfo=UTC)
        with patch("airbyte_agent_mcp.mcp_server.datetime") as mock_dt:
            mock_dt.now.return_value = fixed_time
            result = current_datetime()

        assert result == "2024-06-15T14:30:45+00:00"

    def test_uses_utc_timezone(self):
        result = current_datetime()
        assert result.endswith("+00:00")

    def test_returns_string(self):
        result = current_datetime()
        assert isinstance(result, str)
        datetime.fromisoformat(result)


# --- get_instructions ---


class TestGetInstructions:
    def test_returns_non_empty_string(self):
        result = get_instructions()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_contains_key_sections(self):
        result = get_instructions()
        assert "QUERY PLANNING" in result
        assert "ACTION SELECTION" in result
        assert "FIELD SELECTION" in result
        assert "QUERY SIZING AND PAGINATION" in result
        assert "DATE RANGE QUERIES" in result
        assert "DOWNLOADS" in result

    def test_returns_same_as_constant(self):
        result = get_instructions()
        assert result == _INSTRUCTIONS


# --- _require_connector ---


class TestRequireConnector:
    def test_returns_connector_when_initialized(self):
        mock_connector = MagicMock()
        original = mcp_mod._connector
        mcp_mod._connector = mock_connector
        try:
            result = _require_connector()
            assert result is mock_connector
        finally:
            mcp_mod._connector = original

    def test_raises_when_not_initialized(self):
        original = mcp_mod._connector
        mcp_mod._connector = None
        try:
            with pytest.raises(RuntimeError, match="Connector not initialized"):
                _require_connector()
        finally:
            mcp_mod._connector = original


# --- _transform_response ---


class TestTransformResponse:
    def test_list_action_extracts_and_replaces_data(self):
        result = {"data": [{"id": 1, "name": "Alice"}], "meta": {"has_more": False}}
        transformed = _transform_response(result, ACTION_LIST, None, None)
        assert ENVELOPE_DATA_FIELD[ACTION_LIST] in transformed
        assert transformed["data"] == [{"id": 1, "name": "Alice"}]
        assert transformed["meta"] == {"has_more": False}

    def test_search_action_extracts_and_replaces_data(self):
        result = {"data": [{"id": 1, "name": "Alice"}], "meta": {"has_more": False}}
        transformed = _transform_response(result, ACTION_SEARCH, None, None)
        assert ENVELOPE_DATA_FIELD[ACTION_SEARCH] in transformed
        assert transformed["data"] == [{"id": 1, "name": "Alice"}]
        assert transformed["meta"] == {"has_more": False}

    def test_applies_select_fields_for_search(self):
        result = {
            "data": [{"id": 1, "name": "Alice", "bio": "long"}],
            "meta": {},
        }
        transformed = _transform_response(result, ACTION_SEARCH, ["id", "name"], None)
        assert transformed["data"] == [{"id": 1, "name": "Alice"}]

    def test_applies_exclude_fields_for_search(self):
        result = {
            "data": [{"id": 1, "name": "Alice", "bio": "long"}],
            "meta": {},
        }
        transformed = _transform_response(result, ACTION_SEARCH, None, ["bio"])
        assert transformed["data"] == [{"id": 1, "name": "Alice"}]

    def test_get_action_returns_transformed_directly(self):
        result = {"id": 1, "name": "Alice", "bio": "long"}
        transformed = _transform_response(result, "get", ["id", "name"], None)
        assert transformed == {"id": 1, "name": "Alice"}

    def test_applies_select_fields_for_list(self):
        result = {"data": [{"id": 1, "name": "Alice", "bio": "long"}], "meta": {}}
        transformed = _transform_response(result, ACTION_LIST, ["id", "name"], None)
        assert transformed["data"] == [{"id": 1, "name": "Alice"}]

    def test_applies_exclude_fields_for_list(self):
        result = {"data": [{"id": 1, "name": "Alice", "bio": "long"}], "meta": {}}
        transformed = _transform_response(result, ACTION_LIST, None, ["bio"])
        assert transformed["data"] == [{"id": 1, "name": "Alice"}]

    def test_select_fields_takes_priority(self):
        result = {"data": [{"id": 1, "name": "Alice", "bio": "long"}], "meta": {}}
        transformed = _transform_response(result, ACTION_LIST, ["id"], ["name"])
        assert transformed["data"] == [{"id": 1}]

    def test_truncates_for_list(self):
        long_text = "x" * 500
        result = {"data": [{"id": 1, "text": long_text}], "meta": {}}
        transformed = _transform_response(result, ACTION_LIST, None, None)
        assert transformed["data"][0]["text"].endswith(_TRUNCATION_SUFFIX)
        assert len(transformed["data"][0]["text"]) < 500

    def test_truncates_for_search(self):
        long_text = "x" * 500
        result = {"data": [{"id": 1, "text": long_text}], "meta": {}}
        transformed = _transform_response(result, ACTION_SEARCH, None, None)
        assert transformed["data"][0]["text"].endswith(_TRUNCATION_SUFFIX)

    def test_does_not_truncate_for_get(self):
        long_text = "x" * 500
        result = {"id": 1, "text": long_text}
        transformed = _transform_response(result, "get", None, None)
        assert transformed["text"] == long_text

    def test_compacts_result(self):
        result = {"data": [{"id": 1, "empty": None, "blank": ""}], "meta": {}}
        transformed = _transform_response(result, ACTION_LIST, None, None)
        assert transformed["data"] == [{"id": 1}]

    def test_preserves_envelope_meta(self):
        result = {"data": [{"id": 1}], "meta": {"cursor": "abc", "has_more": True}}
        transformed = _transform_response(result, ACTION_LIST, None, None)
        assert transformed["meta"] == {"cursor": "abc", "has_more": True}

    def test_list_missing_data_envelope_raises(self):
        result = {"items": [{"id": 1}], "meta": {}}
        with pytest.raises(KeyError, match="List response missing 'data' envelope key"):
            _transform_response(result, ACTION_LIST, None, None)

    def test_search_missing_data_envelope_raises(self):
        result = {"results": [{"id": 1}], "meta": {}}
        with pytest.raises(KeyError, match="Search response missing 'data' envelope key"):
            _transform_response(result, ACTION_SEARCH, None, None)


# --- _get_save_download ---


class TestGetSaveDownload:
    def test_imports_from_connector_package(self):
        mock_connector = MagicMock()
        mock_connector.__module__ = "airbyte_agent_gong.connector"
        type(mock_connector).__module__ = "airbyte_agent_gong.connector"

        mock_module = MagicMock()
        mock_module.save_download = lambda: "saved"

        original = mcp_mod._connector
        mcp_mod._connector = mock_connector
        try:
            with patch("importlib.import_module", return_value=mock_module) as mock_import:
                from airbyte_agent_mcp.mcp_server import _get_save_download

                result = _get_save_download()
                mock_import.assert_called_once_with("airbyte_agent_gong._vendored.connector_sdk")
                assert result == mock_module.save_download
        finally:
            mcp_mod._connector = original

    def test_returns_save_download_function(self):
        mock_connector = MagicMock()
        type(mock_connector).__module__ = "airbyte_agent_test.connector"

        mock_save_download = MagicMock()
        mock_module = MagicMock()
        mock_module.save_download = mock_save_download

        original = mcp_mod._connector
        mcp_mod._connector = mock_connector
        try:
            with patch("importlib.import_module", return_value=mock_module):
                from airbyte_agent_mcp.mcp_server import _get_save_download

                result = _get_save_download()
                assert result is mock_save_download
        finally:
            mcp_mod._connector = original


# --- Constants ---


class TestConstants:
    def test_action_constants_are_strings(self):
        assert ACTION_LIST == "list"
        assert ACTION_SEARCH == "search"
        assert ACTION_DOWNLOAD == "download"

    def test_collection_actions_contains_list_and_search(self):
        assert ACTION_LIST in COLLECTION_ACTIONS
        assert ACTION_SEARCH in COLLECTION_ACTIONS
        assert ACTION_DOWNLOAD not in COLLECTION_ACTIONS

    def test_envelope_data_field_mapping(self):
        assert ENVELOPE_DATA_FIELD[ACTION_LIST] == "data"
        assert ENVELOPE_DATA_FIELD[ACTION_SEARCH] == "data"
