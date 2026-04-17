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

class IssueResponseIssueDependenciesSummary(BaseModel):
    """Summary of issue dependencies"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    blocked_by: Union[int, Any] = Field(default=None)
    blocking: Union[int, Any] = Field(default=None)
    total_blocked_by: Union[int, Any] = Field(default=None)
    total_blocking: Union[int, Any] = Field(default=None)

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

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

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



class CommentsSearchData(BaseModel):
    """Search result data for comments entity."""
    model_config = ConfigDict(extra="allow")



class IssuesSearchData(BaseModel):
    """Search result data for issues entity."""
    model_config = ConfigDict(extra="allow")



class OrganizationsSearchData(BaseModel):
    """Search result data for organizations entity."""
    model_config = ConfigDict(extra="allow")



class PullRequestsSearchData(BaseModel):
    """Search result data for pull_requests entity."""
    model_config = ConfigDict(extra="allow")



class RepositoriesSearchData(BaseModel):
    """Search result data for repositories entity."""
    model_config = ConfigDict(extra="allow")



class StargazersSearchData(BaseModel):
    """Search result data for stargazers entity."""
    model_config = ConfigDict(extra="allow")



class TagsSearchData(BaseModel):
    """Search result data for tags entity."""
    model_config = ConfigDict(extra="allow")



class TeamsSearchData(BaseModel):
    """Search result data for teams entity."""
    model_config = ConfigDict(extra="allow")



class UsersSearchData(BaseModel):
    """Search result data for users entity."""
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

RepositoriesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for repositories.list operation."""

RepositoriesApiSearchResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for repositories.api_search operation."""

OrgRepositoriesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for org_repositories.list operation."""

BranchesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for branches.list operation."""

CommitsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for commits.list operation."""

ReleasesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for releases.list operation."""

IssuesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for issues.list operation."""

IssuesApiSearchResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for issues.api_search operation."""

PullRequestsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for pull_requests.list operation."""

PullRequestsApiSearchResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for pull_requests.api_search operation."""

ReviewsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for reviews.list operation."""

CommentsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for comments.list operation."""

PrCommentsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for pr_comments.list operation."""

LabelsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for labels.list operation."""

MilestonesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for milestones.list operation."""

OrganizationsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for organizations.list operation."""

UsersListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for users.list operation."""

UsersApiSearchResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for users.api_search operation."""

TeamsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for teams.list operation."""

TagsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for tags.list operation."""

StargazersListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for stargazers.list operation."""

ViewerRepositoriesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for viewer_repositories.list operation."""

ProjectsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for projects.list operation."""

ProjectItemsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for project_items.list operation."""

DiscussionsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for discussions.list operation."""

DiscussionsApiSearchResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for discussions.api_search operation."""

DirectoryContentListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for directory_content.list operation."""

