"""
Type definitions for hubspot connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



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
