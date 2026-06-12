"""Framework-ready connector tools."""

from __future__ import annotations

import inspect
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Awaitable, Literal, Protocol, cast

from airbyte_agent_sdk.executor import HostedExecutor
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

_PROGRESSIVE_EXECUTE_DESCRIPTION_PREFIX = [
    "Execute a connector operation.",
    "Before your first execute call, call inspect_connector(), then read_skill_docs(), then "
    "read_skill_docs(section=<exact section id>) for the entity/action you plan to execute.",
    "Do not guess entity, action, or parameter names. Exact names, params, fields, relationships, and examples live in read_skill_docs.",
    "Use entity and action names exactly as documented by the schema and docs.",
]
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
    if _supports_response_shaping_kwarg(connector, "select_fields") or _supports_response_shaping_kwarg(connector, "exclude_fields"):
        size_guidance = "For collection responses, keep outputs small with select_fields or exclude_fields, filters, and small limits."
    else:
        size_guidance = "For collection responses, keep outputs small with filters and small limits."
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
    for entity in entities:
        for action in getattr(entity, "actions", []) or []:
            names.add(_action_value(action))
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
    model = _connector_model_for(connector)
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
    active_docs_provider = docs_provider or hosted_executor
    docs_skill_id: str | None = None

    async def inspect_connector() -> dict[str, Any]:
        nonlocal docs_skill_id
        if active_docs_provider is None:
            docs_skill_id = _LOCAL_DOCS_SKILL_ID
            model = _connector_model_for(connector)
            return {
                "mode": "local",
                "docs_skill_id": docs_skill_id,
                "name": getattr(model, "name", None),
                "warnings": ["Hosted connector inspection is unavailable for local/offline connectors."],
            }
        result = await active_docs_provider.inspect_connector()
        raw_docs_skill_id = result.get("docs_skill_id")
        if not isinstance(raw_docs_skill_id, str) or not raw_docs_skill_id:
            raise ValueError("inspect_connector response did not include docs_skill_id.")
        docs_skill_id = raw_docs_skill_id
        return result

    async def read_skill_docs(section: str | None = None) -> str:
        nonlocal docs_skill_id
        if active_docs_provider is None:
            docs_text = _legacy_execute_description(connector)
            if section is None:
                return docs_text
            return f"Section-specific docs are unavailable for local/offline connectors; full generated docs follow.\n{docs_text}"
        if docs_skill_id is None:
            await inspect_connector()
        if docs_skill_id is None:
            raise ValueError("Connector docs_skill_id could not be resolved.")
        docs = await active_docs_provider.read_skill_docs(id=docs_skill_id, section=section)
        return render_skill_docs(docs)

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
