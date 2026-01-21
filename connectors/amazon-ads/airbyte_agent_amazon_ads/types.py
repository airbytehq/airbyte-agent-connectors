"""
Type definitions for amazon-ads connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

class SponsoredProductCampaignsListParamsStatefilter(TypedDict):
    """Nested schema for SponsoredProductCampaignsListParams.stateFilter"""
    include: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class ProfilesListParams(TypedDict):
    """Parameters for profiles.list operation"""
    profile_type_filter: NotRequired[str]

class ProfilesGetParams(TypedDict):
    """Parameters for profiles.get operation"""
    profile_id: str

class PortfoliosListParams(TypedDict):
    """Parameters for portfolios.list operation"""
    include_extended_data_fields: NotRequired[str]

class PortfoliosGetParams(TypedDict):
    """Parameters for portfolios.get operation"""
    portfolio_id: str

class SponsoredProductCampaignsListParams(TypedDict):
    """Parameters for sponsored_product_campaigns.list operation"""
    state_filter: NotRequired[SponsoredProductCampaignsListParamsStatefilter]
    max_results: NotRequired[int]
    next_token: NotRequired[str]

class SponsoredProductCampaignsGetParams(TypedDict):
    """Parameters for sponsored_product_campaigns.get operation"""
    campaign_id: str

