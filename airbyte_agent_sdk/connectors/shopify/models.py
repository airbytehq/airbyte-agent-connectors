"""
Pydantic models for shopify connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
from typing import Optional

# Authentication configuration - multiple options available

class ShopifyAccessTokenAuthenticationAuthConfig(BaseModel):
    """Access Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Shopify Admin API access token"""

class ShopifyOauth2AuthConfig(BaseModel):
    """OAuth2"""

    model_config = ConfigDict(extra="forbid")

    client_id: Optional[str] = None
    """Your Shopify OAuth2 application client ID"""
    client_secret: Optional[str] = None
    """Your Shopify OAuth2 application client secret"""
    access_token: str
    """Your Shopify OAuth2 access token"""

ShopifyAuthConfig = ShopifyAccessTokenAuthenticationAuthConfig | ShopifyOauth2AuthConfig

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class CustomerAddress(BaseModel):
    """A customer address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    customer_id: int | None = Field(default=None)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    company: str | None = Field(default=None)
    address1: str | None = Field(default=None)
    address2: str | None = Field(default=None)
    city: str | None = Field(default=None)
    province: str | None = Field(default=None)
    country: str | None = Field(default=None)
    zip: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    name: str | None = Field(default=None)
    province_code: str | None = Field(default=None)
    country_code: str | None = Field(default=None)
    country_name: str | None = Field(default=None)
    default: bool | None = Field(default=None)

class Customer(BaseModel):
    """A Shopify customer"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    email: str | None = Field(default=None)
    accepts_marketing: bool | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    orders_count: int | None = Field(default=None)
    state: str | None = Field(default=None)
    total_spent: str | None = Field(default=None)
    last_order_id: int | None = Field(default=None)
    note: str | None = Field(default=None)
    verified_email: bool | None = Field(default=None)
    multipass_identifier: str | None = Field(default=None)
    tax_exempt: bool | None = Field(default=None)
    tags: str | None = Field(default=None)
    last_order_name: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    addresses: list[CustomerAddress] | None = Field(default=None)
    accepts_marketing_updated_at: str | None = Field(default=None)
    marketing_opt_in_level: str | None = Field(default=None)
    tax_exemptions: list[str] | None = Field(default=None)
    email_marketing_consent: Any | None = Field(default=None)
    sms_marketing_consent: Any | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)
    default_address: Any | None = Field(default=None)

class CustomerList(BaseModel):
    """CustomerList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    customers: list[Customer] | None = Field(default=None)

class CustomerAddressList(BaseModel):
    """CustomerAddressList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    addresses: list[CustomerAddress] | None = Field(default=None)

class MarketingConsent(BaseModel):
    """MarketingConsent type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    state: str | None = Field(default=None)
    opt_in_level: str | None = Field(default=None)
    consent_updated_at: str | None = Field(default=None)
    consent_collected_from: str | None = Field(default=None)

class OrderAddress(BaseModel):
    """An address in an order (shipping or billing) - does not have id field"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    company: str | None = Field(default=None)
    address1: str | None = Field(default=None)
    address2: str | None = Field(default=None)
    city: str | None = Field(default=None)
    province: str | None = Field(default=None)
    country: str | None = Field(default=None)
    zip: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    name: str | None = Field(default=None)
    province_code: str | None = Field(default=None)
    country_code: str | None = Field(default=None)
    latitude: float | None = Field(default=None)
    longitude: float | None = Field(default=None)

class LineItem(BaseModel):
    """LineItem type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)
    attributed_staffs: list[dict[str, Any]] | None = Field(default=None)
    current_quantity: int | None = Field(default=None)
    fulfillable_quantity: int | None = Field(default=None)
    fulfillment_service: str | None = Field(default=None)
    fulfillment_status: str | None = Field(default=None)
    gift_card: bool | None = Field(default=None)
    grams: int | None = Field(default=None)
    name: str | None = Field(default=None)
    price: str | None = Field(default=None)
    price_set: dict[str, Any] | None = Field(default=None)
    product_exists: bool | None = Field(default=None)
    product_id: int | None = Field(default=None)
    properties: list[dict[str, Any]] | None = Field(default=None)
    quantity: int | None = Field(default=None)
    requires_shipping: bool | None = Field(default=None)
    sku: str | None = Field(default=None)
    taxable: bool | None = Field(default=None)
    title: str | None = Field(default=None)
    total_discount: str | None = Field(default=None)
    total_discount_set: dict[str, Any] | None = Field(default=None)
    variant_id: int | None = Field(default=None)
    variant_inventory_management: str | None = Field(default=None)
    variant_title: str | None = Field(default=None)
    vendor: str | None = Field(default=None)
    tax_lines: list[dict[str, Any]] | None = Field(default=None)
    duties: list[dict[str, Any]] | None = Field(default=None)
    discount_allocations: list[dict[str, Any]] | None = Field(default=None)

class Transaction(BaseModel):
    """An order transaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    order_id: int | None = Field(default=None)
    kind: str | None = Field(default=None)
    gateway: str | None = Field(default=None)
    status: str | None = Field(default=None)
    message: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    test: bool | None = Field(default=None)
    authorization: str | None = Field(default=None)
    location_id: int | None = Field(default=None)
    user_id: int | None = Field(default=None)
    parent_id: int | None = Field(default=None)
    processed_at: str | None = Field(default=None)
    device_id: int | None = Field(default=None)
    error_code: str | None = Field(default=None)
    source_name: str | None = Field(default=None)
    receipt: dict[str, Any] | None = Field(default=None)
    currency_exchange_adjustment: dict[str, Any] | None = Field(default=None)
    amount: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    payment_id: str | None = Field(default=None)
    total_unsettled_set: dict[str, Any] | None = Field(default=None)
    manual_payment_gateway: bool | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)

class Refund(BaseModel):
    """An order refund"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    order_id: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    note: str | None = Field(default=None)
    user_id: int | None = Field(default=None)
    processed_at: str | None = Field(default=None)
    restock: bool | None = Field(default=None)
    duties: list[dict[str, Any]] | None = Field(default=None)
    total_duties_set: dict[str, Any] | None = Field(default=None)
    return_: dict[str, Any] | None = Field(default=None, alias="return")
    refund_line_items: list[dict[str, Any]] | None = Field(default=None)
    transactions: list[Transaction] | None = Field(default=None)
    order_adjustments: list[dict[str, Any]] | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)
    refund_shipping_lines: list[dict[str, Any]] | None = Field(default=None)

class Fulfillment(BaseModel):
    """A fulfillment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    order_id: int | None = Field(default=None)
    status: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    service: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    tracking_company: str | None = Field(default=None)
    shipment_status: str | None = Field(default=None)
    location_id: int | None = Field(default=None)
    origin_address: dict[str, Any] | None = Field(default=None)
    line_items: list[LineItem] | None = Field(default=None)
    tracking_number: str | None = Field(default=None)
    tracking_numbers: list[str] | None = Field(default=None)
    tracking_url: str | None = Field(default=None)
    tracking_urls: list[str] | None = Field(default=None)
    receipt: dict[str, Any] | None = Field(default=None)
    name: str | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)

class Order(BaseModel):
    """A Shopify order"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    admin_graphql_api_id: str | None = Field(default=None)
    app_id: int | None = Field(default=None)
    browser_ip: str | None = Field(default=None)
    buyer_accepts_marketing: bool | None = Field(default=None)
    cancel_reason: str | None = Field(default=None)
    cancelled_at: str | None = Field(default=None)
    cart_token: str | None = Field(default=None)
    checkout_id: int | None = Field(default=None)
    checkout_token: str | None = Field(default=None)
    client_details: dict[str, Any] | None = Field(default=None)
    closed_at: str | None = Field(default=None)
    company: dict[str, Any] | None = Field(default=None)
    confirmation_number: str | None = Field(default=None)
    confirmed: bool | None = Field(default=None)
    contact_email: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    current_subtotal_price: str | None = Field(default=None)
    current_subtotal_price_set: dict[str, Any] | None = Field(default=None)
    current_total_additional_fees_set: dict[str, Any] | None = Field(default=None)
    current_total_discounts: str | None = Field(default=None)
    current_total_discounts_set: dict[str, Any] | None = Field(default=None)
    current_total_duties_set: dict[str, Any] | None = Field(default=None)
    current_total_price: str | None = Field(default=None)
    current_total_price_set: dict[str, Any] | None = Field(default=None)
    current_total_tax: str | None = Field(default=None)
    current_total_tax_set: dict[str, Any] | None = Field(default=None)
    customer: Any | None = Field(default=None)
    customer_locale: str | None = Field(default=None)
    device_id: int | None = Field(default=None)
    discount_applications: list[dict[str, Any]] | None = Field(default=None)
    discount_codes: list[dict[str, Any]] | None = Field(default=None)
    email: str | None = Field(default=None)
    estimated_taxes: bool | None = Field(default=None)
    financial_status: str | None = Field(default=None)
    fulfillment_status: str | None = Field(default=None)
    fulfillments: list[Fulfillment] | None = Field(default=None)
    gateway: str | None = Field(default=None)
    landing_site: str | None = Field(default=None)
    landing_site_ref: str | None = Field(default=None)
    line_items: list[LineItem] | None = Field(default=None)
    location_id: int | None = Field(default=None)
    merchant_of_record_app_id: int | None = Field(default=None)
    merchant_business_entity_id: str | None = Field(default=None)
    duties_included: bool | None = Field(default=None)
    total_cash_rounding_payment_adjustment_set: dict[str, Any] | None = Field(default=None)
    total_cash_rounding_refund_adjustment_set: dict[str, Any] | None = Field(default=None)
    payment_terms: dict[str, Any] | None = Field(default=None)
    name: str | None = Field(default=None)
    note: str | None = Field(default=None)
    note_attributes: list[dict[str, Any]] | None = Field(default=None)
    number: int | None = Field(default=None)
    order_number: int | None = Field(default=None)
    order_status_url: str | None = Field(default=None)
    original_total_additional_fees_set: dict[str, Any] | None = Field(default=None)
    original_total_duties_set: dict[str, Any] | None = Field(default=None)
    payment_gateway_names: list[str] | None = Field(default=None)
    phone: str | None = Field(default=None)
    po_number: str | None = Field(default=None)
    presentment_currency: str | None = Field(default=None)
    processed_at: str | None = Field(default=None)
    reference: str | None = Field(default=None)
    referring_site: str | None = Field(default=None)
    refunds: list[Refund] | None = Field(default=None)
    shipping_address: Any | None = Field(default=None)
    shipping_lines: list[dict[str, Any]] | None = Field(default=None)
    source_identifier: str | None = Field(default=None)
    source_name: str | None = Field(default=None)
    source_url: str | None = Field(default=None)
    subtotal_price: str | None = Field(default=None)
    subtotal_price_set: dict[str, Any] | None = Field(default=None)
    tags: str | None = Field(default=None)
    tax_exempt: bool | None = Field(default=None)
    tax_lines: list[dict[str, Any]] | None = Field(default=None)
    taxes_included: bool | None = Field(default=None)
    test: bool | None = Field(default=None)
    token: str | None = Field(default=None)
    total_discounts: str | None = Field(default=None)
    total_discounts_set: dict[str, Any] | None = Field(default=None)
    total_line_items_price: str | None = Field(default=None)
    total_line_items_price_set: dict[str, Any] | None = Field(default=None)
    total_outstanding: str | None = Field(default=None)
    total_price: str | None = Field(default=None)
    total_price_set: dict[str, Any] | None = Field(default=None)
    total_shipping_price_set: dict[str, Any] | None = Field(default=None)
    total_tax: str | None = Field(default=None)
    total_tax_set: dict[str, Any] | None = Field(default=None)
    total_tip_received: str | None = Field(default=None)
    total_weight: int | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    user_id: int | None = Field(default=None)
    billing_address: Any | None = Field(default=None)

class OrderList(BaseModel):
    """OrderList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    orders: list[Order] | None = Field(default=None)

class ProductVariant(BaseModel):
    """A product variant"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    product_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    price: str | None = Field(default=None)
    sku: str | None = Field(default=None)
    position: int | None = Field(default=None)
    inventory_policy: str | None = Field(default=None)
    compare_at_price: str | None = Field(default=None)
    fulfillment_service: str | None = Field(default=None)
    inventory_management: str | None = Field(default=None)
    option1: str | None = Field(default=None)
    option2: str | None = Field(default=None)
    option3: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    taxable: bool | None = Field(default=None)
    barcode: str | None = Field(default=None)
    grams: int | None = Field(default=None)
    image_id: int | None = Field(default=None)
    weight: float | None = Field(default=None)
    weight_unit: str | None = Field(default=None)
    inventory_item_id: int | None = Field(default=None)
    inventory_quantity: int | None = Field(default=None)
    old_inventory_quantity: int | None = Field(default=None)
    requires_shipping: bool | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)

class ProductImage(BaseModel):
    """A product image"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    product_id: int | None = Field(default=None)
    position: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    alt: str | None = Field(default=None)
    width: int | None = Field(default=None)
    height: int | None = Field(default=None)
    src: str | None = Field(default=None)
    variant_ids: list[int] | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)

class Product(BaseModel):
    """A Shopify product"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    title: str | None = Field(default=None)
    body_html: str | None = Field(default=None)
    vendor: str | None = Field(default=None)
    product_type: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    handle: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    published_at: str | None = Field(default=None)
    template_suffix: str | None = Field(default=None)
    published_scope: str | None = Field(default=None)
    tags: str | None = Field(default=None)
    status: str | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)
    variants: list[ProductVariant] | None = Field(default=None)
    options: list[dict[str, Any]] | None = Field(default=None)
    images: list[ProductImage] | None = Field(default=None)
    image: Any | None = Field(default=None)

class ProductList(BaseModel):
    """ProductList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    products: list[Product] | None = Field(default=None)

class ProductVariantList(BaseModel):
    """ProductVariantList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    variants: list[ProductVariant] | None = Field(default=None)

class ProductImageList(BaseModel):
    """ProductImageList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    images: list[ProductImage] | None = Field(default=None)

class AbandonedCheckout(BaseModel):
    """An abandoned checkout"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    token: str | None = Field(default=None)
    cart_token: str | None = Field(default=None)
    email: str | None = Field(default=None)
    gateway: str | None = Field(default=None)
    buyer_accepts_marketing: bool | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    landing_site: str | None = Field(default=None)
    note: str | None = Field(default=None)
    note_attributes: list[dict[str, Any]] | None = Field(default=None)
    referring_site: str | None = Field(default=None)
    shipping_lines: list[dict[str, Any]] | None = Field(default=None)
    taxes_included: bool | None = Field(default=None)
    total_weight: int | None = Field(default=None)
    currency: str | None = Field(default=None)
    completed_at: str | None = Field(default=None)
    closed_at: str | None = Field(default=None)
    user_id: int | None = Field(default=None)
    location_id: int | None = Field(default=None)
    source_identifier: str | None = Field(default=None)
    source_url: str | None = Field(default=None)
    device_id: int | None = Field(default=None)
    phone: str | None = Field(default=None)
    customer_locale: str | None = Field(default=None)
    line_items: list[LineItem] | None = Field(default=None)
    name: str | None = Field(default=None)
    source: str | None = Field(default=None)
    abandoned_checkout_url: str | None = Field(default=None)
    discount_codes: list[dict[str, Any]] | None = Field(default=None)
    tax_lines: list[dict[str, Any]] | None = Field(default=None)
    source_name: str | None = Field(default=None)
    presentment_currency: str | None = Field(default=None)
    buyer_accepts_sms_marketing: bool | None = Field(default=None)
    sms_marketing_phone: str | None = Field(default=None)
    total_discounts: str | None = Field(default=None)
    total_line_items_price: str | None = Field(default=None)
    total_price: str | None = Field(default=None)
    total_tax: str | None = Field(default=None)
    subtotal_price: str | None = Field(default=None)
    total_duties: str | None = Field(default=None)
    billing_address: Any | None = Field(default=None)
    shipping_address: Any | None = Field(default=None)
    customer: Any | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)

class AbandonedCheckoutList(BaseModel):
    """AbandonedCheckoutList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    checkouts: list[AbandonedCheckout] | None = Field(default=None)

class Location(BaseModel):
    """A store location"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    address1: str | None = Field(default=None)
    address2: str | None = Field(default=None)
    city: str | None = Field(default=None)
    zip: str | None = Field(default=None)
    province: str | None = Field(default=None)
    country: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    country_code: str | None = Field(default=None)
    country_name: str | None = Field(default=None)
    province_code: str | None = Field(default=None)
    legacy: bool | None = Field(default=None)
    active: bool | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)
    localized_country_name: str | None = Field(default=None)
    localized_province_name: str | None = Field(default=None)

class LocationList(BaseModel):
    """LocationList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    locations: list[Location] | None = Field(default=None)

class InventoryLevel(BaseModel):
    """An inventory level"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inventory_item_id: int | None = Field(default=None)
    location_id: int | None = Field(default=None)
    available: int | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)

class InventoryLevelList(BaseModel):
    """InventoryLevelList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inventory_levels: list[InventoryLevel] | None = Field(default=None)

class InventoryItem(BaseModel):
    """An inventory item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    sku: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    requires_shipping: bool | None = Field(default=None)
    cost: str | None = Field(default=None)
    country_code_of_origin: str | None = Field(default=None)
    province_code_of_origin: str | None = Field(default=None)
    harmonized_system_code: str | None = Field(default=None)
    tracked: bool | None = Field(default=None)
    country_harmonized_system_codes: list[dict[str, Any]] | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)

class InventoryItemList(BaseModel):
    """InventoryItemList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inventory_items: list[InventoryItem] | None = Field(default=None)

class Shop(BaseModel):
    """Shop configuration"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    domain: str | None = Field(default=None)
    province: str | None = Field(default=None)
    country: str | None = Field(default=None)
    address1: str | None = Field(default=None)
    zip: str | None = Field(default=None)
    city: str | None = Field(default=None)
    source: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    latitude: float | None = Field(default=None)
    longitude: float | None = Field(default=None)
    primary_locale: str | None = Field(default=None)
    address2: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    country_code: str | None = Field(default=None)
    country_name: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    customer_email: str | None = Field(default=None)
    timezone: str | None = Field(default=None)
    iana_timezone: str | None = Field(default=None)
    shop_owner: str | None = Field(default=None)
    money_format: str | None = Field(default=None)
    money_with_currency_format: str | None = Field(default=None)
    weight_unit: str | None = Field(default=None)
    province_code: str | None = Field(default=None)
    taxes_included: bool | None = Field(default=None)
    auto_configure_tax_inclusivity: bool | None = Field(default=None)
    tax_shipping: bool | None = Field(default=None)
    county_taxes: bool | None = Field(default=None)
    plan_display_name: str | None = Field(default=None)
    plan_name: str | None = Field(default=None)
    has_discounts: bool | None = Field(default=None)
    has_gift_cards: bool | None = Field(default=None)
    myshopify_domain: str | None = Field(default=None)
    google_apps_domain: str | None = Field(default=None)
    google_apps_login_enabled: bool | None = Field(default=None)
    money_in_emails_format: str | None = Field(default=None)
    money_with_currency_in_emails_format: str | None = Field(default=None)
    eligible_for_payments: bool | None = Field(default=None)
    requires_extra_payments_agreement: bool | None = Field(default=None)
    password_enabled: bool | None = Field(default=None)
    has_storefront: bool | None = Field(default=None)
    finances: bool | None = Field(default=None)
    primary_location_id: int | None = Field(default=None)
    checkout_api_supported: bool | None = Field(default=None)
    multi_location_enabled: bool | None = Field(default=None)
    setup_required: bool | None = Field(default=None)
    pre_launch_enabled: bool | None = Field(default=None)
    enabled_presentment_currencies: list[str] | None = Field(default=None)
    transactional_sms_disabled: bool | None = Field(default=None)
    marketing_sms_consent_enabled_at_checkout: bool | None = Field(default=None)

class PriceRule(BaseModel):
    """A price rule"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    value_type: str | None = Field(default=None)
    value: str | None = Field(default=None)
    customer_selection: str | None = Field(default=None)
    target_type: str | None = Field(default=None)
    target_selection: str | None = Field(default=None)
    allocation_method: str | None = Field(default=None)
    allocation_limit: int | None = Field(default=None)
    once_per_customer: bool | None = Field(default=None)
    usage_limit: int | None = Field(default=None)
    starts_at: str | None = Field(default=None)
    ends_at: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    entitled_product_ids: list[int] | None = Field(default=None)
    entitled_variant_ids: list[int] | None = Field(default=None)
    entitled_collection_ids: list[int] | None = Field(default=None)
    entitled_country_ids: list[int] | None = Field(default=None)
    prerequisite_product_ids: list[int] | None = Field(default=None)
    prerequisite_variant_ids: list[int] | None = Field(default=None)
    prerequisite_collection_ids: list[int] | None = Field(default=None)
    customer_segment_prerequisite_ids: list[int] | None = Field(default=None)
    prerequisite_customer_ids: list[int] | None = Field(default=None)
    prerequisite_subtotal_range: dict[str, Any] | None = Field(default=None)
    prerequisite_quantity_range: dict[str, Any] | None = Field(default=None)
    prerequisite_shipping_price_range: dict[str, Any] | None = Field(default=None)
    prerequisite_to_entitlement_quantity_ratio: dict[str, Any] | None = Field(default=None)
    prerequisite_to_entitlement_purchase: dict[str, Any] | None = Field(default=None)
    title: str | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)

class PriceRuleList(BaseModel):
    """PriceRuleList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    price_rules: list[PriceRule] | None = Field(default=None)

class DiscountCode(BaseModel):
    """A discount code"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    price_rule_id: int | None = Field(default=None)
    code: str | None = Field(default=None)
    usage_count: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class DiscountCodeList(BaseModel):
    """DiscountCodeList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    discount_codes: list[DiscountCode] | None = Field(default=None)

class CustomCollection(BaseModel):
    """A custom collection"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    handle: str | None = Field(default=None)
    title: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    body_html: str | None = Field(default=None)
    published_at: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    template_suffix: str | None = Field(default=None)
    published_scope: str | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)
    image: dict[str, Any] | None = Field(default=None)
    products_count: int | None = Field(default=None)

class CustomCollectionList(BaseModel):
    """CustomCollectionList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    custom_collections: list[CustomCollection] | None = Field(default=None)

class SmartCollection(BaseModel):
    """A smart collection"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    handle: str | None = Field(default=None)
    title: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    body_html: str | None = Field(default=None)
    published_at: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    template_suffix: str | None = Field(default=None)
    disjunctive: bool | None = Field(default=None)
    rules: list[dict[str, Any]] | None = Field(default=None)
    published_scope: str | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)
    image: dict[str, Any] | None = Field(default=None)
    products_count: int | None = Field(default=None)

class SmartCollectionList(BaseModel):
    """SmartCollectionList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    smart_collections: list[SmartCollection] | None = Field(default=None)

class Collect(BaseModel):
    """A collect (product-collection link)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    collection_id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    position: int | None = Field(default=None)
    sort_value: str | None = Field(default=None)

class CollectList(BaseModel):
    """CollectList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    collects: list[Collect] | None = Field(default=None)

class DraftOrder(BaseModel):
    """A draft order"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    note: str | None = Field(default=None)
    email: str | None = Field(default=None)
    taxes_included: bool | None = Field(default=None)
    currency: str | None = Field(default=None)
    invoice_sent_at: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    tax_exempt: bool | None = Field(default=None)
    completed_at: str | None = Field(default=None)
    name: str | None = Field(default=None)
    status: str | None = Field(default=None)
    line_items: list[LineItem] | None = Field(default=None)
    shipping_address: Any | None = Field(default=None)
    billing_address: Any | None = Field(default=None)
    invoice_url: str | None = Field(default=None)
    applied_discount: dict[str, Any] | None = Field(default=None)
    order_id: int | None = Field(default=None)
    shipping_line: dict[str, Any] | None = Field(default=None)
    tax_lines: list[dict[str, Any]] | None = Field(default=None)
    tags: str | None = Field(default=None)
    note_attributes: list[dict[str, Any]] | None = Field(default=None)
    total_price: str | None = Field(default=None)
    subtotal_price: str | None = Field(default=None)
    total_tax: str | None = Field(default=None)
    payment_terms: dict[str, Any] | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)
    customer: Any | None = Field(default=None)
    allow_discount_codes_in_checkout: bool | None = Field(default=None, alias="allow_discount_codes_in_checkout?")
    b2b: bool | None = Field(default=None, alias="b2b?")
    api_client_id: int | None = Field(default=None)
    created_on_api_version_handle: str | None = Field(default=None)

class DraftOrderList(BaseModel):
    """DraftOrderList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    draft_orders: list[DraftOrder] | None = Field(default=None)

class FulfillmentList(BaseModel):
    """FulfillmentList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    fulfillments: list[Fulfillment] | None = Field(default=None)

class FulfillmentOrder(BaseModel):
    """A fulfillment order"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    shop_id: int | None = Field(default=None)
    order_id: int | None = Field(default=None)
    assigned_location_id: int | None = Field(default=None)
    request_status: str | None = Field(default=None)
    status: str | None = Field(default=None)
    supported_actions: list[str] | None = Field(default=None)
    destination: dict[str, Any] | None = Field(default=None)
    line_items: list[dict[str, Any]] | None = Field(default=None)
    fulfill_at: str | None = Field(default=None)
    fulfill_by: str | None = Field(default=None)
    international_duties: dict[str, Any] | None = Field(default=None)
    fulfillment_holds: list[dict[str, Any]] | None = Field(default=None)
    delivery_method: dict[str, Any] | None = Field(default=None)
    assigned_location: dict[str, Any] | None = Field(default=None)
    merchant_requests: list[dict[str, Any]] | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class FulfillmentOrderList(BaseModel):
    """FulfillmentOrderList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    fulfillment_orders: list[FulfillmentOrder] | None = Field(default=None)

class RefundList(BaseModel):
    """RefundList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    refunds: list[Refund] | None = Field(default=None)

class TransactionList(BaseModel):
    """TransactionList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transactions: list[Transaction] | None = Field(default=None)

class TenderTransaction(BaseModel):
    """A tender transaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    order_id: int | None = Field(default=None)
    amount: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    user_id: int | None = Field(default=None)
    test: bool | None = Field(default=None)
    processed_at: str | None = Field(default=None)
    remote_reference: str | None = Field(default=None)
    payment_details: dict[str, Any] | None = Field(default=None)
    payment_method: str | None = Field(default=None)

class TenderTransactionList(BaseModel):
    """TenderTransactionList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tender_transactions: list[TenderTransaction] | None = Field(default=None)

class Country(BaseModel):
    """A country"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    code: str | None = Field(default=None)
    tax_name: str | None = Field(default=None)
    tax: float | None = Field(default=None)
    provinces: list[dict[str, Any]] | None = Field(default=None)

class CountryList(BaseModel):
    """CountryList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    countries: list[Country] | None = Field(default=None)

class Page(BaseModel):
    """A static page on the store"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    title: str | None = Field(default=None)
    handle: str | None = Field(default=None)
    body_html: str | None = Field(default=None)
    author: str | None = Field(default=None)
    template_suffix: str | None = Field(default=None)
    published_at: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)

class PageList(BaseModel):
    """PageList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pages: list[Page] | None = Field(default=None)

class Blog(BaseModel):
    """A blog on the store"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    title: str | None = Field(default=None)
    handle: str | None = Field(default=None)
    commentable: str | None = Field(default=None)
    feedburner: str | None = Field(default=None)
    feedburner_location: str | None = Field(default=None)
    tags: str | None = Field(default=None)
    template_suffix: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)

class BlogList(BaseModel):
    """BlogList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    blogs: list[Blog] | None = Field(default=None)

class Article(BaseModel):
    """A blog article (post)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    title: str | None = Field(default=None)
    handle: str | None = Field(default=None)
    author: str | None = Field(default=None)
    blog_id: int | None = Field(default=None)
    body_html: str | None = Field(default=None)
    summary_html: str | None = Field(default=None)
    tags: str | None = Field(default=None)
    template_suffix: str | None = Field(default=None)
    published_at: str | None = Field(default=None)
    user_id: int | None = Field(default=None)
    image: Any | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)

class ArticleList(BaseModel):
    """ArticleList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    articles: list[Article] | None = Field(default=None)

class BalanceTransaction(BaseModel):
    """A Shopify Payments balance transaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    type_: str | None = Field(default=None, alias="type")
    test: bool | None = Field(default=None)
    payout_id: int | None = Field(default=None)
    payout_status: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    amount: str | None = Field(default=None)
    fee: str | None = Field(default=None)
    net: str | None = Field(default=None)
    source_id: int | None = Field(default=None)
    source_type: str | None = Field(default=None)
    source_order_id: int | None = Field(default=None)
    source_order_transaction_id: int | None = Field(default=None)
    processed_at: str | None = Field(default=None)
    adjustment_order_transactions: list[dict[str, Any]] | None = Field(default=None)
    adjustment_reason: str | None = Field(default=None)

class BalanceTransactionList(BaseModel):
    """BalanceTransactionList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transactions: list[BalanceTransaction] | None = Field(default=None)

class Dispute(BaseModel):
    """A Shopify Payments dispute"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    order_id: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    amount: str | None = Field(default=None)
    currency: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    network_reason_code: str | None = Field(default=None)
    status: str | None = Field(default=None)
    evidence_due_by: str | None = Field(default=None)
    evidence_sent_on: str | None = Field(default=None)
    finalized_on: str | None = Field(default=None)
    initiated_at: str | None = Field(default=None)

class DisputeList(BaseModel):
    """DisputeList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    disputes: list[Dispute] | None = Field(default=None)

class Metafield(BaseModel):
    """A metafield"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    namespace: str | None = Field(default=None)
    key: str | None = Field(default=None)
    value: Any | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    description: str | None = Field(default=None)
    owner_id: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    owner_resource: str | None = Field(default=None)
    admin_graphql_api_id: str | None = Field(default=None)

class MetafieldList(BaseModel):
    """MetafieldList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    metafields: list[Metafield] | None = Field(default=None)

class GraphQLUserError(BaseModel):
    """GraphQLUserError type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    field: Any | None = Field(default=None)
    message: str | None = Field(default=None)
    code: str | None = Field(default=None)

class CustomerCreateParamsInputAddressesItem(BaseModel):
    """Nested schema for CustomerCreateParamsInput.addresses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address1: str | None = Field(default=None)
    address2: str | None = Field(default=None)
    city: str | None = Field(default=None)
    province: str | None = Field(default=None)
    zip: str | None = Field(default=None)
    country_code: str | None = Field(default=None, alias="countryCode")
    phone: str | None = Field(default=None)
    first_name: str | None = Field(default=None, alias="firstName")
    last_name: str | None = Field(default=None, alias="lastName")

class CustomerCreateParamsInput(BaseModel):
    """CustomerInput object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None = Field(default=None, description="Customer email address")
    """Customer email address"""
    first_name: str | None = Field(default=None, alias="firstName", description="Customer first name")
    """Customer first name"""
    last_name: str | None = Field(default=None, alias="lastName", description="Customer last name")
    """Customer last name"""
    phone: str | None = Field(default=None, description="Customer phone number (E.164 format, e.g. +16465555555)")
    """Customer phone number (E.164 format, e.g. +16465555555)"""
    note: str | None = Field(default=None, description="Note about the customer")
    """Note about the customer"""
    tags: list[str] | None = Field(default=None, description="Tags to associate with the customer")
    """Tags to associate with the customer"""
    tax_exempt: bool | None = Field(default=None, alias="taxExempt", description="Whether the customer is tax exempt")
    """Whether the customer is tax exempt"""
    addresses: list[CustomerCreateParamsInputAddressesItem] | None = Field(default=None, description="List of customer addresses")
    """List of customer addresses"""

class CustomerCreateParams(BaseModel):
    """Parameters for creating a customer. Provide fields inside the 'input' object.
At least one of email, phone, firstName, or lastName is required.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    input: CustomerCreateParamsInput

class CustomerUpdateParamsInput(BaseModel):
    """CustomerInput object with id"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str = Field(description="The GraphQL GID of the customer (e.g. gid://shopify/Customer/123)")
    """The GraphQL GID of the customer (e.g. gid://shopify/Customer/123)"""
    email: str | None = Field(default=None, description="Customer email address")
    """Customer email address"""
    first_name: str | None = Field(default=None, alias="firstName", description="Customer first name")
    """Customer first name"""
    last_name: str | None = Field(default=None, alias="lastName", description="Customer last name")
    """Customer last name"""
    phone: str | None = Field(default=None, description="Customer phone number (E.164 format)")
    """Customer phone number (E.164 format)"""
    note: str | None = Field(default=None, description="Note about the customer")
    """Note about the customer"""
    tags: list[str] | None = Field(default=None, description="Tags to associate with the customer")
    """Tags to associate with the customer"""
    tax_exempt: bool | None = Field(default=None, alias="taxExempt", description="Whether the customer is tax exempt")
    """Whether the customer is tax exempt"""

class CustomerUpdateParams(BaseModel):
    """Parameters for updating a customer. The input.id field is required.
All other fields are optional for partial updates.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    input: CustomerUpdateParamsInput

class CustomerDeleteParamsInput(BaseModel):
    """Nested schema for CustomerDeleteParams.input"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str = Field(description="The GraphQL GID of the customer to delete (e.g. gid://shopify/Customer/123)")
    """The GraphQL GID of the customer to delete (e.g. gid://shopify/Customer/123)"""

class CustomerDeleteParams(BaseModel):
    """Parameters for deleting a customer. Only succeeds if the customer has no orders."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    input: CustomerDeleteParamsInput

class GraphQLCustomer(BaseModel):
    """Customer returned from GraphQL mutation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    email: str | None = Field(default=None)
    first_name: str | None = Field(default=None, alias="firstName")
    last_name: str | None = Field(default=None, alias="lastName")
    phone: str | None = Field(default=None)
    note: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    tax_exempt: bool | None = Field(default=None, alias="taxExempt")
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class CustomerCreatePayload(BaseModel):
    """CustomerCreatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    customer: GraphQLCustomer | None = Field(default=None)

class CustomerUpdatePayload(BaseModel):
    """CustomerUpdatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    customer: GraphQLCustomer | None = Field(default=None)

class CustomerDeletePayload(BaseModel):
    """CustomerDeletePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    deleted_customer_id: str | None = Field(default=None, alias="deletedCustomerId")

class CustomerMutationResponseData(BaseModel):
    """Nested schema for CustomerMutationResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    customer_create: CustomerCreatePayload | None = Field(default=None, alias="customerCreate")
    customer_update: CustomerUpdatePayload | None = Field(default=None, alias="customerUpdate")

class CustomerMutationResponse(BaseModel):
    """CustomerMutationResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: CustomerMutationResponseData | None = Field(default=None)

class CustomerDeleteResponseData(BaseModel):
    """Nested schema for CustomerDeleteResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    customer_delete: CustomerDeletePayload | None = Field(default=None, alias="customerDelete")

class CustomerDeleteResponse(BaseModel):
    """CustomerDeleteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: CustomerDeleteResponseData | None = Field(default=None)

class ProductCreateParamsProduct(BaseModel):
    """ProductCreateInput object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str = Field(description="Product title")
    """Product title"""
    description_html: str | None = Field(default=None, alias="descriptionHtml", description="Product description in HTML")
    """Product description in HTML"""
    vendor: str | None = Field(default=None, description="Product vendor")
    """Product vendor"""
    product_type: str | None = Field(default=None, alias="productType", description="Product type")
    """Product type"""
    tags: list[str] | None = Field(default=None, description="Tags for the product")
    """Tags for the product"""
    status: str | None = Field(default=None, description="Product status (ACTIVE, ARCHIVED, DRAFT)")
    """Product status (ACTIVE, ARCHIVED, DRAFT)"""

class ProductCreateParamsMediaItem(BaseModel):
    """Nested schema for ProductCreateParams.media_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    original_source: str | None = Field(default=None, alias="originalSource", description="URL of the media")
    """URL of the media"""
    media_content_type: str | None = Field(default=None, alias="mediaContentType")

class ProductCreateParams(BaseModel):
    """Parameters for creating a product.
Creates the product with a default variant.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    product: ProductCreateParamsProduct
    media: list[ProductCreateParamsMediaItem] | None = Field(default=None)

class ProductUpdateParamsProduct(BaseModel):
    """ProductUpdateInput object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str = Field(description="The GraphQL GID of the product (e.g. gid://shopify/Product/123)")
    """The GraphQL GID of the product (e.g. gid://shopify/Product/123)"""
    title: str | None = Field(default=None, description="Product title")
    """Product title"""
    description_html: str | None = Field(default=None, alias="descriptionHtml", description="Product description in HTML")
    """Product description in HTML"""
    vendor: str | None = Field(default=None, description="Product vendor")
    """Product vendor"""
    product_type: str | None = Field(default=None, alias="productType", description="Product type")
    """Product type"""
    tags: list[str] | None = Field(default=None, description="Tags for the product")
    """Tags for the product"""
    status: str | None = Field(default=None, description="Product status")
    """Product status"""

class ProductUpdateParams(BaseModel):
    """Parameters for updating a product. The product.id field is required.
All other fields are optional for partial updates.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    product: ProductUpdateParamsProduct

class ProductDeleteParamsInput(BaseModel):
    """Nested schema for ProductDeleteParams.input"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str = Field(description="The GraphQL GID of the product to delete (e.g. gid://shopify/Product/123)")
    """The GraphQL GID of the product to delete (e.g. gid://shopify/Product/123)"""

class ProductDeleteParams(BaseModel):
    """Parameters for deleting a product. This action is irreversible."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    input: ProductDeleteParamsInput

class GraphQLProduct(BaseModel):
    """Product returned from GraphQL mutation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    description_html: str | None = Field(default=None, alias="descriptionHtml")
    vendor: str | None = Field(default=None)
    product_type: str | None = Field(default=None, alias="productType")
    tags: list[str] | None = Field(default=None)
    status: str | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class ProductCreatePayload(BaseModel):
    """ProductCreatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    product: GraphQLProduct | None = Field(default=None)

class ProductUpdatePayload(BaseModel):
    """ProductUpdatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    product: GraphQLProduct | None = Field(default=None)

class ProductDeletePayload(BaseModel):
    """ProductDeletePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    deleted_product_id: str | None = Field(default=None, alias="deletedProductId")

class ProductMutationResponseData(BaseModel):
    """Nested schema for ProductMutationResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    product_create: ProductCreatePayload | None = Field(default=None, alias="productCreate")
    product_update: ProductUpdatePayload | None = Field(default=None, alias="productUpdate")

class ProductMutationResponse(BaseModel):
    """ProductMutationResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: ProductMutationResponseData | None = Field(default=None)

class ProductDeleteResponseData(BaseModel):
    """Nested schema for ProductDeleteResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    product_delete: ProductDeletePayload | None = Field(default=None, alias="productDelete")

class ProductDeleteResponse(BaseModel):
    """ProductDeleteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: ProductDeleteResponseData | None = Field(default=None)

class ProductVariantsCreateParams(BaseModel):
    """Parameters for bulk creating product variants."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    product_id: str = Field(alias="productId")
    variants: list[ProductVariantsCreateParamsVariantsItem]

class ProductVariantsUpdateParams(BaseModel):
    """Parameters for bulk updating product variants."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    product_id: str = Field(alias="productId")
    variants: list[ProductVariantsUpdateParamsVariantsItem]

class ProductVariantsDeleteParams(BaseModel):
    """Parameters for bulk deleting product variants. Cannot delete the last variant."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    product_id: str = Field(alias="productId")
    variants_ids: list[str] = Field(alias="variantsIds")

class GraphQLProductVariant(BaseModel):
    """GraphQLProductVariant type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    price: str | None = Field(default=None)
    sku: str | None = Field(default=None)
    barcode: str | None = Field(default=None)
    compare_at_price: str | None = Field(default=None, alias="compareAtPrice")
    inventory_quantity: int | None = Field(default=None, alias="inventoryQuantity")

class ProductVariantsBulkCreatePayload(BaseModel):
    """ProductVariantsBulkCreatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    product_variants: list[GraphQLProductVariant] | None = Field(default=None, alias="productVariants")

class ProductVariantsBulkUpdatePayload(BaseModel):
    """ProductVariantsBulkUpdatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    product_variants: list[GraphQLProductVariant] | None = Field(default=None, alias="productVariants")

class ProductVariantsBulkDeletePayloadProduct(BaseModel):
    """Nested schema for ProductVariantsBulkDeletePayload.product"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None | None = Field(default=None)

class ProductVariantsBulkDeletePayload(BaseModel):
    """ProductVariantsBulkDeletePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    product: ProductVariantsBulkDeletePayloadProduct | None = Field(default=None)

class ProductVariantsMutationResponseData(BaseModel):
    """Nested schema for ProductVariantsMutationResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    product_variants_bulk_create: ProductVariantsBulkCreatePayload | None = Field(default=None, alias="productVariantsBulkCreate")
    product_variants_bulk_update: ProductVariantsBulkUpdatePayload | None = Field(default=None, alias="productVariantsBulkUpdate")

class ProductVariantsMutationResponse(BaseModel):
    """ProductVariantsMutationResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: ProductVariantsMutationResponseData | None = Field(default=None)

class ProductVariantsDeleteResponseData(BaseModel):
    """Nested schema for ProductVariantsDeleteResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    product_variants_bulk_delete: ProductVariantsBulkDeletePayload | None = Field(default=None, alias="productVariantsBulkDelete")

class ProductVariantsDeleteResponse(BaseModel):
    """ProductVariantsDeleteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: ProductVariantsDeleteResponseData | None = Field(default=None)

class OrderCreateParamsOrderLineitemsItemPricesetShopmoney(BaseModel):
    """Nested schema for OrderCreateParamsOrderLineitemsItemPriceset.shopMoney"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None = Field(default=None)
    currency_code: str | None = Field(default=None, alias="currencyCode")

class OrderCreateParamsOrderLineitemsItemPriceset(BaseModel):
    """Nested schema for OrderCreateParamsOrderLineitemsItem.priceSet"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    shop_money: OrderCreateParamsOrderLineitemsItemPricesetShopmoney | None = Field(default=None, alias="shopMoney")

class OrderCreateParamsOrderLineitemsItem(BaseModel):
    """Nested schema for OrderCreateParamsOrder.lineItems_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    variant_id: str | None = Field(default=None, alias="variantId", description="GraphQL GID of the product variant")
    """GraphQL GID of the product variant"""
    quantity: int | None = Field(default=None, description="Quantity to order")
    """Quantity to order"""
    title: str | None = Field(default=None, description="Custom title (for custom line items without a variant)")
    """Custom title (for custom line items without a variant)"""
    price_set: OrderCreateParamsOrderLineitemsItemPriceset | None = Field(default=None, alias="priceSet")

class OrderCreateParamsOrderShippingaddress(BaseModel):
    """Nested schema for OrderCreateParamsOrder.shippingAddress"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address1: str | None = Field(default=None)
    city: str | None = Field(default=None)
    province_code: str | None = Field(default=None, alias="provinceCode")
    zip: str | None = Field(default=None)
    country_code: str | None = Field(default=None, alias="countryCode")
    first_name: str | None = Field(default=None, alias="firstName")
    last_name: str | None = Field(default=None, alias="lastName")

class OrderCreateParamsOrder(BaseModel):
    """OrderCreateOrderInput object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    line_items: list[OrderCreateParamsOrderLineitemsItem] = Field(alias="lineItems", description="Line items for the order")
    """Line items for the order"""
    customer_id: str | None = Field(default=None, alias="customerId", description="GraphQL GID of the customer")
    """GraphQL GID of the customer"""
    email: str | None = Field(default=None, description="Customer email")
    """Customer email"""
    note: str | None = Field(default=None, description="Order note")
    """Order note"""
    tags: list[str] | None = Field(default=None, description="Order tags")
    """Order tags"""
    shipping_address: OrderCreateParamsOrderShippingaddress | None = Field(default=None, alias="shippingAddress")

class OrderCreateParamsOptions(BaseModel):
    """OrderCreateOptionsInput"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inventory_behaviour: str | None = Field(default=None, alias="inventoryBehaviour")

class OrderCreateParams(BaseModel):
    """Parameters for creating an order.
Use line items with variantId and quantity.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    order: OrderCreateParamsOrder
    options: OrderCreateParamsOptions | None = Field(default=None)

class OrderUpdateParamsInputShippingaddress(BaseModel):
    """Nested schema for OrderUpdateParamsInput.shippingAddress"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address1: str | None = Field(default=None)
    city: str | None = Field(default=None)
    province_code: str | None = Field(default=None, alias="provinceCode")
    zip: str | None = Field(default=None)
    country_code: str | None = Field(default=None, alias="countryCode")

class OrderUpdateParamsInput(BaseModel):
    """Nested schema for OrderUpdateParams.input"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str = Field(description="The GraphQL GID of the order (e.g. gid://shopify/Order/123)")
    """The GraphQL GID of the order (e.g. gid://shopify/Order/123)"""
    email: str | None = Field(default=None, description="Customer email")
    """Customer email"""
    note: str | None = Field(default=None, description="Order note")
    """Order note"""
    tags: list[str] | None = Field(default=None, description="Order tags")
    """Order tags"""
    shipping_address: OrderUpdateParamsInputShippingaddress | None = Field(default=None, alias="shippingAddress")

class OrderUpdateParams(BaseModel):
    """Parameters for updating an order. The input.id field is required.
For line item changes, use orderEditBegin/orderEditCommit instead.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    input: OrderUpdateParamsInput

class OrderCancelParams(BaseModel):
    """Parameters for cancelling an order. This action is irreversible.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    order_id: str = Field(alias="orderId")
    reason: str
    notify_customer: bool | None = Field(default=None, alias="notifyCustomer")
    refund: bool | None = Field(default=None)
    restock: bool
    staff_note: str | None = Field(default=None, alias="staffNote")

class GraphQLOrderTotalpricesetShopmoney(BaseModel):
    """Nested schema for GraphQLOrderTotalpriceset.shopMoney"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None = Field(default=None)
    currency_code: str | None = Field(default=None, alias="currencyCode")

class GraphQLOrderTotalpriceset(BaseModel):
    """Nested schema for GraphQLOrder.totalPriceSet"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    shop_money: GraphQLOrderTotalpricesetShopmoney | None = Field(default=None, alias="shopMoney")

class GraphQLOrder(BaseModel):
    """GraphQLOrder type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    display_financial_status: str | None = Field(default=None, alias="displayFinancialStatus")
    display_fulfillment_status: str | None = Field(default=None, alias="displayFulfillmentStatus")
    total_price_set: GraphQLOrderTotalpriceset | None = Field(default=None, alias="totalPriceSet")

class OrderCreatePayload(BaseModel):
    """OrderCreatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    order: GraphQLOrder | None = Field(default=None)

class OrderUpdatePayloadOrder(BaseModel):
    """Nested schema for OrderUpdatePayload.order"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None | None = Field(default=None)
    email: str | None | None = Field(default=None)
    note: str | None | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    created_at: str | None | None = Field(default=None, alias="createdAt")
    display_financial_status: str | None | None = Field(default=None, alias="displayFinancialStatus")
    display_fulfillment_status: str | None | None = Field(default=None, alias="displayFulfillmentStatus")

class OrderUpdatePayload(BaseModel):
    """OrderUpdatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    order: OrderUpdatePayloadOrder | None = Field(default=None)

class OrderCancelPayloadJob(BaseModel):
    """Nested schema for OrderCancelPayload.job"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    done: bool | None = Field(default=None)

class OrderCancelPayload(BaseModel):
    """OrderCancelPayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    order_cancel_user_errors: list[GraphQLUserError] | None = Field(default=None, alias="orderCancelUserErrors")
    job: OrderCancelPayloadJob | None = Field(default=None)

class OrderMutationResponseData(BaseModel):
    """Nested schema for OrderMutationResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    order_create: OrderCreatePayload | None = Field(default=None, alias="orderCreate")

class OrderMutationResponse(BaseModel):
    """OrderMutationResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: OrderMutationResponseData | None = Field(default=None)

class OrderUpdateResponseData(BaseModel):
    """Nested schema for OrderUpdateResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    order_update: OrderUpdatePayload | None = Field(default=None, alias="orderUpdate")

class OrderUpdateResponse(BaseModel):
    """OrderUpdateResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: OrderUpdateResponseData | None = Field(default=None)

class OrderCancelResponseData(BaseModel):
    """Nested schema for OrderCancelResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    order_cancel: OrderCancelPayload | None = Field(default=None, alias="orderCancel")

class OrderCancelResponse(BaseModel):
    """OrderCancelResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: OrderCancelResponseData | None = Field(default=None)

class DraftOrderCreateParamsInputLineitemsItem(BaseModel):
    """Nested schema for DraftOrderCreateParamsInput.lineItems_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    variant_id: str | None = Field(default=None, alias="variantId", description="GraphQL GID of the product variant")
    """GraphQL GID of the product variant"""
    quantity: int | None = Field(default=None, description="Quantity")
    """Quantity"""
    title: str | None = Field(default=None, description="Custom title")
    """Custom title"""
    original_unit_price: str | None = Field(default=None, alias="originalUnitPrice", description="Unit price")
    """Unit price"""

class DraftOrderCreateParamsInputShippingaddress(BaseModel):
    """Nested schema for DraftOrderCreateParamsInput.shippingAddress"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address1: str | None = Field(default=None)
    city: str | None = Field(default=None)
    province_code: str | None = Field(default=None, alias="provinceCode")
    zip: str | None = Field(default=None)
    country_code: str | None = Field(default=None, alias="countryCode")

class DraftOrderCreateParamsInput(BaseModel):
    """DraftOrderInput object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    line_items: list[DraftOrderCreateParamsInputLineitemsItem] | None = Field(default=None, alias="lineItems", description="Line items for the draft order")
    """Line items for the draft order"""
    customer_id: str | None = Field(default=None, alias="customerId", description="GraphQL GID of the customer")
    """GraphQL GID of the customer"""
    email: str | None = Field(default=None, description="Customer email")
    """Customer email"""
    note: str | None = Field(default=None, description="Draft order note")
    """Draft order note"""
    tags: list[str] | None = Field(default=None)
    shipping_address: DraftOrderCreateParamsInputShippingaddress | None = Field(default=None, alias="shippingAddress")

class DraftOrderCreateParams(BaseModel):
    """Parameters for creating a draft order."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    input: DraftOrderCreateParamsInput

class DraftOrderUpdateParamsInputLineitemsItem(BaseModel):
    """Nested schema for DraftOrderUpdateParamsInput.lineItems_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    variant_id: str | None = Field(default=None, alias="variantId")
    quantity: int | None = Field(default=None)
    title: str | None = Field(default=None)
    original_unit_price: str | None = Field(default=None, alias="originalUnitPrice")

class DraftOrderUpdateParamsInput(BaseModel):
    """DraftOrderInput object with updated fields"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    line_items: list[DraftOrderUpdateParamsInputLineitemsItem] | None = Field(default=None, alias="lineItems")
    email: str | None = Field(default=None)
    note: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)

class DraftOrderUpdateParams(BaseModel):
    """Parameters for updating a draft order."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    input: DraftOrderUpdateParamsInput

class DraftOrderDeleteParamsInput(BaseModel):
    """Nested schema for DraftOrderDeleteParams.input"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str = Field(description="The GraphQL GID of the draft order to delete")
    """The GraphQL GID of the draft order to delete"""

class DraftOrderDeleteParams(BaseModel):
    """Parameters for deleting a draft order. Only open draft orders can be deleted."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    input: DraftOrderDeleteParamsInput

class DraftOrderCompleteParams(BaseModel):
    """Parameters for completing a draft order, converting it to a regular order."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    payment_pending: bool | None = Field(default=None, alias="paymentPending")

class GraphQLDraftOrder(BaseModel):
    """GraphQLDraftOrder type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    status: str | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    total_price: str | None = Field(default=None, alias="totalPrice")
    currency_code: str | None = Field(default=None, alias="currencyCode")

class DraftOrderCreatePayload(BaseModel):
    """DraftOrderCreatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    draft_order: GraphQLDraftOrder | None = Field(default=None, alias="draftOrder")

class DraftOrderUpdatePayload(BaseModel):
    """DraftOrderUpdatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    draft_order: GraphQLDraftOrder | None = Field(default=None, alias="draftOrder")

class DraftOrderDeletePayload(BaseModel):
    """DraftOrderDeletePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    deleted_id: str | None = Field(default=None, alias="deletedId")

class DraftOrderCompletePayloadDraftorderOrder(BaseModel):
    """Nested schema for DraftOrderCompletePayloadDraftorder.order"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None | None = Field(default=None)

class DraftOrderCompletePayloadDraftorder(BaseModel):
    """Nested schema for DraftOrderCompletePayload.draftOrder"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None | None = Field(default=None)
    status: str | None | None = Field(default=None)
    order: DraftOrderCompletePayloadDraftorderOrder | None | None = Field(default=None)

class DraftOrderCompletePayload(BaseModel):
    """DraftOrderCompletePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    draft_order: DraftOrderCompletePayloadDraftorder | None = Field(default=None, alias="draftOrder")

class DraftOrderMutationResponseData(BaseModel):
    """Nested schema for DraftOrderMutationResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    draft_order_create: DraftOrderCreatePayload | None = Field(default=None, alias="draftOrderCreate")
    draft_order_update: DraftOrderUpdatePayload | None = Field(default=None, alias="draftOrderUpdate")

class DraftOrderMutationResponse(BaseModel):
    """DraftOrderMutationResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: DraftOrderMutationResponseData | None = Field(default=None)

class DraftOrderDeleteResponseData(BaseModel):
    """Nested schema for DraftOrderDeleteResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    draft_order_delete: DraftOrderDeletePayload | None = Field(default=None, alias="draftOrderDelete")

class DraftOrderDeleteResponse(BaseModel):
    """DraftOrderDeleteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: DraftOrderDeleteResponseData | None = Field(default=None)

class DraftOrderCompleteResponseData(BaseModel):
    """Nested schema for DraftOrderCompleteResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    draft_order_complete: DraftOrderCompletePayload | None = Field(default=None, alias="draftOrderComplete")

class DraftOrderCompleteResponse(BaseModel):
    """DraftOrderCompleteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: DraftOrderCompleteResponseData | None = Field(default=None)

class InventorySetQuantitiesParamsInputQuantitiesItem(BaseModel):
    """Nested schema for InventorySetQuantitiesParamsInput.quantities_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inventory_item_id: str = Field(alias="inventoryItemId", description="GraphQL GID of the inventory item")
    """GraphQL GID of the inventory item"""
    location_id: str = Field(alias="locationId", description="GraphQL GID of the location")
    """GraphQL GID of the location"""
    quantity: int = Field(description="Absolute quantity to set")
    """Absolute quantity to set"""

class InventorySetQuantitiesParamsInput(BaseModel):
    """Nested schema for InventorySetQuantitiesParams.input"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str = Field(description="Quantity name (e.g. 'available', 'on_hand')")
    """Quantity name (e.g. 'available', 'on_hand')"""
    reason: str = Field(description="Reason for the adjustment (e.g. 'correction', 'other')")
    """Reason for the adjustment (e.g. 'correction', 'other')"""
    reference_document_uri: str | None = Field(default=None, alias="referenceDocumentUri", description="URI for the reference document")
    """URI for the reference document"""
    quantities: list[InventorySetQuantitiesParamsInputQuantitiesItem] = Field(description="Quantities to set")
    """Quantities to set"""

class InventorySetQuantitiesParams(BaseModel):
    """Parameters for setting absolute inventory quantities.
Requires a reason and reference document URI.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    input: InventorySetQuantitiesParamsInput

class InventoryAdjustQuantitiesParamsInputChangesItem(BaseModel):
    """Nested schema for InventoryAdjustQuantitiesParamsInput.changes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inventory_item_id: str = Field(alias="inventoryItemId", description="GraphQL GID of the inventory item")
    """GraphQL GID of the inventory item"""
    location_id: str = Field(alias="locationId", description="GraphQL GID of the location")
    """GraphQL GID of the location"""
    delta: int = Field(description="Amount to adjust (positive to add, negative to subtract)")
    """Amount to adjust (positive to add, negative to subtract)"""

class InventoryAdjustQuantitiesParamsInput(BaseModel):
    """Nested schema for InventoryAdjustQuantitiesParams.input"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str = Field(description="Quantity name (e.g. 'available')")
    """Quantity name (e.g. 'available')"""
    reason: str = Field(description="Reason for the adjustment")
    """Reason for the adjustment"""
    reference_document_uri: str | None = Field(default=None, alias="referenceDocumentUri", description="URI for the reference document")
    """URI for the reference document"""
    changes: list[InventoryAdjustQuantitiesParamsInputChangesItem] = Field(description="Inventory changes to apply")
    """Inventory changes to apply"""

class InventoryAdjustQuantitiesParams(BaseModel):
    """Parameters for adjusting inventory quantities relatively (add/subtract)."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    input: InventoryAdjustQuantitiesParamsInput

class InventoryAdjustmentGroupChangesItem(BaseModel):
    """Nested schema for InventoryAdjustmentGroup.changes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    delta: int | None | None = Field(default=None)
    quantity_after_change: int | None | None = Field(default=None, alias="quantityAfterChange")

class InventoryAdjustmentGroup(BaseModel):
    """InventoryAdjustmentGroup type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reason: str | None = Field(default=None)
    reference_document_uri: str | None = Field(default=None, alias="referenceDocumentUri")
    changes: list[InventoryAdjustmentGroupChangesItem] | None = Field(default=None)

class InventorySetQuantitiesPayload(BaseModel):
    """InventorySetQuantitiesPayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    inventory_adjustment_group: InventoryAdjustmentGroup | None = Field(default=None, alias="inventoryAdjustmentGroup")

class InventoryAdjustQuantitiesPayload(BaseModel):
    """InventoryAdjustQuantitiesPayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    inventory_adjustment_group: InventoryAdjustmentGroup | None = Field(default=None, alias="inventoryAdjustmentGroup")

class InventorySetQuantitiesResponseData(BaseModel):
    """Nested schema for InventorySetQuantitiesResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inventory_set_quantities: InventorySetQuantitiesPayload | None = Field(default=None, alias="inventorySetQuantities")

class InventorySetQuantitiesResponse(BaseModel):
    """InventorySetQuantitiesResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: InventorySetQuantitiesResponseData | None = Field(default=None)

class InventoryAdjustQuantitiesResponseData(BaseModel):
    """Nested schema for InventoryAdjustQuantitiesResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inventory_adjust_quantities: InventoryAdjustQuantitiesPayload | None = Field(default=None, alias="inventoryAdjustQuantities")

class InventoryAdjustQuantitiesResponse(BaseModel):
    """InventoryAdjustQuantitiesResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: InventoryAdjustQuantitiesResponseData | None = Field(default=None)

class DiscountCodeCreateParamsBasiccodediscountCustomerselection(BaseModel):
    """Which customers can use this discount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    all: bool | None = Field(default=None, description="Set to true for all customers")
    """Set to true for all customers"""

class DiscountCodeCreateParamsBasiccodediscountCustomergetsValueDiscountamount(BaseModel):
    """Nested schema for DiscountCodeCreateParamsBasiccodediscountCustomergetsValue.discountAmount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None = Field(default=None)
    applies_on_each_item: bool | None = Field(default=None, alias="appliesOnEachItem")

class DiscountCodeCreateParamsBasiccodediscountCustomergetsValue(BaseModel):
    """The discount value"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    percentage: float | None = Field(default=None, description="Percentage discount (e.g. 0.1 for 10%)")
    """Percentage discount (e.g. 0.1 for 10%)"""
    discount_amount: DiscountCodeCreateParamsBasiccodediscountCustomergetsValueDiscountamount | None = Field(default=None, alias="discountAmount")

class DiscountCodeCreateParamsBasiccodediscountCustomergetsItems(BaseModel):
    """Which items the discount applies to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    all: bool | None = Field(default=None, description="Set to true for all items")
    """Set to true for all items"""

class DiscountCodeCreateParamsBasiccodediscountCustomergets(BaseModel):
    """What the customer gets from this discount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: DiscountCodeCreateParamsBasiccodediscountCustomergetsValue | None = Field(default=None, description="The discount value")
    """The discount value"""
    items: DiscountCodeCreateParamsBasiccodediscountCustomergetsItems | None = Field(default=None, description="Which items the discount applies to")
    """Which items the discount applies to"""

class DiscountCodeCreateParamsBasiccodediscount(BaseModel):
    """Nested schema for DiscountCodeCreateParams.basicCodeDiscount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str = Field(description="Discount title")
    """Discount title"""
    code: str = Field(description="Discount code that customers enter at checkout")
    """Discount code that customers enter at checkout"""
    starts_at: str = Field(alias="startsAt", description="When the discount starts (ISO 8601)")
    """When the discount starts (ISO 8601)"""
    ends_at: str | None = Field(default=None, alias="endsAt", description="When the discount ends (ISO 8601, optional)")
    """When the discount ends (ISO 8601, optional)"""
    usage_limit: int | None = Field(default=None, alias="usageLimit", description="Maximum number of times the discount can be used")
    """Maximum number of times the discount can be used"""
    customer_selection: DiscountCodeCreateParamsBasiccodediscountCustomerselection = Field(alias="customerSelection", description="Which customers can use this discount")
    """Which customers can use this discount"""
    customer_gets: DiscountCodeCreateParamsBasiccodediscountCustomergets = Field(alias="customerGets", description="What the customer gets from this discount")
    """What the customer gets from this discount"""

class DiscountCodeCreateParams(BaseModel):
    """Parameters for creating a basic discount code.
Supports percentage or fixed amount discounts.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    basic_code_discount: DiscountCodeCreateParamsBasiccodediscount = Field(alias="basicCodeDiscount")

class DiscountCodeUpdateParamsBasiccodediscount(BaseModel):
    """Nested schema for DiscountCodeUpdateParams.basicCodeDiscount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None = Field(default=None)
    code: str | None = Field(default=None)
    starts_at: str | None = Field(default=None, alias="startsAt")
    ends_at: str | None = Field(default=None, alias="endsAt")
    usage_limit: int | None = Field(default=None, alias="usageLimit")

class DiscountCodeUpdateParams(BaseModel):
    """Parameters for updating a basic discount code."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    basic_code_discount: DiscountCodeUpdateParamsBasiccodediscount = Field(alias="basicCodeDiscount")

class DiscountCodeDeleteParams(BaseModel):
    """Parameters for deleting a discount code."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str

class DiscountCodeBasicCreatePayloadCodediscountnodeCodediscountCodesNodesItem(BaseModel):
    """Nested schema for DiscountCodeBasicCreatePayloadCodediscountnodeCodediscountCodes.nodes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    code: str | None = Field(default=None)

class DiscountCodeBasicCreatePayloadCodediscountnodeCodediscountCodes(BaseModel):
    """Nested schema for DiscountCodeBasicCreatePayloadCodediscountnodeCodediscount.codes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    nodes: list[DiscountCodeBasicCreatePayloadCodediscountnodeCodediscountCodesNodesItem] | None = Field(default=None)

class DiscountCodeBasicCreatePayloadCodediscountnodeCodediscount(BaseModel):
    """Nested schema for DiscountCodeBasicCreatePayloadCodediscountnode.codeDiscount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None | None = Field(default=None)
    summary: str | None | None = Field(default=None)
    starts_at: str | None | None = Field(default=None, alias="startsAt")
    ends_at: str | None | None = Field(default=None, alias="endsAt")
    status: str | None | None = Field(default=None)
    codes: DiscountCodeBasicCreatePayloadCodediscountnodeCodediscountCodes | None = Field(default=None)

class DiscountCodeBasicCreatePayloadCodediscountnode(BaseModel):
    """Nested schema for DiscountCodeBasicCreatePayload.codeDiscountNode"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    code_discount: DiscountCodeBasicCreatePayloadCodediscountnodeCodediscount | None = Field(default=None, alias="codeDiscount")

class DiscountCodeBasicCreatePayload(BaseModel):
    """DiscountCodeBasicCreatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    code_discount_node: DiscountCodeBasicCreatePayloadCodediscountnode | None = Field(default=None, alias="codeDiscountNode")

class DiscountCodeBasicUpdatePayloadCodediscountnodeCodediscountCodesNodesItem(BaseModel):
    """Nested schema for DiscountCodeBasicUpdatePayloadCodediscountnodeCodediscountCodes.nodes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    code: str | None = Field(default=None)

class DiscountCodeBasicUpdatePayloadCodediscountnodeCodediscountCodes(BaseModel):
    """Nested schema for DiscountCodeBasicUpdatePayloadCodediscountnodeCodediscount.codes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    nodes: list[DiscountCodeBasicUpdatePayloadCodediscountnodeCodediscountCodesNodesItem] | None = Field(default=None)

class DiscountCodeBasicUpdatePayloadCodediscountnodeCodediscount(BaseModel):
    """Nested schema for DiscountCodeBasicUpdatePayloadCodediscountnode.codeDiscount"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None | None = Field(default=None)
    summary: str | None | None = Field(default=None)
    starts_at: str | None | None = Field(default=None, alias="startsAt")
    ends_at: str | None | None = Field(default=None, alias="endsAt")
    status: str | None | None = Field(default=None)
    codes: DiscountCodeBasicUpdatePayloadCodediscountnodeCodediscountCodes | None = Field(default=None)

class DiscountCodeBasicUpdatePayloadCodediscountnode(BaseModel):
    """Nested schema for DiscountCodeBasicUpdatePayload.codeDiscountNode"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    code_discount: DiscountCodeBasicUpdatePayloadCodediscountnodeCodediscount | None = Field(default=None, alias="codeDiscount")

class DiscountCodeBasicUpdatePayload(BaseModel):
    """DiscountCodeBasicUpdatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    code_discount_node: DiscountCodeBasicUpdatePayloadCodediscountnode | None = Field(default=None, alias="codeDiscountNode")

class DiscountCodeDeletePayload(BaseModel):
    """DiscountCodeDeletePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    deleted_code_discount_id: str | None = Field(default=None, alias="deletedCodeDiscountId")

class DiscountCodeMutationResponseData(BaseModel):
    """Nested schema for DiscountCodeMutationResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    discount_code_basic_create: DiscountCodeBasicCreatePayload | None = Field(default=None, alias="discountCodeBasicCreate")
    discount_code_basic_update: DiscountCodeBasicUpdatePayload | None = Field(default=None, alias="discountCodeBasicUpdate")

class DiscountCodeMutationResponse(BaseModel):
    """DiscountCodeMutationResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: DiscountCodeMutationResponseData | None = Field(default=None)

class DiscountCodeDeleteResponseData(BaseModel):
    """Nested schema for DiscountCodeDeleteResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    discount_code_delete: DiscountCodeDeletePayload | None = Field(default=None, alias="discountCodeDelete")

class DiscountCodeDeleteResponse(BaseModel):
    """DiscountCodeDeleteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: DiscountCodeDeleteResponseData | None = Field(default=None)

class MetafieldsSetParamsMetafieldsItem(BaseModel):
    """Nested schema for MetafieldsSetParams.metafields_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    namespace: str = Field(description="Metafield namespace (e.g. 'custom')")
    """Metafield namespace (e.g. 'custom')"""
    key: str = Field(description="Metafield key (e.g. 'color')")
    """Metafield key (e.g. 'color')"""
    type_: str = Field(alias="type", description="Metafield type (e.g. 'single_line_text_field', 'number_integer', 'boolean')")
    """Metafield type (e.g. 'single_line_text_field', 'number_integer', 'boolean')"""
    value: str = Field(description="Metafield value")
    """Metafield value"""
    owner_id: str = Field(alias="ownerId", description="GraphQL GID of the owner resource (e.g. gid://shopify/Product/123)")
    """GraphQL GID of the owner resource (e.g. gid://shopify/Product/123)"""

class MetafieldsSetParams(BaseModel):
    """Parameters for setting (creating or updating) metafields atomically.
Supports up to 25 metafields per call.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    metafields: list[MetafieldsSetParamsMetafieldsItem]

class MetafieldDeleteParamsMetafieldsItem(BaseModel):
    """Nested schema for MetafieldDeleteParams.metafields_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    owner_id: str = Field(alias="ownerId", description="GraphQL GID of the owner resource (e.g. gid://shopify/Product/123)")
    """GraphQL GID of the owner resource (e.g. gid://shopify/Product/123)"""
    namespace: str = Field(description="Metafield namespace (e.g. 'custom')")
    """Metafield namespace (e.g. 'custom')"""
    key: str = Field(description="Metafield key (e.g. 'color')")
    """Metafield key (e.g. 'color')"""

class MetafieldDeleteParams(BaseModel):
    """Parameters for deleting metafields. Identify each metafield by
ownerId + namespace + key.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    metafields: list[MetafieldDeleteParamsMetafieldsItem]

class MetafieldsSetPayloadMetafieldsItem(BaseModel):
    """Nested schema for MetafieldsSetPayload.metafields_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    namespace: str | None | None = Field(default=None)
    key: str | None | None = Field(default=None)
    value: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")

class MetafieldsSetPayload(BaseModel):
    """MetafieldsSetPayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    metafields: list[MetafieldsSetPayloadMetafieldsItem] | None = Field(default=None)

class MetafieldDeletePayloadDeletedmetafieldsItem(BaseModel):
    """Nested schema for MetafieldDeletePayload.deletedMetafields_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    key: str | None | None = Field(default=None)
    namespace: str | None | None = Field(default=None)
    owner_id: str | None | None = Field(default=None, alias="ownerId")

class MetafieldDeletePayload(BaseModel):
    """MetafieldDeletePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    deleted_metafields: list[MetafieldDeletePayloadDeletedmetafieldsItem | None] | None = Field(default=None, alias="deletedMetafields")
    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")

class MetafieldsSetResponseData(BaseModel):
    """Nested schema for MetafieldsSetResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    metafields_set: MetafieldsSetPayload | None = Field(default=None, alias="metafieldsSet")

class MetafieldsSetResponse(BaseModel):
    """MetafieldsSetResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: MetafieldsSetResponseData | None = Field(default=None)

class MetafieldDeleteResponseData(BaseModel):
    """Nested schema for MetafieldDeleteResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    metafields_delete: MetafieldDeletePayload | None = Field(default=None, alias="metafieldsDelete")

class MetafieldDeleteResponse(BaseModel):
    """MetafieldDeleteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: MetafieldDeleteResponseData | None = Field(default=None)

class CollectionCreateParamsInputRulesetRulesItem(BaseModel):
    """Nested schema for CollectionCreateParamsInputRuleset.rules_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    column: str | None = Field(default=None, description="Rule column (e.g. TAG, TITLE, VENDOR)")
    """Rule column (e.g. TAG, TITLE, VENDOR)"""
    relation: str | None = Field(default=None, description="Rule relation (e.g. EQUALS, CONTAINS)")
    """Rule relation (e.g. EQUALS, CONTAINS)"""
    condition: str | None = Field(default=None, description="Rule condition value")
    """Rule condition value"""

class CollectionCreateParamsInputRuleset(BaseModel):
    """Rule set for smart collections"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    applied_disjunctively: bool | None = Field(default=None, alias="appliedDisjunctively", description="Whether rules are OR (true) or AND (false)")
    """Whether rules are OR (true) or AND (false)"""
    rules: list[CollectionCreateParamsInputRulesetRulesItem] | None = Field(default=None)

class CollectionCreateParamsInput(BaseModel):
    """Nested schema for CollectionCreateParams.input"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str = Field(description="Collection title")
    """Collection title"""
    description_html: str | None = Field(default=None, alias="descriptionHtml", description="Collection description in HTML")
    """Collection description in HTML"""
    handle: str | None = Field(default=None, description="URL handle for the collection")
    """URL handle for the collection"""
    sort_order: str | None = Field(default=None, alias="sortOrder", description="Sort order for products")
    """Sort order for products"""
    template_suffix: str | None = Field(default=None, alias="templateSuffix", description="Liquid template suffix")
    """Liquid template suffix"""
    rule_set: CollectionCreateParamsInputRuleset | None = Field(default=None, alias="ruleSet", description="Rule set for smart collections")
    """Rule set for smart collections"""

class CollectionCreateParams(BaseModel):
    """Parameters for creating a collection (custom or smart)."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    input: CollectionCreateParamsInput

class CollectionUpdateParamsInput(BaseModel):
    """Nested schema for CollectionUpdateParams.input"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str = Field(description="The GraphQL GID of the collection")
    """The GraphQL GID of the collection"""
    title: str | None = Field(default=None)
    description_html: str | None = Field(default=None, alias="descriptionHtml")
    handle: str | None = Field(default=None)
    sort_order: str | None = Field(default=None, alias="sortOrder")

class CollectionUpdateParams(BaseModel):
    """Parameters for updating a collection."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    input: CollectionUpdateParamsInput

class CollectionDeleteParamsInput(BaseModel):
    """Nested schema for CollectionDeleteParams.input"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str = Field(description="The GraphQL GID of the collection to delete")
    """The GraphQL GID of the collection to delete"""

class CollectionDeleteParams(BaseModel):
    """Parameters for deleting a collection."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    input: CollectionDeleteParamsInput

class CollectionCreatePayloadCollection(BaseModel):
    """Nested schema for CollectionCreatePayload.collection"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None | None = Field(default=None)
    handle: str | None | None = Field(default=None)
    description_html: str | None | None = Field(default=None, alias="descriptionHtml")
    sort_order: str | None | None = Field(default=None, alias="sortOrder")
    template_suffix: str | None | None = Field(default=None, alias="templateSuffix")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")

class CollectionCreatePayload(BaseModel):
    """CollectionCreatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    collection: CollectionCreatePayloadCollection | None = Field(default=None)

class CollectionUpdatePayloadCollection(BaseModel):
    """Nested schema for CollectionUpdatePayload.collection"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None | None = Field(default=None)
    handle: str | None | None = Field(default=None)
    description_html: str | None | None = Field(default=None, alias="descriptionHtml")
    sort_order: str | None | None = Field(default=None, alias="sortOrder")
    template_suffix: str | None | None = Field(default=None, alias="templateSuffix")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")

class CollectionUpdatePayload(BaseModel):
    """CollectionUpdatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    collection: CollectionUpdatePayloadCollection | None = Field(default=None)

class CollectionDeletePayload(BaseModel):
    """CollectionDeletePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    deleted_collection_id: str | None = Field(default=None, alias="deletedCollectionId")

class CollectionMutationResponseData(BaseModel):
    """Nested schema for CollectionMutationResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    collection_create: CollectionCreatePayload | None = Field(default=None, alias="collectionCreate")
    collection_update: CollectionUpdatePayload | None = Field(default=None, alias="collectionUpdate")

class CollectionMutationResponse(BaseModel):
    """CollectionMutationResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: CollectionMutationResponseData | None = Field(default=None)

class CollectionDeleteResponseData(BaseModel):
    """Nested schema for CollectionDeleteResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    collection_delete: CollectionDeletePayload | None = Field(default=None, alias="collectionDelete")

class CollectionDeleteResponse(BaseModel):
    """CollectionDeleteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: CollectionDeleteResponseData | None = Field(default=None)

class PageCreateParamsPage(BaseModel):
    """Nested schema for PageCreateParams.page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str = Field(description="Page title")
    """Page title"""
    body: str | None = Field(default=None, description="Page body content (HTML)")
    """Page body content (HTML)"""
    handle: str | None = Field(default=None, description="URL handle for the page")
    """URL handle for the page"""
    is_published: bool | None = Field(default=None, alias="isPublished", description="Whether the page is published")
    """Whether the page is published"""

class PageCreateParams(BaseModel):
    """Parameters for creating a page."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page: PageCreateParamsPage

class PageUpdateParamsPage(BaseModel):
    """Nested schema for PageUpdateParams.page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None = Field(default=None)
    body: str | None = Field(default=None)
    handle: str | None = Field(default=None)
    is_published: bool | None = Field(default=None, alias="isPublished")

class PageUpdateParams(BaseModel):
    """Parameters for updating a page."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    page: PageUpdateParamsPage

class PageDeleteParams(BaseModel):
    """Parameters for deleting a page."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str

class GraphQLPage(BaseModel):
    """GraphQLPage type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    handle: str | None = Field(default=None)
    body: str | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class PageCreatePayload(BaseModel):
    """PageCreatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    page: GraphQLPage | None = Field(default=None)

class PageUpdatePayload(BaseModel):
    """PageUpdatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    page: GraphQLPage | None = Field(default=None)

class PageDeletePayload(BaseModel):
    """PageDeletePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    deleted_page_id: str | None = Field(default=None, alias="deletedPageId")

class PageMutationResponseData(BaseModel):
    """Nested schema for PageMutationResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_create: PageCreatePayload | None = Field(default=None, alias="pageCreate")
    page_update: PageUpdatePayload | None = Field(default=None, alias="pageUpdate")

class PageMutationResponse(BaseModel):
    """PageMutationResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: PageMutationResponseData | None = Field(default=None)

class PageDeleteResponseData(BaseModel):
    """Nested schema for PageDeleteResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_delete: PageDeletePayload | None = Field(default=None, alias="pageDelete")

class PageDeleteResponse(BaseModel):
    """PageDeleteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: PageDeleteResponseData | None = Field(default=None)

class BlogCreateParamsBlog(BaseModel):
    """Nested schema for BlogCreateParams.blog"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str = Field(description="Blog title")
    """Blog title"""
    handle: str | None = Field(default=None, description="URL handle for the blog")
    """URL handle for the blog"""

class BlogCreateParams(BaseModel):
    """Parameters for creating a blog."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    blog: BlogCreateParamsBlog

class BlogUpdateParamsBlog(BaseModel):
    """Nested schema for BlogUpdateParams.blog"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None = Field(default=None)
    handle: str | None = Field(default=None)

class BlogUpdateParams(BaseModel):
    """Parameters for updating a blog."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    blog: BlogUpdateParamsBlog

class BlogDeleteParams(BaseModel):
    """Parameters for deleting a blog."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str

class GraphQLBlog(BaseModel):
    """GraphQLBlog type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    handle: str | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")

class BlogCreatePayload(BaseModel):
    """BlogCreatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    blog: GraphQLBlog | None = Field(default=None)

class BlogUpdatePayload(BaseModel):
    """BlogUpdatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    blog: GraphQLBlog | None = Field(default=None)

class BlogDeletePayload(BaseModel):
    """BlogDeletePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    deleted_blog_id: str | None = Field(default=None, alias="deletedBlogId")

class BlogMutationResponseData(BaseModel):
    """Nested schema for BlogMutationResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    blog_create: BlogCreatePayload | None = Field(default=None, alias="blogCreate")
    blog_update: BlogUpdatePayload | None = Field(default=None, alias="blogUpdate")

class BlogMutationResponse(BaseModel):
    """BlogMutationResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: BlogMutationResponseData | None = Field(default=None)

class BlogDeleteResponseData(BaseModel):
    """Nested schema for BlogDeleteResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    blog_delete: BlogDeletePayload | None = Field(default=None, alias="blogDelete")

class BlogDeleteResponse(BaseModel):
    """BlogDeleteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: BlogDeleteResponseData | None = Field(default=None)

class ArticleCreateParamsArticleAuthor(BaseModel):
    """Author of the article. Required by Shopify's articleCreate mutation (ArticleCreateInput.author is non-null)."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str = Field(description="Author display name. Required (provide the author's name).")
    """Author display name. Required (provide the author's name)."""

class ArticleCreateParamsArticle(BaseModel):
    """Nested schema for ArticleCreateParams.article"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str = Field(description="Article title")
    """Article title"""
    blog_id: str = Field(alias="blogId", description="GraphQL GID of the blog this article belongs to")
    """GraphQL GID of the blog this article belongs to"""
    body: str | None = Field(default=None, description="Article body content (HTML)")
    """Article body content (HTML)"""
    handle: str | None = Field(default=None, description="URL handle for the article")
    """URL handle for the article"""
    is_published: bool | None = Field(default=None, alias="isPublished", description="Whether the article is published")
    """Whether the article is published"""
    tags: list[str] | None = Field(default=None)
    author: ArticleCreateParamsArticleAuthor = Field(description="Author of the article. Required by Shopify's articleCreate mutation (ArticleCreateInput.author is non-null).")
    """Author of the article. Required by Shopify's articleCreate mutation (ArticleCreateInput.author is non-null)."""

class ArticleCreateParams(BaseModel):
    """Parameters for creating a blog article."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    article: ArticleCreateParamsArticle

class ArticleUpdateParamsArticle(BaseModel):
    """Nested schema for ArticleUpdateParams.article"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None = Field(default=None)
    body: str | None = Field(default=None)
    handle: str | None = Field(default=None)
    is_published: bool | None = Field(default=None, alias="isPublished")
    tags: list[str] | None = Field(default=None)

class ArticleUpdateParams(BaseModel):
    """Parameters for updating a blog article."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    article: ArticleUpdateParamsArticle

class ArticleDeleteParams(BaseModel):
    """Parameters for deleting a blog article."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str

class GraphQLArticleBlog(BaseModel):
    """Nested schema for GraphQLArticle.blog"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None | None = Field(default=None)

class GraphQLArticle(BaseModel):
    """GraphQLArticle type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    handle: str | None = Field(default=None)
    body: str | None = Field(default=None)
    blog: GraphQLArticleBlog | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class ArticleCreatePayload(BaseModel):
    """ArticleCreatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    article: GraphQLArticle | None = Field(default=None)

class ArticleUpdatePayload(BaseModel):
    """ArticleUpdatePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    article: GraphQLArticle | None = Field(default=None)

class ArticleDeletePayload(BaseModel):
    """ArticleDeletePayload type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_errors: list[GraphQLUserError] | None = Field(default=None, alias="userErrors")
    deleted_article_id: str | None = Field(default=None, alias="deletedArticleId")

class ArticleMutationResponseData(BaseModel):
    """Nested schema for ArticleMutationResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    article_create: ArticleCreatePayload | None = Field(default=None, alias="articleCreate")
    article_update: ArticleUpdatePayload | None = Field(default=None, alias="articleUpdate")

class ArticleMutationResponse(BaseModel):
    """ArticleMutationResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: ArticleMutationResponseData | None = Field(default=None)

class ArticleDeleteResponseData(BaseModel):
    """Nested schema for ArticleDeleteResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    article_delete: ArticleDeletePayload | None = Field(default=None, alias="articleDelete")

class ArticleDeleteResponse(BaseModel):
    """ArticleDeleteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: ArticleDeleteResponseData | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class CustomersListResultMeta(BaseModel):
    """Metadata for customers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class OrdersListResultMeta(BaseModel):
    """Metadata for orders.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class ProductsListResultMeta(BaseModel):
    """Metadata for products.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class ProductVariantsListResultMeta(BaseModel):
    """Metadata for product_variants.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class ProductImagesListResultMeta(BaseModel):
    """Metadata for product_images.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class AbandonedCheckoutsListResultMeta(BaseModel):
    """Metadata for abandoned_checkouts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class LocationsListResultMeta(BaseModel):
    """Metadata for locations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class InventoryLevelsListResultMeta(BaseModel):
    """Metadata for inventory_levels.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class InventoryItemsListResultMeta(BaseModel):
    """Metadata for inventory_items.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class PriceRulesListResultMeta(BaseModel):
    """Metadata for price_rules.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class DiscountCodesListResultMeta(BaseModel):
    """Metadata for discount_codes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class CustomCollectionsListResultMeta(BaseModel):
    """Metadata for custom_collections.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class SmartCollectionsListResultMeta(BaseModel):
    """Metadata for smart_collections.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class CollectsListResultMeta(BaseModel):
    """Metadata for collects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class DraftOrdersListResultMeta(BaseModel):
    """Metadata for draft_orders.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class FulfillmentsListResultMeta(BaseModel):
    """Metadata for fulfillments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class OrderRefundsListResultMeta(BaseModel):
    """Metadata for order_refunds.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class TransactionsListResultMeta(BaseModel):
    """Metadata for transactions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class TenderTransactionsListResultMeta(BaseModel):
    """Metadata for tender_transactions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class CountriesListResultMeta(BaseModel):
    """Metadata for countries.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class MetafieldShopsListResultMeta(BaseModel):
    """Metadata for metafield_shops.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class MetafieldCustomersListResultMeta(BaseModel):
    """Metadata for metafield_customers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class MetafieldProductsListResultMeta(BaseModel):
    """Metadata for metafield_products.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class MetafieldOrdersListResultMeta(BaseModel):
    """Metadata for metafield_orders.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class MetafieldDraftOrdersListResultMeta(BaseModel):
    """Metadata for metafield_draft_orders.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class MetafieldLocationsListResultMeta(BaseModel):
    """Metadata for metafield_locations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class MetafieldProductVariantsListResultMeta(BaseModel):
    """Metadata for metafield_product_variants.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class MetafieldSmartCollectionsListResultMeta(BaseModel):
    """Metadata for metafield_smart_collections.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class MetafieldProductImagesListResultMeta(BaseModel):
    """Metadata for metafield_product_images.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class CustomerAddressListResultMeta(BaseModel):
    """Metadata for customer_address.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class FulfillmentOrdersListResultMeta(BaseModel):
    """Metadata for fulfillment_orders.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class PagesListResultMeta(BaseModel):
    """Metadata for pages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class BlogsListResultMeta(BaseModel):
    """Metadata for blogs.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class ArticlesListResultMeta(BaseModel):
    """Metadata for articles.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class BalanceTransactionsListResultMeta(BaseModel):
    """Metadata for balance_transactions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class DisputesListResultMeta(BaseModel):
    """Metadata for disputes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class MetafieldPagesListResultMeta(BaseModel):
    """Metadata for metafield_pages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class MetafieldBlogsListResultMeta(BaseModel):
    """Metadata for metafield_blogs.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

class MetafieldArticlesListResultMeta(BaseModel):
    """Metadata for metafield_articles.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class ShopifyCheckResult(BaseModel):
    """Result of a health check operation.

    Returned by the check() method to indicate connectivity and credential status.
    """
    model_config = ConfigDict(extra="forbid")

    status: str
    """Health check status: 'healthy' or 'unhealthy'."""
    error: str | None = None
    """Error message if status is 'unhealthy', None otherwise."""
    checked_entity: str | None = None
    """Entity name used for the health check."""
    checked_action: str | None = None
    """Action name used for the health check."""


# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class ShopifyExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class ShopifyExecuteResultWithMeta(ShopifyExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AbandonedCheckoutsSearchData(BaseModel):
    """Search result data for abandoned_checkouts entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the abandoned checkout"""
    token: str | None = None
    """Unique token identifying the checkout"""
    email: str | None = None
    """Email address provided for the checkout"""
    phone: str | None = None
    """Phone number provided for the checkout"""
    name: str | None = None
    """Shopify-assigned display name for the checkout (e.g. `#C12345`)"""
    currency: str | None = None
    """ISO 4217 currency code for the checkout totals"""
    total_price: str | None = None
    """Total price of the checkout in the shop's currency"""
    created_at: str | None = None
    """ISO 8601 timestamp when the checkout was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the checkout was last updated"""
    completed_at: str | None = None
    """ISO 8601 timestamp when the checkout was completed, if applicable"""


class CollectsSearchData(BaseModel):
    """Search result data for collects entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the collect"""
    collection_id: int | None = None
    """Identifier of the collection the product belongs to"""
    product_id: int | None = None
    """Identifier of the product in the collection"""
    position: int | None = None
    """Position of the product within the collection"""
    created_at: str | None = None
    """ISO 8601 timestamp when the collect was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the collect was last updated"""


class CountriesSearchData(BaseModel):
    """Search result data for countries entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the country tax row"""
    name: str | None = None
    """Human-readable country name"""
    code: str | None = None
    """ISO 3166-1 alpha-2 country code"""
    tax_name: str | None = None
    """Localized name of the tax applied in this country"""


class CustomCollectionsSearchData(BaseModel):
    """Search result data for custom_collections entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the custom collection"""
    handle: str | None = None
    """URL-friendly handle for the custom collection"""
    title: str | None = None
    """Display title of the custom collection"""
    sort_order: str | None = None
    """How products are sorted within the collection (e.g. `best-selling`)"""
    published_scope: str | None = None
    """Publishing scope (`web` or `global`)"""
    published_at: str | None = None
    """ISO 8601 timestamp when the collection was published"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the collection was last updated"""


class CustomersSearchData(BaseModel):
    """Search result data for customers entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the customer"""
    email: str | None = None
    """Primary email address of the customer"""
    phone: str | None = None
    """Primary phone number of the customer"""
    first_name: str | None = None
    """First name of the customer"""
    last_name: str | None = None
    """Last name of the customer"""
    state: str | None = None
    """Account state (`disabled`, `invited`, `enabled`, `declined`)"""
    orders_count: int | None = None
    """Number of orders placed by the customer"""
    total_spent: str | None = None
    """Total lifetime amount spent by the customer"""
    currency: str | None = None
    """ISO 4217 currency code for the customer's total spend"""
    created_at: str | None = None
    """ISO 8601 timestamp when the customer record was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the customer record was last updated"""


class DiscountCodesSearchData(BaseModel):
    """Search result data for discount_codes entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the discount code"""
    price_rule_id: int | None = None
    """Identifier of the parent price rule"""
    code: str | None = None
    """Discount code string shoppers enter at checkout"""
    usage_count: int | None = None
    """Number of times the code has been redeemed"""
    created_at: str | None = None
    """ISO 8601 timestamp when the code was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the code was last updated"""


class DraftOrdersSearchData(BaseModel):
    """Search result data for draft_orders entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the draft order"""
    name: str | None = None
    """Shopify-assigned display name for the draft order (e.g. `#D12345`)"""
    email: str | None = None
    """Email address associated with the draft order"""
    status: str | None = None
    """Status of the draft order (`open`, `invoice_sent`, `completed`)"""
    currency: str | None = None
    """ISO 4217 currency code for the draft order totals"""
    total_price: str | None = None
    """Total price of the draft order"""
    order_id: int | None = None
    """Identifier of the completed order, if the draft has been completed"""
    created_at: str | None = None
    """ISO 8601 timestamp when the draft order was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the draft order was last updated"""
    completed_at: str | None = None
    """ISO 8601 timestamp when the draft order was completed, if applicable"""


class FulfillmentOrdersSearchData(BaseModel):
    """Search result data for fulfillment_orders entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the fulfillment order"""
    order_id: int | None = None
    """Identifier of the parent order"""
    shop_id: int | None = None
    """Identifier of the shop that owns the fulfillment order"""
    assigned_location_id: int | None = None
    """Identifier of the location assigned to fulfill the order"""
    status: str | None = None
    """Fulfillment order status (e.g. `open`, `in_progress`, `closed`)"""
    request_status: str | None = None
    """Status of the fulfillment request (e.g. `unsubmitted`, `submitted`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the fulfillment order was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the fulfillment order was last updated"""


class FulfillmentsSearchData(BaseModel):
    """Search result data for fulfillments entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the fulfillment"""
    order_id: int | None = None
    """Identifier of the parent order"""
    status: str | None = None
    """Fulfillment status (e.g. `pending`, `open`, `success`, `cancelled`)"""
    shipment_status: str | None = None
    """Carrier shipment status (e.g. `delivered`, `in_transit`)"""
    tracking_company: str | None = None
    """Name of the shipping carrier"""
    tracking_number: str | None = None
    """Primary tracking number for the shipment"""
    location_id: int | None = None
    """Identifier of the fulfilling location"""
    created_at: str | None = None
    """ISO 8601 timestamp when the fulfillment was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the fulfillment was last updated"""


class InventoryItemsSearchData(BaseModel):
    """Search result data for inventory_items entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the inventory item"""
    sku: str | None = None
    """Stock keeping unit associated with the inventory item"""
    tracked: bool | None = None
    """Whether Shopify is tracking inventory for this item"""
    requires_shipping: bool | None = None
    """Whether the item requires shipping"""
    country_code_of_origin: str | None = None
    """ISO country code of the item's country of origin"""
    created_at: str | None = None
    """ISO 8601 timestamp when the inventory item was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the inventory item was last updated"""


class InventoryLevelsSearchData(BaseModel):
    """Search result data for inventory_levels entity."""
    model_config = ConfigDict(extra="allow")

    inventory_item_id: int | None = None
    """Identifier of the inventory item"""
    location_id: int | None = None
    """Identifier of the location holding the inventory"""
    available: int | None = None
    """Number of units available at the location"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the inventory level was last updated"""


class LocationsSearchData(BaseModel):
    """Search result data for locations entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the location"""
    name: str | None = None
    """Display name of the location"""
    address1: str | None = None
    """Primary street address of the location"""
    city: str | None = None
    """City of the location"""
    province: str | None = None
    """Province, state, or region of the location"""
    country: str | None = None
    """Country name of the location"""
    country_code: str | None = None
    """ISO 3166-1 alpha-2 country code of the location"""
    phone: str | None = None
    """Phone number for the location"""
    active: bool | None = None
    """Whether the location is currently active"""
    created_at: str | None = None
    """ISO 8601 timestamp when the location was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the location was last updated"""


class MetafieldCustomersSearchData(BaseModel):
    """Search result data for metafield_customers entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the metafield"""
    namespace: str | None = None
    """Namespace group for the metafield"""
    key: str | None = None
    """Key of the metafield within its namespace"""
    value: str | None = None
    """Serialized value stored in the metafield"""
    type_: str | None = None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None = None
    """Human-readable description of the metafield"""
    owner_id: int | None = None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None = None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldDraftOrdersSearchData(BaseModel):
    """Search result data for metafield_draft_orders entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the metafield"""
    namespace: str | None = None
    """Namespace group for the metafield"""
    key: str | None = None
    """Key of the metafield within its namespace"""
    value: str | None = None
    """Serialized value stored in the metafield"""
    type_: str | None = None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None = None
    """Human-readable description of the metafield"""
    owner_id: int | None = None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None = None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldLocationsSearchData(BaseModel):
    """Search result data for metafield_locations entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the metafield"""
    namespace: str | None = None
    """Namespace group for the metafield"""
    key: str | None = None
    """Key of the metafield within its namespace"""
    value: str | None = None
    """Serialized value stored in the metafield"""
    type_: str | None = None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None = None
    """Human-readable description of the metafield"""
    owner_id: int | None = None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None = None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldOrdersSearchData(BaseModel):
    """Search result data for metafield_orders entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the metafield"""
    namespace: str | None = None
    """Namespace group for the metafield"""
    key: str | None = None
    """Key of the metafield within its namespace"""
    value: str | None = None
    """Serialized value stored in the metafield"""
    type_: str | None = None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None = None
    """Human-readable description of the metafield"""
    owner_id: int | None = None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None = None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductImagesSearchData(BaseModel):
    """Search result data for metafield_product_images entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the metafield"""
    namespace: str | None = None
    """Namespace group for the metafield"""
    key: str | None = None
    """Key of the metafield within its namespace"""
    value: str | None = None
    """Serialized value stored in the metafield"""
    type_: str | None = None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None = None
    """Human-readable description of the metafield"""
    owner_id: int | None = None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None = None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductVariantsSearchData(BaseModel):
    """Search result data for metafield_product_variants entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the metafield"""
    namespace: str | None = None
    """Namespace group for the metafield"""
    key: str | None = None
    """Key of the metafield within its namespace"""
    value: str | None = None
    """Serialized value stored in the metafield"""
    type_: str | None = None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None = None
    """Human-readable description of the metafield"""
    owner_id: int | None = None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None = None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductsSearchData(BaseModel):
    """Search result data for metafield_products entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the metafield"""
    namespace: str | None = None
    """Namespace group for the metafield"""
    key: str | None = None
    """Key of the metafield within its namespace"""
    value: str | None = None
    """Serialized value stored in the metafield"""
    type_: str | None = None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None = None
    """Human-readable description of the metafield"""
    owner_id: int | None = None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None = None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldShopsSearchData(BaseModel):
    """Search result data for metafield_shops entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the metafield"""
    namespace: str | None = None
    """Namespace group for the metafield"""
    key: str | None = None
    """Key of the metafield within its namespace"""
    value: str | None = None
    """Serialized value stored in the metafield"""
    type_: str | None = None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None = None
    """Human-readable description of the metafield"""
    owner_id: int | None = None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None = None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldSmartCollectionsSearchData(BaseModel):
    """Search result data for metafield_smart_collections entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the metafield"""
    namespace: str | None = None
    """Namespace group for the metafield"""
    key: str | None = None
    """Key of the metafield within its namespace"""
    value: str | None = None
    """Serialized value stored in the metafield"""
    type_: str | None = None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None = None
    """Human-readable description of the metafield"""
    owner_id: int | None = None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None = None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the metafield was last updated"""


class OrderRefundsSearchData(BaseModel):
    """Search result data for order_refunds entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the refund"""
    order_id: int | None = None
    """Identifier of the refunded order"""
    user_id: int | None = None
    """Identifier of the staff user who processed the refund"""
    note: str | None = None
    """Merchant-provided note explaining the refund"""
    created_at: str | None = None
    """ISO 8601 timestamp when the refund was created"""
    processed_at: str | None = None
    """ISO 8601 timestamp when the refund was processed"""


class OrdersSearchData(BaseModel):
    """Search result data for orders entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the order"""
    name: str | None = None
    """Shopify-assigned display name for the order (e.g. `#1001`)"""
    email: str | None = None
    """Email address associated with the order"""
    phone: str | None = None
    """Phone number associated with the order"""
    order_number: int | None = None
    """Sequential order number displayed in the Shopify admin"""
    financial_status: str | None = None
    """Payment status of the order (e.g. `paid`, `pending`, `refunded`, `partially_refunded`)"""
    fulfillment_status: str | None = None
    """Fulfillment status of the order (e.g. `fulfilled`, `partial`, `null` for unfulfilled)"""
    currency: str | None = None
    """ISO 4217 currency code for the order totals"""
    total_price: str | None = None
    """Total price of the order including taxes and discounts"""
    subtotal_price: str | None = None
    """Subtotal of the order before shipping and taxes"""
    total_tax: str | None = None
    """Total tax amount applied to the order"""
    total_discounts: str | None = None
    """Total discount amount applied to the order"""
    total_weight: int | None = None
    """Total weight of all items in the order, in grams"""
    cancel_reason: str | None = None
    """Reason the order was cancelled, if applicable"""
    cancelled_at: str | None = None
    """ISO 8601 timestamp when the order was cancelled, if applicable"""
    closed_at: str | None = None
    """ISO 8601 timestamp when the order was closed, if applicable"""
    tags: str | None = None
    """Comma-separated tags attached to the order"""
    note: str | None = None
    """Merchant-provided note on the order"""
    processed_at: str | None = None
    """ISO 8601 timestamp when the order was processed"""
    created_at: str | None = None
    """ISO 8601 timestamp when the order was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the order was last updated"""


class PriceRulesSearchData(BaseModel):
    """Search result data for price_rules entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the price rule"""
    title: str | None = None
    """Administrative title of the price rule"""
    value_type: str | None = None
    """How the discount value is interpreted (`fixed_amount` or `percentage`)"""
    value: str | None = None
    """Discount value applied by the rule"""
    target_type: str | None = None
    """Type of target the rule applies to (`line_item` or `shipping_line`)"""
    target_selection: str | None = None
    """Which target items the rule applies to (`all` or `entitled`)"""
    allocation_method: str | None = None
    """How the discount is allocated (`each` or `across`)"""
    starts_at: str | None = None
    """ISO 8601 timestamp when the rule starts being active"""
    ends_at: str | None = None
    """ISO 8601 timestamp when the rule stops being active, if applicable"""
    created_at: str | None = None
    """ISO 8601 timestamp when the rule was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the rule was last updated"""


class ProductImagesSearchData(BaseModel):
    """Search result data for product_images entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the product image"""
    product_id: int | None = None
    """Identifier of the product the image belongs to"""
    position: int | None = None
    """Display position of the image within the product"""
    alt: str | None = None
    """Alt text for the image"""
    width: int | None = None
    """Image width in pixels"""
    height: int | None = None
    """Image height in pixels"""
    src: str | None = None
    """Public URL of the image"""
    created_at: str | None = None
    """ISO 8601 timestamp when the image was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the image was last updated"""


class ProductsSearchData(BaseModel):
    """Search result data for products entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the product"""
    title: str | None = None
    """Product title"""
    body_html: str | None = None
    """Product description in HTML"""
    vendor: str | None = None
    """Product vendor or manufacturer"""
    product_type: str | None = None
    """Product type used for categorization"""
    handle: str | None = None
    """URL-friendly handle for the product"""
    status: str | None = None
    """Product status (`active`, `archived`, or `draft`)"""
    tags: str | None = None
    """Comma-separated tags attached to the product"""
    published_scope: str | None = None
    """Publishing scope (`web` or `global`)"""
    published_at: str | None = None
    """ISO 8601 timestamp when the product was published"""
    created_at: str | None = None
    """ISO 8601 timestamp when the product was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the product was last updated"""


class ProductVariantsSearchData(BaseModel):
    """Search result data for product_variants entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the product variant"""
    product_id: int | None = None
    """Identifier of the parent product"""
    title: str | None = None
    """Display title of the variant"""
    sku: str | None = None
    """Stock keeping unit for the variant"""
    price: str | None = None
    """Price of the variant in the shop's currency"""
    compare_at_price: str | None = None
    """Original (compare-at) price of the variant, if set"""
    position: int | None = None
    """Display position of the variant within the product"""
    inventory_policy: str | None = None
    """Behaviour when out of stock (`deny` or `continue`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the variant was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the variant was last updated"""


class ShopSearchData(BaseModel):
    """Search result data for shop entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the shop"""
    name: str | None = None
    """Display name of the shop"""
    email: str | None = None
    """Primary contact email for the shop"""
    domain: str | None = None
    """Custom domain configured for the shop, if any"""
    myshopify_domain: str | None = None
    """Canonical `*.myshopify.com` domain for the shop"""
    country_code: str | None = None
    """ISO 3166-1 alpha-2 country code of the shop"""
    currency: str | None = None
    """ISO 4217 currency code used by the shop"""
    timezone: str | None = None
    """Timezone configured for the shop (e.g. `(GMT-05:00) Eastern Time`)"""
    plan_name: str | None = None
    """Shopify plan identifier (e.g. `shopify_plus`, `basic`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the shop was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the shop was last updated"""


class SmartCollectionsSearchData(BaseModel):
    """Search result data for smart_collections entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the smart collection"""
    handle: str | None = None
    """URL-friendly handle for the smart collection"""
    title: str | None = None
    """Display title of the smart collection"""
    sort_order: str | None = None
    """How products are sorted within the collection"""
    published_scope: str | None = None
    """Publishing scope (`web` or `global`)"""
    published_at: str | None = None
    """ISO 8601 timestamp when the collection was published"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the collection was last updated"""


class TenderTransactionsSearchData(BaseModel):
    """Search result data for tender_transactions entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the tender transaction"""
    order_id: int | None = None
    """Identifier of the order the transaction belongs to"""
    user_id: int | None = None
    """Identifier of the staff user who processed the transaction"""
    amount: str | None = None
    """Amount of the transaction in the shop's currency"""
    currency: str | None = None
    """ISO 4217 currency code for the transaction amount"""
    payment_method: str | None = None
    """Payment method used (e.g. `credit_card`, `paypal`)"""
    test: bool | None = None
    """Whether the transaction was a test transaction"""
    processed_at: str | None = None
    """ISO 8601 timestamp when the transaction was processed"""


class PagesSearchData(BaseModel):
    """Search result data for pages entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the page"""
    title: str | None = None
    """Title of the page"""
    handle: str | None = None
    """URL-friendly handle for the page"""
    author: str | None = None
    """Name of the page author"""
    body_html: str | None = None
    """HTML content of the page"""
    published_at: str | None = None
    """ISO 8601 timestamp when the page was published"""
    created_at: str | None = None
    """ISO 8601 timestamp when the page was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the page was last updated"""


class BlogsSearchData(BaseModel):
    """Search result data for blogs entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the blog"""
    title: str | None = None
    """Title of the blog"""
    handle: str | None = None
    """URL-friendly handle for the blog"""
    commentable: str | None = None
    """Whether readers can post comments (no, moderate, yes)"""
    tags: str | None = None
    """Comma-separated tags from the blog's articles"""
    created_at: str | None = None
    """ISO 8601 timestamp when the blog was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the blog was last updated"""


class ArticlesSearchData(BaseModel):
    """Search result data for articles entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the article"""
    title: str | None = None
    """Title of the article"""
    handle: str | None = None
    """URL-friendly handle for the article"""
    author: str | None = None
    """Name of the author of the article"""
    blog_id: int | None = None
    """Identifier of the blog the article belongs to"""
    body_html: str | None = None
    """HTML content of the article body"""
    summary_html: str | None = None
    """Summary of the article in HTML"""
    tags: str | None = None
    """Comma-separated list of tags for the article"""
    published_at: str | None = None
    """ISO 8601 timestamp when the article was published"""
    created_at: str | None = None
    """ISO 8601 timestamp when the article was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the article was last updated"""


class BalanceTransactionsSearchData(BaseModel):
    """Search result data for balance_transactions entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier of the balance transaction"""
    type_: str | None = None
    """Type of the transaction (charge, refund, dispute, reserve, adjustment, credit, debit, payout, etc.)"""
    amount: str | None = None
    """Gross amount of the transaction"""
    fee: str | None = None
    """Total fees deducted from the transaction"""
    net: str | None = None
    """Net amount of the transaction"""
    currency: str | None = None
    """ISO 4217 currency code of the transaction"""
    payout_id: int | None = None
    """Identifier of the payout the transaction was paid out in"""
    payout_status: str | None = None
    """Status of the associated payout"""
    source_type: str | None = None
    """Type of the resource that led to this transaction"""
    source_order_id: int | None = None
    """Identifier of the source order, if applicable"""
    processed_at: str | None = None
    """ISO 8601 timestamp when the transaction was processed"""


class DisputesSearchData(BaseModel):
    """Search result data for disputes entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the dispute"""
    order_id: int | None = None
    """Identifier of the order the dispute belongs to"""
    type_: str | None = None
    """Whether the dispute is an inquiry or chargeback"""
    amount: str | None = None
    """Disputed amount"""
    currency: str | None = None
    """ISO 4217 currency code of the dispute amount"""
    reason: str | None = None
    """Reason for the dispute provided by the cardholder's bank"""
    network_reason_code: str | None = None
    """Network reason code from the cardholder's bank"""
    status: str | None = None
    """Current state of the dispute (needs_response, under_review, charge_refunded, accepted, won, lost)"""
    evidence_due_by: str | None = None
    """ISO 8601 deadline for evidence submission"""
    initiated_at: str | None = None
    """ISO 8601 timestamp when the dispute was initiated"""
    finalized_on: str | None = None
    """ISO 8601 timestamp when the dispute was resolved"""


class MetafieldPagesSearchData(BaseModel):
    """Search result data for metafield_pages entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the metafield"""
    namespace: str | None = None
    """Container namespace for the metafield"""
    key: str | None = None
    """Identifier key for the metafield"""
    value: str | None = None
    """The metafield value"""
    type_: str | None = None
    """The metafield's information type"""
    description: str | None = None
    """Human-readable description of the metafield"""
    owner_id: int | None = None
    """Identifier of the page that owns this metafield"""
    owner_resource: str | None = None
    """Resource type that owns this metafield (e.g. `page`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldBlogsSearchData(BaseModel):
    """Search result data for metafield_blogs entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the metafield"""
    namespace: str | None = None
    """Container namespace for the metafield"""
    key: str | None = None
    """Identifier key for the metafield"""
    value: str | None = None
    """The metafield value"""
    type_: str | None = None
    """The metafield's information type"""
    description: str | None = None
    """Human-readable description of the metafield"""
    owner_id: int | None = None
    """Identifier of the blog that owns this metafield"""
    owner_resource: str | None = None
    """Resource type that owns this metafield (e.g. `blog`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldArticlesSearchData(BaseModel):
    """Search result data for metafield_articles entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the metafield"""
    namespace: str | None = None
    """Container namespace for the metafield"""
    key: str | None = None
    """Identifier key for the metafield"""
    value: str | None = None
    """The metafield value"""
    type_: str | None = None
    """The metafield's information type"""
    description: str | None = None
    """Human-readable description of the metafield"""
    owner_id: int | None = None
    """Identifier of the article that owns this metafield"""
    owner_resource: str | None = None
    """Resource type that owns this metafield (e.g. `article`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the metafield was last updated"""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchMeta(BaseModel):
    """Pagination metadata for search responses."""
    model_config = ConfigDict(extra="allow")

    has_more: bool = False
    """Whether more results are available."""
    cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed records."""
    model_config = ConfigDict(extra="allow")

    data: list[D] = Field(default_factory=list)
    """List of matching records."""
    meta: AirbyteSearchMeta = Field(default_factory=AirbyteSearchMeta)
    """Pagination metadata."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

AbandonedCheckoutsSearchResult = AirbyteSearchResult[AbandonedCheckoutsSearchData]
"""Search result type for abandoned_checkouts entity."""

CollectsSearchResult = AirbyteSearchResult[CollectsSearchData]
"""Search result type for collects entity."""

CountriesSearchResult = AirbyteSearchResult[CountriesSearchData]
"""Search result type for countries entity."""

CustomCollectionsSearchResult = AirbyteSearchResult[CustomCollectionsSearchData]
"""Search result type for custom_collections entity."""

CustomersSearchResult = AirbyteSearchResult[CustomersSearchData]
"""Search result type for customers entity."""

DiscountCodesSearchResult = AirbyteSearchResult[DiscountCodesSearchData]
"""Search result type for discount_codes entity."""

DraftOrdersSearchResult = AirbyteSearchResult[DraftOrdersSearchData]
"""Search result type for draft_orders entity."""

FulfillmentOrdersSearchResult = AirbyteSearchResult[FulfillmentOrdersSearchData]
"""Search result type for fulfillment_orders entity."""

FulfillmentsSearchResult = AirbyteSearchResult[FulfillmentsSearchData]
"""Search result type for fulfillments entity."""

InventoryItemsSearchResult = AirbyteSearchResult[InventoryItemsSearchData]
"""Search result type for inventory_items entity."""

InventoryLevelsSearchResult = AirbyteSearchResult[InventoryLevelsSearchData]
"""Search result type for inventory_levels entity."""

LocationsSearchResult = AirbyteSearchResult[LocationsSearchData]
"""Search result type for locations entity."""

MetafieldCustomersSearchResult = AirbyteSearchResult[MetafieldCustomersSearchData]
"""Search result type for metafield_customers entity."""

MetafieldDraftOrdersSearchResult = AirbyteSearchResult[MetafieldDraftOrdersSearchData]
"""Search result type for metafield_draft_orders entity."""

MetafieldLocationsSearchResult = AirbyteSearchResult[MetafieldLocationsSearchData]
"""Search result type for metafield_locations entity."""

MetafieldOrdersSearchResult = AirbyteSearchResult[MetafieldOrdersSearchData]
"""Search result type for metafield_orders entity."""

MetafieldProductImagesSearchResult = AirbyteSearchResult[MetafieldProductImagesSearchData]
"""Search result type for metafield_product_images entity."""

MetafieldProductVariantsSearchResult = AirbyteSearchResult[MetafieldProductVariantsSearchData]
"""Search result type for metafield_product_variants entity."""

MetafieldProductsSearchResult = AirbyteSearchResult[MetafieldProductsSearchData]
"""Search result type for metafield_products entity."""

MetafieldShopsSearchResult = AirbyteSearchResult[MetafieldShopsSearchData]
"""Search result type for metafield_shops entity."""

MetafieldSmartCollectionsSearchResult = AirbyteSearchResult[MetafieldSmartCollectionsSearchData]
"""Search result type for metafield_smart_collections entity."""

OrderRefundsSearchResult = AirbyteSearchResult[OrderRefundsSearchData]
"""Search result type for order_refunds entity."""

OrdersSearchResult = AirbyteSearchResult[OrdersSearchData]
"""Search result type for orders entity."""

PriceRulesSearchResult = AirbyteSearchResult[PriceRulesSearchData]
"""Search result type for price_rules entity."""

ProductImagesSearchResult = AirbyteSearchResult[ProductImagesSearchData]
"""Search result type for product_images entity."""

ProductsSearchResult = AirbyteSearchResult[ProductsSearchData]
"""Search result type for products entity."""

ProductVariantsSearchResult = AirbyteSearchResult[ProductVariantsSearchData]
"""Search result type for product_variants entity."""

ShopSearchResult = AirbyteSearchResult[ShopSearchData]
"""Search result type for shop entity."""

SmartCollectionsSearchResult = AirbyteSearchResult[SmartCollectionsSearchData]
"""Search result type for smart_collections entity."""

TenderTransactionsSearchResult = AirbyteSearchResult[TenderTransactionsSearchData]
"""Search result type for tender_transactions entity."""

PagesSearchResult = AirbyteSearchResult[PagesSearchData]
"""Search result type for pages entity."""

BlogsSearchResult = AirbyteSearchResult[BlogsSearchData]
"""Search result type for blogs entity."""

ArticlesSearchResult = AirbyteSearchResult[ArticlesSearchData]
"""Search result type for articles entity."""

BalanceTransactionsSearchResult = AirbyteSearchResult[BalanceTransactionsSearchData]
"""Search result type for balance_transactions entity."""

DisputesSearchResult = AirbyteSearchResult[DisputesSearchData]
"""Search result type for disputes entity."""

MetafieldPagesSearchResult = AirbyteSearchResult[MetafieldPagesSearchData]
"""Search result type for metafield_pages entity."""

MetafieldBlogsSearchResult = AirbyteSearchResult[MetafieldBlogsSearchData]
"""Search result type for metafield_blogs entity."""

MetafieldArticlesSearchResult = AirbyteSearchResult[MetafieldArticlesSearchData]
"""Search result type for metafield_articles entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

CustomersListResult = ShopifyExecuteResultWithMeta[list[Customer], CustomersListResultMeta]
"""Result type for customers.list operation with data and metadata."""

OrdersListResult = ShopifyExecuteResultWithMeta[list[Order], OrdersListResultMeta]
"""Result type for orders.list operation with data and metadata."""

ProductsListResult = ShopifyExecuteResultWithMeta[list[Product], ProductsListResultMeta]
"""Result type for products.list operation with data and metadata."""

ProductVariantsListResult = ShopifyExecuteResultWithMeta[list[ProductVariant], ProductVariantsListResultMeta]
"""Result type for product_variants.list operation with data and metadata."""

ProductImagesListResult = ShopifyExecuteResultWithMeta[list[ProductImage], ProductImagesListResultMeta]
"""Result type for product_images.list operation with data and metadata."""

AbandonedCheckoutsListResult = ShopifyExecuteResultWithMeta[list[AbandonedCheckout], AbandonedCheckoutsListResultMeta]
"""Result type for abandoned_checkouts.list operation with data and metadata."""

LocationsListResult = ShopifyExecuteResultWithMeta[list[Location], LocationsListResultMeta]
"""Result type for locations.list operation with data and metadata."""

InventoryLevelsListResult = ShopifyExecuteResultWithMeta[list[InventoryLevel], InventoryLevelsListResultMeta]
"""Result type for inventory_levels.list operation with data and metadata."""

InventoryItemsListResult = ShopifyExecuteResultWithMeta[list[InventoryItem], InventoryItemsListResultMeta]
"""Result type for inventory_items.list operation with data and metadata."""

PriceRulesListResult = ShopifyExecuteResultWithMeta[list[PriceRule], PriceRulesListResultMeta]
"""Result type for price_rules.list operation with data and metadata."""

DiscountCodesListResult = ShopifyExecuteResultWithMeta[list[DiscountCode], DiscountCodesListResultMeta]
"""Result type for discount_codes.list operation with data and metadata."""

CustomCollectionsListResult = ShopifyExecuteResultWithMeta[list[CustomCollection], CustomCollectionsListResultMeta]
"""Result type for custom_collections.list operation with data and metadata."""

SmartCollectionsListResult = ShopifyExecuteResultWithMeta[list[SmartCollection], SmartCollectionsListResultMeta]
"""Result type for smart_collections.list operation with data and metadata."""

CollectsListResult = ShopifyExecuteResultWithMeta[list[Collect], CollectsListResultMeta]
"""Result type for collects.list operation with data and metadata."""

DraftOrdersListResult = ShopifyExecuteResultWithMeta[list[DraftOrder], DraftOrdersListResultMeta]
"""Result type for draft_orders.list operation with data and metadata."""

FulfillmentsListResult = ShopifyExecuteResultWithMeta[list[Fulfillment], FulfillmentsListResultMeta]
"""Result type for fulfillments.list operation with data and metadata."""

OrderRefundsListResult = ShopifyExecuteResultWithMeta[list[Refund], OrderRefundsListResultMeta]
"""Result type for order_refunds.list operation with data and metadata."""

TransactionsListResult = ShopifyExecuteResultWithMeta[list[Transaction], TransactionsListResultMeta]
"""Result type for transactions.list operation with data and metadata."""

TenderTransactionsListResult = ShopifyExecuteResultWithMeta[list[TenderTransaction], TenderTransactionsListResultMeta]
"""Result type for tender_transactions.list operation with data and metadata."""

CountriesListResult = ShopifyExecuteResultWithMeta[list[Country], CountriesListResultMeta]
"""Result type for countries.list operation with data and metadata."""

MetafieldShopsListResult = ShopifyExecuteResultWithMeta[list[Metafield], MetafieldShopsListResultMeta]
"""Result type for metafield_shops.list operation with data and metadata."""

MetafieldCustomersListResult = ShopifyExecuteResultWithMeta[list[Metafield], MetafieldCustomersListResultMeta]
"""Result type for metafield_customers.list operation with data and metadata."""

MetafieldProductsListResult = ShopifyExecuteResultWithMeta[list[Metafield], MetafieldProductsListResultMeta]
"""Result type for metafield_products.list operation with data and metadata."""

MetafieldOrdersListResult = ShopifyExecuteResultWithMeta[list[Metafield], MetafieldOrdersListResultMeta]
"""Result type for metafield_orders.list operation with data and metadata."""

MetafieldDraftOrdersListResult = ShopifyExecuteResultWithMeta[list[Metafield], MetafieldDraftOrdersListResultMeta]
"""Result type for metafield_draft_orders.list operation with data and metadata."""

MetafieldLocationsListResult = ShopifyExecuteResultWithMeta[list[Metafield], MetafieldLocationsListResultMeta]
"""Result type for metafield_locations.list operation with data and metadata."""

MetafieldProductVariantsListResult = ShopifyExecuteResultWithMeta[list[Metafield], MetafieldProductVariantsListResultMeta]
"""Result type for metafield_product_variants.list operation with data and metadata."""

MetafieldSmartCollectionsListResult = ShopifyExecuteResultWithMeta[list[Metafield], MetafieldSmartCollectionsListResultMeta]
"""Result type for metafield_smart_collections.list operation with data and metadata."""

MetafieldProductImagesListResult = ShopifyExecuteResultWithMeta[list[Metafield], MetafieldProductImagesListResultMeta]
"""Result type for metafield_product_images.list operation with data and metadata."""

CustomerAddressListResult = ShopifyExecuteResultWithMeta[list[CustomerAddress], CustomerAddressListResultMeta]
"""Result type for customer_address.list operation with data and metadata."""

FulfillmentOrdersListResult = ShopifyExecuteResultWithMeta[list[FulfillmentOrder], FulfillmentOrdersListResultMeta]
"""Result type for fulfillment_orders.list operation with data and metadata."""

PagesListResult = ShopifyExecuteResultWithMeta[list[Page], PagesListResultMeta]
"""Result type for pages.list operation with data and metadata."""

BlogsListResult = ShopifyExecuteResultWithMeta[list[Blog], BlogsListResultMeta]
"""Result type for blogs.list operation with data and metadata."""

ArticlesListResult = ShopifyExecuteResultWithMeta[list[Article], ArticlesListResultMeta]
"""Result type for articles.list operation with data and metadata."""

BalanceTransactionsListResult = ShopifyExecuteResultWithMeta[list[BalanceTransaction], BalanceTransactionsListResultMeta]
"""Result type for balance_transactions.list operation with data and metadata."""

DisputesListResult = ShopifyExecuteResultWithMeta[list[Dispute], DisputesListResultMeta]
"""Result type for disputes.list operation with data and metadata."""

MetafieldPagesListResult = ShopifyExecuteResultWithMeta[list[Metafield], MetafieldPagesListResultMeta]
"""Result type for metafield_pages.list operation with data and metadata."""

MetafieldBlogsListResult = ShopifyExecuteResultWithMeta[list[Metafield], MetafieldBlogsListResultMeta]
"""Result type for metafield_blogs.list operation with data and metadata."""

MetafieldArticlesListResult = ShopifyExecuteResultWithMeta[list[Metafield], MetafieldArticlesListResultMeta]
"""Result type for metafield_articles.list operation with data and metadata."""

