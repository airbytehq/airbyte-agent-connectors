"""
Pydantic models for zendesk-chat connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class ZendeskChatAuthConfig(BaseModel):
    """OAuth 2.0 Access Token - Authenticate using an OAuth 2.0 access token from Zendesk"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """Your Zendesk Chat OAuth 2.0 access token"""

# Replication configuration

class ZendeskChatReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Zendesk Chat."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """The date from which to start replicating data, in the format YYYY-MM-DDT00:00:00Z."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Account(BaseModel):
    """Zendesk Chat account information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_key: str
    status: str | None = Field(default=None)
    create_date: str | None = Field(default=None)
    billing: Any | None = Field(default=None)
    plan: Any | None = Field(default=None)

class Billing(BaseModel):
    """Account billing information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    company: str | None = Field(default=None)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    address1: str | None = Field(default=None)
    address2: str | None = Field(default=None)
    city: str | None = Field(default=None)
    state: str | None = Field(default=None)
    postal_code: str | None = Field(default=None)
    country_code: str | None = Field(default=None)
    additional_info: str | None = Field(default=None)
    cycle: int | None = Field(default=None)

class Plan(BaseModel):
    """Account plan details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    price: float | None = Field(default=None)
    max_agents: int | None = Field(default=None)
    max_departments: str | None = Field(default=None)
    max_concurrent_chats: str | None = Field(default=None)
    max_history_search_days: str | None = Field(default=None)
    max_advanced_triggers: str | None = Field(default=None)
    max_basic_triggers: str | None = Field(default=None)
    analytics: bool | None = Field(default=None)
    file_upload: bool | None = Field(default=None)
    rest_api: bool | None = Field(default=None)
    goals: int | None = Field(default=None)
    high_load: bool | None = Field(default=None)
    integrations: bool | None = Field(default=None)
    ip_restriction: bool | None = Field(default=None)
    monitoring: bool | None = Field(default=None)
    operating_hours: bool | None = Field(default=None)
    sla: bool | None = Field(default=None)
    support: bool | None = Field(default=None)
    unbranding: bool | None = Field(default=None)
    agent_leaderboard: bool | None = Field(default=None)
    agent_reports: bool | None = Field(default=None)
    chat_reports: bool | None = Field(default=None)
    daily_reports: bool | None = Field(default=None)
    email_reports: bool | None = Field(default=None)
    widget_customization: str | None = Field(default=None)
    long_desc: str | None = Field(default=None)
    short_desc: str | None = Field(default=None)

class Agent(BaseModel):
    """Zendesk Chat agent"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    email: str | None = Field(default=None)
    display_name: str | None = Field(default=None)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    enabled: bool | None = Field(default=None)
    role_id: int | None = Field(default=None)
    roles: Any | None = Field(default=None)
    departments: list[int] | None = Field(default=None)
    enabled_departments: list[int] | None = Field(default=None)
    skills: list[int] | None = Field(default=None)
    scope: str | None = Field(default=None)
    create_date: str | None = Field(default=None)
    last_login: str | None = Field(default=None)
    login_count: int | None = Field(default=None)

class AgentRoles(BaseModel):
    """Agent role flags"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    administrator: bool | None = Field(default=None)
    owner: bool | None = Field(default=None)

class AgentTimeline(BaseModel):
    """Agent activity timeline entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    agent_id: int
    start_time: str | None = Field(default=None)
    status: str | None = Field(default=None)
    duration: float | None = Field(default=None)
    engagement_count: int | None = Field(default=None)

class Ban(BaseModel):
    """Banned visitor"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    type_: str | None = Field(default=None, alias="type")
    ip_address: str | None = Field(default=None)
    visitor_id: str | None = Field(default=None)
    visitor_name: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    created_at: str | None = Field(default=None)

class ChatHistoryItem(BaseModel):
    """ChatHistoryItem type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    timestamp: str | None = Field(default=None)
    name: str | None = Field(default=None)
    nick: str | None = Field(default=None)
    msg: str | None = Field(default=None)
    msg_id: str | None = Field(default=None)
    channel: str | None = Field(default=None)
    department_id: int | None = Field(default=None)
    department_name: str | None = Field(default=None)
    rating: str | None = Field(default=None)
    new_rating: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    new_tags: list[str] | None = Field(default=None)
    options: str | None = Field(default=None)

class ChatConversion(BaseModel):
    """ChatConversion type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    goal_id: int | None = Field(default=None)
    goal_name: str | None = Field(default=None)
    timestamp: str | None = Field(default=None)
    attribution: Any | None = Field(default=None)

class WebpathItem(BaseModel):
    """WebpathItem type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: str | None = Field(default=None, alias="from")
    timestamp: str | None = Field(default=None)

class ChatEngagement(BaseModel):
    """ChatEngagement type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    agent_id: str | None = Field(default=None)
    agent_name: str | None = Field(default=None)
    agent_full_name: str | None = Field(default=None)
    department_id: int | None = Field(default=None)
    timestamp: str | None = Field(default=None)
    duration: float | None = Field(default=None)
    accepted: bool | None = Field(default=None)
    assigned: bool | None = Field(default=None)
    started_by: str | None = Field(default=None)
    rating: str | None = Field(default=None)
    comment: str | None = Field(default=None)
    count: Any | None = Field(default=None)
    response_time: Any | None = Field(default=None)
    skills_requested: list[int] | None = Field(default=None)
    skills_fulfilled: bool | None = Field(default=None)

class Chat(BaseModel):
    """Chat conversation transcript"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    type_: str | None = Field(default=None, alias="type")
    timestamp: str | None = Field(default=None)
    update_timestamp: str | None = Field(default=None)
    duration: int | None = Field(default=None)
    department_id: int | None = Field(default=None)
    department_name: str | None = Field(default=None)
    agent_ids: list[str] | None = Field(default=None)
    agent_names: list[str] | None = Field(default=None)
    visitor: Any | None = Field(default=None)
    session: Any | None = Field(default=None)
    history: list[ChatHistoryItem] | None = Field(default=None)
    engagements: list[ChatEngagement] | None = Field(default=None)
    conversions: list[ChatConversion] | None = Field(default=None)
    count: Any | None = Field(default=None)
    response_time: Any | None = Field(default=None)
    rating: str | None = Field(default=None)
    comment: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    started_by: str | None = Field(default=None)
    triggered: bool | None = Field(default=None)
    triggered_response: bool | None = Field(default=None)
    missed: bool | None = Field(default=None)
    unread: bool | None = Field(default=None)
    deleted: bool | None = Field(default=None)
    message: str | None = Field(default=None)
    webpath: list[WebpathItem] | None = Field(default=None)
    zendesk_ticket_id: int | None = Field(default=None)

class Visitor(BaseModel):
    """Visitor type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    phone: str | None = Field(default=None)
    notes: str | None = Field(default=None)

class ChatSession(BaseModel):
    """ChatSession type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    browser: str | None = Field(default=None)
    platform: str | None = Field(default=None)
    user_agent: str | None = Field(default=None)
    ip: str | None = Field(default=None)
    city: str | None = Field(default=None)
    region: str | None = Field(default=None)
    country_code: str | None = Field(default=None)
    country_name: str | None = Field(default=None)
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)

class ConversionAttribution(BaseModel):
    """ConversionAttribution type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    agent_id: int | None = Field(default=None)
    agent_name: str | None = Field(default=None)
    department_id: int | None = Field(default=None)
    department_name: str | None = Field(default=None)
    chat_timestamp: str | None = Field(default=None)

class MessageCount(BaseModel):
    """MessageCount type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: int | None = Field(default=None)
    agent: int | None = Field(default=None)
    visitor: int | None = Field(default=None)

class ResponseTime(BaseModel):
    """ResponseTime type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first: int | None = Field(default=None)
    avg: float | None = Field(default=None)
    max: int | None = Field(default=None)

class Department(BaseModel):
    """Department type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    enabled: bool | None = Field(default=None)
    members: list[int] | None = Field(default=None)
    settings: Any | None = Field(default=None)

class DepartmentSettings(BaseModel):
    """DepartmentSettings type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    chat_limit: int | None = Field(default=None)

class Goal(BaseModel):
    """Goal type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    enabled: bool | None = Field(default=None)
    attribution_model: str | None = Field(default=None)
    attribution_window: int | None = Field(default=None)
    attribution_period: int | None = Field(default=None)
    settings: dict[str, Any] | None = Field(default=None)

class Role(BaseModel):
    """Role type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    enabled: bool | None = Field(default=None)
    permissions: dict[str, Any] | None = Field(default=None)
    members_count: int | None = Field(default=None)

class RoutingSettings(BaseModel):
    """RoutingSettings type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    routing_mode: str | None = Field(default=None)
    chat_limit: dict[str, Any] | None = Field(default=None)
    skill_routing: dict[str, Any] | None = Field(default=None)
    reassignment: dict[str, Any] | None = Field(default=None)
    auto_idle: dict[str, Any] | None = Field(default=None)
    auto_accept: dict[str, Any] | None = Field(default=None)

class Shortcut(BaseModel):
    """Shortcut type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    name: str | None = Field(default=None)
    message: str | None = Field(default=None)
    options: str | None = Field(default=None)
    tags: list[str] | None = Field(default=None)
    departments: list[int] | None = Field(default=None)
    agents: list[int] | None = Field(default=None)
    scope: str | None = Field(default=None)

class Skill(BaseModel):
    """Skill type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    enabled: bool | None = Field(default=None)
    members: list[int] | None = Field(default=None)

class Trigger(BaseModel):
    """Trigger type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    enabled: bool | None = Field(default=None)
    run_once: bool | None = Field(default=None)
    conditions: list[dict[str, Any]] | None = Field(default=None)
    actions: list[dict[str, Any]] | None = Field(default=None)
    departments: list[int] | None = Field(default=None)
    definition: dict[str, Any] | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class AgentTimelineListResultMeta(BaseModel):
    """Metadata for agent_timeline.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: str | None = Field(default=None)
    count: int | None = Field(default=None)

class ChatsListResultMeta(BaseModel):
    """Metadata for chats.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: str | None = Field(default=None)
    count: int | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class ZendeskChatCheckResult(BaseModel):
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


class ZendeskChatExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class ZendeskChatExecuteResultWithMeta(ZendeskChatExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AgentsSearchData(BaseModel):
    """Search result data for agents entity."""
    model_config = ConfigDict(extra="allow")

    id: int = None
    """Unique agent identifier"""
    email: str | None = None
    """Agent email address"""
    display_name: str | None = None
    """Agent display name"""
    first_name: str | None = None
    """Agent first name"""
    last_name: str | None = None
    """Agent last name"""
    enabled: bool | None = None
    """Whether agent is enabled"""
    role_id: int | None = None
    """Agent role ID"""
    departments: list[Any] | None = None
    """Department IDs agent belongs to"""
    create_date: str | None = None
    """When agent was created"""


class ChatsSearchData(BaseModel):
    """Search result data for chats entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique chat identifier"""
    timestamp: str | None = None
    """Chat start timestamp"""
    update_timestamp: str | None = None
    """Last update timestamp"""
    department_id: int | None = None
    """Department ID"""
    department_name: str | None = None
    """Department name"""
    duration: int | None = None
    """Chat duration in seconds"""
    rating: str | None = None
    """Satisfaction rating"""
    missed: bool | None = None
    """Whether chat was missed"""
    agent_ids: list[Any] | None = None
    """IDs of agents in chat"""


class DepartmentsSearchData(BaseModel):
    """Search result data for departments entity."""
    model_config = ConfigDict(extra="allow")

    id: int = None
    """Department ID"""
    name: str | None = None
    """Department name"""
    enabled: bool | None = None
    """Whether department is enabled"""
    members: list[Any] | None = None
    """Agent IDs in department"""


class ShortcutsSearchData(BaseModel):
    """Search result data for shortcuts entity."""
    model_config = ConfigDict(extra="allow")

    id: int = None
    """Shortcut ID"""
    name: str | None = None
    """Shortcut name/trigger"""
    message: str | None = None
    """Shortcut message content"""
    tags: list[Any] | None = None
    """Tags applied when shortcut is used"""


class TriggersSearchData(BaseModel):
    """Search result data for triggers entity."""
    model_config = ConfigDict(extra="allow")

    id: int = None
    """Trigger ID"""
    name: str | None = None
    """Trigger name"""
    enabled: bool | None = None
    """Whether trigger is enabled"""


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

AgentsSearchResult = AirbyteSearchResult[AgentsSearchData]
"""Search result type for agents entity."""

ChatsSearchResult = AirbyteSearchResult[ChatsSearchData]
"""Search result type for chats entity."""

DepartmentsSearchResult = AirbyteSearchResult[DepartmentsSearchData]
"""Search result type for departments entity."""

ShortcutsSearchResult = AirbyteSearchResult[ShortcutsSearchData]
"""Search result type for shortcuts entity."""

TriggersSearchResult = AirbyteSearchResult[TriggersSearchData]
"""Search result type for triggers entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

AgentsListResult = ZendeskChatExecuteResult[list[Agent]]
"""Result type for agents.list operation."""

AgentTimelineListResult = ZendeskChatExecuteResultWithMeta[list[AgentTimeline], AgentTimelineListResultMeta]
"""Result type for agent_timeline.list operation with data and metadata."""

BansListResult = ZendeskChatExecuteResult[dict[str, Any]]
"""Result type for bans.list operation."""

ChatsListResult = ZendeskChatExecuteResultWithMeta[list[Chat], ChatsListResultMeta]
"""Result type for chats.list operation with data and metadata."""

DepartmentsListResult = ZendeskChatExecuteResult[list[Department]]
"""Result type for departments.list operation."""

GoalsListResult = ZendeskChatExecuteResult[list[Goal]]
"""Result type for goals.list operation."""

RolesListResult = ZendeskChatExecuteResult[list[Role]]
"""Result type for roles.list operation."""

ShortcutsListResult = ZendeskChatExecuteResult[list[Shortcut]]
"""Result type for shortcuts.list operation."""

SkillsListResult = ZendeskChatExecuteResult[list[Skill]]
"""Result type for skills.list operation."""

TriggersListResult = ZendeskChatExecuteResult[list[Trigger]]
"""Result type for triggers.list operation."""

