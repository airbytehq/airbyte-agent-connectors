"""
Type definitions for google-drive connector.
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

class FilesListParams(TypedDict):
    """Parameters for files.list operation"""
    page_size: NotRequired[int]
    page_token: NotRequired[str]
    q: NotRequired[str]
    order_by: NotRequired[str]
    fields: NotRequired[str]
    spaces: NotRequired[str]
    corpora: NotRequired[str]
    drive_id: NotRequired[str]
    include_items_from_all_drives: NotRequired[bool]
    supports_all_drives: NotRequired[bool]

class FilesGetParams(TypedDict):
    """Parameters for files.get operation"""
    file_id: str
    fields: NotRequired[str]
    supports_all_drives: NotRequired[bool]

class FilesCreateParams(TypedDict):
    """Parameters for files.create operation"""
    name: str
    mime_type: NotRequired[str]
    parents: NotRequired[list[str]]
    description: NotRequired[str]

class FilesUpdateParams(TypedDict):
    """Parameters for files.update operation"""
    name: NotRequired[str]
    description: NotRequired[str]
    mime_type: NotRequired[str]
    file_id: str
    add_parents: NotRequired[str]
    remove_parents: NotRequired[str]
    supports_all_drives: NotRequired[bool]

class FilesDeleteParams(TypedDict):
    """Parameters for files.delete operation"""
    file_id: str
    supports_all_drives: NotRequired[bool]

class FilesUploadCreateParams(TypedDict):
    """Parameters for files_upload.create operation"""
    name: str
    file_content: str
    mime_type: NotRequired[str]
    parents: NotRequired[list[str]]
    description: NotRequired[str]
    file_mime_type: NotRequired[str]
    upload_type: NotRequired[str]
    supports_all_drives: NotRequired[bool]

class FilesDownloadParams(TypedDict):
    """Parameters for files.download operation"""
    file_id: str
    alt: NotRequired[str]
    acknowledge_abuse: NotRequired[bool]
    supports_all_drives: NotRequired[bool]
    range_header: NotRequired[str]

class FilesExportDownloadParams(TypedDict):
    """Parameters for files_export.download operation"""
    file_id: str
    mime_type: str
    range_header: NotRequired[str]

class DrivesListParams(TypedDict):
    """Parameters for drives.list operation"""
    page_size: NotRequired[int]
    page_token: NotRequired[str]
    q: NotRequired[str]
    use_domain_admin_access: NotRequired[bool]

class DrivesGetParams(TypedDict):
    """Parameters for drives.get operation"""
    drive_id: str
    use_domain_admin_access: NotRequired[bool]

class PermissionsListParams(TypedDict):
    """Parameters for permissions.list operation"""
    file_id: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]
    supports_all_drives: NotRequired[bool]
    use_domain_admin_access: NotRequired[bool]

class PermissionsGetParams(TypedDict):
    """Parameters for permissions.get operation"""
    file_id: str
    permission_id: str
    supports_all_drives: NotRequired[bool]
    use_domain_admin_access: NotRequired[bool]

class CommentsListParams(TypedDict):
    """Parameters for comments.list operation"""
    file_id: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]
    start_modified_time: NotRequired[str]
    include_deleted: NotRequired[bool]
    fields: NotRequired[str]

class CommentsGetParams(TypedDict):
    """Parameters for comments.get operation"""
    file_id: str
    comment_id: str
    include_deleted: NotRequired[bool]
    fields: NotRequired[str]

class RepliesListParams(TypedDict):
    """Parameters for replies.list operation"""
    file_id: str
    comment_id: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]
    include_deleted: NotRequired[bool]
    fields: NotRequired[str]

class RepliesGetParams(TypedDict):
    """Parameters for replies.get operation"""
    file_id: str
    comment_id: str
    reply_id: str
    include_deleted: NotRequired[bool]
    fields: NotRequired[str]

class RevisionsListParams(TypedDict):
    """Parameters for revisions.list operation"""
    file_id: str
    page_size: NotRequired[int]
    page_token: NotRequired[str]

class RevisionsGetParams(TypedDict):
    """Parameters for revisions.get operation"""
    file_id: str
    revision_id: str

class ChangesListParams(TypedDict):
    """Parameters for changes.list operation"""
    page_token: NotRequired[str]
    page_size: NotRequired[int]
    drive_id: NotRequired[str]
    include_items_from_all_drives: NotRequired[bool]
    supports_all_drives: NotRequired[bool]
    spaces: NotRequired[str]
    include_removed: NotRequired[bool]
    restrict_to_my_drive: NotRequired[bool]

class ChangesStartPageTokenGetParams(TypedDict):
    """Parameters for changes_start_page_token.get operation"""
    drive_id: NotRequired[str]
    supports_all_drives: NotRequired[bool]

class AboutGetParams(TypedDict):
    """Parameters for about.get operation"""
    fields: NotRequired[str]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== FILES SEARCH TYPES =====

class FilesSearchFilter(TypedDict, total=False):
    """Available fields for filtering files search queries."""
    id: str | None
    """Unique identifier of the file in Google Drive."""
    updated_at: str | None
    """Timestamp of the last modification to the file."""
    file_name: str | None
    """Name of the file."""
    file_path: str | None
    """Full path of the file within the synced Drive folder."""
    mime_type: str | None
    """MIME type of the file."""
    content: str | None
    """Extracted text content of the file."""


class FilesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    id: list[str]
    """Unique identifier of the file in Google Drive."""
    updated_at: list[str]
    """Timestamp of the last modification to the file."""
    file_name: list[str]
    """Name of the file."""
    file_path: list[str]
    """Full path of the file within the synced Drive folder."""
    mime_type: list[str]
    """MIME type of the file."""
    content: list[str]
    """Extracted text content of the file."""


class FilesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    id: Any
    """Unique identifier of the file in Google Drive."""
    updated_at: Any
    """Timestamp of the last modification to the file."""
    file_name: Any
    """Name of the file."""
    file_path: Any
    """Full path of the file within the synced Drive folder."""
    mime_type: Any
    """MIME type of the file."""
    content: Any
    """Extracted text content of the file."""


class FilesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    id: str
    """Unique identifier of the file in Google Drive."""
    updated_at: str
    """Timestamp of the last modification to the file."""
    file_name: str
    """Name of the file."""
    file_path: str
    """Full path of the file within the synced Drive folder."""
    mime_type: str
    """MIME type of the file."""
    content: str
    """Extracted text content of the file."""


class FilesSortFilter(TypedDict, total=False):
    """Available fields for sorting files search results."""
    id: AirbyteSortOrder
    """Unique identifier of the file in Google Drive."""
    updated_at: AirbyteSortOrder
    """Timestamp of the last modification to the file."""
    file_name: AirbyteSortOrder
    """Name of the file."""
    file_path: AirbyteSortOrder
    """Full path of the file within the synced Drive folder."""
    mime_type: AirbyteSortOrder
    """MIME type of the file."""
    content: AirbyteSortOrder
    """Extracted text content of the file."""


# Entity-specific condition types for files
class FilesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: FilesSearchFilter


class FilesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: FilesSearchFilter


class FilesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: FilesSearchFilter


class FilesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: FilesSearchFilter


class FilesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: FilesSearchFilter


class FilesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: FilesSearchFilter


class FilesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: FilesStringFilter


class FilesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: FilesStringFilter


class FilesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: FilesStringFilter


class FilesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: FilesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
FilesInCondition = TypedDict("FilesInCondition", {"in": FilesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

FilesNotCondition = TypedDict("FilesNotCondition", {"not": "FilesCondition"}, total=False)
"""Negates the nested condition."""

FilesAndCondition = TypedDict("FilesAndCondition", {"and": "list[FilesCondition]"}, total=False)
"""True if all nested conditions are true."""

FilesOrCondition = TypedDict("FilesOrCondition", {"or": "list[FilesCondition]"}, total=False)
"""True if any nested condition is true."""

FilesAnyCondition = TypedDict("FilesAnyCondition", {"any": FilesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all files condition types
FilesCondition = (
    FilesEqCondition
    | FilesNeqCondition
    | FilesGtCondition
    | FilesGteCondition
    | FilesLtCondition
    | FilesLteCondition
    | FilesInCondition
    | FilesLikeCondition
    | FilesFuzzyCondition
    | FilesKeywordCondition
    | FilesContainsCondition
    | FilesNotCondition
    | FilesAndCondition
    | FilesOrCondition
    | FilesAnyCondition
)


class FilesSearchQuery(TypedDict, total=False):
    """Search query for files entity."""
    filter: FilesCondition
    sort: list[FilesSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
