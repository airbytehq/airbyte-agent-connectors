"""
Type definitions for pinterest connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class AdAccountsListParams(TypedDict):
    """Parameters for ad_accounts.list operation"""
    page_size: NotRequired[int]
    bookmark: NotRequired[str]
    include_shared_accounts: NotRequired[bool]

class AdAccountsGetParams(TypedDict):
    """Parameters for ad_accounts.get operation"""
    ad_account_id: str

class BoardsListParams(TypedDict):
    """Parameters for boards.list operation"""
    page_size: NotRequired[int]
    bookmark: NotRequired[str]
    privacy: NotRequired[str]

class BoardsGetParams(TypedDict):
    """Parameters for boards.get operation"""
    board_id: str

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    ad_account_id: str
    page_size: NotRequired[int]
    bookmark: NotRequired[str]
    entity_statuses: NotRequired[list[str]]
    order: NotRequired[str]

class AdGroupsListParams(TypedDict):
    """Parameters for ad_groups.list operation"""
    ad_account_id: str
    page_size: NotRequired[int]
    bookmark: NotRequired[str]
    entity_statuses: NotRequired[list[str]]
    order: NotRequired[str]

class AdsListParams(TypedDict):
    """Parameters for ads.list operation"""
    ad_account_id: str
    page_size: NotRequired[int]
    bookmark: NotRequired[str]
    entity_statuses: NotRequired[list[str]]
    order: NotRequired[str]

class BoardSectionsListParams(TypedDict):
    """Parameters for board_sections.list operation"""
    board_id: str
    page_size: NotRequired[int]
    bookmark: NotRequired[str]

class BoardPinsListParams(TypedDict):
    """Parameters for board_pins.list operation"""
    board_id: str
    page_size: NotRequired[int]
    bookmark: NotRequired[str]

class CatalogsListParams(TypedDict):
    """Parameters for catalogs.list operation"""
    page_size: NotRequired[int]
    bookmark: NotRequired[str]

class CatalogsFeedsListParams(TypedDict):
    """Parameters for catalogs_feeds.list operation"""
    page_size: NotRequired[int]
    bookmark: NotRequired[str]

class CatalogsProductGroupsListParams(TypedDict):
    """Parameters for catalogs_product_groups.list operation"""
    page_size: NotRequired[int]
    bookmark: NotRequired[str]

class AudiencesListParams(TypedDict):
    """Parameters for audiences.list operation"""
    ad_account_id: str
    page_size: NotRequired[int]
    bookmark: NotRequired[str]

class ConversionTagsListParams(TypedDict):
    """Parameters for conversion_tags.list operation"""
    ad_account_id: str
    page_size: NotRequired[int]
    bookmark: NotRequired[str]

class CustomerListsListParams(TypedDict):
    """Parameters for customer_lists.list operation"""
    ad_account_id: str
    page_size: NotRequired[int]
    bookmark: NotRequired[str]

class KeywordsListParams(TypedDict):
    """Parameters for keywords.list operation"""
    ad_account_id: str
    ad_group_id: str
    page_size: NotRequired[int]
    bookmark: NotRequired[str]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== AD_ACCOUNTS SEARCH TYPES =====

class AdAccountsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_accounts search queries."""
    country: str | None
    """Country associated with the ad account"""
    created_time: int | None
    """Timestamp when the ad account was created (Unix seconds)"""
    currency: str | None
    """Currency used for billing"""
    id: str | None
    """Unique identifier for the ad account"""
    name: str | None
    """Name of the ad account"""
    owner: dict[str, Any] | None
    """Owner details of the ad account"""
    permissions: list[Any] | None
    """Permissions assigned to the ad account"""
    updated_time: int | None
    """Timestamp when the ad account was last updated (Unix seconds)"""


class AdAccountsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    country: list[str]
    """Country associated with the ad account"""
    created_time: list[int]
    """Timestamp when the ad account was created (Unix seconds)"""
    currency: list[str]
    """Currency used for billing"""
    id: list[str]
    """Unique identifier for the ad account"""
    name: list[str]
    """Name of the ad account"""
    owner: list[dict[str, Any]]
    """Owner details of the ad account"""
    permissions: list[list[Any]]
    """Permissions assigned to the ad account"""
    updated_time: list[int]
    """Timestamp when the ad account was last updated (Unix seconds)"""


class AdAccountsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    country: Any
    """Country associated with the ad account"""
    created_time: Any
    """Timestamp when the ad account was created (Unix seconds)"""
    currency: Any
    """Currency used for billing"""
    id: Any
    """Unique identifier for the ad account"""
    name: Any
    """Name of the ad account"""
    owner: Any
    """Owner details of the ad account"""
    permissions: Any
    """Permissions assigned to the ad account"""
    updated_time: Any
    """Timestamp when the ad account was last updated (Unix seconds)"""


class AdAccountsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    country: str
    """Country associated with the ad account"""
    created_time: str
    """Timestamp when the ad account was created (Unix seconds)"""
    currency: str
    """Currency used for billing"""
    id: str
    """Unique identifier for the ad account"""
    name: str
    """Name of the ad account"""
    owner: str
    """Owner details of the ad account"""
    permissions: str
    """Permissions assigned to the ad account"""
    updated_time: str
    """Timestamp when the ad account was last updated (Unix seconds)"""


class AdAccountsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_accounts search results."""
    country: AirbyteSortOrder
    """Country associated with the ad account"""
    created_time: AirbyteSortOrder
    """Timestamp when the ad account was created (Unix seconds)"""
    currency: AirbyteSortOrder
    """Currency used for billing"""
    id: AirbyteSortOrder
    """Unique identifier for the ad account"""
    name: AirbyteSortOrder
    """Name of the ad account"""
    owner: AirbyteSortOrder
    """Owner details of the ad account"""
    permissions: AirbyteSortOrder
    """Permissions assigned to the ad account"""
    updated_time: AirbyteSortOrder
    """Timestamp when the ad account was last updated (Unix seconds)"""


# Entity-specific condition types for ad_accounts
class AdAccountsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdAccountsSearchFilter


class AdAccountsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdAccountsSearchFilter


class AdAccountsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdAccountsSearchFilter


class AdAccountsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdAccountsSearchFilter


class AdAccountsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdAccountsSearchFilter


class AdAccountsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdAccountsSearchFilter


class AdAccountsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdAccountsStringFilter


class AdAccountsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdAccountsStringFilter


class AdAccountsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdAccountsStringFilter


class AdAccountsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdAccountsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdAccountsInCondition = TypedDict("AdAccountsInCondition", {"in": AdAccountsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdAccountsNotCondition = TypedDict("AdAccountsNotCondition", {"not": "AdAccountsCondition"}, total=False)
"""Negates the nested condition."""

AdAccountsAndCondition = TypedDict("AdAccountsAndCondition", {"and": "list[AdAccountsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdAccountsOrCondition = TypedDict("AdAccountsOrCondition", {"or": "list[AdAccountsCondition]"}, total=False)
"""True if any nested condition is true."""

AdAccountsAnyCondition = TypedDict("AdAccountsAnyCondition", {"any": AdAccountsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_accounts condition types
AdAccountsCondition = (
    AdAccountsEqCondition
    | AdAccountsNeqCondition
    | AdAccountsGtCondition
    | AdAccountsGteCondition
    | AdAccountsLtCondition
    | AdAccountsLteCondition
    | AdAccountsInCondition
    | AdAccountsLikeCondition
    | AdAccountsFuzzyCondition
    | AdAccountsKeywordCondition
    | AdAccountsContainsCondition
    | AdAccountsNotCondition
    | AdAccountsAndCondition
    | AdAccountsOrCondition
    | AdAccountsAnyCondition
)


class AdAccountsSearchQuery(TypedDict, total=False):
    """Search query for ad_accounts entity."""
    filter: AdAccountsCondition
    sort: list[AdAccountsSortFilter]


# ===== BOARDS SEARCH TYPES =====

class BoardsSearchFilter(TypedDict, total=False):
    """Available fields for filtering boards search queries."""
    board_pins_modified_at: str | None
    """Timestamp when pins on the board were last modified"""
    collaborator_count: int | None
    """Number of collaborators"""
    created_at: str | None
    """Timestamp when the board was created"""
    description: str | None
    """Board description"""
    follower_count: int | None
    """Number of followers"""
    id: str | None
    """Unique identifier for the board"""
    media: dict[str, Any] | None
    """Media content for the board"""
    name: str | None
    """Board name"""
    owner: dict[str, Any] | None
    """Board owner details"""
    pin_count: int | None
    """Number of pins on the board"""
    privacy: str | None
    """Board privacy setting"""


class BoardsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    board_pins_modified_at: list[str]
    """Timestamp when pins on the board were last modified"""
    collaborator_count: list[int]
    """Number of collaborators"""
    created_at: list[str]
    """Timestamp when the board was created"""
    description: list[str]
    """Board description"""
    follower_count: list[int]
    """Number of followers"""
    id: list[str]
    """Unique identifier for the board"""
    media: list[dict[str, Any]]
    """Media content for the board"""
    name: list[str]
    """Board name"""
    owner: list[dict[str, Any]]
    """Board owner details"""
    pin_count: list[int]
    """Number of pins on the board"""
    privacy: list[str]
    """Board privacy setting"""


class BoardsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    board_pins_modified_at: Any
    """Timestamp when pins on the board were last modified"""
    collaborator_count: Any
    """Number of collaborators"""
    created_at: Any
    """Timestamp when the board was created"""
    description: Any
    """Board description"""
    follower_count: Any
    """Number of followers"""
    id: Any
    """Unique identifier for the board"""
    media: Any
    """Media content for the board"""
    name: Any
    """Board name"""
    owner: Any
    """Board owner details"""
    pin_count: Any
    """Number of pins on the board"""
    privacy: Any
    """Board privacy setting"""


class BoardsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    board_pins_modified_at: str
    """Timestamp when pins on the board were last modified"""
    collaborator_count: str
    """Number of collaborators"""
    created_at: str
    """Timestamp when the board was created"""
    description: str
    """Board description"""
    follower_count: str
    """Number of followers"""
    id: str
    """Unique identifier for the board"""
    media: str
    """Media content for the board"""
    name: str
    """Board name"""
    owner: str
    """Board owner details"""
    pin_count: str
    """Number of pins on the board"""
    privacy: str
    """Board privacy setting"""


class BoardsSortFilter(TypedDict, total=False):
    """Available fields for sorting boards search results."""
    board_pins_modified_at: AirbyteSortOrder
    """Timestamp when pins on the board were last modified"""
    collaborator_count: AirbyteSortOrder
    """Number of collaborators"""
    created_at: AirbyteSortOrder
    """Timestamp when the board was created"""
    description: AirbyteSortOrder
    """Board description"""
    follower_count: AirbyteSortOrder
    """Number of followers"""
    id: AirbyteSortOrder
    """Unique identifier for the board"""
    media: AirbyteSortOrder
    """Media content for the board"""
    name: AirbyteSortOrder
    """Board name"""
    owner: AirbyteSortOrder
    """Board owner details"""
    pin_count: AirbyteSortOrder
    """Number of pins on the board"""
    privacy: AirbyteSortOrder
    """Board privacy setting"""


# Entity-specific condition types for boards
class BoardsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BoardsSearchFilter


class BoardsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BoardsSearchFilter


class BoardsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BoardsSearchFilter


class BoardsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BoardsSearchFilter


class BoardsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BoardsSearchFilter


class BoardsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BoardsSearchFilter


class BoardsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BoardsStringFilter


class BoardsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BoardsStringFilter


class BoardsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BoardsStringFilter


class BoardsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BoardsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BoardsInCondition = TypedDict("BoardsInCondition", {"in": BoardsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BoardsNotCondition = TypedDict("BoardsNotCondition", {"not": "BoardsCondition"}, total=False)
"""Negates the nested condition."""

BoardsAndCondition = TypedDict("BoardsAndCondition", {"and": "list[BoardsCondition]"}, total=False)
"""True if all nested conditions are true."""

BoardsOrCondition = TypedDict("BoardsOrCondition", {"or": "list[BoardsCondition]"}, total=False)
"""True if any nested condition is true."""

BoardsAnyCondition = TypedDict("BoardsAnyCondition", {"any": BoardsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all boards condition types
BoardsCondition = (
    BoardsEqCondition
    | BoardsNeqCondition
    | BoardsGtCondition
    | BoardsGteCondition
    | BoardsLtCondition
    | BoardsLteCondition
    | BoardsInCondition
    | BoardsLikeCondition
    | BoardsFuzzyCondition
    | BoardsKeywordCondition
    | BoardsContainsCondition
    | BoardsNotCondition
    | BoardsAndCondition
    | BoardsOrCondition
    | BoardsAnyCondition
)


class BoardsSearchQuery(TypedDict, total=False):
    """Search query for boards entity."""
    filter: BoardsCondition
    sort: list[BoardsSortFilter]


# ===== CAMPAIGNS SEARCH TYPES =====

class CampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaigns search queries."""
    ad_account_id: str | None
    """Ad account ID"""
    created_time: int | None
    """Creation timestamp (Unix seconds)"""
    daily_spend_cap: int | None
    """Maximum daily spend in microcurrency"""
    end_time: int | None
    """End timestamp (Unix seconds)"""
    id: str | None
    """Campaign ID"""
    is_campaign_budget_optimization: bool | None
    """Whether CBO is enabled"""
    is_flexible_daily_budgets: bool | None
    """Whether flexible daily budgets are enabled"""
    lifetime_spend_cap: int | None
    """Maximum lifetime spend in microcurrency"""
    name: str | None
    """Campaign name"""
    objective_type: str | None
    """Campaign objective type"""
    order_line_id: str | None
    """Order line ID on invoice"""
    start_time: int | None
    """Start timestamp (Unix seconds)"""
    status: str | None
    """Entity status"""
    summary_status: str | None
    """Summary status"""
    tracking_urls: dict[str, Any] | None
    """Third-party tracking URLs"""
    type_: str | None
    """Always 'campaign'"""
    updated_time: int | None
    """Last update timestamp (Unix seconds)"""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_account_id: list[str]
    """Ad account ID"""
    created_time: list[int]
    """Creation timestamp (Unix seconds)"""
    daily_spend_cap: list[int]
    """Maximum daily spend in microcurrency"""
    end_time: list[int]
    """End timestamp (Unix seconds)"""
    id: list[str]
    """Campaign ID"""
    is_campaign_budget_optimization: list[bool]
    """Whether CBO is enabled"""
    is_flexible_daily_budgets: list[bool]
    """Whether flexible daily budgets are enabled"""
    lifetime_spend_cap: list[int]
    """Maximum lifetime spend in microcurrency"""
    name: list[str]
    """Campaign name"""
    objective_type: list[str]
    """Campaign objective type"""
    order_line_id: list[str]
    """Order line ID on invoice"""
    start_time: list[int]
    """Start timestamp (Unix seconds)"""
    status: list[str]
    """Entity status"""
    summary_status: list[str]
    """Summary status"""
    tracking_urls: list[dict[str, Any]]
    """Third-party tracking URLs"""
    type_: list[str]
    """Always 'campaign'"""
    updated_time: list[int]
    """Last update timestamp (Unix seconds)"""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_account_id: Any
    """Ad account ID"""
    created_time: Any
    """Creation timestamp (Unix seconds)"""
    daily_spend_cap: Any
    """Maximum daily spend in microcurrency"""
    end_time: Any
    """End timestamp (Unix seconds)"""
    id: Any
    """Campaign ID"""
    is_campaign_budget_optimization: Any
    """Whether CBO is enabled"""
    is_flexible_daily_budgets: Any
    """Whether flexible daily budgets are enabled"""
    lifetime_spend_cap: Any
    """Maximum lifetime spend in microcurrency"""
    name: Any
    """Campaign name"""
    objective_type: Any
    """Campaign objective type"""
    order_line_id: Any
    """Order line ID on invoice"""
    start_time: Any
    """Start timestamp (Unix seconds)"""
    status: Any
    """Entity status"""
    summary_status: Any
    """Summary status"""
    tracking_urls: Any
    """Third-party tracking URLs"""
    type_: Any
    """Always 'campaign'"""
    updated_time: Any
    """Last update timestamp (Unix seconds)"""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_account_id: str
    """Ad account ID"""
    created_time: str
    """Creation timestamp (Unix seconds)"""
    daily_spend_cap: str
    """Maximum daily spend in microcurrency"""
    end_time: str
    """End timestamp (Unix seconds)"""
    id: str
    """Campaign ID"""
    is_campaign_budget_optimization: str
    """Whether CBO is enabled"""
    is_flexible_daily_budgets: str
    """Whether flexible daily budgets are enabled"""
    lifetime_spend_cap: str
    """Maximum lifetime spend in microcurrency"""
    name: str
    """Campaign name"""
    objective_type: str
    """Campaign objective type"""
    order_line_id: str
    """Order line ID on invoice"""
    start_time: str
    """Start timestamp (Unix seconds)"""
    status: str
    """Entity status"""
    summary_status: str
    """Summary status"""
    tracking_urls: str
    """Third-party tracking URLs"""
    type_: str
    """Always 'campaign'"""
    updated_time: str
    """Last update timestamp (Unix seconds)"""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    ad_account_id: AirbyteSortOrder
    """Ad account ID"""
    created_time: AirbyteSortOrder
    """Creation timestamp (Unix seconds)"""
    daily_spend_cap: AirbyteSortOrder
    """Maximum daily spend in microcurrency"""
    end_time: AirbyteSortOrder
    """End timestamp (Unix seconds)"""
    id: AirbyteSortOrder
    """Campaign ID"""
    is_campaign_budget_optimization: AirbyteSortOrder
    """Whether CBO is enabled"""
    is_flexible_daily_budgets: AirbyteSortOrder
    """Whether flexible daily budgets are enabled"""
    lifetime_spend_cap: AirbyteSortOrder
    """Maximum lifetime spend in microcurrency"""
    name: AirbyteSortOrder
    """Campaign name"""
    objective_type: AirbyteSortOrder
    """Campaign objective type"""
    order_line_id: AirbyteSortOrder
    """Order line ID on invoice"""
    start_time: AirbyteSortOrder
    """Start timestamp (Unix seconds)"""
    status: AirbyteSortOrder
    """Entity status"""
    summary_status: AirbyteSortOrder
    """Summary status"""
    tracking_urls: AirbyteSortOrder
    """Third-party tracking URLs"""
    type_: AirbyteSortOrder
    """Always 'campaign'"""
    updated_time: AirbyteSortOrder
    """Last update timestamp (Unix seconds)"""


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


# ===== AD_GROUPS SEARCH TYPES =====

class AdGroupsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_groups search queries."""
    ad_account_id: str | None
    """Ad account ID"""
    auto_targeting_enabled: bool | None
    """Whether auto targeting is enabled"""
    bid_in_micro_currency: float | None
    """Bid in microcurrency"""
    bid_strategy_type: str | None
    """Bid strategy type"""
    billable_event: str | None
    """Billable event type"""
    budget_in_micro_currency: float | None
    """Budget in microcurrency"""
    budget_type: str | None
    """Budget type"""
    campaign_id: str | None
    """Parent campaign ID"""
    conversion_learning_mode_type: str | None
    """oCPM learn mode type"""
    created_time: float | None
    """Creation timestamp (Unix seconds)"""
    end_time: float | None
    """End time (Unix seconds)"""
    feed_profile_id: str | None
    """Feed profile ID"""
    id: str | None
    """Ad group ID"""
    lifetime_frequency_cap: float | None
    """Max impressions per user in 30 days"""
    name: str | None
    """Ad group name"""
    optimization_goal_metadata: dict[str, Any] | None
    """Optimization goal metadata"""
    pacing_delivery_type: str | None
    """Pacing delivery type"""
    placement_group: str | None
    """Placement group"""
    start_time: float | None
    """Start time (Unix seconds)"""
    status: str | None
    """Entity status"""
    summary_status: str | None
    """Summary status"""
    targeting_spec: dict[str, Any] | None
    """Targeting specifications"""
    tracking_urls: dict[str, Any] | None
    """Third-party tracking URLs"""
    type_: str | None
    """Always 'adgroup'"""
    updated_time: float | None
    """Last update timestamp (Unix seconds)"""


class AdGroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_account_id: list[str]
    """Ad account ID"""
    auto_targeting_enabled: list[bool]
    """Whether auto targeting is enabled"""
    bid_in_micro_currency: list[float]
    """Bid in microcurrency"""
    bid_strategy_type: list[str]
    """Bid strategy type"""
    billable_event: list[str]
    """Billable event type"""
    budget_in_micro_currency: list[float]
    """Budget in microcurrency"""
    budget_type: list[str]
    """Budget type"""
    campaign_id: list[str]
    """Parent campaign ID"""
    conversion_learning_mode_type: list[str]
    """oCPM learn mode type"""
    created_time: list[float]
    """Creation timestamp (Unix seconds)"""
    end_time: list[float]
    """End time (Unix seconds)"""
    feed_profile_id: list[str]
    """Feed profile ID"""
    id: list[str]
    """Ad group ID"""
    lifetime_frequency_cap: list[float]
    """Max impressions per user in 30 days"""
    name: list[str]
    """Ad group name"""
    optimization_goal_metadata: list[dict[str, Any]]
    """Optimization goal metadata"""
    pacing_delivery_type: list[str]
    """Pacing delivery type"""
    placement_group: list[str]
    """Placement group"""
    start_time: list[float]
    """Start time (Unix seconds)"""
    status: list[str]
    """Entity status"""
    summary_status: list[str]
    """Summary status"""
    targeting_spec: list[dict[str, Any]]
    """Targeting specifications"""
    tracking_urls: list[dict[str, Any]]
    """Third-party tracking URLs"""
    type_: list[str]
    """Always 'adgroup'"""
    updated_time: list[float]
    """Last update timestamp (Unix seconds)"""


class AdGroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_account_id: Any
    """Ad account ID"""
    auto_targeting_enabled: Any
    """Whether auto targeting is enabled"""
    bid_in_micro_currency: Any
    """Bid in microcurrency"""
    bid_strategy_type: Any
    """Bid strategy type"""
    billable_event: Any
    """Billable event type"""
    budget_in_micro_currency: Any
    """Budget in microcurrency"""
    budget_type: Any
    """Budget type"""
    campaign_id: Any
    """Parent campaign ID"""
    conversion_learning_mode_type: Any
    """oCPM learn mode type"""
    created_time: Any
    """Creation timestamp (Unix seconds)"""
    end_time: Any
    """End time (Unix seconds)"""
    feed_profile_id: Any
    """Feed profile ID"""
    id: Any
    """Ad group ID"""
    lifetime_frequency_cap: Any
    """Max impressions per user in 30 days"""
    name: Any
    """Ad group name"""
    optimization_goal_metadata: Any
    """Optimization goal metadata"""
    pacing_delivery_type: Any
    """Pacing delivery type"""
    placement_group: Any
    """Placement group"""
    start_time: Any
    """Start time (Unix seconds)"""
    status: Any
    """Entity status"""
    summary_status: Any
    """Summary status"""
    targeting_spec: Any
    """Targeting specifications"""
    tracking_urls: Any
    """Third-party tracking URLs"""
    type_: Any
    """Always 'adgroup'"""
    updated_time: Any
    """Last update timestamp (Unix seconds)"""


class AdGroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_account_id: str
    """Ad account ID"""
    auto_targeting_enabled: str
    """Whether auto targeting is enabled"""
    bid_in_micro_currency: str
    """Bid in microcurrency"""
    bid_strategy_type: str
    """Bid strategy type"""
    billable_event: str
    """Billable event type"""
    budget_in_micro_currency: str
    """Budget in microcurrency"""
    budget_type: str
    """Budget type"""
    campaign_id: str
    """Parent campaign ID"""
    conversion_learning_mode_type: str
    """oCPM learn mode type"""
    created_time: str
    """Creation timestamp (Unix seconds)"""
    end_time: str
    """End time (Unix seconds)"""
    feed_profile_id: str
    """Feed profile ID"""
    id: str
    """Ad group ID"""
    lifetime_frequency_cap: str
    """Max impressions per user in 30 days"""
    name: str
    """Ad group name"""
    optimization_goal_metadata: str
    """Optimization goal metadata"""
    pacing_delivery_type: str
    """Pacing delivery type"""
    placement_group: str
    """Placement group"""
    start_time: str
    """Start time (Unix seconds)"""
    status: str
    """Entity status"""
    summary_status: str
    """Summary status"""
    targeting_spec: str
    """Targeting specifications"""
    tracking_urls: str
    """Third-party tracking URLs"""
    type_: str
    """Always 'adgroup'"""
    updated_time: str
    """Last update timestamp (Unix seconds)"""


class AdGroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_groups search results."""
    ad_account_id: AirbyteSortOrder
    """Ad account ID"""
    auto_targeting_enabled: AirbyteSortOrder
    """Whether auto targeting is enabled"""
    bid_in_micro_currency: AirbyteSortOrder
    """Bid in microcurrency"""
    bid_strategy_type: AirbyteSortOrder
    """Bid strategy type"""
    billable_event: AirbyteSortOrder
    """Billable event type"""
    budget_in_micro_currency: AirbyteSortOrder
    """Budget in microcurrency"""
    budget_type: AirbyteSortOrder
    """Budget type"""
    campaign_id: AirbyteSortOrder
    """Parent campaign ID"""
    conversion_learning_mode_type: AirbyteSortOrder
    """oCPM learn mode type"""
    created_time: AirbyteSortOrder
    """Creation timestamp (Unix seconds)"""
    end_time: AirbyteSortOrder
    """End time (Unix seconds)"""
    feed_profile_id: AirbyteSortOrder
    """Feed profile ID"""
    id: AirbyteSortOrder
    """Ad group ID"""
    lifetime_frequency_cap: AirbyteSortOrder
    """Max impressions per user in 30 days"""
    name: AirbyteSortOrder
    """Ad group name"""
    optimization_goal_metadata: AirbyteSortOrder
    """Optimization goal metadata"""
    pacing_delivery_type: AirbyteSortOrder
    """Pacing delivery type"""
    placement_group: AirbyteSortOrder
    """Placement group"""
    start_time: AirbyteSortOrder
    """Start time (Unix seconds)"""
    status: AirbyteSortOrder
    """Entity status"""
    summary_status: AirbyteSortOrder
    """Summary status"""
    targeting_spec: AirbyteSortOrder
    """Targeting specifications"""
    tracking_urls: AirbyteSortOrder
    """Third-party tracking URLs"""
    type_: AirbyteSortOrder
    """Always 'adgroup'"""
    updated_time: AirbyteSortOrder
    """Last update timestamp (Unix seconds)"""


# Entity-specific condition types for ad_groups
class AdGroupsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdGroupsSearchFilter


class AdGroupsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdGroupsSearchFilter


class AdGroupsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdGroupsSearchFilter


class AdGroupsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdGroupsSearchFilter


class AdGroupsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdGroupsSearchFilter


class AdGroupsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdGroupsSearchFilter


class AdGroupsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdGroupsStringFilter


class AdGroupsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdGroupsStringFilter


class AdGroupsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdGroupsStringFilter


class AdGroupsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdGroupsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdGroupsInCondition = TypedDict("AdGroupsInCondition", {"in": AdGroupsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdGroupsNotCondition = TypedDict("AdGroupsNotCondition", {"not": "AdGroupsCondition"}, total=False)
"""Negates the nested condition."""

AdGroupsAndCondition = TypedDict("AdGroupsAndCondition", {"and": "list[AdGroupsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdGroupsOrCondition = TypedDict("AdGroupsOrCondition", {"or": "list[AdGroupsCondition]"}, total=False)
"""True if any nested condition is true."""

AdGroupsAnyCondition = TypedDict("AdGroupsAnyCondition", {"any": AdGroupsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_groups condition types
AdGroupsCondition = (
    AdGroupsEqCondition
    | AdGroupsNeqCondition
    | AdGroupsGtCondition
    | AdGroupsGteCondition
    | AdGroupsLtCondition
    | AdGroupsLteCondition
    | AdGroupsInCondition
    | AdGroupsLikeCondition
    | AdGroupsFuzzyCondition
    | AdGroupsKeywordCondition
    | AdGroupsContainsCondition
    | AdGroupsNotCondition
    | AdGroupsAndCondition
    | AdGroupsOrCondition
    | AdGroupsAnyCondition
)


class AdGroupsSearchQuery(TypedDict, total=False):
    """Search query for ad_groups entity."""
    filter: AdGroupsCondition
    sort: list[AdGroupsSortFilter]


# ===== ADS SEARCH TYPES =====

class AdsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ads search queries."""
    ad_account_id: str | None
    """Ad account ID"""
    ad_group_id: str | None
    """Ad group ID"""
    android_deep_link: str | None
    """Android deep link"""
    campaign_id: str | None
    """Campaign ID"""
    carousel_android_deep_links: list[Any] | None
    """Carousel Android deep links"""
    carousel_destination_urls: list[Any] | None
    """Carousel destination URLs"""
    carousel_ios_deep_links: list[Any] | None
    """Carousel iOS deep links"""
    click_tracking_url: str | None
    """Click tracking URL"""
    collection_items_destination_url_template: str | None
    """Template URL for collection items"""
    created_time: int | None
    """Creation timestamp (Unix seconds)"""
    creative_type: str | None
    """Creative type"""
    destination_url: str | None
    """Main destination URL"""
    id: str | None
    """Unique ad ID"""
    ios_deep_link: str | None
    """iOS deep link"""
    is_pin_deleted: bool | None
    """Whether the original pin is deleted"""
    is_removable: bool | None
    """Whether the ad is removable"""
    lead_form_id: str | None
    """Lead form ID"""
    name: str | None
    """Ad name"""
    pin_id: str | None
    """Associated pin ID"""
    rejected_reasons: list[Any] | None
    """Rejection reasons"""
    rejection_labels: list[Any] | None
    """Rejection text labels"""
    review_status: str | None
    """Review status"""
    status: str | None
    """Entity status"""
    summary_status: str | None
    """Summary status"""
    tracking_urls: dict[str, Any] | None
    """Third-party tracking URLs"""
    type_: str | None
    """Always 'pinpromotion'"""
    updated_time: int | None
    """Last update timestamp (Unix seconds)"""
    view_tracking_url: str | None
    """View tracking URL"""


class AdsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_account_id: list[str]
    """Ad account ID"""
    ad_group_id: list[str]
    """Ad group ID"""
    android_deep_link: list[str]
    """Android deep link"""
    campaign_id: list[str]
    """Campaign ID"""
    carousel_android_deep_links: list[list[Any]]
    """Carousel Android deep links"""
    carousel_destination_urls: list[list[Any]]
    """Carousel destination URLs"""
    carousel_ios_deep_links: list[list[Any]]
    """Carousel iOS deep links"""
    click_tracking_url: list[str]
    """Click tracking URL"""
    collection_items_destination_url_template: list[str]
    """Template URL for collection items"""
    created_time: list[int]
    """Creation timestamp (Unix seconds)"""
    creative_type: list[str]
    """Creative type"""
    destination_url: list[str]
    """Main destination URL"""
    id: list[str]
    """Unique ad ID"""
    ios_deep_link: list[str]
    """iOS deep link"""
    is_pin_deleted: list[bool]
    """Whether the original pin is deleted"""
    is_removable: list[bool]
    """Whether the ad is removable"""
    lead_form_id: list[str]
    """Lead form ID"""
    name: list[str]
    """Ad name"""
    pin_id: list[str]
    """Associated pin ID"""
    rejected_reasons: list[list[Any]]
    """Rejection reasons"""
    rejection_labels: list[list[Any]]
    """Rejection text labels"""
    review_status: list[str]
    """Review status"""
    status: list[str]
    """Entity status"""
    summary_status: list[str]
    """Summary status"""
    tracking_urls: list[dict[str, Any]]
    """Third-party tracking URLs"""
    type_: list[str]
    """Always 'pinpromotion'"""
    updated_time: list[int]
    """Last update timestamp (Unix seconds)"""
    view_tracking_url: list[str]
    """View tracking URL"""


class AdsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_account_id: Any
    """Ad account ID"""
    ad_group_id: Any
    """Ad group ID"""
    android_deep_link: Any
    """Android deep link"""
    campaign_id: Any
    """Campaign ID"""
    carousel_android_deep_links: Any
    """Carousel Android deep links"""
    carousel_destination_urls: Any
    """Carousel destination URLs"""
    carousel_ios_deep_links: Any
    """Carousel iOS deep links"""
    click_tracking_url: Any
    """Click tracking URL"""
    collection_items_destination_url_template: Any
    """Template URL for collection items"""
    created_time: Any
    """Creation timestamp (Unix seconds)"""
    creative_type: Any
    """Creative type"""
    destination_url: Any
    """Main destination URL"""
    id: Any
    """Unique ad ID"""
    ios_deep_link: Any
    """iOS deep link"""
    is_pin_deleted: Any
    """Whether the original pin is deleted"""
    is_removable: Any
    """Whether the ad is removable"""
    lead_form_id: Any
    """Lead form ID"""
    name: Any
    """Ad name"""
    pin_id: Any
    """Associated pin ID"""
    rejected_reasons: Any
    """Rejection reasons"""
    rejection_labels: Any
    """Rejection text labels"""
    review_status: Any
    """Review status"""
    status: Any
    """Entity status"""
    summary_status: Any
    """Summary status"""
    tracking_urls: Any
    """Third-party tracking URLs"""
    type_: Any
    """Always 'pinpromotion'"""
    updated_time: Any
    """Last update timestamp (Unix seconds)"""
    view_tracking_url: Any
    """View tracking URL"""


class AdsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_account_id: str
    """Ad account ID"""
    ad_group_id: str
    """Ad group ID"""
    android_deep_link: str
    """Android deep link"""
    campaign_id: str
    """Campaign ID"""
    carousel_android_deep_links: str
    """Carousel Android deep links"""
    carousel_destination_urls: str
    """Carousel destination URLs"""
    carousel_ios_deep_links: str
    """Carousel iOS deep links"""
    click_tracking_url: str
    """Click tracking URL"""
    collection_items_destination_url_template: str
    """Template URL for collection items"""
    created_time: str
    """Creation timestamp (Unix seconds)"""
    creative_type: str
    """Creative type"""
    destination_url: str
    """Main destination URL"""
    id: str
    """Unique ad ID"""
    ios_deep_link: str
    """iOS deep link"""
    is_pin_deleted: str
    """Whether the original pin is deleted"""
    is_removable: str
    """Whether the ad is removable"""
    lead_form_id: str
    """Lead form ID"""
    name: str
    """Ad name"""
    pin_id: str
    """Associated pin ID"""
    rejected_reasons: str
    """Rejection reasons"""
    rejection_labels: str
    """Rejection text labels"""
    review_status: str
    """Review status"""
    status: str
    """Entity status"""
    summary_status: str
    """Summary status"""
    tracking_urls: str
    """Third-party tracking URLs"""
    type_: str
    """Always 'pinpromotion'"""
    updated_time: str
    """Last update timestamp (Unix seconds)"""
    view_tracking_url: str
    """View tracking URL"""


class AdsSortFilter(TypedDict, total=False):
    """Available fields for sorting ads search results."""
    ad_account_id: AirbyteSortOrder
    """Ad account ID"""
    ad_group_id: AirbyteSortOrder
    """Ad group ID"""
    android_deep_link: AirbyteSortOrder
    """Android deep link"""
    campaign_id: AirbyteSortOrder
    """Campaign ID"""
    carousel_android_deep_links: AirbyteSortOrder
    """Carousel Android deep links"""
    carousel_destination_urls: AirbyteSortOrder
    """Carousel destination URLs"""
    carousel_ios_deep_links: AirbyteSortOrder
    """Carousel iOS deep links"""
    click_tracking_url: AirbyteSortOrder
    """Click tracking URL"""
    collection_items_destination_url_template: AirbyteSortOrder
    """Template URL for collection items"""
    created_time: AirbyteSortOrder
    """Creation timestamp (Unix seconds)"""
    creative_type: AirbyteSortOrder
    """Creative type"""
    destination_url: AirbyteSortOrder
    """Main destination URL"""
    id: AirbyteSortOrder
    """Unique ad ID"""
    ios_deep_link: AirbyteSortOrder
    """iOS deep link"""
    is_pin_deleted: AirbyteSortOrder
    """Whether the original pin is deleted"""
    is_removable: AirbyteSortOrder
    """Whether the ad is removable"""
    lead_form_id: AirbyteSortOrder
    """Lead form ID"""
    name: AirbyteSortOrder
    """Ad name"""
    pin_id: AirbyteSortOrder
    """Associated pin ID"""
    rejected_reasons: AirbyteSortOrder
    """Rejection reasons"""
    rejection_labels: AirbyteSortOrder
    """Rejection text labels"""
    review_status: AirbyteSortOrder
    """Review status"""
    status: AirbyteSortOrder
    """Entity status"""
    summary_status: AirbyteSortOrder
    """Summary status"""
    tracking_urls: AirbyteSortOrder
    """Third-party tracking URLs"""
    type_: AirbyteSortOrder
    """Always 'pinpromotion'"""
    updated_time: AirbyteSortOrder
    """Last update timestamp (Unix seconds)"""
    view_tracking_url: AirbyteSortOrder
    """View tracking URL"""


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


# ===== BOARD_SECTIONS SEARCH TYPES =====

class BoardSectionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering board_sections search queries."""
    id: str | None
    """Unique identifier for the board section"""
    name: str | None
    """Name of the board section"""


class BoardSectionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the board section"""
    name: list[str]
    """Name of the board section"""


class BoardSectionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the board section"""
    name: Any
    """Name of the board section"""


class BoardSectionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the board section"""
    name: str
    """Name of the board section"""


class BoardSectionsSortFilter(TypedDict, total=False):
    """Available fields for sorting board_sections search results."""
    id: AirbyteSortOrder
    """Unique identifier for the board section"""
    name: AirbyteSortOrder
    """Name of the board section"""


# Entity-specific condition types for board_sections
class BoardSectionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BoardSectionsSearchFilter


class BoardSectionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BoardSectionsSearchFilter


class BoardSectionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BoardSectionsSearchFilter


class BoardSectionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BoardSectionsSearchFilter


class BoardSectionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BoardSectionsSearchFilter


class BoardSectionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BoardSectionsSearchFilter


class BoardSectionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BoardSectionsStringFilter


class BoardSectionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BoardSectionsStringFilter


class BoardSectionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BoardSectionsStringFilter


class BoardSectionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BoardSectionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BoardSectionsInCondition = TypedDict("BoardSectionsInCondition", {"in": BoardSectionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BoardSectionsNotCondition = TypedDict("BoardSectionsNotCondition", {"not": "BoardSectionsCondition"}, total=False)
"""Negates the nested condition."""

BoardSectionsAndCondition = TypedDict("BoardSectionsAndCondition", {"and": "list[BoardSectionsCondition]"}, total=False)
"""True if all nested conditions are true."""

BoardSectionsOrCondition = TypedDict("BoardSectionsOrCondition", {"or": "list[BoardSectionsCondition]"}, total=False)
"""True if any nested condition is true."""

BoardSectionsAnyCondition = TypedDict("BoardSectionsAnyCondition", {"any": BoardSectionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all board_sections condition types
BoardSectionsCondition = (
    BoardSectionsEqCondition
    | BoardSectionsNeqCondition
    | BoardSectionsGtCondition
    | BoardSectionsGteCondition
    | BoardSectionsLtCondition
    | BoardSectionsLteCondition
    | BoardSectionsInCondition
    | BoardSectionsLikeCondition
    | BoardSectionsFuzzyCondition
    | BoardSectionsKeywordCondition
    | BoardSectionsContainsCondition
    | BoardSectionsNotCondition
    | BoardSectionsAndCondition
    | BoardSectionsOrCondition
    | BoardSectionsAnyCondition
)


class BoardSectionsSearchQuery(TypedDict, total=False):
    """Search query for board_sections entity."""
    filter: BoardSectionsCondition
    sort: list[BoardSectionsSortFilter]


# ===== BOARD_PINS SEARCH TYPES =====

class BoardPinsSearchFilter(TypedDict, total=False):
    """Available fields for filtering board_pins search queries."""
    alt_text: str | None
    """Alternate text for accessibility"""
    board_id: str | None
    """Board the pin belongs to"""
    board_owner: dict[str, Any] | None
    """Board owner info"""
    board_section_id: str | None
    """Section within the board"""
    created_at: str | None
    """Timestamp when the pin was created"""
    creative_type: str | None
    """Creative type"""
    description: str | None
    """Pin description"""
    dominant_color: str | None
    """Dominant color from the pin image"""
    has_been_promoted: bool | None
    """Whether the pin has been promoted"""
    id: str | None
    """Unique pin identifier"""
    is_owner: bool | None
    """Whether the current user is the owner"""
    is_standard: bool | None
    """Whether the pin is a standard pin"""
    link: str | None
    """URL link associated with the pin"""
    media: dict[str, Any] | None
    """Media content"""
    parent_pin_id: str | None
    """Parent pin ID if this is a repin"""
    pin_metrics: dict[str, Any] | None
    """Pin metrics data"""
    title: str | None
    """Pin title"""


class BoardPinsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    alt_text: list[str]
    """Alternate text for accessibility"""
    board_id: list[str]
    """Board the pin belongs to"""
    board_owner: list[dict[str, Any]]
    """Board owner info"""
    board_section_id: list[str]
    """Section within the board"""
    created_at: list[str]
    """Timestamp when the pin was created"""
    creative_type: list[str]
    """Creative type"""
    description: list[str]
    """Pin description"""
    dominant_color: list[str]
    """Dominant color from the pin image"""
    has_been_promoted: list[bool]
    """Whether the pin has been promoted"""
    id: list[str]
    """Unique pin identifier"""
    is_owner: list[bool]
    """Whether the current user is the owner"""
    is_standard: list[bool]
    """Whether the pin is a standard pin"""
    link: list[str]
    """URL link associated with the pin"""
    media: list[dict[str, Any]]
    """Media content"""
    parent_pin_id: list[str]
    """Parent pin ID if this is a repin"""
    pin_metrics: list[dict[str, Any]]
    """Pin metrics data"""
    title: list[str]
    """Pin title"""


class BoardPinsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    alt_text: Any
    """Alternate text for accessibility"""
    board_id: Any
    """Board the pin belongs to"""
    board_owner: Any
    """Board owner info"""
    board_section_id: Any
    """Section within the board"""
    created_at: Any
    """Timestamp when the pin was created"""
    creative_type: Any
    """Creative type"""
    description: Any
    """Pin description"""
    dominant_color: Any
    """Dominant color from the pin image"""
    has_been_promoted: Any
    """Whether the pin has been promoted"""
    id: Any
    """Unique pin identifier"""
    is_owner: Any
    """Whether the current user is the owner"""
    is_standard: Any
    """Whether the pin is a standard pin"""
    link: Any
    """URL link associated with the pin"""
    media: Any
    """Media content"""
    parent_pin_id: Any
    """Parent pin ID if this is a repin"""
    pin_metrics: Any
    """Pin metrics data"""
    title: Any
    """Pin title"""


class BoardPinsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    alt_text: str
    """Alternate text for accessibility"""
    board_id: str
    """Board the pin belongs to"""
    board_owner: str
    """Board owner info"""
    board_section_id: str
    """Section within the board"""
    created_at: str
    """Timestamp when the pin was created"""
    creative_type: str
    """Creative type"""
    description: str
    """Pin description"""
    dominant_color: str
    """Dominant color from the pin image"""
    has_been_promoted: str
    """Whether the pin has been promoted"""
    id: str
    """Unique pin identifier"""
    is_owner: str
    """Whether the current user is the owner"""
    is_standard: str
    """Whether the pin is a standard pin"""
    link: str
    """URL link associated with the pin"""
    media: str
    """Media content"""
    parent_pin_id: str
    """Parent pin ID if this is a repin"""
    pin_metrics: str
    """Pin metrics data"""
    title: str
    """Pin title"""


class BoardPinsSortFilter(TypedDict, total=False):
    """Available fields for sorting board_pins search results."""
    alt_text: AirbyteSortOrder
    """Alternate text for accessibility"""
    board_id: AirbyteSortOrder
    """Board the pin belongs to"""
    board_owner: AirbyteSortOrder
    """Board owner info"""
    board_section_id: AirbyteSortOrder
    """Section within the board"""
    created_at: AirbyteSortOrder
    """Timestamp when the pin was created"""
    creative_type: AirbyteSortOrder
    """Creative type"""
    description: AirbyteSortOrder
    """Pin description"""
    dominant_color: AirbyteSortOrder
    """Dominant color from the pin image"""
    has_been_promoted: AirbyteSortOrder
    """Whether the pin has been promoted"""
    id: AirbyteSortOrder
    """Unique pin identifier"""
    is_owner: AirbyteSortOrder
    """Whether the current user is the owner"""
    is_standard: AirbyteSortOrder
    """Whether the pin is a standard pin"""
    link: AirbyteSortOrder
    """URL link associated with the pin"""
    media: AirbyteSortOrder
    """Media content"""
    parent_pin_id: AirbyteSortOrder
    """Parent pin ID if this is a repin"""
    pin_metrics: AirbyteSortOrder
    """Pin metrics data"""
    title: AirbyteSortOrder
    """Pin title"""


# Entity-specific condition types for board_pins
class BoardPinsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BoardPinsSearchFilter


class BoardPinsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BoardPinsSearchFilter


class BoardPinsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BoardPinsSearchFilter


class BoardPinsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BoardPinsSearchFilter


class BoardPinsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BoardPinsSearchFilter


class BoardPinsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BoardPinsSearchFilter


class BoardPinsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BoardPinsStringFilter


class BoardPinsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BoardPinsStringFilter


class BoardPinsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BoardPinsStringFilter


class BoardPinsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BoardPinsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BoardPinsInCondition = TypedDict("BoardPinsInCondition", {"in": BoardPinsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BoardPinsNotCondition = TypedDict("BoardPinsNotCondition", {"not": "BoardPinsCondition"}, total=False)
"""Negates the nested condition."""

BoardPinsAndCondition = TypedDict("BoardPinsAndCondition", {"and": "list[BoardPinsCondition]"}, total=False)
"""True if all nested conditions are true."""

BoardPinsOrCondition = TypedDict("BoardPinsOrCondition", {"or": "list[BoardPinsCondition]"}, total=False)
"""True if any nested condition is true."""

BoardPinsAnyCondition = TypedDict("BoardPinsAnyCondition", {"any": BoardPinsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all board_pins condition types
BoardPinsCondition = (
    BoardPinsEqCondition
    | BoardPinsNeqCondition
    | BoardPinsGtCondition
    | BoardPinsGteCondition
    | BoardPinsLtCondition
    | BoardPinsLteCondition
    | BoardPinsInCondition
    | BoardPinsLikeCondition
    | BoardPinsFuzzyCondition
    | BoardPinsKeywordCondition
    | BoardPinsContainsCondition
    | BoardPinsNotCondition
    | BoardPinsAndCondition
    | BoardPinsOrCondition
    | BoardPinsAnyCondition
)


class BoardPinsSearchQuery(TypedDict, total=False):
    """Search query for board_pins entity."""
    filter: BoardPinsCondition
    sort: list[BoardPinsSortFilter]


# ===== CATALOGS SEARCH TYPES =====

class CatalogsSearchFilter(TypedDict, total=False):
    """Available fields for filtering catalogs search queries."""
    catalog_type: str | None
    """Type of catalog"""
    created_at: str | None
    """Timestamp when the catalog was created"""
    id: str | None
    """Unique catalog identifier"""
    name: str | None
    """Catalog name"""
    updated_at: str | None
    """Timestamp when the catalog was last updated"""


class CatalogsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    catalog_type: list[str]
    """Type of catalog"""
    created_at: list[str]
    """Timestamp when the catalog was created"""
    id: list[str]
    """Unique catalog identifier"""
    name: list[str]
    """Catalog name"""
    updated_at: list[str]
    """Timestamp when the catalog was last updated"""


class CatalogsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    catalog_type: Any
    """Type of catalog"""
    created_at: Any
    """Timestamp when the catalog was created"""
    id: Any
    """Unique catalog identifier"""
    name: Any
    """Catalog name"""
    updated_at: Any
    """Timestamp when the catalog was last updated"""


class CatalogsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    catalog_type: str
    """Type of catalog"""
    created_at: str
    """Timestamp when the catalog was created"""
    id: str
    """Unique catalog identifier"""
    name: str
    """Catalog name"""
    updated_at: str
    """Timestamp when the catalog was last updated"""


class CatalogsSortFilter(TypedDict, total=False):
    """Available fields for sorting catalogs search results."""
    catalog_type: AirbyteSortOrder
    """Type of catalog"""
    created_at: AirbyteSortOrder
    """Timestamp when the catalog was created"""
    id: AirbyteSortOrder
    """Unique catalog identifier"""
    name: AirbyteSortOrder
    """Catalog name"""
    updated_at: AirbyteSortOrder
    """Timestamp when the catalog was last updated"""


# Entity-specific condition types for catalogs
class CatalogsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CatalogsSearchFilter


class CatalogsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CatalogsSearchFilter


class CatalogsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CatalogsSearchFilter


class CatalogsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CatalogsSearchFilter


class CatalogsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CatalogsSearchFilter


class CatalogsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CatalogsSearchFilter


class CatalogsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CatalogsStringFilter


class CatalogsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CatalogsStringFilter


class CatalogsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CatalogsStringFilter


class CatalogsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CatalogsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CatalogsInCondition = TypedDict("CatalogsInCondition", {"in": CatalogsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CatalogsNotCondition = TypedDict("CatalogsNotCondition", {"not": "CatalogsCondition"}, total=False)
"""Negates the nested condition."""

CatalogsAndCondition = TypedDict("CatalogsAndCondition", {"and": "list[CatalogsCondition]"}, total=False)
"""True if all nested conditions are true."""

CatalogsOrCondition = TypedDict("CatalogsOrCondition", {"or": "list[CatalogsCondition]"}, total=False)
"""True if any nested condition is true."""

CatalogsAnyCondition = TypedDict("CatalogsAnyCondition", {"any": CatalogsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all catalogs condition types
CatalogsCondition = (
    CatalogsEqCondition
    | CatalogsNeqCondition
    | CatalogsGtCondition
    | CatalogsGteCondition
    | CatalogsLtCondition
    | CatalogsLteCondition
    | CatalogsInCondition
    | CatalogsLikeCondition
    | CatalogsFuzzyCondition
    | CatalogsKeywordCondition
    | CatalogsContainsCondition
    | CatalogsNotCondition
    | CatalogsAndCondition
    | CatalogsOrCondition
    | CatalogsAnyCondition
)


class CatalogsSearchQuery(TypedDict, total=False):
    """Search query for catalogs entity."""
    filter: CatalogsCondition
    sort: list[CatalogsSortFilter]


# ===== CATALOGS_FEEDS SEARCH TYPES =====

class CatalogsFeedsSearchFilter(TypedDict, total=False):
    """Available fields for filtering catalogs_feeds search queries."""
    catalog_type: str | None
    """Type of catalog"""
    created_at: str | None
    """Timestamp when the feed was created"""
    default_availability: str | None
    """Default availability status"""
    default_country: str | None
    """Default country"""
    default_currency: str | None
    """Default currency for pricing"""
    default_locale: str | None
    """Default locale"""
    format: str | None
    """Feed format"""
    id: str | None
    """Unique feed identifier"""
    location: str | None
    """URL where the feed is available"""
    name: str | None
    """Feed name"""
    preferred_processing_schedule: dict[str, Any] | None
    """Preferred processing schedule"""
    status: str | None
    """Feed status"""
    updated_at: str | None
    """Timestamp when the feed was last updated"""


class CatalogsFeedsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    catalog_type: list[str]
    """Type of catalog"""
    created_at: list[str]
    """Timestamp when the feed was created"""
    default_availability: list[str]
    """Default availability status"""
    default_country: list[str]
    """Default country"""
    default_currency: list[str]
    """Default currency for pricing"""
    default_locale: list[str]
    """Default locale"""
    format: list[str]
    """Feed format"""
    id: list[str]
    """Unique feed identifier"""
    location: list[str]
    """URL where the feed is available"""
    name: list[str]
    """Feed name"""
    preferred_processing_schedule: list[dict[str, Any]]
    """Preferred processing schedule"""
    status: list[str]
    """Feed status"""
    updated_at: list[str]
    """Timestamp when the feed was last updated"""


class CatalogsFeedsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    catalog_type: Any
    """Type of catalog"""
    created_at: Any
    """Timestamp when the feed was created"""
    default_availability: Any
    """Default availability status"""
    default_country: Any
    """Default country"""
    default_currency: Any
    """Default currency for pricing"""
    default_locale: Any
    """Default locale"""
    format: Any
    """Feed format"""
    id: Any
    """Unique feed identifier"""
    location: Any
    """URL where the feed is available"""
    name: Any
    """Feed name"""
    preferred_processing_schedule: Any
    """Preferred processing schedule"""
    status: Any
    """Feed status"""
    updated_at: Any
    """Timestamp when the feed was last updated"""


class CatalogsFeedsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    catalog_type: str
    """Type of catalog"""
    created_at: str
    """Timestamp when the feed was created"""
    default_availability: str
    """Default availability status"""
    default_country: str
    """Default country"""
    default_currency: str
    """Default currency for pricing"""
    default_locale: str
    """Default locale"""
    format: str
    """Feed format"""
    id: str
    """Unique feed identifier"""
    location: str
    """URL where the feed is available"""
    name: str
    """Feed name"""
    preferred_processing_schedule: str
    """Preferred processing schedule"""
    status: str
    """Feed status"""
    updated_at: str
    """Timestamp when the feed was last updated"""


class CatalogsFeedsSortFilter(TypedDict, total=False):
    """Available fields for sorting catalogs_feeds search results."""
    catalog_type: AirbyteSortOrder
    """Type of catalog"""
    created_at: AirbyteSortOrder
    """Timestamp when the feed was created"""
    default_availability: AirbyteSortOrder
    """Default availability status"""
    default_country: AirbyteSortOrder
    """Default country"""
    default_currency: AirbyteSortOrder
    """Default currency for pricing"""
    default_locale: AirbyteSortOrder
    """Default locale"""
    format: AirbyteSortOrder
    """Feed format"""
    id: AirbyteSortOrder
    """Unique feed identifier"""
    location: AirbyteSortOrder
    """URL where the feed is available"""
    name: AirbyteSortOrder
    """Feed name"""
    preferred_processing_schedule: AirbyteSortOrder
    """Preferred processing schedule"""
    status: AirbyteSortOrder
    """Feed status"""
    updated_at: AirbyteSortOrder
    """Timestamp when the feed was last updated"""


# Entity-specific condition types for catalogs_feeds
class CatalogsFeedsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CatalogsFeedsSearchFilter


class CatalogsFeedsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CatalogsFeedsSearchFilter


class CatalogsFeedsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CatalogsFeedsSearchFilter


class CatalogsFeedsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CatalogsFeedsSearchFilter


class CatalogsFeedsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CatalogsFeedsSearchFilter


class CatalogsFeedsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CatalogsFeedsSearchFilter


class CatalogsFeedsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CatalogsFeedsStringFilter


class CatalogsFeedsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CatalogsFeedsStringFilter


class CatalogsFeedsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CatalogsFeedsStringFilter


class CatalogsFeedsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CatalogsFeedsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CatalogsFeedsInCondition = TypedDict("CatalogsFeedsInCondition", {"in": CatalogsFeedsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CatalogsFeedsNotCondition = TypedDict("CatalogsFeedsNotCondition", {"not": "CatalogsFeedsCondition"}, total=False)
"""Negates the nested condition."""

CatalogsFeedsAndCondition = TypedDict("CatalogsFeedsAndCondition", {"and": "list[CatalogsFeedsCondition]"}, total=False)
"""True if all nested conditions are true."""

CatalogsFeedsOrCondition = TypedDict("CatalogsFeedsOrCondition", {"or": "list[CatalogsFeedsCondition]"}, total=False)
"""True if any nested condition is true."""

CatalogsFeedsAnyCondition = TypedDict("CatalogsFeedsAnyCondition", {"any": CatalogsFeedsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all catalogs_feeds condition types
CatalogsFeedsCondition = (
    CatalogsFeedsEqCondition
    | CatalogsFeedsNeqCondition
    | CatalogsFeedsGtCondition
    | CatalogsFeedsGteCondition
    | CatalogsFeedsLtCondition
    | CatalogsFeedsLteCondition
    | CatalogsFeedsInCondition
    | CatalogsFeedsLikeCondition
    | CatalogsFeedsFuzzyCondition
    | CatalogsFeedsKeywordCondition
    | CatalogsFeedsContainsCondition
    | CatalogsFeedsNotCondition
    | CatalogsFeedsAndCondition
    | CatalogsFeedsOrCondition
    | CatalogsFeedsAnyCondition
)


class CatalogsFeedsSearchQuery(TypedDict, total=False):
    """Search query for catalogs_feeds entity."""
    filter: CatalogsFeedsCondition
    sort: list[CatalogsFeedsSortFilter]


# ===== CATALOGS_PRODUCT_GROUPS SEARCH TYPES =====

class CatalogsProductGroupsSearchFilter(TypedDict, total=False):
    """Available fields for filtering catalogs_product_groups search queries."""
    created_at: int | None
    """Creation timestamp (Unix seconds)"""
    description: str | None
    """Product group description"""
    feed_id: str | None
    """Associated feed ID"""
    id: str | None
    """Unique product group identifier"""
    is_featured: bool | None
    """Whether the product group is featured"""
    name: str | None
    """Product group name"""
    status: str | None
    """Product group status"""
    type_: str | None
    """Product group type"""
    updated_at: int | None
    """Last update timestamp (Unix seconds)"""


class CatalogsProductGroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[int]
    """Creation timestamp (Unix seconds)"""
    description: list[str]
    """Product group description"""
    feed_id: list[str]
    """Associated feed ID"""
    id: list[str]
    """Unique product group identifier"""
    is_featured: list[bool]
    """Whether the product group is featured"""
    name: list[str]
    """Product group name"""
    status: list[str]
    """Product group status"""
    type_: list[str]
    """Product group type"""
    updated_at: list[int]
    """Last update timestamp (Unix seconds)"""


class CatalogsProductGroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """Creation timestamp (Unix seconds)"""
    description: Any
    """Product group description"""
    feed_id: Any
    """Associated feed ID"""
    id: Any
    """Unique product group identifier"""
    is_featured: Any
    """Whether the product group is featured"""
    name: Any
    """Product group name"""
    status: Any
    """Product group status"""
    type_: Any
    """Product group type"""
    updated_at: Any
    """Last update timestamp (Unix seconds)"""


class CatalogsProductGroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """Creation timestamp (Unix seconds)"""
    description: str
    """Product group description"""
    feed_id: str
    """Associated feed ID"""
    id: str
    """Unique product group identifier"""
    is_featured: str
    """Whether the product group is featured"""
    name: str
    """Product group name"""
    status: str
    """Product group status"""
    type_: str
    """Product group type"""
    updated_at: str
    """Last update timestamp (Unix seconds)"""


class CatalogsProductGroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting catalogs_product_groups search results."""
    created_at: AirbyteSortOrder
    """Creation timestamp (Unix seconds)"""
    description: AirbyteSortOrder
    """Product group description"""
    feed_id: AirbyteSortOrder
    """Associated feed ID"""
    id: AirbyteSortOrder
    """Unique product group identifier"""
    is_featured: AirbyteSortOrder
    """Whether the product group is featured"""
    name: AirbyteSortOrder
    """Product group name"""
    status: AirbyteSortOrder
    """Product group status"""
    type_: AirbyteSortOrder
    """Product group type"""
    updated_at: AirbyteSortOrder
    """Last update timestamp (Unix seconds)"""


# Entity-specific condition types for catalogs_product_groups
class CatalogsProductGroupsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CatalogsProductGroupsSearchFilter


class CatalogsProductGroupsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CatalogsProductGroupsSearchFilter


class CatalogsProductGroupsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CatalogsProductGroupsSearchFilter


class CatalogsProductGroupsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CatalogsProductGroupsSearchFilter


class CatalogsProductGroupsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CatalogsProductGroupsSearchFilter


class CatalogsProductGroupsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CatalogsProductGroupsSearchFilter


class CatalogsProductGroupsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CatalogsProductGroupsStringFilter


class CatalogsProductGroupsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CatalogsProductGroupsStringFilter


class CatalogsProductGroupsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CatalogsProductGroupsStringFilter


class CatalogsProductGroupsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CatalogsProductGroupsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CatalogsProductGroupsInCondition = TypedDict("CatalogsProductGroupsInCondition", {"in": CatalogsProductGroupsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CatalogsProductGroupsNotCondition = TypedDict("CatalogsProductGroupsNotCondition", {"not": "CatalogsProductGroupsCondition"}, total=False)
"""Negates the nested condition."""

CatalogsProductGroupsAndCondition = TypedDict("CatalogsProductGroupsAndCondition", {"and": "list[CatalogsProductGroupsCondition]"}, total=False)
"""True if all nested conditions are true."""

CatalogsProductGroupsOrCondition = TypedDict("CatalogsProductGroupsOrCondition", {"or": "list[CatalogsProductGroupsCondition]"}, total=False)
"""True if any nested condition is true."""

CatalogsProductGroupsAnyCondition = TypedDict("CatalogsProductGroupsAnyCondition", {"any": CatalogsProductGroupsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all catalogs_product_groups condition types
CatalogsProductGroupsCondition = (
    CatalogsProductGroupsEqCondition
    | CatalogsProductGroupsNeqCondition
    | CatalogsProductGroupsGtCondition
    | CatalogsProductGroupsGteCondition
    | CatalogsProductGroupsLtCondition
    | CatalogsProductGroupsLteCondition
    | CatalogsProductGroupsInCondition
    | CatalogsProductGroupsLikeCondition
    | CatalogsProductGroupsFuzzyCondition
    | CatalogsProductGroupsKeywordCondition
    | CatalogsProductGroupsContainsCondition
    | CatalogsProductGroupsNotCondition
    | CatalogsProductGroupsAndCondition
    | CatalogsProductGroupsOrCondition
    | CatalogsProductGroupsAnyCondition
)


class CatalogsProductGroupsSearchQuery(TypedDict, total=False):
    """Search query for catalogs_product_groups entity."""
    filter: CatalogsProductGroupsCondition
    sort: list[CatalogsProductGroupsSortFilter]


# ===== AUDIENCES SEARCH TYPES =====

class AudiencesSearchFilter(TypedDict, total=False):
    """Available fields for filtering audiences search queries."""
    ad_account_id: str | None
    """Ad account ID"""
    audience_type: str | None
    """Audience type"""
    created_timestamp: int | None
    """Creation time (Unix seconds)"""
    description: str | None
    """Audience description"""
    id: str | None
    """Unique audience identifier"""
    name: str | None
    """Audience name"""
    rule: dict[str, Any] | None
    """Audience targeting rules"""
    size: int | None
    """Estimated audience size"""
    status: str | None
    """Audience status"""
    type_: str | None
    """Always 'audience'"""
    updated_timestamp: int | None
    """Last update time (Unix seconds)"""


class AudiencesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_account_id: list[str]
    """Ad account ID"""
    audience_type: list[str]
    """Audience type"""
    created_timestamp: list[int]
    """Creation time (Unix seconds)"""
    description: list[str]
    """Audience description"""
    id: list[str]
    """Unique audience identifier"""
    name: list[str]
    """Audience name"""
    rule: list[dict[str, Any]]
    """Audience targeting rules"""
    size: list[int]
    """Estimated audience size"""
    status: list[str]
    """Audience status"""
    type_: list[str]
    """Always 'audience'"""
    updated_timestamp: list[int]
    """Last update time (Unix seconds)"""


class AudiencesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_account_id: Any
    """Ad account ID"""
    audience_type: Any
    """Audience type"""
    created_timestamp: Any
    """Creation time (Unix seconds)"""
    description: Any
    """Audience description"""
    id: Any
    """Unique audience identifier"""
    name: Any
    """Audience name"""
    rule: Any
    """Audience targeting rules"""
    size: Any
    """Estimated audience size"""
    status: Any
    """Audience status"""
    type_: Any
    """Always 'audience'"""
    updated_timestamp: Any
    """Last update time (Unix seconds)"""


class AudiencesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_account_id: str
    """Ad account ID"""
    audience_type: str
    """Audience type"""
    created_timestamp: str
    """Creation time (Unix seconds)"""
    description: str
    """Audience description"""
    id: str
    """Unique audience identifier"""
    name: str
    """Audience name"""
    rule: str
    """Audience targeting rules"""
    size: str
    """Estimated audience size"""
    status: str
    """Audience status"""
    type_: str
    """Always 'audience'"""
    updated_timestamp: str
    """Last update time (Unix seconds)"""


class AudiencesSortFilter(TypedDict, total=False):
    """Available fields for sorting audiences search results."""
    ad_account_id: AirbyteSortOrder
    """Ad account ID"""
    audience_type: AirbyteSortOrder
    """Audience type"""
    created_timestamp: AirbyteSortOrder
    """Creation time (Unix seconds)"""
    description: AirbyteSortOrder
    """Audience description"""
    id: AirbyteSortOrder
    """Unique audience identifier"""
    name: AirbyteSortOrder
    """Audience name"""
    rule: AirbyteSortOrder
    """Audience targeting rules"""
    size: AirbyteSortOrder
    """Estimated audience size"""
    status: AirbyteSortOrder
    """Audience status"""
    type_: AirbyteSortOrder
    """Always 'audience'"""
    updated_timestamp: AirbyteSortOrder
    """Last update time (Unix seconds)"""


# Entity-specific condition types for audiences
class AudiencesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AudiencesSearchFilter


class AudiencesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AudiencesSearchFilter


class AudiencesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AudiencesSearchFilter


class AudiencesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AudiencesSearchFilter


class AudiencesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AudiencesSearchFilter


class AudiencesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AudiencesSearchFilter


class AudiencesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AudiencesStringFilter


class AudiencesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AudiencesStringFilter


class AudiencesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AudiencesStringFilter


class AudiencesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AudiencesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AudiencesInCondition = TypedDict("AudiencesInCondition", {"in": AudiencesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AudiencesNotCondition = TypedDict("AudiencesNotCondition", {"not": "AudiencesCondition"}, total=False)
"""Negates the nested condition."""

AudiencesAndCondition = TypedDict("AudiencesAndCondition", {"and": "list[AudiencesCondition]"}, total=False)
"""True if all nested conditions are true."""

AudiencesOrCondition = TypedDict("AudiencesOrCondition", {"or": "list[AudiencesCondition]"}, total=False)
"""True if any nested condition is true."""

AudiencesAnyCondition = TypedDict("AudiencesAnyCondition", {"any": AudiencesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all audiences condition types
AudiencesCondition = (
    AudiencesEqCondition
    | AudiencesNeqCondition
    | AudiencesGtCondition
    | AudiencesGteCondition
    | AudiencesLtCondition
    | AudiencesLteCondition
    | AudiencesInCondition
    | AudiencesLikeCondition
    | AudiencesFuzzyCondition
    | AudiencesKeywordCondition
    | AudiencesContainsCondition
    | AudiencesNotCondition
    | AudiencesAndCondition
    | AudiencesOrCondition
    | AudiencesAnyCondition
)


class AudiencesSearchQuery(TypedDict, total=False):
    """Search query for audiences entity."""
    filter: AudiencesCondition
    sort: list[AudiencesSortFilter]


# ===== CONVERSION_TAGS SEARCH TYPES =====

class ConversionTagsSearchFilter(TypedDict, total=False):
    """Available fields for filtering conversion_tags search queries."""
    ad_account_id: str | None
    """Ad account ID"""
    code_snippet: str | None
    """JavaScript code snippet for tracking"""
    configs: dict[str, Any] | None
    """Tag configurations"""
    enhanced_match_status: str | None
    """Enhanced match status"""
    id: str | None
    """Unique conversion tag identifier"""
    last_fired_time_ms: int | None
    """Timestamp of last event fired (milliseconds)"""
    name: str | None
    """Conversion tag name"""
    status: str | None
    """Status"""
    version: str | None
    """Version number"""


class ConversionTagsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_account_id: list[str]
    """Ad account ID"""
    code_snippet: list[str]
    """JavaScript code snippet for tracking"""
    configs: list[dict[str, Any]]
    """Tag configurations"""
    enhanced_match_status: list[str]
    """Enhanced match status"""
    id: list[str]
    """Unique conversion tag identifier"""
    last_fired_time_ms: list[int]
    """Timestamp of last event fired (milliseconds)"""
    name: list[str]
    """Conversion tag name"""
    status: list[str]
    """Status"""
    version: list[str]
    """Version number"""


class ConversionTagsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_account_id: Any
    """Ad account ID"""
    code_snippet: Any
    """JavaScript code snippet for tracking"""
    configs: Any
    """Tag configurations"""
    enhanced_match_status: Any
    """Enhanced match status"""
    id: Any
    """Unique conversion tag identifier"""
    last_fired_time_ms: Any
    """Timestamp of last event fired (milliseconds)"""
    name: Any
    """Conversion tag name"""
    status: Any
    """Status"""
    version: Any
    """Version number"""


class ConversionTagsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_account_id: str
    """Ad account ID"""
    code_snippet: str
    """JavaScript code snippet for tracking"""
    configs: str
    """Tag configurations"""
    enhanced_match_status: str
    """Enhanced match status"""
    id: str
    """Unique conversion tag identifier"""
    last_fired_time_ms: str
    """Timestamp of last event fired (milliseconds)"""
    name: str
    """Conversion tag name"""
    status: str
    """Status"""
    version: str
    """Version number"""


class ConversionTagsSortFilter(TypedDict, total=False):
    """Available fields for sorting conversion_tags search results."""
    ad_account_id: AirbyteSortOrder
    """Ad account ID"""
    code_snippet: AirbyteSortOrder
    """JavaScript code snippet for tracking"""
    configs: AirbyteSortOrder
    """Tag configurations"""
    enhanced_match_status: AirbyteSortOrder
    """Enhanced match status"""
    id: AirbyteSortOrder
    """Unique conversion tag identifier"""
    last_fired_time_ms: AirbyteSortOrder
    """Timestamp of last event fired (milliseconds)"""
    name: AirbyteSortOrder
    """Conversion tag name"""
    status: AirbyteSortOrder
    """Status"""
    version: AirbyteSortOrder
    """Version number"""


# Entity-specific condition types for conversion_tags
class ConversionTagsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ConversionTagsSearchFilter


class ConversionTagsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ConversionTagsSearchFilter


class ConversionTagsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ConversionTagsSearchFilter


class ConversionTagsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ConversionTagsSearchFilter


class ConversionTagsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ConversionTagsSearchFilter


class ConversionTagsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ConversionTagsSearchFilter


class ConversionTagsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ConversionTagsStringFilter


class ConversionTagsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ConversionTagsStringFilter


class ConversionTagsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ConversionTagsStringFilter


class ConversionTagsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ConversionTagsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ConversionTagsInCondition = TypedDict("ConversionTagsInCondition", {"in": ConversionTagsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ConversionTagsNotCondition = TypedDict("ConversionTagsNotCondition", {"not": "ConversionTagsCondition"}, total=False)
"""Negates the nested condition."""

ConversionTagsAndCondition = TypedDict("ConversionTagsAndCondition", {"and": "list[ConversionTagsCondition]"}, total=False)
"""True if all nested conditions are true."""

ConversionTagsOrCondition = TypedDict("ConversionTagsOrCondition", {"or": "list[ConversionTagsCondition]"}, total=False)
"""True if any nested condition is true."""

ConversionTagsAnyCondition = TypedDict("ConversionTagsAnyCondition", {"any": ConversionTagsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all conversion_tags condition types
ConversionTagsCondition = (
    ConversionTagsEqCondition
    | ConversionTagsNeqCondition
    | ConversionTagsGtCondition
    | ConversionTagsGteCondition
    | ConversionTagsLtCondition
    | ConversionTagsLteCondition
    | ConversionTagsInCondition
    | ConversionTagsLikeCondition
    | ConversionTagsFuzzyCondition
    | ConversionTagsKeywordCondition
    | ConversionTagsContainsCondition
    | ConversionTagsNotCondition
    | ConversionTagsAndCondition
    | ConversionTagsOrCondition
    | ConversionTagsAnyCondition
)


class ConversionTagsSearchQuery(TypedDict, total=False):
    """Search query for conversion_tags entity."""
    filter: ConversionTagsCondition
    sort: list[ConversionTagsSortFilter]


# ===== CUSTOMER_LISTS SEARCH TYPES =====

class CustomerListsSearchFilter(TypedDict, total=False):
    """Available fields for filtering customer_lists search queries."""
    ad_account_id: str | None
    """Associated ad account ID"""
    created_time: int | None
    """Creation time (Unix seconds)"""
    id: str | None
    """Unique customer list identifier"""
    name: str | None
    """Customer list name"""
    num_batches: int | None
    """Total number of list updates"""
    num_removed_user_records: int | None
    """Count of removed user records"""
    num_uploaded_user_records: int | None
    """Count of uploaded user records"""
    status: str | None
    """Status"""
    type_: str | None
    """Always 'customerlist'"""
    updated_time: int | None
    """Last update time (Unix seconds)"""


class CustomerListsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_account_id: list[str]
    """Associated ad account ID"""
    created_time: list[int]
    """Creation time (Unix seconds)"""
    id: list[str]
    """Unique customer list identifier"""
    name: list[str]
    """Customer list name"""
    num_batches: list[int]
    """Total number of list updates"""
    num_removed_user_records: list[int]
    """Count of removed user records"""
    num_uploaded_user_records: list[int]
    """Count of uploaded user records"""
    status: list[str]
    """Status"""
    type_: list[str]
    """Always 'customerlist'"""
    updated_time: list[int]
    """Last update time (Unix seconds)"""


class CustomerListsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_account_id: Any
    """Associated ad account ID"""
    created_time: Any
    """Creation time (Unix seconds)"""
    id: Any
    """Unique customer list identifier"""
    name: Any
    """Customer list name"""
    num_batches: Any
    """Total number of list updates"""
    num_removed_user_records: Any
    """Count of removed user records"""
    num_uploaded_user_records: Any
    """Count of uploaded user records"""
    status: Any
    """Status"""
    type_: Any
    """Always 'customerlist'"""
    updated_time: Any
    """Last update time (Unix seconds)"""


class CustomerListsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_account_id: str
    """Associated ad account ID"""
    created_time: str
    """Creation time (Unix seconds)"""
    id: str
    """Unique customer list identifier"""
    name: str
    """Customer list name"""
    num_batches: str
    """Total number of list updates"""
    num_removed_user_records: str
    """Count of removed user records"""
    num_uploaded_user_records: str
    """Count of uploaded user records"""
    status: str
    """Status"""
    type_: str
    """Always 'customerlist'"""
    updated_time: str
    """Last update time (Unix seconds)"""


class CustomerListsSortFilter(TypedDict, total=False):
    """Available fields for sorting customer_lists search results."""
    ad_account_id: AirbyteSortOrder
    """Associated ad account ID"""
    created_time: AirbyteSortOrder
    """Creation time (Unix seconds)"""
    id: AirbyteSortOrder
    """Unique customer list identifier"""
    name: AirbyteSortOrder
    """Customer list name"""
    num_batches: AirbyteSortOrder
    """Total number of list updates"""
    num_removed_user_records: AirbyteSortOrder
    """Count of removed user records"""
    num_uploaded_user_records: AirbyteSortOrder
    """Count of uploaded user records"""
    status: AirbyteSortOrder
    """Status"""
    type_: AirbyteSortOrder
    """Always 'customerlist'"""
    updated_time: AirbyteSortOrder
    """Last update time (Unix seconds)"""


# Entity-specific condition types for customer_lists
class CustomerListsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CustomerListsSearchFilter


class CustomerListsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CustomerListsSearchFilter


class CustomerListsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CustomerListsSearchFilter


class CustomerListsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CustomerListsSearchFilter


class CustomerListsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CustomerListsSearchFilter


class CustomerListsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CustomerListsSearchFilter


class CustomerListsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CustomerListsStringFilter


class CustomerListsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CustomerListsStringFilter


class CustomerListsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CustomerListsStringFilter


class CustomerListsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CustomerListsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CustomerListsInCondition = TypedDict("CustomerListsInCondition", {"in": CustomerListsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CustomerListsNotCondition = TypedDict("CustomerListsNotCondition", {"not": "CustomerListsCondition"}, total=False)
"""Negates the nested condition."""

CustomerListsAndCondition = TypedDict("CustomerListsAndCondition", {"and": "list[CustomerListsCondition]"}, total=False)
"""True if all nested conditions are true."""

CustomerListsOrCondition = TypedDict("CustomerListsOrCondition", {"or": "list[CustomerListsCondition]"}, total=False)
"""True if any nested condition is true."""

CustomerListsAnyCondition = TypedDict("CustomerListsAnyCondition", {"any": CustomerListsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all customer_lists condition types
CustomerListsCondition = (
    CustomerListsEqCondition
    | CustomerListsNeqCondition
    | CustomerListsGtCondition
    | CustomerListsGteCondition
    | CustomerListsLtCondition
    | CustomerListsLteCondition
    | CustomerListsInCondition
    | CustomerListsLikeCondition
    | CustomerListsFuzzyCondition
    | CustomerListsKeywordCondition
    | CustomerListsContainsCondition
    | CustomerListsNotCondition
    | CustomerListsAndCondition
    | CustomerListsOrCondition
    | CustomerListsAnyCondition
)


class CustomerListsSearchQuery(TypedDict, total=False):
    """Search query for customer_lists entity."""
    filter: CustomerListsCondition
    sort: list[CustomerListsSortFilter]


# ===== KEYWORDS SEARCH TYPES =====

class KeywordsSearchFilter(TypedDict, total=False):
    """Available fields for filtering keywords search queries."""
    archived: bool | None
    """Whether the keyword is archived"""
    bid: int | None
    """Bid value in microcurrency"""
    id: str | None
    """Unique keyword identifier"""
    match_type: str | None
    """Match type"""
    parent_id: str | None
    """Parent entity ID"""
    parent_type: str | None
    """Parent entity type"""
    type_: str | None
    """Always 'keyword'"""
    value: str | None
    """Keyword text value"""


class KeywordsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Whether the keyword is archived"""
    bid: list[int]
    """Bid value in microcurrency"""
    id: list[str]
    """Unique keyword identifier"""
    match_type: list[str]
    """Match type"""
    parent_id: list[str]
    """Parent entity ID"""
    parent_type: list[str]
    """Parent entity type"""
    type_: list[str]
    """Always 'keyword'"""
    value: list[str]
    """Keyword text value"""


class KeywordsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Whether the keyword is archived"""
    bid: Any
    """Bid value in microcurrency"""
    id: Any
    """Unique keyword identifier"""
    match_type: Any
    """Match type"""
    parent_id: Any
    """Parent entity ID"""
    parent_type: Any
    """Parent entity type"""
    type_: Any
    """Always 'keyword'"""
    value: Any
    """Keyword text value"""


class KeywordsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Whether the keyword is archived"""
    bid: str
    """Bid value in microcurrency"""
    id: str
    """Unique keyword identifier"""
    match_type: str
    """Match type"""
    parent_id: str
    """Parent entity ID"""
    parent_type: str
    """Parent entity type"""
    type_: str
    """Always 'keyword'"""
    value: str
    """Keyword text value"""


class KeywordsSortFilter(TypedDict, total=False):
    """Available fields for sorting keywords search results."""
    archived: AirbyteSortOrder
    """Whether the keyword is archived"""
    bid: AirbyteSortOrder
    """Bid value in microcurrency"""
    id: AirbyteSortOrder
    """Unique keyword identifier"""
    match_type: AirbyteSortOrder
    """Match type"""
    parent_id: AirbyteSortOrder
    """Parent entity ID"""
    parent_type: AirbyteSortOrder
    """Parent entity type"""
    type_: AirbyteSortOrder
    """Always 'keyword'"""
    value: AirbyteSortOrder
    """Keyword text value"""


# Entity-specific condition types for keywords
class KeywordsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: KeywordsSearchFilter


class KeywordsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: KeywordsSearchFilter


class KeywordsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: KeywordsSearchFilter


class KeywordsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: KeywordsSearchFilter


class KeywordsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: KeywordsSearchFilter


class KeywordsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: KeywordsSearchFilter


class KeywordsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: KeywordsStringFilter


class KeywordsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: KeywordsStringFilter


class KeywordsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: KeywordsStringFilter


class KeywordsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: KeywordsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
KeywordsInCondition = TypedDict("KeywordsInCondition", {"in": KeywordsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

KeywordsNotCondition = TypedDict("KeywordsNotCondition", {"not": "KeywordsCondition"}, total=False)
"""Negates the nested condition."""

KeywordsAndCondition = TypedDict("KeywordsAndCondition", {"and": "list[KeywordsCondition]"}, total=False)
"""True if all nested conditions are true."""

KeywordsOrCondition = TypedDict("KeywordsOrCondition", {"or": "list[KeywordsCondition]"}, total=False)
"""True if any nested condition is true."""

KeywordsAnyCondition = TypedDict("KeywordsAnyCondition", {"any": KeywordsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all keywords condition types
KeywordsCondition = (
    KeywordsEqCondition
    | KeywordsNeqCondition
    | KeywordsGtCondition
    | KeywordsGteCondition
    | KeywordsLtCondition
    | KeywordsLteCondition
    | KeywordsInCondition
    | KeywordsLikeCondition
    | KeywordsFuzzyCondition
    | KeywordsKeywordCondition
    | KeywordsContainsCondition
    | KeywordsNotCondition
    | KeywordsAndCondition
    | KeywordsOrCondition
    | KeywordsAnyCondition
)


class KeywordsSearchQuery(TypedDict, total=False):
    """Search query for keywords entity."""
    filter: KeywordsCondition
    sort: list[KeywordsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
