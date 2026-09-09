"""
Greenhouse connector.
"""
# ruff: noqa: E501

from __future__ import annotations

import logging
from typing import Any, Callable, Mapping, TypeVar, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import GreenhouseConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.tools import UNSET, AgentToolRole, SkillDocsAccessor, Unset, build_agent_tool_decorator
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    ApplicationsListParams,
    AttachmentsDownloadParams,
    AttachmentsListParams,
    CandidatesListParams,
    DepartmentsListParams,
    InterviewsListParams,
    JobPostsListParams,
    JobsListParams,
    OffersListParams,
    OfficesListParams,
    SourcesListParams,
    UsersListParams,
    AirbyteSearchParams,
    ApplicationsSearchFilter,
    ApplicationsSearchQuery,
    CandidatesSearchFilter,
    CandidatesSearchQuery,
    DepartmentsSearchFilter,
    DepartmentsSearchQuery,
    JobPostsSearchFilter,
    JobPostsSearchQuery,
    JobsSearchFilter,
    JobsSearchQuery,
    OffersSearchFilter,
    OffersSearchQuery,
    OfficesSearchFilter,
    OfficesSearchQuery,
    SourcesSearchFilter,
    SourcesSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
)
from .models import GreenhouseAuthConfig

# Import response models and envelope models at runtime
from .models import (
    GreenhouseCheckResult,
    GreenhouseExecuteResult,
    GreenhouseExecuteResultWithMeta,
    ApplicationsListResult,
    CandidatesListResult,
    DepartmentsListResult,
    InterviewsListResult,
    JobPostsListResult,
    JobsListResult,
    OffersListResult,
    OfficesListResult,
    SourcesListResult,
    UsersListResult,
    AttachmentsListResult,
    Application,
    Attachment,
    Candidate,
    Department,
    Interview,
    Job,
    JobPost,
    Offer,
    Office,
    Source,
    User,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    ApplicationsSearchData,
    ApplicationsSearchResult,
    CandidatesSearchData,
    CandidatesSearchResult,
    DepartmentsSearchData,
    DepartmentsSearchResult,
    JobPostsSearchData,
    JobPostsSearchResult,
    JobsSearchData,
    JobsSearchResult,
    OffersSearchData,
    OffersSearchResult,
    OfficesSearchData,
    OfficesSearchResult,
    SourcesSearchData,
    SourcesSearchResult,
    UsersSearchData,
    UsersSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class GreenhouseConnector:
    """
    Type-safe Greenhouse API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "greenhouse"
    connector_version = "0.2.0"
    sdk_version = "0.1.340"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("applications", "list"): True,
        ("candidates", "list"): True,
        ("departments", "list"): True,
        ("interviews", "list"): True,
        ("job_posts", "list"): True,
        ("jobs", "list"): True,
        ("offers", "list"): True,
        ("offices", "list"): True,
        ("sources", "list"): True,
        ("users", "list"): True,
        ("attachments", "list"): True,
        ("attachments", "download"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('applications', 'list'): {'cursor': 'cursor', 'per_page': 'per_page', 'ids': 'ids', 'updated_at': 'updated_at'},
        ('candidates', 'list'): {'cursor': 'cursor', 'per_page': 'per_page', 'ids': 'ids', 'updated_at': 'updated_at'},
        ('departments', 'list'): {'cursor': 'cursor', 'per_page': 'per_page', 'ids': 'ids'},
        ('interviews', 'list'): {'cursor': 'cursor', 'per_page': 'per_page', 'ids': 'ids', 'updated_at': 'updated_at'},
        ('job_posts', 'list'): {'cursor': 'cursor', 'per_page': 'per_page', 'ids': 'ids', 'updated_at': 'updated_at', 'active': 'active'},
        ('jobs', 'list'): {'cursor': 'cursor', 'per_page': 'per_page', 'ids': 'ids', 'updated_at': 'updated_at'},
        ('offers', 'list'): {'cursor': 'cursor', 'per_page': 'per_page', 'ids': 'ids', 'updated_at': 'updated_at'},
        ('offices', 'list'): {'cursor': 'cursor', 'per_page': 'per_page', 'ids': 'ids'},
        ('sources', 'list'): {'cursor': 'cursor', 'per_page': 'per_page', 'ids': 'ids'},
        ('users', 'list'): {'cursor': 'cursor', 'per_page': 'per_page', 'ids': 'ids', 'updated_at': 'updated_at', 'show_service_accounts': 'show_service_accounts'},
        ('attachments', 'list'): {'cursor': 'cursor', 'per_page': 'per_page', 'ids': 'ids', 'updated_at': 'updated_at', 'application_ids': 'application_ids', 'candidate_ids': 'candidate_ids', 'type': 'type'},
        ('attachments', 'download'): {'ids': 'ids', 'range_header': 'range_header'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (GreenhouseAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: GreenhouseAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new greenhouse connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., GreenhouseAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = GreenhouseConnector(auth_config=GreenhouseAuthConfig(client_id="...", client_secret="...", refresh_token="...", access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = GreenhouseConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = GreenhouseConnector(
                auth_config=AirbyteAuthConfig(
                    workspace_name="user-123",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789"
                )
            )
        """
        # Accept AirbyteAuthConfig from any vendored SDK version
        if (
            auth_config is not None
            and not isinstance(auth_config, AirbyteAuthConfig)
            and type(auth_config).__name__ == AirbyteAuthConfig.__name__
        ):
            auth_config = AirbyteAuthConfig(**auth_config.model_dump())

        # Validate auth_config type
        if auth_config is not None and not isinstance(auth_config, self._ACCEPTED_AUTH_TYPES):
            raise TypeError(
                f"Unsupported auth_config type: {type(auth_config).__name__}. "
                f"Expected one of: {', '.join(t.__name__ for t in self._ACCEPTED_AUTH_TYPES)}"
            )

        # Hosted mode: auth_config is AirbyteAuthConfig
        is_hosted = isinstance(auth_config, AirbyteAuthConfig)

        if is_hosted:
            from airbyte_agent_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                workspace_name=auth_config.workspace_name or "default",
                organization_id=auth_config.organization_id,
                connector_definition_id=str(GreenhouseConnectorModel.id),
                model=GreenhouseConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or GreenhouseAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=GreenhouseConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.applications = ApplicationsQuery(self)
        self.candidates = CandidatesQuery(self)
        self.departments = DepartmentsQuery(self)
        self.interviews = InterviewsQuery(self)
        self.job_posts = JobPostsQuery(self)
        self.jobs = JobsQuery(self)
        self.offers = OffersQuery(self)
        self.offices = OfficesQuery(self)
        self.sources = SourcesQuery(self)
        self.users = UsersQuery(self)
        self.attachments = AttachmentsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["applications"],
        action: Literal["list"],
        params: "ApplicationsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ApplicationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["candidates"],
        action: Literal["list"],
        params: "CandidatesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CandidatesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["departments"],
        action: Literal["list"],
        params: "DepartmentsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DepartmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["interviews"],
        action: Literal["list"],
        params: "InterviewsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "InterviewsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["job_posts"],
        action: Literal["list"],
        params: "JobPostsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "JobPostsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["jobs"],
        action: Literal["list"],
        params: "JobsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "JobsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["offers"],
        action: Literal["list"],
        params: "OffersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "OffersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["offices"],
        action: Literal["list"],
        params: "OfficesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "OfficesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sources"],
        action: Literal["list"],
        params: "SourcesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SourcesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["list"],
        params: "UsersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "UsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["list"],
        params: "AttachmentsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AttachmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["download"],
        params: "AttachmentsDownloadParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AsyncIterator[bytes]": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "download", "context_store_search", "context_store_sql_query"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> GreenhouseExecuteResult[Any] | GreenhouseExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "download", "context_store_search", "context_store_sql_query"],
        params: Mapping[str, Any] | None = None,
        *,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True
    ) -> Any:
        """
        Execute an entity operation with full type safety.

        This is the recommended interface for blessed connectors as it:
        - Uses the same signature as non-blessed connectors
        - Provides full IDE autocomplete for entity/action/params
        - Makes migration from generic to blessed connectors seamless

        Args:
            entity: Entity name (e.g., "customers")
            action: Operation action (e.g., "create", "get", "list")
            params: Operation parameters (typed based on entity+action)
            select_fields: Optional allowlist of dot-notation fields to include
            exclude_fields: Optional blocklist of dot-notation fields to remove
            skip_truncation: Disable long-text truncation for collection actions

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from airbyte_agent_sdk.executor import ExecutionConfig

        # Remap parameter names from snake_case (TypedDict keys) to API parameter names
        resolved_params = dict(params) if params is not None else None
        if resolved_params:
            param_map = self._PARAM_MAP.get((entity, action), {})
            if param_map:
                resolved_params = {param_map.get(k, k): v for k, v in resolved_params.items()}

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=resolved_params,
            select_fields=select_fields,
            exclude_fields=exclude_fields,
            skip_truncation=skip_truncation
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._ENVELOPE_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return GreenhouseExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GreenhouseExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> GreenhouseCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            GreenhouseCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return GreenhouseCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return GreenhouseCheckResult(
                status="unhealthy",
                error=result.error or "Unknown error during health check",
            )

    # ===== INTROSPECTION METHODS =====

    @classmethod
    def tool_utils(
        cls,
        func: _F | None = None,
        *,
        update_docstring: bool = True,
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
        framework: FrameworkName | None = None,
        internal_retries: int = 0,
        should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
        exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
    ) -> _F | Callable[[_F], _F]:
        """
        Add connector-specific documentation and runtime safeguards to one tool.

        For new agents, prefer `build_connector_tools`. It returns progressive
        `inspect_connector`, `read_skill_docs`, and `execute` tools so the agent
        can load only the connector guidance it needs:

        ```python
        from airbyte_agent_sdk import build_connector_tools
        from pydantic_ai import Agent

        tools = build_connector_tools(connector, framework="pydantic_ai")
        agent = Agent("openai:gpt-4o", tools=tools.as_list())
        ```

        ### Legacy: one generated-description tool

        Existing integrations can keep using `tool_utils` for one broad
        `execute` tool with the connector's full generated catalog in its
        description:

        ```python
        from fastmcp import FastMCP

        connector = GreenhouseConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @GreenhouseConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @GreenhouseConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @GreenhouseConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        This decorator composes `translate_exceptions` for runtime wrapping,
        output-size checks, framework signal translation, and optional internal
        retries, then adds connector-specific docstring augmentation.

        Args:
            update_docstring: When True, append connector capabilities to `__doc__`.
            max_output_chars: Max serialized output size before raising. Use `None` to disable.
            framework: One of `"pydantic_ai" | "langchain" | "openai_agents" | "mcp"`.
                Defaults to `None`, which auto-detects each framework's canonical
                import in order. Explicit always wins.
            internal_retries: How many transient runtime failures (429/5xx, network,
                timeout) to retry silently before surfacing. Default 0. Forwarded to
                `airbyte_agent_sdk.translation.translate_exceptions`.
            should_internal_retry: Optional predicate `(error, args, kwargs) -> bool`
                further restricting which retryable errors are safe for this specific
                tool. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
            exhausted_runtime_failure_message: Optional callback
                `(error, args, kwargs) -> str | None`. Invoked after internal retries
                are exhausted or were skipped because `should_internal_retry` returned
                `False`. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    GreenhouseConnectorModel,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            wrapped = translate_exceptions(
                inner,
                framework=framework,
                max_output_chars=max_output_chars,
                internal_retries=internal_retries,
                should_internal_retry=should_internal_retry,
                exhausted_runtime_failure_message=exhausted_runtime_failure_message,
            )

            if update_docstring:
                wrapped.__doc__ = full_doc
            return wrapped  # type: ignore[return-value]

        if func is not None:
            return decorate(func)
        return decorate

    @classmethod
    def agent_tool(
        cls,
        role: AgentToolRole | None = None,
        *,
        inspect_tool: str | None = None,
        docs_tool: str | None = None,
        max_output_chars: int | None | Unset = UNSET,
        framework: FrameworkName = "none",
        internal_retries: int = 0,
        should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
        exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
    ) -> Callable[[_F], _F]:
        """
        Framework-agnostic decorator for user-written connector tool functions.

        The progressive-docs sibling of tool_utils: instead of baking the full
        entity/action reference into the docstring, it instructs the agent to
        call this connector's inspect and docs tools before executing. Tool
        failures raise :class:`airbyte_agent_sdk.AirbyteToolError` by default
        (``framework="none"``, no auto-detection) — pass ``framework=...`` to
        translate to a supported framework's signal instead.

        Decorate three functions per connector — execute, inspect and docs.
        The role is inferred from each function's signature (extra parameters
        are allowed); a signature matching more than one role, a generic
        ``(*args, **kwargs)`` wrapper, or a callable whose signature cannot
        be read must pass the role explicitly:

        - ``(entity, action, ...)`` -> ``"execute"``
        - ``(section, ...)``        -> ``"read_skill_docs"``
        - ``()``                    -> ``"inspect_connector"``

        Usage:
            connector = GreenhouseConnector(...)

            @GreenhouseConnector.agent_tool()
            async def execute(entity: str, action: str, params: dict | None = None):
                return await connector.execute(entity=entity, action=action, params=params or {})

            @GreenhouseConnector.agent_tool()
            async def inspect_connector():
                return await connector.inspect_connector()

            @GreenhouseConnector.agent_tool()
            async def read_skill_docs(section: str | None = None):
                return await connector.read_skill_docs(section)

        Args:
            role: ``"execute" | "inspect_connector" | "read_skill_docs"``.
                None (default) infers the role from the decorated function's
                signature; an explicit role validates the canonical
                parameters are present (functions accepting ``**kwargs``, or
                callables whose signature cannot be read, pass validation).
            inspect_tool: Exact registered name of the sibling inspect tool,
                woven into the execute docstring for tighter steering.
                Defaults to generic phrasing.
            docs_tool: Exact registered name of the sibling docs tool (see
                inspect_tool).
            max_output_chars: Max serialized output size before failing.
                Defaults per role: execute -> DEFAULT_MAX_OUTPUT_CHARS, docs
                tools -> None.
            framework: Translation target for tool failures. Defaults to
                ``"none"`` (raise AirbyteToolError); never auto-detects.
            internal_retries: How many transient runtime failures (429/5xx,
                network, timeout) to retry silently before surfacing.
                Forwarded to
                :func:`airbyte_agent_sdk.translation.translate_exceptions`.
            should_internal_retry: Optional predicate ``(error, args, kwargs)
                -> bool`` further restricting which retryable errors are safe
                for this specific tool. Forwarded to
                :func:`airbyte_agent_sdk.translation.translate_exceptions`.
            exhausted_runtime_failure_message: Optional callback ``(error,
                args, kwargs) -> str | None`` invoked after internal retries
                are exhausted or skipped. Forwarded to
                :func:`airbyte_agent_sdk.translation.translate_exceptions`.
        """
        return build_agent_tool_decorator(  # type: ignore[return-value]
            GreenhouseConnectorModel,
            role=role,
            inspect_tool=inspect_tool,
            docs_tool=docs_tool,
            max_output_chars=max_output_chars,
            framework=framework,
            internal_retries=internal_retries,
            should_internal_retry=should_internal_retry,
            exhausted_runtime_failure_message=exhausted_runtime_failure_message,
        )

    def _skill_docs(self) -> SkillDocsAccessor:
        accessor: SkillDocsAccessor | None = getattr(self, "_skill_docs_accessor", None)
        if accessor is None:
            accessor = SkillDocsAccessor(self)
            self._skill_docs_accessor = accessor
        return accessor

    async def inspect_connector(self) -> dict[str, Any]:
        """
        Inspect this connector's hosted metadata/readiness and resolve its docs skill id.

        Call this before read_skill_docs in the normal hosted flow. For
        local/offline connectors this returns a local-mode payload with a
        warning instead of a hosted inspection.

        Example:
            info = await connector.inspect_connector()
            print(info["docs_skill_id"])
        """
        return await self._skill_docs().inspect()

    async def read_skill_docs(self, section: str | None = None) -> str:
        """
        Read this connector's usage docs, rendered to text.

        Omit section for the outline and general guidance; pass an exact
        section id from the outline for full details. For local/offline
        connectors the full generated docs are returned and section is
        ignored.

        Example:
            outline = await connector.read_skill_docs()
            details = await connector.read_skill_docs(section="entity:contacts")
        """
        return await self._skill_docs().read(section)

    def list_entities(self) -> list[dict[str, Any]]:
        """
        Get structured data about available entities, actions, and parameters.

        Returns a list of entity descriptions with:
        - entity_name: Name of the entity (e.g., "contacts", "deals")
        - description: Entity description from the first endpoint
        - available_actions: List of actions (e.g., ["list", "get", "create"])
        - parameters: Dict mapping action -> list of parameter dicts

        Example:
            entities = connector.list_entities()
            for entity in entities:
                print(f"{entity['entity_name']}: {entity['available_actions']}")
        """
        return describe_entities(GreenhouseConnectorModel)

    def entity_schema(self, entity: str) -> dict[str, Any] | None:
        """
        Get the JSON schema for an entity.

        Args:
            entity: Entity name (e.g., "contacts", "companies")

        Returns:
            JSON schema dict describing the entity structure, or None if not found.

        Example:
            schema = connector.entity_schema("contacts")
            if schema:
                print(f"Contact properties: {list(schema.get('properties', {}).keys())}")
        """
        entity_def = next(
            (e for e in GreenhouseConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in GreenhouseConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== RESOURCE MANAGEMENT =====

    async def close(self):
        """Close the connector and release resources."""
        await self._executor.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()



class ApplicationsQuery:
    """
    Query class for Applications entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        per_page: int | None = None,
        ids: list[int] | None = None,
        updated_at: str | None = None,
        **kwargs
    ) -> ApplicationsListResult:
        """
        Returns a cursor-paginated list of applications.

        Args:
            cursor: Cursor from the previous response Link header. Do not combine with any other parameter.
            per_page: Number of records to return on the first page.
            ids: Return only records with these IDs (maximum 50).
            updated_at: Filter by updated timestamp using the Harvest v3 pipe expression, such as gte|2026-01-01T00:00:00Z.
            **kwargs: Additional parameters

        Returns:
            ApplicationsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "per_page": per_page,
            "ids": ids,
            "updated_at": updated_at,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("applications", "list", params)
        # Cast generic envelope to concrete typed result
        return ApplicationsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: ApplicationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ApplicationsSearchResult:
        """
        Search applications records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ApplicationsSearchFilter):
        - agency_note_id: Id of the note created when the candidate was submitted by an agency, or `null` if the application did not come through an agency.
        - answers: Free-text answers the candidate provided on the job post application form. Each entry pairs the question text with the candidate's answer.
        - candidate_id: Id of the candidate (person) this application belongs to.
        - coordinator_id: Id of the user assigned as coordinator on the application's job, or `null` when unassigned.
        - created_at: Created at from the Greenhouse v3 applications record.
        - custom_fields: Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.
        - id: Id from the Greenhouse v3 applications record.
        - job_id: Id of the job this application is on. `null` for jobless prospect applications.
        - job_interview_stage_id: Id of the job interview stage definition (see `GET /v3/job_interview_stages`) the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state.
        - job_post_id: Id of the job post the candidate applied through, or `null` if the application was created internally rather than from a posted role.
        - last_activity_at: Timestamp of the most recent activity on this application (notes, emails, stage changes, etc.), in ISO 8601.
        - location_address: Free-form location string captured on the application (typically from the job post's location question).
        - needs_decision: `true` when the application is waiting on a hiring-team decision (scorecard completion, advance/reject, etc.) in its current stage.
        - prospect: `true` for prospect applications (sourced candidates not yet attached to a single job), `false` for candidate applications on a specific job.
        - prospective_job_ids: For prospect applications, the ids of jobs the prospect is being considered for. Empty for non-prospect applications and for jobless prospects.
        - recruiter_id: Id of the user assigned as recruiter on the application's job, or `null` when unassigned.
        - referrer_id: Id of the referrer who credited this application, or `null` if there was no referral. References a referrer, not a Greenhouse user.
        - rejected_at: Timestamp the application was rejected, in ISO 8601. `null` for applications that have not been rejected.
        - rejection_reason_id: Id of the rejection reason selected for the application. References a `/v3/rejection_reasons` row scoped to the organization. `null` when the application was rejected without a reason, or has not been rejected.
        - source_id: Id of the source the application is attributed to (e.g. a job board, an event, an employee referral source). `null` if no source is set.
        - stage_id: Id of the interview stage the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state.
        - stage_name: Display name of the candidate's current interview stage on this application.
        - status: Lifecycle status of the application. `in_process` for active candidates, `rejected` for rejected applications, `hired` once an offer is closed and the hire endpoint has fired, and `converted` for prospect applications that have been promoted to a candidate application via `convert_to_candidate`.
        - updated_at: Updated at from the Greenhouse v3 applications record.

        Args:
            query: Filter and sort conditions. Supports operators such as eq, neq, gt, gte, lt, lte,
                   in, startswith, endswith, contains, array_contains, fuzzy, keyword, not, and, or.
                   Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ApplicationsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("applications", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ApplicationsSearchResult(
            data=[
                ApplicationsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

    async def context_store_sql_query(
        self,
        sql: str,
        limit: int | None = None,
    ) -> AirbyteSearchResult[dict[str, Any]]:
        """
        Run a SQL query against applications records in the Airbyte Context Store.

        Only available in hosted execution mode.

        Args:
            sql: SQL query to execute.
            limit: Maximum results to return.

        Returns:
            AirbyteSearchResult containing the projected rows and query metadata.

        Raises:
            NotImplementedError: If called in local execution mode.
        """
        params: dict[str, Any] = {"sql": sql}
        if limit is not None:
            params["limit"] = limit

        result = await self._connector.execute("applications", "context_store_sql_query", params)
        meta_data = result.get("meta")
        return AirbyteSearchResult[dict[str, Any]](
            data=result.get("data", []),
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CandidatesQuery:
    """
    Query class for Candidates entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        per_page: int | None = None,
        ids: list[int] | None = None,
        updated_at: str | None = None,
        **kwargs
    ) -> CandidatesListResult:
        """
        Returns a cursor-paginated list of candidates.

        Args:
            cursor: Cursor from the previous response Link header. Do not combine with any other parameter.
            per_page: Number of records to return on the first page.
            ids: Return only records with these IDs (maximum 50).
            updated_at: Filter by updated timestamp using the Harvest v3 pipe expression, such as gte|2026-01-01T00:00:00Z.
            **kwargs: Additional parameters

        Returns:
            CandidatesListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "per_page": per_page,
            "ids": ids,
            "updated_at": updated_at,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("candidates", "list", params)
        # Cast generic envelope to concrete typed result
        return CandidatesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: CandidatesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CandidatesSearchResult:
        """
        Search candidates records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CandidatesSearchFilter):
        - addresses: Postal addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `home`, `work`, or `other`.
        - can_email: Whether this candidate has consented to receive email communication from your organization.
        - company: Candidate's current company, as entered on their profile.
        - created_at: Created at from the Greenhouse v3 candidates record.
        - custom_fields: Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.
        - email_addresses: Email addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `work`, or `other`.
        - first_name: First name from the Greenhouse v3 candidates record.
        - id: Id from the Greenhouse v3 candidates record.
        - last_activity_at: Timestamp of the most recent activity on any of the candidate's applications (notes, emails, stage changes, etc.), in ISO 8601.
        - last_name: Last name from the Greenhouse v3 candidates record.
        - linked_user_ids: Ids of Greenhouse users linked to this candidate (employees represented by both a user record and a candidate record).
        - phone_numbers: Phone numbers on the candidate's profile. Each entry pairs the `value` with a `type` such as `mobile`, `home`, `work`, `skype`, or `other`.
        - preferred_name: Preferred or chosen name the candidate goes by, when different from their legal first name.
        - private: If true, the candidate is restricted to users with `View Private Candidates` access. Defaults to `false`.
        - social_media_addresses: Social media handles or URLs on the candidate's profile. Social entries are untyped — only the `value` is returned.
        - tags: Candidate tag names applied to this candidate within your organization.
        - time_zone: Candidate's time zone as a Rails-style identifier (for example `Eastern Time (US & Canada)`).
        - title: Candidate's current job title, as entered on their profile.
        - updated_at: Updated at from the Greenhouse v3 candidates record.
        - website_addresses: Personal websites or portfolio URLs on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `company`, `portfolio`, `blog`, or `other`.

        Args:
            query: Filter and sort conditions. Supports operators such as eq, neq, gt, gte, lt, lte,
                   in, startswith, endswith, contains, array_contains, fuzzy, keyword, not, and, or.
                   Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CandidatesSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("candidates", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CandidatesSearchResult(
            data=[
                CandidatesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

    async def context_store_sql_query(
        self,
        sql: str,
        limit: int | None = None,
    ) -> AirbyteSearchResult[dict[str, Any]]:
        """
        Run a SQL query against candidates records in the Airbyte Context Store.

        Only available in hosted execution mode.

        Args:
            sql: SQL query to execute.
            limit: Maximum results to return.

        Returns:
            AirbyteSearchResult containing the projected rows and query metadata.

        Raises:
            NotImplementedError: If called in local execution mode.
        """
        params: dict[str, Any] = {"sql": sql}
        if limit is not None:
            params["limit"] = limit

        result = await self._connector.execute("candidates", "context_store_sql_query", params)
        meta_data = result.get("meta")
        return AirbyteSearchResult[dict[str, Any]](
            data=result.get("data", []),
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class DepartmentsQuery:
    """
    Query class for Departments entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        per_page: int | None = None,
        ids: list[int] | None = None,
        **kwargs
    ) -> DepartmentsListResult:
        """
        Returns a cursor-paginated list of departments.

        Args:
            cursor: Cursor from the previous response Link header. Do not combine with any other parameter.
            per_page: Number of records to return on the first page.
            ids: Return only records with these IDs (maximum 50).
            **kwargs: Additional parameters

        Returns:
            DepartmentsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "per_page": per_page,
            "ids": ids,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("departments", "list", params)
        # Cast generic envelope to concrete typed result
        return DepartmentsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: DepartmentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DepartmentsSearchResult:
        """
        Search departments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DepartmentsSearchFilter):
        - created_at: Created at from the Greenhouse v3 departments record.
        - external_id: Partner-supplied identifier for the department, typically the matching id from an HRIS or other external system. Free-form string and `null` when no external id has been set.
        - id: Id from the Greenhouse v3 departments record.
        - name: Display name of the department (e.g. `Engineering`, `Marketing`).
        - parent_id: Id of the parent department in the organization's department tree. `null` for top-level departments. References another `/v3/departments` row.
        - updated_at: Updated at from the Greenhouse v3 departments record.

        Args:
            query: Filter and sort conditions. Supports operators such as eq, neq, gt, gte, lt, lte,
                   in, startswith, endswith, contains, array_contains, fuzzy, keyword, not, and, or.
                   Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DepartmentsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("departments", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DepartmentsSearchResult(
            data=[
                DepartmentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

    async def context_store_sql_query(
        self,
        sql: str,
        limit: int | None = None,
    ) -> AirbyteSearchResult[dict[str, Any]]:
        """
        Run a SQL query against departments records in the Airbyte Context Store.

        Only available in hosted execution mode.

        Args:
            sql: SQL query to execute.
            limit: Maximum results to return.

        Returns:
            AirbyteSearchResult containing the projected rows and query metadata.

        Raises:
            NotImplementedError: If called in local execution mode.
        """
        params: dict[str, Any] = {"sql": sql}
        if limit is not None:
            params["limit"] = limit

        result = await self._connector.execute("departments", "context_store_sql_query", params)
        meta_data = result.get("meta")
        return AirbyteSearchResult[dict[str, Any]](
            data=result.get("data", []),
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class InterviewsQuery:
    """
    Query class for Interviews entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        per_page: int | None = None,
        ids: list[int] | None = None,
        updated_at: str | None = None,
        **kwargs
    ) -> InterviewsListResult:
        """
        Returns a cursor-paginated list of interviews.

        Args:
            cursor: Cursor from the previous response Link header. Do not combine with any other parameter.
            per_page: Number of records to return on the first page.
            ids: Return only records with these IDs (maximum 50).
            updated_at: Filter by updated timestamp using the Harvest v3 pipe expression, such as gte|2026-01-01T00:00:00Z.
            **kwargs: Additional parameters

        Returns:
            InterviewsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "per_page": per_page,
            "ids": ids,
            "updated_at": updated_at,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("interviews", "list", params)
        # Cast generic envelope to concrete typed result
        return InterviewsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



class JobPostsQuery:
    """
    Query class for JobPosts entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        per_page: int | None = None,
        ids: list[int] | None = None,
        updated_at: str | None = None,
        active: bool | None = None,
        **kwargs
    ) -> JobPostsListResult:
        """
        Returns a cursor-paginated list of job posts.

        Args:
            cursor: Cursor from the previous response Link header. Do not combine with any other parameter.
            per_page: Number of records to return on the first page.
            ids: Return only records with these IDs (maximum 50).
            updated_at: Filter by updated timestamp using the Harvest v3 pipe expression, such as gte|2026-01-01T00:00:00Z.
            active: Filter by active status.
            **kwargs: Additional parameters

        Returns:
            JobPostsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "per_page": per_page,
            "ids": ids,
            "updated_at": updated_at,
            "active": active,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("job_posts", "list", params)
        # Cast generic envelope to concrete typed result
        return JobPostsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: JobPostsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> JobPostsSearchResult:
        """
        Search job_posts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (JobPostsSearchFilter):
        - active: If `true`, the post has not been deleted. Deleted posts are excluded by default; pass `active=false` on the list endpoint to retrieve them.
        - content: HTML body of the post shown to candidates on the job board. For internal posts this returns the `internal_content` instead. Sanitized server-side — only a limited element/attribute allowlist (including `iframe`, `video`, `source`) survives. `null` while the post is still being scaffolded.
        - created_at: Created at from the Greenhouse v3 job posts record.
        - demographic_question_set_id: Id of the demographic question set surfaced to candidates on this post for diversity, equity, and inclusion (DE&I) reporting. `null` when the post does not collect demographic data.
        - featured: If `true`, the post is currently featured on the organization's internal job board and surfaces in the weekly internal-jobs email. Only internal posts can be featured, and at most three can be featured at a time.
        - first_published_at: Timestamp the post first transitioned to `live`, in ISO 8601. `null` for posts that have never been published.
        - id: Id from the Greenhouse v3 job posts record.
        - internal: If `true`, the post lives on an internal job board and is visible only to existing employees signed in to the internal board. If `false`, the post is external and lives on a public-facing `job_board`. Set by the board the post is associated with at create time.
        - internal_content: HTML body shown on the internal job board when the post is also configured as internal. `null` for external-only posts. Same sanitization rules as `content`.
        - job_board_id: Id of the `job_board` this post is published to. Resolves to either an external (careers site, syndicated board) or internal job board depending on `internal`. Each post belongs to exactly one board at a time.
        - job_id: Id of the parent job (requisition) this post belongs to. A single job can have multiple posts; the job is the source of truth for the hiring team, openings, and interview plan.
        - language: ISO 639-1 locale of the post, used to render the candidate-facing application form in the matching language (e.g. `en`, `fr`, `ja`). `null` when no locale has been chosen.
        - live: If `true`, the post is published (`job_application_status` is `live`) and its job board is also live. A post on an unpublished board is **not** `live` — its `public_url` returns a 404 until the board is enabled.
        - public_url: Canonical public URL of the post on its job board, including the `gh_jid` tracking parameter. `null` when the post has no associated job board or the board has no public URL configured.
        - questions: Application form questions presented to candidates on this post, including default questions (resume, cover letter, basic info) and any custom questions configured by the hiring team. Ordered as they appear on the form.
        - title: Public-facing title shown to candidates on the job board (e.g. `Senior Backend Engineer, Remote`). Distinct from the internal `job.name` — a single job can have several posts with different titles, one per board, language, or geography.
        - updated_at: Updated at from the Greenhouse v3 job posts record.

        Args:
            query: Filter and sort conditions. Supports operators such as eq, neq, gt, gte, lt, lte,
                   in, startswith, endswith, contains, array_contains, fuzzy, keyword, not, and, or.
                   Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            JobPostsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("job_posts", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return JobPostsSearchResult(
            data=[
                JobPostsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

    async def context_store_sql_query(
        self,
        sql: str,
        limit: int | None = None,
    ) -> AirbyteSearchResult[dict[str, Any]]:
        """
        Run a SQL query against job_posts records in the Airbyte Context Store.

        Only available in hosted execution mode.

        Args:
            sql: SQL query to execute.
            limit: Maximum results to return.

        Returns:
            AirbyteSearchResult containing the projected rows and query metadata.

        Raises:
            NotImplementedError: If called in local execution mode.
        """
        params: dict[str, Any] = {"sql": sql}
        if limit is not None:
            params["limit"] = limit

        result = await self._connector.execute("job_posts", "context_store_sql_query", params)
        meta_data = result.get("meta")
        return AirbyteSearchResult[dict[str, Any]](
            data=result.get("data", []),
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class JobsQuery:
    """
    Query class for Jobs entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        per_page: int | None = None,
        ids: list[int] | None = None,
        updated_at: str | None = None,
        **kwargs
    ) -> JobsListResult:
        """
        Returns a cursor-paginated list of jobs.

        Args:
            cursor: Cursor from the previous response Link header. Do not combine with any other parameter.
            per_page: Number of records to return on the first page.
            ids: Return only records with these IDs (maximum 50).
            updated_at: Filter by updated timestamp using the Harvest v3 pipe expression, such as gte|2026-01-01T00:00:00Z.
            **kwargs: Additional parameters

        Returns:
            JobsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "per_page": per_page,
            "ids": ids,
            "updated_at": updated_at,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("jobs", "list", params)
        # Cast generic envelope to concrete typed result
        return JobsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: JobsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> JobsSearchResult:
        """
        Search jobs records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (JobsSearchFilter):
        - closed_at: Timestamp the job most recently transitioned to `closed`, in ISO 8601. `null` for jobs that are still `open` or `draft`.
        - confidential: If `true`, the job is restricted to users explicitly granted access on the Hiring Team. The legacy Confidential Jobs feature has been sunset — this flag cannot be set on new jobs and is preserved for jobs that already had it enabled.
        - copied_from_id: Id of the job (typically a template) this job was copied from on creation. `null` when the job was not created from another job.
        - created_at: Created at from the Greenhouse v3 jobs record.
        - custom_fields: Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.
        - department_id: Id of the department this job is assigned to. `null` when no department is set.
        - id: Id from the Greenhouse v3 jobs record.
        - is_template: If `true`, this job is a template used as the source for new jobs rather than a real requisition. Templates do not accept applications; reference them via `template_job_id` on `POST /v3/jobs`.
        - name: Internal job title shown to the hiring team in Greenhouse (e.g. `Senior Backend Engineer`). Distinct from the external-facing title on each `job_post`.
        - notes: Internal HTML notes about the job, surfaced to the hiring team in the Greenhouse UI. Not exposed on public job posts.
        - office_ids: Ids of the offices this job is assigned to. A job can span multiple offices; empty array or `null` when no offices are set.
        - opened_at: Timestamp the job first transitioned to `open`, in ISO 8601. `null` while the job is still in `draft`.
        - requisition_id: Partner-supplied external identifier for the requisition (e.g. an HRIS or ATS code). Free-form string, not unique across the organization, and `null` when no external id has been set.
        - status: Lifecycle status of the job. `draft` while it is being scaffolded, `open` once it has at least one open opening, and `closed` after every opening is closed. A job moves to `closed` automatically when its last open opening is closed via `PATCH /v3/openings/{id}`.
        - updated_at: Updated at from the Greenhouse v3 jobs record.

        Args:
            query: Filter and sort conditions. Supports operators such as eq, neq, gt, gte, lt, lte,
                   in, startswith, endswith, contains, array_contains, fuzzy, keyword, not, and, or.
                   Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            JobsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("jobs", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return JobsSearchResult(
            data=[
                JobsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

    async def context_store_sql_query(
        self,
        sql: str,
        limit: int | None = None,
    ) -> AirbyteSearchResult[dict[str, Any]]:
        """
        Run a SQL query against jobs records in the Airbyte Context Store.

        Only available in hosted execution mode.

        Args:
            sql: SQL query to execute.
            limit: Maximum results to return.

        Returns:
            AirbyteSearchResult containing the projected rows and query metadata.

        Raises:
            NotImplementedError: If called in local execution mode.
        """
        params: dict[str, Any] = {"sql": sql}
        if limit is not None:
            params["limit"] = limit

        result = await self._connector.execute("jobs", "context_store_sql_query", params)
        meta_data = result.get("meta")
        return AirbyteSearchResult[dict[str, Any]](
            data=result.get("data", []),
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class OffersQuery:
    """
    Query class for Offers entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        per_page: int | None = None,
        ids: list[int] | None = None,
        updated_at: str | None = None,
        **kwargs
    ) -> OffersListResult:
        """
        Returns a cursor-paginated list of offers.

        Args:
            cursor: Cursor from the previous response Link header. Do not combine with any other parameter.
            per_page: Number of records to return on the first page.
            ids: Return only records with these IDs (maximum 50).
            updated_at: Filter by updated timestamp using the Harvest v3 pipe expression, such as gte|2026-01-01T00:00:00Z.
            **kwargs: Additional parameters

        Returns:
            OffersListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "per_page": per_page,
            "ids": ids,
            "updated_at": updated_at,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("offers", "list", params)
        # Cast generic envelope to concrete typed result
        return OffersListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: OffersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OffersSearchResult:
        """
        Search offers records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OffersSearchFilter):
        - application_id: Id of the application this offer is extended on. Every offer belongs to exactly one application; the offer is voided if the application is rejected or deleted.
        - candidate_id: Id of the candidate (person) receiving this offer. Resolved through the offer's application.
        - created_at: Created at from the Greenhouse v3 offers record.
        - custom_fields: Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.
        - id: Id from the Greenhouse v3 offers record.
        - job_id: Id of the job this offer's application is on.
        - opening_id: Id of the specific opening this offer is being extended for. `null` when the offer has not yet been linked to an opening.
        - resolved_at: Timestamp the offer was resolved (`Accepted` or `Rejected`), in ISO 8601. Date updates submitted through `PATCH /v3/offers/{id}` are normalized to noon UTC on the supplied date. `null` while the offer is still `Created` or has been superseded as `Deprecated` without a resolution.
        - sent_on: Date the offer was sent to the candidate, in ISO 8601 (YYYY-MM-DD). `null` until the offer has been sent.
        - starts_on: Candidate's proposed start date, in ISO 8601 (YYYY-MM-DD). `null` when no start date has been set on the offer.
        - status: Lifecycle status of the offer. `Created` for offers still being drafted or pending approval, `Accepted` once the candidate accepts, `Rejected` if declined or withdrawn, and `Deprecated` for superseded prior versions (a new offer version replaces an earlier one with this status).
        - updated_at: Updated at from the Greenhouse v3 offers record.
        - version: Revision number of this offer within its application. Greenhouse creates a new offer row (incrementing `version`) whenever a tracked field on an existing offer changes — typically `starts_on`, `opening_id`, or a custom field configured to trigger a new version. Pair with `current_only=true` to filter the list endpoint down to the latest version per application.

        Args:
            query: Filter and sort conditions. Supports operators such as eq, neq, gt, gte, lt, lte,
                   in, startswith, endswith, contains, array_contains, fuzzy, keyword, not, and, or.
                   Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OffersSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("offers", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OffersSearchResult(
            data=[
                OffersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

    async def context_store_sql_query(
        self,
        sql: str,
        limit: int | None = None,
    ) -> AirbyteSearchResult[dict[str, Any]]:
        """
        Run a SQL query against offers records in the Airbyte Context Store.

        Only available in hosted execution mode.

        Args:
            sql: SQL query to execute.
            limit: Maximum results to return.

        Returns:
            AirbyteSearchResult containing the projected rows and query metadata.

        Raises:
            NotImplementedError: If called in local execution mode.
        """
        params: dict[str, Any] = {"sql": sql}
        if limit is not None:
            params["limit"] = limit

        result = await self._connector.execute("offers", "context_store_sql_query", params)
        meta_data = result.get("meta")
        return AirbyteSearchResult[dict[str, Any]](
            data=result.get("data", []),
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class OfficesQuery:
    """
    Query class for Offices entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        per_page: int | None = None,
        ids: list[int] | None = None,
        **kwargs
    ) -> OfficesListResult:
        """
        Returns a cursor-paginated list of offices.

        Args:
            cursor: Cursor from the previous response Link header. Do not combine with any other parameter.
            per_page: Number of records to return on the first page.
            ids: Return only records with these IDs (maximum 50).
            **kwargs: Additional parameters

        Returns:
            OfficesListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "per_page": per_page,
            "ids": ids,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("offices", "list", params)
        # Cast generic envelope to concrete typed result
        return OfficesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: OfficesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OfficesSearchResult:
        """
        Search offices records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OfficesSearchFilter):
        - created_at: Created at from the Greenhouse v3 offices record.
        - external_id: Stable identifier supplied by the customer or HRIS for cross-system reconciliation. `null` when no external id has been set. Available when the `org_structure_external_id` product flag is enabled.
        - id: Id from the Greenhouse v3 offices record.
        - location: Free-form physical location string for the office (e.g. `New York, NY, USA`). `null` for offices that have no location set, including most remote offices.
        - name: Display name of the office (e.g. `San Francisco`, `Remote (US)`). Unique among active offices in the same organization.
        - parent_id: Id of the parent office when offices are organized hierarchically. `null` for top-level offices. References another `/v3/offices` row in the same organization.
        - primary_in_house_contact_user_id: Id of the Greenhouse user designated as the office's primary internal contact, typically the local recruiting lead. References a `/v3/users` row. `null` when no contact has been assigned.
        - updated_at: Updated at from the Greenhouse v3 offices record.

        Args:
            query: Filter and sort conditions. Supports operators such as eq, neq, gt, gte, lt, lte,
                   in, startswith, endswith, contains, array_contains, fuzzy, keyword, not, and, or.
                   Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OfficesSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("offices", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OfficesSearchResult(
            data=[
                OfficesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

    async def context_store_sql_query(
        self,
        sql: str,
        limit: int | None = None,
    ) -> AirbyteSearchResult[dict[str, Any]]:
        """
        Run a SQL query against offices records in the Airbyte Context Store.

        Only available in hosted execution mode.

        Args:
            sql: SQL query to execute.
            limit: Maximum results to return.

        Returns:
            AirbyteSearchResult containing the projected rows and query metadata.

        Raises:
            NotImplementedError: If called in local execution mode.
        """
        params: dict[str, Any] = {"sql": sql}
        if limit is not None:
            params["limit"] = limit

        result = await self._connector.execute("offices", "context_store_sql_query", params)
        meta_data = result.get("meta")
        return AirbyteSearchResult[dict[str, Any]](
            data=result.get("data", []),
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SourcesQuery:
    """
    Query class for Sources entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        per_page: int | None = None,
        ids: list[int] | None = None,
        **kwargs
    ) -> SourcesListResult:
        """
        Returns a cursor-paginated list of sources.

        Args:
            cursor: Cursor from the previous response Link header. Do not combine with any other parameter.
            per_page: Number of records to return on the first page.
            ids: Return only records with these IDs (maximum 50).
            **kwargs: Additional parameters

        Returns:
            SourcesListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "per_page": per_page,
            "ids": ids,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sources", "list", params)
        # Cast generic envelope to concrete typed result
        return SourcesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: SourcesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SourcesSearchResult:
        """
        Search sources records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SourcesSearchFilter):
        - created_at: Created at from the Greenhouse v3 sources record.
        - id: Id from the Greenhouse v3 sources record.
        - name: Display name of the source as recruiters see it in Greenhouse (e.g. `LinkedIn (Prospecting)`, `Indeed`, `Referral`, `Internal Applicant`, or a custom agency name). For organization-specific sources this is the label the org configured; for global Greenhouse sources it is the standard public name.
        - type_: The sourcing strategy this source rolls up to — the broader category used for reporting. Sources are grouped under sourcing strategies such as `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`, `Company marketing`, `In person event`, `MyGreenhouse`, and `Other`. Use the strategy when aggregating candidate volume by channel; use the source itself when reporting on a specific channel within that category.
        - updated_at: Updated at from the Greenhouse v3 sources record.

        Args:
            query: Filter and sort conditions. Supports operators such as eq, neq, gt, gte, lt, lte,
                   in, startswith, endswith, contains, array_contains, fuzzy, keyword, not, and, or.
                   Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SourcesSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("sources", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SourcesSearchResult(
            data=[
                SourcesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

    async def context_store_sql_query(
        self,
        sql: str,
        limit: int | None = None,
    ) -> AirbyteSearchResult[dict[str, Any]]:
        """
        Run a SQL query against sources records in the Airbyte Context Store.

        Only available in hosted execution mode.

        Args:
            sql: SQL query to execute.
            limit: Maximum results to return.

        Returns:
            AirbyteSearchResult containing the projected rows and query metadata.

        Raises:
            NotImplementedError: If called in local execution mode.
        """
        params: dict[str, Any] = {"sql": sql}
        if limit is not None:
            params["limit"] = limit

        result = await self._connector.execute("sources", "context_store_sql_query", params)
        meta_data = result.get("meta")
        return AirbyteSearchResult[dict[str, Any]](
            data=result.get("data", []),
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        per_page: int | None = None,
        ids: list[int] | None = None,
        updated_at: str | None = None,
        show_service_accounts: bool | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        Returns a cursor-paginated list of users.

        Args:
            cursor: Cursor from the previous response Link header. Do not combine with any other parameter.
            per_page: Number of records to return on the first page.
            ids: Return only records with these IDs (maximum 50).
            updated_at: Filter by updated timestamp using the Harvest v3 pipe expression, such as gte|2026-01-01T00:00:00Z.
            show_service_accounts: Include Greenhouse service accounts.
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "per_page": per_page,
            "ids": ids,
            "updated_at": updated_at,
            "show_service_accounts": show_service_accounts,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        # Cast generic envelope to concrete typed result
        return UsersListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: UsersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> UsersSearchResult:
        """
        Search users records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (UsersSearchFilter):
        - agency_id: Id of the staffing agency this user belongs to, when the user is an external agency recruiter rather than an employee of your organization. `null` for in-house users.
        - created_at: Created at from the Greenhouse v3 users record.
        - custom_fields: Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.
        - deactivated: Whether the user has been deactivated. Deactivated users cannot sign in or be assigned to new jobs, but their historical activity (notes, scorecards, emails) is preserved. Toggle via `POST /v3/users/{id}/deactivate` and `POST /v3/users/{id}/activate`.
        - department_ids: Ids of the departments this user is assigned to. Used to scope future job permissions and to filter the user list by department. Empty when the user is not pinned to any department.
        - emails: All email addresses on the user's account, including the primary address and any additional verified addresses.
        - employee_id: Partner-supplied external employee identifier, typically the user's HRIS or payroll id. Free-form string; not unique across organizations and `null` when no employee id has been set.
        - first_name: First name from the Greenhouse v3 users record.
        - id: Id from the Greenhouse v3 users record.
        - interviewer_tags: Interviewer tags applied to this user — the labeled skill or panel groupings (e.g. `Senior Engineer`, `Bar Raiser`) used to suggest qualified interviewers when building an interview plan. Each entry pairs the tag's `id` with its `name`.
        - job_title: Free-form job title set on the user's Greenhouse profile (e.g. `Senior Recruiter`). Not synchronized with any HRIS title.
        - last_name: Last name from the Greenhouse v3 users record.
        - linked_candidate_ids: Ids of candidate records linked to this user. Populated when an employee is represented by both a user record (for Greenhouse access) and a candidate record (for past or internal applications).
        - name: Concatenation of `first_name` and `last_name` rendered as a single display string. Provided for convenience; partners that need either component should read `first_name`/`last_name` directly.
        - office_ids: Ids of the offices this user is assigned to. Used to scope future job permissions and to filter the user list by office. Empty when the user is not pinned to any office.
        - primary_email: Primary email address on the user's account. Sign-in identifier and the address Greenhouse uses for outbound mail; additional verified addresses are not surfaced here. Service accounts (integration/ISU users) have no email and are excluded from this endpoint by default; when included via `show_service_accounts=true`, their `primary_email` is an empty string.
        - site_admin: Whether the user holds the Site Admin role. Site admins have unrestricted access to every non-confidential job and to organization-level settings. Demote a site admin to a Basic user with `POST /v3/users/{id}/revoke_permissions`.
        - updated_at: Updated at from the Greenhouse v3 users record.

        Args:
            query: Filter and sort conditions. Supports operators such as eq, neq, gt, gte, lt, lte,
                   in, startswith, endswith, contains, array_contains, fuzzy, keyword, not, and, or.
                   Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            UsersSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("users", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return UsersSearchResult(
            data=[
                UsersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

    async def context_store_sql_query(
        self,
        sql: str,
        limit: int | None = None,
    ) -> AirbyteSearchResult[dict[str, Any]]:
        """
        Run a SQL query against users records in the Airbyte Context Store.

        Only available in hosted execution mode.

        Args:
            sql: SQL query to execute.
            limit: Maximum results to return.

        Returns:
            AirbyteSearchResult containing the projected rows and query metadata.

        Raises:
            NotImplementedError: If called in local execution mode.
        """
        params: dict[str, Any] = {"sql": sql}
        if limit is not None:
            params["limit"] = limit

        result = await self._connector.execute("users", "context_store_sql_query", params)
        meta_data = result.get("meta")
        return AirbyteSearchResult[dict[str, Any]](
            data=result.get("data", []),
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AttachmentsQuery:
    """
    Query class for Attachments entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        per_page: int | None = None,
        ids: list[int] | None = None,
        updated_at: str | None = None,
        application_ids: list[int] | None = None,
        candidate_ids: list[int] | None = None,
        type: str | None = None,
        **kwargs
    ) -> AttachmentsListResult:
        """
        Returns a cursor-paginated list of attachments.

        Args:
            cursor: Cursor from the previous response Link header. Do not combine with any other parameter.
            per_page: Number of records to return on the first page.
            ids: Return only records with these IDs (maximum 50).
            updated_at: Filter by updated timestamp using the Harvest v3 pipe expression, such as gte|2026-01-01T00:00:00Z.
            application_ids: Return attachments associated with these application IDs (maximum 50).
            candidate_ids: Return attachments belonging to these candidate IDs (maximum 50).
            type: Filter by attachment type.
            **kwargs: Additional parameters

        Returns:
            AttachmentsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "per_page": per_page,
            "ids": ids,
            "updated_at": updated_at,
            "application_ids": application_ids,
            "candidate_ids": candidate_ids,
            "type": type,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "list", params)
        # Cast generic envelope to concrete typed result
        return AttachmentsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def download(
        self,
        ids: list[int],
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Looks up an attachment by ID and follows its current time-limited download URL.

        Args:
            ids: The single attachment ID to download.
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "ids": ids,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "download", params)
        return result


    async def download_text(
        self,
        ids: list[int],
        range_header: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Looks up an attachment by ID and follows its current time-limited download URL. and return a JSON-safe UTF-8 text chunk.
        """
        params = {k: v for k, v in {
            "ids": ids,
            "range_header": range_header,
            **kwargs,
            "_airbyte_response_type": "json",
            "_airbyte_response_format": "text",
        }.items() if v is not None}

        return await self._connector.execute("attachments", "download", params)

    async def download_base64(
        self,
        ids: list[int],
        range_header: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Looks up an attachment by ID and follows its current time-limited download URL. and return a JSON-safe base64 chunk.
        """
        params = {k: v for k, v in {
            "ids": ids,
            "range_header": range_header,
            **kwargs,
            "_airbyte_response_type": "json",
            "_airbyte_response_format": "base64",
        }.items() if v is not None}

        return await self._connector.execute("attachments", "download", params)

    async def download_local(
        self,
        ids: list[int],
        path: str,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Looks up an attachment by ID and follows its current time-limited download URL. and save to file.

        Args:
            ids: The single attachment ID to download.
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from airbyte_agent_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            ids=ids,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)

