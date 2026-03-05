"""
Type definitions for woocommerce connector.
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

class CustomersListParams(TypedDict):
    """Parameters for customers.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    search: NotRequired[str]
    orderby: NotRequired[str]
    order: NotRequired[str]
    email: NotRequired[str]
    role: NotRequired[str]

class CustomersGetParams(TypedDict):
    """Parameters for customers.get operation"""
    id: str

class OrdersListParams(TypedDict):
    """Parameters for orders.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    search: NotRequired[str]
    after: NotRequired[str]
    before: NotRequired[str]
    modified_after: NotRequired[str]
    modified_before: NotRequired[str]
    status: NotRequired[str]
    customer: NotRequired[int]
    product: NotRequired[int]
    orderby: NotRequired[str]
    order: NotRequired[str]

class OrdersGetParams(TypedDict):
    """Parameters for orders.get operation"""
    id: str

class ProductsListParams(TypedDict):
    """Parameters for products.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    search: NotRequired[str]
    after: NotRequired[str]
    before: NotRequired[str]
    modified_after: NotRequired[str]
    modified_before: NotRequired[str]
    status: NotRequired[str]
    type: NotRequired[str]
    sku: NotRequired[str]
    featured: NotRequired[bool]
    category: NotRequired[str]
    tag: NotRequired[str]
    on_sale: NotRequired[bool]
    min_price: NotRequired[str]
    max_price: NotRequired[str]
    stock_status: NotRequired[str]
    orderby: NotRequired[str]
    order: NotRequired[str]

class ProductsGetParams(TypedDict):
    """Parameters for products.get operation"""
    id: str

class CouponsListParams(TypedDict):
    """Parameters for coupons.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    search: NotRequired[str]
    after: NotRequired[str]
    before: NotRequired[str]
    modified_after: NotRequired[str]
    modified_before: NotRequired[str]
    code: NotRequired[str]
    orderby: NotRequired[str]
    order: NotRequired[str]

class CouponsGetParams(TypedDict):
    """Parameters for coupons.get operation"""
    id: str

class ProductCategoriesListParams(TypedDict):
    """Parameters for product_categories.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    search: NotRequired[str]
    orderby: NotRequired[str]
    order: NotRequired[str]
    hide_empty: NotRequired[bool]
    parent: NotRequired[int]
    product: NotRequired[int]
    slug: NotRequired[str]

class ProductCategoriesGetParams(TypedDict):
    """Parameters for product_categories.get operation"""
    id: str

class ProductTagsListParams(TypedDict):
    """Parameters for product_tags.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    search: NotRequired[str]
    orderby: NotRequired[str]
    order: NotRequired[str]
    hide_empty: NotRequired[bool]
    product: NotRequired[int]
    slug: NotRequired[str]

class ProductTagsGetParams(TypedDict):
    """Parameters for product_tags.get operation"""
    id: str

class ProductReviewsListParams(TypedDict):
    """Parameters for product_reviews.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    search: NotRequired[str]
    after: NotRequired[str]
    before: NotRequired[str]
    product: NotRequired[list[int]]
    status: NotRequired[str]

class ProductReviewsGetParams(TypedDict):
    """Parameters for product_reviews.get operation"""
    id: str

class ProductAttributesListParams(TypedDict):
    """Parameters for product_attributes.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]

class ProductAttributesGetParams(TypedDict):
    """Parameters for product_attributes.get operation"""
    id: str

class ProductVariationsListParams(TypedDict):
    """Parameters for product_variations.list operation"""
    product_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]
    search: NotRequired[str]
    sku: NotRequired[str]
    status: NotRequired[str]
    stock_status: NotRequired[str]
    on_sale: NotRequired[bool]
    min_price: NotRequired[str]
    max_price: NotRequired[str]
    orderby: NotRequired[str]
    order: NotRequired[str]

class ProductVariationsGetParams(TypedDict):
    """Parameters for product_variations.get operation"""
    product_id: str
    id: str

class OrderNotesListParams(TypedDict):
    """Parameters for order_notes.list operation"""
    order_id: str
    type: NotRequired[str]

class OrderNotesGetParams(TypedDict):
    """Parameters for order_notes.get operation"""
    order_id: str
    id: str

class RefundsListParams(TypedDict):
    """Parameters for refunds.list operation"""
    order_id: str
    page: NotRequired[int]
    per_page: NotRequired[int]

class RefundsGetParams(TypedDict):
    """Parameters for refunds.get operation"""
    order_id: str
    id: str

class PaymentGatewaysListParams(TypedDict):
    """Parameters for payment_gateways.list operation"""
    pass

class PaymentGatewaysGetParams(TypedDict):
    """Parameters for payment_gateways.get operation"""
    id: str

class ShippingMethodsListParams(TypedDict):
    """Parameters for shipping_methods.list operation"""
    pass

class ShippingMethodsGetParams(TypedDict):
    """Parameters for shipping_methods.get operation"""
    id: str

class ShippingZonesListParams(TypedDict):
    """Parameters for shipping_zones.list operation"""
    pass

class ShippingZonesGetParams(TypedDict):
    """Parameters for shipping_zones.get operation"""
    id: str

class TaxRatesListParams(TypedDict):
    """Parameters for tax_rates.list operation"""
    page: NotRequired[int]
    per_page: NotRequired[int]
    class_: NotRequired[str]
    orderby: NotRequired[str]
    order: NotRequired[str]

class TaxRatesGetParams(TypedDict):
    """Parameters for tax_rates.get operation"""
    id: str

class TaxClassesListParams(TypedDict):
    """Parameters for tax_classes.list operation"""
    pass

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== CUSTOMERS SEARCH TYPES =====

class CustomersSearchFilter(TypedDict, total=False):
    """Available fields for filtering customers search queries."""
    avatar_url: str | None
    """Avatar URL"""
    billing: dict[str, Any] | None
    """List of billing address data"""
    date_created: str | None
    """The date the customer was created, in the site's timezone"""
    date_created_gmt: str | None
    """The date the customer was created, as GMT"""
    date_modified: str | None
    """The date the customer was last modified, in the site's timezone"""
    date_modified_gmt: str | None
    """The date the customer was last modified, as GMT"""
    email: str | None
    """The email address for the customer"""
    first_name: str | None
    """Customer first name"""
    id: int | None
    """Unique identifier for the resource"""
    is_paying_customer: bool | None
    """Is the customer a paying customer"""
    last_name: str | None
    """Customer last name"""
    meta_data: list[Any] | None
    """Meta data"""
    role: str | None
    """Customer role"""
    shipping: dict[str, Any] | None
    """List of shipping address data"""
    username: str | None
    """Customer login name"""


class CustomersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    avatar_url: list[str]
    """Avatar URL"""
    billing: list[dict[str, Any]]
    """List of billing address data"""
    date_created: list[str]
    """The date the customer was created, in the site's timezone"""
    date_created_gmt: list[str]
    """The date the customer was created, as GMT"""
    date_modified: list[str]
    """The date the customer was last modified, in the site's timezone"""
    date_modified_gmt: list[str]
    """The date the customer was last modified, as GMT"""
    email: list[str]
    """The email address for the customer"""
    first_name: list[str]
    """Customer first name"""
    id: list[int]
    """Unique identifier for the resource"""
    is_paying_customer: list[bool]
    """Is the customer a paying customer"""
    last_name: list[str]
    """Customer last name"""
    meta_data: list[list[Any]]
    """Meta data"""
    role: list[str]
    """Customer role"""
    shipping: list[dict[str, Any]]
    """List of shipping address data"""
    username: list[str]
    """Customer login name"""


class CustomersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    avatar_url: Any
    """Avatar URL"""
    billing: Any
    """List of billing address data"""
    date_created: Any
    """The date the customer was created, in the site's timezone"""
    date_created_gmt: Any
    """The date the customer was created, as GMT"""
    date_modified: Any
    """The date the customer was last modified, in the site's timezone"""
    date_modified_gmt: Any
    """The date the customer was last modified, as GMT"""
    email: Any
    """The email address for the customer"""
    first_name: Any
    """Customer first name"""
    id: Any
    """Unique identifier for the resource"""
    is_paying_customer: Any
    """Is the customer a paying customer"""
    last_name: Any
    """Customer last name"""
    meta_data: Any
    """Meta data"""
    role: Any
    """Customer role"""
    shipping: Any
    """List of shipping address data"""
    username: Any
    """Customer login name"""


class CustomersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    avatar_url: str
    """Avatar URL"""
    billing: str
    """List of billing address data"""
    date_created: str
    """The date the customer was created, in the site's timezone"""
    date_created_gmt: str
    """The date the customer was created, as GMT"""
    date_modified: str
    """The date the customer was last modified, in the site's timezone"""
    date_modified_gmt: str
    """The date the customer was last modified, as GMT"""
    email: str
    """The email address for the customer"""
    first_name: str
    """Customer first name"""
    id: str
    """Unique identifier for the resource"""
    is_paying_customer: str
    """Is the customer a paying customer"""
    last_name: str
    """Customer last name"""
    meta_data: str
    """Meta data"""
    role: str
    """Customer role"""
    shipping: str
    """List of shipping address data"""
    username: str
    """Customer login name"""


class CustomersSortFilter(TypedDict, total=False):
    """Available fields for sorting customers search results."""
    avatar_url: AirbyteSortOrder
    """Avatar URL"""
    billing: AirbyteSortOrder
    """List of billing address data"""
    date_created: AirbyteSortOrder
    """The date the customer was created, in the site's timezone"""
    date_created_gmt: AirbyteSortOrder
    """The date the customer was created, as GMT"""
    date_modified: AirbyteSortOrder
    """The date the customer was last modified, in the site's timezone"""
    date_modified_gmt: AirbyteSortOrder
    """The date the customer was last modified, as GMT"""
    email: AirbyteSortOrder
    """The email address for the customer"""
    first_name: AirbyteSortOrder
    """Customer first name"""
    id: AirbyteSortOrder
    """Unique identifier for the resource"""
    is_paying_customer: AirbyteSortOrder
    """Is the customer a paying customer"""
    last_name: AirbyteSortOrder
    """Customer last name"""
    meta_data: AirbyteSortOrder
    """Meta data"""
    role: AirbyteSortOrder
    """Customer role"""
    shipping: AirbyteSortOrder
    """List of shipping address data"""
    username: AirbyteSortOrder
    """Customer login name"""


# Entity-specific condition types for customers
class CustomersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CustomersSearchFilter


class CustomersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CustomersSearchFilter


class CustomersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CustomersSearchFilter


class CustomersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CustomersSearchFilter


class CustomersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CustomersSearchFilter


class CustomersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CustomersSearchFilter


class CustomersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CustomersStringFilter


class CustomersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CustomersStringFilter


class CustomersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CustomersStringFilter


class CustomersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CustomersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CustomersInCondition = TypedDict("CustomersInCondition", {"in": CustomersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CustomersNotCondition = TypedDict("CustomersNotCondition", {"not": "CustomersCondition"}, total=False)
"""Negates the nested condition."""

CustomersAndCondition = TypedDict("CustomersAndCondition", {"and": "list[CustomersCondition]"}, total=False)
"""True if all nested conditions are true."""

CustomersOrCondition = TypedDict("CustomersOrCondition", {"or": "list[CustomersCondition]"}, total=False)
"""True if any nested condition is true."""

CustomersAnyCondition = TypedDict("CustomersAnyCondition", {"any": CustomersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all customers condition types
CustomersCondition = (
    CustomersEqCondition
    | CustomersNeqCondition
    | CustomersGtCondition
    | CustomersGteCondition
    | CustomersLtCondition
    | CustomersLteCondition
    | CustomersInCondition
    | CustomersLikeCondition
    | CustomersFuzzyCondition
    | CustomersKeywordCondition
    | CustomersContainsCondition
    | CustomersNotCondition
    | CustomersAndCondition
    | CustomersOrCondition
    | CustomersAnyCondition
)


class CustomersSearchQuery(TypedDict, total=False):
    """Search query for customers entity."""
    filter: CustomersCondition
    sort: list[CustomersSortFilter]


# ===== ORDERS SEARCH TYPES =====

class OrdersSearchFilter(TypedDict, total=False):
    """Available fields for filtering orders search queries."""
    billing: dict[str, Any] | None
    """Billing address"""
    cart_hash: str | None
    """MD5 hash of cart items to ensure orders are not modified"""
    cart_tax: str | None
    """Sum of line item taxes only"""
    coupon_lines: list[Any] | None
    """Coupons line data"""
    created_via: str | None
    """Shows where the order was created"""
    currency: str | None
    """Currency the order was created with, in ISO format"""
    customer_id: int | None
    """User ID who owns the order (0 for guests)"""
    customer_ip_address: str | None
    """Customer's IP address"""
    customer_note: str | None
    """Note left by the customer during checkout"""
    customer_user_agent: str | None
    """User agent of the customer"""
    date_completed: str | None
    """The date the order was completed, in the site's timezone"""
    date_completed_gmt: str | None
    """The date the order was completed, as GMT"""
    date_created: str | None
    """The date the order was created, in the site's timezone"""
    date_created_gmt: str | None
    """The date the order was created, as GMT"""
    date_modified: str | None
    """The date the order was last modified, in the site's timezone"""
    date_modified_gmt: str | None
    """The date the order was last modified, as GMT"""
    date_paid: str | None
    """The date the order was paid, in the site's timezone"""
    date_paid_gmt: str | None
    """The date the order was paid, as GMT"""
    discount_tax: str | None
    """Total discount tax amount for the order"""
    discount_total: str | None
    """Total discount amount for the order"""
    fee_lines: list[Any] | None
    """Fee lines data"""
    id: int | None
    """Unique identifier for the resource"""
    line_items: list[Any] | None
    """Line items data"""
    meta_data: list[Any] | None
    """Meta data"""
    number: str | None
    """Order number"""
    order_key: str | None
    """Order key"""
    parent_id: int | None
    """Parent order ID"""
    payment_method: str | None
    """Payment method ID"""
    payment_method_title: str | None
    """Payment method title"""
    prices_include_tax: bool | None
    """True if the prices included tax during checkout"""
    refunds: list[Any] | None
    """List of refunds"""
    shipping: dict[str, Any] | None
    """Shipping address"""
    shipping_lines: list[Any] | None
    """Shipping lines data"""
    shipping_tax: str | None
    """Total shipping tax amount for the order"""
    shipping_total: str | None
    """Total shipping amount for the order"""
    status: str | None
    """Order status"""
    tax_lines: list[Any] | None
    """Tax lines data"""
    total: str | None
    """Grand total"""
    total_tax: str | None
    """Sum of all taxes"""
    transaction_id: str | None
    """Unique transaction ID"""
    version: str | None
    """Version of WooCommerce which last updated the order"""


class OrdersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    billing: list[dict[str, Any]]
    """Billing address"""
    cart_hash: list[str]
    """MD5 hash of cart items to ensure orders are not modified"""
    cart_tax: list[str]
    """Sum of line item taxes only"""
    coupon_lines: list[list[Any]]
    """Coupons line data"""
    created_via: list[str]
    """Shows where the order was created"""
    currency: list[str]
    """Currency the order was created with, in ISO format"""
    customer_id: list[int]
    """User ID who owns the order (0 for guests)"""
    customer_ip_address: list[str]
    """Customer's IP address"""
    customer_note: list[str]
    """Note left by the customer during checkout"""
    customer_user_agent: list[str]
    """User agent of the customer"""
    date_completed: list[str]
    """The date the order was completed, in the site's timezone"""
    date_completed_gmt: list[str]
    """The date the order was completed, as GMT"""
    date_created: list[str]
    """The date the order was created, in the site's timezone"""
    date_created_gmt: list[str]
    """The date the order was created, as GMT"""
    date_modified: list[str]
    """The date the order was last modified, in the site's timezone"""
    date_modified_gmt: list[str]
    """The date the order was last modified, as GMT"""
    date_paid: list[str]
    """The date the order was paid, in the site's timezone"""
    date_paid_gmt: list[str]
    """The date the order was paid, as GMT"""
    discount_tax: list[str]
    """Total discount tax amount for the order"""
    discount_total: list[str]
    """Total discount amount for the order"""
    fee_lines: list[list[Any]]
    """Fee lines data"""
    id: list[int]
    """Unique identifier for the resource"""
    line_items: list[list[Any]]
    """Line items data"""
    meta_data: list[list[Any]]
    """Meta data"""
    number: list[str]
    """Order number"""
    order_key: list[str]
    """Order key"""
    parent_id: list[int]
    """Parent order ID"""
    payment_method: list[str]
    """Payment method ID"""
    payment_method_title: list[str]
    """Payment method title"""
    prices_include_tax: list[bool]
    """True if the prices included tax during checkout"""
    refunds: list[list[Any]]
    """List of refunds"""
    shipping: list[dict[str, Any]]
    """Shipping address"""
    shipping_lines: list[list[Any]]
    """Shipping lines data"""
    shipping_tax: list[str]
    """Total shipping tax amount for the order"""
    shipping_total: list[str]
    """Total shipping amount for the order"""
    status: list[str]
    """Order status"""
    tax_lines: list[list[Any]]
    """Tax lines data"""
    total: list[str]
    """Grand total"""
    total_tax: list[str]
    """Sum of all taxes"""
    transaction_id: list[str]
    """Unique transaction ID"""
    version: list[str]
    """Version of WooCommerce which last updated the order"""


class OrdersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    billing: Any
    """Billing address"""
    cart_hash: Any
    """MD5 hash of cart items to ensure orders are not modified"""
    cart_tax: Any
    """Sum of line item taxes only"""
    coupon_lines: Any
    """Coupons line data"""
    created_via: Any
    """Shows where the order was created"""
    currency: Any
    """Currency the order was created with, in ISO format"""
    customer_id: Any
    """User ID who owns the order (0 for guests)"""
    customer_ip_address: Any
    """Customer's IP address"""
    customer_note: Any
    """Note left by the customer during checkout"""
    customer_user_agent: Any
    """User agent of the customer"""
    date_completed: Any
    """The date the order was completed, in the site's timezone"""
    date_completed_gmt: Any
    """The date the order was completed, as GMT"""
    date_created: Any
    """The date the order was created, in the site's timezone"""
    date_created_gmt: Any
    """The date the order was created, as GMT"""
    date_modified: Any
    """The date the order was last modified, in the site's timezone"""
    date_modified_gmt: Any
    """The date the order was last modified, as GMT"""
    date_paid: Any
    """The date the order was paid, in the site's timezone"""
    date_paid_gmt: Any
    """The date the order was paid, as GMT"""
    discount_tax: Any
    """Total discount tax amount for the order"""
    discount_total: Any
    """Total discount amount for the order"""
    fee_lines: Any
    """Fee lines data"""
    id: Any
    """Unique identifier for the resource"""
    line_items: Any
    """Line items data"""
    meta_data: Any
    """Meta data"""
    number: Any
    """Order number"""
    order_key: Any
    """Order key"""
    parent_id: Any
    """Parent order ID"""
    payment_method: Any
    """Payment method ID"""
    payment_method_title: Any
    """Payment method title"""
    prices_include_tax: Any
    """True if the prices included tax during checkout"""
    refunds: Any
    """List of refunds"""
    shipping: Any
    """Shipping address"""
    shipping_lines: Any
    """Shipping lines data"""
    shipping_tax: Any
    """Total shipping tax amount for the order"""
    shipping_total: Any
    """Total shipping amount for the order"""
    status: Any
    """Order status"""
    tax_lines: Any
    """Tax lines data"""
    total: Any
    """Grand total"""
    total_tax: Any
    """Sum of all taxes"""
    transaction_id: Any
    """Unique transaction ID"""
    version: Any
    """Version of WooCommerce which last updated the order"""


class OrdersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    billing: str
    """Billing address"""
    cart_hash: str
    """MD5 hash of cart items to ensure orders are not modified"""
    cart_tax: str
    """Sum of line item taxes only"""
    coupon_lines: str
    """Coupons line data"""
    created_via: str
    """Shows where the order was created"""
    currency: str
    """Currency the order was created with, in ISO format"""
    customer_id: str
    """User ID who owns the order (0 for guests)"""
    customer_ip_address: str
    """Customer's IP address"""
    customer_note: str
    """Note left by the customer during checkout"""
    customer_user_agent: str
    """User agent of the customer"""
    date_completed: str
    """The date the order was completed, in the site's timezone"""
    date_completed_gmt: str
    """The date the order was completed, as GMT"""
    date_created: str
    """The date the order was created, in the site's timezone"""
    date_created_gmt: str
    """The date the order was created, as GMT"""
    date_modified: str
    """The date the order was last modified, in the site's timezone"""
    date_modified_gmt: str
    """The date the order was last modified, as GMT"""
    date_paid: str
    """The date the order was paid, in the site's timezone"""
    date_paid_gmt: str
    """The date the order was paid, as GMT"""
    discount_tax: str
    """Total discount tax amount for the order"""
    discount_total: str
    """Total discount amount for the order"""
    fee_lines: str
    """Fee lines data"""
    id: str
    """Unique identifier for the resource"""
    line_items: str
    """Line items data"""
    meta_data: str
    """Meta data"""
    number: str
    """Order number"""
    order_key: str
    """Order key"""
    parent_id: str
    """Parent order ID"""
    payment_method: str
    """Payment method ID"""
    payment_method_title: str
    """Payment method title"""
    prices_include_tax: str
    """True if the prices included tax during checkout"""
    refunds: str
    """List of refunds"""
    shipping: str
    """Shipping address"""
    shipping_lines: str
    """Shipping lines data"""
    shipping_tax: str
    """Total shipping tax amount for the order"""
    shipping_total: str
    """Total shipping amount for the order"""
    status: str
    """Order status"""
    tax_lines: str
    """Tax lines data"""
    total: str
    """Grand total"""
    total_tax: str
    """Sum of all taxes"""
    transaction_id: str
    """Unique transaction ID"""
    version: str
    """Version of WooCommerce which last updated the order"""


class OrdersSortFilter(TypedDict, total=False):
    """Available fields for sorting orders search results."""
    billing: AirbyteSortOrder
    """Billing address"""
    cart_hash: AirbyteSortOrder
    """MD5 hash of cart items to ensure orders are not modified"""
    cart_tax: AirbyteSortOrder
    """Sum of line item taxes only"""
    coupon_lines: AirbyteSortOrder
    """Coupons line data"""
    created_via: AirbyteSortOrder
    """Shows where the order was created"""
    currency: AirbyteSortOrder
    """Currency the order was created with, in ISO format"""
    customer_id: AirbyteSortOrder
    """User ID who owns the order (0 for guests)"""
    customer_ip_address: AirbyteSortOrder
    """Customer's IP address"""
    customer_note: AirbyteSortOrder
    """Note left by the customer during checkout"""
    customer_user_agent: AirbyteSortOrder
    """User agent of the customer"""
    date_completed: AirbyteSortOrder
    """The date the order was completed, in the site's timezone"""
    date_completed_gmt: AirbyteSortOrder
    """The date the order was completed, as GMT"""
    date_created: AirbyteSortOrder
    """The date the order was created, in the site's timezone"""
    date_created_gmt: AirbyteSortOrder
    """The date the order was created, as GMT"""
    date_modified: AirbyteSortOrder
    """The date the order was last modified, in the site's timezone"""
    date_modified_gmt: AirbyteSortOrder
    """The date the order was last modified, as GMT"""
    date_paid: AirbyteSortOrder
    """The date the order was paid, in the site's timezone"""
    date_paid_gmt: AirbyteSortOrder
    """The date the order was paid, as GMT"""
    discount_tax: AirbyteSortOrder
    """Total discount tax amount for the order"""
    discount_total: AirbyteSortOrder
    """Total discount amount for the order"""
    fee_lines: AirbyteSortOrder
    """Fee lines data"""
    id: AirbyteSortOrder
    """Unique identifier for the resource"""
    line_items: AirbyteSortOrder
    """Line items data"""
    meta_data: AirbyteSortOrder
    """Meta data"""
    number: AirbyteSortOrder
    """Order number"""
    order_key: AirbyteSortOrder
    """Order key"""
    parent_id: AirbyteSortOrder
    """Parent order ID"""
    payment_method: AirbyteSortOrder
    """Payment method ID"""
    payment_method_title: AirbyteSortOrder
    """Payment method title"""
    prices_include_tax: AirbyteSortOrder
    """True if the prices included tax during checkout"""
    refunds: AirbyteSortOrder
    """List of refunds"""
    shipping: AirbyteSortOrder
    """Shipping address"""
    shipping_lines: AirbyteSortOrder
    """Shipping lines data"""
    shipping_tax: AirbyteSortOrder
    """Total shipping tax amount for the order"""
    shipping_total: AirbyteSortOrder
    """Total shipping amount for the order"""
    status: AirbyteSortOrder
    """Order status"""
    tax_lines: AirbyteSortOrder
    """Tax lines data"""
    total: AirbyteSortOrder
    """Grand total"""
    total_tax: AirbyteSortOrder
    """Sum of all taxes"""
    transaction_id: AirbyteSortOrder
    """Unique transaction ID"""
    version: AirbyteSortOrder
    """Version of WooCommerce which last updated the order"""


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


# ===== PRODUCTS SEARCH TYPES =====

class ProductsSearchFilter(TypedDict, total=False):
    """Available fields for filtering products search queries."""
    attributes: list[Any] | None
    """List of attributes"""
    average_rating: str | None
    """Reviews average rating"""
    backordered: bool | None
    """Shows if the product is on backordered"""
    backorders: str | None
    """If managing stock, this controls if backorders are allowed"""
    backorders_allowed: bool | None
    """Shows if backorders are allowed"""
    button_text: str | None
    """Product external button text"""
    catalog_visibility: str | None
    """Catalog visibility"""
    categories: list[Any] | None
    """List of categories"""
    cross_sell_ids: list[Any] | None
    """List of cross-sell products IDs"""
    date_created: str | None
    """The date the product was created"""
    date_created_gmt: str | None
    """The date the product was created, as GMT"""
    date_modified: str | None
    """The date the product was last modified"""
    date_modified_gmt: str | None
    """The date the product was last modified, as GMT"""
    date_on_sale_from: str | None
    """Start date of sale price"""
    date_on_sale_from_gmt: str | None
    """Start date of sale price, as GMT"""
    date_on_sale_to: str | None
    """End date of sale price"""
    date_on_sale_to_gmt: str | None
    """End date of sale price, as GMT"""
    default_attributes: list[Any] | None
    """Defaults variation attributes"""
    description: str | None
    """Product description"""
    dimensions: dict[str, Any] | None
    """Product dimensions"""
    download_expiry: int | None
    """Number of days until access to downloadable files expires"""
    download_limit: int | None
    """Number of times downloadable files can be downloaded"""
    downloadable: bool | None
    """If the product is downloadable"""
    downloads: list[Any] | None
    """List of downloadable files"""
    external_url: str | None
    """Product external URL"""
    grouped_products: list[Any] | None
    """List of grouped products ID"""
    id: int | None
    """Unique identifier for the resource"""
    images: list[Any] | None
    """List of images"""
    manage_stock: bool | None
    """Stock management at product level"""
    menu_order: int | None
    """Menu order"""
    meta_data: list[Any] | None
    """Meta data"""
    name: str | None
    """Product name"""
    on_sale: bool | None
    """Shows if the product is on sale"""
    parent_id: int | None
    """Product parent ID"""
    permalink: str | None
    """Product URL"""
    price: str | None
    """Current product price"""
    price_html: str | None
    """Price formatted in HTML"""
    purchasable: bool | None
    """Shows if the product can be bought"""
    purchase_note: str | None
    """Note to send customer after purchase"""
    rating_count: int | None
    """Amount of reviews"""
    regular_price: str | None
    """Product regular price"""
    related_ids: list[Any] | None
    """List of related products IDs"""
    reviews_allowed: bool | None
    """Allow reviews"""
    sale_price: str | None
    """Product sale price"""
    shipping_class: str | None
    """Shipping class slug"""
    shipping_class_id: int | None
    """Shipping class ID"""
    shipping_required: bool | None
    """Shows if the product needs to be shipped"""
    shipping_taxable: bool | None
    """Shows if product shipping is taxable"""
    short_description: str | None
    """Product short description"""
    sku: str | None
    """Unique identifier (SKU)"""
    slug: str | None
    """Product slug"""
    sold_individually: bool | None
    """Allow one item per order"""
    status: str | None
    """Product status"""
    stock_quantity: int | None
    """Stock quantity"""
    stock_status: str | None
    """Controls the stock status"""
    tags: list[Any] | None
    """List of tags"""
    tax_class: str | None
    """Tax class"""
    tax_status: str | None
    """Tax status"""
    total_sales: int | None
    """Amount of sales"""
    type_: str | None
    """Product type"""
    upsell_ids: list[Any] | None
    """List of up-sell products IDs"""
    variations: list[Any] | None
    """List of variations IDs"""
    virtual: bool | None
    """If the product is virtual"""
    weight: str | None
    """Product weight"""


class ProductsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attributes: list[list[Any]]
    """List of attributes"""
    average_rating: list[str]
    """Reviews average rating"""
    backordered: list[bool]
    """Shows if the product is on backordered"""
    backorders: list[str]
    """If managing stock, this controls if backorders are allowed"""
    backorders_allowed: list[bool]
    """Shows if backorders are allowed"""
    button_text: list[str]
    """Product external button text"""
    catalog_visibility: list[str]
    """Catalog visibility"""
    categories: list[list[Any]]
    """List of categories"""
    cross_sell_ids: list[list[Any]]
    """List of cross-sell products IDs"""
    date_created: list[str]
    """The date the product was created"""
    date_created_gmt: list[str]
    """The date the product was created, as GMT"""
    date_modified: list[str]
    """The date the product was last modified"""
    date_modified_gmt: list[str]
    """The date the product was last modified, as GMT"""
    date_on_sale_from: list[str]
    """Start date of sale price"""
    date_on_sale_from_gmt: list[str]
    """Start date of sale price, as GMT"""
    date_on_sale_to: list[str]
    """End date of sale price"""
    date_on_sale_to_gmt: list[str]
    """End date of sale price, as GMT"""
    default_attributes: list[list[Any]]
    """Defaults variation attributes"""
    description: list[str]
    """Product description"""
    dimensions: list[dict[str, Any]]
    """Product dimensions"""
    download_expiry: list[int]
    """Number of days until access to downloadable files expires"""
    download_limit: list[int]
    """Number of times downloadable files can be downloaded"""
    downloadable: list[bool]
    """If the product is downloadable"""
    downloads: list[list[Any]]
    """List of downloadable files"""
    external_url: list[str]
    """Product external URL"""
    grouped_products: list[list[Any]]
    """List of grouped products ID"""
    id: list[int]
    """Unique identifier for the resource"""
    images: list[list[Any]]
    """List of images"""
    manage_stock: list[bool]
    """Stock management at product level"""
    menu_order: list[int]
    """Menu order"""
    meta_data: list[list[Any]]
    """Meta data"""
    name: list[str]
    """Product name"""
    on_sale: list[bool]
    """Shows if the product is on sale"""
    parent_id: list[int]
    """Product parent ID"""
    permalink: list[str]
    """Product URL"""
    price: list[str]
    """Current product price"""
    price_html: list[str]
    """Price formatted in HTML"""
    purchasable: list[bool]
    """Shows if the product can be bought"""
    purchase_note: list[str]
    """Note to send customer after purchase"""
    rating_count: list[int]
    """Amount of reviews"""
    regular_price: list[str]
    """Product regular price"""
    related_ids: list[list[Any]]
    """List of related products IDs"""
    reviews_allowed: list[bool]
    """Allow reviews"""
    sale_price: list[str]
    """Product sale price"""
    shipping_class: list[str]
    """Shipping class slug"""
    shipping_class_id: list[int]
    """Shipping class ID"""
    shipping_required: list[bool]
    """Shows if the product needs to be shipped"""
    shipping_taxable: list[bool]
    """Shows if product shipping is taxable"""
    short_description: list[str]
    """Product short description"""
    sku: list[str]
    """Unique identifier (SKU)"""
    slug: list[str]
    """Product slug"""
    sold_individually: list[bool]
    """Allow one item per order"""
    status: list[str]
    """Product status"""
    stock_quantity: list[int]
    """Stock quantity"""
    stock_status: list[str]
    """Controls the stock status"""
    tags: list[list[Any]]
    """List of tags"""
    tax_class: list[str]
    """Tax class"""
    tax_status: list[str]
    """Tax status"""
    total_sales: list[int]
    """Amount of sales"""
    type_: list[str]
    """Product type"""
    upsell_ids: list[list[Any]]
    """List of up-sell products IDs"""
    variations: list[list[Any]]
    """List of variations IDs"""
    virtual: list[bool]
    """If the product is virtual"""
    weight: list[str]
    """Product weight"""


class ProductsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attributes: Any
    """List of attributes"""
    average_rating: Any
    """Reviews average rating"""
    backordered: Any
    """Shows if the product is on backordered"""
    backorders: Any
    """If managing stock, this controls if backorders are allowed"""
    backorders_allowed: Any
    """Shows if backorders are allowed"""
    button_text: Any
    """Product external button text"""
    catalog_visibility: Any
    """Catalog visibility"""
    categories: Any
    """List of categories"""
    cross_sell_ids: Any
    """List of cross-sell products IDs"""
    date_created: Any
    """The date the product was created"""
    date_created_gmt: Any
    """The date the product was created, as GMT"""
    date_modified: Any
    """The date the product was last modified"""
    date_modified_gmt: Any
    """The date the product was last modified, as GMT"""
    date_on_sale_from: Any
    """Start date of sale price"""
    date_on_sale_from_gmt: Any
    """Start date of sale price, as GMT"""
    date_on_sale_to: Any
    """End date of sale price"""
    date_on_sale_to_gmt: Any
    """End date of sale price, as GMT"""
    default_attributes: Any
    """Defaults variation attributes"""
    description: Any
    """Product description"""
    dimensions: Any
    """Product dimensions"""
    download_expiry: Any
    """Number of days until access to downloadable files expires"""
    download_limit: Any
    """Number of times downloadable files can be downloaded"""
    downloadable: Any
    """If the product is downloadable"""
    downloads: Any
    """List of downloadable files"""
    external_url: Any
    """Product external URL"""
    grouped_products: Any
    """List of grouped products ID"""
    id: Any
    """Unique identifier for the resource"""
    images: Any
    """List of images"""
    manage_stock: Any
    """Stock management at product level"""
    menu_order: Any
    """Menu order"""
    meta_data: Any
    """Meta data"""
    name: Any
    """Product name"""
    on_sale: Any
    """Shows if the product is on sale"""
    parent_id: Any
    """Product parent ID"""
    permalink: Any
    """Product URL"""
    price: Any
    """Current product price"""
    price_html: Any
    """Price formatted in HTML"""
    purchasable: Any
    """Shows if the product can be bought"""
    purchase_note: Any
    """Note to send customer after purchase"""
    rating_count: Any
    """Amount of reviews"""
    regular_price: Any
    """Product regular price"""
    related_ids: Any
    """List of related products IDs"""
    reviews_allowed: Any
    """Allow reviews"""
    sale_price: Any
    """Product sale price"""
    shipping_class: Any
    """Shipping class slug"""
    shipping_class_id: Any
    """Shipping class ID"""
    shipping_required: Any
    """Shows if the product needs to be shipped"""
    shipping_taxable: Any
    """Shows if product shipping is taxable"""
    short_description: Any
    """Product short description"""
    sku: Any
    """Unique identifier (SKU)"""
    slug: Any
    """Product slug"""
    sold_individually: Any
    """Allow one item per order"""
    status: Any
    """Product status"""
    stock_quantity: Any
    """Stock quantity"""
    stock_status: Any
    """Controls the stock status"""
    tags: Any
    """List of tags"""
    tax_class: Any
    """Tax class"""
    tax_status: Any
    """Tax status"""
    total_sales: Any
    """Amount of sales"""
    type_: Any
    """Product type"""
    upsell_ids: Any
    """List of up-sell products IDs"""
    variations: Any
    """List of variations IDs"""
    virtual: Any
    """If the product is virtual"""
    weight: Any
    """Product weight"""


class ProductsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    attributes: str
    """List of attributes"""
    average_rating: str
    """Reviews average rating"""
    backordered: str
    """Shows if the product is on backordered"""
    backorders: str
    """If managing stock, this controls if backorders are allowed"""
    backorders_allowed: str
    """Shows if backorders are allowed"""
    button_text: str
    """Product external button text"""
    catalog_visibility: str
    """Catalog visibility"""
    categories: str
    """List of categories"""
    cross_sell_ids: str
    """List of cross-sell products IDs"""
    date_created: str
    """The date the product was created"""
    date_created_gmt: str
    """The date the product was created, as GMT"""
    date_modified: str
    """The date the product was last modified"""
    date_modified_gmt: str
    """The date the product was last modified, as GMT"""
    date_on_sale_from: str
    """Start date of sale price"""
    date_on_sale_from_gmt: str
    """Start date of sale price, as GMT"""
    date_on_sale_to: str
    """End date of sale price"""
    date_on_sale_to_gmt: str
    """End date of sale price, as GMT"""
    default_attributes: str
    """Defaults variation attributes"""
    description: str
    """Product description"""
    dimensions: str
    """Product dimensions"""
    download_expiry: str
    """Number of days until access to downloadable files expires"""
    download_limit: str
    """Number of times downloadable files can be downloaded"""
    downloadable: str
    """If the product is downloadable"""
    downloads: str
    """List of downloadable files"""
    external_url: str
    """Product external URL"""
    grouped_products: str
    """List of grouped products ID"""
    id: str
    """Unique identifier for the resource"""
    images: str
    """List of images"""
    manage_stock: str
    """Stock management at product level"""
    menu_order: str
    """Menu order"""
    meta_data: str
    """Meta data"""
    name: str
    """Product name"""
    on_sale: str
    """Shows if the product is on sale"""
    parent_id: str
    """Product parent ID"""
    permalink: str
    """Product URL"""
    price: str
    """Current product price"""
    price_html: str
    """Price formatted in HTML"""
    purchasable: str
    """Shows if the product can be bought"""
    purchase_note: str
    """Note to send customer after purchase"""
    rating_count: str
    """Amount of reviews"""
    regular_price: str
    """Product regular price"""
    related_ids: str
    """List of related products IDs"""
    reviews_allowed: str
    """Allow reviews"""
    sale_price: str
    """Product sale price"""
    shipping_class: str
    """Shipping class slug"""
    shipping_class_id: str
    """Shipping class ID"""
    shipping_required: str
    """Shows if the product needs to be shipped"""
    shipping_taxable: str
    """Shows if product shipping is taxable"""
    short_description: str
    """Product short description"""
    sku: str
    """Unique identifier (SKU)"""
    slug: str
    """Product slug"""
    sold_individually: str
    """Allow one item per order"""
    status: str
    """Product status"""
    stock_quantity: str
    """Stock quantity"""
    stock_status: str
    """Controls the stock status"""
    tags: str
    """List of tags"""
    tax_class: str
    """Tax class"""
    tax_status: str
    """Tax status"""
    total_sales: str
    """Amount of sales"""
    type_: str
    """Product type"""
    upsell_ids: str
    """List of up-sell products IDs"""
    variations: str
    """List of variations IDs"""
    virtual: str
    """If the product is virtual"""
    weight: str
    """Product weight"""


class ProductsSortFilter(TypedDict, total=False):
    """Available fields for sorting products search results."""
    attributes: AirbyteSortOrder
    """List of attributes"""
    average_rating: AirbyteSortOrder
    """Reviews average rating"""
    backordered: AirbyteSortOrder
    """Shows if the product is on backordered"""
    backorders: AirbyteSortOrder
    """If managing stock, this controls if backorders are allowed"""
    backorders_allowed: AirbyteSortOrder
    """Shows if backorders are allowed"""
    button_text: AirbyteSortOrder
    """Product external button text"""
    catalog_visibility: AirbyteSortOrder
    """Catalog visibility"""
    categories: AirbyteSortOrder
    """List of categories"""
    cross_sell_ids: AirbyteSortOrder
    """List of cross-sell products IDs"""
    date_created: AirbyteSortOrder
    """The date the product was created"""
    date_created_gmt: AirbyteSortOrder
    """The date the product was created, as GMT"""
    date_modified: AirbyteSortOrder
    """The date the product was last modified"""
    date_modified_gmt: AirbyteSortOrder
    """The date the product was last modified, as GMT"""
    date_on_sale_from: AirbyteSortOrder
    """Start date of sale price"""
    date_on_sale_from_gmt: AirbyteSortOrder
    """Start date of sale price, as GMT"""
    date_on_sale_to: AirbyteSortOrder
    """End date of sale price"""
    date_on_sale_to_gmt: AirbyteSortOrder
    """End date of sale price, as GMT"""
    default_attributes: AirbyteSortOrder
    """Defaults variation attributes"""
    description: AirbyteSortOrder
    """Product description"""
    dimensions: AirbyteSortOrder
    """Product dimensions"""
    download_expiry: AirbyteSortOrder
    """Number of days until access to downloadable files expires"""
    download_limit: AirbyteSortOrder
    """Number of times downloadable files can be downloaded"""
    downloadable: AirbyteSortOrder
    """If the product is downloadable"""
    downloads: AirbyteSortOrder
    """List of downloadable files"""
    external_url: AirbyteSortOrder
    """Product external URL"""
    grouped_products: AirbyteSortOrder
    """List of grouped products ID"""
    id: AirbyteSortOrder
    """Unique identifier for the resource"""
    images: AirbyteSortOrder
    """List of images"""
    manage_stock: AirbyteSortOrder
    """Stock management at product level"""
    menu_order: AirbyteSortOrder
    """Menu order"""
    meta_data: AirbyteSortOrder
    """Meta data"""
    name: AirbyteSortOrder
    """Product name"""
    on_sale: AirbyteSortOrder
    """Shows if the product is on sale"""
    parent_id: AirbyteSortOrder
    """Product parent ID"""
    permalink: AirbyteSortOrder
    """Product URL"""
    price: AirbyteSortOrder
    """Current product price"""
    price_html: AirbyteSortOrder
    """Price formatted in HTML"""
    purchasable: AirbyteSortOrder
    """Shows if the product can be bought"""
    purchase_note: AirbyteSortOrder
    """Note to send customer after purchase"""
    rating_count: AirbyteSortOrder
    """Amount of reviews"""
    regular_price: AirbyteSortOrder
    """Product regular price"""
    related_ids: AirbyteSortOrder
    """List of related products IDs"""
    reviews_allowed: AirbyteSortOrder
    """Allow reviews"""
    sale_price: AirbyteSortOrder
    """Product sale price"""
    shipping_class: AirbyteSortOrder
    """Shipping class slug"""
    shipping_class_id: AirbyteSortOrder
    """Shipping class ID"""
    shipping_required: AirbyteSortOrder
    """Shows if the product needs to be shipped"""
    shipping_taxable: AirbyteSortOrder
    """Shows if product shipping is taxable"""
    short_description: AirbyteSortOrder
    """Product short description"""
    sku: AirbyteSortOrder
    """Unique identifier (SKU)"""
    slug: AirbyteSortOrder
    """Product slug"""
    sold_individually: AirbyteSortOrder
    """Allow one item per order"""
    status: AirbyteSortOrder
    """Product status"""
    stock_quantity: AirbyteSortOrder
    """Stock quantity"""
    stock_status: AirbyteSortOrder
    """Controls the stock status"""
    tags: AirbyteSortOrder
    """List of tags"""
    tax_class: AirbyteSortOrder
    """Tax class"""
    tax_status: AirbyteSortOrder
    """Tax status"""
    total_sales: AirbyteSortOrder
    """Amount of sales"""
    type_: AirbyteSortOrder
    """Product type"""
    upsell_ids: AirbyteSortOrder
    """List of up-sell products IDs"""
    variations: AirbyteSortOrder
    """List of variations IDs"""
    virtual: AirbyteSortOrder
    """If the product is virtual"""
    weight: AirbyteSortOrder
    """Product weight"""


# Entity-specific condition types for products
class ProductsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProductsSearchFilter


class ProductsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProductsSearchFilter


class ProductsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProductsSearchFilter


class ProductsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProductsSearchFilter


class ProductsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProductsSearchFilter


class ProductsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProductsSearchFilter


class ProductsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProductsStringFilter


class ProductsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProductsStringFilter


class ProductsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProductsStringFilter


class ProductsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProductsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProductsInCondition = TypedDict("ProductsInCondition", {"in": ProductsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProductsNotCondition = TypedDict("ProductsNotCondition", {"not": "ProductsCondition"}, total=False)
"""Negates the nested condition."""

ProductsAndCondition = TypedDict("ProductsAndCondition", {"and": "list[ProductsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProductsOrCondition = TypedDict("ProductsOrCondition", {"or": "list[ProductsCondition]"}, total=False)
"""True if any nested condition is true."""

ProductsAnyCondition = TypedDict("ProductsAnyCondition", {"any": ProductsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all products condition types
ProductsCondition = (
    ProductsEqCondition
    | ProductsNeqCondition
    | ProductsGtCondition
    | ProductsGteCondition
    | ProductsLtCondition
    | ProductsLteCondition
    | ProductsInCondition
    | ProductsLikeCondition
    | ProductsFuzzyCondition
    | ProductsKeywordCondition
    | ProductsContainsCondition
    | ProductsNotCondition
    | ProductsAndCondition
    | ProductsOrCondition
    | ProductsAnyCondition
)


class ProductsSearchQuery(TypedDict, total=False):
    """Search query for products entity."""
    filter: ProductsCondition
    sort: list[ProductsSortFilter]


# ===== COUPONS SEARCH TYPES =====

class CouponsSearchFilter(TypedDict, total=False):
    """Available fields for filtering coupons search queries."""
    amount: str | None
    """The amount of discount"""
    code: str | None
    """Coupon code"""
    date_created: str | None
    """The date the coupon was created"""
    date_created_gmt: str | None
    """The date the coupon was created, as GMT"""
    date_expires: str | None
    """The date the coupon expires"""
    date_expires_gmt: str | None
    """The date the coupon expires, as GMT"""
    date_modified: str | None
    """The date the coupon was last modified"""
    date_modified_gmt: str | None
    """The date the coupon was last modified, as GMT"""
    description: str | None
    """Coupon description"""
    discount_type: str | None
    """Determines the type of discount"""
    email_restrictions: list[Any] | None
    """List of email addresses that can use this coupon"""
    exclude_sale_items: bool | None
    """If true, not applied to sale items"""
    excluded_product_categories: list[Any] | None
    """Excluded category IDs"""
    excluded_product_ids: list[Any] | None
    """Excluded product IDs"""
    free_shipping: bool | None
    """Enables free shipping"""
    id: int | None
    """Unique identifier"""
    individual_use: bool | None
    """Can only be used individually"""
    limit_usage_to_x_items: int | None
    """Max cart items coupon applies to"""
    maximum_amount: str | None
    """Maximum order amount"""
    meta_data: list[Any] | None
    """Meta data"""
    minimum_amount: str | None
    """Minimum order amount"""
    product_categories: list[Any] | None
    """Applicable category IDs"""
    product_ids: list[Any] | None
    """Applicable product IDs"""
    usage_count: int | None
    """Times used"""
    usage_limit: int | None
    """Total usage limit"""
    usage_limit_per_user: int | None
    """Per-customer usage limit"""
    used_by: list[Any] | None
    """Users who have used the coupon"""


class CouponsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    amount: list[str]
    """The amount of discount"""
    code: list[str]
    """Coupon code"""
    date_created: list[str]
    """The date the coupon was created"""
    date_created_gmt: list[str]
    """The date the coupon was created, as GMT"""
    date_expires: list[str]
    """The date the coupon expires"""
    date_expires_gmt: list[str]
    """The date the coupon expires, as GMT"""
    date_modified: list[str]
    """The date the coupon was last modified"""
    date_modified_gmt: list[str]
    """The date the coupon was last modified, as GMT"""
    description: list[str]
    """Coupon description"""
    discount_type: list[str]
    """Determines the type of discount"""
    email_restrictions: list[list[Any]]
    """List of email addresses that can use this coupon"""
    exclude_sale_items: list[bool]
    """If true, not applied to sale items"""
    excluded_product_categories: list[list[Any]]
    """Excluded category IDs"""
    excluded_product_ids: list[list[Any]]
    """Excluded product IDs"""
    free_shipping: list[bool]
    """Enables free shipping"""
    id: list[int]
    """Unique identifier"""
    individual_use: list[bool]
    """Can only be used individually"""
    limit_usage_to_x_items: list[int]
    """Max cart items coupon applies to"""
    maximum_amount: list[str]
    """Maximum order amount"""
    meta_data: list[list[Any]]
    """Meta data"""
    minimum_amount: list[str]
    """Minimum order amount"""
    product_categories: list[list[Any]]
    """Applicable category IDs"""
    product_ids: list[list[Any]]
    """Applicable product IDs"""
    usage_count: list[int]
    """Times used"""
    usage_limit: list[int]
    """Total usage limit"""
    usage_limit_per_user: list[int]
    """Per-customer usage limit"""
    used_by: list[list[Any]]
    """Users who have used the coupon"""


class CouponsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    amount: Any
    """The amount of discount"""
    code: Any
    """Coupon code"""
    date_created: Any
    """The date the coupon was created"""
    date_created_gmt: Any
    """The date the coupon was created, as GMT"""
    date_expires: Any
    """The date the coupon expires"""
    date_expires_gmt: Any
    """The date the coupon expires, as GMT"""
    date_modified: Any
    """The date the coupon was last modified"""
    date_modified_gmt: Any
    """The date the coupon was last modified, as GMT"""
    description: Any
    """Coupon description"""
    discount_type: Any
    """Determines the type of discount"""
    email_restrictions: Any
    """List of email addresses that can use this coupon"""
    exclude_sale_items: Any
    """If true, not applied to sale items"""
    excluded_product_categories: Any
    """Excluded category IDs"""
    excluded_product_ids: Any
    """Excluded product IDs"""
    free_shipping: Any
    """Enables free shipping"""
    id: Any
    """Unique identifier"""
    individual_use: Any
    """Can only be used individually"""
    limit_usage_to_x_items: Any
    """Max cart items coupon applies to"""
    maximum_amount: Any
    """Maximum order amount"""
    meta_data: Any
    """Meta data"""
    minimum_amount: Any
    """Minimum order amount"""
    product_categories: Any
    """Applicable category IDs"""
    product_ids: Any
    """Applicable product IDs"""
    usage_count: Any
    """Times used"""
    usage_limit: Any
    """Total usage limit"""
    usage_limit_per_user: Any
    """Per-customer usage limit"""
    used_by: Any
    """Users who have used the coupon"""


class CouponsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    amount: str
    """The amount of discount"""
    code: str
    """Coupon code"""
    date_created: str
    """The date the coupon was created"""
    date_created_gmt: str
    """The date the coupon was created, as GMT"""
    date_expires: str
    """The date the coupon expires"""
    date_expires_gmt: str
    """The date the coupon expires, as GMT"""
    date_modified: str
    """The date the coupon was last modified"""
    date_modified_gmt: str
    """The date the coupon was last modified, as GMT"""
    description: str
    """Coupon description"""
    discount_type: str
    """Determines the type of discount"""
    email_restrictions: str
    """List of email addresses that can use this coupon"""
    exclude_sale_items: str
    """If true, not applied to sale items"""
    excluded_product_categories: str
    """Excluded category IDs"""
    excluded_product_ids: str
    """Excluded product IDs"""
    free_shipping: str
    """Enables free shipping"""
    id: str
    """Unique identifier"""
    individual_use: str
    """Can only be used individually"""
    limit_usage_to_x_items: str
    """Max cart items coupon applies to"""
    maximum_amount: str
    """Maximum order amount"""
    meta_data: str
    """Meta data"""
    minimum_amount: str
    """Minimum order amount"""
    product_categories: str
    """Applicable category IDs"""
    product_ids: str
    """Applicable product IDs"""
    usage_count: str
    """Times used"""
    usage_limit: str
    """Total usage limit"""
    usage_limit_per_user: str
    """Per-customer usage limit"""
    used_by: str
    """Users who have used the coupon"""


class CouponsSortFilter(TypedDict, total=False):
    """Available fields for sorting coupons search results."""
    amount: AirbyteSortOrder
    """The amount of discount"""
    code: AirbyteSortOrder
    """Coupon code"""
    date_created: AirbyteSortOrder
    """The date the coupon was created"""
    date_created_gmt: AirbyteSortOrder
    """The date the coupon was created, as GMT"""
    date_expires: AirbyteSortOrder
    """The date the coupon expires"""
    date_expires_gmt: AirbyteSortOrder
    """The date the coupon expires, as GMT"""
    date_modified: AirbyteSortOrder
    """The date the coupon was last modified"""
    date_modified_gmt: AirbyteSortOrder
    """The date the coupon was last modified, as GMT"""
    description: AirbyteSortOrder
    """Coupon description"""
    discount_type: AirbyteSortOrder
    """Determines the type of discount"""
    email_restrictions: AirbyteSortOrder
    """List of email addresses that can use this coupon"""
    exclude_sale_items: AirbyteSortOrder
    """If true, not applied to sale items"""
    excluded_product_categories: AirbyteSortOrder
    """Excluded category IDs"""
    excluded_product_ids: AirbyteSortOrder
    """Excluded product IDs"""
    free_shipping: AirbyteSortOrder
    """Enables free shipping"""
    id: AirbyteSortOrder
    """Unique identifier"""
    individual_use: AirbyteSortOrder
    """Can only be used individually"""
    limit_usage_to_x_items: AirbyteSortOrder
    """Max cart items coupon applies to"""
    maximum_amount: AirbyteSortOrder
    """Maximum order amount"""
    meta_data: AirbyteSortOrder
    """Meta data"""
    minimum_amount: AirbyteSortOrder
    """Minimum order amount"""
    product_categories: AirbyteSortOrder
    """Applicable category IDs"""
    product_ids: AirbyteSortOrder
    """Applicable product IDs"""
    usage_count: AirbyteSortOrder
    """Times used"""
    usage_limit: AirbyteSortOrder
    """Total usage limit"""
    usage_limit_per_user: AirbyteSortOrder
    """Per-customer usage limit"""
    used_by: AirbyteSortOrder
    """Users who have used the coupon"""


# Entity-specific condition types for coupons
class CouponsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CouponsSearchFilter


class CouponsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CouponsSearchFilter


class CouponsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CouponsSearchFilter


class CouponsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CouponsSearchFilter


class CouponsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CouponsSearchFilter


class CouponsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CouponsSearchFilter


class CouponsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CouponsStringFilter


class CouponsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CouponsStringFilter


class CouponsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CouponsStringFilter


class CouponsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CouponsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CouponsInCondition = TypedDict("CouponsInCondition", {"in": CouponsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CouponsNotCondition = TypedDict("CouponsNotCondition", {"not": "CouponsCondition"}, total=False)
"""Negates the nested condition."""

CouponsAndCondition = TypedDict("CouponsAndCondition", {"and": "list[CouponsCondition]"}, total=False)
"""True if all nested conditions are true."""

CouponsOrCondition = TypedDict("CouponsOrCondition", {"or": "list[CouponsCondition]"}, total=False)
"""True if any nested condition is true."""

CouponsAnyCondition = TypedDict("CouponsAnyCondition", {"any": CouponsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all coupons condition types
CouponsCondition = (
    CouponsEqCondition
    | CouponsNeqCondition
    | CouponsGtCondition
    | CouponsGteCondition
    | CouponsLtCondition
    | CouponsLteCondition
    | CouponsInCondition
    | CouponsLikeCondition
    | CouponsFuzzyCondition
    | CouponsKeywordCondition
    | CouponsContainsCondition
    | CouponsNotCondition
    | CouponsAndCondition
    | CouponsOrCondition
    | CouponsAnyCondition
)


class CouponsSearchQuery(TypedDict, total=False):
    """Search query for coupons entity."""
    filter: CouponsCondition
    sort: list[CouponsSortFilter]


# ===== PRODUCT_CATEGORIES SEARCH TYPES =====

class ProductCategoriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering product_categories search queries."""
    count: int | None
    """Number of published products for the resource"""
    description: str | None
    """HTML description of the resource"""
    display: str | None
    """Category archive display type"""
    id: int | None
    """Unique identifier for the resource"""
    image: list[Any] | None
    """Image data"""
    menu_order: int | None
    """Menu order"""
    name: str | None
    """Category name"""
    parent: int | None
    """The ID for the parent of the resource"""
    slug: str | None
    """An alphanumeric identifier"""


class ProductCategoriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    count: list[int]
    """Number of published products for the resource"""
    description: list[str]
    """HTML description of the resource"""
    display: list[str]
    """Category archive display type"""
    id: list[int]
    """Unique identifier for the resource"""
    image: list[list[Any]]
    """Image data"""
    menu_order: list[int]
    """Menu order"""
    name: list[str]
    """Category name"""
    parent: list[int]
    """The ID for the parent of the resource"""
    slug: list[str]
    """An alphanumeric identifier"""


class ProductCategoriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    count: Any
    """Number of published products for the resource"""
    description: Any
    """HTML description of the resource"""
    display: Any
    """Category archive display type"""
    id: Any
    """Unique identifier for the resource"""
    image: Any
    """Image data"""
    menu_order: Any
    """Menu order"""
    name: Any
    """Category name"""
    parent: Any
    """The ID for the parent of the resource"""
    slug: Any
    """An alphanumeric identifier"""


class ProductCategoriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    count: str
    """Number of published products for the resource"""
    description: str
    """HTML description of the resource"""
    display: str
    """Category archive display type"""
    id: str
    """Unique identifier for the resource"""
    image: str
    """Image data"""
    menu_order: str
    """Menu order"""
    name: str
    """Category name"""
    parent: str
    """The ID for the parent of the resource"""
    slug: str
    """An alphanumeric identifier"""


class ProductCategoriesSortFilter(TypedDict, total=False):
    """Available fields for sorting product_categories search results."""
    count: AirbyteSortOrder
    """Number of published products for the resource"""
    description: AirbyteSortOrder
    """HTML description of the resource"""
    display: AirbyteSortOrder
    """Category archive display type"""
    id: AirbyteSortOrder
    """Unique identifier for the resource"""
    image: AirbyteSortOrder
    """Image data"""
    menu_order: AirbyteSortOrder
    """Menu order"""
    name: AirbyteSortOrder
    """Category name"""
    parent: AirbyteSortOrder
    """The ID for the parent of the resource"""
    slug: AirbyteSortOrder
    """An alphanumeric identifier"""


# Entity-specific condition types for product_categories
class ProductCategoriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProductCategoriesSearchFilter


class ProductCategoriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProductCategoriesSearchFilter


class ProductCategoriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProductCategoriesSearchFilter


class ProductCategoriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProductCategoriesSearchFilter


class ProductCategoriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProductCategoriesSearchFilter


class ProductCategoriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProductCategoriesSearchFilter


class ProductCategoriesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProductCategoriesStringFilter


class ProductCategoriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProductCategoriesStringFilter


class ProductCategoriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProductCategoriesStringFilter


class ProductCategoriesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProductCategoriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProductCategoriesInCondition = TypedDict("ProductCategoriesInCondition", {"in": ProductCategoriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProductCategoriesNotCondition = TypedDict("ProductCategoriesNotCondition", {"not": "ProductCategoriesCondition"}, total=False)
"""Negates the nested condition."""

ProductCategoriesAndCondition = TypedDict("ProductCategoriesAndCondition", {"and": "list[ProductCategoriesCondition]"}, total=False)
"""True if all nested conditions are true."""

ProductCategoriesOrCondition = TypedDict("ProductCategoriesOrCondition", {"or": "list[ProductCategoriesCondition]"}, total=False)
"""True if any nested condition is true."""

ProductCategoriesAnyCondition = TypedDict("ProductCategoriesAnyCondition", {"any": ProductCategoriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all product_categories condition types
ProductCategoriesCondition = (
    ProductCategoriesEqCondition
    | ProductCategoriesNeqCondition
    | ProductCategoriesGtCondition
    | ProductCategoriesGteCondition
    | ProductCategoriesLtCondition
    | ProductCategoriesLteCondition
    | ProductCategoriesInCondition
    | ProductCategoriesLikeCondition
    | ProductCategoriesFuzzyCondition
    | ProductCategoriesKeywordCondition
    | ProductCategoriesContainsCondition
    | ProductCategoriesNotCondition
    | ProductCategoriesAndCondition
    | ProductCategoriesOrCondition
    | ProductCategoriesAnyCondition
)


class ProductCategoriesSearchQuery(TypedDict, total=False):
    """Search query for product_categories entity."""
    filter: ProductCategoriesCondition
    sort: list[ProductCategoriesSortFilter]


# ===== PRODUCT_TAGS SEARCH TYPES =====

class ProductTagsSearchFilter(TypedDict, total=False):
    """Available fields for filtering product_tags search queries."""
    count: int | None
    """Number of published products"""
    description: str | None
    """HTML description"""
    id: int | None
    """Unique identifier"""
    name: str | None
    """Tag name"""
    slug: str | None
    """Alphanumeric identifier"""


class ProductTagsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    count: list[int]
    """Number of published products"""
    description: list[str]
    """HTML description"""
    id: list[int]
    """Unique identifier"""
    name: list[str]
    """Tag name"""
    slug: list[str]
    """Alphanumeric identifier"""


class ProductTagsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    count: Any
    """Number of published products"""
    description: Any
    """HTML description"""
    id: Any
    """Unique identifier"""
    name: Any
    """Tag name"""
    slug: Any
    """Alphanumeric identifier"""


class ProductTagsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    count: str
    """Number of published products"""
    description: str
    """HTML description"""
    id: str
    """Unique identifier"""
    name: str
    """Tag name"""
    slug: str
    """Alphanumeric identifier"""


class ProductTagsSortFilter(TypedDict, total=False):
    """Available fields for sorting product_tags search results."""
    count: AirbyteSortOrder
    """Number of published products"""
    description: AirbyteSortOrder
    """HTML description"""
    id: AirbyteSortOrder
    """Unique identifier"""
    name: AirbyteSortOrder
    """Tag name"""
    slug: AirbyteSortOrder
    """Alphanumeric identifier"""


# Entity-specific condition types for product_tags
class ProductTagsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProductTagsSearchFilter


class ProductTagsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProductTagsSearchFilter


class ProductTagsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProductTagsSearchFilter


class ProductTagsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProductTagsSearchFilter


class ProductTagsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProductTagsSearchFilter


class ProductTagsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProductTagsSearchFilter


class ProductTagsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProductTagsStringFilter


class ProductTagsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProductTagsStringFilter


class ProductTagsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProductTagsStringFilter


class ProductTagsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProductTagsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProductTagsInCondition = TypedDict("ProductTagsInCondition", {"in": ProductTagsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProductTagsNotCondition = TypedDict("ProductTagsNotCondition", {"not": "ProductTagsCondition"}, total=False)
"""Negates the nested condition."""

ProductTagsAndCondition = TypedDict("ProductTagsAndCondition", {"and": "list[ProductTagsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProductTagsOrCondition = TypedDict("ProductTagsOrCondition", {"or": "list[ProductTagsCondition]"}, total=False)
"""True if any nested condition is true."""

ProductTagsAnyCondition = TypedDict("ProductTagsAnyCondition", {"any": ProductTagsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all product_tags condition types
ProductTagsCondition = (
    ProductTagsEqCondition
    | ProductTagsNeqCondition
    | ProductTagsGtCondition
    | ProductTagsGteCondition
    | ProductTagsLtCondition
    | ProductTagsLteCondition
    | ProductTagsInCondition
    | ProductTagsLikeCondition
    | ProductTagsFuzzyCondition
    | ProductTagsKeywordCondition
    | ProductTagsContainsCondition
    | ProductTagsNotCondition
    | ProductTagsAndCondition
    | ProductTagsOrCondition
    | ProductTagsAnyCondition
)


class ProductTagsSearchQuery(TypedDict, total=False):
    """Search query for product_tags entity."""
    filter: ProductTagsCondition
    sort: list[ProductTagsSortFilter]


# ===== PRODUCT_REVIEWS SEARCH TYPES =====

class ProductReviewsSearchFilter(TypedDict, total=False):
    """Available fields for filtering product_reviews search queries."""
    date_created: str | None
    """The date the review was created"""
    date_created_gmt: str | None
    """The date the review was created, as GMT"""
    id: int | None
    """Unique identifier"""
    product_id: int | None
    """Product the review belongs to"""
    rating: int | None
    """Review rating (0 to 5)"""
    review: str | None
    """The content of the review"""
    reviewer: str | None
    """Reviewer name"""
    reviewer_email: str | None
    """Reviewer email"""
    status: str | None
    """Status of the review"""
    verified: bool | None
    """Shows if the reviewer bought the product"""


class ProductReviewsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    date_created: list[str]
    """The date the review was created"""
    date_created_gmt: list[str]
    """The date the review was created, as GMT"""
    id: list[int]
    """Unique identifier"""
    product_id: list[int]
    """Product the review belongs to"""
    rating: list[int]
    """Review rating (0 to 5)"""
    review: list[str]
    """The content of the review"""
    reviewer: list[str]
    """Reviewer name"""
    reviewer_email: list[str]
    """Reviewer email"""
    status: list[str]
    """Status of the review"""
    verified: list[bool]
    """Shows if the reviewer bought the product"""


class ProductReviewsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    date_created: Any
    """The date the review was created"""
    date_created_gmt: Any
    """The date the review was created, as GMT"""
    id: Any
    """Unique identifier"""
    product_id: Any
    """Product the review belongs to"""
    rating: Any
    """Review rating (0 to 5)"""
    review: Any
    """The content of the review"""
    reviewer: Any
    """Reviewer name"""
    reviewer_email: Any
    """Reviewer email"""
    status: Any
    """Status of the review"""
    verified: Any
    """Shows if the reviewer bought the product"""


class ProductReviewsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    date_created: str
    """The date the review was created"""
    date_created_gmt: str
    """The date the review was created, as GMT"""
    id: str
    """Unique identifier"""
    product_id: str
    """Product the review belongs to"""
    rating: str
    """Review rating (0 to 5)"""
    review: str
    """The content of the review"""
    reviewer: str
    """Reviewer name"""
    reviewer_email: str
    """Reviewer email"""
    status: str
    """Status of the review"""
    verified: str
    """Shows if the reviewer bought the product"""


class ProductReviewsSortFilter(TypedDict, total=False):
    """Available fields for sorting product_reviews search results."""
    date_created: AirbyteSortOrder
    """The date the review was created"""
    date_created_gmt: AirbyteSortOrder
    """The date the review was created, as GMT"""
    id: AirbyteSortOrder
    """Unique identifier"""
    product_id: AirbyteSortOrder
    """Product the review belongs to"""
    rating: AirbyteSortOrder
    """Review rating (0 to 5)"""
    review: AirbyteSortOrder
    """The content of the review"""
    reviewer: AirbyteSortOrder
    """Reviewer name"""
    reviewer_email: AirbyteSortOrder
    """Reviewer email"""
    status: AirbyteSortOrder
    """Status of the review"""
    verified: AirbyteSortOrder
    """Shows if the reviewer bought the product"""


# Entity-specific condition types for product_reviews
class ProductReviewsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProductReviewsSearchFilter


class ProductReviewsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProductReviewsSearchFilter


class ProductReviewsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProductReviewsSearchFilter


class ProductReviewsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProductReviewsSearchFilter


class ProductReviewsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProductReviewsSearchFilter


class ProductReviewsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProductReviewsSearchFilter


class ProductReviewsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProductReviewsStringFilter


class ProductReviewsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProductReviewsStringFilter


class ProductReviewsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProductReviewsStringFilter


class ProductReviewsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProductReviewsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProductReviewsInCondition = TypedDict("ProductReviewsInCondition", {"in": ProductReviewsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProductReviewsNotCondition = TypedDict("ProductReviewsNotCondition", {"not": "ProductReviewsCondition"}, total=False)
"""Negates the nested condition."""

ProductReviewsAndCondition = TypedDict("ProductReviewsAndCondition", {"and": "list[ProductReviewsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProductReviewsOrCondition = TypedDict("ProductReviewsOrCondition", {"or": "list[ProductReviewsCondition]"}, total=False)
"""True if any nested condition is true."""

ProductReviewsAnyCondition = TypedDict("ProductReviewsAnyCondition", {"any": ProductReviewsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all product_reviews condition types
ProductReviewsCondition = (
    ProductReviewsEqCondition
    | ProductReviewsNeqCondition
    | ProductReviewsGtCondition
    | ProductReviewsGteCondition
    | ProductReviewsLtCondition
    | ProductReviewsLteCondition
    | ProductReviewsInCondition
    | ProductReviewsLikeCondition
    | ProductReviewsFuzzyCondition
    | ProductReviewsKeywordCondition
    | ProductReviewsContainsCondition
    | ProductReviewsNotCondition
    | ProductReviewsAndCondition
    | ProductReviewsOrCondition
    | ProductReviewsAnyCondition
)


class ProductReviewsSearchQuery(TypedDict, total=False):
    """Search query for product_reviews entity."""
    filter: ProductReviewsCondition
    sort: list[ProductReviewsSortFilter]


# ===== PRODUCT_ATTRIBUTES SEARCH TYPES =====

class ProductAttributesSearchFilter(TypedDict, total=False):
    """Available fields for filtering product_attributes search queries."""
    has_archives: bool | None
    """Enable/Disable attribute archives"""
    id: int | None
    """Unique identifier"""
    name: str | None
    """Attribute name"""
    order_by: str | None
    """Default sort order"""
    slug: str | None
    """Alphanumeric identifier"""
    type_: str | None
    """Type of attribute"""


class ProductAttributesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    has_archives: list[bool]
    """Enable/Disable attribute archives"""
    id: list[int]
    """Unique identifier"""
    name: list[str]
    """Attribute name"""
    order_by: list[str]
    """Default sort order"""
    slug: list[str]
    """Alphanumeric identifier"""
    type_: list[str]
    """Type of attribute"""


class ProductAttributesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    has_archives: Any
    """Enable/Disable attribute archives"""
    id: Any
    """Unique identifier"""
    name: Any
    """Attribute name"""
    order_by: Any
    """Default sort order"""
    slug: Any
    """Alphanumeric identifier"""
    type_: Any
    """Type of attribute"""


class ProductAttributesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    has_archives: str
    """Enable/Disable attribute archives"""
    id: str
    """Unique identifier"""
    name: str
    """Attribute name"""
    order_by: str
    """Default sort order"""
    slug: str
    """Alphanumeric identifier"""
    type_: str
    """Type of attribute"""


class ProductAttributesSortFilter(TypedDict, total=False):
    """Available fields for sorting product_attributes search results."""
    has_archives: AirbyteSortOrder
    """Enable/Disable attribute archives"""
    id: AirbyteSortOrder
    """Unique identifier"""
    name: AirbyteSortOrder
    """Attribute name"""
    order_by: AirbyteSortOrder
    """Default sort order"""
    slug: AirbyteSortOrder
    """Alphanumeric identifier"""
    type_: AirbyteSortOrder
    """Type of attribute"""


# Entity-specific condition types for product_attributes
class ProductAttributesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProductAttributesSearchFilter


class ProductAttributesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProductAttributesSearchFilter


class ProductAttributesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProductAttributesSearchFilter


class ProductAttributesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProductAttributesSearchFilter


class ProductAttributesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProductAttributesSearchFilter


class ProductAttributesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProductAttributesSearchFilter


class ProductAttributesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProductAttributesStringFilter


class ProductAttributesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProductAttributesStringFilter


class ProductAttributesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProductAttributesStringFilter


class ProductAttributesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProductAttributesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProductAttributesInCondition = TypedDict("ProductAttributesInCondition", {"in": ProductAttributesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProductAttributesNotCondition = TypedDict("ProductAttributesNotCondition", {"not": "ProductAttributesCondition"}, total=False)
"""Negates the nested condition."""

ProductAttributesAndCondition = TypedDict("ProductAttributesAndCondition", {"and": "list[ProductAttributesCondition]"}, total=False)
"""True if all nested conditions are true."""

ProductAttributesOrCondition = TypedDict("ProductAttributesOrCondition", {"or": "list[ProductAttributesCondition]"}, total=False)
"""True if any nested condition is true."""

ProductAttributesAnyCondition = TypedDict("ProductAttributesAnyCondition", {"any": ProductAttributesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all product_attributes condition types
ProductAttributesCondition = (
    ProductAttributesEqCondition
    | ProductAttributesNeqCondition
    | ProductAttributesGtCondition
    | ProductAttributesGteCondition
    | ProductAttributesLtCondition
    | ProductAttributesLteCondition
    | ProductAttributesInCondition
    | ProductAttributesLikeCondition
    | ProductAttributesFuzzyCondition
    | ProductAttributesKeywordCondition
    | ProductAttributesContainsCondition
    | ProductAttributesNotCondition
    | ProductAttributesAndCondition
    | ProductAttributesOrCondition
    | ProductAttributesAnyCondition
)


class ProductAttributesSearchQuery(TypedDict, total=False):
    """Search query for product_attributes entity."""
    filter: ProductAttributesCondition
    sort: list[ProductAttributesSortFilter]


# ===== PRODUCT_VARIATIONS SEARCH TYPES =====

class ProductVariationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering product_variations search queries."""
    attributes: list[Any] | None
    """List of attributes"""
    backordered: bool | None
    """On backordered"""
    backorders: str | None
    """Backorders allowed setting"""
    backorders_allowed: bool | None
    """Shows if backorders are allowed"""
    date_created: str | None
    """The date the variation was created"""
    date_created_gmt: str | None
    """The date the variation was created, as GMT"""
    date_modified: str | None
    """The date the variation was last modified"""
    date_modified_gmt: str | None
    """The date the variation was last modified, as GMT"""
    date_on_sale_from: str | None
    """Start date of sale price"""
    date_on_sale_from_gmt: str | None
    """Start date of sale price, as GMT"""
    date_on_sale_to: str | None
    """End date of sale price"""
    date_on_sale_to_gmt: str | None
    """End date of sale price, as GMT"""
    description: str | None
    """Variation description"""
    dimensions: dict[str, Any] | None
    """Variation dimensions"""
    download_expiry: int | None
    """Days until access expires"""
    download_limit: int | None
    """Download limit"""
    downloadable: bool | None
    """If downloadable"""
    downloads: list[Any] | None
    """Downloadable files"""
    id: int | None
    """Unique identifier"""
    image: list[Any] | None
    """Variation image data"""
    manage_stock: str | None
    """Stock management at variation level"""
    menu_order: int | None
    """Menu order"""
    meta_data: list[Any] | None
    """Meta data"""
    on_sale: bool | None
    """Shows if on sale"""
    permalink: str | None
    """Variation URL"""
    price: str | None
    """Current variation price"""
    purchasable: bool | None
    """Can be bought"""
    regular_price: str | None
    """Variation regular price"""
    sale_price: str | None
    """Variation sale price"""
    shipping_class: str | None
    """Shipping class slug"""
    shipping_class_id: int | None
    """Shipping class ID"""
    sku: str | None
    """Unique identifier (SKU)"""
    status: str | None
    """Variation status"""
    stock_quantity: int | None
    """Stock quantity"""
    stock_status: str | None
    """Controls the stock status"""
    tax_class: str | None
    """Tax class"""
    tax_status: str | None
    """Tax status"""
    virtual: bool | None
    """If virtual"""
    weight: str | None
    """Variation weight"""


class ProductVariationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attributes: list[list[Any]]
    """List of attributes"""
    backordered: list[bool]
    """On backordered"""
    backorders: list[str]
    """Backorders allowed setting"""
    backorders_allowed: list[bool]
    """Shows if backorders are allowed"""
    date_created: list[str]
    """The date the variation was created"""
    date_created_gmt: list[str]
    """The date the variation was created, as GMT"""
    date_modified: list[str]
    """The date the variation was last modified"""
    date_modified_gmt: list[str]
    """The date the variation was last modified, as GMT"""
    date_on_sale_from: list[str]
    """Start date of sale price"""
    date_on_sale_from_gmt: list[str]
    """Start date of sale price, as GMT"""
    date_on_sale_to: list[str]
    """End date of sale price"""
    date_on_sale_to_gmt: list[str]
    """End date of sale price, as GMT"""
    description: list[str]
    """Variation description"""
    dimensions: list[dict[str, Any]]
    """Variation dimensions"""
    download_expiry: list[int]
    """Days until access expires"""
    download_limit: list[int]
    """Download limit"""
    downloadable: list[bool]
    """If downloadable"""
    downloads: list[list[Any]]
    """Downloadable files"""
    id: list[int]
    """Unique identifier"""
    image: list[list[Any]]
    """Variation image data"""
    manage_stock: list[str]
    """Stock management at variation level"""
    menu_order: list[int]
    """Menu order"""
    meta_data: list[list[Any]]
    """Meta data"""
    on_sale: list[bool]
    """Shows if on sale"""
    permalink: list[str]
    """Variation URL"""
    price: list[str]
    """Current variation price"""
    purchasable: list[bool]
    """Can be bought"""
    regular_price: list[str]
    """Variation regular price"""
    sale_price: list[str]
    """Variation sale price"""
    shipping_class: list[str]
    """Shipping class slug"""
    shipping_class_id: list[int]
    """Shipping class ID"""
    sku: list[str]
    """Unique identifier (SKU)"""
    status: list[str]
    """Variation status"""
    stock_quantity: list[int]
    """Stock quantity"""
    stock_status: list[str]
    """Controls the stock status"""
    tax_class: list[str]
    """Tax class"""
    tax_status: list[str]
    """Tax status"""
    virtual: list[bool]
    """If virtual"""
    weight: list[str]
    """Variation weight"""


class ProductVariationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attributes: Any
    """List of attributes"""
    backordered: Any
    """On backordered"""
    backorders: Any
    """Backorders allowed setting"""
    backorders_allowed: Any
    """Shows if backorders are allowed"""
    date_created: Any
    """The date the variation was created"""
    date_created_gmt: Any
    """The date the variation was created, as GMT"""
    date_modified: Any
    """The date the variation was last modified"""
    date_modified_gmt: Any
    """The date the variation was last modified, as GMT"""
    date_on_sale_from: Any
    """Start date of sale price"""
    date_on_sale_from_gmt: Any
    """Start date of sale price, as GMT"""
    date_on_sale_to: Any
    """End date of sale price"""
    date_on_sale_to_gmt: Any
    """End date of sale price, as GMT"""
    description: Any
    """Variation description"""
    dimensions: Any
    """Variation dimensions"""
    download_expiry: Any
    """Days until access expires"""
    download_limit: Any
    """Download limit"""
    downloadable: Any
    """If downloadable"""
    downloads: Any
    """Downloadable files"""
    id: Any
    """Unique identifier"""
    image: Any
    """Variation image data"""
    manage_stock: Any
    """Stock management at variation level"""
    menu_order: Any
    """Menu order"""
    meta_data: Any
    """Meta data"""
    on_sale: Any
    """Shows if on sale"""
    permalink: Any
    """Variation URL"""
    price: Any
    """Current variation price"""
    purchasable: Any
    """Can be bought"""
    regular_price: Any
    """Variation regular price"""
    sale_price: Any
    """Variation sale price"""
    shipping_class: Any
    """Shipping class slug"""
    shipping_class_id: Any
    """Shipping class ID"""
    sku: Any
    """Unique identifier (SKU)"""
    status: Any
    """Variation status"""
    stock_quantity: Any
    """Stock quantity"""
    stock_status: Any
    """Controls the stock status"""
    tax_class: Any
    """Tax class"""
    tax_status: Any
    """Tax status"""
    virtual: Any
    """If virtual"""
    weight: Any
    """Variation weight"""


class ProductVariationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    attributes: str
    """List of attributes"""
    backordered: str
    """On backordered"""
    backorders: str
    """Backorders allowed setting"""
    backorders_allowed: str
    """Shows if backorders are allowed"""
    date_created: str
    """The date the variation was created"""
    date_created_gmt: str
    """The date the variation was created, as GMT"""
    date_modified: str
    """The date the variation was last modified"""
    date_modified_gmt: str
    """The date the variation was last modified, as GMT"""
    date_on_sale_from: str
    """Start date of sale price"""
    date_on_sale_from_gmt: str
    """Start date of sale price, as GMT"""
    date_on_sale_to: str
    """End date of sale price"""
    date_on_sale_to_gmt: str
    """End date of sale price, as GMT"""
    description: str
    """Variation description"""
    dimensions: str
    """Variation dimensions"""
    download_expiry: str
    """Days until access expires"""
    download_limit: str
    """Download limit"""
    downloadable: str
    """If downloadable"""
    downloads: str
    """Downloadable files"""
    id: str
    """Unique identifier"""
    image: str
    """Variation image data"""
    manage_stock: str
    """Stock management at variation level"""
    menu_order: str
    """Menu order"""
    meta_data: str
    """Meta data"""
    on_sale: str
    """Shows if on sale"""
    permalink: str
    """Variation URL"""
    price: str
    """Current variation price"""
    purchasable: str
    """Can be bought"""
    regular_price: str
    """Variation regular price"""
    sale_price: str
    """Variation sale price"""
    shipping_class: str
    """Shipping class slug"""
    shipping_class_id: str
    """Shipping class ID"""
    sku: str
    """Unique identifier (SKU)"""
    status: str
    """Variation status"""
    stock_quantity: str
    """Stock quantity"""
    stock_status: str
    """Controls the stock status"""
    tax_class: str
    """Tax class"""
    tax_status: str
    """Tax status"""
    virtual: str
    """If virtual"""
    weight: str
    """Variation weight"""


class ProductVariationsSortFilter(TypedDict, total=False):
    """Available fields for sorting product_variations search results."""
    attributes: AirbyteSortOrder
    """List of attributes"""
    backordered: AirbyteSortOrder
    """On backordered"""
    backorders: AirbyteSortOrder
    """Backorders allowed setting"""
    backorders_allowed: AirbyteSortOrder
    """Shows if backorders are allowed"""
    date_created: AirbyteSortOrder
    """The date the variation was created"""
    date_created_gmt: AirbyteSortOrder
    """The date the variation was created, as GMT"""
    date_modified: AirbyteSortOrder
    """The date the variation was last modified"""
    date_modified_gmt: AirbyteSortOrder
    """The date the variation was last modified, as GMT"""
    date_on_sale_from: AirbyteSortOrder
    """Start date of sale price"""
    date_on_sale_from_gmt: AirbyteSortOrder
    """Start date of sale price, as GMT"""
    date_on_sale_to: AirbyteSortOrder
    """End date of sale price"""
    date_on_sale_to_gmt: AirbyteSortOrder
    """End date of sale price, as GMT"""
    description: AirbyteSortOrder
    """Variation description"""
    dimensions: AirbyteSortOrder
    """Variation dimensions"""
    download_expiry: AirbyteSortOrder
    """Days until access expires"""
    download_limit: AirbyteSortOrder
    """Download limit"""
    downloadable: AirbyteSortOrder
    """If downloadable"""
    downloads: AirbyteSortOrder
    """Downloadable files"""
    id: AirbyteSortOrder
    """Unique identifier"""
    image: AirbyteSortOrder
    """Variation image data"""
    manage_stock: AirbyteSortOrder
    """Stock management at variation level"""
    menu_order: AirbyteSortOrder
    """Menu order"""
    meta_data: AirbyteSortOrder
    """Meta data"""
    on_sale: AirbyteSortOrder
    """Shows if on sale"""
    permalink: AirbyteSortOrder
    """Variation URL"""
    price: AirbyteSortOrder
    """Current variation price"""
    purchasable: AirbyteSortOrder
    """Can be bought"""
    regular_price: AirbyteSortOrder
    """Variation regular price"""
    sale_price: AirbyteSortOrder
    """Variation sale price"""
    shipping_class: AirbyteSortOrder
    """Shipping class slug"""
    shipping_class_id: AirbyteSortOrder
    """Shipping class ID"""
    sku: AirbyteSortOrder
    """Unique identifier (SKU)"""
    status: AirbyteSortOrder
    """Variation status"""
    stock_quantity: AirbyteSortOrder
    """Stock quantity"""
    stock_status: AirbyteSortOrder
    """Controls the stock status"""
    tax_class: AirbyteSortOrder
    """Tax class"""
    tax_status: AirbyteSortOrder
    """Tax status"""
    virtual: AirbyteSortOrder
    """If virtual"""
    weight: AirbyteSortOrder
    """Variation weight"""


# Entity-specific condition types for product_variations
class ProductVariationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProductVariationsSearchFilter


class ProductVariationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProductVariationsSearchFilter


class ProductVariationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProductVariationsSearchFilter


class ProductVariationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProductVariationsSearchFilter


class ProductVariationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProductVariationsSearchFilter


class ProductVariationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProductVariationsSearchFilter


class ProductVariationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProductVariationsStringFilter


class ProductVariationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProductVariationsStringFilter


class ProductVariationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProductVariationsStringFilter


class ProductVariationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProductVariationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProductVariationsInCondition = TypedDict("ProductVariationsInCondition", {"in": ProductVariationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProductVariationsNotCondition = TypedDict("ProductVariationsNotCondition", {"not": "ProductVariationsCondition"}, total=False)
"""Negates the nested condition."""

ProductVariationsAndCondition = TypedDict("ProductVariationsAndCondition", {"and": "list[ProductVariationsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProductVariationsOrCondition = TypedDict("ProductVariationsOrCondition", {"or": "list[ProductVariationsCondition]"}, total=False)
"""True if any nested condition is true."""

ProductVariationsAnyCondition = TypedDict("ProductVariationsAnyCondition", {"any": ProductVariationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all product_variations condition types
ProductVariationsCondition = (
    ProductVariationsEqCondition
    | ProductVariationsNeqCondition
    | ProductVariationsGtCondition
    | ProductVariationsGteCondition
    | ProductVariationsLtCondition
    | ProductVariationsLteCondition
    | ProductVariationsInCondition
    | ProductVariationsLikeCondition
    | ProductVariationsFuzzyCondition
    | ProductVariationsKeywordCondition
    | ProductVariationsContainsCondition
    | ProductVariationsNotCondition
    | ProductVariationsAndCondition
    | ProductVariationsOrCondition
    | ProductVariationsAnyCondition
)


class ProductVariationsSearchQuery(TypedDict, total=False):
    """Search query for product_variations entity."""
    filter: ProductVariationsCondition
    sort: list[ProductVariationsSortFilter]


# ===== ORDER_NOTES SEARCH TYPES =====

class OrderNotesSearchFilter(TypedDict, total=False):
    """Available fields for filtering order_notes search queries."""
    author: str | None
    """Order note author"""
    date_created: str | None
    """The date the order note was created"""
    date_created_gmt: str | None
    """The date the order note was created, as GMT"""
    id: int | None
    """Unique identifier"""
    note: str | None
    """Order note content"""


class OrderNotesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    author: list[str]
    """Order note author"""
    date_created: list[str]
    """The date the order note was created"""
    date_created_gmt: list[str]
    """The date the order note was created, as GMT"""
    id: list[int]
    """Unique identifier"""
    note: list[str]
    """Order note content"""


class OrderNotesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    author: Any
    """Order note author"""
    date_created: Any
    """The date the order note was created"""
    date_created_gmt: Any
    """The date the order note was created, as GMT"""
    id: Any
    """Unique identifier"""
    note: Any
    """Order note content"""


class OrderNotesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    author: str
    """Order note author"""
    date_created: str
    """The date the order note was created"""
    date_created_gmt: str
    """The date the order note was created, as GMT"""
    id: str
    """Unique identifier"""
    note: str
    """Order note content"""


class OrderNotesSortFilter(TypedDict, total=False):
    """Available fields for sorting order_notes search results."""
    author: AirbyteSortOrder
    """Order note author"""
    date_created: AirbyteSortOrder
    """The date the order note was created"""
    date_created_gmt: AirbyteSortOrder
    """The date the order note was created, as GMT"""
    id: AirbyteSortOrder
    """Unique identifier"""
    note: AirbyteSortOrder
    """Order note content"""


# Entity-specific condition types for order_notes
class OrderNotesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OrderNotesSearchFilter


class OrderNotesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OrderNotesSearchFilter


class OrderNotesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OrderNotesSearchFilter


class OrderNotesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OrderNotesSearchFilter


class OrderNotesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OrderNotesSearchFilter


class OrderNotesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OrderNotesSearchFilter


class OrderNotesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OrderNotesStringFilter


class OrderNotesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OrderNotesStringFilter


class OrderNotesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OrderNotesStringFilter


class OrderNotesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OrderNotesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OrderNotesInCondition = TypedDict("OrderNotesInCondition", {"in": OrderNotesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OrderNotesNotCondition = TypedDict("OrderNotesNotCondition", {"not": "OrderNotesCondition"}, total=False)
"""Negates the nested condition."""

OrderNotesAndCondition = TypedDict("OrderNotesAndCondition", {"and": "list[OrderNotesCondition]"}, total=False)
"""True if all nested conditions are true."""

OrderNotesOrCondition = TypedDict("OrderNotesOrCondition", {"or": "list[OrderNotesCondition]"}, total=False)
"""True if any nested condition is true."""

OrderNotesAnyCondition = TypedDict("OrderNotesAnyCondition", {"any": OrderNotesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all order_notes condition types
OrderNotesCondition = (
    OrderNotesEqCondition
    | OrderNotesNeqCondition
    | OrderNotesGtCondition
    | OrderNotesGteCondition
    | OrderNotesLtCondition
    | OrderNotesLteCondition
    | OrderNotesInCondition
    | OrderNotesLikeCondition
    | OrderNotesFuzzyCondition
    | OrderNotesKeywordCondition
    | OrderNotesContainsCondition
    | OrderNotesNotCondition
    | OrderNotesAndCondition
    | OrderNotesOrCondition
    | OrderNotesAnyCondition
)


class OrderNotesSearchQuery(TypedDict, total=False):
    """Search query for order_notes entity."""
    filter: OrderNotesCondition
    sort: list[OrderNotesSortFilter]


# ===== REFUNDS SEARCH TYPES =====

class RefundsSearchFilter(TypedDict, total=False):
    """Available fields for filtering refunds search queries."""
    amount: str | None
    """Refund amount"""
    date_created: str | None
    """The date the refund was created"""
    date_created_gmt: str | None
    """The date the refund was created, as GMT"""
    id: int | None
    """Unique identifier"""
    line_items: list[Any] | None
    """Line items data"""
    meta_data: list[Any] | None
    """Meta data"""
    reason: str | None
    """Reason for refund"""
    refunded_by: int | None
    """User ID of user who created the refund"""
    refunded_payment: bool | None
    """If the payment was refunded via the API"""


class RefundsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    amount: list[str]
    """Refund amount"""
    date_created: list[str]
    """The date the refund was created"""
    date_created_gmt: list[str]
    """The date the refund was created, as GMT"""
    id: list[int]
    """Unique identifier"""
    line_items: list[list[Any]]
    """Line items data"""
    meta_data: list[list[Any]]
    """Meta data"""
    reason: list[str]
    """Reason for refund"""
    refunded_by: list[int]
    """User ID of user who created the refund"""
    refunded_payment: list[bool]
    """If the payment was refunded via the API"""


class RefundsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    amount: Any
    """Refund amount"""
    date_created: Any
    """The date the refund was created"""
    date_created_gmt: Any
    """The date the refund was created, as GMT"""
    id: Any
    """Unique identifier"""
    line_items: Any
    """Line items data"""
    meta_data: Any
    """Meta data"""
    reason: Any
    """Reason for refund"""
    refunded_by: Any
    """User ID of user who created the refund"""
    refunded_payment: Any
    """If the payment was refunded via the API"""


class RefundsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    amount: str
    """Refund amount"""
    date_created: str
    """The date the refund was created"""
    date_created_gmt: str
    """The date the refund was created, as GMT"""
    id: str
    """Unique identifier"""
    line_items: str
    """Line items data"""
    meta_data: str
    """Meta data"""
    reason: str
    """Reason for refund"""
    refunded_by: str
    """User ID of user who created the refund"""
    refunded_payment: str
    """If the payment was refunded via the API"""


class RefundsSortFilter(TypedDict, total=False):
    """Available fields for sorting refunds search results."""
    amount: AirbyteSortOrder
    """Refund amount"""
    date_created: AirbyteSortOrder
    """The date the refund was created"""
    date_created_gmt: AirbyteSortOrder
    """The date the refund was created, as GMT"""
    id: AirbyteSortOrder
    """Unique identifier"""
    line_items: AirbyteSortOrder
    """Line items data"""
    meta_data: AirbyteSortOrder
    """Meta data"""
    reason: AirbyteSortOrder
    """Reason for refund"""
    refunded_by: AirbyteSortOrder
    """User ID of user who created the refund"""
    refunded_payment: AirbyteSortOrder
    """If the payment was refunded via the API"""


# Entity-specific condition types for refunds
class RefundsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: RefundsSearchFilter


class RefundsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: RefundsSearchFilter


class RefundsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: RefundsSearchFilter


class RefundsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: RefundsSearchFilter


class RefundsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: RefundsSearchFilter


class RefundsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: RefundsSearchFilter


class RefundsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: RefundsStringFilter


class RefundsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: RefundsStringFilter


class RefundsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: RefundsStringFilter


class RefundsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: RefundsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
RefundsInCondition = TypedDict("RefundsInCondition", {"in": RefundsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

RefundsNotCondition = TypedDict("RefundsNotCondition", {"not": "RefundsCondition"}, total=False)
"""Negates the nested condition."""

RefundsAndCondition = TypedDict("RefundsAndCondition", {"and": "list[RefundsCondition]"}, total=False)
"""True if all nested conditions are true."""

RefundsOrCondition = TypedDict("RefundsOrCondition", {"or": "list[RefundsCondition]"}, total=False)
"""True if any nested condition is true."""

RefundsAnyCondition = TypedDict("RefundsAnyCondition", {"any": RefundsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all refunds condition types
RefundsCondition = (
    RefundsEqCondition
    | RefundsNeqCondition
    | RefundsGtCondition
    | RefundsGteCondition
    | RefundsLtCondition
    | RefundsLteCondition
    | RefundsInCondition
    | RefundsLikeCondition
    | RefundsFuzzyCondition
    | RefundsKeywordCondition
    | RefundsContainsCondition
    | RefundsNotCondition
    | RefundsAndCondition
    | RefundsOrCondition
    | RefundsAnyCondition
)


class RefundsSearchQuery(TypedDict, total=False):
    """Search query for refunds entity."""
    filter: RefundsCondition
    sort: list[RefundsSortFilter]


# ===== PAYMENT_GATEWAYS SEARCH TYPES =====

class PaymentGatewaysSearchFilter(TypedDict, total=False):
    """Available fields for filtering payment_gateways search queries."""
    description: str | None
    """Payment gateway description on checkout"""
    enabled: bool | None
    """Payment gateway enabled status"""
    id: str | None
    """Payment gateway ID"""
    method_description: str | None
    """Payment gateway method description"""
    method_supports: list[Any] | None
    """Supported features"""
    method_title: str | None
    """Payment gateway method title"""
    order: Any
    """Payment gateway sort order"""
    settings: dict[str, Any] | None
    """Payment gateway settings"""
    title: str | None
    """Payment gateway title on checkout"""


class PaymentGatewaysInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    description: list[str]
    """Payment gateway description on checkout"""
    enabled: list[bool]
    """Payment gateway enabled status"""
    id: list[str]
    """Payment gateway ID"""
    method_description: list[str]
    """Payment gateway method description"""
    method_supports: list[list[Any]]
    """Supported features"""
    method_title: list[str]
    """Payment gateway method title"""
    order: list[Any]
    """Payment gateway sort order"""
    settings: list[dict[str, Any]]
    """Payment gateway settings"""
    title: list[str]
    """Payment gateway title on checkout"""


class PaymentGatewaysAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    description: Any
    """Payment gateway description on checkout"""
    enabled: Any
    """Payment gateway enabled status"""
    id: Any
    """Payment gateway ID"""
    method_description: Any
    """Payment gateway method description"""
    method_supports: Any
    """Supported features"""
    method_title: Any
    """Payment gateway method title"""
    order: Any
    """Payment gateway sort order"""
    settings: Any
    """Payment gateway settings"""
    title: Any
    """Payment gateway title on checkout"""


class PaymentGatewaysStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    description: str
    """Payment gateway description on checkout"""
    enabled: str
    """Payment gateway enabled status"""
    id: str
    """Payment gateway ID"""
    method_description: str
    """Payment gateway method description"""
    method_supports: str
    """Supported features"""
    method_title: str
    """Payment gateway method title"""
    order: str
    """Payment gateway sort order"""
    settings: str
    """Payment gateway settings"""
    title: str
    """Payment gateway title on checkout"""


class PaymentGatewaysSortFilter(TypedDict, total=False):
    """Available fields for sorting payment_gateways search results."""
    description: AirbyteSortOrder
    """Payment gateway description on checkout"""
    enabled: AirbyteSortOrder
    """Payment gateway enabled status"""
    id: AirbyteSortOrder
    """Payment gateway ID"""
    method_description: AirbyteSortOrder
    """Payment gateway method description"""
    method_supports: AirbyteSortOrder
    """Supported features"""
    method_title: AirbyteSortOrder
    """Payment gateway method title"""
    order: AirbyteSortOrder
    """Payment gateway sort order"""
    settings: AirbyteSortOrder
    """Payment gateway settings"""
    title: AirbyteSortOrder
    """Payment gateway title on checkout"""


# Entity-specific condition types for payment_gateways
class PaymentGatewaysEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PaymentGatewaysSearchFilter


class PaymentGatewaysNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PaymentGatewaysSearchFilter


class PaymentGatewaysGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PaymentGatewaysSearchFilter


class PaymentGatewaysGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PaymentGatewaysSearchFilter


class PaymentGatewaysLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PaymentGatewaysSearchFilter


class PaymentGatewaysLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PaymentGatewaysSearchFilter


class PaymentGatewaysLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PaymentGatewaysStringFilter


class PaymentGatewaysFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PaymentGatewaysStringFilter


class PaymentGatewaysKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PaymentGatewaysStringFilter


class PaymentGatewaysContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PaymentGatewaysAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PaymentGatewaysInCondition = TypedDict("PaymentGatewaysInCondition", {"in": PaymentGatewaysInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PaymentGatewaysNotCondition = TypedDict("PaymentGatewaysNotCondition", {"not": "PaymentGatewaysCondition"}, total=False)
"""Negates the nested condition."""

PaymentGatewaysAndCondition = TypedDict("PaymentGatewaysAndCondition", {"and": "list[PaymentGatewaysCondition]"}, total=False)
"""True if all nested conditions are true."""

PaymentGatewaysOrCondition = TypedDict("PaymentGatewaysOrCondition", {"or": "list[PaymentGatewaysCondition]"}, total=False)
"""True if any nested condition is true."""

PaymentGatewaysAnyCondition = TypedDict("PaymentGatewaysAnyCondition", {"any": PaymentGatewaysAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all payment_gateways condition types
PaymentGatewaysCondition = (
    PaymentGatewaysEqCondition
    | PaymentGatewaysNeqCondition
    | PaymentGatewaysGtCondition
    | PaymentGatewaysGteCondition
    | PaymentGatewaysLtCondition
    | PaymentGatewaysLteCondition
    | PaymentGatewaysInCondition
    | PaymentGatewaysLikeCondition
    | PaymentGatewaysFuzzyCondition
    | PaymentGatewaysKeywordCondition
    | PaymentGatewaysContainsCondition
    | PaymentGatewaysNotCondition
    | PaymentGatewaysAndCondition
    | PaymentGatewaysOrCondition
    | PaymentGatewaysAnyCondition
)


class PaymentGatewaysSearchQuery(TypedDict, total=False):
    """Search query for payment_gateways entity."""
    filter: PaymentGatewaysCondition
    sort: list[PaymentGatewaysSortFilter]


# ===== SHIPPING_METHODS SEARCH TYPES =====

class ShippingMethodsSearchFilter(TypedDict, total=False):
    """Available fields for filtering shipping_methods search queries."""
    description: str | None
    """Shipping method description"""
    id: str | None
    """Method ID"""
    title: str | None
    """Shipping method title"""


class ShippingMethodsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    description: list[str]
    """Shipping method description"""
    id: list[str]
    """Method ID"""
    title: list[str]
    """Shipping method title"""


class ShippingMethodsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    description: Any
    """Shipping method description"""
    id: Any
    """Method ID"""
    title: Any
    """Shipping method title"""


class ShippingMethodsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    description: str
    """Shipping method description"""
    id: str
    """Method ID"""
    title: str
    """Shipping method title"""


class ShippingMethodsSortFilter(TypedDict, total=False):
    """Available fields for sorting shipping_methods search results."""
    description: AirbyteSortOrder
    """Shipping method description"""
    id: AirbyteSortOrder
    """Method ID"""
    title: AirbyteSortOrder
    """Shipping method title"""


# Entity-specific condition types for shipping_methods
class ShippingMethodsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ShippingMethodsSearchFilter


class ShippingMethodsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ShippingMethodsSearchFilter


class ShippingMethodsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ShippingMethodsSearchFilter


class ShippingMethodsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ShippingMethodsSearchFilter


class ShippingMethodsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ShippingMethodsSearchFilter


class ShippingMethodsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ShippingMethodsSearchFilter


class ShippingMethodsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ShippingMethodsStringFilter


class ShippingMethodsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ShippingMethodsStringFilter


class ShippingMethodsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ShippingMethodsStringFilter


class ShippingMethodsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ShippingMethodsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ShippingMethodsInCondition = TypedDict("ShippingMethodsInCondition", {"in": ShippingMethodsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ShippingMethodsNotCondition = TypedDict("ShippingMethodsNotCondition", {"not": "ShippingMethodsCondition"}, total=False)
"""Negates the nested condition."""

ShippingMethodsAndCondition = TypedDict("ShippingMethodsAndCondition", {"and": "list[ShippingMethodsCondition]"}, total=False)
"""True if all nested conditions are true."""

ShippingMethodsOrCondition = TypedDict("ShippingMethodsOrCondition", {"or": "list[ShippingMethodsCondition]"}, total=False)
"""True if any nested condition is true."""

ShippingMethodsAnyCondition = TypedDict("ShippingMethodsAnyCondition", {"any": ShippingMethodsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all shipping_methods condition types
ShippingMethodsCondition = (
    ShippingMethodsEqCondition
    | ShippingMethodsNeqCondition
    | ShippingMethodsGtCondition
    | ShippingMethodsGteCondition
    | ShippingMethodsLtCondition
    | ShippingMethodsLteCondition
    | ShippingMethodsInCondition
    | ShippingMethodsLikeCondition
    | ShippingMethodsFuzzyCondition
    | ShippingMethodsKeywordCondition
    | ShippingMethodsContainsCondition
    | ShippingMethodsNotCondition
    | ShippingMethodsAndCondition
    | ShippingMethodsOrCondition
    | ShippingMethodsAnyCondition
)


class ShippingMethodsSearchQuery(TypedDict, total=False):
    """Search query for shipping_methods entity."""
    filter: ShippingMethodsCondition
    sort: list[ShippingMethodsSortFilter]


# ===== SHIPPING_ZONES SEARCH TYPES =====

class ShippingZonesSearchFilter(TypedDict, total=False):
    """Available fields for filtering shipping_zones search queries."""
    id: int | None
    """Unique identifier"""
    name: str | None
    """Shipping zone name"""
    order: int | None
    """Shipping zone order"""


class ShippingZonesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier"""
    name: list[str]
    """Shipping zone name"""
    order: list[int]
    """Shipping zone order"""


class ShippingZonesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier"""
    name: Any
    """Shipping zone name"""
    order: Any
    """Shipping zone order"""


class ShippingZonesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier"""
    name: str
    """Shipping zone name"""
    order: str
    """Shipping zone order"""


class ShippingZonesSortFilter(TypedDict, total=False):
    """Available fields for sorting shipping_zones search results."""
    id: AirbyteSortOrder
    """Unique identifier"""
    name: AirbyteSortOrder
    """Shipping zone name"""
    order: AirbyteSortOrder
    """Shipping zone order"""


# Entity-specific condition types for shipping_zones
class ShippingZonesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ShippingZonesSearchFilter


class ShippingZonesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ShippingZonesSearchFilter


class ShippingZonesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ShippingZonesSearchFilter


class ShippingZonesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ShippingZonesSearchFilter


class ShippingZonesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ShippingZonesSearchFilter


class ShippingZonesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ShippingZonesSearchFilter


class ShippingZonesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ShippingZonesStringFilter


class ShippingZonesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ShippingZonesStringFilter


class ShippingZonesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ShippingZonesStringFilter


class ShippingZonesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ShippingZonesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ShippingZonesInCondition = TypedDict("ShippingZonesInCondition", {"in": ShippingZonesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ShippingZonesNotCondition = TypedDict("ShippingZonesNotCondition", {"not": "ShippingZonesCondition"}, total=False)
"""Negates the nested condition."""

ShippingZonesAndCondition = TypedDict("ShippingZonesAndCondition", {"and": "list[ShippingZonesCondition]"}, total=False)
"""True if all nested conditions are true."""

ShippingZonesOrCondition = TypedDict("ShippingZonesOrCondition", {"or": "list[ShippingZonesCondition]"}, total=False)
"""True if any nested condition is true."""

ShippingZonesAnyCondition = TypedDict("ShippingZonesAnyCondition", {"any": ShippingZonesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all shipping_zones condition types
ShippingZonesCondition = (
    ShippingZonesEqCondition
    | ShippingZonesNeqCondition
    | ShippingZonesGtCondition
    | ShippingZonesGteCondition
    | ShippingZonesLtCondition
    | ShippingZonesLteCondition
    | ShippingZonesInCondition
    | ShippingZonesLikeCondition
    | ShippingZonesFuzzyCondition
    | ShippingZonesKeywordCondition
    | ShippingZonesContainsCondition
    | ShippingZonesNotCondition
    | ShippingZonesAndCondition
    | ShippingZonesOrCondition
    | ShippingZonesAnyCondition
)


class ShippingZonesSearchQuery(TypedDict, total=False):
    """Search query for shipping_zones entity."""
    filter: ShippingZonesCondition
    sort: list[ShippingZonesSortFilter]


# ===== TAX_RATES SEARCH TYPES =====

class TaxRatesSearchFilter(TypedDict, total=False):
    """Available fields for filtering tax_rates search queries."""
    cities: list[Any] | None
    """City names"""
    city: str | None
    """City name"""
    class_: str | None
    """Tax class"""
    compound: bool | None
    """Whether this is a compound rate"""
    country: str | None
    """Country ISO 3166 code"""
    id: int | None
    """Unique identifier"""
    name: str | None
    """Tax rate name"""
    order: int | None
    """Order in queries"""
    postcode: str | None
    """Postcode/ZIP"""
    postcodes: list[Any] | None
    """Postcodes/ZIPs"""
    priority: int | None
    """Tax priority"""
    rate: str | None
    """Tax rate"""
    shipping: bool | None
    """Applied to shipping"""
    state: str | None
    """State code"""


class TaxRatesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    cities: list[list[Any]]
    """City names"""
    city: list[str]
    """City name"""
    class_: list[str]
    """Tax class"""
    compound: list[bool]
    """Whether this is a compound rate"""
    country: list[str]
    """Country ISO 3166 code"""
    id: list[int]
    """Unique identifier"""
    name: list[str]
    """Tax rate name"""
    order: list[int]
    """Order in queries"""
    postcode: list[str]
    """Postcode/ZIP"""
    postcodes: list[list[Any]]
    """Postcodes/ZIPs"""
    priority: list[int]
    """Tax priority"""
    rate: list[str]
    """Tax rate"""
    shipping: list[bool]
    """Applied to shipping"""
    state: list[str]
    """State code"""


class TaxRatesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    cities: Any
    """City names"""
    city: Any
    """City name"""
    class_: Any
    """Tax class"""
    compound: Any
    """Whether this is a compound rate"""
    country: Any
    """Country ISO 3166 code"""
    id: Any
    """Unique identifier"""
    name: Any
    """Tax rate name"""
    order: Any
    """Order in queries"""
    postcode: Any
    """Postcode/ZIP"""
    postcodes: Any
    """Postcodes/ZIPs"""
    priority: Any
    """Tax priority"""
    rate: Any
    """Tax rate"""
    shipping: Any
    """Applied to shipping"""
    state: Any
    """State code"""


class TaxRatesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    cities: str
    """City names"""
    city: str
    """City name"""
    class_: str
    """Tax class"""
    compound: str
    """Whether this is a compound rate"""
    country: str
    """Country ISO 3166 code"""
    id: str
    """Unique identifier"""
    name: str
    """Tax rate name"""
    order: str
    """Order in queries"""
    postcode: str
    """Postcode/ZIP"""
    postcodes: str
    """Postcodes/ZIPs"""
    priority: str
    """Tax priority"""
    rate: str
    """Tax rate"""
    shipping: str
    """Applied to shipping"""
    state: str
    """State code"""


class TaxRatesSortFilter(TypedDict, total=False):
    """Available fields for sorting tax_rates search results."""
    cities: AirbyteSortOrder
    """City names"""
    city: AirbyteSortOrder
    """City name"""
    class_: AirbyteSortOrder
    """Tax class"""
    compound: AirbyteSortOrder
    """Whether this is a compound rate"""
    country: AirbyteSortOrder
    """Country ISO 3166 code"""
    id: AirbyteSortOrder
    """Unique identifier"""
    name: AirbyteSortOrder
    """Tax rate name"""
    order: AirbyteSortOrder
    """Order in queries"""
    postcode: AirbyteSortOrder
    """Postcode/ZIP"""
    postcodes: AirbyteSortOrder
    """Postcodes/ZIPs"""
    priority: AirbyteSortOrder
    """Tax priority"""
    rate: AirbyteSortOrder
    """Tax rate"""
    shipping: AirbyteSortOrder
    """Applied to shipping"""
    state: AirbyteSortOrder
    """State code"""


# Entity-specific condition types for tax_rates
class TaxRatesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TaxRatesSearchFilter


class TaxRatesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TaxRatesSearchFilter


class TaxRatesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TaxRatesSearchFilter


class TaxRatesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TaxRatesSearchFilter


class TaxRatesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TaxRatesSearchFilter


class TaxRatesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TaxRatesSearchFilter


class TaxRatesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TaxRatesStringFilter


class TaxRatesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TaxRatesStringFilter


class TaxRatesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TaxRatesStringFilter


class TaxRatesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TaxRatesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TaxRatesInCondition = TypedDict("TaxRatesInCondition", {"in": TaxRatesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TaxRatesNotCondition = TypedDict("TaxRatesNotCondition", {"not": "TaxRatesCondition"}, total=False)
"""Negates the nested condition."""

TaxRatesAndCondition = TypedDict("TaxRatesAndCondition", {"and": "list[TaxRatesCondition]"}, total=False)
"""True if all nested conditions are true."""

TaxRatesOrCondition = TypedDict("TaxRatesOrCondition", {"or": "list[TaxRatesCondition]"}, total=False)
"""True if any nested condition is true."""

TaxRatesAnyCondition = TypedDict("TaxRatesAnyCondition", {"any": TaxRatesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tax_rates condition types
TaxRatesCondition = (
    TaxRatesEqCondition
    | TaxRatesNeqCondition
    | TaxRatesGtCondition
    | TaxRatesGteCondition
    | TaxRatesLtCondition
    | TaxRatesLteCondition
    | TaxRatesInCondition
    | TaxRatesLikeCondition
    | TaxRatesFuzzyCondition
    | TaxRatesKeywordCondition
    | TaxRatesContainsCondition
    | TaxRatesNotCondition
    | TaxRatesAndCondition
    | TaxRatesOrCondition
    | TaxRatesAnyCondition
)


class TaxRatesSearchQuery(TypedDict, total=False):
    """Search query for tax_rates entity."""
    filter: TaxRatesCondition
    sort: list[TaxRatesSortFilter]


# ===== TAX_CLASSES SEARCH TYPES =====

class TaxClassesSearchFilter(TypedDict, total=False):
    """Available fields for filtering tax_classes search queries."""
    name: str | None
    """Tax class name"""
    slug: str | None
    """Unique identifier"""


class TaxClassesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    name: list[str]
    """Tax class name"""
    slug: list[str]
    """Unique identifier"""


class TaxClassesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    name: Any
    """Tax class name"""
    slug: Any
    """Unique identifier"""


class TaxClassesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    name: str
    """Tax class name"""
    slug: str
    """Unique identifier"""


class TaxClassesSortFilter(TypedDict, total=False):
    """Available fields for sorting tax_classes search results."""
    name: AirbyteSortOrder
    """Tax class name"""
    slug: AirbyteSortOrder
    """Unique identifier"""


# Entity-specific condition types for tax_classes
class TaxClassesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TaxClassesSearchFilter


class TaxClassesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TaxClassesSearchFilter


class TaxClassesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TaxClassesSearchFilter


class TaxClassesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TaxClassesSearchFilter


class TaxClassesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TaxClassesSearchFilter


class TaxClassesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TaxClassesSearchFilter


class TaxClassesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TaxClassesStringFilter


class TaxClassesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TaxClassesStringFilter


class TaxClassesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TaxClassesStringFilter


class TaxClassesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TaxClassesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TaxClassesInCondition = TypedDict("TaxClassesInCondition", {"in": TaxClassesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TaxClassesNotCondition = TypedDict("TaxClassesNotCondition", {"not": "TaxClassesCondition"}, total=False)
"""Negates the nested condition."""

TaxClassesAndCondition = TypedDict("TaxClassesAndCondition", {"and": "list[TaxClassesCondition]"}, total=False)
"""True if all nested conditions are true."""

TaxClassesOrCondition = TypedDict("TaxClassesOrCondition", {"or": "list[TaxClassesCondition]"}, total=False)
"""True if any nested condition is true."""

TaxClassesAnyCondition = TypedDict("TaxClassesAnyCondition", {"any": TaxClassesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tax_classes condition types
TaxClassesCondition = (
    TaxClassesEqCondition
    | TaxClassesNeqCondition
    | TaxClassesGtCondition
    | TaxClassesGteCondition
    | TaxClassesLtCondition
    | TaxClassesLteCondition
    | TaxClassesInCondition
    | TaxClassesLikeCondition
    | TaxClassesFuzzyCondition
    | TaxClassesKeywordCondition
    | TaxClassesContainsCondition
    | TaxClassesNotCondition
    | TaxClassesAndCondition
    | TaxClassesOrCondition
    | TaxClassesAnyCondition
)


class TaxClassesSearchQuery(TypedDict, total=False):
    """Search query for tax_classes entity."""
    filter: TaxClassesCondition
    sort: list[TaxClassesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
