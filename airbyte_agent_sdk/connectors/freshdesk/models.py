"""
Pydantic models for freshdesk connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class FreshdeskAuthConfig(BaseModel):
    """API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Freshdesk API key (found in Profile Settings)"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Ticket(BaseModel):
    """A Freshdesk support ticket"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    subject: str | None = Field(default=None)
    description: str | None = Field(default=None)
    description_text: str | None = Field(default=None)
    status: int | None = Field(default=None)
    priority: int | None = Field(default=None)
    source: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    requester_id: int | None = Field(default=None)
    responder_id: int | None = Field(default=None)
    company_id: int | None = Field(default=None)
    group_id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    email_config_id: int | None = Field(default=None)
    cc_emails: list[str] | None = Field(default=None)
    fwd_emails: list[str] | None = Field(default=None)
    reply_cc_emails: list[str] | None = Field(default=None)
    to_emails: list[str] | None = Field(default=None)
    spam: bool | None = Field(default=None)
    deleted: bool | None = Field(default=None)
    fr_escalated: bool | None = Field(default=None)
    is_escalated: bool | None = Field(default=None)
    fr_due_by: str | None = Field(default=None)
    due_by: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    custom_fields: dict[str, Any] | None = Field(default=None)
    attachments: list[dict[str, Any]] | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    association_type: int | None = Field(default=None)
    associated_tickets_count: int | None = Field(default=None)
    ticket_cc_emails: list[str] | None = Field(default=None)
    ticket_bcc_emails: list[str] | None = Field(default=None)
    support_email: str | None = Field(default=None)
    source_additional_info: dict[str, Any] | None = Field(default=None)
    structured_description: dict[str, Any] | None = Field(default=None)
    form_id: int | None = Field(default=None)
    nr_due_by: str | None = Field(default=None)
    nr_escalated: bool | None = Field(default=None)

class Contact(BaseModel):
    """A Freshdesk contact (customer)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    mobile: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    address: str | None = Field(default=None)
    avatar: dict[str, Any] | None = Field(default=None)
    company_id: int | None = Field(default=None)
    view_all_tickets: bool | None = Field(default=None)
    custom_fields: dict[str, Any] | None = Field(default=None)
    deleted: bool | None = Field(default=None)
    description: str | None = Field(default=None)
    job_title: str | None = Field(default=None)
    language: str | None = Field(default=None)
    twitter_id: str | None = Field(default=None)
    unique_external_id: str | None = Field(default=None)
    other_emails: list[str] | None = Field(default=None)
    other_companies: list[dict[str, Any]] | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    time_zone: str | None = Field(default=None)
    facebook_id: str | None = Field(default=None)
    csat_rating: int | None = Field(default=None)
    preferred_source: str | None = Field(default=None)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    visitor_id: str | None = Field(default=None)
    org_contact_id: int | None = Field(default=None)
    org_contact_id_str: str | None = Field(default=None)
    other_phone_numbers: list[str] | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class AgentContact(BaseModel):
    """Contact details of the agent"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active: bool | None | None = Field(default=None, description="Whether the contact is active")
    """Whether the contact is active"""
    email: str | None | None = Field(default=None, description="Email of the agent")
    """Email of the agent"""
    job_title: str | None | None = Field(default=None, description="Job title")
    """Job title"""
    language: str | None | None = Field(default=None, description="Language")
    """Language"""
    last_login_at: str | None | None = Field(default=None, description="Last login timestamp")
    """Last login timestamp"""
    mobile: str | None | None = Field(default=None, description="Mobile number")
    """Mobile number"""
    name: str | None | None = Field(default=None, description="Name of the agent")
    """Name of the agent"""
    phone: str | None | None = Field(default=None, description="Phone number")
    """Phone number"""
    time_zone: str | None | None = Field(default=None, description="Time zone")
    """Time zone"""
    created_at: str | None | None = Field(default=None, description="Contact creation timestamp")
    """Contact creation timestamp"""
    updated_at: str | None | None = Field(default=None, description="Contact update timestamp")
    """Contact update timestamp"""

class Agent(BaseModel):
    """A Freshdesk agent"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    available: bool | None = Field(default=None)
    available_since: str | None = Field(default=None)
    occasional: bool | None = Field(default=None)
    signature: str | None = Field(default=None)
    ticket_scope: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    skill_ids: list[int] | None = Field(default=None)
    group_ids: list[int] | None = Field(default=None)
    role_ids: list[int] | None = Field(default=None)
    focus_mode: bool | None = Field(default=None)
    contact: AgentContact | None = Field(default=None)
    last_active_at: str | None = Field(default=None)
    deactivated: bool | None = Field(default=None)
    agent_operational_status: str | None = Field(default=None)
    org_agent_id: str | None = Field(default=None)
    org_group_ids: list[str] | None = Field(default=None)
    contribution_group_ids: list[int] | None = Field(default=None)
    org_contribution_group_ids: list[str] | None = Field(default=None)
    scope: Any | None = Field(default=None)
    availability: Any | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class Group(BaseModel):
    """A Freshdesk group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    agent_ids: list[int] | None = Field(default=None)
    auto_ticket_assign: int | None = Field(default=None)
    business_hour_id: int | None = Field(default=None)
    escalate_to: int | None = Field(default=None)
    unassigned_for: str | None = Field(default=None)
    group_type: str | None = Field(default=None)
    allow_agents_to_change_availability: bool | None = Field(default=None)
    agent_availability_status: bool | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class Company(BaseModel):
    """A Freshdesk company"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    domains: list[str] | None = Field(default=None)
    note: str | None = Field(default=None)
    health_score: str | None = Field(default=None)
    account_tier: str | None = Field(default=None)
    renewal_date: str | None = Field(default=None)
    industry: str | None = Field(default=None)
    custom_fields: dict[str, Any] | None = Field(default=None)
    org_company_id: Any | None = Field(default=None)
    org_company_id_str: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class Role(BaseModel):
    """A Freshdesk role"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    default: bool | None = Field(default=None)
    agent_type: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class SatisfactionRating(BaseModel):
    """A Freshdesk satisfaction rating"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    survey_id: int | None = Field(default=None)
    user_id: int | None = Field(default=None)
    agent_id: int | None = Field(default=None)
    group_id: int | None = Field(default=None)
    ticket_id: int | None = Field(default=None)
    feedback: str | None = Field(default=None)
    ratings: dict[str, Any] | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class SurveyQuestionsItem(BaseModel):
    """Nested schema for Survey.questions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None, description="Question ID")
    """Question ID"""
    label: str | None | None = Field(default=None, description="Question label")
    """Question label"""
    accepted_ratings: list[int] | None | None = Field(default=None, description="Accepted rating values")
    """Accepted rating values"""

class Survey(BaseModel):
    """A Freshdesk survey"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    title: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    questions: list[SurveyQuestionsItem] | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class TimeEntry(BaseModel):
    """A Freshdesk time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    agent_id: int | None = Field(default=None)
    ticket_id: int | None = Field(default=None)
    company_id: int | None = Field(default=None)
    billable: bool | None = Field(default=None)
    note: str | None = Field(default=None)
    time_spent: str | None = Field(default=None)
    timer_running: bool | None = Field(default=None)
    executed_at: str | None = Field(default=None)
    start_time: str | None = Field(default=None)
    time_spent_in_seconds: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class TicketField(BaseModel):
    """A Freshdesk ticket field definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    label: str | None = Field(default=None)
    label_for_customers: str | None = Field(default=None)
    description: str | None = Field(default=None)
    position: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    default: bool | None = Field(default=None)
    required_for_closure: bool | None = Field(default=None)
    required_for_agents: bool | None = Field(default=None)
    required_for_customers: bool | None = Field(default=None)
    customers_can_edit: bool | None = Field(default=None)
    displayed_to_customers: bool | None = Field(default=None)
    customers_can_filter: bool | None = Field(default=None)
    portal_cc: bool | None = Field(default=None)
    portal_cc_to: str | None = Field(default=None)
    choices: Any | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class TicketsListResultMeta(BaseModel):
    """Metadata for tickets.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class ContactsListResultMeta(BaseModel):
    """Metadata for contacts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class AgentsListResultMeta(BaseModel):
    """Metadata for agents.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class GroupsListResultMeta(BaseModel):
    """Metadata for groups.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class CompaniesListResultMeta(BaseModel):
    """Metadata for companies.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class RolesListResultMeta(BaseModel):
    """Metadata for roles.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class SatisfactionRatingsListResultMeta(BaseModel):
    """Metadata for satisfaction_ratings.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class SurveysListResultMeta(BaseModel):
    """Metadata for surveys.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class TimeEntriesListResultMeta(BaseModel):
    """Metadata for time_entries.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class TicketFieldsListResultMeta(BaseModel):
    """Metadata for ticket_fields.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class FreshdeskCheckResult(BaseModel):
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


class FreshdeskExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class FreshdeskExecuteResultWithMeta(FreshdeskExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class TicketsSearchData(BaseModel):
    """Search result data for tickets entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique ticket ID"""
    subject: str | None = None
    """Subject of the ticket"""
    description: str | None = None
    """HTML content of the ticket"""
    description_text: str | None = None
    """Plain text content of the ticket"""
    status: int | None = None
    """Status: 2=Open, 3=Pending, 4=Resolved, 5=Closed"""
    priority: int | None = None
    """Priority: 1=Low, 2=Medium, 3=High, 4=Urgent"""
    source: int | None = None
    """Source: 1=Email, 2=Portal, 3=Phone, 7=Chat, 9=Feedback Widget, 10=Outbound Email"""
    type_: str | None = None
    """Ticket type"""
    requester_id: int | None = None
    """ID of the requester"""
    requester: dict[str, Any] | None = None
    """Requester details including name, email, and contact info"""
    responder_id: int | None = None
    """ID of the agent to whom the ticket is assigned"""
    group_id: int | None = None
    """ID of the group to which the ticket is assigned"""
    company_id: int | None = None
    """Company ID of the requester"""
    product_id: int | None = None
    """ID of the product associated with the ticket"""
    email_config_id: int | None = None
    """ID of the email config used for the ticket"""
    cc_emails: list[Any] | None = None
    """CC email addresses"""
    ticket_cc_emails: list[Any] | None = None
    """Ticket CC email addresses"""
    to_emails: list[Any] | None = None
    """To email addresses"""
    fwd_emails: list[Any] | None = None
    """Forwarded email addresses"""
    reply_cc_emails: list[Any] | None = None
    """Reply CC email addresses"""
    tags: list[Any] | None = None
    """Tags associated with the ticket"""
    custom_fields: dict[str, Any] | None = None
    """Custom fields associated with the ticket"""
    due_by: str | None = None
    """Resolution due by timestamp"""
    fr_due_by: str | None = None
    """First response due by timestamp"""
    fr_escalated: bool | None = None
    """Whether the first response time was breached"""
    is_escalated: bool | None = None
    """Whether the ticket is escalated"""
    nr_due_by: str | None = None
    """Next response due by timestamp"""
    nr_escalated: bool | None = None
    """Whether the next response time was breached"""
    spam: bool | None = None
    """Whether the ticket is marked as spam"""
    association_type: int | None = None
    """Association type for parent/child tickets"""
    associated_tickets_count: int | None = None
    """Number of associated tickets"""
    stats: dict[str, Any] | None = None
    """Ticket statistics including response and resolution times"""
    created_at: str | None = None
    """Ticket creation timestamp"""
    updated_at: str | None = None
    """Ticket last update timestamp"""


class AgentsSearchData(BaseModel):
    """Search result data for agents entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique agent ID"""
    available: bool | None = None
    """Whether the agent is available"""
    available_since: str | None = None
    """Timestamp since the agent has been available"""
    contact: dict[str, Any] | None = None
    """Contact details of the agent including name, email, phone, and job title"""
    occasional: bool | None = None
    """Whether the agent is an occasional agent"""
    signature: str | None = None
    """Signature of the agent (HTML)"""
    ticket_scope: int | None = None
    """Ticket scope: 1=Global, 2=Group, 3=Restricted"""
    type_: str | None = None
    """Agent type: support_agent, field_agent, collaborator"""
    last_active_at: str | None = None
    """Timestamp of last agent activity"""
    created_at: str | None = None
    """Agent creation timestamp"""
    updated_at: str | None = None
    """Agent last update timestamp"""


class GroupsSearchData(BaseModel):
    """Search result data for groups entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique group ID"""
    name: str | None = None
    """Name of the group"""
    description: str | None = None
    """Description of the group"""
    auto_ticket_assign: int | None = None
    """Auto ticket assignment: 0=Disabled, 1=Round Robin, 2=Skill Based, 3=Load Based"""
    business_hour_id: int | None = None
    """ID of the associated business hour"""
    escalate_to: int | None = None
    """User ID for escalation"""
    group_type: str | None = None
    """Type of the group (e.g., support_agent_group)"""
    unassigned_for: str | None = None
    """Time after which escalation triggers"""
    created_at: str | None = None
    """Group creation timestamp"""
    updated_at: str | None = None
    """Group last update timestamp"""


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

TicketsSearchResult = AirbyteSearchResult[TicketsSearchData]
"""Search result type for tickets entity."""

AgentsSearchResult = AirbyteSearchResult[AgentsSearchData]
"""Search result type for agents entity."""

GroupsSearchResult = AirbyteSearchResult[GroupsSearchData]
"""Search result type for groups entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

TicketsListResult = FreshdeskExecuteResultWithMeta[list[Ticket], TicketsListResultMeta]
"""Result type for tickets.list operation with data and metadata."""

ContactsListResult = FreshdeskExecuteResultWithMeta[list[Contact], ContactsListResultMeta]
"""Result type for contacts.list operation with data and metadata."""

AgentsListResult = FreshdeskExecuteResultWithMeta[list[Agent], AgentsListResultMeta]
"""Result type for agents.list operation with data and metadata."""

GroupsListResult = FreshdeskExecuteResultWithMeta[list[Group], GroupsListResultMeta]
"""Result type for groups.list operation with data and metadata."""

CompaniesListResult = FreshdeskExecuteResultWithMeta[list[Company], CompaniesListResultMeta]
"""Result type for companies.list operation with data and metadata."""

RolesListResult = FreshdeskExecuteResultWithMeta[list[Role], RolesListResultMeta]
"""Result type for roles.list operation with data and metadata."""

SatisfactionRatingsListResult = FreshdeskExecuteResultWithMeta[list[SatisfactionRating], SatisfactionRatingsListResultMeta]
"""Result type for satisfaction_ratings.list operation with data and metadata."""

SurveysListResult = FreshdeskExecuteResultWithMeta[list[Survey], SurveysListResultMeta]
"""Result type for surveys.list operation with data and metadata."""

TimeEntriesListResult = FreshdeskExecuteResultWithMeta[list[TimeEntry], TimeEntriesListResultMeta]
"""Result type for time_entries.list operation with data and metadata."""

TicketFieldsListResult = FreshdeskExecuteResultWithMeta[list[TicketField], TicketFieldsListResultMeta]
"""Result type for ticket_fields.list operation with data and metadata."""

