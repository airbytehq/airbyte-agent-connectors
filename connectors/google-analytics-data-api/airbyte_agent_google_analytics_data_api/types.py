"""
Type definitions for google-analytics-data-api connector.
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

class WebsiteOverviewListParamsDaterangesItem(TypedDict):
    """Nested schema for WebsiteOverviewListParams.dateRanges_item"""
    startDate: NotRequired[str]
    endDate: NotRequired[str]

class WebsiteOverviewListParamsDimensionsItem(TypedDict):
    """Nested schema for WebsiteOverviewListParams.dimensions_item"""
    name: NotRequired[str]

class WebsiteOverviewListParamsMetricsItem(TypedDict):
    """Nested schema for WebsiteOverviewListParams.metrics_item"""
    name: NotRequired[str]

class DailyActiveUsersListParamsDaterangesItem(TypedDict):
    """Nested schema for DailyActiveUsersListParams.dateRanges_item"""
    startDate: NotRequired[str]
    endDate: NotRequired[str]

class DailyActiveUsersListParamsDimensionsItem(TypedDict):
    """Nested schema for DailyActiveUsersListParams.dimensions_item"""
    name: NotRequired[str]

class DailyActiveUsersListParamsMetricsItem(TypedDict):
    """Nested schema for DailyActiveUsersListParams.metrics_item"""
    name: NotRequired[str]

class WeeklyActiveUsersListParamsDaterangesItem(TypedDict):
    """Nested schema for WeeklyActiveUsersListParams.dateRanges_item"""
    startDate: NotRequired[str]
    endDate: NotRequired[str]

class WeeklyActiveUsersListParamsDimensionsItem(TypedDict):
    """Nested schema for WeeklyActiveUsersListParams.dimensions_item"""
    name: NotRequired[str]

class WeeklyActiveUsersListParamsMetricsItem(TypedDict):
    """Nested schema for WeeklyActiveUsersListParams.metrics_item"""
    name: NotRequired[str]

class FourWeeklyActiveUsersListParamsDaterangesItem(TypedDict):
    """Nested schema for FourWeeklyActiveUsersListParams.dateRanges_item"""
    startDate: NotRequired[str]
    endDate: NotRequired[str]

class FourWeeklyActiveUsersListParamsDimensionsItem(TypedDict):
    """Nested schema for FourWeeklyActiveUsersListParams.dimensions_item"""
    name: NotRequired[str]

class FourWeeklyActiveUsersListParamsMetricsItem(TypedDict):
    """Nested schema for FourWeeklyActiveUsersListParams.metrics_item"""
    name: NotRequired[str]

class TrafficSourcesListParamsDaterangesItem(TypedDict):
    """Nested schema for TrafficSourcesListParams.dateRanges_item"""
    startDate: NotRequired[str]
    endDate: NotRequired[str]

class TrafficSourcesListParamsDimensionsItem(TypedDict):
    """Nested schema for TrafficSourcesListParams.dimensions_item"""
    name: NotRequired[str]

class TrafficSourcesListParamsMetricsItem(TypedDict):
    """Nested schema for TrafficSourcesListParams.metrics_item"""
    name: NotRequired[str]

class PagesListParamsDaterangesItem(TypedDict):
    """Nested schema for PagesListParams.dateRanges_item"""
    startDate: NotRequired[str]
    endDate: NotRequired[str]

class PagesListParamsDimensionsItem(TypedDict):
    """Nested schema for PagesListParams.dimensions_item"""
    name: NotRequired[str]

class PagesListParamsMetricsItem(TypedDict):
    """Nested schema for PagesListParams.metrics_item"""
    name: NotRequired[str]

class DevicesListParamsDaterangesItem(TypedDict):
    """Nested schema for DevicesListParams.dateRanges_item"""
    startDate: NotRequired[str]
    endDate: NotRequired[str]

class DevicesListParamsDimensionsItem(TypedDict):
    """Nested schema for DevicesListParams.dimensions_item"""
    name: NotRequired[str]

class DevicesListParamsMetricsItem(TypedDict):
    """Nested schema for DevicesListParams.metrics_item"""
    name: NotRequired[str]

class LocationsListParamsDaterangesItem(TypedDict):
    """Nested schema for LocationsListParams.dateRanges_item"""
    startDate: NotRequired[str]
    endDate: NotRequired[str]

class LocationsListParamsDimensionsItem(TypedDict):
    """Nested schema for LocationsListParams.dimensions_item"""
    name: NotRequired[str]

class LocationsListParamsMetricsItem(TypedDict):
    """Nested schema for LocationsListParams.metrics_item"""
    name: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class WebsiteOverviewListParams(TypedDict):
    """Parameters for website_overview.list operation"""
    date_ranges: NotRequired[list[WebsiteOverviewListParamsDaterangesItem]]
    dimensions: NotRequired[list[WebsiteOverviewListParamsDimensionsItem]]
    metrics: NotRequired[list[WebsiteOverviewListParamsMetricsItem]]
    keep_empty_rows: NotRequired[bool]
    return_property_quota: NotRequired[bool]
    limit: NotRequired[int]
    property_id: str

class DailyActiveUsersListParams(TypedDict):
    """Parameters for daily_active_users.list operation"""
    date_ranges: NotRequired[list[DailyActiveUsersListParamsDaterangesItem]]
    dimensions: NotRequired[list[DailyActiveUsersListParamsDimensionsItem]]
    metrics: NotRequired[list[DailyActiveUsersListParamsMetricsItem]]
    keep_empty_rows: NotRequired[bool]
    return_property_quota: NotRequired[bool]
    limit: NotRequired[int]
    property_id: str

class WeeklyActiveUsersListParams(TypedDict):
    """Parameters for weekly_active_users.list operation"""
    date_ranges: NotRequired[list[WeeklyActiveUsersListParamsDaterangesItem]]
    dimensions: NotRequired[list[WeeklyActiveUsersListParamsDimensionsItem]]
    metrics: NotRequired[list[WeeklyActiveUsersListParamsMetricsItem]]
    keep_empty_rows: NotRequired[bool]
    return_property_quota: NotRequired[bool]
    limit: NotRequired[int]
    property_id: str

class FourWeeklyActiveUsersListParams(TypedDict):
    """Parameters for four_weekly_active_users.list operation"""
    date_ranges: NotRequired[list[FourWeeklyActiveUsersListParamsDaterangesItem]]
    dimensions: NotRequired[list[FourWeeklyActiveUsersListParamsDimensionsItem]]
    metrics: NotRequired[list[FourWeeklyActiveUsersListParamsMetricsItem]]
    keep_empty_rows: NotRequired[bool]
    return_property_quota: NotRequired[bool]
    limit: NotRequired[int]
    property_id: str

class TrafficSourcesListParams(TypedDict):
    """Parameters for traffic_sources.list operation"""
    date_ranges: NotRequired[list[TrafficSourcesListParamsDaterangesItem]]
    dimensions: NotRequired[list[TrafficSourcesListParamsDimensionsItem]]
    metrics: NotRequired[list[TrafficSourcesListParamsMetricsItem]]
    keep_empty_rows: NotRequired[bool]
    return_property_quota: NotRequired[bool]
    limit: NotRequired[int]
    property_id: str

class PagesListParams(TypedDict):
    """Parameters for pages.list operation"""
    date_ranges: NotRequired[list[PagesListParamsDaterangesItem]]
    dimensions: NotRequired[list[PagesListParamsDimensionsItem]]
    metrics: NotRequired[list[PagesListParamsMetricsItem]]
    keep_empty_rows: NotRequired[bool]
    return_property_quota: NotRequired[bool]
    limit: NotRequired[int]
    property_id: str

class DevicesListParams(TypedDict):
    """Parameters for devices.list operation"""
    date_ranges: NotRequired[list[DevicesListParamsDaterangesItem]]
    dimensions: NotRequired[list[DevicesListParamsDimensionsItem]]
    metrics: NotRequired[list[DevicesListParamsMetricsItem]]
    keep_empty_rows: NotRequired[bool]
    return_property_quota: NotRequired[bool]
    limit: NotRequired[int]
    property_id: str

class LocationsListParams(TypedDict):
    """Parameters for locations.list operation"""
    date_ranges: NotRequired[list[LocationsListParamsDaterangesItem]]
    dimensions: NotRequired[list[LocationsListParamsDimensionsItem]]
    metrics: NotRequired[list[LocationsListParamsMetricsItem]]
    keep_empty_rows: NotRequired[bool]
    return_property_quota: NotRequired[bool]
    limit: NotRequired[int]
    property_id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== WEBSITE_OVERVIEW SEARCH TYPES =====

class WebsiteOverviewSearchFilter(TypedDict, total=False):
    """Available fields for filtering website_overview search queries."""
    average_session_duration: float | None
    """Average duration of sessions in seconds"""
    bounce_rate: float | None
    """Percentage of sessions that were single-page with no interaction"""
    date: str | None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None
    """End date of the reporting period"""
    new_users: int | None
    """Number of first-time users"""
    property_id: str
    """GA4 property ID"""
    screen_page_views: int | None
    """Total number of screen or page views"""
    screen_page_views_per_session: float | None
    """Average page views per session"""
    sessions: int | None
    """Total number of sessions"""
    sessions_per_user: float | None
    """Average number of sessions per user"""
    start_date: str | None
    """Start date of the reporting period"""
    total_users: int | None
    """Total number of unique users"""


class WebsiteOverviewInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    average_session_duration: list[float]
    """Average duration of sessions in seconds"""
    bounce_rate: list[float]
    """Percentage of sessions that were single-page with no interaction"""
    date: list[str]
    """Date of the report row in YYYYMMDD format"""
    end_date: list[str]
    """End date of the reporting period"""
    new_users: list[int]
    """Number of first-time users"""
    property_id: list[str]
    """GA4 property ID"""
    screen_page_views: list[int]
    """Total number of screen or page views"""
    screen_page_views_per_session: list[float]
    """Average page views per session"""
    sessions: list[int]
    """Total number of sessions"""
    sessions_per_user: list[float]
    """Average number of sessions per user"""
    start_date: list[str]
    """Start date of the reporting period"""
    total_users: list[int]
    """Total number of unique users"""


class WebsiteOverviewAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    average_session_duration: Any
    """Average duration of sessions in seconds"""
    bounce_rate: Any
    """Percentage of sessions that were single-page with no interaction"""
    date: Any
    """Date of the report row in YYYYMMDD format"""
    end_date: Any
    """End date of the reporting period"""
    new_users: Any
    """Number of first-time users"""
    property_id: Any
    """GA4 property ID"""
    screen_page_views: Any
    """Total number of screen or page views"""
    screen_page_views_per_session: Any
    """Average page views per session"""
    sessions: Any
    """Total number of sessions"""
    sessions_per_user: Any
    """Average number of sessions per user"""
    start_date: Any
    """Start date of the reporting period"""
    total_users: Any
    """Total number of unique users"""


class WebsiteOverviewStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    average_session_duration: str
    """Average duration of sessions in seconds"""
    bounce_rate: str
    """Percentage of sessions that were single-page with no interaction"""
    date: str
    """Date of the report row in YYYYMMDD format"""
    end_date: str
    """End date of the reporting period"""
    new_users: str
    """Number of first-time users"""
    property_id: str
    """GA4 property ID"""
    screen_page_views: str
    """Total number of screen or page views"""
    screen_page_views_per_session: str
    """Average page views per session"""
    sessions: str
    """Total number of sessions"""
    sessions_per_user: str
    """Average number of sessions per user"""
    start_date: str
    """Start date of the reporting period"""
    total_users: str
    """Total number of unique users"""


class WebsiteOverviewSortFilter(TypedDict, total=False):
    """Available fields for sorting website_overview search results."""
    average_session_duration: AirbyteSortOrder
    """Average duration of sessions in seconds"""
    bounce_rate: AirbyteSortOrder
    """Percentage of sessions that were single-page with no interaction"""
    date: AirbyteSortOrder
    """Date of the report row in YYYYMMDD format"""
    end_date: AirbyteSortOrder
    """End date of the reporting period"""
    new_users: AirbyteSortOrder
    """Number of first-time users"""
    property_id: AirbyteSortOrder
    """GA4 property ID"""
    screen_page_views: AirbyteSortOrder
    """Total number of screen or page views"""
    screen_page_views_per_session: AirbyteSortOrder
    """Average page views per session"""
    sessions: AirbyteSortOrder
    """Total number of sessions"""
    sessions_per_user: AirbyteSortOrder
    """Average number of sessions per user"""
    start_date: AirbyteSortOrder
    """Start date of the reporting period"""
    total_users: AirbyteSortOrder
    """Total number of unique users"""


# Entity-specific condition types for website_overview
class WebsiteOverviewEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: WebsiteOverviewSearchFilter


class WebsiteOverviewNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: WebsiteOverviewSearchFilter


class WebsiteOverviewGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: WebsiteOverviewSearchFilter


class WebsiteOverviewGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: WebsiteOverviewSearchFilter


class WebsiteOverviewLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: WebsiteOverviewSearchFilter


class WebsiteOverviewLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: WebsiteOverviewSearchFilter


class WebsiteOverviewLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: WebsiteOverviewStringFilter


class WebsiteOverviewFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: WebsiteOverviewStringFilter


class WebsiteOverviewKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: WebsiteOverviewStringFilter


class WebsiteOverviewContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: WebsiteOverviewAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
WebsiteOverviewInCondition = TypedDict("WebsiteOverviewInCondition", {"in": WebsiteOverviewInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

WebsiteOverviewNotCondition = TypedDict("WebsiteOverviewNotCondition", {"not": "WebsiteOverviewCondition"}, total=False)
"""Negates the nested condition."""

WebsiteOverviewAndCondition = TypedDict("WebsiteOverviewAndCondition", {"and": "list[WebsiteOverviewCondition]"}, total=False)
"""True if all nested conditions are true."""

WebsiteOverviewOrCondition = TypedDict("WebsiteOverviewOrCondition", {"or": "list[WebsiteOverviewCondition]"}, total=False)
"""True if any nested condition is true."""

WebsiteOverviewAnyCondition = TypedDict("WebsiteOverviewAnyCondition", {"any": WebsiteOverviewAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all website_overview condition types
WebsiteOverviewCondition = (
    WebsiteOverviewEqCondition
    | WebsiteOverviewNeqCondition
    | WebsiteOverviewGtCondition
    | WebsiteOverviewGteCondition
    | WebsiteOverviewLtCondition
    | WebsiteOverviewLteCondition
    | WebsiteOverviewInCondition
    | WebsiteOverviewLikeCondition
    | WebsiteOverviewFuzzyCondition
    | WebsiteOverviewKeywordCondition
    | WebsiteOverviewContainsCondition
    | WebsiteOverviewNotCondition
    | WebsiteOverviewAndCondition
    | WebsiteOverviewOrCondition
    | WebsiteOverviewAnyCondition
)


class WebsiteOverviewSearchQuery(TypedDict, total=False):
    """Search query for website_overview entity."""
    filter: WebsiteOverviewCondition
    sort: list[WebsiteOverviewSortFilter]


# ===== DAILY_ACTIVE_USERS SEARCH TYPES =====

class DailyActiveUsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering daily_active_users search queries."""
    active1_day_users: int | None
    """Number of distinct users active in the last 1 day"""
    date: str | None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None
    """End date of the reporting period"""
    property_id: str
    """GA4 property ID"""
    start_date: str | None
    """Start date of the reporting period"""


class DailyActiveUsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active1_day_users: list[int]
    """Number of distinct users active in the last 1 day"""
    date: list[str]
    """Date of the report row in YYYYMMDD format"""
    end_date: list[str]
    """End date of the reporting period"""
    property_id: list[str]
    """GA4 property ID"""
    start_date: list[str]
    """Start date of the reporting period"""


class DailyActiveUsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active1_day_users: Any
    """Number of distinct users active in the last 1 day"""
    date: Any
    """Date of the report row in YYYYMMDD format"""
    end_date: Any
    """End date of the reporting period"""
    property_id: Any
    """GA4 property ID"""
    start_date: Any
    """Start date of the reporting period"""


class DailyActiveUsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    active1_day_users: str
    """Number of distinct users active in the last 1 day"""
    date: str
    """Date of the report row in YYYYMMDD format"""
    end_date: str
    """End date of the reporting period"""
    property_id: str
    """GA4 property ID"""
    start_date: str
    """Start date of the reporting period"""


class DailyActiveUsersSortFilter(TypedDict, total=False):
    """Available fields for sorting daily_active_users search results."""
    active1_day_users: AirbyteSortOrder
    """Number of distinct users active in the last 1 day"""
    date: AirbyteSortOrder
    """Date of the report row in YYYYMMDD format"""
    end_date: AirbyteSortOrder
    """End date of the reporting period"""
    property_id: AirbyteSortOrder
    """GA4 property ID"""
    start_date: AirbyteSortOrder
    """Start date of the reporting period"""


# Entity-specific condition types for daily_active_users
class DailyActiveUsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DailyActiveUsersSearchFilter


class DailyActiveUsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DailyActiveUsersSearchFilter


class DailyActiveUsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DailyActiveUsersSearchFilter


class DailyActiveUsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DailyActiveUsersSearchFilter


class DailyActiveUsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DailyActiveUsersSearchFilter


class DailyActiveUsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DailyActiveUsersSearchFilter


class DailyActiveUsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DailyActiveUsersStringFilter


class DailyActiveUsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DailyActiveUsersStringFilter


class DailyActiveUsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DailyActiveUsersStringFilter


class DailyActiveUsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DailyActiveUsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DailyActiveUsersInCondition = TypedDict("DailyActiveUsersInCondition", {"in": DailyActiveUsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DailyActiveUsersNotCondition = TypedDict("DailyActiveUsersNotCondition", {"not": "DailyActiveUsersCondition"}, total=False)
"""Negates the nested condition."""

DailyActiveUsersAndCondition = TypedDict("DailyActiveUsersAndCondition", {"and": "list[DailyActiveUsersCondition]"}, total=False)
"""True if all nested conditions are true."""

DailyActiveUsersOrCondition = TypedDict("DailyActiveUsersOrCondition", {"or": "list[DailyActiveUsersCondition]"}, total=False)
"""True if any nested condition is true."""

DailyActiveUsersAnyCondition = TypedDict("DailyActiveUsersAnyCondition", {"any": DailyActiveUsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all daily_active_users condition types
DailyActiveUsersCondition = (
    DailyActiveUsersEqCondition
    | DailyActiveUsersNeqCondition
    | DailyActiveUsersGtCondition
    | DailyActiveUsersGteCondition
    | DailyActiveUsersLtCondition
    | DailyActiveUsersLteCondition
    | DailyActiveUsersInCondition
    | DailyActiveUsersLikeCondition
    | DailyActiveUsersFuzzyCondition
    | DailyActiveUsersKeywordCondition
    | DailyActiveUsersContainsCondition
    | DailyActiveUsersNotCondition
    | DailyActiveUsersAndCondition
    | DailyActiveUsersOrCondition
    | DailyActiveUsersAnyCondition
)


class DailyActiveUsersSearchQuery(TypedDict, total=False):
    """Search query for daily_active_users entity."""
    filter: DailyActiveUsersCondition
    sort: list[DailyActiveUsersSortFilter]


# ===== WEEKLY_ACTIVE_USERS SEARCH TYPES =====

class WeeklyActiveUsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering weekly_active_users search queries."""
    active7_day_users: int | None
    """Number of distinct users active in the last 7 days"""
    date: str | None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None
    """End date of the reporting period"""
    property_id: str
    """GA4 property ID"""
    start_date: str | None
    """Start date of the reporting period"""


class WeeklyActiveUsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active7_day_users: list[int]
    """Number of distinct users active in the last 7 days"""
    date: list[str]
    """Date of the report row in YYYYMMDD format"""
    end_date: list[str]
    """End date of the reporting period"""
    property_id: list[str]
    """GA4 property ID"""
    start_date: list[str]
    """Start date of the reporting period"""


class WeeklyActiveUsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active7_day_users: Any
    """Number of distinct users active in the last 7 days"""
    date: Any
    """Date of the report row in YYYYMMDD format"""
    end_date: Any
    """End date of the reporting period"""
    property_id: Any
    """GA4 property ID"""
    start_date: Any
    """Start date of the reporting period"""


class WeeklyActiveUsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    active7_day_users: str
    """Number of distinct users active in the last 7 days"""
    date: str
    """Date of the report row in YYYYMMDD format"""
    end_date: str
    """End date of the reporting period"""
    property_id: str
    """GA4 property ID"""
    start_date: str
    """Start date of the reporting period"""


class WeeklyActiveUsersSortFilter(TypedDict, total=False):
    """Available fields for sorting weekly_active_users search results."""
    active7_day_users: AirbyteSortOrder
    """Number of distinct users active in the last 7 days"""
    date: AirbyteSortOrder
    """Date of the report row in YYYYMMDD format"""
    end_date: AirbyteSortOrder
    """End date of the reporting period"""
    property_id: AirbyteSortOrder
    """GA4 property ID"""
    start_date: AirbyteSortOrder
    """Start date of the reporting period"""


# Entity-specific condition types for weekly_active_users
class WeeklyActiveUsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: WeeklyActiveUsersSearchFilter


class WeeklyActiveUsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: WeeklyActiveUsersSearchFilter


class WeeklyActiveUsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: WeeklyActiveUsersSearchFilter


class WeeklyActiveUsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: WeeklyActiveUsersSearchFilter


class WeeklyActiveUsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: WeeklyActiveUsersSearchFilter


class WeeklyActiveUsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: WeeklyActiveUsersSearchFilter


class WeeklyActiveUsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: WeeklyActiveUsersStringFilter


class WeeklyActiveUsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: WeeklyActiveUsersStringFilter


class WeeklyActiveUsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: WeeklyActiveUsersStringFilter


class WeeklyActiveUsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: WeeklyActiveUsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
WeeklyActiveUsersInCondition = TypedDict("WeeklyActiveUsersInCondition", {"in": WeeklyActiveUsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

WeeklyActiveUsersNotCondition = TypedDict("WeeklyActiveUsersNotCondition", {"not": "WeeklyActiveUsersCondition"}, total=False)
"""Negates the nested condition."""

WeeklyActiveUsersAndCondition = TypedDict("WeeklyActiveUsersAndCondition", {"and": "list[WeeklyActiveUsersCondition]"}, total=False)
"""True if all nested conditions are true."""

WeeklyActiveUsersOrCondition = TypedDict("WeeklyActiveUsersOrCondition", {"or": "list[WeeklyActiveUsersCondition]"}, total=False)
"""True if any nested condition is true."""

WeeklyActiveUsersAnyCondition = TypedDict("WeeklyActiveUsersAnyCondition", {"any": WeeklyActiveUsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all weekly_active_users condition types
WeeklyActiveUsersCondition = (
    WeeklyActiveUsersEqCondition
    | WeeklyActiveUsersNeqCondition
    | WeeklyActiveUsersGtCondition
    | WeeklyActiveUsersGteCondition
    | WeeklyActiveUsersLtCondition
    | WeeklyActiveUsersLteCondition
    | WeeklyActiveUsersInCondition
    | WeeklyActiveUsersLikeCondition
    | WeeklyActiveUsersFuzzyCondition
    | WeeklyActiveUsersKeywordCondition
    | WeeklyActiveUsersContainsCondition
    | WeeklyActiveUsersNotCondition
    | WeeklyActiveUsersAndCondition
    | WeeklyActiveUsersOrCondition
    | WeeklyActiveUsersAnyCondition
)


class WeeklyActiveUsersSearchQuery(TypedDict, total=False):
    """Search query for weekly_active_users entity."""
    filter: WeeklyActiveUsersCondition
    sort: list[WeeklyActiveUsersSortFilter]


# ===== FOUR_WEEKLY_ACTIVE_USERS SEARCH TYPES =====

class FourWeeklyActiveUsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering four_weekly_active_users search queries."""
    active28_day_users: int | None
    """Number of distinct users active in the last 28 days"""
    date: str | None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None
    """End date of the reporting period"""
    property_id: str
    """GA4 property ID"""
    start_date: str | None
    """Start date of the reporting period"""


class FourWeeklyActiveUsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active28_day_users: list[int]
    """Number of distinct users active in the last 28 days"""
    date: list[str]
    """Date of the report row in YYYYMMDD format"""
    end_date: list[str]
    """End date of the reporting period"""
    property_id: list[str]
    """GA4 property ID"""
    start_date: list[str]
    """Start date of the reporting period"""


class FourWeeklyActiveUsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active28_day_users: Any
    """Number of distinct users active in the last 28 days"""
    date: Any
    """Date of the report row in YYYYMMDD format"""
    end_date: Any
    """End date of the reporting period"""
    property_id: Any
    """GA4 property ID"""
    start_date: Any
    """Start date of the reporting period"""


class FourWeeklyActiveUsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    active28_day_users: str
    """Number of distinct users active in the last 28 days"""
    date: str
    """Date of the report row in YYYYMMDD format"""
    end_date: str
    """End date of the reporting period"""
    property_id: str
    """GA4 property ID"""
    start_date: str
    """Start date of the reporting period"""


class FourWeeklyActiveUsersSortFilter(TypedDict, total=False):
    """Available fields for sorting four_weekly_active_users search results."""
    active28_day_users: AirbyteSortOrder
    """Number of distinct users active in the last 28 days"""
    date: AirbyteSortOrder
    """Date of the report row in YYYYMMDD format"""
    end_date: AirbyteSortOrder
    """End date of the reporting period"""
    property_id: AirbyteSortOrder
    """GA4 property ID"""
    start_date: AirbyteSortOrder
    """Start date of the reporting period"""


# Entity-specific condition types for four_weekly_active_users
class FourWeeklyActiveUsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: FourWeeklyActiveUsersSearchFilter


class FourWeeklyActiveUsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: FourWeeklyActiveUsersSearchFilter


class FourWeeklyActiveUsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: FourWeeklyActiveUsersSearchFilter


class FourWeeklyActiveUsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: FourWeeklyActiveUsersSearchFilter


class FourWeeklyActiveUsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: FourWeeklyActiveUsersSearchFilter


class FourWeeklyActiveUsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: FourWeeklyActiveUsersSearchFilter


class FourWeeklyActiveUsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: FourWeeklyActiveUsersStringFilter


class FourWeeklyActiveUsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: FourWeeklyActiveUsersStringFilter


class FourWeeklyActiveUsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: FourWeeklyActiveUsersStringFilter


class FourWeeklyActiveUsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: FourWeeklyActiveUsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
FourWeeklyActiveUsersInCondition = TypedDict("FourWeeklyActiveUsersInCondition", {"in": FourWeeklyActiveUsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

FourWeeklyActiveUsersNotCondition = TypedDict("FourWeeklyActiveUsersNotCondition", {"not": "FourWeeklyActiveUsersCondition"}, total=False)
"""Negates the nested condition."""

FourWeeklyActiveUsersAndCondition = TypedDict("FourWeeklyActiveUsersAndCondition", {"and": "list[FourWeeklyActiveUsersCondition]"}, total=False)
"""True if all nested conditions are true."""

FourWeeklyActiveUsersOrCondition = TypedDict("FourWeeklyActiveUsersOrCondition", {"or": "list[FourWeeklyActiveUsersCondition]"}, total=False)
"""True if any nested condition is true."""

FourWeeklyActiveUsersAnyCondition = TypedDict("FourWeeklyActiveUsersAnyCondition", {"any": FourWeeklyActiveUsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all four_weekly_active_users condition types
FourWeeklyActiveUsersCondition = (
    FourWeeklyActiveUsersEqCondition
    | FourWeeklyActiveUsersNeqCondition
    | FourWeeklyActiveUsersGtCondition
    | FourWeeklyActiveUsersGteCondition
    | FourWeeklyActiveUsersLtCondition
    | FourWeeklyActiveUsersLteCondition
    | FourWeeklyActiveUsersInCondition
    | FourWeeklyActiveUsersLikeCondition
    | FourWeeklyActiveUsersFuzzyCondition
    | FourWeeklyActiveUsersKeywordCondition
    | FourWeeklyActiveUsersContainsCondition
    | FourWeeklyActiveUsersNotCondition
    | FourWeeklyActiveUsersAndCondition
    | FourWeeklyActiveUsersOrCondition
    | FourWeeklyActiveUsersAnyCondition
)


class FourWeeklyActiveUsersSearchQuery(TypedDict, total=False):
    """Search query for four_weekly_active_users entity."""
    filter: FourWeeklyActiveUsersCondition
    sort: list[FourWeeklyActiveUsersSortFilter]


# ===== TRAFFIC_SOURCES SEARCH TYPES =====

class TrafficSourcesSearchFilter(TypedDict, total=False):
    """Available fields for filtering traffic_sources search queries."""
    average_session_duration: float | None
    """Average duration of sessions in seconds"""
    bounce_rate: float | None
    """Percentage of sessions that were single-page with no interaction"""
    date: str | None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None
    """End date of the reporting period"""
    new_users: int | None
    """Number of first-time users"""
    property_id: str
    """GA4 property ID"""
    screen_page_views: int | None
    """Total number of screen or page views"""
    screen_page_views_per_session: float | None
    """Average page views per session"""
    session_medium: str | None
    """The medium of the traffic source (e.g., organic, cpc, referral)"""
    session_source: str | None
    """The source of the traffic (e.g., google, direct)"""
    sessions: int | None
    """Total number of sessions"""
    sessions_per_user: float | None
    """Average number of sessions per user"""
    start_date: str | None
    """Start date of the reporting period"""
    total_users: int | None
    """Total number of unique users"""


class TrafficSourcesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    average_session_duration: list[float]
    """Average duration of sessions in seconds"""
    bounce_rate: list[float]
    """Percentage of sessions that were single-page with no interaction"""
    date: list[str]
    """Date of the report row in YYYYMMDD format"""
    end_date: list[str]
    """End date of the reporting period"""
    new_users: list[int]
    """Number of first-time users"""
    property_id: list[str]
    """GA4 property ID"""
    screen_page_views: list[int]
    """Total number of screen or page views"""
    screen_page_views_per_session: list[float]
    """Average page views per session"""
    session_medium: list[str]
    """The medium of the traffic source (e.g., organic, cpc, referral)"""
    session_source: list[str]
    """The source of the traffic (e.g., google, direct)"""
    sessions: list[int]
    """Total number of sessions"""
    sessions_per_user: list[float]
    """Average number of sessions per user"""
    start_date: list[str]
    """Start date of the reporting period"""
    total_users: list[int]
    """Total number of unique users"""


class TrafficSourcesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    average_session_duration: Any
    """Average duration of sessions in seconds"""
    bounce_rate: Any
    """Percentage of sessions that were single-page with no interaction"""
    date: Any
    """Date of the report row in YYYYMMDD format"""
    end_date: Any
    """End date of the reporting period"""
    new_users: Any
    """Number of first-time users"""
    property_id: Any
    """GA4 property ID"""
    screen_page_views: Any
    """Total number of screen or page views"""
    screen_page_views_per_session: Any
    """Average page views per session"""
    session_medium: Any
    """The medium of the traffic source (e.g., organic, cpc, referral)"""
    session_source: Any
    """The source of the traffic (e.g., google, direct)"""
    sessions: Any
    """Total number of sessions"""
    sessions_per_user: Any
    """Average number of sessions per user"""
    start_date: Any
    """Start date of the reporting period"""
    total_users: Any
    """Total number of unique users"""


class TrafficSourcesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    average_session_duration: str
    """Average duration of sessions in seconds"""
    bounce_rate: str
    """Percentage of sessions that were single-page with no interaction"""
    date: str
    """Date of the report row in YYYYMMDD format"""
    end_date: str
    """End date of the reporting period"""
    new_users: str
    """Number of first-time users"""
    property_id: str
    """GA4 property ID"""
    screen_page_views: str
    """Total number of screen or page views"""
    screen_page_views_per_session: str
    """Average page views per session"""
    session_medium: str
    """The medium of the traffic source (e.g., organic, cpc, referral)"""
    session_source: str
    """The source of the traffic (e.g., google, direct)"""
    sessions: str
    """Total number of sessions"""
    sessions_per_user: str
    """Average number of sessions per user"""
    start_date: str
    """Start date of the reporting period"""
    total_users: str
    """Total number of unique users"""


class TrafficSourcesSortFilter(TypedDict, total=False):
    """Available fields for sorting traffic_sources search results."""
    average_session_duration: AirbyteSortOrder
    """Average duration of sessions in seconds"""
    bounce_rate: AirbyteSortOrder
    """Percentage of sessions that were single-page with no interaction"""
    date: AirbyteSortOrder
    """Date of the report row in YYYYMMDD format"""
    end_date: AirbyteSortOrder
    """End date of the reporting period"""
    new_users: AirbyteSortOrder
    """Number of first-time users"""
    property_id: AirbyteSortOrder
    """GA4 property ID"""
    screen_page_views: AirbyteSortOrder
    """Total number of screen or page views"""
    screen_page_views_per_session: AirbyteSortOrder
    """Average page views per session"""
    session_medium: AirbyteSortOrder
    """The medium of the traffic source (e.g., organic, cpc, referral)"""
    session_source: AirbyteSortOrder
    """The source of the traffic (e.g., google, direct)"""
    sessions: AirbyteSortOrder
    """Total number of sessions"""
    sessions_per_user: AirbyteSortOrder
    """Average number of sessions per user"""
    start_date: AirbyteSortOrder
    """Start date of the reporting period"""
    total_users: AirbyteSortOrder
    """Total number of unique users"""


# Entity-specific condition types for traffic_sources
class TrafficSourcesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TrafficSourcesSearchFilter


class TrafficSourcesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TrafficSourcesSearchFilter


class TrafficSourcesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TrafficSourcesSearchFilter


class TrafficSourcesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TrafficSourcesSearchFilter


class TrafficSourcesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TrafficSourcesSearchFilter


class TrafficSourcesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TrafficSourcesSearchFilter


class TrafficSourcesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TrafficSourcesStringFilter


class TrafficSourcesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TrafficSourcesStringFilter


class TrafficSourcesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TrafficSourcesStringFilter


class TrafficSourcesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TrafficSourcesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TrafficSourcesInCondition = TypedDict("TrafficSourcesInCondition", {"in": TrafficSourcesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TrafficSourcesNotCondition = TypedDict("TrafficSourcesNotCondition", {"not": "TrafficSourcesCondition"}, total=False)
"""Negates the nested condition."""

TrafficSourcesAndCondition = TypedDict("TrafficSourcesAndCondition", {"and": "list[TrafficSourcesCondition]"}, total=False)
"""True if all nested conditions are true."""

TrafficSourcesOrCondition = TypedDict("TrafficSourcesOrCondition", {"or": "list[TrafficSourcesCondition]"}, total=False)
"""True if any nested condition is true."""

TrafficSourcesAnyCondition = TypedDict("TrafficSourcesAnyCondition", {"any": TrafficSourcesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all traffic_sources condition types
TrafficSourcesCondition = (
    TrafficSourcesEqCondition
    | TrafficSourcesNeqCondition
    | TrafficSourcesGtCondition
    | TrafficSourcesGteCondition
    | TrafficSourcesLtCondition
    | TrafficSourcesLteCondition
    | TrafficSourcesInCondition
    | TrafficSourcesLikeCondition
    | TrafficSourcesFuzzyCondition
    | TrafficSourcesKeywordCondition
    | TrafficSourcesContainsCondition
    | TrafficSourcesNotCondition
    | TrafficSourcesAndCondition
    | TrafficSourcesOrCondition
    | TrafficSourcesAnyCondition
)


class TrafficSourcesSearchQuery(TypedDict, total=False):
    """Search query for traffic_sources entity."""
    filter: TrafficSourcesCondition
    sort: list[TrafficSourcesSortFilter]


# ===== PAGES SEARCH TYPES =====

class PagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering pages search queries."""
    bounce_rate: float | None
    """Percentage of sessions that were single-page with no interaction"""
    date: str | None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None
    """End date of the reporting period"""
    host_name: str | None
    """The hostname of the page"""
    page_path_plus_query_string: str | None
    """The page path and query string"""
    property_id: str
    """GA4 property ID"""
    screen_page_views: int | None
    """Total number of screen or page views"""
    start_date: str | None
    """Start date of the reporting period"""


class PagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    bounce_rate: list[float]
    """Percentage of sessions that were single-page with no interaction"""
    date: list[str]
    """Date of the report row in YYYYMMDD format"""
    end_date: list[str]
    """End date of the reporting period"""
    host_name: list[str]
    """The hostname of the page"""
    page_path_plus_query_string: list[str]
    """The page path and query string"""
    property_id: list[str]
    """GA4 property ID"""
    screen_page_views: list[int]
    """Total number of screen or page views"""
    start_date: list[str]
    """Start date of the reporting period"""


class PagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    bounce_rate: Any
    """Percentage of sessions that were single-page with no interaction"""
    date: Any
    """Date of the report row in YYYYMMDD format"""
    end_date: Any
    """End date of the reporting period"""
    host_name: Any
    """The hostname of the page"""
    page_path_plus_query_string: Any
    """The page path and query string"""
    property_id: Any
    """GA4 property ID"""
    screen_page_views: Any
    """Total number of screen or page views"""
    start_date: Any
    """Start date of the reporting period"""


class PagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    bounce_rate: str
    """Percentage of sessions that were single-page with no interaction"""
    date: str
    """Date of the report row in YYYYMMDD format"""
    end_date: str
    """End date of the reporting period"""
    host_name: str
    """The hostname of the page"""
    page_path_plus_query_string: str
    """The page path and query string"""
    property_id: str
    """GA4 property ID"""
    screen_page_views: str
    """Total number of screen or page views"""
    start_date: str
    """Start date of the reporting period"""


class PagesSortFilter(TypedDict, total=False):
    """Available fields for sorting pages search results."""
    bounce_rate: AirbyteSortOrder
    """Percentage of sessions that were single-page with no interaction"""
    date: AirbyteSortOrder
    """Date of the report row in YYYYMMDD format"""
    end_date: AirbyteSortOrder
    """End date of the reporting period"""
    host_name: AirbyteSortOrder
    """The hostname of the page"""
    page_path_plus_query_string: AirbyteSortOrder
    """The page path and query string"""
    property_id: AirbyteSortOrder
    """GA4 property ID"""
    screen_page_views: AirbyteSortOrder
    """Total number of screen or page views"""
    start_date: AirbyteSortOrder
    """Start date of the reporting period"""


# Entity-specific condition types for pages
class PagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PagesSearchFilter


class PagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PagesSearchFilter


class PagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PagesSearchFilter


class PagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PagesSearchFilter


class PagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PagesSearchFilter


class PagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PagesSearchFilter


class PagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PagesStringFilter


class PagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PagesStringFilter


class PagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PagesStringFilter


class PagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PagesInCondition = TypedDict("PagesInCondition", {"in": PagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PagesNotCondition = TypedDict("PagesNotCondition", {"not": "PagesCondition"}, total=False)
"""Negates the nested condition."""

PagesAndCondition = TypedDict("PagesAndCondition", {"and": "list[PagesCondition]"}, total=False)
"""True if all nested conditions are true."""

PagesOrCondition = TypedDict("PagesOrCondition", {"or": "list[PagesCondition]"}, total=False)
"""True if any nested condition is true."""

PagesAnyCondition = TypedDict("PagesAnyCondition", {"any": PagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all pages condition types
PagesCondition = (
    PagesEqCondition
    | PagesNeqCondition
    | PagesGtCondition
    | PagesGteCondition
    | PagesLtCondition
    | PagesLteCondition
    | PagesInCondition
    | PagesLikeCondition
    | PagesFuzzyCondition
    | PagesKeywordCondition
    | PagesContainsCondition
    | PagesNotCondition
    | PagesAndCondition
    | PagesOrCondition
    | PagesAnyCondition
)


class PagesSearchQuery(TypedDict, total=False):
    """Search query for pages entity."""
    filter: PagesCondition
    sort: list[PagesSortFilter]


# ===== DEVICES SEARCH TYPES =====

class DevicesSearchFilter(TypedDict, total=False):
    """Available fields for filtering devices search queries."""
    average_session_duration: float | None
    """Average duration of sessions in seconds"""
    bounce_rate: float | None
    """Percentage of sessions that were single-page with no interaction"""
    browser: str | None
    """The web browser used (e.g., Chrome, Safari, Firefox)"""
    date: str | None
    """Date of the report row in YYYYMMDD format"""
    device_category: str | None
    """The device category (desktop, mobile, tablet)"""
    end_date: str | None
    """End date of the reporting period"""
    new_users: int | None
    """Number of first-time users"""
    operating_system: str | None
    """The operating system used (e.g., Windows, iOS, Android)"""
    property_id: str
    """GA4 property ID"""
    screen_page_views: int | None
    """Total number of screen or page views"""
    screen_page_views_per_session: float | None
    """Average page views per session"""
    sessions: int | None
    """Total number of sessions"""
    sessions_per_user: float | None
    """Average number of sessions per user"""
    start_date: str | None
    """Start date of the reporting period"""
    total_users: int | None
    """Total number of unique users"""


class DevicesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    average_session_duration: list[float]
    """Average duration of sessions in seconds"""
    bounce_rate: list[float]
    """Percentage of sessions that were single-page with no interaction"""
    browser: list[str]
    """The web browser used (e.g., Chrome, Safari, Firefox)"""
    date: list[str]
    """Date of the report row in YYYYMMDD format"""
    device_category: list[str]
    """The device category (desktop, mobile, tablet)"""
    end_date: list[str]
    """End date of the reporting period"""
    new_users: list[int]
    """Number of first-time users"""
    operating_system: list[str]
    """The operating system used (e.g., Windows, iOS, Android)"""
    property_id: list[str]
    """GA4 property ID"""
    screen_page_views: list[int]
    """Total number of screen or page views"""
    screen_page_views_per_session: list[float]
    """Average page views per session"""
    sessions: list[int]
    """Total number of sessions"""
    sessions_per_user: list[float]
    """Average number of sessions per user"""
    start_date: list[str]
    """Start date of the reporting period"""
    total_users: list[int]
    """Total number of unique users"""


class DevicesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    average_session_duration: Any
    """Average duration of sessions in seconds"""
    bounce_rate: Any
    """Percentage of sessions that were single-page with no interaction"""
    browser: Any
    """The web browser used (e.g., Chrome, Safari, Firefox)"""
    date: Any
    """Date of the report row in YYYYMMDD format"""
    device_category: Any
    """The device category (desktop, mobile, tablet)"""
    end_date: Any
    """End date of the reporting period"""
    new_users: Any
    """Number of first-time users"""
    operating_system: Any
    """The operating system used (e.g., Windows, iOS, Android)"""
    property_id: Any
    """GA4 property ID"""
    screen_page_views: Any
    """Total number of screen or page views"""
    screen_page_views_per_session: Any
    """Average page views per session"""
    sessions: Any
    """Total number of sessions"""
    sessions_per_user: Any
    """Average number of sessions per user"""
    start_date: Any
    """Start date of the reporting period"""
    total_users: Any
    """Total number of unique users"""


class DevicesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    average_session_duration: str
    """Average duration of sessions in seconds"""
    bounce_rate: str
    """Percentage of sessions that were single-page with no interaction"""
    browser: str
    """The web browser used (e.g., Chrome, Safari, Firefox)"""
    date: str
    """Date of the report row in YYYYMMDD format"""
    device_category: str
    """The device category (desktop, mobile, tablet)"""
    end_date: str
    """End date of the reporting period"""
    new_users: str
    """Number of first-time users"""
    operating_system: str
    """The operating system used (e.g., Windows, iOS, Android)"""
    property_id: str
    """GA4 property ID"""
    screen_page_views: str
    """Total number of screen or page views"""
    screen_page_views_per_session: str
    """Average page views per session"""
    sessions: str
    """Total number of sessions"""
    sessions_per_user: str
    """Average number of sessions per user"""
    start_date: str
    """Start date of the reporting period"""
    total_users: str
    """Total number of unique users"""


class DevicesSortFilter(TypedDict, total=False):
    """Available fields for sorting devices search results."""
    average_session_duration: AirbyteSortOrder
    """Average duration of sessions in seconds"""
    bounce_rate: AirbyteSortOrder
    """Percentage of sessions that were single-page with no interaction"""
    browser: AirbyteSortOrder
    """The web browser used (e.g., Chrome, Safari, Firefox)"""
    date: AirbyteSortOrder
    """Date of the report row in YYYYMMDD format"""
    device_category: AirbyteSortOrder
    """The device category (desktop, mobile, tablet)"""
    end_date: AirbyteSortOrder
    """End date of the reporting period"""
    new_users: AirbyteSortOrder
    """Number of first-time users"""
    operating_system: AirbyteSortOrder
    """The operating system used (e.g., Windows, iOS, Android)"""
    property_id: AirbyteSortOrder
    """GA4 property ID"""
    screen_page_views: AirbyteSortOrder
    """Total number of screen or page views"""
    screen_page_views_per_session: AirbyteSortOrder
    """Average page views per session"""
    sessions: AirbyteSortOrder
    """Total number of sessions"""
    sessions_per_user: AirbyteSortOrder
    """Average number of sessions per user"""
    start_date: AirbyteSortOrder
    """Start date of the reporting period"""
    total_users: AirbyteSortOrder
    """Total number of unique users"""


# Entity-specific condition types for devices
class DevicesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DevicesSearchFilter


class DevicesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DevicesSearchFilter


class DevicesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DevicesSearchFilter


class DevicesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DevicesSearchFilter


class DevicesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DevicesSearchFilter


class DevicesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DevicesSearchFilter


class DevicesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DevicesStringFilter


class DevicesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DevicesStringFilter


class DevicesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DevicesStringFilter


class DevicesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DevicesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DevicesInCondition = TypedDict("DevicesInCondition", {"in": DevicesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DevicesNotCondition = TypedDict("DevicesNotCondition", {"not": "DevicesCondition"}, total=False)
"""Negates the nested condition."""

DevicesAndCondition = TypedDict("DevicesAndCondition", {"and": "list[DevicesCondition]"}, total=False)
"""True if all nested conditions are true."""

DevicesOrCondition = TypedDict("DevicesOrCondition", {"or": "list[DevicesCondition]"}, total=False)
"""True if any nested condition is true."""

DevicesAnyCondition = TypedDict("DevicesAnyCondition", {"any": DevicesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all devices condition types
DevicesCondition = (
    DevicesEqCondition
    | DevicesNeqCondition
    | DevicesGtCondition
    | DevicesGteCondition
    | DevicesLtCondition
    | DevicesLteCondition
    | DevicesInCondition
    | DevicesLikeCondition
    | DevicesFuzzyCondition
    | DevicesKeywordCondition
    | DevicesContainsCondition
    | DevicesNotCondition
    | DevicesAndCondition
    | DevicesOrCondition
    | DevicesAnyCondition
)


class DevicesSearchQuery(TypedDict, total=False):
    """Search query for devices entity."""
    filter: DevicesCondition
    sort: list[DevicesSortFilter]


# ===== LOCATIONS SEARCH TYPES =====

class LocationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering locations search queries."""
    average_session_duration: float | None
    """Average duration of sessions in seconds"""
    bounce_rate: float | None
    """Percentage of sessions that were single-page with no interaction"""
    city: str | None
    """The city of the user"""
    country: str | None
    """The country of the user"""
    date: str | None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None
    """End date of the reporting period"""
    new_users: int | None
    """Number of first-time users"""
    property_id: str
    """GA4 property ID"""
    region: str | None
    """The region (state/province) of the user"""
    screen_page_views: int | None
    """Total number of screen or page views"""
    screen_page_views_per_session: float | None
    """Average page views per session"""
    sessions: int | None
    """Total number of sessions"""
    sessions_per_user: float | None
    """Average number of sessions per user"""
    start_date: str | None
    """Start date of the reporting period"""
    total_users: int | None
    """Total number of unique users"""


class LocationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    average_session_duration: list[float]
    """Average duration of sessions in seconds"""
    bounce_rate: list[float]
    """Percentage of sessions that were single-page with no interaction"""
    city: list[str]
    """The city of the user"""
    country: list[str]
    """The country of the user"""
    date: list[str]
    """Date of the report row in YYYYMMDD format"""
    end_date: list[str]
    """End date of the reporting period"""
    new_users: list[int]
    """Number of first-time users"""
    property_id: list[str]
    """GA4 property ID"""
    region: list[str]
    """The region (state/province) of the user"""
    screen_page_views: list[int]
    """Total number of screen or page views"""
    screen_page_views_per_session: list[float]
    """Average page views per session"""
    sessions: list[int]
    """Total number of sessions"""
    sessions_per_user: list[float]
    """Average number of sessions per user"""
    start_date: list[str]
    """Start date of the reporting period"""
    total_users: list[int]
    """Total number of unique users"""


class LocationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    average_session_duration: Any
    """Average duration of sessions in seconds"""
    bounce_rate: Any
    """Percentage of sessions that were single-page with no interaction"""
    city: Any
    """The city of the user"""
    country: Any
    """The country of the user"""
    date: Any
    """Date of the report row in YYYYMMDD format"""
    end_date: Any
    """End date of the reporting period"""
    new_users: Any
    """Number of first-time users"""
    property_id: Any
    """GA4 property ID"""
    region: Any
    """The region (state/province) of the user"""
    screen_page_views: Any
    """Total number of screen or page views"""
    screen_page_views_per_session: Any
    """Average page views per session"""
    sessions: Any
    """Total number of sessions"""
    sessions_per_user: Any
    """Average number of sessions per user"""
    start_date: Any
    """Start date of the reporting period"""
    total_users: Any
    """Total number of unique users"""


class LocationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    average_session_duration: str
    """Average duration of sessions in seconds"""
    bounce_rate: str
    """Percentage of sessions that were single-page with no interaction"""
    city: str
    """The city of the user"""
    country: str
    """The country of the user"""
    date: str
    """Date of the report row in YYYYMMDD format"""
    end_date: str
    """End date of the reporting period"""
    new_users: str
    """Number of first-time users"""
    property_id: str
    """GA4 property ID"""
    region: str
    """The region (state/province) of the user"""
    screen_page_views: str
    """Total number of screen or page views"""
    screen_page_views_per_session: str
    """Average page views per session"""
    sessions: str
    """Total number of sessions"""
    sessions_per_user: str
    """Average number of sessions per user"""
    start_date: str
    """Start date of the reporting period"""
    total_users: str
    """Total number of unique users"""


class LocationsSortFilter(TypedDict, total=False):
    """Available fields for sorting locations search results."""
    average_session_duration: AirbyteSortOrder
    """Average duration of sessions in seconds"""
    bounce_rate: AirbyteSortOrder
    """Percentage of sessions that were single-page with no interaction"""
    city: AirbyteSortOrder
    """The city of the user"""
    country: AirbyteSortOrder
    """The country of the user"""
    date: AirbyteSortOrder
    """Date of the report row in YYYYMMDD format"""
    end_date: AirbyteSortOrder
    """End date of the reporting period"""
    new_users: AirbyteSortOrder
    """Number of first-time users"""
    property_id: AirbyteSortOrder
    """GA4 property ID"""
    region: AirbyteSortOrder
    """The region (state/province) of the user"""
    screen_page_views: AirbyteSortOrder
    """Total number of screen or page views"""
    screen_page_views_per_session: AirbyteSortOrder
    """Average page views per session"""
    sessions: AirbyteSortOrder
    """Total number of sessions"""
    sessions_per_user: AirbyteSortOrder
    """Average number of sessions per user"""
    start_date: AirbyteSortOrder
    """Start date of the reporting period"""
    total_users: AirbyteSortOrder
    """Total number of unique users"""


# Entity-specific condition types for locations
class LocationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: LocationsSearchFilter


class LocationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: LocationsSearchFilter


class LocationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: LocationsSearchFilter


class LocationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: LocationsSearchFilter


class LocationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: LocationsSearchFilter


class LocationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: LocationsSearchFilter


class LocationsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: LocationsStringFilter


class LocationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: LocationsStringFilter


class LocationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: LocationsStringFilter


class LocationsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: LocationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
LocationsInCondition = TypedDict("LocationsInCondition", {"in": LocationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

LocationsNotCondition = TypedDict("LocationsNotCondition", {"not": "LocationsCondition"}, total=False)
"""Negates the nested condition."""

LocationsAndCondition = TypedDict("LocationsAndCondition", {"and": "list[LocationsCondition]"}, total=False)
"""True if all nested conditions are true."""

LocationsOrCondition = TypedDict("LocationsOrCondition", {"or": "list[LocationsCondition]"}, total=False)
"""True if any nested condition is true."""

LocationsAnyCondition = TypedDict("LocationsAnyCondition", {"any": LocationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all locations condition types
LocationsCondition = (
    LocationsEqCondition
    | LocationsNeqCondition
    | LocationsGtCondition
    | LocationsGteCondition
    | LocationsLtCondition
    | LocationsLteCondition
    | LocationsInCondition
    | LocationsLikeCondition
    | LocationsFuzzyCondition
    | LocationsKeywordCondition
    | LocationsContainsCondition
    | LocationsNotCondition
    | LocationsAndCondition
    | LocationsOrCondition
    | LocationsAnyCondition
)


class LocationsSearchQuery(TypedDict, total=False):
    """Search query for locations entity."""
    filter: LocationsCondition
    sort: list[LocationsSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
