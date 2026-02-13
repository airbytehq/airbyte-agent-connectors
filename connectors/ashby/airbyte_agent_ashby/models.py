"""
Pydantic models for ashby connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

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

class CandidateSociallinksItem(BaseModel):
    """Nested schema for Candidate.socialLinks_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    type: Union[str | None, Any] = Field(default=None)
    url: Union[str | None, Any] = Field(default=None)

class CandidateEmailaddressesItem(BaseModel):
    """Nested schema for Candidate.emailAddresses_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    is_primary: Union[bool | None, Any] = Field(default=None, alias="isPrimary")

class CandidateTagsItem(BaseModel):
    """Nested schema for Candidate.tags_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    is_archived: Union[bool | None, Any] = Field(default=None, alias="isArchived")

class CandidatePhonenumbersItem(BaseModel):
    """Nested schema for Candidate.phoneNumbers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    is_primary: Union[bool | None, Any] = Field(default=None, alias="isPrimary")

class Candidate(BaseModel):
    """Candidate object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str | None, Any] = Field(default=None, alias="updatedAt")
    name: Union[str | None, Any] = Field(default=None)
    email_addresses: Union[list[CandidateEmailaddressesItem] | None, Any] = Field(default=None, alias="emailAddresses")
    phone_numbers: Union[list[CandidatePhonenumbersItem] | None, Any] = Field(default=None, alias="phoneNumbers")
    social_links: Union[list[CandidateSociallinksItem] | None, Any] = Field(default=None, alias="socialLinks")
    tags: Union[list[CandidateTagsItem] | None, Any] = Field(default=None)
    application_ids: Union[list[str | None] | None, Any] = Field(default=None, alias="applicationIds")
    file_handles: Union[list[Any] | None, Any] = Field(default=None, alias="fileHandles")
    custom_fields: Union[list[Any] | None, Any] = Field(default=None, alias="customFields")
    profile_url: Union[str | None, Any] = Field(default=None, alias="profileUrl")
    source: Union[Any, Any] = Field(default=None)
    credited_to_user: Union[Any, Any] = Field(default=None, alias="creditedToUser")
    timezone: Union[str | None, Any] = Field(default=None)

class ApplicationHiringteamItem(BaseModel):
    """Nested schema for Application.hiringTeam_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_id: Union[str | None, Any] = Field(default=None, alias="userId")
    first_name: Union[str | None, Any] = Field(default=None, alias="firstName")
    last_name: Union[str | None, Any] = Field(default=None, alias="lastName")
    email: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)

class Application(BaseModel):
    """Application object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str | None, Any] = Field(default=None, alias="updatedAt")
    archived_at: Union[str | None, Any] = Field(default=None, alias="archivedAt")
    candidate: Union[Any, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    custom_fields: Union[list[Any] | None, Any] = Field(default=None, alias="customFields")
    current_interview_stage: Union[Any, Any] = Field(default=None, alias="currentInterviewStage")
    source: Union[Any, Any] = Field(default=None)
    credited_to_user: Union[Any, Any] = Field(default=None, alias="creditedToUser")
    archive_reason: Union[Any, Any] = Field(default=None, alias="archiveReason")
    job: Union[Any, Any] = Field(default=None)
    hiring_team: Union[list[ApplicationHiringteamItem] | None, Any] = Field(default=None, alias="hiringTeam")
    applied_via_job_posting_id: Union[str | None, Any] = Field(default=None, alias="appliedViaJobPostingId")
    submitter_client_ip: Union[str | None, Any] = Field(default=None, alias="submitterClientIp")
    submitter_user_agent: Union[str | None, Any] = Field(default=None, alias="submitterUserAgent")

class JobCustomfieldsItem(BaseModel):
    """Nested schema for Job.customFields_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    is_private: Union[bool | None, Any] = Field(default=None, alias="isPrivate")
    title: Union[str | None, Any] = Field(default=None)
    value: Union[str | None, Any] = Field(default=None)
    value_label: Union[str | None, Any] = Field(default=None, alias="valueLabel")

class JobHiringteamItem(BaseModel):
    """Nested schema for Job.hiringTeam_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_id: Union[str | None, Any] = Field(default=None, alias="userId")
    first_name: Union[str | None, Any] = Field(default=None, alias="firstName")
    last_name: Union[str | None, Any] = Field(default=None, alias="lastName")
    email: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)

class Job(BaseModel):
    """Job object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    confidential: Union[bool | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    employment_type: Union[str | None, Any] = Field(default=None, alias="employmentType")
    location_id: Union[str | None, Any] = Field(default=None, alias="locationId")
    department_id: Union[str | None, Any] = Field(default=None, alias="departmentId")
    default_interview_plan_id: Union[str | None, Any] = Field(default=None, alias="defaultInterviewPlanId")
    interview_plan_ids: Union[list[str | None] | None, Any] = Field(default=None, alias="interviewPlanIds")
    job_posting_ids: Union[list[str | None] | None, Any] = Field(default=None, alias="jobPostingIds")
    custom_fields: Union[list[JobCustomfieldsItem] | None, Any] = Field(default=None, alias="customFields")
    hiring_team: Union[list[JobHiringteamItem] | None, Any] = Field(default=None, alias="hiringTeam")
    custom_requisition_id: Union[str | None, Any] = Field(default=None, alias="customRequisitionId")
    brand_id: Union[str | None, Any] = Field(default=None, alias="brandId")
    author: Union[Any, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str | None, Any] = Field(default=None, alias="updatedAt")
    opened_at: Union[str | None, Any] = Field(default=None, alias="openedAt")
    closed_at: Union[str | None, Any] = Field(default=None, alias="closedAt")

class Department(BaseModel):
    """Department object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    external_name: Union[str | None, Any] = Field(default=None, alias="externalName")
    is_archived: Union[bool | None, Any] = Field(default=None, alias="isArchived")
    parent_id: Union[str | None, Any] = Field(default=None, alias="parentId")
    created_at: Union[str | None, Any] = Field(default=None, alias="createdAt")
    updated_at: Union[str | None, Any] = Field(default=None, alias="updatedAt")
    extra_data: Union[Any, Any] = Field(default=None, alias="extraData")

class Location(BaseModel):
    """Location object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    external_name: Union[str | None, Any] = Field(default=None, alias="externalName")
    is_archived: Union[bool | None, Any] = Field(default=None, alias="isArchived")
    address: Union[Any, Any] = Field(default=None)
    is_remote: Union[bool | None, Any] = Field(default=None, alias="isRemote")
    workplace_type: Union[str | None, Any] = Field(default=None, alias="workplaceType")
    parent_location_id: Union[str | None, Any] = Field(default=None, alias="parentLocationId")
    type: Union[str | None, Any] = Field(default=None)
    extra_data: Union[Any, Any] = Field(default=None, alias="extraData")

class User(BaseModel):
    """User object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    first_name: Union[str | None, Any] = Field(default=None, alias="firstName")
    last_name: Union[str | None, Any] = Field(default=None, alias="lastName")
    email: Union[str | None, Any] = Field(default=None)
    global_role: Union[str | None, Any] = Field(default=None, alias="globalRole")
    is_enabled: Union[bool | None, Any] = Field(default=None, alias="isEnabled")
    updated_at: Union[str | None, Any] = Field(default=None, alias="updatedAt")

class JobPosting(BaseModel):
    """Job posting object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    job_id: Union[str | None, Any] = Field(default=None, alias="jobId")
    department_name: Union[str | None, Any] = Field(default=None, alias="departmentName")
    team_name: Union[str | None, Any] = Field(default=None, alias="teamName")
    location_name: Union[str | None, Any] = Field(default=None, alias="locationName")
    location_external_name: Union[str | None, Any] = Field(default=None, alias="locationExternalName")
    workplace_type: Union[str | None, Any] = Field(default=None, alias="workplaceType")
    employment_type: Union[str | None, Any] = Field(default=None, alias="employmentType")
    is_listed: Union[bool | None, Any] = Field(default=None, alias="isListed")
    published_date: Union[str | None, Any] = Field(default=None, alias="publishedDate")
    application_deadline: Union[str | None, Any] = Field(default=None, alias="applicationDeadline")
    external_link: Union[str | None, Any] = Field(default=None, alias="externalLink")
    apply_link: Union[str | None, Any] = Field(default=None, alias="applyLink")
    location_ids: Union[Any, Any] = Field(default=None, alias="locationIds")
    compensation_tier_summary: Union[str | None, Any] = Field(default=None, alias="compensationTierSummary")
    should_display_compensation_on_job_board: Union[bool | None, Any] = Field(default=None, alias="shouldDisplayCompensationOnJobBoard")
    updated_at: Union[str | None, Any] = Field(default=None, alias="updatedAt")

class Source(BaseModel):
    """Candidate source object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    is_archived: Union[bool | None, Any] = Field(default=None, alias="isArchived")
    source_type: Union[Any, Any] = Field(default=None, alias="sourceType")

class ArchiveReason(BaseModel):
    """Archive reason object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    text: Union[str | None, Any] = Field(default=None)
    reason_type: Union[str | None, Any] = Field(default=None, alias="reasonType")
    is_archived: Union[bool | None, Any] = Field(default=None, alias="isArchived")

class CandidateTag(BaseModel):
    """Candidate tag object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    is_archived: Union[bool | None, Any] = Field(default=None, alias="isArchived")

class CustomField(BaseModel):
    """Custom field definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    object_type: Union[str | None, Any] = Field(default=None, alias="objectType")
    is_archived: Union[bool | None, Any] = Field(default=None, alias="isArchived")
    is_private: Union[bool | None, Any] = Field(default=None, alias="isPrivate")
    field_type: Union[str | None, Any] = Field(default=None, alias="fieldType")

class FeedbackFormDefinition(BaseModel):
    """Feedback form definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    organization_id: Union[str | None, Any] = Field(default=None, alias="organizationId")
    title: Union[str | None, Any] = Field(default=None)
    is_archived: Union[bool | None, Any] = Field(default=None, alias="isArchived")
    is_default_form: Union[bool | None, Any] = Field(default=None, alias="isDefaultForm")
    form_definition: Union[Any, Any] = Field(default=None, alias="formDefinition")
    interview_id: Union[str | None, Any] = Field(default=None, alias="interviewId")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class CandidatesListResultMeta(BaseModel):
    """Metadata for candidates.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

class ApplicationsListResultMeta(BaseModel):
    """Metadata for applications.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

class JobsListResultMeta(BaseModel):
    """Metadata for jobs.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

class DepartmentsListResultMeta(BaseModel):
    """Metadata for departments.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

class LocationsListResultMeta(BaseModel):
    """Metadata for locations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

class JobPostingsListResultMeta(BaseModel):
    """Metadata for job_postings.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

class SourcesListResultMeta(BaseModel):
    """Metadata for sources.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

class ArchiveReasonsListResultMeta(BaseModel):
    """Metadata for archive_reasons.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

class CandidateTagsListResultMeta(BaseModel):
    """Metadata for candidate_tags.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

class CustomFieldsListResultMeta(BaseModel):
    """Metadata for custom_fields.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

class FeedbackFormDefinitionsListResultMeta(BaseModel):
    """Metadata for feedback_form_definitions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: Union[str | None, Any] = Field(default=None)
    has_more: Union[bool, Any] = Field(default=None)

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
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""



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

