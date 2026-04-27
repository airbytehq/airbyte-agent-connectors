"""Per-framework translation strategies for `translate_exceptions`.

Each strategy soft-imports its framework's exception class **inside** the
function body — never at module load time. The SDK MUST NOT depend on
pydantic-ai / langchain-core / openai-agents / fastmcp at runtime.

Each strategy returns a `_TranslationSignal`:

- `Raise(exception_to_raise)` — the decorator wrapper raises the exception
  with `from original_exc` so `__cause__` is preserved.
- `Return(value_to_return)` — the decorator wrapper returns the value
  instead of raising. Used by `framework="openai_agents"` because the
  OpenAI Agents SDK does not catch exceptions inside `on_invoke_tool`; the
  agent expects the tool to return a string describing the error.

Pre-existing framework signals (e.g. user code already raised `ModelRetry`)
are NOT translated — they propagate unwrapped from the decorator wrapper. The
decorator handles that by checking the original exception type **before**
invoking the strategy; this module's strategies are only called for non-signal
exceptions.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Literal

FrameworkName = Literal["pydantic_ai", "langchain", "openai_agents", "mcp"]


# ---------------------------------------------------------------------------
# Translation signal envelope
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class _Raise:
    """Signal that the decorator should `raise exception from original_exc`."""

    exception: BaseException


@dataclass(frozen=True)
class _Return:
    """Signal that the decorator should `return value` instead of raising."""

    value: Any


_TranslationSignal = _Raise | _Return


# ---------------------------------------------------------------------------
# Module / class lookups for pre-existing framework signals
# ---------------------------------------------------------------------------


def _try_import_pydantic_ai_model_retry() -> type[BaseException] | None:
    try:
        from pydantic_ai import ModelRetry  # type: ignore[import-not-found]
    except ImportError:
        return None
    return ModelRetry


def _try_import_langchain_tool_exception() -> type[BaseException] | None:
    try:
        from langchain_core.tools import ToolException  # type: ignore[import-not-found]
    except ImportError:
        return None
    return ToolException


def _try_import_mcp_tool_error() -> type[BaseException] | None:
    try:
        from fastmcp.exceptions import ToolError  # type: ignore[import-not-found]
    except ImportError:
        return None
    return ToolError


def _preexisting_signal_class(framework: FrameworkName) -> type[BaseException] | None:
    """Return the framework's pre-existing-signal class, or None if not applicable."""
    if framework == "pydantic_ai":
        return _try_import_pydantic_ai_model_retry()
    if framework == "langchain":
        return _try_import_langchain_tool_exception()
    if framework == "mcp":
        return _try_import_mcp_tool_error()
    # openai_agents has no pre-existing signal — it's catch-and-return-string.
    return None


# ---------------------------------------------------------------------------
# Strategies
# ---------------------------------------------------------------------------


def _format_message(error: Exception) -> str:
    """Format an exception the same way `auto_retry_tool`'s fallback did.

    Reference: `backend/app/agents/util.py:200,233`.
    """
    return f"{type(error).__name__}: {error}"


def _missing_framework_runtime_error(framework: FrameworkName, module_name: str) -> RuntimeError:
    return RuntimeError(
        f"framework={framework!r} requested but {module_name} is not installed; "
        f"choose from: pydantic_ai, langchain, openai_agents, mcp"
    )


def _pydantic_ai_translate(error: Exception, message: str | None = None) -> _TranslationSignal:
    try:
        from pydantic_ai import ModelRetry  # type: ignore[import-not-found]
    except ImportError as e:
        raise _missing_framework_runtime_error("pydantic_ai", "pydantic_ai") from e

    formatted = message if message is not None else _format_message(error)
    return _Raise(ModelRetry(formatted))


def _langchain_translate(error: Exception, message: str | None = None) -> _TranslationSignal:
    try:
        from langchain_core.tools import ToolException  # type: ignore[import-not-found]
    except ImportError as e:
        raise _missing_framework_runtime_error("langchain", "langchain_core") from e

    formatted = message if message is not None else _format_message(error)
    return _Raise(ToolException(formatted))


def _openai_agents_translate(error: Exception, message: str | None = None) -> _TranslationSignal:
    # OpenAI Agents SDK ('agents' module) has no try/except inside on_invoke_tool;
    # the agent expects the tool to return a string describing the error. We
    # still verify the framework is installed so explicit framework="openai_agents"
    # fails fast on a missing module rather than silently changing behaviour.
    try:
        import agents as _agents  # type: ignore[import-not-found]  # noqa: F401
    except ImportError as e:
        raise _missing_framework_runtime_error("openai_agents", "agents") from e

    formatted = message if message is not None else _format_message(error)
    return _Return(formatted)


def _mcp_translate(error: Exception, message: str | None = None) -> _TranslationSignal:
    # NOTE: We use fastmcp.exceptions.ToolError, NOT mcp.shared.exceptions.McpError —
    # raising McpError would crash the JSONRPC layer. ToolError is the right
    # signal for "this tool failed but the session is fine".
    try:
        from fastmcp.exceptions import ToolError  # type: ignore[import-not-found]
    except ImportError as e:
        raise _missing_framework_runtime_error("mcp", "fastmcp") from e

    formatted = message if message is not None else _format_message(error)
    return _Raise(ToolError(formatted))


_STRATEGIES: dict[FrameworkName, Callable[..., _TranslationSignal]] = {
    "pydantic_ai": _pydantic_ai_translate,
    "langchain": _langchain_translate,
    "openai_agents": _openai_agents_translate,
    "mcp": _mcp_translate,
}


__all__ = [
    "FrameworkName",
    "_TranslationSignal",
    "_Raise",
    "_Return",
    "_STRATEGIES",
    "_format_message",
    "_preexisting_signal_class",
]
