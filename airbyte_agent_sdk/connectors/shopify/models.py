"""
Pydantic models for shopify connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class ShopifyAuthConfig(BaseModel):
    """Access Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Shopify Admin API access token"""

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

PriceRulesSearchResult = AirbyteSearchResult[PriceRulesSearchData]
"""Search result type for price_rules entity."""

ProductImagesSearchResult = AirbyteSearchResult[ProductImagesSearchData]
"""Search result type for product_images entity."""

ProductVariantsSearchResult = AirbyteSearchResult[ProductVariantsSearchData]
"""Search result type for product_variants entity."""

ShopSearchResult = AirbyteSearchResult[ShopSearchData]
"""Search result type for shop entity."""

SmartCollectionsSearchResult = AirbyteSearchResult[SmartCollectionsSearchData]
"""Search result type for smart_collections entity."""

TenderTransactionsSearchResult = AirbyteSearchResult[TenderTransactionsSearchData]
"""Search result type for tender_transactions entity."""



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

