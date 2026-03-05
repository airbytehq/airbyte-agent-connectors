"""
Pydantic models for google-search-console connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any
from typing import Optional

# Authentication configuration

class GoogleSearchConsoleAuthConfig(BaseModel):
    """OAuth2 Authentication"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """The client ID of your Google Search Console developer application."""
    client_secret: str
    """The client secret of your Google Search Console developer application."""
    refresh_token: str
    """The refresh token for obtaining new access tokens."""

# Replication configuration

class GoogleSearchConsoleReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Google Search Console."""

    model_config = ConfigDict(extra="forbid")

    site_urls: str
    """The URLs of the website property attached to your GSC account. Examples: https://example.com/ or sc-domain:example.com
"""
    start_date: Optional[str] = None
    """UTC date in the format YYYY-MM-DD. Any data before this date will not be replicated.
"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Site(BaseModel):
    """A Search Console site resource."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    site_url: Union[str | None, Any] = Field(default=None, alias="siteUrl")
    permission_level: Union[str | None, Any] = Field(default=None, alias="permissionLevel")

class SitesList(BaseModel):
    """Response containing a list of sites."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    site_entry: Union[list[Site], Any] = Field(default=None, alias="siteEntry")

class SitemapContent(BaseModel):
    """Information about a specific content type in a sitemap."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: Union[str | None, Any] = Field(default=None, alias="type")
    submitted: Union[str | None, Any] = Field(default=None)
    indexed: Union[str | None, Any] = Field(default=None)

class Sitemap(BaseModel):
    """A sitemap resource with details about a submitted sitemap."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    path: Union[str | None, Any] = Field(default=None)
    last_submitted: Union[str | None, Any] = Field(default=None, alias="lastSubmitted")
    is_pending: Union[bool | None, Any] = Field(default=None, alias="isPending")
    is_sitemaps_index: Union[bool | None, Any] = Field(default=None, alias="isSitemapsIndex")
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    last_downloaded: Union[str | None, Any] = Field(default=None, alias="lastDownloaded")
    warnings: Union[str | None, Any] = Field(default=None)
    errors: Union[str | None, Any] = Field(default=None)
    contents: Union[list[SitemapContent] | None, Any] = Field(default=None)

class SitemapsList(BaseModel):
    """Response containing a list of sitemaps."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    sitemap: Union[list[Sitemap], Any] = Field(default=None)

class SearchAnalyticsByDateRequest(BaseModel):
    """Request body for search analytics query grouped by date."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate")
    end_date: Union[str, Any] = Field(default=None, alias="endDate")
    dimensions: Union[list[str], Any] = Field(default=None)
    row_limit: Union[int, Any] = Field(default=None, alias="rowLimit")
    start_row: Union[int, Any] = Field(default=None, alias="startRow")
    type_: Union[str, Any] = Field(default=None, alias="type")
    aggregation_type: Union[str, Any] = Field(default=None, alias="aggregationType")
    data_state: Union[str, Any] = Field(default=None, alias="dataState")

class SearchAnalyticsByCountryRequest(BaseModel):
    """Request body for search analytics query grouped by date and country."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate")
    end_date: Union[str, Any] = Field(default=None, alias="endDate")
    dimensions: Union[list[str], Any] = Field(default=None)
    row_limit: Union[int, Any] = Field(default=None, alias="rowLimit")
    start_row: Union[int, Any] = Field(default=None, alias="startRow")
    type_: Union[str, Any] = Field(default=None, alias="type")
    aggregation_type: Union[str, Any] = Field(default=None, alias="aggregationType")
    data_state: Union[str, Any] = Field(default=None, alias="dataState")

class SearchAnalyticsByDeviceRequest(BaseModel):
    """Request body for search analytics query grouped by date and device."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate")
    end_date: Union[str, Any] = Field(default=None, alias="endDate")
    dimensions: Union[list[str], Any] = Field(default=None)
    row_limit: Union[int, Any] = Field(default=None, alias="rowLimit")
    start_row: Union[int, Any] = Field(default=None, alias="startRow")
    type_: Union[str, Any] = Field(default=None, alias="type")
    aggregation_type: Union[str, Any] = Field(default=None, alias="aggregationType")
    data_state: Union[str, Any] = Field(default=None, alias="dataState")

class SearchAnalyticsByPageRequest(BaseModel):
    """Request body for search analytics query grouped by date and page."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate")
    end_date: Union[str, Any] = Field(default=None, alias="endDate")
    dimensions: Union[list[str], Any] = Field(default=None)
    row_limit: Union[int, Any] = Field(default=None, alias="rowLimit")
    start_row: Union[int, Any] = Field(default=None, alias="startRow")
    type_: Union[str, Any] = Field(default=None, alias="type")
    aggregation_type: Union[str, Any] = Field(default=None, alias="aggregationType")
    data_state: Union[str, Any] = Field(default=None, alias="dataState")

class SearchAnalyticsByQueryRequest(BaseModel):
    """Request body for search analytics query grouped by date and query."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate")
    end_date: Union[str, Any] = Field(default=None, alias="endDate")
    dimensions: Union[list[str], Any] = Field(default=None)
    row_limit: Union[int, Any] = Field(default=None, alias="rowLimit")
    start_row: Union[int, Any] = Field(default=None, alias="startRow")
    type_: Union[str, Any] = Field(default=None, alias="type")
    aggregation_type: Union[str, Any] = Field(default=None, alias="aggregationType")
    data_state: Union[str, Any] = Field(default=None, alias="dataState")

class SearchAnalyticsAllFieldsRequest(BaseModel):
    """Request body for search analytics query grouped by all dimensions."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start_date: Union[str, Any] = Field(default=None, alias="startDate")
    end_date: Union[str, Any] = Field(default=None, alias="endDate")
    dimensions: Union[list[str], Any] = Field(default=None)
    row_limit: Union[int, Any] = Field(default=None, alias="rowLimit")
    start_row: Union[int, Any] = Field(default=None, alias="startRow")
    type_: Union[str, Any] = Field(default=None, alias="type")
    aggregation_type: Union[str, Any] = Field(default=None, alias="aggregationType")
    data_state: Union[str, Any] = Field(default=None, alias="dataState")

class SearchAnalyticsRow(BaseModel):
    """A row of search analytics data."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    keys: Union[list[str] | None, Any] = Field(default=None)
    clicks: Union[float | None, Any] = Field(default=None)
    impressions: Union[float | None, Any] = Field(default=None)
    ctr: Union[float | None, Any] = Field(default=None)
    position: Union[float | None, Any] = Field(default=None)

class SearchAnalyticsResponse(BaseModel):
    """Response containing search analytics data."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rows: Union[list[SearchAnalyticsRow], Any] = Field(default=None)
    response_aggregation_type: Union[str | None, Any] = Field(default=None, alias="responseAggregationType")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== CHECK RESULT MODEL =====

class GoogleSearchConsoleCheckResult(BaseModel):
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


class GoogleSearchConsoleExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class GoogleSearchConsoleExecuteResultWithMeta(GoogleSearchConsoleExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class SitesSearchData(BaseModel):
    """Search result data for sites entity."""
    model_config = ConfigDict(extra="allow")

    permission_level: str | None = None
    """The user's permission level for the site (owner, full, restricted, etc.)"""
    site_url: str | None = None
    """The URL of the site data being fetched"""


class SitemapsSearchData(BaseModel):
    """Search result data for sitemaps entity."""
    model_config = ConfigDict(extra="allow")

    contents: list[Any] | None = None
    """Data related to the sitemap contents"""
    errors: str | None = None
    """Errors encountered while processing the sitemaps"""
    is_pending: bool | None = None
    """Flag indicating if the sitemap is pending for processing"""
    is_sitemaps_index: bool | None = None
    """Flag indicating if the data represents a sitemap index"""
    last_downloaded: str | None = None
    """Timestamp when the sitemap was last downloaded"""
    last_submitted: str | None = None
    """Timestamp when the sitemap was last submitted"""
    path: str | None = None
    """Path to the sitemap file"""
    type_: str | None = None
    """Type of the sitemap"""
    warnings: str | None = None
    """Warnings encountered while processing the sitemaps"""


class SearchAnalyticsAllFieldsSearchData(BaseModel):
    """Search result data for search_analytics_all_fields entity."""
    model_config = ConfigDict(extra="allow")

    clicks: int | None = None
    """The number of times users clicked on the search result for a specific query"""
    country: str | None = None
    """The country from which the search query originated"""
    ctr: float | None = None
    """Click-through rate, calculated as clicks divided by impressions"""
    date: str | None = None
    """The date when the search query occurred"""
    device: str | None = None
    """The type of device used by the user (e.g., desktop, mobile)"""
    impressions: int | None = None
    """The number of times a search result appeared in response to a query"""
    page: str | None = None
    """The page URL that appeared in the search results"""
    position: float | None = None
    """The average position of the search result on the search engine results page"""
    query: str | None = None
    """The search query entered by the user"""
    search_type: str | None = None
    """The type of search (e.g., web, image, video) that triggered the search result"""
    site_url: str | None = None
    """The URL of the site from which the data originates"""


class SearchAnalyticsByCountrySearchData(BaseModel):
    """Search result data for search_analytics_by_country entity."""
    model_config = ConfigDict(extra="allow")

    clicks: int | None = None
    """The number of times users clicked on the search result for a specific country"""
    country: str | None = None
    """The country for which the search analytics data is being reported"""
    ctr: float | None = None
    """The click-through rate for a specific country"""
    date: str | None = None
    """The date for which the search analytics data is being reported"""
    impressions: int | None = None
    """The total number of times a search result was shown for a specific country"""
    position: float | None = None
    """The average position at which the site's search result appeared for a specific country"""
    search_type: str | None = None
    """The type of search for which the data is being reported"""
    site_url: str | None = None
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByDateSearchData(BaseModel):
    """Search result data for search_analytics_by_date entity."""
    model_config = ConfigDict(extra="allow")

    clicks: int | None = None
    """The total number of clicks on the specific date"""
    ctr: float | None = None
    """The click-through rate for the specific date"""
    date: str | None = None
    """The date for which the search analytics data is being reported"""
    impressions: int | None = None
    """The number of impressions on the specific date"""
    position: float | None = None
    """The average position in search results for the specific date"""
    search_type: str | None = None
    """The type of search query that generated the data"""
    site_url: str | None = None
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByDeviceSearchData(BaseModel):
    """Search result data for search_analytics_by_device entity."""
    model_config = ConfigDict(extra="allow")

    clicks: int | None = None
    """The total number of clicks by device type"""
    ctr: float | None = None
    """Click-through rate by device type"""
    date: str | None = None
    """The date for which the search analytics data is provided"""
    device: str | None = None
    """The type of device used by the user (e.g., desktop, mobile)"""
    impressions: int | None = None
    """The total number of impressions by device type"""
    position: float | None = None
    """The average position in search results by device type"""
    search_type: str | None = None
    """The type of search performed"""
    site_url: str | None = None
    """The URL of the site for which search analytics data is being provided"""


class SearchAnalyticsByPageSearchData(BaseModel):
    """Search result data for search_analytics_by_page entity."""
    model_config = ConfigDict(extra="allow")

    clicks: int | None = None
    """The number of clicks for a specific page"""
    ctr: float | None = None
    """Click-through rate for the page"""
    date: str | None = None
    """The date for which the search analytics data is reported"""
    impressions: int | None = None
    """The number of impressions for the page"""
    page: str | None = None
    """The URL of the specific page being analyzed"""
    position: float | None = None
    """The average position at which the page appeared in search results"""
    search_type: str | None = None
    """The type of search query that led to the page being displayed"""
    site_url: str | None = None
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByQuerySearchData(BaseModel):
    """Search result data for search_analytics_by_query entity."""
    model_config = ConfigDict(extra="allow")

    clicks: int | None = None
    """The number of clicks for the specific query"""
    ctr: float | None = None
    """The click-through rate for the specific query"""
    date: str | None = None
    """The date for which the search analytics data is recorded"""
    impressions: int | None = None
    """The number of impressions for the specific query"""
    position: float | None = None
    """The average position for the specific query"""
    query: str | None = None
    """The search query for which the data is recorded"""
    search_type: str | None = None
    """The type of search result for the specific query"""
    site_url: str | None = None
    """The URL of the site for which the search analytics data is captured"""


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

SitesSearchResult = AirbyteSearchResult[SitesSearchData]
"""Search result type for sites entity."""

SitemapsSearchResult = AirbyteSearchResult[SitemapsSearchData]
"""Search result type for sitemaps entity."""

SearchAnalyticsAllFieldsSearchResult = AirbyteSearchResult[SearchAnalyticsAllFieldsSearchData]
"""Search result type for search_analytics_all_fields entity."""

SearchAnalyticsByCountrySearchResult = AirbyteSearchResult[SearchAnalyticsByCountrySearchData]
"""Search result type for search_analytics_by_country entity."""

SearchAnalyticsByDateSearchResult = AirbyteSearchResult[SearchAnalyticsByDateSearchData]
"""Search result type for search_analytics_by_date entity."""

SearchAnalyticsByDeviceSearchResult = AirbyteSearchResult[SearchAnalyticsByDeviceSearchData]
"""Search result type for search_analytics_by_device entity."""

SearchAnalyticsByPageSearchResult = AirbyteSearchResult[SearchAnalyticsByPageSearchData]
"""Search result type for search_analytics_by_page entity."""

SearchAnalyticsByQuerySearchResult = AirbyteSearchResult[SearchAnalyticsByQuerySearchData]
"""Search result type for search_analytics_by_query entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

SitesListResult = GoogleSearchConsoleExecuteResult[list[Site]]
"""Result type for sites.list operation."""

SitemapsListResult = GoogleSearchConsoleExecuteResult[list[Sitemap]]
"""Result type for sitemaps.list operation."""

SearchAnalyticsByDateListResult = GoogleSearchConsoleExecuteResult[list[SearchAnalyticsRow]]
"""Result type for search_analytics_by_date.list operation."""

SearchAnalyticsByCountryListResult = GoogleSearchConsoleExecuteResult[list[SearchAnalyticsRow]]
"""Result type for search_analytics_by_country.list operation."""

SearchAnalyticsByDeviceListResult = GoogleSearchConsoleExecuteResult[list[SearchAnalyticsRow]]
"""Result type for search_analytics_by_device.list operation."""

SearchAnalyticsByPageListResult = GoogleSearchConsoleExecuteResult[list[SearchAnalyticsRow]]
"""Result type for search_analytics_by_page.list operation."""

SearchAnalyticsByQueryListResult = GoogleSearchConsoleExecuteResult[list[SearchAnalyticsRow]]
"""Result type for search_analytics_by_query.list operation."""

SearchAnalyticsAllFieldsListResult = GoogleSearchConsoleExecuteResult[list[SearchAnalyticsRow]]
"""Result type for search_analytics_all_fields.list operation."""

