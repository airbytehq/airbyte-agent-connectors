"""
Type definitions for google-drive connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



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

class FilesDownloadParams(TypedDict):
    """Parameters for files.download operation"""
    file_id: str
    alt: str
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
    page_token: str
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

