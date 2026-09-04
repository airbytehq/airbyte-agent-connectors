"""Framework-ready connector tools."""

from __future__ import annotations

import asyncio
import inspect
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Awaitable, Literal, Protocol, cast

from airbyte_agent_sdk.executor import HostedExecutor
from airbyte_agent_sdk.executor.models import HOSTED_ONLY_CONTEXT_STORE_ACTIONS
from airbyte_agent_sdk.introspection import (
    DATE_RANGES,
    FILTER_OPERATORS,
    PAGINATION,
    WRITE_ACTION_FAILURE_GUIDANCE,
    format_param_signature,
    generate_tool_description,
)
from airbyte_agent_sdk.skill_docs_renderer import render_skill_docs
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions

ToolCallable = Callable[..., Awaitable[Any]]

_LOCAL_DOCS_SKILL_ID = "local-connector-docs"


def _progressive_execute_prefix(inspect_ref: str, docs_ref: str, section_ref: str, docs_home: str) -> list[str]:
    return [
        "Execute a connector operation.",
        f"Before your first execute call, call {inspect_ref}, then {docs_ref}, then {section_ref} for the entity/action you plan to execute.",
        f"Do not guess entity, action, or parameter names. Exact names, params, fields, relationships, and examples live in {docs_home}.",
        "Use entity and action names exactly as documented by the schema and docs.",
    ]


def _progressive_size_guidance(supports_field_shaping: bool) -> str:
    if supports_field_shaping:
        return "For collection responses, keep outputs small with select_fields or exclude_fields, filters, and small limits."
    return "For collection responses, keep outputs small with filters and small limits."


_PROGRESSIVE_EXECUTE_DESCRIPTION_PREFIX = _progressive_execute_prefix(
    "inspect_connector()",
    "read_skill_docs()",
    "read_skill_docs(section=<exact section id>)",
    "read_skill_docs",
)
_PROGRESSIVE_EXECUTE_DESCRIPTION_SUFFIX = [
    "If output is too large, refine the query instead of repeating the same broad call.",
    WRITE_ACTION_FAILURE_GUIDANCE,
    FILTER_OPERATORS,
    PAGINATION,
    DATE_RANGES,
]


class ConnectorDocsProvider(Protocol):
    """Provider of connector inspection and skill-doc endpoints."""

    async def inspect_connector(self) -> dict[str, Any]: ...

    async def read_skill_docs(self, id: str, section: str | None = None) -> dict[str, Any]: ...


class SkillDocsAccessor:
    """Stateful access to one connector's skill docs.

    Owns the ``docs_skill_id`` cache: populated after the first successful
    :meth:`inspect`, re-inspected only when missing, never populated on
    failure. Cache lifetime is the accessor instance — `build_connector_tools`
    shares one across its tool closures; generated typed connectors hold one
    per connector instance.
    """

    def __init__(self, connector: Any, *, docs_provider: ConnectorDocsProvider | None = None) -> None:
        self._connector = connector
        self._provider: ConnectorDocsProvider | None = docs_provider if docs_provider is not None else _hosted_executor_for(connector)
        self._docs_skill_id: str | None = None
        self._inspect_lock = asyncio.Lock()

    @property
    def provider(self) -> ConnectorDocsProvider | None:
        return self._provider

    async def inspect(self) -> dict[str, Any]:
        """Inspect the connector's hosted metadata and resolve its docs skill id.

        Local/offline connectors (no docs provider) get a local-mode payload
        with a warning instead of a hosted inspection.
        """
        if self._provider is None:
            self._docs_skill_id = _LOCAL_DOCS_SKILL_ID
            model = _connector_model_for(self._connector)
            return {
                "mode": "local",
                "docs_skill_id": self._docs_skill_id,
                "name": getattr(model, "name", None),
                "warnings": ["Hosted connector inspection is unavailable for local/offline connectors."],
            }
        result = await self._provider.inspect_connector()
        raw_docs_skill_id = result.get("docs_skill_id")
        if not isinstance(raw_docs_skill_id, str) or not raw_docs_skill_id:
            raise ValueError("inspect_connector response did not include docs_skill_id.")
        self._docs_skill_id = raw_docs_skill_id
        return result

    async def read(self, section: str | None = None) -> str:
        """Read the connector's usage docs, rendered to text.

        Omit ``section`` for the outline and general guidance; pass an exact
        section id for full details. Local/offline connectors return the full
        generated docs and ignore ``section``.
        """
        if self._provider is None:
            docs_text = _legacy_execute_description(self._connector)
            if section is None:
                return docs_text
            return f"Section-specific docs are unavailable for local/offline connectors; full generated docs follow.\n{docs_text}"
        if self._docs_skill_id is None:
            # Concurrent first reads share one inspect round trip.
            async with self._inspect_lock:
                if self._docs_skill_id is None:
                    await self.inspect()
        if self._docs_skill_id is None:
            raise ValueError("Connector docs_skill_id could not be resolved.")
        docs = await self._provider.read_skill_docs(id=self._docs_skill_id, section=section)
        return render_skill_docs(docs)


@dataclass(frozen=True)
class ConnectorTools:
    """Connector tool callables for agent frameworks."""

    inspect_connector: ToolCallable
    read_skill_docs: ToolCallable
    execute: ToolCallable
    use_progressive_docs: bool = True

    def as_list(self) -> list[ToolCallable]:
        if not self.use_progressive_docs:
            return [self.execute]
        return [self.inspect_connector, self.read_skill_docs, self.execute]


def _hosted_executor_for(connector: Any) -> HostedExecutor | None:
    if isinstance(connector, HostedExecutor):
        return connector
    executor = getattr(connector, "_executor", None)
    if isinstance(executor, HostedExecutor):
        return executor
    return None


def _connector_model_for(connector: Any) -> Any | None:
    executor = getattr(connector, "_executor", connector)
    model = getattr(executor, "_connector_model", None)
    if model is not None:
        return model
    return getattr(executor, "model", None)


def _legacy_execute_description(connector: Any) -> str:
    model = _connector_model_for(connector)
    if model is None:
        return "Execute a direct connector operation."
    return generate_tool_description(model)


def _execute_description(connector: Any, *, use_progressive_docs: bool, docs_provider: ConnectorDocsProvider | None) -> str:
    if use_progressive_docs and docs_provider is not None:
        description_base = _progressive_execute_description_base(connector)
        action_signatures = _entity_action_signatures(connector)
        if action_signatures:
            return f"{description_base}\nValid entity/action signatures:\n{action_signatures}"
        return description_base
    return _legacy_execute_description(connector)


def _progressive_execute_description_base(connector: Any) -> str:
    size_guidance = _progressive_size_guidance(
        _supports_response_shaping_kwarg(connector, "select_fields") or _supports_response_shaping_kwarg(connector, "exclude_fields")
    )
    return "\n".join([*_PROGRESSIVE_EXECUTE_DESCRIPTION_PREFIX, size_guidance, *_PROGRESSIVE_EXECUTE_DESCRIPTION_SUFFIX])


def _literal_annotation(values: list[str]) -> Any:
    if not values:
        return str
    return Literal.__getitem__(tuple(values))


def _entity_names(connector: Any) -> list[str]:
    model = _connector_model_for(connector)
    entities = getattr(model, "entities", []) if model is not None else []
    return [entity.name for entity in entities if isinstance(getattr(entity, "name", None), str)]


def _action_value(action: Any) -> str:
    value = getattr(action, "value", action)
    return str(value)


def _action_names(connector: Any) -> list[str]:
    model = _connector_model_for(connector)
    entities = getattr(model, "entities", []) if model is not None else []
    names: set[str] = set()
    entity_names: set[str] = set()
    for entity in entities:
        actions = getattr(entity, "actions", []) or []
        entity_name = getattr(entity, "name", None)
        if actions and isinstance(entity_name, str):
            entity_names.add(entity_name)
        for action in actions:
            names.add(_action_value(action))

    context_store = getattr(model, "context_store", None)
    context_store_entities = getattr(context_store, "entities", []) or []
    if _hosted_executor_for(connector) is not None and any(
        getattr(context_store_entity, "entity", None) in entity_names for context_store_entity in context_store_entities
    ):
        names.update(HOSTED_ONLY_CONTEXT_STORE_ACTIONS)
    return sorted(names)


def _endpoint_for_action(entity: Any, action: Any) -> Any | None:
    endpoints = getattr(entity, "endpoints", {}) or {}
    if not isinstance(endpoints, dict):
        return None
    endpoint = endpoints.get(action)
    if endpoint is not None:
        return endpoint
    return endpoints.get(_action_value(action))


def _entity_action_signatures(connector: Any) -> str:
    return _entity_action_signatures_for_model(_connector_model_for(connector))


def _entity_action_signatures_for_model(model: Any) -> str:
    entities = getattr(model, "entities", []) if model is not None else []
    lines: list[str] = []
    for entity in entities:
        entity_name = getattr(entity, "name", None)
        if not isinstance(entity_name, str):
            continue
        for action in getattr(entity, "actions", []) or []:
            action_name = _action_value(action)
            endpoint = _endpoint_for_action(entity, action)
            signature = format_param_signature(endpoint) if endpoint is not None else "()"
            lines.append(f"- {entity_name}.{action_name}{signature}")
    return "\n".join(lines)


def _execute_tool_signature(connector: Any) -> inspect.Signature:
    parameters = [
        inspect.Parameter("entity", inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=_literal_annotation(_entity_names(connector))),
        inspect.Parameter("action", inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=_literal_annotation(_action_names(connector))),
        inspect.Parameter(
            "params",
            inspect.Parameter.POSITIONAL_OR_KEYWORD,
            default=None,
            annotation=dict[str, Any] | None,
        ),
    ]
    if _supports_response_shaping_kwarg(connector, "select_fields"):
        parameters.append(
            inspect.Parameter(
                "select_fields",
                inspect.Parameter.KEYWORD_ONLY,
                default=None,
                annotation=list[str] | None,
            )
        )
    if _supports_response_shaping_kwarg(connector, "exclude_fields"):
        parameters.append(
            inspect.Parameter(
                "exclude_fields",
                inspect.Parameter.KEYWORD_ONLY,
                default=None,
                annotation=list[str] | None,
            )
        )
    if _supports_response_shaping_kwarg(connector, "skip_truncation"):
        parameters.append(
            inspect.Parameter(
                "skip_truncation",
                inspect.Parameter.KEYWORD_ONLY,
                default=True,
                annotation=bool,
            )
        )
    return inspect.Signature(
        parameters=parameters,
        return_annotation=Any,
    )


def _accepts_kwarg(func: Callable[..., Any], name: str) -> bool:
    try:
        signature = inspect.signature(func)
    except (TypeError, ValueError):
        return False
    return name in signature.parameters or any(parameter.kind is inspect.Parameter.VAR_KEYWORD for parameter in signature.parameters.values())


def _supports_response_shaping_kwarg(connector: Any, name: str) -> bool:
    if _hosted_executor_for(connector) is not None:
        return True
    execute_func = getattr(connector, "execute", None)
    return callable(execute_func) and _accepts_kwarg(execute_func, name)


def _unsupported_response_shaping_kwargs(
    execute_func: Callable[..., Any],
    *,
    select_fields: list[str] | None,
    exclude_fields: list[str] | None,
    skip_truncation: bool,
) -> list[str]:
    unsupported: list[str] = []
    if select_fields is not None and not _accepts_kwarg(execute_func, "select_fields"):
        unsupported.append("select_fields")
    if exclude_fields is not None and not _accepts_kwarg(execute_func, "exclude_fields"):
        unsupported.append("exclude_fields")
    if skip_truncation is not True and not _accepts_kwarg(execute_func, "skip_truncation"):
        unsupported.append("skip_truncation")
    return unsupported


def build_connector_tools(
    connector: Any,
    *,
    framework: FrameworkName | None = None,
    docs_provider: ConnectorDocsProvider | None = None,
    use_progressive_docs: bool = True,
    max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
    internal_retries: int = 0,
    should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
    exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
) -> ConnectorTools:
    """Build inspect/docs/execute tools bound to a single connector.

    Hosted connectors use the live inspect and skill-docs endpoints. Local
    connectors keep the generated YAML-derived rich docs as their fallback.
    """
    hosted_executor = _hosted_executor_for(connector)
    accessor = SkillDocsAccessor(connector, docs_provider=docs_provider)
    active_docs_provider = accessor.provider

    async def inspect_connector() -> dict[str, Any]:
        return await accessor.inspect()

    async def read_skill_docs(section: str | None = None) -> str:
        return await accessor.read(section)

    async def execute(
        entity: str,
        action: str,
        params: dict[str, Any] | None = None,
        *,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True,
    ) -> Any:
        if hosted_executor is not None:
            result = await hosted_executor.execute(
                entity,
                action,
                params=params,
                select_fields=select_fields,
                exclude_fields=exclude_fields,
                skip_truncation=skip_truncation,
            )
            if not result.success:
                raise RuntimeError(f"Execution failed: {result.error}")
            return result.data
        execute_kwargs: dict[str, Any] = {
            "entity": entity,
            "action": action,
            "params": params or {},
        }
        unsupported_kwargs = _unsupported_response_shaping_kwargs(
            connector.execute,
            select_fields=select_fields,
            exclude_fields=exclude_fields,
            skip_truncation=skip_truncation,
        )
        if unsupported_kwargs:
            formatted = ", ".join(unsupported_kwargs)
            raise ValueError(
                f"This local connector does not support response-shaping arguments: {formatted}. "
                "Remove those arguments and narrow the request using supported params such as filters, limits, or cursors."
            )
        if select_fields is not None:
            execute_kwargs["select_fields"] = select_fields
        if exclude_fields is not None:
            execute_kwargs["exclude_fields"] = exclude_fields
        if _accepts_kwarg(connector.execute, "skip_truncation"):
            execute_kwargs["skip_truncation"] = skip_truncation
        return await connector.execute(**execute_kwargs)

    inspect_connector.__doc__ = (
        "Inspect this connector's hosted metadata/readiness and get docs_skill_id. " "Call this before read_skill_docs in the normal hosted flow."
    )
    read_skill_docs.__doc__ = (
        "Read this connector's usage docs. Omit section for the outline and general guidance; " "pass an exact section ID before execute."
    )
    execute.__doc__ = _execute_description(connector, use_progressive_docs=use_progressive_docs, docs_provider=active_docs_provider)
    execute.__signature__ = _execute_tool_signature(connector)  # type: ignore[attr-defined]

    docs_wrap = translate_exceptions(
        framework=framework,
        max_output_chars=None,
        internal_retries=internal_retries,
        should_internal_retry=should_internal_retry,
        exhausted_runtime_failure_message=exhausted_runtime_failure_message,
    )
    execute_wrap = translate_exceptions(
        framework=framework,
        max_output_chars=max_output_chars,
        internal_retries=internal_retries,
        should_internal_retry=should_internal_retry,
        exhausted_runtime_failure_message=exhausted_runtime_failure_message,
    )
    return ConnectorTools(
        inspect_connector=cast(ToolCallable, docs_wrap(inspect_connector)),
        read_skill_docs=cast(ToolCallable, docs_wrap(read_skill_docs)),
        execute=cast(ToolCallable, execute_wrap(execute)),
        use_progressive_docs=use_progressive_docs,
    )


# ---------------------------------------------------------------------------
# agent_tool — framework-agnostic decorator for user-written tool functions
# ---------------------------------------------------------------------------

AgentToolRole = Literal["execute", "inspect_connector", "read_skill_docs"]

_AGENT_TOOL_CANONICAL_PARAMS: dict[AgentToolRole, frozenset[str]] = {
    "execute": frozenset({"entity", "action"}),
    "read_skill_docs": frozenset({"section"}),
    "inspect_connector": frozenset(),
}

_AGENT_TOOL_INSPECT_DESCRIPTION = (
    "Inspect this connector's hosted metadata/readiness and resolve its docs skill id. "
    "Call this before reading the connector docs in the normal hosted flow. "
    "For local/offline connectors this returns a local-mode payload with a warning."
)

_AGENT_TOOL_DOCS_DESCRIPTION = (
    "Read this connector's usage docs. Omit section for the outline and general guidance; "
    "pass an exact section id from the outline for full details before executing. "
    "For local/offline connectors the full generated docs are returned and section is ignored."
)


class Unset:
    """Sentinel type marking 'argument not provided' (distinct from None)."""

    def __repr__(self) -> str:
        return "UNSET"


UNSET = Unset()


@dataclass(frozen=True)
class _AgentToolSignatureInfo:
    """Named (non-self/cls) parameters and whether *args/**kwargs are accepted."""

    param_names: frozenset[str]
    has_var_params: bool


def _agent_tool_signature_info(func: Callable[..., Any]) -> _AgentToolSignatureInfo | None:
    """Read the decorated function's signature; None when it cannot be read."""
    try:
        signature = inspect.signature(func)
    except (TypeError, ValueError):
        return None
    names: set[str] = set()
    has_var_params = False
    for name, parameter in signature.parameters.items():
        if name in ("self", "cls"):
            continue
        if parameter.kind in (inspect.Parameter.VAR_KEYWORD, inspect.Parameter.VAR_POSITIONAL):
            has_var_params = True
            continue
        names.add(name)
    return _AgentToolSignatureInfo(param_names=frozenset(names), has_var_params=has_var_params)


def _infer_agent_tool_role(func: Callable[..., Any], info: _AgentToolSignatureInfo | None) -> AgentToolRole:
    if info is None:
        raise ValueError(
            f"agent_tool could not read the signature of {getattr(func, '__name__', func)!r}; "
            "pass the role explicitly, e.g. agent_tool('execute')."
        )
    names = info.param_names
    matches: list[AgentToolRole] = []
    if _AGENT_TOOL_CANONICAL_PARAMS["execute"] <= names:
        matches.append("execute")
    if "section" in names:
        matches.append("read_skill_docs")
    if not names and not info.has_var_params:
        matches.append("inspect_connector")
    if len(matches) != 1:
        detail = "matches more than one role" if matches else "matches no role"
        raise ValueError(
            f"agent_tool could not infer the tool role from {func.__name__}'s signature ({detail}): "
            "expected (entity, action, ...) for execute, (section, ...) for read_skill_docs, "
            "or no parameters for inspect_connector. Pass the role explicitly, e.g. agent_tool('execute')."
        )
    return matches[0]


def _validate_agent_tool_role(func: Callable[..., Any], role: AgentToolRole, info: _AgentToolSignatureInfo | None) -> None:
    if info is None or info.has_var_params:
        # Explicit role is the escape hatch: trust the caller when the
        # signature cannot be read, and let *args/**kwargs stand in for
        # the canonical parameters.
        return
    missing = _AGENT_TOOL_CANONICAL_PARAMS[role] - info.param_names
    if missing:
        formatted = ", ".join(sorted(missing))
        raise ValueError(f"agent_tool role {role!r} requires parameter(s) {formatted} on {func.__name__}; extra parameters are allowed.")


def _agent_tool_execute_description(model: Any, info: _AgentToolSignatureInfo | None, *, inspect_tool: str | None, docs_tool: str | None) -> str:
    inspect_ref = f"{inspect_tool}()" if inspect_tool else "this connector's inspect tool"
    docs_ref = f"{docs_tool}()" if docs_tool else "this connector's docs tool"
    section_ref = f"{docs_tool}(section=<exact section id>)" if docs_tool else "the docs tool with section=<exact section id>"
    docs_home = docs_tool if docs_tool else "the docs tool"
    supports_field_shaping = info is not None and bool(info.param_names & {"select_fields", "exclude_fields"})
    lines = [
        *_progressive_execute_prefix(inspect_ref, docs_ref, section_ref, docs_home),
        _progressive_size_guidance(supports_field_shaping),
        *_PROGRESSIVE_EXECUTE_DESCRIPTION_SUFFIX,
    ]
    description = "\n".join(lines)
    signatures = _entity_action_signatures_for_model(model)
    if signatures:
        return f"{description}\nValid entity/action signatures:\n{signatures}"
    return description


def build_agent_tool_decorator(
    model: Any,
    *,
    role: AgentToolRole | None = None,
    inspect_tool: str | None = None,
    docs_tool: str | None = None,
    max_output_chars: int | None | Unset = UNSET,
    framework: FrameworkName = "none",
    internal_retries: int = 0,
    should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
    exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Build the `agent_tool` decorator bound to one connector model.

    Backs the generated ``@<Connector>.agent_tool(...)`` classmethod, which
    documents the user-facing contract. Always uses progressive skill docs:
    the execute docstring points the agent at the connector's inspect and
    docs tools instead of embedding the full entity/action reference.
    """
    if callable(role):
        raise TypeError(
            "agent_tool requires parentheses: use @Connector.agent_tool() or @Connector.agent_tool('execute'), not @Connector.agent_tool."
        )
    if role is not None and role not in _AGENT_TOOL_CANONICAL_PARAMS:
        raise ValueError(f"Unknown agent_tool role {role!r}; choose from: execute, inspect_connector, read_skill_docs.")

    def decorate(func: Callable[..., Any]) -> Callable[..., Any]:
        info = _agent_tool_signature_info(func)
        if role is None:
            resolved_role = _infer_agent_tool_role(func, info)
        else:
            _validate_agent_tool_role(func, role, info)
            resolved_role = role

        if resolved_role != "execute" and (inspect_tool is not None or docs_tool is not None):
            raise ValueError(
                f"agent_tool arguments inspect_tool/docs_tool only apply to the execute role, "
                f"but {getattr(func, '__name__', func)!r} resolved to role {resolved_role!r}."
            )

        if resolved_role == "execute":
            description = _agent_tool_execute_description(model, info, inspect_tool=inspect_tool, docs_tool=docs_tool)
            role_default_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS
        elif resolved_role == "read_skill_docs":
            description = _AGENT_TOOL_DOCS_DESCRIPTION
            role_default_output_chars = None
        else:
            description = _AGENT_TOOL_INSPECT_DESCRIPTION
            role_default_output_chars = None

        resolved_output_chars = role_default_output_chars if isinstance(max_output_chars, Unset) else max_output_chars

        original_doc = (func.__doc__ or "").strip()
        full_doc = f"{original_doc}\n{description}" if original_doc else description

        wrapped = translate_exceptions(
            framework=framework,
            max_output_chars=resolved_output_chars,
            internal_retries=internal_retries,
            should_internal_retry=should_internal_retry,
            exhausted_runtime_failure_message=exhausted_runtime_failure_message,
        )(func)
        wrapped.__doc__ = full_doc
        return wrapped

    return decorate
