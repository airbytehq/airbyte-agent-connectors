"""
Pydantic models for github connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any
from typing import Optional

# Authentication configuration

class GithubAuthConfig(BaseModel):
    """Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: Optional[str] = None
    """OAuth2 access token"""
    refresh_token: Optional[str] = None
    """OAuth2 refresh token (optional)"""
    client_id: Optional[str] = None
    """OAuth2 client ID (optional)"""
    client_secret: Optional[str] = None
    """OAuth2 client secret (optional)"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

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


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

RepositoriesGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for repositories.get operation."""

RepositoriesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for repositories.list operation."""

RepositoriesSearchResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for repositories.search operation."""

OrgRepositoriesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for org_repositories.list operation."""

BranchesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for branches.list operation."""

BranchesGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for branches.get operation."""

CommitsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for commits.list operation."""

CommitsGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for commits.get operation."""

ReleasesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for releases.list operation."""

ReleasesGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for releases.get operation."""

IssuesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for issues.list operation."""

IssuesGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for issues.get operation."""

IssuesSearchResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for issues.search operation."""

PullRequestsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for pull_requests.list operation."""

PullRequestsGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for pull_requests.get operation."""

PullRequestsSearchResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for pull_requests.search operation."""

ReviewsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for reviews.list operation."""

CommentsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for comments.list operation."""

CommentsGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for comments.get operation."""

PrCommentsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for pr_comments.list operation."""

PrCommentsGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for pr_comments.get operation."""

LabelsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for labels.list operation."""

LabelsGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for labels.get operation."""

MilestonesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for milestones.list operation."""

MilestonesGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for milestones.get operation."""

OrganizationsGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for organizations.get operation."""

OrganizationsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for organizations.list operation."""

UsersGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for users.get operation."""

UsersListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for users.list operation."""

UsersSearchResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for users.search operation."""

TeamsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for teams.list operation."""

TeamsGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for teams.get operation."""

TagsListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for tags.list operation."""

TagsGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for tags.get operation."""

StargazersListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for stargazers.list operation."""

ViewerGetResult = GithubExecuteResult[dict[str, Any]]
"""Result type for viewer.get operation."""

ViewerRepositoriesListResult = GithubExecuteResult[list[dict[str, Any]]]
"""Result type for viewer_repositories.list operation."""

