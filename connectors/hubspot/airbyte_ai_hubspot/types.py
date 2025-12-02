"""
Auto-generated type definitions for hubspot connector.

Generated from OpenAPI specification schemas.
"""
from typing import TypedDict, NotRequired, Any

# ===== AUTH CONFIG TYPE DEFINITIONS =====

class HubspotAuthConfig(TypedDict):
    """Access Token Authentication"""
    access_token: str  # Your HubSpot Private App Access Token or OAuth Access Token

# ===== RESPONSE TYPE DEFINITIONS =====

class Contact(TypedDict):
    """HubSpot contact object"""
    id: NotRequired[str]
    properties: NotRequired[dict[str, Any]]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]
    archived: NotRequired[bool]

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

class Schema(TypedDict):
    """Custom object schema definition"""
    id: NotRequired[str]
    name: NotRequired[str]
    labels: NotRequired[dict[str, Any]]
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

class Paging(TypedDict):
    """Pagination information"""
    next: NotRequired[dict[str, Any]]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    properties: NotRequired[str]
    archived: NotRequired[bool]

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    contactId: str
    properties: NotRequired[str]

class CompaniesListParams(TypedDict):
    """Parameters for companies.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    properties: NotRequired[str]
    archived: NotRequired[bool]

class CompaniesGetParams(TypedDict):
    """Parameters for companies.get operation"""
    companyId: str
    properties: NotRequired[str]

class DealsListParams(TypedDict):
    """Parameters for deals.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    properties: NotRequired[str]
    archived: NotRequired[bool]

class DealsGetParams(TypedDict):
    """Parameters for deals.get operation"""
    dealId: str
    properties: NotRequired[str]

class TicketsListParams(TypedDict):
    """Parameters for tickets.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    properties: NotRequired[str]
    archived: NotRequired[bool]

class TicketsGetParams(TypedDict):
    """Parameters for tickets.get operation"""
    ticketId: str
    properties: NotRequired[str]

class SchemasListParams(TypedDict):
    """Parameters for schemas.list operation"""
    pass

class ObjectsListParams(TypedDict):
    """Parameters for objects.list operation"""
    objectType: str
    limit: NotRequired[int]
    after: NotRequired[str]
    properties: NotRequired[str]
    archived: NotRequired[bool]

class ObjectsGetParams(TypedDict):
    """Parameters for objects.get operation"""
    objectType: str
    objectId: str
    properties: NotRequired[str]
