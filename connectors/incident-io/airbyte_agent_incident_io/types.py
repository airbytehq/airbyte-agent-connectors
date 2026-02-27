"""
Type definitions for incident-io connector.
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

class IncidentsListParams(TypedDict):
    """Parameters for incidents.list operation"""
    page_size: NotRequired[int]
    after: NotRequired[str]

class IncidentsGetParams(TypedDict):
    """Parameters for incidents.get operation"""
    id: str

class AlertsListParams(TypedDict):
    """Parameters for alerts.list operation"""
    page_size: NotRequired[int]
    after: NotRequired[str]

class AlertsGetParams(TypedDict):
    """Parameters for alerts.get operation"""
    id: str

class EscalationsListParams(TypedDict):
    """Parameters for escalations.list operation"""
    page_size: NotRequired[int]
    after: NotRequired[str]

class EscalationsGetParams(TypedDict):
    """Parameters for escalations.get operation"""
    id: str

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    page_size: NotRequired[int]
    after: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class IncidentUpdatesListParams(TypedDict):
    """Parameters for incident_updates.list operation"""
    page_size: NotRequired[int]
    after: NotRequired[str]

class IncidentRolesListParams(TypedDict):
    """Parameters for incident_roles.list operation"""
    pass

class IncidentRolesGetParams(TypedDict):
    """Parameters for incident_roles.get operation"""
    id: str

class IncidentStatusesListParams(TypedDict):
    """Parameters for incident_statuses.list operation"""
    pass

class IncidentStatusesGetParams(TypedDict):
    """Parameters for incident_statuses.get operation"""
    id: str

class IncidentTimestampsListParams(TypedDict):
    """Parameters for incident_timestamps.list operation"""
    pass

class IncidentTimestampsGetParams(TypedDict):
    """Parameters for incident_timestamps.get operation"""
    id: str

class SeveritiesListParams(TypedDict):
    """Parameters for severities.list operation"""
    pass

class SeveritiesGetParams(TypedDict):
    """Parameters for severities.get operation"""
    id: str

class CustomFieldsListParams(TypedDict):
    """Parameters for custom_fields.list operation"""
    pass

class CustomFieldsGetParams(TypedDict):
    """Parameters for custom_fields.get operation"""
    id: str

class CatalogTypesListParams(TypedDict):
    """Parameters for catalog_types.list operation"""
    pass

class CatalogTypesGetParams(TypedDict):
    """Parameters for catalog_types.get operation"""
    id: str

class SchedulesListParams(TypedDict):
    """Parameters for schedules.list operation"""
    page_size: NotRequired[int]
    after: NotRequired[str]

class SchedulesGetParams(TypedDict):
    """Parameters for schedules.get operation"""
    id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== INCIDENTS SEARCH TYPES =====

class IncidentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering incidents search queries."""
    call_url: str | None
    """URL of the call associated with the incident"""
    created_at: str | None
    """When the incident was created"""
    creator: dict[str, Any] | None
    """The user who created the incident"""
    custom_field_entries: list[Any] | None
    """Custom field values for the incident"""
    duration_metrics: list[Any] | None
    """Duration metrics associated with the incident"""
    has_debrief: bool | None
    """Whether the incident has had a debrief"""
    id: str | None
    """Unique identifier for the incident"""
    incident_role_assignments: list[Any] | None
    """Role assignments for the incident"""
    incident_status: dict[str, Any] | None
    """Current status of the incident"""
    incident_timestamp_values: list[Any] | None
    """Timestamp values for the incident"""
    incident_type: dict[str, Any] | None
    """Type of the incident"""
    mode: str | None
    """Mode of the incident: standard, retrospective, test, or tutorial"""
    name: str | None
    """Name/title of the incident"""
    permalink: str | None
    """Link to the incident in the dashboard"""
    reference: str | None
    """Human-readable reference (e.g. INC-123)"""
    severity: dict[str, Any] | None
    """Severity of the incident"""
    slack_channel_id: str | None
    """Slack channel ID for the incident"""
    slack_channel_name: str | None
    """Slack channel name for the incident"""
    slack_team_id: str | None
    """Slack team/workspace ID"""
    summary: str | None
    """Detailed summary of the incident"""
    updated_at: str | None
    """When the incident was last updated"""
    visibility: str | None
    """Whether the incident is public or private"""
    workload_minutes_late: float | None
    """Minutes of workload classified as late"""
    workload_minutes_sleeping: float | None
    """Minutes of workload classified as sleeping"""
    workload_minutes_total: float | None
    """Total workload minutes"""
    workload_minutes_working: float | None
    """Minutes of workload classified as working"""


class IncidentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    call_url: list[str]
    """URL of the call associated with the incident"""
    created_at: list[str]
    """When the incident was created"""
    creator: list[dict[str, Any]]
    """The user who created the incident"""
    custom_field_entries: list[list[Any]]
    """Custom field values for the incident"""
    duration_metrics: list[list[Any]]
    """Duration metrics associated with the incident"""
    has_debrief: list[bool]
    """Whether the incident has had a debrief"""
    id: list[str]
    """Unique identifier for the incident"""
    incident_role_assignments: list[list[Any]]
    """Role assignments for the incident"""
    incident_status: list[dict[str, Any]]
    """Current status of the incident"""
    incident_timestamp_values: list[list[Any]]
    """Timestamp values for the incident"""
    incident_type: list[dict[str, Any]]
    """Type of the incident"""
    mode: list[str]
    """Mode of the incident: standard, retrospective, test, or tutorial"""
    name: list[str]
    """Name/title of the incident"""
    permalink: list[str]
    """Link to the incident in the dashboard"""
    reference: list[str]
    """Human-readable reference (e.g. INC-123)"""
    severity: list[dict[str, Any]]
    """Severity of the incident"""
    slack_channel_id: list[str]
    """Slack channel ID for the incident"""
    slack_channel_name: list[str]
    """Slack channel name for the incident"""
    slack_team_id: list[str]
    """Slack team/workspace ID"""
    summary: list[str]
    """Detailed summary of the incident"""
    updated_at: list[str]
    """When the incident was last updated"""
    visibility: list[str]
    """Whether the incident is public or private"""
    workload_minutes_late: list[float]
    """Minutes of workload classified as late"""
    workload_minutes_sleeping: list[float]
    """Minutes of workload classified as sleeping"""
    workload_minutes_total: list[float]
    """Total workload minutes"""
    workload_minutes_working: list[float]
    """Minutes of workload classified as working"""


class IncidentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    call_url: Any
    """URL of the call associated with the incident"""
    created_at: Any
    """When the incident was created"""
    creator: Any
    """The user who created the incident"""
    custom_field_entries: Any
    """Custom field values for the incident"""
    duration_metrics: Any
    """Duration metrics associated with the incident"""
    has_debrief: Any
    """Whether the incident has had a debrief"""
    id: Any
    """Unique identifier for the incident"""
    incident_role_assignments: Any
    """Role assignments for the incident"""
    incident_status: Any
    """Current status of the incident"""
    incident_timestamp_values: Any
    """Timestamp values for the incident"""
    incident_type: Any
    """Type of the incident"""
    mode: Any
    """Mode of the incident: standard, retrospective, test, or tutorial"""
    name: Any
    """Name/title of the incident"""
    permalink: Any
    """Link to the incident in the dashboard"""
    reference: Any
    """Human-readable reference (e.g. INC-123)"""
    severity: Any
    """Severity of the incident"""
    slack_channel_id: Any
    """Slack channel ID for the incident"""
    slack_channel_name: Any
    """Slack channel name for the incident"""
    slack_team_id: Any
    """Slack team/workspace ID"""
    summary: Any
    """Detailed summary of the incident"""
    updated_at: Any
    """When the incident was last updated"""
    visibility: Any
    """Whether the incident is public or private"""
    workload_minutes_late: Any
    """Minutes of workload classified as late"""
    workload_minutes_sleeping: Any
    """Minutes of workload classified as sleeping"""
    workload_minutes_total: Any
    """Total workload minutes"""
    workload_minutes_working: Any
    """Minutes of workload classified as working"""


class IncidentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    call_url: str
    """URL of the call associated with the incident"""
    created_at: str
    """When the incident was created"""
    creator: str
    """The user who created the incident"""
    custom_field_entries: str
    """Custom field values for the incident"""
    duration_metrics: str
    """Duration metrics associated with the incident"""
    has_debrief: str
    """Whether the incident has had a debrief"""
    id: str
    """Unique identifier for the incident"""
    incident_role_assignments: str
    """Role assignments for the incident"""
    incident_status: str
    """Current status of the incident"""
    incident_timestamp_values: str
    """Timestamp values for the incident"""
    incident_type: str
    """Type of the incident"""
    mode: str
    """Mode of the incident: standard, retrospective, test, or tutorial"""
    name: str
    """Name/title of the incident"""
    permalink: str
    """Link to the incident in the dashboard"""
    reference: str
    """Human-readable reference (e.g. INC-123)"""
    severity: str
    """Severity of the incident"""
    slack_channel_id: str
    """Slack channel ID for the incident"""
    slack_channel_name: str
    """Slack channel name for the incident"""
    slack_team_id: str
    """Slack team/workspace ID"""
    summary: str
    """Detailed summary of the incident"""
    updated_at: str
    """When the incident was last updated"""
    visibility: str
    """Whether the incident is public or private"""
    workload_minutes_late: str
    """Minutes of workload classified as late"""
    workload_minutes_sleeping: str
    """Minutes of workload classified as sleeping"""
    workload_minutes_total: str
    """Total workload minutes"""
    workload_minutes_working: str
    """Minutes of workload classified as working"""


class IncidentsSortFilter(TypedDict, total=False):
    """Available fields for sorting incidents search results."""
    call_url: AirbyteSortOrder
    """URL of the call associated with the incident"""
    created_at: AirbyteSortOrder
    """When the incident was created"""
    creator: AirbyteSortOrder
    """The user who created the incident"""
    custom_field_entries: AirbyteSortOrder
    """Custom field values for the incident"""
    duration_metrics: AirbyteSortOrder
    """Duration metrics associated with the incident"""
    has_debrief: AirbyteSortOrder
    """Whether the incident has had a debrief"""
    id: AirbyteSortOrder
    """Unique identifier for the incident"""
    incident_role_assignments: AirbyteSortOrder
    """Role assignments for the incident"""
    incident_status: AirbyteSortOrder
    """Current status of the incident"""
    incident_timestamp_values: AirbyteSortOrder
    """Timestamp values for the incident"""
    incident_type: AirbyteSortOrder
    """Type of the incident"""
    mode: AirbyteSortOrder
    """Mode of the incident: standard, retrospective, test, or tutorial"""
    name: AirbyteSortOrder
    """Name/title of the incident"""
    permalink: AirbyteSortOrder
    """Link to the incident in the dashboard"""
    reference: AirbyteSortOrder
    """Human-readable reference (e.g. INC-123)"""
    severity: AirbyteSortOrder
    """Severity of the incident"""
    slack_channel_id: AirbyteSortOrder
    """Slack channel ID for the incident"""
    slack_channel_name: AirbyteSortOrder
    """Slack channel name for the incident"""
    slack_team_id: AirbyteSortOrder
    """Slack team/workspace ID"""
    summary: AirbyteSortOrder
    """Detailed summary of the incident"""
    updated_at: AirbyteSortOrder
    """When the incident was last updated"""
    visibility: AirbyteSortOrder
    """Whether the incident is public or private"""
    workload_minutes_late: AirbyteSortOrder
    """Minutes of workload classified as late"""
    workload_minutes_sleeping: AirbyteSortOrder
    """Minutes of workload classified as sleeping"""
    workload_minutes_total: AirbyteSortOrder
    """Total workload minutes"""
    workload_minutes_working: AirbyteSortOrder
    """Minutes of workload classified as working"""


# Entity-specific condition types for incidents
class IncidentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IncidentsSearchFilter


class IncidentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IncidentsSearchFilter


class IncidentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IncidentsSearchFilter


class IncidentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IncidentsSearchFilter


class IncidentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IncidentsSearchFilter


class IncidentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IncidentsSearchFilter


class IncidentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IncidentsStringFilter


class IncidentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IncidentsStringFilter


class IncidentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IncidentsStringFilter


class IncidentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IncidentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IncidentsInCondition = TypedDict("IncidentsInCondition", {"in": IncidentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IncidentsNotCondition = TypedDict("IncidentsNotCondition", {"not": "IncidentsCondition"}, total=False)
"""Negates the nested condition."""

IncidentsAndCondition = TypedDict("IncidentsAndCondition", {"and": "list[IncidentsCondition]"}, total=False)
"""True if all nested conditions are true."""

IncidentsOrCondition = TypedDict("IncidentsOrCondition", {"or": "list[IncidentsCondition]"}, total=False)
"""True if any nested condition is true."""

IncidentsAnyCondition = TypedDict("IncidentsAnyCondition", {"any": IncidentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all incidents condition types
IncidentsCondition = (
    IncidentsEqCondition
    | IncidentsNeqCondition
    | IncidentsGtCondition
    | IncidentsGteCondition
    | IncidentsLtCondition
    | IncidentsLteCondition
    | IncidentsInCondition
    | IncidentsLikeCondition
    | IncidentsFuzzyCondition
    | IncidentsKeywordCondition
    | IncidentsContainsCondition
    | IncidentsNotCondition
    | IncidentsAndCondition
    | IncidentsOrCondition
    | IncidentsAnyCondition
)


class IncidentsSearchQuery(TypedDict, total=False):
    """Search query for incidents entity."""
    filter: IncidentsCondition
    sort: list[IncidentsSortFilter]


# ===== ALERTS SEARCH TYPES =====

class AlertsSearchFilter(TypedDict, total=False):
    """Available fields for filtering alerts search queries."""
    alert_source_id: str | None
    """ID of the alert source that generated this alert"""
    attributes: list[Any] | None
    """Structured alert attributes"""
    created_at: str | None
    """When the alert was created"""
    deduplication_key: str | None
    """Deduplication key uniquely referencing this alert"""
    description: str | None
    """Description of the alert"""
    id: str | None
    """Unique identifier for the alert"""
    resolved_at: str | None
    """When the alert was resolved"""
    source_url: str | None
    """Link to the alert in the upstream system"""
    status: str | None
    """Status of the alert: firing or resolved"""
    title: str | None
    """Title of the alert"""
    updated_at: str | None
    """When the alert was last updated"""


class AlertsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    alert_source_id: list[str]
    """ID of the alert source that generated this alert"""
    attributes: list[list[Any]]
    """Structured alert attributes"""
    created_at: list[str]
    """When the alert was created"""
    deduplication_key: list[str]
    """Deduplication key uniquely referencing this alert"""
    description: list[str]
    """Description of the alert"""
    id: list[str]
    """Unique identifier for the alert"""
    resolved_at: list[str]
    """When the alert was resolved"""
    source_url: list[str]
    """Link to the alert in the upstream system"""
    status: list[str]
    """Status of the alert: firing or resolved"""
    title: list[str]
    """Title of the alert"""
    updated_at: list[str]
    """When the alert was last updated"""


class AlertsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    alert_source_id: Any
    """ID of the alert source that generated this alert"""
    attributes: Any
    """Structured alert attributes"""
    created_at: Any
    """When the alert was created"""
    deduplication_key: Any
    """Deduplication key uniquely referencing this alert"""
    description: Any
    """Description of the alert"""
    id: Any
    """Unique identifier for the alert"""
    resolved_at: Any
    """When the alert was resolved"""
    source_url: Any
    """Link to the alert in the upstream system"""
    status: Any
    """Status of the alert: firing or resolved"""
    title: Any
    """Title of the alert"""
    updated_at: Any
    """When the alert was last updated"""


class AlertsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    alert_source_id: str
    """ID of the alert source that generated this alert"""
    attributes: str
    """Structured alert attributes"""
    created_at: str
    """When the alert was created"""
    deduplication_key: str
    """Deduplication key uniquely referencing this alert"""
    description: str
    """Description of the alert"""
    id: str
    """Unique identifier for the alert"""
    resolved_at: str
    """When the alert was resolved"""
    source_url: str
    """Link to the alert in the upstream system"""
    status: str
    """Status of the alert: firing or resolved"""
    title: str
    """Title of the alert"""
    updated_at: str
    """When the alert was last updated"""


class AlertsSortFilter(TypedDict, total=False):
    """Available fields for sorting alerts search results."""
    alert_source_id: AirbyteSortOrder
    """ID of the alert source that generated this alert"""
    attributes: AirbyteSortOrder
    """Structured alert attributes"""
    created_at: AirbyteSortOrder
    """When the alert was created"""
    deduplication_key: AirbyteSortOrder
    """Deduplication key uniquely referencing this alert"""
    description: AirbyteSortOrder
    """Description of the alert"""
    id: AirbyteSortOrder
    """Unique identifier for the alert"""
    resolved_at: AirbyteSortOrder
    """When the alert was resolved"""
    source_url: AirbyteSortOrder
    """Link to the alert in the upstream system"""
    status: AirbyteSortOrder
    """Status of the alert: firing or resolved"""
    title: AirbyteSortOrder
    """Title of the alert"""
    updated_at: AirbyteSortOrder
    """When the alert was last updated"""


# Entity-specific condition types for alerts
class AlertsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AlertsSearchFilter


class AlertsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AlertsSearchFilter


class AlertsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AlertsSearchFilter


class AlertsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AlertsSearchFilter


class AlertsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AlertsSearchFilter


class AlertsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AlertsSearchFilter


class AlertsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AlertsStringFilter


class AlertsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AlertsStringFilter


class AlertsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AlertsStringFilter


class AlertsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AlertsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AlertsInCondition = TypedDict("AlertsInCondition", {"in": AlertsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AlertsNotCondition = TypedDict("AlertsNotCondition", {"not": "AlertsCondition"}, total=False)
"""Negates the nested condition."""

AlertsAndCondition = TypedDict("AlertsAndCondition", {"and": "list[AlertsCondition]"}, total=False)
"""True if all nested conditions are true."""

AlertsOrCondition = TypedDict("AlertsOrCondition", {"or": "list[AlertsCondition]"}, total=False)
"""True if any nested condition is true."""

AlertsAnyCondition = TypedDict("AlertsAnyCondition", {"any": AlertsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all alerts condition types
AlertsCondition = (
    AlertsEqCondition
    | AlertsNeqCondition
    | AlertsGtCondition
    | AlertsGteCondition
    | AlertsLtCondition
    | AlertsLteCondition
    | AlertsInCondition
    | AlertsLikeCondition
    | AlertsFuzzyCondition
    | AlertsKeywordCondition
    | AlertsContainsCondition
    | AlertsNotCondition
    | AlertsAndCondition
    | AlertsOrCondition
    | AlertsAnyCondition
)


class AlertsSearchQuery(TypedDict, total=False):
    """Search query for alerts entity."""
    filter: AlertsCondition
    sort: list[AlertsSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    base_role: dict[str, Any] | None
    """Base role assigned to the user"""
    custom_roles: list[Any] | None
    """Custom roles assigned to the user"""
    email: str | None
    """Email address of the user"""
    id: str | None
    """Unique identifier for the user"""
    name: str | None
    """Full name of the user"""
    role: str | None
    """Deprecated role field"""
    slack_user_id: str | None
    """Slack user ID"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    base_role: list[dict[str, Any]]
    """Base role assigned to the user"""
    custom_roles: list[list[Any]]
    """Custom roles assigned to the user"""
    email: list[str]
    """Email address of the user"""
    id: list[str]
    """Unique identifier for the user"""
    name: list[str]
    """Full name of the user"""
    role: list[str]
    """Deprecated role field"""
    slack_user_id: list[str]
    """Slack user ID"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    base_role: Any
    """Base role assigned to the user"""
    custom_roles: Any
    """Custom roles assigned to the user"""
    email: Any
    """Email address of the user"""
    id: Any
    """Unique identifier for the user"""
    name: Any
    """Full name of the user"""
    role: Any
    """Deprecated role field"""
    slack_user_id: Any
    """Slack user ID"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    base_role: str
    """Base role assigned to the user"""
    custom_roles: str
    """Custom roles assigned to the user"""
    email: str
    """Email address of the user"""
    id: str
    """Unique identifier for the user"""
    name: str
    """Full name of the user"""
    role: str
    """Deprecated role field"""
    slack_user_id: str
    """Slack user ID"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    base_role: AirbyteSortOrder
    """Base role assigned to the user"""
    custom_roles: AirbyteSortOrder
    """Custom roles assigned to the user"""
    email: AirbyteSortOrder
    """Email address of the user"""
    id: AirbyteSortOrder
    """Unique identifier for the user"""
    name: AirbyteSortOrder
    """Full name of the user"""
    role: AirbyteSortOrder
    """Deprecated role field"""
    slack_user_id: AirbyteSortOrder
    """Slack user ID"""


# Entity-specific condition types for users
class UsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UsersSearchFilter


class UsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UsersSearchFilter


class UsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UsersSearchFilter


class UsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UsersSearchFilter


class UsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UsersSearchFilter


class UsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UsersSearchFilter


class UsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: UsersStringFilter


class UsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsersStringFilter


class UsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsersStringFilter


class UsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: UsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UsersInCondition = TypedDict("UsersInCondition", {"in": UsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UsersNotCondition = TypedDict("UsersNotCondition", {"not": "UsersCondition"}, total=False)
"""Negates the nested condition."""

UsersAndCondition = TypedDict("UsersAndCondition", {"and": "list[UsersCondition]"}, total=False)
"""True if all nested conditions are true."""

UsersOrCondition = TypedDict("UsersOrCondition", {"or": "list[UsersCondition]"}, total=False)
"""True if any nested condition is true."""

UsersAnyCondition = TypedDict("UsersAnyCondition", {"any": UsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all users condition types
UsersCondition = (
    UsersEqCondition
    | UsersNeqCondition
    | UsersGtCondition
    | UsersGteCondition
    | UsersLtCondition
    | UsersLteCondition
    | UsersInCondition
    | UsersLikeCondition
    | UsersFuzzyCondition
    | UsersKeywordCondition
    | UsersContainsCondition
    | UsersNotCondition
    | UsersAndCondition
    | UsersOrCondition
    | UsersAnyCondition
)


class UsersSearchQuery(TypedDict, total=False):
    """Search query for users entity."""
    filter: UsersCondition
    sort: list[UsersSortFilter]


# ===== INCIDENT_UPDATES SEARCH TYPES =====

class IncidentUpdatesSearchFilter(TypedDict, total=False):
    """Available fields for filtering incident_updates search queries."""
    created_at: str | None
    """When the update was created"""
    id: str | None
    """Unique identifier for the incident update"""
    incident_id: str | None
    """ID of the incident this update belongs to"""
    message: str | None
    """Update message content"""
    new_incident_status: dict[str, Any] | None
    """New incident status set by this update"""
    new_severity: dict[str, Any] | None
    """New severity set by this update"""
    updater: dict[str, Any] | None
    """Who made this update"""


class IncidentUpdatesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """When the update was created"""
    id: list[str]
    """Unique identifier for the incident update"""
    incident_id: list[str]
    """ID of the incident this update belongs to"""
    message: list[str]
    """Update message content"""
    new_incident_status: list[dict[str, Any]]
    """New incident status set by this update"""
    new_severity: list[dict[str, Any]]
    """New severity set by this update"""
    updater: list[dict[str, Any]]
    """Who made this update"""


class IncidentUpdatesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """When the update was created"""
    id: Any
    """Unique identifier for the incident update"""
    incident_id: Any
    """ID of the incident this update belongs to"""
    message: Any
    """Update message content"""
    new_incident_status: Any
    """New incident status set by this update"""
    new_severity: Any
    """New severity set by this update"""
    updater: Any
    """Who made this update"""


class IncidentUpdatesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """When the update was created"""
    id: str
    """Unique identifier for the incident update"""
    incident_id: str
    """ID of the incident this update belongs to"""
    message: str
    """Update message content"""
    new_incident_status: str
    """New incident status set by this update"""
    new_severity: str
    """New severity set by this update"""
    updater: str
    """Who made this update"""


class IncidentUpdatesSortFilter(TypedDict, total=False):
    """Available fields for sorting incident_updates search results."""
    created_at: AirbyteSortOrder
    """When the update was created"""
    id: AirbyteSortOrder
    """Unique identifier for the incident update"""
    incident_id: AirbyteSortOrder
    """ID of the incident this update belongs to"""
    message: AirbyteSortOrder
    """Update message content"""
    new_incident_status: AirbyteSortOrder
    """New incident status set by this update"""
    new_severity: AirbyteSortOrder
    """New severity set by this update"""
    updater: AirbyteSortOrder
    """Who made this update"""


# Entity-specific condition types for incident_updates
class IncidentUpdatesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IncidentUpdatesSearchFilter


class IncidentUpdatesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IncidentUpdatesSearchFilter


class IncidentUpdatesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IncidentUpdatesSearchFilter


class IncidentUpdatesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IncidentUpdatesSearchFilter


class IncidentUpdatesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IncidentUpdatesSearchFilter


class IncidentUpdatesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IncidentUpdatesSearchFilter


class IncidentUpdatesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IncidentUpdatesStringFilter


class IncidentUpdatesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IncidentUpdatesStringFilter


class IncidentUpdatesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IncidentUpdatesStringFilter


class IncidentUpdatesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IncidentUpdatesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IncidentUpdatesInCondition = TypedDict("IncidentUpdatesInCondition", {"in": IncidentUpdatesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IncidentUpdatesNotCondition = TypedDict("IncidentUpdatesNotCondition", {"not": "IncidentUpdatesCondition"}, total=False)
"""Negates the nested condition."""

IncidentUpdatesAndCondition = TypedDict("IncidentUpdatesAndCondition", {"and": "list[IncidentUpdatesCondition]"}, total=False)
"""True if all nested conditions are true."""

IncidentUpdatesOrCondition = TypedDict("IncidentUpdatesOrCondition", {"or": "list[IncidentUpdatesCondition]"}, total=False)
"""True if any nested condition is true."""

IncidentUpdatesAnyCondition = TypedDict("IncidentUpdatesAnyCondition", {"any": IncidentUpdatesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all incident_updates condition types
IncidentUpdatesCondition = (
    IncidentUpdatesEqCondition
    | IncidentUpdatesNeqCondition
    | IncidentUpdatesGtCondition
    | IncidentUpdatesGteCondition
    | IncidentUpdatesLtCondition
    | IncidentUpdatesLteCondition
    | IncidentUpdatesInCondition
    | IncidentUpdatesLikeCondition
    | IncidentUpdatesFuzzyCondition
    | IncidentUpdatesKeywordCondition
    | IncidentUpdatesContainsCondition
    | IncidentUpdatesNotCondition
    | IncidentUpdatesAndCondition
    | IncidentUpdatesOrCondition
    | IncidentUpdatesAnyCondition
)


class IncidentUpdatesSearchQuery(TypedDict, total=False):
    """Search query for incident_updates entity."""
    filter: IncidentUpdatesCondition
    sort: list[IncidentUpdatesSortFilter]


# ===== INCIDENT_ROLES SEARCH TYPES =====

class IncidentRolesSearchFilter(TypedDict, total=False):
    """Available fields for filtering incident_roles search queries."""
    created_at: str | None
    """When the role was created"""
    description: str | None
    """Description of the role"""
    id: str | None
    """Unique identifier for the incident role"""
    instructions: str | None
    """Instructions for the role holder"""
    name: str | None
    """Name of the role"""
    required: bool | None
    """Whether this role must be assigned"""
    role_type: str | None
    """Type of role"""
    shortform: str | None
    """Short form label for the role"""
    updated_at: str | None
    """When the role was last updated"""


class IncidentRolesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """When the role was created"""
    description: list[str]
    """Description of the role"""
    id: list[str]
    """Unique identifier for the incident role"""
    instructions: list[str]
    """Instructions for the role holder"""
    name: list[str]
    """Name of the role"""
    required: list[bool]
    """Whether this role must be assigned"""
    role_type: list[str]
    """Type of role"""
    shortform: list[str]
    """Short form label for the role"""
    updated_at: list[str]
    """When the role was last updated"""


class IncidentRolesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """When the role was created"""
    description: Any
    """Description of the role"""
    id: Any
    """Unique identifier for the incident role"""
    instructions: Any
    """Instructions for the role holder"""
    name: Any
    """Name of the role"""
    required: Any
    """Whether this role must be assigned"""
    role_type: Any
    """Type of role"""
    shortform: Any
    """Short form label for the role"""
    updated_at: Any
    """When the role was last updated"""


class IncidentRolesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """When the role was created"""
    description: str
    """Description of the role"""
    id: str
    """Unique identifier for the incident role"""
    instructions: str
    """Instructions for the role holder"""
    name: str
    """Name of the role"""
    required: str
    """Whether this role must be assigned"""
    role_type: str
    """Type of role"""
    shortform: str
    """Short form label for the role"""
    updated_at: str
    """When the role was last updated"""


class IncidentRolesSortFilter(TypedDict, total=False):
    """Available fields for sorting incident_roles search results."""
    created_at: AirbyteSortOrder
    """When the role was created"""
    description: AirbyteSortOrder
    """Description of the role"""
    id: AirbyteSortOrder
    """Unique identifier for the incident role"""
    instructions: AirbyteSortOrder
    """Instructions for the role holder"""
    name: AirbyteSortOrder
    """Name of the role"""
    required: AirbyteSortOrder
    """Whether this role must be assigned"""
    role_type: AirbyteSortOrder
    """Type of role"""
    shortform: AirbyteSortOrder
    """Short form label for the role"""
    updated_at: AirbyteSortOrder
    """When the role was last updated"""


# Entity-specific condition types for incident_roles
class IncidentRolesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IncidentRolesSearchFilter


class IncidentRolesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IncidentRolesSearchFilter


class IncidentRolesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IncidentRolesSearchFilter


class IncidentRolesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IncidentRolesSearchFilter


class IncidentRolesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IncidentRolesSearchFilter


class IncidentRolesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IncidentRolesSearchFilter


class IncidentRolesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IncidentRolesStringFilter


class IncidentRolesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IncidentRolesStringFilter


class IncidentRolesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IncidentRolesStringFilter


class IncidentRolesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IncidentRolesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IncidentRolesInCondition = TypedDict("IncidentRolesInCondition", {"in": IncidentRolesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IncidentRolesNotCondition = TypedDict("IncidentRolesNotCondition", {"not": "IncidentRolesCondition"}, total=False)
"""Negates the nested condition."""

IncidentRolesAndCondition = TypedDict("IncidentRolesAndCondition", {"and": "list[IncidentRolesCondition]"}, total=False)
"""True if all nested conditions are true."""

IncidentRolesOrCondition = TypedDict("IncidentRolesOrCondition", {"or": "list[IncidentRolesCondition]"}, total=False)
"""True if any nested condition is true."""

IncidentRolesAnyCondition = TypedDict("IncidentRolesAnyCondition", {"any": IncidentRolesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all incident_roles condition types
IncidentRolesCondition = (
    IncidentRolesEqCondition
    | IncidentRolesNeqCondition
    | IncidentRolesGtCondition
    | IncidentRolesGteCondition
    | IncidentRolesLtCondition
    | IncidentRolesLteCondition
    | IncidentRolesInCondition
    | IncidentRolesLikeCondition
    | IncidentRolesFuzzyCondition
    | IncidentRolesKeywordCondition
    | IncidentRolesContainsCondition
    | IncidentRolesNotCondition
    | IncidentRolesAndCondition
    | IncidentRolesOrCondition
    | IncidentRolesAnyCondition
)


class IncidentRolesSearchQuery(TypedDict, total=False):
    """Search query for incident_roles entity."""
    filter: IncidentRolesCondition
    sort: list[IncidentRolesSortFilter]


# ===== INCIDENT_STATUSES SEARCH TYPES =====

class IncidentStatusesSearchFilter(TypedDict, total=False):
    """Available fields for filtering incident_statuses search queries."""
    category: str | None
    """Category: triage, active, post-incident, closed, etc."""
    created_at: str | None
    """When the status was created"""
    description: str | None
    """Description of the status"""
    id: str | None
    """Unique identifier for the status"""
    name: str | None
    """Name of the status"""
    rank: float | None
    """Rank for ordering"""
    updated_at: str | None
    """When the status was last updated"""


class IncidentStatusesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    category: list[str]
    """Category: triage, active, post-incident, closed, etc."""
    created_at: list[str]
    """When the status was created"""
    description: list[str]
    """Description of the status"""
    id: list[str]
    """Unique identifier for the status"""
    name: list[str]
    """Name of the status"""
    rank: list[float]
    """Rank for ordering"""
    updated_at: list[str]
    """When the status was last updated"""


class IncidentStatusesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    category: Any
    """Category: triage, active, post-incident, closed, etc."""
    created_at: Any
    """When the status was created"""
    description: Any
    """Description of the status"""
    id: Any
    """Unique identifier for the status"""
    name: Any
    """Name of the status"""
    rank: Any
    """Rank for ordering"""
    updated_at: Any
    """When the status was last updated"""


class IncidentStatusesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    category: str
    """Category: triage, active, post-incident, closed, etc."""
    created_at: str
    """When the status was created"""
    description: str
    """Description of the status"""
    id: str
    """Unique identifier for the status"""
    name: str
    """Name of the status"""
    rank: str
    """Rank for ordering"""
    updated_at: str
    """When the status was last updated"""


class IncidentStatusesSortFilter(TypedDict, total=False):
    """Available fields for sorting incident_statuses search results."""
    category: AirbyteSortOrder
    """Category: triage, active, post-incident, closed, etc."""
    created_at: AirbyteSortOrder
    """When the status was created"""
    description: AirbyteSortOrder
    """Description of the status"""
    id: AirbyteSortOrder
    """Unique identifier for the status"""
    name: AirbyteSortOrder
    """Name of the status"""
    rank: AirbyteSortOrder
    """Rank for ordering"""
    updated_at: AirbyteSortOrder
    """When the status was last updated"""


# Entity-specific condition types for incident_statuses
class IncidentStatusesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IncidentStatusesSearchFilter


class IncidentStatusesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IncidentStatusesSearchFilter


class IncidentStatusesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IncidentStatusesSearchFilter


class IncidentStatusesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IncidentStatusesSearchFilter


class IncidentStatusesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IncidentStatusesSearchFilter


class IncidentStatusesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IncidentStatusesSearchFilter


class IncidentStatusesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IncidentStatusesStringFilter


class IncidentStatusesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IncidentStatusesStringFilter


class IncidentStatusesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IncidentStatusesStringFilter


class IncidentStatusesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IncidentStatusesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IncidentStatusesInCondition = TypedDict("IncidentStatusesInCondition", {"in": IncidentStatusesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IncidentStatusesNotCondition = TypedDict("IncidentStatusesNotCondition", {"not": "IncidentStatusesCondition"}, total=False)
"""Negates the nested condition."""

IncidentStatusesAndCondition = TypedDict("IncidentStatusesAndCondition", {"and": "list[IncidentStatusesCondition]"}, total=False)
"""True if all nested conditions are true."""

IncidentStatusesOrCondition = TypedDict("IncidentStatusesOrCondition", {"or": "list[IncidentStatusesCondition]"}, total=False)
"""True if any nested condition is true."""

IncidentStatusesAnyCondition = TypedDict("IncidentStatusesAnyCondition", {"any": IncidentStatusesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all incident_statuses condition types
IncidentStatusesCondition = (
    IncidentStatusesEqCondition
    | IncidentStatusesNeqCondition
    | IncidentStatusesGtCondition
    | IncidentStatusesGteCondition
    | IncidentStatusesLtCondition
    | IncidentStatusesLteCondition
    | IncidentStatusesInCondition
    | IncidentStatusesLikeCondition
    | IncidentStatusesFuzzyCondition
    | IncidentStatusesKeywordCondition
    | IncidentStatusesContainsCondition
    | IncidentStatusesNotCondition
    | IncidentStatusesAndCondition
    | IncidentStatusesOrCondition
    | IncidentStatusesAnyCondition
)


class IncidentStatusesSearchQuery(TypedDict, total=False):
    """Search query for incident_statuses entity."""
    filter: IncidentStatusesCondition
    sort: list[IncidentStatusesSortFilter]


# ===== INCIDENT_TIMESTAMPS SEARCH TYPES =====

class IncidentTimestampsSearchFilter(TypedDict, total=False):
    """Available fields for filtering incident_timestamps search queries."""
    id: str | None
    """Unique identifier for the timestamp"""
    name: str | None
    """Name of the timestamp"""
    rank: float | None
    """Rank for ordering"""


class IncidentTimestampsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the timestamp"""
    name: list[str]
    """Name of the timestamp"""
    rank: list[float]
    """Rank for ordering"""


class IncidentTimestampsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the timestamp"""
    name: Any
    """Name of the timestamp"""
    rank: Any
    """Rank for ordering"""


class IncidentTimestampsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier for the timestamp"""
    name: str
    """Name of the timestamp"""
    rank: str
    """Rank for ordering"""


class IncidentTimestampsSortFilter(TypedDict, total=False):
    """Available fields for sorting incident_timestamps search results."""
    id: AirbyteSortOrder
    """Unique identifier for the timestamp"""
    name: AirbyteSortOrder
    """Name of the timestamp"""
    rank: AirbyteSortOrder
    """Rank for ordering"""


# Entity-specific condition types for incident_timestamps
class IncidentTimestampsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IncidentTimestampsSearchFilter


class IncidentTimestampsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IncidentTimestampsSearchFilter


class IncidentTimestampsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IncidentTimestampsSearchFilter


class IncidentTimestampsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IncidentTimestampsSearchFilter


class IncidentTimestampsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IncidentTimestampsSearchFilter


class IncidentTimestampsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IncidentTimestampsSearchFilter


class IncidentTimestampsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IncidentTimestampsStringFilter


class IncidentTimestampsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IncidentTimestampsStringFilter


class IncidentTimestampsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IncidentTimestampsStringFilter


class IncidentTimestampsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IncidentTimestampsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IncidentTimestampsInCondition = TypedDict("IncidentTimestampsInCondition", {"in": IncidentTimestampsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IncidentTimestampsNotCondition = TypedDict("IncidentTimestampsNotCondition", {"not": "IncidentTimestampsCondition"}, total=False)
"""Negates the nested condition."""

IncidentTimestampsAndCondition = TypedDict("IncidentTimestampsAndCondition", {"and": "list[IncidentTimestampsCondition]"}, total=False)
"""True if all nested conditions are true."""

IncidentTimestampsOrCondition = TypedDict("IncidentTimestampsOrCondition", {"or": "list[IncidentTimestampsCondition]"}, total=False)
"""True if any nested condition is true."""

IncidentTimestampsAnyCondition = TypedDict("IncidentTimestampsAnyCondition", {"any": IncidentTimestampsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all incident_timestamps condition types
IncidentTimestampsCondition = (
    IncidentTimestampsEqCondition
    | IncidentTimestampsNeqCondition
    | IncidentTimestampsGtCondition
    | IncidentTimestampsGteCondition
    | IncidentTimestampsLtCondition
    | IncidentTimestampsLteCondition
    | IncidentTimestampsInCondition
    | IncidentTimestampsLikeCondition
    | IncidentTimestampsFuzzyCondition
    | IncidentTimestampsKeywordCondition
    | IncidentTimestampsContainsCondition
    | IncidentTimestampsNotCondition
    | IncidentTimestampsAndCondition
    | IncidentTimestampsOrCondition
    | IncidentTimestampsAnyCondition
)


class IncidentTimestampsSearchQuery(TypedDict, total=False):
    """Search query for incident_timestamps entity."""
    filter: IncidentTimestampsCondition
    sort: list[IncidentTimestampsSortFilter]


# ===== SEVERITIES SEARCH TYPES =====

class SeveritiesSearchFilter(TypedDict, total=False):
    """Available fields for filtering severities search queries."""
    created_at: str | None
    """When the severity was created"""
    description: str | None
    """Description of the severity"""
    id: str | None
    """Unique identifier for the severity"""
    name: str | None
    """Name of the severity"""
    rank: float | None
    """Rank for ordering"""
    updated_at: str | None
    """When the severity was last updated"""


class SeveritiesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """When the severity was created"""
    description: list[str]
    """Description of the severity"""
    id: list[str]
    """Unique identifier for the severity"""
    name: list[str]
    """Name of the severity"""
    rank: list[float]
    """Rank for ordering"""
    updated_at: list[str]
    """When the severity was last updated"""


class SeveritiesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """When the severity was created"""
    description: Any
    """Description of the severity"""
    id: Any
    """Unique identifier for the severity"""
    name: Any
    """Name of the severity"""
    rank: Any
    """Rank for ordering"""
    updated_at: Any
    """When the severity was last updated"""


class SeveritiesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """When the severity was created"""
    description: str
    """Description of the severity"""
    id: str
    """Unique identifier for the severity"""
    name: str
    """Name of the severity"""
    rank: str
    """Rank for ordering"""
    updated_at: str
    """When the severity was last updated"""


class SeveritiesSortFilter(TypedDict, total=False):
    """Available fields for sorting severities search results."""
    created_at: AirbyteSortOrder
    """When the severity was created"""
    description: AirbyteSortOrder
    """Description of the severity"""
    id: AirbyteSortOrder
    """Unique identifier for the severity"""
    name: AirbyteSortOrder
    """Name of the severity"""
    rank: AirbyteSortOrder
    """Rank for ordering"""
    updated_at: AirbyteSortOrder
    """When the severity was last updated"""


# Entity-specific condition types for severities
class SeveritiesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SeveritiesSearchFilter


class SeveritiesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SeveritiesSearchFilter


class SeveritiesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SeveritiesSearchFilter


class SeveritiesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SeveritiesSearchFilter


class SeveritiesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SeveritiesSearchFilter


class SeveritiesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SeveritiesSearchFilter


class SeveritiesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SeveritiesStringFilter


class SeveritiesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SeveritiesStringFilter


class SeveritiesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SeveritiesStringFilter


class SeveritiesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SeveritiesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SeveritiesInCondition = TypedDict("SeveritiesInCondition", {"in": SeveritiesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SeveritiesNotCondition = TypedDict("SeveritiesNotCondition", {"not": "SeveritiesCondition"}, total=False)
"""Negates the nested condition."""

SeveritiesAndCondition = TypedDict("SeveritiesAndCondition", {"and": "list[SeveritiesCondition]"}, total=False)
"""True if all nested conditions are true."""

SeveritiesOrCondition = TypedDict("SeveritiesOrCondition", {"or": "list[SeveritiesCondition]"}, total=False)
"""True if any nested condition is true."""

SeveritiesAnyCondition = TypedDict("SeveritiesAnyCondition", {"any": SeveritiesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all severities condition types
SeveritiesCondition = (
    SeveritiesEqCondition
    | SeveritiesNeqCondition
    | SeveritiesGtCondition
    | SeveritiesGteCondition
    | SeveritiesLtCondition
    | SeveritiesLteCondition
    | SeveritiesInCondition
    | SeveritiesLikeCondition
    | SeveritiesFuzzyCondition
    | SeveritiesKeywordCondition
    | SeveritiesContainsCondition
    | SeveritiesNotCondition
    | SeveritiesAndCondition
    | SeveritiesOrCondition
    | SeveritiesAnyCondition
)


class SeveritiesSearchQuery(TypedDict, total=False):
    """Search query for severities entity."""
    filter: SeveritiesCondition
    sort: list[SeveritiesSortFilter]


# ===== CUSTOM_FIELDS SEARCH TYPES =====

class CustomFieldsSearchFilter(TypedDict, total=False):
    """Available fields for filtering custom_fields search queries."""
    catalog_type_id: str | None
    """ID of the catalog type associated with this custom field"""
    created_at: str | None
    """When the custom field was created"""
    description: str | None
    """Description of the custom field"""
    field_type: str | None
    """Type of field"""
    id: str | None
    """Unique identifier for the custom field"""
    name: str | None
    """Name of the custom field"""
    updated_at: str | None
    """When the custom field was last updated"""


class CustomFieldsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    catalog_type_id: list[str]
    """ID of the catalog type associated with this custom field"""
    created_at: list[str]
    """When the custom field was created"""
    description: list[str]
    """Description of the custom field"""
    field_type: list[str]
    """Type of field"""
    id: list[str]
    """Unique identifier for the custom field"""
    name: list[str]
    """Name of the custom field"""
    updated_at: list[str]
    """When the custom field was last updated"""


class CustomFieldsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    catalog_type_id: Any
    """ID of the catalog type associated with this custom field"""
    created_at: Any
    """When the custom field was created"""
    description: Any
    """Description of the custom field"""
    field_type: Any
    """Type of field"""
    id: Any
    """Unique identifier for the custom field"""
    name: Any
    """Name of the custom field"""
    updated_at: Any
    """When the custom field was last updated"""


class CustomFieldsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    catalog_type_id: str
    """ID of the catalog type associated with this custom field"""
    created_at: str
    """When the custom field was created"""
    description: str
    """Description of the custom field"""
    field_type: str
    """Type of field"""
    id: str
    """Unique identifier for the custom field"""
    name: str
    """Name of the custom field"""
    updated_at: str
    """When the custom field was last updated"""


class CustomFieldsSortFilter(TypedDict, total=False):
    """Available fields for sorting custom_fields search results."""
    catalog_type_id: AirbyteSortOrder
    """ID of the catalog type associated with this custom field"""
    created_at: AirbyteSortOrder
    """When the custom field was created"""
    description: AirbyteSortOrder
    """Description of the custom field"""
    field_type: AirbyteSortOrder
    """Type of field"""
    id: AirbyteSortOrder
    """Unique identifier for the custom field"""
    name: AirbyteSortOrder
    """Name of the custom field"""
    updated_at: AirbyteSortOrder
    """When the custom field was last updated"""


# Entity-specific condition types for custom_fields
class CustomFieldsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CustomFieldsSearchFilter


class CustomFieldsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CustomFieldsSearchFilter


class CustomFieldsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CustomFieldsSearchFilter


class CustomFieldsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CustomFieldsSearchFilter


class CustomFieldsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CustomFieldsSearchFilter


class CustomFieldsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CustomFieldsSearchFilter


class CustomFieldsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CustomFieldsStringFilter


class CustomFieldsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CustomFieldsStringFilter


class CustomFieldsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CustomFieldsStringFilter


class CustomFieldsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CustomFieldsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CustomFieldsInCondition = TypedDict("CustomFieldsInCondition", {"in": CustomFieldsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CustomFieldsNotCondition = TypedDict("CustomFieldsNotCondition", {"not": "CustomFieldsCondition"}, total=False)
"""Negates the nested condition."""

CustomFieldsAndCondition = TypedDict("CustomFieldsAndCondition", {"and": "list[CustomFieldsCondition]"}, total=False)
"""True if all nested conditions are true."""

CustomFieldsOrCondition = TypedDict("CustomFieldsOrCondition", {"or": "list[CustomFieldsCondition]"}, total=False)
"""True if any nested condition is true."""

CustomFieldsAnyCondition = TypedDict("CustomFieldsAnyCondition", {"any": CustomFieldsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all custom_fields condition types
CustomFieldsCondition = (
    CustomFieldsEqCondition
    | CustomFieldsNeqCondition
    | CustomFieldsGtCondition
    | CustomFieldsGteCondition
    | CustomFieldsLtCondition
    | CustomFieldsLteCondition
    | CustomFieldsInCondition
    | CustomFieldsLikeCondition
    | CustomFieldsFuzzyCondition
    | CustomFieldsKeywordCondition
    | CustomFieldsContainsCondition
    | CustomFieldsNotCondition
    | CustomFieldsAndCondition
    | CustomFieldsOrCondition
    | CustomFieldsAnyCondition
)


class CustomFieldsSearchQuery(TypedDict, total=False):
    """Search query for custom_fields entity."""
    filter: CustomFieldsCondition
    sort: list[CustomFieldsSortFilter]


# ===== CATALOG_TYPES SEARCH TYPES =====

class CatalogTypesSearchFilter(TypedDict, total=False):
    """Available fields for filtering catalog_types search queries."""
    annotations: dict[str, Any] | None
    """Annotations metadata"""
    categories: list[Any] | None
    """Categories this type belongs to"""
    color: str | None
    """Display color"""
    created_at: str | None
    """When the catalog type was created"""
    description: str | None
    """Description of the catalog type"""
    icon: str | None
    """Display icon"""
    id: str | None
    """Unique identifier for the catalog type"""
    is_editable: bool | None
    """Whether entries can be edited"""
    last_synced_at: str | None
    """When the catalog type was last synced"""
    name: str | None
    """Name of the catalog type"""
    ranked: bool | None
    """Whether entries are ranked"""
    registry_type: str | None
    """Registry type if synced from an integration"""
    required_integrations: list[Any] | None
    """Integrations required for this type"""
    schema_: dict[str, Any] | None
    """Schema definition for the catalog type"""
    semantic_type: str | None
    """Semantic type for special behavior"""
    type_name: str | None
    """Programmatic type name"""
    updated_at: str | None
    """When the catalog type was last updated"""


class CatalogTypesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    annotations: list[dict[str, Any]]
    """Annotations metadata"""
    categories: list[list[Any]]
    """Categories this type belongs to"""
    color: list[str]
    """Display color"""
    created_at: list[str]
    """When the catalog type was created"""
    description: list[str]
    """Description of the catalog type"""
    icon: list[str]
    """Display icon"""
    id: list[str]
    """Unique identifier for the catalog type"""
    is_editable: list[bool]
    """Whether entries can be edited"""
    last_synced_at: list[str]
    """When the catalog type was last synced"""
    name: list[str]
    """Name of the catalog type"""
    ranked: list[bool]
    """Whether entries are ranked"""
    registry_type: list[str]
    """Registry type if synced from an integration"""
    required_integrations: list[list[Any]]
    """Integrations required for this type"""
    schema_: list[dict[str, Any]]
    """Schema definition for the catalog type"""
    semantic_type: list[str]
    """Semantic type for special behavior"""
    type_name: list[str]
    """Programmatic type name"""
    updated_at: list[str]
    """When the catalog type was last updated"""


class CatalogTypesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    annotations: Any
    """Annotations metadata"""
    categories: Any
    """Categories this type belongs to"""
    color: Any
    """Display color"""
    created_at: Any
    """When the catalog type was created"""
    description: Any
    """Description of the catalog type"""
    icon: Any
    """Display icon"""
    id: Any
    """Unique identifier for the catalog type"""
    is_editable: Any
    """Whether entries can be edited"""
    last_synced_at: Any
    """When the catalog type was last synced"""
    name: Any
    """Name of the catalog type"""
    ranked: Any
    """Whether entries are ranked"""
    registry_type: Any
    """Registry type if synced from an integration"""
    required_integrations: Any
    """Integrations required for this type"""
    schema_: Any
    """Schema definition for the catalog type"""
    semantic_type: Any
    """Semantic type for special behavior"""
    type_name: Any
    """Programmatic type name"""
    updated_at: Any
    """When the catalog type was last updated"""


class CatalogTypesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    annotations: str
    """Annotations metadata"""
    categories: str
    """Categories this type belongs to"""
    color: str
    """Display color"""
    created_at: str
    """When the catalog type was created"""
    description: str
    """Description of the catalog type"""
    icon: str
    """Display icon"""
    id: str
    """Unique identifier for the catalog type"""
    is_editable: str
    """Whether entries can be edited"""
    last_synced_at: str
    """When the catalog type was last synced"""
    name: str
    """Name of the catalog type"""
    ranked: str
    """Whether entries are ranked"""
    registry_type: str
    """Registry type if synced from an integration"""
    required_integrations: str
    """Integrations required for this type"""
    schema_: str
    """Schema definition for the catalog type"""
    semantic_type: str
    """Semantic type for special behavior"""
    type_name: str
    """Programmatic type name"""
    updated_at: str
    """When the catalog type was last updated"""


class CatalogTypesSortFilter(TypedDict, total=False):
    """Available fields for sorting catalog_types search results."""
    annotations: AirbyteSortOrder
    """Annotations metadata"""
    categories: AirbyteSortOrder
    """Categories this type belongs to"""
    color: AirbyteSortOrder
    """Display color"""
    created_at: AirbyteSortOrder
    """When the catalog type was created"""
    description: AirbyteSortOrder
    """Description of the catalog type"""
    icon: AirbyteSortOrder
    """Display icon"""
    id: AirbyteSortOrder
    """Unique identifier for the catalog type"""
    is_editable: AirbyteSortOrder
    """Whether entries can be edited"""
    last_synced_at: AirbyteSortOrder
    """When the catalog type was last synced"""
    name: AirbyteSortOrder
    """Name of the catalog type"""
    ranked: AirbyteSortOrder
    """Whether entries are ranked"""
    registry_type: AirbyteSortOrder
    """Registry type if synced from an integration"""
    required_integrations: AirbyteSortOrder
    """Integrations required for this type"""
    schema_: AirbyteSortOrder
    """Schema definition for the catalog type"""
    semantic_type: AirbyteSortOrder
    """Semantic type for special behavior"""
    type_name: AirbyteSortOrder
    """Programmatic type name"""
    updated_at: AirbyteSortOrder
    """When the catalog type was last updated"""


# Entity-specific condition types for catalog_types
class CatalogTypesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CatalogTypesSearchFilter


class CatalogTypesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CatalogTypesSearchFilter


class CatalogTypesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CatalogTypesSearchFilter


class CatalogTypesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CatalogTypesSearchFilter


class CatalogTypesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CatalogTypesSearchFilter


class CatalogTypesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CatalogTypesSearchFilter


class CatalogTypesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CatalogTypesStringFilter


class CatalogTypesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CatalogTypesStringFilter


class CatalogTypesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CatalogTypesStringFilter


class CatalogTypesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CatalogTypesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CatalogTypesInCondition = TypedDict("CatalogTypesInCondition", {"in": CatalogTypesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CatalogTypesNotCondition = TypedDict("CatalogTypesNotCondition", {"not": "CatalogTypesCondition"}, total=False)
"""Negates the nested condition."""

CatalogTypesAndCondition = TypedDict("CatalogTypesAndCondition", {"and": "list[CatalogTypesCondition]"}, total=False)
"""True if all nested conditions are true."""

CatalogTypesOrCondition = TypedDict("CatalogTypesOrCondition", {"or": "list[CatalogTypesCondition]"}, total=False)
"""True if any nested condition is true."""

CatalogTypesAnyCondition = TypedDict("CatalogTypesAnyCondition", {"any": CatalogTypesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all catalog_types condition types
CatalogTypesCondition = (
    CatalogTypesEqCondition
    | CatalogTypesNeqCondition
    | CatalogTypesGtCondition
    | CatalogTypesGteCondition
    | CatalogTypesLtCondition
    | CatalogTypesLteCondition
    | CatalogTypesInCondition
    | CatalogTypesLikeCondition
    | CatalogTypesFuzzyCondition
    | CatalogTypesKeywordCondition
    | CatalogTypesContainsCondition
    | CatalogTypesNotCondition
    | CatalogTypesAndCondition
    | CatalogTypesOrCondition
    | CatalogTypesAnyCondition
)


class CatalogTypesSearchQuery(TypedDict, total=False):
    """Search query for catalog_types entity."""
    filter: CatalogTypesCondition
    sort: list[CatalogTypesSortFilter]


# ===== SCHEDULES SEARCH TYPES =====

class SchedulesSearchFilter(TypedDict, total=False):
    """Available fields for filtering schedules search queries."""
    annotations: dict[str, Any] | None
    """Annotations metadata"""
    config: dict[str, Any] | None
    """Schedule configuration with rotations"""
    created_at: str | None
    """When the schedule was created"""
    current_shifts: list[Any] | None
    """Currently active shifts"""
    holidays_public_config: dict[str, Any] | None
    """Public holiday configuration for the schedule"""
    id: str | None
    """Unique identifier for the schedule"""
    name: str | None
    """Name of the schedule"""
    team_ids: list[Any] | None
    """IDs of teams associated with this schedule"""
    timezone: str | None
    """Timezone for the schedule"""
    updated_at: str | None
    """When the schedule was last updated"""


class SchedulesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    annotations: list[dict[str, Any]]
    """Annotations metadata"""
    config: list[dict[str, Any]]
    """Schedule configuration with rotations"""
    created_at: list[str]
    """When the schedule was created"""
    current_shifts: list[list[Any]]
    """Currently active shifts"""
    holidays_public_config: list[dict[str, Any]]
    """Public holiday configuration for the schedule"""
    id: list[str]
    """Unique identifier for the schedule"""
    name: list[str]
    """Name of the schedule"""
    team_ids: list[list[Any]]
    """IDs of teams associated with this schedule"""
    timezone: list[str]
    """Timezone for the schedule"""
    updated_at: list[str]
    """When the schedule was last updated"""


class SchedulesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    annotations: Any
    """Annotations metadata"""
    config: Any
    """Schedule configuration with rotations"""
    created_at: Any
    """When the schedule was created"""
    current_shifts: Any
    """Currently active shifts"""
    holidays_public_config: Any
    """Public holiday configuration for the schedule"""
    id: Any
    """Unique identifier for the schedule"""
    name: Any
    """Name of the schedule"""
    team_ids: Any
    """IDs of teams associated with this schedule"""
    timezone: Any
    """Timezone for the schedule"""
    updated_at: Any
    """When the schedule was last updated"""


class SchedulesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    annotations: str
    """Annotations metadata"""
    config: str
    """Schedule configuration with rotations"""
    created_at: str
    """When the schedule was created"""
    current_shifts: str
    """Currently active shifts"""
    holidays_public_config: str
    """Public holiday configuration for the schedule"""
    id: str
    """Unique identifier for the schedule"""
    name: str
    """Name of the schedule"""
    team_ids: str
    """IDs of teams associated with this schedule"""
    timezone: str
    """Timezone for the schedule"""
    updated_at: str
    """When the schedule was last updated"""


class SchedulesSortFilter(TypedDict, total=False):
    """Available fields for sorting schedules search results."""
    annotations: AirbyteSortOrder
    """Annotations metadata"""
    config: AirbyteSortOrder
    """Schedule configuration with rotations"""
    created_at: AirbyteSortOrder
    """When the schedule was created"""
    current_shifts: AirbyteSortOrder
    """Currently active shifts"""
    holidays_public_config: AirbyteSortOrder
    """Public holiday configuration for the schedule"""
    id: AirbyteSortOrder
    """Unique identifier for the schedule"""
    name: AirbyteSortOrder
    """Name of the schedule"""
    team_ids: AirbyteSortOrder
    """IDs of teams associated with this schedule"""
    timezone: AirbyteSortOrder
    """Timezone for the schedule"""
    updated_at: AirbyteSortOrder
    """When the schedule was last updated"""


# Entity-specific condition types for schedules
class SchedulesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SchedulesSearchFilter


class SchedulesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SchedulesSearchFilter


class SchedulesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SchedulesSearchFilter


class SchedulesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SchedulesSearchFilter


class SchedulesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SchedulesSearchFilter


class SchedulesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SchedulesSearchFilter


class SchedulesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SchedulesStringFilter


class SchedulesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SchedulesStringFilter


class SchedulesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SchedulesStringFilter


class SchedulesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SchedulesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SchedulesInCondition = TypedDict("SchedulesInCondition", {"in": SchedulesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SchedulesNotCondition = TypedDict("SchedulesNotCondition", {"not": "SchedulesCondition"}, total=False)
"""Negates the nested condition."""

SchedulesAndCondition = TypedDict("SchedulesAndCondition", {"and": "list[SchedulesCondition]"}, total=False)
"""True if all nested conditions are true."""

SchedulesOrCondition = TypedDict("SchedulesOrCondition", {"or": "list[SchedulesCondition]"}, total=False)
"""True if any nested condition is true."""

SchedulesAnyCondition = TypedDict("SchedulesAnyCondition", {"any": SchedulesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all schedules condition types
SchedulesCondition = (
    SchedulesEqCondition
    | SchedulesNeqCondition
    | SchedulesGtCondition
    | SchedulesGteCondition
    | SchedulesLtCondition
    | SchedulesLteCondition
    | SchedulesInCondition
    | SchedulesLikeCondition
    | SchedulesFuzzyCondition
    | SchedulesKeywordCondition
    | SchedulesContainsCondition
    | SchedulesNotCondition
    | SchedulesAndCondition
    | SchedulesOrCondition
    | SchedulesAnyCondition
)


class SchedulesSearchQuery(TypedDict, total=False):
    """Search query for schedules entity."""
    filter: SchedulesCondition
    sort: list[SchedulesSortFilter]


# ===== ESCALATIONS SEARCH TYPES =====

class EscalationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering escalations search queries."""
    created_at: str | None
    """When the escalation was created"""
    creator: dict[str, Any] | None
    """The creator of this escalation"""
    escalation_path_id: str | None
    """ID of the escalation path used"""
    events: list[Any] | None
    """History of escalation events"""
    id: str | None
    """Unique identifier for the escalation"""
    priority: dict[str, Any] | None
    """Priority of the escalation"""
    related_alerts: list[Any] | None
    """Alerts related to this escalation"""
    related_incidents: list[Any] | None
    """Incidents related to this escalation"""
    status: str | None
    """Status: pending, triggered, acked, resolved, expired, cancelled"""
    title: str | None
    """Title of the escalation"""
    updated_at: str | None
    """When the escalation was last updated"""


class EscalationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """When the escalation was created"""
    creator: list[dict[str, Any]]
    """The creator of this escalation"""
    escalation_path_id: list[str]
    """ID of the escalation path used"""
    events: list[list[Any]]
    """History of escalation events"""
    id: list[str]
    """Unique identifier for the escalation"""
    priority: list[dict[str, Any]]
    """Priority of the escalation"""
    related_alerts: list[list[Any]]
    """Alerts related to this escalation"""
    related_incidents: list[list[Any]]
    """Incidents related to this escalation"""
    status: list[str]
    """Status: pending, triggered, acked, resolved, expired, cancelled"""
    title: list[str]
    """Title of the escalation"""
    updated_at: list[str]
    """When the escalation was last updated"""


class EscalationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """When the escalation was created"""
    creator: Any
    """The creator of this escalation"""
    escalation_path_id: Any
    """ID of the escalation path used"""
    events: Any
    """History of escalation events"""
    id: Any
    """Unique identifier for the escalation"""
    priority: Any
    """Priority of the escalation"""
    related_alerts: Any
    """Alerts related to this escalation"""
    related_incidents: Any
    """Incidents related to this escalation"""
    status: Any
    """Status: pending, triggered, acked, resolved, expired, cancelled"""
    title: Any
    """Title of the escalation"""
    updated_at: Any
    """When the escalation was last updated"""


class EscalationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """When the escalation was created"""
    creator: str
    """The creator of this escalation"""
    escalation_path_id: str
    """ID of the escalation path used"""
    events: str
    """History of escalation events"""
    id: str
    """Unique identifier for the escalation"""
    priority: str
    """Priority of the escalation"""
    related_alerts: str
    """Alerts related to this escalation"""
    related_incidents: str
    """Incidents related to this escalation"""
    status: str
    """Status: pending, triggered, acked, resolved, expired, cancelled"""
    title: str
    """Title of the escalation"""
    updated_at: str
    """When the escalation was last updated"""


class EscalationsSortFilter(TypedDict, total=False):
    """Available fields for sorting escalations search results."""
    created_at: AirbyteSortOrder
    """When the escalation was created"""
    creator: AirbyteSortOrder
    """The creator of this escalation"""
    escalation_path_id: AirbyteSortOrder
    """ID of the escalation path used"""
    events: AirbyteSortOrder
    """History of escalation events"""
    id: AirbyteSortOrder
    """Unique identifier for the escalation"""
    priority: AirbyteSortOrder
    """Priority of the escalation"""
    related_alerts: AirbyteSortOrder
    """Alerts related to this escalation"""
    related_incidents: AirbyteSortOrder
    """Incidents related to this escalation"""
    status: AirbyteSortOrder
    """Status: pending, triggered, acked, resolved, expired, cancelled"""
    title: AirbyteSortOrder
    """Title of the escalation"""
    updated_at: AirbyteSortOrder
    """When the escalation was last updated"""


# Entity-specific condition types for escalations
class EscalationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: EscalationsSearchFilter


class EscalationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: EscalationsSearchFilter


class EscalationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: EscalationsSearchFilter


class EscalationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: EscalationsSearchFilter


class EscalationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: EscalationsSearchFilter


class EscalationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: EscalationsSearchFilter


class EscalationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: EscalationsStringFilter


class EscalationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: EscalationsStringFilter


class EscalationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: EscalationsStringFilter


class EscalationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: EscalationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
EscalationsInCondition = TypedDict("EscalationsInCondition", {"in": EscalationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

EscalationsNotCondition = TypedDict("EscalationsNotCondition", {"not": "EscalationsCondition"}, total=False)
"""Negates the nested condition."""

EscalationsAndCondition = TypedDict("EscalationsAndCondition", {"and": "list[EscalationsCondition]"}, total=False)
"""True if all nested conditions are true."""

EscalationsOrCondition = TypedDict("EscalationsOrCondition", {"or": "list[EscalationsCondition]"}, total=False)
"""True if any nested condition is true."""

EscalationsAnyCondition = TypedDict("EscalationsAnyCondition", {"any": EscalationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all escalations condition types
EscalationsCondition = (
    EscalationsEqCondition
    | EscalationsNeqCondition
    | EscalationsGtCondition
    | EscalationsGteCondition
    | EscalationsLtCondition
    | EscalationsLteCondition
    | EscalationsInCondition
    | EscalationsLikeCondition
    | EscalationsFuzzyCondition
    | EscalationsKeywordCondition
    | EscalationsContainsCondition
    | EscalationsNotCondition
    | EscalationsAndCondition
    | EscalationsOrCondition
    | EscalationsAnyCondition
)


class EscalationsSearchQuery(TypedDict, total=False):
    """Search query for escalations entity."""
    filter: EscalationsCondition
    sort: list[EscalationsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
