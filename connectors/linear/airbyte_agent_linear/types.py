"""
Type definitions for linear connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


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

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== COMMENTS SEARCH TYPES =====

class CommentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering comments search queries."""
    body: str | None
    """"""
    body_data: str | None
    """"""
    created_at: str | None
    """"""
    edited_at: str | None
    """"""
    id: str | None
    """"""
    issue: dict[str, Any] | None
    """"""
    issue_id: str | None
    """"""
    parent: dict[str, Any] | None
    """"""
    parent_comment_id: str | None
    """"""
    resolving_comment_id: str | None
    """"""
    resolving_user_id: str | None
    """"""
    updated_at: str | None
    """"""
    url: str | None
    """"""
    user: dict[str, Any] | None
    """"""
    user_id: str | None
    """"""


class CommentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    body: list[str]
    """"""
    body_data: list[str]
    """"""
    created_at: list[str]
    """"""
    edited_at: list[str]
    """"""
    id: list[str]
    """"""
    issue: list[dict[str, Any]]
    """"""
    issue_id: list[str]
    """"""
    parent: list[dict[str, Any]]
    """"""
    parent_comment_id: list[str]
    """"""
    resolving_comment_id: list[str]
    """"""
    resolving_user_id: list[str]
    """"""
    updated_at: list[str]
    """"""
    url: list[str]
    """"""
    user: list[dict[str, Any]]
    """"""
    user_id: list[str]
    """"""


class CommentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    body: Any
    """"""
    body_data: Any
    """"""
    created_at: Any
    """"""
    edited_at: Any
    """"""
    id: Any
    """"""
    issue: Any
    """"""
    issue_id: Any
    """"""
    parent: Any
    """"""
    parent_comment_id: Any
    """"""
    resolving_comment_id: Any
    """"""
    resolving_user_id: Any
    """"""
    updated_at: Any
    """"""
    url: Any
    """"""
    user: Any
    """"""
    user_id: Any
    """"""


class CommentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    body: str
    """"""
    body_data: str
    """"""
    created_at: str
    """"""
    edited_at: str
    """"""
    id: str
    """"""
    issue: str
    """"""
    issue_id: str
    """"""
    parent: str
    """"""
    parent_comment_id: str
    """"""
    resolving_comment_id: str
    """"""
    resolving_user_id: str
    """"""
    updated_at: str
    """"""
    url: str
    """"""
    user: str
    """"""
    user_id: str
    """"""


class CommentsSortFilter(TypedDict, total=False):
    """Available fields for sorting comments search results."""
    body: AirbyteSortOrder
    """"""
    body_data: AirbyteSortOrder
    """"""
    created_at: AirbyteSortOrder
    """"""
    edited_at: AirbyteSortOrder
    """"""
    id: AirbyteSortOrder
    """"""
    issue: AirbyteSortOrder
    """"""
    issue_id: AirbyteSortOrder
    """"""
    parent: AirbyteSortOrder
    """"""
    parent_comment_id: AirbyteSortOrder
    """"""
    resolving_comment_id: AirbyteSortOrder
    """"""
    resolving_user_id: AirbyteSortOrder
    """"""
    updated_at: AirbyteSortOrder
    """"""
    url: AirbyteSortOrder
    """"""
    user: AirbyteSortOrder
    """"""
    user_id: AirbyteSortOrder
    """"""


# Entity-specific condition types for comments
class CommentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CommentsSearchFilter


class CommentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CommentsSearchFilter


class CommentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CommentsSearchFilter


class CommentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CommentsSearchFilter


class CommentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CommentsSearchFilter


class CommentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CommentsSearchFilter


class CommentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CommentsStringFilter


class CommentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CommentsStringFilter


class CommentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CommentsStringFilter


class CommentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CommentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CommentsInCondition = TypedDict("CommentsInCondition", {"in": CommentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CommentsNotCondition = TypedDict("CommentsNotCondition", {"not": "CommentsCondition"}, total=False)
"""Negates the nested condition."""

CommentsAndCondition = TypedDict("CommentsAndCondition", {"and": "list[CommentsCondition]"}, total=False)
"""True if all nested conditions are true."""

CommentsOrCondition = TypedDict("CommentsOrCondition", {"or": "list[CommentsCondition]"}, total=False)
"""True if any nested condition is true."""

CommentsAnyCondition = TypedDict("CommentsAnyCondition", {"any": CommentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all comments condition types
CommentsCondition = (
    CommentsEqCondition
    | CommentsNeqCondition
    | CommentsGtCondition
    | CommentsGteCondition
    | CommentsLtCondition
    | CommentsLteCondition
    | CommentsInCondition
    | CommentsLikeCondition
    | CommentsFuzzyCondition
    | CommentsKeywordCondition
    | CommentsContainsCondition
    | CommentsNotCondition
    | CommentsAndCondition
    | CommentsOrCondition
    | CommentsAnyCondition
)


class CommentsSearchQuery(TypedDict, total=False):
    """Search query for comments entity."""
    filter: CommentsCondition
    sort: list[CommentsSortFilter]


# ===== ISSUES SEARCH TYPES =====

class IssuesSearchFilter(TypedDict, total=False):
    """Available fields for filtering issues search queries."""
    added_to_cycle_at: str | None
    """"""
    added_to_project_at: str | None
    """"""
    added_to_team_at: str | None
    """"""
    assignee: dict[str, Any] | None
    """"""
    assignee_id: str | None
    """"""
    attachment_ids: list[Any] | None
    """"""
    attachments: dict[str, Any] | None
    """"""
    branch_name: str | None
    """"""
    canceled_at: str | None
    """"""
    completed_at: str | None
    """"""
    created_at: str | None
    """"""
    creator: dict[str, Any] | None
    """"""
    creator_id: str | None
    """"""
    customer_ticket_count: float | None
    """"""
    cycle: dict[str, Any] | None
    """"""
    cycle_id: str | None
    """"""
    description: str | None
    """"""
    description_state: str | None
    """"""
    due_date: str | None
    """"""
    estimate: float | None
    """"""
    id: str | None
    """"""
    identifier: str | None
    """"""
    integration_source_type: str | None
    """"""
    label_ids: list[Any] | None
    """"""
    labels: dict[str, Any] | None
    """"""
    milestone_id: str | None
    """"""
    number: float | None
    """"""
    parent: dict[str, Any] | None
    """"""
    parent_id: str | None
    """"""
    previous_identifiers: list[Any] | None
    """"""
    priority: float | None
    """"""
    priority_label: str | None
    """"""
    priority_sort_order: float | None
    """"""
    project: dict[str, Any] | None
    """"""
    project_id: str | None
    """"""
    project_milestone: dict[str, Any] | None
    """"""
    reaction_data: list[Any] | None
    """"""
    relation_ids: list[Any] | None
    """"""
    relations: dict[str, Any] | None
    """"""
    sla_type: str | None
    """"""
    sort_order: float | None
    """"""
    source_comment_id: str | None
    """"""
    started_at: str | None
    """"""
    state: dict[str, Any] | None
    """"""
    state_id: str | None
    """"""
    sub_issue_sort_order: float | None
    """"""
    subscriber_ids: list[Any] | None
    """"""
    subscribers: dict[str, Any] | None
    """"""
    team: dict[str, Any] | None
    """"""
    team_id: str | None
    """"""
    title: str | None
    """"""
    updated_at: str | None
    """"""
    url: str | None
    """"""


class IssuesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    added_to_cycle_at: list[str]
    """"""
    added_to_project_at: list[str]
    """"""
    added_to_team_at: list[str]
    """"""
    assignee: list[dict[str, Any]]
    """"""
    assignee_id: list[str]
    """"""
    attachment_ids: list[list[Any]]
    """"""
    attachments: list[dict[str, Any]]
    """"""
    branch_name: list[str]
    """"""
    canceled_at: list[str]
    """"""
    completed_at: list[str]
    """"""
    created_at: list[str]
    """"""
    creator: list[dict[str, Any]]
    """"""
    creator_id: list[str]
    """"""
    customer_ticket_count: list[float]
    """"""
    cycle: list[dict[str, Any]]
    """"""
    cycle_id: list[str]
    """"""
    description: list[str]
    """"""
    description_state: list[str]
    """"""
    due_date: list[str]
    """"""
    estimate: list[float]
    """"""
    id: list[str]
    """"""
    identifier: list[str]
    """"""
    integration_source_type: list[str]
    """"""
    label_ids: list[list[Any]]
    """"""
    labels: list[dict[str, Any]]
    """"""
    milestone_id: list[str]
    """"""
    number: list[float]
    """"""
    parent: list[dict[str, Any]]
    """"""
    parent_id: list[str]
    """"""
    previous_identifiers: list[list[Any]]
    """"""
    priority: list[float]
    """"""
    priority_label: list[str]
    """"""
    priority_sort_order: list[float]
    """"""
    project: list[dict[str, Any]]
    """"""
    project_id: list[str]
    """"""
    project_milestone: list[dict[str, Any]]
    """"""
    reaction_data: list[list[Any]]
    """"""
    relation_ids: list[list[Any]]
    """"""
    relations: list[dict[str, Any]]
    """"""
    sla_type: list[str]
    """"""
    sort_order: list[float]
    """"""
    source_comment_id: list[str]
    """"""
    started_at: list[str]
    """"""
    state: list[dict[str, Any]]
    """"""
    state_id: list[str]
    """"""
    sub_issue_sort_order: list[float]
    """"""
    subscriber_ids: list[list[Any]]
    """"""
    subscribers: list[dict[str, Any]]
    """"""
    team: list[dict[str, Any]]
    """"""
    team_id: list[str]
    """"""
    title: list[str]
    """"""
    updated_at: list[str]
    """"""
    url: list[str]
    """"""


class IssuesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    added_to_cycle_at: Any
    """"""
    added_to_project_at: Any
    """"""
    added_to_team_at: Any
    """"""
    assignee: Any
    """"""
    assignee_id: Any
    """"""
    attachment_ids: Any
    """"""
    attachments: Any
    """"""
    branch_name: Any
    """"""
    canceled_at: Any
    """"""
    completed_at: Any
    """"""
    created_at: Any
    """"""
    creator: Any
    """"""
    creator_id: Any
    """"""
    customer_ticket_count: Any
    """"""
    cycle: Any
    """"""
    cycle_id: Any
    """"""
    description: Any
    """"""
    description_state: Any
    """"""
    due_date: Any
    """"""
    estimate: Any
    """"""
    id: Any
    """"""
    identifier: Any
    """"""
    integration_source_type: Any
    """"""
    label_ids: Any
    """"""
    labels: Any
    """"""
    milestone_id: Any
    """"""
    number: Any
    """"""
    parent: Any
    """"""
    parent_id: Any
    """"""
    previous_identifiers: Any
    """"""
    priority: Any
    """"""
    priority_label: Any
    """"""
    priority_sort_order: Any
    """"""
    project: Any
    """"""
    project_id: Any
    """"""
    project_milestone: Any
    """"""
    reaction_data: Any
    """"""
    relation_ids: Any
    """"""
    relations: Any
    """"""
    sla_type: Any
    """"""
    sort_order: Any
    """"""
    source_comment_id: Any
    """"""
    started_at: Any
    """"""
    state: Any
    """"""
    state_id: Any
    """"""
    sub_issue_sort_order: Any
    """"""
    subscriber_ids: Any
    """"""
    subscribers: Any
    """"""
    team: Any
    """"""
    team_id: Any
    """"""
    title: Any
    """"""
    updated_at: Any
    """"""
    url: Any
    """"""


class IssuesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    added_to_cycle_at: str
    """"""
    added_to_project_at: str
    """"""
    added_to_team_at: str
    """"""
    assignee: str
    """"""
    assignee_id: str
    """"""
    attachment_ids: str
    """"""
    attachments: str
    """"""
    branch_name: str
    """"""
    canceled_at: str
    """"""
    completed_at: str
    """"""
    created_at: str
    """"""
    creator: str
    """"""
    creator_id: str
    """"""
    customer_ticket_count: str
    """"""
    cycle: str
    """"""
    cycle_id: str
    """"""
    description: str
    """"""
    description_state: str
    """"""
    due_date: str
    """"""
    estimate: str
    """"""
    id: str
    """"""
    identifier: str
    """"""
    integration_source_type: str
    """"""
    label_ids: str
    """"""
    labels: str
    """"""
    milestone_id: str
    """"""
    number: str
    """"""
    parent: str
    """"""
    parent_id: str
    """"""
    previous_identifiers: str
    """"""
    priority: str
    """"""
    priority_label: str
    """"""
    priority_sort_order: str
    """"""
    project: str
    """"""
    project_id: str
    """"""
    project_milestone: str
    """"""
    reaction_data: str
    """"""
    relation_ids: str
    """"""
    relations: str
    """"""
    sla_type: str
    """"""
    sort_order: str
    """"""
    source_comment_id: str
    """"""
    started_at: str
    """"""
    state: str
    """"""
    state_id: str
    """"""
    sub_issue_sort_order: str
    """"""
    subscriber_ids: str
    """"""
    subscribers: str
    """"""
    team: str
    """"""
    team_id: str
    """"""
    title: str
    """"""
    updated_at: str
    """"""
    url: str
    """"""


class IssuesSortFilter(TypedDict, total=False):
    """Available fields for sorting issues search results."""
    added_to_cycle_at: AirbyteSortOrder
    """"""
    added_to_project_at: AirbyteSortOrder
    """"""
    added_to_team_at: AirbyteSortOrder
    """"""
    assignee: AirbyteSortOrder
    """"""
    assignee_id: AirbyteSortOrder
    """"""
    attachment_ids: AirbyteSortOrder
    """"""
    attachments: AirbyteSortOrder
    """"""
    branch_name: AirbyteSortOrder
    """"""
    canceled_at: AirbyteSortOrder
    """"""
    completed_at: AirbyteSortOrder
    """"""
    created_at: AirbyteSortOrder
    """"""
    creator: AirbyteSortOrder
    """"""
    creator_id: AirbyteSortOrder
    """"""
    customer_ticket_count: AirbyteSortOrder
    """"""
    cycle: AirbyteSortOrder
    """"""
    cycle_id: AirbyteSortOrder
    """"""
    description: AirbyteSortOrder
    """"""
    description_state: AirbyteSortOrder
    """"""
    due_date: AirbyteSortOrder
    """"""
    estimate: AirbyteSortOrder
    """"""
    id: AirbyteSortOrder
    """"""
    identifier: AirbyteSortOrder
    """"""
    integration_source_type: AirbyteSortOrder
    """"""
    label_ids: AirbyteSortOrder
    """"""
    labels: AirbyteSortOrder
    """"""
    milestone_id: AirbyteSortOrder
    """"""
    number: AirbyteSortOrder
    """"""
    parent: AirbyteSortOrder
    """"""
    parent_id: AirbyteSortOrder
    """"""
    previous_identifiers: AirbyteSortOrder
    """"""
    priority: AirbyteSortOrder
    """"""
    priority_label: AirbyteSortOrder
    """"""
    priority_sort_order: AirbyteSortOrder
    """"""
    project: AirbyteSortOrder
    """"""
    project_id: AirbyteSortOrder
    """"""
    project_milestone: AirbyteSortOrder
    """"""
    reaction_data: AirbyteSortOrder
    """"""
    relation_ids: AirbyteSortOrder
    """"""
    relations: AirbyteSortOrder
    """"""
    sla_type: AirbyteSortOrder
    """"""
    sort_order: AirbyteSortOrder
    """"""
    source_comment_id: AirbyteSortOrder
    """"""
    started_at: AirbyteSortOrder
    """"""
    state: AirbyteSortOrder
    """"""
    state_id: AirbyteSortOrder
    """"""
    sub_issue_sort_order: AirbyteSortOrder
    """"""
    subscriber_ids: AirbyteSortOrder
    """"""
    subscribers: AirbyteSortOrder
    """"""
    team: AirbyteSortOrder
    """"""
    team_id: AirbyteSortOrder
    """"""
    title: AirbyteSortOrder
    """"""
    updated_at: AirbyteSortOrder
    """"""
    url: AirbyteSortOrder
    """"""


# Entity-specific condition types for issues
class IssuesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: IssuesSearchFilter


class IssuesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: IssuesSearchFilter


class IssuesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: IssuesSearchFilter


class IssuesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: IssuesSearchFilter


class IssuesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: IssuesSearchFilter


class IssuesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: IssuesSearchFilter


class IssuesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: IssuesStringFilter


class IssuesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: IssuesStringFilter


class IssuesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: IssuesStringFilter


class IssuesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: IssuesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
IssuesInCondition = TypedDict("IssuesInCondition", {"in": IssuesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

IssuesNotCondition = TypedDict("IssuesNotCondition", {"not": "IssuesCondition"}, total=False)
"""Negates the nested condition."""

IssuesAndCondition = TypedDict("IssuesAndCondition", {"and": "list[IssuesCondition]"}, total=False)
"""True if all nested conditions are true."""

IssuesOrCondition = TypedDict("IssuesOrCondition", {"or": "list[IssuesCondition]"}, total=False)
"""True if any nested condition is true."""

IssuesAnyCondition = TypedDict("IssuesAnyCondition", {"any": IssuesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all issues condition types
IssuesCondition = (
    IssuesEqCondition
    | IssuesNeqCondition
    | IssuesGtCondition
    | IssuesGteCondition
    | IssuesLtCondition
    | IssuesLteCondition
    | IssuesInCondition
    | IssuesLikeCondition
    | IssuesFuzzyCondition
    | IssuesKeywordCondition
    | IssuesContainsCondition
    | IssuesNotCondition
    | IssuesAndCondition
    | IssuesOrCondition
    | IssuesAnyCondition
)


class IssuesSearchQuery(TypedDict, total=False):
    """Search query for issues entity."""
    filter: IssuesCondition
    sort: list[IssuesSortFilter]


# ===== PROJECTS SEARCH TYPES =====

class ProjectsSearchFilter(TypedDict, total=False):
    """Available fields for filtering projects search queries."""
    canceled_at: str | None
    """"""
    color: str | None
    """"""
    completed_at: str | None
    """"""
    completed_issue_count_history: list[Any] | None
    """"""
    completed_scope_history: list[Any] | None
    """"""
    content: str | None
    """"""
    content_state: str | None
    """"""
    converted_from_issue: dict[str, Any] | None
    """"""
    converted_from_issue_id: str | None
    """"""
    created_at: str | None
    """"""
    creator: dict[str, Any] | None
    """"""
    creator_id: str | None
    """"""
    description: str | None
    """"""
    health: str | None
    """"""
    health_updated_at: str | None
    """"""
    icon: str | None
    """"""
    id: str | None
    """"""
    in_progress_scope_history: list[Any] | None
    """"""
    issue_count_history: list[Any] | None
    """"""
    lead: dict[str, Any] | None
    """"""
    lead_id: str | None
    """"""
    name: str | None
    """"""
    priority: float | None
    """"""
    priority_sort_order: float | None
    """"""
    progress: float | None
    """"""
    scope: float | None
    """"""
    scope_history: list[Any] | None
    """"""
    slug_id: str | None
    """"""
    sort_order: float | None
    """"""
    start_date: str | None
    """"""
    started_at: str | None
    """"""
    status: dict[str, Any] | None
    """"""
    status_id: str | None
    """"""
    target_date: str | None
    """"""
    team_ids: list[Any] | None
    """"""
    teams: dict[str, Any] | None
    """"""
    update_reminders_day: str | None
    """"""
    update_reminders_hour: float | None
    """"""
    updated_at: str | None
    """"""
    url: str | None
    """"""


class ProjectsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    canceled_at: list[str]
    """"""
    color: list[str]
    """"""
    completed_at: list[str]
    """"""
    completed_issue_count_history: list[list[Any]]
    """"""
    completed_scope_history: list[list[Any]]
    """"""
    content: list[str]
    """"""
    content_state: list[str]
    """"""
    converted_from_issue: list[dict[str, Any]]
    """"""
    converted_from_issue_id: list[str]
    """"""
    created_at: list[str]
    """"""
    creator: list[dict[str, Any]]
    """"""
    creator_id: list[str]
    """"""
    description: list[str]
    """"""
    health: list[str]
    """"""
    health_updated_at: list[str]
    """"""
    icon: list[str]
    """"""
    id: list[str]
    """"""
    in_progress_scope_history: list[list[Any]]
    """"""
    issue_count_history: list[list[Any]]
    """"""
    lead: list[dict[str, Any]]
    """"""
    lead_id: list[str]
    """"""
    name: list[str]
    """"""
    priority: list[float]
    """"""
    priority_sort_order: list[float]
    """"""
    progress: list[float]
    """"""
    scope: list[float]
    """"""
    scope_history: list[list[Any]]
    """"""
    slug_id: list[str]
    """"""
    sort_order: list[float]
    """"""
    start_date: list[str]
    """"""
    started_at: list[str]
    """"""
    status: list[dict[str, Any]]
    """"""
    status_id: list[str]
    """"""
    target_date: list[str]
    """"""
    team_ids: list[list[Any]]
    """"""
    teams: list[dict[str, Any]]
    """"""
    update_reminders_day: list[str]
    """"""
    update_reminders_hour: list[float]
    """"""
    updated_at: list[str]
    """"""
    url: list[str]
    """"""


class ProjectsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    canceled_at: Any
    """"""
    color: Any
    """"""
    completed_at: Any
    """"""
    completed_issue_count_history: Any
    """"""
    completed_scope_history: Any
    """"""
    content: Any
    """"""
    content_state: Any
    """"""
    converted_from_issue: Any
    """"""
    converted_from_issue_id: Any
    """"""
    created_at: Any
    """"""
    creator: Any
    """"""
    creator_id: Any
    """"""
    description: Any
    """"""
    health: Any
    """"""
    health_updated_at: Any
    """"""
    icon: Any
    """"""
    id: Any
    """"""
    in_progress_scope_history: Any
    """"""
    issue_count_history: Any
    """"""
    lead: Any
    """"""
    lead_id: Any
    """"""
    name: Any
    """"""
    priority: Any
    """"""
    priority_sort_order: Any
    """"""
    progress: Any
    """"""
    scope: Any
    """"""
    scope_history: Any
    """"""
    slug_id: Any
    """"""
    sort_order: Any
    """"""
    start_date: Any
    """"""
    started_at: Any
    """"""
    status: Any
    """"""
    status_id: Any
    """"""
    target_date: Any
    """"""
    team_ids: Any
    """"""
    teams: Any
    """"""
    update_reminders_day: Any
    """"""
    update_reminders_hour: Any
    """"""
    updated_at: Any
    """"""
    url: Any
    """"""


class ProjectsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    canceled_at: str
    """"""
    color: str
    """"""
    completed_at: str
    """"""
    completed_issue_count_history: str
    """"""
    completed_scope_history: str
    """"""
    content: str
    """"""
    content_state: str
    """"""
    converted_from_issue: str
    """"""
    converted_from_issue_id: str
    """"""
    created_at: str
    """"""
    creator: str
    """"""
    creator_id: str
    """"""
    description: str
    """"""
    health: str
    """"""
    health_updated_at: str
    """"""
    icon: str
    """"""
    id: str
    """"""
    in_progress_scope_history: str
    """"""
    issue_count_history: str
    """"""
    lead: str
    """"""
    lead_id: str
    """"""
    name: str
    """"""
    priority: str
    """"""
    priority_sort_order: str
    """"""
    progress: str
    """"""
    scope: str
    """"""
    scope_history: str
    """"""
    slug_id: str
    """"""
    sort_order: str
    """"""
    start_date: str
    """"""
    started_at: str
    """"""
    status: str
    """"""
    status_id: str
    """"""
    target_date: str
    """"""
    team_ids: str
    """"""
    teams: str
    """"""
    update_reminders_day: str
    """"""
    update_reminders_hour: str
    """"""
    updated_at: str
    """"""
    url: str
    """"""


class ProjectsSortFilter(TypedDict, total=False):
    """Available fields for sorting projects search results."""
    canceled_at: AirbyteSortOrder
    """"""
    color: AirbyteSortOrder
    """"""
    completed_at: AirbyteSortOrder
    """"""
    completed_issue_count_history: AirbyteSortOrder
    """"""
    completed_scope_history: AirbyteSortOrder
    """"""
    content: AirbyteSortOrder
    """"""
    content_state: AirbyteSortOrder
    """"""
    converted_from_issue: AirbyteSortOrder
    """"""
    converted_from_issue_id: AirbyteSortOrder
    """"""
    created_at: AirbyteSortOrder
    """"""
    creator: AirbyteSortOrder
    """"""
    creator_id: AirbyteSortOrder
    """"""
    description: AirbyteSortOrder
    """"""
    health: AirbyteSortOrder
    """"""
    health_updated_at: AirbyteSortOrder
    """"""
    icon: AirbyteSortOrder
    """"""
    id: AirbyteSortOrder
    """"""
    in_progress_scope_history: AirbyteSortOrder
    """"""
    issue_count_history: AirbyteSortOrder
    """"""
    lead: AirbyteSortOrder
    """"""
    lead_id: AirbyteSortOrder
    """"""
    name: AirbyteSortOrder
    """"""
    priority: AirbyteSortOrder
    """"""
    priority_sort_order: AirbyteSortOrder
    """"""
    progress: AirbyteSortOrder
    """"""
    scope: AirbyteSortOrder
    """"""
    scope_history: AirbyteSortOrder
    """"""
    slug_id: AirbyteSortOrder
    """"""
    sort_order: AirbyteSortOrder
    """"""
    start_date: AirbyteSortOrder
    """"""
    started_at: AirbyteSortOrder
    """"""
    status: AirbyteSortOrder
    """"""
    status_id: AirbyteSortOrder
    """"""
    target_date: AirbyteSortOrder
    """"""
    team_ids: AirbyteSortOrder
    """"""
    teams: AirbyteSortOrder
    """"""
    update_reminders_day: AirbyteSortOrder
    """"""
    update_reminders_hour: AirbyteSortOrder
    """"""
    updated_at: AirbyteSortOrder
    """"""
    url: AirbyteSortOrder
    """"""


# Entity-specific condition types for projects
class ProjectsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ProjectsSearchFilter


class ProjectsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ProjectsSearchFilter


class ProjectsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ProjectsSearchFilter


class ProjectsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ProjectsSearchFilter


class ProjectsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ProjectsSearchFilter


class ProjectsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ProjectsSearchFilter


class ProjectsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ProjectsStringFilter


class ProjectsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ProjectsStringFilter


class ProjectsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ProjectsStringFilter


class ProjectsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ProjectsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ProjectsInCondition = TypedDict("ProjectsInCondition", {"in": ProjectsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ProjectsNotCondition = TypedDict("ProjectsNotCondition", {"not": "ProjectsCondition"}, total=False)
"""Negates the nested condition."""

ProjectsAndCondition = TypedDict("ProjectsAndCondition", {"and": "list[ProjectsCondition]"}, total=False)
"""True if all nested conditions are true."""

ProjectsOrCondition = TypedDict("ProjectsOrCondition", {"or": "list[ProjectsCondition]"}, total=False)
"""True if any nested condition is true."""

ProjectsAnyCondition = TypedDict("ProjectsAnyCondition", {"any": ProjectsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all projects condition types
ProjectsCondition = (
    ProjectsEqCondition
    | ProjectsNeqCondition
    | ProjectsGtCondition
    | ProjectsGteCondition
    | ProjectsLtCondition
    | ProjectsLteCondition
    | ProjectsInCondition
    | ProjectsLikeCondition
    | ProjectsFuzzyCondition
    | ProjectsKeywordCondition
    | ProjectsContainsCondition
    | ProjectsNotCondition
    | ProjectsAndCondition
    | ProjectsOrCondition
    | ProjectsAnyCondition
)


class ProjectsSearchQuery(TypedDict, total=False):
    """Search query for projects entity."""
    filter: ProjectsCondition
    sort: list[ProjectsSortFilter]


# ===== TEAMS SEARCH TYPES =====

class TeamsSearchFilter(TypedDict, total=False):
    """Available fields for filtering teams search queries."""
    active_cycle: dict[str, Any] | None
    """"""
    active_cycle_id: str | None
    """"""
    auto_archive_period: float | None
    """"""
    auto_close_period: float | None
    """"""
    auto_close_state_id: str | None
    """"""
    color: str | None
    """"""
    created_at: str | None
    """"""
    cycle_calender_url: str | None
    """"""
    cycle_cooldown_time: float | None
    """"""
    cycle_duration: float | None
    """"""
    cycle_issue_auto_assign_completed: bool | None
    """"""
    cycle_issue_auto_assign_started: bool | None
    """"""
    cycle_lock_to_active: bool | None
    """"""
    cycle_start_day: float | None
    """"""
    cycles_enabled: bool | None
    """"""
    default_issue_estimate: float | None
    """"""
    default_issue_state: dict[str, Any] | None
    """"""
    default_issue_state_id: str | None
    """"""
    group_issue_history: bool | None
    """"""
    icon: str | None
    """"""
    id: str | None
    """"""
    invite_hash: str | None
    """"""
    issue_count: float | None
    """"""
    issue_estimation_allow_zero: bool | None
    """"""
    issue_estimation_extended: bool | None
    """"""
    issue_estimation_type: str | None
    """"""
    key: str | None
    """"""
    marked_as_duplicate_workflow_state: dict[str, Any] | None
    """"""
    marked_as_duplicate_workflow_state_id: str | None
    """"""
    name: str | None
    """"""
    parent_team_id: str | None
    """"""
    private: bool | None
    """"""
    require_priority_to_leave_triage: bool | None
    """"""
    scim_managed: bool | None
    """"""
    set_issue_sort_order_on_state_change: str | None
    """"""
    timezone: str | None
    """"""
    triage_enabled: bool | None
    """"""
    triage_issue_state_id: str | None
    """"""
    upcoming_cycle_count: float | None
    """"""
    updated_at: str | None
    """"""


class TeamsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active_cycle: list[dict[str, Any]]
    """"""
    active_cycle_id: list[str]
    """"""
    auto_archive_period: list[float]
    """"""
    auto_close_period: list[float]
    """"""
    auto_close_state_id: list[str]
    """"""
    color: list[str]
    """"""
    created_at: list[str]
    """"""
    cycle_calender_url: list[str]
    """"""
    cycle_cooldown_time: list[float]
    """"""
    cycle_duration: list[float]
    """"""
    cycle_issue_auto_assign_completed: list[bool]
    """"""
    cycle_issue_auto_assign_started: list[bool]
    """"""
    cycle_lock_to_active: list[bool]
    """"""
    cycle_start_day: list[float]
    """"""
    cycles_enabled: list[bool]
    """"""
    default_issue_estimate: list[float]
    """"""
    default_issue_state: list[dict[str, Any]]
    """"""
    default_issue_state_id: list[str]
    """"""
    group_issue_history: list[bool]
    """"""
    icon: list[str]
    """"""
    id: list[str]
    """"""
    invite_hash: list[str]
    """"""
    issue_count: list[float]
    """"""
    issue_estimation_allow_zero: list[bool]
    """"""
    issue_estimation_extended: list[bool]
    """"""
    issue_estimation_type: list[str]
    """"""
    key: list[str]
    """"""
    marked_as_duplicate_workflow_state: list[dict[str, Any]]
    """"""
    marked_as_duplicate_workflow_state_id: list[str]
    """"""
    name: list[str]
    """"""
    parent_team_id: list[str]
    """"""
    private: list[bool]
    """"""
    require_priority_to_leave_triage: list[bool]
    """"""
    scim_managed: list[bool]
    """"""
    set_issue_sort_order_on_state_change: list[str]
    """"""
    timezone: list[str]
    """"""
    triage_enabled: list[bool]
    """"""
    triage_issue_state_id: list[str]
    """"""
    upcoming_cycle_count: list[float]
    """"""
    updated_at: list[str]
    """"""


class TeamsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active_cycle: Any
    """"""
    active_cycle_id: Any
    """"""
    auto_archive_period: Any
    """"""
    auto_close_period: Any
    """"""
    auto_close_state_id: Any
    """"""
    color: Any
    """"""
    created_at: Any
    """"""
    cycle_calender_url: Any
    """"""
    cycle_cooldown_time: Any
    """"""
    cycle_duration: Any
    """"""
    cycle_issue_auto_assign_completed: Any
    """"""
    cycle_issue_auto_assign_started: Any
    """"""
    cycle_lock_to_active: Any
    """"""
    cycle_start_day: Any
    """"""
    cycles_enabled: Any
    """"""
    default_issue_estimate: Any
    """"""
    default_issue_state: Any
    """"""
    default_issue_state_id: Any
    """"""
    group_issue_history: Any
    """"""
    icon: Any
    """"""
    id: Any
    """"""
    invite_hash: Any
    """"""
    issue_count: Any
    """"""
    issue_estimation_allow_zero: Any
    """"""
    issue_estimation_extended: Any
    """"""
    issue_estimation_type: Any
    """"""
    key: Any
    """"""
    marked_as_duplicate_workflow_state: Any
    """"""
    marked_as_duplicate_workflow_state_id: Any
    """"""
    name: Any
    """"""
    parent_team_id: Any
    """"""
    private: Any
    """"""
    require_priority_to_leave_triage: Any
    """"""
    scim_managed: Any
    """"""
    set_issue_sort_order_on_state_change: Any
    """"""
    timezone: Any
    """"""
    triage_enabled: Any
    """"""
    triage_issue_state_id: Any
    """"""
    upcoming_cycle_count: Any
    """"""
    updated_at: Any
    """"""


class TeamsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    active_cycle: str
    """"""
    active_cycle_id: str
    """"""
    auto_archive_period: str
    """"""
    auto_close_period: str
    """"""
    auto_close_state_id: str
    """"""
    color: str
    """"""
    created_at: str
    """"""
    cycle_calender_url: str
    """"""
    cycle_cooldown_time: str
    """"""
    cycle_duration: str
    """"""
    cycle_issue_auto_assign_completed: str
    """"""
    cycle_issue_auto_assign_started: str
    """"""
    cycle_lock_to_active: str
    """"""
    cycle_start_day: str
    """"""
    cycles_enabled: str
    """"""
    default_issue_estimate: str
    """"""
    default_issue_state: str
    """"""
    default_issue_state_id: str
    """"""
    group_issue_history: str
    """"""
    icon: str
    """"""
    id: str
    """"""
    invite_hash: str
    """"""
    issue_count: str
    """"""
    issue_estimation_allow_zero: str
    """"""
    issue_estimation_extended: str
    """"""
    issue_estimation_type: str
    """"""
    key: str
    """"""
    marked_as_duplicate_workflow_state: str
    """"""
    marked_as_duplicate_workflow_state_id: str
    """"""
    name: str
    """"""
    parent_team_id: str
    """"""
    private: str
    """"""
    require_priority_to_leave_triage: str
    """"""
    scim_managed: str
    """"""
    set_issue_sort_order_on_state_change: str
    """"""
    timezone: str
    """"""
    triage_enabled: str
    """"""
    triage_issue_state_id: str
    """"""
    upcoming_cycle_count: str
    """"""
    updated_at: str
    """"""


class TeamsSortFilter(TypedDict, total=False):
    """Available fields for sorting teams search results."""
    active_cycle: AirbyteSortOrder
    """"""
    active_cycle_id: AirbyteSortOrder
    """"""
    auto_archive_period: AirbyteSortOrder
    """"""
    auto_close_period: AirbyteSortOrder
    """"""
    auto_close_state_id: AirbyteSortOrder
    """"""
    color: AirbyteSortOrder
    """"""
    created_at: AirbyteSortOrder
    """"""
    cycle_calender_url: AirbyteSortOrder
    """"""
    cycle_cooldown_time: AirbyteSortOrder
    """"""
    cycle_duration: AirbyteSortOrder
    """"""
    cycle_issue_auto_assign_completed: AirbyteSortOrder
    """"""
    cycle_issue_auto_assign_started: AirbyteSortOrder
    """"""
    cycle_lock_to_active: AirbyteSortOrder
    """"""
    cycle_start_day: AirbyteSortOrder
    """"""
    cycles_enabled: AirbyteSortOrder
    """"""
    default_issue_estimate: AirbyteSortOrder
    """"""
    default_issue_state: AirbyteSortOrder
    """"""
    default_issue_state_id: AirbyteSortOrder
    """"""
    group_issue_history: AirbyteSortOrder
    """"""
    icon: AirbyteSortOrder
    """"""
    id: AirbyteSortOrder
    """"""
    invite_hash: AirbyteSortOrder
    """"""
    issue_count: AirbyteSortOrder
    """"""
    issue_estimation_allow_zero: AirbyteSortOrder
    """"""
    issue_estimation_extended: AirbyteSortOrder
    """"""
    issue_estimation_type: AirbyteSortOrder
    """"""
    key: AirbyteSortOrder
    """"""
    marked_as_duplicate_workflow_state: AirbyteSortOrder
    """"""
    marked_as_duplicate_workflow_state_id: AirbyteSortOrder
    """"""
    name: AirbyteSortOrder
    """"""
    parent_team_id: AirbyteSortOrder
    """"""
    private: AirbyteSortOrder
    """"""
    require_priority_to_leave_triage: AirbyteSortOrder
    """"""
    scim_managed: AirbyteSortOrder
    """"""
    set_issue_sort_order_on_state_change: AirbyteSortOrder
    """"""
    timezone: AirbyteSortOrder
    """"""
    triage_enabled: AirbyteSortOrder
    """"""
    triage_issue_state_id: AirbyteSortOrder
    """"""
    upcoming_cycle_count: AirbyteSortOrder
    """"""
    updated_at: AirbyteSortOrder
    """"""


# Entity-specific condition types for teams
class TeamsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TeamsSearchFilter


class TeamsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TeamsSearchFilter


class TeamsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TeamsSearchFilter


class TeamsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TeamsSearchFilter


class TeamsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TeamsSearchFilter


class TeamsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TeamsSearchFilter


class TeamsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TeamsStringFilter


class TeamsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TeamsStringFilter


class TeamsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TeamsStringFilter


class TeamsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TeamsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TeamsInCondition = TypedDict("TeamsInCondition", {"in": TeamsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TeamsNotCondition = TypedDict("TeamsNotCondition", {"not": "TeamsCondition"}, total=False)
"""Negates the nested condition."""

TeamsAndCondition = TypedDict("TeamsAndCondition", {"and": "list[TeamsCondition]"}, total=False)
"""True if all nested conditions are true."""

TeamsOrCondition = TypedDict("TeamsOrCondition", {"or": "list[TeamsCondition]"}, total=False)
"""True if any nested condition is true."""

TeamsAnyCondition = TypedDict("TeamsAnyCondition", {"any": TeamsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all teams condition types
TeamsCondition = (
    TeamsEqCondition
    | TeamsNeqCondition
    | TeamsGtCondition
    | TeamsGteCondition
    | TeamsLtCondition
    | TeamsLteCondition
    | TeamsInCondition
    | TeamsLikeCondition
    | TeamsFuzzyCondition
    | TeamsKeywordCondition
    | TeamsContainsCondition
    | TeamsNotCondition
    | TeamsAndCondition
    | TeamsOrCondition
    | TeamsAnyCondition
)


class TeamsSearchQuery(TypedDict, total=False):
    """Search query for teams entity."""
    filter: TeamsCondition
    sort: list[TeamsSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    active: bool | None
    """"""
    admin: bool | None
    """"""
    avatar_background_color: str | None
    """"""
    avatar_url: str | None
    """"""
    created_at: str | None
    """"""
    created_issue_count: float | None
    """"""
    display_name: str | None
    """"""
    email: str | None
    """"""
    guest: bool | None
    """"""
    id: str | None
    """"""
    initials: str | None
    """"""
    invite_hash: str | None
    """"""
    is_me: bool | None
    """"""
    last_seen: str | None
    """"""
    name: str | None
    """"""
    team_ids: list[Any] | None
    """"""
    teams: dict[str, Any] | None
    """"""
    timezone: str | None
    """"""
    updated_at: str | None
    """"""
    url: str | None
    """"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active: list[bool]
    """"""
    admin: list[bool]
    """"""
    avatar_background_color: list[str]
    """"""
    avatar_url: list[str]
    """"""
    created_at: list[str]
    """"""
    created_issue_count: list[float]
    """"""
    display_name: list[str]
    """"""
    email: list[str]
    """"""
    guest: list[bool]
    """"""
    id: list[str]
    """"""
    initials: list[str]
    """"""
    invite_hash: list[str]
    """"""
    is_me: list[bool]
    """"""
    last_seen: list[str]
    """"""
    name: list[str]
    """"""
    team_ids: list[list[Any]]
    """"""
    teams: list[dict[str, Any]]
    """"""
    timezone: list[str]
    """"""
    updated_at: list[str]
    """"""
    url: list[str]
    """"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active: Any
    """"""
    admin: Any
    """"""
    avatar_background_color: Any
    """"""
    avatar_url: Any
    """"""
    created_at: Any
    """"""
    created_issue_count: Any
    """"""
    display_name: Any
    """"""
    email: Any
    """"""
    guest: Any
    """"""
    id: Any
    """"""
    initials: Any
    """"""
    invite_hash: Any
    """"""
    is_me: Any
    """"""
    last_seen: Any
    """"""
    name: Any
    """"""
    team_ids: Any
    """"""
    teams: Any
    """"""
    timezone: Any
    """"""
    updated_at: Any
    """"""
    url: Any
    """"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    active: str
    """"""
    admin: str
    """"""
    avatar_background_color: str
    """"""
    avatar_url: str
    """"""
    created_at: str
    """"""
    created_issue_count: str
    """"""
    display_name: str
    """"""
    email: str
    """"""
    guest: str
    """"""
    id: str
    """"""
    initials: str
    """"""
    invite_hash: str
    """"""
    is_me: str
    """"""
    last_seen: str
    """"""
    name: str
    """"""
    team_ids: str
    """"""
    teams: str
    """"""
    timezone: str
    """"""
    updated_at: str
    """"""
    url: str
    """"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    active: AirbyteSortOrder
    """"""
    admin: AirbyteSortOrder
    """"""
    avatar_background_color: AirbyteSortOrder
    """"""
    avatar_url: AirbyteSortOrder
    """"""
    created_at: AirbyteSortOrder
    """"""
    created_issue_count: AirbyteSortOrder
    """"""
    display_name: AirbyteSortOrder
    """"""
    email: AirbyteSortOrder
    """"""
    guest: AirbyteSortOrder
    """"""
    id: AirbyteSortOrder
    """"""
    initials: AirbyteSortOrder
    """"""
    invite_hash: AirbyteSortOrder
    """"""
    is_me: AirbyteSortOrder
    """"""
    last_seen: AirbyteSortOrder
    """"""
    name: AirbyteSortOrder
    """"""
    team_ids: AirbyteSortOrder
    """"""
    teams: AirbyteSortOrder
    """"""
    timezone: AirbyteSortOrder
    """"""
    updated_at: AirbyteSortOrder
    """"""
    url: AirbyteSortOrder
    """"""


# Entity-specific condition types for users
class UsersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UsersSearchFilter


class UsersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UsersSearchFilter


class UsersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UsersSearchFilter


class UsersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UsersSearchFilter


class UsersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UsersSearchFilter


class UsersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UsersSearchFilter


class UsersLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: UsersStringFilter


class UsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsersStringFilter


class UsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsersStringFilter


class UsersContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: UsersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UsersInCondition = TypedDict("UsersInCondition", {"in": UsersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UsersNotCondition = TypedDict("UsersNotCondition", {"not": "UsersCondition"}, total=False)
"""Negates the nested condition."""

UsersAndCondition = TypedDict("UsersAndCondition", {"and": "list[UsersCondition]"}, total=False)
"""True if all nested conditions are true."""

UsersOrCondition = TypedDict("UsersOrCondition", {"or": "list[UsersCondition]"}, total=False)
"""True if any nested condition is true."""

UsersAnyCondition = TypedDict("UsersAnyCondition", {"any": UsersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all users condition types
UsersCondition = (
    UsersEqCondition
    | UsersNeqCondition
    | UsersGtCondition
    | UsersGteCondition
    | UsersLtCondition
    | UsersLteCondition
    | UsersInCondition
    | UsersLikeCondition
    | UsersFuzzyCondition
    | UsersKeywordCondition
    | UsersContainsCondition
    | UsersNotCondition
    | UsersAndCondition
    | UsersOrCondition
    | UsersAnyCondition
)


class UsersSearchQuery(TypedDict, total=False):
    """Search query for users entity."""
    filter: UsersCondition
    sort: list[UsersSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
