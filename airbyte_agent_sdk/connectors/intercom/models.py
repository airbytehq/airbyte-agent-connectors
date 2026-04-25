"""
Pydantic models for intercom connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class IntercomAuthConfig(BaseModel):
    """Access Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """Your Intercom API Access Token"""

# Replication configuration

class IntercomReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Intercom."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date and time in the format YYYY-MM-DDTHH:mm:ssZ from which to start replicating data."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class PagesNext(BaseModel):
    """Cursor for next page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page: int | None | None = Field(default=None, description="Next page number")
    """Next page number"""
    starting_after: str | None | None = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class Pages(BaseModel):
    """Pagination metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    page: int | None = Field(default=None)
    per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    next: PagesNext | None = Field(default=None)

class Contact(BaseModel):
    """Contact object representing a user or lead"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    workspace_id: str | None = Field(default=None)
    external_id: str | None = Field(default=None)
    role: str | None = Field(default=None)
    email: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    name: str | None = Field(default=None)
    avatar: str | None = Field(default=None)
    owner_id: int | None = Field(default=None)
    social_profiles: Any | None = Field(default=None)
    has_hard_bounced: bool | None = Field(default=None)
    marked_email_as_spam: bool | None = Field(default=None)
    unsubscribed_from_emails: bool | None = Field(default=None)
    created_at: int | None = Field(default=None)
    updated_at: int | None = Field(default=None)
    signed_up_at: int | None = Field(default=None)
    last_seen_at: int | None = Field(default=None)
    last_replied_at: int | None = Field(default=None)
    last_contacted_at: int | None = Field(default=None)
    last_email_opened_at: int | None = Field(default=None)
    last_email_clicked_at: int | None = Field(default=None)
    language_override: str | None = Field(default=None)
    browser: str | None = Field(default=None)
    browser_version: str | None = Field(default=None)
    browser_language: str | None = Field(default=None)
    os: str | None = Field(default=None)
    location: Any | None = Field(default=None)
    android_app_name: str | None = Field(default=None)
    android_app_version: str | None = Field(default=None)
    android_device: str | None = Field(default=None)
    android_os_version: str | None = Field(default=None)
    android_sdk_version: str | None = Field(default=None)
    android_last_seen_at: int | None = Field(default=None)
    ios_app_name: str | None = Field(default=None)
    ios_app_version: str | None = Field(default=None)
    ios_device: str | None = Field(default=None)
    ios_os_version: str | None = Field(default=None)
    ios_sdk_version: str | None = Field(default=None)
    ios_last_seen_at: int | None = Field(default=None)
    custom_attributes: dict[str, Any] | None = Field(default=None)
    tags: Any | None = Field(default=None)
    notes: Any | None = Field(default=None)
    companies: Any | None = Field(default=None)

class SocialProfile(BaseModel):
    """Social profile"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    name: str | None = Field(default=None)
    url: str | None = Field(default=None)

class SocialProfiles(BaseModel):
    """Social profiles"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    data: list[SocialProfile] | None = Field(default=None)

class Location(BaseModel):
    """Location information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    country: str | None = Field(default=None)
    region: str | None = Field(default=None)
    city: str | None = Field(default=None)
    country_code: str | None = Field(default=None)
    continent_code: str | None = Field(default=None)

class TagReference(BaseModel):
    """Tag reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    url: str | None = Field(default=None)

class ContactTags(BaseModel):
    """Tags associated with contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    data: list[TagReference] | None = Field(default=None)

class NoteReference(BaseModel):
    """Note reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    url: str | None = Field(default=None)

class ContactNotes(BaseModel):
    """Notes associated with contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    data: list[NoteReference] | None = Field(default=None)

class CompanyReference(BaseModel):
    """Company reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    url: str | None = Field(default=None)

class ContactCompanies(BaseModel):
    """Companies associated with contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    data: list[CompanyReference] | None = Field(default=None)

class ContactsListPagesNext(BaseModel):
    """Cursor for next page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page: int | None | None = Field(default=None, description="Next page number")
    """Next page number"""
    starting_after: str | None | None = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class ContactsListPages(BaseModel):
    """Pagination metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type", description="Type of pagination")
    """Type of pagination"""
    page: int | None | None = Field(default=None, description="Current page number")
    """Current page number"""
    per_page: int | None | None = Field(default=None, description="Number of items per page")
    """Number of items per page"""
    total_pages: int | None | None = Field(default=None, description="Total number of pages")
    """Total number of pages"""
    next: ContactsListPagesNext | None | None = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class ContactsList(BaseModel):
    """Paginated list of contacts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    data: list[Contact] | None = Field(default=None)
    total_count: int | None = Field(default=None)
    pages: ContactsListPages | None = Field(default=None)

class Conversation(BaseModel):
    """Conversation object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    created_at: int | None = Field(default=None)
    updated_at: int | None = Field(default=None)
    waiting_since: int | None = Field(default=None)
    snoozed_until: int | None = Field(default=None)
    open: bool | None = Field(default=None)
    state: str | None = Field(default=None)
    read: bool | None = Field(default=None)
    priority: str | None = Field(default=None)
    admin_assignee_id: int | None = Field(default=None)
    team_assignee_id: str | None = Field(default=None)
    tags: Any | None = Field(default=None)
    conversation_rating: Any | None = Field(default=None)
    source: Any | None = Field(default=None)
    contacts: Any | None = Field(default=None)
    teammates: Any | None = Field(default=None)
    first_contact_reply: Any | None = Field(default=None)
    sla_applied: Any | None = Field(default=None)
    statistics: Any | None = Field(default=None)
    conversation_parts: Any | None = Field(default=None)
    custom_attributes: dict[str, Any] | None = Field(default=None)

class Tag(BaseModel):
    """Tag object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    applied_at: int | None = Field(default=None)
    applied_by: Any | None = Field(default=None)

class ConversationTags(BaseModel):
    """Tags on conversation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    tags: list[Tag] | None = Field(default=None)

class ConversationRating(BaseModel):
    """Conversation rating"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rating: int | None = Field(default=None)
    remark: str | None = Field(default=None)
    created_at: int | None = Field(default=None)
    contact: Any | None = Field(default=None)
    teammate: Any | None = Field(default=None)

class ContactReference(BaseModel):
    """Contact reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)

class AdminReference(BaseModel):
    """Admin reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)

class Attachment(BaseModel):
    """Message attachment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    name: str | None = Field(default=None)
    url: str | None = Field(default=None)
    content_type: str | None = Field(default=None)
    filesize: int | None = Field(default=None)
    width: int | None = Field(default=None)
    height: int | None = Field(default=None)

class ConversationSource(BaseModel):
    """Conversation source"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    delivered_as: str | None = Field(default=None)
    subject: str | None = Field(default=None)
    body: str | None = Field(default=None)
    author: Any | None = Field(default=None)
    attachments: list[Attachment] | None = Field(default=None)
    url: str | None = Field(default=None)
    redacted: bool | None = Field(default=None)

class Author(BaseModel):
    """Message author"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    email: str | None = Field(default=None)

class ConversationContacts(BaseModel):
    """Contacts in conversation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    contacts: list[ContactReference] | None = Field(default=None)

class ConversationTeammates(BaseModel):
    """Teammates in conversation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    admins: list[AdminReference] | None = Field(default=None)

class FirstContactReply(BaseModel):
    """First contact reply info"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    url: str | None = Field(default=None)

class SlaApplied(BaseModel):
    """SLA applied to conversation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    sla_name: str | None = Field(default=None)
    sla_status: str | None = Field(default=None)

class ConversationStatistics(BaseModel):
    """Conversation statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    time_to_assignment: int | None = Field(default=None)
    time_to_admin_reply: int | None = Field(default=None)
    time_to_first_close: int | None = Field(default=None)
    time_to_last_close: int | None = Field(default=None)
    median_time_to_reply: int | None = Field(default=None)
    first_contact_reply_at: int | None = Field(default=None)
    first_assignment_at: int | None = Field(default=None)
    first_admin_reply_at: int | None = Field(default=None)
    first_close_at: int | None = Field(default=None)
    last_assignment_at: int | None = Field(default=None)
    last_assignment_admin_reply_at: int | None = Field(default=None)
    last_contact_reply_at: int | None = Field(default=None)
    last_admin_reply_at: int | None = Field(default=None)
    last_close_at: int | None = Field(default=None)
    last_closed_by_id: str | None = Field(default=None)
    count_reopens: int | None = Field(default=None)
    count_assignments: int | None = Field(default=None)
    count_conversation_parts: int | None = Field(default=None)

class ConversationPart(BaseModel):
    """Conversation part (message, note, action)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    part_type: str | None = Field(default=None)
    body: str | None = Field(default=None)
    created_at: int | None = Field(default=None)
    updated_at: int | None = Field(default=None)
    notified_at: int | None = Field(default=None)
    assigned_to: Any | None = Field(default=None)
    author: Any | None = Field(default=None)
    attachments: list[Attachment] | None = Field(default=None)
    external_id: str | None = Field(default=None)
    redacted: bool | None = Field(default=None)

class ConversationPartsReference(BaseModel):
    """Reference to conversation parts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    conversation_parts: list[ConversationPart] | None = Field(default=None)
    total_count: int | None = Field(default=None)

class ConversationsListPagesNext(BaseModel):
    """Cursor for next page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page: int | None | None = Field(default=None, description="Next page number")
    """Next page number"""
    starting_after: str | None | None = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class ConversationsListPages(BaseModel):
    """Pagination metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type", description="Type of pagination")
    """Type of pagination"""
    page: int | None | None = Field(default=None, description="Current page number")
    """Current page number"""
    per_page: int | None | None = Field(default=None, description="Number of items per page")
    """Number of items per page"""
    total_pages: int | None | None = Field(default=None, description="Total number of pages")
    """Total number of pages"""
    next: ConversationsListPagesNext | None | None = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class ConversationsList(BaseModel):
    """Paginated list of conversations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    conversations: list[Conversation] | None = Field(default=None)
    total_count: int | None = Field(default=None)
    pages: ConversationsListPages | None = Field(default=None)

class Company(BaseModel):
    """Company object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    app_id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    company_id: str | None = Field(default=None)
    plan: Any | None = Field(default=None)
    size: int | None = Field(default=None)
    industry: str | None = Field(default=None)
    website: str | None = Field(default=None)
    remote_created_at: int | None = Field(default=None)
    created_at: int | None = Field(default=None)
    updated_at: int | None = Field(default=None)
    last_request_at: int | None = Field(default=None)
    session_count: int | None = Field(default=None)
    monthly_spend: float | None = Field(default=None)
    user_count: int | None = Field(default=None)
    tags: Any | None = Field(default=None)
    segments: Any | None = Field(default=None)
    custom_attributes: dict[str, Any] | None = Field(default=None)

class CompanyPlan(BaseModel):
    """Company plan"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)

class CompanyTags(BaseModel):
    """Tags on company"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    tags: list[Tag] | None = Field(default=None)

class Segment(BaseModel):
    """Segment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    created_at: int | None = Field(default=None)
    updated_at: int | None = Field(default=None)
    person_type: str | None = Field(default=None)
    count: int | None = Field(default=None)

class CompanySegments(BaseModel):
    """Segments for company"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    segments: list[Segment] | None = Field(default=None)

class CompaniesListPagesNext(BaseModel):
    """Cursor for next page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page: int | None | None = Field(default=None, description="Next page number")
    """Next page number"""
    starting_after: str | None | None = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class CompaniesListPages(BaseModel):
    """Pagination metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type", description="Type of pagination")
    """Type of pagination"""
    page: int | None | None = Field(default=None, description="Current page number")
    """Current page number"""
    per_page: int | None | None = Field(default=None, description="Number of items per page")
    """Number of items per page"""
    total_pages: int | None | None = Field(default=None, description="Total number of pages")
    """Total number of pages"""
    next: CompaniesListPagesNext | None | None = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class CompaniesList(BaseModel):
    """Paginated list of companies"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    data: list[Company] | None = Field(default=None)
    total_count: int | None = Field(default=None)
    pages: CompaniesListPages | None = Field(default=None)

class Team(BaseModel):
    """Team object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    admin_ids: list[int] | None = Field(default=None)
    admin_priority_level: Any | None = Field(default=None)

class AdminPriorityLevel(BaseModel):
    """Admin priority level settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    primary_admin_ids: list[int] | None = Field(default=None)
    secondary_admin_ids: list[int] | None = Field(default=None)

class TeamsList(BaseModel):
    """List of teams"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    teams: list[Team] | None = Field(default=None)

class Admin(BaseModel):
    """Admin object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    email_verified: bool | None = Field(default=None)
    job_title: str | None = Field(default=None)
    away_mode_enabled: bool | None = Field(default=None)
    away_mode_reassign: bool | None = Field(default=None)
    has_inbox_seat: bool | None = Field(default=None)
    team_ids: list[int] | None = Field(default=None)
    avatar: Any | None = Field(default=None)

class Avatar(BaseModel):
    """Avatar image"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    image_url: str | None = Field(default=None)

class AdminsList(BaseModel):
    """List of admins"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    admins: list[Admin] | None = Field(default=None)

class TagsList(BaseModel):
    """List of tags"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    data: list[Tag] | None = Field(default=None)

class SegmentsList(BaseModel):
    """List of segments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    segments: list[Segment] | None = Field(default=None)

class ContactCreateParams(BaseModel):
    """ContactCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    role: str
    external_id: str | None = Field(default=None)
    email: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    name: str | None = Field(default=None)
    avatar: str | None = Field(default=None)
    signed_up_at: int | None = Field(default=None)
    last_seen_at: int | None = Field(default=None)
    owner_id: int | None = Field(default=None)
    unsubscribed_from_emails: bool | None = Field(default=None)
    custom_attributes: dict[str, Any] | None = Field(default=None)

class ContactUpdateParams(BaseModel):
    """ContactUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    role: str | None = Field(default=None)
    external_id: str | None = Field(default=None)
    email: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    name: str | None = Field(default=None)
    avatar: str | None = Field(default=None)
    signed_up_at: int | None = Field(default=None)
    last_seen_at: int | None = Field(default=None)
    owner_id: int | None = Field(default=None)
    unsubscribed_from_emails: bool | None = Field(default=None)
    custom_attributes: dict[str, Any] | None = Field(default=None)

class CompanyCreateParams(BaseModel):
    """CompanyCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    company_id: str
    name: str | None = Field(default=None)
    plan: str | None = Field(default=None)
    monthly_spend: float | None = Field(default=None)
    size: int | None = Field(default=None)
    website: str | None = Field(default=None)
    industry: str | None = Field(default=None)
    custom_attributes: dict[str, Any] | None = Field(default=None)

class CompanyUpdateParams(BaseModel):
    """CompanyUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    plan: str | None = Field(default=None)
    monthly_spend: float | None = Field(default=None)
    size: int | None = Field(default=None)
    website: str | None = Field(default=None)
    industry: str | None = Field(default=None)
    custom_attributes: dict[str, Any] | None = Field(default=None)

class TagCreateParams(BaseModel):
    """TagCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str

class NoteCreateParams(BaseModel):
    """NoteCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: str
    admin_id: str | None = Field(default=None)

class Note(BaseModel):
    """Note object on a contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    id: str | None = Field(default=None)
    created_at: int | None = Field(default=None)
    contact: Any | None = Field(default=None)
    author: Any | None = Field(default=None)
    body: str | None = Field(default=None)

class InternalArticleCreateParams(BaseModel):
    """InternalArticleCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str
    body: str | None = Field(default=None)
    owner_id: int
    author_id: int

class InternalArticle(BaseModel):
    """Internal article object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Any | None = Field(default=None)
    title: str | None = Field(default=None)
    body: str | None = Field(default=None)
    owner_id: int | None = Field(default=None)
    author_id: int | None = Field(default=None)
    created_at: int | None = Field(default=None)
    updated_at: int | None = Field(default=None)
    locale: str | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: str | None = Field(default=None)

class ConversationsListResultMeta(BaseModel):
    """Metadata for conversations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: str | None = Field(default=None)

class CompaniesListResultMeta(BaseModel):
    """Metadata for companies.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class IntercomCheckResult(BaseModel):
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


class IntercomExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class IntercomExecuteResultWithMeta(IntercomExecuteResult[T], Generic[T, S]):
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

    app_id: str | None = None
    """The ID of the application associated with the company"""
    company_id: str | None = None
    """The unique identifier of the company"""
    created_at: int | None = None
    """The date and time when the company was created"""
    custom_attributes: dict[str, Any] | None = None
    """Custom attributes specific to the company"""
    id: str | None = None
    """The ID of the company"""
    industry: str | None = None
    """The industry in which the company operates"""
    monthly_spend: float | None = None
    """The monthly spend of the company"""
    name: str | None = None
    """The name of the company"""
    plan: dict[str, Any] | None = None
    """Details of the company's subscription plan"""
    remote_created_at: int | None = None
    """The remote date and time when the company was created"""
    segments: dict[str, Any] | None = None
    """Segments associated with the company"""
    session_count: int | None = None
    """The number of sessions related to the company"""
    size: int | None = None
    """The size of the company"""
    tags: dict[str, Any] | None = None
    """Tags associated with the company"""
    type_: str | None = None
    """The type of the company"""
    updated_at: int | None = None
    """The date and time when the company was last updated"""
    user_count: int | None = None
    """The number of users associated with the company"""
    website: str | None = None
    """The website of the company"""


class ContactsSearchData(BaseModel):
    """Search result data for contacts entity."""
    model_config = ConfigDict(extra="allow")

    android_app_name: str | None = None
    """The name of the Android app associated with the contact."""
    android_app_version: str | None = None
    """The version of the Android app associated with the contact."""
    android_device: str | None = None
    """The device used by the contact for Android."""
    android_last_seen_at: str | None = None
    """The date and time when the contact was last seen on Android."""
    android_os_version: str | None = None
    """The operating system version of the Android device."""
    android_sdk_version: str | None = None
    """The SDK version of the Android device."""
    avatar: str | None = None
    """URL pointing to the contact's avatar image."""
    browser: str | None = None
    """The browser used by the contact."""
    browser_language: str | None = None
    """The language preference set in the contact's browser."""
    browser_version: str | None = None
    """The version of the browser used by the contact."""
    companies: dict[str, Any] | None = None
    """Companies associated with the contact."""
    created_at: int | None = None
    """The date and time when the contact was created."""
    custom_attributes: dict[str, Any] | None = None
    """Custom attributes defined for the contact."""
    email: str | None = None
    """The email address of the contact."""
    external_id: str | None = None
    """External identifier for the contact."""
    has_hard_bounced: bool | None = None
    """Flag indicating if the contact has hard bounced."""
    id: str | None = None
    """The unique identifier of the contact."""
    ios_app_name: str | None = None
    """The name of the iOS app associated with the contact."""
    ios_app_version: str | None = None
    """The version of the iOS app associated with the contact."""
    ios_device: str | None = None
    """The device used by the contact for iOS."""
    ios_last_seen_at: int | None = None
    """The date and time when the contact was last seen on iOS."""
    ios_os_version: str | None = None
    """The operating system version of the iOS device."""
    ios_sdk_version: str | None = None
    """The SDK version of the iOS device."""
    language_override: str | None = None
    """Language override set for the contact."""
    last_contacted_at: int | None = None
    """The date and time when the contact was last contacted."""
    last_email_clicked_at: int | None = None
    """The date and time when the contact last clicked an email."""
    last_email_opened_at: int | None = None
    """The date and time when the contact last opened an email."""
    last_replied_at: int | None = None
    """The date and time when the contact last replied."""
    last_seen_at: int | None = None
    """The date and time when the contact was last seen overall."""
    location: dict[str, Any] | None = None
    """Location details of the contact."""
    marked_email_as_spam: bool | None = None
    """Flag indicating if the contact's email was marked as spam."""
    name: str | None = None
    """The name of the contact."""
    notes: dict[str, Any] | None = None
    """Notes associated with the contact."""
    opted_in_subscription_types: dict[str, Any] | None = None
    """Subscription types the contact opted into."""
    opted_out_subscription_types: dict[str, Any] | None = None
    """Subscription types the contact opted out from."""
    os: str | None = None
    """Operating system of the contact's device."""
    owner_id: int | None = None
    """The unique identifier of the contact's owner."""
    phone: str | None = None
    """The phone number of the contact."""
    referrer: str | None = None
    """Referrer information related to the contact."""
    role: str | None = None
    """Role or position of the contact."""
    signed_up_at: int | None = None
    """The date and time when the contact signed up."""
    sms_consent: bool | None = None
    """Consent status for SMS communication."""
    social_profiles: dict[str, Any] | None = None
    """Social profiles associated with the contact."""
    tags: dict[str, Any] | None = None
    """Tags associated with the contact."""
    type_: str | None = None
    """Type of contact."""
    unsubscribed_from_emails: bool | None = None
    """Flag indicating if the contact unsubscribed from emails."""
    unsubscribed_from_sms: bool | None = None
    """Flag indicating if the contact unsubscribed from SMS."""
    updated_at: int | None = None
    """The date and time when the contact was last updated."""
    utm_campaign: str | None = None
    """Campaign data from UTM parameters."""
    utm_content: str | None = None
    """Content data from UTM parameters."""
    utm_medium: str | None = None
    """Medium data from UTM parameters."""
    utm_source: str | None = None
    """Source data from UTM parameters."""
    utm_term: str | None = None
    """Term data from UTM parameters."""
    workspace_id: str | None = None
    """The unique identifier of the workspace associated with the contact."""


class ConversationsSearchData(BaseModel):
    """Search result data for conversations entity."""
    model_config = ConfigDict(extra="allow")

    admin_assignee_id: int | None = None
    """The ID of the administrator assigned to the conversation"""
    ai_agent: dict[str, Any] | None = None
    """Data related to AI Agent involvement in the conversation"""
    ai_agent_participated: bool | None = None
    """Indicates whether AI Agent participated in the conversation"""
    assignee: dict[str, Any] | None = None
    """The assigned user responsible for the conversation."""
    contacts: dict[str, Any] | None = None
    """List of contacts involved in the conversation."""
    conversation_message: dict[str, Any] | None = None
    """The main message content of the conversation."""
    conversation_rating: dict[str, Any] | None = None
    """Ratings given to the conversation by the customer and teammate."""
    created_at: int | None = None
    """The timestamp when the conversation was created"""
    custom_attributes: dict[str, Any] | None = None
    """Custom attributes associated with the conversation"""
    customer_first_reply: dict[str, Any] | None = None
    """Timestamp indicating when the customer first replied."""
    customers: list[Any] | None = None
    """List of customers involved in the conversation"""
    first_contact_reply: dict[str, Any] | None = None
    """Timestamp indicating when the first contact replied."""
    id: str | None = None
    """The unique ID of the conversation"""
    linked_objects: dict[str, Any] | None = None
    """Linked objects associated with the conversation"""
    open: bool | None = None
    """Indicates if the conversation is open or closed"""
    priority: str | None = None
    """The priority level of the conversation"""
    read: bool | None = None
    """Indicates if the conversation has been read"""
    redacted: bool | None = None
    """Indicates if the conversation is redacted"""
    sent_at: int | None = None
    """The timestamp when the conversation was sent"""
    sla_applied: dict[str, Any] | None = None
    """Service Level Agreement details applied to the conversation."""
    snoozed_until: int | None = None
    """Timestamp until the conversation is snoozed"""
    source: dict[str, Any] | None = None
    """Source details of the conversation."""
    state: str | None = None
    """The state of the conversation (e.g., new, in progress)"""
    statistics: dict[str, Any] | None = None
    """Statistics related to the conversation."""
    tags: dict[str, Any] | None = None
    """Tags applied to the conversation."""
    team_assignee_id: int | None = None
    """The ID of the team assigned to the conversation"""
    teammates: dict[str, Any] | None = None
    """List of teammates involved in the conversation."""
    title: str | None = None
    """The title of the conversation"""
    topics: dict[str, Any] | None = None
    """Topics associated with the conversation."""
    type_: str | None = None
    """The type of the conversation"""
    updated_at: int | None = None
    """The timestamp when the conversation was last updated"""
    user: dict[str, Any] | None = None
    """The user related to the conversation."""
    waiting_since: int | None = None
    """Timestamp since waiting for a response"""


class TeamsSearchData(BaseModel):
    """Search result data for teams entity."""
    model_config = ConfigDict(extra="allow")

    admin_ids: list[Any] | None = None
    """Array of user IDs representing the admins of the team."""
    id: str | None = None
    """Unique identifier for the team."""
    name: str | None = None
    """Name of the team."""
    type_: str | None = None
    """Type of team (e.g., 'internal', 'external')."""


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

ConversationsSearchResult = AirbyteSearchResult[ConversationsSearchData]
"""Search result type for conversations entity."""

TeamsSearchResult = AirbyteSearchResult[TeamsSearchData]
"""Search result type for teams entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

ContactsListResult = IntercomExecuteResultWithMeta[list[Contact], ContactsListResultMeta]
"""Result type for contacts.list operation with data and metadata."""

ConversationsListResult = IntercomExecuteResultWithMeta[list[Conversation], ConversationsListResultMeta]
"""Result type for conversations.list operation with data and metadata."""

CompaniesListResult = IntercomExecuteResultWithMeta[list[Company], CompaniesListResultMeta]
"""Result type for companies.list operation with data and metadata."""

TeamsListResult = IntercomExecuteResult[list[Team]]
"""Result type for teams.list operation."""

AdminsListResult = IntercomExecuteResult[list[Admin]]
"""Result type for admins.list operation."""

TagsListResult = IntercomExecuteResult[list[Tag]]
"""Result type for tags.list operation."""

SegmentsListResult = IntercomExecuteResult[list[Segment]]
"""Result type for segments.list operation."""

