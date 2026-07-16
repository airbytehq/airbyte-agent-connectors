"""
Zendesk-Chat connector.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import ZendeskChatConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    AccountsGetParams,
    AgentTimelineListParams,
    AgentsGetParams,
    AgentsListParams,
    BansGetParams,
    BansListParams,
    ChatsGetParams,
    ChatsListParams,
    DepartmentsGetParams,
    DepartmentsListParams,
    GoalsGetParams,
    GoalsListParams,
    RolesGetParams,
    RolesListParams,
    RoutingSettingsGetParams,
    ShortcutsGetParams,
    ShortcutsListParams,
    SkillsGetParams,
    SkillsListParams,
    TriggersListParams,
    AirbyteSearchParams,
    AgentsSearchFilter,
    AgentsSearchQuery,
    ChatsSearchFilter,
    ChatsSearchQuery,
    DepartmentsSearchFilter,
    DepartmentsSearchQuery,
    ShortcutsSearchFilter,
    ShortcutsSearchQuery,
    TriggersSearchFilter,
    TriggersSearchQuery,
)
from .models import ZendeskChatAuthConfig
if TYPE_CHECKING:
    from .models import ZendeskChatReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    ZendeskChatCheckResult,
    ZendeskChatExecuteResult,
    ZendeskChatExecuteResultWithMeta,
    AgentsListResult,
    AgentTimelineListResult,
    BansListResult,
    ChatsListResult,
    DepartmentsListResult,
    GoalsListResult,
    RolesListResult,
    ShortcutsListResult,
    SkillsListResult,
    TriggersListResult,
    Account,
    Agent,
    AgentTimeline,
    Ban,
    Chat,
    Department,
    Goal,
    Role,
    RoutingSettings,
    Shortcut,
    Skill,
    Trigger,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AgentsSearchData,
    AgentsSearchResult,
    ChatsSearchData,
    ChatsSearchResult,
    DepartmentsSearchData,
    DepartmentsSearchResult,
    ShortcutsSearchData,
    ShortcutsSearchResult,
    TriggersSearchData,
    TriggersSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class ZendeskChatConnector:
    """
    Type-safe Zendesk-Chat API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "zendesk-chat"
    connector_version = "0.1.10"
    sdk_version = "0.1.287"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("accounts", "get"): None,
        ("agents", "list"): True,
        ("agents", "get"): None,
        ("agent_timeline", "list"): True,
        ("bans", "list"): True,
        ("bans", "get"): None,
        ("chats", "list"): True,
        ("chats", "get"): None,
        ("departments", "list"): True,
        ("departments", "get"): None,
        ("goals", "list"): True,
        ("goals", "get"): None,
        ("roles", "list"): True,
        ("roles", "get"): None,
        ("routing_settings", "get"): None,
        ("shortcuts", "list"): True,
        ("shortcuts", "get"): None,
        ("skills", "list"): True,
        ("skills", "get"): None,
        ("triggers", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('agents', 'list'): {'limit': 'limit', 'since_id': 'since_id'},
        ('agents', 'get'): {'agent_id': 'agent_id'},
        ('agent_timeline', 'list'): {'start_time': 'start_time', 'limit': 'limit', 'fields': 'fields'},
        ('bans', 'list'): {'limit': 'limit', 'since_id': 'since_id'},
        ('bans', 'get'): {'ban_id': 'ban_id'},
        ('chats', 'list'): {'start_time': 'start_time', 'limit': 'limit', 'fields': 'fields'},
        ('chats', 'get'): {'chat_id': 'chat_id'},
        ('departments', 'get'): {'department_id': 'department_id'},
        ('goals', 'get'): {'goal_id': 'goal_id'},
        ('roles', 'get'): {'role_id': 'role_id'},
        ('shortcuts', 'get'): {'shortcut_id': 'shortcut_id'},
        ('skills', 'get'): {'skill_id': 'skill_id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (ZendeskChatAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: ZendeskChatAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        subdomain: str | None = None    ):
        """
        Initialize a new zendesk-chat connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., ZendeskChatAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            subdomain: Your Zendesk subdomain (the part before .zendesk.com in your Zendesk URL)
        Examples:
            # Local mode (direct API calls)
            connector = ZendeskChatConnector(auth_config=ZendeskChatAuthConfig(access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = ZendeskChatConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = ZendeskChatConnector(
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
                connector_definition_id=str(ZendeskChatConnectorModel.id),
                model=ZendeskChatConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or ZendeskChatAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if subdomain:
                config_values["subdomain"] = subdomain

            self._executor = LocalExecutor(
                model=ZendeskChatConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if subdomain:
                base_url = base_url.replace("{subdomain}", subdomain)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.accounts = AccountsQuery(self)
        self.agents = AgentsQuery(self)
        self.agent_timeline = AgentTimelineQuery(self)
        self.bans = BansQuery(self)
        self.chats = ChatsQuery(self)
        self.departments = DepartmentsQuery(self)
        self.goals = GoalsQuery(self)
        self.roles = RolesQuery(self)
        self.routing_settings = RoutingSettingsQuery(self)
        self.shortcuts = ShortcutsQuery(self)
        self.skills = SkillsQuery(self)
        self.triggers = TriggersQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["get"],
        params: "AccountsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Account": ...

    @overload
    async def execute(
        self,
        entity: Literal["agents"],
        action: Literal["list"],
        params: "AgentsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AgentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["agents"],
        action: Literal["get"],
        params: "AgentsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Agent": ...

    @overload
    async def execute(
        self,
        entity: Literal["agent_timeline"],
        action: Literal["list"],
        params: "AgentTimelineListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AgentTimelineListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["bans"],
        action: Literal["list"],
        params: "BansListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "BansListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["bans"],
        action: Literal["get"],
        params: "BansGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Ban": ...

    @overload
    async def execute(
        self,
        entity: Literal["chats"],
        action: Literal["list"],
        params: "ChatsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ChatsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["chats"],
        action: Literal["get"],
        params: "ChatsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Chat": ...

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
        entity: Literal["departments"],
        action: Literal["get"],
        params: "DepartmentsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Department": ...

    @overload
    async def execute(
        self,
        entity: Literal["goals"],
        action: Literal["list"],
        params: "GoalsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "GoalsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["goals"],
        action: Literal["get"],
        params: "GoalsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Goal": ...

    @overload
    async def execute(
        self,
        entity: Literal["roles"],
        action: Literal["list"],
        params: "RolesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "RolesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["roles"],
        action: Literal["get"],
        params: "RolesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Role": ...

    @overload
    async def execute(
        self,
        entity: Literal["routing_settings"],
        action: Literal["get"],
        params: "RoutingSettingsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "RoutingSettings": ...

    @overload
    async def execute(
        self,
        entity: Literal["shortcuts"],
        action: Literal["list"],
        params: "ShortcutsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ShortcutsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["shortcuts"],
        action: Literal["get"],
        params: "ShortcutsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Shortcut": ...

    @overload
    async def execute(
        self,
        entity: Literal["skills"],
        action: Literal["list"],
        params: "SkillsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SkillsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["skills"],
        action: Literal["get"],
        params: "SkillsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Skill": ...

    @overload
    async def execute(
        self,
        entity: Literal["triggers"],
        action: Literal["list"],
        params: "TriggersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TriggersListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["get", "list", "context_store_search"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> ZendeskChatExecuteResult[Any] | ZendeskChatExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["get", "list", "context_store_search"],
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
                return ZendeskChatExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return ZendeskChatExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> ZendeskChatCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            ZendeskChatCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return ZendeskChatCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return ZendeskChatCheckResult(
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

        connector = ZendeskChatConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @ZendeskChatConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @ZendeskChatConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @ZendeskChatConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
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
                    ZendeskChatConnectorModel,
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
        return describe_entities(ZendeskChatConnectorModel)

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
            (e for e in ZendeskChatConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in ZendeskChatConnectorModel.entities]}"
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



class AccountsQuery:
    """
    Query class for Accounts entity operations.
    """

    def __init__(self, connector: ZendeskChatConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        **kwargs
    ) -> Account:
        """
        Returns the account information for the authenticated user

        Returns:
            Account
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "get", params)
        return result



class AgentsQuery:
    """
    Query class for Agents entity operations.
    """

    def __init__(self, connector: ZendeskChatConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        **kwargs
    ) -> AgentsListResult:
        """
        List all agents

        Args:
            limit: Parameter limit
            since_id: Parameter since_id
            **kwargs: Additional parameters

        Returns:
            AgentsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("agents", "list", params)
        # Cast generic envelope to concrete typed result
        return AgentsListResult(
            data=result.data
        )



    async def get(
        self,
        agent_id: str,
        **kwargs
    ) -> Agent:
        """
        Get an agent

        Args:
            agent_id: Parameter agent_id
            **kwargs: Additional parameters

        Returns:
            Agent
        """
        params = {k: v for k, v in {
            "agent_id": agent_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("agents", "get", params)
        return result



    async def context_store_search(
        self,
        query: AgentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AgentsSearchResult:
        """
        Search agents records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AgentsSearchFilter):
        - id: Unique agent identifier
        - email: Agent email address
        - display_name: Agent display name
        - first_name: Agent first name
        - last_name: Agent last name
        - enabled: Whether agent is enabled
        - role_id: Agent role ID
        - departments: Department IDs agent belongs to
        - create_date: When agent was created

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AgentsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("agents", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AgentsSearchResult(
            data=[
                AgentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AgentTimelineQuery:
    """
    Query class for AgentTimeline entity operations.
    """

    def __init__(self, connector: ZendeskChatConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_time: int | None = None,
        limit: int | None = None,
        fields: str | None = None,
        **kwargs
    ) -> AgentTimelineListResult:
        """
        List agent timeline (incremental export)

        Args:
            start_time: Parameter start_time
            limit: Parameter limit
            fields: Parameter fields
            **kwargs: Additional parameters

        Returns:
            AgentTimelineListResult
        """
        params = {k: v for k, v in {
            "start_time": start_time,
            "limit": limit,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("agent_timeline", "list", params)
        # Cast generic envelope to concrete typed result
        return AgentTimelineListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



class BansQuery:
    """
    Query class for Bans entity operations.
    """

    def __init__(self, connector: ZendeskChatConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        **kwargs
    ) -> BansListResult:
        """
        List all bans

        Args:
            limit: Parameter limit
            since_id: Parameter since_id
            **kwargs: Additional parameters

        Returns:
            BansListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("bans", "list", params)
        # Cast generic envelope to concrete typed result
        return BansListResult(
            data=result.data
        )



    async def get(
        self,
        ban_id: str,
        **kwargs
    ) -> Ban:
        """
        Get a ban

        Args:
            ban_id: Parameter ban_id
            **kwargs: Additional parameters

        Returns:
            Ban
        """
        params = {k: v for k, v in {
            "ban_id": ban_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("bans", "get", params)
        return result



class ChatsQuery:
    """
    Query class for Chats entity operations.
    """

    def __init__(self, connector: ZendeskChatConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_time: int | None = None,
        limit: int | None = None,
        fields: str | None = None,
        **kwargs
    ) -> ChatsListResult:
        """
        List chats (incremental export)

        Args:
            start_time: Parameter start_time
            limit: Parameter limit
            fields: Parameter fields
            **kwargs: Additional parameters

        Returns:
            ChatsListResult
        """
        params = {k: v for k, v in {
            "start_time": start_time,
            "limit": limit,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("chats", "list", params)
        # Cast generic envelope to concrete typed result
        return ChatsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        chat_id: str,
        **kwargs
    ) -> Chat:
        """
        Get a chat

        Args:
            chat_id: Parameter chat_id
            **kwargs: Additional parameters

        Returns:
            Chat
        """
        params = {k: v for k, v in {
            "chat_id": chat_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("chats", "get", params)
        return result



    async def context_store_search(
        self,
        query: ChatsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ChatsSearchResult:
        """
        Search chats records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ChatsSearchFilter):
        - id: Unique chat identifier
        - timestamp: Chat start timestamp
        - update_timestamp: Last update timestamp
        - department_id: Department ID
        - department_name: Department name
        - duration: Chat duration in seconds
        - rating: Satisfaction rating
        - missed: Whether chat was missed
        - agent_ids: IDs of agents in chat

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ChatsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("chats", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ChatsSearchResult(
            data=[
                ChatsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class DepartmentsQuery:
    """
    Query class for Departments entity operations.
    """

    def __init__(self, connector: ZendeskChatConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> DepartmentsListResult:
        """
        List all departments

        Returns:
            DepartmentsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("departments", "list", params)
        # Cast generic envelope to concrete typed result
        return DepartmentsListResult(
            data=result.data
        )



    async def get(
        self,
        department_id: str,
        **kwargs
    ) -> Department:
        """
        Get a department

        Args:
            department_id: Parameter department_id
            **kwargs: Additional parameters

        Returns:
            Department
        """
        params = {k: v for k, v in {
            "department_id": department_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("departments", "get", params)
        return result



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
        - id: Department ID
        - name: Department name
        - enabled: Whether department is enabled
        - members: Agent IDs in department

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
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

class GoalsQuery:
    """
    Query class for Goals entity operations.
    """

    def __init__(self, connector: ZendeskChatConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> GoalsListResult:
        """
        List all goals

        Returns:
            GoalsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("goals", "list", params)
        # Cast generic envelope to concrete typed result
        return GoalsListResult(
            data=result.data
        )



    async def get(
        self,
        goal_id: str,
        **kwargs
    ) -> Goal:
        """
        Get a goal

        Args:
            goal_id: Parameter goal_id
            **kwargs: Additional parameters

        Returns:
            Goal
        """
        params = {k: v for k, v in {
            "goal_id": goal_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("goals", "get", params)
        return result



class RolesQuery:
    """
    Query class for Roles entity operations.
    """

    def __init__(self, connector: ZendeskChatConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> RolesListResult:
        """
        List all roles

        Returns:
            RolesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("roles", "list", params)
        # Cast generic envelope to concrete typed result
        return RolesListResult(
            data=result.data
        )



    async def get(
        self,
        role_id: str,
        **kwargs
    ) -> Role:
        """
        Get a role

        Args:
            role_id: Parameter role_id
            **kwargs: Additional parameters

        Returns:
            Role
        """
        params = {k: v for k, v in {
            "role_id": role_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("roles", "get", params)
        return result



class RoutingSettingsQuery:
    """
    Query class for RoutingSettings entity operations.
    """

    def __init__(self, connector: ZendeskChatConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        **kwargs
    ) -> RoutingSettings:
        """
        Get routing settings

        Returns:
            RoutingSettings
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("routing_settings", "get", params)
        return result



class ShortcutsQuery:
    """
    Query class for Shortcuts entity operations.
    """

    def __init__(self, connector: ZendeskChatConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> ShortcutsListResult:
        """
        List all shortcuts

        Returns:
            ShortcutsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("shortcuts", "list", params)
        # Cast generic envelope to concrete typed result
        return ShortcutsListResult(
            data=result.data
        )



    async def get(
        self,
        shortcut_id: str,
        **kwargs
    ) -> Shortcut:
        """
        Get a shortcut

        Args:
            shortcut_id: Parameter shortcut_id
            **kwargs: Additional parameters

        Returns:
            Shortcut
        """
        params = {k: v for k, v in {
            "shortcut_id": shortcut_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("shortcuts", "get", params)
        return result



    async def context_store_search(
        self,
        query: ShortcutsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ShortcutsSearchResult:
        """
        Search shortcuts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ShortcutsSearchFilter):
        - id: Shortcut ID
        - name: Shortcut name/trigger
        - message: Shortcut message content
        - tags: Tags applied when shortcut is used

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ShortcutsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("shortcuts", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ShortcutsSearchResult(
            data=[
                ShortcutsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SkillsQuery:
    """
    Query class for Skills entity operations.
    """

    def __init__(self, connector: ZendeskChatConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> SkillsListResult:
        """
        List all skills

        Returns:
            SkillsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("skills", "list", params)
        # Cast generic envelope to concrete typed result
        return SkillsListResult(
            data=result.data
        )



    async def get(
        self,
        skill_id: str,
        **kwargs
    ) -> Skill:
        """
        Get a skill

        Args:
            skill_id: Parameter skill_id
            **kwargs: Additional parameters

        Returns:
            Skill
        """
        params = {k: v for k, v in {
            "skill_id": skill_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("skills", "get", params)
        return result



class TriggersQuery:
    """
    Query class for Triggers entity operations.
    """

    def __init__(self, connector: ZendeskChatConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> TriggersListResult:
        """
        List all triggers

        Returns:
            TriggersListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("triggers", "list", params)
        # Cast generic envelope to concrete typed result
        return TriggersListResult(
            data=result.data
        )



    async def context_store_search(
        self,
        query: TriggersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TriggersSearchResult:
        """
        Search triggers records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TriggersSearchFilter):
        - id: Trigger ID
        - name: Trigger name
        - enabled: Whether trigger is enabled

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TriggersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("triggers", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TriggersSearchResult(
            data=[
                TriggersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
