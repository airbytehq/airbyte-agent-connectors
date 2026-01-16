"""
Type definitions for hubspot connector.
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

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    contact_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

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

class CompaniesGetParams(TypedDict):
    """Parameters for companies.get operation"""
    company_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

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

class DealsGetParams(TypedDict):
    """Parameters for deals.get operation"""
    deal_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

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

class TicketsGetParams(TypedDict):
    """Parameters for tickets.get operation"""
    ticket_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

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
    """Boolean flag indicating whether the contact has been archived or deleted."""
    companies: list[Any] | None
    """Associated company records linked to this contact."""
    created_at: str | None
    """Timestamp indicating when the contact was first created in the system."""
    id: str | None
    """Unique identifier for the contact record."""
    properties: dict[str, Any]
    """Key-value object storing all contact properties and their values."""
    updated_at: str | None
    """Timestamp indicating when the contact record was last modified."""


class ContactsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Boolean flag indicating whether the contact has been archived or deleted."""
    companies: list[list[Any]]
    """Associated company records linked to this contact."""
    created_at: list[str]
    """Timestamp indicating when the contact was first created in the system."""
    id: list[str]
    """Unique identifier for the contact record."""
    properties: list[dict[str, Any]]
    """Key-value object storing all contact properties and their values."""
    updated_at: list[str]
    """Timestamp indicating when the contact record was last modified."""


class ContactsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Boolean flag indicating whether the contact has been archived or deleted."""
    companies: Any
    """Associated company records linked to this contact."""
    created_at: Any
    """Timestamp indicating when the contact was first created in the system."""
    id: Any
    """Unique identifier for the contact record."""
    properties: Any
    """Key-value object storing all contact properties and their values."""
    updated_at: Any
    """Timestamp indicating when the contact record was last modified."""


class ContactsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Boolean flag indicating whether the contact has been archived or deleted."""
    companies: str
    """Associated company records linked to this contact."""
    created_at: str
    """Timestamp indicating when the contact was first created in the system."""
    id: str
    """Unique identifier for the contact record."""
    properties: str
    """Key-value object storing all contact properties and their values."""
    updated_at: str
    """Timestamp indicating when the contact record was last modified."""


class ContactsSortFilter(TypedDict, total=False):
    """Available fields for sorting contacts search results."""
    archived: AirbyteSortOrder
    """Boolean flag indicating whether the contact has been archived or deleted."""
    companies: AirbyteSortOrder
    """Associated company records linked to this contact."""
    created_at: AirbyteSortOrder
    """Timestamp indicating when the contact was first created in the system."""
    id: AirbyteSortOrder
    """Unique identifier for the contact record."""
    properties: AirbyteSortOrder
    """Key-value object storing all contact properties and their values."""
    updated_at: AirbyteSortOrder
    """Timestamp indicating when the contact record was last modified."""


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



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
