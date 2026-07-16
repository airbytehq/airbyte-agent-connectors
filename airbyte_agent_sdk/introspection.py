"""
Shared introspection utilities for connector metadata.

This module provides utilities for introspecting connector metadata,
generating descriptions, and formatting parameter signatures. These
functions are used by both the runtime decorators and the generated
connector code.

The module is designed to work with any object conforming to the
ConnectorModel and EndpointDefinition interfaces from airbyte_agent_sdk.types.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Protocol

# Constants
MAX_EXAMPLE_QUESTIONS = 5  # Maximum number of example questions to include in description

# --- Shared instruction sections (used by both EXECUTE_INSTRUCTIONS and generate_tool_description) ---

FILTER_OPERATORS = (
    "FILTER OPERATORS — operator is the outer key, field:value is nested inside:\n"
    '  Exact match:    {"query": {"filter": {"eq":    {"status": "completed"}}}}\n'
    '  Fuzzy text:     {"query": {"filter": {"fuzzy": {"name": "john smith"}}}}\n'
    '  Substring:      {"query": {"filter": {"like":  {"externalId": "CUS-"}}}}\n'
    '  Greater-or-eq:  {"query": {"filter": {"gte":   {"started": "2026-01-01T00:00:00Z"}}}}\n'
    '  Less than:      {"query": {"filter": {"lt":    {"amount": 1000}}}}\n'
    '  Set membership: {"query": {"filter": {"in":    {"stage": ["discovery", "negotiation"]}}}}\n'
    '  Combined (AND): {"query": {"filter": {"gte": {"started": "..."}, "eq": {"status": "completed"}}}}\n'
    "Available operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, contains, any\n"
    'Compose with and/or/not: {"and": [cond1, cond2]}, {"or": [...]}, {"not": cond}'
)

ID_RESOLUTION = (
    "ID RESOLUTION: When filtering by a related entity (person, team, project), "
    "inspect the schema above to identify primary keys and foreign keys — "
    "these are NOT always named 'id'. Look for fields that reference other entities "
    "(e.g. ownerId, accountId, assignee_id, project_key, or any field whose description or type "
    "indicates it links to another entity). Then search that related entity by name to get its key, "
    "and use it as a filter."
)

PAGINATION_PAGE_CAP = 20

PAGINATION = (
    "PAGINATION: Default limit 20-25. Don't paginate unless the user asks for 'all' or an exact count. "
    "Stop as soon as you have enough to answer. For 'how many' questions with has_more=true, say 'at least N'. "
    f"Hard stop at {PAGINATION_PAGE_CAP} pages — use filters to narrow, and say results are partial if you hit the cap."
)

DATE_RANGES = (
    "DATE RANGES INCLUDING TODAY: Search index can lag hours. "
    "Issue BOTH a context_store_search AND a list item with date parameters (in the same batch call), "
    "then merge and deduplicate by id. "
    "If the date range ends before today, search alone is sufficient. "
    "Always resolve relative date phrases like 'today' or 'yesterday' to explicit absolute "
    "timestamps and tell the user which range you used."
)

WRITE_ACTION_FAILURE_GUIDANCE = (
    "FAILURE HANDLING: If this call returns an error or indicates the target "
    "was unreachable, do NOT retry with a different target identifier "
    "(channel, recipient, conversation, repository, record, etc.). "
    "Surface the failure to the caller and let them decide. "
    "Silently substituting a destination is forbidden — return the failure "
    "instead of completing the work against a different target."
)

# MCP-specific execute instructions, appended to the backend describe_connector response
# (via describe_service.py) so models always see them even when MCP clients truncate tool
# descriptions. Framed for the MCP API shape: batched `items` list with connector_id,
# select_fields/exclude_fields, and concurrent execution.
#
# generate_tool_description() does NOT use this constant — it emits its own SDK-appropriate
# sections (execute(entity, action, params), params.fields, no batching). The shared
# constants above (FILTER_OPERATORS, ID_RESOLUTION, PAGINATION, DATE_RANGES) are composed
# into both paths so the overlapping knowledge stays in sync.
EXECUTE_INSTRUCTIONS = (
    "HOW TO CALL THE EXECUTE TOOL:\n"
    "PARAMETER NAMES ARE CASE-SENSITIVE: copy each `params` key EXACTLY as written in the action's "
    "signature (this connector uses camelCase, e.g. `fileId`, `mimeType`). Do NOT snake_case them — "
    "`file_id` is wrong and will fail with a missing-parameter error.\n"
    "RESPONSE STRUCTURE:\n"
    "  - list/api_search: {data: [...], meta: {has_more: bool}}\n"
    "  - get: Returns entity directly (no envelope)\n"
    "  To paginate: pass cursor=<last_cursor> while has_more is true"
    "\n\n"
    "ACTIONS: list, get, api_search, context_store_search, create, update, download. "
    "Use `context_store_search` as the DEFAULT — it supports filtering, sorting, and pagination. "
    "Only use `list` when: (a) you need today's data (search index may lag hours), or "
    "(b) context_store_search returned no results and you suspect indexing delay."
    "\n\n"
    "HOW TO USE DOWNLOAD:\n"
    "- By default, download returns a stream for API/SDK clients.\n"
    '- To request JSON chunks, pass params={"_airbyte_response_type": "json", "_airbyte_response_format": "text"}.\n'
    '- Use params.range_header like "bytes=0-49151" for the bounded chunk range.\n'
    '- Use "_airbyte_response_format": "base64" for binary files.\n'
    "\n\n"
    "HOW TO USE CONTEXT_STORE_SEARCH:\n"
    "action='context_store_search' uses params.query with filter, sort, and limit.\n"
    '- No filter: params={"limit": 20, "query": {}}\n'
    '- Basic:     params={"limit": 20, "query": {"filter": {...}}}\n'
    '- Sort:      params={"limit": 20, "query": {"filter": {...}, "sort": [{"created": "desc"}]}}\n'
    '- Sort only: params={"limit": 20, "query": {"sort": [{"created": "desc"}]}}\n'
    "- Never send an empty filter object; omit filter instead.\n"
    "- When searching for text, ALWAYS prefer `fuzzy` over `like`. "
    "`fuzzy` matches words in any order, ignores punctuation/casing, and handles partial names. "
    "`like` requires exact substring match and fails on typos or word reordering.\n"
    "- Example — find a user by name:\n"
    '  action="context_store_search", params={"query": {"filter": {"fuzzy": {"firstName": "Teo"}}}}\n'
    "- Only fall back to `like` when you need exact substring matching (e.g. prefix search on IDs)."
    "\n\n"
    "FIELD SELECTION (MANDATORY): Every item MUST include select_fields (allowlist) or "
    "exclude_fields (blocklist). Both support dot-notation for nested fields "
    '(e.g. "billing.address.city"). Fewer fields = faster + cheaper. '
    "If both provided, select_fields wins."
    "\n\n" + FILTER_OPERATORS + "\n\n" + ID_RESOLUTION + "\n\n" + PAGINATION + "\n\n" + DATE_RANGES
)

# ALPHA semantic-search alternate syntax. The note is rendered per configured semantic
# field from the connector's x-airbyte-semantic-search annotation so every describe/tool
# surface advertises identical, connector-accurate wording. Lines carry no leading indent
# so callers can indent to match their surrounding block.

# Generic, connector-agnostic guidance shared by every rendered note.
_SEMANTIC_SEARCH_GENERIC_GUIDANCE = (
    "  `query` and `semantic` are mutually exclusive — never pass both in the same request. "
    "Results are ordered by similarity, so `sort` is not supported.\n"
    "  When using `semantic`, any filter must go inside `semantic.filter` (same shape/operators as `query.filter`). "
    "A top-level `query.filter` is ignored when `semantic` is present.\n"
    "  `dedup` controls entity deduplication: `max` (default) returns only the single best-scoring chunk per parent "
    "record (one hit per source entity); `none` disables that collapse so multiple chunks from the same record may "
    "appear, still ranked by similarity and capped by `limit`. Use `none` when you need more than one passage per "
    "record, and raise `limit` if the top `limit` chunks are not enough.\n"
    "  `prompt` is the only required input. `field` is optional — when the connector indexes a single semantic "
    "field it is selected automatically, so pass it only to choose among multiple indexed fields. `fields` "
    "(result projection), `limit`, and `context_size` are all optional too.\n"
    "  `fields` narrows the returned hit to an allowlist -- use the entity field names shown above (NOT direct-API "
    "names). If you will act on a hit afterward (e.g. download a file), keep the fields that call needs -- for file "
    "entities that means `mime_type` and `file_name`, which tell you how to fetch the file."
)


def _humanize_entity_name(entity_name: str) -> str:
    """Turn an entity identifier into prose (e.g. 'support_tickets' -> 'support tickets')."""
    return entity_name.replace("_", " ").strip() or entity_name


def _semantic_metadata_names(config: Any, *, record_root: bool) -> list[str]:
    """Names of metadata fields whose path is (or is not) record-root anchored.

    A leading '/' on the metadata path resolves from the record root (entity-level
    fields); any other path is relative to the sampled unit (per-unit attribution).
    """
    names: list[str] = []
    for meta in getattr(config, "metadata", None) or []:
        path = getattr(meta, "path", "") or ""
        name = getattr(meta, "name", None)
        if not name:
            continue
        if path.startswith("/") == record_root:
            names.append(name)
    return names


def build_semantic_search_note(
    config: Any,
    *,
    entity_name: str,
    field_name: str,
    enrichment_outputs: Sequence[str] = (),
) -> str:
    """Render the ALPHA semantic-search note for one configured field.

    The structure is fixed; the connector-specific facts are pulled from the
    field's ``x-airbyte-semantic-search`` config (``config``):

    - the searchable field name + entity it lives on,
    - the entity-block fields = metadata whose ``path`` starts with ``/`` (record root),
    - the per-unit attribution = metadata whose ``path`` does not start with ``/``,
    - the context-window cap = ``windowing.context_max_chars`` (0/omitted => unbounded).

    ``enrichment_outputs`` are entity-level x-airbyte-enrichment fields added to each
    hit's ``metadata`` at read time (e.g. a speaker's name resolved from a related
    entity); they are advertised so the agent knows they are available to read. They
    are returned only, NOT filterable (the join runs after similarity ranking).

    The generic guidance (query/semantic exclusivity, no sort, ``semantic.filter``,
    ``context_size`` advice) is verbatim and connector-independent.
    """
    entity_label = _humanize_entity_name(entity_name)
    entity_fields = _semantic_metadata_names(config, record_root=True)
    attribution_fields = _semantic_metadata_names(config, record_root=False)

    windowing = getattr(config, "windowing", None)
    context_max_chars = getattr(windowing, "context_max_chars", 0) or 0

    entity_clause = f" `entity` has the {entity_label} fields ({', '.join(entity_fields)});" if entity_fields else ""
    attribution_clause = f", and per-unit attribution ({', '.join(attribution_fields)})" if attribution_fields else ""
    enrichment_clause = (
        f"  `metadata` also carries enriched fields resolved from related entities at read time "
        f"({', '.join(enrichment_outputs)}); these are returned for reading only and are NOT filterable.\n"
        if enrichment_outputs
        else ""
    )

    if context_max_chars > 0:
        context_clause = (
            f"  `context_size` controls how many characters of surrounding context are returned per hit "
            f"(default: full {context_max_chars}-char window, maximum: {context_max_chars}). "
            "Set it large enough for summarization and reasoning about follow-up searches so you avoid "
            "unnecessary extra calls."
        )
    else:
        context_clause = (
            "  `context_size` controls how many characters of surrounding context are returned per hit. "
            "Set it large enough for summarization and reasoning about follow-up searches so you avoid "
            "unnecessary extra calls."
        )

    return (
        "- context_store_search(semantic={prompt, field?, filter?, context_size?, dedup?}, fields?, limit?)\n"
        f"  ALPHA — subject to change. Semantic (similarity) search over the '{field_name}' field of {entity_label}.\n"
        f"  Embeds `prompt` and returns relevance-ranked hits shaped as {{entity, metadata}}:{entity_clause} "
        f"`metadata` has the similarity `score`, the matched `context` text{attribution_clause}.\n"
        f"{enrichment_clause}"
        f"{_SEMANTIC_SEARCH_GENERIC_GUIDANCE}\n"
        f"{context_clause}"
    )


def semantic_search_note_lines(
    entity_semantic_fields: dict[str, Any] | None,
    *,
    entity_name: str,
    indent: str = "      ",
    enrichment_outputs: Sequence[str] = (),
) -> list[str]:
    """Return indented ALPHA semantic-search note lines for an entity's configured fields.

    ``entity_semantic_fields`` is the per-entity ``{field_name: SemanticSearchConfig}``
    mapping (e.g. ``ConnectorModel.semantic_search_fields[entity_name]``). Returns the
    concatenated note lines for every configured semantic field, or an empty list when
    the entity has none. ``enrichment_outputs`` are the entity's x-airbyte-enrichment
    output fields, advertised in each field's metadata description.
    """
    if not entity_semantic_fields:
        return []
    lines: list[str] = []
    for field_name, config in entity_semantic_fields.items():
        note = build_semantic_search_note(config, entity_name=entity_name, field_name=field_name, enrichment_outputs=enrichment_outputs)
        lines.extend(f"{indent}{line}" for line in note.split("\n"))
    return lines


def build_semantic_sql_table_function_note(
    config: Any,
    *,
    entity_name: str,
    field_name: str,
    enrichment_outputs: Sequence[str] = (),
) -> str:
    """Render SQL table-function guidance for one configured semantic field."""
    windowing = getattr(config, "windowing", None)
    context_max_chars = getattr(windowing, "context_max_chars", 0) or 0
    context_clause = f" capped at {context_max_chars} chars" if context_max_chars > 0 else ""
    enrichment_clause = (
        f" Add `enrich => true` to expose configured enrichment columns ({', '.join(enrichment_outputs)}); "
        "without it the relation returns only semantic metadata plus `score` and `context`."
        if enrichment_outputs
        else " `enrich` defaults to false."
    )
    return (
        "- context_store_sql_query(sql, limit?) can compose semantic search with SQL via "
        f"`semantic_search(entity => '{entity_name}', field => '{field_name}', prompt => '...', "
        "filter => ..., limit => ..., context_size => ..., dedup => 'max', enrich => true)`.\n"
        "  Use it in FROM/JOIN/CTEs when you need joins, aggregations, projections, or SQL post-filters over relevance-ranked hits. "
        "`prompt` must be a literal string. `filter => ...` inside semantic_search is the pre-ranking filter; "
        "outer WHERE runs after the inner top-k. "
        "`dedup => 'max'` is the default and returns the single best-scoring chunk per parent record; "
        "use `dedup => 'none'` to keep multiple matching chunks from the same record. "
        f"The relation returns metadata columns plus computed `score` and `context`{context_clause}; "
        f"embeddings table/model/vector columns are hidden.{enrichment_clause}"
    )


def semantic_sql_table_function_note_lines(
    entity_semantic_fields: dict[str, Any] | None,
    *,
    entity_name: str,
    indent: str = "      ",
    enrichment_outputs: Sequence[str] = (),
) -> list[str]:
    if not entity_semantic_fields:
        return []
    lines: list[str] = []
    for field_name, config in entity_semantic_fields.items():
        note = build_semantic_sql_table_function_note(
            config,
            entity_name=entity_name,
            field_name=field_name,
            enrichment_outputs=enrichment_outputs,
        )
        lines.extend(f"{indent}{line}" for line in note.split("\n"))
    return lines


def build_enrichment_note(config: Any, *, entity_name: str) -> str:
    """Render a one-line note for a single x-airbyte-enrichment join.

    Advertises the output fields added to each record and the related entity they
    are resolved from at read time.
    """
    target = getattr(config, "target", "") or ""
    outputs = [getattr(p, "name", None) for p in (getattr(config, "project", None) or [])]
    output_names = [name for name in outputs if name]
    entity_label = _humanize_entity_name(entity_name)
    return f"Each {entity_label} record is enriched with {', '.join(output_names)} (resolved from {target} at read time)."


def enrichment_note_lines(
    entity_enrichments: Any | None,
    *,
    entity_name: str,
    indent: str = "      ",
) -> list[str]:
    """Return indented enrichment note lines for an entity's configured joins.

    ``entity_enrichments`` is the per-entity list of EnrichmentConfig (e.g.
    ``ConnectorModel.enrichment_configs[entity_name]``). Returns one note line per
    configured join, or an empty list when the entity has none.
    """
    if not entity_enrichments:
        return []
    return [f"{indent}- {build_enrichment_note(config, entity_name=entity_name)}" for config in entity_enrichments]


def _simplify_type(type_value: str | list[str]) -> str:
    """Simplify JSON Schema type to display string. ['null', 'string'] → 'string'."""
    if isinstance(type_value, str):
        return type_value
    types = [t for t in type_value if t != "null"]
    return types[0] if types else "any"


def _format_type_with_enum(schema: dict[str, Any]) -> str:
    """Format a JSON Schema into a display type string, appending enum values when present.

    Handles three shapes:
    - scalar with top-level ``enum``    → ``string<"asc" | "desc">``
    - array whose ``items`` has ``enum`` → ``array<"OPEN" | "CLOSED">``
    - no enum present                    → ``string`` (unchanged)

    String enum values are quoted; numeric/boolean values render bare.
    """
    base = _simplify_type(schema.get("type", "string"))
    enum_values = schema.get("enum")
    if enum_values is None:
        items = schema.get("items")
        if isinstance(items, dict):
            enum_values = items.get("enum")
    if not enum_values:
        return base
    formatted = " | ".join(f'"{v}"' if isinstance(v, str) else str(v) for v in enum_values)
    return f"{base}<{formatted}>"


def _format_ai_hint_lines(hints: dict[str, Any], indent: str = "    ") -> list[str]:
    """Format ai_hints dict into indented lines."""
    lines: list[str] = []
    if hints.get("when_to_use"):
        lines.append(f"{indent}WHEN TO USE: {hints['when_to_use']}")
    if hints.get("freshness"):
        lines.append(f"{indent}FRESHNESS: {str(hints['freshness']).upper()}")
    trigger_phrases = hints.get("trigger_phrases", [])
    if trigger_phrases and isinstance(trigger_phrases, list):
        lines.append(f"{indent}Trigger phrases: {', '.join(trigger_phrases)}")
    if hints.get("search_strategy"):
        lines.append(f"{indent}SEARCH STRATEGY: {hints['search_strategy']}")
    return lines


def _type_includes(type_value: Any, target: str) -> bool:
    if isinstance(type_value, list):
        return target in type_value
    return type_value == target


def _is_object_schema(schema: dict[str, Any]) -> bool:
    if "properties" in schema:
        return True
    return _type_includes(schema.get("type"), "object")


def _is_array_schema(schema: dict[str, Any]) -> bool:
    if "items" in schema:
        return True
    return _type_includes(schema.get("type"), "array")


def _dedupe_param_entries(entries: list[tuple[str, bool, str]]) -> list[tuple[str, bool, str]]:
    seen: dict[str, tuple[bool, str]] = {}
    ordered: list[str] = []
    for name, required, param_type in entries:
        if name not in seen:
            seen[name] = (required, param_type)
            ordered.append(name)
        else:
            seen[name] = (seen[name][0] or required, seen[name][1])
    return [(name, seen[name][0], seen[name][1]) for name in ordered]


def _flatten_schema_params(
    schema: dict[str, Any],
    prefix: str = "",
    parent_required: bool = True,
    seen_stack: set[int] | None = None,
) -> list[tuple[str, bool, str]]:
    if not isinstance(schema, dict):
        return []

    if seen_stack is None:
        seen_stack = set()

    schema_id = id(schema)
    if schema_id in seen_stack:
        return []

    seen_stack.add(schema_id)
    try:
        entries: list[tuple[str, bool, str]] = []

        for subschema in schema.get("allOf", []) or []:
            if isinstance(subschema, dict):
                entries.extend(_flatten_schema_params(subschema, prefix, parent_required, seen_stack))

        for keyword in ("anyOf", "oneOf"):
            for subschema in schema.get(keyword, []) or []:
                if isinstance(subschema, dict):
                    entries.extend(_flatten_schema_params(subschema, prefix, False, seen_stack))

        properties = schema.get("properties")
        if isinstance(properties, dict):
            required_fields = set(schema.get("required", [])) if isinstance(schema.get("required"), list) else set()
            for prop_name, prop_schema in properties.items():
                path = f"{prefix}{prop_name}" if prefix else prop_name
                is_required = parent_required and prop_name in required_fields
                type_str = _format_type_with_enum(prop_schema) if isinstance(prop_schema, dict) else "string"
                entries.append((path, is_required, type_str))

                if isinstance(prop_schema, dict):
                    if _is_array_schema(prop_schema):
                        array_path = f"{path}[]"
                        entries.append((array_path, is_required, "array"))
                        items = prop_schema.get("items")
                        if isinstance(items, dict):
                            entries.extend(_flatten_schema_params(items, prefix=f"{array_path}.", parent_required=is_required, seen_stack=seen_stack))
                    if _is_object_schema(prop_schema):
                        entries.extend(_flatten_schema_params(prop_schema, prefix=f"{path}.", parent_required=is_required, seen_stack=seen_stack))

        return _dedupe_param_entries(entries)
    finally:
        seen_stack.remove(schema_id)


def _cache_field_value(field: Any, key: str) -> Any:
    if isinstance(field, dict):
        return field.get(key)
    return getattr(field, key, None)


def _flatten_cache_properties(properties: dict[str, Any], prefix: str) -> list[str]:
    entries: list[str] = []
    for prop_name, prop in properties.items():
        path = f"{prefix}{prop_name}" if prefix else prop_name
        entries.append(path)

        prop_type = _cache_field_value(prop, "type")
        prop_properties = _cache_field_value(prop, "properties")

        if _type_includes(prop_type, "array"):
            array_path = f"{path}[]"
            entries.append(array_path)
            if isinstance(prop_properties, dict):
                entries.extend(_flatten_cache_properties(prop_properties, prefix=f"{array_path}."))
        elif isinstance(prop_properties, dict):
            entries.extend(_flatten_cache_properties(prop_properties, prefix=f"{path}."))

    return entries


def _flatten_cache_field_paths(field: Any) -> list[str]:
    field_name = _cache_field_value(field, "name")
    if not isinstance(field_name, str) or not field_name:
        return []

    field_type = _cache_field_value(field, "type")
    field_properties = _cache_field_value(field, "properties")

    entries = [field_name]
    if _type_includes(field_type, "array"):
        array_path = f"{field_name}[]"
        entries.append(array_path)
        if isinstance(field_properties, dict):
            entries.extend(_flatten_cache_properties(field_properties, prefix=f"{array_path}."))
    elif isinstance(field_properties, dict):
        entries.extend(_flatten_cache_properties(field_properties, prefix=f"{field_name}."))

    return entries


def _dedupe_strings(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            ordered.append(value)
    return ordered


def _collect_search_field_paths(model: ConnectorModelProtocol) -> dict[str, list[str]]:
    search_field_paths = getattr(model, "search_field_paths", None)
    if isinstance(search_field_paths, dict) and search_field_paths:
        normalized: dict[str, list[str]] = {}
        for entity, fields in search_field_paths.items():
            if not isinstance(entity, str) or not entity:
                continue
            if isinstance(fields, list):
                normalized[entity] = _dedupe_strings([field for field in fields if isinstance(field, str) and field])
        return normalized

    openapi_spec = getattr(model, "openapi_spec", None)
    info = getattr(openapi_spec, "info", None)
    cache_config = getattr(info, "x_airbyte_context_store", None)
    entities = getattr(cache_config, "entities", None)
    if not isinstance(entities, list):
        return {}

    search_fields: dict[str, list[str]] = {}
    for entity in entities:
        entity_name = _cache_field_value(entity, "entity")
        if not isinstance(entity_name, str) or not entity_name:
            continue

        fields = _cache_field_value(entity, "fields") or []
        if not isinstance(fields, list):
            continue
        field_paths: list[str] = []
        for field in fields:
            field_paths.extend(_flatten_cache_field_paths(field))

        search_fields[entity_name] = _dedupe_strings(field_paths)

    return search_fields


def _collect_entity_field_schemas(model: ConnectorModelProtocol) -> dict[str, list[dict[str, Any]]]:
    """Collect per-entity field schemas from cache config."""
    openapi_spec = getattr(model, "openapi_spec", None)
    info = getattr(openapi_spec, "info", None)
    cache_config = getattr(info, "x_airbyte_context_store", None)
    entities = getattr(cache_config, "entities", None)
    if not isinstance(entities, list):
        return {}
    result: dict[str, list[dict[str, Any]]] = {}
    for entity in entities:
        entity_name = _cache_field_value(entity, "entity")
        if not isinstance(entity_name, str) or not entity_name:
            continue
        fields_list = _cache_field_value(entity, "fields") or []
        if not isinstance(fields_list, list):
            continue
        fields = []
        for field in fields_list:
            name = _cache_field_value(field, "name")
            if not isinstance(name, str) or not name:
                continue
            fields.append(
                {
                    "name": name,
                    "type": _cache_field_value(field, "type") or "any",
                    "description": _cache_field_value(field, "description") or "",
                }
            )
        if fields:
            result[entity_name] = fields
    return result


def _build_relationship_index(
    entities: list[Any],
) -> tuple[dict[tuple[str, str], Any], dict[str, list[Any]]]:
    """Build relationship indexes from entity relationships."""
    rel_index: dict[tuple[str, str], Any] = {}
    rels_by_entity: dict[str, list[Any]] = {}
    for entity in entities:
        for rel in getattr(entity, "relationships", []) or []:
            source = getattr(rel, "source_entity", None)
            fk = getattr(rel, "foreign_key", None)
            if source and fk:
                rel_index[(source, fk)] = rel
                rels_by_entity.setdefault(source, []).append(rel)
    return rel_index, rels_by_entity


def _format_search_param_signature() -> str:
    params = ["query", "limit?", "cursor?", "fields?"]
    return f"({', '.join(params)})"


def get_cached_search_questions(example_questions: Any) -> list[str]:
    context_store_search_questions = getattr(example_questions, "context_store_search", None)
    if isinstance(context_store_search_questions, list):
        return context_store_search_questions

    legacy_search_questions = getattr(example_questions, "search", None)
    if isinstance(legacy_search_questions, list):
        return legacy_search_questions

    return []


class EndpointProtocol(Protocol):
    """Protocol defining the expected interface for endpoint parameters.

    This allows functions to work with any endpoint-like object
    that has these attributes, including EndpointDefinition and mock objects.
    """

    path_params: list[str]
    path_params_schema: dict[str, dict[str, Any]]
    query_params: list[str]
    query_params_schema: dict[str, dict[str, Any]]
    body_fields: list[str]
    request_schema: dict[str, Any] | None


class EntityProtocol(Protocol):
    """Protocol defining the expected interface for entity definitions."""

    name: str
    actions: list[Any]
    endpoints: dict[Any, EndpointProtocol]


class ConnectorModelProtocol(Protocol):
    """Protocol defining the expected interface for connector model parameters.

    This allows functions to work with any connector-like object
    that has these attributes, including ConnectorModel and mock objects.
    """

    @property
    def entities(self) -> list[EntityProtocol]: ...

    @property
    def openapi_spec(self) -> Any: ...

    @property
    def search_field_paths(self) -> dict[str, list[str]] | None: ...

    @property
    def semantic_search_fields(self) -> dict[str, dict[str, Any]]: ...


def format_param_signature(endpoint: EndpointProtocol) -> str:
    """Format parameter signature for an endpoint action.

    Returns a string like: (id: string) or (limit?: integer, starting_after?: string)
    where ? = optional, unmarked = required

    Args:
        endpoint: Object conforming to EndpointProtocol (e.g., EndpointDefinition)

    Returns:
        Formatted parameter signature string
    """
    params = []

    # Defensive: safely access attributes with defaults for malformed endpoints
    path_params = getattr(endpoint, "path_params", []) or []
    query_params = getattr(endpoint, "query_params", []) or []
    query_params_schema = getattr(endpoint, "query_params_schema", {}) or {}
    body_fields = getattr(endpoint, "body_fields", []) or []
    request_schema = getattr(endpoint, "request_schema", None)

    # Path params (always required)
    for name in path_params:
        params.append(f"{name}: string")

    # Query params (skip config-injected params that are auto-populated)
    for name in query_params:
        schema = query_params_schema.get(name, {})
        if schema.get("config_inject"):
            continue
        required = schema.get("required", False)
        param_type = _format_type_with_enum(schema)
        params.append(f"{name}{'?' if not required else ''}: {param_type}")

    # Body fields (include nested params from schema when available)
    if isinstance(request_schema, dict):
        for name, required, type_str in _flatten_schema_params(request_schema):
            params.append(f"{name}{'?' if not required else ''}: {type_str}")
    elif request_schema:
        required_fields = set(request_schema.get("required", [])) if isinstance(request_schema, dict) else set()
        for name in body_fields:
            params.append(f"{name}{'?' if name not in required_fields else ''}: string")

    return f"({', '.join(params)})" if params else "()"


def describe_entities(model: ConnectorModelProtocol) -> list[dict[str, Any]]:
    """Generate entity descriptions from ConnectorModel.

    Returns a list of entity descriptions with detailed parameter information
    for each action. This is used by generated connectors' list_entities() method.

    Args:
        model: Object conforming to ConnectorModelProtocol (e.g., ConnectorModel)

    Returns:
        List of entity description dicts with keys:
        - entity_name: Name of the entity (e.g., "contacts", "deals")
        - description: Entity description from the first endpoint
        - available_actions: List of actions (e.g., ["list", "get", "create"])
        - parameters: Dict mapping action -> list of parameter dicts
    """
    entities = []
    for entity_def in model.entities:
        description = ""
        parameters: dict[str, list[dict[str, Any]]] = {}

        endpoints = getattr(entity_def, "endpoints", {}) or {}
        if endpoints:
            for action, endpoint in endpoints.items():
                # Get description from first endpoint that has one
                if not description:
                    endpoint_desc = getattr(endpoint, "description", None)
                    if endpoint_desc:
                        description = endpoint_desc

                action_params: list[dict[str, Any]] = []

                # Defensive: safely access endpoint attributes
                path_params = getattr(endpoint, "path_params", []) or []
                path_params_schema = getattr(endpoint, "path_params_schema", {}) or {}
                query_params = getattr(endpoint, "query_params", []) or []
                query_params_schema = getattr(endpoint, "query_params_schema", {}) or {}
                body_fields = getattr(endpoint, "body_fields", []) or []
                request_schema = getattr(endpoint, "request_schema", None)

                # Path params (always required)
                for param_name in path_params:
                    schema = path_params_schema.get(param_name, {})
                    action_params.append(
                        {
                            "name": param_name,
                            "in": "path",
                            "required": True,
                            "type": schema.get("type", "string"),
                            "description": schema.get("description", ""),
                        }
                    )

                # Query params (skip config-injected params that are auto-populated)
                for param_name in query_params:
                    schema = query_params_schema.get(param_name, {})
                    if schema.get("config_inject"):
                        continue
                    query_entry: dict[str, Any] = {
                        "name": param_name,
                        "in": "query",
                        "required": schema.get("required", False),
                        "type": schema.get("type", "string"),
                        "description": schema.get("description", ""),
                    }
                    if "enum" in schema:
                        query_entry["enum"] = schema["enum"]
                    if "items" in schema:
                        query_entry["items"] = schema["items"]
                    action_params.append(query_entry)

                # Body fields
                if request_schema:
                    required_fields = request_schema.get("required", [])
                    properties = request_schema.get("properties", {})
                    for param_name in body_fields:
                        prop = properties.get(param_name, {})
                        body_entry: dict[str, Any] = {
                            "name": param_name,
                            "in": "body",
                            "required": param_name in required_fields,
                            "type": prop.get("type", "string"),
                            "description": prop.get("description", ""),
                        }
                        if isinstance(prop, dict):
                            if "enum" in prop:
                                body_entry["enum"] = prop["enum"]
                            if "items" in prop:
                                body_entry["items"] = prop["items"]
                        action_params.append(body_entry)

                if action_params:
                    # Action is an enum, use .value to get string
                    action_key = action.value if hasattr(action, "value") else str(action)
                    parameters[action_key] = action_params

        actions = getattr(entity_def, "actions", []) or []
        entities.append(
            {
                "entity_name": entity_def.name,
                "description": description,
                "available_actions": [a.value if hasattr(a, "value") else str(a) for a in actions],
                "parameters": parameters,
            }
        )

    return entities


def generate_tool_description(
    model: ConnectorModelProtocol,
    *,
    enable_semantic_sql_table_function: bool | None = None,
) -> str:
    """Generate AI tool description from connector metadata.

    Produces a detailed description that includes:
    - Per-entity/action parameter signatures with optional (?) markers
    - Response structure documentation with pagination hints
    - Example questions if available in the OpenAPI spec

    This is used by the Connector.tool_utils decorator to populate function
    docstrings for AI framework integration.

    Args:
        model: Object conforming to ConnectorModelProtocol (e.g., ConnectorModel)

    Returns:
        Formatted description string suitable for AI tool documentation
    """
    lines = []
    # NOTE: Do not insert blank lines in the docstring; pydantic-ai parsing truncates
    # at the first empty line and only keeps the initial section.

    # Entity/action parameter details (including pagination params like limit, starting_after)
    if enable_semantic_sql_table_function is None:
        enable_semantic_sql_table_function = bool(getattr(model, "enable_semantic_sql_table_function", False))
    semantic_search_fields = getattr(model, "semantic_search_fields", None) or {}
    search_field_paths = _collect_search_field_paths(model)
    entity_field_schemas = _collect_entity_field_schemas(model)
    _, rels_by_entity = _build_relationship_index(model.entities)

    # Avoid single-word CAPS headers ("ENTITIES:", "PARAMETERS:") because griffe's Google-style
    # parser classifies them as admonition/unknown sections, and pydantic-ai's _griffe.py only
    # keeps sections of kind=text — everything under such a header is silently dropped from the
    # tool description sent to the LLM. Use a prose sentence so the block stays classified as text.
    lines.append("Valid entities and their available actions (use these names exactly):")
    for entity in model.entities:
        # Emit per-entity AI hints if available
        ai_hints = getattr(entity, "ai_hints", None) or {}
        actions = getattr(entity, "actions", []) or []
        endpoints = getattr(entity, "endpoints", {}) or {}

        hint_summary = ai_hints.get("summary") if isinstance(ai_hints, dict) else None
        if not hint_summary:
            for action in actions:
                endpoint = endpoints.get(action)
                endpoint_hints = getattr(endpoint, "ai_hints", None) if endpoint else None
                if isinstance(endpoint_hints, dict) and endpoint_hints.get("summary"):
                    hint_summary = endpoint_hints["summary"]
                    break
        if hint_summary:
            lines.append(f"  {entity.name}: {hint_summary}")
        else:
            lines.append(f"  {entity.name}:")
        if isinstance(ai_hints, dict):
            lines.extend(_format_ai_hint_lines(ai_hints))

        # Fields sub-section
        cache_fields = entity_field_schemas.get(entity.name)
        if cache_fields:
            lines.append("    Fields:")
            for field in cache_fields:
                field_name = field["name"]
                simplified = _simplify_type(field["type"])
                line = f"      {field_name}: {simplified}"
                if field.get("description"):
                    line += f" — {field['description']}"
                lines.append(line)

        # Relationships sub-section
        entity_rels = rels_by_entity.get(entity.name, [])
        if entity_rels:
            lines.append("    Relationships:")
            for rel in entity_rels:
                fk = getattr(rel, "foreign_key", "")
                target = getattr(rel, "target_entity", "")
                target_key = getattr(rel, "target_key", "id")
                line = f"      {fk} → {target}.{target_key}"
                cardinality = getattr(rel, "cardinality", None)
                if cardinality:
                    line += f" ({cardinality.replace('_', '-')})"
                rel_desc = getattr(rel, "description", None)
                if rel_desc:
                    line += f" — {rel_desc}"
                lines.append(line)

        # Actions sub-section
        lines.append("    Actions:")
        for action in actions:
            action_str = action.value if hasattr(action, "value") else str(action)
            endpoint = endpoints.get(action)
            if endpoint:
                param_sig = format_param_signature(endpoint)
                lines.append(f"      - {action_str}{param_sig}")
                endpoint_hints = getattr(endpoint, "ai_hints", None)
                if isinstance(endpoint_hints, dict):
                    lines.extend(_format_ai_hint_lines(endpoint_hints, indent="        "))
                    hint_examples = endpoint_hints.get("example_questions", [])
                    if hint_examples and isinstance(hint_examples, list):
                        lines.append(f"        Examples: {'; '.join(hint_examples[:3])}")
                if action_str.lower() in {"create", "update", "delete"}:
                    lines.extend(f"        {line}" for line in WRITE_ACTION_FAILURE_GUIDANCE.split("\n"))
            else:
                lines.append(f"      - {action_str}()")
                if action_str.lower() in {"create", "update", "delete"}:
                    lines.extend(f"        {line}" for line in WRITE_ACTION_FAILURE_GUIDANCE.split("\n"))
        if entity.name in search_field_paths:
            search_sig = _format_search_param_signature()
            lines.append(f"      - context_store_search{search_sig}")
            lines.extend(semantic_search_note_lines(semantic_search_fields.get(entity.name), entity_name=entity.name))
            if enable_semantic_sql_table_function:
                lines.extend(semantic_sql_table_function_note_lines(semantic_search_fields.get(entity.name), entity_name=entity.name))

        # Searchable fields sub-section (nested paths for search queries)
        entity_search_fields = search_field_paths.get(entity.name)
        if entity_search_fields:
            display_fields = entity_search_fields[:20]
            suffix = f" (and {len(entity_search_fields) - 20} more)" if len(entity_search_fields) > 20 else ""
            lines.append(f"    Searchable fields: {', '.join(display_fields)}{suffix}")

        # Per-entity example questions from ai_hints
        hint_examples = ai_hints.get("example_questions", []) if isinstance(ai_hints, dict) else []
        if hint_examples:
            lines.append(f"    Examples: {'; '.join(hint_examples[:3])}")

    # Response structure
    lines.append("RESPONSE STRUCTURE:")
    lines.append("  - list/api_search: {data: [...], meta: {has_more: bool}}")
    lines.append("  - get: Returns entity directly (no envelope)")
    lines.append("  To paginate: pass starting_after=<last_id> while has_more is true")

    # Guidelines — prose header; see note at ENTITIES above.
    lines.append("General guidelines for calling this tool:")
    lines.append('  - Prefer cached search over direct API calls: action="context_store_search" whenever possible.')
    lines.append("  - Direct API actions (list/get/download) are slower and should be used only if search cannot answer the query.")
    lines.append("  - Keep results small: use params.fields, params.query.filter, small params.limit, and cursor pagination.")
    lines.append("  - If output is too large, refine the query with tighter filters/fields/limit.")
    lines.append("  - When searching for text, ALWAYS prefer `fuzzy` over `like`.")
    lines.append("    `fuzzy` matches words in any order, ignores punctuation/casing, and handles partial names.")
    lines.append("    `like` requires exact substring match and fails on typos or word reordering.")
    lines.append("    Only fall back to `like` when you need exact substring matching (e.g. prefix search on IDs).")

    # Search section — only if entities have searchable fields.
    # Prose header; see note at ENTITIES above.
    if search_field_paths:
        lines.append("Context Store search (cached data):")
        lines.append('  execute(entity, action="context_store_search", params={')
        lines.append('    "query": {"filter": <condition>, "sort": [{"field": "asc|desc"}, ...]},')
        lines.append('    "limit": <int>, "cursor": <str>, "fields": ["field", "nested.field", ...]')
        lines.append("  })")
        lines.append('  No filter: use "query": {} or "query": {"sort": [{"field": "desc"}]}; never send "filter": {}.')
        lines.append('  Example: {"query": {"filter": {"eq": {"title": "Intro to Airbyte | Miinto"}}}, "limit": 1,')
        lines.append('            "fields": ["id", "title", "started", "primaryUserId"]}')
        lines.append("  Conditions are composable:")
        lines.append("    - eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, contains, any")
        lines.append('    - and/or/not to combine conditions (e.g., {"and": [cond1, cond2]})')

    # Shared constants — these are the single source of truth, also composed into
    # EXECUTE_INSTRUCTIONS (the MCP/backend path). Split into lines here because
    # pydantic-ai/griffe truncates docstrings at blank lines, so we can't use the
    # constants' \n\n separators directly.
    lines.extend(FILTER_OPERATORS.split("\n"))
    lines.extend(ID_RESOLUTION.split("\n"))
    lines.extend(PAGINATION.split("\n"))
    lines.extend(DATE_RANGES.split("\n"))

    # Add example questions — try direct model field first, fall back to openapi_spec
    example_questions = getattr(model, "example_questions", None)
    if not example_questions:
        openapi_spec = getattr(model, "openapi_spec", None)
        if openapi_spec:
            info = getattr(openapi_spec, "info", None)
            if info:
                example_questions = getattr(info, "x_airbyte_example_questions", None)
    if example_questions:
        direct_questions = getattr(example_questions, "direct", None)
        search_questions = get_cached_search_questions(example_questions)

        direct_questions = direct_questions if isinstance(direct_questions, list) else []

        selected_questions: list[str] = []
        if direct_questions or search_questions:
            if search_questions:
                selected_questions = list(search_questions)
            else:
                selected_questions = list(direct_questions)

        if selected_questions:
            lines.append("EXAMPLE QUESTIONS:")
            for q in selected_questions[:MAX_EXAMPLE_QUESTIONS]:
                lines.append(f"  - {q}")

    # Function parameters — SDK API shape
    lines.append("FUNCTION PARAMETERS:")
    lines.append("  - entity: Entity name (string)")
    lines.append("  - action: Operation to perform (string)")
    lines.append("  - params: Operation parameters (dict) - see entity details above")
    lines.append("Parameter markers: ? = optional, unmarked = required")

    return "\n".join(lines)
