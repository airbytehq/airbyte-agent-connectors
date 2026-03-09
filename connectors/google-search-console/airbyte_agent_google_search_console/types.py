"""
Type definitions for google-search-console connector.
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

class SitesListParams(TypedDict):
    """Parameters for sites.list operation"""
    pass

class SitesGetParams(TypedDict):
    """Parameters for sites.get operation"""
    site_url: str

class SitemapsListParams(TypedDict):
    """Parameters for sitemaps.list operation"""
    site_url: str

class SitemapsGetParams(TypedDict):
    """Parameters for sitemaps.get operation"""
    site_url: str
    feedpath: str

class SearchAnalyticsByDateListParams(TypedDict):
    """Parameters for search_analytics_by_date.list operation"""
    start_date: str
    end_date: str
    dimensions: NotRequired[list[str]]
    row_limit: NotRequired[int]
    start_row: NotRequired[int]
    type: NotRequired[str]
    aggregation_type: NotRequired[str]
    data_state: NotRequired[str]
    site_url: str

class SearchAnalyticsByCountryListParams(TypedDict):
    """Parameters for search_analytics_by_country.list operation"""
    start_date: str
    end_date: str
    dimensions: NotRequired[list[str]]
    row_limit: NotRequired[int]
    start_row: NotRequired[int]
    type: NotRequired[str]
    aggregation_type: NotRequired[str]
    data_state: NotRequired[str]
    site_url: str

class SearchAnalyticsByDeviceListParams(TypedDict):
    """Parameters for search_analytics_by_device.list operation"""
    start_date: str
    end_date: str
    dimensions: NotRequired[list[str]]
    row_limit: NotRequired[int]
    start_row: NotRequired[int]
    type: NotRequired[str]
    aggregation_type: NotRequired[str]
    data_state: NotRequired[str]
    site_url: str

class SearchAnalyticsByPageListParams(TypedDict):
    """Parameters for search_analytics_by_page.list operation"""
    start_date: str
    end_date: str
    dimensions: NotRequired[list[str]]
    row_limit: NotRequired[int]
    start_row: NotRequired[int]
    type: NotRequired[str]
    aggregation_type: NotRequired[str]
    data_state: NotRequired[str]
    site_url: str

class SearchAnalyticsByQueryListParams(TypedDict):
    """Parameters for search_analytics_by_query.list operation"""
    start_date: str
    end_date: str
    dimensions: NotRequired[list[str]]
    row_limit: NotRequired[int]
    start_row: NotRequired[int]
    type: NotRequired[str]
    aggregation_type: NotRequired[str]
    data_state: NotRequired[str]
    site_url: str

class SearchAnalyticsAllFieldsListParams(TypedDict):
    """Parameters for search_analytics_all_fields.list operation"""
    start_date: str
    end_date: str
    dimensions: NotRequired[list[str]]
    row_limit: NotRequired[int]
    start_row: NotRequired[int]
    type: NotRequired[str]
    aggregation_type: NotRequired[str]
    data_state: NotRequired[str]
    site_url: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== SITES SEARCH TYPES =====

class SitesSearchFilter(TypedDict, total=False):
    """Available fields for filtering sites search queries."""
    permission_level: str | None
    """The user's permission level for the site (owner, full, restricted, etc.)"""
    site_url: str | None
    """The URL of the site data being fetched"""


class SitesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    permission_level: list[str]
    """The user's permission level for the site (owner, full, restricted, etc.)"""
    site_url: list[str]
    """The URL of the site data being fetched"""


class SitesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    permission_level: Any
    """The user's permission level for the site (owner, full, restricted, etc.)"""
    site_url: Any
    """The URL of the site data being fetched"""


class SitesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    permission_level: str
    """The user's permission level for the site (owner, full, restricted, etc.)"""
    site_url: str
    """The URL of the site data being fetched"""


class SitesSortFilter(TypedDict, total=False):
    """Available fields for sorting sites search results."""
    permission_level: AirbyteSortOrder
    """The user's permission level for the site (owner, full, restricted, etc.)"""
    site_url: AirbyteSortOrder
    """The URL of the site data being fetched"""


# Entity-specific condition types for sites
class SitesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SitesSearchFilter


class SitesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SitesSearchFilter


class SitesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SitesSearchFilter


class SitesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SitesSearchFilter


class SitesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SitesSearchFilter


class SitesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SitesSearchFilter


class SitesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SitesStringFilter


class SitesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SitesStringFilter


class SitesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SitesStringFilter


class SitesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SitesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SitesInCondition = TypedDict("SitesInCondition", {"in": SitesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SitesNotCondition = TypedDict("SitesNotCondition", {"not": "SitesCondition"}, total=False)
"""Negates the nested condition."""

SitesAndCondition = TypedDict("SitesAndCondition", {"and": "list[SitesCondition]"}, total=False)
"""True if all nested conditions are true."""

SitesOrCondition = TypedDict("SitesOrCondition", {"or": "list[SitesCondition]"}, total=False)
"""True if any nested condition is true."""

SitesAnyCondition = TypedDict("SitesAnyCondition", {"any": SitesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sites condition types
SitesCondition = (
    SitesEqCondition
    | SitesNeqCondition
    | SitesGtCondition
    | SitesGteCondition
    | SitesLtCondition
    | SitesLteCondition
    | SitesInCondition
    | SitesLikeCondition
    | SitesFuzzyCondition
    | SitesKeywordCondition
    | SitesContainsCondition
    | SitesNotCondition
    | SitesAndCondition
    | SitesOrCondition
    | SitesAnyCondition
)


class SitesSearchQuery(TypedDict, total=False):
    """Search query for sites entity."""
    filter: SitesCondition
    sort: list[SitesSortFilter]


# ===== SITEMAPS SEARCH TYPES =====

class SitemapsSearchFilter(TypedDict, total=False):
    """Available fields for filtering sitemaps search queries."""
    contents: list[Any] | None
    """Data related to the sitemap contents"""
    errors: str | None
    """Errors encountered while processing the sitemaps"""
    is_pending: bool | None
    """Flag indicating if the sitemap is pending for processing"""
    is_sitemaps_index: bool | None
    """Flag indicating if the data represents a sitemap index"""
    last_downloaded: str | None
    """Timestamp when the sitemap was last downloaded"""
    last_submitted: str | None
    """Timestamp when the sitemap was last submitted"""
    path: str | None
    """Path to the sitemap file"""
    type_: str | None
    """Type of the sitemap"""
    warnings: str | None
    """Warnings encountered while processing the sitemaps"""


class SitemapsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    contents: list[list[Any]]
    """Data related to the sitemap contents"""
    errors: list[str]
    """Errors encountered while processing the sitemaps"""
    is_pending: list[bool]
    """Flag indicating if the sitemap is pending for processing"""
    is_sitemaps_index: list[bool]
    """Flag indicating if the data represents a sitemap index"""
    last_downloaded: list[str]
    """Timestamp when the sitemap was last downloaded"""
    last_submitted: list[str]
    """Timestamp when the sitemap was last submitted"""
    path: list[str]
    """Path to the sitemap file"""
    type_: list[str]
    """Type of the sitemap"""
    warnings: list[str]
    """Warnings encountered while processing the sitemaps"""


class SitemapsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    contents: Any
    """Data related to the sitemap contents"""
    errors: Any
    """Errors encountered while processing the sitemaps"""
    is_pending: Any
    """Flag indicating if the sitemap is pending for processing"""
    is_sitemaps_index: Any
    """Flag indicating if the data represents a sitemap index"""
    last_downloaded: Any
    """Timestamp when the sitemap was last downloaded"""
    last_submitted: Any
    """Timestamp when the sitemap was last submitted"""
    path: Any
    """Path to the sitemap file"""
    type_: Any
    """Type of the sitemap"""
    warnings: Any
    """Warnings encountered while processing the sitemaps"""


class SitemapsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    contents: str
    """Data related to the sitemap contents"""
    errors: str
    """Errors encountered while processing the sitemaps"""
    is_pending: str
    """Flag indicating if the sitemap is pending for processing"""
    is_sitemaps_index: str
    """Flag indicating if the data represents a sitemap index"""
    last_downloaded: str
    """Timestamp when the sitemap was last downloaded"""
    last_submitted: str
    """Timestamp when the sitemap was last submitted"""
    path: str
    """Path to the sitemap file"""
    type_: str
    """Type of the sitemap"""
    warnings: str
    """Warnings encountered while processing the sitemaps"""


class SitemapsSortFilter(TypedDict, total=False):
    """Available fields for sorting sitemaps search results."""
    contents: AirbyteSortOrder
    """Data related to the sitemap contents"""
    errors: AirbyteSortOrder
    """Errors encountered while processing the sitemaps"""
    is_pending: AirbyteSortOrder
    """Flag indicating if the sitemap is pending for processing"""
    is_sitemaps_index: AirbyteSortOrder
    """Flag indicating if the data represents a sitemap index"""
    last_downloaded: AirbyteSortOrder
    """Timestamp when the sitemap was last downloaded"""
    last_submitted: AirbyteSortOrder
    """Timestamp when the sitemap was last submitted"""
    path: AirbyteSortOrder
    """Path to the sitemap file"""
    type_: AirbyteSortOrder
    """Type of the sitemap"""
    warnings: AirbyteSortOrder
    """Warnings encountered while processing the sitemaps"""


# Entity-specific condition types for sitemaps
class SitemapsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SitemapsSearchFilter


class SitemapsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SitemapsSearchFilter


class SitemapsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SitemapsSearchFilter


class SitemapsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SitemapsSearchFilter


class SitemapsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SitemapsSearchFilter


class SitemapsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SitemapsSearchFilter


class SitemapsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SitemapsStringFilter


class SitemapsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SitemapsStringFilter


class SitemapsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SitemapsStringFilter


class SitemapsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SitemapsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SitemapsInCondition = TypedDict("SitemapsInCondition", {"in": SitemapsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SitemapsNotCondition = TypedDict("SitemapsNotCondition", {"not": "SitemapsCondition"}, total=False)
"""Negates the nested condition."""

SitemapsAndCondition = TypedDict("SitemapsAndCondition", {"and": "list[SitemapsCondition]"}, total=False)
"""True if all nested conditions are true."""

SitemapsOrCondition = TypedDict("SitemapsOrCondition", {"or": "list[SitemapsCondition]"}, total=False)
"""True if any nested condition is true."""

SitemapsAnyCondition = TypedDict("SitemapsAnyCondition", {"any": SitemapsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sitemaps condition types
SitemapsCondition = (
    SitemapsEqCondition
    | SitemapsNeqCondition
    | SitemapsGtCondition
    | SitemapsGteCondition
    | SitemapsLtCondition
    | SitemapsLteCondition
    | SitemapsInCondition
    | SitemapsLikeCondition
    | SitemapsFuzzyCondition
    | SitemapsKeywordCondition
    | SitemapsContainsCondition
    | SitemapsNotCondition
    | SitemapsAndCondition
    | SitemapsOrCondition
    | SitemapsAnyCondition
)


class SitemapsSearchQuery(TypedDict, total=False):
    """Search query for sitemaps entity."""
    filter: SitemapsCondition
    sort: list[SitemapsSortFilter]


# ===== SEARCH_ANALYTICS_ALL_FIELDS SEARCH TYPES =====

class SearchAnalyticsAllFieldsSearchFilter(TypedDict, total=False):
    """Available fields for filtering search_analytics_all_fields search queries."""
    clicks: int | None
    """The number of times users clicked on the search result for a specific query"""
    country: str | None
    """The country from which the search query originated"""
    ctr: float | None
    """Click-through rate, calculated as clicks divided by impressions"""
    date: str | None
    """The date when the search query occurred"""
    device: str | None
    """The type of device used by the user (e.g., desktop, mobile)"""
    impressions: int | None
    """The number of times a search result appeared in response to a query"""
    page: str | None
    """The page URL that appeared in the search results"""
    position: float | None
    """The average position of the search result on the search engine results page"""
    query: str | None
    """The search query entered by the user"""
    search_type: str | None
    """The type of search (e.g., web, image, video) that triggered the search result"""
    site_url: str | None
    """The URL of the site from which the data originates"""


class SearchAnalyticsAllFieldsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    clicks: list[int]
    """The number of times users clicked on the search result for a specific query"""
    country: list[str]
    """The country from which the search query originated"""
    ctr: list[float]
    """Click-through rate, calculated as clicks divided by impressions"""
    date: list[str]
    """The date when the search query occurred"""
    device: list[str]
    """The type of device used by the user (e.g., desktop, mobile)"""
    impressions: list[int]
    """The number of times a search result appeared in response to a query"""
    page: list[str]
    """The page URL that appeared in the search results"""
    position: list[float]
    """The average position of the search result on the search engine results page"""
    query: list[str]
    """The search query entered by the user"""
    search_type: list[str]
    """The type of search (e.g., web, image, video) that triggered the search result"""
    site_url: list[str]
    """The URL of the site from which the data originates"""


class SearchAnalyticsAllFieldsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    clicks: Any
    """The number of times users clicked on the search result for a specific query"""
    country: Any
    """The country from which the search query originated"""
    ctr: Any
    """Click-through rate, calculated as clicks divided by impressions"""
    date: Any
    """The date when the search query occurred"""
    device: Any
    """The type of device used by the user (e.g., desktop, mobile)"""
    impressions: Any
    """The number of times a search result appeared in response to a query"""
    page: Any
    """The page URL that appeared in the search results"""
    position: Any
    """The average position of the search result on the search engine results page"""
    query: Any
    """The search query entered by the user"""
    search_type: Any
    """The type of search (e.g., web, image, video) that triggered the search result"""
    site_url: Any
    """The URL of the site from which the data originates"""


class SearchAnalyticsAllFieldsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    clicks: str
    """The number of times users clicked on the search result for a specific query"""
    country: str
    """The country from which the search query originated"""
    ctr: str
    """Click-through rate, calculated as clicks divided by impressions"""
    date: str
    """The date when the search query occurred"""
    device: str
    """The type of device used by the user (e.g., desktop, mobile)"""
    impressions: str
    """The number of times a search result appeared in response to a query"""
    page: str
    """The page URL that appeared in the search results"""
    position: str
    """The average position of the search result on the search engine results page"""
    query: str
    """The search query entered by the user"""
    search_type: str
    """The type of search (e.g., web, image, video) that triggered the search result"""
    site_url: str
    """The URL of the site from which the data originates"""


class SearchAnalyticsAllFieldsSortFilter(TypedDict, total=False):
    """Available fields for sorting search_analytics_all_fields search results."""
    clicks: AirbyteSortOrder
    """The number of times users clicked on the search result for a specific query"""
    country: AirbyteSortOrder
    """The country from which the search query originated"""
    ctr: AirbyteSortOrder
    """Click-through rate, calculated as clicks divided by impressions"""
    date: AirbyteSortOrder
    """The date when the search query occurred"""
    device: AirbyteSortOrder
    """The type of device used by the user (e.g., desktop, mobile)"""
    impressions: AirbyteSortOrder
    """The number of times a search result appeared in response to a query"""
    page: AirbyteSortOrder
    """The page URL that appeared in the search results"""
    position: AirbyteSortOrder
    """The average position of the search result on the search engine results page"""
    query: AirbyteSortOrder
    """The search query entered by the user"""
    search_type: AirbyteSortOrder
    """The type of search (e.g., web, image, video) that triggered the search result"""
    site_url: AirbyteSortOrder
    """The URL of the site from which the data originates"""


# Entity-specific condition types for search_analytics_all_fields
class SearchAnalyticsAllFieldsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SearchAnalyticsAllFieldsSearchFilter


class SearchAnalyticsAllFieldsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SearchAnalyticsAllFieldsSearchFilter


class SearchAnalyticsAllFieldsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SearchAnalyticsAllFieldsSearchFilter


class SearchAnalyticsAllFieldsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SearchAnalyticsAllFieldsSearchFilter


class SearchAnalyticsAllFieldsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SearchAnalyticsAllFieldsSearchFilter


class SearchAnalyticsAllFieldsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SearchAnalyticsAllFieldsSearchFilter


class SearchAnalyticsAllFieldsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SearchAnalyticsAllFieldsStringFilter


class SearchAnalyticsAllFieldsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SearchAnalyticsAllFieldsStringFilter


class SearchAnalyticsAllFieldsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SearchAnalyticsAllFieldsStringFilter


class SearchAnalyticsAllFieldsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SearchAnalyticsAllFieldsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SearchAnalyticsAllFieldsInCondition = TypedDict("SearchAnalyticsAllFieldsInCondition", {"in": SearchAnalyticsAllFieldsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SearchAnalyticsAllFieldsNotCondition = TypedDict("SearchAnalyticsAllFieldsNotCondition", {"not": "SearchAnalyticsAllFieldsCondition"}, total=False)
"""Negates the nested condition."""

SearchAnalyticsAllFieldsAndCondition = TypedDict("SearchAnalyticsAllFieldsAndCondition", {"and": "list[SearchAnalyticsAllFieldsCondition]"}, total=False)
"""True if all nested conditions are true."""

SearchAnalyticsAllFieldsOrCondition = TypedDict("SearchAnalyticsAllFieldsOrCondition", {"or": "list[SearchAnalyticsAllFieldsCondition]"}, total=False)
"""True if any nested condition is true."""

SearchAnalyticsAllFieldsAnyCondition = TypedDict("SearchAnalyticsAllFieldsAnyCondition", {"any": SearchAnalyticsAllFieldsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all search_analytics_all_fields condition types
SearchAnalyticsAllFieldsCondition = (
    SearchAnalyticsAllFieldsEqCondition
    | SearchAnalyticsAllFieldsNeqCondition
    | SearchAnalyticsAllFieldsGtCondition
    | SearchAnalyticsAllFieldsGteCondition
    | SearchAnalyticsAllFieldsLtCondition
    | SearchAnalyticsAllFieldsLteCondition
    | SearchAnalyticsAllFieldsInCondition
    | SearchAnalyticsAllFieldsLikeCondition
    | SearchAnalyticsAllFieldsFuzzyCondition
    | SearchAnalyticsAllFieldsKeywordCondition
    | SearchAnalyticsAllFieldsContainsCondition
    | SearchAnalyticsAllFieldsNotCondition
    | SearchAnalyticsAllFieldsAndCondition
    | SearchAnalyticsAllFieldsOrCondition
    | SearchAnalyticsAllFieldsAnyCondition
)


class SearchAnalyticsAllFieldsSearchQuery(TypedDict, total=False):
    """Search query for search_analytics_all_fields entity."""
    filter: SearchAnalyticsAllFieldsCondition
    sort: list[SearchAnalyticsAllFieldsSortFilter]


# ===== SEARCH_ANALYTICS_BY_COUNTRY SEARCH TYPES =====

class SearchAnalyticsByCountrySearchFilter(TypedDict, total=False):
    """Available fields for filtering search_analytics_by_country search queries."""
    clicks: int | None
    """The number of times users clicked on the search result for a specific country"""
    country: str | None
    """The country for which the search analytics data is being reported"""
    ctr: float | None
    """The click-through rate for a specific country"""
    date: str | None
    """The date for which the search analytics data is being reported"""
    impressions: int | None
    """The total number of times a search result was shown for a specific country"""
    position: float | None
    """The average position at which the site's search result appeared for a specific country"""
    search_type: str | None
    """The type of search for which the data is being reported"""
    site_url: str | None
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByCountryInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    clicks: list[int]
    """The number of times users clicked on the search result for a specific country"""
    country: list[str]
    """The country for which the search analytics data is being reported"""
    ctr: list[float]
    """The click-through rate for a specific country"""
    date: list[str]
    """The date for which the search analytics data is being reported"""
    impressions: list[int]
    """The total number of times a search result was shown for a specific country"""
    position: list[float]
    """The average position at which the site's search result appeared for a specific country"""
    search_type: list[str]
    """The type of search for which the data is being reported"""
    site_url: list[str]
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByCountryAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    clicks: Any
    """The number of times users clicked on the search result for a specific country"""
    country: Any
    """The country for which the search analytics data is being reported"""
    ctr: Any
    """The click-through rate for a specific country"""
    date: Any
    """The date for which the search analytics data is being reported"""
    impressions: Any
    """The total number of times a search result was shown for a specific country"""
    position: Any
    """The average position at which the site's search result appeared for a specific country"""
    search_type: Any
    """The type of search for which the data is being reported"""
    site_url: Any
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByCountryStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    clicks: str
    """The number of times users clicked on the search result for a specific country"""
    country: str
    """The country for which the search analytics data is being reported"""
    ctr: str
    """The click-through rate for a specific country"""
    date: str
    """The date for which the search analytics data is being reported"""
    impressions: str
    """The total number of times a search result was shown for a specific country"""
    position: str
    """The average position at which the site's search result appeared for a specific country"""
    search_type: str
    """The type of search for which the data is being reported"""
    site_url: str
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByCountrySortFilter(TypedDict, total=False):
    """Available fields for sorting search_analytics_by_country search results."""
    clicks: AirbyteSortOrder
    """The number of times users clicked on the search result for a specific country"""
    country: AirbyteSortOrder
    """The country for which the search analytics data is being reported"""
    ctr: AirbyteSortOrder
    """The click-through rate for a specific country"""
    date: AirbyteSortOrder
    """The date for which the search analytics data is being reported"""
    impressions: AirbyteSortOrder
    """The total number of times a search result was shown for a specific country"""
    position: AirbyteSortOrder
    """The average position at which the site's search result appeared for a specific country"""
    search_type: AirbyteSortOrder
    """The type of search for which the data is being reported"""
    site_url: AirbyteSortOrder
    """The URL of the site for which the search analytics data is being reported"""


# Entity-specific condition types for search_analytics_by_country
class SearchAnalyticsByCountryEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SearchAnalyticsByCountrySearchFilter


class SearchAnalyticsByCountryNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SearchAnalyticsByCountrySearchFilter


class SearchAnalyticsByCountryGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SearchAnalyticsByCountrySearchFilter


class SearchAnalyticsByCountryGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SearchAnalyticsByCountrySearchFilter


class SearchAnalyticsByCountryLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SearchAnalyticsByCountrySearchFilter


class SearchAnalyticsByCountryLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SearchAnalyticsByCountrySearchFilter


class SearchAnalyticsByCountryLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SearchAnalyticsByCountryStringFilter


class SearchAnalyticsByCountryFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SearchAnalyticsByCountryStringFilter


class SearchAnalyticsByCountryKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SearchAnalyticsByCountryStringFilter


class SearchAnalyticsByCountryContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SearchAnalyticsByCountryAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SearchAnalyticsByCountryInCondition = TypedDict("SearchAnalyticsByCountryInCondition", {"in": SearchAnalyticsByCountryInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SearchAnalyticsByCountryNotCondition = TypedDict("SearchAnalyticsByCountryNotCondition", {"not": "SearchAnalyticsByCountryCondition"}, total=False)
"""Negates the nested condition."""

SearchAnalyticsByCountryAndCondition = TypedDict("SearchAnalyticsByCountryAndCondition", {"and": "list[SearchAnalyticsByCountryCondition]"}, total=False)
"""True if all nested conditions are true."""

SearchAnalyticsByCountryOrCondition = TypedDict("SearchAnalyticsByCountryOrCondition", {"or": "list[SearchAnalyticsByCountryCondition]"}, total=False)
"""True if any nested condition is true."""

SearchAnalyticsByCountryAnyCondition = TypedDict("SearchAnalyticsByCountryAnyCondition", {"any": SearchAnalyticsByCountryAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all search_analytics_by_country condition types
SearchAnalyticsByCountryCondition = (
    SearchAnalyticsByCountryEqCondition
    | SearchAnalyticsByCountryNeqCondition
    | SearchAnalyticsByCountryGtCondition
    | SearchAnalyticsByCountryGteCondition
    | SearchAnalyticsByCountryLtCondition
    | SearchAnalyticsByCountryLteCondition
    | SearchAnalyticsByCountryInCondition
    | SearchAnalyticsByCountryLikeCondition
    | SearchAnalyticsByCountryFuzzyCondition
    | SearchAnalyticsByCountryKeywordCondition
    | SearchAnalyticsByCountryContainsCondition
    | SearchAnalyticsByCountryNotCondition
    | SearchAnalyticsByCountryAndCondition
    | SearchAnalyticsByCountryOrCondition
    | SearchAnalyticsByCountryAnyCondition
)


class SearchAnalyticsByCountrySearchQuery(TypedDict, total=False):
    """Search query for search_analytics_by_country entity."""
    filter: SearchAnalyticsByCountryCondition
    sort: list[SearchAnalyticsByCountrySortFilter]


# ===== SEARCH_ANALYTICS_BY_DATE SEARCH TYPES =====

class SearchAnalyticsByDateSearchFilter(TypedDict, total=False):
    """Available fields for filtering search_analytics_by_date search queries."""
    clicks: int | None
    """The total number of clicks on the specific date"""
    ctr: float | None
    """The click-through rate for the specific date"""
    date: str | None
    """The date for which the search analytics data is being reported"""
    impressions: int | None
    """The number of impressions on the specific date"""
    position: float | None
    """The average position in search results for the specific date"""
    search_type: str | None
    """The type of search query that generated the data"""
    site_url: str | None
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByDateInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    clicks: list[int]
    """The total number of clicks on the specific date"""
    ctr: list[float]
    """The click-through rate for the specific date"""
    date: list[str]
    """The date for which the search analytics data is being reported"""
    impressions: list[int]
    """The number of impressions on the specific date"""
    position: list[float]
    """The average position in search results for the specific date"""
    search_type: list[str]
    """The type of search query that generated the data"""
    site_url: list[str]
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByDateAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    clicks: Any
    """The total number of clicks on the specific date"""
    ctr: Any
    """The click-through rate for the specific date"""
    date: Any
    """The date for which the search analytics data is being reported"""
    impressions: Any
    """The number of impressions on the specific date"""
    position: Any
    """The average position in search results for the specific date"""
    search_type: Any
    """The type of search query that generated the data"""
    site_url: Any
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByDateStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    clicks: str
    """The total number of clicks on the specific date"""
    ctr: str
    """The click-through rate for the specific date"""
    date: str
    """The date for which the search analytics data is being reported"""
    impressions: str
    """The number of impressions on the specific date"""
    position: str
    """The average position in search results for the specific date"""
    search_type: str
    """The type of search query that generated the data"""
    site_url: str
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByDateSortFilter(TypedDict, total=False):
    """Available fields for sorting search_analytics_by_date search results."""
    clicks: AirbyteSortOrder
    """The total number of clicks on the specific date"""
    ctr: AirbyteSortOrder
    """The click-through rate for the specific date"""
    date: AirbyteSortOrder
    """The date for which the search analytics data is being reported"""
    impressions: AirbyteSortOrder
    """The number of impressions on the specific date"""
    position: AirbyteSortOrder
    """The average position in search results for the specific date"""
    search_type: AirbyteSortOrder
    """The type of search query that generated the data"""
    site_url: AirbyteSortOrder
    """The URL of the site for which the search analytics data is being reported"""


# Entity-specific condition types for search_analytics_by_date
class SearchAnalyticsByDateEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SearchAnalyticsByDateSearchFilter


class SearchAnalyticsByDateNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SearchAnalyticsByDateSearchFilter


class SearchAnalyticsByDateGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SearchAnalyticsByDateSearchFilter


class SearchAnalyticsByDateGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SearchAnalyticsByDateSearchFilter


class SearchAnalyticsByDateLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SearchAnalyticsByDateSearchFilter


class SearchAnalyticsByDateLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SearchAnalyticsByDateSearchFilter


class SearchAnalyticsByDateLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SearchAnalyticsByDateStringFilter


class SearchAnalyticsByDateFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SearchAnalyticsByDateStringFilter


class SearchAnalyticsByDateKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SearchAnalyticsByDateStringFilter


class SearchAnalyticsByDateContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SearchAnalyticsByDateAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SearchAnalyticsByDateInCondition = TypedDict("SearchAnalyticsByDateInCondition", {"in": SearchAnalyticsByDateInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SearchAnalyticsByDateNotCondition = TypedDict("SearchAnalyticsByDateNotCondition", {"not": "SearchAnalyticsByDateCondition"}, total=False)
"""Negates the nested condition."""

SearchAnalyticsByDateAndCondition = TypedDict("SearchAnalyticsByDateAndCondition", {"and": "list[SearchAnalyticsByDateCondition]"}, total=False)
"""True if all nested conditions are true."""

SearchAnalyticsByDateOrCondition = TypedDict("SearchAnalyticsByDateOrCondition", {"or": "list[SearchAnalyticsByDateCondition]"}, total=False)
"""True if any nested condition is true."""

SearchAnalyticsByDateAnyCondition = TypedDict("SearchAnalyticsByDateAnyCondition", {"any": SearchAnalyticsByDateAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all search_analytics_by_date condition types
SearchAnalyticsByDateCondition = (
    SearchAnalyticsByDateEqCondition
    | SearchAnalyticsByDateNeqCondition
    | SearchAnalyticsByDateGtCondition
    | SearchAnalyticsByDateGteCondition
    | SearchAnalyticsByDateLtCondition
    | SearchAnalyticsByDateLteCondition
    | SearchAnalyticsByDateInCondition
    | SearchAnalyticsByDateLikeCondition
    | SearchAnalyticsByDateFuzzyCondition
    | SearchAnalyticsByDateKeywordCondition
    | SearchAnalyticsByDateContainsCondition
    | SearchAnalyticsByDateNotCondition
    | SearchAnalyticsByDateAndCondition
    | SearchAnalyticsByDateOrCondition
    | SearchAnalyticsByDateAnyCondition
)


class SearchAnalyticsByDateSearchQuery(TypedDict, total=False):
    """Search query for search_analytics_by_date entity."""
    filter: SearchAnalyticsByDateCondition
    sort: list[SearchAnalyticsByDateSortFilter]


# ===== SEARCH_ANALYTICS_BY_DEVICE SEARCH TYPES =====

class SearchAnalyticsByDeviceSearchFilter(TypedDict, total=False):
    """Available fields for filtering search_analytics_by_device search queries."""
    clicks: int | None
    """The total number of clicks by device type"""
    ctr: float | None
    """Click-through rate by device type"""
    date: str | None
    """The date for which the search analytics data is provided"""
    device: str | None
    """The type of device used by the user (e.g., desktop, mobile)"""
    impressions: int | None
    """The total number of impressions by device type"""
    position: float | None
    """The average position in search results by device type"""
    search_type: str | None
    """The type of search performed"""
    site_url: str | None
    """The URL of the site for which search analytics data is being provided"""


class SearchAnalyticsByDeviceInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    clicks: list[int]
    """The total number of clicks by device type"""
    ctr: list[float]
    """Click-through rate by device type"""
    date: list[str]
    """The date for which the search analytics data is provided"""
    device: list[str]
    """The type of device used by the user (e.g., desktop, mobile)"""
    impressions: list[int]
    """The total number of impressions by device type"""
    position: list[float]
    """The average position in search results by device type"""
    search_type: list[str]
    """The type of search performed"""
    site_url: list[str]
    """The URL of the site for which search analytics data is being provided"""


class SearchAnalyticsByDeviceAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    clicks: Any
    """The total number of clicks by device type"""
    ctr: Any
    """Click-through rate by device type"""
    date: Any
    """The date for which the search analytics data is provided"""
    device: Any
    """The type of device used by the user (e.g., desktop, mobile)"""
    impressions: Any
    """The total number of impressions by device type"""
    position: Any
    """The average position in search results by device type"""
    search_type: Any
    """The type of search performed"""
    site_url: Any
    """The URL of the site for which search analytics data is being provided"""


class SearchAnalyticsByDeviceStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    clicks: str
    """The total number of clicks by device type"""
    ctr: str
    """Click-through rate by device type"""
    date: str
    """The date for which the search analytics data is provided"""
    device: str
    """The type of device used by the user (e.g., desktop, mobile)"""
    impressions: str
    """The total number of impressions by device type"""
    position: str
    """The average position in search results by device type"""
    search_type: str
    """The type of search performed"""
    site_url: str
    """The URL of the site for which search analytics data is being provided"""


class SearchAnalyticsByDeviceSortFilter(TypedDict, total=False):
    """Available fields for sorting search_analytics_by_device search results."""
    clicks: AirbyteSortOrder
    """The total number of clicks by device type"""
    ctr: AirbyteSortOrder
    """Click-through rate by device type"""
    date: AirbyteSortOrder
    """The date for which the search analytics data is provided"""
    device: AirbyteSortOrder
    """The type of device used by the user (e.g., desktop, mobile)"""
    impressions: AirbyteSortOrder
    """The total number of impressions by device type"""
    position: AirbyteSortOrder
    """The average position in search results by device type"""
    search_type: AirbyteSortOrder
    """The type of search performed"""
    site_url: AirbyteSortOrder
    """The URL of the site for which search analytics data is being provided"""


# Entity-specific condition types for search_analytics_by_device
class SearchAnalyticsByDeviceEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SearchAnalyticsByDeviceSearchFilter


class SearchAnalyticsByDeviceNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SearchAnalyticsByDeviceSearchFilter


class SearchAnalyticsByDeviceGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SearchAnalyticsByDeviceSearchFilter


class SearchAnalyticsByDeviceGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SearchAnalyticsByDeviceSearchFilter


class SearchAnalyticsByDeviceLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SearchAnalyticsByDeviceSearchFilter


class SearchAnalyticsByDeviceLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SearchAnalyticsByDeviceSearchFilter


class SearchAnalyticsByDeviceLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SearchAnalyticsByDeviceStringFilter


class SearchAnalyticsByDeviceFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SearchAnalyticsByDeviceStringFilter


class SearchAnalyticsByDeviceKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SearchAnalyticsByDeviceStringFilter


class SearchAnalyticsByDeviceContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SearchAnalyticsByDeviceAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SearchAnalyticsByDeviceInCondition = TypedDict("SearchAnalyticsByDeviceInCondition", {"in": SearchAnalyticsByDeviceInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SearchAnalyticsByDeviceNotCondition = TypedDict("SearchAnalyticsByDeviceNotCondition", {"not": "SearchAnalyticsByDeviceCondition"}, total=False)
"""Negates the nested condition."""

SearchAnalyticsByDeviceAndCondition = TypedDict("SearchAnalyticsByDeviceAndCondition", {"and": "list[SearchAnalyticsByDeviceCondition]"}, total=False)
"""True if all nested conditions are true."""

SearchAnalyticsByDeviceOrCondition = TypedDict("SearchAnalyticsByDeviceOrCondition", {"or": "list[SearchAnalyticsByDeviceCondition]"}, total=False)
"""True if any nested condition is true."""

SearchAnalyticsByDeviceAnyCondition = TypedDict("SearchAnalyticsByDeviceAnyCondition", {"any": SearchAnalyticsByDeviceAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all search_analytics_by_device condition types
SearchAnalyticsByDeviceCondition = (
    SearchAnalyticsByDeviceEqCondition
    | SearchAnalyticsByDeviceNeqCondition
    | SearchAnalyticsByDeviceGtCondition
    | SearchAnalyticsByDeviceGteCondition
    | SearchAnalyticsByDeviceLtCondition
    | SearchAnalyticsByDeviceLteCondition
    | SearchAnalyticsByDeviceInCondition
    | SearchAnalyticsByDeviceLikeCondition
    | SearchAnalyticsByDeviceFuzzyCondition
    | SearchAnalyticsByDeviceKeywordCondition
    | SearchAnalyticsByDeviceContainsCondition
    | SearchAnalyticsByDeviceNotCondition
    | SearchAnalyticsByDeviceAndCondition
    | SearchAnalyticsByDeviceOrCondition
    | SearchAnalyticsByDeviceAnyCondition
)


class SearchAnalyticsByDeviceSearchQuery(TypedDict, total=False):
    """Search query for search_analytics_by_device entity."""
    filter: SearchAnalyticsByDeviceCondition
    sort: list[SearchAnalyticsByDeviceSortFilter]


# ===== SEARCH_ANALYTICS_BY_PAGE SEARCH TYPES =====

class SearchAnalyticsByPageSearchFilter(TypedDict, total=False):
    """Available fields for filtering search_analytics_by_page search queries."""
    clicks: int | None
    """The number of clicks for a specific page"""
    ctr: float | None
    """Click-through rate for the page"""
    date: str | None
    """The date for which the search analytics data is reported"""
    impressions: int | None
    """The number of impressions for the page"""
    page: str | None
    """The URL of the specific page being analyzed"""
    position: float | None
    """The average position at which the page appeared in search results"""
    search_type: str | None
    """The type of search query that led to the page being displayed"""
    site_url: str | None
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByPageInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    clicks: list[int]
    """The number of clicks for a specific page"""
    ctr: list[float]
    """Click-through rate for the page"""
    date: list[str]
    """The date for which the search analytics data is reported"""
    impressions: list[int]
    """The number of impressions for the page"""
    page: list[str]
    """The URL of the specific page being analyzed"""
    position: list[float]
    """The average position at which the page appeared in search results"""
    search_type: list[str]
    """The type of search query that led to the page being displayed"""
    site_url: list[str]
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByPageAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    clicks: Any
    """The number of clicks for a specific page"""
    ctr: Any
    """Click-through rate for the page"""
    date: Any
    """The date for which the search analytics data is reported"""
    impressions: Any
    """The number of impressions for the page"""
    page: Any
    """The URL of the specific page being analyzed"""
    position: Any
    """The average position at which the page appeared in search results"""
    search_type: Any
    """The type of search query that led to the page being displayed"""
    site_url: Any
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByPageStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    clicks: str
    """The number of clicks for a specific page"""
    ctr: str
    """Click-through rate for the page"""
    date: str
    """The date for which the search analytics data is reported"""
    impressions: str
    """The number of impressions for the page"""
    page: str
    """The URL of the specific page being analyzed"""
    position: str
    """The average position at which the page appeared in search results"""
    search_type: str
    """The type of search query that led to the page being displayed"""
    site_url: str
    """The URL of the site for which the search analytics data is being reported"""


class SearchAnalyticsByPageSortFilter(TypedDict, total=False):
    """Available fields for sorting search_analytics_by_page search results."""
    clicks: AirbyteSortOrder
    """The number of clicks for a specific page"""
    ctr: AirbyteSortOrder
    """Click-through rate for the page"""
    date: AirbyteSortOrder
    """The date for which the search analytics data is reported"""
    impressions: AirbyteSortOrder
    """The number of impressions for the page"""
    page: AirbyteSortOrder
    """The URL of the specific page being analyzed"""
    position: AirbyteSortOrder
    """The average position at which the page appeared in search results"""
    search_type: AirbyteSortOrder
    """The type of search query that led to the page being displayed"""
    site_url: AirbyteSortOrder
    """The URL of the site for which the search analytics data is being reported"""


# Entity-specific condition types for search_analytics_by_page
class SearchAnalyticsByPageEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SearchAnalyticsByPageSearchFilter


class SearchAnalyticsByPageNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SearchAnalyticsByPageSearchFilter


class SearchAnalyticsByPageGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SearchAnalyticsByPageSearchFilter


class SearchAnalyticsByPageGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SearchAnalyticsByPageSearchFilter


class SearchAnalyticsByPageLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SearchAnalyticsByPageSearchFilter


class SearchAnalyticsByPageLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SearchAnalyticsByPageSearchFilter


class SearchAnalyticsByPageLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SearchAnalyticsByPageStringFilter


class SearchAnalyticsByPageFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SearchAnalyticsByPageStringFilter


class SearchAnalyticsByPageKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SearchAnalyticsByPageStringFilter


class SearchAnalyticsByPageContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SearchAnalyticsByPageAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SearchAnalyticsByPageInCondition = TypedDict("SearchAnalyticsByPageInCondition", {"in": SearchAnalyticsByPageInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SearchAnalyticsByPageNotCondition = TypedDict("SearchAnalyticsByPageNotCondition", {"not": "SearchAnalyticsByPageCondition"}, total=False)
"""Negates the nested condition."""

SearchAnalyticsByPageAndCondition = TypedDict("SearchAnalyticsByPageAndCondition", {"and": "list[SearchAnalyticsByPageCondition]"}, total=False)
"""True if all nested conditions are true."""

SearchAnalyticsByPageOrCondition = TypedDict("SearchAnalyticsByPageOrCondition", {"or": "list[SearchAnalyticsByPageCondition]"}, total=False)
"""True if any nested condition is true."""

SearchAnalyticsByPageAnyCondition = TypedDict("SearchAnalyticsByPageAnyCondition", {"any": SearchAnalyticsByPageAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all search_analytics_by_page condition types
SearchAnalyticsByPageCondition = (
    SearchAnalyticsByPageEqCondition
    | SearchAnalyticsByPageNeqCondition
    | SearchAnalyticsByPageGtCondition
    | SearchAnalyticsByPageGteCondition
    | SearchAnalyticsByPageLtCondition
    | SearchAnalyticsByPageLteCondition
    | SearchAnalyticsByPageInCondition
    | SearchAnalyticsByPageLikeCondition
    | SearchAnalyticsByPageFuzzyCondition
    | SearchAnalyticsByPageKeywordCondition
    | SearchAnalyticsByPageContainsCondition
    | SearchAnalyticsByPageNotCondition
    | SearchAnalyticsByPageAndCondition
    | SearchAnalyticsByPageOrCondition
    | SearchAnalyticsByPageAnyCondition
)


class SearchAnalyticsByPageSearchQuery(TypedDict, total=False):
    """Search query for search_analytics_by_page entity."""
    filter: SearchAnalyticsByPageCondition
    sort: list[SearchAnalyticsByPageSortFilter]


# ===== SEARCH_ANALYTICS_BY_QUERY SEARCH TYPES =====

class SearchAnalyticsByQuerySearchFilter(TypedDict, total=False):
    """Available fields for filtering search_analytics_by_query search queries."""
    clicks: int | None
    """The number of clicks for the specific query"""
    ctr: float | None
    """The click-through rate for the specific query"""
    date: str | None
    """The date for which the search analytics data is recorded"""
    impressions: int | None
    """The number of impressions for the specific query"""
    position: float | None
    """The average position for the specific query"""
    query: str | None
    """The search query for which the data is recorded"""
    search_type: str | None
    """The type of search result for the specific query"""
    site_url: str | None
    """The URL of the site for which the search analytics data is captured"""


class SearchAnalyticsByQueryInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    clicks: list[int]
    """The number of clicks for the specific query"""
    ctr: list[float]
    """The click-through rate for the specific query"""
    date: list[str]
    """The date for which the search analytics data is recorded"""
    impressions: list[int]
    """The number of impressions for the specific query"""
    position: list[float]
    """The average position for the specific query"""
    query: list[str]
    """The search query for which the data is recorded"""
    search_type: list[str]
    """The type of search result for the specific query"""
    site_url: list[str]
    """The URL of the site for which the search analytics data is captured"""


class SearchAnalyticsByQueryAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    clicks: Any
    """The number of clicks for the specific query"""
    ctr: Any
    """The click-through rate for the specific query"""
    date: Any
    """The date for which the search analytics data is recorded"""
    impressions: Any
    """The number of impressions for the specific query"""
    position: Any
    """The average position for the specific query"""
    query: Any
    """The search query for which the data is recorded"""
    search_type: Any
    """The type of search result for the specific query"""
    site_url: Any
    """The URL of the site for which the search analytics data is captured"""


class SearchAnalyticsByQueryStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    clicks: str
    """The number of clicks for the specific query"""
    ctr: str
    """The click-through rate for the specific query"""
    date: str
    """The date for which the search analytics data is recorded"""
    impressions: str
    """The number of impressions for the specific query"""
    position: str
    """The average position for the specific query"""
    query: str
    """The search query for which the data is recorded"""
    search_type: str
    """The type of search result for the specific query"""
    site_url: str
    """The URL of the site for which the search analytics data is captured"""


class SearchAnalyticsByQuerySortFilter(TypedDict, total=False):
    """Available fields for sorting search_analytics_by_query search results."""
    clicks: AirbyteSortOrder
    """The number of clicks for the specific query"""
    ctr: AirbyteSortOrder
    """The click-through rate for the specific query"""
    date: AirbyteSortOrder
    """The date for which the search analytics data is recorded"""
    impressions: AirbyteSortOrder
    """The number of impressions for the specific query"""
    position: AirbyteSortOrder
    """The average position for the specific query"""
    query: AirbyteSortOrder
    """The search query for which the data is recorded"""
    search_type: AirbyteSortOrder
    """The type of search result for the specific query"""
    site_url: AirbyteSortOrder
    """The URL of the site for which the search analytics data is captured"""


# Entity-specific condition types for search_analytics_by_query
class SearchAnalyticsByQueryEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SearchAnalyticsByQuerySearchFilter


class SearchAnalyticsByQueryNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SearchAnalyticsByQuerySearchFilter


class SearchAnalyticsByQueryGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SearchAnalyticsByQuerySearchFilter


class SearchAnalyticsByQueryGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SearchAnalyticsByQuerySearchFilter


class SearchAnalyticsByQueryLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SearchAnalyticsByQuerySearchFilter


class SearchAnalyticsByQueryLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SearchAnalyticsByQuerySearchFilter


class SearchAnalyticsByQueryLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SearchAnalyticsByQueryStringFilter


class SearchAnalyticsByQueryFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SearchAnalyticsByQueryStringFilter


class SearchAnalyticsByQueryKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SearchAnalyticsByQueryStringFilter


class SearchAnalyticsByQueryContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SearchAnalyticsByQueryAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SearchAnalyticsByQueryInCondition = TypedDict("SearchAnalyticsByQueryInCondition", {"in": SearchAnalyticsByQueryInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SearchAnalyticsByQueryNotCondition = TypedDict("SearchAnalyticsByQueryNotCondition", {"not": "SearchAnalyticsByQueryCondition"}, total=False)
"""Negates the nested condition."""

SearchAnalyticsByQueryAndCondition = TypedDict("SearchAnalyticsByQueryAndCondition", {"and": "list[SearchAnalyticsByQueryCondition]"}, total=False)
"""True if all nested conditions are true."""

SearchAnalyticsByQueryOrCondition = TypedDict("SearchAnalyticsByQueryOrCondition", {"or": "list[SearchAnalyticsByQueryCondition]"}, total=False)
"""True if any nested condition is true."""

SearchAnalyticsByQueryAnyCondition = TypedDict("SearchAnalyticsByQueryAnyCondition", {"any": SearchAnalyticsByQueryAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all search_analytics_by_query condition types
SearchAnalyticsByQueryCondition = (
    SearchAnalyticsByQueryEqCondition
    | SearchAnalyticsByQueryNeqCondition
    | SearchAnalyticsByQueryGtCondition
    | SearchAnalyticsByQueryGteCondition
    | SearchAnalyticsByQueryLtCondition
    | SearchAnalyticsByQueryLteCondition
    | SearchAnalyticsByQueryInCondition
    | SearchAnalyticsByQueryLikeCondition
    | SearchAnalyticsByQueryFuzzyCondition
    | SearchAnalyticsByQueryKeywordCondition
    | SearchAnalyticsByQueryContainsCondition
    | SearchAnalyticsByQueryNotCondition
    | SearchAnalyticsByQueryAndCondition
    | SearchAnalyticsByQueryOrCondition
    | SearchAnalyticsByQueryAnyCondition
)


class SearchAnalyticsByQuerySearchQuery(TypedDict, total=False):
    """Search query for search_analytics_by_query entity."""
    filter: SearchAnalyticsByQueryCondition
    sort: list[SearchAnalyticsByQuerySortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
