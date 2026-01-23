"""
Type definitions for amazon-ads connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


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

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== PROFILES SEARCH TYPES =====

class ProfilesSearchFilter(TypedDict, total=False):
    """Available fields for filtering profiles search queries."""
    account_info: dict[str, Any] | None
    """"""
    country_code: str | None
    """"""
    currency_code: str | None
    """"""
    daily_budget: float | None
    """"""
    profile_id: int | None
    """"""
    timezone: str | None
    """"""


class ProfilesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account_info: list[dict[str, Any]]
    """"""
    country_code: list[str]
    """"""
    currency_code: list[str]
    """"""
    daily_budget: list[float]
    """"""
    profile_id: list[int]
    """"""
    timezone: list[str]
    """"""


class ProfilesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account_info: Any
    """"""
    country_code: Any
    """"""
    currency_code: Any
    """"""
    daily_budget: Any
    """"""
    profile_id: Any
    """"""
    timezone: Any
    """"""


class ProfilesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    account_info: str
    """"""
    country_code: str
    """"""
    currency_code: str
    """"""
    daily_budget: str
    """"""
    profile_id: str
    """"""
    timezone: str
    """"""


class ProfilesSortFilter(TypedDict, total=False):
    """Available fields for sorting profiles search results."""
    account_info: AirbyteSortOrder
    """"""
    country_code: AirbyteSortOrder
    """"""
    currency_code: AirbyteSortOrder
    """"""
    daily_budget: AirbyteSortOrder
    """"""
    profile_id: AirbyteSortOrder
    """"""
    timezone: AirbyteSortOrder
    """"""


# Entity-specific condition types for profiles
class ProfilesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProfilesSearchFilter


class ProfilesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProfilesSearchFilter


class ProfilesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProfilesSearchFilter


class ProfilesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProfilesSearchFilter


class ProfilesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProfilesSearchFilter


class ProfilesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProfilesSearchFilter


class ProfilesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProfilesStringFilter


class ProfilesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProfilesStringFilter


class ProfilesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProfilesStringFilter


class ProfilesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProfilesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProfilesInCondition = TypedDict("ProfilesInCondition", {"in": ProfilesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProfilesNotCondition = TypedDict("ProfilesNotCondition", {"not": "ProfilesCondition"}, total=False)
"""Negates the nested condition."""

ProfilesAndCondition = TypedDict("ProfilesAndCondition", {"and": "list[ProfilesCondition]"}, total=False)
"""True if all nested conditions are true."""

ProfilesOrCondition = TypedDict("ProfilesOrCondition", {"or": "list[ProfilesCondition]"}, total=False)
"""True if any nested condition is true."""

ProfilesAnyCondition = TypedDict("ProfilesAnyCondition", {"any": ProfilesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all profiles condition types
ProfilesCondition = (
    ProfilesEqCondition
    | ProfilesNeqCondition
    | ProfilesGtCondition
    | ProfilesGteCondition
    | ProfilesLtCondition
    | ProfilesLteCondition
    | ProfilesInCondition
    | ProfilesLikeCondition
    | ProfilesFuzzyCondition
    | ProfilesKeywordCondition
    | ProfilesContainsCondition
    | ProfilesNotCondition
    | ProfilesAndCondition
    | ProfilesOrCondition
    | ProfilesAnyCondition
)


class ProfilesSearchQuery(TypedDict, total=False):
    """Search query for profiles entity."""
    filter: ProfilesCondition
    sort: list[ProfilesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
