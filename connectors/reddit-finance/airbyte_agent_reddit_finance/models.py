"""
Pydantic models for reddit-finance connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any


# Authentication configuration - Reddit Finance uses no auth
# but we keep a stub config for consistency with the connector pattern

class RedditFinanceAuthConfig(BaseModel):
    """Authentication configuration for Reddit Finance.

    Reddit's public JSON API requires a User-Agent header but no API key.
    The user_agent is injected as an api_key into the User-Agent header.
    """

    model_config = ConfigDict(extra="forbid")

    user_agent: str = Field(
        default="AirbyteTradingBot/1.0 (by /u/airbyte_connector)",
        description="User-Agent string for Reddit API requests",
    )


# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class SubredditPost(BaseModel):
    """A Reddit post from a finance subreddit."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str = Field(description="Reddit post ID")
    subreddit: Union[str, None] = Field(default=None, description="Subreddit name")
    selftext: Union[str, None] = Field(default=None, description="Post body text")
    author_fullname: Union[str, None] = Field(default=None, description="Author unique ID")
    title: Union[str, None] = Field(default=None, description="Post title")
    subreddit_name_prefixed: Union[str, None] = Field(default=None, description="Subreddit name with r/ prefix")
    name: Union[str, None] = Field(default=None, description="Full name (kind_id) of the post")
    upvote_ratio: Union[float, None] = Field(default=None, description="Ratio of upvotes to total votes")
    ups: Union[int, None] = Field(default=None, description="Number of upvotes")
    score: Union[int, None] = Field(default=None, description="Post score")
    created: Union[float, None] = Field(default=None, description="Post creation timestamp (epoch)")
    created_utc: Union[float, None] = Field(default=None, description="Post creation timestamp UTC (epoch)")
    num_comments: Union[int, None] = Field(default=None, description="Number of comments")
    permalink: Union[str, None] = Field(default=None, description="Permalink to post")
    url: Union[str, None] = Field(default=None, description="URL of the post or linked content")
    is_self: Union[bool, None] = Field(default=None, description="Whether the post is a self-post")
    over_18: Union[bool, None] = Field(default=None, description="Whether the post is marked NSFW")
    author: Union[str, None] = Field(default=None, description="Author username")
    link_flair_text: Union[str, None] = Field(default=None, description="Link flair text")
    domain: Union[str, None] = Field(default=None, description="Domain of linked content")
    saved: Union[bool, None] = Field(default=None, description="Whether the post is saved")
    gilded: Union[int, None] = Field(default=None, description="Number of times gilded")
    clicked: Union[bool, None] = Field(default=None, description="Whether the post was clicked")
    hidden: Union[bool, None] = Field(default=None, description="Whether the post is hidden")
    pinned: Union[bool, None] = Field(default=None, description="Whether the post is pinned")
    stickied: Union[bool, None] = Field(default=None, description="Whether the post is stickied")
    num_crossposts: Union[int, None] = Field(default=None, description="Number of crossposts")
    total_awards_received: Union[int, None] = Field(default=None, description="Total awards received")
    subreddit_subscribers: Union[int, None] = Field(default=None, description="Number of subreddit subscribers")


class SubredditSearchPost(BaseModel):
    """A Reddit search result post from a finance subreddit."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str = Field(description="Reddit post ID")
    subreddit: Union[str, None] = Field(default=None, description="Subreddit name")
    selftext: Union[str, None] = Field(default=None, description="Post body text")
    author_fullname: Union[str, None] = Field(default=None, description="Author unique ID")
    title: Union[str, None] = Field(default=None, description="Post title")
    subreddit_name_prefixed: Union[str, None] = Field(default=None, description="Subreddit name with r/ prefix")
    name: Union[str, None] = Field(default=None, description="Full name (kind_id) of the post")
    upvote_ratio: Union[float, None] = Field(default=None, description="Ratio of upvotes to total votes")
    ups: Union[int, None] = Field(default=None, description="Number of upvotes")
    score: Union[int, None] = Field(default=None, description="Post score")
    created: Union[float, None] = Field(default=None, description="Post creation timestamp (epoch)")
    created_utc: Union[float, None] = Field(default=None, description="Post creation timestamp UTC (epoch)")
    num_comments: Union[int, None] = Field(default=None, description="Number of comments")
    permalink: Union[str, None] = Field(default=None, description="Permalink to post")
    url: Union[str, None] = Field(default=None, description="URL of the post or linked content")
    is_self: Union[bool, None] = Field(default=None, description="Whether the post is a self-post")
    over_18: Union[bool, None] = Field(default=None, description="Whether the post is marked NSFW")
    author: Union[str, None] = Field(default=None, description="Author username")
    link_flair_text: Union[str, None] = Field(default=None, description="Link flair text")
    domain: Union[str, None] = Field(default=None, description="Domain of linked content")


class SubredditInfo(BaseModel):
    """Information about a finance subreddit."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    display_name: str = Field(description="Subreddit display name")
    title: Union[str, None] = Field(default=None, description="Subreddit title")
    display_name_prefixed: Union[str, None] = Field(default=None, description="Subreddit name with r/ prefix")
    public_description: Union[str, None] = Field(default=None, description="Public description text")
    subscribers: Union[int, None] = Field(default=None, description="Number of subscribers")
    accounts_active: Union[int, None] = Field(default=None, description="Number of active accounts")
    created: Union[float, None] = Field(default=None, description="Subreddit creation timestamp (epoch)")
    created_utc: Union[float, None] = Field(default=None, description="Subreddit creation timestamp UTC (epoch)")
    over18: Union[bool, None] = Field(default=None, description="Whether subreddit is NSFW")
    wiki_enabled: Union[bool, None] = Field(default=None, description="Whether wiki is enabled")
    icon_img: Union[str, None] = Field(default=None, description="Subreddit icon image URL")
    header_img: Union[str, None] = Field(default=None, description="Subreddit header image URL")
    primary_color: Union[str, None] = Field(default=None, description="Primary theme color")
    key_color: Union[str, None] = Field(default=None, description="Key theme color")
    url: Union[str, None] = Field(default=None, description="Subreddit URL path")
    subreddit_type: Union[str, None] = Field(default=None, description="Subreddit type (public, private, etc.)")
    lang: Union[str, None] = Field(default=None, description="Subreddit language")
    allow_galleries: Union[bool, None] = Field(default=None, description="Whether galleries are allowed")
    restrict_posting: Union[bool, None] = Field(default=None, description="Whether posting is restricted")


# ===== RESPONSE ENVELOPE MODELS =====

T = TypeVar('T')
S = TypeVar('S')


class RedditFinanceCheckResult(BaseModel):
    """Result of a health check."""
    model_config = ConfigDict(extra="forbid")

    status: str = "unhealthy"
    error: str | None = None
    checked_entity: str | None = None
    checked_action: str | None = None


class RedditFinanceExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only."""
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class RedditFinanceExecuteResultWithMeta(RedditFinanceExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata."""
    meta: S
    """Metadata about the response."""


# ===== OPERATION RESULT TYPE ALIASES =====

class SubredditPostsListResultMeta(BaseModel):
    """Metadata for subreddit_posts.list result."""
    model_config = ConfigDict(extra="allow")


class SubredditSearchListResultMeta(BaseModel):
    """Metadata for subreddit_search.list result."""
    model_config = ConfigDict(extra="allow")


SubredditPostsListResult = RedditFinanceExecuteResultWithMeta[list[SubredditPost], SubredditPostsListResultMeta]
SubredditSearchListResult = RedditFinanceExecuteResultWithMeta[list[SubredditSearchPost], SubredditSearchListResultMeta]
