"""
Type definitions for freshdesk connector.
"""
# ruff: noqa: E501
from __future__ import annotations

from airbyte_agent_sdk.types import AirbyteAuthConfig  # noqa: F401

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
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
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


class TicketsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: TicketsStringFilter


class TicketsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: TicketsStringFilter


class TicketsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TicketsStringFilter


class TicketsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TicketsStringFilter


class TicketsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | TicketsStartswithCondition
    | TicketsEndswithCondition
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
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
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


class AgentsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: AgentsStringFilter


class AgentsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: AgentsStringFilter


class AgentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AgentsStringFilter


class AgentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AgentsStringFilter


class AgentsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | AgentsStartswithCondition
    | AgentsEndswithCondition
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
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
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


class GroupsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: GroupsStringFilter


class GroupsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: GroupsStringFilter


class GroupsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: GroupsStringFilter


class GroupsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: GroupsStringFilter


class GroupsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | GroupsStartswithCondition
    | GroupsEndswithCondition
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


# ===== CONTACTS SEARCH TYPES =====

class ContactsSearchFilter(TypedDict, total=False):
    """Available fields for filtering contacts search queries."""
    id: int | None
    """Unique contact ID"""
    name: str | None
    """Name of the contact"""
    email: str | None
    """Primary email address"""
    phone: str | None
    """Phone number"""
    mobile: str | None
    """Mobile number"""
    active: bool | None
    """Whether the contact has been verified"""
    address: str | None
    """Address of the contact"""
    company_id: int | None
    """ID of the primary company"""
    custom_fields: dict[str, Any] | None
    """Custom fields associated with the contact"""
    description: str | None
    """Description of the contact"""
    job_title: str | None
    """Job title of the contact"""
    language: str | None
    """Language of the contact"""
    twitter_id: str | None
    """Twitter ID"""
    unique_external_id: str | None
    """External ID of the contact"""
    time_zone: str | None
    """Time zone of the contact"""
    facebook_id: str | None
    """Facebook ID of the contact"""
    csat_rating: int | None
    """CSAT rating of the contact"""
    preferred_source: str | None
    """Preferred contact source"""
    created_at: str | None
    """Contact creation timestamp"""
    updated_at: str | None
    """Contact last update timestamp"""


class ContactsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique contact ID"""
    name: list[str]
    """Name of the contact"""
    email: list[str]
    """Primary email address"""
    phone: list[str]
    """Phone number"""
    mobile: list[str]
    """Mobile number"""
    active: list[bool]
    """Whether the contact has been verified"""
    address: list[str]
    """Address of the contact"""
    company_id: list[int]
    """ID of the primary company"""
    custom_fields: list[dict[str, Any]]
    """Custom fields associated with the contact"""
    description: list[str]
    """Description of the contact"""
    job_title: list[str]
    """Job title of the contact"""
    language: list[str]
    """Language of the contact"""
    twitter_id: list[str]
    """Twitter ID"""
    unique_external_id: list[str]
    """External ID of the contact"""
    time_zone: list[str]
    """Time zone of the contact"""
    facebook_id: list[str]
    """Facebook ID of the contact"""
    csat_rating: list[int]
    """CSAT rating of the contact"""
    preferred_source: list[str]
    """Preferred contact source"""
    created_at: list[str]
    """Contact creation timestamp"""
    updated_at: list[str]
    """Contact last update timestamp"""


class ContactsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique contact ID"""
    name: Any
    """Name of the contact"""
    email: Any
    """Primary email address"""
    phone: Any
    """Phone number"""
    mobile: Any
    """Mobile number"""
    active: Any
    """Whether the contact has been verified"""
    address: Any
    """Address of the contact"""
    company_id: Any
    """ID of the primary company"""
    custom_fields: Any
    """Custom fields associated with the contact"""
    description: Any
    """Description of the contact"""
    job_title: Any
    """Job title of the contact"""
    language: Any
    """Language of the contact"""
    twitter_id: Any
    """Twitter ID"""
    unique_external_id: Any
    """External ID of the contact"""
    time_zone: Any
    """Time zone of the contact"""
    facebook_id: Any
    """Facebook ID of the contact"""
    csat_rating: Any
    """CSAT rating of the contact"""
    preferred_source: Any
    """Preferred contact source"""
    created_at: Any
    """Contact creation timestamp"""
    updated_at: Any
    """Contact last update timestamp"""


class ContactsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique contact ID"""
    name: str
    """Name of the contact"""
    email: str
    """Primary email address"""
    phone: str
    """Phone number"""
    mobile: str
    """Mobile number"""
    active: str
    """Whether the contact has been verified"""
    address: str
    """Address of the contact"""
    company_id: str
    """ID of the primary company"""
    custom_fields: str
    """Custom fields associated with the contact"""
    description: str
    """Description of the contact"""
    job_title: str
    """Job title of the contact"""
    language: str
    """Language of the contact"""
    twitter_id: str
    """Twitter ID"""
    unique_external_id: str
    """External ID of the contact"""
    time_zone: str
    """Time zone of the contact"""
    facebook_id: str
    """Facebook ID of the contact"""
    csat_rating: str
    """CSAT rating of the contact"""
    preferred_source: str
    """Preferred contact source"""
    created_at: str
    """Contact creation timestamp"""
    updated_at: str
    """Contact last update timestamp"""


class ContactsSortFilter(TypedDict, total=False):
    """Available fields for sorting contacts search results."""
    id: AirbyteSortOrder
    """Unique contact ID"""
    name: AirbyteSortOrder
    """Name of the contact"""
    email: AirbyteSortOrder
    """Primary email address"""
    phone: AirbyteSortOrder
    """Phone number"""
    mobile: AirbyteSortOrder
    """Mobile number"""
    active: AirbyteSortOrder
    """Whether the contact has been verified"""
    address: AirbyteSortOrder
    """Address of the contact"""
    company_id: AirbyteSortOrder
    """ID of the primary company"""
    custom_fields: AirbyteSortOrder
    """Custom fields associated with the contact"""
    description: AirbyteSortOrder
    """Description of the contact"""
    job_title: AirbyteSortOrder
    """Job title of the contact"""
    language: AirbyteSortOrder
    """Language of the contact"""
    twitter_id: AirbyteSortOrder
    """Twitter ID"""
    unique_external_id: AirbyteSortOrder
    """External ID of the contact"""
    time_zone: AirbyteSortOrder
    """Time zone of the contact"""
    facebook_id: AirbyteSortOrder
    """Facebook ID of the contact"""
    csat_rating: AirbyteSortOrder
    """CSAT rating of the contact"""
    preferred_source: AirbyteSortOrder
    """Preferred contact source"""
    created_at: AirbyteSortOrder
    """Contact creation timestamp"""
    updated_at: AirbyteSortOrder
    """Contact last update timestamp"""


# Entity-specific condition types for contacts
class ContactsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ContactsSearchFilter


class ContactsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ContactsSearchFilter


class ContactsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ContactsSearchFilter


class ContactsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ContactsSearchFilter


class ContactsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ContactsSearchFilter


class ContactsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ContactsSearchFilter


class ContactsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: ContactsStringFilter


class ContactsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: ContactsStringFilter


class ContactsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ContactsStringFilter


class ContactsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ContactsStringFilter


class ContactsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: ContactsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ContactsInCondition = TypedDict("ContactsInCondition", {"in": ContactsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ContactsNotCondition = TypedDict("ContactsNotCondition", {"not": "ContactsCondition"}, total=False)
"""Negates the nested condition."""

ContactsAndCondition = TypedDict("ContactsAndCondition", {"and": "list[ContactsCondition]"}, total=False)
"""True if all nested conditions are true."""

ContactsOrCondition = TypedDict("ContactsOrCondition", {"or": "list[ContactsCondition]"}, total=False)
"""True if any nested condition is true."""

ContactsAnyCondition = TypedDict("ContactsAnyCondition", {"any": ContactsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all contacts condition types
ContactsCondition = (
    ContactsEqCondition
    | ContactsNeqCondition
    | ContactsGtCondition
    | ContactsGteCondition
    | ContactsLtCondition
    | ContactsLteCondition
    | ContactsInCondition
    | ContactsStartswithCondition
    | ContactsEndswithCondition
    | ContactsFuzzyCondition
    | ContactsKeywordCondition
    | ContactsContainsCondition
    | ContactsNotCondition
    | ContactsAndCondition
    | ContactsOrCondition
    | ContactsAnyCondition
)


class ContactsSearchQuery(TypedDict, total=False):
    """Search query for contacts entity."""
    filter: ContactsCondition
    sort: list[ContactsSortFilter]


# ===== COMPANIES SEARCH TYPES =====

class CompaniesSearchFilter(TypedDict, total=False):
    """Available fields for filtering companies search queries."""
    id: int | None
    """Unique company ID"""
    name: str | None
    """Name of the company"""
    description: str | None
    """Description of the company"""
    domains: list[Any] | None
    """Email domains associated with the company"""
    note: str | None
    """Notes about the company"""
    health_score: str | None
    """Health score of the company"""
    account_tier: str | None
    """Account tier of the company"""
    renewal_date: str | None
    """Renewal date"""
    industry: str | None
    """Industry of the company"""
    custom_fields: dict[str, Any] | None
    """Custom fields associated with the company"""
    created_at: str | None
    """Company creation timestamp"""
    updated_at: str | None
    """Company last update timestamp"""


class CompaniesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique company ID"""
    name: list[str]
    """Name of the company"""
    description: list[str]
    """Description of the company"""
    domains: list[list[Any]]
    """Email domains associated with the company"""
    note: list[str]
    """Notes about the company"""
    health_score: list[str]
    """Health score of the company"""
    account_tier: list[str]
    """Account tier of the company"""
    renewal_date: list[str]
    """Renewal date"""
    industry: list[str]
    """Industry of the company"""
    custom_fields: list[dict[str, Any]]
    """Custom fields associated with the company"""
    created_at: list[str]
    """Company creation timestamp"""
    updated_at: list[str]
    """Company last update timestamp"""


class CompaniesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique company ID"""
    name: Any
    """Name of the company"""
    description: Any
    """Description of the company"""
    domains: Any
    """Email domains associated with the company"""
    note: Any
    """Notes about the company"""
    health_score: Any
    """Health score of the company"""
    account_tier: Any
    """Account tier of the company"""
    renewal_date: Any
    """Renewal date"""
    industry: Any
    """Industry of the company"""
    custom_fields: Any
    """Custom fields associated with the company"""
    created_at: Any
    """Company creation timestamp"""
    updated_at: Any
    """Company last update timestamp"""


class CompaniesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique company ID"""
    name: str
    """Name of the company"""
    description: str
    """Description of the company"""
    domains: str
    """Email domains associated with the company"""
    note: str
    """Notes about the company"""
    health_score: str
    """Health score of the company"""
    account_tier: str
    """Account tier of the company"""
    renewal_date: str
    """Renewal date"""
    industry: str
    """Industry of the company"""
    custom_fields: str
    """Custom fields associated with the company"""
    created_at: str
    """Company creation timestamp"""
    updated_at: str
    """Company last update timestamp"""


class CompaniesSortFilter(TypedDict, total=False):
    """Available fields for sorting companies search results."""
    id: AirbyteSortOrder
    """Unique company ID"""
    name: AirbyteSortOrder
    """Name of the company"""
    description: AirbyteSortOrder
    """Description of the company"""
    domains: AirbyteSortOrder
    """Email domains associated with the company"""
    note: AirbyteSortOrder
    """Notes about the company"""
    health_score: AirbyteSortOrder
    """Health score of the company"""
    account_tier: AirbyteSortOrder
    """Account tier of the company"""
    renewal_date: AirbyteSortOrder
    """Renewal date"""
    industry: AirbyteSortOrder
    """Industry of the company"""
    custom_fields: AirbyteSortOrder
    """Custom fields associated with the company"""
    created_at: AirbyteSortOrder
    """Company creation timestamp"""
    updated_at: AirbyteSortOrder
    """Company last update timestamp"""


# Entity-specific condition types for companies
class CompaniesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CompaniesSearchFilter


class CompaniesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CompaniesSearchFilter


class CompaniesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CompaniesSearchFilter


class CompaniesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CompaniesSearchFilter


class CompaniesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CompaniesSearchFilter


class CompaniesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CompaniesSearchFilter


class CompaniesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CompaniesStringFilter


class CompaniesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CompaniesStringFilter


class CompaniesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CompaniesStringFilter


class CompaniesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CompaniesStringFilter


class CompaniesContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: CompaniesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CompaniesInCondition = TypedDict("CompaniesInCondition", {"in": CompaniesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CompaniesNotCondition = TypedDict("CompaniesNotCondition", {"not": "CompaniesCondition"}, total=False)
"""Negates the nested condition."""

CompaniesAndCondition = TypedDict("CompaniesAndCondition", {"and": "list[CompaniesCondition]"}, total=False)
"""True if all nested conditions are true."""

CompaniesOrCondition = TypedDict("CompaniesOrCondition", {"or": "list[CompaniesCondition]"}, total=False)
"""True if any nested condition is true."""

CompaniesAnyCondition = TypedDict("CompaniesAnyCondition", {"any": CompaniesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all companies condition types
CompaniesCondition = (
    CompaniesEqCondition
    | CompaniesNeqCondition
    | CompaniesGtCondition
    | CompaniesGteCondition
    | CompaniesLtCondition
    | CompaniesLteCondition
    | CompaniesInCondition
    | CompaniesStartswithCondition
    | CompaniesEndswithCondition
    | CompaniesFuzzyCondition
    | CompaniesKeywordCondition
    | CompaniesContainsCondition
    | CompaniesNotCondition
    | CompaniesAndCondition
    | CompaniesOrCondition
    | CompaniesAnyCondition
)


class CompaniesSearchQuery(TypedDict, total=False):
    """Search query for companies entity."""
    filter: CompaniesCondition
    sort: list[CompaniesSortFilter]


# ===== ROLES SEARCH TYPES =====

class RolesSearchFilter(TypedDict, total=False):
    """Available fields for filtering roles search queries."""
    id: int | None
    """Unique role ID"""
    name: str | None
    """Name of the role"""
    description: str | None
    """Description of the role"""
    default: bool | None
    """Whether this is a default role"""
    created_at: str | None
    """Role creation timestamp"""
    updated_at: str | None
    """Role last update timestamp"""


class RolesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique role ID"""
    name: list[str]
    """Name of the role"""
    description: list[str]
    """Description of the role"""
    default: list[bool]
    """Whether this is a default role"""
    created_at: list[str]
    """Role creation timestamp"""
    updated_at: list[str]
    """Role last update timestamp"""


class RolesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique role ID"""
    name: Any
    """Name of the role"""
    description: Any
    """Description of the role"""
    default: Any
    """Whether this is a default role"""
    created_at: Any
    """Role creation timestamp"""
    updated_at: Any
    """Role last update timestamp"""


class RolesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique role ID"""
    name: str
    """Name of the role"""
    description: str
    """Description of the role"""
    default: str
    """Whether this is a default role"""
    created_at: str
    """Role creation timestamp"""
    updated_at: str
    """Role last update timestamp"""


class RolesSortFilter(TypedDict, total=False):
    """Available fields for sorting roles search results."""
    id: AirbyteSortOrder
    """Unique role ID"""
    name: AirbyteSortOrder
    """Name of the role"""
    description: AirbyteSortOrder
    """Description of the role"""
    default: AirbyteSortOrder
    """Whether this is a default role"""
    created_at: AirbyteSortOrder
    """Role creation timestamp"""
    updated_at: AirbyteSortOrder
    """Role last update timestamp"""


# Entity-specific condition types for roles
class RolesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: RolesSearchFilter


class RolesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: RolesSearchFilter


class RolesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: RolesSearchFilter


class RolesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: RolesSearchFilter


class RolesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: RolesSearchFilter


class RolesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: RolesSearchFilter


class RolesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: RolesStringFilter


class RolesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: RolesStringFilter


class RolesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: RolesStringFilter


class RolesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: RolesStringFilter


class RolesContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: RolesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
RolesInCondition = TypedDict("RolesInCondition", {"in": RolesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

RolesNotCondition = TypedDict("RolesNotCondition", {"not": "RolesCondition"}, total=False)
"""Negates the nested condition."""

RolesAndCondition = TypedDict("RolesAndCondition", {"and": "list[RolesCondition]"}, total=False)
"""True if all nested conditions are true."""

RolesOrCondition = TypedDict("RolesOrCondition", {"or": "list[RolesCondition]"}, total=False)
"""True if any nested condition is true."""

RolesAnyCondition = TypedDict("RolesAnyCondition", {"any": RolesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all roles condition types
RolesCondition = (
    RolesEqCondition
    | RolesNeqCondition
    | RolesGtCondition
    | RolesGteCondition
    | RolesLtCondition
    | RolesLteCondition
    | RolesInCondition
    | RolesStartswithCondition
    | RolesEndswithCondition
    | RolesFuzzyCondition
    | RolesKeywordCondition
    | RolesContainsCondition
    | RolesNotCondition
    | RolesAndCondition
    | RolesOrCondition
    | RolesAnyCondition
)


class RolesSearchQuery(TypedDict, total=False):
    """Search query for roles entity."""
    filter: RolesCondition
    sort: list[RolesSortFilter]


# ===== SATISFACTION_RATINGS SEARCH TYPES =====

class SatisfactionRatingsSearchFilter(TypedDict, total=False):
    """Available fields for filtering satisfaction_ratings search queries."""
    id: int | None
    """Unique satisfaction rating ID"""
    survey_id: int | None
    """ID of the survey"""
    user_id: int | None
    """ID of the user (requester)"""
    agent_id: int | None
    """ID of the agent"""
    group_id: int | None
    """ID of the group"""
    ticket_id: int | None
    """ID of the ticket"""
    feedback: str | None
    """Feedback text"""
    ratings: dict[str, Any] | None
    """Rating values (question_id to rating mapping)"""
    created_at: str | None
    """Rating creation timestamp"""
    updated_at: str | None
    """Rating last update timestamp"""


class SatisfactionRatingsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique satisfaction rating ID"""
    survey_id: list[int]
    """ID of the survey"""
    user_id: list[int]
    """ID of the user (requester)"""
    agent_id: list[int]
    """ID of the agent"""
    group_id: list[int]
    """ID of the group"""
    ticket_id: list[int]
    """ID of the ticket"""
    feedback: list[str]
    """Feedback text"""
    ratings: list[dict[str, Any]]
    """Rating values (question_id to rating mapping)"""
    created_at: list[str]
    """Rating creation timestamp"""
    updated_at: list[str]
    """Rating last update timestamp"""


class SatisfactionRatingsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique satisfaction rating ID"""
    survey_id: Any
    """ID of the survey"""
    user_id: Any
    """ID of the user (requester)"""
    agent_id: Any
    """ID of the agent"""
    group_id: Any
    """ID of the group"""
    ticket_id: Any
    """ID of the ticket"""
    feedback: Any
    """Feedback text"""
    ratings: Any
    """Rating values (question_id to rating mapping)"""
    created_at: Any
    """Rating creation timestamp"""
    updated_at: Any
    """Rating last update timestamp"""


class SatisfactionRatingsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique satisfaction rating ID"""
    survey_id: str
    """ID of the survey"""
    user_id: str
    """ID of the user (requester)"""
    agent_id: str
    """ID of the agent"""
    group_id: str
    """ID of the group"""
    ticket_id: str
    """ID of the ticket"""
    feedback: str
    """Feedback text"""
    ratings: str
    """Rating values (question_id to rating mapping)"""
    created_at: str
    """Rating creation timestamp"""
    updated_at: str
    """Rating last update timestamp"""


class SatisfactionRatingsSortFilter(TypedDict, total=False):
    """Available fields for sorting satisfaction_ratings search results."""
    id: AirbyteSortOrder
    """Unique satisfaction rating ID"""
    survey_id: AirbyteSortOrder
    """ID of the survey"""
    user_id: AirbyteSortOrder
    """ID of the user (requester)"""
    agent_id: AirbyteSortOrder
    """ID of the agent"""
    group_id: AirbyteSortOrder
    """ID of the group"""
    ticket_id: AirbyteSortOrder
    """ID of the ticket"""
    feedback: AirbyteSortOrder
    """Feedback text"""
    ratings: AirbyteSortOrder
    """Rating values (question_id to rating mapping)"""
    created_at: AirbyteSortOrder
    """Rating creation timestamp"""
    updated_at: AirbyteSortOrder
    """Rating last update timestamp"""


# Entity-specific condition types for satisfaction_ratings
class SatisfactionRatingsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SatisfactionRatingsSearchFilter


class SatisfactionRatingsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SatisfactionRatingsSearchFilter


class SatisfactionRatingsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SatisfactionRatingsSearchFilter


class SatisfactionRatingsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SatisfactionRatingsSearchFilter


class SatisfactionRatingsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SatisfactionRatingsSearchFilter


class SatisfactionRatingsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SatisfactionRatingsSearchFilter


class SatisfactionRatingsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: SatisfactionRatingsStringFilter


class SatisfactionRatingsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: SatisfactionRatingsStringFilter


class SatisfactionRatingsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SatisfactionRatingsStringFilter


class SatisfactionRatingsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SatisfactionRatingsStringFilter


class SatisfactionRatingsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: SatisfactionRatingsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SatisfactionRatingsInCondition = TypedDict("SatisfactionRatingsInCondition", {"in": SatisfactionRatingsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SatisfactionRatingsNotCondition = TypedDict("SatisfactionRatingsNotCondition", {"not": "SatisfactionRatingsCondition"}, total=False)
"""Negates the nested condition."""

SatisfactionRatingsAndCondition = TypedDict("SatisfactionRatingsAndCondition", {"and": "list[SatisfactionRatingsCondition]"}, total=False)
"""True if all nested conditions are true."""

SatisfactionRatingsOrCondition = TypedDict("SatisfactionRatingsOrCondition", {"or": "list[SatisfactionRatingsCondition]"}, total=False)
"""True if any nested condition is true."""

SatisfactionRatingsAnyCondition = TypedDict("SatisfactionRatingsAnyCondition", {"any": SatisfactionRatingsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all satisfaction_ratings condition types
SatisfactionRatingsCondition = (
    SatisfactionRatingsEqCondition
    | SatisfactionRatingsNeqCondition
    | SatisfactionRatingsGtCondition
    | SatisfactionRatingsGteCondition
    | SatisfactionRatingsLtCondition
    | SatisfactionRatingsLteCondition
    | SatisfactionRatingsInCondition
    | SatisfactionRatingsStartswithCondition
    | SatisfactionRatingsEndswithCondition
    | SatisfactionRatingsFuzzyCondition
    | SatisfactionRatingsKeywordCondition
    | SatisfactionRatingsContainsCondition
    | SatisfactionRatingsNotCondition
    | SatisfactionRatingsAndCondition
    | SatisfactionRatingsOrCondition
    | SatisfactionRatingsAnyCondition
)


class SatisfactionRatingsSearchQuery(TypedDict, total=False):
    """Search query for satisfaction_ratings entity."""
    filter: SatisfactionRatingsCondition
    sort: list[SatisfactionRatingsSortFilter]


# ===== SURVEYS SEARCH TYPES =====

class SurveysSearchFilter(TypedDict, total=False):
    """Available fields for filtering surveys search queries."""
    id: int | None
    """Unique survey ID"""
    title: str | None
    """Title of the survey"""
    active: bool | None
    """Whether the survey is active"""
    questions: list[Any] | None
    """Survey questions"""
    created_at: str | None
    """Survey creation timestamp"""
    updated_at: str | None
    """Survey last update timestamp"""


class SurveysInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique survey ID"""
    title: list[str]
    """Title of the survey"""
    active: list[bool]
    """Whether the survey is active"""
    questions: list[list[Any]]
    """Survey questions"""
    created_at: list[str]
    """Survey creation timestamp"""
    updated_at: list[str]
    """Survey last update timestamp"""


class SurveysAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique survey ID"""
    title: Any
    """Title of the survey"""
    active: Any
    """Whether the survey is active"""
    questions: Any
    """Survey questions"""
    created_at: Any
    """Survey creation timestamp"""
    updated_at: Any
    """Survey last update timestamp"""


class SurveysStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique survey ID"""
    title: str
    """Title of the survey"""
    active: str
    """Whether the survey is active"""
    questions: str
    """Survey questions"""
    created_at: str
    """Survey creation timestamp"""
    updated_at: str
    """Survey last update timestamp"""


class SurveysSortFilter(TypedDict, total=False):
    """Available fields for sorting surveys search results."""
    id: AirbyteSortOrder
    """Unique survey ID"""
    title: AirbyteSortOrder
    """Title of the survey"""
    active: AirbyteSortOrder
    """Whether the survey is active"""
    questions: AirbyteSortOrder
    """Survey questions"""
    created_at: AirbyteSortOrder
    """Survey creation timestamp"""
    updated_at: AirbyteSortOrder
    """Survey last update timestamp"""


# Entity-specific condition types for surveys
class SurveysEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SurveysSearchFilter


class SurveysNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SurveysSearchFilter


class SurveysGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SurveysSearchFilter


class SurveysGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SurveysSearchFilter


class SurveysLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SurveysSearchFilter


class SurveysLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SurveysSearchFilter


class SurveysStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: SurveysStringFilter


class SurveysEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: SurveysStringFilter


class SurveysFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SurveysStringFilter


class SurveysKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SurveysStringFilter


class SurveysContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: SurveysAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SurveysInCondition = TypedDict("SurveysInCondition", {"in": SurveysInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SurveysNotCondition = TypedDict("SurveysNotCondition", {"not": "SurveysCondition"}, total=False)
"""Negates the nested condition."""

SurveysAndCondition = TypedDict("SurveysAndCondition", {"and": "list[SurveysCondition]"}, total=False)
"""True if all nested conditions are true."""

SurveysOrCondition = TypedDict("SurveysOrCondition", {"or": "list[SurveysCondition]"}, total=False)
"""True if any nested condition is true."""

SurveysAnyCondition = TypedDict("SurveysAnyCondition", {"any": SurveysAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all surveys condition types
SurveysCondition = (
    SurveysEqCondition
    | SurveysNeqCondition
    | SurveysGtCondition
    | SurveysGteCondition
    | SurveysLtCondition
    | SurveysLteCondition
    | SurveysInCondition
    | SurveysStartswithCondition
    | SurveysEndswithCondition
    | SurveysFuzzyCondition
    | SurveysKeywordCondition
    | SurveysContainsCondition
    | SurveysNotCondition
    | SurveysAndCondition
    | SurveysOrCondition
    | SurveysAnyCondition
)


class SurveysSearchQuery(TypedDict, total=False):
    """Search query for surveys entity."""
    filter: SurveysCondition
    sort: list[SurveysSortFilter]


# ===== TIME_ENTRIES SEARCH TYPES =====

class TimeEntriesSearchFilter(TypedDict, total=False):
    """Available fields for filtering time_entries search queries."""
    id: int | None
    """Unique time entry ID"""
    agent_id: int | None
    """ID of the agent"""
    ticket_id: int | None
    """ID of the associated ticket"""
    company_id: int | None
    """ID of the associated company"""
    billable: bool | None
    """Whether the time entry is billable"""
    note: str | None
    """Description of the time entry"""
    time_spent: str | None
    """Time spent in hh:mm format"""
    timer_running: bool | None
    """Whether the timer is running"""
    executed_at: str | None
    """Execution timestamp"""
    start_time: str | None
    """Start time of the timer"""
    created_at: str | None
    """Time entry creation timestamp"""
    updated_at: str | None
    """Time entry last update timestamp"""


class TimeEntriesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique time entry ID"""
    agent_id: list[int]
    """ID of the agent"""
    ticket_id: list[int]
    """ID of the associated ticket"""
    company_id: list[int]
    """ID of the associated company"""
    billable: list[bool]
    """Whether the time entry is billable"""
    note: list[str]
    """Description of the time entry"""
    time_spent: list[str]
    """Time spent in hh:mm format"""
    timer_running: list[bool]
    """Whether the timer is running"""
    executed_at: list[str]
    """Execution timestamp"""
    start_time: list[str]
    """Start time of the timer"""
    created_at: list[str]
    """Time entry creation timestamp"""
    updated_at: list[str]
    """Time entry last update timestamp"""


class TimeEntriesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique time entry ID"""
    agent_id: Any
    """ID of the agent"""
    ticket_id: Any
    """ID of the associated ticket"""
    company_id: Any
    """ID of the associated company"""
    billable: Any
    """Whether the time entry is billable"""
    note: Any
    """Description of the time entry"""
    time_spent: Any
    """Time spent in hh:mm format"""
    timer_running: Any
    """Whether the timer is running"""
    executed_at: Any
    """Execution timestamp"""
    start_time: Any
    """Start time of the timer"""
    created_at: Any
    """Time entry creation timestamp"""
    updated_at: Any
    """Time entry last update timestamp"""


class TimeEntriesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique time entry ID"""
    agent_id: str
    """ID of the agent"""
    ticket_id: str
    """ID of the associated ticket"""
    company_id: str
    """ID of the associated company"""
    billable: str
    """Whether the time entry is billable"""
    note: str
    """Description of the time entry"""
    time_spent: str
    """Time spent in hh:mm format"""
    timer_running: str
    """Whether the timer is running"""
    executed_at: str
    """Execution timestamp"""
    start_time: str
    """Start time of the timer"""
    created_at: str
    """Time entry creation timestamp"""
    updated_at: str
    """Time entry last update timestamp"""


class TimeEntriesSortFilter(TypedDict, total=False):
    """Available fields for sorting time_entries search results."""
    id: AirbyteSortOrder
    """Unique time entry ID"""
    agent_id: AirbyteSortOrder
    """ID of the agent"""
    ticket_id: AirbyteSortOrder
    """ID of the associated ticket"""
    company_id: AirbyteSortOrder
    """ID of the associated company"""
    billable: AirbyteSortOrder
    """Whether the time entry is billable"""
    note: AirbyteSortOrder
    """Description of the time entry"""
    time_spent: AirbyteSortOrder
    """Time spent in hh:mm format"""
    timer_running: AirbyteSortOrder
    """Whether the timer is running"""
    executed_at: AirbyteSortOrder
    """Execution timestamp"""
    start_time: AirbyteSortOrder
    """Start time of the timer"""
    created_at: AirbyteSortOrder
    """Time entry creation timestamp"""
    updated_at: AirbyteSortOrder
    """Time entry last update timestamp"""


# Entity-specific condition types for time_entries
class TimeEntriesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TimeEntriesSearchFilter


class TimeEntriesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TimeEntriesSearchFilter


class TimeEntriesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TimeEntriesSearchFilter


class TimeEntriesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TimeEntriesSearchFilter


class TimeEntriesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TimeEntriesSearchFilter


class TimeEntriesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TimeEntriesSearchFilter


class TimeEntriesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: TimeEntriesStringFilter


class TimeEntriesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: TimeEntriesStringFilter


class TimeEntriesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TimeEntriesStringFilter


class TimeEntriesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TimeEntriesStringFilter


class TimeEntriesContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: TimeEntriesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TimeEntriesInCondition = TypedDict("TimeEntriesInCondition", {"in": TimeEntriesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TimeEntriesNotCondition = TypedDict("TimeEntriesNotCondition", {"not": "TimeEntriesCondition"}, total=False)
"""Negates the nested condition."""

TimeEntriesAndCondition = TypedDict("TimeEntriesAndCondition", {"and": "list[TimeEntriesCondition]"}, total=False)
"""True if all nested conditions are true."""

TimeEntriesOrCondition = TypedDict("TimeEntriesOrCondition", {"or": "list[TimeEntriesCondition]"}, total=False)
"""True if any nested condition is true."""

TimeEntriesAnyCondition = TypedDict("TimeEntriesAnyCondition", {"any": TimeEntriesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all time_entries condition types
TimeEntriesCondition = (
    TimeEntriesEqCondition
    | TimeEntriesNeqCondition
    | TimeEntriesGtCondition
    | TimeEntriesGteCondition
    | TimeEntriesLtCondition
    | TimeEntriesLteCondition
    | TimeEntriesInCondition
    | TimeEntriesStartswithCondition
    | TimeEntriesEndswithCondition
    | TimeEntriesFuzzyCondition
    | TimeEntriesKeywordCondition
    | TimeEntriesContainsCondition
    | TimeEntriesNotCondition
    | TimeEntriesAndCondition
    | TimeEntriesOrCondition
    | TimeEntriesAnyCondition
)


class TimeEntriesSearchQuery(TypedDict, total=False):
    """Search query for time_entries entity."""
    filter: TimeEntriesCondition
    sort: list[TimeEntriesSortFilter]


# ===== TICKET_FIELDS SEARCH TYPES =====

class TicketFieldsSearchFilter(TypedDict, total=False):
    """Available fields for filtering ticket_fields search queries."""
    id: int | None
    """Unique ticket field ID"""
    name: str | None
    """Name of the field"""
    label: str | None
    """Display label for agents"""
    label_for_customers: str | None
    """Display label in the customer portal"""
    description: str | None
    """Description of the field"""
    position: int | None
    """Position of the field in the form"""
    type_: str | None
    """Field type (e.g., custom_dropdown, custom_text)"""
    default: bool | None
    """Whether this is a default (non-custom) field"""
    required_for_closure: bool | None
    """Whether the field is required for ticket closure"""
    required_for_agents: bool | None
    """Whether the field is required for agents"""
    required_for_customers: bool | None
    """Whether the field is required for customers"""
    customers_can_edit: bool | None
    """Whether customers can edit this field"""
    displayed_to_customers: bool | None
    """Whether the field is displayed to customers"""
    portal_cc: bool | None
    """Whether CC is enabled in the portal"""
    portal_cc_to: str | None
    """CC recipients scope (all or company)"""
    choices: dict[str, Any] | None
    """Available choices for dropdown fields"""
    created_at: str | None
    """Field creation timestamp"""
    updated_at: str | None
    """Field last update timestamp"""


class TicketFieldsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique ticket field ID"""
    name: list[str]
    """Name of the field"""
    label: list[str]
    """Display label for agents"""
    label_for_customers: list[str]
    """Display label in the customer portal"""
    description: list[str]
    """Description of the field"""
    position: list[int]
    """Position of the field in the form"""
    type_: list[str]
    """Field type (e.g., custom_dropdown, custom_text)"""
    default: list[bool]
    """Whether this is a default (non-custom) field"""
    required_for_closure: list[bool]
    """Whether the field is required for ticket closure"""
    required_for_agents: list[bool]
    """Whether the field is required for agents"""
    required_for_customers: list[bool]
    """Whether the field is required for customers"""
    customers_can_edit: list[bool]
    """Whether customers can edit this field"""
    displayed_to_customers: list[bool]
    """Whether the field is displayed to customers"""
    portal_cc: list[bool]
    """Whether CC is enabled in the portal"""
    portal_cc_to: list[str]
    """CC recipients scope (all or company)"""
    choices: list[dict[str, Any]]
    """Available choices for dropdown fields"""
    created_at: list[str]
    """Field creation timestamp"""
    updated_at: list[str]
    """Field last update timestamp"""


class TicketFieldsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique ticket field ID"""
    name: Any
    """Name of the field"""
    label: Any
    """Display label for agents"""
    label_for_customers: Any
    """Display label in the customer portal"""
    description: Any
    """Description of the field"""
    position: Any
    """Position of the field in the form"""
    type_: Any
    """Field type (e.g., custom_dropdown, custom_text)"""
    default: Any
    """Whether this is a default (non-custom) field"""
    required_for_closure: Any
    """Whether the field is required for ticket closure"""
    required_for_agents: Any
    """Whether the field is required for agents"""
    required_for_customers: Any
    """Whether the field is required for customers"""
    customers_can_edit: Any
    """Whether customers can edit this field"""
    displayed_to_customers: Any
    """Whether the field is displayed to customers"""
    portal_cc: Any
    """Whether CC is enabled in the portal"""
    portal_cc_to: Any
    """CC recipients scope (all or company)"""
    choices: Any
    """Available choices for dropdown fields"""
    created_at: Any
    """Field creation timestamp"""
    updated_at: Any
    """Field last update timestamp"""


class TicketFieldsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique ticket field ID"""
    name: str
    """Name of the field"""
    label: str
    """Display label for agents"""
    label_for_customers: str
    """Display label in the customer portal"""
    description: str
    """Description of the field"""
    position: str
    """Position of the field in the form"""
    type_: str
    """Field type (e.g., custom_dropdown, custom_text)"""
    default: str
    """Whether this is a default (non-custom) field"""
    required_for_closure: str
    """Whether the field is required for ticket closure"""
    required_for_agents: str
    """Whether the field is required for agents"""
    required_for_customers: str
    """Whether the field is required for customers"""
    customers_can_edit: str
    """Whether customers can edit this field"""
    displayed_to_customers: str
    """Whether the field is displayed to customers"""
    portal_cc: str
    """Whether CC is enabled in the portal"""
    portal_cc_to: str
    """CC recipients scope (all or company)"""
    choices: str
    """Available choices for dropdown fields"""
    created_at: str
    """Field creation timestamp"""
    updated_at: str
    """Field last update timestamp"""


class TicketFieldsSortFilter(TypedDict, total=False):
    """Available fields for sorting ticket_fields search results."""
    id: AirbyteSortOrder
    """Unique ticket field ID"""
    name: AirbyteSortOrder
    """Name of the field"""
    label: AirbyteSortOrder
    """Display label for agents"""
    label_for_customers: AirbyteSortOrder
    """Display label in the customer portal"""
    description: AirbyteSortOrder
    """Description of the field"""
    position: AirbyteSortOrder
    """Position of the field in the form"""
    type_: AirbyteSortOrder
    """Field type (e.g., custom_dropdown, custom_text)"""
    default: AirbyteSortOrder
    """Whether this is a default (non-custom) field"""
    required_for_closure: AirbyteSortOrder
    """Whether the field is required for ticket closure"""
    required_for_agents: AirbyteSortOrder
    """Whether the field is required for agents"""
    required_for_customers: AirbyteSortOrder
    """Whether the field is required for customers"""
    customers_can_edit: AirbyteSortOrder
    """Whether customers can edit this field"""
    displayed_to_customers: AirbyteSortOrder
    """Whether the field is displayed to customers"""
    portal_cc: AirbyteSortOrder
    """Whether CC is enabled in the portal"""
    portal_cc_to: AirbyteSortOrder
    """CC recipients scope (all or company)"""
    choices: AirbyteSortOrder
    """Available choices for dropdown fields"""
    created_at: AirbyteSortOrder
    """Field creation timestamp"""
    updated_at: AirbyteSortOrder
    """Field last update timestamp"""


# Entity-specific condition types for ticket_fields
class TicketFieldsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TicketFieldsSearchFilter


class TicketFieldsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TicketFieldsSearchFilter


class TicketFieldsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TicketFieldsSearchFilter


class TicketFieldsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TicketFieldsSearchFilter


class TicketFieldsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TicketFieldsSearchFilter


class TicketFieldsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TicketFieldsSearchFilter


class TicketFieldsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: TicketFieldsStringFilter


class TicketFieldsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: TicketFieldsStringFilter


class TicketFieldsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TicketFieldsStringFilter


class TicketFieldsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TicketFieldsStringFilter


class TicketFieldsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: TicketFieldsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TicketFieldsInCondition = TypedDict("TicketFieldsInCondition", {"in": TicketFieldsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TicketFieldsNotCondition = TypedDict("TicketFieldsNotCondition", {"not": "TicketFieldsCondition"}, total=False)
"""Negates the nested condition."""

TicketFieldsAndCondition = TypedDict("TicketFieldsAndCondition", {"and": "list[TicketFieldsCondition]"}, total=False)
"""True if all nested conditions are true."""

TicketFieldsOrCondition = TypedDict("TicketFieldsOrCondition", {"or": "list[TicketFieldsCondition]"}, total=False)
"""True if any nested condition is true."""

TicketFieldsAnyCondition = TypedDict("TicketFieldsAnyCondition", {"any": TicketFieldsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all ticket_fields condition types
TicketFieldsCondition = (
    TicketFieldsEqCondition
    | TicketFieldsNeqCondition
    | TicketFieldsGtCondition
    | TicketFieldsGteCondition
    | TicketFieldsLtCondition
    | TicketFieldsLteCondition
    | TicketFieldsInCondition
    | TicketFieldsStartswithCondition
    | TicketFieldsEndswithCondition
    | TicketFieldsFuzzyCondition
    | TicketFieldsKeywordCondition
    | TicketFieldsContainsCondition
    | TicketFieldsNotCondition
    | TicketFieldsAndCondition
    | TicketFieldsOrCondition
    | TicketFieldsAnyCondition
)


class TicketFieldsSearchQuery(TypedDict, total=False):
    """Search query for ticket_fields entity."""
    filter: TicketFieldsCondition
    sort: list[TicketFieldsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
