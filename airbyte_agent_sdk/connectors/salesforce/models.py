"""
Pydantic models for salesforce connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
from typing import Optional

# Authentication configuration

class SalesforceAuthConfig(BaseModel):
    """Salesforce OAuth 2.0"""

    model_config = ConfigDict(extra="forbid")

    refresh_token: str
    """OAuth refresh token for automatic token renewal"""
    client_id: Optional[str] = None
    """Connected App Consumer Key"""
    client_secret: Optional[str] = None
    """Connected App Consumer Secret"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class SObject(BaseModel):
    """Salesforce sObject metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    label: str | None = Field(default=None)
    label_plural: str | None = Field(default=None, alias="labelPlural")
    key_prefix: str | None = Field(default=None, alias="keyPrefix")
    custom: bool | None = Field(default=None)
    queryable: bool | None = Field(default=None)
    searchable: bool | None = Field(default=None)
    createable: bool | None = Field(default=None)
    updateable: bool | None = Field(default=None)
    deletable: bool | None = Field(default=None)
    urls: dict[str, Any] | None = Field(default=None)

class SObjectsResponse(BaseModel):
    """Response from the sobjects endpoint listing all available Salesforce objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    encoding: str | None = Field(default=None)
    max_batch_size: int | None = Field(default=None, alias="maxBatchSize")
    sobjects: list[SObject] | None = Field(default=None)

class AccountAttributes(BaseModel):
    """Nested schema for Account.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class Account(BaseModel):
    """Salesforce Account object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    name: str | None = Field(default=None, alias="Name")
    attributes: AccountAttributes | None = Field(default=None)

class AccountQueryResult(BaseModel):
    """SOQL query result for accounts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[Account] | None = Field(default=None)

class ContactAttributes(BaseModel):
    """Nested schema for Contact.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class Contact(BaseModel):
    """Salesforce Contact object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    name: str | None = Field(default=None, alias="Name")
    attributes: ContactAttributes | None = Field(default=None)

class ContactQueryResult(BaseModel):
    """SOQL query result for contacts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[Contact] | None = Field(default=None)

class LeadAttributes(BaseModel):
    """Nested schema for Lead.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class Lead(BaseModel):
    """Salesforce Lead object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    name: str | None = Field(default=None, alias="Name")
    attributes: LeadAttributes | None = Field(default=None)

class LeadQueryResult(BaseModel):
    """SOQL query result for leads"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[Lead] | None = Field(default=None)

class OpportunityAttributes(BaseModel):
    """Nested schema for Opportunity.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class Opportunity(BaseModel):
    """Salesforce Opportunity object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    name: str | None = Field(default=None, alias="Name")
    attributes: OpportunityAttributes | None = Field(default=None)

class OpportunityQueryResult(BaseModel):
    """SOQL query result for opportunities"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[Opportunity] | None = Field(default=None)

class TaskAttributes(BaseModel):
    """Nested schema for Task.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class Task(BaseModel):
    """Salesforce Task object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    subject: str | None = Field(default=None, alias="Subject")
    attributes: TaskAttributes | None = Field(default=None)

class TaskQueryResult(BaseModel):
    """SOQL query result for tasks"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[Task] | None = Field(default=None)

class EventAttributes(BaseModel):
    """Nested schema for Event.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class Event(BaseModel):
    """Salesforce Event object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    subject: str | None = Field(default=None, alias="Subject")
    attributes: EventAttributes | None = Field(default=None)

class EventQueryResult(BaseModel):
    """SOQL query result for events"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[Event] | None = Field(default=None)

class CampaignAttributes(BaseModel):
    """Nested schema for Campaign.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class Campaign(BaseModel):
    """Salesforce Campaign object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    name: str | None = Field(default=None, alias="Name")
    attributes: CampaignAttributes | None = Field(default=None)

class CampaignQueryResult(BaseModel):
    """SOQL query result for campaigns"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[Campaign] | None = Field(default=None)

class CaseAttributes(BaseModel):
    """Nested schema for Case.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class Case(BaseModel):
    """Salesforce Case object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    case_number: str | None = Field(default=None, alias="CaseNumber")
    subject: str | None = Field(default=None, alias="Subject")
    attributes: CaseAttributes | None = Field(default=None)

class CaseQueryResult(BaseModel):
    """SOQL query result for cases"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[Case] | None = Field(default=None)

class NoteAttributes(BaseModel):
    """Nested schema for Note.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class Note(BaseModel):
    """Salesforce Note object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    title: str | None = Field(default=None, alias="Title")
    attributes: NoteAttributes | None = Field(default=None)

class NoteQueryResult(BaseModel):
    """SOQL query result for notes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[Note] | None = Field(default=None)

class ContentVersionAttributes(BaseModel):
    """Nested schema for ContentVersion.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class ContentVersion(BaseModel):
    """Salesforce ContentVersion object - represents a file version in Salesforce Files"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    title: str | None = Field(default=None, alias="Title")
    file_extension: str | None = Field(default=None, alias="FileExtension")
    content_size: int | None = Field(default=None, alias="ContentSize")
    content_document_id: str | None = Field(default=None, alias="ContentDocumentId")
    version_number: str | None = Field(default=None, alias="VersionNumber")
    is_latest: bool | None = Field(default=None, alias="IsLatest")
    attributes: ContentVersionAttributes | None = Field(default=None)

class ContentVersionQueryResult(BaseModel):
    """SOQL query result for content versions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[ContentVersion] | None = Field(default=None)

class AttachmentAttributes(BaseModel):
    """Nested schema for Attachment.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class Attachment(BaseModel):
    """Salesforce Attachment object - legacy file attachment on a record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    name: str | None = Field(default=None, alias="Name")
    content_type: str | None = Field(default=None, alias="ContentType")
    body_length: int | None = Field(default=None, alias="BodyLength")
    parent_id: str | None = Field(default=None, alias="ParentId")
    attributes: AttachmentAttributes | None = Field(default=None)

class AttachmentQueryResult(BaseModel):
    """SOQL query result for attachments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[Attachment] | None = Field(default=None)

class Report(BaseModel):
    """Salesforce Report metadata from the Analytics API"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    url: str | None = Field(default=None)
    describe_url: str | None = Field(default=None, alias="describeUrl")
    instances_url: str | None = Field(default=None, alias="instancesUrl")

class ReportResults(BaseModel):
    """Executed report results including data rows, aggregates, and metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    attributes: dict[str, Any] | None = Field(default=None)
    report_metadata: dict[str, Any] | None = Field(default=None, alias="reportMetadata")
    report_extended_metadata: dict[str, Any] | None = Field(default=None, alias="reportExtendedMetadata")
    fact_map: dict[str, Any] | None = Field(default=None, alias="factMap")
    groupings_down: dict[str, Any] | None = Field(default=None, alias="groupingsDown")
    groupings_across: dict[str, Any] | None = Field(default=None, alias="groupingsAcross")
    has_detail_rows: bool | None = Field(default=None, alias="hasDetailRows")
    all_data: bool | None = Field(default=None, alias="allData")

class UserAttributes(BaseModel):
    """Nested schema for User.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class User(BaseModel):
    """Salesforce User object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    name: str | None = Field(default=None, alias="Name")
    attributes: UserAttributes | None = Field(default=None)

class UserQueryResult(BaseModel):
    """SOQL query result for users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[User] | None = Field(default=None)

class OpportunityStageAttributes(BaseModel):
    """Nested schema for OpportunityStage.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class OpportunityStage(BaseModel):
    """Salesforce OpportunityStage object - uses FIELDS(STANDARD) so all standard fields are returned"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    master_label: str | None = Field(default=None, alias="MasterLabel")
    attributes: OpportunityStageAttributes | None = Field(default=None)

class OpportunityStageQueryResult(BaseModel):
    """SOQL query result for opportunity stages"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[OpportunityStage] | None = Field(default=None)

class QueryResult(BaseModel):
    """Generic SOQL query result"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_size: int | None = Field(default=None, alias="totalSize")
    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")
    records: list[dict[str, Any]] | None = Field(default=None)

class SearchResultSearchrecordsItemAttributes(BaseModel):
    """Nested schema for SearchResultSearchrecordsItem.attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class SearchResultSearchrecordsItem(BaseModel):
    """Nested schema for SearchResult.searchRecords_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, alias="Id")
    attributes: SearchResultSearchrecordsItemAttributes | None = Field(default=None)

class SearchResult(BaseModel):
    """SOSL search result"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    search_records: list[SearchResultSearchrecordsItem] | None = Field(default=None, alias="searchRecords")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class AccountsListResultMeta(BaseModel):
    """Metadata for accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class LeadsListResultMeta(BaseModel):
    """Metadata for leads.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class OpportunitiesListResultMeta(BaseModel):
    """Metadata for opportunities.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class TasksListResultMeta(BaseModel):
    """Metadata for tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class EventsListResultMeta(BaseModel):
    """Metadata for events.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class CasesListResultMeta(BaseModel):
    """Metadata for cases.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class NotesListResultMeta(BaseModel):
    """Metadata for notes.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class ContentVersionsListResultMeta(BaseModel):
    """Metadata for content_versions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class AttachmentsListResultMeta(BaseModel):
    """Metadata for attachments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class OpportunityStagesListResultMeta(BaseModel):
    """Metadata for opportunity_stages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

class QueryListResultMeta(BaseModel):
    """Metadata for query.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    done: bool | None = Field(default=None)
    next_records_url: str | None = Field(default=None, alias="nextRecordsUrl")

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
    type_: str | None = None
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
    type_: str | None = None
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
    type_: str | None = None
    """Type of task"""
    what_id: str | None = None
    """ID of the related object (Account, Opportunity, etc.)"""
    who_id: str | None = None
    """ID of the related person (Contact or Lead)"""
    system_modstamp: str | None = None
    """System timestamp when the record was last modified"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the user record"""
    account_id: str | None = None
    """ID of the account associated with this user (for portal users)"""
    alias: str | None = None
    """Short name used to identify the user in list views and reports"""
    city: str | None = None
    """City portion of the user's address"""
    company_name: str | None = None
    """Name of the user's company"""
    contact_id: str | None = None
    """ID of the contact associated with this user (for portal users)"""
    country: str | None = None
    """Country portion of the user's address"""
    created_by_id: str | None = None
    """ID of the user who created this user record"""
    created_date: str | None = None
    """Date and time when the user was created"""
    department: str | None = None
    """Department within the organization"""
    division: str | None = None
    """Division within the organization"""
    email: str | None = None
    """Email address of the user"""
    employee_number: str | None = None
    """Employee number or ID assigned by the organization"""
    first_name: str | None = None
    """First name of the user"""
    is_active: bool | None = None
    """Whether the user is active and can log in"""
    last_login_date: str | None = None
    """Date and time of the user's most recent login"""
    last_modified_by_id: str | None = None
    """ID of the user who last modified this user record"""
    last_modified_date: str | None = None
    """Date and time when the user was last modified"""
    last_name: str | None = None
    """Last name of the user"""
    manager_id: str | None = None
    """ID of the user's manager"""
    mobile_phone: str | None = None
    """Mobile phone number of the user"""
    name: str | None = None
    """Full name of the user"""
    phone: str | None = None
    """Business phone number of the user"""
    postal_code: str | None = None
    """Postal code portion of the user's address"""
    profile_id: str | None = None
    """ID of the user's profile"""
    state: str | None = None
    """State or province portion of the user's address"""
    street: str | None = None
    """Street address of the user"""
    title: str | None = None
    """Job title of the user"""
    user_role_id: str | None = None
    """ID of the user's role in the organization"""
    user_type: str | None = None
    """Type of user license (e.g., Standard, PowerPartner)"""
    username: str | None = None
    """Username for logging into Salesforce (unique across all orgs)"""
    system_modstamp: str | None = None
    """System timestamp when the record was last modified"""


class OpportunityStagesSearchData(BaseModel):
    """Search result data for opportunity_stages entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the opportunity stage record"""
    api_name: str | None = None
    """API name of the stage used in code and integrations"""
    created_by_id: str | None = None
    """ID of the user who created this stage"""
    created_date: str | None = None
    """Date and time when the stage was created"""
    default_probability: float | None = None
    """Default probability percentage for opportunities at this stage"""
    description: str | None = None
    """Description of the stage"""
    forecast_category: str | None = None
    """Forecast category for opportunities at this stage"""
    forecast_category_name: str | None = None
    """Display name of the forecast category"""
    is_active: bool | None = None
    """Whether the stage is currently active and can be used"""
    is_closed: bool | None = None
    """Whether opportunities at this stage are considered closed"""
    is_won: bool | None = None
    """Whether opportunities at this stage are considered won"""
    last_modified_by_id: str | None = None
    """ID of the user who last modified this stage"""
    last_modified_date: str | None = None
    """Date and time when the stage was last modified"""
    master_label: str | None = None
    """Display label for the stage"""
    sort_order: int | None = None
    """Order in which the stage appears in the sales process"""
    system_modstamp: str | None = None
    """System timestamp when the record was last modified"""


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

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""

OpportunityStagesSearchResult = AirbyteSearchResult[OpportunityStagesSearchData]
"""Search result type for opportunity_stages entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

SobjectsListResult = SalesforceExecuteResult[list[SObject]]
"""Result type for sobjects.list operation."""

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

ReportsListResult = SalesforceExecuteResult[list[Report]]
"""Result type for reports.list operation."""

UsersListResult = SalesforceExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

OpportunityStagesListResult = SalesforceExecuteResultWithMeta[list[OpportunityStage], OpportunityStagesListResultMeta]
"""Result type for opportunity_stages.list operation with data and metadata."""

QueryListResult = SalesforceExecuteResultWithMeta[list[dict[str, Any]], QueryListResultMeta]
"""Result type for query.list operation with data and metadata."""

