"""
Type definitions for linkedin-ads connector.
"""
from __future__ import annotations

from airbyte_agent_sdk.types import AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

class AccountsUpdateParamsPatch(TypedDict):
    """Nested schema for AccountsUpdateParams.patch"""
    set_: dict[str, Any]

class AccountUsersUpdateParamsPatch(TypedDict):
    """Nested schema for AccountUsersUpdateParams.patch"""
    set_: dict[str, Any]

class CampaignsCreateParamsDailybudget(TypedDict):
    """Daily budget"""
    amount: NotRequired[str]
    currency_code: NotRequired[str]

class CampaignsCreateParamsUnitcost(TypedDict):
    """Bid amount per unit (per click, per impression, etc.)"""
    amount: NotRequired[str]
    currency_code: NotRequired[str]

class CampaignsCreateParamsLocale(TypedDict):
    """Campaign locale"""
    country: NotRequired[str]
    language: NotRequired[str]

class CampaignsCreateParamsRunschedule(TypedDict):
    """Scheduled run window (epoch milliseconds)"""
    start: NotRequired[int]
    end: NotRequired[int]

class CampaignsUpdateParamsPatch(TypedDict):
    """Nested schema for CampaignsUpdateParams.patch"""
    set_: dict[str, Any]

class CampaignGroupsCreateParamsRunschedule(TypedDict):
    """Scheduled run window (epoch milliseconds)"""
    start: NotRequired[int]
    end: NotRequired[int]

class CampaignGroupsCreateParamsTotalbudget(TypedDict):
    """Total budget across the group's lifetime"""
    amount: NotRequired[str]
    currency_code: NotRequired[str]

class CampaignGroupsUpdateParamsPatch(TypedDict):
    """Nested schema for CampaignGroupsUpdateParams.patch"""
    set_: dict[str, Any]

class CreativesUpdateParamsPatch(TypedDict):
    """Nested schema for CreativesUpdateParams.patch"""
    set_: dict[str, Any]

class ConversionsCreateParamsValue(TypedDict):
    """Monetary value assigned to each conversion"""
    amount: NotRequired[str]
    currency_code: NotRequired[str]

class ConversionsUpdateParamsPatch(TypedDict):
    """Nested schema for ConversionsUpdateParams.patch"""
    set_: dict[str, Any]

class ConversionEventsCreateParamsElementsItemUserUseridsItem(TypedDict):
    """Nested schema for ConversionEventsCreateParamsElementsItemUser.userIds_item"""
    id_type: NotRequired[str]
    id_value: NotRequired[str]

class ConversionEventsCreateParamsElementsItemUser(TypedDict):
    """Identifies the converting user (hashed email or other supported ID types)"""
    user_ids: NotRequired[list[ConversionEventsCreateParamsElementsItemUserUseridsItem]]
    user_info: NotRequired[dict[str, Any]]

class ConversionEventsCreateParamsElementsItemConversionvalue(TypedDict):
    """Monetary value of this conversion"""
    amount: NotRequired[str]
    currency_code: NotRequired[str]

class ConversionEventsCreateParamsElementsItem(TypedDict):
    """Nested schema for ConversionEventsCreateParams.elements_item"""
    conversion: str
    conversion_happened_at: int
    user: NotRequired[ConversionEventsCreateParamsElementsItemUser]
    conversion_value: NotRequired[ConversionEventsCreateParamsElementsItemConversionvalue]
    event_id: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class AccountsListParams(TypedDict):
    """Parameters for accounts.list operation"""
    q: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class AccountsCreateParams(TypedDict):
    """Parameters for accounts.create operation"""
    name: str
    type: str
    currency: NotRequired[str]
    reference: NotRequired[str]
    test: NotRequired[bool]

class AccountsGetParams(TypedDict):
    """Parameters for accounts.get operation"""
    id: str

class AccountsUpdateParams(TypedDict):
    """Parameters for accounts.update operation"""
    patch: AccountsUpdateParamsPatch
    id: str

class AccountsDeleteParams(TypedDict):
    """Parameters for accounts.delete operation"""
    id: str

class AccountUsersListParams(TypedDict):
    """Parameters for account_users.list operation"""
    q: str
    accounts: str
    count: NotRequired[int]
    start: NotRequired[int]

class AccountUsersUpdateParams(TypedDict):
    """Parameters for account_users.update operation"""
    patch: AccountUsersUpdateParamsPatch
    account: str
    user: str

class AccountUsersCreateParams(TypedDict):
    """Parameters for account_users.create operation"""
    role: str
    account: str
    user: str

class AccountUsersDeleteParams(TypedDict):
    """Parameters for account_users.delete operation"""
    account: str
    user: str

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    account_id: str
    q: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class CampaignsCreateParams(TypedDict):
    """Parameters for campaigns.create operation"""
    account: str
    name: str
    political_intent: str
    campaign_group: NotRequired[str]
    type: NotRequired[str]
    objective_type: NotRequired[str]
    status: NotRequired[str]
    cost_type: NotRequired[str]
    daily_budget: NotRequired[CampaignsCreateParamsDailybudget]
    unit_cost: NotRequired[CampaignsCreateParamsUnitcost]
    locale: NotRequired[CampaignsCreateParamsLocale]
    run_schedule: CampaignsCreateParamsRunschedule
    targeting_criteria: NotRequired[dict[str, Any]]
    audience_expansion_enabled: NotRequired[bool]
    offsite_delivery_enabled: bool
    creative_selection: NotRequired[str]
    account_id: str

class CampaignsGetParams(TypedDict):
    """Parameters for campaigns.get operation"""
    account_id: str
    id: str

class CampaignsUpdateParams(TypedDict):
    """Parameters for campaigns.update operation"""
    patch: CampaignsUpdateParamsPatch
    account_id: str
    id: str

class CampaignsDeleteParams(TypedDict):
    """Parameters for campaigns.delete operation"""
    account_id: str
    id: str

class CampaignGroupsListParams(TypedDict):
    """Parameters for campaign_groups.list operation"""
    account_id: str
    q: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class CampaignGroupsCreateParams(TypedDict):
    """Parameters for campaign_groups.create operation"""
    account: str
    name: str
    status: NotRequired[str]
    run_schedule: CampaignGroupsCreateParamsRunschedule
    total_budget: NotRequired[CampaignGroupsCreateParamsTotalbudget]
    objective_type: NotRequired[str]
    account_id: str

class CampaignGroupsGetParams(TypedDict):
    """Parameters for campaign_groups.get operation"""
    account_id: str
    id: str

class CampaignGroupsUpdateParams(TypedDict):
    """Parameters for campaign_groups.update operation"""
    patch: CampaignGroupsUpdateParamsPatch
    account_id: str
    id: str

class CampaignGroupsDeleteParams(TypedDict):
    """Parameters for campaign_groups.delete operation"""
    account_id: str
    id: str

class CreativesListParams(TypedDict):
    """Parameters for creatives.list operation"""
    account_id: str
    q: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class CreativesCreateParams(TypedDict):
    """Parameters for creatives.create operation"""
    campaign: str
    content: NotRequired[dict[str, Any]]
    intended_status: NotRequired[str]
    name: NotRequired[str]
    account_id: str

class CreativesGetParams(TypedDict):
    """Parameters for creatives.get operation"""
    account_id: str
    id: str

class CreativesUpdateParams(TypedDict):
    """Parameters for creatives.update operation"""
    patch: CreativesUpdateParamsPatch
    account_id: str
    id: str

class CreativesDeleteParams(TypedDict):
    """Parameters for creatives.delete operation"""
    account_id: str
    id: str

class ConversionsListParams(TypedDict):
    """Parameters for conversions.list operation"""
    q: str
    account: str
    count: NotRequired[int]
    start: NotRequired[int]

class ConversionsCreateParams(TypedDict):
    """Parameters for conversions.create operation"""
    account: str
    name: str
    type: str
    attribution_type: NotRequired[str]
    post_click_attribution_window_size: NotRequired[int]
    view_through_attribution_window_size: NotRequired[int]
    enabled: NotRequired[bool]
    url_match_rule_expression: NotRequired[list[list[dict[str, Any]]]]
    value: NotRequired[ConversionsCreateParamsValue]
    auto_association_type: NotRequired[str]

class ConversionsGetParams(TypedDict):
    """Parameters for conversions.get operation"""
    id: str

class ConversionsUpdateParams(TypedDict):
    """Parameters for conversions.update operation"""
    patch: ConversionsUpdateParamsPatch
    id: str
    account: str

class ConversionEventsCreateParams(TypedDict):
    """Parameters for conversion_events.create operation"""
    elements: list[ConversionEventsCreateParamsElementsItem]

class CampaignConversionsCreateParams(TypedDict):
    """Parameters for campaign_conversions.create operation"""
    campaign: NotRequired[str]
    conversion: NotRequired[str]
    campaign_urn: str
    conversion_urn: str

class CampaignConversionsDeleteParams(TypedDict):
    """Parameters for campaign_conversions.delete operation"""
    campaign_urn: str
    conversion_urn: str

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

class AdImpressionDeviceAnalyticsListParams(TypedDict):
    """Parameters for ad_impression_device_analytics.list operation"""
    q: str
    pivot: str
    time_granularity: str
    date_range: str
    campaigns: str
    fields: NotRequired[str]

class AdMemberCompanyAnalyticsListParams(TypedDict):
    """Parameters for ad_member_company_analytics.list operation"""
    q: str
    pivot: str
    time_granularity: str
    date_range: str
    campaigns: str
    fields: NotRequired[str]

class AdMemberCompanySizeAnalyticsListParams(TypedDict):
    """Parameters for ad_member_company_size_analytics.list operation"""
    q: str
    pivot: str
    time_granularity: str
    date_range: str
    campaigns: str
    fields: NotRequired[str]

class AdMemberCountryAnalyticsListParams(TypedDict):
    """Parameters for ad_member_country_analytics.list operation"""
    q: str
    pivot: str
    time_granularity: str
    date_range: str
    campaigns: str
    fields: NotRequired[str]

class AdMemberIndustryAnalyticsListParams(TypedDict):
    """Parameters for ad_member_industry_analytics.list operation"""
    q: str
    pivot: str
    time_granularity: str
    date_range: str
    campaigns: str
    fields: NotRequired[str]

class AdMemberJobFunctionAnalyticsListParams(TypedDict):
    """Parameters for ad_member_job_function_analytics.list operation"""
    q: str
    pivot: str
    time_granularity: str
    date_range: str
    campaigns: str
    fields: NotRequired[str]

class AdMemberJobTitleAnalyticsListParams(TypedDict):
    """Parameters for ad_member_job_title_analytics.list operation"""
    q: str
    pivot: str
    time_granularity: str
    date_range: str
    campaigns: str
    fields: NotRequired[str]

class AdMemberRegionAnalyticsListParams(TypedDict):
    """Parameters for ad_member_region_analytics.list operation"""
    q: str
    pivot: str
    time_granularity: str
    date_range: str
    campaigns: str
    fields: NotRequired[str]

class AdMemberSeniorityAnalyticsListParams(TypedDict):
    """Parameters for ad_member_seniority_analytics.list operation"""
    q: str
    pivot: str
    time_granularity: str
    date_range: str
    campaigns: str
    fields: NotRequired[str]

class LeadFormsListParams(TypedDict):
    """Parameters for lead_forms.list operation"""
    q: str
    owner: str
    count: NotRequired[int]
    start: NotRequired[int]

class LeadFormResponsesListParams(TypedDict):
    """Parameters for lead_form_responses.list operation"""
    q: str
    owner: str
    lead_type: str
    count: NotRequired[int]
    start: NotRequired[int]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ACCOUNTS SEARCH TYPES =====

class AccountsSearchFilter(TypedDict, total=False):
    """Available fields for filtering accounts search queries."""
    test: bool | None
    """Flag indicating if the account is in a test mode."""
    notified_on_creative_rejection: bool | None
    """Flag for notifications on creative rejection."""
    notified_on_new_features_enabled: bool | None
    """Flag for notifications on new features being enabled."""
    notified_on_end_of_campaign: bool | None
    """Flag for notifications on the end of campaign."""
    serving_statuses: list[Any] | None
    """The serving statuses associated with the account."""
    notified_on_campaign_optimization: bool | None
    """Flag for notifications on campaign optimization."""
    type_: str | None
    """The type or category of the account."""
    version: dict[str, Any] | None
    """The version information related to the account."""
    reference: str | None
    """A reference identifier for the account."""
    notified_on_creative_approval: bool | None
    """Flag for notifications on creative approval."""
    created: str | None
    """The timestamp indicating when the account was created."""
    last_modified: str | None
    """The timestamp of the last modification made to the account."""
    name: str | None
    """The name of the account."""
    currency: str | None
    """The currency used for financial transactions in the account."""
    id: int | None
    """The unique identifier for the account."""
    status: str | None
    """The status of the account."""


class AccountsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    test: list[bool]
    """Flag indicating if the account is in a test mode."""
    notified_on_creative_rejection: list[bool]
    """Flag for notifications on creative rejection."""
    notified_on_new_features_enabled: list[bool]
    """Flag for notifications on new features being enabled."""
    notified_on_end_of_campaign: list[bool]
    """Flag for notifications on the end of campaign."""
    serving_statuses: list[list[Any]]
    """The serving statuses associated with the account."""
    notified_on_campaign_optimization: list[bool]
    """Flag for notifications on campaign optimization."""
    type_: list[str]
    """The type or category of the account."""
    version: list[dict[str, Any]]
    """The version information related to the account."""
    reference: list[str]
    """A reference identifier for the account."""
    notified_on_creative_approval: list[bool]
    """Flag for notifications on creative approval."""
    created: list[str]
    """The timestamp indicating when the account was created."""
    last_modified: list[str]
    """The timestamp of the last modification made to the account."""
    name: list[str]
    """The name of the account."""
    currency: list[str]
    """The currency used for financial transactions in the account."""
    id: list[int]
    """The unique identifier for the account."""
    status: list[str]
    """The status of the account."""


class AccountsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    test: Any
    """Flag indicating if the account is in a test mode."""
    notified_on_creative_rejection: Any
    """Flag for notifications on creative rejection."""
    notified_on_new_features_enabled: Any
    """Flag for notifications on new features being enabled."""
    notified_on_end_of_campaign: Any
    """Flag for notifications on the end of campaign."""
    serving_statuses: Any
    """The serving statuses associated with the account."""
    notified_on_campaign_optimization: Any
    """Flag for notifications on campaign optimization."""
    type_: Any
    """The type or category of the account."""
    version: Any
    """The version information related to the account."""
    reference: Any
    """A reference identifier for the account."""
    notified_on_creative_approval: Any
    """Flag for notifications on creative approval."""
    created: Any
    """The timestamp indicating when the account was created."""
    last_modified: Any
    """The timestamp of the last modification made to the account."""
    name: Any
    """The name of the account."""
    currency: Any
    """The currency used for financial transactions in the account."""
    id: Any
    """The unique identifier for the account."""
    status: Any
    """The status of the account."""


class AccountsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    test: str
    """Flag indicating if the account is in a test mode."""
    notified_on_creative_rejection: str
    """Flag for notifications on creative rejection."""
    notified_on_new_features_enabled: str
    """Flag for notifications on new features being enabled."""
    notified_on_end_of_campaign: str
    """Flag for notifications on the end of campaign."""
    serving_statuses: str
    """The serving statuses associated with the account."""
    notified_on_campaign_optimization: str
    """Flag for notifications on campaign optimization."""
    type_: str
    """The type or category of the account."""
    version: str
    """The version information related to the account."""
    reference: str
    """A reference identifier for the account."""
    notified_on_creative_approval: str
    """Flag for notifications on creative approval."""
    created: str
    """The timestamp indicating when the account was created."""
    last_modified: str
    """The timestamp of the last modification made to the account."""
    name: str
    """The name of the account."""
    currency: str
    """The currency used for financial transactions in the account."""
    id: str
    """The unique identifier for the account."""
    status: str
    """The status of the account."""


class AccountsSortFilter(TypedDict, total=False):
    """Available fields for sorting accounts search results."""
    test: AirbyteSortOrder
    """Flag indicating if the account is in a test mode."""
    notified_on_creative_rejection: AirbyteSortOrder
    """Flag for notifications on creative rejection."""
    notified_on_new_features_enabled: AirbyteSortOrder
    """Flag for notifications on new features being enabled."""
    notified_on_end_of_campaign: AirbyteSortOrder
    """Flag for notifications on the end of campaign."""
    serving_statuses: AirbyteSortOrder
    """The serving statuses associated with the account."""
    notified_on_campaign_optimization: AirbyteSortOrder
    """Flag for notifications on campaign optimization."""
    type_: AirbyteSortOrder
    """The type or category of the account."""
    version: AirbyteSortOrder
    """The version information related to the account."""
    reference: AirbyteSortOrder
    """A reference identifier for the account."""
    notified_on_creative_approval: AirbyteSortOrder
    """Flag for notifications on creative approval."""
    created: AirbyteSortOrder
    """The timestamp indicating when the account was created."""
    last_modified: AirbyteSortOrder
    """The timestamp of the last modification made to the account."""
    name: AirbyteSortOrder
    """The name of the account."""
    currency: AirbyteSortOrder
    """The currency used for financial transactions in the account."""
    id: AirbyteSortOrder
    """The unique identifier for the account."""
    status: AirbyteSortOrder
    """The status of the account."""


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


class AccountsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AccountsStringFilter


class AccountsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AccountsStringFilter


class AccountsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AccountsStringFilter


class AccountsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AccountsStringFilter


class AccountsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | AccountsStartswithCondition
    | AccountsEndswithCondition
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
    """The account associated with the user"""
    created: str | None
    """The date and time when the user account was created"""
    last_modified: str | None
    """The date and time when the user account was last modified"""
    role: str | None
    """The role assigned to the user in the account"""
    user: str | None
    """The user details including name, email, etc."""


class AccountUsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account: list[str]
    """The account associated with the user"""
    created: list[str]
    """The date and time when the user account was created"""
    last_modified: list[str]
    """The date and time when the user account was last modified"""
    role: list[str]
    """The role assigned to the user in the account"""
    user: list[str]
    """The user details including name, email, etc."""


class AccountUsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account: Any
    """The account associated with the user"""
    created: Any
    """The date and time when the user account was created"""
    last_modified: Any
    """The date and time when the user account was last modified"""
    role: Any
    """The role assigned to the user in the account"""
    user: Any
    """The user details including name, email, etc."""


class AccountUsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    account: str
    """The account associated with the user"""
    created: str
    """The date and time when the user account was created"""
    last_modified: str
    """The date and time when the user account was last modified"""
    role: str
    """The role assigned to the user in the account"""
    user: str
    """The user details including name, email, etc."""


class AccountUsersSortFilter(TypedDict, total=False):
    """Available fields for sorting account_users search results."""
    account: AirbyteSortOrder
    """The account associated with the user"""
    created: AirbyteSortOrder
    """The date and time when the user account was created"""
    last_modified: AirbyteSortOrder
    """The date and time when the user account was last modified"""
    role: AirbyteSortOrder
    """The role assigned to the user in the account"""
    user: AirbyteSortOrder
    """The user details including name, email, etc."""


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


class AccountUsersStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AccountUsersStringFilter


class AccountUsersEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AccountUsersStringFilter


class AccountUsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AccountUsersStringFilter


class AccountUsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AccountUsersStringFilter


class AccountUsersContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | AccountUsersStartswithCondition
    | AccountUsersEndswithCondition
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
    targeting_criteria: dict[str, Any] | None
    """Criteria for targeting in the campaign."""
    serving_statuses: list[Any] | None
    """The serving statuses of the campaign."""
    type_: str | None
    """The type of campaign."""
    locale: dict[str, Any] | None
    """The locale settings for the campaign."""
    version: dict[str, Any] | None
    """The version information for the campaign."""
    associated_entity: str | None
    """The entity associated with the campaign."""
    run_schedule: dict[str, Any] | None
    """The schedule for running the campaign."""
    optimization_target_type: str | None
    """The type of optimization target for the campaign."""
    created: str | None
    """The date and time when the campaign was created."""
    last_modified: str | None
    """The date and time when the campaign was last modified."""
    campaign_group: str | None
    """The group to which the campaign belongs."""
    daily_budget: dict[str, Any] | None
    """The daily budget set for the campaign."""
    total_budget: dict[str, Any] | None
    """The total budget amount for the campaign."""
    unit_cost: dict[str, Any] | None
    """The unit cost for the campaign."""
    creative_selection: str | None
    """Information about the creative selection for the campaign."""
    cost_type: str | None
    """The type of cost associated with the campaign."""
    name: str | None
    """The name of the campaign."""
    offsite_delivery_enabled: bool | None
    """Indicates if offsite delivery is enabled for the campaign."""
    id: int | None
    """The unique identifier of the campaign."""
    audience_expansion_enabled: bool | None
    """Indicates if audience expansion is enabled for this campaign."""
    test: bool | None
    """Indicates if the campaign is a test campaign."""
    account: str | None
    """The account associated with the campaign data."""
    status: str | None
    """The status of the campaign."""
    story_delivery_enabled: bool | None
    """Indicates if story delivery is enabled for the campaign."""
    pacing_strategy: str | None
    """The pacing strategy for the campaign."""
    format: str | None
    """The format of the campaign."""
    objective_type: str | None
    """The type of objective for the campaign."""
    offsite_preferences: dict[str, Any] | None
    """Preferences related to offsite delivery."""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    targeting_criteria: list[dict[str, Any]]
    """Criteria for targeting in the campaign."""
    serving_statuses: list[list[Any]]
    """The serving statuses of the campaign."""
    type_: list[str]
    """The type of campaign."""
    locale: list[dict[str, Any]]
    """The locale settings for the campaign."""
    version: list[dict[str, Any]]
    """The version information for the campaign."""
    associated_entity: list[str]
    """The entity associated with the campaign."""
    run_schedule: list[dict[str, Any]]
    """The schedule for running the campaign."""
    optimization_target_type: list[str]
    """The type of optimization target for the campaign."""
    created: list[str]
    """The date and time when the campaign was created."""
    last_modified: list[str]
    """The date and time when the campaign was last modified."""
    campaign_group: list[str]
    """The group to which the campaign belongs."""
    daily_budget: list[dict[str, Any]]
    """The daily budget set for the campaign."""
    total_budget: list[dict[str, Any]]
    """The total budget amount for the campaign."""
    unit_cost: list[dict[str, Any]]
    """The unit cost for the campaign."""
    creative_selection: list[str]
    """Information about the creative selection for the campaign."""
    cost_type: list[str]
    """The type of cost associated with the campaign."""
    name: list[str]
    """The name of the campaign."""
    offsite_delivery_enabled: list[bool]
    """Indicates if offsite delivery is enabled for the campaign."""
    id: list[int]
    """The unique identifier of the campaign."""
    audience_expansion_enabled: list[bool]
    """Indicates if audience expansion is enabled for this campaign."""
    test: list[bool]
    """Indicates if the campaign is a test campaign."""
    account: list[str]
    """The account associated with the campaign data."""
    status: list[str]
    """The status of the campaign."""
    story_delivery_enabled: list[bool]
    """Indicates if story delivery is enabled for the campaign."""
    pacing_strategy: list[str]
    """The pacing strategy for the campaign."""
    format: list[str]
    """The format of the campaign."""
    objective_type: list[str]
    """The type of objective for the campaign."""
    offsite_preferences: list[dict[str, Any]]
    """Preferences related to offsite delivery."""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    targeting_criteria: Any
    """Criteria for targeting in the campaign."""
    serving_statuses: Any
    """The serving statuses of the campaign."""
    type_: Any
    """The type of campaign."""
    locale: Any
    """The locale settings for the campaign."""
    version: Any
    """The version information for the campaign."""
    associated_entity: Any
    """The entity associated with the campaign."""
    run_schedule: Any
    """The schedule for running the campaign."""
    optimization_target_type: Any
    """The type of optimization target for the campaign."""
    created: Any
    """The date and time when the campaign was created."""
    last_modified: Any
    """The date and time when the campaign was last modified."""
    campaign_group: Any
    """The group to which the campaign belongs."""
    daily_budget: Any
    """The daily budget set for the campaign."""
    total_budget: Any
    """The total budget amount for the campaign."""
    unit_cost: Any
    """The unit cost for the campaign."""
    creative_selection: Any
    """Information about the creative selection for the campaign."""
    cost_type: Any
    """The type of cost associated with the campaign."""
    name: Any
    """The name of the campaign."""
    offsite_delivery_enabled: Any
    """Indicates if offsite delivery is enabled for the campaign."""
    id: Any
    """The unique identifier of the campaign."""
    audience_expansion_enabled: Any
    """Indicates if audience expansion is enabled for this campaign."""
    test: Any
    """Indicates if the campaign is a test campaign."""
    account: Any
    """The account associated with the campaign data."""
    status: Any
    """The status of the campaign."""
    story_delivery_enabled: Any
    """Indicates if story delivery is enabled for the campaign."""
    pacing_strategy: Any
    """The pacing strategy for the campaign."""
    format: Any
    """The format of the campaign."""
    objective_type: Any
    """The type of objective for the campaign."""
    offsite_preferences: Any
    """Preferences related to offsite delivery."""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    targeting_criteria: str
    """Criteria for targeting in the campaign."""
    serving_statuses: str
    """The serving statuses of the campaign."""
    type_: str
    """The type of campaign."""
    locale: str
    """The locale settings for the campaign."""
    version: str
    """The version information for the campaign."""
    associated_entity: str
    """The entity associated with the campaign."""
    run_schedule: str
    """The schedule for running the campaign."""
    optimization_target_type: str
    """The type of optimization target for the campaign."""
    created: str
    """The date and time when the campaign was created."""
    last_modified: str
    """The date and time when the campaign was last modified."""
    campaign_group: str
    """The group to which the campaign belongs."""
    daily_budget: str
    """The daily budget set for the campaign."""
    total_budget: str
    """The total budget amount for the campaign."""
    unit_cost: str
    """The unit cost for the campaign."""
    creative_selection: str
    """Information about the creative selection for the campaign."""
    cost_type: str
    """The type of cost associated with the campaign."""
    name: str
    """The name of the campaign."""
    offsite_delivery_enabled: str
    """Indicates if offsite delivery is enabled for the campaign."""
    id: str
    """The unique identifier of the campaign."""
    audience_expansion_enabled: str
    """Indicates if audience expansion is enabled for this campaign."""
    test: str
    """Indicates if the campaign is a test campaign."""
    account: str
    """The account associated with the campaign data."""
    status: str
    """The status of the campaign."""
    story_delivery_enabled: str
    """Indicates if story delivery is enabled for the campaign."""
    pacing_strategy: str
    """The pacing strategy for the campaign."""
    format: str
    """The format of the campaign."""
    objective_type: str
    """The type of objective for the campaign."""
    offsite_preferences: str
    """Preferences related to offsite delivery."""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    targeting_criteria: AirbyteSortOrder
    """Criteria for targeting in the campaign."""
    serving_statuses: AirbyteSortOrder
    """The serving statuses of the campaign."""
    type_: AirbyteSortOrder
    """The type of campaign."""
    locale: AirbyteSortOrder
    """The locale settings for the campaign."""
    version: AirbyteSortOrder
    """The version information for the campaign."""
    associated_entity: AirbyteSortOrder
    """The entity associated with the campaign."""
    run_schedule: AirbyteSortOrder
    """The schedule for running the campaign."""
    optimization_target_type: AirbyteSortOrder
    """The type of optimization target for the campaign."""
    created: AirbyteSortOrder
    """The date and time when the campaign was created."""
    last_modified: AirbyteSortOrder
    """The date and time when the campaign was last modified."""
    campaign_group: AirbyteSortOrder
    """The group to which the campaign belongs."""
    daily_budget: AirbyteSortOrder
    """The daily budget set for the campaign."""
    total_budget: AirbyteSortOrder
    """The total budget amount for the campaign."""
    unit_cost: AirbyteSortOrder
    """The unit cost for the campaign."""
    creative_selection: AirbyteSortOrder
    """Information about the creative selection for the campaign."""
    cost_type: AirbyteSortOrder
    """The type of cost associated with the campaign."""
    name: AirbyteSortOrder
    """The name of the campaign."""
    offsite_delivery_enabled: AirbyteSortOrder
    """Indicates if offsite delivery is enabled for the campaign."""
    id: AirbyteSortOrder
    """The unique identifier of the campaign."""
    audience_expansion_enabled: AirbyteSortOrder
    """Indicates if audience expansion is enabled for this campaign."""
    test: AirbyteSortOrder
    """Indicates if the campaign is a test campaign."""
    account: AirbyteSortOrder
    """The account associated with the campaign data."""
    status: AirbyteSortOrder
    """The status of the campaign."""
    story_delivery_enabled: AirbyteSortOrder
    """Indicates if story delivery is enabled for the campaign."""
    pacing_strategy: AirbyteSortOrder
    """The pacing strategy for the campaign."""
    format: AirbyteSortOrder
    """The format of the campaign."""
    objective_type: AirbyteSortOrder
    """The type of objective for the campaign."""
    offsite_preferences: AirbyteSortOrder
    """Preferences related to offsite delivery."""


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


class CampaignsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CampaignsStringFilter


class CampaignsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CampaignsStringFilter


class CampaignsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CampaignsStringFilter


class CampaignsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CampaignsStringFilter


class CampaignsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | CampaignsStartswithCondition
    | CampaignsEndswithCondition
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
    run_schedule: dict[str, Any] | None
    """Schedule for running the campaign group."""
    created: str | None
    """The date and time when the campaign group was created."""
    last_modified: str | None
    """The date and time when the campaign group was last modified."""
    name: str | None
    """Name of the campaign group."""
    test: bool | None
    """Indicates if the campaign group is a test campaign."""
    total_budget: dict[str, Any] | None
    """Total budget allocated for the campaign group."""
    serving_statuses: list[Any] | None
    """List of serving statuses for the campaign group."""
    backfilled: bool | None
    """Indicates if the campaign group was backfilled."""
    id: int | None
    """Unique identifier for the campaign group."""
    account: str | None
    """The account associated with the campaign group."""
    status: str | None
    """Current status of the campaign group."""
    allowed_campaign_types: list[Any] | None
    """List of campaign types allowed for this campaign group."""


class CampaignGroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    run_schedule: list[dict[str, Any]]
    """Schedule for running the campaign group."""
    created: list[str]
    """The date and time when the campaign group was created."""
    last_modified: list[str]
    """The date and time when the campaign group was last modified."""
    name: list[str]
    """Name of the campaign group."""
    test: list[bool]
    """Indicates if the campaign group is a test campaign."""
    total_budget: list[dict[str, Any]]
    """Total budget allocated for the campaign group."""
    serving_statuses: list[list[Any]]
    """List of serving statuses for the campaign group."""
    backfilled: list[bool]
    """Indicates if the campaign group was backfilled."""
    id: list[int]
    """Unique identifier for the campaign group."""
    account: list[str]
    """The account associated with the campaign group."""
    status: list[str]
    """Current status of the campaign group."""
    allowed_campaign_types: list[list[Any]]
    """List of campaign types allowed for this campaign group."""


class CampaignGroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    run_schedule: Any
    """Schedule for running the campaign group."""
    created: Any
    """The date and time when the campaign group was created."""
    last_modified: Any
    """The date and time when the campaign group was last modified."""
    name: Any
    """Name of the campaign group."""
    test: Any
    """Indicates if the campaign group is a test campaign."""
    total_budget: Any
    """Total budget allocated for the campaign group."""
    serving_statuses: Any
    """List of serving statuses for the campaign group."""
    backfilled: Any
    """Indicates if the campaign group was backfilled."""
    id: Any
    """Unique identifier for the campaign group."""
    account: Any
    """The account associated with the campaign group."""
    status: Any
    """Current status of the campaign group."""
    allowed_campaign_types: Any
    """List of campaign types allowed for this campaign group."""


class CampaignGroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    run_schedule: str
    """Schedule for running the campaign group."""
    created: str
    """The date and time when the campaign group was created."""
    last_modified: str
    """The date and time when the campaign group was last modified."""
    name: str
    """Name of the campaign group."""
    test: str
    """Indicates if the campaign group is a test campaign."""
    total_budget: str
    """Total budget allocated for the campaign group."""
    serving_statuses: str
    """List of serving statuses for the campaign group."""
    backfilled: str
    """Indicates if the campaign group was backfilled."""
    id: str
    """Unique identifier for the campaign group."""
    account: str
    """The account associated with the campaign group."""
    status: str
    """Current status of the campaign group."""
    allowed_campaign_types: str
    """List of campaign types allowed for this campaign group."""


class CampaignGroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaign_groups search results."""
    run_schedule: AirbyteSortOrder
    """Schedule for running the campaign group."""
    created: AirbyteSortOrder
    """The date and time when the campaign group was created."""
    last_modified: AirbyteSortOrder
    """The date and time when the campaign group was last modified."""
    name: AirbyteSortOrder
    """Name of the campaign group."""
    test: AirbyteSortOrder
    """Indicates if the campaign group is a test campaign."""
    total_budget: AirbyteSortOrder
    """Total budget allocated for the campaign group."""
    serving_statuses: AirbyteSortOrder
    """List of serving statuses for the campaign group."""
    backfilled: AirbyteSortOrder
    """Indicates if the campaign group was backfilled."""
    id: AirbyteSortOrder
    """Unique identifier for the campaign group."""
    account: AirbyteSortOrder
    """The account associated with the campaign group."""
    status: AirbyteSortOrder
    """Current status of the campaign group."""
    allowed_campaign_types: AirbyteSortOrder
    """List of campaign types allowed for this campaign group."""


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


class CampaignGroupsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CampaignGroupsStringFilter


class CampaignGroupsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CampaignGroupsStringFilter


class CampaignGroupsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CampaignGroupsStringFilter


class CampaignGroupsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CampaignGroupsStringFilter


class CampaignGroupsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | CampaignGroupsStartswithCondition
    | CampaignGroupsEndswithCondition
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
    serving_hold_reasons: list[Any] | None
    """Reasons for holding the creative from serving."""
    last_modified_at: int | None
    """The timestamp when the creative was last modified."""
    last_modified_by: str | None
    """The user who last modified the creative."""
    content: dict[str, Any] | None
    """The actual content of the creative."""
    created_at: int | None
    """The timestamp when the creative was created."""
    is_test: bool | None
    """Boolean indicating if the creative is a test creative."""
    created_by: str | None
    """The user who created the creative."""
    review: dict[str, Any] | None
    """Review information for the creative."""
    name: str | None
    """The name of the creative."""
    is_serving: bool | None
    """Boolean indicating if the creative is currently serving."""
    campaign: str | None
    """The campaign to which the creative belongs."""
    id: str | None
    """The unique identifier of the creative."""
    intended_status: str | None
    """The intended status of the creative."""
    account: str | None
    """The account associated with the creative."""
    leadgen_call_to_action: dict[str, Any] | None
    """Call-to-action information for lead generation purposes."""


class CreativesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    serving_hold_reasons: list[list[Any]]
    """Reasons for holding the creative from serving."""
    last_modified_at: list[int]
    """The timestamp when the creative was last modified."""
    last_modified_by: list[str]
    """The user who last modified the creative."""
    content: list[dict[str, Any]]
    """The actual content of the creative."""
    created_at: list[int]
    """The timestamp when the creative was created."""
    is_test: list[bool]
    """Boolean indicating if the creative is a test creative."""
    created_by: list[str]
    """The user who created the creative."""
    review: list[dict[str, Any]]
    """Review information for the creative."""
    name: list[str]
    """The name of the creative."""
    is_serving: list[bool]
    """Boolean indicating if the creative is currently serving."""
    campaign: list[str]
    """The campaign to which the creative belongs."""
    id: list[str]
    """The unique identifier of the creative."""
    intended_status: list[str]
    """The intended status of the creative."""
    account: list[str]
    """The account associated with the creative."""
    leadgen_call_to_action: list[dict[str, Any]]
    """Call-to-action information for lead generation purposes."""


class CreativesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    serving_hold_reasons: Any
    """Reasons for holding the creative from serving."""
    last_modified_at: Any
    """The timestamp when the creative was last modified."""
    last_modified_by: Any
    """The user who last modified the creative."""
    content: Any
    """The actual content of the creative."""
    created_at: Any
    """The timestamp when the creative was created."""
    is_test: Any
    """Boolean indicating if the creative is a test creative."""
    created_by: Any
    """The user who created the creative."""
    review: Any
    """Review information for the creative."""
    name: Any
    """The name of the creative."""
    is_serving: Any
    """Boolean indicating if the creative is currently serving."""
    campaign: Any
    """The campaign to which the creative belongs."""
    id: Any
    """The unique identifier of the creative."""
    intended_status: Any
    """The intended status of the creative."""
    account: Any
    """The account associated with the creative."""
    leadgen_call_to_action: Any
    """Call-to-action information for lead generation purposes."""


class CreativesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    serving_hold_reasons: str
    """Reasons for holding the creative from serving."""
    last_modified_at: str
    """The timestamp when the creative was last modified."""
    last_modified_by: str
    """The user who last modified the creative."""
    content: str
    """The actual content of the creative."""
    created_at: str
    """The timestamp when the creative was created."""
    is_test: str
    """Boolean indicating if the creative is a test creative."""
    created_by: str
    """The user who created the creative."""
    review: str
    """Review information for the creative."""
    name: str
    """The name of the creative."""
    is_serving: str
    """Boolean indicating if the creative is currently serving."""
    campaign: str
    """The campaign to which the creative belongs."""
    id: str
    """The unique identifier of the creative."""
    intended_status: str
    """The intended status of the creative."""
    account: str
    """The account associated with the creative."""
    leadgen_call_to_action: str
    """Call-to-action information for lead generation purposes."""


class CreativesSortFilter(TypedDict, total=False):
    """Available fields for sorting creatives search results."""
    serving_hold_reasons: AirbyteSortOrder
    """Reasons for holding the creative from serving."""
    last_modified_at: AirbyteSortOrder
    """The timestamp when the creative was last modified."""
    last_modified_by: AirbyteSortOrder
    """The user who last modified the creative."""
    content: AirbyteSortOrder
    """The actual content of the creative."""
    created_at: AirbyteSortOrder
    """The timestamp when the creative was created."""
    is_test: AirbyteSortOrder
    """Boolean indicating if the creative is a test creative."""
    created_by: AirbyteSortOrder
    """The user who created the creative."""
    review: AirbyteSortOrder
    """Review information for the creative."""
    name: AirbyteSortOrder
    """The name of the creative."""
    is_serving: AirbyteSortOrder
    """Boolean indicating if the creative is currently serving."""
    campaign: AirbyteSortOrder
    """The campaign to which the creative belongs."""
    id: AirbyteSortOrder
    """The unique identifier of the creative."""
    intended_status: AirbyteSortOrder
    """The intended status of the creative."""
    account: AirbyteSortOrder
    """The account associated with the creative."""
    leadgen_call_to_action: AirbyteSortOrder
    """Call-to-action information for lead generation purposes."""


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


class CreativesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CreativesStringFilter


class CreativesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CreativesStringFilter


class CreativesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CreativesStringFilter


class CreativesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CreativesStringFilter


class CreativesContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | CreativesStartswithCondition
    | CreativesEndswithCondition
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
    attribution_type: str | None
    """The type of attribution for the conversion."""
    account: str | None
    """The account associated with the conversion data."""
    campaigns: list[Any] | None
    """List of campaigns related to the conversion."""
    created: int | None
    """Timestamp of when the conversion was created."""
    enabled: bool | None
    """Flag indicating if the conversion tracking is enabled."""
    id: int | None
    """Unique identifier for the conversion."""
    image_pixel_tag: str | None
    """Pixel tag used for tracking the conversion."""
    name: str | None
    """Name of the conversion."""
    type_: str | None
    """Type of conversion."""
    latest_first_party_callback_at: int | None
    """Timestamp of the latest first-party callback for the conversion."""
    post_click_attribution_window_size: int | None
    """Window size for post-click attribution."""
    view_through_attribution_window_size: int | None
    """Window size for view-through attribution."""
    last_callback_at: int | None
    """Timestamp of the last callback for the conversion."""
    last_modified: int | None
    """Timestamp of the last modification made to the conversion."""
    value: dict[str, Any] | None
    """Value associated with the conversion."""
    associated_campaigns: list[Any] | None
    """Campaigns associated with the conversion."""
    url_match_rule_expression: list[Any] | None
    """Expression used for matching URLs for attribution."""
    url_rules: list[Any] | None
    """Rules for URL matching in the conversion."""


class ConversionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    attribution_type: list[str]
    """The type of attribution for the conversion."""
    account: list[str]
    """The account associated with the conversion data."""
    campaigns: list[list[Any]]
    """List of campaigns related to the conversion."""
    created: list[int]
    """Timestamp of when the conversion was created."""
    enabled: list[bool]
    """Flag indicating if the conversion tracking is enabled."""
    id: list[int]
    """Unique identifier for the conversion."""
    image_pixel_tag: list[str]
    """Pixel tag used for tracking the conversion."""
    name: list[str]
    """Name of the conversion."""
    type_: list[str]
    """Type of conversion."""
    latest_first_party_callback_at: list[int]
    """Timestamp of the latest first-party callback for the conversion."""
    post_click_attribution_window_size: list[int]
    """Window size for post-click attribution."""
    view_through_attribution_window_size: list[int]
    """Window size for view-through attribution."""
    last_callback_at: list[int]
    """Timestamp of the last callback for the conversion."""
    last_modified: list[int]
    """Timestamp of the last modification made to the conversion."""
    value: list[dict[str, Any]]
    """Value associated with the conversion."""
    associated_campaigns: list[list[Any]]
    """Campaigns associated with the conversion."""
    url_match_rule_expression: list[list[Any]]
    """Expression used for matching URLs for attribution."""
    url_rules: list[list[Any]]
    """Rules for URL matching in the conversion."""


class ConversionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    attribution_type: Any
    """The type of attribution for the conversion."""
    account: Any
    """The account associated with the conversion data."""
    campaigns: Any
    """List of campaigns related to the conversion."""
    created: Any
    """Timestamp of when the conversion was created."""
    enabled: Any
    """Flag indicating if the conversion tracking is enabled."""
    id: Any
    """Unique identifier for the conversion."""
    image_pixel_tag: Any
    """Pixel tag used for tracking the conversion."""
    name: Any
    """Name of the conversion."""
    type_: Any
    """Type of conversion."""
    latest_first_party_callback_at: Any
    """Timestamp of the latest first-party callback for the conversion."""
    post_click_attribution_window_size: Any
    """Window size for post-click attribution."""
    view_through_attribution_window_size: Any
    """Window size for view-through attribution."""
    last_callback_at: Any
    """Timestamp of the last callback for the conversion."""
    last_modified: Any
    """Timestamp of the last modification made to the conversion."""
    value: Any
    """Value associated with the conversion."""
    associated_campaigns: Any
    """Campaigns associated with the conversion."""
    url_match_rule_expression: Any
    """Expression used for matching URLs for attribution."""
    url_rules: Any
    """Rules for URL matching in the conversion."""


class ConversionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    attribution_type: str
    """The type of attribution for the conversion."""
    account: str
    """The account associated with the conversion data."""
    campaigns: str
    """List of campaigns related to the conversion."""
    created: str
    """Timestamp of when the conversion was created."""
    enabled: str
    """Flag indicating if the conversion tracking is enabled."""
    id: str
    """Unique identifier for the conversion."""
    image_pixel_tag: str
    """Pixel tag used for tracking the conversion."""
    name: str
    """Name of the conversion."""
    type_: str
    """Type of conversion."""
    latest_first_party_callback_at: str
    """Timestamp of the latest first-party callback for the conversion."""
    post_click_attribution_window_size: str
    """Window size for post-click attribution."""
    view_through_attribution_window_size: str
    """Window size for view-through attribution."""
    last_callback_at: str
    """Timestamp of the last callback for the conversion."""
    last_modified: str
    """Timestamp of the last modification made to the conversion."""
    value: str
    """Value associated with the conversion."""
    associated_campaigns: str
    """Campaigns associated with the conversion."""
    url_match_rule_expression: str
    """Expression used for matching URLs for attribution."""
    url_rules: str
    """Rules for URL matching in the conversion."""


class ConversionsSortFilter(TypedDict, total=False):
    """Available fields for sorting conversions search results."""
    attribution_type: AirbyteSortOrder
    """The type of attribution for the conversion."""
    account: AirbyteSortOrder
    """The account associated with the conversion data."""
    campaigns: AirbyteSortOrder
    """List of campaigns related to the conversion."""
    created: AirbyteSortOrder
    """Timestamp of when the conversion was created."""
    enabled: AirbyteSortOrder
    """Flag indicating if the conversion tracking is enabled."""
    id: AirbyteSortOrder
    """Unique identifier for the conversion."""
    image_pixel_tag: AirbyteSortOrder
    """Pixel tag used for tracking the conversion."""
    name: AirbyteSortOrder
    """Name of the conversion."""
    type_: AirbyteSortOrder
    """Type of conversion."""
    latest_first_party_callback_at: AirbyteSortOrder
    """Timestamp of the latest first-party callback for the conversion."""
    post_click_attribution_window_size: AirbyteSortOrder
    """Window size for post-click attribution."""
    view_through_attribution_window_size: AirbyteSortOrder
    """Window size for view-through attribution."""
    last_callback_at: AirbyteSortOrder
    """Timestamp of the last callback for the conversion."""
    last_modified: AirbyteSortOrder
    """Timestamp of the last modification made to the conversion."""
    value: AirbyteSortOrder
    """Value associated with the conversion."""
    associated_campaigns: AirbyteSortOrder
    """Campaigns associated with the conversion."""
    url_match_rule_expression: AirbyteSortOrder
    """Expression used for matching URLs for attribution."""
    url_rules: AirbyteSortOrder
    """Rules for URL matching in the conversion."""


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


class ConversionsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: ConversionsStringFilter


class ConversionsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: ConversionsStringFilter


class ConversionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ConversionsStringFilter


class ConversionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ConversionsStringFilter


class ConversionsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | ConversionsStartswithCondition
    | ConversionsEndswithCondition
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
    action_clicks: float | None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None
    """An approximation of unique ad impressions."""
    card_clicks: float | None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None
    """The number of times interactive cards were displayed."""
    clicks: float | None
    """Total number of clicks on the ad."""
    comment_likes: float | None
    """The count of likes on comments related to the ad."""
    comments: float | None
    """The number of comments on the ad."""
    company_page_clicks: float | None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None
    """Cost of ad campaign in USD."""
    document_completions: float | None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None
    """Completions for third quartile of document views."""
    download_clicks: float | None
    """Clicks on download links in the ad."""
    end_date: str | None
    """End date of the ad analytics data."""
    external_website_conversions: float | None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites."""
    follows: float | None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None
    """Total number of times the ad was displayed."""
    job_applications: float | None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None
    """Leads generated in one click."""
    opens: float | None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None
    """Registrations completed post-viewing the ad."""
    reactions: float | None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None
    """Total registrations completed through the ad."""
    sends: float | None
    """Number of messages sent through the ad."""
    shares: float | None
    """Total shares generated by the ad."""
    start_date: str | None
    """Start date of the ad analytics data."""
    talent_leads: float | None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None
    """Leads generated through valid work emails."""
    video_completions: float | None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None
    """Completions for midpoint of video views."""
    video_starts: float | None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None
    """Completions for third quartile of video views."""
    video_views: float | None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdCampaignAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    action_clicks: list[float]
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: list[float]
    """The number of clicks on ad unit components."""
    approximate_member_reach: list[float]
    """An approximation of unique ad impressions."""
    card_clicks: list[float]
    """The number of clicks on interactive card elements."""
    card_impressions: list[float]
    """The number of times interactive cards were displayed."""
    clicks: list[float]
    """Total number of clicks on the ad."""
    comment_likes: list[float]
    """The count of likes on comments related to the ad."""
    comments: list[float]
    """The number of comments on the ad."""
    company_page_clicks: list[float]
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: list[float]
    """Conversion value in the local currency."""
    cost_in_local_currency: list[float]
    """Cost of ad campaign in the local currency."""
    cost_in_usd: list[float]
    """Cost of ad campaign in USD."""
    document_completions: list[float]
    """Number of completions for document views."""
    document_first_quartile_completions: list[float]
    """Completions for first quartile of document views."""
    document_midpoint_completions: list[float]
    """Completions for midpoint of document views."""
    document_third_quartile_completions: list[float]
    """Completions for third quartile of document views."""
    download_clicks: list[float]
    """Clicks on download links in the ad."""
    end_date: list[str]
    """End date of the ad analytics data."""
    external_website_conversions: list[float]
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites."""
    follows: list[float]
    """Number of follows generated by the ad."""
    full_screen_plays: list[float]
    """Number of times videos were played in fullscreen mode."""
    impressions: list[float]
    """Total number of times the ad was displayed."""
    job_applications: list[float]
    """Number of job applications initiated through the ad."""
    job_apply_clicks: list[float]
    """Clicks on apply job button in the ad."""
    landing_page_clicks: list[float]
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: list[float]
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: list[float]
    """Clicks on expressing interest through lead generation mail."""
    likes: list[float]
    """Total likes received on the ad."""
    one_click_lead_form_opens: list[float]
    """Number of times lead forms were opened in one click."""
    one_click_leads: list[float]
    """Leads generated in one click."""
    opens: list[float]
    """The number of times the ad was opened or expanded."""
    other_engagements: list[float]
    """Engagements other than clicks on the ad."""
    pivot_values: list[list[Any]]
    """Values used for pivoting the analytics."""
    string_of_pivot_values: list[str]
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: list[float]
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: list[float]
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: list[float]
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: list[float]
    """Registrations completed post-viewing the ad."""
    reactions: list[float]
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: list[float]
    """Total registrations completed through the ad."""
    sends: list[float]
    """Number of messages sent through the ad."""
    shares: list[float]
    """Total shares generated by the ad."""
    start_date: list[str]
    """Start date of the ad analytics data."""
    talent_leads: list[float]
    """Number of leads related to talent acquisition."""
    text_url_clicks: list[float]
    """Clicks on text URLs within the ad."""
    total_engagements: list[float]
    """Total number of engagements on the ad."""
    valid_work_email_leads: list[float]
    """Leads generated through valid work emails."""
    video_completions: list[float]
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: list[float]
    """Completions for first quartile of video views."""
    video_midpoint_completions: list[float]
    """Completions for midpoint of video views."""
    video_starts: list[float]
    """Total video starts initiated by users."""
    video_third_quartile_completions: list[float]
    """Completions for third quartile of video views."""
    video_views: list[float]
    """Total views of videos in the ad."""
    viral_card_clicks: list[float]
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: list[float]
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: list[float]
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: list[float]
    """Likes received on comments in viral distribution."""
    viral_comments: list[float]
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: list[float]
    """Clicks on the company page in viral distribution."""
    viral_document_completions: list[float]
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: list[float]
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: list[float]
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: list[float]
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: list[float]
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: list[float]
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: list[float]
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: list[float]
    """Fullscreen video plays in viral distribution."""
    viral_impressions: list[float]
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: list[float]
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: list[float]
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: list[float]
    """Clicks on landing page in viral distribution."""
    viral_likes: list[float]
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: list[float]
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: list[float]
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: list[float]
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: list[float]
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: list[float]
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: list[float]
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: list[float]
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: list[float]
    """Total reactions in viral distribution of the ad."""
    viral_registrations: list[float]
    """Total registrations in viral distribution of the ad."""
    viral_shares: list[float]
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: list[float]
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: list[float]
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: list[float]
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: list[float]
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: list[float]
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: list[float]
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: list[float]
    """Total views of videos in viral distribution of the ad."""
    pivot: list[str]
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: list[str]
    """URN of the sponsored campaign this analytics record belongs to"""


class AdCampaignAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    action_clicks: Any
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: Any
    """The number of clicks on ad unit components."""
    approximate_member_reach: Any
    """An approximation of unique ad impressions."""
    card_clicks: Any
    """The number of clicks on interactive card elements."""
    card_impressions: Any
    """The number of times interactive cards were displayed."""
    clicks: Any
    """Total number of clicks on the ad."""
    comment_likes: Any
    """The count of likes on comments related to the ad."""
    comments: Any
    """The number of comments on the ad."""
    company_page_clicks: Any
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: Any
    """Conversion value in the local currency."""
    cost_in_local_currency: Any
    """Cost of ad campaign in the local currency."""
    cost_in_usd: Any
    """Cost of ad campaign in USD."""
    document_completions: Any
    """Number of completions for document views."""
    document_first_quartile_completions: Any
    """Completions for first quartile of document views."""
    document_midpoint_completions: Any
    """Completions for midpoint of document views."""
    document_third_quartile_completions: Any
    """Completions for third quartile of document views."""
    download_clicks: Any
    """Clicks on download links in the ad."""
    end_date: Any
    """End date of the ad analytics data."""
    external_website_conversions: Any
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites."""
    follows: Any
    """Number of follows generated by the ad."""
    full_screen_plays: Any
    """Number of times videos were played in fullscreen mode."""
    impressions: Any
    """Total number of times the ad was displayed."""
    job_applications: Any
    """Number of job applications initiated through the ad."""
    job_apply_clicks: Any
    """Clicks on apply job button in the ad."""
    landing_page_clicks: Any
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: Any
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: Any
    """Clicks on expressing interest through lead generation mail."""
    likes: Any
    """Total likes received on the ad."""
    one_click_lead_form_opens: Any
    """Number of times lead forms were opened in one click."""
    one_click_leads: Any
    """Leads generated in one click."""
    opens: Any
    """The number of times the ad was opened or expanded."""
    other_engagements: Any
    """Engagements other than clicks on the ad."""
    pivot_values: Any
    """Values used for pivoting the analytics."""
    string_of_pivot_values: Any
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: Any
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: Any
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: Any
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: Any
    """Registrations completed post-viewing the ad."""
    reactions: Any
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: Any
    """Total registrations completed through the ad."""
    sends: Any
    """Number of messages sent through the ad."""
    shares: Any
    """Total shares generated by the ad."""
    start_date: Any
    """Start date of the ad analytics data."""
    talent_leads: Any
    """Number of leads related to talent acquisition."""
    text_url_clicks: Any
    """Clicks on text URLs within the ad."""
    total_engagements: Any
    """Total number of engagements on the ad."""
    valid_work_email_leads: Any
    """Leads generated through valid work emails."""
    video_completions: Any
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: Any
    """Completions for first quartile of video views."""
    video_midpoint_completions: Any
    """Completions for midpoint of video views."""
    video_starts: Any
    """Total video starts initiated by users."""
    video_third_quartile_completions: Any
    """Completions for third quartile of video views."""
    video_views: Any
    """Total views of videos in the ad."""
    viral_card_clicks: Any
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: Any
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: Any
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: Any
    """Likes received on comments in viral distribution."""
    viral_comments: Any
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: Any
    """Clicks on the company page in viral distribution."""
    viral_document_completions: Any
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: Any
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: Any
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: Any
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: Any
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: Any
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: Any
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: Any
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: Any
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: Any
    """Fullscreen video plays in viral distribution."""
    viral_impressions: Any
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: Any
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: Any
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: Any
    """Clicks on landing page in viral distribution."""
    viral_likes: Any
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: Any
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: Any
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: Any
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: Any
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: Any
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: Any
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: Any
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: Any
    """Total reactions in viral distribution of the ad."""
    viral_registrations: Any
    """Total registrations in viral distribution of the ad."""
    viral_shares: Any
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: Any
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: Any
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: Any
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: Any
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: Any
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: Any
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: Any
    """Total views of videos in viral distribution of the ad."""
    pivot: Any
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: Any
    """URN of the sponsored campaign this analytics record belongs to"""


class AdCampaignAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    action_clicks: str
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: str
    """The number of clicks on ad unit components."""
    approximate_member_reach: str
    """An approximation of unique ad impressions."""
    card_clicks: str
    """The number of clicks on interactive card elements."""
    card_impressions: str
    """The number of times interactive cards were displayed."""
    clicks: str
    """Total number of clicks on the ad."""
    comment_likes: str
    """The count of likes on comments related to the ad."""
    comments: str
    """The number of comments on the ad."""
    company_page_clicks: str
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: str
    """Conversion value in the local currency."""
    cost_in_local_currency: str
    """Cost of ad campaign in the local currency."""
    cost_in_usd: str
    """Cost of ad campaign in USD."""
    document_completions: str
    """Number of completions for document views."""
    document_first_quartile_completions: str
    """Completions for first quartile of document views."""
    document_midpoint_completions: str
    """Completions for midpoint of document views."""
    document_third_quartile_completions: str
    """Completions for third quartile of document views."""
    download_clicks: str
    """Clicks on download links in the ad."""
    end_date: str
    """End date of the ad analytics data."""
    external_website_conversions: str
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites."""
    follows: str
    """Number of follows generated by the ad."""
    full_screen_plays: str
    """Number of times videos were played in fullscreen mode."""
    impressions: str
    """Total number of times the ad was displayed."""
    job_applications: str
    """Number of job applications initiated through the ad."""
    job_apply_clicks: str
    """Clicks on apply job button in the ad."""
    landing_page_clicks: str
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: str
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: str
    """Clicks on expressing interest through lead generation mail."""
    likes: str
    """Total likes received on the ad."""
    one_click_lead_form_opens: str
    """Number of times lead forms were opened in one click."""
    one_click_leads: str
    """Leads generated in one click."""
    opens: str
    """The number of times the ad was opened or expanded."""
    other_engagements: str
    """Engagements other than clicks on the ad."""
    pivot_values: str
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: str
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: str
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: str
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: str
    """Registrations completed post-viewing the ad."""
    reactions: str
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: str
    """Total registrations completed through the ad."""
    sends: str
    """Number of messages sent through the ad."""
    shares: str
    """Total shares generated by the ad."""
    start_date: str
    """Start date of the ad analytics data."""
    talent_leads: str
    """Number of leads related to talent acquisition."""
    text_url_clicks: str
    """Clicks on text URLs within the ad."""
    total_engagements: str
    """Total number of engagements on the ad."""
    valid_work_email_leads: str
    """Leads generated through valid work emails."""
    video_completions: str
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: str
    """Completions for first quartile of video views."""
    video_midpoint_completions: str
    """Completions for midpoint of video views."""
    video_starts: str
    """Total video starts initiated by users."""
    video_third_quartile_completions: str
    """Completions for third quartile of video views."""
    video_views: str
    """Total views of videos in the ad."""
    viral_card_clicks: str
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: str
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: str
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: str
    """Likes received on comments in viral distribution."""
    viral_comments: str
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: str
    """Clicks on the company page in viral distribution."""
    viral_document_completions: str
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: str
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: str
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: str
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: str
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: str
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: str
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: str
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: str
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: str
    """Fullscreen video plays in viral distribution."""
    viral_impressions: str
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: str
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: str
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: str
    """Clicks on landing page in viral distribution."""
    viral_likes: str
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: str
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: str
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: str
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: str
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: str
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: str
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: str
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: str
    """Total reactions in viral distribution of the ad."""
    viral_registrations: str
    """Total registrations in viral distribution of the ad."""
    viral_shares: str
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: str
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: str
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: str
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: str
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: str
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: str
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: str
    """Total views of videos in viral distribution of the ad."""
    pivot: str
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str
    """URN of the sponsored campaign this analytics record belongs to"""


class AdCampaignAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_campaign_analytics search results."""
    action_clicks: AirbyteSortOrder
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: AirbyteSortOrder
    """The number of clicks on ad unit components."""
    approximate_member_reach: AirbyteSortOrder
    """An approximation of unique ad impressions."""
    card_clicks: AirbyteSortOrder
    """The number of clicks on interactive card elements."""
    card_impressions: AirbyteSortOrder
    """The number of times interactive cards were displayed."""
    clicks: AirbyteSortOrder
    """Total number of clicks on the ad."""
    comment_likes: AirbyteSortOrder
    """The count of likes on comments related to the ad."""
    comments: AirbyteSortOrder
    """The number of comments on the ad."""
    company_page_clicks: AirbyteSortOrder
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in the local currency."""
    cost_in_local_currency: AirbyteSortOrder
    """Cost of ad campaign in the local currency."""
    cost_in_usd: AirbyteSortOrder
    """Cost of ad campaign in USD."""
    document_completions: AirbyteSortOrder
    """Number of completions for document views."""
    document_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of document views."""
    document_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of document views."""
    document_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of document views."""
    download_clicks: AirbyteSortOrder
    """Clicks on download links in the ad."""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data."""
    external_website_conversions: AirbyteSortOrder
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites."""
    follows: AirbyteSortOrder
    """Number of follows generated by the ad."""
    full_screen_plays: AirbyteSortOrder
    """Number of times videos were played in fullscreen mode."""
    impressions: AirbyteSortOrder
    """Total number of times the ad was displayed."""
    job_applications: AirbyteSortOrder
    """Number of job applications initiated through the ad."""
    job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in the ad."""
    landing_page_clicks: AirbyteSortOrder
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: AirbyteSortOrder
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: AirbyteSortOrder
    """Clicks on expressing interest through lead generation mail."""
    likes: AirbyteSortOrder
    """Total likes received on the ad."""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of times lead forms were opened in one click."""
    one_click_leads: AirbyteSortOrder
    """Leads generated in one click."""
    opens: AirbyteSortOrder
    """The number of times the ad was opened or expanded."""
    other_engagements: AirbyteSortOrder
    """Engagements other than clicks on the ad."""
    pivot_values: AirbyteSortOrder
    """Values used for pivoting the analytics."""
    string_of_pivot_values: AirbyteSortOrder
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing the ad."""
    reactions: AirbyteSortOrder
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: AirbyteSortOrder
    """Total registrations completed through the ad."""
    sends: AirbyteSortOrder
    """Number of messages sent through the ad."""
    shares: AirbyteSortOrder
    """Total shares generated by the ad."""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data."""
    talent_leads: AirbyteSortOrder
    """Number of leads related to talent acquisition."""
    text_url_clicks: AirbyteSortOrder
    """Clicks on text URLs within the ad."""
    total_engagements: AirbyteSortOrder
    """Total number of engagements on the ad."""
    valid_work_email_leads: AirbyteSortOrder
    """Leads generated through valid work emails."""
    video_completions: AirbyteSortOrder
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of video views."""
    video_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of video views."""
    video_starts: AirbyteSortOrder
    """Total video starts initiated by users."""
    video_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of video views."""
    video_views: AirbyteSortOrder
    """Total views of videos in the ad."""
    viral_card_clicks: AirbyteSortOrder
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: AirbyteSortOrder
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: AirbyteSortOrder
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: AirbyteSortOrder
    """Likes received on comments in viral distribution."""
    viral_comments: AirbyteSortOrder
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: AirbyteSortOrder
    """Clicks on the company page in viral distribution."""
    viral_document_completions: AirbyteSortOrder
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: AirbyteSortOrder
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: AirbyteSortOrder
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: AirbyteSortOrder
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: AirbyteSortOrder
    """Fullscreen video plays in viral distribution."""
    viral_impressions: AirbyteSortOrder
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: AirbyteSortOrder
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: AirbyteSortOrder
    """Clicks on landing page in viral distribution."""
    viral_likes: AirbyteSortOrder
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: AirbyteSortOrder
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: AirbyteSortOrder
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: AirbyteSortOrder
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: AirbyteSortOrder
    """Total reactions in viral distribution of the ad."""
    viral_registrations: AirbyteSortOrder
    """Total registrations in viral distribution of the ad."""
    viral_shares: AirbyteSortOrder
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: AirbyteSortOrder
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: AirbyteSortOrder
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: AirbyteSortOrder
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: AirbyteSortOrder
    """Total views of videos in viral distribution of the ad."""
    pivot: AirbyteSortOrder
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: AirbyteSortOrder
    """URN of the sponsored campaign this analytics record belongs to"""


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


class AdCampaignAnalyticsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AdCampaignAnalyticsStringFilter


class AdCampaignAnalyticsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AdCampaignAnalyticsStringFilter


class AdCampaignAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdCampaignAnalyticsStringFilter


class AdCampaignAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdCampaignAnalyticsStringFilter


class AdCampaignAnalyticsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | AdCampaignAnalyticsStartswithCondition
    | AdCampaignAnalyticsEndswithCondition
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
    action_clicks: float | None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None
    """An approximation of unique ad impressions."""
    card_clicks: float | None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None
    """The number of times interactive cards were displayed."""
    clicks: float | None
    """Total number of clicks on the ad."""
    comment_likes: float | None
    """The count of likes on comments related to the ad."""
    comments: float | None
    """The number of comments on the ad."""
    company_page_clicks: float | None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None
    """Cost of ad campaign in USD."""
    document_completions: float | None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None
    """Completions for third quartile of document views."""
    download_clicks: float | None
    """Clicks on download links in the ad."""
    end_date: str | None
    """End date of the ad analytics data."""
    external_website_conversions: float | None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites."""
    follows: float | None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None
    """Total number of times the ad was displayed."""
    job_applications: float | None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None
    """Leads generated in one click."""
    opens: float | None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None
    """Registrations completed post-viewing the ad."""
    reactions: float | None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None
    """Total registrations completed through the ad."""
    sends: float | None
    """Number of messages sent through the ad."""
    shares: float | None
    """Total shares generated by the ad."""
    start_date: str | None
    """Start date of the ad analytics data."""
    talent_leads: float | None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None
    """Leads generated through valid work emails."""
    video_completions: float | None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None
    """Completions for midpoint of video views."""
    video_starts: float | None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None
    """Completions for third quartile of video views."""
    video_views: float | None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None
    """Pivot dimension used for this analytics record"""
    sponsored_creative: str | None
    """Sponsored creative"""


class AdCreativeAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    action_clicks: list[float]
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: list[float]
    """The number of clicks on ad unit components."""
    approximate_member_reach: list[float]
    """An approximation of unique ad impressions."""
    card_clicks: list[float]
    """The number of clicks on interactive card elements."""
    card_impressions: list[float]
    """The number of times interactive cards were displayed."""
    clicks: list[float]
    """Total number of clicks on the ad."""
    comment_likes: list[float]
    """The count of likes on comments related to the ad."""
    comments: list[float]
    """The number of comments on the ad."""
    company_page_clicks: list[float]
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: list[float]
    """Conversion value in the local currency."""
    cost_in_local_currency: list[float]
    """Cost of ad campaign in the local currency."""
    cost_in_usd: list[float]
    """Cost of ad campaign in USD."""
    document_completions: list[float]
    """Number of completions for document views."""
    document_first_quartile_completions: list[float]
    """Completions for first quartile of document views."""
    document_midpoint_completions: list[float]
    """Completions for midpoint of document views."""
    document_third_quartile_completions: list[float]
    """Completions for third quartile of document views."""
    download_clicks: list[float]
    """Clicks on download links in the ad."""
    end_date: list[str]
    """End date of the ad analytics data."""
    external_website_conversions: list[float]
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites."""
    follows: list[float]
    """Number of follows generated by the ad."""
    full_screen_plays: list[float]
    """Number of times videos were played in fullscreen mode."""
    impressions: list[float]
    """Total number of times the ad was displayed."""
    job_applications: list[float]
    """Number of job applications initiated through the ad."""
    job_apply_clicks: list[float]
    """Clicks on apply job button in the ad."""
    landing_page_clicks: list[float]
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: list[float]
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: list[float]
    """Clicks on expressing interest through lead generation mail."""
    likes: list[float]
    """Total likes received on the ad."""
    one_click_lead_form_opens: list[float]
    """Number of times lead forms were opened in one click."""
    one_click_leads: list[float]
    """Leads generated in one click."""
    opens: list[float]
    """The number of times the ad was opened or expanded."""
    other_engagements: list[float]
    """Engagements other than clicks on the ad."""
    pivot_values: list[list[Any]]
    """Values used for pivoting the analytics."""
    string_of_pivot_values: list[str]
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: list[float]
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: list[float]
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: list[float]
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: list[float]
    """Registrations completed post-viewing the ad."""
    reactions: list[float]
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: list[float]
    """Total registrations completed through the ad."""
    sends: list[float]
    """Number of messages sent through the ad."""
    shares: list[float]
    """Total shares generated by the ad."""
    start_date: list[str]
    """Start date of the ad analytics data."""
    talent_leads: list[float]
    """Number of leads related to talent acquisition."""
    text_url_clicks: list[float]
    """Clicks on text URLs within the ad."""
    total_engagements: list[float]
    """Total number of engagements on the ad."""
    valid_work_email_leads: list[float]
    """Leads generated through valid work emails."""
    video_completions: list[float]
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: list[float]
    """Completions for first quartile of video views."""
    video_midpoint_completions: list[float]
    """Completions for midpoint of video views."""
    video_starts: list[float]
    """Total video starts initiated by users."""
    video_third_quartile_completions: list[float]
    """Completions for third quartile of video views."""
    video_views: list[float]
    """Total views of videos in the ad."""
    viral_card_clicks: list[float]
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: list[float]
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: list[float]
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: list[float]
    """Likes received on comments in viral distribution."""
    viral_comments: list[float]
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: list[float]
    """Clicks on the company page in viral distribution."""
    viral_document_completions: list[float]
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: list[float]
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: list[float]
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: list[float]
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: list[float]
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: list[float]
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: list[float]
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: list[float]
    """Fullscreen video plays in viral distribution."""
    viral_impressions: list[float]
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: list[float]
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: list[float]
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: list[float]
    """Clicks on landing page in viral distribution."""
    viral_likes: list[float]
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: list[float]
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: list[float]
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: list[float]
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: list[float]
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: list[float]
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: list[float]
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: list[float]
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: list[float]
    """Total reactions in viral distribution of the ad."""
    viral_registrations: list[float]
    """Total registrations in viral distribution of the ad."""
    viral_shares: list[float]
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: list[float]
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: list[float]
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: list[float]
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: list[float]
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: list[float]
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: list[float]
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: list[float]
    """Total views of videos in viral distribution of the ad."""
    pivot: list[str]
    """Pivot dimension used for this analytics record"""
    sponsored_creative: list[str]
    """Sponsored creative"""


class AdCreativeAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    action_clicks: Any
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: Any
    """The number of clicks on ad unit components."""
    approximate_member_reach: Any
    """An approximation of unique ad impressions."""
    card_clicks: Any
    """The number of clicks on interactive card elements."""
    card_impressions: Any
    """The number of times interactive cards were displayed."""
    clicks: Any
    """Total number of clicks on the ad."""
    comment_likes: Any
    """The count of likes on comments related to the ad."""
    comments: Any
    """The number of comments on the ad."""
    company_page_clicks: Any
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: Any
    """Conversion value in the local currency."""
    cost_in_local_currency: Any
    """Cost of ad campaign in the local currency."""
    cost_in_usd: Any
    """Cost of ad campaign in USD."""
    document_completions: Any
    """Number of completions for document views."""
    document_first_quartile_completions: Any
    """Completions for first quartile of document views."""
    document_midpoint_completions: Any
    """Completions for midpoint of document views."""
    document_third_quartile_completions: Any
    """Completions for third quartile of document views."""
    download_clicks: Any
    """Clicks on download links in the ad."""
    end_date: Any
    """End date of the ad analytics data."""
    external_website_conversions: Any
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites."""
    follows: Any
    """Number of follows generated by the ad."""
    full_screen_plays: Any
    """Number of times videos were played in fullscreen mode."""
    impressions: Any
    """Total number of times the ad was displayed."""
    job_applications: Any
    """Number of job applications initiated through the ad."""
    job_apply_clicks: Any
    """Clicks on apply job button in the ad."""
    landing_page_clicks: Any
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: Any
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: Any
    """Clicks on expressing interest through lead generation mail."""
    likes: Any
    """Total likes received on the ad."""
    one_click_lead_form_opens: Any
    """Number of times lead forms were opened in one click."""
    one_click_leads: Any
    """Leads generated in one click."""
    opens: Any
    """The number of times the ad was opened or expanded."""
    other_engagements: Any
    """Engagements other than clicks on the ad."""
    pivot_values: Any
    """Values used for pivoting the analytics."""
    string_of_pivot_values: Any
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: Any
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: Any
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: Any
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: Any
    """Registrations completed post-viewing the ad."""
    reactions: Any
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: Any
    """Total registrations completed through the ad."""
    sends: Any
    """Number of messages sent through the ad."""
    shares: Any
    """Total shares generated by the ad."""
    start_date: Any
    """Start date of the ad analytics data."""
    talent_leads: Any
    """Number of leads related to talent acquisition."""
    text_url_clicks: Any
    """Clicks on text URLs within the ad."""
    total_engagements: Any
    """Total number of engagements on the ad."""
    valid_work_email_leads: Any
    """Leads generated through valid work emails."""
    video_completions: Any
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: Any
    """Completions for first quartile of video views."""
    video_midpoint_completions: Any
    """Completions for midpoint of video views."""
    video_starts: Any
    """Total video starts initiated by users."""
    video_third_quartile_completions: Any
    """Completions for third quartile of video views."""
    video_views: Any
    """Total views of videos in the ad."""
    viral_card_clicks: Any
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: Any
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: Any
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: Any
    """Likes received on comments in viral distribution."""
    viral_comments: Any
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: Any
    """Clicks on the company page in viral distribution."""
    viral_document_completions: Any
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: Any
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: Any
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: Any
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: Any
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: Any
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: Any
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: Any
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: Any
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: Any
    """Fullscreen video plays in viral distribution."""
    viral_impressions: Any
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: Any
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: Any
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: Any
    """Clicks on landing page in viral distribution."""
    viral_likes: Any
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: Any
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: Any
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: Any
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: Any
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: Any
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: Any
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: Any
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: Any
    """Total reactions in viral distribution of the ad."""
    viral_registrations: Any
    """Total registrations in viral distribution of the ad."""
    viral_shares: Any
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: Any
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: Any
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: Any
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: Any
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: Any
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: Any
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: Any
    """Total views of videos in viral distribution of the ad."""
    pivot: Any
    """Pivot dimension used for this analytics record"""
    sponsored_creative: Any
    """Sponsored creative"""


class AdCreativeAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    action_clicks: str
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: str
    """The number of clicks on ad unit components."""
    approximate_member_reach: str
    """An approximation of unique ad impressions."""
    card_clicks: str
    """The number of clicks on interactive card elements."""
    card_impressions: str
    """The number of times interactive cards were displayed."""
    clicks: str
    """Total number of clicks on the ad."""
    comment_likes: str
    """The count of likes on comments related to the ad."""
    comments: str
    """The number of comments on the ad."""
    company_page_clicks: str
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: str
    """Conversion value in the local currency."""
    cost_in_local_currency: str
    """Cost of ad campaign in the local currency."""
    cost_in_usd: str
    """Cost of ad campaign in USD."""
    document_completions: str
    """Number of completions for document views."""
    document_first_quartile_completions: str
    """Completions for first quartile of document views."""
    document_midpoint_completions: str
    """Completions for midpoint of document views."""
    document_third_quartile_completions: str
    """Completions for third quartile of document views."""
    download_clicks: str
    """Clicks on download links in the ad."""
    end_date: str
    """End date of the ad analytics data."""
    external_website_conversions: str
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites."""
    follows: str
    """Number of follows generated by the ad."""
    full_screen_plays: str
    """Number of times videos were played in fullscreen mode."""
    impressions: str
    """Total number of times the ad was displayed."""
    job_applications: str
    """Number of job applications initiated through the ad."""
    job_apply_clicks: str
    """Clicks on apply job button in the ad."""
    landing_page_clicks: str
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: str
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: str
    """Clicks on expressing interest through lead generation mail."""
    likes: str
    """Total likes received on the ad."""
    one_click_lead_form_opens: str
    """Number of times lead forms were opened in one click."""
    one_click_leads: str
    """Leads generated in one click."""
    opens: str
    """The number of times the ad was opened or expanded."""
    other_engagements: str
    """Engagements other than clicks on the ad."""
    pivot_values: str
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: str
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: str
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: str
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: str
    """Registrations completed post-viewing the ad."""
    reactions: str
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: str
    """Total registrations completed through the ad."""
    sends: str
    """Number of messages sent through the ad."""
    shares: str
    """Total shares generated by the ad."""
    start_date: str
    """Start date of the ad analytics data."""
    talent_leads: str
    """Number of leads related to talent acquisition."""
    text_url_clicks: str
    """Clicks on text URLs within the ad."""
    total_engagements: str
    """Total number of engagements on the ad."""
    valid_work_email_leads: str
    """Leads generated through valid work emails."""
    video_completions: str
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: str
    """Completions for first quartile of video views."""
    video_midpoint_completions: str
    """Completions for midpoint of video views."""
    video_starts: str
    """Total video starts initiated by users."""
    video_third_quartile_completions: str
    """Completions for third quartile of video views."""
    video_views: str
    """Total views of videos in the ad."""
    viral_card_clicks: str
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: str
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: str
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: str
    """Likes received on comments in viral distribution."""
    viral_comments: str
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: str
    """Clicks on the company page in viral distribution."""
    viral_document_completions: str
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: str
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: str
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: str
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: str
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: str
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: str
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: str
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: str
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: str
    """Fullscreen video plays in viral distribution."""
    viral_impressions: str
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: str
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: str
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: str
    """Clicks on landing page in viral distribution."""
    viral_likes: str
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: str
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: str
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: str
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: str
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: str
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: str
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: str
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: str
    """Total reactions in viral distribution of the ad."""
    viral_registrations: str
    """Total registrations in viral distribution of the ad."""
    viral_shares: str
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: str
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: str
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: str
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: str
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: str
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: str
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: str
    """Total views of videos in viral distribution of the ad."""
    pivot: str
    """Pivot dimension used for this analytics record"""
    sponsored_creative: str
    """Sponsored creative"""


class AdCreativeAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_creative_analytics search results."""
    action_clicks: AirbyteSortOrder
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: AirbyteSortOrder
    """The number of clicks on ad unit components."""
    approximate_member_reach: AirbyteSortOrder
    """An approximation of unique ad impressions."""
    card_clicks: AirbyteSortOrder
    """The number of clicks on interactive card elements."""
    card_impressions: AirbyteSortOrder
    """The number of times interactive cards were displayed."""
    clicks: AirbyteSortOrder
    """Total number of clicks on the ad."""
    comment_likes: AirbyteSortOrder
    """The count of likes on comments related to the ad."""
    comments: AirbyteSortOrder
    """The number of comments on the ad."""
    company_page_clicks: AirbyteSortOrder
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in the local currency."""
    cost_in_local_currency: AirbyteSortOrder
    """Cost of ad campaign in the local currency."""
    cost_in_usd: AirbyteSortOrder
    """Cost of ad campaign in USD."""
    document_completions: AirbyteSortOrder
    """Number of completions for document views."""
    document_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of document views."""
    document_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of document views."""
    document_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of document views."""
    download_clicks: AirbyteSortOrder
    """Clicks on download links in the ad."""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data."""
    external_website_conversions: AirbyteSortOrder
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites."""
    follows: AirbyteSortOrder
    """Number of follows generated by the ad."""
    full_screen_plays: AirbyteSortOrder
    """Number of times videos were played in fullscreen mode."""
    impressions: AirbyteSortOrder
    """Total number of times the ad was displayed."""
    job_applications: AirbyteSortOrder
    """Number of job applications initiated through the ad."""
    job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in the ad."""
    landing_page_clicks: AirbyteSortOrder
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: AirbyteSortOrder
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: AirbyteSortOrder
    """Clicks on expressing interest through lead generation mail."""
    likes: AirbyteSortOrder
    """Total likes received on the ad."""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of times lead forms were opened in one click."""
    one_click_leads: AirbyteSortOrder
    """Leads generated in one click."""
    opens: AirbyteSortOrder
    """The number of times the ad was opened or expanded."""
    other_engagements: AirbyteSortOrder
    """Engagements other than clicks on the ad."""
    pivot_values: AirbyteSortOrder
    """Values used for pivoting the analytics."""
    string_of_pivot_values: AirbyteSortOrder
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing the ad."""
    reactions: AirbyteSortOrder
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: AirbyteSortOrder
    """Total registrations completed through the ad."""
    sends: AirbyteSortOrder
    """Number of messages sent through the ad."""
    shares: AirbyteSortOrder
    """Total shares generated by the ad."""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data."""
    talent_leads: AirbyteSortOrder
    """Number of leads related to talent acquisition."""
    text_url_clicks: AirbyteSortOrder
    """Clicks on text URLs within the ad."""
    total_engagements: AirbyteSortOrder
    """Total number of engagements on the ad."""
    valid_work_email_leads: AirbyteSortOrder
    """Leads generated through valid work emails."""
    video_completions: AirbyteSortOrder
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of video views."""
    video_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of video views."""
    video_starts: AirbyteSortOrder
    """Total video starts initiated by users."""
    video_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of video views."""
    video_views: AirbyteSortOrder
    """Total views of videos in the ad."""
    viral_card_clicks: AirbyteSortOrder
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: AirbyteSortOrder
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: AirbyteSortOrder
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: AirbyteSortOrder
    """Likes received on comments in viral distribution."""
    viral_comments: AirbyteSortOrder
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: AirbyteSortOrder
    """Clicks on the company page in viral distribution."""
    viral_document_completions: AirbyteSortOrder
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: AirbyteSortOrder
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: AirbyteSortOrder
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: AirbyteSortOrder
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: AirbyteSortOrder
    """Fullscreen video plays in viral distribution."""
    viral_impressions: AirbyteSortOrder
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: AirbyteSortOrder
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: AirbyteSortOrder
    """Clicks on landing page in viral distribution."""
    viral_likes: AirbyteSortOrder
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: AirbyteSortOrder
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: AirbyteSortOrder
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: AirbyteSortOrder
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: AirbyteSortOrder
    """Total reactions in viral distribution of the ad."""
    viral_registrations: AirbyteSortOrder
    """Total registrations in viral distribution of the ad."""
    viral_shares: AirbyteSortOrder
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: AirbyteSortOrder
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: AirbyteSortOrder
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: AirbyteSortOrder
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: AirbyteSortOrder
    """Total views of videos in viral distribution of the ad."""
    pivot: AirbyteSortOrder
    """Pivot dimension used for this analytics record"""
    sponsored_creative: AirbyteSortOrder
    """Sponsored creative"""


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


class AdCreativeAnalyticsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AdCreativeAnalyticsStringFilter


class AdCreativeAnalyticsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AdCreativeAnalyticsStringFilter


class AdCreativeAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdCreativeAnalyticsStringFilter


class AdCreativeAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdCreativeAnalyticsStringFilter


class AdCreativeAnalyticsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | AdCreativeAnalyticsStartswithCondition
    | AdCreativeAnalyticsEndswithCondition
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


# ===== AD_IMPRESSION_DEVICE_ANALYTICS SEARCH TYPES =====

class AdImpressionDeviceAnalyticsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_impression_device_analytics search queries."""
    action_clicks: float | None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None
    """An approximation of unique ad impressions."""
    card_clicks: float | None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None
    """The number of times interactive cards were displayed."""
    clicks: float | None
    """Total number of clicks on the ad."""
    comment_likes: float | None
    """The count of likes on comments related to the ad."""
    comments: float | None
    """The number of comments on the ad."""
    company_page_clicks: float | None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None
    """Cost of ad campaign in USD."""
    document_completions: float | None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None
    """Completions for third quartile of document views."""
    download_clicks: float | None
    """Clicks on download links in the ad."""
    end_date: str | None
    """End date of the ad analytics data."""
    external_website_conversions: float | None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites."""
    follows: float | None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None
    """Total number of times the ad was displayed."""
    job_applications: float | None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None
    """Leads generated in one click."""
    opens: float | None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None
    """Registrations completed post-viewing the ad."""
    reactions: float | None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None
    """Total registrations completed through the ad."""
    sends: float | None
    """Number of messages sent through the ad."""
    shares: float | None
    """Total shares generated by the ad."""
    start_date: str | None
    """Start date of the ad analytics data."""
    talent_leads: float | None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None
    """Leads generated through valid work emails."""
    video_completions: float | None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None
    """Completions for midpoint of video views."""
    video_starts: float | None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None
    """Completions for third quartile of video views."""
    video_views: float | None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdImpressionDeviceAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    action_clicks: list[float]
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: list[float]
    """The number of clicks on ad unit components."""
    approximate_member_reach: list[float]
    """An approximation of unique ad impressions."""
    card_clicks: list[float]
    """The number of clicks on interactive card elements."""
    card_impressions: list[float]
    """The number of times interactive cards were displayed."""
    clicks: list[float]
    """Total number of clicks on the ad."""
    comment_likes: list[float]
    """The count of likes on comments related to the ad."""
    comments: list[float]
    """The number of comments on the ad."""
    company_page_clicks: list[float]
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: list[float]
    """Conversion value in the local currency."""
    cost_in_local_currency: list[float]
    """Cost of ad campaign in the local currency."""
    cost_in_usd: list[float]
    """Cost of ad campaign in USD."""
    document_completions: list[float]
    """Number of completions for document views."""
    document_first_quartile_completions: list[float]
    """Completions for first quartile of document views."""
    document_midpoint_completions: list[float]
    """Completions for midpoint of document views."""
    document_third_quartile_completions: list[float]
    """Completions for third quartile of document views."""
    download_clicks: list[float]
    """Clicks on download links in the ad."""
    end_date: list[str]
    """End date of the ad analytics data."""
    external_website_conversions: list[float]
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites."""
    follows: list[float]
    """Number of follows generated by the ad."""
    full_screen_plays: list[float]
    """Number of times videos were played in fullscreen mode."""
    impressions: list[float]
    """Total number of times the ad was displayed."""
    job_applications: list[float]
    """Number of job applications initiated through the ad."""
    job_apply_clicks: list[float]
    """Clicks on apply job button in the ad."""
    landing_page_clicks: list[float]
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: list[float]
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: list[float]
    """Clicks on expressing interest through lead generation mail."""
    likes: list[float]
    """Total likes received on the ad."""
    one_click_lead_form_opens: list[float]
    """Number of times lead forms were opened in one click."""
    one_click_leads: list[float]
    """Leads generated in one click."""
    opens: list[float]
    """The number of times the ad was opened or expanded."""
    other_engagements: list[float]
    """Engagements other than clicks on the ad."""
    pivot_values: list[list[Any]]
    """Values used for pivoting the analytics."""
    string_of_pivot_values: list[str]
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: list[float]
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: list[float]
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: list[float]
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: list[float]
    """Registrations completed post-viewing the ad."""
    reactions: list[float]
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: list[float]
    """Total registrations completed through the ad."""
    sends: list[float]
    """Number of messages sent through the ad."""
    shares: list[float]
    """Total shares generated by the ad."""
    start_date: list[str]
    """Start date of the ad analytics data."""
    talent_leads: list[float]
    """Number of leads related to talent acquisition."""
    text_url_clicks: list[float]
    """Clicks on text URLs within the ad."""
    total_engagements: list[float]
    """Total number of engagements on the ad."""
    valid_work_email_leads: list[float]
    """Leads generated through valid work emails."""
    video_completions: list[float]
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: list[float]
    """Completions for first quartile of video views."""
    video_midpoint_completions: list[float]
    """Completions for midpoint of video views."""
    video_starts: list[float]
    """Total video starts initiated by users."""
    video_third_quartile_completions: list[float]
    """Completions for third quartile of video views."""
    video_views: list[float]
    """Total views of videos in the ad."""
    viral_card_clicks: list[float]
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: list[float]
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: list[float]
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: list[float]
    """Likes received on comments in viral distribution."""
    viral_comments: list[float]
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: list[float]
    """Clicks on the company page in viral distribution."""
    viral_document_completions: list[float]
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: list[float]
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: list[float]
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: list[float]
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: list[float]
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: list[float]
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: list[float]
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: list[float]
    """Fullscreen video plays in viral distribution."""
    viral_impressions: list[float]
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: list[float]
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: list[float]
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: list[float]
    """Clicks on landing page in viral distribution."""
    viral_likes: list[float]
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: list[float]
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: list[float]
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: list[float]
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: list[float]
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: list[float]
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: list[float]
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: list[float]
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: list[float]
    """Total reactions in viral distribution of the ad."""
    viral_registrations: list[float]
    """Total registrations in viral distribution of the ad."""
    viral_shares: list[float]
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: list[float]
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: list[float]
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: list[float]
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: list[float]
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: list[float]
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: list[float]
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: list[float]
    """Total views of videos in viral distribution of the ad."""
    pivot: list[str]
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: list[str]
    """URN of the sponsored campaign this analytics record belongs to"""


class AdImpressionDeviceAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    action_clicks: Any
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: Any
    """The number of clicks on ad unit components."""
    approximate_member_reach: Any
    """An approximation of unique ad impressions."""
    card_clicks: Any
    """The number of clicks on interactive card elements."""
    card_impressions: Any
    """The number of times interactive cards were displayed."""
    clicks: Any
    """Total number of clicks on the ad."""
    comment_likes: Any
    """The count of likes on comments related to the ad."""
    comments: Any
    """The number of comments on the ad."""
    company_page_clicks: Any
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: Any
    """Conversion value in the local currency."""
    cost_in_local_currency: Any
    """Cost of ad campaign in the local currency."""
    cost_in_usd: Any
    """Cost of ad campaign in USD."""
    document_completions: Any
    """Number of completions for document views."""
    document_first_quartile_completions: Any
    """Completions for first quartile of document views."""
    document_midpoint_completions: Any
    """Completions for midpoint of document views."""
    document_third_quartile_completions: Any
    """Completions for third quartile of document views."""
    download_clicks: Any
    """Clicks on download links in the ad."""
    end_date: Any
    """End date of the ad analytics data."""
    external_website_conversions: Any
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites."""
    follows: Any
    """Number of follows generated by the ad."""
    full_screen_plays: Any
    """Number of times videos were played in fullscreen mode."""
    impressions: Any
    """Total number of times the ad was displayed."""
    job_applications: Any
    """Number of job applications initiated through the ad."""
    job_apply_clicks: Any
    """Clicks on apply job button in the ad."""
    landing_page_clicks: Any
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: Any
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: Any
    """Clicks on expressing interest through lead generation mail."""
    likes: Any
    """Total likes received on the ad."""
    one_click_lead_form_opens: Any
    """Number of times lead forms were opened in one click."""
    one_click_leads: Any
    """Leads generated in one click."""
    opens: Any
    """The number of times the ad was opened or expanded."""
    other_engagements: Any
    """Engagements other than clicks on the ad."""
    pivot_values: Any
    """Values used for pivoting the analytics."""
    string_of_pivot_values: Any
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: Any
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: Any
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: Any
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: Any
    """Registrations completed post-viewing the ad."""
    reactions: Any
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: Any
    """Total registrations completed through the ad."""
    sends: Any
    """Number of messages sent through the ad."""
    shares: Any
    """Total shares generated by the ad."""
    start_date: Any
    """Start date of the ad analytics data."""
    talent_leads: Any
    """Number of leads related to talent acquisition."""
    text_url_clicks: Any
    """Clicks on text URLs within the ad."""
    total_engagements: Any
    """Total number of engagements on the ad."""
    valid_work_email_leads: Any
    """Leads generated through valid work emails."""
    video_completions: Any
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: Any
    """Completions for first quartile of video views."""
    video_midpoint_completions: Any
    """Completions for midpoint of video views."""
    video_starts: Any
    """Total video starts initiated by users."""
    video_third_quartile_completions: Any
    """Completions for third quartile of video views."""
    video_views: Any
    """Total views of videos in the ad."""
    viral_card_clicks: Any
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: Any
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: Any
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: Any
    """Likes received on comments in viral distribution."""
    viral_comments: Any
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: Any
    """Clicks on the company page in viral distribution."""
    viral_document_completions: Any
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: Any
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: Any
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: Any
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: Any
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: Any
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: Any
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: Any
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: Any
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: Any
    """Fullscreen video plays in viral distribution."""
    viral_impressions: Any
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: Any
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: Any
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: Any
    """Clicks on landing page in viral distribution."""
    viral_likes: Any
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: Any
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: Any
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: Any
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: Any
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: Any
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: Any
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: Any
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: Any
    """Total reactions in viral distribution of the ad."""
    viral_registrations: Any
    """Total registrations in viral distribution of the ad."""
    viral_shares: Any
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: Any
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: Any
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: Any
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: Any
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: Any
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: Any
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: Any
    """Total views of videos in viral distribution of the ad."""
    pivot: Any
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: Any
    """URN of the sponsored campaign this analytics record belongs to"""


class AdImpressionDeviceAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    action_clicks: str
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: str
    """The number of clicks on ad unit components."""
    approximate_member_reach: str
    """An approximation of unique ad impressions."""
    card_clicks: str
    """The number of clicks on interactive card elements."""
    card_impressions: str
    """The number of times interactive cards were displayed."""
    clicks: str
    """Total number of clicks on the ad."""
    comment_likes: str
    """The count of likes on comments related to the ad."""
    comments: str
    """The number of comments on the ad."""
    company_page_clicks: str
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: str
    """Conversion value in the local currency."""
    cost_in_local_currency: str
    """Cost of ad campaign in the local currency."""
    cost_in_usd: str
    """Cost of ad campaign in USD."""
    document_completions: str
    """Number of completions for document views."""
    document_first_quartile_completions: str
    """Completions for first quartile of document views."""
    document_midpoint_completions: str
    """Completions for midpoint of document views."""
    document_third_quartile_completions: str
    """Completions for third quartile of document views."""
    download_clicks: str
    """Clicks on download links in the ad."""
    end_date: str
    """End date of the ad analytics data."""
    external_website_conversions: str
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites."""
    follows: str
    """Number of follows generated by the ad."""
    full_screen_plays: str
    """Number of times videos were played in fullscreen mode."""
    impressions: str
    """Total number of times the ad was displayed."""
    job_applications: str
    """Number of job applications initiated through the ad."""
    job_apply_clicks: str
    """Clicks on apply job button in the ad."""
    landing_page_clicks: str
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: str
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: str
    """Clicks on expressing interest through lead generation mail."""
    likes: str
    """Total likes received on the ad."""
    one_click_lead_form_opens: str
    """Number of times lead forms were opened in one click."""
    one_click_leads: str
    """Leads generated in one click."""
    opens: str
    """The number of times the ad was opened or expanded."""
    other_engagements: str
    """Engagements other than clicks on the ad."""
    pivot_values: str
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: str
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: str
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: str
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: str
    """Registrations completed post-viewing the ad."""
    reactions: str
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: str
    """Total registrations completed through the ad."""
    sends: str
    """Number of messages sent through the ad."""
    shares: str
    """Total shares generated by the ad."""
    start_date: str
    """Start date of the ad analytics data."""
    talent_leads: str
    """Number of leads related to talent acquisition."""
    text_url_clicks: str
    """Clicks on text URLs within the ad."""
    total_engagements: str
    """Total number of engagements on the ad."""
    valid_work_email_leads: str
    """Leads generated through valid work emails."""
    video_completions: str
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: str
    """Completions for first quartile of video views."""
    video_midpoint_completions: str
    """Completions for midpoint of video views."""
    video_starts: str
    """Total video starts initiated by users."""
    video_third_quartile_completions: str
    """Completions for third quartile of video views."""
    video_views: str
    """Total views of videos in the ad."""
    viral_card_clicks: str
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: str
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: str
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: str
    """Likes received on comments in viral distribution."""
    viral_comments: str
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: str
    """Clicks on the company page in viral distribution."""
    viral_document_completions: str
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: str
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: str
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: str
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: str
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: str
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: str
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: str
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: str
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: str
    """Fullscreen video plays in viral distribution."""
    viral_impressions: str
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: str
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: str
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: str
    """Clicks on landing page in viral distribution."""
    viral_likes: str
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: str
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: str
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: str
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: str
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: str
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: str
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: str
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: str
    """Total reactions in viral distribution of the ad."""
    viral_registrations: str
    """Total registrations in viral distribution of the ad."""
    viral_shares: str
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: str
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: str
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: str
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: str
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: str
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: str
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: str
    """Total views of videos in viral distribution of the ad."""
    pivot: str
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str
    """URN of the sponsored campaign this analytics record belongs to"""


class AdImpressionDeviceAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_impression_device_analytics search results."""
    action_clicks: AirbyteSortOrder
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: AirbyteSortOrder
    """The number of clicks on ad unit components."""
    approximate_member_reach: AirbyteSortOrder
    """An approximation of unique ad impressions."""
    card_clicks: AirbyteSortOrder
    """The number of clicks on interactive card elements."""
    card_impressions: AirbyteSortOrder
    """The number of times interactive cards were displayed."""
    clicks: AirbyteSortOrder
    """Total number of clicks on the ad."""
    comment_likes: AirbyteSortOrder
    """The count of likes on comments related to the ad."""
    comments: AirbyteSortOrder
    """The number of comments on the ad."""
    company_page_clicks: AirbyteSortOrder
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in the local currency."""
    cost_in_local_currency: AirbyteSortOrder
    """Cost of ad campaign in the local currency."""
    cost_in_usd: AirbyteSortOrder
    """Cost of ad campaign in USD."""
    document_completions: AirbyteSortOrder
    """Number of completions for document views."""
    document_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of document views."""
    document_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of document views."""
    document_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of document views."""
    download_clicks: AirbyteSortOrder
    """Clicks on download links in the ad."""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data."""
    external_website_conversions: AirbyteSortOrder
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites."""
    follows: AirbyteSortOrder
    """Number of follows generated by the ad."""
    full_screen_plays: AirbyteSortOrder
    """Number of times videos were played in fullscreen mode."""
    impressions: AirbyteSortOrder
    """Total number of times the ad was displayed."""
    job_applications: AirbyteSortOrder
    """Number of job applications initiated through the ad."""
    job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in the ad."""
    landing_page_clicks: AirbyteSortOrder
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: AirbyteSortOrder
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: AirbyteSortOrder
    """Clicks on expressing interest through lead generation mail."""
    likes: AirbyteSortOrder
    """Total likes received on the ad."""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of times lead forms were opened in one click."""
    one_click_leads: AirbyteSortOrder
    """Leads generated in one click."""
    opens: AirbyteSortOrder
    """The number of times the ad was opened or expanded."""
    other_engagements: AirbyteSortOrder
    """Engagements other than clicks on the ad."""
    pivot_values: AirbyteSortOrder
    """Values used for pivoting the analytics."""
    string_of_pivot_values: AirbyteSortOrder
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing the ad."""
    reactions: AirbyteSortOrder
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: AirbyteSortOrder
    """Total registrations completed through the ad."""
    sends: AirbyteSortOrder
    """Number of messages sent through the ad."""
    shares: AirbyteSortOrder
    """Total shares generated by the ad."""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data."""
    talent_leads: AirbyteSortOrder
    """Number of leads related to talent acquisition."""
    text_url_clicks: AirbyteSortOrder
    """Clicks on text URLs within the ad."""
    total_engagements: AirbyteSortOrder
    """Total number of engagements on the ad."""
    valid_work_email_leads: AirbyteSortOrder
    """Leads generated through valid work emails."""
    video_completions: AirbyteSortOrder
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of video views."""
    video_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of video views."""
    video_starts: AirbyteSortOrder
    """Total video starts initiated by users."""
    video_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of video views."""
    video_views: AirbyteSortOrder
    """Total views of videos in the ad."""
    viral_card_clicks: AirbyteSortOrder
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: AirbyteSortOrder
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: AirbyteSortOrder
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: AirbyteSortOrder
    """Likes received on comments in viral distribution."""
    viral_comments: AirbyteSortOrder
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: AirbyteSortOrder
    """Clicks on the company page in viral distribution."""
    viral_document_completions: AirbyteSortOrder
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: AirbyteSortOrder
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: AirbyteSortOrder
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: AirbyteSortOrder
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: AirbyteSortOrder
    """Fullscreen video plays in viral distribution."""
    viral_impressions: AirbyteSortOrder
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: AirbyteSortOrder
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: AirbyteSortOrder
    """Clicks on landing page in viral distribution."""
    viral_likes: AirbyteSortOrder
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: AirbyteSortOrder
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: AirbyteSortOrder
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: AirbyteSortOrder
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: AirbyteSortOrder
    """Total reactions in viral distribution of the ad."""
    viral_registrations: AirbyteSortOrder
    """Total registrations in viral distribution of the ad."""
    viral_shares: AirbyteSortOrder
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: AirbyteSortOrder
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: AirbyteSortOrder
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: AirbyteSortOrder
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: AirbyteSortOrder
    """Total views of videos in viral distribution of the ad."""
    pivot: AirbyteSortOrder
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: AirbyteSortOrder
    """URN of the sponsored campaign this analytics record belongs to"""


# Entity-specific condition types for ad_impression_device_analytics
class AdImpressionDeviceAnalyticsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdImpressionDeviceAnalyticsSearchFilter


class AdImpressionDeviceAnalyticsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdImpressionDeviceAnalyticsSearchFilter


class AdImpressionDeviceAnalyticsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdImpressionDeviceAnalyticsSearchFilter


class AdImpressionDeviceAnalyticsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdImpressionDeviceAnalyticsSearchFilter


class AdImpressionDeviceAnalyticsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdImpressionDeviceAnalyticsSearchFilter


class AdImpressionDeviceAnalyticsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdImpressionDeviceAnalyticsSearchFilter


class AdImpressionDeviceAnalyticsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AdImpressionDeviceAnalyticsStringFilter


class AdImpressionDeviceAnalyticsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AdImpressionDeviceAnalyticsStringFilter


class AdImpressionDeviceAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdImpressionDeviceAnalyticsStringFilter


class AdImpressionDeviceAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdImpressionDeviceAnalyticsStringFilter


class AdImpressionDeviceAnalyticsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: AdImpressionDeviceAnalyticsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdImpressionDeviceAnalyticsInCondition = TypedDict("AdImpressionDeviceAnalyticsInCondition", {"in": AdImpressionDeviceAnalyticsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdImpressionDeviceAnalyticsNotCondition = TypedDict("AdImpressionDeviceAnalyticsNotCondition", {"not": "AdImpressionDeviceAnalyticsCondition"}, total=False)
"""Negates the nested condition."""

AdImpressionDeviceAnalyticsAndCondition = TypedDict("AdImpressionDeviceAnalyticsAndCondition", {"and": "list[AdImpressionDeviceAnalyticsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdImpressionDeviceAnalyticsOrCondition = TypedDict("AdImpressionDeviceAnalyticsOrCondition", {"or": "list[AdImpressionDeviceAnalyticsCondition]"}, total=False)
"""True if any nested condition is true."""

AdImpressionDeviceAnalyticsAnyCondition = TypedDict("AdImpressionDeviceAnalyticsAnyCondition", {"any": AdImpressionDeviceAnalyticsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_impression_device_analytics condition types
AdImpressionDeviceAnalyticsCondition = (
    AdImpressionDeviceAnalyticsEqCondition
    | AdImpressionDeviceAnalyticsNeqCondition
    | AdImpressionDeviceAnalyticsGtCondition
    | AdImpressionDeviceAnalyticsGteCondition
    | AdImpressionDeviceAnalyticsLtCondition
    | AdImpressionDeviceAnalyticsLteCondition
    | AdImpressionDeviceAnalyticsInCondition
    | AdImpressionDeviceAnalyticsStartswithCondition
    | AdImpressionDeviceAnalyticsEndswithCondition
    | AdImpressionDeviceAnalyticsFuzzyCondition
    | AdImpressionDeviceAnalyticsKeywordCondition
    | AdImpressionDeviceAnalyticsContainsCondition
    | AdImpressionDeviceAnalyticsNotCondition
    | AdImpressionDeviceAnalyticsAndCondition
    | AdImpressionDeviceAnalyticsOrCondition
    | AdImpressionDeviceAnalyticsAnyCondition
)


class AdImpressionDeviceAnalyticsSearchQuery(TypedDict, total=False):
    """Search query for ad_impression_device_analytics entity."""
    filter: AdImpressionDeviceAnalyticsCondition
    sort: list[AdImpressionDeviceAnalyticsSortFilter]


# ===== AD_MEMBER_COMPANY_ANALYTICS SEARCH TYPES =====

class AdMemberCompanyAnalyticsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_member_company_analytics search queries."""
    action_clicks: float | None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None
    """An approximation of unique ad impressions."""
    card_clicks: float | None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None
    """The number of times interactive cards were displayed."""
    clicks: float | None
    """Total number of clicks on the ad."""
    comment_likes: float | None
    """The count of likes on comments related to the ad."""
    comments: float | None
    """The number of comments on the ad."""
    company_page_clicks: float | None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None
    """Cost of ad campaign in USD."""
    document_completions: float | None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None
    """Completions for third quartile of document views."""
    download_clicks: float | None
    """Clicks on download links in the ad."""
    end_date: str | None
    """End date of the ad analytics data."""
    external_website_conversions: float | None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites."""
    follows: float | None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None
    """Total number of times the ad was displayed."""
    job_applications: float | None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None
    """Leads generated in one click."""
    opens: float | None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None
    """Registrations completed post-viewing the ad."""
    reactions: float | None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None
    """Total registrations completed through the ad."""
    sends: float | None
    """Number of messages sent through the ad."""
    shares: float | None
    """Total shares generated by the ad."""
    start_date: str | None
    """Start date of the ad analytics data."""
    talent_leads: float | None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None
    """Leads generated through valid work emails."""
    video_completions: float | None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None
    """Completions for midpoint of video views."""
    video_starts: float | None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None
    """Completions for third quartile of video views."""
    video_views: float | None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCompanyAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    action_clicks: list[float]
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: list[float]
    """The number of clicks on ad unit components."""
    approximate_member_reach: list[float]
    """An approximation of unique ad impressions."""
    card_clicks: list[float]
    """The number of clicks on interactive card elements."""
    card_impressions: list[float]
    """The number of times interactive cards were displayed."""
    clicks: list[float]
    """Total number of clicks on the ad."""
    comment_likes: list[float]
    """The count of likes on comments related to the ad."""
    comments: list[float]
    """The number of comments on the ad."""
    company_page_clicks: list[float]
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: list[float]
    """Conversion value in the local currency."""
    cost_in_local_currency: list[float]
    """Cost of ad campaign in the local currency."""
    cost_in_usd: list[float]
    """Cost of ad campaign in USD."""
    document_completions: list[float]
    """Number of completions for document views."""
    document_first_quartile_completions: list[float]
    """Completions for first quartile of document views."""
    document_midpoint_completions: list[float]
    """Completions for midpoint of document views."""
    document_third_quartile_completions: list[float]
    """Completions for third quartile of document views."""
    download_clicks: list[float]
    """Clicks on download links in the ad."""
    end_date: list[str]
    """End date of the ad analytics data."""
    external_website_conversions: list[float]
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites."""
    follows: list[float]
    """Number of follows generated by the ad."""
    full_screen_plays: list[float]
    """Number of times videos were played in fullscreen mode."""
    impressions: list[float]
    """Total number of times the ad was displayed."""
    job_applications: list[float]
    """Number of job applications initiated through the ad."""
    job_apply_clicks: list[float]
    """Clicks on apply job button in the ad."""
    landing_page_clicks: list[float]
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: list[float]
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: list[float]
    """Clicks on expressing interest through lead generation mail."""
    likes: list[float]
    """Total likes received on the ad."""
    one_click_lead_form_opens: list[float]
    """Number of times lead forms were opened in one click."""
    one_click_leads: list[float]
    """Leads generated in one click."""
    opens: list[float]
    """The number of times the ad was opened or expanded."""
    other_engagements: list[float]
    """Engagements other than clicks on the ad."""
    pivot_values: list[list[Any]]
    """Values used for pivoting the analytics."""
    string_of_pivot_values: list[str]
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: list[float]
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: list[float]
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: list[float]
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: list[float]
    """Registrations completed post-viewing the ad."""
    reactions: list[float]
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: list[float]
    """Total registrations completed through the ad."""
    sends: list[float]
    """Number of messages sent through the ad."""
    shares: list[float]
    """Total shares generated by the ad."""
    start_date: list[str]
    """Start date of the ad analytics data."""
    talent_leads: list[float]
    """Number of leads related to talent acquisition."""
    text_url_clicks: list[float]
    """Clicks on text URLs within the ad."""
    total_engagements: list[float]
    """Total number of engagements on the ad."""
    valid_work_email_leads: list[float]
    """Leads generated through valid work emails."""
    video_completions: list[float]
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: list[float]
    """Completions for first quartile of video views."""
    video_midpoint_completions: list[float]
    """Completions for midpoint of video views."""
    video_starts: list[float]
    """Total video starts initiated by users."""
    video_third_quartile_completions: list[float]
    """Completions for third quartile of video views."""
    video_views: list[float]
    """Total views of videos in the ad."""
    viral_card_clicks: list[float]
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: list[float]
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: list[float]
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: list[float]
    """Likes received on comments in viral distribution."""
    viral_comments: list[float]
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: list[float]
    """Clicks on the company page in viral distribution."""
    viral_document_completions: list[float]
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: list[float]
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: list[float]
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: list[float]
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: list[float]
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: list[float]
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: list[float]
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: list[float]
    """Fullscreen video plays in viral distribution."""
    viral_impressions: list[float]
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: list[float]
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: list[float]
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: list[float]
    """Clicks on landing page in viral distribution."""
    viral_likes: list[float]
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: list[float]
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: list[float]
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: list[float]
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: list[float]
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: list[float]
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: list[float]
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: list[float]
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: list[float]
    """Total reactions in viral distribution of the ad."""
    viral_registrations: list[float]
    """Total registrations in viral distribution of the ad."""
    viral_shares: list[float]
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: list[float]
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: list[float]
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: list[float]
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: list[float]
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: list[float]
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: list[float]
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: list[float]
    """Total views of videos in viral distribution of the ad."""
    pivot: list[str]
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: list[str]
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCompanyAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    action_clicks: Any
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: Any
    """The number of clicks on ad unit components."""
    approximate_member_reach: Any
    """An approximation of unique ad impressions."""
    card_clicks: Any
    """The number of clicks on interactive card elements."""
    card_impressions: Any
    """The number of times interactive cards were displayed."""
    clicks: Any
    """Total number of clicks on the ad."""
    comment_likes: Any
    """The count of likes on comments related to the ad."""
    comments: Any
    """The number of comments on the ad."""
    company_page_clicks: Any
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: Any
    """Conversion value in the local currency."""
    cost_in_local_currency: Any
    """Cost of ad campaign in the local currency."""
    cost_in_usd: Any
    """Cost of ad campaign in USD."""
    document_completions: Any
    """Number of completions for document views."""
    document_first_quartile_completions: Any
    """Completions for first quartile of document views."""
    document_midpoint_completions: Any
    """Completions for midpoint of document views."""
    document_third_quartile_completions: Any
    """Completions for third quartile of document views."""
    download_clicks: Any
    """Clicks on download links in the ad."""
    end_date: Any
    """End date of the ad analytics data."""
    external_website_conversions: Any
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites."""
    follows: Any
    """Number of follows generated by the ad."""
    full_screen_plays: Any
    """Number of times videos were played in fullscreen mode."""
    impressions: Any
    """Total number of times the ad was displayed."""
    job_applications: Any
    """Number of job applications initiated through the ad."""
    job_apply_clicks: Any
    """Clicks on apply job button in the ad."""
    landing_page_clicks: Any
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: Any
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: Any
    """Clicks on expressing interest through lead generation mail."""
    likes: Any
    """Total likes received on the ad."""
    one_click_lead_form_opens: Any
    """Number of times lead forms were opened in one click."""
    one_click_leads: Any
    """Leads generated in one click."""
    opens: Any
    """The number of times the ad was opened or expanded."""
    other_engagements: Any
    """Engagements other than clicks on the ad."""
    pivot_values: Any
    """Values used for pivoting the analytics."""
    string_of_pivot_values: Any
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: Any
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: Any
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: Any
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: Any
    """Registrations completed post-viewing the ad."""
    reactions: Any
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: Any
    """Total registrations completed through the ad."""
    sends: Any
    """Number of messages sent through the ad."""
    shares: Any
    """Total shares generated by the ad."""
    start_date: Any
    """Start date of the ad analytics data."""
    talent_leads: Any
    """Number of leads related to talent acquisition."""
    text_url_clicks: Any
    """Clicks on text URLs within the ad."""
    total_engagements: Any
    """Total number of engagements on the ad."""
    valid_work_email_leads: Any
    """Leads generated through valid work emails."""
    video_completions: Any
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: Any
    """Completions for first quartile of video views."""
    video_midpoint_completions: Any
    """Completions for midpoint of video views."""
    video_starts: Any
    """Total video starts initiated by users."""
    video_third_quartile_completions: Any
    """Completions for third quartile of video views."""
    video_views: Any
    """Total views of videos in the ad."""
    viral_card_clicks: Any
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: Any
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: Any
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: Any
    """Likes received on comments in viral distribution."""
    viral_comments: Any
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: Any
    """Clicks on the company page in viral distribution."""
    viral_document_completions: Any
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: Any
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: Any
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: Any
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: Any
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: Any
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: Any
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: Any
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: Any
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: Any
    """Fullscreen video plays in viral distribution."""
    viral_impressions: Any
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: Any
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: Any
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: Any
    """Clicks on landing page in viral distribution."""
    viral_likes: Any
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: Any
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: Any
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: Any
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: Any
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: Any
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: Any
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: Any
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: Any
    """Total reactions in viral distribution of the ad."""
    viral_registrations: Any
    """Total registrations in viral distribution of the ad."""
    viral_shares: Any
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: Any
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: Any
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: Any
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: Any
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: Any
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: Any
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: Any
    """Total views of videos in viral distribution of the ad."""
    pivot: Any
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: Any
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCompanyAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    action_clicks: str
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: str
    """The number of clicks on ad unit components."""
    approximate_member_reach: str
    """An approximation of unique ad impressions."""
    card_clicks: str
    """The number of clicks on interactive card elements."""
    card_impressions: str
    """The number of times interactive cards were displayed."""
    clicks: str
    """Total number of clicks on the ad."""
    comment_likes: str
    """The count of likes on comments related to the ad."""
    comments: str
    """The number of comments on the ad."""
    company_page_clicks: str
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: str
    """Conversion value in the local currency."""
    cost_in_local_currency: str
    """Cost of ad campaign in the local currency."""
    cost_in_usd: str
    """Cost of ad campaign in USD."""
    document_completions: str
    """Number of completions for document views."""
    document_first_quartile_completions: str
    """Completions for first quartile of document views."""
    document_midpoint_completions: str
    """Completions for midpoint of document views."""
    document_third_quartile_completions: str
    """Completions for third quartile of document views."""
    download_clicks: str
    """Clicks on download links in the ad."""
    end_date: str
    """End date of the ad analytics data."""
    external_website_conversions: str
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites."""
    follows: str
    """Number of follows generated by the ad."""
    full_screen_plays: str
    """Number of times videos were played in fullscreen mode."""
    impressions: str
    """Total number of times the ad was displayed."""
    job_applications: str
    """Number of job applications initiated through the ad."""
    job_apply_clicks: str
    """Clicks on apply job button in the ad."""
    landing_page_clicks: str
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: str
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: str
    """Clicks on expressing interest through lead generation mail."""
    likes: str
    """Total likes received on the ad."""
    one_click_lead_form_opens: str
    """Number of times lead forms were opened in one click."""
    one_click_leads: str
    """Leads generated in one click."""
    opens: str
    """The number of times the ad was opened or expanded."""
    other_engagements: str
    """Engagements other than clicks on the ad."""
    pivot_values: str
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: str
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: str
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: str
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: str
    """Registrations completed post-viewing the ad."""
    reactions: str
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: str
    """Total registrations completed through the ad."""
    sends: str
    """Number of messages sent through the ad."""
    shares: str
    """Total shares generated by the ad."""
    start_date: str
    """Start date of the ad analytics data."""
    talent_leads: str
    """Number of leads related to talent acquisition."""
    text_url_clicks: str
    """Clicks on text URLs within the ad."""
    total_engagements: str
    """Total number of engagements on the ad."""
    valid_work_email_leads: str
    """Leads generated through valid work emails."""
    video_completions: str
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: str
    """Completions for first quartile of video views."""
    video_midpoint_completions: str
    """Completions for midpoint of video views."""
    video_starts: str
    """Total video starts initiated by users."""
    video_third_quartile_completions: str
    """Completions for third quartile of video views."""
    video_views: str
    """Total views of videos in the ad."""
    viral_card_clicks: str
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: str
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: str
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: str
    """Likes received on comments in viral distribution."""
    viral_comments: str
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: str
    """Clicks on the company page in viral distribution."""
    viral_document_completions: str
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: str
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: str
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: str
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: str
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: str
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: str
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: str
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: str
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: str
    """Fullscreen video plays in viral distribution."""
    viral_impressions: str
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: str
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: str
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: str
    """Clicks on landing page in viral distribution."""
    viral_likes: str
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: str
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: str
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: str
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: str
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: str
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: str
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: str
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: str
    """Total reactions in viral distribution of the ad."""
    viral_registrations: str
    """Total registrations in viral distribution of the ad."""
    viral_shares: str
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: str
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: str
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: str
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: str
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: str
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: str
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: str
    """Total views of videos in viral distribution of the ad."""
    pivot: str
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCompanyAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_member_company_analytics search results."""
    action_clicks: AirbyteSortOrder
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: AirbyteSortOrder
    """The number of clicks on ad unit components."""
    approximate_member_reach: AirbyteSortOrder
    """An approximation of unique ad impressions."""
    card_clicks: AirbyteSortOrder
    """The number of clicks on interactive card elements."""
    card_impressions: AirbyteSortOrder
    """The number of times interactive cards were displayed."""
    clicks: AirbyteSortOrder
    """Total number of clicks on the ad."""
    comment_likes: AirbyteSortOrder
    """The count of likes on comments related to the ad."""
    comments: AirbyteSortOrder
    """The number of comments on the ad."""
    company_page_clicks: AirbyteSortOrder
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in the local currency."""
    cost_in_local_currency: AirbyteSortOrder
    """Cost of ad campaign in the local currency."""
    cost_in_usd: AirbyteSortOrder
    """Cost of ad campaign in USD."""
    document_completions: AirbyteSortOrder
    """Number of completions for document views."""
    document_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of document views."""
    document_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of document views."""
    document_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of document views."""
    download_clicks: AirbyteSortOrder
    """Clicks on download links in the ad."""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data."""
    external_website_conversions: AirbyteSortOrder
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites."""
    follows: AirbyteSortOrder
    """Number of follows generated by the ad."""
    full_screen_plays: AirbyteSortOrder
    """Number of times videos were played in fullscreen mode."""
    impressions: AirbyteSortOrder
    """Total number of times the ad was displayed."""
    job_applications: AirbyteSortOrder
    """Number of job applications initiated through the ad."""
    job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in the ad."""
    landing_page_clicks: AirbyteSortOrder
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: AirbyteSortOrder
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: AirbyteSortOrder
    """Clicks on expressing interest through lead generation mail."""
    likes: AirbyteSortOrder
    """Total likes received on the ad."""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of times lead forms were opened in one click."""
    one_click_leads: AirbyteSortOrder
    """Leads generated in one click."""
    opens: AirbyteSortOrder
    """The number of times the ad was opened or expanded."""
    other_engagements: AirbyteSortOrder
    """Engagements other than clicks on the ad."""
    pivot_values: AirbyteSortOrder
    """Values used for pivoting the analytics."""
    string_of_pivot_values: AirbyteSortOrder
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing the ad."""
    reactions: AirbyteSortOrder
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: AirbyteSortOrder
    """Total registrations completed through the ad."""
    sends: AirbyteSortOrder
    """Number of messages sent through the ad."""
    shares: AirbyteSortOrder
    """Total shares generated by the ad."""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data."""
    talent_leads: AirbyteSortOrder
    """Number of leads related to talent acquisition."""
    text_url_clicks: AirbyteSortOrder
    """Clicks on text URLs within the ad."""
    total_engagements: AirbyteSortOrder
    """Total number of engagements on the ad."""
    valid_work_email_leads: AirbyteSortOrder
    """Leads generated through valid work emails."""
    video_completions: AirbyteSortOrder
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of video views."""
    video_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of video views."""
    video_starts: AirbyteSortOrder
    """Total video starts initiated by users."""
    video_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of video views."""
    video_views: AirbyteSortOrder
    """Total views of videos in the ad."""
    viral_card_clicks: AirbyteSortOrder
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: AirbyteSortOrder
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: AirbyteSortOrder
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: AirbyteSortOrder
    """Likes received on comments in viral distribution."""
    viral_comments: AirbyteSortOrder
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: AirbyteSortOrder
    """Clicks on the company page in viral distribution."""
    viral_document_completions: AirbyteSortOrder
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: AirbyteSortOrder
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: AirbyteSortOrder
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: AirbyteSortOrder
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: AirbyteSortOrder
    """Fullscreen video plays in viral distribution."""
    viral_impressions: AirbyteSortOrder
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: AirbyteSortOrder
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: AirbyteSortOrder
    """Clicks on landing page in viral distribution."""
    viral_likes: AirbyteSortOrder
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: AirbyteSortOrder
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: AirbyteSortOrder
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: AirbyteSortOrder
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: AirbyteSortOrder
    """Total reactions in viral distribution of the ad."""
    viral_registrations: AirbyteSortOrder
    """Total registrations in viral distribution of the ad."""
    viral_shares: AirbyteSortOrder
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: AirbyteSortOrder
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: AirbyteSortOrder
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: AirbyteSortOrder
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: AirbyteSortOrder
    """Total views of videos in viral distribution of the ad."""
    pivot: AirbyteSortOrder
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: AirbyteSortOrder
    """URN of the sponsored campaign this analytics record belongs to"""


# Entity-specific condition types for ad_member_company_analytics
class AdMemberCompanyAnalyticsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdMemberCompanyAnalyticsSearchFilter


class AdMemberCompanyAnalyticsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdMemberCompanyAnalyticsSearchFilter


class AdMemberCompanyAnalyticsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdMemberCompanyAnalyticsSearchFilter


class AdMemberCompanyAnalyticsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdMemberCompanyAnalyticsSearchFilter


class AdMemberCompanyAnalyticsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdMemberCompanyAnalyticsSearchFilter


class AdMemberCompanyAnalyticsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdMemberCompanyAnalyticsSearchFilter


class AdMemberCompanyAnalyticsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AdMemberCompanyAnalyticsStringFilter


class AdMemberCompanyAnalyticsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AdMemberCompanyAnalyticsStringFilter


class AdMemberCompanyAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdMemberCompanyAnalyticsStringFilter


class AdMemberCompanyAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdMemberCompanyAnalyticsStringFilter


class AdMemberCompanyAnalyticsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: AdMemberCompanyAnalyticsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdMemberCompanyAnalyticsInCondition = TypedDict("AdMemberCompanyAnalyticsInCondition", {"in": AdMemberCompanyAnalyticsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdMemberCompanyAnalyticsNotCondition = TypedDict("AdMemberCompanyAnalyticsNotCondition", {"not": "AdMemberCompanyAnalyticsCondition"}, total=False)
"""Negates the nested condition."""

AdMemberCompanyAnalyticsAndCondition = TypedDict("AdMemberCompanyAnalyticsAndCondition", {"and": "list[AdMemberCompanyAnalyticsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdMemberCompanyAnalyticsOrCondition = TypedDict("AdMemberCompanyAnalyticsOrCondition", {"or": "list[AdMemberCompanyAnalyticsCondition]"}, total=False)
"""True if any nested condition is true."""

AdMemberCompanyAnalyticsAnyCondition = TypedDict("AdMemberCompanyAnalyticsAnyCondition", {"any": AdMemberCompanyAnalyticsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_member_company_analytics condition types
AdMemberCompanyAnalyticsCondition = (
    AdMemberCompanyAnalyticsEqCondition
    | AdMemberCompanyAnalyticsNeqCondition
    | AdMemberCompanyAnalyticsGtCondition
    | AdMemberCompanyAnalyticsGteCondition
    | AdMemberCompanyAnalyticsLtCondition
    | AdMemberCompanyAnalyticsLteCondition
    | AdMemberCompanyAnalyticsInCondition
    | AdMemberCompanyAnalyticsStartswithCondition
    | AdMemberCompanyAnalyticsEndswithCondition
    | AdMemberCompanyAnalyticsFuzzyCondition
    | AdMemberCompanyAnalyticsKeywordCondition
    | AdMemberCompanyAnalyticsContainsCondition
    | AdMemberCompanyAnalyticsNotCondition
    | AdMemberCompanyAnalyticsAndCondition
    | AdMemberCompanyAnalyticsOrCondition
    | AdMemberCompanyAnalyticsAnyCondition
)


class AdMemberCompanyAnalyticsSearchQuery(TypedDict, total=False):
    """Search query for ad_member_company_analytics entity."""
    filter: AdMemberCompanyAnalyticsCondition
    sort: list[AdMemberCompanyAnalyticsSortFilter]


# ===== AD_MEMBER_COMPANY_SIZE_ANALYTICS SEARCH TYPES =====

class AdMemberCompanySizeAnalyticsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_member_company_size_analytics search queries."""
    action_clicks: float | None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None
    """An approximation of unique ad impressions."""
    card_clicks: float | None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None
    """The number of times interactive cards were displayed."""
    clicks: float | None
    """Total number of clicks on the ad."""
    comment_likes: float | None
    """The count of likes on comments related to the ad."""
    comments: float | None
    """The number of comments on the ad."""
    company_page_clicks: float | None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None
    """Cost of ad campaign in USD."""
    document_completions: float | None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None
    """Completions for third quartile of document views."""
    download_clicks: float | None
    """Clicks on download links in the ad."""
    end_date: str | None
    """End date of the ad analytics data."""
    external_website_conversions: float | None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites."""
    follows: float | None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None
    """Total number of times the ad was displayed."""
    job_applications: float | None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None
    """Leads generated in one click."""
    opens: float | None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None
    """Registrations completed post-viewing the ad."""
    reactions: float | None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None
    """Total registrations completed through the ad."""
    sends: float | None
    """Number of messages sent through the ad."""
    shares: float | None
    """Total shares generated by the ad."""
    start_date: str | None
    """Start date of the ad analytics data."""
    talent_leads: float | None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None
    """Leads generated through valid work emails."""
    video_completions: float | None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None
    """Completions for midpoint of video views."""
    video_starts: float | None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None
    """Completions for third quartile of video views."""
    video_views: float | None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCompanySizeAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    action_clicks: list[float]
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: list[float]
    """The number of clicks on ad unit components."""
    approximate_member_reach: list[float]
    """An approximation of unique ad impressions."""
    card_clicks: list[float]
    """The number of clicks on interactive card elements."""
    card_impressions: list[float]
    """The number of times interactive cards were displayed."""
    clicks: list[float]
    """Total number of clicks on the ad."""
    comment_likes: list[float]
    """The count of likes on comments related to the ad."""
    comments: list[float]
    """The number of comments on the ad."""
    company_page_clicks: list[float]
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: list[float]
    """Conversion value in the local currency."""
    cost_in_local_currency: list[float]
    """Cost of ad campaign in the local currency."""
    cost_in_usd: list[float]
    """Cost of ad campaign in USD."""
    document_completions: list[float]
    """Number of completions for document views."""
    document_first_quartile_completions: list[float]
    """Completions for first quartile of document views."""
    document_midpoint_completions: list[float]
    """Completions for midpoint of document views."""
    document_third_quartile_completions: list[float]
    """Completions for third quartile of document views."""
    download_clicks: list[float]
    """Clicks on download links in the ad."""
    end_date: list[str]
    """End date of the ad analytics data."""
    external_website_conversions: list[float]
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites."""
    follows: list[float]
    """Number of follows generated by the ad."""
    full_screen_plays: list[float]
    """Number of times videos were played in fullscreen mode."""
    impressions: list[float]
    """Total number of times the ad was displayed."""
    job_applications: list[float]
    """Number of job applications initiated through the ad."""
    job_apply_clicks: list[float]
    """Clicks on apply job button in the ad."""
    landing_page_clicks: list[float]
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: list[float]
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: list[float]
    """Clicks on expressing interest through lead generation mail."""
    likes: list[float]
    """Total likes received on the ad."""
    one_click_lead_form_opens: list[float]
    """Number of times lead forms were opened in one click."""
    one_click_leads: list[float]
    """Leads generated in one click."""
    opens: list[float]
    """The number of times the ad was opened or expanded."""
    other_engagements: list[float]
    """Engagements other than clicks on the ad."""
    pivot_values: list[list[Any]]
    """Values used for pivoting the analytics."""
    string_of_pivot_values: list[str]
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: list[float]
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: list[float]
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: list[float]
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: list[float]
    """Registrations completed post-viewing the ad."""
    reactions: list[float]
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: list[float]
    """Total registrations completed through the ad."""
    sends: list[float]
    """Number of messages sent through the ad."""
    shares: list[float]
    """Total shares generated by the ad."""
    start_date: list[str]
    """Start date of the ad analytics data."""
    talent_leads: list[float]
    """Number of leads related to talent acquisition."""
    text_url_clicks: list[float]
    """Clicks on text URLs within the ad."""
    total_engagements: list[float]
    """Total number of engagements on the ad."""
    valid_work_email_leads: list[float]
    """Leads generated through valid work emails."""
    video_completions: list[float]
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: list[float]
    """Completions for first quartile of video views."""
    video_midpoint_completions: list[float]
    """Completions for midpoint of video views."""
    video_starts: list[float]
    """Total video starts initiated by users."""
    video_third_quartile_completions: list[float]
    """Completions for third quartile of video views."""
    video_views: list[float]
    """Total views of videos in the ad."""
    viral_card_clicks: list[float]
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: list[float]
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: list[float]
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: list[float]
    """Likes received on comments in viral distribution."""
    viral_comments: list[float]
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: list[float]
    """Clicks on the company page in viral distribution."""
    viral_document_completions: list[float]
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: list[float]
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: list[float]
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: list[float]
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: list[float]
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: list[float]
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: list[float]
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: list[float]
    """Fullscreen video plays in viral distribution."""
    viral_impressions: list[float]
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: list[float]
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: list[float]
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: list[float]
    """Clicks on landing page in viral distribution."""
    viral_likes: list[float]
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: list[float]
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: list[float]
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: list[float]
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: list[float]
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: list[float]
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: list[float]
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: list[float]
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: list[float]
    """Total reactions in viral distribution of the ad."""
    viral_registrations: list[float]
    """Total registrations in viral distribution of the ad."""
    viral_shares: list[float]
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: list[float]
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: list[float]
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: list[float]
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: list[float]
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: list[float]
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: list[float]
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: list[float]
    """Total views of videos in viral distribution of the ad."""
    pivot: list[str]
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: list[str]
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCompanySizeAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    action_clicks: Any
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: Any
    """The number of clicks on ad unit components."""
    approximate_member_reach: Any
    """An approximation of unique ad impressions."""
    card_clicks: Any
    """The number of clicks on interactive card elements."""
    card_impressions: Any
    """The number of times interactive cards were displayed."""
    clicks: Any
    """Total number of clicks on the ad."""
    comment_likes: Any
    """The count of likes on comments related to the ad."""
    comments: Any
    """The number of comments on the ad."""
    company_page_clicks: Any
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: Any
    """Conversion value in the local currency."""
    cost_in_local_currency: Any
    """Cost of ad campaign in the local currency."""
    cost_in_usd: Any
    """Cost of ad campaign in USD."""
    document_completions: Any
    """Number of completions for document views."""
    document_first_quartile_completions: Any
    """Completions for first quartile of document views."""
    document_midpoint_completions: Any
    """Completions for midpoint of document views."""
    document_third_quartile_completions: Any
    """Completions for third quartile of document views."""
    download_clicks: Any
    """Clicks on download links in the ad."""
    end_date: Any
    """End date of the ad analytics data."""
    external_website_conversions: Any
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites."""
    follows: Any
    """Number of follows generated by the ad."""
    full_screen_plays: Any
    """Number of times videos were played in fullscreen mode."""
    impressions: Any
    """Total number of times the ad was displayed."""
    job_applications: Any
    """Number of job applications initiated through the ad."""
    job_apply_clicks: Any
    """Clicks on apply job button in the ad."""
    landing_page_clicks: Any
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: Any
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: Any
    """Clicks on expressing interest through lead generation mail."""
    likes: Any
    """Total likes received on the ad."""
    one_click_lead_form_opens: Any
    """Number of times lead forms were opened in one click."""
    one_click_leads: Any
    """Leads generated in one click."""
    opens: Any
    """The number of times the ad was opened or expanded."""
    other_engagements: Any
    """Engagements other than clicks on the ad."""
    pivot_values: Any
    """Values used for pivoting the analytics."""
    string_of_pivot_values: Any
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: Any
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: Any
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: Any
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: Any
    """Registrations completed post-viewing the ad."""
    reactions: Any
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: Any
    """Total registrations completed through the ad."""
    sends: Any
    """Number of messages sent through the ad."""
    shares: Any
    """Total shares generated by the ad."""
    start_date: Any
    """Start date of the ad analytics data."""
    talent_leads: Any
    """Number of leads related to talent acquisition."""
    text_url_clicks: Any
    """Clicks on text URLs within the ad."""
    total_engagements: Any
    """Total number of engagements on the ad."""
    valid_work_email_leads: Any
    """Leads generated through valid work emails."""
    video_completions: Any
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: Any
    """Completions for first quartile of video views."""
    video_midpoint_completions: Any
    """Completions for midpoint of video views."""
    video_starts: Any
    """Total video starts initiated by users."""
    video_third_quartile_completions: Any
    """Completions for third quartile of video views."""
    video_views: Any
    """Total views of videos in the ad."""
    viral_card_clicks: Any
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: Any
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: Any
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: Any
    """Likes received on comments in viral distribution."""
    viral_comments: Any
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: Any
    """Clicks on the company page in viral distribution."""
    viral_document_completions: Any
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: Any
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: Any
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: Any
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: Any
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: Any
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: Any
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: Any
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: Any
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: Any
    """Fullscreen video plays in viral distribution."""
    viral_impressions: Any
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: Any
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: Any
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: Any
    """Clicks on landing page in viral distribution."""
    viral_likes: Any
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: Any
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: Any
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: Any
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: Any
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: Any
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: Any
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: Any
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: Any
    """Total reactions in viral distribution of the ad."""
    viral_registrations: Any
    """Total registrations in viral distribution of the ad."""
    viral_shares: Any
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: Any
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: Any
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: Any
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: Any
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: Any
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: Any
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: Any
    """Total views of videos in viral distribution of the ad."""
    pivot: Any
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: Any
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCompanySizeAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    action_clicks: str
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: str
    """The number of clicks on ad unit components."""
    approximate_member_reach: str
    """An approximation of unique ad impressions."""
    card_clicks: str
    """The number of clicks on interactive card elements."""
    card_impressions: str
    """The number of times interactive cards were displayed."""
    clicks: str
    """Total number of clicks on the ad."""
    comment_likes: str
    """The count of likes on comments related to the ad."""
    comments: str
    """The number of comments on the ad."""
    company_page_clicks: str
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: str
    """Conversion value in the local currency."""
    cost_in_local_currency: str
    """Cost of ad campaign in the local currency."""
    cost_in_usd: str
    """Cost of ad campaign in USD."""
    document_completions: str
    """Number of completions for document views."""
    document_first_quartile_completions: str
    """Completions for first quartile of document views."""
    document_midpoint_completions: str
    """Completions for midpoint of document views."""
    document_third_quartile_completions: str
    """Completions for third quartile of document views."""
    download_clicks: str
    """Clicks on download links in the ad."""
    end_date: str
    """End date of the ad analytics data."""
    external_website_conversions: str
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites."""
    follows: str
    """Number of follows generated by the ad."""
    full_screen_plays: str
    """Number of times videos were played in fullscreen mode."""
    impressions: str
    """Total number of times the ad was displayed."""
    job_applications: str
    """Number of job applications initiated through the ad."""
    job_apply_clicks: str
    """Clicks on apply job button in the ad."""
    landing_page_clicks: str
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: str
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: str
    """Clicks on expressing interest through lead generation mail."""
    likes: str
    """Total likes received on the ad."""
    one_click_lead_form_opens: str
    """Number of times lead forms were opened in one click."""
    one_click_leads: str
    """Leads generated in one click."""
    opens: str
    """The number of times the ad was opened or expanded."""
    other_engagements: str
    """Engagements other than clicks on the ad."""
    pivot_values: str
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: str
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: str
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: str
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: str
    """Registrations completed post-viewing the ad."""
    reactions: str
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: str
    """Total registrations completed through the ad."""
    sends: str
    """Number of messages sent through the ad."""
    shares: str
    """Total shares generated by the ad."""
    start_date: str
    """Start date of the ad analytics data."""
    talent_leads: str
    """Number of leads related to talent acquisition."""
    text_url_clicks: str
    """Clicks on text URLs within the ad."""
    total_engagements: str
    """Total number of engagements on the ad."""
    valid_work_email_leads: str
    """Leads generated through valid work emails."""
    video_completions: str
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: str
    """Completions for first quartile of video views."""
    video_midpoint_completions: str
    """Completions for midpoint of video views."""
    video_starts: str
    """Total video starts initiated by users."""
    video_third_quartile_completions: str
    """Completions for third quartile of video views."""
    video_views: str
    """Total views of videos in the ad."""
    viral_card_clicks: str
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: str
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: str
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: str
    """Likes received on comments in viral distribution."""
    viral_comments: str
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: str
    """Clicks on the company page in viral distribution."""
    viral_document_completions: str
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: str
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: str
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: str
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: str
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: str
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: str
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: str
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: str
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: str
    """Fullscreen video plays in viral distribution."""
    viral_impressions: str
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: str
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: str
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: str
    """Clicks on landing page in viral distribution."""
    viral_likes: str
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: str
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: str
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: str
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: str
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: str
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: str
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: str
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: str
    """Total reactions in viral distribution of the ad."""
    viral_registrations: str
    """Total registrations in viral distribution of the ad."""
    viral_shares: str
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: str
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: str
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: str
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: str
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: str
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: str
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: str
    """Total views of videos in viral distribution of the ad."""
    pivot: str
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCompanySizeAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_member_company_size_analytics search results."""
    action_clicks: AirbyteSortOrder
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: AirbyteSortOrder
    """The number of clicks on ad unit components."""
    approximate_member_reach: AirbyteSortOrder
    """An approximation of unique ad impressions."""
    card_clicks: AirbyteSortOrder
    """The number of clicks on interactive card elements."""
    card_impressions: AirbyteSortOrder
    """The number of times interactive cards were displayed."""
    clicks: AirbyteSortOrder
    """Total number of clicks on the ad."""
    comment_likes: AirbyteSortOrder
    """The count of likes on comments related to the ad."""
    comments: AirbyteSortOrder
    """The number of comments on the ad."""
    company_page_clicks: AirbyteSortOrder
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in the local currency."""
    cost_in_local_currency: AirbyteSortOrder
    """Cost of ad campaign in the local currency."""
    cost_in_usd: AirbyteSortOrder
    """Cost of ad campaign in USD."""
    document_completions: AirbyteSortOrder
    """Number of completions for document views."""
    document_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of document views."""
    document_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of document views."""
    document_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of document views."""
    download_clicks: AirbyteSortOrder
    """Clicks on download links in the ad."""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data."""
    external_website_conversions: AirbyteSortOrder
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites."""
    follows: AirbyteSortOrder
    """Number of follows generated by the ad."""
    full_screen_plays: AirbyteSortOrder
    """Number of times videos were played in fullscreen mode."""
    impressions: AirbyteSortOrder
    """Total number of times the ad was displayed."""
    job_applications: AirbyteSortOrder
    """Number of job applications initiated through the ad."""
    job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in the ad."""
    landing_page_clicks: AirbyteSortOrder
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: AirbyteSortOrder
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: AirbyteSortOrder
    """Clicks on expressing interest through lead generation mail."""
    likes: AirbyteSortOrder
    """Total likes received on the ad."""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of times lead forms were opened in one click."""
    one_click_leads: AirbyteSortOrder
    """Leads generated in one click."""
    opens: AirbyteSortOrder
    """The number of times the ad was opened or expanded."""
    other_engagements: AirbyteSortOrder
    """Engagements other than clicks on the ad."""
    pivot_values: AirbyteSortOrder
    """Values used for pivoting the analytics."""
    string_of_pivot_values: AirbyteSortOrder
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing the ad."""
    reactions: AirbyteSortOrder
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: AirbyteSortOrder
    """Total registrations completed through the ad."""
    sends: AirbyteSortOrder
    """Number of messages sent through the ad."""
    shares: AirbyteSortOrder
    """Total shares generated by the ad."""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data."""
    talent_leads: AirbyteSortOrder
    """Number of leads related to talent acquisition."""
    text_url_clicks: AirbyteSortOrder
    """Clicks on text URLs within the ad."""
    total_engagements: AirbyteSortOrder
    """Total number of engagements on the ad."""
    valid_work_email_leads: AirbyteSortOrder
    """Leads generated through valid work emails."""
    video_completions: AirbyteSortOrder
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of video views."""
    video_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of video views."""
    video_starts: AirbyteSortOrder
    """Total video starts initiated by users."""
    video_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of video views."""
    video_views: AirbyteSortOrder
    """Total views of videos in the ad."""
    viral_card_clicks: AirbyteSortOrder
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: AirbyteSortOrder
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: AirbyteSortOrder
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: AirbyteSortOrder
    """Likes received on comments in viral distribution."""
    viral_comments: AirbyteSortOrder
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: AirbyteSortOrder
    """Clicks on the company page in viral distribution."""
    viral_document_completions: AirbyteSortOrder
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: AirbyteSortOrder
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: AirbyteSortOrder
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: AirbyteSortOrder
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: AirbyteSortOrder
    """Fullscreen video plays in viral distribution."""
    viral_impressions: AirbyteSortOrder
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: AirbyteSortOrder
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: AirbyteSortOrder
    """Clicks on landing page in viral distribution."""
    viral_likes: AirbyteSortOrder
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: AirbyteSortOrder
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: AirbyteSortOrder
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: AirbyteSortOrder
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: AirbyteSortOrder
    """Total reactions in viral distribution of the ad."""
    viral_registrations: AirbyteSortOrder
    """Total registrations in viral distribution of the ad."""
    viral_shares: AirbyteSortOrder
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: AirbyteSortOrder
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: AirbyteSortOrder
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: AirbyteSortOrder
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: AirbyteSortOrder
    """Total views of videos in viral distribution of the ad."""
    pivot: AirbyteSortOrder
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: AirbyteSortOrder
    """URN of the sponsored campaign this analytics record belongs to"""


# Entity-specific condition types for ad_member_company_size_analytics
class AdMemberCompanySizeAnalyticsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdMemberCompanySizeAnalyticsSearchFilter


class AdMemberCompanySizeAnalyticsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdMemberCompanySizeAnalyticsSearchFilter


class AdMemberCompanySizeAnalyticsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdMemberCompanySizeAnalyticsSearchFilter


class AdMemberCompanySizeAnalyticsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdMemberCompanySizeAnalyticsSearchFilter


class AdMemberCompanySizeAnalyticsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdMemberCompanySizeAnalyticsSearchFilter


class AdMemberCompanySizeAnalyticsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdMemberCompanySizeAnalyticsSearchFilter


class AdMemberCompanySizeAnalyticsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AdMemberCompanySizeAnalyticsStringFilter


class AdMemberCompanySizeAnalyticsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AdMemberCompanySizeAnalyticsStringFilter


class AdMemberCompanySizeAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdMemberCompanySizeAnalyticsStringFilter


class AdMemberCompanySizeAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdMemberCompanySizeAnalyticsStringFilter


class AdMemberCompanySizeAnalyticsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: AdMemberCompanySizeAnalyticsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdMemberCompanySizeAnalyticsInCondition = TypedDict("AdMemberCompanySizeAnalyticsInCondition", {"in": AdMemberCompanySizeAnalyticsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdMemberCompanySizeAnalyticsNotCondition = TypedDict("AdMemberCompanySizeAnalyticsNotCondition", {"not": "AdMemberCompanySizeAnalyticsCondition"}, total=False)
"""Negates the nested condition."""

AdMemberCompanySizeAnalyticsAndCondition = TypedDict("AdMemberCompanySizeAnalyticsAndCondition", {"and": "list[AdMemberCompanySizeAnalyticsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdMemberCompanySizeAnalyticsOrCondition = TypedDict("AdMemberCompanySizeAnalyticsOrCondition", {"or": "list[AdMemberCompanySizeAnalyticsCondition]"}, total=False)
"""True if any nested condition is true."""

AdMemberCompanySizeAnalyticsAnyCondition = TypedDict("AdMemberCompanySizeAnalyticsAnyCondition", {"any": AdMemberCompanySizeAnalyticsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_member_company_size_analytics condition types
AdMemberCompanySizeAnalyticsCondition = (
    AdMemberCompanySizeAnalyticsEqCondition
    | AdMemberCompanySizeAnalyticsNeqCondition
    | AdMemberCompanySizeAnalyticsGtCondition
    | AdMemberCompanySizeAnalyticsGteCondition
    | AdMemberCompanySizeAnalyticsLtCondition
    | AdMemberCompanySizeAnalyticsLteCondition
    | AdMemberCompanySizeAnalyticsInCondition
    | AdMemberCompanySizeAnalyticsStartswithCondition
    | AdMemberCompanySizeAnalyticsEndswithCondition
    | AdMemberCompanySizeAnalyticsFuzzyCondition
    | AdMemberCompanySizeAnalyticsKeywordCondition
    | AdMemberCompanySizeAnalyticsContainsCondition
    | AdMemberCompanySizeAnalyticsNotCondition
    | AdMemberCompanySizeAnalyticsAndCondition
    | AdMemberCompanySizeAnalyticsOrCondition
    | AdMemberCompanySizeAnalyticsAnyCondition
)


class AdMemberCompanySizeAnalyticsSearchQuery(TypedDict, total=False):
    """Search query for ad_member_company_size_analytics entity."""
    filter: AdMemberCompanySizeAnalyticsCondition
    sort: list[AdMemberCompanySizeAnalyticsSortFilter]


# ===== AD_MEMBER_COUNTRY_ANALYTICS SEARCH TYPES =====

class AdMemberCountryAnalyticsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_member_country_analytics search queries."""
    action_clicks: float | None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None
    """An approximation of unique ad impressions."""
    card_clicks: float | None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None
    """The number of times interactive cards were displayed."""
    clicks: float | None
    """Total number of clicks on the ad."""
    comment_likes: float | None
    """The count of likes on comments related to the ad."""
    comments: float | None
    """The number of comments on the ad."""
    company_page_clicks: float | None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None
    """Cost of ad campaign in USD."""
    document_completions: float | None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None
    """Completions for third quartile of document views."""
    download_clicks: float | None
    """Clicks on download links in the ad."""
    end_date: str | None
    """End date of the ad analytics data."""
    external_website_conversions: float | None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites."""
    follows: float | None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None
    """Total number of times the ad was displayed."""
    job_applications: float | None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None
    """Leads generated in one click."""
    opens: float | None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None
    """Registrations completed post-viewing the ad."""
    reactions: float | None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None
    """Total registrations completed through the ad."""
    sends: float | None
    """Number of messages sent through the ad."""
    shares: float | None
    """Total shares generated by the ad."""
    start_date: str | None
    """Start date of the ad analytics data."""
    talent_leads: float | None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None
    """Leads generated through valid work emails."""
    video_completions: float | None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None
    """Completions for midpoint of video views."""
    video_starts: float | None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None
    """Completions for third quartile of video views."""
    video_views: float | None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCountryAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    action_clicks: list[float]
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: list[float]
    """The number of clicks on ad unit components."""
    approximate_member_reach: list[float]
    """An approximation of unique ad impressions."""
    card_clicks: list[float]
    """The number of clicks on interactive card elements."""
    card_impressions: list[float]
    """The number of times interactive cards were displayed."""
    clicks: list[float]
    """Total number of clicks on the ad."""
    comment_likes: list[float]
    """The count of likes on comments related to the ad."""
    comments: list[float]
    """The number of comments on the ad."""
    company_page_clicks: list[float]
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: list[float]
    """Conversion value in the local currency."""
    cost_in_local_currency: list[float]
    """Cost of ad campaign in the local currency."""
    cost_in_usd: list[float]
    """Cost of ad campaign in USD."""
    document_completions: list[float]
    """Number of completions for document views."""
    document_first_quartile_completions: list[float]
    """Completions for first quartile of document views."""
    document_midpoint_completions: list[float]
    """Completions for midpoint of document views."""
    document_third_quartile_completions: list[float]
    """Completions for third quartile of document views."""
    download_clicks: list[float]
    """Clicks on download links in the ad."""
    end_date: list[str]
    """End date of the ad analytics data."""
    external_website_conversions: list[float]
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites."""
    follows: list[float]
    """Number of follows generated by the ad."""
    full_screen_plays: list[float]
    """Number of times videos were played in fullscreen mode."""
    impressions: list[float]
    """Total number of times the ad was displayed."""
    job_applications: list[float]
    """Number of job applications initiated through the ad."""
    job_apply_clicks: list[float]
    """Clicks on apply job button in the ad."""
    landing_page_clicks: list[float]
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: list[float]
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: list[float]
    """Clicks on expressing interest through lead generation mail."""
    likes: list[float]
    """Total likes received on the ad."""
    one_click_lead_form_opens: list[float]
    """Number of times lead forms were opened in one click."""
    one_click_leads: list[float]
    """Leads generated in one click."""
    opens: list[float]
    """The number of times the ad was opened or expanded."""
    other_engagements: list[float]
    """Engagements other than clicks on the ad."""
    pivot_values: list[list[Any]]
    """Values used for pivoting the analytics."""
    string_of_pivot_values: list[str]
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: list[float]
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: list[float]
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: list[float]
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: list[float]
    """Registrations completed post-viewing the ad."""
    reactions: list[float]
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: list[float]
    """Total registrations completed through the ad."""
    sends: list[float]
    """Number of messages sent through the ad."""
    shares: list[float]
    """Total shares generated by the ad."""
    start_date: list[str]
    """Start date of the ad analytics data."""
    talent_leads: list[float]
    """Number of leads related to talent acquisition."""
    text_url_clicks: list[float]
    """Clicks on text URLs within the ad."""
    total_engagements: list[float]
    """Total number of engagements on the ad."""
    valid_work_email_leads: list[float]
    """Leads generated through valid work emails."""
    video_completions: list[float]
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: list[float]
    """Completions for first quartile of video views."""
    video_midpoint_completions: list[float]
    """Completions for midpoint of video views."""
    video_starts: list[float]
    """Total video starts initiated by users."""
    video_third_quartile_completions: list[float]
    """Completions for third quartile of video views."""
    video_views: list[float]
    """Total views of videos in the ad."""
    viral_card_clicks: list[float]
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: list[float]
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: list[float]
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: list[float]
    """Likes received on comments in viral distribution."""
    viral_comments: list[float]
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: list[float]
    """Clicks on the company page in viral distribution."""
    viral_document_completions: list[float]
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: list[float]
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: list[float]
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: list[float]
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: list[float]
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: list[float]
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: list[float]
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: list[float]
    """Fullscreen video plays in viral distribution."""
    viral_impressions: list[float]
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: list[float]
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: list[float]
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: list[float]
    """Clicks on landing page in viral distribution."""
    viral_likes: list[float]
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: list[float]
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: list[float]
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: list[float]
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: list[float]
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: list[float]
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: list[float]
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: list[float]
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: list[float]
    """Total reactions in viral distribution of the ad."""
    viral_registrations: list[float]
    """Total registrations in viral distribution of the ad."""
    viral_shares: list[float]
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: list[float]
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: list[float]
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: list[float]
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: list[float]
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: list[float]
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: list[float]
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: list[float]
    """Total views of videos in viral distribution of the ad."""
    pivot: list[str]
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: list[str]
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCountryAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    action_clicks: Any
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: Any
    """The number of clicks on ad unit components."""
    approximate_member_reach: Any
    """An approximation of unique ad impressions."""
    card_clicks: Any
    """The number of clicks on interactive card elements."""
    card_impressions: Any
    """The number of times interactive cards were displayed."""
    clicks: Any
    """Total number of clicks on the ad."""
    comment_likes: Any
    """The count of likes on comments related to the ad."""
    comments: Any
    """The number of comments on the ad."""
    company_page_clicks: Any
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: Any
    """Conversion value in the local currency."""
    cost_in_local_currency: Any
    """Cost of ad campaign in the local currency."""
    cost_in_usd: Any
    """Cost of ad campaign in USD."""
    document_completions: Any
    """Number of completions for document views."""
    document_first_quartile_completions: Any
    """Completions for first quartile of document views."""
    document_midpoint_completions: Any
    """Completions for midpoint of document views."""
    document_third_quartile_completions: Any
    """Completions for third quartile of document views."""
    download_clicks: Any
    """Clicks on download links in the ad."""
    end_date: Any
    """End date of the ad analytics data."""
    external_website_conversions: Any
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites."""
    follows: Any
    """Number of follows generated by the ad."""
    full_screen_plays: Any
    """Number of times videos were played in fullscreen mode."""
    impressions: Any
    """Total number of times the ad was displayed."""
    job_applications: Any
    """Number of job applications initiated through the ad."""
    job_apply_clicks: Any
    """Clicks on apply job button in the ad."""
    landing_page_clicks: Any
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: Any
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: Any
    """Clicks on expressing interest through lead generation mail."""
    likes: Any
    """Total likes received on the ad."""
    one_click_lead_form_opens: Any
    """Number of times lead forms were opened in one click."""
    one_click_leads: Any
    """Leads generated in one click."""
    opens: Any
    """The number of times the ad was opened or expanded."""
    other_engagements: Any
    """Engagements other than clicks on the ad."""
    pivot_values: Any
    """Values used for pivoting the analytics."""
    string_of_pivot_values: Any
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: Any
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: Any
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: Any
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: Any
    """Registrations completed post-viewing the ad."""
    reactions: Any
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: Any
    """Total registrations completed through the ad."""
    sends: Any
    """Number of messages sent through the ad."""
    shares: Any
    """Total shares generated by the ad."""
    start_date: Any
    """Start date of the ad analytics data."""
    talent_leads: Any
    """Number of leads related to talent acquisition."""
    text_url_clicks: Any
    """Clicks on text URLs within the ad."""
    total_engagements: Any
    """Total number of engagements on the ad."""
    valid_work_email_leads: Any
    """Leads generated through valid work emails."""
    video_completions: Any
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: Any
    """Completions for first quartile of video views."""
    video_midpoint_completions: Any
    """Completions for midpoint of video views."""
    video_starts: Any
    """Total video starts initiated by users."""
    video_third_quartile_completions: Any
    """Completions for third quartile of video views."""
    video_views: Any
    """Total views of videos in the ad."""
    viral_card_clicks: Any
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: Any
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: Any
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: Any
    """Likes received on comments in viral distribution."""
    viral_comments: Any
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: Any
    """Clicks on the company page in viral distribution."""
    viral_document_completions: Any
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: Any
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: Any
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: Any
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: Any
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: Any
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: Any
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: Any
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: Any
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: Any
    """Fullscreen video plays in viral distribution."""
    viral_impressions: Any
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: Any
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: Any
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: Any
    """Clicks on landing page in viral distribution."""
    viral_likes: Any
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: Any
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: Any
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: Any
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: Any
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: Any
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: Any
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: Any
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: Any
    """Total reactions in viral distribution of the ad."""
    viral_registrations: Any
    """Total registrations in viral distribution of the ad."""
    viral_shares: Any
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: Any
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: Any
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: Any
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: Any
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: Any
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: Any
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: Any
    """Total views of videos in viral distribution of the ad."""
    pivot: Any
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: Any
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCountryAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    action_clicks: str
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: str
    """The number of clicks on ad unit components."""
    approximate_member_reach: str
    """An approximation of unique ad impressions."""
    card_clicks: str
    """The number of clicks on interactive card elements."""
    card_impressions: str
    """The number of times interactive cards were displayed."""
    clicks: str
    """Total number of clicks on the ad."""
    comment_likes: str
    """The count of likes on comments related to the ad."""
    comments: str
    """The number of comments on the ad."""
    company_page_clicks: str
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: str
    """Conversion value in the local currency."""
    cost_in_local_currency: str
    """Cost of ad campaign in the local currency."""
    cost_in_usd: str
    """Cost of ad campaign in USD."""
    document_completions: str
    """Number of completions for document views."""
    document_first_quartile_completions: str
    """Completions for first quartile of document views."""
    document_midpoint_completions: str
    """Completions for midpoint of document views."""
    document_third_quartile_completions: str
    """Completions for third quartile of document views."""
    download_clicks: str
    """Clicks on download links in the ad."""
    end_date: str
    """End date of the ad analytics data."""
    external_website_conversions: str
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites."""
    follows: str
    """Number of follows generated by the ad."""
    full_screen_plays: str
    """Number of times videos were played in fullscreen mode."""
    impressions: str
    """Total number of times the ad was displayed."""
    job_applications: str
    """Number of job applications initiated through the ad."""
    job_apply_clicks: str
    """Clicks on apply job button in the ad."""
    landing_page_clicks: str
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: str
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: str
    """Clicks on expressing interest through lead generation mail."""
    likes: str
    """Total likes received on the ad."""
    one_click_lead_form_opens: str
    """Number of times lead forms were opened in one click."""
    one_click_leads: str
    """Leads generated in one click."""
    opens: str
    """The number of times the ad was opened or expanded."""
    other_engagements: str
    """Engagements other than clicks on the ad."""
    pivot_values: str
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: str
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: str
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: str
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: str
    """Registrations completed post-viewing the ad."""
    reactions: str
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: str
    """Total registrations completed through the ad."""
    sends: str
    """Number of messages sent through the ad."""
    shares: str
    """Total shares generated by the ad."""
    start_date: str
    """Start date of the ad analytics data."""
    talent_leads: str
    """Number of leads related to talent acquisition."""
    text_url_clicks: str
    """Clicks on text URLs within the ad."""
    total_engagements: str
    """Total number of engagements on the ad."""
    valid_work_email_leads: str
    """Leads generated through valid work emails."""
    video_completions: str
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: str
    """Completions for first quartile of video views."""
    video_midpoint_completions: str
    """Completions for midpoint of video views."""
    video_starts: str
    """Total video starts initiated by users."""
    video_third_quartile_completions: str
    """Completions for third quartile of video views."""
    video_views: str
    """Total views of videos in the ad."""
    viral_card_clicks: str
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: str
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: str
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: str
    """Likes received on comments in viral distribution."""
    viral_comments: str
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: str
    """Clicks on the company page in viral distribution."""
    viral_document_completions: str
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: str
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: str
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: str
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: str
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: str
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: str
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: str
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: str
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: str
    """Fullscreen video plays in viral distribution."""
    viral_impressions: str
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: str
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: str
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: str
    """Clicks on landing page in viral distribution."""
    viral_likes: str
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: str
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: str
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: str
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: str
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: str
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: str
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: str
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: str
    """Total reactions in viral distribution of the ad."""
    viral_registrations: str
    """Total registrations in viral distribution of the ad."""
    viral_shares: str
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: str
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: str
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: str
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: str
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: str
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: str
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: str
    """Total views of videos in viral distribution of the ad."""
    pivot: str
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberCountryAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_member_country_analytics search results."""
    action_clicks: AirbyteSortOrder
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: AirbyteSortOrder
    """The number of clicks on ad unit components."""
    approximate_member_reach: AirbyteSortOrder
    """An approximation of unique ad impressions."""
    card_clicks: AirbyteSortOrder
    """The number of clicks on interactive card elements."""
    card_impressions: AirbyteSortOrder
    """The number of times interactive cards were displayed."""
    clicks: AirbyteSortOrder
    """Total number of clicks on the ad."""
    comment_likes: AirbyteSortOrder
    """The count of likes on comments related to the ad."""
    comments: AirbyteSortOrder
    """The number of comments on the ad."""
    company_page_clicks: AirbyteSortOrder
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in the local currency."""
    cost_in_local_currency: AirbyteSortOrder
    """Cost of ad campaign in the local currency."""
    cost_in_usd: AirbyteSortOrder
    """Cost of ad campaign in USD."""
    document_completions: AirbyteSortOrder
    """Number of completions for document views."""
    document_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of document views."""
    document_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of document views."""
    document_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of document views."""
    download_clicks: AirbyteSortOrder
    """Clicks on download links in the ad."""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data."""
    external_website_conversions: AirbyteSortOrder
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites."""
    follows: AirbyteSortOrder
    """Number of follows generated by the ad."""
    full_screen_plays: AirbyteSortOrder
    """Number of times videos were played in fullscreen mode."""
    impressions: AirbyteSortOrder
    """Total number of times the ad was displayed."""
    job_applications: AirbyteSortOrder
    """Number of job applications initiated through the ad."""
    job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in the ad."""
    landing_page_clicks: AirbyteSortOrder
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: AirbyteSortOrder
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: AirbyteSortOrder
    """Clicks on expressing interest through lead generation mail."""
    likes: AirbyteSortOrder
    """Total likes received on the ad."""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of times lead forms were opened in one click."""
    one_click_leads: AirbyteSortOrder
    """Leads generated in one click."""
    opens: AirbyteSortOrder
    """The number of times the ad was opened or expanded."""
    other_engagements: AirbyteSortOrder
    """Engagements other than clicks on the ad."""
    pivot_values: AirbyteSortOrder
    """Values used for pivoting the analytics."""
    string_of_pivot_values: AirbyteSortOrder
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing the ad."""
    reactions: AirbyteSortOrder
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: AirbyteSortOrder
    """Total registrations completed through the ad."""
    sends: AirbyteSortOrder
    """Number of messages sent through the ad."""
    shares: AirbyteSortOrder
    """Total shares generated by the ad."""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data."""
    talent_leads: AirbyteSortOrder
    """Number of leads related to talent acquisition."""
    text_url_clicks: AirbyteSortOrder
    """Clicks on text URLs within the ad."""
    total_engagements: AirbyteSortOrder
    """Total number of engagements on the ad."""
    valid_work_email_leads: AirbyteSortOrder
    """Leads generated through valid work emails."""
    video_completions: AirbyteSortOrder
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of video views."""
    video_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of video views."""
    video_starts: AirbyteSortOrder
    """Total video starts initiated by users."""
    video_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of video views."""
    video_views: AirbyteSortOrder
    """Total views of videos in the ad."""
    viral_card_clicks: AirbyteSortOrder
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: AirbyteSortOrder
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: AirbyteSortOrder
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: AirbyteSortOrder
    """Likes received on comments in viral distribution."""
    viral_comments: AirbyteSortOrder
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: AirbyteSortOrder
    """Clicks on the company page in viral distribution."""
    viral_document_completions: AirbyteSortOrder
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: AirbyteSortOrder
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: AirbyteSortOrder
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: AirbyteSortOrder
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: AirbyteSortOrder
    """Fullscreen video plays in viral distribution."""
    viral_impressions: AirbyteSortOrder
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: AirbyteSortOrder
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: AirbyteSortOrder
    """Clicks on landing page in viral distribution."""
    viral_likes: AirbyteSortOrder
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: AirbyteSortOrder
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: AirbyteSortOrder
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: AirbyteSortOrder
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: AirbyteSortOrder
    """Total reactions in viral distribution of the ad."""
    viral_registrations: AirbyteSortOrder
    """Total registrations in viral distribution of the ad."""
    viral_shares: AirbyteSortOrder
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: AirbyteSortOrder
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: AirbyteSortOrder
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: AirbyteSortOrder
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: AirbyteSortOrder
    """Total views of videos in viral distribution of the ad."""
    pivot: AirbyteSortOrder
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: AirbyteSortOrder
    """URN of the sponsored campaign this analytics record belongs to"""


# Entity-specific condition types for ad_member_country_analytics
class AdMemberCountryAnalyticsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdMemberCountryAnalyticsSearchFilter


class AdMemberCountryAnalyticsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdMemberCountryAnalyticsSearchFilter


class AdMemberCountryAnalyticsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdMemberCountryAnalyticsSearchFilter


class AdMemberCountryAnalyticsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdMemberCountryAnalyticsSearchFilter


class AdMemberCountryAnalyticsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdMemberCountryAnalyticsSearchFilter


class AdMemberCountryAnalyticsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdMemberCountryAnalyticsSearchFilter


class AdMemberCountryAnalyticsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AdMemberCountryAnalyticsStringFilter


class AdMemberCountryAnalyticsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AdMemberCountryAnalyticsStringFilter


class AdMemberCountryAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdMemberCountryAnalyticsStringFilter


class AdMemberCountryAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdMemberCountryAnalyticsStringFilter


class AdMemberCountryAnalyticsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: AdMemberCountryAnalyticsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdMemberCountryAnalyticsInCondition = TypedDict("AdMemberCountryAnalyticsInCondition", {"in": AdMemberCountryAnalyticsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdMemberCountryAnalyticsNotCondition = TypedDict("AdMemberCountryAnalyticsNotCondition", {"not": "AdMemberCountryAnalyticsCondition"}, total=False)
"""Negates the nested condition."""

AdMemberCountryAnalyticsAndCondition = TypedDict("AdMemberCountryAnalyticsAndCondition", {"and": "list[AdMemberCountryAnalyticsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdMemberCountryAnalyticsOrCondition = TypedDict("AdMemberCountryAnalyticsOrCondition", {"or": "list[AdMemberCountryAnalyticsCondition]"}, total=False)
"""True if any nested condition is true."""

AdMemberCountryAnalyticsAnyCondition = TypedDict("AdMemberCountryAnalyticsAnyCondition", {"any": AdMemberCountryAnalyticsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_member_country_analytics condition types
AdMemberCountryAnalyticsCondition = (
    AdMemberCountryAnalyticsEqCondition
    | AdMemberCountryAnalyticsNeqCondition
    | AdMemberCountryAnalyticsGtCondition
    | AdMemberCountryAnalyticsGteCondition
    | AdMemberCountryAnalyticsLtCondition
    | AdMemberCountryAnalyticsLteCondition
    | AdMemberCountryAnalyticsInCondition
    | AdMemberCountryAnalyticsStartswithCondition
    | AdMemberCountryAnalyticsEndswithCondition
    | AdMemberCountryAnalyticsFuzzyCondition
    | AdMemberCountryAnalyticsKeywordCondition
    | AdMemberCountryAnalyticsContainsCondition
    | AdMemberCountryAnalyticsNotCondition
    | AdMemberCountryAnalyticsAndCondition
    | AdMemberCountryAnalyticsOrCondition
    | AdMemberCountryAnalyticsAnyCondition
)


class AdMemberCountryAnalyticsSearchQuery(TypedDict, total=False):
    """Search query for ad_member_country_analytics entity."""
    filter: AdMemberCountryAnalyticsCondition
    sort: list[AdMemberCountryAnalyticsSortFilter]


# ===== AD_MEMBER_INDUSTRY_ANALYTICS SEARCH TYPES =====

class AdMemberIndustryAnalyticsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_member_industry_analytics search queries."""
    action_clicks: float | None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None
    """An approximation of unique ad impressions."""
    card_clicks: float | None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None
    """The number of times interactive cards were displayed."""
    clicks: float | None
    """Total number of clicks on the ad."""
    comment_likes: float | None
    """The count of likes on comments related to the ad."""
    comments: float | None
    """The number of comments on the ad."""
    company_page_clicks: float | None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None
    """Cost of ad campaign in USD."""
    document_completions: float | None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None
    """Completions for third quartile of document views."""
    download_clicks: float | None
    """Clicks on download links in the ad."""
    end_date: str | None
    """End date of the ad analytics data."""
    external_website_conversions: float | None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites."""
    follows: float | None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None
    """Total number of times the ad was displayed."""
    job_applications: float | None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None
    """Leads generated in one click."""
    opens: float | None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None
    """Registrations completed post-viewing the ad."""
    reactions: float | None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None
    """Total registrations completed through the ad."""
    sends: float | None
    """Number of messages sent through the ad."""
    shares: float | None
    """Total shares generated by the ad."""
    start_date: str | None
    """Start date of the ad analytics data."""
    talent_leads: float | None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None
    """Leads generated through valid work emails."""
    video_completions: float | None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None
    """Completions for midpoint of video views."""
    video_starts: float | None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None
    """Completions for third quartile of video views."""
    video_views: float | None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberIndustryAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    action_clicks: list[float]
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: list[float]
    """The number of clicks on ad unit components."""
    approximate_member_reach: list[float]
    """An approximation of unique ad impressions."""
    card_clicks: list[float]
    """The number of clicks on interactive card elements."""
    card_impressions: list[float]
    """The number of times interactive cards were displayed."""
    clicks: list[float]
    """Total number of clicks on the ad."""
    comment_likes: list[float]
    """The count of likes on comments related to the ad."""
    comments: list[float]
    """The number of comments on the ad."""
    company_page_clicks: list[float]
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: list[float]
    """Conversion value in the local currency."""
    cost_in_local_currency: list[float]
    """Cost of ad campaign in the local currency."""
    cost_in_usd: list[float]
    """Cost of ad campaign in USD."""
    document_completions: list[float]
    """Number of completions for document views."""
    document_first_quartile_completions: list[float]
    """Completions for first quartile of document views."""
    document_midpoint_completions: list[float]
    """Completions for midpoint of document views."""
    document_third_quartile_completions: list[float]
    """Completions for third quartile of document views."""
    download_clicks: list[float]
    """Clicks on download links in the ad."""
    end_date: list[str]
    """End date of the ad analytics data."""
    external_website_conversions: list[float]
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites."""
    follows: list[float]
    """Number of follows generated by the ad."""
    full_screen_plays: list[float]
    """Number of times videos were played in fullscreen mode."""
    impressions: list[float]
    """Total number of times the ad was displayed."""
    job_applications: list[float]
    """Number of job applications initiated through the ad."""
    job_apply_clicks: list[float]
    """Clicks on apply job button in the ad."""
    landing_page_clicks: list[float]
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: list[float]
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: list[float]
    """Clicks on expressing interest through lead generation mail."""
    likes: list[float]
    """Total likes received on the ad."""
    one_click_lead_form_opens: list[float]
    """Number of times lead forms were opened in one click."""
    one_click_leads: list[float]
    """Leads generated in one click."""
    opens: list[float]
    """The number of times the ad was opened or expanded."""
    other_engagements: list[float]
    """Engagements other than clicks on the ad."""
    pivot_values: list[list[Any]]
    """Values used for pivoting the analytics."""
    string_of_pivot_values: list[str]
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: list[float]
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: list[float]
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: list[float]
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: list[float]
    """Registrations completed post-viewing the ad."""
    reactions: list[float]
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: list[float]
    """Total registrations completed through the ad."""
    sends: list[float]
    """Number of messages sent through the ad."""
    shares: list[float]
    """Total shares generated by the ad."""
    start_date: list[str]
    """Start date of the ad analytics data."""
    talent_leads: list[float]
    """Number of leads related to talent acquisition."""
    text_url_clicks: list[float]
    """Clicks on text URLs within the ad."""
    total_engagements: list[float]
    """Total number of engagements on the ad."""
    valid_work_email_leads: list[float]
    """Leads generated through valid work emails."""
    video_completions: list[float]
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: list[float]
    """Completions for first quartile of video views."""
    video_midpoint_completions: list[float]
    """Completions for midpoint of video views."""
    video_starts: list[float]
    """Total video starts initiated by users."""
    video_third_quartile_completions: list[float]
    """Completions for third quartile of video views."""
    video_views: list[float]
    """Total views of videos in the ad."""
    viral_card_clicks: list[float]
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: list[float]
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: list[float]
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: list[float]
    """Likes received on comments in viral distribution."""
    viral_comments: list[float]
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: list[float]
    """Clicks on the company page in viral distribution."""
    viral_document_completions: list[float]
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: list[float]
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: list[float]
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: list[float]
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: list[float]
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: list[float]
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: list[float]
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: list[float]
    """Fullscreen video plays in viral distribution."""
    viral_impressions: list[float]
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: list[float]
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: list[float]
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: list[float]
    """Clicks on landing page in viral distribution."""
    viral_likes: list[float]
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: list[float]
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: list[float]
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: list[float]
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: list[float]
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: list[float]
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: list[float]
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: list[float]
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: list[float]
    """Total reactions in viral distribution of the ad."""
    viral_registrations: list[float]
    """Total registrations in viral distribution of the ad."""
    viral_shares: list[float]
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: list[float]
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: list[float]
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: list[float]
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: list[float]
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: list[float]
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: list[float]
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: list[float]
    """Total views of videos in viral distribution of the ad."""
    pivot: list[str]
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: list[str]
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberIndustryAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    action_clicks: Any
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: Any
    """The number of clicks on ad unit components."""
    approximate_member_reach: Any
    """An approximation of unique ad impressions."""
    card_clicks: Any
    """The number of clicks on interactive card elements."""
    card_impressions: Any
    """The number of times interactive cards were displayed."""
    clicks: Any
    """Total number of clicks on the ad."""
    comment_likes: Any
    """The count of likes on comments related to the ad."""
    comments: Any
    """The number of comments on the ad."""
    company_page_clicks: Any
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: Any
    """Conversion value in the local currency."""
    cost_in_local_currency: Any
    """Cost of ad campaign in the local currency."""
    cost_in_usd: Any
    """Cost of ad campaign in USD."""
    document_completions: Any
    """Number of completions for document views."""
    document_first_quartile_completions: Any
    """Completions for first quartile of document views."""
    document_midpoint_completions: Any
    """Completions for midpoint of document views."""
    document_third_quartile_completions: Any
    """Completions for third quartile of document views."""
    download_clicks: Any
    """Clicks on download links in the ad."""
    end_date: Any
    """End date of the ad analytics data."""
    external_website_conversions: Any
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites."""
    follows: Any
    """Number of follows generated by the ad."""
    full_screen_plays: Any
    """Number of times videos were played in fullscreen mode."""
    impressions: Any
    """Total number of times the ad was displayed."""
    job_applications: Any
    """Number of job applications initiated through the ad."""
    job_apply_clicks: Any
    """Clicks on apply job button in the ad."""
    landing_page_clicks: Any
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: Any
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: Any
    """Clicks on expressing interest through lead generation mail."""
    likes: Any
    """Total likes received on the ad."""
    one_click_lead_form_opens: Any
    """Number of times lead forms were opened in one click."""
    one_click_leads: Any
    """Leads generated in one click."""
    opens: Any
    """The number of times the ad was opened or expanded."""
    other_engagements: Any
    """Engagements other than clicks on the ad."""
    pivot_values: Any
    """Values used for pivoting the analytics."""
    string_of_pivot_values: Any
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: Any
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: Any
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: Any
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: Any
    """Registrations completed post-viewing the ad."""
    reactions: Any
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: Any
    """Total registrations completed through the ad."""
    sends: Any
    """Number of messages sent through the ad."""
    shares: Any
    """Total shares generated by the ad."""
    start_date: Any
    """Start date of the ad analytics data."""
    talent_leads: Any
    """Number of leads related to talent acquisition."""
    text_url_clicks: Any
    """Clicks on text URLs within the ad."""
    total_engagements: Any
    """Total number of engagements on the ad."""
    valid_work_email_leads: Any
    """Leads generated through valid work emails."""
    video_completions: Any
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: Any
    """Completions for first quartile of video views."""
    video_midpoint_completions: Any
    """Completions for midpoint of video views."""
    video_starts: Any
    """Total video starts initiated by users."""
    video_third_quartile_completions: Any
    """Completions for third quartile of video views."""
    video_views: Any
    """Total views of videos in the ad."""
    viral_card_clicks: Any
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: Any
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: Any
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: Any
    """Likes received on comments in viral distribution."""
    viral_comments: Any
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: Any
    """Clicks on the company page in viral distribution."""
    viral_document_completions: Any
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: Any
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: Any
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: Any
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: Any
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: Any
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: Any
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: Any
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: Any
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: Any
    """Fullscreen video plays in viral distribution."""
    viral_impressions: Any
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: Any
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: Any
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: Any
    """Clicks on landing page in viral distribution."""
    viral_likes: Any
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: Any
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: Any
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: Any
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: Any
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: Any
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: Any
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: Any
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: Any
    """Total reactions in viral distribution of the ad."""
    viral_registrations: Any
    """Total registrations in viral distribution of the ad."""
    viral_shares: Any
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: Any
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: Any
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: Any
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: Any
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: Any
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: Any
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: Any
    """Total views of videos in viral distribution of the ad."""
    pivot: Any
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: Any
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberIndustryAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    action_clicks: str
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: str
    """The number of clicks on ad unit components."""
    approximate_member_reach: str
    """An approximation of unique ad impressions."""
    card_clicks: str
    """The number of clicks on interactive card elements."""
    card_impressions: str
    """The number of times interactive cards were displayed."""
    clicks: str
    """Total number of clicks on the ad."""
    comment_likes: str
    """The count of likes on comments related to the ad."""
    comments: str
    """The number of comments on the ad."""
    company_page_clicks: str
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: str
    """Conversion value in the local currency."""
    cost_in_local_currency: str
    """Cost of ad campaign in the local currency."""
    cost_in_usd: str
    """Cost of ad campaign in USD."""
    document_completions: str
    """Number of completions for document views."""
    document_first_quartile_completions: str
    """Completions for first quartile of document views."""
    document_midpoint_completions: str
    """Completions for midpoint of document views."""
    document_third_quartile_completions: str
    """Completions for third quartile of document views."""
    download_clicks: str
    """Clicks on download links in the ad."""
    end_date: str
    """End date of the ad analytics data."""
    external_website_conversions: str
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites."""
    follows: str
    """Number of follows generated by the ad."""
    full_screen_plays: str
    """Number of times videos were played in fullscreen mode."""
    impressions: str
    """Total number of times the ad was displayed."""
    job_applications: str
    """Number of job applications initiated through the ad."""
    job_apply_clicks: str
    """Clicks on apply job button in the ad."""
    landing_page_clicks: str
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: str
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: str
    """Clicks on expressing interest through lead generation mail."""
    likes: str
    """Total likes received on the ad."""
    one_click_lead_form_opens: str
    """Number of times lead forms were opened in one click."""
    one_click_leads: str
    """Leads generated in one click."""
    opens: str
    """The number of times the ad was opened or expanded."""
    other_engagements: str
    """Engagements other than clicks on the ad."""
    pivot_values: str
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: str
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: str
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: str
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: str
    """Registrations completed post-viewing the ad."""
    reactions: str
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: str
    """Total registrations completed through the ad."""
    sends: str
    """Number of messages sent through the ad."""
    shares: str
    """Total shares generated by the ad."""
    start_date: str
    """Start date of the ad analytics data."""
    talent_leads: str
    """Number of leads related to talent acquisition."""
    text_url_clicks: str
    """Clicks on text URLs within the ad."""
    total_engagements: str
    """Total number of engagements on the ad."""
    valid_work_email_leads: str
    """Leads generated through valid work emails."""
    video_completions: str
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: str
    """Completions for first quartile of video views."""
    video_midpoint_completions: str
    """Completions for midpoint of video views."""
    video_starts: str
    """Total video starts initiated by users."""
    video_third_quartile_completions: str
    """Completions for third quartile of video views."""
    video_views: str
    """Total views of videos in the ad."""
    viral_card_clicks: str
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: str
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: str
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: str
    """Likes received on comments in viral distribution."""
    viral_comments: str
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: str
    """Clicks on the company page in viral distribution."""
    viral_document_completions: str
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: str
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: str
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: str
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: str
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: str
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: str
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: str
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: str
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: str
    """Fullscreen video plays in viral distribution."""
    viral_impressions: str
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: str
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: str
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: str
    """Clicks on landing page in viral distribution."""
    viral_likes: str
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: str
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: str
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: str
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: str
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: str
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: str
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: str
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: str
    """Total reactions in viral distribution of the ad."""
    viral_registrations: str
    """Total registrations in viral distribution of the ad."""
    viral_shares: str
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: str
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: str
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: str
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: str
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: str
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: str
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: str
    """Total views of videos in viral distribution of the ad."""
    pivot: str
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberIndustryAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_member_industry_analytics search results."""
    action_clicks: AirbyteSortOrder
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: AirbyteSortOrder
    """The number of clicks on ad unit components."""
    approximate_member_reach: AirbyteSortOrder
    """An approximation of unique ad impressions."""
    card_clicks: AirbyteSortOrder
    """The number of clicks on interactive card elements."""
    card_impressions: AirbyteSortOrder
    """The number of times interactive cards were displayed."""
    clicks: AirbyteSortOrder
    """Total number of clicks on the ad."""
    comment_likes: AirbyteSortOrder
    """The count of likes on comments related to the ad."""
    comments: AirbyteSortOrder
    """The number of comments on the ad."""
    company_page_clicks: AirbyteSortOrder
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in the local currency."""
    cost_in_local_currency: AirbyteSortOrder
    """Cost of ad campaign in the local currency."""
    cost_in_usd: AirbyteSortOrder
    """Cost of ad campaign in USD."""
    document_completions: AirbyteSortOrder
    """Number of completions for document views."""
    document_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of document views."""
    document_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of document views."""
    document_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of document views."""
    download_clicks: AirbyteSortOrder
    """Clicks on download links in the ad."""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data."""
    external_website_conversions: AirbyteSortOrder
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites."""
    follows: AirbyteSortOrder
    """Number of follows generated by the ad."""
    full_screen_plays: AirbyteSortOrder
    """Number of times videos were played in fullscreen mode."""
    impressions: AirbyteSortOrder
    """Total number of times the ad was displayed."""
    job_applications: AirbyteSortOrder
    """Number of job applications initiated through the ad."""
    job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in the ad."""
    landing_page_clicks: AirbyteSortOrder
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: AirbyteSortOrder
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: AirbyteSortOrder
    """Clicks on expressing interest through lead generation mail."""
    likes: AirbyteSortOrder
    """Total likes received on the ad."""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of times lead forms were opened in one click."""
    one_click_leads: AirbyteSortOrder
    """Leads generated in one click."""
    opens: AirbyteSortOrder
    """The number of times the ad was opened or expanded."""
    other_engagements: AirbyteSortOrder
    """Engagements other than clicks on the ad."""
    pivot_values: AirbyteSortOrder
    """Values used for pivoting the analytics."""
    string_of_pivot_values: AirbyteSortOrder
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing the ad."""
    reactions: AirbyteSortOrder
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: AirbyteSortOrder
    """Total registrations completed through the ad."""
    sends: AirbyteSortOrder
    """Number of messages sent through the ad."""
    shares: AirbyteSortOrder
    """Total shares generated by the ad."""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data."""
    talent_leads: AirbyteSortOrder
    """Number of leads related to talent acquisition."""
    text_url_clicks: AirbyteSortOrder
    """Clicks on text URLs within the ad."""
    total_engagements: AirbyteSortOrder
    """Total number of engagements on the ad."""
    valid_work_email_leads: AirbyteSortOrder
    """Leads generated through valid work emails."""
    video_completions: AirbyteSortOrder
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of video views."""
    video_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of video views."""
    video_starts: AirbyteSortOrder
    """Total video starts initiated by users."""
    video_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of video views."""
    video_views: AirbyteSortOrder
    """Total views of videos in the ad."""
    viral_card_clicks: AirbyteSortOrder
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: AirbyteSortOrder
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: AirbyteSortOrder
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: AirbyteSortOrder
    """Likes received on comments in viral distribution."""
    viral_comments: AirbyteSortOrder
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: AirbyteSortOrder
    """Clicks on the company page in viral distribution."""
    viral_document_completions: AirbyteSortOrder
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: AirbyteSortOrder
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: AirbyteSortOrder
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: AirbyteSortOrder
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: AirbyteSortOrder
    """Fullscreen video plays in viral distribution."""
    viral_impressions: AirbyteSortOrder
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: AirbyteSortOrder
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: AirbyteSortOrder
    """Clicks on landing page in viral distribution."""
    viral_likes: AirbyteSortOrder
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: AirbyteSortOrder
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: AirbyteSortOrder
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: AirbyteSortOrder
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: AirbyteSortOrder
    """Total reactions in viral distribution of the ad."""
    viral_registrations: AirbyteSortOrder
    """Total registrations in viral distribution of the ad."""
    viral_shares: AirbyteSortOrder
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: AirbyteSortOrder
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: AirbyteSortOrder
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: AirbyteSortOrder
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: AirbyteSortOrder
    """Total views of videos in viral distribution of the ad."""
    pivot: AirbyteSortOrder
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: AirbyteSortOrder
    """URN of the sponsored campaign this analytics record belongs to"""


# Entity-specific condition types for ad_member_industry_analytics
class AdMemberIndustryAnalyticsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdMemberIndustryAnalyticsSearchFilter


class AdMemberIndustryAnalyticsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdMemberIndustryAnalyticsSearchFilter


class AdMemberIndustryAnalyticsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdMemberIndustryAnalyticsSearchFilter


class AdMemberIndustryAnalyticsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdMemberIndustryAnalyticsSearchFilter


class AdMemberIndustryAnalyticsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdMemberIndustryAnalyticsSearchFilter


class AdMemberIndustryAnalyticsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdMemberIndustryAnalyticsSearchFilter


class AdMemberIndustryAnalyticsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AdMemberIndustryAnalyticsStringFilter


class AdMemberIndustryAnalyticsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AdMemberIndustryAnalyticsStringFilter


class AdMemberIndustryAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdMemberIndustryAnalyticsStringFilter


class AdMemberIndustryAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdMemberIndustryAnalyticsStringFilter


class AdMemberIndustryAnalyticsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: AdMemberIndustryAnalyticsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdMemberIndustryAnalyticsInCondition = TypedDict("AdMemberIndustryAnalyticsInCondition", {"in": AdMemberIndustryAnalyticsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdMemberIndustryAnalyticsNotCondition = TypedDict("AdMemberIndustryAnalyticsNotCondition", {"not": "AdMemberIndustryAnalyticsCondition"}, total=False)
"""Negates the nested condition."""

AdMemberIndustryAnalyticsAndCondition = TypedDict("AdMemberIndustryAnalyticsAndCondition", {"and": "list[AdMemberIndustryAnalyticsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdMemberIndustryAnalyticsOrCondition = TypedDict("AdMemberIndustryAnalyticsOrCondition", {"or": "list[AdMemberIndustryAnalyticsCondition]"}, total=False)
"""True if any nested condition is true."""

AdMemberIndustryAnalyticsAnyCondition = TypedDict("AdMemberIndustryAnalyticsAnyCondition", {"any": AdMemberIndustryAnalyticsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_member_industry_analytics condition types
AdMemberIndustryAnalyticsCondition = (
    AdMemberIndustryAnalyticsEqCondition
    | AdMemberIndustryAnalyticsNeqCondition
    | AdMemberIndustryAnalyticsGtCondition
    | AdMemberIndustryAnalyticsGteCondition
    | AdMemberIndustryAnalyticsLtCondition
    | AdMemberIndustryAnalyticsLteCondition
    | AdMemberIndustryAnalyticsInCondition
    | AdMemberIndustryAnalyticsStartswithCondition
    | AdMemberIndustryAnalyticsEndswithCondition
    | AdMemberIndustryAnalyticsFuzzyCondition
    | AdMemberIndustryAnalyticsKeywordCondition
    | AdMemberIndustryAnalyticsContainsCondition
    | AdMemberIndustryAnalyticsNotCondition
    | AdMemberIndustryAnalyticsAndCondition
    | AdMemberIndustryAnalyticsOrCondition
    | AdMemberIndustryAnalyticsAnyCondition
)


class AdMemberIndustryAnalyticsSearchQuery(TypedDict, total=False):
    """Search query for ad_member_industry_analytics entity."""
    filter: AdMemberIndustryAnalyticsCondition
    sort: list[AdMemberIndustryAnalyticsSortFilter]


# ===== AD_MEMBER_JOB_FUNCTION_ANALYTICS SEARCH TYPES =====

class AdMemberJobFunctionAnalyticsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_member_job_function_analytics search queries."""
    action_clicks: float | None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None
    """An approximation of unique ad impressions."""
    card_clicks: float | None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None
    """The number of times interactive cards were displayed."""
    clicks: float | None
    """Total number of clicks on the ad."""
    comment_likes: float | None
    """The count of likes on comments related to the ad."""
    comments: float | None
    """The number of comments on the ad."""
    company_page_clicks: float | None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None
    """Cost of ad campaign in USD."""
    document_completions: float | None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None
    """Completions for third quartile of document views."""
    download_clicks: float | None
    """Clicks on download links in the ad."""
    end_date: str | None
    """End date of the ad analytics data."""
    external_website_conversions: float | None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites."""
    follows: float | None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None
    """Total number of times the ad was displayed."""
    job_applications: float | None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None
    """Leads generated in one click."""
    opens: float | None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None
    """Registrations completed post-viewing the ad."""
    reactions: float | None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None
    """Total registrations completed through the ad."""
    sends: float | None
    """Number of messages sent through the ad."""
    shares: float | None
    """Total shares generated by the ad."""
    start_date: str | None
    """Start date of the ad analytics data."""
    talent_leads: float | None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None
    """Leads generated through valid work emails."""
    video_completions: float | None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None
    """Completions for midpoint of video views."""
    video_starts: float | None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None
    """Completions for third quartile of video views."""
    video_views: float | None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberJobFunctionAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    action_clicks: list[float]
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: list[float]
    """The number of clicks on ad unit components."""
    approximate_member_reach: list[float]
    """An approximation of unique ad impressions."""
    card_clicks: list[float]
    """The number of clicks on interactive card elements."""
    card_impressions: list[float]
    """The number of times interactive cards were displayed."""
    clicks: list[float]
    """Total number of clicks on the ad."""
    comment_likes: list[float]
    """The count of likes on comments related to the ad."""
    comments: list[float]
    """The number of comments on the ad."""
    company_page_clicks: list[float]
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: list[float]
    """Conversion value in the local currency."""
    cost_in_local_currency: list[float]
    """Cost of ad campaign in the local currency."""
    cost_in_usd: list[float]
    """Cost of ad campaign in USD."""
    document_completions: list[float]
    """Number of completions for document views."""
    document_first_quartile_completions: list[float]
    """Completions for first quartile of document views."""
    document_midpoint_completions: list[float]
    """Completions for midpoint of document views."""
    document_third_quartile_completions: list[float]
    """Completions for third quartile of document views."""
    download_clicks: list[float]
    """Clicks on download links in the ad."""
    end_date: list[str]
    """End date of the ad analytics data."""
    external_website_conversions: list[float]
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites."""
    follows: list[float]
    """Number of follows generated by the ad."""
    full_screen_plays: list[float]
    """Number of times videos were played in fullscreen mode."""
    impressions: list[float]
    """Total number of times the ad was displayed."""
    job_applications: list[float]
    """Number of job applications initiated through the ad."""
    job_apply_clicks: list[float]
    """Clicks on apply job button in the ad."""
    landing_page_clicks: list[float]
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: list[float]
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: list[float]
    """Clicks on expressing interest through lead generation mail."""
    likes: list[float]
    """Total likes received on the ad."""
    one_click_lead_form_opens: list[float]
    """Number of times lead forms were opened in one click."""
    one_click_leads: list[float]
    """Leads generated in one click."""
    opens: list[float]
    """The number of times the ad was opened or expanded."""
    other_engagements: list[float]
    """Engagements other than clicks on the ad."""
    pivot_values: list[list[Any]]
    """Values used for pivoting the analytics."""
    string_of_pivot_values: list[str]
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: list[float]
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: list[float]
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: list[float]
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: list[float]
    """Registrations completed post-viewing the ad."""
    reactions: list[float]
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: list[float]
    """Total registrations completed through the ad."""
    sends: list[float]
    """Number of messages sent through the ad."""
    shares: list[float]
    """Total shares generated by the ad."""
    start_date: list[str]
    """Start date of the ad analytics data."""
    talent_leads: list[float]
    """Number of leads related to talent acquisition."""
    text_url_clicks: list[float]
    """Clicks on text URLs within the ad."""
    total_engagements: list[float]
    """Total number of engagements on the ad."""
    valid_work_email_leads: list[float]
    """Leads generated through valid work emails."""
    video_completions: list[float]
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: list[float]
    """Completions for first quartile of video views."""
    video_midpoint_completions: list[float]
    """Completions for midpoint of video views."""
    video_starts: list[float]
    """Total video starts initiated by users."""
    video_third_quartile_completions: list[float]
    """Completions for third quartile of video views."""
    video_views: list[float]
    """Total views of videos in the ad."""
    viral_card_clicks: list[float]
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: list[float]
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: list[float]
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: list[float]
    """Likes received on comments in viral distribution."""
    viral_comments: list[float]
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: list[float]
    """Clicks on the company page in viral distribution."""
    viral_document_completions: list[float]
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: list[float]
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: list[float]
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: list[float]
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: list[float]
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: list[float]
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: list[float]
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: list[float]
    """Fullscreen video plays in viral distribution."""
    viral_impressions: list[float]
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: list[float]
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: list[float]
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: list[float]
    """Clicks on landing page in viral distribution."""
    viral_likes: list[float]
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: list[float]
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: list[float]
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: list[float]
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: list[float]
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: list[float]
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: list[float]
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: list[float]
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: list[float]
    """Total reactions in viral distribution of the ad."""
    viral_registrations: list[float]
    """Total registrations in viral distribution of the ad."""
    viral_shares: list[float]
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: list[float]
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: list[float]
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: list[float]
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: list[float]
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: list[float]
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: list[float]
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: list[float]
    """Total views of videos in viral distribution of the ad."""
    pivot: list[str]
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: list[str]
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberJobFunctionAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    action_clicks: Any
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: Any
    """The number of clicks on ad unit components."""
    approximate_member_reach: Any
    """An approximation of unique ad impressions."""
    card_clicks: Any
    """The number of clicks on interactive card elements."""
    card_impressions: Any
    """The number of times interactive cards were displayed."""
    clicks: Any
    """Total number of clicks on the ad."""
    comment_likes: Any
    """The count of likes on comments related to the ad."""
    comments: Any
    """The number of comments on the ad."""
    company_page_clicks: Any
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: Any
    """Conversion value in the local currency."""
    cost_in_local_currency: Any
    """Cost of ad campaign in the local currency."""
    cost_in_usd: Any
    """Cost of ad campaign in USD."""
    document_completions: Any
    """Number of completions for document views."""
    document_first_quartile_completions: Any
    """Completions for first quartile of document views."""
    document_midpoint_completions: Any
    """Completions for midpoint of document views."""
    document_third_quartile_completions: Any
    """Completions for third quartile of document views."""
    download_clicks: Any
    """Clicks on download links in the ad."""
    end_date: Any
    """End date of the ad analytics data."""
    external_website_conversions: Any
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites."""
    follows: Any
    """Number of follows generated by the ad."""
    full_screen_plays: Any
    """Number of times videos were played in fullscreen mode."""
    impressions: Any
    """Total number of times the ad was displayed."""
    job_applications: Any
    """Number of job applications initiated through the ad."""
    job_apply_clicks: Any
    """Clicks on apply job button in the ad."""
    landing_page_clicks: Any
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: Any
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: Any
    """Clicks on expressing interest through lead generation mail."""
    likes: Any
    """Total likes received on the ad."""
    one_click_lead_form_opens: Any
    """Number of times lead forms were opened in one click."""
    one_click_leads: Any
    """Leads generated in one click."""
    opens: Any
    """The number of times the ad was opened or expanded."""
    other_engagements: Any
    """Engagements other than clicks on the ad."""
    pivot_values: Any
    """Values used for pivoting the analytics."""
    string_of_pivot_values: Any
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: Any
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: Any
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: Any
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: Any
    """Registrations completed post-viewing the ad."""
    reactions: Any
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: Any
    """Total registrations completed through the ad."""
    sends: Any
    """Number of messages sent through the ad."""
    shares: Any
    """Total shares generated by the ad."""
    start_date: Any
    """Start date of the ad analytics data."""
    talent_leads: Any
    """Number of leads related to talent acquisition."""
    text_url_clicks: Any
    """Clicks on text URLs within the ad."""
    total_engagements: Any
    """Total number of engagements on the ad."""
    valid_work_email_leads: Any
    """Leads generated through valid work emails."""
    video_completions: Any
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: Any
    """Completions for first quartile of video views."""
    video_midpoint_completions: Any
    """Completions for midpoint of video views."""
    video_starts: Any
    """Total video starts initiated by users."""
    video_third_quartile_completions: Any
    """Completions for third quartile of video views."""
    video_views: Any
    """Total views of videos in the ad."""
    viral_card_clicks: Any
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: Any
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: Any
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: Any
    """Likes received on comments in viral distribution."""
    viral_comments: Any
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: Any
    """Clicks on the company page in viral distribution."""
    viral_document_completions: Any
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: Any
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: Any
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: Any
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: Any
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: Any
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: Any
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: Any
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: Any
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: Any
    """Fullscreen video plays in viral distribution."""
    viral_impressions: Any
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: Any
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: Any
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: Any
    """Clicks on landing page in viral distribution."""
    viral_likes: Any
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: Any
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: Any
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: Any
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: Any
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: Any
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: Any
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: Any
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: Any
    """Total reactions in viral distribution of the ad."""
    viral_registrations: Any
    """Total registrations in viral distribution of the ad."""
    viral_shares: Any
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: Any
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: Any
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: Any
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: Any
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: Any
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: Any
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: Any
    """Total views of videos in viral distribution of the ad."""
    pivot: Any
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: Any
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberJobFunctionAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    action_clicks: str
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: str
    """The number of clicks on ad unit components."""
    approximate_member_reach: str
    """An approximation of unique ad impressions."""
    card_clicks: str
    """The number of clicks on interactive card elements."""
    card_impressions: str
    """The number of times interactive cards were displayed."""
    clicks: str
    """Total number of clicks on the ad."""
    comment_likes: str
    """The count of likes on comments related to the ad."""
    comments: str
    """The number of comments on the ad."""
    company_page_clicks: str
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: str
    """Conversion value in the local currency."""
    cost_in_local_currency: str
    """Cost of ad campaign in the local currency."""
    cost_in_usd: str
    """Cost of ad campaign in USD."""
    document_completions: str
    """Number of completions for document views."""
    document_first_quartile_completions: str
    """Completions for first quartile of document views."""
    document_midpoint_completions: str
    """Completions for midpoint of document views."""
    document_third_quartile_completions: str
    """Completions for third quartile of document views."""
    download_clicks: str
    """Clicks on download links in the ad."""
    end_date: str
    """End date of the ad analytics data."""
    external_website_conversions: str
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites."""
    follows: str
    """Number of follows generated by the ad."""
    full_screen_plays: str
    """Number of times videos were played in fullscreen mode."""
    impressions: str
    """Total number of times the ad was displayed."""
    job_applications: str
    """Number of job applications initiated through the ad."""
    job_apply_clicks: str
    """Clicks on apply job button in the ad."""
    landing_page_clicks: str
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: str
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: str
    """Clicks on expressing interest through lead generation mail."""
    likes: str
    """Total likes received on the ad."""
    one_click_lead_form_opens: str
    """Number of times lead forms were opened in one click."""
    one_click_leads: str
    """Leads generated in one click."""
    opens: str
    """The number of times the ad was opened or expanded."""
    other_engagements: str
    """Engagements other than clicks on the ad."""
    pivot_values: str
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: str
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: str
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: str
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: str
    """Registrations completed post-viewing the ad."""
    reactions: str
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: str
    """Total registrations completed through the ad."""
    sends: str
    """Number of messages sent through the ad."""
    shares: str
    """Total shares generated by the ad."""
    start_date: str
    """Start date of the ad analytics data."""
    talent_leads: str
    """Number of leads related to talent acquisition."""
    text_url_clicks: str
    """Clicks on text URLs within the ad."""
    total_engagements: str
    """Total number of engagements on the ad."""
    valid_work_email_leads: str
    """Leads generated through valid work emails."""
    video_completions: str
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: str
    """Completions for first quartile of video views."""
    video_midpoint_completions: str
    """Completions for midpoint of video views."""
    video_starts: str
    """Total video starts initiated by users."""
    video_third_quartile_completions: str
    """Completions for third quartile of video views."""
    video_views: str
    """Total views of videos in the ad."""
    viral_card_clicks: str
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: str
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: str
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: str
    """Likes received on comments in viral distribution."""
    viral_comments: str
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: str
    """Clicks on the company page in viral distribution."""
    viral_document_completions: str
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: str
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: str
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: str
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: str
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: str
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: str
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: str
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: str
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: str
    """Fullscreen video plays in viral distribution."""
    viral_impressions: str
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: str
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: str
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: str
    """Clicks on landing page in viral distribution."""
    viral_likes: str
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: str
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: str
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: str
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: str
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: str
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: str
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: str
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: str
    """Total reactions in viral distribution of the ad."""
    viral_registrations: str
    """Total registrations in viral distribution of the ad."""
    viral_shares: str
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: str
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: str
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: str
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: str
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: str
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: str
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: str
    """Total views of videos in viral distribution of the ad."""
    pivot: str
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberJobFunctionAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_member_job_function_analytics search results."""
    action_clicks: AirbyteSortOrder
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: AirbyteSortOrder
    """The number of clicks on ad unit components."""
    approximate_member_reach: AirbyteSortOrder
    """An approximation of unique ad impressions."""
    card_clicks: AirbyteSortOrder
    """The number of clicks on interactive card elements."""
    card_impressions: AirbyteSortOrder
    """The number of times interactive cards were displayed."""
    clicks: AirbyteSortOrder
    """Total number of clicks on the ad."""
    comment_likes: AirbyteSortOrder
    """The count of likes on comments related to the ad."""
    comments: AirbyteSortOrder
    """The number of comments on the ad."""
    company_page_clicks: AirbyteSortOrder
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in the local currency."""
    cost_in_local_currency: AirbyteSortOrder
    """Cost of ad campaign in the local currency."""
    cost_in_usd: AirbyteSortOrder
    """Cost of ad campaign in USD."""
    document_completions: AirbyteSortOrder
    """Number of completions for document views."""
    document_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of document views."""
    document_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of document views."""
    document_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of document views."""
    download_clicks: AirbyteSortOrder
    """Clicks on download links in the ad."""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data."""
    external_website_conversions: AirbyteSortOrder
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites."""
    follows: AirbyteSortOrder
    """Number of follows generated by the ad."""
    full_screen_plays: AirbyteSortOrder
    """Number of times videos were played in fullscreen mode."""
    impressions: AirbyteSortOrder
    """Total number of times the ad was displayed."""
    job_applications: AirbyteSortOrder
    """Number of job applications initiated through the ad."""
    job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in the ad."""
    landing_page_clicks: AirbyteSortOrder
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: AirbyteSortOrder
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: AirbyteSortOrder
    """Clicks on expressing interest through lead generation mail."""
    likes: AirbyteSortOrder
    """Total likes received on the ad."""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of times lead forms were opened in one click."""
    one_click_leads: AirbyteSortOrder
    """Leads generated in one click."""
    opens: AirbyteSortOrder
    """The number of times the ad was opened or expanded."""
    other_engagements: AirbyteSortOrder
    """Engagements other than clicks on the ad."""
    pivot_values: AirbyteSortOrder
    """Values used for pivoting the analytics."""
    string_of_pivot_values: AirbyteSortOrder
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing the ad."""
    reactions: AirbyteSortOrder
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: AirbyteSortOrder
    """Total registrations completed through the ad."""
    sends: AirbyteSortOrder
    """Number of messages sent through the ad."""
    shares: AirbyteSortOrder
    """Total shares generated by the ad."""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data."""
    talent_leads: AirbyteSortOrder
    """Number of leads related to talent acquisition."""
    text_url_clicks: AirbyteSortOrder
    """Clicks on text URLs within the ad."""
    total_engagements: AirbyteSortOrder
    """Total number of engagements on the ad."""
    valid_work_email_leads: AirbyteSortOrder
    """Leads generated through valid work emails."""
    video_completions: AirbyteSortOrder
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of video views."""
    video_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of video views."""
    video_starts: AirbyteSortOrder
    """Total video starts initiated by users."""
    video_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of video views."""
    video_views: AirbyteSortOrder
    """Total views of videos in the ad."""
    viral_card_clicks: AirbyteSortOrder
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: AirbyteSortOrder
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: AirbyteSortOrder
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: AirbyteSortOrder
    """Likes received on comments in viral distribution."""
    viral_comments: AirbyteSortOrder
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: AirbyteSortOrder
    """Clicks on the company page in viral distribution."""
    viral_document_completions: AirbyteSortOrder
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: AirbyteSortOrder
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: AirbyteSortOrder
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: AirbyteSortOrder
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: AirbyteSortOrder
    """Fullscreen video plays in viral distribution."""
    viral_impressions: AirbyteSortOrder
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: AirbyteSortOrder
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: AirbyteSortOrder
    """Clicks on landing page in viral distribution."""
    viral_likes: AirbyteSortOrder
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: AirbyteSortOrder
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: AirbyteSortOrder
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: AirbyteSortOrder
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: AirbyteSortOrder
    """Total reactions in viral distribution of the ad."""
    viral_registrations: AirbyteSortOrder
    """Total registrations in viral distribution of the ad."""
    viral_shares: AirbyteSortOrder
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: AirbyteSortOrder
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: AirbyteSortOrder
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: AirbyteSortOrder
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: AirbyteSortOrder
    """Total views of videos in viral distribution of the ad."""
    pivot: AirbyteSortOrder
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: AirbyteSortOrder
    """URN of the sponsored campaign this analytics record belongs to"""


# Entity-specific condition types for ad_member_job_function_analytics
class AdMemberJobFunctionAnalyticsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdMemberJobFunctionAnalyticsSearchFilter


class AdMemberJobFunctionAnalyticsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdMemberJobFunctionAnalyticsSearchFilter


class AdMemberJobFunctionAnalyticsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdMemberJobFunctionAnalyticsSearchFilter


class AdMemberJobFunctionAnalyticsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdMemberJobFunctionAnalyticsSearchFilter


class AdMemberJobFunctionAnalyticsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdMemberJobFunctionAnalyticsSearchFilter


class AdMemberJobFunctionAnalyticsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdMemberJobFunctionAnalyticsSearchFilter


class AdMemberJobFunctionAnalyticsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AdMemberJobFunctionAnalyticsStringFilter


class AdMemberJobFunctionAnalyticsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AdMemberJobFunctionAnalyticsStringFilter


class AdMemberJobFunctionAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdMemberJobFunctionAnalyticsStringFilter


class AdMemberJobFunctionAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdMemberJobFunctionAnalyticsStringFilter


class AdMemberJobFunctionAnalyticsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: AdMemberJobFunctionAnalyticsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdMemberJobFunctionAnalyticsInCondition = TypedDict("AdMemberJobFunctionAnalyticsInCondition", {"in": AdMemberJobFunctionAnalyticsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdMemberJobFunctionAnalyticsNotCondition = TypedDict("AdMemberJobFunctionAnalyticsNotCondition", {"not": "AdMemberJobFunctionAnalyticsCondition"}, total=False)
"""Negates the nested condition."""

AdMemberJobFunctionAnalyticsAndCondition = TypedDict("AdMemberJobFunctionAnalyticsAndCondition", {"and": "list[AdMemberJobFunctionAnalyticsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdMemberJobFunctionAnalyticsOrCondition = TypedDict("AdMemberJobFunctionAnalyticsOrCondition", {"or": "list[AdMemberJobFunctionAnalyticsCondition]"}, total=False)
"""True if any nested condition is true."""

AdMemberJobFunctionAnalyticsAnyCondition = TypedDict("AdMemberJobFunctionAnalyticsAnyCondition", {"any": AdMemberJobFunctionAnalyticsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_member_job_function_analytics condition types
AdMemberJobFunctionAnalyticsCondition = (
    AdMemberJobFunctionAnalyticsEqCondition
    | AdMemberJobFunctionAnalyticsNeqCondition
    | AdMemberJobFunctionAnalyticsGtCondition
    | AdMemberJobFunctionAnalyticsGteCondition
    | AdMemberJobFunctionAnalyticsLtCondition
    | AdMemberJobFunctionAnalyticsLteCondition
    | AdMemberJobFunctionAnalyticsInCondition
    | AdMemberJobFunctionAnalyticsStartswithCondition
    | AdMemberJobFunctionAnalyticsEndswithCondition
    | AdMemberJobFunctionAnalyticsFuzzyCondition
    | AdMemberJobFunctionAnalyticsKeywordCondition
    | AdMemberJobFunctionAnalyticsContainsCondition
    | AdMemberJobFunctionAnalyticsNotCondition
    | AdMemberJobFunctionAnalyticsAndCondition
    | AdMemberJobFunctionAnalyticsOrCondition
    | AdMemberJobFunctionAnalyticsAnyCondition
)


class AdMemberJobFunctionAnalyticsSearchQuery(TypedDict, total=False):
    """Search query for ad_member_job_function_analytics entity."""
    filter: AdMemberJobFunctionAnalyticsCondition
    sort: list[AdMemberJobFunctionAnalyticsSortFilter]


# ===== AD_MEMBER_JOB_TITLE_ANALYTICS SEARCH TYPES =====

class AdMemberJobTitleAnalyticsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_member_job_title_analytics search queries."""
    action_clicks: float | None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None
    """An approximation of unique ad impressions."""
    card_clicks: float | None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None
    """The number of times interactive cards were displayed."""
    clicks: float | None
    """Total number of clicks on the ad."""
    comment_likes: float | None
    """The count of likes on comments related to the ad."""
    comments: float | None
    """The number of comments on the ad."""
    company_page_clicks: float | None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None
    """Cost of ad campaign in USD."""
    document_completions: float | None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None
    """Completions for third quartile of document views."""
    download_clicks: float | None
    """Clicks on download links in the ad."""
    end_date: str | None
    """End date of the ad analytics data."""
    external_website_conversions: float | None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites."""
    follows: float | None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None
    """Total number of times the ad was displayed."""
    job_applications: float | None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None
    """Leads generated in one click."""
    opens: float | None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None
    """Registrations completed post-viewing the ad."""
    reactions: float | None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None
    """Total registrations completed through the ad."""
    sends: float | None
    """Number of messages sent through the ad."""
    shares: float | None
    """Total shares generated by the ad."""
    start_date: str | None
    """Start date of the ad analytics data."""
    talent_leads: float | None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None
    """Leads generated through valid work emails."""
    video_completions: float | None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None
    """Completions for midpoint of video views."""
    video_starts: float | None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None
    """Completions for third quartile of video views."""
    video_views: float | None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberJobTitleAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    action_clicks: list[float]
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: list[float]
    """The number of clicks on ad unit components."""
    approximate_member_reach: list[float]
    """An approximation of unique ad impressions."""
    card_clicks: list[float]
    """The number of clicks on interactive card elements."""
    card_impressions: list[float]
    """The number of times interactive cards were displayed."""
    clicks: list[float]
    """Total number of clicks on the ad."""
    comment_likes: list[float]
    """The count of likes on comments related to the ad."""
    comments: list[float]
    """The number of comments on the ad."""
    company_page_clicks: list[float]
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: list[float]
    """Conversion value in the local currency."""
    cost_in_local_currency: list[float]
    """Cost of ad campaign in the local currency."""
    cost_in_usd: list[float]
    """Cost of ad campaign in USD."""
    document_completions: list[float]
    """Number of completions for document views."""
    document_first_quartile_completions: list[float]
    """Completions for first quartile of document views."""
    document_midpoint_completions: list[float]
    """Completions for midpoint of document views."""
    document_third_quartile_completions: list[float]
    """Completions for third quartile of document views."""
    download_clicks: list[float]
    """Clicks on download links in the ad."""
    end_date: list[str]
    """End date of the ad analytics data."""
    external_website_conversions: list[float]
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites."""
    follows: list[float]
    """Number of follows generated by the ad."""
    full_screen_plays: list[float]
    """Number of times videos were played in fullscreen mode."""
    impressions: list[float]
    """Total number of times the ad was displayed."""
    job_applications: list[float]
    """Number of job applications initiated through the ad."""
    job_apply_clicks: list[float]
    """Clicks on apply job button in the ad."""
    landing_page_clicks: list[float]
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: list[float]
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: list[float]
    """Clicks on expressing interest through lead generation mail."""
    likes: list[float]
    """Total likes received on the ad."""
    one_click_lead_form_opens: list[float]
    """Number of times lead forms were opened in one click."""
    one_click_leads: list[float]
    """Leads generated in one click."""
    opens: list[float]
    """The number of times the ad was opened or expanded."""
    other_engagements: list[float]
    """Engagements other than clicks on the ad."""
    pivot_values: list[list[Any]]
    """Values used for pivoting the analytics."""
    string_of_pivot_values: list[str]
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: list[float]
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: list[float]
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: list[float]
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: list[float]
    """Registrations completed post-viewing the ad."""
    reactions: list[float]
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: list[float]
    """Total registrations completed through the ad."""
    sends: list[float]
    """Number of messages sent through the ad."""
    shares: list[float]
    """Total shares generated by the ad."""
    start_date: list[str]
    """Start date of the ad analytics data."""
    talent_leads: list[float]
    """Number of leads related to talent acquisition."""
    text_url_clicks: list[float]
    """Clicks on text URLs within the ad."""
    total_engagements: list[float]
    """Total number of engagements on the ad."""
    valid_work_email_leads: list[float]
    """Leads generated through valid work emails."""
    video_completions: list[float]
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: list[float]
    """Completions for first quartile of video views."""
    video_midpoint_completions: list[float]
    """Completions for midpoint of video views."""
    video_starts: list[float]
    """Total video starts initiated by users."""
    video_third_quartile_completions: list[float]
    """Completions for third quartile of video views."""
    video_views: list[float]
    """Total views of videos in the ad."""
    viral_card_clicks: list[float]
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: list[float]
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: list[float]
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: list[float]
    """Likes received on comments in viral distribution."""
    viral_comments: list[float]
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: list[float]
    """Clicks on the company page in viral distribution."""
    viral_document_completions: list[float]
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: list[float]
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: list[float]
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: list[float]
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: list[float]
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: list[float]
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: list[float]
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: list[float]
    """Fullscreen video plays in viral distribution."""
    viral_impressions: list[float]
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: list[float]
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: list[float]
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: list[float]
    """Clicks on landing page in viral distribution."""
    viral_likes: list[float]
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: list[float]
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: list[float]
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: list[float]
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: list[float]
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: list[float]
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: list[float]
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: list[float]
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: list[float]
    """Total reactions in viral distribution of the ad."""
    viral_registrations: list[float]
    """Total registrations in viral distribution of the ad."""
    viral_shares: list[float]
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: list[float]
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: list[float]
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: list[float]
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: list[float]
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: list[float]
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: list[float]
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: list[float]
    """Total views of videos in viral distribution of the ad."""
    pivot: list[str]
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: list[str]
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberJobTitleAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    action_clicks: Any
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: Any
    """The number of clicks on ad unit components."""
    approximate_member_reach: Any
    """An approximation of unique ad impressions."""
    card_clicks: Any
    """The number of clicks on interactive card elements."""
    card_impressions: Any
    """The number of times interactive cards were displayed."""
    clicks: Any
    """Total number of clicks on the ad."""
    comment_likes: Any
    """The count of likes on comments related to the ad."""
    comments: Any
    """The number of comments on the ad."""
    company_page_clicks: Any
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: Any
    """Conversion value in the local currency."""
    cost_in_local_currency: Any
    """Cost of ad campaign in the local currency."""
    cost_in_usd: Any
    """Cost of ad campaign in USD."""
    document_completions: Any
    """Number of completions for document views."""
    document_first_quartile_completions: Any
    """Completions for first quartile of document views."""
    document_midpoint_completions: Any
    """Completions for midpoint of document views."""
    document_third_quartile_completions: Any
    """Completions for third quartile of document views."""
    download_clicks: Any
    """Clicks on download links in the ad."""
    end_date: Any
    """End date of the ad analytics data."""
    external_website_conversions: Any
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites."""
    follows: Any
    """Number of follows generated by the ad."""
    full_screen_plays: Any
    """Number of times videos were played in fullscreen mode."""
    impressions: Any
    """Total number of times the ad was displayed."""
    job_applications: Any
    """Number of job applications initiated through the ad."""
    job_apply_clicks: Any
    """Clicks on apply job button in the ad."""
    landing_page_clicks: Any
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: Any
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: Any
    """Clicks on expressing interest through lead generation mail."""
    likes: Any
    """Total likes received on the ad."""
    one_click_lead_form_opens: Any
    """Number of times lead forms were opened in one click."""
    one_click_leads: Any
    """Leads generated in one click."""
    opens: Any
    """The number of times the ad was opened or expanded."""
    other_engagements: Any
    """Engagements other than clicks on the ad."""
    pivot_values: Any
    """Values used for pivoting the analytics."""
    string_of_pivot_values: Any
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: Any
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: Any
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: Any
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: Any
    """Registrations completed post-viewing the ad."""
    reactions: Any
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: Any
    """Total registrations completed through the ad."""
    sends: Any
    """Number of messages sent through the ad."""
    shares: Any
    """Total shares generated by the ad."""
    start_date: Any
    """Start date of the ad analytics data."""
    talent_leads: Any
    """Number of leads related to talent acquisition."""
    text_url_clicks: Any
    """Clicks on text URLs within the ad."""
    total_engagements: Any
    """Total number of engagements on the ad."""
    valid_work_email_leads: Any
    """Leads generated through valid work emails."""
    video_completions: Any
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: Any
    """Completions for first quartile of video views."""
    video_midpoint_completions: Any
    """Completions for midpoint of video views."""
    video_starts: Any
    """Total video starts initiated by users."""
    video_third_quartile_completions: Any
    """Completions for third quartile of video views."""
    video_views: Any
    """Total views of videos in the ad."""
    viral_card_clicks: Any
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: Any
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: Any
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: Any
    """Likes received on comments in viral distribution."""
    viral_comments: Any
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: Any
    """Clicks on the company page in viral distribution."""
    viral_document_completions: Any
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: Any
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: Any
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: Any
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: Any
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: Any
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: Any
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: Any
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: Any
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: Any
    """Fullscreen video plays in viral distribution."""
    viral_impressions: Any
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: Any
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: Any
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: Any
    """Clicks on landing page in viral distribution."""
    viral_likes: Any
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: Any
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: Any
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: Any
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: Any
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: Any
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: Any
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: Any
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: Any
    """Total reactions in viral distribution of the ad."""
    viral_registrations: Any
    """Total registrations in viral distribution of the ad."""
    viral_shares: Any
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: Any
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: Any
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: Any
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: Any
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: Any
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: Any
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: Any
    """Total views of videos in viral distribution of the ad."""
    pivot: Any
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: Any
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberJobTitleAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    action_clicks: str
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: str
    """The number of clicks on ad unit components."""
    approximate_member_reach: str
    """An approximation of unique ad impressions."""
    card_clicks: str
    """The number of clicks on interactive card elements."""
    card_impressions: str
    """The number of times interactive cards were displayed."""
    clicks: str
    """Total number of clicks on the ad."""
    comment_likes: str
    """The count of likes on comments related to the ad."""
    comments: str
    """The number of comments on the ad."""
    company_page_clicks: str
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: str
    """Conversion value in the local currency."""
    cost_in_local_currency: str
    """Cost of ad campaign in the local currency."""
    cost_in_usd: str
    """Cost of ad campaign in USD."""
    document_completions: str
    """Number of completions for document views."""
    document_first_quartile_completions: str
    """Completions for first quartile of document views."""
    document_midpoint_completions: str
    """Completions for midpoint of document views."""
    document_third_quartile_completions: str
    """Completions for third quartile of document views."""
    download_clicks: str
    """Clicks on download links in the ad."""
    end_date: str
    """End date of the ad analytics data."""
    external_website_conversions: str
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites."""
    follows: str
    """Number of follows generated by the ad."""
    full_screen_plays: str
    """Number of times videos were played in fullscreen mode."""
    impressions: str
    """Total number of times the ad was displayed."""
    job_applications: str
    """Number of job applications initiated through the ad."""
    job_apply_clicks: str
    """Clicks on apply job button in the ad."""
    landing_page_clicks: str
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: str
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: str
    """Clicks on expressing interest through lead generation mail."""
    likes: str
    """Total likes received on the ad."""
    one_click_lead_form_opens: str
    """Number of times lead forms were opened in one click."""
    one_click_leads: str
    """Leads generated in one click."""
    opens: str
    """The number of times the ad was opened or expanded."""
    other_engagements: str
    """Engagements other than clicks on the ad."""
    pivot_values: str
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: str
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: str
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: str
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: str
    """Registrations completed post-viewing the ad."""
    reactions: str
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: str
    """Total registrations completed through the ad."""
    sends: str
    """Number of messages sent through the ad."""
    shares: str
    """Total shares generated by the ad."""
    start_date: str
    """Start date of the ad analytics data."""
    talent_leads: str
    """Number of leads related to talent acquisition."""
    text_url_clicks: str
    """Clicks on text URLs within the ad."""
    total_engagements: str
    """Total number of engagements on the ad."""
    valid_work_email_leads: str
    """Leads generated through valid work emails."""
    video_completions: str
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: str
    """Completions for first quartile of video views."""
    video_midpoint_completions: str
    """Completions for midpoint of video views."""
    video_starts: str
    """Total video starts initiated by users."""
    video_third_quartile_completions: str
    """Completions for third quartile of video views."""
    video_views: str
    """Total views of videos in the ad."""
    viral_card_clicks: str
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: str
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: str
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: str
    """Likes received on comments in viral distribution."""
    viral_comments: str
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: str
    """Clicks on the company page in viral distribution."""
    viral_document_completions: str
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: str
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: str
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: str
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: str
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: str
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: str
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: str
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: str
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: str
    """Fullscreen video plays in viral distribution."""
    viral_impressions: str
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: str
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: str
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: str
    """Clicks on landing page in viral distribution."""
    viral_likes: str
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: str
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: str
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: str
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: str
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: str
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: str
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: str
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: str
    """Total reactions in viral distribution of the ad."""
    viral_registrations: str
    """Total registrations in viral distribution of the ad."""
    viral_shares: str
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: str
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: str
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: str
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: str
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: str
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: str
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: str
    """Total views of videos in viral distribution of the ad."""
    pivot: str
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberJobTitleAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_member_job_title_analytics search results."""
    action_clicks: AirbyteSortOrder
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: AirbyteSortOrder
    """The number of clicks on ad unit components."""
    approximate_member_reach: AirbyteSortOrder
    """An approximation of unique ad impressions."""
    card_clicks: AirbyteSortOrder
    """The number of clicks on interactive card elements."""
    card_impressions: AirbyteSortOrder
    """The number of times interactive cards were displayed."""
    clicks: AirbyteSortOrder
    """Total number of clicks on the ad."""
    comment_likes: AirbyteSortOrder
    """The count of likes on comments related to the ad."""
    comments: AirbyteSortOrder
    """The number of comments on the ad."""
    company_page_clicks: AirbyteSortOrder
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in the local currency."""
    cost_in_local_currency: AirbyteSortOrder
    """Cost of ad campaign in the local currency."""
    cost_in_usd: AirbyteSortOrder
    """Cost of ad campaign in USD."""
    document_completions: AirbyteSortOrder
    """Number of completions for document views."""
    document_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of document views."""
    document_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of document views."""
    document_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of document views."""
    download_clicks: AirbyteSortOrder
    """Clicks on download links in the ad."""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data."""
    external_website_conversions: AirbyteSortOrder
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites."""
    follows: AirbyteSortOrder
    """Number of follows generated by the ad."""
    full_screen_plays: AirbyteSortOrder
    """Number of times videos were played in fullscreen mode."""
    impressions: AirbyteSortOrder
    """Total number of times the ad was displayed."""
    job_applications: AirbyteSortOrder
    """Number of job applications initiated through the ad."""
    job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in the ad."""
    landing_page_clicks: AirbyteSortOrder
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: AirbyteSortOrder
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: AirbyteSortOrder
    """Clicks on expressing interest through lead generation mail."""
    likes: AirbyteSortOrder
    """Total likes received on the ad."""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of times lead forms were opened in one click."""
    one_click_leads: AirbyteSortOrder
    """Leads generated in one click."""
    opens: AirbyteSortOrder
    """The number of times the ad was opened or expanded."""
    other_engagements: AirbyteSortOrder
    """Engagements other than clicks on the ad."""
    pivot_values: AirbyteSortOrder
    """Values used for pivoting the analytics."""
    string_of_pivot_values: AirbyteSortOrder
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing the ad."""
    reactions: AirbyteSortOrder
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: AirbyteSortOrder
    """Total registrations completed through the ad."""
    sends: AirbyteSortOrder
    """Number of messages sent through the ad."""
    shares: AirbyteSortOrder
    """Total shares generated by the ad."""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data."""
    talent_leads: AirbyteSortOrder
    """Number of leads related to talent acquisition."""
    text_url_clicks: AirbyteSortOrder
    """Clicks on text URLs within the ad."""
    total_engagements: AirbyteSortOrder
    """Total number of engagements on the ad."""
    valid_work_email_leads: AirbyteSortOrder
    """Leads generated through valid work emails."""
    video_completions: AirbyteSortOrder
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of video views."""
    video_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of video views."""
    video_starts: AirbyteSortOrder
    """Total video starts initiated by users."""
    video_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of video views."""
    video_views: AirbyteSortOrder
    """Total views of videos in the ad."""
    viral_card_clicks: AirbyteSortOrder
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: AirbyteSortOrder
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: AirbyteSortOrder
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: AirbyteSortOrder
    """Likes received on comments in viral distribution."""
    viral_comments: AirbyteSortOrder
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: AirbyteSortOrder
    """Clicks on the company page in viral distribution."""
    viral_document_completions: AirbyteSortOrder
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: AirbyteSortOrder
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: AirbyteSortOrder
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: AirbyteSortOrder
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: AirbyteSortOrder
    """Fullscreen video plays in viral distribution."""
    viral_impressions: AirbyteSortOrder
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: AirbyteSortOrder
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: AirbyteSortOrder
    """Clicks on landing page in viral distribution."""
    viral_likes: AirbyteSortOrder
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: AirbyteSortOrder
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: AirbyteSortOrder
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: AirbyteSortOrder
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: AirbyteSortOrder
    """Total reactions in viral distribution of the ad."""
    viral_registrations: AirbyteSortOrder
    """Total registrations in viral distribution of the ad."""
    viral_shares: AirbyteSortOrder
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: AirbyteSortOrder
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: AirbyteSortOrder
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: AirbyteSortOrder
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: AirbyteSortOrder
    """Total views of videos in viral distribution of the ad."""
    pivot: AirbyteSortOrder
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: AirbyteSortOrder
    """URN of the sponsored campaign this analytics record belongs to"""


# Entity-specific condition types for ad_member_job_title_analytics
class AdMemberJobTitleAnalyticsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdMemberJobTitleAnalyticsSearchFilter


class AdMemberJobTitleAnalyticsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdMemberJobTitleAnalyticsSearchFilter


class AdMemberJobTitleAnalyticsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdMemberJobTitleAnalyticsSearchFilter


class AdMemberJobTitleAnalyticsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdMemberJobTitleAnalyticsSearchFilter


class AdMemberJobTitleAnalyticsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdMemberJobTitleAnalyticsSearchFilter


class AdMemberJobTitleAnalyticsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdMemberJobTitleAnalyticsSearchFilter


class AdMemberJobTitleAnalyticsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AdMemberJobTitleAnalyticsStringFilter


class AdMemberJobTitleAnalyticsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AdMemberJobTitleAnalyticsStringFilter


class AdMemberJobTitleAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdMemberJobTitleAnalyticsStringFilter


class AdMemberJobTitleAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdMemberJobTitleAnalyticsStringFilter


class AdMemberJobTitleAnalyticsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: AdMemberJobTitleAnalyticsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdMemberJobTitleAnalyticsInCondition = TypedDict("AdMemberJobTitleAnalyticsInCondition", {"in": AdMemberJobTitleAnalyticsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdMemberJobTitleAnalyticsNotCondition = TypedDict("AdMemberJobTitleAnalyticsNotCondition", {"not": "AdMemberJobTitleAnalyticsCondition"}, total=False)
"""Negates the nested condition."""

AdMemberJobTitleAnalyticsAndCondition = TypedDict("AdMemberJobTitleAnalyticsAndCondition", {"and": "list[AdMemberJobTitleAnalyticsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdMemberJobTitleAnalyticsOrCondition = TypedDict("AdMemberJobTitleAnalyticsOrCondition", {"or": "list[AdMemberJobTitleAnalyticsCondition]"}, total=False)
"""True if any nested condition is true."""

AdMemberJobTitleAnalyticsAnyCondition = TypedDict("AdMemberJobTitleAnalyticsAnyCondition", {"any": AdMemberJobTitleAnalyticsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_member_job_title_analytics condition types
AdMemberJobTitleAnalyticsCondition = (
    AdMemberJobTitleAnalyticsEqCondition
    | AdMemberJobTitleAnalyticsNeqCondition
    | AdMemberJobTitleAnalyticsGtCondition
    | AdMemberJobTitleAnalyticsGteCondition
    | AdMemberJobTitleAnalyticsLtCondition
    | AdMemberJobTitleAnalyticsLteCondition
    | AdMemberJobTitleAnalyticsInCondition
    | AdMemberJobTitleAnalyticsStartswithCondition
    | AdMemberJobTitleAnalyticsEndswithCondition
    | AdMemberJobTitleAnalyticsFuzzyCondition
    | AdMemberJobTitleAnalyticsKeywordCondition
    | AdMemberJobTitleAnalyticsContainsCondition
    | AdMemberJobTitleAnalyticsNotCondition
    | AdMemberJobTitleAnalyticsAndCondition
    | AdMemberJobTitleAnalyticsOrCondition
    | AdMemberJobTitleAnalyticsAnyCondition
)


class AdMemberJobTitleAnalyticsSearchQuery(TypedDict, total=False):
    """Search query for ad_member_job_title_analytics entity."""
    filter: AdMemberJobTitleAnalyticsCondition
    sort: list[AdMemberJobTitleAnalyticsSortFilter]


# ===== AD_MEMBER_REGION_ANALYTICS SEARCH TYPES =====

class AdMemberRegionAnalyticsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_member_region_analytics search queries."""
    action_clicks: float | None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None
    """An approximation of unique ad impressions."""
    card_clicks: float | None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None
    """The number of times interactive cards were displayed."""
    clicks: float | None
    """Total number of clicks on the ad."""
    comment_likes: float | None
    """The count of likes on comments related to the ad."""
    comments: float | None
    """The number of comments on the ad."""
    company_page_clicks: float | None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None
    """Cost of ad campaign in USD."""
    document_completions: float | None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None
    """Completions for third quartile of document views."""
    download_clicks: float | None
    """Clicks on download links in the ad."""
    end_date: str | None
    """End date of the ad analytics data."""
    external_website_conversions: float | None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites."""
    follows: float | None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None
    """Total number of times the ad was displayed."""
    job_applications: float | None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None
    """Leads generated in one click."""
    opens: float | None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None
    """Registrations completed post-viewing the ad."""
    reactions: float | None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None
    """Total registrations completed through the ad."""
    sends: float | None
    """Number of messages sent through the ad."""
    shares: float | None
    """Total shares generated by the ad."""
    start_date: str | None
    """Start date of the ad analytics data."""
    talent_leads: float | None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None
    """Leads generated through valid work emails."""
    video_completions: float | None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None
    """Completions for midpoint of video views."""
    video_starts: float | None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None
    """Completions for third quartile of video views."""
    video_views: float | None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberRegionAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    action_clicks: list[float]
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: list[float]
    """The number of clicks on ad unit components."""
    approximate_member_reach: list[float]
    """An approximation of unique ad impressions."""
    card_clicks: list[float]
    """The number of clicks on interactive card elements."""
    card_impressions: list[float]
    """The number of times interactive cards were displayed."""
    clicks: list[float]
    """Total number of clicks on the ad."""
    comment_likes: list[float]
    """The count of likes on comments related to the ad."""
    comments: list[float]
    """The number of comments on the ad."""
    company_page_clicks: list[float]
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: list[float]
    """Conversion value in the local currency."""
    cost_in_local_currency: list[float]
    """Cost of ad campaign in the local currency."""
    cost_in_usd: list[float]
    """Cost of ad campaign in USD."""
    document_completions: list[float]
    """Number of completions for document views."""
    document_first_quartile_completions: list[float]
    """Completions for first quartile of document views."""
    document_midpoint_completions: list[float]
    """Completions for midpoint of document views."""
    document_third_quartile_completions: list[float]
    """Completions for third quartile of document views."""
    download_clicks: list[float]
    """Clicks on download links in the ad."""
    end_date: list[str]
    """End date of the ad analytics data."""
    external_website_conversions: list[float]
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites."""
    follows: list[float]
    """Number of follows generated by the ad."""
    full_screen_plays: list[float]
    """Number of times videos were played in fullscreen mode."""
    impressions: list[float]
    """Total number of times the ad was displayed."""
    job_applications: list[float]
    """Number of job applications initiated through the ad."""
    job_apply_clicks: list[float]
    """Clicks on apply job button in the ad."""
    landing_page_clicks: list[float]
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: list[float]
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: list[float]
    """Clicks on expressing interest through lead generation mail."""
    likes: list[float]
    """Total likes received on the ad."""
    one_click_lead_form_opens: list[float]
    """Number of times lead forms were opened in one click."""
    one_click_leads: list[float]
    """Leads generated in one click."""
    opens: list[float]
    """The number of times the ad was opened or expanded."""
    other_engagements: list[float]
    """Engagements other than clicks on the ad."""
    pivot_values: list[list[Any]]
    """Values used for pivoting the analytics."""
    string_of_pivot_values: list[str]
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: list[float]
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: list[float]
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: list[float]
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: list[float]
    """Registrations completed post-viewing the ad."""
    reactions: list[float]
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: list[float]
    """Total registrations completed through the ad."""
    sends: list[float]
    """Number of messages sent through the ad."""
    shares: list[float]
    """Total shares generated by the ad."""
    start_date: list[str]
    """Start date of the ad analytics data."""
    talent_leads: list[float]
    """Number of leads related to talent acquisition."""
    text_url_clicks: list[float]
    """Clicks on text URLs within the ad."""
    total_engagements: list[float]
    """Total number of engagements on the ad."""
    valid_work_email_leads: list[float]
    """Leads generated through valid work emails."""
    video_completions: list[float]
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: list[float]
    """Completions for first quartile of video views."""
    video_midpoint_completions: list[float]
    """Completions for midpoint of video views."""
    video_starts: list[float]
    """Total video starts initiated by users."""
    video_third_quartile_completions: list[float]
    """Completions for third quartile of video views."""
    video_views: list[float]
    """Total views of videos in the ad."""
    viral_card_clicks: list[float]
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: list[float]
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: list[float]
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: list[float]
    """Likes received on comments in viral distribution."""
    viral_comments: list[float]
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: list[float]
    """Clicks on the company page in viral distribution."""
    viral_document_completions: list[float]
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: list[float]
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: list[float]
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: list[float]
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: list[float]
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: list[float]
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: list[float]
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: list[float]
    """Fullscreen video plays in viral distribution."""
    viral_impressions: list[float]
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: list[float]
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: list[float]
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: list[float]
    """Clicks on landing page in viral distribution."""
    viral_likes: list[float]
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: list[float]
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: list[float]
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: list[float]
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: list[float]
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: list[float]
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: list[float]
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: list[float]
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: list[float]
    """Total reactions in viral distribution of the ad."""
    viral_registrations: list[float]
    """Total registrations in viral distribution of the ad."""
    viral_shares: list[float]
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: list[float]
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: list[float]
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: list[float]
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: list[float]
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: list[float]
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: list[float]
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: list[float]
    """Total views of videos in viral distribution of the ad."""
    pivot: list[str]
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: list[str]
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberRegionAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    action_clicks: Any
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: Any
    """The number of clicks on ad unit components."""
    approximate_member_reach: Any
    """An approximation of unique ad impressions."""
    card_clicks: Any
    """The number of clicks on interactive card elements."""
    card_impressions: Any
    """The number of times interactive cards were displayed."""
    clicks: Any
    """Total number of clicks on the ad."""
    comment_likes: Any
    """The count of likes on comments related to the ad."""
    comments: Any
    """The number of comments on the ad."""
    company_page_clicks: Any
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: Any
    """Conversion value in the local currency."""
    cost_in_local_currency: Any
    """Cost of ad campaign in the local currency."""
    cost_in_usd: Any
    """Cost of ad campaign in USD."""
    document_completions: Any
    """Number of completions for document views."""
    document_first_quartile_completions: Any
    """Completions for first quartile of document views."""
    document_midpoint_completions: Any
    """Completions for midpoint of document views."""
    document_third_quartile_completions: Any
    """Completions for third quartile of document views."""
    download_clicks: Any
    """Clicks on download links in the ad."""
    end_date: Any
    """End date of the ad analytics data."""
    external_website_conversions: Any
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites."""
    follows: Any
    """Number of follows generated by the ad."""
    full_screen_plays: Any
    """Number of times videos were played in fullscreen mode."""
    impressions: Any
    """Total number of times the ad was displayed."""
    job_applications: Any
    """Number of job applications initiated through the ad."""
    job_apply_clicks: Any
    """Clicks on apply job button in the ad."""
    landing_page_clicks: Any
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: Any
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: Any
    """Clicks on expressing interest through lead generation mail."""
    likes: Any
    """Total likes received on the ad."""
    one_click_lead_form_opens: Any
    """Number of times lead forms were opened in one click."""
    one_click_leads: Any
    """Leads generated in one click."""
    opens: Any
    """The number of times the ad was opened or expanded."""
    other_engagements: Any
    """Engagements other than clicks on the ad."""
    pivot_values: Any
    """Values used for pivoting the analytics."""
    string_of_pivot_values: Any
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: Any
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: Any
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: Any
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: Any
    """Registrations completed post-viewing the ad."""
    reactions: Any
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: Any
    """Total registrations completed through the ad."""
    sends: Any
    """Number of messages sent through the ad."""
    shares: Any
    """Total shares generated by the ad."""
    start_date: Any
    """Start date of the ad analytics data."""
    talent_leads: Any
    """Number of leads related to talent acquisition."""
    text_url_clicks: Any
    """Clicks on text URLs within the ad."""
    total_engagements: Any
    """Total number of engagements on the ad."""
    valid_work_email_leads: Any
    """Leads generated through valid work emails."""
    video_completions: Any
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: Any
    """Completions for first quartile of video views."""
    video_midpoint_completions: Any
    """Completions for midpoint of video views."""
    video_starts: Any
    """Total video starts initiated by users."""
    video_third_quartile_completions: Any
    """Completions for third quartile of video views."""
    video_views: Any
    """Total views of videos in the ad."""
    viral_card_clicks: Any
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: Any
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: Any
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: Any
    """Likes received on comments in viral distribution."""
    viral_comments: Any
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: Any
    """Clicks on the company page in viral distribution."""
    viral_document_completions: Any
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: Any
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: Any
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: Any
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: Any
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: Any
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: Any
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: Any
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: Any
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: Any
    """Fullscreen video plays in viral distribution."""
    viral_impressions: Any
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: Any
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: Any
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: Any
    """Clicks on landing page in viral distribution."""
    viral_likes: Any
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: Any
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: Any
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: Any
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: Any
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: Any
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: Any
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: Any
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: Any
    """Total reactions in viral distribution of the ad."""
    viral_registrations: Any
    """Total registrations in viral distribution of the ad."""
    viral_shares: Any
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: Any
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: Any
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: Any
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: Any
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: Any
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: Any
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: Any
    """Total views of videos in viral distribution of the ad."""
    pivot: Any
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: Any
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberRegionAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    action_clicks: str
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: str
    """The number of clicks on ad unit components."""
    approximate_member_reach: str
    """An approximation of unique ad impressions."""
    card_clicks: str
    """The number of clicks on interactive card elements."""
    card_impressions: str
    """The number of times interactive cards were displayed."""
    clicks: str
    """Total number of clicks on the ad."""
    comment_likes: str
    """The count of likes on comments related to the ad."""
    comments: str
    """The number of comments on the ad."""
    company_page_clicks: str
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: str
    """Conversion value in the local currency."""
    cost_in_local_currency: str
    """Cost of ad campaign in the local currency."""
    cost_in_usd: str
    """Cost of ad campaign in USD."""
    document_completions: str
    """Number of completions for document views."""
    document_first_quartile_completions: str
    """Completions for first quartile of document views."""
    document_midpoint_completions: str
    """Completions for midpoint of document views."""
    document_third_quartile_completions: str
    """Completions for third quartile of document views."""
    download_clicks: str
    """Clicks on download links in the ad."""
    end_date: str
    """End date of the ad analytics data."""
    external_website_conversions: str
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites."""
    follows: str
    """Number of follows generated by the ad."""
    full_screen_plays: str
    """Number of times videos were played in fullscreen mode."""
    impressions: str
    """Total number of times the ad was displayed."""
    job_applications: str
    """Number of job applications initiated through the ad."""
    job_apply_clicks: str
    """Clicks on apply job button in the ad."""
    landing_page_clicks: str
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: str
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: str
    """Clicks on expressing interest through lead generation mail."""
    likes: str
    """Total likes received on the ad."""
    one_click_lead_form_opens: str
    """Number of times lead forms were opened in one click."""
    one_click_leads: str
    """Leads generated in one click."""
    opens: str
    """The number of times the ad was opened or expanded."""
    other_engagements: str
    """Engagements other than clicks on the ad."""
    pivot_values: str
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: str
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: str
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: str
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: str
    """Registrations completed post-viewing the ad."""
    reactions: str
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: str
    """Total registrations completed through the ad."""
    sends: str
    """Number of messages sent through the ad."""
    shares: str
    """Total shares generated by the ad."""
    start_date: str
    """Start date of the ad analytics data."""
    talent_leads: str
    """Number of leads related to talent acquisition."""
    text_url_clicks: str
    """Clicks on text URLs within the ad."""
    total_engagements: str
    """Total number of engagements on the ad."""
    valid_work_email_leads: str
    """Leads generated through valid work emails."""
    video_completions: str
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: str
    """Completions for first quartile of video views."""
    video_midpoint_completions: str
    """Completions for midpoint of video views."""
    video_starts: str
    """Total video starts initiated by users."""
    video_third_quartile_completions: str
    """Completions for third quartile of video views."""
    video_views: str
    """Total views of videos in the ad."""
    viral_card_clicks: str
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: str
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: str
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: str
    """Likes received on comments in viral distribution."""
    viral_comments: str
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: str
    """Clicks on the company page in viral distribution."""
    viral_document_completions: str
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: str
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: str
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: str
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: str
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: str
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: str
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: str
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: str
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: str
    """Fullscreen video plays in viral distribution."""
    viral_impressions: str
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: str
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: str
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: str
    """Clicks on landing page in viral distribution."""
    viral_likes: str
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: str
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: str
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: str
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: str
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: str
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: str
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: str
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: str
    """Total reactions in viral distribution of the ad."""
    viral_registrations: str
    """Total registrations in viral distribution of the ad."""
    viral_shares: str
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: str
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: str
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: str
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: str
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: str
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: str
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: str
    """Total views of videos in viral distribution of the ad."""
    pivot: str
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberRegionAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_member_region_analytics search results."""
    action_clicks: AirbyteSortOrder
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: AirbyteSortOrder
    """The number of clicks on ad unit components."""
    approximate_member_reach: AirbyteSortOrder
    """An approximation of unique ad impressions."""
    card_clicks: AirbyteSortOrder
    """The number of clicks on interactive card elements."""
    card_impressions: AirbyteSortOrder
    """The number of times interactive cards were displayed."""
    clicks: AirbyteSortOrder
    """Total number of clicks on the ad."""
    comment_likes: AirbyteSortOrder
    """The count of likes on comments related to the ad."""
    comments: AirbyteSortOrder
    """The number of comments on the ad."""
    company_page_clicks: AirbyteSortOrder
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in the local currency."""
    cost_in_local_currency: AirbyteSortOrder
    """Cost of ad campaign in the local currency."""
    cost_in_usd: AirbyteSortOrder
    """Cost of ad campaign in USD."""
    document_completions: AirbyteSortOrder
    """Number of completions for document views."""
    document_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of document views."""
    document_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of document views."""
    document_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of document views."""
    download_clicks: AirbyteSortOrder
    """Clicks on download links in the ad."""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data."""
    external_website_conversions: AirbyteSortOrder
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites."""
    follows: AirbyteSortOrder
    """Number of follows generated by the ad."""
    full_screen_plays: AirbyteSortOrder
    """Number of times videos were played in fullscreen mode."""
    impressions: AirbyteSortOrder
    """Total number of times the ad was displayed."""
    job_applications: AirbyteSortOrder
    """Number of job applications initiated through the ad."""
    job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in the ad."""
    landing_page_clicks: AirbyteSortOrder
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: AirbyteSortOrder
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: AirbyteSortOrder
    """Clicks on expressing interest through lead generation mail."""
    likes: AirbyteSortOrder
    """Total likes received on the ad."""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of times lead forms were opened in one click."""
    one_click_leads: AirbyteSortOrder
    """Leads generated in one click."""
    opens: AirbyteSortOrder
    """The number of times the ad was opened or expanded."""
    other_engagements: AirbyteSortOrder
    """Engagements other than clicks on the ad."""
    pivot_values: AirbyteSortOrder
    """Values used for pivoting the analytics."""
    string_of_pivot_values: AirbyteSortOrder
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing the ad."""
    reactions: AirbyteSortOrder
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: AirbyteSortOrder
    """Total registrations completed through the ad."""
    sends: AirbyteSortOrder
    """Number of messages sent through the ad."""
    shares: AirbyteSortOrder
    """Total shares generated by the ad."""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data."""
    talent_leads: AirbyteSortOrder
    """Number of leads related to talent acquisition."""
    text_url_clicks: AirbyteSortOrder
    """Clicks on text URLs within the ad."""
    total_engagements: AirbyteSortOrder
    """Total number of engagements on the ad."""
    valid_work_email_leads: AirbyteSortOrder
    """Leads generated through valid work emails."""
    video_completions: AirbyteSortOrder
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of video views."""
    video_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of video views."""
    video_starts: AirbyteSortOrder
    """Total video starts initiated by users."""
    video_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of video views."""
    video_views: AirbyteSortOrder
    """Total views of videos in the ad."""
    viral_card_clicks: AirbyteSortOrder
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: AirbyteSortOrder
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: AirbyteSortOrder
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: AirbyteSortOrder
    """Likes received on comments in viral distribution."""
    viral_comments: AirbyteSortOrder
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: AirbyteSortOrder
    """Clicks on the company page in viral distribution."""
    viral_document_completions: AirbyteSortOrder
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: AirbyteSortOrder
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: AirbyteSortOrder
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: AirbyteSortOrder
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: AirbyteSortOrder
    """Fullscreen video plays in viral distribution."""
    viral_impressions: AirbyteSortOrder
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: AirbyteSortOrder
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: AirbyteSortOrder
    """Clicks on landing page in viral distribution."""
    viral_likes: AirbyteSortOrder
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: AirbyteSortOrder
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: AirbyteSortOrder
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: AirbyteSortOrder
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: AirbyteSortOrder
    """Total reactions in viral distribution of the ad."""
    viral_registrations: AirbyteSortOrder
    """Total registrations in viral distribution of the ad."""
    viral_shares: AirbyteSortOrder
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: AirbyteSortOrder
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: AirbyteSortOrder
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: AirbyteSortOrder
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: AirbyteSortOrder
    """Total views of videos in viral distribution of the ad."""
    pivot: AirbyteSortOrder
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: AirbyteSortOrder
    """URN of the sponsored campaign this analytics record belongs to"""


# Entity-specific condition types for ad_member_region_analytics
class AdMemberRegionAnalyticsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdMemberRegionAnalyticsSearchFilter


class AdMemberRegionAnalyticsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdMemberRegionAnalyticsSearchFilter


class AdMemberRegionAnalyticsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdMemberRegionAnalyticsSearchFilter


class AdMemberRegionAnalyticsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdMemberRegionAnalyticsSearchFilter


class AdMemberRegionAnalyticsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdMemberRegionAnalyticsSearchFilter


class AdMemberRegionAnalyticsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdMemberRegionAnalyticsSearchFilter


class AdMemberRegionAnalyticsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AdMemberRegionAnalyticsStringFilter


class AdMemberRegionAnalyticsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AdMemberRegionAnalyticsStringFilter


class AdMemberRegionAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdMemberRegionAnalyticsStringFilter


class AdMemberRegionAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdMemberRegionAnalyticsStringFilter


class AdMemberRegionAnalyticsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: AdMemberRegionAnalyticsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdMemberRegionAnalyticsInCondition = TypedDict("AdMemberRegionAnalyticsInCondition", {"in": AdMemberRegionAnalyticsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdMemberRegionAnalyticsNotCondition = TypedDict("AdMemberRegionAnalyticsNotCondition", {"not": "AdMemberRegionAnalyticsCondition"}, total=False)
"""Negates the nested condition."""

AdMemberRegionAnalyticsAndCondition = TypedDict("AdMemberRegionAnalyticsAndCondition", {"and": "list[AdMemberRegionAnalyticsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdMemberRegionAnalyticsOrCondition = TypedDict("AdMemberRegionAnalyticsOrCondition", {"or": "list[AdMemberRegionAnalyticsCondition]"}, total=False)
"""True if any nested condition is true."""

AdMemberRegionAnalyticsAnyCondition = TypedDict("AdMemberRegionAnalyticsAnyCondition", {"any": AdMemberRegionAnalyticsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_member_region_analytics condition types
AdMemberRegionAnalyticsCondition = (
    AdMemberRegionAnalyticsEqCondition
    | AdMemberRegionAnalyticsNeqCondition
    | AdMemberRegionAnalyticsGtCondition
    | AdMemberRegionAnalyticsGteCondition
    | AdMemberRegionAnalyticsLtCondition
    | AdMemberRegionAnalyticsLteCondition
    | AdMemberRegionAnalyticsInCondition
    | AdMemberRegionAnalyticsStartswithCondition
    | AdMemberRegionAnalyticsEndswithCondition
    | AdMemberRegionAnalyticsFuzzyCondition
    | AdMemberRegionAnalyticsKeywordCondition
    | AdMemberRegionAnalyticsContainsCondition
    | AdMemberRegionAnalyticsNotCondition
    | AdMemberRegionAnalyticsAndCondition
    | AdMemberRegionAnalyticsOrCondition
    | AdMemberRegionAnalyticsAnyCondition
)


class AdMemberRegionAnalyticsSearchQuery(TypedDict, total=False):
    """Search query for ad_member_region_analytics entity."""
    filter: AdMemberRegionAnalyticsCondition
    sort: list[AdMemberRegionAnalyticsSortFilter]


# ===== AD_MEMBER_SENIORITY_ANALYTICS SEARCH TYPES =====

class AdMemberSeniorityAnalyticsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_member_seniority_analytics search queries."""
    action_clicks: float | None
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: float | None
    """The number of clicks on ad unit components."""
    approximate_member_reach: float | None
    """An approximation of unique ad impressions."""
    card_clicks: float | None
    """The number of clicks on interactive card elements."""
    card_impressions: float | None
    """The number of times interactive cards were displayed."""
    clicks: float | None
    """Total number of clicks on the ad."""
    comment_likes: float | None
    """The count of likes on comments related to the ad."""
    comments: float | None
    """The number of comments on the ad."""
    company_page_clicks: float | None
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: float | None
    """Conversion value in the local currency."""
    cost_in_local_currency: float | None
    """Cost of ad campaign in the local currency."""
    cost_in_usd: float | None
    """Cost of ad campaign in USD."""
    document_completions: float | None
    """Number of completions for document views."""
    document_first_quartile_completions: float | None
    """Completions for first quartile of document views."""
    document_midpoint_completions: float | None
    """Completions for midpoint of document views."""
    document_third_quartile_completions: float | None
    """Completions for third quartile of document views."""
    download_clicks: float | None
    """Clicks on download links in the ad."""
    end_date: str | None
    """End date of the ad analytics data."""
    external_website_conversions: float | None
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: float | None
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: float | None
    """Post-view conversions on external websites."""
    follows: float | None
    """Number of follows generated by the ad."""
    full_screen_plays: float | None
    """Number of times videos were played in fullscreen mode."""
    impressions: float | None
    """Total number of times the ad was displayed."""
    job_applications: float | None
    """Number of job applications initiated through the ad."""
    job_apply_clicks: float | None
    """Clicks on apply job button in the ad."""
    landing_page_clicks: float | None
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: float | None
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: float | None
    """Clicks on expressing interest through lead generation mail."""
    likes: float | None
    """Total likes received on the ad."""
    one_click_lead_form_opens: float | None
    """Number of times lead forms were opened in one click."""
    one_click_leads: float | None
    """Leads generated in one click."""
    opens: float | None
    """The number of times the ad was opened or expanded."""
    other_engagements: float | None
    """Engagements other than clicks on the ad."""
    pivot_values: list[Any] | None
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str | None
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: float | None
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: float | None
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: float | None
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: float | None
    """Registrations completed post-viewing the ad."""
    reactions: float | None
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: float | None
    """Total registrations completed through the ad."""
    sends: float | None
    """Number of messages sent through the ad."""
    shares: float | None
    """Total shares generated by the ad."""
    start_date: str | None
    """Start date of the ad analytics data."""
    talent_leads: float | None
    """Number of leads related to talent acquisition."""
    text_url_clicks: float | None
    """Clicks on text URLs within the ad."""
    total_engagements: float | None
    """Total number of engagements on the ad."""
    valid_work_email_leads: float | None
    """Leads generated through valid work emails."""
    video_completions: float | None
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: float | None
    """Completions for first quartile of video views."""
    video_midpoint_completions: float | None
    """Completions for midpoint of video views."""
    video_starts: float | None
    """Total video starts initiated by users."""
    video_third_quartile_completions: float | None
    """Completions for third quartile of video views."""
    video_views: float | None
    """Total views of videos in the ad."""
    viral_card_clicks: float | None
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: float | None
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: float | None
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: float | None
    """Likes received on comments in viral distribution."""
    viral_comments: float | None
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: float | None
    """Clicks on the company page in viral distribution."""
    viral_document_completions: float | None
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: float | None
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: float | None
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: float | None
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: float | None
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: float | None
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: float | None
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: float | None
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: float | None
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: float | None
    """Fullscreen video plays in viral distribution."""
    viral_impressions: float | None
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: float | None
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: float | None
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: float | None
    """Clicks on landing page in viral distribution."""
    viral_likes: float | None
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: float | None
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: float | None
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: float | None
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: float | None
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: float | None
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: float | None
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: float | None
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: float | None
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: float | None
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: float | None
    """Total reactions in viral distribution of the ad."""
    viral_registrations: float | None
    """Total registrations in viral distribution of the ad."""
    viral_shares: float | None
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: float | None
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: float | None
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: float | None
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: float | None
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: float | None
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: float | None
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: float | None
    """Total views of videos in viral distribution of the ad."""
    pivot: str | None
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str | None
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberSeniorityAnalyticsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    action_clicks: list[float]
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: list[float]
    """The number of clicks on ad unit components."""
    approximate_member_reach: list[float]
    """An approximation of unique ad impressions."""
    card_clicks: list[float]
    """The number of clicks on interactive card elements."""
    card_impressions: list[float]
    """The number of times interactive cards were displayed."""
    clicks: list[float]
    """Total number of clicks on the ad."""
    comment_likes: list[float]
    """The count of likes on comments related to the ad."""
    comments: list[float]
    """The number of comments on the ad."""
    company_page_clicks: list[float]
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: list[float]
    """Conversion value in the local currency."""
    cost_in_local_currency: list[float]
    """Cost of ad campaign in the local currency."""
    cost_in_usd: list[float]
    """Cost of ad campaign in USD."""
    document_completions: list[float]
    """Number of completions for document views."""
    document_first_quartile_completions: list[float]
    """Completions for first quartile of document views."""
    document_midpoint_completions: list[float]
    """Completions for midpoint of document views."""
    document_third_quartile_completions: list[float]
    """Completions for third quartile of document views."""
    download_clicks: list[float]
    """Clicks on download links in the ad."""
    end_date: list[str]
    """End date of the ad analytics data."""
    external_website_conversions: list[float]
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites."""
    follows: list[float]
    """Number of follows generated by the ad."""
    full_screen_plays: list[float]
    """Number of times videos were played in fullscreen mode."""
    impressions: list[float]
    """Total number of times the ad was displayed."""
    job_applications: list[float]
    """Number of job applications initiated through the ad."""
    job_apply_clicks: list[float]
    """Clicks on apply job button in the ad."""
    landing_page_clicks: list[float]
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: list[float]
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: list[float]
    """Clicks on expressing interest through lead generation mail."""
    likes: list[float]
    """Total likes received on the ad."""
    one_click_lead_form_opens: list[float]
    """Number of times lead forms were opened in one click."""
    one_click_leads: list[float]
    """Leads generated in one click."""
    opens: list[float]
    """The number of times the ad was opened or expanded."""
    other_engagements: list[float]
    """Engagements other than clicks on the ad."""
    pivot_values: list[list[Any]]
    """Values used for pivoting the analytics."""
    string_of_pivot_values: list[str]
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: list[float]
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: list[float]
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: list[float]
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: list[float]
    """Registrations completed post-viewing the ad."""
    reactions: list[float]
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: list[float]
    """Total registrations completed through the ad."""
    sends: list[float]
    """Number of messages sent through the ad."""
    shares: list[float]
    """Total shares generated by the ad."""
    start_date: list[str]
    """Start date of the ad analytics data."""
    talent_leads: list[float]
    """Number of leads related to talent acquisition."""
    text_url_clicks: list[float]
    """Clicks on text URLs within the ad."""
    total_engagements: list[float]
    """Total number of engagements on the ad."""
    valid_work_email_leads: list[float]
    """Leads generated through valid work emails."""
    video_completions: list[float]
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: list[float]
    """Completions for first quartile of video views."""
    video_midpoint_completions: list[float]
    """Completions for midpoint of video views."""
    video_starts: list[float]
    """Total video starts initiated by users."""
    video_third_quartile_completions: list[float]
    """Completions for third quartile of video views."""
    video_views: list[float]
    """Total views of videos in the ad."""
    viral_card_clicks: list[float]
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: list[float]
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: list[float]
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: list[float]
    """Likes received on comments in viral distribution."""
    viral_comments: list[float]
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: list[float]
    """Clicks on the company page in viral distribution."""
    viral_document_completions: list[float]
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: list[float]
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: list[float]
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: list[float]
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: list[float]
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: list[float]
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: list[float]
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: list[float]
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: list[float]
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: list[float]
    """Fullscreen video plays in viral distribution."""
    viral_impressions: list[float]
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: list[float]
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: list[float]
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: list[float]
    """Clicks on landing page in viral distribution."""
    viral_likes: list[float]
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: list[float]
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: list[float]
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: list[float]
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: list[float]
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: list[float]
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: list[float]
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: list[float]
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: list[float]
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: list[float]
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: list[float]
    """Total reactions in viral distribution of the ad."""
    viral_registrations: list[float]
    """Total registrations in viral distribution of the ad."""
    viral_shares: list[float]
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: list[float]
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: list[float]
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: list[float]
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: list[float]
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: list[float]
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: list[float]
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: list[float]
    """Total views of videos in viral distribution of the ad."""
    pivot: list[str]
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: list[str]
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberSeniorityAnalyticsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    action_clicks: Any
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: Any
    """The number of clicks on ad unit components."""
    approximate_member_reach: Any
    """An approximation of unique ad impressions."""
    card_clicks: Any
    """The number of clicks on interactive card elements."""
    card_impressions: Any
    """The number of times interactive cards were displayed."""
    clicks: Any
    """Total number of clicks on the ad."""
    comment_likes: Any
    """The count of likes on comments related to the ad."""
    comments: Any
    """The number of comments on the ad."""
    company_page_clicks: Any
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: Any
    """Conversion value in the local currency."""
    cost_in_local_currency: Any
    """Cost of ad campaign in the local currency."""
    cost_in_usd: Any
    """Cost of ad campaign in USD."""
    document_completions: Any
    """Number of completions for document views."""
    document_first_quartile_completions: Any
    """Completions for first quartile of document views."""
    document_midpoint_completions: Any
    """Completions for midpoint of document views."""
    document_third_quartile_completions: Any
    """Completions for third quartile of document views."""
    download_clicks: Any
    """Clicks on download links in the ad."""
    end_date: Any
    """End date of the ad analytics data."""
    external_website_conversions: Any
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: Any
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: Any
    """Post-view conversions on external websites."""
    follows: Any
    """Number of follows generated by the ad."""
    full_screen_plays: Any
    """Number of times videos were played in fullscreen mode."""
    impressions: Any
    """Total number of times the ad was displayed."""
    job_applications: Any
    """Number of job applications initiated through the ad."""
    job_apply_clicks: Any
    """Clicks on apply job button in the ad."""
    landing_page_clicks: Any
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: Any
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: Any
    """Clicks on expressing interest through lead generation mail."""
    likes: Any
    """Total likes received on the ad."""
    one_click_lead_form_opens: Any
    """Number of times lead forms were opened in one click."""
    one_click_leads: Any
    """Leads generated in one click."""
    opens: Any
    """The number of times the ad was opened or expanded."""
    other_engagements: Any
    """Engagements other than clicks on the ad."""
    pivot_values: Any
    """Values used for pivoting the analytics."""
    string_of_pivot_values: Any
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: Any
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: Any
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: Any
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: Any
    """Registrations completed post-viewing the ad."""
    reactions: Any
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: Any
    """Total registrations completed through the ad."""
    sends: Any
    """Number of messages sent through the ad."""
    shares: Any
    """Total shares generated by the ad."""
    start_date: Any
    """Start date of the ad analytics data."""
    talent_leads: Any
    """Number of leads related to talent acquisition."""
    text_url_clicks: Any
    """Clicks on text URLs within the ad."""
    total_engagements: Any
    """Total number of engagements on the ad."""
    valid_work_email_leads: Any
    """Leads generated through valid work emails."""
    video_completions: Any
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: Any
    """Completions for first quartile of video views."""
    video_midpoint_completions: Any
    """Completions for midpoint of video views."""
    video_starts: Any
    """Total video starts initiated by users."""
    video_third_quartile_completions: Any
    """Completions for third quartile of video views."""
    video_views: Any
    """Total views of videos in the ad."""
    viral_card_clicks: Any
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: Any
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: Any
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: Any
    """Likes received on comments in viral distribution."""
    viral_comments: Any
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: Any
    """Clicks on the company page in viral distribution."""
    viral_document_completions: Any
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: Any
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: Any
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: Any
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: Any
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: Any
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: Any
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: Any
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: Any
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: Any
    """Fullscreen video plays in viral distribution."""
    viral_impressions: Any
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: Any
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: Any
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: Any
    """Clicks on landing page in viral distribution."""
    viral_likes: Any
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: Any
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: Any
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: Any
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: Any
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: Any
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: Any
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: Any
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: Any
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: Any
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: Any
    """Total reactions in viral distribution of the ad."""
    viral_registrations: Any
    """Total registrations in viral distribution of the ad."""
    viral_shares: Any
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: Any
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: Any
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: Any
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: Any
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: Any
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: Any
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: Any
    """Total views of videos in viral distribution of the ad."""
    pivot: Any
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: Any
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberSeniorityAnalyticsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    action_clicks: str
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: str
    """The number of clicks on ad unit components."""
    approximate_member_reach: str
    """An approximation of unique ad impressions."""
    card_clicks: str
    """The number of clicks on interactive card elements."""
    card_impressions: str
    """The number of times interactive cards were displayed."""
    clicks: str
    """Total number of clicks on the ad."""
    comment_likes: str
    """The count of likes on comments related to the ad."""
    comments: str
    """The number of comments on the ad."""
    company_page_clicks: str
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: str
    """Conversion value in the local currency."""
    cost_in_local_currency: str
    """Cost of ad campaign in the local currency."""
    cost_in_usd: str
    """Cost of ad campaign in USD."""
    document_completions: str
    """Number of completions for document views."""
    document_first_quartile_completions: str
    """Completions for first quartile of document views."""
    document_midpoint_completions: str
    """Completions for midpoint of document views."""
    document_third_quartile_completions: str
    """Completions for third quartile of document views."""
    download_clicks: str
    """Clicks on download links in the ad."""
    end_date: str
    """End date of the ad analytics data."""
    external_website_conversions: str
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: str
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: str
    """Post-view conversions on external websites."""
    follows: str
    """Number of follows generated by the ad."""
    full_screen_plays: str
    """Number of times videos were played in fullscreen mode."""
    impressions: str
    """Total number of times the ad was displayed."""
    job_applications: str
    """Number of job applications initiated through the ad."""
    job_apply_clicks: str
    """Clicks on apply job button in the ad."""
    landing_page_clicks: str
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: str
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: str
    """Clicks on expressing interest through lead generation mail."""
    likes: str
    """Total likes received on the ad."""
    one_click_lead_form_opens: str
    """Number of times lead forms were opened in one click."""
    one_click_leads: str
    """Leads generated in one click."""
    opens: str
    """The number of times the ad was opened or expanded."""
    other_engagements: str
    """Engagements other than clicks on the ad."""
    pivot_values: str
    """Values used for pivoting the analytics."""
    string_of_pivot_values: str
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: str
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: str
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: str
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: str
    """Registrations completed post-viewing the ad."""
    reactions: str
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: str
    """Total registrations completed through the ad."""
    sends: str
    """Number of messages sent through the ad."""
    shares: str
    """Total shares generated by the ad."""
    start_date: str
    """Start date of the ad analytics data."""
    talent_leads: str
    """Number of leads related to talent acquisition."""
    text_url_clicks: str
    """Clicks on text URLs within the ad."""
    total_engagements: str
    """Total number of engagements on the ad."""
    valid_work_email_leads: str
    """Leads generated through valid work emails."""
    video_completions: str
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: str
    """Completions for first quartile of video views."""
    video_midpoint_completions: str
    """Completions for midpoint of video views."""
    video_starts: str
    """Total video starts initiated by users."""
    video_third_quartile_completions: str
    """Completions for third quartile of video views."""
    video_views: str
    """Total views of videos in the ad."""
    viral_card_clicks: str
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: str
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: str
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: str
    """Likes received on comments in viral distribution."""
    viral_comments: str
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: str
    """Clicks on the company page in viral distribution."""
    viral_document_completions: str
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: str
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: str
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: str
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: str
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: str
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: str
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: str
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: str
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: str
    """Fullscreen video plays in viral distribution."""
    viral_impressions: str
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: str
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: str
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: str
    """Clicks on landing page in viral distribution."""
    viral_likes: str
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: str
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: str
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: str
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: str
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: str
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: str
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: str
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: str
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: str
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: str
    """Total reactions in viral distribution of the ad."""
    viral_registrations: str
    """Total registrations in viral distribution of the ad."""
    viral_shares: str
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: str
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: str
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: str
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: str
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: str
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: str
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: str
    """Total views of videos in viral distribution of the ad."""
    pivot: str
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: str
    """URN of the sponsored campaign this analytics record belongs to"""


class AdMemberSeniorityAnalyticsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_member_seniority_analytics search results."""
    action_clicks: AirbyteSortOrder
    """The number of clicks on action buttons in the ad."""
    ad_unit_clicks: AirbyteSortOrder
    """The number of clicks on ad unit components."""
    approximate_member_reach: AirbyteSortOrder
    """An approximation of unique ad impressions."""
    card_clicks: AirbyteSortOrder
    """The number of clicks on interactive card elements."""
    card_impressions: AirbyteSortOrder
    """The number of times interactive cards were displayed."""
    clicks: AirbyteSortOrder
    """Total number of clicks on the ad."""
    comment_likes: AirbyteSortOrder
    """The count of likes on comments related to the ad."""
    comments: AirbyteSortOrder
    """The number of comments on the ad."""
    company_page_clicks: AirbyteSortOrder
    """Clicks on the company page associated with the ad."""
    conversion_value_in_local_currency: AirbyteSortOrder
    """Conversion value in the local currency."""
    cost_in_local_currency: AirbyteSortOrder
    """Cost of ad campaign in the local currency."""
    cost_in_usd: AirbyteSortOrder
    """Cost of ad campaign in USD."""
    document_completions: AirbyteSortOrder
    """Number of completions for document views."""
    document_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of document views."""
    document_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of document views."""
    document_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of document views."""
    download_clicks: AirbyteSortOrder
    """Clicks on download links in the ad."""
    end_date: AirbyteSortOrder
    """End date of the ad analytics data."""
    external_website_conversions: AirbyteSortOrder
    """Conversions that lead to external websites."""
    external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites."""
    external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites."""
    follows: AirbyteSortOrder
    """Number of follows generated by the ad."""
    full_screen_plays: AirbyteSortOrder
    """Number of times videos were played in fullscreen mode."""
    impressions: AirbyteSortOrder
    """Total number of times the ad was displayed."""
    job_applications: AirbyteSortOrder
    """Number of job applications initiated through the ad."""
    job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in the ad."""
    landing_page_clicks: AirbyteSortOrder
    """Clicks on the landing page associated with the ad."""
    lead_generation_mail_contact_info_shares: AirbyteSortOrder
    """Shares of contact information through lead generation."""
    lead_generation_mail_interested_clicks: AirbyteSortOrder
    """Clicks on expressing interest through lead generation mail."""
    likes: AirbyteSortOrder
    """Total likes received on the ad."""
    one_click_lead_form_opens: AirbyteSortOrder
    """Number of times lead forms were opened in one click."""
    one_click_leads: AirbyteSortOrder
    """Leads generated in one click."""
    opens: AirbyteSortOrder
    """The number of times the ad was opened or expanded."""
    other_engagements: AirbyteSortOrder
    """Engagements other than clicks on the ad."""
    pivot_values: AirbyteSortOrder
    """Values used for pivoting the analytics."""
    string_of_pivot_values: AirbyteSortOrder
    """Comma-separated string of pivot values for this analytics record"""
    post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking on the ad."""
    post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking on the ad."""
    post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking on the ad."""
    post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing the ad."""
    post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing the ad."""
    post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing the ad."""
    reactions: AirbyteSortOrder
    """Total reactions (e.g., like, love, celebrate) on the ad."""
    registrations: AirbyteSortOrder
    """Total registrations completed through the ad."""
    sends: AirbyteSortOrder
    """Number of messages sent through the ad."""
    shares: AirbyteSortOrder
    """Total shares generated by the ad."""
    start_date: AirbyteSortOrder
    """Start date of the ad analytics data."""
    talent_leads: AirbyteSortOrder
    """Number of leads related to talent acquisition."""
    text_url_clicks: AirbyteSortOrder
    """Clicks on text URLs within the ad."""
    total_engagements: AirbyteSortOrder
    """Total number of engagements on the ad."""
    valid_work_email_leads: AirbyteSortOrder
    """Leads generated through valid work emails."""
    video_completions: AirbyteSortOrder
    """Number of times videos were watched till completion."""
    video_first_quartile_completions: AirbyteSortOrder
    """Completions for first quartile of video views."""
    video_midpoint_completions: AirbyteSortOrder
    """Completions for midpoint of video views."""
    video_starts: AirbyteSortOrder
    """Total video starts initiated by users."""
    video_third_quartile_completions: AirbyteSortOrder
    """Completions for third quartile of video views."""
    video_views: AirbyteSortOrder
    """Total views of videos in the ad."""
    viral_card_clicks: AirbyteSortOrder
    """Clicks on interactive card components in viral distribution."""
    viral_card_impressions: AirbyteSortOrder
    """Impressions of interactive cards in viral distribution."""
    viral_clicks: AirbyteSortOrder
    """Total clicks in viral distribution of the ad."""
    viral_comment_likes: AirbyteSortOrder
    """Likes received on comments in viral distribution."""
    viral_comments: AirbyteSortOrder
    """Number of comments in viral distribution of the ad."""
    viral_company_page_clicks: AirbyteSortOrder
    """Clicks on the company page in viral distribution."""
    viral_document_completions: AirbyteSortOrder
    """Complete views of documents in viral distribution."""
    viral_document_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of documents in viral distribution."""
    viral_document_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of documents in viral distribution."""
    viral_document_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of documents in viral distribution."""
    viral_download_clicks: AirbyteSortOrder
    """Clicks on downloads in viral distribution of the ad."""
    viral_external_website_conversions: AirbyteSortOrder
    """External website conversions in viral distribution."""
    viral_external_website_post_click_conversions: AirbyteSortOrder
    """Post-click conversions on external websites in viral distribution."""
    viral_external_website_post_view_conversions: AirbyteSortOrder
    """Post-view conversions on external websites in viral distribution."""
    viral_follows: AirbyteSortOrder
    """Follows generated in viral distribution of the ad."""
    viral_full_screen_plays: AirbyteSortOrder
    """Fullscreen video plays in viral distribution."""
    viral_impressions: AirbyteSortOrder
    """Total impressions in viral distribution of the ad."""
    viral_job_applications: AirbyteSortOrder
    """Job applications initiated in viral distribution."""
    viral_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button in viral distribution of the ad."""
    viral_landing_page_clicks: AirbyteSortOrder
    """Clicks on landing page in viral distribution."""
    viral_likes: AirbyteSortOrder
    """Total likes in viral distribution of the ad."""
    viral_one_click_lead_form_opens: AirbyteSortOrder
    """One-click lead form opens in viral distribution."""
    viral_one_click_leads: AirbyteSortOrder
    """Leads generated in one click in viral distribution."""
    viral_other_engagements: AirbyteSortOrder
    """Other engagements in viral distribution of the ad."""
    viral_post_click_job_applications: AirbyteSortOrder
    """Job applications initiated post-clicking in viral distribution."""
    viral_post_click_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-clicking in viral distribution."""
    viral_post_click_registrations: AirbyteSortOrder
    """Registrations completed post-clicking in viral distribution."""
    viral_post_view_job_applications: AirbyteSortOrder
    """Job applications initiated post-viewing in viral distribution."""
    viral_post_view_job_apply_clicks: AirbyteSortOrder
    """Clicks on apply job button post-viewing in viral distribution."""
    viral_post_view_registrations: AirbyteSortOrder
    """Registrations completed post-viewing in viral distribution."""
    viral_reactions: AirbyteSortOrder
    """Total reactions in viral distribution of the ad."""
    viral_registrations: AirbyteSortOrder
    """Total registrations in viral distribution of the ad."""
    viral_shares: AirbyteSortOrder
    """Total shares in viral distribution of the ad."""
    viral_total_engagements: AirbyteSortOrder
    """Total engagements in viral distribution of the ad."""
    viral_video_completions: AirbyteSortOrder
    """Completions of videos in viral distribution."""
    viral_video_first_quartile_completions: AirbyteSortOrder
    """First quartile completions of videos in viral distribution."""
    viral_video_midpoint_completions: AirbyteSortOrder
    """Midpoint completions of videos in viral distribution."""
    viral_video_starts: AirbyteSortOrder
    """Total video starts in viral distribution of the ad."""
    viral_video_third_quartile_completions: AirbyteSortOrder
    """Third quartile completions of videos in viral distribution."""
    viral_video_views: AirbyteSortOrder
    """Total views of videos in viral distribution of the ad."""
    pivot: AirbyteSortOrder
    """Pivot dimension used for this analytics record"""
    sponsored_campaign: AirbyteSortOrder
    """URN of the sponsored campaign this analytics record belongs to"""


# Entity-specific condition types for ad_member_seniority_analytics
class AdMemberSeniorityAnalyticsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdMemberSeniorityAnalyticsSearchFilter


class AdMemberSeniorityAnalyticsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdMemberSeniorityAnalyticsSearchFilter


class AdMemberSeniorityAnalyticsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdMemberSeniorityAnalyticsSearchFilter


class AdMemberSeniorityAnalyticsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdMemberSeniorityAnalyticsSearchFilter


class AdMemberSeniorityAnalyticsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdMemberSeniorityAnalyticsSearchFilter


class AdMemberSeniorityAnalyticsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdMemberSeniorityAnalyticsSearchFilter


class AdMemberSeniorityAnalyticsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AdMemberSeniorityAnalyticsStringFilter


class AdMemberSeniorityAnalyticsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AdMemberSeniorityAnalyticsStringFilter


class AdMemberSeniorityAnalyticsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdMemberSeniorityAnalyticsStringFilter


class AdMemberSeniorityAnalyticsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdMemberSeniorityAnalyticsStringFilter


class AdMemberSeniorityAnalyticsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: AdMemberSeniorityAnalyticsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdMemberSeniorityAnalyticsInCondition = TypedDict("AdMemberSeniorityAnalyticsInCondition", {"in": AdMemberSeniorityAnalyticsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdMemberSeniorityAnalyticsNotCondition = TypedDict("AdMemberSeniorityAnalyticsNotCondition", {"not": "AdMemberSeniorityAnalyticsCondition"}, total=False)
"""Negates the nested condition."""

AdMemberSeniorityAnalyticsAndCondition = TypedDict("AdMemberSeniorityAnalyticsAndCondition", {"and": "list[AdMemberSeniorityAnalyticsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdMemberSeniorityAnalyticsOrCondition = TypedDict("AdMemberSeniorityAnalyticsOrCondition", {"or": "list[AdMemberSeniorityAnalyticsCondition]"}, total=False)
"""True if any nested condition is true."""

AdMemberSeniorityAnalyticsAnyCondition = TypedDict("AdMemberSeniorityAnalyticsAnyCondition", {"any": AdMemberSeniorityAnalyticsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_member_seniority_analytics condition types
AdMemberSeniorityAnalyticsCondition = (
    AdMemberSeniorityAnalyticsEqCondition
    | AdMemberSeniorityAnalyticsNeqCondition
    | AdMemberSeniorityAnalyticsGtCondition
    | AdMemberSeniorityAnalyticsGteCondition
    | AdMemberSeniorityAnalyticsLtCondition
    | AdMemberSeniorityAnalyticsLteCondition
    | AdMemberSeniorityAnalyticsInCondition
    | AdMemberSeniorityAnalyticsStartswithCondition
    | AdMemberSeniorityAnalyticsEndswithCondition
    | AdMemberSeniorityAnalyticsFuzzyCondition
    | AdMemberSeniorityAnalyticsKeywordCondition
    | AdMemberSeniorityAnalyticsContainsCondition
    | AdMemberSeniorityAnalyticsNotCondition
    | AdMemberSeniorityAnalyticsAndCondition
    | AdMemberSeniorityAnalyticsOrCondition
    | AdMemberSeniorityAnalyticsAnyCondition
)


class AdMemberSeniorityAnalyticsSearchQuery(TypedDict, total=False):
    """Search query for ad_member_seniority_analytics entity."""
    filter: AdMemberSeniorityAnalyticsCondition
    sort: list[AdMemberSeniorityAnalyticsSortFilter]


# ===== LEAD_FORMS SEARCH TYPES =====

class LeadFormsSearchFilter(TypedDict, total=False):
    """Available fields for filtering lead_forms search queries."""
    id: int
    """Numerical identifier for the form."""
    name: str | None
    """Name of the Lead Form provided by the owner."""
    owner: dict[str, Any] | None
    """URN that identifies the owner of the Lead Form.
It's a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company account of the marketer.
"""
    state: str | None
    """Information about the current state of the Lead Form."""
    content: dict[str, Any] | None
    """Content of the Lead Form which will be displayed to the viewer."""
    created: int | None
    """An epoch time corresponding to the creation of the form."""
    last_modified: int | None
    """An epoch time corresponding to the last modified of of the form."""
    creation_locale: dict[str, Any] | None
    """Locale of the entity.
This field serves as the preferred locale for all fields within the Lead Form with an object type that is capable of localization, such as MultiLocaleString.
"""
    hidden_fields: list[Any] | None
    """Hidden fields used by the owner to track key attributes of the form that generated the lead.
The field is empty if the owner chooses to not append any tracking attributes to the Lead Form.
"""
    review_info: dict[str, Any] | None
    """Latest information about the content review of the Lead Form.
It will not be present if the form has not been reviewed by the review pipeline.
"""
    version_id: int | None
    """The version ID of the form. This is a derived field and is generated on the server side."""
    version_tag: str | None
    """The number of times the form has been modified."""


class LeadFormsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Numerical identifier for the form."""
    name: list[str]
    """Name of the Lead Form provided by the owner."""
    owner: list[dict[str, Any]]
    """URN that identifies the owner of the Lead Form.
It's a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company account of the marketer.
"""
    state: list[str]
    """Information about the current state of the Lead Form."""
    content: list[dict[str, Any]]
    """Content of the Lead Form which will be displayed to the viewer."""
    created: list[int]
    """An epoch time corresponding to the creation of the form."""
    last_modified: list[int]
    """An epoch time corresponding to the last modified of of the form."""
    creation_locale: list[dict[str, Any]]
    """Locale of the entity.
This field serves as the preferred locale for all fields within the Lead Form with an object type that is capable of localization, such as MultiLocaleString.
"""
    hidden_fields: list[list[Any]]
    """Hidden fields used by the owner to track key attributes of the form that generated the lead.
The field is empty if the owner chooses to not append any tracking attributes to the Lead Form.
"""
    review_info: list[dict[str, Any]]
    """Latest information about the content review of the Lead Form.
It will not be present if the form has not been reviewed by the review pipeline.
"""
    version_id: list[int]
    """The version ID of the form. This is a derived field and is generated on the server side."""
    version_tag: list[str]
    """The number of times the form has been modified."""


class LeadFormsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Numerical identifier for the form."""
    name: Any
    """Name of the Lead Form provided by the owner."""
    owner: Any
    """URN that identifies the owner of the Lead Form.
It's a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company account of the marketer.
"""
    state: Any
    """Information about the current state of the Lead Form."""
    content: Any
    """Content of the Lead Form which will be displayed to the viewer."""
    created: Any
    """An epoch time corresponding to the creation of the form."""
    last_modified: Any
    """An epoch time corresponding to the last modified of of the form."""
    creation_locale: Any
    """Locale of the entity.
This field serves as the preferred locale for all fields within the Lead Form with an object type that is capable of localization, such as MultiLocaleString.
"""
    hidden_fields: Any
    """Hidden fields used by the owner to track key attributes of the form that generated the lead.
The field is empty if the owner chooses to not append any tracking attributes to the Lead Form.
"""
    review_info: Any
    """Latest information about the content review of the Lead Form.
It will not be present if the form has not been reviewed by the review pipeline.
"""
    version_id: Any
    """The version ID of the form. This is a derived field and is generated on the server side."""
    version_tag: Any
    """The number of times the form has been modified."""


class LeadFormsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Numerical identifier for the form."""
    name: str
    """Name of the Lead Form provided by the owner."""
    owner: str
    """URN that identifies the owner of the Lead Form.
It's a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company account of the marketer.
"""
    state: str
    """Information about the current state of the Lead Form."""
    content: str
    """Content of the Lead Form which will be displayed to the viewer."""
    created: str
    """An epoch time corresponding to the creation of the form."""
    last_modified: str
    """An epoch time corresponding to the last modified of of the form."""
    creation_locale: str
    """Locale of the entity.
This field serves as the preferred locale for all fields within the Lead Form with an object type that is capable of localization, such as MultiLocaleString.
"""
    hidden_fields: str
    """Hidden fields used by the owner to track key attributes of the form that generated the lead.
The field is empty if the owner chooses to not append any tracking attributes to the Lead Form.
"""
    review_info: str
    """Latest information about the content review of the Lead Form.
It will not be present if the form has not been reviewed by the review pipeline.
"""
    version_id: str
    """The version ID of the form. This is a derived field and is generated on the server side."""
    version_tag: str
    """The number of times the form has been modified."""


class LeadFormsSortFilter(TypedDict, total=False):
    """Available fields for sorting lead_forms search results."""
    id: AirbyteSortOrder
    """Numerical identifier for the form."""
    name: AirbyteSortOrder
    """Name of the Lead Form provided by the owner."""
    owner: AirbyteSortOrder
    """URN that identifies the owner of the Lead Form.
It's a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company account of the marketer.
"""
    state: AirbyteSortOrder
    """Information about the current state of the Lead Form."""
    content: AirbyteSortOrder
    """Content of the Lead Form which will be displayed to the viewer."""
    created: AirbyteSortOrder
    """An epoch time corresponding to the creation of the form."""
    last_modified: AirbyteSortOrder
    """An epoch time corresponding to the last modified of of the form."""
    creation_locale: AirbyteSortOrder
    """Locale of the entity.
This field serves as the preferred locale for all fields within the Lead Form with an object type that is capable of localization, such as MultiLocaleString.
"""
    hidden_fields: AirbyteSortOrder
    """Hidden fields used by the owner to track key attributes of the form that generated the lead.
The field is empty if the owner chooses to not append any tracking attributes to the Lead Form.
"""
    review_info: AirbyteSortOrder
    """Latest information about the content review of the Lead Form.
It will not be present if the form has not been reviewed by the review pipeline.
"""
    version_id: AirbyteSortOrder
    """The version ID of the form. This is a derived field and is generated on the server side."""
    version_tag: AirbyteSortOrder
    """The number of times the form has been modified."""


# Entity-specific condition types for lead_forms
class LeadFormsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: LeadFormsSearchFilter


class LeadFormsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: LeadFormsSearchFilter


class LeadFormsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: LeadFormsSearchFilter


class LeadFormsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: LeadFormsSearchFilter


class LeadFormsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: LeadFormsSearchFilter


class LeadFormsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: LeadFormsSearchFilter


class LeadFormsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: LeadFormsStringFilter


class LeadFormsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: LeadFormsStringFilter


class LeadFormsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: LeadFormsStringFilter


class LeadFormsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: LeadFormsStringFilter


class LeadFormsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: LeadFormsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
LeadFormsInCondition = TypedDict("LeadFormsInCondition", {"in": LeadFormsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

LeadFormsNotCondition = TypedDict("LeadFormsNotCondition", {"not": "LeadFormsCondition"}, total=False)
"""Negates the nested condition."""

LeadFormsAndCondition = TypedDict("LeadFormsAndCondition", {"and": "list[LeadFormsCondition]"}, total=False)
"""True if all nested conditions are true."""

LeadFormsOrCondition = TypedDict("LeadFormsOrCondition", {"or": "list[LeadFormsCondition]"}, total=False)
"""True if any nested condition is true."""

LeadFormsAnyCondition = TypedDict("LeadFormsAnyCondition", {"any": LeadFormsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all lead_forms condition types
LeadFormsCondition = (
    LeadFormsEqCondition
    | LeadFormsNeqCondition
    | LeadFormsGtCondition
    | LeadFormsGteCondition
    | LeadFormsLtCondition
    | LeadFormsLteCondition
    | LeadFormsInCondition
    | LeadFormsStartswithCondition
    | LeadFormsEndswithCondition
    | LeadFormsFuzzyCondition
    | LeadFormsKeywordCondition
    | LeadFormsContainsCondition
    | LeadFormsNotCondition
    | LeadFormsAndCondition
    | LeadFormsOrCondition
    | LeadFormsAnyCondition
)


class LeadFormsSearchQuery(TypedDict, total=False):
    """Search query for lead_forms entity."""
    filter: LeadFormsCondition
    sort: list[LeadFormsSortFilter]


# ===== LEAD_FORM_RESPONSES SEARCH TYPES =====

class LeadFormResponsesSearchFilter(TypedDict, total=False):
    """Available fields for filtering lead_form_responses search queries."""
    id: str | None
    """Unique id to identify the Lead Form Response."""
    lead_type: str | None
    """Type of the lead representing the origination of the lead."""
    form: dict[str, Any] | None
    """URN identifying which form this FormResponse belongs to."""
    owner: dict[str, Any] | None
    """Owner of this Lead Form Response.
It is a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the ad account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company page of the advertiser.
"""
    owner_info: dict[str, Any] | None
    """Record containing entity info that owns this Lead Form Response. It's a optional Union of sponsoredAccountInfo and organizationInfo."""
    lead_metadata: dict[str, Any] | None
    """Metadata of a lead. This field is optional for test leads and other use cases where sponsored lead metadata (e.g. campaign) may not be relevant. If there is no value, the field is not returned."""
    lead_metadata_info: dict[str, Any] | None
    """Record containing a subset of fields resolved on demand from the lead metadata references (e.g. campaign name , campaign type). If there is no value, an empty object is returned."""
    associated_entity: dict[str, Any] | None
    """URN identifying which entity the lead is associated with. This field is optional for test leads and other use cases where leads don't have any associatedEntity. If there is no value, the field is not returned."""
    associated_entity_info: dict[str, Any] | None
    """Record containing useful fields (creative status, ugc reference etc.) resolved on demand from the associated entity object. If there is no value, an empty object is returned."""
    submitted_at: int | None
    """An epoch timestamp that recording when the form response was submitted."""
    response_id: dict[str, Any] | None
    """The unique identifier for the form response generated in the front-end when a submitter submits the response."""
    form_response: dict[str, Any] | None
    """Answers provided by the form submitter."""
    test_lead: bool | None
    """Whether this is a test lead created for testing purposes."""
    submitter: str | None
    """From version 202408 onwards, Guest Leads (when a user submits a form without being logged in) submitted to lead forms, submitter field is treated as a null field and omitted from the JSON response.
For non-guest leads, the submitter field will still be included in the response and will provide the person's URN. Ex: "submitter": "urn:li:person:MpGcnvaU_p".	Yes
"""
    versioned_lead_gen_form_urn: str | None
    """URN identifying which form this FormResponse belongs to."""


class LeadFormResponsesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique id to identify the Lead Form Response."""
    lead_type: list[str]
    """Type of the lead representing the origination of the lead."""
    form: list[dict[str, Any]]
    """URN identifying which form this FormResponse belongs to."""
    owner: list[dict[str, Any]]
    """Owner of this Lead Form Response.
It is a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the ad account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company page of the advertiser.
"""
    owner_info: list[dict[str, Any]]
    """Record containing entity info that owns this Lead Form Response. It's a optional Union of sponsoredAccountInfo and organizationInfo."""
    lead_metadata: list[dict[str, Any]]
    """Metadata of a lead. This field is optional for test leads and other use cases where sponsored lead metadata (e.g. campaign) may not be relevant. If there is no value, the field is not returned."""
    lead_metadata_info: list[dict[str, Any]]
    """Record containing a subset of fields resolved on demand from the lead metadata references (e.g. campaign name , campaign type). If there is no value, an empty object is returned."""
    associated_entity: list[dict[str, Any]]
    """URN identifying which entity the lead is associated with. This field is optional for test leads and other use cases where leads don't have any associatedEntity. If there is no value, the field is not returned."""
    associated_entity_info: list[dict[str, Any]]
    """Record containing useful fields (creative status, ugc reference etc.) resolved on demand from the associated entity object. If there is no value, an empty object is returned."""
    submitted_at: list[int]
    """An epoch timestamp that recording when the form response was submitted."""
    response_id: list[dict[str, Any]]
    """The unique identifier for the form response generated in the front-end when a submitter submits the response."""
    form_response: list[dict[str, Any]]
    """Answers provided by the form submitter."""
    test_lead: list[bool]
    """Whether this is a test lead created for testing purposes."""
    submitter: list[str]
    """From version 202408 onwards, Guest Leads (when a user submits a form without being logged in) submitted to lead forms, submitter field is treated as a null field and omitted from the JSON response.
For non-guest leads, the submitter field will still be included in the response and will provide the person's URN. Ex: "submitter": "urn:li:person:MpGcnvaU_p".	Yes
"""
    versioned_lead_gen_form_urn: list[str]
    """URN identifying which form this FormResponse belongs to."""


class LeadFormResponsesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique id to identify the Lead Form Response."""
    lead_type: Any
    """Type of the lead representing the origination of the lead."""
    form: Any
    """URN identifying which form this FormResponse belongs to."""
    owner: Any
    """Owner of this Lead Form Response.
It is a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the ad account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company page of the advertiser.
"""
    owner_info: Any
    """Record containing entity info that owns this Lead Form Response. It's a optional Union of sponsoredAccountInfo and organizationInfo."""
    lead_metadata: Any
    """Metadata of a lead. This field is optional for test leads and other use cases where sponsored lead metadata (e.g. campaign) may not be relevant. If there is no value, the field is not returned."""
    lead_metadata_info: Any
    """Record containing a subset of fields resolved on demand from the lead metadata references (e.g. campaign name , campaign type). If there is no value, an empty object is returned."""
    associated_entity: Any
    """URN identifying which entity the lead is associated with. This field is optional for test leads and other use cases where leads don't have any associatedEntity. If there is no value, the field is not returned."""
    associated_entity_info: Any
    """Record containing useful fields (creative status, ugc reference etc.) resolved on demand from the associated entity object. If there is no value, an empty object is returned."""
    submitted_at: Any
    """An epoch timestamp that recording when the form response was submitted."""
    response_id: Any
    """The unique identifier for the form response generated in the front-end when a submitter submits the response."""
    form_response: Any
    """Answers provided by the form submitter."""
    test_lead: Any
    """Whether this is a test lead created for testing purposes."""
    submitter: Any
    """From version 202408 onwards, Guest Leads (when a user submits a form without being logged in) submitted to lead forms, submitter field is treated as a null field and omitted from the JSON response.
For non-guest leads, the submitter field will still be included in the response and will provide the person's URN. Ex: "submitter": "urn:li:person:MpGcnvaU_p".	Yes
"""
    versioned_lead_gen_form_urn: Any
    """URN identifying which form this FormResponse belongs to."""


class LeadFormResponsesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique id to identify the Lead Form Response."""
    lead_type: str
    """Type of the lead representing the origination of the lead."""
    form: str
    """URN identifying which form this FormResponse belongs to."""
    owner: str
    """Owner of this Lead Form Response.
It is a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the ad account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company page of the advertiser.
"""
    owner_info: str
    """Record containing entity info that owns this Lead Form Response. It's a optional Union of sponsoredAccountInfo and organizationInfo."""
    lead_metadata: str
    """Metadata of a lead. This field is optional for test leads and other use cases where sponsored lead metadata (e.g. campaign) may not be relevant. If there is no value, the field is not returned."""
    lead_metadata_info: str
    """Record containing a subset of fields resolved on demand from the lead metadata references (e.g. campaign name , campaign type). If there is no value, an empty object is returned."""
    associated_entity: str
    """URN identifying which entity the lead is associated with. This field is optional for test leads and other use cases where leads don't have any associatedEntity. If there is no value, the field is not returned."""
    associated_entity_info: str
    """Record containing useful fields (creative status, ugc reference etc.) resolved on demand from the associated entity object. If there is no value, an empty object is returned."""
    submitted_at: str
    """An epoch timestamp that recording when the form response was submitted."""
    response_id: str
    """The unique identifier for the form response generated in the front-end when a submitter submits the response."""
    form_response: str
    """Answers provided by the form submitter."""
    test_lead: str
    """Whether this is a test lead created for testing purposes."""
    submitter: str
    """From version 202408 onwards, Guest Leads (when a user submits a form without being logged in) submitted to lead forms, submitter field is treated as a null field and omitted from the JSON response.
For non-guest leads, the submitter field will still be included in the response and will provide the person's URN. Ex: "submitter": "urn:li:person:MpGcnvaU_p".	Yes
"""
    versioned_lead_gen_form_urn: str
    """URN identifying which form this FormResponse belongs to."""


class LeadFormResponsesSortFilter(TypedDict, total=False):
    """Available fields for sorting lead_form_responses search results."""
    id: AirbyteSortOrder
    """Unique id to identify the Lead Form Response."""
    lead_type: AirbyteSortOrder
    """Type of the lead representing the origination of the lead."""
    form: AirbyteSortOrder
    """URN identifying which form this FormResponse belongs to."""
    owner: AirbyteSortOrder
    """Owner of this Lead Form Response.
It is a Union of sponsoredAccount and organization.
sponsoredAccount is an URN of SponsoredAccountUrn that indicates the ad account of the advertiser.
organization is an URN of OrganizationUrn that indicates the company page of the advertiser.
"""
    owner_info: AirbyteSortOrder
    """Record containing entity info that owns this Lead Form Response. It's a optional Union of sponsoredAccountInfo and organizationInfo."""
    lead_metadata: AirbyteSortOrder
    """Metadata of a lead. This field is optional for test leads and other use cases where sponsored lead metadata (e.g. campaign) may not be relevant. If there is no value, the field is not returned."""
    lead_metadata_info: AirbyteSortOrder
    """Record containing a subset of fields resolved on demand from the lead metadata references (e.g. campaign name , campaign type). If there is no value, an empty object is returned."""
    associated_entity: AirbyteSortOrder
    """URN identifying which entity the lead is associated with. This field is optional for test leads and other use cases where leads don't have any associatedEntity. If there is no value, the field is not returned."""
    associated_entity_info: AirbyteSortOrder
    """Record containing useful fields (creative status, ugc reference etc.) resolved on demand from the associated entity object. If there is no value, an empty object is returned."""
    submitted_at: AirbyteSortOrder
    """An epoch timestamp that recording when the form response was submitted."""
    response_id: AirbyteSortOrder
    """The unique identifier for the form response generated in the front-end when a submitter submits the response."""
    form_response: AirbyteSortOrder
    """Answers provided by the form submitter."""
    test_lead: AirbyteSortOrder
    """Whether this is a test lead created for testing purposes."""
    submitter: AirbyteSortOrder
    """From version 202408 onwards, Guest Leads (when a user submits a form without being logged in) submitted to lead forms, submitter field is treated as a null field and omitted from the JSON response.
For non-guest leads, the submitter field will still be included in the response and will provide the person's URN. Ex: "submitter": "urn:li:person:MpGcnvaU_p".	Yes
"""
    versioned_lead_gen_form_urn: AirbyteSortOrder
    """URN identifying which form this FormResponse belongs to."""


# Entity-specific condition types for lead_form_responses
class LeadFormResponsesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: LeadFormResponsesSearchFilter


class LeadFormResponsesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: LeadFormResponsesSearchFilter


class LeadFormResponsesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: LeadFormResponsesSearchFilter


class LeadFormResponsesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: LeadFormResponsesSearchFilter


class LeadFormResponsesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: LeadFormResponsesSearchFilter


class LeadFormResponsesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: LeadFormResponsesSearchFilter


class LeadFormResponsesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: LeadFormResponsesStringFilter


class LeadFormResponsesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: LeadFormResponsesStringFilter


class LeadFormResponsesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: LeadFormResponsesStringFilter


class LeadFormResponsesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: LeadFormResponsesStringFilter


class LeadFormResponsesContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: LeadFormResponsesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
LeadFormResponsesInCondition = TypedDict("LeadFormResponsesInCondition", {"in": LeadFormResponsesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

LeadFormResponsesNotCondition = TypedDict("LeadFormResponsesNotCondition", {"not": "LeadFormResponsesCondition"}, total=False)
"""Negates the nested condition."""

LeadFormResponsesAndCondition = TypedDict("LeadFormResponsesAndCondition", {"and": "list[LeadFormResponsesCondition]"}, total=False)
"""True if all nested conditions are true."""

LeadFormResponsesOrCondition = TypedDict("LeadFormResponsesOrCondition", {"or": "list[LeadFormResponsesCondition]"}, total=False)
"""True if any nested condition is true."""

LeadFormResponsesAnyCondition = TypedDict("LeadFormResponsesAnyCondition", {"any": LeadFormResponsesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all lead_form_responses condition types
LeadFormResponsesCondition = (
    LeadFormResponsesEqCondition
    | LeadFormResponsesNeqCondition
    | LeadFormResponsesGtCondition
    | LeadFormResponsesGteCondition
    | LeadFormResponsesLtCondition
    | LeadFormResponsesLteCondition
    | LeadFormResponsesInCondition
    | LeadFormResponsesStartswithCondition
    | LeadFormResponsesEndswithCondition
    | LeadFormResponsesFuzzyCondition
    | LeadFormResponsesKeywordCondition
    | LeadFormResponsesContainsCondition
    | LeadFormResponsesNotCondition
    | LeadFormResponsesAndCondition
    | LeadFormResponsesOrCondition
    | LeadFormResponsesAnyCondition
)


class LeadFormResponsesSearchQuery(TypedDict, total=False):
    """Search query for lead_form_responses entity."""
    filter: LeadFormResponsesCondition
    sort: list[LeadFormResponsesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
