"""
Type definitions for linear connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class IssuesListParams(TypedDict):
    """Parameters for issues.list operation"""
    first: NotRequired[int]
    after: NotRequired[str]

class IssuesGetParams(TypedDict):
    """Parameters for issues.get operation"""
    id: str

class IssuesCreateParams(TypedDict):
    """Parameters for issues.create operation"""
    team_id: str
    title: str
    description: NotRequired[str]
    state_id: NotRequired[str]
    priority: NotRequired[int]

class IssuesUpdateParams(TypedDict):
    """Parameters for issues.update operation"""
    id: str
    title: NotRequired[str]
    description: NotRequired[str]
    state_id: NotRequired[str]
    priority: NotRequired[int]
    assignee_id: NotRequired[str]

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

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    first: NotRequired[int]
    after: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class CommentsListParams(TypedDict):
    """Parameters for comments.list operation"""
    issue_id: str
    first: NotRequired[int]
    after: NotRequired[str]

class CommentsGetParams(TypedDict):
    """Parameters for comments.get operation"""
    id: str

class CommentsCreateParams(TypedDict):
    """Parameters for comments.create operation"""
    issue_id: str
    body: str

class CommentsUpdateParams(TypedDict):
    """Parameters for comments.update operation"""
    id: str
    body: str

