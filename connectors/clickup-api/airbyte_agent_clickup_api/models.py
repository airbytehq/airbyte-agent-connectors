"""
Pydantic models for clickup-api connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

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

    id: Union[int, Any] = Field(default=None)
    username: Union[str, Any] = Field(default=None)
    email: Union[str, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)
    profile_picture: Union[str | None, Any] = Field(default=None, alias="profilePicture")
    initials: Union[str | None, Any] = Field(default=None)
    week_start_day: Union[int | None, Any] = Field(default=None)
    global_font_support: Union[bool | None, Any] = Field(default=None)
    timezone: Union[str | None, Any] = Field(default=None)

class UserResponse(BaseModel):
    """UserResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user: Union[User, Any] = Field(default=None)

class TeamMembersItemUser(BaseModel):
    """Member user details"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None, description="User ID")
    """User ID"""
    username: Union[str, Any] = Field(default=None, description="Username")
    """Username"""
    email: Union[str, Any] = Field(default=None, description="Email address")
    """Email address"""
    color: Union[str | None, Any] = Field(default=None, description="Avatar color")
    """Avatar color"""
    profile_picture: Union[str | None, Any] = Field(default=None, alias="profilePicture", description="Profile picture URL")
    """Profile picture URL"""
    initials: Union[str | None, Any] = Field(default=None, description="User initials")
    """User initials"""
    role: Union[int | None, Any] = Field(default=None, description="User role ID")
    """User role ID"""
    role_subtype: Union[int | None, Any] = Field(default=None, description="User role subtype")
    """User role subtype"""
    role_key: Union[str | None, Any] = Field(default=None, description="Role key name")
    """Role key name"""
    custom_role: Union[dict[str, Any] | None, Any] = Field(default=None, description="Custom role details")
    """Custom role details"""
    last_active: Union[str | None, Any] = Field(default=None, description="Last active timestamp (Unix ms)")
    """Last active timestamp (Unix ms)"""
    date_joined: Union[str | None, Any] = Field(default=None, description="Date joined (Unix ms)")
    """Date joined (Unix ms)"""
    date_invited: Union[str | None, Any] = Field(default=None, description="Date invited (Unix ms)")
    """Date invited (Unix ms)"""

class TeamMembersItem(BaseModel):
    """Nested schema for Team.members_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user: Union[TeamMembersItemUser, Any] = Field(default=None, description="Member user details")
    """Member user details"""

class Team(BaseModel):
    """Team type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)
    avatar: Union[str | None, Any] = Field(default=None)
    members: Union[list[TeamMembersItem], Any] = Field(default=None)

class TeamsListResponse(BaseModel):
    """TeamsListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    teams: Union[list[Team], Any] = Field(default=None)

class SpaceFeaturesCustomItems(BaseModel):
    """Custom items feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether custom items are enabled")
    """Whether custom items are enabled"""

class SpaceFeaturesPoints(BaseModel):
    """Points feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether points are enabled")
    """Whether points are enabled"""

class SpaceFeaturesSprints(BaseModel):
    """Sprints feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether sprints are enabled")
    """Whether sprints are enabled"""

class SpaceFeaturesTags(BaseModel):
    """Tags feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether tags are enabled")
    """Whether tags are enabled"""

class SpaceFeaturesCustomFields(BaseModel):
    """Custom fields feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether custom fields are enabled")
    """Whether custom fields are enabled"""

class SpaceFeaturesDependencyWarning(BaseModel):
    """Dependency warning feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether dependency warnings are enabled")
    """Whether dependency warnings are enabled"""

class SpaceFeaturesDueDates(BaseModel):
    """Due dates feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether due dates are enabled")
    """Whether due dates are enabled"""
    start_date: Union[bool, Any] = Field(default=None, description="Whether start dates are enabled")
    """Whether start dates are enabled"""
    remap_due_dates: Union[bool, Any] = Field(default=None, description="Whether due dates are remapped")
    """Whether due dates are remapped"""
    remap_closed_due_date: Union[bool, Any] = Field(default=None, description="Whether closed due dates are remapped")
    """Whether closed due dates are remapped"""

class SpaceFeaturesDependencyEnforcement(BaseModel):
    """Dependency enforcement settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enforcement_enabled: Union[bool, Any] = Field(default=None, description="Whether enforcement is enabled")
    """Whether enforcement is enabled"""
    enforcement_mode: Union[int | None, Any] = Field(default=None, description="Enforcement mode")
    """Enforcement mode"""

class SpaceFeaturesRescheduleClosedDependencies(BaseModel):
    """Reschedule closed dependencies settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether rescheduling closed dependencies is enabled")
    """Whether rescheduling closed dependencies is enabled"""

class SpaceFeaturesMilestones(BaseModel):
    """Milestones feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether milestones are enabled")
    """Whether milestones are enabled"""

class SpaceFeaturesStatusPies(BaseModel):
    """Status pies feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether status pies are enabled")
    """Whether status pies are enabled"""

class SpaceFeaturesCheckUnresolved(BaseModel):
    """Check unresolved feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether check unresolved is enabled")
    """Whether check unresolved is enabled"""
    subtasks: Union[bool | None, Any] = Field(default=None, description="Check unresolved subtasks")
    """Check unresolved subtasks"""
    checklists: Union[bool | None, Any] = Field(default=None, description="Check unresolved checklists")
    """Check unresolved checklists"""
    comments: Union[bool | None, Any] = Field(default=None, description="Check unresolved comments")
    """Check unresolved comments"""

class SpaceFeaturesPrioritiesPrioritiesItem(BaseModel):
    """Nested schema for SpaceFeaturesPriorities.priorities_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: Union[str, Any] = Field(default=None, description="Priority color hex code")
    """Priority color hex code"""
    id: Union[str, Any] = Field(default=None, description="Priority ID")
    """Priority ID"""
    orderindex: Union[str, Any] = Field(default=None, description="Priority order index")
    """Priority order index"""
    priority: Union[str, Any] = Field(default=None, description="Priority name")
    """Priority name"""

class SpaceFeaturesPriorities(BaseModel):
    """Priorities feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether priorities are enabled")
    """Whether priorities are enabled"""
    priorities: Union[list[SpaceFeaturesPrioritiesPrioritiesItem], Any] = Field(default=None, description="Priority levels")
    """Priority levels"""

class SpaceFeaturesMultipleAssignees(BaseModel):
    """Multiple assignees feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether multiple assignees are enabled")
    """Whether multiple assignees are enabled"""

class SpaceFeaturesEmails(BaseModel):
    """Emails feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether emails are enabled")
    """Whether emails are enabled"""

class SpaceFeaturesTimeTracking(BaseModel):
    """Time tracking feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether time tracking is enabled")
    """Whether time tracking is enabled"""
    harvest: Union[bool, Any] = Field(default=None, description="Whether Harvest integration is enabled")
    """Whether Harvest integration is enabled"""
    rollup: Union[bool, Any] = Field(default=None, description="Whether time rollup is enabled")
    """Whether time rollup is enabled"""
    default_to_billable: Union[int | None, Any] = Field(default=None, description="Default billable setting")
    """Default billable setting"""

class SpaceFeaturesTimeEstimates(BaseModel):
    """Time estimates feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether time estimates are enabled")
    """Whether time estimates are enabled"""
    rollup: Union[bool, Any] = Field(default=None, description="Whether time estimate rollup is enabled")
    """Whether time estimate rollup is enabled"""
    per_assignee: Union[bool, Any] = Field(default=None, description="Whether per-assignee estimates are enabled")
    """Whether per-assignee estimates are enabled"""

class SpaceFeaturesRemapDependencies(BaseModel):
    """Remap dependencies feature settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    enabled: Union[bool, Any] = Field(default=None, description="Whether remap dependencies is enabled")
    """Whether remap dependencies is enabled"""

class SpaceFeatures(BaseModel):
    """Feature flags for the space"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    due_dates: Union[SpaceFeaturesDueDates, Any] = Field(default=None, description="Due dates feature settings")
    """Due dates feature settings"""
    sprints: Union[SpaceFeaturesSprints, Any] = Field(default=None, description="Sprints feature settings")
    """Sprints feature settings"""
    time_tracking: Union[SpaceFeaturesTimeTracking, Any] = Field(default=None, description="Time tracking feature settings")
    """Time tracking feature settings"""
    points: Union[SpaceFeaturesPoints, Any] = Field(default=None, description="Points feature settings")
    """Points feature settings"""
    custom_items: Union[SpaceFeaturesCustomItems, Any] = Field(default=None, description="Custom items feature settings")
    """Custom items feature settings"""
    priorities: Union[SpaceFeaturesPriorities, Any] = Field(default=None, description="Priorities feature settings")
    """Priorities feature settings"""
    tags: Union[SpaceFeaturesTags, Any] = Field(default=None, description="Tags feature settings")
    """Tags feature settings"""
    time_estimates: Union[SpaceFeaturesTimeEstimates, Any] = Field(default=None, description="Time estimates feature settings")
    """Time estimates feature settings"""
    check_unresolved: Union[SpaceFeaturesCheckUnresolved, Any] = Field(default=None, description="Check unresolved feature settings")
    """Check unresolved feature settings"""
    milestones: Union[SpaceFeaturesMilestones, Any] = Field(default=None, description="Milestones feature settings")
    """Milestones feature settings"""
    custom_fields: Union[SpaceFeaturesCustomFields, Any] = Field(default=None, description="Custom fields feature settings")
    """Custom fields feature settings"""
    remap_dependencies: Union[SpaceFeaturesRemapDependencies, Any] = Field(default=None, description="Remap dependencies feature settings")
    """Remap dependencies feature settings"""
    dependency_warning: Union[SpaceFeaturesDependencyWarning, Any] = Field(default=None, description="Dependency warning feature settings")
    """Dependency warning feature settings"""
    status_pies: Union[SpaceFeaturesStatusPies, Any] = Field(default=None, description="Status pies feature settings")
    """Status pies feature settings"""
    multiple_assignees: Union[SpaceFeaturesMultipleAssignees, Any] = Field(default=None, description="Multiple assignees feature settings")
    """Multiple assignees feature settings"""
    emails: Union[SpaceFeaturesEmails, Any] = Field(default=None, description="Emails feature settings")
    """Emails feature settings"""
    scheduler_enabled: Union[bool, Any] = Field(default=None, description="Whether scheduler is enabled")
    """Whether scheduler is enabled"""
    dependency_type_enabled: Union[bool, Any] = Field(default=None, description="Whether dependency types are enabled")
    """Whether dependency types are enabled"""
    dependency_enforcement: Union[SpaceFeaturesDependencyEnforcement, Any] = Field(default=None, description="Dependency enforcement settings")
    """Dependency enforcement settings"""
    reschedule_closed_dependencies: Union[SpaceFeaturesRescheduleClosedDependencies, Any] = Field(default=None, description="Reschedule closed dependencies settings")
    """Reschedule closed dependencies settings"""

class SpaceStatusesItem(BaseModel):
    """Nested schema for Space.statuses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Status ID")
    """Status ID"""
    status: Union[str, Any] = Field(default=None, description="Status name")
    """Status name"""
    type_: Union[str, Any] = Field(default=None, alias="type", description="Status type (open, custom, closed)")
    """Status type (open, custom, closed)"""
    orderindex: Union[int, Any] = Field(default=None, description="Status order index")
    """Status order index"""
    color: Union[str, Any] = Field(default=None, description="Status color hex code")
    """Status color hex code"""

class Space(BaseModel):
    """Space type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    private: Union[bool, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)
    avatar: Union[str | None, Any] = Field(default=None)
    admin_can_manage: Union[bool | None, Any] = Field(default=None)
    statuses: Union[list[SpaceStatusesItem], Any] = Field(default=None)
    multiple_assignees: Union[bool, Any] = Field(default=None)
    features: Union[SpaceFeatures, Any] = Field(default=None)
    archived: Union[bool, Any] = Field(default=None)

class SpacesListResponse(BaseModel):
    """SpacesListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    spaces: Union[list[Space], Any] = Field(default=None)

class FolderListsItemStatusesItem(BaseModel):
    """Nested schema for FolderListsItem.statuses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Status ID")
    """Status ID"""
    status: Union[str, Any] = Field(default=None, description="Status name")
    """Status name"""
    type_: Union[str, Any] = Field(default=None, alias="type", description="Status type (open, custom, closed)")
    """Status type (open, custom, closed)"""
    orderindex: Union[int, Any] = Field(default=None, description="Status order index")
    """Status order index"""
    color: Union[str, Any] = Field(default=None, description="Status color hex code")
    """Status color hex code"""
    status_group: Union[str | None, Any] = Field(default=None, description="Status group identifier")
    """Status group identifier"""

class FolderListsItem(BaseModel):
    """Nested schema for Folder.lists_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="List ID")
    """List ID"""
    name: Union[str, Any] = Field(default=None, description="List name")
    """List name"""
    orderindex: Union[int | None, Any] = Field(default=None, description="Sort order index")
    """Sort order index"""
    content: Union[str | None, Any] = Field(default=None, description="List description")
    """List description"""
    status: Union[dict[str, Any] | None, Any] = Field(default=None, description="List status")
    """List status"""
    priority: Union[dict[str, Any] | None, Any] = Field(default=None, description="List priority")
    """List priority"""
    assignee: Union[dict[str, Any] | None, Any] = Field(default=None, description="List assignee")
    """List assignee"""
    task_count: Union[int | None, Any] = Field(default=None, description="Number of tasks")
    """Number of tasks"""
    due_date: Union[str | None, Any] = Field(default=None, description="Due date (Unix ms)")
    """Due date (Unix ms)"""
    start_date: Union[str | None, Any] = Field(default=None, description="Start date (Unix ms)")
    """Start date (Unix ms)"""
    space: Union[dict[str, Any] | None, Any] = Field(default=None, description="Parent space reference")
    """Parent space reference"""
    archived: Union[bool | None, Any] = Field(default=None, description="Whether the list is archived")
    """Whether the list is archived"""
    override_statuses: Union[bool | None, Any] = Field(default=None, description="Whether list overrides statuses")
    """Whether list overrides statuses"""
    statuses: Union[list[FolderListsItemStatusesItem], Any] = Field(default=None, description="List statuses")
    """List statuses"""
    permission_level: Union[str | None, Any] = Field(default=None, description="User permission level")
    """User permission level"""

class FolderSpace(BaseModel):
    """Parent space reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Space ID")
    """Space ID"""
    name: Union[str, Any] = Field(default=None, description="Space name")
    """Space name"""
    access: Union[bool | None, Any] = Field(default=None, description="Whether user has access")
    """Whether user has access"""

class FolderStatusesItem(BaseModel):
    """Nested schema for Folder.statuses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Status ID")
    """Status ID"""
    status: Union[str, Any] = Field(default=None, description="Status name")
    """Status name"""
    type_: Union[str, Any] = Field(default=None, alias="type", description="Status type (open, custom, closed)")
    """Status type (open, custom, closed)"""
    orderindex: Union[int, Any] = Field(default=None, description="Status order index")
    """Status order index"""
    color: Union[str, Any] = Field(default=None, description="Status color hex code")
    """Status color hex code"""

class Folder(BaseModel):
    """Folder type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    orderindex: Union[int | None, Any] = Field(default=None)
    override_statuses: Union[bool, Any] = Field(default=None)
    hidden: Union[bool, Any] = Field(default=None)
    space: Union[FolderSpace, Any] = Field(default=None)
    task_count: Union[str | None, Any] = Field(default=None)
    archived: Union[bool, Any] = Field(default=None)
    statuses: Union[list[FolderStatusesItem], Any] = Field(default=None)
    deleted: Union[bool | None, Any] = Field(default=None)
    lists: Union[list[FolderListsItem], Any] = Field(default=None)
    permission_level: Union[str | None, Any] = Field(default=None)

class FoldersListResponse(BaseModel):
    """FoldersListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    folders: Union[list[Folder], Any] = Field(default=None)

class ListStatusesItem(BaseModel):
    """Nested schema for List.statuses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Status ID")
    """Status ID"""
    status: Union[str, Any] = Field(default=None, description="Status name")
    """Status name"""
    type_: Union[str, Any] = Field(default=None, alias="type", description="Status type (open, custom, closed)")
    """Status type (open, custom, closed)"""
    orderindex: Union[int, Any] = Field(default=None, description="Status order index")
    """Status order index"""
    color: Union[str, Any] = Field(default=None, description="Status color hex code")
    """Status color hex code"""
    status_group: Union[str | None, Any] = Field(default=None, description="Status group identifier")
    """Status group identifier"""

class ListSpace(BaseModel):
    """Parent space reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Space ID")
    """Space ID"""
    name: Union[str, Any] = Field(default=None, description="Space name")
    """Space name"""
    access: Union[bool | None, Any] = Field(default=None, description="Whether user has access")
    """Whether user has access"""

class ListFolder(BaseModel):
    """Parent folder reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Folder ID")
    """Folder ID"""
    name: Union[str, Any] = Field(default=None, description="Folder name")
    """Folder name"""
    hidden: Union[bool | None, Any] = Field(default=None, description="Whether the folder is hidden")
    """Whether the folder is hidden"""
    access: Union[bool | None, Any] = Field(default=None, description="Whether user has access")
    """Whether user has access"""

class List(BaseModel):
    """List type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    orderindex: Union[int | None, Any] = Field(default=None)
    status: Union[dict[str, Any] | None, Any] = Field(default=None)
    priority: Union[dict[str, Any] | None, Any] = Field(default=None)
    assignee: Union[dict[str, Any] | None, Any] = Field(default=None)
    task_count: Union[int | None, Any] = Field(default=None)
    due_date: Union[str | None, Any] = Field(default=None)
    start_date: Union[str | None, Any] = Field(default=None)
    folder: Union[ListFolder, Any] = Field(default=None)
    space: Union[ListSpace, Any] = Field(default=None)
    archived: Union[bool, Any] = Field(default=None)
    override_statuses: Union[bool | None, Any] = Field(default=None)
    content: Union[str | None, Any] = Field(default=None)
    deleted: Union[bool | None, Any] = Field(default=None)
    inbound_address: Union[str | None, Any] = Field(default=None)
    statuses: Union[list[ListStatusesItem], Any] = Field(default=None)
    permission_level: Union[str | None, Any] = Field(default=None)

class ListsListResponse(BaseModel):
    """ListsListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    lists: Union[list[List], Any] = Field(default=None)

class TaskStatus(BaseModel):
    """Task status"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Status ID")
    """Status ID"""
    status: Union[str, Any] = Field(default=None, description="Status name")
    """Status name"""
    color: Union[str | None, Any] = Field(default=None, description="Status color hex code")
    """Status color hex code"""
    type_: Union[str, Any] = Field(default=None, alias="type", description="Status type (open, custom, closed)")
    """Status type (open, custom, closed)"""
    orderindex: Union[int, Any] = Field(default=None, description="Status order index")
    """Status order index"""

class TaskWatchersItem(BaseModel):
    """Nested schema for Task.watchers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None, description="Watcher user ID")
    """Watcher user ID"""
    username: Union[str, Any] = Field(default=None, description="Watcher username")
    """Watcher username"""
    color: Union[str | None, Any] = Field(default=None, description="Watcher avatar color")
    """Watcher avatar color"""
    initials: Union[str | None, Any] = Field(default=None, description="Watcher initials")
    """Watcher initials"""
    email: Union[str, Any] = Field(default=None, description="Watcher email")
    """Watcher email"""
    profile_picture: Union[str | None, Any] = Field(default=None, alias="profilePicture", description="Watcher profile picture URL")
    """Watcher profile picture URL"""

class TaskCreator(BaseModel):
    """Task creator"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None, description="Creator user ID")
    """Creator user ID"""
    username: Union[str, Any] = Field(default=None, description="Creator username")
    """Creator username"""
    color: Union[str | None, Any] = Field(default=None, description="Creator avatar color")
    """Creator avatar color"""
    email: Union[str, Any] = Field(default=None, description="Creator email")
    """Creator email"""
    profile_picture: Union[str | None, Any] = Field(default=None, alias="profilePicture", description="Creator profile picture URL")
    """Creator profile picture URL"""

class Task(BaseModel):
    """Task type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    custom_id: Union[str | None, Any] = Field(default=None)
    custom_item_id: Union[int | None, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    text_content: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    status: Union[TaskStatus, Any] = Field(default=None)
    orderindex: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_updated: Union[str | None, Any] = Field(default=None)
    date_closed: Union[str | None, Any] = Field(default=None)
    date_done: Union[str | None, Any] = Field(default=None)
    archived: Union[bool, Any] = Field(default=None)
    creator: Union[TaskCreator, Any] = Field(default=None)
    assignees: Union[list[dict[str, Any]], Any] = Field(default=None)
    group_assignees: Union[list[dict[str, Any]], Any] = Field(default=None)
    watchers: Union[list[TaskWatchersItem], Any] = Field(default=None)
    checklists: Union[list[dict[str, Any]], Any] = Field(default=None)
    tags: Union[list[dict[str, Any]], Any] = Field(default=None)
    parent: Union[str | None, Any] = Field(default=None)
    priority: Union[dict[str, Any] | None, Any] = Field(default=None)
    due_date: Union[str | None, Any] = Field(default=None)
    start_date: Union[str | None, Any] = Field(default=None)
    points: Union[float | None, Any] = Field(default=None)
    time_estimate: Union[int | None, Any] = Field(default=None)
    time_spent: Union[int | None, Any] = Field(default=None)
    custom_fields: Union[list[dict[str, Any]], Any] = Field(default=None)
    dependencies: Union[list[dict[str, Any]], Any] = Field(default=None)
    linked_tasks: Union[list[dict[str, Any]], Any] = Field(default=None)
    team_id: Union[str | None, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    list_: Union[dict[str, Any] | None, Any] = Field(default=None, alias="list")
    project: Union[dict[str, Any] | None, Any] = Field(default=None)
    folder: Union[dict[str, Any] | None, Any] = Field(default=None)
    space: Union[dict[str, Any] | None, Any] = Field(default=None)
    top_level_parent: Union[str | None, Any] = Field(default=None)
    locations: Union[list[dict[str, Any]], Any] = Field(default=None)
    sharing: Union[dict[str, Any] | None, Any] = Field(default=None)
    permission_level: Union[str | None, Any] = Field(default=None)
    attachments: Union[list[dict[str, Any]], Any] = Field(default=None)

class TasksListResponse(BaseModel):
    """TasksListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tasks: Union[list[Task], Any] = Field(default=None)
    last_page: Union[bool | None, Any] = Field(default=None)

class Comment(BaseModel):
    """Comment type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    comment: Union[list[dict[str, Any]], Any] = Field(default=None)
    comment_text: Union[str, Any] = Field(default=None)
    user: Union[dict[str, Any], Any] = Field(default=None)
    resolved: Union[bool, Any] = Field(default=None)
    assignee: Union[dict[str, Any] | None, Any] = Field(default=None)
    assigned_by: Union[dict[str, Any] | None, Any] = Field(default=None)
    reactions: Union[list[dict[str, Any]], Any] = Field(default=None)
    date: Union[str, Any] = Field(default=None)

class CommentsListResponse(BaseModel):
    """CommentsListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: Union[list[Comment], Any] = Field(default=None)

class CommentCreateParams(BaseModel):
    """CommentCreateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comment_text: Union[str, Any] = Field(default=None)
    assignee: Union[int, Any] = Field(default=None)
    notify_all: Union[bool, Any] = Field(default=None)

class CommentCreateResponse(BaseModel):
    """CommentCreateResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    hist_id: Union[str, Any] = Field(default=None)
    date: Union[int, Any] = Field(default=None)
    version: Union[dict[str, Any] | None, Any] = Field(default=None)

class CommentUpdateParams(BaseModel):
    """CommentUpdateParams type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comment_text: Union[str, Any] = Field(default=None)
    assignee: Union[int, Any] = Field(default=None)
    resolved: Union[bool, Any] = Field(default=None)

class CommentUpdateResponse(BaseModel):
    """CommentUpdateResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pass

class Goal(BaseModel):
    """Goal type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    pretty_id: Union[str | None, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    team_id: Union[str, Any] = Field(default=None)
    creator: Union[int | None, Any] = Field(default=None)
    owner: Union[dict[str, Any] | None, Any] = Field(default=None)
    color: Union[str, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    start_date: Union[str | None, Any] = Field(default=None)
    due_date: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    private: Union[bool, Any] = Field(default=None)
    archived: Union[bool, Any] = Field(default=None)
    multiple_owners: Union[bool, Any] = Field(default=None)
    members: Union[list[dict[str, Any]], Any] = Field(default=None)
    key_results: Union[list[dict[str, Any]], Any] = Field(default=None)
    percent_completed: Union[int | None, Any] = Field(default=None)
    history: Union[list[dict[str, Any]], Any] = Field(default=None)
    pretty_url: Union[str | None, Any] = Field(default=None)

class GoalsListResponse(BaseModel):
    """GoalsListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    goals: Union[list[Goal], Any] = Field(default=None)
    folders: Union[list[dict[str, Any]], Any] = Field(default=None)

class GoalResponse(BaseModel):
    """GoalResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    goal: Union[Goal, Any] = Field(default=None)

class ViewParent(BaseModel):
    """Parent reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[Any, Any] = Field(default=None, description="Parent entity ID")
    """Parent entity ID"""
    type_: Union[Any, Any] = Field(default=None, alias="type", description="Parent entity type")
    """Parent entity type"""

class View(BaseModel):
    """View type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    type_: Union[str, Any] = Field(default=None, alias="type")
    parent: Union[ViewParent, Any] = Field(default=None)
    grouping: Union[dict[str, Any], Any] = Field(default=None)
    divide: Union[dict[str, Any], Any] = Field(default=None)
    sorting: Union[dict[str, Any], Any] = Field(default=None)
    filters: Union[dict[str, Any], Any] = Field(default=None)
    columns: Union[dict[str, Any], Any] = Field(default=None)
    team_sidebar: Union[dict[str, Any], Any] = Field(default=None)
    settings: Union[dict[str, Any], Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    creator: Union[int | None, Any] = Field(default=None)
    visibility: Union[str | None, Any] = Field(default=None)
    protected: Union[bool | None, Any] = Field(default=None)
    protected_note: Union[str | None, Any] = Field(default=None)
    protected_by: Union[int | None, Any] = Field(default=None)
    date_protected: Union[str | None, Any] = Field(default=None)
    orderindex: Union[int, Any] = Field(default=None)
    public: Union[bool, Any] = Field(default=None)

class ViewsListResponse(BaseModel):
    """ViewsListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    views: Union[list[View], Any] = Field(default=None)
    required_views: Union[dict[str, Any] | None, Any] = Field(default=None)
    default_view: Union[dict[str, Any] | None, Any] = Field(default=None)

class ViewResponse(BaseModel):
    """ViewResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    view: Union[View, Any] = Field(default=None)

class TimeEntry(BaseModel):
    """TimeEntry type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    task: Union[dict[str, Any] | None, Any] = Field(default=None)
    wid: Union[str | None, Any] = Field(default=None)
    user: Union[dict[str, Any], Any] = Field(default=None)
    billable: Union[bool, Any] = Field(default=None)
    start: Union[str, Any] = Field(default=None)
    end: Union[str | None, Any] = Field(default=None)
    duration: Union[str, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    tags: Union[list[dict[str, Any]], Any] = Field(default=None)
    at: Union[str | None, Any] = Field(default=None)

class TimeEntriesListResponse(BaseModel):
    """TimeEntriesListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[list[TimeEntry], Any] = Field(default=None)

class TimeEntryResponse(BaseModel):
    """TimeEntryResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: Union[TimeEntry, Any] = Field(default=None)

class Member(BaseModel):
    """Member type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    username: Union[str, Any] = Field(default=None)
    email: Union[str, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)
    profile_picture: Union[str | None, Any] = Field(default=None, alias="profilePicture")
    initials: Union[str | None, Any] = Field(default=None)

class MembersListResponse(BaseModel):
    """MembersListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    members: Union[list[Member], Any] = Field(default=None)

class Doc(BaseModel):
    """Doc type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    type_: Union[int | None, Any] = Field(default=None, alias="type")
    parent: Union[dict[str, Any] | None, Any] = Field(default=None)
    creator: Union[int | None, Any] = Field(default=None)
    deleted: Union[bool | None, Any] = Field(default=None)
    public: Union[bool | None, Any] = Field(default=None)
    date_created: Union[int | None, Any] = Field(default=None)
    date_updated: Union[int | None, Any] = Field(default=None)
    workspace_id: Union[int | None, Any] = Field(default=None)
    content: Union[str | None, Any] = Field(default=None)

class DocsListResponse(BaseModel):
    """DocsListResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    docs: Union[list[Doc], Any] = Field(default=None)
    next_cursor: Union[str | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

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

TasksListResult = ClickupApiExecuteResult[list[Task]]
"""Result type for tasks.list operation."""

TasksApiSearchResult = ClickupApiExecuteResult[list[Task]]
"""Result type for tasks.api_search operation."""

CommentsListResult = ClickupApiExecuteResult[list[Comment]]
"""Result type for comments.list operation."""

GoalsListResult = ClickupApiExecuteResult[list[Goal]]
"""Result type for goals.list operation."""

ViewsListResult = ClickupApiExecuteResult[list[View]]
"""Result type for views.list operation."""

ViewTasksListResult = ClickupApiExecuteResult[list[Task]]
"""Result type for view_tasks.list operation."""

TimeTrackingListResult = ClickupApiExecuteResult[list[TimeEntry]]
"""Result type for time_tracking.list operation."""

MembersListResult = ClickupApiExecuteResult[list[Member]]
"""Result type for members.list operation."""

DocsListResult = ClickupApiExecuteResult[list[Doc]]
"""Result type for docs.list operation."""

