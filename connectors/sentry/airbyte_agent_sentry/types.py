"""
Type definitions for sentry connector.
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

class ProjectsListParams(TypedDict):
    """Parameters for projects.list operation"""
    cursor: NotRequired[str]

class ProjectsGetParams(TypedDict):
    """Parameters for projects.get operation"""
    organization_slug: str
    project_slug: str

class IssuesListParams(TypedDict):
    """Parameters for issues.list operation"""
    organization_slug: str
    project_slug: str
    query: NotRequired[str]
    stats_period: NotRequired[str]
    cursor: NotRequired[str]

class IssuesGetParams(TypedDict):
    """Parameters for issues.get operation"""
    organization_slug: str
    issue_id: str

class EventsListParams(TypedDict):
    """Parameters for events.list operation"""
    organization_slug: str
    project_slug: str
    full: NotRequired[str]
    cursor: NotRequired[str]

class EventsGetParams(TypedDict):
    """Parameters for events.get operation"""
    organization_slug: str
    project_slug: str
    event_id: str

class ReleasesListParams(TypedDict):
    """Parameters for releases.list operation"""
    organization_slug: str
    query: NotRequired[str]
    cursor: NotRequired[str]

class ReleasesGetParams(TypedDict):
    """Parameters for releases.get operation"""
    organization_slug: str
    version: str

class ProjectDetailGetParams(TypedDict):
    """Parameters for project_detail.get operation"""
    organization_slug: str
    project_slug: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== EVENTS SEARCH TYPES =====

class EventsSearchFilter(TypedDict, total=False):
    """Available fields for filtering events search queries."""
    meta: dict[str, Any] | None
    """Meta information for data scrubbing."""
    context: dict[str, Any] | None
    """Additional context data."""
    contexts: dict[str, Any] | None
    """Structured context information."""
    crash_file: str | None
    """Crash file reference."""
    culprit: str | None
    """The culprit (source) of the event."""
    date_created: str | None
    """When the event was created."""
    date_received: str | None
    """When the event was received by Sentry."""
    dist: str | None
    """Distribution information."""
    entries: list[Any] | None
    """Event entries (exception, breadcrumbs, request, etc.)."""
    errors: list[Any] | None
    """Processing errors."""
    event_type: str | None
    """The type of the event."""
    event_id: str | None
    """Event ID as reported by the client."""
    fingerprints: list[Any] | None
    """Fingerprints used for grouping."""
    group_id: str | None
    """ID of the issue group this event belongs to."""
    grouping_config: dict[str, Any] | None
    """Grouping configuration."""
    id: str | None
    """Unique event identifier."""
    location: str | None
    """Location in source code."""
    message: str | None
    """Event message."""
    metadata: dict[str, Any] | None
    """Event metadata."""
    occurrence: str | None
    """Occurrence information for the event."""
    packages: dict[str, Any] | None
    """Package information."""
    platform: str | None
    """Platform the event was generated on."""
    project_id: str | None
    """Project ID this event belongs to."""
    sdk: str | None
    """SDK information."""
    size: int | None
    """Event payload size in bytes."""
    tags: list[Any] | None
    """Tags associated with the event."""
    title: str | None
    """Event title."""
    type_: str | None
    """Event type."""
    user: dict[str, Any] | None
    """User associated with the event."""


class EventsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    meta: list[dict[str, Any]]
    """Meta information for data scrubbing."""
    context: list[dict[str, Any]]
    """Additional context data."""
    contexts: list[dict[str, Any]]
    """Structured context information."""
    crash_file: list[str]
    """Crash file reference."""
    culprit: list[str]
    """The culprit (source) of the event."""
    date_created: list[str]
    """When the event was created."""
    date_received: list[str]
    """When the event was received by Sentry."""
    dist: list[str]
    """Distribution information."""
    entries: list[list[Any]]
    """Event entries (exception, breadcrumbs, request, etc.)."""
    errors: list[list[Any]]
    """Processing errors."""
    event_type: list[str]
    """The type of the event."""
    event_id: list[str]
    """Event ID as reported by the client."""
    fingerprints: list[list[Any]]
    """Fingerprints used for grouping."""
    group_id: list[str]
    """ID of the issue group this event belongs to."""
    grouping_config: list[dict[str, Any]]
    """Grouping configuration."""
    id: list[str]
    """Unique event identifier."""
    location: list[str]
    """Location in source code."""
    message: list[str]
    """Event message."""
    metadata: list[dict[str, Any]]
    """Event metadata."""
    occurrence: list[str]
    """Occurrence information for the event."""
    packages: list[dict[str, Any]]
    """Package information."""
    platform: list[str]
    """Platform the event was generated on."""
    project_id: list[str]
    """Project ID this event belongs to."""
    sdk: list[str]
    """SDK information."""
    size: list[int]
    """Event payload size in bytes."""
    tags: list[list[Any]]
    """Tags associated with the event."""
    title: list[str]
    """Event title."""
    type_: list[str]
    """Event type."""
    user: list[dict[str, Any]]
    """User associated with the event."""


class EventsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    meta: Any
    """Meta information for data scrubbing."""
    context: Any
    """Additional context data."""
    contexts: Any
    """Structured context information."""
    crash_file: Any
    """Crash file reference."""
    culprit: Any
    """The culprit (source) of the event."""
    date_created: Any
    """When the event was created."""
    date_received: Any
    """When the event was received by Sentry."""
    dist: Any
    """Distribution information."""
    entries: Any
    """Event entries (exception, breadcrumbs, request, etc.)."""
    errors: Any
    """Processing errors."""
    event_type: Any
    """The type of the event."""
    event_id: Any
    """Event ID as reported by the client."""
    fingerprints: Any
    """Fingerprints used for grouping."""
    group_id: Any
    """ID of the issue group this event belongs to."""
    grouping_config: Any
    """Grouping configuration."""
    id: Any
    """Unique event identifier."""
    location: Any
    """Location in source code."""
    message: Any
    """Event message."""
    metadata: Any
    """Event metadata."""
    occurrence: Any
    """Occurrence information for the event."""
    packages: Any
    """Package information."""
    platform: Any
    """Platform the event was generated on."""
    project_id: Any
    """Project ID this event belongs to."""
    sdk: Any
    """SDK information."""
    size: Any
    """Event payload size in bytes."""
    tags: Any
    """Tags associated with the event."""
    title: Any
    """Event title."""
    type_: Any
    """Event type."""
    user: Any
    """User associated with the event."""


class EventsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    meta: str
    """Meta information for data scrubbing."""
    context: str
    """Additional context data."""
    contexts: str
    """Structured context information."""
    crash_file: str
    """Crash file reference."""
    culprit: str
    """The culprit (source) of the event."""
    date_created: str
    """When the event was created."""
    date_received: str
    """When the event was received by Sentry."""
    dist: str
    """Distribution information."""
    entries: str
    """Event entries (exception, breadcrumbs, request, etc.)."""
    errors: str
    """Processing errors."""
    event_type: str
    """The type of the event."""
    event_id: str
    """Event ID as reported by the client."""
    fingerprints: str
    """Fingerprints used for grouping."""
    group_id: str
    """ID of the issue group this event belongs to."""
    grouping_config: str
    """Grouping configuration."""
    id: str
    """Unique event identifier."""
    location: str
    """Location in source code."""
    message: str
    """Event message."""
    metadata: str
    """Event metadata."""
    occurrence: str
    """Occurrence information for the event."""
    packages: str
    """Package information."""
    platform: str
    """Platform the event was generated on."""
    project_id: str
    """Project ID this event belongs to."""
    sdk: str
    """SDK information."""
    size: str
    """Event payload size in bytes."""
    tags: str
    """Tags associated with the event."""
    title: str
    """Event title."""
    type_: str
    """Event type."""
    user: str
    """User associated with the event."""


class EventsSortFilter(TypedDict, total=False):
    """Available fields for sorting events search results."""
    meta: AirbyteSortOrder
    """Meta information for data scrubbing."""
    context: AirbyteSortOrder
    """Additional context data."""
    contexts: AirbyteSortOrder
    """Structured context information."""
    crash_file: AirbyteSortOrder
    """Crash file reference."""
    culprit: AirbyteSortOrder
    """The culprit (source) of the event."""
    date_created: AirbyteSortOrder
    """When the event was created."""
    date_received: AirbyteSortOrder
    """When the event was received by Sentry."""
    dist: AirbyteSortOrder
    """Distribution information."""
    entries: AirbyteSortOrder
    """Event entries (exception, breadcrumbs, request, etc.)."""
    errors: AirbyteSortOrder
    """Processing errors."""
    event_type: AirbyteSortOrder
    """The type of the event."""
    event_id: AirbyteSortOrder
    """Event ID as reported by the client."""
    fingerprints: AirbyteSortOrder
    """Fingerprints used for grouping."""
    group_id: AirbyteSortOrder
    """ID of the issue group this event belongs to."""
    grouping_config: AirbyteSortOrder
    """Grouping configuration."""
    id: AirbyteSortOrder
    """Unique event identifier."""
    location: AirbyteSortOrder
    """Location in source code."""
    message: AirbyteSortOrder
    """Event message."""
    metadata: AirbyteSortOrder
    """Event metadata."""
    occurrence: AirbyteSortOrder
    """Occurrence information for the event."""
    packages: AirbyteSortOrder
    """Package information."""
    platform: AirbyteSortOrder
    """Platform the event was generated on."""
    project_id: AirbyteSortOrder
    """Project ID this event belongs to."""
    sdk: AirbyteSortOrder
    """SDK information."""
    size: AirbyteSortOrder
    """Event payload size in bytes."""
    tags: AirbyteSortOrder
    """Tags associated with the event."""
    title: AirbyteSortOrder
    """Event title."""
    type_: AirbyteSortOrder
    """Event type."""
    user: AirbyteSortOrder
    """User associated with the event."""


# Entity-specific condition types for events
class EventsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: EventsSearchFilter


class EventsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: EventsSearchFilter


class EventsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: EventsSearchFilter


class EventsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: EventsSearchFilter


class EventsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: EventsSearchFilter


class EventsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: EventsSearchFilter


class EventsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: EventsStringFilter


class EventsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: EventsStringFilter


class EventsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: EventsStringFilter


class EventsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: EventsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
EventsInCondition = TypedDict("EventsInCondition", {"in": EventsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

EventsNotCondition = TypedDict("EventsNotCondition", {"not": "EventsCondition"}, total=False)
"""Negates the nested condition."""

EventsAndCondition = TypedDict("EventsAndCondition", {"and": "list[EventsCondition]"}, total=False)
"""True if all nested conditions are true."""

EventsOrCondition = TypedDict("EventsOrCondition", {"or": "list[EventsCondition]"}, total=False)
"""True if any nested condition is true."""

EventsAnyCondition = TypedDict("EventsAnyCondition", {"any": EventsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all events condition types
EventsCondition = (
    EventsEqCondition
    | EventsNeqCondition
    | EventsGtCondition
    | EventsGteCondition
    | EventsLtCondition
    | EventsLteCondition
    | EventsInCondition
    | EventsLikeCondition
    | EventsFuzzyCondition
    | EventsKeywordCondition
    | EventsContainsCondition
    | EventsNotCondition
    | EventsAndCondition
    | EventsOrCondition
    | EventsAnyCondition
)


class EventsSearchQuery(TypedDict, total=False):
    """Search query for events entity."""
    filter: EventsCondition
    sort: list[EventsSortFilter]


# ===== ISSUES SEARCH TYPES =====

class IssuesSearchFilter(TypedDict, total=False):
    """Available fields for filtering issues search queries."""
    annotations: list[Any] | None
    """Annotations on the issue."""
    assigned_to: dict[str, Any] | None
    """User or team assigned to this issue."""
    count: str | None
    """Number of events for this issue."""
    culprit: str | None
    """The culprit (source) of the issue."""
    first_seen: str | None
    """When the issue was first seen."""
    has_seen: bool | None
    """Whether the authenticated user has seen the issue."""
    id: str | None
    """Unique issue identifier."""
    is_bookmarked: bool | None
    """Whether the issue is bookmarked."""
    is_public: bool | None
    """Whether the issue is public."""
    is_subscribed: bool | None
    """Whether the user is subscribed to the issue."""
    is_unhandled: bool | None
    """Whether the issue is from an unhandled error."""
    issue_category: str | None
    """The category classification of the issue."""
    issue_type: str | None
    """The type classification of the issue."""
    last_seen: str | None
    """When the issue was last seen."""
    level: str | None
    """Issue severity level."""
    logger: str | None
    """Logger that generated the issue."""
    metadata: dict[str, Any] | None
    """Issue metadata."""
    num_comments: int | None
    """Number of comments on the issue."""
    permalink: str | None
    """Permalink to the issue in the Sentry UI."""
    platform: str | None
    """Platform for this issue."""
    project: dict[str, Any] | None
    """Project this issue belongs to."""
    share_id: str | None
    """Share ID if the issue is shared."""
    short_id: str | None
    """Short human-readable identifier."""
    stats: dict[str, Any] | None
    """Issue event statistics."""
    status: str | None
    """Issue status (resolved, unresolved, ignored)."""
    status_details: dict[str, Any] | None
    """Status detail information."""
    subscription_details: dict[str, Any] | None
    """Subscription details."""
    substatus: str | None
    """Issue substatus."""
    title: str | None
    """Issue title."""
    type_: str | None
    """Issue type."""
    user_count: int | None
    """Number of users affected."""


class IssuesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    annotations: list[list[Any]]
    """Annotations on the issue."""
    assigned_to: list[dict[str, Any]]
    """User or team assigned to this issue."""
    count: list[str]
    """Number of events for this issue."""
    culprit: list[str]
    """The culprit (source) of the issue."""
    first_seen: list[str]
    """When the issue was first seen."""
    has_seen: list[bool]
    """Whether the authenticated user has seen the issue."""
    id: list[str]
    """Unique issue identifier."""
    is_bookmarked: list[bool]
    """Whether the issue is bookmarked."""
    is_public: list[bool]
    """Whether the issue is public."""
    is_subscribed: list[bool]
    """Whether the user is subscribed to the issue."""
    is_unhandled: list[bool]
    """Whether the issue is from an unhandled error."""
    issue_category: list[str]
    """The category classification of the issue."""
    issue_type: list[str]
    """The type classification of the issue."""
    last_seen: list[str]
    """When the issue was last seen."""
    level: list[str]
    """Issue severity level."""
    logger: list[str]
    """Logger that generated the issue."""
    metadata: list[dict[str, Any]]
    """Issue metadata."""
    num_comments: list[int]
    """Number of comments on the issue."""
    permalink: list[str]
    """Permalink to the issue in the Sentry UI."""
    platform: list[str]
    """Platform for this issue."""
    project: list[dict[str, Any]]
    """Project this issue belongs to."""
    share_id: list[str]
    """Share ID if the issue is shared."""
    short_id: list[str]
    """Short human-readable identifier."""
    stats: list[dict[str, Any]]
    """Issue event statistics."""
    status: list[str]
    """Issue status (resolved, unresolved, ignored)."""
    status_details: list[dict[str, Any]]
    """Status detail information."""
    subscription_details: list[dict[str, Any]]
    """Subscription details."""
    substatus: list[str]
    """Issue substatus."""
    title: list[str]
    """Issue title."""
    type_: list[str]
    """Issue type."""
    user_count: list[int]
    """Number of users affected."""


class IssuesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    annotations: Any
    """Annotations on the issue."""
    assigned_to: Any
    """User or team assigned to this issue."""
    count: Any
    """Number of events for this issue."""
    culprit: Any
    """The culprit (source) of the issue."""
    first_seen: Any
    """When the issue was first seen."""
    has_seen: Any
    """Whether the authenticated user has seen the issue."""
    id: Any
    """Unique issue identifier."""
    is_bookmarked: Any
    """Whether the issue is bookmarked."""
    is_public: Any
    """Whether the issue is public."""
    is_subscribed: Any
    """Whether the user is subscribed to the issue."""
    is_unhandled: Any
    """Whether the issue is from an unhandled error."""
    issue_category: Any
    """The category classification of the issue."""
    issue_type: Any
    """The type classification of the issue."""
    last_seen: Any
    """When the issue was last seen."""
    level: Any
    """Issue severity level."""
    logger: Any
    """Logger that generated the issue."""
    metadata: Any
    """Issue metadata."""
    num_comments: Any
    """Number of comments on the issue."""
    permalink: Any
    """Permalink to the issue in the Sentry UI."""
    platform: Any
    """Platform for this issue."""
    project: Any
    """Project this issue belongs to."""
    share_id: Any
    """Share ID if the issue is shared."""
    short_id: Any
    """Short human-readable identifier."""
    stats: Any
    """Issue event statistics."""
    status: Any
    """Issue status (resolved, unresolved, ignored)."""
    status_details: Any
    """Status detail information."""
    subscription_details: Any
    """Subscription details."""
    substatus: Any
    """Issue substatus."""
    title: Any
    """Issue title."""
    type_: Any
    """Issue type."""
    user_count: Any
    """Number of users affected."""


class IssuesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    annotations: str
    """Annotations on the issue."""
    assigned_to: str
    """User or team assigned to this issue."""
    count: str
    """Number of events for this issue."""
    culprit: str
    """The culprit (source) of the issue."""
    first_seen: str
    """When the issue was first seen."""
    has_seen: str
    """Whether the authenticated user has seen the issue."""
    id: str
    """Unique issue identifier."""
    is_bookmarked: str
    """Whether the issue is bookmarked."""
    is_public: str
    """Whether the issue is public."""
    is_subscribed: str
    """Whether the user is subscribed to the issue."""
    is_unhandled: str
    """Whether the issue is from an unhandled error."""
    issue_category: str
    """The category classification of the issue."""
    issue_type: str
    """The type classification of the issue."""
    last_seen: str
    """When the issue was last seen."""
    level: str
    """Issue severity level."""
    logger: str
    """Logger that generated the issue."""
    metadata: str
    """Issue metadata."""
    num_comments: str
    """Number of comments on the issue."""
    permalink: str
    """Permalink to the issue in the Sentry UI."""
    platform: str
    """Platform for this issue."""
    project: str
    """Project this issue belongs to."""
    share_id: str
    """Share ID if the issue is shared."""
    short_id: str
    """Short human-readable identifier."""
    stats: str
    """Issue event statistics."""
    status: str
    """Issue status (resolved, unresolved, ignored)."""
    status_details: str
    """Status detail information."""
    subscription_details: str
    """Subscription details."""
    substatus: str
    """Issue substatus."""
    title: str
    """Issue title."""
    type_: str
    """Issue type."""
    user_count: str
    """Number of users affected."""


class IssuesSortFilter(TypedDict, total=False):
    """Available fields for sorting issues search results."""
    annotations: AirbyteSortOrder
    """Annotations on the issue."""
    assigned_to: AirbyteSortOrder
    """User or team assigned to this issue."""
    count: AirbyteSortOrder
    """Number of events for this issue."""
    culprit: AirbyteSortOrder
    """The culprit (source) of the issue."""
    first_seen: AirbyteSortOrder
    """When the issue was first seen."""
    has_seen: AirbyteSortOrder
    """Whether the authenticated user has seen the issue."""
    id: AirbyteSortOrder
    """Unique issue identifier."""
    is_bookmarked: AirbyteSortOrder
    """Whether the issue is bookmarked."""
    is_public: AirbyteSortOrder
    """Whether the issue is public."""
    is_subscribed: AirbyteSortOrder
    """Whether the user is subscribed to the issue."""
    is_unhandled: AirbyteSortOrder
    """Whether the issue is from an unhandled error."""
    issue_category: AirbyteSortOrder
    """The category classification of the issue."""
    issue_type: AirbyteSortOrder
    """The type classification of the issue."""
    last_seen: AirbyteSortOrder
    """When the issue was last seen."""
    level: AirbyteSortOrder
    """Issue severity level."""
    logger: AirbyteSortOrder
    """Logger that generated the issue."""
    metadata: AirbyteSortOrder
    """Issue metadata."""
    num_comments: AirbyteSortOrder
    """Number of comments on the issue."""
    permalink: AirbyteSortOrder
    """Permalink to the issue in the Sentry UI."""
    platform: AirbyteSortOrder
    """Platform for this issue."""
    project: AirbyteSortOrder
    """Project this issue belongs to."""
    share_id: AirbyteSortOrder
    """Share ID if the issue is shared."""
    short_id: AirbyteSortOrder
    """Short human-readable identifier."""
    stats: AirbyteSortOrder
    """Issue event statistics."""
    status: AirbyteSortOrder
    """Issue status (resolved, unresolved, ignored)."""
    status_details: AirbyteSortOrder
    """Status detail information."""
    subscription_details: AirbyteSortOrder
    """Subscription details."""
    substatus: AirbyteSortOrder
    """Issue substatus."""
    title: AirbyteSortOrder
    """Issue title."""
    type_: AirbyteSortOrder
    """Issue type."""
    user_count: AirbyteSortOrder
    """Number of users affected."""


# Entity-specific condition types for issues
class IssuesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IssuesSearchFilter


class IssuesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IssuesSearchFilter


class IssuesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IssuesSearchFilter


class IssuesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IssuesSearchFilter


class IssuesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IssuesSearchFilter


class IssuesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IssuesSearchFilter


class IssuesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IssuesStringFilter


class IssuesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IssuesStringFilter


class IssuesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IssuesStringFilter


class IssuesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IssuesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IssuesInCondition = TypedDict("IssuesInCondition", {"in": IssuesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IssuesNotCondition = TypedDict("IssuesNotCondition", {"not": "IssuesCondition"}, total=False)
"""Negates the nested condition."""

IssuesAndCondition = TypedDict("IssuesAndCondition", {"and": "list[IssuesCondition]"}, total=False)
"""True if all nested conditions are true."""

IssuesOrCondition = TypedDict("IssuesOrCondition", {"or": "list[IssuesCondition]"}, total=False)
"""True if any nested condition is true."""

IssuesAnyCondition = TypedDict("IssuesAnyCondition", {"any": IssuesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all issues condition types
IssuesCondition = (
    IssuesEqCondition
    | IssuesNeqCondition
    | IssuesGtCondition
    | IssuesGteCondition
    | IssuesLtCondition
    | IssuesLteCondition
    | IssuesInCondition
    | IssuesLikeCondition
    | IssuesFuzzyCondition
    | IssuesKeywordCondition
    | IssuesContainsCondition
    | IssuesNotCondition
    | IssuesAndCondition
    | IssuesOrCondition
    | IssuesAnyCondition
)


class IssuesSearchQuery(TypedDict, total=False):
    """Search query for issues entity."""
    filter: IssuesCondition
    sort: list[IssuesSortFilter]


# ===== PROJECTS SEARCH TYPES =====

class ProjectsSearchFilter(TypedDict, total=False):
    """Available fields for filtering projects search queries."""
    access: list[Any] | None
    """List of access permissions for the authenticated user."""
    avatar: dict[str, Any] | None
    """Project avatar information."""
    color: str | None
    """Project color code."""
    date_created: str | None
    """Date the project was created."""
    features: list[Any] | None
    """List of enabled features."""
    first_event: str | None
    """Timestamp of the first event."""
    first_transaction_event: bool | None
    """Whether a transaction event has been received."""
    has_access: bool | None
    """Whether the user has access to this project."""
    has_custom_metrics: bool | None
    """Whether the project has custom metrics."""
    has_feedbacks: bool | None
    """Whether the project has user feedback."""
    has_minified_stack_trace: bool | None
    """Whether the project has minified stack traces."""
    has_monitors: bool | None
    """Whether the project has cron monitors."""
    has_new_feedbacks: bool | None
    """Whether the project has new user feedback."""
    has_profiles: bool | None
    """Whether the project has profiling data."""
    has_replays: bool | None
    """Whether the project has session replays."""
    has_sessions: bool | None
    """Whether the project has session data."""
    id: str | None
    """Unique project identifier."""
    is_bookmarked: bool | None
    """Whether the project is bookmarked."""
    is_internal: bool | None
    """Whether the project is internal."""
    is_member: bool | None
    """Whether the authenticated user is a member."""
    is_public: bool | None
    """Whether the project is public."""
    name: str | None
    """Human-readable project name."""
    organization: dict[str, Any] | None
    """Organization this project belongs to."""
    platform: str | None
    """The platform for this project."""
    slug: str | None
    """URL-friendly project identifier."""
    status: str | None
    """Project status."""


class ProjectsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    access: list[list[Any]]
    """List of access permissions for the authenticated user."""
    avatar: list[dict[str, Any]]
    """Project avatar information."""
    color: list[str]
    """Project color code."""
    date_created: list[str]
    """Date the project was created."""
    features: list[list[Any]]
    """List of enabled features."""
    first_event: list[str]
    """Timestamp of the first event."""
    first_transaction_event: list[bool]
    """Whether a transaction event has been received."""
    has_access: list[bool]
    """Whether the user has access to this project."""
    has_custom_metrics: list[bool]
    """Whether the project has custom metrics."""
    has_feedbacks: list[bool]
    """Whether the project has user feedback."""
    has_minified_stack_trace: list[bool]
    """Whether the project has minified stack traces."""
    has_monitors: list[bool]
    """Whether the project has cron monitors."""
    has_new_feedbacks: list[bool]
    """Whether the project has new user feedback."""
    has_profiles: list[bool]
    """Whether the project has profiling data."""
    has_replays: list[bool]
    """Whether the project has session replays."""
    has_sessions: list[bool]
    """Whether the project has session data."""
    id: list[str]
    """Unique project identifier."""
    is_bookmarked: list[bool]
    """Whether the project is bookmarked."""
    is_internal: list[bool]
    """Whether the project is internal."""
    is_member: list[bool]
    """Whether the authenticated user is a member."""
    is_public: list[bool]
    """Whether the project is public."""
    name: list[str]
    """Human-readable project name."""
    organization: list[dict[str, Any]]
    """Organization this project belongs to."""
    platform: list[str]
    """The platform for this project."""
    slug: list[str]
    """URL-friendly project identifier."""
    status: list[str]
    """Project status."""


class ProjectsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    access: Any
    """List of access permissions for the authenticated user."""
    avatar: Any
    """Project avatar information."""
    color: Any
    """Project color code."""
    date_created: Any
    """Date the project was created."""
    features: Any
    """List of enabled features."""
    first_event: Any
    """Timestamp of the first event."""
    first_transaction_event: Any
    """Whether a transaction event has been received."""
    has_access: Any
    """Whether the user has access to this project."""
    has_custom_metrics: Any
    """Whether the project has custom metrics."""
    has_feedbacks: Any
    """Whether the project has user feedback."""
    has_minified_stack_trace: Any
    """Whether the project has minified stack traces."""
    has_monitors: Any
    """Whether the project has cron monitors."""
    has_new_feedbacks: Any
    """Whether the project has new user feedback."""
    has_profiles: Any
    """Whether the project has profiling data."""
    has_replays: Any
    """Whether the project has session replays."""
    has_sessions: Any
    """Whether the project has session data."""
    id: Any
    """Unique project identifier."""
    is_bookmarked: Any
    """Whether the project is bookmarked."""
    is_internal: Any
    """Whether the project is internal."""
    is_member: Any
    """Whether the authenticated user is a member."""
    is_public: Any
    """Whether the project is public."""
    name: Any
    """Human-readable project name."""
    organization: Any
    """Organization this project belongs to."""
    platform: Any
    """The platform for this project."""
    slug: Any
    """URL-friendly project identifier."""
    status: Any
    """Project status."""


class ProjectsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    access: str
    """List of access permissions for the authenticated user."""
    avatar: str
    """Project avatar information."""
    color: str
    """Project color code."""
    date_created: str
    """Date the project was created."""
    features: str
    """List of enabled features."""
    first_event: str
    """Timestamp of the first event."""
    first_transaction_event: str
    """Whether a transaction event has been received."""
    has_access: str
    """Whether the user has access to this project."""
    has_custom_metrics: str
    """Whether the project has custom metrics."""
    has_feedbacks: str
    """Whether the project has user feedback."""
    has_minified_stack_trace: str
    """Whether the project has minified stack traces."""
    has_monitors: str
    """Whether the project has cron monitors."""
    has_new_feedbacks: str
    """Whether the project has new user feedback."""
    has_profiles: str
    """Whether the project has profiling data."""
    has_replays: str
    """Whether the project has session replays."""
    has_sessions: str
    """Whether the project has session data."""
    id: str
    """Unique project identifier."""
    is_bookmarked: str
    """Whether the project is bookmarked."""
    is_internal: str
    """Whether the project is internal."""
    is_member: str
    """Whether the authenticated user is a member."""
    is_public: str
    """Whether the project is public."""
    name: str
    """Human-readable project name."""
    organization: str
    """Organization this project belongs to."""
    platform: str
    """The platform for this project."""
    slug: str
    """URL-friendly project identifier."""
    status: str
    """Project status."""


class ProjectsSortFilter(TypedDict, total=False):
    """Available fields for sorting projects search results."""
    access: AirbyteSortOrder
    """List of access permissions for the authenticated user."""
    avatar: AirbyteSortOrder
    """Project avatar information."""
    color: AirbyteSortOrder
    """Project color code."""
    date_created: AirbyteSortOrder
    """Date the project was created."""
    features: AirbyteSortOrder
    """List of enabled features."""
    first_event: AirbyteSortOrder
    """Timestamp of the first event."""
    first_transaction_event: AirbyteSortOrder
    """Whether a transaction event has been received."""
    has_access: AirbyteSortOrder
    """Whether the user has access to this project."""
    has_custom_metrics: AirbyteSortOrder
    """Whether the project has custom metrics."""
    has_feedbacks: AirbyteSortOrder
    """Whether the project has user feedback."""
    has_minified_stack_trace: AirbyteSortOrder
    """Whether the project has minified stack traces."""
    has_monitors: AirbyteSortOrder
    """Whether the project has cron monitors."""
    has_new_feedbacks: AirbyteSortOrder
    """Whether the project has new user feedback."""
    has_profiles: AirbyteSortOrder
    """Whether the project has profiling data."""
    has_replays: AirbyteSortOrder
    """Whether the project has session replays."""
    has_sessions: AirbyteSortOrder
    """Whether the project has session data."""
    id: AirbyteSortOrder
    """Unique project identifier."""
    is_bookmarked: AirbyteSortOrder
    """Whether the project is bookmarked."""
    is_internal: AirbyteSortOrder
    """Whether the project is internal."""
    is_member: AirbyteSortOrder
    """Whether the authenticated user is a member."""
    is_public: AirbyteSortOrder
    """Whether the project is public."""
    name: AirbyteSortOrder
    """Human-readable project name."""
    organization: AirbyteSortOrder
    """Organization this project belongs to."""
    platform: AirbyteSortOrder
    """The platform for this project."""
    slug: AirbyteSortOrder
    """URL-friendly project identifier."""
    status: AirbyteSortOrder
    """Project status."""


# Entity-specific condition types for projects
class ProjectsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProjectsSearchFilter


class ProjectsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProjectsSearchFilter


class ProjectsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProjectsSearchFilter


class ProjectsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProjectsSearchFilter


class ProjectsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProjectsSearchFilter


class ProjectsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProjectsSearchFilter


class ProjectsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProjectsStringFilter


class ProjectsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProjectsStringFilter


class ProjectsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProjectsStringFilter


class ProjectsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProjectsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProjectsInCondition = TypedDict("ProjectsInCondition", {"in": ProjectsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProjectsNotCondition = TypedDict("ProjectsNotCondition", {"not": "ProjectsCondition"}, total=False)
"""Negates the nested condition."""

ProjectsAndCondition = TypedDict("ProjectsAndCondition", {"and": "list[ProjectsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProjectsOrCondition = TypedDict("ProjectsOrCondition", {"or": "list[ProjectsCondition]"}, total=False)
"""True if any nested condition is true."""

ProjectsAnyCondition = TypedDict("ProjectsAnyCondition", {"any": ProjectsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all projects condition types
ProjectsCondition = (
    ProjectsEqCondition
    | ProjectsNeqCondition
    | ProjectsGtCondition
    | ProjectsGteCondition
    | ProjectsLtCondition
    | ProjectsLteCondition
    | ProjectsInCondition
    | ProjectsLikeCondition
    | ProjectsFuzzyCondition
    | ProjectsKeywordCondition
    | ProjectsContainsCondition
    | ProjectsNotCondition
    | ProjectsAndCondition
    | ProjectsOrCondition
    | ProjectsAnyCondition
)


class ProjectsSearchQuery(TypedDict, total=False):
    """Search query for projects entity."""
    filter: ProjectsCondition
    sort: list[ProjectsSortFilter]


# ===== RELEASES SEARCH TYPES =====

class ReleasesSearchFilter(TypedDict, total=False):
    """Available fields for filtering releases search queries."""
    authors: list[Any] | None
    """Authors of commits in this release."""
    commit_count: int | None
    """Number of commits in this release."""
    current_project_meta: dict[str, Any] | None
    """Metadata for the current project context."""
    data: dict[str, Any] | None
    """Additional release data."""
    date_created: str | None
    """When the release was created."""
    date_released: str | None
    """When the release was deployed."""
    deploy_count: int | None
    """Number of deploys for this release."""
    first_event: str | None
    """Timestamp of the first event in this release."""
    id: int | None
    """Unique release identifier."""
    last_commit: dict[str, Any] | None
    """Last commit in this release."""
    last_deploy: dict[str, Any] | None
    """Last deploy of this release."""
    last_event: str | None
    """Timestamp of the last event in this release."""
    new_groups: int | None
    """Number of new issue groups in this release."""
    owner: str | None
    """Owner of the release."""
    projects: list[Any] | None
    """Projects associated with this release."""
    ref: str | None
    """Git reference (commit SHA, tag, etc.)."""
    short_version: str | None
    """Short version string."""
    status: str | None
    """Release status."""
    url: str | None
    """URL associated with the release."""
    user_agent: str | None
    """User agent that created the release."""
    version: str | None
    """Release version string."""
    version_info: dict[str, Any] | None
    """Parsed version information."""


class ReleasesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    authors: list[list[Any]]
    """Authors of commits in this release."""
    commit_count: list[int]
    """Number of commits in this release."""
    current_project_meta: list[dict[str, Any]]
    """Metadata for the current project context."""
    data: list[dict[str, Any]]
    """Additional release data."""
    date_created: list[str]
    """When the release was created."""
    date_released: list[str]
    """When the release was deployed."""
    deploy_count: list[int]
    """Number of deploys for this release."""
    first_event: list[str]
    """Timestamp of the first event in this release."""
    id: list[int]
    """Unique release identifier."""
    last_commit: list[dict[str, Any]]
    """Last commit in this release."""
    last_deploy: list[dict[str, Any]]
    """Last deploy of this release."""
    last_event: list[str]
    """Timestamp of the last event in this release."""
    new_groups: list[int]
    """Number of new issue groups in this release."""
    owner: list[str]
    """Owner of the release."""
    projects: list[list[Any]]
    """Projects associated with this release."""
    ref: list[str]
    """Git reference (commit SHA, tag, etc.)."""
    short_version: list[str]
    """Short version string."""
    status: list[str]
    """Release status."""
    url: list[str]
    """URL associated with the release."""
    user_agent: list[str]
    """User agent that created the release."""
    version: list[str]
    """Release version string."""
    version_info: list[dict[str, Any]]
    """Parsed version information."""


class ReleasesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    authors: Any
    """Authors of commits in this release."""
    commit_count: Any
    """Number of commits in this release."""
    current_project_meta: Any
    """Metadata for the current project context."""
    data: Any
    """Additional release data."""
    date_created: Any
    """When the release was created."""
    date_released: Any
    """When the release was deployed."""
    deploy_count: Any
    """Number of deploys for this release."""
    first_event: Any
    """Timestamp of the first event in this release."""
    id: Any
    """Unique release identifier."""
    last_commit: Any
    """Last commit in this release."""
    last_deploy: Any
    """Last deploy of this release."""
    last_event: Any
    """Timestamp of the last event in this release."""
    new_groups: Any
    """Number of new issue groups in this release."""
    owner: Any
    """Owner of the release."""
    projects: Any
    """Projects associated with this release."""
    ref: Any
    """Git reference (commit SHA, tag, etc.)."""
    short_version: Any
    """Short version string."""
    status: Any
    """Release status."""
    url: Any
    """URL associated with the release."""
    user_agent: Any
    """User agent that created the release."""
    version: Any
    """Release version string."""
    version_info: Any
    """Parsed version information."""


class ReleasesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    authors: str
    """Authors of commits in this release."""
    commit_count: str
    """Number of commits in this release."""
    current_project_meta: str
    """Metadata for the current project context."""
    data: str
    """Additional release data."""
    date_created: str
    """When the release was created."""
    date_released: str
    """When the release was deployed."""
    deploy_count: str
    """Number of deploys for this release."""
    first_event: str
    """Timestamp of the first event in this release."""
    id: str
    """Unique release identifier."""
    last_commit: str
    """Last commit in this release."""
    last_deploy: str
    """Last deploy of this release."""
    last_event: str
    """Timestamp of the last event in this release."""
    new_groups: str
    """Number of new issue groups in this release."""
    owner: str
    """Owner of the release."""
    projects: str
    """Projects associated with this release."""
    ref: str
    """Git reference (commit SHA, tag, etc.)."""
    short_version: str
    """Short version string."""
    status: str
    """Release status."""
    url: str
    """URL associated with the release."""
    user_agent: str
    """User agent that created the release."""
    version: str
    """Release version string."""
    version_info: str
    """Parsed version information."""


class ReleasesSortFilter(TypedDict, total=False):
    """Available fields for sorting releases search results."""
    authors: AirbyteSortOrder
    """Authors of commits in this release."""
    commit_count: AirbyteSortOrder
    """Number of commits in this release."""
    current_project_meta: AirbyteSortOrder
    """Metadata for the current project context."""
    data: AirbyteSortOrder
    """Additional release data."""
    date_created: AirbyteSortOrder
    """When the release was created."""
    date_released: AirbyteSortOrder
    """When the release was deployed."""
    deploy_count: AirbyteSortOrder
    """Number of deploys for this release."""
    first_event: AirbyteSortOrder
    """Timestamp of the first event in this release."""
    id: AirbyteSortOrder
    """Unique release identifier."""
    last_commit: AirbyteSortOrder
    """Last commit in this release."""
    last_deploy: AirbyteSortOrder
    """Last deploy of this release."""
    last_event: AirbyteSortOrder
    """Timestamp of the last event in this release."""
    new_groups: AirbyteSortOrder
    """Number of new issue groups in this release."""
    owner: AirbyteSortOrder
    """Owner of the release."""
    projects: AirbyteSortOrder
    """Projects associated with this release."""
    ref: AirbyteSortOrder
    """Git reference (commit SHA, tag, etc.)."""
    short_version: AirbyteSortOrder
    """Short version string."""
    status: AirbyteSortOrder
    """Release status."""
    url: AirbyteSortOrder
    """URL associated with the release."""
    user_agent: AirbyteSortOrder
    """User agent that created the release."""
    version: AirbyteSortOrder
    """Release version string."""
    version_info: AirbyteSortOrder
    """Parsed version information."""


# Entity-specific condition types for releases
class ReleasesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ReleasesSearchFilter


class ReleasesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ReleasesSearchFilter


class ReleasesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ReleasesSearchFilter


class ReleasesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ReleasesSearchFilter


class ReleasesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ReleasesSearchFilter


class ReleasesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ReleasesSearchFilter


class ReleasesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ReleasesStringFilter


class ReleasesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ReleasesStringFilter


class ReleasesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ReleasesStringFilter


class ReleasesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ReleasesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ReleasesInCondition = TypedDict("ReleasesInCondition", {"in": ReleasesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ReleasesNotCondition = TypedDict("ReleasesNotCondition", {"not": "ReleasesCondition"}, total=False)
"""Negates the nested condition."""

ReleasesAndCondition = TypedDict("ReleasesAndCondition", {"and": "list[ReleasesCondition]"}, total=False)
"""True if all nested conditions are true."""

ReleasesOrCondition = TypedDict("ReleasesOrCondition", {"or": "list[ReleasesCondition]"}, total=False)
"""True if any nested condition is true."""

ReleasesAnyCondition = TypedDict("ReleasesAnyCondition", {"any": ReleasesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all releases condition types
ReleasesCondition = (
    ReleasesEqCondition
    | ReleasesNeqCondition
    | ReleasesGtCondition
    | ReleasesGteCondition
    | ReleasesLtCondition
    | ReleasesLteCondition
    | ReleasesInCondition
    | ReleasesLikeCondition
    | ReleasesFuzzyCondition
    | ReleasesKeywordCondition
    | ReleasesContainsCondition
    | ReleasesNotCondition
    | ReleasesAndCondition
    | ReleasesOrCondition
    | ReleasesAnyCondition
)


class ReleasesSearchQuery(TypedDict, total=False):
    """Search query for releases entity."""
    filter: ReleasesCondition
    sort: list[ReleasesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
