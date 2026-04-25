"""
Pydantic models for linear connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class LinearAuthConfig(BaseModel):
    """Linear API Key Authentication - Authenticate using your Linear API key"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Linear API key from Settings > API > Personal API keys"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Issue(BaseModel):
    """Linear issue object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    title: str
    description: Any | None = Field(default=None)
    state: Any | None = Field(default=None)
    priority: Any | None = Field(default=None)
    assignee: Any | None = Field(default=None)
    team: Any | None = Field(default=None)
    project: Any | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class IssuesListResponseDataIssuesPageinfo(BaseModel):
    """Pagination information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None, alias="hasNextPage", description="Whether there are more items available")
    """Whether there are more items available"""
    end_cursor: str | None | None = Field(default=None, alias="endCursor", description="Cursor to fetch next page")
    """Cursor to fetch next page"""

class IssuesListResponseDataIssues(BaseModel):
    """Nested schema for IssuesListResponseData.issues"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    nodes: list[Issue] | None = Field(default=None)
    page_info: IssuesListResponseDataIssuesPageinfo | None = Field(default=None, alias="pageInfo", description="Pagination information")
    """Pagination information"""

class IssuesListResponseData(BaseModel):
    """Nested schema for IssuesListResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issues: IssuesListResponseDataIssues | None = Field(default=None)

class IssuesListResponse(BaseModel):
    """GraphQL response for issues list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: IssuesListResponseData | None = Field(default=None)

class IssueResponseData(BaseModel):
    """Nested schema for IssueResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issue: Issue | None = Field(default=None)

class IssueResponse(BaseModel):
    """GraphQL response for single issue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: IssueResponseData | None = Field(default=None)

class Project(BaseModel):
    """Linear project object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    name: str
    description: Any | None = Field(default=None)
    state: Any | None = Field(default=None)
    start_date: Any | None = Field(default=None, alias="startDate")
    target_date: Any | None = Field(default=None, alias="targetDate")
    lead: Any | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class ProjectsListResponseDataProjectsPageinfo(BaseModel):
    """Pagination information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None, alias="hasNextPage", description="Whether there are more items available")
    """Whether there are more items available"""
    end_cursor: str | None | None = Field(default=None, alias="endCursor", description="Cursor to fetch next page")
    """Cursor to fetch next page"""

class ProjectsListResponseDataProjects(BaseModel):
    """Nested schema for ProjectsListResponseData.projects"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    nodes: list[Project] | None = Field(default=None)
    page_info: ProjectsListResponseDataProjectsPageinfo | None = Field(default=None, alias="pageInfo", description="Pagination information")
    """Pagination information"""

class ProjectsListResponseData(BaseModel):
    """Nested schema for ProjectsListResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    projects: ProjectsListResponseDataProjects | None = Field(default=None)

class ProjectsListResponse(BaseModel):
    """GraphQL response for projects list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: ProjectsListResponseData | None = Field(default=None)

class ProjectResponseData(BaseModel):
    """Nested schema for ProjectResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    project: Project | None = Field(default=None)

class ProjectResponse(BaseModel):
    """GraphQL response for single project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: ProjectResponseData | None = Field(default=None)

class ProjectCreateParams(BaseModel):
    """Parameters for creating a project"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    team_ids: list[str] = Field(alias="teamIds")
    description: str | None = Field(default=None)
    state: str | None = Field(default=None)
    start_date: str | None = Field(default=None, alias="startDate")
    target_date: str | None = Field(default=None, alias="targetDate")
    lead_id: str | None = Field(default=None, alias="leadId")

class ProjectUpdateParams(BaseModel):
    """Parameters for updating a project. All fields except id are optional for partial updates.
Use this to rename projects, change descriptions, update dates, or change the project state.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    state: str | None = Field(default=None)
    start_date: str | None = Field(default=None, alias="startDate")
    target_date: str | None = Field(default=None, alias="targetDate")
    lead_id: str | None = Field(default=None, alias="leadId")

class ProjectMutationPayload(BaseModel):
    """Project mutation result"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    success: bool | None = Field(default=None)
    project: Project | None = Field(default=None)

class ProjectCreateResponseData(BaseModel):
    """Nested schema for ProjectCreateResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    project_create: ProjectMutationPayload | None = Field(default=None, alias="projectCreate")

class ProjectCreateResponse(BaseModel):
    """GraphQL response for project creation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: ProjectCreateResponseData | None = Field(default=None)

class ProjectUpdateResponseData(BaseModel):
    """Nested schema for ProjectUpdateResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    project_update: ProjectMutationPayload | None = Field(default=None, alias="projectUpdate")

class ProjectUpdateResponse(BaseModel):
    """GraphQL response for project update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: ProjectUpdateResponseData | None = Field(default=None)

class Team(BaseModel):
    """Linear team object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    name: str
    key: str
    description: Any | None = Field(default=None)
    timezone: Any | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class TeamsListResponseDataTeamsPageinfo(BaseModel):
    """Pagination information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None, alias="hasNextPage", description="Whether there are more items available")
    """Whether there are more items available"""
    end_cursor: str | None | None = Field(default=None, alias="endCursor", description="Cursor to fetch next page")
    """Cursor to fetch next page"""

class TeamsListResponseDataTeams(BaseModel):
    """Nested schema for TeamsListResponseData.teams"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    nodes: list[Team] | None = Field(default=None)
    page_info: TeamsListResponseDataTeamsPageinfo | None = Field(default=None, alias="pageInfo", description="Pagination information")
    """Pagination information"""

class TeamsListResponseData(BaseModel):
    """Nested schema for TeamsListResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    teams: TeamsListResponseDataTeams | None = Field(default=None)

class TeamsListResponse(BaseModel):
    """GraphQL response for teams list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: TeamsListResponseData | None = Field(default=None)

class TeamResponseData(BaseModel):
    """Nested schema for TeamResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    team: Team | None = Field(default=None)

class TeamResponse(BaseModel):
    """GraphQL response for single team"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: TeamResponseData | None = Field(default=None)

class WorkflowState(BaseModel):
    """Linear workflow state object representing a status in a team's workflow"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    name: str
    type_: str = Field(alias="type")
    position: Any | None = Field(default=None)
    color: Any | None = Field(default=None)
    team: Any | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class WorkflowStatesListResponseDataWorkflowstatesPageinfo(BaseModel):
    """Pagination information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None, alias="hasNextPage", description="Whether there are more items available")
    """Whether there are more items available"""
    end_cursor: str | None | None = Field(default=None, alias="endCursor", description="Cursor to fetch next page")
    """Cursor to fetch next page"""

class WorkflowStatesListResponseDataWorkflowstates(BaseModel):
    """Nested schema for WorkflowStatesListResponseData.workflowStates"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    nodes: list[WorkflowState] | None = Field(default=None)
    page_info: WorkflowStatesListResponseDataWorkflowstatesPageinfo | None = Field(default=None, alias="pageInfo", description="Pagination information")
    """Pagination information"""

class WorkflowStatesListResponseData(BaseModel):
    """Nested schema for WorkflowStatesListResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    workflow_states: WorkflowStatesListResponseDataWorkflowstates | None = Field(default=None, alias="workflowStates")

class WorkflowStatesListResponse(BaseModel):
    """GraphQL response for workflow states list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: WorkflowStatesListResponseData | None = Field(default=None)

class IssueCreateParams(BaseModel):
    """Parameters for creating an issue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    team_id: str = Field(alias="teamId")
    title: str
    description: str | None = Field(default=None)
    state_id: str | None = Field(default=None, alias="stateId")
    priority: int | None = Field(default=None)
    project_id: str | None = Field(default=None, alias="projectId")

class IssueUpdateParams(BaseModel):
    """Parameters for updating an issue. All fields except id are optional for partial updates.
To assign a user, provide assigneeId with the user's ID (get user IDs from the users list).
To unassign the current user, set assigneeId to null.
Omit assigneeId to leave the current assignee unchanged.
"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    title: str | None = Field(default=None)
    description: str | None = Field(default=None)
    state_id: str | None = Field(default=None, alias="stateId")
    priority: int | None = Field(default=None)
    assignee_id: str | None = Field(default=None, alias="assigneeId")
    project_id: str | None = Field(default=None, alias="projectId")

class IssueWithState(BaseModel):
    """Issue object with state ID and assignee ID included"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    description: Any | None = Field(default=None)
    state: Any | None = Field(default=None)
    priority: Any | None = Field(default=None)
    assignee: Any | None = Field(default=None)
    project: Any | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class IssueMutationPayload(BaseModel):
    """Issue mutation result"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    success: bool | None = Field(default=None)
    issue: IssueWithState | None = Field(default=None)

class IssueCreateResponseData(BaseModel):
    """Nested schema for IssueCreateResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issue_create: IssueMutationPayload | None = Field(default=None, alias="issueCreate")

class IssueCreateResponse(BaseModel):
    """GraphQL response for issue creation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: IssueCreateResponseData | None = Field(default=None)

class IssueUpdateResponseData(BaseModel):
    """Nested schema for IssueUpdateResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issue_update: IssueMutationPayload | None = Field(default=None, alias="issueUpdate")

class IssueUpdateResponse(BaseModel):
    """GraphQL response for issue update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: IssueUpdateResponseData | None = Field(default=None)

class User(BaseModel):
    """Linear user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    name: str
    email: str
    display_name: Any | None = Field(default=None, alias="displayName")
    active: bool | None = Field(default=None)
    admin: bool | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class UsersListResponseDataUsersPageinfo(BaseModel):
    """Pagination information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None, alias="hasNextPage", description="Whether there are more items available")
    """Whether there are more items available"""
    end_cursor: str | None | None = Field(default=None, alias="endCursor", description="Cursor to fetch next page")
    """Cursor to fetch next page"""

class UsersListResponseDataUsers(BaseModel):
    """Nested schema for UsersListResponseData.users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    nodes: list[User] | None = Field(default=None)
    page_info: UsersListResponseDataUsersPageinfo | None = Field(default=None, alias="pageInfo", description="Pagination information")
    """Pagination information"""

class UsersListResponseData(BaseModel):
    """Nested schema for UsersListResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    users: UsersListResponseDataUsers | None = Field(default=None)

class UsersListResponse(BaseModel):
    """GraphQL response for users list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: UsersListResponseData | None = Field(default=None)

class UserResponseData(BaseModel):
    """Nested schema for UserResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user: User | None = Field(default=None)

class UserResponse(BaseModel):
    """GraphQL response for single user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: UserResponseData | None = Field(default=None)

class Comment(BaseModel):
    """Linear comment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    body: str
    user: Any | None = Field(default=None)
    issue: Any | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class CommentsListResponseDataIssueCommentsPageinfo(BaseModel):
    """Pagination information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None, alias="hasNextPage", description="Whether there are more items available")
    """Whether there are more items available"""
    end_cursor: str | None | None = Field(default=None, alias="endCursor", description="Cursor to fetch next page")
    """Cursor to fetch next page"""

class CommentsListResponseDataIssueComments(BaseModel):
    """Nested schema for CommentsListResponseDataIssue.comments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    nodes: list[Comment] | None = Field(default=None)
    page_info: CommentsListResponseDataIssueCommentsPageinfo | None = Field(default=None, alias="pageInfo", description="Pagination information")
    """Pagination information"""

class CommentsListResponseDataIssue(BaseModel):
    """Nested schema for CommentsListResponseData.issue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comments: CommentsListResponseDataIssueComments | None = Field(default=None)

class CommentsListResponseData(BaseModel):
    """Nested schema for CommentsListResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issue: CommentsListResponseDataIssue | None = Field(default=None)

class CommentsListResponse(BaseModel):
    """GraphQL response for comments list"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: CommentsListResponseData | None = Field(default=None)

class CommentResponseData(BaseModel):
    """Nested schema for CommentResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comment: Comment | None = Field(default=None)

class CommentResponse(BaseModel):
    """GraphQL response for single comment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: CommentResponseData | None = Field(default=None)

class CommentCreateParams(BaseModel):
    """Parameters for creating a comment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issue_id: str = Field(alias="issueId")
    body: str

class CommentUpdateParams(BaseModel):
    """Parameters for updating a comment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    body: str

class CommentMutationPayload(BaseModel):
    """Comment mutation result"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    success: bool | None = Field(default=None)
    comment: Comment | None = Field(default=None)

class CommentCreateResponseData(BaseModel):
    """Nested schema for CommentCreateResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comment_create: CommentMutationPayload | None = Field(default=None, alias="commentCreate")

class CommentCreateResponse(BaseModel):
    """GraphQL response for comment creation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: CommentCreateResponseData | None = Field(default=None)

class CommentUpdateResponseData(BaseModel):
    """Nested schema for CommentUpdateResponse.data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    comment_update: CommentMutationPayload | None = Field(default=None, alias="commentUpdate")

class CommentUpdateResponse(BaseModel):
    """GraphQL response for comment update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: CommentUpdateResponseData | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class IssuesListResultMeta(BaseModel):
    """Metadata for issues.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None, alias="hasNextPage")
    end_cursor: str | None = Field(default=None, alias="endCursor")

class ProjectsListResultMeta(BaseModel):
    """Metadata for projects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None, alias="hasNextPage")
    end_cursor: str | None = Field(default=None, alias="endCursor")

class TeamsListResultMeta(BaseModel):
    """Metadata for teams.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None, alias="hasNextPage")
    end_cursor: str | None = Field(default=None, alias="endCursor")

class WorkflowStatesListResultMeta(BaseModel):
    """Metadata for workflow_states.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None, alias="hasNextPage")
    end_cursor: str | None = Field(default=None, alias="endCursor")

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None, alias="hasNextPage")
    end_cursor: str | None = Field(default=None, alias="endCursor")

class CommentsListResultMeta(BaseModel):
    """Metadata for comments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_next_page: bool | None = Field(default=None, alias="hasNextPage")
    end_cursor: str | None = Field(default=None, alias="endCursor")

# ===== CHECK RESULT MODEL =====

class LinearCheckResult(BaseModel):
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


class LinearExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class LinearExecuteResultWithMeta(LinearExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class CommentsSearchData(BaseModel):
    """Search result data for comments entity."""
    model_config = ConfigDict(extra="allow")

    body: str | None = None
    """"""
    body_data: str | None = None
    """"""
    created_at: str | None = None
    """"""
    edited_at: str | None = None
    """"""
    id: str | None = None
    """"""
    issue: dict[str, Any] | None = None
    """"""
    issue_id: str | None = None
    """"""
    parent: dict[str, Any] | None = None
    """"""
    parent_comment_id: str | None = None
    """"""
    resolving_comment_id: str | None = None
    """"""
    resolving_user_id: str | None = None
    """"""
    updated_at: str | None = None
    """"""
    url: str | None = None
    """"""
    user: dict[str, Any] | None = None
    """"""
    user_id: str | None = None
    """"""


class IssuesSearchData(BaseModel):
    """Search result data for issues entity."""
    model_config = ConfigDict(extra="allow")

    added_to_cycle_at: str | None = None
    """"""
    added_to_project_at: str | None = None
    """"""
    added_to_team_at: str | None = None
    """"""
    assignee: dict[str, Any] | None = None
    """"""
    assignee_id: str | None = None
    """"""
    attachment_ids: list[Any] | None = None
    """"""
    attachments: dict[str, Any] | None = None
    """"""
    branch_name: str | None = None
    """"""
    canceled_at: str | None = None
    """"""
    completed_at: str | None = None
    """"""
    created_at: str | None = None
    """"""
    creator: dict[str, Any] | None = None
    """"""
    creator_id: str | None = None
    """"""
    customer_ticket_count: float | None = None
    """"""
    cycle: dict[str, Any] | None = None
    """"""
    cycle_id: str | None = None
    """"""
    description: str | None = None
    """"""
    description_state: str | None = None
    """"""
    due_date: str | None = None
    """"""
    estimate: float | None = None
    """"""
    id: str | None = None
    """"""
    identifier: str | None = None
    """"""
    integration_source_type: str | None = None
    """"""
    label_ids: list[Any] | None = None
    """"""
    labels: dict[str, Any] | None = None
    """"""
    milestone_id: str | None = None
    """"""
    number: float | None = None
    """"""
    parent: dict[str, Any] | None = None
    """"""
    parent_id: str | None = None
    """"""
    previous_identifiers: list[Any] | None = None
    """"""
    priority: float | None = None
    """"""
    priority_label: str | None = None
    """"""
    priority_sort_order: float | None = None
    """"""
    project: dict[str, Any] | None = None
    """"""
    project_id: str | None = None
    """"""
    project_milestone: dict[str, Any] | None = None
    """"""
    reaction_data: list[Any] | None = None
    """"""
    relation_ids: list[Any] | None = None
    """"""
    relations: dict[str, Any] | None = None
    """"""
    sla_type: str | None = None
    """"""
    sort_order: float | None = None
    """"""
    source_comment_id: str | None = None
    """"""
    started_at: str | None = None
    """"""
    state: dict[str, Any] | None = None
    """"""
    state_id: str | None = None
    """"""
    sub_issue_sort_order: float | None = None
    """"""
    subscriber_ids: list[Any] | None = None
    """"""
    subscribers: dict[str, Any] | None = None
    """"""
    team: dict[str, Any] | None = None
    """"""
    team_id: str | None = None
    """"""
    title: str | None = None
    """"""
    updated_at: str | None = None
    """"""
    url: str | None = None
    """"""


class ProjectsSearchData(BaseModel):
    """Search result data for projects entity."""
    model_config = ConfigDict(extra="allow")

    canceled_at: str | None = None
    """"""
    color: str | None = None
    """"""
    completed_at: str | None = None
    """"""
    completed_issue_count_history: list[Any] | None = None
    """"""
    completed_scope_history: list[Any] | None = None
    """"""
    content: str | None = None
    """"""
    content_state: str | None = None
    """"""
    converted_from_issue: dict[str, Any] | None = None
    """"""
    converted_from_issue_id: str | None = None
    """"""
    created_at: str | None = None
    """"""
    creator: dict[str, Any] | None = None
    """"""
    creator_id: str | None = None
    """"""
    description: str | None = None
    """"""
    health: str | None = None
    """"""
    health_updated_at: str | None = None
    """"""
    icon: str | None = None
    """"""
    id: str | None = None
    """"""
    in_progress_scope_history: list[Any] | None = None
    """"""
    issue_count_history: list[Any] | None = None
    """"""
    lead: dict[str, Any] | None = None
    """"""
    lead_id: str | None = None
    """"""
    name: str | None = None
    """"""
    priority: float | None = None
    """"""
    priority_sort_order: float | None = None
    """"""
    progress: float | None = None
    """"""
    scope: float | None = None
    """"""
    scope_history: list[Any] | None = None
    """"""
    slug_id: str | None = None
    """"""
    sort_order: float | None = None
    """"""
    start_date: str | None = None
    """"""
    started_at: str | None = None
    """"""
    status: dict[str, Any] | None = None
    """"""
    status_id: str | None = None
    """"""
    target_date: str | None = None
    """"""
    team_ids: list[Any] | None = None
    """"""
    teams: dict[str, Any] | None = None
    """"""
    update_reminders_day: str | None = None
    """"""
    update_reminders_hour: float | None = None
    """"""
    updated_at: str | None = None
    """"""
    url: str | None = None
    """"""


class TeamsSearchData(BaseModel):
    """Search result data for teams entity."""
    model_config = ConfigDict(extra="allow")

    active_cycle: dict[str, Any] | None = None
    """"""
    active_cycle_id: str | None = None
    """"""
    auto_archive_period: float | None = None
    """"""
    auto_close_period: float | None = None
    """"""
    auto_close_state_id: str | None = None
    """"""
    color: str | None = None
    """"""
    created_at: str | None = None
    """"""
    cycle_calender_url: str | None = None
    """"""
    cycle_cooldown_time: float | None = None
    """"""
    cycle_duration: float | None = None
    """"""
    cycle_issue_auto_assign_completed: bool | None = None
    """"""
    cycle_issue_auto_assign_started: bool | None = None
    """"""
    cycle_lock_to_active: bool | None = None
    """"""
    cycle_start_day: float | None = None
    """"""
    cycles_enabled: bool | None = None
    """"""
    default_issue_estimate: float | None = None
    """"""
    default_issue_state: dict[str, Any] | None = None
    """"""
    default_issue_state_id: str | None = None
    """"""
    group_issue_history: bool | None = None
    """"""
    icon: str | None = None
    """"""
    id: str | None = None
    """"""
    invite_hash: str | None = None
    """"""
    issue_count: float | None = None
    """"""
    issue_estimation_allow_zero: bool | None = None
    """"""
    issue_estimation_extended: bool | None = None
    """"""
    issue_estimation_type: str | None = None
    """"""
    key: str | None = None
    """"""
    marked_as_duplicate_workflow_state: dict[str, Any] | None = None
    """"""
    marked_as_duplicate_workflow_state_id: str | None = None
    """"""
    name: str | None = None
    """"""
    parent_team_id: str | None = None
    """"""
    private: bool | None = None
    """"""
    require_priority_to_leave_triage: bool | None = None
    """"""
    scim_managed: bool | None = None
    """"""
    set_issue_sort_order_on_state_change: str | None = None
    """"""
    timezone: str | None = None
    """"""
    triage_enabled: bool | None = None
    """"""
    triage_issue_state_id: str | None = None
    """"""
    upcoming_cycle_count: float | None = None
    """"""
    updated_at: str | None = None
    """"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    active: bool | None = None
    """"""
    admin: bool | None = None
    """"""
    avatar_background_color: str | None = None
    """"""
    avatar_url: str | None = None
    """"""
    created_at: str | None = None
    """"""
    created_issue_count: float | None = None
    """"""
    display_name: str | None = None
    """"""
    email: str | None = None
    """"""
    guest: bool | None = None
    """"""
    id: str | None = None
    """"""
    initials: str | None = None
    """"""
    invite_hash: str | None = None
    """"""
    is_me: bool | None = None
    """"""
    last_seen: str | None = None
    """"""
    name: str | None = None
    """"""
    team_ids: list[Any] | None = None
    """"""
    teams: dict[str, Any] | None = None
    """"""
    timezone: str | None = None
    """"""
    updated_at: str | None = None
    """"""
    url: str | None = None
    """"""


class WorkflowStatesSearchData(BaseModel):
    """Search result data for workflow_states entity."""
    model_config = ConfigDict(extra="allow")

    color: str | None = None
    """"""
    created_at: str | None = None
    """"""
    description: str | None = None
    """"""
    id: str | None = None
    """"""
    inherited_from_id: str | None = None
    """"""
    name: str | None = None
    """"""
    position: float | None = None
    """"""
    team: dict[str, Any] | None = None
    """"""
    team_id: str | None = None
    """"""
    type_: str | None = None
    """"""
    updated_at: str | None = None
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

CommentsSearchResult = AirbyteSearchResult[CommentsSearchData]
"""Search result type for comments entity."""

IssuesSearchResult = AirbyteSearchResult[IssuesSearchData]
"""Search result type for issues entity."""

ProjectsSearchResult = AirbyteSearchResult[ProjectsSearchData]
"""Search result type for projects entity."""

TeamsSearchResult = AirbyteSearchResult[TeamsSearchData]
"""Search result type for teams entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""

WorkflowStatesSearchResult = AirbyteSearchResult[WorkflowStatesSearchData]
"""Search result type for workflow_states entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

IssuesListResult = LinearExecuteResultWithMeta[list[Issue], IssuesListResultMeta]
"""Result type for issues.list operation with data and metadata."""

ProjectsListResult = LinearExecuteResultWithMeta[list[Project], ProjectsListResultMeta]
"""Result type for projects.list operation with data and metadata."""

TeamsListResult = LinearExecuteResultWithMeta[list[Team], TeamsListResultMeta]
"""Result type for teams.list operation with data and metadata."""

WorkflowStatesListResult = LinearExecuteResultWithMeta[list[WorkflowState], WorkflowStatesListResultMeta]
"""Result type for workflow_states.list operation with data and metadata."""

UsersListResult = LinearExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

CommentsListResult = LinearExecuteResultWithMeta[list[Comment], CommentsListResultMeta]
"""Result type for comments.list operation with data and metadata."""

