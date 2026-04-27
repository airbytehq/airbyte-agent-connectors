"""
Pydantic models for sentry connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class SentryAuthConfig(BaseModel):
    """Authentication Token"""

    model_config = ConfigDict(extra="forbid")

    auth_token: str
    """Sentry authentication token. Log into Sentry and create one at Settings > Account > API > Auth Tokens."""

# Replication configuration

class SentryReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Sentry."""

    model_config = ConfigDict(extra="forbid")

    organization: str
    """The slug of the organization to replicate data from."""
    project: str
    """The slug of the project to replicate data from."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class ProjectOrganization(BaseModel):
    """Organization this project belongs to."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)
    slug: str | None | None = Field(default=None)

class ProjectAvatar(BaseModel):
    """Project avatar information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_type: str | None | None = Field(default=None, alias="avatarType")
    avatar_uuid: str | None | None = Field(default=None, alias="avatarUuid")
    avatar_url: str | None | None = Field(default=None, alias="avatarUrl")

class Project(BaseModel):
    """A Sentry project (summary view from list endpoint)."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    slug: str | None = Field(default=None)
    status: str | None = Field(default=None)
    platform: str | None = Field(default=None)
    date_created: str | None = Field(default=None, alias="dateCreated")
    is_bookmarked: bool | None = Field(default=None, alias="isBookmarked")
    is_member: bool | None = Field(default=None, alias="isMember")
    has_access: bool | None = Field(default=None, alias="hasAccess")
    is_public: bool | None = Field(default=None, alias="isPublic")
    is_internal: bool | None = Field(default=None, alias="isInternal")
    color: str | None = Field(default=None)
    features: list[str | None] | None = Field(default=None)
    first_event: str | None = Field(default=None, alias="firstEvent")
    first_transaction_event: bool | None = Field(default=None, alias="firstTransactionEvent")
    access: list[str | None] | None = Field(default=None)
    has_minified_stack_trace: bool | None = Field(default=None, alias="hasMinifiedStackTrace")
    has_monitors: bool | None = Field(default=None, alias="hasMonitors")
    has_profiles: bool | None = Field(default=None, alias="hasProfiles")
    has_replays: bool | None = Field(default=None, alias="hasReplays")
    has_feedbacks: bool | None = Field(default=None, alias="hasFeedbacks")
    has_flags: bool | None = Field(default=None, alias="hasFlags")
    has_new_feedbacks: bool | None = Field(default=None, alias="hasNewFeedbacks")
    has_sessions: bool | None = Field(default=None, alias="hasSessions")
    has_insights_http: bool | None = Field(default=None, alias="hasInsightsHttp")
    has_insights_db: bool | None = Field(default=None, alias="hasInsightsDb")
    has_insights_assets: bool | None = Field(default=None, alias="hasInsightsAssets")
    has_insights_app_start: bool | None = Field(default=None, alias="hasInsightsAppStart")
    has_insights_screen_load: bool | None = Field(default=None, alias="hasInsightsScreenLoad")
    has_insights_vitals: bool | None = Field(default=None, alias="hasInsightsVitals")
    has_insights_caches: bool | None = Field(default=None, alias="hasInsightsCaches")
    has_insights_queues: bool | None = Field(default=None, alias="hasInsightsQueues")
    has_insights_agent_monitoring: bool | None = Field(default=None, alias="hasInsightsAgentMonitoring")
    has_insights_mcp: bool | None = Field(default=None, alias="hasInsightsMCP")
    has_logs: bool | None = Field(default=None, alias="hasLogs")
    has_trace_metrics: bool | None = Field(default=None, alias="hasTraceMetrics")
    avatar: ProjectAvatar | None = Field(default=None)
    organization: ProjectOrganization | None = Field(default=None)

class ProjectDetailOrganization(BaseModel):
    """Organization this project belongs to."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)
    slug: str | None | None = Field(default=None)

class ProjectDetailAvatar(BaseModel):
    """Project avatar information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_type: str | None | None = Field(default=None, alias="avatarType")
    avatar_uuid: str | None | None = Field(default=None, alias="avatarUuid")
    avatar_url: str | None | None = Field(default=None, alias="avatarUrl")

class ProjectDetailTeamsItem(BaseModel):
    """Nested schema for ProjectDetail.teams_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)
    slug: str | None | None = Field(default=None)

class ProjectDetailTeam(BaseModel):
    """Primary team for this project."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)
    slug: str | None | None = Field(default=None)

class ProjectDetail(BaseModel):
    """Detailed project information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    slug: str | None = Field(default=None)
    status: str | None = Field(default=None)
    platform: str | None = Field(default=None)
    date_created: str | None = Field(default=None, alias="dateCreated")
    is_bookmarked: bool | None = Field(default=None, alias="isBookmarked")
    is_member: bool | None = Field(default=None, alias="isMember")
    has_access: bool | None = Field(default=None, alias="hasAccess")
    is_public: bool | None = Field(default=None, alias="isPublic")
    is_internal: bool | None = Field(default=None, alias="isInternal")
    color: str | None = Field(default=None)
    features: list[str | None] | None = Field(default=None)
    first_event: str | None = Field(default=None, alias="firstEvent")
    first_transaction_event: bool | None = Field(default=None, alias="firstTransactionEvent")
    access: list[str | None] | None = Field(default=None)
    has_minified_stack_trace: bool | None = Field(default=None, alias="hasMinifiedStackTrace")
    has_monitors: bool | None = Field(default=None, alias="hasMonitors")
    has_profiles: bool | None = Field(default=None, alias="hasProfiles")
    has_replays: bool | None = Field(default=None, alias="hasReplays")
    has_feedbacks: bool | None = Field(default=None, alias="hasFeedbacks")
    has_flags: bool | None = Field(default=None, alias="hasFlags")
    has_new_feedbacks: bool | None = Field(default=None, alias="hasNewFeedbacks")
    has_sessions: bool | None = Field(default=None, alias="hasSessions")
    has_insights_http: bool | None = Field(default=None, alias="hasInsightsHttp")
    has_insights_db: bool | None = Field(default=None, alias="hasInsightsDb")
    has_insights_assets: bool | None = Field(default=None, alias="hasInsightsAssets")
    has_insights_app_start: bool | None = Field(default=None, alias="hasInsightsAppStart")
    has_insights_screen_load: bool | None = Field(default=None, alias="hasInsightsScreenLoad")
    has_insights_vitals: bool | None = Field(default=None, alias="hasInsightsVitals")
    has_insights_caches: bool | None = Field(default=None, alias="hasInsightsCaches")
    has_insights_queues: bool | None = Field(default=None, alias="hasInsightsQueues")
    has_insights_agent_monitoring: bool | None = Field(default=None, alias="hasInsightsAgentMonitoring")
    has_insights_mcp: bool | None = Field(default=None, alias="hasInsightsMCP")
    has_logs: bool | None = Field(default=None, alias="hasLogs")
    has_trace_metrics: bool | None = Field(default=None, alias="hasTraceMetrics")
    team: ProjectDetailTeam | None = Field(default=None)
    teams: list[ProjectDetailTeamsItem | None] | None = Field(default=None)
    avatar: ProjectDetailAvatar | None = Field(default=None)
    organization: ProjectDetailOrganization | None = Field(default=None)
    latest_release: dict[str, Any] | None = Field(default=None, alias="latestRelease")
    options: dict[str, Any] | None = Field(default=None)
    digests_min_delay: int | None = Field(default=None, alias="digestsMinDelay")
    digests_max_delay: int | None = Field(default=None, alias="digestsMaxDelay")
    resolve_age: int | None = Field(default=None, alias="resolveAge")
    data_scrubber: bool | None = Field(default=None, alias="dataScrubber")
    safe_fields: list[str | None] | None = Field(default=None, alias="safeFields")
    sensitive_fields: list[str | None] | None = Field(default=None, alias="sensitiveFields")
    verify_ssl: bool | None = Field(default=None, alias="verifySSL")
    scrub_ip_addresses: bool | None = Field(default=None, alias="scrubIPAddresses")
    scrape_java_script: bool | None = Field(default=None, alias="scrapeJavaScript")
    allowed_domains: list[str | None] | None = Field(default=None, alias="allowedDomains")
    processing_issues: int | None = Field(default=None, alias="processingIssues")
    security_token: str | None = Field(default=None, alias="securityToken")
    subject_prefix: str | None = Field(default=None, alias="subjectPrefix")
    data_scrubber_defaults: bool | None = Field(default=None, alias="dataScrubberDefaults")
    store_crash_reports: Any | None = Field(default=None, alias="storeCrashReports")
    subject_template: str | None = Field(default=None, alias="subjectTemplate")
    security_token_header: str | None = Field(default=None, alias="securityTokenHeader")
    grouping_config: str | None = Field(default=None, alias="groupingConfig")
    grouping_enhancements: str | None = Field(default=None, alias="groupingEnhancements")
    derived_grouping_enhancements: str | None = Field(default=None, alias="derivedGroupingEnhancements")
    secondary_grouping_expiry: int | None = Field(default=None, alias="secondaryGroupingExpiry")
    secondary_grouping_config: str | None = Field(default=None, alias="secondaryGroupingConfig")
    fingerprinting_rules: str | None = Field(default=None, alias="fingerprintingRules")
    plugins: list[Any] | None = Field(default=None)
    platforms: list[str | None] | None = Field(default=None)
    default_environment: str | None = Field(default=None, alias="defaultEnvironment")
    relay_pii_config: str | None = Field(default=None, alias="relayPiiConfig")
    builtin_symbol_sources: list[str | None] | None = Field(default=None, alias="builtinSymbolSources")
    dynamic_sampling_biases: list[Any] | None = Field(default=None, alias="dynamicSamplingBiases")
    symbol_sources: str | None = Field(default=None, alias="symbolSources")
    is_dynamically_sampled: bool | None = Field(default=None, alias="isDynamicallySampled")
    autofix_automation_tuning: str | None = Field(default=None, alias="autofixAutomationTuning")
    seer_scanner_automation: bool | None = Field(default=None, alias="seerScannerAutomation")
    highlight_tags: list[Any] | None = Field(default=None, alias="highlightTags")
    highlight_context: dict[str, Any] | None = Field(default=None, alias="highlightContext")
    highlight_preset: dict[str, Any] | None = Field(default=None, alias="highlightPreset")
    debug_files_role: str | None = Field(default=None, alias="debugFilesRole")

class IssueProject(BaseModel):
    """Project this issue belongs to."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)
    slug: str | None | None = Field(default=None)

class IssueMetadata(BaseModel):
    """Issue metadata."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None | None = Field(default=None)
    type_: str | None | None = Field(default=None, alias="type")
    value: str | None | None = Field(default=None)
    filename: str | None | None = Field(default=None)

class Issue(BaseModel):
    """A Sentry issue (group of similar events)."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    title: str | None = Field(default=None)
    short_id: str | None = Field(default=None, alias="shortId")
    culprit: str | None = Field(default=None)
    level: str | None = Field(default=None)
    status: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    count: str | None = Field(default=None)
    user_count: int | None = Field(default=None, alias="userCount")
    first_seen: str | None = Field(default=None, alias="firstSeen")
    last_seen: str | None = Field(default=None, alias="lastSeen")
    has_seen: bool | None = Field(default=None, alias="hasSeen")
    is_bookmarked: bool | None = Field(default=None, alias="isBookmarked")
    is_public: bool | None = Field(default=None, alias="isPublic")
    is_subscribed: bool | None = Field(default=None, alias="isSubscribed")
    logger: str | None = Field(default=None)
    permalink: str | None = Field(default=None)
    platform: str | None = Field(default=None)
    share_id: str | None = Field(default=None, alias="shareId")
    num_comments: int | None = Field(default=None, alias="numComments")
    issue_type: str | None = Field(default=None, alias="issueType")
    issue_category: str | None = Field(default=None, alias="issueCategory")
    is_unhandled: bool | None = Field(default=None, alias="isUnhandled")
    substatus: str | None = Field(default=None)
    metadata: IssueMetadata | None = Field(default=None)
    project: IssueProject | None = Field(default=None)
    stats: dict[str, Any] | None = Field(default=None)
    status_details: dict[str, Any] | None = Field(default=None, alias="statusDetails")
    assigned_to: dict[str, Any] | None = Field(default=None, alias="assignedTo")
    annotations: list[str | None] | None = Field(default=None)
    subscription_details: dict[str, Any] | None = Field(default=None, alias="subscriptionDetails")

class EventMetadata(BaseModel):
    """Event metadata."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    title: str | None | None = Field(default=None)

class EventUser(BaseModel):
    """User associated with the event."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    email: str | None | None = Field(default=None)
    username: str | None | None = Field(default=None)
    name: str | None | None = Field(default=None)
    ip_address: str | None | None = Field(default=None)

class EventTagsItem(BaseModel):
    """Nested schema for Event.tags_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    key: str | None | None = Field(default=None)
    value: str | None | None = Field(default=None)

class EventGroupingconfig(BaseModel):
    """Grouping configuration."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None | None = Field(default=None)
    enhancements: str | None | None = Field(default=None)

class Event(BaseModel):
    """A Sentry event (individual error occurrence)."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    event_id: str | None = Field(default=None, alias="eventID")
    group_id: str | None = Field(default=None, alias="groupID")
    title: str | None = Field(default=None)
    message: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    platform: str | None = Field(default=None)
    date_created: str | None = Field(default=None, alias="dateCreated")
    date_received: str | None = Field(default=None, alias="dateReceived")
    culprit: str | None = Field(default=None)
    location: str | None = Field(default=None)
    crash_file: str | None = Field(default=None, alias="crashFile")
    project_id: str | None = Field(default=None, alias="projectID")
    sdk: str | None = Field(default=None)
    dist: str | None = Field(default=None)
    size: int | None = Field(default=None)
    event_type: str | None = Field(default=None, alias="event.type")
    tags: list[EventTagsItem | None] | None = Field(default=None)
    user: EventUser | None = Field(default=None)
    metadata: EventMetadata | None = Field(default=None)
    context: dict[str, Any] | None = Field(default=None)
    contexts: dict[str, Any] | None = Field(default=None)
    entries: list[dict[str, Any] | None] | None = Field(default=None)
    errors: list[str | None] | None = Field(default=None)
    fingerprints: list[str | None] | None = Field(default=None)
    packages: dict[str, Any] | None = Field(default=None)
    grouping_config: EventGroupingconfig | None = Field(default=None, alias="groupingConfig")
    meta: dict[str, Any] | None = Field(default=None, alias="_meta")

class ReleaseAuthorsItem(BaseModel):
    """Nested schema for Release.authors_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None | None = Field(default=None)
    email: str | None | None = Field(default=None)

class ReleaseVersioninfoVersion(BaseModel):
    """Nested schema for ReleaseVersioninfo.version"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    raw: str | None | None = Field(default=None)
    major: int | None | None = Field(default=None)
    minor: int | None | None = Field(default=None)
    patch: int | None | None = Field(default=None)
    pre: str | None | None = Field(default=None)
    build_code: str | None | None = Field(default=None, alias="buildCode")
    components: int | None | None = Field(default=None)

class ReleaseVersioninfo(BaseModel):
    """Parsed version information."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    version: ReleaseVersioninfoVersion | None | None = Field(default=None)
    description: str | None | None = Field(default=None)
    package: str | None | None = Field(default=None)
    build_hash: str | None | None = Field(default=None, alias="buildHash")

class ReleaseProjectsItem(BaseModel):
    """Nested schema for Release.projects_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None | None = Field(default=None)
    name: str | None | None = Field(default=None)
    slug: str | None | None = Field(default=None)
    platform: str | None | None = Field(default=None)
    new_groups: int | None | None = Field(default=None, alias="newGroups")
    has_health_data: bool | None | None = Field(default=None, alias="hasHealthData")

class Release(BaseModel):
    """A Sentry release."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None)
    version: str | None = Field(default=None)
    short_version: str | None = Field(default=None, alias="shortVersion")
    ref: str | None = Field(default=None)
    url: str | None = Field(default=None)
    status: str | None = Field(default=None)
    date_created: str | None = Field(default=None, alias="dateCreated")
    date_released: str | None = Field(default=None, alias="dateReleased")
    owner: str | None = Field(default=None)
    new_groups: int | None = Field(default=None, alias="newGroups")
    commit_count: int | None = Field(default=None, alias="commitCount")
    deploy_count: int | None = Field(default=None, alias="deployCount")
    first_event: str | None = Field(default=None, alias="firstEvent")
    last_event: str | None = Field(default=None, alias="lastEvent")
    last_commit: dict[str, Any] | None = Field(default=None, alias="lastCommit")
    last_deploy: dict[str, Any] | None = Field(default=None, alias="lastDeploy")
    data: dict[str, Any] | None = Field(default=None)
    user_agent: str | None = Field(default=None, alias="userAgent")
    authors: list[ReleaseAuthorsItem | None] | None = Field(default=None)
    projects: list[ReleaseProjectsItem | None] | None = Field(default=None)
    version_info: ReleaseVersioninfo | None = Field(default=None, alias="versionInfo")
    current_project_meta: dict[str, Any] | None = Field(default=None, alias="currentProjectMeta")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class ProjectsListResultMeta(BaseModel):
    """Metadata for projects.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class IssuesListResultMeta(BaseModel):
    """Metadata for issues.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class EventsListResultMeta(BaseModel):
    """Metadata for events.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

class ReleasesListResultMeta(BaseModel):
    """Metadata for releases.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next: str | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class SentryCheckResult(BaseModel):
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


class SentryExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class SentryExecuteResultWithMeta(SentryExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class EventsSearchData(BaseModel):
    """Search result data for events entity."""
    model_config = ConfigDict(extra="allow")

    meta: dict[str, Any] | None = None
    """Meta information for data scrubbing."""
    context: dict[str, Any] | None = None
    """Additional context data."""
    contexts: dict[str, Any] | None = None
    """Structured context information."""
    crash_file: str | None = None
    """Crash file reference."""
    culprit: str | None = None
    """The culprit (source) of the event."""
    date_created: str | None = None
    """When the event was created."""
    date_received: str | None = None
    """When the event was received by Sentry."""
    dist: str | None = None
    """Distribution information."""
    entries: list[Any] | None = None
    """Event entries (exception, breadcrumbs, request, etc.)."""
    errors: list[Any] | None = None
    """Processing errors."""
    event_type: str | None = None
    """The type of the event."""
    event_id: str | None = None
    """Event ID as reported by the client."""
    fingerprints: list[Any] | None = None
    """Fingerprints used for grouping."""
    group_id: str | None = None
    """ID of the issue group this event belongs to."""
    grouping_config: dict[str, Any] | None = None
    """Grouping configuration."""
    id: str | None = None
    """Unique event identifier."""
    location: str | None = None
    """Location in source code."""
    message: str | None = None
    """Event message."""
    metadata: dict[str, Any] | None = None
    """Event metadata."""
    occurrence: str | None = None
    """Occurrence information for the event."""
    packages: dict[str, Any] | None = None
    """Package information."""
    platform: str | None = None
    """Platform the event was generated on."""
    project_id: str | None = None
    """Project ID this event belongs to."""
    sdk: str | None = None
    """SDK information."""
    size: int | None = None
    """Event payload size in bytes."""
    tags: list[Any] | None = None
    """Tags associated with the event."""
    title: str | None = None
    """Event title."""
    type_: str | None = None
    """Event type."""
    user: dict[str, Any] | None = None
    """User associated with the event."""


class IssuesSearchData(BaseModel):
    """Search result data for issues entity."""
    model_config = ConfigDict(extra="allow")

    annotations: list[Any] | None = None
    """Annotations on the issue."""
    assigned_to: dict[str, Any] | None = None
    """User or team assigned to this issue."""
    count: str | None = None
    """Number of events for this issue."""
    culprit: str | None = None
    """The culprit (source) of the issue."""
    first_seen: str | None = None
    """When the issue was first seen."""
    has_seen: bool | None = None
    """Whether the authenticated user has seen the issue."""
    id: str | None = None
    """Unique issue identifier."""
    is_bookmarked: bool | None = None
    """Whether the issue is bookmarked."""
    is_public: bool | None = None
    """Whether the issue is public."""
    is_subscribed: bool | None = None
    """Whether the user is subscribed to the issue."""
    is_unhandled: bool | None = None
    """Whether the issue is from an unhandled error."""
    issue_category: str | None = None
    """The category classification of the issue."""
    issue_type: str | None = None
    """The type classification of the issue."""
    last_seen: str | None = None
    """When the issue was last seen."""
    level: str | None = None
    """Issue severity level."""
    logger: str | None = None
    """Logger that generated the issue."""
    metadata: dict[str, Any] | None = None
    """Issue metadata."""
    num_comments: int | None = None
    """Number of comments on the issue."""
    permalink: str | None = None
    """Permalink to the issue in the Sentry UI."""
    platform: str | None = None
    """Platform for this issue."""
    project: dict[str, Any] | None = None
    """Project this issue belongs to."""
    share_id: str | None = None
    """Share ID if the issue is shared."""
    short_id: str | None = None
    """Short human-readable identifier."""
    stats: dict[str, Any] | None = None
    """Issue event statistics."""
    status: str | None = None
    """Issue status (resolved, unresolved, ignored)."""
    status_details: dict[str, Any] | None = None
    """Status detail information."""
    subscription_details: dict[str, Any] | None = None
    """Subscription details."""
    substatus: str | None = None
    """Issue substatus."""
    title: str | None = None
    """Issue title."""
    type_: str | None = None
    """Issue type."""
    user_count: int | None = None
    """Number of users affected."""


class ProjectsSearchData(BaseModel):
    """Search result data for projects entity."""
    model_config = ConfigDict(extra="allow")

    access: list[Any] | None = None
    """List of access permissions for the authenticated user."""
    avatar: dict[str, Any] | None = None
    """Project avatar information."""
    color: str | None = None
    """Project color code."""
    date_created: str | None = None
    """Date the project was created."""
    features: list[Any] | None = None
    """List of enabled features."""
    first_event: str | None = None
    """Timestamp of the first event."""
    first_transaction_event: bool | None = None
    """Whether a transaction event has been received."""
    has_access: bool | None = None
    """Whether the user has access to this project."""
    has_custom_metrics: bool | None = None
    """Whether the project has custom metrics."""
    has_feedbacks: bool | None = None
    """Whether the project has user feedback."""
    has_minified_stack_trace: bool | None = None
    """Whether the project has minified stack traces."""
    has_monitors: bool | None = None
    """Whether the project has cron monitors."""
    has_new_feedbacks: bool | None = None
    """Whether the project has new user feedback."""
    has_profiles: bool | None = None
    """Whether the project has profiling data."""
    has_replays: bool | None = None
    """Whether the project has session replays."""
    has_sessions: bool | None = None
    """Whether the project has session data."""
    id: str | None = None
    """Unique project identifier."""
    is_bookmarked: bool | None = None
    """Whether the project is bookmarked."""
    is_internal: bool | None = None
    """Whether the project is internal."""
    is_member: bool | None = None
    """Whether the authenticated user is a member."""
    is_public: bool | None = None
    """Whether the project is public."""
    name: str | None = None
    """Human-readable project name."""
    organization: dict[str, Any] | None = None
    """Organization this project belongs to."""
    platform: str | None = None
    """The platform for this project."""
    slug: str | None = None
    """URL-friendly project identifier."""
    status: str | None = None
    """Project status."""


class ReleasesSearchData(BaseModel):
    """Search result data for releases entity."""
    model_config = ConfigDict(extra="allow")

    authors: list[Any] | None = None
    """Authors of commits in this release."""
    commit_count: int | None = None
    """Number of commits in this release."""
    current_project_meta: dict[str, Any] | None = None
    """Metadata for the current project context."""
    data: dict[str, Any] | None = None
    """Additional release data."""
    date_created: str | None = None
    """When the release was created."""
    date_released: str | None = None
    """When the release was deployed."""
    deploy_count: int | None = None
    """Number of deploys for this release."""
    first_event: str | None = None
    """Timestamp of the first event in this release."""
    id: int | None = None
    """Unique release identifier."""
    last_commit: dict[str, Any] | None = None
    """Last commit in this release."""
    last_deploy: dict[str, Any] | None = None
    """Last deploy of this release."""
    last_event: str | None = None
    """Timestamp of the last event in this release."""
    new_groups: int | None = None
    """Number of new issue groups in this release."""
    owner: str | None = None
    """Owner of the release."""
    projects: list[Any] | None = None
    """Projects associated with this release."""
    ref: str | None = None
    """Git reference (commit SHA, tag, etc.)."""
    short_version: str | None = None
    """Short version string."""
    status: str | None = None
    """Release status."""
    url: str | None = None
    """URL associated with the release."""
    user_agent: str | None = None
    """User agent that created the release."""
    version: str | None = None
    """Release version string."""
    version_info: dict[str, Any] | None = None
    """Parsed version information."""


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

EventsSearchResult = AirbyteSearchResult[EventsSearchData]
"""Search result type for events entity."""

IssuesSearchResult = AirbyteSearchResult[IssuesSearchData]
"""Search result type for issues entity."""

ProjectsSearchResult = AirbyteSearchResult[ProjectsSearchData]
"""Search result type for projects entity."""

ReleasesSearchResult = AirbyteSearchResult[ReleasesSearchData]
"""Search result type for releases entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

ProjectsListResult = SentryExecuteResultWithMeta[list[Project], ProjectsListResultMeta]
"""Result type for projects.list operation with data and metadata."""

IssuesListResult = SentryExecuteResultWithMeta[list[Issue], IssuesListResultMeta]
"""Result type for issues.list operation with data and metadata."""

EventsListResult = SentryExecuteResultWithMeta[list[Event], EventsListResultMeta]
"""Result type for events.list operation with data and metadata."""

ReleasesListResult = SentryExecuteResultWithMeta[list[Release], ReleasesListResultMeta]
"""Result type for releases.list operation with data and metadata."""

