"""
Type definitions for intercom connector.
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

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    per_page: NotRequired[int]
    starting_after: NotRequired[str]

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    id: str

class ConversationsListParams(TypedDict):
    """Parameters for conversations.list operation"""
    per_page: NotRequired[int]
    starting_after: NotRequired[str]

class ConversationsGetParams(TypedDict):
    """Parameters for conversations.get operation"""
    id: str

class CompaniesListParams(TypedDict):
    """Parameters for companies.list operation"""
    per_page: NotRequired[int]
    starting_after: NotRequired[str]

class CompaniesGetParams(TypedDict):
    """Parameters for companies.get operation"""
    id: str

class TeamsListParams(TypedDict):
    """Parameters for teams.list operation"""
    pass

class TeamsGetParams(TypedDict):
    """Parameters for teams.get operation"""
    id: str

class AdminsListParams(TypedDict):
    """Parameters for admins.list operation"""
    pass

class AdminsGetParams(TypedDict):
    """Parameters for admins.get operation"""
    id: str

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    pass

class TagsGetParams(TypedDict):
    """Parameters for tags.get operation"""
    id: str

class SegmentsListParams(TypedDict):
    """Parameters for segments.list operation"""
    include_count: NotRequired[bool]

class SegmentsGetParams(TypedDict):
    """Parameters for segments.get operation"""
    id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== COMPANIES SEARCH TYPES =====

class CompaniesSearchFilter(TypedDict, total=False):
    """Available fields for filtering companies search queries."""
    app_id: str | None
    """The ID of the application associated with the company"""
    company_id: str | None
    """The unique identifier of the company"""
    created_at: int | None
    """The date and time when the company was created"""
    custom_attributes: dict[str, Any] | None
    """Custom attributes specific to the company"""
    id: str | None
    """The ID of the company"""
    industry: str | None
    """The industry in which the company operates"""
    monthly_spend: float | None
    """The monthly spend of the company"""
    name: str | None
    """The name of the company"""
    plan: dict[str, Any] | None
    """Details of the company's subscription plan"""
    remote_created_at: int | None
    """The remote date and time when the company was created"""
    segments: dict[str, Any] | None
    """Segments associated with the company"""
    session_count: int | None
    """The number of sessions related to the company"""
    size: int | None
    """The size of the company"""
    tags: dict[str, Any] | None
    """Tags associated with the company"""
    type: str | None
    """The type of the company"""
    updated_at: int | None
    """The date and time when the company was last updated"""
    user_count: int | None
    """The number of users associated with the company"""
    website: str | None
    """The website of the company"""


class CompaniesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    app_id: list[str]
    """The ID of the application associated with the company"""
    company_id: list[str]
    """The unique identifier of the company"""
    created_at: list[int]
    """The date and time when the company was created"""
    custom_attributes: list[dict[str, Any]]
    """Custom attributes specific to the company"""
    id: list[str]
    """The ID of the company"""
    industry: list[str]
    """The industry in which the company operates"""
    monthly_spend: list[float]
    """The monthly spend of the company"""
    name: list[str]
    """The name of the company"""
    plan: list[dict[str, Any]]
    """Details of the company's subscription plan"""
    remote_created_at: list[int]
    """The remote date and time when the company was created"""
    segments: list[dict[str, Any]]
    """Segments associated with the company"""
    session_count: list[int]
    """The number of sessions related to the company"""
    size: list[int]
    """The size of the company"""
    tags: list[dict[str, Any]]
    """Tags associated with the company"""
    type: list[str]
    """The type of the company"""
    updated_at: list[int]
    """The date and time when the company was last updated"""
    user_count: list[int]
    """The number of users associated with the company"""
    website: list[str]
    """The website of the company"""


class CompaniesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    app_id: Any
    """The ID of the application associated with the company"""
    company_id: Any
    """The unique identifier of the company"""
    created_at: Any
    """The date and time when the company was created"""
    custom_attributes: Any
    """Custom attributes specific to the company"""
    id: Any
    """The ID of the company"""
    industry: Any
    """The industry in which the company operates"""
    monthly_spend: Any
    """The monthly spend of the company"""
    name: Any
    """The name of the company"""
    plan: Any
    """Details of the company's subscription plan"""
    remote_created_at: Any
    """The remote date and time when the company was created"""
    segments: Any
    """Segments associated with the company"""
    session_count: Any
    """The number of sessions related to the company"""
    size: Any
    """The size of the company"""
    tags: Any
    """Tags associated with the company"""
    type: Any
    """The type of the company"""
    updated_at: Any
    """The date and time when the company was last updated"""
    user_count: Any
    """The number of users associated with the company"""
    website: Any
    """The website of the company"""


class CompaniesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    app_id: str
    """The ID of the application associated with the company"""
    company_id: str
    """The unique identifier of the company"""
    created_at: str
    """The date and time when the company was created"""
    custom_attributes: str
    """Custom attributes specific to the company"""
    id: str
    """The ID of the company"""
    industry: str
    """The industry in which the company operates"""
    monthly_spend: str
    """The monthly spend of the company"""
    name: str
    """The name of the company"""
    plan: str
    """Details of the company's subscription plan"""
    remote_created_at: str
    """The remote date and time when the company was created"""
    segments: str
    """Segments associated with the company"""
    session_count: str
    """The number of sessions related to the company"""
    size: str
    """The size of the company"""
    tags: str
    """Tags associated with the company"""
    type: str
    """The type of the company"""
    updated_at: str
    """The date and time when the company was last updated"""
    user_count: str
    """The number of users associated with the company"""
    website: str
    """The website of the company"""


class CompaniesSortFilter(TypedDict, total=False):
    """Available fields for sorting companies search results."""
    app_id: AirbyteSortOrder
    """The ID of the application associated with the company"""
    company_id: AirbyteSortOrder
    """The unique identifier of the company"""
    created_at: AirbyteSortOrder
    """The date and time when the company was created"""
    custom_attributes: AirbyteSortOrder
    """Custom attributes specific to the company"""
    id: AirbyteSortOrder
    """The ID of the company"""
    industry: AirbyteSortOrder
    """The industry in which the company operates"""
    monthly_spend: AirbyteSortOrder
    """The monthly spend of the company"""
    name: AirbyteSortOrder
    """The name of the company"""
    plan: AirbyteSortOrder
    """Details of the company's subscription plan"""
    remote_created_at: AirbyteSortOrder
    """The remote date and time when the company was created"""
    segments: AirbyteSortOrder
    """Segments associated with the company"""
    session_count: AirbyteSortOrder
    """The number of sessions related to the company"""
    size: AirbyteSortOrder
    """The size of the company"""
    tags: AirbyteSortOrder
    """Tags associated with the company"""
    type: AirbyteSortOrder
    """The type of the company"""
    updated_at: AirbyteSortOrder
    """The date and time when the company was last updated"""
    user_count: AirbyteSortOrder
    """The number of users associated with the company"""
    website: AirbyteSortOrder
    """The website of the company"""


# Entity-specific condition types for companies
class CompaniesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CompaniesSearchFilter


class CompaniesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CompaniesSearchFilter


class CompaniesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CompaniesSearchFilter


class CompaniesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CompaniesSearchFilter


class CompaniesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CompaniesSearchFilter


class CompaniesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CompaniesSearchFilter


class CompaniesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CompaniesStringFilter


class CompaniesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CompaniesStringFilter


class CompaniesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CompaniesStringFilter


class CompaniesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CompaniesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CompaniesInCondition = TypedDict("CompaniesInCondition", {"in": CompaniesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CompaniesNotCondition = TypedDict("CompaniesNotCondition", {"not": "CompaniesCondition"}, total=False)
"""Negates the nested condition."""

CompaniesAndCondition = TypedDict("CompaniesAndCondition", {"and": "list[CompaniesCondition]"}, total=False)
"""True if all nested conditions are true."""

CompaniesOrCondition = TypedDict("CompaniesOrCondition", {"or": "list[CompaniesCondition]"}, total=False)
"""True if any nested condition is true."""

CompaniesAnyCondition = TypedDict("CompaniesAnyCondition", {"any": CompaniesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all companies condition types
CompaniesCondition = (
    CompaniesEqCondition
    | CompaniesNeqCondition
    | CompaniesGtCondition
    | CompaniesGteCondition
    | CompaniesLtCondition
    | CompaniesLteCondition
    | CompaniesInCondition
    | CompaniesLikeCondition
    | CompaniesFuzzyCondition
    | CompaniesKeywordCondition
    | CompaniesContainsCondition
    | CompaniesNotCondition
    | CompaniesAndCondition
    | CompaniesOrCondition
    | CompaniesAnyCondition
)


class CompaniesSearchQuery(TypedDict, total=False):
    """Search query for companies entity."""
    filter: CompaniesCondition
    sort: list[CompaniesSortFilter]


# ===== CONTACTS SEARCH TYPES =====

class ContactsSearchFilter(TypedDict, total=False):
    """Available fields for filtering contacts search queries."""
    android_app_name: str | None
    """The name of the Android app associated with the contact."""
    android_app_version: str | None
    """The version of the Android app associated with the contact."""
    android_device: str | None
    """The device used by the contact for Android."""
    android_last_seen_at: str | None
    """The date and time when the contact was last seen on Android."""
    android_os_version: str | None
    """The operating system version of the Android device."""
    android_sdk_version: str | None
    """The SDK version of the Android device."""
    avatar: str | None
    """URL pointing to the contact's avatar image."""
    browser: str | None
    """The browser used by the contact."""
    browser_language: str | None
    """The language preference set in the contact's browser."""
    browser_version: str | None
    """The version of the browser used by the contact."""
    companies: dict[str, Any] | None
    """Companies associated with the contact."""
    created_at: int | None
    """The date and time when the contact was created."""
    custom_attributes: dict[str, Any] | None
    """Custom attributes defined for the contact."""
    email: str | None
    """The email address of the contact."""
    external_id: str | None
    """External identifier for the contact."""
    has_hard_bounced: bool | None
    """Flag indicating if the contact has hard bounced."""
    id: str | None
    """The unique identifier of the contact."""
    ios_app_name: str | None
    """The name of the iOS app associated with the contact."""
    ios_app_version: str | None
    """The version of the iOS app associated with the contact."""
    ios_device: str | None
    """The device used by the contact for iOS."""
    ios_last_seen_at: int | None
    """The date and time when the contact was last seen on iOS."""
    ios_os_version: str | None
    """The operating system version of the iOS device."""
    ios_sdk_version: str | None
    """The SDK version of the iOS device."""
    language_override: str | None
    """Language override set for the contact."""
    last_contacted_at: int | None
    """The date and time when the contact was last contacted."""
    last_email_clicked_at: int | None
    """The date and time when the contact last clicked an email."""
    last_email_opened_at: int | None
    """The date and time when the contact last opened an email."""
    last_replied_at: int | None
    """The date and time when the contact last replied."""
    last_seen_at: int | None
    """The date and time when the contact was last seen overall."""
    location: dict[str, Any] | None
    """Location details of the contact."""
    marked_email_as_spam: bool | None
    """Flag indicating if the contact's email was marked as spam."""
    name: str | None
    """The name of the contact."""
    notes: dict[str, Any] | None
    """Notes associated with the contact."""
    opted_in_subscription_types: dict[str, Any] | None
    """Subscription types the contact opted into."""
    opted_out_subscription_types: dict[str, Any] | None
    """Subscription types the contact opted out from."""
    os: str | None
    """Operating system of the contact's device."""
    owner_id: int | None
    """The unique identifier of the contact's owner."""
    phone: str | None
    """The phone number of the contact."""
    referrer: str | None
    """Referrer information related to the contact."""
    role: str | None
    """Role or position of the contact."""
    signed_up_at: int | None
    """The date and time when the contact signed up."""
    sms_consent: bool | None
    """Consent status for SMS communication."""
    social_profiles: dict[str, Any] | None
    """Social profiles associated with the contact."""
    tags: dict[str, Any] | None
    """Tags associated with the contact."""
    type: str | None
    """Type of contact."""
    unsubscribed_from_emails: bool | None
    """Flag indicating if the contact unsubscribed from emails."""
    unsubscribed_from_sms: bool | None
    """Flag indicating if the contact unsubscribed from SMS."""
    updated_at: int | None
    """The date and time when the contact was last updated."""
    utm_campaign: str | None
    """Campaign data from UTM parameters."""
    utm_content: str | None
    """Content data from UTM parameters."""
    utm_medium: str | None
    """Medium data from UTM parameters."""
    utm_source: str | None
    """Source data from UTM parameters."""
    utm_term: str | None
    """Term data from UTM parameters."""
    workspace_id: str | None
    """The unique identifier of the workspace associated with the contact."""


class ContactsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    android_app_name: list[str]
    """The name of the Android app associated with the contact."""
    android_app_version: list[str]
    """The version of the Android app associated with the contact."""
    android_device: list[str]
    """The device used by the contact for Android."""
    android_last_seen_at: list[str]
    """The date and time when the contact was last seen on Android."""
    android_os_version: list[str]
    """The operating system version of the Android device."""
    android_sdk_version: list[str]
    """The SDK version of the Android device."""
    avatar: list[str]
    """URL pointing to the contact's avatar image."""
    browser: list[str]
    """The browser used by the contact."""
    browser_language: list[str]
    """The language preference set in the contact's browser."""
    browser_version: list[str]
    """The version of the browser used by the contact."""
    companies: list[dict[str, Any]]
    """Companies associated with the contact."""
    created_at: list[int]
    """The date and time when the contact was created."""
    custom_attributes: list[dict[str, Any]]
    """Custom attributes defined for the contact."""
    email: list[str]
    """The email address of the contact."""
    external_id: list[str]
    """External identifier for the contact."""
    has_hard_bounced: list[bool]
    """Flag indicating if the contact has hard bounced."""
    id: list[str]
    """The unique identifier of the contact."""
    ios_app_name: list[str]
    """The name of the iOS app associated with the contact."""
    ios_app_version: list[str]
    """The version of the iOS app associated with the contact."""
    ios_device: list[str]
    """The device used by the contact for iOS."""
    ios_last_seen_at: list[int]
    """The date and time when the contact was last seen on iOS."""
    ios_os_version: list[str]
    """The operating system version of the iOS device."""
    ios_sdk_version: list[str]
    """The SDK version of the iOS device."""
    language_override: list[str]
    """Language override set for the contact."""
    last_contacted_at: list[int]
    """The date and time when the contact was last contacted."""
    last_email_clicked_at: list[int]
    """The date and time when the contact last clicked an email."""
    last_email_opened_at: list[int]
    """The date and time when the contact last opened an email."""
    last_replied_at: list[int]
    """The date and time when the contact last replied."""
    last_seen_at: list[int]
    """The date and time when the contact was last seen overall."""
    location: list[dict[str, Any]]
    """Location details of the contact."""
    marked_email_as_spam: list[bool]
    """Flag indicating if the contact's email was marked as spam."""
    name: list[str]
    """The name of the contact."""
    notes: list[dict[str, Any]]
    """Notes associated with the contact."""
    opted_in_subscription_types: list[dict[str, Any]]
    """Subscription types the contact opted into."""
    opted_out_subscription_types: list[dict[str, Any]]
    """Subscription types the contact opted out from."""
    os: list[str]
    """Operating system of the contact's device."""
    owner_id: list[int]
    """The unique identifier of the contact's owner."""
    phone: list[str]
    """The phone number of the contact."""
    referrer: list[str]
    """Referrer information related to the contact."""
    role: list[str]
    """Role or position of the contact."""
    signed_up_at: list[int]
    """The date and time when the contact signed up."""
    sms_consent: list[bool]
    """Consent status for SMS communication."""
    social_profiles: list[dict[str, Any]]
    """Social profiles associated with the contact."""
    tags: list[dict[str, Any]]
    """Tags associated with the contact."""
    type: list[str]
    """Type of contact."""
    unsubscribed_from_emails: list[bool]
    """Flag indicating if the contact unsubscribed from emails."""
    unsubscribed_from_sms: list[bool]
    """Flag indicating if the contact unsubscribed from SMS."""
    updated_at: list[int]
    """The date and time when the contact was last updated."""
    utm_campaign: list[str]
    """Campaign data from UTM parameters."""
    utm_content: list[str]
    """Content data from UTM parameters."""
    utm_medium: list[str]
    """Medium data from UTM parameters."""
    utm_source: list[str]
    """Source data from UTM parameters."""
    utm_term: list[str]
    """Term data from UTM parameters."""
    workspace_id: list[str]
    """The unique identifier of the workspace associated with the contact."""


class ContactsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    android_app_name: Any
    """The name of the Android app associated with the contact."""
    android_app_version: Any
    """The version of the Android app associated with the contact."""
    android_device: Any
    """The device used by the contact for Android."""
    android_last_seen_at: Any
    """The date and time when the contact was last seen on Android."""
    android_os_version: Any
    """The operating system version of the Android device."""
    android_sdk_version: Any
    """The SDK version of the Android device."""
    avatar: Any
    """URL pointing to the contact's avatar image."""
    browser: Any
    """The browser used by the contact."""
    browser_language: Any
    """The language preference set in the contact's browser."""
    browser_version: Any
    """The version of the browser used by the contact."""
    companies: Any
    """Companies associated with the contact."""
    created_at: Any
    """The date and time when the contact was created."""
    custom_attributes: Any
    """Custom attributes defined for the contact."""
    email: Any
    """The email address of the contact."""
    external_id: Any
    """External identifier for the contact."""
    has_hard_bounced: Any
    """Flag indicating if the contact has hard bounced."""
    id: Any
    """The unique identifier of the contact."""
    ios_app_name: Any
    """The name of the iOS app associated with the contact."""
    ios_app_version: Any
    """The version of the iOS app associated with the contact."""
    ios_device: Any
    """The device used by the contact for iOS."""
    ios_last_seen_at: Any
    """The date and time when the contact was last seen on iOS."""
    ios_os_version: Any
    """The operating system version of the iOS device."""
    ios_sdk_version: Any
    """The SDK version of the iOS device."""
    language_override: Any
    """Language override set for the contact."""
    last_contacted_at: Any
    """The date and time when the contact was last contacted."""
    last_email_clicked_at: Any
    """The date and time when the contact last clicked an email."""
    last_email_opened_at: Any
    """The date and time when the contact last opened an email."""
    last_replied_at: Any
    """The date and time when the contact last replied."""
    last_seen_at: Any
    """The date and time when the contact was last seen overall."""
    location: Any
    """Location details of the contact."""
    marked_email_as_spam: Any
    """Flag indicating if the contact's email was marked as spam."""
    name: Any
    """The name of the contact."""
    notes: Any
    """Notes associated with the contact."""
    opted_in_subscription_types: Any
    """Subscription types the contact opted into."""
    opted_out_subscription_types: Any
    """Subscription types the contact opted out from."""
    os: Any
    """Operating system of the contact's device."""
    owner_id: Any
    """The unique identifier of the contact's owner."""
    phone: Any
    """The phone number of the contact."""
    referrer: Any
    """Referrer information related to the contact."""
    role: Any
    """Role or position of the contact."""
    signed_up_at: Any
    """The date and time when the contact signed up."""
    sms_consent: Any
    """Consent status for SMS communication."""
    social_profiles: Any
    """Social profiles associated with the contact."""
    tags: Any
    """Tags associated with the contact."""
    type: Any
    """Type of contact."""
    unsubscribed_from_emails: Any
    """Flag indicating if the contact unsubscribed from emails."""
    unsubscribed_from_sms: Any
    """Flag indicating if the contact unsubscribed from SMS."""
    updated_at: Any
    """The date and time when the contact was last updated."""
    utm_campaign: Any
    """Campaign data from UTM parameters."""
    utm_content: Any
    """Content data from UTM parameters."""
    utm_medium: Any
    """Medium data from UTM parameters."""
    utm_source: Any
    """Source data from UTM parameters."""
    utm_term: Any
    """Term data from UTM parameters."""
    workspace_id: Any
    """The unique identifier of the workspace associated with the contact."""


class ContactsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    android_app_name: str
    """The name of the Android app associated with the contact."""
    android_app_version: str
    """The version of the Android app associated with the contact."""
    android_device: str
    """The device used by the contact for Android."""
    android_last_seen_at: str
    """The date and time when the contact was last seen on Android."""
    android_os_version: str
    """The operating system version of the Android device."""
    android_sdk_version: str
    """The SDK version of the Android device."""
    avatar: str
    """URL pointing to the contact's avatar image."""
    browser: str
    """The browser used by the contact."""
    browser_language: str
    """The language preference set in the contact's browser."""
    browser_version: str
    """The version of the browser used by the contact."""
    companies: str
    """Companies associated with the contact."""
    created_at: str
    """The date and time when the contact was created."""
    custom_attributes: str
    """Custom attributes defined for the contact."""
    email: str
    """The email address of the contact."""
    external_id: str
    """External identifier for the contact."""
    has_hard_bounced: str
    """Flag indicating if the contact has hard bounced."""
    id: str
    """The unique identifier of the contact."""
    ios_app_name: str
    """The name of the iOS app associated with the contact."""
    ios_app_version: str
    """The version of the iOS app associated with the contact."""
    ios_device: str
    """The device used by the contact for iOS."""
    ios_last_seen_at: str
    """The date and time when the contact was last seen on iOS."""
    ios_os_version: str
    """The operating system version of the iOS device."""
    ios_sdk_version: str
    """The SDK version of the iOS device."""
    language_override: str
    """Language override set for the contact."""
    last_contacted_at: str
    """The date and time when the contact was last contacted."""
    last_email_clicked_at: str
    """The date and time when the contact last clicked an email."""
    last_email_opened_at: str
    """The date and time when the contact last opened an email."""
    last_replied_at: str
    """The date and time when the contact last replied."""
    last_seen_at: str
    """The date and time when the contact was last seen overall."""
    location: str
    """Location details of the contact."""
    marked_email_as_spam: str
    """Flag indicating if the contact's email was marked as spam."""
    name: str
    """The name of the contact."""
    notes: str
    """Notes associated with the contact."""
    opted_in_subscription_types: str
    """Subscription types the contact opted into."""
    opted_out_subscription_types: str
    """Subscription types the contact opted out from."""
    os: str
    """Operating system of the contact's device."""
    owner_id: str
    """The unique identifier of the contact's owner."""
    phone: str
    """The phone number of the contact."""
    referrer: str
    """Referrer information related to the contact."""
    role: str
    """Role or position of the contact."""
    signed_up_at: str
    """The date and time when the contact signed up."""
    sms_consent: str
    """Consent status for SMS communication."""
    social_profiles: str
    """Social profiles associated with the contact."""
    tags: str
    """Tags associated with the contact."""
    type: str
    """Type of contact."""
    unsubscribed_from_emails: str
    """Flag indicating if the contact unsubscribed from emails."""
    unsubscribed_from_sms: str
    """Flag indicating if the contact unsubscribed from SMS."""
    updated_at: str
    """The date and time when the contact was last updated."""
    utm_campaign: str
    """Campaign data from UTM parameters."""
    utm_content: str
    """Content data from UTM parameters."""
    utm_medium: str
    """Medium data from UTM parameters."""
    utm_source: str
    """Source data from UTM parameters."""
    utm_term: str
    """Term data from UTM parameters."""
    workspace_id: str
    """The unique identifier of the workspace associated with the contact."""


class ContactsSortFilter(TypedDict, total=False):
    """Available fields for sorting contacts search results."""
    android_app_name: AirbyteSortOrder
    """The name of the Android app associated with the contact."""
    android_app_version: AirbyteSortOrder
    """The version of the Android app associated with the contact."""
    android_device: AirbyteSortOrder
    """The device used by the contact for Android."""
    android_last_seen_at: AirbyteSortOrder
    """The date and time when the contact was last seen on Android."""
    android_os_version: AirbyteSortOrder
    """The operating system version of the Android device."""
    android_sdk_version: AirbyteSortOrder
    """The SDK version of the Android device."""
    avatar: AirbyteSortOrder
    """URL pointing to the contact's avatar image."""
    browser: AirbyteSortOrder
    """The browser used by the contact."""
    browser_language: AirbyteSortOrder
    """The language preference set in the contact's browser."""
    browser_version: AirbyteSortOrder
    """The version of the browser used by the contact."""
    companies: AirbyteSortOrder
    """Companies associated with the contact."""
    created_at: AirbyteSortOrder
    """The date and time when the contact was created."""
    custom_attributes: AirbyteSortOrder
    """Custom attributes defined for the contact."""
    email: AirbyteSortOrder
    """The email address of the contact."""
    external_id: AirbyteSortOrder
    """External identifier for the contact."""
    has_hard_bounced: AirbyteSortOrder
    """Flag indicating if the contact has hard bounced."""
    id: AirbyteSortOrder
    """The unique identifier of the contact."""
    ios_app_name: AirbyteSortOrder
    """The name of the iOS app associated with the contact."""
    ios_app_version: AirbyteSortOrder
    """The version of the iOS app associated with the contact."""
    ios_device: AirbyteSortOrder
    """The device used by the contact for iOS."""
    ios_last_seen_at: AirbyteSortOrder
    """The date and time when the contact was last seen on iOS."""
    ios_os_version: AirbyteSortOrder
    """The operating system version of the iOS device."""
    ios_sdk_version: AirbyteSortOrder
    """The SDK version of the iOS device."""
    language_override: AirbyteSortOrder
    """Language override set for the contact."""
    last_contacted_at: AirbyteSortOrder
    """The date and time when the contact was last contacted."""
    last_email_clicked_at: AirbyteSortOrder
    """The date and time when the contact last clicked an email."""
    last_email_opened_at: AirbyteSortOrder
    """The date and time when the contact last opened an email."""
    last_replied_at: AirbyteSortOrder
    """The date and time when the contact last replied."""
    last_seen_at: AirbyteSortOrder
    """The date and time when the contact was last seen overall."""
    location: AirbyteSortOrder
    """Location details of the contact."""
    marked_email_as_spam: AirbyteSortOrder
    """Flag indicating if the contact's email was marked as spam."""
    name: AirbyteSortOrder
    """The name of the contact."""
    notes: AirbyteSortOrder
    """Notes associated with the contact."""
    opted_in_subscription_types: AirbyteSortOrder
    """Subscription types the contact opted into."""
    opted_out_subscription_types: AirbyteSortOrder
    """Subscription types the contact opted out from."""
    os: AirbyteSortOrder
    """Operating system of the contact's device."""
    owner_id: AirbyteSortOrder
    """The unique identifier of the contact's owner."""
    phone: AirbyteSortOrder
    """The phone number of the contact."""
    referrer: AirbyteSortOrder
    """Referrer information related to the contact."""
    role: AirbyteSortOrder
    """Role or position of the contact."""
    signed_up_at: AirbyteSortOrder
    """The date and time when the contact signed up."""
    sms_consent: AirbyteSortOrder
    """Consent status for SMS communication."""
    social_profiles: AirbyteSortOrder
    """Social profiles associated with the contact."""
    tags: AirbyteSortOrder
    """Tags associated with the contact."""
    type: AirbyteSortOrder
    """Type of contact."""
    unsubscribed_from_emails: AirbyteSortOrder
    """Flag indicating if the contact unsubscribed from emails."""
    unsubscribed_from_sms: AirbyteSortOrder
    """Flag indicating if the contact unsubscribed from SMS."""
    updated_at: AirbyteSortOrder
    """The date and time when the contact was last updated."""
    utm_campaign: AirbyteSortOrder
    """Campaign data from UTM parameters."""
    utm_content: AirbyteSortOrder
    """Content data from UTM parameters."""
    utm_medium: AirbyteSortOrder
    """Medium data from UTM parameters."""
    utm_source: AirbyteSortOrder
    """Source data from UTM parameters."""
    utm_term: AirbyteSortOrder
    """Term data from UTM parameters."""
    workspace_id: AirbyteSortOrder
    """The unique identifier of the workspace associated with the contact."""


# Entity-specific condition types for contacts
class ContactsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ContactsSearchFilter


class ContactsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ContactsSearchFilter


class ContactsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ContactsSearchFilter


class ContactsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ContactsSearchFilter


class ContactsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ContactsSearchFilter


class ContactsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ContactsSearchFilter


class ContactsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ContactsStringFilter


class ContactsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ContactsStringFilter


class ContactsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ContactsStringFilter


class ContactsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ContactsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ContactsInCondition = TypedDict("ContactsInCondition", {"in": ContactsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ContactsNotCondition = TypedDict("ContactsNotCondition", {"not": "ContactsCondition"}, total=False)
"""Negates the nested condition."""

ContactsAndCondition = TypedDict("ContactsAndCondition", {"and": "list[ContactsCondition]"}, total=False)
"""True if all nested conditions are true."""

ContactsOrCondition = TypedDict("ContactsOrCondition", {"or": "list[ContactsCondition]"}, total=False)
"""True if any nested condition is true."""

ContactsAnyCondition = TypedDict("ContactsAnyCondition", {"any": ContactsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all contacts condition types
ContactsCondition = (
    ContactsEqCondition
    | ContactsNeqCondition
    | ContactsGtCondition
    | ContactsGteCondition
    | ContactsLtCondition
    | ContactsLteCondition
    | ContactsInCondition
    | ContactsLikeCondition
    | ContactsFuzzyCondition
    | ContactsKeywordCondition
    | ContactsContainsCondition
    | ContactsNotCondition
    | ContactsAndCondition
    | ContactsOrCondition
    | ContactsAnyCondition
)


class ContactsSearchQuery(TypedDict, total=False):
    """Search query for contacts entity."""
    filter: ContactsCondition
    sort: list[ContactsSortFilter]


# ===== CONVERSATIONS SEARCH TYPES =====

class ConversationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering conversations search queries."""
    admin_assignee_id: int | None
    """The ID of the administrator assigned to the conversation"""
    ai_agent: dict[str, Any] | None
    """Data related to AI Agent involvement in the conversation"""
    ai_agent_participated: bool | None
    """Indicates whether AI Agent participated in the conversation"""
    assignee: dict[str, Any] | None
    """The assigned user responsible for the conversation."""
    contacts: dict[str, Any] | None
    """List of contacts involved in the conversation."""
    conversation_message: dict[str, Any] | None
    """The main message content of the conversation."""
    conversation_rating: dict[str, Any] | None
    """Ratings given to the conversation by the customer and teammate."""
    created_at: int | None
    """The timestamp when the conversation was created"""
    custom_attributes: dict[str, Any] | None
    """Custom attributes associated with the conversation"""
    customer_first_reply: dict[str, Any] | None
    """Timestamp indicating when the customer first replied."""
    customers: list[Any] | None
    """List of customers involved in the conversation"""
    first_contact_reply: dict[str, Any] | None
    """Timestamp indicating when the first contact replied."""
    id: str | None
    """The unique ID of the conversation"""
    linked_objects: dict[str, Any] | None
    """Linked objects associated with the conversation"""
    open: bool | None
    """Indicates if the conversation is open or closed"""
    priority: str | None
    """The priority level of the conversation"""
    read: bool | None
    """Indicates if the conversation has been read"""
    redacted: bool | None
    """Indicates if the conversation is redacted"""
    sent_at: int | None
    """The timestamp when the conversation was sent"""
    sla_applied: dict[str, Any] | None
    """Service Level Agreement details applied to the conversation."""
    snoozed_until: int | None
    """Timestamp until the conversation is snoozed"""
    source: dict[str, Any] | None
    """Source details of the conversation."""
    state: str | None
    """The state of the conversation (e.g., new, in progress)"""
    statistics: dict[str, Any] | None
    """Statistics related to the conversation."""
    tags: dict[str, Any] | None
    """Tags applied to the conversation."""
    team_assignee_id: int | None
    """The ID of the team assigned to the conversation"""
    teammates: dict[str, Any] | None
    """List of teammates involved in the conversation."""
    title: str | None
    """The title of the conversation"""
    topics: dict[str, Any] | None
    """Topics associated with the conversation."""
    type: str | None
    """The type of the conversation"""
    updated_at: int | None
    """The timestamp when the conversation was last updated"""
    user: dict[str, Any] | None
    """The user related to the conversation."""
    waiting_since: int | None
    """Timestamp since waiting for a response"""


class ConversationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    admin_assignee_id: list[int]
    """The ID of the administrator assigned to the conversation"""
    ai_agent: list[dict[str, Any]]
    """Data related to AI Agent involvement in the conversation"""
    ai_agent_participated: list[bool]
    """Indicates whether AI Agent participated in the conversation"""
    assignee: list[dict[str, Any]]
    """The assigned user responsible for the conversation."""
    contacts: list[dict[str, Any]]
    """List of contacts involved in the conversation."""
    conversation_message: list[dict[str, Any]]
    """The main message content of the conversation."""
    conversation_rating: list[dict[str, Any]]
    """Ratings given to the conversation by the customer and teammate."""
    created_at: list[int]
    """The timestamp when the conversation was created"""
    custom_attributes: list[dict[str, Any]]
    """Custom attributes associated with the conversation"""
    customer_first_reply: list[dict[str, Any]]
    """Timestamp indicating when the customer first replied."""
    customers: list[list[Any]]
    """List of customers involved in the conversation"""
    first_contact_reply: list[dict[str, Any]]
    """Timestamp indicating when the first contact replied."""
    id: list[str]
    """The unique ID of the conversation"""
    linked_objects: list[dict[str, Any]]
    """Linked objects associated with the conversation"""
    open: list[bool]
    """Indicates if the conversation is open or closed"""
    priority: list[str]
    """The priority level of the conversation"""
    read: list[bool]
    """Indicates if the conversation has been read"""
    redacted: list[bool]
    """Indicates if the conversation is redacted"""
    sent_at: list[int]
    """The timestamp when the conversation was sent"""
    sla_applied: list[dict[str, Any]]
    """Service Level Agreement details applied to the conversation."""
    snoozed_until: list[int]
    """Timestamp until the conversation is snoozed"""
    source: list[dict[str, Any]]
    """Source details of the conversation."""
    state: list[str]
    """The state of the conversation (e.g., new, in progress)"""
    statistics: list[dict[str, Any]]
    """Statistics related to the conversation."""
    tags: list[dict[str, Any]]
    """Tags applied to the conversation."""
    team_assignee_id: list[int]
    """The ID of the team assigned to the conversation"""
    teammates: list[dict[str, Any]]
    """List of teammates involved in the conversation."""
    title: list[str]
    """The title of the conversation"""
    topics: list[dict[str, Any]]
    """Topics associated with the conversation."""
    type: list[str]
    """The type of the conversation"""
    updated_at: list[int]
    """The timestamp when the conversation was last updated"""
    user: list[dict[str, Any]]
    """The user related to the conversation."""
    waiting_since: list[int]
    """Timestamp since waiting for a response"""


class ConversationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    admin_assignee_id: Any
    """The ID of the administrator assigned to the conversation"""
    ai_agent: Any
    """Data related to AI Agent involvement in the conversation"""
    ai_agent_participated: Any
    """Indicates whether AI Agent participated in the conversation"""
    assignee: Any
    """The assigned user responsible for the conversation."""
    contacts: Any
    """List of contacts involved in the conversation."""
    conversation_message: Any
    """The main message content of the conversation."""
    conversation_rating: Any
    """Ratings given to the conversation by the customer and teammate."""
    created_at: Any
    """The timestamp when the conversation was created"""
    custom_attributes: Any
    """Custom attributes associated with the conversation"""
    customer_first_reply: Any
    """Timestamp indicating when the customer first replied."""
    customers: Any
    """List of customers involved in the conversation"""
    first_contact_reply: Any
    """Timestamp indicating when the first contact replied."""
    id: Any
    """The unique ID of the conversation"""
    linked_objects: Any
    """Linked objects associated with the conversation"""
    open: Any
    """Indicates if the conversation is open or closed"""
    priority: Any
    """The priority level of the conversation"""
    read: Any
    """Indicates if the conversation has been read"""
    redacted: Any
    """Indicates if the conversation is redacted"""
    sent_at: Any
    """The timestamp when the conversation was sent"""
    sla_applied: Any
    """Service Level Agreement details applied to the conversation."""
    snoozed_until: Any
    """Timestamp until the conversation is snoozed"""
    source: Any
    """Source details of the conversation."""
    state: Any
    """The state of the conversation (e.g., new, in progress)"""
    statistics: Any
    """Statistics related to the conversation."""
    tags: Any
    """Tags applied to the conversation."""
    team_assignee_id: Any
    """The ID of the team assigned to the conversation"""
    teammates: Any
    """List of teammates involved in the conversation."""
    title: Any
    """The title of the conversation"""
    topics: Any
    """Topics associated with the conversation."""
    type: Any
    """The type of the conversation"""
    updated_at: Any
    """The timestamp when the conversation was last updated"""
    user: Any
    """The user related to the conversation."""
    waiting_since: Any
    """Timestamp since waiting for a response"""


class ConversationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    admin_assignee_id: str
    """The ID of the administrator assigned to the conversation"""
    ai_agent: str
    """Data related to AI Agent involvement in the conversation"""
    ai_agent_participated: str
    """Indicates whether AI Agent participated in the conversation"""
    assignee: str
    """The assigned user responsible for the conversation."""
    contacts: str
    """List of contacts involved in the conversation."""
    conversation_message: str
    """The main message content of the conversation."""
    conversation_rating: str
    """Ratings given to the conversation by the customer and teammate."""
    created_at: str
    """The timestamp when the conversation was created"""
    custom_attributes: str
    """Custom attributes associated with the conversation"""
    customer_first_reply: str
    """Timestamp indicating when the customer first replied."""
    customers: str
    """List of customers involved in the conversation"""
    first_contact_reply: str
    """Timestamp indicating when the first contact replied."""
    id: str
    """The unique ID of the conversation"""
    linked_objects: str
    """Linked objects associated with the conversation"""
    open: str
    """Indicates if the conversation is open or closed"""
    priority: str
    """The priority level of the conversation"""
    read: str
    """Indicates if the conversation has been read"""
    redacted: str
    """Indicates if the conversation is redacted"""
    sent_at: str
    """The timestamp when the conversation was sent"""
    sla_applied: str
    """Service Level Agreement details applied to the conversation."""
    snoozed_until: str
    """Timestamp until the conversation is snoozed"""
    source: str
    """Source details of the conversation."""
    state: str
    """The state of the conversation (e.g., new, in progress)"""
    statistics: str
    """Statistics related to the conversation."""
    tags: str
    """Tags applied to the conversation."""
    team_assignee_id: str
    """The ID of the team assigned to the conversation"""
    teammates: str
    """List of teammates involved in the conversation."""
    title: str
    """The title of the conversation"""
    topics: str
    """Topics associated with the conversation."""
    type: str
    """The type of the conversation"""
    updated_at: str
    """The timestamp when the conversation was last updated"""
    user: str
    """The user related to the conversation."""
    waiting_since: str
    """Timestamp since waiting for a response"""


class ConversationsSortFilter(TypedDict, total=False):
    """Available fields for sorting conversations search results."""
    admin_assignee_id: AirbyteSortOrder
    """The ID of the administrator assigned to the conversation"""
    ai_agent: AirbyteSortOrder
    """Data related to AI Agent involvement in the conversation"""
    ai_agent_participated: AirbyteSortOrder
    """Indicates whether AI Agent participated in the conversation"""
    assignee: AirbyteSortOrder
    """The assigned user responsible for the conversation."""
    contacts: AirbyteSortOrder
    """List of contacts involved in the conversation."""
    conversation_message: AirbyteSortOrder
    """The main message content of the conversation."""
    conversation_rating: AirbyteSortOrder
    """Ratings given to the conversation by the customer and teammate."""
    created_at: AirbyteSortOrder
    """The timestamp when the conversation was created"""
    custom_attributes: AirbyteSortOrder
    """Custom attributes associated with the conversation"""
    customer_first_reply: AirbyteSortOrder
    """Timestamp indicating when the customer first replied."""
    customers: AirbyteSortOrder
    """List of customers involved in the conversation"""
    first_contact_reply: AirbyteSortOrder
    """Timestamp indicating when the first contact replied."""
    id: AirbyteSortOrder
    """The unique ID of the conversation"""
    linked_objects: AirbyteSortOrder
    """Linked objects associated with the conversation"""
    open: AirbyteSortOrder
    """Indicates if the conversation is open or closed"""
    priority: AirbyteSortOrder
    """The priority level of the conversation"""
    read: AirbyteSortOrder
    """Indicates if the conversation has been read"""
    redacted: AirbyteSortOrder
    """Indicates if the conversation is redacted"""
    sent_at: AirbyteSortOrder
    """The timestamp when the conversation was sent"""
    sla_applied: AirbyteSortOrder
    """Service Level Agreement details applied to the conversation."""
    snoozed_until: AirbyteSortOrder
    """Timestamp until the conversation is snoozed"""
    source: AirbyteSortOrder
    """Source details of the conversation."""
    state: AirbyteSortOrder
    """The state of the conversation (e.g., new, in progress)"""
    statistics: AirbyteSortOrder
    """Statistics related to the conversation."""
    tags: AirbyteSortOrder
    """Tags applied to the conversation."""
    team_assignee_id: AirbyteSortOrder
    """The ID of the team assigned to the conversation"""
    teammates: AirbyteSortOrder
    """List of teammates involved in the conversation."""
    title: AirbyteSortOrder
    """The title of the conversation"""
    topics: AirbyteSortOrder
    """Topics associated with the conversation."""
    type: AirbyteSortOrder
    """The type of the conversation"""
    updated_at: AirbyteSortOrder
    """The timestamp when the conversation was last updated"""
    user: AirbyteSortOrder
    """The user related to the conversation."""
    waiting_since: AirbyteSortOrder
    """Timestamp since waiting for a response"""


# Entity-specific condition types for conversations
class ConversationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ConversationsSearchFilter


class ConversationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ConversationsSearchFilter


class ConversationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ConversationsSearchFilter


class ConversationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ConversationsSearchFilter


class ConversationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ConversationsSearchFilter


class ConversationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ConversationsSearchFilter


class ConversationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ConversationsStringFilter


class ConversationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ConversationsStringFilter


class ConversationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ConversationsStringFilter


class ConversationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ConversationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ConversationsInCondition = TypedDict("ConversationsInCondition", {"in": ConversationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ConversationsNotCondition = TypedDict("ConversationsNotCondition", {"not": "ConversationsCondition"}, total=False)
"""Negates the nested condition."""

ConversationsAndCondition = TypedDict("ConversationsAndCondition", {"and": "list[ConversationsCondition]"}, total=False)
"""True if all nested conditions are true."""

ConversationsOrCondition = TypedDict("ConversationsOrCondition", {"or": "list[ConversationsCondition]"}, total=False)
"""True if any nested condition is true."""

ConversationsAnyCondition = TypedDict("ConversationsAnyCondition", {"any": ConversationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all conversations condition types
ConversationsCondition = (
    ConversationsEqCondition
    | ConversationsNeqCondition
    | ConversationsGtCondition
    | ConversationsGteCondition
    | ConversationsLtCondition
    | ConversationsLteCondition
    | ConversationsInCondition
    | ConversationsLikeCondition
    | ConversationsFuzzyCondition
    | ConversationsKeywordCondition
    | ConversationsContainsCondition
    | ConversationsNotCondition
    | ConversationsAndCondition
    | ConversationsOrCondition
    | ConversationsAnyCondition
)


class ConversationsSearchQuery(TypedDict, total=False):
    """Search query for conversations entity."""
    filter: ConversationsCondition
    sort: list[ConversationsSortFilter]


# ===== TEAMS SEARCH TYPES =====

class TeamsSearchFilter(TypedDict, total=False):
    """Available fields for filtering teams search queries."""
    admin_ids: list[Any] | None
    """Array of user IDs representing the admins of the team."""
    id: str | None
    """Unique identifier for the team."""
    name: str | None
    """Name of the team."""
    type: str | None
    """Type of team (e.g., 'internal', 'external')."""


class TeamsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    admin_ids: list[list[Any]]
    """Array of user IDs representing the admins of the team."""
    id: list[str]
    """Unique identifier for the team."""
    name: list[str]
    """Name of the team."""
    type: list[str]
    """Type of team (e.g., 'internal', 'external')."""


class TeamsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    admin_ids: Any
    """Array of user IDs representing the admins of the team."""
    id: Any
    """Unique identifier for the team."""
    name: Any
    """Name of the team."""
    type: Any
    """Type of team (e.g., 'internal', 'external')."""


class TeamsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    admin_ids: str
    """Array of user IDs representing the admins of the team."""
    id: str
    """Unique identifier for the team."""
    name: str
    """Name of the team."""
    type: str
    """Type of team (e.g., 'internal', 'external')."""


class TeamsSortFilter(TypedDict, total=False):
    """Available fields for sorting teams search results."""
    admin_ids: AirbyteSortOrder
    """Array of user IDs representing the admins of the team."""
    id: AirbyteSortOrder
    """Unique identifier for the team."""
    name: AirbyteSortOrder
    """Name of the team."""
    type: AirbyteSortOrder
    """Type of team (e.g., 'internal', 'external')."""


# Entity-specific condition types for teams
class TeamsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TeamsSearchFilter


class TeamsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TeamsSearchFilter


class TeamsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TeamsSearchFilter


class TeamsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TeamsSearchFilter


class TeamsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TeamsSearchFilter


class TeamsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TeamsSearchFilter


class TeamsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TeamsStringFilter


class TeamsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TeamsStringFilter


class TeamsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TeamsStringFilter


class TeamsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TeamsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TeamsInCondition = TypedDict("TeamsInCondition", {"in": TeamsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TeamsNotCondition = TypedDict("TeamsNotCondition", {"not": "TeamsCondition"}, total=False)
"""Negates the nested condition."""

TeamsAndCondition = TypedDict("TeamsAndCondition", {"and": "list[TeamsCondition]"}, total=False)
"""True if all nested conditions are true."""

TeamsOrCondition = TypedDict("TeamsOrCondition", {"or": "list[TeamsCondition]"}, total=False)
"""True if any nested condition is true."""

TeamsAnyCondition = TypedDict("TeamsAnyCondition", {"any": TeamsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all teams condition types
TeamsCondition = (
    TeamsEqCondition
    | TeamsNeqCondition
    | TeamsGtCondition
    | TeamsGteCondition
    | TeamsLtCondition
    | TeamsLteCondition
    | TeamsInCondition
    | TeamsLikeCondition
    | TeamsFuzzyCondition
    | TeamsKeywordCondition
    | TeamsContainsCondition
    | TeamsNotCondition
    | TeamsAndCondition
    | TeamsOrCondition
    | TeamsAnyCondition
)


class TeamsSearchQuery(TypedDict, total=False):
    """Search query for teams entity."""
    filter: TeamsCondition
    sort: list[TeamsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
