"""
Type definitions for greenhouse connector.
"""
# ruff: noqa: E501
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

class ApplicationsListParams(TypedDict):
    """Parameters for applications.list operation"""
    cursor: NotRequired[str]
    per_page: NotRequired[int]
    ids: NotRequired[list[int]]
    updated_at: NotRequired[str]

class CandidatesListParams(TypedDict):
    """Parameters for candidates.list operation"""
    cursor: NotRequired[str]
    per_page: NotRequired[int]
    ids: NotRequired[list[int]]
    updated_at: NotRequired[str]

class DepartmentsListParams(TypedDict):
    """Parameters for departments.list operation"""
    cursor: NotRequired[str]
    per_page: NotRequired[int]
    ids: NotRequired[list[int]]

class InterviewsListParams(TypedDict):
    """Parameters for interviews.list operation"""
    cursor: NotRequired[str]
    per_page: NotRequired[int]
    ids: NotRequired[list[int]]
    updated_at: NotRequired[str]

class JobPostsListParams(TypedDict):
    """Parameters for job_posts.list operation"""
    cursor: NotRequired[str]
    per_page: NotRequired[int]
    ids: NotRequired[list[int]]
    updated_at: NotRequired[str]
    active: NotRequired[bool]

class JobsListParams(TypedDict):
    """Parameters for jobs.list operation"""
    cursor: NotRequired[str]
    per_page: NotRequired[int]
    ids: NotRequired[list[int]]
    updated_at: NotRequired[str]

class OffersListParams(TypedDict):
    """Parameters for offers.list operation"""
    cursor: NotRequired[str]
    per_page: NotRequired[int]
    ids: NotRequired[list[int]]
    updated_at: NotRequired[str]

class OfficesListParams(TypedDict):
    """Parameters for offices.list operation"""
    cursor: NotRequired[str]
    per_page: NotRequired[int]
    ids: NotRequired[list[int]]

class SourcesListParams(TypedDict):
    """Parameters for sources.list operation"""
    cursor: NotRequired[str]
    per_page: NotRequired[int]
    ids: NotRequired[list[int]]

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    cursor: NotRequired[str]
    per_page: NotRequired[int]
    ids: NotRequired[list[int]]
    updated_at: NotRequired[str]
    show_service_accounts: NotRequired[bool]

class AttachmentsListParams(TypedDict):
    """Parameters for attachments.list operation"""
    cursor: NotRequired[str]
    per_page: NotRequired[int]
    ids: NotRequired[list[int]]
    updated_at: NotRequired[str]
    application_ids: NotRequired[list[int]]
    candidate_ids: NotRequired[list[int]]
    type: NotRequired[str]

class AttachmentsDownloadParams(TypedDict):
    """Parameters for attachments.download operation"""
    ids: list[int]
    range_header: NotRequired[str]

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== APPLICATIONS SEARCH TYPES =====

class ApplicationsSearchFilter(TypedDict, total=False):
    """Available fields for filtering applications search queries."""
    agency_note_id: int | None
    """Id of the note created when the candidate was submitted by an agency, or `null` if the application did not come through an agency."""
    answers: list[Any] | None
    """Free-text answers the candidate provided on the job post application form. Each entry pairs the question text with the candidate's answer."""
    candidate_id: int | None
    """Id of the candidate (person) this application belongs to."""
    coordinator_id: int | None
    """Id of the user assigned as coordinator on the application's job, or `null` when unassigned."""
    created_at: str | None
    """Created at from the Greenhouse v3 applications record."""
    custom_fields: dict[str, Any] | None
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    id: int | None
    """Id from the Greenhouse v3 applications record."""
    job_id: int | None
    """Id of the job this application is on. `null` for jobless prospect applications."""
    job_interview_stage_id: int | None
    """Id of the job interview stage definition (see `GET /v3/job_interview_stages`) the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state."""
    job_post_id: int | None
    """Id of the job post the candidate applied through, or `null` if the application was created internally rather than from a posted role."""
    last_activity_at: str | None
    """Timestamp of the most recent activity on this application (notes, emails, stage changes, etc.), in ISO 8601."""
    location_address: str | None
    """Free-form location string captured on the application (typically from the job post's location question)."""
    needs_decision: bool | None
    """`true` when the application is waiting on a hiring-team decision (scorecard completion, advance/reject, etc.) in its current stage."""
    prospect: bool | None
    """`true` for prospect applications (sourced candidates not yet attached to a single job), `false` for candidate applications on a specific job."""
    prospective_job_ids: list[Any] | None
    """For prospect applications, the ids of jobs the prospect is being considered for. Empty for non-prospect applications and for jobless prospects."""
    recruiter_id: int | None
    """Id of the user assigned as recruiter on the application's job, or `null` when unassigned."""
    referrer_id: int | None
    """Id of the referrer who credited this application, or `null` if there was no referral. References a referrer, not a Greenhouse user."""
    rejected_at: str | None
    """Timestamp the application was rejected, in ISO 8601. `null` for applications that have not been rejected."""
    rejection_reason_id: int | None
    """Id of the rejection reason selected for the application. References a `/v3/rejection_reasons` row scoped to the organization. `null` when the application was rejected without a reason, or has not been rejected."""
    source_id: int | None
    """Id of the source the application is attributed to (e.g. a job board, an event, an employee referral source). `null` if no source is set."""
    stage_id: int | None
    """Id of the interview stage the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state."""
    stage_name: str | None
    """Display name of the candidate's current interview stage on this application."""
    status: str | None
    """Lifecycle status of the application. `in_process` for active candidates, `rejected` for rejected applications, `hired` once an offer is closed and the hire endpoint has fired, and `converted` for prospect applications that have been promoted to a candidate application via `convert_to_candidate`."""
    updated_at: str | None
    """Updated at from the Greenhouse v3 applications record."""


class ApplicationsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    agency_note_id: list[int]
    """Id of the note created when the candidate was submitted by an agency, or `null` if the application did not come through an agency."""
    answers: list[list[Any]]
    """Free-text answers the candidate provided on the job post application form. Each entry pairs the question text with the candidate's answer."""
    candidate_id: list[int]
    """Id of the candidate (person) this application belongs to."""
    coordinator_id: list[int]
    """Id of the user assigned as coordinator on the application's job, or `null` when unassigned."""
    created_at: list[str]
    """Created at from the Greenhouse v3 applications record."""
    custom_fields: list[dict[str, Any]]
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    id: list[int]
    """Id from the Greenhouse v3 applications record."""
    job_id: list[int]
    """Id of the job this application is on. `null` for jobless prospect applications."""
    job_interview_stage_id: list[int]
    """Id of the job interview stage definition (see `GET /v3/job_interview_stages`) the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state."""
    job_post_id: list[int]
    """Id of the job post the candidate applied through, or `null` if the application was created internally rather than from a posted role."""
    last_activity_at: list[str]
    """Timestamp of the most recent activity on this application (notes, emails, stage changes, etc.), in ISO 8601."""
    location_address: list[str]
    """Free-form location string captured on the application (typically from the job post's location question)."""
    needs_decision: list[bool]
    """`true` when the application is waiting on a hiring-team decision (scorecard completion, advance/reject, etc.) in its current stage."""
    prospect: list[bool]
    """`true` for prospect applications (sourced candidates not yet attached to a single job), `false` for candidate applications on a specific job."""
    prospective_job_ids: list[list[Any]]
    """For prospect applications, the ids of jobs the prospect is being considered for. Empty for non-prospect applications and for jobless prospects."""
    recruiter_id: list[int]
    """Id of the user assigned as recruiter on the application's job, or `null` when unassigned."""
    referrer_id: list[int]
    """Id of the referrer who credited this application, or `null` if there was no referral. References a referrer, not a Greenhouse user."""
    rejected_at: list[str]
    """Timestamp the application was rejected, in ISO 8601. `null` for applications that have not been rejected."""
    rejection_reason_id: list[int]
    """Id of the rejection reason selected for the application. References a `/v3/rejection_reasons` row scoped to the organization. `null` when the application was rejected without a reason, or has not been rejected."""
    source_id: list[int]
    """Id of the source the application is attributed to (e.g. a job board, an event, an employee referral source). `null` if no source is set."""
    stage_id: list[int]
    """Id of the interview stage the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state."""
    stage_name: list[str]
    """Display name of the candidate's current interview stage on this application."""
    status: list[str]
    """Lifecycle status of the application. `in_process` for active candidates, `rejected` for rejected applications, `hired` once an offer is closed and the hire endpoint has fired, and `converted` for prospect applications that have been promoted to a candidate application via `convert_to_candidate`."""
    updated_at: list[str]
    """Updated at from the Greenhouse v3 applications record."""


class ApplicationsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    agency_note_id: Any
    """Id of the note created when the candidate was submitted by an agency, or `null` if the application did not come through an agency."""
    answers: Any
    """Free-text answers the candidate provided on the job post application form. Each entry pairs the question text with the candidate's answer."""
    candidate_id: Any
    """Id of the candidate (person) this application belongs to."""
    coordinator_id: Any
    """Id of the user assigned as coordinator on the application's job, or `null` when unassigned."""
    created_at: Any
    """Created at from the Greenhouse v3 applications record."""
    custom_fields: Any
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    id: Any
    """Id from the Greenhouse v3 applications record."""
    job_id: Any
    """Id of the job this application is on. `null` for jobless prospect applications."""
    job_interview_stage_id: Any
    """Id of the job interview stage definition (see `GET /v3/job_interview_stages`) the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state."""
    job_post_id: Any
    """Id of the job post the candidate applied through, or `null` if the application was created internally rather than from a posted role."""
    last_activity_at: Any
    """Timestamp of the most recent activity on this application (notes, emails, stage changes, etc.), in ISO 8601."""
    location_address: Any
    """Free-form location string captured on the application (typically from the job post's location question)."""
    needs_decision: Any
    """`true` when the application is waiting on a hiring-team decision (scorecard completion, advance/reject, etc.) in its current stage."""
    prospect: Any
    """`true` for prospect applications (sourced candidates not yet attached to a single job), `false` for candidate applications on a specific job."""
    prospective_job_ids: Any
    """For prospect applications, the ids of jobs the prospect is being considered for. Empty for non-prospect applications and for jobless prospects."""
    recruiter_id: Any
    """Id of the user assigned as recruiter on the application's job, or `null` when unassigned."""
    referrer_id: Any
    """Id of the referrer who credited this application, or `null` if there was no referral. References a referrer, not a Greenhouse user."""
    rejected_at: Any
    """Timestamp the application was rejected, in ISO 8601. `null` for applications that have not been rejected."""
    rejection_reason_id: Any
    """Id of the rejection reason selected for the application. References a `/v3/rejection_reasons` row scoped to the organization. `null` when the application was rejected without a reason, or has not been rejected."""
    source_id: Any
    """Id of the source the application is attributed to (e.g. a job board, an event, an employee referral source). `null` if no source is set."""
    stage_id: Any
    """Id of the interview stage the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state."""
    stage_name: Any
    """Display name of the candidate's current interview stage on this application."""
    status: Any
    """Lifecycle status of the application. `in_process` for active candidates, `rejected` for rejected applications, `hired` once an offer is closed and the hire endpoint has fired, and `converted` for prospect applications that have been promoted to a candidate application via `convert_to_candidate`."""
    updated_at: Any
    """Updated at from the Greenhouse v3 applications record."""


class ApplicationsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    agency_note_id: str
    """Id of the note created when the candidate was submitted by an agency, or `null` if the application did not come through an agency."""
    answers: str
    """Free-text answers the candidate provided on the job post application form. Each entry pairs the question text with the candidate's answer."""
    candidate_id: str
    """Id of the candidate (person) this application belongs to."""
    coordinator_id: str
    """Id of the user assigned as coordinator on the application's job, or `null` when unassigned."""
    created_at: str
    """Created at from the Greenhouse v3 applications record."""
    custom_fields: str
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    id: str
    """Id from the Greenhouse v3 applications record."""
    job_id: str
    """Id of the job this application is on. `null` for jobless prospect applications."""
    job_interview_stage_id: str
    """Id of the job interview stage definition (see `GET /v3/job_interview_stages`) the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state."""
    job_post_id: str
    """Id of the job post the candidate applied through, or `null` if the application was created internally rather than from a posted role."""
    last_activity_at: str
    """Timestamp of the most recent activity on this application (notes, emails, stage changes, etc.), in ISO 8601."""
    location_address: str
    """Free-form location string captured on the application (typically from the job post's location question)."""
    needs_decision: str
    """`true` when the application is waiting on a hiring-team decision (scorecard completion, advance/reject, etc.) in its current stage."""
    prospect: str
    """`true` for prospect applications (sourced candidates not yet attached to a single job), `false` for candidate applications on a specific job."""
    prospective_job_ids: str
    """For prospect applications, the ids of jobs the prospect is being considered for. Empty for non-prospect applications and for jobless prospects."""
    recruiter_id: str
    """Id of the user assigned as recruiter on the application's job, or `null` when unassigned."""
    referrer_id: str
    """Id of the referrer who credited this application, or `null` if there was no referral. References a referrer, not a Greenhouse user."""
    rejected_at: str
    """Timestamp the application was rejected, in ISO 8601. `null` for applications that have not been rejected."""
    rejection_reason_id: str
    """Id of the rejection reason selected for the application. References a `/v3/rejection_reasons` row scoped to the organization. `null` when the application was rejected without a reason, or has not been rejected."""
    source_id: str
    """Id of the source the application is attributed to (e.g. a job board, an event, an employee referral source). `null` if no source is set."""
    stage_id: str
    """Id of the interview stage the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state."""
    stage_name: str
    """Display name of the candidate's current interview stage on this application."""
    status: str
    """Lifecycle status of the application. `in_process` for active candidates, `rejected` for rejected applications, `hired` once an offer is closed and the hire endpoint has fired, and `converted` for prospect applications that have been promoted to a candidate application via `convert_to_candidate`."""
    updated_at: str
    """Updated at from the Greenhouse v3 applications record."""


class ApplicationsSortFilter(TypedDict, total=False):
    """Available fields for sorting applications search results."""
    agency_note_id: AirbyteSortOrder
    """Id of the note created when the candidate was submitted by an agency, or `null` if the application did not come through an agency."""
    answers: AirbyteSortOrder
    """Free-text answers the candidate provided on the job post application form. Each entry pairs the question text with the candidate's answer."""
    candidate_id: AirbyteSortOrder
    """Id of the candidate (person) this application belongs to."""
    coordinator_id: AirbyteSortOrder
    """Id of the user assigned as coordinator on the application's job, or `null` when unassigned."""
    created_at: AirbyteSortOrder
    """Created at from the Greenhouse v3 applications record."""
    custom_fields: AirbyteSortOrder
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    id: AirbyteSortOrder
    """Id from the Greenhouse v3 applications record."""
    job_id: AirbyteSortOrder
    """Id of the job this application is on. `null` for jobless prospect applications."""
    job_interview_stage_id: AirbyteSortOrder
    """Id of the job interview stage definition (see `GET /v3/job_interview_stages`) the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state."""
    job_post_id: AirbyteSortOrder
    """Id of the job post the candidate applied through, or `null` if the application was created internally rather than from a posted role."""
    last_activity_at: AirbyteSortOrder
    """Timestamp of the most recent activity on this application (notes, emails, stage changes, etc.), in ISO 8601."""
    location_address: AirbyteSortOrder
    """Free-form location string captured on the application (typically from the job post's location question)."""
    needs_decision: AirbyteSortOrder
    """`true` when the application is waiting on a hiring-team decision (scorecard completion, advance/reject, etc.) in its current stage."""
    prospect: AirbyteSortOrder
    """`true` for prospect applications (sourced candidates not yet attached to a single job), `false` for candidate applications on a specific job."""
    prospective_job_ids: AirbyteSortOrder
    """For prospect applications, the ids of jobs the prospect is being considered for. Empty for non-prospect applications and for jobless prospects."""
    recruiter_id: AirbyteSortOrder
    """Id of the user assigned as recruiter on the application's job, or `null` when unassigned."""
    referrer_id: AirbyteSortOrder
    """Id of the referrer who credited this application, or `null` if there was no referral. References a referrer, not a Greenhouse user."""
    rejected_at: AirbyteSortOrder
    """Timestamp the application was rejected, in ISO 8601. `null` for applications that have not been rejected."""
    rejection_reason_id: AirbyteSortOrder
    """Id of the rejection reason selected for the application. References a `/v3/rejection_reasons` row scoped to the organization. `null` when the application was rejected without a reason, or has not been rejected."""
    source_id: AirbyteSortOrder
    """Id of the source the application is attributed to (e.g. a job board, an event, an employee referral source). `null` if no source is set."""
    stage_id: AirbyteSortOrder
    """Id of the interview stage the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state."""
    stage_name: AirbyteSortOrder
    """Display name of the candidate's current interview stage on this application."""
    status: AirbyteSortOrder
    """Lifecycle status of the application. `in_process` for active candidates, `rejected` for rejected applications, `hired` once an offer is closed and the hire endpoint has fired, and `converted` for prospect applications that have been promoted to a candidate application via `convert_to_candidate`."""
    updated_at: AirbyteSortOrder
    """Updated at from the Greenhouse v3 applications record."""


# Entity-specific condition types for applications
class ApplicationsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ApplicationsSearchFilter


class ApplicationsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ApplicationsSearchFilter


class ApplicationsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ApplicationsSearchFilter


class ApplicationsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ApplicationsSearchFilter


class ApplicationsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ApplicationsSearchFilter


class ApplicationsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ApplicationsSearchFilter


class ApplicationsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: ApplicationsStringFilter


class ApplicationsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: ApplicationsStringFilter


class ApplicationsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ApplicationsStringFilter


class ApplicationsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ApplicationsStringFilter


class ApplicationsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: ApplicationsAnyValueFilter


class ApplicationsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: ApplicationsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ApplicationsInCondition = TypedDict("ApplicationsInCondition", {"in": ApplicationsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ApplicationsNotCondition = TypedDict("ApplicationsNotCondition", {"not": "ApplicationsCondition"}, total=False)
"""Negates the nested condition."""

ApplicationsAndCondition = TypedDict("ApplicationsAndCondition", {"and": "list[ApplicationsCondition]"}, total=False)
"""True if all nested conditions are true."""

ApplicationsOrCondition = TypedDict("ApplicationsOrCondition", {"or": "list[ApplicationsCondition]"}, total=False)
"""True if any nested condition is true."""

ApplicationsAnyCondition = TypedDict("ApplicationsAnyCondition", {"any": ApplicationsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all applications condition types
ApplicationsCondition = (
    ApplicationsEqCondition
    | ApplicationsNeqCondition
    | ApplicationsGtCondition
    | ApplicationsGteCondition
    | ApplicationsLtCondition
    | ApplicationsLteCondition
    | ApplicationsInCondition
    | ApplicationsStartswithCondition
    | ApplicationsEndswithCondition
    | ApplicationsFuzzyCondition
    | ApplicationsKeywordCondition
    | ApplicationsContainsCondition
    | ApplicationsArrayContainsCondition
    | ApplicationsNotCondition
    | ApplicationsAndCondition
    | ApplicationsOrCondition
    | ApplicationsAnyCondition
)


class ApplicationsSearchQuery(TypedDict, total=False):
    """Search query for applications entity."""
    filter: ApplicationsCondition
    sort: list[ApplicationsSortFilter]


# ===== CANDIDATES SEARCH TYPES =====

class CandidatesSearchFilter(TypedDict, total=False):
    """Available fields for filtering candidates search queries."""
    addresses: list[Any] | None
    """Postal addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `home`, `work`, or `other`."""
    can_email: bool | None
    """Whether this candidate has consented to receive email communication from your organization."""
    company: str | None
    """Candidate's current company, as entered on their profile."""
    created_at: str | None
    """Created at from the Greenhouse v3 candidates record."""
    custom_fields: dict[str, Any] | None
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    email_addresses: list[Any] | None
    """Email addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `work`, or `other`."""
    first_name: str | None
    """First name from the Greenhouse v3 candidates record."""
    id: int | None
    """Id from the Greenhouse v3 candidates record."""
    last_activity_at: str | None
    """Timestamp of the most recent activity on any of the candidate's applications (notes, emails, stage changes, etc.), in ISO 8601."""
    last_name: str | None
    """Last name from the Greenhouse v3 candidates record."""
    linked_user_ids: list[Any] | None
    """Ids of Greenhouse users linked to this candidate (employees represented by both a user record and a candidate record)."""
    phone_numbers: list[Any] | None
    """Phone numbers on the candidate's profile. Each entry pairs the `value` with a `type` such as `mobile`, `home`, `work`, `skype`, or `other`."""
    preferred_name: str | None
    """Preferred or chosen name the candidate goes by, when different from their legal first name."""
    private: bool | None
    """If true, the candidate is restricted to users with `View Private Candidates` access. Defaults to `false`."""
    social_media_addresses: list[Any] | None
    """Social media handles or URLs on the candidate's profile. Social entries are untyped — only the `value` is returned."""
    tags: list[Any] | None
    """Candidate tag names applied to this candidate within your organization."""
    time_zone: str | None
    """Candidate's time zone as a Rails-style identifier (for example `Eastern Time (US & Canada)`)."""
    title: str | None
    """Candidate's current job title, as entered on their profile."""
    updated_at: str | None
    """Updated at from the Greenhouse v3 candidates record."""
    website_addresses: list[Any] | None
    """Personal websites or portfolio URLs on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `company`, `portfolio`, `blog`, or `other`."""


class CandidatesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    addresses: list[list[Any]]
    """Postal addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `home`, `work`, or `other`."""
    can_email: list[bool]
    """Whether this candidate has consented to receive email communication from your organization."""
    company: list[str]
    """Candidate's current company, as entered on their profile."""
    created_at: list[str]
    """Created at from the Greenhouse v3 candidates record."""
    custom_fields: list[dict[str, Any]]
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    email_addresses: list[list[Any]]
    """Email addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `work`, or `other`."""
    first_name: list[str]
    """First name from the Greenhouse v3 candidates record."""
    id: list[int]
    """Id from the Greenhouse v3 candidates record."""
    last_activity_at: list[str]
    """Timestamp of the most recent activity on any of the candidate's applications (notes, emails, stage changes, etc.), in ISO 8601."""
    last_name: list[str]
    """Last name from the Greenhouse v3 candidates record."""
    linked_user_ids: list[list[Any]]
    """Ids of Greenhouse users linked to this candidate (employees represented by both a user record and a candidate record)."""
    phone_numbers: list[list[Any]]
    """Phone numbers on the candidate's profile. Each entry pairs the `value` with a `type` such as `mobile`, `home`, `work`, `skype`, or `other`."""
    preferred_name: list[str]
    """Preferred or chosen name the candidate goes by, when different from their legal first name."""
    private: list[bool]
    """If true, the candidate is restricted to users with `View Private Candidates` access. Defaults to `false`."""
    social_media_addresses: list[list[Any]]
    """Social media handles or URLs on the candidate's profile. Social entries are untyped — only the `value` is returned."""
    tags: list[list[Any]]
    """Candidate tag names applied to this candidate within your organization."""
    time_zone: list[str]
    """Candidate's time zone as a Rails-style identifier (for example `Eastern Time (US & Canada)`)."""
    title: list[str]
    """Candidate's current job title, as entered on their profile."""
    updated_at: list[str]
    """Updated at from the Greenhouse v3 candidates record."""
    website_addresses: list[list[Any]]
    """Personal websites or portfolio URLs on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `company`, `portfolio`, `blog`, or `other`."""


class CandidatesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    addresses: Any
    """Postal addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `home`, `work`, or `other`."""
    can_email: Any
    """Whether this candidate has consented to receive email communication from your organization."""
    company: Any
    """Candidate's current company, as entered on their profile."""
    created_at: Any
    """Created at from the Greenhouse v3 candidates record."""
    custom_fields: Any
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    email_addresses: Any
    """Email addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `work`, or `other`."""
    first_name: Any
    """First name from the Greenhouse v3 candidates record."""
    id: Any
    """Id from the Greenhouse v3 candidates record."""
    last_activity_at: Any
    """Timestamp of the most recent activity on any of the candidate's applications (notes, emails, stage changes, etc.), in ISO 8601."""
    last_name: Any
    """Last name from the Greenhouse v3 candidates record."""
    linked_user_ids: Any
    """Ids of Greenhouse users linked to this candidate (employees represented by both a user record and a candidate record)."""
    phone_numbers: Any
    """Phone numbers on the candidate's profile. Each entry pairs the `value` with a `type` such as `mobile`, `home`, `work`, `skype`, or `other`."""
    preferred_name: Any
    """Preferred or chosen name the candidate goes by, when different from their legal first name."""
    private: Any
    """If true, the candidate is restricted to users with `View Private Candidates` access. Defaults to `false`."""
    social_media_addresses: Any
    """Social media handles or URLs on the candidate's profile. Social entries are untyped — only the `value` is returned."""
    tags: Any
    """Candidate tag names applied to this candidate within your organization."""
    time_zone: Any
    """Candidate's time zone as a Rails-style identifier (for example `Eastern Time (US & Canada)`)."""
    title: Any
    """Candidate's current job title, as entered on their profile."""
    updated_at: Any
    """Updated at from the Greenhouse v3 candidates record."""
    website_addresses: Any
    """Personal websites or portfolio URLs on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `company`, `portfolio`, `blog`, or `other`."""


class CandidatesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    addresses: str
    """Postal addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `home`, `work`, or `other`."""
    can_email: str
    """Whether this candidate has consented to receive email communication from your organization."""
    company: str
    """Candidate's current company, as entered on their profile."""
    created_at: str
    """Created at from the Greenhouse v3 candidates record."""
    custom_fields: str
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    email_addresses: str
    """Email addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `work`, or `other`."""
    first_name: str
    """First name from the Greenhouse v3 candidates record."""
    id: str
    """Id from the Greenhouse v3 candidates record."""
    last_activity_at: str
    """Timestamp of the most recent activity on any of the candidate's applications (notes, emails, stage changes, etc.), in ISO 8601."""
    last_name: str
    """Last name from the Greenhouse v3 candidates record."""
    linked_user_ids: str
    """Ids of Greenhouse users linked to this candidate (employees represented by both a user record and a candidate record)."""
    phone_numbers: str
    """Phone numbers on the candidate's profile. Each entry pairs the `value` with a `type` such as `mobile`, `home`, `work`, `skype`, or `other`."""
    preferred_name: str
    """Preferred or chosen name the candidate goes by, when different from their legal first name."""
    private: str
    """If true, the candidate is restricted to users with `View Private Candidates` access. Defaults to `false`."""
    social_media_addresses: str
    """Social media handles or URLs on the candidate's profile. Social entries are untyped — only the `value` is returned."""
    tags: str
    """Candidate tag names applied to this candidate within your organization."""
    time_zone: str
    """Candidate's time zone as a Rails-style identifier (for example `Eastern Time (US & Canada)`)."""
    title: str
    """Candidate's current job title, as entered on their profile."""
    updated_at: str
    """Updated at from the Greenhouse v3 candidates record."""
    website_addresses: str
    """Personal websites or portfolio URLs on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `company`, `portfolio`, `blog`, or `other`."""


class CandidatesSortFilter(TypedDict, total=False):
    """Available fields for sorting candidates search results."""
    addresses: AirbyteSortOrder
    """Postal addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `home`, `work`, or `other`."""
    can_email: AirbyteSortOrder
    """Whether this candidate has consented to receive email communication from your organization."""
    company: AirbyteSortOrder
    """Candidate's current company, as entered on their profile."""
    created_at: AirbyteSortOrder
    """Created at from the Greenhouse v3 candidates record."""
    custom_fields: AirbyteSortOrder
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    email_addresses: AirbyteSortOrder
    """Email addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `work`, or `other`."""
    first_name: AirbyteSortOrder
    """First name from the Greenhouse v3 candidates record."""
    id: AirbyteSortOrder
    """Id from the Greenhouse v3 candidates record."""
    last_activity_at: AirbyteSortOrder
    """Timestamp of the most recent activity on any of the candidate's applications (notes, emails, stage changes, etc.), in ISO 8601."""
    last_name: AirbyteSortOrder
    """Last name from the Greenhouse v3 candidates record."""
    linked_user_ids: AirbyteSortOrder
    """Ids of Greenhouse users linked to this candidate (employees represented by both a user record and a candidate record)."""
    phone_numbers: AirbyteSortOrder
    """Phone numbers on the candidate's profile. Each entry pairs the `value` with a `type` such as `mobile`, `home`, `work`, `skype`, or `other`."""
    preferred_name: AirbyteSortOrder
    """Preferred or chosen name the candidate goes by, when different from their legal first name."""
    private: AirbyteSortOrder
    """If true, the candidate is restricted to users with `View Private Candidates` access. Defaults to `false`."""
    social_media_addresses: AirbyteSortOrder
    """Social media handles or URLs on the candidate's profile. Social entries are untyped — only the `value` is returned."""
    tags: AirbyteSortOrder
    """Candidate tag names applied to this candidate within your organization."""
    time_zone: AirbyteSortOrder
    """Candidate's time zone as a Rails-style identifier (for example `Eastern Time (US & Canada)`)."""
    title: AirbyteSortOrder
    """Candidate's current job title, as entered on their profile."""
    updated_at: AirbyteSortOrder
    """Updated at from the Greenhouse v3 candidates record."""
    website_addresses: AirbyteSortOrder
    """Personal websites or portfolio URLs on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `company`, `portfolio`, `blog`, or `other`."""


# Entity-specific condition types for candidates
class CandidatesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CandidatesSearchFilter


class CandidatesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CandidatesSearchFilter


class CandidatesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CandidatesSearchFilter


class CandidatesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CandidatesSearchFilter


class CandidatesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CandidatesSearchFilter


class CandidatesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CandidatesSearchFilter


class CandidatesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: CandidatesStringFilter


class CandidatesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: CandidatesStringFilter


class CandidatesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CandidatesStringFilter


class CandidatesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CandidatesStringFilter


class CandidatesContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: CandidatesAnyValueFilter


class CandidatesArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: CandidatesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CandidatesInCondition = TypedDict("CandidatesInCondition", {"in": CandidatesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CandidatesNotCondition = TypedDict("CandidatesNotCondition", {"not": "CandidatesCondition"}, total=False)
"""Negates the nested condition."""

CandidatesAndCondition = TypedDict("CandidatesAndCondition", {"and": "list[CandidatesCondition]"}, total=False)
"""True if all nested conditions are true."""

CandidatesOrCondition = TypedDict("CandidatesOrCondition", {"or": "list[CandidatesCondition]"}, total=False)
"""True if any nested condition is true."""

CandidatesAnyCondition = TypedDict("CandidatesAnyCondition", {"any": CandidatesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all candidates condition types
CandidatesCondition = (
    CandidatesEqCondition
    | CandidatesNeqCondition
    | CandidatesGtCondition
    | CandidatesGteCondition
    | CandidatesLtCondition
    | CandidatesLteCondition
    | CandidatesInCondition
    | CandidatesStartswithCondition
    | CandidatesEndswithCondition
    | CandidatesFuzzyCondition
    | CandidatesKeywordCondition
    | CandidatesContainsCondition
    | CandidatesArrayContainsCondition
    | CandidatesNotCondition
    | CandidatesAndCondition
    | CandidatesOrCondition
    | CandidatesAnyCondition
)


class CandidatesSearchQuery(TypedDict, total=False):
    """Search query for candidates entity."""
    filter: CandidatesCondition
    sort: list[CandidatesSortFilter]


# ===== DEPARTMENTS SEARCH TYPES =====

class DepartmentsSearchFilter(TypedDict, total=False):
    """Available fields for filtering departments search queries."""
    created_at: str | None
    """Created at from the Greenhouse v3 departments record."""
    external_id: str | None
    """Partner-supplied identifier for the department, typically the matching id from an HRIS or other external system. Free-form string and `null` when no external id has been set."""
    id: int | None
    """Id from the Greenhouse v3 departments record."""
    name: str | None
    """Display name of the department (e.g. `Engineering`, `Marketing`)."""
    parent_id: int | None
    """Id of the parent department in the organization's department tree. `null` for top-level departments. References another `/v3/departments` row."""
    updated_at: str | None
    """Updated at from the Greenhouse v3 departments record."""


class DepartmentsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """Created at from the Greenhouse v3 departments record."""
    external_id: list[str]
    """Partner-supplied identifier for the department, typically the matching id from an HRIS or other external system. Free-form string and `null` when no external id has been set."""
    id: list[int]
    """Id from the Greenhouse v3 departments record."""
    name: list[str]
    """Display name of the department (e.g. `Engineering`, `Marketing`)."""
    parent_id: list[int]
    """Id of the parent department in the organization's department tree. `null` for top-level departments. References another `/v3/departments` row."""
    updated_at: list[str]
    """Updated at from the Greenhouse v3 departments record."""


class DepartmentsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """Created at from the Greenhouse v3 departments record."""
    external_id: Any
    """Partner-supplied identifier for the department, typically the matching id from an HRIS or other external system. Free-form string and `null` when no external id has been set."""
    id: Any
    """Id from the Greenhouse v3 departments record."""
    name: Any
    """Display name of the department (e.g. `Engineering`, `Marketing`)."""
    parent_id: Any
    """Id of the parent department in the organization's department tree. `null` for top-level departments. References another `/v3/departments` row."""
    updated_at: Any
    """Updated at from the Greenhouse v3 departments record."""


class DepartmentsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    created_at: str
    """Created at from the Greenhouse v3 departments record."""
    external_id: str
    """Partner-supplied identifier for the department, typically the matching id from an HRIS or other external system. Free-form string and `null` when no external id has been set."""
    id: str
    """Id from the Greenhouse v3 departments record."""
    name: str
    """Display name of the department (e.g. `Engineering`, `Marketing`)."""
    parent_id: str
    """Id of the parent department in the organization's department tree. `null` for top-level departments. References another `/v3/departments` row."""
    updated_at: str
    """Updated at from the Greenhouse v3 departments record."""


class DepartmentsSortFilter(TypedDict, total=False):
    """Available fields for sorting departments search results."""
    created_at: AirbyteSortOrder
    """Created at from the Greenhouse v3 departments record."""
    external_id: AirbyteSortOrder
    """Partner-supplied identifier for the department, typically the matching id from an HRIS or other external system. Free-form string and `null` when no external id has been set."""
    id: AirbyteSortOrder
    """Id from the Greenhouse v3 departments record."""
    name: AirbyteSortOrder
    """Display name of the department (e.g. `Engineering`, `Marketing`)."""
    parent_id: AirbyteSortOrder
    """Id of the parent department in the organization's department tree. `null` for top-level departments. References another `/v3/departments` row."""
    updated_at: AirbyteSortOrder
    """Updated at from the Greenhouse v3 departments record."""


# Entity-specific condition types for departments
class DepartmentsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DepartmentsSearchFilter


class DepartmentsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DepartmentsSearchFilter


class DepartmentsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DepartmentsSearchFilter


class DepartmentsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DepartmentsSearchFilter


class DepartmentsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DepartmentsSearchFilter


class DepartmentsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DepartmentsSearchFilter


class DepartmentsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: DepartmentsStringFilter


class DepartmentsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: DepartmentsStringFilter


class DepartmentsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DepartmentsStringFilter


class DepartmentsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DepartmentsStringFilter


class DepartmentsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: DepartmentsAnyValueFilter


class DepartmentsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: DepartmentsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DepartmentsInCondition = TypedDict("DepartmentsInCondition", {"in": DepartmentsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DepartmentsNotCondition = TypedDict("DepartmentsNotCondition", {"not": "DepartmentsCondition"}, total=False)
"""Negates the nested condition."""

DepartmentsAndCondition = TypedDict("DepartmentsAndCondition", {"and": "list[DepartmentsCondition]"}, total=False)
"""True if all nested conditions are true."""

DepartmentsOrCondition = TypedDict("DepartmentsOrCondition", {"or": "list[DepartmentsCondition]"}, total=False)
"""True if any nested condition is true."""

DepartmentsAnyCondition = TypedDict("DepartmentsAnyCondition", {"any": DepartmentsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all departments condition types
DepartmentsCondition = (
    DepartmentsEqCondition
    | DepartmentsNeqCondition
    | DepartmentsGtCondition
    | DepartmentsGteCondition
    | DepartmentsLtCondition
    | DepartmentsLteCondition
    | DepartmentsInCondition
    | DepartmentsStartswithCondition
    | DepartmentsEndswithCondition
    | DepartmentsFuzzyCondition
    | DepartmentsKeywordCondition
    | DepartmentsContainsCondition
    | DepartmentsArrayContainsCondition
    | DepartmentsNotCondition
    | DepartmentsAndCondition
    | DepartmentsOrCondition
    | DepartmentsAnyCondition
)


class DepartmentsSearchQuery(TypedDict, total=False):
    """Search query for departments entity."""
    filter: DepartmentsCondition
    sort: list[DepartmentsSortFilter]


# ===== JOB_POSTS SEARCH TYPES =====

class JobPostsSearchFilter(TypedDict, total=False):
    """Available fields for filtering job_posts search queries."""
    active: bool | None
    """If `true`, the post has not been deleted. Deleted posts are excluded by default; pass `active=false` on the list endpoint to retrieve them."""
    content: str | None
    """HTML body of the post shown to candidates on the job board. For internal posts this returns the `internal_content` instead. Sanitized server-side — only a limited element/attribute allowlist (including `iframe`, `video`, `source`) survives. `null` while the post is still being scaffolded."""
    created_at: str | None
    """Created at from the Greenhouse v3 job posts record."""
    demographic_question_set_id: int | None
    """Id of the demographic question set surfaced to candidates on this post for diversity, equity, and inclusion (DE&I) reporting. `null` when the post does not collect demographic data."""
    featured: bool | None
    """If `true`, the post is currently featured on the organization's internal job board and surfaces in the weekly internal-jobs email. Only internal posts can be featured, and at most three can be featured at a time."""
    first_published_at: str | None
    """Timestamp the post first transitioned to `live`, in ISO 8601. `null` for posts that have never been published."""
    id: int | None
    """Id from the Greenhouse v3 job posts record."""
    internal: bool | None
    """If `true`, the post lives on an internal job board and is visible only to existing employees signed in to the internal board. If `false`, the post is external and lives on a public-facing `job_board`. Set by the board the post is associated with at create time."""
    internal_content: str | None
    """HTML body shown on the internal job board when the post is also configured as internal. `null` for external-only posts. Same sanitization rules as `content`."""
    job_board_id: int | None
    """Id of the `job_board` this post is published to. Resolves to either an external (careers site, syndicated board) or internal job board depending on `internal`. Each post belongs to exactly one board at a time."""
    job_id: int | None
    """Id of the parent job (requisition) this post belongs to. A single job can have multiple posts; the job is the source of truth for the hiring team, openings, and interview plan."""
    language: str | None
    """ISO 639-1 locale of the post, used to render the candidate-facing application form in the matching language (e.g. `en`, `fr`, `ja`). `null` when no locale has been chosen."""
    live: bool | None
    """If `true`, the post is published (`job_application_status` is `live`) and its job board is also live. A post on an unpublished board is **not** `live` — its `public_url` returns a 404 until the board is enabled."""
    public_url: str | None
    """Canonical public URL of the post on its job board, including the `gh_jid` tracking parameter. `null` when the post has no associated job board or the board has no public URL configured."""
    questions: list[Any] | None
    """Application form questions presented to candidates on this post, including default questions (resume, cover letter, basic info) and any custom questions configured by the hiring team. Ordered as they appear on the form."""
    title: str | None
    """Public-facing title shown to candidates on the job board (e.g. `Senior Backend Engineer, Remote`). Distinct from the internal `job.name` — a single job can have several posts with different titles, one per board, language, or geography."""
    updated_at: str | None
    """Updated at from the Greenhouse v3 job posts record."""


class JobPostsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    active: list[bool]
    """If `true`, the post has not been deleted. Deleted posts are excluded by default; pass `active=false` on the list endpoint to retrieve them."""
    content: list[str]
    """HTML body of the post shown to candidates on the job board. For internal posts this returns the `internal_content` instead. Sanitized server-side — only a limited element/attribute allowlist (including `iframe`, `video`, `source`) survives. `null` while the post is still being scaffolded."""
    created_at: list[str]
    """Created at from the Greenhouse v3 job posts record."""
    demographic_question_set_id: list[int]
    """Id of the demographic question set surfaced to candidates on this post for diversity, equity, and inclusion (DE&I) reporting. `null` when the post does not collect demographic data."""
    featured: list[bool]
    """If `true`, the post is currently featured on the organization's internal job board and surfaces in the weekly internal-jobs email. Only internal posts can be featured, and at most three can be featured at a time."""
    first_published_at: list[str]
    """Timestamp the post first transitioned to `live`, in ISO 8601. `null` for posts that have never been published."""
    id: list[int]
    """Id from the Greenhouse v3 job posts record."""
    internal: list[bool]
    """If `true`, the post lives on an internal job board and is visible only to existing employees signed in to the internal board. If `false`, the post is external and lives on a public-facing `job_board`. Set by the board the post is associated with at create time."""
    internal_content: list[str]
    """HTML body shown on the internal job board when the post is also configured as internal. `null` for external-only posts. Same sanitization rules as `content`."""
    job_board_id: list[int]
    """Id of the `job_board` this post is published to. Resolves to either an external (careers site, syndicated board) or internal job board depending on `internal`. Each post belongs to exactly one board at a time."""
    job_id: list[int]
    """Id of the parent job (requisition) this post belongs to. A single job can have multiple posts; the job is the source of truth for the hiring team, openings, and interview plan."""
    language: list[str]
    """ISO 639-1 locale of the post, used to render the candidate-facing application form in the matching language (e.g. `en`, `fr`, `ja`). `null` when no locale has been chosen."""
    live: list[bool]
    """If `true`, the post is published (`job_application_status` is `live`) and its job board is also live. A post on an unpublished board is **not** `live` — its `public_url` returns a 404 until the board is enabled."""
    public_url: list[str]
    """Canonical public URL of the post on its job board, including the `gh_jid` tracking parameter. `null` when the post has no associated job board or the board has no public URL configured."""
    questions: list[list[Any]]
    """Application form questions presented to candidates on this post, including default questions (resume, cover letter, basic info) and any custom questions configured by the hiring team. Ordered as they appear on the form."""
    title: list[str]
    """Public-facing title shown to candidates on the job board (e.g. `Senior Backend Engineer, Remote`). Distinct from the internal `job.name` — a single job can have several posts with different titles, one per board, language, or geography."""
    updated_at: list[str]
    """Updated at from the Greenhouse v3 job posts record."""


class JobPostsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    active: Any
    """If `true`, the post has not been deleted. Deleted posts are excluded by default; pass `active=false` on the list endpoint to retrieve them."""
    content: Any
    """HTML body of the post shown to candidates on the job board. For internal posts this returns the `internal_content` instead. Sanitized server-side — only a limited element/attribute allowlist (including `iframe`, `video`, `source`) survives. `null` while the post is still being scaffolded."""
    created_at: Any
    """Created at from the Greenhouse v3 job posts record."""
    demographic_question_set_id: Any
    """Id of the demographic question set surfaced to candidates on this post for diversity, equity, and inclusion (DE&I) reporting. `null` when the post does not collect demographic data."""
    featured: Any
    """If `true`, the post is currently featured on the organization's internal job board and surfaces in the weekly internal-jobs email. Only internal posts can be featured, and at most three can be featured at a time."""
    first_published_at: Any
    """Timestamp the post first transitioned to `live`, in ISO 8601. `null` for posts that have never been published."""
    id: Any
    """Id from the Greenhouse v3 job posts record."""
    internal: Any
    """If `true`, the post lives on an internal job board and is visible only to existing employees signed in to the internal board. If `false`, the post is external and lives on a public-facing `job_board`. Set by the board the post is associated with at create time."""
    internal_content: Any
    """HTML body shown on the internal job board when the post is also configured as internal. `null` for external-only posts. Same sanitization rules as `content`."""
    job_board_id: Any
    """Id of the `job_board` this post is published to. Resolves to either an external (careers site, syndicated board) or internal job board depending on `internal`. Each post belongs to exactly one board at a time."""
    job_id: Any
    """Id of the parent job (requisition) this post belongs to. A single job can have multiple posts; the job is the source of truth for the hiring team, openings, and interview plan."""
    language: Any
    """ISO 639-1 locale of the post, used to render the candidate-facing application form in the matching language (e.g. `en`, `fr`, `ja`). `null` when no locale has been chosen."""
    live: Any
    """If `true`, the post is published (`job_application_status` is `live`) and its job board is also live. A post on an unpublished board is **not** `live` — its `public_url` returns a 404 until the board is enabled."""
    public_url: Any
    """Canonical public URL of the post on its job board, including the `gh_jid` tracking parameter. `null` when the post has no associated job board or the board has no public URL configured."""
    questions: Any
    """Application form questions presented to candidates on this post, including default questions (resume, cover letter, basic info) and any custom questions configured by the hiring team. Ordered as they appear on the form."""
    title: Any
    """Public-facing title shown to candidates on the job board (e.g. `Senior Backend Engineer, Remote`). Distinct from the internal `job.name` — a single job can have several posts with different titles, one per board, language, or geography."""
    updated_at: Any
    """Updated at from the Greenhouse v3 job posts record."""


class JobPostsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    active: str
    """If `true`, the post has not been deleted. Deleted posts are excluded by default; pass `active=false` on the list endpoint to retrieve them."""
    content: str
    """HTML body of the post shown to candidates on the job board. For internal posts this returns the `internal_content` instead. Sanitized server-side — only a limited element/attribute allowlist (including `iframe`, `video`, `source`) survives. `null` while the post is still being scaffolded."""
    created_at: str
    """Created at from the Greenhouse v3 job posts record."""
    demographic_question_set_id: str
    """Id of the demographic question set surfaced to candidates on this post for diversity, equity, and inclusion (DE&I) reporting. `null` when the post does not collect demographic data."""
    featured: str
    """If `true`, the post is currently featured on the organization's internal job board and surfaces in the weekly internal-jobs email. Only internal posts can be featured, and at most three can be featured at a time."""
    first_published_at: str
    """Timestamp the post first transitioned to `live`, in ISO 8601. `null` for posts that have never been published."""
    id: str
    """Id from the Greenhouse v3 job posts record."""
    internal: str
    """If `true`, the post lives on an internal job board and is visible only to existing employees signed in to the internal board. If `false`, the post is external and lives on a public-facing `job_board`. Set by the board the post is associated with at create time."""
    internal_content: str
    """HTML body shown on the internal job board when the post is also configured as internal. `null` for external-only posts. Same sanitization rules as `content`."""
    job_board_id: str
    """Id of the `job_board` this post is published to. Resolves to either an external (careers site, syndicated board) or internal job board depending on `internal`. Each post belongs to exactly one board at a time."""
    job_id: str
    """Id of the parent job (requisition) this post belongs to. A single job can have multiple posts; the job is the source of truth for the hiring team, openings, and interview plan."""
    language: str
    """ISO 639-1 locale of the post, used to render the candidate-facing application form in the matching language (e.g. `en`, `fr`, `ja`). `null` when no locale has been chosen."""
    live: str
    """If `true`, the post is published (`job_application_status` is `live`) and its job board is also live. A post on an unpublished board is **not** `live` — its `public_url` returns a 404 until the board is enabled."""
    public_url: str
    """Canonical public URL of the post on its job board, including the `gh_jid` tracking parameter. `null` when the post has no associated job board or the board has no public URL configured."""
    questions: str
    """Application form questions presented to candidates on this post, including default questions (resume, cover letter, basic info) and any custom questions configured by the hiring team. Ordered as they appear on the form."""
    title: str
    """Public-facing title shown to candidates on the job board (e.g. `Senior Backend Engineer, Remote`). Distinct from the internal `job.name` — a single job can have several posts with different titles, one per board, language, or geography."""
    updated_at: str
    """Updated at from the Greenhouse v3 job posts record."""


class JobPostsSortFilter(TypedDict, total=False):
    """Available fields for sorting job_posts search results."""
    active: AirbyteSortOrder
    """If `true`, the post has not been deleted. Deleted posts are excluded by default; pass `active=false` on the list endpoint to retrieve them."""
    content: AirbyteSortOrder
    """HTML body of the post shown to candidates on the job board. For internal posts this returns the `internal_content` instead. Sanitized server-side — only a limited element/attribute allowlist (including `iframe`, `video`, `source`) survives. `null` while the post is still being scaffolded."""
    created_at: AirbyteSortOrder
    """Created at from the Greenhouse v3 job posts record."""
    demographic_question_set_id: AirbyteSortOrder
    """Id of the demographic question set surfaced to candidates on this post for diversity, equity, and inclusion (DE&I) reporting. `null` when the post does not collect demographic data."""
    featured: AirbyteSortOrder
    """If `true`, the post is currently featured on the organization's internal job board and surfaces in the weekly internal-jobs email. Only internal posts can be featured, and at most three can be featured at a time."""
    first_published_at: AirbyteSortOrder
    """Timestamp the post first transitioned to `live`, in ISO 8601. `null` for posts that have never been published."""
    id: AirbyteSortOrder
    """Id from the Greenhouse v3 job posts record."""
    internal: AirbyteSortOrder
    """If `true`, the post lives on an internal job board and is visible only to existing employees signed in to the internal board. If `false`, the post is external and lives on a public-facing `job_board`. Set by the board the post is associated with at create time."""
    internal_content: AirbyteSortOrder
    """HTML body shown on the internal job board when the post is also configured as internal. `null` for external-only posts. Same sanitization rules as `content`."""
    job_board_id: AirbyteSortOrder
    """Id of the `job_board` this post is published to. Resolves to either an external (careers site, syndicated board) or internal job board depending on `internal`. Each post belongs to exactly one board at a time."""
    job_id: AirbyteSortOrder
    """Id of the parent job (requisition) this post belongs to. A single job can have multiple posts; the job is the source of truth for the hiring team, openings, and interview plan."""
    language: AirbyteSortOrder
    """ISO 639-1 locale of the post, used to render the candidate-facing application form in the matching language (e.g. `en`, `fr`, `ja`). `null` when no locale has been chosen."""
    live: AirbyteSortOrder
    """If `true`, the post is published (`job_application_status` is `live`) and its job board is also live. A post on an unpublished board is **not** `live` — its `public_url` returns a 404 until the board is enabled."""
    public_url: AirbyteSortOrder
    """Canonical public URL of the post on its job board, including the `gh_jid` tracking parameter. `null` when the post has no associated job board or the board has no public URL configured."""
    questions: AirbyteSortOrder
    """Application form questions presented to candidates on this post, including default questions (resume, cover letter, basic info) and any custom questions configured by the hiring team. Ordered as they appear on the form."""
    title: AirbyteSortOrder
    """Public-facing title shown to candidates on the job board (e.g. `Senior Backend Engineer, Remote`). Distinct from the internal `job.name` — a single job can have several posts with different titles, one per board, language, or geography."""
    updated_at: AirbyteSortOrder
    """Updated at from the Greenhouse v3 job posts record."""


# Entity-specific condition types for job_posts
class JobPostsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: JobPostsSearchFilter


class JobPostsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: JobPostsSearchFilter


class JobPostsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: JobPostsSearchFilter


class JobPostsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: JobPostsSearchFilter


class JobPostsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: JobPostsSearchFilter


class JobPostsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: JobPostsSearchFilter


class JobPostsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: JobPostsStringFilter


class JobPostsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: JobPostsStringFilter


class JobPostsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: JobPostsStringFilter


class JobPostsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: JobPostsStringFilter


class JobPostsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: JobPostsAnyValueFilter


class JobPostsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: JobPostsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
JobPostsInCondition = TypedDict("JobPostsInCondition", {"in": JobPostsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

JobPostsNotCondition = TypedDict("JobPostsNotCondition", {"not": "JobPostsCondition"}, total=False)
"""Negates the nested condition."""

JobPostsAndCondition = TypedDict("JobPostsAndCondition", {"and": "list[JobPostsCondition]"}, total=False)
"""True if all nested conditions are true."""

JobPostsOrCondition = TypedDict("JobPostsOrCondition", {"or": "list[JobPostsCondition]"}, total=False)
"""True if any nested condition is true."""

JobPostsAnyCondition = TypedDict("JobPostsAnyCondition", {"any": JobPostsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all job_posts condition types
JobPostsCondition = (
    JobPostsEqCondition
    | JobPostsNeqCondition
    | JobPostsGtCondition
    | JobPostsGteCondition
    | JobPostsLtCondition
    | JobPostsLteCondition
    | JobPostsInCondition
    | JobPostsStartswithCondition
    | JobPostsEndswithCondition
    | JobPostsFuzzyCondition
    | JobPostsKeywordCondition
    | JobPostsContainsCondition
    | JobPostsArrayContainsCondition
    | JobPostsNotCondition
    | JobPostsAndCondition
    | JobPostsOrCondition
    | JobPostsAnyCondition
)


class JobPostsSearchQuery(TypedDict, total=False):
    """Search query for job_posts entity."""
    filter: JobPostsCondition
    sort: list[JobPostsSortFilter]


# ===== JOBS SEARCH TYPES =====

class JobsSearchFilter(TypedDict, total=False):
    """Available fields for filtering jobs search queries."""
    closed_at: str | None
    """Timestamp the job most recently transitioned to `closed`, in ISO 8601. `null` for jobs that are still `open` or `draft`."""
    confidential: bool | None
    """If `true`, the job is restricted to users explicitly granted access on the Hiring Team. The legacy Confidential Jobs feature has been sunset — this flag cannot be set on new jobs and is preserved for jobs that already had it enabled."""
    copied_from_id: int | None
    """Id of the job (typically a template) this job was copied from on creation. `null` when the job was not created from another job."""
    created_at: str | None
    """Created at from the Greenhouse v3 jobs record."""
    custom_fields: dict[str, Any] | None
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    department_id: int | None
    """Id of the department this job is assigned to. `null` when no department is set."""
    id: int | None
    """Id from the Greenhouse v3 jobs record."""
    is_template: bool | None
    """If `true`, this job is a template used as the source for new jobs rather than a real requisition. Templates do not accept applications; reference them via `template_job_id` on `POST /v3/jobs`."""
    name: str | None
    """Internal job title shown to the hiring team in Greenhouse (e.g. `Senior Backend Engineer`). Distinct from the external-facing title on each `job_post`."""
    notes: str | None
    """Internal HTML notes about the job, surfaced to the hiring team in the Greenhouse UI. Not exposed on public job posts."""
    office_ids: list[Any] | None
    """Ids of the offices this job is assigned to. A job can span multiple offices; empty array or `null` when no offices are set."""
    opened_at: str | None
    """Timestamp the job first transitioned to `open`, in ISO 8601. `null` while the job is still in `draft`."""
    requisition_id: str | None
    """Partner-supplied external identifier for the requisition (e.g. an HRIS or ATS code). Free-form string, not unique across the organization, and `null` when no external id has been set."""
    status: str | None
    """Lifecycle status of the job. `draft` while it is being scaffolded, `open` once it has at least one open opening, and `closed` after every opening is closed. A job moves to `closed` automatically when its last open opening is closed via `PATCH /v3/openings/{id}`."""
    updated_at: str | None
    """Updated at from the Greenhouse v3 jobs record."""


class JobsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    closed_at: list[str]
    """Timestamp the job most recently transitioned to `closed`, in ISO 8601. `null` for jobs that are still `open` or `draft`."""
    confidential: list[bool]
    """If `true`, the job is restricted to users explicitly granted access on the Hiring Team. The legacy Confidential Jobs feature has been sunset — this flag cannot be set on new jobs and is preserved for jobs that already had it enabled."""
    copied_from_id: list[int]
    """Id of the job (typically a template) this job was copied from on creation. `null` when the job was not created from another job."""
    created_at: list[str]
    """Created at from the Greenhouse v3 jobs record."""
    custom_fields: list[dict[str, Any]]
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    department_id: list[int]
    """Id of the department this job is assigned to. `null` when no department is set."""
    id: list[int]
    """Id from the Greenhouse v3 jobs record."""
    is_template: list[bool]
    """If `true`, this job is a template used as the source for new jobs rather than a real requisition. Templates do not accept applications; reference them via `template_job_id` on `POST /v3/jobs`."""
    name: list[str]
    """Internal job title shown to the hiring team in Greenhouse (e.g. `Senior Backend Engineer`). Distinct from the external-facing title on each `job_post`."""
    notes: list[str]
    """Internal HTML notes about the job, surfaced to the hiring team in the Greenhouse UI. Not exposed on public job posts."""
    office_ids: list[list[Any]]
    """Ids of the offices this job is assigned to. A job can span multiple offices; empty array or `null` when no offices are set."""
    opened_at: list[str]
    """Timestamp the job first transitioned to `open`, in ISO 8601. `null` while the job is still in `draft`."""
    requisition_id: list[str]
    """Partner-supplied external identifier for the requisition (e.g. an HRIS or ATS code). Free-form string, not unique across the organization, and `null` when no external id has been set."""
    status: list[str]
    """Lifecycle status of the job. `draft` while it is being scaffolded, `open` once it has at least one open opening, and `closed` after every opening is closed. A job moves to `closed` automatically when its last open opening is closed via `PATCH /v3/openings/{id}`."""
    updated_at: list[str]
    """Updated at from the Greenhouse v3 jobs record."""


class JobsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    closed_at: Any
    """Timestamp the job most recently transitioned to `closed`, in ISO 8601. `null` for jobs that are still `open` or `draft`."""
    confidential: Any
    """If `true`, the job is restricted to users explicitly granted access on the Hiring Team. The legacy Confidential Jobs feature has been sunset — this flag cannot be set on new jobs and is preserved for jobs that already had it enabled."""
    copied_from_id: Any
    """Id of the job (typically a template) this job was copied from on creation. `null` when the job was not created from another job."""
    created_at: Any
    """Created at from the Greenhouse v3 jobs record."""
    custom_fields: Any
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    department_id: Any
    """Id of the department this job is assigned to. `null` when no department is set."""
    id: Any
    """Id from the Greenhouse v3 jobs record."""
    is_template: Any
    """If `true`, this job is a template used as the source for new jobs rather than a real requisition. Templates do not accept applications; reference them via `template_job_id` on `POST /v3/jobs`."""
    name: Any
    """Internal job title shown to the hiring team in Greenhouse (e.g. `Senior Backend Engineer`). Distinct from the external-facing title on each `job_post`."""
    notes: Any
    """Internal HTML notes about the job, surfaced to the hiring team in the Greenhouse UI. Not exposed on public job posts."""
    office_ids: Any
    """Ids of the offices this job is assigned to. A job can span multiple offices; empty array or `null` when no offices are set."""
    opened_at: Any
    """Timestamp the job first transitioned to `open`, in ISO 8601. `null` while the job is still in `draft`."""
    requisition_id: Any
    """Partner-supplied external identifier for the requisition (e.g. an HRIS or ATS code). Free-form string, not unique across the organization, and `null` when no external id has been set."""
    status: Any
    """Lifecycle status of the job. `draft` while it is being scaffolded, `open` once it has at least one open opening, and `closed` after every opening is closed. A job moves to `closed` automatically when its last open opening is closed via `PATCH /v3/openings/{id}`."""
    updated_at: Any
    """Updated at from the Greenhouse v3 jobs record."""


class JobsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    closed_at: str
    """Timestamp the job most recently transitioned to `closed`, in ISO 8601. `null` for jobs that are still `open` or `draft`."""
    confidential: str
    """If `true`, the job is restricted to users explicitly granted access on the Hiring Team. The legacy Confidential Jobs feature has been sunset — this flag cannot be set on new jobs and is preserved for jobs that already had it enabled."""
    copied_from_id: str
    """Id of the job (typically a template) this job was copied from on creation. `null` when the job was not created from another job."""
    created_at: str
    """Created at from the Greenhouse v3 jobs record."""
    custom_fields: str
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    department_id: str
    """Id of the department this job is assigned to. `null` when no department is set."""
    id: str
    """Id from the Greenhouse v3 jobs record."""
    is_template: str
    """If `true`, this job is a template used as the source for new jobs rather than a real requisition. Templates do not accept applications; reference them via `template_job_id` on `POST /v3/jobs`."""
    name: str
    """Internal job title shown to the hiring team in Greenhouse (e.g. `Senior Backend Engineer`). Distinct from the external-facing title on each `job_post`."""
    notes: str
    """Internal HTML notes about the job, surfaced to the hiring team in the Greenhouse UI. Not exposed on public job posts."""
    office_ids: str
    """Ids of the offices this job is assigned to. A job can span multiple offices; empty array or `null` when no offices are set."""
    opened_at: str
    """Timestamp the job first transitioned to `open`, in ISO 8601. `null` while the job is still in `draft`."""
    requisition_id: str
    """Partner-supplied external identifier for the requisition (e.g. an HRIS or ATS code). Free-form string, not unique across the organization, and `null` when no external id has been set."""
    status: str
    """Lifecycle status of the job. `draft` while it is being scaffolded, `open` once it has at least one open opening, and `closed` after every opening is closed. A job moves to `closed` automatically when its last open opening is closed via `PATCH /v3/openings/{id}`."""
    updated_at: str
    """Updated at from the Greenhouse v3 jobs record."""


class JobsSortFilter(TypedDict, total=False):
    """Available fields for sorting jobs search results."""
    closed_at: AirbyteSortOrder
    """Timestamp the job most recently transitioned to `closed`, in ISO 8601. `null` for jobs that are still `open` or `draft`."""
    confidential: AirbyteSortOrder
    """If `true`, the job is restricted to users explicitly granted access on the Hiring Team. The legacy Confidential Jobs feature has been sunset — this flag cannot be set on new jobs and is preserved for jobs that already had it enabled."""
    copied_from_id: AirbyteSortOrder
    """Id of the job (typically a template) this job was copied from on creation. `null` when the job was not created from another job."""
    created_at: AirbyteSortOrder
    """Created at from the Greenhouse v3 jobs record."""
    custom_fields: AirbyteSortOrder
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    department_id: AirbyteSortOrder
    """Id of the department this job is assigned to. `null` when no department is set."""
    id: AirbyteSortOrder
    """Id from the Greenhouse v3 jobs record."""
    is_template: AirbyteSortOrder
    """If `true`, this job is a template used as the source for new jobs rather than a real requisition. Templates do not accept applications; reference them via `template_job_id` on `POST /v3/jobs`."""
    name: AirbyteSortOrder
    """Internal job title shown to the hiring team in Greenhouse (e.g. `Senior Backend Engineer`). Distinct from the external-facing title on each `job_post`."""
    notes: AirbyteSortOrder
    """Internal HTML notes about the job, surfaced to the hiring team in the Greenhouse UI. Not exposed on public job posts."""
    office_ids: AirbyteSortOrder
    """Ids of the offices this job is assigned to. A job can span multiple offices; empty array or `null` when no offices are set."""
    opened_at: AirbyteSortOrder
    """Timestamp the job first transitioned to `open`, in ISO 8601. `null` while the job is still in `draft`."""
    requisition_id: AirbyteSortOrder
    """Partner-supplied external identifier for the requisition (e.g. an HRIS or ATS code). Free-form string, not unique across the organization, and `null` when no external id has been set."""
    status: AirbyteSortOrder
    """Lifecycle status of the job. `draft` while it is being scaffolded, `open` once it has at least one open opening, and `closed` after every opening is closed. A job moves to `closed` automatically when its last open opening is closed via `PATCH /v3/openings/{id}`."""
    updated_at: AirbyteSortOrder
    """Updated at from the Greenhouse v3 jobs record."""


# Entity-specific condition types for jobs
class JobsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: JobsSearchFilter


class JobsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: JobsSearchFilter


class JobsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: JobsSearchFilter


class JobsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: JobsSearchFilter


class JobsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: JobsSearchFilter


class JobsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: JobsSearchFilter


class JobsStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: JobsStringFilter


class JobsEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: JobsStringFilter


class JobsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: JobsStringFilter


class JobsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: JobsStringFilter


class JobsContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: JobsAnyValueFilter


class JobsArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: JobsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
JobsInCondition = TypedDict("JobsInCondition", {"in": JobsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

JobsNotCondition = TypedDict("JobsNotCondition", {"not": "JobsCondition"}, total=False)
"""Negates the nested condition."""

JobsAndCondition = TypedDict("JobsAndCondition", {"and": "list[JobsCondition]"}, total=False)
"""True if all nested conditions are true."""

JobsOrCondition = TypedDict("JobsOrCondition", {"or": "list[JobsCondition]"}, total=False)
"""True if any nested condition is true."""

JobsAnyCondition = TypedDict("JobsAnyCondition", {"any": JobsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all jobs condition types
JobsCondition = (
    JobsEqCondition
    | JobsNeqCondition
    | JobsGtCondition
    | JobsGteCondition
    | JobsLtCondition
    | JobsLteCondition
    | JobsInCondition
    | JobsStartswithCondition
    | JobsEndswithCondition
    | JobsFuzzyCondition
    | JobsKeywordCondition
    | JobsContainsCondition
    | JobsArrayContainsCondition
    | JobsNotCondition
    | JobsAndCondition
    | JobsOrCondition
    | JobsAnyCondition
)


class JobsSearchQuery(TypedDict, total=False):
    """Search query for jobs entity."""
    filter: JobsCondition
    sort: list[JobsSortFilter]


# ===== OFFERS SEARCH TYPES =====

class OffersSearchFilter(TypedDict, total=False):
    """Available fields for filtering offers search queries."""
    application_id: int | None
    """Id of the application this offer is extended on. Every offer belongs to exactly one application; the offer is voided if the application is rejected or deleted."""
    candidate_id: int | None
    """Id of the candidate (person) receiving this offer. Resolved through the offer's application."""
    created_at: str | None
    """Created at from the Greenhouse v3 offers record."""
    custom_fields: dict[str, Any] | None
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    id: int | None
    """Id from the Greenhouse v3 offers record."""
    job_id: int | None
    """Id of the job this offer's application is on."""
    opening_id: int | None
    """Id of the specific opening this offer is being extended for. `null` when the offer has not yet been linked to an opening."""
    resolved_at: str | None
    """Timestamp the offer was resolved (`Accepted` or `Rejected`), in ISO 8601. Date updates submitted through `PATCH /v3/offers/{id}` are normalized to noon UTC on the supplied date. `null` while the offer is still `Created` or has been superseded as `Deprecated` without a resolution."""
    sent_on: str | None
    """Date the offer was sent to the candidate, in ISO 8601 (YYYY-MM-DD). `null` until the offer has been sent."""
    starts_on: str | None
    """Candidate's proposed start date, in ISO 8601 (YYYY-MM-DD). `null` when no start date has been set on the offer."""
    status: str | None
    """Lifecycle status of the offer. `Created` for offers still being drafted or pending approval, `Accepted` once the candidate accepts, `Rejected` if declined or withdrawn, and `Deprecated` for superseded prior versions (a new offer version replaces an earlier one with this status)."""
    updated_at: str | None
    """Updated at from the Greenhouse v3 offers record."""
    version: int | None
    """Revision number of this offer within its application. Greenhouse creates a new offer row (incrementing `version`) whenever a tracked field on an existing offer changes — typically `starts_on`, `opening_id`, or a custom field configured to trigger a new version. Pair with `current_only=true` to filter the list endpoint down to the latest version per application."""


class OffersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    application_id: list[int]
    """Id of the application this offer is extended on. Every offer belongs to exactly one application; the offer is voided if the application is rejected or deleted."""
    candidate_id: list[int]
    """Id of the candidate (person) receiving this offer. Resolved through the offer's application."""
    created_at: list[str]
    """Created at from the Greenhouse v3 offers record."""
    custom_fields: list[dict[str, Any]]
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    id: list[int]
    """Id from the Greenhouse v3 offers record."""
    job_id: list[int]
    """Id of the job this offer's application is on."""
    opening_id: list[int]
    """Id of the specific opening this offer is being extended for. `null` when the offer has not yet been linked to an opening."""
    resolved_at: list[str]
    """Timestamp the offer was resolved (`Accepted` or `Rejected`), in ISO 8601. Date updates submitted through `PATCH /v3/offers/{id}` are normalized to noon UTC on the supplied date. `null` while the offer is still `Created` or has been superseded as `Deprecated` without a resolution."""
    sent_on: list[str]
    """Date the offer was sent to the candidate, in ISO 8601 (YYYY-MM-DD). `null` until the offer has been sent."""
    starts_on: list[str]
    """Candidate's proposed start date, in ISO 8601 (YYYY-MM-DD). `null` when no start date has been set on the offer."""
    status: list[str]
    """Lifecycle status of the offer. `Created` for offers still being drafted or pending approval, `Accepted` once the candidate accepts, `Rejected` if declined or withdrawn, and `Deprecated` for superseded prior versions (a new offer version replaces an earlier one with this status)."""
    updated_at: list[str]
    """Updated at from the Greenhouse v3 offers record."""
    version: list[int]
    """Revision number of this offer within its application. Greenhouse creates a new offer row (incrementing `version`) whenever a tracked field on an existing offer changes — typically `starts_on`, `opening_id`, or a custom field configured to trigger a new version. Pair with `current_only=true` to filter the list endpoint down to the latest version per application."""


class OffersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    application_id: Any
    """Id of the application this offer is extended on. Every offer belongs to exactly one application; the offer is voided if the application is rejected or deleted."""
    candidate_id: Any
    """Id of the candidate (person) receiving this offer. Resolved through the offer's application."""
    created_at: Any
    """Created at from the Greenhouse v3 offers record."""
    custom_fields: Any
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    id: Any
    """Id from the Greenhouse v3 offers record."""
    job_id: Any
    """Id of the job this offer's application is on."""
    opening_id: Any
    """Id of the specific opening this offer is being extended for. `null` when the offer has not yet been linked to an opening."""
    resolved_at: Any
    """Timestamp the offer was resolved (`Accepted` or `Rejected`), in ISO 8601. Date updates submitted through `PATCH /v3/offers/{id}` are normalized to noon UTC on the supplied date. `null` while the offer is still `Created` or has been superseded as `Deprecated` without a resolution."""
    sent_on: Any
    """Date the offer was sent to the candidate, in ISO 8601 (YYYY-MM-DD). `null` until the offer has been sent."""
    starts_on: Any
    """Candidate's proposed start date, in ISO 8601 (YYYY-MM-DD). `null` when no start date has been set on the offer."""
    status: Any
    """Lifecycle status of the offer. `Created` for offers still being drafted or pending approval, `Accepted` once the candidate accepts, `Rejected` if declined or withdrawn, and `Deprecated` for superseded prior versions (a new offer version replaces an earlier one with this status)."""
    updated_at: Any
    """Updated at from the Greenhouse v3 offers record."""
    version: Any
    """Revision number of this offer within its application. Greenhouse creates a new offer row (incrementing `version`) whenever a tracked field on an existing offer changes — typically `starts_on`, `opening_id`, or a custom field configured to trigger a new version. Pair with `current_only=true` to filter the list endpoint down to the latest version per application."""


class OffersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    application_id: str
    """Id of the application this offer is extended on. Every offer belongs to exactly one application; the offer is voided if the application is rejected or deleted."""
    candidate_id: str
    """Id of the candidate (person) receiving this offer. Resolved through the offer's application."""
    created_at: str
    """Created at from the Greenhouse v3 offers record."""
    custom_fields: str
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    id: str
    """Id from the Greenhouse v3 offers record."""
    job_id: str
    """Id of the job this offer's application is on."""
    opening_id: str
    """Id of the specific opening this offer is being extended for. `null` when the offer has not yet been linked to an opening."""
    resolved_at: str
    """Timestamp the offer was resolved (`Accepted` or `Rejected`), in ISO 8601. Date updates submitted through `PATCH /v3/offers/{id}` are normalized to noon UTC on the supplied date. `null` while the offer is still `Created` or has been superseded as `Deprecated` without a resolution."""
    sent_on: str
    """Date the offer was sent to the candidate, in ISO 8601 (YYYY-MM-DD). `null` until the offer has been sent."""
    starts_on: str
    """Candidate's proposed start date, in ISO 8601 (YYYY-MM-DD). `null` when no start date has been set on the offer."""
    status: str
    """Lifecycle status of the offer. `Created` for offers still being drafted or pending approval, `Accepted` once the candidate accepts, `Rejected` if declined or withdrawn, and `Deprecated` for superseded prior versions (a new offer version replaces an earlier one with this status)."""
    updated_at: str
    """Updated at from the Greenhouse v3 offers record."""
    version: str
    """Revision number of this offer within its application. Greenhouse creates a new offer row (incrementing `version`) whenever a tracked field on an existing offer changes — typically `starts_on`, `opening_id`, or a custom field configured to trigger a new version. Pair with `current_only=true` to filter the list endpoint down to the latest version per application."""


class OffersSortFilter(TypedDict, total=False):
    """Available fields for sorting offers search results."""
    application_id: AirbyteSortOrder
    """Id of the application this offer is extended on. Every offer belongs to exactly one application; the offer is voided if the application is rejected or deleted."""
    candidate_id: AirbyteSortOrder
    """Id of the candidate (person) receiving this offer. Resolved through the offer's application."""
    created_at: AirbyteSortOrder
    """Created at from the Greenhouse v3 offers record."""
    custom_fields: AirbyteSortOrder
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    id: AirbyteSortOrder
    """Id from the Greenhouse v3 offers record."""
    job_id: AirbyteSortOrder
    """Id of the job this offer's application is on."""
    opening_id: AirbyteSortOrder
    """Id of the specific opening this offer is being extended for. `null` when the offer has not yet been linked to an opening."""
    resolved_at: AirbyteSortOrder
    """Timestamp the offer was resolved (`Accepted` or `Rejected`), in ISO 8601. Date updates submitted through `PATCH /v3/offers/{id}` are normalized to noon UTC on the supplied date. `null` while the offer is still `Created` or has been superseded as `Deprecated` without a resolution."""
    sent_on: AirbyteSortOrder
    """Date the offer was sent to the candidate, in ISO 8601 (YYYY-MM-DD). `null` until the offer has been sent."""
    starts_on: AirbyteSortOrder
    """Candidate's proposed start date, in ISO 8601 (YYYY-MM-DD). `null` when no start date has been set on the offer."""
    status: AirbyteSortOrder
    """Lifecycle status of the offer. `Created` for offers still being drafted or pending approval, `Accepted` once the candidate accepts, `Rejected` if declined or withdrawn, and `Deprecated` for superseded prior versions (a new offer version replaces an earlier one with this status)."""
    updated_at: AirbyteSortOrder
    """Updated at from the Greenhouse v3 offers record."""
    version: AirbyteSortOrder
    """Revision number of this offer within its application. Greenhouse creates a new offer row (incrementing `version`) whenever a tracked field on an existing offer changes — typically `starts_on`, `opening_id`, or a custom field configured to trigger a new version. Pair with `current_only=true` to filter the list endpoint down to the latest version per application."""


# Entity-specific condition types for offers
class OffersEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OffersSearchFilter


class OffersNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OffersSearchFilter


class OffersGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OffersSearchFilter


class OffersGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OffersSearchFilter


class OffersLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OffersSearchFilter


class OffersLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OffersSearchFilter


class OffersStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: OffersStringFilter


class OffersEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: OffersStringFilter


class OffersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OffersStringFilter


class OffersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OffersStringFilter


class OffersContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: OffersAnyValueFilter


class OffersArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: OffersAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OffersInCondition = TypedDict("OffersInCondition", {"in": OffersInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OffersNotCondition = TypedDict("OffersNotCondition", {"not": "OffersCondition"}, total=False)
"""Negates the nested condition."""

OffersAndCondition = TypedDict("OffersAndCondition", {"and": "list[OffersCondition]"}, total=False)
"""True if all nested conditions are true."""

OffersOrCondition = TypedDict("OffersOrCondition", {"or": "list[OffersCondition]"}, total=False)
"""True if any nested condition is true."""

OffersAnyCondition = TypedDict("OffersAnyCondition", {"any": OffersAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all offers condition types
OffersCondition = (
    OffersEqCondition
    | OffersNeqCondition
    | OffersGtCondition
    | OffersGteCondition
    | OffersLtCondition
    | OffersLteCondition
    | OffersInCondition
    | OffersStartswithCondition
    | OffersEndswithCondition
    | OffersFuzzyCondition
    | OffersKeywordCondition
    | OffersContainsCondition
    | OffersArrayContainsCondition
    | OffersNotCondition
    | OffersAndCondition
    | OffersOrCondition
    | OffersAnyCondition
)


class OffersSearchQuery(TypedDict, total=False):
    """Search query for offers entity."""
    filter: OffersCondition
    sort: list[OffersSortFilter]


# ===== OFFICES SEARCH TYPES =====

class OfficesSearchFilter(TypedDict, total=False):
    """Available fields for filtering offices search queries."""
    created_at: str | None
    """Created at from the Greenhouse v3 offices record."""
    external_id: str | None
    """Stable identifier supplied by the customer or HRIS for cross-system reconciliation. `null` when no external id has been set. Available when the `org_structure_external_id` product flag is enabled."""
    id: int | None
    """Id from the Greenhouse v3 offices record."""
    location: str | None
    """Free-form physical location string for the office (e.g. `New York, NY, USA`). `null` for offices that have no location set, including most remote offices."""
    name: str | None
    """Display name of the office (e.g. `San Francisco`, `Remote (US)`). Unique among active offices in the same organization."""
    parent_id: int | None
    """Id of the parent office when offices are organized hierarchically. `null` for top-level offices. References another `/v3/offices` row in the same organization."""
    primary_in_house_contact_user_id: int | None
    """Id of the Greenhouse user designated as the office's primary internal contact, typically the local recruiting lead. References a `/v3/users` row. `null` when no contact has been assigned."""
    updated_at: str | None
    """Updated at from the Greenhouse v3 offices record."""


class OfficesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """Created at from the Greenhouse v3 offices record."""
    external_id: list[str]
    """Stable identifier supplied by the customer or HRIS for cross-system reconciliation. `null` when no external id has been set. Available when the `org_structure_external_id` product flag is enabled."""
    id: list[int]
    """Id from the Greenhouse v3 offices record."""
    location: list[str]
    """Free-form physical location string for the office (e.g. `New York, NY, USA`). `null` for offices that have no location set, including most remote offices."""
    name: list[str]
    """Display name of the office (e.g. `San Francisco`, `Remote (US)`). Unique among active offices in the same organization."""
    parent_id: list[int]
    """Id of the parent office when offices are organized hierarchically. `null` for top-level offices. References another `/v3/offices` row in the same organization."""
    primary_in_house_contact_user_id: list[int]
    """Id of the Greenhouse user designated as the office's primary internal contact, typically the local recruiting lead. References a `/v3/users` row. `null` when no contact has been assigned."""
    updated_at: list[str]
    """Updated at from the Greenhouse v3 offices record."""


class OfficesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """Created at from the Greenhouse v3 offices record."""
    external_id: Any
    """Stable identifier supplied by the customer or HRIS for cross-system reconciliation. `null` when no external id has been set. Available when the `org_structure_external_id` product flag is enabled."""
    id: Any
    """Id from the Greenhouse v3 offices record."""
    location: Any
    """Free-form physical location string for the office (e.g. `New York, NY, USA`). `null` for offices that have no location set, including most remote offices."""
    name: Any
    """Display name of the office (e.g. `San Francisco`, `Remote (US)`). Unique among active offices in the same organization."""
    parent_id: Any
    """Id of the parent office when offices are organized hierarchically. `null` for top-level offices. References another `/v3/offices` row in the same organization."""
    primary_in_house_contact_user_id: Any
    """Id of the Greenhouse user designated as the office's primary internal contact, typically the local recruiting lead. References a `/v3/users` row. `null` when no contact has been assigned."""
    updated_at: Any
    """Updated at from the Greenhouse v3 offices record."""


class OfficesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    created_at: str
    """Created at from the Greenhouse v3 offices record."""
    external_id: str
    """Stable identifier supplied by the customer or HRIS for cross-system reconciliation. `null` when no external id has been set. Available when the `org_structure_external_id` product flag is enabled."""
    id: str
    """Id from the Greenhouse v3 offices record."""
    location: str
    """Free-form physical location string for the office (e.g. `New York, NY, USA`). `null` for offices that have no location set, including most remote offices."""
    name: str
    """Display name of the office (e.g. `San Francisco`, `Remote (US)`). Unique among active offices in the same organization."""
    parent_id: str
    """Id of the parent office when offices are organized hierarchically. `null` for top-level offices. References another `/v3/offices` row in the same organization."""
    primary_in_house_contact_user_id: str
    """Id of the Greenhouse user designated as the office's primary internal contact, typically the local recruiting lead. References a `/v3/users` row. `null` when no contact has been assigned."""
    updated_at: str
    """Updated at from the Greenhouse v3 offices record."""


class OfficesSortFilter(TypedDict, total=False):
    """Available fields for sorting offices search results."""
    created_at: AirbyteSortOrder
    """Created at from the Greenhouse v3 offices record."""
    external_id: AirbyteSortOrder
    """Stable identifier supplied by the customer or HRIS for cross-system reconciliation. `null` when no external id has been set. Available when the `org_structure_external_id` product flag is enabled."""
    id: AirbyteSortOrder
    """Id from the Greenhouse v3 offices record."""
    location: AirbyteSortOrder
    """Free-form physical location string for the office (e.g. `New York, NY, USA`). `null` for offices that have no location set, including most remote offices."""
    name: AirbyteSortOrder
    """Display name of the office (e.g. `San Francisco`, `Remote (US)`). Unique among active offices in the same organization."""
    parent_id: AirbyteSortOrder
    """Id of the parent office when offices are organized hierarchically. `null` for top-level offices. References another `/v3/offices` row in the same organization."""
    primary_in_house_contact_user_id: AirbyteSortOrder
    """Id of the Greenhouse user designated as the office's primary internal contact, typically the local recruiting lead. References a `/v3/users` row. `null` when no contact has been assigned."""
    updated_at: AirbyteSortOrder
    """Updated at from the Greenhouse v3 offices record."""


# Entity-specific condition types for offices
class OfficesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: OfficesSearchFilter


class OfficesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: OfficesSearchFilter


class OfficesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: OfficesSearchFilter


class OfficesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: OfficesSearchFilter


class OfficesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: OfficesSearchFilter


class OfficesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: OfficesSearchFilter


class OfficesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: OfficesStringFilter


class OfficesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: OfficesStringFilter


class OfficesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: OfficesStringFilter


class OfficesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: OfficesStringFilter


class OfficesContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: OfficesAnyValueFilter


class OfficesArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: OfficesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
OfficesInCondition = TypedDict("OfficesInCondition", {"in": OfficesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

OfficesNotCondition = TypedDict("OfficesNotCondition", {"not": "OfficesCondition"}, total=False)
"""Negates the nested condition."""

OfficesAndCondition = TypedDict("OfficesAndCondition", {"and": "list[OfficesCondition]"}, total=False)
"""True if all nested conditions are true."""

OfficesOrCondition = TypedDict("OfficesOrCondition", {"or": "list[OfficesCondition]"}, total=False)
"""True if any nested condition is true."""

OfficesAnyCondition = TypedDict("OfficesAnyCondition", {"any": OfficesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all offices condition types
OfficesCondition = (
    OfficesEqCondition
    | OfficesNeqCondition
    | OfficesGtCondition
    | OfficesGteCondition
    | OfficesLtCondition
    | OfficesLteCondition
    | OfficesInCondition
    | OfficesStartswithCondition
    | OfficesEndswithCondition
    | OfficesFuzzyCondition
    | OfficesKeywordCondition
    | OfficesContainsCondition
    | OfficesArrayContainsCondition
    | OfficesNotCondition
    | OfficesAndCondition
    | OfficesOrCondition
    | OfficesAnyCondition
)


class OfficesSearchQuery(TypedDict, total=False):
    """Search query for offices entity."""
    filter: OfficesCondition
    sort: list[OfficesSortFilter]


# ===== SOURCES SEARCH TYPES =====

class SourcesSearchFilter(TypedDict, total=False):
    """Available fields for filtering sources search queries."""
    created_at: str | None
    """Created at from the Greenhouse v3 sources record."""
    id: int | None
    """Id from the Greenhouse v3 sources record."""
    name: str | None
    """Display name of the source as recruiters see it in Greenhouse (e.g. `LinkedIn (Prospecting)`, `Indeed`, `Referral`, `Internal Applicant`, or a custom agency name). For organization-specific sources this is the label the org configured; for global Greenhouse sources it is the standard public name."""
    type_: dict[str, Any] | None
    """The sourcing strategy this source rolls up to — the broader category used for reporting. Sources are grouped under sourcing strategies such as `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`, `Company marketing`, `In person event`, `MyGreenhouse`, and `Other`. Use the strategy when aggregating candidate volume by channel; use the source itself when reporting on a specific channel within that category."""
    updated_at: str | None
    """Updated at from the Greenhouse v3 sources record."""


class SourcesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    created_at: list[str]
    """Created at from the Greenhouse v3 sources record."""
    id: list[int]
    """Id from the Greenhouse v3 sources record."""
    name: list[str]
    """Display name of the source as recruiters see it in Greenhouse (e.g. `LinkedIn (Prospecting)`, `Indeed`, `Referral`, `Internal Applicant`, or a custom agency name). For organization-specific sources this is the label the org configured; for global Greenhouse sources it is the standard public name."""
    type_: list[dict[str, Any]]
    """The sourcing strategy this source rolls up to — the broader category used for reporting. Sources are grouped under sourcing strategies such as `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`, `Company marketing`, `In person event`, `MyGreenhouse`, and `Other`. Use the strategy when aggregating candidate volume by channel; use the source itself when reporting on a specific channel within that category."""
    updated_at: list[str]
    """Updated at from the Greenhouse v3 sources record."""


class SourcesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    created_at: Any
    """Created at from the Greenhouse v3 sources record."""
    id: Any
    """Id from the Greenhouse v3 sources record."""
    name: Any
    """Display name of the source as recruiters see it in Greenhouse (e.g. `LinkedIn (Prospecting)`, `Indeed`, `Referral`, `Internal Applicant`, or a custom agency name). For organization-specific sources this is the label the org configured; for global Greenhouse sources it is the standard public name."""
    type_: Any
    """The sourcing strategy this source rolls up to — the broader category used for reporting. Sources are grouped under sourcing strategies such as `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`, `Company marketing`, `In person event`, `MyGreenhouse`, and `Other`. Use the strategy when aggregating candidate volume by channel; use the source itself when reporting on a specific channel within that category."""
    updated_at: Any
    """Updated at from the Greenhouse v3 sources record."""


class SourcesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    created_at: str
    """Created at from the Greenhouse v3 sources record."""
    id: str
    """Id from the Greenhouse v3 sources record."""
    name: str
    """Display name of the source as recruiters see it in Greenhouse (e.g. `LinkedIn (Prospecting)`, `Indeed`, `Referral`, `Internal Applicant`, or a custom agency name). For organization-specific sources this is the label the org configured; for global Greenhouse sources it is the standard public name."""
    type_: str
    """The sourcing strategy this source rolls up to — the broader category used for reporting. Sources are grouped under sourcing strategies such as `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`, `Company marketing`, `In person event`, `MyGreenhouse`, and `Other`. Use the strategy when aggregating candidate volume by channel; use the source itself when reporting on a specific channel within that category."""
    updated_at: str
    """Updated at from the Greenhouse v3 sources record."""


class SourcesSortFilter(TypedDict, total=False):
    """Available fields for sorting sources search results."""
    created_at: AirbyteSortOrder
    """Created at from the Greenhouse v3 sources record."""
    id: AirbyteSortOrder
    """Id from the Greenhouse v3 sources record."""
    name: AirbyteSortOrder
    """Display name of the source as recruiters see it in Greenhouse (e.g. `LinkedIn (Prospecting)`, `Indeed`, `Referral`, `Internal Applicant`, or a custom agency name). For organization-specific sources this is the label the org configured; for global Greenhouse sources it is the standard public name."""
    type_: AirbyteSortOrder
    """The sourcing strategy this source rolls up to — the broader category used for reporting. Sources are grouped under sourcing strategies such as `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`, `Company marketing`, `In person event`, `MyGreenhouse`, and `Other`. Use the strategy when aggregating candidate volume by channel; use the source itself when reporting on a specific channel within that category."""
    updated_at: AirbyteSortOrder
    """Updated at from the Greenhouse v3 sources record."""


# Entity-specific condition types for sources
class SourcesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: SourcesSearchFilter


class SourcesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: SourcesSearchFilter


class SourcesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: SourcesSearchFilter


class SourcesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: SourcesSearchFilter


class SourcesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: SourcesSearchFilter


class SourcesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: SourcesSearchFilter


class SourcesStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: SourcesStringFilter


class SourcesEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: SourcesStringFilter


class SourcesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: SourcesStringFilter


class SourcesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: SourcesStringFilter


class SourcesContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: SourcesAnyValueFilter


class SourcesArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: SourcesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
SourcesInCondition = TypedDict("SourcesInCondition", {"in": SourcesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

SourcesNotCondition = TypedDict("SourcesNotCondition", {"not": "SourcesCondition"}, total=False)
"""Negates the nested condition."""

SourcesAndCondition = TypedDict("SourcesAndCondition", {"and": "list[SourcesCondition]"}, total=False)
"""True if all nested conditions are true."""

SourcesOrCondition = TypedDict("SourcesOrCondition", {"or": "list[SourcesCondition]"}, total=False)
"""True if any nested condition is true."""

SourcesAnyCondition = TypedDict("SourcesAnyCondition", {"any": SourcesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all sources condition types
SourcesCondition = (
    SourcesEqCondition
    | SourcesNeqCondition
    | SourcesGtCondition
    | SourcesGteCondition
    | SourcesLtCondition
    | SourcesLteCondition
    | SourcesInCondition
    | SourcesStartswithCondition
    | SourcesEndswithCondition
    | SourcesFuzzyCondition
    | SourcesKeywordCondition
    | SourcesContainsCondition
    | SourcesArrayContainsCondition
    | SourcesNotCondition
    | SourcesAndCondition
    | SourcesOrCondition
    | SourcesAnyCondition
)


class SourcesSearchQuery(TypedDict, total=False):
    """Search query for sources entity."""
    filter: SourcesCondition
    sort: list[SourcesSortFilter]


# ===== USERS SEARCH TYPES =====

class UsersSearchFilter(TypedDict, total=False):
    """Available fields for filtering users search queries."""
    agency_id: int | None
    """Id of the staffing agency this user belongs to, when the user is an external agency recruiter rather than an employee of your organization. `null` for in-house users."""
    created_at: str | None
    """Created at from the Greenhouse v3 users record."""
    custom_fields: dict[str, Any] | None
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    deactivated: bool | None
    """Whether the user has been deactivated. Deactivated users cannot sign in or be assigned to new jobs, but their historical activity (notes, scorecards, emails) is preserved. Toggle via `POST /v3/users/{id}/deactivate` and `POST /v3/users/{id}/activate`."""
    department_ids: list[Any] | None
    """Ids of the departments this user is assigned to. Used to scope future job permissions and to filter the user list by department. Empty when the user is not pinned to any department."""
    emails: list[Any] | None
    """All email addresses on the user's account, including the primary address and any additional verified addresses."""
    employee_id: str | None
    """Partner-supplied external employee identifier, typically the user's HRIS or payroll id. Free-form string; not unique across organizations and `null` when no employee id has been set."""
    first_name: str | None
    """First name from the Greenhouse v3 users record."""
    id: int | None
    """Id from the Greenhouse v3 users record."""
    interviewer_tags: list[Any] | None
    """Interviewer tags applied to this user — the labeled skill or panel groupings (e.g. `Senior Engineer`, `Bar Raiser`) used to suggest qualified interviewers when building an interview plan. Each entry pairs the tag's `id` with its `name`."""
    job_title: str | None
    """Free-form job title set on the user's Greenhouse profile (e.g. `Senior Recruiter`). Not synchronized with any HRIS title."""
    last_name: str | None
    """Last name from the Greenhouse v3 users record."""
    linked_candidate_ids: list[Any] | None
    """Ids of candidate records linked to this user. Populated when an employee is represented by both a user record (for Greenhouse access) and a candidate record (for past or internal applications)."""
    name: str | None
    """Concatenation of `first_name` and `last_name` rendered as a single display string. Provided for convenience; partners that need either component should read `first_name`/`last_name` directly."""
    office_ids: list[Any] | None
    """Ids of the offices this user is assigned to. Used to scope future job permissions and to filter the user list by office. Empty when the user is not pinned to any office."""
    primary_email: str | None
    """Primary email address on the user's account. Sign-in identifier and the address Greenhouse uses for outbound mail; additional verified addresses are not surfaced here. Service accounts (integration/ISU users) have no email and are excluded from this endpoint by default; when included via `show_service_accounts=true`, their `primary_email` is an empty string."""
    site_admin: bool | None
    """Whether the user holds the Site Admin role. Site admins have unrestricted access to every non-confidential job and to organization-level settings. Demote a site admin to a Basic user with `POST /v3/users/{id}/revoke_permissions`."""
    updated_at: str | None
    """Updated at from the Greenhouse v3 users record."""


class UsersInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    agency_id: list[int]
    """Id of the staffing agency this user belongs to, when the user is an external agency recruiter rather than an employee of your organization. `null` for in-house users."""
    created_at: list[str]
    """Created at from the Greenhouse v3 users record."""
    custom_fields: list[dict[str, Any]]
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    deactivated: list[bool]
    """Whether the user has been deactivated. Deactivated users cannot sign in or be assigned to new jobs, but their historical activity (notes, scorecards, emails) is preserved. Toggle via `POST /v3/users/{id}/deactivate` and `POST /v3/users/{id}/activate`."""
    department_ids: list[list[Any]]
    """Ids of the departments this user is assigned to. Used to scope future job permissions and to filter the user list by department. Empty when the user is not pinned to any department."""
    emails: list[list[Any]]
    """All email addresses on the user's account, including the primary address and any additional verified addresses."""
    employee_id: list[str]
    """Partner-supplied external employee identifier, typically the user's HRIS or payroll id. Free-form string; not unique across organizations and `null` when no employee id has been set."""
    first_name: list[str]
    """First name from the Greenhouse v3 users record."""
    id: list[int]
    """Id from the Greenhouse v3 users record."""
    interviewer_tags: list[list[Any]]
    """Interviewer tags applied to this user — the labeled skill or panel groupings (e.g. `Senior Engineer`, `Bar Raiser`) used to suggest qualified interviewers when building an interview plan. Each entry pairs the tag's `id` with its `name`."""
    job_title: list[str]
    """Free-form job title set on the user's Greenhouse profile (e.g. `Senior Recruiter`). Not synchronized with any HRIS title."""
    last_name: list[str]
    """Last name from the Greenhouse v3 users record."""
    linked_candidate_ids: list[list[Any]]
    """Ids of candidate records linked to this user. Populated when an employee is represented by both a user record (for Greenhouse access) and a candidate record (for past or internal applications)."""
    name: list[str]
    """Concatenation of `first_name` and `last_name` rendered as a single display string. Provided for convenience; partners that need either component should read `first_name`/`last_name` directly."""
    office_ids: list[list[Any]]
    """Ids of the offices this user is assigned to. Used to scope future job permissions and to filter the user list by office. Empty when the user is not pinned to any office."""
    primary_email: list[str]
    """Primary email address on the user's account. Sign-in identifier and the address Greenhouse uses for outbound mail; additional verified addresses are not surfaced here. Service accounts (integration/ISU users) have no email and are excluded from this endpoint by default; when included via `show_service_accounts=true`, their `primary_email` is an empty string."""
    site_admin: list[bool]
    """Whether the user holds the Site Admin role. Site admins have unrestricted access to every non-confidential job and to organization-level settings. Demote a site admin to a Basic user with `POST /v3/users/{id}/revoke_permissions`."""
    updated_at: list[str]
    """Updated at from the Greenhouse v3 users record."""


class UsersAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    agency_id: Any
    """Id of the staffing agency this user belongs to, when the user is an external agency recruiter rather than an employee of your organization. `null` for in-house users."""
    created_at: Any
    """Created at from the Greenhouse v3 users record."""
    custom_fields: Any
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    deactivated: Any
    """Whether the user has been deactivated. Deactivated users cannot sign in or be assigned to new jobs, but their historical activity (notes, scorecards, emails) is preserved. Toggle via `POST /v3/users/{id}/deactivate` and `POST /v3/users/{id}/activate`."""
    department_ids: Any
    """Ids of the departments this user is assigned to. Used to scope future job permissions and to filter the user list by department. Empty when the user is not pinned to any department."""
    emails: Any
    """All email addresses on the user's account, including the primary address and any additional verified addresses."""
    employee_id: Any
    """Partner-supplied external employee identifier, typically the user's HRIS or payroll id. Free-form string; not unique across organizations and `null` when no employee id has been set."""
    first_name: Any
    """First name from the Greenhouse v3 users record."""
    id: Any
    """Id from the Greenhouse v3 users record."""
    interviewer_tags: Any
    """Interviewer tags applied to this user — the labeled skill or panel groupings (e.g. `Senior Engineer`, `Bar Raiser`) used to suggest qualified interviewers when building an interview plan. Each entry pairs the tag's `id` with its `name`."""
    job_title: Any
    """Free-form job title set on the user's Greenhouse profile (e.g. `Senior Recruiter`). Not synchronized with any HRIS title."""
    last_name: Any
    """Last name from the Greenhouse v3 users record."""
    linked_candidate_ids: Any
    """Ids of candidate records linked to this user. Populated when an employee is represented by both a user record (for Greenhouse access) and a candidate record (for past or internal applications)."""
    name: Any
    """Concatenation of `first_name` and `last_name` rendered as a single display string. Provided for convenience; partners that need either component should read `first_name`/`last_name` directly."""
    office_ids: Any
    """Ids of the offices this user is assigned to. Used to scope future job permissions and to filter the user list by office. Empty when the user is not pinned to any office."""
    primary_email: Any
    """Primary email address on the user's account. Sign-in identifier and the address Greenhouse uses for outbound mail; additional verified addresses are not surfaced here. Service accounts (integration/ISU users) have no email and are excluded from this endpoint by default; when included via `show_service_accounts=true`, their `primary_email` is an empty string."""
    site_admin: Any
    """Whether the user holds the Site Admin role. Site admins have unrestricted access to every non-confidential job and to organization-level settings. Demote a site admin to a Basic user with `POST /v3/users/{id}/revoke_permissions`."""
    updated_at: Any
    """Updated at from the Greenhouse v3 users record."""


class UsersStringFilter(TypedDict, total=False):
    """String fields for text search conditions (startswith, endswith, fuzzy, keyword)."""
    agency_id: str
    """Id of the staffing agency this user belongs to, when the user is an external agency recruiter rather than an employee of your organization. `null` for in-house users."""
    created_at: str
    """Created at from the Greenhouse v3 users record."""
    custom_fields: str
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    deactivated: str
    """Whether the user has been deactivated. Deactivated users cannot sign in or be assigned to new jobs, but their historical activity (notes, scorecards, emails) is preserved. Toggle via `POST /v3/users/{id}/deactivate` and `POST /v3/users/{id}/activate`."""
    department_ids: str
    """Ids of the departments this user is assigned to. Used to scope future job permissions and to filter the user list by department. Empty when the user is not pinned to any department."""
    emails: str
    """All email addresses on the user's account, including the primary address and any additional verified addresses."""
    employee_id: str
    """Partner-supplied external employee identifier, typically the user's HRIS or payroll id. Free-form string; not unique across organizations and `null` when no employee id has been set."""
    first_name: str
    """First name from the Greenhouse v3 users record."""
    id: str
    """Id from the Greenhouse v3 users record."""
    interviewer_tags: str
    """Interviewer tags applied to this user — the labeled skill or panel groupings (e.g. `Senior Engineer`, `Bar Raiser`) used to suggest qualified interviewers when building an interview plan. Each entry pairs the tag's `id` with its `name`."""
    job_title: str
    """Free-form job title set on the user's Greenhouse profile (e.g. `Senior Recruiter`). Not synchronized with any HRIS title."""
    last_name: str
    """Last name from the Greenhouse v3 users record."""
    linked_candidate_ids: str
    """Ids of candidate records linked to this user. Populated when an employee is represented by both a user record (for Greenhouse access) and a candidate record (for past or internal applications)."""
    name: str
    """Concatenation of `first_name` and `last_name` rendered as a single display string. Provided for convenience; partners that need either component should read `first_name`/`last_name` directly."""
    office_ids: str
    """Ids of the offices this user is assigned to. Used to scope future job permissions and to filter the user list by office. Empty when the user is not pinned to any office."""
    primary_email: str
    """Primary email address on the user's account. Sign-in identifier and the address Greenhouse uses for outbound mail; additional verified addresses are not surfaced here. Service accounts (integration/ISU users) have no email and are excluded from this endpoint by default; when included via `show_service_accounts=true`, their `primary_email` is an empty string."""
    site_admin: str
    """Whether the user holds the Site Admin role. Site admins have unrestricted access to every non-confidential job and to organization-level settings. Demote a site admin to a Basic user with `POST /v3/users/{id}/revoke_permissions`."""
    updated_at: str
    """Updated at from the Greenhouse v3 users record."""


class UsersSortFilter(TypedDict, total=False):
    """Available fields for sorting users search results."""
    agency_id: AirbyteSortOrder
    """Id of the staffing agency this user belongs to, when the user is an external agency recruiter rather than an employee of your organization. `null` for in-house users."""
    created_at: AirbyteSortOrder
    """Created at from the Greenhouse v3 users record."""
    custom_fields: AirbyteSortOrder
    """Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`."""
    deactivated: AirbyteSortOrder
    """Whether the user has been deactivated. Deactivated users cannot sign in or be assigned to new jobs, but their historical activity (notes, scorecards, emails) is preserved. Toggle via `POST /v3/users/{id}/deactivate` and `POST /v3/users/{id}/activate`."""
    department_ids: AirbyteSortOrder
    """Ids of the departments this user is assigned to. Used to scope future job permissions and to filter the user list by department. Empty when the user is not pinned to any department."""
    emails: AirbyteSortOrder
    """All email addresses on the user's account, including the primary address and any additional verified addresses."""
    employee_id: AirbyteSortOrder
    """Partner-supplied external employee identifier, typically the user's HRIS or payroll id. Free-form string; not unique across organizations and `null` when no employee id has been set."""
    first_name: AirbyteSortOrder
    """First name from the Greenhouse v3 users record."""
    id: AirbyteSortOrder
    """Id from the Greenhouse v3 users record."""
    interviewer_tags: AirbyteSortOrder
    """Interviewer tags applied to this user — the labeled skill or panel groupings (e.g. `Senior Engineer`, `Bar Raiser`) used to suggest qualified interviewers when building an interview plan. Each entry pairs the tag's `id` with its `name`."""
    job_title: AirbyteSortOrder
    """Free-form job title set on the user's Greenhouse profile (e.g. `Senior Recruiter`). Not synchronized with any HRIS title."""
    last_name: AirbyteSortOrder
    """Last name from the Greenhouse v3 users record."""
    linked_candidate_ids: AirbyteSortOrder
    """Ids of candidate records linked to this user. Populated when an employee is represented by both a user record (for Greenhouse access) and a candidate record (for past or internal applications)."""
    name: AirbyteSortOrder
    """Concatenation of `first_name` and `last_name` rendered as a single display string. Provided for convenience; partners that need either component should read `first_name`/`last_name` directly."""
    office_ids: AirbyteSortOrder
    """Ids of the offices this user is assigned to. Used to scope future job permissions and to filter the user list by office. Empty when the user is not pinned to any office."""
    primary_email: AirbyteSortOrder
    """Primary email address on the user's account. Sign-in identifier and the address Greenhouse uses for outbound mail; additional verified addresses are not surfaced here. Service accounts (integration/ISU users) have no email and are excluded from this endpoint by default; when included via `show_service_accounts=true`, their `primary_email` is an empty string."""
    site_admin: AirbyteSortOrder
    """Whether the user holds the Site Admin role. Site admins have unrestricted access to every non-confidential job and to organization-level settings. Demote a site admin to a Basic user with `POST /v3/users/{id}/revoke_permissions`."""
    updated_at: AirbyteSortOrder
    """Updated at from the Greenhouse v3 users record."""


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


class UsersStartswithCondition(TypedDict, total=False):
    """Literal case-insensitive prefix match."""
    startswith: UsersStringFilter


class UsersEndswithCondition(TypedDict, total=False):
    """Literal case-insensitive suffix match."""
    endswith: UsersStringFilter


class UsersFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: UsersStringFilter


class UsersKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: UsersStringFilter


class UsersContainsCondition(TypedDict, total=False):
    """Case-insensitive substring match on a scalar field. Example: {"contains": {"subject": "billing"}}"""
    contains: UsersAnyValueFilter


class UsersArrayContainsCondition(TypedDict, total=False):
    """Exact membership test on an array field. Example: {"array_contains": {"tags": "premium"}}"""
    array_contains: UsersAnyValueFilter


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
    | UsersStartswithCondition
    | UsersEndswithCondition
    | UsersFuzzyCondition
    | UsersKeywordCondition
    | UsersContainsCondition
    | UsersArrayContainsCondition
    | UsersNotCondition
    | UsersAndCondition
    | UsersOrCondition
    | UsersAnyCondition
)


class UsersSearchQuery(TypedDict, total=False):
    """Search query for users entity."""
    filter: UsersCondition
    sort: list[UsersSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
