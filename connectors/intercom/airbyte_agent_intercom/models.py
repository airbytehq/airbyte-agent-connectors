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
    """Metadata for contacts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)

class ConversationsListResultMeta(BaseModel):
    """Metadata for conversations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)

class CompaniesListResultMeta(BaseModel):
    """Metadata for companies.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)

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
    type: str | None = None
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
    type: str | None = None
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
    type: str | None = None
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
    type: str | None = None
    """Type of team (e.g., 'internal', 'external')."""


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

