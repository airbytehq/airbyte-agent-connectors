"""
Type definitions for shopify connector.
"""
from __future__ import annotations

from airbyte_agent_sdk.types import AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

class CustomersCreateParamsInputAddressesItem(TypedDict):
    """Nested schema for CustomersCreateParamsInput.addresses_item"""
    address1: NotRequired[str]
    address2: NotRequired[str]
    city: NotRequired[str]
    province: NotRequired[str]
    zip: NotRequired[str]
    country_code: NotRequired[str]
    phone: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]

class CustomersCreateParamsInput(TypedDict):
    """CustomerInput object"""
    email: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    phone: NotRequired[str]
    note: NotRequired[str]
    tags: NotRequired[list[str]]
    tax_exempt: NotRequired[bool]
    addresses: NotRequired[list[CustomersCreateParamsInputAddressesItem]]

class CustomersUpdateParamsInput(TypedDict):
    """CustomerInput object with id"""
    id: str
    email: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    phone: NotRequired[str]
    note: NotRequired[str]
    tags: NotRequired[list[str]]
    tax_exempt: NotRequired[bool]

class CustomersDeleteParamsInput(TypedDict):
    """Nested schema for CustomersDeleteParams.input"""
    id: str

class ProductsCreateParamsProduct(TypedDict):
    """ProductCreateInput object"""
    title: str
    description_html: NotRequired[str]
    vendor: NotRequired[str]
    product_type: NotRequired[str]
    tags: NotRequired[list[str]]
    status: NotRequired[str]

class ProductsCreateParamsMediaItem(TypedDict):
    """Nested schema for ProductsCreateParams.media_item"""
    original_source: NotRequired[str]
    media_content_type: NotRequired[str]

class ProductsUpdateParamsProduct(TypedDict):
    """ProductUpdateInput object"""
    id: str
    title: NotRequired[str]
    description_html: NotRequired[str]
    vendor: NotRequired[str]
    product_type: NotRequired[str]
    tags: NotRequired[list[str]]
    status: NotRequired[str]

class ProductsDeleteParamsInput(TypedDict):
    """Nested schema for ProductsDeleteParams.input"""
    id: str

class ProductVariantsCreateParamsVariantsItemInventoryitem(TypedDict):
    """Inventory-item attributes for the variant. As of Admin API 2024-07+ the SKU is no longer a variant-level field and must be set here (a top-level sku is ignored/rejected by productVariantsBulkCreate)."""
    sku: NotRequired[str]

class ProductVariantsCreateParamsVariantsItemOptionvaluesItem(TypedDict):
    """Nested schema for ProductVariantsCreateParamsVariantsItem.optionValues_item"""
    option_name: str
    name: str

class ProductVariantsCreateParamsVariantsItem(TypedDict):
    """Nested schema for ProductVariantsCreateParams.variants_item"""
    price: NotRequired[str]
    barcode: NotRequired[str]
    compare_at_price: NotRequired[str]
    inventory_item: NotRequired[ProductVariantsCreateParamsVariantsItemInventoryitem]
    option_values: NotRequired[list[ProductVariantsCreateParamsVariantsItemOptionvaluesItem]]

class ProductVariantsUpdateParamsVariantsItemInventoryitem(TypedDict):
    """Inventory-item attributes for the variant. As of Admin API 2024-07+ the SKU is no longer a variant-level field and must be set here (a top-level sku is ignored/rejected by productVariantsBulkUpdate, which silently returns null instead of updating)."""
    sku: NotRequired[str]

class ProductVariantsUpdateParamsVariantsItem(TypedDict):
    """Nested schema for ProductVariantsUpdateParams.variants_item"""
    id: str
    price: NotRequired[str]
    barcode: NotRequired[str]
    compare_at_price: NotRequired[str]
    inventory_item: NotRequired[ProductVariantsUpdateParamsVariantsItemInventoryitem]

class OrdersCreateParamsOrderLineitemsItemPricesetShopmoney(TypedDict):
    """Nested schema for OrdersCreateParamsOrderLineitemsItemPriceset.shopMoney"""
    amount: NotRequired[str]
    currency_code: NotRequired[str]

class OrdersCreateParamsOrderLineitemsItemPriceset(TypedDict):
    """Nested schema for OrdersCreateParamsOrderLineitemsItem.priceSet"""
    shop_money: NotRequired[OrdersCreateParamsOrderLineitemsItemPricesetShopmoney]

class OrdersCreateParamsOrderLineitemsItem(TypedDict):
    """Nested schema for OrdersCreateParamsOrder.lineItems_item"""
    variant_id: NotRequired[str]
    quantity: NotRequired[int]
    title: NotRequired[str]
    price_set: NotRequired[OrdersCreateParamsOrderLineitemsItemPriceset]

class OrdersCreateParamsOrderShippingaddress(TypedDict):
    """Nested schema for OrdersCreateParamsOrder.shippingAddress"""
    address1: NotRequired[str]
    city: NotRequired[str]
    province_code: NotRequired[str]
    zip: NotRequired[str]
    country_code: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]

class OrdersCreateParamsOrder(TypedDict):
    """OrderCreateOrderInput object"""
    line_items: list[OrdersCreateParamsOrderLineitemsItem]
    customer_id: NotRequired[str]
    email: NotRequired[str]
    note: NotRequired[str]
    tags: NotRequired[list[str]]
    shipping_address: NotRequired[OrdersCreateParamsOrderShippingaddress]

class OrdersCreateParamsOptions(TypedDict):
    """OrderCreateOptionsInput"""
    inventory_behaviour: NotRequired[str]

class OrdersUpdateParamsInputShippingaddress(TypedDict):
    """Nested schema for OrdersUpdateParamsInput.shippingAddress"""
    address1: NotRequired[str]
    city: NotRequired[str]
    province_code: NotRequired[str]
    zip: NotRequired[str]
    country_code: NotRequired[str]

class OrdersUpdateParamsInput(TypedDict):
    """Nested schema for OrdersUpdateParams.input"""
    id: str
    email: NotRequired[str]
    note: NotRequired[str]
    tags: NotRequired[list[str]]
    shipping_address: NotRequired[OrdersUpdateParamsInputShippingaddress]

class DraftOrdersCreateParamsInputLineitemsItem(TypedDict):
    """Nested schema for DraftOrdersCreateParamsInput.lineItems_item"""
    variant_id: NotRequired[str]
    quantity: NotRequired[int]
    title: NotRequired[str]
    original_unit_price: NotRequired[str]

class DraftOrdersCreateParamsInputShippingaddress(TypedDict):
    """Nested schema for DraftOrdersCreateParamsInput.shippingAddress"""
    address1: NotRequired[str]
    city: NotRequired[str]
    province_code: NotRequired[str]
    zip: NotRequired[str]
    country_code: NotRequired[str]

class DraftOrdersCreateParamsInput(TypedDict):
    """DraftOrderInput object"""
    line_items: NotRequired[list[DraftOrdersCreateParamsInputLineitemsItem]]
    customer_id: NotRequired[str]
    email: NotRequired[str]
    note: NotRequired[str]
    tags: NotRequired[list[str]]
    shipping_address: NotRequired[DraftOrdersCreateParamsInputShippingaddress]

class DraftOrdersUpdateParamsInputLineitemsItem(TypedDict):
    """Nested schema for DraftOrdersUpdateParamsInput.lineItems_item"""
    variant_id: NotRequired[str]
    quantity: NotRequired[int]
    title: NotRequired[str]
    original_unit_price: NotRequired[str]

class DraftOrdersUpdateParamsInput(TypedDict):
    """DraftOrderInput object with updated fields"""
    line_items: NotRequired[list[DraftOrdersUpdateParamsInputLineitemsItem]]
    email: NotRequired[str]
    note: NotRequired[str]
    tags: NotRequired[list[str]]

class DraftOrdersDeleteParamsInput(TypedDict):
    """Nested schema for DraftOrdersDeleteParams.input"""
    id: str

class InventorySetCreateParamsInputQuantitiesItem(TypedDict):
    """Nested schema for InventorySetCreateParamsInput.quantities_item"""
    inventory_item_id: str
    location_id: str
    quantity: int

class InventorySetCreateParamsInput(TypedDict):
    """Nested schema for InventorySetCreateParams.input"""
    name: str
    reason: str
    reference_document_uri: NotRequired[str]
    quantities: list[InventorySetCreateParamsInputQuantitiesItem]

class InventoryAdjustCreateParamsInputChangesItem(TypedDict):
    """Nested schema for InventoryAdjustCreateParamsInput.changes_item"""
    inventory_item_id: str
    location_id: str
    delta: int

class InventoryAdjustCreateParamsInput(TypedDict):
    """Nested schema for InventoryAdjustCreateParams.input"""
    name: str
    reason: str
    reference_document_uri: NotRequired[str]
    changes: list[InventoryAdjustCreateParamsInputChangesItem]

class DiscountCodesCreateParamsBasiccodediscountCustomerselection(TypedDict):
    """Which customers can use this discount"""
    all: NotRequired[bool]

class DiscountCodesCreateParamsBasiccodediscountCustomergetsValueDiscountamount(TypedDict):
    """Nested schema for DiscountCodesCreateParamsBasiccodediscountCustomergetsValue.discountAmount"""
    amount: NotRequired[str]
    applies_on_each_item: NotRequired[bool]

class DiscountCodesCreateParamsBasiccodediscountCustomergetsValue(TypedDict):
    """The discount value"""
    percentage: NotRequired[float]
    discount_amount: NotRequired[DiscountCodesCreateParamsBasiccodediscountCustomergetsValueDiscountamount]

class DiscountCodesCreateParamsBasiccodediscountCustomergetsItems(TypedDict):
    """Which items the discount applies to"""
    all: NotRequired[bool]

class DiscountCodesCreateParamsBasiccodediscountCustomergets(TypedDict):
    """What the customer gets from this discount"""
    value: NotRequired[DiscountCodesCreateParamsBasiccodediscountCustomergetsValue]
    items: NotRequired[DiscountCodesCreateParamsBasiccodediscountCustomergetsItems]

class DiscountCodesCreateParamsBasiccodediscount(TypedDict):
    """Nested schema for DiscountCodesCreateParams.basicCodeDiscount"""
    title: str
    code: str
    starts_at: str
    ends_at: NotRequired[str]
    usage_limit: NotRequired[int]
    customer_selection: DiscountCodesCreateParamsBasiccodediscountCustomerselection
    customer_gets: DiscountCodesCreateParamsBasiccodediscountCustomergets

class DiscountCodesUpdateParamsBasiccodediscount(TypedDict):
    """Nested schema for DiscountCodesUpdateParams.basicCodeDiscount"""
    title: NotRequired[str]
    code: NotRequired[str]
    starts_at: NotRequired[str]
    ends_at: NotRequired[str]
    usage_limit: NotRequired[int]

class MetafieldsCreateParamsMetafieldsItem(TypedDict):
    """Nested schema for MetafieldsCreateParams.metafields_item"""
    namespace: str
    key: str
    type_: str
    value: str
    owner_id: str

class MetafieldsDeleteParamsMetafieldsItem(TypedDict):
    """Nested schema for MetafieldsDeleteParams.metafields_item"""
    owner_id: str
    namespace: str
    key: str

class CustomCollectionsCreateParamsInputRulesetRulesItem(TypedDict):
    """Nested schema for CustomCollectionsCreateParamsInputRuleset.rules_item"""
    column: NotRequired[str]
    relation: NotRequired[str]
    condition: NotRequired[str]

class CustomCollectionsCreateParamsInputRuleset(TypedDict):
    """Rule set for smart collections"""
    applied_disjunctively: NotRequired[bool]
    rules: NotRequired[list[CustomCollectionsCreateParamsInputRulesetRulesItem]]

class CustomCollectionsCreateParamsInput(TypedDict):
    """Nested schema for CustomCollectionsCreateParams.input"""
    title: str
    description_html: NotRequired[str]
    handle: NotRequired[str]
    sort_order: NotRequired[str]
    template_suffix: NotRequired[str]
    rule_set: NotRequired[CustomCollectionsCreateParamsInputRuleset]

class CustomCollectionsUpdateParamsInput(TypedDict):
    """Nested schema for CustomCollectionsUpdateParams.input"""
    id: str
    title: NotRequired[str]
    description_html: NotRequired[str]
    handle: NotRequired[str]
    sort_order: NotRequired[str]

class CustomCollectionsDeleteParamsInput(TypedDict):
    """Nested schema for CustomCollectionsDeleteParams.input"""
    id: str

class PagesCreateParamsPage(TypedDict):
    """Nested schema for PagesCreateParams.page"""
    title: str
    body: NotRequired[str]
    handle: NotRequired[str]
    is_published: NotRequired[bool]

class PagesUpdateParamsPage(TypedDict):
    """Nested schema for PagesUpdateParams.page"""
    title: NotRequired[str]
    body: NotRequired[str]
    handle: NotRequired[str]
    is_published: NotRequired[bool]

class BlogsCreateParamsBlog(TypedDict):
    """Nested schema for BlogsCreateParams.blog"""
    title: str
    handle: NotRequired[str]

class BlogsUpdateParamsBlog(TypedDict):
    """Nested schema for BlogsUpdateParams.blog"""
    title: NotRequired[str]
    handle: NotRequired[str]

class ArticlesCreateParamsArticleAuthor(TypedDict):
    """Author of the article. Required by Shopify's articleCreate mutation (ArticleCreateInput.author is non-null)."""
    name: str

class ArticlesCreateParamsArticle(TypedDict):
    """Nested schema for ArticlesCreateParams.article"""
    title: str
    blog_id: str
    body: NotRequired[str]
    handle: NotRequired[str]
    is_published: NotRequired[bool]
    tags: NotRequired[list[str]]
    author: ArticlesCreateParamsArticleAuthor

class ArticlesUpdateParamsArticle(TypedDict):
    """Nested schema for ArticlesUpdateParams.article"""
    title: NotRequired[str]
    body: NotRequired[str]
    handle: NotRequired[str]
    is_published: NotRequired[bool]
    tags: NotRequired[list[str]]

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

class PagesListParams(TypedDict):
    """Parameters for pages.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]
    published_status: NotRequired[str]

class PagesGetParams(TypedDict):
    """Parameters for pages.get operation"""
    page_id: str

class BlogsListParams(TypedDict):
    """Parameters for blogs.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]

class BlogsGetParams(TypedDict):
    """Parameters for blogs.get operation"""
    blog_id: str

class ArticlesListParams(TypedDict):
    """Parameters for articles.list operation"""
    blog_id: str
    limit: NotRequired[int]
    since_id: NotRequired[int]
    created_at_min: NotRequired[str]
    created_at_max: NotRequired[str]
    updated_at_min: NotRequired[str]
    updated_at_max: NotRequired[str]
    published_status: NotRequired[str]

class ArticlesGetParams(TypedDict):
    """Parameters for articles.get operation"""
    blog_id: str
    article_id: str

class BalanceTransactionsListParams(TypedDict):
    """Parameters for balance_transactions.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    payout_id: NotRequired[int]
    payout_status: NotRequired[str]

class DisputesListParams(TypedDict):
    """Parameters for disputes.list operation"""
    limit: NotRequired[int]
    since_id: NotRequired[int]
    status: NotRequired[str]
    initiated_at: NotRequired[str]

class DisputesGetParams(TypedDict):
    """Parameters for disputes.get operation"""
    dispute_id: str

class MetafieldPagesListParams(TypedDict):
    """Parameters for metafield_pages.list operation"""
    page_id: str
    limit: NotRequired[int]

class MetafieldBlogsListParams(TypedDict):
    """Parameters for metafield_blogs.list operation"""
    blog_id: str
    limit: NotRequired[int]

class MetafieldArticlesListParams(TypedDict):
    """Parameters for metafield_articles.list operation"""
    blog_id: str
    article_id: str
    limit: NotRequired[int]

class CustomersCreateParams(TypedDict):
    """Parameters for customers.create operation"""
    input: CustomersCreateParamsInput

class CustomersUpdateParams(TypedDict):
    """Parameters for customers.update operation"""
    input: CustomersUpdateParamsInput

class CustomersDeleteParams(TypedDict):
    """Parameters for customers.delete operation"""
    input: CustomersDeleteParamsInput

class ProductsCreateParams(TypedDict):
    """Parameters for products.create operation"""
    product: ProductsCreateParamsProduct
    media: NotRequired[list[ProductsCreateParamsMediaItem]]

class ProductsUpdateParams(TypedDict):
    """Parameters for products.update operation"""
    product: ProductsUpdateParamsProduct

class ProductsDeleteParams(TypedDict):
    """Parameters for products.delete operation"""
    input: ProductsDeleteParamsInput

class ProductVariantsCreateParams(TypedDict):
    """Parameters for product_variants.create operation"""
    product_id: str
    variants: list[ProductVariantsCreateParamsVariantsItem]

class ProductVariantsUpdateParams(TypedDict):
    """Parameters for product_variants.update operation"""
    product_id: str
    variants: list[ProductVariantsUpdateParamsVariantsItem]

class ProductVariantsDeleteParams(TypedDict):
    """Parameters for product_variants.delete operation"""
    product_id: str
    variants_ids: list[str]

class OrdersCreateParams(TypedDict):
    """Parameters for orders.create operation"""
    order: OrdersCreateParamsOrder
    options: NotRequired[OrdersCreateParamsOptions]

class OrdersUpdateParams(TypedDict):
    """Parameters for orders.update operation"""
    input: OrdersUpdateParamsInput

class OrdersDeleteParams(TypedDict):
    """Parameters for orders.delete operation"""
    order_id: str
    reason: str
    notify_customer: NotRequired[bool]
    refund: NotRequired[bool]
    restock: bool
    staff_note: NotRequired[str]

class DraftOrdersCreateParams(TypedDict):
    """Parameters for draft_orders.create operation"""
    input: DraftOrdersCreateParamsInput

class DraftOrdersUpdateParams(TypedDict):
    """Parameters for draft_orders.update operation"""
    id: str
    input: DraftOrdersUpdateParamsInput

class DraftOrdersDeleteParams(TypedDict):
    """Parameters for draft_orders.delete operation"""
    input: DraftOrdersDeleteParamsInput

class DraftOrderCompleteUpdateParams(TypedDict):
    """Parameters for draft_order_complete.update operation"""
    id: str
    payment_pending: NotRequired[bool]

class InventorySetCreateParams(TypedDict):
    """Parameters for inventory_set.create operation"""
    input: InventorySetCreateParamsInput

class InventoryAdjustCreateParams(TypedDict):
    """Parameters for inventory_adjust.create operation"""
    input: InventoryAdjustCreateParamsInput

class DiscountCodesCreateParams(TypedDict):
    """Parameters for discount_codes.create operation"""
    basic_code_discount: DiscountCodesCreateParamsBasiccodediscount

class DiscountCodesUpdateParams(TypedDict):
    """Parameters for discount_codes.update operation"""
    id: str
    basic_code_discount: DiscountCodesUpdateParamsBasiccodediscount

class DiscountCodesDeleteParams(TypedDict):
    """Parameters for discount_codes.delete operation"""
    id: str

class MetafieldsCreateParams(TypedDict):
    """Parameters for metafields.create operation"""
    metafields: list[MetafieldsCreateParamsMetafieldsItem]

class MetafieldsDeleteParams(TypedDict):
    """Parameters for metafields.delete operation"""
    metafields: list[MetafieldsDeleteParamsMetafieldsItem]

class CustomCollectionsCreateParams(TypedDict):
    """Parameters for custom_collections.create operation"""
    input: CustomCollectionsCreateParamsInput

class CustomCollectionsUpdateParams(TypedDict):
    """Parameters for custom_collections.update operation"""
    input: CustomCollectionsUpdateParamsInput

class CustomCollectionsDeleteParams(TypedDict):
    """Parameters for custom_collections.delete operation"""
    input: CustomCollectionsDeleteParamsInput

class PagesCreateParams(TypedDict):
    """Parameters for pages.create operation"""
    page: PagesCreateParamsPage

class PagesUpdateParams(TypedDict):
    """Parameters for pages.update operation"""
    id: str
    page: PagesUpdateParamsPage

class PagesDeleteParams(TypedDict):
    """Parameters for pages.delete operation"""
    id: str

class BlogsCreateParams(TypedDict):
    """Parameters for blogs.create operation"""
    blog: BlogsCreateParamsBlog

class BlogsUpdateParams(TypedDict):
    """Parameters for blogs.update operation"""
    id: str
    blog: BlogsUpdateParamsBlog

class BlogsDeleteParams(TypedDict):
    """Parameters for blogs.delete operation"""
    id: str

class ArticlesCreateParams(TypedDict):
    """Parameters for articles.create operation"""
    article: ArticlesCreateParamsArticle

class ArticlesUpdateParams(TypedDict):
    """Parameters for articles.update operation"""
    id: str
    article: ArticlesUpdateParamsArticle

class ArticlesDeleteParams(TypedDict):
    """Parameters for articles.delete operation"""
    id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ABANDONED_CHECKOUTS SEARCH TYPES =====

class AbandonedCheckoutsSearchFilter(TypedDict, total=False):
    """Available fields for filtering abandoned_checkouts search queries."""
    id: int | None
    """Unique identifier for the abandoned checkout"""
    token: str | None
    """Unique token identifying the checkout"""
    email: str | None
    """Email address provided for the checkout"""
    phone: str | None
    """Phone number provided for the checkout"""
    name: str | None
    """Shopify-assigned display name for the checkout (e.g. `#C12345`)"""
    currency: str | None
    """ISO 4217 currency code for the checkout totals"""
    total_price: str | None
    """Total price of the checkout in the shop's currency"""
    created_at: str | None
    """ISO 8601 timestamp when the checkout was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the checkout was last updated"""
    completed_at: str | None
    """ISO 8601 timestamp when the checkout was completed, if applicable"""


class AbandonedCheckoutsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the abandoned checkout"""
    token: list[str]
    """Unique token identifying the checkout"""
    email: list[str]
    """Email address provided for the checkout"""
    phone: list[str]
    """Phone number provided for the checkout"""
    name: list[str]
    """Shopify-assigned display name for the checkout (e.g. `#C12345`)"""
    currency: list[str]
    """ISO 4217 currency code for the checkout totals"""
    total_price: list[str]
    """Total price of the checkout in the shop's currency"""
    created_at: list[str]
    """ISO 8601 timestamp when the checkout was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the checkout was last updated"""
    completed_at: list[str]
    """ISO 8601 timestamp when the checkout was completed, if applicable"""


class AbandonedCheckoutsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the abandoned checkout"""
    token: Any
    """Unique token identifying the checkout"""
    email: Any
    """Email address provided for the checkout"""
    phone: Any
    """Phone number provided for the checkout"""
    name: Any
    """Shopify-assigned display name for the checkout (e.g. `#C12345`)"""
    currency: Any
    """ISO 4217 currency code for the checkout totals"""
    total_price: Any
    """Total price of the checkout in the shop's currency"""
    created_at: Any
    """ISO 8601 timestamp when the checkout was created"""
    updated_at: Any
    """ISO 8601 timestamp when the checkout was last updated"""
    completed_at: Any
    """ISO 8601 timestamp when the checkout was completed, if applicable"""


class AbandonedCheckoutsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the abandoned checkout"""
    token: str
    """Unique token identifying the checkout"""
    email: str
    """Email address provided for the checkout"""
    phone: str
    """Phone number provided for the checkout"""
    name: str
    """Shopify-assigned display name for the checkout (e.g. `#C12345`)"""
    currency: str
    """ISO 4217 currency code for the checkout totals"""
    total_price: str
    """Total price of the checkout in the shop's currency"""
    created_at: str
    """ISO 8601 timestamp when the checkout was created"""
    updated_at: str
    """ISO 8601 timestamp when the checkout was last updated"""
    completed_at: str
    """ISO 8601 timestamp when the checkout was completed, if applicable"""


class AbandonedCheckoutsSortFilter(TypedDict, total=False):
    """Available fields for sorting abandoned_checkouts search results."""
    id: AirbyteSortOrder
    """Unique identifier for the abandoned checkout"""
    token: AirbyteSortOrder
    """Unique token identifying the checkout"""
    email: AirbyteSortOrder
    """Email address provided for the checkout"""
    phone: AirbyteSortOrder
    """Phone number provided for the checkout"""
    name: AirbyteSortOrder
    """Shopify-assigned display name for the checkout (e.g. `#C12345`)"""
    currency: AirbyteSortOrder
    """ISO 4217 currency code for the checkout totals"""
    total_price: AirbyteSortOrder
    """Total price of the checkout in the shop's currency"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the checkout was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the checkout was last updated"""
    completed_at: AirbyteSortOrder
    """ISO 8601 timestamp when the checkout was completed, if applicable"""


# Entity-specific condition types for abandoned_checkouts
class AbandonedCheckoutsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AbandonedCheckoutsSearchFilter


class AbandonedCheckoutsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AbandonedCheckoutsSearchFilter


class AbandonedCheckoutsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AbandonedCheckoutsSearchFilter


class AbandonedCheckoutsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AbandonedCheckoutsSearchFilter


class AbandonedCheckoutsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AbandonedCheckoutsSearchFilter


class AbandonedCheckoutsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AbandonedCheckoutsSearchFilter


class AbandonedCheckoutsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AbandonedCheckoutsStringFilter


class AbandonedCheckoutsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AbandonedCheckoutsStringFilter


class AbandonedCheckoutsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AbandonedCheckoutsStringFilter


class AbandonedCheckoutsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AbandonedCheckoutsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AbandonedCheckoutsInCondition = TypedDict("AbandonedCheckoutsInCondition", {"in": AbandonedCheckoutsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AbandonedCheckoutsNotCondition = TypedDict("AbandonedCheckoutsNotCondition", {"not": "AbandonedCheckoutsCondition"}, total=False)
"""Negates the nested condition."""

AbandonedCheckoutsAndCondition = TypedDict("AbandonedCheckoutsAndCondition", {"and": "list[AbandonedCheckoutsCondition]"}, total=False)
"""True if all nested conditions are true."""

AbandonedCheckoutsOrCondition = TypedDict("AbandonedCheckoutsOrCondition", {"or": "list[AbandonedCheckoutsCondition]"}, total=False)
"""True if any nested condition is true."""

AbandonedCheckoutsAnyCondition = TypedDict("AbandonedCheckoutsAnyCondition", {"any": AbandonedCheckoutsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all abandoned_checkouts condition types
AbandonedCheckoutsCondition = (
    AbandonedCheckoutsEqCondition
    | AbandonedCheckoutsNeqCondition
    | AbandonedCheckoutsGtCondition
    | AbandonedCheckoutsGteCondition
    | AbandonedCheckoutsLtCondition
    | AbandonedCheckoutsLteCondition
    | AbandonedCheckoutsInCondition
    | AbandonedCheckoutsLikeCondition
    | AbandonedCheckoutsFuzzyCondition
    | AbandonedCheckoutsKeywordCondition
    | AbandonedCheckoutsContainsCondition
    | AbandonedCheckoutsNotCondition
    | AbandonedCheckoutsAndCondition
    | AbandonedCheckoutsOrCondition
    | AbandonedCheckoutsAnyCondition
)


class AbandonedCheckoutsSearchQuery(TypedDict, total=False):
    """Search query for abandoned_checkouts entity."""
    filter: AbandonedCheckoutsCondition
    sort: list[AbandonedCheckoutsSortFilter]


# ===== COLLECTS SEARCH TYPES =====

class CollectsSearchFilter(TypedDict, total=False):
    """Available fields for filtering collects search queries."""
    id: int | None
    """Unique identifier for the collect"""
    collection_id: int | None
    """Identifier of the collection the product belongs to"""
    product_id: int | None
    """Identifier of the product in the collection"""
    position: int | None
    """Position of the product within the collection"""
    created_at: str | None
    """ISO 8601 timestamp when the collect was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the collect was last updated"""


class CollectsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the collect"""
    collection_id: list[int]
    """Identifier of the collection the product belongs to"""
    product_id: list[int]
    """Identifier of the product in the collection"""
    position: list[int]
    """Position of the product within the collection"""
    created_at: list[str]
    """ISO 8601 timestamp when the collect was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the collect was last updated"""


class CollectsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the collect"""
    collection_id: Any
    """Identifier of the collection the product belongs to"""
    product_id: Any
    """Identifier of the product in the collection"""
    position: Any
    """Position of the product within the collection"""
    created_at: Any
    """ISO 8601 timestamp when the collect was created"""
    updated_at: Any
    """ISO 8601 timestamp when the collect was last updated"""


class CollectsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the collect"""
    collection_id: str
    """Identifier of the collection the product belongs to"""
    product_id: str
    """Identifier of the product in the collection"""
    position: str
    """Position of the product within the collection"""
    created_at: str
    """ISO 8601 timestamp when the collect was created"""
    updated_at: str
    """ISO 8601 timestamp when the collect was last updated"""


class CollectsSortFilter(TypedDict, total=False):
    """Available fields for sorting collects search results."""
    id: AirbyteSortOrder
    """Unique identifier for the collect"""
    collection_id: AirbyteSortOrder
    """Identifier of the collection the product belongs to"""
    product_id: AirbyteSortOrder
    """Identifier of the product in the collection"""
    position: AirbyteSortOrder
    """Position of the product within the collection"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the collect was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the collect was last updated"""


# Entity-specific condition types for collects
class CollectsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CollectsSearchFilter


class CollectsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CollectsSearchFilter


class CollectsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CollectsSearchFilter


class CollectsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CollectsSearchFilter


class CollectsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CollectsSearchFilter


class CollectsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CollectsSearchFilter


class CollectsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CollectsStringFilter


class CollectsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CollectsStringFilter


class CollectsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CollectsStringFilter


class CollectsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CollectsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CollectsInCondition = TypedDict("CollectsInCondition", {"in": CollectsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CollectsNotCondition = TypedDict("CollectsNotCondition", {"not": "CollectsCondition"}, total=False)
"""Negates the nested condition."""

CollectsAndCondition = TypedDict("CollectsAndCondition", {"and": "list[CollectsCondition]"}, total=False)
"""True if all nested conditions are true."""

CollectsOrCondition = TypedDict("CollectsOrCondition", {"or": "list[CollectsCondition]"}, total=False)
"""True if any nested condition is true."""

CollectsAnyCondition = TypedDict("CollectsAnyCondition", {"any": CollectsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all collects condition types
CollectsCondition = (
    CollectsEqCondition
    | CollectsNeqCondition
    | CollectsGtCondition
    | CollectsGteCondition
    | CollectsLtCondition
    | CollectsLteCondition
    | CollectsInCondition
    | CollectsLikeCondition
    | CollectsFuzzyCondition
    | CollectsKeywordCondition
    | CollectsContainsCondition
    | CollectsNotCondition
    | CollectsAndCondition
    | CollectsOrCondition
    | CollectsAnyCondition
)


class CollectsSearchQuery(TypedDict, total=False):
    """Search query for collects entity."""
    filter: CollectsCondition
    sort: list[CollectsSortFilter]


# ===== COUNTRIES SEARCH TYPES =====

class CountriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering countries search queries."""
    id: int | None
    """Unique identifier for the country tax row"""
    name: str | None
    """Human-readable country name"""
    code: str | None
    """ISO 3166-1 alpha-2 country code"""
    tax_name: str | None
    """Localized name of the tax applied in this country"""


class CountriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the country tax row"""
    name: list[str]
    """Human-readable country name"""
    code: list[str]
    """ISO 3166-1 alpha-2 country code"""
    tax_name: list[str]
    """Localized name of the tax applied in this country"""


class CountriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the country tax row"""
    name: Any
    """Human-readable country name"""
    code: Any
    """ISO 3166-1 alpha-2 country code"""
    tax_name: Any
    """Localized name of the tax applied in this country"""


class CountriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the country tax row"""
    name: str
    """Human-readable country name"""
    code: str
    """ISO 3166-1 alpha-2 country code"""
    tax_name: str
    """Localized name of the tax applied in this country"""


class CountriesSortFilter(TypedDict, total=False):
    """Available fields for sorting countries search results."""
    id: AirbyteSortOrder
    """Unique identifier for the country tax row"""
    name: AirbyteSortOrder
    """Human-readable country name"""
    code: AirbyteSortOrder
    """ISO 3166-1 alpha-2 country code"""
    tax_name: AirbyteSortOrder
    """Localized name of the tax applied in this country"""


# Entity-specific condition types for countries
class CountriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CountriesSearchFilter


class CountriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CountriesSearchFilter


class CountriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CountriesSearchFilter


class CountriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CountriesSearchFilter


class CountriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CountriesSearchFilter


class CountriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CountriesSearchFilter


class CountriesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CountriesStringFilter


class CountriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CountriesStringFilter


class CountriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CountriesStringFilter


class CountriesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CountriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CountriesInCondition = TypedDict("CountriesInCondition", {"in": CountriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CountriesNotCondition = TypedDict("CountriesNotCondition", {"not": "CountriesCondition"}, total=False)
"""Negates the nested condition."""

CountriesAndCondition = TypedDict("CountriesAndCondition", {"and": "list[CountriesCondition]"}, total=False)
"""True if all nested conditions are true."""

CountriesOrCondition = TypedDict("CountriesOrCondition", {"or": "list[CountriesCondition]"}, total=False)
"""True if any nested condition is true."""

CountriesAnyCondition = TypedDict("CountriesAnyCondition", {"any": CountriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all countries condition types
CountriesCondition = (
    CountriesEqCondition
    | CountriesNeqCondition
    | CountriesGtCondition
    | CountriesGteCondition
    | CountriesLtCondition
    | CountriesLteCondition
    | CountriesInCondition
    | CountriesLikeCondition
    | CountriesFuzzyCondition
    | CountriesKeywordCondition
    | CountriesContainsCondition
    | CountriesNotCondition
    | CountriesAndCondition
    | CountriesOrCondition
    | CountriesAnyCondition
)


class CountriesSearchQuery(TypedDict, total=False):
    """Search query for countries entity."""
    filter: CountriesCondition
    sort: list[CountriesSortFilter]


# ===== CUSTOM_COLLECTIONS SEARCH TYPES =====

class CustomCollectionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering custom_collections search queries."""
    id: int | None
    """Unique identifier for the custom collection"""
    handle: str | None
    """URL-friendly handle for the custom collection"""
    title: str | None
    """Display title of the custom collection"""
    sort_order: str | None
    """How products are sorted within the collection (e.g. `best-selling`)"""
    published_scope: str | None
    """Publishing scope (`web` or `global`)"""
    published_at: str | None
    """ISO 8601 timestamp when the collection was published"""
    updated_at: str | None
    """ISO 8601 timestamp when the collection was last updated"""


class CustomCollectionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the custom collection"""
    handle: list[str]
    """URL-friendly handle for the custom collection"""
    title: list[str]
    """Display title of the custom collection"""
    sort_order: list[str]
    """How products are sorted within the collection (e.g. `best-selling`)"""
    published_scope: list[str]
    """Publishing scope (`web` or `global`)"""
    published_at: list[str]
    """ISO 8601 timestamp when the collection was published"""
    updated_at: list[str]
    """ISO 8601 timestamp when the collection was last updated"""


class CustomCollectionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the custom collection"""
    handle: Any
    """URL-friendly handle for the custom collection"""
    title: Any
    """Display title of the custom collection"""
    sort_order: Any
    """How products are sorted within the collection (e.g. `best-selling`)"""
    published_scope: Any
    """Publishing scope (`web` or `global`)"""
    published_at: Any
    """ISO 8601 timestamp when the collection was published"""
    updated_at: Any
    """ISO 8601 timestamp when the collection was last updated"""


class CustomCollectionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the custom collection"""
    handle: str
    """URL-friendly handle for the custom collection"""
    title: str
    """Display title of the custom collection"""
    sort_order: str
    """How products are sorted within the collection (e.g. `best-selling`)"""
    published_scope: str
    """Publishing scope (`web` or `global`)"""
    published_at: str
    """ISO 8601 timestamp when the collection was published"""
    updated_at: str
    """ISO 8601 timestamp when the collection was last updated"""


class CustomCollectionsSortFilter(TypedDict, total=False):
    """Available fields for sorting custom_collections search results."""
    id: AirbyteSortOrder
    """Unique identifier for the custom collection"""
    handle: AirbyteSortOrder
    """URL-friendly handle for the custom collection"""
    title: AirbyteSortOrder
    """Display title of the custom collection"""
    sort_order: AirbyteSortOrder
    """How products are sorted within the collection (e.g. `best-selling`)"""
    published_scope: AirbyteSortOrder
    """Publishing scope (`web` or `global`)"""
    published_at: AirbyteSortOrder
    """ISO 8601 timestamp when the collection was published"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the collection was last updated"""


# Entity-specific condition types for custom_collections
class CustomCollectionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CustomCollectionsSearchFilter


class CustomCollectionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CustomCollectionsSearchFilter


class CustomCollectionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CustomCollectionsSearchFilter


class CustomCollectionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CustomCollectionsSearchFilter


class CustomCollectionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CustomCollectionsSearchFilter


class CustomCollectionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CustomCollectionsSearchFilter


class CustomCollectionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CustomCollectionsStringFilter


class CustomCollectionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CustomCollectionsStringFilter


class CustomCollectionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CustomCollectionsStringFilter


class CustomCollectionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CustomCollectionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CustomCollectionsInCondition = TypedDict("CustomCollectionsInCondition", {"in": CustomCollectionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CustomCollectionsNotCondition = TypedDict("CustomCollectionsNotCondition", {"not": "CustomCollectionsCondition"}, total=False)
"""Negates the nested condition."""

CustomCollectionsAndCondition = TypedDict("CustomCollectionsAndCondition", {"and": "list[CustomCollectionsCondition]"}, total=False)
"""True if all nested conditions are true."""

CustomCollectionsOrCondition = TypedDict("CustomCollectionsOrCondition", {"or": "list[CustomCollectionsCondition]"}, total=False)
"""True if any nested condition is true."""

CustomCollectionsAnyCondition = TypedDict("CustomCollectionsAnyCondition", {"any": CustomCollectionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all custom_collections condition types
CustomCollectionsCondition = (
    CustomCollectionsEqCondition
    | CustomCollectionsNeqCondition
    | CustomCollectionsGtCondition
    | CustomCollectionsGteCondition
    | CustomCollectionsLtCondition
    | CustomCollectionsLteCondition
    | CustomCollectionsInCondition
    | CustomCollectionsLikeCondition
    | CustomCollectionsFuzzyCondition
    | CustomCollectionsKeywordCondition
    | CustomCollectionsContainsCondition
    | CustomCollectionsNotCondition
    | CustomCollectionsAndCondition
    | CustomCollectionsOrCondition
    | CustomCollectionsAnyCondition
)


class CustomCollectionsSearchQuery(TypedDict, total=False):
    """Search query for custom_collections entity."""
    filter: CustomCollectionsCondition
    sort: list[CustomCollectionsSortFilter]


# ===== CUSTOMERS SEARCH TYPES =====

class CustomersSearchFilter(TypedDict, total=False):
    """Available fields for filtering customers search queries."""
    id: int | None
    """Unique identifier for the customer"""
    email: str | None
    """Primary email address of the customer"""
    phone: str | None
    """Primary phone number of the customer"""
    first_name: str | None
    """First name of the customer"""
    last_name: str | None
    """Last name of the customer"""
    state: str | None
    """Account state (`disabled`, `invited`, `enabled`, `declined`)"""
    orders_count: int | None
    """Number of orders placed by the customer"""
    total_spent: str | None
    """Total lifetime amount spent by the customer"""
    currency: str | None
    """ISO 4217 currency code for the customer's total spend"""
    created_at: str | None
    """ISO 8601 timestamp when the customer record was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the customer record was last updated"""


class CustomersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the customer"""
    email: list[str]
    """Primary email address of the customer"""
    phone: list[str]
    """Primary phone number of the customer"""
    first_name: list[str]
    """First name of the customer"""
    last_name: list[str]
    """Last name of the customer"""
    state: list[str]
    """Account state (`disabled`, `invited`, `enabled`, `declined`)"""
    orders_count: list[int]
    """Number of orders placed by the customer"""
    total_spent: list[str]
    """Total lifetime amount spent by the customer"""
    currency: list[str]
    """ISO 4217 currency code for the customer's total spend"""
    created_at: list[str]
    """ISO 8601 timestamp when the customer record was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the customer record was last updated"""


class CustomersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the customer"""
    email: Any
    """Primary email address of the customer"""
    phone: Any
    """Primary phone number of the customer"""
    first_name: Any
    """First name of the customer"""
    last_name: Any
    """Last name of the customer"""
    state: Any
    """Account state (`disabled`, `invited`, `enabled`, `declined`)"""
    orders_count: Any
    """Number of orders placed by the customer"""
    total_spent: Any
    """Total lifetime amount spent by the customer"""
    currency: Any
    """ISO 4217 currency code for the customer's total spend"""
    created_at: Any
    """ISO 8601 timestamp when the customer record was created"""
    updated_at: Any
    """ISO 8601 timestamp when the customer record was last updated"""


class CustomersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the customer"""
    email: str
    """Primary email address of the customer"""
    phone: str
    """Primary phone number of the customer"""
    first_name: str
    """First name of the customer"""
    last_name: str
    """Last name of the customer"""
    state: str
    """Account state (`disabled`, `invited`, `enabled`, `declined`)"""
    orders_count: str
    """Number of orders placed by the customer"""
    total_spent: str
    """Total lifetime amount spent by the customer"""
    currency: str
    """ISO 4217 currency code for the customer's total spend"""
    created_at: str
    """ISO 8601 timestamp when the customer record was created"""
    updated_at: str
    """ISO 8601 timestamp when the customer record was last updated"""


class CustomersSortFilter(TypedDict, total=False):
    """Available fields for sorting customers search results."""
    id: AirbyteSortOrder
    """Unique identifier for the customer"""
    email: AirbyteSortOrder
    """Primary email address of the customer"""
    phone: AirbyteSortOrder
    """Primary phone number of the customer"""
    first_name: AirbyteSortOrder
    """First name of the customer"""
    last_name: AirbyteSortOrder
    """Last name of the customer"""
    state: AirbyteSortOrder
    """Account state (`disabled`, `invited`, `enabled`, `declined`)"""
    orders_count: AirbyteSortOrder
    """Number of orders placed by the customer"""
    total_spent: AirbyteSortOrder
    """Total lifetime amount spent by the customer"""
    currency: AirbyteSortOrder
    """ISO 4217 currency code for the customer's total spend"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the customer record was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the customer record was last updated"""


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


# ===== DISCOUNT_CODES SEARCH TYPES =====

class DiscountCodesSearchFilter(TypedDict, total=False):
    """Available fields for filtering discount_codes search queries."""
    id: int | None
    """Unique identifier for the discount code"""
    price_rule_id: int | None
    """Identifier of the parent price rule"""
    code: str | None
    """Discount code string shoppers enter at checkout"""
    usage_count: int | None
    """Number of times the code has been redeemed"""
    created_at: str | None
    """ISO 8601 timestamp when the code was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the code was last updated"""


class DiscountCodesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the discount code"""
    price_rule_id: list[int]
    """Identifier of the parent price rule"""
    code: list[str]
    """Discount code string shoppers enter at checkout"""
    usage_count: list[int]
    """Number of times the code has been redeemed"""
    created_at: list[str]
    """ISO 8601 timestamp when the code was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the code was last updated"""


class DiscountCodesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the discount code"""
    price_rule_id: Any
    """Identifier of the parent price rule"""
    code: Any
    """Discount code string shoppers enter at checkout"""
    usage_count: Any
    """Number of times the code has been redeemed"""
    created_at: Any
    """ISO 8601 timestamp when the code was created"""
    updated_at: Any
    """ISO 8601 timestamp when the code was last updated"""


class DiscountCodesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the discount code"""
    price_rule_id: str
    """Identifier of the parent price rule"""
    code: str
    """Discount code string shoppers enter at checkout"""
    usage_count: str
    """Number of times the code has been redeemed"""
    created_at: str
    """ISO 8601 timestamp when the code was created"""
    updated_at: str
    """ISO 8601 timestamp when the code was last updated"""


class DiscountCodesSortFilter(TypedDict, total=False):
    """Available fields for sorting discount_codes search results."""
    id: AirbyteSortOrder
    """Unique identifier for the discount code"""
    price_rule_id: AirbyteSortOrder
    """Identifier of the parent price rule"""
    code: AirbyteSortOrder
    """Discount code string shoppers enter at checkout"""
    usage_count: AirbyteSortOrder
    """Number of times the code has been redeemed"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the code was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the code was last updated"""


# Entity-specific condition types for discount_codes
class DiscountCodesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DiscountCodesSearchFilter


class DiscountCodesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DiscountCodesSearchFilter


class DiscountCodesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DiscountCodesSearchFilter


class DiscountCodesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DiscountCodesSearchFilter


class DiscountCodesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DiscountCodesSearchFilter


class DiscountCodesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DiscountCodesSearchFilter


class DiscountCodesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DiscountCodesStringFilter


class DiscountCodesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DiscountCodesStringFilter


class DiscountCodesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DiscountCodesStringFilter


class DiscountCodesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DiscountCodesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DiscountCodesInCondition = TypedDict("DiscountCodesInCondition", {"in": DiscountCodesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DiscountCodesNotCondition = TypedDict("DiscountCodesNotCondition", {"not": "DiscountCodesCondition"}, total=False)
"""Negates the nested condition."""

DiscountCodesAndCondition = TypedDict("DiscountCodesAndCondition", {"and": "list[DiscountCodesCondition]"}, total=False)
"""True if all nested conditions are true."""

DiscountCodesOrCondition = TypedDict("DiscountCodesOrCondition", {"or": "list[DiscountCodesCondition]"}, total=False)
"""True if any nested condition is true."""

DiscountCodesAnyCondition = TypedDict("DiscountCodesAnyCondition", {"any": DiscountCodesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all discount_codes condition types
DiscountCodesCondition = (
    DiscountCodesEqCondition
    | DiscountCodesNeqCondition
    | DiscountCodesGtCondition
    | DiscountCodesGteCondition
    | DiscountCodesLtCondition
    | DiscountCodesLteCondition
    | DiscountCodesInCondition
    | DiscountCodesLikeCondition
    | DiscountCodesFuzzyCondition
    | DiscountCodesKeywordCondition
    | DiscountCodesContainsCondition
    | DiscountCodesNotCondition
    | DiscountCodesAndCondition
    | DiscountCodesOrCondition
    | DiscountCodesAnyCondition
)


class DiscountCodesSearchQuery(TypedDict, total=False):
    """Search query for discount_codes entity."""
    filter: DiscountCodesCondition
    sort: list[DiscountCodesSortFilter]


# ===== DRAFT_ORDERS SEARCH TYPES =====

class DraftOrdersSearchFilter(TypedDict, total=False):
    """Available fields for filtering draft_orders search queries."""
    id: int | None
    """Unique identifier for the draft order"""
    name: str | None
    """Shopify-assigned display name for the draft order (e.g. `#D12345`)"""
    email: str | None
    """Email address associated with the draft order"""
    status: str | None
    """Status of the draft order (`open`, `invoice_sent`, `completed`)"""
    currency: str | None
    """ISO 4217 currency code for the draft order totals"""
    total_price: str | None
    """Total price of the draft order"""
    order_id: int | None
    """Identifier of the completed order, if the draft has been completed"""
    created_at: str | None
    """ISO 8601 timestamp when the draft order was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the draft order was last updated"""
    completed_at: str | None
    """ISO 8601 timestamp when the draft order was completed, if applicable"""


class DraftOrdersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the draft order"""
    name: list[str]
    """Shopify-assigned display name for the draft order (e.g. `#D12345`)"""
    email: list[str]
    """Email address associated with the draft order"""
    status: list[str]
    """Status of the draft order (`open`, `invoice_sent`, `completed`)"""
    currency: list[str]
    """ISO 4217 currency code for the draft order totals"""
    total_price: list[str]
    """Total price of the draft order"""
    order_id: list[int]
    """Identifier of the completed order, if the draft has been completed"""
    created_at: list[str]
    """ISO 8601 timestamp when the draft order was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the draft order was last updated"""
    completed_at: list[str]
    """ISO 8601 timestamp when the draft order was completed, if applicable"""


class DraftOrdersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the draft order"""
    name: Any
    """Shopify-assigned display name for the draft order (e.g. `#D12345`)"""
    email: Any
    """Email address associated with the draft order"""
    status: Any
    """Status of the draft order (`open`, `invoice_sent`, `completed`)"""
    currency: Any
    """ISO 4217 currency code for the draft order totals"""
    total_price: Any
    """Total price of the draft order"""
    order_id: Any
    """Identifier of the completed order, if the draft has been completed"""
    created_at: Any
    """ISO 8601 timestamp when the draft order was created"""
    updated_at: Any
    """ISO 8601 timestamp when the draft order was last updated"""
    completed_at: Any
    """ISO 8601 timestamp when the draft order was completed, if applicable"""


class DraftOrdersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the draft order"""
    name: str
    """Shopify-assigned display name for the draft order (e.g. `#D12345`)"""
    email: str
    """Email address associated with the draft order"""
    status: str
    """Status of the draft order (`open`, `invoice_sent`, `completed`)"""
    currency: str
    """ISO 4217 currency code for the draft order totals"""
    total_price: str
    """Total price of the draft order"""
    order_id: str
    """Identifier of the completed order, if the draft has been completed"""
    created_at: str
    """ISO 8601 timestamp when the draft order was created"""
    updated_at: str
    """ISO 8601 timestamp when the draft order was last updated"""
    completed_at: str
    """ISO 8601 timestamp when the draft order was completed, if applicable"""


class DraftOrdersSortFilter(TypedDict, total=False):
    """Available fields for sorting draft_orders search results."""
    id: AirbyteSortOrder
    """Unique identifier for the draft order"""
    name: AirbyteSortOrder
    """Shopify-assigned display name for the draft order (e.g. `#D12345`)"""
    email: AirbyteSortOrder
    """Email address associated with the draft order"""
    status: AirbyteSortOrder
    """Status of the draft order (`open`, `invoice_sent`, `completed`)"""
    currency: AirbyteSortOrder
    """ISO 4217 currency code for the draft order totals"""
    total_price: AirbyteSortOrder
    """Total price of the draft order"""
    order_id: AirbyteSortOrder
    """Identifier of the completed order, if the draft has been completed"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the draft order was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the draft order was last updated"""
    completed_at: AirbyteSortOrder
    """ISO 8601 timestamp when the draft order was completed, if applicable"""


# Entity-specific condition types for draft_orders
class DraftOrdersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DraftOrdersSearchFilter


class DraftOrdersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DraftOrdersSearchFilter


class DraftOrdersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DraftOrdersSearchFilter


class DraftOrdersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DraftOrdersSearchFilter


class DraftOrdersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DraftOrdersSearchFilter


class DraftOrdersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DraftOrdersSearchFilter


class DraftOrdersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DraftOrdersStringFilter


class DraftOrdersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DraftOrdersStringFilter


class DraftOrdersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DraftOrdersStringFilter


class DraftOrdersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DraftOrdersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DraftOrdersInCondition = TypedDict("DraftOrdersInCondition", {"in": DraftOrdersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DraftOrdersNotCondition = TypedDict("DraftOrdersNotCondition", {"not": "DraftOrdersCondition"}, total=False)
"""Negates the nested condition."""

DraftOrdersAndCondition = TypedDict("DraftOrdersAndCondition", {"and": "list[DraftOrdersCondition]"}, total=False)
"""True if all nested conditions are true."""

DraftOrdersOrCondition = TypedDict("DraftOrdersOrCondition", {"or": "list[DraftOrdersCondition]"}, total=False)
"""True if any nested condition is true."""

DraftOrdersAnyCondition = TypedDict("DraftOrdersAnyCondition", {"any": DraftOrdersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all draft_orders condition types
DraftOrdersCondition = (
    DraftOrdersEqCondition
    | DraftOrdersNeqCondition
    | DraftOrdersGtCondition
    | DraftOrdersGteCondition
    | DraftOrdersLtCondition
    | DraftOrdersLteCondition
    | DraftOrdersInCondition
    | DraftOrdersLikeCondition
    | DraftOrdersFuzzyCondition
    | DraftOrdersKeywordCondition
    | DraftOrdersContainsCondition
    | DraftOrdersNotCondition
    | DraftOrdersAndCondition
    | DraftOrdersOrCondition
    | DraftOrdersAnyCondition
)


class DraftOrdersSearchQuery(TypedDict, total=False):
    """Search query for draft_orders entity."""
    filter: DraftOrdersCondition
    sort: list[DraftOrdersSortFilter]


# ===== FULFILLMENT_ORDERS SEARCH TYPES =====

class FulfillmentOrdersSearchFilter(TypedDict, total=False):
    """Available fields for filtering fulfillment_orders search queries."""
    id: int | None
    """Unique identifier for the fulfillment order"""
    order_id: int | None
    """Identifier of the parent order"""
    shop_id: int | None
    """Identifier of the shop that owns the fulfillment order"""
    assigned_location_id: int | None
    """Identifier of the location assigned to fulfill the order"""
    status: str | None
    """Fulfillment order status (e.g. `open`, `in_progress`, `closed`)"""
    request_status: str | None
    """Status of the fulfillment request (e.g. `unsubmitted`, `submitted`)"""
    created_at: str | None
    """ISO 8601 timestamp when the fulfillment order was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the fulfillment order was last updated"""


class FulfillmentOrdersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the fulfillment order"""
    order_id: list[int]
    """Identifier of the parent order"""
    shop_id: list[int]
    """Identifier of the shop that owns the fulfillment order"""
    assigned_location_id: list[int]
    """Identifier of the location assigned to fulfill the order"""
    status: list[str]
    """Fulfillment order status (e.g. `open`, `in_progress`, `closed`)"""
    request_status: list[str]
    """Status of the fulfillment request (e.g. `unsubmitted`, `submitted`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the fulfillment order was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the fulfillment order was last updated"""


class FulfillmentOrdersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the fulfillment order"""
    order_id: Any
    """Identifier of the parent order"""
    shop_id: Any
    """Identifier of the shop that owns the fulfillment order"""
    assigned_location_id: Any
    """Identifier of the location assigned to fulfill the order"""
    status: Any
    """Fulfillment order status (e.g. `open`, `in_progress`, `closed`)"""
    request_status: Any
    """Status of the fulfillment request (e.g. `unsubmitted`, `submitted`)"""
    created_at: Any
    """ISO 8601 timestamp when the fulfillment order was created"""
    updated_at: Any
    """ISO 8601 timestamp when the fulfillment order was last updated"""


class FulfillmentOrdersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the fulfillment order"""
    order_id: str
    """Identifier of the parent order"""
    shop_id: str
    """Identifier of the shop that owns the fulfillment order"""
    assigned_location_id: str
    """Identifier of the location assigned to fulfill the order"""
    status: str
    """Fulfillment order status (e.g. `open`, `in_progress`, `closed`)"""
    request_status: str
    """Status of the fulfillment request (e.g. `unsubmitted`, `submitted`)"""
    created_at: str
    """ISO 8601 timestamp when the fulfillment order was created"""
    updated_at: str
    """ISO 8601 timestamp when the fulfillment order was last updated"""


class FulfillmentOrdersSortFilter(TypedDict, total=False):
    """Available fields for sorting fulfillment_orders search results."""
    id: AirbyteSortOrder
    """Unique identifier for the fulfillment order"""
    order_id: AirbyteSortOrder
    """Identifier of the parent order"""
    shop_id: AirbyteSortOrder
    """Identifier of the shop that owns the fulfillment order"""
    assigned_location_id: AirbyteSortOrder
    """Identifier of the location assigned to fulfill the order"""
    status: AirbyteSortOrder
    """Fulfillment order status (e.g. `open`, `in_progress`, `closed`)"""
    request_status: AirbyteSortOrder
    """Status of the fulfillment request (e.g. `unsubmitted`, `submitted`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the fulfillment order was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the fulfillment order was last updated"""


# Entity-specific condition types for fulfillment_orders
class FulfillmentOrdersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: FulfillmentOrdersSearchFilter


class FulfillmentOrdersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: FulfillmentOrdersSearchFilter


class FulfillmentOrdersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: FulfillmentOrdersSearchFilter


class FulfillmentOrdersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: FulfillmentOrdersSearchFilter


class FulfillmentOrdersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: FulfillmentOrdersSearchFilter


class FulfillmentOrdersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: FulfillmentOrdersSearchFilter


class FulfillmentOrdersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: FulfillmentOrdersStringFilter


class FulfillmentOrdersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: FulfillmentOrdersStringFilter


class FulfillmentOrdersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: FulfillmentOrdersStringFilter


class FulfillmentOrdersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: FulfillmentOrdersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
FulfillmentOrdersInCondition = TypedDict("FulfillmentOrdersInCondition", {"in": FulfillmentOrdersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

FulfillmentOrdersNotCondition = TypedDict("FulfillmentOrdersNotCondition", {"not": "FulfillmentOrdersCondition"}, total=False)
"""Negates the nested condition."""

FulfillmentOrdersAndCondition = TypedDict("FulfillmentOrdersAndCondition", {"and": "list[FulfillmentOrdersCondition]"}, total=False)
"""True if all nested conditions are true."""

FulfillmentOrdersOrCondition = TypedDict("FulfillmentOrdersOrCondition", {"or": "list[FulfillmentOrdersCondition]"}, total=False)
"""True if any nested condition is true."""

FulfillmentOrdersAnyCondition = TypedDict("FulfillmentOrdersAnyCondition", {"any": FulfillmentOrdersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all fulfillment_orders condition types
FulfillmentOrdersCondition = (
    FulfillmentOrdersEqCondition
    | FulfillmentOrdersNeqCondition
    | FulfillmentOrdersGtCondition
    | FulfillmentOrdersGteCondition
    | FulfillmentOrdersLtCondition
    | FulfillmentOrdersLteCondition
    | FulfillmentOrdersInCondition
    | FulfillmentOrdersLikeCondition
    | FulfillmentOrdersFuzzyCondition
    | FulfillmentOrdersKeywordCondition
    | FulfillmentOrdersContainsCondition
    | FulfillmentOrdersNotCondition
    | FulfillmentOrdersAndCondition
    | FulfillmentOrdersOrCondition
    | FulfillmentOrdersAnyCondition
)


class FulfillmentOrdersSearchQuery(TypedDict, total=False):
    """Search query for fulfillment_orders entity."""
    filter: FulfillmentOrdersCondition
    sort: list[FulfillmentOrdersSortFilter]


# ===== FULFILLMENTS SEARCH TYPES =====

class FulfillmentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering fulfillments search queries."""
    id: int | None
    """Unique identifier for the fulfillment"""
    order_id: int | None
    """Identifier of the parent order"""
    status: str | None
    """Fulfillment status (e.g. `pending`, `open`, `success`, `cancelled`)"""
    shipment_status: str | None
    """Carrier shipment status (e.g. `delivered`, `in_transit`)"""
    tracking_company: str | None
    """Name of the shipping carrier"""
    tracking_number: str | None
    """Primary tracking number for the shipment"""
    location_id: int | None
    """Identifier of the fulfilling location"""
    created_at: str | None
    """ISO 8601 timestamp when the fulfillment was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the fulfillment was last updated"""


class FulfillmentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the fulfillment"""
    order_id: list[int]
    """Identifier of the parent order"""
    status: list[str]
    """Fulfillment status (e.g. `pending`, `open`, `success`, `cancelled`)"""
    shipment_status: list[str]
    """Carrier shipment status (e.g. `delivered`, `in_transit`)"""
    tracking_company: list[str]
    """Name of the shipping carrier"""
    tracking_number: list[str]
    """Primary tracking number for the shipment"""
    location_id: list[int]
    """Identifier of the fulfilling location"""
    created_at: list[str]
    """ISO 8601 timestamp when the fulfillment was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the fulfillment was last updated"""


class FulfillmentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the fulfillment"""
    order_id: Any
    """Identifier of the parent order"""
    status: Any
    """Fulfillment status (e.g. `pending`, `open`, `success`, `cancelled`)"""
    shipment_status: Any
    """Carrier shipment status (e.g. `delivered`, `in_transit`)"""
    tracking_company: Any
    """Name of the shipping carrier"""
    tracking_number: Any
    """Primary tracking number for the shipment"""
    location_id: Any
    """Identifier of the fulfilling location"""
    created_at: Any
    """ISO 8601 timestamp when the fulfillment was created"""
    updated_at: Any
    """ISO 8601 timestamp when the fulfillment was last updated"""


class FulfillmentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the fulfillment"""
    order_id: str
    """Identifier of the parent order"""
    status: str
    """Fulfillment status (e.g. `pending`, `open`, `success`, `cancelled`)"""
    shipment_status: str
    """Carrier shipment status (e.g. `delivered`, `in_transit`)"""
    tracking_company: str
    """Name of the shipping carrier"""
    tracking_number: str
    """Primary tracking number for the shipment"""
    location_id: str
    """Identifier of the fulfilling location"""
    created_at: str
    """ISO 8601 timestamp when the fulfillment was created"""
    updated_at: str
    """ISO 8601 timestamp when the fulfillment was last updated"""


class FulfillmentsSortFilter(TypedDict, total=False):
    """Available fields for sorting fulfillments search results."""
    id: AirbyteSortOrder
    """Unique identifier for the fulfillment"""
    order_id: AirbyteSortOrder
    """Identifier of the parent order"""
    status: AirbyteSortOrder
    """Fulfillment status (e.g. `pending`, `open`, `success`, `cancelled`)"""
    shipment_status: AirbyteSortOrder
    """Carrier shipment status (e.g. `delivered`, `in_transit`)"""
    tracking_company: AirbyteSortOrder
    """Name of the shipping carrier"""
    tracking_number: AirbyteSortOrder
    """Primary tracking number for the shipment"""
    location_id: AirbyteSortOrder
    """Identifier of the fulfilling location"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the fulfillment was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the fulfillment was last updated"""


# Entity-specific condition types for fulfillments
class FulfillmentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: FulfillmentsSearchFilter


class FulfillmentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: FulfillmentsSearchFilter


class FulfillmentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: FulfillmentsSearchFilter


class FulfillmentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: FulfillmentsSearchFilter


class FulfillmentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: FulfillmentsSearchFilter


class FulfillmentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: FulfillmentsSearchFilter


class FulfillmentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: FulfillmentsStringFilter


class FulfillmentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: FulfillmentsStringFilter


class FulfillmentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: FulfillmentsStringFilter


class FulfillmentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: FulfillmentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
FulfillmentsInCondition = TypedDict("FulfillmentsInCondition", {"in": FulfillmentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

FulfillmentsNotCondition = TypedDict("FulfillmentsNotCondition", {"not": "FulfillmentsCondition"}, total=False)
"""Negates the nested condition."""

FulfillmentsAndCondition = TypedDict("FulfillmentsAndCondition", {"and": "list[FulfillmentsCondition]"}, total=False)
"""True if all nested conditions are true."""

FulfillmentsOrCondition = TypedDict("FulfillmentsOrCondition", {"or": "list[FulfillmentsCondition]"}, total=False)
"""True if any nested condition is true."""

FulfillmentsAnyCondition = TypedDict("FulfillmentsAnyCondition", {"any": FulfillmentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all fulfillments condition types
FulfillmentsCondition = (
    FulfillmentsEqCondition
    | FulfillmentsNeqCondition
    | FulfillmentsGtCondition
    | FulfillmentsGteCondition
    | FulfillmentsLtCondition
    | FulfillmentsLteCondition
    | FulfillmentsInCondition
    | FulfillmentsLikeCondition
    | FulfillmentsFuzzyCondition
    | FulfillmentsKeywordCondition
    | FulfillmentsContainsCondition
    | FulfillmentsNotCondition
    | FulfillmentsAndCondition
    | FulfillmentsOrCondition
    | FulfillmentsAnyCondition
)


class FulfillmentsSearchQuery(TypedDict, total=False):
    """Search query for fulfillments entity."""
    filter: FulfillmentsCondition
    sort: list[FulfillmentsSortFilter]


# ===== INVENTORY_ITEMS SEARCH TYPES =====

class InventoryItemsSearchFilter(TypedDict, total=False):
    """Available fields for filtering inventory_items search queries."""
    id: int | None
    """Unique identifier for the inventory item"""
    sku: str | None
    """Stock keeping unit associated with the inventory item"""
    tracked: bool | None
    """Whether Shopify is tracking inventory for this item"""
    requires_shipping: bool | None
    """Whether the item requires shipping"""
    country_code_of_origin: str | None
    """ISO country code of the item's country of origin"""
    created_at: str | None
    """ISO 8601 timestamp when the inventory item was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the inventory item was last updated"""


class InventoryItemsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the inventory item"""
    sku: list[str]
    """Stock keeping unit associated with the inventory item"""
    tracked: list[bool]
    """Whether Shopify is tracking inventory for this item"""
    requires_shipping: list[bool]
    """Whether the item requires shipping"""
    country_code_of_origin: list[str]
    """ISO country code of the item's country of origin"""
    created_at: list[str]
    """ISO 8601 timestamp when the inventory item was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the inventory item was last updated"""


class InventoryItemsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the inventory item"""
    sku: Any
    """Stock keeping unit associated with the inventory item"""
    tracked: Any
    """Whether Shopify is tracking inventory for this item"""
    requires_shipping: Any
    """Whether the item requires shipping"""
    country_code_of_origin: Any
    """ISO country code of the item's country of origin"""
    created_at: Any
    """ISO 8601 timestamp when the inventory item was created"""
    updated_at: Any
    """ISO 8601 timestamp when the inventory item was last updated"""


class InventoryItemsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the inventory item"""
    sku: str
    """Stock keeping unit associated with the inventory item"""
    tracked: str
    """Whether Shopify is tracking inventory for this item"""
    requires_shipping: str
    """Whether the item requires shipping"""
    country_code_of_origin: str
    """ISO country code of the item's country of origin"""
    created_at: str
    """ISO 8601 timestamp when the inventory item was created"""
    updated_at: str
    """ISO 8601 timestamp when the inventory item was last updated"""


class InventoryItemsSortFilter(TypedDict, total=False):
    """Available fields for sorting inventory_items search results."""
    id: AirbyteSortOrder
    """Unique identifier for the inventory item"""
    sku: AirbyteSortOrder
    """Stock keeping unit associated with the inventory item"""
    tracked: AirbyteSortOrder
    """Whether Shopify is tracking inventory for this item"""
    requires_shipping: AirbyteSortOrder
    """Whether the item requires shipping"""
    country_code_of_origin: AirbyteSortOrder
    """ISO country code of the item's country of origin"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the inventory item was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the inventory item was last updated"""


# Entity-specific condition types for inventory_items
class InventoryItemsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: InventoryItemsSearchFilter


class InventoryItemsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: InventoryItemsSearchFilter


class InventoryItemsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: InventoryItemsSearchFilter


class InventoryItemsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: InventoryItemsSearchFilter


class InventoryItemsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: InventoryItemsSearchFilter


class InventoryItemsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: InventoryItemsSearchFilter


class InventoryItemsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: InventoryItemsStringFilter


class InventoryItemsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: InventoryItemsStringFilter


class InventoryItemsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: InventoryItemsStringFilter


class InventoryItemsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: InventoryItemsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
InventoryItemsInCondition = TypedDict("InventoryItemsInCondition", {"in": InventoryItemsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

InventoryItemsNotCondition = TypedDict("InventoryItemsNotCondition", {"not": "InventoryItemsCondition"}, total=False)
"""Negates the nested condition."""

InventoryItemsAndCondition = TypedDict("InventoryItemsAndCondition", {"and": "list[InventoryItemsCondition]"}, total=False)
"""True if all nested conditions are true."""

InventoryItemsOrCondition = TypedDict("InventoryItemsOrCondition", {"or": "list[InventoryItemsCondition]"}, total=False)
"""True if any nested condition is true."""

InventoryItemsAnyCondition = TypedDict("InventoryItemsAnyCondition", {"any": InventoryItemsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all inventory_items condition types
InventoryItemsCondition = (
    InventoryItemsEqCondition
    | InventoryItemsNeqCondition
    | InventoryItemsGtCondition
    | InventoryItemsGteCondition
    | InventoryItemsLtCondition
    | InventoryItemsLteCondition
    | InventoryItemsInCondition
    | InventoryItemsLikeCondition
    | InventoryItemsFuzzyCondition
    | InventoryItemsKeywordCondition
    | InventoryItemsContainsCondition
    | InventoryItemsNotCondition
    | InventoryItemsAndCondition
    | InventoryItemsOrCondition
    | InventoryItemsAnyCondition
)


class InventoryItemsSearchQuery(TypedDict, total=False):
    """Search query for inventory_items entity."""
    filter: InventoryItemsCondition
    sort: list[InventoryItemsSortFilter]


# ===== INVENTORY_LEVELS SEARCH TYPES =====

class InventoryLevelsSearchFilter(TypedDict, total=False):
    """Available fields for filtering inventory_levels search queries."""
    inventory_item_id: int | None
    """Identifier of the inventory item"""
    location_id: int | None
    """Identifier of the location holding the inventory"""
    available: int | None
    """Number of units available at the location"""
    updated_at: str | None
    """ISO 8601 timestamp when the inventory level was last updated"""


class InventoryLevelsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    inventory_item_id: list[int]
    """Identifier of the inventory item"""
    location_id: list[int]
    """Identifier of the location holding the inventory"""
    available: list[int]
    """Number of units available at the location"""
    updated_at: list[str]
    """ISO 8601 timestamp when the inventory level was last updated"""


class InventoryLevelsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    inventory_item_id: Any
    """Identifier of the inventory item"""
    location_id: Any
    """Identifier of the location holding the inventory"""
    available: Any
    """Number of units available at the location"""
    updated_at: Any
    """ISO 8601 timestamp when the inventory level was last updated"""


class InventoryLevelsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    inventory_item_id: str
    """Identifier of the inventory item"""
    location_id: str
    """Identifier of the location holding the inventory"""
    available: str
    """Number of units available at the location"""
    updated_at: str
    """ISO 8601 timestamp when the inventory level was last updated"""


class InventoryLevelsSortFilter(TypedDict, total=False):
    """Available fields for sorting inventory_levels search results."""
    inventory_item_id: AirbyteSortOrder
    """Identifier of the inventory item"""
    location_id: AirbyteSortOrder
    """Identifier of the location holding the inventory"""
    available: AirbyteSortOrder
    """Number of units available at the location"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the inventory level was last updated"""


# Entity-specific condition types for inventory_levels
class InventoryLevelsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: InventoryLevelsSearchFilter


class InventoryLevelsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: InventoryLevelsSearchFilter


class InventoryLevelsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: InventoryLevelsSearchFilter


class InventoryLevelsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: InventoryLevelsSearchFilter


class InventoryLevelsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: InventoryLevelsSearchFilter


class InventoryLevelsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: InventoryLevelsSearchFilter


class InventoryLevelsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: InventoryLevelsStringFilter


class InventoryLevelsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: InventoryLevelsStringFilter


class InventoryLevelsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: InventoryLevelsStringFilter


class InventoryLevelsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: InventoryLevelsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
InventoryLevelsInCondition = TypedDict("InventoryLevelsInCondition", {"in": InventoryLevelsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

InventoryLevelsNotCondition = TypedDict("InventoryLevelsNotCondition", {"not": "InventoryLevelsCondition"}, total=False)
"""Negates the nested condition."""

InventoryLevelsAndCondition = TypedDict("InventoryLevelsAndCondition", {"and": "list[InventoryLevelsCondition]"}, total=False)
"""True if all nested conditions are true."""

InventoryLevelsOrCondition = TypedDict("InventoryLevelsOrCondition", {"or": "list[InventoryLevelsCondition]"}, total=False)
"""True if any nested condition is true."""

InventoryLevelsAnyCondition = TypedDict("InventoryLevelsAnyCondition", {"any": InventoryLevelsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all inventory_levels condition types
InventoryLevelsCondition = (
    InventoryLevelsEqCondition
    | InventoryLevelsNeqCondition
    | InventoryLevelsGtCondition
    | InventoryLevelsGteCondition
    | InventoryLevelsLtCondition
    | InventoryLevelsLteCondition
    | InventoryLevelsInCondition
    | InventoryLevelsLikeCondition
    | InventoryLevelsFuzzyCondition
    | InventoryLevelsKeywordCondition
    | InventoryLevelsContainsCondition
    | InventoryLevelsNotCondition
    | InventoryLevelsAndCondition
    | InventoryLevelsOrCondition
    | InventoryLevelsAnyCondition
)


class InventoryLevelsSearchQuery(TypedDict, total=False):
    """Search query for inventory_levels entity."""
    filter: InventoryLevelsCondition
    sort: list[InventoryLevelsSortFilter]


# ===== LOCATIONS SEARCH TYPES =====

class LocationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering locations search queries."""
    id: int | None
    """Unique identifier for the location"""
    name: str | None
    """Display name of the location"""
    address1: str | None
    """Primary street address of the location"""
    city: str | None
    """City of the location"""
    province: str | None
    """Province, state, or region of the location"""
    country: str | None
    """Country name of the location"""
    country_code: str | None
    """ISO 3166-1 alpha-2 country code of the location"""
    phone: str | None
    """Phone number for the location"""
    active: bool | None
    """Whether the location is currently active"""
    created_at: str | None
    """ISO 8601 timestamp when the location was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the location was last updated"""


class LocationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the location"""
    name: list[str]
    """Display name of the location"""
    address1: list[str]
    """Primary street address of the location"""
    city: list[str]
    """City of the location"""
    province: list[str]
    """Province, state, or region of the location"""
    country: list[str]
    """Country name of the location"""
    country_code: list[str]
    """ISO 3166-1 alpha-2 country code of the location"""
    phone: list[str]
    """Phone number for the location"""
    active: list[bool]
    """Whether the location is currently active"""
    created_at: list[str]
    """ISO 8601 timestamp when the location was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the location was last updated"""


class LocationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the location"""
    name: Any
    """Display name of the location"""
    address1: Any
    """Primary street address of the location"""
    city: Any
    """City of the location"""
    province: Any
    """Province, state, or region of the location"""
    country: Any
    """Country name of the location"""
    country_code: Any
    """ISO 3166-1 alpha-2 country code of the location"""
    phone: Any
    """Phone number for the location"""
    active: Any
    """Whether the location is currently active"""
    created_at: Any
    """ISO 8601 timestamp when the location was created"""
    updated_at: Any
    """ISO 8601 timestamp when the location was last updated"""


class LocationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the location"""
    name: str
    """Display name of the location"""
    address1: str
    """Primary street address of the location"""
    city: str
    """City of the location"""
    province: str
    """Province, state, or region of the location"""
    country: str
    """Country name of the location"""
    country_code: str
    """ISO 3166-1 alpha-2 country code of the location"""
    phone: str
    """Phone number for the location"""
    active: str
    """Whether the location is currently active"""
    created_at: str
    """ISO 8601 timestamp when the location was created"""
    updated_at: str
    """ISO 8601 timestamp when the location was last updated"""


class LocationsSortFilter(TypedDict, total=False):
    """Available fields for sorting locations search results."""
    id: AirbyteSortOrder
    """Unique identifier for the location"""
    name: AirbyteSortOrder
    """Display name of the location"""
    address1: AirbyteSortOrder
    """Primary street address of the location"""
    city: AirbyteSortOrder
    """City of the location"""
    province: AirbyteSortOrder
    """Province, state, or region of the location"""
    country: AirbyteSortOrder
    """Country name of the location"""
    country_code: AirbyteSortOrder
    """ISO 3166-1 alpha-2 country code of the location"""
    phone: AirbyteSortOrder
    """Phone number for the location"""
    active: AirbyteSortOrder
    """Whether the location is currently active"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the location was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the location was last updated"""


# Entity-specific condition types for locations
class LocationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: LocationsSearchFilter


class LocationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: LocationsSearchFilter


class LocationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: LocationsSearchFilter


class LocationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: LocationsSearchFilter


class LocationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: LocationsSearchFilter


class LocationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: LocationsSearchFilter


class LocationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: LocationsStringFilter


class LocationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: LocationsStringFilter


class LocationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: LocationsStringFilter


class LocationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: LocationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
LocationsInCondition = TypedDict("LocationsInCondition", {"in": LocationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

LocationsNotCondition = TypedDict("LocationsNotCondition", {"not": "LocationsCondition"}, total=False)
"""Negates the nested condition."""

LocationsAndCondition = TypedDict("LocationsAndCondition", {"and": "list[LocationsCondition]"}, total=False)
"""True if all nested conditions are true."""

LocationsOrCondition = TypedDict("LocationsOrCondition", {"or": "list[LocationsCondition]"}, total=False)
"""True if any nested condition is true."""

LocationsAnyCondition = TypedDict("LocationsAnyCondition", {"any": LocationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all locations condition types
LocationsCondition = (
    LocationsEqCondition
    | LocationsNeqCondition
    | LocationsGtCondition
    | LocationsGteCondition
    | LocationsLtCondition
    | LocationsLteCondition
    | LocationsInCondition
    | LocationsLikeCondition
    | LocationsFuzzyCondition
    | LocationsKeywordCondition
    | LocationsContainsCondition
    | LocationsNotCondition
    | LocationsAndCondition
    | LocationsOrCondition
    | LocationsAnyCondition
)


class LocationsSearchQuery(TypedDict, total=False):
    """Search query for locations entity."""
    filter: LocationsCondition
    sort: list[LocationsSortFilter]


# ===== METAFIELD_CUSTOMERS SEARCH TYPES =====

class MetafieldCustomersSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_customers search queries."""
    id: int | None
    """Unique identifier for the metafield"""
    namespace: str | None
    """Namespace group for the metafield"""
    key: str | None
    """Key of the metafield within its namespace"""
    value: str | None
    """Serialized value stored in the metafield"""
    type_: str | None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None
    """Human-readable description of the metafield"""
    owner_id: int | None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldCustomersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the metafield"""
    namespace: list[str]
    """Namespace group for the metafield"""
    key: list[str]
    """Key of the metafield within its namespace"""
    value: list[str]
    """Serialized value stored in the metafield"""
    type_: list[str]
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: list[str]
    """Human-readable description of the metafield"""
    owner_id: list[int]
    """Identifier of the resource that owns this metafield"""
    owner_resource: list[str]
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldCustomersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the metafield"""
    namespace: Any
    """Namespace group for the metafield"""
    key: Any
    """Key of the metafield within its namespace"""
    value: Any
    """Serialized value stored in the metafield"""
    type_: Any
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: Any
    """Human-readable description of the metafield"""
    owner_id: Any
    """Identifier of the resource that owns this metafield"""
    owner_resource: Any
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: Any
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: Any
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldCustomersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the metafield"""
    namespace: str
    """Namespace group for the metafield"""
    key: str
    """Key of the metafield within its namespace"""
    value: str
    """Serialized value stored in the metafield"""
    type_: str
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str
    """Human-readable description of the metafield"""
    owner_id: str
    """Identifier of the resource that owns this metafield"""
    owner_resource: str
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldCustomersSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_customers search results."""
    id: AirbyteSortOrder
    """Unique identifier for the metafield"""
    namespace: AirbyteSortOrder
    """Namespace group for the metafield"""
    key: AirbyteSortOrder
    """Key of the metafield within its namespace"""
    value: AirbyteSortOrder
    """Serialized value stored in the metafield"""
    type_: AirbyteSortOrder
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: AirbyteSortOrder
    """Human-readable description of the metafield"""
    owner_id: AirbyteSortOrder
    """Identifier of the resource that owns this metafield"""
    owner_resource: AirbyteSortOrder
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was last updated"""


# Entity-specific condition types for metafield_customers
class MetafieldCustomersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldCustomersSearchFilter


class MetafieldCustomersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldCustomersSearchFilter


class MetafieldCustomersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldCustomersSearchFilter


class MetafieldCustomersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldCustomersSearchFilter


class MetafieldCustomersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldCustomersSearchFilter


class MetafieldCustomersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldCustomersSearchFilter


class MetafieldCustomersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldCustomersStringFilter


class MetafieldCustomersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldCustomersStringFilter


class MetafieldCustomersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldCustomersStringFilter


class MetafieldCustomersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldCustomersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldCustomersInCondition = TypedDict("MetafieldCustomersInCondition", {"in": MetafieldCustomersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldCustomersNotCondition = TypedDict("MetafieldCustomersNotCondition", {"not": "MetafieldCustomersCondition"}, total=False)
"""Negates the nested condition."""

MetafieldCustomersAndCondition = TypedDict("MetafieldCustomersAndCondition", {"and": "list[MetafieldCustomersCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldCustomersOrCondition = TypedDict("MetafieldCustomersOrCondition", {"or": "list[MetafieldCustomersCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldCustomersAnyCondition = TypedDict("MetafieldCustomersAnyCondition", {"any": MetafieldCustomersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_customers condition types
MetafieldCustomersCondition = (
    MetafieldCustomersEqCondition
    | MetafieldCustomersNeqCondition
    | MetafieldCustomersGtCondition
    | MetafieldCustomersGteCondition
    | MetafieldCustomersLtCondition
    | MetafieldCustomersLteCondition
    | MetafieldCustomersInCondition
    | MetafieldCustomersLikeCondition
    | MetafieldCustomersFuzzyCondition
    | MetafieldCustomersKeywordCondition
    | MetafieldCustomersContainsCondition
    | MetafieldCustomersNotCondition
    | MetafieldCustomersAndCondition
    | MetafieldCustomersOrCondition
    | MetafieldCustomersAnyCondition
)


class MetafieldCustomersSearchQuery(TypedDict, total=False):
    """Search query for metafield_customers entity."""
    filter: MetafieldCustomersCondition
    sort: list[MetafieldCustomersSortFilter]


# ===== METAFIELD_DRAFT_ORDERS SEARCH TYPES =====

class MetafieldDraftOrdersSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_draft_orders search queries."""
    id: int | None
    """Unique identifier for the metafield"""
    namespace: str | None
    """Namespace group for the metafield"""
    key: str | None
    """Key of the metafield within its namespace"""
    value: str | None
    """Serialized value stored in the metafield"""
    type_: str | None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None
    """Human-readable description of the metafield"""
    owner_id: int | None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldDraftOrdersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the metafield"""
    namespace: list[str]
    """Namespace group for the metafield"""
    key: list[str]
    """Key of the metafield within its namespace"""
    value: list[str]
    """Serialized value stored in the metafield"""
    type_: list[str]
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: list[str]
    """Human-readable description of the metafield"""
    owner_id: list[int]
    """Identifier of the resource that owns this metafield"""
    owner_resource: list[str]
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldDraftOrdersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the metafield"""
    namespace: Any
    """Namespace group for the metafield"""
    key: Any
    """Key of the metafield within its namespace"""
    value: Any
    """Serialized value stored in the metafield"""
    type_: Any
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: Any
    """Human-readable description of the metafield"""
    owner_id: Any
    """Identifier of the resource that owns this metafield"""
    owner_resource: Any
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: Any
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: Any
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldDraftOrdersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the metafield"""
    namespace: str
    """Namespace group for the metafield"""
    key: str
    """Key of the metafield within its namespace"""
    value: str
    """Serialized value stored in the metafield"""
    type_: str
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str
    """Human-readable description of the metafield"""
    owner_id: str
    """Identifier of the resource that owns this metafield"""
    owner_resource: str
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldDraftOrdersSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_draft_orders search results."""
    id: AirbyteSortOrder
    """Unique identifier for the metafield"""
    namespace: AirbyteSortOrder
    """Namespace group for the metafield"""
    key: AirbyteSortOrder
    """Key of the metafield within its namespace"""
    value: AirbyteSortOrder
    """Serialized value stored in the metafield"""
    type_: AirbyteSortOrder
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: AirbyteSortOrder
    """Human-readable description of the metafield"""
    owner_id: AirbyteSortOrder
    """Identifier of the resource that owns this metafield"""
    owner_resource: AirbyteSortOrder
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was last updated"""


# Entity-specific condition types for metafield_draft_orders
class MetafieldDraftOrdersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldDraftOrdersSearchFilter


class MetafieldDraftOrdersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldDraftOrdersSearchFilter


class MetafieldDraftOrdersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldDraftOrdersSearchFilter


class MetafieldDraftOrdersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldDraftOrdersSearchFilter


class MetafieldDraftOrdersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldDraftOrdersSearchFilter


class MetafieldDraftOrdersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldDraftOrdersSearchFilter


class MetafieldDraftOrdersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldDraftOrdersStringFilter


class MetafieldDraftOrdersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldDraftOrdersStringFilter


class MetafieldDraftOrdersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldDraftOrdersStringFilter


class MetafieldDraftOrdersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldDraftOrdersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldDraftOrdersInCondition = TypedDict("MetafieldDraftOrdersInCondition", {"in": MetafieldDraftOrdersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldDraftOrdersNotCondition = TypedDict("MetafieldDraftOrdersNotCondition", {"not": "MetafieldDraftOrdersCondition"}, total=False)
"""Negates the nested condition."""

MetafieldDraftOrdersAndCondition = TypedDict("MetafieldDraftOrdersAndCondition", {"and": "list[MetafieldDraftOrdersCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldDraftOrdersOrCondition = TypedDict("MetafieldDraftOrdersOrCondition", {"or": "list[MetafieldDraftOrdersCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldDraftOrdersAnyCondition = TypedDict("MetafieldDraftOrdersAnyCondition", {"any": MetafieldDraftOrdersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_draft_orders condition types
MetafieldDraftOrdersCondition = (
    MetafieldDraftOrdersEqCondition
    | MetafieldDraftOrdersNeqCondition
    | MetafieldDraftOrdersGtCondition
    | MetafieldDraftOrdersGteCondition
    | MetafieldDraftOrdersLtCondition
    | MetafieldDraftOrdersLteCondition
    | MetafieldDraftOrdersInCondition
    | MetafieldDraftOrdersLikeCondition
    | MetafieldDraftOrdersFuzzyCondition
    | MetafieldDraftOrdersKeywordCondition
    | MetafieldDraftOrdersContainsCondition
    | MetafieldDraftOrdersNotCondition
    | MetafieldDraftOrdersAndCondition
    | MetafieldDraftOrdersOrCondition
    | MetafieldDraftOrdersAnyCondition
)


class MetafieldDraftOrdersSearchQuery(TypedDict, total=False):
    """Search query for metafield_draft_orders entity."""
    filter: MetafieldDraftOrdersCondition
    sort: list[MetafieldDraftOrdersSortFilter]


# ===== METAFIELD_LOCATIONS SEARCH TYPES =====

class MetafieldLocationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_locations search queries."""
    id: int | None
    """Unique identifier for the metafield"""
    namespace: str | None
    """Namespace group for the metafield"""
    key: str | None
    """Key of the metafield within its namespace"""
    value: str | None
    """Serialized value stored in the metafield"""
    type_: str | None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None
    """Human-readable description of the metafield"""
    owner_id: int | None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldLocationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the metafield"""
    namespace: list[str]
    """Namespace group for the metafield"""
    key: list[str]
    """Key of the metafield within its namespace"""
    value: list[str]
    """Serialized value stored in the metafield"""
    type_: list[str]
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: list[str]
    """Human-readable description of the metafield"""
    owner_id: list[int]
    """Identifier of the resource that owns this metafield"""
    owner_resource: list[str]
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldLocationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the metafield"""
    namespace: Any
    """Namespace group for the metafield"""
    key: Any
    """Key of the metafield within its namespace"""
    value: Any
    """Serialized value stored in the metafield"""
    type_: Any
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: Any
    """Human-readable description of the metafield"""
    owner_id: Any
    """Identifier of the resource that owns this metafield"""
    owner_resource: Any
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: Any
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: Any
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldLocationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the metafield"""
    namespace: str
    """Namespace group for the metafield"""
    key: str
    """Key of the metafield within its namespace"""
    value: str
    """Serialized value stored in the metafield"""
    type_: str
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str
    """Human-readable description of the metafield"""
    owner_id: str
    """Identifier of the resource that owns this metafield"""
    owner_resource: str
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldLocationsSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_locations search results."""
    id: AirbyteSortOrder
    """Unique identifier for the metafield"""
    namespace: AirbyteSortOrder
    """Namespace group for the metafield"""
    key: AirbyteSortOrder
    """Key of the metafield within its namespace"""
    value: AirbyteSortOrder
    """Serialized value stored in the metafield"""
    type_: AirbyteSortOrder
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: AirbyteSortOrder
    """Human-readable description of the metafield"""
    owner_id: AirbyteSortOrder
    """Identifier of the resource that owns this metafield"""
    owner_resource: AirbyteSortOrder
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was last updated"""


# Entity-specific condition types for metafield_locations
class MetafieldLocationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldLocationsSearchFilter


class MetafieldLocationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldLocationsSearchFilter


class MetafieldLocationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldLocationsSearchFilter


class MetafieldLocationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldLocationsSearchFilter


class MetafieldLocationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldLocationsSearchFilter


class MetafieldLocationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldLocationsSearchFilter


class MetafieldLocationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldLocationsStringFilter


class MetafieldLocationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldLocationsStringFilter


class MetafieldLocationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldLocationsStringFilter


class MetafieldLocationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldLocationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldLocationsInCondition = TypedDict("MetafieldLocationsInCondition", {"in": MetafieldLocationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldLocationsNotCondition = TypedDict("MetafieldLocationsNotCondition", {"not": "MetafieldLocationsCondition"}, total=False)
"""Negates the nested condition."""

MetafieldLocationsAndCondition = TypedDict("MetafieldLocationsAndCondition", {"and": "list[MetafieldLocationsCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldLocationsOrCondition = TypedDict("MetafieldLocationsOrCondition", {"or": "list[MetafieldLocationsCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldLocationsAnyCondition = TypedDict("MetafieldLocationsAnyCondition", {"any": MetafieldLocationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_locations condition types
MetafieldLocationsCondition = (
    MetafieldLocationsEqCondition
    | MetafieldLocationsNeqCondition
    | MetafieldLocationsGtCondition
    | MetafieldLocationsGteCondition
    | MetafieldLocationsLtCondition
    | MetafieldLocationsLteCondition
    | MetafieldLocationsInCondition
    | MetafieldLocationsLikeCondition
    | MetafieldLocationsFuzzyCondition
    | MetafieldLocationsKeywordCondition
    | MetafieldLocationsContainsCondition
    | MetafieldLocationsNotCondition
    | MetafieldLocationsAndCondition
    | MetafieldLocationsOrCondition
    | MetafieldLocationsAnyCondition
)


class MetafieldLocationsSearchQuery(TypedDict, total=False):
    """Search query for metafield_locations entity."""
    filter: MetafieldLocationsCondition
    sort: list[MetafieldLocationsSortFilter]


# ===== METAFIELD_ORDERS SEARCH TYPES =====

class MetafieldOrdersSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_orders search queries."""
    id: int | None
    """Unique identifier for the metafield"""
    namespace: str | None
    """Namespace group for the metafield"""
    key: str | None
    """Key of the metafield within its namespace"""
    value: str | None
    """Serialized value stored in the metafield"""
    type_: str | None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None
    """Human-readable description of the metafield"""
    owner_id: int | None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldOrdersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the metafield"""
    namespace: list[str]
    """Namespace group for the metafield"""
    key: list[str]
    """Key of the metafield within its namespace"""
    value: list[str]
    """Serialized value stored in the metafield"""
    type_: list[str]
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: list[str]
    """Human-readable description of the metafield"""
    owner_id: list[int]
    """Identifier of the resource that owns this metafield"""
    owner_resource: list[str]
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldOrdersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the metafield"""
    namespace: Any
    """Namespace group for the metafield"""
    key: Any
    """Key of the metafield within its namespace"""
    value: Any
    """Serialized value stored in the metafield"""
    type_: Any
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: Any
    """Human-readable description of the metafield"""
    owner_id: Any
    """Identifier of the resource that owns this metafield"""
    owner_resource: Any
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: Any
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: Any
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldOrdersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the metafield"""
    namespace: str
    """Namespace group for the metafield"""
    key: str
    """Key of the metafield within its namespace"""
    value: str
    """Serialized value stored in the metafield"""
    type_: str
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str
    """Human-readable description of the metafield"""
    owner_id: str
    """Identifier of the resource that owns this metafield"""
    owner_resource: str
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldOrdersSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_orders search results."""
    id: AirbyteSortOrder
    """Unique identifier for the metafield"""
    namespace: AirbyteSortOrder
    """Namespace group for the metafield"""
    key: AirbyteSortOrder
    """Key of the metafield within its namespace"""
    value: AirbyteSortOrder
    """Serialized value stored in the metafield"""
    type_: AirbyteSortOrder
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: AirbyteSortOrder
    """Human-readable description of the metafield"""
    owner_id: AirbyteSortOrder
    """Identifier of the resource that owns this metafield"""
    owner_resource: AirbyteSortOrder
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was last updated"""


# Entity-specific condition types for metafield_orders
class MetafieldOrdersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldOrdersSearchFilter


class MetafieldOrdersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldOrdersSearchFilter


class MetafieldOrdersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldOrdersSearchFilter


class MetafieldOrdersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldOrdersSearchFilter


class MetafieldOrdersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldOrdersSearchFilter


class MetafieldOrdersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldOrdersSearchFilter


class MetafieldOrdersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldOrdersStringFilter


class MetafieldOrdersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldOrdersStringFilter


class MetafieldOrdersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldOrdersStringFilter


class MetafieldOrdersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldOrdersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldOrdersInCondition = TypedDict("MetafieldOrdersInCondition", {"in": MetafieldOrdersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldOrdersNotCondition = TypedDict("MetafieldOrdersNotCondition", {"not": "MetafieldOrdersCondition"}, total=False)
"""Negates the nested condition."""

MetafieldOrdersAndCondition = TypedDict("MetafieldOrdersAndCondition", {"and": "list[MetafieldOrdersCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldOrdersOrCondition = TypedDict("MetafieldOrdersOrCondition", {"or": "list[MetafieldOrdersCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldOrdersAnyCondition = TypedDict("MetafieldOrdersAnyCondition", {"any": MetafieldOrdersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_orders condition types
MetafieldOrdersCondition = (
    MetafieldOrdersEqCondition
    | MetafieldOrdersNeqCondition
    | MetafieldOrdersGtCondition
    | MetafieldOrdersGteCondition
    | MetafieldOrdersLtCondition
    | MetafieldOrdersLteCondition
    | MetafieldOrdersInCondition
    | MetafieldOrdersLikeCondition
    | MetafieldOrdersFuzzyCondition
    | MetafieldOrdersKeywordCondition
    | MetafieldOrdersContainsCondition
    | MetafieldOrdersNotCondition
    | MetafieldOrdersAndCondition
    | MetafieldOrdersOrCondition
    | MetafieldOrdersAnyCondition
)


class MetafieldOrdersSearchQuery(TypedDict, total=False):
    """Search query for metafield_orders entity."""
    filter: MetafieldOrdersCondition
    sort: list[MetafieldOrdersSortFilter]


# ===== METAFIELD_PRODUCT_IMAGES SEARCH TYPES =====

class MetafieldProductImagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_product_images search queries."""
    id: int | None
    """Unique identifier for the metafield"""
    namespace: str | None
    """Namespace group for the metafield"""
    key: str | None
    """Key of the metafield within its namespace"""
    value: str | None
    """Serialized value stored in the metafield"""
    type_: str | None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None
    """Human-readable description of the metafield"""
    owner_id: int | None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductImagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the metafield"""
    namespace: list[str]
    """Namespace group for the metafield"""
    key: list[str]
    """Key of the metafield within its namespace"""
    value: list[str]
    """Serialized value stored in the metafield"""
    type_: list[str]
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: list[str]
    """Human-readable description of the metafield"""
    owner_id: list[int]
    """Identifier of the resource that owns this metafield"""
    owner_resource: list[str]
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductImagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the metafield"""
    namespace: Any
    """Namespace group for the metafield"""
    key: Any
    """Key of the metafield within its namespace"""
    value: Any
    """Serialized value stored in the metafield"""
    type_: Any
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: Any
    """Human-readable description of the metafield"""
    owner_id: Any
    """Identifier of the resource that owns this metafield"""
    owner_resource: Any
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: Any
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: Any
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductImagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the metafield"""
    namespace: str
    """Namespace group for the metafield"""
    key: str
    """Key of the metafield within its namespace"""
    value: str
    """Serialized value stored in the metafield"""
    type_: str
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str
    """Human-readable description of the metafield"""
    owner_id: str
    """Identifier of the resource that owns this metafield"""
    owner_resource: str
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductImagesSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_product_images search results."""
    id: AirbyteSortOrder
    """Unique identifier for the metafield"""
    namespace: AirbyteSortOrder
    """Namespace group for the metafield"""
    key: AirbyteSortOrder
    """Key of the metafield within its namespace"""
    value: AirbyteSortOrder
    """Serialized value stored in the metafield"""
    type_: AirbyteSortOrder
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: AirbyteSortOrder
    """Human-readable description of the metafield"""
    owner_id: AirbyteSortOrder
    """Identifier of the resource that owns this metafield"""
    owner_resource: AirbyteSortOrder
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was last updated"""


# Entity-specific condition types for metafield_product_images
class MetafieldProductImagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldProductImagesSearchFilter


class MetafieldProductImagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldProductImagesSearchFilter


class MetafieldProductImagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldProductImagesSearchFilter


class MetafieldProductImagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldProductImagesSearchFilter


class MetafieldProductImagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldProductImagesSearchFilter


class MetafieldProductImagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldProductImagesSearchFilter


class MetafieldProductImagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldProductImagesStringFilter


class MetafieldProductImagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldProductImagesStringFilter


class MetafieldProductImagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldProductImagesStringFilter


class MetafieldProductImagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldProductImagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldProductImagesInCondition = TypedDict("MetafieldProductImagesInCondition", {"in": MetafieldProductImagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldProductImagesNotCondition = TypedDict("MetafieldProductImagesNotCondition", {"not": "MetafieldProductImagesCondition"}, total=False)
"""Negates the nested condition."""

MetafieldProductImagesAndCondition = TypedDict("MetafieldProductImagesAndCondition", {"and": "list[MetafieldProductImagesCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldProductImagesOrCondition = TypedDict("MetafieldProductImagesOrCondition", {"or": "list[MetafieldProductImagesCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldProductImagesAnyCondition = TypedDict("MetafieldProductImagesAnyCondition", {"any": MetafieldProductImagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_product_images condition types
MetafieldProductImagesCondition = (
    MetafieldProductImagesEqCondition
    | MetafieldProductImagesNeqCondition
    | MetafieldProductImagesGtCondition
    | MetafieldProductImagesGteCondition
    | MetafieldProductImagesLtCondition
    | MetafieldProductImagesLteCondition
    | MetafieldProductImagesInCondition
    | MetafieldProductImagesLikeCondition
    | MetafieldProductImagesFuzzyCondition
    | MetafieldProductImagesKeywordCondition
    | MetafieldProductImagesContainsCondition
    | MetafieldProductImagesNotCondition
    | MetafieldProductImagesAndCondition
    | MetafieldProductImagesOrCondition
    | MetafieldProductImagesAnyCondition
)


class MetafieldProductImagesSearchQuery(TypedDict, total=False):
    """Search query for metafield_product_images entity."""
    filter: MetafieldProductImagesCondition
    sort: list[MetafieldProductImagesSortFilter]


# ===== METAFIELD_PRODUCT_VARIANTS SEARCH TYPES =====

class MetafieldProductVariantsSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_product_variants search queries."""
    id: int | None
    """Unique identifier for the metafield"""
    namespace: str | None
    """Namespace group for the metafield"""
    key: str | None
    """Key of the metafield within its namespace"""
    value: str | None
    """Serialized value stored in the metafield"""
    type_: str | None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None
    """Human-readable description of the metafield"""
    owner_id: int | None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductVariantsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the metafield"""
    namespace: list[str]
    """Namespace group for the metafield"""
    key: list[str]
    """Key of the metafield within its namespace"""
    value: list[str]
    """Serialized value stored in the metafield"""
    type_: list[str]
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: list[str]
    """Human-readable description of the metafield"""
    owner_id: list[int]
    """Identifier of the resource that owns this metafield"""
    owner_resource: list[str]
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductVariantsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the metafield"""
    namespace: Any
    """Namespace group for the metafield"""
    key: Any
    """Key of the metafield within its namespace"""
    value: Any
    """Serialized value stored in the metafield"""
    type_: Any
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: Any
    """Human-readable description of the metafield"""
    owner_id: Any
    """Identifier of the resource that owns this metafield"""
    owner_resource: Any
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: Any
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: Any
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductVariantsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the metafield"""
    namespace: str
    """Namespace group for the metafield"""
    key: str
    """Key of the metafield within its namespace"""
    value: str
    """Serialized value stored in the metafield"""
    type_: str
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str
    """Human-readable description of the metafield"""
    owner_id: str
    """Identifier of the resource that owns this metafield"""
    owner_resource: str
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductVariantsSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_product_variants search results."""
    id: AirbyteSortOrder
    """Unique identifier for the metafield"""
    namespace: AirbyteSortOrder
    """Namespace group for the metafield"""
    key: AirbyteSortOrder
    """Key of the metafield within its namespace"""
    value: AirbyteSortOrder
    """Serialized value stored in the metafield"""
    type_: AirbyteSortOrder
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: AirbyteSortOrder
    """Human-readable description of the metafield"""
    owner_id: AirbyteSortOrder
    """Identifier of the resource that owns this metafield"""
    owner_resource: AirbyteSortOrder
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was last updated"""


# Entity-specific condition types for metafield_product_variants
class MetafieldProductVariantsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldProductVariantsSearchFilter


class MetafieldProductVariantsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldProductVariantsSearchFilter


class MetafieldProductVariantsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldProductVariantsSearchFilter


class MetafieldProductVariantsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldProductVariantsSearchFilter


class MetafieldProductVariantsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldProductVariantsSearchFilter


class MetafieldProductVariantsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldProductVariantsSearchFilter


class MetafieldProductVariantsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldProductVariantsStringFilter


class MetafieldProductVariantsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldProductVariantsStringFilter


class MetafieldProductVariantsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldProductVariantsStringFilter


class MetafieldProductVariantsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldProductVariantsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldProductVariantsInCondition = TypedDict("MetafieldProductVariantsInCondition", {"in": MetafieldProductVariantsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldProductVariantsNotCondition = TypedDict("MetafieldProductVariantsNotCondition", {"not": "MetafieldProductVariantsCondition"}, total=False)
"""Negates the nested condition."""

MetafieldProductVariantsAndCondition = TypedDict("MetafieldProductVariantsAndCondition", {"and": "list[MetafieldProductVariantsCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldProductVariantsOrCondition = TypedDict("MetafieldProductVariantsOrCondition", {"or": "list[MetafieldProductVariantsCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldProductVariantsAnyCondition = TypedDict("MetafieldProductVariantsAnyCondition", {"any": MetafieldProductVariantsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_product_variants condition types
MetafieldProductVariantsCondition = (
    MetafieldProductVariantsEqCondition
    | MetafieldProductVariantsNeqCondition
    | MetafieldProductVariantsGtCondition
    | MetafieldProductVariantsGteCondition
    | MetafieldProductVariantsLtCondition
    | MetafieldProductVariantsLteCondition
    | MetafieldProductVariantsInCondition
    | MetafieldProductVariantsLikeCondition
    | MetafieldProductVariantsFuzzyCondition
    | MetafieldProductVariantsKeywordCondition
    | MetafieldProductVariantsContainsCondition
    | MetafieldProductVariantsNotCondition
    | MetafieldProductVariantsAndCondition
    | MetafieldProductVariantsOrCondition
    | MetafieldProductVariantsAnyCondition
)


class MetafieldProductVariantsSearchQuery(TypedDict, total=False):
    """Search query for metafield_product_variants entity."""
    filter: MetafieldProductVariantsCondition
    sort: list[MetafieldProductVariantsSortFilter]


# ===== METAFIELD_PRODUCTS SEARCH TYPES =====

class MetafieldProductsSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_products search queries."""
    id: int | None
    """Unique identifier for the metafield"""
    namespace: str | None
    """Namespace group for the metafield"""
    key: str | None
    """Key of the metafield within its namespace"""
    value: str | None
    """Serialized value stored in the metafield"""
    type_: str | None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None
    """Human-readable description of the metafield"""
    owner_id: int | None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the metafield"""
    namespace: list[str]
    """Namespace group for the metafield"""
    key: list[str]
    """Key of the metafield within its namespace"""
    value: list[str]
    """Serialized value stored in the metafield"""
    type_: list[str]
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: list[str]
    """Human-readable description of the metafield"""
    owner_id: list[int]
    """Identifier of the resource that owns this metafield"""
    owner_resource: list[str]
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the metafield"""
    namespace: Any
    """Namespace group for the metafield"""
    key: Any
    """Key of the metafield within its namespace"""
    value: Any
    """Serialized value stored in the metafield"""
    type_: Any
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: Any
    """Human-readable description of the metafield"""
    owner_id: Any
    """Identifier of the resource that owns this metafield"""
    owner_resource: Any
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: Any
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: Any
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the metafield"""
    namespace: str
    """Namespace group for the metafield"""
    key: str
    """Key of the metafield within its namespace"""
    value: str
    """Serialized value stored in the metafield"""
    type_: str
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str
    """Human-readable description of the metafield"""
    owner_id: str
    """Identifier of the resource that owns this metafield"""
    owner_resource: str
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldProductsSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_products search results."""
    id: AirbyteSortOrder
    """Unique identifier for the metafield"""
    namespace: AirbyteSortOrder
    """Namespace group for the metafield"""
    key: AirbyteSortOrder
    """Key of the metafield within its namespace"""
    value: AirbyteSortOrder
    """Serialized value stored in the metafield"""
    type_: AirbyteSortOrder
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: AirbyteSortOrder
    """Human-readable description of the metafield"""
    owner_id: AirbyteSortOrder
    """Identifier of the resource that owns this metafield"""
    owner_resource: AirbyteSortOrder
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was last updated"""


# Entity-specific condition types for metafield_products
class MetafieldProductsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldProductsSearchFilter


class MetafieldProductsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldProductsSearchFilter


class MetafieldProductsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldProductsSearchFilter


class MetafieldProductsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldProductsSearchFilter


class MetafieldProductsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldProductsSearchFilter


class MetafieldProductsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldProductsSearchFilter


class MetafieldProductsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldProductsStringFilter


class MetafieldProductsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldProductsStringFilter


class MetafieldProductsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldProductsStringFilter


class MetafieldProductsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldProductsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldProductsInCondition = TypedDict("MetafieldProductsInCondition", {"in": MetafieldProductsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldProductsNotCondition = TypedDict("MetafieldProductsNotCondition", {"not": "MetafieldProductsCondition"}, total=False)
"""Negates the nested condition."""

MetafieldProductsAndCondition = TypedDict("MetafieldProductsAndCondition", {"and": "list[MetafieldProductsCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldProductsOrCondition = TypedDict("MetafieldProductsOrCondition", {"or": "list[MetafieldProductsCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldProductsAnyCondition = TypedDict("MetafieldProductsAnyCondition", {"any": MetafieldProductsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_products condition types
MetafieldProductsCondition = (
    MetafieldProductsEqCondition
    | MetafieldProductsNeqCondition
    | MetafieldProductsGtCondition
    | MetafieldProductsGteCondition
    | MetafieldProductsLtCondition
    | MetafieldProductsLteCondition
    | MetafieldProductsInCondition
    | MetafieldProductsLikeCondition
    | MetafieldProductsFuzzyCondition
    | MetafieldProductsKeywordCondition
    | MetafieldProductsContainsCondition
    | MetafieldProductsNotCondition
    | MetafieldProductsAndCondition
    | MetafieldProductsOrCondition
    | MetafieldProductsAnyCondition
)


class MetafieldProductsSearchQuery(TypedDict, total=False):
    """Search query for metafield_products entity."""
    filter: MetafieldProductsCondition
    sort: list[MetafieldProductsSortFilter]


# ===== METAFIELD_SHOPS SEARCH TYPES =====

class MetafieldShopsSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_shops search queries."""
    id: int | None
    """Unique identifier for the metafield"""
    namespace: str | None
    """Namespace group for the metafield"""
    key: str | None
    """Key of the metafield within its namespace"""
    value: str | None
    """Serialized value stored in the metafield"""
    type_: str | None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None
    """Human-readable description of the metafield"""
    owner_id: int | None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldShopsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the metafield"""
    namespace: list[str]
    """Namespace group for the metafield"""
    key: list[str]
    """Key of the metafield within its namespace"""
    value: list[str]
    """Serialized value stored in the metafield"""
    type_: list[str]
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: list[str]
    """Human-readable description of the metafield"""
    owner_id: list[int]
    """Identifier of the resource that owns this metafield"""
    owner_resource: list[str]
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldShopsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the metafield"""
    namespace: Any
    """Namespace group for the metafield"""
    key: Any
    """Key of the metafield within its namespace"""
    value: Any
    """Serialized value stored in the metafield"""
    type_: Any
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: Any
    """Human-readable description of the metafield"""
    owner_id: Any
    """Identifier of the resource that owns this metafield"""
    owner_resource: Any
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: Any
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: Any
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldShopsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the metafield"""
    namespace: str
    """Namespace group for the metafield"""
    key: str
    """Key of the metafield within its namespace"""
    value: str
    """Serialized value stored in the metafield"""
    type_: str
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str
    """Human-readable description of the metafield"""
    owner_id: str
    """Identifier of the resource that owns this metafield"""
    owner_resource: str
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldShopsSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_shops search results."""
    id: AirbyteSortOrder
    """Unique identifier for the metafield"""
    namespace: AirbyteSortOrder
    """Namespace group for the metafield"""
    key: AirbyteSortOrder
    """Key of the metafield within its namespace"""
    value: AirbyteSortOrder
    """Serialized value stored in the metafield"""
    type_: AirbyteSortOrder
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: AirbyteSortOrder
    """Human-readable description of the metafield"""
    owner_id: AirbyteSortOrder
    """Identifier of the resource that owns this metafield"""
    owner_resource: AirbyteSortOrder
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was last updated"""


# Entity-specific condition types for metafield_shops
class MetafieldShopsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldShopsSearchFilter


class MetafieldShopsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldShopsSearchFilter


class MetafieldShopsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldShopsSearchFilter


class MetafieldShopsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldShopsSearchFilter


class MetafieldShopsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldShopsSearchFilter


class MetafieldShopsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldShopsSearchFilter


class MetafieldShopsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldShopsStringFilter


class MetafieldShopsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldShopsStringFilter


class MetafieldShopsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldShopsStringFilter


class MetafieldShopsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldShopsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldShopsInCondition = TypedDict("MetafieldShopsInCondition", {"in": MetafieldShopsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldShopsNotCondition = TypedDict("MetafieldShopsNotCondition", {"not": "MetafieldShopsCondition"}, total=False)
"""Negates the nested condition."""

MetafieldShopsAndCondition = TypedDict("MetafieldShopsAndCondition", {"and": "list[MetafieldShopsCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldShopsOrCondition = TypedDict("MetafieldShopsOrCondition", {"or": "list[MetafieldShopsCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldShopsAnyCondition = TypedDict("MetafieldShopsAnyCondition", {"any": MetafieldShopsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_shops condition types
MetafieldShopsCondition = (
    MetafieldShopsEqCondition
    | MetafieldShopsNeqCondition
    | MetafieldShopsGtCondition
    | MetafieldShopsGteCondition
    | MetafieldShopsLtCondition
    | MetafieldShopsLteCondition
    | MetafieldShopsInCondition
    | MetafieldShopsLikeCondition
    | MetafieldShopsFuzzyCondition
    | MetafieldShopsKeywordCondition
    | MetafieldShopsContainsCondition
    | MetafieldShopsNotCondition
    | MetafieldShopsAndCondition
    | MetafieldShopsOrCondition
    | MetafieldShopsAnyCondition
)


class MetafieldShopsSearchQuery(TypedDict, total=False):
    """Search query for metafield_shops entity."""
    filter: MetafieldShopsCondition
    sort: list[MetafieldShopsSortFilter]


# ===== METAFIELD_SMART_COLLECTIONS SEARCH TYPES =====

class MetafieldSmartCollectionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_smart_collections search queries."""
    id: int | None
    """Unique identifier for the metafield"""
    namespace: str | None
    """Namespace group for the metafield"""
    key: str | None
    """Key of the metafield within its namespace"""
    value: str | None
    """Serialized value stored in the metafield"""
    type_: str | None
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str | None
    """Human-readable description of the metafield"""
    owner_id: int | None
    """Identifier of the resource that owns this metafield"""
    owner_resource: str | None
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str | None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldSmartCollectionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the metafield"""
    namespace: list[str]
    """Namespace group for the metafield"""
    key: list[str]
    """Key of the metafield within its namespace"""
    value: list[str]
    """Serialized value stored in the metafield"""
    type_: list[str]
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: list[str]
    """Human-readable description of the metafield"""
    owner_id: list[int]
    """Identifier of the resource that owns this metafield"""
    owner_resource: list[str]
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldSmartCollectionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the metafield"""
    namespace: Any
    """Namespace group for the metafield"""
    key: Any
    """Key of the metafield within its namespace"""
    value: Any
    """Serialized value stored in the metafield"""
    type_: Any
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: Any
    """Human-readable description of the metafield"""
    owner_id: Any
    """Identifier of the resource that owns this metafield"""
    owner_resource: Any
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: Any
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: Any
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldSmartCollectionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the metafield"""
    namespace: str
    """Namespace group for the metafield"""
    key: str
    """Key of the metafield within its namespace"""
    value: str
    """Serialized value stored in the metafield"""
    type_: str
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: str
    """Human-readable description of the metafield"""
    owner_id: str
    """Identifier of the resource that owns this metafield"""
    owner_resource: str
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: str
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldSmartCollectionsSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_smart_collections search results."""
    id: AirbyteSortOrder
    """Unique identifier for the metafield"""
    namespace: AirbyteSortOrder
    """Namespace group for the metafield"""
    key: AirbyteSortOrder
    """Key of the metafield within its namespace"""
    value: AirbyteSortOrder
    """Serialized value stored in the metafield"""
    type_: AirbyteSortOrder
    """Shopify metafield type (e.g. `single_line_text_field`, `json`)"""
    description: AirbyteSortOrder
    """Human-readable description of the metafield"""
    owner_id: AirbyteSortOrder
    """Identifier of the resource that owns this metafield"""
    owner_resource: AirbyteSortOrder
    """Resource type that owns this metafield (e.g. `product`, `customer`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was last updated"""


# Entity-specific condition types for metafield_smart_collections
class MetafieldSmartCollectionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldSmartCollectionsSearchFilter


class MetafieldSmartCollectionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldSmartCollectionsSearchFilter


class MetafieldSmartCollectionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldSmartCollectionsSearchFilter


class MetafieldSmartCollectionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldSmartCollectionsSearchFilter


class MetafieldSmartCollectionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldSmartCollectionsSearchFilter


class MetafieldSmartCollectionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldSmartCollectionsSearchFilter


class MetafieldSmartCollectionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldSmartCollectionsStringFilter


class MetafieldSmartCollectionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldSmartCollectionsStringFilter


class MetafieldSmartCollectionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldSmartCollectionsStringFilter


class MetafieldSmartCollectionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldSmartCollectionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldSmartCollectionsInCondition = TypedDict("MetafieldSmartCollectionsInCondition", {"in": MetafieldSmartCollectionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldSmartCollectionsNotCondition = TypedDict("MetafieldSmartCollectionsNotCondition", {"not": "MetafieldSmartCollectionsCondition"}, total=False)
"""Negates the nested condition."""

MetafieldSmartCollectionsAndCondition = TypedDict("MetafieldSmartCollectionsAndCondition", {"and": "list[MetafieldSmartCollectionsCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldSmartCollectionsOrCondition = TypedDict("MetafieldSmartCollectionsOrCondition", {"or": "list[MetafieldSmartCollectionsCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldSmartCollectionsAnyCondition = TypedDict("MetafieldSmartCollectionsAnyCondition", {"any": MetafieldSmartCollectionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_smart_collections condition types
MetafieldSmartCollectionsCondition = (
    MetafieldSmartCollectionsEqCondition
    | MetafieldSmartCollectionsNeqCondition
    | MetafieldSmartCollectionsGtCondition
    | MetafieldSmartCollectionsGteCondition
    | MetafieldSmartCollectionsLtCondition
    | MetafieldSmartCollectionsLteCondition
    | MetafieldSmartCollectionsInCondition
    | MetafieldSmartCollectionsLikeCondition
    | MetafieldSmartCollectionsFuzzyCondition
    | MetafieldSmartCollectionsKeywordCondition
    | MetafieldSmartCollectionsContainsCondition
    | MetafieldSmartCollectionsNotCondition
    | MetafieldSmartCollectionsAndCondition
    | MetafieldSmartCollectionsOrCondition
    | MetafieldSmartCollectionsAnyCondition
)


class MetafieldSmartCollectionsSearchQuery(TypedDict, total=False):
    """Search query for metafield_smart_collections entity."""
    filter: MetafieldSmartCollectionsCondition
    sort: list[MetafieldSmartCollectionsSortFilter]


# ===== ORDER_REFUNDS SEARCH TYPES =====

class OrderRefundsSearchFilter(TypedDict, total=False):
    """Available fields for filtering order_refunds search queries."""
    id: int | None
    """Unique identifier for the refund"""
    order_id: int | None
    """Identifier of the refunded order"""
    user_id: int | None
    """Identifier of the staff user who processed the refund"""
    note: str | None
    """Merchant-provided note explaining the refund"""
    created_at: str | None
    """ISO 8601 timestamp when the refund was created"""
    processed_at: str | None
    """ISO 8601 timestamp when the refund was processed"""


class OrderRefundsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the refund"""
    order_id: list[int]
    """Identifier of the refunded order"""
    user_id: list[int]
    """Identifier of the staff user who processed the refund"""
    note: list[str]
    """Merchant-provided note explaining the refund"""
    created_at: list[str]
    """ISO 8601 timestamp when the refund was created"""
    processed_at: list[str]
    """ISO 8601 timestamp when the refund was processed"""


class OrderRefundsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the refund"""
    order_id: Any
    """Identifier of the refunded order"""
    user_id: Any
    """Identifier of the staff user who processed the refund"""
    note: Any
    """Merchant-provided note explaining the refund"""
    created_at: Any
    """ISO 8601 timestamp when the refund was created"""
    processed_at: Any
    """ISO 8601 timestamp when the refund was processed"""


class OrderRefundsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the refund"""
    order_id: str
    """Identifier of the refunded order"""
    user_id: str
    """Identifier of the staff user who processed the refund"""
    note: str
    """Merchant-provided note explaining the refund"""
    created_at: str
    """ISO 8601 timestamp when the refund was created"""
    processed_at: str
    """ISO 8601 timestamp when the refund was processed"""


class OrderRefundsSortFilter(TypedDict, total=False):
    """Available fields for sorting order_refunds search results."""
    id: AirbyteSortOrder
    """Unique identifier for the refund"""
    order_id: AirbyteSortOrder
    """Identifier of the refunded order"""
    user_id: AirbyteSortOrder
    """Identifier of the staff user who processed the refund"""
    note: AirbyteSortOrder
    """Merchant-provided note explaining the refund"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the refund was created"""
    processed_at: AirbyteSortOrder
    """ISO 8601 timestamp when the refund was processed"""


# Entity-specific condition types for order_refunds
class OrderRefundsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OrderRefundsSearchFilter


class OrderRefundsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OrderRefundsSearchFilter


class OrderRefundsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OrderRefundsSearchFilter


class OrderRefundsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OrderRefundsSearchFilter


class OrderRefundsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OrderRefundsSearchFilter


class OrderRefundsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OrderRefundsSearchFilter


class OrderRefundsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OrderRefundsStringFilter


class OrderRefundsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OrderRefundsStringFilter


class OrderRefundsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OrderRefundsStringFilter


class OrderRefundsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OrderRefundsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OrderRefundsInCondition = TypedDict("OrderRefundsInCondition", {"in": OrderRefundsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OrderRefundsNotCondition = TypedDict("OrderRefundsNotCondition", {"not": "OrderRefundsCondition"}, total=False)
"""Negates the nested condition."""

OrderRefundsAndCondition = TypedDict("OrderRefundsAndCondition", {"and": "list[OrderRefundsCondition]"}, total=False)
"""True if all nested conditions are true."""

OrderRefundsOrCondition = TypedDict("OrderRefundsOrCondition", {"or": "list[OrderRefundsCondition]"}, total=False)
"""True if any nested condition is true."""

OrderRefundsAnyCondition = TypedDict("OrderRefundsAnyCondition", {"any": OrderRefundsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all order_refunds condition types
OrderRefundsCondition = (
    OrderRefundsEqCondition
    | OrderRefundsNeqCondition
    | OrderRefundsGtCondition
    | OrderRefundsGteCondition
    | OrderRefundsLtCondition
    | OrderRefundsLteCondition
    | OrderRefundsInCondition
    | OrderRefundsLikeCondition
    | OrderRefundsFuzzyCondition
    | OrderRefundsKeywordCondition
    | OrderRefundsContainsCondition
    | OrderRefundsNotCondition
    | OrderRefundsAndCondition
    | OrderRefundsOrCondition
    | OrderRefundsAnyCondition
)


class OrderRefundsSearchQuery(TypedDict, total=False):
    """Search query for order_refunds entity."""
    filter: OrderRefundsCondition
    sort: list[OrderRefundsSortFilter]


# ===== ORDERS SEARCH TYPES =====

class OrdersSearchFilter(TypedDict, total=False):
    """Available fields for filtering orders search queries."""
    id: int | None
    """Unique identifier for the order"""
    name: str | None
    """Shopify-assigned display name for the order (e.g. `#1001`)"""
    email: str | None
    """Email address associated with the order"""
    phone: str | None
    """Phone number associated with the order"""
    order_number: int | None
    """Sequential order number displayed in the Shopify admin"""
    financial_status: str | None
    """Payment status of the order (e.g. `paid`, `pending`, `refunded`, `partially_refunded`)"""
    fulfillment_status: str | None
    """Fulfillment status of the order (e.g. `fulfilled`, `partial`, `null` for unfulfilled)"""
    currency: str | None
    """ISO 4217 currency code for the order totals"""
    total_price: str | None
    """Total price of the order including taxes and discounts"""
    subtotal_price: str | None
    """Subtotal of the order before shipping and taxes"""
    total_tax: str | None
    """Total tax amount applied to the order"""
    total_discounts: str | None
    """Total discount amount applied to the order"""
    total_weight: int | None
    """Total weight of all items in the order, in grams"""
    cancel_reason: str | None
    """Reason the order was cancelled, if applicable"""
    cancelled_at: str | None
    """ISO 8601 timestamp when the order was cancelled, if applicable"""
    closed_at: str | None
    """ISO 8601 timestamp when the order was closed, if applicable"""
    tags: str | None
    """Comma-separated tags attached to the order"""
    note: str | None
    """Merchant-provided note on the order"""
    processed_at: str | None
    """ISO 8601 timestamp when the order was processed"""
    created_at: str | None
    """ISO 8601 timestamp when the order was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the order was last updated"""


class OrdersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the order"""
    name: list[str]
    """Shopify-assigned display name for the order (e.g. `#1001`)"""
    email: list[str]
    """Email address associated with the order"""
    phone: list[str]
    """Phone number associated with the order"""
    order_number: list[int]
    """Sequential order number displayed in the Shopify admin"""
    financial_status: list[str]
    """Payment status of the order (e.g. `paid`, `pending`, `refunded`, `partially_refunded`)"""
    fulfillment_status: list[str]
    """Fulfillment status of the order (e.g. `fulfilled`, `partial`, `null` for unfulfilled)"""
    currency: list[str]
    """ISO 4217 currency code for the order totals"""
    total_price: list[str]
    """Total price of the order including taxes and discounts"""
    subtotal_price: list[str]
    """Subtotal of the order before shipping and taxes"""
    total_tax: list[str]
    """Total tax amount applied to the order"""
    total_discounts: list[str]
    """Total discount amount applied to the order"""
    total_weight: list[int]
    """Total weight of all items in the order, in grams"""
    cancel_reason: list[str]
    """Reason the order was cancelled, if applicable"""
    cancelled_at: list[str]
    """ISO 8601 timestamp when the order was cancelled, if applicable"""
    closed_at: list[str]
    """ISO 8601 timestamp when the order was closed, if applicable"""
    tags: list[str]
    """Comma-separated tags attached to the order"""
    note: list[str]
    """Merchant-provided note on the order"""
    processed_at: list[str]
    """ISO 8601 timestamp when the order was processed"""
    created_at: list[str]
    """ISO 8601 timestamp when the order was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the order was last updated"""


class OrdersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the order"""
    name: Any
    """Shopify-assigned display name for the order (e.g. `#1001`)"""
    email: Any
    """Email address associated with the order"""
    phone: Any
    """Phone number associated with the order"""
    order_number: Any
    """Sequential order number displayed in the Shopify admin"""
    financial_status: Any
    """Payment status of the order (e.g. `paid`, `pending`, `refunded`, `partially_refunded`)"""
    fulfillment_status: Any
    """Fulfillment status of the order (e.g. `fulfilled`, `partial`, `null` for unfulfilled)"""
    currency: Any
    """ISO 4217 currency code for the order totals"""
    total_price: Any
    """Total price of the order including taxes and discounts"""
    subtotal_price: Any
    """Subtotal of the order before shipping and taxes"""
    total_tax: Any
    """Total tax amount applied to the order"""
    total_discounts: Any
    """Total discount amount applied to the order"""
    total_weight: Any
    """Total weight of all items in the order, in grams"""
    cancel_reason: Any
    """Reason the order was cancelled, if applicable"""
    cancelled_at: Any
    """ISO 8601 timestamp when the order was cancelled, if applicable"""
    closed_at: Any
    """ISO 8601 timestamp when the order was closed, if applicable"""
    tags: Any
    """Comma-separated tags attached to the order"""
    note: Any
    """Merchant-provided note on the order"""
    processed_at: Any
    """ISO 8601 timestamp when the order was processed"""
    created_at: Any
    """ISO 8601 timestamp when the order was created"""
    updated_at: Any
    """ISO 8601 timestamp when the order was last updated"""


class OrdersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the order"""
    name: str
    """Shopify-assigned display name for the order (e.g. `#1001`)"""
    email: str
    """Email address associated with the order"""
    phone: str
    """Phone number associated with the order"""
    order_number: str
    """Sequential order number displayed in the Shopify admin"""
    financial_status: str
    """Payment status of the order (e.g. `paid`, `pending`, `refunded`, `partially_refunded`)"""
    fulfillment_status: str
    """Fulfillment status of the order (e.g. `fulfilled`, `partial`, `null` for unfulfilled)"""
    currency: str
    """ISO 4217 currency code for the order totals"""
    total_price: str
    """Total price of the order including taxes and discounts"""
    subtotal_price: str
    """Subtotal of the order before shipping and taxes"""
    total_tax: str
    """Total tax amount applied to the order"""
    total_discounts: str
    """Total discount amount applied to the order"""
    total_weight: str
    """Total weight of all items in the order, in grams"""
    cancel_reason: str
    """Reason the order was cancelled, if applicable"""
    cancelled_at: str
    """ISO 8601 timestamp when the order was cancelled, if applicable"""
    closed_at: str
    """ISO 8601 timestamp when the order was closed, if applicable"""
    tags: str
    """Comma-separated tags attached to the order"""
    note: str
    """Merchant-provided note on the order"""
    processed_at: str
    """ISO 8601 timestamp when the order was processed"""
    created_at: str
    """ISO 8601 timestamp when the order was created"""
    updated_at: str
    """ISO 8601 timestamp when the order was last updated"""


class OrdersSortFilter(TypedDict, total=False):
    """Available fields for sorting orders search results."""
    id: AirbyteSortOrder
    """Unique identifier for the order"""
    name: AirbyteSortOrder
    """Shopify-assigned display name for the order (e.g. `#1001`)"""
    email: AirbyteSortOrder
    """Email address associated with the order"""
    phone: AirbyteSortOrder
    """Phone number associated with the order"""
    order_number: AirbyteSortOrder
    """Sequential order number displayed in the Shopify admin"""
    financial_status: AirbyteSortOrder
    """Payment status of the order (e.g. `paid`, `pending`, `refunded`, `partially_refunded`)"""
    fulfillment_status: AirbyteSortOrder
    """Fulfillment status of the order (e.g. `fulfilled`, `partial`, `null` for unfulfilled)"""
    currency: AirbyteSortOrder
    """ISO 4217 currency code for the order totals"""
    total_price: AirbyteSortOrder
    """Total price of the order including taxes and discounts"""
    subtotal_price: AirbyteSortOrder
    """Subtotal of the order before shipping and taxes"""
    total_tax: AirbyteSortOrder
    """Total tax amount applied to the order"""
    total_discounts: AirbyteSortOrder
    """Total discount amount applied to the order"""
    total_weight: AirbyteSortOrder
    """Total weight of all items in the order, in grams"""
    cancel_reason: AirbyteSortOrder
    """Reason the order was cancelled, if applicable"""
    cancelled_at: AirbyteSortOrder
    """ISO 8601 timestamp when the order was cancelled, if applicable"""
    closed_at: AirbyteSortOrder
    """ISO 8601 timestamp when the order was closed, if applicable"""
    tags: AirbyteSortOrder
    """Comma-separated tags attached to the order"""
    note: AirbyteSortOrder
    """Merchant-provided note on the order"""
    processed_at: AirbyteSortOrder
    """ISO 8601 timestamp when the order was processed"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the order was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the order was last updated"""


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


# ===== PRICE_RULES SEARCH TYPES =====

class PriceRulesSearchFilter(TypedDict, total=False):
    """Available fields for filtering price_rules search queries."""
    id: int | None
    """Unique identifier for the price rule"""
    title: str | None
    """Administrative title of the price rule"""
    value_type: str | None
    """How the discount value is interpreted (`fixed_amount` or `percentage`)"""
    value: str | None
    """Discount value applied by the rule"""
    target_type: str | None
    """Type of target the rule applies to (`line_item` or `shipping_line`)"""
    target_selection: str | None
    """Which target items the rule applies to (`all` or `entitled`)"""
    allocation_method: str | None
    """How the discount is allocated (`each` or `across`)"""
    starts_at: str | None
    """ISO 8601 timestamp when the rule starts being active"""
    ends_at: str | None
    """ISO 8601 timestamp when the rule stops being active, if applicable"""
    created_at: str | None
    """ISO 8601 timestamp when the rule was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the rule was last updated"""


class PriceRulesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the price rule"""
    title: list[str]
    """Administrative title of the price rule"""
    value_type: list[str]
    """How the discount value is interpreted (`fixed_amount` or `percentage`)"""
    value: list[str]
    """Discount value applied by the rule"""
    target_type: list[str]
    """Type of target the rule applies to (`line_item` or `shipping_line`)"""
    target_selection: list[str]
    """Which target items the rule applies to (`all` or `entitled`)"""
    allocation_method: list[str]
    """How the discount is allocated (`each` or `across`)"""
    starts_at: list[str]
    """ISO 8601 timestamp when the rule starts being active"""
    ends_at: list[str]
    """ISO 8601 timestamp when the rule stops being active, if applicable"""
    created_at: list[str]
    """ISO 8601 timestamp when the rule was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the rule was last updated"""


class PriceRulesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the price rule"""
    title: Any
    """Administrative title of the price rule"""
    value_type: Any
    """How the discount value is interpreted (`fixed_amount` or `percentage`)"""
    value: Any
    """Discount value applied by the rule"""
    target_type: Any
    """Type of target the rule applies to (`line_item` or `shipping_line`)"""
    target_selection: Any
    """Which target items the rule applies to (`all` or `entitled`)"""
    allocation_method: Any
    """How the discount is allocated (`each` or `across`)"""
    starts_at: Any
    """ISO 8601 timestamp when the rule starts being active"""
    ends_at: Any
    """ISO 8601 timestamp when the rule stops being active, if applicable"""
    created_at: Any
    """ISO 8601 timestamp when the rule was created"""
    updated_at: Any
    """ISO 8601 timestamp when the rule was last updated"""


class PriceRulesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the price rule"""
    title: str
    """Administrative title of the price rule"""
    value_type: str
    """How the discount value is interpreted (`fixed_amount` or `percentage`)"""
    value: str
    """Discount value applied by the rule"""
    target_type: str
    """Type of target the rule applies to (`line_item` or `shipping_line`)"""
    target_selection: str
    """Which target items the rule applies to (`all` or `entitled`)"""
    allocation_method: str
    """How the discount is allocated (`each` or `across`)"""
    starts_at: str
    """ISO 8601 timestamp when the rule starts being active"""
    ends_at: str
    """ISO 8601 timestamp when the rule stops being active, if applicable"""
    created_at: str
    """ISO 8601 timestamp when the rule was created"""
    updated_at: str
    """ISO 8601 timestamp when the rule was last updated"""


class PriceRulesSortFilter(TypedDict, total=False):
    """Available fields for sorting price_rules search results."""
    id: AirbyteSortOrder
    """Unique identifier for the price rule"""
    title: AirbyteSortOrder
    """Administrative title of the price rule"""
    value_type: AirbyteSortOrder
    """How the discount value is interpreted (`fixed_amount` or `percentage`)"""
    value: AirbyteSortOrder
    """Discount value applied by the rule"""
    target_type: AirbyteSortOrder
    """Type of target the rule applies to (`line_item` or `shipping_line`)"""
    target_selection: AirbyteSortOrder
    """Which target items the rule applies to (`all` or `entitled`)"""
    allocation_method: AirbyteSortOrder
    """How the discount is allocated (`each` or `across`)"""
    starts_at: AirbyteSortOrder
    """ISO 8601 timestamp when the rule starts being active"""
    ends_at: AirbyteSortOrder
    """ISO 8601 timestamp when the rule stops being active, if applicable"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the rule was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the rule was last updated"""


# Entity-specific condition types for price_rules
class PriceRulesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PriceRulesSearchFilter


class PriceRulesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PriceRulesSearchFilter


class PriceRulesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PriceRulesSearchFilter


class PriceRulesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PriceRulesSearchFilter


class PriceRulesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PriceRulesSearchFilter


class PriceRulesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PriceRulesSearchFilter


class PriceRulesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PriceRulesStringFilter


class PriceRulesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PriceRulesStringFilter


class PriceRulesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PriceRulesStringFilter


class PriceRulesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PriceRulesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PriceRulesInCondition = TypedDict("PriceRulesInCondition", {"in": PriceRulesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PriceRulesNotCondition = TypedDict("PriceRulesNotCondition", {"not": "PriceRulesCondition"}, total=False)
"""Negates the nested condition."""

PriceRulesAndCondition = TypedDict("PriceRulesAndCondition", {"and": "list[PriceRulesCondition]"}, total=False)
"""True if all nested conditions are true."""

PriceRulesOrCondition = TypedDict("PriceRulesOrCondition", {"or": "list[PriceRulesCondition]"}, total=False)
"""True if any nested condition is true."""

PriceRulesAnyCondition = TypedDict("PriceRulesAnyCondition", {"any": PriceRulesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all price_rules condition types
PriceRulesCondition = (
    PriceRulesEqCondition
    | PriceRulesNeqCondition
    | PriceRulesGtCondition
    | PriceRulesGteCondition
    | PriceRulesLtCondition
    | PriceRulesLteCondition
    | PriceRulesInCondition
    | PriceRulesLikeCondition
    | PriceRulesFuzzyCondition
    | PriceRulesKeywordCondition
    | PriceRulesContainsCondition
    | PriceRulesNotCondition
    | PriceRulesAndCondition
    | PriceRulesOrCondition
    | PriceRulesAnyCondition
)


class PriceRulesSearchQuery(TypedDict, total=False):
    """Search query for price_rules entity."""
    filter: PriceRulesCondition
    sort: list[PriceRulesSortFilter]


# ===== PRODUCT_IMAGES SEARCH TYPES =====

class ProductImagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering product_images search queries."""
    id: int | None
    """Unique identifier for the product image"""
    product_id: int | None
    """Identifier of the product the image belongs to"""
    position: int | None
    """Display position of the image within the product"""
    alt: str | None
    """Alt text for the image"""
    width: int | None
    """Image width in pixels"""
    height: int | None
    """Image height in pixels"""
    src: str | None
    """Public URL of the image"""
    created_at: str | None
    """ISO 8601 timestamp when the image was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the image was last updated"""


class ProductImagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the product image"""
    product_id: list[int]
    """Identifier of the product the image belongs to"""
    position: list[int]
    """Display position of the image within the product"""
    alt: list[str]
    """Alt text for the image"""
    width: list[int]
    """Image width in pixels"""
    height: list[int]
    """Image height in pixels"""
    src: list[str]
    """Public URL of the image"""
    created_at: list[str]
    """ISO 8601 timestamp when the image was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the image was last updated"""


class ProductImagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the product image"""
    product_id: Any
    """Identifier of the product the image belongs to"""
    position: Any
    """Display position of the image within the product"""
    alt: Any
    """Alt text for the image"""
    width: Any
    """Image width in pixels"""
    height: Any
    """Image height in pixels"""
    src: Any
    """Public URL of the image"""
    created_at: Any
    """ISO 8601 timestamp when the image was created"""
    updated_at: Any
    """ISO 8601 timestamp when the image was last updated"""


class ProductImagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the product image"""
    product_id: str
    """Identifier of the product the image belongs to"""
    position: str
    """Display position of the image within the product"""
    alt: str
    """Alt text for the image"""
    width: str
    """Image width in pixels"""
    height: str
    """Image height in pixels"""
    src: str
    """Public URL of the image"""
    created_at: str
    """ISO 8601 timestamp when the image was created"""
    updated_at: str
    """ISO 8601 timestamp when the image was last updated"""


class ProductImagesSortFilter(TypedDict, total=False):
    """Available fields for sorting product_images search results."""
    id: AirbyteSortOrder
    """Unique identifier for the product image"""
    product_id: AirbyteSortOrder
    """Identifier of the product the image belongs to"""
    position: AirbyteSortOrder
    """Display position of the image within the product"""
    alt: AirbyteSortOrder
    """Alt text for the image"""
    width: AirbyteSortOrder
    """Image width in pixels"""
    height: AirbyteSortOrder
    """Image height in pixels"""
    src: AirbyteSortOrder
    """Public URL of the image"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the image was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the image was last updated"""


# Entity-specific condition types for product_images
class ProductImagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProductImagesSearchFilter


class ProductImagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProductImagesSearchFilter


class ProductImagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProductImagesSearchFilter


class ProductImagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProductImagesSearchFilter


class ProductImagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProductImagesSearchFilter


class ProductImagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProductImagesSearchFilter


class ProductImagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProductImagesStringFilter


class ProductImagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProductImagesStringFilter


class ProductImagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProductImagesStringFilter


class ProductImagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProductImagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProductImagesInCondition = TypedDict("ProductImagesInCondition", {"in": ProductImagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProductImagesNotCondition = TypedDict("ProductImagesNotCondition", {"not": "ProductImagesCondition"}, total=False)
"""Negates the nested condition."""

ProductImagesAndCondition = TypedDict("ProductImagesAndCondition", {"and": "list[ProductImagesCondition]"}, total=False)
"""True if all nested conditions are true."""

ProductImagesOrCondition = TypedDict("ProductImagesOrCondition", {"or": "list[ProductImagesCondition]"}, total=False)
"""True if any nested condition is true."""

ProductImagesAnyCondition = TypedDict("ProductImagesAnyCondition", {"any": ProductImagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all product_images condition types
ProductImagesCondition = (
    ProductImagesEqCondition
    | ProductImagesNeqCondition
    | ProductImagesGtCondition
    | ProductImagesGteCondition
    | ProductImagesLtCondition
    | ProductImagesLteCondition
    | ProductImagesInCondition
    | ProductImagesLikeCondition
    | ProductImagesFuzzyCondition
    | ProductImagesKeywordCondition
    | ProductImagesContainsCondition
    | ProductImagesNotCondition
    | ProductImagesAndCondition
    | ProductImagesOrCondition
    | ProductImagesAnyCondition
)


class ProductImagesSearchQuery(TypedDict, total=False):
    """Search query for product_images entity."""
    filter: ProductImagesCondition
    sort: list[ProductImagesSortFilter]


# ===== PRODUCTS SEARCH TYPES =====

class ProductsSearchFilter(TypedDict, total=False):
    """Available fields for filtering products search queries."""
    id: int | None
    """Unique identifier for the product"""
    title: str | None
    """Product title"""
    body_html: str | None
    """Product description in HTML"""
    vendor: str | None
    """Product vendor or manufacturer"""
    product_type: str | None
    """Product type used for categorization"""
    handle: str | None
    """URL-friendly handle for the product"""
    status: str | None
    """Product status (`active`, `archived`, or `draft`)"""
    tags: str | None
    """Comma-separated tags attached to the product"""
    published_scope: str | None
    """Publishing scope (`web` or `global`)"""
    published_at: str | None
    """ISO 8601 timestamp when the product was published"""
    created_at: str | None
    """ISO 8601 timestamp when the product was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the product was last updated"""


class ProductsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the product"""
    title: list[str]
    """Product title"""
    body_html: list[str]
    """Product description in HTML"""
    vendor: list[str]
    """Product vendor or manufacturer"""
    product_type: list[str]
    """Product type used for categorization"""
    handle: list[str]
    """URL-friendly handle for the product"""
    status: list[str]
    """Product status (`active`, `archived`, or `draft`)"""
    tags: list[str]
    """Comma-separated tags attached to the product"""
    published_scope: list[str]
    """Publishing scope (`web` or `global`)"""
    published_at: list[str]
    """ISO 8601 timestamp when the product was published"""
    created_at: list[str]
    """ISO 8601 timestamp when the product was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the product was last updated"""


class ProductsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the product"""
    title: Any
    """Product title"""
    body_html: Any
    """Product description in HTML"""
    vendor: Any
    """Product vendor or manufacturer"""
    product_type: Any
    """Product type used for categorization"""
    handle: Any
    """URL-friendly handle for the product"""
    status: Any
    """Product status (`active`, `archived`, or `draft`)"""
    tags: Any
    """Comma-separated tags attached to the product"""
    published_scope: Any
    """Publishing scope (`web` or `global`)"""
    published_at: Any
    """ISO 8601 timestamp when the product was published"""
    created_at: Any
    """ISO 8601 timestamp when the product was created"""
    updated_at: Any
    """ISO 8601 timestamp when the product was last updated"""


class ProductsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the product"""
    title: str
    """Product title"""
    body_html: str
    """Product description in HTML"""
    vendor: str
    """Product vendor or manufacturer"""
    product_type: str
    """Product type used for categorization"""
    handle: str
    """URL-friendly handle for the product"""
    status: str
    """Product status (`active`, `archived`, or `draft`)"""
    tags: str
    """Comma-separated tags attached to the product"""
    published_scope: str
    """Publishing scope (`web` or `global`)"""
    published_at: str
    """ISO 8601 timestamp when the product was published"""
    created_at: str
    """ISO 8601 timestamp when the product was created"""
    updated_at: str
    """ISO 8601 timestamp when the product was last updated"""


class ProductsSortFilter(TypedDict, total=False):
    """Available fields for sorting products search results."""
    id: AirbyteSortOrder
    """Unique identifier for the product"""
    title: AirbyteSortOrder
    """Product title"""
    body_html: AirbyteSortOrder
    """Product description in HTML"""
    vendor: AirbyteSortOrder
    """Product vendor or manufacturer"""
    product_type: AirbyteSortOrder
    """Product type used for categorization"""
    handle: AirbyteSortOrder
    """URL-friendly handle for the product"""
    status: AirbyteSortOrder
    """Product status (`active`, `archived`, or `draft`)"""
    tags: AirbyteSortOrder
    """Comma-separated tags attached to the product"""
    published_scope: AirbyteSortOrder
    """Publishing scope (`web` or `global`)"""
    published_at: AirbyteSortOrder
    """ISO 8601 timestamp when the product was published"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the product was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the product was last updated"""


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


# ===== PRODUCT_VARIANTS SEARCH TYPES =====

class ProductVariantsSearchFilter(TypedDict, total=False):
    """Available fields for filtering product_variants search queries."""
    id: int | None
    """Unique identifier for the product variant"""
    product_id: int | None
    """Identifier of the parent product"""
    title: str | None
    """Display title of the variant"""
    sku: str | None
    """Stock keeping unit for the variant"""
    price: str | None
    """Price of the variant in the shop's currency"""
    compare_at_price: str | None
    """Original (compare-at) price of the variant, if set"""
    position: int | None
    """Display position of the variant within the product"""
    inventory_policy: str | None
    """Behaviour when out of stock (`deny` or `continue`)"""
    created_at: str | None
    """ISO 8601 timestamp when the variant was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the variant was last updated"""


class ProductVariantsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the product variant"""
    product_id: list[int]
    """Identifier of the parent product"""
    title: list[str]
    """Display title of the variant"""
    sku: list[str]
    """Stock keeping unit for the variant"""
    price: list[str]
    """Price of the variant in the shop's currency"""
    compare_at_price: list[str]
    """Original (compare-at) price of the variant, if set"""
    position: list[int]
    """Display position of the variant within the product"""
    inventory_policy: list[str]
    """Behaviour when out of stock (`deny` or `continue`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the variant was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the variant was last updated"""


class ProductVariantsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the product variant"""
    product_id: Any
    """Identifier of the parent product"""
    title: Any
    """Display title of the variant"""
    sku: Any
    """Stock keeping unit for the variant"""
    price: Any
    """Price of the variant in the shop's currency"""
    compare_at_price: Any
    """Original (compare-at) price of the variant, if set"""
    position: Any
    """Display position of the variant within the product"""
    inventory_policy: Any
    """Behaviour when out of stock (`deny` or `continue`)"""
    created_at: Any
    """ISO 8601 timestamp when the variant was created"""
    updated_at: Any
    """ISO 8601 timestamp when the variant was last updated"""


class ProductVariantsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the product variant"""
    product_id: str
    """Identifier of the parent product"""
    title: str
    """Display title of the variant"""
    sku: str
    """Stock keeping unit for the variant"""
    price: str
    """Price of the variant in the shop's currency"""
    compare_at_price: str
    """Original (compare-at) price of the variant, if set"""
    position: str
    """Display position of the variant within the product"""
    inventory_policy: str
    """Behaviour when out of stock (`deny` or `continue`)"""
    created_at: str
    """ISO 8601 timestamp when the variant was created"""
    updated_at: str
    """ISO 8601 timestamp when the variant was last updated"""


class ProductVariantsSortFilter(TypedDict, total=False):
    """Available fields for sorting product_variants search results."""
    id: AirbyteSortOrder
    """Unique identifier for the product variant"""
    product_id: AirbyteSortOrder
    """Identifier of the parent product"""
    title: AirbyteSortOrder
    """Display title of the variant"""
    sku: AirbyteSortOrder
    """Stock keeping unit for the variant"""
    price: AirbyteSortOrder
    """Price of the variant in the shop's currency"""
    compare_at_price: AirbyteSortOrder
    """Original (compare-at) price of the variant, if set"""
    position: AirbyteSortOrder
    """Display position of the variant within the product"""
    inventory_policy: AirbyteSortOrder
    """Behaviour when out of stock (`deny` or `continue`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the variant was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the variant was last updated"""


# Entity-specific condition types for product_variants
class ProductVariantsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProductVariantsSearchFilter


class ProductVariantsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProductVariantsSearchFilter


class ProductVariantsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProductVariantsSearchFilter


class ProductVariantsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProductVariantsSearchFilter


class ProductVariantsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProductVariantsSearchFilter


class ProductVariantsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProductVariantsSearchFilter


class ProductVariantsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProductVariantsStringFilter


class ProductVariantsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProductVariantsStringFilter


class ProductVariantsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProductVariantsStringFilter


class ProductVariantsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProductVariantsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProductVariantsInCondition = TypedDict("ProductVariantsInCondition", {"in": ProductVariantsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProductVariantsNotCondition = TypedDict("ProductVariantsNotCondition", {"not": "ProductVariantsCondition"}, total=False)
"""Negates the nested condition."""

ProductVariantsAndCondition = TypedDict("ProductVariantsAndCondition", {"and": "list[ProductVariantsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProductVariantsOrCondition = TypedDict("ProductVariantsOrCondition", {"or": "list[ProductVariantsCondition]"}, total=False)
"""True if any nested condition is true."""

ProductVariantsAnyCondition = TypedDict("ProductVariantsAnyCondition", {"any": ProductVariantsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all product_variants condition types
ProductVariantsCondition = (
    ProductVariantsEqCondition
    | ProductVariantsNeqCondition
    | ProductVariantsGtCondition
    | ProductVariantsGteCondition
    | ProductVariantsLtCondition
    | ProductVariantsLteCondition
    | ProductVariantsInCondition
    | ProductVariantsLikeCondition
    | ProductVariantsFuzzyCondition
    | ProductVariantsKeywordCondition
    | ProductVariantsContainsCondition
    | ProductVariantsNotCondition
    | ProductVariantsAndCondition
    | ProductVariantsOrCondition
    | ProductVariantsAnyCondition
)


class ProductVariantsSearchQuery(TypedDict, total=False):
    """Search query for product_variants entity."""
    filter: ProductVariantsCondition
    sort: list[ProductVariantsSortFilter]


# ===== SHOP SEARCH TYPES =====

class ShopSearchFilter(TypedDict, total=False):
    """Available fields for filtering shop search queries."""
    id: int | None
    """Unique identifier for the shop"""
    name: str | None
    """Display name of the shop"""
    email: str | None
    """Primary contact email for the shop"""
    domain: str | None
    """Custom domain configured for the shop, if any"""
    myshopify_domain: str | None
    """Canonical `*.myshopify.com` domain for the shop"""
    country_code: str | None
    """ISO 3166-1 alpha-2 country code of the shop"""
    currency: str | None
    """ISO 4217 currency code used by the shop"""
    timezone: str | None
    """Timezone configured for the shop (e.g. `(GMT-05:00) Eastern Time`)"""
    plan_name: str | None
    """Shopify plan identifier (e.g. `shopify_plus`, `basic`)"""
    created_at: str | None
    """ISO 8601 timestamp when the shop was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the shop was last updated"""


class ShopInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the shop"""
    name: list[str]
    """Display name of the shop"""
    email: list[str]
    """Primary contact email for the shop"""
    domain: list[str]
    """Custom domain configured for the shop, if any"""
    myshopify_domain: list[str]
    """Canonical `*.myshopify.com` domain for the shop"""
    country_code: list[str]
    """ISO 3166-1 alpha-2 country code of the shop"""
    currency: list[str]
    """ISO 4217 currency code used by the shop"""
    timezone: list[str]
    """Timezone configured for the shop (e.g. `(GMT-05:00) Eastern Time`)"""
    plan_name: list[str]
    """Shopify plan identifier (e.g. `shopify_plus`, `basic`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the shop was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the shop was last updated"""


class ShopAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the shop"""
    name: Any
    """Display name of the shop"""
    email: Any
    """Primary contact email for the shop"""
    domain: Any
    """Custom domain configured for the shop, if any"""
    myshopify_domain: Any
    """Canonical `*.myshopify.com` domain for the shop"""
    country_code: Any
    """ISO 3166-1 alpha-2 country code of the shop"""
    currency: Any
    """ISO 4217 currency code used by the shop"""
    timezone: Any
    """Timezone configured for the shop (e.g. `(GMT-05:00) Eastern Time`)"""
    plan_name: Any
    """Shopify plan identifier (e.g. `shopify_plus`, `basic`)"""
    created_at: Any
    """ISO 8601 timestamp when the shop was created"""
    updated_at: Any
    """ISO 8601 timestamp when the shop was last updated"""


class ShopStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the shop"""
    name: str
    """Display name of the shop"""
    email: str
    """Primary contact email for the shop"""
    domain: str
    """Custom domain configured for the shop, if any"""
    myshopify_domain: str
    """Canonical `*.myshopify.com` domain for the shop"""
    country_code: str
    """ISO 3166-1 alpha-2 country code of the shop"""
    currency: str
    """ISO 4217 currency code used by the shop"""
    timezone: str
    """Timezone configured for the shop (e.g. `(GMT-05:00) Eastern Time`)"""
    plan_name: str
    """Shopify plan identifier (e.g. `shopify_plus`, `basic`)"""
    created_at: str
    """ISO 8601 timestamp when the shop was created"""
    updated_at: str
    """ISO 8601 timestamp when the shop was last updated"""


class ShopSortFilter(TypedDict, total=False):
    """Available fields for sorting shop search results."""
    id: AirbyteSortOrder
    """Unique identifier for the shop"""
    name: AirbyteSortOrder
    """Display name of the shop"""
    email: AirbyteSortOrder
    """Primary contact email for the shop"""
    domain: AirbyteSortOrder
    """Custom domain configured for the shop, if any"""
    myshopify_domain: AirbyteSortOrder
    """Canonical `*.myshopify.com` domain for the shop"""
    country_code: AirbyteSortOrder
    """ISO 3166-1 alpha-2 country code of the shop"""
    currency: AirbyteSortOrder
    """ISO 4217 currency code used by the shop"""
    timezone: AirbyteSortOrder
    """Timezone configured for the shop (e.g. `(GMT-05:00) Eastern Time`)"""
    plan_name: AirbyteSortOrder
    """Shopify plan identifier (e.g. `shopify_plus`, `basic`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the shop was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the shop was last updated"""


# Entity-specific condition types for shop
class ShopEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ShopSearchFilter


class ShopNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ShopSearchFilter


class ShopGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ShopSearchFilter


class ShopGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ShopSearchFilter


class ShopLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ShopSearchFilter


class ShopLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ShopSearchFilter


class ShopLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ShopStringFilter


class ShopFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ShopStringFilter


class ShopKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ShopStringFilter


class ShopContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ShopAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ShopInCondition = TypedDict("ShopInCondition", {"in": ShopInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ShopNotCondition = TypedDict("ShopNotCondition", {"not": "ShopCondition"}, total=False)
"""Negates the nested condition."""

ShopAndCondition = TypedDict("ShopAndCondition", {"and": "list[ShopCondition]"}, total=False)
"""True if all nested conditions are true."""

ShopOrCondition = TypedDict("ShopOrCondition", {"or": "list[ShopCondition]"}, total=False)
"""True if any nested condition is true."""

ShopAnyCondition = TypedDict("ShopAnyCondition", {"any": ShopAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all shop condition types
ShopCondition = (
    ShopEqCondition
    | ShopNeqCondition
    | ShopGtCondition
    | ShopGteCondition
    | ShopLtCondition
    | ShopLteCondition
    | ShopInCondition
    | ShopLikeCondition
    | ShopFuzzyCondition
    | ShopKeywordCondition
    | ShopContainsCondition
    | ShopNotCondition
    | ShopAndCondition
    | ShopOrCondition
    | ShopAnyCondition
)


class ShopSearchQuery(TypedDict, total=False):
    """Search query for shop entity."""
    filter: ShopCondition
    sort: list[ShopSortFilter]


# ===== SMART_COLLECTIONS SEARCH TYPES =====

class SmartCollectionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering smart_collections search queries."""
    id: int | None
    """Unique identifier for the smart collection"""
    handle: str | None
    """URL-friendly handle for the smart collection"""
    title: str | None
    """Display title of the smart collection"""
    sort_order: str | None
    """How products are sorted within the collection"""
    published_scope: str | None
    """Publishing scope (`web` or `global`)"""
    published_at: str | None
    """ISO 8601 timestamp when the collection was published"""
    updated_at: str | None
    """ISO 8601 timestamp when the collection was last updated"""


class SmartCollectionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the smart collection"""
    handle: list[str]
    """URL-friendly handle for the smart collection"""
    title: list[str]
    """Display title of the smart collection"""
    sort_order: list[str]
    """How products are sorted within the collection"""
    published_scope: list[str]
    """Publishing scope (`web` or `global`)"""
    published_at: list[str]
    """ISO 8601 timestamp when the collection was published"""
    updated_at: list[str]
    """ISO 8601 timestamp when the collection was last updated"""


class SmartCollectionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the smart collection"""
    handle: Any
    """URL-friendly handle for the smart collection"""
    title: Any
    """Display title of the smart collection"""
    sort_order: Any
    """How products are sorted within the collection"""
    published_scope: Any
    """Publishing scope (`web` or `global`)"""
    published_at: Any
    """ISO 8601 timestamp when the collection was published"""
    updated_at: Any
    """ISO 8601 timestamp when the collection was last updated"""


class SmartCollectionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the smart collection"""
    handle: str
    """URL-friendly handle for the smart collection"""
    title: str
    """Display title of the smart collection"""
    sort_order: str
    """How products are sorted within the collection"""
    published_scope: str
    """Publishing scope (`web` or `global`)"""
    published_at: str
    """ISO 8601 timestamp when the collection was published"""
    updated_at: str
    """ISO 8601 timestamp when the collection was last updated"""


class SmartCollectionsSortFilter(TypedDict, total=False):
    """Available fields for sorting smart_collections search results."""
    id: AirbyteSortOrder
    """Unique identifier for the smart collection"""
    handle: AirbyteSortOrder
    """URL-friendly handle for the smart collection"""
    title: AirbyteSortOrder
    """Display title of the smart collection"""
    sort_order: AirbyteSortOrder
    """How products are sorted within the collection"""
    published_scope: AirbyteSortOrder
    """Publishing scope (`web` or `global`)"""
    published_at: AirbyteSortOrder
    """ISO 8601 timestamp when the collection was published"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the collection was last updated"""


# Entity-specific condition types for smart_collections
class SmartCollectionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SmartCollectionsSearchFilter


class SmartCollectionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SmartCollectionsSearchFilter


class SmartCollectionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SmartCollectionsSearchFilter


class SmartCollectionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SmartCollectionsSearchFilter


class SmartCollectionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SmartCollectionsSearchFilter


class SmartCollectionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SmartCollectionsSearchFilter


class SmartCollectionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SmartCollectionsStringFilter


class SmartCollectionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SmartCollectionsStringFilter


class SmartCollectionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SmartCollectionsStringFilter


class SmartCollectionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SmartCollectionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SmartCollectionsInCondition = TypedDict("SmartCollectionsInCondition", {"in": SmartCollectionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SmartCollectionsNotCondition = TypedDict("SmartCollectionsNotCondition", {"not": "SmartCollectionsCondition"}, total=False)
"""Negates the nested condition."""

SmartCollectionsAndCondition = TypedDict("SmartCollectionsAndCondition", {"and": "list[SmartCollectionsCondition]"}, total=False)
"""True if all nested conditions are true."""

SmartCollectionsOrCondition = TypedDict("SmartCollectionsOrCondition", {"or": "list[SmartCollectionsCondition]"}, total=False)
"""True if any nested condition is true."""

SmartCollectionsAnyCondition = TypedDict("SmartCollectionsAnyCondition", {"any": SmartCollectionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all smart_collections condition types
SmartCollectionsCondition = (
    SmartCollectionsEqCondition
    | SmartCollectionsNeqCondition
    | SmartCollectionsGtCondition
    | SmartCollectionsGteCondition
    | SmartCollectionsLtCondition
    | SmartCollectionsLteCondition
    | SmartCollectionsInCondition
    | SmartCollectionsLikeCondition
    | SmartCollectionsFuzzyCondition
    | SmartCollectionsKeywordCondition
    | SmartCollectionsContainsCondition
    | SmartCollectionsNotCondition
    | SmartCollectionsAndCondition
    | SmartCollectionsOrCondition
    | SmartCollectionsAnyCondition
)


class SmartCollectionsSearchQuery(TypedDict, total=False):
    """Search query for smart_collections entity."""
    filter: SmartCollectionsCondition
    sort: list[SmartCollectionsSortFilter]


# ===== TENDER_TRANSACTIONS SEARCH TYPES =====

class TenderTransactionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tender_transactions search queries."""
    id: int | None
    """Unique identifier for the tender transaction"""
    order_id: int | None
    """Identifier of the order the transaction belongs to"""
    user_id: int | None
    """Identifier of the staff user who processed the transaction"""
    amount: str | None
    """Amount of the transaction in the shop's currency"""
    currency: str | None
    """ISO 4217 currency code for the transaction amount"""
    payment_method: str | None
    """Payment method used (e.g. `credit_card`, `paypal`)"""
    test: bool | None
    """Whether the transaction was a test transaction"""
    processed_at: str | None
    """ISO 8601 timestamp when the transaction was processed"""


class TenderTransactionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the tender transaction"""
    order_id: list[int]
    """Identifier of the order the transaction belongs to"""
    user_id: list[int]
    """Identifier of the staff user who processed the transaction"""
    amount: list[str]
    """Amount of the transaction in the shop's currency"""
    currency: list[str]
    """ISO 4217 currency code for the transaction amount"""
    payment_method: list[str]
    """Payment method used (e.g. `credit_card`, `paypal`)"""
    test: list[bool]
    """Whether the transaction was a test transaction"""
    processed_at: list[str]
    """ISO 8601 timestamp when the transaction was processed"""


class TenderTransactionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the tender transaction"""
    order_id: Any
    """Identifier of the order the transaction belongs to"""
    user_id: Any
    """Identifier of the staff user who processed the transaction"""
    amount: Any
    """Amount of the transaction in the shop's currency"""
    currency: Any
    """ISO 4217 currency code for the transaction amount"""
    payment_method: Any
    """Payment method used (e.g. `credit_card`, `paypal`)"""
    test: Any
    """Whether the transaction was a test transaction"""
    processed_at: Any
    """ISO 8601 timestamp when the transaction was processed"""


class TenderTransactionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the tender transaction"""
    order_id: str
    """Identifier of the order the transaction belongs to"""
    user_id: str
    """Identifier of the staff user who processed the transaction"""
    amount: str
    """Amount of the transaction in the shop's currency"""
    currency: str
    """ISO 4217 currency code for the transaction amount"""
    payment_method: str
    """Payment method used (e.g. `credit_card`, `paypal`)"""
    test: str
    """Whether the transaction was a test transaction"""
    processed_at: str
    """ISO 8601 timestamp when the transaction was processed"""


class TenderTransactionsSortFilter(TypedDict, total=False):
    """Available fields for sorting tender_transactions search results."""
    id: AirbyteSortOrder
    """Unique identifier for the tender transaction"""
    order_id: AirbyteSortOrder
    """Identifier of the order the transaction belongs to"""
    user_id: AirbyteSortOrder
    """Identifier of the staff user who processed the transaction"""
    amount: AirbyteSortOrder
    """Amount of the transaction in the shop's currency"""
    currency: AirbyteSortOrder
    """ISO 4217 currency code for the transaction amount"""
    payment_method: AirbyteSortOrder
    """Payment method used (e.g. `credit_card`, `paypal`)"""
    test: AirbyteSortOrder
    """Whether the transaction was a test transaction"""
    processed_at: AirbyteSortOrder
    """ISO 8601 timestamp when the transaction was processed"""


# Entity-specific condition types for tender_transactions
class TenderTransactionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TenderTransactionsSearchFilter


class TenderTransactionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TenderTransactionsSearchFilter


class TenderTransactionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TenderTransactionsSearchFilter


class TenderTransactionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TenderTransactionsSearchFilter


class TenderTransactionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TenderTransactionsSearchFilter


class TenderTransactionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TenderTransactionsSearchFilter


class TenderTransactionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TenderTransactionsStringFilter


class TenderTransactionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TenderTransactionsStringFilter


class TenderTransactionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TenderTransactionsStringFilter


class TenderTransactionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TenderTransactionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TenderTransactionsInCondition = TypedDict("TenderTransactionsInCondition", {"in": TenderTransactionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TenderTransactionsNotCondition = TypedDict("TenderTransactionsNotCondition", {"not": "TenderTransactionsCondition"}, total=False)
"""Negates the nested condition."""

TenderTransactionsAndCondition = TypedDict("TenderTransactionsAndCondition", {"and": "list[TenderTransactionsCondition]"}, total=False)
"""True if all nested conditions are true."""

TenderTransactionsOrCondition = TypedDict("TenderTransactionsOrCondition", {"or": "list[TenderTransactionsCondition]"}, total=False)
"""True if any nested condition is true."""

TenderTransactionsAnyCondition = TypedDict("TenderTransactionsAnyCondition", {"any": TenderTransactionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tender_transactions condition types
TenderTransactionsCondition = (
    TenderTransactionsEqCondition
    | TenderTransactionsNeqCondition
    | TenderTransactionsGtCondition
    | TenderTransactionsGteCondition
    | TenderTransactionsLtCondition
    | TenderTransactionsLteCondition
    | TenderTransactionsInCondition
    | TenderTransactionsLikeCondition
    | TenderTransactionsFuzzyCondition
    | TenderTransactionsKeywordCondition
    | TenderTransactionsContainsCondition
    | TenderTransactionsNotCondition
    | TenderTransactionsAndCondition
    | TenderTransactionsOrCondition
    | TenderTransactionsAnyCondition
)


class TenderTransactionsSearchQuery(TypedDict, total=False):
    """Search query for tender_transactions entity."""
    filter: TenderTransactionsCondition
    sort: list[TenderTransactionsSortFilter]


# ===== PAGES SEARCH TYPES =====

class PagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering pages search queries."""
    id: int | None
    """Unique identifier for the page"""
    title: str | None
    """Title of the page"""
    handle: str | None
    """URL-friendly handle for the page"""
    author: str | None
    """Name of the page author"""
    body_html: str | None
    """HTML content of the page"""
    published_at: str | None
    """ISO 8601 timestamp when the page was published"""
    created_at: str | None
    """ISO 8601 timestamp when the page was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the page was last updated"""


class PagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the page"""
    title: list[str]
    """Title of the page"""
    handle: list[str]
    """URL-friendly handle for the page"""
    author: list[str]
    """Name of the page author"""
    body_html: list[str]
    """HTML content of the page"""
    published_at: list[str]
    """ISO 8601 timestamp when the page was published"""
    created_at: list[str]
    """ISO 8601 timestamp when the page was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the page was last updated"""


class PagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the page"""
    title: Any
    """Title of the page"""
    handle: Any
    """URL-friendly handle for the page"""
    author: Any
    """Name of the page author"""
    body_html: Any
    """HTML content of the page"""
    published_at: Any
    """ISO 8601 timestamp when the page was published"""
    created_at: Any
    """ISO 8601 timestamp when the page was created"""
    updated_at: Any
    """ISO 8601 timestamp when the page was last updated"""


class PagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the page"""
    title: str
    """Title of the page"""
    handle: str
    """URL-friendly handle for the page"""
    author: str
    """Name of the page author"""
    body_html: str
    """HTML content of the page"""
    published_at: str
    """ISO 8601 timestamp when the page was published"""
    created_at: str
    """ISO 8601 timestamp when the page was created"""
    updated_at: str
    """ISO 8601 timestamp when the page was last updated"""


class PagesSortFilter(TypedDict, total=False):
    """Available fields for sorting pages search results."""
    id: AirbyteSortOrder
    """Unique identifier for the page"""
    title: AirbyteSortOrder
    """Title of the page"""
    handle: AirbyteSortOrder
    """URL-friendly handle for the page"""
    author: AirbyteSortOrder
    """Name of the page author"""
    body_html: AirbyteSortOrder
    """HTML content of the page"""
    published_at: AirbyteSortOrder
    """ISO 8601 timestamp when the page was published"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the page was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the page was last updated"""


# Entity-specific condition types for pages
class PagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PagesSearchFilter


class PagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PagesSearchFilter


class PagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PagesSearchFilter


class PagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PagesSearchFilter


class PagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PagesSearchFilter


class PagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PagesSearchFilter


class PagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PagesStringFilter


class PagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PagesStringFilter


class PagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PagesStringFilter


class PagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PagesInCondition = TypedDict("PagesInCondition", {"in": PagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PagesNotCondition = TypedDict("PagesNotCondition", {"not": "PagesCondition"}, total=False)
"""Negates the nested condition."""

PagesAndCondition = TypedDict("PagesAndCondition", {"and": "list[PagesCondition]"}, total=False)
"""True if all nested conditions are true."""

PagesOrCondition = TypedDict("PagesOrCondition", {"or": "list[PagesCondition]"}, total=False)
"""True if any nested condition is true."""

PagesAnyCondition = TypedDict("PagesAnyCondition", {"any": PagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all pages condition types
PagesCondition = (
    PagesEqCondition
    | PagesNeqCondition
    | PagesGtCondition
    | PagesGteCondition
    | PagesLtCondition
    | PagesLteCondition
    | PagesInCondition
    | PagesLikeCondition
    | PagesFuzzyCondition
    | PagesKeywordCondition
    | PagesContainsCondition
    | PagesNotCondition
    | PagesAndCondition
    | PagesOrCondition
    | PagesAnyCondition
)


class PagesSearchQuery(TypedDict, total=False):
    """Search query for pages entity."""
    filter: PagesCondition
    sort: list[PagesSortFilter]


# ===== BLOGS SEARCH TYPES =====

class BlogsSearchFilter(TypedDict, total=False):
    """Available fields for filtering blogs search queries."""
    id: int | None
    """Unique identifier for the blog"""
    title: str | None
    """Title of the blog"""
    handle: str | None
    """URL-friendly handle for the blog"""
    commentable: str | None
    """Whether readers can post comments (no, moderate, yes)"""
    tags: str | None
    """Comma-separated tags from the blog's articles"""
    created_at: str | None
    """ISO 8601 timestamp when the blog was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the blog was last updated"""


class BlogsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the blog"""
    title: list[str]
    """Title of the blog"""
    handle: list[str]
    """URL-friendly handle for the blog"""
    commentable: list[str]
    """Whether readers can post comments (no, moderate, yes)"""
    tags: list[str]
    """Comma-separated tags from the blog's articles"""
    created_at: list[str]
    """ISO 8601 timestamp when the blog was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the blog was last updated"""


class BlogsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the blog"""
    title: Any
    """Title of the blog"""
    handle: Any
    """URL-friendly handle for the blog"""
    commentable: Any
    """Whether readers can post comments (no, moderate, yes)"""
    tags: Any
    """Comma-separated tags from the blog's articles"""
    created_at: Any
    """ISO 8601 timestamp when the blog was created"""
    updated_at: Any
    """ISO 8601 timestamp when the blog was last updated"""


class BlogsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the blog"""
    title: str
    """Title of the blog"""
    handle: str
    """URL-friendly handle for the blog"""
    commentable: str
    """Whether readers can post comments (no, moderate, yes)"""
    tags: str
    """Comma-separated tags from the blog's articles"""
    created_at: str
    """ISO 8601 timestamp when the blog was created"""
    updated_at: str
    """ISO 8601 timestamp when the blog was last updated"""


class BlogsSortFilter(TypedDict, total=False):
    """Available fields for sorting blogs search results."""
    id: AirbyteSortOrder
    """Unique identifier for the blog"""
    title: AirbyteSortOrder
    """Title of the blog"""
    handle: AirbyteSortOrder
    """URL-friendly handle for the blog"""
    commentable: AirbyteSortOrder
    """Whether readers can post comments (no, moderate, yes)"""
    tags: AirbyteSortOrder
    """Comma-separated tags from the blog's articles"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the blog was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the blog was last updated"""


# Entity-specific condition types for blogs
class BlogsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BlogsSearchFilter


class BlogsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BlogsSearchFilter


class BlogsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BlogsSearchFilter


class BlogsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BlogsSearchFilter


class BlogsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BlogsSearchFilter


class BlogsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BlogsSearchFilter


class BlogsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BlogsStringFilter


class BlogsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BlogsStringFilter


class BlogsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BlogsStringFilter


class BlogsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BlogsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BlogsInCondition = TypedDict("BlogsInCondition", {"in": BlogsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BlogsNotCondition = TypedDict("BlogsNotCondition", {"not": "BlogsCondition"}, total=False)
"""Negates the nested condition."""

BlogsAndCondition = TypedDict("BlogsAndCondition", {"and": "list[BlogsCondition]"}, total=False)
"""True if all nested conditions are true."""

BlogsOrCondition = TypedDict("BlogsOrCondition", {"or": "list[BlogsCondition]"}, total=False)
"""True if any nested condition is true."""

BlogsAnyCondition = TypedDict("BlogsAnyCondition", {"any": BlogsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all blogs condition types
BlogsCondition = (
    BlogsEqCondition
    | BlogsNeqCondition
    | BlogsGtCondition
    | BlogsGteCondition
    | BlogsLtCondition
    | BlogsLteCondition
    | BlogsInCondition
    | BlogsLikeCondition
    | BlogsFuzzyCondition
    | BlogsKeywordCondition
    | BlogsContainsCondition
    | BlogsNotCondition
    | BlogsAndCondition
    | BlogsOrCondition
    | BlogsAnyCondition
)


class BlogsSearchQuery(TypedDict, total=False):
    """Search query for blogs entity."""
    filter: BlogsCondition
    sort: list[BlogsSortFilter]


# ===== ARTICLES SEARCH TYPES =====

class ArticlesSearchFilter(TypedDict, total=False):
    """Available fields for filtering articles search queries."""
    id: int | None
    """Unique identifier for the article"""
    title: str | None
    """Title of the article"""
    handle: str | None
    """URL-friendly handle for the article"""
    author: str | None
    """Name of the author of the article"""
    blog_id: int | None
    """Identifier of the blog the article belongs to"""
    body_html: str | None
    """HTML content of the article body"""
    summary_html: str | None
    """Summary of the article in HTML"""
    tags: str | None
    """Comma-separated list of tags for the article"""
    published_at: str | None
    """ISO 8601 timestamp when the article was published"""
    created_at: str | None
    """ISO 8601 timestamp when the article was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the article was last updated"""


class ArticlesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the article"""
    title: list[str]
    """Title of the article"""
    handle: list[str]
    """URL-friendly handle for the article"""
    author: list[str]
    """Name of the author of the article"""
    blog_id: list[int]
    """Identifier of the blog the article belongs to"""
    body_html: list[str]
    """HTML content of the article body"""
    summary_html: list[str]
    """Summary of the article in HTML"""
    tags: list[str]
    """Comma-separated list of tags for the article"""
    published_at: list[str]
    """ISO 8601 timestamp when the article was published"""
    created_at: list[str]
    """ISO 8601 timestamp when the article was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the article was last updated"""


class ArticlesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the article"""
    title: Any
    """Title of the article"""
    handle: Any
    """URL-friendly handle for the article"""
    author: Any
    """Name of the author of the article"""
    blog_id: Any
    """Identifier of the blog the article belongs to"""
    body_html: Any
    """HTML content of the article body"""
    summary_html: Any
    """Summary of the article in HTML"""
    tags: Any
    """Comma-separated list of tags for the article"""
    published_at: Any
    """ISO 8601 timestamp when the article was published"""
    created_at: Any
    """ISO 8601 timestamp when the article was created"""
    updated_at: Any
    """ISO 8601 timestamp when the article was last updated"""


class ArticlesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the article"""
    title: str
    """Title of the article"""
    handle: str
    """URL-friendly handle for the article"""
    author: str
    """Name of the author of the article"""
    blog_id: str
    """Identifier of the blog the article belongs to"""
    body_html: str
    """HTML content of the article body"""
    summary_html: str
    """Summary of the article in HTML"""
    tags: str
    """Comma-separated list of tags for the article"""
    published_at: str
    """ISO 8601 timestamp when the article was published"""
    created_at: str
    """ISO 8601 timestamp when the article was created"""
    updated_at: str
    """ISO 8601 timestamp when the article was last updated"""


class ArticlesSortFilter(TypedDict, total=False):
    """Available fields for sorting articles search results."""
    id: AirbyteSortOrder
    """Unique identifier for the article"""
    title: AirbyteSortOrder
    """Title of the article"""
    handle: AirbyteSortOrder
    """URL-friendly handle for the article"""
    author: AirbyteSortOrder
    """Name of the author of the article"""
    blog_id: AirbyteSortOrder
    """Identifier of the blog the article belongs to"""
    body_html: AirbyteSortOrder
    """HTML content of the article body"""
    summary_html: AirbyteSortOrder
    """Summary of the article in HTML"""
    tags: AirbyteSortOrder
    """Comma-separated list of tags for the article"""
    published_at: AirbyteSortOrder
    """ISO 8601 timestamp when the article was published"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the article was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the article was last updated"""


# Entity-specific condition types for articles
class ArticlesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ArticlesSearchFilter


class ArticlesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ArticlesSearchFilter


class ArticlesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ArticlesSearchFilter


class ArticlesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ArticlesSearchFilter


class ArticlesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ArticlesSearchFilter


class ArticlesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ArticlesSearchFilter


class ArticlesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ArticlesStringFilter


class ArticlesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ArticlesStringFilter


class ArticlesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ArticlesStringFilter


class ArticlesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ArticlesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ArticlesInCondition = TypedDict("ArticlesInCondition", {"in": ArticlesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ArticlesNotCondition = TypedDict("ArticlesNotCondition", {"not": "ArticlesCondition"}, total=False)
"""Negates the nested condition."""

ArticlesAndCondition = TypedDict("ArticlesAndCondition", {"and": "list[ArticlesCondition]"}, total=False)
"""True if all nested conditions are true."""

ArticlesOrCondition = TypedDict("ArticlesOrCondition", {"or": "list[ArticlesCondition]"}, total=False)
"""True if any nested condition is true."""

ArticlesAnyCondition = TypedDict("ArticlesAnyCondition", {"any": ArticlesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all articles condition types
ArticlesCondition = (
    ArticlesEqCondition
    | ArticlesNeqCondition
    | ArticlesGtCondition
    | ArticlesGteCondition
    | ArticlesLtCondition
    | ArticlesLteCondition
    | ArticlesInCondition
    | ArticlesLikeCondition
    | ArticlesFuzzyCondition
    | ArticlesKeywordCondition
    | ArticlesContainsCondition
    | ArticlesNotCondition
    | ArticlesAndCondition
    | ArticlesOrCondition
    | ArticlesAnyCondition
)


class ArticlesSearchQuery(TypedDict, total=False):
    """Search query for articles entity."""
    filter: ArticlesCondition
    sort: list[ArticlesSortFilter]


# ===== BALANCE_TRANSACTIONS SEARCH TYPES =====

class BalanceTransactionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering balance_transactions search queries."""
    id: int | None
    """Unique identifier of the balance transaction"""
    type_: str | None
    """Type of the transaction (charge, refund, dispute, reserve, adjustment, credit, debit, payout, etc.)"""
    amount: str | None
    """Gross amount of the transaction"""
    fee: str | None
    """Total fees deducted from the transaction"""
    net: str | None
    """Net amount of the transaction"""
    currency: str | None
    """ISO 4217 currency code of the transaction"""
    payout_id: int | None
    """Identifier of the payout the transaction was paid out in"""
    payout_status: str | None
    """Status of the associated payout"""
    source_type: str | None
    """Type of the resource that led to this transaction"""
    source_order_id: int | None
    """Identifier of the source order, if applicable"""
    processed_at: str | None
    """ISO 8601 timestamp when the transaction was processed"""


class BalanceTransactionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier of the balance transaction"""
    type_: list[str]
    """Type of the transaction (charge, refund, dispute, reserve, adjustment, credit, debit, payout, etc.)"""
    amount: list[str]
    """Gross amount of the transaction"""
    fee: list[str]
    """Total fees deducted from the transaction"""
    net: list[str]
    """Net amount of the transaction"""
    currency: list[str]
    """ISO 4217 currency code of the transaction"""
    payout_id: list[int]
    """Identifier of the payout the transaction was paid out in"""
    payout_status: list[str]
    """Status of the associated payout"""
    source_type: list[str]
    """Type of the resource that led to this transaction"""
    source_order_id: list[int]
    """Identifier of the source order, if applicable"""
    processed_at: list[str]
    """ISO 8601 timestamp when the transaction was processed"""


class BalanceTransactionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier of the balance transaction"""
    type_: Any
    """Type of the transaction (charge, refund, dispute, reserve, adjustment, credit, debit, payout, etc.)"""
    amount: Any
    """Gross amount of the transaction"""
    fee: Any
    """Total fees deducted from the transaction"""
    net: Any
    """Net amount of the transaction"""
    currency: Any
    """ISO 4217 currency code of the transaction"""
    payout_id: Any
    """Identifier of the payout the transaction was paid out in"""
    payout_status: Any
    """Status of the associated payout"""
    source_type: Any
    """Type of the resource that led to this transaction"""
    source_order_id: Any
    """Identifier of the source order, if applicable"""
    processed_at: Any
    """ISO 8601 timestamp when the transaction was processed"""


class BalanceTransactionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier of the balance transaction"""
    type_: str
    """Type of the transaction (charge, refund, dispute, reserve, adjustment, credit, debit, payout, etc.)"""
    amount: str
    """Gross amount of the transaction"""
    fee: str
    """Total fees deducted from the transaction"""
    net: str
    """Net amount of the transaction"""
    currency: str
    """ISO 4217 currency code of the transaction"""
    payout_id: str
    """Identifier of the payout the transaction was paid out in"""
    payout_status: str
    """Status of the associated payout"""
    source_type: str
    """Type of the resource that led to this transaction"""
    source_order_id: str
    """Identifier of the source order, if applicable"""
    processed_at: str
    """ISO 8601 timestamp when the transaction was processed"""


class BalanceTransactionsSortFilter(TypedDict, total=False):
    """Available fields for sorting balance_transactions search results."""
    id: AirbyteSortOrder
    """Unique identifier of the balance transaction"""
    type_: AirbyteSortOrder
    """Type of the transaction (charge, refund, dispute, reserve, adjustment, credit, debit, payout, etc.)"""
    amount: AirbyteSortOrder
    """Gross amount of the transaction"""
    fee: AirbyteSortOrder
    """Total fees deducted from the transaction"""
    net: AirbyteSortOrder
    """Net amount of the transaction"""
    currency: AirbyteSortOrder
    """ISO 4217 currency code of the transaction"""
    payout_id: AirbyteSortOrder
    """Identifier of the payout the transaction was paid out in"""
    payout_status: AirbyteSortOrder
    """Status of the associated payout"""
    source_type: AirbyteSortOrder
    """Type of the resource that led to this transaction"""
    source_order_id: AirbyteSortOrder
    """Identifier of the source order, if applicable"""
    processed_at: AirbyteSortOrder
    """ISO 8601 timestamp when the transaction was processed"""


# Entity-specific condition types for balance_transactions
class BalanceTransactionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BalanceTransactionsSearchFilter


class BalanceTransactionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BalanceTransactionsSearchFilter


class BalanceTransactionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BalanceTransactionsSearchFilter


class BalanceTransactionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BalanceTransactionsSearchFilter


class BalanceTransactionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BalanceTransactionsSearchFilter


class BalanceTransactionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BalanceTransactionsSearchFilter


class BalanceTransactionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BalanceTransactionsStringFilter


class BalanceTransactionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BalanceTransactionsStringFilter


class BalanceTransactionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BalanceTransactionsStringFilter


class BalanceTransactionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BalanceTransactionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BalanceTransactionsInCondition = TypedDict("BalanceTransactionsInCondition", {"in": BalanceTransactionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BalanceTransactionsNotCondition = TypedDict("BalanceTransactionsNotCondition", {"not": "BalanceTransactionsCondition"}, total=False)
"""Negates the nested condition."""

BalanceTransactionsAndCondition = TypedDict("BalanceTransactionsAndCondition", {"and": "list[BalanceTransactionsCondition]"}, total=False)
"""True if all nested conditions are true."""

BalanceTransactionsOrCondition = TypedDict("BalanceTransactionsOrCondition", {"or": "list[BalanceTransactionsCondition]"}, total=False)
"""True if any nested condition is true."""

BalanceTransactionsAnyCondition = TypedDict("BalanceTransactionsAnyCondition", {"any": BalanceTransactionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all balance_transactions condition types
BalanceTransactionsCondition = (
    BalanceTransactionsEqCondition
    | BalanceTransactionsNeqCondition
    | BalanceTransactionsGtCondition
    | BalanceTransactionsGteCondition
    | BalanceTransactionsLtCondition
    | BalanceTransactionsLteCondition
    | BalanceTransactionsInCondition
    | BalanceTransactionsLikeCondition
    | BalanceTransactionsFuzzyCondition
    | BalanceTransactionsKeywordCondition
    | BalanceTransactionsContainsCondition
    | BalanceTransactionsNotCondition
    | BalanceTransactionsAndCondition
    | BalanceTransactionsOrCondition
    | BalanceTransactionsAnyCondition
)


class BalanceTransactionsSearchQuery(TypedDict, total=False):
    """Search query for balance_transactions entity."""
    filter: BalanceTransactionsCondition
    sort: list[BalanceTransactionsSortFilter]


# ===== DISPUTES SEARCH TYPES =====

class DisputesSearchFilter(TypedDict, total=False):
    """Available fields for filtering disputes search queries."""
    id: int | None
    """Unique identifier for the dispute"""
    order_id: int | None
    """Identifier of the order the dispute belongs to"""
    type_: str | None
    """Whether the dispute is an inquiry or chargeback"""
    amount: str | None
    """Disputed amount"""
    currency: str | None
    """ISO 4217 currency code of the dispute amount"""
    reason: str | None
    """Reason for the dispute provided by the cardholder's bank"""
    network_reason_code: str | None
    """Network reason code from the cardholder's bank"""
    status: str | None
    """Current state of the dispute (needs_response, under_review, charge_refunded, accepted, won, lost)"""
    evidence_due_by: str | None
    """ISO 8601 deadline for evidence submission"""
    initiated_at: str | None
    """ISO 8601 timestamp when the dispute was initiated"""
    finalized_on: str | None
    """ISO 8601 timestamp when the dispute was resolved"""


class DisputesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the dispute"""
    order_id: list[int]
    """Identifier of the order the dispute belongs to"""
    type_: list[str]
    """Whether the dispute is an inquiry or chargeback"""
    amount: list[str]
    """Disputed amount"""
    currency: list[str]
    """ISO 4217 currency code of the dispute amount"""
    reason: list[str]
    """Reason for the dispute provided by the cardholder's bank"""
    network_reason_code: list[str]
    """Network reason code from the cardholder's bank"""
    status: list[str]
    """Current state of the dispute (needs_response, under_review, charge_refunded, accepted, won, lost)"""
    evidence_due_by: list[str]
    """ISO 8601 deadline for evidence submission"""
    initiated_at: list[str]
    """ISO 8601 timestamp when the dispute was initiated"""
    finalized_on: list[str]
    """ISO 8601 timestamp when the dispute was resolved"""


class DisputesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the dispute"""
    order_id: Any
    """Identifier of the order the dispute belongs to"""
    type_: Any
    """Whether the dispute is an inquiry or chargeback"""
    amount: Any
    """Disputed amount"""
    currency: Any
    """ISO 4217 currency code of the dispute amount"""
    reason: Any
    """Reason for the dispute provided by the cardholder's bank"""
    network_reason_code: Any
    """Network reason code from the cardholder's bank"""
    status: Any
    """Current state of the dispute (needs_response, under_review, charge_refunded, accepted, won, lost)"""
    evidence_due_by: Any
    """ISO 8601 deadline for evidence submission"""
    initiated_at: Any
    """ISO 8601 timestamp when the dispute was initiated"""
    finalized_on: Any
    """ISO 8601 timestamp when the dispute was resolved"""


class DisputesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the dispute"""
    order_id: str
    """Identifier of the order the dispute belongs to"""
    type_: str
    """Whether the dispute is an inquiry or chargeback"""
    amount: str
    """Disputed amount"""
    currency: str
    """ISO 4217 currency code of the dispute amount"""
    reason: str
    """Reason for the dispute provided by the cardholder's bank"""
    network_reason_code: str
    """Network reason code from the cardholder's bank"""
    status: str
    """Current state of the dispute (needs_response, under_review, charge_refunded, accepted, won, lost)"""
    evidence_due_by: str
    """ISO 8601 deadline for evidence submission"""
    initiated_at: str
    """ISO 8601 timestamp when the dispute was initiated"""
    finalized_on: str
    """ISO 8601 timestamp when the dispute was resolved"""


class DisputesSortFilter(TypedDict, total=False):
    """Available fields for sorting disputes search results."""
    id: AirbyteSortOrder
    """Unique identifier for the dispute"""
    order_id: AirbyteSortOrder
    """Identifier of the order the dispute belongs to"""
    type_: AirbyteSortOrder
    """Whether the dispute is an inquiry or chargeback"""
    amount: AirbyteSortOrder
    """Disputed amount"""
    currency: AirbyteSortOrder
    """ISO 4217 currency code of the dispute amount"""
    reason: AirbyteSortOrder
    """Reason for the dispute provided by the cardholder's bank"""
    network_reason_code: AirbyteSortOrder
    """Network reason code from the cardholder's bank"""
    status: AirbyteSortOrder
    """Current state of the dispute (needs_response, under_review, charge_refunded, accepted, won, lost)"""
    evidence_due_by: AirbyteSortOrder
    """ISO 8601 deadline for evidence submission"""
    initiated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the dispute was initiated"""
    finalized_on: AirbyteSortOrder
    """ISO 8601 timestamp when the dispute was resolved"""


# Entity-specific condition types for disputes
class DisputesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DisputesSearchFilter


class DisputesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DisputesSearchFilter


class DisputesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DisputesSearchFilter


class DisputesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DisputesSearchFilter


class DisputesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DisputesSearchFilter


class DisputesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DisputesSearchFilter


class DisputesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DisputesStringFilter


class DisputesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DisputesStringFilter


class DisputesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DisputesStringFilter


class DisputesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DisputesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DisputesInCondition = TypedDict("DisputesInCondition", {"in": DisputesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DisputesNotCondition = TypedDict("DisputesNotCondition", {"not": "DisputesCondition"}, total=False)
"""Negates the nested condition."""

DisputesAndCondition = TypedDict("DisputesAndCondition", {"and": "list[DisputesCondition]"}, total=False)
"""True if all nested conditions are true."""

DisputesOrCondition = TypedDict("DisputesOrCondition", {"or": "list[DisputesCondition]"}, total=False)
"""True if any nested condition is true."""

DisputesAnyCondition = TypedDict("DisputesAnyCondition", {"any": DisputesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all disputes condition types
DisputesCondition = (
    DisputesEqCondition
    | DisputesNeqCondition
    | DisputesGtCondition
    | DisputesGteCondition
    | DisputesLtCondition
    | DisputesLteCondition
    | DisputesInCondition
    | DisputesLikeCondition
    | DisputesFuzzyCondition
    | DisputesKeywordCondition
    | DisputesContainsCondition
    | DisputesNotCondition
    | DisputesAndCondition
    | DisputesOrCondition
    | DisputesAnyCondition
)


class DisputesSearchQuery(TypedDict, total=False):
    """Search query for disputes entity."""
    filter: DisputesCondition
    sort: list[DisputesSortFilter]


# ===== METAFIELD_PAGES SEARCH TYPES =====

class MetafieldPagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_pages search queries."""
    id: int | None
    """Unique identifier for the metafield"""
    namespace: str | None
    """Container namespace for the metafield"""
    key: str | None
    """Identifier key for the metafield"""
    value: str | None
    """The metafield value"""
    type_: str | None
    """The metafield's information type"""
    description: str | None
    """Human-readable description of the metafield"""
    owner_id: int | None
    """Identifier of the page that owns this metafield"""
    owner_resource: str | None
    """Resource type that owns this metafield (e.g. `page`)"""
    created_at: str | None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldPagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the metafield"""
    namespace: list[str]
    """Container namespace for the metafield"""
    key: list[str]
    """Identifier key for the metafield"""
    value: list[str]
    """The metafield value"""
    type_: list[str]
    """The metafield's information type"""
    description: list[str]
    """Human-readable description of the metafield"""
    owner_id: list[int]
    """Identifier of the page that owns this metafield"""
    owner_resource: list[str]
    """Resource type that owns this metafield (e.g. `page`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldPagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the metafield"""
    namespace: Any
    """Container namespace for the metafield"""
    key: Any
    """Identifier key for the metafield"""
    value: Any
    """The metafield value"""
    type_: Any
    """The metafield's information type"""
    description: Any
    """Human-readable description of the metafield"""
    owner_id: Any
    """Identifier of the page that owns this metafield"""
    owner_resource: Any
    """Resource type that owns this metafield (e.g. `page`)"""
    created_at: Any
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: Any
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldPagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the metafield"""
    namespace: str
    """Container namespace for the metafield"""
    key: str
    """Identifier key for the metafield"""
    value: str
    """The metafield value"""
    type_: str
    """The metafield's information type"""
    description: str
    """Human-readable description of the metafield"""
    owner_id: str
    """Identifier of the page that owns this metafield"""
    owner_resource: str
    """Resource type that owns this metafield (e.g. `page`)"""
    created_at: str
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldPagesSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_pages search results."""
    id: AirbyteSortOrder
    """Unique identifier for the metafield"""
    namespace: AirbyteSortOrder
    """Container namespace for the metafield"""
    key: AirbyteSortOrder
    """Identifier key for the metafield"""
    value: AirbyteSortOrder
    """The metafield value"""
    type_: AirbyteSortOrder
    """The metafield's information type"""
    description: AirbyteSortOrder
    """Human-readable description of the metafield"""
    owner_id: AirbyteSortOrder
    """Identifier of the page that owns this metafield"""
    owner_resource: AirbyteSortOrder
    """Resource type that owns this metafield (e.g. `page`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was last updated"""


# Entity-specific condition types for metafield_pages
class MetafieldPagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldPagesSearchFilter


class MetafieldPagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldPagesSearchFilter


class MetafieldPagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldPagesSearchFilter


class MetafieldPagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldPagesSearchFilter


class MetafieldPagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldPagesSearchFilter


class MetafieldPagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldPagesSearchFilter


class MetafieldPagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldPagesStringFilter


class MetafieldPagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldPagesStringFilter


class MetafieldPagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldPagesStringFilter


class MetafieldPagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldPagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldPagesInCondition = TypedDict("MetafieldPagesInCondition", {"in": MetafieldPagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldPagesNotCondition = TypedDict("MetafieldPagesNotCondition", {"not": "MetafieldPagesCondition"}, total=False)
"""Negates the nested condition."""

MetafieldPagesAndCondition = TypedDict("MetafieldPagesAndCondition", {"and": "list[MetafieldPagesCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldPagesOrCondition = TypedDict("MetafieldPagesOrCondition", {"or": "list[MetafieldPagesCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldPagesAnyCondition = TypedDict("MetafieldPagesAnyCondition", {"any": MetafieldPagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_pages condition types
MetafieldPagesCondition = (
    MetafieldPagesEqCondition
    | MetafieldPagesNeqCondition
    | MetafieldPagesGtCondition
    | MetafieldPagesGteCondition
    | MetafieldPagesLtCondition
    | MetafieldPagesLteCondition
    | MetafieldPagesInCondition
    | MetafieldPagesLikeCondition
    | MetafieldPagesFuzzyCondition
    | MetafieldPagesKeywordCondition
    | MetafieldPagesContainsCondition
    | MetafieldPagesNotCondition
    | MetafieldPagesAndCondition
    | MetafieldPagesOrCondition
    | MetafieldPagesAnyCondition
)


class MetafieldPagesSearchQuery(TypedDict, total=False):
    """Search query for metafield_pages entity."""
    filter: MetafieldPagesCondition
    sort: list[MetafieldPagesSortFilter]


# ===== METAFIELD_BLOGS SEARCH TYPES =====

class MetafieldBlogsSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_blogs search queries."""
    id: int | None
    """Unique identifier for the metafield"""
    namespace: str | None
    """Container namespace for the metafield"""
    key: str | None
    """Identifier key for the metafield"""
    value: str | None
    """The metafield value"""
    type_: str | None
    """The metafield's information type"""
    description: str | None
    """Human-readable description of the metafield"""
    owner_id: int | None
    """Identifier of the blog that owns this metafield"""
    owner_resource: str | None
    """Resource type that owns this metafield (e.g. `blog`)"""
    created_at: str | None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldBlogsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the metafield"""
    namespace: list[str]
    """Container namespace for the metafield"""
    key: list[str]
    """Identifier key for the metafield"""
    value: list[str]
    """The metafield value"""
    type_: list[str]
    """The metafield's information type"""
    description: list[str]
    """Human-readable description of the metafield"""
    owner_id: list[int]
    """Identifier of the blog that owns this metafield"""
    owner_resource: list[str]
    """Resource type that owns this metafield (e.g. `blog`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldBlogsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the metafield"""
    namespace: Any
    """Container namespace for the metafield"""
    key: Any
    """Identifier key for the metafield"""
    value: Any
    """The metafield value"""
    type_: Any
    """The metafield's information type"""
    description: Any
    """Human-readable description of the metafield"""
    owner_id: Any
    """Identifier of the blog that owns this metafield"""
    owner_resource: Any
    """Resource type that owns this metafield (e.g. `blog`)"""
    created_at: Any
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: Any
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldBlogsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the metafield"""
    namespace: str
    """Container namespace for the metafield"""
    key: str
    """Identifier key for the metafield"""
    value: str
    """The metafield value"""
    type_: str
    """The metafield's information type"""
    description: str
    """Human-readable description of the metafield"""
    owner_id: str
    """Identifier of the blog that owns this metafield"""
    owner_resource: str
    """Resource type that owns this metafield (e.g. `blog`)"""
    created_at: str
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldBlogsSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_blogs search results."""
    id: AirbyteSortOrder
    """Unique identifier for the metafield"""
    namespace: AirbyteSortOrder
    """Container namespace for the metafield"""
    key: AirbyteSortOrder
    """Identifier key for the metafield"""
    value: AirbyteSortOrder
    """The metafield value"""
    type_: AirbyteSortOrder
    """The metafield's information type"""
    description: AirbyteSortOrder
    """Human-readable description of the metafield"""
    owner_id: AirbyteSortOrder
    """Identifier of the blog that owns this metafield"""
    owner_resource: AirbyteSortOrder
    """Resource type that owns this metafield (e.g. `blog`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was last updated"""


# Entity-specific condition types for metafield_blogs
class MetafieldBlogsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldBlogsSearchFilter


class MetafieldBlogsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldBlogsSearchFilter


class MetafieldBlogsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldBlogsSearchFilter


class MetafieldBlogsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldBlogsSearchFilter


class MetafieldBlogsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldBlogsSearchFilter


class MetafieldBlogsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldBlogsSearchFilter


class MetafieldBlogsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldBlogsStringFilter


class MetafieldBlogsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldBlogsStringFilter


class MetafieldBlogsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldBlogsStringFilter


class MetafieldBlogsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldBlogsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldBlogsInCondition = TypedDict("MetafieldBlogsInCondition", {"in": MetafieldBlogsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldBlogsNotCondition = TypedDict("MetafieldBlogsNotCondition", {"not": "MetafieldBlogsCondition"}, total=False)
"""Negates the nested condition."""

MetafieldBlogsAndCondition = TypedDict("MetafieldBlogsAndCondition", {"and": "list[MetafieldBlogsCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldBlogsOrCondition = TypedDict("MetafieldBlogsOrCondition", {"or": "list[MetafieldBlogsCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldBlogsAnyCondition = TypedDict("MetafieldBlogsAnyCondition", {"any": MetafieldBlogsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_blogs condition types
MetafieldBlogsCondition = (
    MetafieldBlogsEqCondition
    | MetafieldBlogsNeqCondition
    | MetafieldBlogsGtCondition
    | MetafieldBlogsGteCondition
    | MetafieldBlogsLtCondition
    | MetafieldBlogsLteCondition
    | MetafieldBlogsInCondition
    | MetafieldBlogsLikeCondition
    | MetafieldBlogsFuzzyCondition
    | MetafieldBlogsKeywordCondition
    | MetafieldBlogsContainsCondition
    | MetafieldBlogsNotCondition
    | MetafieldBlogsAndCondition
    | MetafieldBlogsOrCondition
    | MetafieldBlogsAnyCondition
)


class MetafieldBlogsSearchQuery(TypedDict, total=False):
    """Search query for metafield_blogs entity."""
    filter: MetafieldBlogsCondition
    sort: list[MetafieldBlogsSortFilter]


# ===== METAFIELD_ARTICLES SEARCH TYPES =====

class MetafieldArticlesSearchFilter(TypedDict, total=False):
    """Available fields for filtering metafield_articles search queries."""
    id: int | None
    """Unique identifier for the metafield"""
    namespace: str | None
    """Container namespace for the metafield"""
    key: str | None
    """Identifier key for the metafield"""
    value: str | None
    """The metafield value"""
    type_: str | None
    """The metafield's information type"""
    description: str | None
    """Human-readable description of the metafield"""
    owner_id: int | None
    """Identifier of the article that owns this metafield"""
    owner_resource: str | None
    """Resource type that owns this metafield (e.g. `article`)"""
    created_at: str | None
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str | None
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldArticlesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the metafield"""
    namespace: list[str]
    """Container namespace for the metafield"""
    key: list[str]
    """Identifier key for the metafield"""
    value: list[str]
    """The metafield value"""
    type_: list[str]
    """The metafield's information type"""
    description: list[str]
    """Human-readable description of the metafield"""
    owner_id: list[int]
    """Identifier of the article that owns this metafield"""
    owner_resource: list[str]
    """Resource type that owns this metafield (e.g. `article`)"""
    created_at: list[str]
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: list[str]
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldArticlesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the metafield"""
    namespace: Any
    """Container namespace for the metafield"""
    key: Any
    """Identifier key for the metafield"""
    value: Any
    """The metafield value"""
    type_: Any
    """The metafield's information type"""
    description: Any
    """Human-readable description of the metafield"""
    owner_id: Any
    """Identifier of the article that owns this metafield"""
    owner_resource: Any
    """Resource type that owns this metafield (e.g. `article`)"""
    created_at: Any
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: Any
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldArticlesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the metafield"""
    namespace: str
    """Container namespace for the metafield"""
    key: str
    """Identifier key for the metafield"""
    value: str
    """The metafield value"""
    type_: str
    """The metafield's information type"""
    description: str
    """Human-readable description of the metafield"""
    owner_id: str
    """Identifier of the article that owns this metafield"""
    owner_resource: str
    """Resource type that owns this metafield (e.g. `article`)"""
    created_at: str
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: str
    """ISO 8601 timestamp when the metafield was last updated"""


class MetafieldArticlesSortFilter(TypedDict, total=False):
    """Available fields for sorting metafield_articles search results."""
    id: AirbyteSortOrder
    """Unique identifier for the metafield"""
    namespace: AirbyteSortOrder
    """Container namespace for the metafield"""
    key: AirbyteSortOrder
    """Identifier key for the metafield"""
    value: AirbyteSortOrder
    """The metafield value"""
    type_: AirbyteSortOrder
    """The metafield's information type"""
    description: AirbyteSortOrder
    """Human-readable description of the metafield"""
    owner_id: AirbyteSortOrder
    """Identifier of the article that owns this metafield"""
    owner_resource: AirbyteSortOrder
    """Resource type that owns this metafield (e.g. `article`)"""
    created_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was created"""
    updated_at: AirbyteSortOrder
    """ISO 8601 timestamp when the metafield was last updated"""


# Entity-specific condition types for metafield_articles
class MetafieldArticlesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MetafieldArticlesSearchFilter


class MetafieldArticlesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MetafieldArticlesSearchFilter


class MetafieldArticlesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MetafieldArticlesSearchFilter


class MetafieldArticlesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MetafieldArticlesSearchFilter


class MetafieldArticlesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MetafieldArticlesSearchFilter


class MetafieldArticlesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MetafieldArticlesSearchFilter


class MetafieldArticlesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MetafieldArticlesStringFilter


class MetafieldArticlesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MetafieldArticlesStringFilter


class MetafieldArticlesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MetafieldArticlesStringFilter


class MetafieldArticlesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MetafieldArticlesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MetafieldArticlesInCondition = TypedDict("MetafieldArticlesInCondition", {"in": MetafieldArticlesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MetafieldArticlesNotCondition = TypedDict("MetafieldArticlesNotCondition", {"not": "MetafieldArticlesCondition"}, total=False)
"""Negates the nested condition."""

MetafieldArticlesAndCondition = TypedDict("MetafieldArticlesAndCondition", {"and": "list[MetafieldArticlesCondition]"}, total=False)
"""True if all nested conditions are true."""

MetafieldArticlesOrCondition = TypedDict("MetafieldArticlesOrCondition", {"or": "list[MetafieldArticlesCondition]"}, total=False)
"""True if any nested condition is true."""

MetafieldArticlesAnyCondition = TypedDict("MetafieldArticlesAnyCondition", {"any": MetafieldArticlesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all metafield_articles condition types
MetafieldArticlesCondition = (
    MetafieldArticlesEqCondition
    | MetafieldArticlesNeqCondition
    | MetafieldArticlesGtCondition
    | MetafieldArticlesGteCondition
    | MetafieldArticlesLtCondition
    | MetafieldArticlesLteCondition
    | MetafieldArticlesInCondition
    | MetafieldArticlesLikeCondition
    | MetafieldArticlesFuzzyCondition
    | MetafieldArticlesKeywordCondition
    | MetafieldArticlesContainsCondition
    | MetafieldArticlesNotCondition
    | MetafieldArticlesAndCondition
    | MetafieldArticlesOrCondition
    | MetafieldArticlesAnyCondition
)


class MetafieldArticlesSearchQuery(TypedDict, total=False):
    """Search query for metafield_articles entity."""
    filter: MetafieldArticlesCondition
    sort: list[MetafieldArticlesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
