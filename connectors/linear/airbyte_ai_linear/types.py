"""
Type definitions for linear connector.
"""
from typing import TypedDict, NotRequired, Any

# ===== AUTH CONFIG TYPE DEFINITIONS =====

class LinearAuthConfig(TypedDict):
    """Authentication"""
    api_key: str  # API authentication key

# ===== RESPONSE TYPE DEFINITIONS =====

class Issue(TypedDict):
    """Linear issue object"""
    id: str
    title: str
    description: NotRequired[Any]
    state: NotRequired[Any]
    priority: NotRequired[Any]
    assignee: NotRequired[Any]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]

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

class IssuesListResponse(TypedDict):
    """GraphQL response for issues list"""
    data: NotRequired[IssuesListResponseData]

class IssueResponseData(TypedDict):
    """Nested schema for IssueResponse.data"""
    issue: NotRequired[Issue]

class IssueResponse(TypedDict):
    """GraphQL response for single issue"""
    data: NotRequired[IssueResponseData]

class Project(TypedDict):
    """Linear project object"""
    id: str
    name: str
    description: NotRequired[Any]
    state: NotRequired[Any]
    startDate: NotRequired[Any]
    targetDate: NotRequired[Any]
    lead: NotRequired[Any]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]

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

class ProjectsListResponse(TypedDict):
    """GraphQL response for projects list"""
    data: NotRequired[ProjectsListResponseData]

class ProjectResponseData(TypedDict):
    """Nested schema for ProjectResponse.data"""
    project: NotRequired[Project]

class ProjectResponse(TypedDict):
    """GraphQL response for single project"""
    data: NotRequired[ProjectResponseData]

class Team(TypedDict):
    """Linear team object"""
    id: str
    name: str
    key: str
    description: NotRequired[Any]
    timezone: NotRequired[Any]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]

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

class TeamsListResponse(TypedDict):
    """GraphQL response for teams list"""
    data: NotRequired[TeamsListResponseData]

class TeamResponseData(TypedDict):
    """Nested schema for TeamResponse.data"""
    team: NotRequired[Team]

class TeamResponse(TypedDict):
    """GraphQL response for single team"""
    data: NotRequired[TeamResponseData]

# ===== ENVELOPE TYPE DEFINITIONS =====

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
