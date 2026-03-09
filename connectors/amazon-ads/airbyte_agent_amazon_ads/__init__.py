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
    AirbyteSearchMeta,
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
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig

__all__ = [
    "AmazonAdsConnector",
    "AirbyteAuthConfig",
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
    "AirbyteSearchMeta",
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