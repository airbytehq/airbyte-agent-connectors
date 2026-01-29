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

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

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

