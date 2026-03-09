"""
Type definitions for freshdesk connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class TicketsListParams(TypedDict):
    """Parameters for tickets.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    updated_since: NotRequired[str]
    order_by: NotRequired[str]
    order_type: NotRequired[str]

class TicketsGetParams(TypedDict):
    """Parameters for tickets.get operation"""
    id: str

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    updated_since: NotRequired[str]

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    id: str

class AgentsListParams(TypedDict):
    """Parameters for agents.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class AgentsGetParams(TypedDict):
    """Parameters for agents.get operation"""
    id: str

class GroupsListParams(TypedDict):
    """Parameters for groups.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class GroupsGetParams(TypedDict):
    """Parameters for groups.get operation"""
    id: str

class CompaniesListParams(TypedDict):
    """Parameters for companies.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class CompaniesGetParams(TypedDict):
    """Parameters for companies.get operation"""
    id: str

class RolesListParams(TypedDict):
    """Parameters for roles.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class RolesGetParams(TypedDict):
    """Parameters for roles.get operation"""
    id: str

class SatisfactionRatingsListParams(TypedDict):
    """Parameters for satisfaction_ratings.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    created_since: NotRequired[str]

class SurveysListParams(TypedDict):
    """Parameters for surveys.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class TimeEntriesListParams(TypedDict):
    """Parameters for time_entries.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class TicketFieldsListParams(TypedDict):
    """Parameters for ticket_fields.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== TICKETS SEARCH TYPES =====

class TicketsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tickets search queries."""
    id: int | None
    """Unique ticket ID"""
    subject: str | None
    """Subject of the ticket"""
    description: str | None
    """HTML content of the ticket"""
    description_text: str | None
    """Plain text content of the ticket"""
    status: int | None
    """Status: 2=Open, 3=Pending, 4=Resolved, 5=Closed"""
    priority: int | None
    """Priority: 1=Low, 2=Medium, 3=High, 4=Urgent"""
    source: int | None
    """Source: 1=Email, 2=Portal, 3=Phone, 7=Chat, 9=Feedback Widget, 10=Outbound Email"""
    type_: str | None
    """Ticket type"""
    requester_id: int | None
    """ID of the requester"""
    requester: dict[str, Any] | None
    """Requester details including name, email, and contact info"""
    responder_id: int | None
    """ID of the agent to whom the ticket is assigned"""
    group_id: int | None
    """ID of the group to which the ticket is assigned"""
    company_id: int | None
    """Company ID of the requester"""
    product_id: int | None
    """ID of the product associated with the ticket"""
    email_config_id: int | None
    """ID of the email config used for the ticket"""
    cc_emails: list[Any] | None
    """CC email addresses"""
    ticket_cc_emails: list[Any] | None
    """Ticket CC email addresses"""
    to_emails: list[Any] | None
    """To email addresses"""
    fwd_emails: list[Any] | None
    """Forwarded email addresses"""
    reply_cc_emails: list[Any] | None
    """Reply CC email addresses"""
    tags: list[Any] | None
    """Tags associated with the ticket"""
    custom_fields: dict[str, Any] | None
    """Custom fields associated with the ticket"""
    due_by: str | None
    """Resolution due by timestamp"""
    fr_due_by: str | None
    """First response due by timestamp"""
    fr_escalated: bool | None
    """Whether the first response time was breached"""
    is_escalated: bool | None
    """Whether the ticket is escalated"""
    nr_due_by: str | None
    """Next response due by timestamp"""
    nr_escalated: bool | None
    """Whether the next response time was breached"""
    spam: bool | None
    """Whether the ticket is marked as spam"""
    association_type: int | None
    """Association type for parent/child tickets"""
    associated_tickets_count: int | None
    """Number of associated tickets"""
    stats: dict[str, Any] | None
    """Ticket statistics including response and resolution times"""
    created_at: str | None
    """Ticket creation timestamp"""
    updated_at: str | None
    """Ticket last update timestamp"""


class TicketsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique ticket ID"""
    subject: list[str]
    """Subject of the ticket"""
    description: list[str]
    """HTML content of the ticket"""
    description_text: list[str]
    """Plain text content of the ticket"""
    status: list[int]
    """Status: 2=Open, 3=Pending, 4=Resolved, 5=Closed"""
    priority: list[int]
    """Priority: 1=Low, 2=Medium, 3=High, 4=Urgent"""
    source: list[int]
    """Source: 1=Email, 2=Portal, 3=Phone, 7=Chat, 9=Feedback Widget, 10=Outbound Email"""
    type_: list[str]
    """Ticket type"""
    requester_id: list[int]
    """ID of the requester"""
    requester: list[dict[str, Any]]
    """Requester details including name, email, and contact info"""
    responder_id: list[int]
    """ID of the agent to whom the ticket is assigned"""
    group_id: list[int]
    """ID of the group to which the ticket is assigned"""
    company_id: list[int]
    """Company ID of the requester"""
    product_id: list[int]
    """ID of the product associated with the ticket"""
    email_config_id: list[int]
    """ID of the email config used for the ticket"""
    cc_emails: list[list[Any]]
    """CC email addresses"""
    ticket_cc_emails: list[list[Any]]
    """Ticket CC email addresses"""
    to_emails: list[list[Any]]
    """To email addresses"""
    fwd_emails: list[list[Any]]
    """Forwarded email addresses"""
    reply_cc_emails: list[list[Any]]
    """Reply CC email addresses"""
    tags: list[list[Any]]
    """Tags associated with the ticket"""
    custom_fields: list[dict[str, Any]]
    """Custom fields associated with the ticket"""
    due_by: list[str]
    """Resolution due by timestamp"""
    fr_due_by: list[str]
    """First response due by timestamp"""
    fr_escalated: list[bool]
    """Whether the first response time was breached"""
    is_escalated: list[bool]
    """Whether the ticket is escalated"""
    nr_due_by: list[str]
    """Next response due by timestamp"""
    nr_escalated: list[bool]
    """Whether the next response time was breached"""
    spam: list[bool]
    """Whether the ticket is marked as spam"""
    association_type: list[int]
    """Association type for parent/child tickets"""
    associated_tickets_count: list[int]
    """Number of associated tickets"""
    stats: list[dict[str, Any]]
    """Ticket statistics including response and resolution times"""
    created_at: list[str]
    """Ticket creation timestamp"""
    updated_at: list[str]
    """Ticket last update timestamp"""


class TicketsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique ticket ID"""
    subject: Any
    """Subject of the ticket"""
    description: Any
    """HTML content of the ticket"""
    description_text: Any
    """Plain text content of the ticket"""
    status: Any
    """Status: 2=Open, 3=Pending, 4=Resolved, 5=Closed"""
    priority: Any
    """Priority: 1=Low, 2=Medium, 3=High, 4=Urgent"""
    source: Any
    """Source: 1=Email, 2=Portal, 3=Phone, 7=Chat, 9=Feedback Widget, 10=Outbound Email"""
    type_: Any
    """Ticket type"""
    requester_id: Any
    """ID of the requester"""
    requester: Any
    """Requester details including name, email, and contact info"""
    responder_id: Any
    """ID of the agent to whom the ticket is assigned"""
    group_id: Any
    """ID of the group to which the ticket is assigned"""
    company_id: Any
    """Company ID of the requester"""
    product_id: Any
    """ID of the product associated with the ticket"""
    email_config_id: Any
    """ID of the email config used for the ticket"""
    cc_emails: Any
    """CC email addresses"""
    ticket_cc_emails: Any
    """Ticket CC email addresses"""
    to_emails: Any
    """To email addresses"""
    fwd_emails: Any
    """Forwarded email addresses"""
    reply_cc_emails: Any
    """Reply CC email addresses"""
    tags: Any
    """Tags associated with the ticket"""
    custom_fields: Any
    """Custom fields associated with the ticket"""
    due_by: Any
    """Resolution due by timestamp"""
    fr_due_by: Any
    """First response due by timestamp"""
    fr_escalated: Any
    """Whether the first response time was breached"""
    is_escalated: Any
    """Whether the ticket is escalated"""
    nr_due_by: Any
    """Next response due by timestamp"""
    nr_escalated: Any
    """Whether the next response time was breached"""
    spam: Any
    """Whether the ticket is marked as spam"""
    association_type: Any
    """Association type for parent/child tickets"""
    associated_tickets_count: Any
    """Number of associated tickets"""
    stats: Any
    """Ticket statistics including response and resolution times"""
    created_at: Any
    """Ticket creation timestamp"""
    updated_at: Any
    """Ticket last update timestamp"""


class TicketsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique ticket ID"""
    subject: str
    """Subject of the ticket"""
    description: str
    """HTML content of the ticket"""
    description_text: str
    """Plain text content of the ticket"""
    status: str
    """Status: 2=Open, 3=Pending, 4=Resolved, 5=Closed"""
    priority: str
    """Priority: 1=Low, 2=Medium, 3=High, 4=Urgent"""
    source: str
    """Source: 1=Email, 2=Portal, 3=Phone, 7=Chat, 9=Feedback Widget, 10=Outbound Email"""
    type_: str
    """Ticket type"""
    requester_id: str
    """ID of the requester"""
    requester: str
    """Requester details including name, email, and contact info"""
    responder_id: str
    """ID of the agent to whom the ticket is assigned"""
    group_id: str
    """ID of the group to which the ticket is assigned"""
    company_id: str
    """Company ID of the requester"""
    product_id: str
    """ID of the product associated with the ticket"""
    email_config_id: str
    """ID of the email config used for the ticket"""
    cc_emails: str
    """CC email addresses"""
    ticket_cc_emails: str
    """Ticket CC email addresses"""
    to_emails: str
    """To email addresses"""
    fwd_emails: str
    """Forwarded email addresses"""
    reply_cc_emails: str
    """Reply CC email addresses"""
    tags: str
    """Tags associated with the ticket"""
    custom_fields: str
    """Custom fields associated with the ticket"""
    due_by: str
    """Resolution due by timestamp"""
    fr_due_by: str
    """First response due by timestamp"""
    fr_escalated: str
    """Whether the first response time was breached"""
    is_escalated: str
    """Whether the ticket is escalated"""
    nr_due_by: str
    """Next response due by timestamp"""
    nr_escalated: str
    """Whether the next response time was breached"""
    spam: str
    """Whether the ticket is marked as spam"""
    association_type: str
    """Association type for parent/child tickets"""
    associated_tickets_count: str
    """Number of associated tickets"""
    stats: str
    """Ticket statistics including response and resolution times"""
    created_at: str
    """Ticket creation timestamp"""
    updated_at: str
    """Ticket last update timestamp"""


class TicketsSortFilter(TypedDict, total=False):
    """Available fields for sorting tickets search results."""
    id: AirbyteSortOrder
    """Unique ticket ID"""
    subject: AirbyteSortOrder
    """Subject of the ticket"""
    description: AirbyteSortOrder
    """HTML content of the ticket"""
    description_text: AirbyteSortOrder
    """Plain text content of the ticket"""
    status: AirbyteSortOrder
    """Status: 2=Open, 3=Pending, 4=Resolved, 5=Closed"""
    priority: AirbyteSortOrder
    """Priority: 1=Low, 2=Medium, 3=High, 4=Urgent"""
    source: AirbyteSortOrder
    """Source: 1=Email, 2=Portal, 3=Phone, 7=Chat, 9=Feedback Widget, 10=Outbound Email"""
    type_: AirbyteSortOrder
    """Ticket type"""
    requester_id: AirbyteSortOrder
    """ID of the requester"""
    requester: AirbyteSortOrder
    """Requester details including name, email, and contact info"""
    responder_id: AirbyteSortOrder
    """ID of the agent to whom the ticket is assigned"""
    group_id: AirbyteSortOrder
    """ID of the group to which the ticket is assigned"""
    company_id: AirbyteSortOrder
    """Company ID of the requester"""
    product_id: AirbyteSortOrder
    """ID of the product associated with the ticket"""
    email_config_id: AirbyteSortOrder
    """ID of the email config used for the ticket"""
    cc_emails: AirbyteSortOrder
    """CC email addresses"""
    ticket_cc_emails: AirbyteSortOrder
    """Ticket CC email addresses"""
    to_emails: AirbyteSortOrder
    """To email addresses"""
    fwd_emails: AirbyteSortOrder
    """Forwarded email addresses"""
    reply_cc_emails: AirbyteSortOrder
    """Reply CC email addresses"""
    tags: AirbyteSortOrder
    """Tags associated with the ticket"""
    custom_fields: AirbyteSortOrder
    """Custom fields associated with the ticket"""
    due_by: AirbyteSortOrder
    """Resolution due by timestamp"""
    fr_due_by: AirbyteSortOrder
    """First response due by timestamp"""
    fr_escalated: AirbyteSortOrder
    """Whether the first response time was breached"""
    is_escalated: AirbyteSortOrder
    """Whether the ticket is escalated"""
    nr_due_by: AirbyteSortOrder
    """Next response due by timestamp"""
    nr_escalated: AirbyteSortOrder
    """Whether the next response time was breached"""
    spam: AirbyteSortOrder
    """Whether the ticket is marked as spam"""
    association_type: AirbyteSortOrder
    """Association type for parent/child tickets"""
    associated_tickets_count: AirbyteSortOrder
    """Number of associated tickets"""
    stats: AirbyteSortOrder
    """Ticket statistics including response and resolution times"""
    created_at: AirbyteSortOrder
    """Ticket creation timestamp"""
    updated_at: AirbyteSortOrder
    """Ticket last update timestamp"""


# Entity-specific condition types for tickets
class TicketsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TicketsSearchFilter


class TicketsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TicketsSearchFilter


class TicketsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TicketsSearchFilter


class TicketsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TicketsSearchFilter


class TicketsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TicketsSearchFilter


class TicketsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TicketsSearchFilter


class TicketsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TicketsStringFilter


class TicketsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TicketsStringFilter


class TicketsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TicketsStringFilter


class TicketsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TicketsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TicketsInCondition = TypedDict("TicketsInCondition", {"in": TicketsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TicketsNotCondition = TypedDict("TicketsNotCondition", {"not": "TicketsCondition"}, total=False)
"""Negates the nested condition."""

TicketsAndCondition = TypedDict("TicketsAndCondition", {"and": "list[TicketsCondition]"}, total=False)
"""True if all nested conditions are true."""

TicketsOrCondition = TypedDict("TicketsOrCondition", {"or": "list[TicketsCondition]"}, total=False)
"""True if any nested condition is true."""

TicketsAnyCondition = TypedDict("TicketsAnyCondition", {"any": TicketsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tickets condition types
TicketsCondition = (
    TicketsEqCondition
    | TicketsNeqCondition
    | TicketsGtCondition
    | TicketsGteCondition
    | TicketsLtCondition
    | TicketsLteCondition
    | TicketsInCondition
    | TicketsLikeCondition
    | TicketsFuzzyCondition
    | TicketsKeywordCondition
    | TicketsContainsCondition
    | TicketsNotCondition
    | TicketsAndCondition
    | TicketsOrCondition
    | TicketsAnyCondition
)


class TicketsSearchQuery(TypedDict, total=False):
    """Search query for tickets entity."""
    filter: TicketsCondition
    sort: list[TicketsSortFilter]


# ===== AGENTS SEARCH TYPES =====

class AgentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering agents search queries."""
    id: int | None
    """Unique agent ID"""
    available: bool | None
    """Whether the agent is available"""
    available_since: str | None
    """Timestamp since the agent has been available"""
    contact: dict[str, Any] | None
    """Contact details of the agent including name, email, phone, and job title"""
    occasional: bool | None
    """Whether the agent is an occasional agent"""
    signature: str | None
    """Signature of the agent (HTML)"""
    ticket_scope: int | None
    """Ticket scope: 1=Global, 2=Group, 3=Restricted"""
    type_: str | None
    """Agent type: support_agent, field_agent, collaborator"""
    last_active_at: str | None
    """Timestamp of last agent activity"""
    created_at: str | None
    """Agent creation timestamp"""
    updated_at: str | None
    """Agent last update timestamp"""


class AgentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique agent ID"""
    available: list[bool]
    """Whether the agent is available"""
    available_since: list[str]
    """Timestamp since the agent has been available"""
    contact: list[dict[str, Any]]
    """Contact details of the agent including name, email, phone, and job title"""
    occasional: list[bool]
    """Whether the agent is an occasional agent"""
    signature: list[str]
    """Signature of the agent (HTML)"""
    ticket_scope: list[int]
    """Ticket scope: 1=Global, 2=Group, 3=Restricted"""
    type_: list[str]
    """Agent type: support_agent, field_agent, collaborator"""
    last_active_at: list[str]
    """Timestamp of last agent activity"""
    created_at: list[str]
    """Agent creation timestamp"""
    updated_at: list[str]
    """Agent last update timestamp"""


class AgentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique agent ID"""
    available: Any
    """Whether the agent is available"""
    available_since: Any
    """Timestamp since the agent has been available"""
    contact: Any
    """Contact details of the agent including name, email, phone, and job title"""
    occasional: Any
    """Whether the agent is an occasional agent"""
    signature: Any
    """Signature of the agent (HTML)"""
    ticket_scope: Any
    """Ticket scope: 1=Global, 2=Group, 3=Restricted"""
    type_: Any
    """Agent type: support_agent, field_agent, collaborator"""
    last_active_at: Any
    """Timestamp of last agent activity"""
    created_at: Any
    """Agent creation timestamp"""
    updated_at: Any
    """Agent last update timestamp"""


class AgentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique agent ID"""
    available: str
    """Whether the agent is available"""
    available_since: str
    """Timestamp since the agent has been available"""
    contact: str
    """Contact details of the agent including name, email, phone, and job title"""
    occasional: str
    """Whether the agent is an occasional agent"""
    signature: str
    """Signature of the agent (HTML)"""
    ticket_scope: str
    """Ticket scope: 1=Global, 2=Group, 3=Restricted"""
    type_: str
    """Agent type: support_agent, field_agent, collaborator"""
    last_active_at: str
    """Timestamp of last agent activity"""
    created_at: str
    """Agent creation timestamp"""
    updated_at: str
    """Agent last update timestamp"""


class AgentsSortFilter(TypedDict, total=False):
    """Available fields for sorting agents search results."""
    id: AirbyteSortOrder
    """Unique agent ID"""
    available: AirbyteSortOrder
    """Whether the agent is available"""
    available_since: AirbyteSortOrder
    """Timestamp since the agent has been available"""
    contact: AirbyteSortOrder
    """Contact details of the agent including name, email, phone, and job title"""
    occasional: AirbyteSortOrder
    """Whether the agent is an occasional agent"""
    signature: AirbyteSortOrder
    """Signature of the agent (HTML)"""
    ticket_scope: AirbyteSortOrder
    """Ticket scope: 1=Global, 2=Group, 3=Restricted"""
    type_: AirbyteSortOrder
    """Agent type: support_agent, field_agent, collaborator"""
    last_active_at: AirbyteSortOrder
    """Timestamp of last agent activity"""
    created_at: AirbyteSortOrder
    """Agent creation timestamp"""
    updated_at: AirbyteSortOrder
    """Agent last update timestamp"""


# Entity-specific condition types for agents
class AgentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AgentsSearchFilter


class AgentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AgentsSearchFilter


class AgentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AgentsSearchFilter


class AgentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AgentsSearchFilter


class AgentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AgentsSearchFilter


class AgentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AgentsSearchFilter


class AgentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AgentsStringFilter


class AgentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AgentsStringFilter


class AgentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AgentsStringFilter


class AgentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AgentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AgentsInCondition = TypedDict("AgentsInCondition", {"in": AgentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AgentsNotCondition = TypedDict("AgentsNotCondition", {"not": "AgentsCondition"}, total=False)
"""Negates the nested condition."""

AgentsAndCondition = TypedDict("AgentsAndCondition", {"and": "list[AgentsCondition]"}, total=False)
"""True if all nested conditions are true."""

AgentsOrCondition = TypedDict("AgentsOrCondition", {"or": "list[AgentsCondition]"}, total=False)
"""True if any nested condition is true."""

AgentsAnyCondition = TypedDict("AgentsAnyCondition", {"any": AgentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all agents condition types
AgentsCondition = (
    AgentsEqCondition
    | AgentsNeqCondition
    | AgentsGtCondition
    | AgentsGteCondition
    | AgentsLtCondition
    | AgentsLteCondition
    | AgentsInCondition
    | AgentsLikeCondition
    | AgentsFuzzyCondition
    | AgentsKeywordCondition
    | AgentsContainsCondition
    | AgentsNotCondition
    | AgentsAndCondition
    | AgentsOrCondition
    | AgentsAnyCondition
)


class AgentsSearchQuery(TypedDict, total=False):
    """Search query for agents entity."""
    filter: AgentsCondition
    sort: list[AgentsSortFilter]


# ===== GROUPS SEARCH TYPES =====

class GroupsSearchFilter(TypedDict, total=False):
    """Available fields for filtering groups search queries."""
    id: int | None
    """Unique group ID"""
    name: str | None
    """Name of the group"""
    description: str | None
    """Description of the group"""
    auto_ticket_assign: int | None
    """Auto ticket assignment: 0=Disabled, 1=Round Robin, 2=Skill Based, 3=Load Based"""
    business_hour_id: int | None
    """ID of the associated business hour"""
    escalate_to: int | None
    """User ID for escalation"""
    group_type: str | None
    """Type of the group (e.g., support_agent_group)"""
    unassigned_for: str | None
    """Time after which escalation triggers"""
    created_at: str | None
    """Group creation timestamp"""
    updated_at: str | None
    """Group last update timestamp"""


class GroupsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique group ID"""
    name: list[str]
    """Name of the group"""
    description: list[str]
    """Description of the group"""
    auto_ticket_assign: list[int]
    """Auto ticket assignment: 0=Disabled, 1=Round Robin, 2=Skill Based, 3=Load Based"""
    business_hour_id: list[int]
    """ID of the associated business hour"""
    escalate_to: list[int]
    """User ID for escalation"""
    group_type: list[str]
    """Type of the group (e.g., support_agent_group)"""
    unassigned_for: list[str]
    """Time after which escalation triggers"""
    created_at: list[str]
    """Group creation timestamp"""
    updated_at: list[str]
    """Group last update timestamp"""


class GroupsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique group ID"""
    name: Any
    """Name of the group"""
    description: Any
    """Description of the group"""
    auto_ticket_assign: Any
    """Auto ticket assignment: 0=Disabled, 1=Round Robin, 2=Skill Based, 3=Load Based"""
    business_hour_id: Any
    """ID of the associated business hour"""
    escalate_to: Any
    """User ID for escalation"""
    group_type: Any
    """Type of the group (e.g., support_agent_group)"""
    unassigned_for: Any
    """Time after which escalation triggers"""
    created_at: Any
    """Group creation timestamp"""
    updated_at: Any
    """Group last update timestamp"""


class GroupsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique group ID"""
    name: str
    """Name of the group"""
    description: str
    """Description of the group"""
    auto_ticket_assign: str
    """Auto ticket assignment: 0=Disabled, 1=Round Robin, 2=Skill Based, 3=Load Based"""
    business_hour_id: str
    """ID of the associated business hour"""
    escalate_to: str
    """User ID for escalation"""
    group_type: str
    """Type of the group (e.g., support_agent_group)"""
    unassigned_for: str
    """Time after which escalation triggers"""
    created_at: str
    """Group creation timestamp"""
    updated_at: str
    """Group last update timestamp"""


class GroupsSortFilter(TypedDict, total=False):
    """Available fields for sorting groups search results."""
    id: AirbyteSortOrder
    """Unique group ID"""
    name: AirbyteSortOrder
    """Name of the group"""
    description: AirbyteSortOrder
    """Description of the group"""
    auto_ticket_assign: AirbyteSortOrder
    """Auto ticket assignment: 0=Disabled, 1=Round Robin, 2=Skill Based, 3=Load Based"""
    business_hour_id: AirbyteSortOrder
    """ID of the associated business hour"""
    escalate_to: AirbyteSortOrder
    """User ID for escalation"""
    group_type: AirbyteSortOrder
    """Type of the group (e.g., support_agent_group)"""
    unassigned_for: AirbyteSortOrder
    """Time after which escalation triggers"""
    created_at: AirbyteSortOrder
    """Group creation timestamp"""
    updated_at: AirbyteSortOrder
    """Group last update timestamp"""


# Entity-specific condition types for groups
class GroupsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: GroupsSearchFilter


class GroupsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: GroupsSearchFilter


class GroupsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: GroupsSearchFilter


class GroupsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: GroupsSearchFilter


class GroupsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: GroupsSearchFilter


class GroupsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: GroupsSearchFilter


class GroupsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: GroupsStringFilter


class GroupsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: GroupsStringFilter


class GroupsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: GroupsStringFilter


class GroupsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: GroupsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
GroupsInCondition = TypedDict("GroupsInCondition", {"in": GroupsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

GroupsNotCondition = TypedDict("GroupsNotCondition", {"not": "GroupsCondition"}, total=False)
"""Negates the nested condition."""

GroupsAndCondition = TypedDict("GroupsAndCondition", {"and": "list[GroupsCondition]"}, total=False)
"""True if all nested conditions are true."""

GroupsOrCondition = TypedDict("GroupsOrCondition", {"or": "list[GroupsCondition]"}, total=False)
"""True if any nested condition is true."""

GroupsAnyCondition = TypedDict("GroupsAnyCondition", {"any": GroupsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all groups condition types
GroupsCondition = (
    GroupsEqCondition
    | GroupsNeqCondition
    | GroupsGtCondition
    | GroupsGteCondition
    | GroupsLtCondition
    | GroupsLteCondition
    | GroupsInCondition
    | GroupsLikeCondition
    | GroupsFuzzyCondition
    | GroupsKeywordCondition
    | GroupsContainsCondition
    | GroupsNotCondition
    | GroupsAndCondition
    | GroupsOrCondition
    | GroupsAnyCondition
)


class GroupsSearchQuery(TypedDict, total=False):
    """Search query for groups entity."""
    filter: GroupsCondition
    sort: list[GroupsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
