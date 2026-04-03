"""
Woocommerce connector.
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

from .connector_model import WoocommerceConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    CouponsGetParams,
    CouponsListParams,
    CustomersGetParams,
    CustomersListParams,
    OrderNotesGetParams,
    OrderNotesListParams,
    OrdersGetParams,
    OrdersListParams,
    PaymentGatewaysGetParams,
    PaymentGatewaysListParams,
    ProductAttributesGetParams,
    ProductAttributesListParams,
    ProductCategoriesGetParams,
    ProductCategoriesListParams,
    ProductReviewsGetParams,
    ProductReviewsListParams,
    ProductTagsGetParams,
    ProductTagsListParams,
    ProductVariationsGetParams,
    ProductVariationsListParams,
    ProductsGetParams,
    ProductsListParams,
    RefundsGetParams,
    RefundsListParams,
    ShippingMethodsGetParams,
    ShippingMethodsListParams,
    ShippingZonesGetParams,
    ShippingZonesListParams,
    TaxClassesListParams,
    TaxRatesGetParams,
    TaxRatesListParams,
    AirbyteSearchParams,
    CustomersSearchFilter,
    CustomersSearchQuery,
    OrdersSearchFilter,
    OrdersSearchQuery,
    ProductsSearchFilter,
    ProductsSearchQuery,
    CouponsSearchFilter,
    CouponsSearchQuery,
    ProductCategoriesSearchFilter,
    ProductCategoriesSearchQuery,
    ProductTagsSearchFilter,
    ProductTagsSearchQuery,
    ProductReviewsSearchFilter,
    ProductReviewsSearchQuery,
    ProductAttributesSearchFilter,
    ProductAttributesSearchQuery,
    ProductVariationsSearchFilter,
    ProductVariationsSearchQuery,
    OrderNotesSearchFilter,
    OrderNotesSearchQuery,
    RefundsSearchFilter,
    RefundsSearchQuery,
    PaymentGatewaysSearchFilter,
    PaymentGatewaysSearchQuery,
    ShippingMethodsSearchFilter,
    ShippingMethodsSearchQuery,
    ShippingZonesSearchFilter,
    ShippingZonesSearchQuery,
    TaxRatesSearchFilter,
    TaxRatesSearchQuery,
    TaxClassesSearchFilter,
    TaxClassesSearchQuery,
)
from .models import WoocommerceAuthConfig
if TYPE_CHECKING:
    from .models import WoocommerceReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    WoocommerceCheckResult,
    WoocommerceExecuteResult,
    WoocommerceExecuteResultWithMeta,
    CustomersListResult,
    OrdersListResult,
    ProductsListResult,
    CouponsListResult,
    ProductCategoriesListResult,
    ProductTagsListResult,
    ProductReviewsListResult,
    ProductAttributesListResult,
    ProductVariationsListResult,
    OrderNotesListResult,
    RefundsListResult,
    PaymentGatewaysListResult,
    ShippingMethodsListResult,
    ShippingZonesListResult,
    TaxRatesListResult,
    TaxClassesListResult,
    Coupon,
    Customer,
    Order,
    OrderNote,
    PaymentGateway,
    Product,
    ProductAttribute,
    ProductCategory,
    ProductReview,
    ProductTag,
    ProductVariation,
    Refund,
    ShippingMethod,
    ShippingZone,
    TaxClass,
    TaxRate,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    CustomersSearchData,
    CustomersSearchResult,
    OrdersSearchData,
    OrdersSearchResult,
    ProductsSearchData,
    ProductsSearchResult,
    CouponsSearchData,
    CouponsSearchResult,
    ProductCategoriesSearchData,
    ProductCategoriesSearchResult,
    ProductTagsSearchData,
    ProductTagsSearchResult,
    ProductReviewsSearchData,
    ProductReviewsSearchResult,
    ProductAttributesSearchData,
    ProductAttributesSearchResult,
    ProductVariationsSearchData,
    ProductVariationsSearchResult,
    OrderNotesSearchData,
    OrderNotesSearchResult,
    RefundsSearchData,
    RefundsSearchResult,
    PaymentGatewaysSearchData,
    PaymentGatewaysSearchResult,
    ShippingMethodsSearchData,
    ShippingMethodsSearchResult,
    ShippingZonesSearchData,
    ShippingZonesSearchResult,
    TaxRatesSearchData,
    TaxRatesSearchResult,
    TaxClassesSearchData,
    TaxClassesSearchResult,
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




class WoocommerceConnector:
    """
    Type-safe Woocommerce API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "woocommerce"
    connector_version = "1.0.3"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("customers", "list"): True,
        ("customers", "get"): None,
        ("orders", "list"): True,
        ("orders", "get"): None,
        ("products", "list"): True,
        ("products", "get"): None,
        ("coupons", "list"): True,
        ("coupons", "get"): None,
        ("product_categories", "list"): True,
        ("product_categories", "get"): None,
        ("product_tags", "list"): True,
        ("product_tags", "get"): None,
        ("product_reviews", "list"): True,
        ("product_reviews", "get"): None,
        ("product_attributes", "list"): True,
        ("product_attributes", "get"): None,
        ("product_variations", "list"): True,
        ("product_variations", "get"): None,
        ("order_notes", "list"): True,
        ("order_notes", "get"): None,
        ("refunds", "list"): True,
        ("refunds", "get"): None,
        ("payment_gateways", "list"): True,
        ("payment_gateways", "get"): None,
        ("shipping_methods", "list"): True,
        ("shipping_methods", "get"): None,
        ("shipping_zones", "list"): True,
        ("shipping_zones", "get"): None,
        ("tax_rates", "list"): True,
        ("tax_rates", "get"): None,
        ("tax_classes", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('customers', 'list'): {'page': 'page', 'per_page': 'per_page', 'search': 'search', 'orderby': 'orderby', 'order': 'order', 'email': 'email', 'role': 'role'},
        ('customers', 'get'): {'id': 'id'},
        ('orders', 'list'): {'page': 'page', 'per_page': 'per_page', 'search': 'search', 'after': 'after', 'before': 'before', 'modified_after': 'modified_after', 'modified_before': 'modified_before', 'status': 'status', 'customer': 'customer', 'product': 'product', 'orderby': 'orderby', 'order': 'order'},
        ('orders', 'get'): {'id': 'id'},
        ('products', 'list'): {'page': 'page', 'per_page': 'per_page', 'search': 'search', 'after': 'after', 'before': 'before', 'modified_after': 'modified_after', 'modified_before': 'modified_before', 'status': 'status', 'type': 'type', 'sku': 'sku', 'featured': 'featured', 'category': 'category', 'tag': 'tag', 'on_sale': 'on_sale', 'min_price': 'min_price', 'max_price': 'max_price', 'stock_status': 'stock_status', 'orderby': 'orderby', 'order': 'order'},
        ('products', 'get'): {'id': 'id'},
        ('coupons', 'list'): {'page': 'page', 'per_page': 'per_page', 'search': 'search', 'after': 'after', 'before': 'before', 'modified_after': 'modified_after', 'modified_before': 'modified_before', 'code': 'code', 'orderby': 'orderby', 'order': 'order'},
        ('coupons', 'get'): {'id': 'id'},
        ('product_categories', 'list'): {'page': 'page', 'per_page': 'per_page', 'search': 'search', 'orderby': 'orderby', 'order': 'order', 'hide_empty': 'hide_empty', 'parent': 'parent', 'product': 'product', 'slug': 'slug'},
        ('product_categories', 'get'): {'id': 'id'},
        ('product_tags', 'list'): {'page': 'page', 'per_page': 'per_page', 'search': 'search', 'orderby': 'orderby', 'order': 'order', 'hide_empty': 'hide_empty', 'product': 'product', 'slug': 'slug'},
        ('product_tags', 'get'): {'id': 'id'},
        ('product_reviews', 'list'): {'page': 'page', 'per_page': 'per_page', 'search': 'search', 'after': 'after', 'before': 'before', 'product': 'product', 'status': 'status'},
        ('product_reviews', 'get'): {'id': 'id'},
        ('product_attributes', 'list'): {'page': 'page', 'per_page': 'per_page'},
        ('product_attributes', 'get'): {'id': 'id'},
        ('product_variations', 'list'): {'product_id': 'product_id', 'page': 'page', 'per_page': 'per_page', 'search': 'search', 'sku': 'sku', 'status': 'status', 'stock_status': 'stock_status', 'on_sale': 'on_sale', 'min_price': 'min_price', 'max_price': 'max_price', 'orderby': 'orderby', 'order': 'order'},
        ('product_variations', 'get'): {'product_id': 'product_id', 'id': 'id'},
        ('order_notes', 'list'): {'order_id': 'order_id', 'type': 'type'},
        ('order_notes', 'get'): {'order_id': 'order_id', 'id': 'id'},
        ('refunds', 'list'): {'order_id': 'order_id', 'page': 'page', 'per_page': 'per_page'},
        ('refunds', 'get'): {'order_id': 'order_id', 'id': 'id'},
        ('payment_gateways', 'get'): {'id': 'id'},
        ('shipping_methods', 'get'): {'id': 'id'},
        ('shipping_zones', 'get'): {'id': 'id'},
        ('tax_rates', 'list'): {'page': 'page', 'per_page': 'per_page', 'class_': 'class', 'orderby': 'orderby', 'order': 'order'},
        ('tax_rates', 'get'): {'id': 'id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (WoocommerceAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: WoocommerceAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        shop: str | None = None    ):
        """
        Initialize a new woocommerce connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., WoocommerceAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            shop: The WooCommerce store domain (e.g., mystore.com)
        Examples:
            # Local mode (direct API calls)
            connector = WoocommerceConnector(auth_config=WoocommerceAuthConfig(api_key="...", api_secret="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = WoocommerceConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = WoocommerceConnector(
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
                connector_definition_id=str(WoocommerceConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or WoocommerceAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if shop:
                config_values["shop"] = shop

            self._executor = LocalExecutor(
                model=WoocommerceConnectorModel,
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
        self.coupons = CouponsQuery(self)
        self.product_categories = ProductCategoriesQuery(self)
        self.product_tags = ProductTagsQuery(self)
        self.product_reviews = ProductReviewsQuery(self)
        self.product_attributes = ProductAttributesQuery(self)
        self.product_variations = ProductVariationsQuery(self)
        self.order_notes = OrderNotesQuery(self)
        self.refunds = RefundsQuery(self)
        self.payment_gateways = PaymentGatewaysQuery(self)
        self.shipping_methods = ShippingMethodsQuery(self)
        self.shipping_zones = ShippingZonesQuery(self)
        self.tax_rates = TaxRatesQuery(self)
        self.tax_classes = TaxClassesQuery(self)

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
        entity: Literal["coupons"],
        action: Literal["list"],
        params: "CouponsListParams"
    ) -> "CouponsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["coupons"],
        action: Literal["get"],
        params: "CouponsGetParams"
    ) -> "Coupon": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_categories"],
        action: Literal["list"],
        params: "ProductCategoriesListParams"
    ) -> "ProductCategoriesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_categories"],
        action: Literal["get"],
        params: "ProductCategoriesGetParams"
    ) -> "ProductCategory": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_tags"],
        action: Literal["list"],
        params: "ProductTagsListParams"
    ) -> "ProductTagsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_tags"],
        action: Literal["get"],
        params: "ProductTagsGetParams"
    ) -> "ProductTag": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_reviews"],
        action: Literal["list"],
        params: "ProductReviewsListParams"
    ) -> "ProductReviewsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_reviews"],
        action: Literal["get"],
        params: "ProductReviewsGetParams"
    ) -> "ProductReview": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_attributes"],
        action: Literal["list"],
        params: "ProductAttributesListParams"
    ) -> "ProductAttributesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_attributes"],
        action: Literal["get"],
        params: "ProductAttributesGetParams"
    ) -> "ProductAttribute": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_variations"],
        action: Literal["list"],
        params: "ProductVariationsListParams"
    ) -> "ProductVariationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_variations"],
        action: Literal["get"],
        params: "ProductVariationsGetParams"
    ) -> "ProductVariation": ...

    @overload
    async def execute(
        self,
        entity: Literal["order_notes"],
        action: Literal["list"],
        params: "OrderNotesListParams"
    ) -> "OrderNotesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["order_notes"],
        action: Literal["get"],
        params: "OrderNotesGetParams"
    ) -> "OrderNote": ...

    @overload
    async def execute(
        self,
        entity: Literal["refunds"],
        action: Literal["list"],
        params: "RefundsListParams"
    ) -> "RefundsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["refunds"],
        action: Literal["get"],
        params: "RefundsGetParams"
    ) -> "Refund": ...

    @overload
    async def execute(
        self,
        entity: Literal["payment_gateways"],
        action: Literal["list"],
        params: "PaymentGatewaysListParams"
    ) -> "PaymentGatewaysListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["payment_gateways"],
        action: Literal["get"],
        params: "PaymentGatewaysGetParams"
    ) -> "PaymentGateway": ...

    @overload
    async def execute(
        self,
        entity: Literal["shipping_methods"],
        action: Literal["list"],
        params: "ShippingMethodsListParams"
    ) -> "ShippingMethodsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["shipping_methods"],
        action: Literal["get"],
        params: "ShippingMethodsGetParams"
    ) -> "ShippingMethod": ...

    @overload
    async def execute(
        self,
        entity: Literal["shipping_zones"],
        action: Literal["list"],
        params: "ShippingZonesListParams"
    ) -> "ShippingZonesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["shipping_zones"],
        action: Literal["get"],
        params: "ShippingZonesGetParams"
    ) -> "ShippingZone": ...

    @overload
    async def execute(
        self,
        entity: Literal["tax_rates"],
        action: Literal["list"],
        params: "TaxRatesListParams"
    ) -> "TaxRatesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tax_rates"],
        action: Literal["get"],
        params: "TaxRatesGetParams"
    ) -> "TaxRate": ...

    @overload
    async def execute(
        self,
        entity: Literal["tax_classes"],
        action: Literal["list"],
        params: "TaxClassesListParams"
    ) -> "TaxClassesListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> WoocommerceExecuteResult[Any] | WoocommerceExecuteResultWithMeta[Any, Any] | Any: ...

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
                return WoocommerceExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return WoocommerceExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> WoocommerceCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            WoocommerceCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return WoocommerceCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return WoocommerceCheckResult(
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
            @WoocommerceConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @WoocommerceConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    WoocommerceConnectorModel,
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
        return describe_entities(WoocommerceConnectorModel)

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
            (e for e in WoocommerceConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in WoocommerceConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await WoocommerceConnector.create(...)
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
        auth_config: "WoocommerceAuthConfig",
        name: str | None = None,
        replication_config: "WoocommerceReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "WoocommerceConnector":
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
            replication_config: Typed replication settings.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A WoocommerceConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await WoocommerceConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=WoocommerceAuthConfig(api_key="...", api_secret="..."),
            )

            # With replication config (required for this connector):
            connector = await WoocommerceConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=WoocommerceAuthConfig(api_key="...", api_secret="..."),
                replication_config=WoocommerceReplicationConfig(start_date="..."),
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
                connector_definition_id=str(WoocommerceConnectorModel.id),
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




class CustomersQuery:
    """
    Query class for Customers entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        search: str | None = None,
        orderby: str | None = None,
        order: str | None = None,
        email: str | None = None,
        role: str | None = None,
        **kwargs
    ) -> CustomersListResult:
        """
        List customers

        Args:
            page: Current page of the collection
            per_page: Maximum number of items to return per page
            search: Limit results to those matching a string
            orderby: Sort collection by attribute
            order: Order sort attribute ascending or descending
            email: Limit result set to resources with a specific email
            role: Limit result set to resources with a specific role
            **kwargs: Additional parameters

        Returns:
            CustomersListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "search": search,
            "orderby": orderby,
            "order": order,
            "email": email,
            "role": role,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "list", params)
        # Cast generic envelope to concrete typed result
        return CustomersListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Customer:
        """
        Retrieve a customer

        Args:
            id: Unique identifier for the customer
            **kwargs: Additional parameters

        Returns:
            Customer
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "get", params)
        return result



    async def search(
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
        - avatar_url: Avatar URL
        - billing: List of billing address data
        - date_created: The date the customer was created, in the site's timezone
        - date_created_gmt: The date the customer was created, as GMT
        - date_modified: The date the customer was last modified, in the site's timezone
        - date_modified_gmt: The date the customer was last modified, as GMT
        - email: The email address for the customer
        - first_name: Customer first name
        - id: Unique identifier for the resource
        - is_paying_customer: Is the customer a paying customer
        - last_name: Customer last name
        - meta_data: Meta data
        - role: Customer role
        - shipping: List of shipping address data
        - username: Customer login name

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

        result = await self._connector.execute("customers", "search", params)

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

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        search: str | None = None,
        after: str | None = None,
        before: str | None = None,
        modified_after: str | None = None,
        modified_before: str | None = None,
        status: str | None = None,
        customer: int | None = None,
        product: int | None = None,
        orderby: str | None = None,
        order: str | None = None,
        **kwargs
    ) -> OrdersListResult:
        """
        List orders

        Args:
            page: Current page of the collection
            per_page: Maximum number of items to return per page
            search: Limit results to those matching a string
            after: Limit response to resources published after a given ISO8601 date
            before: Limit response to resources published before a given ISO8601 date
            modified_after: Limit response to resources modified after a given ISO8601 date
            modified_before: Limit response to resources modified before a given ISO8601 date
            status: Limit result set to orders with a specific status
            customer: Limit result set to orders assigned to a specific customer ID
            product: Limit result set to orders that include a specific product ID
            orderby: Sort collection by attribute
            order: Order sort attribute ascending or descending
            **kwargs: Additional parameters

        Returns:
            OrdersListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "search": search,
            "after": after,
            "before": before,
            "modified_after": modified_after,
            "modified_before": modified_before,
            "status": status,
            "customer": customer,
            "product": product,
            "orderby": orderby,
            "order": order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("orders", "list", params)
        # Cast generic envelope to concrete typed result
        return OrdersListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Order:
        """
        Retrieve an order

        Args:
            id: Unique identifier for the order
            **kwargs: Additional parameters

        Returns:
            Order
        """
        params = {k: v for k, v in {
            "id": id,
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
        - billing: Billing address
        - cart_hash: MD5 hash of cart items to ensure orders are not modified
        - cart_tax: Sum of line item taxes only
        - coupon_lines: Coupons line data
        - created_via: Shows where the order was created
        - currency: Currency the order was created with, in ISO format
        - customer_id: User ID who owns the order (0 for guests)
        - customer_ip_address: Customer's IP address
        - customer_note: Note left by the customer during checkout
        - customer_user_agent: User agent of the customer
        - date_completed: The date the order was completed, in the site's timezone
        - date_completed_gmt: The date the order was completed, as GMT
        - date_created: The date the order was created, in the site's timezone
        - date_created_gmt: The date the order was created, as GMT
        - date_modified: The date the order was last modified, in the site's timezone
        - date_modified_gmt: The date the order was last modified, as GMT
        - date_paid: The date the order was paid, in the site's timezone
        - date_paid_gmt: The date the order was paid, as GMT
        - discount_tax: Total discount tax amount for the order
        - discount_total: Total discount amount for the order
        - fee_lines: Fee lines data
        - id: Unique identifier for the resource
        - line_items: Line items data
        - meta_data: Meta data
        - number: Order number
        - order_key: Order key
        - parent_id: Parent order ID
        - payment_method: Payment method ID
        - payment_method_title: Payment method title
        - prices_include_tax: True if the prices included tax during checkout
        - refunds: List of refunds
        - shipping: Shipping address
        - shipping_lines: Shipping lines data
        - shipping_tax: Total shipping tax amount for the order
        - shipping_total: Total shipping amount for the order
        - status: Order status
        - tax_lines: Tax lines data
        - total: Grand total
        - total_tax: Sum of all taxes
        - transaction_id: Unique transaction ID
        - version: Version of WooCommerce which last updated the order

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

class ProductsQuery:
    """
    Query class for Products entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        search: str | None = None,
        after: str | None = None,
        before: str | None = None,
        modified_after: str | None = None,
        modified_before: str | None = None,
        status: str | None = None,
        type: str | None = None,
        sku: str | None = None,
        featured: bool | None = None,
        category: str | None = None,
        tag: str | None = None,
        on_sale: bool | None = None,
        min_price: str | None = None,
        max_price: str | None = None,
        stock_status: str | None = None,
        orderby: str | None = None,
        order: str | None = None,
        **kwargs
    ) -> ProductsListResult:
        """
        List products

        Args:
            page: Current page of the collection
            per_page: Maximum number of items to return per page
            search: Limit results to those matching a string
            after: Limit response to resources published after a given ISO8601 date
            before: Limit response to resources published before a given ISO8601 date
            modified_after: Limit response to resources modified after a given ISO8601 date
            modified_before: Limit response to resources modified before a given ISO8601 date
            status: Limit result set to products with a specific status
            type: Limit result set to products with a specific type
            sku: Limit result set to products with a specific SKU
            featured: Limit result set to featured products
            category: Limit result set to products assigned a specific category ID
            tag: Limit result set to products assigned a specific tag ID
            on_sale: Limit result set to products on sale
            min_price: Limit result set to products based on a minimum price
            max_price: Limit result set to products based on a maximum price
            stock_status: Limit result set to products with specified stock status
            orderby: Sort collection by attribute
            order: Order sort attribute ascending or descending
            **kwargs: Additional parameters

        Returns:
            ProductsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "search": search,
            "after": after,
            "before": before,
            "modified_after": modified_after,
            "modified_before": modified_before,
            "status": status,
            "type": type,
            "sku": sku,
            "featured": featured,
            "category": category,
            "tag": tag,
            "on_sale": on_sale,
            "min_price": min_price,
            "max_price": max_price,
            "stock_status": stock_status,
            "orderby": orderby,
            "order": order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "list", params)
        # Cast generic envelope to concrete typed result
        return ProductsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Product:
        """
        Retrieve a product

        Args:
            id: Unique identifier for the product
            **kwargs: Additional parameters

        Returns:
            Product
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "get", params)
        return result



    async def search(
        self,
        query: ProductsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProductsSearchResult:
        """
        Search products records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProductsSearchFilter):
        - attributes: List of attributes
        - average_rating: Reviews average rating
        - backordered: Shows if the product is on backordered
        - backorders: If managing stock, this controls if backorders are allowed
        - backorders_allowed: Shows if backorders are allowed
        - button_text: Product external button text
        - catalog_visibility: Catalog visibility
        - categories: List of categories
        - cross_sell_ids: List of cross-sell products IDs
        - date_created: The date the product was created
        - date_created_gmt: The date the product was created, as GMT
        - date_modified: The date the product was last modified
        - date_modified_gmt: The date the product was last modified, as GMT
        - date_on_sale_from: Start date of sale price
        - date_on_sale_from_gmt: Start date of sale price, as GMT
        - date_on_sale_to: End date of sale price
        - date_on_sale_to_gmt: End date of sale price, as GMT
        - default_attributes: Defaults variation attributes
        - description: Product description
        - dimensions: Product dimensions
        - download_expiry: Number of days until access to downloadable files expires
        - download_limit: Number of times downloadable files can be downloaded
        - downloadable: If the product is downloadable
        - downloads: List of downloadable files
        - external_url: Product external URL
        - grouped_products: List of grouped products ID
        - id: Unique identifier for the resource
        - images: List of images
        - manage_stock: Stock management at product level
        - menu_order: Menu order
        - meta_data: Meta data
        - name: Product name
        - on_sale: Shows if the product is on sale
        - parent_id: Product parent ID
        - permalink: Product URL
        - price: Current product price
        - price_html: Price formatted in HTML
        - purchasable: Shows if the product can be bought
        - purchase_note: Note to send customer after purchase
        - rating_count: Amount of reviews
        - regular_price: Product regular price
        - related_ids: List of related products IDs
        - reviews_allowed: Allow reviews
        - sale_price: Product sale price
        - shipping_class: Shipping class slug
        - shipping_class_id: Shipping class ID
        - shipping_required: Shows if the product needs to be shipped
        - shipping_taxable: Shows if product shipping is taxable
        - short_description: Product short description
        - sku: Unique identifier (SKU)
        - slug: Product slug
        - sold_individually: Allow one item per order
        - status: Product status
        - stock_quantity: Stock quantity
        - stock_status: Controls the stock status
        - tags: List of tags
        - tax_class: Tax class
        - tax_status: Tax status
        - total_sales: Amount of sales
        - type_: Product type
        - upsell_ids: List of up-sell products IDs
        - variations: List of variations IDs
        - virtual: If the product is virtual
        - weight: Product weight

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProductsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("products", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProductsSearchResult(
            data=[
                ProductsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CouponsQuery:
    """
    Query class for Coupons entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        search: str | None = None,
        after: str | None = None,
        before: str | None = None,
        modified_after: str | None = None,
        modified_before: str | None = None,
        code: str | None = None,
        orderby: str | None = None,
        order: str | None = None,
        **kwargs
    ) -> CouponsListResult:
        """
        List coupons

        Args:
            page: Current page of the collection
            per_page: Maximum number of items to return per page
            search: Limit results to those matching a string
            after: Limit response to resources published after a given ISO8601 date
            before: Limit response to resources published before a given ISO8601 date
            modified_after: Limit response to resources modified after a given ISO8601 date
            modified_before: Limit response to resources modified before a given ISO8601 date
            code: Limit result set to resources with a specific code
            orderby: Sort collection by attribute
            order: Order sort attribute ascending or descending
            **kwargs: Additional parameters

        Returns:
            CouponsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "search": search,
            "after": after,
            "before": before,
            "modified_after": modified_after,
            "modified_before": modified_before,
            "code": code,
            "orderby": orderby,
            "order": order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("coupons", "list", params)
        # Cast generic envelope to concrete typed result
        return CouponsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Coupon:
        """
        Retrieve a coupon

        Args:
            id: Unique identifier for the coupon
            **kwargs: Additional parameters

        Returns:
            Coupon
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("coupons", "get", params)
        return result



    async def search(
        self,
        query: CouponsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CouponsSearchResult:
        """
        Search coupons records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CouponsSearchFilter):
        - amount: The amount of discount
        - code: Coupon code
        - date_created: The date the coupon was created
        - date_created_gmt: The date the coupon was created, as GMT
        - date_expires: The date the coupon expires
        - date_expires_gmt: The date the coupon expires, as GMT
        - date_modified: The date the coupon was last modified
        - date_modified_gmt: The date the coupon was last modified, as GMT
        - description: Coupon description
        - discount_type: Determines the type of discount
        - email_restrictions: List of email addresses that can use this coupon
        - exclude_sale_items: If true, not applied to sale items
        - excluded_product_categories: Excluded category IDs
        - excluded_product_ids: Excluded product IDs
        - free_shipping: Enables free shipping
        - id: Unique identifier
        - individual_use: Can only be used individually
        - limit_usage_to_x_items: Max cart items coupon applies to
        - maximum_amount: Maximum order amount
        - meta_data: Meta data
        - minimum_amount: Minimum order amount
        - product_categories: Applicable category IDs
        - product_ids: Applicable product IDs
        - usage_count: Times used
        - usage_limit: Total usage limit
        - usage_limit_per_user: Per-customer usage limit
        - used_by: Users who have used the coupon

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CouponsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("coupons", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CouponsSearchResult(
            data=[
                CouponsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ProductCategoriesQuery:
    """
    Query class for ProductCategories entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        search: str | None = None,
        orderby: str | None = None,
        order: str | None = None,
        hide_empty: bool | None = None,
        parent: int | None = None,
        product: int | None = None,
        slug: str | None = None,
        **kwargs
    ) -> ProductCategoriesListResult:
        """
        List product categories

        Args:
            page: Current page of the collection
            per_page: Maximum number of items to return per page
            search: Limit results to those matching a string
            orderby: Sort collection by attribute
            order: Order sort attribute ascending or descending
            hide_empty: Whether to hide categories not assigned to any products
            parent: Limit result set to categories assigned a specific parent
            product: Limit result set to categories assigned to a specific product
            slug: Limit result set to categories with a specific slug
            **kwargs: Additional parameters

        Returns:
            ProductCategoriesListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "search": search,
            "orderby": orderby,
            "order": order,
            "hide_empty": hide_empty,
            "parent": parent,
            "product": product,
            "slug": slug,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_categories", "list", params)
        # Cast generic envelope to concrete typed result
        return ProductCategoriesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ProductCategory:
        """
        Retrieve a product category

        Args:
            id: Unique identifier for the category
            **kwargs: Additional parameters

        Returns:
            ProductCategory
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_categories", "get", params)
        return result



    async def search(
        self,
        query: ProductCategoriesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProductCategoriesSearchResult:
        """
        Search product_categories records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProductCategoriesSearchFilter):
        - count: Number of published products for the resource
        - description: HTML description of the resource
        - display: Category archive display type
        - id: Unique identifier for the resource
        - image: Image data
        - menu_order: Menu order
        - name: Category name
        - parent: The ID for the parent of the resource
        - slug: An alphanumeric identifier

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProductCategoriesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("product_categories", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProductCategoriesSearchResult(
            data=[
                ProductCategoriesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ProductTagsQuery:
    """
    Query class for ProductTags entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        search: str | None = None,
        orderby: str | None = None,
        order: str | None = None,
        hide_empty: bool | None = None,
        product: int | None = None,
        slug: str | None = None,
        **kwargs
    ) -> ProductTagsListResult:
        """
        List product tags

        Args:
            page: Current page of the collection
            per_page: Maximum number of items to return per page
            search: Limit results to those matching a string
            orderby: Sort collection by attribute
            order: Order sort attribute ascending or descending
            hide_empty: Whether to hide tags not assigned to any products
            product: Limit result set to tags assigned to a specific product
            slug: Limit result set to tags with a specific slug
            **kwargs: Additional parameters

        Returns:
            ProductTagsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "search": search,
            "orderby": orderby,
            "order": order,
            "hide_empty": hide_empty,
            "product": product,
            "slug": slug,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_tags", "list", params)
        # Cast generic envelope to concrete typed result
        return ProductTagsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ProductTag:
        """
        Retrieve a product tag

        Args:
            id: Unique identifier for the tag
            **kwargs: Additional parameters

        Returns:
            ProductTag
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_tags", "get", params)
        return result



    async def search(
        self,
        query: ProductTagsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProductTagsSearchResult:
        """
        Search product_tags records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProductTagsSearchFilter):
        - count: Number of published products
        - description: HTML description
        - id: Unique identifier
        - name: Tag name
        - slug: Alphanumeric identifier

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProductTagsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("product_tags", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProductTagsSearchResult(
            data=[
                ProductTagsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ProductReviewsQuery:
    """
    Query class for ProductReviews entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        search: str | None = None,
        after: str | None = None,
        before: str | None = None,
        product: list[int] | None = None,
        status: str | None = None,
        **kwargs
    ) -> ProductReviewsListResult:
        """
        List product reviews

        Args:
            page: Current page of the collection
            per_page: Maximum number of items to return per page
            search: Limit results to those matching a string
            after: Limit response to reviews published after a given ISO8601 date
            before: Limit response to reviews published before a given ISO8601 date
            product: Limit result set to reviews assigned to specific product IDs
            status: Limit result set to reviews assigned a specific status
            **kwargs: Additional parameters

        Returns:
            ProductReviewsListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "search": search,
            "after": after,
            "before": before,
            "product": product,
            "status": status,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_reviews", "list", params)
        # Cast generic envelope to concrete typed result
        return ProductReviewsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ProductReview:
        """
        Retrieve a product review

        Args:
            id: Unique identifier for the review
            **kwargs: Additional parameters

        Returns:
            ProductReview
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_reviews", "get", params)
        return result



    async def search(
        self,
        query: ProductReviewsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProductReviewsSearchResult:
        """
        Search product_reviews records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProductReviewsSearchFilter):
        - date_created: The date the review was created
        - date_created_gmt: The date the review was created, as GMT
        - id: Unique identifier
        - product_id: Product the review belongs to
        - rating: Review rating (0 to 5)
        - review: The content of the review
        - reviewer: Reviewer name
        - reviewer_email: Reviewer email
        - status: Status of the review
        - verified: Shows if the reviewer bought the product

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProductReviewsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("product_reviews", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProductReviewsSearchResult(
            data=[
                ProductReviewsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ProductAttributesQuery:
    """
    Query class for ProductAttributes entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        **kwargs
    ) -> ProductAttributesListResult:
        """
        List product attributes

        Args:
            page: Current page of the collection
            per_page: Maximum number of items to return per page
            **kwargs: Additional parameters

        Returns:
            ProductAttributesListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_attributes", "list", params)
        # Cast generic envelope to concrete typed result
        return ProductAttributesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ProductAttribute:
        """
        Retrieve a product attribute

        Args:
            id: Unique identifier for the attribute
            **kwargs: Additional parameters

        Returns:
            ProductAttribute
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_attributes", "get", params)
        return result



    async def search(
        self,
        query: ProductAttributesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProductAttributesSearchResult:
        """
        Search product_attributes records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProductAttributesSearchFilter):
        - has_archives: Enable/Disable attribute archives
        - id: Unique identifier
        - name: Attribute name
        - order_by: Default sort order
        - slug: Alphanumeric identifier
        - type_: Type of attribute

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProductAttributesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("product_attributes", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProductAttributesSearchResult(
            data=[
                ProductAttributesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ProductVariationsQuery:
    """
    Query class for ProductVariations entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        product_id: str,
        page: int | None = None,
        per_page: int | None = None,
        search: str | None = None,
        sku: str | None = None,
        status: str | None = None,
        stock_status: str | None = None,
        on_sale: bool | None = None,
        min_price: str | None = None,
        max_price: str | None = None,
        orderby: str | None = None,
        order: str | None = None,
        **kwargs
    ) -> ProductVariationsListResult:
        """
        List product variations

        Args:
            product_id: Unique identifier for the parent product
            page: Current page of the collection
            per_page: Maximum number of items to return per page
            search: Limit results to those matching a string
            sku: Limit result set to variations with a specific SKU
            status: Limit result set to variations with a specific status
            stock_status: Limit result set to variations with specified stock status
            on_sale: Limit result set to variations on sale
            min_price: Limit result set to variations based on a minimum price
            max_price: Limit result set to variations based on a maximum price
            orderby: Sort collection by attribute
            order: Order sort attribute ascending or descending
            **kwargs: Additional parameters

        Returns:
            ProductVariationsListResult
        """
        params = {k: v for k, v in {
            "product_id": product_id,
            "page": page,
            "per_page": per_page,
            "search": search,
            "sku": sku,
            "status": status,
            "stock_status": stock_status,
            "on_sale": on_sale,
            "min_price": min_price,
            "max_price": max_price,
            "orderby": orderby,
            "order": order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_variations", "list", params)
        # Cast generic envelope to concrete typed result
        return ProductVariationsListResult(
            data=result.data
        )



    async def get(
        self,
        product_id: str,
        id: str | None = None,
        **kwargs
    ) -> ProductVariation:
        """
        Retrieve a product variation

        Args:
            product_id: Unique identifier for the parent product
            id: Unique identifier for the variation
            **kwargs: Additional parameters

        Returns:
            ProductVariation
        """
        params = {k: v for k, v in {
            "product_id": product_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_variations", "get", params)
        return result



    async def search(
        self,
        query: ProductVariationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProductVariationsSearchResult:
        """
        Search product_variations records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProductVariationsSearchFilter):
        - attributes: List of attributes
        - backordered: On backordered
        - backorders: Backorders allowed setting
        - backorders_allowed: Shows if backorders are allowed
        - date_created: The date the variation was created
        - date_created_gmt: The date the variation was created, as GMT
        - date_modified: The date the variation was last modified
        - date_modified_gmt: The date the variation was last modified, as GMT
        - date_on_sale_from: Start date of sale price
        - date_on_sale_from_gmt: Start date of sale price, as GMT
        - date_on_sale_to: End date of sale price
        - date_on_sale_to_gmt: End date of sale price, as GMT
        - description: Variation description
        - dimensions: Variation dimensions
        - download_expiry: Days until access expires
        - download_limit: Download limit
        - downloadable: If downloadable
        - downloads: Downloadable files
        - id: Unique identifier
        - image: Variation image data
        - manage_stock: Stock management at variation level
        - menu_order: Menu order
        - meta_data: Meta data
        - on_sale: Shows if on sale
        - permalink: Variation URL
        - price: Current variation price
        - purchasable: Can be bought
        - regular_price: Variation regular price
        - sale_price: Variation sale price
        - shipping_class: Shipping class slug
        - shipping_class_id: Shipping class ID
        - sku: Unique identifier (SKU)
        - status: Variation status
        - stock_quantity: Stock quantity
        - stock_status: Controls the stock status
        - tax_class: Tax class
        - tax_status: Tax status
        - virtual: If virtual
        - weight: Variation weight

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProductVariationsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("product_variations", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProductVariationsSearchResult(
            data=[
                ProductVariationsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class OrderNotesQuery:
    """
    Query class for OrderNotes entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        order_id: str,
        type: str | None = None,
        **kwargs
    ) -> OrderNotesListResult:
        """
        List order notes

        Args:
            order_id: Unique identifier for the order
            type: Limit result set to a specific note type
            **kwargs: Additional parameters

        Returns:
            OrderNotesListResult
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            "type": type,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("order_notes", "list", params)
        # Cast generic envelope to concrete typed result
        return OrderNotesListResult(
            data=result.data
        )



    async def get(
        self,
        order_id: str,
        id: str | None = None,
        **kwargs
    ) -> OrderNote:
        """
        Retrieve an order note

        Args:
            order_id: Unique identifier for the order
            id: Unique identifier for the note
            **kwargs: Additional parameters

        Returns:
            OrderNote
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("order_notes", "get", params)
        return result



    async def search(
        self,
        query: OrderNotesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OrderNotesSearchResult:
        """
        Search order_notes records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OrderNotesSearchFilter):
        - author: Order note author
        - date_created: The date the order note was created
        - date_created_gmt: The date the order note was created, as GMT
        - id: Unique identifier
        - note: Order note content

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OrderNotesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("order_notes", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OrderNotesSearchResult(
            data=[
                OrderNotesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class RefundsQuery:
    """
    Query class for Refunds entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        order_id: str,
        page: int | None = None,
        per_page: int | None = None,
        **kwargs
    ) -> RefundsListResult:
        """
        List order refunds

        Args:
            order_id: Unique identifier for the order
            page: Current page of the collection
            per_page: Maximum number of items to return per page
            **kwargs: Additional parameters

        Returns:
            RefundsListResult
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            "page": page,
            "per_page": per_page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("refunds", "list", params)
        # Cast generic envelope to concrete typed result
        return RefundsListResult(
            data=result.data
        )



    async def get(
        self,
        order_id: str,
        id: str | None = None,
        **kwargs
    ) -> Refund:
        """
        Retrieve a refund

        Args:
            order_id: Unique identifier for the order
            id: Unique identifier for the refund
            **kwargs: Additional parameters

        Returns:
            Refund
        """
        params = {k: v for k, v in {
            "order_id": order_id,
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("refunds", "get", params)
        return result



    async def search(
        self,
        query: RefundsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> RefundsSearchResult:
        """
        Search refunds records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (RefundsSearchFilter):
        - amount: Refund amount
        - date_created: The date the refund was created
        - date_created_gmt: The date the refund was created, as GMT
        - id: Unique identifier
        - line_items: Line items data
        - meta_data: Meta data
        - reason: Reason for refund
        - refunded_by: User ID of user who created the refund
        - refunded_payment: If the payment was refunded via the API

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            RefundsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("refunds", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return RefundsSearchResult(
            data=[
                RefundsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class PaymentGatewaysQuery:
    """
    Query class for PaymentGateways entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> PaymentGatewaysListResult:
        """
        List payment gateways

        Returns:
            PaymentGatewaysListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("payment_gateways", "list", params)
        # Cast generic envelope to concrete typed result
        return PaymentGatewaysListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> PaymentGateway:
        """
        Retrieve a payment gateway

        Args:
            id: Unique identifier for the payment gateway
            **kwargs: Additional parameters

        Returns:
            PaymentGateway
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("payment_gateways", "get", params)
        return result



    async def search(
        self,
        query: PaymentGatewaysSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> PaymentGatewaysSearchResult:
        """
        Search payment_gateways records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (PaymentGatewaysSearchFilter):
        - description: Payment gateway description on checkout
        - enabled: Payment gateway enabled status
        - id: Payment gateway ID
        - method_description: Payment gateway method description
        - method_supports: Supported features
        - method_title: Payment gateway method title
        - order: Payment gateway sort order
        - settings: Payment gateway settings
        - title: Payment gateway title on checkout

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            PaymentGatewaysSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("payment_gateways", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return PaymentGatewaysSearchResult(
            data=[
                PaymentGatewaysSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ShippingMethodsQuery:
    """
    Query class for ShippingMethods entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> ShippingMethodsListResult:
        """
        List shipping methods

        Returns:
            ShippingMethodsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("shipping_methods", "list", params)
        # Cast generic envelope to concrete typed result
        return ShippingMethodsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ShippingMethod:
        """
        Retrieve a shipping method

        Args:
            id: Unique identifier for the shipping method
            **kwargs: Additional parameters

        Returns:
            ShippingMethod
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("shipping_methods", "get", params)
        return result



    async def search(
        self,
        query: ShippingMethodsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ShippingMethodsSearchResult:
        """
        Search shipping_methods records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ShippingMethodsSearchFilter):
        - description: Shipping method description
        - id: Method ID
        - title: Shipping method title

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ShippingMethodsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("shipping_methods", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ShippingMethodsSearchResult(
            data=[
                ShippingMethodsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ShippingZonesQuery:
    """
    Query class for ShippingZones entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> ShippingZonesListResult:
        """
        List shipping zones

        Returns:
            ShippingZonesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("shipping_zones", "list", params)
        # Cast generic envelope to concrete typed result
        return ShippingZonesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ShippingZone:
        """
        Retrieve a shipping zone

        Args:
            id: Unique identifier for the shipping zone
            **kwargs: Additional parameters

        Returns:
            ShippingZone
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("shipping_zones", "get", params)
        return result



    async def search(
        self,
        query: ShippingZonesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ShippingZonesSearchResult:
        """
        Search shipping_zones records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ShippingZonesSearchFilter):
        - id: Unique identifier
        - name: Shipping zone name
        - order: Shipping zone order

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ShippingZonesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("shipping_zones", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ShippingZonesSearchResult(
            data=[
                ShippingZonesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TaxRatesQuery:
    """
    Query class for TaxRates entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page: int | None = None,
        per_page: int | None = None,
        class_: str | None = None,
        orderby: str | None = None,
        order: str | None = None,
        **kwargs
    ) -> TaxRatesListResult:
        """
        List tax rates

        Args:
            page: Current page of the collection
            per_page: Maximum number of items to return per page
            class_: Sort by tax class
            orderby: Sort collection by attribute
            order: Order sort attribute ascending or descending
            **kwargs: Additional parameters

        Returns:
            TaxRatesListResult
        """
        params = {k: v for k, v in {
            "page": page,
            "per_page": per_page,
            "class": class_,
            "orderby": orderby,
            "order": order,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tax_rates", "list", params)
        # Cast generic envelope to concrete typed result
        return TaxRatesListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> TaxRate:
        """
        Retrieve a tax rate

        Args:
            id: Unique identifier for the tax rate
            **kwargs: Additional parameters

        Returns:
            TaxRate
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tax_rates", "get", params)
        return result



    async def search(
        self,
        query: TaxRatesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TaxRatesSearchResult:
        """
        Search tax_rates records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TaxRatesSearchFilter):
        - cities: City names
        - city: City name
        - class_: Tax class
        - compound: Whether this is a compound rate
        - country: Country ISO 3166 code
        - id: Unique identifier
        - name: Tax rate name
        - order: Order in queries
        - postcode: Postcode/ZIP
        - postcodes: Postcodes/ZIPs
        - priority: Tax priority
        - rate: Tax rate
        - shipping: Applied to shipping
        - state: State code

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TaxRatesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("tax_rates", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TaxRatesSearchResult(
            data=[
                TaxRatesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TaxClassesQuery:
    """
    Query class for TaxClasses entity operations.
    """

    def __init__(self, connector: WoocommerceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> TaxClassesListResult:
        """
        List tax classes

        Returns:
            TaxClassesListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tax_classes", "list", params)
        # Cast generic envelope to concrete typed result
        return TaxClassesListResult(
            data=result.data
        )



    async def search(
        self,
        query: TaxClassesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TaxClassesSearchResult:
        """
        Search tax_classes records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TaxClassesSearchFilter):
        - name: Tax class name
        - slug: Unique identifier

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TaxClassesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("tax_classes", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TaxClassesSearchResult(
            data=[
                TaxClassesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
