"""Exception-to-framework-signal translation for tool callables.

Public entry points:

- [`translate_exceptions`](#translate_exceptions) — decorator that wraps a
  sync or async tool callable and converts runtime errors into the active
  framework's retry signal (`ModelRetry` for pydantic-ai,
  `ToolException` for LangChain, return-string for OpenAI Agents,
  `ToolError` for FastMCP).
- [`DEFAULT_MAX_OUTPUT_CHARS`](#DEFAULT_MAX_OUTPUT_CHARS) — default
  serialized-output size limit (100 KB).

The implementation modules (`_predicates`, `_output`, `_strategies`,
`_decorator`) are private; their underscore prefix marks them as
unsupported. Public consumers should import from `airbyte_agent_sdk` or
this `airbyte_agent_sdk.translation` package only.
"""

from __future__ import annotations

from ._decorator import translate_exceptions
from ._output import DEFAULT_MAX_OUTPUT_CHARS
from ._strategies import FrameworkName

__all__ = [
    "translate_exceptions",
    "DEFAULT_MAX_OUTPUT_CHARS",
    "FrameworkName",
]
