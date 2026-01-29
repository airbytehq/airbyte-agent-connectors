"""
Type definitions for facebook-marketing connector.
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

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    account_id: str
    fields: NotRequired[str]
    limit: NotRequired[int]
    after: NotRequired[str]

class AdSetsListParams(TypedDict):
    """Parameters for ad_sets.list operation"""
    account_id: str
    fields: NotRequired[str]
    limit: NotRequired[int]
    after: NotRequired[str]

class AdsListParams(TypedDict):
    """Parameters for ads.list operation"""
    account_id: str
    fields: NotRequired[str]
    limit: NotRequired[int]
    after: NotRequired[str]

class AdCreativesListParams(TypedDict):
    """Parameters for ad_creatives.list operation"""
    account_id: str
    fields: NotRequired[str]
    limit: NotRequired[int]
    after: NotRequired[str]

class AdsInsightsListParams(TypedDict):
    """Parameters for ads_insights.list operation"""
    account_id: str
    fields: NotRequired[str]
    date_preset: NotRequired[str]
    time_range: NotRequired[str]
    level: NotRequired[str]
    limit: NotRequired[int]
    after: NotRequired[str]

class CustomConversionsListParams(TypedDict):
    """Parameters for custom_conversions.list operation"""
    account_id: str
    fields: NotRequired[str]
    limit: NotRequired[int]
    after: NotRequired[str]

class ImagesListParams(TypedDict):
    """Parameters for images.list operation"""
    account_id: str
    fields: NotRequired[str]
    limit: NotRequired[int]
    after: NotRequired[str]

class VideosListParams(TypedDict):
    """Parameters for videos.list operation"""
    account_id: str
    fields: NotRequired[str]
    limit: NotRequired[int]
    after: NotRequired[str]

class CampaignsGetParams(TypedDict):
    """Parameters for campaigns.get operation"""
    campaign_id: str
    fields: NotRequired[str]

class AdSetsGetParams(TypedDict):
    """Parameters for ad_sets.get operation"""
    adset_id: str
    fields: NotRequired[str]

class AdsGetParams(TypedDict):
    """Parameters for ads.get operation"""
    ad_id: str
    fields: NotRequired[str]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== CAMPAIGNS SEARCH TYPES =====

class CampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaigns search queries."""
    id: str | None
    """Campaign ID"""
    name: str | None
    """Campaign name"""
    account_id: str | None
    """Ad account ID"""
    status: str | None
    """Campaign status"""
    effective_status: str | None
    """Effective status"""
    objective: str | None
    """Campaign objective"""
    daily_budget: float | None
    """Daily budget in account currency"""
    lifetime_budget: float | None
    """Lifetime budget"""
    budget_remaining: float | None
    """Remaining budget"""
    created_time: str | None
    """Campaign creation time"""
    start_time: str | None
    """Campaign start time"""
    stop_time: str | None
    """Campaign stop time"""
    updated_time: str | None
    """Last update time"""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Campaign ID"""
    name: list[str]
    """Campaign name"""
    account_id: list[str]
    """Ad account ID"""
    status: list[str]
    """Campaign status"""
    effective_status: list[str]
    """Effective status"""
    objective: list[str]
    """Campaign objective"""
    daily_budget: list[float]
    """Daily budget in account currency"""
    lifetime_budget: list[float]
    """Lifetime budget"""
    budget_remaining: list[float]
    """Remaining budget"""
    created_time: list[str]
    """Campaign creation time"""
    start_time: list[str]
    """Campaign start time"""
    stop_time: list[str]
    """Campaign stop time"""
    updated_time: list[str]
    """Last update time"""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Campaign ID"""
    name: Any
    """Campaign name"""
    account_id: Any
    """Ad account ID"""
    status: Any
    """Campaign status"""
    effective_status: Any
    """Effective status"""
    objective: Any
    """Campaign objective"""
    daily_budget: Any
    """Daily budget in account currency"""
    lifetime_budget: Any
    """Lifetime budget"""
    budget_remaining: Any
    """Remaining budget"""
    created_time: Any
    """Campaign creation time"""
    start_time: Any
    """Campaign start time"""
    stop_time: Any
    """Campaign stop time"""
    updated_time: Any
    """Last update time"""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Campaign ID"""
    name: str
    """Campaign name"""
    account_id: str
    """Ad account ID"""
    status: str
    """Campaign status"""
    effective_status: str
    """Effective status"""
    objective: str
    """Campaign objective"""
    daily_budget: str
    """Daily budget in account currency"""
    lifetime_budget: str
    """Lifetime budget"""
    budget_remaining: str
    """Remaining budget"""
    created_time: str
    """Campaign creation time"""
    start_time: str
    """Campaign start time"""
    stop_time: str
    """Campaign stop time"""
    updated_time: str
    """Last update time"""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    id: AirbyteSortOrder
    """Campaign ID"""
    name: AirbyteSortOrder
    """Campaign name"""
    account_id: AirbyteSortOrder
    """Ad account ID"""
    status: AirbyteSortOrder
    """Campaign status"""
    effective_status: AirbyteSortOrder
    """Effective status"""
    objective: AirbyteSortOrder
    """Campaign objective"""
    daily_budget: AirbyteSortOrder
    """Daily budget in account currency"""
    lifetime_budget: AirbyteSortOrder
    """Lifetime budget"""
    budget_remaining: AirbyteSortOrder
    """Remaining budget"""
    created_time: AirbyteSortOrder
    """Campaign creation time"""
    start_time: AirbyteSortOrder
    """Campaign start time"""
    stop_time: AirbyteSortOrder
    """Campaign stop time"""
    updated_time: AirbyteSortOrder
    """Last update time"""


# Entity-specific condition types for campaigns
class CampaignsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CampaignsSearchFilter


class CampaignsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CampaignsSearchFilter


class CampaignsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CampaignsSearchFilter


class CampaignsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CampaignsSearchFilter


class CampaignsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CampaignsSearchFilter


class CampaignsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CampaignsSearchFilter


class CampaignsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CampaignsStringFilter


class CampaignsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CampaignsStringFilter


class CampaignsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CampaignsStringFilter


class CampaignsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CampaignsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CampaignsInCondition = TypedDict("CampaignsInCondition", {"in": CampaignsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CampaignsNotCondition = TypedDict("CampaignsNotCondition", {"not": "CampaignsCondition"}, total=False)
"""Negates the nested condition."""

CampaignsAndCondition = TypedDict("CampaignsAndCondition", {"and": "list[CampaignsCondition]"}, total=False)
"""True if all nested conditions are true."""

CampaignsOrCondition = TypedDict("CampaignsOrCondition", {"or": "list[CampaignsCondition]"}, total=False)
"""True if any nested condition is true."""

CampaignsAnyCondition = TypedDict("CampaignsAnyCondition", {"any": CampaignsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all campaigns condition types
CampaignsCondition = (
    CampaignsEqCondition
    | CampaignsNeqCondition
    | CampaignsGtCondition
    | CampaignsGteCondition
    | CampaignsLtCondition
    | CampaignsLteCondition
    | CampaignsInCondition
    | CampaignsLikeCondition
    | CampaignsFuzzyCondition
    | CampaignsKeywordCondition
    | CampaignsContainsCondition
    | CampaignsNotCondition
    | CampaignsAndCondition
    | CampaignsOrCondition
    | CampaignsAnyCondition
)


class CampaignsSearchQuery(TypedDict, total=False):
    """Search query for campaigns entity."""
    filter: CampaignsCondition
    sort: list[CampaignsSortFilter]


# ===== AD_SETS SEARCH TYPES =====

class AdSetsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_sets search queries."""
    id: str | None
    """Ad Set ID"""
    name: str | None
    """Ad Set name"""
    account_id: str | None
    """Ad account ID"""
    campaign_id: str | None
    """Parent campaign ID"""
    effective_status: str | None
    """Effective status"""
    daily_budget: float | None
    """Daily budget"""
    lifetime_budget: float | None
    """Lifetime budget"""
    budget_remaining: float | None
    """Remaining budget"""
    bid_amount: float | None
    """Bid amount"""
    bid_strategy: str | None
    """Bid strategy"""
    created_time: str | None
    """Ad set creation time"""
    start_time: str | None
    """Ad set start time"""
    end_time: str | None
    """Ad set end time"""
    updated_time: str | None
    """Last update time"""


class AdSetsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Ad Set ID"""
    name: list[str]
    """Ad Set name"""
    account_id: list[str]
    """Ad account ID"""
    campaign_id: list[str]
    """Parent campaign ID"""
    effective_status: list[str]
    """Effective status"""
    daily_budget: list[float]
    """Daily budget"""
    lifetime_budget: list[float]
    """Lifetime budget"""
    budget_remaining: list[float]
    """Remaining budget"""
    bid_amount: list[float]
    """Bid amount"""
    bid_strategy: list[str]
    """Bid strategy"""
    created_time: list[str]
    """Ad set creation time"""
    start_time: list[str]
    """Ad set start time"""
    end_time: list[str]
    """Ad set end time"""
    updated_time: list[str]
    """Last update time"""


class AdSetsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Ad Set ID"""
    name: Any
    """Ad Set name"""
    account_id: Any
    """Ad account ID"""
    campaign_id: Any
    """Parent campaign ID"""
    effective_status: Any
    """Effective status"""
    daily_budget: Any
    """Daily budget"""
    lifetime_budget: Any
    """Lifetime budget"""
    budget_remaining: Any
    """Remaining budget"""
    bid_amount: Any
    """Bid amount"""
    bid_strategy: Any
    """Bid strategy"""
    created_time: Any
    """Ad set creation time"""
    start_time: Any
    """Ad set start time"""
    end_time: Any
    """Ad set end time"""
    updated_time: Any
    """Last update time"""


class AdSetsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Ad Set ID"""
    name: str
    """Ad Set name"""
    account_id: str
    """Ad account ID"""
    campaign_id: str
    """Parent campaign ID"""
    effective_status: str
    """Effective status"""
    daily_budget: str
    """Daily budget"""
    lifetime_budget: str
    """Lifetime budget"""
    budget_remaining: str
    """Remaining budget"""
    bid_amount: str
    """Bid amount"""
    bid_strategy: str
    """Bid strategy"""
    created_time: str
    """Ad set creation time"""
    start_time: str
    """Ad set start time"""
    end_time: str
    """Ad set end time"""
    updated_time: str
    """Last update time"""


class AdSetsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_sets search results."""
    id: AirbyteSortOrder
    """Ad Set ID"""
    name: AirbyteSortOrder
    """Ad Set name"""
    account_id: AirbyteSortOrder
    """Ad account ID"""
    campaign_id: AirbyteSortOrder
    """Parent campaign ID"""
    effective_status: AirbyteSortOrder
    """Effective status"""
    daily_budget: AirbyteSortOrder
    """Daily budget"""
    lifetime_budget: AirbyteSortOrder
    """Lifetime budget"""
    budget_remaining: AirbyteSortOrder
    """Remaining budget"""
    bid_amount: AirbyteSortOrder
    """Bid amount"""
    bid_strategy: AirbyteSortOrder
    """Bid strategy"""
    created_time: AirbyteSortOrder
    """Ad set creation time"""
    start_time: AirbyteSortOrder
    """Ad set start time"""
    end_time: AirbyteSortOrder
    """Ad set end time"""
    updated_time: AirbyteSortOrder
    """Last update time"""


# Entity-specific condition types for ad_sets
class AdSetsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdSetsSearchFilter


class AdSetsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdSetsSearchFilter


class AdSetsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdSetsSearchFilter


class AdSetsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdSetsSearchFilter


class AdSetsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdSetsSearchFilter


class AdSetsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdSetsSearchFilter


class AdSetsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdSetsStringFilter


class AdSetsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdSetsStringFilter


class AdSetsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdSetsStringFilter


class AdSetsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdSetsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdSetsInCondition = TypedDict("AdSetsInCondition", {"in": AdSetsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdSetsNotCondition = TypedDict("AdSetsNotCondition", {"not": "AdSetsCondition"}, total=False)
"""Negates the nested condition."""

AdSetsAndCondition = TypedDict("AdSetsAndCondition", {"and": "list[AdSetsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdSetsOrCondition = TypedDict("AdSetsOrCondition", {"or": "list[AdSetsCondition]"}, total=False)
"""True if any nested condition is true."""

AdSetsAnyCondition = TypedDict("AdSetsAnyCondition", {"any": AdSetsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_sets condition types
AdSetsCondition = (
    AdSetsEqCondition
    | AdSetsNeqCondition
    | AdSetsGtCondition
    | AdSetsGteCondition
    | AdSetsLtCondition
    | AdSetsLteCondition
    | AdSetsInCondition
    | AdSetsLikeCondition
    | AdSetsFuzzyCondition
    | AdSetsKeywordCondition
    | AdSetsContainsCondition
    | AdSetsNotCondition
    | AdSetsAndCondition
    | AdSetsOrCondition
    | AdSetsAnyCondition
)


class AdSetsSearchQuery(TypedDict, total=False):
    """Search query for ad_sets entity."""
    filter: AdSetsCondition
    sort: list[AdSetsSortFilter]


# ===== ADS SEARCH TYPES =====

class AdsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ads search queries."""
    id: str | None
    """Ad ID"""
    name: str | None
    """Ad name"""
    account_id: str | None
    """Ad account ID"""
    adset_id: str | None
    """Parent ad set ID"""
    campaign_id: str | None
    """Parent campaign ID"""
    status: str | None
    """Ad status"""
    effective_status: str | None
    """Effective status"""
    created_time: str | None
    """Ad creation time"""
    updated_time: str | None
    """Last update time"""


class AdsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Ad ID"""
    name: list[str]
    """Ad name"""
    account_id: list[str]
    """Ad account ID"""
    adset_id: list[str]
    """Parent ad set ID"""
    campaign_id: list[str]
    """Parent campaign ID"""
    status: list[str]
    """Ad status"""
    effective_status: list[str]
    """Effective status"""
    created_time: list[str]
    """Ad creation time"""
    updated_time: list[str]
    """Last update time"""


class AdsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Ad ID"""
    name: Any
    """Ad name"""
    account_id: Any
    """Ad account ID"""
    adset_id: Any
    """Parent ad set ID"""
    campaign_id: Any
    """Parent campaign ID"""
    status: Any
    """Ad status"""
    effective_status: Any
    """Effective status"""
    created_time: Any
    """Ad creation time"""
    updated_time: Any
    """Last update time"""


class AdsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Ad ID"""
    name: str
    """Ad name"""
    account_id: str
    """Ad account ID"""
    adset_id: str
    """Parent ad set ID"""
    campaign_id: str
    """Parent campaign ID"""
    status: str
    """Ad status"""
    effective_status: str
    """Effective status"""
    created_time: str
    """Ad creation time"""
    updated_time: str
    """Last update time"""


class AdsSortFilter(TypedDict, total=False):
    """Available fields for sorting ads search results."""
    id: AirbyteSortOrder
    """Ad ID"""
    name: AirbyteSortOrder
    """Ad name"""
    account_id: AirbyteSortOrder
    """Ad account ID"""
    adset_id: AirbyteSortOrder
    """Parent ad set ID"""
    campaign_id: AirbyteSortOrder
    """Parent campaign ID"""
    status: AirbyteSortOrder
    """Ad status"""
    effective_status: AirbyteSortOrder
    """Effective status"""
    created_time: AirbyteSortOrder
    """Ad creation time"""
    updated_time: AirbyteSortOrder
    """Last update time"""


# Entity-specific condition types for ads
class AdsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdsSearchFilter


class AdsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdsSearchFilter


class AdsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdsSearchFilter


class AdsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdsSearchFilter


class AdsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdsSearchFilter


class AdsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdsSearchFilter


class AdsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdsStringFilter


class AdsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdsStringFilter


class AdsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdsStringFilter


class AdsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdsInCondition = TypedDict("AdsInCondition", {"in": AdsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdsNotCondition = TypedDict("AdsNotCondition", {"not": "AdsCondition"}, total=False)
"""Negates the nested condition."""

AdsAndCondition = TypedDict("AdsAndCondition", {"and": "list[AdsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdsOrCondition = TypedDict("AdsOrCondition", {"or": "list[AdsCondition]"}, total=False)
"""True if any nested condition is true."""

AdsAnyCondition = TypedDict("AdsAnyCondition", {"any": AdsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ads condition types
AdsCondition = (
    AdsEqCondition
    | AdsNeqCondition
    | AdsGtCondition
    | AdsGteCondition
    | AdsLtCondition
    | AdsLteCondition
    | AdsInCondition
    | AdsLikeCondition
    | AdsFuzzyCondition
    | AdsKeywordCondition
    | AdsContainsCondition
    | AdsNotCondition
    | AdsAndCondition
    | AdsOrCondition
    | AdsAnyCondition
)


class AdsSearchQuery(TypedDict, total=False):
    """Search query for ads entity."""
    filter: AdsCondition
    sort: list[AdsSortFilter]


# ===== AD_CREATIVES SEARCH TYPES =====

class AdCreativesSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_creatives search queries."""
    id: str | None
    """Ad Creative ID"""
    name: str | None
    """Ad Creative name"""
    account_id: str | None
    """Ad account ID"""
    body: str | None
    """Ad body text"""
    title: str | None
    """Ad title"""
    status: str | None
    """Creative status"""
    image_url: str | None
    """Image URL"""
    thumbnail_url: str | None
    """Thumbnail URL"""
    link_url: str | None
    """Link URL"""
    call_to_action_type: str | None
    """Call to action type"""


class AdCreativesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Ad Creative ID"""
    name: list[str]
    """Ad Creative name"""
    account_id: list[str]
    """Ad account ID"""
    body: list[str]
    """Ad body text"""
    title: list[str]
    """Ad title"""
    status: list[str]
    """Creative status"""
    image_url: list[str]
    """Image URL"""
    thumbnail_url: list[str]
    """Thumbnail URL"""
    link_url: list[str]
    """Link URL"""
    call_to_action_type: list[str]
    """Call to action type"""


class AdCreativesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Ad Creative ID"""
    name: Any
    """Ad Creative name"""
    account_id: Any
    """Ad account ID"""
    body: Any
    """Ad body text"""
    title: Any
    """Ad title"""
    status: Any
    """Creative status"""
    image_url: Any
    """Image URL"""
    thumbnail_url: Any
    """Thumbnail URL"""
    link_url: Any
    """Link URL"""
    call_to_action_type: Any
    """Call to action type"""


class AdCreativesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Ad Creative ID"""
    name: str
    """Ad Creative name"""
    account_id: str
    """Ad account ID"""
    body: str
    """Ad body text"""
    title: str
    """Ad title"""
    status: str
    """Creative status"""
    image_url: str
    """Image URL"""
    thumbnail_url: str
    """Thumbnail URL"""
    link_url: str
    """Link URL"""
    call_to_action_type: str
    """Call to action type"""


class AdCreativesSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_creatives search results."""
    id: AirbyteSortOrder
    """Ad Creative ID"""
    name: AirbyteSortOrder
    """Ad Creative name"""
    account_id: AirbyteSortOrder
    """Ad account ID"""
    body: AirbyteSortOrder
    """Ad body text"""
    title: AirbyteSortOrder
    """Ad title"""
    status: AirbyteSortOrder
    """Creative status"""
    image_url: AirbyteSortOrder
    """Image URL"""
    thumbnail_url: AirbyteSortOrder
    """Thumbnail URL"""
    link_url: AirbyteSortOrder
    """Link URL"""
    call_to_action_type: AirbyteSortOrder
    """Call to action type"""


# Entity-specific condition types for ad_creatives
class AdCreativesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdCreativesSearchFilter


class AdCreativesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdCreativesSearchFilter


class AdCreativesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdCreativesSearchFilter


class AdCreativesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdCreativesSearchFilter


class AdCreativesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdCreativesSearchFilter


class AdCreativesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdCreativesSearchFilter


class AdCreativesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdCreativesStringFilter


class AdCreativesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdCreativesStringFilter


class AdCreativesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdCreativesStringFilter


class AdCreativesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdCreativesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdCreativesInCondition = TypedDict("AdCreativesInCondition", {"in": AdCreativesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdCreativesNotCondition = TypedDict("AdCreativesNotCondition", {"not": "AdCreativesCondition"}, total=False)
"""Negates the nested condition."""

AdCreativesAndCondition = TypedDict("AdCreativesAndCondition", {"and": "list[AdCreativesCondition]"}, total=False)
"""True if all nested conditions are true."""

AdCreativesOrCondition = TypedDict("AdCreativesOrCondition", {"or": "list[AdCreativesCondition]"}, total=False)
"""True if any nested condition is true."""

AdCreativesAnyCondition = TypedDict("AdCreativesAnyCondition", {"any": AdCreativesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_creatives condition types
AdCreativesCondition = (
    AdCreativesEqCondition
    | AdCreativesNeqCondition
    | AdCreativesGtCondition
    | AdCreativesGteCondition
    | AdCreativesLtCondition
    | AdCreativesLteCondition
    | AdCreativesInCondition
    | AdCreativesLikeCondition
    | AdCreativesFuzzyCondition
    | AdCreativesKeywordCondition
    | AdCreativesContainsCondition
    | AdCreativesNotCondition
    | AdCreativesAndCondition
    | AdCreativesOrCondition
    | AdCreativesAnyCondition
)


class AdCreativesSearchQuery(TypedDict, total=False):
    """Search query for ad_creatives entity."""
    filter: AdCreativesCondition
    sort: list[AdCreativesSortFilter]


# ===== ADS_INSIGHTS SEARCH TYPES =====

class AdsInsightsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ads_insights search queries."""
    account_id: str | None
    """Ad account ID"""
    account_name: str | None
    """Ad account name"""
    campaign_id: str | None
    """Campaign ID"""
    campaign_name: str | None
    """Campaign name"""
    adset_id: str | None
    """Ad set ID"""
    adset_name: str | None
    """Ad set name"""
    ad_id: str | None
    """Ad ID"""
    ad_name: str | None
    """Ad name"""
    clicks: int | None
    """Number of clicks"""
    impressions: int | None
    """Number of impressions"""
    reach: int | None
    """Number of unique people reached"""
    spend: float | None
    """Amount spent"""
    cpc: float | None
    """Cost per click"""
    cpm: float | None
    """Cost per 1000 impressions"""
    ctr: float | None
    """Click-through rate"""
    date_start: str | None
    """Start date of the reporting period"""
    date_stop: str | None
    """End date of the reporting period"""


class AdsInsightsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account_id: list[str]
    """Ad account ID"""
    account_name: list[str]
    """Ad account name"""
    campaign_id: list[str]
    """Campaign ID"""
    campaign_name: list[str]
    """Campaign name"""
    adset_id: list[str]
    """Ad set ID"""
    adset_name: list[str]
    """Ad set name"""
    ad_id: list[str]
    """Ad ID"""
    ad_name: list[str]
    """Ad name"""
    clicks: list[int]
    """Number of clicks"""
    impressions: list[int]
    """Number of impressions"""
    reach: list[int]
    """Number of unique people reached"""
    spend: list[float]
    """Amount spent"""
    cpc: list[float]
    """Cost per click"""
    cpm: list[float]
    """Cost per 1000 impressions"""
    ctr: list[float]
    """Click-through rate"""
    date_start: list[str]
    """Start date of the reporting period"""
    date_stop: list[str]
    """End date of the reporting period"""


class AdsInsightsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account_id: Any
    """Ad account ID"""
    account_name: Any
    """Ad account name"""
    campaign_id: Any
    """Campaign ID"""
    campaign_name: Any
    """Campaign name"""
    adset_id: Any
    """Ad set ID"""
    adset_name: Any
    """Ad set name"""
    ad_id: Any
    """Ad ID"""
    ad_name: Any
    """Ad name"""
    clicks: Any
    """Number of clicks"""
    impressions: Any
    """Number of impressions"""
    reach: Any
    """Number of unique people reached"""
    spend: Any
    """Amount spent"""
    cpc: Any
    """Cost per click"""
    cpm: Any
    """Cost per 1000 impressions"""
    ctr: Any
    """Click-through rate"""
    date_start: Any
    """Start date of the reporting period"""
    date_stop: Any
    """End date of the reporting period"""


class AdsInsightsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    account_id: str
    """Ad account ID"""
    account_name: str
    """Ad account name"""
    campaign_id: str
    """Campaign ID"""
    campaign_name: str
    """Campaign name"""
    adset_id: str
    """Ad set ID"""
    adset_name: str
    """Ad set name"""
    ad_id: str
    """Ad ID"""
    ad_name: str
    """Ad name"""
    clicks: str
    """Number of clicks"""
    impressions: str
    """Number of impressions"""
    reach: str
    """Number of unique people reached"""
    spend: str
    """Amount spent"""
    cpc: str
    """Cost per click"""
    cpm: str
    """Cost per 1000 impressions"""
    ctr: str
    """Click-through rate"""
    date_start: str
    """Start date of the reporting period"""
    date_stop: str
    """End date of the reporting period"""


class AdsInsightsSortFilter(TypedDict, total=False):
    """Available fields for sorting ads_insights search results."""
    account_id: AirbyteSortOrder
    """Ad account ID"""
    account_name: AirbyteSortOrder
    """Ad account name"""
    campaign_id: AirbyteSortOrder
    """Campaign ID"""
    campaign_name: AirbyteSortOrder
    """Campaign name"""
    adset_id: AirbyteSortOrder
    """Ad set ID"""
    adset_name: AirbyteSortOrder
    """Ad set name"""
    ad_id: AirbyteSortOrder
    """Ad ID"""
    ad_name: AirbyteSortOrder
    """Ad name"""
    clicks: AirbyteSortOrder
    """Number of clicks"""
    impressions: AirbyteSortOrder
    """Number of impressions"""
    reach: AirbyteSortOrder
    """Number of unique people reached"""
    spend: AirbyteSortOrder
    """Amount spent"""
    cpc: AirbyteSortOrder
    """Cost per click"""
    cpm: AirbyteSortOrder
    """Cost per 1000 impressions"""
    ctr: AirbyteSortOrder
    """Click-through rate"""
    date_start: AirbyteSortOrder
    """Start date of the reporting period"""
    date_stop: AirbyteSortOrder
    """End date of the reporting period"""


# Entity-specific condition types for ads_insights
class AdsInsightsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdsInsightsSearchFilter


class AdsInsightsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdsInsightsSearchFilter


class AdsInsightsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdsInsightsSearchFilter


class AdsInsightsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdsInsightsSearchFilter


class AdsInsightsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdsInsightsSearchFilter


class AdsInsightsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdsInsightsSearchFilter


class AdsInsightsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdsInsightsStringFilter


class AdsInsightsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdsInsightsStringFilter


class AdsInsightsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdsInsightsStringFilter


class AdsInsightsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdsInsightsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdsInsightsInCondition = TypedDict("AdsInsightsInCondition", {"in": AdsInsightsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdsInsightsNotCondition = TypedDict("AdsInsightsNotCondition", {"not": "AdsInsightsCondition"}, total=False)
"""Negates the nested condition."""

AdsInsightsAndCondition = TypedDict("AdsInsightsAndCondition", {"and": "list[AdsInsightsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdsInsightsOrCondition = TypedDict("AdsInsightsOrCondition", {"or": "list[AdsInsightsCondition]"}, total=False)
"""True if any nested condition is true."""

AdsInsightsAnyCondition = TypedDict("AdsInsightsAnyCondition", {"any": AdsInsightsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ads_insights condition types
AdsInsightsCondition = (
    AdsInsightsEqCondition
    | AdsInsightsNeqCondition
    | AdsInsightsGtCondition
    | AdsInsightsGteCondition
    | AdsInsightsLtCondition
    | AdsInsightsLteCondition
    | AdsInsightsInCondition
    | AdsInsightsLikeCondition
    | AdsInsightsFuzzyCondition
    | AdsInsightsKeywordCondition
    | AdsInsightsContainsCondition
    | AdsInsightsNotCondition
    | AdsInsightsAndCondition
    | AdsInsightsOrCondition
    | AdsInsightsAnyCondition
)


class AdsInsightsSearchQuery(TypedDict, total=False):
    """Search query for ads_insights entity."""
    filter: AdsInsightsCondition
    sort: list[AdsInsightsSortFilter]


# ===== CUSTOM_CONVERSIONS SEARCH TYPES =====

class CustomConversionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering custom_conversions search queries."""
    id: str | None
    """Custom Conversion ID"""
    name: str | None
    """Custom Conversion name"""
    account_id: str | None
    """Ad account ID"""
    description: str | None
    """Description"""
    custom_event_type: str | None
    """Custom event type"""
    creation_time: str | None
    """Creation time"""
    first_fired_time: str | None
    """First fired time"""
    last_fired_time: str | None
    """Last fired time"""
    is_archived: bool | None
    """Whether the conversion is archived"""


class CustomConversionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Custom Conversion ID"""
    name: list[str]
    """Custom Conversion name"""
    account_id: list[str]
    """Ad account ID"""
    description: list[str]
    """Description"""
    custom_event_type: list[str]
    """Custom event type"""
    creation_time: list[str]
    """Creation time"""
    first_fired_time: list[str]
    """First fired time"""
    last_fired_time: list[str]
    """Last fired time"""
    is_archived: list[bool]
    """Whether the conversion is archived"""


class CustomConversionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Custom Conversion ID"""
    name: Any
    """Custom Conversion name"""
    account_id: Any
    """Ad account ID"""
    description: Any
    """Description"""
    custom_event_type: Any
    """Custom event type"""
    creation_time: Any
    """Creation time"""
    first_fired_time: Any
    """First fired time"""
    last_fired_time: Any
    """Last fired time"""
    is_archived: Any
    """Whether the conversion is archived"""


class CustomConversionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Custom Conversion ID"""
    name: str
    """Custom Conversion name"""
    account_id: str
    """Ad account ID"""
    description: str
    """Description"""
    custom_event_type: str
    """Custom event type"""
    creation_time: str
    """Creation time"""
    first_fired_time: str
    """First fired time"""
    last_fired_time: str
    """Last fired time"""
    is_archived: str
    """Whether the conversion is archived"""


class CustomConversionsSortFilter(TypedDict, total=False):
    """Available fields for sorting custom_conversions search results."""
    id: AirbyteSortOrder
    """Custom Conversion ID"""
    name: AirbyteSortOrder
    """Custom Conversion name"""
    account_id: AirbyteSortOrder
    """Ad account ID"""
    description: AirbyteSortOrder
    """Description"""
    custom_event_type: AirbyteSortOrder
    """Custom event type"""
    creation_time: AirbyteSortOrder
    """Creation time"""
    first_fired_time: AirbyteSortOrder
    """First fired time"""
    last_fired_time: AirbyteSortOrder
    """Last fired time"""
    is_archived: AirbyteSortOrder
    """Whether the conversion is archived"""


# Entity-specific condition types for custom_conversions
class CustomConversionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CustomConversionsSearchFilter


class CustomConversionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CustomConversionsSearchFilter


class CustomConversionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CustomConversionsSearchFilter


class CustomConversionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CustomConversionsSearchFilter


class CustomConversionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CustomConversionsSearchFilter


class CustomConversionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CustomConversionsSearchFilter


class CustomConversionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CustomConversionsStringFilter


class CustomConversionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CustomConversionsStringFilter


class CustomConversionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CustomConversionsStringFilter


class CustomConversionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CustomConversionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CustomConversionsInCondition = TypedDict("CustomConversionsInCondition", {"in": CustomConversionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CustomConversionsNotCondition = TypedDict("CustomConversionsNotCondition", {"not": "CustomConversionsCondition"}, total=False)
"""Negates the nested condition."""

CustomConversionsAndCondition = TypedDict("CustomConversionsAndCondition", {"and": "list[CustomConversionsCondition]"}, total=False)
"""True if all nested conditions are true."""

CustomConversionsOrCondition = TypedDict("CustomConversionsOrCondition", {"or": "list[CustomConversionsCondition]"}, total=False)
"""True if any nested condition is true."""

CustomConversionsAnyCondition = TypedDict("CustomConversionsAnyCondition", {"any": CustomConversionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all custom_conversions condition types
CustomConversionsCondition = (
    CustomConversionsEqCondition
    | CustomConversionsNeqCondition
    | CustomConversionsGtCondition
    | CustomConversionsGteCondition
    | CustomConversionsLtCondition
    | CustomConversionsLteCondition
    | CustomConversionsInCondition
    | CustomConversionsLikeCondition
    | CustomConversionsFuzzyCondition
    | CustomConversionsKeywordCondition
    | CustomConversionsContainsCondition
    | CustomConversionsNotCondition
    | CustomConversionsAndCondition
    | CustomConversionsOrCondition
    | CustomConversionsAnyCondition
)


class CustomConversionsSearchQuery(TypedDict, total=False):
    """Search query for custom_conversions entity."""
    filter: CustomConversionsCondition
    sort: list[CustomConversionsSortFilter]


# ===== IMAGES SEARCH TYPES =====

class ImagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering images search queries."""
    id: str | None
    """Image ID"""
    name: str | None
    """Image name"""
    account_id: str | None
    """Ad account ID"""
    hash: str | None
    """Image hash"""
    url: str | None
    """Image URL"""
    permalink_url: str | None
    """Permalink URL"""
    width: int | None
    """Image width"""
    height: int | None
    """Image height"""
    status: str | None
    """Image status"""
    created_time: str | None
    """Creation time"""
    updated_time: str | None
    """Last update time"""


class ImagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Image ID"""
    name: list[str]
    """Image name"""
    account_id: list[str]
    """Ad account ID"""
    hash: list[str]
    """Image hash"""
    url: list[str]
    """Image URL"""
    permalink_url: list[str]
    """Permalink URL"""
    width: list[int]
    """Image width"""
    height: list[int]
    """Image height"""
    status: list[str]
    """Image status"""
    created_time: list[str]
    """Creation time"""
    updated_time: list[str]
    """Last update time"""


class ImagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Image ID"""
    name: Any
    """Image name"""
    account_id: Any
    """Ad account ID"""
    hash: Any
    """Image hash"""
    url: Any
    """Image URL"""
    permalink_url: Any
    """Permalink URL"""
    width: Any
    """Image width"""
    height: Any
    """Image height"""
    status: Any
    """Image status"""
    created_time: Any
    """Creation time"""
    updated_time: Any
    """Last update time"""


class ImagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Image ID"""
    name: str
    """Image name"""
    account_id: str
    """Ad account ID"""
    hash: str
    """Image hash"""
    url: str
    """Image URL"""
    permalink_url: str
    """Permalink URL"""
    width: str
    """Image width"""
    height: str
    """Image height"""
    status: str
    """Image status"""
    created_time: str
    """Creation time"""
    updated_time: str
    """Last update time"""


class ImagesSortFilter(TypedDict, total=False):
    """Available fields for sorting images search results."""
    id: AirbyteSortOrder
    """Image ID"""
    name: AirbyteSortOrder
    """Image name"""
    account_id: AirbyteSortOrder
    """Ad account ID"""
    hash: AirbyteSortOrder
    """Image hash"""
    url: AirbyteSortOrder
    """Image URL"""
    permalink_url: AirbyteSortOrder
    """Permalink URL"""
    width: AirbyteSortOrder
    """Image width"""
    height: AirbyteSortOrder
    """Image height"""
    status: AirbyteSortOrder
    """Image status"""
    created_time: AirbyteSortOrder
    """Creation time"""
    updated_time: AirbyteSortOrder
    """Last update time"""


# Entity-specific condition types for images
class ImagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ImagesSearchFilter


class ImagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ImagesSearchFilter


class ImagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ImagesSearchFilter


class ImagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ImagesSearchFilter


class ImagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ImagesSearchFilter


class ImagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ImagesSearchFilter


class ImagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ImagesStringFilter


class ImagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ImagesStringFilter


class ImagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ImagesStringFilter


class ImagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ImagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ImagesInCondition = TypedDict("ImagesInCondition", {"in": ImagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ImagesNotCondition = TypedDict("ImagesNotCondition", {"not": "ImagesCondition"}, total=False)
"""Negates the nested condition."""

ImagesAndCondition = TypedDict("ImagesAndCondition", {"and": "list[ImagesCondition]"}, total=False)
"""True if all nested conditions are true."""

ImagesOrCondition = TypedDict("ImagesOrCondition", {"or": "list[ImagesCondition]"}, total=False)
"""True if any nested condition is true."""

ImagesAnyCondition = TypedDict("ImagesAnyCondition", {"any": ImagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all images condition types
ImagesCondition = (
    ImagesEqCondition
    | ImagesNeqCondition
    | ImagesGtCondition
    | ImagesGteCondition
    | ImagesLtCondition
    | ImagesLteCondition
    | ImagesInCondition
    | ImagesLikeCondition
    | ImagesFuzzyCondition
    | ImagesKeywordCondition
    | ImagesContainsCondition
    | ImagesNotCondition
    | ImagesAndCondition
    | ImagesOrCondition
    | ImagesAnyCondition
)


class ImagesSearchQuery(TypedDict, total=False):
    """Search query for images entity."""
    filter: ImagesCondition
    sort: list[ImagesSortFilter]


# ===== VIDEOS SEARCH TYPES =====

class VideosSearchFilter(TypedDict, total=False):
    """Available fields for filtering videos search queries."""
    id: str | None
    """Video ID"""
    title: str | None
    """Video title"""
    account_id: str | None
    """Ad account ID"""
    description: str | None
    """Video description"""
    length: float | None
    """Video length in seconds"""
    source: str | None
    """Video source URL"""
    permalink_url: str | None
    """Permalink URL"""
    views: int | None
    """Number of views"""
    created_time: str | None
    """Creation time"""
    updated_time: str | None
    """Last update time"""


class VideosInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Video ID"""
    title: list[str]
    """Video title"""
    account_id: list[str]
    """Ad account ID"""
    description: list[str]
    """Video description"""
    length: list[float]
    """Video length in seconds"""
    source: list[str]
    """Video source URL"""
    permalink_url: list[str]
    """Permalink URL"""
    views: list[int]
    """Number of views"""
    created_time: list[str]
    """Creation time"""
    updated_time: list[str]
    """Last update time"""


class VideosAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Video ID"""
    title: Any
    """Video title"""
    account_id: Any
    """Ad account ID"""
    description: Any
    """Video description"""
    length: Any
    """Video length in seconds"""
    source: Any
    """Video source URL"""
    permalink_url: Any
    """Permalink URL"""
    views: Any
    """Number of views"""
    created_time: Any
    """Creation time"""
    updated_time: Any
    """Last update time"""


class VideosStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Video ID"""
    title: str
    """Video title"""
    account_id: str
    """Ad account ID"""
    description: str
    """Video description"""
    length: str
    """Video length in seconds"""
    source: str
    """Video source URL"""
    permalink_url: str
    """Permalink URL"""
    views: str
    """Number of views"""
    created_time: str
    """Creation time"""
    updated_time: str
    """Last update time"""


class VideosSortFilter(TypedDict, total=False):
    """Available fields for sorting videos search results."""
    id: AirbyteSortOrder
    """Video ID"""
    title: AirbyteSortOrder
    """Video title"""
    account_id: AirbyteSortOrder
    """Ad account ID"""
    description: AirbyteSortOrder
    """Video description"""
    length: AirbyteSortOrder
    """Video length in seconds"""
    source: AirbyteSortOrder
    """Video source URL"""
    permalink_url: AirbyteSortOrder
    """Permalink URL"""
    views: AirbyteSortOrder
    """Number of views"""
    created_time: AirbyteSortOrder
    """Creation time"""
    updated_time: AirbyteSortOrder
    """Last update time"""


# Entity-specific condition types for videos
class VideosEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: VideosSearchFilter


class VideosNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: VideosSearchFilter


class VideosGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: VideosSearchFilter


class VideosGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: VideosSearchFilter


class VideosLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: VideosSearchFilter


class VideosLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: VideosSearchFilter


class VideosLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: VideosStringFilter


class VideosFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: VideosStringFilter


class VideosKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: VideosStringFilter


class VideosContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: VideosAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
VideosInCondition = TypedDict("VideosInCondition", {"in": VideosInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

VideosNotCondition = TypedDict("VideosNotCondition", {"not": "VideosCondition"}, total=False)
"""Negates the nested condition."""

VideosAndCondition = TypedDict("VideosAndCondition", {"and": "list[VideosCondition]"}, total=False)
"""True if all nested conditions are true."""

VideosOrCondition = TypedDict("VideosOrCondition", {"or": "list[VideosCondition]"}, total=False)
"""True if any nested condition is true."""

VideosAnyCondition = TypedDict("VideosAnyCondition", {"any": VideosAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all videos condition types
VideosCondition = (
    VideosEqCondition
    | VideosNeqCondition
    | VideosGtCondition
    | VideosGteCondition
    | VideosLtCondition
    | VideosLteCondition
    | VideosInCondition
    | VideosLikeCondition
    | VideosFuzzyCondition
    | VideosKeywordCondition
    | VideosContainsCondition
    | VideosNotCondition
    | VideosAndCondition
    | VideosOrCondition
    | VideosAnyCondition
)


class VideosSearchQuery(TypedDict, total=False):
    """Search query for videos entity."""
    filter: VideosCondition
    sort: list[VideosSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
