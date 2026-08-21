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

from typing import Any, Literal


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

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== USER SEARCH TYPES =====

class UserSearchFilter(TypedDict, total=False):
    """Available fields for filtering user search queries."""
    id: int | None
    """Unique identifier for the user"""
    username: str | None
    """Display name of the user"""


class UserInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique identifier for the user"""
    username: list[str]
    """Display name of the user"""


class UserAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the user"""
    username: Any
    """Display name of the user"""


class UserStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the user"""
    username: str
    """Display name of the user"""


class UserSortFilter(TypedDict, total=False):
    """Available fields for sorting user search results."""
    id: AirbyteSortOrder
    """Unique identifier for the user"""
    username: AirbyteSortOrder
    """Display name of the user"""


# Entity-specific condition types for user
class UserEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UserSearchFilter


class UserNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UserSearchFilter


class UserGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UserSearchFilter


class UserGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UserSearchFilter


class UserLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UserSearchFilter


class UserLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UserSearchFilter


class UserStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: UserStringFilter


class UserEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: UserStringFilter


class UserFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UserStringFilter


class UserKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UserStringFilter


class UserContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: UserAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UserInCondition = TypedDict("UserInCondition", {"in": UserInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UserNotCondition = TypedDict("UserNotCondition", {"not": "UserCondition"}, total=False)
"""Negates the nested condition."""

UserAndCondition = TypedDict("UserAndCondition", {"and": "list[UserCondition]"}, total=False)
"""True if all nested conditions are true."""

UserOrCondition = TypedDict("UserOrCondition", {"or": "list[UserCondition]"}, total=False)
"""True if any nested condition is true."""

UserAnyCondition = TypedDict("UserAnyCondition", {"any": UserAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all user condition types
UserCondition = (
    UserEqCondition
    | UserNeqCondition
    | UserGtCondition
    | UserGteCondition
    | UserLtCondition
    | UserLteCondition
    | UserInCondition
    | UserStartswithCondition
    | UserEndswithCondition
    | UserFuzzyCondition
    | UserKeywordCondition
    | UserContainsCondition
    | UserNotCondition
    | UserAndCondition
    | UserOrCondition
    | UserAnyCondition
)


class UserSearchQuery(TypedDict, total=False):
    """Search query for user entity."""
    filter: UserCondition
    sort: list[UserSortFilter]


# ===== TEAMS SEARCH TYPES =====

class TeamsSearchFilter(TypedDict, total=False):
    """Available fields for filtering teams search queries."""
    id: str | None
    """Unique identifier for the team (workspace)"""
    name: str | None
    """Name of the team"""


class TeamsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the team (workspace)"""
    name: list[str]
    """Name of the team"""


class TeamsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the team (workspace)"""
    name: Any
    """Name of the team"""


class TeamsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the team (workspace)"""
    name: str
    """Name of the team"""


class TeamsSortFilter(TypedDict, total=False):
    """Available fields for sorting teams search results."""
    id: AirbyteSortOrder
    """Unique identifier for the team (workspace)"""
    name: AirbyteSortOrder
    """Name of the team"""


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


class TeamsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: TeamsStringFilter


class TeamsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: TeamsStringFilter


class TeamsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TeamsStringFilter


class TeamsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TeamsStringFilter


class TeamsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | TeamsStartswithCondition
    | TeamsEndswithCondition
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


# ===== SPACES SEARCH TYPES =====

class SpacesSearchFilter(TypedDict, total=False):
    """Available fields for filtering spaces search queries."""
    id: str | None
    """Unique identifier for the space"""
    name: str | None
    """Name of the space"""
    private: bool | None
    """Whether the space is private"""


class SpacesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the space"""
    name: list[str]
    """Name of the space"""
    private: list[bool]
    """Whether the space is private"""


class SpacesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the space"""
    name: Any
    """Name of the space"""
    private: Any
    """Whether the space is private"""


class SpacesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the space"""
    name: str
    """Name of the space"""
    private: str
    """Whether the space is private"""


class SpacesSortFilter(TypedDict, total=False):
    """Available fields for sorting spaces search results."""
    id: AirbyteSortOrder
    """Unique identifier for the space"""
    name: AirbyteSortOrder
    """Name of the space"""
    private: AirbyteSortOrder
    """Whether the space is private"""


# Entity-specific condition types for spaces
class SpacesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SpacesSearchFilter


class SpacesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SpacesSearchFilter


class SpacesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SpacesSearchFilter


class SpacesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SpacesSearchFilter


class SpacesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SpacesSearchFilter


class SpacesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SpacesSearchFilter


class SpacesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: SpacesStringFilter


class SpacesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: SpacesStringFilter


class SpacesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SpacesStringFilter


class SpacesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SpacesStringFilter


class SpacesContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: SpacesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SpacesInCondition = TypedDict("SpacesInCondition", {"in": SpacesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SpacesNotCondition = TypedDict("SpacesNotCondition", {"not": "SpacesCondition"}, total=False)
"""Negates the nested condition."""

SpacesAndCondition = TypedDict("SpacesAndCondition", {"and": "list[SpacesCondition]"}, total=False)
"""True if all nested conditions are true."""

SpacesOrCondition = TypedDict("SpacesOrCondition", {"or": "list[SpacesCondition]"}, total=False)
"""True if any nested condition is true."""

SpacesAnyCondition = TypedDict("SpacesAnyCondition", {"any": SpacesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all spaces condition types
SpacesCondition = (
    SpacesEqCondition
    | SpacesNeqCondition
    | SpacesGtCondition
    | SpacesGteCondition
    | SpacesLtCondition
    | SpacesLteCondition
    | SpacesInCondition
    | SpacesStartswithCondition
    | SpacesEndswithCondition
    | SpacesFuzzyCondition
    | SpacesKeywordCondition
    | SpacesContainsCondition
    | SpacesNotCondition
    | SpacesAndCondition
    | SpacesOrCondition
    | SpacesAnyCondition
)


class SpacesSearchQuery(TypedDict, total=False):
    """Search query for spaces entity."""
    filter: SpacesCondition
    sort: list[SpacesSortFilter]


# ===== FOLDERS SEARCH TYPES =====

class FoldersSearchFilter(TypedDict, total=False):
    """Available fields for filtering folders search queries."""
    id: str | None
    """Unique identifier for the folder"""
    name: str | None
    """Name of the folder"""
    hidden: bool | None
    """Whether the folder is hidden from the sidebar"""
    task_count: str | None
    """Number of tasks contained in the folder"""


class FoldersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the folder"""
    name: list[str]
    """Name of the folder"""
    hidden: list[bool]
    """Whether the folder is hidden from the sidebar"""
    task_count: list[str]
    """Number of tasks contained in the folder"""


class FoldersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the folder"""
    name: Any
    """Name of the folder"""
    hidden: Any
    """Whether the folder is hidden from the sidebar"""
    task_count: Any
    """Number of tasks contained in the folder"""


class FoldersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the folder"""
    name: str
    """Name of the folder"""
    hidden: str
    """Whether the folder is hidden from the sidebar"""
    task_count: str
    """Number of tasks contained in the folder"""


class FoldersSortFilter(TypedDict, total=False):
    """Available fields for sorting folders search results."""
    id: AirbyteSortOrder
    """Unique identifier for the folder"""
    name: AirbyteSortOrder
    """Name of the folder"""
    hidden: AirbyteSortOrder
    """Whether the folder is hidden from the sidebar"""
    task_count: AirbyteSortOrder
    """Number of tasks contained in the folder"""


# Entity-specific condition types for folders
class FoldersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: FoldersSearchFilter


class FoldersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: FoldersSearchFilter


class FoldersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: FoldersSearchFilter


class FoldersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: FoldersSearchFilter


class FoldersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: FoldersSearchFilter


class FoldersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: FoldersSearchFilter


class FoldersStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: FoldersStringFilter


class FoldersEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: FoldersStringFilter


class FoldersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: FoldersStringFilter


class FoldersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: FoldersStringFilter


class FoldersContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: FoldersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
FoldersInCondition = TypedDict("FoldersInCondition", {"in": FoldersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

FoldersNotCondition = TypedDict("FoldersNotCondition", {"not": "FoldersCondition"}, total=False)
"""Negates the nested condition."""

FoldersAndCondition = TypedDict("FoldersAndCondition", {"and": "list[FoldersCondition]"}, total=False)
"""True if all nested conditions are true."""

FoldersOrCondition = TypedDict("FoldersOrCondition", {"or": "list[FoldersCondition]"}, total=False)
"""True if any nested condition is true."""

FoldersAnyCondition = TypedDict("FoldersAnyCondition", {"any": FoldersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all folders condition types
FoldersCondition = (
    FoldersEqCondition
    | FoldersNeqCondition
    | FoldersGtCondition
    | FoldersGteCondition
    | FoldersLtCondition
    | FoldersLteCondition
    | FoldersInCondition
    | FoldersStartswithCondition
    | FoldersEndswithCondition
    | FoldersFuzzyCondition
    | FoldersKeywordCondition
    | FoldersContainsCondition
    | FoldersNotCondition
    | FoldersAndCondition
    | FoldersOrCondition
    | FoldersAnyCondition
)


class FoldersSearchQuery(TypedDict, total=False):
    """Search query for folders entity."""
    filter: FoldersCondition
    sort: list[FoldersSortFilter]


# ===== LISTS SEARCH TYPES =====

class ListsSearchFilter(TypedDict, total=False):
    """Available fields for filtering lists search queries."""
    id: str | None
    """Unique identifier for the list"""
    name: str | None
    """Name of the list"""
    archived: bool | None
    """Whether the list has been archived"""
    due_date: str | None
    """Due date for the list, in ClickUp timestamp format"""
    start_date: str | None
    """Start date for the list, in ClickUp timestamp format"""
    priority: str | None
    """Priority assigned to the list"""
    task_count: int | None
    """Number of tasks contained in the list"""


class ListsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the list"""
    name: list[str]
    """Name of the list"""
    archived: list[bool]
    """Whether the list has been archived"""
    due_date: list[str]
    """Due date for the list, in ClickUp timestamp format"""
    start_date: list[str]
    """Start date for the list, in ClickUp timestamp format"""
    priority: list[str]
    """Priority assigned to the list"""
    task_count: list[int]
    """Number of tasks contained in the list"""


class ListsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the list"""
    name: Any
    """Name of the list"""
    archived: Any
    """Whether the list has been archived"""
    due_date: Any
    """Due date for the list, in ClickUp timestamp format"""
    start_date: Any
    """Start date for the list, in ClickUp timestamp format"""
    priority: Any
    """Priority assigned to the list"""
    task_count: Any
    """Number of tasks contained in the list"""


class ListsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the list"""
    name: str
    """Name of the list"""
    archived: str
    """Whether the list has been archived"""
    due_date: str
    """Due date for the list, in ClickUp timestamp format"""
    start_date: str
    """Start date for the list, in ClickUp timestamp format"""
    priority: str
    """Priority assigned to the list"""
    task_count: str
    """Number of tasks contained in the list"""


class ListsSortFilter(TypedDict, total=False):
    """Available fields for sorting lists search results."""
    id: AirbyteSortOrder
    """Unique identifier for the list"""
    name: AirbyteSortOrder
    """Name of the list"""
    archived: AirbyteSortOrder
    """Whether the list has been archived"""
    due_date: AirbyteSortOrder
    """Due date for the list, in ClickUp timestamp format"""
    start_date: AirbyteSortOrder
    """Start date for the list, in ClickUp timestamp format"""
    priority: AirbyteSortOrder
    """Priority assigned to the list"""
    task_count: AirbyteSortOrder
    """Number of tasks contained in the list"""


# Entity-specific condition types for lists
class ListsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ListsSearchFilter


class ListsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ListsSearchFilter


class ListsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ListsSearchFilter


class ListsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ListsSearchFilter


class ListsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ListsSearchFilter


class ListsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ListsSearchFilter


class ListsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: ListsStringFilter


class ListsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: ListsStringFilter


class ListsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ListsStringFilter


class ListsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ListsStringFilter


class ListsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: ListsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ListsInCondition = TypedDict("ListsInCondition", {"in": ListsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ListsNotCondition = TypedDict("ListsNotCondition", {"not": "ListsCondition"}, total=False)
"""Negates the nested condition."""

ListsAndCondition = TypedDict("ListsAndCondition", {"and": "list[ListsCondition]"}, total=False)
"""True if all nested conditions are true."""

ListsOrCondition = TypedDict("ListsOrCondition", {"or": "list[ListsCondition]"}, total=False)
"""True if any nested condition is true."""

ListsAnyCondition = TypedDict("ListsAnyCondition", {"any": ListsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all lists condition types
ListsCondition = (
    ListsEqCondition
    | ListsNeqCondition
    | ListsGtCondition
    | ListsGteCondition
    | ListsLtCondition
    | ListsLteCondition
    | ListsInCondition
    | ListsStartswithCondition
    | ListsEndswithCondition
    | ListsFuzzyCondition
    | ListsKeywordCondition
    | ListsContainsCondition
    | ListsNotCondition
    | ListsAndCondition
    | ListsOrCondition
    | ListsAnyCondition
)


class ListsSearchQuery(TypedDict, total=False):
    """Search query for lists entity."""
    filter: ListsCondition
    sort: list[ListsSortFilter]


# ===== TASKS SEARCH TYPES =====

class TasksSearchFilter(TypedDict, total=False):
    """Available fields for filtering tasks search queries."""
    id: str | None
    """Unique identifier for the task"""
    name: str | None
    """Name of the task"""
    date_created: str | None
    """Creation timestamp of the task, in ClickUp timestamp format"""
    date_updated: str | None
    """Last update timestamp of the task, in ClickUp timestamp format"""
    date_closed: str | None
    """Timestamp when the task was closed, in ClickUp timestamp format"""
    due_date: str | None
    """Due date for the task, in ClickUp timestamp format"""
    start_date: str | None
    """Start date for the task, in ClickUp timestamp format"""
    parent: str | None
    """ID of the parent task, if this task is a subtask"""
    url: str | None
    """Permalink URL to view the task in ClickUp"""


class TasksInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the task"""
    name: list[str]
    """Name of the task"""
    date_created: list[str]
    """Creation timestamp of the task, in ClickUp timestamp format"""
    date_updated: list[str]
    """Last update timestamp of the task, in ClickUp timestamp format"""
    date_closed: list[str]
    """Timestamp when the task was closed, in ClickUp timestamp format"""
    due_date: list[str]
    """Due date for the task, in ClickUp timestamp format"""
    start_date: list[str]
    """Start date for the task, in ClickUp timestamp format"""
    parent: list[str]
    """ID of the parent task, if this task is a subtask"""
    url: list[str]
    """Permalink URL to view the task in ClickUp"""


class TasksAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the task"""
    name: Any
    """Name of the task"""
    date_created: Any
    """Creation timestamp of the task, in ClickUp timestamp format"""
    date_updated: Any
    """Last update timestamp of the task, in ClickUp timestamp format"""
    date_closed: Any
    """Timestamp when the task was closed, in ClickUp timestamp format"""
    due_date: Any
    """Due date for the task, in ClickUp timestamp format"""
    start_date: Any
    """Start date for the task, in ClickUp timestamp format"""
    parent: Any
    """ID of the parent task, if this task is a subtask"""
    url: Any
    """Permalink URL to view the task in ClickUp"""


class TasksStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the task"""
    name: str
    """Name of the task"""
    date_created: str
    """Creation timestamp of the task, in ClickUp timestamp format"""
    date_updated: str
    """Last update timestamp of the task, in ClickUp timestamp format"""
    date_closed: str
    """Timestamp when the task was closed, in ClickUp timestamp format"""
    due_date: str
    """Due date for the task, in ClickUp timestamp format"""
    start_date: str
    """Start date for the task, in ClickUp timestamp format"""
    parent: str
    """ID of the parent task, if this task is a subtask"""
    url: str
    """Permalink URL to view the task in ClickUp"""


class TasksSortFilter(TypedDict, total=False):
    """Available fields for sorting tasks search results."""
    id: AirbyteSortOrder
    """Unique identifier for the task"""
    name: AirbyteSortOrder
    """Name of the task"""
    date_created: AirbyteSortOrder
    """Creation timestamp of the task, in ClickUp timestamp format"""
    date_updated: AirbyteSortOrder
    """Last update timestamp of the task, in ClickUp timestamp format"""
    date_closed: AirbyteSortOrder
    """Timestamp when the task was closed, in ClickUp timestamp format"""
    due_date: AirbyteSortOrder
    """Due date for the task, in ClickUp timestamp format"""
    start_date: AirbyteSortOrder
    """Start date for the task, in ClickUp timestamp format"""
    parent: AirbyteSortOrder
    """ID of the parent task, if this task is a subtask"""
    url: AirbyteSortOrder
    """Permalink URL to view the task in ClickUp"""


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


class TasksStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: TasksStringFilter


class TasksEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: TasksStringFilter


class TasksFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TasksStringFilter


class TasksKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TasksStringFilter


class TasksContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | TasksStartswithCondition
    | TasksEndswithCondition
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


# ===== COMMENTS SEARCH TYPES =====

class CommentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering comments search queries."""
    id: str
    """Unique identifier for the comment"""
    comment_text: str | None
    """Plain-text content of the comment"""
    date: str | None
    """Timestamp when the comment was posted, in ClickUp timestamp format"""
    reply_count: float | None
    """Number of replies on the comment"""


class CommentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the comment"""
    comment_text: list[str]
    """Plain-text content of the comment"""
    date: list[str]
    """Timestamp when the comment was posted, in ClickUp timestamp format"""
    reply_count: list[float]
    """Number of replies on the comment"""


class CommentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the comment"""
    comment_text: Any
    """Plain-text content of the comment"""
    date: Any
    """Timestamp when the comment was posted, in ClickUp timestamp format"""
    reply_count: Any
    """Number of replies on the comment"""


class CommentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the comment"""
    comment_text: str
    """Plain-text content of the comment"""
    date: str
    """Timestamp when the comment was posted, in ClickUp timestamp format"""
    reply_count: str
    """Number of replies on the comment"""


class CommentsSortFilter(TypedDict, total=False):
    """Available fields for sorting comments search results."""
    id: AirbyteSortOrder
    """Unique identifier for the comment"""
    comment_text: AirbyteSortOrder
    """Plain-text content of the comment"""
    date: AirbyteSortOrder
    """Timestamp when the comment was posted, in ClickUp timestamp format"""
    reply_count: AirbyteSortOrder
    """Number of replies on the comment"""


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


class CommentsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CommentsStringFilter


class CommentsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CommentsStringFilter


class CommentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CommentsStringFilter


class CommentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CommentsStringFilter


class CommentsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
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
    | CommentsStartswithCondition
    | CommentsEndswithCondition
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


# ===== GOALS SEARCH TYPES =====

class GoalsSearchFilter(TypedDict, total=False):
    """Available fields for filtering goals search queries."""
    id: str
    """Unique identifier for the goal"""
    name: str | None
    """Name of the goal"""
    description: str | None
    """Description of the goal"""
    archived: bool | None
    """Whether the goal has been archived"""
    pinned: bool | None
    """Whether the goal is pinned to the top of the list"""
    private: bool | None
    """Whether the goal is private to its owners"""
    date_created: str | None
    """Creation timestamp of the goal, in ClickUp timestamp format"""
    due_date: str | None
    """Due date for the goal, in ClickUp timestamp format"""
    percent_completed: float | None
    """Completion percentage of the goal, between 0 and 100"""
    team_id: str | None
    """Identifier of the team that owns the goal"""


class GoalsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier for the goal"""
    name: list[str]
    """Name of the goal"""
    description: list[str]
    """Description of the goal"""
    archived: list[bool]
    """Whether the goal has been archived"""
    pinned: list[bool]
    """Whether the goal is pinned to the top of the list"""
    private: list[bool]
    """Whether the goal is private to its owners"""
    date_created: list[str]
    """Creation timestamp of the goal, in ClickUp timestamp format"""
    due_date: list[str]
    """Due date for the goal, in ClickUp timestamp format"""
    percent_completed: list[float]
    """Completion percentage of the goal, between 0 and 100"""
    team_id: list[str]
    """Identifier of the team that owns the goal"""


class GoalsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier for the goal"""
    name: Any
    """Name of the goal"""
    description: Any
    """Description of the goal"""
    archived: Any
    """Whether the goal has been archived"""
    pinned: Any
    """Whether the goal is pinned to the top of the list"""
    private: Any
    """Whether the goal is private to its owners"""
    date_created: Any
    """Creation timestamp of the goal, in ClickUp timestamp format"""
    due_date: Any
    """Due date for the goal, in ClickUp timestamp format"""
    percent_completed: Any
    """Completion percentage of the goal, between 0 and 100"""
    team_id: Any
    """Identifier of the team that owns the goal"""


class GoalsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    id: str
    """Unique identifier for the goal"""
    name: str
    """Name of the goal"""
    description: str
    """Description of the goal"""
    archived: str
    """Whether the goal has been archived"""
    pinned: str
    """Whether the goal is pinned to the top of the list"""
    private: str
    """Whether the goal is private to its owners"""
    date_created: str
    """Creation timestamp of the goal, in ClickUp timestamp format"""
    due_date: str
    """Due date for the goal, in ClickUp timestamp format"""
    percent_completed: str
    """Completion percentage of the goal, between 0 and 100"""
    team_id: str
    """Identifier of the team that owns the goal"""


class GoalsSortFilter(TypedDict, total=False):
    """Available fields for sorting goals search results."""
    id: AirbyteSortOrder
    """Unique identifier for the goal"""
    name: AirbyteSortOrder
    """Name of the goal"""
    description: AirbyteSortOrder
    """Description of the goal"""
    archived: AirbyteSortOrder
    """Whether the goal has been archived"""
    pinned: AirbyteSortOrder
    """Whether the goal is pinned to the top of the list"""
    private: AirbyteSortOrder
    """Whether the goal is private to its owners"""
    date_created: AirbyteSortOrder
    """Creation timestamp of the goal, in ClickUp timestamp format"""
    due_date: AirbyteSortOrder
    """Due date for the goal, in ClickUp timestamp format"""
    percent_completed: AirbyteSortOrder
    """Completion percentage of the goal, between 0 and 100"""
    team_id: AirbyteSortOrder
    """Identifier of the team that owns the goal"""


# Entity-specific condition types for goals
class GoalsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: GoalsSearchFilter


class GoalsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: GoalsSearchFilter


class GoalsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: GoalsSearchFilter


class GoalsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: GoalsSearchFilter


class GoalsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: GoalsSearchFilter


class GoalsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: GoalsSearchFilter


class GoalsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: GoalsStringFilter


class GoalsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: GoalsStringFilter


class GoalsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: GoalsStringFilter


class GoalsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: GoalsStringFilter


class GoalsContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: GoalsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
GoalsInCondition = TypedDict("GoalsInCondition", {"in": GoalsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

GoalsNotCondition = TypedDict("GoalsNotCondition", {"not": "GoalsCondition"}, total=False)
"""Negates the nested condition."""

GoalsAndCondition = TypedDict("GoalsAndCondition", {"and": "list[GoalsCondition]"}, total=False)
"""True if all nested conditions are true."""

GoalsOrCondition = TypedDict("GoalsOrCondition", {"or": "list[GoalsCondition]"}, total=False)
"""True if any nested condition is true."""

GoalsAnyCondition = TypedDict("GoalsAnyCondition", {"any": GoalsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all goals condition types
GoalsCondition = (
    GoalsEqCondition
    | GoalsNeqCondition
    | GoalsGtCondition
    | GoalsGteCondition
    | GoalsLtCondition
    | GoalsLteCondition
    | GoalsInCondition
    | GoalsStartswithCondition
    | GoalsEndswithCondition
    | GoalsFuzzyCondition
    | GoalsKeywordCondition
    | GoalsContainsCondition
    | GoalsNotCondition
    | GoalsAndCondition
    | GoalsOrCondition
    | GoalsAnyCondition
)


class GoalsSearchQuery(TypedDict, total=False):
    """Search query for goals entity."""
    filter: GoalsCondition
    sort: list[GoalsSortFilter]


# ===== TIME_TRACKING SEARCH TYPES =====

class TimeTrackingSearchFilter(TypedDict, total=False):
    """Available fields for filtering time_tracking search queries."""
    time: float | None
    """Total tracked time in milliseconds"""
    user: dict[str, Any] | None
    """User who tracked the time"""


class TimeTrackingInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    time: list[float]
    """Total tracked time in milliseconds"""
    user: list[dict[str, Any]]
    """User who tracked the time"""


class TimeTrackingAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    time: Any
    """Total tracked time in milliseconds"""
    user: Any
    """User who tracked the time"""


class TimeTrackingStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    time: str
    """Total tracked time in milliseconds"""
    user: str
    """User who tracked the time"""


class TimeTrackingSortFilter(TypedDict, total=False):
    """Available fields for sorting time_tracking search results."""
    time: AirbyteSortOrder
    """Total tracked time in milliseconds"""
    user: AirbyteSortOrder
    """User who tracked the time"""


# Entity-specific condition types for time_tracking
class TimeTrackingEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TimeTrackingSearchFilter


class TimeTrackingNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TimeTrackingSearchFilter


class TimeTrackingGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TimeTrackingSearchFilter


class TimeTrackingGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TimeTrackingSearchFilter


class TimeTrackingLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TimeTrackingSearchFilter


class TimeTrackingLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TimeTrackingSearchFilter


class TimeTrackingStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: TimeTrackingStringFilter


class TimeTrackingEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: TimeTrackingStringFilter


class TimeTrackingFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TimeTrackingStringFilter


class TimeTrackingKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TimeTrackingStringFilter


class TimeTrackingContainsCondition(TypedDict, total=False):
    """Literal case-insensitive substring on scalar fields or exact array membership."""
    contains: TimeTrackingAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TimeTrackingInCondition = TypedDict("TimeTrackingInCondition", {"in": TimeTrackingInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TimeTrackingNotCondition = TypedDict("TimeTrackingNotCondition", {"not": "TimeTrackingCondition"}, total=False)
"""Negates the nested condition."""

TimeTrackingAndCondition = TypedDict("TimeTrackingAndCondition", {"and": "list[TimeTrackingCondition]"}, total=False)
"""True if all nested conditions are true."""

TimeTrackingOrCondition = TypedDict("TimeTrackingOrCondition", {"or": "list[TimeTrackingCondition]"}, total=False)
"""True if any nested condition is true."""

TimeTrackingAnyCondition = TypedDict("TimeTrackingAnyCondition", {"any": TimeTrackingAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all time_tracking condition types
TimeTrackingCondition = (
    TimeTrackingEqCondition
    | TimeTrackingNeqCondition
    | TimeTrackingGtCondition
    | TimeTrackingGteCondition
    | TimeTrackingLtCondition
    | TimeTrackingLteCondition
    | TimeTrackingInCondition
    | TimeTrackingStartswithCondition
    | TimeTrackingEndswithCondition
    | TimeTrackingFuzzyCondition
    | TimeTrackingKeywordCondition
    | TimeTrackingContainsCondition
    | TimeTrackingNotCondition
    | TimeTrackingAndCondition
    | TimeTrackingOrCondition
    | TimeTrackingAnyCondition
)


class TimeTrackingSearchQuery(TypedDict, total=False):
    """Search query for time_tracking entity."""
    filter: TimeTrackingCondition
    sort: list[TimeTrackingSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
