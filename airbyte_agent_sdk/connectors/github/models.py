"""
Pydantic models for github connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration - multiple options available

class GithubOauth2AuthConfig(BaseModel):
    """OAuth 2"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """OAuth 2.0 access token"""

class GithubPersonalAccessTokenAuthConfig(BaseModel):
    """Personal Access Token"""

    model_config = ConfigDict(extra="forbid")

    token: str
    """GitHub personal access token (fine-grained or classic)"""

GithubAuthConfig = GithubOauth2AuthConfig | GithubPersonalAccessTokenAuthConfig

# Replication configuration

class GithubReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from GitHub."""

    model_config = ConfigDict(extra="forbid")

    repositories: str
    """List of GitHub organizations/repositories, e.g. `airbytehq/airbyte` for single repository, `airbytehq/*` for all repositories from organization"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class IssueCreateParams(BaseModel):
    """IssueCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: Union[str, Any] = Field(default=None)
    body: Union[str, Any] = Field(default=None)
    labels: Union[list[str], Any] = Field(default=None)
    assignees: Union[list[str], Any] = Field(default=None)
    milestone: Union[int | None, Any] = Field(default=None)

class IssueResponseLabelsItem(BaseModel):
    """Nested schema for IssueResponse.labels_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    color: Union[str, Any] = Field(default=None)
    default: Union[bool, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)

class IssueResponseAssignee(BaseModel):
    """Primary user assigned to this issue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: Union[str, Any] = Field(default=None)
    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    avatar_url: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    html_url: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    site_admin: Union[bool, Any] = Field(default=None)

class IssueResponseSubIssuesSummary(BaseModel):
    """Summary of sub-issues"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: Union[int, Any] = Field(default=None)
    completed: Union[int, Any] = Field(default=None)
    percent_completed: Union[int, Any] = Field(default=None)

class IssueResponseAssigneesItem(BaseModel):
    """Nested schema for IssueResponse.assignees_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: Union[str, Any] = Field(default=None)
    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    avatar_url: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    html_url: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    site_admin: Union[bool, Any] = Field(default=None)

class IssueResponseUser(BaseModel):
    """The user who created the issue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: Union[str, Any] = Field(default=None)
    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    avatar_url: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    html_url: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    site_admin: Union[bool, Any] = Field(default=None)

class IssueResponseIssueDependenciesSummary(BaseModel):
    """Summary of issue dependencies"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    blocked_by: Union[int, Any] = Field(default=None)
    blocking: Union[int, Any] = Field(default=None)
    total_blocked_by: Union[int, Any] = Field(default=None)
    total_blocking: Union[int, Any] = Field(default=None)

class IssueResponseReactions(BaseModel):
    """Reaction counts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: Union[str, Any] = Field(default=None)
    total_count: Union[int, Any] = Field(default=None)
    field_1: Union[int, Any] = Field(default=None, alias="+1")
    field_1: Union[int, Any] = Field(default=None, alias="-1")
    laugh: Union[int, Any] = Field(default=None)
    hooray: Union[int, Any] = Field(default=None)
    confused: Union[int, Any] = Field(default=None)
    heart: Union[int, Any] = Field(default=None)
    rocket: Union[int, Any] = Field(default=None)
    eyes: Union[int, Any] = Field(default=None)

class IssueResponse(BaseModel):
    """IssueResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    repository_url: Union[str, Any] = Field(default=None)
    labels_url: Union[str, Any] = Field(default=None)
    comments_url: Union[str, Any] = Field(default=None)
    events_url: Union[str, Any] = Field(default=None)
    html_url: Union[str, Any] = Field(default=None)
    number: Union[int, Any] = Field(default=None)
    state: Union[str, Any] = Field(default=None)
    state_reason: Union[str | None, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    body: Union[str | None, Any] = Field(default=None)
    user: Union[IssueResponseUser | None, Any] = Field(default=None)
    labels: Union[list[IssueResponseLabelsItem], Any] = Field(default=None)
    assignees: Union[list[IssueResponseAssigneesItem], Any] = Field(default=None)
    milestone: Union[dict[str, Any] | None, Any] = Field(default=None)
    locked: Union[bool, Any] = Field(default=None)
    comments: Union[int, Any] = Field(default=None)
    closed_at: Union[str | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    author_association: Union[str, Any] = Field(default=None)
    active_lock_reason: Union[str | None, Any] = Field(default=None)
    closed_by: Union[dict[str, Any] | None, Any] = Field(default=None)
    timeline_url: Union[str, Any] = Field(default=None)
    performed_via_github_app: Union[dict[str, Any] | None, Any] = Field(default=None)
    assignee: Union[IssueResponseAssignee | None, Any] = Field(default=None)
    reactions: Union[IssueResponseReactions, Any] = Field(default=None)
    sub_issues_summary: Union[IssueResponseSubIssuesSummary, Any] = Field(default=None)
    type_: Union[dict[str, Any] | None, Any] = Field(default=None, alias="type")
    pinned_comment: Union[dict[str, Any] | None, Any] = Field(default=None)
    issue_field_values: Union[list[dict[str, Any]], Any] = Field(default=None)
    issue_dependencies_summary: Union[IssueResponseIssueDependenciesSummary, Any] = Field(default=None)

class IssueUpdateParams(BaseModel):
    """IssueUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: Union[str, Any] = Field(default=None)
    body: Union[str, Any] = Field(default=None)
    state: Union[str, Any] = Field(default=None)
    state_reason: Union[str | None, Any] = Field(default=None)
    labels: Union[list[str], Any] = Field(default=None)
    assignees: Union[list[str], Any] = Field(default=None)
    milestone: Union[int | None, Any] = Field(default=None)

class CommentCreateParams(BaseModel):
    """CommentCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: Union[str, Any] = Field(default=None)

class CommentResponseReactions(BaseModel):
    """Reaction counts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: Union[str, Any] = Field(default=None)
    total_count: Union[int, Any] = Field(default=None)
    field_1: Union[int, Any] = Field(default=None, alias="+1")
    field_1: Union[int, Any] = Field(default=None, alias="-1")
    laugh: Union[int, Any] = Field(default=None)
    hooray: Union[int, Any] = Field(default=None)
    confused: Union[int, Any] = Field(default=None)
    heart: Union[int, Any] = Field(default=None)
    rocket: Union[int, Any] = Field(default=None)
    eyes: Union[int, Any] = Field(default=None)

class CommentResponseUser(BaseModel):
    """The user who created the comment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: Union[str, Any] = Field(default=None)
    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    avatar_url: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    html_url: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    site_admin: Union[bool, Any] = Field(default=None)

class CommentResponse(BaseModel):
    """CommentResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    html_url: Union[str, Any] = Field(default=None)
    body: Union[str, Any] = Field(default=None)
    user: Union[CommentResponseUser | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    issue_url: Union[str, Any] = Field(default=None)
    author_association: Union[str, Any] = Field(default=None)
    performed_via_github_app: Union[dict[str, Any] | None, Any] = Field(default=None)
    reactions: Union[CommentResponseReactions, Any] = Field(default=None)

class PullRequestCreateParams(BaseModel):
    """PullRequestCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: Union[str, Any] = Field(default=None)
    head: Union[str, Any] = Field(default=None)
    base: Union[str, Any] = Field(default=None)
    body: Union[str, Any] = Field(default=None)
    draft: Union[bool, Any] = Field(default=None)
    maintainer_can_modify: Union[bool, Any] = Field(default=None)

class PullRequestResponseLabelsItem(BaseModel):
    """Nested schema for PullRequestResponse.labels_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    color: Union[str, Any] = Field(default=None)
    default: Union[bool, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)

class PullRequestResponseHead(BaseModel):
    """The head branch"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: Union[str, Any] = Field(default=None)
    ref: Union[str, Any] = Field(default=None)
    sha: Union[str, Any] = Field(default=None)

class PullRequestResponseUser(BaseModel):
    """The user who created the pull request"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: Union[str, Any] = Field(default=None)
    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    avatar_url: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    html_url: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    site_admin: Union[bool, Any] = Field(default=None)

class PullRequestResponseAssigneesItem(BaseModel):
    """Nested schema for PullRequestResponse.assignees_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: Union[str, Any] = Field(default=None)
    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    avatar_url: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    html_url: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    site_admin: Union[bool, Any] = Field(default=None)

class PullRequestResponseBase(BaseModel):
    """The base branch"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: Union[str, Any] = Field(default=None)
    ref: Union[str, Any] = Field(default=None)
    sha: Union[str, Any] = Field(default=None)

class PullRequestResponse(BaseModel):
    """PullRequestResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    html_url: Union[str, Any] = Field(default=None)
    diff_url: Union[str, Any] = Field(default=None)
    patch_url: Union[str, Any] = Field(default=None)
    number: Union[int, Any] = Field(default=None)
    state: Union[str, Any] = Field(default=None)
    locked: Union[bool, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    body: Union[str | None, Any] = Field(default=None)
    user: Union[PullRequestResponseUser | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    closed_at: Union[str | None, Any] = Field(default=None)
    merged_at: Union[str | None, Any] = Field(default=None)
    merge_commit_sha: Union[str | None, Any] = Field(default=None)
    draft: Union[bool, Any] = Field(default=None)
    head: Union[PullRequestResponseHead, Any] = Field(default=None)
    base: Union[PullRequestResponseBase, Any] = Field(default=None)
    author_association: Union[str, Any] = Field(default=None)
    labels: Union[list[PullRequestResponseLabelsItem], Any] = Field(default=None)
    milestone: Union[dict[str, Any] | None, Any] = Field(default=None)
    assignees: Union[list[PullRequestResponseAssigneesItem], Any] = Field(default=None)
    requested_reviewers: Union[list[dict[str, Any]], Any] = Field(default=None)
    comments: Union[int, Any] = Field(default=None)
    review_comments: Union[int, Any] = Field(default=None)
    commits: Union[int, Any] = Field(default=None)
    additions: Union[int, Any] = Field(default=None)
    deletions: Union[int, Any] = Field(default=None)
    changed_files: Union[int, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class RepositoriesListResultMeta(BaseModel):
    """Metadata for repositories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class RepositoriesApiSearchResultMeta(BaseModel):
    """Metadata for repositories.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)
    total_count: Union[int, Any] = Field(default=None)

class OrgRepositoriesListResultMeta(BaseModel):
    """Metadata for org_repositories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class BranchesListResultMeta(BaseModel):
    """Metadata for branches.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class CommitsListResultMeta(BaseModel):
    """Metadata for commits.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class ReleasesListResultMeta(BaseModel):
    """Metadata for releases.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class IssuesListResultMeta(BaseModel):
    """Metadata for issues.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class IssuesApiSearchResultMeta(BaseModel):
    """Metadata for issues.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)
    total_count: Union[int, Any] = Field(default=None)

class PullRequestsListResultMeta(BaseModel):
    """Metadata for pull_requests.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class PullRequestsApiSearchResultMeta(BaseModel):
    """Metadata for pull_requests.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)
    total_count: Union[int, Any] = Field(default=None)

class ReviewsListResultMeta(BaseModel):
    """Metadata for reviews.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class CommentsListResultMeta(BaseModel):
    """Metadata for comments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class PrCommentsListResultMeta(BaseModel):
    """Metadata for pr_comments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class LabelsListResultMeta(BaseModel):
    """Metadata for labels.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class MilestonesListResultMeta(BaseModel):
    """Metadata for milestones.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class OrganizationsListResultMeta(BaseModel):
    """Metadata for organizations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class UsersApiSearchResultMeta(BaseModel):
    """Metadata for users.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)
    total_count: Union[int, Any] = Field(default=None)

class TeamsListResultMeta(BaseModel):
    """Metadata for teams.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class TagsListResultMeta(BaseModel):
    """Metadata for tags.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class StargazersListResultMeta(BaseModel):
    """Metadata for stargazers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str, Any] = Field(default=None)

class ViewerRepositoriesListResultMeta(BaseModel):
    """Metadata for viewer_repositories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class ProjectsListResultMeta(BaseModel):
    """Metadata for projects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class ProjectItemsListResultMeta(BaseModel):
    """Metadata for project_items.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class DiscussionsListResultMeta(BaseModel):
    """Metadata for discussions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)

class DiscussionsApiSearchResultMeta(BaseModel):
    """Metadata for discussions.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: Union[bool, Any] = Field(default=None)
    end_cursor: Union[str | None, Any] = Field(default=None)
    total_count: Union[int, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class GithubCheckResult(BaseModel):
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


class GithubExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class GithubExecuteResultWithMeta(GithubExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class BranchesSearchData(BaseModel):
    """Search result data for branches entity."""
    model_config = ConfigDict(extra="allow")

    name: str | None = None
    """Branch name (e.g. `main`, `feature/foo`)"""
    prefix: str | None = None
    """Git ref prefix for the branch (typically `refs/heads/`)"""


class CommentsSearchData(BaseModel):
    """Search result data for comments entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """GraphQL node ID of the comment"""
    database_id: int | None = None
    """REST API numeric identifier for the comment"""
    body: str | None = None
    """Markdown body of the comment"""
    created_at: str | None = None
    """ISO 8601 timestamp when the comment was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the comment was last updated"""
    url: str | None = None
    """Permalink to the comment on GitHub"""
    is_minimized: bool | None = None
    """Whether the comment has been hidden/collapsed"""


class IssuesSearchData(BaseModel):
    """Search result data for issues entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """GraphQL node ID of the issue"""
    database_id: int | None = None
    """REST API numeric identifier for the issue"""
    number: int | None = None
    """Repository-scoped issue number"""
    title: str | None = None
    """Issue title"""
    state: str | None = None
    """Issue state: `OPEN` or `CLOSED`"""
    state_reason: str | None = None
    """Reason the issue is in its current state (e.g. `COMPLETED`, `NOT_PLANNED`)"""
    created_at: str | None = None
    """ISO 8601 timestamp when the issue was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the issue was last updated"""
    closed_at: str | None = None
    """ISO 8601 timestamp when the issue was closed, if applicable"""
    locked: bool | None = None
    """Whether the conversation on the issue is locked"""
    url: str | None = None
    """Permalink to the issue on GitHub"""


class OrganizationsSearchData(BaseModel):
    """Search result data for organizations entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """GraphQL node ID of the organization"""
    database_id: int | None = None
    """REST API numeric identifier for the organization"""
    login: str | None = None
    """Organization login/handle (unique URL slug)"""
    name: str | None = None
    """Display name of the organization"""
    description: str | None = None
    """Short public description of the organization"""
    email: str | None = None
    """Public contact email for the organization, if set"""
    location: str | None = None
    """Public location of the organization, if set"""
    is_verified: bool | None = None
    """Whether the organization has a verified domain"""
    created_at: str | None = None
    """ISO 8601 timestamp when the organization was created"""


class PullRequestsSearchData(BaseModel):
    """Search result data for pull_requests entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """GraphQL node ID of the pull request"""
    database_id: int | None = None
    """REST API numeric identifier for the pull request"""
    number: int | None = None
    """Repository-scoped pull request number"""
    title: str | None = None
    """Pull request title"""
    state: str | None = None
    """Pull request state: `OPEN`, `CLOSED`, or `MERGED`"""
    is_draft: bool | None = None
    """Whether the pull request is still a draft"""
    merged: bool | None = None
    """Whether the pull request has been merged"""
    created_at: str | None = None
    """ISO 8601 timestamp when the pull request was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the pull request was last updated"""
    closed_at: str | None = None
    """ISO 8601 timestamp when the pull request was closed, if applicable"""
    merged_at: str | None = None
    """ISO 8601 timestamp when the pull request was merged, if applicable"""
    base_ref_name: str | None = None
    """Name of the branch being merged into"""
    head_ref_name: str | None = None
    """Name of the branch with the proposed changes"""
    url: str | None = None
    """Permalink to the pull request on GitHub"""


class RepositoriesSearchData(BaseModel):
    """Search result data for repositories entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """GraphQL node ID of the repository"""
    name: str | None = None
    """Short repository name (without owner)"""
    name_with_owner: str | None = None
    """Fully-qualified `owner/name` identifier for the repository"""
    description: str | None = None
    """Short description of the repository"""
    url: str | None = None
    """Canonical GitHub URL for the repository"""
    created_at: str | None = None
    """ISO 8601 timestamp when the repository was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the repository was last updated"""
    pushed_at: str | None = None
    """ISO 8601 timestamp of the most recent push to the repository"""
    fork_count: int | None = None
    """Number of forks of the repository"""
    stargazer_count: int | None = None
    """Number of users who have starred the repository"""
    is_private: bool | None = None
    """Whether the repository is private"""
    is_fork: bool | None = None
    """Whether the repository is a fork of another repository"""
    is_archived: bool | None = None
    """Whether the repository has been archived"""


class StargazersSearchData(BaseModel):
    """Search result data for stargazers entity."""
    model_config = ConfigDict(extra="allow")

    starred_at: str | None = None
    """ISO 8601 timestamp when the user starred the repository"""


class TagsSearchData(BaseModel):
    """Search result data for tags entity."""
    model_config = ConfigDict(extra="allow")

    name: str | None = None
    """Tag name (e.g. `v1.2.3`)"""
    prefix: str | None = None
    """Git ref prefix for the tag (typically `refs/tags/`)"""


class TeamsSearchData(BaseModel):
    """Search result data for teams entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """GraphQL node ID of the team"""
    database_id: int | None = None
    """REST API numeric identifier for the team"""
    slug: str | None = None
    """URL-friendly slug for the team within its organization"""
    name: str | None = None
    """Display name of the team"""
    description: str | None = None
    """Short description of the team"""
    privacy: str | None = None
    """Team visibility: `SECRET` or `VISIBLE`"""
    url: str | None = None
    """Permalink to the team on GitHub"""
    created_at: str | None = None
    """ISO 8601 timestamp when the team was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the team was last updated"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """GraphQL node ID of the user"""
    database_id: int | None = None
    """REST API numeric identifier for the user"""
    login: str | None = None
    """User login/handle"""
    name: str | None = None
    """Public display name of the user, if set"""
    email: str | None = None
    """Public email address of the user, if set"""
    company: str | None = None
    """Public company affiliation of the user, if set"""
    location: str | None = None
    """Public location of the user, if set"""
    twitter_username: str | None = None
    """Public Twitter/X username of the user, if set"""
    url: str | None = None
    """Permalink to the user's profile on GitHub"""
    created_at: str | None = None
    """ISO 8601 timestamp when the user account was created"""
    is_hireable: bool | None = None
    """Whether the user has marked themselves as available for hire"""


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

BranchesSearchResult = AirbyteSearchResult[BranchesSearchData]
"""Search result type for branches entity."""

CommentsSearchResult = AirbyteSearchResult[CommentsSearchData]
"""Search result type for comments entity."""

IssuesSearchResult = AirbyteSearchResult[IssuesSearchData]
"""Search result type for issues entity."""

OrganizationsSearchResult = AirbyteSearchResult[OrganizationsSearchData]
"""Search result type for organizations entity."""

PullRequestsSearchResult = AirbyteSearchResult[PullRequestsSearchData]
"""Search result type for pull_requests entity."""

RepositoriesSearchResult = AirbyteSearchResult[RepositoriesSearchData]
"""Search result type for repositories entity."""

StargazersSearchResult = AirbyteSearchResult[StargazersSearchData]
"""Search result type for stargazers entity."""

TagsSearchResult = AirbyteSearchResult[TagsSearchData]
"""Search result type for tags entity."""

TeamsSearchResult = AirbyteSearchResult[TeamsSearchData]
"""Search result type for teams entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

RepositoriesListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], RepositoriesListResultMeta]
"""Result type for repositories.list operation with data and metadata."""

RepositoriesApiSearchResult = GithubExecuteResultWithMeta[list[dict[str, Any]], RepositoriesApiSearchResultMeta]
"""Result type for repositories.api_search operation with data and metadata."""

OrgRepositoriesListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], OrgRepositoriesListResultMeta]
"""Result type for org_repositories.list operation with data and metadata."""

BranchesListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], BranchesListResultMeta]
"""Result type for branches.list operation with data and metadata."""

CommitsListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], CommitsListResultMeta]
"""Result type for commits.list operation with data and metadata."""

ReleasesListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], ReleasesListResultMeta]
"""Result type for releases.list operation with data and metadata."""

IssuesListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], IssuesListResultMeta]
"""Result type for issues.list operation with data and metadata."""

IssuesApiSearchResult = GithubExecuteResultWithMeta[list[dict[str, Any]], IssuesApiSearchResultMeta]
"""Result type for issues.api_search operation with data and metadata."""

PullRequestsListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], PullRequestsListResultMeta]
"""Result type for pull_requests.list operation with data and metadata."""

PullRequestsApiSearchResult = GithubExecuteResultWithMeta[list[dict[str, Any]], PullRequestsApiSearchResultMeta]
"""Result type for pull_requests.api_search operation with data and metadata."""

ReviewsListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], ReviewsListResultMeta]
"""Result type for reviews.list operation with data and metadata."""

CommentsListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], CommentsListResultMeta]
"""Result type for comments.list operation with data and metadata."""

PrCommentsListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], PrCommentsListResultMeta]
"""Result type for pr_comments.list operation with data and metadata."""

LabelsListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], LabelsListResultMeta]
"""Result type for labels.list operation with data and metadata."""

MilestonesListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], MilestonesListResultMeta]
"""Result type for milestones.list operation with data and metadata."""

OrganizationsListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], OrganizationsListResultMeta]
"""Result type for organizations.list operation with data and metadata."""

UsersListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

UsersApiSearchResult = GithubExecuteResultWithMeta[list[dict[str, Any]], UsersApiSearchResultMeta]
"""Result type for users.api_search operation with data and metadata."""

TeamsListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], TeamsListResultMeta]
"""Result type for teams.list operation with data and metadata."""

TagsListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], TagsListResultMeta]
"""Result type for tags.list operation with data and metadata."""

StargazersListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], StargazersListResultMeta]
"""Result type for stargazers.list operation with data and metadata."""

ViewerRepositoriesListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], ViewerRepositoriesListResultMeta]
"""Result type for viewer_repositories.list operation with data and metadata."""

ProjectsListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], ProjectsListResultMeta]
"""Result type for projects.list operation with data and metadata."""

ProjectItemsListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], ProjectItemsListResultMeta]
"""Result type for project_items.list operation with data and metadata."""

DiscussionsListResult = GithubExecuteResultWithMeta[list[dict[str, Any]], DiscussionsListResultMeta]
"""Result type for discussions.list operation with data and metadata."""

DiscussionsApiSearchResult = GithubExecuteResultWithMeta[list[dict[str, Any]], DiscussionsApiSearchResultMeta]
"""Result type for discussions.api_search operation with data and metadata."""

DirectoryContentListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for directory_content.list operation."""

