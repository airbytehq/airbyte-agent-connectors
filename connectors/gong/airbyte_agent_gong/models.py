"""
Pydantic models for gong connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration - multiple options available

class GongOauth20AuthenticationAuthConfig(BaseModel):
    """OAuth 2.0 Authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """Your Gong OAuth2 Access Token. Token refresh is managed externally."""

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

    total_records: Union[int, Any] = Field(default=None, alias="totalRecords")
    current_page_size: Union[int, Any] = Field(default=None, alias="currentPageSize")
    current_page_number: Union[int, Any] = Field(default=None, alias="currentPageNumber")
    cursor: Union[str, Any] = Field(default=None)

class UserSpokenlanguagesItem(BaseModel):
    """Nested schema for User.spokenLanguages_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    language: Union[str, Any] = Field(default=None)
    primary: Union[bool, Any] = Field(default=None)

class UserSettings(BaseModel):
    """User settings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    web_conferences_recorded: Union[bool, Any] = Field(default=None, alias="webConferencesRecorded")
    prevent_web_conference_recording: Union[bool, Any] = Field(default=None, alias="preventWebConferenceRecording")
    telephony_calls_imported: Union[bool, Any] = Field(default=None, alias="telephonyCallsImported")
    emails_imported: Union[bool, Any] = Field(default=None, alias="emailsImported")
    prevent_email_import: Union[bool, Any] = Field(default=None, alias="preventEmailImport")
    non_recorded_meetings_imported: Union[bool, Any] = Field(default=None, alias="nonRecordedMeetingsImported")
    gong_connect_enabled: Union[bool, Any] = Field(default=None, alias="gongConnectEnabled")

class User(BaseModel):
    """User object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    email_address: Union[str, Any] = Field(default=None, alias="emailAddress")
    created: Union[str, Any] = Field(default=None)
    active: Union[bool, Any] = Field(default=None)
    email_aliases: Union[list[str], Any] = Field(default=None, alias="emailAliases")
    trusted_email_address: Union[str | None, Any] = Field(default=None, alias="trustedEmailAddress")
    first_name: Union[str, Any] = Field(default=None, alias="firstName")
    last_name: Union[str, Any] = Field(default=None, alias="lastName")
    title: Union[str | None, Any] = Field(default=None)
    phone_number: Union[str | None, Any] = Field(default=None, alias="phoneNumber")
    extension: Union[str | None, Any] = Field(default=None)
    personal_meeting_urls: Union[list[str], Any] = Field(default=None, alias="personalMeetingUrls")
    settings: Union[UserSettings, Any] = Field(default=None)
    manager_id: Union[str | None, Any] = Field(default=None, alias="managerId")
    meeting_consent_page_url: Union[str | None, Any] = Field(default=None, alias="meetingConsentPageUrl")
    spoken_languages: Union[list[UserSpokenlanguagesItem], Any] = Field(default=None, alias="spokenLanguages")

class UsersResponse(BaseModel):
    """Response containing list of users"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    users: Union[list[User], Any] = Field(default=None)
    records: Union[PaginationRecords, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None, alias="requestId")

class UserResponse(BaseModel):
    """Response containing single user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user: Union[User, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None, alias="requestId")

class Call(BaseModel):
    """Call object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    url: Union[str, Any] = Field(default=None)
    title: Union[str, Any] = Field(default=None)
    scheduled: Union[str, Any] = Field(default=None)
    started: Union[str, Any] = Field(default=None)
    duration: Union[int, Any] = Field(default=None)
    primary_user_id: Union[str, Any] = Field(default=None, alias="primaryUserId")
    direction: Union[str, Any] = Field(default=None)
    system: Union[str, Any] = Field(default=None)
    scope: Union[str, Any] = Field(default=None)
    media: Union[str, Any] = Field(default=None)
    language: Union[str, Any] = Field(default=None)
    workspace_id: Union[str, Any] = Field(default=None, alias="workspaceId")
    sdr_disposition: Union[str | None, Any] = Field(default=None, alias="sdrDisposition")
    client_unique_id: Union[str | None, Any] = Field(default=None, alias="clientUniqueId")
    custom_data: Union[str | None, Any] = Field(default=None, alias="customData")
    purpose: Union[str | None, Any] = Field(default=None)
    meeting_url: Union[str, Any] = Field(default=None, alias="meetingUrl")
    is_private: Union[bool, Any] = Field(default=None, alias="isPrivate")
    calendar_event_id: Union[str | None, Any] = Field(default=None, alias="calendarEventId")

class CallsResponse(BaseModel):
    """Response containing list of calls"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls: Union[list[Call], Any] = Field(default=None)
    records: Union[PaginationRecords, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None, alias="requestId")

class CallResponse(BaseModel):
    """Response containing single call"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    call: Union[Call, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None, alias="requestId")

class Workspace(BaseModel):
    """Workspace object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    workspace_id: Union[str, Any] = Field(default=None, alias="workspaceId")
    name: Union[str, Any] = Field(default=None)
    description: Union[str, Any] = Field(default=None)

class WorkspacesResponse(BaseModel):
    """Response containing list of workspaces"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    workspaces: Union[list[Workspace], Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None, alias="requestId")

class CallTranscriptTranscriptItemSentencesItem(BaseModel):
    """Nested schema for CallTranscriptTranscriptItem.sentences_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    start: Union[int, Any] = Field(default=None, description="Start time in seconds")
    """Start time in seconds"""
    end: Union[int, Any] = Field(default=None, description="End time in seconds")
    """End time in seconds"""
    text: Union[str, Any] = Field(default=None, description="Sentence text")
    """Sentence text"""

class CallTranscriptTranscriptItem(BaseModel):
    """Nested schema for CallTranscript.transcript_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    speaker_id: Union[str, Any] = Field(default=None, alias="speakerId", description="Speaker identifier")
    """Speaker identifier"""
    topic: Union[str | None, Any] = Field(default=None, description="Topic")
    """Topic"""
    sentences: Union[list[CallTranscriptTranscriptItemSentencesItem], Any] = Field(default=None)

class CallTranscript(BaseModel):
    """Call transcript object"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    call_id: Union[str, Any] = Field(default=None, alias="callId")
    transcript: Union[list[CallTranscriptTranscriptItem], Any] = Field(default=None)

class TranscriptsResponse(BaseModel):
    """Response containing call transcripts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    call_transcripts: Union[list[CallTranscript], Any] = Field(default=None, alias="callTranscripts")
    records: Union[PaginationRecords, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None, alias="requestId")

class ExtensiveCallMedia(BaseModel):
    """Media URLs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    audio_url: Union[str, Any] = Field(default=None, alias="audioUrl")
    video_url: Union[str, Any] = Field(default=None, alias="videoUrl")

class ExtensiveCallMetadata(BaseModel):
    """Call metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Unique call identifier")
    """Unique call identifier"""
    url: Union[str, Any] = Field(default=None, description="URL to call in Gong")
    """URL to call in Gong"""
    title: Union[str, Any] = Field(default=None, description="Call title")
    """Call title"""
    scheduled: Union[str, Any] = Field(default=None, description="Scheduled time")
    """Scheduled time"""
    started: Union[str, Any] = Field(default=None, description="Call start time")
    """Call start time"""
    duration: Union[int, Any] = Field(default=None, description="Call duration in seconds")
    """Call duration in seconds"""
    primary_user_id: Union[str, Any] = Field(default=None, alias="primaryUserId", description="Primary user ID")
    """Primary user ID"""
    direction: Union[str, Any] = Field(default=None, description="Call direction")
    """Call direction"""
    system: Union[str, Any] = Field(default=None, description="System type")
    """System type"""
    scope: Union[str, Any] = Field(default=None, description="Call scope")
    """Call scope"""
    media: Union[str, Any] = Field(default=None, description="Media type (Audio/Video)")
    """Media type (Audio/Video)"""
    language: Union[str, Any] = Field(default=None, description="Call language")
    """Call language"""
    workspace_id: Union[str, Any] = Field(default=None, alias="workspaceId", description="Workspace ID")
    """Workspace ID"""
    sdr_disposition: Union[str | None, Any] = Field(default=None, alias="sdrDisposition", description="SDR disposition")
    """SDR disposition"""
    client_unique_id: Union[str | None, Any] = Field(default=None, alias="clientUniqueId", description="Client unique identifier")
    """Client unique identifier"""
    custom_data: Union[str | None, Any] = Field(default=None, alias="customData", description="Custom data")
    """Custom data"""
    purpose: Union[str | None, Any] = Field(default=None, description="Call purpose")
    """Call purpose"""
    is_private: Union[bool, Any] = Field(default=None, alias="isPrivate", description="Whether call is private")
    """Whether call is private"""
    meeting_url: Union[str, Any] = Field(default=None, alias="meetingUrl", description="Meeting URL")
    """Meeting URL"""
    calendar_event_id: Union[str | None, Any] = Field(default=None, alias="calendarEventId", description="Calendar event ID")
    """Calendar event ID"""

class ExtensiveCallPartiesItemContextItemObjectsItemFieldsItem(BaseModel):
    """Nested schema for ExtensiveCallPartiesItemContextItemObjectsItem.fields_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None, description="Field name")
    """Field name"""
    value: Union[Any, Any] = Field(default=None, description="Field value")
    """Field value"""

class ExtensiveCallPartiesItemContextItemObjectsItem(BaseModel):
    """Nested schema for ExtensiveCallPartiesItemContextItem.objects_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object_type: Union[str, Any] = Field(default=None, alias="objectType", description="CRM object type (Account, Contact, Opportunity, Lead)")
    """CRM object type (Account, Contact, Opportunity, Lead)"""
    object_id: Union[str, Any] = Field(default=None, alias="objectId", description="CRM record ID")
    """CRM record ID"""
    fields: Union[list[ExtensiveCallPartiesItemContextItemObjectsItemFieldsItem], Any] = Field(default=None, description="CRM field values")
    """CRM field values"""

class ExtensiveCallPartiesItemContextItem(BaseModel):
    """Nested schema for ExtensiveCallPartiesItem.context_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    system: Union[str, Any] = Field(default=None, description="CRM system name (e.g., Salesforce, HubSpot)")
    """CRM system name (e.g., Salesforce, HubSpot)"""
    objects: Union[list[ExtensiveCallPartiesItemContextItemObjectsItem], Any] = Field(default=None, description="CRM objects linked to this participant")
    """CRM objects linked to this participant"""

class ExtensiveCallPartiesItem(BaseModel):
    """Nested schema for ExtensiveCall.parties_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None, description="Party ID")
    """Party ID"""
    email_address: Union[str, Any] = Field(default=None, alias="emailAddress", description="Email address")
    """Email address"""
    name: Union[str, Any] = Field(default=None, description="Full name")
    """Full name"""
    title: Union[str, Any] = Field(default=None, description="Job title")
    """Job title"""
    user_id: Union[str, Any] = Field(default=None, alias="userId", description="Gong user ID if internal")
    """Gong user ID if internal"""
    speaker_id: Union[str | None, Any] = Field(default=None, alias="speakerId", description="Speaker ID for transcript matching")
    """Speaker ID for transcript matching"""
    affiliation: Union[str, Any] = Field(default=None, description="Internal or External")
    """Internal or External"""
    methods: Union[list[str], Any] = Field(default=None, description="Contact methods")
    """Contact methods"""
    phone_number: Union[str, Any] = Field(default=None, alias="phoneNumber", description="Phone number")
    """Phone number"""
    context: Union[list[ExtensiveCallPartiesItemContextItem], Any] = Field(default=None, description="CRM context data linked to this participant")
    """CRM context data linked to this participant"""

class ExtensiveCallCollaboration(BaseModel):
    """Collaboration data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    public_comments: Union[list[dict[str, Any]], Any] = Field(default=None, alias="publicComments")

class ExtensiveCallContentTrackersItem(BaseModel):
    """Nested schema for ExtensiveCallContent.trackers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    count: Union[int, Any] = Field(default=None)
    type: Union[str, Any] = Field(default=None)
    occurrences: Union[list[dict[str, Any]], Any] = Field(default=None)

class ExtensiveCallContentTopicsItem(BaseModel):
    """Nested schema for ExtensiveCallContent.topics_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    duration: Union[float, Any] = Field(default=None)

class ExtensiveCallContent(BaseModel):
    """Content data including topics and trackers"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    topics: Union[list[ExtensiveCallContentTopicsItem], Any] = Field(default=None)
    trackers: Union[list[ExtensiveCallContentTrackersItem], Any] = Field(default=None)
    points_of_interest: Union[dict[str, Any], Any] = Field(default=None, alias="pointsOfInterest")

class ExtensiveCallInteractionInteractionstatsItem(BaseModel):
    """Nested schema for ExtensiveCallInteraction.interactionStats_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None, description="Stat name")
    """Stat name"""
    value: Union[float, Any] = Field(default=None, description="Stat value")
    """Stat value"""

class ExtensiveCallInteractionQuestions(BaseModel):
    """Nested schema for ExtensiveCallInteraction.questions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    company_count: Union[int, Any] = Field(default=None, alias="companyCount")
    non_company_count: Union[int, Any] = Field(default=None, alias="nonCompanyCount")

class ExtensiveCallInteraction(BaseModel):
    """Interaction statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    interaction_stats: Union[list[ExtensiveCallInteractionInteractionstatsItem], Any] = Field(default=None, alias="interactionStats")
    questions: Union[ExtensiveCallInteractionQuestions, Any] = Field(default=None)

class ExtensiveCall(BaseModel):
    """Detailed call object with extended information"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    meta_data: Union[ExtensiveCallMetadata, Any] = Field(default=None, alias="metaData")
    parties: Union[list[ExtensiveCallPartiesItem], Any] = Field(default=None)
    interaction: Union[ExtensiveCallInteraction, Any] = Field(default=None)
    collaboration: Union[ExtensiveCallCollaboration, Any] = Field(default=None)
    content: Union[ExtensiveCallContent, Any] = Field(default=None)
    media: Union[ExtensiveCallMedia, Any] = Field(default=None)

class ExtensiveCallsResponse(BaseModel):
    """Response containing detailed call data"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls: Union[list[ExtensiveCall], Any] = Field(default=None)
    records: Union[PaginationRecords, Any] = Field(default=None)
    request_id: Union[str, Any] = Field(default=None, alias="requestId")

class UserAggregateActivityStats(BaseModel):
    """Aggregated activity statistics for a user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls_as_host: Union[int, Any] = Field(default=None, alias="callsAsHost")
    calls_gave_feedback: Union[int, Any] = Field(default=None, alias="callsGaveFeedback")
    calls_requested_feedback: Union[int, Any] = Field(default=None, alias="callsRequestedFeedback")
    calls_received_feedback: Union[int, Any] = Field(default=None, alias="callsReceivedFeedback")
    own_calls_listened_to: Union[int, Any] = Field(default=None, alias="ownCallsListenedTo")
    others_calls_listened_to: Union[int, Any] = Field(default=None, alias="othersCallsListenedTo")
    calls_shared_internally: Union[int, Any] = Field(default=None, alias="callsSharedInternally")
    calls_shared_externally: Union[int, Any] = Field(default=None, alias="callsSharedExternally")
    calls_scorecards_filled: Union[int, Any] = Field(default=None, alias="callsScorecardsFilled")
    calls_scorecards_received: Union[int, Any] = Field(default=None, alias="callsScorecardsReceived")
    calls_attended: Union[int, Any] = Field(default=None, alias="callsAttended")
    calls_comments_given: Union[int, Any] = Field(default=None, alias="callsCommentsGiven")
    calls_comments_received: Union[int, Any] = Field(default=None, alias="callsCommentsReceived")
    calls_marked_as_feedback_given: Union[int, Any] = Field(default=None, alias="callsMarkedAsFeedbackGiven")
    calls_marked_as_feedback_received: Union[int, Any] = Field(default=None, alias="callsMarkedAsFeedbackReceived")

class UserAggregateActivity(BaseModel):
    """User with aggregated activity statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_id: Union[str, Any] = Field(default=None, alias="userId")
    user_email_address: Union[str, Any] = Field(default=None, alias="userEmailAddress")
    user_aggregate_activity_stats: Union[UserAggregateActivityStats, Any] = Field(default=None, alias="userAggregateActivityStats")

class ActivityAggregateResponse(BaseModel):
    """Response containing aggregated activity statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: Union[str, Any] = Field(default=None, alias="requestId")
    records: Union[PaginationRecords, Any] = Field(default=None)
    users_aggregate_activity_stats: Union[list[UserAggregateActivity], Any] = Field(default=None, alias="usersAggregateActivityStats")
    from_date_time: Union[str, Any] = Field(default=None, alias="fromDateTime")
    to_date_time: Union[str, Any] = Field(default=None, alias="toDateTime")
    time_zone: Union[str, Any] = Field(default=None, alias="timeZone")

class DailyActivityStats(BaseModel):
    """Daily activity statistics with call IDs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls_as_host: Union[list[str], Any] = Field(default=None, alias="callsAsHost")
    calls_gave_feedback: Union[list[str], Any] = Field(default=None, alias="callsGaveFeedback")
    calls_requested_feedback: Union[list[str], Any] = Field(default=None, alias="callsRequestedFeedback")
    calls_received_feedback: Union[list[str], Any] = Field(default=None, alias="callsReceivedFeedback")
    own_calls_listened_to: Union[list[str], Any] = Field(default=None, alias="ownCallsListenedTo")
    others_calls_listened_to: Union[list[str], Any] = Field(default=None, alias="othersCallsListenedTo")
    calls_shared_internally: Union[list[str], Any] = Field(default=None, alias="callsSharedInternally")
    calls_shared_externally: Union[list[str], Any] = Field(default=None, alias="callsSharedExternally")
    calls_attended: Union[list[str], Any] = Field(default=None, alias="callsAttended")
    calls_comments_given: Union[list[str], Any] = Field(default=None, alias="callsCommentsGiven")
    calls_comments_received: Union[list[str], Any] = Field(default=None, alias="callsCommentsReceived")
    calls_marked_as_feedback_given: Union[list[str], Any] = Field(default=None, alias="callsMarkedAsFeedbackGiven")
    calls_marked_as_feedback_received: Union[list[str], Any] = Field(default=None, alias="callsMarkedAsFeedbackReceived")
    calls_scorecards_filled: Union[list[str], Any] = Field(default=None, alias="callsScorecardsFilled")
    calls_scorecards_received: Union[list[str], Any] = Field(default=None, alias="callsScorecardsReceived")
    from_date: Union[str, Any] = Field(default=None, alias="fromDate")
    to_date: Union[str, Any] = Field(default=None, alias="toDate")

class UserDetailedActivity(BaseModel):
    """User with detailed daily activity statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_id: Union[str, Any] = Field(default=None, alias="userId")
    user_email_address: Union[str, Any] = Field(default=None, alias="userEmailAddress")
    user_daily_activity_stats: Union[list[DailyActivityStats], Any] = Field(default=None, alias="userDailyActivityStats")

class ActivityDayByDayResponse(BaseModel):
    """Response containing daily activity statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: Union[str, Any] = Field(default=None, alias="requestId")
    records: Union[PaginationRecords, Any] = Field(default=None)
    users_detailed_activities: Union[list[UserDetailedActivity], Any] = Field(default=None, alias="usersDetailedActivities")

class PersonInteractionStat(BaseModel):
    """Individual interaction statistic"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str, Any] = Field(default=None)
    value: Union[float, Any] = Field(default=None)

class UserInteractionStats(BaseModel):
    """User with interaction statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_id: Union[str, Any] = Field(default=None, alias="userId")
    user_email_address: Union[str, Any] = Field(default=None, alias="userEmailAddress")
    person_interaction_stats: Union[list[PersonInteractionStat], Any] = Field(default=None, alias="personInteractionStats")

class InteractionStatsResponse(BaseModel):
    """Response containing interaction statistics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: Union[str, Any] = Field(default=None, alias="requestId")
    records: Union[PaginationRecords, Any] = Field(default=None)
    people_interaction_stats: Union[list[UserInteractionStats], Any] = Field(default=None, alias="peopleInteractionStats")
    from_date_time: Union[str, Any] = Field(default=None, alias="fromDateTime")
    to_date_time: Union[str, Any] = Field(default=None, alias="toDateTime")
    time_zone: Union[str, Any] = Field(default=None, alias="timeZone")

class ScorecardQuestionAnsweroptionsItem(BaseModel):
    """Nested schema for ScorecardQuestion.answerOptions_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    option_id: Union[str, Any] = Field(default=None, alias="optionId")
    option_text: Union[str, Any] = Field(default=None, alias="optionText")
    score: Union[float, Any] = Field(default=None)

class ScorecardQuestion(BaseModel):
    """A question within a scorecard"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    question_id: Union[str, Any] = Field(default=None, alias="questionId")
    question_revision_id: Union[str, Any] = Field(default=None, alias="questionRevisionId")
    question_text: Union[str, Any] = Field(default=None, alias="questionText")
    question_type: Union[str, Any] = Field(default=None, alias="questionType")
    is_required: Union[bool, Any] = Field(default=None, alias="isRequired")
    is_overall: Union[bool, Any] = Field(default=None, alias="isOverall")
    updater_user_id: Union[str, Any] = Field(default=None, alias="updaterUserId")
    answer_guide: Union[str | None, Any] = Field(default=None, alias="answerGuide")
    min_range: Union[str | None, Any] = Field(default=None, alias="minRange")
    max_range: Union[str | None, Any] = Field(default=None, alias="maxRange")
    created: Union[str, Any] = Field(default=None)
    updated: Union[str, Any] = Field(default=None)
    answer_options: Union[list[ScorecardQuestionAnsweroptionsItem], Any] = Field(default=None, alias="answerOptions")

class Scorecard(BaseModel):
    """Scorecard configuration"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    scorecard_id: Union[str, Any] = Field(default=None, alias="scorecardId")
    scorecard_name: Union[str, Any] = Field(default=None, alias="scorecardName")
    workspace_id: Union[str | None, Any] = Field(default=None, alias="workspaceId")
    enabled: Union[bool, Any] = Field(default=None)
    updater_user_id: Union[str, Any] = Field(default=None, alias="updaterUserId")
    created: Union[str, Any] = Field(default=None)
    updated: Union[str, Any] = Field(default=None)
    review_method: Union[str, Any] = Field(default=None, alias="reviewMethod")
    questions: Union[list[ScorecardQuestion], Any] = Field(default=None)

class ScorecardsResponse(BaseModel):
    """Response containing list of scorecards"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: Union[str, Any] = Field(default=None, alias="requestId")
    scorecards: Union[list[Scorecard], Any] = Field(default=None)

class TrackerLanguagekeywordsItem(BaseModel):
    """Nested schema for Tracker.languageKeywords_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    language: Union[str, Any] = Field(default=None, description="Language code")
    """Language code"""
    keywords: Union[list[str], Any] = Field(default=None, description="List of keywords for this language")
    """List of keywords for this language"""
    include_related_forms: Union[bool, Any] = Field(default=None, alias="includeRelatedForms", description="Whether to include related word forms")
    """Whether to include related word forms"""

class Tracker(BaseModel):
    """Keyword tracker configuration"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tracker_id: Union[str, Any] = Field(default=None, alias="trackerId")
    tracker_name: Union[str, Any] = Field(default=None, alias="trackerName")
    workspace_id: Union[str | None, Any] = Field(default=None, alias="workspaceId")
    language_keywords: Union[list[TrackerLanguagekeywordsItem], Any] = Field(default=None, alias="languageKeywords")
    affiliation: Union[str, Any] = Field(default=None)
    part_of_question: Union[bool, Any] = Field(default=None, alias="partOfQuestion")
    said_at: Union[str, Any] = Field(default=None, alias="saidAt")
    said_at_interval: Union[str | None, Any] = Field(default=None, alias="saidAtInterval")
    said_at_unit: Union[str | None, Any] = Field(default=None, alias="saidAtUnit")
    said_in_topics: Union[list[str], Any] = Field(default=None, alias="saidInTopics")
    filter_query: Union[str, Any] = Field(default=None, alias="filterQuery")
    created: Union[str, Any] = Field(default=None)
    creator_user_id: Union[str | None, Any] = Field(default=None, alias="creatorUserId")
    updated: Union[str, Any] = Field(default=None)
    updater_user_id: Union[str | None, Any] = Field(default=None, alias="updaterUserId")

class TrackersResponse(BaseModel):
    """Response containing list of trackers"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: Union[str, Any] = Field(default=None, alias="requestId")
    keyword_trackers: Union[list[Tracker], Any] = Field(default=None, alias="keywordTrackers")

class LibraryFolder(BaseModel):
    """Library folder structure"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    parent_folder_id: Union[str | None, Any] = Field(default=None, alias="parentFolderId")
    created_by: Union[str | None, Any] = Field(default=None, alias="createdBy")
    updated: Union[str, Any] = Field(default=None)

class LibraryFoldersResponse(BaseModel):
    """Response containing library folder structure"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: Union[str, Any] = Field(default=None, alias="requestId")
    folders: Union[list[LibraryFolder], Any] = Field(default=None)

class FolderCall(BaseModel):
    """Call within a library folder"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    call_id: Union[str, Any] = Field(default=None, alias="callId")
    title: Union[str, Any] = Field(default=None)
    started: Union[str, Any] = Field(default=None)
    duration: Union[int, Any] = Field(default=None)
    primary_user_id: Union[str, Any] = Field(default=None, alias="primaryUserId")
    url: Union[str, Any] = Field(default=None)

class FolderContentResponse(BaseModel):
    """Response containing calls in a folder"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: Union[str, Any] = Field(default=None, alias="requestId")
    id: Union[str, Any] = Field(default=None)
    name: Union[str, Any] = Field(default=None)
    created_by: Union[str | None, Any] = Field(default=None, alias="createdBy")
    updated: Union[str, Any] = Field(default=None)
    calls: Union[list[FolderCall], Any] = Field(default=None)
    records: Union[PaginationRecords, Any] = Field(default=None)

class CoachingMetrics(BaseModel):
    """Coaching metrics for a user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls_listened: Union[int, Any] = Field(default=None, alias="callsListened")
    calls_attended: Union[int, Any] = Field(default=None, alias="callsAttended")
    calls_with_feedback: Union[int, Any] = Field(default=None, alias="callsWithFeedback")
    calls_with_comments: Union[int, Any] = Field(default=None, alias="callsWithComments")
    scorecards_filled: Union[int, Any] = Field(default=None, alias="scorecardsFilled")

class CoachingData(BaseModel):
    """Coaching data for a user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user_id: Union[str, Any] = Field(default=None, alias="userId")
    user_email_address: Union[str, Any] = Field(default=None, alias="userEmailAddress")
    user_name: Union[str, Any] = Field(default=None, alias="userName")
    is_manager: Union[bool, Any] = Field(default=None, alias="isManager")
    coaching_metrics: Union[CoachingMetrics, Any] = Field(default=None, alias="coachingMetrics")

class CoachingResponse(BaseModel):
    """Response containing coaching metrics"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: Union[str, Any] = Field(default=None, alias="requestId")
    coaching_data: Union[list[CoachingData], Any] = Field(default=None, alias="coachingData")
    from_date_time: Union[str, Any] = Field(default=None, alias="fromDateTime")
    to_date_time: Union[str, Any] = Field(default=None, alias="toDateTime")

class AnsweredScorecardAnswer(BaseModel):
    """An answer to a scorecard question"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    question_id: Union[str, Any] = Field(default=None, alias="questionId")
    question_revision_id: Union[str, Any] = Field(default=None, alias="questionRevisionId")
    is_overall: Union[bool, Any] = Field(default=None, alias="isOverall")
    answer: Union[str, Any] = Field(default=None)
    answer_text: Union[str | None, Any] = Field(default=None, alias="answerText")
    score: Union[float, Any] = Field(default=None)
    not_applicable: Union[bool, Any] = Field(default=None, alias="notApplicable")
    selected_options: Union[list[str] | None, Any] = Field(default=None, alias="selectedOptions")

class AnsweredScorecard(BaseModel):
    """A completed scorecard"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    answered_scorecard_id: Union[str, Any] = Field(default=None, alias="answeredScorecardId")
    scorecard_id: Union[str, Any] = Field(default=None, alias="scorecardId")
    scorecard_name: Union[str, Any] = Field(default=None, alias="scorecardName")
    call_id: Union[str, Any] = Field(default=None, alias="callId")
    call_start_time: Union[str, Any] = Field(default=None, alias="callStartTime")
    reviewed_user_id: Union[str, Any] = Field(default=None, alias="reviewedUserId")
    reviewer_user_id: Union[str, Any] = Field(default=None, alias="reviewerUserId")
    review_method: Union[str, Any] = Field(default=None, alias="reviewMethod")
    editor_user_id: Union[str | None, Any] = Field(default=None, alias="editorUserId")
    answered_date_time: Union[str, Any] = Field(default=None, alias="answeredDateTime")
    review_time: Union[str, Any] = Field(default=None, alias="reviewTime")
    visibility_type: Union[str, Any] = Field(default=None, alias="visibilityType")
    answers: Union[list[AnsweredScorecardAnswer], Any] = Field(default=None)
    overall_score: Union[float, Any] = Field(default=None, alias="overallScore")
    visibility: Union[str, Any] = Field(default=None)

class AnsweredScorecardsResponse(BaseModel):
    """Response containing answered scorecards"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    request_id: Union[str, Any] = Field(default=None, alias="requestId")
    answered_scorecards: Union[list[AnsweredScorecard], Any] = Field(default=None, alias="answeredScorecards")
    records: Union[PaginationRecords, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class UsersListResultMeta(BaseModel):
    """Metadata for users.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationRecords, Any] = Field(default=None)

class CallsListResultMeta(BaseModel):
    """Metadata for calls.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationRecords, Any] = Field(default=None)

class CallsExtensiveListResultMeta(BaseModel):
    """Metadata for calls_extensive.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationRecords, Any] = Field(default=None)

class CallTranscriptsListResultMeta(BaseModel):
    """Metadata for call_transcripts.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationRecords, Any] = Field(default=None)

class StatsActivityAggregateListResultMeta(BaseModel):
    """Metadata for stats_activity_aggregate.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationRecords, Any] = Field(default=None)

class StatsActivityDayByDayListResultMeta(BaseModel):
    """Metadata for stats_activity_day_by_day.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationRecords, Any] = Field(default=None)

class StatsInteractionListResultMeta(BaseModel):
    """Metadata for stats_interaction.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationRecords, Any] = Field(default=None)

class LibraryFolderContentListResultMeta(BaseModel):
    """Metadata for library_folder_content.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationRecords, Any] = Field(default=None)

class StatsActivityScorecardsListResultMeta(BaseModel):
    """Metadata for stats_activity_scorecards.list operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationRecords, Any] = Field(default=None)

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


# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

UsersListResult = GongExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

UsersGetResult = GongExecuteResult[User]
"""Result type for users.get operation."""

CallsListResult = GongExecuteResultWithMeta[list[Call], CallsListResultMeta]
"""Result type for calls.list operation with data and metadata."""

CallsGetResult = GongExecuteResult[Call]
"""Result type for calls.get operation."""

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

