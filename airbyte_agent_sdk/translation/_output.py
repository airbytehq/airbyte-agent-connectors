"""Output-size accounting for `translate_exceptions`.

Canonical `_check_output_size(result, max_chars: int | None, tool_name: str)`
that subsumes the two pre-existing variants:

- `backend/app/agents/util.py:_check_output_size` — raised `ModelRetry`
  directly, signature `(result, max_chars: int, tool_name: str)`.
- `connector-sdk/airbyte_agent_sdk/codegen/templates/connector.py.jinja2`
  — signature `(result, max_chars: int | None, tool_name: str)`,
  routed through `_raise_output_too_large`.

The new function raises an internal `_OutputTooLargeSignal` sentinel that the
decorator catches and routes through the active framework strategy. The
sentinel is module-private and never escapes the public boundary.

Error message wording follows backend `util.py:117-123` (more informative
than the template variant).
"""

from __future__ import annotations

import json
from typing import Any


class _OutputTooLargeSignal(Exception):
    """Internal sentinel raised by `_check_output_size` when output exceeds limit.

    The decorator wrapper catches this and translates it through the active
    framework strategy (e.g. → `ModelRetry` for pydantic-ai). It MUST NEVER
    propagate to user code unwrapped.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


DEFAULT_MAX_OUTPUT_CHARS = 100_000  # ~100KB default, configurable per-tool


def _check_output_size(result: Any, max_chars: int | None, tool_name: str) -> Any:
    """Return `result` if it fits within `max_chars`; otherwise raise the sentinel.

    Args:
        result: Tool result. May be any JSON-serializable shape (or anything
            that `json.dumps(..., default=str)` can stringify).
        max_chars: Maximum serialized character length. `None` or `<= 0`
            disables size limiting.
        tool_name: Human-readable tool name for the error message.

    Returns:
        `result` unchanged when within limit (or when limit is disabled, or
        when serialization fails — the message wording mirrors backend
        `util.py:117-123`).

    Raises:
        _OutputTooLargeSignal: when serialized output exceeds `max_chars`.
    """
    if max_chars is None or max_chars <= 0:
        return result

    try:
        serialized = json.dumps(result, default=str)
    except (TypeError, ValueError):
        return result  # Can't serialize, let it through

    if len(serialized) > max_chars:
        truncated_preview = serialized[:500] + "..." if len(serialized) > 500 else serialized
        raise _OutputTooLargeSignal(
            f"Tool '{tool_name}' output too large ({len(serialized):,} chars, limit {max_chars:,}). "
            f"Please narrow your query by: adding filters via 'params', reducing the 'limit', "
            f"or (for search actions only) passing a 'fields' list for server-side projection. Preview: {truncated_preview}"
        )

    return result
