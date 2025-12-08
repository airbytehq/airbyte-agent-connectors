"""
Blessed Hubspot connector for Airbyte SDK.

Auto-generated from OpenAPI specification.
"""

from .connector import HubspotConnector
from .models import (
    HubspotAuthConfig,
    Contact,
    PagingNext,
    Paging,
    ContactsList,
    Company,
    CompaniesList,
    Deal,
    DealsList,
    Ticket,
    TicketsList,
    SchemaLabels,
    Schema,
    SchemasList,
    CRMObject,
    ObjectsList,
    HubspotExecuteResult,
    HubspotExecuteResultWithMeta
)
from .types import (
    SchemaLabels,
    PagingNext,
    ContactsListParams,
    ContactsGetParams,
    CompaniesListParams,
    CompaniesGetParams,
    DealsListParams,
    DealsGetParams,
    TicketsListParams,
    TicketsGetParams,
    SchemasListParams,
    ObjectsListParams,
    ObjectsGetParams
)

__all__ = ["HubspotConnector", "HubspotAuthConfig", "Contact", "PagingNext", "Paging", "ContactsList", "Company", "CompaniesList", "Deal", "DealsList", "Ticket", "TicketsList", "SchemaLabels", "Schema", "SchemasList", "CRMObject", "ObjectsList", "HubspotExecuteResult", "HubspotExecuteResultWithMeta", "SchemaLabels", "PagingNext", "ContactsListParams", "ContactsGetParams", "CompaniesListParams", "CompaniesGetParams", "DealsListParams", "DealsGetParams", "TicketsListParams", "TicketsGetParams", "SchemasListParams", "ObjectsListParams", "ObjectsGetParams"]
