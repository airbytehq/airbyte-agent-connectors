"""
Pydantic models for shopify connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class ShopifyAuthConfig(BaseModel):
    """Access Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Shopify Admin API access token"""
    shop: str
    """Your Shopify store name (e.g., 'my-store' from my-store.myshopify.com)"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class CustomerAddress(BaseModel):
    """A customer address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    customer_id: Union[int | None, Any] = Field(default=None)
    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    company: Union[str | None, Any] = Field(default=None)
    address1: Union[str | None, Any] = Field(default=None)
    address2: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    province: Union[str | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)
    zip: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    province_code: Union[str | None, Any] = Field(default=None)
    country_code: Union[str | None, Any] = Field(default=None)
    country_name: Union[str | None, Any] = Field(default=None)
    default: Union[bool | None, Any] = Field(default=None)

class Customer(BaseModel):
    """A Shopify customer"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    accepts_marketing: Union[bool | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    orders_count: Union[int | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    total_spent: Union[str | None, Any] = Field(default=None)
    last_order_id: Union[int | None, Any] = Field(default=None)
    note: Union[str | None, Any] = Field(default=None)
    verified_email: Union[bool | None, Any] = Field(default=None)
    multipass_identifier: Union[str | None, Any] = Field(default=None)
    tax_exempt: Union[bool | None, Any] = Field(default=None)
    tags: Union[str | None, Any] = Field(default=None)
    last_order_name: Union[str | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    addresses: Union[list[CustomerAddress] | None, Any] = Field(default=None)
    accepts_marketing_updated_at: Union[str | None, Any] = Field(default=None)
    marketing_opt_in_level: Union[str | None, Any] = Field(default=None)
    tax_exemptions: Union[list[str] | None, Any] = Field(default=None)
    email_marketing_consent: Union[Any, Any] = Field(default=None)
    sms_marketing_consent: Union[Any, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)
    default_address: Union[Any, Any] = Field(default=None)

class CustomerList(BaseModel):
    """CustomerList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    customers: Union[list[Customer], Any] = Field(default=None)

class CustomerAddressList(BaseModel):
    """CustomerAddressList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    addresses: Union[list[CustomerAddress], Any] = Field(default=None)

class MarketingConsent(BaseModel):
    """MarketingConsent type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    state: Union[str | None, Any] = Field(default=None)
    opt_in_level: Union[str | None, Any] = Field(default=None)
    consent_updated_at: Union[str | None, Any] = Field(default=None)
    consent_collected_from: Union[str | None, Any] = Field(default=None)

class OrderAddress(BaseModel):
    """An address in an order (shipping or billing) - does not have id field"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    company: Union[str | None, Any] = Field(default=None)
    address1: Union[str | None, Any] = Field(default=None)
    address2: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    province: Union[str | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)
    zip: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    province_code: Union[str | None, Any] = Field(default=None)
    country_code: Union[str | None, Any] = Field(default=None)
    latitude: Union[float | None, Any] = Field(default=None)
    longitude: Union[float | None, Any] = Field(default=None)

class Transaction(BaseModel):
    """An order transaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    order_id: Union[int | None, Any] = Field(default=None)
    kind: Union[str | None, Any] = Field(default=None)
    gateway: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    message: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    test: Union[bool | None, Any] = Field(default=None)
    authorization: Union[str | None, Any] = Field(default=None)
    location_id: Union[int | None, Any] = Field(default=None)
    user_id: Union[int | None, Any] = Field(default=None)
    parent_id: Union[int | None, Any] = Field(default=None)
    processed_at: Union[str | None, Any] = Field(default=None)
    device_id: Union[int | None, Any] = Field(default=None)
    error_code: Union[str | None, Any] = Field(default=None)
    source_name: Union[str | None, Any] = Field(default=None)
    receipt: Union[dict[str, Any] | None, Any] = Field(default=None)
    currency_exchange_adjustment: Union[dict[str, Any] | None, Any] = Field(default=None)
    amount: Union[str | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    payment_id: Union[str | None, Any] = Field(default=None)
    total_unsettled_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    manual_payment_gateway: Union[bool | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)

class Refund(BaseModel):
    """An order refund"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    order_id: Union[int | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    note: Union[str | None, Any] = Field(default=None)
    user_id: Union[int | None, Any] = Field(default=None)
    processed_at: Union[str | None, Any] = Field(default=None)
    restock: Union[bool | None, Any] = Field(default=None)
    duties: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    total_duties_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    return_: Union[dict[str, Any] | None, Any] = Field(default=None, alias="return")
    refund_line_items: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    transactions: Union[list[Transaction] | None, Any] = Field(default=None)
    order_adjustments: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)
    refund_shipping_lines: Union[list[dict[str, Any]] | None, Any] = Field(default=None)

class LineItem(BaseModel):
    """LineItem type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)
    attributed_staffs: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    current_quantity: Union[int | None, Any] = Field(default=None)
    fulfillable_quantity: Union[int | None, Any] = Field(default=None)
    fulfillment_service: Union[str | None, Any] = Field(default=None)
    fulfillment_status: Union[str | None, Any] = Field(default=None)
    gift_card: Union[bool | None, Any] = Field(default=None)
    grams: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    price: Union[str | None, Any] = Field(default=None)
    price_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    product_exists: Union[bool | None, Any] = Field(default=None)
    product_id: Union[int | None, Any] = Field(default=None)
    properties: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    quantity: Union[int | None, Any] = Field(default=None)
    requires_shipping: Union[bool | None, Any] = Field(default=None)
    sku: Union[str | None, Any] = Field(default=None)
    taxable: Union[bool | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    total_discount: Union[str | None, Any] = Field(default=None)
    total_discount_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    variant_id: Union[int | None, Any] = Field(default=None)
    variant_inventory_management: Union[str | None, Any] = Field(default=None)
    variant_title: Union[str | None, Any] = Field(default=None)
    vendor: Union[str | None, Any] = Field(default=None)
    tax_lines: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    duties: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    discount_allocations: Union[list[dict[str, Any]] | None, Any] = Field(default=None)

class Fulfillment(BaseModel):
    """A fulfillment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    order_id: Union[int | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    service: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    tracking_company: Union[str | None, Any] = Field(default=None)
    shipment_status: Union[str | None, Any] = Field(default=None)
    location_id: Union[int | None, Any] = Field(default=None)
    origin_address: Union[dict[str, Any] | None, Any] = Field(default=None)
    line_items: Union[list[LineItem] | None, Any] = Field(default=None)
    tracking_number: Union[str | None, Any] = Field(default=None)
    tracking_numbers: Union[list[str] | None, Any] = Field(default=None)
    tracking_url: Union[str | None, Any] = Field(default=None)
    tracking_urls: Union[list[str] | None, Any] = Field(default=None)
    receipt: Union[dict[str, Any] | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)

class Order(BaseModel):
    """A Shopify order"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)
    app_id: Union[int | None, Any] = Field(default=None)
    browser_ip: Union[str | None, Any] = Field(default=None)
    buyer_accepts_marketing: Union[bool | None, Any] = Field(default=None)
    cancel_reason: Union[str | None, Any] = Field(default=None)
    cancelled_at: Union[str | None, Any] = Field(default=None)
    cart_token: Union[str | None, Any] = Field(default=None)
    checkout_id: Union[int | None, Any] = Field(default=None)
    checkout_token: Union[str | None, Any] = Field(default=None)
    client_details: Union[dict[str, Any] | None, Any] = Field(default=None)
    closed_at: Union[str | None, Any] = Field(default=None)
    company: Union[dict[str, Any] | None, Any] = Field(default=None)
    confirmation_number: Union[str | None, Any] = Field(default=None)
    confirmed: Union[bool | None, Any] = Field(default=None)
    contact_email: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    current_subtotal_price: Union[str | None, Any] = Field(default=None)
    current_subtotal_price_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    current_total_additional_fees_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    current_total_discounts: Union[str | None, Any] = Field(default=None)
    current_total_discounts_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    current_total_duties_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    current_total_price: Union[str | None, Any] = Field(default=None)
    current_total_price_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    current_total_tax: Union[str | None, Any] = Field(default=None)
    current_total_tax_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    customer: Union[Any, Any] = Field(default=None)
    customer_locale: Union[str | None, Any] = Field(default=None)
    device_id: Union[int | None, Any] = Field(default=None)
    discount_applications: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    discount_codes: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    estimated_taxes: Union[bool | None, Any] = Field(default=None)
    financial_status: Union[str | None, Any] = Field(default=None)
    fulfillment_status: Union[str | None, Any] = Field(default=None)
    fulfillments: Union[list[Fulfillment] | None, Any] = Field(default=None)
    gateway: Union[str | None, Any] = Field(default=None)
    landing_site: Union[str | None, Any] = Field(default=None)
    landing_site_ref: Union[str | None, Any] = Field(default=None)
    line_items: Union[list[LineItem] | None, Any] = Field(default=None)
    location_id: Union[int | None, Any] = Field(default=None)
    merchant_of_record_app_id: Union[int | None, Any] = Field(default=None)
    merchant_business_entity_id: Union[str | None, Any] = Field(default=None)
    duties_included: Union[bool | None, Any] = Field(default=None)
    total_cash_rounding_payment_adjustment_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    total_cash_rounding_refund_adjustment_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    payment_terms: Union[dict[str, Any] | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    note: Union[str | None, Any] = Field(default=None)
    note_attributes: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    number: Union[int | None, Any] = Field(default=None)
    order_number: Union[int | None, Any] = Field(default=None)
    order_status_url: Union[str | None, Any] = Field(default=None)
    original_total_additional_fees_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    original_total_duties_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    payment_gateway_names: Union[list[str] | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    po_number: Union[str | None, Any] = Field(default=None)
    presentment_currency: Union[str | None, Any] = Field(default=None)
    processed_at: Union[str | None, Any] = Field(default=None)
    reference: Union[str | None, Any] = Field(default=None)
    referring_site: Union[str | None, Any] = Field(default=None)
    refunds: Union[list[Refund] | None, Any] = Field(default=None)
    shipping_address: Union[Any, Any] = Field(default=None)
    shipping_lines: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    source_identifier: Union[str | None, Any] = Field(default=None)
    source_name: Union[str | None, Any] = Field(default=None)
    source_url: Union[str | None, Any] = Field(default=None)
    subtotal_price: Union[str | None, Any] = Field(default=None)
    subtotal_price_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    tags: Union[str | None, Any] = Field(default=None)
    tax_exempt: Union[bool | None, Any] = Field(default=None)
    tax_lines: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    taxes_included: Union[bool | None, Any] = Field(default=None)
    test: Union[bool | None, Any] = Field(default=None)
    token: Union[str | None, Any] = Field(default=None)
    total_discounts: Union[str | None, Any] = Field(default=None)
    total_discounts_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    total_line_items_price: Union[str | None, Any] = Field(default=None)
    total_line_items_price_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    total_outstanding: Union[str | None, Any] = Field(default=None)
    total_price: Union[str | None, Any] = Field(default=None)
    total_price_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    total_shipping_price_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    total_tax: Union[str | None, Any] = Field(default=None)
    total_tax_set: Union[dict[str, Any] | None, Any] = Field(default=None)
    total_tip_received: Union[str | None, Any] = Field(default=None)
    total_weight: Union[int | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    user_id: Union[int | None, Any] = Field(default=None)
    billing_address: Union[Any, Any] = Field(default=None)

class OrderList(BaseModel):
    """OrderList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    orders: Union[list[Order], Any] = Field(default=None)

class ProductImage(BaseModel):
    """A product image"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    product_id: Union[int | None, Any] = Field(default=None)
    position: Union[int | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    alt: Union[str | None, Any] = Field(default=None)
    width: Union[int | None, Any] = Field(default=None)
    height: Union[int | None, Any] = Field(default=None)
    src: Union[str | None, Any] = Field(default=None)
    variant_ids: Union[list[int] | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)

class ProductVariant(BaseModel):
    """A product variant"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    product_id: Union[int | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    price: Union[str | None, Any] = Field(default=None)
    sku: Union[str | None, Any] = Field(default=None)
    position: Union[int | None, Any] = Field(default=None)
    inventory_policy: Union[str | None, Any] = Field(default=None)
    compare_at_price: Union[str | None, Any] = Field(default=None)
    fulfillment_service: Union[str | None, Any] = Field(default=None)
    inventory_management: Union[str | None, Any] = Field(default=None)
    option1: Union[str | None, Any] = Field(default=None)
    option2: Union[str | None, Any] = Field(default=None)
    option3: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    taxable: Union[bool | None, Any] = Field(default=None)
    barcode: Union[str | None, Any] = Field(default=None)
    grams: Union[int | None, Any] = Field(default=None)
    image_id: Union[int | None, Any] = Field(default=None)
    weight: Union[float | None, Any] = Field(default=None)
    weight_unit: Union[str | None, Any] = Field(default=None)
    inventory_item_id: Union[int | None, Any] = Field(default=None)
    inventory_quantity: Union[int | None, Any] = Field(default=None)
    old_inventory_quantity: Union[int | None, Any] = Field(default=None)
    requires_shipping: Union[bool | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)

class Product(BaseModel):
    """A Shopify product"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    body_html: Union[str | None, Any] = Field(default=None)
    vendor: Union[str | None, Any] = Field(default=None)
    product_type: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    handle: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    published_at: Union[str | None, Any] = Field(default=None)
    template_suffix: Union[str | None, Any] = Field(default=None)
    published_scope: Union[str | None, Any] = Field(default=None)
    tags: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)
    variants: Union[list[ProductVariant] | None, Any] = Field(default=None)
    options: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    images: Union[list[ProductImage] | None, Any] = Field(default=None)
    image: Union[Any, Any] = Field(default=None)

class ProductList(BaseModel):
    """ProductList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    products: Union[list[Product], Any] = Field(default=None)

class ProductVariantList(BaseModel):
    """ProductVariantList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    variants: Union[list[ProductVariant], Any] = Field(default=None)

class ProductImageList(BaseModel):
    """ProductImageList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    images: Union[list[ProductImage], Any] = Field(default=None)

class AbandonedCheckout(BaseModel):
    """An abandoned checkout"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    token: Union[str | None, Any] = Field(default=None)
    cart_token: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    gateway: Union[str | None, Any] = Field(default=None)
    buyer_accepts_marketing: Union[bool | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    landing_site: Union[str | None, Any] = Field(default=None)
    note: Union[str | None, Any] = Field(default=None)
    note_attributes: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    referring_site: Union[str | None, Any] = Field(default=None)
    shipping_lines: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    taxes_included: Union[bool | None, Any] = Field(default=None)
    total_weight: Union[int | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    completed_at: Union[str | None, Any] = Field(default=None)
    closed_at: Union[str | None, Any] = Field(default=None)
    user_id: Union[int | None, Any] = Field(default=None)
    location_id: Union[int | None, Any] = Field(default=None)
    source_identifier: Union[str | None, Any] = Field(default=None)
    source_url: Union[str | None, Any] = Field(default=None)
    device_id: Union[int | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    customer_locale: Union[str | None, Any] = Field(default=None)
    line_items: Union[list[LineItem] | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    source: Union[str | None, Any] = Field(default=None)
    abandoned_checkout_url: Union[str | None, Any] = Field(default=None)
    discount_codes: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    tax_lines: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    source_name: Union[str | None, Any] = Field(default=None)
    presentment_currency: Union[str | None, Any] = Field(default=None)
    buyer_accepts_sms_marketing: Union[bool | None, Any] = Field(default=None)
    sms_marketing_phone: Union[str | None, Any] = Field(default=None)
    total_discounts: Union[str | None, Any] = Field(default=None)
    total_line_items_price: Union[str | None, Any] = Field(default=None)
    total_price: Union[str | None, Any] = Field(default=None)
    total_tax: Union[str | None, Any] = Field(default=None)
    subtotal_price: Union[str | None, Any] = Field(default=None)
    total_duties: Union[str | None, Any] = Field(default=None)
    billing_address: Union[Any, Any] = Field(default=None)
    shipping_address: Union[Any, Any] = Field(default=None)
    customer: Union[Any, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)

class AbandonedCheckoutList(BaseModel):
    """AbandonedCheckoutList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    checkouts: Union[list[AbandonedCheckout], Any] = Field(default=None)

class Location(BaseModel):
    """A store location"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    address1: Union[str | None, Any] = Field(default=None)
    address2: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    zip: Union[str | None, Any] = Field(default=None)
    province: Union[str | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    country_code: Union[str | None, Any] = Field(default=None)
    country_name: Union[str | None, Any] = Field(default=None)
    province_code: Union[str | None, Any] = Field(default=None)
    legacy: Union[bool | None, Any] = Field(default=None)
    active: Union[bool | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)
    localized_country_name: Union[str | None, Any] = Field(default=None)
    localized_province_name: Union[str | None, Any] = Field(default=None)

class LocationList(BaseModel):
    """LocationList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    locations: Union[list[Location], Any] = Field(default=None)

class InventoryLevel(BaseModel):
    """An inventory level"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inventory_item_id: Union[int, Any] = Field(default=None)
    location_id: Union[int | None, Any] = Field(default=None)
    available: Union[int | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)

class InventoryLevelList(BaseModel):
    """InventoryLevelList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inventory_levels: Union[list[InventoryLevel], Any] = Field(default=None)

class InventoryItem(BaseModel):
    """An inventory item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    sku: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    requires_shipping: Union[bool | None, Any] = Field(default=None)
    cost: Union[str | None, Any] = Field(default=None)
    country_code_of_origin: Union[str | None, Any] = Field(default=None)
    province_code_of_origin: Union[str | None, Any] = Field(default=None)
    harmonized_system_code: Union[str | None, Any] = Field(default=None)
    tracked: Union[bool | None, Any] = Field(default=None)
    country_harmonized_system_codes: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)

class InventoryItemList(BaseModel):
    """InventoryItemList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inventory_items: Union[list[InventoryItem], Any] = Field(default=None)

class Shop(BaseModel):
    """Shop configuration"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    domain: Union[str | None, Any] = Field(default=None)
    province: Union[str | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)
    address1: Union[str | None, Any] = Field(default=None)
    zip: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    source: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    latitude: Union[float | None, Any] = Field(default=None)
    longitude: Union[float | None, Any] = Field(default=None)
    primary_locale: Union[str | None, Any] = Field(default=None)
    address2: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    country_code: Union[str | None, Any] = Field(default=None)
    country_name: Union[str | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    customer_email: Union[str | None, Any] = Field(default=None)
    timezone: Union[str | None, Any] = Field(default=None)
    iana_timezone: Union[str | None, Any] = Field(default=None)
    shop_owner: Union[str | None, Any] = Field(default=None)
    money_format: Union[str | None, Any] = Field(default=None)
    money_with_currency_format: Union[str | None, Any] = Field(default=None)
    weight_unit: Union[str | None, Any] = Field(default=None)
    province_code: Union[str | None, Any] = Field(default=None)
    taxes_included: Union[bool | None, Any] = Field(default=None)
    auto_configure_tax_inclusivity: Union[bool | None, Any] = Field(default=None)
    tax_shipping: Union[bool | None, Any] = Field(default=None)
    county_taxes: Union[bool | None, Any] = Field(default=None)
    plan_display_name: Union[str | None, Any] = Field(default=None)
    plan_name: Union[str | None, Any] = Field(default=None)
    has_discounts: Union[bool | None, Any] = Field(default=None)
    has_gift_cards: Union[bool | None, Any] = Field(default=None)
    myshopify_domain: Union[str | None, Any] = Field(default=None)
    google_apps_domain: Union[str | None, Any] = Field(default=None)
    google_apps_login_enabled: Union[bool | None, Any] = Field(default=None)
    money_in_emails_format: Union[str | None, Any] = Field(default=None)
    money_with_currency_in_emails_format: Union[str | None, Any] = Field(default=None)
    eligible_for_payments: Union[bool | None, Any] = Field(default=None)
    requires_extra_payments_agreement: Union[bool | None, Any] = Field(default=None)
    password_enabled: Union[bool | None, Any] = Field(default=None)
    has_storefront: Union[bool | None, Any] = Field(default=None)
    finances: Union[bool | None, Any] = Field(default=None)
    primary_location_id: Union[int | None, Any] = Field(default=None)
    checkout_api_supported: Union[bool | None, Any] = Field(default=None)
    multi_location_enabled: Union[bool | None, Any] = Field(default=None)
    setup_required: Union[bool | None, Any] = Field(default=None)
    pre_launch_enabled: Union[bool | None, Any] = Field(default=None)
    enabled_presentment_currencies: Union[list[str] | None, Any] = Field(default=None)
    transactional_sms_disabled: Union[bool | None, Any] = Field(default=None)
    marketing_sms_consent_enabled_at_checkout: Union[bool | None, Any] = Field(default=None)

class PriceRule(BaseModel):
    """A price rule"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    value_type: Union[str | None, Any] = Field(default=None)
    value: Union[str | None, Any] = Field(default=None)
    customer_selection: Union[str | None, Any] = Field(default=None)
    target_type: Union[str | None, Any] = Field(default=None)
    target_selection: Union[str | None, Any] = Field(default=None)
    allocation_method: Union[str | None, Any] = Field(default=None)
    allocation_limit: Union[int | None, Any] = Field(default=None)
    once_per_customer: Union[bool | None, Any] = Field(default=None)
    usage_limit: Union[int | None, Any] = Field(default=None)
    starts_at: Union[str | None, Any] = Field(default=None)
    ends_at: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    entitled_product_ids: Union[list[int] | None, Any] = Field(default=None)
    entitled_variant_ids: Union[list[int] | None, Any] = Field(default=None)
    entitled_collection_ids: Union[list[int] | None, Any] = Field(default=None)
    entitled_country_ids: Union[list[int] | None, Any] = Field(default=None)
    prerequisite_product_ids: Union[list[int] | None, Any] = Field(default=None)
    prerequisite_variant_ids: Union[list[int] | None, Any] = Field(default=None)
    prerequisite_collection_ids: Union[list[int] | None, Any] = Field(default=None)
    customer_segment_prerequisite_ids: Union[list[int] | None, Any] = Field(default=None)
    prerequisite_customer_ids: Union[list[int] | None, Any] = Field(default=None)
    prerequisite_subtotal_range: Union[dict[str, Any] | None, Any] = Field(default=None)
    prerequisite_quantity_range: Union[dict[str, Any] | None, Any] = Field(default=None)
    prerequisite_shipping_price_range: Union[dict[str, Any] | None, Any] = Field(default=None)
    prerequisite_to_entitlement_quantity_ratio: Union[dict[str, Any] | None, Any] = Field(default=None)
    prerequisite_to_entitlement_purchase: Union[dict[str, Any] | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)

class PriceRuleList(BaseModel):
    """PriceRuleList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    price_rules: Union[list[PriceRule], Any] = Field(default=None)

class DiscountCode(BaseModel):
    """A discount code"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    price_rule_id: Union[int | None, Any] = Field(default=None)
    code: Union[str | None, Any] = Field(default=None)
    usage_count: Union[int | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class DiscountCodeList(BaseModel):
    """DiscountCodeList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    discount_codes: Union[list[DiscountCode], Any] = Field(default=None)

class CustomCollection(BaseModel):
    """A custom collection"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    handle: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    body_html: Union[str | None, Any] = Field(default=None)
    published_at: Union[str | None, Any] = Field(default=None)
    sort_order: Union[str | None, Any] = Field(default=None)
    template_suffix: Union[str | None, Any] = Field(default=None)
    published_scope: Union[str | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)
    image: Union[dict[str, Any] | None, Any] = Field(default=None)
    products_count: Union[int | None, Any] = Field(default=None)

class CustomCollectionList(BaseModel):
    """CustomCollectionList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    custom_collections: Union[list[CustomCollection], Any] = Field(default=None)

class SmartCollection(BaseModel):
    """A smart collection"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    handle: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    body_html: Union[str | None, Any] = Field(default=None)
    published_at: Union[str | None, Any] = Field(default=None)
    sort_order: Union[str | None, Any] = Field(default=None)
    template_suffix: Union[str | None, Any] = Field(default=None)
    disjunctive: Union[bool | None, Any] = Field(default=None)
    rules: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    published_scope: Union[str | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)
    image: Union[dict[str, Any] | None, Any] = Field(default=None)
    products_count: Union[int | None, Any] = Field(default=None)

class SmartCollectionList(BaseModel):
    """SmartCollectionList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    smart_collections: Union[list[SmartCollection], Any] = Field(default=None)

class Collect(BaseModel):
    """A collect (product-collection link)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    collection_id: Union[int | None, Any] = Field(default=None)
    product_id: Union[int | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    position: Union[int | None, Any] = Field(default=None)
    sort_value: Union[str | None, Any] = Field(default=None)

class CollectList(BaseModel):
    """CollectList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    collects: Union[list[Collect], Any] = Field(default=None)

class DraftOrder(BaseModel):
    """A draft order"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    note: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    taxes_included: Union[bool | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    invoice_sent_at: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    tax_exempt: Union[bool | None, Any] = Field(default=None)
    completed_at: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    line_items: Union[list[LineItem] | None, Any] = Field(default=None)
    shipping_address: Union[Any, Any] = Field(default=None)
    billing_address: Union[Any, Any] = Field(default=None)
    invoice_url: Union[str | None, Any] = Field(default=None)
    applied_discount: Union[dict[str, Any] | None, Any] = Field(default=None)
    order_id: Union[int | None, Any] = Field(default=None)
    shipping_line: Union[dict[str, Any] | None, Any] = Field(default=None)
    tax_lines: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    tags: Union[str | None, Any] = Field(default=None)
    note_attributes: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    total_price: Union[str | None, Any] = Field(default=None)
    subtotal_price: Union[str | None, Any] = Field(default=None)
    total_tax: Union[str | None, Any] = Field(default=None)
    payment_terms: Union[dict[str, Any] | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)
    customer: Union[Any, Any] = Field(default=None)
    allow_discount_codes_in_checkout: Union[bool | None, Any] = Field(default=None, alias="allow_discount_codes_in_checkout?")
    b2b: Union[bool | None, Any] = Field(default=None, alias="b2b?")
    api_client_id: Union[int | None, Any] = Field(default=None)
    created_on_api_version_handle: Union[str | None, Any] = Field(default=None)

class DraftOrderList(BaseModel):
    """DraftOrderList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    draft_orders: Union[list[DraftOrder], Any] = Field(default=None)

class FulfillmentList(BaseModel):
    """FulfillmentList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    fulfillments: Union[list[Fulfillment], Any] = Field(default=None)

class FulfillmentOrder(BaseModel):
    """A fulfillment order"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    shop_id: Union[int | None, Any] = Field(default=None)
    order_id: Union[int | None, Any] = Field(default=None)
    assigned_location_id: Union[int | None, Any] = Field(default=None)
    request_status: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    supported_actions: Union[list[str] | None, Any] = Field(default=None)
    destination: Union[dict[str, Any] | None, Any] = Field(default=None)
    line_items: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    fulfill_at: Union[str | None, Any] = Field(default=None)
    fulfill_by: Union[str | None, Any] = Field(default=None)
    international_duties: Union[dict[str, Any] | None, Any] = Field(default=None)
    fulfillment_holds: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    delivery_method: Union[dict[str, Any] | None, Any] = Field(default=None)
    assigned_location: Union[dict[str, Any] | None, Any] = Field(default=None)
    merchant_requests: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class FulfillmentOrderList(BaseModel):
    """FulfillmentOrderList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    fulfillment_orders: Union[list[FulfillmentOrder], Any] = Field(default=None)

class RefundList(BaseModel):
    """RefundList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    refunds: Union[list[Refund], Any] = Field(default=None)

class TransactionList(BaseModel):
    """TransactionList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transactions: Union[list[Transaction], Any] = Field(default=None)

class TenderTransaction(BaseModel):
    """A tender transaction"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    order_id: Union[int | None, Any] = Field(default=None)
    amount: Union[str | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    user_id: Union[int | None, Any] = Field(default=None)
    test: Union[bool | None, Any] = Field(default=None)
    processed_at: Union[str | None, Any] = Field(default=None)
    remote_reference: Union[str | None, Any] = Field(default=None)
    payment_details: Union[dict[str, Any] | None, Any] = Field(default=None)
    payment_method: Union[str | None, Any] = Field(default=None)

class TenderTransactionList(BaseModel):
    """TenderTransactionList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tender_transactions: Union[list[TenderTransaction], Any] = Field(default=None)

class Country(BaseModel):
    """A country"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    code: Union[str | None, Any] = Field(default=None)
    tax_name: Union[str | None, Any] = Field(default=None)
    tax: Union[float | None, Any] = Field(default=None)
    provinces: Union[list[dict[str, Any]] | None, Any] = Field(default=None)

class CountryList(BaseModel):
    """CountryList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    countries: Union[list[Country], Any] = Field(default=None)

class Metafield(BaseModel):
    """A metafield"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    namespace: Union[str | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[Any, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    owner_id: Union[int | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    owner_resource: Union[str | None, Any] = Field(default=None)
    admin_graphql_api_id: Union[str | None, Any] = Field(default=None)

class MetafieldList(BaseModel):
    """MetafieldList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    metafields: Union[list[Metafield], Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class CustomersListResultMeta(BaseModel):
    """Metadata for customers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class OrdersListResultMeta(BaseModel):
    """Metadata for orders.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class ProductsListResultMeta(BaseModel):
    """Metadata for products.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class ProductVariantsListResultMeta(BaseModel):
    """Metadata for product_variants.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class ProductImagesListResultMeta(BaseModel):
    """Metadata for product_images.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class AbandonedCheckoutsListResultMeta(BaseModel):
    """Metadata for abandoned_checkouts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class LocationsListResultMeta(BaseModel):
    """Metadata for locations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class InventoryLevelsListResultMeta(BaseModel):
    """Metadata for inventory_levels.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class InventoryItemsListResultMeta(BaseModel):
    """Metadata for inventory_items.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class PriceRulesListResultMeta(BaseModel):
    """Metadata for price_rules.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class DiscountCodesListResultMeta(BaseModel):
    """Metadata for discount_codes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class CustomCollectionsListResultMeta(BaseModel):
    """Metadata for custom_collections.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class SmartCollectionsListResultMeta(BaseModel):
    """Metadata for smart_collections.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class CollectsListResultMeta(BaseModel):
    """Metadata for collects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class DraftOrdersListResultMeta(BaseModel):
    """Metadata for draft_orders.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class FulfillmentsListResultMeta(BaseModel):
    """Metadata for fulfillments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class OrderRefundsListResultMeta(BaseModel):
    """Metadata for order_refunds.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class TransactionsListResultMeta(BaseModel):
    """Metadata for transactions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class TenderTransactionsListResultMeta(BaseModel):
    """Metadata for tender_transactions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class CountriesListResultMeta(BaseModel):
    """Metadata for countries.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class MetafieldShopsListResultMeta(BaseModel):
    """Metadata for metafield_shops.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class MetafieldCustomersListResultMeta(BaseModel):
    """Metadata for metafield_customers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class MetafieldProductsListResultMeta(BaseModel):
    """Metadata for metafield_products.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class MetafieldOrdersListResultMeta(BaseModel):
    """Metadata for metafield_orders.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class MetafieldDraftOrdersListResultMeta(BaseModel):
    """Metadata for metafield_draft_orders.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class MetafieldLocationsListResultMeta(BaseModel):
    """Metadata for metafield_locations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class MetafieldProductVariantsListResultMeta(BaseModel):
    """Metadata for metafield_product_variants.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class MetafieldSmartCollectionsListResultMeta(BaseModel):
    """Metadata for metafield_smart_collections.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class MetafieldProductImagesListResultMeta(BaseModel):
    """Metadata for metafield_product_images.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class CustomerAddressListResultMeta(BaseModel):
    """Metadata for customer_address.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

class FulfillmentOrdersListResultMeta(BaseModel):
    """Metadata for fulfillment_orders.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_url: Union[str | None, Any] = Field(default=None)

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
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""



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

