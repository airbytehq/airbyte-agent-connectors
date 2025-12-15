"""
Type definitions for greenhouse connector.
"""
from __future__ import annotations

# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]



# ===== NESTED PARAM TYPE DEFINITIONS =====
# Nested parameter schemas discovered during parameter extraction

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class CandidatesListParams(TypedDict):
    """Parameters for candidates.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class CandidatesGetParams(TypedDict):
    """Parameters for candidates.get operation"""
    id: str

class ApplicationsListParams(TypedDict):
    """Parameters for applications.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    created_before: NotRequired[str]
    created_after: NotRequired[str]
    last_activity_after: NotRequired[str]
    job_id: NotRequired[int]
    status: NotRequired[str]

class ApplicationsGetParams(TypedDict):
    """Parameters for applications.get operation"""
    id: str

class JobsListParams(TypedDict):
    """Parameters for jobs.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class JobsGetParams(TypedDict):
    """Parameters for jobs.get operation"""
    id: str

class OffersListParams(TypedDict):
    """Parameters for offers.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    created_before: NotRequired[str]
    created_after: NotRequired[str]
    resolved_after: NotRequired[str]

class OffersGetParams(TypedDict):
    """Parameters for offers.get operation"""
    id: str

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    created_before: NotRequired[str]
    created_after: NotRequired[str]
    updated_before: NotRequired[str]
    updated_after: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class DepartmentsListParams(TypedDict):
    """Parameters for departments.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class DepartmentsGetParams(TypedDict):
    """Parameters for departments.get operation"""
    id: str

class OfficesListParams(TypedDict):
    """Parameters for offices.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class OfficesGetParams(TypedDict):
    """Parameters for offices.get operation"""
    id: str

class JobPostsListParams(TypedDict):
    """Parameters for job_posts.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    live: NotRequired[bool]
    active: NotRequired[bool]

class JobPostsGetParams(TypedDict):
    """Parameters for job_posts.get operation"""
    id: str

class SourcesListParams(TypedDict):
    """Parameters for sources.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]

class ScheduledInterviewsListParams(TypedDict):
    """Parameters for scheduled_interviews.list operation"""
    per_page: NotRequired[int]
    page: NotRequired[int]
    created_before: NotRequired[str]
    created_after: NotRequired[str]
    updated_before: NotRequired[str]
    updated_after: NotRequired[str]
    starts_after: NotRequired[str]
    ends_before: NotRequired[str]

class ScheduledInterviewsGetParams(TypedDict):
    """Parameters for scheduled_interviews.get operation"""
    id: str

class ApplicationAttachmentDownloadParams(TypedDict):
    """Parameters for application_attachment.download operation"""
    id: str
    attachment_index: str
    range_header: NotRequired[str]

class CandidateAttachmentDownloadParams(TypedDict):
    """Parameters for candidate_attachment.download operation"""
    id: str
    attachment_index: str
    range_header: NotRequired[str]
