"""
Auto-generated type definitions for asana connector.

Generated from OpenAPI specification schemas.
"""
from typing import TypedDict, NotRequired, Any

# ===== AUTH CONFIG TYPE DEFINITIONS =====

class AsanaAuthConfig(TypedDict):
    """Authentication"""
    token: str  # Authentication bearer token

# ===== RESPONSE TYPE DEFINITIONS =====

class Task(TypedDict):
    """Compact task object"""
    gid: NotRequired[str]
    resource_type: NotRequired[str]
    name: NotRequired[str]

class TaskResponse(TypedDict):
    """Task response wrapper"""
    data: NotRequired[Task]

class TasksList(TypedDict):
    """Paginated list of tasks"""
    data: NotRequired[list[Task]]
    next_page: NotRequired[dict[str, Any] | None]

class Project(TypedDict):
    """Compact project object"""
    gid: NotRequired[str]
    resource_type: NotRequired[str]
    name: NotRequired[str]

class ProjectResponse(TypedDict):
    """Project response wrapper"""
    data: NotRequired[Project]

class ProjectsList(TypedDict):
    """Paginated list of projects"""
    data: NotRequired[list[Project]]
    next_page: NotRequired[dict[str, Any] | None]

class Workspace(TypedDict):
    """Compact workspace object"""
    gid: NotRequired[str]
    resource_type: NotRequired[str]
    name: NotRequired[str]

class WorkspaceResponse(TypedDict):
    """Workspace response wrapper"""
    data: NotRequired[Workspace]

class WorkspacesList(TypedDict):
    """Paginated list of workspaces"""
    data: NotRequired[list[Workspace]]
    next_page: NotRequired[dict[str, Any] | None]

class User(TypedDict):
    """Compact user object"""
    gid: NotRequired[str]
    resource_type: NotRequired[str]
    name: NotRequired[str]

class UserResponse(TypedDict):
    """User response wrapper"""
    data: NotRequired[User]

class UsersList(TypedDict):
    """Paginated list of users"""
    data: NotRequired[list[User]]
    next_page: NotRequired[dict[str, Any] | None]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class TasksListParams(TypedDict):
    """Parameters for tasks.list operation"""
    project_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]

class TasksGetParams(TypedDict):
    """Parameters for tasks.get operation"""
    task_gid: str

class ProjectsListParams(TypedDict):
    """Parameters for projects.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]
    workspace: NotRequired[str]

class ProjectsGetParams(TypedDict):
    """Parameters for projects.get operation"""
    project_gid: str

class WorkspacesListParams(TypedDict):
    """Parameters for workspaces.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]

class WorkspacesGetParams(TypedDict):
    """Parameters for workspaces.get operation"""
    workspace_gid: str

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]
    workspace: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    user_gid: str
