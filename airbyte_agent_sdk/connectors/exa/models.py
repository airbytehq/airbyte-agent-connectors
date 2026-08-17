"""
Pydantic models for exa connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class ExaAuthConfig(BaseModel):
    """API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Exa API key from dashboard.exa.ai/api-keys"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class SearchRequestContentsSummary(BaseModel):
    """Summary generation options."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    query: str | None = Field(default=None, description="Custom query for the LLM-generated summary.")
    """Custom query for the LLM-generated summary."""

class SearchRequestContents(BaseModel):
    """Options for requesting page contents inline with search results."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    text: Any | None = Field(default=None, description="Text extraction options. Pass true for defaults or an object for advanced options.")
    """Text extraction options. Pass true for defaults or an object for advanced options."""
    highlights: Any | None = Field(default=None, description="Highlight extraction options. Pass true for defaults or an object for advanced options.")
    """Highlight extraction options. Pass true for defaults or an object for advanced options."""
    summary: SearchRequestContentsSummary | None = Field(default=None, description="Summary generation options.")
    """Summary generation options."""

class SearchRequest(BaseModel):
    """SearchRequest type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    query: str
    type_: str | None = Field(default=None, alias="type")
    category: str | None = Field(default=None)
    num_results: int | None = Field(default=None, alias="numResults")
    include_domains: list[str] | None = Field(default=None, alias="includeDomains")
    exclude_domains: list[str] | None = Field(default=None, alias="excludeDomains")
    start_published_date: str | None = Field(default=None, alias="startPublishedDate")
    end_published_date: str | None = Field(default=None, alias="endPublishedDate")
    start_crawl_date: str | None = Field(default=None, alias="startCrawlDate")
    end_crawl_date: str | None = Field(default=None, alias="endCrawlDate")
    contents: SearchRequestContents | None = Field(default=None)
    moderation: bool | None = Field(default=None)

class CostDollarsSearch(BaseModel):
    """Nested schema for CostDollars.search"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    neural: float | None = Field(default=None, description="Cost for neural search.")
    """Cost for neural search."""

class CostDollarsContents(BaseModel):
    """Cost breakdown for contents retrieval."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    text: float | None = Field(default=None, description="Cost for text extraction.")
    """Cost for text extraction."""

class CostDollars(BaseModel):
    """Estimated cost breakdown for the request."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: float | None = Field(default=None)
    search: CostDollarsSearch | None = Field(default=None)
    contents: CostDollarsContents | None = Field(default=None)

class SearchResult(BaseModel):
    """SearchResult type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None = Field(default=None)
    url: str | None = Field(default=None)
    id: str | None = Field(default=None)
    published_date: str | None = Field(default=None, alias="publishedDate")
    author: str | None = Field(default=None)
    image: str | None = Field(default=None)
    favicon: str | None = Field(default=None)
    text: str | None = Field(default=None)
    highlights: list[str] | None = Field(default=None)
    highlight_scores: list[float] | None = Field(default=None, alias="highlightScores")
    summary: str | None = Field(default=None)
    score: float | None = Field(default=None)

class SearchResponse(BaseModel):
    """SearchResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    results: list[SearchResult] | None = Field(default=None)
    resolved_search_type: str | None = Field(default=None, alias="resolvedSearchType")
    search_time: float | None = Field(default=None, alias="searchTime")
    cost_dollars: CostDollars | None = Field(default=None, alias="costDollars")

class ContentsRequestSummary(BaseModel):
    """Summary generation options."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    query: str | None = Field(default=None, description="Custom query for the LLM-generated summary.")
    """Custom query for the LLM-generated summary."""

class ContentsRequest(BaseModel):
    """ContentsRequest type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    urls: list[str]
    text: Any | None = Field(default=None)
    highlights: Any | None = Field(default=None)
    summary: ContentsRequestSummary | None = Field(default=None)

class ContentsResponseStatusesItem(BaseModel):
    """Nested schema for ContentsResponse.statuses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="The URL or document ID that was requested.")
    """The URL or document ID that was requested."""
    status: str | None = Field(default=None, description="Status of the content fetch.")
    """Status of the content fetch."""
    source: str | None = Field(default=None, description="Where the content was sourced from.")
    """Where the content was sourced from."""

class ContentsResponse(BaseModel):
    """ContentsResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    results: list[SearchResult] | None = Field(default=None)
    statuses: list[ContentsResponseStatusesItem] | None = Field(default=None)
    search_time: float | None = Field(default=None, alias="searchTime")
    cost_dollars: CostDollars | None = Field(default=None, alias="costDollars")

class FindSimilarRequestContentsSummary(BaseModel):
    """Summary generation options."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    query: str | None = Field(default=None, description="Custom query for the LLM-generated summary.")
    """Custom query for the LLM-generated summary."""

class FindSimilarRequestContents(BaseModel):
    """Options for requesting page contents inline with similar page results."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    text: Any | None = Field(default=None, description="Text extraction options. Pass true for defaults or an object for advanced options.")
    """Text extraction options. Pass true for defaults or an object for advanced options."""
    highlights: Any | None = Field(default=None, description="Highlight extraction options. Pass true for defaults or an object for advanced options.")
    """Highlight extraction options. Pass true for defaults or an object for advanced options."""
    summary: FindSimilarRequestContentsSummary | None = Field(default=None, description="Summary generation options.")
    """Summary generation options."""

class FindSimilarRequest(BaseModel):
    """FindSimilarRequest type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str
    num_results: int | None = Field(default=None, alias="numResults")
    include_domains: list[str] | None = Field(default=None, alias="includeDomains")
    exclude_domains: list[str] | None = Field(default=None, alias="excludeDomains")
    start_published_date: str | None = Field(default=None, alias="startPublishedDate")
    end_published_date: str | None = Field(default=None, alias="endPublishedDate")
    start_crawl_date: str | None = Field(default=None, alias="startCrawlDate")
    end_crawl_date: str | None = Field(default=None, alias="endCrawlDate")
    contents: FindSimilarRequestContents | None = Field(default=None)

class FindSimilarResponse(BaseModel):
    """FindSimilarResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    results: list[SearchResult] | None = Field(default=None)
    search_time: float | None = Field(default=None, alias="searchTime")
    cost_dollars: CostDollars | None = Field(default=None, alias="costDollars")

class ContentResult(BaseModel):
    """ContentResult type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None = Field(default=None)
    url: str | None = Field(default=None)
    id: str | None = Field(default=None)
    published_date: str | None = Field(default=None, alias="publishedDate")
    author: str | None = Field(default=None)
    image: str | None = Field(default=None)
    favicon: str | None = Field(default=None)
    text: str | None = Field(default=None)
    highlights: list[str] | None = Field(default=None)
    highlight_scores: list[float] | None = Field(default=None, alias="highlightScores")
    summary: str | None = Field(default=None)
    score: float | None = Field(default=None)

class SimilarResult(BaseModel):
    """SimilarResult type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None = Field(default=None)
    url: str | None = Field(default=None)
    id: str | None = Field(default=None)
    published_date: str | None = Field(default=None, alias="publishedDate")
    author: str | None = Field(default=None)
    image: str | None = Field(default=None)
    favicon: str | None = Field(default=None)
    text: str | None = Field(default=None)
    highlights: list[str] | None = Field(default=None)
    highlight_scores: list[float] | None = Field(default=None, alias="highlightScores")
    summary: str | None = Field(default=None)
    score: float | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== CHECK RESULT MODEL =====

class ExaCheckResult(BaseModel):
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


class ExaExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class ExaExecuteResultWithMeta(ExaExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

SearchResultsListResult = ExaExecuteResult[list[SearchResult]]
"""Result type for search_results.list operation."""

ContentsListResult = ExaExecuteResult[list[SearchResult]]
"""Result type for contents.list operation."""

SimilarResultsListResult = ExaExecuteResult[list[SearchResult]]
"""Result type for similar_results.list operation."""

