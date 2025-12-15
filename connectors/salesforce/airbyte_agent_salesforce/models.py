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


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

