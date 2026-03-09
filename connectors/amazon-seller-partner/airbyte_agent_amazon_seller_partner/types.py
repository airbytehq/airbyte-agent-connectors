"""
Type definitions for amazon-seller-partner connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class OrdersListParams(TypedDict):
    """Parameters for orders.list operation"""
    marketplace_ids: str
    created_after: NotRequired[str]
    created_before: NotRequired[str]
    last_updated_after: NotRequired[str]
    last_updated_before: NotRequired[str]
    order_statuses: NotRequired[str]
    max_results_per_page: NotRequired[int]
    next_token: NotRequired[str]

class OrdersGetParams(TypedDict):
    """Parameters for orders.get operation"""
    order_id: str

class OrderItemsListParams(TypedDict):
    """Parameters for order_items.list operation"""
    order_id: str
    next_token: NotRequired[str]

class ListFinancialEventGroupsListParams(TypedDict):
    """Parameters for list_financial_event_groups.list operation"""
    financial_event_group_started_after: NotRequired[str]
    financial_event_group_started_before: NotRequired[str]
    max_results_per_page: NotRequired[int]
    next_token: NotRequired[str]

class ListFinancialEventsListParams(TypedDict):
    """Parameters for list_financial_events.list operation"""
    posted_after: NotRequired[str]
    posted_before: NotRequired[str]
    max_results_per_page: NotRequired[int]
    next_token: NotRequired[str]

class CatalogItemsListParams(TypedDict):
    """Parameters for catalog_items.list operation"""
    marketplace_ids: str
    keywords: NotRequired[str]
    identifiers: NotRequired[str]
    identifiers_type: NotRequired[str]
    included_data: NotRequired[str]
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class CatalogItemsGetParams(TypedDict):
    """Parameters for catalog_items.get operation"""
    asin: str
    marketplace_ids: str
    included_data: NotRequired[str]

class ReportsListParams(TypedDict):
    """Parameters for reports.list operation"""
    report_types: NotRequired[str]
    processing_statuses: NotRequired[str]
    marketplace_ids: NotRequired[str]
    page_size: NotRequired[int]
    created_since: NotRequired[str]
    created_until: NotRequired[str]
    next_token: NotRequired[str]

class ReportsGetParams(TypedDict):
    """Parameters for reports.get operation"""
    report_id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ORDERS SEARCH TYPES =====

class OrdersSearchFilter(TypedDict, total=False):
    """Available fields for filtering orders search queries."""
    amazon_order_id: str | None
    """Unique identifier for the Amazon order"""
    automated_shipping_settings: dict[str, Any] | None
    """Settings related to automated shipping processes"""
    buyer_info: dict[str, Any] | None
    """Information about the buyer"""
    default_ship_from_location_address: dict[str, Any] | None
    """The default address from which orders are shipped"""
    earliest_delivery_date: str | None
    """Earliest estimated delivery date of the order"""
    earliest_ship_date: str | None
    """Earliest shipment date for the order"""
    fulfillment_channel: str | None
    """Channel through which the order is fulfilled"""
    has_regulated_items: bool | None
    """Indicates if the order has regulated items"""
    is_access_point_order: bool | None
    """Indicates if the order is an Amazon Hub Counter order"""
    is_business_order: bool | None
    """Indicates if the order is a business order"""
    is_global_express_enabled: bool | None
    """Indicates if global express is enabled for the order"""
    is_ispu: bool | None
    """Indicates if the order is for In-Store Pickup"""
    is_premium_order: bool | None
    """Indicates if the order is a premium order"""
    is_prime: bool | None
    """Indicates if the order is a Prime order"""
    is_replacement_order: str | None
    """Indicates if the order is a replacement order"""
    is_sold_by_ab: bool | None
    """Indicates if the order is sold by Amazon Business"""
    last_update_date: str | None
    """Date and time when the order was last updated"""
    latest_delivery_date: str | None
    """Latest estimated delivery date of the order"""
    latest_ship_date: str | None
    """Latest shipment date for the order"""
    marketplace_id: str | None
    """Identifier for the marketplace where the order was placed"""
    number_of_items_shipped: int | None
    """Number of items shipped in the order"""
    number_of_items_unshipped: int | None
    """Number of items yet to be shipped in the order"""
    order_status: str | None
    """Status of the order"""
    order_total: dict[str, Any] | None
    """Total amount of the order"""
    order_type: str | None
    """Type of the order"""
    payment_method: str | None
    """Payment method used for the order"""
    payment_method_details: list[Any] | None
    """Details of the payment method used for the order"""
    purchase_date: str | None
    """Date and time when the order was purchased"""
    sales_channel: str | None
    """Channel through which the order was sold"""
    seller_order_id: str | None
    """Unique identifier given by the seller for the order"""
    ship_service_level: str | None
    """Service level for shipping the order"""
    shipment_service_level_category: str | None
    """Service level category for shipping the order"""
    shipping_address: dict[str, Any] | None
    """The address to which the order will be shipped"""
    seller_id: str | None
    """Identifier for the seller associated with the order"""


class OrdersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    amazon_order_id: list[str]
    """Unique identifier for the Amazon order"""
    automated_shipping_settings: list[dict[str, Any]]
    """Settings related to automated shipping processes"""
    buyer_info: list[dict[str, Any]]
    """Information about the buyer"""
    default_ship_from_location_address: list[dict[str, Any]]
    """The default address from which orders are shipped"""
    earliest_delivery_date: list[str]
    """Earliest estimated delivery date of the order"""
    earliest_ship_date: list[str]
    """Earliest shipment date for the order"""
    fulfillment_channel: list[str]
    """Channel through which the order is fulfilled"""
    has_regulated_items: list[bool]
    """Indicates if the order has regulated items"""
    is_access_point_order: list[bool]
    """Indicates if the order is an Amazon Hub Counter order"""
    is_business_order: list[bool]
    """Indicates if the order is a business order"""
    is_global_express_enabled: list[bool]
    """Indicates if global express is enabled for the order"""
    is_ispu: list[bool]
    """Indicates if the order is for In-Store Pickup"""
    is_premium_order: list[bool]
    """Indicates if the order is a premium order"""
    is_prime: list[bool]
    """Indicates if the order is a Prime order"""
    is_replacement_order: list[str]
    """Indicates if the order is a replacement order"""
    is_sold_by_ab: list[bool]
    """Indicates if the order is sold by Amazon Business"""
    last_update_date: list[str]
    """Date and time when the order was last updated"""
    latest_delivery_date: list[str]
    """Latest estimated delivery date of the order"""
    latest_ship_date: list[str]
    """Latest shipment date for the order"""
    marketplace_id: list[str]
    """Identifier for the marketplace where the order was placed"""
    number_of_items_shipped: list[int]
    """Number of items shipped in the order"""
    number_of_items_unshipped: list[int]
    """Number of items yet to be shipped in the order"""
    order_status: list[str]
    """Status of the order"""
    order_total: list[dict[str, Any]]
    """Total amount of the order"""
    order_type: list[str]
    """Type of the order"""
    payment_method: list[str]
    """Payment method used for the order"""
    payment_method_details: list[list[Any]]
    """Details of the payment method used for the order"""
    purchase_date: list[str]
    """Date and time when the order was purchased"""
    sales_channel: list[str]
    """Channel through which the order was sold"""
    seller_order_id: list[str]
    """Unique identifier given by the seller for the order"""
    ship_service_level: list[str]
    """Service level for shipping the order"""
    shipment_service_level_category: list[str]
    """Service level category for shipping the order"""
    shipping_address: list[dict[str, Any]]
    """The address to which the order will be shipped"""
    seller_id: list[str]
    """Identifier for the seller associated with the order"""


class OrdersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    amazon_order_id: Any
    """Unique identifier for the Amazon order"""
    automated_shipping_settings: Any
    """Settings related to automated shipping processes"""
    buyer_info: Any
    """Information about the buyer"""
    default_ship_from_location_address: Any
    """The default address from which orders are shipped"""
    earliest_delivery_date: Any
    """Earliest estimated delivery date of the order"""
    earliest_ship_date: Any
    """Earliest shipment date for the order"""
    fulfillment_channel: Any
    """Channel through which the order is fulfilled"""
    has_regulated_items: Any
    """Indicates if the order has regulated items"""
    is_access_point_order: Any
    """Indicates if the order is an Amazon Hub Counter order"""
    is_business_order: Any
    """Indicates if the order is a business order"""
    is_global_express_enabled: Any
    """Indicates if global express is enabled for the order"""
    is_ispu: Any
    """Indicates if the order is for In-Store Pickup"""
    is_premium_order: Any
    """Indicates if the order is a premium order"""
    is_prime: Any
    """Indicates if the order is a Prime order"""
    is_replacement_order: Any
    """Indicates if the order is a replacement order"""
    is_sold_by_ab: Any
    """Indicates if the order is sold by Amazon Business"""
    last_update_date: Any
    """Date and time when the order was last updated"""
    latest_delivery_date: Any
    """Latest estimated delivery date of the order"""
    latest_ship_date: Any
    """Latest shipment date for the order"""
    marketplace_id: Any
    """Identifier for the marketplace where the order was placed"""
    number_of_items_shipped: Any
    """Number of items shipped in the order"""
    number_of_items_unshipped: Any
    """Number of items yet to be shipped in the order"""
    order_status: Any
    """Status of the order"""
    order_total: Any
    """Total amount of the order"""
    order_type: Any
    """Type of the order"""
    payment_method: Any
    """Payment method used for the order"""
    payment_method_details: Any
    """Details of the payment method used for the order"""
    purchase_date: Any
    """Date and time when the order was purchased"""
    sales_channel: Any
    """Channel through which the order was sold"""
    seller_order_id: Any
    """Unique identifier given by the seller for the order"""
    ship_service_level: Any
    """Service level for shipping the order"""
    shipment_service_level_category: Any
    """Service level category for shipping the order"""
    shipping_address: Any
    """The address to which the order will be shipped"""
    seller_id: Any
    """Identifier for the seller associated with the order"""


class OrdersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    amazon_order_id: str
    """Unique identifier for the Amazon order"""
    automated_shipping_settings: str
    """Settings related to automated shipping processes"""
    buyer_info: str
    """Information about the buyer"""
    default_ship_from_location_address: str
    """The default address from which orders are shipped"""
    earliest_delivery_date: str
    """Earliest estimated delivery date of the order"""
    earliest_ship_date: str
    """Earliest shipment date for the order"""
    fulfillment_channel: str
    """Channel through which the order is fulfilled"""
    has_regulated_items: str
    """Indicates if the order has regulated items"""
    is_access_point_order: str
    """Indicates if the order is an Amazon Hub Counter order"""
    is_business_order: str
    """Indicates if the order is a business order"""
    is_global_express_enabled: str
    """Indicates if global express is enabled for the order"""
    is_ispu: str
    """Indicates if the order is for In-Store Pickup"""
    is_premium_order: str
    """Indicates if the order is a premium order"""
    is_prime: str
    """Indicates if the order is a Prime order"""
    is_replacement_order: str
    """Indicates if the order is a replacement order"""
    is_sold_by_ab: str
    """Indicates if the order is sold by Amazon Business"""
    last_update_date: str
    """Date and time when the order was last updated"""
    latest_delivery_date: str
    """Latest estimated delivery date of the order"""
    latest_ship_date: str
    """Latest shipment date for the order"""
    marketplace_id: str
    """Identifier for the marketplace where the order was placed"""
    number_of_items_shipped: str
    """Number of items shipped in the order"""
    number_of_items_unshipped: str
    """Number of items yet to be shipped in the order"""
    order_status: str
    """Status of the order"""
    order_total: str
    """Total amount of the order"""
    order_type: str
    """Type of the order"""
    payment_method: str
    """Payment method used for the order"""
    payment_method_details: str
    """Details of the payment method used for the order"""
    purchase_date: str
    """Date and time when the order was purchased"""
    sales_channel: str
    """Channel through which the order was sold"""
    seller_order_id: str
    """Unique identifier given by the seller for the order"""
    ship_service_level: str
    """Service level for shipping the order"""
    shipment_service_level_category: str
    """Service level category for shipping the order"""
    shipping_address: str
    """The address to which the order will be shipped"""
    seller_id: str
    """Identifier for the seller associated with the order"""


class OrdersSortFilter(TypedDict, total=False):
    """Available fields for sorting orders search results."""
    amazon_order_id: AirbyteSortOrder
    """Unique identifier for the Amazon order"""
    automated_shipping_settings: AirbyteSortOrder
    """Settings related to automated shipping processes"""
    buyer_info: AirbyteSortOrder
    """Information about the buyer"""
    default_ship_from_location_address: AirbyteSortOrder
    """The default address from which orders are shipped"""
    earliest_delivery_date: AirbyteSortOrder
    """Earliest estimated delivery date of the order"""
    earliest_ship_date: AirbyteSortOrder
    """Earliest shipment date for the order"""
    fulfillment_channel: AirbyteSortOrder
    """Channel through which the order is fulfilled"""
    has_regulated_items: AirbyteSortOrder
    """Indicates if the order has regulated items"""
    is_access_point_order: AirbyteSortOrder
    """Indicates if the order is an Amazon Hub Counter order"""
    is_business_order: AirbyteSortOrder
    """Indicates if the order is a business order"""
    is_global_express_enabled: AirbyteSortOrder
    """Indicates if global express is enabled for the order"""
    is_ispu: AirbyteSortOrder
    """Indicates if the order is for In-Store Pickup"""
    is_premium_order: AirbyteSortOrder
    """Indicates if the order is a premium order"""
    is_prime: AirbyteSortOrder
    """Indicates if the order is a Prime order"""
    is_replacement_order: AirbyteSortOrder
    """Indicates if the order is a replacement order"""
    is_sold_by_ab: AirbyteSortOrder
    """Indicates if the order is sold by Amazon Business"""
    last_update_date: AirbyteSortOrder
    """Date and time when the order was last updated"""
    latest_delivery_date: AirbyteSortOrder
    """Latest estimated delivery date of the order"""
    latest_ship_date: AirbyteSortOrder
    """Latest shipment date for the order"""
    marketplace_id: AirbyteSortOrder
    """Identifier for the marketplace where the order was placed"""
    number_of_items_shipped: AirbyteSortOrder
    """Number of items shipped in the order"""
    number_of_items_unshipped: AirbyteSortOrder
    """Number of items yet to be shipped in the order"""
    order_status: AirbyteSortOrder
    """Status of the order"""
    order_total: AirbyteSortOrder
    """Total amount of the order"""
    order_type: AirbyteSortOrder
    """Type of the order"""
    payment_method: AirbyteSortOrder
    """Payment method used for the order"""
    payment_method_details: AirbyteSortOrder
    """Details of the payment method used for the order"""
    purchase_date: AirbyteSortOrder
    """Date and time when the order was purchased"""
    sales_channel: AirbyteSortOrder
    """Channel through which the order was sold"""
    seller_order_id: AirbyteSortOrder
    """Unique identifier given by the seller for the order"""
    ship_service_level: AirbyteSortOrder
    """Service level for shipping the order"""
    shipment_service_level_category: AirbyteSortOrder
    """Service level category for shipping the order"""
    shipping_address: AirbyteSortOrder
    """The address to which the order will be shipped"""
    seller_id: AirbyteSortOrder
    """Identifier for the seller associated with the order"""


# Entity-specific condition types for orders
class OrdersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OrdersSearchFilter


class OrdersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OrdersSearchFilter


class OrdersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OrdersSearchFilter


class OrdersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OrdersSearchFilter


class OrdersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OrdersSearchFilter


class OrdersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OrdersSearchFilter


class OrdersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OrdersStringFilter


class OrdersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OrdersStringFilter


class OrdersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OrdersStringFilter


class OrdersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OrdersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OrdersInCondition = TypedDict("OrdersInCondition", {"in": OrdersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OrdersNotCondition = TypedDict("OrdersNotCondition", {"not": "OrdersCondition"}, total=False)
"""Negates the nested condition."""

OrdersAndCondition = TypedDict("OrdersAndCondition", {"and": "list[OrdersCondition]"}, total=False)
"""True if all nested conditions are true."""

OrdersOrCondition = TypedDict("OrdersOrCondition", {"or": "list[OrdersCondition]"}, total=False)
"""True if any nested condition is true."""

OrdersAnyCondition = TypedDict("OrdersAnyCondition", {"any": OrdersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all orders condition types
OrdersCondition = (
    OrdersEqCondition
    | OrdersNeqCondition
    | OrdersGtCondition
    | OrdersGteCondition
    | OrdersLtCondition
    | OrdersLteCondition
    | OrdersInCondition
    | OrdersLikeCondition
    | OrdersFuzzyCondition
    | OrdersKeywordCondition
    | OrdersContainsCondition
    | OrdersNotCondition
    | OrdersAndCondition
    | OrdersOrCondition
    | OrdersAnyCondition
)


class OrdersSearchQuery(TypedDict, total=False):
    """Search query for orders entity."""
    filter: OrdersCondition
    sort: list[OrdersSortFilter]


# ===== ORDER_ITEMS SEARCH TYPES =====

class OrderItemsSearchFilter(TypedDict, total=False):
    """Available fields for filtering order_items search queries."""
    asin: str | None
    """Amazon Standard Identification Number of the product"""
    amazon_order_id: str | None
    """ID of the Amazon order"""
    buyer_info: dict[str, Any] | None
    """Information about the buyer"""
    buyer_requested_cancel: dict[str, Any] | None
    """Information about buyer's request for cancellation"""
    cod_fee: dict[str, Any] | None
    """Cash on delivery fee"""
    cod_fee_discount: dict[str, Any] | None
    """Discount on cash on delivery fee"""
    condition_id: str | None
    """Condition ID of the product"""
    condition_note: str | None
    """Additional notes on the condition of the product"""
    condition_subtype_id: str | None
    """Subtype ID of the product condition"""
    deemed_reseller_category: str | None
    """Category indicating if the seller is considered a reseller"""
    ioss_number: str | None
    """Import One Stop Shop number"""
    is_gift: str | None
    """Flag indicating if the order is a gift"""
    is_transparency: bool | None
    """Flag indicating if transparency is applied"""
    item_price: dict[str, Any] | None
    """Price of the item"""
    item_tax: dict[str, Any] | None
    """Tax applied on the item"""
    last_update_date: str | None
    """Date and time of the last update"""
    order_item_id: str | None
    """ID of the order item"""
    points_granted: dict[str, Any] | None
    """Points granted for the purchase"""
    price_designation: str | None
    """Designation of the price"""
    product_info: dict[str, Any] | None
    """Information about the product"""
    promotion_discount: dict[str, Any] | None
    """Discount applied due to promotion"""
    promotion_discount_tax: dict[str, Any] | None
    """Tax applied on the promotion discount"""
    promotion_ids: list[Any] | None
    """IDs of promotions applied"""
    quantity_ordered: int | None
    """Quantity of the item ordered"""
    quantity_shipped: int | None
    """Quantity of the item shipped"""
    scheduled_delivery_end_date: str | None
    """End date for scheduled delivery"""
    scheduled_delivery_start_date: str | None
    """Start date for scheduled delivery"""
    seller_sku: str | None
    """SKU of the seller"""
    serial_number_required: bool | None
    """Flag indicating if serial number is required"""
    serial_numbers: list[Any] | None
    """List of serial numbers"""
    shipping_discount: dict[str, Any] | None
    """Discount applied on shipping"""
    shipping_discount_tax: dict[str, Any] | None
    """Tax applied on the shipping discount"""
    shipping_price: dict[str, Any] | None
    """Price of shipping"""
    shipping_tax: dict[str, Any] | None
    """Tax applied on shipping"""
    store_chain_store_id: str | None
    """ID of the store chain"""
    tax_collection: dict[str, Any] | None
    """Information about tax collection"""
    title: str | None
    """Title of the product"""


class OrderItemsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    asin: list[str]
    """Amazon Standard Identification Number of the product"""
    amazon_order_id: list[str]
    """ID of the Amazon order"""
    buyer_info: list[dict[str, Any]]
    """Information about the buyer"""
    buyer_requested_cancel: list[dict[str, Any]]
    """Information about buyer's request for cancellation"""
    cod_fee: list[dict[str, Any]]
    """Cash on delivery fee"""
    cod_fee_discount: list[dict[str, Any]]
    """Discount on cash on delivery fee"""
    condition_id: list[str]
    """Condition ID of the product"""
    condition_note: list[str]
    """Additional notes on the condition of the product"""
    condition_subtype_id: list[str]
    """Subtype ID of the product condition"""
    deemed_reseller_category: list[str]
    """Category indicating if the seller is considered a reseller"""
    ioss_number: list[str]
    """Import One Stop Shop number"""
    is_gift: list[str]
    """Flag indicating if the order is a gift"""
    is_transparency: list[bool]
    """Flag indicating if transparency is applied"""
    item_price: list[dict[str, Any]]
    """Price of the item"""
    item_tax: list[dict[str, Any]]
    """Tax applied on the item"""
    last_update_date: list[str]
    """Date and time of the last update"""
    order_item_id: list[str]
    """ID of the order item"""
    points_granted: list[dict[str, Any]]
    """Points granted for the purchase"""
    price_designation: list[str]
    """Designation of the price"""
    product_info: list[dict[str, Any]]
    """Information about the product"""
    promotion_discount: list[dict[str, Any]]
    """Discount applied due to promotion"""
    promotion_discount_tax: list[dict[str, Any]]
    """Tax applied on the promotion discount"""
    promotion_ids: list[list[Any]]
    """IDs of promotions applied"""
    quantity_ordered: list[int]
    """Quantity of the item ordered"""
    quantity_shipped: list[int]
    """Quantity of the item shipped"""
    scheduled_delivery_end_date: list[str]
    """End date for scheduled delivery"""
    scheduled_delivery_start_date: list[str]
    """Start date for scheduled delivery"""
    seller_sku: list[str]
    """SKU of the seller"""
    serial_number_required: list[bool]
    """Flag indicating if serial number is required"""
    serial_numbers: list[list[Any]]
    """List of serial numbers"""
    shipping_discount: list[dict[str, Any]]
    """Discount applied on shipping"""
    shipping_discount_tax: list[dict[str, Any]]
    """Tax applied on the shipping discount"""
    shipping_price: list[dict[str, Any]]
    """Price of shipping"""
    shipping_tax: list[dict[str, Any]]
    """Tax applied on shipping"""
    store_chain_store_id: list[str]
    """ID of the store chain"""
    tax_collection: list[dict[str, Any]]
    """Information about tax collection"""
    title: list[str]
    """Title of the product"""


class OrderItemsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    asin: Any
    """Amazon Standard Identification Number of the product"""
    amazon_order_id: Any
    """ID of the Amazon order"""
    buyer_info: Any
    """Information about the buyer"""
    buyer_requested_cancel: Any
    """Information about buyer's request for cancellation"""
    cod_fee: Any
    """Cash on delivery fee"""
    cod_fee_discount: Any
    """Discount on cash on delivery fee"""
    condition_id: Any
    """Condition ID of the product"""
    condition_note: Any
    """Additional notes on the condition of the product"""
    condition_subtype_id: Any
    """Subtype ID of the product condition"""
    deemed_reseller_category: Any
    """Category indicating if the seller is considered a reseller"""
    ioss_number: Any
    """Import One Stop Shop number"""
    is_gift: Any
    """Flag indicating if the order is a gift"""
    is_transparency: Any
    """Flag indicating if transparency is applied"""
    item_price: Any
    """Price of the item"""
    item_tax: Any
    """Tax applied on the item"""
    last_update_date: Any
    """Date and time of the last update"""
    order_item_id: Any
    """ID of the order item"""
    points_granted: Any
    """Points granted for the purchase"""
    price_designation: Any
    """Designation of the price"""
    product_info: Any
    """Information about the product"""
    promotion_discount: Any
    """Discount applied due to promotion"""
    promotion_discount_tax: Any
    """Tax applied on the promotion discount"""
    promotion_ids: Any
    """IDs of promotions applied"""
    quantity_ordered: Any
    """Quantity of the item ordered"""
    quantity_shipped: Any
    """Quantity of the item shipped"""
    scheduled_delivery_end_date: Any
    """End date for scheduled delivery"""
    scheduled_delivery_start_date: Any
    """Start date for scheduled delivery"""
    seller_sku: Any
    """SKU of the seller"""
    serial_number_required: Any
    """Flag indicating if serial number is required"""
    serial_numbers: Any
    """List of serial numbers"""
    shipping_discount: Any
    """Discount applied on shipping"""
    shipping_discount_tax: Any
    """Tax applied on the shipping discount"""
    shipping_price: Any
    """Price of shipping"""
    shipping_tax: Any
    """Tax applied on shipping"""
    store_chain_store_id: Any
    """ID of the store chain"""
    tax_collection: Any
    """Information about tax collection"""
    title: Any
    """Title of the product"""


class OrderItemsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    asin: str
    """Amazon Standard Identification Number of the product"""
    amazon_order_id: str
    """ID of the Amazon order"""
    buyer_info: str
    """Information about the buyer"""
    buyer_requested_cancel: str
    """Information about buyer's request for cancellation"""
    cod_fee: str
    """Cash on delivery fee"""
    cod_fee_discount: str
    """Discount on cash on delivery fee"""
    condition_id: str
    """Condition ID of the product"""
    condition_note: str
    """Additional notes on the condition of the product"""
    condition_subtype_id: str
    """Subtype ID of the product condition"""
    deemed_reseller_category: str
    """Category indicating if the seller is considered a reseller"""
    ioss_number: str
    """Import One Stop Shop number"""
    is_gift: str
    """Flag indicating if the order is a gift"""
    is_transparency: str
    """Flag indicating if transparency is applied"""
    item_price: str
    """Price of the item"""
    item_tax: str
    """Tax applied on the item"""
    last_update_date: str
    """Date and time of the last update"""
    order_item_id: str
    """ID of the order item"""
    points_granted: str
    """Points granted for the purchase"""
    price_designation: str
    """Designation of the price"""
    product_info: str
    """Information about the product"""
    promotion_discount: str
    """Discount applied due to promotion"""
    promotion_discount_tax: str
    """Tax applied on the promotion discount"""
    promotion_ids: str
    """IDs of promotions applied"""
    quantity_ordered: str
    """Quantity of the item ordered"""
    quantity_shipped: str
    """Quantity of the item shipped"""
    scheduled_delivery_end_date: str
    """End date for scheduled delivery"""
    scheduled_delivery_start_date: str
    """Start date for scheduled delivery"""
    seller_sku: str
    """SKU of the seller"""
    serial_number_required: str
    """Flag indicating if serial number is required"""
    serial_numbers: str
    """List of serial numbers"""
    shipping_discount: str
    """Discount applied on shipping"""
    shipping_discount_tax: str
    """Tax applied on the shipping discount"""
    shipping_price: str
    """Price of shipping"""
    shipping_tax: str
    """Tax applied on shipping"""
    store_chain_store_id: str
    """ID of the store chain"""
    tax_collection: str
    """Information about tax collection"""
    title: str
    """Title of the product"""


class OrderItemsSortFilter(TypedDict, total=False):
    """Available fields for sorting order_items search results."""
    asin: AirbyteSortOrder
    """Amazon Standard Identification Number of the product"""
    amazon_order_id: AirbyteSortOrder
    """ID of the Amazon order"""
    buyer_info: AirbyteSortOrder
    """Information about the buyer"""
    buyer_requested_cancel: AirbyteSortOrder
    """Information about buyer's request for cancellation"""
    cod_fee: AirbyteSortOrder
    """Cash on delivery fee"""
    cod_fee_discount: AirbyteSortOrder
    """Discount on cash on delivery fee"""
    condition_id: AirbyteSortOrder
    """Condition ID of the product"""
    condition_note: AirbyteSortOrder
    """Additional notes on the condition of the product"""
    condition_subtype_id: AirbyteSortOrder
    """Subtype ID of the product condition"""
    deemed_reseller_category: AirbyteSortOrder
    """Category indicating if the seller is considered a reseller"""
    ioss_number: AirbyteSortOrder
    """Import One Stop Shop number"""
    is_gift: AirbyteSortOrder
    """Flag indicating if the order is a gift"""
    is_transparency: AirbyteSortOrder
    """Flag indicating if transparency is applied"""
    item_price: AirbyteSortOrder
    """Price of the item"""
    item_tax: AirbyteSortOrder
    """Tax applied on the item"""
    last_update_date: AirbyteSortOrder
    """Date and time of the last update"""
    order_item_id: AirbyteSortOrder
    """ID of the order item"""
    points_granted: AirbyteSortOrder
    """Points granted for the purchase"""
    price_designation: AirbyteSortOrder
    """Designation of the price"""
    product_info: AirbyteSortOrder
    """Information about the product"""
    promotion_discount: AirbyteSortOrder
    """Discount applied due to promotion"""
    promotion_discount_tax: AirbyteSortOrder
    """Tax applied on the promotion discount"""
    promotion_ids: AirbyteSortOrder
    """IDs of promotions applied"""
    quantity_ordered: AirbyteSortOrder
    """Quantity of the item ordered"""
    quantity_shipped: AirbyteSortOrder
    """Quantity of the item shipped"""
    scheduled_delivery_end_date: AirbyteSortOrder
    """End date for scheduled delivery"""
    scheduled_delivery_start_date: AirbyteSortOrder
    """Start date for scheduled delivery"""
    seller_sku: AirbyteSortOrder
    """SKU of the seller"""
    serial_number_required: AirbyteSortOrder
    """Flag indicating if serial number is required"""
    serial_numbers: AirbyteSortOrder
    """List of serial numbers"""
    shipping_discount: AirbyteSortOrder
    """Discount applied on shipping"""
    shipping_discount_tax: AirbyteSortOrder
    """Tax applied on the shipping discount"""
    shipping_price: AirbyteSortOrder
    """Price of shipping"""
    shipping_tax: AirbyteSortOrder
    """Tax applied on shipping"""
    store_chain_store_id: AirbyteSortOrder
    """ID of the store chain"""
    tax_collection: AirbyteSortOrder
    """Information about tax collection"""
    title: AirbyteSortOrder
    """Title of the product"""


# Entity-specific condition types for order_items
class OrderItemsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OrderItemsSearchFilter


class OrderItemsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OrderItemsSearchFilter


class OrderItemsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OrderItemsSearchFilter


class OrderItemsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OrderItemsSearchFilter


class OrderItemsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OrderItemsSearchFilter


class OrderItemsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OrderItemsSearchFilter


class OrderItemsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OrderItemsStringFilter


class OrderItemsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OrderItemsStringFilter


class OrderItemsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OrderItemsStringFilter


class OrderItemsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OrderItemsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OrderItemsInCondition = TypedDict("OrderItemsInCondition", {"in": OrderItemsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OrderItemsNotCondition = TypedDict("OrderItemsNotCondition", {"not": "OrderItemsCondition"}, total=False)
"""Negates the nested condition."""

OrderItemsAndCondition = TypedDict("OrderItemsAndCondition", {"and": "list[OrderItemsCondition]"}, total=False)
"""True if all nested conditions are true."""

OrderItemsOrCondition = TypedDict("OrderItemsOrCondition", {"or": "list[OrderItemsCondition]"}, total=False)
"""True if any nested condition is true."""

OrderItemsAnyCondition = TypedDict("OrderItemsAnyCondition", {"any": OrderItemsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all order_items condition types
OrderItemsCondition = (
    OrderItemsEqCondition
    | OrderItemsNeqCondition
    | OrderItemsGtCondition
    | OrderItemsGteCondition
    | OrderItemsLtCondition
    | OrderItemsLteCondition
    | OrderItemsInCondition
    | OrderItemsLikeCondition
    | OrderItemsFuzzyCondition
    | OrderItemsKeywordCondition
    | OrderItemsContainsCondition
    | OrderItemsNotCondition
    | OrderItemsAndCondition
    | OrderItemsOrCondition
    | OrderItemsAnyCondition
)


class OrderItemsSearchQuery(TypedDict, total=False):
    """Search query for order_items entity."""
    filter: OrderItemsCondition
    sort: list[OrderItemsSortFilter]


# ===== LIST_FINANCIAL_EVENT_GROUPS SEARCH TYPES =====

class ListFinancialEventGroupsSearchFilter(TypedDict, total=False):
    """Available fields for filtering list_financial_event_groups search queries."""
    account_tail: str | None
    """The last digits of the account number"""
    beginning_balance: dict[str, Any] | None
    """Beginning balance"""
    converted_total: dict[str, Any] | None
    """Converted total"""
    financial_event_group_end: str | None
    """End datetime of the financial event group"""
    financial_event_group_id: str | None
    """Unique identifier for the financial event group"""
    financial_event_group_start: str | None
    """Start datetime of the financial event group"""
    fund_transfer_date: str | None
    """Date the fund transfer occurred"""
    fund_transfer_status: str | None
    """Status of the fund transfer"""
    original_total: dict[str, Any] | None
    """Original total amount"""
    processing_status: str | None
    """Processing status of the financial event group"""
    trace_id: str | None
    """Unique identifier for tracing"""


class ListFinancialEventGroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account_tail: list[str]
    """The last digits of the account number"""
    beginning_balance: list[dict[str, Any]]
    """Beginning balance"""
    converted_total: list[dict[str, Any]]
    """Converted total"""
    financial_event_group_end: list[str]
    """End datetime of the financial event group"""
    financial_event_group_id: list[str]
    """Unique identifier for the financial event group"""
    financial_event_group_start: list[str]
    """Start datetime of the financial event group"""
    fund_transfer_date: list[str]
    """Date the fund transfer occurred"""
    fund_transfer_status: list[str]
    """Status of the fund transfer"""
    original_total: list[dict[str, Any]]
    """Original total amount"""
    processing_status: list[str]
    """Processing status of the financial event group"""
    trace_id: list[str]
    """Unique identifier for tracing"""


class ListFinancialEventGroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account_tail: Any
    """The last digits of the account number"""
    beginning_balance: Any
    """Beginning balance"""
    converted_total: Any
    """Converted total"""
    financial_event_group_end: Any
    """End datetime of the financial event group"""
    financial_event_group_id: Any
    """Unique identifier for the financial event group"""
    financial_event_group_start: Any
    """Start datetime of the financial event group"""
    fund_transfer_date: Any
    """Date the fund transfer occurred"""
    fund_transfer_status: Any
    """Status of the fund transfer"""
    original_total: Any
    """Original total amount"""
    processing_status: Any
    """Processing status of the financial event group"""
    trace_id: Any
    """Unique identifier for tracing"""


class ListFinancialEventGroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    account_tail: str
    """The last digits of the account number"""
    beginning_balance: str
    """Beginning balance"""
    converted_total: str
    """Converted total"""
    financial_event_group_end: str
    """End datetime of the financial event group"""
    financial_event_group_id: str
    """Unique identifier for the financial event group"""
    financial_event_group_start: str
    """Start datetime of the financial event group"""
    fund_transfer_date: str
    """Date the fund transfer occurred"""
    fund_transfer_status: str
    """Status of the fund transfer"""
    original_total: str
    """Original total amount"""
    processing_status: str
    """Processing status of the financial event group"""
    trace_id: str
    """Unique identifier for tracing"""


class ListFinancialEventGroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting list_financial_event_groups search results."""
    account_tail: AirbyteSortOrder
    """The last digits of the account number"""
    beginning_balance: AirbyteSortOrder
    """Beginning balance"""
    converted_total: AirbyteSortOrder
    """Converted total"""
    financial_event_group_end: AirbyteSortOrder
    """End datetime of the financial event group"""
    financial_event_group_id: AirbyteSortOrder
    """Unique identifier for the financial event group"""
    financial_event_group_start: AirbyteSortOrder
    """Start datetime of the financial event group"""
    fund_transfer_date: AirbyteSortOrder
    """Date the fund transfer occurred"""
    fund_transfer_status: AirbyteSortOrder
    """Status of the fund transfer"""
    original_total: AirbyteSortOrder
    """Original total amount"""
    processing_status: AirbyteSortOrder
    """Processing status of the financial event group"""
    trace_id: AirbyteSortOrder
    """Unique identifier for tracing"""


# Entity-specific condition types for list_financial_event_groups
class ListFinancialEventGroupsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ListFinancialEventGroupsSearchFilter


class ListFinancialEventGroupsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ListFinancialEventGroupsSearchFilter


class ListFinancialEventGroupsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ListFinancialEventGroupsSearchFilter


class ListFinancialEventGroupsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ListFinancialEventGroupsSearchFilter


class ListFinancialEventGroupsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ListFinancialEventGroupsSearchFilter


class ListFinancialEventGroupsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ListFinancialEventGroupsSearchFilter


class ListFinancialEventGroupsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ListFinancialEventGroupsStringFilter


class ListFinancialEventGroupsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ListFinancialEventGroupsStringFilter


class ListFinancialEventGroupsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ListFinancialEventGroupsStringFilter


class ListFinancialEventGroupsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ListFinancialEventGroupsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ListFinancialEventGroupsInCondition = TypedDict("ListFinancialEventGroupsInCondition", {"in": ListFinancialEventGroupsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ListFinancialEventGroupsNotCondition = TypedDict("ListFinancialEventGroupsNotCondition", {"not": "ListFinancialEventGroupsCondition"}, total=False)
"""Negates the nested condition."""

ListFinancialEventGroupsAndCondition = TypedDict("ListFinancialEventGroupsAndCondition", {"and": "list[ListFinancialEventGroupsCondition]"}, total=False)
"""True if all nested conditions are true."""

ListFinancialEventGroupsOrCondition = TypedDict("ListFinancialEventGroupsOrCondition", {"or": "list[ListFinancialEventGroupsCondition]"}, total=False)
"""True if any nested condition is true."""

ListFinancialEventGroupsAnyCondition = TypedDict("ListFinancialEventGroupsAnyCondition", {"any": ListFinancialEventGroupsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all list_financial_event_groups condition types
ListFinancialEventGroupsCondition = (
    ListFinancialEventGroupsEqCondition
    | ListFinancialEventGroupsNeqCondition
    | ListFinancialEventGroupsGtCondition
    | ListFinancialEventGroupsGteCondition
    | ListFinancialEventGroupsLtCondition
    | ListFinancialEventGroupsLteCondition
    | ListFinancialEventGroupsInCondition
    | ListFinancialEventGroupsLikeCondition
    | ListFinancialEventGroupsFuzzyCondition
    | ListFinancialEventGroupsKeywordCondition
    | ListFinancialEventGroupsContainsCondition
    | ListFinancialEventGroupsNotCondition
    | ListFinancialEventGroupsAndCondition
    | ListFinancialEventGroupsOrCondition
    | ListFinancialEventGroupsAnyCondition
)


class ListFinancialEventGroupsSearchQuery(TypedDict, total=False):
    """Search query for list_financial_event_groups entity."""
    filter: ListFinancialEventGroupsCondition
    sort: list[ListFinancialEventGroupsSortFilter]


# ===== LIST_FINANCIAL_EVENTS SEARCH TYPES =====

class ListFinancialEventsSearchFilter(TypedDict, total=False):
    """Available fields for filtering list_financial_events search queries."""
    adhoc_disbursement_event_list: list[Any] | None
    """List of adhoc disbursement events"""
    adjustment_event_list: list[Any] | None
    """List of adjustment events"""
    affordability_expense_event_list: list[Any] | None
    """List of affordability expense events"""
    affordability_expense_reversal_event_list: list[Any] | None
    """List of affordability expense reversal events"""
    capacity_reservation_billing_event_list: list[Any] | None
    """List of capacity reservation billing events"""
    charge_refund_event_list: list[Any] | None
    """List of charge refund events"""
    chargeback_event_list: list[Any] | None
    """List of chargeback events"""
    coupon_payment_event_list: list[Any] | None
    """List of coupon payment events"""
    debt_recovery_event_list: list[Any] | None
    """List of debt recovery events"""
    fba_liquidation_event_list: list[Any] | None
    """List of FBA liquidation events"""
    failed_adhoc_disbursement_event_list: list[Any] | None
    """List of failed adhoc disbursement events"""
    guarantee_claim_event_list: list[Any] | None
    """List of guarantee claim events"""
    imaging_services_fee_event_list: list[Any] | None
    """List of imaging services fee events"""
    loan_servicing_event_list: list[Any] | None
    """List of loan servicing events"""
    network_commingling_transaction_event_list: list[Any] | None
    """List of network commingling events"""
    pay_with_amazon_event_list: list[Any] | None
    """List of Pay with Amazon events"""
    performance_bond_refund_event_list: list[Any] | None
    """List of performance bond refund events"""
    posted_before: str | None
    """Date filter for events posted before"""
    product_ads_payment_event_list: list[Any] | None
    """List of product ads payment events"""
    refund_event_list: list[Any] | None
    """List of refund events"""
    removal_shipment_adjustment_event_list: list[Any] | None
    """List of removal shipment adjustment events"""
    removal_shipment_event_list: list[Any] | None
    """List of removal shipment events"""
    rental_transaction_event_list: list[Any] | None
    """List of rental transaction events"""
    retrocharge_event_list: list[Any] | None
    """List of retrocharge events"""
    safet_reimbursement_event_list: list[Any] | None
    """List of SAFET reimbursement events"""
    seller_deal_payment_event_list: list[Any] | None
    """List of seller deal payment events"""
    seller_review_enrollment_payment_event_list: list[Any] | None
    """List of seller review enrollment events"""
    service_fee_event_list: list[Any] | None
    """List of service fee events"""
    service_provider_credit_event_list: list[Any] | None
    """List of service provider credit events"""
    shipment_event_list: list[Any] | None
    """List of shipment events"""
    shipment_settle_event_list: list[Any] | None
    """List of shipment settlement events"""
    tds_reimbursement_event_list: list[Any] | None
    """List of TDS reimbursement events"""
    tax_withholding_event_list: list[Any] | None
    """List of tax withholding events"""
    trial_shipment_event_list: list[Any] | None
    """List of trial shipment events"""
    value_added_service_charge_event_list: list[Any] | None
    """List of value-added service charge events"""


class ListFinancialEventsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    adhoc_disbursement_event_list: list[list[Any]]
    """List of adhoc disbursement events"""
    adjustment_event_list: list[list[Any]]
    """List of adjustment events"""
    affordability_expense_event_list: list[list[Any]]
    """List of affordability expense events"""
    affordability_expense_reversal_event_list: list[list[Any]]
    """List of affordability expense reversal events"""
    capacity_reservation_billing_event_list: list[list[Any]]
    """List of capacity reservation billing events"""
    charge_refund_event_list: list[list[Any]]
    """List of charge refund events"""
    chargeback_event_list: list[list[Any]]
    """List of chargeback events"""
    coupon_payment_event_list: list[list[Any]]
    """List of coupon payment events"""
    debt_recovery_event_list: list[list[Any]]
    """List of debt recovery events"""
    fba_liquidation_event_list: list[list[Any]]
    """List of FBA liquidation events"""
    failed_adhoc_disbursement_event_list: list[list[Any]]
    """List of failed adhoc disbursement events"""
    guarantee_claim_event_list: list[list[Any]]
    """List of guarantee claim events"""
    imaging_services_fee_event_list: list[list[Any]]
    """List of imaging services fee events"""
    loan_servicing_event_list: list[list[Any]]
    """List of loan servicing events"""
    network_commingling_transaction_event_list: list[list[Any]]
    """List of network commingling events"""
    pay_with_amazon_event_list: list[list[Any]]
    """List of Pay with Amazon events"""
    performance_bond_refund_event_list: list[list[Any]]
    """List of performance bond refund events"""
    posted_before: list[str]
    """Date filter for events posted before"""
    product_ads_payment_event_list: list[list[Any]]
    """List of product ads payment events"""
    refund_event_list: list[list[Any]]
    """List of refund events"""
    removal_shipment_adjustment_event_list: list[list[Any]]
    """List of removal shipment adjustment events"""
    removal_shipment_event_list: list[list[Any]]
    """List of removal shipment events"""
    rental_transaction_event_list: list[list[Any]]
    """List of rental transaction events"""
    retrocharge_event_list: list[list[Any]]
    """List of retrocharge events"""
    safet_reimbursement_event_list: list[list[Any]]
    """List of SAFET reimbursement events"""
    seller_deal_payment_event_list: list[list[Any]]
    """List of seller deal payment events"""
    seller_review_enrollment_payment_event_list: list[list[Any]]
    """List of seller review enrollment events"""
    service_fee_event_list: list[list[Any]]
    """List of service fee events"""
    service_provider_credit_event_list: list[list[Any]]
    """List of service provider credit events"""
    shipment_event_list: list[list[Any]]
    """List of shipment events"""
    shipment_settle_event_list: list[list[Any]]
    """List of shipment settlement events"""
    tds_reimbursement_event_list: list[list[Any]]
    """List of TDS reimbursement events"""
    tax_withholding_event_list: list[list[Any]]
    """List of tax withholding events"""
    trial_shipment_event_list: list[list[Any]]
    """List of trial shipment events"""
    value_added_service_charge_event_list: list[list[Any]]
    """List of value-added service charge events"""


class ListFinancialEventsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    adhoc_disbursement_event_list: Any
    """List of adhoc disbursement events"""
    adjustment_event_list: Any
    """List of adjustment events"""
    affordability_expense_event_list: Any
    """List of affordability expense events"""
    affordability_expense_reversal_event_list: Any
    """List of affordability expense reversal events"""
    capacity_reservation_billing_event_list: Any
    """List of capacity reservation billing events"""
    charge_refund_event_list: Any
    """List of charge refund events"""
    chargeback_event_list: Any
    """List of chargeback events"""
    coupon_payment_event_list: Any
    """List of coupon payment events"""
    debt_recovery_event_list: Any
    """List of debt recovery events"""
    fba_liquidation_event_list: Any
    """List of FBA liquidation events"""
    failed_adhoc_disbursement_event_list: Any
    """List of failed adhoc disbursement events"""
    guarantee_claim_event_list: Any
    """List of guarantee claim events"""
    imaging_services_fee_event_list: Any
    """List of imaging services fee events"""
    loan_servicing_event_list: Any
    """List of loan servicing events"""
    network_commingling_transaction_event_list: Any
    """List of network commingling events"""
    pay_with_amazon_event_list: Any
    """List of Pay with Amazon events"""
    performance_bond_refund_event_list: Any
    """List of performance bond refund events"""
    posted_before: Any
    """Date filter for events posted before"""
    product_ads_payment_event_list: Any
    """List of product ads payment events"""
    refund_event_list: Any
    """List of refund events"""
    removal_shipment_adjustment_event_list: Any
    """List of removal shipment adjustment events"""
    removal_shipment_event_list: Any
    """List of removal shipment events"""
    rental_transaction_event_list: Any
    """List of rental transaction events"""
    retrocharge_event_list: Any
    """List of retrocharge events"""
    safet_reimbursement_event_list: Any
    """List of SAFET reimbursement events"""
    seller_deal_payment_event_list: Any
    """List of seller deal payment events"""
    seller_review_enrollment_payment_event_list: Any
    """List of seller review enrollment events"""
    service_fee_event_list: Any
    """List of service fee events"""
    service_provider_credit_event_list: Any
    """List of service provider credit events"""
    shipment_event_list: Any
    """List of shipment events"""
    shipment_settle_event_list: Any
    """List of shipment settlement events"""
    tds_reimbursement_event_list: Any
    """List of TDS reimbursement events"""
    tax_withholding_event_list: Any
    """List of tax withholding events"""
    trial_shipment_event_list: Any
    """List of trial shipment events"""
    value_added_service_charge_event_list: Any
    """List of value-added service charge events"""


class ListFinancialEventsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    adhoc_disbursement_event_list: str
    """List of adhoc disbursement events"""
    adjustment_event_list: str
    """List of adjustment events"""
    affordability_expense_event_list: str
    """List of affordability expense events"""
    affordability_expense_reversal_event_list: str
    """List of affordability expense reversal events"""
    capacity_reservation_billing_event_list: str
    """List of capacity reservation billing events"""
    charge_refund_event_list: str
    """List of charge refund events"""
    chargeback_event_list: str
    """List of chargeback events"""
    coupon_payment_event_list: str
    """List of coupon payment events"""
    debt_recovery_event_list: str
    """List of debt recovery events"""
    fba_liquidation_event_list: str
    """List of FBA liquidation events"""
    failed_adhoc_disbursement_event_list: str
    """List of failed adhoc disbursement events"""
    guarantee_claim_event_list: str
    """List of guarantee claim events"""
    imaging_services_fee_event_list: str
    """List of imaging services fee events"""
    loan_servicing_event_list: str
    """List of loan servicing events"""
    network_commingling_transaction_event_list: str
    """List of network commingling events"""
    pay_with_amazon_event_list: str
    """List of Pay with Amazon events"""
    performance_bond_refund_event_list: str
    """List of performance bond refund events"""
    posted_before: str
    """Date filter for events posted before"""
    product_ads_payment_event_list: str
    """List of product ads payment events"""
    refund_event_list: str
    """List of refund events"""
    removal_shipment_adjustment_event_list: str
    """List of removal shipment adjustment events"""
    removal_shipment_event_list: str
    """List of removal shipment events"""
    rental_transaction_event_list: str
    """List of rental transaction events"""
    retrocharge_event_list: str
    """List of retrocharge events"""
    safet_reimbursement_event_list: str
    """List of SAFET reimbursement events"""
    seller_deal_payment_event_list: str
    """List of seller deal payment events"""
    seller_review_enrollment_payment_event_list: str
    """List of seller review enrollment events"""
    service_fee_event_list: str
    """List of service fee events"""
    service_provider_credit_event_list: str
    """List of service provider credit events"""
    shipment_event_list: str
    """List of shipment events"""
    shipment_settle_event_list: str
    """List of shipment settlement events"""
    tds_reimbursement_event_list: str
    """List of TDS reimbursement events"""
    tax_withholding_event_list: str
    """List of tax withholding events"""
    trial_shipment_event_list: str
    """List of trial shipment events"""
    value_added_service_charge_event_list: str
    """List of value-added service charge events"""


class ListFinancialEventsSortFilter(TypedDict, total=False):
    """Available fields for sorting list_financial_events search results."""
    adhoc_disbursement_event_list: AirbyteSortOrder
    """List of adhoc disbursement events"""
    adjustment_event_list: AirbyteSortOrder
    """List of adjustment events"""
    affordability_expense_event_list: AirbyteSortOrder
    """List of affordability expense events"""
    affordability_expense_reversal_event_list: AirbyteSortOrder
    """List of affordability expense reversal events"""
    capacity_reservation_billing_event_list: AirbyteSortOrder
    """List of capacity reservation billing events"""
    charge_refund_event_list: AirbyteSortOrder
    """List of charge refund events"""
    chargeback_event_list: AirbyteSortOrder
    """List of chargeback events"""
    coupon_payment_event_list: AirbyteSortOrder
    """List of coupon payment events"""
    debt_recovery_event_list: AirbyteSortOrder
    """List of debt recovery events"""
    fba_liquidation_event_list: AirbyteSortOrder
    """List of FBA liquidation events"""
    failed_adhoc_disbursement_event_list: AirbyteSortOrder
    """List of failed adhoc disbursement events"""
    guarantee_claim_event_list: AirbyteSortOrder
    """List of guarantee claim events"""
    imaging_services_fee_event_list: AirbyteSortOrder
    """List of imaging services fee events"""
    loan_servicing_event_list: AirbyteSortOrder
    """List of loan servicing events"""
    network_commingling_transaction_event_list: AirbyteSortOrder
    """List of network commingling events"""
    pay_with_amazon_event_list: AirbyteSortOrder
    """List of Pay with Amazon events"""
    performance_bond_refund_event_list: AirbyteSortOrder
    """List of performance bond refund events"""
    posted_before: AirbyteSortOrder
    """Date filter for events posted before"""
    product_ads_payment_event_list: AirbyteSortOrder
    """List of product ads payment events"""
    refund_event_list: AirbyteSortOrder
    """List of refund events"""
    removal_shipment_adjustment_event_list: AirbyteSortOrder
    """List of removal shipment adjustment events"""
    removal_shipment_event_list: AirbyteSortOrder
    """List of removal shipment events"""
    rental_transaction_event_list: AirbyteSortOrder
    """List of rental transaction events"""
    retrocharge_event_list: AirbyteSortOrder
    """List of retrocharge events"""
    safet_reimbursement_event_list: AirbyteSortOrder
    """List of SAFET reimbursement events"""
    seller_deal_payment_event_list: AirbyteSortOrder
    """List of seller deal payment events"""
    seller_review_enrollment_payment_event_list: AirbyteSortOrder
    """List of seller review enrollment events"""
    service_fee_event_list: AirbyteSortOrder
    """List of service fee events"""
    service_provider_credit_event_list: AirbyteSortOrder
    """List of service provider credit events"""
    shipment_event_list: AirbyteSortOrder
    """List of shipment events"""
    shipment_settle_event_list: AirbyteSortOrder
    """List of shipment settlement events"""
    tds_reimbursement_event_list: AirbyteSortOrder
    """List of TDS reimbursement events"""
    tax_withholding_event_list: AirbyteSortOrder
    """List of tax withholding events"""
    trial_shipment_event_list: AirbyteSortOrder
    """List of trial shipment events"""
    value_added_service_charge_event_list: AirbyteSortOrder
    """List of value-added service charge events"""


# Entity-specific condition types for list_financial_events
class ListFinancialEventsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ListFinancialEventsSearchFilter


class ListFinancialEventsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ListFinancialEventsSearchFilter


class ListFinancialEventsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ListFinancialEventsSearchFilter


class ListFinancialEventsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ListFinancialEventsSearchFilter


class ListFinancialEventsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ListFinancialEventsSearchFilter


class ListFinancialEventsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ListFinancialEventsSearchFilter


class ListFinancialEventsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ListFinancialEventsStringFilter


class ListFinancialEventsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ListFinancialEventsStringFilter


class ListFinancialEventsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ListFinancialEventsStringFilter


class ListFinancialEventsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ListFinancialEventsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ListFinancialEventsInCondition = TypedDict("ListFinancialEventsInCondition", {"in": ListFinancialEventsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ListFinancialEventsNotCondition = TypedDict("ListFinancialEventsNotCondition", {"not": "ListFinancialEventsCondition"}, total=False)
"""Negates the nested condition."""

ListFinancialEventsAndCondition = TypedDict("ListFinancialEventsAndCondition", {"and": "list[ListFinancialEventsCondition]"}, total=False)
"""True if all nested conditions are true."""

ListFinancialEventsOrCondition = TypedDict("ListFinancialEventsOrCondition", {"or": "list[ListFinancialEventsCondition]"}, total=False)
"""True if any nested condition is true."""

ListFinancialEventsAnyCondition = TypedDict("ListFinancialEventsAnyCondition", {"any": ListFinancialEventsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all list_financial_events condition types
ListFinancialEventsCondition = (
    ListFinancialEventsEqCondition
    | ListFinancialEventsNeqCondition
    | ListFinancialEventsGtCondition
    | ListFinancialEventsGteCondition
    | ListFinancialEventsLtCondition
    | ListFinancialEventsLteCondition
    | ListFinancialEventsInCondition
    | ListFinancialEventsLikeCondition
    | ListFinancialEventsFuzzyCondition
    | ListFinancialEventsKeywordCondition
    | ListFinancialEventsContainsCondition
    | ListFinancialEventsNotCondition
    | ListFinancialEventsAndCondition
    | ListFinancialEventsOrCondition
    | ListFinancialEventsAnyCondition
)


class ListFinancialEventsSearchQuery(TypedDict, total=False):
    """Search query for list_financial_events entity."""
    filter: ListFinancialEventsCondition
    sort: list[ListFinancialEventsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
