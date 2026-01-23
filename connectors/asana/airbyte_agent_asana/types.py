"""
Type definitions for asana connector.
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

class WorkspaceTagsListParams(TypedDict):
    """Parameters for workspace_tags.list operation"""
    workspace_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]

class TagsGetParams(TypedDict):
    """Parameters for tags.get operation"""
    tag_gid: str

class ProjectSectionsListParams(TypedDict):
    """Parameters for project_sections.list operation"""
    project_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]

class SectionsGetParams(TypedDict):
    """Parameters for sections.get operation"""
    section_gid: str

class TaskSubtasksListParams(TypedDict):
    """Parameters for task_subtasks.list operation"""
    task_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]

class TaskDependenciesListParams(TypedDict):
    """Parameters for task_dependencies.list operation"""
    task_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]

class TaskDependentsListParams(TypedDict):
    """Parameters for task_dependents.list operation"""
    task_gid: str
    limit: NotRequired[int]
    offset: NotRequired[str]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ATTACHMENTS SEARCH TYPES =====

class AttachmentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering attachments search queries."""
    connected_to_app: bool | None
    """"""
    created_at: str | None
    """"""
    download_url: str | None
    """"""
    gid: str | None
    """"""
    host: str | None
    """"""
    name: str | None
    """"""
    parent: dict[str, Any] | None
    """"""
    permanent_url: str | None
    """"""
    resource_subtype: str | None
    """"""
    resource_type: str | None
    """"""
    size: int | None
    """"""
    view_url: str | None
    """"""


class AttachmentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    connected_to_app: list[bool]
    """"""
    created_at: list[str]
    """"""
    download_url: list[str]
    """"""
    gid: list[str]
    """"""
    host: list[str]
    """"""
    name: list[str]
    """"""
    parent: list[dict[str, Any]]
    """"""
    permanent_url: list[str]
    """"""
    resource_subtype: list[str]
    """"""
    resource_type: list[str]
    """"""
    size: list[int]
    """"""
    view_url: list[str]
    """"""


class AttachmentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    connected_to_app: Any
    """"""
    created_at: Any
    """"""
    download_url: Any
    """"""
    gid: Any
    """"""
    host: Any
    """"""
    name: Any
    """"""
    parent: Any
    """"""
    permanent_url: Any
    """"""
    resource_subtype: Any
    """"""
    resource_type: Any
    """"""
    size: Any
    """"""
    view_url: Any
    """"""


class AttachmentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    connected_to_app: str
    """"""
    created_at: str
    """"""
    download_url: str
    """"""
    gid: str
    """"""
    host: str
    """"""
    name: str
    """"""
    parent: str
    """"""
    permanent_url: str
    """"""
    resource_subtype: str
    """"""
    resource_type: str
    """"""
    size: str
    """"""
    view_url: str
    """"""


class AttachmentsSortFilter(TypedDict, total=False):
    """Available fields for sorting attachments search results."""
    connected_to_app: AirbyteSortOrder
    """"""
    created_at: AirbyteSortOrder
    """"""
    download_url: AirbyteSortOrder
    """"""
    gid: AirbyteSortOrder
    """"""
    host: AirbyteSortOrder
    """"""
    name: AirbyteSortOrder
    """"""
    parent: AirbyteSortOrder
    """"""
    permanent_url: AirbyteSortOrder
    """"""
    resource_subtype: AirbyteSortOrder
    """"""
    resource_type: AirbyteSortOrder
    """"""
    size: AirbyteSortOrder
    """"""
    view_url: AirbyteSortOrder
    """"""


# Entity-specific condition types for attachments
class AttachmentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: AttachmentsSearchFilter


class AttachmentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: AttachmentsSearchFilter


class AttachmentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: AttachmentsSearchFilter


class AttachmentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: AttachmentsSearchFilter


class AttachmentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: AttachmentsSearchFilter


class AttachmentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: AttachmentsSearchFilter


class AttachmentsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: AttachmentsStringFilter


class AttachmentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: AttachmentsStringFilter


class AttachmentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: AttachmentsStringFilter


class AttachmentsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: AttachmentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
AttachmentsInCondition = TypedDict("AttachmentsInCondition", {"in": AttachmentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

AttachmentsNotCondition = TypedDict("AttachmentsNotCondition", {"not": "AttachmentsCondition"}, total=False)
"""Negates the nested condition."""

AttachmentsAndCondition = TypedDict("AttachmentsAndCondition", {"and": "list[AttachmentsCondition]"}, total=False)
"""True if all nested conditions are true."""

AttachmentsOrCondition = TypedDict("AttachmentsOrCondition", {"or": "list[AttachmentsCondition]"}, total=False)
"""True if any nested condition is true."""

AttachmentsAnyCondition = TypedDict("AttachmentsAnyCondition", {"any": AttachmentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all attachments condition types
AttachmentsCondition = (
    AttachmentsEqCondition
    | AttachmentsNeqCondition
    | AttachmentsGtCondition
    | AttachmentsGteCondition
    | AttachmentsLtCondition
    | AttachmentsLteCondition
    | AttachmentsInCondition
    | AttachmentsLikeCondition
    | AttachmentsFuzzyCondition
    | AttachmentsKeywordCondition
    | AttachmentsContainsCondition
    | AttachmentsNotCondition
    | AttachmentsAndCondition
    | AttachmentsOrCondition
    | AttachmentsAnyCondition
)


class AttachmentsSearchQuery(TypedDict, total=False):
    """Search query for attachments entity."""
    filter: AttachmentsCondition
    sort: list[AttachmentsSortFilter]


# ===== PROJECTS SEARCH TYPES =====

class ProjectsSearchFilter(TypedDict, total=False):
    """Available fields for filtering projects search queries."""
    archived: bool | None
    """"""
    color: str | None
    """"""
    created_at: str | None
    """"""
    current_status: dict[str, Any] | None
    """"""
    custom_field_settings: list[Any] | None
    """"""
    custom_fields: list[Any] | None
    """"""
    default_view: str | None
    """"""
    due_date: str | None
    """"""
    due_on: str | None
    """"""
    followers: list[Any] | None
    """"""
    gid: str | None
    """"""
    html_notes: str | None
    """"""
    icon: str | None
    """"""
    is_template: bool | None
    """"""
    members: list[Any] | None
    """"""
    modified_at: str | None
    """"""
    name: str | None
    """"""
    notes: str | None
    """"""
    owner: dict[str, Any] | None
    """"""
    permalink_url: str | None
    """"""
    public: bool | None
    """"""
    resource_type: str | None
    """"""
    start_on: str | None
    """"""
    team: dict[str, Any] | None
    """"""
    workspace: dict[str, Any] | None
    """"""


class ProjectsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """"""
    color: list[str]
    """"""
    created_at: list[str]
    """"""
    current_status: list[dict[str, Any]]
    """"""
    custom_field_settings: list[list[Any]]
    """"""
    custom_fields: list[list[Any]]
    """"""
    default_view: list[str]
    """"""
    due_date: list[str]
    """"""
    due_on: list[str]
    """"""
    followers: list[list[Any]]
    """"""
    gid: list[str]
    """"""
    html_notes: list[str]
    """"""
    icon: list[str]
    """"""
    is_template: list[bool]
    """"""
    members: list[list[Any]]
    """"""
    modified_at: list[str]
    """"""
    name: list[str]
    """"""
    notes: list[str]
    """"""
    owner: list[dict[str, Any]]
    """"""
    permalink_url: list[str]
    """"""
    public: list[bool]
    """"""
    resource_type: list[str]
    """"""
    start_on: list[str]
    """"""
    team: list[dict[str, Any]]
    """"""
    workspace: list[dict[str, Any]]
    """"""


class ProjectsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """"""
    color: Any
    """"""
    created_at: Any
    """"""
    current_status: Any
    """"""
    custom_field_settings: Any
    """"""
    custom_fields: Any
    """"""
    default_view: Any
    """"""
    due_date: Any
    """"""
    due_on: Any
    """"""
    followers: Any
    """"""
    gid: Any
    """"""
    html_notes: Any
    """"""
    icon: Any
    """"""
    is_template: Any
    """"""
    members: Any
    """"""
    modified_at: Any
    """"""
    name: Any
    """"""
    notes: Any
    """"""
    owner: Any
    """"""
    permalink_url: Any
    """"""
    public: Any
    """"""
    resource_type: Any
    """"""
    start_on: Any
    """"""
    team: Any
    """"""
    workspace: Any
    """"""


class ProjectsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """"""
    color: str
    """"""
    created_at: str
    """"""
    current_status: str
    """"""
    custom_field_settings: str
    """"""
    custom_fields: str
    """"""
    default_view: str
    """"""
    due_date: str
    """"""
    due_on: str
    """"""
    followers: str
    """"""
    gid: str
    """"""
    html_notes: str
    """"""
    icon: str
    """"""
    is_template: str
    """"""
    members: str
    """"""
    modified_at: str
    """"""
    name: str
    """"""
    notes: str
    """"""
    owner: str
    """"""
    permalink_url: str
    """"""
    public: str
    """"""
    resource_type: str
    """"""
    start_on: str
    """"""
    team: str
    """"""
    workspace: str
    """"""


class ProjectsSortFilter(TypedDict, total=False):
    """Available fields for sorting projects search results."""
    archived: AirbyteSortOrder
    """"""
    color: AirbyteSortOrder
    """"""
    created_at: AirbyteSortOrder
    """"""
    current_status: AirbyteSortOrder
    """"""
    custom_field_settings: AirbyteSortOrder
    """"""
    custom_fields: AirbyteSortOrder
    """"""
    default_view: AirbyteSortOrder
    """"""
    due_date: AirbyteSortOrder
    """"""
    due_on: AirbyteSortOrder
    """"""
    followers: AirbyteSortOrder
    """"""
    gid: AirbyteSortOrder
    """"""
    html_notes: AirbyteSortOrder
    """"""
    icon: AirbyteSortOrder
    """"""
    is_template: AirbyteSortOrder
    """"""
    members: AirbyteSortOrder
    """"""
    modified_at: AirbyteSortOrder
    """"""
    name: AirbyteSortOrder
    """"""
    notes: AirbyteSortOrder
    """"""
    owner: AirbyteSortOrder
    """"""
    permalink_url: AirbyteSortOrder
    """"""
    public: AirbyteSortOrder
    """"""
    resource_type: AirbyteSortOrder
    """"""
    start_on: AirbyteSortOrder
    """"""
    team: AirbyteSortOrder
    """"""
    workspace: AirbyteSortOrder
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


# ===== SECTIONS SEARCH TYPES =====

class SectionsSearchFilter(TypedDict, total=False):
    """Available fields for filtering sections search queries."""
    created_at: str | None
    """"""
    gid: str | None
    """"""
    name: str | None
    """"""
    project: dict[str, Any] | None
    """"""
    resource_type: str | None
    """"""


class SectionsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """"""
    gid: list[str]
    """"""
    name: list[str]
    """"""
    project: list[dict[str, Any]]
    """"""
    resource_type: list[str]
    """"""


class SectionsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """"""
    gid: Any
    """"""
    name: Any
    """"""
    project: Any
    """"""
    resource_type: Any
    """"""


class SectionsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_at: str
    """"""
    gid: str
    """"""
    name: str
    """"""
    project: str
    """"""
    resource_type: str
    """"""


class SectionsSortFilter(TypedDict, total=False):
    """Available fields for sorting sections search results."""
    created_at: AirbyteSortOrder
    """"""
    gid: AirbyteSortOrder
    """"""
    name: AirbyteSortOrder
    """"""
    project: AirbyteSortOrder
    """"""
    resource_type: AirbyteSortOrder
    """"""


# Entity-specific condition types for sections
class SectionsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SectionsSearchFilter


class SectionsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SectionsSearchFilter


class SectionsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SectionsSearchFilter


class SectionsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SectionsSearchFilter


class SectionsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SectionsSearchFilter


class SectionsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SectionsSearchFilter


class SectionsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: SectionsStringFilter


class SectionsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SectionsStringFilter


class SectionsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SectionsStringFilter


class SectionsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: SectionsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SectionsInCondition = TypedDict("SectionsInCondition", {"in": SectionsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SectionsNotCondition = TypedDict("SectionsNotCondition", {"not": "SectionsCondition"}, total=False)
"""Negates the nested condition."""

SectionsAndCondition = TypedDict("SectionsAndCondition", {"and": "list[SectionsCondition]"}, total=False)
"""True if all nested conditions are true."""

SectionsOrCondition = TypedDict("SectionsOrCondition", {"or": "list[SectionsCondition]"}, total=False)
"""True if any nested condition is true."""

SectionsAnyCondition = TypedDict("SectionsAnyCondition", {"any": SectionsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sections condition types
SectionsCondition = (
    SectionsEqCondition
    | SectionsNeqCondition
    | SectionsGtCondition
    | SectionsGteCondition
    | SectionsLtCondition
    | SectionsLteCondition
    | SectionsInCondition
    | SectionsLikeCondition
    | SectionsFuzzyCondition
    | SectionsKeywordCondition
    | SectionsContainsCondition
    | SectionsNotCondition
    | SectionsAndCondition
    | SectionsOrCondition
    | SectionsAnyCondition
)


class SectionsSearchQuery(TypedDict, total=False):
    """Search query for sections entity."""
    filter: SectionsCondition
    sort: list[SectionsSortFilter]


# ===== TAGS SEARCH TYPES =====

class TagsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tags search queries."""
    color: str | None
    """"""
    followers: list[Any] | None
    """"""
    gid: str | None
    """"""
    name: str | None
    """"""
    permalink_url: str | None
    """"""
    resource_type: str | None
    """"""
    workspace: dict[str, Any] | None
    """"""


class TagsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    color: list[str]
    """"""
    followers: list[list[Any]]
    """"""
    gid: list[str]
    """"""
    name: list[str]
    """"""
    permalink_url: list[str]
    """"""
    resource_type: list[str]
    """"""
    workspace: list[dict[str, Any]]
    """"""


class TagsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    color: Any
    """"""
    followers: Any
    """"""
    gid: Any
    """"""
    name: Any
    """"""
    permalink_url: Any
    """"""
    resource_type: Any
    """"""
    workspace: Any
    """"""


class TagsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    color: str
    """"""
    followers: str
    """"""
    gid: str
    """"""
    name: str
    """"""
    permalink_url: str
    """"""
    resource_type: str
    """"""
    workspace: str
    """"""


class TagsSortFilter(TypedDict, total=False):
    """Available fields for sorting tags search results."""
    color: AirbyteSortOrder
    """"""
    followers: AirbyteSortOrder
    """"""
    gid: AirbyteSortOrder
    """"""
    name: AirbyteSortOrder
    """"""
    permalink_url: AirbyteSortOrder
    """"""
    resource_type: AirbyteSortOrder
    """"""
    workspace: AirbyteSortOrder
    """"""


# Entity-specific condition types for tags
class TagsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TagsSearchFilter


class TagsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TagsSearchFilter


class TagsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TagsSearchFilter


class TagsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TagsSearchFilter


class TagsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TagsSearchFilter


class TagsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TagsSearchFilter


class TagsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TagsStringFilter


class TagsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TagsStringFilter


class TagsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TagsStringFilter


class TagsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TagsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TagsInCondition = TypedDict("TagsInCondition", {"in": TagsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TagsNotCondition = TypedDict("TagsNotCondition", {"not": "TagsCondition"}, total=False)
"""Negates the nested condition."""

TagsAndCondition = TypedDict("TagsAndCondition", {"and": "list[TagsCondition]"}, total=False)
"""True if all nested conditions are true."""

TagsOrCondition = TypedDict("TagsOrCondition", {"or": "list[TagsCondition]"}, total=False)
"""True if any nested condition is true."""

TagsAnyCondition = TypedDict("TagsAnyCondition", {"any": TagsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tags condition types
TagsCondition = (
    TagsEqCondition
    | TagsNeqCondition
    | TagsGtCondition
    | TagsGteCondition
    | TagsLtCondition
    | TagsLteCondition
    | TagsInCondition
    | TagsLikeCondition
    | TagsFuzzyCondition
    | TagsKeywordCondition
    | TagsContainsCondition
    | TagsNotCondition
    | TagsAndCondition
    | TagsOrCondition
    | TagsAnyCondition
)


class TagsSearchQuery(TypedDict, total=False):
    """Search query for tags entity."""
    filter: TagsCondition
    sort: list[TagsSortFilter]


# ===== TASKS SEARCH TYPES =====

class TasksSearchFilter(TypedDict, total=False):
    """Available fields for filtering tasks search queries."""
    actual_time_minutes: int | None
    """The actual time spent on the task in minutes"""
    approval_status: str | None
    """"""
    assignee: dict[str, Any] | None
    """"""
    completed: bool | None
    """"""
    completed_at: str | None
    """"""
    completed_by: dict[str, Any] | None
    """"""
    created_at: str | None
    """"""
    custom_fields: list[Any] | None
    """"""
    dependencies: list[Any] | None
    """"""
    dependents: list[Any] | None
    """"""
    due_at: str | None
    """"""
    due_on: str | None
    """"""
    external: dict[str, Any] | None
    """"""
    followers: list[Any] | None
    """"""
    gid: str | None
    """"""
    hearted: bool | None
    """"""
    hearts: list[Any] | None
    """"""
    html_notes: str | None
    """"""
    is_rendered_as_separator: bool | None
    """"""
    liked: bool | None
    """"""
    likes: list[Any] | None
    """"""
    memberships: list[Any] | None
    """"""
    modified_at: str | None
    """"""
    name: str | None
    """"""
    notes: str | None
    """"""
    num_hearts: int | None
    """"""
    num_likes: int | None
    """"""
    num_subtasks: int | None
    """"""
    parent: dict[str, Any] | None
    """"""
    permalink_url: str | None
    """"""
    projects: list[Any] | None
    """"""
    resource_subtype: str | None
    """"""
    resource_type: str | None
    """"""
    start_on: str | None
    """"""
    tags: list[Any] | None
    """"""
    workspace: dict[str, Any] | None
    """"""


class TasksInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    actual_time_minutes: list[int]
    """The actual time spent on the task in minutes"""
    approval_status: list[str]
    """"""
    assignee: list[dict[str, Any]]
    """"""
    completed: list[bool]
    """"""
    completed_at: list[str]
    """"""
    completed_by: list[dict[str, Any]]
    """"""
    created_at: list[str]
    """"""
    custom_fields: list[list[Any]]
    """"""
    dependencies: list[list[Any]]
    """"""
    dependents: list[list[Any]]
    """"""
    due_at: list[str]
    """"""
    due_on: list[str]
    """"""
    external: list[dict[str, Any]]
    """"""
    followers: list[list[Any]]
    """"""
    gid: list[str]
    """"""
    hearted: list[bool]
    """"""
    hearts: list[list[Any]]
    """"""
    html_notes: list[str]
    """"""
    is_rendered_as_separator: list[bool]
    """"""
    liked: list[bool]
    """"""
    likes: list[list[Any]]
    """"""
    memberships: list[list[Any]]
    """"""
    modified_at: list[str]
    """"""
    name: list[str]
    """"""
    notes: list[str]
    """"""
    num_hearts: list[int]
    """"""
    num_likes: list[int]
    """"""
    num_subtasks: list[int]
    """"""
    parent: list[dict[str, Any]]
    """"""
    permalink_url: list[str]
    """"""
    projects: list[list[Any]]
    """"""
    resource_subtype: list[str]
    """"""
    resource_type: list[str]
    """"""
    start_on: list[str]
    """"""
    tags: list[list[Any]]
    """"""
    workspace: list[dict[str, Any]]
    """"""


class TasksAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    actual_time_minutes: Any
    """The actual time spent on the task in minutes"""
    approval_status: Any
    """"""
    assignee: Any
    """"""
    completed: Any
    """"""
    completed_at: Any
    """"""
    completed_by: Any
    """"""
    created_at: Any
    """"""
    custom_fields: Any
    """"""
    dependencies: Any
    """"""
    dependents: Any
    """"""
    due_at: Any
    """"""
    due_on: Any
    """"""
    external: Any
    """"""
    followers: Any
    """"""
    gid: Any
    """"""
    hearted: Any
    """"""
    hearts: Any
    """"""
    html_notes: Any
    """"""
    is_rendered_as_separator: Any
    """"""
    liked: Any
    """"""
    likes: Any
    """"""
    memberships: Any
    """"""
    modified_at: Any
    """"""
    name: Any
    """"""
    notes: Any
    """"""
    num_hearts: Any
    """"""
    num_likes: Any
    """"""
    num_subtasks: Any
    """"""
    parent: Any
    """"""
    permalink_url: Any
    """"""
    projects: Any
    """"""
    resource_subtype: Any
    """"""
    resource_type: Any
    """"""
    start_on: Any
    """"""
    tags: Any
    """"""
    workspace: Any
    """"""


class TasksStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    actual_time_minutes: str
    """The actual time spent on the task in minutes"""
    approval_status: str
    """"""
    assignee: str
    """"""
    completed: str
    """"""
    completed_at: str
    """"""
    completed_by: str
    """"""
    created_at: str
    """"""
    custom_fields: str
    """"""
    dependencies: str
    """"""
    dependents: str
    """"""
    due_at: str
    """"""
    due_on: str
    """"""
    external: str
    """"""
    followers: str
    """"""
    gid: str
    """"""
    hearted: str
    """"""
    hearts: str
    """"""
    html_notes: str
    """"""
    is_rendered_as_separator: str
    """"""
    liked: str
    """"""
    likes: str
    """"""
    memberships: str
    """"""
    modified_at: str
    """"""
    name: str
    """"""
    notes: str
    """"""
    num_hearts: str
    """"""
    num_likes: str
    """"""
    num_subtasks: str
    """"""
    parent: str
    """"""
    permalink_url: str
    """"""
    projects: str
    """"""
    resource_subtype: str
    """"""
    resource_type: str
    """"""
    start_on: str
    """"""
    tags: str
    """"""
    workspace: str
    """"""


class TasksSortFilter(TypedDict, total=False):
    """Available fields for sorting tasks search results."""
    actual_time_minutes: AirbyteSortOrder
    """The actual time spent on the task in minutes"""
    approval_status: AirbyteSortOrder
    """"""
    assignee: AirbyteSortOrder
    """"""
    completed: AirbyteSortOrder
    """"""
    completed_at: AirbyteSortOrder
    """"""
    completed_by: AirbyteSortOrder
    """"""
    created_at: AirbyteSortOrder
    """"""
    custom_fields: AirbyteSortOrder
    """"""
    dependencies: AirbyteSortOrder
    """"""
    dependents: AirbyteSortOrder
    """"""
    due_at: AirbyteSortOrder
    """"""
    due_on: AirbyteSortOrder
    """"""
    external: AirbyteSortOrder
    """"""
    followers: AirbyteSortOrder
    """"""
    gid: AirbyteSortOrder
    """"""
    hearted: AirbyteSortOrder
    """"""
    hearts: AirbyteSortOrder
    """"""
    html_notes: AirbyteSortOrder
    """"""
    is_rendered_as_separator: AirbyteSortOrder
    """"""
    liked: AirbyteSortOrder
    """"""
    likes: AirbyteSortOrder
    """"""
    memberships: AirbyteSortOrder
    """"""
    modified_at: AirbyteSortOrder
    """"""
    name: AirbyteSortOrder
    """"""
    notes: AirbyteSortOrder
    """"""
    num_hearts: AirbyteSortOrder
    """"""
    num_likes: AirbyteSortOrder
    """"""
    num_subtasks: AirbyteSortOrder
    """"""
    parent: AirbyteSortOrder
    """"""
    permalink_url: AirbyteSortOrder
    """"""
    projects: AirbyteSortOrder
    """"""
    resource_subtype: AirbyteSortOrder
    """"""
    resource_type: AirbyteSortOrder
    """"""
    start_on: AirbyteSortOrder
    """"""
    tags: AirbyteSortOrder
    """"""
    workspace: AirbyteSortOrder
    """"""


# Entity-specific condition types for tasks
class TasksEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TasksSearchFilter


class TasksNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TasksSearchFilter


class TasksGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TasksSearchFilter


class TasksGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TasksSearchFilter


class TasksLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TasksSearchFilter


class TasksLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TasksSearchFilter


class TasksLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TasksStringFilter


class TasksFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TasksStringFilter


class TasksKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TasksStringFilter


class TasksContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TasksAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TasksInCondition = TypedDict("TasksInCondition", {"in": TasksInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TasksNotCondition = TypedDict("TasksNotCondition", {"not": "TasksCondition"}, total=False)
"""Negates the nested condition."""

TasksAndCondition = TypedDict("TasksAndCondition", {"and": "list[TasksCondition]"}, total=False)
"""True if all nested conditions are true."""

TasksOrCondition = TypedDict("TasksOrCondition", {"or": "list[TasksCondition]"}, total=False)
"""True if any nested condition is true."""

TasksAnyCondition = TypedDict("TasksAnyCondition", {"any": TasksAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tasks condition types
TasksCondition = (
    TasksEqCondition
    | TasksNeqCondition
    | TasksGtCondition
    | TasksGteCondition
    | TasksLtCondition
    | TasksLteCondition
    | TasksInCondition
    | TasksLikeCondition
    | TasksFuzzyCondition
    | TasksKeywordCondition
    | TasksContainsCondition
    | TasksNotCondition
    | TasksAndCondition
    | TasksOrCondition
    | TasksAnyCondition
)


class TasksSearchQuery(TypedDict, total=False):
    """Search query for tasks entity."""
    filter: TasksCondition
    sort: list[TasksSortFilter]


# ===== TEAMS SEARCH TYPES =====

class TeamsSearchFilter(TypedDict, total=False):
    """Available fields for filtering teams search queries."""
    description: str | None
    """"""
    gid: str | None
    """"""
    html_description: str | None
    """"""
    name: str | None
    """"""
    organization: dict[str, Any] | None
    """"""
    permalink_url: str | None
    """"""
    resource_type: str | None
    """"""


class TeamsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    description: list[str]
    """"""
    gid: list[str]
    """"""
    html_description: list[str]
    """"""
    name: list[str]
    """"""
    organization: list[dict[str, Any]]
    """"""
    permalink_url: list[str]
    """"""
    resource_type: list[str]
    """"""


class TeamsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    description: Any
    """"""
    gid: Any
    """"""
    html_description: Any
    """"""
    name: Any
    """"""
    organization: Any
    """"""
    permalink_url: Any
    """"""
    resource_type: Any
    """"""


class TeamsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    description: str
    """"""
    gid: str
    """"""
    html_description: str
    """"""
    name: str
    """"""
    organization: str
    """"""
    permalink_url: str
    """"""
    resource_type: str
    """"""


class TeamsSortFilter(TypedDict, total=False):
    """Available fields for sorting teams search results."""
    description: AirbyteSortOrder
    """"""
    gid: AirbyteSortOrder
    """"""
    html_description: AirbyteSortOrder
    """"""
    name: AirbyteSortOrder
    """"""
    organization: AirbyteSortOrder
    """"""
    permalink_url: AirbyteSortOrder
    """"""
    resource_type: AirbyteSortOrder
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
    email: str | None
    """"""
    gid: str | None
    """"""
    name: str | None
    """"""
    photo: dict[str, Any] | None
    """"""
    resource_type: str | None
    """"""
    workspaces: list[Any] | None
    """"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    email: list[str]
    """"""
    gid: list[str]
    """"""
    name: list[str]
    """"""
    photo: list[dict[str, Any]]
    """"""
    resource_type: list[str]
    """"""
    workspaces: list[list[Any]]
    """"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    email: Any
    """"""
    gid: Any
    """"""
    name: Any
    """"""
    photo: Any
    """"""
    resource_type: Any
    """"""
    workspaces: Any
    """"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    email: str
    """"""
    gid: str
    """"""
    name: str
    """"""
    photo: str
    """"""
    resource_type: str
    """"""
    workspaces: str
    """"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    email: AirbyteSortOrder
    """"""
    gid: AirbyteSortOrder
    """"""
    name: AirbyteSortOrder
    """"""
    photo: AirbyteSortOrder
    """"""
    resource_type: AirbyteSortOrder
    """"""
    workspaces: AirbyteSortOrder
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


# ===== WORKSPACES SEARCH TYPES =====

class WorkspacesSearchFilter(TypedDict, total=False):
    """Available fields for filtering workspaces search queries."""
    email_domains: list[Any] | None
    """"""
    gid: str | None
    """"""
    is_organization: bool | None
    """"""
    name: str | None
    """"""
    resource_type: str | None
    """"""


class WorkspacesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    email_domains: list[list[Any]]
    """"""
    gid: list[str]
    """"""
    is_organization: list[bool]
    """"""
    name: list[str]
    """"""
    resource_type: list[str]
    """"""


class WorkspacesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    email_domains: Any
    """"""
    gid: Any
    """"""
    is_organization: Any
    """"""
    name: Any
    """"""
    resource_type: Any
    """"""


class WorkspacesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    email_domains: str
    """"""
    gid: str
    """"""
    is_organization: str
    """"""
    name: str
    """"""
    resource_type: str
    """"""


class WorkspacesSortFilter(TypedDict, total=False):
    """Available fields for sorting workspaces search results."""
    email_domains: AirbyteSortOrder
    """"""
    gid: AirbyteSortOrder
    """"""
    is_organization: AirbyteSortOrder
    """"""
    name: AirbyteSortOrder
    """"""
    resource_type: AirbyteSortOrder
    """"""


# Entity-specific condition types for workspaces
class WorkspacesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: WorkspacesSearchFilter


class WorkspacesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: WorkspacesSearchFilter


class WorkspacesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: WorkspacesSearchFilter


class WorkspacesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: WorkspacesSearchFilter


class WorkspacesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: WorkspacesSearchFilter


class WorkspacesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: WorkspacesSearchFilter


class WorkspacesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: WorkspacesStringFilter


class WorkspacesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: WorkspacesStringFilter


class WorkspacesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: WorkspacesStringFilter


class WorkspacesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: WorkspacesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
WorkspacesInCondition = TypedDict("WorkspacesInCondition", {"in": WorkspacesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

WorkspacesNotCondition = TypedDict("WorkspacesNotCondition", {"not": "WorkspacesCondition"}, total=False)
"""Negates the nested condition."""

WorkspacesAndCondition = TypedDict("WorkspacesAndCondition", {"and": "list[WorkspacesCondition]"}, total=False)
"""True if all nested conditions are true."""

WorkspacesOrCondition = TypedDict("WorkspacesOrCondition", {"or": "list[WorkspacesCondition]"}, total=False)
"""True if any nested condition is true."""

WorkspacesAnyCondition = TypedDict("WorkspacesAnyCondition", {"any": WorkspacesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all workspaces condition types
WorkspacesCondition = (
    WorkspacesEqCondition
    | WorkspacesNeqCondition
    | WorkspacesGtCondition
    | WorkspacesGteCondition
    | WorkspacesLtCondition
    | WorkspacesLteCondition
    | WorkspacesInCondition
    | WorkspacesLikeCondition
    | WorkspacesFuzzyCondition
    | WorkspacesKeywordCondition
    | WorkspacesContainsCondition
    | WorkspacesNotCondition
    | WorkspacesAndCondition
    | WorkspacesOrCondition
    | WorkspacesAnyCondition
)


class WorkspacesSearchQuery(TypedDict, total=False):
    """Search query for workspaces entity."""
    filter: WorkspacesCondition
    sort: list[WorkspacesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
