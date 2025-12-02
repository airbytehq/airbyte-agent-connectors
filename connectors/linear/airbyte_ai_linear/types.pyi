"""
Auto-generated type definitions for linear connector.

Generated from OpenAPI specification schemas.
"""
from typing import TypedDict, NotRequired, Any

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

class IssuesListResponse(TypedDict):
    """GraphQL response for issues list"""
    data: NotRequired[dict[str, Any]]

class IssueResponse(TypedDict):
    """GraphQL response for single issue"""
    data: NotRequired[dict[str, Any]]

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

class ProjectsListResponse(TypedDict):
    """GraphQL response for projects list"""
    data: NotRequired[dict[str, Any]]

class ProjectResponse(TypedDict):
    """GraphQL response for single project"""
    data: NotRequired[dict[str, Any]]

class Team(TypedDict):
    """Linear team object"""
    id: str
    name: str
    key: str
    description: NotRequired[Any]
    timezone: NotRequired[Any]
    createdAt: NotRequired[str]
    updatedAt: NotRequired[str]

class TeamsListResponse(TypedDict):
    """GraphQL response for teams list"""
    data: NotRequired[dict[str, Any]]

class TeamResponse(TypedDict):
    """GraphQL response for single team"""
    data: NotRequired[dict[str, Any]]

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
