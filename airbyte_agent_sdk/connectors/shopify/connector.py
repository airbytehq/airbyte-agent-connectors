"""
Shopify connector.
"""

from __future__ import annotations

import logging
from typing import Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import ShopifyConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    AbandonedCheckoutsListParams,
    ArticlesCreateParams,
    ArticlesCreateParamsArticle,
    ArticlesDeleteParams,
    ArticlesGetParams,
    ArticlesListParams,
    ArticlesUpdateParams,
    ArticlesUpdateParamsArticle,
    BalanceTransactionsListParams,
    BlogsCreateParams,
    BlogsCreateParamsBlog,
    BlogsDeleteParams,
    BlogsGetParams,
    BlogsListParams,
    BlogsUpdateParams,
    BlogsUpdateParamsBlog,
    CollectsGetParams,
    CollectsListParams,
    CountriesGetParams,
    CountriesListParams,
    CustomCollectionsCreateParams,
    CustomCollectionsCreateParamsInput,
    CustomCollectionsDeleteParams,
    CustomCollectionsDeleteParamsInput,
    CustomCollectionsGetParams,
    CustomCollectionsListParams,
    CustomCollectionsUpdateParams,
    CustomCollectionsUpdateParamsInput,
    CustomerAddressGetParams,
    CustomerAddressListParams,
    CustomersCreateParams,
    CustomersCreateParamsInput,
    CustomersDeleteParams,
    CustomersDeleteParamsInput,
    CustomersGetParams,
    CustomersListParams,
    CustomersUpdateParams,
    CustomersUpdateParamsInput,
    DiscountCodesCreateParams,
    DiscountCodesCreateParamsBasiccodediscount,
    DiscountCodesDeleteParams,
    DiscountCodesGetParams,
    DiscountCodesListParams,
    DiscountCodesUpdateParams,
    DiscountCodesUpdateParamsBasiccodediscount,
    DisputesGetParams,
    DisputesListParams,
    DraftOrderCompleteUpdateParams,
    DraftOrdersCreateParams,
    DraftOrdersCreateParamsInput,
    DraftOrdersDeleteParams,
    DraftOrdersDeleteParamsInput,
    DraftOrdersGetParams,
    DraftOrdersListParams,
    DraftOrdersUpdateParams,
    DraftOrdersUpdateParamsInput,
    FulfillmentOrdersGetParams,
    FulfillmentOrdersListParams,
    FulfillmentsGetParams,
    FulfillmentsListParams,
    InventoryAdjustCreateParams,
    InventoryAdjustCreateParamsInput,
    InventoryItemsGetParams,
    InventoryItemsListParams,
    InventoryLevelsListParams,
    InventorySetCreateParams,
    InventorySetCreateParamsInput,
    LocationsGetParams,
    LocationsListParams,
    MetafieldArticlesListParams,
    MetafieldBlogsListParams,
    MetafieldCustomersListParams,
    MetafieldDraftOrdersListParams,
    MetafieldLocationsListParams,
    MetafieldOrdersListParams,
    MetafieldPagesListParams,
    MetafieldProductImagesListParams,
    MetafieldProductVariantsListParams,
    MetafieldProductsListParams,
    MetafieldShopsGetParams,
    MetafieldShopsListParams,
    MetafieldSmartCollectionsListParams,
    MetafieldsCreateParams,
    MetafieldsCreateParamsMetafieldsItem,
    MetafieldsDeleteParams,
    MetafieldsDeleteParamsMetafieldsItem,
    OrderRefundsGetParams,
    OrderRefundsListParams,
    OrdersCreateParams,
    OrdersCreateParamsOptions,
    OrdersCreateParamsOrder,
    OrdersDeleteParams,
    OrdersGetParams,
    OrdersListParams,
    OrdersUpdateParams,
    OrdersUpdateParamsInput,
    PagesCreateParams,
    PagesCreateParamsPage,
    PagesDeleteParams,
    PagesGetParams,
    PagesListParams,
    PagesUpdateParams,
    PagesUpdateParamsPage,
    PriceRulesGetParams,
    PriceRulesListParams,
    ProductImagesGetParams,
    ProductImagesListParams,
    ProductVariantsCreateParams,
    ProductVariantsCreateParamsVariantsItem,
    ProductVariantsDeleteParams,
    ProductVariantsGetParams,
    ProductVariantsListParams,
    ProductVariantsUpdateParams,
    ProductVariantsUpdateParamsVariantsItem,
    ProductsCreateParams,
    ProductsCreateParamsMediaItem,
    ProductsCreateParamsProduct,
    ProductsDeleteParams,
    ProductsDeleteParamsInput,
    ProductsGetParams,
    ProductsListParams,
    ProductsUpdateParams,
    ProductsUpdateParamsProduct,
    ShopGetParams,
    SmartCollectionsGetParams,
    SmartCollectionsListParams,
    TenderTransactionsListParams,
    TransactionsGetParams,
    TransactionsListParams,
    AirbyteSearchParams,
    AbandonedCheckoutsSearchFilter,
    AbandonedCheckoutsSearchQuery,
    CollectsSearchFilter,
    CollectsSearchQuery,
    CountriesSearchFilter,
    CountriesSearchQuery,
    CustomCollectionsSearchFilter,
    CustomCollectionsSearchQuery,
    CustomersSearchFilter,
    CustomersSearchQuery,
    DiscountCodesSearchFilter,
    DiscountCodesSearchQuery,
    DraftOrdersSearchFilter,
    DraftOrdersSearchQuery,
    FulfillmentOrdersSearchFilter,
    FulfillmentOrdersSearchQuery,
    FulfillmentsSearchFilter,
    FulfillmentsSearchQuery,
    InventoryItemsSearchFilter,
    InventoryItemsSearchQuery,
    InventoryLevelsSearchFilter,
    InventoryLevelsSearchQuery,
    LocationsSearchFilter,
    LocationsSearchQuery,
    MetafieldCustomersSearchFilter,
    MetafieldCustomersSearchQuery,
    MetafieldDraftOrdersSearchFilter,
    MetafieldDraftOrdersSearchQuery,
    MetafieldLocationsSearchFilter,
    MetafieldLocationsSearchQuery,
    MetafieldOrdersSearchFilter,
    MetafieldOrdersSearchQuery,
    MetafieldProductImagesSearchFilter,
    MetafieldProductImagesSearchQuery,
    MetafieldProductVariantsSearchFilter,
    MetafieldProductVariantsSearchQuery,
    MetafieldProductsSearchFilter,
    MetafieldProductsSearchQuery,
    MetafieldShopsSearchFilter,
    MetafieldShopsSearchQuery,
    MetafieldSmartCollectionsSearchFilter,
    MetafieldSmartCollectionsSearchQuery,
    OrderRefundsSearchFilter,
    OrderRefundsSearchQuery,
    OrdersSearchFilter,
    OrdersSearchQuery,
    PriceRulesSearchFilter,
    PriceRulesSearchQuery,
    ProductImagesSearchFilter,
    ProductImagesSearchQuery,
    ProductsSearchFilter,
    ProductsSearchQuery,
    ProductVariantsSearchFilter,
    ProductVariantsSearchQuery,
    ShopSearchFilter,
    ShopSearchQuery,
    SmartCollectionsSearchFilter,
    SmartCollectionsSearchQuery,
    TenderTransactionsSearchFilter,
    TenderTransactionsSearchQuery,
    PagesSearchFilter,
    PagesSearchQuery,
    BlogsSearchFilter,
    BlogsSearchQuery,
    ArticlesSearchFilter,
    ArticlesSearchQuery,
    BalanceTransactionsSearchFilter,
    BalanceTransactionsSearchQuery,
    DisputesSearchFilter,
    DisputesSearchQuery,
    MetafieldPagesSearchFilter,
    MetafieldPagesSearchQuery,
    MetafieldBlogsSearchFilter,
    MetafieldBlogsSearchQuery,
    MetafieldArticlesSearchFilter,
    MetafieldArticlesSearchQuery,
)
from .models import ShopifyAccessTokenAuthenticationAuthConfig, ShopifyOauth2AuthConfig
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
    PagesListResult,
    BlogsListResult,
    ArticlesListResult,
    BalanceTransactionsListResult,
    DisputesListResult,
    MetafieldPagesListResult,
    MetafieldBlogsListResult,
    MetafieldArticlesListResult,
    AbandonedCheckout,
    Article,
    ArticleCreatePayload,
    ArticleDeletePayload,
    ArticleUpdatePayload,
    BalanceTransaction,
    Blog,
    BlogCreatePayload,
    BlogDeletePayload,
    BlogUpdatePayload,
    Collect,
    CollectionCreatePayload,
    CollectionDeletePayload,
    CollectionUpdatePayload,
    Country,
    CustomCollection,
    Customer,
    CustomerAddress,
    CustomerCreatePayload,
    CustomerDeletePayload,
    CustomerUpdatePayload,
    DiscountCode,
    DiscountCodeBasicCreatePayload,
    DiscountCodeBasicUpdatePayload,
    DiscountCodeDeletePayload,
    Dispute,
    DraftOrder,
    DraftOrderCompletePayload,
    DraftOrderCreatePayload,
    DraftOrderDeletePayload,
    DraftOrderUpdatePayload,
    Fulfillment,
    FulfillmentOrder,
    InventoryAdjustQuantitiesPayload,
    InventoryItem,
    InventoryLevel,
    InventorySetQuantitiesPayload,
    Location,
    Metafield,
    MetafieldDeletePayload,
    MetafieldsSetPayload,
    Order,
    OrderCancelPayload,
    OrderCreatePayload,
    OrderUpdatePayload,
    Page,
    PageCreatePayload,
    PageDeletePayload,
    PageUpdatePayload,
    PriceRule,
    Product,
    ProductCreatePayload,
    ProductDeletePayload,
    ProductImage,
    ProductUpdatePayload,
    ProductVariant,
    ProductVariantsBulkCreatePayload,
    ProductVariantsBulkDeletePayload,
    ProductVariantsBulkUpdatePayload,
    Refund,
    Shop,
    SmartCollection,
    TenderTransaction,
    Transaction,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AbandonedCheckoutsSearchData,
    AbandonedCheckoutsSearchResult,
    CollectsSearchData,
    CollectsSearchResult,
    CountriesSearchData,
    CountriesSearchResult,
    CustomCollectionsSearchData,
    CustomCollectionsSearchResult,
    CustomersSearchData,
    CustomersSearchResult,
    DiscountCodesSearchData,
    DiscountCodesSearchResult,
    DraftOrdersSearchData,
    DraftOrdersSearchResult,
    FulfillmentOrdersSearchData,
    FulfillmentOrdersSearchResult,
    FulfillmentsSearchData,
    FulfillmentsSearchResult,
    InventoryItemsSearchData,
    InventoryItemsSearchResult,
    InventoryLevelsSearchData,
    InventoryLevelsSearchResult,
    LocationsSearchData,
    LocationsSearchResult,
    MetafieldCustomersSearchData,
    MetafieldCustomersSearchResult,
    MetafieldDraftOrdersSearchData,
    MetafieldDraftOrdersSearchResult,
    MetafieldLocationsSearchData,
    MetafieldLocationsSearchResult,
    MetafieldOrdersSearchData,
    MetafieldOrdersSearchResult,
    MetafieldProductImagesSearchData,
    MetafieldProductImagesSearchResult,
    MetafieldProductVariantsSearchData,
    MetafieldProductVariantsSearchResult,
    MetafieldProductsSearchData,
    MetafieldProductsSearchResult,
    MetafieldShopsSearchData,
    MetafieldShopsSearchResult,
    MetafieldSmartCollectionsSearchData,
    MetafieldSmartCollectionsSearchResult,
    OrderRefundsSearchData,
    OrderRefundsSearchResult,
    OrdersSearchData,
    OrdersSearchResult,
    PriceRulesSearchData,
    PriceRulesSearchResult,
    ProductImagesSearchData,
    ProductImagesSearchResult,
    ProductsSearchData,
    ProductsSearchResult,
    ProductVariantsSearchData,
    ProductVariantsSearchResult,
    ShopSearchData,
    ShopSearchResult,
    SmartCollectionsSearchData,
    SmartCollectionsSearchResult,
    TenderTransactionsSearchData,
    TenderTransactionsSearchResult,
    PagesSearchData,
    PagesSearchResult,
    BlogsSearchData,
    BlogsSearchResult,
    ArticlesSearchData,
    ArticlesSearchResult,
    BalanceTransactionsSearchData,
    BalanceTransactionsSearchResult,
    DisputesSearchData,
    DisputesSearchResult,
    MetafieldPagesSearchData,
    MetafieldPagesSearchResult,
    MetafieldBlogsSearchData,
    MetafieldBlogsSearchResult,
    MetafieldArticlesSearchData,
    MetafieldArticlesSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class ShopifyConnector:
    """
    Type-safe Shopify API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "shopify"
    connector_version = "0.1.13"
    sdk_version = "0.1.287"

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
        ("pages", "list"): True,
        ("pages", "get"): None,
        ("blogs", "list"): True,
        ("blogs", "get"): None,
        ("articles", "list"): True,
        ("articles", "get"): None,
        ("balance_transactions", "list"): True,
        ("disputes", "list"): True,
        ("disputes", "get"): None,
        ("metafield_pages", "list"): True,
        ("metafield_blogs", "list"): True,
        ("metafield_articles", "list"): True,
        ("customers", "create"): None,
        ("customers", "update"): None,
        ("customers", "delete"): None,
        ("products", "create"): None,
        ("products", "update"): None,
        ("products", "delete"): None,
        ("product_variants", "create"): None,
        ("product_variants", "update"): None,
        ("product_variants", "delete"): None,
        ("orders", "create"): None,
        ("orders", "update"): None,
        ("orders", "delete"): None,
        ("draft_orders", "create"): None,
        ("draft_orders", "update"): None,
        ("draft_orders", "delete"): None,
        ("draft_order_complete", "update"): None,
        ("inventory_set", "create"): None,
        ("inventory_adjust", "create"): None,
        ("discount_codes", "create"): None,
        ("discount_codes", "update"): None,
        ("discount_codes", "delete"): None,
        ("metafields", "create"): None,
        ("metafields", "delete"): None,
        ("custom_collections", "create"): None,
        ("custom_collections", "update"): None,
        ("custom_collections", "delete"): None,
        ("pages", "create"): None,
        ("pages", "update"): None,
        ("pages", "delete"): None,
        ("blogs", "create"): None,
        ("blogs", "update"): None,
        ("blogs", "delete"): None,
        ("articles", "create"): None,
        ("articles", "update"): None,
        ("articles", "delete"): None,
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
        ('pages', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'created_at_min': 'created_at_min', 'created_at_max': 'created_at_max', 'updated_at_min': 'updated_at_min', 'updated_at_max': 'updated_at_max', 'published_status': 'published_status'},
        ('pages', 'get'): {'page_id': 'page_id'},
        ('blogs', 'list'): {'limit': 'limit', 'since_id': 'since_id'},
        ('blogs', 'get'): {'blog_id': 'blog_id'},
        ('articles', 'list'): {'blog_id': 'blog_id', 'limit': 'limit', 'since_id': 'since_id', 'created_at_min': 'created_at_min', 'created_at_max': 'created_at_max', 'updated_at_min': 'updated_at_min', 'updated_at_max': 'updated_at_max', 'published_status': 'published_status'},
        ('articles', 'get'): {'blog_id': 'blog_id', 'article_id': 'article_id'},
        ('balance_transactions', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'payout_id': 'payout_id', 'payout_status': 'payout_status'},
        ('disputes', 'list'): {'limit': 'limit', 'since_id': 'since_id', 'status': 'status', 'initiated_at': 'initiated_at'},
        ('disputes', 'get'): {'dispute_id': 'dispute_id'},
        ('metafield_pages', 'list'): {'page_id': 'page_id', 'limit': 'limit'},
        ('metafield_blogs', 'list'): {'blog_id': 'blog_id', 'limit': 'limit'},
        ('metafield_articles', 'list'): {'blog_id': 'blog_id', 'article_id': 'article_id', 'limit': 'limit'},
        ('customers', 'create'): {'input': 'input'},
        ('customers', 'update'): {'input': 'input'},
        ('customers', 'delete'): {'input': 'input'},
        ('products', 'create'): {'product': 'product', 'media': 'media'},
        ('products', 'update'): {'product': 'product'},
        ('products', 'delete'): {'input': 'input'},
        ('product_variants', 'create'): {'product_id': 'productId', 'variants': 'variants'},
        ('product_variants', 'update'): {'product_id': 'productId', 'variants': 'variants'},
        ('product_variants', 'delete'): {'product_id': 'productId', 'variants_ids': 'variantsIds'},
        ('orders', 'create'): {'order': 'order', 'options': 'options'},
        ('orders', 'update'): {'input': 'input'},
        ('orders', 'delete'): {'order_id': 'orderId', 'reason': 'reason', 'notify_customer': 'notifyCustomer', 'refund': 'refund', 'restock': 'restock', 'staff_note': 'staffNote'},
        ('draft_orders', 'create'): {'input': 'input'},
        ('draft_orders', 'update'): {'id': 'id', 'input': 'input'},
        ('draft_orders', 'delete'): {'input': 'input'},
        ('draft_order_complete', 'update'): {'id': 'id', 'payment_pending': 'paymentPending'},
        ('inventory_set', 'create'): {'input': 'input'},
        ('inventory_adjust', 'create'): {'input': 'input'},
        ('discount_codes', 'create'): {'basic_code_discount': 'basicCodeDiscount'},
        ('discount_codes', 'update'): {'id': 'id', 'basic_code_discount': 'basicCodeDiscount'},
        ('discount_codes', 'delete'): {'id': 'id'},
        ('metafields', 'create'): {'metafields': 'metafields'},
        ('metafields', 'delete'): {'metafields': 'metafields'},
        ('custom_collections', 'create'): {'input': 'input'},
        ('custom_collections', 'update'): {'input': 'input'},
        ('custom_collections', 'delete'): {'input': 'input'},
        ('pages', 'create'): {'page': 'page'},
        ('pages', 'update'): {'id': 'id', 'page': 'page'},
        ('pages', 'delete'): {'id': 'id'},
        ('blogs', 'create'): {'blog': 'blog'},
        ('blogs', 'update'): {'id': 'id', 'blog': 'blog'},
        ('blogs', 'delete'): {'id': 'id'},
        ('articles', 'create'): {'article': 'article'},
        ('articles', 'update'): {'id': 'id', 'article': 'article'},
        ('articles', 'delete'): {'id': 'id'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (ShopifyAccessTokenAuthenticationAuthConfig, ShopifyOauth2AuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: ShopifyAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None,
        shop: str | None = None    ):
        """
        Initialize a new shopify connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., ShopifyAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            shop: Your Shopify store name (e.g., 'my-store' from my-store.myshopify.com)
        Examples:
            # Local mode (direct API calls)
            connector = ShopifyConnector(auth_config=ShopifyAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = ShopifyConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = ShopifyConnector(
                auth_config=AirbyteAuthConfig(
                    workspace_name="user-123",
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
            from airbyte_agent_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                workspace_name=auth_config.workspace_name or "default",
                organization_id=auth_config.organization_id,
                connector_definition_id=str(ShopifyConnectorModel.id),
                model=ShopifyConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or ShopifyAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if shop:
                config_values["shop"] = shop

            # Multi-auth connector: detect auth scheme from auth_config type
            auth_scheme: str | None = None
            if auth_config:
                if isinstance(auth_config, ShopifyAccessTokenAuthenticationAuthConfig):
                    auth_scheme = "shopifyAccessToken"
                if isinstance(auth_config, ShopifyOauth2AuthConfig):
                    auth_scheme = "shopifyOAuth"

            self._executor = LocalExecutor(
                model=ShopifyConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                auth_scheme=auth_scheme,
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
        self.pages = PagesQuery(self)
        self.blogs = BlogsQuery(self)
        self.articles = ArticlesQuery(self)
        self.balance_transactions = BalanceTransactionsQuery(self)
        self.disputes = DisputesQuery(self)
        self.metafield_pages = MetafieldPagesQuery(self)
        self.metafield_blogs = MetafieldBlogsQuery(self)
        self.metafield_articles = MetafieldArticlesQuery(self)
        self.draft_order_complete = DraftOrderCompleteQuery(self)
        self.inventory_set = InventorySetQuery(self)
        self.inventory_adjust = InventoryAdjustQuery(self)
        self.metafields = MetafieldsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["customers"],
        action: Literal["list"],
        params: "CustomersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CustomersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["customers"],
        action: Literal["get"],
        params: "CustomersGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Customer": ...

    @overload
    async def execute(
        self,
        entity: Literal["orders"],
        action: Literal["list"],
        params: "OrdersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "OrdersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["orders"],
        action: Literal["get"],
        params: "OrdersGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Order": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["list"],
        params: "ProductsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ProductsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["get"],
        params: "ProductsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Product": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_variants"],
        action: Literal["list"],
        params: "ProductVariantsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ProductVariantsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_variants"],
        action: Literal["get"],
        params: "ProductVariantsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ProductVariant": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_images"],
        action: Literal["list"],
        params: "ProductImagesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ProductImagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_images"],
        action: Literal["get"],
        params: "ProductImagesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ProductImage": ...

    @overload
    async def execute(
        self,
        entity: Literal["abandoned_checkouts"],
        action: Literal["list"],
        params: "AbandonedCheckoutsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "AbandonedCheckoutsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["locations"],
        action: Literal["list"],
        params: "LocationsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "LocationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["locations"],
        action: Literal["get"],
        params: "LocationsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Location": ...

    @overload
    async def execute(
        self,
        entity: Literal["inventory_levels"],
        action: Literal["list"],
        params: "InventoryLevelsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "InventoryLevelsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["inventory_items"],
        action: Literal["list"],
        params: "InventoryItemsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "InventoryItemsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["inventory_items"],
        action: Literal["get"],
        params: "InventoryItemsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "InventoryItem": ...

    @overload
    async def execute(
        self,
        entity: Literal["shop"],
        action: Literal["get"],
        params: "ShopGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Shop": ...

    @overload
    async def execute(
        self,
        entity: Literal["price_rules"],
        action: Literal["list"],
        params: "PriceRulesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "PriceRulesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["price_rules"],
        action: Literal["get"],
        params: "PriceRulesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "PriceRule": ...

    @overload
    async def execute(
        self,
        entity: Literal["discount_codes"],
        action: Literal["list"],
        params: "DiscountCodesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DiscountCodesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["discount_codes"],
        action: Literal["get"],
        params: "DiscountCodesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DiscountCode": ...

    @overload
    async def execute(
        self,
        entity: Literal["custom_collections"],
        action: Literal["list"],
        params: "CustomCollectionsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CustomCollectionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["custom_collections"],
        action: Literal["get"],
        params: "CustomCollectionsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CustomCollection": ...

    @overload
    async def execute(
        self,
        entity: Literal["smart_collections"],
        action: Literal["list"],
        params: "SmartCollectionsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SmartCollectionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["smart_collections"],
        action: Literal["get"],
        params: "SmartCollectionsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SmartCollection": ...

    @overload
    async def execute(
        self,
        entity: Literal["collects"],
        action: Literal["list"],
        params: "CollectsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CollectsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["collects"],
        action: Literal["get"],
        params: "CollectsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Collect": ...

    @overload
    async def execute(
        self,
        entity: Literal["draft_orders"],
        action: Literal["list"],
        params: "DraftOrdersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DraftOrdersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["draft_orders"],
        action: Literal["get"],
        params: "DraftOrdersGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DraftOrder": ...

    @overload
    async def execute(
        self,
        entity: Literal["fulfillments"],
        action: Literal["list"],
        params: "FulfillmentsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "FulfillmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["fulfillments"],
        action: Literal["get"],
        params: "FulfillmentsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Fulfillment": ...

    @overload
    async def execute(
        self,
        entity: Literal["order_refunds"],
        action: Literal["list"],
        params: "OrderRefundsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "OrderRefundsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["order_refunds"],
        action: Literal["get"],
        params: "OrderRefundsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Refund": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactions"],
        action: Literal["list"],
        params: "TransactionsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TransactionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["transactions"],
        action: Literal["get"],
        params: "TransactionsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Transaction": ...

    @overload
    async def execute(
        self,
        entity: Literal["tender_transactions"],
        action: Literal["list"],
        params: "TenderTransactionsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "TenderTransactionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["countries"],
        action: Literal["list"],
        params: "CountriesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CountriesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["countries"],
        action: Literal["get"],
        params: "CountriesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Country": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_shops"],
        action: Literal["list"],
        params: "MetafieldShopsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldShopsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_shops"],
        action: Literal["get"],
        params: "MetafieldShopsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Metafield": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_customers"],
        action: Literal["list"],
        params: "MetafieldCustomersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldCustomersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_products"],
        action: Literal["list"],
        params: "MetafieldProductsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldProductsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_orders"],
        action: Literal["list"],
        params: "MetafieldOrdersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldOrdersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_draft_orders"],
        action: Literal["list"],
        params: "MetafieldDraftOrdersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldDraftOrdersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_locations"],
        action: Literal["list"],
        params: "MetafieldLocationsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldLocationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_product_variants"],
        action: Literal["list"],
        params: "MetafieldProductVariantsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldProductVariantsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_smart_collections"],
        action: Literal["list"],
        params: "MetafieldSmartCollectionsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldSmartCollectionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_product_images"],
        action: Literal["list"],
        params: "MetafieldProductImagesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldProductImagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["customer_address"],
        action: Literal["list"],
        params: "CustomerAddressListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CustomerAddressListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["customer_address"],
        action: Literal["get"],
        params: "CustomerAddressGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CustomerAddress": ...

    @overload
    async def execute(
        self,
        entity: Literal["fulfillment_orders"],
        action: Literal["list"],
        params: "FulfillmentOrdersListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "FulfillmentOrdersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["fulfillment_orders"],
        action: Literal["get"],
        params: "FulfillmentOrdersGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "FulfillmentOrder": ...

    @overload
    async def execute(
        self,
        entity: Literal["pages"],
        action: Literal["list"],
        params: "PagesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "PagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["pages"],
        action: Literal["get"],
        params: "PagesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Page": ...

    @overload
    async def execute(
        self,
        entity: Literal["blogs"],
        action: Literal["list"],
        params: "BlogsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "BlogsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["blogs"],
        action: Literal["get"],
        params: "BlogsGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Blog": ...

    @overload
    async def execute(
        self,
        entity: Literal["articles"],
        action: Literal["list"],
        params: "ArticlesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ArticlesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["articles"],
        action: Literal["get"],
        params: "ArticlesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Article": ...

    @overload
    async def execute(
        self,
        entity: Literal["balance_transactions"],
        action: Literal["list"],
        params: "BalanceTransactionsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "BalanceTransactionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["disputes"],
        action: Literal["list"],
        params: "DisputesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DisputesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["disputes"],
        action: Literal["get"],
        params: "DisputesGetParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "Dispute": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_pages"],
        action: Literal["list"],
        params: "MetafieldPagesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldPagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_blogs"],
        action: Literal["list"],
        params: "MetafieldBlogsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldBlogsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafield_articles"],
        action: Literal["list"],
        params: "MetafieldArticlesListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldArticlesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["customers"],
        action: Literal["create"],
        params: "CustomersCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CustomerCreatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["customers"],
        action: Literal["update"],
        params: "CustomersUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CustomerUpdatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["customers"],
        action: Literal["delete"],
        params: "CustomersDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CustomerDeletePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["create"],
        params: "ProductsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ProductCreatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["update"],
        params: "ProductsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ProductUpdatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["products"],
        action: Literal["delete"],
        params: "ProductsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ProductDeletePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_variants"],
        action: Literal["create"],
        params: "ProductVariantsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ProductVariantsBulkCreatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_variants"],
        action: Literal["update"],
        params: "ProductVariantsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ProductVariantsBulkUpdatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["product_variants"],
        action: Literal["delete"],
        params: "ProductVariantsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ProductVariantsBulkDeletePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["orders"],
        action: Literal["create"],
        params: "OrdersCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "OrderCreatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["orders"],
        action: Literal["update"],
        params: "OrdersUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "OrderUpdatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["orders"],
        action: Literal["delete"],
        params: "OrdersDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "OrderCancelPayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["draft_orders"],
        action: Literal["create"],
        params: "DraftOrdersCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DraftOrderCreatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["draft_orders"],
        action: Literal["update"],
        params: "DraftOrdersUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DraftOrderUpdatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["draft_orders"],
        action: Literal["delete"],
        params: "DraftOrdersDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DraftOrderDeletePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["draft_order_complete"],
        action: Literal["update"],
        params: "DraftOrderCompleteUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DraftOrderCompletePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["inventory_set"],
        action: Literal["create"],
        params: "InventorySetCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "InventorySetQuantitiesPayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["inventory_adjust"],
        action: Literal["create"],
        params: "InventoryAdjustCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "InventoryAdjustQuantitiesPayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["discount_codes"],
        action: Literal["create"],
        params: "DiscountCodesCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DiscountCodeBasicCreatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["discount_codes"],
        action: Literal["update"],
        params: "DiscountCodesUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DiscountCodeBasicUpdatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["discount_codes"],
        action: Literal["delete"],
        params: "DiscountCodesDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "DiscountCodeDeletePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafields"],
        action: Literal["create"],
        params: "MetafieldsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldsSetPayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["metafields"],
        action: Literal["delete"],
        params: "MetafieldsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "MetafieldDeletePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["custom_collections"],
        action: Literal["create"],
        params: "CustomCollectionsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CollectionCreatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["custom_collections"],
        action: Literal["update"],
        params: "CustomCollectionsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CollectionUpdatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["custom_collections"],
        action: Literal["delete"],
        params: "CustomCollectionsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "CollectionDeletePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["pages"],
        action: Literal["create"],
        params: "PagesCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "PageCreatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["pages"],
        action: Literal["update"],
        params: "PagesUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "PageUpdatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["pages"],
        action: Literal["delete"],
        params: "PagesDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "PageDeletePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["blogs"],
        action: Literal["create"],
        params: "BlogsCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "BlogCreatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["blogs"],
        action: Literal["update"],
        params: "BlogsUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "BlogUpdatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["blogs"],
        action: Literal["delete"],
        params: "BlogsDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "BlogDeletePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["articles"],
        action: Literal["create"],
        params: "ArticlesCreateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ArticleCreatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["articles"],
        action: Literal["update"],
        params: "ArticlesUpdateParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ArticleUpdatePayload": ...

    @overload
    async def execute(
        self,
        entity: Literal["articles"],
        action: Literal["delete"],
        params: "ArticlesDeleteParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ArticleDeletePayload": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "create", "update", "delete", "context_store_search"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> ShopifyExecuteResult[Any] | ShopifyExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "create", "update", "delete", "context_store_search"],
        params: Mapping[str, Any] | None = None,
        *,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True
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
            select_fields: Optional allowlist of dot-notation fields to include
            exclude_fields: Optional blocklist of dot-notation fields to remove
            skip_truncation: Disable long-text truncation for collection actions

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from airbyte_agent_sdk.executor import ExecutionConfig

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
            params=resolved_params,
            select_fields=select_fields,
            exclude_fields=exclude_fields,
            skip_truncation=skip_truncation
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
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
        framework: FrameworkName | None = None,
        internal_retries: int = 0,
        should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
        exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
    ) -> _F | Callable[[_F], _F]:
        """
        Add connector-specific documentation and runtime safeguards to one tool.

        For new agents, prefer `build_connector_tools`. It returns progressive
        `inspect_connector`, `read_skill_docs`, and `execute` tools so the agent
        can load only the connector guidance it needs:

        ```python
        from airbyte_agent_sdk import build_connector_tools
        from pydantic_ai import Agent

        tools = build_connector_tools(connector, framework="pydantic_ai")
        agent = Agent("openai:gpt-4o", tools=tools.as_list())
        ```

        ### Legacy: one generated-description tool

        Existing integrations can keep using `tool_utils` for one broad
        `execute` tool with the connector's full generated catalog in its
        description:

        ```python
        from fastmcp import FastMCP

        connector = ShopifyConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @ShopifyConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @ShopifyConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @ShopifyConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        This decorator composes `translate_exceptions` for runtime wrapping,
        output-size checks, framework signal translation, and optional internal
        retries, then adds connector-specific docstring augmentation.

        Args:
            update_docstring: When True, append connector capabilities to `__doc__`.
            max_output_chars: Max serialized output size before raising. Use `None` to disable.
            framework: One of `"pydantic_ai" | "langchain" | "openai_agents" | "mcp"`.
                Defaults to `None`, which auto-detects each framework's canonical
                import in order. Explicit always wins.
            internal_retries: How many transient runtime failures (429/5xx, network,
                timeout) to retry silently before surfacing. Default 0. Forwarded to
                `airbyte_agent_sdk.translation.translate_exceptions`.
            should_internal_retry: Optional predicate `(error, args, kwargs) -> bool`
                further restricting which retryable errors are safe for this specific
                tool. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
            exhausted_runtime_failure_message: Optional callback
                `(error, args, kwargs) -> str | None`. Invoked after internal retries
                are exhausted or were skipped because `should_internal_retry` returned
                `False`. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    ShopifyConnectorModel,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            wrapped = translate_exceptions(
                inner,
                framework=framework,
                max_output_chars=max_output_chars,
                internal_retries=internal_retries,
                should_internal_retry=should_internal_retry,
                exhausted_runtime_failure_message=exhausted_runtime_failure_message,
            )

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
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== RESOURCE MANAGEMENT =====

    async def close(self):
        """Close the connector and release resources."""
        await self._executor.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()



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
            meta=getattr(result, "meta", None)
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



    async def create(
        self,
        input: CustomersCreateParamsInput,
        **kwargs
    ) -> CustomerCreatePayload:
        """
        Creates a new customer in the store via GraphQL mutation.
Requires at least one of: email, phone, firstName, or lastName.


        Args:
            input: CustomerInput object
            **kwargs: Additional parameters

        Returns:
            CustomerCreatePayload
        """
        params = {k: v for k, v in {
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "create", params)
        return result



    async def update(
        self,
        input: CustomersUpdateParamsInput,
        **kwargs
    ) -> CustomerUpdatePayload:
        """
        Updates an existing customer via GraphQL mutation.
All fields except id are optional for partial updates.


        Args:
            input: CustomerInput object with id
            **kwargs: Additional parameters

        Returns:
            CustomerUpdatePayload
        """
        params = {k: v for k, v in {
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "update", params)
        return result



    async def delete(
        self,
        input: CustomersDeleteParamsInput,
        **kwargs
    ) -> CustomerDeletePayload:
        """
        Deletes a customer from the store via GraphQL mutation.
Only succeeds if the customer has no orders. This action is irreversible.


        Args:
            input: Parameter input
            **kwargs: Additional parameters

        Returns:
            CustomerDeletePayload
        """
        params = {k: v for k, v in {
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("customers", "delete", params)
        return result



    async def context_store_search(
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
        - id: Unique identifier for the customer
        - email: Primary email address of the customer
        - phone: Primary phone number of the customer
        - first_name: First name of the customer
        - last_name: Last name of the customer
        - state: Account state (`disabled`, `invited`, `enabled`, `declined`)
        - orders_count: Number of orders placed by the customer
        - total_spent: Total lifetime amount spent by the customer
        - currency: ISO 4217 currency code for the customer's total spend
        - created_at: ISO 8601 timestamp when the customer record was created
        - updated_at: ISO 8601 timestamp when the customer record was last updated

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

        result = await self._connector.execute("customers", "context_store_search", params)

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
            meta=getattr(result, "meta", None)
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



    async def create(
        self,
        order: OrdersCreateParamsOrder,
        options: OrdersCreateParamsOptions | None = None,
        **kwargs
    ) -> OrderCreatePayload:
        """
        Creates a new order via GraphQL mutation.
Use line items with either variantId or customAttributes.


        Args:
            order: OrderCreateOrderInput object
            options: OrderCreateOptionsInput
            **kwargs: Additional parameters

        Returns:
            OrderCreatePayload
        """
        params = {k: v for k, v in {
            "order": order,
            "options": options,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("orders", "create", params)
        return result



    async def update(
        self,
        input: OrdersUpdateParamsInput,
        **kwargs
    ) -> OrderUpdatePayload:
        """
        Updates simple fields on an existing order via GraphQL mutation.
For line item changes, use orderEditBegin/orderEditCommit instead.


        Args:
            input: Parameter input
            **kwargs: Additional parameters

        Returns:
            OrderUpdatePayload
        """
        params = {k: v for k, v in {
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("orders", "update", params)
        return result



    async def delete(
        self,
        order_id: str,
        reason: str,
        restock: bool,
        notify_customer: bool | None = None,
        refund: bool | None = None,
        staff_note: str | None = None,
        **kwargs
    ) -> OrderCancelPayload:
        """
        Cancels an open order via GraphQL mutation.
This action is irreversible. Optional refund and restock parameters.


        Args:
            order_id: The GraphQL GID of the order to cancel
            reason: Reason for cancellation
            notify_customer: Whether to notify the customer
            refund: Whether to refund the order
            restock: Whether to restock items
            staff_note: Staff note for the cancellation
            **kwargs: Additional parameters

        Returns:
            OrderCancelPayload
        """
        params = {k: v for k, v in {
            "orderId": order_id,
            "reason": reason,
            "notifyCustomer": notify_customer,
            "refund": refund,
            "restock": restock,
            "staffNote": staff_note,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("orders", "delete", params)
        return result



    async def context_store_search(
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
        - id: Unique identifier for the order
        - name: Shopify-assigned display name for the order (e.g. `#1001`)
        - email: Email address associated with the order
        - phone: Phone number associated with the order
        - order_number: Sequential order number displayed in the Shopify admin
        - financial_status: Payment status of the order (e.g. `paid`, `pending`, `refunded`, `partially_refunded`)
        - fulfillment_status: Fulfillment status of the order (e.g. `fulfilled`, `partial`, `null` for unfulfilled)
        - currency: ISO 4217 currency code for the order totals
        - total_price: Total price of the order including taxes and discounts
        - subtotal_price: Subtotal of the order before shipping and taxes
        - total_tax: Total tax amount applied to the order
        - total_discounts: Total discount amount applied to the order
        - total_weight: Total weight of all items in the order, in grams
        - cancel_reason: Reason the order was cancelled, if applicable
        - cancelled_at: ISO 8601 timestamp when the order was cancelled, if applicable
        - closed_at: ISO 8601 timestamp when the order was closed, if applicable
        - tags: Comma-separated tags attached to the order
        - note: Merchant-provided note on the order
        - processed_at: ISO 8601 timestamp when the order was processed
        - created_at: ISO 8601 timestamp when the order was created
        - updated_at: ISO 8601 timestamp when the order was last updated

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

        result = await self._connector.execute("orders", "context_store_search", params)

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
            meta=getattr(result, "meta", None)
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



    async def create(
        self,
        product: ProductsCreateParamsProduct,
        media: list[ProductsCreateParamsMediaItem] | None = None,
        **kwargs
    ) -> ProductCreatePayload:
        """
        Creates a new product via GraphQL mutation.
Creates the product with a default variant. Use productVariantsBulkCreate
to add additional variants afterwards.


        Args:
            product: ProductCreateInput object
            media: Media to attach to the product
            **kwargs: Additional parameters

        Returns:
            ProductCreatePayload
        """
        params = {k: v for k, v in {
            "product": product,
            "media": media,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "create", params)
        return result



    async def update(
        self,
        product: ProductsUpdateParamsProduct,
        **kwargs
    ) -> ProductUpdatePayload:
        """
        Updates an existing product via GraphQL mutation.
All fields except id are optional for partial updates.


        Args:
            product: ProductUpdateInput object
            **kwargs: Additional parameters

        Returns:
            ProductUpdatePayload
        """
        params = {k: v for k, v in {
            "product": product,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "update", params)
        return result



    async def delete(
        self,
        input: ProductsDeleteParamsInput,
        **kwargs
    ) -> ProductDeletePayload:
        """
        Deletes a product from the store via GraphQL mutation.
This action is irreversible.


        Args:
            input: Parameter input
            **kwargs: Additional parameters

        Returns:
            ProductDeletePayload
        """
        params = {k: v for k, v in {
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("products", "delete", params)
        return result



    async def context_store_search(
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
        - id: Unique identifier for the product
        - title: Product title
        - body_html: Product description in HTML
        - vendor: Product vendor or manufacturer
        - product_type: Product type used for categorization
        - handle: URL-friendly handle for the product
        - status: Product status (`active`, `archived`, or `draft`)
        - tags: Comma-separated tags attached to the product
        - published_scope: Publishing scope (`web` or `global`)
        - published_at: ISO 8601 timestamp when the product was published
        - created_at: ISO 8601 timestamp when the product was created
        - updated_at: ISO 8601 timestamp when the product was last updated

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

        result = await self._connector.execute("products", "context_store_search", params)

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
            meta=getattr(result, "meta", None)
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



    async def create(
        self,
        product_id: str,
        variants: list[ProductVariantsCreateParamsVariantsItem],
        **kwargs
    ) -> ProductVariantsBulkCreatePayload:
        """
        Creates one or more product variants via GraphQL mutation.
Variants are created in bulk for a given product.


        Args:
            product_id: The GraphQL GID of the product (e.g. gid://shopify/Product/123)
            variants: List of variants to create
            **kwargs: Additional parameters

        Returns:
            ProductVariantsBulkCreatePayload
        """
        params = {k: v for k, v in {
            "productId": product_id,
            "variants": variants,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_variants", "create", params)
        return result



    async def update(
        self,
        product_id: str,
        variants: list[ProductVariantsUpdateParamsVariantsItem],
        **kwargs
    ) -> ProductVariantsBulkUpdatePayload:
        """
        Updates one or more product variants via GraphQL mutation.
Variants are updated in bulk for a given product.


        Args:
            product_id: The GraphQL GID of the product
            variants: List of variants to update (each must include id)
            **kwargs: Additional parameters

        Returns:
            ProductVariantsBulkUpdatePayload
        """
        params = {k: v for k, v in {
            "productId": product_id,
            "variants": variants,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_variants", "update", params)
        return result



    async def delete(
        self,
        product_id: str,
        variants_ids: list[str],
        **kwargs
    ) -> ProductVariantsBulkDeletePayload:
        """
        Deletes one or more product variants via GraphQL mutation.
Cannot delete the last variant of a product.


        Args:
            product_id: The GraphQL GID of the product
            variants_ids: List of variant GIDs to delete
            **kwargs: Additional parameters

        Returns:
            ProductVariantsBulkDeletePayload
        """
        params = {k: v for k, v in {
            "productId": product_id,
            "variantsIds": variants_ids,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("product_variants", "delete", params)
        return result



    async def context_store_search(
        self,
        query: ProductVariantsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProductVariantsSearchResult:
        """
        Search product_variants records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProductVariantsSearchFilter):
        - id: Unique identifier for the product variant
        - product_id: Identifier of the parent product
        - title: Display title of the variant
        - sku: Stock keeping unit for the variant
        - price: Price of the variant in the shop's currency
        - compare_at_price: Original (compare-at) price of the variant, if set
        - position: Display position of the variant within the product
        - inventory_policy: Behaviour when out of stock (`deny` or `continue`)
        - created_at: ISO 8601 timestamp when the variant was created
        - updated_at: ISO 8601 timestamp when the variant was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProductVariantsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("product_variants", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProductVariantsSearchResult(
            data=[
                ProductVariantsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
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



    async def context_store_search(
        self,
        query: ProductImagesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ProductImagesSearchResult:
        """
        Search product_images records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ProductImagesSearchFilter):
        - id: Unique identifier for the product image
        - product_id: Identifier of the product the image belongs to
        - position: Display position of the image within the product
        - alt: Alt text for the image
        - width: Image width in pixels
        - height: Image height in pixels
        - src: Public URL of the image
        - created_at: ISO 8601 timestamp when the image was created
        - updated_at: ISO 8601 timestamp when the image was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ProductImagesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("product_images", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ProductImagesSearchResult(
            data=[
                ProductImagesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: AbandonedCheckoutsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AbandonedCheckoutsSearchResult:
        """
        Search abandoned_checkouts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AbandonedCheckoutsSearchFilter):
        - id: Unique identifier for the abandoned checkout
        - token: Unique token identifying the checkout
        - email: Email address provided for the checkout
        - phone: Phone number provided for the checkout
        - name: Shopify-assigned display name for the checkout (e.g. `#C12345`)
        - currency: ISO 4217 currency code for the checkout totals
        - total_price: Total price of the checkout in the shop's currency
        - created_at: ISO 8601 timestamp when the checkout was created
        - updated_at: ISO 8601 timestamp when the checkout was last updated
        - completed_at: ISO 8601 timestamp when the checkout was completed, if applicable

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AbandonedCheckoutsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("abandoned_checkouts", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AbandonedCheckoutsSearchResult(
            data=[
                AbandonedCheckoutsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            meta=getattr(result, "meta", None)
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



    async def context_store_search(
        self,
        query: LocationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> LocationsSearchResult:
        """
        Search locations records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (LocationsSearchFilter):
        - id: Unique identifier for the location
        - name: Display name of the location
        - address1: Primary street address of the location
        - city: City of the location
        - province: Province, state, or region of the location
        - country: Country name of the location
        - country_code: ISO 3166-1 alpha-2 country code of the location
        - phone: Phone number for the location
        - active: Whether the location is currently active
        - created_at: ISO 8601 timestamp when the location was created
        - updated_at: ISO 8601 timestamp when the location was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            LocationsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("locations", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return LocationsSearchResult(
            data=[
                LocationsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: InventoryLevelsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> InventoryLevelsSearchResult:
        """
        Search inventory_levels records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (InventoryLevelsSearchFilter):
        - inventory_item_id: Identifier of the inventory item
        - location_id: Identifier of the location holding the inventory
        - available: Number of units available at the location
        - updated_at: ISO 8601 timestamp when the inventory level was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            InventoryLevelsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("inventory_levels", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return InventoryLevelsSearchResult(
            data=[
                InventoryLevelsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            meta=getattr(result, "meta", None)
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



    async def context_store_search(
        self,
        query: InventoryItemsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> InventoryItemsSearchResult:
        """
        Search inventory_items records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (InventoryItemsSearchFilter):
        - id: Unique identifier for the inventory item
        - sku: Stock keeping unit associated with the inventory item
        - tracked: Whether Shopify is tracking inventory for this item
        - requires_shipping: Whether the item requires shipping
        - country_code_of_origin: ISO country code of the item's country of origin
        - created_at: ISO 8601 timestamp when the inventory item was created
        - updated_at: ISO 8601 timestamp when the inventory item was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            InventoryItemsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("inventory_items", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return InventoryItemsSearchResult(
            data=[
                InventoryItemsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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



    async def context_store_search(
        self,
        query: ShopSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ShopSearchResult:
        """
        Search shop records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ShopSearchFilter):
        - id: Unique identifier for the shop
        - name: Display name of the shop
        - email: Primary contact email for the shop
        - domain: Custom domain configured for the shop, if any
        - myshopify_domain: Canonical `*.myshopify.com` domain for the shop
        - country_code: ISO 3166-1 alpha-2 country code of the shop
        - currency: ISO 4217 currency code used by the shop
        - timezone: Timezone configured for the shop (e.g. `(GMT-05:00) Eastern Time`)
        - plan_name: Shopify plan identifier (e.g. `shopify_plus`, `basic`)
        - created_at: ISO 8601 timestamp when the shop was created
        - updated_at: ISO 8601 timestamp when the shop was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ShopSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("shop", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ShopSearchResult(
            data=[
                ShopSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
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



    async def context_store_search(
        self,
        query: PriceRulesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> PriceRulesSearchResult:
        """
        Search price_rules records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (PriceRulesSearchFilter):
        - id: Unique identifier for the price rule
        - title: Administrative title of the price rule
        - value_type: How the discount value is interpreted (`fixed_amount` or `percentage`)
        - value: Discount value applied by the rule
        - target_type: Type of target the rule applies to (`line_item` or `shipping_line`)
        - target_selection: Which target items the rule applies to (`all` or `entitled`)
        - allocation_method: How the discount is allocated (`each` or `across`)
        - starts_at: ISO 8601 timestamp when the rule starts being active
        - ends_at: ISO 8601 timestamp when the rule stops being active, if applicable
        - created_at: ISO 8601 timestamp when the rule was created
        - updated_at: ISO 8601 timestamp when the rule was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            PriceRulesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("price_rules", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return PriceRulesSearchResult(
            data=[
                PriceRulesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
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



    async def create(
        self,
        basic_code_discount: DiscountCodesCreateParamsBasiccodediscount,
        **kwargs
    ) -> DiscountCodeBasicCreatePayload:
        """
        Creates a basic discount code via GraphQL mutation.
Supports percentage, fixed amount, or free shipping discounts.


        Args:
            basic_code_discount: Parameter basicCodeDiscount
            **kwargs: Additional parameters

        Returns:
            DiscountCodeBasicCreatePayload
        """
        params = {k: v for k, v in {
            "basicCodeDiscount": basic_code_discount,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("discount_codes", "create", params)
        return result



    async def update(
        self,
        basic_code_discount: DiscountCodesUpdateParamsBasiccodediscount,
        id: str | None = None,
        **kwargs
    ) -> DiscountCodeBasicUpdatePayload:
        """
        Updates an existing basic discount code via GraphQL mutation.


        Args:
            id: The GraphQL GID of the discount code node to update
            basic_code_discount: Parameter basicCodeDiscount
            **kwargs: Additional parameters

        Returns:
            DiscountCodeBasicUpdatePayload
        """
        params = {k: v for k, v in {
            "id": id,
            "basicCodeDiscount": basic_code_discount,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("discount_codes", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> DiscountCodeDeletePayload:
        """
        Deletes a discount code via GraphQL mutation.


        Args:
            id: The GraphQL GID of the discount code node to delete
            **kwargs: Additional parameters

        Returns:
            DiscountCodeDeletePayload
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("discount_codes", "delete", params)
        return result



    async def context_store_search(
        self,
        query: DiscountCodesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DiscountCodesSearchResult:
        """
        Search discount_codes records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DiscountCodesSearchFilter):
        - id: Unique identifier for the discount code
        - price_rule_id: Identifier of the parent price rule
        - code: Discount code string shoppers enter at checkout
        - usage_count: Number of times the code has been redeemed
        - created_at: ISO 8601 timestamp when the code was created
        - updated_at: ISO 8601 timestamp when the code was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DiscountCodesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("discount_codes", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DiscountCodesSearchResult(
            data=[
                DiscountCodesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
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



    async def create(
        self,
        input: CustomCollectionsCreateParamsInput,
        **kwargs
    ) -> CollectionCreatePayload:
        """
        Creates a new collection (custom or smart) via GraphQL mutation.
For smart collections, provide ruleSet with rules.


        Args:
            input: Parameter input
            **kwargs: Additional parameters

        Returns:
            CollectionCreatePayload
        """
        params = {k: v for k, v in {
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("custom_collections", "create", params)
        return result



    async def update(
        self,
        input: CustomCollectionsUpdateParamsInput,
        **kwargs
    ) -> CollectionUpdatePayload:
        """
        Updates an existing collection via GraphQL mutation.
Rule-based membership recompute is async for smart collections.


        Args:
            input: Parameter input
            **kwargs: Additional parameters

        Returns:
            CollectionUpdatePayload
        """
        params = {k: v for k, v in {
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("custom_collections", "update", params)
        return result



    async def delete(
        self,
        input: CustomCollectionsDeleteParamsInput,
        **kwargs
    ) -> CollectionDeletePayload:
        """
        Deletes a collection via GraphQL mutation.


        Args:
            input: Parameter input
            **kwargs: Additional parameters

        Returns:
            CollectionDeletePayload
        """
        params = {k: v for k, v in {
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("custom_collections", "delete", params)
        return result



    async def context_store_search(
        self,
        query: CustomCollectionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CustomCollectionsSearchResult:
        """
        Search custom_collections records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CustomCollectionsSearchFilter):
        - id: Unique identifier for the custom collection
        - handle: URL-friendly handle for the custom collection
        - title: Display title of the custom collection
        - sort_order: How products are sorted within the collection (e.g. `best-selling`)
        - published_scope: Publishing scope (`web` or `global`)
        - published_at: ISO 8601 timestamp when the collection was published
        - updated_at: ISO 8601 timestamp when the collection was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CustomCollectionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("custom_collections", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CustomCollectionsSearchResult(
            data=[
                CustomCollectionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
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



    async def context_store_search(
        self,
        query: SmartCollectionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SmartCollectionsSearchResult:
        """
        Search smart_collections records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SmartCollectionsSearchFilter):
        - id: Unique identifier for the smart collection
        - handle: URL-friendly handle for the smart collection
        - title: Display title of the smart collection
        - sort_order: How products are sorted within the collection
        - published_scope: Publishing scope (`web` or `global`)
        - published_at: ISO 8601 timestamp when the collection was published
        - updated_at: ISO 8601 timestamp when the collection was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SmartCollectionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("smart_collections", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SmartCollectionsSearchResult(
            data=[
                SmartCollectionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
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



    async def context_store_search(
        self,
        query: CollectsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CollectsSearchResult:
        """
        Search collects records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CollectsSearchFilter):
        - id: Unique identifier for the collect
        - collection_id: Identifier of the collection the product belongs to
        - product_id: Identifier of the product in the collection
        - position: Position of the product within the collection
        - created_at: ISO 8601 timestamp when the collect was created
        - updated_at: ISO 8601 timestamp when the collect was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CollectsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("collects", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CollectsSearchResult(
            data=[
                CollectsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
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



    async def create(
        self,
        input: DraftOrdersCreateParamsInput,
        **kwargs
    ) -> DraftOrderCreatePayload:
        """
        Creates a new draft order via GraphQL mutation.
Draft orders can be completed to become regular orders.


        Args:
            input: DraftOrderInput object
            **kwargs: Additional parameters

        Returns:
            DraftOrderCreatePayload
        """
        params = {k: v for k, v in {
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("draft_orders", "create", params)
        return result



    async def update(
        self,
        input: DraftOrdersUpdateParamsInput,
        id: str | None = None,
        **kwargs
    ) -> DraftOrderUpdatePayload:
        """
        Updates an existing draft order via GraphQL mutation.
Only open draft orders can be updated.


        Args:
            id: The GraphQL GID of the draft order to update
            input: DraftOrderInput object with updated fields
            **kwargs: Additional parameters

        Returns:
            DraftOrderUpdatePayload
        """
        params = {k: v for k, v in {
            "id": id,
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("draft_orders", "update", params)
        return result



    async def delete(
        self,
        input: DraftOrdersDeleteParamsInput,
        **kwargs
    ) -> DraftOrderDeletePayload:
        """
        Deletes a draft order via GraphQL mutation.
Only open draft orders can be deleted.


        Args:
            input: Parameter input
            **kwargs: Additional parameters

        Returns:
            DraftOrderDeletePayload
        """
        params = {k: v for k, v in {
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("draft_orders", "delete", params)
        return result



    async def context_store_search(
        self,
        query: DraftOrdersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DraftOrdersSearchResult:
        """
        Search draft_orders records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DraftOrdersSearchFilter):
        - id: Unique identifier for the draft order
        - name: Shopify-assigned display name for the draft order (e.g. `#D12345`)
        - email: Email address associated with the draft order
        - status: Status of the draft order (`open`, `invoice_sent`, `completed`)
        - currency: ISO 4217 currency code for the draft order totals
        - total_price: Total price of the draft order
        - order_id: Identifier of the completed order, if the draft has been completed
        - created_at: ISO 8601 timestamp when the draft order was created
        - updated_at: ISO 8601 timestamp when the draft order was last updated
        - completed_at: ISO 8601 timestamp when the draft order was completed, if applicable

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DraftOrdersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("draft_orders", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DraftOrdersSearchResult(
            data=[
                DraftOrdersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
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



    async def context_store_search(
        self,
        query: FulfillmentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> FulfillmentsSearchResult:
        """
        Search fulfillments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (FulfillmentsSearchFilter):
        - id: Unique identifier for the fulfillment
        - order_id: Identifier of the parent order
        - status: Fulfillment status (e.g. `pending`, `open`, `success`, `cancelled`)
        - shipment_status: Carrier shipment status (e.g. `delivered`, `in_transit`)
        - tracking_company: Name of the shipping carrier
        - tracking_number: Primary tracking number for the shipment
        - location_id: Identifier of the fulfilling location
        - created_at: ISO 8601 timestamp when the fulfillment was created
        - updated_at: ISO 8601 timestamp when the fulfillment was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            FulfillmentsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("fulfillments", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return FulfillmentsSearchResult(
            data=[
                FulfillmentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
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



    async def context_store_search(
        self,
        query: OrderRefundsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OrderRefundsSearchResult:
        """
        Search order_refunds records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OrderRefundsSearchFilter):
        - id: Unique identifier for the refund
        - order_id: Identifier of the refunded order
        - user_id: Identifier of the staff user who processed the refund
        - note: Merchant-provided note explaining the refund
        - created_at: ISO 8601 timestamp when the refund was created
        - processed_at: ISO 8601 timestamp when the refund was processed

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OrderRefundsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("order_refunds", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OrderRefundsSearchResult(
            data=[
                OrderRefundsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
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
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: TenderTransactionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TenderTransactionsSearchResult:
        """
        Search tender_transactions records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TenderTransactionsSearchFilter):
        - id: Unique identifier for the tender transaction
        - order_id: Identifier of the order the transaction belongs to
        - user_id: Identifier of the staff user who processed the transaction
        - amount: Amount of the transaction in the shop's currency
        - currency: ISO 4217 currency code for the transaction amount
        - payment_method: Payment method used (e.g. `credit_card`, `paypal`)
        - test: Whether the transaction was a test transaction
        - processed_at: ISO 8601 timestamp when the transaction was processed

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TenderTransactionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("tender_transactions", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TenderTransactionsSearchResult(
            data=[
                TenderTransactionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            meta=getattr(result, "meta", None)
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



    async def context_store_search(
        self,
        query: CountriesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CountriesSearchResult:
        """
        Search countries records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CountriesSearchFilter):
        - id: Unique identifier for the country tax row
        - name: Human-readable country name
        - code: ISO 3166-1 alpha-2 country code
        - tax_name: Localized name of the tax applied in this country

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CountriesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("countries", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CountriesSearchResult(
            data=[
                CountriesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
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



    async def context_store_search(
        self,
        query: MetafieldShopsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldShopsSearchResult:
        """
        Search metafield_shops records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldShopsSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldShopsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_shops", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldShopsSearchResult(
            data=[
                MetafieldShopsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

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
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: MetafieldCustomersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldCustomersSearchResult:
        """
        Search metafield_customers records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldCustomersSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldCustomersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_customers", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldCustomersSearchResult(
            data=[
                MetafieldCustomersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: MetafieldProductsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldProductsSearchResult:
        """
        Search metafield_products records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldProductsSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldProductsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_products", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldProductsSearchResult(
            data=[
                MetafieldProductsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: MetafieldOrdersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldOrdersSearchResult:
        """
        Search metafield_orders records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldOrdersSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldOrdersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_orders", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldOrdersSearchResult(
            data=[
                MetafieldOrdersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: MetafieldDraftOrdersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldDraftOrdersSearchResult:
        """
        Search metafield_draft_orders records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldDraftOrdersSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldDraftOrdersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_draft_orders", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldDraftOrdersSearchResult(
            data=[
                MetafieldDraftOrdersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: MetafieldLocationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldLocationsSearchResult:
        """
        Search metafield_locations records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldLocationsSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldLocationsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_locations", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldLocationsSearchResult(
            data=[
                MetafieldLocationsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: MetafieldProductVariantsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldProductVariantsSearchResult:
        """
        Search metafield_product_variants records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldProductVariantsSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldProductVariantsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_product_variants", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldProductVariantsSearchResult(
            data=[
                MetafieldProductVariantsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: MetafieldSmartCollectionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldSmartCollectionsSearchResult:
        """
        Search metafield_smart_collections records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldSmartCollectionsSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldSmartCollectionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_smart_collections", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldSmartCollectionsSearchResult(
            data=[
                MetafieldSmartCollectionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: MetafieldProductImagesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldProductImagesSearchResult:
        """
        Search metafield_product_images records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldProductImagesSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Namespace group for the metafield
        - key: Key of the metafield within its namespace
        - value: Serialized value stored in the metafield
        - type_: Shopify metafield type (e.g. `single_line_text_field`, `json`)
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the resource that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `product`, `customer`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldProductImagesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_product_images", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldProductImagesSearchResult(
            data=[
                MetafieldProductImagesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
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
            meta=getattr(result, "meta", None)
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
            meta=getattr(result, "meta", None)
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



    async def context_store_search(
        self,
        query: FulfillmentOrdersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> FulfillmentOrdersSearchResult:
        """
        Search fulfillment_orders records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (FulfillmentOrdersSearchFilter):
        - id: Unique identifier for the fulfillment order
        - order_id: Identifier of the parent order
        - shop_id: Identifier of the shop that owns the fulfillment order
        - assigned_location_id: Identifier of the location assigned to fulfill the order
        - status: Fulfillment order status (e.g. `open`, `in_progress`, `closed`)
        - request_status: Status of the fulfillment request (e.g. `unsubmitted`, `submitted`)
        - created_at: ISO 8601 timestamp when the fulfillment order was created
        - updated_at: ISO 8601 timestamp when the fulfillment order was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            FulfillmentOrdersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("fulfillment_orders", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return FulfillmentOrdersSearchResult(
            data=[
                FulfillmentOrdersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class PagesQuery:
    """
    Query class for Pages entity operations.
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
        published_status: str | None = None,
        **kwargs
    ) -> PagesListResult:
        """
        Returns a list of static pages for the store

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            created_at_min: Show pages created after date (ISO 8601 format)
            created_at_max: Show pages created before date (ISO 8601 format)
            updated_at_min: Show pages last updated after date (ISO 8601 format)
            updated_at_max: Show pages last updated before date (ISO 8601 format)
            published_status: Filter by published status (published, unpublished, any)
            **kwargs: Additional parameters

        Returns:
            PagesListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "created_at_min": created_at_min,
            "created_at_max": created_at_max,
            "updated_at_min": updated_at_min,
            "updated_at_max": updated_at_max,
            "published_status": published_status,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pages", "list", params)
        # Cast generic envelope to concrete typed result
        return PagesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        page_id: str,
        **kwargs
    ) -> Page:
        """
        Retrieves a single page by ID

        Args:
            page_id: The page ID
            **kwargs: Additional parameters

        Returns:
            Page
        """
        params = {k: v for k, v in {
            "page_id": page_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pages", "get", params)
        return result



    async def create(
        self,
        page: PagesCreateParamsPage,
        **kwargs
    ) -> PageCreatePayload:
        """
        Creates a new page on the online store via GraphQL mutation.


        Args:
            page: Parameter page
            **kwargs: Additional parameters

        Returns:
            PageCreatePayload
        """
        params = {k: v for k, v in {
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pages", "create", params)
        return result



    async def update(
        self,
        page: PagesUpdateParamsPage,
        id: str | None = None,
        **kwargs
    ) -> PageUpdatePayload:
        """
        Updates an existing page on the online store via GraphQL mutation.


        Args:
            id: The GraphQL GID of the page to update
            page: Parameter page
            **kwargs: Additional parameters

        Returns:
            PageUpdatePayload
        """
        params = {k: v for k, v in {
            "id": id,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pages", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> PageDeletePayload:
        """
        Deletes a page from the online store via GraphQL mutation.


        Args:
            id: The GraphQL GID of the page to delete
            **kwargs: Additional parameters

        Returns:
            PageDeletePayload
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("pages", "delete", params)
        return result



    async def context_store_search(
        self,
        query: PagesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> PagesSearchResult:
        """
        Search pages records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (PagesSearchFilter):
        - id: Unique identifier for the page
        - title: Title of the page
        - handle: URL-friendly handle for the page
        - author: Name of the page author
        - body_html: HTML content of the page
        - published_at: ISO 8601 timestamp when the page was published
        - created_at: ISO 8601 timestamp when the page was created
        - updated_at: ISO 8601 timestamp when the page was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            PagesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("pages", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return PagesSearchResult(
            data=[
                PagesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class BlogsQuery:
    """
    Query class for Blogs entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        **kwargs
    ) -> BlogsListResult:
        """
        Returns a list of blogs for the store

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            **kwargs: Additional parameters

        Returns:
            BlogsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("blogs", "list", params)
        # Cast generic envelope to concrete typed result
        return BlogsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        blog_id: str,
        **kwargs
    ) -> Blog:
        """
        Retrieves a single blog by ID

        Args:
            blog_id: The blog ID
            **kwargs: Additional parameters

        Returns:
            Blog
        """
        params = {k: v for k, v in {
            "blog_id": blog_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("blogs", "get", params)
        return result



    async def create(
        self,
        blog: BlogsCreateParamsBlog,
        **kwargs
    ) -> BlogCreatePayload:
        """
        Creates a new blog on the online store via GraphQL mutation.


        Args:
            blog: Parameter blog
            **kwargs: Additional parameters

        Returns:
            BlogCreatePayload
        """
        params = {k: v for k, v in {
            "blog": blog,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("blogs", "create", params)
        return result



    async def update(
        self,
        blog: BlogsUpdateParamsBlog,
        id: str | None = None,
        **kwargs
    ) -> BlogUpdatePayload:
        """
        Updates an existing blog via GraphQL mutation.


        Args:
            id: The GraphQL GID of the blog to update
            blog: Parameter blog
            **kwargs: Additional parameters

        Returns:
            BlogUpdatePayload
        """
        params = {k: v for k, v in {
            "id": id,
            "blog": blog,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("blogs", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> BlogDeletePayload:
        """
        Deletes a blog from the online store via GraphQL mutation.


        Args:
            id: The GraphQL GID of the blog to delete
            **kwargs: Additional parameters

        Returns:
            BlogDeletePayload
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("blogs", "delete", params)
        return result



    async def context_store_search(
        self,
        query: BlogsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BlogsSearchResult:
        """
        Search blogs records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BlogsSearchFilter):
        - id: Unique identifier for the blog
        - title: Title of the blog
        - handle: URL-friendly handle for the blog
        - commentable: Whether readers can post comments (no, moderate, yes)
        - tags: Comma-separated tags from the blog's articles
        - created_at: ISO 8601 timestamp when the blog was created
        - updated_at: ISO 8601 timestamp when the blog was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BlogsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("blogs", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return BlogsSearchResult(
            data=[
                BlogsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ArticlesQuery:
    """
    Query class for Articles entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        blog_id: str,
        limit: int | None = None,
        since_id: int | None = None,
        created_at_min: str | None = None,
        created_at_max: str | None = None,
        updated_at_min: str | None = None,
        updated_at_max: str | None = None,
        published_status: str | None = None,
        **kwargs
    ) -> ArticlesListResult:
        """
        Returns a list of articles from a specific blog

        Args:
            blog_id: The blog ID
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            created_at_min: Show articles created after date (ISO 8601 format)
            created_at_max: Show articles created before date (ISO 8601 format)
            updated_at_min: Show articles last updated after date (ISO 8601 format)
            updated_at_max: Show articles last updated before date (ISO 8601 format)
            published_status: Filter by published status (published, unpublished, any)
            **kwargs: Additional parameters

        Returns:
            ArticlesListResult
        """
        params = {k: v for k, v in {
            "blog_id": blog_id,
            "limit": limit,
            "since_id": since_id,
            "created_at_min": created_at_min,
            "created_at_max": created_at_max,
            "updated_at_min": updated_at_min,
            "updated_at_max": updated_at_max,
            "published_status": published_status,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "list", params)
        # Cast generic envelope to concrete typed result
        return ArticlesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        blog_id: str,
        article_id: str,
        **kwargs
    ) -> Article:
        """
        Retrieves a single article by ID from a blog

        Args:
            blog_id: The blog ID
            article_id: The article ID
            **kwargs: Additional parameters

        Returns:
            Article
        """
        params = {k: v for k, v in {
            "blog_id": blog_id,
            "article_id": article_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "get", params)
        return result



    async def create(
        self,
        article: ArticlesCreateParamsArticle,
        **kwargs
    ) -> ArticleCreatePayload:
        """
        Creates a new blog article via GraphQL mutation.


        Args:
            article: Parameter article
            **kwargs: Additional parameters

        Returns:
            ArticleCreatePayload
        """
        params = {k: v for k, v in {
            "article": article,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "create", params)
        return result



    async def update(
        self,
        article: ArticlesUpdateParamsArticle,
        id: str | None = None,
        **kwargs
    ) -> ArticleUpdatePayload:
        """
        Updates an existing blog article via GraphQL mutation.


        Args:
            id: The GraphQL GID of the article to update
            article: Parameter article
            **kwargs: Additional parameters

        Returns:
            ArticleUpdatePayload
        """
        params = {k: v for k, v in {
            "id": id,
            "article": article,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "update", params)
        return result



    async def delete(
        self,
        id: str | None = None,
        **kwargs
    ) -> ArticleDeletePayload:
        """
        Deletes a blog article via GraphQL mutation.


        Args:
            id: The GraphQL GID of the article to delete
            **kwargs: Additional parameters

        Returns:
            ArticleDeletePayload
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("articles", "delete", params)
        return result



    async def context_store_search(
        self,
        query: ArticlesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ArticlesSearchResult:
        """
        Search articles records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ArticlesSearchFilter):
        - id: Unique identifier for the article
        - title: Title of the article
        - handle: URL-friendly handle for the article
        - author: Name of the author of the article
        - blog_id: Identifier of the blog the article belongs to
        - body_html: HTML content of the article body
        - summary_html: Summary of the article in HTML
        - tags: Comma-separated list of tags for the article
        - published_at: ISO 8601 timestamp when the article was published
        - created_at: ISO 8601 timestamp when the article was created
        - updated_at: ISO 8601 timestamp when the article was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ArticlesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("articles", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ArticlesSearchResult(
            data=[
                ArticlesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class BalanceTransactionsQuery:
    """
    Query class for BalanceTransactions entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        payout_id: int | None = None,
        payout_status: str | None = None,
        **kwargs
    ) -> BalanceTransactionsListResult:
        """
        Returns a list of Shopify Payments balance transactions

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            payout_id: Filter to transactions in a specific payout
            payout_status: Filter by payout status
            **kwargs: Additional parameters

        Returns:
            BalanceTransactionsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "payout_id": payout_id,
            "payout_status": payout_status,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("balance_transactions", "list", params)
        # Cast generic envelope to concrete typed result
        return BalanceTransactionsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: BalanceTransactionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BalanceTransactionsSearchResult:
        """
        Search balance_transactions records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BalanceTransactionsSearchFilter):
        - id: Unique identifier of the balance transaction
        - type_: Type of the transaction (charge, refund, dispute, reserve, adjustment, credit, debit, payout, etc.)
        - amount: Gross amount of the transaction
        - fee: Total fees deducted from the transaction
        - net: Net amount of the transaction
        - currency: ISO 4217 currency code of the transaction
        - payout_id: Identifier of the payout the transaction was paid out in
        - payout_status: Status of the associated payout
        - source_type: Type of the resource that led to this transaction
        - source_order_id: Identifier of the source order, if applicable
        - processed_at: ISO 8601 timestamp when the transaction was processed

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BalanceTransactionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("balance_transactions", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return BalanceTransactionsSearchResult(
            data=[
                BalanceTransactionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class DisputesQuery:
    """
    Query class for Disputes entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        since_id: int | None = None,
        status: str | None = None,
        initiated_at: str | None = None,
        **kwargs
    ) -> DisputesListResult:
        """
        Returns a list of Shopify Payments disputes (chargebacks and inquiries)

        Args:
            limit: Maximum number of results to return (max 250)
            since_id: Restrict results to after the specified ID
            status: Filter by dispute status
            initiated_at: Filter by initiated date (ISO 8601 format)
            **kwargs: Additional parameters

        Returns:
            DisputesListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "since_id": since_id,
            "status": status,
            "initiated_at": initiated_at,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("disputes", "list", params)
        # Cast generic envelope to concrete typed result
        return DisputesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def get(
        self,
        dispute_id: str,
        **kwargs
    ) -> Dispute:
        """
        Retrieves a single Shopify Payments dispute by ID

        Args:
            dispute_id: The dispute ID
            **kwargs: Additional parameters

        Returns:
            Dispute
        """
        params = {k: v for k, v in {
            "dispute_id": dispute_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("disputes", "get", params)
        return result



    async def context_store_search(
        self,
        query: DisputesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> DisputesSearchResult:
        """
        Search disputes records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (DisputesSearchFilter):
        - id: Unique identifier for the dispute
        - order_id: Identifier of the order the dispute belongs to
        - type_: Whether the dispute is an inquiry or chargeback
        - amount: Disputed amount
        - currency: ISO 4217 currency code of the dispute amount
        - reason: Reason for the dispute provided by the cardholder's bank
        - network_reason_code: Network reason code from the cardholder's bank
        - status: Current state of the dispute (needs_response, under_review, charge_refunded, accepted, won, lost)
        - evidence_due_by: ISO 8601 deadline for evidence submission
        - initiated_at: ISO 8601 timestamp when the dispute was initiated
        - finalized_on: ISO 8601 timestamp when the dispute was resolved

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            DisputesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("disputes", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return DisputesSearchResult(
            data=[
                DisputesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MetafieldPagesQuery:
    """
    Query class for MetafieldPages entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_id: str,
        limit: int | None = None,
        **kwargs
    ) -> MetafieldPagesListResult:
        """
        Returns a list of metafields for a specific page

        Args:
            page_id: The page ID
            limit: Maximum number of results to return (max 250)
            **kwargs: Additional parameters

        Returns:
            MetafieldPagesListResult
        """
        params = {k: v for k, v in {
            "page_id": page_id,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_pages", "list", params)
        # Cast generic envelope to concrete typed result
        return MetafieldPagesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: MetafieldPagesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldPagesSearchResult:
        """
        Search metafield_pages records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldPagesSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Container namespace for the metafield
        - key: Identifier key for the metafield
        - value: The metafield value
        - type_: The metafield's information type
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the page that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `page`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldPagesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_pages", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldPagesSearchResult(
            data=[
                MetafieldPagesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MetafieldBlogsQuery:
    """
    Query class for MetafieldBlogs entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        blog_id: str,
        limit: int | None = None,
        **kwargs
    ) -> MetafieldBlogsListResult:
        """
        Returns a list of metafields for a specific blog

        Args:
            blog_id: The blog ID
            limit: Maximum number of results to return (max 250)
            **kwargs: Additional parameters

        Returns:
            MetafieldBlogsListResult
        """
        params = {k: v for k, v in {
            "blog_id": blog_id,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_blogs", "list", params)
        # Cast generic envelope to concrete typed result
        return MetafieldBlogsListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: MetafieldBlogsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldBlogsSearchResult:
        """
        Search metafield_blogs records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldBlogsSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Container namespace for the metafield
        - key: Identifier key for the metafield
        - value: The metafield value
        - type_: The metafield's information type
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the blog that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `blog`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldBlogsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_blogs", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldBlogsSearchResult(
            data=[
                MetafieldBlogsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MetafieldArticlesQuery:
    """
    Query class for MetafieldArticles entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        blog_id: str,
        article_id: str,
        limit: int | None = None,
        **kwargs
    ) -> MetafieldArticlesListResult:
        """
        Returns a list of metafields for a specific article

        Args:
            blog_id: The blog ID
            article_id: The article ID
            limit: Maximum number of results to return (max 250)
            **kwargs: Additional parameters

        Returns:
            MetafieldArticlesListResult
        """
        params = {k: v for k, v in {
            "blog_id": blog_id,
            "article_id": article_id,
            "limit": limit,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafield_articles", "list", params)
        # Cast generic envelope to concrete typed result
        return MetafieldArticlesListResult(
            data=result.data,
            meta=getattr(result, "meta", None)
        )



    async def context_store_search(
        self,
        query: MetafieldArticlesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MetafieldArticlesSearchResult:
        """
        Search metafield_articles records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MetafieldArticlesSearchFilter):
        - id: Unique identifier for the metafield
        - namespace: Container namespace for the metafield
        - key: Identifier key for the metafield
        - value: The metafield value
        - type_: The metafield's information type
        - description: Human-readable description of the metafield
        - owner_id: Identifier of the article that owns this metafield
        - owner_resource: Resource type that owns this metafield (e.g. `article`)
        - created_at: ISO 8601 timestamp when the metafield was created
        - updated_at: ISO 8601 timestamp when the metafield was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MetafieldArticlesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("metafield_articles", "context_store_search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MetafieldArticlesSearchResult(
            data=[
                MetafieldArticlesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class DraftOrderCompleteQuery:
    """
    Query class for DraftOrderComplete entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def update(
        self,
        id: str | None = None,
        payment_pending: bool | None = None,
        **kwargs
    ) -> DraftOrderCompletePayload:
        """
        Completes a draft order, converting it to a regular order via GraphQL mutation.


        Args:
            id: The GraphQL GID of the draft order to complete
            payment_pending: Whether payment is pending (true) or mark as paid (false/omit)
            **kwargs: Additional parameters

        Returns:
            DraftOrderCompletePayload
        """
        params = {k: v for k, v in {
            "id": id,
            "paymentPending": payment_pending,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("draft_order_complete", "update", params)
        return result



class InventorySetQuery:
    """
    Query class for InventorySet entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        input: InventorySetCreateParamsInput,
        **kwargs
    ) -> InventorySetQuantitiesPayload:
        """
        Sets absolute inventory quantities for items at locations via GraphQL mutation.
Uses the inventorySetQuantities mutation with a required reason and reference document.


        Args:
            input: Parameter input
            **kwargs: Additional parameters

        Returns:
            InventorySetQuantitiesPayload
        """
        params = {k: v for k, v in {
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("inventory_set", "create", params)
        return result



class InventoryAdjustQuery:
    """
    Query class for InventoryAdjust entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        input: InventoryAdjustCreateParamsInput,
        **kwargs
    ) -> InventoryAdjustQuantitiesPayload:
        """
        Adjusts inventory quantities relatively (add/subtract) for items at locations via GraphQL mutation.


        Args:
            input: Parameter input
            **kwargs: Additional parameters

        Returns:
            InventoryAdjustQuantitiesPayload
        """
        params = {k: v for k, v in {
            "input": input,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("inventory_adjust", "create", params)
        return result



class MetafieldsQuery:
    """
    Query class for Metafields entity operations.
    """

    def __init__(self, connector: ShopifyConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def create(
        self,
        metafields: list[MetafieldsCreateParamsMetafieldsItem],
        **kwargs
    ) -> MetafieldsSetPayload:
        """
        Sets (creates or updates) up to 25 metafields atomically via GraphQL mutation.
Works across all resource types (products, customers, orders, etc.).


        Args:
            metafields: List of metafields to set
            **kwargs: Additional parameters

        Returns:
            MetafieldsSetPayload
        """
        params = {k: v for k, v in {
            "metafields": metafields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafields", "create", params)
        return result



    async def delete(
        self,
        metafields: list[MetafieldsDeleteParamsMetafieldsItem],
        **kwargs
    ) -> MetafieldDeletePayload:
        """
        Deletes one or more metafields via GraphQL mutation.
Identifies metafields by ownerId + namespace + key.


        Args:
            metafields: List of metafield identifiers to delete
            **kwargs: Additional parameters

        Returns:
            MetafieldDeletePayload
        """
        params = {k: v for k, v in {
            "metafields": metafields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("metafields", "delete", params)
        return result


