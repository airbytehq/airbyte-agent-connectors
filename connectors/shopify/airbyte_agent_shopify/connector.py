"""
Shopify connector.
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

from .connector_model import ShopifyConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
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
)
if TYPE_CHECKING:
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




class ShopifyConnector:
    """
    Type-safe Shopify API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "shopify"
    connector_version = "0.1.3"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

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

    def __init__(
        self,
        auth_config: ShopifyAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        connector_id: str | None = None,
        on_token_refresh: Any | None = None,
        shop: str | None = None    ):
        """
        Initialize a new shopify connector instance.

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
                Example: lambda tokens: save_to_database(tokens)            shop: Your Shopify store name (e.g., 'my-store' from my-store.myshopify.com)
        Examples:
            # Local mode (direct API calls)
            connector = ShopifyConnector(auth_config=ShopifyAuthConfig(api_key="...", shop="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = ShopifyConnector(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid"
            )

            # Hosted mode with lookup by external_user_id
            connector = ShopifyConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = ShopifyConnector(
                auth_config=ShopifyAuthConfig(access_token="...", refresh_token="..."),
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
                connector_definition_id=str(ShopifyConnectorModel.id) if not connector_id else None,
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
        action: Literal["list", "get"],
        params: Mapping[str, Any]
    ) -> ShopifyExecuteResult[Any] | ShopifyExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get"],
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
        enable_hosted_mode_features: bool = True,
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
            enable_hosted_mode_features: When False, omit hosted-mode search sections from docstrings.
            max_output_chars: Max serialized output size before raising. Use None to disable.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    ShopifyConnectorModel,
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
            connector = await ShopifyConnector.create_hosted(...)
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
        auth_config: "ShopifyAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
    ) -> "ShopifyConnector":
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
            A ShopifyConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await ShopifyConnector.create_hosted(
                external_user_id="my-workspace",
                airbyte_client_id="client_abc",
                airbyte_client_secret="secret_xyz",
                auth_config=ShopifyAuthConfig(api_key="...", shop="..."),
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
                connector_definition_id=str(ShopifyConnectorModel.id),
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


