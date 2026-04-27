"""Public `translate_exceptions` decorator.

Wraps a sync or async function so that:

1. Output exceeding `max_output_chars` is converted to the active framework's
   retry signal (e.g. `ModelRetry` for pydantic-ai).
2. Transient runtime errors (`RateLimitError`, `NetworkError`, `TimeoutError`,
   429/5xx HTTP responses) can be retried `internal_retries` times before
   surfacing to the framework.
3. Non-retryable exceptions are translated through the strategy on the very
   first attempt — matching `auto_retry_tool`'s historical behavior.

Behaviour mirrors `backend/app/agents/util.py:auto_retry_tool` line-for-line
except for two intentional substitutions:

- `fastapi.HTTPException` recognition uses narrowed duck-typing on
  `status_code` (see `_predicates.py`).
- `logfire.warning` is soft-imported; falls back to `logging.warning` when
  logfire is not present.
"""

from __future__ import annotations

import inspect
import logging
from collections.abc import Callable
from functools import wraps
from typing import Any, overload

from ._output import DEFAULT_MAX_OUTPUT_CHARS, _check_output_size, _OutputTooLargeSignal
from ._predicates import _is_retryable_runtime_error
from ._strategies import (
    _STRATEGIES,
    FrameworkName,
    _preexisting_signal_class,
    _Raise,
    _Return,
    _TranslationSignal,
)

logger = logging.getLogger(__name__)

# Auto-detect order: try each framework's canonical import; first success wins.
# Only consulted when the caller does NOT pass an explicit `framework=` kwarg.
_AUTO_DETECT_ORDER: tuple[tuple[FrameworkName, str], ...] = (
    ("pydantic_ai", "pydantic_ai"),
    ("langchain", "langchain_core"),
    ("openai_agents", "agents"),
    ("mcp", "mcp"),
)

_CACHED_FRAMEWORK: FrameworkName | None = None

# Cached at module level so we don't re-attempt `import logfire` on every retry call.
_CACHED_LOGFIRE: Any = None
_LOGFIRE_PROBED: bool = False


def _reset_cached_framework_for_tests() -> None:
    """Test helper: clear the auto-detect cache between cases that mock framework presence."""
    global _CACHED_FRAMEWORK
    _CACHED_FRAMEWORK = None


def _reset_cached_logfire_for_tests() -> None:
    """Test helper: clear the logfire-probe cache between cases that mock logfire presence."""
    global _CACHED_LOGFIRE, _LOGFIRE_PROBED
    _CACHED_LOGFIRE = None
    _LOGFIRE_PROBED = False


def _detect_framework() -> FrameworkName:
    """Return the first installed framework in `_AUTO_DETECT_ORDER`.

    Caches the result on a module-level singleton; tests use
    `_reset_cached_framework_for_tests()` to clear between cases.
    """
    global _CACHED_FRAMEWORK
    if _CACHED_FRAMEWORK is not None:
        return _CACHED_FRAMEWORK

    import importlib

    for framework_name, module_name in _AUTO_DETECT_ORDER:
        try:
            importlib.import_module(module_name)
        except ImportError:
            continue
        _CACHED_FRAMEWORK = framework_name
        return framework_name

    raise RuntimeError(
        "translate_exceptions could not auto-detect an installed framework. "
        "Pass framework='pydantic_ai' | 'langchain' | 'openai_agents' | 'mcp' explicitly, "
        "or install one of: pydantic_ai, langchain_core, agents (openai-agents), mcp."
    )


def _emit_retry_telemetry(*, tool_name: str, attempt: int, max_attempts: int, error_type: str) -> None:
    """Best-effort retry telemetry. Prefers logfire if installed; else logging.warning.

    The logfire probe is cached at module level (see `_CACHED_LOGFIRE` /
    `_LOGFIRE_PROBED`) so we attempt `import logfire` at most once per process,
    not on every retry call.
    """
    global _CACHED_LOGFIRE, _LOGFIRE_PROBED
    if not _LOGFIRE_PROBED:
        try:
            import logfire  # type: ignore[import-not-found]

            _CACHED_LOGFIRE = logfire
        except ImportError:
            _CACHED_LOGFIRE = None
        _LOGFIRE_PROBED = True

    if _CACHED_LOGFIRE is not None:
        _CACHED_LOGFIRE.warning(
            "Retrying tool after transient runtime failure",
            tool_name=tool_name,
            attempt=attempt,
            max_attempts=max_attempts,
            error_type=error_type,
        )
        return

    logger.warning(
        "Retrying tool %s after transient runtime failure (attempt %d/%d, error_type=%s)",
        tool_name,
        attempt,
        max_attempts,
        error_type,
    )


def _resolve_strategy(framework: FrameworkName | None) -> tuple[FrameworkName, Callable[..., _TranslationSignal]]:
    resolved: FrameworkName = framework if framework is not None else _detect_framework()
    if resolved not in _STRATEGIES:
        raise ValueError(f"Unknown framework={resolved!r}; choose from: pydantic_ai, langchain, openai_agents, mcp")
    return resolved, _STRATEGIES[resolved]


def _apply_signal(signal: _TranslationSignal, original_exc: BaseException) -> Any:
    """Honor a translation signal: raise-with-cause or return-value."""
    if isinstance(signal, _Raise):
        raise signal.exception from original_exc
    # _Return — caller must return this value
    assert isinstance(signal, _Return)
    return signal.value


@overload
def translate_exceptions(func: Callable[..., Any]) -> Callable[..., Any]: ...


@overload
def translate_exceptions(
    *,
    framework: FrameworkName | None = None,
    max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
    internal_retries: int = 0,
    should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
    exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...


def translate_exceptions(
    func: Any = None,
    *,
    framework: FrameworkName | None = None,
    max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
    internal_retries: int = 0,
    should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
    exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
) -> Any:
    """Translate tool exceptions into the active framework's retry signal.

    Args:
        func: The function to wrap (when used without arguments, e.g.
            `@translate_exceptions`).
        framework: One of `"pydantic_ai" | "langchain" | "openai_agents" |
            "mcp"`. Defaults to None → auto-detect by attempting each
            framework's canonical import in order. Explicit always wins.
        max_output_chars: Maximum serialized output size (`json.dumps`,
            `default=str`). Excess raises the framework's signal asking the
            LLM to narrow the query. Set to `None` or `0` to disable.
        internal_retries: How many transient runtime failures (429/5xx,
            network, timeout) to retry silently before surfacing. Default 0.
        should_internal_retry: Optional predicate `(error, args, kwargs) ->
            bool` further restricting which retryable errors are safe for
            this specific tool.
        exhausted_runtime_failure_message: Optional callback `(error, args,
            kwargs) -> str | None`. Invoked after internal retries are
            exhausted OR were skipped via `should_internal_retry` returning
            False. Return a non-None string to translate the failure
            through the strategy with that message; return None to re-raise
            the original exception unwrapped.

    Returns:
        The wrapped callable. Sync or async is preserved via
        `inspect.iscoroutinefunction`. `functools.wraps` preserves
        `__name__`, `__doc__`, and `__wrapped__`.

    Decoration form:
        @translate_exceptions
        def tool(...): ...

        @translate_exceptions(framework="pydantic_ai", internal_retries=2)
        async def tool(...): ...
    """

    internal_retry_gate = should_internal_retry or (lambda _error, _args, _kwargs: True)
    exhausted_runtime_failure_message_builder = exhausted_runtime_failure_message or (lambda _error, _args, _kwargs: None)

    def decorator(fn: Any) -> Any:
        # Reject generator/async-generator functions at decoration time —
        # translate_exceptions only wraps regular sync/async callables.
        if inspect.isgeneratorfunction(fn) or inspect.isasyncgenfunction(fn):
            raise TypeError(
                f"translate_exceptions does not support generator/async-generator tools "
                f"(got {fn.__name__}); return a list/dict instead"
            )

        # Double-wrap guard: if the function is already wrapped by translate_exceptions,
        # log once and return the existing wrapper unchanged. Re-wrapping would silently
        # double-translate; the marker check is the supported behavioural contract for
        # users who decorate already-public helpers.
        if getattr(fn, "__translate_exceptions_wrapped__", False):
            logger.warning(
                "translate_exceptions: %s is already wrapped — skipping double-wrap",
                fn.__name__,
            )
            return fn

        # Resolve the strategy lazily — we MUST NOT call _detect_framework() at
        # decoration time, because that would cache before tests can mock module
        # presence and would force users to install a framework just to import
        # a module that uses @translate_exceptions. The strategy is resolved on
        # first call.
        if inspect.iscoroutinefunction(fn):

            @wraps(fn)
            async def aw(*args: Any, **kwargs: Any) -> Any:
                attempt = 0
                while True:
                    try:
                        result = await fn(*args, **kwargs)
                    except _OutputTooLargeSignal as e:  # pragma: no cover — defence in depth
                        _resolved_framework, strategy = _resolve_strategy(framework)
                        signal = strategy(e, e.message)
                        return _apply_signal(signal, e)
                    except BaseException as e:
                        if not isinstance(e, Exception):
                            # KeyboardInterrupt / SystemExit / etc. — never run framework
                            # imports during interrupt unwinds.
                            raise

                        # Pre-existing framework signal? Propagate unwrapped.
                        resolved_framework, strategy = _resolve_strategy(framework)
                        signal_cls = _preexisting_signal_class(resolved_framework)
                        if signal_cls is not None and isinstance(e, signal_cls):
                            raise

                        logger.exception("Tool %s raised %s", fn.__name__, type(e).__name__)
                        is_retryable = _is_retryable_runtime_error(e)
                        can_retry_internally = is_retryable and internal_retry_gate(e, args, kwargs)
                        if attempt < internal_retries and can_retry_internally:
                            attempt += 1
                            _emit_retry_telemetry(
                                tool_name=fn.__name__,
                                attempt=attempt,
                                max_attempts=internal_retries + 1,
                                error_type=type(e).__name__,
                            )
                            continue
                        if internal_retries > 0 and is_retryable:
                            exhausted_message = exhausted_runtime_failure_message_builder(e, args, kwargs)
                            if exhausted_message is not None:
                                signal = strategy(e, exhausted_message)
                                return _apply_signal(signal, e)
                            raise
                        signal = strategy(e)
                        return _apply_signal(signal, e)

                    # Output-size check — sentinel translates via strategy too.
                    try:
                        return _check_output_size(result, max_output_chars, fn.__name__)
                    except _OutputTooLargeSignal as e:
                        _resolved_framework, strategy = _resolve_strategy(framework)
                        signal = strategy(e, e.message)
                        return _apply_signal(signal, e)

            aw.__translate_exceptions_wrapped__ = True  # type: ignore[attr-defined]
            return aw

        @wraps(fn)
        def sw(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while True:
                try:
                    result = fn(*args, **kwargs)
                except _OutputTooLargeSignal as e:  # pragma: no cover — defence in depth
                    _resolved_framework, strategy = _resolve_strategy(framework)
                    signal = strategy(e, e.message)
                    return _apply_signal(signal, e)
                except BaseException as e:
                    if not isinstance(e, Exception):
                        # KeyboardInterrupt / SystemExit / etc. — never run framework
                        # imports during interrupt unwinds.
                        raise

                    resolved_framework, strategy = _resolve_strategy(framework)
                    signal_cls = _preexisting_signal_class(resolved_framework)
                    if signal_cls is not None and isinstance(e, signal_cls):
                        raise

                    logger.exception("Tool %s raised %s", fn.__name__, type(e).__name__)
                    is_retryable = _is_retryable_runtime_error(e)
                    can_retry_internally = is_retryable and internal_retry_gate(e, args, kwargs)
                    if attempt < internal_retries and can_retry_internally:
                        attempt += 1
                        _emit_retry_telemetry(
                            tool_name=fn.__name__,
                            attempt=attempt,
                            max_attempts=internal_retries + 1,
                            error_type=type(e).__name__,
                        )
                        continue
                    if internal_retries > 0 and is_retryable:
                        exhausted_message = exhausted_runtime_failure_message_builder(e, args, kwargs)
                        if exhausted_message is not None:
                            signal = strategy(e, exhausted_message)
                            return _apply_signal(signal, e)
                        raise
                    signal = strategy(e)
                    return _apply_signal(signal, e)

                try:
                    return _check_output_size(result, max_output_chars, fn.__name__)
                except _OutputTooLargeSignal as e:
                    _resolved_framework, strategy = _resolve_strategy(framework)
                    signal = strategy(e, e.message)
                    return _apply_signal(signal, e)

        sw.__translate_exceptions_wrapped__ = True  # type: ignore[attr-defined]
        return sw

    # Support both @translate_exceptions and @translate_exceptions(framework=...)
    if func is not None:
        return decorator(func)
    return decorator


__all__ = ["translate_exceptions"]
