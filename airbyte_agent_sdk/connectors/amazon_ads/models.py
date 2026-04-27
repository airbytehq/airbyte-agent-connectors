"""
Pydantic models for amazon-ads connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
from typing import Optional

# Authentication configuration

class AmazonAdsAuthConfig(BaseModel):
    """OAuth2 Authentication"""

    model_config = ConfigDict(extra="forbid")

    client_id: Optional[str] = None
    """The client ID of your Amazon Ads API application"""
    client_secret: Optional[str] = None
    """The client secret of your Amazon Ads API application"""
    refresh_token: str
    """The refresh token obtained from the OAuth authorization flow"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Profile(BaseModel):
    """An advertising profile represents an advertiser's account in a specific marketplace.
Profiles are used to scope API calls and manage advertising campaigns.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    profile_id: int | None = Field(default=None, alias="profileId")
    country_code: str | None = Field(default=None, alias="countryCode")
    currency_code: str | None = Field(default=None, alias="currencyCode")
    daily_budget: float | None = Field(default=None, alias="dailyBudget")
    timezone: str | None = Field(default=None)
    account_info: Any | None = Field(default=None, alias="accountInfo")

class AccountInfo(BaseModel):
    """Information about the advertiser's account associated with a profile"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    marketplace_string_id: str | None = Field(default=None, alias="marketplaceStringId")
    id: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    name: str | None = Field(default=None)
    sub_type: str | None = Field(default=None, alias="subType")
    valid_payment_method: bool | None = Field(default=None, alias="validPaymentMethod")

class Portfolio(BaseModel):
    """A portfolio is a container for grouping campaigns together for organizational
and budget management purposes.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    portfolio_id: Any | None = Field(default=None, alias="portfolioId")
    name: str | None = Field(default=None)
    budget: Any | None = Field(default=None)
    in_budget: bool | None = Field(default=None, alias="inBudget")
    state: str | None = Field(default=None)
    creation_date: int | None = Field(default=None, alias="creationDate")
    last_updated_date: int | None = Field(default=None, alias="lastUpdatedDate")
    serving_status: str | None = Field(default=None, alias="servingStatus")

class PortfolioBudget(BaseModel):
    """Budget configuration for a portfolio"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: float | None = Field(default=None)
    currency_code: str | None = Field(default=None, alias="currencyCode")
    policy: str | None = Field(default=None)
    start_date: str | None = Field(default=None, alias="startDate")
    end_date: str | None = Field(default=None, alias="endDate")

class SponsoredProductCampaign(BaseModel):
    """A Sponsored Products campaign promotes individual product listings on Amazon.
Campaigns contain ad groups, which contain ads and targeting settings.
Note: The list endpoint (v3) and get endpoint (v2) return slightly different field formats.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign_id: Any | None = Field(default=None, alias="campaignId")
    portfolio_id: Any | None = Field(default=None, alias="portfolioId")
    name: str | None = Field(default=None)
    campaign_type: str | None = Field(default=None, alias="campaignType")
    tags: dict[str, Any] | None = Field(default=None)
    targeting_type: str | None = Field(default=None, alias="targetingType")
    premium_bid_adjustment: bool | None = Field(default=None, alias="premiumBidAdjustment")
    state: str | None = Field(default=None)
    dynamic_bidding: Any | None = Field(default=None, alias="dynamicBidding")
    bidding: Any | None = Field(default=None)
    start_date: str | None = Field(default=None, alias="startDate")
    end_date: str | None = Field(default=None, alias="endDate")
    daily_budget: float | None = Field(default=None, alias="dailyBudget")
    budget: Any | None = Field(default=None)
    extended_data: dict[str, Any] | None = Field(default=None, alias="extendedData")
    marketplace_budget_allocation: str | None = Field(default=None, alias="marketplaceBudgetAllocation")
    off_amazon_settings: dict[str, Any] | None = Field(default=None, alias="offAmazonSettings")

class DynamicBiddingPlacementbiddingItem(BaseModel):
    """Nested schema for DynamicBidding.placementBidding_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    placement: str | None | None = Field(default=None, description="The placement type")
    """The placement type"""
    percentage: int | None | None = Field(default=None, description="The bid adjustment percentage")
    """The bid adjustment percentage"""

class DynamicBidding(BaseModel):
    """Dynamic bidding settings for a campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    placement_bidding: list[DynamicBiddingPlacementbiddingItem] | None = Field(default=None, alias="placementBidding")
    strategy: str | None = Field(default=None)

class CampaignBudget(BaseModel):
    """Budget configuration for a campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    budget_type: str | None = Field(default=None, alias="budgetType")
    budget: float | None = Field(default=None)

class SponsoredProductAdGroup(BaseModel):
    """An ad group within a Sponsored Products campaign. Ad groups contain ads and targeting
settings and have a default bid that applies to all ads in the group.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group_id: Any | None = Field(default=None, alias="adGroupId")
    campaign_id: Any | None = Field(default=None, alias="campaignId")
    name: str | None = Field(default=None)
    state: str | None = Field(default=None)
    default_bid: float | None = Field(default=None, alias="defaultBid")
    extended_data: dict[str, Any] | None = Field(default=None, alias="extendedData")

class SponsoredProductKeyword(BaseModel):
    """A keyword within a Sponsored Products ad group. Keywords are used in manual targeting
campaigns to match shopper search queries.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    keyword_id: Any | None = Field(default=None, alias="keywordId")
    campaign_id: Any | None = Field(default=None, alias="campaignId")
    ad_group_id: Any | None = Field(default=None, alias="adGroupId")
    keyword_text: str | None = Field(default=None, alias="keywordText")
    match_type: str | None = Field(default=None, alias="matchType")
    state: str | None = Field(default=None)
    bid: float | None = Field(default=None)
    extended_data: dict[str, Any] | None = Field(default=None, alias="extendedData")

class SponsoredProductProductAd(BaseModel):
    """A product ad within a Sponsored Products ad group. Product ads associate an
advertised product (identified by ASIN or SKU) with an ad group.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_id: Any | None = Field(default=None, alias="adId")
    campaign_id: Any | None = Field(default=None, alias="campaignId")
    ad_group_id: Any | None = Field(default=None, alias="adGroupId")
    asin: str | None = Field(default=None)
    sku: str | None = Field(default=None)
    state: str | None = Field(default=None)
    extended_data: dict[str, Any] | None = Field(default=None, alias="extendedData")

class SponsoredProductTargetResolvedexpressionItem(BaseModel):
    """Nested schema for SponsoredProductTarget.resolvedExpression_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type", description="The resolved expression type")
    """The resolved expression type"""
    value: str | None | None = Field(default=None, description="The resolved expression value")
    """The resolved expression value"""

class SponsoredProductTargetExpressionItem(BaseModel):
    """Nested schema for SponsoredProductTarget.expression_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type", description="The expression type")
    """The expression type"""
    value: str | None | None = Field(default=None, description="The expression value")
    """The expression value"""

class SponsoredProductTarget(BaseModel):
    """A targeting clause within a Sponsored Products ad group. Targeting clauses define
product or category targeting for the ad group.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    target_id: Any | None = Field(default=None, alias="targetId")
    campaign_id: Any | None = Field(default=None, alias="campaignId")
    ad_group_id: Any | None = Field(default=None, alias="adGroupId")
    expression: list[SponsoredProductTargetExpressionItem] | None = Field(default=None)
    resolved_expression: list[SponsoredProductTargetResolvedexpressionItem] | None = Field(default=None, alias="resolvedExpression")
    expression_type: str | None = Field(default=None, alias="expressionType")
    state: str | None = Field(default=None)
    bid: float | None = Field(default=None)
    extended_data: dict[str, Any] | None = Field(default=None, alias="extendedData")

class SponsoredProductNegativeKeyword(BaseModel):
    """A negative keyword within a Sponsored Products ad group. Negative keywords prevent
ads from showing for specific search terms.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    keyword_id: Any | None = Field(default=None, alias="keywordId")
    campaign_id: Any | None = Field(default=None, alias="campaignId")
    ad_group_id: Any | None = Field(default=None, alias="adGroupId")
    keyword_text: str | None = Field(default=None, alias="keywordText")
    match_type: str | None = Field(default=None, alias="matchType")
    state: str | None = Field(default=None)
    extended_data: dict[str, Any] | None = Field(default=None, alias="extendedData")

class SponsoredProductNegativeTargetResolvedexpressionItem(BaseModel):
    """Nested schema for SponsoredProductNegativeTarget.resolvedExpression_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type", description="The resolved expression type")
    """The resolved expression type"""
    value: str | None | None = Field(default=None, description="The resolved expression value")
    """The resolved expression value"""

class SponsoredProductNegativeTargetExpressionItem(BaseModel):
    """Nested schema for SponsoredProductNegativeTarget.expression_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type", description="The expression type")
    """The expression type"""
    value: str | None | None = Field(default=None, description="The expression value")
    """The expression value"""

class SponsoredProductNegativeTarget(BaseModel):
    """A negative targeting clause within a Sponsored Products ad group. Negative targeting
clauses exclude specific products or categories from targeting.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    target_id: Any | None = Field(default=None, alias="targetId")
    campaign_id: Any | None = Field(default=None, alias="campaignId")
    ad_group_id: Any | None = Field(default=None, alias="adGroupId")
    expression: list[SponsoredProductNegativeTargetExpressionItem] | None = Field(default=None)
    resolved_expression: list[SponsoredProductNegativeTargetResolvedexpressionItem] | None = Field(default=None, alias="resolvedExpression")
    expression_type: str | None = Field(default=None, alias="expressionType")
    state: str | None = Field(default=None)
    extended_data: dict[str, Any] | None = Field(default=None, alias="extendedData")

class SponsoredBrandsCampaign(BaseModel):
    """A Sponsored Brands campaign. Sponsored Brands campaigns help drive discovery and sales
with creative ad experiences that appear in shopping results.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign_id: Any | None = Field(default=None, alias="campaignId")
    name: str | None = Field(default=None)
    state: str | None = Field(default=None)
    budget: float | None = Field(default=None)
    budget_type: str | None = Field(default=None, alias="budgetType")
    start_date: str | None = Field(default=None, alias="startDate")
    end_date: str | None = Field(default=None, alias="endDate")
    bid_optimization: bool | None = Field(default=None, alias="bidOptimization")
    bid_multiplier: float | None = Field(default=None, alias="bidMultiplier")
    portfolio_id: Any | None = Field(default=None, alias="portfolioId")
    cost_type: str | None = Field(default=None, alias="costType")
    product_location: str | None = Field(default=None, alias="productLocation")
    smart_default: str | None = Field(default=None, alias="smartDefault")
    tags: dict[str, Any] | None = Field(default=None)
    extended_data: dict[str, Any] | None = Field(default=None, alias="extendedData")

class SponsoredBrandsAdGroup(BaseModel):
    """An ad group within a Sponsored Brands campaign. Ad groups organize ads and targeting
within a campaign.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ad_group_id: Any | None = Field(default=None, alias="adGroupId")
    campaign_id: Any | None = Field(default=None, alias="campaignId")
    name: str | None = Field(default=None)
    state: str | None = Field(default=None)
    bid: float | None = Field(default=None)
    extended_data: dict[str, Any] | None = Field(default=None, alias="extendedData")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class PortfoliosListResultMeta(BaseModel):
    """Metadata for portfolios.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: str | None = Field(default=None)

class SponsoredProductCampaignsListResultMeta(BaseModel):
    """Metadata for sponsored_product_campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: str | None = Field(default=None)

class SponsoredProductAdGroupsListResultMeta(BaseModel):
    """Metadata for sponsored_product_ad_groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: str | None = Field(default=None)

class SponsoredProductKeywordsListResultMeta(BaseModel):
    """Metadata for sponsored_product_keywords.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: str | None = Field(default=None)

class SponsoredProductProductAdsListResultMeta(BaseModel):
    """Metadata for sponsored_product_product_ads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: str | None = Field(default=None)

class SponsoredProductTargetsListResultMeta(BaseModel):
    """Metadata for sponsored_product_targets.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: str | None = Field(default=None)

class SponsoredProductNegativeKeywordsListResultMeta(BaseModel):
    """Metadata for sponsored_product_negative_keywords.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: str | None = Field(default=None)

class SponsoredProductNegativeTargetsListResultMeta(BaseModel):
    """Metadata for sponsored_product_negative_targets.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: str | None = Field(default=None)

class SponsoredBrandsCampaignsListResultMeta(BaseModel):
    """Metadata for sponsored_brands_campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: str | None = Field(default=None)

class SponsoredBrandsAdGroupsListResultMeta(BaseModel):
    """Metadata for sponsored_brands_ad_groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_token: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class AmazonAdsCheckResult(BaseModel):
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


class AmazonAdsExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class AmazonAdsExecuteResultWithMeta(AmazonAdsExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class ProfilesSearchData(BaseModel):
    """Search result data for profiles entity."""
    model_config = ConfigDict(extra="allow")

    account_info: dict[str, Any] | None = None
    """"""
    country_code: str | None = None
    """"""
    currency_code: str | None = None
    """"""
    daily_budget: float | None = None
    """"""
    profile_id: int | None = None
    """"""
    timezone: str | None = None
    """"""


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

ProfilesSearchResult = AirbyteSearchResult[ProfilesSearchData]
"""Search result type for profiles entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

ProfilesListResult = AmazonAdsExecuteResult[list[Profile]]
"""Result type for profiles.list operation."""

PortfoliosListResult = AmazonAdsExecuteResultWithMeta[dict[str, Any], PortfoliosListResultMeta]
"""Result type for portfolios.list operation with data and metadata."""

SponsoredProductCampaignsListResult = AmazonAdsExecuteResultWithMeta[dict[str, Any], SponsoredProductCampaignsListResultMeta]
"""Result type for sponsored_product_campaigns.list operation with data and metadata."""

SponsoredProductAdGroupsListResult = AmazonAdsExecuteResultWithMeta[dict[str, Any], SponsoredProductAdGroupsListResultMeta]
"""Result type for sponsored_product_ad_groups.list operation with data and metadata."""

SponsoredProductKeywordsListResult = AmazonAdsExecuteResultWithMeta[dict[str, Any], SponsoredProductKeywordsListResultMeta]
"""Result type for sponsored_product_keywords.list operation with data and metadata."""

SponsoredProductProductAdsListResult = AmazonAdsExecuteResultWithMeta[dict[str, Any], SponsoredProductProductAdsListResultMeta]
"""Result type for sponsored_product_product_ads.list operation with data and metadata."""

SponsoredProductTargetsListResult = AmazonAdsExecuteResultWithMeta[dict[str, Any], SponsoredProductTargetsListResultMeta]
"""Result type for sponsored_product_targets.list operation with data and metadata."""

SponsoredProductNegativeKeywordsListResult = AmazonAdsExecuteResultWithMeta[dict[str, Any], SponsoredProductNegativeKeywordsListResultMeta]
"""Result type for sponsored_product_negative_keywords.list operation with data and metadata."""

SponsoredProductNegativeTargetsListResult = AmazonAdsExecuteResultWithMeta[dict[str, Any], SponsoredProductNegativeTargetsListResultMeta]
"""Result type for sponsored_product_negative_targets.list operation with data and metadata."""

SponsoredBrandsCampaignsListResult = AmazonAdsExecuteResultWithMeta[dict[str, Any], SponsoredBrandsCampaignsListResultMeta]
"""Result type for sponsored_brands_campaigns.list operation with data and metadata."""

SponsoredBrandsAdGroupsListResult = AmazonAdsExecuteResultWithMeta[dict[str, Any], SponsoredBrandsAdGroupsListResultMeta]
"""Result type for sponsored_brands_ad_groups.list operation with data and metadata."""

