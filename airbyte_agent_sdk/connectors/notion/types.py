"""
Type definitions for notion connector.
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

class PagesListParamsFilter(TypedDict):
    """Nested schema for PagesListParams.filter"""
    property: NotRequired[str]
    value: NotRequired[str]

class PagesListParamsSort(TypedDict):
    """Nested schema for PagesListParams.sort"""
    direction: NotRequired[str]
    timestamp: NotRequired[str]

class PagesCreateParamsIconExternal(TypedDict):
    """External URL icon (when type is external)"""
    url: NotRequired[str]

class PagesCreateParamsIconFileUpload(TypedDict):
    """Uploaded file icon (when type is file_upload)"""
    id: NotRequired[str]

class PagesCreateParamsIconCustomEmoji(TypedDict):
    """Custom emoji icon (when type is custom_emoji)"""
    id: NotRequired[str]

class PagesCreateParamsIconIcon(TypedDict):
    """Notion native icon (when type is icon)"""
    name: NotRequired[str]
    color: NotRequired[str]

class PagesCreateParamsIcon(TypedDict):
    """Icon. Supports emoji, external URL, file upload, custom emoji, and Notion native icons. Set to null to remove."""
    type_: NotRequired[str]
    emoji: NotRequired[str]
    external: NotRequired[PagesCreateParamsIconExternal]
    file_upload: NotRequired[PagesCreateParamsIconFileUpload]
    custom_emoji: NotRequired[PagesCreateParamsIconCustomEmoji]
    icon: NotRequired[PagesCreateParamsIconIcon]

class PagesCreateParamsCoverExternal(TypedDict):
    """External URL cover"""
    url: NotRequired[str]

class PagesCreateParamsCoverFileUpload(TypedDict):
    """Uploaded file cover"""
    id: NotRequired[str]

class PagesCreateParamsCover(TypedDict):
    """Cover image. Supports external URL or file upload. Set to null to remove."""
    type_: NotRequired[str]
    external: NotRequired[PagesCreateParamsCoverExternal]
    file_upload: NotRequired[PagesCreateParamsCoverFileUpload]

class PagesUpdateParamsIconExternal(TypedDict):
    """External URL icon (when type is external)"""
    url: NotRequired[str]

class PagesUpdateParamsIconFileUpload(TypedDict):
    """Uploaded file icon (when type is file_upload)"""
    id: NotRequired[str]

class PagesUpdateParamsIconCustomEmoji(TypedDict):
    """Custom emoji icon (when type is custom_emoji)"""
    id: NotRequired[str]

class PagesUpdateParamsIconIcon(TypedDict):
    """Notion native icon (when type is icon)"""
    name: NotRequired[str]
    color: NotRequired[str]

class PagesUpdateParamsIcon(TypedDict):
    """Icon. Supports emoji, external URL, file upload, custom emoji, and Notion native icons. Set to null to remove."""
    type_: NotRequired[str]
    emoji: NotRequired[str]
    external: NotRequired[PagesUpdateParamsIconExternal]
    file_upload: NotRequired[PagesUpdateParamsIconFileUpload]
    custom_emoji: NotRequired[PagesUpdateParamsIconCustomEmoji]
    icon: NotRequired[PagesUpdateParamsIconIcon]

class PagesUpdateParamsCoverExternal(TypedDict):
    """External URL cover"""
    url: NotRequired[str]

class PagesUpdateParamsCoverFileUpload(TypedDict):
    """Uploaded file cover"""
    id: NotRequired[str]

class PagesUpdateParamsCover(TypedDict):
    """Cover image. Supports external URL or file upload. Set to null to remove."""
    type_: NotRequired[str]
    external: NotRequired[PagesUpdateParamsCoverExternal]
    file_upload: NotRequired[PagesUpdateParamsCoverFileUpload]

class DataSourcesListParamsFilter(TypedDict):
    """Nested schema for DataSourcesListParams.filter"""
    property: NotRequired[str]
    value: NotRequired[str]

class DataSourcesListParamsSort(TypedDict):
    """Nested schema for DataSourcesListParams.sort"""
    direction: NotRequired[str]
    timestamp: NotRequired[str]

class BlocksCreateParamsChildrenItemParagraphRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemParagraphRichTextItemText.link"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemParagraphRichTextItemText(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemParagraphRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksCreateParamsChildrenItemParagraphRichTextItemTextLink | None]

class BlocksCreateParamsChildrenItemParagraphRichTextItemEquation(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemParagraphRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemParagraphRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemParagraphRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemParagraphRichTextItem(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemParagraph.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksCreateParamsChildrenItemParagraphRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksCreateParamsChildrenItemParagraphRichTextItemEquation]
    annotations: NotRequired[BlocksCreateParamsChildrenItemParagraphRichTextItemAnnotations]

class BlocksCreateParamsChildrenItemParagraph(TypedDict):
    """Paragraph block content"""
    rich_text: NotRequired[list[BlocksCreateParamsChildrenItemParagraphRichTextItem]]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemHeading1RichTextItemTextLink(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading1RichTextItemText.link"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemHeading1RichTextItemText(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading1RichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksCreateParamsChildrenItemHeading1RichTextItemTextLink | None]

class BlocksCreateParamsChildrenItemHeading1RichTextItemEquation(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading1RichTextItem.equation"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemHeading1RichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading1RichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemHeading1RichTextItem(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading1.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksCreateParamsChildrenItemHeading1RichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksCreateParamsChildrenItemHeading1RichTextItemEquation]
    annotations: NotRequired[BlocksCreateParamsChildrenItemHeading1RichTextItemAnnotations]

class BlocksCreateParamsChildrenItemHeading1(TypedDict):
    """Heading 1 block content"""
    rich_text: NotRequired[list[BlocksCreateParamsChildrenItemHeading1RichTextItem]]
    color: NotRequired[str]
    is_toggleable: NotRequired[bool]

class BlocksCreateParamsChildrenItemHeading2RichTextItemTextLink(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading2RichTextItemText.link"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemHeading2RichTextItemText(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading2RichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksCreateParamsChildrenItemHeading2RichTextItemTextLink | None]

class BlocksCreateParamsChildrenItemHeading2RichTextItemEquation(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading2RichTextItem.equation"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemHeading2RichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading2RichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemHeading2RichTextItem(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading2.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksCreateParamsChildrenItemHeading2RichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksCreateParamsChildrenItemHeading2RichTextItemEquation]
    annotations: NotRequired[BlocksCreateParamsChildrenItemHeading2RichTextItemAnnotations]

class BlocksCreateParamsChildrenItemHeading2(TypedDict):
    """Heading 2 block content"""
    rich_text: NotRequired[list[BlocksCreateParamsChildrenItemHeading2RichTextItem]]
    color: NotRequired[str]
    is_toggleable: NotRequired[bool]

class BlocksCreateParamsChildrenItemHeading3RichTextItemTextLink(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading3RichTextItemText.link"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemHeading3RichTextItemText(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading3RichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksCreateParamsChildrenItemHeading3RichTextItemTextLink | None]

class BlocksCreateParamsChildrenItemHeading3RichTextItemEquation(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading3RichTextItem.equation"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemHeading3RichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading3RichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemHeading3RichTextItem(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemHeading3.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksCreateParamsChildrenItemHeading3RichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksCreateParamsChildrenItemHeading3RichTextItemEquation]
    annotations: NotRequired[BlocksCreateParamsChildrenItemHeading3RichTextItemAnnotations]

class BlocksCreateParamsChildrenItemHeading3(TypedDict):
    """Heading 3 block content"""
    rich_text: NotRequired[list[BlocksCreateParamsChildrenItemHeading3RichTextItem]]
    color: NotRequired[str]
    is_toggleable: NotRequired[bool]

class BlocksCreateParamsChildrenItemBulletedListItemRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemBulletedListItemRichTextItemText.link"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemBulletedListItemRichTextItemText(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemBulletedListItemRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksCreateParamsChildrenItemBulletedListItemRichTextItemTextLink | None]

class BlocksCreateParamsChildrenItemBulletedListItemRichTextItemEquation(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemBulletedListItemRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemBulletedListItemRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemBulletedListItemRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemBulletedListItemRichTextItem(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemBulletedListItem.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksCreateParamsChildrenItemBulletedListItemRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksCreateParamsChildrenItemBulletedListItemRichTextItemEquation]
    annotations: NotRequired[BlocksCreateParamsChildrenItemBulletedListItemRichTextItemAnnotations]

class BlocksCreateParamsChildrenItemBulletedListItem(TypedDict):
    """Bulleted list item content"""
    rich_text: NotRequired[list[BlocksCreateParamsChildrenItemBulletedListItemRichTextItem]]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemNumberedListItemRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemNumberedListItemRichTextItemText.link"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemNumberedListItemRichTextItemText(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemNumberedListItemRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksCreateParamsChildrenItemNumberedListItemRichTextItemTextLink | None]

class BlocksCreateParamsChildrenItemNumberedListItemRichTextItemEquation(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemNumberedListItemRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemNumberedListItemRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemNumberedListItemRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemNumberedListItemRichTextItem(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemNumberedListItem.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksCreateParamsChildrenItemNumberedListItemRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksCreateParamsChildrenItemNumberedListItemRichTextItemEquation]
    annotations: NotRequired[BlocksCreateParamsChildrenItemNumberedListItemRichTextItemAnnotations]

class BlocksCreateParamsChildrenItemNumberedListItem(TypedDict):
    """Numbered list item content"""
    rich_text: NotRequired[list[BlocksCreateParamsChildrenItemNumberedListItemRichTextItem]]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemToDoRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemToDoRichTextItemText.link"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemToDoRichTextItemText(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemToDoRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksCreateParamsChildrenItemToDoRichTextItemTextLink | None]

class BlocksCreateParamsChildrenItemToDoRichTextItemEquation(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemToDoRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemToDoRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemToDoRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemToDoRichTextItem(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemToDo.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksCreateParamsChildrenItemToDoRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksCreateParamsChildrenItemToDoRichTextItemEquation]
    annotations: NotRequired[BlocksCreateParamsChildrenItemToDoRichTextItemAnnotations]

class BlocksCreateParamsChildrenItemToDo(TypedDict):
    """To-do block content"""
    rich_text: NotRequired[list[BlocksCreateParamsChildrenItemToDoRichTextItem]]
    checked: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemToggleRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemToggleRichTextItemText.link"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemToggleRichTextItemText(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemToggleRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksCreateParamsChildrenItemToggleRichTextItemTextLink | None]

class BlocksCreateParamsChildrenItemToggleRichTextItemEquation(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemToggleRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemToggleRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemToggleRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemToggleRichTextItem(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemToggle.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksCreateParamsChildrenItemToggleRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksCreateParamsChildrenItemToggleRichTextItemEquation]
    annotations: NotRequired[BlocksCreateParamsChildrenItemToggleRichTextItemAnnotations]

class BlocksCreateParamsChildrenItemToggle(TypedDict):
    """Toggle block content"""
    rich_text: NotRequired[list[BlocksCreateParamsChildrenItemToggleRichTextItem]]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemCodeRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemCodeRichTextItemText.link"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemCodeRichTextItemText(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemCodeRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksCreateParamsChildrenItemCodeRichTextItemTextLink | None]

class BlocksCreateParamsChildrenItemCodeRichTextItemEquation(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemCodeRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemCodeRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemCodeRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemCodeRichTextItem(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemCode.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksCreateParamsChildrenItemCodeRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksCreateParamsChildrenItemCodeRichTextItemEquation]
    annotations: NotRequired[BlocksCreateParamsChildrenItemCodeRichTextItemAnnotations]

class BlocksCreateParamsChildrenItemCode(TypedDict):
    """Code block content"""
    rich_text: NotRequired[list[BlocksCreateParamsChildrenItemCodeRichTextItem]]
    language: NotRequired[str]

class BlocksCreateParamsChildrenItemQuoteRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemQuoteRichTextItemText.link"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemQuoteRichTextItemText(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemQuoteRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksCreateParamsChildrenItemQuoteRichTextItemTextLink | None]

class BlocksCreateParamsChildrenItemQuoteRichTextItemEquation(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemQuoteRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemQuoteRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemQuoteRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemQuoteRichTextItem(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemQuote.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksCreateParamsChildrenItemQuoteRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksCreateParamsChildrenItemQuoteRichTextItemEquation]
    annotations: NotRequired[BlocksCreateParamsChildrenItemQuoteRichTextItemAnnotations]

class BlocksCreateParamsChildrenItemQuote(TypedDict):
    """Quote block content"""
    rich_text: NotRequired[list[BlocksCreateParamsChildrenItemQuoteRichTextItem]]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemCalloutRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemCalloutRichTextItemText.link"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemCalloutRichTextItemText(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemCalloutRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksCreateParamsChildrenItemCalloutRichTextItemTextLink | None]

class BlocksCreateParamsChildrenItemCalloutRichTextItemEquation(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemCalloutRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemCalloutRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemCalloutRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemCalloutRichTextItem(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemCallout.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksCreateParamsChildrenItemCalloutRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksCreateParamsChildrenItemCalloutRichTextItemEquation]
    annotations: NotRequired[BlocksCreateParamsChildrenItemCalloutRichTextItemAnnotations]

class BlocksCreateParamsChildrenItemCallout(TypedDict):
    """Callout block content"""
    rich_text: NotRequired[list[BlocksCreateParamsChildrenItemCalloutRichTextItem]]
    icon: NotRequired[dict[str, Any]]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemBookmarkCaptionItemTextLink(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemBookmarkCaptionItemText.link"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemBookmarkCaptionItemText(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemBookmarkCaptionItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksCreateParamsChildrenItemBookmarkCaptionItemTextLink | None]

class BlocksCreateParamsChildrenItemBookmarkCaptionItemEquation(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemBookmarkCaptionItem.equation"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemBookmarkCaptionItemAnnotations(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemBookmarkCaptionItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemBookmarkCaptionItem(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemBookmark.caption_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksCreateParamsChildrenItemBookmarkCaptionItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksCreateParamsChildrenItemBookmarkCaptionItemEquation]
    annotations: NotRequired[BlocksCreateParamsChildrenItemBookmarkCaptionItemAnnotations]

class BlocksCreateParamsChildrenItemBookmark(TypedDict):
    """Bookmark block"""
    url: NotRequired[str]
    caption: NotRequired[list[BlocksCreateParamsChildrenItemBookmarkCaptionItem]]

class BlocksCreateParamsChildrenItemEmbed(TypedDict):
    """Embed block"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemEquation(TypedDict):
    """Equation block"""
    expression: NotRequired[str]

class BlocksCreateParamsChildrenItemTableOfContents(TypedDict):
    """Table of contents block"""
    color: NotRequired[str]

class BlocksCreateParamsChildrenItemImageExternal(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemImage.external"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemImageFileUpload(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemImage.file_upload"""
    id: NotRequired[str]

class BlocksCreateParamsChildrenItemImage(TypedDict):
    """Media file. Use external URL or file upload."""
    type_: NotRequired[str]
    external: NotRequired[BlocksCreateParamsChildrenItemImageExternal]
    file_upload: NotRequired[BlocksCreateParamsChildrenItemImageFileUpload]

class BlocksCreateParamsChildrenItemVideoExternal(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemVideo.external"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemVideoFileUpload(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemVideo.file_upload"""
    id: NotRequired[str]

class BlocksCreateParamsChildrenItemVideo(TypedDict):
    """Media file. Use external URL or file upload."""
    type_: NotRequired[str]
    external: NotRequired[BlocksCreateParamsChildrenItemVideoExternal]
    file_upload: NotRequired[BlocksCreateParamsChildrenItemVideoFileUpload]

class BlocksCreateParamsChildrenItemFileExternal(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemFile.external"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemFileFileUpload(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemFile.file_upload"""
    id: NotRequired[str]

class BlocksCreateParamsChildrenItemFile(TypedDict):
    """Media file. Use external URL or file upload."""
    type_: NotRequired[str]
    external: NotRequired[BlocksCreateParamsChildrenItemFileExternal]
    file_upload: NotRequired[BlocksCreateParamsChildrenItemFileFileUpload]

class BlocksCreateParamsChildrenItemPdfExternal(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemPdf.external"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemPdfFileUpload(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemPdf.file_upload"""
    id: NotRequired[str]

class BlocksCreateParamsChildrenItemPdf(TypedDict):
    """Media file. Use external URL or file upload."""
    type_: NotRequired[str]
    external: NotRequired[BlocksCreateParamsChildrenItemPdfExternal]
    file_upload: NotRequired[BlocksCreateParamsChildrenItemPdfFileUpload]

class BlocksCreateParamsChildrenItemAudioExternal(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemAudio.external"""
    url: NotRequired[str]

class BlocksCreateParamsChildrenItemAudioFileUpload(TypedDict):
    """Nested schema for BlocksCreateParamsChildrenItemAudio.file_upload"""
    id: NotRequired[str]

class BlocksCreateParamsChildrenItemAudio(TypedDict):
    """Media file. Use external URL or file upload."""
    type_: NotRequired[str]
    external: NotRequired[BlocksCreateParamsChildrenItemAudioExternal]
    file_upload: NotRequired[BlocksCreateParamsChildrenItemAudioFileUpload]

class BlocksCreateParamsChildrenItem(TypedDict):
    """A block object. Set type to the block kind and include matching content."""
    type_: NotRequired[str]
    paragraph: NotRequired[BlocksCreateParamsChildrenItemParagraph]
    heading_1: NotRequired[BlocksCreateParamsChildrenItemHeading1]
    heading_2: NotRequired[BlocksCreateParamsChildrenItemHeading2]
    heading_3: NotRequired[BlocksCreateParamsChildrenItemHeading3]
    bulleted_list_item: NotRequired[BlocksCreateParamsChildrenItemBulletedListItem]
    numbered_list_item: NotRequired[BlocksCreateParamsChildrenItemNumberedListItem]
    to_do: NotRequired[BlocksCreateParamsChildrenItemToDo]
    toggle: NotRequired[BlocksCreateParamsChildrenItemToggle]
    code: NotRequired[BlocksCreateParamsChildrenItemCode]
    quote: NotRequired[BlocksCreateParamsChildrenItemQuote]
    callout: NotRequired[BlocksCreateParamsChildrenItemCallout]
    divider: NotRequired[dict[str, Any]]
    bookmark: NotRequired[BlocksCreateParamsChildrenItemBookmark]
    embed: NotRequired[BlocksCreateParamsChildrenItemEmbed]
    equation: NotRequired[BlocksCreateParamsChildrenItemEquation]
    table_of_contents: NotRequired[BlocksCreateParamsChildrenItemTableOfContents]
    image: NotRequired[BlocksCreateParamsChildrenItemImage]
    video: NotRequired[BlocksCreateParamsChildrenItemVideo]
    file: NotRequired[BlocksCreateParamsChildrenItemFile]
    pdf: NotRequired[BlocksCreateParamsChildrenItemPdf]
    audio: NotRequired[BlocksCreateParamsChildrenItemAudio]

class BlocksUpdateParamsParagraphRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsParagraphRichTextItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsParagraphRichTextItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsParagraphRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsParagraphRichTextItemTextLink | None]

class BlocksUpdateParamsParagraphRichTextItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsParagraphRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsParagraphRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsParagraphRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsParagraphRichTextItem(TypedDict):
    """Nested schema for BlocksUpdateParamsParagraph.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsParagraphRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsParagraphRichTextItemEquation]
    annotations: NotRequired[BlocksUpdateParamsParagraphRichTextItemAnnotations]

class BlocksUpdateParamsParagraph(TypedDict):
    """Updated paragraph content"""
    rich_text: NotRequired[list[BlocksUpdateParamsParagraphRichTextItem]]
    color: NotRequired[str]

class BlocksUpdateParamsHeading1RichTextItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading1RichTextItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsHeading1RichTextItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading1RichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsHeading1RichTextItemTextLink | None]

class BlocksUpdateParamsHeading1RichTextItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading1RichTextItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsHeading1RichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading1RichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsHeading1RichTextItem(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading1.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsHeading1RichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsHeading1RichTextItemEquation]
    annotations: NotRequired[BlocksUpdateParamsHeading1RichTextItemAnnotations]

class BlocksUpdateParamsHeading1(TypedDict):
    """Updated heading 1 content"""
    rich_text: NotRequired[list[BlocksUpdateParamsHeading1RichTextItem]]
    color: NotRequired[str]
    is_toggleable: NotRequired[bool]

class BlocksUpdateParamsHeading2RichTextItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading2RichTextItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsHeading2RichTextItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading2RichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsHeading2RichTextItemTextLink | None]

class BlocksUpdateParamsHeading2RichTextItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading2RichTextItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsHeading2RichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading2RichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsHeading2RichTextItem(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading2.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsHeading2RichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsHeading2RichTextItemEquation]
    annotations: NotRequired[BlocksUpdateParamsHeading2RichTextItemAnnotations]

class BlocksUpdateParamsHeading2(TypedDict):
    """Updated heading 2 content"""
    rich_text: NotRequired[list[BlocksUpdateParamsHeading2RichTextItem]]
    color: NotRequired[str]
    is_toggleable: NotRequired[bool]

class BlocksUpdateParamsHeading3RichTextItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading3RichTextItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsHeading3RichTextItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading3RichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsHeading3RichTextItemTextLink | None]

class BlocksUpdateParamsHeading3RichTextItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading3RichTextItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsHeading3RichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading3RichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsHeading3RichTextItem(TypedDict):
    """Nested schema for BlocksUpdateParamsHeading3.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsHeading3RichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsHeading3RichTextItemEquation]
    annotations: NotRequired[BlocksUpdateParamsHeading3RichTextItemAnnotations]

class BlocksUpdateParamsHeading3(TypedDict):
    """Updated heading 3 content"""
    rich_text: NotRequired[list[BlocksUpdateParamsHeading3RichTextItem]]
    color: NotRequired[str]
    is_toggleable: NotRequired[bool]

class BlocksUpdateParamsBulletedListItemRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsBulletedListItemRichTextItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsBulletedListItemRichTextItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsBulletedListItemRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsBulletedListItemRichTextItemTextLink | None]

class BlocksUpdateParamsBulletedListItemRichTextItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsBulletedListItemRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsBulletedListItemRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsBulletedListItemRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsBulletedListItemRichTextItem(TypedDict):
    """Nested schema for BlocksUpdateParamsBulletedListItem.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsBulletedListItemRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsBulletedListItemRichTextItemEquation]
    annotations: NotRequired[BlocksUpdateParamsBulletedListItemRichTextItemAnnotations]

class BlocksUpdateParamsBulletedListItem(TypedDict):
    """Updated bulleted list item"""
    rich_text: NotRequired[list[BlocksUpdateParamsBulletedListItemRichTextItem]]
    color: NotRequired[str]

class BlocksUpdateParamsNumberedListItemRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsNumberedListItemRichTextItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsNumberedListItemRichTextItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsNumberedListItemRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsNumberedListItemRichTextItemTextLink | None]

class BlocksUpdateParamsNumberedListItemRichTextItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsNumberedListItemRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsNumberedListItemRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsNumberedListItemRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsNumberedListItemRichTextItem(TypedDict):
    """Nested schema for BlocksUpdateParamsNumberedListItem.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsNumberedListItemRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsNumberedListItemRichTextItemEquation]
    annotations: NotRequired[BlocksUpdateParamsNumberedListItemRichTextItemAnnotations]

class BlocksUpdateParamsNumberedListItem(TypedDict):
    """Updated numbered list item"""
    rich_text: NotRequired[list[BlocksUpdateParamsNumberedListItemRichTextItem]]
    color: NotRequired[str]

class BlocksUpdateParamsToDoRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsToDoRichTextItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsToDoRichTextItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsToDoRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsToDoRichTextItemTextLink | None]

class BlocksUpdateParamsToDoRichTextItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsToDoRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsToDoRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsToDoRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsToDoRichTextItem(TypedDict):
    """Nested schema for BlocksUpdateParamsToDo.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsToDoRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsToDoRichTextItemEquation]
    annotations: NotRequired[BlocksUpdateParamsToDoRichTextItemAnnotations]

class BlocksUpdateParamsToDo(TypedDict):
    """Updated to-do content"""
    rich_text: NotRequired[list[BlocksUpdateParamsToDoRichTextItem]]
    checked: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsToggleRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsToggleRichTextItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsToggleRichTextItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsToggleRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsToggleRichTextItemTextLink | None]

class BlocksUpdateParamsToggleRichTextItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsToggleRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsToggleRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsToggleRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsToggleRichTextItem(TypedDict):
    """Nested schema for BlocksUpdateParamsToggle.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsToggleRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsToggleRichTextItemEquation]
    annotations: NotRequired[BlocksUpdateParamsToggleRichTextItemAnnotations]

class BlocksUpdateParamsToggle(TypedDict):
    """Updated toggle content"""
    rich_text: NotRequired[list[BlocksUpdateParamsToggleRichTextItem]]
    color: NotRequired[str]

class BlocksUpdateParamsCodeRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsCodeRichTextItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsCodeRichTextItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsCodeRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsCodeRichTextItemTextLink | None]

class BlocksUpdateParamsCodeRichTextItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsCodeRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsCodeRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsCodeRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsCodeRichTextItem(TypedDict):
    """Nested schema for BlocksUpdateParamsCode.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsCodeRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsCodeRichTextItemEquation]
    annotations: NotRequired[BlocksUpdateParamsCodeRichTextItemAnnotations]

class BlocksUpdateParamsCodeCaptionItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsCodeCaptionItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsCodeCaptionItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsCodeCaptionItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsCodeCaptionItemTextLink | None]

class BlocksUpdateParamsCodeCaptionItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsCodeCaptionItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsCodeCaptionItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsCodeCaptionItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsCodeCaptionItem(TypedDict):
    """Nested schema for BlocksUpdateParamsCode.caption_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsCodeCaptionItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsCodeCaptionItemEquation]
    annotations: NotRequired[BlocksUpdateParamsCodeCaptionItemAnnotations]

class BlocksUpdateParamsCode(TypedDict):
    """Updated code block content"""
    rich_text: NotRequired[list[BlocksUpdateParamsCodeRichTextItem]]
    language: NotRequired[str]
    caption: NotRequired[list[BlocksUpdateParamsCodeCaptionItem]]

class BlocksUpdateParamsQuoteRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsQuoteRichTextItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsQuoteRichTextItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsQuoteRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsQuoteRichTextItemTextLink | None]

class BlocksUpdateParamsQuoteRichTextItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsQuoteRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsQuoteRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsQuoteRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsQuoteRichTextItem(TypedDict):
    """Nested schema for BlocksUpdateParamsQuote.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsQuoteRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsQuoteRichTextItemEquation]
    annotations: NotRequired[BlocksUpdateParamsQuoteRichTextItemAnnotations]

class BlocksUpdateParamsQuote(TypedDict):
    """Updated quote content"""
    rich_text: NotRequired[list[BlocksUpdateParamsQuoteRichTextItem]]
    color: NotRequired[str]

class BlocksUpdateParamsCalloutRichTextItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsCalloutRichTextItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsCalloutRichTextItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsCalloutRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsCalloutRichTextItemTextLink | None]

class BlocksUpdateParamsCalloutRichTextItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsCalloutRichTextItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsCalloutRichTextItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsCalloutRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsCalloutRichTextItem(TypedDict):
    """Nested schema for BlocksUpdateParamsCallout.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsCalloutRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsCalloutRichTextItemEquation]
    annotations: NotRequired[BlocksUpdateParamsCalloutRichTextItemAnnotations]

class BlocksUpdateParamsCallout(TypedDict):
    """Updated callout content"""
    rich_text: NotRequired[list[BlocksUpdateParamsCalloutRichTextItem]]
    icon: NotRequired[dict[str, Any]]
    color: NotRequired[str]

class BlocksUpdateParamsBookmarkCaptionItemTextLink(TypedDict):
    """Nested schema for BlocksUpdateParamsBookmarkCaptionItemText.link"""
    url: NotRequired[str]

class BlocksUpdateParamsBookmarkCaptionItemText(TypedDict):
    """Nested schema for BlocksUpdateParamsBookmarkCaptionItem.text"""
    content: NotRequired[str]
    link: NotRequired[BlocksUpdateParamsBookmarkCaptionItemTextLink | None]

class BlocksUpdateParamsBookmarkCaptionItemEquation(TypedDict):
    """Nested schema for BlocksUpdateParamsBookmarkCaptionItem.equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsBookmarkCaptionItemAnnotations(TypedDict):
    """Nested schema for BlocksUpdateParamsBookmarkCaptionItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class BlocksUpdateParamsBookmarkCaptionItem(TypedDict):
    """Nested schema for BlocksUpdateParamsBookmark.caption_item"""
    type_: NotRequired[str]
    text: NotRequired[BlocksUpdateParamsBookmarkCaptionItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[BlocksUpdateParamsBookmarkCaptionItemEquation]
    annotations: NotRequired[BlocksUpdateParamsBookmarkCaptionItemAnnotations]

class BlocksUpdateParamsBookmark(TypedDict):
    """Updated bookmark"""
    url: NotRequired[str]
    caption: NotRequired[list[BlocksUpdateParamsBookmarkCaptionItem]]

class BlocksUpdateParamsEmbed(TypedDict):
    """Updated embed"""
    url: NotRequired[str]

class BlocksUpdateParamsEquation(TypedDict):
    """Updated equation"""
    expression: NotRequired[str]

class BlocksUpdateParamsImageExternal(TypedDict):
    """Nested schema for BlocksUpdateParamsImage.external"""
    url: NotRequired[str]

class BlocksUpdateParamsImageFileUpload(TypedDict):
    """Nested schema for BlocksUpdateParamsImage.file_upload"""
    id: NotRequired[str]

class BlocksUpdateParamsImage(TypedDict):
    """Media file. Use external URL or file upload."""
    type_: NotRequired[str]
    external: NotRequired[BlocksUpdateParamsImageExternal]
    file_upload: NotRequired[BlocksUpdateParamsImageFileUpload]

class BlocksUpdateParamsVideoExternal(TypedDict):
    """Nested schema for BlocksUpdateParamsVideo.external"""
    url: NotRequired[str]

class BlocksUpdateParamsVideoFileUpload(TypedDict):
    """Nested schema for BlocksUpdateParamsVideo.file_upload"""
    id: NotRequired[str]

class BlocksUpdateParamsVideo(TypedDict):
    """Media file. Use external URL or file upload."""
    type_: NotRequired[str]
    external: NotRequired[BlocksUpdateParamsVideoExternal]
    file_upload: NotRequired[BlocksUpdateParamsVideoFileUpload]

class BlocksUpdateParamsFileExternal(TypedDict):
    """Nested schema for BlocksUpdateParamsFile.external"""
    url: NotRequired[str]

class BlocksUpdateParamsFileFileUpload(TypedDict):
    """Nested schema for BlocksUpdateParamsFile.file_upload"""
    id: NotRequired[str]

class BlocksUpdateParamsFile(TypedDict):
    """Media file. Use external URL or file upload."""
    type_: NotRequired[str]
    external: NotRequired[BlocksUpdateParamsFileExternal]
    file_upload: NotRequired[BlocksUpdateParamsFileFileUpload]

class BlocksUpdateParamsPdfExternal(TypedDict):
    """Nested schema for BlocksUpdateParamsPdf.external"""
    url: NotRequired[str]

class BlocksUpdateParamsPdfFileUpload(TypedDict):
    """Nested schema for BlocksUpdateParamsPdf.file_upload"""
    id: NotRequired[str]

class BlocksUpdateParamsPdf(TypedDict):
    """Media file. Use external URL or file upload."""
    type_: NotRequired[str]
    external: NotRequired[BlocksUpdateParamsPdfExternal]
    file_upload: NotRequired[BlocksUpdateParamsPdfFileUpload]

class BlocksUpdateParamsAudioExternal(TypedDict):
    """Nested schema for BlocksUpdateParamsAudio.external"""
    url: NotRequired[str]

class BlocksUpdateParamsAudioFileUpload(TypedDict):
    """Nested schema for BlocksUpdateParamsAudio.file_upload"""
    id: NotRequired[str]

class BlocksUpdateParamsAudio(TypedDict):
    """Media file. Use external URL or file upload."""
    type_: NotRequired[str]
    external: NotRequired[BlocksUpdateParamsAudioExternal]
    file_upload: NotRequired[BlocksUpdateParamsAudioFileUpload]

class BlocksUpdateParamsTable(TypedDict):
    """Updated table properties"""
    has_column_header: NotRequired[bool]
    has_row_header: NotRequired[bool]

class CommentsCreateParamsRichTextItemTextLink(TypedDict):
    """Nested schema for CommentsCreateParamsRichTextItemText.link"""
    url: NotRequired[str]

class CommentsCreateParamsRichTextItemText(TypedDict):
    """Nested schema for CommentsCreateParamsRichTextItem.text"""
    content: NotRequired[str]
    link: NotRequired[CommentsCreateParamsRichTextItemTextLink | None]

class CommentsCreateParamsRichTextItemEquation(TypedDict):
    """Nested schema for CommentsCreateParamsRichTextItem.equation"""
    expression: NotRequired[str]

class CommentsCreateParamsRichTextItemAnnotations(TypedDict):
    """Nested schema for CommentsCreateParamsRichTextItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class CommentsCreateParamsRichTextItem(TypedDict):
    """Nested schema for CommentsCreateParams.rich_text_item"""
    type_: NotRequired[str]
    text: NotRequired[CommentsCreateParamsRichTextItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[CommentsCreateParamsRichTextItemEquation]
    annotations: NotRequired[CommentsCreateParamsRichTextItemAnnotations]

class DataSourcesUpdateParamsTitleItemTextLink(TypedDict):
    """Nested schema for DataSourcesUpdateParamsTitleItemText.link"""
    url: NotRequired[str]

class DataSourcesUpdateParamsTitleItemText(TypedDict):
    """Nested schema for DataSourcesUpdateParamsTitleItem.text"""
    content: NotRequired[str]
    link: NotRequired[DataSourcesUpdateParamsTitleItemTextLink | None]

class DataSourcesUpdateParamsTitleItemEquation(TypedDict):
    """Nested schema for DataSourcesUpdateParamsTitleItem.equation"""
    expression: NotRequired[str]

class DataSourcesUpdateParamsTitleItemAnnotations(TypedDict):
    """Nested schema for DataSourcesUpdateParamsTitleItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class DataSourcesUpdateParamsTitleItem(TypedDict):
    """Nested schema for DataSourcesUpdateParams.title_item"""
    type_: NotRequired[str]
    text: NotRequired[DataSourcesUpdateParamsTitleItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[DataSourcesUpdateParamsTitleItemEquation]
    annotations: NotRequired[DataSourcesUpdateParamsTitleItemAnnotations]

class DataSourcesUpdateParamsDescriptionItemTextLink(TypedDict):
    """Nested schema for DataSourcesUpdateParamsDescriptionItemText.link"""
    url: NotRequired[str]

class DataSourcesUpdateParamsDescriptionItemText(TypedDict):
    """Nested schema for DataSourcesUpdateParamsDescriptionItem.text"""
    content: NotRequired[str]
    link: NotRequired[DataSourcesUpdateParamsDescriptionItemTextLink | None]

class DataSourcesUpdateParamsDescriptionItemEquation(TypedDict):
    """Nested schema for DataSourcesUpdateParamsDescriptionItem.equation"""
    expression: NotRequired[str]

class DataSourcesUpdateParamsDescriptionItemAnnotations(TypedDict):
    """Nested schema for DataSourcesUpdateParamsDescriptionItem.annotations"""
    bold: NotRequired[bool]
    italic: NotRequired[bool]
    strikethrough: NotRequired[bool]
    underline: NotRequired[bool]
    code: NotRequired[bool]
    color: NotRequired[str]

class DataSourcesUpdateParamsDescriptionItem(TypedDict):
    """Nested schema for DataSourcesUpdateParams.description_item"""
    type_: NotRequired[str]
    text: NotRequired[DataSourcesUpdateParamsDescriptionItemText]
    mention: NotRequired[dict[str, Any]]
    equation: NotRequired[DataSourcesUpdateParamsDescriptionItemEquation]
    annotations: NotRequired[DataSourcesUpdateParamsDescriptionItemAnnotations]

class DataSourcesUpdateParamsIconExternal(TypedDict):
    """External URL icon (when type is external)"""
    url: NotRequired[str]

class DataSourcesUpdateParamsIconFileUpload(TypedDict):
    """Uploaded file icon (when type is file_upload)"""
    id: NotRequired[str]

class DataSourcesUpdateParamsIconCustomEmoji(TypedDict):
    """Custom emoji icon (when type is custom_emoji)"""
    id: NotRequired[str]

class DataSourcesUpdateParamsIconIcon(TypedDict):
    """Notion native icon (when type is icon)"""
    name: NotRequired[str]
    color: NotRequired[str]

class DataSourcesUpdateParamsIcon(TypedDict):
    """Icon. Supports emoji, external URL, file upload, custom emoji, and Notion native icons. Set to null to remove."""
    type_: NotRequired[str]
    emoji: NotRequired[str]
    external: NotRequired[DataSourcesUpdateParamsIconExternal]
    file_upload: NotRequired[DataSourcesUpdateParamsIconFileUpload]
    custom_emoji: NotRequired[DataSourcesUpdateParamsIconCustomEmoji]
    icon: NotRequired[DataSourcesUpdateParamsIconIcon]

class DataSourcesUpdateParamsCoverExternal(TypedDict):
    """External URL cover"""
    url: NotRequired[str]

class DataSourcesUpdateParamsCoverFileUpload(TypedDict):
    """Uploaded file cover"""
    id: NotRequired[str]

class DataSourcesUpdateParamsCover(TypedDict):
    """Cover image. Supports external URL or file upload. Set to null to remove."""
    type_: NotRequired[str]
    external: NotRequired[DataSourcesUpdateParamsCoverExternal]
    file_upload: NotRequired[DataSourcesUpdateParamsCoverFileUpload]

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

class PagesCreateParams(TypedDict):
    """Parameters for pages.create operation"""
    parent: dict[str, Any]
    properties: NotRequired[dict[str, Any]]
    children: NotRequired[list[dict[str, Any]]]
    icon: NotRequired[PagesCreateParamsIcon | None]
    cover: NotRequired[PagesCreateParamsCover | None]

class PagesGetParams(TypedDict):
    """Parameters for pages.get operation"""
    page_id: str

class PagesUpdateParams(TypedDict):
    """Parameters for pages.update operation"""
    properties: NotRequired[dict[str, Any]]
    icon: NotRequired[PagesUpdateParamsIcon | None]
    cover: NotRequired[PagesUpdateParamsCover | None]
    archived: NotRequired[bool]
    in_trash: NotRequired[bool]
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

class BlocksCreateParams(TypedDict):
    """Parameters for blocks.create operation"""
    children: list[BlocksCreateParamsChildrenItem]
    block_id: str

class BlocksGetParams(TypedDict):
    """Parameters for blocks.get operation"""
    block_id: str

class BlocksUpdateParams(TypedDict):
    """Parameters for blocks.update operation"""
    paragraph: NotRequired[BlocksUpdateParamsParagraph]
    heading_1: NotRequired[BlocksUpdateParamsHeading1]
    heading_2: NotRequired[BlocksUpdateParamsHeading2]
    heading_3: NotRequired[BlocksUpdateParamsHeading3]
    bulleted_list_item: NotRequired[BlocksUpdateParamsBulletedListItem]
    numbered_list_item: NotRequired[BlocksUpdateParamsNumberedListItem]
    to_do: NotRequired[BlocksUpdateParamsToDo]
    toggle: NotRequired[BlocksUpdateParamsToggle]
    code: NotRequired[BlocksUpdateParamsCode]
    quote: NotRequired[BlocksUpdateParamsQuote]
    callout: NotRequired[BlocksUpdateParamsCallout]
    bookmark: NotRequired[BlocksUpdateParamsBookmark]
    embed: NotRequired[BlocksUpdateParamsEmbed]
    equation: NotRequired[BlocksUpdateParamsEquation]
    image: NotRequired[BlocksUpdateParamsImage]
    video: NotRequired[BlocksUpdateParamsVideo]
    file: NotRequired[BlocksUpdateParamsFile]
    pdf: NotRequired[BlocksUpdateParamsPdf]
    audio: NotRequired[BlocksUpdateParamsAudio]
    table: NotRequired[BlocksUpdateParamsTable]
    archived: NotRequired[bool]
    block_id: str

class CommentsListParams(TypedDict):
    """Parameters for comments.list operation"""
    block_id: str
    start_cursor: NotRequired[str]
    page_size: NotRequired[int]

class CommentsCreateParams(TypedDict):
    """Parameters for comments.create operation"""
    parent: NotRequired[dict[str, Any]]
    discussion_id: NotRequired[str]
    rich_text: list[CommentsCreateParamsRichTextItem]

class DataSourcesUpdateParams(TypedDict):
    """Parameters for data_sources.update operation"""
    title: NotRequired[list[DataSourcesUpdateParamsTitleItem]]
    description: NotRequired[list[DataSourcesUpdateParamsDescriptionItem]]
    properties: NotRequired[dict[str, Any]]
    icon: NotRequired[DataSourcesUpdateParamsIcon | None]
    cover: NotRequired[DataSourcesUpdateParamsCover | None]
    archived: NotRequired[bool]
    in_trash: NotRequired[bool]
    data_source_id: str

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
    object_: dict[str, Any] | None
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
    object_: list[dict[str, Any]]
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
    object_: Any
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
    object_: str
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
    object_: AirbyteSortOrder
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
    object_: dict[str, Any] | None
    """Always user"""
    person: dict[str, Any] | None
    """Person-specific data"""
    type_: dict[str, Any] | None
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
    object_: list[dict[str, Any]]
    """Always user"""
    person: list[dict[str, Any]]
    """Person-specific data"""
    type_: list[dict[str, Any]]
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
    object_: Any
    """Always user"""
    person: Any
    """Person-specific data"""
    type_: Any
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
    object_: str
    """Always user"""
    person: str
    """Person-specific data"""
    type_: str
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
    object_: AirbyteSortOrder
    """Always user"""
    person: AirbyteSortOrder
    """Person-specific data"""
    type_: AirbyteSortOrder
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
    object_: dict[str, Any] | None
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
    object_: list[dict[str, Any]]
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
    object_: Any
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
    object_: str
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
    object_: AirbyteSortOrder
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
    object_: dict[str, Any] | None
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
    type_: dict[str, Any] | None
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
    object_: list[dict[str, Any]]
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
    type_: list[dict[str, Any]]
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
    object_: Any
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
    type_: Any
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
    object_: str
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
    type_: str
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
    object_: AirbyteSortOrder
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
    type_: AirbyteSortOrder
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


# ===== COMMENTS SEARCH TYPES =====

class CommentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering comments search queries."""
    created_by: dict[str, Any] | None
    """User who created the comment."""
    created_time: str | None
    """Date and time when the comment was created."""
    discussion_id: str | None
    """Discussion thread ID."""
    id: str | None
    """Unique identifier for the comment."""
    last_edited_time: str | None
    """Date and time when the comment was last edited."""
    object_: str | None
    """Always comment."""
    parent: dict[str, Any] | None
    """Parent of the comment."""
    rich_text: list[Any] | None
    """Content of the comment as rich text."""


class CommentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_by: list[dict[str, Any]]
    """User who created the comment."""
    created_time: list[str]
    """Date and time when the comment was created."""
    discussion_id: list[str]
    """Discussion thread ID."""
    id: list[str]
    """Unique identifier for the comment."""
    last_edited_time: list[str]
    """Date and time when the comment was last edited."""
    object_: list[str]
    """Always comment."""
    parent: list[dict[str, Any]]
    """Parent of the comment."""
    rich_text: list[list[Any]]
    """Content of the comment as rich text."""


class CommentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_by: Any
    """User who created the comment."""
    created_time: Any
    """Date and time when the comment was created."""
    discussion_id: Any
    """Discussion thread ID."""
    id: Any
    """Unique identifier for the comment."""
    last_edited_time: Any
    """Date and time when the comment was last edited."""
    object_: Any
    """Always comment."""
    parent: Any
    """Parent of the comment."""
    rich_text: Any
    """Content of the comment as rich text."""


class CommentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    created_by: str
    """User who created the comment."""
    created_time: str
    """Date and time when the comment was created."""
    discussion_id: str
    """Discussion thread ID."""
    id: str
    """Unique identifier for the comment."""
    last_edited_time: str
    """Date and time when the comment was last edited."""
    object_: str
    """Always comment."""
    parent: str
    """Parent of the comment."""
    rich_text: str
    """Content of the comment as rich text."""


class CommentsSortFilter(TypedDict, total=False):
    """Available fields for sorting comments search results."""
    created_by: AirbyteSortOrder
    """User who created the comment."""
    created_time: AirbyteSortOrder
    """Date and time when the comment was created."""
    discussion_id: AirbyteSortOrder
    """Discussion thread ID."""
    id: AirbyteSortOrder
    """Unique identifier for the comment."""
    last_edited_time: AirbyteSortOrder
    """Date and time when the comment was last edited."""
    object_: AirbyteSortOrder
    """Always comment."""
    parent: AirbyteSortOrder
    """Parent of the comment."""
    rich_text: AirbyteSortOrder
    """Content of the comment as rich text."""


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



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
