"""
Pydantic models for notion connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class NotionAuthConfig(BaseModel):
    """API Token Authentication"""

    model_config = ConfigDict(extra="forbid")

    token: str
    """Notion internal integration token (starts with ntn_ or secret_)"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class UserBot(BaseModel):
    """Bot-specific data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    owner: Union[dict[str, Any] | None, Any] = Field(default=None, description="Bot owner information")
    """Bot owner information"""
    workspace_name: Union[str | None, Any] = Field(default=None, description="Name of the workspace the bot belongs to")
    """Name of the workspace the bot belongs to"""

class UserPerson(BaseModel):
    """Person-specific data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: Union[str | None, Any] = Field(default=None, description="Person's email address")
    """Person's email address"""

class User(BaseModel):
    """A Notion user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    avatar_url: Union[str | None, Any] = Field(default=None)
    person: Union[UserPerson | None, Any] = Field(default=None)
    bot: Union[UserBot | None, Any] = Field(default=None)
    request_id: Union[str | None, Any] = Field(default=None)

class UsersListResponse(BaseModel):
    """Paginated list of users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str | None, Any] = Field(default=None)
    results: Union[list[User], Any] = Field(default=None)
    next_cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    user: Union[dict[str, Any] | None, Any] = Field(default=None)
    request_id: Union[str | None, Any] = Field(default=None)

class RichTextAnnotations(BaseModel):
    """Text annotations (bold, italic, etc.)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: Union[bool | None, Any] = Field(default=None)
    italic: Union[bool | None, Any] = Field(default=None)
    strikethrough: Union[bool | None, Any] = Field(default=None)
    underline: Union[bool | None, Any] = Field(default=None)
    code: Union[bool | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)

class RichTextText(BaseModel):
    """Text content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: Union[str | None, Any] = Field(default=None, description="Plain text content")
    """Plain text content"""
    link: Union[dict[str, Any] | None, Any] = Field(default=None, description="Link object")
    """Link object"""

class RichText(BaseModel):
    """A rich text object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    text: Union[RichTextText | None, Any] = Field(default=None)
    annotations: Union[RichTextAnnotations | None, Any] = Field(default=None)
    plain_text: Union[str | None, Any] = Field(default=None)
    href: Union[str | None, Any] = Field(default=None)

class Parent(BaseModel):
    """Parent object reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    database_id: Union[str | None, Any] = Field(default=None)
    data_source_id: Union[str | None, Any] = Field(default=None)
    page_id: Union[str | None, Any] = Field(default=None)
    block_id: Union[str | None, Any] = Field(default=None)
    workspace: Union[bool | None, Any] = Field(default=None)

class PageLastEditedBy(BaseModel):
    """User who last edited the page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class PageCreatedBy(BaseModel):
    """User who created the page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class Page(BaseModel):
    """A Notion page object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str | None, Any] = Field(default=None)
    created_time: Union[str | None, Any] = Field(default=None)
    last_edited_time: Union[str | None, Any] = Field(default=None)
    created_by: Union[PageCreatedBy | None, Any] = Field(default=None)
    last_edited_by: Union[PageLastEditedBy | None, Any] = Field(default=None)
    cover: Union[dict[str, Any] | None, Any] = Field(default=None)
    icon: Union[dict[str, Any] | None, Any] = Field(default=None)
    parent: Union[Any, Any] = Field(default=None)
    archived: Union[bool | None, Any] = Field(default=None)
    in_trash: Union[bool | None, Any] = Field(default=None)
    is_locked: Union[bool | None, Any] = Field(default=None)
    properties: Union[dict[str, Any] | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)
    public_url: Union[str | None, Any] = Field(default=None)
    request_id: Union[str | None, Any] = Field(default=None)

class PagesListResponse(BaseModel):
    """Paginated list of pages"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str | None, Any] = Field(default=None)
    results: Union[list[Page], Any] = Field(default=None)
    next_cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    page_or_data_source: Union[dict[str, Any] | None, Any] = Field(default=None)
    request_id: Union[str | None, Any] = Field(default=None)

class DataSourceCreatedBy(BaseModel):
    """User who created the data source"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class DataSourceLastEditedBy(BaseModel):
    """User who last edited the data source"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class DataSource(BaseModel):
    """A Notion data source object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str | None, Any] = Field(default=None)
    created_time: Union[str | None, Any] = Field(default=None)
    last_edited_time: Union[str | None, Any] = Field(default=None)
    created_by: Union[DataSourceCreatedBy | None, Any] = Field(default=None)
    last_edited_by: Union[DataSourceLastEditedBy | None, Any] = Field(default=None)
    title: Union[list[RichText] | None, Any] = Field(default=None)
    description: Union[list[RichText] | None, Any] = Field(default=None)
    icon: Union[dict[str, Any] | None, Any] = Field(default=None)
    cover: Union[dict[str, Any] | None, Any] = Field(default=None)
    properties: Union[dict[str, Any] | None, Any] = Field(default=None)
    parent: Union[Any, Any] = Field(default=None)
    database_parent: Union[Any, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)
    public_url: Union[str | None, Any] = Field(default=None)
    archived: Union[bool | None, Any] = Field(default=None)
    in_trash: Union[bool | None, Any] = Field(default=None)
    is_inline: Union[bool | None, Any] = Field(default=None)
    is_locked: Union[bool | None, Any] = Field(default=None)
    request_id: Union[str | None, Any] = Field(default=None)

class DataSourcesListResponse(BaseModel):
    """Paginated list of data sources"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str | None, Any] = Field(default=None)
    results: Union[list[DataSource], Any] = Field(default=None)
    next_cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    page_or_data_source: Union[dict[str, Any] | None, Any] = Field(default=None)
    request_id: Union[str | None, Any] = Field(default=None)

class BlockTable(BaseModel):
    """Table block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    table_width: Union[int | None, Any] = Field(default=None)
    has_column_header: Union[bool | None, Any] = Field(default=None)
    has_row_header: Union[bool | None, Any] = Field(default=None)

class BlockCallout(BaseModel):
    """Callout block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: Union[list[RichText] | None, Any] = Field(default=None)
    icon: Union[dict[str, Any] | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)

class BlockTableRow(BaseModel):
    """Table row block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cells: Union[list[Any] | None, Any] = Field(default=None)

class BlockColumn(BaseModel):
    """Column block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    width_ratio: Union[float | None, Any] = Field(default=None)

class BlockQuote(BaseModel):
    """Quote block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: Union[list[RichText] | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)

class BlockLinkPreview(BaseModel):
    """Link preview block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: Union[str | None, Any] = Field(default=None)

class BlockBulletedListItem(BaseModel):
    """Bulleted list item content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: Union[list[RichText] | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)

class BlockCreatedBy(BaseModel):
    """User who created the block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class BlockLastEditedBy(BaseModel):
    """User who last edited the block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class BlockHeading3(BaseModel):
    """Heading 3 block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: Union[list[RichText] | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)
    is_toggleable: Union[bool | None, Any] = Field(default=None)

class BlockParagraph(BaseModel):
    """Paragraph block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: Union[list[RichText] | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)

class BlockHeading2(BaseModel):
    """Heading 2 block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: Union[list[RichText] | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)
    is_toggleable: Union[bool | None, Any] = Field(default=None)

class BlockTableOfContents(BaseModel):
    """Table of contents block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: Union[str | None, Any] = Field(default=None)

class BlockToDo(BaseModel):
    """To-do block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: Union[list[RichText] | None, Any] = Field(default=None)
    checked: Union[bool | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)

class BlockHeading1(BaseModel):
    """Heading 1 block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: Union[list[RichText] | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)
    is_toggleable: Union[bool | None, Any] = Field(default=None)

class BlockChildDatabase(BaseModel):
    """Child database block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: Union[str | None, Any] = Field(default=None)

class BlockChildPage(BaseModel):
    """Child page block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: Union[str | None, Any] = Field(default=None)

class BlockEmbed(BaseModel):
    """Embed block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: Union[str | None, Any] = Field(default=None)

class BlockBookmark(BaseModel):
    """Bookmark block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    caption: Union[list[RichText] | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)

class BlockToggle(BaseModel):
    """Toggle block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: Union[list[RichText] | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)

class BlockCode(BaseModel):
    """Code block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: Union[list[RichText] | None, Any] = Field(default=None)
    caption: Union[list[RichText] | None, Any] = Field(default=None)
    language: Union[str | None, Any] = Field(default=None)

class BlockNumberedListItem(BaseModel):
    """Numbered list item content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: Union[list[RichText] | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)

class BlockEquation(BaseModel):
    """Equation block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: Union[str | None, Any] = Field(default=None)

class Block(BaseModel):
    """A Notion block object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    created_time: Union[str | None, Any] = Field(default=None)
    last_edited_time: Union[str | None, Any] = Field(default=None)
    created_by: Union[BlockCreatedBy | None, Any] = Field(default=None)
    last_edited_by: Union[BlockLastEditedBy | None, Any] = Field(default=None)
    has_children: Union[bool | None, Any] = Field(default=None)
    archived: Union[bool | None, Any] = Field(default=None)
    in_trash: Union[bool | None, Any] = Field(default=None)
    parent: Union[Any, Any] = Field(default=None)
    paragraph: Union[BlockParagraph | None, Any] = Field(default=None)
    heading_1: Union[BlockHeading1 | None, Any] = Field(default=None)
    heading_2: Union[BlockHeading2 | None, Any] = Field(default=None)
    heading_3: Union[BlockHeading3 | None, Any] = Field(default=None)
    bulleted_list_item: Union[BlockBulletedListItem | None, Any] = Field(default=None)
    numbered_list_item: Union[BlockNumberedListItem | None, Any] = Field(default=None)
    to_do: Union[BlockToDo | None, Any] = Field(default=None)
    toggle: Union[BlockToggle | None, Any] = Field(default=None)
    code: Union[BlockCode | None, Any] = Field(default=None)
    child_page: Union[BlockChildPage | None, Any] = Field(default=None)
    child_database: Union[BlockChildDatabase | None, Any] = Field(default=None)
    callout: Union[BlockCallout | None, Any] = Field(default=None)
    quote: Union[BlockQuote | None, Any] = Field(default=None)
    divider: Union[dict[str, Any] | None, Any] = Field(default=None)
    table_of_contents: Union[BlockTableOfContents | None, Any] = Field(default=None)
    bookmark: Union[BlockBookmark | None, Any] = Field(default=None)
    image: Union[dict[str, Any] | None, Any] = Field(default=None)
    video: Union[dict[str, Any] | None, Any] = Field(default=None)
    file: Union[dict[str, Any] | None, Any] = Field(default=None)
    pdf: Union[dict[str, Any] | None, Any] = Field(default=None)
    embed: Union[BlockEmbed | None, Any] = Field(default=None)
    equation: Union[BlockEquation | None, Any] = Field(default=None)
    table: Union[BlockTable | None, Any] = Field(default=None)
    table_row: Union[BlockTableRow | None, Any] = Field(default=None)
    column: Union[BlockColumn | None, Any] = Field(default=None)
    column_list: Union[dict[str, Any] | None, Any] = Field(default=None)
    synced_block: Union[dict[str, Any] | None, Any] = Field(default=None)
    template: Union[dict[str, Any] | None, Any] = Field(default=None)
    link_preview: Union[BlockLinkPreview | None, Any] = Field(default=None)
    link_to_page: Union[dict[str, Any] | None, Any] = Field(default=None)
    breadcrumb: Union[dict[str, Any] | None, Any] = Field(default=None)
    unsupported: Union[dict[str, Any] | None, Any] = Field(default=None)
    request_id: Union[str | None, Any] = Field(default=None)

class BlocksListResponse(BaseModel):
    """Paginated list of blocks"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str | None, Any] = Field(default=None)
    results: Union[list[Block], Any] = Field(default=None)
    next_cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    block: Union[dict[str, Any] | None, Any] = Field(default=None)
    request_id: Union[str | None, Any] = Field(default=None)

class CommentCreatedBy(BaseModel):
    """User who created the comment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str | None, Any] = Field(default=None)
    id: Union[str | None, Any] = Field(default=None)

class Comment(BaseModel):
    """A Notion comment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    object: Union[str | None, Any] = Field(default=None)
    parent: Union[Any, Any] = Field(default=None)
    discussion_id: Union[str | None, Any] = Field(default=None)
    created_time: Union[str | None, Any] = Field(default=None)
    last_edited_time: Union[str | None, Any] = Field(default=None)
    created_by: Union[CommentCreatedBy | None, Any] = Field(default=None)
    rich_text: Union[list[RichText] | None, Any] = Field(default=None)

class CommentsListResponse(BaseModel):
    """Paginated list of comments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: Union[str | None, Any] = Field(default=None)
    results: Union[list[Comment], Any] = Field(default=None)
    next_cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    comment: Union[dict[str, Any] | None, Any] = Field(default=None)
    request_id: Union[str | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)

class PagesListResultMeta(BaseModel):
    """Metadata for pages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)

class DataSourcesListResultMeta(BaseModel):
    """Metadata for data_sources.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)

class BlocksListResultMeta(BaseModel):
    """Metadata for blocks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)

class CommentsListResultMeta(BaseModel):
    """Metadata for comments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool | None, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class NotionCheckResult(BaseModel):
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


class NotionExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class NotionExecuteResultWithMeta(NotionExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class PagesSearchData(BaseModel):
    """Search result data for pages entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Indicates whether the page is archived or not."""
    cover: dict[str, Any] | None = None
    """URL or reference to the page cover image."""
    created_by: dict[str, Any] | None = None
    """User ID or name of the creator of the page."""
    created_time: str | None = None
    """Date and time when the page was created."""
    icon: dict[str, Any] | None = None
    """URL or reference to the page icon."""
    id: str | None = None
    """Unique identifier of the page."""
    in_trash: bool | None = None
    """Indicates whether the page is in trash or not."""
    last_edited_by: dict[str, Any] | None = None
    """User ID or name of the last editor of the page."""
    last_edited_time: str | None = None
    """Date and time when the page was last edited."""
    object: dict[str, Any] | None = None
    """Type or category of the page object."""
    parent: dict[str, Any] | None = None
    """ID or reference to the parent page."""
    properties: list[Any] | None = None
    """Custom properties associated with the page."""
    public_url: str | None = None
    """Publicly accessible URL of the page."""
    url: str | None = None
    """URL of the page within the service."""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    avatar_url: str | None = None
    """URL of the user's avatar"""
    bot: dict[str, Any] | None = None
    """Bot-specific data"""
    id: str | None = None
    """Unique identifier for the user"""
    name: str | None = None
    """User's display name"""
    object: dict[str, Any] | None = None
    """Always user"""
    person: dict[str, Any] | None = None
    """Person-specific data"""
    type: dict[str, Any] | None = None
    """Type of user (person or bot)"""


class DataSourcesSearchData(BaseModel):
    """Search result data for data_sources entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Indicates if the data source is archived or not."""
    cover: dict[str, Any] | None = None
    """URL or reference to the cover image of the data source."""
    created_by: dict[str, Any] | None = None
    """The user who created the data source."""
    created_time: str | None = None
    """The timestamp when the data source was created."""
    database_parent: dict[str, Any] | None = None
    """The grandparent of the data source (parent of the database)."""
    description: list[Any] | None = None
    """Description text associated with the data source."""
    icon: dict[str, Any] | None = None
    """URL or reference to the icon of the data source."""
    id: str | None = None
    """Unique identifier of the data source."""
    is_inline: bool | None = None
    """Indicates if the data source is displayed inline."""
    last_edited_by: dict[str, Any] | None = None
    """The user who last edited the data source."""
    last_edited_time: str | None = None
    """The timestamp when the data source was last edited."""
    object: dict[str, Any] | None = None
    """The type of object (data_source)."""
    parent: dict[str, Any] | None = None
    """The parent database of the data source."""
    properties: list[Any] | None = None
    """Schema of properties for the data source."""
    public_url: str | None = None
    """Public URL to access the data source."""
    title: list[Any] | None = None
    """Title or name of the data source."""
    url: str | None = None
    """URL or reference to access the data source."""


class BlocksSearchData(BaseModel):
    """Search result data for blocks entity."""
    model_config = ConfigDict(extra="allow")

    archived: bool | None = None
    """Indicates if the block is archived or not."""
    bookmark: dict[str, Any] | None = None
    """Represents a bookmark within the block"""
    breadcrumb: dict[str, Any] | None = None
    """Represents a breadcrumb block."""
    bulleted_list_item: dict[str, Any] | None = None
    """Represents an item in a bulleted list."""
    callout: dict[str, Any] | None = None
    """Describes a callout message or content in the block"""
    child_database: dict[str, Any] | None = None
    """Represents a child database block."""
    child_page: dict[str, Any] | None = None
    """Represents a child page block."""
    code: dict[str, Any] | None = None
    """Contains code snippets or blocks in the block content"""
    column: dict[str, Any] | None = None
    """Represents a column block."""
    column_list: dict[str, Any] | None = None
    """Represents a list of columns."""
    created_by: dict[str, Any] | None = None
    """The user who created the block."""
    created_time: str | None = None
    """The timestamp when the block was created."""
    divider: dict[str, Any] | None = None
    """Represents a divider block."""
    embed: dict[str, Any] | None = None
    """Contains embedded content such as videos, tweets, etc."""
    equation: dict[str, Any] | None = None
    """Represents an equation or mathematical formula in the block"""
    file: dict[str, Any] | None = None
    """Represents a file block."""
    has_children: bool | None = None
    """Indicates if the block has children or not."""
    heading_1: dict[str, Any] | None = None
    """Represents a level 1 heading."""
    heading_2: dict[str, Any] | None = None
    """Represents a level 2 heading."""
    heading_3: dict[str, Any] | None = None
    """Represents a level 3 heading."""
    id: str | None = None
    """The unique identifier of the block."""
    image: dict[str, Any] | None = None
    """Represents an image block."""
    last_edited_by: dict[str, Any] | None = None
    """The user who last edited the block."""
    last_edited_time: str | None = None
    """The timestamp when the block was last edited."""
    link_preview: dict[str, Any] | None = None
    """Displays a preview of an external link within the block"""
    link_to_page: dict[str, Any] | None = None
    """Provides a link to another page within the block"""
    numbered_list_item: dict[str, Any] | None = None
    """Represents an item in a numbered list."""
    object: dict[str, Any] | None = None
    """Represents an object block."""
    paragraph: dict[str, Any] | None = None
    """Represents a paragraph block."""
    parent: dict[str, Any] | None = None
    """The parent block of the current block."""
    pdf: dict[str, Any] | None = None
    """Represents a PDF document block."""
    quote: dict[str, Any] | None = None
    """Represents a quote block."""
    synced_block: dict[str, Any] | None = None
    """Represents a block synced from another source"""
    table: dict[str, Any] | None = None
    """Represents a table within the block"""
    table_of_contents: dict[str, Any] | None = None
    """Contains information regarding the table of contents"""
    table_row: dict[str, Any] | None = None
    """Represents a row in a table within the block"""
    template: dict[str, Any] | None = None
    """Specifies a template used within the block"""
    to_do: dict[str, Any] | None = None
    """Represents a to-do list or task content"""
    toggle: dict[str, Any] | None = None
    """Represents a toggle block."""
    type: dict[str, Any] | None = None
    """The type of the block."""
    unsupported: dict[str, Any] | None = None
    """Represents an unsupported block."""
    video: dict[str, Any] | None = None
    """Represents a video block."""


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

PagesSearchResult = AirbyteSearchResult[PagesSearchData]
"""Search result type for pages entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""

DataSourcesSearchResult = AirbyteSearchResult[DataSourcesSearchData]
"""Search result type for data_sources entity."""

BlocksSearchResult = AirbyteSearchResult[BlocksSearchData]
"""Search result type for blocks entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

UsersListResult = NotionExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

PagesListResult = NotionExecuteResultWithMeta[list[Page], PagesListResultMeta]
"""Result type for pages.list operation with data and metadata."""

DataSourcesListResult = NotionExecuteResultWithMeta[list[DataSource], DataSourcesListResultMeta]
"""Result type for data_sources.list operation with data and metadata."""

BlocksListResult = NotionExecuteResultWithMeta[list[Block], BlocksListResultMeta]
"""Result type for blocks.list operation with data and metadata."""

CommentsListResult = NotionExecuteResultWithMeta[list[Comment], CommentsListResultMeta]
"""Result type for comments.list operation with data and metadata."""

