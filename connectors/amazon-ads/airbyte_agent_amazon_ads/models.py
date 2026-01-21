"""
Pydantic models for amazon-ads connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class AmazonAdsAuthConfig(BaseModel):
    """OAuth2 Authentication"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """The client ID of your Amazon Ads API application"""
    client_secret: str
    """The client secret of your Amazon Ads API application"""
    refresh_token: str
    """The refresh token obtained from the OAuth authorization flow"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Profile(BaseModel):
    """An advertising profile represents an advertiser's account in a specific marketplace.
Profiles are used to scope API calls and manage advertising campaigns.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    profile_id: Union[int, Any] = Field(default=None, alias="profileId")
    country_code: Union[str | None, Any] = Field(default=None, alias="countryCode")
    currency_code: Union[str | None, Any] = Field(default=None, alias="currencyCode")
    daily_budget: Union[float | None, Any] = Field(default=None, alias="dailyBudget")
    timezone: Union[str | None, Any] = Field(default=None)
    account_info: Union[Any, Any] = Field(default=None, alias="accountInfo")

class AccountInfo(BaseModel):
    """Information about the advertiser's account associated with a profile"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    marketplace_string_id: Union[str | None, Any] = Field(default=None, alias="marketplaceStringId")
    id: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    sub_type: Union[str | None, Any] = Field(default=None, alias="subType")
    valid_payment_method: Union[bool | None, Any] = Field(default=None, alias="validPaymentMethod")

class Portfolio(BaseModel):
    """A portfolio is a container for grouping campaigns together for organizational
and budget management purposes.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    portfolio_id: Union[Any, Any] = Field(default=None, alias="portfolioId")
    name: Union[str | None, Any] = Field(default=None)
    budget: Union[Any, Any] = Field(default=None)
    in_budget: Union[bool | None, Any] = Field(default=None, alias="inBudget")
    state: Union[str | None, Any] = Field(default=None)
    creation_date: Union[int | None, Any] = Field(default=None, alias="creationDate")
    last_updated_date: Union[int | None, Any] = Field(default=None, alias="lastUpdatedDate")
    serving_status: Union[str | None, Any] = Field(default=None, alias="servingStatus")

class PortfolioBudget(BaseModel):
    """Budget configuration for a portfolio"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[float | None, Any] = Field(default=None)
    currency_code: Union[str | None, Any] = Field(default=None, alias="currencyCode")
    policy: Union[str | None, Any] = Field(default=None)
    start_date: Union[str | None, Any] = Field(default=None, alias="startDate")
    end_date: Union[str | None, Any] = Field(default=None, alias="endDate")

class SponsoredProductCampaign(BaseModel):
    """A Sponsored Products campaign promotes individual product listings on Amazon.
Campaigns contain ad groups, which contain ads and targeting settings.
Note: The list endpoint (v3) and get endpoint (v2) return slightly different field formats.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    campaign_id: Union[Any, Any] = Field(default=None, alias="campaignId")
    portfolio_id: Union[Any, Any] = Field(default=None, alias="portfolioId")
    name: Union[str | None, Any] = Field(default=None)
    campaign_type: Union[str | None, Any] = Field(default=None, alias="campaignType")
    tags: Union[dict[str, Any] | None, Any] = Field(default=None)
    targeting_type: Union[str | None, Any] = Field(default=None, alias="targetingType")
    premium_bid_adjustment: Union[bool | None, Any] = Field(default=None, alias="premiumBidAdjustment")
    state: Union[str | None, Any] = Field(default=None)
    dynamic_bidding: Union[Any, Any] = Field(default=None, alias="dynamicBidding")
    bidding: Union[Any, Any] = Field(default=None)
    start_date: Union[str | None, Any] = Field(default=None, alias="startDate")
    end_date: Union[str | None, Any] = Field(default=None, alias="endDate")
    daily_budget: Union[float | None, Any] = Field(default=None, alias="dailyBudget")
    budget: Union[Any, Any] = Field(default=None)
    extended_data: Union[dict[str, Any] | None, Any] = Field(default=None, alias="extendedData")
    marketplace_budget_allocation: Union[str | None, Any] = Field(default=None, alias="marketplaceBudgetAllocation")
    off_amazon_settings: Union[dict[str, Any] | None, Any] = Field(default=None, alias="offAmazonSettings")

class DynamicBiddingPlacementbiddingItem(BaseModel):
    """Nested schema for DynamicBidding.placementBidding_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    placement: Union[str | None, Any] = Field(default=None, description="The placement type")
    """The placement type"""
    percentage: Union[int | None, Any] = Field(default=None, description="The bid adjustment percentage")
    """The bid adjustment percentage"""

class DynamicBidding(BaseModel):
    """Dynamic bidding settings for a campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    placement_bidding: Union[list[DynamicBiddingPlacementbiddingItem] | None, Any] = Field(default=None, alias="placementBidding")
    strategy: Union[str | None, Any] = Field(default=None)

class CampaignBudget(BaseModel):
    """Budget configuration for a campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    budget_type: Union[str | None, Any] = Field(default=None, alias="budgetType")
    budget: Union[float | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

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



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

ProfilesListResult = AmazonAdsExecuteResult[list[Profile]]
"""Result type for profiles.list operation."""

PortfoliosListResult = AmazonAdsExecuteResult[dict[str, Any]]
"""Result type for portfolios.list operation."""

SponsoredProductCampaignsListResult = AmazonAdsExecuteResult[dict[str, Any]]
"""Result type for sponsored_product_campaigns.list operation."""

