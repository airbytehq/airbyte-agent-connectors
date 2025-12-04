"""
Type definitions for asana connector.
"""
from typing import TypedDict, NotRequired

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

class TasksListNextPage(TypedDict):
    """Nested schema for TasksList.next_page"""
    offset: NotRequired[str]
    path: NotRequired[str]
    uri: NotRequired[str]

class TasksList(TypedDict):
    """Paginated list of tasks"""
    data: NotRequired[list[Task]]
    next_page: NotRequired[TasksListNextPage | None]

class Project(TypedDict):
    """Compact project object"""
    gid: NotRequired[str]
    resource_type: NotRequired[str]
    name: NotRequired[str]

class ProjectResponse(TypedDict):
    """Project response wrapper"""
    data: NotRequired[Project]

class ProjectsListNextPage(TypedDict):
    """Nested schema for ProjectsList.next_page"""
    offset: NotRequired[str]
    path: NotRequired[str]
    uri: NotRequired[str]

class ProjectsList(TypedDict):
    """Paginated list of projects"""
    data: NotRequired[list[Project]]
    next_page: NotRequired[ProjectsListNextPage | None]

class Workspace(TypedDict):
    """Compact workspace object"""
    gid: NotRequired[str]
    resource_type: NotRequired[str]
    name: NotRequired[str]

class WorkspaceResponse(TypedDict):
    """Workspace response wrapper"""
    data: NotRequired[Workspace]

class WorkspacesListNextPage(TypedDict):
    """Nested schema for WorkspacesList.next_page"""
    offset: NotRequired[str]
    path: NotRequired[str]
    uri: NotRequired[str]

class WorkspacesList(TypedDict):
    """Paginated list of workspaces"""
    data: NotRequired[list[Workspace]]
    next_page: NotRequired[WorkspacesListNextPage | None]

class User(TypedDict):
    """Compact user object"""
    gid: NotRequired[str]
    resource_type: NotRequired[str]
    name: NotRequired[str]

class UserResponse(TypedDict):
    """User response wrapper"""
    data: NotRequired[User]

class UsersListNextPage(TypedDict):
    """Nested schema for UsersList.next_page"""
    offset: NotRequired[str]
    path: NotRequired[str]
    uri: NotRequired[str]

class UsersList(TypedDict):
    """Paginated list of users"""
    data: NotRequired[list[User]]
    next_page: NotRequired[UsersListNextPage | None]

# ===== ENVELOPE TYPE DEFINITIONS =====

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
