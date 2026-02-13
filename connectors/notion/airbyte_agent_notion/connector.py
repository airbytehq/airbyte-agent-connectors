"""
Notion connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import NotionConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    BlocksGetParams,
    BlocksListParams,
    CommentsListParams,
    DataSourcesGetParams,
    DataSourcesListParams,
    DataSourcesListParamsFilter,
    DataSourcesListParamsSort,
    PagesGetParams,
    PagesListParams,
    PagesListParamsFilter,
    PagesListParamsSort,
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
)
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
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])

DEFAULT_MAX_OUTPUT_CHARS = 50_000  # ~50KB default, configurable per-tool


def _raise_output_too_large(message: str) -> None:
    try:
        from pydantic_ai import ModelRetry  # type: ignore[import-not-found]
    except Exception as exc:
        raise RuntimeError(message) from exc
    raise ModelRetry(message)


def _check_output_size(result: Any, max_chars: int | None, tool_name: str) -> Any:
    if max_chars is None or max_chars <= 0:
        return result

    try:
        serialized = json.dumps(result, default=str)
    except (TypeError, ValueError):
        return result

    if len(serialized) > max_chars:
        truncated_preview = serialized[:500] + "..." if len(serialized) > 500 else serialized
        _raise_output_too_large(
            f"Tool '{tool_name}' output too large ({len(serialized):,} chars, limit {max_chars:,}). "
            "Please narrow your query by: using the 'fields' parameter to select only needed fields, "
            "adding filters, or reducing the 'limit'. "
            f"Preview: {truncated_preview}"
        )

    return result




class NotionConnector:
    """
    Type-safe Notion API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "notion"
    connector_version = "0.1.2"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("users", "list"): True,
        ("users", "get"): None,
        ("pages", "list"): True,
        ("pages", "get"): None,
        ("data_sources", "list"): True,
        ("data_sources", "get"): None,
        ("blocks", "list"): True,
        ("blocks", "get"): None,
        ("comments", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('users', 'list'): {'start_cursor': 'start_cursor', 'page_size': 'page_size'},
        ('users', 'get'): {'user_id': 'user_id'},
        ('pages', 'list'): {'filter': 'filter', 'sort': 'sort', 'start_cursor': 'start_cursor', 'page_size': 'page_size'},
        ('pages', 'get'): {'page_id': 'page_id'},
        ('data_sources', 'list'): {'filter': 'filter', 'sort': 'sort', 'start_cursor': 'start_cursor', 'page_size': 'page_size'},
        ('data_sources', 'get'): {'data_source_id': 'data_source_id'},
        ('blocks', 'list'): {'block_id': 'block_id', 'start_cursor': 'start_cursor', 'page_size': 'page_size'},
        ('blocks', 'get'): {'block_id': 'block_id'},
        ('comments', 'list'): {'block_id': 'block_id', 'start_cursor': 'start_cursor', 'page_size': 'page_size'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (NotionAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: NotionAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new notion connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., NotionAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `external_user_id`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = NotionConnector(auth_config=NotionAuthConfig(token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = NotionConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by external_user_id
            connector = NotionConnector(
                auth_config=AirbyteAuthConfig(
                    external_user_id="user-123",
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
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                external_user_id=auth_config.external_user_id,
                connector_definition_id=str(NotionConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or NotionAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=NotionConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
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
        params: "UsersListParams"
    ) -> "UsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["get"],
        params: "UsersGetParams"
    ) -> "User": ...

    @overload
    async def execute(
        self,
        entity: Literal["pages"],
        action: Literal["list"],
        params: "PagesListParams"
    ) -> "PagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["pages"],
        action: Literal["get"],
        params: "PagesGetParams"
    ) -> "Page": ...

    @overload
    async def execute(
        self,
        entity: Literal["data_sources"],
        action: Literal["list"],
        params: "DataSourcesListParams"
    ) -> "DataSourcesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["data_sources"],
        action: Literal["get"],
        params: "DataSourcesGetParams"
    ) -> "DataSource": ...

    @overload
    async def execute(
        self,
        entity: Literal["blocks"],
        action: Literal["list"],
        params: "BlocksListParams"
    ) -> "BlocksListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["blocks"],
        action: Literal["get"],
        params: "BlocksGetParams"
    ) -> "Block": ...

    @overload
    async def execute(
        self,
        entity: Literal["comments"],
        action: Literal["list"],
        params: "CommentsListParams"
    ) -> "CommentsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> NotionExecuteResult[Any] | NotionExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any] | None = None
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

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from ._vendored.connector_sdk.executor import ExecutionConfig

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
            params=resolved_params
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
        enable_hosted_mode_features: bool = True,
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
    ) -> _F | Callable[[_F], _F]:
        """
        Decorator that adds tool utilities like docstring augmentation and output limits.

        Usage:
            @mcp.tool()
            @NotionConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @NotionConnector.tool_utils(update_docstring=False, max_output_chars=None)
            async def execute(entity: str, action: str, params: dict):
                ...

        Args:
            update_docstring: When True, append connector capabilities to __doc__.
            enable_hosted_mode_features: When False, omit hosted-mode search sections from docstrings.
            max_output_chars: Max serialized output size before raising. Use None to disable.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    NotionConnectorModel,
                    enable_hosted_mode_features=enable_hosted_mode_features,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            if inspect.iscoroutinefunction(inner):

                @wraps(inner)
                async def aw(*args: Any, **kwargs: Any) -> Any:
                    result = await inner(*args, **kwargs)
                    return _check_output_size(result, max_output_chars, inner.__name__)

                wrapped = aw
            else:

                @wraps(inner)
                def sw(*args: Any, **kwargs: Any) -> Any:
                    result = inner(*args, **kwargs)
                    return _check_output_size(result, max_output_chars, inner.__name__)

                wrapped = sw

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

        Example:
            connector = await NotionConnector.create(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def create(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        auth_config: "NotionAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> "NotionConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and external_user_id.
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + external_user_id)
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A NotionConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await NotionConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    external_user_id="my-workspace",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=NotionAuthConfig(token="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.external_user_id:
            raise ValueError("airbyte_config.external_user_id is required for create()")


        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient
        from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as _AirbyteAuthConfig

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
        )

        try:
            # Build credentials from auth_config (if provided)
            credentials = auth_config.model_dump(exclude_none=True) if auth_config else None
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {airbyte_config.external_user_id}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(NotionConnectorModel.id),
                external_user_id=airbyte_config.external_user_id,
                credentials=credentials,
                replication_config=replication_config_dict,
                source_template_id=source_template_id,
            )
        finally:
            await client.close()

        # Return connector configured with the new connector_id
        return cls(
            auth_config=_AirbyteAuthConfig(
                airbyte_client_id=airbyte_config.airbyte_client_id,
                airbyte_client_secret=airbyte_config.airbyte_client_secret,
                connector_id=source_id,
            ),
        )




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
            meta=result.meta
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



    async def search(
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
        - object: Always user
        - person: Person-specific data
        - type: Type of user (person or bot)

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

        result = await self._connector.execute("users", "search", params)

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
            meta=result.meta
        )



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



    async def search(
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
        - object: Type or category of the page object.
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

        result = await self._connector.execute("pages", "search", params)

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
            meta=result.meta
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



    async def search(
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
        - object: The type of object (data_source).
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

        result = await self._connector.execute("data_sources", "search", params)

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
            meta=result.meta
        )



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



    async def search(
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
        - object: Represents an object block.
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
        - type: The type of the block.
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

        result = await self._connector.execute("blocks", "search", params)

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
            meta=result.meta
        )


