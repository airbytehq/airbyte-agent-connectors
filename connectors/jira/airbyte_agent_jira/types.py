"""
Type definitions for jira connector.
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

class IssuesApiSearchParams(TypedDict):
    """Parameters for issues.api_search operation"""
    jql: NotRequired[str]
    next_page_token: NotRequired[str]
    max_results: NotRequired[int]
    fields: NotRequired[str]
    expand: NotRequired[str]
    properties: NotRequired[str]
    fields_by_keys: NotRequired[bool]
    fail_fast: NotRequired[bool]

class IssuesGetParams(TypedDict):
    """Parameters for issues.get operation"""
    issue_id_or_key: str
    fields: NotRequired[str]
    expand: NotRequired[str]
    properties: NotRequired[str]
    fields_by_keys: NotRequired[bool]
    update_history: NotRequired[bool]
    fail_fast: NotRequired[bool]

class ProjectsApiSearchParams(TypedDict):
    """Parameters for projects.api_search operation"""
    start_at: NotRequired[int]
    max_results: NotRequired[int]
    order_by: NotRequired[str]
    id: NotRequired[list[int]]
    keys: NotRequired[list[str]]
    query: NotRequired[str]
    type_key: NotRequired[str]
    category_id: NotRequired[int]
    action: NotRequired[str]
    expand: NotRequired[str]
    status: NotRequired[list[str]]

class ProjectsGetParams(TypedDict):
    """Parameters for projects.get operation"""
    project_id_or_key: str
    expand: NotRequired[str]
    properties: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    account_id: str
    expand: NotRequired[str]

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    start_at: NotRequired[int]
    max_results: NotRequired[int]

class UsersApiSearchParams(TypedDict):
    """Parameters for users.api_search operation"""
    query: NotRequired[str]
    start_at: NotRequired[int]
    max_results: NotRequired[int]
    account_id: NotRequired[str]
    property: NotRequired[str]

class IssueFieldsListParams(TypedDict):
    """Parameters for issue_fields.list operation"""
    pass

class IssueFieldsApiSearchParams(TypedDict):
    """Parameters for issue_fields.api_search operation"""
    start_at: NotRequired[int]
    max_results: NotRequired[int]
    type: NotRequired[list[str]]
    id: NotRequired[list[str]]
    query: NotRequired[str]
    order_by: NotRequired[str]
    expand: NotRequired[str]

class IssueCommentsListParams(TypedDict):
    """Parameters for issue_comments.list operation"""
    issue_id_or_key: str
    start_at: NotRequired[int]
    max_results: NotRequired[int]
    order_by: NotRequired[str]
    expand: NotRequired[str]

class IssueCommentsGetParams(TypedDict):
    """Parameters for issue_comments.get operation"""
    issue_id_or_key: str
    comment_id: str
    expand: NotRequired[str]

class IssueWorklogsListParams(TypedDict):
    """Parameters for issue_worklogs.list operation"""
    issue_id_or_key: str
    start_at: NotRequired[int]
    max_results: NotRequired[int]
    expand: NotRequired[str]

class IssueWorklogsGetParams(TypedDict):
    """Parameters for issue_worklogs.get operation"""
    issue_id_or_key: str
    worklog_id: str
    expand: NotRequired[str]
