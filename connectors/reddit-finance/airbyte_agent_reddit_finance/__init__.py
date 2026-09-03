"""
Airbyte Agent Connector for Reddit Finance.

Provides access to finance-related subreddit posts, search results,
and subreddit information from Reddit.
"""

from .connector import RedditFinanceConnector
from .models import (
    RedditFinanceAuthConfig,
    RedditFinanceCheckResult,
    RedditFinanceExecuteResult,
    RedditFinanceExecuteResultWithMeta,
    SubredditPost,
    SubredditSearchPost,
    SubredditInfo,
    SubredditPostsListResult,
    SubredditSearchListResult,
)
from .types import (
    SubredditPostsListParams,
    SubredditSearchListParams,
    SubredditInfoGetParams,
)
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig

__all__ = [
    "RedditFinanceConnector",
    "AirbyteAuthConfig",
    "RedditFinanceAuthConfig",
    "RedditFinanceCheckResult",
    "RedditFinanceExecuteResult",
    "RedditFinanceExecuteResultWithMeta",
    "SubredditPost",
    "SubredditSearchPost",
    "SubredditInfo",
    "SubredditPostsListResult",
    "SubredditSearchListResult",
    "SubredditPostsListParams",
    "SubredditSearchListParams",
    "SubredditInfoGetParams",
]
