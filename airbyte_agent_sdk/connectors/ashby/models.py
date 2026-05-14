"""
Pydantic models for ashby connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class AshbyAuthConfig(BaseModel):
    """API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your Ashby API key"""

# Replication configuration

class AshbyReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Ashby."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """The date from which to start replicating data, in the format YYYY-MM-DDT00:00:00Z."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class CandidateTagsItem(BaseModel):
    """Nested schema for Candidate.tags_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    title: str | None | None = Field(default=None)
    is_archived: bool | None | None = Field(default=None, alias="isArchived")

class CandidatePhonenumbersItem(BaseModel):
    """Nested schema for Candidate.phoneNumbers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    is_primary: bool | None | None = Field(default=None, alias="isPrimary")

class CandidateEmailaddressesItem(BaseModel):
    """Nested schema for Candidate.emailAddresses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    is_primary: bool | None | None = Field(default=None, alias="isPrimary")

class CandidateSociallinksItem(BaseModel):
    """Nested schema for Candidate.socialLinks_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type_: str | None | None = Field(default=None, alias="type")
    url: str | None | None = Field(default=None)

class Candidate(BaseModel):
    """Candidate object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    name: str | None = Field(default=None)
    email_addresses: list[CandidateEmailaddressesItem] | None = Field(default=None, alias="emailAddresses")
    phone_numbers: list[CandidatePhonenumbersItem] | None = Field(default=None, alias="phoneNumbers")
    social_links: list[CandidateSociallinksItem] | None = Field(default=None, alias="socialLinks")
    tags: list[CandidateTagsItem] | None = Field(default=None)
    application_ids: list[str | None] | None = Field(default=None, alias="applicationIds")
    file_handles: list[Any] | None = Field(default=None, alias="fileHandles")
    custom_fields: list[Any] | None = Field(default=None, alias="customFields")
    profile_url: str | None = Field(default=None, alias="profileUrl")
    source: Any | None = Field(default=None)
    credited_to_user: Any | None = Field(default=None, alias="creditedToUser")
    timezone: str | None = Field(default=None)

class ApplicationHiringteamItem(BaseModel):
    """Nested schema for Application.hiringTeam_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_id: str | None | None = Field(default=None, alias="userId")
    first_name: str | None | None = Field(default=None, alias="firstName")
    last_name: str | None | None = Field(default=None, alias="lastName")
    email: str | None | None = Field(default=None)
    role: str | None | None = Field(default=None)

class Application(BaseModel):
    """Application object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    archived_at: str | None = Field(default=None, alias="archivedAt")
    candidate: Any | None = Field(default=None)
    status: str | None = Field(default=None)
    custom_fields: list[Any] | None = Field(default=None, alias="customFields")
    current_interview_stage: Any | None = Field(default=None, alias="currentInterviewStage")
    source: Any | None = Field(default=None)
    credited_to_user: Any | None = Field(default=None, alias="creditedToUser")
    archive_reason: Any | None = Field(default=None, alias="archiveReason")
    job: Any | None = Field(default=None)
    hiring_team: list[ApplicationHiringteamItem] | None = Field(default=None, alias="hiringTeam")
    applied_via_job_posting_id: str | None = Field(default=None, alias="appliedViaJobPostingId")
    submitter_client_ip: str | None = Field(default=None, alias="submitterClientIp")
    submitter_user_agent: str | None = Field(default=None, alias="submitterUserAgent")

class JobCustomfieldsItem(BaseModel):
    """Nested schema for Job.customFields_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    is_private: bool | None | None = Field(default=None, alias="isPrivate")
    title: str | None | None = Field(default=None)
    value: str | None | None = Field(default=None)
    value_label: str | None | None = Field(default=None, alias="valueLabel")

class JobHiringteamItem(BaseModel):
    """Nested schema for Job.hiringTeam_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_id: str | None | None = Field(default=None, alias="userId")
    first_name: str | None | None = Field(default=None, alias="firstName")
    last_name: str | None | None = Field(default=None, alias="lastName")
    email: str | None | None = Field(default=None)
    role: str | None | None = Field(default=None)

class Job(BaseModel):
    """Job object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    title: str | None = Field(default=None)
    confidential: bool | None = Field(default=None)
    status: str | None = Field(default=None)
    employment_type: str | None = Field(default=None, alias="employmentType")
    location_id: str | None = Field(default=None, alias="locationId")
    department_id: str | None = Field(default=None, alias="departmentId")
    default_interview_plan_id: str | None = Field(default=None, alias="defaultInterviewPlanId")
    interview_plan_ids: list[str | None] | None = Field(default=None, alias="interviewPlanIds")
    job_posting_ids: list[str | None] | None = Field(default=None, alias="jobPostingIds")
    custom_fields: list[JobCustomfieldsItem] | None = Field(default=None, alias="customFields")
    hiring_team: list[JobHiringteamItem] | None = Field(default=None, alias="hiringTeam")
    custom_requisition_id: str | None = Field(default=None, alias="customRequisitionId")
    brand_id: str | None = Field(default=None, alias="brandId")
    author: Any | None = Field(default=None)
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    opened_at: str | None = Field(default=None, alias="openedAt")
    closed_at: str | None = Field(default=None, alias="closedAt")

class Department(BaseModel):
    """Department object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    name: str | None = Field(default=None)
    external_name: str | None = Field(default=None, alias="externalName")
    is_archived: bool | None = Field(default=None, alias="isArchived")
    parent_id: str | None = Field(default=None, alias="parentId")
    created_at: str | None = Field(default=None, alias="createdAt")
    updated_at: str | None = Field(default=None, alias="updatedAt")
    extra_data: Any | None = Field(default=None, alias="extraData")

class Location(BaseModel):
    """Location object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    name: str | None = Field(default=None)
    external_name: str | None = Field(default=None, alias="externalName")
    is_archived: bool | None = Field(default=None, alias="isArchived")
    address: Any | None = Field(default=None)
    is_remote: bool | None = Field(default=None, alias="isRemote")
    workplace_type: str | None = Field(default=None, alias="workplaceType")
    parent_location_id: str | None = Field(default=None, alias="parentLocationId")
    type_: str | None = Field(default=None, alias="type")
    extra_data: Any | None = Field(default=None, alias="extraData")

class User(BaseModel):
    """User object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    first_name: str | None = Field(default=None, alias="firstName")
    last_name: str | None = Field(default=None, alias="lastName")
    email: str | None = Field(default=None)
    global_role: str | None = Field(default=None, alias="globalRole")
    is_enabled: bool | None = Field(default=None, alias="isEnabled")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class JobPosting(BaseModel):
    """Job posting object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    title: str | None = Field(default=None)
    job_id: str | None = Field(default=None, alias="jobId")
    department_name: str | None = Field(default=None, alias="departmentName")
    team_name: str | None = Field(default=None, alias="teamName")
    location_name: str | None = Field(default=None, alias="locationName")
    location_external_name: str | None = Field(default=None, alias="locationExternalName")
    workplace_type: str | None = Field(default=None, alias="workplaceType")
    employment_type: str | None = Field(default=None, alias="employmentType")
    is_listed: bool | None = Field(default=None, alias="isListed")
    published_date: str | None = Field(default=None, alias="publishedDate")
    application_deadline: str | None = Field(default=None, alias="applicationDeadline")
    external_link: str | None = Field(default=None, alias="externalLink")
    apply_link: str | None = Field(default=None, alias="applyLink")
    location_ids: Any | None = Field(default=None, alias="locationIds")
    compensation_tier_summary: str | None = Field(default=None, alias="compensationTierSummary")
    should_display_compensation_on_job_board: bool | None = Field(default=None, alias="shouldDisplayCompensationOnJobBoard")
    updated_at: str | None = Field(default=None, alias="updatedAt")

class Source(BaseModel):
    """Candidate source object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    title: str | None = Field(default=None)
    is_archived: bool | None = Field(default=None, alias="isArchived")
    source_type: Any | None = Field(default=None, alias="sourceType")

class ArchiveReason(BaseModel):
    """Archive reason object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    text: str | None = Field(default=None)
    reason_type: str | None = Field(default=None, alias="reasonType")
    is_archived: bool | None = Field(default=None, alias="isArchived")

class CandidateTag(BaseModel):
    """Candidate tag object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    title: str | None = Field(default=None)
    is_archived: bool | None = Field(default=None, alias="isArchived")

class CustomField(BaseModel):
    """Custom field definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    title: str | None = Field(default=None)
    object_type: str | None = Field(default=None, alias="objectType")
    is_archived: bool | None = Field(default=None, alias="isArchived")
    is_private: bool | None = Field(default=None, alias="isPrivate")
    field_type: str | None = Field(default=None, alias="fieldType")

class FeedbackFormDefinition(BaseModel):
    """Feedback form definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str
    organization_id: str | None = Field(default=None, alias="organizationId")
    title: str | None = Field(default=None)
    is_archived: bool | None = Field(default=None, alias="isArchived")
    is_default_form: bool | None = Field(default=None, alias="isDefaultForm")
    form_definition: Any | None = Field(default=None, alias="formDefinition")
    interview_id: str | None = Field(default=None, alias="interviewId")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class CandidatesListResultMeta(BaseModel):
    """Metadata for candidates.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class ApplicationsListResultMeta(BaseModel):
    """Metadata for applications.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class JobsListResultMeta(BaseModel):
    """Metadata for jobs.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class DepartmentsListResultMeta(BaseModel):
    """Metadata for departments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class LocationsListResultMeta(BaseModel):
    """Metadata for locations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class JobPostingsListResultMeta(BaseModel):
    """Metadata for job_postings.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class SourcesListResultMeta(BaseModel):
    """Metadata for sources.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class ArchiveReasonsListResultMeta(BaseModel):
    """Metadata for archive_reasons.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class CandidateTagsListResultMeta(BaseModel):
    """Metadata for candidate_tags.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class CustomFieldsListResultMeta(BaseModel):
    """Metadata for custom_fields.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

class FeedbackFormDefinitionsListResultMeta(BaseModel):
    """Metadata for feedback_form_definitions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    has_more: bool | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class AshbyCheckResult(BaseModel):
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


class AshbyExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class AshbyExecuteResultWithMeta(AshbyExecuteResult[T], Generic[T, S]):
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

    id: str | None = None
    """Unique identifier for the application"""
    status: str | None = None
    """Current application status (e.g. active, archived, hired)"""
    archive_reason: str | None = None
    """Reason the application was archived, if applicable"""
    created_at: str | None = None
    """Timestamp when the application was created, in ISO 8601 format"""
    updated_at: str | None = None
    """Timestamp when the application was last updated, in ISO 8601 format"""


class CandidatesSearchData(BaseModel):
    """Search result data for candidates entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the candidate"""
    name: str | None = None
    """Full name of the candidate"""
    company: str | None = None
    """Candidate's current company"""
    position: str | None = None
    """Candidate's current position or title"""
    school: str | None = None
    """School associated with the candidate's education"""


class JobPostingsSearchData(BaseModel):
    """Search result data for job_postings entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the job posting"""
    title: str | None = None
    """Title of the job posting"""
    is_listed: bool | None = None
    """Whether the job posting is currently published/listed"""
    job_id: str | None = None
    """Identifier of the job this posting belongs to"""
    location_name: str | None = None
    """Name of the location associated with the posting"""


class JobsSearchData(BaseModel):
    """Search result data for jobs entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the job"""
    title: str | None = None
    """Title of the job"""
    status: str | None = None
    """Current status of the job (e.g. open, closed, draft)"""
    department_id: str | None = None
    """Identifier of the department the job belongs to"""
    location_id: str | None = None
    """Identifier of the primary location of the job"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the user"""
    first_name: str | None = None
    """First name of the user"""
    last_name: str | None = None
    """Last name of the user"""
    email: str | None = None
    """Primary email address of the user"""


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

JobPostingsSearchResult = AirbyteSearchResult[JobPostingsSearchData]
"""Search result type for job_postings entity."""

JobsSearchResult = AirbyteSearchResult[JobsSearchData]
"""Search result type for jobs entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

CandidatesListResult = AshbyExecuteResultWithMeta[list[Candidate], CandidatesListResultMeta]
"""Result type for candidates.list operation with data and metadata."""

ApplicationsListResult = AshbyExecuteResultWithMeta[list[Application], ApplicationsListResultMeta]
"""Result type for applications.list operation with data and metadata."""

JobsListResult = AshbyExecuteResultWithMeta[list[Job], JobsListResultMeta]
"""Result type for jobs.list operation with data and metadata."""

DepartmentsListResult = AshbyExecuteResultWithMeta[list[Department], DepartmentsListResultMeta]
"""Result type for departments.list operation with data and metadata."""

LocationsListResult = AshbyExecuteResultWithMeta[list[Location], LocationsListResultMeta]
"""Result type for locations.list operation with data and metadata."""

UsersListResult = AshbyExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

JobPostingsListResult = AshbyExecuteResultWithMeta[list[JobPosting], JobPostingsListResultMeta]
"""Result type for job_postings.list operation with data and metadata."""

SourcesListResult = AshbyExecuteResultWithMeta[list[Source], SourcesListResultMeta]
"""Result type for sources.list operation with data and metadata."""

ArchiveReasonsListResult = AshbyExecuteResultWithMeta[list[ArchiveReason], ArchiveReasonsListResultMeta]
"""Result type for archive_reasons.list operation with data and metadata."""

CandidateTagsListResult = AshbyExecuteResultWithMeta[list[CandidateTag], CandidateTagsListResultMeta]
"""Result type for candidate_tags.list operation with data and metadata."""

CustomFieldsListResult = AshbyExecuteResultWithMeta[list[CustomField], CustomFieldsListResultMeta]
"""Result type for custom_fields.list operation with data and metadata."""

FeedbackFormDefinitionsListResult = AshbyExecuteResultWithMeta[list[FeedbackFormDefinition], FeedbackFormDefinitionsListResultMeta]
"""Result type for feedback_form_definitions.list operation with data and metadata."""

