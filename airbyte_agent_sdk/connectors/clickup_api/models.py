"""
Pydantic models for clickup-api connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class ClickupApiAuthConfig(BaseModel):
    """API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your ClickUp personal API token"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class User(BaseModel):
    """User type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    username: str | None = Field(default=None)
    email: str | None = Field(default=None)
    color: str | None = Field(default=None)
    profile_picture: str | None = Field(default=None, alias="profilePicture")
    initials: str | None = Field(default=None)
    week_start_day: int | None = Field(default=None)
    global_font_support: bool | None = Field(default=None)
    timezone: str | None = Field(default=None)

class UserResponse(BaseModel):
    """UserResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user: User | None = Field(default=None)

class TeamMembersItemUser(BaseModel):
    """Member user details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None, description="User ID")
    """User ID"""
    username: str | None = Field(default=None, description="Username")
    """Username"""
    email: str | None = Field(default=None, description="Email address")
    """Email address"""
    color: str | None | None = Field(default=None, description="Avatar color")
    """Avatar color"""
    profile_picture: str | None | None = Field(default=None, alias="profilePicture", description="Profile picture URL")
    """Profile picture URL"""
    initials: str | None | None = Field(default=None, description="User initials")
    """User initials"""
    role: int | None | None = Field(default=None, description="User role ID")
    """User role ID"""
    role_subtype: int | None | None = Field(default=None, description="User role subtype")
    """User role subtype"""
    role_key: str | None | None = Field(default=None, description="Role key name")
    """Role key name"""
    custom_role: dict[str, Any] | None | None = Field(default=None, description="Custom role details")
    """Custom role details"""
    last_active: str | None | None = Field(default=None, description="Last active timestamp (Unix ms)")
    """Last active timestamp (Unix ms)"""
    date_joined: str | None | None = Field(default=None, description="Date joined (Unix ms)")
    """Date joined (Unix ms)"""
    date_invited: str | None | None = Field(default=None, description="Date invited (Unix ms)")
    """Date invited (Unix ms)"""

class TeamMembersItem(BaseModel):
    """Nested schema for Team.members_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user: TeamMembersItemUser | None = Field(default=None, description="Member user details")
    """Member user details"""

class Team(BaseModel):
    """Team type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    color: str | None = Field(default=None)
    avatar: str | None = Field(default=None)
    members: list[TeamMembersItem] | None = Field(default=None)

class TeamsListResponse(BaseModel):
    """TeamsListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    teams: list[Team] | None = Field(default=None)

class SpaceFeaturesCustomItems(BaseModel):
    """Custom items feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether custom items are enabled")
    """Whether custom items are enabled"""

class SpaceFeaturesDependencyWarning(BaseModel):
    """Dependency warning feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether dependency warnings are enabled")
    """Whether dependency warnings are enabled"""

class SpaceFeaturesTimeTracking(BaseModel):
    """Time tracking feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether time tracking is enabled")
    """Whether time tracking is enabled"""
    harvest: bool | None = Field(default=None, description="Whether Harvest integration is enabled")
    """Whether Harvest integration is enabled"""
    rollup: bool | None = Field(default=None, description="Whether time rollup is enabled")
    """Whether time rollup is enabled"""
    default_to_billable: int | None | None = Field(default=None, description="Default billable setting")
    """Default billable setting"""

class SpaceFeaturesTags(BaseModel):
    """Tags feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether tags are enabled")
    """Whether tags are enabled"""

class SpaceFeaturesPrioritiesPrioritiesItem(BaseModel):
    """Nested schema for SpaceFeaturesPriorities.priorities_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str | None = Field(default=None, description="Priority color hex code")
    """Priority color hex code"""
    id: str | None = Field(default=None, description="Priority ID")
    """Priority ID"""
    orderindex: str | None = Field(default=None, description="Priority order index")
    """Priority order index"""
    priority: str | None = Field(default=None, description="Priority name")
    """Priority name"""

class SpaceFeaturesPriorities(BaseModel):
    """Priorities feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether priorities are enabled")
    """Whether priorities are enabled"""
    priorities: list[SpaceFeaturesPrioritiesPrioritiesItem] | None = Field(default=None, description="Priority levels")
    """Priority levels"""

class SpaceFeaturesRescheduleClosedDependencies(BaseModel):
    """Reschedule closed dependencies settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether rescheduling closed dependencies is enabled")
    """Whether rescheduling closed dependencies is enabled"""

class SpaceFeaturesDependencyEnforcement(BaseModel):
    """Dependency enforcement settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enforcement_enabled: bool | None = Field(default=None, description="Whether enforcement is enabled")
    """Whether enforcement is enabled"""
    enforcement_mode: int | None | None = Field(default=None, description="Enforcement mode")
    """Enforcement mode"""

class SpaceFeaturesTimeEstimates(BaseModel):
    """Time estimates feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether time estimates are enabled")
    """Whether time estimates are enabled"""
    rollup: bool | None = Field(default=None, description="Whether time estimate rollup is enabled")
    """Whether time estimate rollup is enabled"""
    per_assignee: bool | None = Field(default=None, description="Whether per-assignee estimates are enabled")
    """Whether per-assignee estimates are enabled"""

class SpaceFeaturesCustomFields(BaseModel):
    """Custom fields feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether custom fields are enabled")
    """Whether custom fields are enabled"""

class SpaceFeaturesMilestones(BaseModel):
    """Milestones feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether milestones are enabled")
    """Whether milestones are enabled"""

class SpaceFeaturesCheckUnresolved(BaseModel):
    """Check unresolved feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether check unresolved is enabled")
    """Whether check unresolved is enabled"""
    subtasks: bool | None | None = Field(default=None, description="Check unresolved subtasks")
    """Check unresolved subtasks"""
    checklists: bool | None | None = Field(default=None, description="Check unresolved checklists")
    """Check unresolved checklists"""
    comments: bool | None | None = Field(default=None, description="Check unresolved comments")
    """Check unresolved comments"""

class SpaceFeaturesStatusPies(BaseModel):
    """Status pies feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether status pies are enabled")
    """Whether status pies are enabled"""

class SpaceFeaturesMultipleAssignees(BaseModel):
    """Multiple assignees feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether multiple assignees are enabled")
    """Whether multiple assignees are enabled"""

class SpaceFeaturesEmails(BaseModel):
    """Emails feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether emails are enabled")
    """Whether emails are enabled"""

class SpaceFeaturesPoints(BaseModel):
    """Points feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether points are enabled")
    """Whether points are enabled"""

class SpaceFeaturesRemapDependencies(BaseModel):
    """Remap dependencies feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether remap dependencies is enabled")
    """Whether remap dependencies is enabled"""

class SpaceFeaturesSprints(BaseModel):
    """Sprints feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether sprints are enabled")
    """Whether sprints are enabled"""

class SpaceFeaturesDueDates(BaseModel):
    """Due dates feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Whether due dates are enabled")
    """Whether due dates are enabled"""
    start_date: bool | None = Field(default=None, description="Whether start dates are enabled")
    """Whether start dates are enabled"""
    remap_due_dates: bool | None = Field(default=None, description="Whether due dates are remapped")
    """Whether due dates are remapped"""
    remap_closed_due_date: bool | None = Field(default=None, description="Whether closed due dates are remapped")
    """Whether closed due dates are remapped"""

class SpaceFeatures(BaseModel):
    """Feature flags for the space"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    due_dates: SpaceFeaturesDueDates | None = Field(default=None, description="Due dates feature settings")
    """Due dates feature settings"""
    sprints: SpaceFeaturesSprints | None = Field(default=None, description="Sprints feature settings")
    """Sprints feature settings"""
    time_tracking: SpaceFeaturesTimeTracking | None = Field(default=None, description="Time tracking feature settings")
    """Time tracking feature settings"""
    points: SpaceFeaturesPoints | None = Field(default=None, description="Points feature settings")
    """Points feature settings"""
    custom_items: SpaceFeaturesCustomItems | None = Field(default=None, description="Custom items feature settings")
    """Custom items feature settings"""
    priorities: SpaceFeaturesPriorities | None = Field(default=None, description="Priorities feature settings")
    """Priorities feature settings"""
    tags: SpaceFeaturesTags | None = Field(default=None, description="Tags feature settings")
    """Tags feature settings"""
    time_estimates: SpaceFeaturesTimeEstimates | None = Field(default=None, description="Time estimates feature settings")
    """Time estimates feature settings"""
    check_unresolved: SpaceFeaturesCheckUnresolved | None = Field(default=None, description="Check unresolved feature settings")
    """Check unresolved feature settings"""
    milestones: SpaceFeaturesMilestones | None = Field(default=None, description="Milestones feature settings")
    """Milestones feature settings"""
    custom_fields: SpaceFeaturesCustomFields | None = Field(default=None, description="Custom fields feature settings")
    """Custom fields feature settings"""
    remap_dependencies: SpaceFeaturesRemapDependencies | None = Field(default=None, description="Remap dependencies feature settings")
    """Remap dependencies feature settings"""
    dependency_warning: SpaceFeaturesDependencyWarning | None = Field(default=None, description="Dependency warning feature settings")
    """Dependency warning feature settings"""
    status_pies: SpaceFeaturesStatusPies | None = Field(default=None, description="Status pies feature settings")
    """Status pies feature settings"""
    multiple_assignees: SpaceFeaturesMultipleAssignees | None = Field(default=None, description="Multiple assignees feature settings")
    """Multiple assignees feature settings"""
    emails: SpaceFeaturesEmails | None = Field(default=None, description="Emails feature settings")
    """Emails feature settings"""
    scheduler_enabled: bool | None = Field(default=None, description="Whether scheduler is enabled")
    """Whether scheduler is enabled"""
    dependency_type_enabled: bool | None = Field(default=None, description="Whether dependency types are enabled")
    """Whether dependency types are enabled"""
    dependency_enforcement: SpaceFeaturesDependencyEnforcement | None = Field(default=None, description="Dependency enforcement settings")
    """Dependency enforcement settings"""
    reschedule_closed_dependencies: SpaceFeaturesRescheduleClosedDependencies | None = Field(default=None, description="Reschedule closed dependencies settings")
    """Reschedule closed dependencies settings"""

class SpaceStatusesItem(BaseModel):
    """Nested schema for Space.statuses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Status ID")
    """Status ID"""
    status: str | None = Field(default=None, description="Status name")
    """Status name"""
    type_: str | None = Field(default=None, alias="type", description="Status type (open, custom, closed)")
    """Status type (open, custom, closed)"""
    orderindex: int | None = Field(default=None, description="Status order index")
    """Status order index"""
    color: str | None = Field(default=None, description="Status color hex code")
    """Status color hex code"""

class Space(BaseModel):
    """Space type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    private: bool | None = Field(default=None)
    color: str | None = Field(default=None)
    avatar: str | None = Field(default=None)
    admin_can_manage: bool | None = Field(default=None)
    statuses: list[SpaceStatusesItem] | None = Field(default=None)
    multiple_assignees: bool | None = Field(default=None)
    features: SpaceFeatures | None = Field(default=None)
    archived: bool | None = Field(default=None)

class SpacesListResponse(BaseModel):
    """SpacesListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    spaces: list[Space] | None = Field(default=None)

class FolderListsItemStatusesItem(BaseModel):
    """Nested schema for FolderListsItem.statuses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Status ID")
    """Status ID"""
    status: str | None = Field(default=None, description="Status name")
    """Status name"""
    type_: str | None = Field(default=None, alias="type", description="Status type (open, custom, closed)")
    """Status type (open, custom, closed)"""
    orderindex: int | None = Field(default=None, description="Status order index")
    """Status order index"""
    color: str | None = Field(default=None, description="Status color hex code")
    """Status color hex code"""
    status_group: str | None | None = Field(default=None, description="Status group identifier")
    """Status group identifier"""

class FolderListsItem(BaseModel):
    """Nested schema for Folder.lists_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="List ID")
    """List ID"""
    name: str | None = Field(default=None, description="List name")
    """List name"""
    orderindex: int | None | None = Field(default=None, description="Sort order index")
    """Sort order index"""
    content: str | None | None = Field(default=None, description="List description")
    """List description"""
    status: dict[str, Any] | None | None = Field(default=None, description="List status")
    """List status"""
    priority: dict[str, Any] | None | None = Field(default=None, description="List priority")
    """List priority"""
    assignee: dict[str, Any] | None | None = Field(default=None, description="List assignee")
    """List assignee"""
    task_count: int | None | None = Field(default=None, description="Number of tasks")
    """Number of tasks"""
    due_date: str | None | None = Field(default=None, description="Due date (Unix ms)")
    """Due date (Unix ms)"""
    start_date: str | None | None = Field(default=None, description="Start date (Unix ms)")
    """Start date (Unix ms)"""
    space: dict[str, Any] | None | None = Field(default=None, description="Parent space reference")
    """Parent space reference"""
    archived: bool | None | None = Field(default=None, description="Whether the list is archived")
    """Whether the list is archived"""
    override_statuses: bool | None | None = Field(default=None, description="Whether list overrides statuses")
    """Whether list overrides statuses"""
    statuses: list[FolderListsItemStatusesItem] | None = Field(default=None, description="List statuses")
    """List statuses"""
    permission_level: str | None | None = Field(default=None, description="User permission level")
    """User permission level"""

class FolderStatusesItem(BaseModel):
    """Nested schema for Folder.statuses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Status ID")
    """Status ID"""
    status: str | None = Field(default=None, description="Status name")
    """Status name"""
    type_: str | None = Field(default=None, alias="type", description="Status type (open, custom, closed)")
    """Status type (open, custom, closed)"""
    orderindex: int | None = Field(default=None, description="Status order index")
    """Status order index"""
    color: str | None = Field(default=None, description="Status color hex code")
    """Status color hex code"""

class FolderSpace(BaseModel):
    """Parent space reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Space ID")
    """Space ID"""
    name: str | None = Field(default=None, description="Space name")
    """Space name"""
    access: bool | None | None = Field(default=None, description="Whether user has access")
    """Whether user has access"""

class Folder(BaseModel):
    """Folder type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    orderindex: int | None = Field(default=None)
    override_statuses: bool | None = Field(default=None)
    hidden: bool | None = Field(default=None)
    space: FolderSpace | None = Field(default=None)
    task_count: str | None = Field(default=None)
    archived: bool | None = Field(default=None)
    statuses: list[FolderStatusesItem] | None = Field(default=None)
    deleted: bool | None = Field(default=None)
    lists: list[FolderListsItem] | None = Field(default=None)
    permission_level: str | None = Field(default=None)

class FoldersListResponse(BaseModel):
    """FoldersListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    folders: list[Folder] | None = Field(default=None)

class ListStatusesItem(BaseModel):
    """Nested schema for List.statuses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Status ID")
    """Status ID"""
    status: str | None = Field(default=None, description="Status name")
    """Status name"""
    type_: str | None = Field(default=None, alias="type", description="Status type (open, custom, closed)")
    """Status type (open, custom, closed)"""
    orderindex: int | None = Field(default=None, description="Status order index")
    """Status order index"""
    color: str | None = Field(default=None, description="Status color hex code")
    """Status color hex code"""
    status_group: str | None | None = Field(default=None, description="Status group identifier")
    """Status group identifier"""

class ListSpace(BaseModel):
    """Parent space reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Space ID")
    """Space ID"""
    name: str | None = Field(default=None, description="Space name")
    """Space name"""
    access: bool | None | None = Field(default=None, description="Whether user has access")
    """Whether user has access"""

class ListFolder(BaseModel):
    """Parent folder reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Folder ID")
    """Folder ID"""
    name: str | None = Field(default=None, description="Folder name")
    """Folder name"""
    hidden: bool | None | None = Field(default=None, description="Whether the folder is hidden")
    """Whether the folder is hidden"""
    access: bool | None | None = Field(default=None, description="Whether user has access")
    """Whether user has access"""

class List(BaseModel):
    """List type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    orderindex: int | None = Field(default=None)
    status: dict[str, Any] | None = Field(default=None)
    priority: dict[str, Any] | None = Field(default=None)
    assignee: dict[str, Any] | None = Field(default=None)
    task_count: int | None = Field(default=None)
    due_date: str | None = Field(default=None)
    start_date: str | None = Field(default=None)
    folder: ListFolder | None = Field(default=None)
    space: ListSpace | None = Field(default=None)
    archived: bool | None = Field(default=None)
    override_statuses: bool | None = Field(default=None)
    content: str | None = Field(default=None)
    deleted: bool | None = Field(default=None)
    inbound_address: str | None = Field(default=None)
    statuses: list[ListStatusesItem] | None = Field(default=None)
    permission_level: str | None = Field(default=None)

class ListsListResponse(BaseModel):
    """ListsListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    lists: list[List] | None = Field(default=None)

class TaskStatus(BaseModel):
    """Task status"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Status ID")
    """Status ID"""
    status: str | None = Field(default=None, description="Status name")
    """Status name"""
    color: str | None | None = Field(default=None, description="Status color hex code")
    """Status color hex code"""
    type_: str | None = Field(default=None, alias="type", description="Status type (open, custom, closed)")
    """Status type (open, custom, closed)"""
    orderindex: int | None = Field(default=None, description="Status order index")
    """Status order index"""

class TaskWatchersItem(BaseModel):
    """Nested schema for Task.watchers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None, description="Watcher user ID")
    """Watcher user ID"""
    username: str | None = Field(default=None, description="Watcher username")
    """Watcher username"""
    color: str | None | None = Field(default=None, description="Watcher avatar color")
    """Watcher avatar color"""
    initials: str | None | None = Field(default=None, description="Watcher initials")
    """Watcher initials"""
    email: str | None = Field(default=None, description="Watcher email")
    """Watcher email"""
    profile_picture: str | None | None = Field(default=None, alias="profilePicture", description="Watcher profile picture URL")
    """Watcher profile picture URL"""

class TaskCreator(BaseModel):
    """Task creator"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None, description="Creator user ID")
    """Creator user ID"""
    username: str | None = Field(default=None, description="Creator username")
    """Creator username"""
    color: str | None | None = Field(default=None, description="Creator avatar color")
    """Creator avatar color"""
    email: str | None = Field(default=None, description="Creator email")
    """Creator email"""
    profile_picture: str | None | None = Field(default=None, alias="profilePicture", description="Creator profile picture URL")
    """Creator profile picture URL"""

class Task(BaseModel):
    """Task type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    custom_id: str | None = Field(default=None)
    custom_item_id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    text_content: str | None = Field(default=None)
    description: str | None = Field(default=None)
    status: TaskStatus | None = Field(default=None)
    orderindex: str | None = Field(default=None)
    date_created: str | None = Field(default=None)
    date_updated: str | None = Field(default=None)
    date_closed: str | None = Field(default=None)
    date_done: str | None = Field(default=None)
    archived: bool | None = Field(default=None)
    creator: TaskCreator | None = Field(default=None)
    assignees: list[dict[str, Any]] | None = Field(default=None)
    group_assignees: list[dict[str, Any]] | None = Field(default=None)
    watchers: list[TaskWatchersItem] | None = Field(default=None)
    checklists: list[dict[str, Any]] | None = Field(default=None)
    tags: list[dict[str, Any]] | None = Field(default=None)
    parent: str | None = Field(default=None)
    priority: dict[str, Any] | None = Field(default=None)
    due_date: str | None = Field(default=None)
    start_date: str | None = Field(default=None)
    points: float | None = Field(default=None)
    time_estimate: int | None = Field(default=None)
    time_spent: int | None = Field(default=None)
    custom_fields: list[dict[str, Any]] | None = Field(default=None)
    dependencies: list[dict[str, Any]] | None = Field(default=None)
    linked_tasks: list[dict[str, Any]] | None = Field(default=None)
    team_id: str | None = Field(default=None)
    url: str | None = Field(default=None)
    list_: dict[str, Any] | None = Field(default=None, alias="list")
    project: dict[str, Any] | None = Field(default=None)
    folder: dict[str, Any] | None = Field(default=None)
    space: dict[str, Any] | None = Field(default=None)
    top_level_parent: str | None = Field(default=None)
    locations: list[dict[str, Any]] | None = Field(default=None)
    sharing: dict[str, Any] | None = Field(default=None)
    permission_level: str | None = Field(default=None)
    attachments: list[dict[str, Any]] | None = Field(default=None)

class TasksListResponse(BaseModel):
    """TasksListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tasks: list[Task] | None = Field(default=None)
    last_page: bool | None = Field(default=None)

class Comment(BaseModel):
    """Comment type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    comment: list[dict[str, Any]] | None = Field(default=None)
    comment_text: str | None = Field(default=None)
    user: dict[str, Any] | None = Field(default=None)
    resolved: bool | None = Field(default=None)
    assignee: dict[str, Any] | None = Field(default=None)
    assigned_by: dict[str, Any] | None = Field(default=None)
    reactions: list[dict[str, Any]] | None = Field(default=None)
    date: str | None = Field(default=None)

class CommentsListResponse(BaseModel):
    """CommentsListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: list[Comment] | None = Field(default=None)

class CommentCreateParams(BaseModel):
    """CommentCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comment_text: str
    assignee: int | None = Field(default=None)
    notify_all: bool | None = Field(default=None)

class CommentCreateResponse(BaseModel):
    """CommentCreateResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    hist_id: str | None = Field(default=None)
    date: int | None = Field(default=None)
    version: dict[str, Any] | None = Field(default=None)

class CommentUpdateParams(BaseModel):
    """CommentUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comment_text: str | None = Field(default=None)
    assignee: int | None = Field(default=None)
    resolved: bool | None = Field(default=None)

class CommentUpdateResponse(BaseModel):
    """CommentUpdateResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pass

class Goal(BaseModel):
    """Goal type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    pretty_id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    team_id: str | None = Field(default=None)
    creator: int | None = Field(default=None)
    owner: dict[str, Any] | None = Field(default=None)
    color: str | None = Field(default=None)
    date_created: str | None = Field(default=None)
    start_date: str | None = Field(default=None)
    due_date: str | None = Field(default=None)
    description: str | None = Field(default=None)
    private: bool | None = Field(default=None)
    archived: bool | None = Field(default=None)
    multiple_owners: bool | None = Field(default=None)
    members: list[dict[str, Any]] | None = Field(default=None)
    key_results: list[dict[str, Any]] | None = Field(default=None)
    percent_completed: int | None = Field(default=None)
    history: list[dict[str, Any]] | None = Field(default=None)
    pretty_url: str | None = Field(default=None)

class GoalsListResponse(BaseModel):
    """GoalsListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    goals: list[Goal] | None = Field(default=None)
    folders: list[dict[str, Any]] | None = Field(default=None)

class GoalResponse(BaseModel):
    """GoalResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    goal: Goal | None = Field(default=None)

class ViewParent(BaseModel):
    """Parent reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Any | None = Field(default=None, description="Parent entity ID")
    """Parent entity ID"""
    type_: Any | None = Field(default=None, alias="type", description="Parent entity type")
    """Parent entity type"""

class View(BaseModel):
    """View type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    parent: ViewParent | None = Field(default=None)
    grouping: dict[str, Any] | None = Field(default=None)
    divide: dict[str, Any] | None = Field(default=None)
    sorting: dict[str, Any] | None = Field(default=None)
    filters: dict[str, Any] | None = Field(default=None)
    columns: dict[str, Any] | None = Field(default=None)
    team_sidebar: dict[str, Any] | None = Field(default=None)
    settings: dict[str, Any] | None = Field(default=None)
    date_created: str | None = Field(default=None)
    creator: int | None = Field(default=None)
    visibility: str | None = Field(default=None)
    protected: bool | None = Field(default=None)
    protected_note: str | None = Field(default=None)
    protected_by: int | None = Field(default=None)
    date_protected: str | None = Field(default=None)
    orderindex: int | None = Field(default=None)
    public: bool | None = Field(default=None)

class ViewsListResponse(BaseModel):
    """ViewsListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    views: list[View] | None = Field(default=None)
    required_views: dict[str, Any] | None = Field(default=None)
    default_view: dict[str, Any] | None = Field(default=None)

class ViewResponse(BaseModel):
    """ViewResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    view: View | None = Field(default=None)

class TimeEntry(BaseModel):
    """TimeEntry type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    task: dict[str, Any] | None = Field(default=None)
    wid: str | None = Field(default=None)
    user: dict[str, Any] | None = Field(default=None)
    billable: bool | None = Field(default=None)
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)
    duration: str | None = Field(default=None)
    description: str | None = Field(default=None)
    tags: list[dict[str, Any]] | None = Field(default=None)
    at: str | None = Field(default=None)

class TimeEntriesListResponse(BaseModel):
    """TimeEntriesListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[TimeEntry] | None = Field(default=None)

class TimeEntryResponse(BaseModel):
    """TimeEntryResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: TimeEntry | None = Field(default=None)

class Member(BaseModel):
    """Member type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    username: str | None = Field(default=None)
    email: str | None = Field(default=None)
    color: str | None = Field(default=None)
    profile_picture: str | None = Field(default=None, alias="profilePicture")
    initials: str | None = Field(default=None)

class MembersListResponse(BaseModel):
    """MembersListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    members: list[Member] | None = Field(default=None)

class Doc(BaseModel):
    """Doc type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    type_: int | None = Field(default=None, alias="type")
    parent: dict[str, Any] | None = Field(default=None)
    creator: int | None = Field(default=None)
    deleted: bool | None = Field(default=None)
    public: bool | None = Field(default=None)
    date_created: int | None = Field(default=None)
    date_updated: int | None = Field(default=None)
    workspace_id: int | None = Field(default=None)
    content: str | None = Field(default=None)

class DocsListResponse(BaseModel):
    """DocsListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    docs: list[Doc] | None = Field(default=None)
    next_cursor: str | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class TasksListResultMeta(BaseModel):
    """Metadata for tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    last_page: bool | None = Field(default=None)

class TasksApiSearchResultMeta(BaseModel):
    """Metadata for tasks.Action.API_SEARCH operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    last_page: bool | None = Field(default=None)

class ViewTasksListResultMeta(BaseModel):
    """Metadata for view_tasks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    last_page: bool | None = Field(default=None)

class DocsListResultMeta(BaseModel):
    """Metadata for docs.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class ClickupApiCheckResult(BaseModel):
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


class ClickupApiExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class ClickupApiExecuteResultWithMeta(ClickupApiExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class UserSearchData(BaseModel):
    """Search result data for user entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the user"""
    username: str | None = None
    """Display name of the user"""


class TeamsSearchData(BaseModel):
    """Search result data for teams entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the team (workspace)"""
    name: str | None = None
    """Name of the team"""


class SpacesSearchData(BaseModel):
    """Search result data for spaces entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the space"""
    name: str | None = None
    """Name of the space"""
    private: bool | None = None
    """Whether the space is private"""


class FoldersSearchData(BaseModel):
    """Search result data for folders entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the folder"""
    name: str | None = None
    """Name of the folder"""
    hidden: bool | None = None
    """Whether the folder is hidden from the sidebar"""
    task_count: str | None = None
    """Number of tasks contained in the folder"""


class ListsSearchData(BaseModel):
    """Search result data for lists entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the list"""
    name: str | None = None
    """Name of the list"""
    archived: bool | None = None
    """Whether the list has been archived"""
    due_date: str | None = None
    """Due date for the list, in ClickUp timestamp format"""
    start_date: str | None = None
    """Start date for the list, in ClickUp timestamp format"""
    priority: str | None = None
    """Priority assigned to the list"""
    task_count: int | None = None
    """Number of tasks contained in the list"""


class TasksSearchData(BaseModel):
    """Search result data for tasks entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the task"""
    name: str | None = None
    """Name of the task"""
    date_created: str | None = None
    """Creation timestamp of the task, in ClickUp timestamp format"""
    date_updated: str | None = None
    """Last update timestamp of the task, in ClickUp timestamp format"""
    date_closed: str | None = None
    """Timestamp when the task was closed, in ClickUp timestamp format"""
    due_date: str | None = None
    """Due date for the task, in ClickUp timestamp format"""
    start_date: str | None = None
    """Start date for the task, in ClickUp timestamp format"""
    parent: str | None = None
    """ID of the parent task, if this task is a subtask"""
    url: str | None = None
    """Permalink URL to view the task in ClickUp"""


class CommentsSearchData(BaseModel):
    """Search result data for comments entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the comment"""
    comment_text: str | None = None
    """Plain-text content of the comment"""
    date: str | None = None
    """Timestamp when the comment was posted, in ClickUp timestamp format"""
    reply_count: float | None = None
    """Number of replies on the comment"""


class GoalsSearchData(BaseModel):
    """Search result data for goals entity."""
    model_config = ConfigDict(extra="allow")

    id: str = None
    """Unique identifier for the goal"""
    name: str | None = None
    """Name of the goal"""
    description: str | None = None
    """Description of the goal"""
    archived: bool | None = None
    """Whether the goal has been archived"""
    pinned: bool | None = None
    """Whether the goal is pinned to the top of the list"""
    private: bool | None = None
    """Whether the goal is private to its owners"""
    date_created: str | None = None
    """Creation timestamp of the goal, in ClickUp timestamp format"""
    due_date: str | None = None
    """Due date for the goal, in ClickUp timestamp format"""
    percent_completed: float | None = None
    """Completion percentage of the goal, between 0 and 100"""
    team_id: str | None = None
    """Identifier of the team that owns the goal"""


class TimeTrackingSearchData(BaseModel):
    """Search result data for time_tracking entity."""
    model_config = ConfigDict(extra="allow")

    time: float | None = None
    """Total tracked time in milliseconds"""
    user: dict[str, Any] | None = None
    """User who tracked the time"""


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

UserSearchResult = AirbyteSearchResult[UserSearchData]
"""Search result type for user entity."""

TeamsSearchResult = AirbyteSearchResult[TeamsSearchData]
"""Search result type for teams entity."""

SpacesSearchResult = AirbyteSearchResult[SpacesSearchData]
"""Search result type for spaces entity."""

FoldersSearchResult = AirbyteSearchResult[FoldersSearchData]
"""Search result type for folders entity."""

ListsSearchResult = AirbyteSearchResult[ListsSearchData]
"""Search result type for lists entity."""

TasksSearchResult = AirbyteSearchResult[TasksSearchData]
"""Search result type for tasks entity."""

CommentsSearchResult = AirbyteSearchResult[CommentsSearchData]
"""Search result type for comments entity."""

GoalsSearchResult = AirbyteSearchResult[GoalsSearchData]
"""Search result type for goals entity."""

TimeTrackingSearchResult = AirbyteSearchResult[TimeTrackingSearchData]
"""Search result type for time_tracking entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

TeamsListResult = ClickupApiExecuteResult[list[Team]]
"""Result type for teams.list operation."""

SpacesListResult = ClickupApiExecuteResult[list[Space]]
"""Result type for spaces.list operation."""

FoldersListResult = ClickupApiExecuteResult[list[Folder]]
"""Result type for folders.list operation."""

ListsListResult = ClickupApiExecuteResult[list[List]]
"""Result type for lists.list operation."""

TasksListResult = ClickupApiExecuteResultWithMeta[list[Task], TasksListResultMeta]
"""Result type for tasks.list operation with data and metadata."""

TasksApiSearchResult = ClickupApiExecuteResultWithMeta[list[Task], TasksApiSearchResultMeta]
"""Result type for tasks.api_search operation with data and metadata."""

CommentsListResult = ClickupApiExecuteResult[list[Comment]]
"""Result type for comments.list operation."""

GoalsListResult = ClickupApiExecuteResult[list[Goal]]
"""Result type for goals.list operation."""

ViewsListResult = ClickupApiExecuteResult[list[View]]
"""Result type for views.list operation."""

ViewTasksListResult = ClickupApiExecuteResultWithMeta[list[Task], ViewTasksListResultMeta]
"""Result type for view_tasks.list operation with data and metadata."""

TimeTrackingListResult = ClickupApiExecuteResult[list[TimeEntry]]
"""Result type for time_tracking.list operation."""

MembersListResult = ClickupApiExecuteResult[list[Member]]
"""Result type for members.list operation."""

DocsListResult = ClickupApiExecuteResultWithMeta[list[Doc], DocsListResultMeta]
"""Result type for docs.list operation with data and metadata."""

