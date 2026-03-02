"""
Pydantic models for amplitude connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class AmplitudeAuthConfig(BaseModel):
    """API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Amplitude project API key. Find it in Settings > Projects in your Amplitude account.
"""
    secret_key: str
    """Your Amplitude project secret key. Find it in Settings > Projects in your Amplitude account.
"""

# Replication configuration

class AmplitudeReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Amplitude."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date and time in the format YYYY-MM-DDTHH:mm:ssZ. Any data before this date will not be replicated.
"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Annotation(BaseModel):
    """A chart annotation object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    date: Union[str | None, Any] = Field(default=None)
    details: Union[str | None, Any] = Field(default=None)
    label: Union[str | None, Any] = Field(default=None)

class AnnotationV3Category(BaseModel):
    """The annotation category"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None, description="Category ID")
    """Category ID"""
    category: Union[str, Any] = Field(default=None, description="Category name")
    """Category name"""

class AnnotationV3(BaseModel):
    """A chart annotation object (v3 API format)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    start: Union[str | None, Any] = Field(default=None)
    end: Union[str | None, Any] = Field(default=None)
    label: Union[str | None, Any] = Field(default=None)
    details: Union[str | None, Any] = Field(default=None)
    category: Union[AnnotationV3Category | None, Any] = Field(default=None)
    chart_id: Union[str | None, Any] = Field(default=None)

class AnnotationsList(BaseModel):
    """List of annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[Annotation], Any] = Field(default=None)

class AnnotationGetResponse(BaseModel):
    """Single annotation response"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[AnnotationV3, Any] = Field(default=None)

class Cohort(BaseModel):
    """A user cohort object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    app_id: Union[int | None, Any] = Field(default=None, alias="appId")
    archived: Union[bool | None, Any] = Field(default=None)
    chart_id: Union[str | None, Any] = Field(default=None)
    created_at: Union[int | None, Any] = Field(default=None, alias="createdAt")
    definition: Union[dict[str, Any] | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    edit_id: Union[str | None, Any] = Field(default=None)
    finished: Union[bool | None, Any] = Field(default=None)
    hidden: Union[bool | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)
    is_official_content: Union[bool | None, Any] = Field(default=None)
    is_predictive: Union[bool | None, Any] = Field(default=None)
    last_computed: Union[int | None, Any] = Field(default=None, alias="lastComputed")
    last_mod: Union[int | None, Any] = Field(default=None, alias="lastMod")
    last_viewed: Union[int | None, Any] = Field(default=None)
    location_id: Union[str | None, Any] = Field(default=None)
    metadata: Union[list[str] | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    owners: Union[list[str] | None, Any] = Field(default=None)
    popularity: Union[int | None, Any] = Field(default=None)
    published: Union[bool | None, Any] = Field(default=None)
    shortcut_ids: Union[list[str] | None, Any] = Field(default=None)
    size: Union[int | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    view_count: Union[int | None, Any] = Field(default=None)
    viewers: Union[list[str] | None, Any] = Field(default=None)
    include_data_app_types: Union[list[str] | None, Any] = Field(default=None)
    per_app_metadata: Union[dict[str, Any] | None, Any] = Field(default=None)
    cohort_definition_type: Union[str | None, Any] = Field(default=None)
    cohort_output_type: Union[str | None, Any] = Field(default=None)
    is_generated_content: Union[bool | None, Any] = Field(default=None)

class CohortGetResponse(BaseModel):
    """Single cohort response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cohort: Union[Cohort, Any] = Field(default=None)

class CohortsList(BaseModel):
    """List of cohorts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cohorts: Union[list[Cohort], Any] = Field(default=None)

class EventType(BaseModel):
    """An event type definition with weekly totals"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    autohidden: Union[bool | None, Any] = Field(default=None)
    clusters_hidden: Union[bool | None, Any] = Field(default=None)
    deleted: Union[bool | None, Any] = Field(default=None)
    display: Union[str | None, Any] = Field(default=None)
    flow_hidden: Union[bool | None, Any] = Field(default=None)
    hidden: Union[bool | None, Any] = Field(default=None)
    id: Union[float, Any] = Field(default=None)
    in_waitroom: Union[bool | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    non_active: Union[bool | None, Any] = Field(default=None)
    timeline_hidden: Union[bool | None, Any] = Field(default=None)
    totals: Union[float | None, Any] = Field(default=None)
    totals_delta: Union[float | None, Any] = Field(default=None)
    value: Union[str | None, Any] = Field(default=None)
    waitroom_approved: Union[bool | None, Any] = Field(default=None)

class EventsListResponse(BaseModel):
    """List of event types"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[EventType], Any] = Field(default=None)

class ActiveUsersDataSeriesmetaItem(BaseModel):
    """Nested schema for ActiveUsersData.seriesMeta_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    segment_index: Union[int, Any] = Field(default=None, alias="segmentIndex")

class ActiveUsersData(BaseModel):
    """Active or new user count data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    series: Union[list[list[float]] | None, Any] = Field(default=None)
    series_collapsed: Union[list[list[float]] | None, Any] = Field(default=None, alias="seriesCollapsed")
    series_labels: Union[list[Any] | None, Any] = Field(default=None, alias="seriesLabels")
    series_meta: Union[list[ActiveUsersDataSeriesmetaItem] | None, Any] = Field(default=None, alias="seriesMeta")
    x_values: Union[list[str] | None, Any] = Field(default=None, alias="xValues")

class ActiveUsersResponse(BaseModel):
    """Active users response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[ActiveUsersData, Any] = Field(default=None)

class AverageSessionLengthDataSeriesmetaItem(BaseModel):
    """Nested schema for AverageSessionLengthData.seriesMeta_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    segment_index: Union[int, Any] = Field(default=None, alias="segmentIndex")
    session_index: Union[int, Any] = Field(default=None, alias="sessionIndex")

class AverageSessionLengthDataSeriescollapsedItemItem(BaseModel):
    """Nested schema for AverageSessionLengthData.seriesCollapsed_item_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    set_id: Union[str, Any] = Field(default=None, alias="setId")
    value: Union[float, Any] = Field(default=None)

class AverageSessionLengthData(BaseModel):
    """Average session length data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    series: Union[list[list[float]] | None, Any] = Field(default=None)
    series_collapsed: Union[list[list[AverageSessionLengthDataSeriescollapsedItemItem]] | None, Any] = Field(default=None, alias="seriesCollapsed")
    series_meta: Union[list[AverageSessionLengthDataSeriesmetaItem] | None, Any] = Field(default=None, alias="seriesMeta")
    x_values: Union[list[str] | None, Any] = Field(default=None, alias="xValues")

class AverageSessionLengthResponse(BaseModel):
    """Average session length response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[AverageSessionLengthData, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== CHECK RESULT MODEL =====

class AmplitudeCheckResult(BaseModel):
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


class AmplitudeExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class AmplitudeExecuteResultWithMeta(AmplitudeExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AnnotationsSearchData(BaseModel):
    """Search result data for annotations entity."""
    model_config = ConfigDict(extra="allow")

    date: str | None = None
    """The date when the annotation was made"""
    details: str | None = None
    """Additional details or information related to the annotation"""
    id: int | None = None
    """The unique identifier for the annotation"""
    label: str | None = None
    """The label assigned to the annotation"""


class CohortsSearchData(BaseModel):
    """Search result data for cohorts entity."""
    model_config = ConfigDict(extra="allow")

    app_id: int | None = None
    """The unique identifier of the application"""
    archived: bool | None = None
    """Indicates if the cohort data is archived"""
    chart_id: str | None = None
    """The identifier of the chart associated with the cohort"""
    created_at: int | None = None
    """The timestamp when the cohort was created"""
    definition: dict[str, Any] | None = None
    """The specific definition or criteria for the cohort"""
    description: str | None = None
    """A brief explanation or summary of the cohort"""
    edit_id: str | None = None
    """The ID for editing purposes or version control"""
    finished: bool | None = None
    """Indicates if the cohort data has been finalized"""
    hidden: bool | None = None
    """Flag to determine if the cohort is hidden from view"""
    id: str | None = None
    """The unique identifier for the cohort"""
    is_official_content: bool | None = None
    """Indicates if the cohort data is official content"""
    is_predictive: bool | None = None
    """Flag to indicate if the cohort is predictive"""
    last_computed: int | None = None
    """Timestamp of the last computation of cohort data"""
    last_mod: int | None = None
    """Timestamp of the last modification made to the cohort"""
    last_viewed: int | None = None
    """Timestamp when the cohort was last viewed"""
    location_id: str | None = None
    """Identifier of the location associated with the cohort"""
    metadata: list[Any] | None = None
    """Additional information or data related to the cohort"""
    name: str | None = None
    """The name or title of the cohort"""
    owners: list[Any] | None = None
    """The owners or administrators of the cohort"""
    popularity: int | None = None
    """Popularity rank or score of the cohort"""
    published: bool | None = None
    """Status indicating if the cohort data is published"""
    shortcut_ids: list[Any] | None = None
    """Identifiers of any shortcuts associated with the cohort"""
    size: int | None = None
    """Size or scale of the cohort data"""
    type: str | None = None
    """The type or category of the cohort"""
    view_count: int | None = None
    """The total count of views on the cohort data"""
    viewers: list[Any] | None = None
    """Users or viewers who have access to the cohort data"""


class EventsListSearchData(BaseModel):
    """Search result data for events_list entity."""
    model_config = ConfigDict(extra="allow")

    autohidden: bool | None = None
    """Whether the event is auto-hidden"""
    clusters_hidden: bool | None = None
    """Whether the event is hidden from clusters"""
    deleted: bool | None = None
    """Whether the event is deleted"""
    display: str | None = None
    """Display name of the event"""
    flow_hidden: bool | None = None
    """Whether the event is hidden from Pathfinder"""
    hidden: bool | None = None
    """Whether the event is hidden"""
    id: float | None = None
    """Unique identifier for the event type"""
    in_waitroom: bool | None = None
    """Whether the event is in the waitroom"""
    name: str | None = None
    """Name of the event type"""
    non_active: bool | None = None
    """Whether the event is marked as inactive"""
    timeline_hidden: Any = None
    """Whether the event is hidden from the timeline"""
    totals: float | None = None
    """Total number of times the event occurred this week"""
    totals_delta: float | None = None
    """Change in totals from the previous period"""
    value: str | None = None
    """Raw event name in the data"""


class ActiveUsersSearchData(BaseModel):
    """Search result data for active_users entity."""
    model_config = ConfigDict(extra="allow")

    date: str | None = None
    """The date for which the active user data is reported"""
    statistics: dict[str, Any] | None = None
    """The statistics related to the active users for the given date"""


class AverageSessionLengthSearchData(BaseModel):
    """Search result data for average_session_length entity."""
    model_config = ConfigDict(extra="allow")

    date: str | None = None
    """The date on which the session occurred"""
    length: float | None = None
    """The duration of the session in seconds"""


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

AnnotationsSearchResult = AirbyteSearchResult[AnnotationsSearchData]
"""Search result type for annotations entity."""

CohortsSearchResult = AirbyteSearchResult[CohortsSearchData]
"""Search result type for cohorts entity."""

EventsListSearchResult = AirbyteSearchResult[EventsListSearchData]
"""Search result type for events_list entity."""

ActiveUsersSearchResult = AirbyteSearchResult[ActiveUsersSearchData]
"""Search result type for active_users entity."""

AverageSessionLengthSearchResult = AirbyteSearchResult[AverageSessionLengthSearchData]
"""Search result type for average_session_length entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

AnnotationsListResult = AmplitudeExecuteResult[list[Annotation]]
"""Result type for annotations.list operation."""

CohortsListResult = AmplitudeExecuteResult[list[Cohort]]
"""Result type for cohorts.list operation."""

EventsListListResult = AmplitudeExecuteResult[list[EventType]]
"""Result type for events_list.list operation."""

ActiveUsersListResult = AmplitudeExecuteResult[ActiveUsersData]
"""Result type for active_users.list operation."""

AverageSessionLengthListResult = AmplitudeExecuteResult[AverageSessionLengthData]
"""Result type for average_session_length.list operation."""

