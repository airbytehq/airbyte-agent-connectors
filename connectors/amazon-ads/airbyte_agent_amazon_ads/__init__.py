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
    AmazonAdsExecuteResult,
    AmazonAdsExecuteResultWithMeta,
    ProfilesListResult,
    PortfoliosListResult,
    SponsoredProductCampaignsListResult
)
from .types import (
    SponsoredProductCampaignsListParamsStatefilter,
    ProfilesListParams,
    ProfilesGetParams,
    PortfoliosListParams,
    PortfoliosGetParams,
    SponsoredProductCampaignsListParams,
    SponsoredProductCampaignsGetParams
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
    "AmazonAdsExecuteResult",
    "AmazonAdsExecuteResultWithMeta",
    "ProfilesListResult",
    "PortfoliosListResult",
    "SponsoredProductCampaignsListResult",
    "SponsoredProductCampaignsListParamsStatefilter",
    "ProfilesListParams",
    "ProfilesGetParams",
    "PortfoliosListParams",
    "PortfoliosGetParams",
    "SponsoredProductCampaignsListParams",
    "SponsoredProductCampaignsGetParams",
]