"""
Type definitions for hubspot connector.
"""
# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any

# ===== RESPONSE TYPE DEFINITIONS =====

class Contact(TypedDict):
    """HubSpot contact object"""
    id: NotRequired[str]
    properties: NotRequired[dict[str, Any]]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]
    archived: NotRequired[bool]

class PagingNext(TypedDict):
    """Nested schema for Paging.next"""
    after: NotRequired[str]
    link: NotRequired[str]

class Paging(TypedDict):
    """Pagination information"""
    next: NotRequired[PagingNext]

class ContactsList(TypedDict):
    """Paginated list of contacts"""
    results: NotRequired[list[Contact]]
    paging: NotRequired[Paging]

class Company(TypedDict):
    """HubSpot company object"""
    id: NotRequired[str]
    properties: NotRequired[dict[str, Any]]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]
    archived: NotRequired[bool]

class CompaniesList(TypedDict):
    """Paginated list of companies"""
    results: NotRequired[list[Company]]
    paging: NotRequired[Paging]

class Deal(TypedDict):
    """HubSpot deal object"""
    id: NotRequired[str]
    properties: NotRequired[dict[str, Any]]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]
    archived: NotRequired[bool]

class DealsList(TypedDict):
    """Paginated list of deals"""
    results: NotRequired[list[Deal]]
    paging: NotRequired[Paging]

class Ticket(TypedDict):
    """HubSpot ticket object"""
    id: NotRequired[str]
    properties: NotRequired[dict[str, Any]]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]
    archived: NotRequired[bool]

class TicketsList(TypedDict):
    """Paginated list of tickets"""
    results: NotRequired[list[Ticket]]
    paging: NotRequired[Paging]

class SchemaLabels(TypedDict):
    """Display labels"""
    singular: NotRequired[str]
    plural: NotRequired[str]

class Schema(TypedDict):
    """Custom object schema definition"""
    id: NotRequired[str]
    name: NotRequired[str]
    labels: NotRequired[SchemaLabels]
    objectTypeId: NotRequired[str]
    fullyQualifiedName: NotRequired[str]
    properties: NotRequired[list[dict[str, Any]]]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]

class SchemasList(TypedDict):
    """List of custom object schemas"""
    results: NotRequired[list[Schema]]

class CRMObject(TypedDict):
    """Generic HubSpot CRM object (for custom objects)"""
    id: NotRequired[str]
    properties: NotRequired[dict[str, Any]]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]
    archived: NotRequired[bool]

class ObjectsList(TypedDict):
    """Paginated list of generic CRM objects"""
    results: NotRequired[list[CRMObject]]
    paging: NotRequired[Paging]

# ===== METADATA TYPE DEFINITIONS =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    properties: NotRequired[str]
    archived: NotRequired[bool]

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    contact_id: str
    properties: NotRequired[str]

class CompaniesListParams(TypedDict):
    """Parameters for companies.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    properties: NotRequired[str]
    archived: NotRequired[bool]

class CompaniesGetParams(TypedDict):
    """Parameters for companies.get operation"""
    company_id: str
    properties: NotRequired[str]

class DealsListParams(TypedDict):
    """Parameters for deals.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    properties: NotRequired[str]
    archived: NotRequired[bool]

class DealsGetParams(TypedDict):
    """Parameters for deals.get operation"""
    deal_id: str
    properties: NotRequired[str]

class TicketsListParams(TypedDict):
    """Parameters for tickets.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    properties: NotRequired[str]
    archived: NotRequired[bool]

class TicketsGetParams(TypedDict):
    """Parameters for tickets.get operation"""
    ticket_id: str
    properties: NotRequired[str]

class SchemasListParams(TypedDict):
    """Parameters for schemas.list operation"""
    pass

class ObjectsListParams(TypedDict):
    """Parameters for objects.list operation"""
    object_type: str
    limit: NotRequired[int]
    after: NotRequired[str]
    properties: NotRequired[str]
    archived: NotRequired[bool]

class ObjectsGetParams(TypedDict):
    """Parameters for objects.get operation"""
    object_type: str
    object_id: str
    properties: NotRequired[str]
