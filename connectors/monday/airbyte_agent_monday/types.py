"""
Type definitions for monday connector.
"""
from __future__ import annotations

from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig  # noqa: F401

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any, Literal


# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    pass

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class BoardsListParams(TypedDict):
    """Parameters for boards.list operation"""
    pass

class BoardsGetParams(TypedDict):
    """Parameters for boards.get operation"""
    id: str

class ItemsListParams(TypedDict):
    """Parameters for items.list operation"""
    board_id: str

class ItemsGetParams(TypedDict):
    """Parameters for items.get operation"""
    id: str

class TeamsListParams(TypedDict):
    """Parameters for teams.list operation"""
    pass

class TeamsGetParams(TypedDict):
    """Parameters for teams.get operation"""
    id: str

class TagsListParams(TypedDict):
    """Parameters for tags.list operation"""
    pass

class UpdatesListParams(TypedDict):
    """Parameters for updates.list operation"""
    page: NotRequired[int]
    limit: NotRequired[int]

class UpdatesGetParams(TypedDict):
    """Parameters for updates.get operation"""
    id: str

class WorkspacesListParams(TypedDict):
    """Parameters for workspaces.list operation"""
    pass

class WorkspacesGetParams(TypedDict):
    """Parameters for workspaces.get operation"""
    id: str

class ActivityLogsListParams(TypedDict):
    """Parameters for activity_logs.list operation"""
    board_id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== ACTIVITY_LOGS SEARCH TYPES =====

class ActivityLogsSearchFilter(TypedDict, total=False):
    """Available fields for filtering activity_logs search queries."""
    board_id: int | None
    """Board ID the activity belongs to"""
    created_at: str | None
    """When the activity occurred"""
    created_at_int: int | None
    """When the activity occurred (Unix timestamp)"""
    data: str | None
    """Event data (JSON string)"""
    entity: str | None
    """Entity type that was affected"""
    event: str | None
    """Event type"""
    id: str | None
    """Unique activity log identifier"""
    pulse_id: int | None
    """Item (pulse) ID the activity belongs to"""
    user_id: str | None
    """ID of the user who performed the action"""


class ActivityLogsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    board_id: list[int]
    """Board ID the activity belongs to"""
    created_at: list[str]
    """When the activity occurred"""
    created_at_int: list[int]
    """When the activity occurred (Unix timestamp)"""
    data: list[str]
    """Event data (JSON string)"""
    entity: list[str]
    """Entity type that was affected"""
    event: list[str]
    """Event type"""
    id: list[str]
    """Unique activity log identifier"""
    pulse_id: list[int]
    """Item (pulse) ID the activity belongs to"""
    user_id: list[str]
    """ID of the user who performed the action"""


class ActivityLogsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    board_id: Any
    """Board ID the activity belongs to"""
    created_at: Any
    """When the activity occurred"""
    created_at_int: Any
    """When the activity occurred (Unix timestamp)"""
    data: Any
    """Event data (JSON string)"""
    entity: Any
    """Entity type that was affected"""
    event: Any
    """Event type"""
    id: Any
    """Unique activity log identifier"""
    pulse_id: Any
    """Item (pulse) ID the activity belongs to"""
    user_id: Any
    """ID of the user who performed the action"""


class ActivityLogsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    board_id: str
    """Board ID the activity belongs to"""
    created_at: str
    """When the activity occurred"""
    created_at_int: str
    """When the activity occurred (Unix timestamp)"""
    data: str
    """Event data (JSON string)"""
    entity: str
    """Entity type that was affected"""
    event: str
    """Event type"""
    id: str
    """Unique activity log identifier"""
    pulse_id: str
    """Item (pulse) ID the activity belongs to"""
    user_id: str
    """ID of the user who performed the action"""


class ActivityLogsSortFilter(TypedDict, total=False):
    """Available fields for sorting activity_logs search results."""
    board_id: AirbyteSortOrder
    """Board ID the activity belongs to"""
    created_at: AirbyteSortOrder
    """When the activity occurred"""
    created_at_int: AirbyteSortOrder
    """When the activity occurred (Unix timestamp)"""
    data: AirbyteSortOrder
    """Event data (JSON string)"""
    entity: AirbyteSortOrder
    """Entity type that was affected"""
    event: AirbyteSortOrder
    """Event type"""
    id: AirbyteSortOrder
    """Unique activity log identifier"""
    pulse_id: AirbyteSortOrder
    """Item (pulse) ID the activity belongs to"""
    user_id: AirbyteSortOrder
    """ID of the user who performed the action"""


# Entity-specific condition types for activity_logs
class ActivityLogsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ActivityLogsSearchFilter


class ActivityLogsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ActivityLogsSearchFilter


class ActivityLogsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ActivityLogsSearchFilter


class ActivityLogsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ActivityLogsSearchFilter


class ActivityLogsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ActivityLogsSearchFilter


class ActivityLogsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ActivityLogsSearchFilter


class ActivityLogsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ActivityLogsStringFilter


class ActivityLogsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ActivityLogsStringFilter


class ActivityLogsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ActivityLogsStringFilter


class ActivityLogsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ActivityLogsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ActivityLogsInCondition = TypedDict("ActivityLogsInCondition", {"in": ActivityLogsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ActivityLogsNotCondition = TypedDict("ActivityLogsNotCondition", {"not": "ActivityLogsCondition"}, total=False)
"""Negates the nested condition."""

ActivityLogsAndCondition = TypedDict("ActivityLogsAndCondition", {"and": "list[ActivityLogsCondition]"}, total=False)
"""True if all nested conditions are true."""

ActivityLogsOrCondition = TypedDict("ActivityLogsOrCondition", {"or": "list[ActivityLogsCondition]"}, total=False)
"""True if any nested condition is true."""

ActivityLogsAnyCondition = TypedDict("ActivityLogsAnyCondition", {"any": ActivityLogsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all activity_logs condition types
ActivityLogsCondition = (
    ActivityLogsEqCondition
    | ActivityLogsNeqCondition
    | ActivityLogsGtCondition
    | ActivityLogsGteCondition
    | ActivityLogsLtCondition
    | ActivityLogsLteCondition
    | ActivityLogsInCondition
    | ActivityLogsLikeCondition
    | ActivityLogsFuzzyCondition
    | ActivityLogsKeywordCondition
    | ActivityLogsContainsCondition
    | ActivityLogsNotCondition
    | ActivityLogsAndCondition
    | ActivityLogsOrCondition
    | ActivityLogsAnyCondition
)


class ActivityLogsSearchQuery(TypedDict, total=False):
    """Search query for activity_logs entity."""
    filter: ActivityLogsCondition
    sort: list[ActivityLogsSortFilter]


# ===== BOARDS SEARCH TYPES =====

class BoardsSearchFilter(TypedDict, total=False):
    """Available fields for filtering boards search queries."""
    board_kind: str | None
    """Board kind (public, private, share)"""
    columns: list[Any] | None
    """Board columns"""
    communication: str | None
    """Board communication value"""
    creator: dict[str, Any] | None
    """Board creator"""
    description: str | None
    """Board description"""
    groups: list[Any] | None
    """Board groups"""
    id: str | None
    """Unique board identifier"""
    name: str | None
    """Board name"""
    owners: list[Any] | None
    """Board owners"""
    permissions: str | None
    """Board permissions"""
    state: str | None
    """Board state (active, archived, deleted)"""
    subscribers: list[Any] | None
    """Board subscribers"""
    tags: list[Any] | None
    """Board tags"""
    top_group: dict[str, Any] | None
    """Top group on the board"""
    type_: str | None
    """Board type"""
    updated_at: str | None
    """When the board was last updated"""
    updated_at_int: int | None
    """When the board was last updated (Unix timestamp)"""
    updates: list[Any] | None
    """Board updates"""
    views: list[Any] | None
    """Board views"""
    workspace: dict[str, Any] | None
    """Workspace the board belongs to"""


class BoardsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    board_kind: list[str]
    """Board kind (public, private, share)"""
    columns: list[list[Any]]
    """Board columns"""
    communication: list[str]
    """Board communication value"""
    creator: list[dict[str, Any]]
    """Board creator"""
    description: list[str]
    """Board description"""
    groups: list[list[Any]]
    """Board groups"""
    id: list[str]
    """Unique board identifier"""
    name: list[str]
    """Board name"""
    owners: list[list[Any]]
    """Board owners"""
    permissions: list[str]
    """Board permissions"""
    state: list[str]
    """Board state (active, archived, deleted)"""
    subscribers: list[list[Any]]
    """Board subscribers"""
    tags: list[list[Any]]
    """Board tags"""
    top_group: list[dict[str, Any]]
    """Top group on the board"""
    type_: list[str]
    """Board type"""
    updated_at: list[str]
    """When the board was last updated"""
    updated_at_int: list[int]
    """When the board was last updated (Unix timestamp)"""
    updates: list[list[Any]]
    """Board updates"""
    views: list[list[Any]]
    """Board views"""
    workspace: list[dict[str, Any]]
    """Workspace the board belongs to"""


class BoardsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    board_kind: Any
    """Board kind (public, private, share)"""
    columns: Any
    """Board columns"""
    communication: Any
    """Board communication value"""
    creator: Any
    """Board creator"""
    description: Any
    """Board description"""
    groups: Any
    """Board groups"""
    id: Any
    """Unique board identifier"""
    name: Any
    """Board name"""
    owners: Any
    """Board owners"""
    permissions: Any
    """Board permissions"""
    state: Any
    """Board state (active, archived, deleted)"""
    subscribers: Any
    """Board subscribers"""
    tags: Any
    """Board tags"""
    top_group: Any
    """Top group on the board"""
    type_: Any
    """Board type"""
    updated_at: Any
    """When the board was last updated"""
    updated_at_int: Any
    """When the board was last updated (Unix timestamp)"""
    updates: Any
    """Board updates"""
    views: Any
    """Board views"""
    workspace: Any
    """Workspace the board belongs to"""


class BoardsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    board_kind: str
    """Board kind (public, private, share)"""
    columns: str
    """Board columns"""
    communication: str
    """Board communication value"""
    creator: str
    """Board creator"""
    description: str
    """Board description"""
    groups: str
    """Board groups"""
    id: str
    """Unique board identifier"""
    name: str
    """Board name"""
    owners: str
    """Board owners"""
    permissions: str
    """Board permissions"""
    state: str
    """Board state (active, archived, deleted)"""
    subscribers: str
    """Board subscribers"""
    tags: str
    """Board tags"""
    top_group: str
    """Top group on the board"""
    type_: str
    """Board type"""
    updated_at: str
    """When the board was last updated"""
    updated_at_int: str
    """When the board was last updated (Unix timestamp)"""
    updates: str
    """Board updates"""
    views: str
    """Board views"""
    workspace: str
    """Workspace the board belongs to"""


class BoardsSortFilter(TypedDict, total=False):
    """Available fields for sorting boards search results."""
    board_kind: AirbyteSortOrder
    """Board kind (public, private, share)"""
    columns: AirbyteSortOrder
    """Board columns"""
    communication: AirbyteSortOrder
    """Board communication value"""
    creator: AirbyteSortOrder
    """Board creator"""
    description: AirbyteSortOrder
    """Board description"""
    groups: AirbyteSortOrder
    """Board groups"""
    id: AirbyteSortOrder
    """Unique board identifier"""
    name: AirbyteSortOrder
    """Board name"""
    owners: AirbyteSortOrder
    """Board owners"""
    permissions: AirbyteSortOrder
    """Board permissions"""
    state: AirbyteSortOrder
    """Board state (active, archived, deleted)"""
    subscribers: AirbyteSortOrder
    """Board subscribers"""
    tags: AirbyteSortOrder
    """Board tags"""
    top_group: AirbyteSortOrder
    """Top group on the board"""
    type_: AirbyteSortOrder
    """Board type"""
    updated_at: AirbyteSortOrder
    """When the board was last updated"""
    updated_at_int: AirbyteSortOrder
    """When the board was last updated (Unix timestamp)"""
    updates: AirbyteSortOrder
    """Board updates"""
    views: AirbyteSortOrder
    """Board views"""
    workspace: AirbyteSortOrder
    """Workspace the board belongs to"""


# Entity-specific condition types for boards
class BoardsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BoardsSearchFilter


class BoardsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BoardsSearchFilter


class BoardsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BoardsSearchFilter


class BoardsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BoardsSearchFilter


class BoardsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BoardsSearchFilter


class BoardsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BoardsSearchFilter


class BoardsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BoardsStringFilter


class BoardsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BoardsStringFilter


class BoardsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BoardsStringFilter


class BoardsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BoardsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BoardsInCondition = TypedDict("BoardsInCondition", {"in": BoardsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BoardsNotCondition = TypedDict("BoardsNotCondition", {"not": "BoardsCondition"}, total=False)
"""Negates the nested condition."""

BoardsAndCondition = TypedDict("BoardsAndCondition", {"and": "list[BoardsCondition]"}, total=False)
"""True if all nested conditions are true."""

BoardsOrCondition = TypedDict("BoardsOrCondition", {"or": "list[BoardsCondition]"}, total=False)
"""True if any nested condition is true."""

BoardsAnyCondition = TypedDict("BoardsAnyCondition", {"any": BoardsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all boards condition types
BoardsCondition = (
    BoardsEqCondition
    | BoardsNeqCondition
    | BoardsGtCondition
    | BoardsGteCondition
    | BoardsLtCondition
    | BoardsLteCondition
    | BoardsInCondition
    | BoardsLikeCondition
    | BoardsFuzzyCondition
    | BoardsKeywordCondition
    | BoardsContainsCondition
    | BoardsNotCondition
    | BoardsAndCondition
    | BoardsOrCondition
    | BoardsAnyCondition
)


class BoardsSearchQuery(TypedDict, total=False):
    """Search query for boards entity."""
    filter: BoardsCondition
    sort: list[BoardsSortFilter]


# ===== ITEMS SEARCH TYPES =====

class ItemsSearchFilter(TypedDict, total=False):
    """Available fields for filtering items search queries."""
    assets: list[Any] | None
    """Files attached to the item"""
    board: dict[str, Any] | None
    """Board the item belongs to"""
    column_values: list[Any] | None
    """Item column values"""
    created_at: str | None
    """When the item was created"""
    creator_id: str | None
    """ID of the user who created the item"""
    group: dict[str, Any] | None
    """Group the item belongs to"""
    id: str | None
    """Unique item identifier"""
    name: str | None
    """Item name"""
    parent_item: dict[str, Any] | None
    """Parent item (for subitems)"""
    state: str | None
    """Item state (active, archived, deleted)"""
    subscribers: list[Any] | None
    """Item subscribers"""
    updated_at: str | None
    """When the item was last updated"""
    updated_at_int: int | None
    """When the item was last updated (Unix timestamp)"""
    updates: list[Any] | None
    """Item updates"""


class ItemsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    assets: list[list[Any]]
    """Files attached to the item"""
    board: list[dict[str, Any]]
    """Board the item belongs to"""
    column_values: list[list[Any]]
    """Item column values"""
    created_at: list[str]
    """When the item was created"""
    creator_id: list[str]
    """ID of the user who created the item"""
    group: list[dict[str, Any]]
    """Group the item belongs to"""
    id: list[str]
    """Unique item identifier"""
    name: list[str]
    """Item name"""
    parent_item: list[dict[str, Any]]
    """Parent item (for subitems)"""
    state: list[str]
    """Item state (active, archived, deleted)"""
    subscribers: list[list[Any]]
    """Item subscribers"""
    updated_at: list[str]
    """When the item was last updated"""
    updated_at_int: list[int]
    """When the item was last updated (Unix timestamp)"""
    updates: list[list[Any]]
    """Item updates"""


class ItemsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    assets: Any
    """Files attached to the item"""
    board: Any
    """Board the item belongs to"""
    column_values: Any
    """Item column values"""
    created_at: Any
    """When the item was created"""
    creator_id: Any
    """ID of the user who created the item"""
    group: Any
    """Group the item belongs to"""
    id: Any
    """Unique item identifier"""
    name: Any
    """Item name"""
    parent_item: Any
    """Parent item (for subitems)"""
    state: Any
    """Item state (active, archived, deleted)"""
    subscribers: Any
    """Item subscribers"""
    updated_at: Any
    """When the item was last updated"""
    updated_at_int: Any
    """When the item was last updated (Unix timestamp)"""
    updates: Any
    """Item updates"""


class ItemsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    assets: str
    """Files attached to the item"""
    board: str
    """Board the item belongs to"""
    column_values: str
    """Item column values"""
    created_at: str
    """When the item was created"""
    creator_id: str
    """ID of the user who created the item"""
    group: str
    """Group the item belongs to"""
    id: str
    """Unique item identifier"""
    name: str
    """Item name"""
    parent_item: str
    """Parent item (for subitems)"""
    state: str
    """Item state (active, archived, deleted)"""
    subscribers: str
    """Item subscribers"""
    updated_at: str
    """When the item was last updated"""
    updated_at_int: str
    """When the item was last updated (Unix timestamp)"""
    updates: str
    """Item updates"""


class ItemsSortFilter(TypedDict, total=False):
    """Available fields for sorting items search results."""
    assets: AirbyteSortOrder
    """Files attached to the item"""
    board: AirbyteSortOrder
    """Board the item belongs to"""
    column_values: AirbyteSortOrder
    """Item column values"""
    created_at: AirbyteSortOrder
    """When the item was created"""
    creator_id: AirbyteSortOrder
    """ID of the user who created the item"""
    group: AirbyteSortOrder
    """Group the item belongs to"""
    id: AirbyteSortOrder
    """Unique item identifier"""
    name: AirbyteSortOrder
    """Item name"""
    parent_item: AirbyteSortOrder
    """Parent item (for subitems)"""
    state: AirbyteSortOrder
    """Item state (active, archived, deleted)"""
    subscribers: AirbyteSortOrder
    """Item subscribers"""
    updated_at: AirbyteSortOrder
    """When the item was last updated"""
    updated_at_int: AirbyteSortOrder
    """When the item was last updated (Unix timestamp)"""
    updates: AirbyteSortOrder
    """Item updates"""


# Entity-specific condition types for items
class ItemsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ItemsSearchFilter


class ItemsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ItemsSearchFilter


class ItemsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ItemsSearchFilter


class ItemsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ItemsSearchFilter


class ItemsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ItemsSearchFilter


class ItemsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ItemsSearchFilter


class ItemsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ItemsStringFilter


class ItemsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ItemsStringFilter


class ItemsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ItemsStringFilter


class ItemsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ItemsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ItemsInCondition = TypedDict("ItemsInCondition", {"in": ItemsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ItemsNotCondition = TypedDict("ItemsNotCondition", {"not": "ItemsCondition"}, total=False)
"""Negates the nested condition."""

ItemsAndCondition = TypedDict("ItemsAndCondition", {"and": "list[ItemsCondition]"}, total=False)
"""True if all nested conditions are true."""

ItemsOrCondition = TypedDict("ItemsOrCondition", {"or": "list[ItemsCondition]"}, total=False)
"""True if any nested condition is true."""

ItemsAnyCondition = TypedDict("ItemsAnyCondition", {"any": ItemsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all items condition types
ItemsCondition = (
    ItemsEqCondition
    | ItemsNeqCondition
    | ItemsGtCondition
    | ItemsGteCondition
    | ItemsLtCondition
    | ItemsLteCondition
    | ItemsInCondition
    | ItemsLikeCondition
    | ItemsFuzzyCondition
    | ItemsKeywordCondition
    | ItemsContainsCondition
    | ItemsNotCondition
    | ItemsAndCondition
    | ItemsOrCondition
    | ItemsAnyCondition
)


class ItemsSearchQuery(TypedDict, total=False):
    """Search query for items entity."""
    filter: ItemsCondition
    sort: list[ItemsSortFilter]


# ===== TAGS SEARCH TYPES =====

class TagsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tags search queries."""
    color: str | None
    """Tag color"""
    id: str | None
    """Unique tag identifier"""
    name: str | None
    """Tag name"""


class TagsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    color: list[str]
    """Tag color"""
    id: list[str]
    """Unique tag identifier"""
    name: list[str]
    """Tag name"""


class TagsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    color: Any
    """Tag color"""
    id: Any
    """Unique tag identifier"""
    name: Any
    """Tag name"""


class TagsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    color: str
    """Tag color"""
    id: str
    """Unique tag identifier"""
    name: str
    """Tag name"""


class TagsSortFilter(TypedDict, total=False):
    """Available fields for sorting tags search results."""
    color: AirbyteSortOrder
    """Tag color"""
    id: AirbyteSortOrder
    """Unique tag identifier"""
    name: AirbyteSortOrder
    """Tag name"""


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


# ===== TEAMS SEARCH TYPES =====

class TeamsSearchFilter(TypedDict, total=False):
    """Available fields for filtering teams search queries."""
    id: int | None
    """Unique team identifier"""
    name: str | None
    """Team name"""
    picture_url: str | None
    """Team picture URL"""
    users: list[Any] | None
    """Team members"""


class TeamsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[int]
    """Unique team identifier"""
    name: list[str]
    """Team name"""
    picture_url: list[str]
    """Team picture URL"""
    users: list[list[Any]]
    """Team members"""


class TeamsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique team identifier"""
    name: Any
    """Team name"""
    picture_url: Any
    """Team picture URL"""
    users: Any
    """Team members"""


class TeamsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique team identifier"""
    name: str
    """Team name"""
    picture_url: str
    """Team picture URL"""
    users: str
    """Team members"""


class TeamsSortFilter(TypedDict, total=False):
    """Available fields for sorting teams search results."""
    id: AirbyteSortOrder
    """Unique team identifier"""
    name: AirbyteSortOrder
    """Team name"""
    picture_url: AirbyteSortOrder
    """Team picture URL"""
    users: AirbyteSortOrder
    """Team members"""


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


# ===== UPDATES SEARCH TYPES =====

class UpdatesSearchFilter(TypedDict, total=False):
    """Available fields for filtering updates search queries."""
    assets: list[Any] | None
    """Files attached to this update"""
    body: str | None
    """Update body (HTML)"""
    created_at: str | None
    """When the update was created"""
    creator_id: str | None
    """ID of the user who created the update"""
    id: str | None
    """Unique update identifier"""
    item_id: str | None
    """ID of the item this update belongs to"""
    replies: list[Any] | None
    """Replies to this update"""
    text_body: str | None
    """Update body (plain text)"""
    updated_at: str | None
    """When the update was last modified"""


class UpdatesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    assets: list[list[Any]]
    """Files attached to this update"""
    body: list[str]
    """Update body (HTML)"""
    created_at: list[str]
    """When the update was created"""
    creator_id: list[str]
    """ID of the user who created the update"""
    id: list[str]
    """Unique update identifier"""
    item_id: list[str]
    """ID of the item this update belongs to"""
    replies: list[list[Any]]
    """Replies to this update"""
    text_body: list[str]
    """Update body (plain text)"""
    updated_at: list[str]
    """When the update was last modified"""


class UpdatesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    assets: Any
    """Files attached to this update"""
    body: Any
    """Update body (HTML)"""
    created_at: Any
    """When the update was created"""
    creator_id: Any
    """ID of the user who created the update"""
    id: Any
    """Unique update identifier"""
    item_id: Any
    """ID of the item this update belongs to"""
    replies: Any
    """Replies to this update"""
    text_body: Any
    """Update body (plain text)"""
    updated_at: Any
    """When the update was last modified"""


class UpdatesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    assets: str
    """Files attached to this update"""
    body: str
    """Update body (HTML)"""
    created_at: str
    """When the update was created"""
    creator_id: str
    """ID of the user who created the update"""
    id: str
    """Unique update identifier"""
    item_id: str
    """ID of the item this update belongs to"""
    replies: str
    """Replies to this update"""
    text_body: str
    """Update body (plain text)"""
    updated_at: str
    """When the update was last modified"""


class UpdatesSortFilter(TypedDict, total=False):
    """Available fields for sorting updates search results."""
    assets: AirbyteSortOrder
    """Files attached to this update"""
    body: AirbyteSortOrder
    """Update body (HTML)"""
    created_at: AirbyteSortOrder
    """When the update was created"""
    creator_id: AirbyteSortOrder
    """ID of the user who created the update"""
    id: AirbyteSortOrder
    """Unique update identifier"""
    item_id: AirbyteSortOrder
    """ID of the item this update belongs to"""
    replies: AirbyteSortOrder
    """Replies to this update"""
    text_body: AirbyteSortOrder
    """Update body (plain text)"""
    updated_at: AirbyteSortOrder
    """When the update was last modified"""


# Entity-specific condition types for updates
class UpdatesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: UpdatesSearchFilter


class UpdatesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: UpdatesSearchFilter


class UpdatesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: UpdatesSearchFilter


class UpdatesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: UpdatesSearchFilter


class UpdatesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: UpdatesSearchFilter


class UpdatesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: UpdatesSearchFilter


class UpdatesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: UpdatesStringFilter


class UpdatesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UpdatesStringFilter


class UpdatesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UpdatesStringFilter


class UpdatesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: UpdatesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
UpdatesInCondition = TypedDict("UpdatesInCondition", {"in": UpdatesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

UpdatesNotCondition = TypedDict("UpdatesNotCondition", {"not": "UpdatesCondition"}, total=False)
"""Negates the nested condition."""

UpdatesAndCondition = TypedDict("UpdatesAndCondition", {"and": "list[UpdatesCondition]"}, total=False)
"""True if all nested conditions are true."""

UpdatesOrCondition = TypedDict("UpdatesOrCondition", {"or": "list[UpdatesCondition]"}, total=False)
"""True if any nested condition is true."""

UpdatesAnyCondition = TypedDict("UpdatesAnyCondition", {"any": UpdatesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all updates condition types
UpdatesCondition = (
    UpdatesEqCondition
    | UpdatesNeqCondition
    | UpdatesGtCondition
    | UpdatesGteCondition
    | UpdatesLtCondition
    | UpdatesLteCondition
    | UpdatesInCondition
    | UpdatesLikeCondition
    | UpdatesFuzzyCondition
    | UpdatesKeywordCondition
    | UpdatesContainsCondition
    | UpdatesNotCondition
    | UpdatesAndCondition
    | UpdatesOrCondition
    | UpdatesAnyCondition
)


class UpdatesSearchQuery(TypedDict, total=False):
    """Search query for updates entity."""
    filter: UpdatesCondition
    sort: list[UpdatesSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    birthday: str | None
    """User's birthday"""
    country_code: str | None
    """User's country code"""
    created_at: str | None
    """When the user was created"""
    email: str | None
    """User's email address"""
    enabled: bool | None
    """Whether the user account is enabled"""
    id: str | None
    """Unique user identifier"""
    is_admin: bool | None
    """Whether the user is an admin"""
    is_guest: bool | None
    """Whether the user is a guest"""
    is_pending: bool | None
    """Whether the user is pending"""
    is_view_only: bool | None
    """Whether the user is view-only"""
    is_verified: bool | None
    """Whether the user is verified"""
    join_date: str | None
    """When the user joined"""
    location: str | None
    """User's location"""
    mobile_phone: str | None
    """User's mobile phone number"""
    name: str | None
    """User's display name"""
    phone: str | None
    """User's phone number"""
    photo_original: str | None
    """URL to original size photo"""
    photo_small: str | None
    """URL to small photo"""
    photo_thumb: str | None
    """URL to thumbnail photo"""
    photo_thumb_small: str | None
    """URL to small thumbnail photo"""
    photo_tiny: str | None
    """URL to tiny photo"""
    time_zone_identifier: str | None
    """User's timezone identifier"""
    title: str | None
    """User's job title"""
    url: str | None
    """User's Monday.com profile URL"""
    utc_hours_diff: int | None
    """UTC hours difference for the user's timezone"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    birthday: list[str]
    """User's birthday"""
    country_code: list[str]
    """User's country code"""
    created_at: list[str]
    """When the user was created"""
    email: list[str]
    """User's email address"""
    enabled: list[bool]
    """Whether the user account is enabled"""
    id: list[str]
    """Unique user identifier"""
    is_admin: list[bool]
    """Whether the user is an admin"""
    is_guest: list[bool]
    """Whether the user is a guest"""
    is_pending: list[bool]
    """Whether the user is pending"""
    is_view_only: list[bool]
    """Whether the user is view-only"""
    is_verified: list[bool]
    """Whether the user is verified"""
    join_date: list[str]
    """When the user joined"""
    location: list[str]
    """User's location"""
    mobile_phone: list[str]
    """User's mobile phone number"""
    name: list[str]
    """User's display name"""
    phone: list[str]
    """User's phone number"""
    photo_original: list[str]
    """URL to original size photo"""
    photo_small: list[str]
    """URL to small photo"""
    photo_thumb: list[str]
    """URL to thumbnail photo"""
    photo_thumb_small: list[str]
    """URL to small thumbnail photo"""
    photo_tiny: list[str]
    """URL to tiny photo"""
    time_zone_identifier: list[str]
    """User's timezone identifier"""
    title: list[str]
    """User's job title"""
    url: list[str]
    """User's Monday.com profile URL"""
    utc_hours_diff: list[int]
    """UTC hours difference for the user's timezone"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    birthday: Any
    """User's birthday"""
    country_code: Any
    """User's country code"""
    created_at: Any
    """When the user was created"""
    email: Any
    """User's email address"""
    enabled: Any
    """Whether the user account is enabled"""
    id: Any
    """Unique user identifier"""
    is_admin: Any
    """Whether the user is an admin"""
    is_guest: Any
    """Whether the user is a guest"""
    is_pending: Any
    """Whether the user is pending"""
    is_view_only: Any
    """Whether the user is view-only"""
    is_verified: Any
    """Whether the user is verified"""
    join_date: Any
    """When the user joined"""
    location: Any
    """User's location"""
    mobile_phone: Any
    """User's mobile phone number"""
    name: Any
    """User's display name"""
    phone: Any
    """User's phone number"""
    photo_original: Any
    """URL to original size photo"""
    photo_small: Any
    """URL to small photo"""
    photo_thumb: Any
    """URL to thumbnail photo"""
    photo_thumb_small: Any
    """URL to small thumbnail photo"""
    photo_tiny: Any
    """URL to tiny photo"""
    time_zone_identifier: Any
    """User's timezone identifier"""
    title: Any
    """User's job title"""
    url: Any
    """User's Monday.com profile URL"""
    utc_hours_diff: Any
    """UTC hours difference for the user's timezone"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    birthday: str
    """User's birthday"""
    country_code: str
    """User's country code"""
    created_at: str
    """When the user was created"""
    email: str
    """User's email address"""
    enabled: str
    """Whether the user account is enabled"""
    id: str
    """Unique user identifier"""
    is_admin: str
    """Whether the user is an admin"""
    is_guest: str
    """Whether the user is a guest"""
    is_pending: str
    """Whether the user is pending"""
    is_view_only: str
    """Whether the user is view-only"""
    is_verified: str
    """Whether the user is verified"""
    join_date: str
    """When the user joined"""
    location: str
    """User's location"""
    mobile_phone: str
    """User's mobile phone number"""
    name: str
    """User's display name"""
    phone: str
    """User's phone number"""
    photo_original: str
    """URL to original size photo"""
    photo_small: str
    """URL to small photo"""
    photo_thumb: str
    """URL to thumbnail photo"""
    photo_thumb_small: str
    """URL to small thumbnail photo"""
    photo_tiny: str
    """URL to tiny photo"""
    time_zone_identifier: str
    """User's timezone identifier"""
    title: str
    """User's job title"""
    url: str
    """User's Monday.com profile URL"""
    utc_hours_diff: str
    """UTC hours difference for the user's timezone"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    birthday: AirbyteSortOrder
    """User's birthday"""
    country_code: AirbyteSortOrder
    """User's country code"""
    created_at: AirbyteSortOrder
    """When the user was created"""
    email: AirbyteSortOrder
    """User's email address"""
    enabled: AirbyteSortOrder
    """Whether the user account is enabled"""
    id: AirbyteSortOrder
    """Unique user identifier"""
    is_admin: AirbyteSortOrder
    """Whether the user is an admin"""
    is_guest: AirbyteSortOrder
    """Whether the user is a guest"""
    is_pending: AirbyteSortOrder
    """Whether the user is pending"""
    is_view_only: AirbyteSortOrder
    """Whether the user is view-only"""
    is_verified: AirbyteSortOrder
    """Whether the user is verified"""
    join_date: AirbyteSortOrder
    """When the user joined"""
    location: AirbyteSortOrder
    """User's location"""
    mobile_phone: AirbyteSortOrder
    """User's mobile phone number"""
    name: AirbyteSortOrder
    """User's display name"""
    phone: AirbyteSortOrder
    """User's phone number"""
    photo_original: AirbyteSortOrder
    """URL to original size photo"""
    photo_small: AirbyteSortOrder
    """URL to small photo"""
    photo_thumb: AirbyteSortOrder
    """URL to thumbnail photo"""
    photo_thumb_small: AirbyteSortOrder
    """URL to small thumbnail photo"""
    photo_tiny: AirbyteSortOrder
    """URL to tiny photo"""
    time_zone_identifier: AirbyteSortOrder
    """User's timezone identifier"""
    title: AirbyteSortOrder
    """User's job title"""
    url: AirbyteSortOrder
    """User's Monday.com profile URL"""
    utc_hours_diff: AirbyteSortOrder
    """UTC hours difference for the user's timezone"""


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
    account_product: dict[str, Any] | None
    """Account product info"""
    created_at: str | None
    """When the workspace was created"""
    description: str | None
    """Workspace description"""
    id: str | None
    """Unique workspace identifier"""
    kind: str | None
    """Workspace kind (open, closed)"""
    name: str | None
    """Workspace name"""
    owners_subscribers: list[Any] | None
    """Owner subscribers"""
    settings: dict[str, Any] | None
    """Workspace settings"""
    state: str | None
    """Workspace state"""
    team_owners_subscribers: list[Any] | None
    """Team owner subscribers"""
    teams_subscribers: list[Any] | None
    """Team subscribers"""
    users_subscribers: list[Any] | None
    """User subscribers"""


class WorkspacesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    account_product: list[dict[str, Any]]
    """Account product info"""
    created_at: list[str]
    """When the workspace was created"""
    description: list[str]
    """Workspace description"""
    id: list[str]
    """Unique workspace identifier"""
    kind: list[str]
    """Workspace kind (open, closed)"""
    name: list[str]
    """Workspace name"""
    owners_subscribers: list[list[Any]]
    """Owner subscribers"""
    settings: list[dict[str, Any]]
    """Workspace settings"""
    state: list[str]
    """Workspace state"""
    team_owners_subscribers: list[list[Any]]
    """Team owner subscribers"""
    teams_subscribers: list[list[Any]]
    """Team subscribers"""
    users_subscribers: list[list[Any]]
    """User subscribers"""


class WorkspacesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    account_product: Any
    """Account product info"""
    created_at: Any
    """When the workspace was created"""
    description: Any
    """Workspace description"""
    id: Any
    """Unique workspace identifier"""
    kind: Any
    """Workspace kind (open, closed)"""
    name: Any
    """Workspace name"""
    owners_subscribers: Any
    """Owner subscribers"""
    settings: Any
    """Workspace settings"""
    state: Any
    """Workspace state"""
    team_owners_subscribers: Any
    """Team owner subscribers"""
    teams_subscribers: Any
    """Team subscribers"""
    users_subscribers: Any
    """User subscribers"""


class WorkspacesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    account_product: str
    """Account product info"""
    created_at: str
    """When the workspace was created"""
    description: str
    """Workspace description"""
    id: str
    """Unique workspace identifier"""
    kind: str
    """Workspace kind (open, closed)"""
    name: str
    """Workspace name"""
    owners_subscribers: str
    """Owner subscribers"""
    settings: str
    """Workspace settings"""
    state: str
    """Workspace state"""
    team_owners_subscribers: str
    """Team owner subscribers"""
    teams_subscribers: str
    """Team subscribers"""
    users_subscribers: str
    """User subscribers"""


class WorkspacesSortFilter(TypedDict, total=False):
    """Available fields for sorting workspaces search results."""
    account_product: AirbyteSortOrder
    """Account product info"""
    created_at: AirbyteSortOrder
    """When the workspace was created"""
    description: AirbyteSortOrder
    """Workspace description"""
    id: AirbyteSortOrder
    """Unique workspace identifier"""
    kind: AirbyteSortOrder
    """Workspace kind (open, closed)"""
    name: AirbyteSortOrder
    """Workspace name"""
    owners_subscribers: AirbyteSortOrder
    """Owner subscribers"""
    settings: AirbyteSortOrder
    """Workspace settings"""
    state: AirbyteSortOrder
    """Workspace state"""
    team_owners_subscribers: AirbyteSortOrder
    """Team owner subscribers"""
    teams_subscribers: AirbyteSortOrder
    """Team subscribers"""
    users_subscribers: AirbyteSortOrder
    """User subscribers"""


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
