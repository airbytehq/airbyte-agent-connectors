"""
Pydantic models for intercom connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class IntercomAuthConfig(BaseModel):
    """Access Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """Your Intercom API Access Token"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class PagesNext(BaseModel):
    """Cursor for next page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page: Union[int | None, Any] = Field(default=None, description="Next page number")
    """Next page number"""
    starting_after: Union[str | None, Any] = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class Pages(BaseModel):
    """Pagination metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    per_page: Union[int | None, Any] = Field(default=None)
    total_pages: Union[int | None, Any] = Field(default=None)
    next: Union[PagesNext | None, Any] = Field(default=None)

class Contact(BaseModel):
    """Contact object representing a user or lead"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    workspace_id: Union[str | None, Any] = Field(default=None)
    external_id: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    avatar: Union[str | None, Any] = Field(default=None)
    owner_id: Union[int | None, Any] = Field(default=None)
    social_profiles: Union[Any, Any] = Field(default=None)
    has_hard_bounced: Union[bool | None, Any] = Field(default=None)
    marked_email_as_spam: Union[bool | None, Any] = Field(default=None)
    unsubscribed_from_emails: Union[bool | None, Any] = Field(default=None)
    created_at: Union[int | None, Any] = Field(default=None)
    updated_at: Union[int | None, Any] = Field(default=None)
    signed_up_at: Union[int | None, Any] = Field(default=None)
    last_seen_at: Union[int | None, Any] = Field(default=None)
    last_replied_at: Union[int | None, Any] = Field(default=None)
    last_contacted_at: Union[int | None, Any] = Field(default=None)
    last_email_opened_at: Union[int | None, Any] = Field(default=None)
    last_email_clicked_at: Union[int | None, Any] = Field(default=None)
    language_override: Union[str | None, Any] = Field(default=None)
    browser: Union[str | None, Any] = Field(default=None)
    browser_version: Union[str | None, Any] = Field(default=None)
    browser_language: Union[str | None, Any] = Field(default=None)
    os: Union[str | None, Any] = Field(default=None)
    location: Union[Any, Any] = Field(default=None)
    android_app_name: Union[str | None, Any] = Field(default=None)
    android_app_version: Union[str | None, Any] = Field(default=None)
    android_device: Union[str | None, Any] = Field(default=None)
    android_os_version: Union[str | None, Any] = Field(default=None)
    android_sdk_version: Union[str | None, Any] = Field(default=None)
    android_last_seen_at: Union[int | None, Any] = Field(default=None)
    ios_app_name: Union[str | None, Any] = Field(default=None)
    ios_app_version: Union[str | None, Any] = Field(default=None)
    ios_device: Union[str | None, Any] = Field(default=None)
    ios_os_version: Union[str | None, Any] = Field(default=None)
    ios_sdk_version: Union[str | None, Any] = Field(default=None)
    ios_last_seen_at: Union[int | None, Any] = Field(default=None)
    custom_attributes: Union[dict[str, Any] | None, Any] = Field(default=None)
    tags: Union[Any, Any] = Field(default=None)
    notes: Union[Any, Any] = Field(default=None)
    companies: Union[Any, Any] = Field(default=None)

class SocialProfile(BaseModel):
    """Social profile"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)

class SocialProfiles(BaseModel):
    """Social profiles"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    data: Union[list[SocialProfile], Any] = Field(default=None)

class Location(BaseModel):
    """Location information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)
    region: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    country_code: Union[str | None, Any] = Field(default=None)
    continent_code: Union[str | None, Any] = Field(default=None)

class TagReference(BaseModel):
    """Tag reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)

class ContactTags(BaseModel):
    """Tags associated with contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    data: Union[list[TagReference], Any] = Field(default=None)

class NoteReference(BaseModel):
    """Note reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)

class ContactNotes(BaseModel):
    """Notes associated with contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    data: Union[list[NoteReference], Any] = Field(default=None)

class CompanyReference(BaseModel):
    """Company reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)

class ContactCompanies(BaseModel):
    """Companies associated with contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    data: Union[list[CompanyReference], Any] = Field(default=None)

class ContactsListPagesNext(BaseModel):
    """Cursor for next page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page: Union[int | None, Any] = Field(default=None, description="Next page number")
    """Next page number"""
    starting_after: Union[str | None, Any] = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class ContactsListPages(BaseModel):
    """Pagination metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None, description="Type of pagination")
    """Type of pagination"""
    page: Union[int | None, Any] = Field(default=None, description="Current page number")
    """Current page number"""
    per_page: Union[int | None, Any] = Field(default=None, description="Number of items per page")
    """Number of items per page"""
    total_pages: Union[int | None, Any] = Field(default=None, description="Total number of pages")
    """Total number of pages"""
    next: Union[ContactsListPagesNext | None, Any] = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class ContactsList(BaseModel):
    """Paginated list of contacts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    data: Union[list[Contact], Any] = Field(default=None)
    total_count: Union[int | None, Any] = Field(default=None)
    pages: Union[ContactsListPages | None, Any] = Field(default=None)

class Conversation(BaseModel):
    """Conversation object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    created_at: Union[int | None, Any] = Field(default=None)
    updated_at: Union[int | None, Any] = Field(default=None)
    waiting_since: Union[int | None, Any] = Field(default=None)
    snoozed_until: Union[int | None, Any] = Field(default=None)
    open: Union[bool | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    read: Union[bool | None, Any] = Field(default=None)
    priority: Union[str | None, Any] = Field(default=None)
    admin_assignee_id: Union[int | None, Any] = Field(default=None)
    team_assignee_id: Union[str | None, Any] = Field(default=None)
    tags: Union[Any, Any] = Field(default=None)
    conversation_rating: Union[Any, Any] = Field(default=None)
    source: Union[Any, Any] = Field(default=None)
    contacts: Union[Any, Any] = Field(default=None)
    teammates: Union[Any, Any] = Field(default=None)
    first_contact_reply: Union[Any, Any] = Field(default=None)
    sla_applied: Union[Any, Any] = Field(default=None)
    statistics: Union[Any, Any] = Field(default=None)
    conversation_parts: Union[Any, Any] = Field(default=None)
    custom_attributes: Union[dict[str, Any] | None, Any] = Field(default=None)

class Tag(BaseModel):
    """Tag object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    applied_at: Union[int | None, Any] = Field(default=None)
    applied_by: Union[Any, Any] = Field(default=None)

class ConversationTags(BaseModel):
    """Tags on conversation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    tags: Union[list[Tag], Any] = Field(default=None)

class ConversationRating(BaseModel):
    """Conversation rating"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rating: Union[int | None, Any] = Field(default=None)
    remark: Union[str | None, Any] = Field(default=None)
    created_at: Union[int | None, Any] = Field(default=None)
    contact: Union[Any, Any] = Field(default=None)
    teammate: Union[Any, Any] = Field(default=None)

class ContactReference(BaseModel):
    """Contact reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class AdminReference(BaseModel):
    """Admin reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class Attachment(BaseModel):
    """Message attachment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)
    content_type: Union[str | None, Any] = Field(default=None)
    filesize: Union[int | None, Any] = Field(default=None)
    width: Union[int | None, Any] = Field(default=None)
    height: Union[int | None, Any] = Field(default=None)

class ConversationSource(BaseModel):
    """Conversation source"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)
    delivered_as: Union[str | None, Any] = Field(default=None)
    subject: Union[str | None, Any] = Field(default=None)
    body: Union[str | None, Any] = Field(default=None)
    author: Union[Any, Any] = Field(default=None)
    attachments: Union[list[Attachment], Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)
    redacted: Union[bool | None, Any] = Field(default=None)

class Author(BaseModel):
    """Message author"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)

class ConversationContacts(BaseModel):
    """Contacts in conversation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    contacts: Union[list[ContactReference], Any] = Field(default=None)

class ConversationTeammates(BaseModel):
    """Teammates in conversation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    admins: Union[list[AdminReference], Any] = Field(default=None)

class FirstContactReply(BaseModel):
    """First contact reply info"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: Union[int | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)

class SlaApplied(BaseModel):
    """SLA applied to conversation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    sla_name: Union[str | None, Any] = Field(default=None)
    sla_status: Union[str | None, Any] = Field(default=None)

class ConversationStatistics(BaseModel):
    """Conversation statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    time_to_assignment: Union[int | None, Any] = Field(default=None)
    time_to_admin_reply: Union[int | None, Any] = Field(default=None)
    time_to_first_close: Union[int | None, Any] = Field(default=None)
    time_to_last_close: Union[int | None, Any] = Field(default=None)
    median_time_to_reply: Union[int | None, Any] = Field(default=None)
    first_contact_reply_at: Union[int | None, Any] = Field(default=None)
    first_assignment_at: Union[int | None, Any] = Field(default=None)
    first_admin_reply_at: Union[int | None, Any] = Field(default=None)
    first_close_at: Union[int | None, Any] = Field(default=None)
    last_assignment_at: Union[int | None, Any] = Field(default=None)
    last_assignment_admin_reply_at: Union[int | None, Any] = Field(default=None)
    last_contact_reply_at: Union[int | None, Any] = Field(default=None)
    last_admin_reply_at: Union[int | None, Any] = Field(default=None)
    last_close_at: Union[int | None, Any] = Field(default=None)
    last_closed_by_id: Union[str | None, Any] = Field(default=None)
    count_reopens: Union[int | None, Any] = Field(default=None)
    count_assignments: Union[int | None, Any] = Field(default=None)
    count_conversation_parts: Union[int | None, Any] = Field(default=None)

class ConversationPart(BaseModel):
    """Conversation part (message, note, action)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    part_type: Union[str | None, Any] = Field(default=None)
    body: Union[str | None, Any] = Field(default=None)
    created_at: Union[int | None, Any] = Field(default=None)
    updated_at: Union[int | None, Any] = Field(default=None)
    notified_at: Union[int | None, Any] = Field(default=None)
    assigned_to: Union[Any, Any] = Field(default=None)
    author: Union[Any, Any] = Field(default=None)
    attachments: Union[list[Attachment], Any] = Field(default=None)
    external_id: Union[str | None, Any] = Field(default=None)
    redacted: Union[bool | None, Any] = Field(default=None)

class ConversationPartsReference(BaseModel):
    """Reference to conversation parts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    conversation_parts: Union[list[ConversationPart], Any] = Field(default=None)
    total_count: Union[int | None, Any] = Field(default=None)

class ConversationsListPagesNext(BaseModel):
    """Cursor for next page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page: Union[int | None, Any] = Field(default=None, description="Next page number")
    """Next page number"""
    starting_after: Union[str | None, Any] = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class ConversationsListPages(BaseModel):
    """Pagination metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None, description="Type of pagination")
    """Type of pagination"""
    page: Union[int | None, Any] = Field(default=None, description="Current page number")
    """Current page number"""
    per_page: Union[int | None, Any] = Field(default=None, description="Number of items per page")
    """Number of items per page"""
    total_pages: Union[int | None, Any] = Field(default=None, description="Total number of pages")
    """Total number of pages"""
    next: Union[ConversationsListPagesNext | None, Any] = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class ConversationsList(BaseModel):
    """Paginated list of conversations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    conversations: Union[list[Conversation], Any] = Field(default=None)
    total_count: Union[int | None, Any] = Field(default=None)
    pages: Union[ConversationsListPages | None, Any] = Field(default=None)

class Company(BaseModel):
    """Company object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    company_id: Union[str | None, Any] = Field(default=None)
    plan: Union[Any, Any] = Field(default=None)
    size: Union[int | None, Any] = Field(default=None)
    industry: Union[str | None, Any] = Field(default=None)
    website: Union[str | None, Any] = Field(default=None)
    remote_created_at: Union[int | None, Any] = Field(default=None)
    created_at: Union[int | None, Any] = Field(default=None)
    updated_at: Union[int | None, Any] = Field(default=None)
    last_request_at: Union[int | None, Any] = Field(default=None)
    session_count: Union[int | None, Any] = Field(default=None)
    monthly_spend: Union[float | None, Any] = Field(default=None)
    user_count: Union[int | None, Any] = Field(default=None)
    tags: Union[Any, Any] = Field(default=None)
    segments: Union[Any, Any] = Field(default=None)
    custom_attributes: Union[dict[str, Any] | None, Any] = Field(default=None)

class CompanyPlan(BaseModel):
    """Company plan"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class CompanyTags(BaseModel):
    """Tags on company"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    tags: Union[list[Tag], Any] = Field(default=None)

class Segment(BaseModel):
    """Segment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    created_at: Union[int | None, Any] = Field(default=None)
    updated_at: Union[int | None, Any] = Field(default=None)
    person_type: Union[str | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

class CompanySegments(BaseModel):
    """Segments for company"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    segments: Union[list[Segment], Any] = Field(default=None)

class CompaniesListPagesNext(BaseModel):
    """Cursor for next page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page: Union[int | None, Any] = Field(default=None, description="Next page number")
    """Next page number"""
    starting_after: Union[str | None, Any] = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class CompaniesListPages(BaseModel):
    """Pagination metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None, description="Type of pagination")
    """Type of pagination"""
    page: Union[int | None, Any] = Field(default=None, description="Current page number")
    """Current page number"""
    per_page: Union[int | None, Any] = Field(default=None, description="Number of items per page")
    """Number of items per page"""
    total_pages: Union[int | None, Any] = Field(default=None, description="Total number of pages")
    """Total number of pages"""
    next: Union[CompaniesListPagesNext | None, Any] = Field(default=None, description="Cursor for next page")
    """Cursor for next page"""

class CompaniesList(BaseModel):
    """Paginated list of companies"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    data: Union[list[Company], Any] = Field(default=None)
    total_count: Union[int | None, Any] = Field(default=None)
    pages: Union[CompaniesListPages | None, Any] = Field(default=None)

class Team(BaseModel):
    """Team object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    admin_ids: Union[list[int], Any] = Field(default=None)
    admin_priority_level: Union[Any, Any] = Field(default=None)

class AdminPriorityLevel(BaseModel):
    """Admin priority level settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    primary_admin_ids: Union[list[int], Any] = Field(default=None)
    secondary_admin_ids: Union[list[int], Any] = Field(default=None)

class TeamsList(BaseModel):
    """List of teams"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    teams: Union[list[Team], Any] = Field(default=None)

class Admin(BaseModel):
    """Admin object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    email_verified: Union[bool | None, Any] = Field(default=None)
    job_title: Union[str | None, Any] = Field(default=None)
    away_mode_enabled: Union[bool | None, Any] = Field(default=None)
    away_mode_reassign: Union[bool | None, Any] = Field(default=None)
    has_inbox_seat: Union[bool | None, Any] = Field(default=None)
    team_ids: Union[list[int], Any] = Field(default=None)
    avatar: Union[Any, Any] = Field(default=None)

class Avatar(BaseModel):
    """Avatar image"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    image_url: Union[str | None, Any] = Field(default=None)

class AdminsList(BaseModel):
    """List of admins"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    admins: Union[list[Admin], Any] = Field(default=None)

class TagsList(BaseModel):
    """List of tags"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    data: Union[list[Tag], Any] = Field(default=None)

class SegmentsList(BaseModel):
    """List of segments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    segments: Union[list[Segment], Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)

class ConversationsListResultMeta(BaseModel):
    """Metadata for conversations.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)

class CompaniesListResultMeta(BaseModel):
    """Metadata for companies.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)

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

