"""
Klaviyo connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .connector_model import KlaviyoConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    CampaignsGetParams,
    CampaignsListParams,
    EmailTemplatesGetParams,
    EmailTemplatesListParams,
    EventsListParams,
    FlowsGetParams,
    FlowsListParams,
    ListsGetParams,
    ListsListParams,
    MetricsGetParams,
    MetricsListParams,
    ProfilesGetParams,
    ProfilesListParams,
    AirbyteSearchParams,
    ProfilesSearchFilter,
    ProfilesSearchQuery,
    EventsSearchFilter,
    EventsSearchQuery,
    EmailTemplatesSearchFilter,
    EmailTemplatesSearchQuery,
    CampaignsSearchFilter,
    CampaignsSearchQuery,
    FlowsSearchFilter,
    FlowsSearchQuery,
    MetricsSearchFilter,
    MetricsSearchQuery,
    ListsSearchFilter,
    ListsSearchQuery,
)
if TYPE_CHECKING:
    from .models import KlaviyoAuthConfig

# Import response models and envelope models at runtime
from .models import (
    KlaviyoCheckResult,
    KlaviyoExecuteResult,
    KlaviyoExecuteResultWithMeta,
    ProfilesListResult,
    ListsListResult,
    CampaignsListResult,
    EventsListResult,
    MetricsListResult,
    FlowsListResult,
    EmailTemplatesListResult,
    Campaign,
    Event,
    Flow,
    List,
    Metric,
    Profile,
    Template,
    AirbyteSearchHit,
    AirbyteSearchResult,
    ProfilesSearchData,
    ProfilesSearchResult,
    EventsSearchData,
    EventsSearchResult,
    EmailTemplatesSearchData,
    EmailTemplatesSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    FlowsSearchData,
    FlowsSearchResult,
    MetricsSearchData,
    MetricsSearchResult,
    ListsSearchData,
    ListsSearchResult,
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




class KlaviyoConnector:
    """
    Type-safe Klaviyo API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "klaviyo"
    connector_version = "1.0.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("profiles", "list"): True,
        ("profiles", "get"): None,
        ("lists", "list"): True,
        ("lists", "get"): None,
        ("campaigns", "list"): True,
        ("campaigns", "get"): None,
        ("events", "list"): True,
        ("metrics", "list"): True,
        ("metrics", "get"): None,
        ("flows", "list"): True,
        ("flows", "get"): None,
        ("email_templates", "list"): True,
        ("email_templates", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('profiles', 'list'): {'page_size': 'page[size]', 'page_cursor': 'page[cursor]'},
        ('profiles', 'get'): {'id': 'id'},
        ('lists', 'list'): {'page_size': 'page[size]', 'page_cursor': 'page[cursor]'},
        ('lists', 'get'): {'id': 'id'},
        ('campaigns', 'list'): {'filter': 'filter', 'page_size': 'page[size]', 'page_cursor': 'page[cursor]'},
        ('campaigns', 'get'): {'id': 'id'},
        ('events', 'list'): {'page_size': 'page[size]', 'page_cursor': 'page[cursor]', 'sort': 'sort'},
        ('metrics', 'list'): {'page_size': 'page[size]', 'page_cursor': 'page[cursor]'},
        ('metrics', 'get'): {'id': 'id'},
        ('flows', 'list'): {'page_size': 'page[size]', 'page_cursor': 'page[cursor]'},
        ('flows', 'get'): {'id': 'id'},
        ('email_templates', 'list'): {'page_size': 'page[size]', 'page_cursor': 'page[cursor]'},
        ('email_templates', 'get'): {'id': 'id'},
    }

    def __init__(
        self,
        auth_config: KlaviyoAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        connector_id: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new klaviyo connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide Airbyte credentials with either `connector_id` or `external_user_id`

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            external_user_id: External user ID (for hosted mode lookup)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            connector_id: Specific connector/source ID (for hosted mode, skips lookup)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = KlaviyoConnector(auth_config=KlaviyoAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = KlaviyoConnector(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid"
            )

            # Hosted mode with lookup by external_user_id
            connector = KlaviyoConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = KlaviyoConnector(
                auth_config=KlaviyoAuthConfig(access_token="...", refresh_token="..."),
                on_token_refresh=save_tokens
            )
        """
        # Hosted mode: Airbyte credentials + either connector_id OR external_user_id
        is_hosted = airbyte_client_id and airbyte_client_secret and (connector_id or external_user_id)

        if is_hosted:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                connector_id=connector_id,
                external_user_id=external_user_id,
                connector_definition_id=str(KlaviyoConnectorModel.id) if not connector_id else None,
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide Airbyte credentials (airbyte_client_id, airbyte_client_secret) with "
                    "connector_id or external_user_id for hosted mode, or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=KlaviyoConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.profiles = ProfilesQuery(self)
        self.lists = ListsQuery(self)
        self.campaigns = CampaignsQuery(self)
        self.events = EventsQuery(self)
        self.metrics = MetricsQuery(self)
        self.flows = FlowsQuery(self)
        self.email_templates = EmailTemplatesQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["profiles"],
        action: Literal["list"],
        params: "ProfilesListParams"
    ) -> "ProfilesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["profiles"],
        action: Literal["get"],
        params: "ProfilesGetParams"
    ) -> "Profile": ...

    @overload
    async def execute(
        self,
        entity: Literal["lists"],
        action: Literal["list"],
        params: "ListsListParams"
    ) -> "ListsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["lists"],
        action: Literal["get"],
        params: "ListsGetParams"
    ) -> "List": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["list"],
        params: "CampaignsListParams"
    ) -> "CampaignsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["get"],
        params: "CampaignsGetParams"
    ) -> "Campaign": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["list"],
        params: "EventsListParams"
    ) -> "EventsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metrics"],
        action: Literal["list"],
        params: "MetricsListParams"
    ) -> "MetricsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metrics"],
        action: Literal["get"],
        params: "MetricsGetParams"
    ) -> "Metric": ...

    @overload
    async def execute(
        self,
        entity: Literal["flows"],
        action: Literal["list"],
        params: "FlowsListParams"
    ) -> "FlowsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["flows"],
        action: Literal["get"],
        params: "FlowsGetParams"
    ) -> "Flow": ...

    @overload
    async def execute(
        self,
        entity: Literal["email_templates"],
        action: Literal["list"],
        params: "EmailTemplatesListParams"
    ) -> "EmailTemplatesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["email_templates"],
        action: Literal["get"],
        params: "EmailTemplatesGetParams"
    ) -> "Template": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> KlaviyoExecuteResult[Any] | KlaviyoExecuteResultWithMeta[Any, Any] | Any: ...

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
                return KlaviyoExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return KlaviyoExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> KlaviyoCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            KlaviyoCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return KlaviyoCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return KlaviyoCheckResult(
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
            @KlaviyoConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @KlaviyoConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    KlaviyoConnectorModel,
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
        return describe_entities(KlaviyoConnectorModel)

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
            (e for e in KlaviyoConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in KlaviyoConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await KlaviyoConnector.create_hosted(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def create_hosted(
        cls,
        *,
        external_user_id: str,
        airbyte_client_id: str,
        airbyte_client_secret: str,
        auth_config: "KlaviyoAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
    ) -> "KlaviyoConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            external_user_id: Workspace identifier in Airbyte Cloud
            airbyte_client_id: Airbyte OAuth client ID
            airbyte_client_secret: Airbyte OAuth client secret
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + external_user_id)
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).

        Returns:
            A KlaviyoConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await KlaviyoConnector.create_hosted(
                external_user_id="my-workspace",
                airbyte_client_id="client_abc",
                airbyte_client_secret="secret_xyz",
                auth_config=KlaviyoAuthConfig(api_key="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient

        client = AirbyteCloudClient(
            client_id=airbyte_client_id,
            client_secret=airbyte_client_secret,
        )

        try:
            # Build credentials from auth_config
            credentials = auth_config.model_dump(exclude_none=True)
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {external_user_id}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(KlaviyoConnectorModel.id),
                external_user_id=external_user_id,
                credentials=credentials,
                replication_config=replication_config_dict,
            )
        finally:
            await client.close()

        # Return connector configured with the new connector_id
        return cls(
            airbyte_client_id=airbyte_client_id,
            airbyte_client_secret=airbyte_client_secret,
            connector_id=source_id,
        )



class ProfilesQuery:
    """
    Query class for Profiles entity operations.
    """

    def __init__(self, connector: KlaviyoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        page_cursor: str | None = None,
        **kwargs
    ) -> ProfilesListResult:
        """
        Returns a paginated list of profiles (contacts) in your Klaviyo account

        Args:
            page_size: Number of results per page (max 100)
            page_cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            ProfilesListResult
        """
        params = {k: v for k, v in {
            "page[size]": page_size,
            "page[cursor]": page_cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("profiles", "list", params)
        # Cast generic envelope to concrete typed result
        return ProfilesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Profile:
        """
        Get a single profile by ID

        Args:
            id: Profile ID
            **kwargs: Additional parameters

        Returns:
            Profile
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("profiles", "get", params)
        return result



    async def search(
        self,
        query: ProfilesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProfilesSearchResult:
        """
        Search profiles records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProfilesSearchFilter):
        - attributes: 
        - id: 
        - links: 
        - relationships: 
        - segments: 
        - type: 
        - updated: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProfilesSearchResult with hits (list of AirbyteSearchHit[ProfilesSearchData]) and pagination info

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

        result = await self._connector.execute("profiles", "search", params)

        # Parse response into typed result
        return ProfilesSearchResult(
            hits=[
                AirbyteSearchHit[ProfilesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ProfilesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class ListsQuery:
    """
    Query class for Lists entity operations.
    """

    def __init__(self, connector: KlaviyoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        page_cursor: str | None = None,
        **kwargs
    ) -> ListsListResult:
        """
        Returns a paginated list of all lists in your Klaviyo account

        Args:
            page_size: Number of results per page (max 100)
            page_cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            ListsListResult
        """
        params = {k: v for k, v in {
            "page[size]": page_size,
            "page[cursor]": page_cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("lists", "list", params)
        # Cast generic envelope to concrete typed result
        return ListsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> List:
        """
        Get a single list by ID

        Args:
            id: List ID
            **kwargs: Additional parameters

        Returns:
            List
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("lists", "get", params)
        return result



    async def search(
        self,
        query: ListsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ListsSearchResult:
        """
        Search lists records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ListsSearchFilter):
        - attributes: 
        - id: 
        - links: 
        - relationships: 
        - type: 
        - updated: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ListsSearchResult with hits (list of AirbyteSearchHit[ListsSearchData]) and pagination info

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

        result = await self._connector.execute("lists", "search", params)

        # Parse response into typed result
        return ListsSearchResult(
            hits=[
                AirbyteSearchHit[ListsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ListsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class CampaignsQuery:
    """
    Query class for Campaigns entity operations.
    """

    def __init__(self, connector: KlaviyoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        filter: str,
        page_size: int | None = None,
        page_cursor: str | None = None,
        **kwargs
    ) -> CampaignsListResult:
        """
        Returns a paginated list of campaigns. A channel filter is required.

        Args:
            filter: Filter by channel (email or sms)
            page_size: Number of results per page (max 100)
            page_cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "filter": filter,
            "page[size]": page_size,
            "page[cursor]": page_cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Campaign:
        """
        Get a single campaign by ID

        Args:
            id: Campaign ID
            **kwargs: Additional parameters

        Returns:
            Campaign
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "get", params)
        return result



    async def search(
        self,
        query: CampaignsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CampaignsSearchResult:
        """
        Search campaigns records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CampaignsSearchFilter):
        - attributes: 
        - id: 
        - links: 
        - relationships: 
        - type: 
        - updated_at: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CampaignsSearchResult with hits (list of AirbyteSearchHit[CampaignsSearchData]) and pagination info

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

        result = await self._connector.execute("campaigns", "search", params)

        # Parse response into typed result
        return CampaignsSearchResult(
            hits=[
                AirbyteSearchHit[CampaignsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=CampaignsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class EventsQuery:
    """
    Query class for Events entity operations.
    """

    def __init__(self, connector: KlaviyoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        page_cursor: str | None = None,
        sort: str | None = None,
        **kwargs
    ) -> EventsListResult:
        """
        Returns a paginated list of events (actions taken by profiles)

        Args:
            page_size: Number of results per page (max 100)
            page_cursor: Cursor for pagination
            sort: Sort order for events
            **kwargs: Additional parameters

        Returns:
            EventsListResult
        """
        params = {k: v for k, v in {
            "page[size]": page_size,
            "page[cursor]": page_cursor,
            "sort": sort,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "list", params)
        # Cast generic envelope to concrete typed result
        return EventsListResult(
            data=result.data
        )



    async def search(
        self,
        query: EventsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> EventsSearchResult:
        """
        Search events records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (EventsSearchFilter):
        - attributes: 
        - datetime: 
        - id: 
        - links: 
        - relationships: 
        - type: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            EventsSearchResult with hits (list of AirbyteSearchHit[EventsSearchData]) and pagination info

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

        result = await self._connector.execute("events", "search", params)

        # Parse response into typed result
        return EventsSearchResult(
            hits=[
                AirbyteSearchHit[EventsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=EventsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class MetricsQuery:
    """
    Query class for Metrics entity operations.
    """

    def __init__(self, connector: KlaviyoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        page_cursor: str | None = None,
        **kwargs
    ) -> MetricsListResult:
        """
        Returns a paginated list of metrics (event types)

        Args:
            page_size: Number of results per page (max 100)
            page_cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            MetricsListResult
        """
        params = {k: v for k, v in {
            "page[size]": page_size,
            "page[cursor]": page_cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metrics", "list", params)
        # Cast generic envelope to concrete typed result
        return MetricsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Metric:
        """
        Get a single metric by ID

        Args:
            id: Metric ID
            **kwargs: Additional parameters

        Returns:
            Metric
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metrics", "get", params)
        return result



    async def search(
        self,
        query: MetricsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetricsSearchResult:
        """
        Search metrics records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetricsSearchFilter):
        - attributes: 
        - id: 
        - links: 
        - relationships: 
        - type: 
        - updated: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetricsSearchResult with hits (list of AirbyteSearchHit[MetricsSearchData]) and pagination info

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

        result = await self._connector.execute("metrics", "search", params)

        # Parse response into typed result
        return MetricsSearchResult(
            hits=[
                AirbyteSearchHit[MetricsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=MetricsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class FlowsQuery:
    """
    Query class for Flows entity operations.
    """

    def __init__(self, connector: KlaviyoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        page_cursor: str | None = None,
        **kwargs
    ) -> FlowsListResult:
        """
        Returns a paginated list of flows (automated sequences)

        Args:
            page_size: Number of results per page (max 100)
            page_cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            FlowsListResult
        """
        params = {k: v for k, v in {
            "page[size]": page_size,
            "page[cursor]": page_cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("flows", "list", params)
        # Cast generic envelope to concrete typed result
        return FlowsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Flow:
        """
        Get a single flow by ID

        Args:
            id: Flow ID
            **kwargs: Additional parameters

        Returns:
            Flow
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("flows", "get", params)
        return result



    async def search(
        self,
        query: FlowsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> FlowsSearchResult:
        """
        Search flows records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (FlowsSearchFilter):
        - attributes: 
        - id: 
        - links: 
        - relationships: 
        - type: 
        - updated: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            FlowsSearchResult with hits (list of AirbyteSearchHit[FlowsSearchData]) and pagination info

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

        result = await self._connector.execute("flows", "search", params)

        # Parse response into typed result
        return FlowsSearchResult(
            hits=[
                AirbyteSearchHit[FlowsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=FlowsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class EmailTemplatesQuery:
    """
    Query class for EmailTemplates entity operations.
    """

    def __init__(self, connector: KlaviyoConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        page_cursor: str | None = None,
        **kwargs
    ) -> EmailTemplatesListResult:
        """
        Returns a paginated list of email templates

        Args:
            page_size: Number of results per page (max 100)
            page_cursor: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            EmailTemplatesListResult
        """
        params = {k: v for k, v in {
            "page[size]": page_size,
            "page[cursor]": page_cursor,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("email_templates", "list", params)
        # Cast generic envelope to concrete typed result
        return EmailTemplatesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Template:
        """
        Get a single email template by ID

        Args:
            id: Template ID
            **kwargs: Additional parameters

        Returns:
            Template
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("email_templates", "get", params)
        return result



    async def search(
        self,
        query: EmailTemplatesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> EmailTemplatesSearchResult:
        """
        Search email_templates records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (EmailTemplatesSearchFilter):
        - attributes: 
        - id: 
        - links: 
        - type: 
        - updated: 

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            EmailTemplatesSearchResult with hits (list of AirbyteSearchHit[EmailTemplatesSearchData]) and pagination info

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

        result = await self._connector.execute("email_templates", "search", params)

        # Parse response into typed result
        return EmailTemplatesSearchResult(
            hits=[
                AirbyteSearchHit[EmailTemplatesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=EmailTemplatesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )
