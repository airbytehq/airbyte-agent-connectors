"""
Pydantic models for klaviyo connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class KlaviyoAuthConfig(BaseModel):
    """Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Klaviyo private API key"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class ProfileLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)

class ProfileAttributesLocation(BaseModel):
    """Location information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address1: Union[str | None, Any] = Field(default=None)
    address2: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    country: Union[str | None, Any] = Field(default=None)
    region: Union[str | None, Any] = Field(default=None)
    zip: Union[str | None, Any] = Field(default=None)
    timezone: Union[str | None, Any] = Field(default=None)
    latitude: Union[float | None, Any] = Field(default=None)
    longitude: Union[float | None, Any] = Field(default=None)

class ProfileAttributes(BaseModel):
    """Profile attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: Union[str | None, Any] = Field(default=None, description="Email address")
    """Email address"""
    phone_number: Union[str | None, Any] = Field(default=None, description="Phone number")
    """Phone number"""
    external_id: Union[str | None, Any] = Field(default=None, description="External identifier")
    """External identifier"""
    first_name: Union[str | None, Any] = Field(default=None, description="First name")
    """First name"""
    last_name: Union[str | None, Any] = Field(default=None, description="Last name")
    """Last name"""
    organization: Union[str | None, Any] = Field(default=None, description="Organization name")
    """Organization name"""
    title: Union[str | None, Any] = Field(default=None, description="Job title")
    """Job title"""
    image: Union[str | None, Any] = Field(default=None, description="Profile image URL")
    """Profile image URL"""
    created: Union[str | None, Any] = Field(default=None, description="Creation timestamp")
    """Creation timestamp"""
    updated: Union[str | None, Any] = Field(default=None, description="Last update timestamp")
    """Last update timestamp"""
    location: Union[ProfileAttributesLocation | None, Any] = Field(default=None, description="Location information")
    """Location information"""
    properties: Union[dict[str, Any] | None, Any] = Field(default=None, description="Custom properties")
    """Custom properties"""

class Profile(BaseModel):
    """A Klaviyo profile representing a contact"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    attributes: Union[ProfileAttributes | None, Any] = Field(default=None)
    links: Union[ProfileLinks | None, Any] = Field(default=None)

class ProfilesListLinks(BaseModel):
    """Nested schema for ProfilesList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)
    next: Union[str | None, Any] = Field(default=None)
    prev: Union[str | None, Any] = Field(default=None)

class ProfilesList(BaseModel):
    """Paginated list of profiles"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Profile], Any] = Field(default=None)
    links: Union[ProfilesListLinks | None, Any] = Field(default=None)

class ListAttributes(BaseModel):
    """List attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str | None, Any] = Field(default=None, description="List name")
    """List name"""
    created: Union[str | None, Any] = Field(default=None, description="Creation timestamp")
    """Creation timestamp"""
    updated: Union[str | None, Any] = Field(default=None, description="Last update timestamp")
    """Last update timestamp"""
    opt_in_process: Union[str | None, Any] = Field(default=None, description="Opt-in process type")
    """Opt-in process type"""

class ListLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)

class List(BaseModel):
    """A Klaviyo list for organizing profiles"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    attributes: Union[ListAttributes | None, Any] = Field(default=None)
    links: Union[ListLinks | None, Any] = Field(default=None)

class ListsListLinks(BaseModel):
    """Nested schema for ListsList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)
    next: Union[str | None, Any] = Field(default=None)
    prev: Union[str | None, Any] = Field(default=None)

class ListsList(BaseModel):
    """Paginated list of lists"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[List], Any] = Field(default=None)
    links: Union[ListsListLinks | None, Any] = Field(default=None)

class CampaignAttributes(BaseModel):
    """Campaign attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str | None, Any] = Field(default=None, description="Campaign name")
    """Campaign name"""
    status: Union[str | None, Any] = Field(default=None, description="Campaign status")
    """Campaign status"""
    archived: Union[bool | None, Any] = Field(default=None, description="Whether campaign is archived")
    """Whether campaign is archived"""
    audiences: Union[dict[str, Any] | None, Any] = Field(default=None, description="Target audiences")
    """Target audiences"""
    send_options: Union[dict[str, Any] | None, Any] = Field(default=None, description="Send options")
    """Send options"""
    tracking_options: Union[dict[str, Any] | None, Any] = Field(default=None, description="Tracking options")
    """Tracking options"""
    send_strategy: Union[dict[str, Any] | None, Any] = Field(default=None, description="Send strategy")
    """Send strategy"""
    created_at: Union[str | None, Any] = Field(default=None, description="Creation timestamp")
    """Creation timestamp"""
    scheduled_at: Union[str | None, Any] = Field(default=None, description="Scheduled send time")
    """Scheduled send time"""
    updated_at: Union[str | None, Any] = Field(default=None, description="Last update timestamp")
    """Last update timestamp"""
    send_time: Union[str | None, Any] = Field(default=None, description="Actual send time")
    """Actual send time"""

class CampaignLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)

class Campaign(BaseModel):
    """A Klaviyo campaign"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    attributes: Union[CampaignAttributes | None, Any] = Field(default=None)
    links: Union[CampaignLinks | None, Any] = Field(default=None)

class CampaignsListLinks(BaseModel):
    """Nested schema for CampaignsList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)
    next: Union[str | None, Any] = Field(default=None)
    prev: Union[str | None, Any] = Field(default=None)

class CampaignsList(BaseModel):
    """Paginated list of campaigns"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Campaign], Any] = Field(default=None)
    links: Union[CampaignsListLinks | None, Any] = Field(default=None)

class EventRelationshipsProfileData(BaseModel):
    """Nested schema for EventRelationshipsProfile.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class EventRelationshipsProfile(BaseModel):
    """Nested schema for EventRelationships.profile"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[EventRelationshipsProfileData | None, Any] = Field(default=None)

class EventRelationshipsMetricData(BaseModel):
    """Nested schema for EventRelationshipsMetric.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class EventRelationshipsMetric(BaseModel):
    """Nested schema for EventRelationships.metric"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[EventRelationshipsMetricData | None, Any] = Field(default=None)

class EventRelationships(BaseModel):
    """Related resources"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    profile: Union[EventRelationshipsProfile | None, Any] = Field(default=None)
    metric: Union[EventRelationshipsMetric | None, Any] = Field(default=None)

class EventAttributes(BaseModel):
    """Event attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    timestamp: Union[Any, Any] = Field(default=None, description="Event timestamp (can be ISO string or Unix timestamp)")
    """Event timestamp (can be ISO string or Unix timestamp)"""
    datetime: Union[str | None, Any] = Field(default=None, description="Event datetime")
    """Event datetime"""
    uuid: Union[str | None, Any] = Field(default=None, description="Event UUID")
    """Event UUID"""
    event_properties: Union[dict[str, Any] | None, Any] = Field(default=None, description="Custom event properties")
    """Custom event properties"""

class EventLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)

class Event(BaseModel):
    """A Klaviyo event representing an action taken by a profile"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    attributes: Union[EventAttributes | None, Any] = Field(default=None)
    relationships: Union[EventRelationships | None, Any] = Field(default=None)
    links: Union[EventLinks | None, Any] = Field(default=None)

class EventsListLinks(BaseModel):
    """Nested schema for EventsList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)
    next: Union[str | None, Any] = Field(default=None)
    prev: Union[str | None, Any] = Field(default=None)

class EventsList(BaseModel):
    """Paginated list of events"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Event], Any] = Field(default=None)
    links: Union[EventsListLinks | None, Any] = Field(default=None)

class MetricAttributesIntegration(BaseModel):
    """Integration information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    category: Union[str | None, Any] = Field(default=None)

class MetricAttributes(BaseModel):
    """Metric attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str | None, Any] = Field(default=None, description="Metric name")
    """Metric name"""
    created: Union[str | None, Any] = Field(default=None, description="Creation timestamp")
    """Creation timestamp"""
    updated: Union[str | None, Any] = Field(default=None, description="Last update timestamp")
    """Last update timestamp"""
    integration: Union[MetricAttributesIntegration | None, Any] = Field(default=None, description="Integration information")
    """Integration information"""

class MetricLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)

class Metric(BaseModel):
    """A Klaviyo metric (event type)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    attributes: Union[MetricAttributes | None, Any] = Field(default=None)
    links: Union[MetricLinks | None, Any] = Field(default=None)

class MetricsListLinks(BaseModel):
    """Nested schema for MetricsList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)
    next: Union[str | None, Any] = Field(default=None)
    prev: Union[str | None, Any] = Field(default=None)

class MetricsList(BaseModel):
    """Paginated list of metrics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Metric], Any] = Field(default=None)
    links: Union[MetricsListLinks | None, Any] = Field(default=None)

class FlowLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)

class FlowAttributes(BaseModel):
    """Flow attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str | None, Any] = Field(default=None, description="Flow name")
    """Flow name"""
    status: Union[str | None, Any] = Field(default=None, description="Flow status (draft, manual, live)")
    """Flow status (draft, manual, live)"""
    archived: Union[bool | None, Any] = Field(default=None, description="Whether flow is archived")
    """Whether flow is archived"""
    created: Union[str | None, Any] = Field(default=None, description="Creation timestamp")
    """Creation timestamp"""
    updated: Union[str | None, Any] = Field(default=None, description="Last update timestamp")
    """Last update timestamp"""
    trigger_type: Union[str | None, Any] = Field(default=None, description="Type of trigger for the flow")
    """Type of trigger for the flow"""

class Flow(BaseModel):
    """A Klaviyo flow (automated sequence)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    attributes: Union[FlowAttributes | None, Any] = Field(default=None)
    links: Union[FlowLinks | None, Any] = Field(default=None)

class FlowsListLinks(BaseModel):
    """Nested schema for FlowsList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)
    next: Union[str | None, Any] = Field(default=None)
    prev: Union[str | None, Any] = Field(default=None)

class FlowsList(BaseModel):
    """Paginated list of flows"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Flow], Any] = Field(default=None)
    links: Union[FlowsListLinks | None, Any] = Field(default=None)

class TemplateAttributes(BaseModel):
    """Template attributes"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str | None, Any] = Field(default=None, description="Template name")
    """Template name"""
    editor_type: Union[str | None, Any] = Field(default=None, description="Editor type used to create template")
    """Editor type used to create template"""
    html: Union[str | None, Any] = Field(default=None, description="HTML content")
    """HTML content"""
    text: Union[str | None, Any] = Field(default=None, description="Plain text content")
    """Plain text content"""
    created: Union[str | None, Any] = Field(default=None, description="Creation timestamp")
    """Creation timestamp"""
    updated: Union[str | None, Any] = Field(default=None, description="Last update timestamp")
    """Last update timestamp"""

class TemplateLinks(BaseModel):
    """Related links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)

class Template(BaseModel):
    """A Klaviyo email template"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    attributes: Union[TemplateAttributes | None, Any] = Field(default=None)
    links: Union[TemplateLinks | None, Any] = Field(default=None)

class TemplatesListLinks(BaseModel):
    """Nested schema for TemplatesList.links"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: Union[str | None, Any] = Field(default=None)
    next: Union[str | None, Any] = Field(default=None)
    prev: Union[str | None, Any] = Field(default=None)

class TemplatesList(BaseModel):
    """Paginated list of templates"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Template], Any] = Field(default=None)
    links: Union[TemplatesListLinks | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

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
    type: str | None = None
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
    type: str | None = None
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
    type: str | None = None
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
    type: str | None = None
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
    type: str | None = None
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
    type: str | None = None
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
    type: str | None = None
    """"""
    updated: str | None = None
    """"""


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

ProfilesListResult = KlaviyoExecuteResult[list[Profile]]
"""Result type for profiles.list operation."""

ListsListResult = KlaviyoExecuteResult[list[List]]
"""Result type for lists.list operation."""

CampaignsListResult = KlaviyoExecuteResult[list[Campaign]]
"""Result type for campaigns.list operation."""

EventsListResult = KlaviyoExecuteResult[list[Event]]
"""Result type for events.list operation."""

MetricsListResult = KlaviyoExecuteResult[list[Metric]]
"""Result type for metrics.list operation."""

FlowsListResult = KlaviyoExecuteResult[list[Flow]]
"""Result type for flows.list operation."""

EmailTemplatesListResult = KlaviyoExecuteResult[list[Template]]
"""Result type for email_templates.list operation."""

