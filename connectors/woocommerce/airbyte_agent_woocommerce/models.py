"""
Pydantic models for woocommerce connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class WoocommerceAuthConfig(BaseModel):
    """WooCommerce API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """WooCommerce REST API consumer key (starts with ck_)"""
    api_secret: str
    """WooCommerce REST API consumer secret (starts with cs_)"""

# Replication configuration

class WoocommerceReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from WooCommerce."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date and time in the format YYYY-MM-DDTHH:mm:ssZ from which to start replicating data."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class CustomerShipping(BaseModel):
    """List of shipping address data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    company: Union[str | None, Any] = Field(default=None)
    address_1: Union[str | None, Any] = Field(default=None)
    address_2: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    postcode: Union[str | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)

class CustomerMetaDataItem(BaseModel):
    """Nested schema for Customer.meta_data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[str | None, Any] = Field(default=None)

class CustomerBilling(BaseModel):
    """List of billing address data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    company: Union[str | None, Any] = Field(default=None)
    address_1: Union[str | None, Any] = Field(default=None)
    address_2: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    postcode: Union[str | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)

class Customer(BaseModel):
    """Customer type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_created_gmt: Union[str | None, Any] = Field(default=None)
    date_modified: Union[str | None, Any] = Field(default=None)
    date_modified_gmt: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)
    username: Union[str | None, Any] = Field(default=None)
    billing: Union[CustomerBilling | None, Any] = Field(default=None)
    shipping: Union[CustomerShipping | None, Any] = Field(default=None)
    is_paying_customer: Union[bool | None, Any] = Field(default=None)
    avatar_url: Union[str | None, Any] = Field(default=None)
    meta_data: Union[list[CustomerMetaDataItem] | None, Any] = Field(default=None)

class OrderBilling(BaseModel):
    """Billing address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    company: Union[str | None, Any] = Field(default=None)
    address_1: Union[str | None, Any] = Field(default=None)
    address_2: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    postcode: Union[str | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)

class OrderShipping(BaseModel):
    """Shipping address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    company: Union[str | None, Any] = Field(default=None)
    address_1: Union[str | None, Any] = Field(default=None)
    address_2: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    postcode: Union[str | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)

class OrderShippingLinesItemTaxesItem(BaseModel):
    """Nested schema for OrderShippingLinesItem.taxes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    total: Union[str | None, Any] = Field(default=None)
    subtotal: Union[str | None, Any] = Field(default=None)

class OrderShippingLinesItemMetaDataItem(BaseModel):
    """Nested schema for OrderShippingLinesItem.meta_data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[Any, Any] = Field(default=None)

class OrderShippingLinesItem(BaseModel):
    """Nested schema for Order.shipping_lines_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    method_title: Union[str | None, Any] = Field(default=None)
    method_id: Union[str | None, Any] = Field(default=None)
    total: Union[str | None, Any] = Field(default=None)
    total_tax: Union[str | None, Any] = Field(default=None)
    taxes: Union[list[OrderShippingLinesItemTaxesItem] | None, Any] = Field(default=None)
    meta_data: Union[list[OrderShippingLinesItemMetaDataItem] | None, Any] = Field(default=None)

class OrderCouponLinesItemMetaDataItem(BaseModel):
    """Nested schema for OrderCouponLinesItem.meta_data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[Any, Any] = Field(default=None)

class OrderCouponLinesItem(BaseModel):
    """Nested schema for Order.coupon_lines_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    code: Union[str | None, Any] = Field(default=None)
    discount: Union[str | None, Any] = Field(default=None)
    discount_tax: Union[str | None, Any] = Field(default=None)
    meta_data: Union[list[OrderCouponLinesItemMetaDataItem] | None, Any] = Field(default=None)

class OrderTaxLinesItemMetaDataItem(BaseModel):
    """Nested schema for OrderTaxLinesItem.meta_data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[Any, Any] = Field(default=None)

class OrderTaxLinesItem(BaseModel):
    """Nested schema for Order.tax_lines_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    rate_code: Union[str | None, Any] = Field(default=None)
    rate_id: Union[int | None, Any] = Field(default=None)
    label: Union[str | None, Any] = Field(default=None)
    compound: Union[bool | None, Any] = Field(default=None)
    tax_total: Union[str | None, Any] = Field(default=None)
    shipping_tax_total: Union[str | None, Any] = Field(default=None)
    meta_data: Union[list[OrderTaxLinesItemMetaDataItem] | None, Any] = Field(default=None)

class OrderRefundsItem(BaseModel):
    """Nested schema for Order.refunds_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    reason: Union[str | None, Any] = Field(default=None)
    total: Union[str | None, Any] = Field(default=None)

class OrderMetaDataItem(BaseModel):
    """Nested schema for Order.meta_data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[Any, Any] = Field(default=None)

class OrderLineItemsItemImage(BaseModel):
    """Nested schema for OrderLineItemsItem.image"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[Any, Any] = Field(default=None)
    src: Union[str | None, Any] = Field(default=None)

class OrderLineItemsItemTaxesItem(BaseModel):
    """Nested schema for OrderLineItemsItem.taxes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    total: Union[str | None, Any] = Field(default=None)
    subtotal: Union[str | None, Any] = Field(default=None)

class OrderLineItemsItemMetaDataItem(BaseModel):
    """Nested schema for OrderLineItemsItem.meta_data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[Any, Any] = Field(default=None)
    display_key: Union[str | None, Any] = Field(default=None)
    display_value: Union[str | None, Any] = Field(default=None)

class OrderLineItemsItem(BaseModel):
    """Nested schema for Order.line_items_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    product_id: Union[int | None, Any] = Field(default=None)
    variation_id: Union[int | None, Any] = Field(default=None)
    quantity: Union[int | None, Any] = Field(default=None)
    tax_class: Union[str | None, Any] = Field(default=None)
    subtotal: Union[str | None, Any] = Field(default=None)
    subtotal_tax: Union[str | None, Any] = Field(default=None)
    total: Union[str | None, Any] = Field(default=None)
    total_tax: Union[str | None, Any] = Field(default=None)
    taxes: Union[list[OrderLineItemsItemTaxesItem] | None, Any] = Field(default=None)
    meta_data: Union[list[OrderLineItemsItemMetaDataItem] | None, Any] = Field(default=None)
    sku: Union[str | None, Any] = Field(default=None)
    price: Union[float | None, Any] = Field(default=None)
    image: Union[OrderLineItemsItemImage | None, Any] = Field(default=None)
    parent_name: Union[str | None, Any] = Field(default=None)

class OrderFeeLinesItemMetaDataItem(BaseModel):
    """Nested schema for OrderFeeLinesItem.meta_data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[Any, Any] = Field(default=None)

class OrderFeeLinesItemTaxesItem(BaseModel):
    """Nested schema for OrderFeeLinesItem.taxes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    total: Union[str | None, Any] = Field(default=None)
    subtotal: Union[str | None, Any] = Field(default=None)

class OrderFeeLinesItem(BaseModel):
    """Nested schema for Order.fee_lines_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    tax_class: Union[str | None, Any] = Field(default=None)
    tax_status: Union[str | None, Any] = Field(default=None)
    total: Union[str | None, Any] = Field(default=None)
    total_tax: Union[str | None, Any] = Field(default=None)
    taxes: Union[list[OrderFeeLinesItemTaxesItem] | None, Any] = Field(default=None)
    meta_data: Union[list[OrderFeeLinesItemMetaDataItem] | None, Any] = Field(default=None)

class Order(BaseModel):
    """Order type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    parent_id: Union[int | None, Any] = Field(default=None)
    number: Union[str | None, Any] = Field(default=None)
    order_key: Union[str | None, Any] = Field(default=None)
    created_via: Union[str | None, Any] = Field(default=None)
    version: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    currency: Union[str | None, Any] = Field(default=None)
    currency_symbol: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_created_gmt: Union[str | None, Any] = Field(default=None)
    date_modified: Union[str | None, Any] = Field(default=None)
    date_modified_gmt: Union[str | None, Any] = Field(default=None)
    discount_total: Union[str | None, Any] = Field(default=None)
    discount_tax: Union[str | None, Any] = Field(default=None)
    shipping_total: Union[str | None, Any] = Field(default=None)
    shipping_tax: Union[str | None, Any] = Field(default=None)
    cart_tax: Union[str | None, Any] = Field(default=None)
    total: Union[str | None, Any] = Field(default=None)
    total_tax: Union[str | None, Any] = Field(default=None)
    prices_include_tax: Union[bool | None, Any] = Field(default=None)
    customer_id: Union[int | None, Any] = Field(default=None)
    customer_ip_address: Union[str | None, Any] = Field(default=None)
    customer_user_agent: Union[str | None, Any] = Field(default=None)
    customer_note: Union[str | None, Any] = Field(default=None)
    billing: Union[OrderBilling | None, Any] = Field(default=None)
    shipping: Union[OrderShipping | None, Any] = Field(default=None)
    payment_method: Union[str | None, Any] = Field(default=None)
    payment_method_title: Union[str | None, Any] = Field(default=None)
    transaction_id: Union[str | None, Any] = Field(default=None)
    date_paid: Union[str | None, Any] = Field(default=None)
    date_paid_gmt: Union[str | None, Any] = Field(default=None)
    date_completed: Union[str | None, Any] = Field(default=None)
    date_completed_gmt: Union[str | None, Any] = Field(default=None)
    cart_hash: Union[str | None, Any] = Field(default=None)
    meta_data: Union[list[OrderMetaDataItem] | None, Any] = Field(default=None)
    line_items: Union[list[OrderLineItemsItem] | None, Any] = Field(default=None)
    tax_lines: Union[list[OrderTaxLinesItem] | None, Any] = Field(default=None)
    shipping_lines: Union[list[OrderShippingLinesItem] | None, Any] = Field(default=None)
    fee_lines: Union[list[OrderFeeLinesItem] | None, Any] = Field(default=None)
    coupon_lines: Union[list[OrderCouponLinesItem] | None, Any] = Field(default=None)
    refunds: Union[list[OrderRefundsItem] | None, Any] = Field(default=None)
    payment_url: Union[str | None, Any] = Field(default=None)
    is_editable: Union[bool | None, Any] = Field(default=None)
    needs_payment: Union[bool | None, Any] = Field(default=None)
    needs_processing: Union[bool | None, Any] = Field(default=None)

class ProductAttributesItem(BaseModel):
    """Nested schema for Product.attributes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    position: Union[int | None, Any] = Field(default=None)
    visible: Union[bool | None, Any] = Field(default=None)
    variation: Union[bool | None, Any] = Field(default=None)
    options: Union[list[str | None] | None, Any] = Field(default=None)

class ProductDownloadsItem(BaseModel):
    """Nested schema for Product.downloads_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    file: Union[str | None, Any] = Field(default=None)

class ProductImagesItem(BaseModel):
    """Nested schema for Product.images_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_created_gmt: Union[str | None, Any] = Field(default=None)
    date_modified: Union[str | None, Any] = Field(default=None)
    date_modified_gmt: Union[str | None, Any] = Field(default=None)
    src: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    alt: Union[str | None, Any] = Field(default=None)

class ProductMetaDataItem(BaseModel):
    """Nested schema for Product.meta_data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[Any, Any] = Field(default=None)

class ProductCategoriesItem(BaseModel):
    """Nested schema for Product.categories_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)

class ProductTagsItem(BaseModel):
    """Nested schema for Product.tags_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)

class ProductDefaultAttributesItem(BaseModel):
    """Nested schema for Product.default_attributes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    option: Union[str | None, Any] = Field(default=None)

class ProductDimensions(BaseModel):
    """Product dimensions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    length: Union[str | None, Any] = Field(default=None)
    width: Union[str | None, Any] = Field(default=None)
    height: Union[str | None, Any] = Field(default=None)

class Product(BaseModel):
    """Product type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)
    permalink: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_created_gmt: Union[str | None, Any] = Field(default=None)
    date_modified: Union[str | None, Any] = Field(default=None)
    date_modified_gmt: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    status: Union[str | None, Any] = Field(default=None)
    featured: Union[bool | None, Any] = Field(default=None)
    catalog_visibility: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    short_description: Union[str | None, Any] = Field(default=None)
    sku: Union[str | None, Any] = Field(default=None)
    price: Union[str | None, Any] = Field(default=None)
    regular_price: Union[str | None, Any] = Field(default=None)
    sale_price: Union[str | None, Any] = Field(default=None)
    date_on_sale_from: Union[str | None, Any] = Field(default=None)
    date_on_sale_from_gmt: Union[str | None, Any] = Field(default=None)
    date_on_sale_to: Union[str | None, Any] = Field(default=None)
    date_on_sale_to_gmt: Union[str | None, Any] = Field(default=None)
    price_html: Union[str | None, Any] = Field(default=None)
    on_sale: Union[bool | None, Any] = Field(default=None)
    purchasable: Union[bool | None, Any] = Field(default=None)
    total_sales: Union[int | None, Any] = Field(default=None)
    virtual: Union[bool | None, Any] = Field(default=None)
    downloadable: Union[bool | None, Any] = Field(default=None)
    downloads: Union[list[ProductDownloadsItem] | None, Any] = Field(default=None)
    download_limit: Union[int | None, Any] = Field(default=None)
    download_expiry: Union[int | None, Any] = Field(default=None)
    external_url: Union[str | None, Any] = Field(default=None)
    button_text: Union[str | None, Any] = Field(default=None)
    tax_status: Union[str | None, Any] = Field(default=None)
    tax_class: Union[str | None, Any] = Field(default=None)
    manage_stock: Union[bool | None, Any] = Field(default=None)
    stock_quantity: Union[int | None, Any] = Field(default=None)
    stock_status: Union[str | None, Any] = Field(default=None)
    backorders: Union[str | None, Any] = Field(default=None)
    backorders_allowed: Union[bool | None, Any] = Field(default=None)
    backordered: Union[bool | None, Any] = Field(default=None)
    sold_individually: Union[bool | None, Any] = Field(default=None)
    weight: Union[str | None, Any] = Field(default=None)
    dimensions: Union[ProductDimensions | None, Any] = Field(default=None)
    shipping_required: Union[bool | None, Any] = Field(default=None)
    shipping_taxable: Union[bool | None, Any] = Field(default=None)
    shipping_class: Union[str | None, Any] = Field(default=None)
    shipping_class_id: Union[int | None, Any] = Field(default=None)
    reviews_allowed: Union[bool | None, Any] = Field(default=None)
    average_rating: Union[str | None, Any] = Field(default=None)
    rating_count: Union[int | None, Any] = Field(default=None)
    related_ids: Union[list[int | None] | None, Any] = Field(default=None)
    upsell_ids: Union[list[int | None] | None, Any] = Field(default=None)
    cross_sell_ids: Union[list[int | None] | None, Any] = Field(default=None)
    parent_id: Union[int | None, Any] = Field(default=None)
    purchase_note: Union[str | None, Any] = Field(default=None)
    categories: Union[list[ProductCategoriesItem] | None, Any] = Field(default=None)
    tags: Union[list[ProductTagsItem] | None, Any] = Field(default=None)
    images: Union[list[ProductImagesItem] | None, Any] = Field(default=None)
    attributes: Union[list[ProductAttributesItem] | None, Any] = Field(default=None)
    default_attributes: Union[list[ProductDefaultAttributesItem] | None, Any] = Field(default=None)
    variations: Union[list[int | None] | None, Any] = Field(default=None)
    grouped_products: Union[list[int | None] | None, Any] = Field(default=None)
    menu_order: Union[int | None, Any] = Field(default=None)
    meta_data: Union[list[ProductMetaDataItem] | None, Any] = Field(default=None)
    low_stock_amount: Union[int | None, Any] = Field(default=None)
    brands: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    has_options: Union[bool | None, Any] = Field(default=None)
    post_password: Union[str | None, Any] = Field(default=None)
    global_unique_id: Union[str | None, Any] = Field(default=None)

class CouponMetaDataItem(BaseModel):
    """Nested schema for Coupon.meta_data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[Any, Any] = Field(default=None)

class Coupon(BaseModel):
    """Coupon type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    code: Union[str | None, Any] = Field(default=None)
    amount: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_created_gmt: Union[str | None, Any] = Field(default=None)
    date_modified: Union[str | None, Any] = Field(default=None)
    date_modified_gmt: Union[str | None, Any] = Field(default=None)
    discount_type: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    date_expires: Union[str | None, Any] = Field(default=None)
    date_expires_gmt: Union[str | None, Any] = Field(default=None)
    usage_count: Union[int | None, Any] = Field(default=None)
    individual_use: Union[bool | None, Any] = Field(default=None)
    product_ids: Union[list[int | None] | None, Any] = Field(default=None)
    excluded_product_ids: Union[list[int | None] | None, Any] = Field(default=None)
    usage_limit: Union[int | None, Any] = Field(default=None)
    usage_limit_per_user: Union[int | None, Any] = Field(default=None)
    limit_usage_to_x_items: Union[int | None, Any] = Field(default=None)
    free_shipping: Union[bool | None, Any] = Field(default=None)
    product_categories: Union[list[int | None] | None, Any] = Field(default=None)
    excluded_product_categories: Union[list[int | None] | None, Any] = Field(default=None)
    exclude_sale_items: Union[bool | None, Any] = Field(default=None)
    minimum_amount: Union[str | None, Any] = Field(default=None)
    maximum_amount: Union[str | None, Any] = Field(default=None)
    email_restrictions: Union[list[str | None] | None, Any] = Field(default=None)
    used_by: Union[list[str | None] | None, Any] = Field(default=None)
    meta_data: Union[list[CouponMetaDataItem] | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)

class ProductCategoryImage(BaseModel):
    """Image data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_created_gmt: Union[str | None, Any] = Field(default=None)
    date_modified: Union[str | None, Any] = Field(default=None)
    date_modified_gmt: Union[str | None, Any] = Field(default=None)
    src: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    alt: Union[str | None, Any] = Field(default=None)

class ProductCategory(BaseModel):
    """ProductCategory type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)
    parent: Union[int | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    display: Union[str | None, Any] = Field(default=None)
    image: Union[ProductCategoryImage | None, Any] = Field(default=None)
    menu_order: Union[int | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

class ProductTag(BaseModel):
    """ProductTag type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

class ProductReview(BaseModel):
    """ProductReview type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_created_gmt: Union[str | None, Any] = Field(default=None)
    product_id: Union[int | None, Any] = Field(default=None)
    product_name: Union[str | None, Any] = Field(default=None)
    product_permalink: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    reviewer: Union[str | None, Any] = Field(default=None)
    reviewer_email: Union[str | None, Any] = Field(default=None)
    review: Union[str | None, Any] = Field(default=None)
    rating: Union[int | None, Any] = Field(default=None)
    verified: Union[bool | None, Any] = Field(default=None)
    reviewer_avatar_urls: Union[dict[str, str | None] | None, Any] = Field(default=None)

class ProductAttribute(BaseModel):
    """ProductAttribute type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    order_by: Union[str | None, Any] = Field(default=None)
    has_archives: Union[bool | None, Any] = Field(default=None)

class ProductVariationDimensions(BaseModel):
    """Variation dimensions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    length: Union[str | None, Any] = Field(default=None)
    width: Union[str | None, Any] = Field(default=None)
    height: Union[str | None, Any] = Field(default=None)

class ProductVariationImage(BaseModel):
    """Variation image data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_created_gmt: Union[str | None, Any] = Field(default=None)
    date_modified: Union[str | None, Any] = Field(default=None)
    date_modified_gmt: Union[str | None, Any] = Field(default=None)
    src: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    alt: Union[str | None, Any] = Field(default=None)

class ProductVariationAttributesItem(BaseModel):
    """Nested schema for ProductVariation.attributes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    option: Union[str | None, Any] = Field(default=None)

class ProductVariationDownloadsItem(BaseModel):
    """Nested schema for ProductVariation.downloads_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    file: Union[str | None, Any] = Field(default=None)

class ProductVariationMetaDataItem(BaseModel):
    """Nested schema for ProductVariation.meta_data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[Any, Any] = Field(default=None)

class ProductVariation(BaseModel):
    """ProductVariation type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_created_gmt: Union[str | None, Any] = Field(default=None)
    date_modified: Union[str | None, Any] = Field(default=None)
    date_modified_gmt: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    permalink: Union[str | None, Any] = Field(default=None)
    sku: Union[str | None, Any] = Field(default=None)
    price: Union[str | None, Any] = Field(default=None)
    regular_price: Union[str | None, Any] = Field(default=None)
    sale_price: Union[str | None, Any] = Field(default=None)
    date_on_sale_from: Union[str | None, Any] = Field(default=None)
    date_on_sale_from_gmt: Union[str | None, Any] = Field(default=None)
    date_on_sale_to: Union[str | None, Any] = Field(default=None)
    date_on_sale_to_gmt: Union[str | None, Any] = Field(default=None)
    on_sale: Union[bool | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    purchasable: Union[bool | None, Any] = Field(default=None)
    virtual: Union[bool | None, Any] = Field(default=None)
    downloadable: Union[bool | None, Any] = Field(default=None)
    downloads: Union[list[ProductVariationDownloadsItem] | None, Any] = Field(default=None)
    download_limit: Union[int | None, Any] = Field(default=None)
    download_expiry: Union[int | None, Any] = Field(default=None)
    tax_status: Union[str | None, Any] = Field(default=None)
    tax_class: Union[str | None, Any] = Field(default=None)
    manage_stock: Union[bool | None, Any] = Field(default=None)
    stock_quantity: Union[int | None, Any] = Field(default=None)
    stock_status: Union[str | None, Any] = Field(default=None)
    backorders: Union[str | None, Any] = Field(default=None)
    backorders_allowed: Union[bool | None, Any] = Field(default=None)
    backordered: Union[bool | None, Any] = Field(default=None)
    weight: Union[str | None, Any] = Field(default=None)
    dimensions: Union[ProductVariationDimensions | None, Any] = Field(default=None)
    shipping_class: Union[str | None, Any] = Field(default=None)
    shipping_class_id: Union[int | None, Any] = Field(default=None)
    image: Union[ProductVariationImage | None, Any] = Field(default=None)
    attributes: Union[list[ProductVariationAttributesItem] | None, Any] = Field(default=None)
    menu_order: Union[int | None, Any] = Field(default=None)
    meta_data: Union[list[ProductVariationMetaDataItem] | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    global_unique_id: Union[str | None, Any] = Field(default=None)
    low_stock_amount: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    parent_id: Union[int | None, Any] = Field(default=None)

class OrderNote(BaseModel):
    """OrderNote type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    author: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_created_gmt: Union[str | None, Any] = Field(default=None)
    note: Union[str | None, Any] = Field(default=None)
    customer_note: Union[bool | None, Any] = Field(default=None)

class RefundMetaDataItem(BaseModel):
    """Nested schema for Refund.meta_data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[Any, Any] = Field(default=None)

class RefundFeeLinesItem(BaseModel):
    """Nested schema for Refund.fee_lines_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    tax_class: Union[str | None, Any] = Field(default=None)
    tax_status: Union[str | None, Any] = Field(default=None)
    total: Union[str | None, Any] = Field(default=None)
    total_tax: Union[str | None, Any] = Field(default=None)

class RefundLineItemsItemMetaDataItem(BaseModel):
    """Nested schema for RefundLineItemsItem.meta_data_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    key: Union[str | None, Any] = Field(default=None)
    value: Union[Any, Any] = Field(default=None)

class RefundLineItemsItemTaxesItem(BaseModel):
    """Nested schema for RefundLineItemsItem.taxes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    total: Union[str | None, Any] = Field(default=None)
    subtotal: Union[str | None, Any] = Field(default=None)

class RefundLineItemsItem(BaseModel):
    """Nested schema for Refund.line_items_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    product_id: Union[int | None, Any] = Field(default=None)
    variation_id: Union[int | None, Any] = Field(default=None)
    quantity: Union[int | None, Any] = Field(default=None)
    tax_class: Union[str | None, Any] = Field(default=None)
    subtotal: Union[str | None, Any] = Field(default=None)
    subtotal_tax: Union[str | None, Any] = Field(default=None)
    total: Union[str | None, Any] = Field(default=None)
    total_tax: Union[str | None, Any] = Field(default=None)
    taxes: Union[list[RefundLineItemsItemTaxesItem] | None, Any] = Field(default=None)
    meta_data: Union[list[RefundLineItemsItemMetaDataItem] | None, Any] = Field(default=None)
    sku: Union[str | None, Any] = Field(default=None)
    price: Union[float | None, Any] = Field(default=None)

class RefundShippingLinesItem(BaseModel):
    """Nested schema for Refund.shipping_lines_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    method_title: Union[str | None, Any] = Field(default=None)
    method_id: Union[str | None, Any] = Field(default=None)
    total: Union[str | None, Any] = Field(default=None)
    total_tax: Union[str | None, Any] = Field(default=None)

class RefundTaxLinesItem(BaseModel):
    """Nested schema for Refund.tax_lines_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    rate_code: Union[str | None, Any] = Field(default=None)
    rate_id: Union[int | None, Any] = Field(default=None)
    label: Union[str | None, Any] = Field(default=None)
    compound: Union[bool | None, Any] = Field(default=None)
    tax_total: Union[str | None, Any] = Field(default=None)
    shipping_tax_total: Union[str | None, Any] = Field(default=None)

class Refund(BaseModel):
    """Refund type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_created_gmt: Union[str | None, Any] = Field(default=None)
    amount: Union[str | None, Any] = Field(default=None)
    reason: Union[str | None, Any] = Field(default=None)
    refunded_by: Union[int | None, Any] = Field(default=None)
    refunded_payment: Union[bool | None, Any] = Field(default=None)
    meta_data: Union[list[RefundMetaDataItem] | None, Any] = Field(default=None)
    line_items: Union[list[RefundLineItemsItem] | None, Any] = Field(default=None)
    shipping_lines: Union[list[RefundShippingLinesItem] | None, Any] = Field(default=None)
    tax_lines: Union[list[RefundTaxLinesItem] | None, Any] = Field(default=None)
    fee_lines: Union[list[RefundFeeLinesItem] | None, Any] = Field(default=None)

class PaymentGateway(BaseModel):
    """PaymentGateway type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    order: Union[int | None, Any] = Field(default=None)
    enabled: Union[bool | None, Any] = Field(default=None)
    method_title: Union[str | None, Any] = Field(default=None)
    method_description: Union[str | None, Any] = Field(default=None)
    method_supports: Union[list[str | None] | None, Any] = Field(default=None)
    settings: Union[dict[str, Any] | None, Any] = Field(default=None)
    needs_setup: Union[bool | None, Any] = Field(default=None)
    post_install_scripts: Union[list[str | None] | None, Any] = Field(default=None)
    settings_url: Union[str | None, Any] = Field(default=None)
    connection_url: Union[str | None, Any] = Field(default=None)
    setup_help_text: Union[str | None, Any] = Field(default=None)
    required_settings_keys: Union[list[str | None] | None, Any] = Field(default=None)

class ShippingMethod(BaseModel):
    """ShippingMethod type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)

class ShippingZone(BaseModel):
    """ShippingZone type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    order: Union[int | None, Any] = Field(default=None)

class TaxRate(BaseModel):
    """TaxRate type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    postcode: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    postcodes: Union[list[str | None] | None, Any] = Field(default=None)
    cities: Union[list[str | None] | None, Any] = Field(default=None)
    rate: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    priority: Union[int | None, Any] = Field(default=None)
    compound: Union[bool | None, Any] = Field(default=None)
    shipping: Union[bool | None, Any] = Field(default=None)
    order: Union[int | None, Any] = Field(default=None)
    class_: Union[str | None, Any] = Field(default=None, alias="class")

class TaxClass(BaseModel):
    """TaxClass type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    slug: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== CHECK RESULT MODEL =====

class WoocommerceCheckResult(BaseModel):
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


class WoocommerceExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class WoocommerceExecuteResultWithMeta(WoocommerceExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class CustomersSearchData(BaseModel):
    """Search result data for customers entity."""
    model_config = ConfigDict(extra="allow")

    avatar_url: str | None = None
    """Avatar URL"""
    billing: dict[str, Any] | None = None
    """List of billing address data"""
    date_created: str | None = None
    """The date the customer was created, in the site's timezone"""
    date_created_gmt: str | None = None
    """The date the customer was created, as GMT"""
    date_modified: str | None = None
    """The date the customer was last modified, in the site's timezone"""
    date_modified_gmt: str | None = None
    """The date the customer was last modified, as GMT"""
    email: str | None = None
    """The email address for the customer"""
    first_name: str | None = None
    """Customer first name"""
    id: int | None = None
    """Unique identifier for the resource"""
    is_paying_customer: bool | None = None
    """Is the customer a paying customer"""
    last_name: str | None = None
    """Customer last name"""
    meta_data: list[Any] | None = None
    """Meta data"""
    role: str | None = None
    """Customer role"""
    shipping: dict[str, Any] | None = None
    """List of shipping address data"""
    username: str | None = None
    """Customer login name"""


class OrdersSearchData(BaseModel):
    """Search result data for orders entity."""
    model_config = ConfigDict(extra="allow")

    billing: dict[str, Any] | None = None
    """Billing address"""
    cart_hash: str | None = None
    """MD5 hash of cart items to ensure orders are not modified"""
    cart_tax: str | None = None
    """Sum of line item taxes only"""
    coupon_lines: list[Any] | None = None
    """Coupons line data"""
    created_via: str | None = None
    """Shows where the order was created"""
    currency: str | None = None
    """Currency the order was created with, in ISO format"""
    customer_id: int | None = None
    """User ID who owns the order (0 for guests)"""
    customer_ip_address: str | None = None
    """Customer's IP address"""
    customer_note: str | None = None
    """Note left by the customer during checkout"""
    customer_user_agent: str | None = None
    """User agent of the customer"""
    date_completed: str | None = None
    """The date the order was completed, in the site's timezone"""
    date_completed_gmt: str | None = None
    """The date the order was completed, as GMT"""
    date_created: str | None = None
    """The date the order was created, in the site's timezone"""
    date_created_gmt: str | None = None
    """The date the order was created, as GMT"""
    date_modified: str | None = None
    """The date the order was last modified, in the site's timezone"""
    date_modified_gmt: str | None = None
    """The date the order was last modified, as GMT"""
    date_paid: str | None = None
    """The date the order was paid, in the site's timezone"""
    date_paid_gmt: str | None = None
    """The date the order was paid, as GMT"""
    discount_tax: str | None = None
    """Total discount tax amount for the order"""
    discount_total: str | None = None
    """Total discount amount for the order"""
    fee_lines: list[Any] | None = None
    """Fee lines data"""
    id: int | None = None
    """Unique identifier for the resource"""
    line_items: list[Any] | None = None
    """Line items data"""
    meta_data: list[Any] | None = None
    """Meta data"""
    number: str | None = None
    """Order number"""
    order_key: str | None = None
    """Order key"""
    parent_id: int | None = None
    """Parent order ID"""
    payment_method: str | None = None
    """Payment method ID"""
    payment_method_title: str | None = None
    """Payment method title"""
    prices_include_tax: bool | None = None
    """True if the prices included tax during checkout"""
    refunds: list[Any] | None = None
    """List of refunds"""
    shipping: dict[str, Any] | None = None
    """Shipping address"""
    shipping_lines: list[Any] | None = None
    """Shipping lines data"""
    shipping_tax: str | None = None
    """Total shipping tax amount for the order"""
    shipping_total: str | None = None
    """Total shipping amount for the order"""
    status: str | None = None
    """Order status"""
    tax_lines: list[Any] | None = None
    """Tax lines data"""
    total: str | None = None
    """Grand total"""
    total_tax: str | None = None
    """Sum of all taxes"""
    transaction_id: str | None = None
    """Unique transaction ID"""
    version: str | None = None
    """Version of WooCommerce which last updated the order"""


class ProductsSearchData(BaseModel):
    """Search result data for products entity."""
    model_config = ConfigDict(extra="allow")

    attributes: list[Any] | None = None
    """List of attributes"""
    average_rating: str | None = None
    """Reviews average rating"""
    backordered: bool | None = None
    """Shows if the product is on backordered"""
    backorders: str | None = None
    """If managing stock, this controls if backorders are allowed"""
    backorders_allowed: bool | None = None
    """Shows if backorders are allowed"""
    button_text: str | None = None
    """Product external button text"""
    catalog_visibility: str | None = None
    """Catalog visibility"""
    categories: list[Any] | None = None
    """List of categories"""
    cross_sell_ids: list[Any] | None = None
    """List of cross-sell products IDs"""
    date_created: str | None = None
    """The date the product was created"""
    date_created_gmt: str | None = None
    """The date the product was created, as GMT"""
    date_modified: str | None = None
    """The date the product was last modified"""
    date_modified_gmt: str | None = None
    """The date the product was last modified, as GMT"""
    date_on_sale_from: str | None = None
    """Start date of sale price"""
    date_on_sale_from_gmt: str | None = None
    """Start date of sale price, as GMT"""
    date_on_sale_to: str | None = None
    """End date of sale price"""
    date_on_sale_to_gmt: str | None = None
    """End date of sale price, as GMT"""
    default_attributes: list[Any] | None = None
    """Defaults variation attributes"""
    description: str | None = None
    """Product description"""
    dimensions: dict[str, Any] | None = None
    """Product dimensions"""
    download_expiry: int | None = None
    """Number of days until access to downloadable files expires"""
    download_limit: int | None = None
    """Number of times downloadable files can be downloaded"""
    downloadable: bool | None = None
    """If the product is downloadable"""
    downloads: list[Any] | None = None
    """List of downloadable files"""
    external_url: str | None = None
    """Product external URL"""
    grouped_products: list[Any] | None = None
    """List of grouped products ID"""
    id: int | None = None
    """Unique identifier for the resource"""
    images: list[Any] | None = None
    """List of images"""
    manage_stock: bool | None = None
    """Stock management at product level"""
    menu_order: int | None = None
    """Menu order"""
    meta_data: list[Any] | None = None
    """Meta data"""
    name: str | None = None
    """Product name"""
    on_sale: bool | None = None
    """Shows if the product is on sale"""
    parent_id: int | None = None
    """Product parent ID"""
    permalink: str | None = None
    """Product URL"""
    price: str | None = None
    """Current product price"""
    price_html: str | None = None
    """Price formatted in HTML"""
    purchasable: bool | None = None
    """Shows if the product can be bought"""
    purchase_note: str | None = None
    """Note to send customer after purchase"""
    rating_count: int | None = None
    """Amount of reviews"""
    regular_price: str | None = None
    """Product regular price"""
    related_ids: list[Any] | None = None
    """List of related products IDs"""
    reviews_allowed: bool | None = None
    """Allow reviews"""
    sale_price: str | None = None
    """Product sale price"""
    shipping_class: str | None = None
    """Shipping class slug"""
    shipping_class_id: int | None = None
    """Shipping class ID"""
    shipping_required: bool | None = None
    """Shows if the product needs to be shipped"""
    shipping_taxable: bool | None = None
    """Shows if product shipping is taxable"""
    short_description: str | None = None
    """Product short description"""
    sku: str | None = None
    """Unique identifier (SKU)"""
    slug: str | None = None
    """Product slug"""
    sold_individually: bool | None = None
    """Allow one item per order"""
    status: str | None = None
    """Product status"""
    stock_quantity: int | None = None
    """Stock quantity"""
    stock_status: str | None = None
    """Controls the stock status"""
    tags: list[Any] | None = None
    """List of tags"""
    tax_class: str | None = None
    """Tax class"""
    tax_status: str | None = None
    """Tax status"""
    total_sales: int | None = None
    """Amount of sales"""
    type_: str | None = None
    """Product type"""
    upsell_ids: list[Any] | None = None
    """List of up-sell products IDs"""
    variations: list[Any] | None = None
    """List of variations IDs"""
    virtual: bool | None = None
    """If the product is virtual"""
    weight: str | None = None
    """Product weight"""


class CouponsSearchData(BaseModel):
    """Search result data for coupons entity."""
    model_config = ConfigDict(extra="allow")

    amount: str | None = None
    """The amount of discount"""
    code: str | None = None
    """Coupon code"""
    date_created: str | None = None
    """The date the coupon was created"""
    date_created_gmt: str | None = None
    """The date the coupon was created, as GMT"""
    date_expires: str | None = None
    """The date the coupon expires"""
    date_expires_gmt: str | None = None
    """The date the coupon expires, as GMT"""
    date_modified: str | None = None
    """The date the coupon was last modified"""
    date_modified_gmt: str | None = None
    """The date the coupon was last modified, as GMT"""
    description: str | None = None
    """Coupon description"""
    discount_type: str | None = None
    """Determines the type of discount"""
    email_restrictions: list[Any] | None = None
    """List of email addresses that can use this coupon"""
    exclude_sale_items: bool | None = None
    """If true, not applied to sale items"""
    excluded_product_categories: list[Any] | None = None
    """Excluded category IDs"""
    excluded_product_ids: list[Any] | None = None
    """Excluded product IDs"""
    free_shipping: bool | None = None
    """Enables free shipping"""
    id: int | None = None
    """Unique identifier"""
    individual_use: bool | None = None
    """Can only be used individually"""
    limit_usage_to_x_items: int | None = None
    """Max cart items coupon applies to"""
    maximum_amount: str | None = None
    """Maximum order amount"""
    meta_data: list[Any] | None = None
    """Meta data"""
    minimum_amount: str | None = None
    """Minimum order amount"""
    product_categories: list[Any] | None = None
    """Applicable category IDs"""
    product_ids: list[Any] | None = None
    """Applicable product IDs"""
    usage_count: int | None = None
    """Times used"""
    usage_limit: int | None = None
    """Total usage limit"""
    usage_limit_per_user: int | None = None
    """Per-customer usage limit"""
    used_by: list[Any] | None = None
    """Users who have used the coupon"""


class ProductCategoriesSearchData(BaseModel):
    """Search result data for product_categories entity."""
    model_config = ConfigDict(extra="allow")

    count: int | None = None
    """Number of published products for the resource"""
    description: str | None = None
    """HTML description of the resource"""
    display: str | None = None
    """Category archive display type"""
    id: int | None = None
    """Unique identifier for the resource"""
    image: list[Any] | None = None
    """Image data"""
    menu_order: int | None = None
    """Menu order"""
    name: str | None = None
    """Category name"""
    parent: int | None = None
    """The ID for the parent of the resource"""
    slug: str | None = None
    """An alphanumeric identifier"""


class ProductTagsSearchData(BaseModel):
    """Search result data for product_tags entity."""
    model_config = ConfigDict(extra="allow")

    count: int | None = None
    """Number of published products"""
    description: str | None = None
    """HTML description"""
    id: int | None = None
    """Unique identifier"""
    name: str | None = None
    """Tag name"""
    slug: str | None = None
    """Alphanumeric identifier"""


class ProductReviewsSearchData(BaseModel):
    """Search result data for product_reviews entity."""
    model_config = ConfigDict(extra="allow")

    date_created: str | None = None
    """The date the review was created"""
    date_created_gmt: str | None = None
    """The date the review was created, as GMT"""
    id: int | None = None
    """Unique identifier"""
    product_id: int | None = None
    """Product the review belongs to"""
    rating: int | None = None
    """Review rating (0 to 5)"""
    review: str | None = None
    """The content of the review"""
    reviewer: str | None = None
    """Reviewer name"""
    reviewer_email: str | None = None
    """Reviewer email"""
    status: str | None = None
    """Status of the review"""
    verified: bool | None = None
    """Shows if the reviewer bought the product"""


class ProductAttributesSearchData(BaseModel):
    """Search result data for product_attributes entity."""
    model_config = ConfigDict(extra="allow")

    has_archives: bool | None = None
    """Enable/Disable attribute archives"""
    id: int | None = None
    """Unique identifier"""
    name: str | None = None
    """Attribute name"""
    order_by: str | None = None
    """Default sort order"""
    slug: str | None = None
    """Alphanumeric identifier"""
    type_: str | None = None
    """Type of attribute"""


class ProductVariationsSearchData(BaseModel):
    """Search result data for product_variations entity."""
    model_config = ConfigDict(extra="allow")

    attributes: list[Any] | None = None
    """List of attributes"""
    backordered: bool | None = None
    """On backordered"""
    backorders: str | None = None
    """Backorders allowed setting"""
    backorders_allowed: bool | None = None
    """Shows if backorders are allowed"""
    date_created: str | None = None
    """The date the variation was created"""
    date_created_gmt: str | None = None
    """The date the variation was created, as GMT"""
    date_modified: str | None = None
    """The date the variation was last modified"""
    date_modified_gmt: str | None = None
    """The date the variation was last modified, as GMT"""
    date_on_sale_from: str | None = None
    """Start date of sale price"""
    date_on_sale_from_gmt: str | None = None
    """Start date of sale price, as GMT"""
    date_on_sale_to: str | None = None
    """End date of sale price"""
    date_on_sale_to_gmt: str | None = None
    """End date of sale price, as GMT"""
    description: str | None = None
    """Variation description"""
    dimensions: dict[str, Any] | None = None
    """Variation dimensions"""
    download_expiry: int | None = None
    """Days until access expires"""
    download_limit: int | None = None
    """Download limit"""
    downloadable: bool | None = None
    """If downloadable"""
    downloads: list[Any] | None = None
    """Downloadable files"""
    id: int | None = None
    """Unique identifier"""
    image: list[Any] | None = None
    """Variation image data"""
    manage_stock: str | None = None
    """Stock management at variation level"""
    menu_order: int | None = None
    """Menu order"""
    meta_data: list[Any] | None = None
    """Meta data"""
    on_sale: bool | None = None
    """Shows if on sale"""
    permalink: str | None = None
    """Variation URL"""
    price: str | None = None
    """Current variation price"""
    purchasable: bool | None = None
    """Can be bought"""
    regular_price: str | None = None
    """Variation regular price"""
    sale_price: str | None = None
    """Variation sale price"""
    shipping_class: str | None = None
    """Shipping class slug"""
    shipping_class_id: int | None = None
    """Shipping class ID"""
    sku: str | None = None
    """Unique identifier (SKU)"""
    status: str | None = None
    """Variation status"""
    stock_quantity: int | None = None
    """Stock quantity"""
    stock_status: str | None = None
    """Controls the stock status"""
    tax_class: str | None = None
    """Tax class"""
    tax_status: str | None = None
    """Tax status"""
    virtual: bool | None = None
    """If virtual"""
    weight: str | None = None
    """Variation weight"""


class OrderNotesSearchData(BaseModel):
    """Search result data for order_notes entity."""
    model_config = ConfigDict(extra="allow")

    author: str | None = None
    """Order note author"""
    date_created: str | None = None
    """The date the order note was created"""
    date_created_gmt: str | None = None
    """The date the order note was created, as GMT"""
    id: int | None = None
    """Unique identifier"""
    note: str | None = None
    """Order note content"""


class RefundsSearchData(BaseModel):
    """Search result data for refunds entity."""
    model_config = ConfigDict(extra="allow")

    amount: str | None = None
    """Refund amount"""
    date_created: str | None = None
    """The date the refund was created"""
    date_created_gmt: str | None = None
    """The date the refund was created, as GMT"""
    id: int | None = None
    """Unique identifier"""
    line_items: list[Any] | None = None
    """Line items data"""
    meta_data: list[Any] | None = None
    """Meta data"""
    reason: str | None = None
    """Reason for refund"""
    refunded_by: int | None = None
    """User ID of user who created the refund"""
    refunded_payment: bool | None = None
    """If the payment was refunded via the API"""


class PaymentGatewaysSearchData(BaseModel):
    """Search result data for payment_gateways entity."""
    model_config = ConfigDict(extra="allow")

    description: str | None = None
    """Payment gateway description on checkout"""
    enabled: bool | None = None
    """Payment gateway enabled status"""
    id: str | None = None
    """Payment gateway ID"""
    method_description: str | None = None
    """Payment gateway method description"""
    method_supports: list[Any] | None = None
    """Supported features"""
    method_title: str | None = None
    """Payment gateway method title"""
    order: Any = None
    """Payment gateway sort order"""
    settings: dict[str, Any] | None = None
    """Payment gateway settings"""
    title: str | None = None
    """Payment gateway title on checkout"""


class ShippingMethodsSearchData(BaseModel):
    """Search result data for shipping_methods entity."""
    model_config = ConfigDict(extra="allow")

    description: str | None = None
    """Shipping method description"""
    id: str | None = None
    """Method ID"""
    title: str | None = None
    """Shipping method title"""


class ShippingZonesSearchData(BaseModel):
    """Search result data for shipping_zones entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier"""
    name: str | None = None
    """Shipping zone name"""
    order: int | None = None
    """Shipping zone order"""


class TaxRatesSearchData(BaseModel):
    """Search result data for tax_rates entity."""
    model_config = ConfigDict(extra="allow")

    cities: list[Any] | None = None
    """City names"""
    city: str | None = None
    """City name"""
    class_: str | None = None
    """Tax class"""
    compound: bool | None = None
    """Whether this is a compound rate"""
    country: str | None = None
    """Country ISO 3166 code"""
    id: int | None = None
    """Unique identifier"""
    name: str | None = None
    """Tax rate name"""
    order: int | None = None
    """Order in queries"""
    postcode: str | None = None
    """Postcode/ZIP"""
    postcodes: list[Any] | None = None
    """Postcodes/ZIPs"""
    priority: int | None = None
    """Tax priority"""
    rate: str | None = None
    """Tax rate"""
    shipping: bool | None = None
    """Applied to shipping"""
    state: str | None = None
    """State code"""


class TaxClassesSearchData(BaseModel):
    """Search result data for tax_classes entity."""
    model_config = ConfigDict(extra="allow")

    name: str | None = None
    """Tax class name"""
    slug: str | None = None
    """Unique identifier"""


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

CustomersSearchResult = AirbyteSearchResult[CustomersSearchData]
"""Search result type for customers entity."""

OrdersSearchResult = AirbyteSearchResult[OrdersSearchData]
"""Search result type for orders entity."""

ProductsSearchResult = AirbyteSearchResult[ProductsSearchData]
"""Search result type for products entity."""

CouponsSearchResult = AirbyteSearchResult[CouponsSearchData]
"""Search result type for coupons entity."""

ProductCategoriesSearchResult = AirbyteSearchResult[ProductCategoriesSearchData]
"""Search result type for product_categories entity."""

ProductTagsSearchResult = AirbyteSearchResult[ProductTagsSearchData]
"""Search result type for product_tags entity."""

ProductReviewsSearchResult = AirbyteSearchResult[ProductReviewsSearchData]
"""Search result type for product_reviews entity."""

ProductAttributesSearchResult = AirbyteSearchResult[ProductAttributesSearchData]
"""Search result type for product_attributes entity."""

ProductVariationsSearchResult = AirbyteSearchResult[ProductVariationsSearchData]
"""Search result type for product_variations entity."""

OrderNotesSearchResult = AirbyteSearchResult[OrderNotesSearchData]
"""Search result type for order_notes entity."""

RefundsSearchResult = AirbyteSearchResult[RefundsSearchData]
"""Search result type for refunds entity."""

PaymentGatewaysSearchResult = AirbyteSearchResult[PaymentGatewaysSearchData]
"""Search result type for payment_gateways entity."""

ShippingMethodsSearchResult = AirbyteSearchResult[ShippingMethodsSearchData]
"""Search result type for shipping_methods entity."""

ShippingZonesSearchResult = AirbyteSearchResult[ShippingZonesSearchData]
"""Search result type for shipping_zones entity."""

TaxRatesSearchResult = AirbyteSearchResult[TaxRatesSearchData]
"""Search result type for tax_rates entity."""

TaxClassesSearchResult = AirbyteSearchResult[TaxClassesSearchData]
"""Search result type for tax_classes entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

CustomersListResult = WoocommerceExecuteResult[list[Customer]]
"""Result type for customers.list operation."""

OrdersListResult = WoocommerceExecuteResult[list[Order]]
"""Result type for orders.list operation."""

ProductsListResult = WoocommerceExecuteResult[list[Product]]
"""Result type for products.list operation."""

CouponsListResult = WoocommerceExecuteResult[list[Coupon]]
"""Result type for coupons.list operation."""

ProductCategoriesListResult = WoocommerceExecuteResult[list[ProductCategory]]
"""Result type for product_categories.list operation."""

ProductTagsListResult = WoocommerceExecuteResult[list[ProductTag]]
"""Result type for product_tags.list operation."""

ProductReviewsListResult = WoocommerceExecuteResult[list[ProductReview]]
"""Result type for product_reviews.list operation."""

ProductAttributesListResult = WoocommerceExecuteResult[list[ProductAttribute]]
"""Result type for product_attributes.list operation."""

ProductVariationsListResult = WoocommerceExecuteResult[list[ProductVariation]]
"""Result type for product_variations.list operation."""

OrderNotesListResult = WoocommerceExecuteResult[list[OrderNote]]
"""Result type for order_notes.list operation."""

RefundsListResult = WoocommerceExecuteResult[list[Refund]]
"""Result type for refunds.list operation."""

PaymentGatewaysListResult = WoocommerceExecuteResult[list[PaymentGateway]]
"""Result type for payment_gateways.list operation."""

ShippingMethodsListResult = WoocommerceExecuteResult[list[ShippingMethod]]
"""Result type for shipping_methods.list operation."""

ShippingZonesListResult = WoocommerceExecuteResult[list[ShippingZone]]
"""Result type for shipping_zones.list operation."""

TaxRatesListResult = WoocommerceExecuteResult[list[TaxRate]]
"""Result type for tax_rates.list operation."""

TaxClassesListResult = WoocommerceExecuteResult[list[TaxClass]]
"""Result type for tax_classes.list operation."""

