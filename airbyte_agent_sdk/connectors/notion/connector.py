"""
Notion connector.
"""

from __future__ import annotations

import logging
from typing import Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import NotionConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    BlocksCreateParams,
    BlocksCreateParamsChildrenItem,
    BlocksGetParams,
    BlocksListParams,
    BlocksUpdateParams,
    BlocksUpdateParamsAudio,
    BlocksUpdateParamsBookmark,
    BlocksUpdateParamsBulletedListItem,
    BlocksUpdateParamsCallout,
    BlocksUpdateParamsCode,
    BlocksUpdateParamsEmbed,
    BlocksUpdateParamsEquation,
    BlocksUpdateParamsFile,
    BlocksUpdateParamsHeading1,
    BlocksUpdateParamsHeading2,
    BlocksUpdateParamsHeading3,
    BlocksUpdateParamsImage,
    BlocksUpdateParamsNumberedListItem,
    BlocksUpdateParamsParagraph,
    BlocksUpdateParamsPdf,
    BlocksUpdateParamsQuote,
    BlocksUpdateParamsTable,
    BlocksUpdateParamsToDo,
    BlocksUpdateParamsToggle,
    BlocksUpdateParamsVideo,
    CommentsCreateParams,
    CommentsCreateParamsRichTextItem,
    CommentsListParams,
    DataSourcesGetParams,
    DataSourcesListParams,
    DataSourcesListParamsFilter,
    DataSourcesListParamsSort,
    DataSourcesUpdateParams,
    DataSourcesUpdateParamsCover,
    DataSourcesUpdateParamsDescriptionItem,
    DataSourcesUpdateParamsIcon,
    DataSourcesUpdateParamsTitleItem,
    PagesCreateParams,
    PagesCreateParamsCover,
    PagesCreateParamsIcon,
    PagesGetParams,
    PagesListParams,
    PagesListParamsFilter,
    PagesListParamsSort,
    PagesUpdateParams,
    PagesUpdateParamsCover,
    PagesUpdateParamsIcon,
    UsersGetParams,
    UsersListParams,
    AirbyteSearchParams,
    PagesSearchFilter,
    PagesSearchQuery,
    UsersSearchFilter,
    UsersSearchQuery,
    DataSourcesSearchFilter,
    DataSourcesSearchQuery,
    BlocksSearchFilter,
    BlocksSearchQuery,
    CommentsSearchFilter,
    CommentsSearchQuery,
)
from .models import NotionOauth20AuthConfig, NotionAccessTokenAuthConfig
from .models import NotionAuthConfig

# Import response models and envelope models at runtime
from .models import (
    NotionCheckResult,
    NotionExecuteResult,
    NotionExecuteResultWithMeta,
    UsersListResult,
    PagesListResult,
    DataSourcesListResult,
    BlocksListResult,
    CommentsListResult,
    Block,
    Comment,
    DataSource,
    Page,
    User,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    PagesSearchData,
    PagesSearchResult,
    UsersSearchData,
    UsersSearchResult,
    DataSourcesSearchData,
    DataSourcesSearchResult,
    BlocksSearchData,
    BlocksSearchResult,
    CommentsSearchData,
    CommentsSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class NotionConnector:
    """
    Type-safe Notion API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "notion"
    connector_version = "0.1.12"
    sdk_version = "0.1.287"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("users", "list"): True,
        ("users", "get"): None,
        ("pages", "list"): True,
        ("pages", "create"): None,
        ("pages", "get"): None,
        ("pages", "update"): None,
        ("data_sources", "list"): True,
        ("data_sources", "get"): None,
        ("blocks", "list"): True,
        ("blocks", "create"): None,
        ("blocks", "get"): None,
        ("blocks", "update"): None,
        ("comments", "list"): True,
        ("comments", "create"): None,
        ("data_sources", "update"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('users', 'list'): {'start_cursor': 'start_cursor', 'page_size': 'page_size'},
        ('users', 'get'): {'user_id': 'user_id'},
        ('pages', 'list'): {'filter': 'filter', 'sort': 'sort', 'start_cursor': 'start_cursor', 'page_size': 'page_size'},
        ('pages', 'create'): {'parent': 'parent', 'properties': 'properties', 'children': 'children', 'icon': 'icon', 'cover': 'cover'},
        ('pages', 'get'): {'page_id': 'page_id'},
        ('pages', 'update'): {'properties': 'properties', 'icon': 'icon', 'cover': 'cover', 'archived': 'archived', 'in_trash': 'in_trash', 'page_id': 'page_id'},
        ('data_sources', 'list'): {'filter': 'filter', 'sort': 'sort', 'start_cursor': 'start_cursor', 'page_size': 'page_size'},
        ('data_sources', 'get'): {'data_source_id': 'data_source_id'},
        ('blocks', 'list'): {'block_id': 'block_id', 'start_cursor': 'start_cursor', 'page_size': 'page_size'},
        ('blocks', 'create'): {'children': 'children', 'block_id': 'block_id'},
        ('blocks', 'get'): {'block_id': 'block_id'},
        ('blocks', 'update'): {'paragraph': 'paragraph', 'heading_1': 'heading_1', 'heading_2': 'heading_2', 'heading_3': 'heading_3', 'bulleted_list_item': 'bulleted_list_item', 'numbered_list_item': 'numbered_list_item', 'to_do': 'to_do', 'toggle': 'toggle', 'code': 'code', 'quote': 'quote', 'callout': 'callout', 'bookmark': 'bookmark', 'embed': 'embed', 'equation': 'equation', 'image': 'image', 'video': 'video', 'file': 'file', 'pdf': 'pdf', 'audio': 'audio', 'table': 'table', 'archived': 'archived', 'block_id': 'block_id'},
        ('comments', 'list'): {'block_id': 'block_id', 'start_cursor': 'start_cursor', 'page_size': 'page_size'},
        ('comments', 'create'): {'parent': 'parent', 'discussion_id': 'discussion_id', 'rich_text': 'rich_text'},
        ('data_sources', 'update'): {'title': 'title', 'description': 'description', 'properties': 'properties', 'icon': 'icon', 'cover': 'cover', 'archived': 'archived', 'in_trash': 'in_trash', 'data_source_id': 'data_source_id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (NotionOauth20AuthConfig, NotionAccessTokenAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: NotionAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new notion connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., NotionAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = NotionConnector(auth_config=NotionAuthConfig(client_id="...", client_secret="...", access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = NotionConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = NotionConnector(
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
                connector_definition_id=str(NotionConnectorModel.id),
                model=NotionConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or NotionAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            # Multi-auth connector: detect auth scheme from auth_config type
            auth_scheme: str | None = None
            if auth_config:
                if isinstance(auth_config, NotionOauth20AuthConfig):
                    auth_scheme = "notionOAuth"
                if isinstance(auth_config, NotionAccessTokenAuthConfig):
                    auth_scheme = "notionBearerToken"

            self._executor = LocalExecutor(
                model=NotionConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                auth_scheme=auth_scheme,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.users = UsersQuery(self)
        self.pages = PagesQuery(self)
        self.data_sources = DataSourcesQuery(self)
        self.blocks = BlocksQuery(self)
        self.comments = CommentsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

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
        entity: Literal["users"],
        action: Literal["get"],
        params: "UsersGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "User": ...

    @overload
    async def execute(
        self,
        entity: Literal["pages"],
        action: Literal["list"],
        params: "PagesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "PagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["pages"],
        action: Literal["create"],
        params: "PagesCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Page": ...

    @overload
    async def execute(
        self,
        entity: Literal["pages"],
        action: Literal["get"],
        params: "PagesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Page": ...

    @overload
    async def execute(
        self,
        entity: Literal["pages"],
        action: Literal["update"],
        params: "PagesUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Page": ...

    @overload
    async def execute(
        self,
        entity: Literal["data_sources"],
        action: Literal["list"],
        params: "DataSourcesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DataSourcesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["data_sources"],
        action: Literal["get"],
        params: "DataSourcesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DataSource": ...

    @overload
    async def execute(
        self,
        entity: Literal["blocks"],
        action: Literal["list"],
        params: "BlocksListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "BlocksListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["blocks"],
        action: Literal["create"],
        params: "BlocksCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "list[Block]": ...

    @overload
    async def execute(
        self,
        entity: Literal["blocks"],
        action: Literal["get"],
        params: "BlocksGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Block": ...

    @overload
    async def execute(
        self,
        entity: Literal["blocks"],
        action: Literal["update"],
        params: "BlocksUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Block": ...

    @overload
    async def execute(
        self,
        entity: Literal["comments"],
        action: Literal["list"],
        params: "CommentsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CommentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["comments"],
        action: Literal["create"],
        params: "CommentsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Comment": ...

    @overload
    async def execute(
        self,
        entity: Literal["data_sources"],
        action: Literal["update"],
        params: "DataSourcesUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DataSource": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "create", "update", "context_store_search"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> NotionExecuteResult[Any] | NotionExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "create", "update", "context_store_search"],
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
                return NotionExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return NotionExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> NotionCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            NotionCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return NotionCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return NotionCheckResult(
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

        connector = NotionConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @NotionConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @NotionConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @NotionConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
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
                    NotionConnectorModel,
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
        return describe_entities(NotionConnectorModel)

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
            (e for e in NotionConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in NotionConnectorModel.entities]}"
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



class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: NotionConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_cursor: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> UsersListResult:
        """
        Returns a paginated list of users for the workspace

        Args:
            start_cursor: Pagination cursor for next page
            page_size: Number of items per page (max 100)
            **kwargs: Additional parameters

        Returns:
            UsersListResult
        """
        params = {k: v for k, v in {
            "start_cursor": start_cursor,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        # Cast generic envelope to concrete typed result
        return UsersListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        user_id: str,
        **kwargs
    ) -> User:
        """
        Retrieves a single user by ID

        Args:
            user_id: User ID
            **kwargs: Additional parameters

        Returns:
            User
        """
        params = {k: v for k, v in {
            "user_id": user_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        return result



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
        - avatar_url: URL of the user's avatar
        - bot: Bot-specific data
        - id: Unique identifier for the user
        - name: User's display name
        - object_: Always user
        - person: Person-specific data
        - type_: Type of user (person or bot)

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
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

class PagesQuery:
    """
    Query class for Pages entity operations.
    """

    def __init__(self, connector: NotionConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        filter: PagesListParamsFilter | None = None,
        sort: PagesListParamsSort | None = None,
        start_cursor: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> PagesListResult:
        """
        Returns pages shared with the integration using the search endpoint

        Args:
            filter: Parameter filter
            sort: Parameter sort
            start_cursor: Pagination cursor
            page_size: Parameter page_size
            **kwargs: Additional parameters

        Returns:
            PagesListResult
        """
        params = {k: v for k, v in {
            "filter": filter,
            "sort": sort,
            "start_cursor": start_cursor,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pages", "list", params)
        # Cast generic envelope to concrete typed result
        return PagesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        parent: dict[str, Any],
        properties: dict[str, Any] | None = None,
        children: list[dict[str, Any]] | None = None,
        icon: PagesCreateParamsIcon | None | None = None,
        cover: PagesCreateParamsCover | None | None = None,
        **kwargs
    ) -> Page:
        """
        Creates a new page as a child of an existing page or data source

        Args:
            parent: Parent of the page. Provide exactly one of page_id, database_id, data_source_id, or workspace.
            properties: Page properties. For pages under a page, use title property. For data source pages, match the data source schema.
            children: Content blocks to add to the page (max 100)
            icon: Icon. Supports emoji, external URL, file upload, custom emoji, and Notion native icons. Set to null to remove.
            cover: Cover image. Supports external URL or file upload. Set to null to remove.
            **kwargs: Additional parameters

        Returns:
            Page
        """
        params = {k: v for k, v in {
            "parent": parent,
            "properties": properties,
            "children": children,
            "icon": icon,
            "cover": cover,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pages", "create", params)
        return result



    async def get(
        self,
        page_id: str,
        **kwargs
    ) -> Page:
        """
        Retrieves a page object using the ID specified

        Args:
            page_id: Page ID
            **kwargs: Additional parameters

        Returns:
            Page
        """
        params = {k: v for k, v in {
            "page_id": page_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pages", "get", params)
        return result



    async def update(
        self,
        page_id: str,
        properties: dict[str, Any] | None = None,
        icon: PagesUpdateParamsIcon | None | None = None,
        cover: PagesUpdateParamsCover | None | None = None,
        archived: bool | None = None,
        in_trash: bool | None = None,
        **kwargs
    ) -> Page:
        """
        Updates page properties, icon, cover, or archived status

        Args:
            properties: Page property values to update. Keys must match the page's property schema.
            icon: Icon. Supports emoji, external URL, file upload, custom emoji, and Notion native icons. Set to null to remove.
            cover: Cover image. Supports external URL or file upload. Set to null to remove.
            archived: Set to true to archive the page, false to un-archive
            in_trash: Set to true to move the page to trash, false to restore
            page_id: Page ID
            **kwargs: Additional parameters

        Returns:
            Page
        """
        params = {k: v for k, v in {
            "properties": properties,
            "icon": icon,
            "cover": cover,
            "archived": archived,
            "in_trash": in_trash,
            "page_id": page_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pages", "update", params)
        return result



    async def context_store_search(
        self,
        query: PagesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> PagesSearchResult:
        """
        Search pages records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (PagesSearchFilter):
        - archived: Indicates whether the page is archived or not.
        - cover: URL or reference to the page cover image.
        - created_by: User ID or name of the creator of the page.
        - created_time: Date and time when the page was created.
        - icon: URL or reference to the page icon.
        - id: Unique identifier of the page.
        - in_trash: Indicates whether the page is in trash or not.
        - last_edited_by: User ID or name of the last editor of the page.
        - last_edited_time: Date and time when the page was last edited.
        - object_: Type or category of the page object.
        - parent: ID or reference to the parent page.
        - properties: Custom properties associated with the page.
        - public_url: Publicly accessible URL of the page.
        - url: URL of the page within the service.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            PagesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("pages", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return PagesSearchResult(
            data=[
                PagesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class DataSourcesQuery:
    """
    Query class for DataSources entity operations.
    """

    def __init__(self, connector: NotionConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        filter: DataSourcesListParamsFilter | None = None,
        sort: DataSourcesListParamsSort | None = None,
        start_cursor: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> DataSourcesListResult:
        """
        Returns data sources shared with the integration using the search endpoint

        Args:
            filter: Parameter filter
            sort: Parameter sort
            start_cursor: Pagination cursor
            page_size: Parameter page_size
            **kwargs: Additional parameters

        Returns:
            DataSourcesListResult
        """
        params = {k: v for k, v in {
            "filter": filter,
            "sort": sort,
            "start_cursor": start_cursor,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("data_sources", "list", params)
        # Cast generic envelope to concrete typed result
        return DataSourcesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        data_source_id: str,
        **kwargs
    ) -> DataSource:
        """
        Retrieves a data source object using the ID specified

        Args:
            data_source_id: Data Source ID
            **kwargs: Additional parameters

        Returns:
            DataSource
        """
        params = {k: v for k, v in {
            "data_source_id": data_source_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("data_sources", "get", params)
        return result



    async def update(
        self,
        data_source_id: str,
        title: list[DataSourcesUpdateParamsTitleItem] | None = None,
        description: list[DataSourcesUpdateParamsDescriptionItem] | None = None,
        properties: dict[str, Any] | None = None,
        icon: DataSourcesUpdateParamsIcon | None | None = None,
        cover: DataSourcesUpdateParamsCover | None | None = None,
        archived: bool | None = None,
        in_trash: bool | None = None,
        **kwargs
    ) -> DataSource:
        """
        Updates a data source's title, description, icon, properties, or trash status

        Args:
            title: Updated title of the data source as rich text
            description: Updated description of the data source as rich text
            properties: Data source property schema to update. Keys are property names or IDs. Set a property to null to remove it.
            icon: Icon. Supports emoji, external URL, file upload, custom emoji, and Notion native icons. Set to null to remove.
            cover: Cover image. Supports external URL or file upload. Set to null to remove.
            archived: Set to true to archive the data source
            in_trash: Set to true to move the data source to trash
            data_source_id: Data source ID
            **kwargs: Additional parameters

        Returns:
            DataSource
        """
        params = {k: v for k, v in {
            "title": title,
            "description": description,
            "properties": properties,
            "icon": icon,
            "cover": cover,
            "archived": archived,
            "in_trash": in_trash,
            "data_source_id": data_source_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("data_sources", "update", params)
        return result



    async def context_store_search(
        self,
        query: DataSourcesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DataSourcesSearchResult:
        """
        Search data_sources records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DataSourcesSearchFilter):
        - archived: Indicates if the data source is archived or not.
        - cover: URL or reference to the cover image of the data source.
        - created_by: The user who created the data source.
        - created_time: The timestamp when the data source was created.
        - database_parent: The grandparent of the data source (parent of the database).
        - description: Description text associated with the data source.
        - icon: URL or reference to the icon of the data source.
        - id: Unique identifier of the data source.
        - is_inline: Indicates if the data source is displayed inline.
        - last_edited_by: The user who last edited the data source.
        - last_edited_time: The timestamp when the data source was last edited.
        - object_: The type of object (data_source).
        - parent: The parent database of the data source.
        - properties: Schema of properties for the data source.
        - public_url: Public URL to access the data source.
        - title: Title or name of the data source.
        - url: URL or reference to access the data source.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DataSourcesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("data_sources", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DataSourcesSearchResult(
            data=[
                DataSourcesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class BlocksQuery:
    """
    Query class for Blocks entity operations.
    """

    def __init__(self, connector: NotionConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        block_id: str,
        start_cursor: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> BlocksListResult:
        """
        Returns a paginated list of child blocks for the specified block

        Args:
            block_id: Block or page ID
            start_cursor: Pagination cursor for next page
            page_size: Number of items per page (max 100)
            **kwargs: Additional parameters

        Returns:
            BlocksListResult
        """
        params = {k: v for k, v in {
            "block_id": block_id,
            "start_cursor": start_cursor,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("blocks", "list", params)
        # Cast generic envelope to concrete typed result
        return BlocksListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        children: list[BlocksCreateParamsChildrenItem],
        block_id: str,
        **kwargs
    ) -> list[Block]:
        """
        Creates and appends new children blocks to the specified parent block or page

        Args:
            children: Array of block objects to append (max 100). Each block must specify a type and corresponding content.
            block_id: Block or page ID to append children to
            **kwargs: Additional parameters

        Returns:
            list[Block]
        """
        params = {k: v for k, v in {
            "children": children,
            "block_id": block_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("blocks", "create", params)
        return result



    async def get(
        self,
        block_id: str,
        **kwargs
    ) -> Block:
        """
        Retrieves a block object using the ID specified

        Args:
            block_id: Block ID
            **kwargs: Additional parameters

        Returns:
            Block
        """
        params = {k: v for k, v in {
            "block_id": block_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("blocks", "get", params)
        return result



    async def update(
        self,
        block_id: str,
        paragraph: BlocksUpdateParamsParagraph | None = None,
        heading_1: BlocksUpdateParamsHeading1 | None = None,
        heading_2: BlocksUpdateParamsHeading2 | None = None,
        heading_3: BlocksUpdateParamsHeading3 | None = None,
        bulleted_list_item: BlocksUpdateParamsBulletedListItem | None = None,
        numbered_list_item: BlocksUpdateParamsNumberedListItem | None = None,
        to_do: BlocksUpdateParamsToDo | None = None,
        toggle: BlocksUpdateParamsToggle | None = None,
        code: BlocksUpdateParamsCode | None = None,
        quote: BlocksUpdateParamsQuote | None = None,
        callout: BlocksUpdateParamsCallout | None = None,
        bookmark: BlocksUpdateParamsBookmark | None = None,
        embed: BlocksUpdateParamsEmbed | None = None,
        equation: BlocksUpdateParamsEquation | None = None,
        image: BlocksUpdateParamsImage | None = None,
        video: BlocksUpdateParamsVideo | None = None,
        file: BlocksUpdateParamsFile | None = None,
        pdf: BlocksUpdateParamsPdf | None = None,
        audio: BlocksUpdateParamsAudio | None = None,
        table: BlocksUpdateParamsTable | None = None,
        archived: bool | None = None,
        **kwargs
    ) -> Block:
        """
        Updates the content of a block based on its type

        Args:
            paragraph: Updated paragraph content
            heading_1: Updated heading 1 content
            heading_2: Updated heading 2 content
            heading_3: Updated heading 3 content
            bulleted_list_item: Updated bulleted list item
            numbered_list_item: Updated numbered list item
            to_do: Updated to-do content
            toggle: Updated toggle content
            code: Updated code block content
            quote: Updated quote content
            callout: Updated callout content
            bookmark: Updated bookmark
            embed: Updated embed
            equation: Updated equation
            image: Media file. Use external URL or file upload.
            video: Media file. Use external URL or file upload.
            file: Media file. Use external URL or file upload.
            pdf: Media file. Use external URL or file upload.
            audio: Media file. Use external URL or file upload.
            table: Updated table properties
            archived: Set to true to archive the block (API version 2025-09-03)
            block_id: Block ID
            **kwargs: Additional parameters

        Returns:
            Block
        """
        params = {k: v for k, v in {
            "paragraph": paragraph,
            "heading_1": heading_1,
            "heading_2": heading_2,
            "heading_3": heading_3,
            "bulleted_list_item": bulleted_list_item,
            "numbered_list_item": numbered_list_item,
            "to_do": to_do,
            "toggle": toggle,
            "code": code,
            "quote": quote,
            "callout": callout,
            "bookmark": bookmark,
            "embed": embed,
            "equation": equation,
            "image": image,
            "video": video,
            "file": file,
            "pdf": pdf,
            "audio": audio,
            "table": table,
            "archived": archived,
            "block_id": block_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("blocks", "update", params)
        return result



    async def context_store_search(
        self,
        query: BlocksSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BlocksSearchResult:
        """
        Search blocks records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BlocksSearchFilter):
        - archived: Indicates if the block is archived or not.
        - bookmark: Represents a bookmark within the block
        - breadcrumb: Represents a breadcrumb block.
        - bulleted_list_item: Represents an item in a bulleted list.
        - callout: Describes a callout message or content in the block
        - child_database: Represents a child database block.
        - child_page: Represents a child page block.
        - code: Contains code snippets or blocks in the block content
        - column: Represents a column block.
        - column_list: Represents a list of columns.
        - created_by: The user who created the block.
        - created_time: The timestamp when the block was created.
        - divider: Represents a divider block.
        - embed: Contains embedded content such as videos, tweets, etc.
        - equation: Represents an equation or mathematical formula in the block
        - file: Represents a file block.
        - has_children: Indicates if the block has children or not.
        - heading_1: Represents a level 1 heading.
        - heading_2: Represents a level 2 heading.
        - heading_3: Represents a level 3 heading.
        - id: The unique identifier of the block.
        - image: Represents an image block.
        - last_edited_by: The user who last edited the block.
        - last_edited_time: The timestamp when the block was last edited.
        - link_preview: Displays a preview of an external link within the block
        - link_to_page: Provides a link to another page within the block
        - numbered_list_item: Represents an item in a numbered list.
        - object_: Represents an object block.
        - paragraph: Represents a paragraph block.
        - parent: The parent block of the current block.
        - pdf: Represents a PDF document block.
        - quote: Represents a quote block.
        - synced_block: Represents a block synced from another source
        - table: Represents a table within the block
        - table_of_contents: Contains information regarding the table of contents
        - table_row: Represents a row in a table within the block
        - template: Specifies a template used within the block
        - to_do: Represents a to-do list or task content
        - toggle: Represents a toggle block.
        - type_: The type of the block.
        - unsupported: Represents an unsupported block.
        - video: Represents a video block.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BlocksSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("blocks", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return BlocksSearchResult(
            data=[
                BlocksSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CommentsQuery:
    """
    Query class for Comments entity operations.
    """

    def __init__(self, connector: NotionConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        block_id: str,
        start_cursor: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> CommentsListResult:
        """
        Returns a list of comments for a specified block or page

        Args:
            block_id: Block or page ID to retrieve comments for
            start_cursor: Pagination cursor for next page
            page_size: Number of items per page (max 100)
            **kwargs: Additional parameters

        Returns:
            CommentsListResult
        """
        params = {k: v for k, v in {
            "block_id": block_id,
            "start_cursor": start_cursor,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "list", params)
        # Cast generic envelope to concrete typed result
        return CommentsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def create(
        self,
        rich_text: list[CommentsCreateParamsRichTextItem],
        parent: dict[str, Any] | None = None,
        discussion_id: str | None = None,
        **kwargs
    ) -> Comment:
        """
        Creates a comment on a page or block, or replies to an existing discussion thread

        Args:
            parent: Parent of the comment. Provide exactly one of page_id or block_id. Mutually exclusive with discussion_id.
            discussion_id: ID of an existing discussion thread to reply to. Mutually exclusive with parent.
            rich_text: Content of the comment as rich text
            **kwargs: Additional parameters

        Returns:
            Comment
        """
        params = {k: v for k, v in {
            "parent": parent,
            "discussion_id": discussion_id,
            "rich_text": rich_text,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("comments", "create", params)
        return result



    async def context_store_search(
        self,
        query: CommentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CommentsSearchResult:
        """
        Search comments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CommentsSearchFilter):
        - created_by: User who created the comment.
        - created_time: Date and time when the comment was created.
        - discussion_id: Discussion thread ID.
        - id: Unique identifier for the comment.
        - last_edited_time: Date and time when the comment was last edited.
        - object_: Always comment.
        - parent: Parent of the comment.
        - rich_text: Content of the comment as rich text.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CommentsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("comments", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CommentsSearchResult(
            data=[
                CommentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
