"""
Pydantic models for greenhouse connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class GreenhouseAuthConfig(BaseModel):
    """Harvest API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Greenhouse Harvest API Key from the Dev Center"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Attachment(BaseModel):
    """File attachment (resume, cover letter, etc.)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    filename: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)

class Candidate(BaseModel):
    """Greenhouse candidate object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    first_name: Union[str, Any] = Field(default=None)
    last_name: Union[str, Any] = Field(default=None)
    company: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    last_activity: Union[str, Any] = Field(default=None)
    is_private: Union[bool, Any] = Field(default=None)
    photo_url: Union[str | None, Any] = Field(default=None)
    attachments: Union[list[Attachment], Any] = Field(default=None)
    application_ids: Union[list[int], Any] = Field(default=None)
    phone_numbers: Union[list[dict[str, Any]], Any] = Field(default=None)
    addresses: Union[list[dict[str, Any]], Any] = Field(default=None)
    email_addresses: Union[list[dict[str, Any]], Any] = Field(default=None)
    website_addresses: Union[list[dict[str, Any]], Any] = Field(default=None)
    social_media_addresses: Union[list[dict[str, Any]], Any] = Field(default=None)
    recruiter: Union[dict[str, Any] | None, Any] = Field(default=None)
    coordinator: Union[dict[str, Any] | None, Any] = Field(default=None)
    can_email: Union[bool, Any] = Field(default=None)
    tags: Union[list[str], Any] = Field(default=None)
    custom_fields: Union[dict[str, Any], Any] = Field(default=None)

class Application(BaseModel):
    """Greenhouse application object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    candidate_id: Union[int, Any] = Field(default=None)
    prospect: Union[bool, Any] = Field(default=None)
    applied_at: Union[str, Any] = Field(default=None)
    rejected_at: Union[str | None, Any] = Field(default=None)
    last_activity_at: Union[str, Any] = Field(default=None)
    location: Union[dict[str, Any] | None, Any] = Field(default=None)
    source: Union[dict[str, Any], Any] = Field(default=None)
    credited_to: Union[dict[str, Any], Any] = Field(default=None)
    rejection_reason: Union[dict[str, Any] | None, Any] = Field(default=None)
    rejection_details: Union[dict[str, Any] | None, Any] = Field(default=None)
    jobs: Union[list[dict[str, Any]], Any] = Field(default=None)
    job_post_id: Union[int | None, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    current_stage: Union[dict[str, Any] | None, Any] = Field(default=None)
    answers: Union[list[dict[str, Any]], Any] = Field(default=None)
    prospective_office: Union[dict[str, Any] | None, Any] = Field(default=None)
    prospective_department: Union[dict[str, Any] | None, Any] = Field(default=None)
    prospect_detail: Union[dict[str, Any], Any] = Field(default=None)
    attachments: Union[list[Attachment], Any] = Field(default=None)
    custom_fields: Union[dict[str, Any], Any] = Field(default=None)

class Job(BaseModel):
    """Greenhouse job object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    requisition_id: Union[str | None, Any] = Field(default=None)
    notes: Union[str | None, Any] = Field(default=None)
    confidential: Union[bool, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    opened_at: Union[str, Any] = Field(default=None)
    closed_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    departments: Union[list[dict[str, Any] | None], Any] = Field(default=None)
    offices: Union[list[dict[str, Any]], Any] = Field(default=None)
    custom_fields: Union[dict[str, Any], Any] = Field(default=None)
    hiring_team: Union[dict[str, Any], Any] = Field(default=None)
    openings: Union[list[dict[str, Any]], Any] = Field(default=None)

class Offer(BaseModel):
    """Greenhouse offer object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    version: Union[int, Any] = Field(default=None)
    application_id: Union[int, Any] = Field(default=None)
    job_id: Union[int, Any] = Field(default=None)
    candidate_id: Union[int, Any] = Field(default=None)
    opening: Union[dict[str, Any] | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    sent_at: Union[str | None, Any] = Field(default=None)
    resolved_at: Union[str | None, Any] = Field(default=None)
    starts_at: Union[str | None, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    custom_fields: Union[dict[str, Any], Any] = Field(default=None)

class User(BaseModel):
    """Greenhouse user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    first_name: Union[str, Any] = Field(default=None)
    last_name: Union[str, Any] = Field(default=None)
    primary_email_address: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    disabled: Union[bool, Any] = Field(default=None)
    site_admin: Union[bool, Any] = Field(default=None)
    emails: Union[list[str], Any] = Field(default=None)
    employee_id: Union[str | None, Any] = Field(default=None)
    linked_candidate_ids: Union[list[int], Any] = Field(default=None)
    offices: Union[list[dict[str, Any]], Any] = Field(default=None)
    departments: Union[list[dict[str, Any]], Any] = Field(default=None)

class Department(BaseModel):
    """Greenhouse department object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    parent_id: Union[int | None, Any] = Field(default=None)
    parent_department_external_id: Union[str | None, Any] = Field(default=None)
    child_ids: Union[list[int], Any] = Field(default=None)
    child_department_external_ids: Union[list[str], Any] = Field(default=None)
    external_id: Union[str | None, Any] = Field(default=None)

class Office(BaseModel):
    """Greenhouse office object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    location: Union[dict[str, Any] | None, Any] = Field(default=None)
    primary_contact_user_id: Union[int | None, Any] = Field(default=None)
    parent_id: Union[int | None, Any] = Field(default=None)
    parent_office_external_id: Union[str | None, Any] = Field(default=None)
    child_ids: Union[list[int], Any] = Field(default=None)
    child_office_external_ids: Union[list[str], Any] = Field(default=None)
    external_id: Union[str | None, Any] = Field(default=None)

class JobPost(BaseModel):
    """Greenhouse job post object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    location: Union[dict[str, Any] | None, Any] = Field(default=None)
    internal: Union[bool, Any] = Field(default=None)
    external: Union[bool, Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    live: Union[bool, Any] = Field(default=None)
    first_published_at: Union[str | None, Any] = Field(default=None)
    job_id: Union[int, Any] = Field(default=None)
    content: Union[str | None, Any] = Field(default=None)
    internal_content: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    demographic_question_set_id: Union[int | None, Any] = Field(default=None)
    questions: Union[list[dict[str, Any]], Any] = Field(default=None)

class Source(BaseModel):
    """Greenhouse source object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    type: Union[dict[str, Any] | None, Any] = Field(default=None)

class ScheduledInterview(BaseModel):
    """Greenhouse scheduled interview object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int, Any] = Field(default=None)
    application_id: Union[int, Any] = Field(default=None)
    external_event_id: Union[str | None, Any] = Field(default=None)
    created_at: Union[str, Any] = Field(default=None)
    updated_at: Union[str, Any] = Field(default=None)
    start: Union[dict[str, Any] | None, Any] = Field(default=None)
    end: Union[dict[str, Any] | None, Any] = Field(default=None)
    location: Union[str | None, Any] = Field(default=None)
    video_conferencing_url: Union[str | None, Any] = Field(default=None)
    status: Union[str, Any] = Field(default=None)
    interview: Union[dict[str, Any] | None, Any] = Field(default=None)
    organizer: Union[dict[str, Any] | None, Any] = Field(default=None)
    interviewers: Union[list[dict[str, Any]], Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== RESPONSE ENVELOPE MODELS =====

# Type variables for generic envelope models
T = TypeVar('T')
S = TypeVar('S')


class GreenhouseExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class GreenhouseExecuteResultWithMeta(GreenhouseExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

