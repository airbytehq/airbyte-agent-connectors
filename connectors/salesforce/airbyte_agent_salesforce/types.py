"""
Type definitions for salesforce connector.
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

class AccountsListParams(TypedDict):
    """Parameters for accounts.list operation"""
    q: str

class AccountsGetParams(TypedDict):
    """Parameters for accounts.get operation"""
    id: str
    fields: NotRequired[str]

class AccountsApiSearchParams(TypedDict):
    """Parameters for accounts.api_search operation"""
    q: str

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    q: str

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    id: str
    fields: NotRequired[str]

class ContactsApiSearchParams(TypedDict):
    """Parameters for contacts.api_search operation"""
    q: str

class LeadsListParams(TypedDict):
    """Parameters for leads.list operation"""
    q: str

class LeadsGetParams(TypedDict):
    """Parameters for leads.get operation"""
    id: str
    fields: NotRequired[str]

class LeadsApiSearchParams(TypedDict):
    """Parameters for leads.api_search operation"""
    q: str

class OpportunitiesListParams(TypedDict):
    """Parameters for opportunities.list operation"""
    q: str

class OpportunitiesGetParams(TypedDict):
    """Parameters for opportunities.get operation"""
    id: str
    fields: NotRequired[str]

class OpportunitiesApiSearchParams(TypedDict):
    """Parameters for opportunities.api_search operation"""
    q: str

class TasksListParams(TypedDict):
    """Parameters for tasks.list operation"""
    q: str

class TasksGetParams(TypedDict):
    """Parameters for tasks.get operation"""
    id: str
    fields: NotRequired[str]

class TasksApiSearchParams(TypedDict):
    """Parameters for tasks.api_search operation"""
    q: str

class EventsListParams(TypedDict):
    """Parameters for events.list operation"""
    q: str

class EventsGetParams(TypedDict):
    """Parameters for events.get operation"""
    id: str
    fields: NotRequired[str]

class EventsApiSearchParams(TypedDict):
    """Parameters for events.api_search operation"""
    q: str

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    q: str

class CampaignsGetParams(TypedDict):
    """Parameters for campaigns.get operation"""
    id: str
    fields: NotRequired[str]

class CampaignsApiSearchParams(TypedDict):
    """Parameters for campaigns.api_search operation"""
    q: str

class CasesListParams(TypedDict):
    """Parameters for cases.list operation"""
    q: str

class CasesGetParams(TypedDict):
    """Parameters for cases.get operation"""
    id: str
    fields: NotRequired[str]

class CasesApiSearchParams(TypedDict):
    """Parameters for cases.api_search operation"""
    q: str

class NotesListParams(TypedDict):
    """Parameters for notes.list operation"""
    q: str

class NotesGetParams(TypedDict):
    """Parameters for notes.get operation"""
    id: str
    fields: NotRequired[str]

class NotesApiSearchParams(TypedDict):
    """Parameters for notes.api_search operation"""
    q: str

class ContentVersionsListParams(TypedDict):
    """Parameters for content_versions.list operation"""
    q: str

class ContentVersionsGetParams(TypedDict):
    """Parameters for content_versions.get operation"""
    id: str
    fields: NotRequired[str]

class ContentVersionsDownloadParams(TypedDict):
    """Parameters for content_versions.download operation"""
    id: str
    range_header: NotRequired[str]

class AttachmentsListParams(TypedDict):
    """Parameters for attachments.list operation"""
    q: str

class AttachmentsGetParams(TypedDict):
    """Parameters for attachments.get operation"""
    id: str
    fields: NotRequired[str]

class AttachmentsDownloadParams(TypedDict):
    """Parameters for attachments.download operation"""
    id: str
    range_header: NotRequired[str]

class QueryListParams(TypedDict):
    """Parameters for query.list operation"""
    q: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ACCOUNTS SEARCH TYPES =====

class AccountsSearchFilter(TypedDict, total=False):
    """Available fields for filtering accounts search queries."""
    id: str
    """Unique identifier for the account record"""
    name: str | None
    """Name of the account or company"""
    account_source: str | None
    """Source of the account record (e.g., Web, Referral)"""
    billing_address: dict[str, Any] | None
    """Complete billing address as a compound field"""
    billing_city: str | None
    """City portion of the billing address"""
    billing_country: str | None
    """Country portion of the billing address"""
    billing_postal_code: str | None
    """Postal code portion of the billing address"""
    billing_state: str | None
    """State or province portion of the billing address"""
    billing_street: str | None
    """Street address portion of the billing address"""
    created_by_id: str | None
    """ID of the user who created this account"""
    created_date: str | None
    """Date and time when the account was created"""
    description: str | None
    """Text description of the account"""
    industry: str | None
    """Primary business industry of the account"""
    is_deleted: bool | None
    """Whether the account has been moved to the Recycle Bin"""
    last_activity_date: str | None
    """Date of the last activity associated with this account"""
    last_modified_by_id: str | None
    """ID of the user who last modified this account"""
    last_modified_date: str | None
    """Date and time when the account was last modified"""
    number_of_employees: int | None
    """Number of employees at the account"""
    owner_id: str | None
    """ID of the user who owns this account"""
    parent_id: str | None
    """ID of the parent account, if this is a subsidiary"""
    phone: str | None
    """Primary phone number for the account"""
    shipping_address: dict[str, Any] | None
    """Complete shipping address as a compound field"""
    shipping_city: str | None
    """City portion of the shipping address"""
    shipping_country: str | None
    """Country portion of the shipping address"""
    shipping_postal_code: str | None
    """Postal code portion of the shipping address"""
    shipping_state: str | None
    """State or province portion of the shipping address"""
    shipping_street: str | None
    """Street address portion of the shipping address"""
    type: str | None
    """Type of account (e.g., Customer, Partner, Competitor)"""
    website: str | None
    """Website URL for the account"""
    system_modstamp: str | None
    """System timestamp when the record was last modified"""


class AccountsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the account record"""
    name: list[str]
    """Name of the account or company"""
    account_source: list[str]
    """Source of the account record (e.g., Web, Referral)"""
    billing_address: list[dict[str, Any]]
    """Complete billing address as a compound field"""
    billing_city: list[str]
    """City portion of the billing address"""
    billing_country: list[str]
    """Country portion of the billing address"""
    billing_postal_code: list[str]
    """Postal code portion of the billing address"""
    billing_state: list[str]
    """State or province portion of the billing address"""
    billing_street: list[str]
    """Street address portion of the billing address"""
    created_by_id: list[str]
    """ID of the user who created this account"""
    created_date: list[str]
    """Date and time when the account was created"""
    description: list[str]
    """Text description of the account"""
    industry: list[str]
    """Primary business industry of the account"""
    is_deleted: list[bool]
    """Whether the account has been moved to the Recycle Bin"""
    last_activity_date: list[str]
    """Date of the last activity associated with this account"""
    last_modified_by_id: list[str]
    """ID of the user who last modified this account"""
    last_modified_date: list[str]
    """Date and time when the account was last modified"""
    number_of_employees: list[int]
    """Number of employees at the account"""
    owner_id: list[str]
    """ID of the user who owns this account"""
    parent_id: list[str]
    """ID of the parent account, if this is a subsidiary"""
    phone: list[str]
    """Primary phone number for the account"""
    shipping_address: list[dict[str, Any]]
    """Complete shipping address as a compound field"""
    shipping_city: list[str]
    """City portion of the shipping address"""
    shipping_country: list[str]
    """Country portion of the shipping address"""
    shipping_postal_code: list[str]
    """Postal code portion of the shipping address"""
    shipping_state: list[str]
    """State or province portion of the shipping address"""
    shipping_street: list[str]
    """Street address portion of the shipping address"""
    type: list[str]
    """Type of account (e.g., Customer, Partner, Competitor)"""
    website: list[str]
    """Website URL for the account"""
    system_modstamp: list[str]
    """System timestamp when the record was last modified"""


class AccountsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the account record"""
    name: Any
    """Name of the account or company"""
    account_source: Any
    """Source of the account record (e.g., Web, Referral)"""
    billing_address: Any
    """Complete billing address as a compound field"""
    billing_city: Any
    """City portion of the billing address"""
    billing_country: Any
    """Country portion of the billing address"""
    billing_postal_code: Any
    """Postal code portion of the billing address"""
    billing_state: Any
    """State or province portion of the billing address"""
    billing_street: Any
    """Street address portion of the billing address"""
    created_by_id: Any
    """ID of the user who created this account"""
    created_date: Any
    """Date and time when the account was created"""
    description: Any
    """Text description of the account"""
    industry: Any
    """Primary business industry of the account"""
    is_deleted: Any
    """Whether the account has been moved to the Recycle Bin"""
    last_activity_date: Any
    """Date of the last activity associated with this account"""
    last_modified_by_id: Any
    """ID of the user who last modified this account"""
    last_modified_date: Any
    """Date and time when the account was last modified"""
    number_of_employees: Any
    """Number of employees at the account"""
    owner_id: Any
    """ID of the user who owns this account"""
    parent_id: Any
    """ID of the parent account, if this is a subsidiary"""
    phone: Any
    """Primary phone number for the account"""
    shipping_address: Any
    """Complete shipping address as a compound field"""
    shipping_city: Any
    """City portion of the shipping address"""
    shipping_country: Any
    """Country portion of the shipping address"""
    shipping_postal_code: Any
    """Postal code portion of the shipping address"""
    shipping_state: Any
    """State or province portion of the shipping address"""
    shipping_street: Any
    """Street address portion of the shipping address"""
    type: Any
    """Type of account (e.g., Customer, Partner, Competitor)"""
    website: Any
    """Website URL for the account"""
    system_modstamp: Any
    """System timestamp when the record was last modified"""


class AccountsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the account record"""
    name: str
    """Name of the account or company"""
    account_source: str
    """Source of the account record (e.g., Web, Referral)"""
    billing_address: str
    """Complete billing address as a compound field"""
    billing_city: str
    """City portion of the billing address"""
    billing_country: str
    """Country portion of the billing address"""
    billing_postal_code: str
    """Postal code portion of the billing address"""
    billing_state: str
    """State or province portion of the billing address"""
    billing_street: str
    """Street address portion of the billing address"""
    created_by_id: str
    """ID of the user who created this account"""
    created_date: str
    """Date and time when the account was created"""
    description: str
    """Text description of the account"""
    industry: str
    """Primary business industry of the account"""
    is_deleted: str
    """Whether the account has been moved to the Recycle Bin"""
    last_activity_date: str
    """Date of the last activity associated with this account"""
    last_modified_by_id: str
    """ID of the user who last modified this account"""
    last_modified_date: str
    """Date and time when the account was last modified"""
    number_of_employees: str
    """Number of employees at the account"""
    owner_id: str
    """ID of the user who owns this account"""
    parent_id: str
    """ID of the parent account, if this is a subsidiary"""
    phone: str
    """Primary phone number for the account"""
    shipping_address: str
    """Complete shipping address as a compound field"""
    shipping_city: str
    """City portion of the shipping address"""
    shipping_country: str
    """Country portion of the shipping address"""
    shipping_postal_code: str
    """Postal code portion of the shipping address"""
    shipping_state: str
    """State or province portion of the shipping address"""
    shipping_street: str
    """Street address portion of the shipping address"""
    type: str
    """Type of account (e.g., Customer, Partner, Competitor)"""
    website: str
    """Website URL for the account"""
    system_modstamp: str
    """System timestamp when the record was last modified"""


class AccountsSortFilter(TypedDict, total=False):
    """Available fields for sorting accounts search results."""
    id: AirbyteSortOrder
    """Unique identifier for the account record"""
    name: AirbyteSortOrder
    """Name of the account or company"""
    account_source: AirbyteSortOrder
    """Source of the account record (e.g., Web, Referral)"""
    billing_address: AirbyteSortOrder
    """Complete billing address as a compound field"""
    billing_city: AirbyteSortOrder
    """City portion of the billing address"""
    billing_country: AirbyteSortOrder
    """Country portion of the billing address"""
    billing_postal_code: AirbyteSortOrder
    """Postal code portion of the billing address"""
    billing_state: AirbyteSortOrder
    """State or province portion of the billing address"""
    billing_street: AirbyteSortOrder
    """Street address portion of the billing address"""
    created_by_id: AirbyteSortOrder
    """ID of the user who created this account"""
    created_date: AirbyteSortOrder
    """Date and time when the account was created"""
    description: AirbyteSortOrder
    """Text description of the account"""
    industry: AirbyteSortOrder
    """Primary business industry of the account"""
    is_deleted: AirbyteSortOrder
    """Whether the account has been moved to the Recycle Bin"""
    last_activity_date: AirbyteSortOrder
    """Date of the last activity associated with this account"""
    last_modified_by_id: AirbyteSortOrder
    """ID of the user who last modified this account"""
    last_modified_date: AirbyteSortOrder
    """Date and time when the account was last modified"""
    number_of_employees: AirbyteSortOrder
    """Number of employees at the account"""
    owner_id: AirbyteSortOrder
    """ID of the user who owns this account"""
    parent_id: AirbyteSortOrder
    """ID of the parent account, if this is a subsidiary"""
    phone: AirbyteSortOrder
    """Primary phone number for the account"""
    shipping_address: AirbyteSortOrder
    """Complete shipping address as a compound field"""
    shipping_city: AirbyteSortOrder
    """City portion of the shipping address"""
    shipping_country: AirbyteSortOrder
    """Country portion of the shipping address"""
    shipping_postal_code: AirbyteSortOrder
    """Postal code portion of the shipping address"""
    shipping_state: AirbyteSortOrder
    """State or province portion of the shipping address"""
    shipping_street: AirbyteSortOrder
    """Street address portion of the shipping address"""
    type: AirbyteSortOrder
    """Type of account (e.g., Customer, Partner, Competitor)"""
    website: AirbyteSortOrder
    """Website URL for the account"""
    system_modstamp: AirbyteSortOrder
    """System timestamp when the record was last modified"""


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


# ===== CONTACTS SEARCH TYPES =====

class ContactsSearchFilter(TypedDict, total=False):
    """Available fields for filtering contacts search queries."""
    id: str
    """Unique identifier for the contact record"""
    account_id: str | None
    """ID of the account this contact is associated with"""
    created_by_id: str | None
    """ID of the user who created this contact"""
    created_date: str | None
    """Date and time when the contact was created"""
    department: str | None
    """Department within the account where the contact works"""
    email: str | None
    """Email address of the contact"""
    first_name: str | None
    """First name of the contact"""
    is_deleted: bool | None
    """Whether the contact has been moved to the Recycle Bin"""
    last_activity_date: str | None
    """Date of the last activity associated with this contact"""
    last_modified_by_id: str | None
    """ID of the user who last modified this contact"""
    last_modified_date: str | None
    """Date and time when the contact was last modified"""
    last_name: str | None
    """Last name of the contact"""
    lead_source: str | None
    """Source from which this contact originated"""
    mailing_address: dict[str, Any] | None
    """Complete mailing address as a compound field"""
    mailing_city: str | None
    """City portion of the mailing address"""
    mailing_country: str | None
    """Country portion of the mailing address"""
    mailing_postal_code: str | None
    """Postal code portion of the mailing address"""
    mailing_state: str | None
    """State or province portion of the mailing address"""
    mailing_street: str | None
    """Street address portion of the mailing address"""
    mobile_phone: str | None
    """Mobile phone number of the contact"""
    name: str | None
    """Full name of the contact (read-only, concatenation of first and last name)"""
    owner_id: str | None
    """ID of the user who owns this contact"""
    phone: str | None
    """Business phone number of the contact"""
    reports_to_id: str | None
    """ID of the contact this contact reports to"""
    title: str | None
    """Job title of the contact"""
    system_modstamp: str | None
    """System timestamp when the record was last modified"""


class ContactsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the contact record"""
    account_id: list[str]
    """ID of the account this contact is associated with"""
    created_by_id: list[str]
    """ID of the user who created this contact"""
    created_date: list[str]
    """Date and time when the contact was created"""
    department: list[str]
    """Department within the account where the contact works"""
    email: list[str]
    """Email address of the contact"""
    first_name: list[str]
    """First name of the contact"""
    is_deleted: list[bool]
    """Whether the contact has been moved to the Recycle Bin"""
    last_activity_date: list[str]
    """Date of the last activity associated with this contact"""
    last_modified_by_id: list[str]
    """ID of the user who last modified this contact"""
    last_modified_date: list[str]
    """Date and time when the contact was last modified"""
    last_name: list[str]
    """Last name of the contact"""
    lead_source: list[str]
    """Source from which this contact originated"""
    mailing_address: list[dict[str, Any]]
    """Complete mailing address as a compound field"""
    mailing_city: list[str]
    """City portion of the mailing address"""
    mailing_country: list[str]
    """Country portion of the mailing address"""
    mailing_postal_code: list[str]
    """Postal code portion of the mailing address"""
    mailing_state: list[str]
    """State or province portion of the mailing address"""
    mailing_street: list[str]
    """Street address portion of the mailing address"""
    mobile_phone: list[str]
    """Mobile phone number of the contact"""
    name: list[str]
    """Full name of the contact (read-only, concatenation of first and last name)"""
    owner_id: list[str]
    """ID of the user who owns this contact"""
    phone: list[str]
    """Business phone number of the contact"""
    reports_to_id: list[str]
    """ID of the contact this contact reports to"""
    title: list[str]
    """Job title of the contact"""
    system_modstamp: list[str]
    """System timestamp when the record was last modified"""


class ContactsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the contact record"""
    account_id: Any
    """ID of the account this contact is associated with"""
    created_by_id: Any
    """ID of the user who created this contact"""
    created_date: Any
    """Date and time when the contact was created"""
    department: Any
    """Department within the account where the contact works"""
    email: Any
    """Email address of the contact"""
    first_name: Any
    """First name of the contact"""
    is_deleted: Any
    """Whether the contact has been moved to the Recycle Bin"""
    last_activity_date: Any
    """Date of the last activity associated with this contact"""
    last_modified_by_id: Any
    """ID of the user who last modified this contact"""
    last_modified_date: Any
    """Date and time when the contact was last modified"""
    last_name: Any
    """Last name of the contact"""
    lead_source: Any
    """Source from which this contact originated"""
    mailing_address: Any
    """Complete mailing address as a compound field"""
    mailing_city: Any
    """City portion of the mailing address"""
    mailing_country: Any
    """Country portion of the mailing address"""
    mailing_postal_code: Any
    """Postal code portion of the mailing address"""
    mailing_state: Any
    """State or province portion of the mailing address"""
    mailing_street: Any
    """Street address portion of the mailing address"""
    mobile_phone: Any
    """Mobile phone number of the contact"""
    name: Any
    """Full name of the contact (read-only, concatenation of first and last name)"""
    owner_id: Any
    """ID of the user who owns this contact"""
    phone: Any
    """Business phone number of the contact"""
    reports_to_id: Any
    """ID of the contact this contact reports to"""
    title: Any
    """Job title of the contact"""
    system_modstamp: Any
    """System timestamp when the record was last modified"""


class ContactsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the contact record"""
    account_id: str
    """ID of the account this contact is associated with"""
    created_by_id: str
    """ID of the user who created this contact"""
    created_date: str
    """Date and time when the contact was created"""
    department: str
    """Department within the account where the contact works"""
    email: str
    """Email address of the contact"""
    first_name: str
    """First name of the contact"""
    is_deleted: str
    """Whether the contact has been moved to the Recycle Bin"""
    last_activity_date: str
    """Date of the last activity associated with this contact"""
    last_modified_by_id: str
    """ID of the user who last modified this contact"""
    last_modified_date: str
    """Date and time when the contact was last modified"""
    last_name: str
    """Last name of the contact"""
    lead_source: str
    """Source from which this contact originated"""
    mailing_address: str
    """Complete mailing address as a compound field"""
    mailing_city: str
    """City portion of the mailing address"""
    mailing_country: str
    """Country portion of the mailing address"""
    mailing_postal_code: str
    """Postal code portion of the mailing address"""
    mailing_state: str
    """State or province portion of the mailing address"""
    mailing_street: str
    """Street address portion of the mailing address"""
    mobile_phone: str
    """Mobile phone number of the contact"""
    name: str
    """Full name of the contact (read-only, concatenation of first and last name)"""
    owner_id: str
    """ID of the user who owns this contact"""
    phone: str
    """Business phone number of the contact"""
    reports_to_id: str
    """ID of the contact this contact reports to"""
    title: str
    """Job title of the contact"""
    system_modstamp: str
    """System timestamp when the record was last modified"""


class ContactsSortFilter(TypedDict, total=False):
    """Available fields for sorting contacts search results."""
    id: AirbyteSortOrder
    """Unique identifier for the contact record"""
    account_id: AirbyteSortOrder
    """ID of the account this contact is associated with"""
    created_by_id: AirbyteSortOrder
    """ID of the user who created this contact"""
    created_date: AirbyteSortOrder
    """Date and time when the contact was created"""
    department: AirbyteSortOrder
    """Department within the account where the contact works"""
    email: AirbyteSortOrder
    """Email address of the contact"""
    first_name: AirbyteSortOrder
    """First name of the contact"""
    is_deleted: AirbyteSortOrder
    """Whether the contact has been moved to the Recycle Bin"""
    last_activity_date: AirbyteSortOrder
    """Date of the last activity associated with this contact"""
    last_modified_by_id: AirbyteSortOrder
    """ID of the user who last modified this contact"""
    last_modified_date: AirbyteSortOrder
    """Date and time when the contact was last modified"""
    last_name: AirbyteSortOrder
    """Last name of the contact"""
    lead_source: AirbyteSortOrder
    """Source from which this contact originated"""
    mailing_address: AirbyteSortOrder
    """Complete mailing address as a compound field"""
    mailing_city: AirbyteSortOrder
    """City portion of the mailing address"""
    mailing_country: AirbyteSortOrder
    """Country portion of the mailing address"""
    mailing_postal_code: AirbyteSortOrder
    """Postal code portion of the mailing address"""
    mailing_state: AirbyteSortOrder
    """State or province portion of the mailing address"""
    mailing_street: AirbyteSortOrder
    """Street address portion of the mailing address"""
    mobile_phone: AirbyteSortOrder
    """Mobile phone number of the contact"""
    name: AirbyteSortOrder
    """Full name of the contact (read-only, concatenation of first and last name)"""
    owner_id: AirbyteSortOrder
    """ID of the user who owns this contact"""
    phone: AirbyteSortOrder
    """Business phone number of the contact"""
    reports_to_id: AirbyteSortOrder
    """ID of the contact this contact reports to"""
    title: AirbyteSortOrder
    """Job title of the contact"""
    system_modstamp: AirbyteSortOrder
    """System timestamp when the record was last modified"""


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


# ===== LEADS SEARCH TYPES =====

class LeadsSearchFilter(TypedDict, total=False):
    """Available fields for filtering leads search queries."""
    id: str
    """Unique identifier for the lead record"""
    address: dict[str, Any] | None
    """Complete address as a compound field"""
    city: str | None
    """City portion of the address"""
    company: str | None
    """Company or organization the lead works for"""
    converted_account_id: str | None
    """ID of the account created when lead was converted"""
    converted_contact_id: str | None
    """ID of the contact created when lead was converted"""
    converted_date: str | None
    """Date when the lead was converted"""
    converted_opportunity_id: str | None
    """ID of the opportunity created when lead was converted"""
    country: str | None
    """Country portion of the address"""
    created_by_id: str | None
    """ID of the user who created this lead"""
    created_date: str | None
    """Date and time when the lead was created"""
    email: str | None
    """Email address of the lead"""
    first_name: str | None
    """First name of the lead"""
    industry: str | None
    """Industry the lead's company operates in"""
    is_converted: bool | None
    """Whether the lead has been converted to an account, contact, and opportunity"""
    is_deleted: bool | None
    """Whether the lead has been moved to the Recycle Bin"""
    last_activity_date: str | None
    """Date of the last activity associated with this lead"""
    last_modified_by_id: str | None
    """ID of the user who last modified this lead"""
    last_modified_date: str | None
    """Date and time when the lead was last modified"""
    last_name: str | None
    """Last name of the lead"""
    lead_source: str | None
    """Source from which this lead originated"""
    mobile_phone: str | None
    """Mobile phone number of the lead"""
    name: str | None
    """Full name of the lead (read-only, concatenation of first and last name)"""
    number_of_employees: int | None
    """Number of employees at the lead's company"""
    owner_id: str | None
    """ID of the user who owns this lead"""
    phone: str | None
    """Phone number of the lead"""
    postal_code: str | None
    """Postal code portion of the address"""
    rating: str | None
    """Rating of the lead (e.g., Hot, Warm, Cold)"""
    state: str | None
    """State or province portion of the address"""
    status: str | None
    """Current status of the lead in the sales process"""
    street: str | None
    """Street address portion of the address"""
    title: str | None
    """Job title of the lead"""
    website: str | None
    """Website URL for the lead's company"""
    system_modstamp: str | None
    """System timestamp when the record was last modified"""


class LeadsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the lead record"""
    address: list[dict[str, Any]]
    """Complete address as a compound field"""
    city: list[str]
    """City portion of the address"""
    company: list[str]
    """Company or organization the lead works for"""
    converted_account_id: list[str]
    """ID of the account created when lead was converted"""
    converted_contact_id: list[str]
    """ID of the contact created when lead was converted"""
    converted_date: list[str]
    """Date when the lead was converted"""
    converted_opportunity_id: list[str]
    """ID of the opportunity created when lead was converted"""
    country: list[str]
    """Country portion of the address"""
    created_by_id: list[str]
    """ID of the user who created this lead"""
    created_date: list[str]
    """Date and time when the lead was created"""
    email: list[str]
    """Email address of the lead"""
    first_name: list[str]
    """First name of the lead"""
    industry: list[str]
    """Industry the lead's company operates in"""
    is_converted: list[bool]
    """Whether the lead has been converted to an account, contact, and opportunity"""
    is_deleted: list[bool]
    """Whether the lead has been moved to the Recycle Bin"""
    last_activity_date: list[str]
    """Date of the last activity associated with this lead"""
    last_modified_by_id: list[str]
    """ID of the user who last modified this lead"""
    last_modified_date: list[str]
    """Date and time when the lead was last modified"""
    last_name: list[str]
    """Last name of the lead"""
    lead_source: list[str]
    """Source from which this lead originated"""
    mobile_phone: list[str]
    """Mobile phone number of the lead"""
    name: list[str]
    """Full name of the lead (read-only, concatenation of first and last name)"""
    number_of_employees: list[int]
    """Number of employees at the lead's company"""
    owner_id: list[str]
    """ID of the user who owns this lead"""
    phone: list[str]
    """Phone number of the lead"""
    postal_code: list[str]
    """Postal code portion of the address"""
    rating: list[str]
    """Rating of the lead (e.g., Hot, Warm, Cold)"""
    state: list[str]
    """State or province portion of the address"""
    status: list[str]
    """Current status of the lead in the sales process"""
    street: list[str]
    """Street address portion of the address"""
    title: list[str]
    """Job title of the lead"""
    website: list[str]
    """Website URL for the lead's company"""
    system_modstamp: list[str]
    """System timestamp when the record was last modified"""


class LeadsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the lead record"""
    address: Any
    """Complete address as a compound field"""
    city: Any
    """City portion of the address"""
    company: Any
    """Company or organization the lead works for"""
    converted_account_id: Any
    """ID of the account created when lead was converted"""
    converted_contact_id: Any
    """ID of the contact created when lead was converted"""
    converted_date: Any
    """Date when the lead was converted"""
    converted_opportunity_id: Any
    """ID of the opportunity created when lead was converted"""
    country: Any
    """Country portion of the address"""
    created_by_id: Any
    """ID of the user who created this lead"""
    created_date: Any
    """Date and time when the lead was created"""
    email: Any
    """Email address of the lead"""
    first_name: Any
    """First name of the lead"""
    industry: Any
    """Industry the lead's company operates in"""
    is_converted: Any
    """Whether the lead has been converted to an account, contact, and opportunity"""
    is_deleted: Any
    """Whether the lead has been moved to the Recycle Bin"""
    last_activity_date: Any
    """Date of the last activity associated with this lead"""
    last_modified_by_id: Any
    """ID of the user who last modified this lead"""
    last_modified_date: Any
    """Date and time when the lead was last modified"""
    last_name: Any
    """Last name of the lead"""
    lead_source: Any
    """Source from which this lead originated"""
    mobile_phone: Any
    """Mobile phone number of the lead"""
    name: Any
    """Full name of the lead (read-only, concatenation of first and last name)"""
    number_of_employees: Any
    """Number of employees at the lead's company"""
    owner_id: Any
    """ID of the user who owns this lead"""
    phone: Any
    """Phone number of the lead"""
    postal_code: Any
    """Postal code portion of the address"""
    rating: Any
    """Rating of the lead (e.g., Hot, Warm, Cold)"""
    state: Any
    """State or province portion of the address"""
    status: Any
    """Current status of the lead in the sales process"""
    street: Any
    """Street address portion of the address"""
    title: Any
    """Job title of the lead"""
    website: Any
    """Website URL for the lead's company"""
    system_modstamp: Any
    """System timestamp when the record was last modified"""


class LeadsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the lead record"""
    address: str
    """Complete address as a compound field"""
    city: str
    """City portion of the address"""
    company: str
    """Company or organization the lead works for"""
    converted_account_id: str
    """ID of the account created when lead was converted"""
    converted_contact_id: str
    """ID of the contact created when lead was converted"""
    converted_date: str
    """Date when the lead was converted"""
    converted_opportunity_id: str
    """ID of the opportunity created when lead was converted"""
    country: str
    """Country portion of the address"""
    created_by_id: str
    """ID of the user who created this lead"""
    created_date: str
    """Date and time when the lead was created"""
    email: str
    """Email address of the lead"""
    first_name: str
    """First name of the lead"""
    industry: str
    """Industry the lead's company operates in"""
    is_converted: str
    """Whether the lead has been converted to an account, contact, and opportunity"""
    is_deleted: str
    """Whether the lead has been moved to the Recycle Bin"""
    last_activity_date: str
    """Date of the last activity associated with this lead"""
    last_modified_by_id: str
    """ID of the user who last modified this lead"""
    last_modified_date: str
    """Date and time when the lead was last modified"""
    last_name: str
    """Last name of the lead"""
    lead_source: str
    """Source from which this lead originated"""
    mobile_phone: str
    """Mobile phone number of the lead"""
    name: str
    """Full name of the lead (read-only, concatenation of first and last name)"""
    number_of_employees: str
    """Number of employees at the lead's company"""
    owner_id: str
    """ID of the user who owns this lead"""
    phone: str
    """Phone number of the lead"""
    postal_code: str
    """Postal code portion of the address"""
    rating: str
    """Rating of the lead (e.g., Hot, Warm, Cold)"""
    state: str
    """State or province portion of the address"""
    status: str
    """Current status of the lead in the sales process"""
    street: str
    """Street address portion of the address"""
    title: str
    """Job title of the lead"""
    website: str
    """Website URL for the lead's company"""
    system_modstamp: str
    """System timestamp when the record was last modified"""


class LeadsSortFilter(TypedDict, total=False):
    """Available fields for sorting leads search results."""
    id: AirbyteSortOrder
    """Unique identifier for the lead record"""
    address: AirbyteSortOrder
    """Complete address as a compound field"""
    city: AirbyteSortOrder
    """City portion of the address"""
    company: AirbyteSortOrder
    """Company or organization the lead works for"""
    converted_account_id: AirbyteSortOrder
    """ID of the account created when lead was converted"""
    converted_contact_id: AirbyteSortOrder
    """ID of the contact created when lead was converted"""
    converted_date: AirbyteSortOrder
    """Date when the lead was converted"""
    converted_opportunity_id: AirbyteSortOrder
    """ID of the opportunity created when lead was converted"""
    country: AirbyteSortOrder
    """Country portion of the address"""
    created_by_id: AirbyteSortOrder
    """ID of the user who created this lead"""
    created_date: AirbyteSortOrder
    """Date and time when the lead was created"""
    email: AirbyteSortOrder
    """Email address of the lead"""
    first_name: AirbyteSortOrder
    """First name of the lead"""
    industry: AirbyteSortOrder
    """Industry the lead's company operates in"""
    is_converted: AirbyteSortOrder
    """Whether the lead has been converted to an account, contact, and opportunity"""
    is_deleted: AirbyteSortOrder
    """Whether the lead has been moved to the Recycle Bin"""
    last_activity_date: AirbyteSortOrder
    """Date of the last activity associated with this lead"""
    last_modified_by_id: AirbyteSortOrder
    """ID of the user who last modified this lead"""
    last_modified_date: AirbyteSortOrder
    """Date and time when the lead was last modified"""
    last_name: AirbyteSortOrder
    """Last name of the lead"""
    lead_source: AirbyteSortOrder
    """Source from which this lead originated"""
    mobile_phone: AirbyteSortOrder
    """Mobile phone number of the lead"""
    name: AirbyteSortOrder
    """Full name of the lead (read-only, concatenation of first and last name)"""
    number_of_employees: AirbyteSortOrder
    """Number of employees at the lead's company"""
    owner_id: AirbyteSortOrder
    """ID of the user who owns this lead"""
    phone: AirbyteSortOrder
    """Phone number of the lead"""
    postal_code: AirbyteSortOrder
    """Postal code portion of the address"""
    rating: AirbyteSortOrder
    """Rating of the lead (e.g., Hot, Warm, Cold)"""
    state: AirbyteSortOrder
    """State or province portion of the address"""
    status: AirbyteSortOrder
    """Current status of the lead in the sales process"""
    street: AirbyteSortOrder
    """Street address portion of the address"""
    title: AirbyteSortOrder
    """Job title of the lead"""
    website: AirbyteSortOrder
    """Website URL for the lead's company"""
    system_modstamp: AirbyteSortOrder
    """System timestamp when the record was last modified"""


# Entity-specific condition types for leads
class LeadsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: LeadsSearchFilter


class LeadsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: LeadsSearchFilter


class LeadsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: LeadsSearchFilter


class LeadsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: LeadsSearchFilter


class LeadsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: LeadsSearchFilter


class LeadsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: LeadsSearchFilter


class LeadsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: LeadsStringFilter


class LeadsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: LeadsStringFilter


class LeadsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: LeadsStringFilter


class LeadsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: LeadsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
LeadsInCondition = TypedDict("LeadsInCondition", {"in": LeadsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

LeadsNotCondition = TypedDict("LeadsNotCondition", {"not": "LeadsCondition"}, total=False)
"""Negates the nested condition."""

LeadsAndCondition = TypedDict("LeadsAndCondition", {"and": "list[LeadsCondition]"}, total=False)
"""True if all nested conditions are true."""

LeadsOrCondition = TypedDict("LeadsOrCondition", {"or": "list[LeadsCondition]"}, total=False)
"""True if any nested condition is true."""

LeadsAnyCondition = TypedDict("LeadsAnyCondition", {"any": LeadsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all leads condition types
LeadsCondition = (
    LeadsEqCondition
    | LeadsNeqCondition
    | LeadsGtCondition
    | LeadsGteCondition
    | LeadsLtCondition
    | LeadsLteCondition
    | LeadsInCondition
    | LeadsLikeCondition
    | LeadsFuzzyCondition
    | LeadsKeywordCondition
    | LeadsContainsCondition
    | LeadsNotCondition
    | LeadsAndCondition
    | LeadsOrCondition
    | LeadsAnyCondition
)


class LeadsSearchQuery(TypedDict, total=False):
    """Search query for leads entity."""
    filter: LeadsCondition
    sort: list[LeadsSortFilter]


# ===== OPPORTUNITIES SEARCH TYPES =====

class OpportunitiesSearchFilter(TypedDict, total=False):
    """Available fields for filtering opportunities search queries."""
    id: str
    """Unique identifier for the opportunity record"""
    account_id: str | None
    """ID of the account associated with this opportunity"""
    amount: float | None
    """Estimated total sale amount"""
    campaign_id: str | None
    """ID of the campaign that generated this opportunity"""
    close_date: str | None
    """Expected close date for the opportunity"""
    contact_id: str | None
    """ID of the primary contact for this opportunity"""
    created_by_id: str | None
    """ID of the user who created this opportunity"""
    created_date: str | None
    """Date and time when the opportunity was created"""
    description: str | None
    """Text description of the opportunity"""
    expected_revenue: float | None
    """Expected revenue based on amount and probability"""
    forecast_category: str | None
    """Forecast category for this opportunity"""
    forecast_category_name: str | None
    """Name of the forecast category"""
    is_closed: bool | None
    """Whether the opportunity is closed"""
    is_deleted: bool | None
    """Whether the opportunity has been moved to the Recycle Bin"""
    is_won: bool | None
    """Whether the opportunity was won"""
    last_activity_date: str | None
    """Date of the last activity associated with this opportunity"""
    last_modified_by_id: str | None
    """ID of the user who last modified this opportunity"""
    last_modified_date: str | None
    """Date and time when the opportunity was last modified"""
    lead_source: str | None
    """Source from which this opportunity originated"""
    name: str | None
    """Name of the opportunity"""
    next_step: str | None
    """Description of the next step in closing the opportunity"""
    owner_id: str | None
    """ID of the user who owns this opportunity"""
    probability: float | None
    """Likelihood of closing the opportunity (percentage)"""
    stage_name: str | None
    """Current stage of the opportunity in the sales process"""
    type: str | None
    """Type of opportunity (e.g., New Business, Existing Business)"""
    system_modstamp: str | None
    """System timestamp when the record was last modified"""


class OpportunitiesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the opportunity record"""
    account_id: list[str]
    """ID of the account associated with this opportunity"""
    amount: list[float]
    """Estimated total sale amount"""
    campaign_id: list[str]
    """ID of the campaign that generated this opportunity"""
    close_date: list[str]
    """Expected close date for the opportunity"""
    contact_id: list[str]
    """ID of the primary contact for this opportunity"""
    created_by_id: list[str]
    """ID of the user who created this opportunity"""
    created_date: list[str]
    """Date and time when the opportunity was created"""
    description: list[str]
    """Text description of the opportunity"""
    expected_revenue: list[float]
    """Expected revenue based on amount and probability"""
    forecast_category: list[str]
    """Forecast category for this opportunity"""
    forecast_category_name: list[str]
    """Name of the forecast category"""
    is_closed: list[bool]
    """Whether the opportunity is closed"""
    is_deleted: list[bool]
    """Whether the opportunity has been moved to the Recycle Bin"""
    is_won: list[bool]
    """Whether the opportunity was won"""
    last_activity_date: list[str]
    """Date of the last activity associated with this opportunity"""
    last_modified_by_id: list[str]
    """ID of the user who last modified this opportunity"""
    last_modified_date: list[str]
    """Date and time when the opportunity was last modified"""
    lead_source: list[str]
    """Source from which this opportunity originated"""
    name: list[str]
    """Name of the opportunity"""
    next_step: list[str]
    """Description of the next step in closing the opportunity"""
    owner_id: list[str]
    """ID of the user who owns this opportunity"""
    probability: list[float]
    """Likelihood of closing the opportunity (percentage)"""
    stage_name: list[str]
    """Current stage of the opportunity in the sales process"""
    type: list[str]
    """Type of opportunity (e.g., New Business, Existing Business)"""
    system_modstamp: list[str]
    """System timestamp when the record was last modified"""


class OpportunitiesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the opportunity record"""
    account_id: Any
    """ID of the account associated with this opportunity"""
    amount: Any
    """Estimated total sale amount"""
    campaign_id: Any
    """ID of the campaign that generated this opportunity"""
    close_date: Any
    """Expected close date for the opportunity"""
    contact_id: Any
    """ID of the primary contact for this opportunity"""
    created_by_id: Any
    """ID of the user who created this opportunity"""
    created_date: Any
    """Date and time when the opportunity was created"""
    description: Any
    """Text description of the opportunity"""
    expected_revenue: Any
    """Expected revenue based on amount and probability"""
    forecast_category: Any
    """Forecast category for this opportunity"""
    forecast_category_name: Any
    """Name of the forecast category"""
    is_closed: Any
    """Whether the opportunity is closed"""
    is_deleted: Any
    """Whether the opportunity has been moved to the Recycle Bin"""
    is_won: Any
    """Whether the opportunity was won"""
    last_activity_date: Any
    """Date of the last activity associated with this opportunity"""
    last_modified_by_id: Any
    """ID of the user who last modified this opportunity"""
    last_modified_date: Any
    """Date and time when the opportunity was last modified"""
    lead_source: Any
    """Source from which this opportunity originated"""
    name: Any
    """Name of the opportunity"""
    next_step: Any
    """Description of the next step in closing the opportunity"""
    owner_id: Any
    """ID of the user who owns this opportunity"""
    probability: Any
    """Likelihood of closing the opportunity (percentage)"""
    stage_name: Any
    """Current stage of the opportunity in the sales process"""
    type: Any
    """Type of opportunity (e.g., New Business, Existing Business)"""
    system_modstamp: Any
    """System timestamp when the record was last modified"""


class OpportunitiesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the opportunity record"""
    account_id: str
    """ID of the account associated with this opportunity"""
    amount: str
    """Estimated total sale amount"""
    campaign_id: str
    """ID of the campaign that generated this opportunity"""
    close_date: str
    """Expected close date for the opportunity"""
    contact_id: str
    """ID of the primary contact for this opportunity"""
    created_by_id: str
    """ID of the user who created this opportunity"""
    created_date: str
    """Date and time when the opportunity was created"""
    description: str
    """Text description of the opportunity"""
    expected_revenue: str
    """Expected revenue based on amount and probability"""
    forecast_category: str
    """Forecast category for this opportunity"""
    forecast_category_name: str
    """Name of the forecast category"""
    is_closed: str
    """Whether the opportunity is closed"""
    is_deleted: str
    """Whether the opportunity has been moved to the Recycle Bin"""
    is_won: str
    """Whether the opportunity was won"""
    last_activity_date: str
    """Date of the last activity associated with this opportunity"""
    last_modified_by_id: str
    """ID of the user who last modified this opportunity"""
    last_modified_date: str
    """Date and time when the opportunity was last modified"""
    lead_source: str
    """Source from which this opportunity originated"""
    name: str
    """Name of the opportunity"""
    next_step: str
    """Description of the next step in closing the opportunity"""
    owner_id: str
    """ID of the user who owns this opportunity"""
    probability: str
    """Likelihood of closing the opportunity (percentage)"""
    stage_name: str
    """Current stage of the opportunity in the sales process"""
    type: str
    """Type of opportunity (e.g., New Business, Existing Business)"""
    system_modstamp: str
    """System timestamp when the record was last modified"""


class OpportunitiesSortFilter(TypedDict, total=False):
    """Available fields for sorting opportunities search results."""
    id: AirbyteSortOrder
    """Unique identifier for the opportunity record"""
    account_id: AirbyteSortOrder
    """ID of the account associated with this opportunity"""
    amount: AirbyteSortOrder
    """Estimated total sale amount"""
    campaign_id: AirbyteSortOrder
    """ID of the campaign that generated this opportunity"""
    close_date: AirbyteSortOrder
    """Expected close date for the opportunity"""
    contact_id: AirbyteSortOrder
    """ID of the primary contact for this opportunity"""
    created_by_id: AirbyteSortOrder
    """ID of the user who created this opportunity"""
    created_date: AirbyteSortOrder
    """Date and time when the opportunity was created"""
    description: AirbyteSortOrder
    """Text description of the opportunity"""
    expected_revenue: AirbyteSortOrder
    """Expected revenue based on amount and probability"""
    forecast_category: AirbyteSortOrder
    """Forecast category for this opportunity"""
    forecast_category_name: AirbyteSortOrder
    """Name of the forecast category"""
    is_closed: AirbyteSortOrder
    """Whether the opportunity is closed"""
    is_deleted: AirbyteSortOrder
    """Whether the opportunity has been moved to the Recycle Bin"""
    is_won: AirbyteSortOrder
    """Whether the opportunity was won"""
    last_activity_date: AirbyteSortOrder
    """Date of the last activity associated with this opportunity"""
    last_modified_by_id: AirbyteSortOrder
    """ID of the user who last modified this opportunity"""
    last_modified_date: AirbyteSortOrder
    """Date and time when the opportunity was last modified"""
    lead_source: AirbyteSortOrder
    """Source from which this opportunity originated"""
    name: AirbyteSortOrder
    """Name of the opportunity"""
    next_step: AirbyteSortOrder
    """Description of the next step in closing the opportunity"""
    owner_id: AirbyteSortOrder
    """ID of the user who owns this opportunity"""
    probability: AirbyteSortOrder
    """Likelihood of closing the opportunity (percentage)"""
    stage_name: AirbyteSortOrder
    """Current stage of the opportunity in the sales process"""
    type: AirbyteSortOrder
    """Type of opportunity (e.g., New Business, Existing Business)"""
    system_modstamp: AirbyteSortOrder
    """System timestamp when the record was last modified"""


# Entity-specific condition types for opportunities
class OpportunitiesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OpportunitiesSearchFilter


class OpportunitiesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OpportunitiesSearchFilter


class OpportunitiesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OpportunitiesSearchFilter


class OpportunitiesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OpportunitiesSearchFilter


class OpportunitiesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OpportunitiesSearchFilter


class OpportunitiesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OpportunitiesSearchFilter


class OpportunitiesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OpportunitiesStringFilter


class OpportunitiesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OpportunitiesStringFilter


class OpportunitiesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OpportunitiesStringFilter


class OpportunitiesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OpportunitiesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OpportunitiesInCondition = TypedDict("OpportunitiesInCondition", {"in": OpportunitiesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OpportunitiesNotCondition = TypedDict("OpportunitiesNotCondition", {"not": "OpportunitiesCondition"}, total=False)
"""Negates the nested condition."""

OpportunitiesAndCondition = TypedDict("OpportunitiesAndCondition", {"and": "list[OpportunitiesCondition]"}, total=False)
"""True if all nested conditions are true."""

OpportunitiesOrCondition = TypedDict("OpportunitiesOrCondition", {"or": "list[OpportunitiesCondition]"}, total=False)
"""True if any nested condition is true."""

OpportunitiesAnyCondition = TypedDict("OpportunitiesAnyCondition", {"any": OpportunitiesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all opportunities condition types
OpportunitiesCondition = (
    OpportunitiesEqCondition
    | OpportunitiesNeqCondition
    | OpportunitiesGtCondition
    | OpportunitiesGteCondition
    | OpportunitiesLtCondition
    | OpportunitiesLteCondition
    | OpportunitiesInCondition
    | OpportunitiesLikeCondition
    | OpportunitiesFuzzyCondition
    | OpportunitiesKeywordCondition
    | OpportunitiesContainsCondition
    | OpportunitiesNotCondition
    | OpportunitiesAndCondition
    | OpportunitiesOrCondition
    | OpportunitiesAnyCondition
)


class OpportunitiesSearchQuery(TypedDict, total=False):
    """Search query for opportunities entity."""
    filter: OpportunitiesCondition
    sort: list[OpportunitiesSortFilter]


# ===== TASKS SEARCH TYPES =====

class TasksSearchFilter(TypedDict, total=False):
    """Available fields for filtering tasks search queries."""
    id: str
    """Unique identifier for the task record"""
    account_id: str | None
    """ID of the account associated with this task"""
    activity_date: str | None
    """Due date for the task"""
    call_disposition: str | None
    """Result of the call, if this task represents a call"""
    call_duration_in_seconds: int | None
    """Duration of the call in seconds"""
    call_type: str | None
    """Type of call (Inbound, Outbound, Internal)"""
    completed_date_time: str | None
    """Date and time when the task was completed"""
    created_by_id: str | None
    """ID of the user who created this task"""
    created_date: str | None
    """Date and time when the task was created"""
    description: str | None
    """Text description or notes about the task"""
    is_closed: bool | None
    """Whether the task has been completed"""
    is_deleted: bool | None
    """Whether the task has been moved to the Recycle Bin"""
    is_high_priority: bool | None
    """Whether the task is marked as high priority"""
    last_modified_by_id: str | None
    """ID of the user who last modified this task"""
    last_modified_date: str | None
    """Date and time when the task was last modified"""
    owner_id: str | None
    """ID of the user who owns this task"""
    priority: str | None
    """Priority level of the task (High, Normal, Low)"""
    status: str | None
    """Current status of the task"""
    subject: str | None
    """Subject or title of the task"""
    task_subtype: str | None
    """Subtype of the task (e.g., Call, Email, Task)"""
    type: str | None
    """Type of task"""
    what_id: str | None
    """ID of the related object (Account, Opportunity, etc.)"""
    who_id: str | None
    """ID of the related person (Contact or Lead)"""
    system_modstamp: str | None
    """System timestamp when the record was last modified"""


class TasksInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the task record"""
    account_id: list[str]
    """ID of the account associated with this task"""
    activity_date: list[str]
    """Due date for the task"""
    call_disposition: list[str]
    """Result of the call, if this task represents a call"""
    call_duration_in_seconds: list[int]
    """Duration of the call in seconds"""
    call_type: list[str]
    """Type of call (Inbound, Outbound, Internal)"""
    completed_date_time: list[str]
    """Date and time when the task was completed"""
    created_by_id: list[str]
    """ID of the user who created this task"""
    created_date: list[str]
    """Date and time when the task was created"""
    description: list[str]
    """Text description or notes about the task"""
    is_closed: list[bool]
    """Whether the task has been completed"""
    is_deleted: list[bool]
    """Whether the task has been moved to the Recycle Bin"""
    is_high_priority: list[bool]
    """Whether the task is marked as high priority"""
    last_modified_by_id: list[str]
    """ID of the user who last modified this task"""
    last_modified_date: list[str]
    """Date and time when the task was last modified"""
    owner_id: list[str]
    """ID of the user who owns this task"""
    priority: list[str]
    """Priority level of the task (High, Normal, Low)"""
    status: list[str]
    """Current status of the task"""
    subject: list[str]
    """Subject or title of the task"""
    task_subtype: list[str]
    """Subtype of the task (e.g., Call, Email, Task)"""
    type: list[str]
    """Type of task"""
    what_id: list[str]
    """ID of the related object (Account, Opportunity, etc.)"""
    who_id: list[str]
    """ID of the related person (Contact or Lead)"""
    system_modstamp: list[str]
    """System timestamp when the record was last modified"""


class TasksAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the task record"""
    account_id: Any
    """ID of the account associated with this task"""
    activity_date: Any
    """Due date for the task"""
    call_disposition: Any
    """Result of the call, if this task represents a call"""
    call_duration_in_seconds: Any
    """Duration of the call in seconds"""
    call_type: Any
    """Type of call (Inbound, Outbound, Internal)"""
    completed_date_time: Any
    """Date and time when the task was completed"""
    created_by_id: Any
    """ID of the user who created this task"""
    created_date: Any
    """Date and time when the task was created"""
    description: Any
    """Text description or notes about the task"""
    is_closed: Any
    """Whether the task has been completed"""
    is_deleted: Any
    """Whether the task has been moved to the Recycle Bin"""
    is_high_priority: Any
    """Whether the task is marked as high priority"""
    last_modified_by_id: Any
    """ID of the user who last modified this task"""
    last_modified_date: Any
    """Date and time when the task was last modified"""
    owner_id: Any
    """ID of the user who owns this task"""
    priority: Any
    """Priority level of the task (High, Normal, Low)"""
    status: Any
    """Current status of the task"""
    subject: Any
    """Subject or title of the task"""
    task_subtype: Any
    """Subtype of the task (e.g., Call, Email, Task)"""
    type: Any
    """Type of task"""
    what_id: Any
    """ID of the related object (Account, Opportunity, etc.)"""
    who_id: Any
    """ID of the related person (Contact or Lead)"""
    system_modstamp: Any
    """System timestamp when the record was last modified"""


class TasksStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the task record"""
    account_id: str
    """ID of the account associated with this task"""
    activity_date: str
    """Due date for the task"""
    call_disposition: str
    """Result of the call, if this task represents a call"""
    call_duration_in_seconds: str
    """Duration of the call in seconds"""
    call_type: str
    """Type of call (Inbound, Outbound, Internal)"""
    completed_date_time: str
    """Date and time when the task was completed"""
    created_by_id: str
    """ID of the user who created this task"""
    created_date: str
    """Date and time when the task was created"""
    description: str
    """Text description or notes about the task"""
    is_closed: str
    """Whether the task has been completed"""
    is_deleted: str
    """Whether the task has been moved to the Recycle Bin"""
    is_high_priority: str
    """Whether the task is marked as high priority"""
    last_modified_by_id: str
    """ID of the user who last modified this task"""
    last_modified_date: str
    """Date and time when the task was last modified"""
    owner_id: str
    """ID of the user who owns this task"""
    priority: str
    """Priority level of the task (High, Normal, Low)"""
    status: str
    """Current status of the task"""
    subject: str
    """Subject or title of the task"""
    task_subtype: str
    """Subtype of the task (e.g., Call, Email, Task)"""
    type: str
    """Type of task"""
    what_id: str
    """ID of the related object (Account, Opportunity, etc.)"""
    who_id: str
    """ID of the related person (Contact or Lead)"""
    system_modstamp: str
    """System timestamp when the record was last modified"""


class TasksSortFilter(TypedDict, total=False):
    """Available fields for sorting tasks search results."""
    id: AirbyteSortOrder
    """Unique identifier for the task record"""
    account_id: AirbyteSortOrder
    """ID of the account associated with this task"""
    activity_date: AirbyteSortOrder
    """Due date for the task"""
    call_disposition: AirbyteSortOrder
    """Result of the call, if this task represents a call"""
    call_duration_in_seconds: AirbyteSortOrder
    """Duration of the call in seconds"""
    call_type: AirbyteSortOrder
    """Type of call (Inbound, Outbound, Internal)"""
    completed_date_time: AirbyteSortOrder
    """Date and time when the task was completed"""
    created_by_id: AirbyteSortOrder
    """ID of the user who created this task"""
    created_date: AirbyteSortOrder
    """Date and time when the task was created"""
    description: AirbyteSortOrder
    """Text description or notes about the task"""
    is_closed: AirbyteSortOrder
    """Whether the task has been completed"""
    is_deleted: AirbyteSortOrder
    """Whether the task has been moved to the Recycle Bin"""
    is_high_priority: AirbyteSortOrder
    """Whether the task is marked as high priority"""
    last_modified_by_id: AirbyteSortOrder
    """ID of the user who last modified this task"""
    last_modified_date: AirbyteSortOrder
    """Date and time when the task was last modified"""
    owner_id: AirbyteSortOrder
    """ID of the user who owns this task"""
    priority: AirbyteSortOrder
    """Priority level of the task (High, Normal, Low)"""
    status: AirbyteSortOrder
    """Current status of the task"""
    subject: AirbyteSortOrder
    """Subject or title of the task"""
    task_subtype: AirbyteSortOrder
    """Subtype of the task (e.g., Call, Email, Task)"""
    type: AirbyteSortOrder
    """Type of task"""
    what_id: AirbyteSortOrder
    """ID of the related object (Account, Opportunity, etc.)"""
    who_id: AirbyteSortOrder
    """ID of the related person (Contact or Lead)"""
    system_modstamp: AirbyteSortOrder
    """System timestamp when the record was last modified"""


# Entity-specific condition types for tasks
class TasksEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TasksSearchFilter


class TasksNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TasksSearchFilter


class TasksGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TasksSearchFilter


class TasksGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TasksSearchFilter


class TasksLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TasksSearchFilter


class TasksLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TasksSearchFilter


class TasksLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TasksStringFilter


class TasksFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TasksStringFilter


class TasksKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TasksStringFilter


class TasksContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TasksAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TasksInCondition = TypedDict("TasksInCondition", {"in": TasksInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TasksNotCondition = TypedDict("TasksNotCondition", {"not": "TasksCondition"}, total=False)
"""Negates the nested condition."""

TasksAndCondition = TypedDict("TasksAndCondition", {"and": "list[TasksCondition]"}, total=False)
"""True if all nested conditions are true."""

TasksOrCondition = TypedDict("TasksOrCondition", {"or": "list[TasksCondition]"}, total=False)
"""True if any nested condition is true."""

TasksAnyCondition = TypedDict("TasksAnyCondition", {"any": TasksAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tasks condition types
TasksCondition = (
    TasksEqCondition
    | TasksNeqCondition
    | TasksGtCondition
    | TasksGteCondition
    | TasksLtCondition
    | TasksLteCondition
    | TasksInCondition
    | TasksLikeCondition
    | TasksFuzzyCondition
    | TasksKeywordCondition
    | TasksContainsCondition
    | TasksNotCondition
    | TasksAndCondition
    | TasksOrCondition
    | TasksAnyCondition
)


class TasksSearchQuery(TypedDict, total=False):
    """Search query for tasks entity."""
    filter: TasksCondition
    sort: list[TasksSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
