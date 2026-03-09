"""
Type definitions for snapchat-marketing connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict
except ImportError:
    from typing import TypedDict  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class OrganizationsListParams(TypedDict):
    """Parameters for organizations.list operation"""
    pass

class OrganizationsGetParams(TypedDict):
    """Parameters for organizations.get operation"""
    id: str

class AdaccountsListParams(TypedDict):
    """Parameters for adaccounts.list operation"""
    organization_id: str

class AdaccountsGetParams(TypedDict):
    """Parameters for adaccounts.get operation"""
    id: str

class CampaignsListParams(TypedDict):
    """Parameters for campaigns.list operation"""
    ad_account_id: str

class CampaignsGetParams(TypedDict):
    """Parameters for campaigns.get operation"""
    id: str

class AdsquadsListParams(TypedDict):
    """Parameters for adsquads.list operation"""
    ad_account_id: str

class AdsquadsGetParams(TypedDict):
    """Parameters for adsquads.get operation"""
    id: str

class AdsListParams(TypedDict):
    """Parameters for ads.list operation"""
    ad_account_id: str

class AdsGetParams(TypedDict):
    """Parameters for ads.get operation"""
    id: str

class CreativesListParams(TypedDict):
    """Parameters for creatives.list operation"""
    ad_account_id: str

class CreativesGetParams(TypedDict):
    """Parameters for creatives.get operation"""
    id: str

class MediaListParams(TypedDict):
    """Parameters for media.list operation"""
    ad_account_id: str

class MediaGetParams(TypedDict):
    """Parameters for media.get operation"""
    id: str

class SegmentsListParams(TypedDict):
    """Parameters for segments.list operation"""
    ad_account_id: str

class SegmentsGetParams(TypedDict):
    """Parameters for segments.get operation"""
    id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ORGANIZATIONS SEARCH TYPES =====

class OrganizationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering organizations search queries."""
    accepted_term_version: str | None
    """Version of accepted terms"""
    address_line_1: str | None
    """Street address"""
    administrative_district_level_1: str | None
    """State or province"""
    configuration_settings: dict[str, Any] | None
    """Organization configuration settings"""
    contact_email: str | None
    """Contact email address"""
    contact_name: str | None
    """Contact person name"""
    contact_phone: str | None
    """Contact phone number"""
    contact_phone_optin: bool | None
    """Whether the contact opted in for phone communications"""
    country: str | None
    """Country code"""
    created_by_caller: bool | None
    """Whether the organization was created by the caller"""
    created_at: str | None
    """Creation timestamp"""
    id: str | None
    """Unique organization identifier"""
    locality: str | None
    """City or locality"""
    my_display_name: str | None
    """Display name of the authenticated user in the organization"""
    my_invited_email: str | None
    """Email used to invite the authenticated user"""
    my_member_id: str | None
    """Member ID of the authenticated user"""
    name: str | None
    """Organization name"""
    postal_code: str | None
    """Postal code"""
    roles: list[Any] | None
    """Roles of the authenticated user in this organization"""
    state: str | None
    """Organization state"""
    type_: str | None
    """Organization type"""
    updated_at: str | None
    """Last update timestamp"""


class OrganizationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    accepted_term_version: list[str]
    """Version of accepted terms"""
    address_line_1: list[str]
    """Street address"""
    administrative_district_level_1: list[str]
    """State or province"""
    configuration_settings: list[dict[str, Any]]
    """Organization configuration settings"""
    contact_email: list[str]
    """Contact email address"""
    contact_name: list[str]
    """Contact person name"""
    contact_phone: list[str]
    """Contact phone number"""
    contact_phone_optin: list[bool]
    """Whether the contact opted in for phone communications"""
    country: list[str]
    """Country code"""
    created_by_caller: list[bool]
    """Whether the organization was created by the caller"""
    created_at: list[str]
    """Creation timestamp"""
    id: list[str]
    """Unique organization identifier"""
    locality: list[str]
    """City or locality"""
    my_display_name: list[str]
    """Display name of the authenticated user in the organization"""
    my_invited_email: list[str]
    """Email used to invite the authenticated user"""
    my_member_id: list[str]
    """Member ID of the authenticated user"""
    name: list[str]
    """Organization name"""
    postal_code: list[str]
    """Postal code"""
    roles: list[list[Any]]
    """Roles of the authenticated user in this organization"""
    state: list[str]
    """Organization state"""
    type_: list[str]
    """Organization type"""
    updated_at: list[str]
    """Last update timestamp"""


class OrganizationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    accepted_term_version: Any
    """Version of accepted terms"""
    address_line_1: Any
    """Street address"""
    administrative_district_level_1: Any
    """State or province"""
    configuration_settings: Any
    """Organization configuration settings"""
    contact_email: Any
    """Contact email address"""
    contact_name: Any
    """Contact person name"""
    contact_phone: Any
    """Contact phone number"""
    contact_phone_optin: Any
    """Whether the contact opted in for phone communications"""
    country: Any
    """Country code"""
    created_by_caller: Any
    """Whether the organization was created by the caller"""
    created_at: Any
    """Creation timestamp"""
    id: Any
    """Unique organization identifier"""
    locality: Any
    """City or locality"""
    my_display_name: Any
    """Display name of the authenticated user in the organization"""
    my_invited_email: Any
    """Email used to invite the authenticated user"""
    my_member_id: Any
    """Member ID of the authenticated user"""
    name: Any
    """Organization name"""
    postal_code: Any
    """Postal code"""
    roles: Any
    """Roles of the authenticated user in this organization"""
    state: Any
    """Organization state"""
    type_: Any
    """Organization type"""
    updated_at: Any
    """Last update timestamp"""


class OrganizationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    accepted_term_version: str
    """Version of accepted terms"""
    address_line_1: str
    """Street address"""
    administrative_district_level_1: str
    """State or province"""
    configuration_settings: str
    """Organization configuration settings"""
    contact_email: str
    """Contact email address"""
    contact_name: str
    """Contact person name"""
    contact_phone: str
    """Contact phone number"""
    contact_phone_optin: str
    """Whether the contact opted in for phone communications"""
    country: str
    """Country code"""
    created_by_caller: str
    """Whether the organization was created by the caller"""
    created_at: str
    """Creation timestamp"""
    id: str
    """Unique organization identifier"""
    locality: str
    """City or locality"""
    my_display_name: str
    """Display name of the authenticated user in the organization"""
    my_invited_email: str
    """Email used to invite the authenticated user"""
    my_member_id: str
    """Member ID of the authenticated user"""
    name: str
    """Organization name"""
    postal_code: str
    """Postal code"""
    roles: str
    """Roles of the authenticated user in this organization"""
    state: str
    """Organization state"""
    type_: str
    """Organization type"""
    updated_at: str
    """Last update timestamp"""


class OrganizationsSortFilter(TypedDict, total=False):
    """Available fields for sorting organizations search results."""
    accepted_term_version: AirbyteSortOrder
    """Version of accepted terms"""
    address_line_1: AirbyteSortOrder
    """Street address"""
    administrative_district_level_1: AirbyteSortOrder
    """State or province"""
    configuration_settings: AirbyteSortOrder
    """Organization configuration settings"""
    contact_email: AirbyteSortOrder
    """Contact email address"""
    contact_name: AirbyteSortOrder
    """Contact person name"""
    contact_phone: AirbyteSortOrder
    """Contact phone number"""
    contact_phone_optin: AirbyteSortOrder
    """Whether the contact opted in for phone communications"""
    country: AirbyteSortOrder
    """Country code"""
    created_by_caller: AirbyteSortOrder
    """Whether the organization was created by the caller"""
    created_at: AirbyteSortOrder
    """Creation timestamp"""
    id: AirbyteSortOrder
    """Unique organization identifier"""
    locality: AirbyteSortOrder
    """City or locality"""
    my_display_name: AirbyteSortOrder
    """Display name of the authenticated user in the organization"""
    my_invited_email: AirbyteSortOrder
    """Email used to invite the authenticated user"""
    my_member_id: AirbyteSortOrder
    """Member ID of the authenticated user"""
    name: AirbyteSortOrder
    """Organization name"""
    postal_code: AirbyteSortOrder
    """Postal code"""
    roles: AirbyteSortOrder
    """Roles of the authenticated user in this organization"""
    state: AirbyteSortOrder
    """Organization state"""
    type_: AirbyteSortOrder
    """Organization type"""
    updated_at: AirbyteSortOrder
    """Last update timestamp"""


# Entity-specific condition types for organizations
class OrganizationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OrganizationsSearchFilter


class OrganizationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OrganizationsSearchFilter


class OrganizationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OrganizationsSearchFilter


class OrganizationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OrganizationsSearchFilter


class OrganizationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OrganizationsSearchFilter


class OrganizationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OrganizationsSearchFilter


class OrganizationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: OrganizationsStringFilter


class OrganizationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OrganizationsStringFilter


class OrganizationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OrganizationsStringFilter


class OrganizationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: OrganizationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OrganizationsInCondition = TypedDict("OrganizationsInCondition", {"in": OrganizationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OrganizationsNotCondition = TypedDict("OrganizationsNotCondition", {"not": "OrganizationsCondition"}, total=False)
"""Negates the nested condition."""

OrganizationsAndCondition = TypedDict("OrganizationsAndCondition", {"and": "list[OrganizationsCondition]"}, total=False)
"""True if all nested conditions are true."""

OrganizationsOrCondition = TypedDict("OrganizationsOrCondition", {"or": "list[OrganizationsCondition]"}, total=False)
"""True if any nested condition is true."""

OrganizationsAnyCondition = TypedDict("OrganizationsAnyCondition", {"any": OrganizationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all organizations condition types
OrganizationsCondition = (
    OrganizationsEqCondition
    | OrganizationsNeqCondition
    | OrganizationsGtCondition
    | OrganizationsGteCondition
    | OrganizationsLtCondition
    | OrganizationsLteCondition
    | OrganizationsInCondition
    | OrganizationsLikeCondition
    | OrganizationsFuzzyCondition
    | OrganizationsKeywordCondition
    | OrganizationsContainsCondition
    | OrganizationsNotCondition
    | OrganizationsAndCondition
    | OrganizationsOrCondition
    | OrganizationsAnyCondition
)


class OrganizationsSearchQuery(TypedDict, total=False):
    """Search query for organizations entity."""
    filter: OrganizationsCondition
    sort: list[OrganizationsSortFilter]


# ===== ADACCOUNTS SEARCH TYPES =====

class AdaccountsSearchFilter(TypedDict, total=False):
    """Available fields for filtering adaccounts search queries."""
    advertiser_organization_id: str | None
    """Advertiser organization ID"""
    agency_representing_client: bool | None
    """Whether the account is managed by an agency"""
    billing_center_id: str | None
    """Billing center ID"""
    billing_type: str | None
    """Billing type"""
    client_paying_invoices: bool | None
    """Whether the client pays invoices directly"""
    created_at: str | None
    """Creation timestamp"""
    currency: str | None
    """Account currency code"""
    funding_source_ids: list[Any] | None
    """Associated funding source IDs"""
    id: str | None
    """Unique ad account identifier"""
    name: str | None
    """Ad account name"""
    organization_id: str | None
    """Parent organization ID"""
    regulations: dict[str, Any] | None
    """Regulatory settings"""
    status: str | None
    """Ad account status"""
    timezone: str | None
    """Account timezone"""
    type_: str | None
    """Ad account type"""
    updated_at: str | None
    """Last update timestamp"""


class AdaccountsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    advertiser_organization_id: list[str]
    """Advertiser organization ID"""
    agency_representing_client: list[bool]
    """Whether the account is managed by an agency"""
    billing_center_id: list[str]
    """Billing center ID"""
    billing_type: list[str]
    """Billing type"""
    client_paying_invoices: list[bool]
    """Whether the client pays invoices directly"""
    created_at: list[str]
    """Creation timestamp"""
    currency: list[str]
    """Account currency code"""
    funding_source_ids: list[list[Any]]
    """Associated funding source IDs"""
    id: list[str]
    """Unique ad account identifier"""
    name: list[str]
    """Ad account name"""
    organization_id: list[str]
    """Parent organization ID"""
    regulations: list[dict[str, Any]]
    """Regulatory settings"""
    status: list[str]
    """Ad account status"""
    timezone: list[str]
    """Account timezone"""
    type_: list[str]
    """Ad account type"""
    updated_at: list[str]
    """Last update timestamp"""


class AdaccountsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    advertiser_organization_id: Any
    """Advertiser organization ID"""
    agency_representing_client: Any
    """Whether the account is managed by an agency"""
    billing_center_id: Any
    """Billing center ID"""
    billing_type: Any
    """Billing type"""
    client_paying_invoices: Any
    """Whether the client pays invoices directly"""
    created_at: Any
    """Creation timestamp"""
    currency: Any
    """Account currency code"""
    funding_source_ids: Any
    """Associated funding source IDs"""
    id: Any
    """Unique ad account identifier"""
    name: Any
    """Ad account name"""
    organization_id: Any
    """Parent organization ID"""
    regulations: Any
    """Regulatory settings"""
    status: Any
    """Ad account status"""
    timezone: Any
    """Account timezone"""
    type_: Any
    """Ad account type"""
    updated_at: Any
    """Last update timestamp"""


class AdaccountsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    advertiser_organization_id: str
    """Advertiser organization ID"""
    agency_representing_client: str
    """Whether the account is managed by an agency"""
    billing_center_id: str
    """Billing center ID"""
    billing_type: str
    """Billing type"""
    client_paying_invoices: str
    """Whether the client pays invoices directly"""
    created_at: str
    """Creation timestamp"""
    currency: str
    """Account currency code"""
    funding_source_ids: str
    """Associated funding source IDs"""
    id: str
    """Unique ad account identifier"""
    name: str
    """Ad account name"""
    organization_id: str
    """Parent organization ID"""
    regulations: str
    """Regulatory settings"""
    status: str
    """Ad account status"""
    timezone: str
    """Account timezone"""
    type_: str
    """Ad account type"""
    updated_at: str
    """Last update timestamp"""


class AdaccountsSortFilter(TypedDict, total=False):
    """Available fields for sorting adaccounts search results."""
    advertiser_organization_id: AirbyteSortOrder
    """Advertiser organization ID"""
    agency_representing_client: AirbyteSortOrder
    """Whether the account is managed by an agency"""
    billing_center_id: AirbyteSortOrder
    """Billing center ID"""
    billing_type: AirbyteSortOrder
    """Billing type"""
    client_paying_invoices: AirbyteSortOrder
    """Whether the client pays invoices directly"""
    created_at: AirbyteSortOrder
    """Creation timestamp"""
    currency: AirbyteSortOrder
    """Account currency code"""
    funding_source_ids: AirbyteSortOrder
    """Associated funding source IDs"""
    id: AirbyteSortOrder
    """Unique ad account identifier"""
    name: AirbyteSortOrder
    """Ad account name"""
    organization_id: AirbyteSortOrder
    """Parent organization ID"""
    regulations: AirbyteSortOrder
    """Regulatory settings"""
    status: AirbyteSortOrder
    """Ad account status"""
    timezone: AirbyteSortOrder
    """Account timezone"""
    type_: AirbyteSortOrder
    """Ad account type"""
    updated_at: AirbyteSortOrder
    """Last update timestamp"""


# Entity-specific condition types for adaccounts
class AdaccountsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdaccountsSearchFilter


class AdaccountsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdaccountsSearchFilter


class AdaccountsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdaccountsSearchFilter


class AdaccountsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdaccountsSearchFilter


class AdaccountsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdaccountsSearchFilter


class AdaccountsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdaccountsSearchFilter


class AdaccountsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdaccountsStringFilter


class AdaccountsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdaccountsStringFilter


class AdaccountsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdaccountsStringFilter


class AdaccountsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdaccountsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdaccountsInCondition = TypedDict("AdaccountsInCondition", {"in": AdaccountsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdaccountsNotCondition = TypedDict("AdaccountsNotCondition", {"not": "AdaccountsCondition"}, total=False)
"""Negates the nested condition."""

AdaccountsAndCondition = TypedDict("AdaccountsAndCondition", {"and": "list[AdaccountsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdaccountsOrCondition = TypedDict("AdaccountsOrCondition", {"or": "list[AdaccountsCondition]"}, total=False)
"""True if any nested condition is true."""

AdaccountsAnyCondition = TypedDict("AdaccountsAnyCondition", {"any": AdaccountsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all adaccounts condition types
AdaccountsCondition = (
    AdaccountsEqCondition
    | AdaccountsNeqCondition
    | AdaccountsGtCondition
    | AdaccountsGteCondition
    | AdaccountsLtCondition
    | AdaccountsLteCondition
    | AdaccountsInCondition
    | AdaccountsLikeCondition
    | AdaccountsFuzzyCondition
    | AdaccountsKeywordCondition
    | AdaccountsContainsCondition
    | AdaccountsNotCondition
    | AdaccountsAndCondition
    | AdaccountsOrCondition
    | AdaccountsAnyCondition
)


class AdaccountsSearchQuery(TypedDict, total=False):
    """Search query for adaccounts entity."""
    filter: AdaccountsCondition
    sort: list[AdaccountsSortFilter]


# ===== CAMPAIGNS SEARCH TYPES =====

class CampaignsSearchFilter(TypedDict, total=False):
    """Available fields for filtering campaigns search queries."""
    ad_account_id: str | None
    """Parent ad account ID"""
    buy_model: str | None
    """Buy model type"""
    created_at: str | None
    """Creation timestamp"""
    creation_state: str | None
    """Creation state"""
    delivery_status: list[Any] | None
    """Delivery status messages"""
    id: str | None
    """Unique campaign identifier"""
    name: str | None
    """Campaign name"""
    objective: str | None
    """Campaign objective"""
    start_time: str | None
    """Campaign start time"""
    status: str | None
    """Campaign status"""
    updated_at: str | None
    """Last update timestamp"""


class CampaignsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_account_id: list[str]
    """Parent ad account ID"""
    buy_model: list[str]
    """Buy model type"""
    created_at: list[str]
    """Creation timestamp"""
    creation_state: list[str]
    """Creation state"""
    delivery_status: list[list[Any]]
    """Delivery status messages"""
    id: list[str]
    """Unique campaign identifier"""
    name: list[str]
    """Campaign name"""
    objective: list[str]
    """Campaign objective"""
    start_time: list[str]
    """Campaign start time"""
    status: list[str]
    """Campaign status"""
    updated_at: list[str]
    """Last update timestamp"""


class CampaignsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_account_id: Any
    """Parent ad account ID"""
    buy_model: Any
    """Buy model type"""
    created_at: Any
    """Creation timestamp"""
    creation_state: Any
    """Creation state"""
    delivery_status: Any
    """Delivery status messages"""
    id: Any
    """Unique campaign identifier"""
    name: Any
    """Campaign name"""
    objective: Any
    """Campaign objective"""
    start_time: Any
    """Campaign start time"""
    status: Any
    """Campaign status"""
    updated_at: Any
    """Last update timestamp"""


class CampaignsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_account_id: str
    """Parent ad account ID"""
    buy_model: str
    """Buy model type"""
    created_at: str
    """Creation timestamp"""
    creation_state: str
    """Creation state"""
    delivery_status: str
    """Delivery status messages"""
    id: str
    """Unique campaign identifier"""
    name: str
    """Campaign name"""
    objective: str
    """Campaign objective"""
    start_time: str
    """Campaign start time"""
    status: str
    """Campaign status"""
    updated_at: str
    """Last update timestamp"""


class CampaignsSortFilter(TypedDict, total=False):
    """Available fields for sorting campaigns search results."""
    ad_account_id: AirbyteSortOrder
    """Parent ad account ID"""
    buy_model: AirbyteSortOrder
    """Buy model type"""
    created_at: AirbyteSortOrder
    """Creation timestamp"""
    creation_state: AirbyteSortOrder
    """Creation state"""
    delivery_status: AirbyteSortOrder
    """Delivery status messages"""
    id: AirbyteSortOrder
    """Unique campaign identifier"""
    name: AirbyteSortOrder
    """Campaign name"""
    objective: AirbyteSortOrder
    """Campaign objective"""
    start_time: AirbyteSortOrder
    """Campaign start time"""
    status: AirbyteSortOrder
    """Campaign status"""
    updated_at: AirbyteSortOrder
    """Last update timestamp"""


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


# ===== ADSQUADS SEARCH TYPES =====

class AdsquadsSearchFilter(TypedDict, total=False):
    """Available fields for filtering adsquads search queries."""
    auto_bid: bool | None
    """Whether auto bidding is enabled"""
    bid_strategy: str | None
    """Bid strategy"""
    billing_event: str | None
    """Billing event type"""
    campaign_id: str | None
    """Parent campaign ID"""
    child_ad_type: str | None
    """Child ad type"""
    created_at: str | None
    """Creation timestamp"""
    creation_state: str | None
    """Creation state"""
    daily_budget_micro: int | None
    """Daily budget in micro-currency"""
    delivery_constraint: str | None
    """Delivery constraint"""
    delivery_properties_version: int | None
    """Delivery properties version"""
    delivery_status: list[Any] | None
    """Delivery status messages"""
    end_time: str | None
    """Ad squad end time"""
    event_sources: dict[str, Any] | None
    """Event sources configuration"""
    forced_view_setting: str | None
    """Forced view setting"""
    id: str | None
    """Unique ad squad identifier"""
    lifetime_budget_micro: int | None
    """Lifetime budget in micro-currency"""
    name: str | None
    """Ad squad name"""
    optimization_goal: str | None
    """Optimization goal"""
    pacing_type: str | None
    """Pacing type"""
    placement: str | None
    """Placement type"""
    skadnetwork_properties: dict[str, Any] | None
    """SKAdNetwork properties"""
    start_time: str | None
    """Ad squad start time"""
    status: str | None
    """Ad squad status"""
    target_bid: bool | None
    """Whether target bid is enabled"""
    targeting: dict[str, Any] | None
    """Targeting specification"""
    targeting_reach_status: str | None
    """Targeting reach status"""
    type_: str | None
    """Ad squad type"""
    updated_at: str | None
    """Last update timestamp"""


class AdsquadsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    auto_bid: list[bool]
    """Whether auto bidding is enabled"""
    bid_strategy: list[str]
    """Bid strategy"""
    billing_event: list[str]
    """Billing event type"""
    campaign_id: list[str]
    """Parent campaign ID"""
    child_ad_type: list[str]
    """Child ad type"""
    created_at: list[str]
    """Creation timestamp"""
    creation_state: list[str]
    """Creation state"""
    daily_budget_micro: list[int]
    """Daily budget in micro-currency"""
    delivery_constraint: list[str]
    """Delivery constraint"""
    delivery_properties_version: list[int]
    """Delivery properties version"""
    delivery_status: list[list[Any]]
    """Delivery status messages"""
    end_time: list[str]
    """Ad squad end time"""
    event_sources: list[dict[str, Any]]
    """Event sources configuration"""
    forced_view_setting: list[str]
    """Forced view setting"""
    id: list[str]
    """Unique ad squad identifier"""
    lifetime_budget_micro: list[int]
    """Lifetime budget in micro-currency"""
    name: list[str]
    """Ad squad name"""
    optimization_goal: list[str]
    """Optimization goal"""
    pacing_type: list[str]
    """Pacing type"""
    placement: list[str]
    """Placement type"""
    skadnetwork_properties: list[dict[str, Any]]
    """SKAdNetwork properties"""
    start_time: list[str]
    """Ad squad start time"""
    status: list[str]
    """Ad squad status"""
    target_bid: list[bool]
    """Whether target bid is enabled"""
    targeting: list[dict[str, Any]]
    """Targeting specification"""
    targeting_reach_status: list[str]
    """Targeting reach status"""
    type_: list[str]
    """Ad squad type"""
    updated_at: list[str]
    """Last update timestamp"""


class AdsquadsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    auto_bid: Any
    """Whether auto bidding is enabled"""
    bid_strategy: Any
    """Bid strategy"""
    billing_event: Any
    """Billing event type"""
    campaign_id: Any
    """Parent campaign ID"""
    child_ad_type: Any
    """Child ad type"""
    created_at: Any
    """Creation timestamp"""
    creation_state: Any
    """Creation state"""
    daily_budget_micro: Any
    """Daily budget in micro-currency"""
    delivery_constraint: Any
    """Delivery constraint"""
    delivery_properties_version: Any
    """Delivery properties version"""
    delivery_status: Any
    """Delivery status messages"""
    end_time: Any
    """Ad squad end time"""
    event_sources: Any
    """Event sources configuration"""
    forced_view_setting: Any
    """Forced view setting"""
    id: Any
    """Unique ad squad identifier"""
    lifetime_budget_micro: Any
    """Lifetime budget in micro-currency"""
    name: Any
    """Ad squad name"""
    optimization_goal: Any
    """Optimization goal"""
    pacing_type: Any
    """Pacing type"""
    placement: Any
    """Placement type"""
    skadnetwork_properties: Any
    """SKAdNetwork properties"""
    start_time: Any
    """Ad squad start time"""
    status: Any
    """Ad squad status"""
    target_bid: Any
    """Whether target bid is enabled"""
    targeting: Any
    """Targeting specification"""
    targeting_reach_status: Any
    """Targeting reach status"""
    type_: Any
    """Ad squad type"""
    updated_at: Any
    """Last update timestamp"""


class AdsquadsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    auto_bid: str
    """Whether auto bidding is enabled"""
    bid_strategy: str
    """Bid strategy"""
    billing_event: str
    """Billing event type"""
    campaign_id: str
    """Parent campaign ID"""
    child_ad_type: str
    """Child ad type"""
    created_at: str
    """Creation timestamp"""
    creation_state: str
    """Creation state"""
    daily_budget_micro: str
    """Daily budget in micro-currency"""
    delivery_constraint: str
    """Delivery constraint"""
    delivery_properties_version: str
    """Delivery properties version"""
    delivery_status: str
    """Delivery status messages"""
    end_time: str
    """Ad squad end time"""
    event_sources: str
    """Event sources configuration"""
    forced_view_setting: str
    """Forced view setting"""
    id: str
    """Unique ad squad identifier"""
    lifetime_budget_micro: str
    """Lifetime budget in micro-currency"""
    name: str
    """Ad squad name"""
    optimization_goal: str
    """Optimization goal"""
    pacing_type: str
    """Pacing type"""
    placement: str
    """Placement type"""
    skadnetwork_properties: str
    """SKAdNetwork properties"""
    start_time: str
    """Ad squad start time"""
    status: str
    """Ad squad status"""
    target_bid: str
    """Whether target bid is enabled"""
    targeting: str
    """Targeting specification"""
    targeting_reach_status: str
    """Targeting reach status"""
    type_: str
    """Ad squad type"""
    updated_at: str
    """Last update timestamp"""


class AdsquadsSortFilter(TypedDict, total=False):
    """Available fields for sorting adsquads search results."""
    auto_bid: AirbyteSortOrder
    """Whether auto bidding is enabled"""
    bid_strategy: AirbyteSortOrder
    """Bid strategy"""
    billing_event: AirbyteSortOrder
    """Billing event type"""
    campaign_id: AirbyteSortOrder
    """Parent campaign ID"""
    child_ad_type: AirbyteSortOrder
    """Child ad type"""
    created_at: AirbyteSortOrder
    """Creation timestamp"""
    creation_state: AirbyteSortOrder
    """Creation state"""
    daily_budget_micro: AirbyteSortOrder
    """Daily budget in micro-currency"""
    delivery_constraint: AirbyteSortOrder
    """Delivery constraint"""
    delivery_properties_version: AirbyteSortOrder
    """Delivery properties version"""
    delivery_status: AirbyteSortOrder
    """Delivery status messages"""
    end_time: AirbyteSortOrder
    """Ad squad end time"""
    event_sources: AirbyteSortOrder
    """Event sources configuration"""
    forced_view_setting: AirbyteSortOrder
    """Forced view setting"""
    id: AirbyteSortOrder
    """Unique ad squad identifier"""
    lifetime_budget_micro: AirbyteSortOrder
    """Lifetime budget in micro-currency"""
    name: AirbyteSortOrder
    """Ad squad name"""
    optimization_goal: AirbyteSortOrder
    """Optimization goal"""
    pacing_type: AirbyteSortOrder
    """Pacing type"""
    placement: AirbyteSortOrder
    """Placement type"""
    skadnetwork_properties: AirbyteSortOrder
    """SKAdNetwork properties"""
    start_time: AirbyteSortOrder
    """Ad squad start time"""
    status: AirbyteSortOrder
    """Ad squad status"""
    target_bid: AirbyteSortOrder
    """Whether target bid is enabled"""
    targeting: AirbyteSortOrder
    """Targeting specification"""
    targeting_reach_status: AirbyteSortOrder
    """Targeting reach status"""
    type_: AirbyteSortOrder
    """Ad squad type"""
    updated_at: AirbyteSortOrder
    """Last update timestamp"""


# Entity-specific condition types for adsquads
class AdsquadsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AdsquadsSearchFilter


class AdsquadsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AdsquadsSearchFilter


class AdsquadsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AdsquadsSearchFilter


class AdsquadsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AdsquadsSearchFilter


class AdsquadsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AdsquadsSearchFilter


class AdsquadsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AdsquadsSearchFilter


class AdsquadsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AdsquadsStringFilter


class AdsquadsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AdsquadsStringFilter


class AdsquadsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AdsquadsStringFilter


class AdsquadsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AdsquadsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AdsquadsInCondition = TypedDict("AdsquadsInCondition", {"in": AdsquadsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AdsquadsNotCondition = TypedDict("AdsquadsNotCondition", {"not": "AdsquadsCondition"}, total=False)
"""Negates the nested condition."""

AdsquadsAndCondition = TypedDict("AdsquadsAndCondition", {"and": "list[AdsquadsCondition]"}, total=False)
"""True if all nested conditions are true."""

AdsquadsOrCondition = TypedDict("AdsquadsOrCondition", {"or": "list[AdsquadsCondition]"}, total=False)
"""True if any nested condition is true."""

AdsquadsAnyCondition = TypedDict("AdsquadsAnyCondition", {"any": AdsquadsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all adsquads condition types
AdsquadsCondition = (
    AdsquadsEqCondition
    | AdsquadsNeqCondition
    | AdsquadsGtCondition
    | AdsquadsGteCondition
    | AdsquadsLtCondition
    | AdsquadsLteCondition
    | AdsquadsInCondition
    | AdsquadsLikeCondition
    | AdsquadsFuzzyCondition
    | AdsquadsKeywordCondition
    | AdsquadsContainsCondition
    | AdsquadsNotCondition
    | AdsquadsAndCondition
    | AdsquadsOrCondition
    | AdsquadsAnyCondition
)


class AdsquadsSearchQuery(TypedDict, total=False):
    """Search query for adsquads entity."""
    filter: AdsquadsCondition
    sort: list[AdsquadsSortFilter]


# ===== ADS SEARCH TYPES =====

class AdsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ads search queries."""
    ad_squad_id: str | None
    """Parent ad squad ID"""
    created_at: str | None
    """Creation timestamp"""
    creative_id: str | None
    """Associated creative ID"""
    delivery_status: list[Any] | None
    """Delivery status messages"""
    id: str | None
    """Unique ad identifier"""
    name: str | None
    """Ad name"""
    render_type: str | None
    """Render type"""
    review_status: str | None
    """Review status"""
    review_status_reasons: list[Any] | None
    """Reasons for review status"""
    status: str | None
    """Ad status"""
    type_: str | None
    """Ad type"""
    updated_at: str | None
    """Last update timestamp"""


class AdsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_squad_id: list[str]
    """Parent ad squad ID"""
    created_at: list[str]
    """Creation timestamp"""
    creative_id: list[str]
    """Associated creative ID"""
    delivery_status: list[list[Any]]
    """Delivery status messages"""
    id: list[str]
    """Unique ad identifier"""
    name: list[str]
    """Ad name"""
    render_type: list[str]
    """Render type"""
    review_status: list[str]
    """Review status"""
    review_status_reasons: list[list[Any]]
    """Reasons for review status"""
    status: list[str]
    """Ad status"""
    type_: list[str]
    """Ad type"""
    updated_at: list[str]
    """Last update timestamp"""


class AdsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_squad_id: Any
    """Parent ad squad ID"""
    created_at: Any
    """Creation timestamp"""
    creative_id: Any
    """Associated creative ID"""
    delivery_status: Any
    """Delivery status messages"""
    id: Any
    """Unique ad identifier"""
    name: Any
    """Ad name"""
    render_type: Any
    """Render type"""
    review_status: Any
    """Review status"""
    review_status_reasons: Any
    """Reasons for review status"""
    status: Any
    """Ad status"""
    type_: Any
    """Ad type"""
    updated_at: Any
    """Last update timestamp"""


class AdsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_squad_id: str
    """Parent ad squad ID"""
    created_at: str
    """Creation timestamp"""
    creative_id: str
    """Associated creative ID"""
    delivery_status: str
    """Delivery status messages"""
    id: str
    """Unique ad identifier"""
    name: str
    """Ad name"""
    render_type: str
    """Render type"""
    review_status: str
    """Review status"""
    review_status_reasons: str
    """Reasons for review status"""
    status: str
    """Ad status"""
    type_: str
    """Ad type"""
    updated_at: str
    """Last update timestamp"""


class AdsSortFilter(TypedDict, total=False):
    """Available fields for sorting ads search results."""
    ad_squad_id: AirbyteSortOrder
    """Parent ad squad ID"""
    created_at: AirbyteSortOrder
    """Creation timestamp"""
    creative_id: AirbyteSortOrder
    """Associated creative ID"""
    delivery_status: AirbyteSortOrder
    """Delivery status messages"""
    id: AirbyteSortOrder
    """Unique ad identifier"""
    name: AirbyteSortOrder
    """Ad name"""
    render_type: AirbyteSortOrder
    """Render type"""
    review_status: AirbyteSortOrder
    """Review status"""
    review_status_reasons: AirbyteSortOrder
    """Reasons for review status"""
    status: AirbyteSortOrder
    """Ad status"""
    type_: AirbyteSortOrder
    """Ad type"""
    updated_at: AirbyteSortOrder
    """Last update timestamp"""


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


# ===== CREATIVES SEARCH TYPES =====

class CreativesSearchFilter(TypedDict, total=False):
    """Available fields for filtering creatives search queries."""
    ad_account_id: str | None
    """Parent ad account ID"""
    ad_product: str | None
    """Ad product type"""
    ad_to_place_properties: dict[str, Any] | None
    """Ad-to-place properties"""
    brand_name: str | None
    """Brand name displayed in the creative"""
    call_to_action: str | None
    """Call to action text"""
    created_at: str | None
    """Creation timestamp"""
    forced_view_eligibility: str | None
    """Forced view eligibility status"""
    headline: str | None
    """Creative headline"""
    id: str | None
    """Unique creative identifier"""
    name: str | None
    """Creative name"""
    packaging_status: str | None
    """Packaging status"""
    render_type: str | None
    """Render type"""
    review_status: str | None
    """Review status"""
    review_status_details: str | None
    """Details about the review status"""
    shareable: bool | None
    """Whether the creative is shareable"""
    top_snap_crop_position: str | None
    """Top snap crop position"""
    top_snap_media_id: str | None
    """Top snap media ID"""
    type_: str | None
    """Creative type"""
    updated_at: str | None
    """Last update timestamp"""
    web_view_properties: dict[str, Any] | None
    """Web view properties"""


class CreativesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_account_id: list[str]
    """Parent ad account ID"""
    ad_product: list[str]
    """Ad product type"""
    ad_to_place_properties: list[dict[str, Any]]
    """Ad-to-place properties"""
    brand_name: list[str]
    """Brand name displayed in the creative"""
    call_to_action: list[str]
    """Call to action text"""
    created_at: list[str]
    """Creation timestamp"""
    forced_view_eligibility: list[str]
    """Forced view eligibility status"""
    headline: list[str]
    """Creative headline"""
    id: list[str]
    """Unique creative identifier"""
    name: list[str]
    """Creative name"""
    packaging_status: list[str]
    """Packaging status"""
    render_type: list[str]
    """Render type"""
    review_status: list[str]
    """Review status"""
    review_status_details: list[str]
    """Details about the review status"""
    shareable: list[bool]
    """Whether the creative is shareable"""
    top_snap_crop_position: list[str]
    """Top snap crop position"""
    top_snap_media_id: list[str]
    """Top snap media ID"""
    type_: list[str]
    """Creative type"""
    updated_at: list[str]
    """Last update timestamp"""
    web_view_properties: list[dict[str, Any]]
    """Web view properties"""


class CreativesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_account_id: Any
    """Parent ad account ID"""
    ad_product: Any
    """Ad product type"""
    ad_to_place_properties: Any
    """Ad-to-place properties"""
    brand_name: Any
    """Brand name displayed in the creative"""
    call_to_action: Any
    """Call to action text"""
    created_at: Any
    """Creation timestamp"""
    forced_view_eligibility: Any
    """Forced view eligibility status"""
    headline: Any
    """Creative headline"""
    id: Any
    """Unique creative identifier"""
    name: Any
    """Creative name"""
    packaging_status: Any
    """Packaging status"""
    render_type: Any
    """Render type"""
    review_status: Any
    """Review status"""
    review_status_details: Any
    """Details about the review status"""
    shareable: Any
    """Whether the creative is shareable"""
    top_snap_crop_position: Any
    """Top snap crop position"""
    top_snap_media_id: Any
    """Top snap media ID"""
    type_: Any
    """Creative type"""
    updated_at: Any
    """Last update timestamp"""
    web_view_properties: Any
    """Web view properties"""


class CreativesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_account_id: str
    """Parent ad account ID"""
    ad_product: str
    """Ad product type"""
    ad_to_place_properties: str
    """Ad-to-place properties"""
    brand_name: str
    """Brand name displayed in the creative"""
    call_to_action: str
    """Call to action text"""
    created_at: str
    """Creation timestamp"""
    forced_view_eligibility: str
    """Forced view eligibility status"""
    headline: str
    """Creative headline"""
    id: str
    """Unique creative identifier"""
    name: str
    """Creative name"""
    packaging_status: str
    """Packaging status"""
    render_type: str
    """Render type"""
    review_status: str
    """Review status"""
    review_status_details: str
    """Details about the review status"""
    shareable: str
    """Whether the creative is shareable"""
    top_snap_crop_position: str
    """Top snap crop position"""
    top_snap_media_id: str
    """Top snap media ID"""
    type_: str
    """Creative type"""
    updated_at: str
    """Last update timestamp"""
    web_view_properties: str
    """Web view properties"""


class CreativesSortFilter(TypedDict, total=False):
    """Available fields for sorting creatives search results."""
    ad_account_id: AirbyteSortOrder
    """Parent ad account ID"""
    ad_product: AirbyteSortOrder
    """Ad product type"""
    ad_to_place_properties: AirbyteSortOrder
    """Ad-to-place properties"""
    brand_name: AirbyteSortOrder
    """Brand name displayed in the creative"""
    call_to_action: AirbyteSortOrder
    """Call to action text"""
    created_at: AirbyteSortOrder
    """Creation timestamp"""
    forced_view_eligibility: AirbyteSortOrder
    """Forced view eligibility status"""
    headline: AirbyteSortOrder
    """Creative headline"""
    id: AirbyteSortOrder
    """Unique creative identifier"""
    name: AirbyteSortOrder
    """Creative name"""
    packaging_status: AirbyteSortOrder
    """Packaging status"""
    render_type: AirbyteSortOrder
    """Render type"""
    review_status: AirbyteSortOrder
    """Review status"""
    review_status_details: AirbyteSortOrder
    """Details about the review status"""
    shareable: AirbyteSortOrder
    """Whether the creative is shareable"""
    top_snap_crop_position: AirbyteSortOrder
    """Top snap crop position"""
    top_snap_media_id: AirbyteSortOrder
    """Top snap media ID"""
    type_: AirbyteSortOrder
    """Creative type"""
    updated_at: AirbyteSortOrder
    """Last update timestamp"""
    web_view_properties: AirbyteSortOrder
    """Web view properties"""


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


# ===== MEDIA SEARCH TYPES =====

class MediaSearchFilter(TypedDict, total=False):
    """Available fields for filtering media search queries."""
    ad_account_id: str | None
    """Parent ad account ID"""
    created_at: str | None
    """Creation timestamp"""
    download_link: str | None
    """Download URL for the media"""
    duration_in_seconds: float | None
    """Duration in seconds for video media"""
    file_name: str | None
    """Original file name"""
    file_size_in_bytes: int | None
    """File size in bytes"""
    hash: str | None
    """Media file hash"""
    id: str | None
    """Unique media identifier"""
    image_metadata: dict[str, Any] | None
    """Image-specific metadata"""
    is_demo_media: bool | None
    """Whether this is demo media"""
    media_status: str | None
    """Media processing status"""
    media_usages: list[Any] | None
    """Where the media is used"""
    name: str | None
    """Media name"""
    type_: str | None
    """Media type"""
    updated_at: str | None
    """Last update timestamp"""
    video_metadata: dict[str, Any] | None
    """Video-specific metadata"""
    visibility: str | None
    """Media visibility setting"""


class MediaInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_account_id: list[str]
    """Parent ad account ID"""
    created_at: list[str]
    """Creation timestamp"""
    download_link: list[str]
    """Download URL for the media"""
    duration_in_seconds: list[float]
    """Duration in seconds for video media"""
    file_name: list[str]
    """Original file name"""
    file_size_in_bytes: list[int]
    """File size in bytes"""
    hash: list[str]
    """Media file hash"""
    id: list[str]
    """Unique media identifier"""
    image_metadata: list[dict[str, Any]]
    """Image-specific metadata"""
    is_demo_media: list[bool]
    """Whether this is demo media"""
    media_status: list[str]
    """Media processing status"""
    media_usages: list[list[Any]]
    """Where the media is used"""
    name: list[str]
    """Media name"""
    type_: list[str]
    """Media type"""
    updated_at: list[str]
    """Last update timestamp"""
    video_metadata: list[dict[str, Any]]
    """Video-specific metadata"""
    visibility: list[str]
    """Media visibility setting"""


class MediaAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_account_id: Any
    """Parent ad account ID"""
    created_at: Any
    """Creation timestamp"""
    download_link: Any
    """Download URL for the media"""
    duration_in_seconds: Any
    """Duration in seconds for video media"""
    file_name: Any
    """Original file name"""
    file_size_in_bytes: Any
    """File size in bytes"""
    hash: Any
    """Media file hash"""
    id: Any
    """Unique media identifier"""
    image_metadata: Any
    """Image-specific metadata"""
    is_demo_media: Any
    """Whether this is demo media"""
    media_status: Any
    """Media processing status"""
    media_usages: Any
    """Where the media is used"""
    name: Any
    """Media name"""
    type_: Any
    """Media type"""
    updated_at: Any
    """Last update timestamp"""
    video_metadata: Any
    """Video-specific metadata"""
    visibility: Any
    """Media visibility setting"""


class MediaStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_account_id: str
    """Parent ad account ID"""
    created_at: str
    """Creation timestamp"""
    download_link: str
    """Download URL for the media"""
    duration_in_seconds: str
    """Duration in seconds for video media"""
    file_name: str
    """Original file name"""
    file_size_in_bytes: str
    """File size in bytes"""
    hash: str
    """Media file hash"""
    id: str
    """Unique media identifier"""
    image_metadata: str
    """Image-specific metadata"""
    is_demo_media: str
    """Whether this is demo media"""
    media_status: str
    """Media processing status"""
    media_usages: str
    """Where the media is used"""
    name: str
    """Media name"""
    type_: str
    """Media type"""
    updated_at: str
    """Last update timestamp"""
    video_metadata: str
    """Video-specific metadata"""
    visibility: str
    """Media visibility setting"""


class MediaSortFilter(TypedDict, total=False):
    """Available fields for sorting media search results."""
    ad_account_id: AirbyteSortOrder
    """Parent ad account ID"""
    created_at: AirbyteSortOrder
    """Creation timestamp"""
    download_link: AirbyteSortOrder
    """Download URL for the media"""
    duration_in_seconds: AirbyteSortOrder
    """Duration in seconds for video media"""
    file_name: AirbyteSortOrder
    """Original file name"""
    file_size_in_bytes: AirbyteSortOrder
    """File size in bytes"""
    hash: AirbyteSortOrder
    """Media file hash"""
    id: AirbyteSortOrder
    """Unique media identifier"""
    image_metadata: AirbyteSortOrder
    """Image-specific metadata"""
    is_demo_media: AirbyteSortOrder
    """Whether this is demo media"""
    media_status: AirbyteSortOrder
    """Media processing status"""
    media_usages: AirbyteSortOrder
    """Where the media is used"""
    name: AirbyteSortOrder
    """Media name"""
    type_: AirbyteSortOrder
    """Media type"""
    updated_at: AirbyteSortOrder
    """Last update timestamp"""
    video_metadata: AirbyteSortOrder
    """Video-specific metadata"""
    visibility: AirbyteSortOrder
    """Media visibility setting"""


# Entity-specific condition types for media
class MediaEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MediaSearchFilter


class MediaNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MediaSearchFilter


class MediaGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MediaSearchFilter


class MediaGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MediaSearchFilter


class MediaLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MediaSearchFilter


class MediaLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MediaSearchFilter


class MediaLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MediaStringFilter


class MediaFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MediaStringFilter


class MediaKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MediaStringFilter


class MediaContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MediaAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MediaInCondition = TypedDict("MediaInCondition", {"in": MediaInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MediaNotCondition = TypedDict("MediaNotCondition", {"not": "MediaCondition"}, total=False)
"""Negates the nested condition."""

MediaAndCondition = TypedDict("MediaAndCondition", {"and": "list[MediaCondition]"}, total=False)
"""True if all nested conditions are true."""

MediaOrCondition = TypedDict("MediaOrCondition", {"or": "list[MediaCondition]"}, total=False)
"""True if any nested condition is true."""

MediaAnyCondition = TypedDict("MediaAnyCondition", {"any": MediaAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all media condition types
MediaCondition = (
    MediaEqCondition
    | MediaNeqCondition
    | MediaGtCondition
    | MediaGteCondition
    | MediaLtCondition
    | MediaLteCondition
    | MediaInCondition
    | MediaLikeCondition
    | MediaFuzzyCondition
    | MediaKeywordCondition
    | MediaContainsCondition
    | MediaNotCondition
    | MediaAndCondition
    | MediaOrCondition
    | MediaAnyCondition
)


class MediaSearchQuery(TypedDict, total=False):
    """Search query for media entity."""
    filter: MediaCondition
    sort: list[MediaSortFilter]


# ===== SEGMENTS SEARCH TYPES =====

class SegmentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering segments search queries."""
    ad_account_id: str | None
    """Parent ad account ID"""
    approximate_number_users: int | None
    """Approximate number of users in the segment"""
    created_at: str | None
    """Creation timestamp"""
    description: str | None
    """Segment description"""
    id: str | None
    """Unique segment identifier"""
    name: str | None
    """Segment name"""
    organization_id: str | None
    """Parent organization ID"""
    retention_in_days: int | None
    """Data retention period in days"""
    source_type: str | None
    """Segment source type"""
    status: str | None
    """Segment status"""
    targetable_status: str | None
    """Whether the segment is targetable"""
    updated_at: str | None
    """Last update timestamp"""
    upload_status: str | None
    """Upload processing status"""
    visible_to: list[Any] | None
    """Visibility settings"""


class SegmentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    ad_account_id: list[str]
    """Parent ad account ID"""
    approximate_number_users: list[int]
    """Approximate number of users in the segment"""
    created_at: list[str]
    """Creation timestamp"""
    description: list[str]
    """Segment description"""
    id: list[str]
    """Unique segment identifier"""
    name: list[str]
    """Segment name"""
    organization_id: list[str]
    """Parent organization ID"""
    retention_in_days: list[int]
    """Data retention period in days"""
    source_type: list[str]
    """Segment source type"""
    status: list[str]
    """Segment status"""
    targetable_status: list[str]
    """Whether the segment is targetable"""
    updated_at: list[str]
    """Last update timestamp"""
    upload_status: list[str]
    """Upload processing status"""
    visible_to: list[list[Any]]
    """Visibility settings"""


class SegmentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    ad_account_id: Any
    """Parent ad account ID"""
    approximate_number_users: Any
    """Approximate number of users in the segment"""
    created_at: Any
    """Creation timestamp"""
    description: Any
    """Segment description"""
    id: Any
    """Unique segment identifier"""
    name: Any
    """Segment name"""
    organization_id: Any
    """Parent organization ID"""
    retention_in_days: Any
    """Data retention period in days"""
    source_type: Any
    """Segment source type"""
    status: Any
    """Segment status"""
    targetable_status: Any
    """Whether the segment is targetable"""
    updated_at: Any
    """Last update timestamp"""
    upload_status: Any
    """Upload processing status"""
    visible_to: Any
    """Visibility settings"""


class SegmentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    ad_account_id: str
    """Parent ad account ID"""
    approximate_number_users: str
    """Approximate number of users in the segment"""
    created_at: str
    """Creation timestamp"""
    description: str
    """Segment description"""
    id: str
    """Unique segment identifier"""
    name: str
    """Segment name"""
    organization_id: str
    """Parent organization ID"""
    retention_in_days: str
    """Data retention period in days"""
    source_type: str
    """Segment source type"""
    status: str
    """Segment status"""
    targetable_status: str
    """Whether the segment is targetable"""
    updated_at: str
    """Last update timestamp"""
    upload_status: str
    """Upload processing status"""
    visible_to: str
    """Visibility settings"""


class SegmentsSortFilter(TypedDict, total=False):
    """Available fields for sorting segments search results."""
    ad_account_id: AirbyteSortOrder
    """Parent ad account ID"""
    approximate_number_users: AirbyteSortOrder
    """Approximate number of users in the segment"""
    created_at: AirbyteSortOrder
    """Creation timestamp"""
    description: AirbyteSortOrder
    """Segment description"""
    id: AirbyteSortOrder
    """Unique segment identifier"""
    name: AirbyteSortOrder
    """Segment name"""
    organization_id: AirbyteSortOrder
    """Parent organization ID"""
    retention_in_days: AirbyteSortOrder
    """Data retention period in days"""
    source_type: AirbyteSortOrder
    """Segment source type"""
    status: AirbyteSortOrder
    """Segment status"""
    targetable_status: AirbyteSortOrder
    """Whether the segment is targetable"""
    updated_at: AirbyteSortOrder
    """Last update timestamp"""
    upload_status: AirbyteSortOrder
    """Upload processing status"""
    visible_to: AirbyteSortOrder
    """Visibility settings"""


# Entity-specific condition types for segments
class SegmentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SegmentsSearchFilter


class SegmentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SegmentsSearchFilter


class SegmentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SegmentsSearchFilter


class SegmentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SegmentsSearchFilter


class SegmentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SegmentsSearchFilter


class SegmentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SegmentsSearchFilter


class SegmentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SegmentsStringFilter


class SegmentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SegmentsStringFilter


class SegmentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SegmentsStringFilter


class SegmentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SegmentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SegmentsInCondition = TypedDict("SegmentsInCondition", {"in": SegmentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SegmentsNotCondition = TypedDict("SegmentsNotCondition", {"not": "SegmentsCondition"}, total=False)
"""Negates the nested condition."""

SegmentsAndCondition = TypedDict("SegmentsAndCondition", {"and": "list[SegmentsCondition]"}, total=False)
"""True if all nested conditions are true."""

SegmentsOrCondition = TypedDict("SegmentsOrCondition", {"or": "list[SegmentsCondition]"}, total=False)
"""True if any nested condition is true."""

SegmentsAnyCondition = TypedDict("SegmentsAnyCondition", {"any": SegmentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all segments condition types
SegmentsCondition = (
    SegmentsEqCondition
    | SegmentsNeqCondition
    | SegmentsGtCondition
    | SegmentsGteCondition
    | SegmentsLtCondition
    | SegmentsLteCondition
    | SegmentsInCondition
    | SegmentsLikeCondition
    | SegmentsFuzzyCondition
    | SegmentsKeywordCondition
    | SegmentsContainsCondition
    | SegmentsNotCondition
    | SegmentsAndCondition
    | SegmentsOrCondition
    | SegmentsAnyCondition
)


class SegmentsSearchQuery(TypedDict, total=False):
    """Search query for segments entity."""
    filter: SegmentsCondition
    sort: list[SegmentsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
