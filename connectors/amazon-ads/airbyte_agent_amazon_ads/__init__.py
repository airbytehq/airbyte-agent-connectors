"""
Blessed Amazon-Ads connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import AmazonAdsConnector
from .models import (
    AmazonAdsAuthConfig,
    Profile,
    AccountInfo,
    Portfolio,
    PortfolioBudget,
    SponsoredProductCampaign,
    DynamicBiddingPlacementbiddingItem,
    DynamicBidding,
    CampaignBudget,
    AmazonAdsCheckResult,
    AmazonAdsExecuteResult,
    AmazonAdsExecuteResultWithMeta,
    ProfilesListResult,
    PortfoliosListResult,
    SponsoredProductCampaignsListResult,
    AirbyteSearchHit,
    AirbyteSearchResult,
    ProfilesSearchData,
    ProfilesSearchResult
)
from .types import (
    SponsoredProductCampaignsListParamsStatefilter,
    ProfilesListParams,
    ProfilesGetParams,
    PortfoliosListParams,
    PortfoliosGetParams,
    SponsoredProductCampaignsListParams,
    SponsoredProductCampaignsGetParams,
    AirbyteSearchParams,
    AirbyteSortOrder,
    ProfilesSearchFilter,
    ProfilesSearchQuery,
    ProfilesCondition
)

__all__ = [
    "AmazonAdsConnector",
    "AmazonAdsAuthConfig",
    "Profile",
    "AccountInfo",
    "Portfolio",
    "PortfolioBudget",
    "SponsoredProductCampaign",
    "DynamicBiddingPlacementbiddingItem",
    "DynamicBidding",
    "CampaignBudget",
    "AmazonAdsCheckResult",
    "AmazonAdsExecuteResult",
    "AmazonAdsExecuteResultWithMeta",
    "ProfilesListResult",
    "PortfoliosListResult",
    "SponsoredProductCampaignsListResult",
    "AirbyteSearchHit",
    "AirbyteSearchResult",
    "ProfilesSearchData",
    "ProfilesSearchResult",
    "SponsoredProductCampaignsListParamsStatefilter",
    "ProfilesListParams",
    "ProfilesGetParams",
    "PortfoliosListParams",
    "PortfoliosGetParams",
    "SponsoredProductCampaignsListParams",
    "SponsoredProductCampaignsGetParams",
    "AirbyteSearchParams",
    "AirbyteSortOrder",
    "ProfilesSearchFilter",
    "ProfilesSearchQuery",
    "ProfilesCondition",
]