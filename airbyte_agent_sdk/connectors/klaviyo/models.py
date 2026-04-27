"""
Pydantic models for klaviyo connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class KlaviyoAuthConfig(BaseModel):
    """Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Klaviyo private API key"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class ProfileAttributesLocation(BaseModel):
    """Location information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address1: str | None | None = Field(default=None)
    address2: str | None | None = Field(default=None)
    city: str | None | None = Field(default=None)
    country: str | None | None = Field(default=None)
    region: str | None | None = Field(default=None)
    zip: str | None | None = Field(default=None)
    timezone: str | None | None = Field(default=None)
    latitude: float | None | None = Field(default=None)
    longitude: float | None | None = Field(default=None)

class ProfileAttributes(BaseModel):
    """Profile attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None | None = Field(default=None, description="Email address")
    """Email address"""
    phone_number: str | None | None = Field(default=None, description="Phone number")
    """Phone number"""
    external_id: str | None | None = Field(default=None, description="External identifier")
    """External identifier"""
    first_name: str | None | None = Field(default=None, description="First name")
    """First name"""
    last_name: str | None | None = Field(default=None, description="Last name")
    """Last name"""
    organization: str | None | None = Field(default=None, description="Organization name")
    """Organization name"""
    title: str | None | None = Field(default=None, description="Job title")
    """Job title"""
    image: str | None | None = Field(default=None, description="Profile image URL")
    """Profile image URL"""
    created: str | None | None = Field(default=None, description="Creation timestamp")
    """Creation timestamp"""
    updated: str | None | None = Field(default=None, description="Last update timestamp")
    """Last update timestamp"""
    location: ProfileAttributesLocation | None | None = Field(default=None, description="Location information")
    """Location information"""
    properties: dict[str, Any] | None | None = Field(default=None, description="Custom properties")
    """Custom properties"""

class ProfileLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)

class Profile(BaseModel):
    """A Klaviyo profile representing a contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    type_: str | None = Field(default=None, alias="type")
    attributes: ProfileAttributes | None = Field(default=None)
    links: ProfileLinks | None = Field(default=None)

class ProfilesListLinks(BaseModel):
    """Nested schema for ProfilesList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)
    next: str | None | None = Field(default=None)
    prev: str | None | None = Field(default=None)

class ProfilesList(BaseModel):
    """Paginated list of profiles"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Profile] | None = Field(default=None)
    links: ProfilesListLinks | None = Field(default=None)

class ListLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)

class ListAttributes(BaseModel):
    """List attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None, description="List name")
    """List name"""
    created: str | None | None = Field(default=None, description="Creation timestamp")
    """Creation timestamp"""
    updated: str | None | None = Field(default=None, description="Last update timestamp")
    """Last update timestamp"""
    opt_in_process: str | None | None = Field(default=None, description="Opt-in process type")
    """Opt-in process type"""

class List(BaseModel):
    """A Klaviyo list for organizing profiles"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    type_: str | None = Field(default=None, alias="type")
    attributes: ListAttributes | None = Field(default=None)
    links: ListLinks | None = Field(default=None)

class ListsListLinks(BaseModel):
    """Nested schema for ListsList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)
    next: str | None | None = Field(default=None)
    prev: str | None | None = Field(default=None)

class ListsList(BaseModel):
    """Paginated list of lists"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[List] | None = Field(default=None)
    links: ListsListLinks | None = Field(default=None)

class CampaignAttributes(BaseModel):
    """Campaign attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None, description="Campaign name")
    """Campaign name"""
    status: str | None | None = Field(default=None, description="Campaign status")
    """Campaign status"""
    archived: bool | None | None = Field(default=None, description="Whether campaign is archived")
    """Whether campaign is archived"""
    audiences: dict[str, Any] | None | None = Field(default=None, description="Target audiences")
    """Target audiences"""
    send_options: dict[str, Any] | None | None = Field(default=None, description="Send options")
    """Send options"""
    tracking_options: dict[str, Any] | None | None = Field(default=None, description="Tracking options")
    """Tracking options"""
    send_strategy: dict[str, Any] | None | None = Field(default=None, description="Send strategy")
    """Send strategy"""
    created_at: str | None | None = Field(default=None, description="Creation timestamp")
    """Creation timestamp"""
    scheduled_at: str | None | None = Field(default=None, description="Scheduled send time")
    """Scheduled send time"""
    updated_at: str | None | None = Field(default=None, description="Last update timestamp")
    """Last update timestamp"""
    send_time: str | None | None = Field(default=None, description="Actual send time")
    """Actual send time"""

class CampaignLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)

class Campaign(BaseModel):
    """A Klaviyo campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    type_: str | None = Field(default=None, alias="type")
    attributes: CampaignAttributes | None = Field(default=None)
    links: CampaignLinks | None = Field(default=None)

class CampaignsListLinks(BaseModel):
    """Nested schema for CampaignsList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)
    next: str | None | None = Field(default=None)
    prev: str | None | None = Field(default=None)

class CampaignsList(BaseModel):
    """Paginated list of campaigns"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Campaign] | None = Field(default=None)
    links: CampaignsListLinks | None = Field(default=None)

class EventAttributes(BaseModel):
    """Event attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    timestamp: Any | None = Field(default=None, description="Event timestamp (can be ISO string or Unix timestamp)")
    """Event timestamp (can be ISO string or Unix timestamp)"""
    datetime: str | None | None = Field(default=None, description="Event datetime")
    """Event datetime"""
    uuid: str | None | None = Field(default=None, description="Event UUID")
    """Event UUID"""
    event_properties: dict[str, Any] | None | None = Field(default=None, description="Custom event properties")
    """Custom event properties"""

class EventRelationshipsMetricData(BaseModel):
    """Nested schema for EventRelationshipsMetric.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    id: str | None | None = Field(default=None)

class EventRelationshipsMetric(BaseModel):
    """Nested schema for EventRelationships.metric"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: EventRelationshipsMetricData | None | None = Field(default=None)

class EventRelationshipsProfileData(BaseModel):
    """Nested schema for EventRelationshipsProfile.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    id: str | None | None = Field(default=None)

class EventRelationshipsProfile(BaseModel):
    """Nested schema for EventRelationships.profile"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: EventRelationshipsProfileData | None | None = Field(default=None)

class EventRelationships(BaseModel):
    """Related resources"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    profile: EventRelationshipsProfile | None | None = Field(default=None)
    metric: EventRelationshipsMetric | None | None = Field(default=None)

class EventLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)

class Event(BaseModel):
    """A Klaviyo event representing an action taken by a profile"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    type_: str | None = Field(default=None, alias="type")
    attributes: EventAttributes | None = Field(default=None)
    relationships: EventRelationships | None = Field(default=None)
    links: EventLinks | None = Field(default=None)

class EventsListLinks(BaseModel):
    """Nested schema for EventsList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)
    next: str | None | None = Field(default=None)
    prev: str | None | None = Field(default=None)

class EventsList(BaseModel):
    """Paginated list of events"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Event] | None = Field(default=None)
    links: EventsListLinks | None = Field(default=None)

class MetricLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)

class MetricAttributesIntegration(BaseModel):
    """Integration information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)
    category: str | None | None = Field(default=None)

class MetricAttributes(BaseModel):
    """Metric attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None, description="Metric name")
    """Metric name"""
    created: str | None | None = Field(default=None, description="Creation timestamp")
    """Creation timestamp"""
    updated: str | None | None = Field(default=None, description="Last update timestamp")
    """Last update timestamp"""
    integration: MetricAttributesIntegration | None | None = Field(default=None, description="Integration information")
    """Integration information"""

class Metric(BaseModel):
    """A Klaviyo metric (event type)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    type_: str | None = Field(default=None, alias="type")
    attributes: MetricAttributes | None = Field(default=None)
    links: MetricLinks | None = Field(default=None)

class MetricsListLinks(BaseModel):
    """Nested schema for MetricsList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)
    next: str | None | None = Field(default=None)
    prev: str | None | None = Field(default=None)

class MetricsList(BaseModel):
    """Paginated list of metrics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Metric] | None = Field(default=None)
    links: MetricsListLinks | None = Field(default=None)

class FlowAttributes(BaseModel):
    """Flow attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None, description="Flow name")
    """Flow name"""
    status: str | None | None = Field(default=None, description="Flow status (draft, manual, live)")
    """Flow status (draft, manual, live)"""
    archived: bool | None | None = Field(default=None, description="Whether flow is archived")
    """Whether flow is archived"""
    created: str | None | None = Field(default=None, description="Creation timestamp")
    """Creation timestamp"""
    updated: str | None | None = Field(default=None, description="Last update timestamp")
    """Last update timestamp"""
    trigger_type: str | None | None = Field(default=None, description="Type of trigger for the flow")
    """Type of trigger for the flow"""

class FlowLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)

class Flow(BaseModel):
    """A Klaviyo flow (automated sequence)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    type_: str | None = Field(default=None, alias="type")
    attributes: FlowAttributes | None = Field(default=None)
    links: FlowLinks | None = Field(default=None)

class FlowsListLinks(BaseModel):
    """Nested schema for FlowsList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)
    next: str | None | None = Field(default=None)
    prev: str | None | None = Field(default=None)

class FlowsList(BaseModel):
    """Paginated list of flows"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Flow] | None = Field(default=None)
    links: FlowsListLinks | None = Field(default=None)

class TemplateLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)

class TemplateAttributes(BaseModel):
    """Template attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None, description="Template name")
    """Template name"""
    editor_type: str | None | None = Field(default=None, description="Editor type used to create template")
    """Editor type used to create template"""
    html: str | None | None = Field(default=None, description="HTML content")
    """HTML content"""
    text: str | None | None = Field(default=None, description="Plain text content")
    """Plain text content"""
    created: str | None | None = Field(default=None, description="Creation timestamp")
    """Creation timestamp"""
    updated: str | None | None = Field(default=None, description="Last update timestamp")
    """Last update timestamp"""

class Template(BaseModel):
    """A Klaviyo email template"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    type_: str | None = Field(default=None, alias="type")
    attributes: TemplateAttributes | None = Field(default=None)
    links: TemplateLinks | None = Field(default=None)

class TemplatesListLinks(BaseModel):
    """Nested schema for TemplatesList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None | None = Field(default=None)
    next: str | None | None = Field(default=None)
    prev: str | None | None = Field(default=None)

class TemplatesList(BaseModel):
    """Paginated list of templates"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Template] | None = Field(default=None)
    links: TemplatesListLinks | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class ProfilesListResultMeta(BaseModel):
    """Metadata for profiles.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class ListsListResultMeta(BaseModel):
    """Metadata for lists.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class CampaignsListResultMeta(BaseModel):
    """Metadata for campaigns.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class EventsListResultMeta(BaseModel):
    """Metadata for events.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class MetricsListResultMeta(BaseModel):
    """Metadata for metrics.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class FlowsListResultMeta(BaseModel):
    """Metadata for flows.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class EmailTemplatesListResultMeta(BaseModel):
    """Metadata for email_templates.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class KlaviyoCheckResult(BaseModel):
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


class KlaviyoExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class KlaviyoExecuteResultWithMeta(KlaviyoExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class ProfilesSearchData(BaseModel):
    """Search result data for profiles entity."""
    model_config = ConfigDict(extra="allow")

    attributes: dict[str, Any] | None = None
    """"""
    id: str | None = None
    """"""
    links: dict[str, Any] | None = None
    """"""
    relationships: dict[str, Any] | None = None
    """"""
    segments: dict[str, Any] | None = None
    """"""
    type_: str | None = None
    """"""
    updated: str | None = None
    """"""


class EventsSearchData(BaseModel):
    """Search result data for events entity."""
    model_config = ConfigDict(extra="allow")

    attributes: dict[str, Any] | None = None
    """"""
    datetime: str | None = None
    """"""
    id: str | None = None
    """"""
    links: dict[str, Any] | None = None
    """"""
    relationships: dict[str, Any] | None = None
    """"""
    type_: str | None = None
    """"""


class EmailTemplatesSearchData(BaseModel):
    """Search result data for email_templates entity."""
    model_config = ConfigDict(extra="allow")

    attributes: dict[str, Any] | None = None
    """"""
    id: str | None = None
    """"""
    links: dict[str, Any] | None = None
    """"""
    type_: str | None = None
    """"""
    updated: str | None = None
    """"""


class CampaignsSearchData(BaseModel):
    """Search result data for campaigns entity."""
    model_config = ConfigDict(extra="allow")

    attributes: dict[str, Any] | None = None
    """"""
    id: str | None = None
    """"""
    links: dict[str, Any] | None = None
    """"""
    relationships: dict[str, Any] | None = None
    """"""
    type_: str | None = None
    """"""
    updated_at: str | None = None
    """"""


class FlowsSearchData(BaseModel):
    """Search result data for flows entity."""
    model_config = ConfigDict(extra="allow")

    attributes: dict[str, Any] | None = None
    """"""
    id: str | None = None
    """"""
    links: dict[str, Any] | None = None
    """"""
    relationships: dict[str, Any] | None = None
    """"""
    type_: str | None = None
    """"""
    updated: str | None = None
    """"""


class MetricsSearchData(BaseModel):
    """Search result data for metrics entity."""
    model_config = ConfigDict(extra="allow")

    attributes: dict[str, Any] | None = None
    """"""
    id: str | None = None
    """"""
    links: dict[str, Any] | None = None
    """"""
    relationships: dict[str, Any] | None = None
    """"""
    type_: str | None = None
    """"""
    updated: str | None = None
    """"""


class ListsSearchData(BaseModel):
    """Search result data for lists entity."""
    model_config = ConfigDict(extra="allow")

    attributes: dict[str, Any] | None = None
    """"""
    id: str | None = None
    """"""
    links: dict[str, Any] | None = None
    """"""
    relationships: dict[str, Any] | None = None
    """"""
    type_: str | None = None
    """"""
    updated: str | None = None
    """"""


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

ProfilesSearchResult = AirbyteSearchResult[ProfilesSearchData]
"""Search result type for profiles entity."""

EventsSearchResult = AirbyteSearchResult[EventsSearchData]
"""Search result type for events entity."""

EmailTemplatesSearchResult = AirbyteSearchResult[EmailTemplatesSearchData]
"""Search result type for email_templates entity."""

CampaignsSearchResult = AirbyteSearchResult[CampaignsSearchData]
"""Search result type for campaigns entity."""

FlowsSearchResult = AirbyteSearchResult[FlowsSearchData]
"""Search result type for flows entity."""

MetricsSearchResult = AirbyteSearchResult[MetricsSearchData]
"""Search result type for metrics entity."""

ListsSearchResult = AirbyteSearchResult[ListsSearchData]
"""Search result type for lists entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

ProfilesListResult = KlaviyoExecuteResultWithMeta[list[Profile], ProfilesListResultMeta]
"""Result type for profiles.list operation with data and metadata."""

ListsListResult = KlaviyoExecuteResultWithMeta[list[List], ListsListResultMeta]
"""Result type for lists.list operation with data and metadata."""

CampaignsListResult = KlaviyoExecuteResultWithMeta[list[Campaign], CampaignsListResultMeta]
"""Result type for campaigns.list operation with data and metadata."""

EventsListResult = KlaviyoExecuteResultWithMeta[list[Event], EventsListResultMeta]
"""Result type for events.list operation with data and metadata."""

MetricsListResult = KlaviyoExecuteResultWithMeta[list[Metric], MetricsListResultMeta]
"""Result type for metrics.list operation with data and metadata."""

FlowsListResult = KlaviyoExecuteResultWithMeta[list[Flow], FlowsListResultMeta]
"""Result type for flows.list operation with data and metadata."""

EmailTemplatesListResult = KlaviyoExecuteResultWithMeta[list[Template], EmailTemplatesListResultMeta]
"""Result type for email_templates.list operation with data and metadata."""

