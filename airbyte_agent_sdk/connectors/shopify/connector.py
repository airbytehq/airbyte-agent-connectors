"""
Shopify connector.
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

from .connector_model import ShopifyConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    AbandonedCheckoutsListParams,
    CollectsGetParams,
    CollectsListParams,
    CountriesGetParams,
    CountriesListParams,
    CustomCollectionsGetParams,
    CustomCollectionsListParams,
    CustomerAddressGetParams,
    CustomerAddressListParams,
    CustomersGetParams,
    CustomersListParams,
    DiscountCodesGetParams,
    DiscountCodesListParams,
    DraftOrdersGetParams,
    DraftOrdersListParams,
    FulfillmentOrdersGetParams,
    FulfillmentOrdersListParams,
    FulfillmentsGetParams,
    FulfillmentsListParams,
    InventoryItemsGetParams,
    InventoryItemsListParams,
    InventoryLevelsListParams,
    LocationsGetParams,
    LocationsListParams,
    MetafieldCustomersListParams,
    MetafieldDraftOrdersListParams,
    MetafieldLocationsListParams,
    MetafieldOrdersListParams,
    MetafieldProductImagesListParams,
    MetafieldProductVariantsListParams,
    MetafieldProductsListParams,
    MetafieldShopsGetParams,
    MetafieldShopsListParams,
    MetafieldSmartCollectionsListParams,
    OrderRefundsGetParams,
    OrderRefundsListParams,
    OrdersGetParams,
    OrdersListParams,
    PriceRulesGetParams,
    PriceRulesListParams,
    ProductImagesGetParams,
    ProductImagesListParams,
    ProductVariantsGetParams,
    ProductVariantsListParams,
    ProductsGetParams,
    ProductsListParams,
    ShopGetParams,
    SmartCollectionsGetParams,
    SmartCollectionsListParams,
    TenderTransactionsListParams,
    TransactionsGetParams,
    TransactionsListParams,
    AirbyteSearchParams,
    AbandonedCheckoutsSearchFilter,
    AbandonedCheckoutsSearchQuery,
    CollectsSearchFilter,
    CollectsSearchQuery,
    CountriesSearchFilter,
    CountriesSearchQuery,
    CustomCollectionsSearchFilter,
    CustomCollectionsSearchQuery,
    CustomersSearchFilter,
    CustomersSearchQuery,
    DiscountCodesSearchFilter,
    DiscountCodesSearchQuery,
    DraftOrdersSearchFilter,
    DraftOrdersSearchQuery,
    FulfillmentOrdersSearchFilter,
    FulfillmentOrdersSearchQuery,
    FulfillmentsSearchFilter,
    FulfillmentsSearchQuery,
    InventoryItemsSearchFilter,
    InventoryItemsSearchQuery,
    InventoryLevelsSearchFilter,
    InventoryLevelsSearchQuery,
    LocationsSearchFilter,
    LocationsSearchQuery,
    MetafieldCustomersSearchFilter,
    MetafieldCustomersSearchQuery,
    MetafieldDraftOrdersSearchFilter,
    MetafieldDraftOrdersSearchQuery,
    MetafieldLocationsSearchFilter,
    MetafieldLocationsSearchQuery,
    MetafieldOrdersSearchFilter,
    MetafieldOrdersSearchQuery,
    MetafieldProductImagesSearchFilter,
    MetafieldProductImagesSearchQuery,
    MetafieldProductVariantsSearchFilter,
    MetafieldProductVariantsSearchQuery,
    MetafieldProductsSearchFilter,
    MetafieldProductsSearchQuery,
    MetafieldShopsSearchFilter,
    MetafieldShopsSearchQuery,
    MetafieldSmartCollectionsSearchFilter,
    MetafieldSmartCollectionsSearchQuery,
    OrderRefundsSearchFilter,
    OrderRefundsSearchQuery,
    PriceRulesSearchFilter,
    PriceRulesSearchQuery,
    ProductImagesSearchFilter,
    ProductImagesSearchQuery,
    ProductVariantsSearchFilter,
    ProductVariantsSearchQuery,
    ShopSearchFilter,
    ShopSearchQuery,
    SmartCollectionsSearchFilter,
    SmartCollectionsSearchQuery,
    TenderTransactionsSearchFilter,
    TenderTransactionsSearchQuery,
)
from .models import ShopifyAuthConfig

# Import response models and envelope models at runtime
from .models import (
    ShopifyCheckResult,
    ShopifyExecuteResult,
    ShopifyExecuteResultWithMeta,
    CustomersListResult,
    OrdersListResult,
    ProductsListResult,
    ProductVariantsListResult,
    ProductImagesListResult,
    AbandonedCheckoutsListResult,
    LocationsListResult,
    InventoryLevelsListResult,
    InventoryItemsListResult,
    PriceRulesListResult,
    DiscountCodesListResult,
    CustomCollectionsListResult,
    SmartCollectionsListResult,
    CollectsListResult,
    DraftOrdersListResult,
    FulfillmentsListResult,
    OrderRefundsListResult,
    TransactionsListResult,
    TenderTransactionsListResult,
    CountriesListResult,
    MetafieldShopsListResult,
    MetafieldCustomersListResult,
    MetafieldProductsListResult,
    MetafieldOrdersListResult,
    MetafieldDraftOrdersListResult,
    MetafieldLocationsListResult,
    MetafieldProductVariantsListResult,
    MetafieldSmartCollectionsListResult,
    MetafieldProductImagesListResult,
    CustomerAddressListResult,
    FulfillmentOrdersListResult,
    AbandonedCheckout,
    Collect,
    Country,
    CustomCollection,
    Customer,
    CustomerAddress,
    DiscountCode,
    DraftOrder,
    Fulfillment,
    FulfillmentOrder,
    InventoryItem,
    InventoryLevel,
    Location,
    Metafield,
    Order,
    PriceRule,
    Product,
    ProductImage,
    ProductVariant,
    Refund,
    Shop,
    SmartCollection,
    TenderTransaction,
    Transaction,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AbandonedCheckoutsSearchData,
    AbandonedCheckoutsSearchResult,
    CollectsSearchData,
    CollectsSearchResult,
    CountriesSearchData,
    CountriesSearchResult,
    CustomCollectionsSearchData,
    CustomCollectionsSearchResult,
    CustomersSearchData,
    CustomersSearchResult,
    DiscountCodesSearchData,
    DiscountCodesSearchResult,
    DraftOrdersSearchData,
    DraftOrdersSearchResult,
    FulfillmentOrdersSearchData,
    FulfillmentOrdersSearchResult,
    FulfillmentsSearchData,
    FulfillmentsSearchResult,
    InventoryItemsSearchData,
    InventoryItemsSearchResult,
    InventoryLevelsSearchData,
    InventoryLevelsSearchResult,
    LocationsSearchData,
    LocationsSearchResult,
    MetafieldCustomersSearchData,
    MetafieldCustomersSearchResult,
    MetafieldDraftOrdersSearchData,
    MetafieldDraftOrdersSearchResult,
    MetafieldLocationsSearchData,
    MetafieldLocationsSearchResult,
    MetafieldOrdersSearchData,
    MetafieldOrdersSearchResult,
    MetafieldProductImagesSearchData,
    MetafieldProductImagesSearchResult,
    MetafieldProductVariantsSearchData,
    MetafieldProductVariantsSearchResult,
    MetafieldProductsSearchData,
    MetafieldProductsSearchResult,
    MetafieldShopsSearchData,
    MetafieldShopsSearchResult,
    MetafieldSmartCollectionsSearchData,
    MetafieldSmartCollectionsSearchResult,
    OrderRefundsSearchData,
    OrderRefundsSearchResult,
    PriceRulesSearchData,
    PriceRulesSearchResult,
    ProductImagesSearchData,
    ProductImagesSearchResult,
    ProductVariantsSearchData,
    ProductVariantsSearchResult,
    ShopSearchData,
    ShopSearchResult,
    SmartCollectionsSearchData,
    SmartCollectionsSearchResult,
    TenderTransactionsSearchData,
    TenderTransactionsSearchResult,
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




class ShopifyConnector:
    """
    Type-safe Shopify API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "shopify"
    connector_version = "0.1.12"
    sdk_version = "0.1.72"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("customers", "list"): True,
        ("customers", "get"): None,
        ("orders", "list"): True,
        ("orders", "get"): None,
        ("products", "list"): True,
        ("products", "get"): None,
        ("product_variants", "list"): True,
        ("product_variants", "get"): None,
        ("product_images", "list"): True,
        ("product_images", "get"): None,
        ("abandoned_checkouts", "list"): True,
        ("locations", "list"): True,
        ("locations", "get"): None,
        ("inventory_levels", "list"): True,
        ("inventory_items", "list"): True,
        ("inventory_items", "get"): None,
        ("shop", "get"): None,
        ("price_rules", "list"): True,
        ("price_rules", "get"): None,
        ("discount_codes", "list"): True,
        ("discount_codes", "get"): None,
        ("custom_collections", "list"): True,
        ("custom_collections", "get"): None,
        ("smart_collections", "list"): True,
        ("smart_collections", "get"): None,
        ("collects", "list"): True,
        ("collects", "get"): None,
        ("draft_orders", "list"): True,
        ("draft_orders", "get"): None,
        ("fulfillments", "list"): True,
        ("fulfillments", "get"): None,
        ("order_refunds", "list"): True,
        ("order_refunds", "get"): None,
        ("transactions", "list"): True,
        ("transactions", "get"): None,
        ("tender_transactions", "list"): True,
        ("countries", "list"): True,
        ("countries", "get"): None,
        ("metafield_shops", "list"): True,
        ("metafield_shops", "get"): None,
        ("metafield_customers", "list"): True,
        ("metafield_products", "list"): True,
        ("metafield_orders", "list"): True,
        ("metafield_draft_orders", "list"): True,
        ("metafield_locations", "list"): True,
        ("metafield_product_variants", "list"): True,
        ("metafield_smart_collections", "list"): True,
        ("metafield_product_images", "list"): True,
        ("customer_address", "list"): True,
        ("customer_address", "get"): None,
        ("fulfillment_orders", "list"): True,
        ("fulfillment_orders", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('customers', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'created_at_min': 'created_at_min', 'created_at_max': 'created_at_max', 'updated_at_min': 'updated_at_min', 'updated_at_max': 'updated_at_max'},
        ('customers', 'get'): {'customer_id': 'customer_id'},
        ('orders', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'created_at_min': 'created_at_min', 'created_at_max': 'created_at_max', 'updated_at_min': 'updated_at_min', 'updated_at_max': 'updated_at_max', 'status': 'status', 'financial_status': 'financial_status', 'fulfillment_status': 'fulfillment_status'},
        ('orders', 'get'): {'order_id': 'order_id'},
        ('products', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'created_at_min': 'created_at_min', 'created_at_max': 'created_at_max', 'updated_at_min': 'updated_at_min', 'updated_at_max': 'updated_at_max', 'status': 'status', 'product_type': 'product_type', 'vendor': 'vendor', 'collection_id': 'collection_id'},
        ('products', 'get'): {'product_id': 'product_id'},
        ('product_variants', 'list'): {'product_id': 'product_id', 'limit': 'limit', 'since_id': 'since_id'},
        ('product_variants', 'get'): {'variant_id': 'variant_id'},
        ('product_images', 'list'): {'product_id': 'product_id', 'since_id': 'since_id'},
        ('product_images', 'get'): {'product_id': 'product_id', 'image_id': 'image_id'},
        ('abandoned_checkouts', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'created_at_min': 'created_at_min', 'created_at_max': 'created_at_max', 'updated_at_min': 'updated_at_min', 'updated_at_max': 'updated_at_max', 'status': 'status'},
        ('locations', 'get'): {'location_id': 'location_id'},
        ('inventory_levels', 'list'): {'location_id': 'location_id', 'limit': 'limit'},
        ('inventory_items', 'list'): {'ids': 'ids', 'limit': 'limit'},
        ('inventory_items', 'get'): {'inventory_item_id': 'inventory_item_id'},
        ('price_rules', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'created_at_min': 'created_at_min', 'created_at_max': 'created_at_max', 'updated_at_min': 'updated_at_min', 'updated_at_max': 'updated_at_max'},
        ('price_rules', 'get'): {'price_rule_id': 'price_rule_id'},
        ('discount_codes', 'list'): {'price_rule_id': 'price_rule_id', 'limit': 'limit'},
        ('discount_codes', 'get'): {'price_rule_id': 'price_rule_id', 'discount_code_id': 'discount_code_id'},
        ('custom_collections', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'title': 'title', 'product_id': 'product_id', 'updated_at_min': 'updated_at_min', 'updated_at_max': 'updated_at_max'},
        ('custom_collections', 'get'): {'collection_id': 'collection_id'},
        ('smart_collections', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'title': 'title', 'product_id': 'product_id', 'updated_at_min': 'updated_at_min', 'updated_at_max': 'updated_at_max'},
        ('smart_collections', 'get'): {'collection_id': 'collection_id'},
        ('collects', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'collection_id': 'collection_id', 'product_id': 'product_id'},
        ('collects', 'get'): {'collect_id': 'collect_id'},
        ('draft_orders', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'status': 'status', 'updated_at_min': 'updated_at_min', 'updated_at_max': 'updated_at_max'},
        ('draft_orders', 'get'): {'draft_order_id': 'draft_order_id'},
        ('fulfillments', 'list'): {'order_id': 'order_id', 'limit': 'limit', 'since_id': 'since_id', 'created_at_min': 'created_at_min', 'created_at_max': 'created_at_max', 'updated_at_min': 'updated_at_min', 'updated_at_max': 'updated_at_max'},
        ('fulfillments', 'get'): {'order_id': 'order_id', 'fulfillment_id': 'fulfillment_id'},
        ('order_refunds', 'list'): {'order_id': 'order_id', 'limit': 'limit'},
        ('order_refunds', 'get'): {'order_id': 'order_id', 'refund_id': 'refund_id'},
        ('transactions', 'list'): {'order_id': 'order_id', 'since_id': 'since_id'},
        ('transactions', 'get'): {'order_id': 'order_id', 'transaction_id': 'transaction_id'},
        ('tender_transactions', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'processed_at_min': 'processed_at_min', 'processed_at_max': 'processed_at_max', 'order': 'order'},
        ('countries', 'list'): {'since_id': 'since_id'},
        ('countries', 'get'): {'country_id': 'country_id'},
        ('metafield_shops', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'namespace': 'namespace', 'key': 'key', 'type': 'type'},
        ('metafield_shops', 'get'): {'metafield_id': 'metafield_id'},
        ('metafield_customers', 'list'): {'customer_id': 'customer_id', 'limit': 'limit', 'since_id': 'since_id', 'namespace': 'namespace', 'key': 'key'},
        ('metafield_products', 'list'): {'product_id': 'product_id', 'limit': 'limit', 'since_id': 'since_id', 'namespace': 'namespace', 'key': 'key'},
        ('metafield_orders', 'list'): {'order_id': 'order_id', 'limit': 'limit', 'since_id': 'since_id', 'namespace': 'namespace', 'key': 'key'},
        ('metafield_draft_orders', 'list'): {'draft_order_id': 'draft_order_id', 'limit': 'limit', 'since_id': 'since_id', 'namespace': 'namespace', 'key': 'key'},
        ('metafield_locations', 'list'): {'location_id': 'location_id', 'limit': 'limit', 'since_id': 'since_id', 'namespace': 'namespace', 'key': 'key'},
        ('metafield_product_variants', 'list'): {'variant_id': 'variant_id', 'limit': 'limit', 'since_id': 'since_id', 'namespace': 'namespace', 'key': 'key'},
        ('metafield_smart_collections', 'list'): {'collection_id': 'collection_id', 'limit': 'limit', 'since_id': 'since_id', 'namespace': 'namespace', 'key': 'key'},
        ('metafield_product_images', 'list'): {'product_id': 'product_id', 'image_id': 'image_id', 'limit': 'limit', 'since_id': 'since_id', 'namespace': 'namespace', 'key': 'key'},
        ('customer_address', 'list'): {'customer_id': 'customer_id', 'limit': 'limit'},
        ('customer_address', 'get'): {'customer_id': 'customer_id', 'address_id': 'address_id'},
        ('fulfillment_orders', 'list'): {'order_id': 'order_id'},
        ('fulfillment_orders', 'get'): {'fulfillment_order_id': 'fulfillment_order_id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (ShopifyAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: ShopifyAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        shop: str | None = None    ):
        """
        Initialize a new shopify connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., ShopifyAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            shop: Your Shopify store name (e.g., 'my-store' from my-store.myshopify.com)
        Examples:
            # Local mode (direct API calls)
            connector = ShopifyConnector(auth_config=ShopifyAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = ShopifyConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = ShopifyConnector(
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
                connector_definition_id=str(ShopifyConnectorModel.id),
                model=ShopifyConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or ShopifyAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if shop:
                config_values["shop"] = shop

            self._executor = LocalExecutor(
                model=ShopifyConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if shop:
                base_url = base_url.replace("{shop}", shop)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.customers = CustomersQuery(self)
        self.orders = OrdersQuery(self)
        self.products = ProductsQuery(self)
        self.product_variants = ProductVariantsQuery(self)
        self.product_images = ProductImagesQuery(self)
        self.abandoned_checkouts = AbandonedCheckoutsQuery(self)
        self.locations = LocationsQuery(self)
        self.inventory_levels = InventoryLevelsQuery(self)
        self.inventory_items = InventoryItemsQuery(self)
        self.shop = ShopQuery(self)
        self.price_rules = PriceRulesQuery(self)
        self.discount_codes = DiscountCodesQuery(self)
        self.custom_collections = CustomCollectionsQuery(self)
        self.smart_collections = SmartCollectionsQuery(self)
        self.collects = CollectsQuery(self)
        self.draft_orders = DraftOrdersQuery(self)
        self.fulfillments = FulfillmentsQuery(self)
        self.order_refunds = OrderRefundsQuery(self)
        self.transactions = TransactionsQuery(self)
        self.tender_transactions = TenderTransactionsQuery(self)
        self.countries = CountriesQuery(self)
        self.metafield_shops = MetafieldShopsQuery(self)
        self.metafield_customers = MetafieldCustomersQuery(self)
        self.metafield_products = MetafieldProductsQuery(self)
        self.metafield_orders = MetafieldOrdersQuery(self)
        self.metafield_draft_orders = MetafieldDraftOrdersQuery(self)
        self.metafield_locations = MetafieldLocationsQuery(self)
        self.metafield_product_variants = MetafieldProductVariantsQuery(self)
        self.metafield_smart_collections = MetafieldSmartCollectionsQuery(self)
        self.metafield_product_images = MetafieldProductImagesQuery(self)
        self.customer_address = CustomerAddressQuery(self)
        self.fulfillment_orders = FulfillmentOrdersQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["customers"],
        action: Literal["list"],
        params: "CustomersListParams"
    ) -> "CustomersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["customers"],
        action: Literal["get"],
        params: "CustomersGetParams"
    ) -> "Customer": ...

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
    ) -> "Order": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["list"],
        params: "ProductsListParams"
    ) -> "ProductsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["get"],
        params: "ProductsGetParams"
    ) -> "Product": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_variants"],
        action: Literal["list"],
        params: "ProductVariantsListParams"
    ) -> "ProductVariantsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_variants"],
        action: Literal["get"],
        params: "ProductVariantsGetParams"
    ) -> "ProductVariant": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_images"],
        action: Literal["list"],
        params: "ProductImagesListParams"
    ) -> "ProductImagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_images"],
        action: Literal["get"],
        params: "ProductImagesGetParams"
    ) -> "ProductImage": ...

    @overload
    async def execute(
        self,
        entity: Literal["abandoned_checkouts"],
        action: Literal["list"],
        params: "AbandonedCheckoutsListParams"
    ) -> "AbandonedCheckoutsListResult": ...

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
        entity: Literal["locations"],
        action: Literal["get"],
        params: "LocationsGetParams"
    ) -> "Location": ...

    @overload
    async def execute(
        self,
        entity: Literal["inventory_levels"],
        action: Literal["list"],
        params: "InventoryLevelsListParams"
    ) -> "InventoryLevelsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["inventory_items"],
        action: Literal["list"],
        params: "InventoryItemsListParams"
    ) -> "InventoryItemsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["inventory_items"],
        action: Literal["get"],
        params: "InventoryItemsGetParams"
    ) -> "InventoryItem": ...

    @overload
    async def execute(
        self,
        entity: Literal["shop"],
        action: Literal["get"],
        params: "ShopGetParams"
    ) -> "Shop": ...

    @overload
    async def execute(
        self,
        entity: Literal["price_rules"],
        action: Literal["list"],
        params: "PriceRulesListParams"
    ) -> "PriceRulesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["price_rules"],
        action: Literal["get"],
        params: "PriceRulesGetParams"
    ) -> "PriceRule": ...

    @overload
    async def execute(
        self,
        entity: Literal["discount_codes"],
        action: Literal["list"],
        params: "DiscountCodesListParams"
    ) -> "DiscountCodesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["discount_codes"],
        action: Literal["get"],
        params: "DiscountCodesGetParams"
    ) -> "DiscountCode": ...

    @overload
    async def execute(
        self,
        entity: Literal["custom_collections"],
        action: Literal["list"],
        params: "CustomCollectionsListParams"
    ) -> "CustomCollectionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["custom_collections"],
        action: Literal["get"],
        params: "CustomCollectionsGetParams"
    ) -> "CustomCollection": ...

    @overload
    async def execute(
        self,
        entity: Literal["smart_collections"],
        action: Literal["list"],
        params: "SmartCollectionsListParams"
    ) -> "SmartCollectionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["smart_collections"],
        action: Literal["get"],
        params: "SmartCollectionsGetParams"
    ) -> "SmartCollection": ...

    @overload
    async def execute(
        self,
        entity: Literal["collects"],
        action: Literal["list"],
        params: "CollectsListParams"
    ) -> "CollectsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["collects"],
        action: Literal["get"],
        params: "CollectsGetParams"
    ) -> "Collect": ...

    @overload
    async def execute(
        self,
        entity: Literal["draft_orders"],
        action: Literal["list"],
        params: "DraftOrdersListParams"
    ) -> "DraftOrdersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["draft_orders"],
        action: Literal["get"],
        params: "DraftOrdersGetParams"
    ) -> "DraftOrder": ...

    @overload
    async def execute(
        self,
        entity: Literal["fulfillments"],
        action: Literal["list"],
        params: "FulfillmentsListParams"
    ) -> "FulfillmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["fulfillments"],
        action: Literal["get"],
        params: "FulfillmentsGetParams"
    ) -> "Fulfillment": ...

    @overload
    async def execute(
        self,
        entity: Literal["order_refunds"],
        action: Literal["list"],
        params: "OrderRefundsListParams"
    ) -> "OrderRefundsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["order_refunds"],
        action: Literal["get"],
        params: "OrderRefundsGetParams"
    ) -> "Refund": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactions"],
        action: Literal["list"],
        params: "TransactionsListParams"
    ) -> "TransactionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactions"],
        action: Literal["get"],
        params: "TransactionsGetParams"
    ) -> "Transaction": ...

    @overload
    async def execute(
        self,
        entity: Literal["tender_transactions"],
        action: Literal["list"],
        params: "TenderTransactionsListParams"
    ) -> "TenderTransactionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["countries"],
        action: Literal["list"],
        params: "CountriesListParams"
    ) -> "CountriesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["countries"],
        action: Literal["get"],
        params: "CountriesGetParams"
    ) -> "Country": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_shops"],
        action: Literal["list"],
        params: "MetafieldShopsListParams"
    ) -> "MetafieldShopsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_shops"],
        action: Literal["get"],
        params: "MetafieldShopsGetParams"
    ) -> "Metafield": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_customers"],
        action: Literal["list"],
        params: "MetafieldCustomersListParams"
    ) -> "MetafieldCustomersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_products"],
        action: Literal["list"],
        params: "MetafieldProductsListParams"
    ) -> "MetafieldProductsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_orders"],
        action: Literal["list"],
        params: "MetafieldOrdersListParams"
    ) -> "MetafieldOrdersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_draft_orders"],
        action: Literal["list"],
        params: "MetafieldDraftOrdersListParams"
    ) -> "MetafieldDraftOrdersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_locations"],
        action: Literal["list"],
        params: "MetafieldLocationsListParams"
    ) -> "MetafieldLocationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_product_variants"],
        action: Literal["list"],
        params: "MetafieldProductVariantsListParams"
    ) -> "MetafieldProductVariantsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_smart_collections"],
        action: Literal["list"],
        params: "MetafieldSmartCollectionsListParams"
    ) -> "MetafieldSmartCollectionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_product_images"],
        action: Literal["list"],
        params: "MetafieldProductImagesListParams"
    ) -> "MetafieldProductImagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["customer_address"],
        action: Literal["list"],
        params: "CustomerAddressListParams"
    ) -> "CustomerAddressListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["customer_address"],
        action: Literal["get"],
        params: "CustomerAddressGetParams"
    ) -> "CustomerAddress": ...

    @overload
    async def execute(
        self,
        entity: Literal["fulfillment_orders"],
        action: Literal["list"],
        params: "FulfillmentOrdersListParams"
    ) -> "FulfillmentOrdersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["fulfillment_orders"],
        action: Literal["get"],
        params: "FulfillmentOrdersGetParams"
    ) -> "FulfillmentOrder": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "context_store_search"],
        params: Mapping[str, Any]
    ) -> ShopifyExecuteResult[Any] | ShopifyExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "context_store_search"],
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
                return ShopifyExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return ShopifyExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> ShopifyCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            ShopifyCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return ShopifyCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return ShopifyCheckResult(
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
    ) -> _F | Callable[[_F], _F]:
        """
        Decorator that adds tool utilities like docstring augmentation and output limits.

        Usage:
            @mcp.tool()
            @ShopifyConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @ShopifyConnector.tool_utils(update_docstring=False, max_output_chars=None)
            async def execute(entity: str, action: str, params: dict):
                ...

        Args:
            update_docstring: When True, append connector capabilities to __doc__.
            max_output_chars: Max serialized output size before raising. Use None to disable.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    ShopifyConnectorModel,
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
        return describe_entities(ShopifyConnectorModel)

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
            (e for e in ShopifyConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in ShopifyConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await ShopifyConnector.create(...)
            print(f"Created connector: {connector.connector_id}")
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

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def create(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        auth_config: "ShopifyAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
        source_template_id: str | None = None,
    ) -> "ShopifyConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and workspace_name.
                Optionally include organization_id for multi-org request routing.
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + workspace_name)
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A ShopifyConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await ShopifyConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    workspace_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=ShopifyAuthConfig(api_key="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.workspace_name:
            raise ValueError("airbyte_config.workspace_name is required for create()")


        from airbyte_agent_sdk.cloud_utils import AirbyteCloudClient
        from airbyte_agent_sdk.types import AirbyteAuthConfig as _AirbyteAuthConfig

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
            source_name = name or f"{cls.connector_name} - {airbyte_config.workspace_name}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(ShopifyConnectorModel.id),
                workspace_name=airbyte_config.workspace_name,
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




class CustomersQuery:
    """
    Query class for Customers entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        created_at_min: str | None = None,
        created_at_max: str | None = None,
        updated_at_min: str | None = None,
        updated_at_max: str | None = None,
        **kwargs
    ) -> CustomersListResult:
        """
        Returns a list of customers from the store

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            created_at_min: Show customers created after date (ISO 8601 format)
            created_at_max: Show customers created before date (ISO 8601 format)
            updated_at_min: Show customers last updated after date (ISO 8601 format)
            updated_at_max: Show customers last updated before date (ISO 8601 format)
            **kwargs: Additional parameters

        Returns:
            CustomersListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "created_at_min": created_at_min,
            "created_at_max": created_at_max,
            "updated_at_min": updated_at_min,
            "updated_at_max": updated_at_max,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "list", params)
        # Cast generic envelope to concrete typed result
        return CustomersListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        customer_id: str,
        **kwargs
    ) -> Customer:
        """
        Retrieves a single customer by ID

        Args:
            customer_id: The customer ID
            **kwargs: Additional parameters

        Returns:
            Customer
        """
        params = {k: v for k, v in {
            "customer_id": customer_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "get", params)
        return result



    async def context_store_search(
        self,
        query: CustomersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CustomersSearchResult:
        """
        Search customers records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CustomersSearchFilter):
        - id: Unique identifier for the customer
        - email: Primary email address of the customer
        - phone: Primary phone number of the customer
        - first_name: First name of the customer
        - last_name: Last name of the customer
        - state: Account state (`disabled`, `invited`, `enabled`, `declined`)
        - orders_count: Number of orders placed by the customer
        - total_spent: Total lifetime amount spent by the customer
        - currency: ISO 4217 currency code for the customer's total spend
        - created_at: ISO 8601 timestamp when the customer record was created
        - updated_at: ISO 8601 timestamp when the customer record was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CustomersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("customers", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CustomersSearchResult(
            data=[
                CustomersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class OrdersQuery:
    """
    Query class for Orders entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        created_at_min: str | None = None,
        created_at_max: str | None = None,
        updated_at_min: str | None = None,
        updated_at_max: str | None = None,
        status: str | None = None,
        financial_status: str | None = None,
        fulfillment_status: str | None = None,
        **kwargs
    ) -> OrdersListResult:
        """
        Returns a list of orders from the store

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            created_at_min: Show orders created after date (ISO 8601 format)
            created_at_max: Show orders created before date (ISO 8601 format)
            updated_at_min: Show orders last updated after date (ISO 8601 format)
            updated_at_max: Show orders last updated before date (ISO 8601 format)
            status: Filter orders by status
            financial_status: Filter orders by financial status
            fulfillment_status: Filter orders by fulfillment status
            **kwargs: Additional parameters

        Returns:
            OrdersListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "created_at_min": created_at_min,
            "created_at_max": created_at_max,
            "updated_at_min": updated_at_min,
            "updated_at_max": updated_at_max,
            "status": status,
            "financial_status": financial_status,
            "fulfillment_status": fulfillment_status,
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
    ) -> Order:
        """
        Retrieves a single order by ID

        Args:
            order_id: The order ID
            **kwargs: Additional parameters

        Returns:
            Order
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("orders", "get", params)
        return result



class ProductsQuery:
    """
    Query class for Products entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        created_at_min: str | None = None,
        created_at_max: str | None = None,
        updated_at_min: str | None = None,
        updated_at_max: str | None = None,
        status: str | None = None,
        product_type: str | None = None,
        vendor: str | None = None,
        collection_id: int | None = None,
        **kwargs
    ) -> ProductsListResult:
        """
        Returns a list of products from the store

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            created_at_min: Show products created after date (ISO 8601 format)
            created_at_max: Show products created before date (ISO 8601 format)
            updated_at_min: Show products last updated after date (ISO 8601 format)
            updated_at_max: Show products last updated before date (ISO 8601 format)
            status: Filter products by status
            product_type: Filter by product type
            vendor: Filter by vendor
            collection_id: Filter by collection ID
            **kwargs: Additional parameters

        Returns:
            ProductsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "created_at_min": created_at_min,
            "created_at_max": created_at_max,
            "updated_at_min": updated_at_min,
            "updated_at_max": updated_at_max,
            "status": status,
            "product_type": product_type,
            "vendor": vendor,
            "collection_id": collection_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "list", params)
        # Cast generic envelope to concrete typed result
        return ProductsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        product_id: str,
        **kwargs
    ) -> Product:
        """
        Retrieves a single product by ID

        Args:
            product_id: The product ID
            **kwargs: Additional parameters

        Returns:
            Product
        """
        params = {k: v for k, v in {
            "product_id": product_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "get", params)
        return result



class ProductVariantsQuery:
    """
    Query class for ProductVariants entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        product_id: str,
        limit: int | None = None,
        since_id: int | None = None,
        **kwargs
    ) -> ProductVariantsListResult:
        """
        Returns a list of variants for a product

        Args:
            product_id: The product ID
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            **kwargs: Additional parameters

        Returns:
            ProductVariantsListResult
        """
        params = {k: v for k, v in {
            "product_id": product_id,
            "limit": limit,
            "since_id": since_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_variants", "list", params)
        # Cast generic envelope to concrete typed result
        return ProductVariantsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        variant_id: str,
        **kwargs
    ) -> ProductVariant:
        """
        Retrieves a single product variant by ID

        Args:
            variant_id: The variant ID
            **kwargs: Additional parameters

        Returns:
            ProductVariant
        """
        params = {k: v for k, v in {
            "variant_id": variant_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_variants", "get", params)
        return result



    async def context_store_search(
        self,
        query: ProductVariantsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProductVariantsSearchResult:
        """
        Search product_variants records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProductVariantsSearchFilter):
        - id: Unique identifier for the product variant
        - product_id: Identifier of the parent product
        - title: Display title of the variant
        - sku: Stock keeping unit for the variant
        - price: Price of the variant in the shop's currency
        - compare_at_price: Original (compare-at) price of the variant, if set
        - position: Display position of the variant within the product
        - inventory_policy: Behaviour when out of stock (`deny` or `continue`)
        - created_at: ISO 8601 timestamp when the variant was created
        - updated_at: ISO 8601 timestamp when the variant was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProductVariantsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("product_variants", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProductVariantsSearchResult(
            data=[
                ProductVariantsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ProductImagesQuery:
    """
    Query class for ProductImages entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        product_id: str,
        since_id: int | None = None,
        **kwargs
    ) -> ProductImagesListResult:
        """
        Returns a list of images for a product

        Args:
            product_id: The product ID
            since_id: Restrict results to after the specified ID
            **kwargs: Additional parameters

        Returns:
            ProductImagesListResult
        """
        params = {k: v for k, v in {
            "product_id": product_id,
            "since_id": since_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_images", "list", params)
        # Cast generic envelope to concrete typed result
        return ProductImagesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        product_id: str,
        image_id: str,
        **kwargs
    ) -> ProductImage:
        """
        Retrieves a single product image by ID

        Args:
            product_id: The product ID
            image_id: The image ID
            **kwargs: Additional parameters

        Returns:
            ProductImage
        """
        params = {k: v for k, v in {
            "product_id": product_id,
            "image_id": image_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_images", "get", params)
        return result



    async def context_store_search(
        self,
        query: ProductImagesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProductImagesSearchResult:
        """
        Search product_images records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProductImagesSearchFilter):
        - id: Unique identifier for the product image
        - product_id: Identifier of the product the image belongs to
        - position: Display position of the image within the product
        - alt: Alt text for the image
        - width: Image width in pixels
        - height: Image height in pixels
        - src: Public URL of the image
        - created_at: ISO 8601 timestamp when the image was created
        - updated_at: ISO 8601 timestamp when the image was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProductImagesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("product_images", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProductImagesSearchResult(
            data=[
                ProductImagesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AbandonedCheckoutsQuery:
    """
    Query class for AbandonedCheckouts entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        created_at_min: str | None = None,
        created_at_max: str | None = None,
        updated_at_min: str | None = None,
        updated_at_max: str | None = None,
        status: str | None = None,
        **kwargs
    ) -> AbandonedCheckoutsListResult:
        """
        Returns a list of abandoned checkouts

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            created_at_min: Show checkouts created after date (ISO 8601 format)
            created_at_max: Show checkouts created before date (ISO 8601 format)
            updated_at_min: Show checkouts last updated after date (ISO 8601 format)
            updated_at_max: Show checkouts last updated before date (ISO 8601 format)
            status: Filter checkouts by status
            **kwargs: Additional parameters

        Returns:
            AbandonedCheckoutsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "created_at_min": created_at_min,
            "created_at_max": created_at_max,
            "updated_at_min": updated_at_min,
            "updated_at_max": updated_at_max,
            "status": status,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("abandoned_checkouts", "list", params)
        # Cast generic envelope to concrete typed result
        return AbandonedCheckoutsListResult(
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: AbandonedCheckoutsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AbandonedCheckoutsSearchResult:
        """
        Search abandoned_checkouts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AbandonedCheckoutsSearchFilter):
        - id: Unique identifier for the abandoned checkout
        - token: Unique token identifying the checkout
        - email: Email address provided for the checkout
        - phone: Phone number provided for the checkout
        - name: Shopify-assigned display name for the checkout (e.g. `#C12345`)
        - currency: ISO 4217 currency code for the checkout totals
        - total_price: Total price of the checkout in the shop's currency
        - created_at: ISO 8601 timestamp when the checkout was created
        - updated_at: ISO 8601 timestamp when the checkout was last updated
        - completed_at: ISO 8601 timestamp when the checkout was completed, if applicable

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AbandonedCheckoutsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("abandoned_checkouts", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AbandonedCheckoutsSearchResult(
            data=[
                AbandonedCheckoutsSearchData(**row)
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

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> LocationsListResult:
        """
        Returns a list of locations for the store

        Returns:
            LocationsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("locations", "list", params)
        # Cast generic envelope to concrete typed result
        return LocationsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        location_id: str,
        **kwargs
    ) -> Location:
        """
        Retrieves a single location by ID

        Args:
            location_id: The location ID
            **kwargs: Additional parameters

        Returns:
            Location
        """
        params = {k: v for k, v in {
            "location_id": location_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("locations", "get", params)
        return result



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
        - id: Unique identifier for the location
        - name: Display name of the location
        - address1: Primary street address of the location
        - city: City of the location
        - province: Province, state, or region of the location
        - country: Country name of the location
        - country_code: ISO 3166-1 alpha-2 country code of the location
        - phone: Phone number for the location
        - active: Whether the location is currently active
        - created_at: ISO 8601 timestamp when the location was created
        - updated_at: ISO 8601 timestamp when the location was last updated

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

class InventoryLevelsQuery:
    """
    Query class for InventoryLevels entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        location_id: str,
        limit: int | None = None,
        **kwargs
    ) -> InventoryLevelsListResult:
        """
        Returns a list of inventory levels for a specific location

        Args:
            location_id: The location ID
            limit: Maximum number of results to return (max 250)
            **kwargs: Additional parameters

        Returns:
            InventoryLevelsListResult
        """
        params = {k: v for k, v in {
            "location_id": location_id,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("inventory_levels", "list", params)
        # Cast generic envelope to concrete typed result
        return InventoryLevelsListResult(
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: InventoryLevelsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> InventoryLevelsSearchResult:
        """
        Search inventory_levels records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (InventoryLevelsSearchFilter):
        - inventory_item_id: Identifier of the inventory item
        - location_id: Identifier of the location holding the inventory
        - available: Number of units available at the location
        - updated_at: ISO 8601 timestamp when the inventory level was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            InventoryLevelsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("inventory_levels", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return InventoryLevelsSearchResult(
            data=[
                InventoryLevelsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class InventoryItemsQuery:
    """
    Query class for InventoryItems entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        ids: str,
        limit: int | None = None,
        **kwargs
    ) -> InventoryItemsListResult:
        """
        Returns a list of inventory items

        Args:
            ids: Comma-separated list of inventory item IDs
            limit: Maximum number of results to return (max 250)
            **kwargs: Additional parameters

        Returns:
            InventoryItemsListResult
        """
        params = {k: v for k, v in {
            "ids": ids,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("inventory_items", "list", params)
        # Cast generic envelope to concrete typed result
        return InventoryItemsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        inventory_item_id: str,
        **kwargs
    ) -> InventoryItem:
        """
        Retrieves a single inventory item by ID

        Args:
            inventory_item_id: The inventory item ID
            **kwargs: Additional parameters

        Returns:
            InventoryItem
        """
        params = {k: v for k, v in {
            "inventory_item_id": inventory_item_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("inventory_items", "get", params)
        return result



    async def context_store_search(
        self,
        query: InventoryItemsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> InventoryItemsSearchResult:
        """
        Search inventory_items records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (InventoryItemsSearchFilter):
        - id: Unique identifier for the inventory item
        - sku: Stock keeping unit associated with the inventory item
        - tracked: Whether Shopify is tracking inventory for this item
        - requires_shipping: Whether the item requires shipping
        - country_code_of_origin: ISO country code of the item's country of origin
        - created_at: ISO 8601 timestamp when the inventory item was created
        - updated_at: ISO 8601 timestamp when the inventory item was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            InventoryItemsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("inventory_items", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return InventoryItemsSearchResult(
            data=[
                InventoryItemsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ShopQuery:
    """
    Query class for Shop entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        **kwargs
    ) -> Shop:
        """
        Retrieves the shop's configuration

        Returns:
            Shop
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("shop", "get", params)
        return result



    async def context_store_search(
        self,
        query: ShopSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ShopSearchResult:
        """
        Search shop records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ShopSearchFilter):
        - id: Unique identifier for the shop
        - name: Display name of the shop
        - email: Primary contact email for the shop
        - domain: Custom domain configured for the shop, if any
        - myshopify_domain: Canonical `*.myshopify.com` domain for the shop
        - country_code: ISO 3166-1 alpha-2 country code of the shop
        - currency: ISO 4217 currency code used by the shop
        - timezone: Timezone configured for the shop (e.g. `(GMT-05:00) Eastern Time`)
        - plan_name: Shopify plan identifier (e.g. `shopify_plus`, `basic`)
        - created_at: ISO 8601 timestamp when the shop was created
        - updated_at: ISO 8601 timestamp when the shop was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ShopSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("shop", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ShopSearchResult(
            data=[
                ShopSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class PriceRulesQuery:
    """
    Query class for PriceRules entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        created_at_min: str | None = None,
        created_at_max: str | None = None,
        updated_at_min: str | None = None,
        updated_at_max: str | None = None,
        **kwargs
    ) -> PriceRulesListResult:
        """
        Returns a list of price rules

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            created_at_min: Show price rules created after date (ISO 8601 format)
            created_at_max: Show price rules created before date (ISO 8601 format)
            updated_at_min: Show price rules last updated after date (ISO 8601 format)
            updated_at_max: Show price rules last updated before date (ISO 8601 format)
            **kwargs: Additional parameters

        Returns:
            PriceRulesListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "created_at_min": created_at_min,
            "created_at_max": created_at_max,
            "updated_at_min": updated_at_min,
            "updated_at_max": updated_at_max,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("price_rules", "list", params)
        # Cast generic envelope to concrete typed result
        return PriceRulesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        price_rule_id: str,
        **kwargs
    ) -> PriceRule:
        """
        Retrieves a single price rule by ID

        Args:
            price_rule_id: The price rule ID
            **kwargs: Additional parameters

        Returns:
            PriceRule
        """
        params = {k: v for k, v in {
            "price_rule_id": price_rule_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("price_rules", "get", params)
        return result



    async def context_store_search(
        self,
        query: PriceRulesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> PriceRulesSearchResult:
        """
        Search price_rules records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (PriceRulesSearchFilter):
        - id: Unique identifier for the price rule
        - title: Administrative title of the price rule
        - value_type: How the discount value is interpreted (`fixed_amount` or `percentage`)
        - value: Discount value applied by the rule
        - target_type: Type of target the rule applies to (`line_item` or `shipping_line`)
        - target_selection: Which target items the rule applies to (`all` or `entitled`)
        - allocation_method: How the discount is allocated (`each` or `across`)
        - starts_at: ISO 8601 timestamp when the rule starts being active
        - ends_at: ISO 8601 timestamp when the rule stops being active, if applicable
        - created_at: ISO 8601 timestamp when the rule was created
        - updated_at: ISO 8601 timestamp when the rule was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            PriceRulesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("price_rules", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return PriceRulesSearchResult(
            data=[
                PriceRulesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class DiscountCodesQuery:
    """
    Query class for DiscountCodes entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        price_rule_id: str,
        limit: int | None = None,
        **kwargs
    ) -> DiscountCodesListResult:
        """
        Returns a list of discount codes for a price rule

        Args:
            price_rule_id: The price rule ID
            limit: Maximum number of results to return (max 250)
            **kwargs: Additional parameters

        Returns:
            DiscountCodesListResult
        """
        params = {k: v for k, v in {
            "price_rule_id": price_rule_id,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("discount_codes", "list", params)
        # Cast generic envelope to concrete typed result
        return DiscountCodesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        price_rule_id: str,
        discount_code_id: str,
        **kwargs
    ) -> DiscountCode:
        """
        Retrieves a single discount code by ID

        Args:
            price_rule_id: The price rule ID
            discount_code_id: The discount code ID
            **kwargs: Additional parameters

        Returns:
            DiscountCode
        """
        params = {k: v for k, v in {
            "price_rule_id": price_rule_id,
            "discount_code_id": discount_code_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("discount_codes", "get", params)
        return result



    async def context_store_search(
        self,
        query: DiscountCodesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DiscountCodesSearchResult:
        """
        Search discount_codes records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DiscountCodesSearchFilter):
        - id: Unique identifier for the discount code
        - price_rule_id: Identifier of the parent price rule
        - code: Discount code string shoppers enter at checkout
        - usage_count: Number of times the code has been redeemed
        - created_at: ISO 8601 timestamp when the code was created
        - updated_at: ISO 8601 timestamp when the code was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DiscountCodesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("discount_codes", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DiscountCodesSearchResult(
            data=[
                DiscountCodesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CustomCollectionsQuery:
    """
    Query class for CustomCollections entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        title: str | None = None,
        product_id: int | None = None,
        updated_at_min: str | None = None,
        updated_at_max: str | None = None,
        **kwargs
    ) -> CustomCollectionsListResult:
        """
        Returns a list of custom collections

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            title: Filter by collection title
            product_id: Filter by product ID
            updated_at_min: Show collections last updated after date (ISO 8601 format)
            updated_at_max: Show collections last updated before date (ISO 8601 format)
            **kwargs: Additional parameters

        Returns:
            CustomCollectionsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "title": title,
            "product_id": product_id,
            "updated_at_min": updated_at_min,
            "updated_at_max": updated_at_max,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("custom_collections", "list", params)
        # Cast generic envelope to concrete typed result
        return CustomCollectionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        collection_id: str,
        **kwargs
    ) -> CustomCollection:
        """
        Retrieves a single custom collection by ID

        Args:
            collection_id: The collection ID
            **kwargs: Additional parameters

        Returns:
            CustomCollection
        """
        params = {k: v for k, v in {
            "collection_id": collection_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("custom_collections", "get", params)
        return result



    async def context_store_search(
        self,
        query: CustomCollectionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CustomCollectionsSearchResult:
        """
        Search custom_collections records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CustomCollectionsSearchFilter):
        - id: Unique identifier for the custom collection
        - handle: URL-friendly handle for the custom collection
        - title: Display title of the custom collection
        - sort_order: How products are sorted within the collection (e.g. `best-selling`)
        - published_scope: Publishing scope (`web` or `global`)
        - published_at: ISO 8601 timestamp when the collection was published
        - updated_at: ISO 8601 timestamp when the collection was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CustomCollectionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("custom_collections", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CustomCollectionsSearchResult(
            data=[
                CustomCollectionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SmartCollectionsQuery:
    """
    Query class for SmartCollections entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        title: str | None = None,
        product_id: int | None = None,
        updated_at_min: str | None = None,
        updated_at_max: str | None = None,
        **kwargs
    ) -> SmartCollectionsListResult:
        """
        Returns a list of smart collections

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            title: Filter by collection title
            product_id: Filter by product ID
            updated_at_min: Show collections last updated after date (ISO 8601 format)
            updated_at_max: Show collections last updated before date (ISO 8601 format)
            **kwargs: Additional parameters

        Returns:
            SmartCollectionsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "title": title,
            "product_id": product_id,
            "updated_at_min": updated_at_min,
            "updated_at_max": updated_at_max,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("smart_collections", "list", params)
        # Cast generic envelope to concrete typed result
        return SmartCollectionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        collection_id: str,
        **kwargs
    ) -> SmartCollection:
        """
        Retrieves a single smart collection by ID

        Args:
            collection_id: The collection ID
            **kwargs: Additional parameters

        Returns:
            SmartCollection
        """
        params = {k: v for k, v in {
            "collection_id": collection_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("smart_collections", "get", params)
        return result



    async def context_store_search(
        self,
        query: SmartCollectionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SmartCollectionsSearchResult:
        """
        Search smart_collections records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SmartCollectionsSearchFilter):
        - id: Unique identifier for the smart collection
        - handle: URL-friendly handle for the smart collection
        - title: Display title of the smart collection
        - sort_order: How products are sorted within the collection
        - published_scope: Publishing scope (`web` or `global`)
        - published_at: ISO 8601 timestamp when the collection was published
        - updated_at: ISO 8601 timestamp when the collection was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SmartCollectionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("smart_collections", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SmartCollectionsSearchResult(
            data=[
                SmartCollectionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CollectsQuery:
    """
    Query class for Collects entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        collection_id: int | None = None,
        product_id: int | None = None,
        **kwargs
    ) -> CollectsListResult:
        """
        Returns a list of collects (links between products and collections)

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            collection_id: Filter by collection ID
            product_id: Filter by product ID
            **kwargs: Additional parameters

        Returns:
            CollectsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "collection_id": collection_id,
            "product_id": product_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("collects", "list", params)
        # Cast generic envelope to concrete typed result
        return CollectsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        collect_id: str,
        **kwargs
    ) -> Collect:
        """
        Retrieves a single collect by ID

        Args:
            collect_id: The collect ID
            **kwargs: Additional parameters

        Returns:
            Collect
        """
        params = {k: v for k, v in {
            "collect_id": collect_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("collects", "get", params)
        return result



    async def context_store_search(
        self,
        query: CollectsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CollectsSearchResult:
        """
        Search collects records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CollectsSearchFilter):
        - id: Unique identifier for the collect
        - collection_id: Identifier of the collection the product belongs to
        - product_id: Identifier of the product in the collection
        - position: Position of the product within the collection
        - created_at: ISO 8601 timestamp when the collect was created
        - updated_at: ISO 8601 timestamp when the collect was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CollectsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("collects", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CollectsSearchResult(
            data=[
                CollectsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class DraftOrdersQuery:
    """
    Query class for DraftOrders entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        status: str | None = None,
        updated_at_min: str | None = None,
        updated_at_max: str | None = None,
        **kwargs
    ) -> DraftOrdersListResult:
        """
        Returns a list of draft orders

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            status: Filter draft orders by status
            updated_at_min: Show draft orders last updated after date (ISO 8601 format)
            updated_at_max: Show draft orders last updated before date (ISO 8601 format)
            **kwargs: Additional parameters

        Returns:
            DraftOrdersListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "status": status,
            "updated_at_min": updated_at_min,
            "updated_at_max": updated_at_max,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("draft_orders", "list", params)
        # Cast generic envelope to concrete typed result
        return DraftOrdersListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        draft_order_id: str,
        **kwargs
    ) -> DraftOrder:
        """
        Retrieves a single draft order by ID

        Args:
            draft_order_id: The draft order ID
            **kwargs: Additional parameters

        Returns:
            DraftOrder
        """
        params = {k: v for k, v in {
            "draft_order_id": draft_order_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("draft_orders", "get", params)
        return result



    async def context_store_search(
        self,
        query: DraftOrdersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DraftOrdersSearchResult:
        """
        Search draft_orders records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DraftOrdersSearchFilter):
        - id: Unique identifier for the draft order
        - name: Shopify-assigned display name for the draft order (e.g. `#D12345`)
        - email: Email address associated with the draft order
        - status: Status of the draft order (`open`, `invoice_sent`, `completed`)
        - currency: ISO 4217 currency code for the draft order totals
        - total_price: Total price of the draft order
        - order_id: Identifier of the completed order, if the draft has been completed
        - created_at: ISO 8601 timestamp when the draft order was created
        - updated_at: ISO 8601 timestamp when the draft order was last updated
        - completed_at: ISO 8601 timestamp when the draft order was completed, if applicable

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DraftOrdersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("draft_orders", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DraftOrdersSearchResult(
            data=[
                DraftOrdersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class FulfillmentsQuery:
    """
    Query class for Fulfillments entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        order_id: str,
        limit: int | None = None,
        since_id: int | None = None,
        created_at_min: str | None = None,
        created_at_max: str | None = None,
        updated_at_min: str | None = None,
        updated_at_max: str | None = None,
        **kwargs
    ) -> FulfillmentsListResult:
        """
        Returns a list of fulfillments for an order

        Args:
            order_id: The order ID
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            created_at_min: Show fulfillments created after date (ISO 8601 format)
            created_at_max: Show fulfillments created before date (ISO 8601 format)
            updated_at_min: Show fulfillments last updated after date (ISO 8601 format)
            updated_at_max: Show fulfillments last updated before date (ISO 8601 format)
            **kwargs: Additional parameters

        Returns:
            FulfillmentsListResult
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            "limit": limit,
            "since_id": since_id,
            "created_at_min": created_at_min,
            "created_at_max": created_at_max,
            "updated_at_min": updated_at_min,
            "updated_at_max": updated_at_max,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("fulfillments", "list", params)
        # Cast generic envelope to concrete typed result
        return FulfillmentsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        order_id: str,
        fulfillment_id: str,
        **kwargs
    ) -> Fulfillment:
        """
        Retrieves a single fulfillment by ID

        Args:
            order_id: The order ID
            fulfillment_id: The fulfillment ID
            **kwargs: Additional parameters

        Returns:
            Fulfillment
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            "fulfillment_id": fulfillment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("fulfillments", "get", params)
        return result



    async def context_store_search(
        self,
        query: FulfillmentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> FulfillmentsSearchResult:
        """
        Search fulfillments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (FulfillmentsSearchFilter):
        - id: Unique identifier for the fulfillment
        - order_id: Identifier of the parent order
        - status: Fulfillment status (e.g. `pending`, `open`, `success`, `cancelled`)
        - shipment_status: Carrier shipment status (e.g. `delivered`, `in_transit`)
        - tracking_company: Name of the shipping carrier
        - tracking_number: Primary tracking number for the shipment
        - location_id: Identifier of the fulfilling location
        - created_at: ISO 8601 timestamp when the fulfillment was created
        - updated_at: ISO 8601 timestamp when the fulfillment was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            FulfillmentsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("fulfillments", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return FulfillmentsSearchResult(
            data=[
                FulfillmentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class OrderRefundsQuery:
    """
    Query class for OrderRefunds entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        order_id: str,
        limit: int | None = None,
        **kwargs
    ) -> OrderRefundsListResult:
        """
        Returns a list of refunds for an order

        Args:
            order_id: The order ID
            limit: Maximum number of results to return (max 250)
            **kwargs: Additional parameters

        Returns:
            OrderRefundsListResult
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("order_refunds", "list", params)
        # Cast generic envelope to concrete typed result
        return OrderRefundsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        order_id: str,
        refund_id: str,
        **kwargs
    ) -> Refund:
        """
        Retrieves a single refund by ID

        Args:
            order_id: The order ID
            refund_id: The refund ID
            **kwargs: Additional parameters

        Returns:
            Refund
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            "refund_id": refund_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("order_refunds", "get", params)
        return result



    async def context_store_search(
        self,
        query: OrderRefundsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OrderRefundsSearchResult:
        """
        Search order_refunds records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OrderRefundsSearchFilter):
        - id: Unique identifier for the refund
        - order_id: Identifier of the refunded order
        - user_id: Identifier of the staff user who processed the refund
        - note: Merchant-provided note explaining the refund
        - created_at: ISO 8601 timestamp when the refund was created
        - processed_at: ISO 8601 timestamp when the refund was processed

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OrderRefundsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("order_refunds", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OrderRefundsSearchResult(
            data=[
                OrderRefundsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TransactionsQuery:
    """
    Query class for Transactions entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        order_id: str,
        since_id: int | None = None,
        **kwargs
    ) -> TransactionsListResult:
        """
        Returns a list of transactions for an order

        Args:
            order_id: The order ID
            since_id: Restrict results to after the specified ID
            **kwargs: Additional parameters

        Returns:
            TransactionsListResult
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            "since_id": since_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transactions", "list", params)
        # Cast generic envelope to concrete typed result
        return TransactionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        order_id: str,
        transaction_id: str,
        **kwargs
    ) -> Transaction:
        """
        Retrieves a single transaction by ID

        Args:
            order_id: The order ID
            transaction_id: The transaction ID
            **kwargs: Additional parameters

        Returns:
            Transaction
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            "transaction_id": transaction_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transactions", "get", params)
        return result



class TenderTransactionsQuery:
    """
    Query class for TenderTransactions entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        processed_at_min: str | None = None,
        processed_at_max: str | None = None,
        order: str | None = None,
        **kwargs
    ) -> TenderTransactionsListResult:
        """
        Returns a list of tender transactions

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            processed_at_min: Show tender transactions processed after date (ISO 8601 format)
            processed_at_max: Show tender transactions processed before date (ISO 8601 format)
            order: Order of results
            **kwargs: Additional parameters

        Returns:
            TenderTransactionsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "processed_at_min": processed_at_min,
            "processed_at_max": processed_at_max,
            "order": order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tender_transactions", "list", params)
        # Cast generic envelope to concrete typed result
        return TenderTransactionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: TenderTransactionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TenderTransactionsSearchResult:
        """
        Search tender_transactions records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TenderTransactionsSearchFilter):
        - id: Unique identifier for the tender transaction
        - order_id: Identifier of the order the transaction belongs to
        - user_id: Identifier of the staff user who processed the transaction
        - amount: Amount of the transaction in the shop's currency
        - currency: ISO 4217 currency code for the transaction amount
        - payment_method: Payment method used (e.g. `credit_card`, `paypal`)
        - test: Whether the transaction was a test transaction
        - processed_at: ISO 8601 timestamp when the transaction was processed

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TenderTransactionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("tender_transactions", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TenderTransactionsSearchResult(
            data=[
                TenderTransactionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CountriesQuery:
    """
    Query class for Countries entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        since_id: int | None = None,
        **kwargs
    ) -> CountriesListResult:
        """
        Returns a list of countries

        Args:
            since_id: Restrict results to after the specified ID
            **kwargs: Additional parameters

        Returns:
            CountriesListResult
        """
        params = {k: v for k, v in {
            "since_id": since_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("countries", "list", params)
        # Cast generic envelope to concrete typed result
        return CountriesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        country_id: str,
        **kwargs
    ) -> Country:
        """
        Retrieves a single country by ID

        Args:
            country_id: The country ID
            **kwargs: Additional parameters

        Returns:
            Country
        """
        params = {k: v for k, v in {
            "country_id": country_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("countries", "get", params)
        return result



    async def context_store_search(
        self,
        query: CountriesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CountriesSearchResult:
        """
        Search countries records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CountriesSearchFilter):
        - id: Unique identifier for the country tax row
        - name: Human-readable country name
        - code: ISO 3166-1 alpha-2 country code
        - tax_name: Localized name of the tax applied in this country

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CountriesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("countries", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CountriesSearchResult(
            data=[
                CountriesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MetafieldShopsQuery:
    """
    Query class for MetafieldShops entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        namespace: str | None = None,
        key: str | None = None,
        type: str | None = None,
        **kwargs
    ) -> MetafieldShopsListResult:
        """
        Returns a list of metafields for the shop

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            namespace: Filter by namespace
            key: Filter by key
            type: Filter by type
            **kwargs: Additional parameters

        Returns:
            MetafieldShopsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "namespace": namespace,
            "key": key,
            "type": type,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_shops", "list", params)
        # Cast generic envelope to concrete typed result
        return MetafieldShopsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        metafield_id: str,
        **kwargs
    ) -> Metafield:
        """
        Retrieves a single metafield by ID

        Args:
            metafield_id: The metafield ID
            **kwargs: Additional parameters

        Returns:
            Metafield
        """
        params = {k: v for k, v in {
            "metafield_id": metafield_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_shops", "get", params)
        return result



    async def context_store_search(
        self,
        query: MetafieldShopsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldShopsSearchResult:
        """
        Search metafield_shops records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldShopsSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldShopsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_shops", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldShopsSearchResult(
            data=[
                MetafieldShopsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MetafieldCustomersQuery:
    """
    Query class for MetafieldCustomers entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        customer_id: str,
        limit: int | None = None,
        since_id: int | None = None,
        namespace: str | None = None,
        key: str | None = None,
        **kwargs
    ) -> MetafieldCustomersListResult:
        """
        Returns a list of metafields for a customer

        Args:
            customer_id: The customer ID
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            namespace: Filter by namespace
            key: Filter by key
            **kwargs: Additional parameters

        Returns:
            MetafieldCustomersListResult
        """
        params = {k: v for k, v in {
            "customer_id": customer_id,
            "limit": limit,
            "since_id": since_id,
            "namespace": namespace,
            "key": key,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_customers", "list", params)
        # Cast generic envelope to concrete typed result
        return MetafieldCustomersListResult(
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: MetafieldCustomersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldCustomersSearchResult:
        """
        Search metafield_customers records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldCustomersSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldCustomersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_customers", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldCustomersSearchResult(
            data=[
                MetafieldCustomersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MetafieldProductsQuery:
    """
    Query class for MetafieldProducts entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        product_id: str,
        limit: int | None = None,
        since_id: int | None = None,
        namespace: str | None = None,
        key: str | None = None,
        **kwargs
    ) -> MetafieldProductsListResult:
        """
        Returns a list of metafields for a product

        Args:
            product_id: The product ID
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            namespace: Filter by namespace
            key: Filter by key
            **kwargs: Additional parameters

        Returns:
            MetafieldProductsListResult
        """
        params = {k: v for k, v in {
            "product_id": product_id,
            "limit": limit,
            "since_id": since_id,
            "namespace": namespace,
            "key": key,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_products", "list", params)
        # Cast generic envelope to concrete typed result
        return MetafieldProductsListResult(
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: MetafieldProductsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldProductsSearchResult:
        """
        Search metafield_products records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldProductsSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldProductsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_products", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldProductsSearchResult(
            data=[
                MetafieldProductsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MetafieldOrdersQuery:
    """
    Query class for MetafieldOrders entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        order_id: str,
        limit: int | None = None,
        since_id: int | None = None,
        namespace: str | None = None,
        key: str | None = None,
        **kwargs
    ) -> MetafieldOrdersListResult:
        """
        Returns a list of metafields for an order

        Args:
            order_id: The order ID
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            namespace: Filter by namespace
            key: Filter by key
            **kwargs: Additional parameters

        Returns:
            MetafieldOrdersListResult
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            "limit": limit,
            "since_id": since_id,
            "namespace": namespace,
            "key": key,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_orders", "list", params)
        # Cast generic envelope to concrete typed result
        return MetafieldOrdersListResult(
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: MetafieldOrdersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldOrdersSearchResult:
        """
        Search metafield_orders records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldOrdersSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldOrdersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_orders", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldOrdersSearchResult(
            data=[
                MetafieldOrdersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MetafieldDraftOrdersQuery:
    """
    Query class for MetafieldDraftOrders entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        draft_order_id: str,
        limit: int | None = None,
        since_id: int | None = None,
        namespace: str | None = None,
        key: str | None = None,
        **kwargs
    ) -> MetafieldDraftOrdersListResult:
        """
        Returns a list of metafields for a draft order

        Args:
            draft_order_id: The draft order ID
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            namespace: Filter by namespace
            key: Filter by key
            **kwargs: Additional parameters

        Returns:
            MetafieldDraftOrdersListResult
        """
        params = {k: v for k, v in {
            "draft_order_id": draft_order_id,
            "limit": limit,
            "since_id": since_id,
            "namespace": namespace,
            "key": key,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_draft_orders", "list", params)
        # Cast generic envelope to concrete typed result
        return MetafieldDraftOrdersListResult(
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: MetafieldDraftOrdersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldDraftOrdersSearchResult:
        """
        Search metafield_draft_orders records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldDraftOrdersSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldDraftOrdersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_draft_orders", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldDraftOrdersSearchResult(
            data=[
                MetafieldDraftOrdersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MetafieldLocationsQuery:
    """
    Query class for MetafieldLocations entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        location_id: str,
        limit: int | None = None,
        since_id: int | None = None,
        namespace: str | None = None,
        key: str | None = None,
        **kwargs
    ) -> MetafieldLocationsListResult:
        """
        Returns a list of metafields for a location

        Args:
            location_id: The location ID
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            namespace: Filter by namespace
            key: Filter by key
            **kwargs: Additional parameters

        Returns:
            MetafieldLocationsListResult
        """
        params = {k: v for k, v in {
            "location_id": location_id,
            "limit": limit,
            "since_id": since_id,
            "namespace": namespace,
            "key": key,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_locations", "list", params)
        # Cast generic envelope to concrete typed result
        return MetafieldLocationsListResult(
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: MetafieldLocationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldLocationsSearchResult:
        """
        Search metafield_locations records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldLocationsSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldLocationsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_locations", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldLocationsSearchResult(
            data=[
                MetafieldLocationsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MetafieldProductVariantsQuery:
    """
    Query class for MetafieldProductVariants entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        variant_id: str,
        limit: int | None = None,
        since_id: int | None = None,
        namespace: str | None = None,
        key: str | None = None,
        **kwargs
    ) -> MetafieldProductVariantsListResult:
        """
        Returns a list of metafields for a product variant

        Args:
            variant_id: The variant ID
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            namespace: Filter by namespace
            key: Filter by key
            **kwargs: Additional parameters

        Returns:
            MetafieldProductVariantsListResult
        """
        params = {k: v for k, v in {
            "variant_id": variant_id,
            "limit": limit,
            "since_id": since_id,
            "namespace": namespace,
            "key": key,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_product_variants", "list", params)
        # Cast generic envelope to concrete typed result
        return MetafieldProductVariantsListResult(
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: MetafieldProductVariantsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldProductVariantsSearchResult:
        """
        Search metafield_product_variants records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldProductVariantsSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldProductVariantsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_product_variants", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldProductVariantsSearchResult(
            data=[
                MetafieldProductVariantsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MetafieldSmartCollectionsQuery:
    """
    Query class for MetafieldSmartCollections entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        collection_id: str,
        limit: int | None = None,
        since_id: int | None = None,
        namespace: str | None = None,
        key: str | None = None,
        **kwargs
    ) -> MetafieldSmartCollectionsListResult:
        """
        Returns a list of metafields for a smart collection

        Args:
            collection_id: The collection ID
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            namespace: Filter by namespace
            key: Filter by key
            **kwargs: Additional parameters

        Returns:
            MetafieldSmartCollectionsListResult
        """
        params = {k: v for k, v in {
            "collection_id": collection_id,
            "limit": limit,
            "since_id": since_id,
            "namespace": namespace,
            "key": key,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_smart_collections", "list", params)
        # Cast generic envelope to concrete typed result
        return MetafieldSmartCollectionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: MetafieldSmartCollectionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldSmartCollectionsSearchResult:
        """
        Search metafield_smart_collections records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldSmartCollectionsSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldSmartCollectionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_smart_collections", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldSmartCollectionsSearchResult(
            data=[
                MetafieldSmartCollectionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MetafieldProductImagesQuery:
    """
    Query class for MetafieldProductImages entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        product_id: str,
        image_id: str,
        limit: int | None = None,
        since_id: int | None = None,
        namespace: str | None = None,
        key: str | None = None,
        **kwargs
    ) -> MetafieldProductImagesListResult:
        """
        Returns a list of metafields for a product image

        Args:
            product_id: The product ID
            image_id: The image ID
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            namespace: Filter by namespace
            key: Filter by key
            **kwargs: Additional parameters

        Returns:
            MetafieldProductImagesListResult
        """
        params = {k: v for k, v in {
            "product_id": product_id,
            "image_id": image_id,
            "limit": limit,
            "since_id": since_id,
            "namespace": namespace,
            "key": key,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_product_images", "list", params)
        # Cast generic envelope to concrete typed result
        return MetafieldProductImagesListResult(
            data=result.data,
            meta=result.meta
        )



    async def context_store_search(
        self,
        query: MetafieldProductImagesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldProductImagesSearchResult:
        """
        Search metafield_product_images records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldProductImagesSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldProductImagesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_product_images", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldProductImagesSearchResult(
            data=[
                MetafieldProductImagesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CustomerAddressQuery:
    """
    Query class for CustomerAddress entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        customer_id: str,
        limit: int | None = None,
        **kwargs
    ) -> CustomerAddressListResult:
        """
        Returns a list of addresses for a customer

        Args:
            customer_id: The customer ID
            limit: Maximum number of results to return (max 250)
            **kwargs: Additional parameters

        Returns:
            CustomerAddressListResult
        """
        params = {k: v for k, v in {
            "customer_id": customer_id,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customer_address", "list", params)
        # Cast generic envelope to concrete typed result
        return CustomerAddressListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        customer_id: str,
        address_id: str,
        **kwargs
    ) -> CustomerAddress:
        """
        Retrieves a single customer address by ID

        Args:
            customer_id: The customer ID
            address_id: The address ID
            **kwargs: Additional parameters

        Returns:
            CustomerAddress
        """
        params = {k: v for k, v in {
            "customer_id": customer_id,
            "address_id": address_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customer_address", "get", params)
        return result



class FulfillmentOrdersQuery:
    """
    Query class for FulfillmentOrders entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        order_id: str,
        **kwargs
    ) -> FulfillmentOrdersListResult:
        """
        Returns a list of fulfillment orders for a specific order

        Args:
            order_id: The order ID
            **kwargs: Additional parameters

        Returns:
            FulfillmentOrdersListResult
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("fulfillment_orders", "list", params)
        # Cast generic envelope to concrete typed result
        return FulfillmentOrdersListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        fulfillment_order_id: str,
        **kwargs
    ) -> FulfillmentOrder:
        """
        Retrieves a single fulfillment order by ID

        Args:
            fulfillment_order_id: The fulfillment order ID
            **kwargs: Additional parameters

        Returns:
            FulfillmentOrder
        """
        params = {k: v for k, v in {
            "fulfillment_order_id": fulfillment_order_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("fulfillment_orders", "get", params)
        return result



    async def context_store_search(
        self,
        query: FulfillmentOrdersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> FulfillmentOrdersSearchResult:
        """
        Search fulfillment_orders records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (FulfillmentOrdersSearchFilter):
        - id: Unique identifier for the fulfillment order
        - order_id: Identifier of the parent order
        - shop_id: Identifier of the shop that owns the fulfillment order
        - assigned_location_id: Identifier of the location assigned to fulfill the order
        - status: Fulfillment order status (e.g. `open`, `in_progress`, `closed`)
        - request_status: Status of the fulfillment request (e.g. `unsubmitted`, `submitted`)
        - created_at: ISO 8601 timestamp when the fulfillment order was created
        - updated_at: ISO 8601 timestamp when the fulfillment order was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            FulfillmentOrdersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("fulfillment_orders", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return FulfillmentOrdersSearchResult(
            data=[
                FulfillmentOrdersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
