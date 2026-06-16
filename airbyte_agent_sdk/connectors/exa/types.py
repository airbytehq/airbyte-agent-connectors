"""
Type definitions for exa connector.
"""
from __future__ import annotations

from airbyte_agent_sdk.types import AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

class SearchResultsListParamsContentsSummary(TypedDict):
    """Summary generation options."""
    query: NotRequired[str]

class SearchResultsListParamsContents(TypedDict):
    """Options for requesting page contents inline with search results."""
    text: NotRequired[Any]
    highlights: NotRequired[Any]
    summary: NotRequired[SearchResultsListParamsContentsSummary]

class ContentsListParamsSummary(TypedDict):
    """Summary generation options."""
    query: NotRequired[str]

class SimilarResultsListParamsContentsSummary(TypedDict):
    """Summary generation options."""
    query: NotRequired[str]

class SimilarResultsListParamsContents(TypedDict):
    """Options for requesting page contents inline with similar page results."""
    text: NotRequired[Any]
    highlights: NotRequired[Any]
    summary: NotRequired[SimilarResultsListParamsContentsSummary]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class SearchResultsListParams(TypedDict):
    """Parameters for search_results.list operation"""
    query: str
    type: NotRequired[str]
    category: NotRequired[str]
    num_results: NotRequired[int]
    include_domains: NotRequired[list[str]]
    exclude_domains: NotRequired[list[str]]
    start_published_date: NotRequired[str]
    end_published_date: NotRequired[str]
    start_crawl_date: NotRequired[str]
    end_crawl_date: NotRequired[str]
    contents: NotRequired[SearchResultsListParamsContents]
    moderation: NotRequired[bool]

class ContentsListParams(TypedDict):
    """Parameters for contents.list operation"""
    urls: list[str]
    text: NotRequired[Any]
    highlights: NotRequired[Any]
    summary: NotRequired[ContentsListParamsSummary]

class SimilarResultsListParams(TypedDict):
    """Parameters for similar_results.list operation"""
    url: str
    num_results: NotRequired[int]
    include_domains: NotRequired[list[str]]
    exclude_domains: NotRequired[list[str]]
    start_published_date: NotRequired[str]
    end_published_date: NotRequired[str]
    start_crawl_date: NotRequired[str]
    end_crawl_date: NotRequired[str]
    contents: NotRequired[SimilarResultsListParamsContents]

