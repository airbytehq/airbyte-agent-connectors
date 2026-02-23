"""
Type definitions for google-ads connector.
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

class AccessibleCustomersListParams(TypedDict):
    """Parameters for accessible_customers.list operation"""
    pass

class AccountsListParams(TypedDict):
    """Parameters for accounts.list operation"""
    query: NotRequired[str]
    page_token: NotRequired[str]
    page_size: NotRequired[int]
    customer_id: str

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    query: NotRequired[str]
    page_token: NotRequired[str]
    page_size: NotRequired[int]
    customer_id: str

class AdGroupsListParams(TypedDict):
    """Parameters for ad_groups.list operation"""
    query: NotRequired[str]
    page_token: NotRequired[str]
    page_size: NotRequired[int]
    customer_id: str

class AdGroupAdsListParams(TypedDict):
    """Parameters for ad_group_ads.list operation"""
    query: NotRequired[str]
    page_token: NotRequired[str]
    page_size: NotRequired[int]
    customer_id: str

class CampaignLabelsListParams(TypedDict):
    """Parameters for campaign_labels.list operation"""
    query: NotRequired[str]
    page_token: NotRequired[str]
    page_size: NotRequired[int]
    customer_id: str

class AdGroupLabelsListParams(TypedDict):
    """Parameters for ad_group_labels.list operation"""
    query: NotRequired[str]
    page_token: NotRequired[str]
    page_size: NotRequired[int]
    customer_id: str

class AdGroupAdLabelsListParams(TypedDict):
    """Parameters for ad_group_ad_labels.list operation"""
    query: NotRequired[str]
    page_token: NotRequired[str]
    page_size: NotRequired[int]
    customer_id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ACCOUNTS SEARCH TYPES =====

class AccountsSearchFilter(TypedDict, total=False):
    """Available fields for filtering accounts search queries."""
    customer_auto_tagging_enabled: bool | None
    """Whether auto-tagging is enabled for the account"""
    customer_call_reporting_setting_call_conversion_action: str | None
    """Call conversion action resource name"""
    customer_call_reporting_setting_call_conversion_reporting_enabled: bool | None
    """Whether call conversion reporting is enabled"""
    customer_call_reporting_setting_call_reporting_enabled: bool | None
    """Whether call reporting is enabled"""
    customer_conversion_tracking_setting_conversion_tracking_id: int | None
    """Conversion tracking ID"""
    customer_conversion_tracking_setting_cross_account_conversion_tracking_id: int | None
    """Cross-account conversion tracking ID"""
    customer_currency_code: str | None
    """Currency code for the account (e.g., USD)"""
    customer_descriptive_name: str | None
    """Descriptive name of the customer account"""
    customer_final_url_suffix: str | None
    """URL suffix appended to final URLs"""
    customer_has_partners_badge: bool | None
    """Whether the account has a Google Partners badge"""
    customer_id: int | None
    """Unique customer account ID"""
    customer_manager: bool | None
    """Whether this is a manager (MCC) account"""
    customer_optimization_score: float | None
    """Optimization score for the account (0.0 to 1.0)"""
    customer_optimization_score_weight: float | None
    """Weight of the optimization score"""
    customer_pay_per_conversion_eligibility_failure_reasons: list[Any] | None
    """Reasons why pay-per-conversion is not eligible"""
    customer_remarketing_setting_google_global_site_tag: str | None
    """Google global site tag snippet"""
    customer_resource_name: str | None
    """Resource name of the customer"""
    customer_test_account: bool | None
    """Whether this is a test account"""
    customer_time_zone: str | None
    """Time zone of the account"""
    customer_tracking_url_template: str | None
    """Tracking URL template for the account"""
    segments_date: str | None
    """Date segment for the report row"""


class AccountsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    customer_auto_tagging_enabled: list[bool]
    """Whether auto-tagging is enabled for the account"""
    customer_call_reporting_setting_call_conversion_action: list[str]
    """Call conversion action resource name"""
    customer_call_reporting_setting_call_conversion_reporting_enabled: list[bool]
    """Whether call conversion reporting is enabled"""
    customer_call_reporting_setting_call_reporting_enabled: list[bool]
    """Whether call reporting is enabled"""
    customer_conversion_tracking_setting_conversion_tracking_id: list[int]
    """Conversion tracking ID"""
    customer_conversion_tracking_setting_cross_account_conversion_tracking_id: list[int]
    """Cross-account conversion tracking ID"""
    customer_currency_code: list[str]
    """Currency code for the account (e.g., USD)"""
    customer_descriptive_name: list[str]
    """Descriptive name of the customer account"""
    customer_final_url_suffix: list[str]
    """URL suffix appended to final URLs"""
    customer_has_partners_badge: list[bool]
    """Whether the account has a Google Partners badge"""
    customer_id: list[int]
    """Unique customer account ID"""
    customer_manager: list[bool]
    """Whether this is a manager (MCC) account"""
    customer_optimization_score: list[float]
    """Optimization score for the account (0.0 to 1.0)"""
    customer_optimization_score_weight: list[float]
    """Weight of the optimization score"""
    customer_pay_per_conversion_eligibility_failure_reasons: list[list[Any]]
    """Reasons why pay-per-conversion is not eligible"""
    customer_remarketing_setting_google_global_site_tag: list[str]
    """Google global site tag snippet"""
    customer_resource_name: list[str]
    """Resource name of the customer"""
    customer_test_account: list[bool]
    """Whether this is a test account"""
    customer_time_zone: list[str]
    """Time zone of the account"""
    customer_tracking_url_template: list[str]
    """Tracking URL template for the account"""
    segments_date: list[str]
    """Date segment for the report row"""


class AccountsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    customer_auto_tagging_enabled: Any
    """Whether auto-tagging is enabled for the account"""
    customer_call_reporting_setting_call_conversion_action: Any
    """Call conversion action resource name"""
    customer_call_reporting_setting_call_conversion_reporting_enabled: Any
    """Whether call conversion reporting is enabled"""
    customer_call_reporting_setting_call_reporting_enabled: Any
    """Whether call reporting is enabled"""
    customer_conversion_tracking_setting_conversion_tracking_id: Any
    """Conversion tracking ID"""
    customer_conversion_tracking_setting_cross_account_conversion_tracking_id: Any
    """Cross-account conversion tracking ID"""
    customer_currency_code: Any
    """Currency code for the account (e.g., USD)"""
    customer_descriptive_name: Any
    """Descriptive name of the customer account"""
    customer_final_url_suffix: Any
    """URL suffix appended to final URLs"""
    customer_has_partners_badge: Any
    """Whether the account has a Google Partners badge"""
    customer_id: Any
    """Unique customer account ID"""
    customer_manager: Any
    """Whether this is a manager (MCC) account"""
    customer_optimization_score: Any
    """Optimization score for the account (0.0 to 1.0)"""
    customer_optimization_score_weight: Any
    """Weight of the optimization score"""
    customer_pay_per_conversion_eligibility_failure_reasons: Any
    """Reasons why pay-per-conversion is not eligible"""
    customer_remarketing_setting_google_global_site_tag: Any
    """Google global site tag snippet"""
    customer_resource_name: Any
    """Resource name of the customer"""
    customer_test_account: Any
    """Whether this is a test account"""
    customer_time_zone: Any
    """Time zone of the account"""
    customer_tracking_url_template: Any
    """Tracking URL template for the account"""
    segments_date: Any
    """Date segment for the report row"""


class AccountsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    customer_auto_tagging_enabled: str
    """Whether auto-tagging is enabled for the account"""
    customer_call_reporting_setting_call_conversion_action: str
    """Call conversion action resource name"""
    customer_call_reporting_setting_call_conversion_reporting_enabled: str
    """Whether call conversion reporting is enabled"""
    customer_call_reporting_setting_call_reporting_enabled: str
    """Whether call reporting is enabled"""
    customer_conversion_tracking_setting_conversion_tracking_id: str
    """Conversion tracking ID"""
    customer_conversion_tracking_setting_cross_account_conversion_tracking_id: str
    """Cross-account conversion tracking ID"""
    customer_currency_code: str
    """Currency code for the account (e.g., USD)"""
    customer_descriptive_name: str
    """Descriptive name of the customer account"""
    customer_final_url_suffix: str
    """URL suffix appended to final URLs"""
    customer_has_partners_badge: str
    """Whether the account has a Google Partners badge"""
    customer_id: str
    """Unique customer account ID"""
    customer_manager: str
    """Whether this is a manager (MCC) account"""
    customer_optimization_score: str
    """Optimization score for the account (0.0 to 1.0)"""
    customer_optimization_score_weight: str
    """Weight of the optimization score"""
    customer_pay_per_conversion_eligibility_failure_reasons: str
    """Reasons why pay-per-conversion is not eligible"""
    customer_remarketing_setting_google_global_site_tag: str
    """Google global site tag snippet"""
    customer_resource_name: str
    """Resource name of the customer"""
    customer_test_account: str
    """Whether this is a test account"""
    customer_time_zone: str
    """Time zone of the account"""
    customer_tracking_url_template: str
    """Tracking URL template for the account"""
    segments_date: str
    """Date segment for the report row"""


class AccountsSortFilter(TypedDict, total=False):
    """Available fields for sorting accounts search results."""
    customer_auto_tagging_enabled: AirbyteSortOrder
    """Whether auto-tagging is enabled for the account"""
    customer_call_reporting_setting_call_conversion_action: AirbyteSortOrder
    """Call conversion action resource name"""
    customer_call_reporting_setting_call_conversion_reporting_enabled: AirbyteSortOrder
    """Whether call conversion reporting is enabled"""
    customer_call_reporting_setting_call_reporting_enabled: AirbyteSortOrder
    """Whether call reporting is enabled"""
    customer_conversion_tracking_setting_conversion_tracking_id: AirbyteSortOrder
    """Conversion tracking ID"""
    customer_conversion_tracking_setting_cross_account_conversion_tracking_id: AirbyteSortOrder
    """Cross-account conversion tracking ID"""
    customer_currency_code: AirbyteSortOrder
    """Currency code for the account (e.g., USD)"""
    customer_descriptive_name: AirbyteSortOrder
    """Descriptive name of the customer account"""
    customer_final_url_suffix: AirbyteSortOrder
    """URL suffix appended to final URLs"""
    customer_has_partners_badge: AirbyteSortOrder
    """Whether the account has a Google Partners badge"""
    customer_id: AirbyteSortOrder
    """Unique customer account ID"""
    customer_manager: AirbyteSortOrder
    """Whether this is a manager (MCC) account"""
    customer_optimization_score: AirbyteSortOrder
    """Optimization score for the account (0.0 to 1.0)"""
    customer_optimization_score_weight: AirbyteSortOrder
    """Weight of the optimization score"""
    customer_pay_per_conversion_eligibility_failure_reasons: AirbyteSortOrder
    """Reasons why pay-per-conversion is not eligible"""
    customer_remarketing_setting_google_global_site_tag: AirbyteSortOrder
    """Google global site tag snippet"""
    customer_resource_name: AirbyteSortOrder
    """Resource name of the customer"""
    customer_test_account: AirbyteSortOrder
    """Whether this is a test account"""
    customer_time_zone: AirbyteSortOrder
    """Time zone of the account"""
    customer_tracking_url_template: AirbyteSortOrder
    """Tracking URL template for the account"""
    segments_date: AirbyteSortOrder
    """Date segment for the report row"""


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


# ===== CAMPAIGNS SEARCH TYPES =====

class CampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaigns search queries."""
    campaign_id: int | None
    """Campaign ID"""
    campaign_name: str | None
    """Campaign name"""
    campaign_status: str | None
    """Campaign status (ENABLED, PAUSED, REMOVED)"""
    campaign_advertising_channel_type: str | None
    """Advertising channel type (SEARCH, DISPLAY, etc.)"""
    campaign_advertising_channel_sub_type: str | None
    """Advertising channel sub-type"""
    campaign_bidding_strategy: str | None
    """Bidding strategy resource name"""
    campaign_bidding_strategy_type: str | None
    """Bidding strategy type"""
    campaign_campaign_budget: str | None
    """Campaign budget resource name"""
    campaign_budget_amount_micros: int | None
    """Campaign budget amount in micros"""
    campaign_start_date: str | None
    """Campaign start date"""
    campaign_end_date: str | None
    """Campaign end date"""
    campaign_serving_status: str | None
    """Campaign serving status"""
    campaign_resource_name: str | None
    """Resource name of the campaign"""
    campaign_labels: list[Any] | None
    """Labels applied to the campaign"""
    campaign_network_settings_target_google_search: bool | None
    """Whether targeting Google Search"""
    campaign_network_settings_target_search_network: bool | None
    """Whether targeting search network"""
    campaign_network_settings_target_content_network: bool | None
    """Whether targeting content network"""
    campaign_network_settings_target_partner_search_network: bool | None
    """Whether targeting partner search network"""
    metrics_clicks: int | None
    """Number of clicks"""
    metrics_ctr: float | None
    """Click-through rate"""
    metrics_conversions: float | None
    """Number of conversions"""
    metrics_conversions_value: float | None
    """Total conversions value"""
    metrics_cost_micros: int | None
    """Cost in micros"""
    metrics_impressions: int | None
    """Number of impressions"""
    metrics_average_cpc: float | None
    """Average cost per click"""
    metrics_average_cpm: float | None
    """Average cost per thousand impressions"""
    metrics_interactions: int | None
    """Number of interactions"""
    segments_date: str | None
    """Date segment for the report row"""
    segments_hour: int | None
    """Hour segment"""
    segments_ad_network_type: str | None
    """Ad network type segment"""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    campaign_id: list[int]
    """Campaign ID"""
    campaign_name: list[str]
    """Campaign name"""
    campaign_status: list[str]
    """Campaign status (ENABLED, PAUSED, REMOVED)"""
    campaign_advertising_channel_type: list[str]
    """Advertising channel type (SEARCH, DISPLAY, etc.)"""
    campaign_advertising_channel_sub_type: list[str]
    """Advertising channel sub-type"""
    campaign_bidding_strategy: list[str]
    """Bidding strategy resource name"""
    campaign_bidding_strategy_type: list[str]
    """Bidding strategy type"""
    campaign_campaign_budget: list[str]
    """Campaign budget resource name"""
    campaign_budget_amount_micros: list[int]
    """Campaign budget amount in micros"""
    campaign_start_date: list[str]
    """Campaign start date"""
    campaign_end_date: list[str]
    """Campaign end date"""
    campaign_serving_status: list[str]
    """Campaign serving status"""
    campaign_resource_name: list[str]
    """Resource name of the campaign"""
    campaign_labels: list[list[Any]]
    """Labels applied to the campaign"""
    campaign_network_settings_target_google_search: list[bool]
    """Whether targeting Google Search"""
    campaign_network_settings_target_search_network: list[bool]
    """Whether targeting search network"""
    campaign_network_settings_target_content_network: list[bool]
    """Whether targeting content network"""
    campaign_network_settings_target_partner_search_network: list[bool]
    """Whether targeting partner search network"""
    metrics_clicks: list[int]
    """Number of clicks"""
    metrics_ctr: list[float]
    """Click-through rate"""
    metrics_conversions: list[float]
    """Number of conversions"""
    metrics_conversions_value: list[float]
    """Total conversions value"""
    metrics_cost_micros: list[int]
    """Cost in micros"""
    metrics_impressions: list[int]
    """Number of impressions"""
    metrics_average_cpc: list[float]
    """Average cost per click"""
    metrics_average_cpm: list[float]
    """Average cost per thousand impressions"""
    metrics_interactions: list[int]
    """Number of interactions"""
    segments_date: list[str]
    """Date segment for the report row"""
    segments_hour: list[int]
    """Hour segment"""
    segments_ad_network_type: list[str]
    """Ad network type segment"""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    campaign_id: Any
    """Campaign ID"""
    campaign_name: Any
    """Campaign name"""
    campaign_status: Any
    """Campaign status (ENABLED, PAUSED, REMOVED)"""
    campaign_advertising_channel_type: Any
    """Advertising channel type (SEARCH, DISPLAY, etc.)"""
    campaign_advertising_channel_sub_type: Any
    """Advertising channel sub-type"""
    campaign_bidding_strategy: Any
    """Bidding strategy resource name"""
    campaign_bidding_strategy_type: Any
    """Bidding strategy type"""
    campaign_campaign_budget: Any
    """Campaign budget resource name"""
    campaign_budget_amount_micros: Any
    """Campaign budget amount in micros"""
    campaign_start_date: Any
    """Campaign start date"""
    campaign_end_date: Any
    """Campaign end date"""
    campaign_serving_status: Any
    """Campaign serving status"""
    campaign_resource_name: Any
    """Resource name of the campaign"""
    campaign_labels: Any
    """Labels applied to the campaign"""
    campaign_network_settings_target_google_search: Any
    """Whether targeting Google Search"""
    campaign_network_settings_target_search_network: Any
    """Whether targeting search network"""
    campaign_network_settings_target_content_network: Any
    """Whether targeting content network"""
    campaign_network_settings_target_partner_search_network: Any
    """Whether targeting partner search network"""
    metrics_clicks: Any
    """Number of clicks"""
    metrics_ctr: Any
    """Click-through rate"""
    metrics_conversions: Any
    """Number of conversions"""
    metrics_conversions_value: Any
    """Total conversions value"""
    metrics_cost_micros: Any
    """Cost in micros"""
    metrics_impressions: Any
    """Number of impressions"""
    metrics_average_cpc: Any
    """Average cost per click"""
    metrics_average_cpm: Any
    """Average cost per thousand impressions"""
    metrics_interactions: Any
    """Number of interactions"""
    segments_date: Any
    """Date segment for the report row"""
    segments_hour: Any
    """Hour segment"""
    segments_ad_network_type: Any
    """Ad network type segment"""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    campaign_id: str
    """Campaign ID"""
    campaign_name: str
    """Campaign name"""
    campaign_status: str
    """Campaign status (ENABLED, PAUSED, REMOVED)"""
    campaign_advertising_channel_type: str
    """Advertising channel type (SEARCH, DISPLAY, etc.)"""
    campaign_advertising_channel_sub_type: str
    """Advertising channel sub-type"""
    campaign_bidding_strategy: str
    """Bidding strategy resource name"""
    campaign_bidding_strategy_type: str
    """Bidding strategy type"""
    campaign_campaign_budget: str
    """Campaign budget resource name"""
    campaign_budget_amount_micros: str
    """Campaign budget amount in micros"""
    campaign_start_date: str
    """Campaign start date"""
    campaign_end_date: str
    """Campaign end date"""
    campaign_serving_status: str
    """Campaign serving status"""
    campaign_resource_name: str
    """Resource name of the campaign"""
    campaign_labels: str
    """Labels applied to the campaign"""
    campaign_network_settings_target_google_search: str
    """Whether targeting Google Search"""
    campaign_network_settings_target_search_network: str
    """Whether targeting search network"""
    campaign_network_settings_target_content_network: str
    """Whether targeting content network"""
    campaign_network_settings_target_partner_search_network: str
    """Whether targeting partner search network"""
    metrics_clicks: str
    """Number of clicks"""
    metrics_ctr: str
    """Click-through rate"""
    metrics_conversions: str
    """Number of conversions"""
    metrics_conversions_value: str
    """Total conversions value"""
    metrics_cost_micros: str
    """Cost in micros"""
    metrics_impressions: str
    """Number of impressions"""
    metrics_average_cpc: str
    """Average cost per click"""
    metrics_average_cpm: str
    """Average cost per thousand impressions"""
    metrics_interactions: str
    """Number of interactions"""
    segments_date: str
    """Date segment for the report row"""
    segments_hour: str
    """Hour segment"""
    segments_ad_network_type: str
    """Ad network type segment"""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    campaign_id: AirbyteSortOrder
    """Campaign ID"""
    campaign_name: AirbyteSortOrder
    """Campaign name"""
    campaign_status: AirbyteSortOrder
    """Campaign status (ENABLED, PAUSED, REMOVED)"""
    campaign_advertising_channel_type: AirbyteSortOrder
    """Advertising channel type (SEARCH, DISPLAY, etc.)"""
    campaign_advertising_channel_sub_type: AirbyteSortOrder
    """Advertising channel sub-type"""
    campaign_bidding_strategy: AirbyteSortOrder
    """Bidding strategy resource name"""
    campaign_bidding_strategy_type: AirbyteSortOrder
    """Bidding strategy type"""
    campaign_campaign_budget: AirbyteSortOrder
    """Campaign budget resource name"""
    campaign_budget_amount_micros: AirbyteSortOrder
    """Campaign budget amount in micros"""
    campaign_start_date: AirbyteSortOrder
    """Campaign start date"""
    campaign_end_date: AirbyteSortOrder
    """Campaign end date"""
    campaign_serving_status: AirbyteSortOrder
    """Campaign serving status"""
    campaign_resource_name: AirbyteSortOrder
    """Resource name of the campaign"""
    campaign_labels: AirbyteSortOrder
    """Labels applied to the campaign"""
    campaign_network_settings_target_google_search: AirbyteSortOrder
    """Whether targeting Google Search"""
    campaign_network_settings_target_search_network: AirbyteSortOrder
    """Whether targeting search network"""
    campaign_network_settings_target_content_network: AirbyteSortOrder
    """Whether targeting content network"""
    campaign_network_settings_target_partner_search_network: AirbyteSortOrder
    """Whether targeting partner search network"""
    metrics_clicks: AirbyteSortOrder
    """Number of clicks"""
    metrics_ctr: AirbyteSortOrder
    """Click-through rate"""
    metrics_conversions: AirbyteSortOrder
    """Number of conversions"""
    metrics_conversions_value: AirbyteSortOrder
    """Total conversions value"""
    metrics_cost_micros: AirbyteSortOrder
    """Cost in micros"""
    metrics_impressions: AirbyteSortOrder
    """Number of impressions"""
    metrics_average_cpc: AirbyteSortOrder
    """Average cost per click"""
    metrics_average_cpm: AirbyteSortOrder
    """Average cost per thousand impressions"""
    metrics_interactions: AirbyteSortOrder
    """Number of interactions"""
    segments_date: AirbyteSortOrder
    """Date segment for the report row"""
    segments_hour: AirbyteSortOrder
    """Hour segment"""
    segments_ad_network_type: AirbyteSortOrder
    """Ad network type segment"""


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
    campaign_id: int | None
    """Parent campaign ID"""
    ad_group_id: int | None
    """Ad group ID"""
    ad_group_name: str | None
    """Ad group name"""
    ad_group_status: str | None
    """Ad group status (ENABLED, PAUSED, REMOVED)"""
    ad_group_type: str | None
    """Ad group type"""
    ad_group_ad_rotation_mode: str | None
    """Ad rotation mode"""
    ad_group_base_ad_group: str | None
    """Base ad group resource name"""
    ad_group_campaign: str | None
    """Parent campaign resource name"""
    ad_group_cpc_bid_micros: int | None
    """CPC bid in micros"""
    ad_group_cpm_bid_micros: int | None
    """CPM bid in micros"""
    ad_group_cpv_bid_micros: int | None
    """CPV bid in micros"""
    ad_group_effective_target_cpa_micros: int | None
    """Effective target CPA in micros"""
    ad_group_effective_target_cpa_source: str | None
    """Source of the effective target CPA"""
    ad_group_effective_target_roas: float | None
    """Effective target ROAS"""
    ad_group_effective_target_roas_source: str | None
    """Source of the effective target ROAS"""
    ad_group_labels: list[Any] | None
    """Labels applied to the ad group"""
    ad_group_resource_name: str | None
    """Resource name of the ad group"""
    ad_group_target_cpa_micros: int | None
    """Target CPA in micros"""
    ad_group_target_roas: float | None
    """Target ROAS"""
    ad_group_tracking_url_template: str | None
    """Tracking URL template"""
    metrics_cost_micros: int | None
    """Cost in micros"""
    segments_date: str | None
    """Date segment for the report row"""


class AdGroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    campaign_id: list[int]
    """Parent campaign ID"""
    ad_group_id: list[int]
    """Ad group ID"""
    ad_group_name: list[str]
    """Ad group name"""
    ad_group_status: list[str]
    """Ad group status (ENABLED, PAUSED, REMOVED)"""
    ad_group_type: list[str]
    """Ad group type"""
    ad_group_ad_rotation_mode: list[str]
    """Ad rotation mode"""
    ad_group_base_ad_group: list[str]
    """Base ad group resource name"""
    ad_group_campaign: list[str]
    """Parent campaign resource name"""
    ad_group_cpc_bid_micros: list[int]
    """CPC bid in micros"""
    ad_group_cpm_bid_micros: list[int]
    """CPM bid in micros"""
    ad_group_cpv_bid_micros: list[int]
    """CPV bid in micros"""
    ad_group_effective_target_cpa_micros: list[int]
    """Effective target CPA in micros"""
    ad_group_effective_target_cpa_source: list[str]
    """Source of the effective target CPA"""
    ad_group_effective_target_roas: list[float]
    """Effective target ROAS"""
    ad_group_effective_target_roas_source: list[str]
    """Source of the effective target ROAS"""
    ad_group_labels: list[list[Any]]
    """Labels applied to the ad group"""
    ad_group_resource_name: list[str]
    """Resource name of the ad group"""
    ad_group_target_cpa_micros: list[int]
    """Target CPA in micros"""
    ad_group_target_roas: list[float]
    """Target ROAS"""
    ad_group_tracking_url_template: list[str]
    """Tracking URL template"""
    metrics_cost_micros: list[int]
    """Cost in micros"""
    segments_date: list[str]
    """Date segment for the report row"""


class AdGroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    campaign_id: Any
    """Parent campaign ID"""
    ad_group_id: Any
    """Ad group ID"""
    ad_group_name: Any
    """Ad group name"""
    ad_group_status: Any
    """Ad group status (ENABLED, PAUSED, REMOVED)"""
    ad_group_type: Any
    """Ad group type"""
    ad_group_ad_rotation_mode: Any
    """Ad rotation mode"""
    ad_group_base_ad_group: Any
    """Base ad group resource name"""
    ad_group_campaign: Any
    """Parent campaign resource name"""
    ad_group_cpc_bid_micros: Any
    """CPC bid in micros"""
    ad_group_cpm_bid_micros: Any
    """CPM bid in micros"""
    ad_group_cpv_bid_micros: Any
    """CPV bid in micros"""
    ad_group_effective_target_cpa_micros: Any
    """Effective target CPA in micros"""
    ad_group_effective_target_cpa_source: Any
    """Source of the effective target CPA"""
    ad_group_effective_target_roas: Any
    """Effective target ROAS"""
    ad_group_effective_target_roas_source: Any
    """Source of the effective target ROAS"""
    ad_group_labels: Any
    """Labels applied to the ad group"""
    ad_group_resource_name: Any
    """Resource name of the ad group"""
    ad_group_target_cpa_micros: Any
    """Target CPA in micros"""
    ad_group_target_roas: Any
    """Target ROAS"""
    ad_group_tracking_url_template: Any
    """Tracking URL template"""
    metrics_cost_micros: Any
    """Cost in micros"""
    segments_date: Any
    """Date segment for the report row"""


class AdGroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    campaign_id: str
    """Parent campaign ID"""
    ad_group_id: str
    """Ad group ID"""
    ad_group_name: str
    """Ad group name"""
    ad_group_status: str
    """Ad group status (ENABLED, PAUSED, REMOVED)"""
    ad_group_type: str
    """Ad group type"""
    ad_group_ad_rotation_mode: str
    """Ad rotation mode"""
    ad_group_base_ad_group: str
    """Base ad group resource name"""
    ad_group_campaign: str
    """Parent campaign resource name"""
    ad_group_cpc_bid_micros: str
    """CPC bid in micros"""
    ad_group_cpm_bid_micros: str
    """CPM bid in micros"""
    ad_group_cpv_bid_micros: str
    """CPV bid in micros"""
    ad_group_effective_target_cpa_micros: str
    """Effective target CPA in micros"""
    ad_group_effective_target_cpa_source: str
    """Source of the effective target CPA"""
    ad_group_effective_target_roas: str
    """Effective target ROAS"""
    ad_group_effective_target_roas_source: str
    """Source of the effective target ROAS"""
    ad_group_labels: str
    """Labels applied to the ad group"""
    ad_group_resource_name: str
    """Resource name of the ad group"""
    ad_group_target_cpa_micros: str
    """Target CPA in micros"""
    ad_group_target_roas: str
    """Target ROAS"""
    ad_group_tracking_url_template: str
    """Tracking URL template"""
    metrics_cost_micros: str
    """Cost in micros"""
    segments_date: str
    """Date segment for the report row"""


class AdGroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_groups search results."""
    campaign_id: AirbyteSortOrder
    """Parent campaign ID"""
    ad_group_id: AirbyteSortOrder
    """Ad group ID"""
    ad_group_name: AirbyteSortOrder
    """Ad group name"""
    ad_group_status: AirbyteSortOrder
    """Ad group status (ENABLED, PAUSED, REMOVED)"""
    ad_group_type: AirbyteSortOrder
    """Ad group type"""
    ad_group_ad_rotation_mode: AirbyteSortOrder
    """Ad rotation mode"""
    ad_group_base_ad_group: AirbyteSortOrder
    """Base ad group resource name"""
    ad_group_campaign: AirbyteSortOrder
    """Parent campaign resource name"""
    ad_group_cpc_bid_micros: AirbyteSortOrder
    """CPC bid in micros"""
    ad_group_cpm_bid_micros: AirbyteSortOrder
    """CPM bid in micros"""
    ad_group_cpv_bid_micros: AirbyteSortOrder
    """CPV bid in micros"""
    ad_group_effective_target_cpa_micros: AirbyteSortOrder
    """Effective target CPA in micros"""
    ad_group_effective_target_cpa_source: AirbyteSortOrder
    """Source of the effective target CPA"""
    ad_group_effective_target_roas: AirbyteSortOrder
    """Effective target ROAS"""
    ad_group_effective_target_roas_source: AirbyteSortOrder
    """Source of the effective target ROAS"""
    ad_group_labels: AirbyteSortOrder
    """Labels applied to the ad group"""
    ad_group_resource_name: AirbyteSortOrder
    """Resource name of the ad group"""
    ad_group_target_cpa_micros: AirbyteSortOrder
    """Target CPA in micros"""
    ad_group_target_roas: AirbyteSortOrder
    """Target ROAS"""
    ad_group_tracking_url_template: AirbyteSortOrder
    """Tracking URL template"""
    metrics_cost_micros: AirbyteSortOrder
    """Cost in micros"""
    segments_date: AirbyteSortOrder
    """Date segment for the report row"""


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


# ===== AD_GROUP_ADS SEARCH TYPES =====

class AdGroupAdsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_group_ads search queries."""
    ad_group_id: int | None
    """Parent ad group ID"""
    ad_group_ad_ad_id: int | None
    """Ad ID"""
    ad_group_ad_ad_name: str | None
    """Ad name"""
    ad_group_ad_ad_type: str | None
    """Ad type"""
    ad_group_ad_status: str | None
    """Ad group ad status (ENABLED, PAUSED, REMOVED)"""
    ad_group_ad_ad_strength: str | None
    """Ad strength rating"""
    ad_group_ad_ad_display_url: str | None
    """Display URL of the ad"""
    ad_group_ad_ad_final_urls: list[Any] | None
    """Final URLs for the ad"""
    ad_group_ad_ad_final_mobile_urls: list[Any] | None
    """Final mobile URLs for the ad"""
    ad_group_ad_ad_final_url_suffix: str | None
    """Final URL suffix"""
    ad_group_ad_ad_tracking_url_template: str | None
    """Tracking URL template"""
    ad_group_ad_ad_resource_name: str | None
    """Resource name of the ad"""
    ad_group_ad_ad_group: str | None
    """Ad group resource name"""
    ad_group_ad_resource_name: str | None
    """Resource name of the ad group ad"""
    ad_group_ad_labels: list[Any] | None
    """Labels applied to the ad group ad"""
    ad_group_ad_policy_summary_approval_status: str | None
    """Policy approval status"""
    ad_group_ad_policy_summary_review_status: str | None
    """Policy review status"""
    segments_date: str | None
    """Date segment for the report row"""


class AdGroupAdsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_group_id: list[int]
    """Parent ad group ID"""
    ad_group_ad_ad_id: list[int]
    """Ad ID"""
    ad_group_ad_ad_name: list[str]
    """Ad name"""
    ad_group_ad_ad_type: list[str]
    """Ad type"""
    ad_group_ad_status: list[str]
    """Ad group ad status (ENABLED, PAUSED, REMOVED)"""
    ad_group_ad_ad_strength: list[str]
    """Ad strength rating"""
    ad_group_ad_ad_display_url: list[str]
    """Display URL of the ad"""
    ad_group_ad_ad_final_urls: list[list[Any]]
    """Final URLs for the ad"""
    ad_group_ad_ad_final_mobile_urls: list[list[Any]]
    """Final mobile URLs for the ad"""
    ad_group_ad_ad_final_url_suffix: list[str]
    """Final URL suffix"""
    ad_group_ad_ad_tracking_url_template: list[str]
    """Tracking URL template"""
    ad_group_ad_ad_resource_name: list[str]
    """Resource name of the ad"""
    ad_group_ad_ad_group: list[str]
    """Ad group resource name"""
    ad_group_ad_resource_name: list[str]
    """Resource name of the ad group ad"""
    ad_group_ad_labels: list[list[Any]]
    """Labels applied to the ad group ad"""
    ad_group_ad_policy_summary_approval_status: list[str]
    """Policy approval status"""
    ad_group_ad_policy_summary_review_status: list[str]
    """Policy review status"""
    segments_date: list[str]
    """Date segment for the report row"""


class AdGroupAdsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_group_id: Any
    """Parent ad group ID"""
    ad_group_ad_ad_id: Any
    """Ad ID"""
    ad_group_ad_ad_name: Any
    """Ad name"""
    ad_group_ad_ad_type: Any
    """Ad type"""
    ad_group_ad_status: Any
    """Ad group ad status (ENABLED, PAUSED, REMOVED)"""
    ad_group_ad_ad_strength: Any
    """Ad strength rating"""
    ad_group_ad_ad_display_url: Any
    """Display URL of the ad"""
    ad_group_ad_ad_final_urls: Any
    """Final URLs for the ad"""
    ad_group_ad_ad_final_mobile_urls: Any
    """Final mobile URLs for the ad"""
    ad_group_ad_ad_final_url_suffix: Any
    """Final URL suffix"""
    ad_group_ad_ad_tracking_url_template: Any
    """Tracking URL template"""
    ad_group_ad_ad_resource_name: Any
    """Resource name of the ad"""
    ad_group_ad_ad_group: Any
    """Ad group resource name"""
    ad_group_ad_resource_name: Any
    """Resource name of the ad group ad"""
    ad_group_ad_labels: Any
    """Labels applied to the ad group ad"""
    ad_group_ad_policy_summary_approval_status: Any
    """Policy approval status"""
    ad_group_ad_policy_summary_review_status: Any
    """Policy review status"""
    segments_date: Any
    """Date segment for the report row"""


class AdGroupAdsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_group_id: str
    """Parent ad group ID"""
    ad_group_ad_ad_id: str
    """Ad ID"""
    ad_group_ad_ad_name: str
    """Ad name"""
    ad_group_ad_ad_type: str
    """Ad type"""
    ad_group_ad_status: str
    """Ad group ad status (ENABLED, PAUSED, REMOVED)"""
    ad_group_ad_ad_strength: str
    """Ad strength rating"""
    ad_group_ad_ad_display_url: str
    """Display URL of the ad"""
    ad_group_ad_ad_final_urls: str
    """Final URLs for the ad"""
    ad_group_ad_ad_final_mobile_urls: str
    """Final mobile URLs for the ad"""
    ad_group_ad_ad_final_url_suffix: str
    """Final URL suffix"""
    ad_group_ad_ad_tracking_url_template: str
    """Tracking URL template"""
    ad_group_ad_ad_resource_name: str
    """Resource name of the ad"""
    ad_group_ad_ad_group: str
    """Ad group resource name"""
    ad_group_ad_resource_name: str
    """Resource name of the ad group ad"""
    ad_group_ad_labels: str
    """Labels applied to the ad group ad"""
    ad_group_ad_policy_summary_approval_status: str
    """Policy approval status"""
    ad_group_ad_policy_summary_review_status: str
    """Policy review status"""
    segments_date: str
    """Date segment for the report row"""


class AdGroupAdsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_group_ads search results."""
    ad_group_id: AirbyteSortOrder
    """Parent ad group ID"""
    ad_group_ad_ad_id: AirbyteSortOrder
    """Ad ID"""
    ad_group_ad_ad_name: AirbyteSortOrder
    """Ad name"""
    ad_group_ad_ad_type: AirbyteSortOrder
    """Ad type"""
    ad_group_ad_status: AirbyteSortOrder
    """Ad group ad status (ENABLED, PAUSED, REMOVED)"""
    ad_group_ad_ad_strength: AirbyteSortOrder
    """Ad strength rating"""
    ad_group_ad_ad_display_url: AirbyteSortOrder
    """Display URL of the ad"""
    ad_group_ad_ad_final_urls: AirbyteSortOrder
    """Final URLs for the ad"""
    ad_group_ad_ad_final_mobile_urls: AirbyteSortOrder
    """Final mobile URLs for the ad"""
    ad_group_ad_ad_final_url_suffix: AirbyteSortOrder
    """Final URL suffix"""
    ad_group_ad_ad_tracking_url_template: AirbyteSortOrder
    """Tracking URL template"""
    ad_group_ad_ad_resource_name: AirbyteSortOrder
    """Resource name of the ad"""
    ad_group_ad_ad_group: AirbyteSortOrder
    """Ad group resource name"""
    ad_group_ad_resource_name: AirbyteSortOrder
    """Resource name of the ad group ad"""
    ad_group_ad_labels: AirbyteSortOrder
    """Labels applied to the ad group ad"""
    ad_group_ad_policy_summary_approval_status: AirbyteSortOrder
    """Policy approval status"""
    ad_group_ad_policy_summary_review_status: AirbyteSortOrder
    """Policy review status"""
    segments_date: AirbyteSortOrder
    """Date segment for the report row"""


# Entity-specific condition types for ad_group_ads
class AdGroupAdsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdGroupAdsSearchFilter


class AdGroupAdsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdGroupAdsSearchFilter


class AdGroupAdsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdGroupAdsSearchFilter


class AdGroupAdsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdGroupAdsSearchFilter


class AdGroupAdsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdGroupAdsSearchFilter


class AdGroupAdsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdGroupAdsSearchFilter


class AdGroupAdsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdGroupAdsStringFilter


class AdGroupAdsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdGroupAdsStringFilter


class AdGroupAdsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdGroupAdsStringFilter


class AdGroupAdsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdGroupAdsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdGroupAdsInCondition = TypedDict("AdGroupAdsInCondition", {"in": AdGroupAdsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdGroupAdsNotCondition = TypedDict("AdGroupAdsNotCondition", {"not": "AdGroupAdsCondition"}, total=False)
"""Negates the nested condition."""

AdGroupAdsAndCondition = TypedDict("AdGroupAdsAndCondition", {"and": "list[AdGroupAdsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdGroupAdsOrCondition = TypedDict("AdGroupAdsOrCondition", {"or": "list[AdGroupAdsCondition]"}, total=False)
"""True if any nested condition is true."""

AdGroupAdsAnyCondition = TypedDict("AdGroupAdsAnyCondition", {"any": AdGroupAdsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_group_ads condition types
AdGroupAdsCondition = (
    AdGroupAdsEqCondition
    | AdGroupAdsNeqCondition
    | AdGroupAdsGtCondition
    | AdGroupAdsGteCondition
    | AdGroupAdsLtCondition
    | AdGroupAdsLteCondition
    | AdGroupAdsInCondition
    | AdGroupAdsLikeCondition
    | AdGroupAdsFuzzyCondition
    | AdGroupAdsKeywordCondition
    | AdGroupAdsContainsCondition
    | AdGroupAdsNotCondition
    | AdGroupAdsAndCondition
    | AdGroupAdsOrCondition
    | AdGroupAdsAnyCondition
)


class AdGroupAdsSearchQuery(TypedDict, total=False):
    """Search query for ad_group_ads entity."""
    filter: AdGroupAdsCondition
    sort: list[AdGroupAdsSortFilter]


# ===== CAMPAIGN_LABELS SEARCH TYPES =====

class CampaignLabelsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaign_labels search queries."""
    campaign_id: int | None
    """Campaign ID"""
    campaign_label_campaign: str | None
    """Campaign resource name"""
    campaign_label_label: str | None
    """Label resource name"""
    campaign_label_resource_name: str | None
    """Resource name of the campaign label"""
    label_id: int | None
    """Label ID"""
    label_name: str | None
    """Label name"""
    label_resource_name: str | None
    """Resource name of the label"""


class CampaignLabelsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    campaign_id: list[int]
    """Campaign ID"""
    campaign_label_campaign: list[str]
    """Campaign resource name"""
    campaign_label_label: list[str]
    """Label resource name"""
    campaign_label_resource_name: list[str]
    """Resource name of the campaign label"""
    label_id: list[int]
    """Label ID"""
    label_name: list[str]
    """Label name"""
    label_resource_name: list[str]
    """Resource name of the label"""


class CampaignLabelsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    campaign_id: Any
    """Campaign ID"""
    campaign_label_campaign: Any
    """Campaign resource name"""
    campaign_label_label: Any
    """Label resource name"""
    campaign_label_resource_name: Any
    """Resource name of the campaign label"""
    label_id: Any
    """Label ID"""
    label_name: Any
    """Label name"""
    label_resource_name: Any
    """Resource name of the label"""


class CampaignLabelsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    campaign_id: str
    """Campaign ID"""
    campaign_label_campaign: str
    """Campaign resource name"""
    campaign_label_label: str
    """Label resource name"""
    campaign_label_resource_name: str
    """Resource name of the campaign label"""
    label_id: str
    """Label ID"""
    label_name: str
    """Label name"""
    label_resource_name: str
    """Resource name of the label"""


class CampaignLabelsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaign_labels search results."""
    campaign_id: AirbyteSortOrder
    """Campaign ID"""
    campaign_label_campaign: AirbyteSortOrder
    """Campaign resource name"""
    campaign_label_label: AirbyteSortOrder
    """Label resource name"""
    campaign_label_resource_name: AirbyteSortOrder
    """Resource name of the campaign label"""
    label_id: AirbyteSortOrder
    """Label ID"""
    label_name: AirbyteSortOrder
    """Label name"""
    label_resource_name: AirbyteSortOrder
    """Resource name of the label"""


# Entity-specific condition types for campaign_labels
class CampaignLabelsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CampaignLabelsSearchFilter


class CampaignLabelsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CampaignLabelsSearchFilter


class CampaignLabelsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CampaignLabelsSearchFilter


class CampaignLabelsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CampaignLabelsSearchFilter


class CampaignLabelsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CampaignLabelsSearchFilter


class CampaignLabelsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CampaignLabelsSearchFilter


class CampaignLabelsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CampaignLabelsStringFilter


class CampaignLabelsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CampaignLabelsStringFilter


class CampaignLabelsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CampaignLabelsStringFilter


class CampaignLabelsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CampaignLabelsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CampaignLabelsInCondition = TypedDict("CampaignLabelsInCondition", {"in": CampaignLabelsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CampaignLabelsNotCondition = TypedDict("CampaignLabelsNotCondition", {"not": "CampaignLabelsCondition"}, total=False)
"""Negates the nested condition."""

CampaignLabelsAndCondition = TypedDict("CampaignLabelsAndCondition", {"and": "list[CampaignLabelsCondition]"}, total=False)
"""True if all nested conditions are true."""

CampaignLabelsOrCondition = TypedDict("CampaignLabelsOrCondition", {"or": "list[CampaignLabelsCondition]"}, total=False)
"""True if any nested condition is true."""

CampaignLabelsAnyCondition = TypedDict("CampaignLabelsAnyCondition", {"any": CampaignLabelsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all campaign_labels condition types
CampaignLabelsCondition = (
    CampaignLabelsEqCondition
    | CampaignLabelsNeqCondition
    | CampaignLabelsGtCondition
    | CampaignLabelsGteCondition
    | CampaignLabelsLtCondition
    | CampaignLabelsLteCondition
    | CampaignLabelsInCondition
    | CampaignLabelsLikeCondition
    | CampaignLabelsFuzzyCondition
    | CampaignLabelsKeywordCondition
    | CampaignLabelsContainsCondition
    | CampaignLabelsNotCondition
    | CampaignLabelsAndCondition
    | CampaignLabelsOrCondition
    | CampaignLabelsAnyCondition
)


class CampaignLabelsSearchQuery(TypedDict, total=False):
    """Search query for campaign_labels entity."""
    filter: CampaignLabelsCondition
    sort: list[CampaignLabelsSortFilter]


# ===== AD_GROUP_LABELS SEARCH TYPES =====

class AdGroupLabelsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_group_labels search queries."""
    ad_group_id: int | None
    """Ad group ID"""
    ad_group_label_ad_group: str | None
    """Ad group resource name"""
    ad_group_label_label: str | None
    """Label resource name"""
    ad_group_label_resource_name: str | None
    """Resource name of the ad group label"""
    label_id: int | None
    """Label ID"""
    label_name: str | None
    """Label name"""
    label_resource_name: str | None
    """Resource name of the label"""


class AdGroupLabelsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_group_id: list[int]
    """Ad group ID"""
    ad_group_label_ad_group: list[str]
    """Ad group resource name"""
    ad_group_label_label: list[str]
    """Label resource name"""
    ad_group_label_resource_name: list[str]
    """Resource name of the ad group label"""
    label_id: list[int]
    """Label ID"""
    label_name: list[str]
    """Label name"""
    label_resource_name: list[str]
    """Resource name of the label"""


class AdGroupLabelsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_group_id: Any
    """Ad group ID"""
    ad_group_label_ad_group: Any
    """Ad group resource name"""
    ad_group_label_label: Any
    """Label resource name"""
    ad_group_label_resource_name: Any
    """Resource name of the ad group label"""
    label_id: Any
    """Label ID"""
    label_name: Any
    """Label name"""
    label_resource_name: Any
    """Resource name of the label"""


class AdGroupLabelsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_group_id: str
    """Ad group ID"""
    ad_group_label_ad_group: str
    """Ad group resource name"""
    ad_group_label_label: str
    """Label resource name"""
    ad_group_label_resource_name: str
    """Resource name of the ad group label"""
    label_id: str
    """Label ID"""
    label_name: str
    """Label name"""
    label_resource_name: str
    """Resource name of the label"""


class AdGroupLabelsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_group_labels search results."""
    ad_group_id: AirbyteSortOrder
    """Ad group ID"""
    ad_group_label_ad_group: AirbyteSortOrder
    """Ad group resource name"""
    ad_group_label_label: AirbyteSortOrder
    """Label resource name"""
    ad_group_label_resource_name: AirbyteSortOrder
    """Resource name of the ad group label"""
    label_id: AirbyteSortOrder
    """Label ID"""
    label_name: AirbyteSortOrder
    """Label name"""
    label_resource_name: AirbyteSortOrder
    """Resource name of the label"""


# Entity-specific condition types for ad_group_labels
class AdGroupLabelsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdGroupLabelsSearchFilter


class AdGroupLabelsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdGroupLabelsSearchFilter


class AdGroupLabelsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdGroupLabelsSearchFilter


class AdGroupLabelsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdGroupLabelsSearchFilter


class AdGroupLabelsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdGroupLabelsSearchFilter


class AdGroupLabelsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdGroupLabelsSearchFilter


class AdGroupLabelsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdGroupLabelsStringFilter


class AdGroupLabelsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdGroupLabelsStringFilter


class AdGroupLabelsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdGroupLabelsStringFilter


class AdGroupLabelsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdGroupLabelsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdGroupLabelsInCondition = TypedDict("AdGroupLabelsInCondition", {"in": AdGroupLabelsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdGroupLabelsNotCondition = TypedDict("AdGroupLabelsNotCondition", {"not": "AdGroupLabelsCondition"}, total=False)
"""Negates the nested condition."""

AdGroupLabelsAndCondition = TypedDict("AdGroupLabelsAndCondition", {"and": "list[AdGroupLabelsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdGroupLabelsOrCondition = TypedDict("AdGroupLabelsOrCondition", {"or": "list[AdGroupLabelsCondition]"}, total=False)
"""True if any nested condition is true."""

AdGroupLabelsAnyCondition = TypedDict("AdGroupLabelsAnyCondition", {"any": AdGroupLabelsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_group_labels condition types
AdGroupLabelsCondition = (
    AdGroupLabelsEqCondition
    | AdGroupLabelsNeqCondition
    | AdGroupLabelsGtCondition
    | AdGroupLabelsGteCondition
    | AdGroupLabelsLtCondition
    | AdGroupLabelsLteCondition
    | AdGroupLabelsInCondition
    | AdGroupLabelsLikeCondition
    | AdGroupLabelsFuzzyCondition
    | AdGroupLabelsKeywordCondition
    | AdGroupLabelsContainsCondition
    | AdGroupLabelsNotCondition
    | AdGroupLabelsAndCondition
    | AdGroupLabelsOrCondition
    | AdGroupLabelsAnyCondition
)


class AdGroupLabelsSearchQuery(TypedDict, total=False):
    """Search query for ad_group_labels entity."""
    filter: AdGroupLabelsCondition
    sort: list[AdGroupLabelsSortFilter]


# ===== AD_GROUP_AD_LABELS SEARCH TYPES =====

class AdGroupAdLabelsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ad_group_ad_labels search queries."""
    ad_group_ad_ad_id: int | None
    """Ad ID"""
    ad_group_ad_label_ad_group_ad: str | None
    """Ad group ad resource name"""
    ad_group_ad_label_label: str | None
    """Label resource name"""
    ad_group_ad_label_resource_name: str | None
    """Resource name of the ad group ad label"""
    label_id: int | None
    """Label ID"""
    label_name: str | None
    """Label name"""
    label_resource_name: str | None
    """Resource name of the label"""


class AdGroupAdLabelsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_group_ad_ad_id: list[int]
    """Ad ID"""
    ad_group_ad_label_ad_group_ad: list[str]
    """Ad group ad resource name"""
    ad_group_ad_label_label: list[str]
    """Label resource name"""
    ad_group_ad_label_resource_name: list[str]
    """Resource name of the ad group ad label"""
    label_id: list[int]
    """Label ID"""
    label_name: list[str]
    """Label name"""
    label_resource_name: list[str]
    """Resource name of the label"""


class AdGroupAdLabelsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_group_ad_ad_id: Any
    """Ad ID"""
    ad_group_ad_label_ad_group_ad: Any
    """Ad group ad resource name"""
    ad_group_ad_label_label: Any
    """Label resource name"""
    ad_group_ad_label_resource_name: Any
    """Resource name of the ad group ad label"""
    label_id: Any
    """Label ID"""
    label_name: Any
    """Label name"""
    label_resource_name: Any
    """Resource name of the label"""


class AdGroupAdLabelsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_group_ad_ad_id: str
    """Ad ID"""
    ad_group_ad_label_ad_group_ad: str
    """Ad group ad resource name"""
    ad_group_ad_label_label: str
    """Label resource name"""
    ad_group_ad_label_resource_name: str
    """Resource name of the ad group ad label"""
    label_id: str
    """Label ID"""
    label_name: str
    """Label name"""
    label_resource_name: str
    """Resource name of the label"""


class AdGroupAdLabelsSortFilter(TypedDict, total=False):
    """Available fields for sorting ad_group_ad_labels search results."""
    ad_group_ad_ad_id: AirbyteSortOrder
    """Ad ID"""
    ad_group_ad_label_ad_group_ad: AirbyteSortOrder
    """Ad group ad resource name"""
    ad_group_ad_label_label: AirbyteSortOrder
    """Label resource name"""
    ad_group_ad_label_resource_name: AirbyteSortOrder
    """Resource name of the ad group ad label"""
    label_id: AirbyteSortOrder
    """Label ID"""
    label_name: AirbyteSortOrder
    """Label name"""
    label_resource_name: AirbyteSortOrder
    """Resource name of the label"""


# Entity-specific condition types for ad_group_ad_labels
class AdGroupAdLabelsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdGroupAdLabelsSearchFilter


class AdGroupAdLabelsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdGroupAdLabelsSearchFilter


class AdGroupAdLabelsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdGroupAdLabelsSearchFilter


class AdGroupAdLabelsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdGroupAdLabelsSearchFilter


class AdGroupAdLabelsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdGroupAdLabelsSearchFilter


class AdGroupAdLabelsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdGroupAdLabelsSearchFilter


class AdGroupAdLabelsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdGroupAdLabelsStringFilter


class AdGroupAdLabelsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdGroupAdLabelsStringFilter


class AdGroupAdLabelsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdGroupAdLabelsStringFilter


class AdGroupAdLabelsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdGroupAdLabelsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdGroupAdLabelsInCondition = TypedDict("AdGroupAdLabelsInCondition", {"in": AdGroupAdLabelsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdGroupAdLabelsNotCondition = TypedDict("AdGroupAdLabelsNotCondition", {"not": "AdGroupAdLabelsCondition"}, total=False)
"""Negates the nested condition."""

AdGroupAdLabelsAndCondition = TypedDict("AdGroupAdLabelsAndCondition", {"and": "list[AdGroupAdLabelsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdGroupAdLabelsOrCondition = TypedDict("AdGroupAdLabelsOrCondition", {"or": "list[AdGroupAdLabelsCondition]"}, total=False)
"""True if any nested condition is true."""

AdGroupAdLabelsAnyCondition = TypedDict("AdGroupAdLabelsAnyCondition", {"any": AdGroupAdLabelsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ad_group_ad_labels condition types
AdGroupAdLabelsCondition = (
    AdGroupAdLabelsEqCondition
    | AdGroupAdLabelsNeqCondition
    | AdGroupAdLabelsGtCondition
    | AdGroupAdLabelsGteCondition
    | AdGroupAdLabelsLtCondition
    | AdGroupAdLabelsLteCondition
    | AdGroupAdLabelsInCondition
    | AdGroupAdLabelsLikeCondition
    | AdGroupAdLabelsFuzzyCondition
    | AdGroupAdLabelsKeywordCondition
    | AdGroupAdLabelsContainsCondition
    | AdGroupAdLabelsNotCondition
    | AdGroupAdLabelsAndCondition
    | AdGroupAdLabelsOrCondition
    | AdGroupAdLabelsAnyCondition
)


class AdGroupAdLabelsSearchQuery(TypedDict, total=False):
    """Search query for ad_group_ad_labels entity."""
    filter: AdGroupAdLabelsCondition
    sort: list[AdGroupAdLabelsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
