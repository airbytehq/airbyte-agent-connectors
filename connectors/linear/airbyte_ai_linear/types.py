"""
Type definitions for linear connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .models import (
        Issue,
        Project,
        Team,
    )

# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

class IssuesListResponseDataIssuesPageinfo(TypedDict):
    """Pagination information"""
    hasNextPage: NotRequired[bool]
    endCursor: NotRequired[str | None]

class IssuesListResponseDataIssues(TypedDict):
    """Nested schema for IssuesListResponseData.issues"""
    nodes: NotRequired[list[Issue]]
    pageInfo: NotRequired[IssuesListResponseDataIssuesPageinfo]

class IssuesListResponseData(TypedDict):
    """Nested schema for IssuesListResponse.data"""
    issues: NotRequired[IssuesListResponseDataIssues]

class IssueResponseData(TypedDict):
    """Nested schema for IssueResponse.data"""
    issue: NotRequired[Issue]

class ProjectsListResponseDataProjectsPageinfo(TypedDict):
    """Pagination information"""
    hasNextPage: NotRequired[bool]
    endCursor: NotRequired[str | None]

class ProjectsListResponseDataProjects(TypedDict):
    """Nested schema for ProjectsListResponseData.projects"""
    nodes: NotRequired[list[Project]]
    pageInfo: NotRequired[ProjectsListResponseDataProjectsPageinfo]

class ProjectsListResponseData(TypedDict):
    """Nested schema for ProjectsListResponse.data"""
    projects: NotRequired[ProjectsListResponseDataProjects]

class ProjectResponseData(TypedDict):
    """Nested schema for ProjectResponse.data"""
    project: NotRequired[Project]

class TeamsListResponseDataTeamsPageinfo(TypedDict):
    """Pagination information"""
    hasNextPage: NotRequired[bool]
    endCursor: NotRequired[str | None]

class TeamsListResponseDataTeams(TypedDict):
    """Nested schema for TeamsListResponseData.teams"""
    nodes: NotRequired[list[Team]]
    pageInfo: NotRequired[TeamsListResponseDataTeamsPageinfo]

class TeamsListResponseData(TypedDict):
    """Nested schema for TeamsListResponse.data"""
    teams: NotRequired[TeamsListResponseDataTeams]

class TeamResponseData(TypedDict):
    """Nested schema for TeamResponse.data"""
    team: NotRequired[Team]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class IssuesListParams(TypedDict):
    """Parameters for issues.list operation"""
    first: NotRequired[int]
    after: NotRequired[str]

class IssuesGetParams(TypedDict):
    """Parameters for issues.get operation"""
    id: str

class ProjectsListParams(TypedDict):
    """Parameters for projects.list operation"""
    first: NotRequired[int]
    after: NotRequired[str]

class ProjectsGetParams(TypedDict):
    """Parameters for projects.get operation"""
    id: str

class TeamsListParams(TypedDict):
    """Parameters for teams.list operation"""
    first: NotRequired[int]
    after: NotRequired[str]

class TeamsGetParams(TypedDict):
    """Parameters for teams.get operation"""
    id: str
