"""
Google-Analytics-Data-Api connector.
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

from pydantic import BaseModel

from .connector_model import GoogleAnalyticsDataApiConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
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




class GoogleAnalyticsDataApiConnector:
    """
    Type-safe Google-Analytics-Data-Api API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "google-analytics-data-api"
    connector_version = "1.0.2"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

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
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

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

            # Hosted mode with lookup by customer_name
            connector = GoogleAnalyticsDataApiConnector(
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
                connector_definition_id=str(GoogleAnalyticsDataApiConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or GoogleAnalyticsDataApiAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

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
        params: "WebsiteOverviewListParams"
    ) -> "WebsiteOverviewListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["daily_active_users"],
        action: Literal["list"],
        params: "DailyActiveUsersListParams"
    ) -> "DailyActiveUsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["weekly_active_users"],
        action: Literal["list"],
        params: "WeeklyActiveUsersListParams"
    ) -> "WeeklyActiveUsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["four_weekly_active_users"],
        action: Literal["list"],
        params: "FourWeeklyActiveUsersListParams"
    ) -> "FourWeeklyActiveUsersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["traffic_sources"],
        action: Literal["list"],
        params: "TrafficSourcesListParams"
    ) -> "TrafficSourcesListResult": ...

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
        entity: Literal["devices"],
        action: Literal["list"],
        params: "DevicesListParams"
    ) -> "DevicesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["locations"],
        action: Literal["list"],
        params: "LocationsListParams"
    ) -> "LocationsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "search"],
        params: Mapping[str, Any]
    ) -> GoogleAnalyticsDataApiExecuteResult[Any] | GoogleAnalyticsDataApiExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "search"],
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
        enable_hosted_mode_features: bool = True,
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
    ) -> _F | Callable[[_F], _F]:
        """
        Decorator that adds tool utilities like docstring augmentation and output limits.

        Usage:
            @mcp.tool()
            @GoogleAnalyticsDataApiConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @GoogleAnalyticsDataApiConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    GoogleAnalyticsDataApiConnectorModel,
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

        Example:
            connector = await GoogleAnalyticsDataApiConnector.create(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def get_consent_url(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        redirect_url: str,
        name: str | None = None,
        replication_config: "GoogleAnalyticsDataApiReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> str:
        """
        Initiate server-side OAuth flow with auto-source creation.

        Returns a consent URL where the end user should be redirected to grant access.
        After completing consent, the source is automatically created and the user is
        redirected to your redirect_url with a `connector_id` query parameter.

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            redirect_url: URL where users will be redirected after OAuth consent.
                After consent, user arrives at: redirect_url?connector_id=...
            name: Optional name for the source. Defaults to connector name + customer_name.
            replication_config: Typed replication settings. Merged with OAuth credentials.
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            The OAuth consent URL

        Example:
            consent_url = await GoogleAnalyticsDataApiConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Google-Analytics-Data-Api Source",
                replication_config=GoogleAnalyticsDataApiReplicationConfig(property_ids="..."),
            )
            # Redirect user to: consent_url
            # After consent, user arrives at: https://myapp.com/oauth/callback?connector_id=...
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for get_consent_url()")

        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
            organization_id=airbyte_config.organization_id,
        )

        try:
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config and hasattr(replication_config, 'model_dump') else replication_config

            consent_url = await client.initiate_oauth(
                definition_id=str(GoogleAnalyticsDataApiConnectorModel.id),
                customer_name=airbyte_config.customer_name,
                redirect_url=redirect_url,
                name=name,
                replication_config=replication_config_dict,
                source_template_id=source_template_id,
            )
        finally:
            await client.close()

        return consent_url

    @classmethod
    async def create(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        auth_config: "GoogleAnalyticsDataApiAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "GoogleAnalyticsDataApiReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "GoogleAnalyticsDataApiConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Supports two authentication modes:
        1. Direct credentials: Provide `auth_config` with typed credentials
        2. Server-side OAuth: Provide `server_side_oauth_secret_id` from OAuth flow

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            auth_config: Typed auth config. Required unless using server_side_oauth_secret_id.
            server_side_oauth_secret_id: OAuth secret ID from get_consent_url redirect.
                When provided, auth_config is not required.
            name: Optional source name (defaults to connector name + customer_name)
            replication_config: Typed replication settings.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A GoogleAnalyticsDataApiConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await GoogleAnalyticsDataApiConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GoogleAnalyticsDataApiAuthConfig(client_id="...", client_secret="...", refresh_token="..."),
            )

            # With replication config (required for this connector):
            connector = await GoogleAnalyticsDataApiConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GoogleAnalyticsDataApiAuthConfig(client_id="...", client_secret="...", refresh_token="..."),
                replication_config=GoogleAnalyticsDataApiReplicationConfig(property_ids="..."),
            )

            # With server-side OAuth:
            connector = await GoogleAnalyticsDataApiConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=GoogleAnalyticsDataApiReplicationConfig(property_ids="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for create()")

        # Validate: exactly one of auth_config or server_side_oauth_secret_id required
        if auth_config is None and server_side_oauth_secret_id is None:
            raise ValueError(
                "Either auth_config or server_side_oauth_secret_id must be provided"
            )
        if auth_config is not None and server_side_oauth_secret_id is not None:
            raise ValueError(
                "Cannot provide both auth_config and server_side_oauth_secret_id"
            )

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
                connector_definition_id=str(GoogleAnalyticsDataApiConnectorModel.id),
                customer_name=airbyte_config.customer_name,
                credentials=credentials,
                replication_config=replication_config_dict,
                server_side_oauth_secret_id=server_side_oauth_secret_id,
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
            data=result.data
        )



    async def search(
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

        result = await self._connector.execute("website_overview", "search", params)

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
            data=result.data
        )



    async def search(
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

        result = await self._connector.execute("daily_active_users", "search", params)

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
            data=result.data
        )



    async def search(
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

        result = await self._connector.execute("weekly_active_users", "search", params)

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
            data=result.data
        )



    async def search(
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

        result = await self._connector.execute("four_weekly_active_users", "search", params)

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
            data=result.data
        )



    async def search(
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

        result = await self._connector.execute("traffic_sources", "search", params)

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
            data=result.data
        )



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
            data=result.data
        )



    async def search(
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

        result = await self._connector.execute("devices", "search", params)

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
            data=result.data
        )



    async def search(
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

        result = await self._connector.execute("locations", "search", params)

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
