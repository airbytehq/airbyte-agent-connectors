"""
Pydantic models for asana connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any
from typing import Optional

# Authentication configuration - multiple options available

class AsanaOauth2AuthConfig(BaseModel):
    """OAuth 2"""

    model_config = ConfigDict(extra="forbid")

    access_token: Optional[str] = None
    """OAuth access token for API requests"""
    refresh_token: str
    """OAuth refresh token for automatic token renewal"""
    client_id: str
    """Connected App Consumer Key"""
    client_secret: str
    """Connected App Consumer Secret"""

class AsanaPersonalAccessTokenAuthConfig(BaseModel):
    """Personal Access Token"""

    model_config = ConfigDict(extra="forbid")

    token: str
    """Your Asana Personal Access Token. Generate one at https://app.asana.com/0/my-apps"""

AsanaAuthConfig = AsanaOauth2AuthConfig | AsanaPersonalAccessTokenAuthConfig

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class TaskCompactCreatedBy(BaseModel):
    """User who created the task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class TaskCompact(BaseModel):
    """Compact task object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_subtype: Union[str, Any] = Field(default=None)
    created_by: Union[TaskCompactCreatedBy, Any] = Field(default=None)

class Task(BaseModel):
    """Full task object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)

class TaskResponse(BaseModel):
    """Task response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Task, Any] = Field(default=None)

class TasksListNextPage(BaseModel):
    """Nested schema for TasksList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    uri: Union[str, Any] = Field(default=None)

class TasksList(BaseModel):
    """Paginated list of tasks containing compact task objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[TaskCompact], Any] = Field(default=None)
    next_page: Union[TasksListNextPage | None, Any] = Field(default=None)

class ProjectCompact(BaseModel):
    """Compact project object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)

class ProjectWorkspace(BaseModel):
    """Nested schema for Project.workspace"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class ProjectFollowersItem(BaseModel):
    """Nested schema for Project.followers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class ProjectMembersItem(BaseModel):
    """Nested schema for Project.members_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class ProjectTeam(BaseModel):
    """Nested schema for Project.team"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class ProjectOwner(BaseModel):
    """Nested schema for Project.owner"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class ProjectCurrentStatusCreatedBy(BaseModel):
    """Nested schema for ProjectCurrentStatus.created_by"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class ProjectCurrentStatusAuthor(BaseModel):
    """Nested schema for ProjectCurrentStatus.author"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class ProjectCurrentStatus(BaseModel):
    """Nested schema for Project.current_status"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    author: Union[ProjectCurrentStatusAuthor, Any] = Field(default=None)
    color: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    created_by: Union[ProjectCurrentStatusCreatedBy, Any] = Field(default=None)
    modified_at: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    text: Union[str, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)

class ProjectCurrentStatusUpdate(BaseModel):
    """Nested schema for Project.current_status_update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    resource_subtype: Union[str, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)

class Project(BaseModel):
    """Full project object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    archived: Union[bool, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)
    completed: Union[bool, Any] = Field(default=None)
    completed_at: Union[str | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    current_status: Union[ProjectCurrentStatus | None, Any] = Field(default=None)
    current_status_update: Union[ProjectCurrentStatusUpdate | None, Any] = Field(default=None)
    custom_fields: Union[list[Any], Any] = Field(default=None)
    default_access_level: Union[str, Any] = Field(default=None)
    default_view: Union[str, Any] = Field(default=None)
    due_on: Union[str | None, Any] = Field(default=None)
    due_date: Union[str | None, Any] = Field(default=None)
    followers: Union[list[ProjectFollowersItem], Any] = Field(default=None)
    members: Union[list[ProjectMembersItem], Any] = Field(default=None)
    minimum_access_level_for_customization: Union[str, Any] = Field(default=None)
    minimum_access_level_for_sharing: Union[str, Any] = Field(default=None)
    modified_at: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    notes: Union[str, Any] = Field(default=None)
    owner: Union[ProjectOwner, Any] = Field(default=None)
    permalink_url: Union[str, Any] = Field(default=None)
    privacy_setting: Union[str, Any] = Field(default=None)
    public: Union[bool, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    start_on: Union[str | None, Any] = Field(default=None)
    team: Union[ProjectTeam, Any] = Field(default=None)
    workspace: Union[ProjectWorkspace, Any] = Field(default=None)

class ProjectResponse(BaseModel):
    """Project response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Project, Any] = Field(default=None)

class ProjectsListNextPage(BaseModel):
    """Nested schema for ProjectsList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    uri: Union[str, Any] = Field(default=None)

class ProjectsList(BaseModel):
    """Paginated list of projects containing compact project objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[ProjectCompact], Any] = Field(default=None)
    next_page: Union[ProjectsListNextPage | None, Any] = Field(default=None)

class WorkspaceCompact(BaseModel):
    """Compact workspace object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)

class Workspace(BaseModel):
    """Full workspace object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    email_domains: Union[list[str], Any] = Field(default=None)
    is_organization: Union[bool, Any] = Field(default=None)

class WorkspaceResponse(BaseModel):
    """Workspace response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Workspace, Any] = Field(default=None)

class WorkspacesListNextPage(BaseModel):
    """Nested schema for WorkspacesList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    uri: Union[str, Any] = Field(default=None)

class WorkspacesList(BaseModel):
    """Paginated list of workspaces containing compact workspace objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[WorkspaceCompact], Any] = Field(default=None)
    next_page: Union[WorkspacesListNextPage | None, Any] = Field(default=None)

class UserCompact(BaseModel):
    """Compact user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)

class UserWorkspacesItem(BaseModel):
    """Nested schema for User.workspaces_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class User(BaseModel):
    """Full user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    email: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    photo: Union[dict[str, Any] | None, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    workspaces: Union[list[UserWorkspacesItem], Any] = Field(default=None)

class UserResponse(BaseModel):
    """User response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[User, Any] = Field(default=None)

class UsersListNextPage(BaseModel):
    """Nested schema for UsersList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    uri: Union[str, Any] = Field(default=None)

class UsersList(BaseModel):
    """Paginated list of users containing compact user objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[UserCompact], Any] = Field(default=None)
    next_page: Union[UsersListNextPage | None, Any] = Field(default=None)

class TeamCompact(BaseModel):
    """Compact team object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)

class TeamOrganization(BaseModel):
    """Nested schema for Team.organization"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class Team(BaseModel):
    """Full team object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    organization: Union[TeamOrganization, Any] = Field(default=None)
    permalink_url: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class TeamResponse(BaseModel):
    """Team response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Team, Any] = Field(default=None)

class TeamsListNextPage(BaseModel):
    """Nested schema for TeamsList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    uri: Union[str, Any] = Field(default=None)

class TeamsList(BaseModel):
    """Paginated list of teams containing compact team objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[TeamCompact], Any] = Field(default=None)
    next_page: Union[TeamsListNextPage | None, Any] = Field(default=None)

class AttachmentCompact(BaseModel):
    """Compact attachment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_subtype: Union[str, Any] = Field(default=None)

class AttachmentParent(BaseModel):
    """The parent object this attachment is attached to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_subtype: Union[str, Any] = Field(default=None, description="The subtype of the parent resource")
    """The subtype of the parent resource"""

class Attachment(BaseModel):
    """Full attachment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_subtype: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    download_url: Union[str | None, Any] = Field(default=None)
    permanent_url: Union[str | None, Any] = Field(default=None)
    host: Union[str, Any] = Field(default=None)
    parent: Union[AttachmentParent, Any] = Field(default=None)
    view_url: Union[str | None, Any] = Field(default=None)
    size: Union[int | None, Any] = Field(default=None)

class AttachmentResponse(BaseModel):
    """Attachment response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Attachment, Any] = Field(default=None)

class AttachmentsListNextPage(BaseModel):
    """Nested schema for AttachmentsList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    uri: Union[str, Any] = Field(default=None)

class AttachmentsList(BaseModel):
    """Paginated list of attachments containing compact attachment objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[AttachmentCompact], Any] = Field(default=None)
    next_page: Union[AttachmentsListNextPage | None, Any] = Field(default=None)

class TagCompact(BaseModel):
    """Compact tag object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)

class TagWorkspace(BaseModel):
    """Nested schema for Tag.workspace"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class Tag(BaseModel):
    """Full tag object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    color: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    followers: Union[list[Any], Any] = Field(default=None)
    notes: Union[str, Any] = Field(default=None)
    permalink_url: Union[str, Any] = Field(default=None)
    workspace: Union[TagWorkspace, Any] = Field(default=None)

class TagResponse(BaseModel):
    """Tag response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Tag, Any] = Field(default=None)

class TagsListNextPage(BaseModel):
    """Nested schema for TagsList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    uri: Union[str, Any] = Field(default=None)

class TagsList(BaseModel):
    """Paginated list of tags containing compact tag objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[TagCompact], Any] = Field(default=None)
    next_page: Union[TagsListNextPage | None, Any] = Field(default=None)

class SectionCompact(BaseModel):
    """Compact section object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)

class SectionProject(BaseModel):
    """Nested schema for Section.project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)

class Section(BaseModel):
    """Full section object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: Union[str, Any] = Field(default=None)
    resource_type: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    project: Union[SectionProject, Any] = Field(default=None)

class SectionResponse(BaseModel):
    """Section response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[Section, Any] = Field(default=None)

class SectionsListNextPage(BaseModel):
    """Nested schema for SectionsList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: Union[str, Any] = Field(default=None)
    path: Union[str, Any] = Field(default=None)
    uri: Union[str, Any] = Field(default=None)

class SectionsList(BaseModel):
    """Paginated list of sections containing compact section objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[SectionCompact], Any] = Field(default=None)
    next_page: Union[SectionsListNextPage | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class TasksListResultMeta(BaseModel):
    """Metadata for tasks.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class ProjectTasksListResultMeta(BaseModel):
    """Metadata for project_tasks.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class WorkspaceTaskSearchListResultMeta(BaseModel):
    """Metadata for workspace_task_search.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class ProjectsListResultMeta(BaseModel):
    """Metadata for projects.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class TaskProjectsListResultMeta(BaseModel):
    """Metadata for task_projects.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class TeamProjectsListResultMeta(BaseModel):
    """Metadata for team_projects.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class WorkspaceProjectsListResultMeta(BaseModel):
    """Metadata for workspace_projects.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class WorkspacesListResultMeta(BaseModel):
    """Metadata for workspaces.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class WorkspaceUsersListResultMeta(BaseModel):
    """Metadata for workspace_users.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class TeamUsersListResultMeta(BaseModel):
    """Metadata for team_users.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class WorkspaceTeamsListResultMeta(BaseModel):
    """Metadata for workspace_teams.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class UserTeamsListResultMeta(BaseModel):
    """Metadata for user_teams.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class AttachmentsListResultMeta(BaseModel):
    """Metadata for attachments.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class WorkspaceTagsListResultMeta(BaseModel):
    """Metadata for workspace_tags.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class ProjectSectionsListResultMeta(BaseModel):
    """Metadata for project_sections.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class TaskSubtasksListResultMeta(BaseModel):
    """Metadata for task_subtasks.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class TaskDependenciesListResultMeta(BaseModel):
    """Metadata for task_dependencies.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

class TaskDependentsListResultMeta(BaseModel):
    """Metadata for task_dependents.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[dict[str, Any] | None, Any] = Field(default=None)

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class AsanaExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class AsanaExecuteResultWithMeta(AsanaExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

TasksListResult = AsanaExecuteResultWithMeta[list[TaskCompact], TasksListResultMeta]
"""Result type for tasks.list operation with data and metadata."""

ProjectTasksListResult = AsanaExecuteResultWithMeta[list[TaskCompact], ProjectTasksListResultMeta]
"""Result type for project_tasks.list operation with data and metadata."""

TasksGetResult = AsanaExecuteResult[Task]
"""Result type for tasks.get operation."""

WorkspaceTaskSearchListResult = AsanaExecuteResultWithMeta[list[TaskCompact], WorkspaceTaskSearchListResultMeta]
"""Result type for workspace_task_search.list operation with data and metadata."""

ProjectsListResult = AsanaExecuteResultWithMeta[list[ProjectCompact], ProjectsListResultMeta]
"""Result type for projects.list operation with data and metadata."""

ProjectsGetResult = AsanaExecuteResult[Project]
"""Result type for projects.get operation."""

TaskProjectsListResult = AsanaExecuteResultWithMeta[list[ProjectCompact], TaskProjectsListResultMeta]
"""Result type for task_projects.list operation with data and metadata."""

TeamProjectsListResult = AsanaExecuteResultWithMeta[list[ProjectCompact], TeamProjectsListResultMeta]
"""Result type for team_projects.list operation with data and metadata."""

WorkspaceProjectsListResult = AsanaExecuteResultWithMeta[list[ProjectCompact], WorkspaceProjectsListResultMeta]
"""Result type for workspace_projects.list operation with data and metadata."""

WorkspacesListResult = AsanaExecuteResultWithMeta[list[WorkspaceCompact], WorkspacesListResultMeta]
"""Result type for workspaces.list operation with data and metadata."""

WorkspacesGetResult = AsanaExecuteResult[Workspace]
"""Result type for workspaces.get operation."""

UsersListResult = AsanaExecuteResultWithMeta[list[UserCompact], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

UsersGetResult = AsanaExecuteResult[User]
"""Result type for users.get operation."""

WorkspaceUsersListResult = AsanaExecuteResultWithMeta[list[UserCompact], WorkspaceUsersListResultMeta]
"""Result type for workspace_users.list operation with data and metadata."""

TeamUsersListResult = AsanaExecuteResultWithMeta[list[UserCompact], TeamUsersListResultMeta]
"""Result type for team_users.list operation with data and metadata."""

TeamsGetResult = AsanaExecuteResult[Team]
"""Result type for teams.get operation."""

WorkspaceTeamsListResult = AsanaExecuteResultWithMeta[list[TeamCompact], WorkspaceTeamsListResultMeta]
"""Result type for workspace_teams.list operation with data and metadata."""

UserTeamsListResult = AsanaExecuteResultWithMeta[list[TeamCompact], UserTeamsListResultMeta]
"""Result type for user_teams.list operation with data and metadata."""

AttachmentsListResult = AsanaExecuteResultWithMeta[list[AttachmentCompact], AttachmentsListResultMeta]
"""Result type for attachments.list operation with data and metadata."""

AttachmentsGetResult = AsanaExecuteResult[Attachment]
"""Result type for attachments.get operation."""

WorkspaceTagsListResult = AsanaExecuteResultWithMeta[list[TagCompact], WorkspaceTagsListResultMeta]
"""Result type for workspace_tags.list operation with data and metadata."""

TagsGetResult = AsanaExecuteResult[Tag]
"""Result type for tags.get operation."""

ProjectSectionsListResult = AsanaExecuteResultWithMeta[list[SectionCompact], ProjectSectionsListResultMeta]
"""Result type for project_sections.list operation with data and metadata."""

SectionsGetResult = AsanaExecuteResult[Section]
"""Result type for sections.get operation."""

TaskSubtasksListResult = AsanaExecuteResultWithMeta[list[TaskCompact], TaskSubtasksListResultMeta]
"""Result type for task_subtasks.list operation with data and metadata."""

TaskDependenciesListResult = AsanaExecuteResultWithMeta[list[TaskCompact], TaskDependenciesListResultMeta]
"""Result type for task_dependencies.list operation with data and metadata."""

TaskDependentsListResult = AsanaExecuteResultWithMeta[list[TaskCompact], TaskDependentsListResultMeta]
"""Result type for task_dependents.list operation with data and metadata."""

