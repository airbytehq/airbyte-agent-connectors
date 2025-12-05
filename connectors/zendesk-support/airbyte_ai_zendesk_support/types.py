"""
Type definitions for zendesk-support connector.
"""
# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]


# ===== RESPONSE TYPE DEFINITIONS =====

class Article(TypedDict):
    """Help Center article object"""
    id: int
    url: NotRequired[str]
    html_url: NotRequired[str]
    title: NotRequired[str]
    body: NotRequired[str]
    locale: NotRequired[str]
    author_id: NotRequired[int]
    section_id: NotRequired[int]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    vote_sum: NotRequired[int]
    vote_count: NotRequired[int]
    label_names: NotRequired[list[str]]
    draft: NotRequired[bool]
    promoted: NotRequired[bool]
    position: NotRequired[int]

class ArticleList(TypedDict):
    """List of articles"""
    articles: NotRequired[list[Article]]
    count: NotRequired[int]
    next_page: NotRequired[str | None]
    previous_page: NotRequired[str | None]

class ArticleAttachment(TypedDict):
    """Article attachment object"""
    id: int
    url: NotRequired[str]
    article_id: NotRequired[int]
    file_name: str
    content_type: NotRequired[str]
    content_url: NotRequired[str]
    size: NotRequired[int]
    inline: NotRequired[bool]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]

class ArticleAttachmentList(TypedDict):
    """List of article attachments"""
    article_attachments: NotRequired[list[ArticleAttachment]]
    count: NotRequired[int]
    next_page: NotRequired[str | None]
    previous_page: NotRequired[str | None]

# ===== METADATA TYPE DEFINITIONS =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class ArticlesListParams(TypedDict):
    """Parameters for articles.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    sort_by: NotRequired[str]
    sort_order: NotRequired[str]

class ArticlesGetParams(TypedDict):
    """Parameters for articles.get operation"""
    id: str

class ArticleAttachmentsListParams(TypedDict):
    """Parameters for article_attachments.list operation"""
    article_id: str

class ArticleAttachmentsGetParams(TypedDict):
    """Parameters for article_attachments.get operation"""
    article_id: str
    attachment_id: str

class ArticleAttachmentsDownloadParams(TypedDict):
    """Parameters for article_attachments.download operation"""
    article_id: str
    attachment_id: str
    range_header: NotRequired[str]
