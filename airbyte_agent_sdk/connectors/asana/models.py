"""
Pydantic models for asana connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
from typing import Optional

# Authentication configuration - multiple options available

class AsanaOauth2AuthConfig(BaseModel):
    """OAuth 2"""

    model_config = ConfigDict(extra="forbid")

    access_token: Optional[str] = None
    """OAuth access token for API requests"""
    refresh_token: str
    """OAuth refresh token for automatic token renewal"""
    client_id: Optional[str] = None
    """Connected App Consumer Key"""
    client_secret: Optional[str] = None
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

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class TaskCompact(BaseModel):
    """Compact task object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_subtype: str | None = Field(default=None)
    created_by: TaskCompactCreatedBy | None = Field(default=None)

class Task(BaseModel):
    """Full task object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)

class TaskResponse(BaseModel):
    """Task response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Task | None = Field(default=None)

class TasksListNextPage(BaseModel):
    """Nested schema for TasksList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: str | None = Field(default=None)
    path: str | None = Field(default=None)
    uri: str | None = Field(default=None)

class TasksList(BaseModel):
    """Paginated list of tasks containing compact task objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[TaskCompact] | None = Field(default=None)
    next_page: TasksListNextPage | None = Field(default=None)

class ProjectCompact(BaseModel):
    """Compact project object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)

class ProjectFollowersItem(BaseModel):
    """Nested schema for Project.followers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class ProjectCurrentStatusAuthor(BaseModel):
    """Nested schema for ProjectCurrentStatus.author"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class ProjectCurrentStatusCreatedBy(BaseModel):
    """Nested schema for ProjectCurrentStatus.created_by"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class ProjectCurrentStatus(BaseModel):
    """Nested schema for Project.current_status"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    author: ProjectCurrentStatusAuthor | None = Field(default=None)
    color: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    created_by: ProjectCurrentStatusCreatedBy | None = Field(default=None)
    modified_at: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    text: str | None = Field(default=None)
    title: str | None = Field(default=None)

class ProjectOwner(BaseModel):
    """Nested schema for Project.owner"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class ProjectTeam(BaseModel):
    """Nested schema for Project.team"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class ProjectWorkspace(BaseModel):
    """Nested schema for Project.workspace"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class ProjectCompletedBy(BaseModel):
    """Nested schema for Project.completed_by"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class ProjectMembersItem(BaseModel):
    """Nested schema for Project.members_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class ProjectCurrentStatusUpdate(BaseModel):
    """Nested schema for Project.current_status_update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    resource_subtype: str | None = Field(default=None)
    title: str | None = Field(default=None)

class Project(BaseModel):
    """Full project object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    archived: bool | None = Field(default=None)
    color: str | None = Field(default=None)
    completed: bool | None = Field(default=None)
    completed_at: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    current_status: ProjectCurrentStatus | None = Field(default=None)
    current_status_update: ProjectCurrentStatusUpdate | None = Field(default=None)
    custom_fields: list[Any] | None = Field(default=None)
    default_access_level: str | None = Field(default=None)
    default_view: str | None = Field(default=None)
    due_on: str | None = Field(default=None)
    due_date: str | None = Field(default=None)
    followers: list[ProjectFollowersItem] | None = Field(default=None)
    members: list[ProjectMembersItem] | None = Field(default=None)
    minimum_access_level_for_customization: str | None = Field(default=None)
    minimum_access_level_for_sharing: str | None = Field(default=None)
    modified_at: str | None = Field(default=None)
    name: str | None = Field(default=None)
    notes: str | None = Field(default=None)
    owner: ProjectOwner | None = Field(default=None)
    permalink_url: str | None = Field(default=None)
    privacy_setting: str | None = Field(default=None)
    public: bool | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    start_on: str | None = Field(default=None)
    team: ProjectTeam | None = Field(default=None)
    workspace: ProjectWorkspace | None = Field(default=None)
    icon: str | None = Field(default=None)
    completed_by: ProjectCompletedBy | None = Field(default=None)

class ProjectResponse(BaseModel):
    """Project response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Project | None = Field(default=None)

class ProjectsListNextPage(BaseModel):
    """Nested schema for ProjectsList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: str | None = Field(default=None)
    path: str | None = Field(default=None)
    uri: str | None = Field(default=None)

class ProjectsList(BaseModel):
    """Paginated list of projects containing compact project objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[ProjectCompact] | None = Field(default=None)
    next_page: ProjectsListNextPage | None = Field(default=None)

class WorkspaceCompact(BaseModel):
    """Compact workspace object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)

class Workspace(BaseModel):
    """Full workspace object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)
    email_domains: list[str] | None = Field(default=None)
    is_organization: bool | None = Field(default=None)

class WorkspaceResponse(BaseModel):
    """Workspace response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Workspace | None = Field(default=None)

class WorkspacesListNextPage(BaseModel):
    """Nested schema for WorkspacesList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: str | None = Field(default=None)
    path: str | None = Field(default=None)
    uri: str | None = Field(default=None)

class WorkspacesList(BaseModel):
    """Paginated list of workspaces containing compact workspace objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[WorkspaceCompact] | None = Field(default=None)
    next_page: WorkspacesListNextPage | None = Field(default=None)

class UserCompact(BaseModel):
    """Compact user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)

class UserWorkspacesItem(BaseModel):
    """Nested schema for User.workspaces_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class User(BaseModel):
    """Full user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    email: str | None = Field(default=None)
    name: str | None = Field(default=None)
    photo: dict[str, Any] | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    workspaces: list[UserWorkspacesItem] | None = Field(default=None)

class UserResponse(BaseModel):
    """User response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: User | None = Field(default=None)

class UsersListNextPage(BaseModel):
    """Nested schema for UsersList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: str | None = Field(default=None)
    path: str | None = Field(default=None)
    uri: str | None = Field(default=None)

class UsersList(BaseModel):
    """Paginated list of users containing compact user objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[UserCompact] | None = Field(default=None)
    next_page: UsersListNextPage | None = Field(default=None)

class TeamCompact(BaseModel):
    """Compact team object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)

class TeamOrganization(BaseModel):
    """Nested schema for Team.organization"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class Team(BaseModel):
    """Full team object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    organization: TeamOrganization | None = Field(default=None)
    permalink_url: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class TeamResponse(BaseModel):
    """Team response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Team | None = Field(default=None)

class TeamsListNextPage(BaseModel):
    """Nested schema for TeamsList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: str | None = Field(default=None)
    path: str | None = Field(default=None)
    uri: str | None = Field(default=None)

class TeamsList(BaseModel):
    """Paginated list of teams containing compact team objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[TeamCompact] | None = Field(default=None)
    next_page: TeamsListNextPage | None = Field(default=None)

class AttachmentCompact(BaseModel):
    """Compact attachment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_subtype: str | None = Field(default=None)

class AttachmentParent(BaseModel):
    """The parent object this attachment is attached to"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_subtype: str | None = Field(default=None, description="The subtype of the parent resource")
    """The subtype of the parent resource"""

class Attachment(BaseModel):
    """Full attachment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_subtype: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    download_url: str | None = Field(default=None)
    permanent_url: str | None = Field(default=None)
    host: str | None = Field(default=None)
    parent: AttachmentParent | None = Field(default=None)
    view_url: str | None = Field(default=None)
    size: int | None = Field(default=None)

class AttachmentResponse(BaseModel):
    """Attachment response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Attachment | None = Field(default=None)

class AttachmentsListNextPage(BaseModel):
    """Nested schema for AttachmentsList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: str | None = Field(default=None)
    path: str | None = Field(default=None)
    uri: str | None = Field(default=None)

class AttachmentsList(BaseModel):
    """Paginated list of attachments containing compact attachment objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[AttachmentCompact] | None = Field(default=None)
    next_page: AttachmentsListNextPage | None = Field(default=None)

class TagCompact(BaseModel):
    """Compact tag object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)

class TagWorkspace(BaseModel):
    """Nested schema for Tag.workspace"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class Tag(BaseModel):
    """Full tag object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)
    color: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    followers: list[Any] | None = Field(default=None)
    notes: str | None = Field(default=None)
    permalink_url: str | None = Field(default=None)
    workspace: TagWorkspace | None = Field(default=None)

class TagResponse(BaseModel):
    """Tag response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Tag | None = Field(default=None)

class TagsListNextPage(BaseModel):
    """Nested schema for TagsList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: str | None = Field(default=None)
    path: str | None = Field(default=None)
    uri: str | None = Field(default=None)

class TagsList(BaseModel):
    """Paginated list of tags containing compact tag objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[TagCompact] | None = Field(default=None)
    next_page: TagsListNextPage | None = Field(default=None)

class SectionCompact(BaseModel):
    """Compact section object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)

class SectionProject(BaseModel):
    """Nested schema for Section.project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class Section(BaseModel):
    """Full section object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    name: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    project: SectionProject | None = Field(default=None)

class SectionResponse(BaseModel):
    """Section response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Section | None = Field(default=None)

class SectionsListNextPage(BaseModel):
    """Nested schema for SectionsList.next_page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    offset: str | None = Field(default=None)
    path: str | None = Field(default=None)
    uri: str | None = Field(default=None)

class SectionsList(BaseModel):
    """Paginated list of sections containing compact section objects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[SectionCompact] | None = Field(default=None)
    next_page: SectionsListNextPage | None = Field(default=None)

class SectionCreateParamsData(BaseModel):
    """Nested schema for SectionCreateParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str = Field(description="The name of the section (this is displayed as the column header in board view)")
    """The name of the section (this is displayed as the column header in board view)"""
    insert_before: str | None = Field(default=None, description="GID of a section in the same project before which the new section should be inserted. Cannot be provided together with insert_after.")
    """GID of a section in the same project before which the new section should be inserted. Cannot be provided together with insert_after."""
    insert_after: str | None = Field(default=None, description="GID of a section in the same project after which the new section should be inserted. Cannot be provided together with insert_before.")
    """GID of a section in the same project after which the new section should be inserted. Cannot be provided together with insert_before."""

class SectionCreateParams(BaseModel):
    """Parameters for creating a new section in a project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: SectionCreateParamsData

class SectionUpdateParamsData(BaseModel):
    """Nested schema for SectionUpdateParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="The new name of the section")
    """The new name of the section"""

class SectionUpdateParams(BaseModel):
    """Parameters for updating an existing section"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: SectionUpdateParamsData

class SectionAddTaskParamsData(BaseModel):
    """Nested schema for SectionAddTaskParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    task: str = Field(description="The GID of the task to add to this section")
    """The GID of the task to add to this section"""
    insert_before: str | None = Field(default=None, description="GID of a task in this section before which the added task should be inserted. Cannot be provided together with insert_after.")
    """GID of a task in this section before which the added task should be inserted. Cannot be provided together with insert_after."""
    insert_after: str | None = Field(default=None, description="GID of a task in this section after which the added task should be inserted. Cannot be provided together with insert_before.")
    """GID of a task in this section after which the added task should be inserted. Cannot be provided together with insert_before."""

class SectionAddTaskParams(BaseModel):
    """Parameters for adding a task to a section"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: SectionAddTaskParamsData

class TagCreateParamsData(BaseModel):
    """Nested schema for TagCreateParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str = Field(description="Name of the tag")
    """Name of the tag"""
    color: str | None = Field(default=None, description="Color of the tag. Must be one of: dark-pink, dark-green, dark-blue, dark-red, dark-teal, dark-brown, dark-orange, dark-purple, dark-warm-gray, light-pink, light-green, light-blue, light-red, light-teal, light-brown, light-orange, light-purple, light-warm-gray, none, null")
    """Color of the tag. Must be one of: dark-pink, dark-green, dark-blue, dark-red, dark-teal, dark-brown, dark-orange, dark-purple, dark-warm-gray, light-pink, light-green, light-blue, light-red, light-teal, light-brown, light-orange, light-purple, light-warm-gray, none, null"""
    notes: str | None = Field(default=None, description="Free-form textual description of the tag")
    """Free-form textual description of the tag"""

class TagCreateParams(BaseModel):
    """Parameters for creating a new tag in a workspace"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: TagCreateParamsData

class TagUpdateParamsData(BaseModel):
    """Nested schema for TagUpdateParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="Name of the tag")
    """Name of the tag"""
    color: str | None = Field(default=None, description="Color of the tag")
    """Color of the tag"""
    notes: str | None = Field(default=None, description="Free-form textual description of the tag")
    """Free-form textual description of the tag"""

class TagUpdateParams(BaseModel):
    """Parameters for updating an existing tag"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: TagUpdateParamsData

class TaskAddTagParamsData(BaseModel):
    """Nested schema for TaskAddTagParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tag: str = Field(description="The GID of the tag to add to the task")
    """The GID of the tag to add to the task"""

class TaskAddTagParams(BaseModel):
    """Parameters for adding a tag to a task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: TaskAddTagParamsData

class TaskRemoveTagParamsData(BaseModel):
    """Nested schema for TaskRemoveTagParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tag: str = Field(description="The GID of the tag to remove from the task")
    """The GID of the tag to remove from the task"""

class TaskRemoveTagParams(BaseModel):
    """Parameters for removing a tag from a task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: TaskRemoveTagParamsData

class TaskCreateParamsData(BaseModel):
    """Nested schema for TaskCreateParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str = Field(description="Name of the task")
    """Name of the task"""
    workspace: str = Field(description="GID of the workspace to create the task in")
    """GID of the workspace to create the task in"""
    projects: list[str] | None = Field(default=None, description="Array of project GIDs to add the task to")
    """Array of project GIDs to add the task to"""
    assignee: str | None = Field(default=None, description="GID of the user to assign the task to, or 'me' for the current user")
    """GID of the user to assign the task to, or 'me' for the current user"""
    notes: str | None = Field(default=None, description="Free-form textual description of the task (plain text, no formatting)")
    """Free-form textual description of the task (plain text, no formatting)"""
    html_notes: str | None = Field(default=None, description="HTML-formatted description of the task")
    """HTML-formatted description of the task"""
    due_on: str | None = Field(default=None, description="Due date in YYYY-MM-DD format")
    """Due date in YYYY-MM-DD format"""
    due_at: str | None = Field(default=None, description="Due date and time in ISO 8601 format (e.g., 2025-03-20T12:00:00.000Z)")
    """Due date and time in ISO 8601 format (e.g., 2025-03-20T12:00:00.000Z)"""
    start_on: str | None = Field(default=None, description="Start date in YYYY-MM-DD format")
    """Start date in YYYY-MM-DD format"""
    completed: bool | None = Field(default=None, description="Whether the task is completed")
    """Whether the task is completed"""
    parent: str | None = Field(default=None, description="GID of the parent task (to create a subtask)")
    """GID of the parent task (to create a subtask)"""
    tags: list[str] | None = Field(default=None, description="Array of tag GIDs to add to the task")
    """Array of tag GIDs to add to the task"""
    followers: list[str] | None = Field(default=None, description="Array of user GIDs to add as followers")
    """Array of user GIDs to add as followers"""
    resource_subtype: str | None = Field(default=None, description="The subtype of the task: default_task, milestone, section, or approval")
    """The subtype of the task: default_task, milestone, section, or approval"""

class TaskCreateParams(BaseModel):
    """Parameters for creating a new task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: TaskCreateParamsData

class TaskUpdateParamsData(BaseModel):
    """Nested schema for TaskUpdateParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="Name of the task")
    """Name of the task"""
    assignee: str | None = Field(default=None, description="GID of the user to assign the task to, or 'me' for the current user")
    """GID of the user to assign the task to, or 'me' for the current user"""
    notes: str | None = Field(default=None, description="Free-form textual description of the task (plain text, no formatting)")
    """Free-form textual description of the task (plain text, no formatting)"""
    html_notes: str | None = Field(default=None, description="HTML-formatted description of the task")
    """HTML-formatted description of the task"""
    due_on: str | None = Field(default=None, description="Due date in YYYY-MM-DD format")
    """Due date in YYYY-MM-DD format"""
    due_at: str | None = Field(default=None, description="Due date and time in ISO 8601 format (e.g., 2025-03-20T12:00:00.000Z)")
    """Due date and time in ISO 8601 format (e.g., 2025-03-20T12:00:00.000Z)"""
    start_on: str | None = Field(default=None, description="Start date in YYYY-MM-DD format")
    """Start date in YYYY-MM-DD format"""
    completed: bool | None = Field(default=None, description="Whether the task is completed")
    """Whether the task is completed"""

class TaskUpdateParams(BaseModel):
    """Parameters for updating an existing task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: TaskUpdateParamsData

class ProjectCreateParamsData(BaseModel):
    """Nested schema for ProjectCreateParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str = Field(description="Name of the project")
    """Name of the project"""
    workspace: str = Field(description="GID of the workspace to create the project in")
    """GID of the workspace to create the project in"""
    team: str | None = Field(default=None, description="GID of the team to share the project with (required for organizations)")
    """GID of the team to share the project with (required for organizations)"""
    notes: str | None = Field(default=None, description="Free-form textual description of the project (plain text)")
    """Free-form textual description of the project (plain text)"""
    html_notes: str | None = Field(default=None, description="HTML-formatted description of the project")
    """HTML-formatted description of the project"""
    color: str | None = Field(default=None, description="Color of the project (e.g., dark-pink, dark-green, dark-blue, dark-red, dark-teal, dark-brown, dark-orange, dark-purple, dark-warm-gray, light-pink, light-green, light-blue, light-red, light-teal, light-brown, light-orange, light-purple, light-warm-gray, none)")
    """Color of the project (e.g., dark-pink, dark-green, dark-blue, dark-red, dark-teal, dark-brown, dark-orange, dark-purple, dark-warm-gray, light-pink, light-green, light-blue, light-red, light-teal, light-brown, light-orange, light-purple, light-warm-gray, none)"""
    default_view: str | None = Field(default=None, description="The default view of the project (list, board, calendar, timeline)")
    """The default view of the project (list, board, calendar, timeline)"""
    due_on: str | None = Field(default=None, description="Due date in YYYY-MM-DD format")
    """Due date in YYYY-MM-DD format"""
    start_on: str | None = Field(default=None, description="Start date in YYYY-MM-DD format")
    """Start date in YYYY-MM-DD format"""
    privacy_setting: str | None = Field(default=None, description="Privacy setting: public_to_workspace or private")
    """Privacy setting: public_to_workspace or private"""
    archived: bool | None = Field(default=None, description="Whether the project is archived")
    """Whether the project is archived"""

class ProjectCreateParams(BaseModel):
    """Parameters for creating a new project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: ProjectCreateParamsData

class ProjectUpdateParamsData(BaseModel):
    """Nested schema for ProjectUpdateParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="Name of the project")
    """Name of the project"""
    notes: str | None = Field(default=None, description="Free-form textual description of the project (plain text)")
    """Free-form textual description of the project (plain text)"""
    html_notes: str | None = Field(default=None, description="HTML-formatted description of the project")
    """HTML-formatted description of the project"""
    color: str | None = Field(default=None, description="Color of the project")
    """Color of the project"""
    default_view: str | None = Field(default=None, description="The default view of the project (list, board, calendar, timeline)")
    """The default view of the project (list, board, calendar, timeline)"""
    due_on: str | None = Field(default=None, description="Due date in YYYY-MM-DD format")
    """Due date in YYYY-MM-DD format"""
    start_on: str | None = Field(default=None, description="Start date in YYYY-MM-DD format")
    """Start date in YYYY-MM-DD format"""
    archived: bool | None = Field(default=None, description="Whether the project is archived")
    """Whether the project is archived"""

class ProjectUpdateParams(BaseModel):
    """Parameters for updating an existing project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: ProjectUpdateParamsData

class StoryCreateParamsData(BaseModel):
    """Nested schema for StoryCreateParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    text: str = Field(description="The plain text body of the comment")
    """The plain text body of the comment"""
    html_text: str | None = Field(default=None, description="HTML-formatted body of the comment")
    """HTML-formatted body of the comment"""
    is_pinned: bool | None = Field(default=None, description="Whether the story should be pinned on the resource")
    """Whether the story should be pinned on the resource"""

class StoryCreateParams(BaseModel):
    """Parameters for creating a comment (story) on a task"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: StoryCreateParamsData

class StoryCreatedBy(BaseModel):
    """Nested schema for Story.created_by"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class StoryTarget(BaseModel):
    """Nested schema for Story.target"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    name: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)

class Story(BaseModel):
    """A story represents an activity associated with an object in Asana"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    gid: str | None = Field(default=None)
    resource_type: str | None = Field(default=None)
    resource_subtype: str | None = Field(default=None)
    text: str | None = Field(default=None)
    html_text: str | None = Field(default=None)
    is_pinned: bool | None = Field(default=None)
    created_at: str | None = Field(default=None)
    created_by: StoryCreatedBy | None = Field(default=None)
    target: StoryTarget | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")

class StoryResponse(BaseModel):
    """Story response wrapper"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Story | None = Field(default=None)

class EmptyResponse(BaseModel):
    """Empty response returned by delete operations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: dict[str, Any] | None = Field(default=None)

class WorkspaceAddUserParamsData(BaseModel):
    """Nested schema for WorkspaceAddUserParams.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user: str = Field(description="A user GID or email address to add to the workspace")
    """A user GID or email address to add to the workspace"""

class WorkspaceAddUserParams(BaseModel):
    """Parameters for adding a user to a workspace or organization"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: WorkspaceAddUserParamsData

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class TasksListResultMeta(BaseModel):
    """Metadata for tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class ProjectTasksListResultMeta(BaseModel):
    """Metadata for project_tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class WorkspaceTaskSearchListResultMeta(BaseModel):
    """Metadata for workspace_task_search.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class ProjectsListResultMeta(BaseModel):
    """Metadata for projects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class TaskProjectsListResultMeta(BaseModel):
    """Metadata for task_projects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class TeamProjectsListResultMeta(BaseModel):
    """Metadata for team_projects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class WorkspaceProjectsListResultMeta(BaseModel):
    """Metadata for workspace_projects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class WorkspacesListResultMeta(BaseModel):
    """Metadata for workspaces.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class WorkspaceUsersListResultMeta(BaseModel):
    """Metadata for workspace_users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class TeamUsersListResultMeta(BaseModel):
    """Metadata for team_users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class WorkspaceTeamsListResultMeta(BaseModel):
    """Metadata for workspace_teams.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class UserTeamsListResultMeta(BaseModel):
    """Metadata for user_teams.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class AttachmentsListResultMeta(BaseModel):
    """Metadata for attachments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class WorkspaceTagsListResultMeta(BaseModel):
    """Metadata for workspace_tags.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class TagTasksListResultMeta(BaseModel):
    """Metadata for tag_tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class ProjectSectionsListResultMeta(BaseModel):
    """Metadata for project_sections.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class SectionTasksListResultMeta(BaseModel):
    """Metadata for section_tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class TaskSubtasksListResultMeta(BaseModel):
    """Metadata for task_subtasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class TaskDependenciesListResultMeta(BaseModel):
    """Metadata for task_dependencies.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

class TaskDependentsListResultMeta(BaseModel):
    """Metadata for task_dependents.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: dict[str, Any] | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class AsanaCheckResult(BaseModel):
    """Result of a health check operation.

    Returned by the check() method to indicate connectivity and credential status.
    """
    model_config = ConfigDict(extra="forbid")

    status: str
    """Health check status: 'healthy' or 'unhealthy'."""
    error: str | None = None
    """Error message if status is 'unhealthy', None otherwise."""
    checked_entity: str | None = None
    """Entity name used for the health check."""
    checked_action: str | None = None
    """Action name used for the health check."""


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

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AttachmentsSearchData(BaseModel):
    """Search result data for attachments entity."""
    model_config = ConfigDict(extra="allow")

    connected_to_app: bool | None = None
    """"""
    created_at: str | None = None
    """"""
    download_url: str | None = None
    """"""
    gid: str | None = None
    """"""
    host: str | None = None
    """"""
    name: str | None = None
    """"""
    parent: dict[str, Any] | None = None
    """"""
    permanent_url: str | None = None
    """"""
    resource_subtype: str | None = None
    """"""
    resource_type: str | None = None
    """"""
    size: int | None = None
    """"""
    view_url: str | None = None
    """"""


class ProjectsSearchData(BaseModel):
    """Search result data for projects entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """"""
    color: str | None = None
    """"""
    created_at: str | None = None
    """"""
    current_status: dict[str, Any] | None = None
    """"""
    custom_field_settings: list[Any] | None = None
    """"""
    custom_fields: list[Any] | None = None
    """"""
    default_view: str | None = None
    """"""
    due_date: str | None = None
    """"""
    due_on: str | None = None
    """"""
    followers: list[Any] | None = None
    """"""
    gid: str | None = None
    """"""
    html_notes: str | None = None
    """"""
    icon: str | None = None
    """"""
    is_template: bool | None = None
    """"""
    members: list[Any] | None = None
    """"""
    modified_at: str | None = None
    """"""
    name: str | None = None
    """"""
    notes: str | None = None
    """"""
    owner: dict[str, Any] | None = None
    """"""
    permalink_url: str | None = None
    """"""
    public: bool | None = None
    """"""
    resource_type: str | None = None
    """"""
    start_on: str | None = None
    """"""
    team: dict[str, Any] | None = None
    """"""
    workspace: dict[str, Any] | None = None
    """"""


class SectionsSearchData(BaseModel):
    """Search result data for sections entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """"""
    gid: str | None = None
    """"""
    name: str | None = None
    """"""
    project: dict[str, Any] | None = None
    """"""
    resource_type: str | None = None
    """"""


class TagsSearchData(BaseModel):
    """Search result data for tags entity."""
    model_config = ConfigDict(extra="allow")

    color: str | None = None
    """"""
    followers: list[Any] | None = None
    """"""
    gid: str | None = None
    """"""
    name: str | None = None
    """"""
    permalink_url: str | None = None
    """"""
    resource_type: str | None = None
    """"""
    workspace: dict[str, Any] | None = None
    """"""


class TasksSearchData(BaseModel):
    """Search result data for tasks entity."""
    model_config = ConfigDict(extra="allow")

    actual_time_minutes: int | None = None
    """The actual time spent on the task in minutes"""
    approval_status: str | None = None
    """"""
    assignee: dict[str, Any] | None = None
    """"""
    completed: bool | None = None
    """"""
    completed_at: str | None = None
    """"""
    completed_by: dict[str, Any] | None = None
    """"""
    created_at: str | None = None
    """"""
    custom_fields: list[Any] | None = None
    """"""
    dependencies: list[Any] | None = None
    """"""
    dependents: list[Any] | None = None
    """"""
    due_at: str | None = None
    """"""
    due_on: str | None = None
    """"""
    external: dict[str, Any] | None = None
    """"""
    followers: list[Any] | None = None
    """"""
    gid: str | None = None
    """"""
    hearted: bool | None = None
    """"""
    hearts: list[Any] | None = None
    """"""
    html_notes: str | None = None
    """"""
    is_rendered_as_separator: bool | None = None
    """"""
    liked: bool | None = None
    """"""
    likes: list[Any] | None = None
    """"""
    memberships: list[Any] | None = None
    """"""
    modified_at: str | None = None
    """"""
    name: str | None = None
    """"""
    notes: str | None = None
    """"""
    num_hearts: int | None = None
    """"""
    num_likes: int | None = None
    """"""
    num_subtasks: int | None = None
    """"""
    parent: dict[str, Any] | None = None
    """"""
    permalink_url: str | None = None
    """"""
    projects: list[Any] | None = None
    """"""
    resource_subtype: str | None = None
    """"""
    resource_type: str | None = None
    """"""
    start_on: str | None = None
    """"""
    tags: list[Any] | None = None
    """"""
    workspace: dict[str, Any] | None = None
    """"""


class TeamsSearchData(BaseModel):
    """Search result data for teams entity."""
    model_config = ConfigDict(extra="allow")

    description: str | None = None
    """"""
    gid: str | None = None
    """"""
    html_description: str | None = None
    """"""
    name: str | None = None
    """"""
    organization: dict[str, Any] | None = None
    """"""
    permalink_url: str | None = None
    """"""
    resource_type: str | None = None
    """"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    email: str | None = None
    """"""
    gid: str | None = None
    """"""
    name: str | None = None
    """"""
    photo: dict[str, Any] | None = None
    """"""
    resource_type: str | None = None
    """"""
    workspaces: list[Any] | None = None
    """"""


class WorkspacesSearchData(BaseModel):
    """Search result data for workspaces entity."""
    model_config = ConfigDict(extra="allow")

    email_domains: list[Any] | None = None
    """"""
    gid: str | None = None
    """"""
    is_organization: bool | None = None
    """"""
    name: str | None = None
    """"""
    resource_type: str | None = None
    """"""


# ===== GENERIC SEARCH RESULT TYPES =====

class AirbyteSearchMeta(BaseModel):
    """Pagination metadata for search responses."""
    model_config = ConfigDict(extra="allow")

    has_more: bool = False
    """Whether more results are available."""
    cursor: str | None = None
    """Cursor for fetching the next page of results."""
    took_ms: int | None = None
    """Time taken to execute the search in milliseconds."""


class AirbyteSearchResult(BaseModel, Generic[D]):
    """Result from Airbyte cache search operations with typed records."""
    model_config = ConfigDict(extra="allow")

    data: list[D] = Field(default_factory=list)
    """List of matching records."""
    meta: AirbyteSearchMeta = Field(default_factory=AirbyteSearchMeta)
    """Pagination metadata."""


# ===== ENTITY-SPECIFIC SEARCH RESULT TYPE ALIASES =====

AttachmentsSearchResult = AirbyteSearchResult[AttachmentsSearchData]
"""Search result type for attachments entity."""

ProjectsSearchResult = AirbyteSearchResult[ProjectsSearchData]
"""Search result type for projects entity."""

SectionsSearchResult = AirbyteSearchResult[SectionsSearchData]
"""Search result type for sections entity."""

TagsSearchResult = AirbyteSearchResult[TagsSearchData]
"""Search result type for tags entity."""

TasksSearchResult = AirbyteSearchResult[TasksSearchData]
"""Search result type for tasks entity."""

TeamsSearchResult = AirbyteSearchResult[TeamsSearchData]
"""Search result type for teams entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""

WorkspacesSearchResult = AirbyteSearchResult[WorkspacesSearchData]
"""Search result type for workspaces entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

TasksListResult = AsanaExecuteResultWithMeta[list[TaskCompact], TasksListResultMeta]
"""Result type for tasks.list operation with data and metadata."""

ProjectTasksListResult = AsanaExecuteResultWithMeta[list[TaskCompact], ProjectTasksListResultMeta]
"""Result type for project_tasks.list operation with data and metadata."""

WorkspaceTaskSearchListResult = AsanaExecuteResultWithMeta[list[TaskCompact], WorkspaceTaskSearchListResultMeta]
"""Result type for workspace_task_search.list operation with data and metadata."""

ProjectsListResult = AsanaExecuteResultWithMeta[list[ProjectCompact], ProjectsListResultMeta]
"""Result type for projects.list operation with data and metadata."""

TaskProjectsListResult = AsanaExecuteResultWithMeta[list[ProjectCompact], TaskProjectsListResultMeta]
"""Result type for task_projects.list operation with data and metadata."""

TeamProjectsListResult = AsanaExecuteResultWithMeta[list[ProjectCompact], TeamProjectsListResultMeta]
"""Result type for team_projects.list operation with data and metadata."""

WorkspaceProjectsListResult = AsanaExecuteResultWithMeta[list[ProjectCompact], WorkspaceProjectsListResultMeta]
"""Result type for workspace_projects.list operation with data and metadata."""

WorkspacesListResult = AsanaExecuteResultWithMeta[list[WorkspaceCompact], WorkspacesListResultMeta]
"""Result type for workspaces.list operation with data and metadata."""

UsersListResult = AsanaExecuteResultWithMeta[list[UserCompact], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

WorkspaceUsersListResult = AsanaExecuteResultWithMeta[list[UserCompact], WorkspaceUsersListResultMeta]
"""Result type for workspace_users.list operation with data and metadata."""

TeamUsersListResult = AsanaExecuteResultWithMeta[list[UserCompact], TeamUsersListResultMeta]
"""Result type for team_users.list operation with data and metadata."""

WorkspaceTeamsListResult = AsanaExecuteResultWithMeta[list[TeamCompact], WorkspaceTeamsListResultMeta]
"""Result type for workspace_teams.list operation with data and metadata."""

UserTeamsListResult = AsanaExecuteResultWithMeta[list[TeamCompact], UserTeamsListResultMeta]
"""Result type for user_teams.list operation with data and metadata."""

AttachmentsListResult = AsanaExecuteResultWithMeta[list[AttachmentCompact], AttachmentsListResultMeta]
"""Result type for attachments.list operation with data and metadata."""

WorkspaceTagsListResult = AsanaExecuteResultWithMeta[list[TagCompact], WorkspaceTagsListResultMeta]
"""Result type for workspace_tags.list operation with data and metadata."""

TagTasksListResult = AsanaExecuteResultWithMeta[list[TaskCompact], TagTasksListResultMeta]
"""Result type for tag_tasks.list operation with data and metadata."""

ProjectSectionsListResult = AsanaExecuteResultWithMeta[list[SectionCompact], ProjectSectionsListResultMeta]
"""Result type for project_sections.list operation with data and metadata."""

SectionTasksListResult = AsanaExecuteResultWithMeta[list[TaskCompact], SectionTasksListResultMeta]
"""Result type for section_tasks.list operation with data and metadata."""

TaskSubtasksListResult = AsanaExecuteResultWithMeta[list[TaskCompact], TaskSubtasksListResultMeta]
"""Result type for task_subtasks.list operation with data and metadata."""

TaskDependenciesListResult = AsanaExecuteResultWithMeta[list[TaskCompact], TaskDependenciesListResultMeta]
"""Result type for task_dependencies.list operation with data and metadata."""

TaskDependentsListResult = AsanaExecuteResultWithMeta[list[TaskCompact], TaskDependentsListResultMeta]
"""Result type for task_dependents.list operation with data and metadata."""

