"""
Pydantic models for pylon connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class PylonAuthConfig(BaseModel):
    """API Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_token: str
    """Your Pylon API token. Only admin users can create API tokens."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Pagination(BaseModel):
    """Pagination type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_next_page: bool | None = Field(default=None)

class MiniAccount(BaseModel):
    """MiniAccount type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class MiniUser(BaseModel):
    """MiniUser type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None = Field(default=None)
    id: str | None = Field(default=None)

class MiniContact(BaseModel):
    """MiniContact type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None = Field(default=None)
    id: str | None = Field(default=None)

class MiniTeam(BaseModel):
    """MiniTeam type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class SlackInfo(BaseModel):
    """SlackInfo type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel_id: str | None = Field(default=None)
    message_ts: str | None = Field(default=None)
    workspace_id: str | None = Field(default=None)

class IssueChatWidgetInfo(BaseModel):
    """IssueChatWidgetInfo type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page_url: str | None = Field(default=None)

class CSATResponse(BaseModel):
    """CSATResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comment: str | None = Field(default=None)
    score: int | None = Field(default=None)

class CustomFieldValue(BaseModel):
    """CustomFieldValue type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    slug: str | None = Field(default=None)
    value: str | None = Field(default=None)
    values: list[str] | None = Field(default=None)

class ExternalIssue(BaseModel):
    """ExternalIssue type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    external_id: str | None = Field(default=None)
    link: str | None = Field(default=None)
    source: str | None = Field(default=None)

class Issue(BaseModel):
    """Issue type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    account: Any | None = Field(default=None)
    assignee: Any | None = Field(default=None)
    attachment_urls: list[str] | None = Field(default=None)
    author_unverified: bool | None = Field(default=None)
    body_html: str | None = Field(default=None)
    business_hours_first_response_seconds: int | None = Field(default=None)
    business_hours_resolution_seconds: int | None = Field(default=None)
    business_hours_time_in_status_seconds: dict[str, int] | None = Field(default=None)
    chat_widget_info: Any | None = Field(default=None)
    created_at: str | None = Field(default=None)
    csat_responses: list[CSATResponse] | None = Field(default=None)
    custom_fields: dict[str, CustomFieldValue] | None = Field(default=None)
    customer_portal_visible: bool | None = Field(default=None)
    external_issues: list[ExternalIssue] | None = Field(default=None)
    first_response_seconds: int | None = Field(default=None)
    first_response_time: str | None = Field(default=None)
    latest_message_time: str | None = Field(default=None)
    link: str | None = Field(default=None)
    number: int | None = Field(default=None)
    number_of_touches: int | None = Field(default=None)
    requester: Any | None = Field(default=None)
    resolution_seconds: int | None = Field(default=None)
    resolution_time: str | None = Field(default=None)
    slack: Any | None = Field(default=None)
    snoozed_until_time: str | None = Field(default=None)
    source: Any | None = Field(default=None)
    state: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    team: Any | None = Field(default=None)
    title: str | None = Field(default=None)
    time_in_status_seconds: dict[str, int] | None = Field(default=None)
    type_: Any | None = Field(default=None, alias="type")
    updated_at: str | None = Field(default=None)

class IssuesResponse(BaseModel):
    """IssuesResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Issue] | None = Field(default=None)
    pagination: Pagination | None = Field(default=None)
    request_id: str | None = Field(default=None)

class IssueResponse(BaseModel):
    """IssueResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Issue | None = Field(default=None)
    request_id: str | None = Field(default=None)

class MessageAuthor(BaseModel):
    """MessageAuthor type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_url: str | None = Field(default=None)
    contact: Any | None = Field(default=None)
    name: str | None = Field(default=None)
    user: Any | None = Field(default=None)

class EmailMessageInfo(BaseModel):
    """EmailMessageInfo type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bcc_emails: list[str] | None = Field(default=None)
    cc_emails: list[str] | None = Field(default=None)
    from_email: str | None = Field(default=None)
    message_id: str | None = Field(default=None)
    to_emails: list[str] | None = Field(default=None)

class Message(BaseModel):
    """Message type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    author: Any | None = Field(default=None)
    email_info: Any | None = Field(default=None)
    file_urls: list[str] | None = Field(default=None)
    is_private: bool | None = Field(default=None)
    message_html: str | None = Field(default=None)
    source: str | None = Field(default=None)
    thread_id: str | None = Field(default=None)
    timestamp: str | None = Field(default=None)

class MessagesResponse(BaseModel):
    """MessagesResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Message] | None = Field(default=None)
    pagination: Pagination | None = Field(default=None)
    request_id: str | None = Field(default=None)

class AccountChannel(BaseModel):
    """AccountChannel type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    channel_id: str | None = Field(default=None)
    source: str | None = Field(default=None)
    is_primary: bool | None = Field(default=None)

class Account(BaseModel):
    """Account type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    channels: list[AccountChannel] | None = Field(default=None)
    created_at: str | None = Field(default=None)
    custom_fields: dict[str, Any] | None = Field(default=None)
    domain: str | None = Field(default=None)
    domains: list[str] | None = Field(default=None)
    external_ids: dict[str, Any] | None = Field(default=None)
    is_disabled: bool | None = Field(default=None)
    latest_customer_activity_time: str | None = Field(default=None)
    name: str | None = Field(default=None)
    owner: Any | None = Field(default=None)
    primary_domain: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")

class AccountsResponse(BaseModel):
    """AccountsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Account] | None = Field(default=None)
    pagination: Pagination | None = Field(default=None)
    request_id: str | None = Field(default=None)

class AccountResponse(BaseModel):
    """AccountResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Account | None = Field(default=None)
    request_id: str | None = Field(default=None)

class AccountCreateParams(BaseModel):
    """AccountCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    domains: list[str] | None = Field(default=None)
    primary_domain: str | None = Field(default=None)
    owner_id: str | None = Field(default=None)
    logo_url: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)

class AccountUpdateParams(BaseModel):
    """AccountUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    domains: list[str] | None = Field(default=None)
    primary_domain: str | None = Field(default=None)
    owner_id: str | None = Field(default=None)
    logo_url: str | None = Field(default=None)
    is_disabled: bool | None = Field(default=None)
    tags: list[str] | None = Field(default=None)

class IntegrationUserId(BaseModel):
    """IntegrationUserId type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    source: str | None = Field(default=None)

class Contact(BaseModel):
    """Contact type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    account: Any | None = Field(default=None)
    avatar_url: str | None = Field(default=None)
    custom_fields: dict[str, Any] | None = Field(default=None)
    email: str | None = Field(default=None)
    emails: list[str] | None = Field(default=None)
    integration_user_ids: list[IntegrationUserId] | None = Field(default=None)
    name: str | None = Field(default=None)
    phone_numbers: list[str] | None = Field(default=None)
    portal_role: str | None = Field(default=None)
    portal_role_id: str | None = Field(default=None)

class ContactsResponse(BaseModel):
    """ContactsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Contact] | None = Field(default=None)
    pagination: Pagination | None = Field(default=None)
    request_id: str | None = Field(default=None)

class ContactResponse(BaseModel):
    """ContactResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Contact | None = Field(default=None)
    request_id: str | None = Field(default=None)

class Team(BaseModel):
    """Team type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    users: list[MiniUser] | None = Field(default=None)

class TeamsResponse(BaseModel):
    """TeamsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Team] | None = Field(default=None)
    pagination: Pagination | None = Field(default=None)
    request_id: str | None = Field(default=None)

class TeamResponse(BaseModel):
    """TeamResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Team | None = Field(default=None)
    request_id: str | None = Field(default=None)

class Tag(BaseModel):
    """Tag type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    hex_color: str | None = Field(default=None)
    object_type: str | None = Field(default=None)
    value: str | None = Field(default=None)

class TagsResponse(BaseModel):
    """TagsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Tag] | None = Field(default=None)
    pagination: Pagination | None = Field(default=None)
    request_id: str | None = Field(default=None)

class TagResponse(BaseModel):
    """TagResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Tag | None = Field(default=None)
    request_id: str | None = Field(default=None)

class User(BaseModel):
    """User type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    avatar_url: str | None = Field(default=None)
    email: str | None = Field(default=None)
    emails: list[str] | None = Field(default=None)
    name: str | None = Field(default=None)
    role_id: str | None = Field(default=None)
    status: str | None = Field(default=None)

class UsersResponse(BaseModel):
    """UsersResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[User] | None = Field(default=None)
    pagination: Pagination | None = Field(default=None)
    request_id: str | None = Field(default=None)

class UserResponse(BaseModel):
    """UserResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: User | None = Field(default=None)
    request_id: str | None = Field(default=None)

class SelectOption(BaseModel):
    """SelectOption type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str | None = Field(default=None)
    slug: str | None = Field(default=None)

class NumberMetadata(BaseModel):
    """NumberMetadata type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency: str | None = Field(default=None)
    decimal_places: int | None = Field(default=None)
    format: str | None = Field(default=None)

class SelectMetadata(BaseModel):
    """SelectMetadata type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    options: list[SelectOption] | None = Field(default=None)

class CustomField(BaseModel):
    """CustomField type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    default_value: str | None = Field(default=None)
    default_values: list[str] | None = Field(default=None)
    description: str | None = Field(default=None)
    is_read_only: bool | None = Field(default=None)
    label: str | None = Field(default=None)
    number_metadata: Any | None = Field(default=None)
    object_type: str | None = Field(default=None)
    select_metadata: Any | None = Field(default=None)
    slug: str | None = Field(default=None)
    source: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    updated_at: str | None = Field(default=None)

class CustomFieldsResponse(BaseModel):
    """CustomFieldsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[CustomField] | None = Field(default=None)
    pagination: Pagination | None = Field(default=None)
    request_id: str | None = Field(default=None)

class CustomFieldResponse(BaseModel):
    """CustomFieldResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: CustomField | None = Field(default=None)
    request_id: str | None = Field(default=None)

class TicketFormField(BaseModel):
    """TicketFormField type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description_html: str | None = Field(default=None)
    name: str | None = Field(default=None)
    slug: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")

class TicketForm(BaseModel):
    """TicketForm type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    description_html: str | None = Field(default=None)
    fields: list[TicketFormField] | None = Field(default=None)
    is_public: bool | None = Field(default=None)
    name: str | None = Field(default=None)
    slug: str | None = Field(default=None)
    url: str | None = Field(default=None)

class TicketFormsResponse(BaseModel):
    """TicketFormsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[TicketForm] | None = Field(default=None)
    pagination: Pagination | None = Field(default=None)
    request_id: str | None = Field(default=None)

class UserRole(BaseModel):
    """UserRole type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    slug: str | None = Field(default=None)

class UserRolesResponse(BaseModel):
    """UserRolesResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[UserRole] | None = Field(default=None)
    pagination: Pagination | None = Field(default=None)
    request_id: str | None = Field(default=None)

class MeResponse(BaseModel):
    """MeResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: User | None = Field(default=None)
    request_id: str | None = Field(default=None)

class IssueCreateParams(BaseModel):
    """IssueCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str
    body_html: str
    priority: str | None = Field(default=None)
    requester_email: str | None = Field(default=None)
    requester_name: str | None = Field(default=None)
    account_id: str | None = Field(default=None)
    assignee_id: str | None = Field(default=None)
    team_id: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)

class IssueUpdateParams(BaseModel):
    """IssueUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    state: str | None = Field(default=None)
    assignee_id: str | None = Field(default=None)
    team_id: str | None = Field(default=None)
    account_id: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)

class IssueNoteCreateParams(BaseModel):
    """IssueNoteCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body_html: str
    thread_id: str | None = Field(default=None)
    message_id: str | None = Field(default=None)

class IssueNote(BaseModel):
    """IssueNote type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    body_html: str | None = Field(default=None)
    timestamp: str | None = Field(default=None)

class IssueNoteResponse(BaseModel):
    """IssueNoteResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: IssueNote | None = Field(default=None)
    request_id: str | None = Field(default=None)

class IssueThreadCreateParams(BaseModel):
    """IssueThreadCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)

class IssueThread(BaseModel):
    """IssueThread type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)

class IssueThreadResponse(BaseModel):
    """IssueThreadResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: IssueThread | None = Field(default=None)
    request_id: str | None = Field(default=None)

class IssueReplyCreateParams(BaseModel):
    """IssueReplyCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body_html: str
    message_id: str
    user_id: str | None = Field(default=None)
    contact_id: str | None = Field(default=None)
    attachment_urls: list[str] | None = Field(default=None)

class IssueReplyData(BaseModel):
    """IssueReplyData type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    issue_id: str | None = Field(default=None)

class IssueReplyResponse(BaseModel):
    """IssueReplyResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: IssueReplyData | None = Field(default=None)
    request_id: str | None = Field(default=None)

class IssueAssignParams(BaseModel):
    """IssueAssignParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assignee_id: str | None = Field(default=None)
    team_id: str | None = Field(default=None)

class IssueStatusUpdateParams(BaseModel):
    """IssueStatusUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    state: str

class DeleteIssueResponse(BaseModel):
    """DeleteIssueResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None)

class ContactCreateParams(BaseModel):
    """ContactCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    email: str | None = Field(default=None)
    account_id: str | None = Field(default=None)
    avatar_url: str | None = Field(default=None)

class ContactUpdateParams(BaseModel):
    """ContactUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    account_id: str | None = Field(default=None)

class TeamCreateParams(BaseModel):
    """TeamCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)

class TeamUpdateParams(BaseModel):
    """TeamUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)

class TagCreateParams(BaseModel):
    """TagCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: str
    object_type: str
    hex_color: str | None = Field(default=None)

class TagUpdateParams(BaseModel):
    """TagUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: str | None = Field(default=None)
    hex_color: str | None = Field(default=None)

class Task(BaseModel):
    """Task type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    body_html: str | None = Field(default=None)
    status: str | None = Field(default=None)
    assignee_id: str | None = Field(default=None)
    project_id: str | None = Field(default=None)
    milestone_id: str | None = Field(default=None)
    due_date: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class TaskCreateParams(BaseModel):
    """TaskCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str
    body_html: str | None = Field(default=None)
    status: str | None = Field(default=None)
    assignee_id: str | None = Field(default=None)
    project_id: str | None = Field(default=None)
    milestone_id: str | None = Field(default=None)
    due_date: str | None = Field(default=None)

class TaskUpdateParams(BaseModel):
    """TaskUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None = Field(default=None)
    body_html: str | None = Field(default=None)
    status: str | None = Field(default=None)
    assignee_id: str | None = Field(default=None)

class TaskResponse(BaseModel):
    """TaskResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Task | None = Field(default=None)
    request_id: str | None = Field(default=None)

class Project(BaseModel):
    """Project type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    description_html: str | None = Field(default=None)
    account_id: str | None = Field(default=None)
    owner_id: str | None = Field(default=None)
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    is_archived: bool | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class ProjectCreateParams(BaseModel):
    """ProjectCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    account_id: str
    description_html: str | None = Field(default=None)
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)

class ProjectUpdateParams(BaseModel):
    """ProjectUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    description_html: str | None = Field(default=None)
    is_archived: bool | None = Field(default=None)

class ProjectResponse(BaseModel):
    """ProjectResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Project | None = Field(default=None)
    request_id: str | None = Field(default=None)

class Milestone(BaseModel):
    """Milestone type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    project_id: str | None = Field(default=None)
    due_date: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class MilestoneCreateParams(BaseModel):
    """MilestoneCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    project_id: str
    due_date: str | None = Field(default=None)

class MilestoneUpdateParams(BaseModel):
    """MilestoneUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    due_date: str | None = Field(default=None)

class MilestoneResponse(BaseModel):
    """MilestoneResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Milestone | None = Field(default=None)
    request_id: str | None = Field(default=None)

class Article(BaseModel):
    """Article type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    body_html: str | None = Field(default=None)
    slug: str | None = Field(default=None)
    is_published: bool | None = Field(default=None)
    author_user_id: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class ArticleCreateParams(BaseModel):
    """ArticleCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str
    body_html: str
    author_user_id: str
    slug: str | None = Field(default=None)
    is_published: bool | None = Field(default=None)

class ArticleUpdateParams(BaseModel):
    """ArticleUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None = Field(default=None)
    body_html: str | None = Field(default=None)

class ArticleResponse(BaseModel):
    """ArticleResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Article | None = Field(default=None)
    request_id: str | None = Field(default=None)

class Collection(BaseModel):
    """Collection type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    description: str | None = Field(default=None)
    slug: str | None = Field(default=None)
    created_at: str | None = Field(default=None)

class CollectionCreateParams(BaseModel):
    """CollectionCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str
    description: str | None = Field(default=None)
    slug: str | None = Field(default=None)

class CollectionResponse(BaseModel):
    """CollectionResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Collection | None = Field(default=None)
    request_id: str | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class IssuesListResultMeta(BaseModel):
    """Metadata for issues.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_next_page: bool | None = Field(default=None)

class MessagesListResultMeta(BaseModel):
    """Metadata for messages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_next_page: bool | None = Field(default=None)

class AccountsListResultMeta(BaseModel):
    """Metadata for accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_next_page: bool | None = Field(default=None)

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_next_page: bool | None = Field(default=None)

class TeamsListResultMeta(BaseModel):
    """Metadata for teams.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_next_page: bool | None = Field(default=None)

class TagsListResultMeta(BaseModel):
    """Metadata for tags.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_next_page: bool | None = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_next_page: bool | None = Field(default=None)

class CustomFieldsListResultMeta(BaseModel):
    """Metadata for custom_fields.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_next_page: bool | None = Field(default=None)

class TicketFormsListResultMeta(BaseModel):
    """Metadata for ticket_forms.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_next_page: bool | None = Field(default=None)

class UserRolesListResultMeta(BaseModel):
    """Metadata for user_roles.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_next_page: bool | None = Field(default=None)

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

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class IssuesSearchData(BaseModel):
    """Search result data for issues entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the issue"""
    title: str | None = None
    """Title of the issue"""
    state: str | None = None
    """Current state of the issue (e.g. new, in_progress, closed)"""
    source: str | None = None
    """Channel the issue originated from (e.g. email, slack)"""
    type_: str | None = None
    """Type classification of the issue"""
    number: int | None = None
    """Human-readable issue number within the workspace"""
    created_at: str | None = None
    """Timestamp when the issue was created, in ISO 8601 format"""
    latest_message_time: str | None = None
    """Timestamp of the most recent message on the issue, in ISO 8601 format"""
    resolution_time: str | None = None
    """Timestamp when the issue was resolved, in ISO 8601 format"""
    snoozed_until_time: str | None = None
    """Timestamp the issue is snoozed until, in ISO 8601 format"""
    customer_portal_visible: bool | None = None
    """Whether the issue is visible in the customer portal"""


class MessagesSearchData(BaseModel):
    """Search result data for messages entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the message"""
    timestamp: str | None = None
    """Timestamp the message was posted, in ISO 8601 format"""
    is_private: bool | None = None
    """Whether the message is an internal note (not visible to the customer)"""
    source: str | None = None
    """Channel the message was sent through (e.g. email, slack)"""
    thread_id: str | None = None
    """Identifier of the thread this message belongs to"""


class AccountsSearchData(BaseModel):
    """Search result data for accounts entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the account"""
    name: str | None = None
    """Name of the account (customer organization)"""
    domain: str | None = None
    """Primary domain associated with the account"""
    primary_domain: str | None = None
    """Canonical primary domain for the account"""
    type_: str | None = None
    """Classification of the account (e.g. customer, prospect)"""
    is_disabled: bool | None = None
    """Whether the account has been disabled"""
    created_at: str | None = None
    """Timestamp when the account was created, in ISO 8601 format"""
    latest_customer_activity_time: str | None = None
    """Timestamp of the most recent activity from this account, in ISO 8601 format"""


class ContactsSearchData(BaseModel):
    """Search result data for contacts entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the contact"""
    name: str | None = None
    """Full name of the contact"""
    email: str | None = None
    """Primary email address of the contact"""
    primary_phone_number: str | None = None
    """Primary phone number of the contact"""
    portal_role: str | None = None
    """Role the contact has in the customer portal"""


class TeamsSearchData(BaseModel):
    """Search result data for teams entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the team"""
    name: str | None = None
    """Name of the team"""


class TagsSearchData(BaseModel):
    """Search result data for tags entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the tag"""
    value: str | None = None
    """Display value of the tag"""
    object_type: str | None = None
    """Type of object this tag applies to (e.g. issue, account)"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the user"""
    name: str | None = None
    """Full name of the user"""
    email: str | None = None
    """Primary email address of the user"""
    role_id: str | None = None
    """Identifier of the user's role"""
    status: str | None = None
    """Current status of the user (e.g. active, disabled)"""


class CustomFieldsSearchData(BaseModel):
    """Search result data for custom_fields entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the custom field"""
    label: str | None = None
    """Display label of the custom field"""
    slug: str | None = None
    """URL-safe identifier for the custom field"""
    type_: str | None = None
    """Data type of the custom field (e.g. text, select)"""
    object_type: str | None = None
    """Type of object this custom field applies to (e.g. issue, account)"""
    is_read_only: bool | None = None
    """Whether the custom field is read-only"""
    created_at: str | None = None
    """Timestamp when the custom field was created, in ISO 8601 format"""


class TicketFormsSearchData(BaseModel):
    """Search result data for ticket_forms entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the ticket form"""
    name: str | None = None
    """Display name of the ticket form"""
    slug: str | None = None
    """URL-safe identifier for the ticket form"""
    is_public: bool | None = None
    """Whether the ticket form is publicly accessible"""


class UserRolesSearchData(BaseModel):
    """Search result data for user_roles entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the user role"""
    name: str | None = None
    """Display name of the user role"""
    slug: str | None = None
    """URL-safe identifier for the user role"""


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

IssuesSearchResult = AirbyteSearchResult[IssuesSearchData]
"""Search result type for issues entity."""

MessagesSearchResult = AirbyteSearchResult[MessagesSearchData]
"""Search result type for messages entity."""

AccountsSearchResult = AirbyteSearchResult[AccountsSearchData]
"""Search result type for accounts entity."""

ContactsSearchResult = AirbyteSearchResult[ContactsSearchData]
"""Search result type for contacts entity."""

TeamsSearchResult = AirbyteSearchResult[TeamsSearchData]
"""Search result type for teams entity."""

TagsSearchResult = AirbyteSearchResult[TagsSearchData]
"""Search result type for tags entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""

CustomFieldsSearchResult = AirbyteSearchResult[CustomFieldsSearchData]
"""Search result type for custom_fields entity."""

TicketFormsSearchResult = AirbyteSearchResult[TicketFormsSearchData]
"""Search result type for ticket_forms entity."""

UserRolesSearchResult = AirbyteSearchResult[UserRolesSearchData]
"""Search result type for user_roles entity."""



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

