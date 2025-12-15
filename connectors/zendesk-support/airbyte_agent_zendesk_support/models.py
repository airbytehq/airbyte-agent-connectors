"""
Pydantic models for zendesk-support connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any
from typing import Optional

# Authentication configuration - multiple options available

class ZendeskSupportOauth20AuthConfig(BaseModel):
    """OAuth 2.0 - Zendesk OAuth 2.0 authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """OAuth 2.0 access token"""
    refresh_token: Optional[str] = None
    """OAuth 2.0 refresh token (optional)"""

class ZendeskSupportApiTokenAuthConfig(BaseModel):
    """API Token - Authenticate using email and API token"""

    model_config = ConfigDict(extra="forbid")

    email: str
    """Your Zendesk account email address"""
    api_token: str
    """Your Zendesk API token from Admin Center"""

ZendeskSupportAuthConfig = ZendeskSupportOauth20AuthConfig | ZendeskSupportApiTokenAuthConfig

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Ticket(BaseModel):
    """Zendesk Support ticket object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    external_id: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    subject: Union[str | None, Any] = Field(default=None)
    raw_subject: Union[str | None, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    priority: Union[str | None, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    recipient: Union[str | None, Any] = Field(default=None)
    requester_id: Union[int, Any] = Field(default=None)
    submitter_id: Union[int, Any] = Field(default=None)
    assignee_id: Union[int | None, Any] = Field(default=None)
    organization_id: Union[int | None, Any] = Field(default=None)
    group_id: Union[int | None, Any] = Field(default=None)
    collaborator_ids: Union[list[int], Any] = Field(default=None)
    follower_ids: Union[list[int], Any] = Field(default=None)
    email_cc_ids: Union[list[int], Any] = Field(default=None)
    forum_topic_id: Union[int | None, Any] = Field(default=None)
    problem_id: Union[int | None, Any] = Field(default=None)
    has_incidents: Union[bool, Any] = Field(default=None)
    is_public: Union[bool, Any] = Field(default=None)
    due_at: Union[str | None, Any] = Field(default=None)
    tags: Union[list[str], Any] = Field(default=None)
    custom_fields: Union[list[dict[str, Any]], Any] = Field(default=None)
    satisfaction_rating: Union[dict[str, Any], Any] = Field(default=None)
    sharing_agreement_ids: Union[list[int], Any] = Field(default=None)
    custom_status_id: Union[int, Any] = Field(default=None)
    fields: Union[list[dict[str, Any]], Any] = Field(default=None)
    followup_ids: Union[list[int], Any] = Field(default=None)
    ticket_form_id: Union[int, Any] = Field(default=None)
    brand_id: Union[int, Any] = Field(default=None)
    allow_channelback: Union[bool, Any] = Field(default=None)
    allow_attachments: Union[bool, Any] = Field(default=None)
    from_messaging_channel: Union[bool, Any] = Field(default=None)
    generated_timestamp: Union[int, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    via: Union[dict[str, Any], Any] = Field(default=None)

class User(BaseModel):
    """Zendesk Support user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    alias: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    time_zone: Union[str, Any] = Field(default=None)
    locale: Union[str, Any] = Field(default=None)
    locale_id: Union[int, Any] = Field(default=None)
    organization_id: Union[int | None, Any] = Field(default=None)
    role: Union[str, Any] = Field(default=None)
    role_type: Union[int | None, Any] = Field(default=None)
    custom_role_id: Union[int | None, Any] = Field(default=None)
    external_id: Union[str | None, Any] = Field(default=None)
    tags: Union[list[str], Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    verified: Union[bool, Any] = Field(default=None)
    shared: Union[bool, Any] = Field(default=None)
    shared_agent: Union[bool, Any] = Field(default=None)
    shared_phone_number: Union[bool | None, Any] = Field(default=None)
    signature: Union[str | None, Any] = Field(default=None)
    details: Union[str | None, Any] = Field(default=None)
    notes: Union[str | None, Any] = Field(default=None)
    suspended: Union[bool, Any] = Field(default=None)
    restricted_agent: Union[bool, Any] = Field(default=None)
    only_private_comments: Union[bool, Any] = Field(default=None)
    moderator: Union[bool, Any] = Field(default=None)
    ticket_restriction: Union[str | None, Any] = Field(default=None)
    default_group_id: Union[int | None, Any] = Field(default=None)
    report_csv: Union[bool, Any] = Field(default=None)
    photo: Union[dict[str, Any] | None, Any] = Field(default=None)
    user_fields: Union[dict[str, Any], Any] = Field(default=None)
    last_login_at: Union[str | None, Any] = Field(default=None)
    two_factor_auth_enabled: Union[bool | None, Any] = Field(default=None)
    iana_time_zone: Union[str, Any] = Field(default=None)
    permanently_deleted: Union[bool, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class Organization(BaseModel):
    """Zendesk Support organization object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    details: Union[str | None, Any] = Field(default=None)
    notes: Union[str | None, Any] = Field(default=None)
    group_id: Union[int | None, Any] = Field(default=None)
    shared_tickets: Union[bool, Any] = Field(default=None)
    shared_comments: Union[bool, Any] = Field(default=None)
    external_id: Union[str | None, Any] = Field(default=None)
    domain_names: Union[list[str], Any] = Field(default=None)
    tags: Union[list[str], Any] = Field(default=None)
    organization_fields: Union[dict[str, Any], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class Group(BaseModel):
    """Zendesk Support group object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    default: Union[bool, Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)
    is_public: Union[bool, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class TicketComment(BaseModel):
    """Zendesk Support ticket comment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)
    body: Union[str, Any] = Field(default=None)
    html_body: Union[str, Any] = Field(default=None)
    plain_body: Union[str, Any] = Field(default=None)
    public: Union[bool, Any] = Field(default=None)
    author_id: Union[int, Any] = Field(default=None)
    attachments: Union[list[dict[str, Any]], Any] = Field(default=None)
    audit_id: Union[int, Any] = Field(default=None)
    via: Union[dict[str, Any], Any] = Field(default=None)
    metadata: Union[dict[str, Any], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)

class Attachment(BaseModel):
    """Zendesk Support attachment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    file_name: Union[str, Any] = Field(default=None)
    content_url: Union[str, Any] = Field(default=None)
    mapped_content_url: Union[str, Any] = Field(default=None)
    content_type: Union[str, Any] = Field(default=None)
    size: Union[int, Any] = Field(default=None)
    width: Union[int | None, Any] = Field(default=None)
    height: Union[int | None, Any] = Field(default=None)
    inline: Union[bool, Any] = Field(default=None)
    deleted: Union[bool, Any] = Field(default=None)
    malware_access_override: Union[bool, Any] = Field(default=None)
    malware_scan_result: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    thumbnails: Union[list[dict[str, Any]], Any] = Field(default=None)

class TicketAudit(BaseModel):
    """Zendesk Support ticket audit object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    ticket_id: Union[int, Any] = Field(default=None)
    author_id: Union[int, Any] = Field(default=None)
    metadata: Union[dict[str, Any], Any] = Field(default=None)
    via: Union[dict[str, Any], Any] = Field(default=None)
    events: Union[list[dict[str, Any]], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)

class TicketMetric(BaseModel):
    """Zendesk Support ticket metric object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    ticket_id: Union[int, Any] = Field(default=None)
    group_stations: Union[int, Any] = Field(default=None)
    assignee_stations: Union[int, Any] = Field(default=None)
    reopens: Union[int, Any] = Field(default=None)
    replies: Union[int, Any] = Field(default=None)
    assignee_updated_at: Union[str | None, Any] = Field(default=None)
    requester_updated_at: Union[str, Any] = Field(default=None)
    status_updated_at: Union[str, Any] = Field(default=None)
    initially_assigned_at: Union[str | None, Any] = Field(default=None)
    assigned_at: Union[str | None, Any] = Field(default=None)
    solved_at: Union[str | None, Any] = Field(default=None)
    latest_comment_added_at: Union[str, Any] = Field(default=None)
    reply_time_in_minutes: Union[dict[str, Any], Any] = Field(default=None)
    first_resolution_time_in_minutes: Union[dict[str, Any], Any] = Field(default=None)
    full_resolution_time_in_minutes: Union[dict[str, Any], Any] = Field(default=None)
    agent_wait_time_in_minutes: Union[dict[str, Any], Any] = Field(default=None)
    requester_wait_time_in_minutes: Union[dict[str, Any], Any] = Field(default=None)
    on_hold_time_in_minutes: Union[dict[str, Any], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class TicketField(BaseModel):
    """Zendesk Support ticket field object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    raw_title: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    raw_description: Union[str, Any] = Field(default=None)
    position: Union[int, Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    required: Union[bool, Any] = Field(default=None)
    collapsed_for_agents: Union[bool, Any] = Field(default=None)
    regexp_for_validation: Union[str | None, Any] = Field(default=None)
    title_in_portal: Union[str, Any] = Field(default=None)
    raw_title_in_portal: Union[str, Any] = Field(default=None)
    visible_in_portal: Union[bool, Any] = Field(default=None)
    editable_in_portal: Union[bool, Any] = Field(default=None)
    required_in_portal: Union[bool, Any] = Field(default=None)
    tag: Union[str | None, Any] = Field(default=None)
    custom_field_options: Union[list[dict[str, Any]], Any] = Field(default=None)
    system_field_options: Union[list[dict[str, Any]], Any] = Field(default=None)
    sub_type_id: Union[int, Any] = Field(default=None)
    removable: Union[bool, Any] = Field(default=None)
    agent_description: Union[str | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class Brand(BaseModel):
    """Zendesk Support brand object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    brand_url: Union[str, Any] = Field(default=None)
    subdomain: Union[str, Any] = Field(default=None)
    host_mapping: Union[str | None, Any] = Field(default=None)
    has_help_center: Union[bool, Any] = Field(default=None)
    help_center_state: Union[str, Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    default: Union[bool, Any] = Field(default=None)
    is_deleted: Union[bool, Any] = Field(default=None)
    logo: Union[dict[str, Any] | None, Any] = Field(default=None)
    ticket_form_ids: Union[list[int], Any] = Field(default=None)
    signature_template: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class View(BaseModel):
    """Zendesk Support view object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    position: Union[int, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    execution: Union[dict[str, Any], Any] = Field(default=None)
    conditions: Union[dict[str, Any], Any] = Field(default=None)
    restriction: Union[dict[str, Any] | None, Any] = Field(default=None)
    raw_title: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class Macro(BaseModel):
    """Zendesk Support macro object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    position: Union[int, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    actions: Union[list[dict[str, Any]], Any] = Field(default=None)
    restriction: Union[dict[str, Any] | None, Any] = Field(default=None)
    raw_title: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class Trigger(BaseModel):
    """Zendesk Support trigger object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    position: Union[int, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    conditions: Union[dict[str, Any], Any] = Field(default=None)
    actions: Union[list[dict[str, Any]], Any] = Field(default=None)
    raw_title: Union[str, Any] = Field(default=None)
    category_id: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class Automation(BaseModel):
    """Zendesk Support automation object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    position: Union[int, Any] = Field(default=None)
    conditions: Union[dict[str, Any], Any] = Field(default=None)
    actions: Union[list[dict[str, Any]], Any] = Field(default=None)
    raw_title: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class Tag(BaseModel):
    """Zendesk Support tag object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class SatisfactionRating(BaseModel):
    """Zendesk Support satisfaction rating object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    assignee_id: Union[int | None, Any] = Field(default=None)
    group_id: Union[int | None, Any] = Field(default=None)
    requester_id: Union[int, Any] = Field(default=None)
    ticket_id: Union[int, Any] = Field(default=None)
    score: Union[str, Any] = Field(default=None)
    comment: Union[str | None, Any] = Field(default=None)
    reason: Union[str | None, Any] = Field(default=None)
    reason_id: Union[int | None, Any] = Field(default=None)
    reason_code: Union[int | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class GroupMembership(BaseModel):
    """Zendesk Support group membership object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    user_id: Union[int, Any] = Field(default=None)
    group_id: Union[int, Any] = Field(default=None)
    default: Union[bool, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class OrganizationMembership(BaseModel):
    """Zendesk Support organization membership object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    user_id: Union[int, Any] = Field(default=None)
    organization_id: Union[int, Any] = Field(default=None)
    default: Union[bool, Any] = Field(default=None)
    organization_name: Union[str, Any] = Field(default=None)
    view_tickets: Union[bool, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class SLAPolicy(BaseModel):
    """Zendesk Support SLA policy object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)
    position: Union[int, Any] = Field(default=None)
    filter: Union[dict[str, Any], Any] = Field(default=None)
    policy_metrics: Union[list[dict[str, Any]], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class TicketForm(BaseModel):
    """Zendesk Support ticket form object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    display_name: Union[str, Any] = Field(default=None)
    raw_name: Union[str, Any] = Field(default=None)
    raw_display_name: Union[str, Any] = Field(default=None)
    position: Union[int, Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    end_user_visible: Union[bool, Any] = Field(default=None)
    default: Union[bool, Any] = Field(default=None)
    in_all_brands: Union[bool, Any] = Field(default=None)
    restricted_brand_ids: Union[list[int], Any] = Field(default=None)
    ticket_field_ids: Union[list[int], Any] = Field(default=None)
    agent_conditions: Union[list[dict[str, Any]], Any] = Field(default=None)
    end_user_conditions: Union[list[dict[str, Any]], Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

class Article(BaseModel):
    """Help Center article object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    html_url: Union[str, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    body: Union[str, Any] = Field(default=None)
    locale: Union[str, Any] = Field(default=None)
    author_id: Union[int, Any] = Field(default=None)
    section_id: Union[int, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    vote_sum: Union[int, Any] = Field(default=None)
    vote_count: Union[int, Any] = Field(default=None)
    label_names: Union[list[str], Any] = Field(default=None)
    draft: Union[bool, Any] = Field(default=None)
    promoted: Union[bool, Any] = Field(default=None)
    position: Union[int, Any] = Field(default=None)

class ArticleAttachment(BaseModel):
    """Article attachment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    article_id: Union[int, Any] = Field(default=None)
    file_name: Union[str, Any] = Field(default=None)
    content_type: Union[str, Any] = Field(default=None)
    content_url: Union[str, Any] = Field(default=None)
    size: Union[int, Any] = Field(default=None)
    inline: Union[bool, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class TicketsListResultMeta(BaseModel):
    """Metadata for tickets.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class OrganizationsListResultMeta(BaseModel):
    """Metadata for organizations.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class GroupsListResultMeta(BaseModel):
    """Metadata for groups.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TicketCommentsListResultMeta(BaseModel):
    """Metadata for ticket_comments.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TicketAuditsListResultMeta(BaseModel):
    """Metadata for ticket_audits.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TicketMetricsListResultMeta(BaseModel):
    """Metadata for ticket_metrics.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TicketFieldsListResultMeta(BaseModel):
    """Metadata for ticket_fields.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class BrandsListResultMeta(BaseModel):
    """Metadata for brands.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class ViewsListResultMeta(BaseModel):
    """Metadata for views.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class MacrosListResultMeta(BaseModel):
    """Metadata for macros.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TriggersListResultMeta(BaseModel):
    """Metadata for triggers.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class AutomationsListResultMeta(BaseModel):
    """Metadata for automations.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TagsListResultMeta(BaseModel):
    """Metadata for tags.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class SatisfactionRatingsListResultMeta(BaseModel):
    """Metadata for satisfaction_ratings.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class GroupMembershipsListResultMeta(BaseModel):
    """Metadata for group_memberships.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class OrganizationMembershipsListResultMeta(BaseModel):
    """Metadata for organization_memberships.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class SlaPoliciesListResultMeta(BaseModel):
    """Metadata for sla_policies.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TicketFormsListResultMeta(BaseModel):
    """Metadata for ticket_forms.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class ArticlesListResultMeta(BaseModel):
    """Metadata for articles.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class ArticleAttachmentsListResultMeta(BaseModel):
    """Metadata for article_attachments.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class ZendeskSupportExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class ZendeskSupportExecuteResultWithMeta(ZendeskSupportExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

TicketsListResult = ZendeskSupportExecuteResultWithMeta[list[Ticket], TicketsListResultMeta]
"""Result type for tickets.list operation with data and metadata."""

TicketsGetResult = ZendeskSupportExecuteResult[Ticket]
"""Result type for tickets.get operation."""

UsersListResult = ZendeskSupportExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

UsersGetResult = ZendeskSupportExecuteResult[User]
"""Result type for users.get operation."""

OrganizationsListResult = ZendeskSupportExecuteResultWithMeta[list[Organization], OrganizationsListResultMeta]
"""Result type for organizations.list operation with data and metadata."""

OrganizationsGetResult = ZendeskSupportExecuteResult[Organization]
"""Result type for organizations.get operation."""

GroupsListResult = ZendeskSupportExecuteResultWithMeta[list[Group], GroupsListResultMeta]
"""Result type for groups.list operation with data and metadata."""

GroupsGetResult = ZendeskSupportExecuteResult[Group]
"""Result type for groups.get operation."""

TicketCommentsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketComment], TicketCommentsListResultMeta]
"""Result type for ticket_comments.list operation with data and metadata."""

AttachmentsGetResult = ZendeskSupportExecuteResult[Attachment]
"""Result type for attachments.get operation."""

TicketAuditsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta]
"""Result type for ticket_audits.list operation with data and metadata."""

TicketAuditsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta]
"""Result type for ticket_audits.list operation with data and metadata."""

TicketMetricsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketMetric], TicketMetricsListResultMeta]
"""Result type for ticket_metrics.list operation with data and metadata."""

TicketFieldsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketField], TicketFieldsListResultMeta]
"""Result type for ticket_fields.list operation with data and metadata."""

TicketFieldsGetResult = ZendeskSupportExecuteResult[TicketField]
"""Result type for ticket_fields.get operation."""

BrandsListResult = ZendeskSupportExecuteResultWithMeta[list[Brand], BrandsListResultMeta]
"""Result type for brands.list operation with data and metadata."""

BrandsGetResult = ZendeskSupportExecuteResult[Brand]
"""Result type for brands.get operation."""

ViewsListResult = ZendeskSupportExecuteResultWithMeta[list[View], ViewsListResultMeta]
"""Result type for views.list operation with data and metadata."""

ViewsGetResult = ZendeskSupportExecuteResult[View]
"""Result type for views.get operation."""

MacrosListResult = ZendeskSupportExecuteResultWithMeta[list[Macro], MacrosListResultMeta]
"""Result type for macros.list operation with data and metadata."""

MacrosGetResult = ZendeskSupportExecuteResult[Macro]
"""Result type for macros.get operation."""

TriggersListResult = ZendeskSupportExecuteResultWithMeta[list[Trigger], TriggersListResultMeta]
"""Result type for triggers.list operation with data and metadata."""

TriggersGetResult = ZendeskSupportExecuteResult[Trigger]
"""Result type for triggers.get operation."""

AutomationsListResult = ZendeskSupportExecuteResultWithMeta[list[Automation], AutomationsListResultMeta]
"""Result type for automations.list operation with data and metadata."""

AutomationsGetResult = ZendeskSupportExecuteResult[Automation]
"""Result type for automations.get operation."""

TagsListResult = ZendeskSupportExecuteResultWithMeta[list[Tag], TagsListResultMeta]
"""Result type for tags.list operation with data and metadata."""

SatisfactionRatingsListResult = ZendeskSupportExecuteResultWithMeta[list[SatisfactionRating], SatisfactionRatingsListResultMeta]
"""Result type for satisfaction_ratings.list operation with data and metadata."""

SatisfactionRatingsGetResult = ZendeskSupportExecuteResult[SatisfactionRating]
"""Result type for satisfaction_ratings.get operation."""

GroupMembershipsListResult = ZendeskSupportExecuteResultWithMeta[list[GroupMembership], GroupMembershipsListResultMeta]
"""Result type for group_memberships.list operation with data and metadata."""

OrganizationMembershipsListResult = ZendeskSupportExecuteResultWithMeta[list[OrganizationMembership], OrganizationMembershipsListResultMeta]
"""Result type for organization_memberships.list operation with data and metadata."""

SlaPoliciesListResult = ZendeskSupportExecuteResultWithMeta[list[SLAPolicy], SlaPoliciesListResultMeta]
"""Result type for sla_policies.list operation with data and metadata."""

SlaPoliciesGetResult = ZendeskSupportExecuteResult[SLAPolicy]
"""Result type for sla_policies.get operation."""

TicketFormsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketForm], TicketFormsListResultMeta]
"""Result type for ticket_forms.list operation with data and metadata."""

TicketFormsGetResult = ZendeskSupportExecuteResult[TicketForm]
"""Result type for ticket_forms.get operation."""

ArticlesListResult = ZendeskSupportExecuteResultWithMeta[list[Article], ArticlesListResultMeta]
"""Result type for articles.list operation with data and metadata."""

ArticlesGetResult = ZendeskSupportExecuteResult[Article]
"""Result type for articles.get operation."""

ArticleAttachmentsListResult = ZendeskSupportExecuteResultWithMeta[list[ArticleAttachment], ArticleAttachmentsListResultMeta]
"""Result type for article_attachments.list operation with data and metadata."""

ArticleAttachmentsGetResult = ZendeskSupportExecuteResult[ArticleAttachment]
"""Result type for article_attachments.get operation."""

