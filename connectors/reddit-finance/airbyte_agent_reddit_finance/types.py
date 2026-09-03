"""
Type definitions for reddit-finance connector.
"""
from __future__ import annotations

try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]


# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class SubredditPostsListParams(TypedDict):
    """Parameters for subreddit_posts.list operation"""
    subreddit: str
    sort: str
    limit: NotRequired[int]
    after: NotRequired[str]
    raw_json: NotRequired[str]


class SubredditSearchListParams(TypedDict):
    """Parameters for subreddit_search.list operation"""
    subreddit: str
    q: str
    restrict_sr: NotRequired[str]
    sort: NotRequired[str]
    limit: NotRequired[int]
    after: NotRequired[str]
    raw_json: NotRequired[str]


class SubredditInfoGetParams(TypedDict):
    """Parameters for subreddit_info.get operation"""
    subreddit: str
