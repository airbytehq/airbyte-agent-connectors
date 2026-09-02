"""
Pydantic models for greenhouse connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""
# ruff: noqa: E501

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
from typing import Optional

# Authentication configuration

class GreenhouseAuthConfig(BaseModel):
    """Greenhouse OAuth 2.0"""

    model_config = ConfigDict(extra="forbid")

    client_id: str
    """Client ID from the Greenhouse OAuth application"""
    client_secret: str
    """Client secret from the Greenhouse OAuth application"""
    refresh_token: str
    """Refresh token generated through the Greenhouse OAuth consent flow"""
    access_token: Optional[str] = None
    """Access token generated through the Greenhouse OAuth consent flow (optional if refresh_token is provided)"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class CandidateSocialMediaAddressesItem(BaseModel):
    """Nested schema for Candidate.social_media_addresses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: str | None | None = Field(default=None)

class CandidateWebsiteAddressesItem(BaseModel):
    """Nested schema for Candidate.website_addresses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    value: str | None | None = Field(default=None)

class CandidateCustomFields(BaseModel):
    """Nested schema for Candidate.custom_fields"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    value: Any | None = Field(default=None)

class CandidatePhoneNumbersItem(BaseModel):
    """Nested schema for Candidate.phone_numbers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    value: str | None | None = Field(default=None)

class CandidateEmailAddressesItem(BaseModel):
    """Nested schema for Candidate.email_addresses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    value: str | None | None = Field(default=None)

class CandidateAddressesItem(BaseModel):
    """Nested schema for Candidate.addresses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    value: str | None | None = Field(default=None)

class Candidate(BaseModel):
    """Greenhouse candidate object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    addresses: list[CandidateAddressesItem | None] | None = Field(default=None)
    can_email: bool | None = Field(default=None)
    company: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    custom_fields: dict[str, CandidateCustomFields] | None = Field(default=None)
    email_addresses: list[CandidateEmailAddressesItem | None] | None = Field(default=None)
    first_name: str | None = Field(default=None)
    id: int | None = Field(default=None)
    last_activity_at: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    linked_user_ids: list[int | None] | None = Field(default=None)
    phone_numbers: list[CandidatePhoneNumbersItem | None] | None = Field(default=None)
    preferred_name: str | None = Field(default=None)
    private: bool | None = Field(default=None)
    social_media_addresses: list[CandidateSocialMediaAddressesItem | None] | None = Field(default=None)
    tags: list[str | None] | None = Field(default=None)
    time_zone: str | None = Field(default=None)
    title: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    website_addresses: list[CandidateWebsiteAddressesItem | None] | None = Field(default=None)

class ApplicationCustomFields(BaseModel):
    """Nested schema for Application.custom_fields"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    value: Any | None = Field(default=None)

class ApplicationAnswersItem(BaseModel):
    """Nested schema for Application.answers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    answer: str | None | None = Field(default=None, description="Candidate's free-text answer to the question.")
    """Candidate's free-text answer to the question."""
    question: str | None | None = Field(default=None, description="Application-form question the candidate answered.")
    """Application-form question the candidate answered."""

class Application(BaseModel):
    """Greenhouse application object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    agency_note_id: int | None = Field(default=None)
    answers: list[ApplicationAnswersItem | None] | None = Field(default=None)
    candidate_id: int | None = Field(default=None)
    coordinator_id: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    custom_fields: dict[str, ApplicationCustomFields] | None = Field(default=None)
    id: int | None = Field(default=None)
    job_id: int | None = Field(default=None)
    job_interview_stage_id: int | None = Field(default=None)
    job_post_id: int | None = Field(default=None)
    last_activity_at: str | None = Field(default=None)
    location_address: str | None = Field(default=None)
    needs_decision: bool | None = Field(default=None)
    prospect: bool | None = Field(default=None)
    prospective_job_ids: list[int | None] | None = Field(default=None)
    recruiter_id: int | None = Field(default=None)
    referrer_id: int | None = Field(default=None)
    rejected_at: str | None = Field(default=None)
    rejection_reason_id: int | None = Field(default=None)
    source_id: int | None = Field(default=None)
    stage_id: int | None = Field(default=None)
    stage_name: str | None = Field(default=None)
    status: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class JobCustomFields(BaseModel):
    """Nested schema for Job.custom_fields"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    value: Any | None = Field(default=None)

class Job(BaseModel):
    """Greenhouse job object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    closed_at: str | None = Field(default=None)
    confidential: bool | None = Field(default=None)
    copied_from_id: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    custom_fields: dict[str, JobCustomFields] | None = Field(default=None)
    department_id: int | None = Field(default=None)
    id: int | None = Field(default=None)
    is_template: bool | None = Field(default=None)
    name: str | None = Field(default=None)
    notes: str | None = Field(default=None)
    office_ids: list[int | None] | None = Field(default=None)
    opened_at: str | None = Field(default=None)
    requisition_id: str | None = Field(default=None)
    status: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class OfferCustomFields(BaseModel):
    """Nested schema for Offer.custom_fields"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    value: Any | None = Field(default=None)

class Offer(BaseModel):
    """Greenhouse offer object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    application_id: int | None = Field(default=None)
    candidate_id: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    custom_fields: dict[str, OfferCustomFields] | None = Field(default=None)
    id: int | None = Field(default=None)
    job_id: int | None = Field(default=None)
    opening_id: int | None = Field(default=None)
    resolved_at: str | None = Field(default=None)
    sent_on: str | None = Field(default=None)
    starts_on: str | None = Field(default=None)
    status: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    version: int | None = Field(default=None)

class UserInterviewerTagsItem(BaseModel):
    """Nested schema for User.interviewer_tags_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None)
    name: str | None | None = Field(default=None)

class UserCustomFields(BaseModel):
    """Nested schema for User.custom_fields"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    value: Any | None = Field(default=None)

class User(BaseModel):
    """Greenhouse user object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    agency_id: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    custom_fields: dict[str, UserCustomFields] | None = Field(default=None)
    deactivated: bool | None = Field(default=None)
    department_ids: list[int | None] | None = Field(default=None)
    emails: list[str | None] | None = Field(default=None)
    employee_id: str | None = Field(default=None)
    first_name: str | None = Field(default=None)
    id: int | None = Field(default=None)
    interviewer_tags: list[UserInterviewerTagsItem | None] | None = Field(default=None)
    job_title: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    linked_candidate_ids: list[int | None] | None = Field(default=None)
    name: str | None = Field(default=None)
    office_ids: list[int | None] | None = Field(default=None)
    primary_email: str | None = Field(default=None)
    site_admin: bool | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class Department(BaseModel):
    """Greenhouse department object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str | None = Field(default=None)
    external_id: str | None = Field(default=None)
    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    parent_id: int | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class Office(BaseModel):
    """Greenhouse office object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str | None = Field(default=None)
    external_id: str | None = Field(default=None)
    id: int | None = Field(default=None)
    location: str | None = Field(default=None)
    name: str | None = Field(default=None)
    parent_id: int | None = Field(default=None)
    primary_in_house_contact_user_id: int | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class JobPostQuestionsItemOptionsItem(BaseModel):
    """Nested schema for JobPostQuestionsItem.options_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="Id of the option, stable across edits to the option label.")
    """Id of the option, stable across edits to the option label."""
    label: str | None | None = Field(default=None, description="Human-readable text shown to the candidate for this option.")
    """Human-readable text shown to the candidate for this option."""

class JobPostQuestionsItem(BaseModel):
    """Nested schema for JobPost.questions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    answer_type: str | None | None = Field(default=None, description="Input type the candidate uses to answer. `short_text` and `long_text` are free-text inputs, `single_select` and `multi_select` use the `options` array, `boolean` is a yes/no, `attachment` accepts a file upload, and `hidden` is set programmatically without rendering a field.")
    """Input type the candidate uses to answer. `short_text` and `long_text` are free-text inputs, `single_select` and `multi_select` use the `options` array, `boolean` is a yes/no, `attachment` accepts a file upload, and `hidden` is set programmatically without rendering a field."""
    description: str | None | None = Field(default=None, description="Help text shown below the question label to give candidates additional context. `null` when no help text is set.")
    """Help text shown below the question label to give candidates additional context. `null` when no help text is set."""
    id: int | None | None = Field(default=None, description="Id of the question. `null` for default questions that are rendered from configuration rather than persisted per post (e.g. the built-in `first_name` field).")
    """Id of the question. `null` for default questions that are rendered from configuration rather than persisted per post (e.g. the built-in `first_name` field)."""
    label: str | None | None = Field(default=None, description="Human-readable label rendered above the input on the application form.")
    """Human-readable label rendered above the input on the application form."""
    name: str | None | None = Field(default=None, description="Stable form-field name used when submitting an application (e.g. `question_42` for a custom question, `first_name` for a default field). Use this when mapping responses back to a question.")
    """Stable form-field name used when submitting an application (e.g. `question_42` for a custom question, `first_name` for a default field). Use this when mapping responses back to a question."""
    options: list[JobPostQuestionsItemOptionsItem | None] | None | None = Field(default=None, description="Selectable answer options for `single_select` and `multi_select` questions. Empty for other answer types.")
    """Selectable answer options for `single_select` and `multi_select` questions. Empty for other answer types."""
    private: bool | None | None = Field(default=None, description="If `true`, answers to this question are visible only to users with explicit access (e.g. private notes, API-only questions). Defaults to `false`.")
    """If `true`, answers to this question are visible only to users with explicit access (e.g. private notes, API-only questions). Defaults to `false`."""
    required: bool | None | None = Field(default=None, description="If `true`, the candidate must answer this question to submit the application. `null` for default questions whose required-ness is driven by board-level configuration.")
    """If `true`, the candidate must answer this question to submit the application. `null` for default questions whose required-ness is driven by board-level configuration."""

class JobPost(BaseModel):
    """Greenhouse job post object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active: bool | None = Field(default=None)
    content: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    demographic_question_set_id: int | None = Field(default=None)
    featured: bool | None = Field(default=None)
    first_published_at: str | None = Field(default=None)
    id: int | None = Field(default=None)
    internal: bool | None = Field(default=None)
    internal_content: str | None = Field(default=None)
    job_board_id: int | None = Field(default=None)
    job_id: int | None = Field(default=None)
    language: str | None = Field(default=None)
    live: bool | None = Field(default=None)
    public_url: str | None = Field(default=None)
    questions: list[JobPostQuestionsItem | None] | None = Field(default=None)
    title: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

class SourceType(BaseModel):
    """The sourcing strategy this source rolls up to — the broader category used for reporting. Sources are grouped under sourcing strategies such as `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`, `Company marketing`, `In person event`, `MyGreenhouse`, and `Other`. Use the strategy when aggregating candidate volume by channel; use the source itself when reporting on a specific channel within that category."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None, description="Id of the sourcing strategy. References the same strategy across all sources in the organization that roll up to it.")
    """Id of the sourcing strategy. References the same strategy across all sources in the organization that roll up to it."""
    name: str | None | None = Field(default=None, description="Display name of the sourcing strategy used in Greenhouse reporting (e.g. `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`).")
    """Display name of the sourcing strategy used in Greenhouse reporting (e.g. `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`)."""

class Source(BaseModel):
    """Greenhouse source object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: str | None = Field(default=None)
    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    type_: SourceType | None = Field(default=None, alias="type")
    updated_at: str | None = Field(default=None)

class Interview(BaseModel):
    """Greenhouse interview object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    all_day_end_on: str | None = Field(default=None)
    all_day_start_on: str | None = Field(default=None)
    application_id: int | None = Field(default=None)
    availability_received_at: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    ends_at: str | None = Field(default=None)
    external_event_id: str | None = Field(default=None)
    id: int | None = Field(default=None)
    job_id: int | None = Field(default=None)
    job_interview_id: int | None = Field(default=None)
    location: str | None = Field(default=None)
    organizer_id: int | None = Field(default=None)
    scheduled_at: str | None = Field(default=None)
    starts_at: str | None = Field(default=None)
    status: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    video_conferencing_url: str | None = Field(default=None)

class Attachment(BaseModel):
    """File associated with a Greenhouse application"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    application_id: int | None = Field(default=None)
    candidate_id: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    filename: str | None = Field(default=None)
    url: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class ApplicationsListResultMeta(BaseModel):
    """Metadata for applications.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class CandidatesListResultMeta(BaseModel):
    """Metadata for candidates.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class DepartmentsListResultMeta(BaseModel):
    """Metadata for departments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class InterviewsListResultMeta(BaseModel):
    """Metadata for interviews.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class JobPostsListResultMeta(BaseModel):
    """Metadata for job_posts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class JobsListResultMeta(BaseModel):
    """Metadata for jobs.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class OffersListResultMeta(BaseModel):
    """Metadata for offers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class OfficesListResultMeta(BaseModel):
    """Metadata for offices.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class SourcesListResultMeta(BaseModel):
    """Metadata for sources.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class AttachmentsListResultMeta(BaseModel):
    """Metadata for attachments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class GreenhouseCheckResult(BaseModel):
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
    meta: S | None = None
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class ApplicationsSearchData(BaseModel):
    """Search result data for applications entity."""
    model_config = ConfigDict(extra="allow")

    agency_note_id: int | None = None
    """Id of the note created when the candidate was submitted by an agency, or `null` if the application did not come through an agency."""
    answers: list[Any] | None = None
    """Free-text answers the candidate provided on the job post application form. Each entry pairs the question text with the candidate's answer."""
    candidate_id: int | None = None
    """Id of the candidate (person) this application belongs to."""
    coordinator_id: int | None = None
    """Id of the user assigned as coordinator on the application's job, or `null` when unassigned."""
    created_at: str | None = None
    """Created at from the Greenhouse v3 applications record."""
    custom_fields: dict[str, Any] | None = None
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    id: int | None = None
    """Id from the Greenhouse v3 applications record."""
    job_id: int | None = None
    """Id of the job this application is on. `null` for jobless prospect applications."""
    job_interview_stage_id: int | None = None
    """Id of the job interview stage definition (see `GET /v3/job_interview_stages`) the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state."""
    job_post_id: int | None = None
    """Id of the job post the candidate applied through, or `null` if the application was created internally rather than from a posted role."""
    last_activity_at: str | None = None
    """Timestamp of the most recent activity on this application (notes, emails, stage changes, etc.), in ISO 8601."""
    location_address: str | None = None
    """Free-form location string captured on the application (typically from the job post's location question)."""
    needs_decision: bool | None = None
    """`true` when the application is waiting on a hiring-team decision (scorecard completion, advance/reject, etc.) in its current stage."""
    prospect: bool | None = None
    """`true` for prospect applications (sourced candidates not yet attached to a single job), `false` for candidate applications on a specific job."""
    prospective_job_ids: list[Any] | None = None
    """For prospect applications, the ids of jobs the prospect is being considered for. Empty for non-prospect applications and for jobless prospects."""
    recruiter_id: int | None = None
    """Id of the user assigned as recruiter on the application's job, or `null` when unassigned."""
    referrer_id: int | None = None
    """Id of the referrer who credited this application, or `null` if there was no referral. References a referrer, not a Greenhouse user."""
    rejected_at: str | None = None
    """Timestamp the application was rejected, in ISO 8601. `null` for applications that have not been rejected."""
    rejection_reason_id: int | None = None
    """Id of the rejection reason selected for the application. References a `/v3/rejection_reasons` row scoped to the organization. `null` when the application was rejected without a reason, or has not been rejected."""
    source_id: int | None = None
    """Id of the source the application is attributed to (e.g. a job board, an event, an employee referral source). `null` if no source is set."""
    stage_id: int | None = None
    """Id of the interview stage the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state."""
    stage_name: str | None = None
    """Display name of the candidate's current interview stage on this application."""
    status: str | None = None
    """Lifecycle status of the application. `in_process` for active candidates, `rejected` for rejected applications, `hired` once an offer is closed and the hire endpoint has fired, and `converted` for prospect applications that have been promoted to a candidate application via `convert_to_candidate`."""
    updated_at: str | None = None
    """Updated at from the Greenhouse v3 applications record."""


class CandidatesSearchData(BaseModel):
    """Search result data for candidates entity."""
    model_config = ConfigDict(extra="allow")

    addresses: list[Any] | None = None
    """Postal addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `home`, `work`, or `other`."""
    can_email: bool | None = None
    """Whether this candidate has consented to receive email communication from your organization."""
    company: str | None = None
    """Candidate's current company, as entered on their profile."""
    created_at: str | None = None
    """Created at from the Greenhouse v3 candidates record."""
    custom_fields: dict[str, Any] | None = None
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    email_addresses: list[Any] | None = None
    """Email addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `work`, or `other`."""
    first_name: str | None = None
    """First name from the Greenhouse v3 candidates record."""
    id: int | None = None
    """Id from the Greenhouse v3 candidates record."""
    last_activity_at: str | None = None
    """Timestamp of the most recent activity on any of the candidate's applications (notes, emails, stage changes, etc.), in ISO 8601."""
    last_name: str | None = None
    """Last name from the Greenhouse v3 candidates record."""
    linked_user_ids: list[Any] | None = None
    """Ids of Greenhouse users linked to this candidate (employees represented by both a user record and a candidate record)."""
    phone_numbers: list[Any] | None = None
    """Phone numbers on the candidate's profile. Each entry pairs the `value` with a `type` such as `mobile`, `home`, `work`, `skype`, or `other`."""
    preferred_name: str | None = None
    """Preferred or chosen name the candidate goes by, when different from their legal first name."""
    private: bool | None = None
    """If true, the candidate is restricted to users with `View Private Candidates` access. Defaults to `false`."""
    social_media_addresses: list[Any] | None = None
    """Social media handles or URLs on the candidate's profile. Social entries are untyped — only the `value` is returned."""
    tags: list[Any] | None = None
    """Candidate tag names applied to this candidate within your organization."""
    time_zone: str | None = None
    """Candidate's time zone as a Rails-style identifier (for example `Eastern Time (US & Canada)`)."""
    title: str | None = None
    """Candidate's current job title, as entered on their profile."""
    updated_at: str | None = None
    """Updated at from the Greenhouse v3 candidates record."""
    website_addresses: list[Any] | None = None
    """Personal websites or portfolio URLs on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `company`, `portfolio`, `blog`, or `other`."""


class DepartmentsSearchData(BaseModel):
    """Search result data for departments entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """Created at from the Greenhouse v3 departments record."""
    external_id: str | None = None
    """Partner-supplied identifier for the department, typically the matching id from an HRIS or other external system. Free-form string and `null` when no external id has been set."""
    id: int | None = None
    """Id from the Greenhouse v3 departments record."""
    name: str | None = None
    """Display name of the department (e.g. `Engineering`, `Marketing`)."""
    parent_id: int | None = None
    """Id of the parent department in the organization's department tree. `null` for top-level departments. References another `/v3/departments` row."""
    updated_at: str | None = None
    """Updated at from the Greenhouse v3 departments record."""


class JobPostsSearchData(BaseModel):
    """Search result data for job_posts entity."""
    model_config = ConfigDict(extra="allow")

    active: bool | None = None
    """If `true`, the post has not been deleted. Deleted posts are excluded by default; pass `active=false` on the list endpoint to retrieve them."""
    content: str | None = None
    """HTML body of the post shown to candidates on the job board. For internal posts this returns the `internal_content` instead. Sanitized server-side — only a limited element/attribute allowlist (including `iframe`, `video`, `source`) survives. `null` while the post is still being scaffolded."""
    created_at: str | None = None
    """Created at from the Greenhouse v3 job posts record."""
    demographic_question_set_id: int | None = None
    """Id of the demographic question set surfaced to candidates on this post for diversity, equity, and inclusion (DE&I) reporting. `null` when the post does not collect demographic data."""
    featured: bool | None = None
    """If `true`, the post is currently featured on the organization's internal job board and surfaces in the weekly internal-jobs email. Only internal posts can be featured, and at most three can be featured at a time."""
    first_published_at: str | None = None
    """Timestamp the post first transitioned to `live`, in ISO 8601. `null` for posts that have never been published."""
    id: int | None = None
    """Id from the Greenhouse v3 job posts record."""
    internal: bool | None = None
    """If `true`, the post lives on an internal job board and is visible only to existing employees signed in to the internal board. If `false`, the post is external and lives on a public-facing `job_board`. Set by the board the post is associated with at create time."""
    internal_content: str | None = None
    """HTML body shown on the internal job board when the post is also configured as internal. `null` for external-only posts. Same sanitization rules as `content`."""
    job_board_id: int | None = None
    """Id of the `job_board` this post is published to. Resolves to either an external (careers site, syndicated board) or internal job board depending on `internal`. Each post belongs to exactly one board at a time."""
    job_id: int | None = None
    """Id of the parent job (requisition) this post belongs to. A single job can have multiple posts; the job is the source of truth for the hiring team, openings, and interview plan."""
    language: str | None = None
    """ISO 639-1 locale of the post, used to render the candidate-facing application form in the matching language (e.g. `en`, `fr`, `ja`). `null` when no locale has been chosen."""
    live: bool | None = None
    """If `true`, the post is published (`job_application_status` is `live`) and its job board is also live. A post on an unpublished board is **not** `live` — its `public_url` returns a 404 until the board is enabled."""
    public_url: str | None = None
    """Canonical public URL of the post on its job board, including the `gh_jid` tracking parameter. `null` when the post has no associated job board or the board has no public URL configured."""
    questions: list[Any] | None = None
    """Application form questions presented to candidates on this post, including default questions (resume, cover letter, basic info) and any custom questions configured by the hiring team. Ordered as they appear on the form."""
    title: str | None = None
    """Public-facing title shown to candidates on the job board (e.g. `Senior Backend Engineer, Remote`). Distinct from the internal `job.name` — a single job can have several posts with different titles, one per board, language, or geography."""
    updated_at: str | None = None
    """Updated at from the Greenhouse v3 job posts record."""


class JobsSearchData(BaseModel):
    """Search result data for jobs entity."""
    model_config = ConfigDict(extra="allow")

    closed_at: str | None = None
    """Timestamp the job most recently transitioned to `closed`, in ISO 8601. `null` for jobs that are still `open` or `draft`."""
    confidential: bool | None = None
    """If `true`, the job is restricted to users explicitly granted access on the Hiring Team. The legacy Confidential Jobs feature has been sunset — this flag cannot be set on new jobs and is preserved for jobs that already had it enabled."""
    copied_from_id: int | None = None
    """Id of the job (typically a template) this job was copied from on creation. `null` when the job was not created from another job."""
    created_at: str | None = None
    """Created at from the Greenhouse v3 jobs record."""
    custom_fields: dict[str, Any] | None = None
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    department_id: int | None = None
    """Id of the department this job is assigned to. `null` when no department is set."""
    id: int | None = None
    """Id from the Greenhouse v3 jobs record."""
    is_template: bool | None = None
    """If `true`, this job is a template used as the source for new jobs rather than a real requisition. Templates do not accept applications; reference them via `template_job_id` on `POST /v3/jobs`."""
    name: str | None = None
    """Internal job title shown to the hiring team in Greenhouse (e.g. `Senior Backend Engineer`). Distinct from the external-facing title on each `job_post`."""
    notes: str | None = None
    """Internal HTML notes about the job, surfaced to the hiring team in the Greenhouse UI. Not exposed on public job posts."""
    office_ids: list[Any] | None = None
    """Ids of the offices this job is assigned to. A job can span multiple offices; empty array or `null` when no offices are set."""
    opened_at: str | None = None
    """Timestamp the job first transitioned to `open`, in ISO 8601. `null` while the job is still in `draft`."""
    requisition_id: str | None = None
    """Partner-supplied external identifier for the requisition (e.g. an HRIS or ATS code). Free-form string, not unique across the organization, and `null` when no external id has been set."""
    status: str | None = None
    """Lifecycle status of the job. `draft` while it is being scaffolded, `open` once it has at least one open opening, and `closed` after every opening is closed. A job moves to `closed` automatically when its last open opening is closed via `PATCH /v3/openings/{id}`."""
    updated_at: str | None = None
    """Updated at from the Greenhouse v3 jobs record."""


class OffersSearchData(BaseModel):
    """Search result data for offers entity."""
    model_config = ConfigDict(extra="allow")

    application_id: int | None = None
    """Id of the application this offer is extended on. Every offer belongs to exactly one application; the offer is voided if the application is rejected or deleted."""
    candidate_id: int | None = None
    """Id of the candidate (person) receiving this offer. Resolved through the offer's application."""
    created_at: str | None = None
    """Created at from the Greenhouse v3 offers record."""
    custom_fields: dict[str, Any] | None = None
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    id: int | None = None
    """Id from the Greenhouse v3 offers record."""
    job_id: int | None = None
    """Id of the job this offer's application is on."""
    opening_id: int | None = None
    """Id of the specific opening this offer is being extended for. `null` when the offer has not yet been linked to an opening."""
    resolved_at: str | None = None
    """Timestamp the offer was resolved (`Accepted` or `Rejected`), in ISO 8601. Date updates submitted through `PATCH /v3/offers/{id}` are normalized to noon UTC on the supplied date. `null` while the offer is still `Created` or has been superseded as `Deprecated` without a resolution."""
    sent_on: str | None = None
    """Date the offer was sent to the candidate, in ISO 8601 (YYYY-MM-DD). `null` until the offer has been sent."""
    starts_on: str | None = None
    """Candidate's proposed start date, in ISO 8601 (YYYY-MM-DD). `null` when no start date has been set on the offer."""
    status: str | None = None
    """Lifecycle status of the offer. `Created` for offers still being drafted or pending approval, `Accepted` once the candidate accepts, `Rejected` if declined or withdrawn, and `Deprecated` for superseded prior versions (a new offer version replaces an earlier one with this status)."""
    updated_at: str | None = None
    """Updated at from the Greenhouse v3 offers record."""
    version: int | None = None
    """Revision number of this offer within its application. Greenhouse creates a new offer row (incrementing `version`) whenever a tracked field on an existing offer changes — typically `starts_on`, `opening_id`, or a custom field configured to trigger a new version. Pair with `current_only=true` to filter the list endpoint down to the latest version per application."""


class OfficesSearchData(BaseModel):
    """Search result data for offices entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """Created at from the Greenhouse v3 offices record."""
    external_id: str | None = None
    """Stable identifier supplied by the customer or HRIS for cross-system reconciliation. `null` when no external id has been set. Available when the `org_structure_external_id` product flag is enabled."""
    id: int | None = None
    """Id from the Greenhouse v3 offices record."""
    location: str | None = None
    """Free-form physical location string for the office (e.g. `New York, NY, USA`). `null` for offices that have no location set, including most remote offices."""
    name: str | None = None
    """Display name of the office (e.g. `San Francisco`, `Remote (US)`). Unique among active offices in the same organization."""
    parent_id: int | None = None
    """Id of the parent office when offices are organized hierarchically. `null` for top-level offices. References another `/v3/offices` row in the same organization."""
    primary_in_house_contact_user_id: int | None = None
    """Id of the Greenhouse user designated as the office's primary internal contact, typically the local recruiting lead. References a `/v3/users` row. `null` when no contact has been assigned."""
    updated_at: str | None = None
    """Updated at from the Greenhouse v3 offices record."""


class SourcesSearchData(BaseModel):
    """Search result data for sources entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """Created at from the Greenhouse v3 sources record."""
    id: int | None = None
    """Id from the Greenhouse v3 sources record."""
    name: str | None = None
    """Display name of the source as recruiters see it in Greenhouse (e.g. `LinkedIn (Prospecting)`, `Indeed`, `Referral`, `Internal Applicant`, or a custom agency name). For organization-specific sources this is the label the org configured; for global Greenhouse sources it is the standard public name."""
    type_: dict[str, Any] | None = None
    """The sourcing strategy this source rolls up to — the broader category used for reporting. Sources are grouped under sourcing strategies such as `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`, `Company marketing`, `In person event`, `MyGreenhouse`, and `Other`. Use the strategy when aggregating candidate volume by channel; use the source itself when reporting on a specific channel within that category."""
    updated_at: str | None = None
    """Updated at from the Greenhouse v3 sources record."""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    agency_id: int | None = None
    """Id of the staffing agency this user belongs to, when the user is an external agency recruiter rather than an employee of your organization. `null` for in-house users."""
    created_at: str | None = None
    """Created at from the Greenhouse v3 users record."""
    custom_fields: dict[str, Any] | None = None
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    deactivated: bool | None = None
    """Whether the user has been deactivated. Deactivated users cannot sign in or be assigned to new jobs, but their historical activity (notes, scorecards, emails) is preserved. Toggle via `POST /v3/users/{id}/deactivate` and `POST /v3/users/{id}/activate`."""
    department_ids: list[Any] | None = None
    """Ids of the departments this user is assigned to. Used to scope future job permissions and to filter the user list by department. Empty when the user is not pinned to any department."""
    emails: list[Any] | None = None
    """All email addresses on the user's account, including the primary address and any additional verified addresses."""
    employee_id: str | None = None
    """Partner-supplied external employee identifier, typically the user's HRIS or payroll id. Free-form string; not unique across organizations and `null` when no employee id has been set."""
    first_name: str | None = None
    """First name from the Greenhouse v3 users record."""
    id: int | None = None
    """Id from the Greenhouse v3 users record."""
    interviewer_tags: list[Any] | None = None
    """Interviewer tags applied to this user — the labeled skill or panel groupings (e.g. `Senior Engineer`, `Bar Raiser`) used to suggest qualified interviewers when building an interview plan. Each entry pairs the tag's `id` with its `name`."""
    job_title: str | None = None
    """Free-form job title set on the user's Greenhouse profile (e.g. `Senior Recruiter`). Not synchronized with any HRIS title."""
    last_name: str | None = None
    """Last name from the Greenhouse v3 users record."""
    linked_candidate_ids: list[Any] | None = None
    """Ids of candidate records linked to this user. Populated when an employee is represented by both a user record (for Greenhouse access) and a candidate record (for past or internal applications)."""
    name: str | None = None
    """Concatenation of `first_name` and `last_name` rendered as a single display string. Provided for convenience; partners that need either component should read `first_name`/`last_name` directly."""
    office_ids: list[Any] | None = None
    """Ids of the offices this user is assigned to. Used to scope future job permissions and to filter the user list by office. Empty when the user is not pinned to any office."""
    primary_email: str | None = None
    """Primary email address on the user's account. Sign-in identifier and the address Greenhouse uses for outbound mail; additional verified addresses are not surfaced here. Service accounts (integration/ISU users) have no email and are excluded from this endpoint by default; when included via `show_service_accounts=true`, their `primary_email` is an empty string."""
    site_admin: bool | None = None
    """Whether the user holds the Site Admin role. Site admins have unrestricted access to every non-confidential job and to organization-level settings. Demote a site admin to a Basic user with `POST /v3/users/{id}/revoke_permissions`."""
    updated_at: str | None = None
    """Updated at from the Greenhouse v3 users record."""


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

ApplicationsSearchResult = AirbyteSearchResult[ApplicationsSearchData]
"""Search result type for applications entity."""

CandidatesSearchResult = AirbyteSearchResult[CandidatesSearchData]
"""Search result type for candidates entity."""

DepartmentsSearchResult = AirbyteSearchResult[DepartmentsSearchData]
"""Search result type for departments entity."""

JobPostsSearchResult = AirbyteSearchResult[JobPostsSearchData]
"""Search result type for job_posts entity."""

JobsSearchResult = AirbyteSearchResult[JobsSearchData]
"""Search result type for jobs entity."""

OffersSearchResult = AirbyteSearchResult[OffersSearchData]
"""Search result type for offers entity."""

OfficesSearchResult = AirbyteSearchResult[OfficesSearchData]
"""Search result type for offices entity."""

SourcesSearchResult = AirbyteSearchResult[SourcesSearchData]
"""Search result type for sources entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

ApplicationsListResult = GreenhouseExecuteResultWithMeta[list[Application], ApplicationsListResultMeta]
"""Result type for applications.list operation with data and metadata."""

CandidatesListResult = GreenhouseExecuteResultWithMeta[list[Candidate], CandidatesListResultMeta]
"""Result type for candidates.list operation with data and metadata."""

DepartmentsListResult = GreenhouseExecuteResultWithMeta[list[Department], DepartmentsListResultMeta]
"""Result type for departments.list operation with data and metadata."""

InterviewsListResult = GreenhouseExecuteResultWithMeta[list[Interview], InterviewsListResultMeta]
"""Result type for interviews.list operation with data and metadata."""

JobPostsListResult = GreenhouseExecuteResultWithMeta[list[JobPost], JobPostsListResultMeta]
"""Result type for job_posts.list operation with data and metadata."""

JobsListResult = GreenhouseExecuteResultWithMeta[list[Job], JobsListResultMeta]
"""Result type for jobs.list operation with data and metadata."""

OffersListResult = GreenhouseExecuteResultWithMeta[list[Offer], OffersListResultMeta]
"""Result type for offers.list operation with data and metadata."""

OfficesListResult = GreenhouseExecuteResultWithMeta[list[Office], OfficesListResultMeta]
"""Result type for offices.list operation with data and metadata."""

SourcesListResult = GreenhouseExecuteResultWithMeta[list[Source], SourcesListResultMeta]
"""Result type for sources.list operation with data and metadata."""

UsersListResult = GreenhouseExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

AttachmentsListResult = GreenhouseExecuteResultWithMeta[list[Attachment], AttachmentsListResultMeta]
"""Result type for attachments.list operation with data and metadata."""

