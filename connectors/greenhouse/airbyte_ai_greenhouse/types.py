"""
Type definitions for greenhouse connector.
"""
# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]

from typing import Any

# ===== RESPONSE TYPE DEFINITIONS =====

class Candidate(TypedDict):
    """Greenhouse candidate object"""
    id: NotRequired[int]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    company: NotRequired[str | None]
    title: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    last_activity: NotRequired[str]
    is_private: NotRequired[bool]
    photo_url: NotRequired[str | None]
    attachments: NotRequired[list[dict[str, Any]]]
    application_ids: NotRequired[list[int]]
    phone_numbers: NotRequired[list[dict[str, Any]]]
    addresses: NotRequired[list[dict[str, Any]]]
    email_addresses: NotRequired[list[dict[str, Any]]]
    website_addresses: NotRequired[list[dict[str, Any]]]
    social_media_addresses: NotRequired[list[dict[str, Any]]]
    recruiter: NotRequired[dict[str, Any] | None]
    coordinator: NotRequired[dict[str, Any] | None]
    can_email: NotRequired[bool]
    tags: NotRequired[list[str]]
    custom_fields: NotRequired[dict[str, Any]]

class Application(TypedDict):
    """Greenhouse application object"""
    id: NotRequired[int]
    candidate_id: NotRequired[int]
    prospect: NotRequired[bool]
    applied_at: NotRequired[str]
    rejected_at: NotRequired[str | None]
    last_activity_at: NotRequired[str]
    location: NotRequired[dict[str, Any] | None]
    source: NotRequired[dict[str, Any]]
    credited_to: NotRequired[dict[str, Any]]
    rejection_reason: NotRequired[dict[str, Any] | None]
    rejection_details: NotRequired[dict[str, Any] | None]
    jobs: NotRequired[list[dict[str, Any]]]
    job_post_id: NotRequired[int | None]
    status: NotRequired[str]
    current_stage: NotRequired[dict[str, Any] | None]
    answers: NotRequired[list[dict[str, Any]]]
    prospective_office: NotRequired[dict[str, Any] | None]
    prospective_department: NotRequired[dict[str, Any] | None]
    prospect_detail: NotRequired[dict[str, Any]]
    attachments: NotRequired[list[dict[str, Any]]]
    custom_fields: NotRequired[dict[str, Any]]

class Job(TypedDict):
    """Greenhouse job object"""
    id: NotRequired[int]
    name: NotRequired[str]
    requisition_id: NotRequired[str | None]
    notes: NotRequired[str | None]
    confidential: NotRequired[bool]
    status: NotRequired[str]
    created_at: NotRequired[str]
    opened_at: NotRequired[str]
    closed_at: NotRequired[str | None]
    updated_at: NotRequired[str]
    departments: NotRequired[list[dict[str, Any] | None]]
    offices: NotRequired[list[dict[str, Any]]]
    custom_fields: NotRequired[dict[str, Any]]
    hiring_team: NotRequired[dict[str, Any]]
    openings: NotRequired[list[dict[str, Any]]]

# ===== METADATA TYPE DEFINITIONS =====
# Meta types for operations that extract metadata (e.g., pagination info)

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
