"""
Type definitions for shopify connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class CustomersListParams(TypedDict):
    """Parameters for customers.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]

class CustomersGetParams(TypedDict):
    """Parameters for customers.get operation"""
    customer_id: str

class OrdersListParams(TypedDict):
    """Parameters for orders.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]
    status: NotRequired[str]
    financial_status: NotRequired[str]
    fulfillment_status: NotRequired[str]

class OrdersGetParams(TypedDict):
    """Parameters for orders.get operation"""
    order_id: str

class ProductsListParams(TypedDict):
    """Parameters for products.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]
    status: NotRequired[str]
    product_type: NotRequired[str]
    vendor: NotRequired[str]
    collection_id: NotRequired[int]

class ProductsGetParams(TypedDict):
    """Parameters for products.get operation"""
    product_id: str

class ProductVariantsListParams(TypedDict):
    """Parameters for product_variants.list operation"""
    product_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]

class ProductVariantsGetParams(TypedDict):
    """Parameters for product_variants.get operation"""
    variant_id: str

class ProductImagesListParams(TypedDict):
    """Parameters for product_images.list operation"""
    product_id: str
    since_id: NotRequired[int]

class ProductImagesGetParams(TypedDict):
    """Parameters for product_images.get operation"""
    product_id: str
    image_id: str

class AbandonedCheckoutsListParams(TypedDict):
    """Parameters for abandoned_checkouts.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]
    status: NotRequired[str]

class LocationsListParams(TypedDict):
    """Parameters for locations.list operation"""
    pass

class LocationsGetParams(TypedDict):
    """Parameters for locations.get operation"""
    location_id: str

class InventoryLevelsListParams(TypedDict):
    """Parameters for inventory_levels.list operation"""
    location_id: str
    limit: NotRequired[int]

class InventoryItemsListParams(TypedDict):
    """Parameters for inventory_items.list operation"""
    ids: str
    limit: NotRequired[int]

class InventoryItemsGetParams(TypedDict):
    """Parameters for inventory_items.get operation"""
    inventory_item_id: str

class ShopGetParams(TypedDict):
    """Parameters for shop.get operation"""
    pass

class PriceRulesListParams(TypedDict):
    """Parameters for price_rules.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]

class PriceRulesGetParams(TypedDict):
    """Parameters for price_rules.get operation"""
    price_rule_id: str

class DiscountCodesListParams(TypedDict):
    """Parameters for discount_codes.list operation"""
    price_rule_id: str
    limit: NotRequired[int]

class DiscountCodesGetParams(TypedDict):
    """Parameters for discount_codes.get operation"""
    price_rule_id: str
    discount_code_id: str

class CustomCollectionsListParams(TypedDict):
    """Parameters for custom_collections.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    title: NotRequired[str]
    product_id: NotRequired[int]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]

class CustomCollectionsGetParams(TypedDict):
    """Parameters for custom_collections.get operation"""
    collection_id: str

class SmartCollectionsListParams(TypedDict):
    """Parameters for smart_collections.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    title: NotRequired[str]
    product_id: NotRequired[int]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]

class SmartCollectionsGetParams(TypedDict):
    """Parameters for smart_collections.get operation"""
    collection_id: str

class CollectsListParams(TypedDict):
    """Parameters for collects.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    collection_id: NotRequired[int]
    product_id: NotRequired[int]

class CollectsGetParams(TypedDict):
    """Parameters for collects.get operation"""
    collect_id: str

class DraftOrdersListParams(TypedDict):
    """Parameters for draft_orders.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    status: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]

class DraftOrdersGetParams(TypedDict):
    """Parameters for draft_orders.get operation"""
    draft_order_id: str

class FulfillmentsListParams(TypedDict):
    """Parameters for fulfillments.list operation"""
    order_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]

class FulfillmentsGetParams(TypedDict):
    """Parameters for fulfillments.get operation"""
    order_id: str
    fulfillment_id: str

class OrderRefundsListParams(TypedDict):
    """Parameters for order_refunds.list operation"""
    order_id: str
    limit: NotRequired[int]

class OrderRefundsGetParams(TypedDict):
    """Parameters for order_refunds.get operation"""
    order_id: str
    refund_id: str

class TransactionsListParams(TypedDict):
    """Parameters for transactions.list operation"""
    order_id: str
    since_id: NotRequired[int]

class TransactionsGetParams(TypedDict):
    """Parameters for transactions.get operation"""
    order_id: str
    transaction_id: str

class TenderTransactionsListParams(TypedDict):
    """Parameters for tender_transactions.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    processed_at_min: NotRequired[str]
    processed_at_max: NotRequired[str]
    order: NotRequired[str]

class CountriesListParams(TypedDict):
    """Parameters for countries.list operation"""
    since_id: NotRequired[int]

class CountriesGetParams(TypedDict):
    """Parameters for countries.get operation"""
    country_id: str

class MetafieldShopsListParams(TypedDict):
    """Parameters for metafield_shops.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]
    type: NotRequired[str]

class MetafieldShopsGetParams(TypedDict):
    """Parameters for metafield_shops.get operation"""
    metafield_id: str

class MetafieldCustomersListParams(TypedDict):
    """Parameters for metafield_customers.list operation"""
    customer_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldProductsListParams(TypedDict):
    """Parameters for metafield_products.list operation"""
    product_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldOrdersListParams(TypedDict):
    """Parameters for metafield_orders.list operation"""
    order_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldDraftOrdersListParams(TypedDict):
    """Parameters for metafield_draft_orders.list operation"""
    draft_order_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldLocationsListParams(TypedDict):
    """Parameters for metafield_locations.list operation"""
    location_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldProductVariantsListParams(TypedDict):
    """Parameters for metafield_product_variants.list operation"""
    variant_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldSmartCollectionsListParams(TypedDict):
    """Parameters for metafield_smart_collections.list operation"""
    collection_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class MetafieldProductImagesListParams(TypedDict):
    """Parameters for metafield_product_images.list operation"""
    product_id: str
    image_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    namespace: NotRequired[str]
    key: NotRequired[str]

class CustomerAddressListParams(TypedDict):
    """Parameters for customer_address.list operation"""
    customer_id: str
    limit: NotRequired[int]

class CustomerAddressGetParams(TypedDict):
    """Parameters for customer_address.get operation"""
    customer_id: str
    address_id: str

class FulfillmentOrdersListParams(TypedDict):
    """Parameters for fulfillment_orders.list operation"""
    order_id: str

class FulfillmentOrdersGetParams(TypedDict):
    """Parameters for fulfillment_orders.get operation"""
    fulfillment_order_id: str

