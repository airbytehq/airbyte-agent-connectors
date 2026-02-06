"""MCP server for Airbyte Agent connectors."""

from __future__ import annotations

import importlib
import inspect
import uuid
from collections.abc import Callable
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import filetype
from fastmcp import FastMCP

from .models.cli_config import get_download_dir

# Action type constants
ACTION_LIST = "list"
ACTION_SEARCH = "search"
ACTION_DOWNLOAD = "download"

COLLECTION_ACTIONS = {ACTION_LIST, ACTION_SEARCH}

# Response envelope keys
ENVELOPE_DATA_FIELD = {
    ACTION_SEARCH: "hits",
    ACTION_LIST: "data",
}


_INSTRUCTIONS = """\
CRITICAL — context budget is limited. Large responses waste tokens and degrade performance. Follow these rules strictly:

QUERY PLANNING (DO THIS FIRST):
- For ANY time-based question, call `current_datetime` FIRST to get the current date/time.
- Concrete date mappings (relative to current date):
  - "recent" or "lately" = last 7 days
  - "last week" = last 7 days
  - "this week" = since Monday of the current week
  - "this month" = since the 1st of the current month
  - "last month" = from the 1st to the last day of the previous month
  - "today" = since midnight UTC today
  - "yesterday" = the previous calendar day (midnight to midnight UTC)
- When a question mentions a person, team, project, or any entity by name, you MUST resolve \
the name to an ID BEFORE querying the target entity. Call `entity_schema` on the target entity \
to find fields ending in `Id` or `_id` — these tell you which related entity to look up. \
Then search that related entity by name to get the ID, and use the ID as a filter.

NEVER PAGINATE TO FILTER — USE IDs INSTEAD:
- If you get back a large result set and need a specific subset, do NOT paginate through all pages \
scanning for matches. Instead:
  Step 1: Look at the fields in the response — find any field ending in `Id` or `_id` that links \
to the entity you care about.
  Step 2: If you don't already have the ID, search the related entity to resolve it.
  Step 3: Re-query with the ID as a filter.
- This applies even if you already have the first page of results. Stop, resolve the ID, re-query filtered.

ACTION SELECTION:
- Use `search` as your DEFAULT action. NEVER use `list` as your first choice.
- `search` supports filtering, sorting, field selection, and pagination.
- `list` returns ALL records and is expensive. Only use `list` when:
  (a) You need today's data (search index may lag by hours), OR
  (b) `search` returned no results and you suspect an indexing delay.
- Example: to find a user by name, use action="search" with \
params={"query": {"filter": {"like": {"firstName": "Teo"}}}}, NOT action="list" on users.

FIELD SELECTION (MANDATORY for every call):
- You MUST use `select_fields` or `exclude_fields` on EVERY `execute` call. Omitting both is almost never correct.
- `select_fields`: allowlist — only these fields are returned. Use when you know exactly which fields you need. \
Example: select_fields=["id", "title", "started", "primaryUserId"]
- `exclude_fields`: blocklist — these fields are removed. Use when you need most fields but want to drop \
known-heavy ones (e.g. transcripts, content bodies, nested objects). \
Example: exclude_fields=["content", "interaction", "parties", "context"]
- Both support dot notation for nested fields (e.g. "content.brief", "interaction.speakers").
- Both are top-level arguments on `execute`, separate from `params`.
- If you provide both, `select_fields` takes priority and `exclude_fields` is ignored.
- When in doubt, use `select_fields` with just the fields you need — fewer fields = faster + cheaper.

FILTERING (MANDATORY when the user's question implies criteria):
- ALWAYS add filters that match the user's intent. Never do a broad list/search and filter client-side.
- For `search`: use `params.query.filter` with the appropriate condition (eq, like, gt, lt, in, etc.).
- For `list`: use the available query parameters (e.g. fromDateTime, toDateTime, workspaceId) to narrow results server-side.
- If you are unsure which filter fields are available, call `entity_schema` or `connector_info` first.
- When searching for text, try `like` first. If `like` returns no results, retry with `fuzzy` \
(e.g., {"fuzzy": {"name": "search term"}}) which matches words in any order and ignores punctuation.

QUERY SIZING AND PAGINATION:
- Use a default `limit` of 20-25. This is enough for most questions.
- Do NOT paginate by default — the first page usually answers the question.
- Only paginate when:
  (a) The user explicitly asks for "all" results, OR
  (b) You need an exact count and the first page has `has_more: true`.
- Hard stop: never fetch more than 3 pages without pausing to check if you have enough data.
- For "how many" questions: if the first page shows `has_more: true`, say "at least N" \
based on what you have rather than exhaustively paginating.
- Use filters to narrow queries instead of fetching everything.
- If a response is too large, retry with tighter `select_fields`, smaller `limit`, or more specific filters.

DATE RANGE QUERIES:
- If the date range includes today (e.g. "calls from today", "this week's activity", "since yesterday"), \
the search index may lag behind by hours and miss recent records. You MUST issue BOTH a `search` call \
AND a `list` call with date boundary parameters, then merge the results and deduplicate by `id`. \
This ensures you get both fast indexed results and the latest unindexed records.
- If the date range ends before today, `search` alone is sufficient.

DOWNLOADS:
- Some entities support a `download` action (e.g., call_audio, call_video).
- Download results include a file_path where the file was saved and its size.
- Share the file path with the user so they can access the downloaded file.

OTHER:
- In `list` and `search` results, long text fields are truncated and marked with "[truncated]". \
Use the `get` action with the record id to retrieve full values.
"""

mcp = FastMCP("Airbyte Agent MCP", instructions=_INSTRUCTIONS)

MAX_TEXT_FIELD_CHARS = 200
_TRUNCATION_SUFFIX = "... [truncated — use `get` action with the record id to retrieve the full value]"


def _detect_extension(file_path: Path) -> str:
    """Detect file extension from magic bytes using filetype."""
    kind = filetype.guess(str(file_path))
    if kind:
        return f".{kind.extension}"
    return ""


def _get_save_download() -> Any:
    """Import save_download from the loaded connector's vendored SDK."""
    package = type(_connector).__module__.split(".")[0]
    vendored = importlib.import_module(f"{package}._vendored.connector_sdk")
    return vendored.save_download


async def _handle_download(entity: str, action: str, params: dict[str, Any]) -> dict[str, Any]:
    """Handle download actions by saving streamed bytes to a file.

    Returns metadata about the saved file instead of raw bytes.
    """
    connector = _require_connector()
    result = await connector.execute(entity, action, params)

    if not inspect.isasyncgen(result):
        return _to_dict(result)

    download_dir = get_download_dir()
    download_dir.mkdir(parents=True, exist_ok=True)
    base_name = f"{entity}_{uuid.uuid4().hex[:12]}"
    file_path = download_dir / base_name

    save_download = _get_save_download()
    saved_path: Path = await save_download(result, file_path)

    ext = _detect_extension(saved_path)
    if ext:
        final_path = saved_path.with_suffix(ext)
        saved_path.rename(final_path)
        saved_path = final_path

    size_bytes = saved_path.stat().st_size

    return {
        "download": {
            "file_path": str(saved_path),
            "size_bytes": size_bytes,
            "entity": entity,
            "message": f"File downloaded and saved to: {saved_path} ({size_bytes:,} bytes). Share this path with the user.",
        }
    }


def _to_dict(obj: Any) -> Any:
    """Convert Pydantic models (or any object with model_dump) to plain dicts."""
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    return obj


def _compact(obj: Any) -> Any:
    """Recursively strip None values, empty strings, and empty collections from a result."""
    if isinstance(obj, dict):
        compacted = {k: _compact(v) for k, v in obj.items()}
        return {k: v for k, v in compacted.items() if v is not None and v != "" and v != [] and v != {}}
    if isinstance(obj, list):
        return [_compact(item) for item in obj]
    return obj


def _truncate_long_text_deep(obj: Any) -> Any:
    """Recursively truncate string values that exceed MAX_TEXT_FIELD_CHARS."""
    if isinstance(obj, dict):
        return {k: _truncate_long_text_deep(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_truncate_long_text_deep(item) for item in obj]
    if isinstance(obj, str) and len(obj) > MAX_TEXT_FIELD_CHARS:
        return obj[:MAX_TEXT_FIELD_CHARS] + _TRUNCATION_SUFFIX
    return obj


def _truncate_long_text(obj: Any) -> Any:
    """Truncate long text in records."""
    return _apply_to_records(obj, _truncate_long_text_deep)


def _pick_fields_from_record(record: Any, fields: list[str]) -> Any:
    """Select only the specified fields from a single record dict.

    Supports dot notation for nested fields (e.g., "content.topics").
    """
    if not isinstance(record, dict):
        return record
    result: dict[str, Any] = {}
    for field in fields:
        if "." in field:
            top, rest = field.split(".", 1)
            if top in record and isinstance(record[top], dict):
                if top not in result:
                    result[top] = {}
                nested = _pick_fields_from_record(record[top], [rest])
                result[top].update(nested)
        elif field in record:
            result[field] = record[field]
    return result


def _drop_fields_from_record(record: Any, fields: list[str]) -> Any:
    """Remove the specified fields from a single record dict.

    Supports dot notation for nested fields (e.g., "content.brief").
    """
    if not isinstance(record, dict):
        return record
    top_level_drops = {f for f in fields if "." not in f}
    nested_drops: dict[str, list[str]] = {}
    for field in fields:
        if "." in field:
            top, rest = field.split(".", 1)
            nested_drops.setdefault(top, []).append(rest)

    result: dict[str, Any] = {}
    for key, value in record.items():
        if key in top_level_drops:
            continue
        if key in nested_drops and isinstance(value, dict):
            result[key] = _drop_fields_from_record(value, nested_drops[key])
        else:
            result[key] = value
    return result


def _apply_to_records(obj: Any, record_fn: Callable[[Any], Any]) -> Any:
    """Apply a transform function to records.

    If obj is a list, applies record_fn to each item.
    If obj is a single record (dict), applies record_fn directly.
    """
    if isinstance(obj, list):
        return [record_fn(item) for item in obj]
    return record_fn(obj)


def _select_fields(obj: Any, fields: list[str]) -> Any:
    """Select only the specified fields from records."""
    return _apply_to_records(obj, lambda r: _pick_fields_from_record(r, fields))


def _exclude_fields(obj: Any, fields: list[str]) -> Any:
    """Remove the specified fields from records."""
    return _apply_to_records(obj, lambda r: _drop_fields_from_record(r, fields))


@mcp.tool(name="current_datetime")
def current_datetime() -> str:
    """Get the current date and time in ISO 8601 format (UTC)."""
    return datetime.now(UTC).isoformat()


@mcp.tool(name="get_instructions")
def get_instructions() -> str:
    """Get the instructions for using this MCP server effectively.

    Call this tool when you need a reminder of best practices for querying data,
    including action selection, field selection, query sizing, and date range handling.
    """
    return _INSTRUCTIONS


# Global reference to loaded connector (set during server initialization)
_connector: Any | None = None


def _require_connector() -> Any:
    """Get the connector, raising if not initialized."""
    if _connector is None:
        raise RuntimeError("Connector not initialized")
    return _connector


def _transform_response(
    result: dict[str, Any],
    action: str,
    select_fields: list[str] | None,
    exclude_fields: list[str] | None,
) -> dict[str, Any]:
    """Transform API response with field selection, truncation, and compaction.

    For list/search actions, extracts records from envelope, transforms them,
    and puts them back. For other actions, transforms the result directly.

    Raises:
        KeyError: If expected envelope key is missing from list/search response.
    """
    records = result
    # Determine envelope structure based on action type
    if action in COLLECTION_ACTIONS:
        if ENVELOPE_DATA_FIELD[action] not in result:
            raise KeyError(f"{action.capitalize()} response missing '{ENVELOPE_DATA_FIELD[action]}' envelope key. Got keys: {list(result.keys())}")
        records = result[ENVELOPE_DATA_FIELD[action]]

    # Search hits nest entity data under "data" key
    if action == ACTION_SEARCH:
        if select_fields:
            select_fields = [f"data.{f}" for f in select_fields]
        if exclude_fields:
            exclude_fields = [f"data.{f}" for f in exclude_fields]

    # Apply transformations
    if select_fields:
        records = _select_fields(records, select_fields)
    elif exclude_fields:
        records = _exclude_fields(records, exclude_fields)

    if action in COLLECTION_ACTIONS:
        records = _truncate_long_text(records)

    records = _compact(records)

    # Reconstruct response
    if action in COLLECTION_ACTIONS:
        result[ENVELOPE_DATA_FIELD[action]] = records
        return result

    return records


def register_connector_tools(connector: Any) -> None:
    """Register connector-specific MCP tools dynamically.

    This function creates and registers three tools:
    1. connector_info - Returns connector metadata and available entities
    2. execute - Executes entity operations (uses tool_utils decorator)
    3. entity_schema - Returns JSON schema for an entity

    Args:
        connector: Instantiated connector object with list_entities(), execute(),
                   entity_schema(), and tool_utils methods.
    """
    global _connector
    _connector = connector

    # Tool 1: Connector info/metadata
    @mcp.tool(name="connector_info")
    def connector_info() -> dict[str, Any]:
        """Get connector metadata including version and available entities/actions.

        Returns a dict with:
        - connector_name: Name of the connector
        - connector_version: Version string
        - entities: List of entity descriptions with available actions and parameters
        """
        connector = _require_connector()
        return {
            "connector_name": connector.connector_name,
            "connector_version": connector.connector_version,
            "entities": connector.list_entities(),
        }

    # Tool 2: Execute operations - uses tool_utils for docstring/output handling
    # We need to define the function first, then apply the decorator
    async def _execute_impl(
        entity: str,
        action: str,
        params: dict[str, Any] | None = None,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
    ) -> Any:
        """Execute an operation on a connector entity.

        Args:
            entity: Entity name (e.g., "users", "calls")
            action: Operation to perform (e.g., "list", "get", "search")
            params: Operation parameters as a dict
            select_fields: Optional list of field names to include in the response (allowlist).
                Supports dot notation for nested fields (e.g., "content.topics").
                When provided, only the specified fields are returned per record.
            exclude_fields: Optional list of field names to remove from the response (blocklist).
                Supports dot notation for nested fields (e.g., "content.brief").
                Ignored if select_fields is provided.

        Returns:
            Operation result (structure varies by entity/action)
        """
        connector = _require_connector()

        if action == ACTION_DOWNLOAD:
            return await _handle_download(entity, action, params or {})

        result = _to_dict(await connector.execute(entity, action, params or {}))
        return _transform_response(result, action, select_fields, exclude_fields)

    # Apply tool_utils decorator for docstring augmentation and output limits
    decorated_execute = connector.tool_utils(max_output_chars=None)(_execute_impl)

    # Register with MCP
    mcp.tool(name="execute")(decorated_execute)

    # Tool 3: Entity schema lookup
    @mcp.tool(name="entity_schema")
    def entity_schema(entity: str) -> dict[str, Any] | None:
        """Get the JSON schema for a specific entity.

        Args:
            entity: Entity name to get schema for (e.g., "users", "calls")

        Returns:
            JSON schema dict describing the entity structure, or None if not found.
        """
        connector = _require_connector()
        return connector.entity_schema(entity)
