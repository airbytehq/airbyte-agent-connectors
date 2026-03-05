"""
Google-Search-Console connector.
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

from .connector_model import GoogleSearchConsoleConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    SearchAnalyticsAllFieldsListParams,
    SearchAnalyticsByCountryListParams,
    SearchAnalyticsByDateListParams,
    SearchAnalyticsByDeviceListParams,
    SearchAnalyticsByPageListParams,
    SearchAnalyticsByQueryListParams,
    SitemapsGetParams,
    SitemapsListParams,
    SitesGetParams,
    SitesListParams,
    AirbyteSearchParams,
    SitesSearchFilter,
    SitesSearchQuery,
    SitemapsSearchFilter,
    SitemapsSearchQuery,
    SearchAnalyticsAllFieldsSearchFilter,
    SearchAnalyticsAllFieldsSearchQuery,
    SearchAnalyticsByCountrySearchFilter,
    SearchAnalyticsByCountrySearchQuery,
    SearchAnalyticsByDateSearchFilter,
    SearchAnalyticsByDateSearchQuery,
    SearchAnalyticsByDeviceSearchFilter,
    SearchAnalyticsByDeviceSearchQuery,
    SearchAnalyticsByPageSearchFilter,
    SearchAnalyticsByPageSearchQuery,
    SearchAnalyticsByQuerySearchFilter,
    SearchAnalyticsByQuerySearchQuery,
)
from .models import GoogleSearchConsoleAuthConfig
if TYPE_CHECKING:
    from .models import GoogleSearchConsoleReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    GoogleSearchConsoleCheckResult,
    GoogleSearchConsoleExecuteResult,
    GoogleSearchConsoleExecuteResultWithMeta,
    SitesListResult,
    SitemapsListResult,
    SearchAnalyticsByDateListResult,
    SearchAnalyticsByCountryListResult,
    SearchAnalyticsByDeviceListResult,
    SearchAnalyticsByPageListResult,
    SearchAnalyticsByQueryListResult,
    SearchAnalyticsAllFieldsListResult,
    SearchAnalyticsRow,
    Site,
    Sitemap,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    SitesSearchData,
    SitesSearchResult,
    SitemapsSearchData,
    SitemapsSearchResult,
    SearchAnalyticsAllFieldsSearchData,
    SearchAnalyticsAllFieldsSearchResult,
    SearchAnalyticsByCountrySearchData,
    SearchAnalyticsByCountrySearchResult,
    SearchAnalyticsByDateSearchData,
    SearchAnalyticsByDateSearchResult,
    SearchAnalyticsByDeviceSearchData,
    SearchAnalyticsByDeviceSearchResult,
    SearchAnalyticsByPageSearchData,
    SearchAnalyticsByPageSearchResult,
    SearchAnalyticsByQuerySearchData,
    SearchAnalyticsByQuerySearchResult,
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




class GoogleSearchConsoleConnector:
    """
    Type-safe Google-Search-Console API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "google-search-console"
    connector_version = "1.0.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("sites", "list"): True,
        ("sites", "get"): None,
        ("sitemaps", "list"): True,
        ("sitemaps", "get"): None,
        ("search_analytics_by_date", "list"): True,
        ("search_analytics_by_country", "list"): True,
        ("search_analytics_by_device", "list"): True,
        ("search_analytics_by_page", "list"): True,
        ("search_analytics_by_query", "list"): True,
        ("search_analytics_all_fields", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('sites', 'get'): {'site_url': 'siteUrl'},
        ('sitemaps', 'list'): {'site_url': 'siteUrl'},
        ('sitemaps', 'get'): {'site_url': 'siteUrl', 'feedpath': 'feedpath'},
        ('search_analytics_by_date', 'list'): {'start_date': 'startDate', 'end_date': 'endDate', 'dimensions': 'dimensions', 'row_limit': 'rowLimit', 'start_row': 'startRow', 'type': 'type', 'aggregation_type': 'aggregationType', 'data_state': 'dataState', 'site_url': 'siteUrl'},
        ('search_analytics_by_country', 'list'): {'start_date': 'startDate', 'end_date': 'endDate', 'dimensions': 'dimensions', 'row_limit': 'rowLimit', 'start_row': 'startRow', 'type': 'type', 'aggregation_type': 'aggregationType', 'data_state': 'dataState', 'site_url': 'siteUrl'},
        ('search_analytics_by_device', 'list'): {'start_date': 'startDate', 'end_date': 'endDate', 'dimensions': 'dimensions', 'row_limit': 'rowLimit', 'start_row': 'startRow', 'type': 'type', 'aggregation_type': 'aggregationType', 'data_state': 'dataState', 'site_url': 'siteUrl'},
        ('search_analytics_by_page', 'list'): {'start_date': 'startDate', 'end_date': 'endDate', 'dimensions': 'dimensions', 'row_limit': 'rowLimit', 'start_row': 'startRow', 'type': 'type', 'aggregation_type': 'aggregationType', 'data_state': 'dataState', 'site_url': 'siteUrl'},
        ('search_analytics_by_query', 'list'): {'start_date': 'startDate', 'end_date': 'endDate', 'dimensions': 'dimensions', 'row_limit': 'rowLimit', 'start_row': 'startRow', 'type': 'type', 'aggregation_type': 'aggregationType', 'data_state': 'dataState', 'site_url': 'siteUrl'},
        ('search_analytics_all_fields', 'list'): {'start_date': 'startDate', 'end_date': 'endDate', 'dimensions': 'dimensions', 'row_limit': 'rowLimit', 'start_row': 'startRow', 'type': 'type', 'aggregation_type': 'aggregationType', 'data_state': 'dataState', 'site_url': 'siteUrl'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (GoogleSearchConsoleAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: GoogleSearchConsoleAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new google-search-console connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., GoogleSearchConsoleAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = GoogleSearchConsoleConnector(auth_config=GoogleSearchConsoleAuthConfig(client_id="...", client_secret="...", refresh_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = GoogleSearchConsoleConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = GoogleSearchConsoleConnector(
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
                connector_definition_id=str(GoogleSearchConsoleConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or GoogleSearchConsoleAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=GoogleSearchConsoleConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.sites = SitesQuery(self)
        self.sitemaps = SitemapsQuery(self)
        self.search_analytics_by_date = SearchAnalyticsByDateQuery(self)
        self.search_analytics_by_country = SearchAnalyticsByCountryQuery(self)
        self.search_analytics_by_device = SearchAnalyticsByDeviceQuery(self)
        self.search_analytics_by_page = SearchAnalyticsByPageQuery(self)
        self.search_analytics_by_query = SearchAnalyticsByQueryQuery(self)
        self.search_analytics_all_fields = SearchAnalyticsAllFieldsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["sites"],
        action: Literal["list"],
        params: "SitesListParams"
    ) -> "SitesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sites"],
        action: Literal["get"],
        params: "SitesGetParams"
    ) -> "Site": ...

    @overload
    async def execute(
        self,
        entity: Literal["sitemaps"],
        action: Literal["list"],
        params: "SitemapsListParams"
    ) -> "SitemapsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["sitemaps"],
        action: Literal["get"],
        params: "SitemapsGetParams"
    ) -> "Sitemap": ...

    @overload
    async def execute(
        self,
        entity: Literal["search_analytics_by_date"],
        action: Literal["list"],
        params: "SearchAnalyticsByDateListParams"
    ) -> "SearchAnalyticsByDateListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["search_analytics_by_country"],
        action: Literal["list"],
        params: "SearchAnalyticsByCountryListParams"
    ) -> "SearchAnalyticsByCountryListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["search_analytics_by_device"],
        action: Literal["list"],
        params: "SearchAnalyticsByDeviceListParams"
    ) -> "SearchAnalyticsByDeviceListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["search_analytics_by_page"],
        action: Literal["list"],
        params: "SearchAnalyticsByPageListParams"
    ) -> "SearchAnalyticsByPageListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["search_analytics_by_query"],
        action: Literal["list"],
        params: "SearchAnalyticsByQueryListParams"
    ) -> "SearchAnalyticsByQueryListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["search_analytics_all_fields"],
        action: Literal["list"],
        params: "SearchAnalyticsAllFieldsListParams"
    ) -> "SearchAnalyticsAllFieldsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> GoogleSearchConsoleExecuteResult[Any] | GoogleSearchConsoleExecuteResultWithMeta[Any, Any] | Any: ...

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
                return GoogleSearchConsoleExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GoogleSearchConsoleExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> GoogleSearchConsoleCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            GoogleSearchConsoleCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return GoogleSearchConsoleCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return GoogleSearchConsoleCheckResult(
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
            @GoogleSearchConsoleConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @GoogleSearchConsoleConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    GoogleSearchConsoleConnectorModel,
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
        return describe_entities(GoogleSearchConsoleConnectorModel)

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
            (e for e in GoogleSearchConsoleConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in GoogleSearchConsoleConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await GoogleSearchConsoleConnector.create(...)
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
        replication_config: "GoogleSearchConsoleReplicationConfig" | None = None,
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
            consent_url = await GoogleSearchConsoleConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Google-Search-Console Source",
                replication_config=GoogleSearchConsoleReplicationConfig(site_urls="...", start_date="..."),
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
                definition_id=str(GoogleSearchConsoleConnectorModel.id),
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
        auth_config: "GoogleSearchConsoleAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "GoogleSearchConsoleReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "GoogleSearchConsoleConnector":
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
            A GoogleSearchConsoleConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await GoogleSearchConsoleConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GoogleSearchConsoleAuthConfig(client_id="...", client_secret="...", refresh_token="..."),
            )

            # With replication config (required for this connector):
            connector = await GoogleSearchConsoleConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=GoogleSearchConsoleAuthConfig(client_id="...", client_secret="...", refresh_token="..."),
                replication_config=GoogleSearchConsoleReplicationConfig(site_urls="...", start_date="..."),
            )

            # With server-side OAuth:
            connector = await GoogleSearchConsoleConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=GoogleSearchConsoleReplicationConfig(site_urls="...", start_date="..."),
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
                connector_definition_id=str(GoogleSearchConsoleConnectorModel.id),
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




class SitesQuery:
    """
    Query class for Sites entity operations.
    """

    def __init__(self, connector: GoogleSearchConsoleConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> SitesListResult:
        """
        Lists the user's Search Console sites.

        Returns:
            SitesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sites", "list", params)
        # Cast generic envelope to concrete typed result
        return SitesListResult(
            data=result.data
        )



    async def get(
        self,
        site_url: str,
        **kwargs
    ) -> Site:
        """
        Retrieves information about a specific site.

        Args:
            site_url: The URL of the property as defined in Search Console. Examples: http://www.example.com/ (for a URL-prefix property) or sc-domain:example.com (for a Domain property)

            **kwargs: Additional parameters

        Returns:
            Site
        """
        params = {k: v for k, v in {
            "siteUrl": site_url,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sites", "get", params)
        return result



    async def search(
        self,
        query: SitesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SitesSearchResult:
        """
        Search sites records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SitesSearchFilter):
        - permission_level: The user's permission level for the site (owner, full, restricted, etc.)
        - site_url: The URL of the site data being fetched

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SitesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("sites", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SitesSearchResult(
            data=[
                SitesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SitemapsQuery:
    """
    Query class for Sitemaps entity operations.
    """

    def __init__(self, connector: GoogleSearchConsoleConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        site_url: str,
        **kwargs
    ) -> SitemapsListResult:
        """
        Lists the sitemaps submitted for a site.

        Args:
            site_url: The URL of the property as defined in Search Console.

            **kwargs: Additional parameters

        Returns:
            SitemapsListResult
        """
        params = {k: v for k, v in {
            "siteUrl": site_url,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sitemaps", "list", params)
        # Cast generic envelope to concrete typed result
        return SitemapsListResult(
            data=result.data
        )



    async def get(
        self,
        site_url: str,
        feedpath: str,
        **kwargs
    ) -> Sitemap:
        """
        Retrieves information about a specific sitemap.

        Args:
            site_url: The URL of the property as defined in Search Console.

            feedpath: The URL of the sitemap.
            **kwargs: Additional parameters

        Returns:
            Sitemap
        """
        params = {k: v for k, v in {
            "siteUrl": site_url,
            "feedpath": feedpath,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sitemaps", "get", params)
        return result



    async def search(
        self,
        query: SitemapsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SitemapsSearchResult:
        """
        Search sitemaps records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SitemapsSearchFilter):
        - contents: Data related to the sitemap contents
        - errors: Errors encountered while processing the sitemaps
        - is_pending: Flag indicating if the sitemap is pending for processing
        - is_sitemaps_index: Flag indicating if the data represents a sitemap index
        - last_downloaded: Timestamp when the sitemap was last downloaded
        - last_submitted: Timestamp when the sitemap was last submitted
        - path: Path to the sitemap file
        - type_: Type of the sitemap
        - warnings: Warnings encountered while processing the sitemaps

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SitemapsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("sitemaps", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SitemapsSearchResult(
            data=[
                SitemapsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SearchAnalyticsByDateQuery:
    """
    Query class for SearchAnalyticsByDate entity operations.
    """

    def __init__(self, connector: GoogleSearchConsoleConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_date: str,
        end_date: str,
        site_url: str,
        dimensions: list[str] | None = None,
        row_limit: int | None = None,
        start_row: int | None = None,
        type: str | None = None,
        aggregation_type: str | None = None,
        data_state: str | None = None,
        **kwargs
    ) -> SearchAnalyticsByDateListResult:
        """
        Query search analytics data grouped by date. Returns clicks, impressions, CTR, and average position for each date in the specified range.


        Args:
            start_date: Start date of the requested date range, in YYYY-MM-DD format.
            end_date: End date of the requested date range, in YYYY-MM-DD format.
            dimensions: Dimensions to group results by.
            row_limit: The maximum number of rows to return.
            start_row: Zero-based index of the first row in the response.
            type: Filter results by type: web, discover, googleNews, news, image, video.

            aggregation_type: How data is aggregated: auto, byPage, byProperty, byNewsShowcasePanel.

            data_state: Data freshness: final (stable data only) or all (includes fresh data).

            site_url: The URL of the property as defined in Search Console.
            **kwargs: Additional parameters

        Returns:
            SearchAnalyticsByDateListResult
        """
        params = {k: v for k, v in {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": dimensions,
            "rowLimit": row_limit,
            "startRow": start_row,
            "type": type,
            "aggregationType": aggregation_type,
            "dataState": data_state,
            "siteUrl": site_url,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("search_analytics_by_date", "list", params)
        # Cast generic envelope to concrete typed result
        return SearchAnalyticsByDateListResult(
            data=result.data
        )



    async def search(
        self,
        query: SearchAnalyticsByDateSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SearchAnalyticsByDateSearchResult:
        """
        Search search_analytics_by_date records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SearchAnalyticsByDateSearchFilter):
        - clicks: The total number of clicks on the specific date
        - ctr: The click-through rate for the specific date
        - date: The date for which the search analytics data is being reported
        - impressions: The number of impressions on the specific date
        - position: The average position in search results for the specific date
        - search_type: The type of search query that generated the data
        - site_url: The URL of the site for which the search analytics data is being reported

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SearchAnalyticsByDateSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("search_analytics_by_date", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SearchAnalyticsByDateSearchResult(
            data=[
                SearchAnalyticsByDateSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SearchAnalyticsByCountryQuery:
    """
    Query class for SearchAnalyticsByCountry entity operations.
    """

    def __init__(self, connector: GoogleSearchConsoleConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_date: str,
        end_date: str,
        site_url: str,
        dimensions: list[str] | None = None,
        row_limit: int | None = None,
        start_row: int | None = None,
        type: str | None = None,
        aggregation_type: str | None = None,
        data_state: str | None = None,
        **kwargs
    ) -> SearchAnalyticsByCountryListResult:
        """
        Query search analytics data grouped by date and country. Returns clicks, impressions, CTR, and average position for each country.


        Args:
            start_date: Start date of the requested date range, in YYYY-MM-DD format.
            end_date: End date of the requested date range, in YYYY-MM-DD format.
            dimensions: Dimensions to group results by.
            row_limit: The maximum number of rows to return.
            start_row: Zero-based index of the first row in the response.
            type: Filter results by type: web, discover, googleNews, news, image, video.

            aggregation_type: How data is aggregated: auto, byPage, byProperty.

            data_state: Data freshness: final (stable data only) or all (includes fresh data).

            site_url: The URL of the property as defined in Search Console.
            **kwargs: Additional parameters

        Returns:
            SearchAnalyticsByCountryListResult
        """
        params = {k: v for k, v in {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": dimensions,
            "rowLimit": row_limit,
            "startRow": start_row,
            "type": type,
            "aggregationType": aggregation_type,
            "dataState": data_state,
            "siteUrl": site_url,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("search_analytics_by_country", "list", params)
        # Cast generic envelope to concrete typed result
        return SearchAnalyticsByCountryListResult(
            data=result.data
        )



    async def search(
        self,
        query: SearchAnalyticsByCountrySearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SearchAnalyticsByCountrySearchResult:
        """
        Search search_analytics_by_country records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SearchAnalyticsByCountrySearchFilter):
        - clicks: The number of times users clicked on the search result for a specific country
        - country: The country for which the search analytics data is being reported
        - ctr: The click-through rate for a specific country
        - date: The date for which the search analytics data is being reported
        - impressions: The total number of times a search result was shown for a specific country
        - position: The average position at which the site's search result appeared for a specific country
        - search_type: The type of search for which the data is being reported
        - site_url: The URL of the site for which the search analytics data is being reported

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SearchAnalyticsByCountrySearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("search_analytics_by_country", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SearchAnalyticsByCountrySearchResult(
            data=[
                SearchAnalyticsByCountrySearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SearchAnalyticsByDeviceQuery:
    """
    Query class for SearchAnalyticsByDevice entity operations.
    """

    def __init__(self, connector: GoogleSearchConsoleConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_date: str,
        end_date: str,
        site_url: str,
        dimensions: list[str] | None = None,
        row_limit: int | None = None,
        start_row: int | None = None,
        type: str | None = None,
        aggregation_type: str | None = None,
        data_state: str | None = None,
        **kwargs
    ) -> SearchAnalyticsByDeviceListResult:
        """
        Query search analytics data grouped by date and device. Returns clicks, impressions, CTR, and average position for each device type.


        Args:
            start_date: Start date of the requested date range, in YYYY-MM-DD format.
            end_date: End date of the requested date range, in YYYY-MM-DD format.
            dimensions: Dimensions to group results by.
            row_limit: The maximum number of rows to return.
            start_row: Zero-based index of the first row in the response.
            type: Filter results by type: web, discover, googleNews, news, image, video.

            aggregation_type: How data is aggregated: auto, byPage, byProperty.

            data_state: Data freshness: final (stable data only) or all (includes fresh data).

            site_url: The URL of the property as defined in Search Console.
            **kwargs: Additional parameters

        Returns:
            SearchAnalyticsByDeviceListResult
        """
        params = {k: v for k, v in {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": dimensions,
            "rowLimit": row_limit,
            "startRow": start_row,
            "type": type,
            "aggregationType": aggregation_type,
            "dataState": data_state,
            "siteUrl": site_url,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("search_analytics_by_device", "list", params)
        # Cast generic envelope to concrete typed result
        return SearchAnalyticsByDeviceListResult(
            data=result.data
        )



    async def search(
        self,
        query: SearchAnalyticsByDeviceSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SearchAnalyticsByDeviceSearchResult:
        """
        Search search_analytics_by_device records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SearchAnalyticsByDeviceSearchFilter):
        - clicks: The total number of clicks by device type
        - ctr: Click-through rate by device type
        - date: The date for which the search analytics data is provided
        - device: The type of device used by the user (e.g., desktop, mobile)
        - impressions: The total number of impressions by device type
        - position: The average position in search results by device type
        - search_type: The type of search performed
        - site_url: The URL of the site for which search analytics data is being provided

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SearchAnalyticsByDeviceSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("search_analytics_by_device", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SearchAnalyticsByDeviceSearchResult(
            data=[
                SearchAnalyticsByDeviceSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SearchAnalyticsByPageQuery:
    """
    Query class for SearchAnalyticsByPage entity operations.
    """

    def __init__(self, connector: GoogleSearchConsoleConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_date: str,
        end_date: str,
        site_url: str,
        dimensions: list[str] | None = None,
        row_limit: int | None = None,
        start_row: int | None = None,
        type: str | None = None,
        aggregation_type: str | None = None,
        data_state: str | None = None,
        **kwargs
    ) -> SearchAnalyticsByPageListResult:
        """
        Query search analytics data grouped by date and page. Returns clicks, impressions, CTR, and average position for each page URL.


        Args:
            start_date: Start date of the requested date range, in YYYY-MM-DD format.
            end_date: End date of the requested date range, in YYYY-MM-DD format.
            dimensions: Dimensions to group results by.
            row_limit: The maximum number of rows to return.
            start_row: Zero-based index of the first row in the response.
            type: Filter results by type: web, discover, googleNews, news, image, video.

            aggregation_type: How data is aggregated: auto, byPage, byProperty.

            data_state: Data freshness: final (stable data only) or all (includes fresh data).

            site_url: The URL of the property as defined in Search Console.
            **kwargs: Additional parameters

        Returns:
            SearchAnalyticsByPageListResult
        """
        params = {k: v for k, v in {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": dimensions,
            "rowLimit": row_limit,
            "startRow": start_row,
            "type": type,
            "aggregationType": aggregation_type,
            "dataState": data_state,
            "siteUrl": site_url,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("search_analytics_by_page", "list", params)
        # Cast generic envelope to concrete typed result
        return SearchAnalyticsByPageListResult(
            data=result.data
        )



    async def search(
        self,
        query: SearchAnalyticsByPageSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SearchAnalyticsByPageSearchResult:
        """
        Search search_analytics_by_page records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SearchAnalyticsByPageSearchFilter):
        - clicks: The number of clicks for a specific page
        - ctr: Click-through rate for the page
        - date: The date for which the search analytics data is reported
        - impressions: The number of impressions for the page
        - page: The URL of the specific page being analyzed
        - position: The average position at which the page appeared in search results
        - search_type: The type of search query that led to the page being displayed
        - site_url: The URL of the site for which the search analytics data is being reported

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SearchAnalyticsByPageSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("search_analytics_by_page", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SearchAnalyticsByPageSearchResult(
            data=[
                SearchAnalyticsByPageSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SearchAnalyticsByQueryQuery:
    """
    Query class for SearchAnalyticsByQuery entity operations.
    """

    def __init__(self, connector: GoogleSearchConsoleConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_date: str,
        end_date: str,
        site_url: str,
        dimensions: list[str] | None = None,
        row_limit: int | None = None,
        start_row: int | None = None,
        type: str | None = None,
        aggregation_type: str | None = None,
        data_state: str | None = None,
        **kwargs
    ) -> SearchAnalyticsByQueryListResult:
        """
        Query search analytics data grouped by date and query. Returns clicks, impressions, CTR, and average position for each search query.


        Args:
            start_date: Start date of the requested date range, in YYYY-MM-DD format.
            end_date: End date of the requested date range, in YYYY-MM-DD format.
            dimensions: Dimensions to group results by.
            row_limit: The maximum number of rows to return.
            start_row: Zero-based index of the first row in the response.
            type: Filter results by type: web, discover, googleNews, news, image, video.

            aggregation_type: How data is aggregated: auto, byPage, byProperty.

            data_state: Data freshness: final (stable data only) or all (includes fresh data).

            site_url: The URL of the property as defined in Search Console.
            **kwargs: Additional parameters

        Returns:
            SearchAnalyticsByQueryListResult
        """
        params = {k: v for k, v in {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": dimensions,
            "rowLimit": row_limit,
            "startRow": start_row,
            "type": type,
            "aggregationType": aggregation_type,
            "dataState": data_state,
            "siteUrl": site_url,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("search_analytics_by_query", "list", params)
        # Cast generic envelope to concrete typed result
        return SearchAnalyticsByQueryListResult(
            data=result.data
        )



    async def search(
        self,
        query: SearchAnalyticsByQuerySearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SearchAnalyticsByQuerySearchResult:
        """
        Search search_analytics_by_query records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SearchAnalyticsByQuerySearchFilter):
        - clicks: The number of clicks for the specific query
        - ctr: The click-through rate for the specific query
        - date: The date for which the search analytics data is recorded
        - impressions: The number of impressions for the specific query
        - position: The average position for the specific query
        - query: The search query for which the data is recorded
        - search_type: The type of search result for the specific query
        - site_url: The URL of the site for which the search analytics data is captured

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SearchAnalyticsByQuerySearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("search_analytics_by_query", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SearchAnalyticsByQuerySearchResult(
            data=[
                SearchAnalyticsByQuerySearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SearchAnalyticsAllFieldsQuery:
    """
    Query class for SearchAnalyticsAllFields entity operations.
    """

    def __init__(self, connector: GoogleSearchConsoleConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        start_date: str,
        end_date: str,
        site_url: str,
        dimensions: list[str] | None = None,
        row_limit: int | None = None,
        start_row: int | None = None,
        type: str | None = None,
        aggregation_type: str | None = None,
        data_state: str | None = None,
        **kwargs
    ) -> SearchAnalyticsAllFieldsListResult:
        """
        Query search analytics data grouped by all dimensions (date, country, device, page, query). Returns the most granular breakdown of search data.


        Args:
            start_date: Start date of the requested date range, in YYYY-MM-DD format.
            end_date: End date of the requested date range, in YYYY-MM-DD format.
            dimensions: Dimensions to group results by.
            row_limit: The maximum number of rows to return.
            start_row: Zero-based index of the first row in the response.
            type: Filter results by type: web, discover, googleNews, news, image, video.

            aggregation_type: How data is aggregated: auto, byPage, byProperty.

            data_state: Data freshness: final (stable data only) or all (includes fresh data).

            site_url: The URL of the property as defined in Search Console.
            **kwargs: Additional parameters

        Returns:
            SearchAnalyticsAllFieldsListResult
        """
        params = {k: v for k, v in {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": dimensions,
            "rowLimit": row_limit,
            "startRow": start_row,
            "type": type,
            "aggregationType": aggregation_type,
            "dataState": data_state,
            "siteUrl": site_url,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("search_analytics_all_fields", "list", params)
        # Cast generic envelope to concrete typed result
        return SearchAnalyticsAllFieldsListResult(
            data=result.data
        )



    async def search(
        self,
        query: SearchAnalyticsAllFieldsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SearchAnalyticsAllFieldsSearchResult:
        """
        Search search_analytics_all_fields records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SearchAnalyticsAllFieldsSearchFilter):
        - clicks: The number of times users clicked on the search result for a specific query
        - country: The country from which the search query originated
        - ctr: Click-through rate, calculated as clicks divided by impressions
        - date: The date when the search query occurred
        - device: The type of device used by the user (e.g., desktop, mobile)
        - impressions: The number of times a search result appeared in response to a query
        - page: The page URL that appeared in the search results
        - position: The average position of the search result on the search engine results page
        - query: The search query entered by the user
        - search_type: The type of search (e.g., web, image, video) that triggered the search result
        - site_url: The URL of the site from which the data originates

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SearchAnalyticsAllFieldsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("search_analytics_all_fields", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SearchAnalyticsAllFieldsSearchResult(
            data=[
                SearchAnalyticsAllFieldsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
