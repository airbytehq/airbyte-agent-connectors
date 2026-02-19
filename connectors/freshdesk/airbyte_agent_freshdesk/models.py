"""
Pydantic models for freshdesk connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

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

    id: Union[int, Any] = Field(default=None)
    subject: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    description_text: Union[str | None, Any] = Field(default=None)
    status: Union[int | None, Any] = Field(default=None)
    priority: Union[int | None, Any] = Field(default=None)
    source: Union[int | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    requester_id: Union[int | None, Any] = Field(default=None)
    responder_id: Union[int | None, Any] = Field(default=None)
    company_id: Union[int | None, Any] = Field(default=None)
    group_id: Union[int | None, Any] = Field(default=None)
    product_id: Union[int | None, Any] = Field(default=None)
    email_config_id: Union[int | None, Any] = Field(default=None)
    cc_emails: Union[list[str] | None, Any] = Field(default=None)
    fwd_emails: Union[list[str] | None, Any] = Field(default=None)
    reply_cc_emails: Union[list[str] | None, Any] = Field(default=None)
    to_emails: Union[list[str] | None, Any] = Field(default=None)
    spam: Union[bool | None, Any] = Field(default=None)
    deleted: Union[bool | None, Any] = Field(default=None)
    fr_escalated: Union[bool | None, Any] = Field(default=None)
    is_escalated: Union[bool | None, Any] = Field(default=None)
    fr_due_by: Union[str | None, Any] = Field(default=None)
    due_by: Union[str | None, Any] = Field(default=None)
    tags: Union[list[str] | None, Any] = Field(default=None)
    custom_fields: Union[dict[str, Any] | None, Any] = Field(default=None)
    attachments: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    association_type: Union[int | None, Any] = Field(default=None)
    associated_tickets_count: Union[int | None, Any] = Field(default=None)
    ticket_cc_emails: Union[list[str] | None, Any] = Field(default=None)
    ticket_bcc_emails: Union[list[str] | None, Any] = Field(default=None)
    support_email: Union[str | None, Any] = Field(default=None)
    source_additional_info: Union[dict[str, Any] | None, Any] = Field(default=None)
    structured_description: Union[dict[str, Any] | None, Any] = Field(default=None)
    form_id: Union[int | None, Any] = Field(default=None)
    nr_due_by: Union[str | None, Any] = Field(default=None)
    nr_escalated: Union[bool | None, Any] = Field(default=None)

class Contact(BaseModel):
    """A Freshdesk contact (customer)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    mobile: Union[str | None, Any] = Field(default=None)
    active: Union[bool | None, Any] = Field(default=None)
    address: Union[str | None, Any] = Field(default=None)
    avatar: Union[dict[str, Any] | None, Any] = Field(default=None)
    company_id: Union[int | None, Any] = Field(default=None)
    view_all_tickets: Union[bool | None, Any] = Field(default=None)
    custom_fields: Union[dict[str, Any] | None, Any] = Field(default=None)
    deleted: Union[bool | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    job_title: Union[str | None, Any] = Field(default=None)
    language: Union[str | None, Any] = Field(default=None)
    twitter_id: Union[str | None, Any] = Field(default=None)
    unique_external_id: Union[str | None, Any] = Field(default=None)
    other_emails: Union[list[str] | None, Any] = Field(default=None)
    other_companies: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    tags: Union[list[str] | None, Any] = Field(default=None)
    time_zone: Union[str | None, Any] = Field(default=None)
    facebook_id: Union[str | None, Any] = Field(default=None)
    csat_rating: Union[int | None, Any] = Field(default=None)
    preferred_source: Union[str | None, Any] = Field(default=None)
    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    visitor_id: Union[str | None, Any] = Field(default=None)
    org_contact_id: Union[int | None, Any] = Field(default=None)
    org_contact_id_str: Union[str | None, Any] = Field(default=None)
    other_phone_numbers: Union[list[str] | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class AgentContact(BaseModel):
    """Contact details of the agent"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active: Union[bool | None, Any] = Field(default=None, description="Whether the contact is active")
    """Whether the contact is active"""
    email: Union[str | None, Any] = Field(default=None, description="Email of the agent")
    """Email of the agent"""
    job_title: Union[str | None, Any] = Field(default=None, description="Job title")
    """Job title"""
    language: Union[str | None, Any] = Field(default=None, description="Language")
    """Language"""
    last_login_at: Union[str | None, Any] = Field(default=None, description="Last login timestamp")
    """Last login timestamp"""
    mobile: Union[str | None, Any] = Field(default=None, description="Mobile number")
    """Mobile number"""
    name: Union[str | None, Any] = Field(default=None, description="Name of the agent")
    """Name of the agent"""
    phone: Union[str | None, Any] = Field(default=None, description="Phone number")
    """Phone number"""
    time_zone: Union[str | None, Any] = Field(default=None, description="Time zone")
    """Time zone"""
    created_at: Union[str | None, Any] = Field(default=None, description="Contact creation timestamp")
    """Contact creation timestamp"""
    updated_at: Union[str | None, Any] = Field(default=None, description="Contact update timestamp")
    """Contact update timestamp"""

class Agent(BaseModel):
    """A Freshdesk agent"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    available: Union[bool | None, Any] = Field(default=None)
    available_since: Union[str | None, Any] = Field(default=None)
    occasional: Union[bool | None, Any] = Field(default=None)
    signature: Union[str | None, Any] = Field(default=None)
    ticket_scope: Union[int | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    skill_ids: Union[list[int] | None, Any] = Field(default=None)
    group_ids: Union[list[int] | None, Any] = Field(default=None)
    role_ids: Union[list[int] | None, Any] = Field(default=None)
    focus_mode: Union[bool | None, Any] = Field(default=None)
    contact: Union[AgentContact | None, Any] = Field(default=None)
    last_active_at: Union[str | None, Any] = Field(default=None)
    deactivated: Union[bool | None, Any] = Field(default=None)
    agent_operational_status: Union[str | None, Any] = Field(default=None)
    org_agent_id: Union[str | None, Any] = Field(default=None)
    org_group_ids: Union[list[str] | None, Any] = Field(default=None)
    contribution_group_ids: Union[list[int] | None, Any] = Field(default=None)
    org_contribution_group_ids: Union[list[str] | None, Any] = Field(default=None)
    scope: Union[Any, Any] = Field(default=None)
    availability: Union[Any, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class Group(BaseModel):
    """A Freshdesk group"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    agent_ids: Union[list[int] | None, Any] = Field(default=None)
    auto_ticket_assign: Union[int | None, Any] = Field(default=None)
    business_hour_id: Union[int | None, Any] = Field(default=None)
    escalate_to: Union[int | None, Any] = Field(default=None)
    unassigned_for: Union[str | None, Any] = Field(default=None)
    group_type: Union[str | None, Any] = Field(default=None)
    allow_agents_to_change_availability: Union[bool | None, Any] = Field(default=None)
    agent_availability_status: Union[bool | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class Company(BaseModel):
    """A Freshdesk company"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    domains: Union[list[str] | None, Any] = Field(default=None)
    note: Union[str | None, Any] = Field(default=None)
    health_score: Union[str | None, Any] = Field(default=None)
    account_tier: Union[str | None, Any] = Field(default=None)
    renewal_date: Union[str | None, Any] = Field(default=None)
    industry: Union[str | None, Any] = Field(default=None)
    custom_fields: Union[dict[str, Any] | None, Any] = Field(default=None)
    org_company_id: Union[Any, Any] = Field(default=None)
    org_company_id_str: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class Role(BaseModel):
    """A Freshdesk role"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    default: Union[bool | None, Any] = Field(default=None)
    agent_type: Union[int | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class SatisfactionRating(BaseModel):
    """A Freshdesk satisfaction rating"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    survey_id: Union[int | None, Any] = Field(default=None)
    user_id: Union[int | None, Any] = Field(default=None)
    agent_id: Union[int | None, Any] = Field(default=None)
    group_id: Union[int | None, Any] = Field(default=None)
    ticket_id: Union[int | None, Any] = Field(default=None)
    feedback: Union[str | None, Any] = Field(default=None)
    ratings: Union[dict[str, Any] | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class SurveyQuestionsItem(BaseModel):
    """Nested schema for Survey.questions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None, description="Question ID")
    """Question ID"""
    label: Union[str | None, Any] = Field(default=None, description="Question label")
    """Question label"""
    accepted_ratings: Union[list[int] | None, Any] = Field(default=None, description="Accepted rating values")
    """Accepted rating values"""

class Survey(BaseModel):
    """A Freshdesk survey"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    active: Union[bool | None, Any] = Field(default=None)
    questions: Union[list[SurveyQuestionsItem] | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class TimeEntry(BaseModel):
    """A Freshdesk time entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    agent_id: Union[int | None, Any] = Field(default=None)
    ticket_id: Union[int | None, Any] = Field(default=None)
    company_id: Union[int | None, Any] = Field(default=None)
    billable: Union[bool | None, Any] = Field(default=None)
    note: Union[str | None, Any] = Field(default=None)
    time_spent: Union[str | None, Any] = Field(default=None)
    timer_running: Union[bool | None, Any] = Field(default=None)
    executed_at: Union[str | None, Any] = Field(default=None)
    start_time: Union[str | None, Any] = Field(default=None)
    time_spent_in_seconds: Union[int | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class TicketField(BaseModel):
    """A Freshdesk ticket field definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    label: Union[str | None, Any] = Field(default=None)
    label_for_customers: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    position: Union[int | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    default: Union[bool | None, Any] = Field(default=None)
    required_for_closure: Union[bool | None, Any] = Field(default=None)
    required_for_agents: Union[bool | None, Any] = Field(default=None)
    required_for_customers: Union[bool | None, Any] = Field(default=None)
    customers_can_edit: Union[bool | None, Any] = Field(default=None)
    displayed_to_customers: Union[bool | None, Any] = Field(default=None)
    customers_can_filter: Union[bool | None, Any] = Field(default=None)
    portal_cc: Union[bool | None, Any] = Field(default=None)
    portal_cc_to: Union[str | None, Any] = Field(default=None)
    choices: Union[Any, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

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
    type: str | None = None
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
    type: str | None = None
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

TicketsListResult = FreshdeskExecuteResult[list[Ticket]]
"""Result type for tickets.list operation."""

ContactsListResult = FreshdeskExecuteResult[list[Contact]]
"""Result type for contacts.list operation."""

AgentsListResult = FreshdeskExecuteResult[list[Agent]]
"""Result type for agents.list operation."""

GroupsListResult = FreshdeskExecuteResult[list[Group]]
"""Result type for groups.list operation."""

CompaniesListResult = FreshdeskExecuteResult[list[Company]]
"""Result type for companies.list operation."""

RolesListResult = FreshdeskExecuteResult[list[Role]]
"""Result type for roles.list operation."""

SatisfactionRatingsListResult = FreshdeskExecuteResult[list[SatisfactionRating]]
"""Result type for satisfaction_ratings.list operation."""

SurveysListResult = FreshdeskExecuteResult[list[Survey]]
"""Result type for surveys.list operation."""

TimeEntriesListResult = FreshdeskExecuteResult[list[TimeEntry]]
"""Result type for time_entries.list operation."""

TicketFieldsListResult = FreshdeskExecuteResult[list[TicketField]]
"""Result type for ticket_fields.list operation."""

