"""
Pydantic models for notion connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration - multiple options available

class NotionOauth20AuthConfig(BaseModel):
    """OAuth2.0"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """Your Notion OAuth integration's client ID"""
    client_secret: str
    """Your Notion OAuth integration's client secret"""
    access_token: str
    """OAuth access token obtained through the Notion authorization flow"""

class NotionAccessTokenAuthConfig(BaseModel):
    """Access Token"""

    model_config = ConfigDict(extra="forbid")

    token: str
    """Notion internal integration token (starts with ntn_ or secret_)"""

NotionAuthConfig = NotionOauth20AuthConfig | NotionAccessTokenAuthConfig

# OAuth credential override

class NotionOAuthCredentials(BaseModel):
    """Notion OAuth App Credentials - Provide your own Notion OAuth app credentials to override the default Airbyte-managed ones."""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """Your Notion OAuth integration's client ID"""
    client_secret: str
    """Your Notion OAuth integration's client secret"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class UserBot(BaseModel):
    """Bot-specific data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    owner: dict[str, Any] | None | None = Field(default=None, description="Bot owner information")
    """Bot owner information"""
    workspace_name: str | None | None = Field(default=None, description="Name of the workspace the bot belongs to")
    """Name of the workspace the bot belongs to"""

class UserPerson(BaseModel):
    """Person-specific data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None | None = Field(default=None, description="Person's email address")
    """Person's email address"""

class User(BaseModel):
    """A Notion user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    object_: str | None = Field(default=None, alias="object")
    type_: str | None = Field(default=None, alias="type")
    name: str | None = Field(default=None)
    avatar_url: str | None = Field(default=None)
    person: UserPerson | None = Field(default=None)
    bot: UserBot | None = Field(default=None)
    request_id: str | None = Field(default=None)

class UsersListResponse(BaseModel):
    """Paginated list of users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_: str | None = Field(default=None, alias="object")
    results: list[User] | None = Field(default=None)
    next_cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    user: dict[str, Any] | None = Field(default=None)
    request_id: str | None = Field(default=None)

class RichTextText(BaseModel):
    """Text content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None | None = Field(default=None, description="Plain text content")
    """Plain text content"""
    link: dict[str, Any] | None | None = Field(default=None, description="Link object")
    """Link object"""

class RichTextAnnotations(BaseModel):
    """Text annotations (bold, italic, etc.)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None | None = Field(default=None)
    italic: bool | None | None = Field(default=None)
    strikethrough: bool | None | None = Field(default=None)
    underline: bool | None | None = Field(default=None)
    code: bool | None | None = Field(default=None)
    color: str | None | None = Field(default=None)

class RichText(BaseModel):
    """A rich text object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: RichTextText | None = Field(default=None)
    annotations: RichTextAnnotations | None = Field(default=None)
    plain_text: str | None = Field(default=None)
    href: str | None = Field(default=None)

class Parent(BaseModel):
    """Parent object reference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    database_id: str | None = Field(default=None)
    data_source_id: str | None = Field(default=None)
    page_id: str | None = Field(default=None)
    block_id: str | None = Field(default=None)
    workspace: bool | None = Field(default=None)

class PageCreatedBy(BaseModel):
    """User who created the page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_: str | None | None = Field(default=None, alias="object")
    id: str | None | None = Field(default=None)

class PageLastEditedBy(BaseModel):
    """User who last edited the page"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_: str | None | None = Field(default=None, alias="object")
    id: str | None | None = Field(default=None)

class Page(BaseModel):
    """A Notion page object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    object_: str | None = Field(default=None, alias="object")
    created_time: str | None = Field(default=None)
    last_edited_time: str | None = Field(default=None)
    created_by: PageCreatedBy | None = Field(default=None)
    last_edited_by: PageLastEditedBy | None = Field(default=None)
    cover: dict[str, Any] | None = Field(default=None)
    icon: dict[str, Any] | None = Field(default=None)
    parent: Any | None = Field(default=None)
    archived: bool | None = Field(default=None)
    in_trash: bool | None = Field(default=None)
    is_archived: bool | None = Field(default=None)
    is_locked: bool | None = Field(default=None)
    properties: dict[str, Any] | None = Field(default=None)
    url: str | None = Field(default=None)
    public_url: str | None = Field(default=None)
    request_id: str | None = Field(default=None)

class PagesListResponse(BaseModel):
    """Paginated list of pages"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_: str | None = Field(default=None, alias="object")
    results: list[Page] | None = Field(default=None)
    next_cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    page_or_data_source: dict[str, Any] | None = Field(default=None)
    request_id: str | None = Field(default=None)

class DataSourceLastEditedBy(BaseModel):
    """User who last edited the data source"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_: str | None | None = Field(default=None, alias="object")
    id: str | None | None = Field(default=None)

class DataSourceCreatedBy(BaseModel):
    """User who created the data source"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_: str | None | None = Field(default=None, alias="object")
    id: str | None | None = Field(default=None)

class DataSource(BaseModel):
    """A Notion data source object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    object_: str | None = Field(default=None, alias="object")
    created_time: str | None = Field(default=None)
    last_edited_time: str | None = Field(default=None)
    created_by: DataSourceCreatedBy | None = Field(default=None)
    last_edited_by: DataSourceLastEditedBy | None = Field(default=None)
    title: list[RichText] | None = Field(default=None)
    description: list[RichText] | None = Field(default=None)
    icon: dict[str, Any] | None = Field(default=None)
    cover: dict[str, Any] | None = Field(default=None)
    properties: dict[str, Any] | None = Field(default=None)
    parent: Any | None = Field(default=None)
    database_parent: Any | None = Field(default=None)
    url: str | None = Field(default=None)
    public_url: str | None = Field(default=None)
    archived: bool | None = Field(default=None)
    in_trash: bool | None = Field(default=None)
    is_archived: bool | None = Field(default=None)
    is_inline: bool | None = Field(default=None)
    is_locked: bool | None = Field(default=None)
    request_id: str | None = Field(default=None)

class DataSourcesListResponse(BaseModel):
    """Paginated list of data sources"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_: str | None = Field(default=None, alias="object")
    results: list[DataSource] | None = Field(default=None)
    next_cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    page_or_data_source: dict[str, Any] | None = Field(default=None)
    request_id: str | None = Field(default=None)

class BlockColumn(BaseModel):
    """Column block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    width_ratio: float | None | None = Field(default=None)

class BlockCreatedBy(BaseModel):
    """User who created the block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_: str | None | None = Field(default=None, alias="object")
    id: str | None | None = Field(default=None)

class BlockBulletedListItem(BaseModel):
    """Bulleted list item content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[RichText] | None | None = Field(default=None)
    color: str | None | None = Field(default=None)

class BlockLinkPreview(BaseModel):
    """Link preview block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None | None = Field(default=None)

class BlockTableRow(BaseModel):
    """Table row block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cells: list[Any] | None | None = Field(default=None)

class BlockLastEditedBy(BaseModel):
    """User who last edited the block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_: str | None | None = Field(default=None, alias="object")
    id: str | None | None = Field(default=None)

class BlockChildDatabase(BaseModel):
    """Child database block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None | None = Field(default=None)

class BlockEmbed(BaseModel):
    """Embed block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None | None = Field(default=None)

class BlockHeading2(BaseModel):
    """Heading 2 block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[RichText] | None | None = Field(default=None)
    color: str | None | None = Field(default=None)
    is_toggleable: bool | None | None = Field(default=None)

class BlockHeading1(BaseModel):
    """Heading 1 block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[RichText] | None | None = Field(default=None)
    color: str | None | None = Field(default=None)
    is_toggleable: bool | None | None = Field(default=None)

class BlockToggle(BaseModel):
    """Toggle block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[RichText] | None | None = Field(default=None)
    color: str | None | None = Field(default=None)

class BlockTable(BaseModel):
    """Table block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    table_width: int | None | None = Field(default=None)
    has_column_header: bool | None | None = Field(default=None)
    has_row_header: bool | None | None = Field(default=None)

class BlockHeading3(BaseModel):
    """Heading 3 block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[RichText] | None | None = Field(default=None)
    color: str | None | None = Field(default=None)
    is_toggleable: bool | None | None = Field(default=None)

class BlockBookmark(BaseModel):
    """Bookmark block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    caption: list[RichText] | None | None = Field(default=None)
    url: str | None | None = Field(default=None)

class BlockCallout(BaseModel):
    """Callout block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[RichText] | None | None = Field(default=None)
    icon: dict[str, Any] | None | None = Field(default=None)
    color: str | None | None = Field(default=None)

class BlockEquation(BaseModel):
    """Equation block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None | None = Field(default=None)

class BlockParagraph(BaseModel):
    """Paragraph block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[RichText] | None | None = Field(default=None)
    color: str | None | None = Field(default=None)

class BlockToDo(BaseModel):
    """To-do block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[RichText] | None | None = Field(default=None)
    checked: bool | None | None = Field(default=None)
    color: str | None | None = Field(default=None)

class BlockCode(BaseModel):
    """Code block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[RichText] | None | None = Field(default=None)
    caption: list[RichText] | None | None = Field(default=None)
    language: str | None | None = Field(default=None)

class BlockTableOfContents(BaseModel):
    """Table of contents block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str | None | None = Field(default=None)

class BlockNumberedListItem(BaseModel):
    """Numbered list item content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[RichText] | None | None = Field(default=None)
    color: str | None | None = Field(default=None)

class BlockChildPage(BaseModel):
    """Child page block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None | None = Field(default=None)

class BlockQuote(BaseModel):
    """Quote block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[RichText] | None | None = Field(default=None)
    color: str | None | None = Field(default=None)

class Block(BaseModel):
    """A Notion block object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    object_: str | None = Field(default=None, alias="object")
    type_: str | None = Field(default=None, alias="type")
    created_time: str | None = Field(default=None)
    last_edited_time: str | None = Field(default=None)
    created_by: BlockCreatedBy | None = Field(default=None)
    last_edited_by: BlockLastEditedBy | None = Field(default=None)
    has_children: bool | None = Field(default=None)
    archived: bool | None = Field(default=None)
    in_trash: bool | None = Field(default=None)
    parent: Any | None = Field(default=None)
    paragraph: BlockParagraph | None = Field(default=None)
    heading_1: BlockHeading1 | None = Field(default=None)
    heading_2: BlockHeading2 | None = Field(default=None)
    heading_3: BlockHeading3 | None = Field(default=None)
    bulleted_list_item: BlockBulletedListItem | None = Field(default=None)
    numbered_list_item: BlockNumberedListItem | None = Field(default=None)
    to_do: BlockToDo | None = Field(default=None)
    toggle: BlockToggle | None = Field(default=None)
    code: BlockCode | None = Field(default=None)
    child_page: BlockChildPage | None = Field(default=None)
    child_database: BlockChildDatabase | None = Field(default=None)
    callout: BlockCallout | None = Field(default=None)
    quote: BlockQuote | None = Field(default=None)
    divider: dict[str, Any] | None = Field(default=None)
    table_of_contents: BlockTableOfContents | None = Field(default=None)
    bookmark: BlockBookmark | None = Field(default=None)
    image: dict[str, Any] | None = Field(default=None)
    video: dict[str, Any] | None = Field(default=None)
    file: dict[str, Any] | None = Field(default=None)
    pdf: dict[str, Any] | None = Field(default=None)
    embed: BlockEmbed | None = Field(default=None)
    equation: BlockEquation | None = Field(default=None)
    table: BlockTable | None = Field(default=None)
    table_row: BlockTableRow | None = Field(default=None)
    column: BlockColumn | None = Field(default=None)
    column_list: dict[str, Any] | None = Field(default=None)
    synced_block: dict[str, Any] | None = Field(default=None)
    template: dict[str, Any] | None = Field(default=None)
    link_preview: BlockLinkPreview | None = Field(default=None)
    link_to_page: dict[str, Any] | None = Field(default=None)
    breadcrumb: dict[str, Any] | None = Field(default=None)
    unsupported: dict[str, Any] | None = Field(default=None)
    request_id: str | None = Field(default=None)

class BlocksListResponse(BaseModel):
    """Paginated list of blocks"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_: str | None = Field(default=None, alias="object")
    results: list[Block] | None = Field(default=None)
    next_cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    block: dict[str, Any] | None = Field(default=None)
    request_id: str | None = Field(default=None)

class CommentCreatedBy(BaseModel):
    """User who created the comment"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_: str | None | None = Field(default=None, alias="object")
    id: str | None | None = Field(default=None)

class Comment(BaseModel):
    """A Notion comment object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    object_: str | None = Field(default=None, alias="object")
    parent: Any | None = Field(default=None)
    discussion_id: str | None = Field(default=None)
    created_time: str | None = Field(default=None)
    last_edited_time: str | None = Field(default=None)
    created_by: CommentCreatedBy | None = Field(default=None)
    rich_text: list[RichText] | None = Field(default=None)

class CommentsListResponse(BaseModel):
    """Paginated list of comments"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_: str | None = Field(default=None, alias="object")
    results: list[Comment] | None = Field(default=None)
    next_cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    comment: dict[str, Any] | None = Field(default=None)
    request_id: str | None = Field(default=None)

class PageCreateParamsIconIcon(BaseModel):
    """Notion native icon (when type is icon)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    color: str | None = Field(default=None)

class PageCreateParamsIconCustomEmoji(BaseModel):
    """Custom emoji icon (when type is custom_emoji)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class PageCreateParamsIconFileUpload(BaseModel):
    """Uploaded file icon (when type is file_upload)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class PageCreateParamsIconExternal(BaseModel):
    """External URL icon (when type is external)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class PageCreateParamsIcon(BaseModel):
    """Icon. Supports emoji, external URL, file upload, custom emoji, and Notion native icons. Set to null to remove."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="Icon type: emoji, external, file_upload, custom_emoji, or icon")
    """Icon type: emoji, external, file_upload, custom_emoji, or icon"""
    emoji: str | None = Field(default=None, description="Emoji character (when type is emoji)")
    """Emoji character (when type is emoji)"""
    external: PageCreateParamsIconExternal | None = Field(default=None, description="External URL icon (when type is external)")
    """External URL icon (when type is external)"""
    file_upload: PageCreateParamsIconFileUpload | None = Field(default=None, description="Uploaded file icon (when type is file_upload)")
    """Uploaded file icon (when type is file_upload)"""
    custom_emoji: PageCreateParamsIconCustomEmoji | None = Field(default=None, description="Custom emoji icon (when type is custom_emoji)")
    """Custom emoji icon (when type is custom_emoji)"""
    icon: PageCreateParamsIconIcon | None = Field(default=None, description="Notion native icon (when type is icon)")
    """Notion native icon (when type is icon)"""

class PageCreateParamsCoverFileUpload(BaseModel):
    """Uploaded file cover"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class PageCreateParamsCoverExternal(BaseModel):
    """External URL cover"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class PageCreateParamsCover(BaseModel):
    """Cover image. Supports external URL or file upload. Set to null to remove."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="Cover type: external or file_upload")
    """Cover type: external or file_upload"""
    external: PageCreateParamsCoverExternal | None = Field(default=None, description="External URL cover")
    """External URL cover"""
    file_upload: PageCreateParamsCoverFileUpload | None = Field(default=None, description="Uploaded file cover")
    """Uploaded file cover"""

class PageCreateParams(BaseModel):
    """Parameters for creating a new page as a child of an existing page, data source, or at the workspace level."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    parent: dict[str, Any]
    properties: dict[str, Any] | None = Field(default=None)
    children: list[dict[str, Any]] | None = Field(default=None)
    icon: PageCreateParamsIcon | None = Field(default=None)
    cover: PageCreateParamsCover | None = Field(default=None)

class PageUpdateParamsIconIcon(BaseModel):
    """Notion native icon (when type is icon)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    color: str | None = Field(default=None)

class PageUpdateParamsIconExternal(BaseModel):
    """External URL icon (when type is external)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class PageUpdateParamsIconFileUpload(BaseModel):
    """Uploaded file icon (when type is file_upload)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class PageUpdateParamsIconCustomEmoji(BaseModel):
    """Custom emoji icon (when type is custom_emoji)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class PageUpdateParamsIcon(BaseModel):
    """Icon. Supports emoji, external URL, file upload, custom emoji, and Notion native icons. Set to null to remove."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="Icon type: emoji, external, file_upload, custom_emoji, or icon")
    """Icon type: emoji, external, file_upload, custom_emoji, or icon"""
    emoji: str | None = Field(default=None, description="Emoji character (when type is emoji)")
    """Emoji character (when type is emoji)"""
    external: PageUpdateParamsIconExternal | None = Field(default=None, description="External URL icon (when type is external)")
    """External URL icon (when type is external)"""
    file_upload: PageUpdateParamsIconFileUpload | None = Field(default=None, description="Uploaded file icon (when type is file_upload)")
    """Uploaded file icon (when type is file_upload)"""
    custom_emoji: PageUpdateParamsIconCustomEmoji | None = Field(default=None, description="Custom emoji icon (when type is custom_emoji)")
    """Custom emoji icon (when type is custom_emoji)"""
    icon: PageUpdateParamsIconIcon | None = Field(default=None, description="Notion native icon (when type is icon)")
    """Notion native icon (when type is icon)"""

class PageUpdateParamsCoverFileUpload(BaseModel):
    """Uploaded file cover"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class PageUpdateParamsCoverExternal(BaseModel):
    """External URL cover"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class PageUpdateParamsCover(BaseModel):
    """Cover image. Supports external URL or file upload. Set to null to remove."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="Cover type: external or file_upload")
    """Cover type: external or file_upload"""
    external: PageUpdateParamsCoverExternal | None = Field(default=None, description="External URL cover")
    """External URL cover"""
    file_upload: PageUpdateParamsCoverFileUpload | None = Field(default=None, description="Uploaded file cover")
    """Uploaded file cover"""

class PageUpdateParams(BaseModel):
    """Parameters for updating a page. All fields are optional for partial updates."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    properties: dict[str, Any] | None = Field(default=None)
    icon: PageUpdateParamsIcon | None = Field(default=None)
    cover: PageUpdateParamsCover | None = Field(default=None)
    archived: bool | None = Field(default=None)
    in_trash: bool | None = Field(default=None)

class BlockCreateParamsChildrenItemToggleRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemToggleRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemToggleRichTextItemTextLink(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemToggleRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemToggleRichTextItemText(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemToggleRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockCreateParamsChildrenItemToggleRichTextItemTextLink | None | None = Field(default=None)

class BlockCreateParamsChildrenItemToggleRichTextItemEquation(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemToggleRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockCreateParamsChildrenItemToggleRichTextItem(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemToggle.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockCreateParamsChildrenItemToggleRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockCreateParamsChildrenItemToggleRichTextItemEquation | None = Field(default=None)
    annotations: BlockCreateParamsChildrenItemToggleRichTextItemAnnotations | None = Field(default=None)

class BlockCreateParamsChildrenItemToggle(BaseModel):
    """Toggle block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockCreateParamsChildrenItemToggleRichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemPdfExternal(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemPdf.external"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemPdfFileUpload(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemPdf.file_upload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class BlockCreateParamsChildrenItemPdf(BaseModel):
    """Media file. Use external URL or file upload."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="File type: external or file_upload")
    """File type: external or file_upload"""
    external: BlockCreateParamsChildrenItemPdfExternal | None = Field(default=None)
    file_upload: BlockCreateParamsChildrenItemPdfFileUpload | None = Field(default=None)

class BlockCreateParamsChildrenItemNumberedListItemRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemNumberedListItemRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemNumberedListItemRichTextItemEquation(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemNumberedListItemRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockCreateParamsChildrenItemNumberedListItemRichTextItemTextLink(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemNumberedListItemRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemNumberedListItemRichTextItemText(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemNumberedListItemRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockCreateParamsChildrenItemNumberedListItemRichTextItemTextLink | None | None = Field(default=None)

class BlockCreateParamsChildrenItemNumberedListItemRichTextItem(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemNumberedListItem.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockCreateParamsChildrenItemNumberedListItemRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockCreateParamsChildrenItemNumberedListItemRichTextItemEquation | None = Field(default=None)
    annotations: BlockCreateParamsChildrenItemNumberedListItemRichTextItemAnnotations | None = Field(default=None)

class BlockCreateParamsChildrenItemNumberedListItem(BaseModel):
    """Numbered list item content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockCreateParamsChildrenItemNumberedListItemRichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading1RichTextItemEquation(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading1RichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading1RichTextItemTextLink(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading1RichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading1RichTextItemText(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading1RichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockCreateParamsChildrenItemHeading1RichTextItemTextLink | None | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading1RichTextItemAnnotations(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading1RichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading1RichTextItem(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading1.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockCreateParamsChildrenItemHeading1RichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockCreateParamsChildrenItemHeading1RichTextItemEquation | None = Field(default=None)
    annotations: BlockCreateParamsChildrenItemHeading1RichTextItemAnnotations | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading1(BaseModel):
    """Heading 1 block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockCreateParamsChildrenItemHeading1RichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)
    is_toggleable: bool | None = Field(default=None)

class BlockCreateParamsChildrenItemCalloutRichTextItemEquation(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemCalloutRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockCreateParamsChildrenItemCalloutRichTextItemTextLink(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemCalloutRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemCalloutRichTextItemText(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemCalloutRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockCreateParamsChildrenItemCalloutRichTextItemTextLink | None | None = Field(default=None)

class BlockCreateParamsChildrenItemCalloutRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemCalloutRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemCalloutRichTextItem(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemCallout.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockCreateParamsChildrenItemCalloutRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockCreateParamsChildrenItemCalloutRichTextItemEquation | None = Field(default=None)
    annotations: BlockCreateParamsChildrenItemCalloutRichTextItemAnnotations | None = Field(default=None)

class BlockCreateParamsChildrenItemCallout(BaseModel):
    """Callout block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockCreateParamsChildrenItemCalloutRichTextItem] | None = Field(default=None)
    icon: dict[str, Any] | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemImageExternal(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemImage.external"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemImageFileUpload(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemImage.file_upload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class BlockCreateParamsChildrenItemImage(BaseModel):
    """Media file. Use external URL or file upload."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="File type: external or file_upload")
    """File type: external or file_upload"""
    external: BlockCreateParamsChildrenItemImageExternal | None = Field(default=None)
    file_upload: BlockCreateParamsChildrenItemImageFileUpload | None = Field(default=None)

class BlockCreateParamsChildrenItemParagraphRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemParagraphRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemParagraphRichTextItemEquation(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemParagraphRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockCreateParamsChildrenItemParagraphRichTextItemTextLink(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemParagraphRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemParagraphRichTextItemText(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemParagraphRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockCreateParamsChildrenItemParagraphRichTextItemTextLink | None | None = Field(default=None)

class BlockCreateParamsChildrenItemParagraphRichTextItem(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemParagraph.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockCreateParamsChildrenItemParagraphRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockCreateParamsChildrenItemParagraphRichTextItemEquation | None = Field(default=None)
    annotations: BlockCreateParamsChildrenItemParagraphRichTextItemAnnotations | None = Field(default=None)

class BlockCreateParamsChildrenItemParagraph(BaseModel):
    """Paragraph block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockCreateParamsChildrenItemParagraphRichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading2RichTextItemEquation(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading2RichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading2RichTextItemTextLink(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading2RichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading2RichTextItemText(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading2RichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockCreateParamsChildrenItemHeading2RichTextItemTextLink | None | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading2RichTextItemAnnotations(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading2RichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading2RichTextItem(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading2.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockCreateParamsChildrenItemHeading2RichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockCreateParamsChildrenItemHeading2RichTextItemEquation | None = Field(default=None)
    annotations: BlockCreateParamsChildrenItemHeading2RichTextItemAnnotations | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading2(BaseModel):
    """Heading 2 block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockCreateParamsChildrenItemHeading2RichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)
    is_toggleable: bool | None = Field(default=None)

class BlockCreateParamsChildrenItemQuoteRichTextItemTextLink(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemQuoteRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemQuoteRichTextItemText(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemQuoteRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockCreateParamsChildrenItemQuoteRichTextItemTextLink | None | None = Field(default=None)

class BlockCreateParamsChildrenItemQuoteRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemQuoteRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemQuoteRichTextItemEquation(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemQuoteRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockCreateParamsChildrenItemQuoteRichTextItem(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemQuote.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockCreateParamsChildrenItemQuoteRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockCreateParamsChildrenItemQuoteRichTextItemEquation | None = Field(default=None)
    annotations: BlockCreateParamsChildrenItemQuoteRichTextItemAnnotations | None = Field(default=None)

class BlockCreateParamsChildrenItemQuote(BaseModel):
    """Quote block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockCreateParamsChildrenItemQuoteRichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemBulletedListItemRichTextItemTextLink(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemBulletedListItemRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemBulletedListItemRichTextItemText(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemBulletedListItemRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockCreateParamsChildrenItemBulletedListItemRichTextItemTextLink | None | None = Field(default=None)

class BlockCreateParamsChildrenItemBulletedListItemRichTextItemEquation(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemBulletedListItemRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockCreateParamsChildrenItemBulletedListItemRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemBulletedListItemRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemBulletedListItemRichTextItem(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemBulletedListItem.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockCreateParamsChildrenItemBulletedListItemRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockCreateParamsChildrenItemBulletedListItemRichTextItemEquation | None = Field(default=None)
    annotations: BlockCreateParamsChildrenItemBulletedListItemRichTextItemAnnotations | None = Field(default=None)

class BlockCreateParamsChildrenItemBulletedListItem(BaseModel):
    """Bulleted list item content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockCreateParamsChildrenItemBulletedListItemRichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading3RichTextItemTextLink(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading3RichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading3RichTextItemText(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading3RichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockCreateParamsChildrenItemHeading3RichTextItemTextLink | None | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading3RichTextItemAnnotations(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading3RichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading3RichTextItemEquation(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading3RichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading3RichTextItem(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemHeading3.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockCreateParamsChildrenItemHeading3RichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockCreateParamsChildrenItemHeading3RichTextItemEquation | None = Field(default=None)
    annotations: BlockCreateParamsChildrenItemHeading3RichTextItemAnnotations | None = Field(default=None)

class BlockCreateParamsChildrenItemHeading3(BaseModel):
    """Heading 3 block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockCreateParamsChildrenItemHeading3RichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)
    is_toggleable: bool | None = Field(default=None)

class BlockCreateParamsChildrenItemFileExternal(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemFile.external"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemFileFileUpload(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemFile.file_upload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class BlockCreateParamsChildrenItemFile(BaseModel):
    """Media file. Use external URL or file upload."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="File type: external or file_upload")
    """File type: external or file_upload"""
    external: BlockCreateParamsChildrenItemFileExternal | None = Field(default=None)
    file_upload: BlockCreateParamsChildrenItemFileFileUpload | None = Field(default=None)

class BlockCreateParamsChildrenItemCodeRichTextItemEquation(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemCodeRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockCreateParamsChildrenItemCodeRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemCodeRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemCodeRichTextItemTextLink(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemCodeRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemCodeRichTextItemText(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemCodeRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockCreateParamsChildrenItemCodeRichTextItemTextLink | None | None = Field(default=None)

class BlockCreateParamsChildrenItemCodeRichTextItem(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemCode.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockCreateParamsChildrenItemCodeRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockCreateParamsChildrenItemCodeRichTextItemEquation | None = Field(default=None)
    annotations: BlockCreateParamsChildrenItemCodeRichTextItemAnnotations | None = Field(default=None)

class BlockCreateParamsChildrenItemCode(BaseModel):
    """Code block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockCreateParamsChildrenItemCodeRichTextItem] | None = Field(default=None)
    language: str | None = Field(default=None, description="Programming language for syntax highlighting")
    """Programming language for syntax highlighting"""

class BlockCreateParamsChildrenItemEquation(BaseModel):
    """Equation block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None, description="LaTeX expression")
    """LaTeX expression"""

class BlockCreateParamsChildrenItemBookmarkCaptionItemEquation(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemBookmarkCaptionItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockCreateParamsChildrenItemBookmarkCaptionItemAnnotations(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemBookmarkCaptionItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemBookmarkCaptionItemTextLink(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemBookmarkCaptionItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemBookmarkCaptionItemText(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemBookmarkCaptionItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockCreateParamsChildrenItemBookmarkCaptionItemTextLink | None | None = Field(default=None)

class BlockCreateParamsChildrenItemBookmarkCaptionItem(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemBookmark.caption_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockCreateParamsChildrenItemBookmarkCaptionItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockCreateParamsChildrenItemBookmarkCaptionItemEquation | None = Field(default=None)
    annotations: BlockCreateParamsChildrenItemBookmarkCaptionItemAnnotations | None = Field(default=None)

class BlockCreateParamsChildrenItemBookmark(BaseModel):
    """Bookmark block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None, description="URL to bookmark")
    """URL to bookmark"""
    caption: list[BlockCreateParamsChildrenItemBookmarkCaptionItem] | None = Field(default=None)

class BlockCreateParamsChildrenItemToDoRichTextItemTextLink(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemToDoRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemToDoRichTextItemText(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemToDoRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockCreateParamsChildrenItemToDoRichTextItemTextLink | None | None = Field(default=None)

class BlockCreateParamsChildrenItemToDoRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemToDoRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemToDoRichTextItemEquation(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemToDoRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockCreateParamsChildrenItemToDoRichTextItem(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemToDo.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockCreateParamsChildrenItemToDoRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockCreateParamsChildrenItemToDoRichTextItemEquation | None = Field(default=None)
    annotations: BlockCreateParamsChildrenItemToDoRichTextItemAnnotations | None = Field(default=None)

class BlockCreateParamsChildrenItemToDo(BaseModel):
    """To-do block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockCreateParamsChildrenItemToDoRichTextItem] | None = Field(default=None)
    checked: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItemAudioFileUpload(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemAudio.file_upload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class BlockCreateParamsChildrenItemAudioExternal(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemAudio.external"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemAudio(BaseModel):
    """Media file. Use external URL or file upload."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="File type: external or file_upload")
    """File type: external or file_upload"""
    external: BlockCreateParamsChildrenItemAudioExternal | None = Field(default=None)
    file_upload: BlockCreateParamsChildrenItemAudioFileUpload | None = Field(default=None)

class BlockCreateParamsChildrenItemVideoFileUpload(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemVideo.file_upload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class BlockCreateParamsChildrenItemVideoExternal(BaseModel):
    """Nested schema for BlockCreateParamsChildrenItemVideo.external"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockCreateParamsChildrenItemVideo(BaseModel):
    """Media file. Use external URL or file upload."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="File type: external or file_upload")
    """File type: external or file_upload"""
    external: BlockCreateParamsChildrenItemVideoExternal | None = Field(default=None)
    file_upload: BlockCreateParamsChildrenItemVideoFileUpload | None = Field(default=None)

class BlockCreateParamsChildrenItemEmbed(BaseModel):
    """Embed block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None, description="URL to embed")
    """URL to embed"""

class BlockCreateParamsChildrenItemTableOfContents(BaseModel):
    """Table of contents block"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str | None = Field(default=None)

class BlockCreateParamsChildrenItem(BaseModel):
    """A block object. Set type to the block kind and include matching content."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="Block type: paragraph, heading_1, heading_2, heading_3, bulleted_list_item, numbered_list_item, to_do, toggle, code, quote, callout, divider, bookmark, embed, equation, table_of_contents, image, video, file, pdf, audio, column_list, column, table, synced_block, link_to_page, etc.")
    """Block type: paragraph, heading_1, heading_2, heading_3, bulleted_list_item, numbered_list_item, to_do, toggle, code, quote, callout, divider, bookmark, embed, equation, table_of_contents, image, video, file, pdf, audio, column_list, column, table, synced_block, link_to_page, etc."""
    paragraph: BlockCreateParamsChildrenItemParagraph | None = Field(default=None, description="Paragraph block content")
    """Paragraph block content"""
    heading_1: BlockCreateParamsChildrenItemHeading1 | None = Field(default=None, description="Heading 1 block content")
    """Heading 1 block content"""
    heading_2: BlockCreateParamsChildrenItemHeading2 | None = Field(default=None, description="Heading 2 block content")
    """Heading 2 block content"""
    heading_3: BlockCreateParamsChildrenItemHeading3 | None = Field(default=None, description="Heading 3 block content")
    """Heading 3 block content"""
    bulleted_list_item: BlockCreateParamsChildrenItemBulletedListItem | None = Field(default=None, description="Bulleted list item content")
    """Bulleted list item content"""
    numbered_list_item: BlockCreateParamsChildrenItemNumberedListItem | None = Field(default=None, description="Numbered list item content")
    """Numbered list item content"""
    to_do: BlockCreateParamsChildrenItemToDo | None = Field(default=None, description="To-do block content")
    """To-do block content"""
    toggle: BlockCreateParamsChildrenItemToggle | None = Field(default=None, description="Toggle block content")
    """Toggle block content"""
    code: BlockCreateParamsChildrenItemCode | None = Field(default=None, description="Code block content")
    """Code block content"""
    quote: BlockCreateParamsChildrenItemQuote | None = Field(default=None, description="Quote block content")
    """Quote block content"""
    callout: BlockCreateParamsChildrenItemCallout | None = Field(default=None, description="Callout block content")
    """Callout block content"""
    divider: dict[str, Any] | None = Field(default=None, description="Divider block (empty object)")
    """Divider block (empty object)"""
    bookmark: BlockCreateParamsChildrenItemBookmark | None = Field(default=None, description="Bookmark block")
    """Bookmark block"""
    embed: BlockCreateParamsChildrenItemEmbed | None = Field(default=None, description="Embed block")
    """Embed block"""
    equation: BlockCreateParamsChildrenItemEquation | None = Field(default=None, description="Equation block")
    """Equation block"""
    table_of_contents: BlockCreateParamsChildrenItemTableOfContents | None = Field(default=None, description="Table of contents block")
    """Table of contents block"""
    image: BlockCreateParamsChildrenItemImage | None = Field(default=None, description="Media file. Use external URL or file upload.")
    """Media file. Use external URL or file upload."""
    video: BlockCreateParamsChildrenItemVideo | None = Field(default=None, description="Media file. Use external URL or file upload.")
    """Media file. Use external URL or file upload."""
    file: BlockCreateParamsChildrenItemFile | None = Field(default=None, description="Media file. Use external URL or file upload.")
    """Media file. Use external URL or file upload."""
    pdf: BlockCreateParamsChildrenItemPdf | None = Field(default=None, description="Media file. Use external URL or file upload.")
    """Media file. Use external URL or file upload."""
    audio: BlockCreateParamsChildrenItemAudio | None = Field(default=None, description="Media file. Use external URL or file upload.")
    """Media file. Use external URL or file upload."""

class BlockCreateParams(BaseModel):
    """Parameters for appending child blocks to a parent block or page. The block_id path parameter specifies the parent."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    children: list[BlockCreateParamsChildrenItem]

class BlockUpdateParamsHeading3RichTextItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsHeading3RichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsHeading3RichTextItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsHeading3RichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsHeading3RichTextItemText(BaseModel):
    """Nested schema for BlockUpdateParamsHeading3RichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsHeading3RichTextItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsHeading3RichTextItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsHeading3RichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsHeading3RichTextItem(BaseModel):
    """Nested schema for BlockUpdateParamsHeading3.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsHeading3RichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsHeading3RichTextItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsHeading3RichTextItemAnnotations | None = Field(default=None)

class BlockUpdateParamsHeading3(BaseModel):
    """Updated heading 3 content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockUpdateParamsHeading3RichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)
    is_toggleable: bool | None = Field(default=None)

class BlockUpdateParamsQuoteRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsQuoteRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsQuoteRichTextItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsQuoteRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsQuoteRichTextItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsQuoteRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsQuoteRichTextItemText(BaseModel):
    """Nested schema for BlockUpdateParamsQuoteRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsQuoteRichTextItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsQuoteRichTextItem(BaseModel):
    """Nested schema for BlockUpdateParamsQuote.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsQuoteRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsQuoteRichTextItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsQuoteRichTextItemAnnotations | None = Field(default=None)

class BlockUpdateParamsQuote(BaseModel):
    """Updated quote content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockUpdateParamsQuoteRichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsBulletedListItemRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsBulletedListItemRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsBulletedListItemRichTextItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsBulletedListItemRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsBulletedListItemRichTextItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsBulletedListItemRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsBulletedListItemRichTextItemText(BaseModel):
    """Nested schema for BlockUpdateParamsBulletedListItemRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsBulletedListItemRichTextItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsBulletedListItemRichTextItem(BaseModel):
    """Nested schema for BlockUpdateParamsBulletedListItem.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsBulletedListItemRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsBulletedListItemRichTextItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsBulletedListItemRichTextItemAnnotations | None = Field(default=None)

class BlockUpdateParamsBulletedListItem(BaseModel):
    """Updated bulleted list item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockUpdateParamsBulletedListItemRichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsEquation(BaseModel):
    """Updated equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsParagraphRichTextItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsParagraphRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsParagraphRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsParagraphRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsParagraphRichTextItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsParagraphRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsParagraphRichTextItemText(BaseModel):
    """Nested schema for BlockUpdateParamsParagraphRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsParagraphRichTextItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsParagraphRichTextItem(BaseModel):
    """Nested schema for BlockUpdateParamsParagraph.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsParagraphRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsParagraphRichTextItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsParagraphRichTextItemAnnotations | None = Field(default=None)

class BlockUpdateParamsParagraph(BaseModel):
    """Updated paragraph content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockUpdateParamsParagraphRichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsNumberedListItemRichTextItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsNumberedListItemRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsNumberedListItemRichTextItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsNumberedListItemRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsNumberedListItemRichTextItemText(BaseModel):
    """Nested schema for BlockUpdateParamsNumberedListItemRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsNumberedListItemRichTextItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsNumberedListItemRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsNumberedListItemRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsNumberedListItemRichTextItem(BaseModel):
    """Nested schema for BlockUpdateParamsNumberedListItem.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsNumberedListItemRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsNumberedListItemRichTextItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsNumberedListItemRichTextItemAnnotations | None = Field(default=None)

class BlockUpdateParamsNumberedListItem(BaseModel):
    """Updated numbered list item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockUpdateParamsNumberedListItemRichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsEmbed(BaseModel):
    """Updated embed"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsPdfFileUpload(BaseModel):
    """Nested schema for BlockUpdateParamsPdf.file_upload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class BlockUpdateParamsPdfExternal(BaseModel):
    """Nested schema for BlockUpdateParamsPdf.external"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsPdf(BaseModel):
    """Media file. Use external URL or file upload."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="File type: external or file_upload")
    """File type: external or file_upload"""
    external: BlockUpdateParamsPdfExternal | None = Field(default=None)
    file_upload: BlockUpdateParamsPdfFileUpload | None = Field(default=None)

class BlockUpdateParamsImageFileUpload(BaseModel):
    """Nested schema for BlockUpdateParamsImage.file_upload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class BlockUpdateParamsImageExternal(BaseModel):
    """Nested schema for BlockUpdateParamsImage.external"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsImage(BaseModel):
    """Media file. Use external URL or file upload."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="File type: external or file_upload")
    """File type: external or file_upload"""
    external: BlockUpdateParamsImageExternal | None = Field(default=None)
    file_upload: BlockUpdateParamsImageFileUpload | None = Field(default=None)

class BlockUpdateParamsToDoRichTextItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsToDoRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsToDoRichTextItemText(BaseModel):
    """Nested schema for BlockUpdateParamsToDoRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsToDoRichTextItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsToDoRichTextItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsToDoRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsToDoRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsToDoRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsToDoRichTextItem(BaseModel):
    """Nested schema for BlockUpdateParamsToDo.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsToDoRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsToDoRichTextItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsToDoRichTextItemAnnotations | None = Field(default=None)

class BlockUpdateParamsToDo(BaseModel):
    """Updated to-do content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockUpdateParamsToDoRichTextItem] | None = Field(default=None)
    checked: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsCalloutRichTextItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsCalloutRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsCalloutRichTextItemText(BaseModel):
    """Nested schema for BlockUpdateParamsCalloutRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsCalloutRichTextItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsCalloutRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsCalloutRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsCalloutRichTextItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsCalloutRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsCalloutRichTextItem(BaseModel):
    """Nested schema for BlockUpdateParamsCallout.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsCalloutRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsCalloutRichTextItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsCalloutRichTextItemAnnotations | None = Field(default=None)

class BlockUpdateParamsCallout(BaseModel):
    """Updated callout content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockUpdateParamsCalloutRichTextItem] | None = Field(default=None)
    icon: dict[str, Any] | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsTable(BaseModel):
    """Updated table properties"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    has_column_header: bool | None = Field(default=None)
    has_row_header: bool | None = Field(default=None)

class BlockUpdateParamsHeading1RichTextItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsHeading1RichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsHeading1RichTextItemText(BaseModel):
    """Nested schema for BlockUpdateParamsHeading1RichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsHeading1RichTextItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsHeading1RichTextItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsHeading1RichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsHeading1RichTextItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsHeading1RichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsHeading1RichTextItem(BaseModel):
    """Nested schema for BlockUpdateParamsHeading1.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsHeading1RichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsHeading1RichTextItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsHeading1RichTextItemAnnotations | None = Field(default=None)

class BlockUpdateParamsHeading1(BaseModel):
    """Updated heading 1 content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockUpdateParamsHeading1RichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)
    is_toggleable: bool | None = Field(default=None)

class BlockUpdateParamsBookmarkCaptionItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsBookmarkCaptionItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsBookmarkCaptionItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsBookmarkCaptionItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsBookmarkCaptionItemText(BaseModel):
    """Nested schema for BlockUpdateParamsBookmarkCaptionItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsBookmarkCaptionItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsBookmarkCaptionItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsBookmarkCaptionItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsBookmarkCaptionItem(BaseModel):
    """Nested schema for BlockUpdateParamsBookmark.caption_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsBookmarkCaptionItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsBookmarkCaptionItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsBookmarkCaptionItemAnnotations | None = Field(default=None)

class BlockUpdateParamsBookmark(BaseModel):
    """Updated bookmark"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)
    caption: list[BlockUpdateParamsBookmarkCaptionItem] | None = Field(default=None)

class BlockUpdateParamsHeading2RichTextItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsHeading2RichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsHeading2RichTextItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsHeading2RichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsHeading2RichTextItemText(BaseModel):
    """Nested schema for BlockUpdateParamsHeading2RichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsHeading2RichTextItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsHeading2RichTextItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsHeading2RichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsHeading2RichTextItem(BaseModel):
    """Nested schema for BlockUpdateParamsHeading2.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsHeading2RichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsHeading2RichTextItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsHeading2RichTextItemAnnotations | None = Field(default=None)

class BlockUpdateParamsHeading2(BaseModel):
    """Updated heading 2 content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockUpdateParamsHeading2RichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)
    is_toggleable: bool | None = Field(default=None)

class BlockUpdateParamsAudioFileUpload(BaseModel):
    """Nested schema for BlockUpdateParamsAudio.file_upload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class BlockUpdateParamsAudioExternal(BaseModel):
    """Nested schema for BlockUpdateParamsAudio.external"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsAudio(BaseModel):
    """Media file. Use external URL or file upload."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="File type: external or file_upload")
    """File type: external or file_upload"""
    external: BlockUpdateParamsAudioExternal | None = Field(default=None)
    file_upload: BlockUpdateParamsAudioFileUpload | None = Field(default=None)

class BlockUpdateParamsToggleRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsToggleRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsToggleRichTextItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsToggleRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsToggleRichTextItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsToggleRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsToggleRichTextItemText(BaseModel):
    """Nested schema for BlockUpdateParamsToggleRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsToggleRichTextItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsToggleRichTextItem(BaseModel):
    """Nested schema for BlockUpdateParamsToggle.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsToggleRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsToggleRichTextItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsToggleRichTextItemAnnotations | None = Field(default=None)

class BlockUpdateParamsToggle(BaseModel):
    """Updated toggle content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockUpdateParamsToggleRichTextItem] | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsCodeRichTextItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsCodeRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsCodeRichTextItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsCodeRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsCodeRichTextItemText(BaseModel):
    """Nested schema for BlockUpdateParamsCodeRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsCodeRichTextItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsCodeRichTextItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsCodeRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsCodeRichTextItem(BaseModel):
    """Nested schema for BlockUpdateParamsCode.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsCodeRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsCodeRichTextItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsCodeRichTextItemAnnotations | None = Field(default=None)

class BlockUpdateParamsCodeCaptionItemAnnotations(BaseModel):
    """Nested schema for BlockUpdateParamsCodeCaptionItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class BlockUpdateParamsCodeCaptionItemEquation(BaseModel):
    """Nested schema for BlockUpdateParamsCodeCaptionItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class BlockUpdateParamsCodeCaptionItemTextLink(BaseModel):
    """Nested schema for BlockUpdateParamsCodeCaptionItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsCodeCaptionItemText(BaseModel):
    """Nested schema for BlockUpdateParamsCodeCaptionItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: BlockUpdateParamsCodeCaptionItemTextLink | None | None = Field(default=None)

class BlockUpdateParamsCodeCaptionItem(BaseModel):
    """Nested schema for BlockUpdateParamsCode.caption_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: BlockUpdateParamsCodeCaptionItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: BlockUpdateParamsCodeCaptionItemEquation | None = Field(default=None)
    annotations: BlockUpdateParamsCodeCaptionItemAnnotations | None = Field(default=None)

class BlockUpdateParamsCode(BaseModel):
    """Updated code block content"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rich_text: list[BlockUpdateParamsCodeRichTextItem] | None = Field(default=None)
    language: str | None = Field(default=None)
    caption: list[BlockUpdateParamsCodeCaptionItem] | None = Field(default=None)

class BlockUpdateParamsFileFileUpload(BaseModel):
    """Nested schema for BlockUpdateParamsFile.file_upload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class BlockUpdateParamsFileExternal(BaseModel):
    """Nested schema for BlockUpdateParamsFile.external"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsFile(BaseModel):
    """Media file. Use external URL or file upload."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="File type: external or file_upload")
    """File type: external or file_upload"""
    external: BlockUpdateParamsFileExternal | None = Field(default=None)
    file_upload: BlockUpdateParamsFileFileUpload | None = Field(default=None)

class BlockUpdateParamsVideoExternal(BaseModel):
    """Nested schema for BlockUpdateParamsVideo.external"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class BlockUpdateParamsVideoFileUpload(BaseModel):
    """Nested schema for BlockUpdateParamsVideo.file_upload"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class BlockUpdateParamsVideo(BaseModel):
    """Media file. Use external URL or file upload."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="File type: external or file_upload")
    """File type: external or file_upload"""
    external: BlockUpdateParamsVideoExternal | None = Field(default=None)
    file_upload: BlockUpdateParamsVideoFileUpload | None = Field(default=None)

class BlockUpdateParams(BaseModel):
    """Parameters for updating a block. Include the block type and its updated content. Omitted fields within the type are unchanged."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    paragraph: BlockUpdateParamsParagraph | None = Field(default=None)
    heading_1: BlockUpdateParamsHeading1 | None = Field(default=None)
    heading_2: BlockUpdateParamsHeading2 | None = Field(default=None)
    heading_3: BlockUpdateParamsHeading3 | None = Field(default=None)
    bulleted_list_item: BlockUpdateParamsBulletedListItem | None = Field(default=None)
    numbered_list_item: BlockUpdateParamsNumberedListItem | None = Field(default=None)
    to_do: BlockUpdateParamsToDo | None = Field(default=None)
    toggle: BlockUpdateParamsToggle | None = Field(default=None)
    code: BlockUpdateParamsCode | None = Field(default=None)
    quote: BlockUpdateParamsQuote | None = Field(default=None)
    callout: BlockUpdateParamsCallout | None = Field(default=None)
    bookmark: BlockUpdateParamsBookmark | None = Field(default=None)
    embed: BlockUpdateParamsEmbed | None = Field(default=None)
    equation: BlockUpdateParamsEquation | None = Field(default=None)
    image: BlockUpdateParamsImage | None = Field(default=None)
    video: BlockUpdateParamsVideo | None = Field(default=None)
    file: BlockUpdateParamsFile | None = Field(default=None)
    pdf: BlockUpdateParamsPdf | None = Field(default=None)
    audio: BlockUpdateParamsAudio | None = Field(default=None)
    table: BlockUpdateParamsTable | None = Field(default=None)
    archived: bool | None = Field(default=None)

class CommentCreateParamsRichTextItemAnnotations(BaseModel):
    """Nested schema for CommentCreateParamsRichTextItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class CommentCreateParamsRichTextItemTextLink(BaseModel):
    """Nested schema for CommentCreateParamsRichTextItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class CommentCreateParamsRichTextItemText(BaseModel):
    """Nested schema for CommentCreateParamsRichTextItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: CommentCreateParamsRichTextItemTextLink | None | None = Field(default=None)

class CommentCreateParamsRichTextItemEquation(BaseModel):
    """Nested schema for CommentCreateParamsRichTextItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class CommentCreateParamsRichTextItem(BaseModel):
    """Nested schema for CommentCreateParams.rich_text_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: CommentCreateParamsRichTextItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: CommentCreateParamsRichTextItemEquation | None = Field(default=None)
    annotations: CommentCreateParamsRichTextItemAnnotations | None = Field(default=None)

class CommentCreateParams(BaseModel):
    """Parameters for creating a comment. Provide either parent (with page_id or block_id) for a new comment, or discussion_id to reply to an existing thread. Exactly one of parent or discussion_id must be provided."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    parent: dict[str, Any] | None = Field(default=None)
    discussion_id: str | None = Field(default=None)
    rich_text: list[CommentCreateParamsRichTextItem]

class DataSourceUpdateParamsCoverExternal(BaseModel):
    """External URL cover"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class DataSourceUpdateParamsCoverFileUpload(BaseModel):
    """Uploaded file cover"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class DataSourceUpdateParamsCover(BaseModel):
    """Cover image. Supports external URL or file upload. Set to null to remove."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="Cover type: external or file_upload")
    """Cover type: external or file_upload"""
    external: DataSourceUpdateParamsCoverExternal | None = Field(default=None, description="External URL cover")
    """External URL cover"""
    file_upload: DataSourceUpdateParamsCoverFileUpload | None = Field(default=None, description="Uploaded file cover")
    """Uploaded file cover"""

class DataSourceUpdateParamsTitleItemAnnotations(BaseModel):
    """Nested schema for DataSourceUpdateParamsTitleItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class DataSourceUpdateParamsTitleItemEquation(BaseModel):
    """Nested schema for DataSourceUpdateParamsTitleItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class DataSourceUpdateParamsTitleItemTextLink(BaseModel):
    """Nested schema for DataSourceUpdateParamsTitleItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class DataSourceUpdateParamsTitleItemText(BaseModel):
    """Nested schema for DataSourceUpdateParamsTitleItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: DataSourceUpdateParamsTitleItemTextLink | None | None = Field(default=None)

class DataSourceUpdateParamsTitleItem(BaseModel):
    """Nested schema for DataSourceUpdateParams.title_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: DataSourceUpdateParamsTitleItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: DataSourceUpdateParamsTitleItemEquation | None = Field(default=None)
    annotations: DataSourceUpdateParamsTitleItemAnnotations | None = Field(default=None)

class DataSourceUpdateParamsDescriptionItemAnnotations(BaseModel):
    """Nested schema for DataSourceUpdateParamsDescriptionItem.annotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    bold: bool | None = Field(default=None)
    italic: bool | None = Field(default=None)
    strikethrough: bool | None = Field(default=None)
    underline: bool | None = Field(default=None)
    code: bool | None = Field(default=None)
    color: str | None = Field(default=None)

class DataSourceUpdateParamsDescriptionItemTextLink(BaseModel):
    """Nested schema for DataSourceUpdateParamsDescriptionItemText.link"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class DataSourceUpdateParamsDescriptionItemText(BaseModel):
    """Nested schema for DataSourceUpdateParamsDescriptionItem.text"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None)
    link: DataSourceUpdateParamsDescriptionItemTextLink | None | None = Field(default=None)

class DataSourceUpdateParamsDescriptionItemEquation(BaseModel):
    """Nested schema for DataSourceUpdateParamsDescriptionItem.equation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    expression: str | None = Field(default=None)

class DataSourceUpdateParamsDescriptionItem(BaseModel):
    """Nested schema for DataSourceUpdateParams.description_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type")
    text: DataSourceUpdateParamsDescriptionItemText | None = Field(default=None)
    mention: dict[str, Any] | None = Field(default=None)
    equation: DataSourceUpdateParamsDescriptionItemEquation | None = Field(default=None)
    annotations: DataSourceUpdateParamsDescriptionItemAnnotations | None = Field(default=None)

class DataSourceUpdateParamsIconExternal(BaseModel):
    """External URL icon (when type is external)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    url: str | None = Field(default=None)

class DataSourceUpdateParamsIconIcon(BaseModel):
    """Notion native icon (when type is icon)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    color: str | None = Field(default=None)

class DataSourceUpdateParamsIconFileUpload(BaseModel):
    """Uploaded file icon (when type is file_upload)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class DataSourceUpdateParamsIconCustomEmoji(BaseModel):
    """Custom emoji icon (when type is custom_emoji)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)

class DataSourceUpdateParamsIcon(BaseModel):
    """Icon. Supports emoji, external URL, file upload, custom emoji, and Notion native icons. Set to null to remove."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None = Field(default=None, alias="type", description="Icon type: emoji, external, file_upload, custom_emoji, or icon")
    """Icon type: emoji, external, file_upload, custom_emoji, or icon"""
    emoji: str | None = Field(default=None, description="Emoji character (when type is emoji)")
    """Emoji character (when type is emoji)"""
    external: DataSourceUpdateParamsIconExternal | None = Field(default=None, description="External URL icon (when type is external)")
    """External URL icon (when type is external)"""
    file_upload: DataSourceUpdateParamsIconFileUpload | None = Field(default=None, description="Uploaded file icon (when type is file_upload)")
    """Uploaded file icon (when type is file_upload)"""
    custom_emoji: DataSourceUpdateParamsIconCustomEmoji | None = Field(default=None, description="Custom emoji icon (when type is custom_emoji)")
    """Custom emoji icon (when type is custom_emoji)"""
    icon: DataSourceUpdateParamsIconIcon | None = Field(default=None, description="Notion native icon (when type is icon)")
    """Notion native icon (when type is icon)"""

class DataSourceUpdateParams(BaseModel):
    """Parameters for updating a data source. All fields are optional."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: list[DataSourceUpdateParamsTitleItem] | None = Field(default=None)
    description: list[DataSourceUpdateParamsDescriptionItem] | None = Field(default=None)
    properties: dict[str, Any] | None = Field(default=None)
    icon: DataSourceUpdateParamsIcon | None = Field(default=None)
    cover: DataSourceUpdateParamsCover | None = Field(default=None)
    archived: bool | None = Field(default=None)
    in_trash: bool | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class PagesListResultMeta(BaseModel):
    """Metadata for pages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class DataSourcesListResultMeta(BaseModel):
    """Metadata for data_sources.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class BlocksListResultMeta(BaseModel):
    """Metadata for blocks.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class CommentsListResultMeta(BaseModel):
    """Metadata for comments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

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
    meta: S | None = None
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
    object_: dict[str, Any] | None = None
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
    object_: dict[str, Any] | None = None
    """Always user"""
    person: dict[str, Any] | None = None
    """Person-specific data"""
    type_: dict[str, Any] | None = None
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
    object_: dict[str, Any] | None = None
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
    object_: dict[str, Any] | None = None
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
    type_: dict[str, Any] | None = None
    """The type of the block."""
    unsupported: dict[str, Any] | None = None
    """Represents an unsupported block."""
    video: dict[str, Any] | None = None
    """Represents a video block."""


class CommentsSearchData(BaseModel):
    """Search result data for comments entity."""
    model_config = ConfigDict(extra="allow")

    created_by: dict[str, Any] | None = None
    """User who created the comment."""
    created_time: str | None = None
    """Date and time when the comment was created."""
    discussion_id: str | None = None
    """Discussion thread ID."""
    id: str | None = None
    """Unique identifier for the comment."""
    last_edited_time: str | None = None
    """Date and time when the comment was last edited."""
    object_: str | None = None
    """Always comment."""
    parent: dict[str, Any] | None = None
    """Parent of the comment."""
    rich_text: list[Any] | None = None
    """Content of the comment as rich text."""


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

CommentsSearchResult = AirbyteSearchResult[CommentsSearchData]
"""Search result type for comments entity."""



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

