"""
Type definitions for github connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

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
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class RepositoriesApiSearchParams(TypedDict):
    """Parameters for repositories.api_search operation"""
    query: str
    limit: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class OrgRepositoriesListParams(TypedDict):
    """Parameters for org_repositories.list operation"""
    org: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class BranchesListParams(TypedDict):
    """Parameters for branches.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class BranchesGetParams(TypedDict):
    """Parameters for branches.get operation"""
    owner: str
    repo: str
    branch: str
    fields: NotRequired[list[str]]

class CommitsListParams(TypedDict):
    """Parameters for commits.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class CommitsGetParams(TypedDict):
    """Parameters for commits.get operation"""
    owner: str
    repo: str
    sha: str
    fields: NotRequired[list[str]]

class ReleasesListParams(TypedDict):
    """Parameters for releases.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ReleasesGetParams(TypedDict):
    """Parameters for releases.get operation"""
    owner: str
    repo: str
    tag: str
    fields: NotRequired[list[str]]

class IssuesListParams(TypedDict):
    """Parameters for issues.list operation"""
    owner: str
    repo: str
    states: NotRequired[list[str]]
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class IssuesGetParams(TypedDict):
    """Parameters for issues.get operation"""
    owner: str
    repo: str
    number: int
    fields: NotRequired[list[str]]

class IssuesApiSearchParams(TypedDict):
    """Parameters for issues.api_search operation"""
    query: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class PullRequestsListParams(TypedDict):
    """Parameters for pull_requests.list operation"""
    owner: str
    repo: str
    states: NotRequired[list[str]]
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class PullRequestsGetParams(TypedDict):
    """Parameters for pull_requests.get operation"""
    owner: str
    repo: str
    number: int
    fields: NotRequired[list[str]]

class PullRequestsApiSearchParams(TypedDict):
    """Parameters for pull_requests.api_search operation"""
    query: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ReviewsListParams(TypedDict):
    """Parameters for reviews.list operation"""
    owner: str
    repo: str
    number: int
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class CommentsListParams(TypedDict):
    """Parameters for comments.list operation"""
    owner: str
    repo: str
    number: int
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class CommentsGetParams(TypedDict):
    """Parameters for comments.get operation"""
    id: str
    fields: NotRequired[list[str]]

class PrCommentsListParams(TypedDict):
    """Parameters for pr_comments.list operation"""
    owner: str
    repo: str
    number: int
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class PrCommentsGetParams(TypedDict):
    """Parameters for pr_comments.get operation"""
    id: str
    fields: NotRequired[list[str]]

class LabelsListParams(TypedDict):
    """Parameters for labels.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class LabelsGetParams(TypedDict):
    """Parameters for labels.get operation"""
    owner: str
    repo: str
    name: str
    fields: NotRequired[list[str]]

class MilestonesListParams(TypedDict):
    """Parameters for milestones.list operation"""
    owner: str
    repo: str
    states: NotRequired[list[str]]
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class MilestonesGetParams(TypedDict):
    """Parameters for milestones.get operation"""
    owner: str
    repo: str
    number: int
    fields: NotRequired[list[str]]

class OrganizationsGetParams(TypedDict):
    """Parameters for organizations.get operation"""
    org: str
    fields: NotRequired[list[str]]

class OrganizationsListParams(TypedDict):
    """Parameters for organizations.list operation"""
    username: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    username: str
    fields: NotRequired[list[str]]

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    org: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class UsersApiSearchParams(TypedDict):
    """Parameters for users.api_search operation"""
    query: str
    limit: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class TeamsListParams(TypedDict):
    """Parameters for teams.list operation"""
    org: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class TeamsGetParams(TypedDict):
    """Parameters for teams.get operation"""
    org: str
    team_slug: str
    fields: NotRequired[list[str]]

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class TagsGetParams(TypedDict):
    """Parameters for tags.get operation"""
    owner: str
    repo: str
    tag: str
    fields: NotRequired[list[str]]

class StargazersListParams(TypedDict):
    """Parameters for stargazers.list operation"""
    owner: str
    repo: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ViewerGetParams(TypedDict):
    """Parameters for viewer.get operation"""
    fields: NotRequired[list[str]]

class ViewerRepositoriesListParams(TypedDict):
    """Parameters for viewer_repositories.list operation"""
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ProjectsListParams(TypedDict):
    """Parameters for projects.list operation"""
    org: str
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

class ProjectsGetParams(TypedDict):
    """Parameters for projects.get operation"""
    org: str
    project_number: int
    fields: NotRequired[list[str]]

class ProjectItemsListParams(TypedDict):
    """Parameters for project_items.list operation"""
    org: str
    project_number: int
    per_page: NotRequired[int]
    after: NotRequired[str]
    fields: NotRequired[list[str]]

