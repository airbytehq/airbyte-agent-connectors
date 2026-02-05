"""
Pydantic models for zendesk-chat connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

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

    account_key: Union[str, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    create_date: Union[str | None, Any] = Field(default=None)
    billing: Union[Any, Any] = Field(default=None)
    plan: Union[Any, Any] = Field(default=None)

class Billing(BaseModel):
    """Account billing information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    company: Union[str | None, Any] = Field(default=None)
    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    address1: Union[str | None, Any] = Field(default=None)
    address2: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    postal_code: Union[str | None, Any] = Field(default=None)
    country_code: Union[str | None, Any] = Field(default=None)
    additional_info: Union[str | None, Any] = Field(default=None)
    cycle: Union[int | None, Any] = Field(default=None)

class Plan(BaseModel):
    """Account plan details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str | None, Any] = Field(default=None)
    price: Union[float | None, Any] = Field(default=None)
    max_agents: Union[int | None, Any] = Field(default=None)
    max_departments: Union[str | None, Any] = Field(default=None)
    max_concurrent_chats: Union[str | None, Any] = Field(default=None)
    max_history_search_days: Union[str | None, Any] = Field(default=None)
    max_advanced_triggers: Union[str | None, Any] = Field(default=None)
    max_basic_triggers: Union[str | None, Any] = Field(default=None)
    analytics: Union[bool | None, Any] = Field(default=None)
    file_upload: Union[bool | None, Any] = Field(default=None)
    rest_api: Union[bool | None, Any] = Field(default=None)
    goals: Union[int | None, Any] = Field(default=None)
    high_load: Union[bool | None, Any] = Field(default=None)
    integrations: Union[bool | None, Any] = Field(default=None)
    ip_restriction: Union[bool | None, Any] = Field(default=None)
    monitoring: Union[bool | None, Any] = Field(default=None)
    operating_hours: Union[bool | None, Any] = Field(default=None)
    sla: Union[bool | None, Any] = Field(default=None)
    support: Union[bool | None, Any] = Field(default=None)
    unbranding: Union[bool | None, Any] = Field(default=None)
    agent_leaderboard: Union[bool | None, Any] = Field(default=None)
    agent_reports: Union[bool | None, Any] = Field(default=None)
    chat_reports: Union[bool | None, Any] = Field(default=None)
    daily_reports: Union[bool | None, Any] = Field(default=None)
    email_reports: Union[bool | None, Any] = Field(default=None)
    widget_customization: Union[str | None, Any] = Field(default=None)
    long_desc: Union[str | None, Any] = Field(default=None)
    short_desc: Union[str | None, Any] = Field(default=None)

class Agent(BaseModel):
    """Zendesk Chat agent"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    display_name: Union[str | None, Any] = Field(default=None)
    first_name: Union[str | None, Any] = Field(default=None)
    last_name: Union[str | None, Any] = Field(default=None)
    enabled: Union[bool | None, Any] = Field(default=None)
    role_id: Union[int | None, Any] = Field(default=None)
    roles: Union[Any, Any] = Field(default=None)
    departments: Union[list[int] | None, Any] = Field(default=None)
    enabled_departments: Union[list[int] | None, Any] = Field(default=None)
    skills: Union[list[int] | None, Any] = Field(default=None)
    scope: Union[str | None, Any] = Field(default=None)
    create_date: Union[str | None, Any] = Field(default=None)
    last_login: Union[str | None, Any] = Field(default=None)
    login_count: Union[int | None, Any] = Field(default=None)

class AgentRoles(BaseModel):
    """Agent role flags"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    administrator: Union[bool | None, Any] = Field(default=None)
    owner: Union[bool | None, Any] = Field(default=None)

class AgentTimeline(BaseModel):
    """Agent activity timeline entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    agent_id: Union[int, Any] = Field(default=None)
    start_time: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    duration: Union[float | None, Any] = Field(default=None)
    engagement_count: Union[int | None, Any] = Field(default=None)

class Ban(BaseModel):
    """Banned visitor"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    ip_address: Union[str | None, Any] = Field(default=None)
    visitor_id: Union[str | None, Any] = Field(default=None)
    visitor_name: Union[str | None, Any] = Field(default=None)
    reason: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)

class ChatHistoryItem(BaseModel):
    """ChatHistoryItem type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    timestamp: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    nick: Union[str | None, Any] = Field(default=None)
    msg: Union[str | None, Any] = Field(default=None)
    msg_id: Union[str | None, Any] = Field(default=None)
    channel: Union[str | None, Any] = Field(default=None)
    department_id: Union[int | None, Any] = Field(default=None)
    department_name: Union[str | None, Any] = Field(default=None)
    rating: Union[str | None, Any] = Field(default=None)
    new_rating: Union[str | None, Any] = Field(default=None)
    tags: Union[list[str] | None, Any] = Field(default=None)
    new_tags: Union[list[str] | None, Any] = Field(default=None)
    options: Union[str | None, Any] = Field(default=None)

class WebpathItem(BaseModel):
    """WebpathItem type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    from_: Union[str | None, Any] = Field(default=None, alias="from")
    timestamp: Union[str | None, Any] = Field(default=None)

class ChatConversion(BaseModel):
    """ChatConversion type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    goal_id: Union[int | None, Any] = Field(default=None)
    goal_name: Union[str | None, Any] = Field(default=None)
    timestamp: Union[str | None, Any] = Field(default=None)
    attribution: Union[Any, Any] = Field(default=None)

class ChatEngagement(BaseModel):
    """ChatEngagement type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    agent_id: Union[str | None, Any] = Field(default=None)
    agent_name: Union[str | None, Any] = Field(default=None)
    agent_full_name: Union[str | None, Any] = Field(default=None)
    department_id: Union[int | None, Any] = Field(default=None)
    timestamp: Union[str | None, Any] = Field(default=None)
    duration: Union[float | None, Any] = Field(default=None)
    accepted: Union[bool | None, Any] = Field(default=None)
    assigned: Union[bool | None, Any] = Field(default=None)
    started_by: Union[str | None, Any] = Field(default=None)
    rating: Union[str | None, Any] = Field(default=None)
    comment: Union[str | None, Any] = Field(default=None)
    count: Union[Any, Any] = Field(default=None)
    response_time: Union[Any, Any] = Field(default=None)
    skills_requested: Union[list[int] | None, Any] = Field(default=None)
    skills_fulfilled: Union[bool | None, Any] = Field(default=None)

class Chat(BaseModel):
    """Chat conversation transcript"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    timestamp: Union[str | None, Any] = Field(default=None)
    update_timestamp: Union[str | None, Any] = Field(default=None)
    duration: Union[int | None, Any] = Field(default=None)
    department_id: Union[int | None, Any] = Field(default=None)
    department_name: Union[str | None, Any] = Field(default=None)
    agent_ids: Union[list[str] | None, Any] = Field(default=None)
    agent_names: Union[list[str] | None, Any] = Field(default=None)
    visitor: Union[Any, Any] = Field(default=None)
    session: Union[Any, Any] = Field(default=None)
    history: Union[list[ChatHistoryItem] | None, Any] = Field(default=None)
    engagements: Union[list[ChatEngagement] | None, Any] = Field(default=None)
    conversions: Union[list[ChatConversion] | None, Any] = Field(default=None)
    count: Union[Any, Any] = Field(default=None)
    response_time: Union[Any, Any] = Field(default=None)
    rating: Union[str | None, Any] = Field(default=None)
    comment: Union[str | None, Any] = Field(default=None)
    tags: Union[list[str] | None, Any] = Field(default=None)
    started_by: Union[str | None, Any] = Field(default=None)
    triggered: Union[bool | None, Any] = Field(default=None)
    triggered_response: Union[bool | None, Any] = Field(default=None)
    missed: Union[bool | None, Any] = Field(default=None)
    unread: Union[bool | None, Any] = Field(default=None)
    deleted: Union[bool | None, Any] = Field(default=None)
    message: Union[str | None, Any] = Field(default=None)
    webpath: Union[list[WebpathItem] | None, Any] = Field(default=None)
    zendesk_ticket_id: Union[int | None, Any] = Field(default=None)

class Visitor(BaseModel):
    """Visitor type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    phone: Union[str | None, Any] = Field(default=None)
    notes: Union[str | None, Any] = Field(default=None)

class ChatSession(BaseModel):
    """ChatSession type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    browser: Union[str | None, Any] = Field(default=None)
    platform: Union[str | None, Any] = Field(default=None)
    user_agent: Union[str | None, Any] = Field(default=None)
    ip: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    region: Union[str | None, Any] = Field(default=None)
    country_code: Union[str | None, Any] = Field(default=None)
    country_name: Union[str | None, Any] = Field(default=None)
    start_date: Union[str | None, Any] = Field(default=None)
    end_date: Union[str | None, Any] = Field(default=None)

class ConversionAttribution(BaseModel):
    """ConversionAttribution type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    agent_id: Union[int | None, Any] = Field(default=None)
    agent_name: Union[str | None, Any] = Field(default=None)
    department_id: Union[int | None, Any] = Field(default=None)
    department_name: Union[str | None, Any] = Field(default=None)
    chat_timestamp: Union[str | None, Any] = Field(default=None)

class MessageCount(BaseModel):
    """MessageCount type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: Union[int | None, Any] = Field(default=None)
    agent: Union[int | None, Any] = Field(default=None)
    visitor: Union[int | None, Any] = Field(default=None)

class ResponseTime(BaseModel):
    """ResponseTime type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first: Union[int | None, Any] = Field(default=None)
    avg: Union[float | None, Any] = Field(default=None)
    max: Union[int | None, Any] = Field(default=None)

class Department(BaseModel):
    """Department type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    enabled: Union[bool | None, Any] = Field(default=None)
    members: Union[list[int] | None, Any] = Field(default=None)
    settings: Union[Any, Any] = Field(default=None)

class DepartmentSettings(BaseModel):
    """DepartmentSettings type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    chat_limit: Union[int | None, Any] = Field(default=None)

class Goal(BaseModel):
    """Goal type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    enabled: Union[bool | None, Any] = Field(default=None)
    attribution_model: Union[str | None, Any] = Field(default=None)
    attribution_window: Union[int | None, Any] = Field(default=None)
    attribution_period: Union[int | None, Any] = Field(default=None)
    settings: Union[dict[str, Any] | None, Any] = Field(default=None)

class Role(BaseModel):
    """Role type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    enabled: Union[bool | None, Any] = Field(default=None)
    permissions: Union[dict[str, Any] | None, Any] = Field(default=None)
    members_count: Union[int | None, Any] = Field(default=None)

class RoutingSettings(BaseModel):
    """RoutingSettings type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    routing_mode: Union[str | None, Any] = Field(default=None)
    chat_limit: Union[dict[str, Any] | None, Any] = Field(default=None)
    skill_routing: Union[dict[str, Any] | None, Any] = Field(default=None)
    reassignment: Union[dict[str, Any] | None, Any] = Field(default=None)
    auto_idle: Union[dict[str, Any] | None, Any] = Field(default=None)
    auto_accept: Union[dict[str, Any] | None, Any] = Field(default=None)

class Shortcut(BaseModel):
    """Shortcut type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    message: Union[str | None, Any] = Field(default=None)
    options: Union[str | None, Any] = Field(default=None)
    tags: Union[list[str] | None, Any] = Field(default=None)
    departments: Union[list[int] | None, Any] = Field(default=None)
    agents: Union[list[int] | None, Any] = Field(default=None)
    scope: Union[str | None, Any] = Field(default=None)

class Skill(BaseModel):
    """Skill type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    enabled: Union[bool | None, Any] = Field(default=None)
    members: Union[list[int] | None, Any] = Field(default=None)

class Trigger(BaseModel):
    """Trigger type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    enabled: Union[bool | None, Any] = Field(default=None)
    run_once: Union[bool | None, Any] = Field(default=None)
    conditions: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    actions: Union[list[dict[str, Any]] | None, Any] = Field(default=None)
    departments: Union[list[int] | None, Any] = Field(default=None)
    definition: Union[dict[str, Any] | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class AgentTimelineListResultMeta(BaseModel):
    """Metadata for agent_timeline.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

class ChatsListResultMeta(BaseModel):
    """Metadata for chats.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)

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

