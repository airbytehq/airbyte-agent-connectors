"""
Type definitions for github connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

class RepositoryOwner(TypedDict):
    """Repository owner information"""
    login: NotRequired[str]
    id: NotRequired[int]
    node_id: NotRequired[str]
    avatar_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    url: NotRequired[str]
    html_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    organizations_url: NotRequired[str]
    repos_url: NotRequired[str]
    events_url: NotRequired[str]
    received_events_url: NotRequired[str]
    type: NotRequired[str]
    site_admin: NotRequired[bool]

class RepositoryPermissions(TypedDict):
    """User permissions for the repository"""
    admin: NotRequired[bool]
    push: NotRequired[bool]
    pull: NotRequired[bool]

class RepositoryLicense(TypedDict):
    """Repository license information"""
    key: NotRequired[str]
    name: NotRequired[str]
    url: NotRequired[str | None]
    spdx_id: NotRequired[str | None]
    node_id: NotRequired[str]
    html_url: NotRequired[str | None]

class RepositorySecurityAndAnalysisAdvancedSecurity(TypedDict):
    """Nested schema for RepositorySecurityAndAnalysis.advanced_security"""
    status: NotRequired[str]

class RepositorySecurityAndAnalysisSecretScanning(TypedDict):
    """Nested schema for RepositorySecurityAndAnalysis.secret_scanning"""
    status: NotRequired[str]

class RepositorySecurityAndAnalysisSecretScanningPushProtection(TypedDict):
    """Nested schema for RepositorySecurityAndAnalysis.secret_scanning_push_protection"""
    status: NotRequired[str]

class RepositorySecurityAndAnalysis(TypedDict):
    """Security and analysis settings"""
    advanced_security: NotRequired[RepositorySecurityAndAnalysisAdvancedSecurity]
    secret_scanning: NotRequired[RepositorySecurityAndAnalysisSecretScanning]
    secret_scanning_push_protection: NotRequired[RepositorySecurityAndAnalysisSecretScanningPushProtection]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class RepositoriesGetParams(TypedDict):
    """Parameters for repositories.get operation"""
    owner: str
    repo: str
    fields: NotRequired[list[str]]

class RepositoriesListParams(TypedDict):
    """Parameters for repositories.list operation"""
    username: str
    per_page: NotRequired[int]
    fields: NotRequired[list[str]]

class RepositoriesSearchParams(TypedDict):
    """Parameters for repositories.search operation"""
    query: str
    limit: NotRequired[int]
    fields: NotRequired[list[str]]
