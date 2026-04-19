"""
Type definitions for clickup-api connector.
"""
from __future__ import annotations

from airbyte_agent_sdk.types import AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class UserGetParams(TypedDict):
    """Parameters for user.get operation"""
    pass

class TeamsListParams(TypedDict):
    """Parameters for teams.list operation"""
    pass

class SpacesListParams(TypedDict):
    """Parameters for spaces.list operation"""
    team_id: str

class SpacesGetParams(TypedDict):
    """Parameters for spaces.get operation"""
    space_id: str

class FoldersListParams(TypedDict):
    """Parameters for folders.list operation"""
    space_id: str

class FoldersGetParams(TypedDict):
    """Parameters for folders.get operation"""
    folder_id: str

class ListsListParams(TypedDict):
    """Parameters for lists.list operation"""
    folder_id: str

class ListsGetParams(TypedDict):
    """Parameters for lists.get operation"""
    list_id: str

class TasksListParams(TypedDict):
    """Parameters for tasks.list operation"""
    list_id: str
    page: NotRequired[int]

class TasksGetParams(TypedDict):
    """Parameters for tasks.get operation"""
    task_id: str
    custom_task_ids: NotRequired[bool]
    include_subtasks: NotRequired[bool]

class TasksApiSearchParams(TypedDict):
    """Parameters for tasks.api_search operation"""
    team_id: str
    search: NotRequired[str]
    statuses: NotRequired[list[str]]
    assignees: NotRequired[list[str]]
    tags: NotRequired[list[str]]
    priority: NotRequired[int]
    due_date_gt: NotRequired[int]
    due_date_lt: NotRequired[int]
    date_created_gt: NotRequired[int]
    date_created_lt: NotRequired[int]
    date_updated_gt: NotRequired[int]
    date_updated_lt: NotRequired[int]
    custom_fields: NotRequired[list[dict[str, Any]]]
    include_closed: NotRequired[bool]
    page: NotRequired[int]

class CommentsListParams(TypedDict):
    """Parameters for comments.list operation"""
    task_id: str

class CommentsCreateParams(TypedDict):
    """Parameters for comments.create operation"""
    comment_text: str
    assignee: NotRequired[int]
    notify_all: NotRequired[bool]
    task_id: str

class CommentsGetParams(TypedDict):
    """Parameters for comments.get operation"""
    comment_id: str

class CommentsUpdateParams(TypedDict):
    """Parameters for comments.update operation"""
    comment_text: NotRequired[str]
    assignee: NotRequired[int]
    resolved: NotRequired[bool]
    comment_id: str

class GoalsListParams(TypedDict):
    """Parameters for goals.list operation"""
    team_id: str

class GoalsGetParams(TypedDict):
    """Parameters for goals.get operation"""
    goal_id: str

class ViewsListParams(TypedDict):
    """Parameters for views.list operation"""
    team_id: str

class ViewsGetParams(TypedDict):
    """Parameters for views.get operation"""
    view_id: str

class ViewTasksListParams(TypedDict):
    """Parameters for view_tasks.list operation"""
    view_id: str
    page: NotRequired[int]

class TimeTrackingListParams(TypedDict):
    """Parameters for time_tracking.list operation"""
    team_id: str
    start_date: NotRequired[int]
    end_date: NotRequired[int]
    assignee: NotRequired[str]

class TimeTrackingGetParams(TypedDict):
    """Parameters for time_tracking.get operation"""
    team_id: str
    time_entry_id: str

class MembersListParams(TypedDict):
    """Parameters for members.list operation"""
    task_id: str

class DocsListParams(TypedDict):
    """Parameters for docs.list operation"""
    workspace_id: str
    cursor: NotRequired[str]

class DocsGetParams(TypedDict):
    """Parameters for docs.get operation"""
    workspace_id: str
    doc_id: str

