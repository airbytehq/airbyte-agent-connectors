"""Tests for mcp_server helper functions."""

from pydantic import BaseModel

from airbyte_agent_mcp.mcp_server import (
    _TRUNCATION_SUFFIX,
    MAX_TEXT_FIELD_CHARS,
    _compact,
    _drop_fields_from_record,
    _exclude_fields,
    _pick_fields_from_record,
    _select_fields,
    _to_dict,
    _truncate_long_text,
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
        class Meta(BaseModel):
            has_more: bool

        class Envelope(BaseModel):
            data: list[dict]
            meta: Meta

        model = Envelope(data=[{"id": 1, "name": "Alice", "bio": "long"}], meta=Meta(has_more=False))
        result = _select_fields(_to_dict(model), ["id", "name"])
        assert result == {"data": [{"id": 1, "name": "Alice"}], "meta": {"has_more": False}}

    def test_exclude_fields_works_after_to_dict(self):
        class Meta(BaseModel):
            has_more: bool

        class Envelope(BaseModel):
            data: list[dict]
            meta: Meta

        model = Envelope(data=[{"id": 1, "name": "Alice", "bio": "long"}], meta=Meta(has_more=False))
        result = _exclude_fields(_to_dict(model), ["bio"])
        assert result == {"data": [{"id": 1, "name": "Alice"}], "meta": {"has_more": False}}


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
    def test_envelope_response(self):
        data = {
            "data": [
                {"id": 1, "name": "Alice", "bio": "long"},
                {"id": 2, "name": "Bob", "bio": "long"},
            ],
            "meta": {"has_more": False},
        }
        result = _select_fields(data, ["id", "name"])
        assert result == {
            "data": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}],
            "meta": {"has_more": False},
        }

    def test_direct_entity_response(self):
        data = {"id": 1, "name": "Alice", "bio": "long", "email": "a@b.com"}
        result = _select_fields(data, ["id", "name"])
        assert result == {"id": 1, "name": "Alice"}

    def test_non_dict_passthrough(self):
        assert _select_fields("scalar", ["id"]) == "scalar"
        assert _select_fields(42, ["id"]) == 42

    def test_envelope_with_nested_fields(self):
        data = {
            "data": [
                {"id": 1, "content": {"topics": ["a"], "brief": "b", "details": "c"}},
            ],
            "meta": {"has_more": False},
        }
        result = _select_fields(data, ["id", "content.topics"])
        assert result == {
            "data": [{"id": 1, "content": {"topics": ["a"]}}],
            "meta": {"has_more": False},
        }

    def test_envelope_preserves_non_data_keys(self):
        data = {"data": [{"id": 1, "x": 2}], "meta": {"has_more": True}, "extra": "info"}
        result = _select_fields(data, ["id"])
        assert result == {"data": [{"id": 1}], "meta": {"has_more": True}, "extra": "info"}

    def test_empty_data_list(self):
        data = {"data": [], "meta": {"has_more": False}}
        result = _select_fields(data, ["id"])
        assert result == {"data": [], "meta": {"has_more": False}}


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
    def test_envelope_response(self):
        data = {
            "data": [
                {"id": 1, "name": "Alice", "bio": "long"},
                {"id": 2, "name": "Bob", "bio": "long"},
            ],
            "meta": {"has_more": False},
        }
        result = _exclude_fields(data, ["bio"])
        assert result == {
            "data": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}],
            "meta": {"has_more": False},
        }

    def test_direct_entity_response(self):
        data = {"id": 1, "name": "Alice", "bio": "long", "email": "a@b.com"}
        result = _exclude_fields(data, ["bio", "email"])
        assert result == {"id": 1, "name": "Alice"}

    def test_non_dict_passthrough(self):
        assert _exclude_fields("scalar", ["id"]) == "scalar"
        assert _exclude_fields(42, ["id"]) == 42

    def test_envelope_with_nested_excludes(self):
        data = {
            "data": [
                {"id": 1, "content": {"topics": ["a"], "brief": "b", "details": "c"}},
            ],
            "meta": {"has_more": False},
        }
        result = _exclude_fields(data, ["content.brief", "content.details"])
        assert result == {
            "data": [{"id": 1, "content": {"topics": ["a"]}}],
            "meta": {"has_more": False},
        }

    def test_envelope_preserves_non_data_keys(self):
        data = {"data": [{"id": 1, "x": 2}], "meta": {"has_more": True}, "extra": "info"}
        result = _exclude_fields(data, ["x"])
        assert result == {"data": [{"id": 1}], "meta": {"has_more": True}, "extra": "info"}
