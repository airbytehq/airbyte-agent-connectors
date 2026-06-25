"""
Type definitions for hubspot connector.
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

class ContactsCreateParamsProperties(TypedDict):
    """Contact properties to set"""
    email: str
    firstname: NotRequired[str]
    lastname: NotRequired[str]
    phone: NotRequired[str]
    company: NotRequired[str]
    website: NotRequired[str]
    lifecyclestage: NotRequired[str]
    jobtitle: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class ContactsUpdateParamsProperties(TypedDict):
    """Contact properties to update"""
    email: NotRequired[str]
    firstname: NotRequired[str]
    lastname: NotRequired[str]
    phone: NotRequired[str]
    company: NotRequired[str]
    website: NotRequired[str]
    lifecyclestage: NotRequired[str]
    jobtitle: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class ContactsApiSearchParamsFiltergroupsItemFiltersItem(TypedDict):
    """Nested schema for ContactsApiSearchParamsFiltergroupsItem.filters_item"""
    operator: NotRequired[str]
    propertyName: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[list[str]]

class ContactsApiSearchParamsFiltergroupsItem(TypedDict):
    """Nested schema for ContactsApiSearchParams.filterGroups_item"""
    filters: NotRequired[list[ContactsApiSearchParamsFiltergroupsItemFiltersItem]]

class ContactsApiSearchParamsSortsItem(TypedDict):
    """Nested schema for ContactsApiSearchParams.sorts_item"""
    propertyName: NotRequired[str]
    direction: NotRequired[str]

class CompaniesCreateParamsProperties(TypedDict):
    """Company properties to set"""
    name: str
    domain: NotRequired[str]
    description: NotRequired[str]
    phone: NotRequired[str]
    industry: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    country: NotRequired[str]
    zip: NotRequired[str]
    numberofemployees: NotRequired[str]
    annualrevenue: NotRequired[str]
    lifecyclestage: NotRequired[str]
    hubspot_owner_id: NotRequired[str]
    website: NotRequired[str]

class CompaniesUpdateParamsProperties(TypedDict):
    """Company properties to update"""
    name: NotRequired[str]
    domain: NotRequired[str]
    description: NotRequired[str]
    phone: NotRequired[str]
    industry: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    country: NotRequired[str]
    zip: NotRequired[str]
    numberofemployees: NotRequired[str]
    annualrevenue: NotRequired[str]
    lifecyclestage: NotRequired[str]
    hubspot_owner_id: NotRequired[str]
    website: NotRequired[str]

class CompaniesApiSearchParamsFiltergroupsItemFiltersItem(TypedDict):
    """Nested schema for CompaniesApiSearchParamsFiltergroupsItem.filters_item"""
    operator: NotRequired[str]
    propertyName: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[list[str]]

class CompaniesApiSearchParamsFiltergroupsItem(TypedDict):
    """Nested schema for CompaniesApiSearchParams.filterGroups_item"""
    filters: NotRequired[list[CompaniesApiSearchParamsFiltergroupsItemFiltersItem]]

class CompaniesApiSearchParamsSortsItem(TypedDict):
    """Nested schema for CompaniesApiSearchParams.sorts_item"""
    propertyName: NotRequired[str]
    direction: NotRequired[str]

class DealsCreateParamsProperties(TypedDict):
    """Deal properties to set"""
    dealname: str
    amount: NotRequired[str]
    dealstage: NotRequired[str]
    pipeline: NotRequired[str]
    closedate: NotRequired[str]
    dealtype: NotRequired[str]
    description: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class DealsUpdateParamsProperties(TypedDict):
    """Deal properties to update"""
    dealname: NotRequired[str]
    amount: NotRequired[str]
    dealstage: NotRequired[str]
    pipeline: NotRequired[str]
    closedate: NotRequired[str]
    dealtype: NotRequired[str]
    description: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class DealsApiSearchParamsFiltergroupsItemFiltersItem(TypedDict):
    """Nested schema for DealsApiSearchParamsFiltergroupsItem.filters_item"""
    operator: NotRequired[str]
    propertyName: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[list[str]]

class DealsApiSearchParamsFiltergroupsItem(TypedDict):
    """Nested schema for DealsApiSearchParams.filterGroups_item"""
    filters: NotRequired[list[DealsApiSearchParamsFiltergroupsItemFiltersItem]]

class DealsApiSearchParamsSortsItem(TypedDict):
    """Nested schema for DealsApiSearchParams.sorts_item"""
    propertyName: NotRequired[str]
    direction: NotRequired[str]

class TicketsCreateParamsProperties(TypedDict):
    """Ticket properties to set"""
    subject: str
    content: NotRequired[str]
    hs_pipeline: str
    hs_pipeline_stage: str
    hs_ticket_priority: NotRequired[str]
    hs_ticket_category: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class TicketsUpdateParamsProperties(TypedDict):
    """Ticket properties to update"""
    subject: NotRequired[str]
    content: NotRequired[str]
    hs_pipeline: NotRequired[str]
    hs_pipeline_stage: NotRequired[str]
    hs_ticket_priority: NotRequired[str]
    hs_ticket_category: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class TicketsApiSearchParamsFiltergroupsItemFiltersItem(TypedDict):
    """Nested schema for TicketsApiSearchParamsFiltergroupsItem.filters_item"""
    operator: NotRequired[str]
    propertyName: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[list[str]]

class TicketsApiSearchParamsFiltergroupsItem(TypedDict):
    """Nested schema for TicketsApiSearchParams.filterGroups_item"""
    filters: NotRequired[list[TicketsApiSearchParamsFiltergroupsItemFiltersItem]]

class TicketsApiSearchParamsSortsItem(TypedDict):
    """Nested schema for TicketsApiSearchParams.sorts_item"""
    propertyName: NotRequired[str]
    direction: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class ContactsCreateParams(TypedDict):
    """Parameters for contacts.create operation"""
    properties: ContactsCreateParamsProperties

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    contact_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class ContactsUpdateParams(TypedDict):
    """Parameters for contacts.update operation"""
    properties: ContactsUpdateParamsProperties
    contact_id: str

class ContactsApiSearchParams(TypedDict):
    """Parameters for contacts.api_search operation"""
    filter_groups: NotRequired[list[ContactsApiSearchParamsFiltergroupsItem]]
    properties: NotRequired[list[str]]
    limit: NotRequired[int]
    after: NotRequired[str]
    sorts: NotRequired[list[ContactsApiSearchParamsSortsItem]]
    query: NotRequired[str]

class CompaniesListParams(TypedDict):
    """Parameters for companies.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class CompaniesCreateParams(TypedDict):
    """Parameters for companies.create operation"""
    properties: CompaniesCreateParamsProperties

class CompaniesGetParams(TypedDict):
    """Parameters for companies.get operation"""
    company_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class CompaniesUpdateParams(TypedDict):
    """Parameters for companies.update operation"""
    properties: CompaniesUpdateParamsProperties
    company_id: str

class CompaniesApiSearchParams(TypedDict):
    """Parameters for companies.api_search operation"""
    filter_groups: NotRequired[list[CompaniesApiSearchParamsFiltergroupsItem]]
    properties: NotRequired[list[str]]
    limit: NotRequired[int]
    after: NotRequired[str]
    sorts: NotRequired[list[CompaniesApiSearchParamsSortsItem]]
    query: NotRequired[str]

class DealsListParams(TypedDict):
    """Parameters for deals.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class DealsCreateParams(TypedDict):
    """Parameters for deals.create operation"""
    properties: DealsCreateParamsProperties

class DealsGetParams(TypedDict):
    """Parameters for deals.get operation"""
    deal_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class DealsUpdateParams(TypedDict):
    """Parameters for deals.update operation"""
    properties: DealsUpdateParamsProperties
    deal_id: str

class DealsApiSearchParams(TypedDict):
    """Parameters for deals.api_search operation"""
    filter_groups: NotRequired[list[DealsApiSearchParamsFiltergroupsItem]]
    properties: NotRequired[list[str]]
    limit: NotRequired[int]
    after: NotRequired[str]
    sorts: NotRequired[list[DealsApiSearchParamsSortsItem]]
    query: NotRequired[str]

class TicketsListParams(TypedDict):
    """Parameters for tickets.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class TicketsCreateParams(TypedDict):
    """Parameters for tickets.create operation"""
    properties: TicketsCreateParamsProperties

class TicketsGetParams(TypedDict):
    """Parameters for tickets.get operation"""
    ticket_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class TicketsUpdateParams(TypedDict):
    """Parameters for tickets.update operation"""
    properties: TicketsUpdateParamsProperties
    ticket_id: str

class TicketsApiSearchParams(TypedDict):
    """Parameters for tickets.api_search operation"""
    filter_groups: NotRequired[list[TicketsApiSearchParamsFiltergroupsItem]]
    properties: NotRequired[list[str]]
    limit: NotRequired[int]
    after: NotRequired[str]
    sorts: NotRequired[list[TicketsApiSearchParamsSortsItem]]
    query: NotRequired[str]

class SchemasListParams(TypedDict):
    """Parameters for schemas.list operation"""
    archived: NotRequired[bool]

class SchemasGetParams(TypedDict):
    """Parameters for schemas.get operation"""
    object_type: str

class ObjectsListParams(TypedDict):
    """Parameters for objects.list operation"""
    object_type: str
    limit: NotRequired[int]
    after: NotRequired[str]
    properties: NotRequired[str]
    archived: NotRequired[bool]
    associations: NotRequired[str]
    properties_with_history: NotRequired[str]

class ObjectsGetParams(TypedDict):
    """Parameters for objects.get operation"""
    object_type: str
    object_id: str
    properties: NotRequired[str]
    archived: NotRequired[bool]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    properties_with_history: NotRequired[str]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== COMPANIES SEARCH TYPES =====

class CompaniesSearchFilter(TypedDict, total=False):
    """Available fields for filtering companies search queries."""
    archived: bool | None
    """Indicates whether the company has been deleted and moved to the recycling bin"""
    contacts: list[Any] | None
    """Associated contact records linked to this company"""
    created_at: str | None
    """Timestamp when the company record was created"""
    id: str | None
    """Unique identifier for the company record"""
    properties: dict[str, Any]
    """Object containing all property values for the company"""
    properties_createdate: str | None
    """Date the company was created"""
    properties_domain: str | None
    """Company domain name"""
    properties_hs_lastmodifieddate: str | None
    """Last modified date of the company"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hubspot_owner_id: str | None
    """ID of the HubSpot owner assigned to this company"""
    properties_name: str | None
    """Company name"""
    updated_at: str | None
    """Timestamp when the company record was last modified"""


class CompaniesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates whether the company has been deleted and moved to the recycling bin"""
    contacts: list[list[Any]]
    """Associated contact records linked to this company"""
    created_at: list[str]
    """Timestamp when the company record was created"""
    id: list[str]
    """Unique identifier for the company record"""
    properties: list[dict[str, Any]]
    """Object containing all property values for the company"""
    properties_createdate: list[str]
    """Date the company was created"""
    properties_domain: list[str]
    """Company domain name"""
    properties_hs_lastmodifieddate: list[str]
    """Last modified date of the company"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hubspot_owner_id: list[str]
    """ID of the HubSpot owner assigned to this company"""
    properties_name: list[str]
    """Company name"""
    updated_at: list[str]
    """Timestamp when the company record was last modified"""


class CompaniesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates whether the company has been deleted and moved to the recycling bin"""
    contacts: Any
    """Associated contact records linked to this company"""
    created_at: Any
    """Timestamp when the company record was created"""
    id: Any
    """Unique identifier for the company record"""
    properties: Any
    """Object containing all property values for the company"""
    properties_createdate: Any
    """Date the company was created"""
    properties_domain: Any
    """Company domain name"""
    properties_hs_lastmodifieddate: Any
    """Last modified date of the company"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hubspot_owner_id: Any
    """ID of the HubSpot owner assigned to this company"""
    properties_name: Any
    """Company name"""
    updated_at: Any
    """Timestamp when the company record was last modified"""


class CompaniesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates whether the company has been deleted and moved to the recycling bin"""
    contacts: str
    """Associated contact records linked to this company"""
    created_at: str
    """Timestamp when the company record was created"""
    id: str
    """Unique identifier for the company record"""
    properties: str
    """Object containing all property values for the company"""
    properties_createdate: str
    """Date the company was created"""
    properties_domain: str
    """Company domain name"""
    properties_hs_lastmodifieddate: str
    """Last modified date of the company"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hubspot_owner_id: str
    """ID of the HubSpot owner assigned to this company"""
    properties_name: str
    """Company name"""
    updated_at: str
    """Timestamp when the company record was last modified"""


class CompaniesSortFilter(TypedDict, total=False):
    """Available fields for sorting companies search results."""
    archived: AirbyteSortOrder
    """Indicates whether the company has been deleted and moved to the recycling bin"""
    contacts: AirbyteSortOrder
    """Associated contact records linked to this company"""
    created_at: AirbyteSortOrder
    """Timestamp when the company record was created"""
    id: AirbyteSortOrder
    """Unique identifier for the company record"""
    properties: AirbyteSortOrder
    """Object containing all property values for the company"""
    properties_createdate: AirbyteSortOrder
    """Date the company was created"""
    properties_domain: AirbyteSortOrder
    """Company domain name"""
    properties_hs_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the company"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hubspot_owner_id: AirbyteSortOrder
    """ID of the HubSpot owner assigned to this company"""
    properties_name: AirbyteSortOrder
    """Company name"""
    updated_at: AirbyteSortOrder
    """Timestamp when the company record was last modified"""


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
    archived: bool | None
    """Boolean flag indicating whether the contact has been archived or deleted"""
    companies: list[Any] | None
    """Associated company records linked to this contact"""
    created_at: str | None
    """Timestamp indicating when the contact was first created in the system"""
    id: str | None
    """Unique identifier for the contact record"""
    properties: dict[str, Any]
    """Key-value object storing all contact properties and their values."""
    properties_associatedcompanyid: str | None
    """ID of the associated company"""
    properties_createdate: str | None
    """Date the contact was created"""
    properties_email: str | None
    """Contact email address"""
    properties_firstname: str | None
    """Contact first name"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hubspot_owner_id: str | None
    """ID of the HubSpot owner assigned to this contact"""
    properties_lastmodifieddate: str | None
    """Last modified date of the contact"""
    properties_lastname: str | None
    """Contact last name"""
    updated_at: str | None
    """Timestamp indicating when the contact record was last modified"""


class ContactsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Boolean flag indicating whether the contact has been archived or deleted"""
    companies: list[list[Any]]
    """Associated company records linked to this contact"""
    created_at: list[str]
    """Timestamp indicating when the contact was first created in the system"""
    id: list[str]
    """Unique identifier for the contact record"""
    properties: list[dict[str, Any]]
    """Key-value object storing all contact properties and their values."""
    properties_associatedcompanyid: list[str]
    """ID of the associated company"""
    properties_createdate: list[str]
    """Date the contact was created"""
    properties_email: list[str]
    """Contact email address"""
    properties_firstname: list[str]
    """Contact first name"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hubspot_owner_id: list[str]
    """ID of the HubSpot owner assigned to this contact"""
    properties_lastmodifieddate: list[str]
    """Last modified date of the contact"""
    properties_lastname: list[str]
    """Contact last name"""
    updated_at: list[str]
    """Timestamp indicating when the contact record was last modified"""


class ContactsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Boolean flag indicating whether the contact has been archived or deleted"""
    companies: Any
    """Associated company records linked to this contact"""
    created_at: Any
    """Timestamp indicating when the contact was first created in the system"""
    id: Any
    """Unique identifier for the contact record"""
    properties: Any
    """Key-value object storing all contact properties and their values."""
    properties_associatedcompanyid: Any
    """ID of the associated company"""
    properties_createdate: Any
    """Date the contact was created"""
    properties_email: Any
    """Contact email address"""
    properties_firstname: Any
    """Contact first name"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hubspot_owner_id: Any
    """ID of the HubSpot owner assigned to this contact"""
    properties_lastmodifieddate: Any
    """Last modified date of the contact"""
    properties_lastname: Any
    """Contact last name"""
    updated_at: Any
    """Timestamp indicating when the contact record was last modified"""


class ContactsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Boolean flag indicating whether the contact has been archived or deleted"""
    companies: str
    """Associated company records linked to this contact"""
    created_at: str
    """Timestamp indicating when the contact was first created in the system"""
    id: str
    """Unique identifier for the contact record"""
    properties: str
    """Key-value object storing all contact properties and their values."""
    properties_associatedcompanyid: str
    """ID of the associated company"""
    properties_createdate: str
    """Date the contact was created"""
    properties_email: str
    """Contact email address"""
    properties_firstname: str
    """Contact first name"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hubspot_owner_id: str
    """ID of the HubSpot owner assigned to this contact"""
    properties_lastmodifieddate: str
    """Last modified date of the contact"""
    properties_lastname: str
    """Contact last name"""
    updated_at: str
    """Timestamp indicating when the contact record was last modified"""


class ContactsSortFilter(TypedDict, total=False):
    """Available fields for sorting contacts search results."""
    archived: AirbyteSortOrder
    """Boolean flag indicating whether the contact has been archived or deleted"""
    companies: AirbyteSortOrder
    """Associated company records linked to this contact"""
    created_at: AirbyteSortOrder
    """Timestamp indicating when the contact was first created in the system"""
    id: AirbyteSortOrder
    """Unique identifier for the contact record"""
    properties: AirbyteSortOrder
    """Key-value object storing all contact properties and their values."""
    properties_associatedcompanyid: AirbyteSortOrder
    """ID of the associated company"""
    properties_createdate: AirbyteSortOrder
    """Date the contact was created"""
    properties_email: AirbyteSortOrder
    """Contact email address"""
    properties_firstname: AirbyteSortOrder
    """Contact first name"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hubspot_owner_id: AirbyteSortOrder
    """ID of the HubSpot owner assigned to this contact"""
    properties_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the contact"""
    properties_lastname: AirbyteSortOrder
    """Contact last name"""
    updated_at: AirbyteSortOrder
    """Timestamp indicating when the contact record was last modified"""


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


# ===== DEALS SEARCH TYPES =====

class DealsSearchFilter(TypedDict, total=False):
    """Available fields for filtering deals search queries."""
    archived: bool | None
    """Indicates whether the deal has been deleted and moved to the recycling bin"""
    companies: list[Any] | None
    """Collection of company records associated with the deal"""
    contacts: list[Any] | None
    """Collection of contact records associated with the deal"""
    created_at: str | None
    """Timestamp when the deal record was originally created"""
    id: str | None
    """Unique identifier for the deal record"""
    line_items: list[Any] | None
    """Collection of product line items associated with the deal"""
    properties: dict[str, Any]
    """Key-value object containing all deal properties and custom fields"""
    properties_amount: str | None
    """Deal amount"""
    properties_closedate: str | None
    """Expected close date of the deal"""
    properties_createdate: str | None
    """Date the deal was created"""
    properties_dealname: str | None
    """Deal name"""
    properties_dealstage: str | None
    """Current deal stage"""
    properties_hs_lastmodifieddate: str | None
    """Last modified date of the deal"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hubspot_owner_id: str | None
    """ID of the HubSpot owner assigned to this deal"""
    properties_pipeline: str | None
    """Deal pipeline"""
    updated_at: str | None
    """Timestamp when the deal record was last modified"""


class DealsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates whether the deal has been deleted and moved to the recycling bin"""
    companies: list[list[Any]]
    """Collection of company records associated with the deal"""
    contacts: list[list[Any]]
    """Collection of contact records associated with the deal"""
    created_at: list[str]
    """Timestamp when the deal record was originally created"""
    id: list[str]
    """Unique identifier for the deal record"""
    line_items: list[list[Any]]
    """Collection of product line items associated with the deal"""
    properties: list[dict[str, Any]]
    """Key-value object containing all deal properties and custom fields"""
    properties_amount: list[str]
    """Deal amount"""
    properties_closedate: list[str]
    """Expected close date of the deal"""
    properties_createdate: list[str]
    """Date the deal was created"""
    properties_dealname: list[str]
    """Deal name"""
    properties_dealstage: list[str]
    """Current deal stage"""
    properties_hs_lastmodifieddate: list[str]
    """Last modified date of the deal"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hubspot_owner_id: list[str]
    """ID of the HubSpot owner assigned to this deal"""
    properties_pipeline: list[str]
    """Deal pipeline"""
    updated_at: list[str]
    """Timestamp when the deal record was last modified"""


class DealsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates whether the deal has been deleted and moved to the recycling bin"""
    companies: Any
    """Collection of company records associated with the deal"""
    contacts: Any
    """Collection of contact records associated with the deal"""
    created_at: Any
    """Timestamp when the deal record was originally created"""
    id: Any
    """Unique identifier for the deal record"""
    line_items: Any
    """Collection of product line items associated with the deal"""
    properties: Any
    """Key-value object containing all deal properties and custom fields"""
    properties_amount: Any
    """Deal amount"""
    properties_closedate: Any
    """Expected close date of the deal"""
    properties_createdate: Any
    """Date the deal was created"""
    properties_dealname: Any
    """Deal name"""
    properties_dealstage: Any
    """Current deal stage"""
    properties_hs_lastmodifieddate: Any
    """Last modified date of the deal"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hubspot_owner_id: Any
    """ID of the HubSpot owner assigned to this deal"""
    properties_pipeline: Any
    """Deal pipeline"""
    updated_at: Any
    """Timestamp when the deal record was last modified"""


class DealsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates whether the deal has been deleted and moved to the recycling bin"""
    companies: str
    """Collection of company records associated with the deal"""
    contacts: str
    """Collection of contact records associated with the deal"""
    created_at: str
    """Timestamp when the deal record was originally created"""
    id: str
    """Unique identifier for the deal record"""
    line_items: str
    """Collection of product line items associated with the deal"""
    properties: str
    """Key-value object containing all deal properties and custom fields"""
    properties_amount: str
    """Deal amount"""
    properties_closedate: str
    """Expected close date of the deal"""
    properties_createdate: str
    """Date the deal was created"""
    properties_dealname: str
    """Deal name"""
    properties_dealstage: str
    """Current deal stage"""
    properties_hs_lastmodifieddate: str
    """Last modified date of the deal"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hubspot_owner_id: str
    """ID of the HubSpot owner assigned to this deal"""
    properties_pipeline: str
    """Deal pipeline"""
    updated_at: str
    """Timestamp when the deal record was last modified"""


class DealsSortFilter(TypedDict, total=False):
    """Available fields for sorting deals search results."""
    archived: AirbyteSortOrder
    """Indicates whether the deal has been deleted and moved to the recycling bin"""
    companies: AirbyteSortOrder
    """Collection of company records associated with the deal"""
    contacts: AirbyteSortOrder
    """Collection of contact records associated with the deal"""
    created_at: AirbyteSortOrder
    """Timestamp when the deal record was originally created"""
    id: AirbyteSortOrder
    """Unique identifier for the deal record"""
    line_items: AirbyteSortOrder
    """Collection of product line items associated with the deal"""
    properties: AirbyteSortOrder
    """Key-value object containing all deal properties and custom fields"""
    properties_amount: AirbyteSortOrder
    """Deal amount"""
    properties_closedate: AirbyteSortOrder
    """Expected close date of the deal"""
    properties_createdate: AirbyteSortOrder
    """Date the deal was created"""
    properties_dealname: AirbyteSortOrder
    """Deal name"""
    properties_dealstage: AirbyteSortOrder
    """Current deal stage"""
    properties_hs_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the deal"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hubspot_owner_id: AirbyteSortOrder
    """ID of the HubSpot owner assigned to this deal"""
    properties_pipeline: AirbyteSortOrder
    """Deal pipeline"""
    updated_at: AirbyteSortOrder
    """Timestamp when the deal record was last modified"""


# Entity-specific condition types for deals
class DealsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DealsSearchFilter


class DealsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DealsSearchFilter


class DealsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DealsSearchFilter


class DealsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DealsSearchFilter


class DealsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DealsSearchFilter


class DealsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DealsSearchFilter


class DealsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DealsStringFilter


class DealsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DealsStringFilter


class DealsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DealsStringFilter


class DealsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DealsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DealsInCondition = TypedDict("DealsInCondition", {"in": DealsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DealsNotCondition = TypedDict("DealsNotCondition", {"not": "DealsCondition"}, total=False)
"""Negates the nested condition."""

DealsAndCondition = TypedDict("DealsAndCondition", {"and": "list[DealsCondition]"}, total=False)
"""True if all nested conditions are true."""

DealsOrCondition = TypedDict("DealsOrCondition", {"or": "list[DealsCondition]"}, total=False)
"""True if any nested condition is true."""

DealsAnyCondition = TypedDict("DealsAnyCondition", {"any": DealsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all deals condition types
DealsCondition = (
    DealsEqCondition
    | DealsNeqCondition
    | DealsGtCondition
    | DealsGteCondition
    | DealsLtCondition
    | DealsLteCondition
    | DealsInCondition
    | DealsLikeCondition
    | DealsFuzzyCondition
    | DealsKeywordCondition
    | DealsContainsCondition
    | DealsNotCondition
    | DealsAndCondition
    | DealsOrCondition
    | DealsAnyCondition
)


class DealsSearchQuery(TypedDict, total=False):
    """Search query for deals entity."""
    filter: DealsCondition
    sort: list[DealsSortFilter]


# ===== TICKETS SEARCH TYPES =====

class TicketsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tickets search queries."""
    archived: bool | None
    """Indicates whether the ticket has been deleted and moved to the recycling bin"""
    companies: list[Any] | None
    """Collection of company records associated with the ticket"""
    contacts: list[Any] | None
    """Collection of contact records associated with the ticket"""
    created_at: str | None
    """Timestamp when the ticket record was originally created"""
    id: str | None
    """Unique identifier for the ticket record"""
    properties: dict[str, Any]
    """Object containing all property values for the ticket"""
    properties_content: str | None
    """Ticket content/description"""
    properties_createdate: str | None
    """Date the ticket was created"""
    properties_hs_lastmodifieddate: str | None
    """Last modified date of the ticket"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hs_pipeline: str | None
    """Ticket pipeline"""
    properties_hs_pipeline_stage: str | None
    """Current pipeline stage of the ticket"""
    properties_hs_ticket_category: str | None
    """Ticket category"""
    properties_hs_ticket_priority: str | None
    """Ticket priority level"""
    properties_subject: str | None
    """Ticket subject line"""
    updated_at: str | None
    """Timestamp when the ticket record was last modified"""


class TicketsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates whether the ticket has been deleted and moved to the recycling bin"""
    companies: list[list[Any]]
    """Collection of company records associated with the ticket"""
    contacts: list[list[Any]]
    """Collection of contact records associated with the ticket"""
    created_at: list[str]
    """Timestamp when the ticket record was originally created"""
    id: list[str]
    """Unique identifier for the ticket record"""
    properties: list[dict[str, Any]]
    """Object containing all property values for the ticket"""
    properties_content: list[str]
    """Ticket content/description"""
    properties_createdate: list[str]
    """Date the ticket was created"""
    properties_hs_lastmodifieddate: list[str]
    """Last modified date of the ticket"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hs_pipeline: list[str]
    """Ticket pipeline"""
    properties_hs_pipeline_stage: list[str]
    """Current pipeline stage of the ticket"""
    properties_hs_ticket_category: list[str]
    """Ticket category"""
    properties_hs_ticket_priority: list[str]
    """Ticket priority level"""
    properties_subject: list[str]
    """Ticket subject line"""
    updated_at: list[str]
    """Timestamp when the ticket record was last modified"""


class TicketsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates whether the ticket has been deleted and moved to the recycling bin"""
    companies: Any
    """Collection of company records associated with the ticket"""
    contacts: Any
    """Collection of contact records associated with the ticket"""
    created_at: Any
    """Timestamp when the ticket record was originally created"""
    id: Any
    """Unique identifier for the ticket record"""
    properties: Any
    """Object containing all property values for the ticket"""
    properties_content: Any
    """Ticket content/description"""
    properties_createdate: Any
    """Date the ticket was created"""
    properties_hs_lastmodifieddate: Any
    """Last modified date of the ticket"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hs_pipeline: Any
    """Ticket pipeline"""
    properties_hs_pipeline_stage: Any
    """Current pipeline stage of the ticket"""
    properties_hs_ticket_category: Any
    """Ticket category"""
    properties_hs_ticket_priority: Any
    """Ticket priority level"""
    properties_subject: Any
    """Ticket subject line"""
    updated_at: Any
    """Timestamp when the ticket record was last modified"""


class TicketsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates whether the ticket has been deleted and moved to the recycling bin"""
    companies: str
    """Collection of company records associated with the ticket"""
    contacts: str
    """Collection of contact records associated with the ticket"""
    created_at: str
    """Timestamp when the ticket record was originally created"""
    id: str
    """Unique identifier for the ticket record"""
    properties: str
    """Object containing all property values for the ticket"""
    properties_content: str
    """Ticket content/description"""
    properties_createdate: str
    """Date the ticket was created"""
    properties_hs_lastmodifieddate: str
    """Last modified date of the ticket"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hs_pipeline: str
    """Ticket pipeline"""
    properties_hs_pipeline_stage: str
    """Current pipeline stage of the ticket"""
    properties_hs_ticket_category: str
    """Ticket category"""
    properties_hs_ticket_priority: str
    """Ticket priority level"""
    properties_subject: str
    """Ticket subject line"""
    updated_at: str
    """Timestamp when the ticket record was last modified"""


class TicketsSortFilter(TypedDict, total=False):
    """Available fields for sorting tickets search results."""
    archived: AirbyteSortOrder
    """Indicates whether the ticket has been deleted and moved to the recycling bin"""
    companies: AirbyteSortOrder
    """Collection of company records associated with the ticket"""
    contacts: AirbyteSortOrder
    """Collection of contact records associated with the ticket"""
    created_at: AirbyteSortOrder
    """Timestamp when the ticket record was originally created"""
    id: AirbyteSortOrder
    """Unique identifier for the ticket record"""
    properties: AirbyteSortOrder
    """Object containing all property values for the ticket"""
    properties_content: AirbyteSortOrder
    """Ticket content/description"""
    properties_createdate: AirbyteSortOrder
    """Date the ticket was created"""
    properties_hs_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the ticket"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hs_pipeline: AirbyteSortOrder
    """Ticket pipeline"""
    properties_hs_pipeline_stage: AirbyteSortOrder
    """Current pipeline stage of the ticket"""
    properties_hs_ticket_category: AirbyteSortOrder
    """Ticket category"""
    properties_hs_ticket_priority: AirbyteSortOrder
    """Ticket priority level"""
    properties_subject: AirbyteSortOrder
    """Ticket subject line"""
    updated_at: AirbyteSortOrder
    """Timestamp when the ticket record was last modified"""


# Entity-specific condition types for tickets
class TicketsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TicketsSearchFilter


class TicketsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TicketsSearchFilter


class TicketsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TicketsSearchFilter


class TicketsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TicketsSearchFilter


class TicketsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TicketsSearchFilter


class TicketsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TicketsSearchFilter


class TicketsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TicketsStringFilter


class TicketsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TicketsStringFilter


class TicketsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TicketsStringFilter


class TicketsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TicketsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TicketsInCondition = TypedDict("TicketsInCondition", {"in": TicketsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TicketsNotCondition = TypedDict("TicketsNotCondition", {"not": "TicketsCondition"}, total=False)
"""Negates the nested condition."""

TicketsAndCondition = TypedDict("TicketsAndCondition", {"and": "list[TicketsCondition]"}, total=False)
"""True if all nested conditions are true."""

TicketsOrCondition = TypedDict("TicketsOrCondition", {"or": "list[TicketsCondition]"}, total=False)
"""True if any nested condition is true."""

TicketsAnyCondition = TypedDict("TicketsAnyCondition", {"any": TicketsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tickets condition types
TicketsCondition = (
    TicketsEqCondition
    | TicketsNeqCondition
    | TicketsGtCondition
    | TicketsGteCondition
    | TicketsLtCondition
    | TicketsLteCondition
    | TicketsInCondition
    | TicketsLikeCondition
    | TicketsFuzzyCondition
    | TicketsKeywordCondition
    | TicketsContainsCondition
    | TicketsNotCondition
    | TicketsAndCondition
    | TicketsOrCondition
    | TicketsAnyCondition
)


class TicketsSearchQuery(TypedDict, total=False):
    """Search query for tickets entity."""
    filter: TicketsCondition
    sort: list[TicketsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
