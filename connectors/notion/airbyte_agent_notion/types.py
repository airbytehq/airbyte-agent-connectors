"""
Type definitions for notion connector.
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

class PagesListParamsFilter(TypedDict):
    """Nested schema for PagesListParams.filter"""
    property: NotRequired[str]
    value: NotRequired[str]

class PagesListParamsSort(TypedDict):
    """Nested schema for PagesListParams.sort"""
    direction: NotRequired[str]
    timestamp: NotRequired[str]

class DataSourcesListParamsFilter(TypedDict):
    """Nested schema for DataSourcesListParams.filter"""
    property: NotRequired[str]
    value: NotRequired[str]

class DataSourcesListParamsSort(TypedDict):
    """Nested schema for DataSourcesListParams.sort"""
    direction: NotRequired[str]
    timestamp: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    start_cursor: NotRequired[str]
    page_size: NotRequired[int]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    user_id: str

class PagesListParams(TypedDict):
    """Parameters for pages.list operation"""
    filter: NotRequired[PagesListParamsFilter]
    sort: NotRequired[PagesListParamsSort]
    start_cursor: NotRequired[str]
    page_size: NotRequired[int]

class PagesGetParams(TypedDict):
    """Parameters for pages.get operation"""
    page_id: str

class DataSourcesListParams(TypedDict):
    """Parameters for data_sources.list operation"""
    filter: NotRequired[DataSourcesListParamsFilter]
    sort: NotRequired[DataSourcesListParamsSort]
    start_cursor: NotRequired[str]
    page_size: NotRequired[int]

class DataSourcesGetParams(TypedDict):
    """Parameters for data_sources.get operation"""
    data_source_id: str

class BlocksListParams(TypedDict):
    """Parameters for blocks.list operation"""
    block_id: str
    start_cursor: NotRequired[str]
    page_size: NotRequired[int]

class BlocksGetParams(TypedDict):
    """Parameters for blocks.get operation"""
    block_id: str

class CommentsListParams(TypedDict):
    """Parameters for comments.list operation"""
    block_id: str
    start_cursor: NotRequired[str]
    page_size: NotRequired[int]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== PAGES SEARCH TYPES =====

class PagesSearchFilter(TypedDict, total=False):
    """Available fields for filtering pages search queries."""
    archived: bool | None
    """Indicates whether the page is archived or not."""
    cover: dict[str, Any] | None
    """URL or reference to the page cover image."""
    created_by: dict[str, Any] | None
    """User ID or name of the creator of the page."""
    created_time: str | None
    """Date and time when the page was created."""
    icon: dict[str, Any] | None
    """URL or reference to the page icon."""
    id: str | None
    """Unique identifier of the page."""
    in_trash: bool | None
    """Indicates whether the page is in trash or not."""
    last_edited_by: dict[str, Any] | None
    """User ID or name of the last editor of the page."""
    last_edited_time: str | None
    """Date and time when the page was last edited."""
    object: dict[str, Any] | None
    """Type or category of the page object."""
    parent: dict[str, Any] | None
    """ID or reference to the parent page."""
    properties: list[Any] | None
    """Custom properties associated with the page."""
    public_url: str | None
    """Publicly accessible URL of the page."""
    url: str | None
    """URL of the page within the service."""


class PagesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates whether the page is archived or not."""
    cover: list[dict[str, Any]]
    """URL or reference to the page cover image."""
    created_by: list[dict[str, Any]]
    """User ID or name of the creator of the page."""
    created_time: list[str]
    """Date and time when the page was created."""
    icon: list[dict[str, Any]]
    """URL or reference to the page icon."""
    id: list[str]
    """Unique identifier of the page."""
    in_trash: list[bool]
    """Indicates whether the page is in trash or not."""
    last_edited_by: list[dict[str, Any]]
    """User ID or name of the last editor of the page."""
    last_edited_time: list[str]
    """Date and time when the page was last edited."""
    object: list[dict[str, Any]]
    """Type or category of the page object."""
    parent: list[dict[str, Any]]
    """ID or reference to the parent page."""
    properties: list[list[Any]]
    """Custom properties associated with the page."""
    public_url: list[str]
    """Publicly accessible URL of the page."""
    url: list[str]
    """URL of the page within the service."""


class PagesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates whether the page is archived or not."""
    cover: Any
    """URL or reference to the page cover image."""
    created_by: Any
    """User ID or name of the creator of the page."""
    created_time: Any
    """Date and time when the page was created."""
    icon: Any
    """URL or reference to the page icon."""
    id: Any
    """Unique identifier of the page."""
    in_trash: Any
    """Indicates whether the page is in trash or not."""
    last_edited_by: Any
    """User ID or name of the last editor of the page."""
    last_edited_time: Any
    """Date and time when the page was last edited."""
    object: Any
    """Type or category of the page object."""
    parent: Any
    """ID or reference to the parent page."""
    properties: Any
    """Custom properties associated with the page."""
    public_url: Any
    """Publicly accessible URL of the page."""
    url: Any
    """URL of the page within the service."""


class PagesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates whether the page is archived or not."""
    cover: str
    """URL or reference to the page cover image."""
    created_by: str
    """User ID or name of the creator of the page."""
    created_time: str
    """Date and time when the page was created."""
    icon: str
    """URL or reference to the page icon."""
    id: str
    """Unique identifier of the page."""
    in_trash: str
    """Indicates whether the page is in trash or not."""
    last_edited_by: str
    """User ID or name of the last editor of the page."""
    last_edited_time: str
    """Date and time when the page was last edited."""
    object: str
    """Type or category of the page object."""
    parent: str
    """ID or reference to the parent page."""
    properties: str
    """Custom properties associated with the page."""
    public_url: str
    """Publicly accessible URL of the page."""
    url: str
    """URL of the page within the service."""


class PagesSortFilter(TypedDict, total=False):
    """Available fields for sorting pages search results."""
    archived: AirbyteSortOrder
    """Indicates whether the page is archived or not."""
    cover: AirbyteSortOrder
    """URL or reference to the page cover image."""
    created_by: AirbyteSortOrder
    """User ID or name of the creator of the page."""
    created_time: AirbyteSortOrder
    """Date and time when the page was created."""
    icon: AirbyteSortOrder
    """URL or reference to the page icon."""
    id: AirbyteSortOrder
    """Unique identifier of the page."""
    in_trash: AirbyteSortOrder
    """Indicates whether the page is in trash or not."""
    last_edited_by: AirbyteSortOrder
    """User ID or name of the last editor of the page."""
    last_edited_time: AirbyteSortOrder
    """Date and time when the page was last edited."""
    object: AirbyteSortOrder
    """Type or category of the page object."""
    parent: AirbyteSortOrder
    """ID or reference to the parent page."""
    properties: AirbyteSortOrder
    """Custom properties associated with the page."""
    public_url: AirbyteSortOrder
    """Publicly accessible URL of the page."""
    url: AirbyteSortOrder
    """URL of the page within the service."""


# Entity-specific condition types for pages
class PagesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: PagesSearchFilter


class PagesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: PagesSearchFilter


class PagesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: PagesSearchFilter


class PagesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: PagesSearchFilter


class PagesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: PagesSearchFilter


class PagesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: PagesSearchFilter


class PagesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: PagesStringFilter


class PagesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: PagesStringFilter


class PagesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: PagesStringFilter


class PagesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: PagesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
PagesInCondition = TypedDict("PagesInCondition", {"in": PagesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

PagesNotCondition = TypedDict("PagesNotCondition", {"not": "PagesCondition"}, total=False)
"""Negates the nested condition."""

PagesAndCondition = TypedDict("PagesAndCondition", {"and": "list[PagesCondition]"}, total=False)
"""True if all nested conditions are true."""

PagesOrCondition = TypedDict("PagesOrCondition", {"or": "list[PagesCondition]"}, total=False)
"""True if any nested condition is true."""

PagesAnyCondition = TypedDict("PagesAnyCondition", {"any": PagesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all pages condition types
PagesCondition = (
    PagesEqCondition
    | PagesNeqCondition
    | PagesGtCondition
    | PagesGteCondition
    | PagesLtCondition
    | PagesLteCondition
    | PagesInCondition
    | PagesLikeCondition
    | PagesFuzzyCondition
    | PagesKeywordCondition
    | PagesContainsCondition
    | PagesNotCondition
    | PagesAndCondition
    | PagesOrCondition
    | PagesAnyCondition
)


class PagesSearchQuery(TypedDict, total=False):
    """Search query for pages entity."""
    filter: PagesCondition
    sort: list[PagesSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    avatar_url: str | None
    """URL of the user's avatar"""
    bot: dict[str, Any] | None
    """Bot-specific data"""
    id: str | None
    """Unique identifier for the user"""
    name: str | None
    """User's display name"""
    object: dict[str, Any] | None
    """Always user"""
    person: dict[str, Any] | None
    """Person-specific data"""
    type: dict[str, Any] | None
    """Type of user (person or bot)"""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    avatar_url: list[str]
    """URL of the user's avatar"""
    bot: list[dict[str, Any]]
    """Bot-specific data"""
    id: list[str]
    """Unique identifier for the user"""
    name: list[str]
    """User's display name"""
    object: list[dict[str, Any]]
    """Always user"""
    person: list[dict[str, Any]]
    """Person-specific data"""
    type: list[dict[str, Any]]
    """Type of user (person or bot)"""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    avatar_url: Any
    """URL of the user's avatar"""
    bot: Any
    """Bot-specific data"""
    id: Any
    """Unique identifier for the user"""
    name: Any
    """User's display name"""
    object: Any
    """Always user"""
    person: Any
    """Person-specific data"""
    type: Any
    """Type of user (person or bot)"""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    avatar_url: str
    """URL of the user's avatar"""
    bot: str
    """Bot-specific data"""
    id: str
    """Unique identifier for the user"""
    name: str
    """User's display name"""
    object: str
    """Always user"""
    person: str
    """Person-specific data"""
    type: str
    """Type of user (person or bot)"""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    avatar_url: AirbyteSortOrder
    """URL of the user's avatar"""
    bot: AirbyteSortOrder
    """Bot-specific data"""
    id: AirbyteSortOrder
    """Unique identifier for the user"""
    name: AirbyteSortOrder
    """User's display name"""
    object: AirbyteSortOrder
    """Always user"""
    person: AirbyteSortOrder
    """Person-specific data"""
    type: AirbyteSortOrder
    """Type of user (person or bot)"""


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


# ===== DATA_SOURCES SEARCH TYPES =====

class DataSourcesSearchFilter(TypedDict, total=False):
    """Available fields for filtering data_sources search queries."""
    archived: bool | None
    """Indicates if the data source is archived or not."""
    cover: dict[str, Any] | None
    """URL or reference to the cover image of the data source."""
    created_by: dict[str, Any] | None
    """The user who created the data source."""
    created_time: str | None
    """The timestamp when the data source was created."""
    database_parent: dict[str, Any] | None
    """The grandparent of the data source (parent of the database)."""
    description: list[Any] | None
    """Description text associated with the data source."""
    icon: dict[str, Any] | None
    """URL or reference to the icon of the data source."""
    id: str | None
    """Unique identifier of the data source."""
    is_inline: bool | None
    """Indicates if the data source is displayed inline."""
    last_edited_by: dict[str, Any] | None
    """The user who last edited the data source."""
    last_edited_time: str | None
    """The timestamp when the data source was last edited."""
    object: dict[str, Any] | None
    """The type of object (data_source)."""
    parent: dict[str, Any] | None
    """The parent database of the data source."""
    properties: list[Any] | None
    """Schema of properties for the data source."""
    public_url: str | None
    """Public URL to access the data source."""
    title: list[Any] | None
    """Title or name of the data source."""
    url: str | None
    """URL or reference to access the data source."""


class DataSourcesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates if the data source is archived or not."""
    cover: list[dict[str, Any]]
    """URL or reference to the cover image of the data source."""
    created_by: list[dict[str, Any]]
    """The user who created the data source."""
    created_time: list[str]
    """The timestamp when the data source was created."""
    database_parent: list[dict[str, Any]]
    """The grandparent of the data source (parent of the database)."""
    description: list[list[Any]]
    """Description text associated with the data source."""
    icon: list[dict[str, Any]]
    """URL or reference to the icon of the data source."""
    id: list[str]
    """Unique identifier of the data source."""
    is_inline: list[bool]
    """Indicates if the data source is displayed inline."""
    last_edited_by: list[dict[str, Any]]
    """The user who last edited the data source."""
    last_edited_time: list[str]
    """The timestamp when the data source was last edited."""
    object: list[dict[str, Any]]
    """The type of object (data_source)."""
    parent: list[dict[str, Any]]
    """The parent database of the data source."""
    properties: list[list[Any]]
    """Schema of properties for the data source."""
    public_url: list[str]
    """Public URL to access the data source."""
    title: list[list[Any]]
    """Title or name of the data source."""
    url: list[str]
    """URL or reference to access the data source."""


class DataSourcesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates if the data source is archived or not."""
    cover: Any
    """URL or reference to the cover image of the data source."""
    created_by: Any
    """The user who created the data source."""
    created_time: Any
    """The timestamp when the data source was created."""
    database_parent: Any
    """The grandparent of the data source (parent of the database)."""
    description: Any
    """Description text associated with the data source."""
    icon: Any
    """URL or reference to the icon of the data source."""
    id: Any
    """Unique identifier of the data source."""
    is_inline: Any
    """Indicates if the data source is displayed inline."""
    last_edited_by: Any
    """The user who last edited the data source."""
    last_edited_time: Any
    """The timestamp when the data source was last edited."""
    object: Any
    """The type of object (data_source)."""
    parent: Any
    """The parent database of the data source."""
    properties: Any
    """Schema of properties for the data source."""
    public_url: Any
    """Public URL to access the data source."""
    title: Any
    """Title or name of the data source."""
    url: Any
    """URL or reference to access the data source."""


class DataSourcesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates if the data source is archived or not."""
    cover: str
    """URL or reference to the cover image of the data source."""
    created_by: str
    """The user who created the data source."""
    created_time: str
    """The timestamp when the data source was created."""
    database_parent: str
    """The grandparent of the data source (parent of the database)."""
    description: str
    """Description text associated with the data source."""
    icon: str
    """URL or reference to the icon of the data source."""
    id: str
    """Unique identifier of the data source."""
    is_inline: str
    """Indicates if the data source is displayed inline."""
    last_edited_by: str
    """The user who last edited the data source."""
    last_edited_time: str
    """The timestamp when the data source was last edited."""
    object: str
    """The type of object (data_source)."""
    parent: str
    """The parent database of the data source."""
    properties: str
    """Schema of properties for the data source."""
    public_url: str
    """Public URL to access the data source."""
    title: str
    """Title or name of the data source."""
    url: str
    """URL or reference to access the data source."""


class DataSourcesSortFilter(TypedDict, total=False):
    """Available fields for sorting data_sources search results."""
    archived: AirbyteSortOrder
    """Indicates if the data source is archived or not."""
    cover: AirbyteSortOrder
    """URL or reference to the cover image of the data source."""
    created_by: AirbyteSortOrder
    """The user who created the data source."""
    created_time: AirbyteSortOrder
    """The timestamp when the data source was created."""
    database_parent: AirbyteSortOrder
    """The grandparent of the data source (parent of the database)."""
    description: AirbyteSortOrder
    """Description text associated with the data source."""
    icon: AirbyteSortOrder
    """URL or reference to the icon of the data source."""
    id: AirbyteSortOrder
    """Unique identifier of the data source."""
    is_inline: AirbyteSortOrder
    """Indicates if the data source is displayed inline."""
    last_edited_by: AirbyteSortOrder
    """The user who last edited the data source."""
    last_edited_time: AirbyteSortOrder
    """The timestamp when the data source was last edited."""
    object: AirbyteSortOrder
    """The type of object (data_source)."""
    parent: AirbyteSortOrder
    """The parent database of the data source."""
    properties: AirbyteSortOrder
    """Schema of properties for the data source."""
    public_url: AirbyteSortOrder
    """Public URL to access the data source."""
    title: AirbyteSortOrder
    """Title or name of the data source."""
    url: AirbyteSortOrder
    """URL or reference to access the data source."""


# Entity-specific condition types for data_sources
class DataSourcesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DataSourcesSearchFilter


class DataSourcesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DataSourcesSearchFilter


class DataSourcesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DataSourcesSearchFilter


class DataSourcesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DataSourcesSearchFilter


class DataSourcesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DataSourcesSearchFilter


class DataSourcesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DataSourcesSearchFilter


class DataSourcesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DataSourcesStringFilter


class DataSourcesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DataSourcesStringFilter


class DataSourcesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DataSourcesStringFilter


class DataSourcesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DataSourcesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DataSourcesInCondition = TypedDict("DataSourcesInCondition", {"in": DataSourcesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DataSourcesNotCondition = TypedDict("DataSourcesNotCondition", {"not": "DataSourcesCondition"}, total=False)
"""Negates the nested condition."""

DataSourcesAndCondition = TypedDict("DataSourcesAndCondition", {"and": "list[DataSourcesCondition]"}, total=False)
"""True if all nested conditions are true."""

DataSourcesOrCondition = TypedDict("DataSourcesOrCondition", {"or": "list[DataSourcesCondition]"}, total=False)
"""True if any nested condition is true."""

DataSourcesAnyCondition = TypedDict("DataSourcesAnyCondition", {"any": DataSourcesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all data_sources condition types
DataSourcesCondition = (
    DataSourcesEqCondition
    | DataSourcesNeqCondition
    | DataSourcesGtCondition
    | DataSourcesGteCondition
    | DataSourcesLtCondition
    | DataSourcesLteCondition
    | DataSourcesInCondition
    | DataSourcesLikeCondition
    | DataSourcesFuzzyCondition
    | DataSourcesKeywordCondition
    | DataSourcesContainsCondition
    | DataSourcesNotCondition
    | DataSourcesAndCondition
    | DataSourcesOrCondition
    | DataSourcesAnyCondition
)


class DataSourcesSearchQuery(TypedDict, total=False):
    """Search query for data_sources entity."""
    filter: DataSourcesCondition
    sort: list[DataSourcesSortFilter]


# ===== BLOCKS SEARCH TYPES =====

class BlocksSearchFilter(TypedDict, total=False):
    """Available fields for filtering blocks search queries."""
    archived: bool | None
    """Indicates if the block is archived or not."""
    bookmark: dict[str, Any] | None
    """Represents a bookmark within the block"""
    breadcrumb: dict[str, Any] | None
    """Represents a breadcrumb block."""
    bulleted_list_item: dict[str, Any] | None
    """Represents an item in a bulleted list."""
    callout: dict[str, Any] | None
    """Describes a callout message or content in the block"""
    child_database: dict[str, Any] | None
    """Represents a child database block."""
    child_page: dict[str, Any] | None
    """Represents a child page block."""
    code: dict[str, Any] | None
    """Contains code snippets or blocks in the block content"""
    column: dict[str, Any] | None
    """Represents a column block."""
    column_list: dict[str, Any] | None
    """Represents a list of columns."""
    created_by: dict[str, Any] | None
    """The user who created the block."""
    created_time: str | None
    """The timestamp when the block was created."""
    divider: dict[str, Any] | None
    """Represents a divider block."""
    embed: dict[str, Any] | None
    """Contains embedded content such as videos, tweets, etc."""
    equation: dict[str, Any] | None
    """Represents an equation or mathematical formula in the block"""
    file: dict[str, Any] | None
    """Represents a file block."""
    has_children: bool | None
    """Indicates if the block has children or not."""
    heading_1: dict[str, Any] | None
    """Represents a level 1 heading."""
    heading_2: dict[str, Any] | None
    """Represents a level 2 heading."""
    heading_3: dict[str, Any] | None
    """Represents a level 3 heading."""
    id: str | None
    """The unique identifier of the block."""
    image: dict[str, Any] | None
    """Represents an image block."""
    last_edited_by: dict[str, Any] | None
    """The user who last edited the block."""
    last_edited_time: str | None
    """The timestamp when the block was last edited."""
    link_preview: dict[str, Any] | None
    """Displays a preview of an external link within the block"""
    link_to_page: dict[str, Any] | None
    """Provides a link to another page within the block"""
    numbered_list_item: dict[str, Any] | None
    """Represents an item in a numbered list."""
    object: dict[str, Any] | None
    """Represents an object block."""
    paragraph: dict[str, Any] | None
    """Represents a paragraph block."""
    parent: dict[str, Any] | None
    """The parent block of the current block."""
    pdf: dict[str, Any] | None
    """Represents a PDF document block."""
    quote: dict[str, Any] | None
    """Represents a quote block."""
    synced_block: dict[str, Any] | None
    """Represents a block synced from another source"""
    table: dict[str, Any] | None
    """Represents a table within the block"""
    table_of_contents: dict[str, Any] | None
    """Contains information regarding the table of contents"""
    table_row: dict[str, Any] | None
    """Represents a row in a table within the block"""
    template: dict[str, Any] | None
    """Specifies a template used within the block"""
    to_do: dict[str, Any] | None
    """Represents a to-do list or task content"""
    toggle: dict[str, Any] | None
    """Represents a toggle block."""
    type: dict[str, Any] | None
    """The type of the block."""
    unsupported: dict[str, Any] | None
    """Represents an unsupported block."""
    video: dict[str, Any] | None
    """Represents a video block."""


class BlocksInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates if the block is archived or not."""
    bookmark: list[dict[str, Any]]
    """Represents a bookmark within the block"""
    breadcrumb: list[dict[str, Any]]
    """Represents a breadcrumb block."""
    bulleted_list_item: list[dict[str, Any]]
    """Represents an item in a bulleted list."""
    callout: list[dict[str, Any]]
    """Describes a callout message or content in the block"""
    child_database: list[dict[str, Any]]
    """Represents a child database block."""
    child_page: list[dict[str, Any]]
    """Represents a child page block."""
    code: list[dict[str, Any]]
    """Contains code snippets or blocks in the block content"""
    column: list[dict[str, Any]]
    """Represents a column block."""
    column_list: list[dict[str, Any]]
    """Represents a list of columns."""
    created_by: list[dict[str, Any]]
    """The user who created the block."""
    created_time: list[str]
    """The timestamp when the block was created."""
    divider: list[dict[str, Any]]
    """Represents a divider block."""
    embed: list[dict[str, Any]]
    """Contains embedded content such as videos, tweets, etc."""
    equation: list[dict[str, Any]]
    """Represents an equation or mathematical formula in the block"""
    file: list[dict[str, Any]]
    """Represents a file block."""
    has_children: list[bool]
    """Indicates if the block has children or not."""
    heading_1: list[dict[str, Any]]
    """Represents a level 1 heading."""
    heading_2: list[dict[str, Any]]
    """Represents a level 2 heading."""
    heading_3: list[dict[str, Any]]
    """Represents a level 3 heading."""
    id: list[str]
    """The unique identifier of the block."""
    image: list[dict[str, Any]]
    """Represents an image block."""
    last_edited_by: list[dict[str, Any]]
    """The user who last edited the block."""
    last_edited_time: list[str]
    """The timestamp when the block was last edited."""
    link_preview: list[dict[str, Any]]
    """Displays a preview of an external link within the block"""
    link_to_page: list[dict[str, Any]]
    """Provides a link to another page within the block"""
    numbered_list_item: list[dict[str, Any]]
    """Represents an item in a numbered list."""
    object: list[dict[str, Any]]
    """Represents an object block."""
    paragraph: list[dict[str, Any]]
    """Represents a paragraph block."""
    parent: list[dict[str, Any]]
    """The parent block of the current block."""
    pdf: list[dict[str, Any]]
    """Represents a PDF document block."""
    quote: list[dict[str, Any]]
    """Represents a quote block."""
    synced_block: list[dict[str, Any]]
    """Represents a block synced from another source"""
    table: list[dict[str, Any]]
    """Represents a table within the block"""
    table_of_contents: list[dict[str, Any]]
    """Contains information regarding the table of contents"""
    table_row: list[dict[str, Any]]
    """Represents a row in a table within the block"""
    template: list[dict[str, Any]]
    """Specifies a template used within the block"""
    to_do: list[dict[str, Any]]
    """Represents a to-do list or task content"""
    toggle: list[dict[str, Any]]
    """Represents a toggle block."""
    type: list[dict[str, Any]]
    """The type of the block."""
    unsupported: list[dict[str, Any]]
    """Represents an unsupported block."""
    video: list[dict[str, Any]]
    """Represents a video block."""


class BlocksAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates if the block is archived or not."""
    bookmark: Any
    """Represents a bookmark within the block"""
    breadcrumb: Any
    """Represents a breadcrumb block."""
    bulleted_list_item: Any
    """Represents an item in a bulleted list."""
    callout: Any
    """Describes a callout message or content in the block"""
    child_database: Any
    """Represents a child database block."""
    child_page: Any
    """Represents a child page block."""
    code: Any
    """Contains code snippets or blocks in the block content"""
    column: Any
    """Represents a column block."""
    column_list: Any
    """Represents a list of columns."""
    created_by: Any
    """The user who created the block."""
    created_time: Any
    """The timestamp when the block was created."""
    divider: Any
    """Represents a divider block."""
    embed: Any
    """Contains embedded content such as videos, tweets, etc."""
    equation: Any
    """Represents an equation or mathematical formula in the block"""
    file: Any
    """Represents a file block."""
    has_children: Any
    """Indicates if the block has children or not."""
    heading_1: Any
    """Represents a level 1 heading."""
    heading_2: Any
    """Represents a level 2 heading."""
    heading_3: Any
    """Represents a level 3 heading."""
    id: Any
    """The unique identifier of the block."""
    image: Any
    """Represents an image block."""
    last_edited_by: Any
    """The user who last edited the block."""
    last_edited_time: Any
    """The timestamp when the block was last edited."""
    link_preview: Any
    """Displays a preview of an external link within the block"""
    link_to_page: Any
    """Provides a link to another page within the block"""
    numbered_list_item: Any
    """Represents an item in a numbered list."""
    object: Any
    """Represents an object block."""
    paragraph: Any
    """Represents a paragraph block."""
    parent: Any
    """The parent block of the current block."""
    pdf: Any
    """Represents a PDF document block."""
    quote: Any
    """Represents a quote block."""
    synced_block: Any
    """Represents a block synced from another source"""
    table: Any
    """Represents a table within the block"""
    table_of_contents: Any
    """Contains information regarding the table of contents"""
    table_row: Any
    """Represents a row in a table within the block"""
    template: Any
    """Specifies a template used within the block"""
    to_do: Any
    """Represents a to-do list or task content"""
    toggle: Any
    """Represents a toggle block."""
    type: Any
    """The type of the block."""
    unsupported: Any
    """Represents an unsupported block."""
    video: Any
    """Represents a video block."""


class BlocksStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates if the block is archived or not."""
    bookmark: str
    """Represents a bookmark within the block"""
    breadcrumb: str
    """Represents a breadcrumb block."""
    bulleted_list_item: str
    """Represents an item in a bulleted list."""
    callout: str
    """Describes a callout message or content in the block"""
    child_database: str
    """Represents a child database block."""
    child_page: str
    """Represents a child page block."""
    code: str
    """Contains code snippets or blocks in the block content"""
    column: str
    """Represents a column block."""
    column_list: str
    """Represents a list of columns."""
    created_by: str
    """The user who created the block."""
    created_time: str
    """The timestamp when the block was created."""
    divider: str
    """Represents a divider block."""
    embed: str
    """Contains embedded content such as videos, tweets, etc."""
    equation: str
    """Represents an equation or mathematical formula in the block"""
    file: str
    """Represents a file block."""
    has_children: str
    """Indicates if the block has children or not."""
    heading_1: str
    """Represents a level 1 heading."""
    heading_2: str
    """Represents a level 2 heading."""
    heading_3: str
    """Represents a level 3 heading."""
    id: str
    """The unique identifier of the block."""
    image: str
    """Represents an image block."""
    last_edited_by: str
    """The user who last edited the block."""
    last_edited_time: str
    """The timestamp when the block was last edited."""
    link_preview: str
    """Displays a preview of an external link within the block"""
    link_to_page: str
    """Provides a link to another page within the block"""
    numbered_list_item: str
    """Represents an item in a numbered list."""
    object: str
    """Represents an object block."""
    paragraph: str
    """Represents a paragraph block."""
    parent: str
    """The parent block of the current block."""
    pdf: str
    """Represents a PDF document block."""
    quote: str
    """Represents a quote block."""
    synced_block: str
    """Represents a block synced from another source"""
    table: str
    """Represents a table within the block"""
    table_of_contents: str
    """Contains information regarding the table of contents"""
    table_row: str
    """Represents a row in a table within the block"""
    template: str
    """Specifies a template used within the block"""
    to_do: str
    """Represents a to-do list or task content"""
    toggle: str
    """Represents a toggle block."""
    type: str
    """The type of the block."""
    unsupported: str
    """Represents an unsupported block."""
    video: str
    """Represents a video block."""


class BlocksSortFilter(TypedDict, total=False):
    """Available fields for sorting blocks search results."""
    archived: AirbyteSortOrder
    """Indicates if the block is archived or not."""
    bookmark: AirbyteSortOrder
    """Represents a bookmark within the block"""
    breadcrumb: AirbyteSortOrder
    """Represents a breadcrumb block."""
    bulleted_list_item: AirbyteSortOrder
    """Represents an item in a bulleted list."""
    callout: AirbyteSortOrder
    """Describes a callout message or content in the block"""
    child_database: AirbyteSortOrder
    """Represents a child database block."""
    child_page: AirbyteSortOrder
    """Represents a child page block."""
    code: AirbyteSortOrder
    """Contains code snippets or blocks in the block content"""
    column: AirbyteSortOrder
    """Represents a column block."""
    column_list: AirbyteSortOrder
    """Represents a list of columns."""
    created_by: AirbyteSortOrder
    """The user who created the block."""
    created_time: AirbyteSortOrder
    """The timestamp when the block was created."""
    divider: AirbyteSortOrder
    """Represents a divider block."""
    embed: AirbyteSortOrder
    """Contains embedded content such as videos, tweets, etc."""
    equation: AirbyteSortOrder
    """Represents an equation or mathematical formula in the block"""
    file: AirbyteSortOrder
    """Represents a file block."""
    has_children: AirbyteSortOrder
    """Indicates if the block has children or not."""
    heading_1: AirbyteSortOrder
    """Represents a level 1 heading."""
    heading_2: AirbyteSortOrder
    """Represents a level 2 heading."""
    heading_3: AirbyteSortOrder
    """Represents a level 3 heading."""
    id: AirbyteSortOrder
    """The unique identifier of the block."""
    image: AirbyteSortOrder
    """Represents an image block."""
    last_edited_by: AirbyteSortOrder
    """The user who last edited the block."""
    last_edited_time: AirbyteSortOrder
    """The timestamp when the block was last edited."""
    link_preview: AirbyteSortOrder
    """Displays a preview of an external link within the block"""
    link_to_page: AirbyteSortOrder
    """Provides a link to another page within the block"""
    numbered_list_item: AirbyteSortOrder
    """Represents an item in a numbered list."""
    object: AirbyteSortOrder
    """Represents an object block."""
    paragraph: AirbyteSortOrder
    """Represents a paragraph block."""
    parent: AirbyteSortOrder
    """The parent block of the current block."""
    pdf: AirbyteSortOrder
    """Represents a PDF document block."""
    quote: AirbyteSortOrder
    """Represents a quote block."""
    synced_block: AirbyteSortOrder
    """Represents a block synced from another source"""
    table: AirbyteSortOrder
    """Represents a table within the block"""
    table_of_contents: AirbyteSortOrder
    """Contains information regarding the table of contents"""
    table_row: AirbyteSortOrder
    """Represents a row in a table within the block"""
    template: AirbyteSortOrder
    """Specifies a template used within the block"""
    to_do: AirbyteSortOrder
    """Represents a to-do list or task content"""
    toggle: AirbyteSortOrder
    """Represents a toggle block."""
    type: AirbyteSortOrder
    """The type of the block."""
    unsupported: AirbyteSortOrder
    """Represents an unsupported block."""
    video: AirbyteSortOrder
    """Represents a video block."""


# Entity-specific condition types for blocks
class BlocksEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: BlocksSearchFilter


class BlocksNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: BlocksSearchFilter


class BlocksGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: BlocksSearchFilter


class BlocksGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: BlocksSearchFilter


class BlocksLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: BlocksSearchFilter


class BlocksLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: BlocksSearchFilter


class BlocksLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: BlocksStringFilter


class BlocksFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: BlocksStringFilter


class BlocksKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: BlocksStringFilter


class BlocksContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: BlocksAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
BlocksInCondition = TypedDict("BlocksInCondition", {"in": BlocksInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

BlocksNotCondition = TypedDict("BlocksNotCondition", {"not": "BlocksCondition"}, total=False)
"""Negates the nested condition."""

BlocksAndCondition = TypedDict("BlocksAndCondition", {"and": "list[BlocksCondition]"}, total=False)
"""True if all nested conditions are true."""

BlocksOrCondition = TypedDict("BlocksOrCondition", {"or": "list[BlocksCondition]"}, total=False)
"""True if any nested condition is true."""

BlocksAnyCondition = TypedDict("BlocksAnyCondition", {"any": BlocksAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all blocks condition types
BlocksCondition = (
    BlocksEqCondition
    | BlocksNeqCondition
    | BlocksGtCondition
    | BlocksGteCondition
    | BlocksLtCondition
    | BlocksLteCondition
    | BlocksInCondition
    | BlocksLikeCondition
    | BlocksFuzzyCondition
    | BlocksKeywordCondition
    | BlocksContainsCondition
    | BlocksNotCondition
    | BlocksAndCondition
    | BlocksOrCondition
    | BlocksAnyCondition
)


class BlocksSearchQuery(TypedDict, total=False):
    """Search query for blocks entity."""
    filter: BlocksCondition
    sort: list[BlocksSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
