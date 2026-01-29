"""
Pydantic models for salesforce connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class SalesforceAuthConfig(BaseModel):
    """Salesforce OAuth 2.0"""

    model_config = ConfigDict(extra="forbid")

    refresh_token: str
    """OAuth refresh token for automatic token renewal"""
    client_id: str
    """Connected App Consumer Key"""
    client_secret: str
    """Connected App Consumer Secret"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class AccountAttributes(BaseModel):
    """Nested schema for Account.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class Account(BaseModel):
    """Salesforce Account object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, alias="Id")
    name: Union[str, Any] = Field(default=None, alias="Name")
    attributes: Union[AccountAttributes, Any] = Field(default=None)

class AccountQueryResult(BaseModel):
    """SOQL query result for accounts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: Union[int, Any] = Field(default=None, alias="totalSize")
    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")
    records: Union[list[Account], Any] = Field(default=None)

class ContactAttributes(BaseModel):
    """Nested schema for Contact.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class Contact(BaseModel):
    """Salesforce Contact object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, alias="Id")
    name: Union[str, Any] = Field(default=None, alias="Name")
    attributes: Union[ContactAttributes, Any] = Field(default=None)

class ContactQueryResult(BaseModel):
    """SOQL query result for contacts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: Union[int, Any] = Field(default=None, alias="totalSize")
    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")
    records: Union[list[Contact], Any] = Field(default=None)

class LeadAttributes(BaseModel):
    """Nested schema for Lead.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class Lead(BaseModel):
    """Salesforce Lead object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, alias="Id")
    name: Union[str, Any] = Field(default=None, alias="Name")
    attributes: Union[LeadAttributes, Any] = Field(default=None)

class LeadQueryResult(BaseModel):
    """SOQL query result for leads"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: Union[int, Any] = Field(default=None, alias="totalSize")
    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")
    records: Union[list[Lead], Any] = Field(default=None)

class OpportunityAttributes(BaseModel):
    """Nested schema for Opportunity.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class Opportunity(BaseModel):
    """Salesforce Opportunity object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, alias="Id")
    name: Union[str, Any] = Field(default=None, alias="Name")
    attributes: Union[OpportunityAttributes, Any] = Field(default=None)

class OpportunityQueryResult(BaseModel):
    """SOQL query result for opportunities"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: Union[int, Any] = Field(default=None, alias="totalSize")
    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")
    records: Union[list[Opportunity], Any] = Field(default=None)

class TaskAttributes(BaseModel):
    """Nested schema for Task.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class Task(BaseModel):
    """Salesforce Task object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, alias="Id")
    subject: Union[str, Any] = Field(default=None, alias="Subject")
    attributes: Union[TaskAttributes, Any] = Field(default=None)

class TaskQueryResult(BaseModel):
    """SOQL query result for tasks"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: Union[int, Any] = Field(default=None, alias="totalSize")
    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")
    records: Union[list[Task], Any] = Field(default=None)

class EventAttributes(BaseModel):
    """Nested schema for Event.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class Event(BaseModel):
    """Salesforce Event object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, alias="Id")
    subject: Union[str, Any] = Field(default=None, alias="Subject")
    attributes: Union[EventAttributes, Any] = Field(default=None)

class EventQueryResult(BaseModel):
    """SOQL query result for events"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: Union[int, Any] = Field(default=None, alias="totalSize")
    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")
    records: Union[list[Event], Any] = Field(default=None)

class CampaignAttributes(BaseModel):
    """Nested schema for Campaign.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class Campaign(BaseModel):
    """Salesforce Campaign object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, alias="Id")
    name: Union[str, Any] = Field(default=None, alias="Name")
    attributes: Union[CampaignAttributes, Any] = Field(default=None)

class CampaignQueryResult(BaseModel):
    """SOQL query result for campaigns"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: Union[int, Any] = Field(default=None, alias="totalSize")
    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")
    records: Union[list[Campaign], Any] = Field(default=None)

class CaseAttributes(BaseModel):
    """Nested schema for Case.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class Case(BaseModel):
    """Salesforce Case object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, alias="Id")
    case_number: Union[str, Any] = Field(default=None, alias="CaseNumber")
    subject: Union[str, Any] = Field(default=None, alias="Subject")
    attributes: Union[CaseAttributes, Any] = Field(default=None)

class CaseQueryResult(BaseModel):
    """SOQL query result for cases"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: Union[int, Any] = Field(default=None, alias="totalSize")
    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")
    records: Union[list[Case], Any] = Field(default=None)

class NoteAttributes(BaseModel):
    """Nested schema for Note.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class Note(BaseModel):
    """Salesforce Note object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, alias="Id")
    title: Union[str, Any] = Field(default=None, alias="Title")
    attributes: Union[NoteAttributes, Any] = Field(default=None)

class NoteQueryResult(BaseModel):
    """SOQL query result for notes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: Union[int, Any] = Field(default=None, alias="totalSize")
    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")
    records: Union[list[Note], Any] = Field(default=None)

class ContentVersionAttributes(BaseModel):
    """Nested schema for ContentVersion.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class ContentVersion(BaseModel):
    """Salesforce ContentVersion object - represents a file version in Salesforce Files"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, alias="Id")
    title: Union[str, Any] = Field(default=None, alias="Title")
    file_extension: Union[str, Any] = Field(default=None, alias="FileExtension")
    content_size: Union[int, Any] = Field(default=None, alias="ContentSize")
    content_document_id: Union[str, Any] = Field(default=None, alias="ContentDocumentId")
    version_number: Union[str, Any] = Field(default=None, alias="VersionNumber")
    is_latest: Union[bool, Any] = Field(default=None, alias="IsLatest")
    attributes: Union[ContentVersionAttributes, Any] = Field(default=None)

class ContentVersionQueryResult(BaseModel):
    """SOQL query result for content versions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: Union[int, Any] = Field(default=None, alias="totalSize")
    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")
    records: Union[list[ContentVersion], Any] = Field(default=None)

class AttachmentAttributes(BaseModel):
    """Nested schema for Attachment.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class Attachment(BaseModel):
    """Salesforce Attachment object - legacy file attachment on a record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, alias="Id")
    name: Union[str, Any] = Field(default=None, alias="Name")
    content_type: Union[str, Any] = Field(default=None, alias="ContentType")
    body_length: Union[int, Any] = Field(default=None, alias="BodyLength")
    parent_id: Union[str, Any] = Field(default=None, alias="ParentId")
    attributes: Union[AttachmentAttributes, Any] = Field(default=None)

class AttachmentQueryResult(BaseModel):
    """SOQL query result for attachments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: Union[int, Any] = Field(default=None, alias="totalSize")
    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")
    records: Union[list[Attachment], Any] = Field(default=None)

class QueryResult(BaseModel):
    """Generic SOQL query result"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: Union[int, Any] = Field(default=None, alias="totalSize")
    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")
    records: Union[list[dict[str, Any]], Any] = Field(default=None)

class SearchResultSearchrecordsItemAttributes(BaseModel):
    """Nested schema for SearchResultSearchrecordsItem.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)

class SearchResultSearchrecordsItem(BaseModel):
    """Nested schema for SearchResult.searchRecords_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, alias="Id")
    attributes: Union[SearchResultSearchrecordsItemAttributes, Any] = Field(default=None)

class SearchResult(BaseModel):
    """SOSL search result"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    search_records: Union[list[SearchResultSearchrecordsItem], Any] = Field(default=None, alias="searchRecords")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class AccountsListResultMeta(BaseModel):
    """Metadata for accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")

class LeadsListResultMeta(BaseModel):
    """Metadata for leads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")

class OpportunitiesListResultMeta(BaseModel):
    """Metadata for opportunities.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")

class TasksListResultMeta(BaseModel):
    """Metadata for tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")

class EventsListResultMeta(BaseModel):
    """Metadata for events.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")

class CasesListResultMeta(BaseModel):
    """Metadata for cases.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")

class NotesListResultMeta(BaseModel):
    """Metadata for notes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")

class ContentVersionsListResultMeta(BaseModel):
    """Metadata for content_versions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")

class AttachmentsListResultMeta(BaseModel):
    """Metadata for attachments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")

class QueryListResultMeta(BaseModel):
    """Metadata for query.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: Union[bool, Any] = Field(default=None)
    next_records_url: Union[str, Any] = Field(default=None, alias="nextRecordsUrl")

# ===== CHECK RESULT MODEL =====

class SalesforceCheckResult(BaseModel):
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


class SalesforceExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class SalesforceExecuteResultWithMeta(SalesforceExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AccountsSearchData(BaseModel):
    """Search result data for accounts entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the account record"""
    name: str | None = None
    """Name of the account or company"""
    account_source: str | None = None
    """Source of the account record (e.g., Web, Referral)"""
    billing_address: dict[str, Any] | None = None
    """Complete billing address as a compound field"""
    billing_city: str | None = None
    """City portion of the billing address"""
    billing_country: str | None = None
    """Country portion of the billing address"""
    billing_postal_code: str | None = None
    """Postal code portion of the billing address"""
    billing_state: str | None = None
    """State or province portion of the billing address"""
    billing_street: str | None = None
    """Street address portion of the billing address"""
    created_by_id: str | None = None
    """ID of the user who created this account"""
    created_date: str | None = None
    """Date and time when the account was created"""
    description: str | None = None
    """Text description of the account"""
    industry: str | None = None
    """Primary business industry of the account"""
    is_deleted: bool | None = None
    """Whether the account has been moved to the Recycle Bin"""
    last_activity_date: str | None = None
    """Date of the last activity associated with this account"""
    last_modified_by_id: str | None = None
    """ID of the user who last modified this account"""
    last_modified_date: str | None = None
    """Date and time when the account was last modified"""
    number_of_employees: int | None = None
    """Number of employees at the account"""
    owner_id: str | None = None
    """ID of the user who owns this account"""
    parent_id: str | None = None
    """ID of the parent account, if this is a subsidiary"""
    phone: str | None = None
    """Primary phone number for the account"""
    shipping_address: dict[str, Any] | None = None
    """Complete shipping address as a compound field"""
    shipping_city: str | None = None
    """City portion of the shipping address"""
    shipping_country: str | None = None
    """Country portion of the shipping address"""
    shipping_postal_code: str | None = None
    """Postal code portion of the shipping address"""
    shipping_state: str | None = None
    """State or province portion of the shipping address"""
    shipping_street: str | None = None
    """Street address portion of the shipping address"""
    type: str | None = None
    """Type of account (e.g., Customer, Partner, Competitor)"""
    website: str | None = None
    """Website URL for the account"""
    system_modstamp: str | None = None
    """System timestamp when the record was last modified"""


class ContactsSearchData(BaseModel):
    """Search result data for contacts entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the contact record"""
    account_id: str | None = None
    """ID of the account this contact is associated with"""
    created_by_id: str | None = None
    """ID of the user who created this contact"""
    created_date: str | None = None
    """Date and time when the contact was created"""
    department: str | None = None
    """Department within the account where the contact works"""
    email: str | None = None
    """Email address of the contact"""
    first_name: str | None = None
    """First name of the contact"""
    is_deleted: bool | None = None
    """Whether the contact has been moved to the Recycle Bin"""
    last_activity_date: str | None = None
    """Date of the last activity associated with this contact"""
    last_modified_by_id: str | None = None
    """ID of the user who last modified this contact"""
    last_modified_date: str | None = None
    """Date and time when the contact was last modified"""
    last_name: str | None = None
    """Last name of the contact"""
    lead_source: str | None = None
    """Source from which this contact originated"""
    mailing_address: dict[str, Any] | None = None
    """Complete mailing address as a compound field"""
    mailing_city: str | None = None
    """City portion of the mailing address"""
    mailing_country: str | None = None
    """Country portion of the mailing address"""
    mailing_postal_code: str | None = None
    """Postal code portion of the mailing address"""
    mailing_state: str | None = None
    """State or province portion of the mailing address"""
    mailing_street: str | None = None
    """Street address portion of the mailing address"""
    mobile_phone: str | None = None
    """Mobile phone number of the contact"""
    name: str | None = None
    """Full name of the contact (read-only, concatenation of first and last name)"""
    owner_id: str | None = None
    """ID of the user who owns this contact"""
    phone: str | None = None
    """Business phone number of the contact"""
    reports_to_id: str | None = None
    """ID of the contact this contact reports to"""
    title: str | None = None
    """Job title of the contact"""
    system_modstamp: str | None = None
    """System timestamp when the record was last modified"""


class LeadsSearchData(BaseModel):
    """Search result data for leads entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the lead record"""
    address: dict[str, Any] | None = None
    """Complete address as a compound field"""
    city: str | None = None
    """City portion of the address"""
    company: str | None = None
    """Company or organization the lead works for"""
    converted_account_id: str | None = None
    """ID of the account created when lead was converted"""
    converted_contact_id: str | None = None
    """ID of the contact created when lead was converted"""
    converted_date: str | None = None
    """Date when the lead was converted"""
    converted_opportunity_id: str | None = None
    """ID of the opportunity created when lead was converted"""
    country: str | None = None
    """Country portion of the address"""
    created_by_id: str | None = None
    """ID of the user who created this lead"""
    created_date: str | None = None
    """Date and time when the lead was created"""
    email: str | None = None
    """Email address of the lead"""
    first_name: str | None = None
    """First name of the lead"""
    industry: str | None = None
    """Industry the lead's company operates in"""
    is_converted: bool | None = None
    """Whether the lead has been converted to an account, contact, and opportunity"""
    is_deleted: bool | None = None
    """Whether the lead has been moved to the Recycle Bin"""
    last_activity_date: str | None = None
    """Date of the last activity associated with this lead"""
    last_modified_by_id: str | None = None
    """ID of the user who last modified this lead"""
    last_modified_date: str | None = None
    """Date and time when the lead was last modified"""
    last_name: str | None = None
    """Last name of the lead"""
    lead_source: str | None = None
    """Source from which this lead originated"""
    mobile_phone: str | None = None
    """Mobile phone number of the lead"""
    name: str | None = None
    """Full name of the lead (read-only, concatenation of first and last name)"""
    number_of_employees: int | None = None
    """Number of employees at the lead's company"""
    owner_id: str | None = None
    """ID of the user who owns this lead"""
    phone: str | None = None
    """Phone number of the lead"""
    postal_code: str | None = None
    """Postal code portion of the address"""
    rating: str | None = None
    """Rating of the lead (e.g., Hot, Warm, Cold)"""
    state: str | None = None
    """State or province portion of the address"""
    status: str | None = None
    """Current status of the lead in the sales process"""
    street: str | None = None
    """Street address portion of the address"""
    title: str | None = None
    """Job title of the lead"""
    website: str | None = None
    """Website URL for the lead's company"""
    system_modstamp: str | None = None
    """System timestamp when the record was last modified"""


class OpportunitiesSearchData(BaseModel):
    """Search result data for opportunities entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the opportunity record"""
    account_id: str | None = None
    """ID of the account associated with this opportunity"""
    amount: float | None = None
    """Estimated total sale amount"""
    campaign_id: str | None = None
    """ID of the campaign that generated this opportunity"""
    close_date: str | None = None
    """Expected close date for the opportunity"""
    contact_id: str | None = None
    """ID of the primary contact for this opportunity"""
    created_by_id: str | None = None
    """ID of the user who created this opportunity"""
    created_date: str | None = None
    """Date and time when the opportunity was created"""
    description: str | None = None
    """Text description of the opportunity"""
    expected_revenue: float | None = None
    """Expected revenue based on amount and probability"""
    forecast_category: str | None = None
    """Forecast category for this opportunity"""
    forecast_category_name: str | None = None
    """Name of the forecast category"""
    is_closed: bool | None = None
    """Whether the opportunity is closed"""
    is_deleted: bool | None = None
    """Whether the opportunity has been moved to the Recycle Bin"""
    is_won: bool | None = None
    """Whether the opportunity was won"""
    last_activity_date: str | None = None
    """Date of the last activity associated with this opportunity"""
    last_modified_by_id: str | None = None
    """ID of the user who last modified this opportunity"""
    last_modified_date: str | None = None
    """Date and time when the opportunity was last modified"""
    lead_source: str | None = None
    """Source from which this opportunity originated"""
    name: str | None = None
    """Name of the opportunity"""
    next_step: str | None = None
    """Description of the next step in closing the opportunity"""
    owner_id: str | None = None
    """ID of the user who owns this opportunity"""
    probability: float | None = None
    """Likelihood of closing the opportunity (percentage)"""
    stage_name: str | None = None
    """Current stage of the opportunity in the sales process"""
    type: str | None = None
    """Type of opportunity (e.g., New Business, Existing Business)"""
    system_modstamp: str | None = None
    """System timestamp when the record was last modified"""


class TasksSearchData(BaseModel):
    """Search result data for tasks entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the task record"""
    account_id: str | None = None
    """ID of the account associated with this task"""
    activity_date: str | None = None
    """Due date for the task"""
    call_disposition: str | None = None
    """Result of the call, if this task represents a call"""
    call_duration_in_seconds: int | None = None
    """Duration of the call in seconds"""
    call_type: str | None = None
    """Type of call (Inbound, Outbound, Internal)"""
    completed_date_time: str | None = None
    """Date and time when the task was completed"""
    created_by_id: str | None = None
    """ID of the user who created this task"""
    created_date: str | None = None
    """Date and time when the task was created"""
    description: str | None = None
    """Text description or notes about the task"""
    is_closed: bool | None = None
    """Whether the task has been completed"""
    is_deleted: bool | None = None
    """Whether the task has been moved to the Recycle Bin"""
    is_high_priority: bool | None = None
    """Whether the task is marked as high priority"""
    last_modified_by_id: str | None = None
    """ID of the user who last modified this task"""
    last_modified_date: str | None = None
    """Date and time when the task was last modified"""
    owner_id: str | None = None
    """ID of the user who owns this task"""
    priority: str | None = None
    """Priority level of the task (High, Normal, Low)"""
    status: str | None = None
    """Current status of the task"""
    subject: str | None = None
    """Subject or title of the task"""
    task_subtype: str | None = None
    """Subtype of the task (e.g., Call, Email, Task)"""
    type: str | None = None
    """Type of task"""
    what_id: str | None = None
    """ID of the related object (Account, Opportunity, etc.)"""
    who_id: str | None = None
    """ID of the related person (Contact or Lead)"""
    system_modstamp: str | None = None
    """System timestamp when the record was last modified"""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchHit(BaseModel, Generic[D]):
    """A single search result with typed data."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the record."""
    score: float | None = None
    """Relevance score for the match."""
    data: D
    """The matched record data."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed hits."""
    model_config = ConfigDict(extra="allow")

    hits: list[AirbyteSearchHit[D]] = Field(default_factory=list)
    """List of matching records."""
    next_cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

AccountsSearchResult = AirbyteSearchResult[AccountsSearchData]
"""Search result type for accounts entity."""

ContactsSearchResult = AirbyteSearchResult[ContactsSearchData]
"""Search result type for contacts entity."""

LeadsSearchResult = AirbyteSearchResult[LeadsSearchData]
"""Search result type for leads entity."""

OpportunitiesSearchResult = AirbyteSearchResult[OpportunitiesSearchData]
"""Search result type for opportunities entity."""

TasksSearchResult = AirbyteSearchResult[TasksSearchData]
"""Search result type for tasks entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

AccountsListResult = SalesforceExecuteResultWithMeta[list[Account], AccountsListResultMeta]
"""Result type for accounts.list operation with data and metadata."""

AccountsApiSearchResult = SalesforceExecuteResult[SearchResult]
"""Result type for accounts.api_search operation."""

ContactsListResult = SalesforceExecuteResultWithMeta[list[Contact], ContactsListResultMeta]
"""Result type for contacts.list operation with data and metadata."""

ContactsApiSearchResult = SalesforceExecuteResult[SearchResult]
"""Result type for contacts.api_search operation."""

LeadsListResult = SalesforceExecuteResultWithMeta[list[Lead], LeadsListResultMeta]
"""Result type for leads.list operation with data and metadata."""

LeadsApiSearchResult = SalesforceExecuteResult[SearchResult]
"""Result type for leads.api_search operation."""

OpportunitiesListResult = SalesforceExecuteResultWithMeta[list[Opportunity], OpportunitiesListResultMeta]
"""Result type for opportunities.list operation with data and metadata."""

OpportunitiesApiSearchResult = SalesforceExecuteResult[SearchResult]
"""Result type for opportunities.api_search operation."""

TasksListResult = SalesforceExecuteResultWithMeta[list[Task], TasksListResultMeta]
"""Result type for tasks.list operation with data and metadata."""

TasksApiSearchResult = SalesforceExecuteResult[SearchResult]
"""Result type for tasks.api_search operation."""

EventsListResult = SalesforceExecuteResultWithMeta[list[Event], EventsListResultMeta]
"""Result type for events.list operation with data and metadata."""

EventsApiSearchResult = SalesforceExecuteResult[SearchResult]
"""Result type for events.api_search operation."""

CampaignsListResult = SalesforceExecuteResultWithMeta[list[Campaign], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

CampaignsApiSearchResult = SalesforceExecuteResult[SearchResult]
"""Result type for campaigns.api_search operation."""

CasesListResult = SalesforceExecuteResultWithMeta[list[Case], CasesListResultMeta]
"""Result type for cases.list operation with data and metadata."""

CasesApiSearchResult = SalesforceExecuteResult[SearchResult]
"""Result type for cases.api_search operation."""

NotesListResult = SalesforceExecuteResultWithMeta[list[Note], NotesListResultMeta]
"""Result type for notes.list operation with data and metadata."""

NotesApiSearchResult = SalesforceExecuteResult[SearchResult]
"""Result type for notes.api_search operation."""

ContentVersionsListResult = SalesforceExecuteResultWithMeta[list[ContentVersion], ContentVersionsListResultMeta]
"""Result type for content_versions.list operation with data and metadata."""

AttachmentsListResult = SalesforceExecuteResultWithMeta[list[Attachment], AttachmentsListResultMeta]
"""Result type for attachments.list operation with data and metadata."""

QueryListResult = SalesforceExecuteResultWithMeta[list[dict[str, Any]], QueryListResultMeta]
"""Result type for query.list operation with data and metadata."""

