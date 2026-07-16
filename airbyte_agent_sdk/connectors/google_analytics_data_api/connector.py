"""
Google-Analytics-Data-Api connector.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import GoogleAnalyticsDataApiConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    DailyActiveUsersListParams,
    DailyActiveUsersListParamsDaterangesItem,
    DailyActiveUsersListParamsDimensionsItem,
    DailyActiveUsersListParamsMetricsItem,
    DevicesListParams,
    DevicesListParamsDaterangesItem,
    DevicesListParamsDimensionsItem,
    DevicesListParamsMetricsItem,
    FourWeeklyActiveUsersListParams,
    FourWeeklyActiveUsersListParamsDaterangesItem,
    FourWeeklyActiveUsersListParamsDimensionsItem,
    FourWeeklyActiveUsersListParamsMetricsItem,
    LocationsListParams,
    LocationsListParamsDaterangesItem,
    LocationsListParamsDimensionsItem,
    LocationsListParamsMetricsItem,
    PagesListParams,
    PagesListParamsDaterangesItem,
    PagesListParamsDimensionsItem,
    PagesListParamsMetricsItem,
    TrafficSourcesListParams,
    TrafficSourcesListParamsDaterangesItem,
    TrafficSourcesListParamsDimensionsItem,
    TrafficSourcesListParamsMetricsItem,
    WebsiteOverviewListParams,
    WebsiteOverviewListParamsDaterangesItem,
    WebsiteOverviewListParamsDimensionsItem,
    WebsiteOverviewListParamsMetricsItem,
    WeeklyActiveUsersListParams,
    WeeklyActiveUsersListParamsDaterangesItem,
    WeeklyActiveUsersListParamsDimensionsItem,
    WeeklyActiveUsersListParamsMetricsItem,
    AirbyteSearchParams,
    WebsiteOverviewSearchFilter,
    WebsiteOverviewSearchQuery,
    DailyActiveUsersSearchFilter,
    DailyActiveUsersSearchQuery,
    WeeklyActiveUsersSearchFilter,
    WeeklyActiveUsersSearchQuery,
    FourWeeklyActiveUsersSearchFilter,
    FourWeeklyActiveUsersSearchQuery,
    TrafficSourcesSearchFilter,
    TrafficSourcesSearchQuery,
    PagesSearchFilter,
    PagesSearchQuery,
    DevicesSearchFilter,
    DevicesSearchQuery,
    LocationsSearchFilter,
    LocationsSearchQuery,
)
from .models import GoogleAnalyticsDataApiAuthConfig
if TYPE_CHECKING:
    from .models import GoogleAnalyticsDataApiReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    GoogleAnalyticsDataApiCheckResult,
    GoogleAnalyticsDataApiExecuteResult,
    GoogleAnalyticsDataApiExecuteResultWithMeta,
    WebsiteOverviewListResult,
    DailyActiveUsersListResult,
    WeeklyActiveUsersListResult,
    FourWeeklyActiveUsersListResult,
    TrafficSourcesListResult,
    PagesListResult,
    DevicesListResult,
    LocationsListResult,
    Row,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    WebsiteOverviewSearchData,
    WebsiteOverviewSearchResult,
    DailyActiveUsersSearchData,
    DailyActiveUsersSearchResult,
    WeeklyActiveUsersSearchData,
    WeeklyActiveUsersSearchResult,
    FourWeeklyActiveUsersSearchData,
    FourWeeklyActiveUsersSearchResult,
    TrafficSourcesSearchData,
    TrafficSourcesSearchResult,
    PagesSearchData,
    PagesSearchResult,
    DevicesSearchData,
    DevicesSearchResult,
    LocationsSearchData,
    LocationsSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class GoogleAnalyticsDataApiConnector:
    """
    Type-safe Google-Analytics-Data-Api API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "google-analytics-data-api"
    connector_version = "1.0.5"
    sdk_version = "0.1.287"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("website_overview", "list"): True,
        ("daily_active_users", "list"): True,
        ("weekly_active_users", "list"): True,
        ("four_weekly_active_users", "list"): True,
        ("traffic_sources", "list"): True,
        ("pages", "list"): True,
        ("devices", "list"): True,
        ("locations", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('website_overview', 'list'): {'date_ranges': 'dateRanges', 'dimensions': 'dimensions', 'metrics': 'metrics', 'keep_empty_rows': 'keepEmptyRows', 'return_property_quota': 'returnPropertyQuota', 'limit': 'limit', 'property_id': 'property_id'},
        ('daily_active_users', 'list'): {'date_ranges': 'dateRanges', 'dimensions': 'dimensions', 'metrics': 'metrics', 'keep_empty_rows': 'keepEmptyRows', 'return_property_quota': 'returnPropertyQuota', 'limit': 'limit', 'property_id': 'property_id'},
        ('weekly_active_users', 'list'): {'date_ranges': 'dateRanges', 'dimensions': 'dimensions', 'metrics': 'metrics', 'keep_empty_rows': 'keepEmptyRows', 'return_property_quota': 'returnPropertyQuota', 'limit': 'limit', 'property_id': 'property_id'},
        ('four_weekly_active_users', 'list'): {'date_ranges': 'dateRanges', 'dimensions': 'dimensions', 'metrics': 'metrics', 'keep_empty_rows': 'keepEmptyRows', 'return_property_quota': 'returnPropertyQuota', 'limit': 'limit', 'property_id': 'property_id'},
        ('traffic_sources', 'list'): {'date_ranges': 'dateRanges', 'dimensions': 'dimensions', 'metrics': 'metrics', 'keep_empty_rows': 'keepEmptyRows', 'return_property_quota': 'returnPropertyQuota', 'limit': 'limit', 'property_id': 'property_id'},
        ('pages', 'list'): {'date_ranges': 'dateRanges', 'dimensions': 'dimensions', 'metrics': 'metrics', 'keep_empty_rows': 'keepEmptyRows', 'return_property_quota': 'returnPropertyQuota', 'limit': 'limit', 'property_id': 'property_id'},
        ('devices', 'list'): {'date_ranges': 'dateRanges', 'dimensions': 'dimensions', 'metrics': 'metrics', 'keep_empty_rows': 'keepEmptyRows', 'return_property_quota': 'returnPropertyQuota', 'limit': 'limit', 'property_id': 'property_id'},
        ('locations', 'list'): {'date_ranges': 'dateRanges', 'dimensions': 'dimensions', 'metrics': 'metrics', 'keep_empty_rows': 'keepEmptyRows', 'return_property_quota': 'returnPropertyQuota', 'limit': 'limit', 'property_id': 'property_id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (GoogleAnalyticsDataApiAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: GoogleAnalyticsDataApiAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new google-analytics-data-api connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., GoogleAnalyticsDataApiAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = GoogleAnalyticsDataApiConnector(auth_config=GoogleAnalyticsDataApiAuthConfig(client_id="...", client_secret="...", refresh_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = GoogleAnalyticsDataApiConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = GoogleAnalyticsDataApiConnector(
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
                connector_definition_id=str(GoogleAnalyticsDataApiConnectorModel.id),
                model=GoogleAnalyticsDataApiConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or GoogleAnalyticsDataApiAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=GoogleAnalyticsDataApiConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.website_overview = WebsiteOverviewQuery(self)
        self.daily_active_users = DailyActiveUsersQuery(self)
        self.weekly_active_users = WeeklyActiveUsersQuery(self)
        self.four_weekly_active_users = FourWeeklyActiveUsersQuery(self)
        self.traffic_sources = TrafficSourcesQuery(self)
        self.pages = PagesQuery(self)
        self.devices = DevicesQuery(self)
        self.locations = LocationsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["website_overview"],
        action: Literal["list"],
        params: "WebsiteOverviewListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "WebsiteOverviewListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["daily_active_users"],
        action: Literal["list"],
        params: "DailyActiveUsersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DailyActiveUsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["weekly_active_users"],
        action: Literal["list"],
        params: "WeeklyActiveUsersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "WeeklyActiveUsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["four_weekly_active_users"],
        action: Literal["list"],
        params: "FourWeeklyActiveUsersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "FourWeeklyActiveUsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["traffic_sources"],
        action: Literal["list"],
        params: "TrafficSourcesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TrafficSourcesListResult": ...

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
        entity: Literal["devices"],
        action: Literal["list"],
        params: "DevicesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DevicesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["locations"],
        action: Literal["list"],
        params: "LocationsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "LocationsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "context_store_search"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> GoogleAnalyticsDataApiExecuteResult[Any] | GoogleAnalyticsDataApiExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "context_store_search"],
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
                return GoogleAnalyticsDataApiExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GoogleAnalyticsDataApiExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> GoogleAnalyticsDataApiCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            GoogleAnalyticsDataApiCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return GoogleAnalyticsDataApiCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return GoogleAnalyticsDataApiCheckResult(
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

        connector = GoogleAnalyticsDataApiConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @GoogleAnalyticsDataApiConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @GoogleAnalyticsDataApiConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @GoogleAnalyticsDataApiConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
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
                    GoogleAnalyticsDataApiConnectorModel,
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
        return describe_entities(GoogleAnalyticsDataApiConnectorModel)

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
            (e for e in GoogleAnalyticsDataApiConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in GoogleAnalyticsDataApiConnectorModel.entities]}"
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



class WebsiteOverviewQuery:
    """
    Query class for WebsiteOverview entity operations.
    """

    def __init__(self, connector: GoogleAnalyticsDataApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        property_id: str,
        date_ranges: list[WebsiteOverviewListParamsDaterangesItem] | None = None,
        dimensions: list[WebsiteOverviewListParamsDimensionsItem] | None = None,
        metrics: list[WebsiteOverviewListParamsMetricsItem] | None = None,
        keep_empty_rows: bool | None = None,
        return_property_quota: bool | None = None,
        limit: int | None = None,
        **kwargs
    ) -> WebsiteOverviewListResult:
        """
        Returns website overview metrics including total users, new users, sessions, bounce rate, page views, and average session duration by date.

        Args:
            date_ranges: Parameter dateRanges
            dimensions: Parameter dimensions
            metrics: Parameter metrics
            keep_empty_rows: Parameter keepEmptyRows
            return_property_quota: Parameter returnPropertyQuota
            limit: Parameter limit
            property_id: GA4 property ID
            **kwargs: Additional parameters

        Returns:
            WebsiteOverviewListResult
        """
        params = {k: v for k, v in {
            "dateRanges": date_ranges,
            "dimensions": dimensions,
            "metrics": metrics,
            "keepEmptyRows": keep_empty_rows,
            "returnPropertyQuota": return_property_quota,
            "limit": limit,
            "property_id": property_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("website_overview", "list", params)
        # Cast generic envelope to concrete typed result
        return WebsiteOverviewListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: WebsiteOverviewSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> WebsiteOverviewSearchResult:
        """
        Search website_overview records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (WebsiteOverviewSearchFilter):
        - average_session_duration: Average duration of sessions in seconds
        - bounce_rate: Percentage of sessions that were single-page with no interaction
        - date: Date of the report row in YYYYMMDD format
        - end_date: End date of the reporting period
        - new_users: Number of first-time users
        - property_id: GA4 property ID
        - screen_page_views: Total number of screen or page views
        - screen_page_views_per_session: Average page views per session
        - sessions: Total number of sessions
        - sessions_per_user: Average number of sessions per user
        - start_date: Start date of the reporting period
        - total_users: Total number of unique users

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            WebsiteOverviewSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("website_overview", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return WebsiteOverviewSearchResult(
            data=[
                WebsiteOverviewSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class DailyActiveUsersQuery:
    """
    Query class for DailyActiveUsers entity operations.
    """

    def __init__(self, connector: GoogleAnalyticsDataApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        property_id: str,
        date_ranges: list[DailyActiveUsersListParamsDaterangesItem] | None = None,
        dimensions: list[DailyActiveUsersListParamsDimensionsItem] | None = None,
        metrics: list[DailyActiveUsersListParamsMetricsItem] | None = None,
        keep_empty_rows: bool | None = None,
        return_property_quota: bool | None = None,
        limit: int | None = None,
        **kwargs
    ) -> DailyActiveUsersListResult:
        """
        Returns daily active user counts (1-day active users) by date.

        Args:
            date_ranges: Parameter dateRanges
            dimensions: Parameter dimensions
            metrics: Parameter metrics
            keep_empty_rows: Parameter keepEmptyRows
            return_property_quota: Parameter returnPropertyQuota
            limit: Parameter limit
            property_id: GA4 property ID
            **kwargs: Additional parameters

        Returns:
            DailyActiveUsersListResult
        """
        params = {k: v for k, v in {
            "dateRanges": date_ranges,
            "dimensions": dimensions,
            "metrics": metrics,
            "keepEmptyRows": keep_empty_rows,
            "returnPropertyQuota": return_property_quota,
            "limit": limit,
            "property_id": property_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("daily_active_users", "list", params)
        # Cast generic envelope to concrete typed result
        return DailyActiveUsersListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: DailyActiveUsersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DailyActiveUsersSearchResult:
        """
        Search daily_active_users records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DailyActiveUsersSearchFilter):
        - active1_day_users: Number of distinct users active in the last 1 day
        - date: Date of the report row in YYYYMMDD format
        - end_date: End date of the reporting period
        - property_id: GA4 property ID
        - start_date: Start date of the reporting period

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DailyActiveUsersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("daily_active_users", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DailyActiveUsersSearchResult(
            data=[
                DailyActiveUsersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class WeeklyActiveUsersQuery:
    """
    Query class for WeeklyActiveUsers entity operations.
    """

    def __init__(self, connector: GoogleAnalyticsDataApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        property_id: str,
        date_ranges: list[WeeklyActiveUsersListParamsDaterangesItem] | None = None,
        dimensions: list[WeeklyActiveUsersListParamsDimensionsItem] | None = None,
        metrics: list[WeeklyActiveUsersListParamsMetricsItem] | None = None,
        keep_empty_rows: bool | None = None,
        return_property_quota: bool | None = None,
        limit: int | None = None,
        **kwargs
    ) -> WeeklyActiveUsersListResult:
        """
        Returns weekly active user counts (7-day active users) by date.

        Args:
            date_ranges: Parameter dateRanges
            dimensions: Parameter dimensions
            metrics: Parameter metrics
            keep_empty_rows: Parameter keepEmptyRows
            return_property_quota: Parameter returnPropertyQuota
            limit: Parameter limit
            property_id: GA4 property ID
            **kwargs: Additional parameters

        Returns:
            WeeklyActiveUsersListResult
        """
        params = {k: v for k, v in {
            "dateRanges": date_ranges,
            "dimensions": dimensions,
            "metrics": metrics,
            "keepEmptyRows": keep_empty_rows,
            "returnPropertyQuota": return_property_quota,
            "limit": limit,
            "property_id": property_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("weekly_active_users", "list", params)
        # Cast generic envelope to concrete typed result
        return WeeklyActiveUsersListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: WeeklyActiveUsersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> WeeklyActiveUsersSearchResult:
        """
        Search weekly_active_users records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (WeeklyActiveUsersSearchFilter):
        - active7_day_users: Number of distinct users active in the last 7 days
        - date: Date of the report row in YYYYMMDD format
        - end_date: End date of the reporting period
        - property_id: GA4 property ID
        - start_date: Start date of the reporting period

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            WeeklyActiveUsersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("weekly_active_users", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return WeeklyActiveUsersSearchResult(
            data=[
                WeeklyActiveUsersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class FourWeeklyActiveUsersQuery:
    """
    Query class for FourWeeklyActiveUsers entity operations.
    """

    def __init__(self, connector: GoogleAnalyticsDataApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        property_id: str,
        date_ranges: list[FourWeeklyActiveUsersListParamsDaterangesItem] | None = None,
        dimensions: list[FourWeeklyActiveUsersListParamsDimensionsItem] | None = None,
        metrics: list[FourWeeklyActiveUsersListParamsMetricsItem] | None = None,
        keep_empty_rows: bool | None = None,
        return_property_quota: bool | None = None,
        limit: int | None = None,
        **kwargs
    ) -> FourWeeklyActiveUsersListResult:
        """
        Returns 28-day active user counts by date.

        Args:
            date_ranges: Parameter dateRanges
            dimensions: Parameter dimensions
            metrics: Parameter metrics
            keep_empty_rows: Parameter keepEmptyRows
            return_property_quota: Parameter returnPropertyQuota
            limit: Parameter limit
            property_id: GA4 property ID
            **kwargs: Additional parameters

        Returns:
            FourWeeklyActiveUsersListResult
        """
        params = {k: v for k, v in {
            "dateRanges": date_ranges,
            "dimensions": dimensions,
            "metrics": metrics,
            "keepEmptyRows": keep_empty_rows,
            "returnPropertyQuota": return_property_quota,
            "limit": limit,
            "property_id": property_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("four_weekly_active_users", "list", params)
        # Cast generic envelope to concrete typed result
        return FourWeeklyActiveUsersListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: FourWeeklyActiveUsersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> FourWeeklyActiveUsersSearchResult:
        """
        Search four_weekly_active_users records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (FourWeeklyActiveUsersSearchFilter):
        - active28_day_users: Number of distinct users active in the last 28 days
        - date: Date of the report row in YYYYMMDD format
        - end_date: End date of the reporting period
        - property_id: GA4 property ID
        - start_date: Start date of the reporting period

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            FourWeeklyActiveUsersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("four_weekly_active_users", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return FourWeeklyActiveUsersSearchResult(
            data=[
                FourWeeklyActiveUsersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TrafficSourcesQuery:
    """
    Query class for TrafficSources entity operations.
    """

    def __init__(self, connector: GoogleAnalyticsDataApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        property_id: str,
        date_ranges: list[TrafficSourcesListParamsDaterangesItem] | None = None,
        dimensions: list[TrafficSourcesListParamsDimensionsItem] | None = None,
        metrics: list[TrafficSourcesListParamsMetricsItem] | None = None,
        keep_empty_rows: bool | None = None,
        return_property_quota: bool | None = None,
        limit: int | None = None,
        **kwargs
    ) -> TrafficSourcesListResult:
        """
        Returns traffic source metrics broken down by session source, session medium, and date, including users, sessions, bounce rate, and page views.

        Args:
            date_ranges: Parameter dateRanges
            dimensions: Parameter dimensions
            metrics: Parameter metrics
            keep_empty_rows: Parameter keepEmptyRows
            return_property_quota: Parameter returnPropertyQuota
            limit: Parameter limit
            property_id: GA4 property ID
            **kwargs: Additional parameters

        Returns:
            TrafficSourcesListResult
        """
        params = {k: v for k, v in {
            "dateRanges": date_ranges,
            "dimensions": dimensions,
            "metrics": metrics,
            "keepEmptyRows": keep_empty_rows,
            "returnPropertyQuota": return_property_quota,
            "limit": limit,
            "property_id": property_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("traffic_sources", "list", params)
        # Cast generic envelope to concrete typed result
        return TrafficSourcesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: TrafficSourcesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TrafficSourcesSearchResult:
        """
        Search traffic_sources records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TrafficSourcesSearchFilter):
        - average_session_duration: Average duration of sessions in seconds
        - bounce_rate: Percentage of sessions that were single-page with no interaction
        - date: Date of the report row in YYYYMMDD format
        - end_date: End date of the reporting period
        - new_users: Number of first-time users
        - property_id: GA4 property ID
        - screen_page_views: Total number of screen or page views
        - screen_page_views_per_session: Average page views per session
        - session_medium: The medium of the traffic source (e.g., organic, cpc, referral)
        - session_source: The source of the traffic (e.g., google, direct)
        - sessions: Total number of sessions
        - sessions_per_user: Average number of sessions per user
        - start_date: Start date of the reporting period
        - total_users: Total number of unique users

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TrafficSourcesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("traffic_sources", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TrafficSourcesSearchResult(
            data=[
                TrafficSourcesSearchData(**row)
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

    def __init__(self, connector: GoogleAnalyticsDataApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        property_id: str,
        date_ranges: list[PagesListParamsDaterangesItem] | None = None,
        dimensions: list[PagesListParamsDimensionsItem] | None = None,
        metrics: list[PagesListParamsMetricsItem] | None = None,
        keep_empty_rows: bool | None = None,
        return_property_quota: bool | None = None,
        limit: int | None = None,
        **kwargs
    ) -> PagesListResult:
        """
        Returns page-level metrics including page views and bounce rate, broken down by host name, page path, and date.

        Args:
            date_ranges: Parameter dateRanges
            dimensions: Parameter dimensions
            metrics: Parameter metrics
            keep_empty_rows: Parameter keepEmptyRows
            return_property_quota: Parameter returnPropertyQuota
            limit: Parameter limit
            property_id: GA4 property ID
            **kwargs: Additional parameters

        Returns:
            PagesListResult
        """
        params = {k: v for k, v in {
            "dateRanges": date_ranges,
            "dimensions": dimensions,
            "metrics": metrics,
            "keepEmptyRows": keep_empty_rows,
            "returnPropertyQuota": return_property_quota,
            "limit": limit,
            "property_id": property_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pages", "list", params)
        # Cast generic envelope to concrete typed result
        return PagesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



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
        - bounce_rate: Percentage of sessions that were single-page with no interaction
        - date: Date of the report row in YYYYMMDD format
        - end_date: End date of the reporting period
        - host_name: The hostname of the page
        - page_path_plus_query_string: The page path and query string
        - property_id: GA4 property ID
        - screen_page_views: Total number of screen or page views
        - start_date: Start date of the reporting period

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

class DevicesQuery:
    """
    Query class for Devices entity operations.
    """

    def __init__(self, connector: GoogleAnalyticsDataApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        property_id: str,
        date_ranges: list[DevicesListParamsDaterangesItem] | None = None,
        dimensions: list[DevicesListParamsDimensionsItem] | None = None,
        metrics: list[DevicesListParamsMetricsItem] | None = None,
        keep_empty_rows: bool | None = None,
        return_property_quota: bool | None = None,
        limit: int | None = None,
        **kwargs
    ) -> DevicesListResult:
        """
        Returns device-related metrics broken down by device category, operating system, browser, and date, including users, sessions, and page views.

        Args:
            date_ranges: Parameter dateRanges
            dimensions: Parameter dimensions
            metrics: Parameter metrics
            keep_empty_rows: Parameter keepEmptyRows
            return_property_quota: Parameter returnPropertyQuota
            limit: Parameter limit
            property_id: GA4 property ID
            **kwargs: Additional parameters

        Returns:
            DevicesListResult
        """
        params = {k: v for k, v in {
            "dateRanges": date_ranges,
            "dimensions": dimensions,
            "metrics": metrics,
            "keepEmptyRows": keep_empty_rows,
            "returnPropertyQuota": return_property_quota,
            "limit": limit,
            "property_id": property_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("devices", "list", params)
        # Cast generic envelope to concrete typed result
        return DevicesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: DevicesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DevicesSearchResult:
        """
        Search devices records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DevicesSearchFilter):
        - average_session_duration: Average duration of sessions in seconds
        - bounce_rate: Percentage of sessions that were single-page with no interaction
        - browser: The web browser used (e.g., Chrome, Safari, Firefox)
        - date: Date of the report row in YYYYMMDD format
        - device_category: The device category (desktop, mobile, tablet)
        - end_date: End date of the reporting period
        - new_users: Number of first-time users
        - operating_system: The operating system used (e.g., Windows, iOS, Android)
        - property_id: GA4 property ID
        - screen_page_views: Total number of screen or page views
        - screen_page_views_per_session: Average page views per session
        - sessions: Total number of sessions
        - sessions_per_user: Average number of sessions per user
        - start_date: Start date of the reporting period
        - total_users: Total number of unique users

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DevicesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("devices", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DevicesSearchResult(
            data=[
                DevicesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class LocationsQuery:
    """
    Query class for Locations entity operations.
    """

    def __init__(self, connector: GoogleAnalyticsDataApiConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        property_id: str,
        date_ranges: list[LocationsListParamsDaterangesItem] | None = None,
        dimensions: list[LocationsListParamsDimensionsItem] | None = None,
        metrics: list[LocationsListParamsMetricsItem] | None = None,
        keep_empty_rows: bool | None = None,
        return_property_quota: bool | None = None,
        limit: int | None = None,
        **kwargs
    ) -> LocationsListResult:
        """
        Returns geographic metrics broken down by region, country, city, and date, including users, sessions, bounce rate, and page views.

        Args:
            date_ranges: Parameter dateRanges
            dimensions: Parameter dimensions
            metrics: Parameter metrics
            keep_empty_rows: Parameter keepEmptyRows
            return_property_quota: Parameter returnPropertyQuota
            limit: Parameter limit
            property_id: GA4 property ID
            **kwargs: Additional parameters

        Returns:
            LocationsListResult
        """
        params = {k: v for k, v in {
            "dateRanges": date_ranges,
            "dimensions": dimensions,
            "metrics": metrics,
            "keepEmptyRows": keep_empty_rows,
            "returnPropertyQuota": return_property_quota,
            "limit": limit,
            "property_id": property_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("locations", "list", params)
        # Cast generic envelope to concrete typed result
        return LocationsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: LocationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> LocationsSearchResult:
        """
        Search locations records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (LocationsSearchFilter):
        - average_session_duration: Average duration of sessions in seconds
        - bounce_rate: Percentage of sessions that were single-page with no interaction
        - city: The city of the user
        - country: The country of the user
        - date: Date of the report row in YYYYMMDD format
        - end_date: End date of the reporting period
        - new_users: Number of first-time users
        - property_id: GA4 property ID
        - region: The region (state/province) of the user
        - screen_page_views: Total number of screen or page views
        - screen_page_views_per_session: Average page views per session
        - sessions: Total number of sessions
        - sessions_per_user: Average number of sessions per user
        - start_date: Start date of the reporting period
        - total_users: Total number of unique users

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            LocationsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("locations", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return LocationsSearchResult(
            data=[
                LocationsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
