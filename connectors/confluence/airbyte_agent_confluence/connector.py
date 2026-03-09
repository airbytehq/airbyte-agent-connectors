"""
Confluence connector.
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

from .connector_model import ConfluenceConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AuditListParams,
    BlogPostsGetParams,
    BlogPostsListParams,
    GroupsListParams,
    PagesGetParams,
    PagesListParams,
    SpacesGetParams,
    SpacesListParams,
    AirbyteSearchParams,
    AuditSearchFilter,
    AuditSearchQuery,
    BlogPostsSearchFilter,
    BlogPostsSearchQuery,
    GroupsSearchFilter,
    GroupsSearchQuery,
    PagesSearchFilter,
    PagesSearchQuery,
    SpacesSearchFilter,
    SpacesSearchQuery,
)
from .models import ConfluenceAuthConfig

# Import response models and envelope models at runtime
from .models import (
    ConfluenceCheckResult,
    ConfluenceExecuteResult,
    ConfluenceExecuteResultWithMeta,
    SpacesListResult,
    PagesListResult,
    BlogPostsListResult,
    GroupsListResult,
    AuditListResult,
    AuditRecord,
    BlogPost,
    Group,
    Page,
    Space,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AuditSearchData,
    AuditSearchResult,
    BlogPostsSearchData,
    BlogPostsSearchResult,
    GroupsSearchData,
    GroupsSearchResult,
    PagesSearchData,
    PagesSearchResult,
    SpacesSearchData,
    SpacesSearchResult,
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




class ConfluenceConnector:
    """
    Type-safe Confluence API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "confluence"
    connector_version = "1.0.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("spaces", "list"): True,
        ("spaces", "get"): None,
        ("pages", "list"): True,
        ("pages", "get"): None,
        ("blog_posts", "list"): True,
        ("blog_posts", "get"): None,
        ("groups", "list"): True,
        ("audit", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('spaces', 'list'): {'cursor': 'cursor', 'limit': 'limit', 'type': 'type', 'status': 'status', 'keys': 'keys', 'sort': 'sort'},
        ('spaces', 'get'): {'id': 'id', 'description_format': 'description-format'},
        ('pages', 'list'): {'cursor': 'cursor', 'limit': 'limit', 'space_id': 'space-id', 'title': 'title', 'status': 'status', 'sort': 'sort', 'body_format': 'body-format'},
        ('pages', 'get'): {'id': 'id', 'body_format': 'body-format', 'version': 'version'},
        ('blog_posts', 'list'): {'cursor': 'cursor', 'limit': 'limit', 'space_id': 'space-id', 'title': 'title', 'status': 'status', 'sort': 'sort', 'body_format': 'body-format'},
        ('blog_posts', 'get'): {'id': 'id', 'body_format': 'body-format', 'version': 'version'},
        ('groups', 'list'): {'start': 'start', 'limit': 'limit'},
        ('audit', 'list'): {'start': 'start', 'limit': 'limit', 'start_date': 'startDate', 'end_date': 'endDate', 'search_string': 'searchString'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (ConfluenceAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: ConfluenceAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        subdomain: str | None = None    ):
        """
        Initialize a new confluence connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., ConfluenceAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            subdomain: Your Confluence Cloud subdomain (e.g., mycompany for mycompany.atlassian.net)
        Examples:
            # Local mode (direct API calls)
            connector = ConfluenceConnector(auth_config=ConfluenceAuthConfig(username="...", password="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = ConfluenceConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = ConfluenceConnector(
                auth_config=AirbyteAuthConfig(
                    customer_name="user-123",
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
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                customer_name=auth_config.customer_name,
                organization_id=auth_config.organization_id,
                connector_definition_id=str(ConfluenceConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or ConfluenceAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if subdomain:
                config_values["subdomain"] = subdomain

            self._executor = LocalExecutor(
                model=ConfluenceConnectorModel,
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
        self.spaces = SpacesQuery(self)
        self.pages = PagesQuery(self)
        self.blog_posts = BlogPostsQuery(self)
        self.groups = GroupsQuery(self)
        self.audit = AuditQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["spaces"],
        action: Literal["list"],
        params: "SpacesListParams"
    ) -> "SpacesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["spaces"],
        action: Literal["get"],
        params: "SpacesGetParams"
    ) -> "Space": ...

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
        entity: Literal["blog_posts"],
        action: Literal["list"],
        params: "BlogPostsListParams"
    ) -> "BlogPostsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["blog_posts"],
        action: Literal["get"],
        params: "BlogPostsGetParams"
    ) -> "BlogPost": ...

    @overload
    async def execute(
        self,
        entity: Literal["groups"],
        action: Literal["list"],
        params: "GroupsListParams"
    ) -> "GroupsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["audit"],
        action: Literal["list"],
        params: "AuditListParams"
    ) -> "AuditListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> ConfluenceExecuteResult[Any] | ConfluenceExecuteResultWithMeta[Any, Any] | Any: ...

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
                return ConfluenceExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return ConfluenceExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> ConfluenceCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            ConfluenceCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return ConfluenceCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return ConfluenceCheckResult(
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
            @ConfluenceConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @ConfluenceConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    ConfluenceConnectorModel,
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
        return describe_entities(ConfluenceConnectorModel)

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
            (e for e in ConfluenceConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in ConfluenceConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await ConfluenceConnector.create(...)
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
        auth_config: "ConfluenceAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> "ConfluenceConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + customer_name)
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A ConfluenceConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await ConfluenceConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=ConfluenceAuthConfig(username="...", password="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for create()")


        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient
        from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as _AirbyteAuthConfig

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
            organization_id=airbyte_config.organization_id,
        )

        try:
            # Build credentials from auth_config (if provided)
            credentials = auth_config.model_dump(exclude_none=True) if auth_config else None
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {airbyte_config.customer_name}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(ConfluenceConnectorModel.id),
                customer_name=airbyte_config.customer_name,
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
                organization_id=airbyte_config.organization_id,
                connector_id=source_id,
            ),
        )




class SpacesQuery:
    """
    Query class for Spaces entity operations.
    """

    def __init__(self, connector: ConfluenceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        type: str | None = None,
        status: str | None = None,
        keys: list[str] | None = None,
        sort: str | None = None,
        **kwargs
    ) -> SpacesListResult:
        """
        Returns all spaces. Only spaces that the user has permission to view will be returned.

        Args:
            cursor: Cursor for pagination
            limit: Maximum number of spaces to return
            type: Filter by space type (global or personal)
            status: Filter by space status (current or archived)
            keys: Filter by space keys
            sort: Sort order for results
            **kwargs: Additional parameters

        Returns:
            SpacesListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            "type": type,
            "status": status,
            "keys": keys,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("spaces", "list", params)
        # Cast generic envelope to concrete typed result
        return SpacesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        description_format: str | None = None,
        **kwargs
    ) -> Space:
        """
        Returns a specific space.

        Args:
            id: The ID of the space
            description_format: The format of the space description in the response
            **kwargs: Additional parameters

        Returns:
            Space
        """
        params = {k: v for k, v in {
            "id": id,
            "description-format": description_format,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("spaces", "get", params)
        return result



    async def search(
        self,
        query: SpacesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SpacesSearchResult:
        """
        Search spaces records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SpacesSearchFilter):
        - links: Links related to the space
        - author_id: ID of the user who created the space
        - created_at: Timestamp when the space was created
        - description: Space description in various formats
        - homepage_id: ID of the space homepage
        - icon: Space icon information
        - id: Unique space identifier
        - key: Space key
        - name: Space name
        - status: Space status (current or archived)
        - type_: Space type (global or personal)

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SpacesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("spaces", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SpacesSearchResult(
            data=[
                SpacesSearchData(**row)
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

    def __init__(self, connector: ConfluenceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        space_id: list[int] | None = None,
        title: str | None = None,
        status: list[str] | None = None,
        sort: str | None = None,
        body_format: str | None = None,
        **kwargs
    ) -> PagesListResult:
        """
        Returns all pages. Only pages that the user has permission to view will be returned.

        Args:
            cursor: Cursor for pagination
            limit: Maximum number of pages to return
            space_id: Filter pages by space ID(s)
            title: Filter pages by title (exact match)
            status: Filter pages by status
            sort: Sort order for results
            body_format: The format of the page body in the response
            **kwargs: Additional parameters

        Returns:
            PagesListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            "space-id": space_id,
            "title": title,
            "status": status,
            "sort": sort,
            "body-format": body_format,
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
        id: str | None = None,
        body_format: str | None = None,
        version: int | None = None,
        **kwargs
    ) -> Page:
        """
        Returns a specific page.

        Args:
            id: The ID of the page
            body_format: The format of the page body in the response
            version: Specific version number to retrieve
            **kwargs: Additional parameters

        Returns:
            Page
        """
        params = {k: v for k, v in {
            "id": id,
            "body-format": body_format,
            "version": version,
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
        - links: Links related to the page
        - author_id: ID of the user who created the page
        - body: Page body content
        - created_at: Timestamp when the page was created
        - id: Unique page identifier
        - last_owner_id: ID of the previous page owner
        - owner_id: ID of the current page owner
        - parent_id: ID of the parent page
        - parent_type: Type of the parent (page or space)
        - position: Position of the page among siblings
        - space_id: ID of the space containing this page
        - status: Page status (current, archived, trashed, draft)
        - title: Page title
        - version: Version information

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

class BlogPostsQuery:
    """
    Query class for BlogPosts entity operations.
    """

    def __init__(self, connector: ConfluenceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        cursor: str | None = None,
        limit: int | None = None,
        space_id: list[int] | None = None,
        title: str | None = None,
        status: list[str] | None = None,
        sort: str | None = None,
        body_format: str | None = None,
        **kwargs
    ) -> BlogPostsListResult:
        """
        Returns all blog posts. Only blog posts that the user has permission to view will be returned.

        Args:
            cursor: Cursor for pagination
            limit: Maximum number of blog posts to return
            space_id: Filter blog posts by space ID(s)
            title: Filter blog posts by title (exact match)
            status: Filter blog posts by status
            sort: Sort order for results
            body_format: The format of the blog post body in the response
            **kwargs: Additional parameters

        Returns:
            BlogPostsListResult
        """
        params = {k: v for k, v in {
            "cursor": cursor,
            "limit": limit,
            "space-id": space_id,
            "title": title,
            "status": status,
            "sort": sort,
            "body-format": body_format,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("blog_posts", "list", params)
        # Cast generic envelope to concrete typed result
        return BlogPostsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        body_format: str | None = None,
        version: int | None = None,
        **kwargs
    ) -> BlogPost:
        """
        Returns a specific blog post.

        Args:
            id: The ID of the blog post
            body_format: The format of the blog post body in the response
            version: Specific version number to retrieve
            **kwargs: Additional parameters

        Returns:
            BlogPost
        """
        params = {k: v for k, v in {
            "id": id,
            "body-format": body_format,
            "version": version,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("blog_posts", "get", params)
        return result



    async def search(
        self,
        query: BlogPostsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BlogPostsSearchResult:
        """
        Search blog_posts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BlogPostsSearchFilter):
        - links: Links related to the blog post
        - author_id: ID of the user who created the blog post
        - body: Blog post body content
        - created_at: Timestamp when the blog post was created
        - id: Unique blog post identifier
        - space_id: ID of the space containing this blog post
        - status: Blog post status (current, draft, trashed)
        - title: Blog post title
        - version: Version information

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BlogPostsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("blog_posts", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return BlogPostsSearchResult(
            data=[
                BlogPostsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class GroupsQuery:
    """
    Query class for Groups entity operations.
    """

    def __init__(self, connector: ConfluenceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start: int | None = None,
        limit: int | None = None,
        **kwargs
    ) -> GroupsListResult:
        """
        Returns all user groups.

        Args:
            start: Starting index for pagination
            limit: Maximum number of groups to return
            **kwargs: Additional parameters

        Returns:
            GroupsListResult
        """
        params = {k: v for k, v in {
            "start": start,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("groups", "list", params)
        # Cast generic envelope to concrete typed result
        return GroupsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: GroupsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> GroupsSearchResult:
        """
        Search groups records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (GroupsSearchFilter):
        - links: Links related to the group
        - id: The unique identifier of the group
        - name: The name of the group
        - type_: The type of group

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            GroupsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("groups", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return GroupsSearchResult(
            data=[
                GroupsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AuditQuery:
    """
    Query class for Audit entity operations.
    """

    def __init__(self, connector: ConfluenceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start: int | None = None,
        limit: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        search_string: str | None = None,
        **kwargs
    ) -> AuditListResult:
        """
        Returns audit log records.

        Args:
            start: Starting index for pagination
            limit: Maximum number of audit records to return
            start_date: Start date for filtering audit records (ISO 8601)
            end_date: End date for filtering audit records (ISO 8601)
            search_string: Search string to filter audit records
            **kwargs: Additional parameters

        Returns:
            AuditListResult
        """
        params = {k: v for k, v in {
            "start": start,
            "limit": limit,
            "startDate": start_date,
            "endDate": end_date,
            "searchString": search_string,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("audit", "list", params)
        # Cast generic envelope to concrete typed result
        return AuditListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: AuditSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AuditSearchResult:
        """
        Search audit records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AuditSearchFilter):
        - affected_object: The object that was affected by the audit event.
        - associated_objects: Any associated objects related to the audit event.
        - author: The user who triggered the audit event.
        - category: The category under which the audit event falls.
        - changed_values: Details of the values that were changed during the audit event.
        - creation_date: The date and time when the audit event was created.
        - description: A detailed description of the audit event.
        - remote_address: The IP address from which the audit event originated.
        - summary: A brief summary or title describing the audit event.
        - super_admin: Indicates if the user triggering the audit event is a super admin.
        - sys_admin: Indicates if the user triggering the audit event is a system admin.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AuditSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("audit", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AuditSearchResult(
            data=[
                AuditSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
