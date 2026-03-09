"""
Type definitions for linkedin-ads connector.
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

class AccountsListParams(TypedDict):
    """Parameters for accounts.list operation"""
    q: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class AccountsGetParams(TypedDict):
    """Parameters for accounts.get operation"""
    id: str

class AccountUsersListParams(TypedDict):
    """Parameters for account_users.list operation"""
    q: str
    accounts: str
    count: NotRequired[int]
    start: NotRequired[int]

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    account_id: str
    q: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class CampaignsGetParams(TypedDict):
    """Parameters for campaigns.get operation"""
    account_id: str
    id: str

class CampaignGroupsListParams(TypedDict):
    """Parameters for campaign_groups.list operation"""
    account_id: str
    q: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class CampaignGroupsGetParams(TypedDict):
    """Parameters for campaign_groups.get operation"""
    account_id: str
    id: str

class CreativesListParams(TypedDict):
    """Parameters for creatives.list operation"""
    account_id: str
    q: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class CreativesGetParams(TypedDict):
    """Parameters for creatives.get operation"""
    account_id: str
    id: str

class ConversionsListParams(TypedDict):
    """Parameters for conversions.list operation"""
    q: str
    account: str
    count: NotRequired[int]
    start: NotRequired[int]

class ConversionsGetParams(TypedDict):
    """Parameters for conversions.get operation"""
    id: str

class AdCampaignAnalyticsListParams(TypedDict):
    """Parameters for ad_campaign_analytics.list operation"""
    q: str
    pivot: str
    time_granularity: str
    date_range: str
    campaigns: str
    fields: NotRequired[str]

class AdCreativeAnalyticsListParams(TypedDict):
    """Parameters for ad_creative_analytics.list operation"""
    q: str
    pivot: str
    time_granularity: str
    date_range: str
    creatives: str
    fields: NotRequired[str]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ACCOUNTS SEARCH TYPES =====

class AccountsSearchFilter(TypedDict, total=False):
    """Available fields for filtering accounts search queries."""
    id: int | None
    """Unique account identifier"""
    name: str | None
    """Account name"""
    currency: str | None
    """Currency code used by the account"""
    status: str | None
    """Account status"""
    type_: str | None
    """Account type"""
    reference: str | None
    """Reference organization URN"""
    test: bool | None
    """Whether this is a test account"""
    notified_on_campaign_optimization: bool | None
    """Flag for notifications on campaign optimization"""
    notified_on_creative_approval: bool | None
    """Flag for notifications on creative approval"""
    notified_on_creative_rejection: bool | None
    """Flag for notifications on creative rejection"""
    notified_on_end_of_campaign: bool | None
    """Flag for notifications on end of campaign"""
    notified_on_new_features_enabled: bool | None
    """Flag for notifications on new features"""
    serving_statuses: list[Any] | None
    """List of serving statuses"""
    version: dict[str, Any] | None
    """Version information"""


class AccountsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique account identifier"""
    name: list[str]
    """Account name"""
    currency: list[str]
    """Currency code used by the account"""
    status: list[str]
    """Account status"""
    type_: list[str]
    """Account type"""
    reference: list[str]
    """Reference organization URN"""
    test: list[bool]
    """Whether this is a test account"""
    notified_on_campaign_optimization: list[bool]
    """Flag for notifications on campaign optimization"""
    notified_on_creative_approval: list[bool]
    """Flag for notifications on creative approval"""
    notified_on_creative_rejection: list[bool]
    """Flag for notifications on creative rejection"""
    notified_on_end_of_campaign: list[bool]
    """Flag for notifications on end of campaign"""
    notified_on_new_features_enabled: list[bool]
    """Flag for notifications on new features"""
    serving_statuses: list[list[Any]]
    """List of serving statuses"""
    version: list[dict[str, Any]]
    """Version information"""


class AccountsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique account identifier"""
    name: Any
    """Account name"""
    currency: Any
    """Currency code used by the account"""
    status: Any
    """Account status"""
    type_: Any
    """Account type"""
    reference: Any
    """Reference organization URN"""
    test: Any
    """Whether this is a test account"""
    notified_on_campaign_optimization: Any
    """Flag for notifications on campaign optimization"""
    notified_on_creative_approval: Any
    """Flag for notifications on creative approval"""
    notified_on_creative_rejection: Any
    """Flag for notifications on creative rejection"""
    notified_on_end_of_campaign: Any
    """Flag for notifications on end of campaign"""
    notified_on_new_features_enabled: Any
    """Flag for notifications on new features"""
    serving_statuses: Any
    """List of serving statuses"""
    version: Any
    """Version information"""


class AccountsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique account identifier"""
    name: str
    """Account name"""
    currency: str
    """Currency code used by the account"""
    status: str
    """Account status"""
    type_: str
    """Account type"""
    reference: str
    """Reference organization URN"""
    test: str
    """Whether this is a test account"""
    notified_on_campaign_optimization: str
    """Flag for notifications on campaign optimization"""
    notified_on_creative_approval: str
    """Flag for notifications on creative approval"""
    notified_on_creative_rejection: str
    """Flag for notifications on creative rejection"""
    notified_on_end_of_campaign: str
    """Flag for notifications on end of campaign"""
    notified_on_new_features_enabled: str
    """Flag for notifications on new features"""
    serving_statuses: str
    """List of serving statuses"""
    version: str
    """Version information"""


class AccountsSortFilter(TypedDict, total=False):
    """Available fields for sorting accounts search results."""
    id: AirbyteSortOrder
    """Unique account identifier"""
    name: AirbyteSortOrder
    """Account name"""
    currency: AirbyteSortOrder
    """Currency code used by the account"""
    status: AirbyteSortOrder
    """Account status"""
    type_: AirbyteSortOrder
    """Account type"""
    reference: AirbyteSortOrder
    """Reference organization URN"""
    test: AirbyteSortOrder
    """Whether this is a test account"""
    notified_on_campaign_optimization: AirbyteSortOrder
    """Flag for notifications on campaign optimization"""
    notified_on_creative_approval: AirbyteSortOrder
    """Flag for notifications on creative approval"""
    notified_on_creative_rejection: AirbyteSortOrder
    """Flag for notifications on creative rejection"""
    notified_on_end_of_campaign: AirbyteSortOrder
    """Flag for notifications on end of campaign"""
    notified_on_new_features_enabled: AirbyteSortOrder
    """Flag for notifications on new features"""
    serving_statuses: AirbyteSortOrder
    """List of serving statuses"""
    version: AirbyteSortOrder
    """Version information"""


# Entity-specific condition types for accounts
class AccountsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AccountsSearchFilter


class AccountsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AccountsSearchFilter


class AccountsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AccountsSearchFilter


class AccountsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AccountsSearchFilter


class AccountsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AccountsSearchFilter


class AccountsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AccountsSearchFilter


class AccountsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AccountsStringFilter


class AccountsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AccountsStringFilter


class AccountsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AccountsStringFilter


class AccountsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AccountsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AccountsInCondition = TypedDict("AccountsInCondition", {"in": AccountsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AccountsNotCondition = TypedDict("AccountsNotCondition", {"not": "AccountsCondition"}, total=False)
"""Negates the nested condition."""

AccountsAndCondition = TypedDict("AccountsAndCondition", {"and": "list[AccountsCondition]"}, total=False)
"""True if all nested conditions are true."""

AccountsOrCondition = TypedDict("AccountsOrCondition", {"or": "list[AccountsCondition]"}, total=False)
"""True if any nested condition is true."""

AccountsAnyCondition = TypedDict("AccountsAnyCondition", {"any": AccountsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all accounts condition types
AccountsCondition = (
    AccountsEqCondition
    | AccountsNeqCondition
    | AccountsGtCondition
    | AccountsGteCondition
    | AccountsLtCondition
    | AccountsLteCondition
    | AccountsInCondition
    | AccountsLikeCondition
    | AccountsFuzzyCondition
    | AccountsKeywordCondition
    | AccountsContainsCondition
    | AccountsNotCondition
    | AccountsAndCondition
    | AccountsOrCondition
    | AccountsAnyCondition
)


class AccountsSearchQuery(TypedDict, total=False):
    """Search query for accounts entity."""
    filter: AccountsCondition
    sort: list[AccountsSortFilter]


# ===== ACCOUNT_USERS SEARCH TYPES =====

class AccountUsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering account_users search queries."""
    account: str | None
    """Associated account URN"""
    user: str | None
    """User URN"""
    role: str | None
    """User role in the account"""


class AccountUsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account: list[str]
    """Associated account URN"""
    user: list[str]
    """User URN"""
    role: list[str]
    """User role in the account"""


class AccountUsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account: Any
    """Associated account URN"""
    user: Any
    """User URN"""
    role: Any
    """User role in the account"""


class AccountUsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    account: str
    """Associated account URN"""
    user: str
    """User URN"""
    role: str
    """User role in the account"""


class AccountUsersSortFilter(TypedDict, total=False):
    """Available fields for sorting account_users search results."""
    account: AirbyteSortOrder
    """Associated account URN"""
    user: AirbyteSortOrder
    """User URN"""
    role: AirbyteSortOrder
    """User role in the account"""


# Entity-specific condition types for account_users
class AccountUsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AccountUsersSearchFilter


class AccountUsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AccountUsersSearchFilter


class AccountUsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AccountUsersSearchFilter


class AccountUsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AccountUsersSearchFilter


class AccountUsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AccountUsersSearchFilter


class AccountUsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AccountUsersSearchFilter


class AccountUsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AccountUsersStringFilter


class AccountUsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AccountUsersStringFilter


class AccountUsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AccountUsersStringFilter


class AccountUsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AccountUsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AccountUsersInCondition = TypedDict("AccountUsersInCondition", {"in": AccountUsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AccountUsersNotCondition = TypedDict("AccountUsersNotCondition", {"not": "AccountUsersCondition"}, total=False)
"""Negates the nested condition."""

AccountUsersAndCondition = TypedDict("AccountUsersAndCondition", {"and": "list[AccountUsersCondition]"}, total=False)
"""True if all nested conditions are true."""

AccountUsersOrCondition = TypedDict("AccountUsersOrCondition", {"or": "list[AccountUsersCondition]"}, total=False)
"""True if any nested condition is true."""

AccountUsersAnyCondition = TypedDict("AccountUsersAnyCondition", {"any": AccountUsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all account_users condition types
AccountUsersCondition = (
    AccountUsersEqCondition
    | AccountUsersNeqCondition
    | AccountUsersGtCondition
    | AccountUsersGteCondition
    | AccountUsersLtCondition
    | AccountUsersLteCondition
    | AccountUsersInCondition
    | AccountUsersLikeCondition
    | AccountUsersFuzzyCondition
    | AccountUsersKeywordCondition
    | AccountUsersContainsCondition
    | AccountUsersNotCondition
    | AccountUsersAndCondition
    | AccountUsersOrCondition
    | AccountUsersAnyCondition
)


class AccountUsersSearchQuery(TypedDict, total=False):
    """Search query for account_users entity."""
    filter: AccountUsersCondition
    sort: list[AccountUsersSortFilter]


# ===== CAMPAIGNS SEARCH TYPES =====

class CampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaigns search queries."""
    id: int | None
    """Unique campaign identifier"""
    name: str | None
    """Campaign name"""
    account: str | None
    """Associated account URN"""
    campaign_group: str | None
    """Parent campaign group URN"""
    status: str | None
    """Campaign status"""
    type_: str | None
    """Campaign type"""
    cost_type: str | None
    """Cost type (CPC CPM etc)"""
    format: str | None
    """Campaign ad format"""
    objective_type: str | None
    """Campaign objective type"""
    optimization_target_type: str | None
    """Optimization target type"""
    creative_selection: str | None
    """Creative selection mode"""
    pacing_strategy: str | None
    """Budget pacing strategy"""
    audience_expansion_enabled: bool | None
    """Whether audience expansion is enabled"""
    offsite_delivery_enabled: bool | None
    """Whether offsite delivery is enabled"""
    story_delivery_enabled: bool | None
    """Whether story delivery is enabled"""
    test: bool | None
    """Whether this is a test campaign"""
    associated_entity: str | None
    """Associated entity URN"""
    daily_budget: dict[str, Any] | None
    """Daily budget configuration"""
    total_budget: dict[str, Any] | None
    """Total budget configuration"""
    unit_cost: dict[str, Any] | None
    """Cost per unit (bid amount)"""
    run_schedule: dict[str, Any] | None
    """Campaign run schedule"""
    locale: dict[str, Any] | None
    """Campaign locale settings"""
    serving_statuses: list[Any] | None
    """List of serving statuses"""
    version: dict[str, Any] | None
    """Version information"""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique campaign identifier"""
    name: list[str]
    """Campaign name"""
    account: list[str]
    """Associated account URN"""
    campaign_group: list[str]
    """Parent campaign group URN"""
    status: list[str]
    """Campaign status"""
    type_: list[str]
    """Campaign type"""
    cost_type: list[str]
    """Cost type (CPC CPM etc)"""
    format: list[str]
    """Campaign ad format"""
    objective_type: list[str]
    """Campaign objective type"""
    optimization_target_type: list[str]
    """Optimization target type"""
    creative_selection: list[str]
    """Creative selection mode"""
    pacing_strategy: list[str]
    """Budget pacing strategy"""
    audience_expansion_enabled: list[bool]
    """Whether audience expansion is enabled"""
    offsite_delivery_enabled: list[bool]
    """Whether offsite delivery is enabled"""
    story_delivery_enabled: list[bool]
    """Whether story delivery is enabled"""
    test: list[bool]
    """Whether this is a test campaign"""
    associated_entity: list[str]
    """Associated entity URN"""
    daily_budget: list[dict[str, Any]]
    """Daily budget configuration"""
    total_budget: list[dict[str, Any]]
    """Total budget configuration"""
    unit_cost: list[dict[str, Any]]
    """Cost per unit (bid amount)"""
    run_schedule: list[dict[str, Any]]
    """Campaign run schedule"""
    locale: list[dict[str, Any]]
    """Campaign locale settings"""
    serving_statuses: list[list[Any]]
    """List of serving statuses"""
    version: list[dict[str, Any]]
    """Version information"""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique campaign identifier"""
    name: Any
    """Campaign name"""
    account: Any
    """Associated account URN"""
    campaign_group: Any
    """Parent campaign group URN"""
    status: Any
    """Campaign status"""
    type_: Any
    """Campaign type"""
    cost_type: Any
    """Cost type (CPC CPM etc)"""
    format: Any
    """Campaign ad format"""
    objective_type: Any
    """Campaign objective type"""
    optimization_target_type: Any
    """Optimization target type"""
    creative_selection: Any
    """Creative selection mode"""
    pacing_strategy: Any
    """Budget pacing strategy"""
    audience_expansion_enabled: Any
    """Whether audience expansion is enabled"""
    offsite_delivery_enabled: Any
    """Whether offsite delivery is enabled"""
    story_delivery_enabled: Any
    """Whether story delivery is enabled"""
    test: Any
    """Whether this is a test campaign"""
    associated_entity: Any
    """Associated entity URN"""
    daily_budget: Any
    """Daily budget configuration"""
    total_budget: Any
    """Total budget configuration"""
    unit_cost: Any
    """Cost per unit (bid amount)"""
    run_schedule: Any
    """Campaign run schedule"""
    locale: Any
    """Campaign locale settings"""
    serving_statuses: Any
    """List of serving statuses"""
    version: Any
    """Version information"""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique campaign identifier"""
    name: str
    """Campaign name"""
    account: str
    """Associated account URN"""
    campaign_group: str
    """Parent campaign group URN"""
    status: str
    """Campaign status"""
    type_: str
    """Campaign type"""
    cost_type: str
    """Cost type (CPC CPM etc)"""
    format: str
    """Campaign ad format"""
    objective_type: str
    """Campaign objective type"""
    optimization_target_type: str
    """Optimization target type"""
    creative_selection: str
    """Creative selection mode"""
    pacing_strategy: str
    """Budget pacing strategy"""
    audience_expansion_enabled: str
    """Whether audience expansion is enabled"""
    offsite_delivery_enabled: str
    """Whether offsite delivery is enabled"""
    story_delivery_enabled: str
    """Whether story delivery is enabled"""
    test: str
    """Whether this is a test campaign"""
    associated_entity: str
    """Associated entity URN"""
    daily_budget: str
    """Daily budget configuration"""
    total_budget: str
    """Total budget configuration"""
    unit_cost: str
    """Cost per unit (bid amount)"""
    run_schedule: str
    """Campaign run schedule"""
    locale: str
    """Campaign locale settings"""
    serving_statuses: str
    """List of serving statuses"""
    version: str
    """Version information"""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    id: AirbyteSortOrder
    """Unique campaign identifier"""
    name: AirbyteSortOrder
    """Campaign name"""
    account: AirbyteSortOrder
    """Associated account URN"""
    campaign_group: AirbyteSortOrder
    """Parent campaign group URN"""
    status: AirbyteSortOrder
    """Campaign status"""
    type_: AirbyteSortOrder
    """Campaign type"""
    cost_type: AirbyteSortOrder
    """Cost type (CPC CPM etc)"""
    format: AirbyteSortOrder
    """Campaign ad format"""
    objective_type: AirbyteSortOrder
    """Campaign objective type"""
    optimization_target_type: AirbyteSortOrder
    """Optimization target type"""
    creative_selection: AirbyteSortOrder
    """Creative selection mode"""
    pacing_strategy: AirbyteSortOrder
    """Budget pacing strategy"""
    audience_expansion_enabled: AirbyteSortOrder
    """Whether audience expansion is enabled"""
    offsite_delivery_enabled: AirbyteSortOrder
    """Whether offsite delivery is enabled"""
    story_delivery_enabled: AirbyteSortOrder
    """Whether story delivery is enabled"""
    test: AirbyteSortOrder
    """Whether this is a test campaign"""
    associated_entity: AirbyteSortOrder
    """Associated entity URN"""
    daily_budget: AirbyteSortOrder
    """Daily budget configuration"""
    total_budget: AirbyteSortOrder
    """Total budget configuration"""
    unit_cost: AirbyteSortOrder
    """Cost per unit (bid amount)"""
    run_schedule: AirbyteSortOrder
    """Campaign run schedule"""
    locale: AirbyteSortOrder
    """Campaign locale settings"""
    serving_statuses: AirbyteSortOrder
    """List of serving statuses"""
    version: AirbyteSortOrder
    """Version information"""


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


# ===== CAMPAIGN_GROUPS SEARCH TYPES =====

class CampaignGroupsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaign_groups search queries."""
    id: int | None
    """Unique campaign group identifier"""
    name: str | None
    """Campaign group name"""
    account: str | None
    """Associated account URN"""
    status: str | None
    """Campaign group status"""
    test: bool | None
    """Whether this is a test campaign group"""
    backfilled: bool | None
    """Whether the campaign group is backfilled"""
    total_budget: dict[str, Any] | None
    """Total budget for the campaign group"""
    run_schedule: dict[str, Any] | None
    """Campaign group run schedule"""
    serving_statuses: list[Any] | None
    """List of serving statuses"""
    allowed_campaign_types: list[Any] | None
    """Types of campaigns allowed in this group"""


class CampaignGroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique campaign group identifier"""
    name: list[str]
    """Campaign group name"""
    account: list[str]
    """Associated account URN"""
    status: list[str]
    """Campaign group status"""
    test: list[bool]
    """Whether this is a test campaign group"""
    backfilled: list[bool]
    """Whether the campaign group is backfilled"""
    total_budget: list[dict[str, Any]]
    """Total budget for the campaign group"""
    run_schedule: list[dict[str, Any]]
    """Campaign group run schedule"""
    serving_statuses: list[list[Any]]
    """List of serving statuses"""
    allowed_campaign_types: list[list[Any]]
    """Types of campaigns allowed in this group"""


class CampaignGroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique campaign group identifier"""
    name: Any
    """Campaign group name"""
    account: Any
    """Associated account URN"""
    status: Any
    """Campaign group status"""
    test: Any
    """Whether this is a test campaign group"""
    backfilled: Any
    """Whether the campaign group is backfilled"""
    total_budget: Any
    """Total budget for the campaign group"""
    run_schedule: Any
    """Campaign group run schedule"""
    serving_statuses: Any
    """List of serving statuses"""
    allowed_campaign_types: Any
    """Types of campaigns allowed in this group"""


class CampaignGroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique campaign group identifier"""
    name: str
    """Campaign group name"""
    account: str
    """Associated account URN"""
    status: str
    """Campaign group status"""
    test: str
    """Whether this is a test campaign group"""
    backfilled: str
    """Whether the campaign group is backfilled"""
    total_budget: str
    """Total budget for the campaign group"""
    run_schedule: str
    """Campaign group run schedule"""
    serving_statuses: str
    """List of serving statuses"""
    allowed_campaign_types: str
    """Types of campaigns allowed in this group"""


class CampaignGroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaign_groups search results."""
    id: AirbyteSortOrder
    """Unique campaign group identifier"""
    name: AirbyteSortOrder
    """Campaign group name"""
    account: AirbyteSortOrder
    """Associated account URN"""
    status: AirbyteSortOrder
    """Campaign group status"""
    test: AirbyteSortOrder
    """Whether this is a test campaign group"""
    backfilled: AirbyteSortOrder
    """Whether the campaign group is backfilled"""
    total_budget: AirbyteSortOrder
    """Total budget for the campaign group"""
    run_schedule: AirbyteSortOrder
    """Campaign group run schedule"""
    serving_statuses: AirbyteSortOrder
    """List of serving statuses"""
    allowed_campaign_types: AirbyteSortOrder
    """Types of campaigns allowed in this group"""


# Entity-specific condition types for campaign_groups
class CampaignGroupsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CampaignGroupsSearchFilter


class CampaignGroupsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CampaignGroupsSearchFilter


class CampaignGroupsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CampaignGroupsSearchFilter


class CampaignGroupsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CampaignGroupsSearchFilter


class CampaignGroupsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CampaignGroupsSearchFilter


class CampaignGroupsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CampaignGroupsSearchFilter


class CampaignGroupsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CampaignGroupsStringFilter


class CampaignGroupsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CampaignGroupsStringFilter


class CampaignGroupsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CampaignGroupsStringFilter


class CampaignGroupsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CampaignGroupsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CampaignGroupsInCondition = TypedDict("CampaignGroupsInCondition", {"in": CampaignGroupsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CampaignGroupsNotCondition = TypedDict("CampaignGroupsNotCondition", {"not": "CampaignGroupsCondition"}, total=False)
"""Negates the nested condition."""

CampaignGroupsAndCondition = TypedDict("CampaignGroupsAndCondition", {"and": "list[CampaignGroupsCondition]"}, total=False)
"""True if all nested conditions are true."""

CampaignGroupsOrCondition = TypedDict("CampaignGroupsOrCondition", {"or": "list[CampaignGroupsCondition]"}, total=False)
"""True if any nested condition is true."""

CampaignGroupsAnyCondition = TypedDict("CampaignGroupsAnyCondition", {"any": CampaignGroupsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all campaign_groups condition types
CampaignGroupsCondition = (
    CampaignGroupsEqCondition
    | CampaignGroupsNeqCondition
    | CampaignGroupsGtCondition
    | CampaignGroupsGteCondition
    | CampaignGroupsLtCondition
    | CampaignGroupsLteCondition
    | CampaignGroupsInCondition
    | CampaignGroupsLikeCondition
    | CampaignGroupsFuzzyCondition
    | CampaignGroupsKeywordCondition
    | CampaignGroupsContainsCondition
    | CampaignGroupsNotCondition
    | CampaignGroupsAndCondition
    | CampaignGroupsOrCondition
    | CampaignGroupsAnyCondition
)


class CampaignGroupsSearchQuery(TypedDict, total=False):
    """Search query for campaign_groups entity."""
    filter: CampaignGroupsCondition
    sort: list[CampaignGroupsSortFilter]


# ===== CREATIVES SEARCH TYPES =====

class CreativesSearchFilter(TypedDict, total=False):
    """Available fields for filtering creatives search queries."""
    id: str | None
    """Unique creative identifier"""
    name: str | None
    """Creative name"""
    account: str | None
    """Associated account URN"""
    campaign: str | None
    """Parent campaign URN"""
    intended_status: str | None
    """Intended creative status"""
    is_serving: bool | None
    """Whether the creative is currently serving"""
    is_test: bool | None
    """Whether this is a test creative"""
    created_at: int | None
    """Creation timestamp (epoch milliseconds)"""
    created_by: str | None
    """URN of the user who created the creative"""
    last_modified_at: int | None
    """Last modification timestamp (epoch milliseconds)"""
    last_modified_by: str | None
    """URN of the user who last modified the creative"""
    content: dict[str, Any] | None
    """Creative content configuration"""
    serving_hold_reasons: list[Any] | None
    """Reasons for holding creative from serving"""


class CreativesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique creative identifier"""
    name: list[str]
    """Creative name"""
    account: list[str]
    """Associated account URN"""
    campaign: list[str]
    """Parent campaign URN"""
    intended_status: list[str]
    """Intended creative status"""
    is_serving: list[bool]
    """Whether the creative is currently serving"""
    is_test: list[bool]
    """Whether this is a test creative"""
    created_at: list[int]
    """Creation timestamp (epoch milliseconds)"""
    created_by: list[str]
    """URN of the user who created the creative"""
    last_modified_at: list[int]
    """Last modification timestamp (epoch milliseconds)"""
    last_modified_by: list[str]
    """URN of the user who last modified the creative"""
    content: list[dict[str, Any]]
    """Creative content configuration"""
    serving_hold_reasons: list[list[Any]]
    """Reasons for holding creative from serving"""


class CreativesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique creative identifier"""
    name: Any
    """Creative name"""
    account: Any
    """Associated account URN"""
    campaign: Any
    """Parent campaign URN"""
    intended_status: Any
    """Intended creative status"""
    is_serving: Any
    """Whether the creative is currently serving"""
    is_test: Any
    """Whether this is a test creative"""
    created_at: Any
    """Creation timestamp (epoch milliseconds)"""
    created_by: Any
    """URN of the user who created the creative"""
    last_modified_at: Any
    """Last modification timestamp (epoch milliseconds)"""
    last_modified_by: Any
    """URN of the user who last modified the creative"""
    content: Any
    """Creative content configuration"""
    serving_hold_reasons: Any
    """Reasons for holding creative from serving"""


class CreativesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique creative identifier"""
    name: str
    """Creative name"""
    account: str
    """Associated account URN"""
    campaign: str
    """Parent campaign URN"""
    intended_status: str
    """Intended creative status"""
    is_serving: str
    """Whether the creative is currently serving"""
    is_test: str
    """Whether this is a test creative"""
    created_at: str
    """Creation timestamp (epoch milliseconds)"""
    created_by: str
    """URN of the user who created the creative"""
    last_modified_at: str
    """Last modification timestamp (epoch milliseconds)"""
    last_modified_by: str
    """URN of the user who last modified the creative"""
    content: str
    """Creative content configuration"""
    serving_hold_reasons: str
    """Reasons for holding creative from serving"""


class CreativesSortFilter(TypedDict, total=False):
    """Available fields for sorting creatives search results."""
    id: AirbyteSortOrder
    """Unique creative identifier"""
    name: AirbyteSortOrder
    """Creative name"""
    account: AirbyteSortOrder
    """Associated account URN"""
    campaign: AirbyteSortOrder
    """Parent campaign URN"""
    intended_status: AirbyteSortOrder
    """Intended creative status"""
    is_serving: AirbyteSortOrder
    """Whether the creative is currently serving"""
    is_test: AirbyteSortOrder
    """Whether this is a test creative"""
    created_at: AirbyteSortOrder
    """Creation timestamp (epoch milliseconds)"""
    created_by: AirbyteSortOrder
    """URN of the user who created the creative"""
    last_modified_at: AirbyteSortOrder
    """Last modification timestamp (epoch milliseconds)"""
    last_modified_by: AirbyteSortOrder
    """URN of the user who last modified the creative"""
    content: AirbyteSortOrder
    """Creative content configuration"""
    serving_hold_reasons: AirbyteSortOrder
    """Reasons for holding creative from serving"""


# Entity-specific condition types for creatives
class CreativesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CreativesSearchFilter


class CreativesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CreativesSearchFilter


class CreativesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CreativesSearchFilter


class CreativesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CreativesSearchFilter


class CreativesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CreativesSearchFilter


class CreativesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CreativesSearchFilter


class CreativesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CreativesStringFilter


class CreativesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CreativesStringFilter


class CreativesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CreativesStringFilter


class CreativesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CreativesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CreativesInCondition = TypedDict("CreativesInCondition", {"in": CreativesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CreativesNotCondition = TypedDict("CreativesNotCondition", {"not": "CreativesCondition"}, total=False)
"""Negates the nested condition."""

CreativesAndCondition = TypedDict("CreativesAndCondition", {"and": "list[CreativesCondition]"}, total=False)
"""True if all nested conditions are true."""

CreativesOrCondition = TypedDict("CreativesOrCondition", {"or": "list[CreativesCondition]"}, total=False)
"""True if any nested condition is true."""

CreativesAnyCondition = TypedDict("CreativesAnyCondition", {"any": CreativesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all creatives condition types
CreativesCondition = (
    CreativesEqCondition
    | CreativesNeqCondition
    | CreativesGtCondition
    | CreativesGteCondition
    | CreativesLtCondition
    | CreativesLteCondition
    | CreativesInCondition
    | CreativesLikeCondition
    | CreativesFuzzyCondition
    | CreativesKeywordCondition
    | CreativesContainsCondition
    | CreativesNotCondition
    | CreativesAndCondition
    | CreativesOrCondition
    | CreativesAnyCondition
)


class CreativesSearchQuery(TypedDict, total=False):
    """Search query for creatives entity."""
    filter: CreativesCondition
    sort: list[CreativesSortFilter]


# ===== CONVERSIONS SEARCH TYPES =====

class ConversionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering conversions search queries."""
    id: int | None
    """Unique conversion identifier"""
    name: str | None
    """Conversion name"""
    account: str | None
    """Associated account URN"""
    type_: str | None
    """Conversion type"""
    attribution_type: str | None
    """Attribution type for the conversion"""
    enabled: bool | None
    """Whether the conversion tracking is enabled"""
    created: int | None
    """Creation timestamp (epoch milliseconds)"""
    last_modified: int | None
    """Last modification timestamp (epoch milliseconds)"""
    post_click_attribution_window_size: int | None
    """Post-click attribution window size in days"""
    view_through_attribution_window_size: int | None
    """View-through attribution window size in days"""
    campaigns: list[Any] | None
    """Related campaign URNs"""
    associated_campaigns: list[Any] | None
    """Associated campaigns"""
    image_pixel_tag: str | None
    """Image pixel tracking tag"""
    value: dict[str, Any] | None
    """Conversion value"""


class ConversionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique conversion identifier"""
    name: list[str]
    """Conversion name"""
    account: list[str]
    """Associated account URN"""
    type_: list[str]
    """Conversion type"""
    attribution_type: list[str]
    """Attribution type for the conversion"""
    enabled: list[bool]
    """Whether the conversion tracking is enabled"""
    created: list[int]
    """Creation timestamp (epoch milliseconds)"""
    last_modified: list[int]
    """Last modification timestamp (epoch milliseconds)"""
    post_click_attribution_window_size: list[int]
    """Post-click attribution window size in days"""
    view_through_attribution_window_size: list[int]
    """View-through attribution window size in days"""
    campaigns: list[list[Any]]
    """Related campaign URNs"""
    associated_campaigns: list[list[Any]]
    """Associated campaigns"""
    image_pixel_tag: list[str]
    """Image pixel tracking tag"""
    value: list[dict[str, Any]]
    """Conversion value"""


class ConversionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique conversion identifier"""
    name: Any
    """Conversion name"""
    account: Any
    """Associated account URN"""
    type_: Any
    """Conversion type"""
    attribution_type: Any
    """Attribution type for the conversion"""
    enabled: Any
    """Whether the conversion tracking is enabled"""
    created: Any
    """Creation timestamp (epoch milliseconds)"""
    last_modified: Any
    """Last modification timestamp (epoch milliseconds)"""
    post_click_attribution_window_size: Any
    """Post-click attribution window size in days"""
    view_through_attribution_window_size: Any
    """View-through attribution window size in days"""
    campaigns: Any
    """Related campaign URNs"""
    associated_campaigns: Any
    """Associated campaigns"""
    image_pixel_tag: Any
    """Image pixel tracking tag"""
    value: Any
    """Conversion value"""


class ConversionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique conversion identifier"""
    name: str
    """Conversion name"""
    account: str
    """Associated account URN"""
    type_: str
    """Conversion type"""
    attribution_type: str
    """Attribution type for the conversion"""
    enabled: str
    """Whether the conversion tracking is enabled"""
    created: str
    """Creation timestamp (epoch milliseconds)"""
    last_modified: str
    """Last modification timestamp (epoch milliseconds)"""
    post_click_attribution_window_size: str
    """Post-click attribution window size in days"""
    view_through_attribution_window_size: str
    """View-through attribution window size in days"""
    campaigns: str
    """Related campaign URNs"""
    associated_campaigns: str
    """Associated campaigns"""
    image_pixel_tag: str
    """Image pixel tracking tag"""
    value: str
    """Conversion value"""


class ConversionsSortFilter(TypedDict, total=False):
    """Available fields for sorting conversions search results."""
    id: AirbyteSortOrder
    """Unique conversion identifier"""
    name: AirbyteSortOrder
    """Conversion name"""
    account: AirbyteSortOrder
    """Associated account URN"""
    type_: AirbyteSortOrder
    """Conversion type"""
    attribution_type: AirbyteSortOrder
    """Attribution type for the conversion"""
    enabled: AirbyteSortOrder
    """Whether the conversion tracking is enabled"""
    created: AirbyteSortOrder
    """Creation timestamp (epoch milliseconds)"""
    last_modified: AirbyteSortOrder
    """Last modification timestamp (epoch milliseconds)"""
    post_click_attribution_window_size: AirbyteSortOrder
    """Post-click attribution window size in days"""
    view_through_attribution_window_size: AirbyteSortOrder
    """View-through attribution window size in days"""
    campaigns: AirbyteSortOrder
    """Related campaign URNs"""
    associated_campaigns: AirbyteSortOrder
    """Associated campaigns"""
    image_pixel_tag: AirbyteSortOrder
    """Image pixel tracking tag"""
    value: AirbyteSortOrder
    """Conversion value"""


# Entity-specific condition types for conversions
class ConversionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ConversionsSearchFilter


class ConversionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ConversionsSearchFilter


class ConversionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ConversionsSearchFilter


class ConversionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ConversionsSearchFilter


class ConversionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ConversionsSearchFilter


class ConversionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ConversionsSearchFilter


class ConversionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ConversionsStringFilter


class ConversionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ConversionsStringFilter


class ConversionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ConversionsStringFilter


class ConversionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ConversionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ConversionsInCondition = TypedDict("ConversionsInCondition", {"in": ConversionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ConversionsNotCondition = TypedDict("ConversionsNotCondition", {"not": "ConversionsCondition"}, total=False)
"""Negates the nested condition."""

ConversionsAndCondition = TypedDict("ConversionsAndCondition", {"and": "list[ConversionsCondition]"}, total=False)
"""True if all nested conditions are true."""

ConversionsOrCondition = TypedDict("ConversionsOrCondition", {"or": "list[ConversionsCondition]"}, total=False)
"""True if any nested condition is true."""

ConversionsAnyCondition = TypedDict("ConversionsAnyCondition", {"any": ConversionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all conversions condition types
ConversionsCondition = (
    ConversionsEqCondition
    | ConversionsNeqCondition
    | ConversionsGtCondition
    | ConversionsGteCondition
    | ConversionsLtCondition
    | ConversionsLteCondition
    | ConversionsInCondition
    | ConversionsLikeCondition
    | ConversionsFuzzyCondition
    | ConversionsKeywordCondition
    | ConversionsContainsCondition
    | ConversionsNotCondition
    | ConversionsAndCondition
    | ConversionsOrCondition
    | ConversionsAnyCondition
)


class ConversionsSearchQuery(TypedDict, total=False):
    """Search query for conversions entity."""
    filter: ConversionsCondition
    sort: list[ConversionsSortFilter]


# ===== AD_CAMPAIGN_ANALYTICS SEARCH TYPES =====

class AdCampaignAnalyticsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_campaign_analytics search queries."""
    impressions: float | None
    """Number of times the ad was shown"""
    clicks: float | None
    """Number of clicks on the ad"""
    cost_in_local_currency: float | None
    """Total cost in the accounts local currency"""
    cost_in_usd: float | None
    """Total cost in USD"""
    likes: float | None
    """Number of likes"""
    shares: float | None
    """Number of shares"""
    comments: float | None
    """Number of comments"""
    reactions: float | None
    """Number of reactions"""
    follows: float | None
    """Number of follows"""
    total_engagements: float | None
    """Total number of engagements"""
    landing_page_clicks: float | None
    """Number of landing page clicks"""
    company_page_clicks: float | None
    """Number of company page clicks"""
    external_website_conversions: float | None
    """Number of conversions on external websites"""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites"""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites"""
    conversion_value_in_local_currency: float | None
    """Conversion value in local currency"""
    approximate_member_reach: float | None
    """Approximate unique member reach"""
    card_clicks: float | None
    """Number of carousel card clicks"""
    card_impressions: float | None
    """Number of carousel card impressions"""
    video_starts: float | None
    """Number of video starts"""
    video_views: float | None
    """Number of video views"""
    video_first_quartile_completions: float | None
    """Number of times video played to 25%"""
    video_midpoint_completions: float | None
    """Number of times video played to 50%"""
    video_third_quartile_completions: float | None
    """Number of times video played to 75%"""
    video_completions: float | None
    """Number of times video played to 100%"""
    full_screen_plays: float | None
    """Number of full screen video plays"""
    one_click_leads: float | None
    """Number of one-click leads"""
    one_click_lead_form_opens: float | None
    """Number of one-click lead form opens"""
    other_engagements: float | None
    """Number of other engagements"""
    ad_unit_clicks: float | None
    """Number of ad unit clicks"""
    action_clicks: float | None
    """Number of action clicks"""
    text_url_clicks: float | None
    """Number of text URL clicks"""
    comment_likes: float | None
    """Number of comment likes"""
    sends: float | None
    """Number of sends (InMail)"""
    opens: float | None
    """Number of opens (InMail)"""
    download_clicks: float | None
    """Number of download clicks"""
    pivot_values: list[Any] | None
    """Pivot values (URNs) for this analytics record"""
    start_date: str | None
    """Start date of the ad analytics data"""
    end_date: str | None
    """End date of the ad analytics data"""


class AdCampaignAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    impressions: list[float]
    """Number of times the ad was shown"""
    clicks: list[float]
    """Number of clicks on the ad"""
    cost_in_local_currency: list[float]
    """Total cost in the accounts local currency"""
    cost_in_usd: list[float]
    """Total cost in USD"""
    likes: list[float]
    """Number of likes"""
    shares: list[float]
    """Number of shares"""
    comments: list[float]
    """Number of comments"""
    reactions: list[float]
    """Number of reactions"""
    follows: list[float]
    """Number of follows"""
    total_engagements: list[float]
    """Total number of engagements"""
    landing_page_clicks: list[float]
    """Number of landing page clicks"""
    company_page_clicks: list[float]
    """Number of company page clicks"""
    external_website_conversions: list[float]
    """Number of conversions on external websites"""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites"""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites"""
    conversion_value_in_local_currency: list[float]
    """Conversion value in local currency"""
    approximate_member_reach: list[float]
    """Approximate unique member reach"""
    card_clicks: list[float]
    """Number of carousel card clicks"""
    card_impressions: list[float]
    """Number of carousel card impressions"""
    video_starts: list[float]
    """Number of video starts"""
    video_views: list[float]
    """Number of video views"""
    video_first_quartile_completions: list[float]
    """Number of times video played to 25%"""
    video_midpoint_completions: list[float]
    """Number of times video played to 50%"""
    video_third_quartile_completions: list[float]
    """Number of times video played to 75%"""
    video_completions: list[float]
    """Number of times video played to 100%"""
    full_screen_plays: list[float]
    """Number of full screen video plays"""
    one_click_leads: list[float]
    """Number of one-click leads"""
    one_click_lead_form_opens: list[float]
    """Number of one-click lead form opens"""
    other_engagements: list[float]
    """Number of other engagements"""
    ad_unit_clicks: list[float]
    """Number of ad unit clicks"""
    action_clicks: list[float]
    """Number of action clicks"""
    text_url_clicks: list[float]
    """Number of text URL clicks"""
    comment_likes: list[float]
    """Number of comment likes"""
    sends: list[float]
    """Number of sends (InMail)"""
    opens: list[float]
    """Number of opens (InMail)"""
    download_clicks: list[float]
    """Number of download clicks"""
    pivot_values: list[list[Any]]
    """Pivot values (URNs) for this analytics record"""
    start_date: list[str]
    """Start date of the ad analytics data"""
    end_date: list[str]
    """End date of the ad analytics data"""


class AdCampaignAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    impressions: Any
    """Number of times the ad was shown"""
    clicks: Any
    """Number of clicks on the ad"""
    cost_in_local_currency: Any
    """Total cost in the accounts local currency"""
    cost_in_usd: Any
    """Total cost in USD"""
    likes: Any
    """Number of likes"""
    shares: Any
    """Number of shares"""
    comments: Any
    """Number of comments"""
    reactions: Any
    """Number of reactions"""
    follows: Any
    """Number of follows"""
    total_engagements: Any
    """Total number of engagements"""
    landing_page_clicks: Any
    """Number of landing page clicks"""
    company_page_clicks: Any
    """Number of company page clicks"""
    external_website_conversions: Any
    """Number of conversions on external websites"""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites"""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites"""
    conversion_value_in_local_currency: Any
    """Conversion value in local currency"""
    approximate_member_reach: Any
    """Approximate unique member reach"""
    card_clicks: Any
    """Number of carousel card clicks"""
    card_impressions: Any
    """Number of carousel card impressions"""
    video_starts: Any
    """Number of video starts"""
    video_views: Any
    """Number of video views"""
    video_first_quartile_completions: Any
    """Number of times video played to 25%"""
    video_midpoint_completions: Any
    """Number of times video played to 50%"""
    video_third_quartile_completions: Any
    """Number of times video played to 75%"""
    video_completions: Any
    """Number of times video played to 100%"""
    full_screen_plays: Any
    """Number of full screen video plays"""
    one_click_leads: Any
    """Number of one-click leads"""
    one_click_lead_form_opens: Any
    """Number of one-click lead form opens"""
    other_engagements: Any
    """Number of other engagements"""
    ad_unit_clicks: Any
    """Number of ad unit clicks"""
    action_clicks: Any
    """Number of action clicks"""
    text_url_clicks: Any
    """Number of text URL clicks"""
    comment_likes: Any
    """Number of comment likes"""
    sends: Any
    """Number of sends (InMail)"""
    opens: Any
    """Number of opens (InMail)"""
    download_clicks: Any
    """Number of download clicks"""
    pivot_values: Any
    """Pivot values (URNs) for this analytics record"""
    start_date: Any
    """Start date of the ad analytics data"""
    end_date: Any
    """End date of the ad analytics data"""


class AdCampaignAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    impressions: str
    """Number of times the ad was shown"""
    clicks: str
    """Number of clicks on the ad"""
    cost_in_local_currency: str
    """Total cost in the accounts local currency"""
    cost_in_usd: str
    """Total cost in USD"""
    likes: str
    """Number of likes"""
    shares: str
    """Number of shares"""
    comments: str
    """Number of comments"""
    reactions: str
    """Number of reactions"""
    follows: str
    """Number of follows"""
    total_engagements: str
    """Total number of engagements"""
    landing_page_clicks: str
    """Number of landing page clicks"""
    company_page_clicks: str
    """Number of company page clicks"""
    external_website_conversions: str
    """Number of conversions on external websites"""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites"""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites"""
    conversion_value_in_local_currency: str
    """Conversion value in local currency"""
    approximate_member_reach: str
    """Approximate unique member reach"""
    card_clicks: str
    """Number of carousel card clicks"""
    card_impressions: str
    """Number of carousel card impressions"""
    video_starts: str
    """Number of video starts"""
    video_views: str
    """Number of video views"""
    video_first_quartile_completions: str
    """Number of times video played to 25%"""
    video_midpoint_completions: str
    """Number of times video played to 50%"""
    video_third_quartile_completions: str
    """Number of times video played to 75%"""
    video_completions: str
    """Number of times video played to 100%"""
    full_screen_plays: str
    """Number of full screen video plays"""
    one_click_leads: str
    """Number of one-click leads"""
    one_click_lead_form_opens: str
    """Number of one-click lead form opens"""
    other_engagements: str
    """Number of other engagements"""
    ad_unit_clicks: str
    """Number of ad unit clicks"""
    action_clicks: str
    """Number of action clicks"""
    text_url_clicks: str
    """Number of text URL clicks"""
    comment_likes: str
    """Number of comment likes"""
    sends: str
    """Number of sends (InMail)"""
    opens: str
    """Number of opens (InMail)"""
    download_clicks: str
    """Number of download clicks"""
    pivot_values: str
    """Pivot values (URNs) for this analytics record"""
    start_date: str
    """Start date of the ad analytics data"""
    end_date: str
    """End date of the ad analytics data"""


class AdCampaignAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_campaign_analytics search results."""
    impressions: AirbyteSortOrder
    """Number of times the ad was shown"""
    clicks: AirbyteSortOrder
    """Number of clicks on the ad"""
    cost_in_local_currency: AirbyteSortOrder
    """Total cost in the accounts local currency"""
    cost_in_usd: AirbyteSortOrder
    """Total cost in USD"""
    likes: AirbyteSortOrder
    """Number of likes"""
    shares: AirbyteSortOrder
    """Number of shares"""
    comments: AirbyteSortOrder
    """Number of comments"""
    reactions: AirbyteSortOrder
    """Number of reactions"""
    follows: AirbyteSortOrder
    """Number of follows"""
    total_engagements: AirbyteSortOrder
    """Total number of engagements"""
    landing_page_clicks: AirbyteSortOrder
    """Number of landing page clicks"""
    company_page_clicks: AirbyteSortOrder
    """Number of company page clicks"""
    external_website_conversions: AirbyteSortOrder
    """Number of conversions on external websites"""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites"""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites"""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in local currency"""
    approximate_member_reach: AirbyteSortOrder
    """Approximate unique member reach"""
    card_clicks: AirbyteSortOrder
    """Number of carousel card clicks"""
    card_impressions: AirbyteSortOrder
    """Number of carousel card impressions"""
    video_starts: AirbyteSortOrder
    """Number of video starts"""
    video_views: AirbyteSortOrder
    """Number of video views"""
    video_first_quartile_completions: AirbyteSortOrder
    """Number of times video played to 25%"""
    video_midpoint_completions: AirbyteSortOrder
    """Number of times video played to 50%"""
    video_third_quartile_completions: AirbyteSortOrder
    """Number of times video played to 75%"""
    video_completions: AirbyteSortOrder
    """Number of times video played to 100%"""
    full_screen_plays: AirbyteSortOrder
    """Number of full screen video plays"""
    one_click_leads: AirbyteSortOrder
    """Number of one-click leads"""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of one-click lead form opens"""
    other_engagements: AirbyteSortOrder
    """Number of other engagements"""
    ad_unit_clicks: AirbyteSortOrder
    """Number of ad unit clicks"""
    action_clicks: AirbyteSortOrder
    """Number of action clicks"""
    text_url_clicks: AirbyteSortOrder
    """Number of text URL clicks"""
    comment_likes: AirbyteSortOrder
    """Number of comment likes"""
    sends: AirbyteSortOrder
    """Number of sends (InMail)"""
    opens: AirbyteSortOrder
    """Number of opens (InMail)"""
    download_clicks: AirbyteSortOrder
    """Number of download clicks"""
    pivot_values: AirbyteSortOrder
    """Pivot values (URNs) for this analytics record"""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data"""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data"""


# Entity-specific condition types for ad_campaign_analytics
class AdCampaignAnalyticsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdCampaignAnalyticsSearchFilter


class AdCampaignAnalyticsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdCampaignAnalyticsSearchFilter


class AdCampaignAnalyticsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdCampaignAnalyticsSearchFilter


class AdCampaignAnalyticsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdCampaignAnalyticsSearchFilter


class AdCampaignAnalyticsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdCampaignAnalyticsSearchFilter


class AdCampaignAnalyticsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdCampaignAnalyticsSearchFilter


class AdCampaignAnalyticsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdCampaignAnalyticsStringFilter


class AdCampaignAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdCampaignAnalyticsStringFilter


class AdCampaignAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdCampaignAnalyticsStringFilter


class AdCampaignAnalyticsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdCampaignAnalyticsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdCampaignAnalyticsInCondition = TypedDict("AdCampaignAnalyticsInCondition", {"in": AdCampaignAnalyticsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdCampaignAnalyticsNotCondition = TypedDict("AdCampaignAnalyticsNotCondition", {"not": "AdCampaignAnalyticsCondition"}, total=False)
"""Negates the nested condition."""

AdCampaignAnalyticsAndCondition = TypedDict("AdCampaignAnalyticsAndCondition", {"and": "list[AdCampaignAnalyticsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdCampaignAnalyticsOrCondition = TypedDict("AdCampaignAnalyticsOrCondition", {"or": "list[AdCampaignAnalyticsCondition]"}, total=False)
"""True if any nested condition is true."""

AdCampaignAnalyticsAnyCondition = TypedDict("AdCampaignAnalyticsAnyCondition", {"any": AdCampaignAnalyticsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_campaign_analytics condition types
AdCampaignAnalyticsCondition = (
    AdCampaignAnalyticsEqCondition
    | AdCampaignAnalyticsNeqCondition
    | AdCampaignAnalyticsGtCondition
    | AdCampaignAnalyticsGteCondition
    | AdCampaignAnalyticsLtCondition
    | AdCampaignAnalyticsLteCondition
    | AdCampaignAnalyticsInCondition
    | AdCampaignAnalyticsLikeCondition
    | AdCampaignAnalyticsFuzzyCondition
    | AdCampaignAnalyticsKeywordCondition
    | AdCampaignAnalyticsContainsCondition
    | AdCampaignAnalyticsNotCondition
    | AdCampaignAnalyticsAndCondition
    | AdCampaignAnalyticsOrCondition
    | AdCampaignAnalyticsAnyCondition
)


class AdCampaignAnalyticsSearchQuery(TypedDict, total=False):
    """Search query for ad_campaign_analytics entity."""
    filter: AdCampaignAnalyticsCondition
    sort: list[AdCampaignAnalyticsSortFilter]


# ===== AD_CREATIVE_ANALYTICS SEARCH TYPES =====

class AdCreativeAnalyticsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_creative_analytics search queries."""
    impressions: float | None
    """Number of times the ad was shown"""
    clicks: float | None
    """Number of clicks on the ad"""
    cost_in_local_currency: float | None
    """Total cost in the accounts local currency"""
    cost_in_usd: float | None
    """Total cost in USD"""
    likes: float | None
    """Number of likes"""
    shares: float | None
    """Number of shares"""
    comments: float | None
    """Number of comments"""
    reactions: float | None
    """Number of reactions"""
    follows: float | None
    """Number of follows"""
    total_engagements: float | None
    """Total number of engagements"""
    landing_page_clicks: float | None
    """Number of landing page clicks"""
    company_page_clicks: float | None
    """Number of company page clicks"""
    external_website_conversions: float | None
    """Number of conversions on external websites"""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites"""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites"""
    conversion_value_in_local_currency: float | None
    """Conversion value in local currency"""
    approximate_member_reach: float | None
    """Approximate unique member reach"""
    card_clicks: float | None
    """Number of carousel card clicks"""
    card_impressions: float | None
    """Number of carousel card impressions"""
    video_starts: float | None
    """Number of video starts"""
    video_views: float | None
    """Number of video views"""
    video_first_quartile_completions: float | None
    """Number of times video played to 25%"""
    video_midpoint_completions: float | None
    """Number of times video played to 50%"""
    video_third_quartile_completions: float | None
    """Number of times video played to 75%"""
    video_completions: float | None
    """Number of times video played to 100%"""
    full_screen_plays: float | None
    """Number of full screen video plays"""
    one_click_leads: float | None
    """Number of one-click leads"""
    one_click_lead_form_opens: float | None
    """Number of one-click lead form opens"""
    other_engagements: float | None
    """Number of other engagements"""
    ad_unit_clicks: float | None
    """Number of ad unit clicks"""
    action_clicks: float | None
    """Number of action clicks"""
    text_url_clicks: float | None
    """Number of text URL clicks"""
    comment_likes: float | None
    """Number of comment likes"""
    sends: float | None
    """Number of sends (InMail)"""
    opens: float | None
    """Number of opens (InMail)"""
    download_clicks: float | None
    """Number of download clicks"""
    pivot_values: list[Any] | None
    """Pivot values (URNs) for this analytics record"""
    start_date: str | None
    """Start date of the ad analytics data"""
    end_date: str | None
    """End date of the ad analytics data"""


class AdCreativeAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    impressions: list[float]
    """Number of times the ad was shown"""
    clicks: list[float]
    """Number of clicks on the ad"""
    cost_in_local_currency: list[float]
    """Total cost in the accounts local currency"""
    cost_in_usd: list[float]
    """Total cost in USD"""
    likes: list[float]
    """Number of likes"""
    shares: list[float]
    """Number of shares"""
    comments: list[float]
    """Number of comments"""
    reactions: list[float]
    """Number of reactions"""
    follows: list[float]
    """Number of follows"""
    total_engagements: list[float]
    """Total number of engagements"""
    landing_page_clicks: list[float]
    """Number of landing page clicks"""
    company_page_clicks: list[float]
    """Number of company page clicks"""
    external_website_conversions: list[float]
    """Number of conversions on external websites"""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites"""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites"""
    conversion_value_in_local_currency: list[float]
    """Conversion value in local currency"""
    approximate_member_reach: list[float]
    """Approximate unique member reach"""
    card_clicks: list[float]
    """Number of carousel card clicks"""
    card_impressions: list[float]
    """Number of carousel card impressions"""
    video_starts: list[float]
    """Number of video starts"""
    video_views: list[float]
    """Number of video views"""
    video_first_quartile_completions: list[float]
    """Number of times video played to 25%"""
    video_midpoint_completions: list[float]
    """Number of times video played to 50%"""
    video_third_quartile_completions: list[float]
    """Number of times video played to 75%"""
    video_completions: list[float]
    """Number of times video played to 100%"""
    full_screen_plays: list[float]
    """Number of full screen video plays"""
    one_click_leads: list[float]
    """Number of one-click leads"""
    one_click_lead_form_opens: list[float]
    """Number of one-click lead form opens"""
    other_engagements: list[float]
    """Number of other engagements"""
    ad_unit_clicks: list[float]
    """Number of ad unit clicks"""
    action_clicks: list[float]
    """Number of action clicks"""
    text_url_clicks: list[float]
    """Number of text URL clicks"""
    comment_likes: list[float]
    """Number of comment likes"""
    sends: list[float]
    """Number of sends (InMail)"""
    opens: list[float]
    """Number of opens (InMail)"""
    download_clicks: list[float]
    """Number of download clicks"""
    pivot_values: list[list[Any]]
    """Pivot values (URNs) for this analytics record"""
    start_date: list[str]
    """Start date of the ad analytics data"""
    end_date: list[str]
    """End date of the ad analytics data"""


class AdCreativeAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    impressions: Any
    """Number of times the ad was shown"""
    clicks: Any
    """Number of clicks on the ad"""
    cost_in_local_currency: Any
    """Total cost in the accounts local currency"""
    cost_in_usd: Any
    """Total cost in USD"""
    likes: Any
    """Number of likes"""
    shares: Any
    """Number of shares"""
    comments: Any
    """Number of comments"""
    reactions: Any
    """Number of reactions"""
    follows: Any
    """Number of follows"""
    total_engagements: Any
    """Total number of engagements"""
    landing_page_clicks: Any
    """Number of landing page clicks"""
    company_page_clicks: Any
    """Number of company page clicks"""
    external_website_conversions: Any
    """Number of conversions on external websites"""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites"""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites"""
    conversion_value_in_local_currency: Any
    """Conversion value in local currency"""
    approximate_member_reach: Any
    """Approximate unique member reach"""
    card_clicks: Any
    """Number of carousel card clicks"""
    card_impressions: Any
    """Number of carousel card impressions"""
    video_starts: Any
    """Number of video starts"""
    video_views: Any
    """Number of video views"""
    video_first_quartile_completions: Any
    """Number of times video played to 25%"""
    video_midpoint_completions: Any
    """Number of times video played to 50%"""
    video_third_quartile_completions: Any
    """Number of times video played to 75%"""
    video_completions: Any
    """Number of times video played to 100%"""
    full_screen_plays: Any
    """Number of full screen video plays"""
    one_click_leads: Any
    """Number of one-click leads"""
    one_click_lead_form_opens: Any
    """Number of one-click lead form opens"""
    other_engagements: Any
    """Number of other engagements"""
    ad_unit_clicks: Any
    """Number of ad unit clicks"""
    action_clicks: Any
    """Number of action clicks"""
    text_url_clicks: Any
    """Number of text URL clicks"""
    comment_likes: Any
    """Number of comment likes"""
    sends: Any
    """Number of sends (InMail)"""
    opens: Any
    """Number of opens (InMail)"""
    download_clicks: Any
    """Number of download clicks"""
    pivot_values: Any
    """Pivot values (URNs) for this analytics record"""
    start_date: Any
    """Start date of the ad analytics data"""
    end_date: Any
    """End date of the ad analytics data"""


class AdCreativeAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    impressions: str
    """Number of times the ad was shown"""
    clicks: str
    """Number of clicks on the ad"""
    cost_in_local_currency: str
    """Total cost in the accounts local currency"""
    cost_in_usd: str
    """Total cost in USD"""
    likes: str
    """Number of likes"""
    shares: str
    """Number of shares"""
    comments: str
    """Number of comments"""
    reactions: str
    """Number of reactions"""
    follows: str
    """Number of follows"""
    total_engagements: str
    """Total number of engagements"""
    landing_page_clicks: str
    """Number of landing page clicks"""
    company_page_clicks: str
    """Number of company page clicks"""
    external_website_conversions: str
    """Number of conversions on external websites"""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites"""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites"""
    conversion_value_in_local_currency: str
    """Conversion value in local currency"""
    approximate_member_reach: str
    """Approximate unique member reach"""
    card_clicks: str
    """Number of carousel card clicks"""
    card_impressions: str
    """Number of carousel card impressions"""
    video_starts: str
    """Number of video starts"""
    video_views: str
    """Number of video views"""
    video_first_quartile_completions: str
    """Number of times video played to 25%"""
    video_midpoint_completions: str
    """Number of times video played to 50%"""
    video_third_quartile_completions: str
    """Number of times video played to 75%"""
    video_completions: str
    """Number of times video played to 100%"""
    full_screen_plays: str
    """Number of full screen video plays"""
    one_click_leads: str
    """Number of one-click leads"""
    one_click_lead_form_opens: str
    """Number of one-click lead form opens"""
    other_engagements: str
    """Number of other engagements"""
    ad_unit_clicks: str
    """Number of ad unit clicks"""
    action_clicks: str
    """Number of action clicks"""
    text_url_clicks: str
    """Number of text URL clicks"""
    comment_likes: str
    """Number of comment likes"""
    sends: str
    """Number of sends (InMail)"""
    opens: str
    """Number of opens (InMail)"""
    download_clicks: str
    """Number of download clicks"""
    pivot_values: str
    """Pivot values (URNs) for this analytics record"""
    start_date: str
    """Start date of the ad analytics data"""
    end_date: str
    """End date of the ad analytics data"""


class AdCreativeAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_creative_analytics search results."""
    impressions: AirbyteSortOrder
    """Number of times the ad was shown"""
    clicks: AirbyteSortOrder
    """Number of clicks on the ad"""
    cost_in_local_currency: AirbyteSortOrder
    """Total cost in the accounts local currency"""
    cost_in_usd: AirbyteSortOrder
    """Total cost in USD"""
    likes: AirbyteSortOrder
    """Number of likes"""
    shares: AirbyteSortOrder
    """Number of shares"""
    comments: AirbyteSortOrder
    """Number of comments"""
    reactions: AirbyteSortOrder
    """Number of reactions"""
    follows: AirbyteSortOrder
    """Number of follows"""
    total_engagements: AirbyteSortOrder
    """Total number of engagements"""
    landing_page_clicks: AirbyteSortOrder
    """Number of landing page clicks"""
    company_page_clicks: AirbyteSortOrder
    """Number of company page clicks"""
    external_website_conversions: AirbyteSortOrder
    """Number of conversions on external websites"""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites"""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites"""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in local currency"""
    approximate_member_reach: AirbyteSortOrder
    """Approximate unique member reach"""
    card_clicks: AirbyteSortOrder
    """Number of carousel card clicks"""
    card_impressions: AirbyteSortOrder
    """Number of carousel card impressions"""
    video_starts: AirbyteSortOrder
    """Number of video starts"""
    video_views: AirbyteSortOrder
    """Number of video views"""
    video_first_quartile_completions: AirbyteSortOrder
    """Number of times video played to 25%"""
    video_midpoint_completions: AirbyteSortOrder
    """Number of times video played to 50%"""
    video_third_quartile_completions: AirbyteSortOrder
    """Number of times video played to 75%"""
    video_completions: AirbyteSortOrder
    """Number of times video played to 100%"""
    full_screen_plays: AirbyteSortOrder
    """Number of full screen video plays"""
    one_click_leads: AirbyteSortOrder
    """Number of one-click leads"""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of one-click lead form opens"""
    other_engagements: AirbyteSortOrder
    """Number of other engagements"""
    ad_unit_clicks: AirbyteSortOrder
    """Number of ad unit clicks"""
    action_clicks: AirbyteSortOrder
    """Number of action clicks"""
    text_url_clicks: AirbyteSortOrder
    """Number of text URL clicks"""
    comment_likes: AirbyteSortOrder
    """Number of comment likes"""
    sends: AirbyteSortOrder
    """Number of sends (InMail)"""
    opens: AirbyteSortOrder
    """Number of opens (InMail)"""
    download_clicks: AirbyteSortOrder
    """Number of download clicks"""
    pivot_values: AirbyteSortOrder
    """Pivot values (URNs) for this analytics record"""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data"""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data"""


# Entity-specific condition types for ad_creative_analytics
class AdCreativeAnalyticsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdCreativeAnalyticsSearchFilter


class AdCreativeAnalyticsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdCreativeAnalyticsSearchFilter


class AdCreativeAnalyticsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdCreativeAnalyticsSearchFilter


class AdCreativeAnalyticsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdCreativeAnalyticsSearchFilter


class AdCreativeAnalyticsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdCreativeAnalyticsSearchFilter


class AdCreativeAnalyticsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdCreativeAnalyticsSearchFilter


class AdCreativeAnalyticsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdCreativeAnalyticsStringFilter


class AdCreativeAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdCreativeAnalyticsStringFilter


class AdCreativeAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdCreativeAnalyticsStringFilter


class AdCreativeAnalyticsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdCreativeAnalyticsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdCreativeAnalyticsInCondition = TypedDict("AdCreativeAnalyticsInCondition", {"in": AdCreativeAnalyticsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdCreativeAnalyticsNotCondition = TypedDict("AdCreativeAnalyticsNotCondition", {"not": "AdCreativeAnalyticsCondition"}, total=False)
"""Negates the nested condition."""

AdCreativeAnalyticsAndCondition = TypedDict("AdCreativeAnalyticsAndCondition", {"and": "list[AdCreativeAnalyticsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdCreativeAnalyticsOrCondition = TypedDict("AdCreativeAnalyticsOrCondition", {"or": "list[AdCreativeAnalyticsCondition]"}, total=False)
"""True if any nested condition is true."""

AdCreativeAnalyticsAnyCondition = TypedDict("AdCreativeAnalyticsAnyCondition", {"any": AdCreativeAnalyticsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_creative_analytics condition types
AdCreativeAnalyticsCondition = (
    AdCreativeAnalyticsEqCondition
    | AdCreativeAnalyticsNeqCondition
    | AdCreativeAnalyticsGtCondition
    | AdCreativeAnalyticsGteCondition
    | AdCreativeAnalyticsLtCondition
    | AdCreativeAnalyticsLteCondition
    | AdCreativeAnalyticsInCondition
    | AdCreativeAnalyticsLikeCondition
    | AdCreativeAnalyticsFuzzyCondition
    | AdCreativeAnalyticsKeywordCondition
    | AdCreativeAnalyticsContainsCondition
    | AdCreativeAnalyticsNotCondition
    | AdCreativeAnalyticsAndCondition
    | AdCreativeAnalyticsOrCondition
    | AdCreativeAnalyticsAnyCondition
)


class AdCreativeAnalyticsSearchQuery(TypedDict, total=False):
    """Search query for ad_creative_analytics entity."""
    filter: AdCreativeAnalyticsCondition
    sort: list[AdCreativeAnalyticsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
