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

class SchemaLabels(BaseModel):
    """Display labels"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    singular: str | None = Field(default=None)
    plural: str | None = Field(default=None)

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

class ContactCreateParamsProperties(BaseModel):
    """Contact properties to set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str = Field(description="Contact email address (required, used as unique identifier)")
    """Contact email address (required, used as unique identifier)"""
    firstname: str | None = Field(default=None, description="Contact first name")
    """Contact first name"""
    lastname: str | None = Field(default=None, description="Contact last name")
    """Contact last name"""
    phone: str | None = Field(default=None, description="Contact phone number")
    """Contact phone number"""
    company: str | None = Field(default=None, description="Company name associated with the contact")
    """Company name associated with the contact"""
    website: str | None = Field(default=None, description="Contact website URL")
    """Contact website URL"""
    lifecyclestage: str | None = Field(default=None, description="Lifecycle stage (e.g., subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, evangelist, other)")
    """Lifecycle stage (e.g., subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, evangelist, other)"""
    jobtitle: str | None = Field(default=None, description="Contact job title")
    """Contact job title"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this contact")
    """ID of the HubSpot owner to assign to this contact"""

class ContactCreateParams(BaseModel):
    """Parameters for creating a new contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: ContactCreateParamsProperties

class ContactUpdateParamsProperties(BaseModel):
    """Contact properties to update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None = Field(default=None, description="Contact email address")
    """Contact email address"""
    firstname: str | None = Field(default=None, description="Contact first name")
    """Contact first name"""
    lastname: str | None = Field(default=None, description="Contact last name")
    """Contact last name"""
    phone: str | None = Field(default=None, description="Contact phone number")
    """Contact phone number"""
    company: str | None = Field(default=None, description="Company name associated with the contact")
    """Company name associated with the contact"""
    website: str | None = Field(default=None, description="Contact website URL")
    """Contact website URL"""
    lifecyclestage: str | None = Field(default=None, description="Lifecycle stage (e.g., subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, evangelist, other)")
    """Lifecycle stage (e.g., subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, evangelist, other)"""
    jobtitle: str | None = Field(default=None, description="Contact job title")
    """Contact job title"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this contact")
    """ID of the HubSpot owner to assign to this contact"""

class ContactUpdateParams(BaseModel):
    """Parameters for updating an existing contact. Only provided properties will be updated."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: ContactUpdateParamsProperties

class CompanyCreateParamsProperties(BaseModel):
    """Company properties to set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str = Field(description="Company name (required)")
    """Company name (required)"""
    domain: str | None = Field(default=None, description="Company domain name (e.g., example.com)")
    """Company domain name (e.g., example.com)"""
    description: str | None = Field(default=None, description="Company description")
    """Company description"""
    phone: str | None = Field(default=None, description="Company phone number")
    """Company phone number"""
    industry: str | None = Field(default=None, description="Company industry (e.g., COMPUTER_SOFTWARE, INFORMATION_TECHNOLOGY_AND_SERVICES, INTERNET, FINANCIAL_SERVICES, MARKETING_AND_ADVERTISING, EDUCATION_MANAGEMENT)")
    """Company industry (e.g., COMPUTER_SOFTWARE, INFORMATION_TECHNOLOGY_AND_SERVICES, INTERNET, FINANCIAL_SERVICES, MARKETING_AND_ADVERTISING, EDUCATION_MANAGEMENT)"""
    city: str | None = Field(default=None, description="Company city")
    """Company city"""
    state: str | None = Field(default=None, description="Company state/region")
    """Company state/region"""
    country: str | None = Field(default=None, description="Company country")
    """Company country"""
    zip: str | None = Field(default=None, description="Company postal/zip code")
    """Company postal/zip code"""
    numberofemployees: str | None = Field(default=None, description="Number of employees")
    """Number of employees"""
    annualrevenue: str | None = Field(default=None, description="Annual revenue")
    """Annual revenue"""
    lifecyclestage: str | None = Field(default=None, description="Lifecycle stage (e.g., subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, evangelist, other)")
    """Lifecycle stage (e.g., subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, evangelist, other)"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this company")
    """ID of the HubSpot owner to assign to this company"""
    website: str | None = Field(default=None, description="Company website URL")
    """Company website URL"""

class CompanyCreateParams(BaseModel):
    """Parameters for creating a new company"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: CompanyCreateParamsProperties

class CompanyUpdateParamsProperties(BaseModel):
    """Company properties to update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="Company name")
    """Company name"""
    domain: str | None = Field(default=None, description="Company domain name (e.g., example.com)")
    """Company domain name (e.g., example.com)"""
    description: str | None = Field(default=None, description="Company description")
    """Company description"""
    phone: str | None = Field(default=None, description="Company phone number")
    """Company phone number"""
    industry: str | None = Field(default=None, description="Company industry (e.g., COMPUTER_SOFTWARE, INFORMATION_TECHNOLOGY_AND_SERVICES, INTERNET, FINANCIAL_SERVICES, MARKETING_AND_ADVERTISING, EDUCATION_MANAGEMENT)")
    """Company industry (e.g., COMPUTER_SOFTWARE, INFORMATION_TECHNOLOGY_AND_SERVICES, INTERNET, FINANCIAL_SERVICES, MARKETING_AND_ADVERTISING, EDUCATION_MANAGEMENT)"""
    city: str | None = Field(default=None, description="Company city")
    """Company city"""
    state: str | None = Field(default=None, description="Company state/region")
    """Company state/region"""
    country: str | None = Field(default=None, description="Company country")
    """Company country"""
    zip: str | None = Field(default=None, description="Company postal/zip code")
    """Company postal/zip code"""
    numberofemployees: str | None = Field(default=None, description="Number of employees")
    """Number of employees"""
    annualrevenue: str | None = Field(default=None, description="Annual revenue")
    """Annual revenue"""
    lifecyclestage: str | None = Field(default=None, description="Lifecycle stage (e.g., subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, evangelist, other)")
    """Lifecycle stage (e.g., subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, evangelist, other)"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this company")
    """ID of the HubSpot owner to assign to this company"""
    website: str | None = Field(default=None, description="Company website URL")
    """Company website URL"""

class CompanyUpdateParams(BaseModel):
    """Parameters for updating an existing company. Only provided properties will be updated."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: CompanyUpdateParamsProperties

class DealCreateParamsProperties(BaseModel):
    """Deal properties to set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    dealname: str = Field(description="Deal name (required)")
    """Deal name (required)"""
    amount: str | None = Field(default=None, description="Deal amount")
    """Deal amount"""
    dealstage: str | None = Field(default=None, description="Deal stage ID (e.g., appointmentscheduled, qualifiedtobuy, presentationscheduled, decisionmakerboughtin, contractsent, closedwon, closedlost)")
    """Deal stage ID (e.g., appointmentscheduled, qualifiedtobuy, presentationscheduled, decisionmakerboughtin, contractsent, closedwon, closedlost)"""
    pipeline: str | None = Field(default=None, description="Deal pipeline ID (defaults to the default pipeline)")
    """Deal pipeline ID (defaults to the default pipeline)"""
    closedate: str | None = Field(default=None, description="Expected close date (ISO 8601 format, e.g., 2024-12-31T00:00:00.000Z)")
    """Expected close date (ISO 8601 format, e.g., 2024-12-31T00:00:00.000Z)"""
    dealtype: str | None = Field(default=None, description="Deal type (e.g., newbusiness, existingbusiness)")
    """Deal type (e.g., newbusiness, existingbusiness)"""
    description: str | None = Field(default=None, description="Deal description")
    """Deal description"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this deal")
    """ID of the HubSpot owner to assign to this deal"""

class DealCreateParams(BaseModel):
    """Parameters for creating a new deal"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: DealCreateParamsProperties

class DealUpdateParamsProperties(BaseModel):
    """Deal properties to update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    dealname: str | None = Field(default=None, description="Deal name")
    """Deal name"""
    amount: str | None = Field(default=None, description="Deal amount")
    """Deal amount"""
    dealstage: str | None = Field(default=None, description="Deal stage ID (e.g., appointmentscheduled, qualifiedtobuy, presentationscheduled, decisionmakerboughtin, contractsent, closedwon, closedlost)")
    """Deal stage ID (e.g., appointmentscheduled, qualifiedtobuy, presentationscheduled, decisionmakerboughtin, contractsent, closedwon, closedlost)"""
    pipeline: str | None = Field(default=None, description="Deal pipeline ID")
    """Deal pipeline ID"""
    closedate: str | None = Field(default=None, description="Expected close date (ISO 8601 format, e.g., 2024-12-31T00:00:00.000Z)")
    """Expected close date (ISO 8601 format, e.g., 2024-12-31T00:00:00.000Z)"""
    dealtype: str | None = Field(default=None, description="Deal type (e.g., newbusiness, existingbusiness)")
    """Deal type (e.g., newbusiness, existingbusiness)"""
    description: str | None = Field(default=None, description="Deal description")
    """Deal description"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this deal")
    """ID of the HubSpot owner to assign to this deal"""

class DealUpdateParams(BaseModel):
    """Parameters for updating an existing deal. Only provided properties will be updated."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: DealUpdateParamsProperties

class TicketCreateParamsProperties(BaseModel):
    """Ticket properties to set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    subject: str = Field(description="Ticket subject line (required)")
    """Ticket subject line (required)"""
    content: str | None = Field(default=None, description="Ticket description/content")
    """Ticket description/content"""
    hs_pipeline: str = Field(description="Ticket pipeline ID (required, use '0' for default pipeline)")
    """Ticket pipeline ID (required, use '0' for default pipeline)"""
    hs_pipeline_stage: str = Field(description="Pipeline stage ID (required, e.g., '1' for New in the default pipeline)")
    """Pipeline stage ID (required, e.g., '1' for New in the default pipeline)"""
    hs_ticket_priority: str | None = Field(default=None, description="Ticket priority (e.g., LOW, MEDIUM, HIGH)")
    """Ticket priority (e.g., LOW, MEDIUM, HIGH)"""
    hs_ticket_category: str | None = Field(default=None, description="Ticket category")
    """Ticket category"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this ticket")
    """ID of the HubSpot owner to assign to this ticket"""

class TicketCreateParams(BaseModel):
    """Parameters for creating a new support ticket"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: TicketCreateParamsProperties

class TicketUpdateParamsProperties(BaseModel):
    """Ticket properties to update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    subject: str | None = Field(default=None, description="Ticket subject line")
    """Ticket subject line"""
    content: str | None = Field(default=None, description="Ticket description/content")
    """Ticket description/content"""
    hs_pipeline: str | None = Field(default=None, description="Ticket pipeline ID")
    """Ticket pipeline ID"""
    hs_pipeline_stage: str | None = Field(default=None, description="Pipeline stage ID")
    """Pipeline stage ID"""
    hs_ticket_priority: str | None = Field(default=None, description="Ticket priority (e.g., LOW, MEDIUM, HIGH)")
    """Ticket priority (e.g., LOW, MEDIUM, HIGH)"""
    hs_ticket_category: str | None = Field(default=None, description="Ticket category")
    """Ticket category"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this ticket")
    """ID of the HubSpot owner to assign to this ticket"""

class TicketUpdateParams(BaseModel):
    """Parameters for updating an existing ticket. Only provided properties will be updated."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: TicketUpdateParamsProperties

class AssociationResultResultsItemTo(BaseModel):
    """The target record of the association"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="ID of the target record")
    """ID of the target record"""

class AssociationResultResultsItemFrom(BaseModel):
    """The source record of the association"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="ID of the source record")
    """ID of the source record"""

class AssociationResultResultsItemAssociationspec(BaseModel):
    """Details about the association type"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    association_category: str | None = Field(default=None, alias="associationCategory", description="Category of the association (HUBSPOT_DEFINED or USER_DEFINED)")
    """Category of the association (HUBSPOT_DEFINED or USER_DEFINED)"""
    association_type_id: int | None = Field(default=None, alias="associationTypeId", description="Numeric ID of the association type")
    """Numeric ID of the association type"""

class AssociationResultResultsItem(BaseModel):
    """Nested schema for AssociationResult.results_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: AssociationResultResultsItemFrom | None = Field(default=None, alias="from", description="The source record of the association")
    """The source record of the association"""
    to: AssociationResultResultsItemTo | None = Field(default=None, description="The target record of the association")
    """The target record of the association"""
    association_spec: AssociationResultResultsItemAssociationspec | None = Field(default=None, alias="associationSpec", description="Details about the association type")
    """Details about the association type"""

class AssociationResult(BaseModel):
    """Result of creating an association between two CRM records"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    status: str | None = Field(default=None)
    results: list[AssociationResultResultsItem] | None = Field(default=None)
    started_at: str | None = Field(default=None, alias="startedAt")
    completed_at: str | None = Field(default=None, alias="completedAt")
    requested_at: str | None = Field(default=None, alias="requestedAt")

class AssociationLabeledParams(BaseModel):
    """Array of association type specifications. Each item defines a labeled association type
to apply between the two records. Multiple labels can be set in a single call.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pass

class AssociationListResultResultsItemAssociationtypesItem(BaseModel):
    """Nested schema for AssociationListResultResultsItem.associationTypes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    category: str | None = Field(default=None, description="Category of the association (HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED)")
    """Category of the association (HUBSPOT_DEFINED, USER_DEFINED, or INTEGRATOR_DEFINED)"""
    type_id: int | None = Field(default=None, alias="typeId", description="Numeric identifier for the association type")
    """Numeric identifier for the association type"""
    label: str | None | None = Field(default=None, description="Human-readable label for the association type (e.g., \"Primary Company\")")
    """Human-readable label for the association type (e.g., "Primary Company")"""

class AssociationListResultResultsItem(BaseModel):
    """Nested schema for AssociationListResult.results_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    to_object_id: Any | None = Field(default=None, alias="toObjectId", description="ID of the associated target record")
    """ID of the associated target record"""
    association_types: list[AssociationListResultResultsItemAssociationtypesItem] | None = Field(default=None, alias="associationTypes", description="List of association types linking the two records")
    """List of association types linking the two records"""

class AssociationListResultPagingNext(BaseModel):
    """Cursor for the next page of results"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: str | None = Field(default=None, description="Paging cursor token for retrieving the next page")
    """Paging cursor token for retrieving the next page"""
    link: str | None = Field(default=None, description="URL for retrieving the next page of results")
    """URL for retrieving the next page of results"""

class AssociationListResultPaging(BaseModel):
    """Pagination information for retrieving additional results"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: AssociationListResultPagingNext | None = Field(default=None, description="Cursor for the next page of results")
    """Cursor for the next page of results"""
    additional_properties: Any | None = Field(default=None, alias="additionalProperties")

class AssociationListResult(BaseModel):
    """Paginated list of associations for a CRM record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[AssociationListResultResultsItem] | None = Field(default=None)
    paging: AssociationListResultPaging | None = Field(default=None)

class NoteProperties(BaseModel):
    """Note properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_note_body: str | None | None = Field(default=None, description="The body content of the note (supports HTML)")
    """The body content of the note (supports HTML)"""
    hs_timestamp: str | None | None = Field(default=None, description="Timestamp when the note activity occurred")
    """Timestamp when the note activity occurred"""
    hubspot_owner_id: str | None | None = Field(default=None, description="ID of the note owner")
    """ID of the note owner"""
    hs_object_id: str | None | None = Field(default=None, description="HubSpot object ID")
    """HubSpot object ID"""
    hs_createdate: str | None | None = Field(default=None, description="Date the note was created")
    """Date the note was created"""
    hs_lastmodifieddate: str | None | None = Field(default=None, description="Last modified date")
    """Last modified date"""

class Note(BaseModel):
    """HubSpot note/engagement object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    properties: NoteProperties | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    archived: bool | None = Field(default=None)
    archived_at: str | None = Field(default=None, alias="archivedAt")
    associations: dict[str, Any] | None = Field(default=None)

class NoteCreateParamsProperties(BaseModel):
    """Note properties to set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_note_body: str = Field(description="The body content of the note (supports HTML)")
    """The body content of the note (supports HTML)"""
    hs_timestamp: str = Field(description="Required. Timestamp when the note activity occurred (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one.")
    """Required. Timestamp when the note activity occurred (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one."""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this note")
    """ID of the HubSpot owner to assign to this note"""

class NoteCreateParamsAssociationsItemTypesItem(BaseModel):
    """Nested schema for NoteCreateParamsAssociationsItem.types_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    association_category: str | None = Field(default=None, alias="associationCategory", description="Association category (e.g., HUBSPOT_DEFINED)")
    """Association category (e.g., HUBSPOT_DEFINED)"""
    association_type_id: int | None = Field(default=None, alias="associationTypeId", description="Association type ID (e.g., 202 for note-to-contact, 190 for note-to-company, 214 for note-to-deal, 18 for note-to-ticket)")
    """Association type ID (e.g., 202 for note-to-contact, 190 for note-to-company, 214 for note-to-deal, 18 for note-to-ticket)"""

class NoteCreateParamsAssociationsItemTo(BaseModel):
    """Nested schema for NoteCreateParamsAssociationsItem.to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="ID of the record to associate with")
    """ID of the record to associate with"""

class NoteCreateParamsAssociationsItem(BaseModel):
    """Nested schema for NoteCreateParams.associations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    to: NoteCreateParamsAssociationsItemTo | None = Field(default=None)
    types: list[NoteCreateParamsAssociationsItemTypesItem] | None = Field(default=None)

class NoteCreateParams(BaseModel):
    """Parameters for creating a new note"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: NoteCreateParamsProperties
    associations: list[NoteCreateParamsAssociationsItem] | None = Field(default=None)

class NoteUpdateParamsProperties(BaseModel):
    """Note properties to update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_note_body: str | None = Field(default=None, description="The body content of the note (supports HTML)")
    """The body content of the note (supports HTML)"""
    hs_timestamp: str | None = Field(default=None, description="Timestamp when the note activity occurred")
    """Timestamp when the note activity occurred"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this note")
    """ID of the HubSpot owner to assign to this note"""

class NoteUpdateParams(BaseModel):
    """Parameters for updating an existing note. Only provided properties will be updated."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: NoteUpdateParamsProperties

class NotesList(BaseModel):
    """Paginated list of notes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Note] | None = Field(default=None)
    paging: Paging | None = Field(default=None)
    total: int | None = Field(default=None)

class CallProperties(BaseModel):
    """Call properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_call_body: str | None | None = Field(default=None, description="Description or notes about the call")
    """Description or notes about the call"""
    hs_call_direction: str | None | None = Field(default=None, description="Direction of the call (INBOUND or OUTBOUND)")
    """Direction of the call (INBOUND or OUTBOUND)"""
    hs_call_disposition: str | None | None = Field(default=None, description="The outcome of the call (e.g., connected, no answer, busy, left voicemail)")
    """The outcome of the call (e.g., connected, no answer, busy, left voicemail)"""
    hs_call_duration: str | None | None = Field(default=None, description="Duration of the call in milliseconds")
    """Duration of the call in milliseconds"""
    hs_call_from_number: str | None | None = Field(default=None, description="Phone number the call was made from")
    """Phone number the call was made from"""
    hs_call_to_number: str | None | None = Field(default=None, description="Phone number the call was made to")
    """Phone number the call was made to"""
    hs_call_status: str | None | None = Field(default=None, description="Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER, FAILED, CANCELED, CONNECTING, RINGING, IN_PROGRESS)")
    """Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER, FAILED, CANCELED, CONNECTING, RINGING, IN_PROGRESS)"""
    hs_call_title: str | None | None = Field(default=None, description="Title or subject of the call")
    """Title or subject of the call"""
    hs_timestamp: str | None | None = Field(default=None, description="Timestamp when the call activity occurred")
    """Timestamp when the call activity occurred"""
    hubspot_owner_id: str | None | None = Field(default=None, description="ID of the call owner")
    """ID of the call owner"""
    hs_object_id: str | None | None = Field(default=None, description="HubSpot object ID")
    """HubSpot object ID"""
    hs_createdate: str | None | None = Field(default=None, description="Date the call was created")
    """Date the call was created"""
    hs_lastmodifieddate: str | None | None = Field(default=None, description="Last modified date")
    """Last modified date"""

class Call(BaseModel):
    """HubSpot call engagement object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    properties: CallProperties | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    archived: bool | None = Field(default=None)
    archived_at: str | None = Field(default=None, alias="archivedAt")
    associations: dict[str, Any] | None = Field(default=None)

class CallCreateParamsProperties(BaseModel):
    """Call properties to set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_call_body: str | None = Field(default=None, description="Description or notes about the call")
    """Description or notes about the call"""
    hs_call_direction: str | None = Field(default=None, description="Direction of the call (INBOUND or OUTBOUND)")
    """Direction of the call (INBOUND or OUTBOUND)"""
    hs_call_disposition: str | None = Field(default=None, description="The outcome of the call (e.g., connected, no answer, busy, left voicemail)")
    """The outcome of the call (e.g., connected, no answer, busy, left voicemail)"""
    hs_call_duration: str | None = Field(default=None, description="Duration of the call in milliseconds")
    """Duration of the call in milliseconds"""
    hs_call_from_number: str | None = Field(default=None, description="Phone number the call was made from")
    """Phone number the call was made from"""
    hs_call_to_number: str | None = Field(default=None, description="Phone number the call was made to")
    """Phone number the call was made to"""
    hs_call_status: str | None = Field(default=None, description="Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER, FAILED, CANCELED)")
    """Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER, FAILED, CANCELED)"""
    hs_call_title: str | None = Field(default=None, description="Title or subject of the call")
    """Title or subject of the call"""
    hs_timestamp: str = Field(description="Required. Timestamp when the call activity occurred (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one.")
    """Required. Timestamp when the call activity occurred (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one."""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this call")
    """ID of the HubSpot owner to assign to this call"""

class CallCreateParamsAssociationsItemTypesItem(BaseModel):
    """Nested schema for CallCreateParamsAssociationsItem.types_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    association_category: str | None = Field(default=None, alias="associationCategory", description="Association category (e.g., HUBSPOT_DEFINED)")
    """Association category (e.g., HUBSPOT_DEFINED)"""
    association_type_id: int | None = Field(default=None, alias="associationTypeId", description="Association type ID (e.g., 194 for call-to-contact, 182 for call-to-company, 206 for call-to-deal, 220 for call-to-ticket)")
    """Association type ID (e.g., 194 for call-to-contact, 182 for call-to-company, 206 for call-to-deal, 220 for call-to-ticket)"""

class CallCreateParamsAssociationsItemTo(BaseModel):
    """Nested schema for CallCreateParamsAssociationsItem.to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="ID of the record to associate with")
    """ID of the record to associate with"""

class CallCreateParamsAssociationsItem(BaseModel):
    """Nested schema for CallCreateParams.associations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    to: CallCreateParamsAssociationsItemTo | None = Field(default=None)
    types: list[CallCreateParamsAssociationsItemTypesItem] | None = Field(default=None)

class CallCreateParams(BaseModel):
    """Parameters for creating a new call"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: CallCreateParamsProperties
    associations: list[CallCreateParamsAssociationsItem] | None = Field(default=None)

class CallUpdateParamsProperties(BaseModel):
    """Call properties to update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_call_body: str | None = Field(default=None, description="Description or notes about the call")
    """Description or notes about the call"""
    hs_call_direction: str | None = Field(default=None, description="Direction of the call (INBOUND or OUTBOUND)")
    """Direction of the call (INBOUND or OUTBOUND)"""
    hs_call_disposition: str | None = Field(default=None, description="The outcome of the call")
    """The outcome of the call"""
    hs_call_duration: str | None = Field(default=None, description="Duration of the call in milliseconds")
    """Duration of the call in milliseconds"""
    hs_call_from_number: str | None = Field(default=None, description="Phone number the call was made from")
    """Phone number the call was made from"""
    hs_call_to_number: str | None = Field(default=None, description="Phone number the call was made to")
    """Phone number the call was made to"""
    hs_call_status: str | None = Field(default=None, description="Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER)")
    """Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER)"""
    hs_call_title: str | None = Field(default=None, description="Title or subject of the call")
    """Title or subject of the call"""
    hs_timestamp: str | None = Field(default=None, description="Timestamp when the call activity occurred")
    """Timestamp when the call activity occurred"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this call")
    """ID of the HubSpot owner to assign to this call"""

class CallUpdateParams(BaseModel):
    """Parameters for updating an existing call. Only provided properties will be updated."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: CallUpdateParamsProperties

class CallsList(BaseModel):
    """Paginated list of calls"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Call] | None = Field(default=None)
    paging: Paging | None = Field(default=None)
    total: int | None = Field(default=None)

class EmailProperties(BaseModel):
    """Email properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_email_subject: str | None | None = Field(default=None, description="Subject line of the email")
    """Subject line of the email"""
    hs_email_text: str | None | None = Field(default=None, description="Plain text body of the email")
    """Plain text body of the email"""
    hs_email_html: str | None | None = Field(default=None, description="HTML body of the email")
    """HTML body of the email"""
    hs_email_direction: str | None | None = Field(default=None, description="Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)")
    """Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)"""
    hs_email_status: str | None | None = Field(default=None, description="Status of the email (e.g., BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)")
    """Status of the email (e.g., BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)"""
    hs_email_sender_email: str | None | None = Field(default=None, description="Sender email address")
    """Sender email address"""
    hs_email_to_email: str | None | None = Field(default=None, description="Recipient email address(es)")
    """Recipient email address(es)"""
    hs_timestamp: str | None | None = Field(default=None, description="Timestamp when the email activity occurred")
    """Timestamp when the email activity occurred"""
    hubspot_owner_id: str | None | None = Field(default=None, description="ID of the email owner")
    """ID of the email owner"""
    hs_object_id: str | None | None = Field(default=None, description="HubSpot object ID")
    """HubSpot object ID"""
    hs_createdate: str | None | None = Field(default=None, description="Date the email was created")
    """Date the email was created"""
    hs_lastmodifieddate: str | None | None = Field(default=None, description="Last modified date")
    """Last modified date"""

class Email(BaseModel):
    """HubSpot email engagement object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    properties: EmailProperties | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    archived: bool | None = Field(default=None)
    archived_at: str | None = Field(default=None, alias="archivedAt")
    associations: dict[str, Any] | None = Field(default=None)

class EmailCreateParamsAssociationsItemTypesItem(BaseModel):
    """Nested schema for EmailCreateParamsAssociationsItem.types_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    association_category: str | None = Field(default=None, alias="associationCategory", description="Association category (e.g., HUBSPOT_DEFINED)")
    """Association category (e.g., HUBSPOT_DEFINED)"""
    association_type_id: int | None = Field(default=None, alias="associationTypeId", description="Association type ID (e.g., 198 for email-to-contact, 186 for email-to-company, 210 for email-to-deal, 224 for email-to-ticket)")
    """Association type ID (e.g., 198 for email-to-contact, 186 for email-to-company, 210 for email-to-deal, 224 for email-to-ticket)"""

class EmailCreateParamsAssociationsItemTo(BaseModel):
    """Nested schema for EmailCreateParamsAssociationsItem.to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="ID of the record to associate with")
    """ID of the record to associate with"""

class EmailCreateParamsAssociationsItem(BaseModel):
    """Nested schema for EmailCreateParams.associations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    to: EmailCreateParamsAssociationsItemTo | None = Field(default=None)
    types: list[EmailCreateParamsAssociationsItemTypesItem] | None = Field(default=None)

class EmailCreateParamsProperties(BaseModel):
    """Email properties to set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_email_subject: str | None = Field(default=None, description="Subject line of the email")
    """Subject line of the email"""
    hs_email_text: str | None = Field(default=None, description="Plain text body of the email")
    """Plain text body of the email"""
    hs_email_html: str | None = Field(default=None, description="HTML body of the email")
    """HTML body of the email"""
    hs_email_direction: str = Field(description="Required. Direction of the email (EMAIL for sent, INCOMING_EMAIL for received, FORWARDED_EMAIL for forwarded)")
    """Required. Direction of the email (EMAIL for sent, INCOMING_EMAIL for received, FORWARDED_EMAIL for forwarded)"""
    hs_email_status: str | None = Field(default=None, description="Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)")
    """Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)"""
    hs_email_sender_email: str | None = Field(default=None, description="Sender email address")
    """Sender email address"""
    hs_email_to_email: str | None = Field(default=None, description="Recipient email address(es)")
    """Recipient email address(es)"""
    hs_timestamp: str = Field(description="Required. Timestamp when the email activity occurred (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one.")
    """Required. Timestamp when the email activity occurred (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one."""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this email")
    """ID of the HubSpot owner to assign to this email"""

class EmailCreateParams(BaseModel):
    """Parameters for creating a new email"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: EmailCreateParamsProperties
    associations: list[EmailCreateParamsAssociationsItem] | None = Field(default=None)

class EmailUpdateParamsProperties(BaseModel):
    """Email properties to update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_email_subject: str | None = Field(default=None, description="Subject line of the email")
    """Subject line of the email"""
    hs_email_text: str | None = Field(default=None, description="Plain text body of the email")
    """Plain text body of the email"""
    hs_email_html: str | None = Field(default=None, description="HTML body of the email")
    """HTML body of the email"""
    hs_email_direction: str | None = Field(default=None, description="Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)")
    """Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)"""
    hs_email_status: str | None = Field(default=None, description="Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)")
    """Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)"""
    hs_timestamp: str | None = Field(default=None, description="Timestamp when the email activity occurred")
    """Timestamp when the email activity occurred"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this email")
    """ID of the HubSpot owner to assign to this email"""

class EmailUpdateParams(BaseModel):
    """Parameters for updating an existing email. Only provided properties will be updated."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: EmailUpdateParamsProperties

class EmailsList(BaseModel):
    """Paginated list of emails"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Email] | None = Field(default=None)
    paging: Paging | None = Field(default=None)
    total: int | None = Field(default=None)

class MeetingProperties(BaseModel):
    """Meeting properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_meeting_title: str | None | None = Field(default=None, description="Title of the meeting")
    """Title of the meeting"""
    hs_meeting_body: str | None | None = Field(default=None, description="Description or notes about the meeting")
    """Description or notes about the meeting"""
    hs_meeting_start_time: str | None | None = Field(default=None, description="Start time of the meeting (ISO 8601 format)")
    """Start time of the meeting (ISO 8601 format)"""
    hs_meeting_end_time: str | None | None = Field(default=None, description="End time of the meeting (ISO 8601 format)")
    """End time of the meeting (ISO 8601 format)"""
    hs_meeting_location: str | None | None = Field(default=None, description="Location of the meeting")
    """Location of the meeting"""
    hs_meeting_outcome: str | None | None = Field(default=None, description="Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)")
    """Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)"""
    hs_internal_meeting_notes: str | None | None = Field(default=None, description="Internal notes about the meeting")
    """Internal notes about the meeting"""
    hs_timestamp: str | None | None = Field(default=None, description="Timestamp when the meeting activity occurred")
    """Timestamp when the meeting activity occurred"""
    hubspot_owner_id: str | None | None = Field(default=None, description="ID of the meeting owner")
    """ID of the meeting owner"""
    hs_object_id: str | None | None = Field(default=None, description="HubSpot object ID")
    """HubSpot object ID"""
    hs_createdate: str | None | None = Field(default=None, description="Date the meeting was created")
    """Date the meeting was created"""
    hs_lastmodifieddate: str | None | None = Field(default=None, description="Last modified date")
    """Last modified date"""

class Meeting(BaseModel):
    """HubSpot meeting engagement object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    properties: MeetingProperties | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    archived: bool | None = Field(default=None)
    archived_at: str | None = Field(default=None, alias="archivedAt")
    associations: dict[str, Any] | None = Field(default=None)

class MeetingCreateParamsProperties(BaseModel):
    """Meeting properties to set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_meeting_title: str = Field(description="Required. Title of the meeting")
    """Required. Title of the meeting"""
    hs_meeting_body: str | None = Field(default=None, description="Description or notes about the meeting (supports HTML)")
    """Description or notes about the meeting (supports HTML)"""
    hs_meeting_start_time: str | None = Field(default=None, description="Start time of the meeting (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z)")
    """Start time of the meeting (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z)"""
    hs_meeting_end_time: str | None = Field(default=None, description="End time of the meeting (ISO 8601 format, e.g. 2025-01-15T11:30:00.000Z)")
    """End time of the meeting (ISO 8601 format, e.g. 2025-01-15T11:30:00.000Z)"""
    hs_meeting_location: str | None = Field(default=None, description="Location of the meeting")
    """Location of the meeting"""
    hs_meeting_outcome: str | None = Field(default=None, description="Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)")
    """Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)"""
    hs_internal_meeting_notes: str | None = Field(default=None, description="Internal notes about the meeting")
    """Internal notes about the meeting"""
    hs_timestamp: str = Field(description="Required. Timestamp when the meeting activity occurred (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one.")
    """Required. Timestamp when the meeting activity occurred (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one."""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this meeting")
    """ID of the HubSpot owner to assign to this meeting"""

class MeetingCreateParamsAssociationsItemTo(BaseModel):
    """Nested schema for MeetingCreateParamsAssociationsItem.to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="ID of the record to associate with")
    """ID of the record to associate with"""

class MeetingCreateParamsAssociationsItemTypesItem(BaseModel):
    """Nested schema for MeetingCreateParamsAssociationsItem.types_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    association_category: str | None = Field(default=None, alias="associationCategory", description="Association category (e.g., HUBSPOT_DEFINED)")
    """Association category (e.g., HUBSPOT_DEFINED)"""
    association_type_id: int | None = Field(default=None, alias="associationTypeId", description="Association type ID (e.g., 200 for meeting-to-contact, 188 for meeting-to-company, 212 for meeting-to-deal, 226 for meeting-to-ticket)")
    """Association type ID (e.g., 200 for meeting-to-contact, 188 for meeting-to-company, 212 for meeting-to-deal, 226 for meeting-to-ticket)"""

class MeetingCreateParamsAssociationsItem(BaseModel):
    """Nested schema for MeetingCreateParams.associations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    to: MeetingCreateParamsAssociationsItemTo | None = Field(default=None)
    types: list[MeetingCreateParamsAssociationsItemTypesItem] | None = Field(default=None)

class MeetingCreateParams(BaseModel):
    """Parameters for creating a new meeting"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: MeetingCreateParamsProperties
    associations: list[MeetingCreateParamsAssociationsItem] | None = Field(default=None)

class MeetingUpdateParamsProperties(BaseModel):
    """Meeting properties to update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_meeting_title: str | None = Field(default=None, description="Title of the meeting")
    """Title of the meeting"""
    hs_meeting_body: str | None = Field(default=None, description="Description or notes about the meeting (supports HTML)")
    """Description or notes about the meeting (supports HTML)"""
    hs_meeting_start_time: str | None = Field(default=None, description="Start time of the meeting (ISO 8601 format)")
    """Start time of the meeting (ISO 8601 format)"""
    hs_meeting_end_time: str | None = Field(default=None, description="End time of the meeting (ISO 8601 format)")
    """End time of the meeting (ISO 8601 format)"""
    hs_meeting_location: str | None = Field(default=None, description="Location of the meeting")
    """Location of the meeting"""
    hs_meeting_outcome: str | None = Field(default=None, description="Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)")
    """Outcome of the meeting (e.g., SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW, CANCELED)"""
    hs_internal_meeting_notes: str | None = Field(default=None, description="Internal notes about the meeting")
    """Internal notes about the meeting"""
    hs_timestamp: str | None = Field(default=None, description="Timestamp when the meeting activity occurred")
    """Timestamp when the meeting activity occurred"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this meeting")
    """ID of the HubSpot owner to assign to this meeting"""

class MeetingUpdateParams(BaseModel):
    """Parameters for updating an existing meeting. Only provided properties will be updated."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: MeetingUpdateParamsProperties

class MeetingsList(BaseModel):
    """Paginated list of meetings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Meeting] | None = Field(default=None)
    paging: Paging | None = Field(default=None)
    total: int | None = Field(default=None)

class TaskProperties(BaseModel):
    """Task properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_task_body: str | None | None = Field(default=None, description="Description or notes for the task (supports HTML)")
    """Description or notes for the task (supports HTML)"""
    hs_task_subject: str | None | None = Field(default=None, description="Subject or title of the task")
    """Subject or title of the task"""
    hs_task_status: str | None | None = Field(default=None, description="Status of the task (e.g., NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)")
    """Status of the task (e.g., NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)"""
    hs_task_priority: str | None | None = Field(default=None, description="Priority of the task (e.g., LOW, MEDIUM, HIGH)")
    """Priority of the task (e.g., LOW, MEDIUM, HIGH)"""
    hs_task_type: str | None | None = Field(default=None, description="Type of the task (e.g., TODO, CALL, EMAIL)")
    """Type of the task (e.g., TODO, CALL, EMAIL)"""
    hs_task_reminders: str | None | None = Field(default=None, description="Reminder timestamp for the task (epoch milliseconds)")
    """Reminder timestamp for the task (epoch milliseconds)"""
    hs_timestamp: str | None | None = Field(default=None, description="Timestamp when the task activity occurred (due date)")
    """Timestamp when the task activity occurred (due date)"""
    hubspot_owner_id: str | None | None = Field(default=None, description="ID of the task owner")
    """ID of the task owner"""
    hs_object_id: str | None | None = Field(default=None, description="HubSpot object ID")
    """HubSpot object ID"""
    hs_createdate: str | None | None = Field(default=None, description="Date the task was created")
    """Date the task was created"""
    hs_lastmodifieddate: str | None | None = Field(default=None, description="Last modified date")
    """Last modified date"""

class Task(BaseModel):
    """HubSpot task engagement object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    properties: TaskProperties | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    archived: bool | None = Field(default=None)
    archived_at: str | None = Field(default=None, alias="archivedAt")
    associations: dict[str, Any] | None = Field(default=None)

class TaskCreateParamsProperties(BaseModel):
    """Task properties to set"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_task_body: str | None = Field(default=None, description="Description or notes for the task (supports HTML)")
    """Description or notes for the task (supports HTML)"""
    hs_task_subject: str = Field(description="Required. Subject or title of the task")
    """Required. Subject or title of the task"""
    hs_task_status: str | None = Field(default=None, description="Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED). Defaults to NOT_STARTED.")
    """Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED). Defaults to NOT_STARTED."""
    hs_task_priority: str | None = Field(default=None, description="Priority of the task (LOW, MEDIUM, HIGH)")
    """Priority of the task (LOW, MEDIUM, HIGH)"""
    hs_task_type: str | None = Field(default=None, description="Type of the task (TODO, CALL, EMAIL). Defaults to TODO.")
    """Type of the task (TODO, CALL, EMAIL). Defaults to TODO."""
    hs_task_reminders: str | None = Field(default=None, description="Reminder timestamp for the task (epoch milliseconds)")
    """Reminder timestamp for the task (epoch milliseconds)"""
    hs_timestamp: str = Field(description="Required. Due date / timestamp for the task (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one.")
    """Required. Due date / timestamp for the task (ISO 8601 format, e.g. 2025-01-15T10:30:00.000Z). Use the current time if the user does not specify one."""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this task")
    """ID of the HubSpot owner to assign to this task"""

class TaskCreateParamsAssociationsItemTo(BaseModel):
    """Nested schema for TaskCreateParamsAssociationsItem.to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="ID of the record to associate with")
    """ID of the record to associate with"""

class TaskCreateParamsAssociationsItemTypesItem(BaseModel):
    """Nested schema for TaskCreateParamsAssociationsItem.types_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    association_category: str | None = Field(default=None, alias="associationCategory", description="Association category (e.g., HUBSPOT_DEFINED)")
    """Association category (e.g., HUBSPOT_DEFINED)"""
    association_type_id: int | None = Field(default=None, alias="associationTypeId", description="Association type ID (e.g., 204 for task-to-contact, 192 for task-to-company, 216 for task-to-deal, 228 for task-to-ticket)")
    """Association type ID (e.g., 204 for task-to-contact, 192 for task-to-company, 216 for task-to-deal, 228 for task-to-ticket)"""

class TaskCreateParamsAssociationsItem(BaseModel):
    """Nested schema for TaskCreateParams.associations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    to: TaskCreateParamsAssociationsItemTo | None = Field(default=None)
    types: list[TaskCreateParamsAssociationsItemTypesItem] | None = Field(default=None)

class TaskCreateParams(BaseModel):
    """Parameters for creating a new task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: TaskCreateParamsProperties
    associations: list[TaskCreateParamsAssociationsItem] | None = Field(default=None)

class TaskUpdateParamsProperties(BaseModel):
    """Task properties to update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    hs_task_body: str | None = Field(default=None, description="Description or notes for the task (supports HTML)")
    """Description or notes for the task (supports HTML)"""
    hs_task_subject: str | None = Field(default=None, description="Subject or title of the task")
    """Subject or title of the task"""
    hs_task_status: str | None = Field(default=None, description="Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)")
    """Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)"""
    hs_task_priority: str | None = Field(default=None, description="Priority of the task (LOW, MEDIUM, HIGH)")
    """Priority of the task (LOW, MEDIUM, HIGH)"""
    hs_task_type: str | None = Field(default=None, description="Type of the task (TODO, CALL, EMAIL)")
    """Type of the task (TODO, CALL, EMAIL)"""
    hs_task_reminders: str | None = Field(default=None, description="Reminder timestamp for the task (epoch milliseconds)")
    """Reminder timestamp for the task (epoch milliseconds)"""
    hs_timestamp: str | None = Field(default=None, description="Due date / timestamp for the task")
    """Due date / timestamp for the task"""
    hubspot_owner_id: str | None = Field(default=None, description="ID of the HubSpot owner to assign to this task")
    """ID of the HubSpot owner to assign to this task"""

class TaskUpdateParams(BaseModel):
    """Parameters for updating an existing task. Only provided properties will be updated."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: TaskUpdateParamsProperties

class TasksList(BaseModel):
    """Paginated list of tasks"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    results: list[Task] | None = Field(default=None)
    paging: Paging | None = Field(default=None)
    total: int | None = Field(default=None)

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

class NotesListResultMeta(BaseModel):
    """Metadata for notes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class CallsListResultMeta(BaseModel):
    """Metadata for calls.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class EmailsListResultMeta(BaseModel):
    """Metadata for emails.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class MeetingsListResultMeta(BaseModel):
    """Metadata for meetings.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class TasksListResultMeta(BaseModel):
    """Metadata for tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class ObjectsListResultMeta(BaseModel):
    """Metadata for objects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    next_link: str | None = Field(default=None)

class AssociationsListResultMeta(BaseModel):
    """Metadata for associations.Action.LIST operation"""
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
    meta: S | None = None
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
    properties_createdate: str | None = None
    """Date the company was created"""
    properties_domain: str | None = None
    """Company domain name"""
    properties_hs_lastmodifieddate: str | None = None
    """Last modified date of the company"""
    properties_hs_object_id: str | None = None
    """HubSpot object ID"""
    properties_hubspot_owner_id: str | None = None
    """ID of the HubSpot owner assigned to this company"""
    properties_name: str | None = None
    """Company name"""
    updated_at: str | None = None
    """Timestamp when the company record was last modified"""


class ContactsSearchData(BaseModel):
    """Search result data for contacts entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Boolean flag indicating whether the contact has been archived or deleted"""
    companies: list[Any] | None = None
    """Associated company records linked to this contact"""
    created_at: str | None = None
    """Timestamp indicating when the contact was first created in the system"""
    id: str | None = None
    """Unique identifier for the contact record"""
    properties: dict[str, Any] = None
    """Key-value object storing all contact properties and their values."""
    properties_associatedcompanyid: str | None = None
    """ID of the associated company"""
    properties_createdate: str | None = None
    """Date the contact was created"""
    properties_email: str | None = None
    """Contact email address"""
    properties_firstname: str | None = None
    """Contact first name"""
    properties_hs_object_id: str | None = None
    """HubSpot object ID"""
    properties_hubspot_owner_id: str | None = None
    """ID of the HubSpot owner assigned to this contact"""
    properties_lastmodifieddate: str | None = None
    """Last modified date of the contact"""
    properties_lastname: str | None = None
    """Contact last name"""
    updated_at: str | None = None
    """Timestamp indicating when the contact record was last modified"""


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
    properties_amount: str | None = None
    """Deal amount"""
    properties_closedate: str | None = None
    """Expected close date of the deal"""
    properties_createdate: str | None = None
    """Date the deal was created"""
    properties_dealname: str | None = None
    """Deal name"""
    properties_dealstage: str | None = None
    """Current deal stage"""
    properties_hs_lastmodifieddate: str | None = None
    """Last modified date of the deal"""
    properties_hs_object_id: str | None = None
    """HubSpot object ID"""
    properties_hubspot_owner_id: str | None = None
    """ID of the HubSpot owner assigned to this deal"""
    properties_pipeline: str | None = None
    """Deal pipeline"""
    updated_at: str | None = None
    """Timestamp when the deal record was last modified"""


class TicketsSearchData(BaseModel):
    """Search result data for tickets entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Indicates whether the ticket has been deleted and moved to the recycling bin"""
    companies: list[Any] | None = None
    """Collection of company records associated with the ticket"""
    contacts: list[Any] | None = None
    """Collection of contact records associated with the ticket"""
    created_at: str | None = None
    """Timestamp when the ticket record was originally created"""
    id: str | None = None
    """Unique identifier for the ticket record"""
    properties: dict[str, Any] = None
    """Object containing all property values for the ticket"""
    properties_content: str | None = None
    """Ticket content/description"""
    properties_createdate: str | None = None
    """Date the ticket was created"""
    properties_hs_lastmodifieddate: str | None = None
    """Last modified date of the ticket"""
    properties_hs_object_id: str | None = None
    """HubSpot object ID"""
    properties_hs_pipeline: str | None = None
    """Ticket pipeline"""
    properties_hs_pipeline_stage: str | None = None
    """Current pipeline stage of the ticket"""
    properties_hs_ticket_category: str | None = None
    """Ticket category"""
    properties_hs_ticket_priority: str | None = None
    """Ticket priority level"""
    properties_subject: str | None = None
    """Ticket subject line"""
    updated_at: str | None = None
    """Timestamp when the ticket record was last modified"""


class NotesSearchData(BaseModel):
    """Search result data for notes entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Indicates whether the note has been archived"""
    created_at: str | None = None
    """Timestamp when the note was created"""
    id: str | None = None
    """Unique identifier for the note record"""
    properties: dict[str, Any] = None
    """Object containing all property values for the note"""
    properties_hs_createdate: str | None = None
    """Date the note was created"""
    properties_hs_lastmodifieddate: str | None = None
    """Last modified date of the note"""
    properties_hs_note_body: str | None = None
    """The body content of the note (supports HTML)"""
    properties_hs_object_id: str | None = None
    """HubSpot object ID"""
    properties_hs_timestamp: str | None = None
    """Timestamp when the note activity occurred"""
    properties_hubspot_owner_id: str | None = None
    """ID of the note owner"""
    updated_at: str | None = None
    """Timestamp when the note record was last modified"""


class CallsSearchData(BaseModel):
    """Search result data for calls entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Indicates whether the call has been archived"""
    created_at: str | None = None
    """Timestamp when the call was created"""
    id: str | None = None
    """Unique identifier for the call record"""
    properties: dict[str, Any] = None
    """Object containing all property values for the call"""
    properties_hs_call_body: str | None = None
    """Description or notes about the call"""
    properties_hs_call_direction: str | None = None
    """Direction of the call (INBOUND or OUTBOUND)"""
    properties_hs_call_duration: str | None = None
    """Duration of the call in milliseconds"""
    properties_hs_call_status: str | None = None
    """Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER)"""
    properties_hs_call_title: str | None = None
    """Title or subject of the call"""
    properties_hs_createdate: str | None = None
    """Date the call was created"""
    properties_hs_lastmodifieddate: str | None = None
    """Last modified date of the call"""
    properties_hs_object_id: str | None = None
    """HubSpot object ID"""
    properties_hs_timestamp: str | None = None
    """Timestamp when the call activity occurred"""
    properties_hubspot_owner_id: str | None = None
    """ID of the call owner"""
    updated_at: str | None = None
    """Timestamp when the call record was last modified"""


class EmailsSearchData(BaseModel):
    """Search result data for emails entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Indicates whether the email has been archived"""
    created_at: str | None = None
    """Timestamp when the email was created"""
    id: str | None = None
    """Unique identifier for the email record"""
    properties: dict[str, Any] = None
    """Object containing all property values for the email"""
    properties_hs_createdate: str | None = None
    """Date the email was created"""
    properties_hs_email_direction: str | None = None
    """Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)"""
    properties_hs_email_status: str | None = None
    """Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)"""
    properties_hs_email_subject: str | None = None
    """Subject line of the email"""
    properties_hs_email_text: str | None = None
    """Plain text body of the email"""
    properties_hs_lastmodifieddate: str | None = None
    """Last modified date of the email"""
    properties_hs_object_id: str | None = None
    """HubSpot object ID"""
    properties_hs_timestamp: str | None = None
    """Timestamp when the email activity occurred"""
    properties_hubspot_owner_id: str | None = None
    """ID of the email owner"""
    updated_at: str | None = None
    """Timestamp when the email record was last modified"""


class MeetingsSearchData(BaseModel):
    """Search result data for meetings entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Indicates whether the meeting has been archived"""
    created_at: str | None = None
    """Timestamp when the meeting was created"""
    id: str | None = None
    """Unique identifier for the meeting record"""
    properties: dict[str, Any] = None
    """Object containing all property values for the meeting"""
    properties_hs_createdate: str | None = None
    """Date the meeting was created"""
    properties_hs_lastmodifieddate: str | None = None
    """Last modified date of the meeting"""
    properties_hs_meeting_body: str | None = None
    """Description or notes about the meeting"""
    properties_hs_meeting_end_time: str | None = None
    """End time of the meeting"""
    properties_hs_meeting_location: str | None = None
    """Location of the meeting"""
    properties_hs_meeting_outcome: str | None = None
    """Outcome of the meeting (e.g., SCHEDULED, COMPLETED, NO_SHOW, CANCELED)"""
    properties_hs_meeting_start_time: str | None = None
    """Start time of the meeting"""
    properties_hs_meeting_title: str | None = None
    """Title of the meeting"""
    properties_hs_object_id: str | None = None
    """HubSpot object ID"""
    properties_hs_timestamp: str | None = None
    """Timestamp when the meeting activity occurred"""
    properties_hubspot_owner_id: str | None = None
    """ID of the meeting owner"""
    updated_at: str | None = None
    """Timestamp when the meeting record was last modified"""


class TasksSearchData(BaseModel):
    """Search result data for tasks entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Indicates whether the task has been archived"""
    created_at: str | None = None
    """Timestamp when the task was created"""
    id: str | None = None
    """Unique identifier for the task record"""
    properties: dict[str, Any] = None
    """Object containing all property values for the task"""
    properties_hs_createdate: str | None = None
    """Date the task was created"""
    properties_hs_lastmodifieddate: str | None = None
    """Last modified date of the task"""
    properties_hs_object_id: str | None = None
    """HubSpot object ID"""
    properties_hs_task_body: str | None = None
    """Description or notes for the task"""
    properties_hs_task_priority: str | None = None
    """Priority of the task (LOW, MEDIUM, HIGH)"""
    properties_hs_task_status: str | None = None
    """Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)"""
    properties_hs_task_subject: str | None = None
    """Subject or title of the task"""
    properties_hs_task_type: str | None = None
    """Type of the task (TODO, CALL, EMAIL)"""
    properties_hs_timestamp: str | None = None
    """Due date / timestamp for the task"""
    properties_hubspot_owner_id: str | None = None
    """ID of the task owner"""
    updated_at: str | None = None
    """Timestamp when the task record was last modified"""


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

TicketsSearchResult = AirbyteSearchResult[TicketsSearchData]
"""Search result type for tickets entity."""

NotesSearchResult = AirbyteSearchResult[NotesSearchData]
"""Search result type for notes entity."""

CallsSearchResult = AirbyteSearchResult[CallsSearchData]
"""Search result type for calls entity."""

EmailsSearchResult = AirbyteSearchResult[EmailsSearchData]
"""Search result type for emails entity."""

MeetingsSearchResult = AirbyteSearchResult[MeetingsSearchData]
"""Search result type for meetings entity."""

TasksSearchResult = AirbyteSearchResult[TasksSearchData]
"""Search result type for tasks entity."""



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

NotesListResult = HubspotExecuteResultWithMeta[list[Note], NotesListResultMeta]
"""Result type for notes.list operation with data and metadata."""

CallsListResult = HubspotExecuteResultWithMeta[list[Call], CallsListResultMeta]
"""Result type for calls.list operation with data and metadata."""

EmailsListResult = HubspotExecuteResultWithMeta[list[Email], EmailsListResultMeta]
"""Result type for emails.list operation with data and metadata."""

MeetingsListResult = HubspotExecuteResultWithMeta[list[Meeting], MeetingsListResultMeta]
"""Result type for meetings.list operation with data and metadata."""

TasksListResult = HubspotExecuteResultWithMeta[list[Task], TasksListResultMeta]
"""Result type for tasks.list operation with data and metadata."""

SchemasListResult = HubspotExecuteResult[list[Schema]]
"""Result type for schemas.list operation."""

ObjectsListResult = HubspotExecuteResultWithMeta[list[CRMObject], ObjectsListResultMeta]
"""Result type for objects.list operation with data and metadata."""

AssociationsListResult = HubspotExecuteResultWithMeta[AssociationListResult, AssociationsListResultMeta]
"""Result type for associations.list operation with data and metadata."""

