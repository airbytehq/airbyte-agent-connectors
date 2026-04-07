"""
Amazon-Seller-Partner connector.
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

from .connector_model import AmazonSellerPartnerConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    CatalogItemsGetParams,
    CatalogItemsListParams,
    ListFinancialEventGroupsListParams,
    ListFinancialEventsListParams,
    OrderItemsListParams,
    OrdersGetParams,
    OrdersListParams,
    ReportsGetParams,
    ReportsListParams,
    AirbyteSearchParams,
    OrdersSearchFilter,
    OrdersSearchQuery,
    OrderItemsSearchFilter,
    OrderItemsSearchQuery,
    ListFinancialEventGroupsSearchFilter,
    ListFinancialEventGroupsSearchQuery,
    ListFinancialEventsSearchFilter,
    ListFinancialEventsSearchQuery,
)
from .models import AmazonSellerPartnerAuthConfig
if TYPE_CHECKING:
    from .models import AmazonSellerPartnerReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    AmazonSellerPartnerCheckResult,
    AmazonSellerPartnerExecuteResult,
    AmazonSellerPartnerExecuteResultWithMeta,
    OrdersListResult,
    OrderItemsListResult,
    ListFinancialEventGroupsListResult,
    ListFinancialEventsListResult,
    CatalogItemsListResult,
    ReportsListResult,
    CatalogItem,
    FinancialEventGroup,
    FinancialEvents,
    Order,
    OrderItem,
    Report,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    OrdersSearchData,
    OrdersSearchResult,
    OrderItemsSearchData,
    OrderItemsSearchResult,
    ListFinancialEventGroupsSearchData,
    ListFinancialEventGroupsSearchResult,
    ListFinancialEventsSearchData,
    ListFinancialEventsSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])

DEFAULT_MAX_OUTPUT_CHARS = 100_000  # ~100KB default, configurable per-tool


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




class AmazonSellerPartnerConnector:
    """
    Type-safe Amazon-Seller-Partner API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "amazon-seller-partner"
    connector_version = "1.0.3"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("orders", "list"): True,
        ("orders", "get"): None,
        ("order_items", "list"): True,
        ("list_financial_event_groups", "list"): True,
        ("list_financial_events", "list"): True,
        ("catalog_items", "list"): True,
        ("catalog_items", "get"): None,
        ("reports", "list"): True,
        ("reports", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('orders', 'list'): {'marketplace_ids': 'MarketplaceIds', 'created_after': 'CreatedAfter', 'created_before': 'CreatedBefore', 'last_updated_after': 'LastUpdatedAfter', 'last_updated_before': 'LastUpdatedBefore', 'order_statuses': 'OrderStatuses', 'max_results_per_page': 'MaxResultsPerPage', 'next_token': 'NextToken'},
        ('orders', 'get'): {'order_id': 'orderId'},
        ('order_items', 'list'): {'order_id': 'orderId', 'next_token': 'NextToken'},
        ('list_financial_event_groups', 'list'): {'financial_event_group_started_after': 'FinancialEventGroupStartedAfter', 'financial_event_group_started_before': 'FinancialEventGroupStartedBefore', 'max_results_per_page': 'MaxResultsPerPage', 'next_token': 'NextToken'},
        ('list_financial_events', 'list'): {'posted_after': 'PostedAfter', 'posted_before': 'PostedBefore', 'max_results_per_page': 'MaxResultsPerPage', 'next_token': 'NextToken'},
        ('catalog_items', 'list'): {'marketplace_ids': 'marketplaceIds', 'keywords': 'keywords', 'identifiers': 'identifiers', 'identifiers_type': 'identifiersType', 'included_data': 'includedData', 'page_size': 'pageSize', 'page_token': 'pageToken'},
        ('catalog_items', 'get'): {'asin': 'asin', 'marketplace_ids': 'marketplaceIds', 'included_data': 'includedData'},
        ('reports', 'list'): {'report_types': 'reportTypes', 'processing_statuses': 'processingStatuses', 'marketplace_ids': 'marketplaceIds', 'page_size': 'pageSize', 'created_since': 'createdSince', 'created_until': 'createdUntil', 'next_token': 'nextToken'},
        ('reports', 'get'): {'report_id': 'reportId'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (AmazonSellerPartnerAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: AmazonSellerPartnerAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        region: str | None = None    ):
        """
        Initialize a new amazon-seller-partner connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., AmazonSellerPartnerAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            region: The SP-API endpoint URL based on seller region:
- NA (North America: US, CA, MX, BR): https://sellingpartnerapi-na.amazon.com
- EU (Europe/Middle East/Africa/India): https://sellingpartnerapi-eu.amazon.com
- FE (Far East: JP, AU, SG): https://sellingpartnerapi-fe.amazon.com

        Examples:
            # Local mode (direct API calls)
            connector = AmazonSellerPartnerConnector(auth_config=AmazonSellerPartnerAuthConfig(lwa_app_id="...", lwa_client_secret="...", refresh_token="...", access_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = AmazonSellerPartnerConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = AmazonSellerPartnerConnector(
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
                connector_definition_id=str(AmazonSellerPartnerConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or AmazonSellerPartnerAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if region:
                config_values["region"] = region

            self._executor = LocalExecutor(
                model=AmazonSellerPartnerConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if region:
                base_url = base_url.replace("{region}", region)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.orders = OrdersQuery(self)
        self.order_items = OrderItemsQuery(self)
        self.list_financial_event_groups = ListFinancialEventGroupsQuery(self)
        self.list_financial_events = ListFinancialEventsQuery(self)
        self.catalog_items = CatalogItemsQuery(self)
        self.reports = ReportsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["orders"],
        action: Literal["list"],
        params: "OrdersListParams"
    ) -> "OrdersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["orders"],
        action: Literal["get"],
        params: "OrdersGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["order_items"],
        action: Literal["list"],
        params: "OrderItemsListParams"
    ) -> "OrderItemsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["list_financial_event_groups"],
        action: Literal["list"],
        params: "ListFinancialEventGroupsListParams"
    ) -> "ListFinancialEventGroupsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["list_financial_events"],
        action: Literal["list"],
        params: "ListFinancialEventsListParams"
    ) -> "ListFinancialEventsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["catalog_items"],
        action: Literal["list"],
        params: "CatalogItemsListParams"
    ) -> "CatalogItemsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["catalog_items"],
        action: Literal["get"],
        params: "CatalogItemsGetParams"
    ) -> "CatalogItem": ...

    @overload
    async def execute(
        self,
        entity: Literal["reports"],
        action: Literal["list"],
        params: "ReportsListParams"
    ) -> "ReportsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["reports"],
        action: Literal["get"],
        params: "ReportsGetParams"
    ) -> "Report": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> AmazonSellerPartnerExecuteResult[Any] | AmazonSellerPartnerExecuteResultWithMeta[Any, Any] | Any: ...

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
                return AmazonSellerPartnerExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return AmazonSellerPartnerExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> AmazonSellerPartnerCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            AmazonSellerPartnerCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return AmazonSellerPartnerCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return AmazonSellerPartnerCheckResult(
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
            @AmazonSellerPartnerConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @AmazonSellerPartnerConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    AmazonSellerPartnerConnectorModel,
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
        return describe_entities(AmazonSellerPartnerConnectorModel)

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
            (e for e in AmazonSellerPartnerConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in AmazonSellerPartnerConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await AmazonSellerPartnerConnector.create(...)
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
        replication_config: "AmazonSellerPartnerReplicationConfig" | None = None,
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
            consent_url = await AmazonSellerPartnerConnector.get_consent_url(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                redirect_url="https://myapp.com/oauth/callback",
                name="My Amazon-Seller-Partner Source",
                replication_config=AmazonSellerPartnerReplicationConfig(replication_start_date="..."),
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
                definition_id=str(AmazonSellerPartnerConnectorModel.id),
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
        auth_config: "AmazonSellerPartnerAuthConfig" | None = None,
        server_side_oauth_secret_id: str | None = None,
        name: str | None = None,
        replication_config: "AmazonSellerPartnerReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "AmazonSellerPartnerConnector":
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
            A AmazonSellerPartnerConnector instance configured in hosted mode

        Raises:
            ValueError: If neither or both auth_config and server_side_oauth_secret_id provided

        Example:
            # Create a new hosted connector with API key auth
            connector = await AmazonSellerPartnerConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=AmazonSellerPartnerAuthConfig(lwa_app_id="...", lwa_client_secret="...", refresh_token="...", access_token="..."),
            )

            # With replication config (required for this connector):
            connector = await AmazonSellerPartnerConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=AmazonSellerPartnerAuthConfig(lwa_app_id="...", lwa_client_secret="...", refresh_token="...", access_token="..."),
                replication_config=AmazonSellerPartnerReplicationConfig(replication_start_date="..."),
            )

            # With server-side OAuth:
            connector = await AmazonSellerPartnerConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                server_side_oauth_secret_id="airbyte_oauth_..._secret_...",
                replication_config=AmazonSellerPartnerReplicationConfig(replication_start_date="..."),
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
                connector_definition_id=str(AmazonSellerPartnerConnectorModel.id),
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




class OrdersQuery:
    """
    Query class for Orders entity operations.
    """

    def __init__(self, connector: AmazonSellerPartnerConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        marketplace_ids: str,
        created_after: str | None = None,
        created_before: str | None = None,
        last_updated_after: str | None = None,
        last_updated_before: str | None = None,
        order_statuses: str | None = None,
        max_results_per_page: int | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> OrdersListResult:
        """
        Returns a list of orders based on the specified parameters.

        Args:
            marketplace_ids: A list of MarketplaceId values. Used to select orders placed in the specified marketplaces.
            created_after: A date used for selecting orders created after the specified date (ISO 8601 format). Required if LastUpdatedAfter is not set.
            created_before: A date used for selecting orders created before the specified date (ISO 8601 format).
            last_updated_after: A date used for selecting orders that were last updated after the specified date (ISO 8601 format).
            last_updated_before: A date used for selecting orders that were last updated before the specified date (ISO 8601 format).
            order_statuses: Filter by order status values.
            max_results_per_page: Maximum number of results to return per page.
            next_token: A string token returned in a previous response for pagination.
            **kwargs: Additional parameters

        Returns:
            OrdersListResult
        """
        params = {k: v for k, v in {
            "MarketplaceIds": marketplace_ids,
            "CreatedAfter": created_after,
            "CreatedBefore": created_before,
            "LastUpdatedAfter": last_updated_after,
            "LastUpdatedBefore": last_updated_before,
            "OrderStatuses": order_statuses,
            "MaxResultsPerPage": max_results_per_page,
            "NextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("orders", "list", params)
        # Cast generic envelope to concrete typed result
        return OrdersListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        order_id: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns the order indicated by the specified order ID.

        Args:
            order_id: An Amazon order identifier in 3-7-7 format.
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "orderId": order_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("orders", "get", params)
        return result



    async def search(
        self,
        query: OrdersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OrdersSearchResult:
        """
        Search orders records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OrdersSearchFilter):
        - amazon_order_id: Unique identifier for the Amazon order
        - automated_shipping_settings: Settings related to automated shipping processes
        - buyer_info: Information about the buyer
        - default_ship_from_location_address: The default address from which orders are shipped
        - earliest_delivery_date: Earliest estimated delivery date of the order
        - earliest_ship_date: Earliest shipment date for the order
        - fulfillment_channel: Channel through which the order is fulfilled
        - has_regulated_items: Indicates if the order has regulated items
        - is_access_point_order: Indicates if the order is an Amazon Hub Counter order
        - is_business_order: Indicates if the order is a business order
        - is_global_express_enabled: Indicates if global express is enabled for the order
        - is_ispu: Indicates if the order is for In-Store Pickup
        - is_premium_order: Indicates if the order is a premium order
        - is_prime: Indicates if the order is a Prime order
        - is_replacement_order: Indicates if the order is a replacement order
        - is_sold_by_ab: Indicates if the order is sold by Amazon Business
        - last_update_date: Date and time when the order was last updated
        - latest_delivery_date: Latest estimated delivery date of the order
        - latest_ship_date: Latest shipment date for the order
        - marketplace_id: Identifier for the marketplace where the order was placed
        - number_of_items_shipped: Number of items shipped in the order
        - number_of_items_unshipped: Number of items yet to be shipped in the order
        - order_status: Status of the order
        - order_total: Total amount of the order
        - order_type: Type of the order
        - payment_method: Payment method used for the order
        - payment_method_details: Details of the payment method used for the order
        - purchase_date: Date and time when the order was purchased
        - sales_channel: Channel through which the order was sold
        - seller_order_id: Unique identifier given by the seller for the order
        - ship_service_level: Service level for shipping the order
        - shipment_service_level_category: Service level category for shipping the order
        - shipping_address: The address to which the order will be shipped
        - seller_id: Identifier for the seller associated with the order

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OrdersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("orders", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OrdersSearchResult(
            data=[
                OrdersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class OrderItemsQuery:
    """
    Query class for OrderItems entity operations.
    """

    def __init__(self, connector: AmazonSellerPartnerConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        order_id: str,
        next_token: str | None = None,
        **kwargs
    ) -> OrderItemsListResult:
        """
        Returns detailed order item information for the order indicated by the specified order ID.

        Args:
            order_id: An Amazon order identifier in 3-7-7 format.
            next_token: A string token returned in a previous response for pagination.
            **kwargs: Additional parameters

        Returns:
            OrderItemsListResult
        """
        params = {k: v for k, v in {
            "orderId": order_id,
            "NextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("order_items", "list", params)
        # Cast generic envelope to concrete typed result
        return OrderItemsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: OrderItemsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OrderItemsSearchResult:
        """
        Search order_items records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OrderItemsSearchFilter):
        - asin: Amazon Standard Identification Number of the product
        - amazon_order_id: ID of the Amazon order
        - buyer_info: Information about the buyer
        - buyer_requested_cancel: Information about buyer's request for cancellation
        - cod_fee: Cash on delivery fee
        - cod_fee_discount: Discount on cash on delivery fee
        - condition_id: Condition ID of the product
        - condition_note: Additional notes on the condition of the product
        - condition_subtype_id: Subtype ID of the product condition
        - deemed_reseller_category: Category indicating if the seller is considered a reseller
        - ioss_number: Import One Stop Shop number
        - is_gift: Flag indicating if the order is a gift
        - is_transparency: Flag indicating if transparency is applied
        - item_price: Price of the item
        - item_tax: Tax applied on the item
        - last_update_date: Date and time of the last update
        - order_item_id: ID of the order item
        - points_granted: Points granted for the purchase
        - price_designation: Designation of the price
        - product_info: Information about the product
        - promotion_discount: Discount applied due to promotion
        - promotion_discount_tax: Tax applied on the promotion discount
        - promotion_ids: IDs of promotions applied
        - quantity_ordered: Quantity of the item ordered
        - quantity_shipped: Quantity of the item shipped
        - scheduled_delivery_end_date: End date for scheduled delivery
        - scheduled_delivery_start_date: Start date for scheduled delivery
        - seller_sku: SKU of the seller
        - serial_number_required: Flag indicating if serial number is required
        - serial_numbers: List of serial numbers
        - shipping_discount: Discount applied on shipping
        - shipping_discount_tax: Tax applied on the shipping discount
        - shipping_price: Price of shipping
        - shipping_tax: Tax applied on shipping
        - store_chain_store_id: ID of the store chain
        - tax_collection: Information about tax collection
        - title: Title of the product

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OrderItemsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("order_items", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OrderItemsSearchResult(
            data=[
                OrderItemsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ListFinancialEventGroupsQuery:
    """
    Query class for ListFinancialEventGroups entity operations.
    """

    def __init__(self, connector: AmazonSellerPartnerConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        financial_event_group_started_after: str | None = None,
        financial_event_group_started_before: str | None = None,
        max_results_per_page: int | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> ListFinancialEventGroupsListResult:
        """
        Returns financial event groups for a given date range.

        Args:
            financial_event_group_started_after: Return groups opened after this date (ISO 8601 format).
            financial_event_group_started_before: Return groups opened before this date (ISO 8601 format).
            max_results_per_page: Maximum number of results to return per page.
            next_token: A string token returned in a previous response for pagination.
            **kwargs: Additional parameters

        Returns:
            ListFinancialEventGroupsListResult
        """
        params = {k: v for k, v in {
            "FinancialEventGroupStartedAfter": financial_event_group_started_after,
            "FinancialEventGroupStartedBefore": financial_event_group_started_before,
            "MaxResultsPerPage": max_results_per_page,
            "NextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("list_financial_event_groups", "list", params)
        # Cast generic envelope to concrete typed result
        return ListFinancialEventGroupsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: ListFinancialEventGroupsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ListFinancialEventGroupsSearchResult:
        """
        Search list_financial_event_groups records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ListFinancialEventGroupsSearchFilter):
        - account_tail: The last digits of the account number
        - beginning_balance: Beginning balance
        - converted_total: Converted total
        - financial_event_group_end: End datetime of the financial event group
        - financial_event_group_id: Unique identifier for the financial event group
        - financial_event_group_start: Start datetime of the financial event group
        - fund_transfer_date: Date the fund transfer occurred
        - fund_transfer_status: Status of the fund transfer
        - original_total: Original total amount
        - processing_status: Processing status of the financial event group
        - trace_id: Unique identifier for tracing

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ListFinancialEventGroupsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("list_financial_event_groups", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ListFinancialEventGroupsSearchResult(
            data=[
                ListFinancialEventGroupsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ListFinancialEventsQuery:
    """
    Query class for ListFinancialEvents entity operations.
    """

    def __init__(self, connector: AmazonSellerPartnerConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        posted_after: str | None = None,
        posted_before: str | None = None,
        max_results_per_page: int | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> ListFinancialEventsListResult:
        """
        Returns financial events for a given date range.

        Args:
            posted_after: Return events posted after this date (ISO 8601 format).
            posted_before: Return events posted before this date (ISO 8601 format).
            max_results_per_page: Maximum number of results to return per page.
            next_token: A string token returned in a previous response for pagination.
            **kwargs: Additional parameters

        Returns:
            ListFinancialEventsListResult
        """
        params = {k: v for k, v in {
            "PostedAfter": posted_after,
            "PostedBefore": posted_before,
            "MaxResultsPerPage": max_results_per_page,
            "NextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("list_financial_events", "list", params)
        # Cast generic envelope to concrete typed result
        return ListFinancialEventsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: ListFinancialEventsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ListFinancialEventsSearchResult:
        """
        Search list_financial_events records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ListFinancialEventsSearchFilter):
        - adhoc_disbursement_event_list: List of adhoc disbursement events
        - adjustment_event_list: List of adjustment events
        - affordability_expense_event_list: List of affordability expense events
        - affordability_expense_reversal_event_list: List of affordability expense reversal events
        - capacity_reservation_billing_event_list: List of capacity reservation billing events
        - charge_refund_event_list: List of charge refund events
        - chargeback_event_list: List of chargeback events
        - coupon_payment_event_list: List of coupon payment events
        - debt_recovery_event_list: List of debt recovery events
        - fba_liquidation_event_list: List of FBA liquidation events
        - failed_adhoc_disbursement_event_list: List of failed adhoc disbursement events
        - guarantee_claim_event_list: List of guarantee claim events
        - imaging_services_fee_event_list: List of imaging services fee events
        - loan_servicing_event_list: List of loan servicing events
        - network_commingling_transaction_event_list: List of network commingling events
        - pay_with_amazon_event_list: List of Pay with Amazon events
        - performance_bond_refund_event_list: List of performance bond refund events
        - posted_before: Date filter for events posted before
        - product_ads_payment_event_list: List of product ads payment events
        - refund_event_list: List of refund events
        - removal_shipment_adjustment_event_list: List of removal shipment adjustment events
        - removal_shipment_event_list: List of removal shipment events
        - rental_transaction_event_list: List of rental transaction events
        - retrocharge_event_list: List of retrocharge events
        - safet_reimbursement_event_list: List of SAFET reimbursement events
        - seller_deal_payment_event_list: List of seller deal payment events
        - seller_review_enrollment_payment_event_list: List of seller review enrollment events
        - service_fee_event_list: List of service fee events
        - service_provider_credit_event_list: List of service provider credit events
        - shipment_event_list: List of shipment events
        - shipment_settle_event_list: List of shipment settlement events
        - tds_reimbursement_event_list: List of TDS reimbursement events
        - tax_withholding_event_list: List of tax withholding events
        - trial_shipment_event_list: List of trial shipment events
        - value_added_service_charge_event_list: List of value-added service charge events

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ListFinancialEventsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("list_financial_events", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ListFinancialEventsSearchResult(
            data=[
                ListFinancialEventsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CatalogItemsQuery:
    """
    Query class for CatalogItems entity operations.
    """

    def __init__(self, connector: AmazonSellerPartnerConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        marketplace_ids: str,
        keywords: str | None = None,
        identifiers: str | None = None,
        identifiers_type: str | None = None,
        included_data: str | None = None,
        page_size: int | None = None,
        page_token: str | None = None,
        **kwargs
    ) -> CatalogItemsListResult:
        """
        Search for items in the Amazon catalog by keywords or identifiers.

        Args:
            marketplace_ids: A marketplace identifier.
            keywords: Keywords to search for in the Amazon catalog.
            identifiers: Product identifiers to search for (ASIN, EAN, UPC, etc.).
            identifiers_type: Type of identifiers (required when identifiers is set).
            included_data: Data sets to include in the response.
            page_size: Number of items to return per page.
            page_token: Token for pagination returned by a previous request.
            **kwargs: Additional parameters

        Returns:
            CatalogItemsListResult
        """
        params = {k: v for k, v in {
            "marketplaceIds": marketplace_ids,
            "keywords": keywords,
            "identifiers": identifiers,
            "identifiersType": identifiers_type,
            "includedData": included_data,
            "pageSize": page_size,
            "pageToken": page_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("catalog_items", "list", params)
        # Cast generic envelope to concrete typed result
        return CatalogItemsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        asin: str,
        marketplace_ids: str,
        included_data: str | None = None,
        **kwargs
    ) -> CatalogItem:
        """
        Retrieves details for an item in the Amazon catalog by ASIN.

        Args:
            asin: The Amazon Standard Identification Number (ASIN) of the item.
            marketplace_ids: A marketplace identifier.
            included_data: Data sets to include in the response.
            **kwargs: Additional parameters

        Returns:
            CatalogItem
        """
        params = {k: v for k, v in {
            "asin": asin,
            "marketplaceIds": marketplace_ids,
            "includedData": included_data,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("catalog_items", "get", params)
        return result



class ReportsQuery:
    """
    Query class for Reports entity operations.
    """

    def __init__(self, connector: AmazonSellerPartnerConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        report_types: str | None = None,
        processing_statuses: str | None = None,
        marketplace_ids: str | None = None,
        page_size: int | None = None,
        created_since: str | None = None,
        created_until: str | None = None,
        next_token: str | None = None,
        **kwargs
    ) -> ReportsListResult:
        """
        Returns report details for the reports that match the specified filters.

        Args:
            report_types: A list of report types used to filter reports.
            processing_statuses: A list of processing statuses used to filter reports.
            marketplace_ids: A list of marketplace identifiers used to filter reports.
            page_size: Maximum number of reports to return per page.
            created_since: Earliest report creation date and time (ISO 8601 format).
            created_until: Latest report creation date and time (ISO 8601 format).
            next_token: A string token returned in a previous response for pagination.
            **kwargs: Additional parameters

        Returns:
            ReportsListResult
        """
        params = {k: v for k, v in {
            "reportTypes": report_types,
            "processingStatuses": processing_statuses,
            "marketplaceIds": marketplace_ids,
            "pageSize": page_size,
            "createdSince": created_since,
            "createdUntil": created_until,
            "nextToken": next_token,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("reports", "list", params)
        # Cast generic envelope to concrete typed result
        return ReportsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        report_id: str,
        **kwargs
    ) -> Report:
        """
        Returns report details including status and report document ID for a specified report.

        Args:
            report_id: The identifier for the report.
            **kwargs: Additional parameters

        Returns:
            Report
        """
        params = {k: v for k, v in {
            "reportId": report_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("reports", "get", params)
        return result


