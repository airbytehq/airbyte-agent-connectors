"""
Type definitions for asana connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class TasksListParams(TypedDict):
    """Parameters for tasks.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]
    project: NotRequired[str]
    workspace: NotRequired[str]
    section: NotRequired[str]
    assignee: NotRequired[str]
    completed_since: NotRequired[str]
    modified_since: NotRequired[str]

class ProjectTasksListParams(TypedDict):
    """Parameters for project_tasks.list operation"""
    project_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]
    completed_since: NotRequired[str]

class TasksGetParams(TypedDict):
    """Parameters for tasks.get operation"""
    task_gid: str

class WorkspaceTaskSearchListParams(TypedDict):
    """Parameters for workspace_task_search.list operation"""
    workspace_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]
    text: NotRequired[str]
    completed: NotRequired[bool]
    assignee_any: NotRequired[str]
    projects_any: NotRequired[str]
    sections_any: NotRequired[str]
    teams_any: NotRequired[str]
    followers_any: NotRequired[str]
    created_at_after: NotRequired[str]
    created_at_before: NotRequired[str]
    modified_at_after: NotRequired[str]
    modified_at_before: NotRequired[str]
    due_on_after: NotRequired[str]
    due_on_before: NotRequired[str]
    resource_subtype: NotRequired[str]
    sort_by: NotRequired[str]
    sort_ascending: NotRequired[bool]

class ProjectsListParams(TypedDict):
    """Parameters for projects.list operation"""
    limit: NotRequired[int]
    offset: NotRequired[str]
    workspace: NotRequired[str]
    team: NotRequired[str]
    archived: NotRequired[bool]

class ProjectsGetParams(TypedDict):
    """Parameters for projects.get operation"""
    project_gid: str

class TaskProjectsListParams(TypedDict):
    """Parameters for task_projects.list operation"""
    task_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]

class TeamProjectsListParams(TypedDict):
    """Parameters for team_projects.list operation"""
    team_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]
    archived: NotRequired[bool]

class WorkspaceProjectsListParams(TypedDict):
    """Parameters for workspace_projects.list operation"""
    workspace_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]
    archived: NotRequired[bool]

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
    team: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    user_gid: str

class WorkspaceUsersListParams(TypedDict):
    """Parameters for workspace_users.list operation"""
    workspace_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]

class TeamUsersListParams(TypedDict):
    """Parameters for team_users.list operation"""
    team_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]

class TeamsGetParams(TypedDict):
    """Parameters for teams.get operation"""
    team_gid: str

class WorkspaceTeamsListParams(TypedDict):
    """Parameters for workspace_teams.list operation"""
    workspace_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]

class UserTeamsListParams(TypedDict):
    """Parameters for user_teams.list operation"""
    user_gid: str
    organization: str
    limit: NotRequired[int]
    offset: NotRequired[str]

class AttachmentsListParams(TypedDict):
    """Parameters for attachments.list operation"""
    parent: str
    limit: NotRequired[int]
    offset: NotRequired[str]

class AttachmentsGetParams(TypedDict):
    """Parameters for attachments.get operation"""
    attachment_gid: str

class AttachmentsDownloadParams(TypedDict):
    """Parameters for attachments.download operation"""
    attachment_gid: str
    range_header: NotRequired[str]
