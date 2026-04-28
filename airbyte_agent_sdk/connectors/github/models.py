"""
Pydantic models for github connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

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

    title: str
    body: str | None = Field(default=None)
    labels: list[str] | None = Field(default=None)
    assignees: list[str] | None = Field(default=None)
    milestone: int | None = Field(default=None)

class IssueResponseAssigneesItem(BaseModel):
    """Nested schema for IssueResponse.assignees_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: str | None = Field(default=None)
    id: int | None = Field(default=None)
    node_id: str | None = Field(default=None)
    avatar_url: str | None = Field(default=None)
    url: str | None = Field(default=None)
    html_url: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    site_admin: bool | None = Field(default=None)

class IssueResponseLabelsItem(BaseModel):
    """Nested schema for IssueResponse.labels_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    node_id: str | None = Field(default=None)
    url: str | None = Field(default=None)
    name: str | None = Field(default=None)
    color: str | None = Field(default=None)
    default: bool | None = Field(default=None)
    description: str | None | None = Field(default=None)

class IssueResponseAssignee(BaseModel):
    """Primary user assigned to this issue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: str | None = Field(default=None)
    id: int | None = Field(default=None)
    node_id: str | None = Field(default=None)
    avatar_url: str | None = Field(default=None)
    url: str | None = Field(default=None)
    html_url: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    site_admin: bool | None = Field(default=None)

class IssueResponseReactions(BaseModel):
    """Reaction counts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)
    total_count: int | None = Field(default=None)
    field_1: int | None = Field(default=None, alias="+1")
    field_1: int | None = Field(default=None, alias="-1")
    laugh: int | None = Field(default=None)
    hooray: int | None = Field(default=None)
    confused: int | None = Field(default=None)
    heart: int | None = Field(default=None)
    rocket: int | None = Field(default=None)
    eyes: int | None = Field(default=None)

class IssueResponseIssueDependenciesSummary(BaseModel):
    """Summary of issue dependencies"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    blocked_by: int | None = Field(default=None)
    blocking: int | None = Field(default=None)
    total_blocked_by: int | None = Field(default=None)
    total_blocking: int | None = Field(default=None)

class IssueResponseSubIssuesSummary(BaseModel):
    """Summary of sub-issues"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total: int | None = Field(default=None)
    completed: int | None = Field(default=None)
    percent_completed: int | None = Field(default=None)

class IssueResponseUser(BaseModel):
    """The user who created the issue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: str | None = Field(default=None)
    id: int | None = Field(default=None)
    node_id: str | None = Field(default=None)
    avatar_url: str | None = Field(default=None)
    url: str | None = Field(default=None)
    html_url: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    site_admin: bool | None = Field(default=None)

class IssueResponse(BaseModel):
    """IssueResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    node_id: str | None = Field(default=None)
    url: str | None = Field(default=None)
    repository_url: str | None = Field(default=None)
    labels_url: str | None = Field(default=None)
    comments_url: str | None = Field(default=None)
    events_url: str | None = Field(default=None)
    html_url: str | None = Field(default=None)
    number: int | None = Field(default=None)
    state: str | None = Field(default=None)
    state_reason: str | None = Field(default=None)
    title: str | None = Field(default=None)
    body: str | None = Field(default=None)
    user: IssueResponseUser | None = Field(default=None)
    labels: list[IssueResponseLabelsItem] | None = Field(default=None)
    assignees: list[IssueResponseAssigneesItem] | None = Field(default=None)
    milestone: dict[str, Any] | None = Field(default=None)
    locked: bool | None = Field(default=None)
    comments: int | None = Field(default=None)
    closed_at: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    author_association: str | None = Field(default=None)
    active_lock_reason: str | None = Field(default=None)
    closed_by: dict[str, Any] | None = Field(default=None)
    timeline_url: str | None = Field(default=None)
    performed_via_github_app: dict[str, Any] | None = Field(default=None)
    assignee: IssueResponseAssignee | None = Field(default=None)
    reactions: IssueResponseReactions | None = Field(default=None)
    sub_issues_summary: IssueResponseSubIssuesSummary | None = Field(default=None)
    type_: dict[str, Any] | None = Field(default=None, alias="type")
    pinned_comment: dict[str, Any] | None = Field(default=None)
    issue_field_values: list[dict[str, Any]] | None = Field(default=None)
    issue_dependencies_summary: IssueResponseIssueDependenciesSummary | None = Field(default=None)

class IssueUpdateParams(BaseModel):
    """IssueUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None = Field(default=None)
    body: str | None = Field(default=None)
    state: str | None = Field(default=None)
    state_reason: str | None = Field(default=None)
    labels: list[str] | None = Field(default=None)
    assignees: list[str] | None = Field(default=None)
    milestone: int | None = Field(default=None)

class CommentCreateParams(BaseModel):
    """CommentCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: str

class CommentResponseReactions(BaseModel):
    """Reaction counts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)
    total_count: int | None = Field(default=None)
    field_1: int | None = Field(default=None, alias="+1")
    field_1: int | None = Field(default=None, alias="-1")
    laugh: int | None = Field(default=None)
    hooray: int | None = Field(default=None)
    confused: int | None = Field(default=None)
    heart: int | None = Field(default=None)
    rocket: int | None = Field(default=None)
    eyes: int | None = Field(default=None)

class CommentResponseUser(BaseModel):
    """The user who created the comment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: str | None = Field(default=None)
    id: int | None = Field(default=None)
    node_id: str | None = Field(default=None)
    avatar_url: str | None = Field(default=None)
    url: str | None = Field(default=None)
    html_url: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    site_admin: bool | None = Field(default=None)

class CommentResponse(BaseModel):
    """CommentResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    node_id: str | None = Field(default=None)
    url: str | None = Field(default=None)
    html_url: str | None = Field(default=None)
    body: str | None = Field(default=None)
    user: CommentResponseUser | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    issue_url: str | None = Field(default=None)
    author_association: str | None = Field(default=None)
    performed_via_github_app: dict[str, Any] | None = Field(default=None)
    reactions: CommentResponseReactions | None = Field(default=None)

class PullRequestCreateParams(BaseModel):
    """PullRequestCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str
    head: str
    base: str
    body: str | None = Field(default=None)
    draft: bool | None = Field(default=None)
    maintainer_can_modify: bool | None = Field(default=None)

class PullRequestResponseBase(BaseModel):
    """The base branch"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str | None = Field(default=None)
    ref: str | None = Field(default=None)
    sha: str | None = Field(default=None)

class PullRequestResponseLabelsItem(BaseModel):
    """Nested schema for PullRequestResponse.labels_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    node_id: str | None = Field(default=None)
    url: str | None = Field(default=None)
    name: str | None = Field(default=None)
    color: str | None = Field(default=None)
    default: bool | None = Field(default=None)
    description: str | None | None = Field(default=None)

class PullRequestResponseUser(BaseModel):
    """The user who created the pull request"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: str | None = Field(default=None)
    id: int | None = Field(default=None)
    node_id: str | None = Field(default=None)
    avatar_url: str | None = Field(default=None)
    url: str | None = Field(default=None)
    html_url: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    site_admin: bool | None = Field(default=None)

class PullRequestResponseAssigneesItem(BaseModel):
    """Nested schema for PullRequestResponse.assignees_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: str | None = Field(default=None)
    id: int | None = Field(default=None)
    node_id: str | None = Field(default=None)
    avatar_url: str | None = Field(default=None)
    url: str | None = Field(default=None)
    html_url: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    site_admin: bool | None = Field(default=None)

class PullRequestResponseHead(BaseModel):
    """The head branch"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str | None = Field(default=None)
    ref: str | None = Field(default=None)
    sha: str | None = Field(default=None)

class PullRequestResponse(BaseModel):
    """PullRequestResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    node_id: str | None = Field(default=None)
    url: str | None = Field(default=None)
    html_url: str | None = Field(default=None)
    diff_url: str | None = Field(default=None)
    patch_url: str | None = Field(default=None)
    number: int | None = Field(default=None)
    state: str | None = Field(default=None)
    locked: bool | None = Field(default=None)
    title: str | None = Field(default=None)
    body: str | None = Field(default=None)
    user: PullRequestResponseUser | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    closed_at: str | None = Field(default=None)
    merged_at: str | None = Field(default=None)
    merge_commit_sha: str | None = Field(default=None)
    draft: bool | None = Field(default=None)
    head: PullRequestResponseHead | None = Field(default=None)
    base: PullRequestResponseBase | None = Field(default=None)
    author_association: str | None = Field(default=None)
    labels: list[PullRequestResponseLabelsItem] | None = Field(default=None)
    milestone: dict[str, Any] | None = Field(default=None)
    assignees: list[PullRequestResponseAssigneesItem] | None = Field(default=None)
    requested_reviewers: list[dict[str, Any]] | None = Field(default=None)
    comments: int | None = Field(default=None)
    review_comments: int | None = Field(default=None)
    commits: int | None = Field(default=None)
    additions: int | None = Field(default=None)
    deletions: int | None = Field(default=None)
    changed_files: int | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class RepositoriesListResultMeta(BaseModel):
    """Metadata for repositories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class RepositoriesApiSearchResultMeta(BaseModel):
    """Metadata for repositories.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)
    total_count: int | None = Field(default=None)

class OrgRepositoriesListResultMeta(BaseModel):
    """Metadata for org_repositories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class BranchesListResultMeta(BaseModel):
    """Metadata for branches.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class CommitsListResultMeta(BaseModel):
    """Metadata for commits.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class ReleasesListResultMeta(BaseModel):
    """Metadata for releases.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class IssuesListResultMeta(BaseModel):
    """Metadata for issues.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class IssuesApiSearchResultMeta(BaseModel):
    """Metadata for issues.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)
    total_count: int | None = Field(default=None)

class PullRequestsListResultMeta(BaseModel):
    """Metadata for pull_requests.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class PullRequestsApiSearchResultMeta(BaseModel):
    """Metadata for pull_requests.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)
    total_count: int | None = Field(default=None)

class ReviewsListResultMeta(BaseModel):
    """Metadata for reviews.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class CommentsListResultMeta(BaseModel):
    """Metadata for comments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class PrCommentsListResultMeta(BaseModel):
    """Metadata for pr_comments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class LabelsListResultMeta(BaseModel):
    """Metadata for labels.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class MilestonesListResultMeta(BaseModel):
    """Metadata for milestones.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class OrganizationsListResultMeta(BaseModel):
    """Metadata for organizations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class UsersApiSearchResultMeta(BaseModel):
    """Metadata for users.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)
    total_count: int | None = Field(default=None)

class TeamsListResultMeta(BaseModel):
    """Metadata for teams.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class TagsListResultMeta(BaseModel):
    """Metadata for tags.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class StargazersListResultMeta(BaseModel):
    """Metadata for stargazers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class ViewerRepositoriesListResultMeta(BaseModel):
    """Metadata for viewer_repositories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class ProjectsListResultMeta(BaseModel):
    """Metadata for projects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class ProjectItemsListResultMeta(BaseModel):
    """Metadata for project_items.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class DiscussionsListResultMeta(BaseModel):
    """Metadata for discussions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)

class DiscussionsApiSearchResultMeta(BaseModel):
    """Metadata for discussions.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None)
    end_cursor: str | None = Field(default=None)
    total_count: int | None = Field(default=None)

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


class CommitsSearchData(BaseModel):
    """Search result data for commits entity."""
    model_config = ConfigDict(extra="allow")

    oid: str | None = None
    """Full Git commit SHA"""
    abbreviated_oid: str | None = None
    """Abbreviated Git commit SHA (typically 7 characters)"""
    message_headline: str | None = None
    """First line of the commit message"""
    message: str | None = None
    """Full commit message"""
    committed_date: str | None = None
    """ISO 8601 timestamp when the commit was applied to its tree"""
    authored_date: str | None = None
    """ISO 8601 timestamp when the commit was originally authored"""
    additions: int | None = None
    """Number of lines added across all files in the commit"""
    deletions: int | None = None
    """Number of lines deleted across all files in the commit"""
    changed_files: int | None = None
    """Number of files changed in the commit"""
    url: str | None = None
    """Permalink to the commit on GitHub"""


class DirectoryContentSearchData(BaseModel):
    """Search result data for directory_content entity."""
    model_config = ConfigDict(extra="allow")



class DiscussionsSearchData(BaseModel):
    """Search result data for discussions entity."""
    model_config = ConfigDict(extra="allow")



class FileContentSearchData(BaseModel):
    """Search result data for file_content entity."""
    model_config = ConfigDict(extra="allow")



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


class LabelsSearchData(BaseModel):
    """Search result data for labels entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """GraphQL node ID of the label"""
    name: str | None = None
    """Label name"""
    color: str | None = None
    """Label color as a 6-character hex string without a leading `#`"""
    description: str | None = None
    """Short description of what the label is used for"""
    created_at: str | None = None
    """ISO 8601 timestamp when the label was created"""
    url: str | None = None
    """Permalink to the label on GitHub"""


class MilestonesSearchData(BaseModel):
    """Search result data for milestones entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """GraphQL node ID of the milestone"""
    number: int | None = None
    """Repository-scoped milestone number"""
    title: str | None = None
    """Milestone title"""
    description: str | None = None
    """Milestone description"""
    state: str | None = None
    """Milestone state: `OPEN` or `CLOSED`"""
    due_on: str | None = None
    """ISO 8601 timestamp for the milestone's due date, if set"""
    closed_at: str | None = None
    """ISO 8601 timestamp when the milestone was closed, if applicable"""
    created_at: str | None = None
    """ISO 8601 timestamp when the milestone was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the milestone was last updated"""
    progress_percentage: float | None = None
    """Percentage of associated issues/PRs that are closed"""


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


class OrgRepositoriesSearchData(BaseModel):
    """Search result data for org_repositories entity."""
    model_config = ConfigDict(extra="allow")



class PrCommentsSearchData(BaseModel):
    """Search result data for pr_comments entity."""
    model_config = ConfigDict(extra="allow")



class ProjectItemsSearchData(BaseModel):
    """Search result data for project_items entity."""
    model_config = ConfigDict(extra="allow")



class ProjectsSearchData(BaseModel):
    """Search result data for projects entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """GraphQL node ID of the project"""
    number: int | None = None
    """Organization- or user-scoped project number"""
    title: str | None = None
    """Project title"""
    short_description: str | None = None
    """Short description displayed on the project summary"""
    url: str | None = None
    """Permalink to the project on GitHub"""
    closed: bool | None = None
    """Whether the project has been closed"""
    public: bool | None = None
    """Whether the project is publicly visible"""
    created_at: str | None = None
    """ISO 8601 timestamp when the project was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the project was last updated"""


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


class ReleasesSearchData(BaseModel):
    """Search result data for releases entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """GraphQL node ID of the release"""
    database_id: int | None = None
    """REST API numeric identifier for the release"""
    name: str | None = None
    """Display name of the release"""
    tag_name: str | None = None
    """Git tag the release points at (e.g. `v1.2.3`)"""
    description: str | None = None
    """Markdown body / release notes"""
    published_at: str | None = None
    """ISO 8601 timestamp when the release was published"""
    created_at: str | None = None
    """ISO 8601 timestamp when the release was created"""
    is_prerelease: bool | None = None
    """Whether the release is marked as a pre-release"""
    is_draft: bool | None = None
    """Whether the release is still a draft and not published"""
    url: str | None = None
    """Permalink to the release on GitHub"""


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


class ReviewsSearchData(BaseModel):
    """Search result data for reviews entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """GraphQL node ID of the review"""
    database_id: int | None = None
    """REST API numeric identifier for the review"""
    state: str | None = None
    """Review state: `PENDING`, `COMMENTED`, `APPROVED`, `CHANGES_REQUESTED`, or `DISMISSED`"""
    body: str | None = None
    """Review body text"""
    submitted_at: str | None = None
    """ISO 8601 timestamp when the review was submitted"""
    created_at: str | None = None
    """ISO 8601 timestamp when the review was created"""
    updated_at: str | None = None
    """ISO 8601 timestamp when the review was last updated"""
    url: str | None = None
    """Permalink to the review on GitHub"""


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


class ViewerSearchData(BaseModel):
    """Search result data for viewer entity."""
    model_config = ConfigDict(extra="allow")



class ViewerRepositoriesSearchData(BaseModel):
    """Search result data for viewer_repositories entity."""
    model_config = ConfigDict(extra="allow")



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

CommitsSearchResult = AirbyteSearchResult[CommitsSearchData]
"""Search result type for commits entity."""

DirectoryContentSearchResult = AirbyteSearchResult[DirectoryContentSearchData]
"""Search result type for directory_content entity."""

DiscussionsSearchResult = AirbyteSearchResult[DiscussionsSearchData]
"""Search result type for discussions entity."""

FileContentSearchResult = AirbyteSearchResult[FileContentSearchData]
"""Search result type for file_content entity."""

IssuesSearchResult = AirbyteSearchResult[IssuesSearchData]
"""Search result type for issues entity."""

LabelsSearchResult = AirbyteSearchResult[LabelsSearchData]
"""Search result type for labels entity."""

MilestonesSearchResult = AirbyteSearchResult[MilestonesSearchData]
"""Search result type for milestones entity."""

OrganizationsSearchResult = AirbyteSearchResult[OrganizationsSearchData]
"""Search result type for organizations entity."""

OrgRepositoriesSearchResult = AirbyteSearchResult[OrgRepositoriesSearchData]
"""Search result type for org_repositories entity."""

PrCommentsSearchResult = AirbyteSearchResult[PrCommentsSearchData]
"""Search result type for pr_comments entity."""

ProjectItemsSearchResult = AirbyteSearchResult[ProjectItemsSearchData]
"""Search result type for project_items entity."""

ProjectsSearchResult = AirbyteSearchResult[ProjectsSearchData]
"""Search result type for projects entity."""

PullRequestsSearchResult = AirbyteSearchResult[PullRequestsSearchData]
"""Search result type for pull_requests entity."""

ReleasesSearchResult = AirbyteSearchResult[ReleasesSearchData]
"""Search result type for releases entity."""

RepositoriesSearchResult = AirbyteSearchResult[RepositoriesSearchData]
"""Search result type for repositories entity."""

ReviewsSearchResult = AirbyteSearchResult[ReviewsSearchData]
"""Search result type for reviews entity."""

StargazersSearchResult = AirbyteSearchResult[StargazersSearchData]
"""Search result type for stargazers entity."""

TagsSearchResult = AirbyteSearchResult[TagsSearchData]
"""Search result type for tags entity."""

TeamsSearchResult = AirbyteSearchResult[TeamsSearchData]
"""Search result type for teams entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""

ViewerSearchResult = AirbyteSearchResult[ViewerSearchData]
"""Search result type for viewer entity."""

ViewerRepositoriesSearchResult = AirbyteSearchResult[ViewerRepositoriesSearchData]
"""Search result type for viewer_repositories entity."""



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

