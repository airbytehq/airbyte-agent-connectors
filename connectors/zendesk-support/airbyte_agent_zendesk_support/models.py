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
    """Metadata for tickets.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class OrganizationsListResultMeta(BaseModel):
    """Metadata for organizations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class GroupsListResultMeta(BaseModel):
    """Metadata for groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TicketCommentsListResultMeta(BaseModel):
    """Metadata for ticket_comments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TicketAuditsListResultMeta(BaseModel):
    """Metadata for ticket_audits.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TicketMetricsListResultMeta(BaseModel):
    """Metadata for ticket_metrics.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TicketFieldsListResultMeta(BaseModel):
    """Metadata for ticket_fields.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class BrandsListResultMeta(BaseModel):
    """Metadata for brands.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class ViewsListResultMeta(BaseModel):
    """Metadata for views.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class MacrosListResultMeta(BaseModel):
    """Metadata for macros.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TriggersListResultMeta(BaseModel):
    """Metadata for triggers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class AutomationsListResultMeta(BaseModel):
    """Metadata for automations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TagsListResultMeta(BaseModel):
    """Metadata for tags.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class SatisfactionRatingsListResultMeta(BaseModel):
    """Metadata for satisfaction_ratings.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class GroupMembershipsListResultMeta(BaseModel):
    """Metadata for group_memberships.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class OrganizationMembershipsListResultMeta(BaseModel):
    """Metadata for organization_memberships.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class SlaPoliciesListResultMeta(BaseModel):
    """Metadata for sla_policies.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class TicketFormsListResultMeta(BaseModel):
    """Metadata for ticket_forms.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class ArticlesListResultMeta(BaseModel):
    """Metadata for articles.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class ArticleAttachmentsListResultMeta(BaseModel):
    """Metadata for article_attachments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class ZendeskSupportCheckResult(BaseModel):
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

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class BrandsSearchData(BaseModel):
    """Search result data for brands entity."""
    model_config = ConfigDict(extra="allow")

    active: bool | None = None
    """Indicates whether the brand is set as active"""
    brand_url: str | None = None
    """The public URL of the brand"""
    created_at: str | None = None
    """Timestamp when the brand was created"""
    default: bool | None = None
    """Indicates whether the brand is the default brand for tickets generated from non-branded channels"""
    has_help_center: bool | None = None
    """Indicates whether the brand has a Help Center enabled"""
    help_center_state: str | None = None
    """The state of the Help Center, with allowed values of enabled, disabled, or restricted"""
    host_mapping: str | None = None
    """The host mapping configuration for the brand, visible only to administrators"""
    id: int | None = None
    """Unique identifier automatically assigned when the brand is created"""
    is_deleted: bool | None = None
    """Indicates whether the brand has been deleted"""
    logo: str | None = None
    """Brand logo image file represented as an Attachment object"""
    name: str | None = None
    """The name of the brand"""
    signature_template: str | None = None
    """The signature template used for the brand"""
    subdomain: str | None = None
    """The subdomain associated with the brand"""
    ticket_form_ids: list[Any] | None = None
    """Array of ticket form IDs that are available for use by this brand"""
    updated_at: str | None = None
    """Timestamp when the brand was last updated"""
    url: str | None = None
    """The API URL for accessing this brand resource"""


class GroupsSearchData(BaseModel):
    """Search result data for groups entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """Timestamp indicating when the group was created"""
    default: bool | None = None
    """Indicates if the group is the default one for the account"""
    deleted: bool | None = None
    """Indicates whether the group has been deleted"""
    description: str | None = None
    """The description of the group"""
    id: int | None = None
    """Unique identifier automatically assigned when creating groups"""
    is_public: bool | None = None
    """Indicates if the group is public (true) or private (false)"""
    name: str | None = None
    """The name of the group"""
    updated_at: str | None = None
    """Timestamp indicating when the group was last updated"""
    url: str | None = None
    """The API URL of the group"""


class OrganizationsSearchData(BaseModel):
    """Search result data for organizations entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """Timestamp when the organization was created"""
    deleted_at: str | None = None
    """Timestamp when the organization was deleted"""
    details: str | None = None
    """Details about the organization, such as the address"""
    domain_names: list[Any] | None = None
    """Array of domain names associated with this organization for automatic user assignment"""
    external_id: str | None = None
    """Unique external identifier to associate the organization to an external record (case-insensitive)"""
    group_id: int | None = None
    """ID of the group where new tickets from users in this organization are automatically assigned"""
    id: int | None = None
    """Unique identifier automatically assigned when the organization is created"""
    name: str | None = None
    """Unique name for the organization (mandatory field)"""
    notes: str | None = None
    """Notes about the organization"""
    organization_fields: dict[str, Any] | None = None
    """Key-value object for custom organization fields"""
    shared_comments: bool | None = None
    """Boolean indicating whether end users in this organization can comment on each other's tickets"""
    shared_tickets: bool | None = None
    """Boolean indicating whether end users in this organization can see each other's tickets"""
    tags: list[Any] | None = None
    """Array of tags associated with the organization"""
    updated_at: str | None = None
    """Timestamp of the last update to the organization"""
    url: str | None = None
    """The API URL of this organization"""


class SatisfactionRatingsSearchData(BaseModel):
    """Search result data for satisfaction_ratings entity."""
    model_config = ConfigDict(extra="allow")

    assignee_id: int | None = None
    """The identifier of the agent assigned to the ticket at the time the rating was submitted"""
    comment: str | None = None
    """Optional comment provided by the requester with the rating"""
    created_at: str | None = None
    """Timestamp indicating when the satisfaction rating was created"""
    group_id: int | None = None
    """The identifier of the group assigned to the ticket at the time the rating was submitted"""
    id: int | None = None
    """Unique identifier for the satisfaction rating, automatically assigned upon creation"""
    reason: str | None = None
    """Free-text reason for a bad rating provided by the requester in a follow-up question"""
    reason_id: int | None = None
    """Identifier for the predefined reason given for a negative rating"""
    requester_id: int | None = None
    """The identifier of the ticket requester who submitted the satisfaction rating"""
    score: str | None = None
    """The satisfaction rating value: 'offered', 'unoffered', 'good', or 'bad'"""
    ticket_id: int | None = None
    """The identifier of the ticket being rated"""
    updated_at: str | None = None
    """Timestamp indicating when the satisfaction rating was last updated"""
    url: str | None = None
    """The API URL of this satisfaction rating resource"""


class TagsSearchData(BaseModel):
    """Search result data for tags entity."""
    model_config = ConfigDict(extra="allow")

    count: int | None = None
    """The number of times this tag has been used across resources"""
    name: str | None = None
    """The tag name string used to label and categorize resources"""


class TicketAuditsSearchData(BaseModel):
    """Search result data for ticket_audits entity."""
    model_config = ConfigDict(extra="allow")

    attachments: list[Any] | None = None
    """Files or documents attached to the audit"""
    author_id: int | None = None
    """The unique identifier of the user who created the audit"""
    created_at: str | None = None
    """Timestamp indicating when the audit was created"""
    events: list[Any] | None = None
    """Array of events that occurred in this audit, such as field changes, comments, or tag updates"""
    id: int | None = None
    """Unique identifier for the audit record, automatically assigned when the audit is created"""
    metadata: dict[str, Any] | None = None
    """Custom and system data associated with the audit"""
    ticket_id: int | None = None
    """The unique identifier of the ticket associated with this audit"""
    via: dict[str, Any] | None = None
    """Describes how the audit was created, providing context about the creation source"""


class TicketCommentsSearchData(BaseModel):
    """Search result data for ticket_comments entity."""
    model_config = ConfigDict(extra="allow")

    attachments: list[Any] | None = None
    """List of files or media attached to the comment"""
    audit_id: int | None = None
    """Identifier of the audit record associated with this comment event"""
    author_id: int | None = None
    """Identifier of the user who created the comment"""
    body: str | None = None
    """Content of the comment in its original format"""
    created_at: str | None = None
    """Timestamp when the comment was created"""
    event_type: str | None = None
    """Specific classification of the event within the ticket event stream"""
    html_body: str | None = None
    """HTML-formatted content of the comment"""
    id: int | None = None
    """Unique identifier for the comment event"""
    metadata: dict[str, Any] | None = None
    """Additional structured information about the comment not covered by standard fields"""
    plain_body: str | None = None
    """Plain text content of the comment without formatting"""
    public: bool | None = None
    """Boolean indicating whether the comment is visible to end users or is an internal note"""
    ticket_id: int | None = None
    """Identifier of the ticket to which this comment belongs"""
    timestamp: int | None = None
    """Timestamp of when the event occurred in the incremental export stream"""
    type: str | None = None
    """Type of event, typically indicating this is a comment event"""
    uploads: list[Any] | None = None
    """Array of upload tokens or identifiers for files being attached to the comment"""
    via: dict[str, Any] | None = None
    """Channel or method through which the comment was submitted"""
    via_reference_id: int | None = None
    """Reference identifier for the channel through which the comment was created"""


class TicketFieldsSearchData(BaseModel):
    """Search result data for ticket_fields entity."""
    model_config = ConfigDict(extra="allow")

    active: bool | None = None
    """Whether this field is currently available for use"""
    agent_description: str | None = None
    """A description of the ticket field that only agents can see"""
    collapsed_for_agents: bool | None = None
    """If true, the field is shown to agents by default; if false, it is hidden alongside infrequently used fields"""
    created_at: str | None = None
    """Timestamp when the custom ticket field was created"""
    custom_field_options: list[Any] | None = None
    """Array of option objects for custom ticket fields of type multiselect or tagger"""
    custom_statuses: list[Any] | None = None
    """List of customized ticket statuses, only present for system ticket fields of type custom_status"""
    description: str | None = None
    """Text describing the purpose of the ticket field to users"""
    editable_in_portal: bool | None = None
    """Whether this field is editable by end users in Help Center"""
    id: int | None = None
    """Unique identifier for the ticket field, automatically assigned when created"""
    key: str | None = None
    """Internal identifier or reference key for the field"""
    position: int | None = None
    """The relative position of the ticket field on a ticket, controlling display order"""
    raw_description: str | None = None
    """The dynamic content placeholder if present, or the description value if not"""
    raw_title: str | None = None
    """The dynamic content placeholder if present, or the title value if not"""
    raw_title_in_portal: str | None = None
    """The dynamic content placeholder if present, or the title_in_portal value if not"""
    regexp_for_validation: str | None = None
    """For regexp fields only, the validation pattern for a field value to be deemed valid"""
    removable: bool | None = None
    """If false, this field is a system field that must be present on all tickets"""
    required: bool | None = None
    """If true, agents must enter a value in the field to change the ticket status to solved"""
    required_in_portal: bool | None = None
    """If true, end users must enter a value in the field to create a request"""
    sub_type_id: int | None = None
    """For system ticket fields of type priority and status, controlling available options"""
    system_field_options: list[Any] | None = None
    """Array of options for system ticket fields of type tickettype, priority, or status"""
    tag: str | None = None
    """For checkbox fields only, a tag added to tickets when the checkbox field is selected"""
    title: str | None = None
    """The title of the ticket field displayed to agents"""
    title_in_portal: str | None = None
    """The title of the ticket field displayed to end users in Help Center"""
    type: str | None = None
    """Field type such as text, textarea, checkbox, date, integer, decimal, regexp, multiselect, or tagger"""
    updated_at: str | None = None
    """Timestamp when the custom ticket field was last updated"""
    url: str | None = None
    """The API URL for this ticket field resource"""
    visible_in_portal: bool | None = None
    """Whether this field is visible to end users in Help Center"""


class TicketFormsSearchData(BaseModel):
    """Search result data for ticket_forms entity."""
    model_config = ConfigDict(extra="allow")

    active: bool | None = None
    """Indicates if the form is set as active"""
    agent_conditions: list[Any] | None = None
    """Array of condition sets for agent workspaces"""
    created_at: str | None = None
    """Timestamp when the ticket form was created"""
    default: bool | None = None
    """Indicates if the form is the default form for this account"""
    display_name: str | None = None
    """The name of the form that is displayed to an end user"""
    end_user_conditions: list[Any] | None = None
    """Array of condition sets for end user products"""
    end_user_visible: bool | None = None
    """Indicates if the form is visible to the end user"""
    id: int | None = None
    """Unique identifier for the ticket form, automatically assigned when creating the form"""
    in_all_brands: bool | None = None
    """Indicates if the form is available for use in all brands on this account"""
    name: str | None = None
    """The name of the ticket form"""
    position: int | None = None
    """The position of this form among other forms in the account, such as in a dropdown"""
    raw_display_name: str | None = None
    """The dynamic content placeholder if present, or the display_name value if not"""
    raw_name: str | None = None
    """The dynamic content placeholder if present, or the name value if not"""
    restricted_brand_ids: list[Any] | None = None
    """IDs of all brands that this ticket form is restricted to"""
    ticket_field_ids: list[Any] | None = None
    """IDs of all ticket fields included in this ticket form"""
    updated_at: str | None = None
    """Timestamp of the last update to the ticket form"""
    url: str | None = None
    """URL of the ticket form"""


class TicketMetricsSearchData(BaseModel):
    """Search result data for ticket_metrics entity."""
    model_config = ConfigDict(extra="allow")

    agent_wait_time_in_minutes: dict[str, Any] | None = None
    """Number of minutes the agent spent waiting during calendar and business hours"""
    assigned_at: str | None = None
    """Timestamp when the ticket was assigned"""
    assignee_stations: int | None = None
    """Number of assignees the ticket had"""
    assignee_updated_at: str | None = None
    """Timestamp when the assignee last updated the ticket"""
    created_at: str | None = None
    """Timestamp when the metric record was created"""
    custom_status_updated_at: str | None = None
    """Timestamp when the ticket's custom status was last updated"""
    first_resolution_time_in_minutes: dict[str, Any] | None = None
    """Number of minutes to the first resolution time during calendar and business hours"""
    full_resolution_time_in_minutes: dict[str, Any] | None = None
    """Number of minutes to the full resolution during calendar and business hours"""
    generated_timestamp: int | None = None
    """Timestamp of when record was last updated"""
    group_stations: int | None = None
    """Number of groups the ticket passed through"""
    id: int | None = None
    """Unique identifier for the ticket metric record"""
    initially_assigned_at: str | None = None
    """Timestamp when the ticket was initially assigned"""
    instance_id: int | None = None
    """ID of the Zendesk instance associated with the ticket"""
    latest_comment_added_at: str | None = None
    """Timestamp when the latest comment was added"""
    metric: str | None = None
    """Ticket metrics data"""
    on_hold_time_in_minutes: dict[str, Any] | None = None
    """Number of minutes on hold"""
    reopens: int | None = None
    """Total number of times the ticket was reopened"""
    replies: int | None = None
    """The number of public replies added to a ticket by an agent"""
    reply_time_in_minutes: dict[str, Any] | None = None
    """Number of minutes to the first reply during calendar and business hours"""
    reply_time_in_seconds: dict[str, Any] | None = None
    """Number of seconds to the first reply during calendar hours, only available for Messaging tickets"""
    requester_updated_at: str | None = None
    """Timestamp when the requester last updated the ticket"""
    requester_wait_time_in_minutes: dict[str, Any] | None = None
    """Number of minutes the requester spent waiting during calendar and business hours"""
    solved_at: str | None = None
    """Timestamp when the ticket was solved"""
    status: dict[str, Any] | None = None
    """The current status of the ticket (open, pending, solved, etc.)."""
    status_updated_at: str | None = None
    """Timestamp when the status of the ticket was last updated"""
    ticket_id: int | None = None
    """Identifier of the associated ticket"""
    time: str | None = None
    """Time related to the ticket"""
    type: str | None = None
    """Type of ticket"""
    updated_at: str | None = None
    """Timestamp when the metric record was last updated"""
    url: str | None = None
    """The API url of the ticket metric"""


class TicketsSearchData(BaseModel):
    """Search result data for tickets entity."""
    model_config = ConfigDict(extra="allow")

    allow_attachments: bool | None = None
    """Boolean indicating whether attachments are allowed on the ticket"""
    allow_channelback: bool | None = None
    """Boolean indicating whether agents can reply to the ticket through the original channel"""
    assignee_id: int | None = None
    """Unique identifier of the agent currently assigned to the ticket"""
    brand_id: int | None = None
    """Unique identifier of the brand associated with the ticket in multi-brand accounts"""
    collaborator_ids: list[Any] | None = None
    """Array of user identifiers who are collaborating on the ticket"""
    created_at: str | None = None
    """Timestamp indicating when the ticket was created"""
    custom_fields: list[Any] | None = None
    """Array of custom field values specific to the account's ticket configuration"""
    custom_status_id: int | None = None
    """Unique identifier of the custom status applied to the ticket"""
    deleted_ticket_form_id: int | None = None
    """The ID of the ticket form that was previously associated with this ticket but has since been deleted"""
    description: str | None = None
    """Initial description or content of the ticket when it was created"""
    due_at: str | None = None
    """Timestamp indicating when the ticket is due for completion or resolution"""
    email_cc_ids: list[Any] | None = None
    """Array of user identifiers who are CC'd on ticket email notifications"""
    external_id: str | None = None
    """External identifier for the ticket, used for integrations with other systems"""
    fields: list[Any] | None = None
    """Array of ticket field values including both system and custom fields"""
    follower_ids: list[Any] | None = None
    """Array of user identifiers who are following the ticket for updates"""
    followup_ids: list[Any] | None = None
    """Array of identifiers for follow-up tickets related to this ticket"""
    forum_topic_id: int | None = None
    """Unique identifier linking the ticket to a forum topic if applicable"""
    from_messaging_channel: bool | None = None
    """Boolean indicating whether the ticket originated from a messaging channel"""
    generated_timestamp: int | None = None
    """Timestamp updated for all ticket updates including system changes, used for incremental export"""
    group_id: int | None = None
    """Unique identifier of the agent group assigned to handle the ticket"""
    has_incidents: bool | None = None
    """Boolean indicating whether this problem ticket has related incident tickets"""
    id: int | None = None
    """Unique identifier for the ticket"""
    is_public: bool | None = None
    """Boolean indicating whether the ticket is publicly visible"""
    organization_id: int | None = None
    """Unique identifier of the organization associated with the ticket"""
    priority: str | None = None
    """Priority level assigned to the ticket (e.g., urgent, high, normal, low)"""
    problem_id: int | None = None
    """Unique identifier of the problem ticket if this is an incident ticket"""
    raw_subject: str | None = None
    """Original unprocessed subject line before any system modifications"""
    recipient: str | None = None
    """Email address or identifier of the ticket recipient"""
    requester_id: int | None = None
    """Unique identifier of the user who requested or created the ticket"""
    satisfaction_rating: Any = None
    """Object containing customer satisfaction rating data for the ticket"""
    sharing_agreement_ids: list[Any] | None = None
    """Array of sharing agreement identifiers if the ticket is shared across Zendesk instances"""
    status: str | None = None
    """Current status of the ticket (e.g., new, open, pending, solved, closed)"""
    subject: str | None = None
    """Subject line of the ticket describing the issue or request"""
    submitter_id: int | None = None
    """Unique identifier of the user who submitted the ticket on behalf of the requester"""
    tags: list[Any] | None = None
    """Array of tags applied to the ticket for categorization and filtering"""
    ticket_form_id: int | None = None
    """Unique identifier of the ticket form used when creating the ticket"""
    type: str | None = None
    """Type of ticket (e.g., problem, incident, question, task)"""
    updated_at: str | None = None
    """Timestamp indicating when the ticket was last updated with a ticket event"""
    url: str | None = None
    """API URL to access the full ticket resource"""
    via: dict[str, Any] | None = None
    """Object describing the channel and method through which the ticket was created"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    active: bool | None = None
    """Indicates if the user account is currently active"""
    alias: str | None = None
    """Alternative name or nickname for the user"""
    chat_only: bool | None = None
    """Indicates if the user can only interact via chat"""
    created_at: str | None = None
    """Timestamp indicating when the user was created"""
    custom_role_id: int | None = None
    """Identifier for a custom role assigned to the user"""
    default_group_id: int | None = None
    """Identifier of the default group assigned to the user"""
    details: str | None = None
    """Additional descriptive information about the user"""
    email: str | None = None
    """Email address of the user"""
    external_id: str | None = None
    """External system identifier for the user, used for integrations"""
    iana_time_zone: str | None = None
    """IANA standard time zone identifier for the user"""
    id: int | None = None
    """Unique identifier for the user"""
    last_login_at: str | None = None
    """Timestamp of the user's most recent login"""
    locale: str | None = None
    """Locale setting determining language and regional format preferences"""
    locale_id: int | None = None
    """Identifier for the user's locale preference"""
    moderator: bool | None = None
    """Indicates if the user has moderator privileges"""
    name: str | None = None
    """Display name of the user"""
    notes: str | None = None
    """Internal notes about the user, visible only to agents"""
    only_private_comments: bool | None = None
    """Indicates if the user can only make private comments on tickets"""
    organization_id: int | None = None
    """Identifier of the organization the user belongs to"""
    permanently_deleted: bool | None = None
    """Indicates if the user has been permanently deleted from the system"""
    phone: str | None = None
    """Phone number of the user"""
    photo: dict[str, Any] | None = None
    """Profile photo or avatar of the user"""
    report_csv: bool | None = None
    """Indicates if the user receives reports in CSV format"""
    restricted_agent: bool | None = None
    """Indicates if the agent has restricted access permissions"""
    role: str | None = None
    """Role assigned to the user defining their permissions level"""
    role_type: int | None = None
    """Type classification of the user's role"""
    shared: bool | None = None
    """Indicates if the user is shared across multiple accounts"""
    shared_agent: bool | None = None
    """Indicates if the user is a shared agent across multiple brands or accounts"""
    shared_phone_number: bool | None = None
    """Indicates if the phone number is shared with other users"""
    signature: str | None = None
    """Email signature text for the user"""
    suspended: bool | None = None
    """Indicates if the user account is suspended"""
    tags: list[Any] | None = None
    """Labels or tags associated with the user for categorization"""
    ticket_restriction: str | None = None
    """Defines which tickets the user can access based on restrictions"""
    time_zone: str | None = None
    """Time zone setting for the user"""
    two_factor_auth_enabled: bool | None = None
    """Indicates if two-factor authentication is enabled for the user"""
    updated_at: str | None = None
    """Timestamp indicating when the user was last updated"""
    url: str | None = None
    """API endpoint URL for accessing the user's detailed information"""
    user_fields: dict[str, Any] | None = None
    """Custom field values specific to the user, stored as key-value pairs"""
    verified: bool | None = None
    """Indicates if the user's identity has been verified"""


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

BrandsSearchResult = AirbyteSearchResult[BrandsSearchData]
"""Search result type for brands entity."""

GroupsSearchResult = AirbyteSearchResult[GroupsSearchData]
"""Search result type for groups entity."""

OrganizationsSearchResult = AirbyteSearchResult[OrganizationsSearchData]
"""Search result type for organizations entity."""

SatisfactionRatingsSearchResult = AirbyteSearchResult[SatisfactionRatingsSearchData]
"""Search result type for satisfaction_ratings entity."""

TagsSearchResult = AirbyteSearchResult[TagsSearchData]
"""Search result type for tags entity."""

TicketAuditsSearchResult = AirbyteSearchResult[TicketAuditsSearchData]
"""Search result type for ticket_audits entity."""

TicketCommentsSearchResult = AirbyteSearchResult[TicketCommentsSearchData]
"""Search result type for ticket_comments entity."""

TicketFieldsSearchResult = AirbyteSearchResult[TicketFieldsSearchData]
"""Search result type for ticket_fields entity."""

TicketFormsSearchResult = AirbyteSearchResult[TicketFormsSearchData]
"""Search result type for ticket_forms entity."""

TicketMetricsSearchResult = AirbyteSearchResult[TicketMetricsSearchData]
"""Search result type for ticket_metrics entity."""

TicketsSearchResult = AirbyteSearchResult[TicketsSearchData]
"""Search result type for tickets entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

TicketsListResult = ZendeskSupportExecuteResultWithMeta[list[Ticket], TicketsListResultMeta]
"""Result type for tickets.list operation with data and metadata."""

UsersListResult = ZendeskSupportExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

OrganizationsListResult = ZendeskSupportExecuteResultWithMeta[list[Organization], OrganizationsListResultMeta]
"""Result type for organizations.list operation with data and metadata."""

GroupsListResult = ZendeskSupportExecuteResultWithMeta[list[Group], GroupsListResultMeta]
"""Result type for groups.list operation with data and metadata."""

TicketCommentsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketComment], TicketCommentsListResultMeta]
"""Result type for ticket_comments.list operation with data and metadata."""

TicketAuditsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta]
"""Result type for ticket_audits.list operation with data and metadata."""

TicketAuditsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketAudit], TicketAuditsListResultMeta]
"""Result type for ticket_audits.list operation with data and metadata."""

TicketMetricsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketMetric], TicketMetricsListResultMeta]
"""Result type for ticket_metrics.list operation with data and metadata."""

TicketFieldsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketField], TicketFieldsListResultMeta]
"""Result type for ticket_fields.list operation with data and metadata."""

BrandsListResult = ZendeskSupportExecuteResultWithMeta[list[Brand], BrandsListResultMeta]
"""Result type for brands.list operation with data and metadata."""

ViewsListResult = ZendeskSupportExecuteResultWithMeta[list[View], ViewsListResultMeta]
"""Result type for views.list operation with data and metadata."""

MacrosListResult = ZendeskSupportExecuteResultWithMeta[list[Macro], MacrosListResultMeta]
"""Result type for macros.list operation with data and metadata."""

TriggersListResult = ZendeskSupportExecuteResultWithMeta[list[Trigger], TriggersListResultMeta]
"""Result type for triggers.list operation with data and metadata."""

AutomationsListResult = ZendeskSupportExecuteResultWithMeta[list[Automation], AutomationsListResultMeta]
"""Result type for automations.list operation with data and metadata."""

TagsListResult = ZendeskSupportExecuteResultWithMeta[list[Tag], TagsListResultMeta]
"""Result type for tags.list operation with data and metadata."""

SatisfactionRatingsListResult = ZendeskSupportExecuteResultWithMeta[list[SatisfactionRating], SatisfactionRatingsListResultMeta]
"""Result type for satisfaction_ratings.list operation with data and metadata."""

GroupMembershipsListResult = ZendeskSupportExecuteResultWithMeta[list[GroupMembership], GroupMembershipsListResultMeta]
"""Result type for group_memberships.list operation with data and metadata."""

OrganizationMembershipsListResult = ZendeskSupportExecuteResultWithMeta[list[OrganizationMembership], OrganizationMembershipsListResultMeta]
"""Result type for organization_memberships.list operation with data and metadata."""

SlaPoliciesListResult = ZendeskSupportExecuteResultWithMeta[list[SLAPolicy], SlaPoliciesListResultMeta]
"""Result type for sla_policies.list operation with data and metadata."""

TicketFormsListResult = ZendeskSupportExecuteResultWithMeta[list[TicketForm], TicketFormsListResultMeta]
"""Result type for ticket_forms.list operation with data and metadata."""

ArticlesListResult = ZendeskSupportExecuteResultWithMeta[list[Article], ArticlesListResultMeta]
"""Result type for articles.list operation with data and metadata."""

ArticleAttachmentsListResult = ZendeskSupportExecuteResultWithMeta[list[ArticleAttachment], ArticleAttachmentsListResultMeta]
"""Result type for article_attachments.list operation with data and metadata."""

