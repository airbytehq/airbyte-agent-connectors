"""
Pydantic models for hubspot connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
from typing import Optional

# Authentication configuration - multiple options available

class HubspotOauth2AuthConfig(BaseModel):
    """OAuth2"""

    model_config = ConfigDict(extra="forbid")

    client_id: Optional[str] = None
    """Your HubSpot OAuth2 Client ID"""
    client_secret: Optional[str] = None
    """Your HubSpot OAuth2 Client Secret"""
    refresh_token: str
    """Your HubSpot OAuth2 Refresh Token"""
    access_token: Optional[str] = None
    """Your HubSpot OAuth2 Access Token (optional if refresh_token is provided)"""

class HubspotPrivateAppAuthConfig(BaseModel):
    """Private App"""

    model_config = ConfigDict(extra="forbid")

    private_app_token: str
    """Access token from a HubSpot Private App"""

HubspotAuthConfig = HubspotOauth2AuthConfig | HubspotPrivateAppAuthConfig

# OAuth credential override

class HubspotOAuthCredentials(BaseModel):
    """HubSpot OAuth App Credentials - Provide your own HubSpot OAuth app credentials to override the default Airbyte-managed ones."""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """Your HubSpot OAuth app's client ID"""
    client_secret: str
    """Your HubSpot OAuth app's client secret"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class ContactProperties(BaseModel):
    """Contact properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    createdate: str | None | None = Field(default=None)
    email: str | None | None = Field(default=None)
    firstname: str | None | None = Field(default=None)
    hs_object_id: str | None | None = Field(default=None)
    lastmodifieddate: str | None | None = Field(default=None)
    lastname: str | None | None = Field(default=None)

class Contact(BaseModel):
    """HubSpot contact object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    properties: ContactProperties | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    archived: bool | None = Field(default=None)
    archived_at: str | None = Field(default=None, alias="archivedAt")
    properties_with_history: dict[str, Any] | None = Field(default=None, alias="propertiesWithHistory")
    associations: dict[str, Any] | None = Field(default=None)
    object_write_trace_id: str | None = Field(default=None, alias="objectWriteTraceId")
    url: str | None = Field(default=None)

class PagingNext(BaseModel):
    """Nested schema for Paging.next"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: str | None = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""
    link: str | None = Field(default=None, description="URL for next page")
    """URL for next page"""

class Paging(BaseModel):
    """Pagination information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: PagingNext | None = Field(default=None)

class ContactsList(BaseModel):
    """Paginated list of contacts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Contact] | None = Field(default=None)
    paging: Paging | None = Field(default=None)
    total: int | None = Field(default=None)

class CompanyProperties(BaseModel):
    """Company properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    createdate: str | None | None = Field(default=None)
    domain: str | None | None = Field(default=None)
    hs_lastmodifieddate: str | None | None = Field(default=None)
    hs_object_id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)

class Company(BaseModel):
    """HubSpot company object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    properties: CompanyProperties | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    archived: bool | None = Field(default=None)
    archived_at: str | None = Field(default=None, alias="archivedAt")
    properties_with_history: dict[str, Any] | None = Field(default=None, alias="propertiesWithHistory")
    associations: dict[str, Any] | None = Field(default=None)
    object_write_trace_id: str | None = Field(default=None, alias="objectWriteTraceId")
    url: str | None = Field(default=None)

class CompaniesList(BaseModel):
    """Paginated list of companies"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Company] | None = Field(default=None)
    paging: Paging | None = Field(default=None)
    total: int | None = Field(default=None)

class DealProperties(BaseModel):
    """Deal properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: str | None | None = Field(default=None)
    closedate: str | None | None = Field(default=None)
    createdate: str | None | None = Field(default=None)
    dealname: str | None | None = Field(default=None)
    dealstage: str | None | None = Field(default=None)
    hs_lastmodifieddate: str | None | None = Field(default=None)
    hs_object_id: str | None | None = Field(default=None)
    pipeline: str | None | None = Field(default=None)

class Deal(BaseModel):
    """HubSpot deal object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    properties: DealProperties | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    archived: bool | None = Field(default=None)
    archived_at: str | None = Field(default=None, alias="archivedAt")
    properties_with_history: dict[str, Any] | None = Field(default=None, alias="propertiesWithHistory")
    associations: dict[str, Any] | None = Field(default=None)
    object_write_trace_id: str | None = Field(default=None, alias="objectWriteTraceId")
    url: str | None = Field(default=None)

class DealsList(BaseModel):
    """Paginated list of deals"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Deal] | None = Field(default=None)
    paging: Paging | None = Field(default=None)
    total: int | None = Field(default=None)

class TicketProperties(BaseModel):
    """Ticket properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None | None = Field(default=None)
    createdate: str | None | None = Field(default=None)
    hs_lastmodifieddate: str | None | None = Field(default=None)
    hs_object_id: str | None | None = Field(default=None)
    hs_pipeline: str | None | None = Field(default=None)
    hs_pipeline_stage: str | None | None = Field(default=None)
    hs_ticket_category: str | None | None = Field(default=None)
    hs_ticket_priority: str | None | None = Field(default=None)
    subject: str | None | None = Field(default=None)

class Ticket(BaseModel):
    """HubSpot ticket object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    properties: TicketProperties | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    archived: bool | None = Field(default=None)
    archived_at: str | None = Field(default=None, alias="archivedAt")
    properties_with_history: dict[str, Any] | None = Field(default=None, alias="propertiesWithHistory")
    associations: dict[str, Any] | None = Field(default=None)
    object_write_trace_id: str | None = Field(default=None, alias="objectWriteTraceId")
    url: str | None = Field(default=None)

class TicketsList(BaseModel):
    """Paginated list of tickets"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Ticket] | None = Field(default=None)
    paging: Paging | None = Field(default=None)
    total: int | None = Field(default=None)

class SchemaLabels(BaseModel):
    """Display labels"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    singular: str | None = Field(default=None)
    plural: str | None = Field(default=None)

class SchemaPropertiesItemModificationmetadata(BaseModel):
    """Nested schema for SchemaPropertiesItem.modificationMetadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archivable: bool | None = Field(default=None)
    read_only_definition: bool | None = Field(default=None, alias="readOnlyDefinition")
    read_only_value: bool | None = Field(default=None, alias="readOnlyValue")
    read_only_options: bool | None = Field(default=None, alias="readOnlyOptions")

class SchemaPropertiesItem(BaseModel):
    """Nested schema for Schema.properties_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    label: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    field_type: str | None = Field(default=None, alias="fieldType")
    description: str | None = Field(default=None)
    group_name: str | None = Field(default=None, alias="groupName")
    display_order: int | None = Field(default=None, alias="displayOrder")
    calculated: bool | None = Field(default=None)
    external_options: bool | None = Field(default=None, alias="externalOptions")
    archived: bool | None = Field(default=None)
    has_unique_value: bool | None = Field(default=None, alias="hasUniqueValue")
    hidden: bool | None = Field(default=None)
    form_field: bool | None = Field(default=None, alias="formField")
    data_sensitivity: str | None = Field(default=None, alias="dataSensitivity")
    hubspot_defined: bool | None = Field(default=None, alias="hubspotDefined")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    created_at: str | None = Field(default=None, alias="createdAt")
    options: list[Any] | None = Field(default=None)
    created_user_id: str | None = Field(default=None, alias="createdUserId")
    updated_user_id: str | None = Field(default=None, alias="updatedUserId")
    show_currency_symbol: bool | None = Field(default=None, alias="showCurrencySymbol")
    modification_metadata: SchemaPropertiesItemModificationmetadata | None = Field(default=None, alias="modificationMetadata")

class SchemaAssociationsItem(BaseModel):
    """Nested schema for Schema.associations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_object_type_id: str | None = Field(default=None, alias="fromObjectTypeId")
    to_object_type_id: str | None = Field(default=None, alias="toObjectTypeId")
    name: str | None = Field(default=None)
    cardinality: str | None = Field(default=None)
    id: str | None = Field(default=None)
    inverse_cardinality: str | None = Field(default=None, alias="inverseCardinality")
    has_user_enforced_max_to_object_ids: bool | None = Field(default=None, alias="hasUserEnforcedMaxToObjectIds")
    has_user_enforced_max_from_object_ids: bool | None = Field(default=None, alias="hasUserEnforcedMaxFromObjectIds")
    max_to_object_ids: int | None = Field(default=None, alias="maxToObjectIds")
    max_from_object_ids: int | None = Field(default=None, alias="maxFromObjectIds")
    created_at: str | None | None = Field(default=None, alias="createdAt")
    updated_at: str | None | None = Field(default=None, alias="updatedAt")

class Schema(BaseModel):
    """Custom object schema definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    labels: SchemaLabels | None = Field(default=None)
    object_type_id: str | None = Field(default=None, alias="objectTypeId")
    fully_qualified_name: str | None = Field(default=None, alias="fullyQualifiedName")
    required_properties: list[str] | None = Field(default=None, alias="requiredProperties")
    searchable_properties: list[str] | None = Field(default=None, alias="searchableProperties")
    primary_display_property: str | None = Field(default=None, alias="primaryDisplayProperty")
    secondary_display_properties: list[str] | None = Field(default=None, alias="secondaryDisplayProperties")
    description: str | None = Field(default=None)
    allows_sensitive_properties: bool | None = Field(default=None, alias="allowsSensitiveProperties")
    archived: bool | None = Field(default=None)
    restorable: bool | None = Field(default=None)
    meta_type: str | None = Field(default=None, alias="metaType")
    created_by_user_id: int | None = Field(default=None, alias="createdByUserId")
    updated_by_user_id: int | None = Field(default=None, alias="updatedByUserId")
    properties: list[SchemaPropertiesItem] | None = Field(default=None)
    associations: list[SchemaAssociationsItem] | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class SchemasList(BaseModel):
    """List of custom object schemas"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Schema] | None = Field(default=None)

class CRMObjectProperties(BaseModel):
    """Object properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_createdate: str | None | None = Field(default=None)
    hs_lastmodifieddate: str | None | None = Field(default=None)
    hs_object_id: str | None | None = Field(default=None)

class CRMObject(BaseModel):
    """Generic HubSpot CRM object (for custom objects)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    properties: CRMObjectProperties | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    archived: bool | None = Field(default=None)
    archived_at: str | None = Field(default=None, alias="archivedAt")
    properties_with_history: dict[str, Any] | None = Field(default=None, alias="propertiesWithHistory")
    associations: dict[str, Any] | None = Field(default=None)
    object_write_trace_id: str | None = Field(default=None, alias="objectWriteTraceId")
    url: str | None = Field(default=None)

class ObjectsList(BaseModel):
    """Paginated list of generic CRM objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[CRMObject] | None = Field(default=None)
    paging: Paging | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class ContactsApiSearchResultMeta(BaseModel):
    """Metadata for contacts.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: int | None = Field(default=None)
    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class CompaniesListResultMeta(BaseModel):
    """Metadata for companies.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class CompaniesApiSearchResultMeta(BaseModel):
    """Metadata for companies.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: int | None = Field(default=None)
    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class DealsListResultMeta(BaseModel):
    """Metadata for deals.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class DealsApiSearchResultMeta(BaseModel):
    """Metadata for deals.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: int | None = Field(default=None)
    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class TicketsListResultMeta(BaseModel):
    """Metadata for tickets.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class TicketsApiSearchResultMeta(BaseModel):
    """Metadata for tickets.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: int | None = Field(default=None)
    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class ObjectsListResultMeta(BaseModel):
    """Metadata for objects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class HubspotCheckResult(BaseModel):
    """Result of a health check operation.

    Returned by the check() method to indicate connectivity and credential status.
    """
    model_config = ConfigDict(extra="forbid")

    status: str
    """Health check status: 'healthy' or 'unhealthy'."""
    error: str | None = None
    """Error message if status is 'unhealthy', None otherwise."""
    checked_entity: str | None = None
    """Entity name used for the health check."""
    checked_action: str | None = None
    """Action name used for the health check."""


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

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class CompaniesSearchData(BaseModel):
    """Search result data for companies entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Indicates whether the company has been deleted and moved to the recycling bin"""
    contacts: list[Any] | None = None
    """Associated contact records linked to this company"""
    created_at: str | None = None
    """Timestamp when the company record was created"""
    id: str | None = None
    """Unique identifier for the company record"""
    properties: dict[str, Any] = None
    """Object containing all property values for the company"""
    updated_at: str | None = None
    """Timestamp when the company record was last modified"""


class ContactsSearchData(BaseModel):
    """Search result data for contacts entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Boolean flag indicating whether the contact has been archived or deleted."""
    companies: list[Any] | None = None
    """Associated company records linked to this contact."""
    created_at: str | None = None
    """Timestamp indicating when the contact was first created in the system."""
    id: str | None = None
    """Unique identifier for the contact record."""
    properties: dict[str, Any] = None
    """Key-value object storing all contact properties and their values."""
    updated_at: str | None = None
    """Timestamp indicating when the contact record was last modified."""


class DealsSearchData(BaseModel):
    """Search result data for deals entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Indicates whether the deal has been deleted and moved to the recycling bin"""
    companies: list[Any] | None = None
    """Collection of company records associated with the deal"""
    contacts: list[Any] | None = None
    """Collection of contact records associated with the deal"""
    created_at: str | None = None
    """Timestamp when the deal record was originally created"""
    id: str | None = None
    """Unique identifier for the deal record"""
    line_items: list[Any] | None = None
    """Collection of product line items associated with the deal"""
    properties: dict[str, Any] = None
    """Key-value object containing all deal properties and custom fields"""
    updated_at: str | None = None
    """Timestamp when the deal record was last modified"""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchMeta(BaseModel):
    """Pagination metadata for search responses."""
    model_config = ConfigDict(extra="allow")

    has_more: bool = False
    """Whether more results are available."""
    cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed records."""
    model_config = ConfigDict(extra="allow")

    data: list[D] = Field(default_factory=list)
    """List of matching records."""
    meta: AirbyteSearchMeta = Field(default_factory=AirbyteSearchMeta)
    """Pagination metadata."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

CompaniesSearchResult = AirbyteSearchResult[CompaniesSearchData]
"""Search result type for companies entity."""

ContactsSearchResult = AirbyteSearchResult[ContactsSearchData]
"""Search result type for contacts entity."""

DealsSearchResult = AirbyteSearchResult[DealsSearchData]
"""Search result type for deals entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

ContactsListResult = HubspotExecuteResultWithMeta[list[Contact], ContactsListResultMeta]
"""Result type for contacts.list operation with data and metadata."""

ContactsApiSearchResult = HubspotExecuteResultWithMeta[list[Contact], ContactsApiSearchResultMeta]
"""Result type for contacts.api_search operation with data and metadata."""

CompaniesListResult = HubspotExecuteResultWithMeta[list[Company], CompaniesListResultMeta]
"""Result type for companies.list operation with data and metadata."""

CompaniesApiSearchResult = HubspotExecuteResultWithMeta[list[Company], CompaniesApiSearchResultMeta]
"""Result type for companies.api_search operation with data and metadata."""

DealsListResult = HubspotExecuteResultWithMeta[list[Deal], DealsListResultMeta]
"""Result type for deals.list operation with data and metadata."""

DealsApiSearchResult = HubspotExecuteResultWithMeta[list[Deal], DealsApiSearchResultMeta]
"""Result type for deals.api_search operation with data and metadata."""

TicketsListResult = HubspotExecuteResultWithMeta[list[Ticket], TicketsListResultMeta]
"""Result type for tickets.list operation with data and metadata."""

TicketsApiSearchResult = HubspotExecuteResultWithMeta[list[Ticket], TicketsApiSearchResultMeta]
"""Result type for tickets.api_search operation with data and metadata."""

SchemasListResult = HubspotExecuteResult[list[Schema]]
"""Result type for schemas.list operation."""

ObjectsListResult = HubspotExecuteResultWithMeta[list[CRMObject], ObjectsListResultMeta]
"""Result type for objects.list operation with data and metadata."""

