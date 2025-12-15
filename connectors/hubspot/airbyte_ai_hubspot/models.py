"""
Pydantic models for hubspot connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class HubspotAuthConfig(BaseModel):
    """OAuth2 Authentication"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """Your HubSpot OAuth2 Client ID"""
    client_secret: str
    """Your HubSpot OAuth2 Client Secret"""
    refresh_token: str
    """Your HubSpot OAuth2 Refresh Token"""
    access_token: str
    """Your HubSpot OAuth2 Access Token (optional if refresh_token is provided)"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class ContactProperties(BaseModel):
    """Contact properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    createdate: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    firstname: Union[str | None, Any] = Field(default=None)
    hs_object_id: Union[str | None, Any] = Field(default=None)
    lastmodifieddate: Union[str | None, Any] = Field(default=None)
    lastname: Union[str | None, Any] = Field(default=None)

class Contact(BaseModel):
    """HubSpot contact object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    properties: Union[ContactProperties, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")
    archived: Union[bool, Any] = Field(default=None)
    archived_at: Union[str | None, Any] = Field(default=None, alias="archivedAt")
    properties_with_history: Union[dict[str, Any] | None, Any] = Field(default=None, alias="propertiesWithHistory")
    associations: Union[dict[str, Any] | None, Any] = Field(default=None)
    object_write_trace_id: Union[str | None, Any] = Field(default=None, alias="objectWriteTraceId")
    url: Union[str | None, Any] = Field(default=None)

class PagingNext(BaseModel):
    """Nested schema for Paging.next"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: Union[str, Any] = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""
    link: Union[str, Any] = Field(default=None, description="URL for next page")
    """URL for next page"""

class Paging(BaseModel):
    """Pagination information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: Union[PagingNext, Any] = Field(default=None)

class ContactsList(BaseModel):
    """Paginated list of contacts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[Contact], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)
    total: Union[int, Any] = Field(default=None)

class CompanyProperties(BaseModel):
    """Company properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    createdate: Union[str | None, Any] = Field(default=None)
    domain: Union[str | None, Any] = Field(default=None)
    hs_lastmodifieddate: Union[str | None, Any] = Field(default=None)
    hs_object_id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class Company(BaseModel):
    """HubSpot company object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    properties: Union[CompanyProperties, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")
    archived: Union[bool, Any] = Field(default=None)
    archived_at: Union[str | None, Any] = Field(default=None, alias="archivedAt")
    properties_with_history: Union[dict[str, Any] | None, Any] = Field(default=None, alias="propertiesWithHistory")
    associations: Union[dict[str, Any] | None, Any] = Field(default=None)
    object_write_trace_id: Union[str | None, Any] = Field(default=None, alias="objectWriteTraceId")
    url: Union[str | None, Any] = Field(default=None)

class CompaniesList(BaseModel):
    """Paginated list of companies"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[Company], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)
    total: Union[int, Any] = Field(default=None)

class DealProperties(BaseModel):
    """Deal properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Union[str | None, Any] = Field(default=None)
    closedate: Union[str | None, Any] = Field(default=None)
    createdate: Union[str | None, Any] = Field(default=None)
    dealname: Union[str | None, Any] = Field(default=None)
    dealstage: Union[str | None, Any] = Field(default=None)
    hs_lastmodifieddate: Union[str | None, Any] = Field(default=None)
    hs_object_id: Union[str | None, Any] = Field(default=None)
    pipeline: Union[str | None, Any] = Field(default=None)

class Deal(BaseModel):
    """HubSpot deal object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    properties: Union[DealProperties, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")
    archived: Union[bool, Any] = Field(default=None)
    archived_at: Union[str | None, Any] = Field(default=None, alias="archivedAt")
    properties_with_history: Union[dict[str, Any] | None, Any] = Field(default=None, alias="propertiesWithHistory")
    associations: Union[dict[str, Any] | None, Any] = Field(default=None)
    object_write_trace_id: Union[str | None, Any] = Field(default=None, alias="objectWriteTraceId")
    url: Union[str | None, Any] = Field(default=None)

class DealsList(BaseModel):
    """Paginated list of deals"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[Deal], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)
    total: Union[int, Any] = Field(default=None)

class TicketProperties(BaseModel):
    """Ticket properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: Union[str | None, Any] = Field(default=None)
    createdate: Union[str | None, Any] = Field(default=None)
    hs_lastmodifieddate: Union[str | None, Any] = Field(default=None)
    hs_object_id: Union[str | None, Any] = Field(default=None)
    hs_pipeline: Union[str | None, Any] = Field(default=None)
    hs_pipeline_stage: Union[str | None, Any] = Field(default=None)
    hs_ticket_category: Union[str | None, Any] = Field(default=None)
    hs_ticket_priority: Union[str | None, Any] = Field(default=None)
    subject: Union[str | None, Any] = Field(default=None)

class Ticket(BaseModel):
    """HubSpot ticket object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    properties: Union[TicketProperties, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")
    archived: Union[bool, Any] = Field(default=None)
    archived_at: Union[str | None, Any] = Field(default=None, alias="archivedAt")
    properties_with_history: Union[dict[str, Any] | None, Any] = Field(default=None, alias="propertiesWithHistory")
    associations: Union[dict[str, Any] | None, Any] = Field(default=None)
    object_write_trace_id: Union[str | None, Any] = Field(default=None, alias="objectWriteTraceId")
    url: Union[str | None, Any] = Field(default=None)

class TicketsList(BaseModel):
    """Paginated list of tickets"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[Ticket], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)
    total: Union[int, Any] = Field(default=None)

class SchemaLabels(BaseModel):
    """Display labels"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    singular: Union[str, Any] = Field(default=None)
    plural: Union[str, Any] = Field(default=None)

class SchemaAssociationsItem(BaseModel):
    """Nested schema for Schema.associations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_object_type_id: Union[str, Any] = Field(default=None, alias="fromObjectTypeId")
    to_object_type_id: Union[str, Any] = Field(default=None, alias="toObjectTypeId")
    name: Union[str, Any] = Field(default=None)
    cardinality: Union[str, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    inverse_cardinality: Union[str, Any] = Field(default=None, alias="inverseCardinality")
    has_user_enforced_max_to_object_ids: Union[bool, Any] = Field(default=None, alias="hasUserEnforcedMaxToObjectIds")
    has_user_enforced_max_from_object_ids: Union[bool, Any] = Field(default=None, alias="hasUserEnforcedMaxFromObjectIds")
    max_to_object_ids: Union[int, Any] = Field(default=None, alias="maxToObjectIds")
    max_from_object_ids: Union[int, Any] = Field(default=None, alias="maxFromObjectIds")
    created_at: Union[str | None, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str | None, Any] = Field(default=None, alias="updatedAt")

class SchemaPropertiesItemModificationmetadata(BaseModel):
    """Nested schema for SchemaPropertiesItem.modificationMetadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archivable: Union[bool, Any] = Field(default=None)
    read_only_definition: Union[bool, Any] = Field(default=None, alias="readOnlyDefinition")
    read_only_value: Union[bool, Any] = Field(default=None, alias="readOnlyValue")
    read_only_options: Union[bool, Any] = Field(default=None, alias="readOnlyOptions")

class SchemaPropertiesItem(BaseModel):
    """Nested schema for Schema.properties_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    label: Union[str, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)
    field_type: Union[str, Any] = Field(default=None, alias="fieldType")
    description: Union[str, Any] = Field(default=None)
    group_name: Union[str, Any] = Field(default=None, alias="groupName")
    display_order: Union[int, Any] = Field(default=None, alias="displayOrder")
    calculated: Union[bool, Any] = Field(default=None)
    external_options: Union[bool, Any] = Field(default=None, alias="externalOptions")
    archived: Union[bool, Any] = Field(default=None)
    has_unique_value: Union[bool, Any] = Field(default=None, alias="hasUniqueValue")
    hidden: Union[bool, Any] = Field(default=None)
    form_field: Union[bool, Any] = Field(default=None, alias="formField")
    data_sensitivity: Union[str, Any] = Field(default=None, alias="dataSensitivity")
    hubspot_defined: Union[bool, Any] = Field(default=None, alias="hubspotDefined")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    options: Union[list[Any], Any] = Field(default=None)
    created_user_id: Union[str, Any] = Field(default=None, alias="createdUserId")
    updated_user_id: Union[str, Any] = Field(default=None, alias="updatedUserId")
    show_currency_symbol: Union[bool, Any] = Field(default=None, alias="showCurrencySymbol")
    modification_metadata: Union[SchemaPropertiesItemModificationmetadata, Any] = Field(default=None, alias="modificationMetadata")

class Schema(BaseModel):
    """Custom object schema definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    labels: Union[SchemaLabels, Any] = Field(default=None)
    object_type_id: Union[str, Any] = Field(default=None, alias="objectTypeId")
    fully_qualified_name: Union[str, Any] = Field(default=None, alias="fullyQualifiedName")
    required_properties: Union[list[str], Any] = Field(default=None, alias="requiredProperties")
    searchable_properties: Union[list[str], Any] = Field(default=None, alias="searchableProperties")
    primary_display_property: Union[str, Any] = Field(default=None, alias="primaryDisplayProperty")
    secondary_display_properties: Union[list[str], Any] = Field(default=None, alias="secondaryDisplayProperties")
    description: Union[str | None, Any] = Field(default=None)
    allows_sensitive_properties: Union[bool, Any] = Field(default=None, alias="allowsSensitiveProperties")
    archived: Union[bool, Any] = Field(default=None)
    restorable: Union[bool, Any] = Field(default=None)
    meta_type: Union[str, Any] = Field(default=None, alias="metaType")
    created_by_user_id: Union[int, Any] = Field(default=None, alias="createdByUserId")
    updated_by_user_id: Union[int, Any] = Field(default=None, alias="updatedByUserId")
    properties: Union[list[SchemaPropertiesItem], Any] = Field(default=None)
    associations: Union[list[SchemaAssociationsItem], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")

class SchemasList(BaseModel):
    """List of custom object schemas"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[Schema], Any] = Field(default=None)

class CRMObjectProperties(BaseModel):
    """Object properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_createdate: Union[str | None, Any] = Field(default=None)
    hs_lastmodifieddate: Union[str | None, Any] = Field(default=None)
    hs_object_id: Union[str | None, Any] = Field(default=None)

class CRMObject(BaseModel):
    """Generic HubSpot CRM object (for custom objects)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    properties: Union[CRMObjectProperties, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str, Any] = Field(default=None, alias="updatedAt")
    archived: Union[bool, Any] = Field(default=None)
    archived_at: Union[str | None, Any] = Field(default=None, alias="archivedAt")
    properties_with_history: Union[dict[str, Any] | None, Any] = Field(default=None, alias="propertiesWithHistory")
    associations: Union[dict[str, Any] | None, Any] = Field(default=None)
    object_write_trace_id: Union[str | None, Any] = Field(default=None, alias="objectWriteTraceId")
    url: Union[str | None, Any] = Field(default=None)

class ObjectsList(BaseModel):
    """Paginated list of generic CRM objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: Union[list[CRMObject], Any] = Field(default=None)
    paging: Union[Paging, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str, Any] = Field(default=None)
    next_link: Union[str, Any] = Field(default=None)

class ContactsSearchResultMeta(BaseModel):
    """Metadata for contacts.search operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: Union[int, Any] = Field(default=None)
    next_cursor: Union[str, Any] = Field(default=None)
    next_link: Union[str, Any] = Field(default=None)

class CompaniesListResultMeta(BaseModel):
    """Metadata for companies.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str, Any] = Field(default=None)
    next_link: Union[str, Any] = Field(default=None)

class CompaniesSearchResultMeta(BaseModel):
    """Metadata for companies.search operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: Union[int, Any] = Field(default=None)
    next_cursor: Union[str, Any] = Field(default=None)
    next_link: Union[str, Any] = Field(default=None)

class DealsListResultMeta(BaseModel):
    """Metadata for deals.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str, Any] = Field(default=None)
    next_link: Union[str, Any] = Field(default=None)

class DealsSearchResultMeta(BaseModel):
    """Metadata for deals.search operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: Union[int, Any] = Field(default=None)
    next_cursor: Union[str, Any] = Field(default=None)
    next_link: Union[str, Any] = Field(default=None)

class TicketsListResultMeta(BaseModel):
    """Metadata for tickets.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str, Any] = Field(default=None)
    next_link: Union[str, Any] = Field(default=None)

class TicketsSearchResultMeta(BaseModel):
    """Metadata for tickets.search operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: Union[int, Any] = Field(default=None)
    next_cursor: Union[str, Any] = Field(default=None)
    next_link: Union[str, Any] = Field(default=None)

class ObjectsListResultMeta(BaseModel):
    """Metadata for objects.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str, Any] = Field(default=None)
    next_link: Union[str, Any] = Field(default=None)

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class HubspotExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class HubspotExecuteResultWithMeta(HubspotExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

ContactsListResult = HubspotExecuteResultWithMeta[list[Contact], ContactsListResultMeta]
"""Result type for contacts.list operation with data and metadata."""

ContactsSearchResult = HubspotExecuteResultWithMeta[list[Contact], ContactsSearchResultMeta]
"""Result type for contacts.search operation with data and metadata."""

CompaniesListResult = HubspotExecuteResultWithMeta[list[Company], CompaniesListResultMeta]
"""Result type for companies.list operation with data and metadata."""

CompaniesSearchResult = HubspotExecuteResultWithMeta[list[Company], CompaniesSearchResultMeta]
"""Result type for companies.search operation with data and metadata."""

DealsListResult = HubspotExecuteResultWithMeta[list[Deal], DealsListResultMeta]
"""Result type for deals.list operation with data and metadata."""

DealsSearchResult = HubspotExecuteResultWithMeta[list[Deal], DealsSearchResultMeta]
"""Result type for deals.search operation with data and metadata."""

TicketsListResult = HubspotExecuteResultWithMeta[list[Ticket], TicketsListResultMeta]
"""Result type for tickets.list operation with data and metadata."""

TicketsSearchResult = HubspotExecuteResultWithMeta[list[Ticket], TicketsSearchResultMeta]
"""Result type for tickets.search operation with data and metadata."""

SchemasListResult = HubspotExecuteResult[list[Schema]]
"""Result type for schemas.list operation."""

ObjectsListResult = HubspotExecuteResultWithMeta[list[CRMObject], ObjectsListResultMeta]
"""Result type for objects.list operation with data and metadata."""

