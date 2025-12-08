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

    access_token: str
    """OAuth2 access token"""
    refresh_token: Optional[str] = None
    """OAuth2 refresh token (optional)"""
    client_id: Optional[str] = None
    """OAuth2 client ID (optional)"""
    client_secret: Optional[str] = None
    """OAuth2 client secret (optional)"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class RepositorySecurityAndAnalysisAdvancedSecurity(BaseModel):
    """Nested schema for RepositorySecurityAndAnalysis.advanced_security"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    status: Union[str, Any] = Field(default=None)

class RepositorySecurityAndAnalysisSecretScanningPushProtection(BaseModel):
    """Nested schema for RepositorySecurityAndAnalysis.secret_scanning_push_protection"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    status: Union[str, Any] = Field(default=None)

class RepositorySecurityAndAnalysisSecretScanning(BaseModel):
    """Nested schema for RepositorySecurityAndAnalysis.secret_scanning"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    status: Union[str, Any] = Field(default=None)

class RepositorySecurityAndAnalysis(BaseModel):
    """Security and analysis settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    advanced_security: Union[RepositorySecurityAndAnalysisAdvancedSecurity, Any] = Field(default=None)
    secret_scanning: Union[RepositorySecurityAndAnalysisSecretScanning, Any] = Field(default=None)
    secret_scanning_push_protection: Union[RepositorySecurityAndAnalysisSecretScanningPushProtection, Any] = Field(default=None)

class RepositoryPermissions(BaseModel):
    """User permissions for the repository"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: Union[bool, Any] = Field(default=None)
    push: Union[bool, Any] = Field(default=None)
    pull: Union[bool, Any] = Field(default=None)

class RepositoryOwner(BaseModel):
    """Repository owner information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: Union[str, Any] = Field(default=None)
    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    avatar_url: Union[str, Any] = Field(default=None)
    gravatar_id: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    html_url: Union[str, Any] = Field(default=None)
    followers_url: Union[str, Any] = Field(default=None)
    following_url: Union[str, Any] = Field(default=None)
    gists_url: Union[str, Any] = Field(default=None)
    starred_url: Union[str, Any] = Field(default=None)
    subscriptions_url: Union[str, Any] = Field(default=None)
    organizations_url: Union[str, Any] = Field(default=None)
    repos_url: Union[str, Any] = Field(default=None)
    events_url: Union[str, Any] = Field(default=None)
    received_events_url: Union[str, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)
    site_admin: Union[bool, Any] = Field(default=None)

class RepositoryLicense(BaseModel):
    """Repository license information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    key: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)
    spdx_id: Union[str | None, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    html_url: Union[str | None, Any] = Field(default=None)

class Repository(BaseModel):
    """GitHub repository object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    node_id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    full_name: Union[str, Any] = Field(default=None)
    owner: Union[RepositoryOwner, Any] = Field(default=None)
    private: Union[bool, Any] = Field(default=None)
    html_url: Union[str, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    fork: Union[bool, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    archive_url: Union[str, Any] = Field(default=None)
    assignees_url: Union[str, Any] = Field(default=None)
    blobs_url: Union[str, Any] = Field(default=None)
    branches_url: Union[str, Any] = Field(default=None)
    collaborators_url: Union[str, Any] = Field(default=None)
    comments_url: Union[str, Any] = Field(default=None)
    commits_url: Union[str, Any] = Field(default=None)
    compare_url: Union[str, Any] = Field(default=None)
    contents_url: Union[str, Any] = Field(default=None)
    contributors_url: Union[str, Any] = Field(default=None)
    deployments_url: Union[str, Any] = Field(default=None)
    downloads_url: Union[str, Any] = Field(default=None)
    events_url: Union[str, Any] = Field(default=None)
    forks_url: Union[str, Any] = Field(default=None)
    git_commits_url: Union[str, Any] = Field(default=None)
    git_refs_url: Union[str, Any] = Field(default=None)
    git_tags_url: Union[str, Any] = Field(default=None)
    git_url: Union[str, Any] = Field(default=None)
    issue_comment_url: Union[str, Any] = Field(default=None)
    issue_events_url: Union[str, Any] = Field(default=None)
    issues_url: Union[str, Any] = Field(default=None)
    keys_url: Union[str, Any] = Field(default=None)
    labels_url: Union[str, Any] = Field(default=None)
    languages_url: Union[str, Any] = Field(default=None)
    merges_url: Union[str, Any] = Field(default=None)
    milestones_url: Union[str, Any] = Field(default=None)
    notifications_url: Union[str, Any] = Field(default=None)
    pulls_url: Union[str, Any] = Field(default=None)
    releases_url: Union[str, Any] = Field(default=None)
    ssh_url: Union[str, Any] = Field(default=None)
    stargazers_url: Union[str, Any] = Field(default=None)
    statuses_url: Union[str, Any] = Field(default=None)
    subscribers_url: Union[str, Any] = Field(default=None)
    subscription_url: Union[str, Any] = Field(default=None)
    tags_url: Union[str, Any] = Field(default=None)
    teams_url: Union[str, Any] = Field(default=None)
    trees_url: Union[str, Any] = Field(default=None)
    clone_url: Union[str, Any] = Field(default=None)
    mirror_url: Union[str | None, Any] = Field(default=None)
    hooks_url: Union[str, Any] = Field(default=None)
    svn_url: Union[str, Any] = Field(default=None)
    homepage: Union[str | None, Any] = Field(default=None)
    language: Union[str | None, Any] = Field(default=None)
    forks_count: Union[int, Any] = Field(default=None)
    forks: Union[int, Any] = Field(default=None)
    stargazers_count: Union[int, Any] = Field(default=None)
    watchers_count: Union[int, Any] = Field(default=None)
    watchers: Union[int, Any] = Field(default=None)
    size: Union[int, Any] = Field(default=None)
    default_branch: Union[str, Any] = Field(default=None)
    open_issues_count: Union[int, Any] = Field(default=None)
    open_issues: Union[int, Any] = Field(default=None)
    is_template: Union[bool, Any] = Field(default=None)
    topics: Union[list[str], Any] = Field(default=None)
    has_issues: Union[bool, Any] = Field(default=None)
    has_projects: Union[bool, Any] = Field(default=None)
    has_wiki: Union[bool, Any] = Field(default=None)
    has_pages: Union[bool, Any] = Field(default=None)
    has_downloads: Union[bool, Any] = Field(default=None)
    has_discussions: Union[bool, Any] = Field(default=None)
    archived: Union[bool, Any] = Field(default=None)
    disabled: Union[bool, Any] = Field(default=None)
    visibility: Union[str, Any] = Field(default=None)
    pushed_at: Union[str | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    permissions: Union[RepositoryPermissions, Any] = Field(default=None)
    allow_rebase_merge: Union[bool, Any] = Field(default=None)
    allow_squash_merge: Union[bool, Any] = Field(default=None)
    allow_merge_commit: Union[bool, Any] = Field(default=None)
    allow_auto_merge: Union[bool, Any] = Field(default=None)
    delete_branch_on_merge: Union[bool, Any] = Field(default=None)
    allow_forking: Union[bool, Any] = Field(default=None)
    subscribers_count: Union[int, Any] = Field(default=None)
    network_count: Union[int, Any] = Field(default=None)
    license: Union[RepositoryLicense | None, Any] = Field(default=None)
    parent: Union[dict[str, Any] | None, Any] = Field(default=None)
    source: Union[dict[str, Any] | None, Any] = Field(default=None)
    template_repository: Union[dict[str, Any] | None, Any] = Field(default=None)
    organization: Union[dict[str, Any] | None, Any] = Field(default=None)
    security_and_analysis: Union[RepositorySecurityAndAnalysis | None, Any] = Field(default=None)
    temp_clone_token: Union[str | None, Any] = Field(default=None)

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

