"""
Type definitions for amplitude connector.
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

class AnnotationsListParams(TypedDict):
    """Parameters for annotations.list operation"""
    pass

class AnnotationsGetParams(TypedDict):
    """Parameters for annotations.get operation"""
    annotation_id: str

class CohortsListParams(TypedDict):
    """Parameters for cohorts.list operation"""
    pass

class CohortsGetParams(TypedDict):
    """Parameters for cohorts.get operation"""
    cohort_id: str

class EventsListListParams(TypedDict):
    """Parameters for events_list.list operation"""
    pass

class ActiveUsersListParams(TypedDict):
    """Parameters for active_users.list operation"""
    start: str
    end: str
    m: NotRequired[str]
    i: NotRequired[int]
    g: NotRequired[str]

class AverageSessionLengthListParams(TypedDict):
    """Parameters for average_session_length.list operation"""
    start: str
    end: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ANNOTATIONS SEARCH TYPES =====

class AnnotationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering annotations search queries."""
    date: str | None
    """The date when the annotation was made"""
    details: str | None
    """Additional details or information related to the annotation"""
    id: int | None
    """The unique identifier for the annotation"""
    label: str | None
    """The label assigned to the annotation"""


class AnnotationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    date: list[str]
    """The date when the annotation was made"""
    details: list[str]
    """Additional details or information related to the annotation"""
    id: list[int]
    """The unique identifier for the annotation"""
    label: list[str]
    """The label assigned to the annotation"""


class AnnotationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    date: Any
    """The date when the annotation was made"""
    details: Any
    """Additional details or information related to the annotation"""
    id: Any
    """The unique identifier for the annotation"""
    label: Any
    """The label assigned to the annotation"""


class AnnotationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    date: str
    """The date when the annotation was made"""
    details: str
    """Additional details or information related to the annotation"""
    id: str
    """The unique identifier for the annotation"""
    label: str
    """The label assigned to the annotation"""


class AnnotationsSortFilter(TypedDict, total=False):
    """Available fields for sorting annotations search results."""
    date: AirbyteSortOrder
    """The date when the annotation was made"""
    details: AirbyteSortOrder
    """Additional details or information related to the annotation"""
    id: AirbyteSortOrder
    """The unique identifier for the annotation"""
    label: AirbyteSortOrder
    """The label assigned to the annotation"""


# Entity-specific condition types for annotations
class AnnotationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AnnotationsSearchFilter


class AnnotationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AnnotationsSearchFilter


class AnnotationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AnnotationsSearchFilter


class AnnotationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AnnotationsSearchFilter


class AnnotationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AnnotationsSearchFilter


class AnnotationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AnnotationsSearchFilter


class AnnotationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AnnotationsStringFilter


class AnnotationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AnnotationsStringFilter


class AnnotationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AnnotationsStringFilter


class AnnotationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AnnotationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AnnotationsInCondition = TypedDict("AnnotationsInCondition", {"in": AnnotationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AnnotationsNotCondition = TypedDict("AnnotationsNotCondition", {"not": "AnnotationsCondition"}, total=False)
"""Negates the nested condition."""

AnnotationsAndCondition = TypedDict("AnnotationsAndCondition", {"and": "list[AnnotationsCondition]"}, total=False)
"""True if all nested conditions are true."""

AnnotationsOrCondition = TypedDict("AnnotationsOrCondition", {"or": "list[AnnotationsCondition]"}, total=False)
"""True if any nested condition is true."""

AnnotationsAnyCondition = TypedDict("AnnotationsAnyCondition", {"any": AnnotationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all annotations condition types
AnnotationsCondition = (
    AnnotationsEqCondition
    | AnnotationsNeqCondition
    | AnnotationsGtCondition
    | AnnotationsGteCondition
    | AnnotationsLtCondition
    | AnnotationsLteCondition
    | AnnotationsInCondition
    | AnnotationsLikeCondition
    | AnnotationsFuzzyCondition
    | AnnotationsKeywordCondition
    | AnnotationsContainsCondition
    | AnnotationsNotCondition
    | AnnotationsAndCondition
    | AnnotationsOrCondition
    | AnnotationsAnyCondition
)


class AnnotationsSearchQuery(TypedDict, total=False):
    """Search query for annotations entity."""
    filter: AnnotationsCondition
    sort: list[AnnotationsSortFilter]


# ===== COHORTS SEARCH TYPES =====

class CohortsSearchFilter(TypedDict, total=False):
    """Available fields for filtering cohorts search queries."""
    app_id: int | None
    """The unique identifier of the application"""
    archived: bool | None
    """Indicates if the cohort data is archived"""
    chart_id: str | None
    """The identifier of the chart associated with the cohort"""
    created_at: int | None
    """The timestamp when the cohort was created"""
    definition: dict[str, Any] | None
    """The specific definition or criteria for the cohort"""
    description: str | None
    """A brief explanation or summary of the cohort"""
    edit_id: str | None
    """The ID for editing purposes or version control"""
    finished: bool | None
    """Indicates if the cohort data has been finalized"""
    hidden: bool | None
    """Flag to determine if the cohort is hidden from view"""
    id: str | None
    """The unique identifier for the cohort"""
    is_official_content: bool | None
    """Indicates if the cohort data is official content"""
    is_predictive: bool | None
    """Flag to indicate if the cohort is predictive"""
    last_computed: int | None
    """Timestamp of the last computation of cohort data"""
    last_mod: int | None
    """Timestamp of the last modification made to the cohort"""
    last_viewed: int | None
    """Timestamp when the cohort was last viewed"""
    location_id: str | None
    """Identifier of the location associated with the cohort"""
    metadata: list[Any] | None
    """Additional information or data related to the cohort"""
    name: str | None
    """The name or title of the cohort"""
    owners: list[Any] | None
    """The owners or administrators of the cohort"""
    popularity: int | None
    """Popularity rank or score of the cohort"""
    published: bool | None
    """Status indicating if the cohort data is published"""
    shortcut_ids: list[Any] | None
    """Identifiers of any shortcuts associated with the cohort"""
    size: int | None
    """Size or scale of the cohort data"""
    type: str | None
    """The type or category of the cohort"""
    view_count: int | None
    """The total count of views on the cohort data"""
    viewers: list[Any] | None
    """Users or viewers who have access to the cohort data"""


class CohortsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    app_id: list[int]
    """The unique identifier of the application"""
    archived: list[bool]
    """Indicates if the cohort data is archived"""
    chart_id: list[str]
    """The identifier of the chart associated with the cohort"""
    created_at: list[int]
    """The timestamp when the cohort was created"""
    definition: list[dict[str, Any]]
    """The specific definition or criteria for the cohort"""
    description: list[str]
    """A brief explanation or summary of the cohort"""
    edit_id: list[str]
    """The ID for editing purposes or version control"""
    finished: list[bool]
    """Indicates if the cohort data has been finalized"""
    hidden: list[bool]
    """Flag to determine if the cohort is hidden from view"""
    id: list[str]
    """The unique identifier for the cohort"""
    is_official_content: list[bool]
    """Indicates if the cohort data is official content"""
    is_predictive: list[bool]
    """Flag to indicate if the cohort is predictive"""
    last_computed: list[int]
    """Timestamp of the last computation of cohort data"""
    last_mod: list[int]
    """Timestamp of the last modification made to the cohort"""
    last_viewed: list[int]
    """Timestamp when the cohort was last viewed"""
    location_id: list[str]
    """Identifier of the location associated with the cohort"""
    metadata: list[list[Any]]
    """Additional information or data related to the cohort"""
    name: list[str]
    """The name or title of the cohort"""
    owners: list[list[Any]]
    """The owners or administrators of the cohort"""
    popularity: list[int]
    """Popularity rank or score of the cohort"""
    published: list[bool]
    """Status indicating if the cohort data is published"""
    shortcut_ids: list[list[Any]]
    """Identifiers of any shortcuts associated with the cohort"""
    size: list[int]
    """Size or scale of the cohort data"""
    type: list[str]
    """The type or category of the cohort"""
    view_count: list[int]
    """The total count of views on the cohort data"""
    viewers: list[list[Any]]
    """Users or viewers who have access to the cohort data"""


class CohortsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    app_id: Any
    """The unique identifier of the application"""
    archived: Any
    """Indicates if the cohort data is archived"""
    chart_id: Any
    """The identifier of the chart associated with the cohort"""
    created_at: Any
    """The timestamp when the cohort was created"""
    definition: Any
    """The specific definition or criteria for the cohort"""
    description: Any
    """A brief explanation or summary of the cohort"""
    edit_id: Any
    """The ID for editing purposes or version control"""
    finished: Any
    """Indicates if the cohort data has been finalized"""
    hidden: Any
    """Flag to determine if the cohort is hidden from view"""
    id: Any
    """The unique identifier for the cohort"""
    is_official_content: Any
    """Indicates if the cohort data is official content"""
    is_predictive: Any
    """Flag to indicate if the cohort is predictive"""
    last_computed: Any
    """Timestamp of the last computation of cohort data"""
    last_mod: Any
    """Timestamp of the last modification made to the cohort"""
    last_viewed: Any
    """Timestamp when the cohort was last viewed"""
    location_id: Any
    """Identifier of the location associated with the cohort"""
    metadata: Any
    """Additional information or data related to the cohort"""
    name: Any
    """The name or title of the cohort"""
    owners: Any
    """The owners or administrators of the cohort"""
    popularity: Any
    """Popularity rank or score of the cohort"""
    published: Any
    """Status indicating if the cohort data is published"""
    shortcut_ids: Any
    """Identifiers of any shortcuts associated with the cohort"""
    size: Any
    """Size or scale of the cohort data"""
    type: Any
    """The type or category of the cohort"""
    view_count: Any
    """The total count of views on the cohort data"""
    viewers: Any
    """Users or viewers who have access to the cohort data"""


class CohortsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    app_id: str
    """The unique identifier of the application"""
    archived: str
    """Indicates if the cohort data is archived"""
    chart_id: str
    """The identifier of the chart associated with the cohort"""
    created_at: str
    """The timestamp when the cohort was created"""
    definition: str
    """The specific definition or criteria for the cohort"""
    description: str
    """A brief explanation or summary of the cohort"""
    edit_id: str
    """The ID for editing purposes or version control"""
    finished: str
    """Indicates if the cohort data has been finalized"""
    hidden: str
    """Flag to determine if the cohort is hidden from view"""
    id: str
    """The unique identifier for the cohort"""
    is_official_content: str
    """Indicates if the cohort data is official content"""
    is_predictive: str
    """Flag to indicate if the cohort is predictive"""
    last_computed: str
    """Timestamp of the last computation of cohort data"""
    last_mod: str
    """Timestamp of the last modification made to the cohort"""
    last_viewed: str
    """Timestamp when the cohort was last viewed"""
    location_id: str
    """Identifier of the location associated with the cohort"""
    metadata: str
    """Additional information or data related to the cohort"""
    name: str
    """The name or title of the cohort"""
    owners: str
    """The owners or administrators of the cohort"""
    popularity: str
    """Popularity rank or score of the cohort"""
    published: str
    """Status indicating if the cohort data is published"""
    shortcut_ids: str
    """Identifiers of any shortcuts associated with the cohort"""
    size: str
    """Size or scale of the cohort data"""
    type: str
    """The type or category of the cohort"""
    view_count: str
    """The total count of views on the cohort data"""
    viewers: str
    """Users or viewers who have access to the cohort data"""


class CohortsSortFilter(TypedDict, total=False):
    """Available fields for sorting cohorts search results."""
    app_id: AirbyteSortOrder
    """The unique identifier of the application"""
    archived: AirbyteSortOrder
    """Indicates if the cohort data is archived"""
    chart_id: AirbyteSortOrder
    """The identifier of the chart associated with the cohort"""
    created_at: AirbyteSortOrder
    """The timestamp when the cohort was created"""
    definition: AirbyteSortOrder
    """The specific definition or criteria for the cohort"""
    description: AirbyteSortOrder
    """A brief explanation or summary of the cohort"""
    edit_id: AirbyteSortOrder
    """The ID for editing purposes or version control"""
    finished: AirbyteSortOrder
    """Indicates if the cohort data has been finalized"""
    hidden: AirbyteSortOrder
    """Flag to determine if the cohort is hidden from view"""
    id: AirbyteSortOrder
    """The unique identifier for the cohort"""
    is_official_content: AirbyteSortOrder
    """Indicates if the cohort data is official content"""
    is_predictive: AirbyteSortOrder
    """Flag to indicate if the cohort is predictive"""
    last_computed: AirbyteSortOrder
    """Timestamp of the last computation of cohort data"""
    last_mod: AirbyteSortOrder
    """Timestamp of the last modification made to the cohort"""
    last_viewed: AirbyteSortOrder
    """Timestamp when the cohort was last viewed"""
    location_id: AirbyteSortOrder
    """Identifier of the location associated with the cohort"""
    metadata: AirbyteSortOrder
    """Additional information or data related to the cohort"""
    name: AirbyteSortOrder
    """The name or title of the cohort"""
    owners: AirbyteSortOrder
    """The owners or administrators of the cohort"""
    popularity: AirbyteSortOrder
    """Popularity rank or score of the cohort"""
    published: AirbyteSortOrder
    """Status indicating if the cohort data is published"""
    shortcut_ids: AirbyteSortOrder
    """Identifiers of any shortcuts associated with the cohort"""
    size: AirbyteSortOrder
    """Size or scale of the cohort data"""
    type: AirbyteSortOrder
    """The type or category of the cohort"""
    view_count: AirbyteSortOrder
    """The total count of views on the cohort data"""
    viewers: AirbyteSortOrder
    """Users or viewers who have access to the cohort data"""


# Entity-specific condition types for cohorts
class CohortsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CohortsSearchFilter


class CohortsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CohortsSearchFilter


class CohortsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CohortsSearchFilter


class CohortsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CohortsSearchFilter


class CohortsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CohortsSearchFilter


class CohortsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CohortsSearchFilter


class CohortsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CohortsStringFilter


class CohortsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CohortsStringFilter


class CohortsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CohortsStringFilter


class CohortsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CohortsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CohortsInCondition = TypedDict("CohortsInCondition", {"in": CohortsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CohortsNotCondition = TypedDict("CohortsNotCondition", {"not": "CohortsCondition"}, total=False)
"""Negates the nested condition."""

CohortsAndCondition = TypedDict("CohortsAndCondition", {"and": "list[CohortsCondition]"}, total=False)
"""True if all nested conditions are true."""

CohortsOrCondition = TypedDict("CohortsOrCondition", {"or": "list[CohortsCondition]"}, total=False)
"""True if any nested condition is true."""

CohortsAnyCondition = TypedDict("CohortsAnyCondition", {"any": CohortsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all cohorts condition types
CohortsCondition = (
    CohortsEqCondition
    | CohortsNeqCondition
    | CohortsGtCondition
    | CohortsGteCondition
    | CohortsLtCondition
    | CohortsLteCondition
    | CohortsInCondition
    | CohortsLikeCondition
    | CohortsFuzzyCondition
    | CohortsKeywordCondition
    | CohortsContainsCondition
    | CohortsNotCondition
    | CohortsAndCondition
    | CohortsOrCondition
    | CohortsAnyCondition
)


class CohortsSearchQuery(TypedDict, total=False):
    """Search query for cohorts entity."""
    filter: CohortsCondition
    sort: list[CohortsSortFilter]


# ===== EVENTS_LIST SEARCH TYPES =====

class EventsListSearchFilter(TypedDict, total=False):
    """Available fields for filtering events_list search queries."""
    autohidden: bool | None
    """Whether the event is auto-hidden"""
    clusters_hidden: bool | None
    """Whether the event is hidden from clusters"""
    deleted: bool | None
    """Whether the event is deleted"""
    display: str | None
    """Display name of the event"""
    flow_hidden: bool | None
    """Whether the event is hidden from Pathfinder"""
    hidden: bool | None
    """Whether the event is hidden"""
    id: float | None
    """Unique identifier for the event type"""
    in_waitroom: bool | None
    """Whether the event is in the waitroom"""
    name: str | None
    """Name of the event type"""
    non_active: bool | None
    """Whether the event is marked as inactive"""
    timeline_hidden: Any
    """Whether the event is hidden from the timeline"""
    totals: float | None
    """Total number of times the event occurred this week"""
    totals_delta: float | None
    """Change in totals from the previous period"""
    value: str | None
    """Raw event name in the data"""


class EventsListInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    autohidden: list[bool]
    """Whether the event is auto-hidden"""
    clusters_hidden: list[bool]
    """Whether the event is hidden from clusters"""
    deleted: list[bool]
    """Whether the event is deleted"""
    display: list[str]
    """Display name of the event"""
    flow_hidden: list[bool]
    """Whether the event is hidden from Pathfinder"""
    hidden: list[bool]
    """Whether the event is hidden"""
    id: list[float]
    """Unique identifier for the event type"""
    in_waitroom: list[bool]
    """Whether the event is in the waitroom"""
    name: list[str]
    """Name of the event type"""
    non_active: list[bool]
    """Whether the event is marked as inactive"""
    timeline_hidden: list[Any]
    """Whether the event is hidden from the timeline"""
    totals: list[float]
    """Total number of times the event occurred this week"""
    totals_delta: list[float]
    """Change in totals from the previous period"""
    value: list[str]
    """Raw event name in the data"""


class EventsListAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    autohidden: Any
    """Whether the event is auto-hidden"""
    clusters_hidden: Any
    """Whether the event is hidden from clusters"""
    deleted: Any
    """Whether the event is deleted"""
    display: Any
    """Display name of the event"""
    flow_hidden: Any
    """Whether the event is hidden from Pathfinder"""
    hidden: Any
    """Whether the event is hidden"""
    id: Any
    """Unique identifier for the event type"""
    in_waitroom: Any
    """Whether the event is in the waitroom"""
    name: Any
    """Name of the event type"""
    non_active: Any
    """Whether the event is marked as inactive"""
    timeline_hidden: Any
    """Whether the event is hidden from the timeline"""
    totals: Any
    """Total number of times the event occurred this week"""
    totals_delta: Any
    """Change in totals from the previous period"""
    value: Any
    """Raw event name in the data"""


class EventsListStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    autohidden: str
    """Whether the event is auto-hidden"""
    clusters_hidden: str
    """Whether the event is hidden from clusters"""
    deleted: str
    """Whether the event is deleted"""
    display: str
    """Display name of the event"""
    flow_hidden: str
    """Whether the event is hidden from Pathfinder"""
    hidden: str
    """Whether the event is hidden"""
    id: str
    """Unique identifier for the event type"""
    in_waitroom: str
    """Whether the event is in the waitroom"""
    name: str
    """Name of the event type"""
    non_active: str
    """Whether the event is marked as inactive"""
    timeline_hidden: str
    """Whether the event is hidden from the timeline"""
    totals: str
    """Total number of times the event occurred this week"""
    totals_delta: str
    """Change in totals from the previous period"""
    value: str
    """Raw event name in the data"""


class EventsListSortFilter(TypedDict, total=False):
    """Available fields for sorting events_list search results."""
    autohidden: AirbyteSortOrder
    """Whether the event is auto-hidden"""
    clusters_hidden: AirbyteSortOrder
    """Whether the event is hidden from clusters"""
    deleted: AirbyteSortOrder
    """Whether the event is deleted"""
    display: AirbyteSortOrder
    """Display name of the event"""
    flow_hidden: AirbyteSortOrder
    """Whether the event is hidden from Pathfinder"""
    hidden: AirbyteSortOrder
    """Whether the event is hidden"""
    id: AirbyteSortOrder
    """Unique identifier for the event type"""
    in_waitroom: AirbyteSortOrder
    """Whether the event is in the waitroom"""
    name: AirbyteSortOrder
    """Name of the event type"""
    non_active: AirbyteSortOrder
    """Whether the event is marked as inactive"""
    timeline_hidden: AirbyteSortOrder
    """Whether the event is hidden from the timeline"""
    totals: AirbyteSortOrder
    """Total number of times the event occurred this week"""
    totals_delta: AirbyteSortOrder
    """Change in totals from the previous period"""
    value: AirbyteSortOrder
    """Raw event name in the data"""


# Entity-specific condition types for events_list
class EventsListEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: EventsListSearchFilter


class EventsListNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: EventsListSearchFilter


class EventsListGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: EventsListSearchFilter


class EventsListGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: EventsListSearchFilter


class EventsListLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: EventsListSearchFilter


class EventsListLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: EventsListSearchFilter


class EventsListLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: EventsListStringFilter


class EventsListFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: EventsListStringFilter


class EventsListKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: EventsListStringFilter


class EventsListContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: EventsListAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
EventsListInCondition = TypedDict("EventsListInCondition", {"in": EventsListInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

EventsListNotCondition = TypedDict("EventsListNotCondition", {"not": "EventsListCondition"}, total=False)
"""Negates the nested condition."""

EventsListAndCondition = TypedDict("EventsListAndCondition", {"and": "list[EventsListCondition]"}, total=False)
"""True if all nested conditions are true."""

EventsListOrCondition = TypedDict("EventsListOrCondition", {"or": "list[EventsListCondition]"}, total=False)
"""True if any nested condition is true."""

EventsListAnyCondition = TypedDict("EventsListAnyCondition", {"any": EventsListAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all events_list condition types
EventsListCondition = (
    EventsListEqCondition
    | EventsListNeqCondition
    | EventsListGtCondition
    | EventsListGteCondition
    | EventsListLtCondition
    | EventsListLteCondition
    | EventsListInCondition
    | EventsListLikeCondition
    | EventsListFuzzyCondition
    | EventsListKeywordCondition
    | EventsListContainsCondition
    | EventsListNotCondition
    | EventsListAndCondition
    | EventsListOrCondition
    | EventsListAnyCondition
)


class EventsListSearchQuery(TypedDict, total=False):
    """Search query for events_list entity."""
    filter: EventsListCondition
    sort: list[EventsListSortFilter]


# ===== ACTIVE_USERS SEARCH TYPES =====

class ActiveUsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering active_users search queries."""
    date: str | None
    """The date for which the active user data is reported"""
    statistics: dict[str, Any] | None
    """The statistics related to the active users for the given date"""


class ActiveUsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    date: list[str]
    """The date for which the active user data is reported"""
    statistics: list[dict[str, Any]]
    """The statistics related to the active users for the given date"""


class ActiveUsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    date: Any
    """The date for which the active user data is reported"""
    statistics: Any
    """The statistics related to the active users for the given date"""


class ActiveUsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    date: str
    """The date for which the active user data is reported"""
    statistics: str
    """The statistics related to the active users for the given date"""


class ActiveUsersSortFilter(TypedDict, total=False):
    """Available fields for sorting active_users search results."""
    date: AirbyteSortOrder
    """The date for which the active user data is reported"""
    statistics: AirbyteSortOrder
    """The statistics related to the active users for the given date"""


# Entity-specific condition types for active_users
class ActiveUsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ActiveUsersSearchFilter


class ActiveUsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ActiveUsersSearchFilter


class ActiveUsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ActiveUsersSearchFilter


class ActiveUsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ActiveUsersSearchFilter


class ActiveUsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ActiveUsersSearchFilter


class ActiveUsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ActiveUsersSearchFilter


class ActiveUsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ActiveUsersStringFilter


class ActiveUsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ActiveUsersStringFilter


class ActiveUsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ActiveUsersStringFilter


class ActiveUsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ActiveUsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ActiveUsersInCondition = TypedDict("ActiveUsersInCondition", {"in": ActiveUsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ActiveUsersNotCondition = TypedDict("ActiveUsersNotCondition", {"not": "ActiveUsersCondition"}, total=False)
"""Negates the nested condition."""

ActiveUsersAndCondition = TypedDict("ActiveUsersAndCondition", {"and": "list[ActiveUsersCondition]"}, total=False)
"""True if all nested conditions are true."""

ActiveUsersOrCondition = TypedDict("ActiveUsersOrCondition", {"or": "list[ActiveUsersCondition]"}, total=False)
"""True if any nested condition is true."""

ActiveUsersAnyCondition = TypedDict("ActiveUsersAnyCondition", {"any": ActiveUsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all active_users condition types
ActiveUsersCondition = (
    ActiveUsersEqCondition
    | ActiveUsersNeqCondition
    | ActiveUsersGtCondition
    | ActiveUsersGteCondition
    | ActiveUsersLtCondition
    | ActiveUsersLteCondition
    | ActiveUsersInCondition
    | ActiveUsersLikeCondition
    | ActiveUsersFuzzyCondition
    | ActiveUsersKeywordCondition
    | ActiveUsersContainsCondition
    | ActiveUsersNotCondition
    | ActiveUsersAndCondition
    | ActiveUsersOrCondition
    | ActiveUsersAnyCondition
)


class ActiveUsersSearchQuery(TypedDict, total=False):
    """Search query for active_users entity."""
    filter: ActiveUsersCondition
    sort: list[ActiveUsersSortFilter]


# ===== AVERAGE_SESSION_LENGTH SEARCH TYPES =====

class AverageSessionLengthSearchFilter(TypedDict, total=False):
    """Available fields for filtering average_session_length search queries."""
    date: str | None
    """The date on which the session occurred"""
    length: float | None
    """The duration of the session in seconds"""


class AverageSessionLengthInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    date: list[str]
    """The date on which the session occurred"""
    length: list[float]
    """The duration of the session in seconds"""


class AverageSessionLengthAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    date: Any
    """The date on which the session occurred"""
    length: Any
    """The duration of the session in seconds"""


class AverageSessionLengthStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    date: str
    """The date on which the session occurred"""
    length: str
    """The duration of the session in seconds"""


class AverageSessionLengthSortFilter(TypedDict, total=False):
    """Available fields for sorting average_session_length search results."""
    date: AirbyteSortOrder
    """The date on which the session occurred"""
    length: AirbyteSortOrder
    """The duration of the session in seconds"""


# Entity-specific condition types for average_session_length
class AverageSessionLengthEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AverageSessionLengthSearchFilter


class AverageSessionLengthNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AverageSessionLengthSearchFilter


class AverageSessionLengthGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AverageSessionLengthSearchFilter


class AverageSessionLengthGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AverageSessionLengthSearchFilter


class AverageSessionLengthLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AverageSessionLengthSearchFilter


class AverageSessionLengthLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AverageSessionLengthSearchFilter


class AverageSessionLengthLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AverageSessionLengthStringFilter


class AverageSessionLengthFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AverageSessionLengthStringFilter


class AverageSessionLengthKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AverageSessionLengthStringFilter


class AverageSessionLengthContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AverageSessionLengthAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AverageSessionLengthInCondition = TypedDict("AverageSessionLengthInCondition", {"in": AverageSessionLengthInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AverageSessionLengthNotCondition = TypedDict("AverageSessionLengthNotCondition", {"not": "AverageSessionLengthCondition"}, total=False)
"""Negates the nested condition."""

AverageSessionLengthAndCondition = TypedDict("AverageSessionLengthAndCondition", {"and": "list[AverageSessionLengthCondition]"}, total=False)
"""True if all nested conditions are true."""

AverageSessionLengthOrCondition = TypedDict("AverageSessionLengthOrCondition", {"or": "list[AverageSessionLengthCondition]"}, total=False)
"""True if any nested condition is true."""

AverageSessionLengthAnyCondition = TypedDict("AverageSessionLengthAnyCondition", {"any": AverageSessionLengthAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all average_session_length condition types
AverageSessionLengthCondition = (
    AverageSessionLengthEqCondition
    | AverageSessionLengthNeqCondition
    | AverageSessionLengthGtCondition
    | AverageSessionLengthGteCondition
    | AverageSessionLengthLtCondition
    | AverageSessionLengthLteCondition
    | AverageSessionLengthInCondition
    | AverageSessionLengthLikeCondition
    | AverageSessionLengthFuzzyCondition
    | AverageSessionLengthKeywordCondition
    | AverageSessionLengthContainsCondition
    | AverageSessionLengthNotCondition
    | AverageSessionLengthAndCondition
    | AverageSessionLengthOrCondition
    | AverageSessionLengthAnyCondition
)


class AverageSessionLengthSearchQuery(TypedDict, total=False):
    """Search query for average_session_length entity."""
    filter: AverageSessionLengthCondition
    sort: list[AverageSessionLengthSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
