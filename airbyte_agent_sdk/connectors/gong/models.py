"""
Pydantic models for gong connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any
from typing import Optional

# Authentication configuration - multiple options available

class GongOauth20AuthenticationAuthConfig(BaseModel):
    """OAuth 2.0 Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: Optional[str] = None
    """Your Gong OAuth2 Access Token."""
    refresh_token: str
    """Your Gong OAuth2 Refresh Token. Note: Gong uses single-use refresh tokens."""
    client_id: Optional[str] = None
    """Your Gong OAuth App Client ID."""
    client_secret: Optional[str] = None
    """Your Gong OAuth App Client Secret."""

class GongAccessKeyAuthenticationAuthConfig(BaseModel):
    """Access Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_key: str
    """Your Gong API Access Key"""
    access_key_secret: str
    """Your Gong API Access Key Secret"""

GongAuthConfig = GongOauth20AuthenticationAuthConfig | GongAccessKeyAuthenticationAuthConfig

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class PaginationRecords(BaseModel):
    """Pagination metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_records: int | None = Field(default=None, alias="totalRecords")
    current_page_size: int | None = Field(default=None, alias="currentPageSize")
    current_page_number: int | None = Field(default=None, alias="currentPageNumber")
    cursor: str | None = Field(default=None)

class UserSettings(BaseModel):
    """User settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    web_conferences_recorded: bool | None = Field(default=None, alias="webConferencesRecorded")
    prevent_web_conference_recording: bool | None = Field(default=None, alias="preventWebConferenceRecording")
    telephony_calls_imported: bool | None = Field(default=None, alias="telephonyCallsImported")
    emails_imported: bool | None = Field(default=None, alias="emailsImported")
    prevent_email_import: bool | None = Field(default=None, alias="preventEmailImport")
    non_recorded_meetings_imported: bool | None = Field(default=None, alias="nonRecordedMeetingsImported")
    gong_connect_enabled: bool | None = Field(default=None, alias="gongConnectEnabled")

class UserSpokenlanguagesItem(BaseModel):
    """Nested schema for User.spokenLanguages_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    language: str | None = Field(default=None)
    primary: bool | None = Field(default=None)

class User(BaseModel):
    """User object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    email_address: str | None = Field(default=None, alias="emailAddress")
    created: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    email_aliases: list[str] | None = Field(default=None, alias="emailAliases")
    trusted_email_address: str | None = Field(default=None, alias="trustedEmailAddress")
    first_name: str | None = Field(default=None, alias="firstName")
    last_name: str | None = Field(default=None, alias="lastName")
    title: str | None = Field(default=None)
    phone_number: str | None = Field(default=None, alias="phoneNumber")
    extension: str | None = Field(default=None)
    personal_meeting_urls: list[str] | None = Field(default=None, alias="personalMeetingUrls")
    settings: UserSettings | None = Field(default=None)
    manager_id: str | None = Field(default=None, alias="managerId")
    meeting_consent_page_url: str | None = Field(default=None, alias="meetingConsentPageUrl")
    spoken_languages: list[UserSpokenlanguagesItem] | None = Field(default=None, alias="spokenLanguages")

class UsersResponse(BaseModel):
    """Response containing list of users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    users: list[User] | None = Field(default=None)
    records: PaginationRecords | None = Field(default=None)
    request_id: str | None = Field(default=None, alias="requestId")

class UserResponse(BaseModel):
    """Response containing single user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user: User | None = Field(default=None)
    request_id: str | None = Field(default=None, alias="requestId")

class Call(BaseModel):
    """Call object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    url: str | None = Field(default=None)
    title: str | None = Field(default=None)
    scheduled: str | None = Field(default=None)
    started: str | None = Field(default=None)
    duration: int | None = Field(default=None)
    primary_user_id: str | None = Field(default=None, alias="primaryUserId")
    direction: str | None = Field(default=None)
    system: str | None = Field(default=None)
    scope: str | None = Field(default=None)
    media: str | None = Field(default=None)
    language: str | None = Field(default=None)
    workspace_id: str | None = Field(default=None, alias="workspaceId")
    sdr_disposition: str | None = Field(default=None, alias="sdrDisposition")
    client_unique_id: str | None = Field(default=None, alias="clientUniqueId")
    custom_data: str | None = Field(default=None, alias="customData")
    purpose: str | None = Field(default=None)
    meeting_url: str | None = Field(default=None, alias="meetingUrl")
    is_private: bool | None = Field(default=None, alias="isPrivate")
    calendar_event_id: str | None = Field(default=None, alias="calendarEventId")

class CallsResponse(BaseModel):
    """Response containing list of calls"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls: list[Call] | None = Field(default=None)
    records: PaginationRecords | None = Field(default=None)
    request_id: str | None = Field(default=None, alias="requestId")

class CallResponse(BaseModel):
    """Response containing single call"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    call: Call | None = Field(default=None)
    request_id: str | None = Field(default=None, alias="requestId")

class Workspace(BaseModel):
    """Workspace object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    workspace_id: str | None = Field(default=None, alias="workspaceId")
    name: str | None = Field(default=None)
    description: str | None = Field(default=None)

class WorkspacesResponse(BaseModel):
    """Response containing list of workspaces"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    workspaces: list[Workspace] | None = Field(default=None)
    request_id: str | None = Field(default=None, alias="requestId")

class CallTranscriptTranscriptItemSentencesItem(BaseModel):
    """Nested schema for CallTranscriptTranscriptItem.sentences_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: int | None = Field(default=None, description="Start time in seconds")
    """Start time in seconds"""
    end: int | None = Field(default=None, description="End time in seconds")
    """End time in seconds"""
    text: str | None = Field(default=None, description="Sentence text")
    """Sentence text"""

class CallTranscriptTranscriptItem(BaseModel):
    """Nested schema for CallTranscript.transcript_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    speaker_id: str | None = Field(default=None, alias="speakerId", description="Speaker identifier")
    """Speaker identifier"""
    topic: str | None | None = Field(default=None, description="Topic")
    """Topic"""
    sentences: list[CallTranscriptTranscriptItemSentencesItem] | None = Field(default=None)

class CallTranscript(BaseModel):
    """Call transcript object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    call_id: str | None = Field(default=None, alias="callId")
    transcript: list[CallTranscriptTranscriptItem] | None = Field(default=None)

class TranscriptsResponse(BaseModel):
    """Response containing call transcripts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    call_transcripts: list[CallTranscript] | None = Field(default=None, alias="callTranscripts")
    records: PaginationRecords | None = Field(default=None)
    request_id: str | None = Field(default=None, alias="requestId")

class ExtensiveCallPartiesItemContextItemObjectsItemFieldsItem(BaseModel):
    """Nested schema for ExtensiveCallPartiesItemContextItemObjectsItem.fields_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="Field name")
    """Field name"""
    value: Any | None = Field(default=None, description="Field value")
    """Field value"""

class ExtensiveCallPartiesItemContextItemObjectsItem(BaseModel):
    """Nested schema for ExtensiveCallPartiesItemContextItem.objects_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_type: str | None = Field(default=None, alias="objectType", description="CRM object type (Account, Contact, Opportunity, Lead)")
    """CRM object type (Account, Contact, Opportunity, Lead)"""
    object_id: str | None = Field(default=None, alias="objectId", description="CRM record ID")
    """CRM record ID"""
    fields: list[ExtensiveCallPartiesItemContextItemObjectsItemFieldsItem] | None = Field(default=None, description="CRM field values")
    """CRM field values"""

class ExtensiveCallPartiesItemContextItem(BaseModel):
    """Nested schema for ExtensiveCallPartiesItem.context_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    system: str | None = Field(default=None, description="CRM system name (e.g., Salesforce, HubSpot)")
    """CRM system name (e.g., Salesforce, HubSpot)"""
    objects: list[ExtensiveCallPartiesItemContextItemObjectsItem] | None = Field(default=None, description="CRM objects linked to this participant")
    """CRM objects linked to this participant"""

class ExtensiveCallPartiesItem(BaseModel):
    """Nested schema for ExtensiveCall.parties_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Party ID")
    """Party ID"""
    email_address: str | None = Field(default=None, alias="emailAddress", description="Email address")
    """Email address"""
    name: str | None = Field(default=None, description="Full name")
    """Full name"""
    title: str | None = Field(default=None, description="Job title")
    """Job title"""
    user_id: str | None = Field(default=None, alias="userId", description="Gong user ID if internal")
    """Gong user ID if internal"""
    speaker_id: str | None | None = Field(default=None, alias="speakerId", description="Speaker ID for transcript matching")
    """Speaker ID for transcript matching"""
    affiliation: str | None = Field(default=None, description="Internal or External")
    """Internal or External"""
    methods: list[str] | None = Field(default=None, description="Contact methods")
    """Contact methods"""
    phone_number: str | None = Field(default=None, alias="phoneNumber", description="Phone number")
    """Phone number"""
    context: list[ExtensiveCallPartiesItemContextItem] | None = Field(default=None, description="CRM context data linked to this participant")
    """CRM context data linked to this participant"""

class ExtensiveCallContentTopicsItem(BaseModel):
    """Nested schema for ExtensiveCallContent.topics_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    duration: float | None = Field(default=None)

class ExtensiveCallContentTrackersItem(BaseModel):
    """Nested schema for ExtensiveCallContent.trackers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    count: int | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    occurrences: list[dict[str, Any]] | None = Field(default=None)

class ExtensiveCallContent(BaseModel):
    """Content data including topics and trackers"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    topics: list[ExtensiveCallContentTopicsItem] | None = Field(default=None)
    trackers: list[ExtensiveCallContentTrackersItem] | None = Field(default=None)
    points_of_interest: dict[str, Any] | None = Field(default=None, alias="pointsOfInterest")

class ExtensiveCallMetadata(BaseModel):
    """Call metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None, description="Unique call identifier")
    """Unique call identifier"""
    url: str | None = Field(default=None, description="URL to call in Gong")
    """URL to call in Gong"""
    title: str | None = Field(default=None, description="Call title")
    """Call title"""
    scheduled: str | None = Field(default=None, description="Scheduled time")
    """Scheduled time"""
    started: str | None = Field(default=None, description="Call start time")
    """Call start time"""
    duration: int | None = Field(default=None, description="Call duration in seconds")
    """Call duration in seconds"""
    primary_user_id: str | None = Field(default=None, alias="primaryUserId", description="Primary user ID")
    """Primary user ID"""
    direction: str | None = Field(default=None, description="Call direction")
    """Call direction"""
    system: str | None = Field(default=None, description="System type")
    """System type"""
    scope: str | None = Field(default=None, description="Call scope")
    """Call scope"""
    media: str | None = Field(default=None, description="Media type (Audio/Video)")
    """Media type (Audio/Video)"""
    language: str | None = Field(default=None, description="Call language")
    """Call language"""
    workspace_id: str | None = Field(default=None, alias="workspaceId", description="Workspace ID")
    """Workspace ID"""
    sdr_disposition: str | None | None = Field(default=None, alias="sdrDisposition", description="SDR disposition")
    """SDR disposition"""
    client_unique_id: str | None | None = Field(default=None, alias="clientUniqueId", description="Client unique identifier")
    """Client unique identifier"""
    custom_data: str | None | None = Field(default=None, alias="customData", description="Custom data")
    """Custom data"""
    purpose: str | None | None = Field(default=None, description="Call purpose")
    """Call purpose"""
    is_private: bool | None = Field(default=None, alias="isPrivate", description="Whether call is private")
    """Whether call is private"""
    meeting_url: str | None = Field(default=None, alias="meetingUrl", description="Meeting URL")
    """Meeting URL"""
    calendar_event_id: str | None | None = Field(default=None, alias="calendarEventId", description="Calendar event ID")
    """Calendar event ID"""

class ExtensiveCallMedia(BaseModel):
    """Media URLs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    audio_url: str | None = Field(default=None, alias="audioUrl")
    video_url: str | None = Field(default=None, alias="videoUrl")

class ExtensiveCallCollaboration(BaseModel):
    """Collaboration data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    public_comments: list[dict[str, Any]] | None = Field(default=None, alias="publicComments")

class ExtensiveCallInteractionInteractionstatsItem(BaseModel):
    """Nested schema for ExtensiveCallInteraction.interactionStats_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="Stat name")
    """Stat name"""
    value: float | None = Field(default=None, description="Stat value")
    """Stat value"""

class ExtensiveCallInteractionQuestions(BaseModel):
    """Nested schema for ExtensiveCallInteraction.questions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    company_count: int | None = Field(default=None, alias="companyCount")
    non_company_count: int | None = Field(default=None, alias="nonCompanyCount")

class ExtensiveCallInteraction(BaseModel):
    """Interaction statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    interaction_stats: list[ExtensiveCallInteractionInteractionstatsItem] | None = Field(default=None, alias="interactionStats")
    questions: ExtensiveCallInteractionQuestions | None = Field(default=None)

class ExtensiveCall(BaseModel):
    """Detailed call object with extended information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    meta_data: ExtensiveCallMetadata | None = Field(default=None, alias="metaData")
    parties: list[ExtensiveCallPartiesItem] | None = Field(default=None)
    interaction: ExtensiveCallInteraction | None = Field(default=None)
    collaboration: ExtensiveCallCollaboration | None = Field(default=None)
    content: ExtensiveCallContent | None = Field(default=None)
    media: ExtensiveCallMedia | None = Field(default=None)

class ExtensiveCallsResponse(BaseModel):
    """Response containing detailed call data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls: list[ExtensiveCall] | None = Field(default=None)
    records: PaginationRecords | None = Field(default=None)
    request_id: str | None = Field(default=None, alias="requestId")

class UserAggregateActivityStats(BaseModel):
    """Aggregated activity statistics for a user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls_as_host: int | None = Field(default=None, alias="callsAsHost")
    calls_gave_feedback: int | None = Field(default=None, alias="callsGaveFeedback")
    calls_requested_feedback: int | None = Field(default=None, alias="callsRequestedFeedback")
    calls_received_feedback: int | None = Field(default=None, alias="callsReceivedFeedback")
    own_calls_listened_to: int | None = Field(default=None, alias="ownCallsListenedTo")
    others_calls_listened_to: int | None = Field(default=None, alias="othersCallsListenedTo")
    calls_shared_internally: int | None = Field(default=None, alias="callsSharedInternally")
    calls_shared_externally: int | None = Field(default=None, alias="callsSharedExternally")
    calls_scorecards_filled: int | None = Field(default=None, alias="callsScorecardsFilled")
    calls_scorecards_received: int | None = Field(default=None, alias="callsScorecardsReceived")
    calls_attended: int | None = Field(default=None, alias="callsAttended")
    calls_comments_given: int | None = Field(default=None, alias="callsCommentsGiven")
    calls_comments_received: int | None = Field(default=None, alias="callsCommentsReceived")
    calls_marked_as_feedback_given: int | None = Field(default=None, alias="callsMarkedAsFeedbackGiven")
    calls_marked_as_feedback_received: int | None = Field(default=None, alias="callsMarkedAsFeedbackReceived")

class UserAggregateActivity(BaseModel):
    """User with aggregated activity statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_id: str | None = Field(default=None, alias="userId")
    user_email_address: str | None = Field(default=None, alias="userEmailAddress")
    user_aggregate_activity_stats: UserAggregateActivityStats | None = Field(default=None, alias="userAggregateActivityStats")

class ActivityAggregateResponse(BaseModel):
    """Response containing aggregated activity statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    records: PaginationRecords | None = Field(default=None)
    users_aggregate_activity_stats: list[UserAggregateActivity] | None = Field(default=None, alias="usersAggregateActivityStats")
    from_date_time: str | None = Field(default=None, alias="fromDateTime")
    to_date_time: str | None = Field(default=None, alias="toDateTime")
    time_zone: str | None = Field(default=None, alias="timeZone")

class DailyActivityStats(BaseModel):
    """Daily activity statistics with call IDs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls_as_host: list[str] | None = Field(default=None, alias="callsAsHost")
    calls_gave_feedback: list[str] | None = Field(default=None, alias="callsGaveFeedback")
    calls_requested_feedback: list[str] | None = Field(default=None, alias="callsRequestedFeedback")
    calls_received_feedback: list[str] | None = Field(default=None, alias="callsReceivedFeedback")
    own_calls_listened_to: list[str] | None = Field(default=None, alias="ownCallsListenedTo")
    others_calls_listened_to: list[str] | None = Field(default=None, alias="othersCallsListenedTo")
    calls_shared_internally: list[str] | None = Field(default=None, alias="callsSharedInternally")
    calls_shared_externally: list[str] | None = Field(default=None, alias="callsSharedExternally")
    calls_attended: list[str] | None = Field(default=None, alias="callsAttended")
    calls_comments_given: list[str] | None = Field(default=None, alias="callsCommentsGiven")
    calls_comments_received: list[str] | None = Field(default=None, alias="callsCommentsReceived")
    calls_marked_as_feedback_given: list[str] | None = Field(default=None, alias="callsMarkedAsFeedbackGiven")
    calls_marked_as_feedback_received: list[str] | None = Field(default=None, alias="callsMarkedAsFeedbackReceived")
    calls_scorecards_filled: list[str] | None = Field(default=None, alias="callsScorecardsFilled")
    calls_scorecards_received: list[str] | None = Field(default=None, alias="callsScorecardsReceived")
    from_date: str | None = Field(default=None, alias="fromDate")
    to_date: str | None = Field(default=None, alias="toDate")

class UserDetailedActivity(BaseModel):
    """User with detailed daily activity statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_id: str | None = Field(default=None, alias="userId")
    user_email_address: str | None = Field(default=None, alias="userEmailAddress")
    user_daily_activity_stats: list[DailyActivityStats] | None = Field(default=None, alias="userDailyActivityStats")

class ActivityDayByDayResponse(BaseModel):
    """Response containing daily activity statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    records: PaginationRecords | None = Field(default=None)
    users_detailed_activities: list[UserDetailedActivity] | None = Field(default=None, alias="usersDetailedActivities")

class PersonInteractionStat(BaseModel):
    """Individual interaction statistic"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None)
    value: float | None = Field(default=None)

class UserInteractionStats(BaseModel):
    """User with interaction statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_id: str | None = Field(default=None, alias="userId")
    user_email_address: str | None = Field(default=None, alias="userEmailAddress")
    person_interaction_stats: list[PersonInteractionStat] | None = Field(default=None, alias="personInteractionStats")

class InteractionStatsResponse(BaseModel):
    """Response containing interaction statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    records: PaginationRecords | None = Field(default=None)
    people_interaction_stats: list[UserInteractionStats] | None = Field(default=None, alias="peopleInteractionStats")
    from_date_time: str | None = Field(default=None, alias="fromDateTime")
    to_date_time: str | None = Field(default=None, alias="toDateTime")
    time_zone: str | None = Field(default=None, alias="timeZone")

class ScorecardQuestionAnsweroptionsItem(BaseModel):
    """Nested schema for ScorecardQuestion.answerOptions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    option_id: str | None = Field(default=None, alias="optionId")
    option_text: str | None = Field(default=None, alias="optionText")
    score: float | None = Field(default=None)

class ScorecardQuestion(BaseModel):
    """A question within a scorecard"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    question_id: str | None = Field(default=None, alias="questionId")
    question_revision_id: str | None = Field(default=None, alias="questionRevisionId")
    question_text: str | None = Field(default=None, alias="questionText")
    question_type: str | None = Field(default=None, alias="questionType")
    is_required: bool | None = Field(default=None, alias="isRequired")
    is_overall: bool | None = Field(default=None, alias="isOverall")
    updater_user_id: str | None = Field(default=None, alias="updaterUserId")
    answer_guide: str | None = Field(default=None, alias="answerGuide")
    min_range: str | None = Field(default=None, alias="minRange")
    max_range: str | None = Field(default=None, alias="maxRange")
    created: str | None = Field(default=None)
    updated: str | None = Field(default=None)
    answer_options: list[ScorecardQuestionAnsweroptionsItem] | None = Field(default=None, alias="answerOptions")

class Scorecard(BaseModel):
    """Scorecard configuration"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    scorecard_id: str | None = Field(default=None, alias="scorecardId")
    scorecard_name: str | None = Field(default=None, alias="scorecardName")
    workspace_id: str | None = Field(default=None, alias="workspaceId")
    enabled: bool | None = Field(default=None)
    updater_user_id: str | None = Field(default=None, alias="updaterUserId")
    created: str | None = Field(default=None)
    updated: str | None = Field(default=None)
    review_method: str | None = Field(default=None, alias="reviewMethod")
    questions: list[ScorecardQuestion] | None = Field(default=None)

class ScorecardsResponse(BaseModel):
    """Response containing list of scorecards"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    scorecards: list[Scorecard] | None = Field(default=None)

class TrackerLanguagekeywordsItem(BaseModel):
    """Nested schema for Tracker.languageKeywords_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    language: str | None = Field(default=None, description="Language code")
    """Language code"""
    keywords: list[str] | None = Field(default=None, description="List of keywords for this language")
    """List of keywords for this language"""
    include_related_forms: bool | None = Field(default=None, alias="includeRelatedForms", description="Whether to include related word forms")
    """Whether to include related word forms"""

class Tracker(BaseModel):
    """Keyword tracker configuration"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tracker_id: str | None = Field(default=None, alias="trackerId")
    tracker_name: str | None = Field(default=None, alias="trackerName")
    workspace_id: str | None = Field(default=None, alias="workspaceId")
    language_keywords: list[TrackerLanguagekeywordsItem] | None = Field(default=None, alias="languageKeywords")
    affiliation: str | None = Field(default=None)
    part_of_question: bool | None = Field(default=None, alias="partOfQuestion")
    said_at: str | None = Field(default=None, alias="saidAt")
    said_at_interval: str | None = Field(default=None, alias="saidAtInterval")
    said_at_unit: str | None = Field(default=None, alias="saidAtUnit")
    said_in_topics: list[str] | None = Field(default=None, alias="saidInTopics")
    filter_query: str | None = Field(default=None, alias="filterQuery")
    created: str | None = Field(default=None)
    creator_user_id: str | None = Field(default=None, alias="creatorUserId")
    updated: str | None = Field(default=None)
    updater_user_id: str | None = Field(default=None, alias="updaterUserId")

class TrackersResponse(BaseModel):
    """Response containing list of trackers"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    keyword_trackers: list[Tracker] | None = Field(default=None, alias="keywordTrackers")

class LibraryFolder(BaseModel):
    """Library folder structure"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    parent_folder_id: str | None = Field(default=None, alias="parentFolderId")
    created_by: str | None = Field(default=None, alias="createdBy")
    updated: str | None = Field(default=None)

class LibraryFoldersResponse(BaseModel):
    """Response containing library folder structure"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    folders: list[LibraryFolder] | None = Field(default=None)

class FolderCall(BaseModel):
    """Call within a library folder"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    call_id: str | None = Field(default=None, alias="callId")
    title: str | None = Field(default=None)
    started: str | None = Field(default=None)
    duration: int | None = Field(default=None)
    primary_user_id: str | None = Field(default=None, alias="primaryUserId")
    url: str | None = Field(default=None)

class FolderContentResponse(BaseModel):
    """Response containing calls in a folder"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    created_by: str | None = Field(default=None, alias="createdBy")
    updated: str | None = Field(default=None)
    calls: list[FolderCall] | None = Field(default=None)
    records: PaginationRecords | None = Field(default=None)

class CoachingMetrics(BaseModel):
    """Coaching metrics for a user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls_listened: int | None = Field(default=None, alias="callsListened")
    calls_attended: int | None = Field(default=None, alias="callsAttended")
    calls_with_feedback: int | None = Field(default=None, alias="callsWithFeedback")
    calls_with_comments: int | None = Field(default=None, alias="callsWithComments")
    scorecards_filled: int | None = Field(default=None, alias="scorecardsFilled")

class CoachingData(BaseModel):
    """Coaching data for a user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_id: str | None = Field(default=None, alias="userId")
    user_email_address: str | None = Field(default=None, alias="userEmailAddress")
    user_name: str | None = Field(default=None, alias="userName")
    is_manager: bool | None = Field(default=None, alias="isManager")
    coaching_metrics: CoachingMetrics | None = Field(default=None, alias="coachingMetrics")

class CoachingResponse(BaseModel):
    """Response containing coaching metrics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    coaching_data: list[CoachingData] | None = Field(default=None, alias="coachingData")
    from_date_time: str | None = Field(default=None, alias="fromDateTime")
    to_date_time: str | None = Field(default=None, alias="toDateTime")

class AnsweredScorecardAnswer(BaseModel):
    """An answer to a scorecard question"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    question_id: str | None = Field(default=None, alias="questionId")
    question_revision_id: str | None = Field(default=None, alias="questionRevisionId")
    is_overall: bool | None = Field(default=None, alias="isOverall")
    answer: str | None = Field(default=None)
    answer_text: str | None = Field(default=None, alias="answerText")
    score: float | None = Field(default=None)
    not_applicable: bool | None = Field(default=None, alias="notApplicable")
    selected_options: list[str] | None = Field(default=None, alias="selectedOptions")

class AnsweredScorecard(BaseModel):
    """A completed scorecard"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    answered_scorecard_id: str | None = Field(default=None, alias="answeredScorecardId")
    scorecard_id: str | None = Field(default=None, alias="scorecardId")
    scorecard_name: str | None = Field(default=None, alias="scorecardName")
    call_id: str | None = Field(default=None, alias="callId")
    call_start_time: str | None = Field(default=None, alias="callStartTime")
    reviewed_user_id: str | None = Field(default=None, alias="reviewedUserId")
    reviewer_user_id: str | None = Field(default=None, alias="reviewerUserId")
    review_method: str | None = Field(default=None, alias="reviewMethod")
    editor_user_id: str | None = Field(default=None, alias="editorUserId")
    answered_date_time: str | None = Field(default=None, alias="answeredDateTime")
    review_time: str | None = Field(default=None, alias="reviewTime")
    visibility_type: str | None = Field(default=None, alias="visibilityType")
    answers: list[AnsweredScorecardAnswer] | None = Field(default=None)
    overall_score: float | None = Field(default=None, alias="overallScore")
    visibility: str | None = Field(default=None)

class AnsweredScorecardsResponse(BaseModel):
    """Response containing answered scorecards"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: str | None = Field(default=None, alias="requestId")
    answered_scorecards: list[AnsweredScorecard] | None = Field(default=None, alias="answeredScorecards")
    records: PaginationRecords | None = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    total_records: int | None = Field(default=None)
    current_page_number: int | None = Field(default=None)

class CallsListResultMeta(BaseModel):
    """Metadata for calls.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    total_records: int | None = Field(default=None)
    current_page_number: int | None = Field(default=None)

class CallsExtensiveListResultMeta(BaseModel):
    """Metadata for calls_extensive.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    total_records: int | None = Field(default=None)
    current_page_number: int | None = Field(default=None)

class CallTranscriptsListResultMeta(BaseModel):
    """Metadata for call_transcripts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    total_records: int | None = Field(default=None)
    current_page_number: int | None = Field(default=None)

class StatsActivityAggregateListResultMeta(BaseModel):
    """Metadata for stats_activity_aggregate.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    total_records: int | None = Field(default=None)
    current_page_number: int | None = Field(default=None)

class StatsActivityDayByDayListResultMeta(BaseModel):
    """Metadata for stats_activity_day_by_day.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    total_records: int | None = Field(default=None)
    current_page_number: int | None = Field(default=None)

class StatsInteractionListResultMeta(BaseModel):
    """Metadata for stats_interaction.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    total_records: int | None = Field(default=None)
    current_page_number: int | None = Field(default=None)

class LibraryFolderContentListResultMeta(BaseModel):
    """Metadata for library_folder_content.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    total_records: int | None = Field(default=None)
    current_page_number: int | None = Field(default=None)

class StatsActivityScorecardsListResultMeta(BaseModel):
    """Metadata for stats_activity_scorecards.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    cursor: str | None = Field(default=None)
    total_records: int | None = Field(default=None)
    current_page_number: int | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class GongCheckResult(BaseModel):
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


class GongExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class GongExecuteResultWithMeta(GongExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    active: bool | None = None
    """Indicates if the user is currently active or not"""
    created: str | None = None
    """The timestamp denoting when the user account was created"""
    email_address: str | None = None
    """The primary email address associated with the user"""
    email_aliases: list[Any] | None = None
    """Additional email addresses that can be used to reach the user"""
    extension: str | None = None
    """The phone extension number for the user"""
    first_name: str | None = None
    """The first name of the user"""
    id: str | None = None
    """Unique identifier for the user"""
    last_name: str | None = None
    """The last name of the user"""
    manager_id: str | None = None
    """The ID of the user's manager"""
    meeting_consent_page_url: str | None = None
    """URL for the consent page related to meetings"""
    personal_meeting_urls: list[Any] | None = None
    """URLs for personal meeting rooms assigned to the user"""
    phone_number: str | None = None
    """The phone number associated with the user"""
    settings: dict[str, Any] | None = None
    """User-specific settings and configurations"""
    spoken_languages: list[Any] | None = None
    """Languages spoken by the user"""
    title: str | None = None
    """The job title or position of the user"""
    trusted_email_address: str | None = None
    """An email address that is considered trusted for the user"""


class CallsSearchData(BaseModel):
    """Search result data for calls entity."""
    model_config = ConfigDict(extra="allow")

    calendar_event_id: str | None = None
    """Unique identifier for the calendar event associated with the call."""
    client_unique_id: str | None = None
    """Unique identifier for the client related to the call."""
    custom_data: str | None = None
    """Custom data associated with the call."""
    direction: str | None = None
    """Direction of the call (inbound/outbound)."""
    duration: int | None = None
    """Duration of the call in seconds."""
    id: str | None = None
    """Unique identifier for the call."""
    is_private: bool | None = None
    """Indicates if the call is private or not."""
    language: str | None = None
    """Language used in the call."""
    media: str | None = None
    """Media type used for communication (voice, video, etc.)."""
    meeting_url: str | None = None
    """URL for accessing the meeting associated with the call."""
    primary_user_id: str | None = None
    """Unique identifier for the primary user involved in the call."""
    purpose: str | None = None
    """Purpose or topic of the call."""
    scheduled: str | None = None
    """Scheduled date and time of the call."""
    scope: str | None = None
    """Scope or extent of the call."""
    sdr_disposition: str | None = None
    """Disposition set by the sales development representative."""
    started: str | None = None
    """Start date and time of the call."""
    system: str | None = None
    """System information related to the call."""
    title: str | None = None
    """Title or headline of the call."""
    url: str | None = None
    """URL associated with the call."""
    workspace_id: str | None = None
    """Identifier for the workspace to which the call belongs."""


class CallsExtensiveSearchData(BaseModel):
    """Search result data for calls_extensive entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Unique identifier for the call (from metaData.id)."""
    startdatetime: str | None = None
    """Datetime for extensive calls."""
    collaboration: dict[str, Any] | None = None
    """Collaboration information added to the call"""
    content: dict[str, Any] | None = None
    """Analysis of the interaction content."""
    context: dict[str, Any] | None = None
    """A list of the agenda of each part of the call."""
    interaction: dict[str, Any] | None = None
    """Metrics collected around the interaction during the call."""
    media: dict[str, Any] | None = None
    """The media urls of the call."""
    meta_data: dict[str, Any] | None = None
    """call's metadata."""
    parties: list[Any] | None = None
    """A list of the call's participants"""


class SettingsScorecardsSearchData(BaseModel):
    """Search result data for settings_scorecards entity."""
    model_config = ConfigDict(extra="allow")

    created: str | None = None
    """The timestamp when the scorecard was created"""
    enabled: bool | None = None
    """Indicates if the scorecard is enabled or disabled"""
    questions: list[Any] | None = None
    """An array of questions related to the scorecard"""
    scorecard_id: str | None = None
    """The unique identifier of the scorecard"""
    scorecard_name: str | None = None
    """The name of the scorecard"""
    updated: str | None = None
    """The timestamp when the scorecard was last updated"""
    updater_user_id: str | None = None
    """The user ID of the person who last updated the scorecard"""
    workspace_id: str | None = None
    """The unique identifier of the workspace associated with the scorecard"""


class StatsActivityScorecardsSearchData(BaseModel):
    """Search result data for stats_activity_scorecards entity."""
    model_config = ConfigDict(extra="allow")

    answered_scorecard_id: str | None = None
    """Unique identifier for the answered scorecard instance."""
    answers: list[Any] | None = None
    """Contains the answered questions in the scorecards"""
    call_id: str | None = None
    """Unique identifier for the call associated with the answered scorecard."""
    call_start_time: str | None = None
    """Timestamp indicating the start time of the call."""
    review_time: str | None = None
    """Timestamp indicating when the review of the answered scorecard was completed."""
    reviewed_user_id: str | None = None
    """Unique identifier for the user whose performance was reviewed."""
    reviewer_user_id: str | None = None
    """Unique identifier for the user who performed the review."""
    scorecard_id: str | None = None
    """Unique identifier for the scorecard template used."""
    scorecard_name: str | None = None
    """Name or title of the scorecard template used."""
    visibility_type: str | None = None
    """Type indicating the visibility permissions for the answered scorecard."""


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

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""

CallsSearchResult = AirbyteSearchResult[CallsSearchData]
"""Search result type for calls entity."""

CallsExtensiveSearchResult = AirbyteSearchResult[CallsExtensiveSearchData]
"""Search result type for calls_extensive entity."""

SettingsScorecardsSearchResult = AirbyteSearchResult[SettingsScorecardsSearchData]
"""Search result type for settings_scorecards entity."""

StatsActivityScorecardsSearchResult = AirbyteSearchResult[StatsActivityScorecardsSearchData]
"""Search result type for stats_activity_scorecards entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

UsersListResult = GongExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

CallsListResult = GongExecuteResultWithMeta[list[Call], CallsListResultMeta]
"""Result type for calls.list operation with data and metadata."""

CallsExtensiveListResult = GongExecuteResultWithMeta[list[ExtensiveCall], CallsExtensiveListResultMeta]
"""Result type for calls_extensive.list operation with data and metadata."""

WorkspacesListResult = GongExecuteResult[list[Workspace]]
"""Result type for workspaces.list operation."""

CallTranscriptsListResult = GongExecuteResultWithMeta[list[CallTranscript], CallTranscriptsListResultMeta]
"""Result type for call_transcripts.list operation with data and metadata."""

StatsActivityAggregateListResult = GongExecuteResultWithMeta[list[UserAggregateActivity], StatsActivityAggregateListResultMeta]
"""Result type for stats_activity_aggregate.list operation with data and metadata."""

StatsActivityDayByDayListResult = GongExecuteResultWithMeta[list[UserDetailedActivity], StatsActivityDayByDayListResultMeta]
"""Result type for stats_activity_day_by_day.list operation with data and metadata."""

StatsInteractionListResult = GongExecuteResultWithMeta[list[UserInteractionStats], StatsInteractionListResultMeta]
"""Result type for stats_interaction.list operation with data and metadata."""

SettingsScorecardsListResult = GongExecuteResult[list[Scorecard]]
"""Result type for settings_scorecards.list operation."""

SettingsTrackersListResult = GongExecuteResult[list[Tracker]]
"""Result type for settings_trackers.list operation."""

LibraryFoldersListResult = GongExecuteResult[list[LibraryFolder]]
"""Result type for library_folders.list operation."""

LibraryFolderContentListResult = GongExecuteResultWithMeta[list[FolderCall], LibraryFolderContentListResultMeta]
"""Result type for library_folder_content.list operation with data and metadata."""

CoachingListResult = GongExecuteResult[list[CoachingData]]
"""Result type for coaching.list operation."""

StatsActivityScorecardsListResult = GongExecuteResultWithMeta[list[AnsweredScorecard], StatsActivityScorecardsListResultMeta]
"""Result type for stats_activity_scorecards.list operation with data and metadata."""

