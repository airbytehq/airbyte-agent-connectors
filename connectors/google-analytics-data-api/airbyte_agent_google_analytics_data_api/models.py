"""
Pydantic models for google-analytics-data-api connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class GoogleAnalyticsDataApiAuthConfig(BaseModel):
    """OAuth 2.0 Authentication"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """OAuth 2.0 Client ID from Google Cloud Console"""
    client_secret: str
    """OAuth 2.0 Client Secret from Google Cloud Console"""
    refresh_token: str
    """OAuth 2.0 Refresh Token for obtaining new access tokens"""

# Replication configuration

class GoogleAnalyticsDataApiReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Google Analytics."""

    model_config = ConfigDict(extra="forbid")

    property_ids: str
    """A list of GA4 Property IDs to replicate data from."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class DimensionValue(BaseModel):
    """DimensionValue type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: Union[str, Any] = Field(default=None)

class MetricValue(BaseModel):
    """MetricValue type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: Union[str, Any] = Field(default=None)

class Row(BaseModel):
    """Row type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    dimension_values: Union[list[DimensionValue], Any] = Field(default=None, alias="dimensionValues")
    metric_values: Union[list[MetricValue], Any] = Field(default=None, alias="metricValues")

class DimensionHeader(BaseModel):
    """DimensionHeader type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class MetricHeader(BaseModel):
    """MetricHeader type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)

class RunReportResponsePropertyquotaTokensperprojectperhour(BaseModel):
    """Nested schema for RunReportResponsePropertyquota.tokensPerProjectPerHour"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    consumed: Union[int, Any] = Field(default=None)
    remaining: Union[int, Any] = Field(default=None)

class RunReportResponsePropertyquotaTokensperhour(BaseModel):
    """Nested schema for RunReportResponsePropertyquota.tokensPerHour"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    consumed: Union[int, Any] = Field(default=None)
    remaining: Union[int, Any] = Field(default=None)

class RunReportResponsePropertyquotaServererrorsperprojectperhour(BaseModel):
    """Nested schema for RunReportResponsePropertyquota.serverErrorsPerProjectPerHour"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    consumed: Union[int, Any] = Field(default=None)
    remaining: Union[int, Any] = Field(default=None)

class RunReportResponsePropertyquotaTokensperday(BaseModel):
    """Nested schema for RunReportResponsePropertyquota.tokensPerDay"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    consumed: Union[int, Any] = Field(default=None)
    remaining: Union[int, Any] = Field(default=None)

class RunReportResponsePropertyquotaConcurrentrequests(BaseModel):
    """Nested schema for RunReportResponsePropertyquota.concurrentRequests"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    consumed: Union[int, Any] = Field(default=None)
    remaining: Union[int, Any] = Field(default=None)

class RunReportResponsePropertyquotaPotentiallythresholdedrequestsperhour(BaseModel):
    """Nested schema for RunReportResponsePropertyquota.potentiallyThresholdedRequestsPerHour"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    consumed: Union[int, Any] = Field(default=None)
    remaining: Union[int, Any] = Field(default=None)

class RunReportResponsePropertyquota(BaseModel):
    """Quota status for this Analytics property"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tokens_per_day: Union[RunReportResponsePropertyquotaTokensperday, Any] = Field(default=None, alias="tokensPerDay")
    tokens_per_hour: Union[RunReportResponsePropertyquotaTokensperhour, Any] = Field(default=None, alias="tokensPerHour")
    concurrent_requests: Union[RunReportResponsePropertyquotaConcurrentrequests, Any] = Field(default=None, alias="concurrentRequests")
    server_errors_per_project_per_hour: Union[RunReportResponsePropertyquotaServererrorsperprojectperhour, Any] = Field(default=None, alias="serverErrorsPerProjectPerHour")
    potentially_thresholded_requests_per_hour: Union[RunReportResponsePropertyquotaPotentiallythresholdedrequestsperhour, Any] = Field(default=None, alias="potentiallyThresholdedRequestsPerHour")
    tokens_per_project_per_hour: Union[RunReportResponsePropertyquotaTokensperprojectperhour, Any] = Field(default=None, alias="tokensPerProjectPerHour")

class RunReportResponseMetadata(BaseModel):
    """Nested schema for RunReportResponse.metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    currency_code: Union[str, Any] = Field(default=None, alias="currencyCode", description="The currency code used in this report")
    """The currency code used in this report"""
    time_zone: Union[str, Any] = Field(default=None, alias="timeZone", description="The property's current timezone")
    """The property's current timezone"""

class RunReportResponse(BaseModel):
    """Response from the runReport endpoint"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    dimension_headers: Union[list[DimensionHeader], Any] = Field(default=None, alias="dimensionHeaders")
    metric_headers: Union[list[MetricHeader], Any] = Field(default=None, alias="metricHeaders")
    rows: Union[list[Row], Any] = Field(default=None)
    row_count: Union[int, Any] = Field(default=None, alias="rowCount")
    metadata: Union[RunReportResponseMetadata, Any] = Field(default=None)
    property_quota: Union[RunReportResponsePropertyquota, Any] = Field(default=None, alias="propertyQuota")
    kind: Union[str, Any] = Field(default=None)

class WebsiteOverviewRequestDaterangesItem(BaseModel):
    """Nested schema for WebsiteOverviewRequest.dateRanges_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate", description="Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)")
    """Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)"""
    end_date: Union[str, Any] = Field(default=None, alias="endDate", description="End date in YYYY-MM-DD format or relative (e.g., today)")
    """End date in YYYY-MM-DD format or relative (e.g., today)"""

class WebsiteOverviewRequestDimensionsItem(BaseModel):
    """Nested schema for WebsiteOverviewRequest.dimensions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class WebsiteOverviewRequestMetricsItem(BaseModel):
    """Nested schema for WebsiteOverviewRequest.metrics_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class WebsiteOverviewRequest(BaseModel):
    """Request body for website overview report"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date_ranges: Union[list[WebsiteOverviewRequestDaterangesItem], Any] = Field(default=None, alias="dateRanges")
    dimensions: Union[list[WebsiteOverviewRequestDimensionsItem], Any] = Field(default=None)
    metrics: Union[list[WebsiteOverviewRequestMetricsItem], Any] = Field(default=None)
    keep_empty_rows: Union[bool, Any] = Field(default=None, alias="keepEmptyRows")
    return_property_quota: Union[bool, Any] = Field(default=None, alias="returnPropertyQuota")
    limit: Union[int, Any] = Field(default=None)

class DailyActiveUsersRequestDaterangesItem(BaseModel):
    """Nested schema for DailyActiveUsersRequest.dateRanges_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate", description="Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)")
    """Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)"""
    end_date: Union[str, Any] = Field(default=None, alias="endDate", description="End date in YYYY-MM-DD format or relative (e.g., today)")
    """End date in YYYY-MM-DD format or relative (e.g., today)"""

class DailyActiveUsersRequestDimensionsItem(BaseModel):
    """Nested schema for DailyActiveUsersRequest.dimensions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class DailyActiveUsersRequestMetricsItem(BaseModel):
    """Nested schema for DailyActiveUsersRequest.metrics_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class DailyActiveUsersRequest(BaseModel):
    """Request body for daily active users report"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date_ranges: Union[list[DailyActiveUsersRequestDaterangesItem], Any] = Field(default=None, alias="dateRanges")
    dimensions: Union[list[DailyActiveUsersRequestDimensionsItem], Any] = Field(default=None)
    metrics: Union[list[DailyActiveUsersRequestMetricsItem], Any] = Field(default=None)
    keep_empty_rows: Union[bool, Any] = Field(default=None, alias="keepEmptyRows")
    return_property_quota: Union[bool, Any] = Field(default=None, alias="returnPropertyQuota")
    limit: Union[int, Any] = Field(default=None)

class WeeklyActiveUsersRequestMetricsItem(BaseModel):
    """Nested schema for WeeklyActiveUsersRequest.metrics_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class WeeklyActiveUsersRequestDaterangesItem(BaseModel):
    """Nested schema for WeeklyActiveUsersRequest.dateRanges_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate", description="Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)")
    """Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)"""
    end_date: Union[str, Any] = Field(default=None, alias="endDate", description="End date in YYYY-MM-DD format or relative (e.g., today)")
    """End date in YYYY-MM-DD format or relative (e.g., today)"""

class WeeklyActiveUsersRequestDimensionsItem(BaseModel):
    """Nested schema for WeeklyActiveUsersRequest.dimensions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class WeeklyActiveUsersRequest(BaseModel):
    """Request body for weekly active users report"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date_ranges: Union[list[WeeklyActiveUsersRequestDaterangesItem], Any] = Field(default=None, alias="dateRanges")
    dimensions: Union[list[WeeklyActiveUsersRequestDimensionsItem], Any] = Field(default=None)
    metrics: Union[list[WeeklyActiveUsersRequestMetricsItem], Any] = Field(default=None)
    keep_empty_rows: Union[bool, Any] = Field(default=None, alias="keepEmptyRows")
    return_property_quota: Union[bool, Any] = Field(default=None, alias="returnPropertyQuota")
    limit: Union[int, Any] = Field(default=None)

class FourWeeklyActiveUsersRequestDimensionsItem(BaseModel):
    """Nested schema for FourWeeklyActiveUsersRequest.dimensions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class FourWeeklyActiveUsersRequestDaterangesItem(BaseModel):
    """Nested schema for FourWeeklyActiveUsersRequest.dateRanges_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate", description="Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)")
    """Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)"""
    end_date: Union[str, Any] = Field(default=None, alias="endDate", description="End date in YYYY-MM-DD format or relative (e.g., today)")
    """End date in YYYY-MM-DD format or relative (e.g., today)"""

class FourWeeklyActiveUsersRequestMetricsItem(BaseModel):
    """Nested schema for FourWeeklyActiveUsersRequest.metrics_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class FourWeeklyActiveUsersRequest(BaseModel):
    """Request body for four-weekly active users report"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date_ranges: Union[list[FourWeeklyActiveUsersRequestDaterangesItem], Any] = Field(default=None, alias="dateRanges")
    dimensions: Union[list[FourWeeklyActiveUsersRequestDimensionsItem], Any] = Field(default=None)
    metrics: Union[list[FourWeeklyActiveUsersRequestMetricsItem], Any] = Field(default=None)
    keep_empty_rows: Union[bool, Any] = Field(default=None, alias="keepEmptyRows")
    return_property_quota: Union[bool, Any] = Field(default=None, alias="returnPropertyQuota")
    limit: Union[int, Any] = Field(default=None)

class TrafficSourcesRequestMetricsItem(BaseModel):
    """Nested schema for TrafficSourcesRequest.metrics_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class TrafficSourcesRequestDimensionsItem(BaseModel):
    """Nested schema for TrafficSourcesRequest.dimensions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class TrafficSourcesRequestDaterangesItem(BaseModel):
    """Nested schema for TrafficSourcesRequest.dateRanges_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate", description="Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)")
    """Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)"""
    end_date: Union[str, Any] = Field(default=None, alias="endDate", description="End date in YYYY-MM-DD format or relative (e.g., today)")
    """End date in YYYY-MM-DD format or relative (e.g., today)"""

class TrafficSourcesRequest(BaseModel):
    """Request body for traffic sources report"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date_ranges: Union[list[TrafficSourcesRequestDaterangesItem], Any] = Field(default=None, alias="dateRanges")
    dimensions: Union[list[TrafficSourcesRequestDimensionsItem], Any] = Field(default=None)
    metrics: Union[list[TrafficSourcesRequestMetricsItem], Any] = Field(default=None)
    keep_empty_rows: Union[bool, Any] = Field(default=None, alias="keepEmptyRows")
    return_property_quota: Union[bool, Any] = Field(default=None, alias="returnPropertyQuota")
    limit: Union[int, Any] = Field(default=None)

class PagesRequestDaterangesItem(BaseModel):
    """Nested schema for PagesRequest.dateRanges_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate", description="Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)")
    """Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)"""
    end_date: Union[str, Any] = Field(default=None, alias="endDate", description="End date in YYYY-MM-DD format or relative (e.g., today)")
    """End date in YYYY-MM-DD format or relative (e.g., today)"""

class PagesRequestDimensionsItem(BaseModel):
    """Nested schema for PagesRequest.dimensions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class PagesRequestMetricsItem(BaseModel):
    """Nested schema for PagesRequest.metrics_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class PagesRequest(BaseModel):
    """Request body for pages report"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date_ranges: Union[list[PagesRequestDaterangesItem], Any] = Field(default=None, alias="dateRanges")
    dimensions: Union[list[PagesRequestDimensionsItem], Any] = Field(default=None)
    metrics: Union[list[PagesRequestMetricsItem], Any] = Field(default=None)
    keep_empty_rows: Union[bool, Any] = Field(default=None, alias="keepEmptyRows")
    return_property_quota: Union[bool, Any] = Field(default=None, alias="returnPropertyQuota")
    limit: Union[int, Any] = Field(default=None)

class DevicesRequestDaterangesItem(BaseModel):
    """Nested schema for DevicesRequest.dateRanges_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate", description="Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)")
    """Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)"""
    end_date: Union[str, Any] = Field(default=None, alias="endDate", description="End date in YYYY-MM-DD format or relative (e.g., today)")
    """End date in YYYY-MM-DD format or relative (e.g., today)"""

class DevicesRequestMetricsItem(BaseModel):
    """Nested schema for DevicesRequest.metrics_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class DevicesRequestDimensionsItem(BaseModel):
    """Nested schema for DevicesRequest.dimensions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class DevicesRequest(BaseModel):
    """Request body for devices report"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date_ranges: Union[list[DevicesRequestDaterangesItem], Any] = Field(default=None, alias="dateRanges")
    dimensions: Union[list[DevicesRequestDimensionsItem], Any] = Field(default=None)
    metrics: Union[list[DevicesRequestMetricsItem], Any] = Field(default=None)
    keep_empty_rows: Union[bool, Any] = Field(default=None, alias="keepEmptyRows")
    return_property_quota: Union[bool, Any] = Field(default=None, alias="returnPropertyQuota")
    limit: Union[int, Any] = Field(default=None)

class LocationsRequestMetricsItem(BaseModel):
    """Nested schema for LocationsRequest.metrics_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class LocationsRequestDaterangesItem(BaseModel):
    """Nested schema for LocationsRequest.dateRanges_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate", description="Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)")
    """Start date in YYYY-MM-DD format or relative (e.g., 30daysAgo)"""
    end_date: Union[str, Any] = Field(default=None, alias="endDate", description="End date in YYYY-MM-DD format or relative (e.g., today)")
    """End date in YYYY-MM-DD format or relative (e.g., today)"""

class LocationsRequestDimensionsItem(BaseModel):
    """Nested schema for LocationsRequest.dimensions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)

class LocationsRequest(BaseModel):
    """Request body for locations report"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date_ranges: Union[list[LocationsRequestDaterangesItem], Any] = Field(default=None, alias="dateRanges")
    dimensions: Union[list[LocationsRequestDimensionsItem], Any] = Field(default=None)
    metrics: Union[list[LocationsRequestMetricsItem], Any] = Field(default=None)
    keep_empty_rows: Union[bool, Any] = Field(default=None, alias="keepEmptyRows")
    return_property_quota: Union[bool, Any] = Field(default=None, alias="returnPropertyQuota")
    limit: Union[int, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== CHECK RESULT MODEL =====

class GoogleAnalyticsDataApiCheckResult(BaseModel):
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


class GoogleAnalyticsDataApiExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class GoogleAnalyticsDataApiExecuteResultWithMeta(GoogleAnalyticsDataApiExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class WebsiteOverviewSearchData(BaseModel):
    """Search result data for website_overview entity."""
    model_config = ConfigDict(extra="allow")

    average_session_duration: float | None = None
    """Average duration of sessions in seconds"""
    bounce_rate: float | None = None
    """Percentage of sessions that were single-page with no interaction"""
    date: str | None = None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None = None
    """End date of the reporting period"""
    new_users: int | None = None
    """Number of first-time users"""
    property_id: str = None
    """GA4 property ID"""
    screen_page_views: int | None = None
    """Total number of screen or page views"""
    screen_page_views_per_session: float | None = None
    """Average page views per session"""
    sessions: int | None = None
    """Total number of sessions"""
    sessions_per_user: float | None = None
    """Average number of sessions per user"""
    start_date: str | None = None
    """Start date of the reporting period"""
    total_users: int | None = None
    """Total number of unique users"""


class DailyActiveUsersSearchData(BaseModel):
    """Search result data for daily_active_users entity."""
    model_config = ConfigDict(extra="allow")

    active1_day_users: int | None = None
    """Number of distinct users active in the last 1 day"""
    date: str | None = None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None = None
    """End date of the reporting period"""
    property_id: str = None
    """GA4 property ID"""
    start_date: str | None = None
    """Start date of the reporting period"""


class WeeklyActiveUsersSearchData(BaseModel):
    """Search result data for weekly_active_users entity."""
    model_config = ConfigDict(extra="allow")

    active7_day_users: int | None = None
    """Number of distinct users active in the last 7 days"""
    date: str | None = None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None = None
    """End date of the reporting period"""
    property_id: str = None
    """GA4 property ID"""
    start_date: str | None = None
    """Start date of the reporting period"""


class FourWeeklyActiveUsersSearchData(BaseModel):
    """Search result data for four_weekly_active_users entity."""
    model_config = ConfigDict(extra="allow")

    active28_day_users: int | None = None
    """Number of distinct users active in the last 28 days"""
    date: str | None = None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None = None
    """End date of the reporting period"""
    property_id: str = None
    """GA4 property ID"""
    start_date: str | None = None
    """Start date of the reporting period"""


class TrafficSourcesSearchData(BaseModel):
    """Search result data for traffic_sources entity."""
    model_config = ConfigDict(extra="allow")

    average_session_duration: float | None = None
    """Average duration of sessions in seconds"""
    bounce_rate: float | None = None
    """Percentage of sessions that were single-page with no interaction"""
    date: str | None = None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None = None
    """End date of the reporting period"""
    new_users: int | None = None
    """Number of first-time users"""
    property_id: str = None
    """GA4 property ID"""
    screen_page_views: int | None = None
    """Total number of screen or page views"""
    screen_page_views_per_session: float | None = None
    """Average page views per session"""
    session_medium: str | None = None
    """The medium of the traffic source (e.g., organic, cpc, referral)"""
    session_source: str | None = None
    """The source of the traffic (e.g., google, direct)"""
    sessions: int | None = None
    """Total number of sessions"""
    sessions_per_user: float | None = None
    """Average number of sessions per user"""
    start_date: str | None = None
    """Start date of the reporting period"""
    total_users: int | None = None
    """Total number of unique users"""


class PagesSearchData(BaseModel):
    """Search result data for pages entity."""
    model_config = ConfigDict(extra="allow")

    bounce_rate: float | None = None
    """Percentage of sessions that were single-page with no interaction"""
    date: str | None = None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None = None
    """End date of the reporting period"""
    host_name: str | None = None
    """The hostname of the page"""
    page_path_plus_query_string: str | None = None
    """The page path and query string"""
    property_id: str = None
    """GA4 property ID"""
    screen_page_views: int | None = None
    """Total number of screen or page views"""
    start_date: str | None = None
    """Start date of the reporting period"""


class DevicesSearchData(BaseModel):
    """Search result data for devices entity."""
    model_config = ConfigDict(extra="allow")

    average_session_duration: float | None = None
    """Average duration of sessions in seconds"""
    bounce_rate: float | None = None
    """Percentage of sessions that were single-page with no interaction"""
    browser: str | None = None
    """The web browser used (e.g., Chrome, Safari, Firefox)"""
    date: str | None = None
    """Date of the report row in YYYYMMDD format"""
    device_category: str | None = None
    """The device category (desktop, mobile, tablet)"""
    end_date: str | None = None
    """End date of the reporting period"""
    new_users: int | None = None
    """Number of first-time users"""
    operating_system: str | None = None
    """The operating system used (e.g., Windows, iOS, Android)"""
    property_id: str = None
    """GA4 property ID"""
    screen_page_views: int | None = None
    """Total number of screen or page views"""
    screen_page_views_per_session: float | None = None
    """Average page views per session"""
    sessions: int | None = None
    """Total number of sessions"""
    sessions_per_user: float | None = None
    """Average number of sessions per user"""
    start_date: str | None = None
    """Start date of the reporting period"""
    total_users: int | None = None
    """Total number of unique users"""


class LocationsSearchData(BaseModel):
    """Search result data for locations entity."""
    model_config = ConfigDict(extra="allow")

    average_session_duration: float | None = None
    """Average duration of sessions in seconds"""
    bounce_rate: float | None = None
    """Percentage of sessions that were single-page with no interaction"""
    city: str | None = None
    """The city of the user"""
    country: str | None = None
    """The country of the user"""
    date: str | None = None
    """Date of the report row in YYYYMMDD format"""
    end_date: str | None = None
    """End date of the reporting period"""
    new_users: int | None = None
    """Number of first-time users"""
    property_id: str = None
    """GA4 property ID"""
    region: str | None = None
    """The region (state/province) of the user"""
    screen_page_views: int | None = None
    """Total number of screen or page views"""
    screen_page_views_per_session: float | None = None
    """Average page views per session"""
    sessions: int | None = None
    """Total number of sessions"""
    sessions_per_user: float | None = None
    """Average number of sessions per user"""
    start_date: str | None = None
    """Start date of the reporting period"""
    total_users: int | None = None
    """Total number of unique users"""


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

WebsiteOverviewSearchResult = AirbyteSearchResult[WebsiteOverviewSearchData]
"""Search result type for website_overview entity."""

DailyActiveUsersSearchResult = AirbyteSearchResult[DailyActiveUsersSearchData]
"""Search result type for daily_active_users entity."""

WeeklyActiveUsersSearchResult = AirbyteSearchResult[WeeklyActiveUsersSearchData]
"""Search result type for weekly_active_users entity."""

FourWeeklyActiveUsersSearchResult = AirbyteSearchResult[FourWeeklyActiveUsersSearchData]
"""Search result type for four_weekly_active_users entity."""

TrafficSourcesSearchResult = AirbyteSearchResult[TrafficSourcesSearchData]
"""Search result type for traffic_sources entity."""

PagesSearchResult = AirbyteSearchResult[PagesSearchData]
"""Search result type for pages entity."""

DevicesSearchResult = AirbyteSearchResult[DevicesSearchData]
"""Search result type for devices entity."""

LocationsSearchResult = AirbyteSearchResult[LocationsSearchData]
"""Search result type for locations entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

WebsiteOverviewListResult = GoogleAnalyticsDataApiExecuteResult[list[Row]]
"""Result type for website_overview.list operation."""

DailyActiveUsersListResult = GoogleAnalyticsDataApiExecuteResult[list[Row]]
"""Result type for daily_active_users.list operation."""

WeeklyActiveUsersListResult = GoogleAnalyticsDataApiExecuteResult[list[Row]]
"""Result type for weekly_active_users.list operation."""

FourWeeklyActiveUsersListResult = GoogleAnalyticsDataApiExecuteResult[list[Row]]
"""Result type for four_weekly_active_users.list operation."""

TrafficSourcesListResult = GoogleAnalyticsDataApiExecuteResult[list[Row]]
"""Result type for traffic_sources.list operation."""

PagesListResult = GoogleAnalyticsDataApiExecuteResult[list[Row]]
"""Result type for pages.list operation."""

DevicesListResult = GoogleAnalyticsDataApiExecuteResult[list[Row]]
"""Result type for devices.list operation."""

LocationsListResult = GoogleAnalyticsDataApiExecuteResult[list[Row]]
"""Result type for locations.list operation."""

