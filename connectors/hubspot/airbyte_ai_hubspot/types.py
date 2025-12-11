"""
Type definitions for hubspot connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

class ContactsSearchParamsFiltergroupsItemFiltersItem(TypedDict):
    """Nested schema for ContactsSearchParamsFiltergroupsItem.filters_item"""
    operator: NotRequired[str]
    propertyName: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[list[str]]

class ContactsSearchParamsFiltergroupsItem(TypedDict):
    """Nested schema for ContactsSearchParams.filterGroups_item"""
    filters: NotRequired[list[ContactsSearchParamsFiltergroupsItemFiltersItem]]

class ContactsSearchParamsSortsItem(TypedDict):
    """Nested schema for ContactsSearchParams.sorts_item"""
    propertyName: NotRequired[str]
    direction: NotRequired[str]

class CompaniesSearchParamsFiltergroupsItemFiltersItem(TypedDict):
    """Nested schema for CompaniesSearchParamsFiltergroupsItem.filters_item"""
    operator: NotRequired[str]
    propertyName: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[list[str]]

class CompaniesSearchParamsFiltergroupsItem(TypedDict):
    """Nested schema for CompaniesSearchParams.filterGroups_item"""
    filters: NotRequired[list[CompaniesSearchParamsFiltergroupsItemFiltersItem]]

class CompaniesSearchParamsSortsItem(TypedDict):
    """Nested schema for CompaniesSearchParams.sorts_item"""
    propertyName: NotRequired[str]
    direction: NotRequired[str]

class DealsSearchParamsFiltergroupsItemFiltersItem(TypedDict):
    """Nested schema for DealsSearchParamsFiltergroupsItem.filters_item"""
    operator: NotRequired[str]
    propertyName: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[list[str]]

class DealsSearchParamsFiltergroupsItem(TypedDict):
    """Nested schema for DealsSearchParams.filterGroups_item"""
    filters: NotRequired[list[DealsSearchParamsFiltergroupsItemFiltersItem]]

class DealsSearchParamsSortsItem(TypedDict):
    """Nested schema for DealsSearchParams.sorts_item"""
    propertyName: NotRequired[str]
    direction: NotRequired[str]

class TicketsSearchParamsFiltergroupsItemFiltersItem(TypedDict):
    """Nested schema for TicketsSearchParamsFiltergroupsItem.filters_item"""
    operator: NotRequired[str]
    propertyName: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[list[str]]

class TicketsSearchParamsFiltergroupsItem(TypedDict):
    """Nested schema for TicketsSearchParams.filterGroups_item"""
    filters: NotRequired[list[TicketsSearchParamsFiltergroupsItemFiltersItem]]

class TicketsSearchParamsSortsItem(TypedDict):
    """Nested schema for TicketsSearchParams.sorts_item"""
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

class ContactsSearchParams(TypedDict):
    """Parameters for contacts.search operation"""
    filter_groups: NotRequired[list[ContactsSearchParamsFiltergroupsItem]]
    properties: NotRequired[list[str]]
    limit: NotRequired[int]
    after: NotRequired[str]
    sorts: NotRequired[list[ContactsSearchParamsSortsItem]]
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

class CompaniesSearchParams(TypedDict):
    """Parameters for companies.search operation"""
    filter_groups: NotRequired[list[CompaniesSearchParamsFiltergroupsItem]]
    properties: NotRequired[list[str]]
    limit: NotRequired[int]
    after: NotRequired[str]
    sorts: NotRequired[list[CompaniesSearchParamsSortsItem]]
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

class DealsSearchParams(TypedDict):
    """Parameters for deals.search operation"""
    filter_groups: NotRequired[list[DealsSearchParamsFiltergroupsItem]]
    properties: NotRequired[list[str]]
    limit: NotRequired[int]
    after: NotRequired[str]
    sorts: NotRequired[list[DealsSearchParamsSortsItem]]
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

class TicketsSearchParams(TypedDict):
    """Parameters for tickets.search operation"""
    filter_groups: NotRequired[list[TicketsSearchParamsFiltergroupsItem]]
    properties: NotRequired[list[str]]
    limit: NotRequired[int]
    after: NotRequired[str]
    sorts: NotRequired[list[TicketsSearchParamsSortsItem]]
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
