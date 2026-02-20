"""
Pydantic models for pylon connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class PylonAuthConfig(BaseModel):
    """API Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_token: str
    """Your Pylon API token. Only admin users can create API tokens."""

# Replication configuration

class PylonReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Pylon."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date and time in the format YYYY-MM-DDTHH:mm:ssZ from which to start replicating data."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Pagination(BaseModel):
    """Pagination type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_next_page: Union[bool, Any] = Field(default=None)

class MiniAccount(BaseModel):
    """MiniAccount type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class MiniUser(BaseModel):
    """MiniUser type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class MiniContact(BaseModel):
    """MiniContact type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class MiniTeam(BaseModel):
    """MiniTeam type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)

class SlackInfo(BaseModel):
    """SlackInfo type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel_id: Union[str | None, Any] = Field(default=None)
    message_ts: Union[str | None, Any] = Field(default=None)
    workspace_id: Union[str | None, Any] = Field(default=None)

class IssueChatWidgetInfo(BaseModel):
    """IssueChatWidgetInfo type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_url: Union[str | None, Any] = Field(default=None)

class CSATResponse(BaseModel):
    """CSATResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comment: Union[str | None, Any] = Field(default=None)
    score: Union[int | None, Any] = Field(default=None)

class CustomFieldValue(BaseModel):
    """CustomFieldValue type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    slug: Union[str | None, Any] = Field(default=None)
    value: Union[str | None, Any] = Field(default=None)
    values: Union[list[str] | None, Any] = Field(default=None)

class ExternalIssue(BaseModel):
    """ExternalIssue type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    external_id: Union[str | None, Any] = Field(default=None)
    link: Union[str | None, Any] = Field(default=None)
    source: Union[str | None, Any] = Field(default=None)

class Issue(BaseModel):
    """Issue type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    account: Union[Any, Any] = Field(default=None)
    assignee: Union[Any, Any] = Field(default=None)
    attachment_urls: Union[list[str] | None, Any] = Field(default=None)
    author_unverified: Union[bool | None, Any] = Field(default=None)
    body_html: Union[str | None, Any] = Field(default=None)
    business_hours_first_response_seconds: Union[int | None, Any] = Field(default=None)
    business_hours_resolution_seconds: Union[int | None, Any] = Field(default=None)
    chat_widget_info: Union[Any, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    csat_responses: Union[list[CSATResponse] | None, Any] = Field(default=None)
    custom_fields: Union[dict[str, CustomFieldValue] | None, Any] = Field(default=None)
    customer_portal_visible: Union[bool | None, Any] = Field(default=None)
    external_issues: Union[list[ExternalIssue] | None, Any] = Field(default=None)
    first_response_seconds: Union[int | None, Any] = Field(default=None)
    first_response_time: Union[str | None, Any] = Field(default=None)
    latest_message_time: Union[str | None, Any] = Field(default=None)
    link: Union[str | None, Any] = Field(default=None)
    number: Union[int | None, Any] = Field(default=None)
    number_of_touches: Union[int | None, Any] = Field(default=None)
    requester: Union[Any, Any] = Field(default=None)
    resolution_seconds: Union[int | None, Any] = Field(default=None)
    resolution_time: Union[str | None, Any] = Field(default=None)
    slack: Union[Any, Any] = Field(default=None)
    snoozed_until_time: Union[str | None, Any] = Field(default=None)
    source: Union[Any, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    tags: Union[list[str] | None, Any] = Field(default=None)
    team: Union[Any, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    type: Union[Any, Any] = Field(default=None)

class IssuesResponse(BaseModel):
    """IssuesResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Issue], Any] = Field(default=None)
    pagination: Union[Pagination, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class IssueResponse(BaseModel):
    """IssueResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Issue, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class MessageAuthor(BaseModel):
    """MessageAuthor type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_url: Union[str | None, Any] = Field(default=None)
    contact: Union[Any, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    user: Union[Any, Any] = Field(default=None)

class EmailMessageInfo(BaseModel):
    """EmailMessageInfo type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bcc_emails: Union[list[str] | None, Any] = Field(default=None)
    cc_emails: Union[list[str] | None, Any] = Field(default=None)
    from_email: Union[str | None, Any] = Field(default=None)
    message_id: Union[str | None, Any] = Field(default=None)
    to_emails: Union[list[str] | None, Any] = Field(default=None)

class Message(BaseModel):
    """Message type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    author: Union[Any, Any] = Field(default=None)
    email_info: Union[Any, Any] = Field(default=None)
    file_urls: Union[list[str] | None, Any] = Field(default=None)
    is_private: Union[bool | None, Any] = Field(default=None)
    message_html: Union[str | None, Any] = Field(default=None)
    source: Union[str | None, Any] = Field(default=None)
    thread_id: Union[str | None, Any] = Field(default=None)
    timestamp: Union[str | None, Any] = Field(default=None)

class MessagesResponse(BaseModel):
    """MessagesResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Message], Any] = Field(default=None)
    pagination: Union[Pagination, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class AccountChannel(BaseModel):
    """AccountChannel type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel_id: Union[str | None, Any] = Field(default=None)
    source: Union[str | None, Any] = Field(default=None)
    is_primary: Union[bool | None, Any] = Field(default=None)

class Account(BaseModel):
    """Account type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    channels: Union[list[AccountChannel] | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    custom_fields: Union[dict[str, Any] | None, Any] = Field(default=None)
    domain: Union[str | None, Any] = Field(default=None)
    domains: Union[list[str] | None, Any] = Field(default=None)
    external_ids: Union[dict[str, Any] | None, Any] = Field(default=None)
    is_disabled: Union[bool | None, Any] = Field(default=None)
    latest_customer_activity_time: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    owner: Union[Any, Any] = Field(default=None)
    primary_domain: Union[str | None, Any] = Field(default=None)
    tags: Union[list[str] | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)

class AccountsResponse(BaseModel):
    """AccountsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Account], Any] = Field(default=None)
    pagination: Union[Pagination, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class AccountResponse(BaseModel):
    """AccountResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Account, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class AccountCreateParams(BaseModel):
    """AccountCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    domains: Union[list[str], Any] = Field(default=None)
    primary_domain: Union[str, Any] = Field(default=None)
    owner_id: Union[str, Any] = Field(default=None)
    logo_url: Union[str, Any] = Field(default=None)
    tags: Union[list[str], Any] = Field(default=None)

class AccountUpdateParams(BaseModel):
    """AccountUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    domains: Union[list[str], Any] = Field(default=None)
    primary_domain: Union[str, Any] = Field(default=None)
    owner_id: Union[str, Any] = Field(default=None)
    logo_url: Union[str, Any] = Field(default=None)
    is_disabled: Union[bool, Any] = Field(default=None)
    tags: Union[list[str], Any] = Field(default=None)

class IntegrationUserId(BaseModel):
    """IntegrationUserId type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    source: Union[str | None, Any] = Field(default=None)

class Contact(BaseModel):
    """Contact type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    account: Union[Any, Any] = Field(default=None)
    avatar_url: Union[str | None, Any] = Field(default=None)
    custom_fields: Union[dict[str, Any] | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    emails: Union[list[str] | None, Any] = Field(default=None)
    integration_user_ids: Union[list[IntegrationUserId] | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    phone_numbers: Union[list[str] | None, Any] = Field(default=None)
    portal_role: Union[str | None, Any] = Field(default=None)
    portal_role_id: Union[str | None, Any] = Field(default=None)

class ContactsResponse(BaseModel):
    """ContactsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Contact], Any] = Field(default=None)
    pagination: Union[Pagination, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class ContactResponse(BaseModel):
    """ContactResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Contact, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class Team(BaseModel):
    """Team type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    users: Union[list[MiniUser] | None, Any] = Field(default=None)

class TeamsResponse(BaseModel):
    """TeamsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Team], Any] = Field(default=None)
    pagination: Union[Pagination, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class TeamResponse(BaseModel):
    """TeamResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Team, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class Tag(BaseModel):
    """Tag type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    hex_color: Union[str | None, Any] = Field(default=None)
    object_type: Union[str | None, Any] = Field(default=None)
    value: Union[str | None, Any] = Field(default=None)

class TagsResponse(BaseModel):
    """TagsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Tag], Any] = Field(default=None)
    pagination: Union[Pagination, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class TagResponse(BaseModel):
    """TagResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Tag, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class User(BaseModel):
    """User type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    avatar_url: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    emails: Union[list[str] | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    role_id: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)

class UsersResponse(BaseModel):
    """UsersResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[User], Any] = Field(default=None)
    pagination: Union[Pagination, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class UserResponse(BaseModel):
    """UserResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[User, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class SelectOption(BaseModel):
    """SelectOption type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)

class NumberMetadata(BaseModel):
    """NumberMetadata type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency: Union[str | None, Any] = Field(default=None)
    decimal_places: Union[int | None, Any] = Field(default=None)
    format: Union[str | None, Any] = Field(default=None)

class SelectMetadata(BaseModel):
    """SelectMetadata type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    options: Union[list[SelectOption] | None, Any] = Field(default=None)

class CustomField(BaseModel):
    """CustomField type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    default_value: Union[str | None, Any] = Field(default=None)
    default_values: Union[list[str] | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    is_read_only: Union[bool | None, Any] = Field(default=None)
    label: Union[str | None, Any] = Field(default=None)
    number_metadata: Union[Any, Any] = Field(default=None)
    object_type: Union[str | None, Any] = Field(default=None)
    select_metadata: Union[Any, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)
    source: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class CustomFieldsResponse(BaseModel):
    """CustomFieldsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[CustomField], Any] = Field(default=None)
    pagination: Union[Pagination, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class CustomFieldResponse(BaseModel):
    """CustomFieldResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[CustomField, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class TicketFormField(BaseModel):
    """TicketFormField type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description_html: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)

class TicketForm(BaseModel):
    """TicketForm type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    description_html: Union[str | None, Any] = Field(default=None)
    fields: Union[list[TicketFormField] | None, Any] = Field(default=None)
    is_public: Union[bool | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)

class TicketFormsResponse(BaseModel):
    """TicketFormsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[TicketForm], Any] = Field(default=None)
    pagination: Union[Pagination, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class UserRole(BaseModel):
    """UserRole type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)

class UserRolesResponse(BaseModel):
    """UserRolesResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[UserRole], Any] = Field(default=None)
    pagination: Union[Pagination, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class MeResponse(BaseModel):
    """MeResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[User, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class IssueCreateParams(BaseModel):
    """IssueCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: Union[str, Any] = Field(default=None)
    body_html: Union[str, Any] = Field(default=None)
    priority: Union[str, Any] = Field(default=None)
    requester_email: Union[str, Any] = Field(default=None)
    requester_name: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None)
    assignee_id: Union[str, Any] = Field(default=None)
    team_id: Union[str, Any] = Field(default=None)
    tags: Union[list[str], Any] = Field(default=None)

class IssueUpdateParams(BaseModel):
    """IssueUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    state: Union[str, Any] = Field(default=None)
    assignee_id: Union[str, Any] = Field(default=None)
    team_id: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None)
    tags: Union[list[str], Any] = Field(default=None)

class IssueNoteCreateParams(BaseModel):
    """IssueNoteCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body_html: Union[str, Any] = Field(default=None)
    thread_id: Union[str, Any] = Field(default=None)
    message_id: Union[str, Any] = Field(default=None)

class IssueNote(BaseModel):
    """IssueNote type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    body_html: Union[str | None, Any] = Field(default=None)
    timestamp: Union[str | None, Any] = Field(default=None)

class IssueNoteResponse(BaseModel):
    """IssueNoteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[IssueNote, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class IssueThreadCreateParams(BaseModel):
    """IssueThreadCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class IssueThread(BaseModel):
    """IssueThread type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class IssueThreadResponse(BaseModel):
    """IssueThreadResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[IssueThread, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class ContactCreateParams(BaseModel):
    """ContactCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    email: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None)
    avatar_url: Union[str, Any] = Field(default=None)

class ContactUpdateParams(BaseModel):
    """ContactUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    email: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None)

class TeamCreateParams(BaseModel):
    """TeamCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class TeamUpdateParams(BaseModel):
    """TeamUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class TagCreateParams(BaseModel):
    """TagCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: Union[str, Any] = Field(default=None)
    object_type: Union[str, Any] = Field(default=None)
    hex_color: Union[str, Any] = Field(default=None)

class TagUpdateParams(BaseModel):
    """TagUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: Union[str, Any] = Field(default=None)
    hex_color: Union[str, Any] = Field(default=None)

class Task(BaseModel):
    """Task type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    body_html: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    assignee_id: Union[str | None, Any] = Field(default=None)
    project_id: Union[str | None, Any] = Field(default=None)
    milestone_id: Union[str | None, Any] = Field(default=None)
    due_date: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class TaskCreateParams(BaseModel):
    """TaskCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: Union[str, Any] = Field(default=None)
    body_html: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    assignee_id: Union[str, Any] = Field(default=None)
    project_id: Union[str, Any] = Field(default=None)
    milestone_id: Union[str, Any] = Field(default=None)
    due_date: Union[str, Any] = Field(default=None)

class TaskUpdateParams(BaseModel):
    """TaskUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: Union[str, Any] = Field(default=None)
    body_html: Union[str, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    assignee_id: Union[str, Any] = Field(default=None)

class TaskResponse(BaseModel):
    """TaskResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Task, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class Project(BaseModel):
    """Project type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description_html: Union[str | None, Any] = Field(default=None)
    account_id: Union[str | None, Any] = Field(default=None)
    owner_id: Union[str | None, Any] = Field(default=None)
    start_date: Union[str | None, Any] = Field(default=None)
    end_date: Union[str | None, Any] = Field(default=None)
    is_archived: Union[bool | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class ProjectCreateParams(BaseModel):
    """ProjectCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    account_id: Union[str, Any] = Field(default=None)
    description_html: Union[str, Any] = Field(default=None)
    start_date: Union[str, Any] = Field(default=None)
    end_date: Union[str, Any] = Field(default=None)

class ProjectUpdateParams(BaseModel):
    """ProjectUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    description_html: Union[str, Any] = Field(default=None)
    is_archived: Union[bool, Any] = Field(default=None)

class ProjectResponse(BaseModel):
    """ProjectResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Project, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class Milestone(BaseModel):
    """Milestone type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    project_id: Union[str | None, Any] = Field(default=None)
    due_date: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class MilestoneCreateParams(BaseModel):
    """MilestoneCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    project_id: Union[str, Any] = Field(default=None)
    due_date: Union[str, Any] = Field(default=None)

class MilestoneUpdateParams(BaseModel):
    """MilestoneUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    due_date: Union[str, Any] = Field(default=None)

class MilestoneResponse(BaseModel):
    """MilestoneResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Milestone, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class Article(BaseModel):
    """Article type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    body_html: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)
    is_published: Union[bool | None, Any] = Field(default=None)
    author_user_id: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class ArticleCreateParams(BaseModel):
    """ArticleCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: Union[str, Any] = Field(default=None)
    body_html: Union[str, Any] = Field(default=None)
    author_user_id: Union[str, Any] = Field(default=None)
    slug: Union[str, Any] = Field(default=None)
    is_published: Union[bool, Any] = Field(default=None)

class ArticleUpdateParams(BaseModel):
    """ArticleUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: Union[str, Any] = Field(default=None)
    body_html: Union[str, Any] = Field(default=None)

class ArticleResponse(BaseModel):
    """ArticleResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Article, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

class Collection(BaseModel):
    """Collection type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)

class CollectionCreateParams(BaseModel):
    """CollectionCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    slug: Union[str, Any] = Field(default=None)

class CollectionResponse(BaseModel):
    """CollectionResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Collection, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class IssuesListResultMeta(BaseModel):
    """Metadata for issues.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_next_page: Union[bool, Any] = Field(default=None)

class MessagesListResultMeta(BaseModel):
    """Metadata for messages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_next_page: Union[bool, Any] = Field(default=None)

class AccountsListResultMeta(BaseModel):
    """Metadata for accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_next_page: Union[bool, Any] = Field(default=None)

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_next_page: Union[bool, Any] = Field(default=None)

class TeamsListResultMeta(BaseModel):
    """Metadata for teams.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_next_page: Union[bool, Any] = Field(default=None)

class TagsListResultMeta(BaseModel):
    """Metadata for tags.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_next_page: Union[bool, Any] = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_next_page: Union[bool, Any] = Field(default=None)

class CustomFieldsListResultMeta(BaseModel):
    """Metadata for custom_fields.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_next_page: Union[bool, Any] = Field(default=None)

class TicketFormsListResultMeta(BaseModel):
    """Metadata for ticket_forms.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_next_page: Union[bool, Any] = Field(default=None)

class UserRolesListResultMeta(BaseModel):
    """Metadata for user_roles.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_next_page: Union[bool, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class PylonCheckResult(BaseModel):
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


class PylonExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class PylonExecuteResultWithMeta(PylonExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

IssuesListResult = PylonExecuteResultWithMeta[list[Issue], IssuesListResultMeta]
"""Result type for issues.list operation with data and metadata."""

MessagesListResult = PylonExecuteResultWithMeta[list[Message], MessagesListResultMeta]
"""Result type for messages.list operation with data and metadata."""

AccountsListResult = PylonExecuteResultWithMeta[list[Account], AccountsListResultMeta]
"""Result type for accounts.list operation with data and metadata."""

ContactsListResult = PylonExecuteResultWithMeta[list[Contact], ContactsListResultMeta]
"""Result type for contacts.list operation with data and metadata."""

TeamsListResult = PylonExecuteResultWithMeta[list[Team], TeamsListResultMeta]
"""Result type for teams.list operation with data and metadata."""

TagsListResult = PylonExecuteResultWithMeta[list[Tag], TagsListResultMeta]
"""Result type for tags.list operation with data and metadata."""

UsersListResult = PylonExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

CustomFieldsListResult = PylonExecuteResultWithMeta[list[CustomField], CustomFieldsListResultMeta]
"""Result type for custom_fields.list operation with data and metadata."""

TicketFormsListResult = PylonExecuteResultWithMeta[list[TicketForm], TicketFormsListResultMeta]
"""Result type for ticket_forms.list operation with data and metadata."""

UserRolesListResult = PylonExecuteResultWithMeta[list[UserRole], UserRolesListResultMeta]
"""Result type for user_roles.list operation with data and metadata."""

