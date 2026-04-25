"""
Pydantic models for twilio connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Any

# Authentication configuration

class TwilioAuthConfig(BaseModel):
    """Twilio Authentication"""

    model_config = ConfigDict(extra="forbid")

    account_sid: str
    """Your Twilio Account SID (starts with AC)"""
    auth_token: str
    """Your Twilio Auth Token"""

# Replication configuration

class TwilioReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Twilio."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date and time in the format YYYY-MM-DDTHH:mm:ssZ. Any data before this date will not be replicated.
"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class Account(BaseModel):
    """A Twilio account"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    auth_token: str | None = Field(default=None)
    date_created: str | None = Field(default=None)
    date_updated: str | None = Field(default=None)
    friendly_name: str | None = Field(default=None)
    owner_account_sid: str | None = Field(default=None)
    sid: str | None
    status: str | None = Field(default=None)
    subresource_uris: dict[str, Any] | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    uri: str | None = Field(default=None)

class AccountsList(BaseModel):
    """Paginated list of accounts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    accounts: list[Account] | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    next_page_uri: str | None = Field(default=None)
    previous_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)
    uri: str | None = Field(default=None)

class Call(BaseModel):
    """A Twilio call"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    sid: str | None
    date_created: str | None = Field(default=None)
    date_updated: str | None = Field(default=None)
    parent_call_sid: str | None = Field(default=None)
    account_sid: str | None = Field(default=None)
    to: str | None = Field(default=None)
    to_formatted: str | None = Field(default=None)
    from_: str | None = Field(default=None, alias="from")
    from_formatted: str | None = Field(default=None)
    phone_number_sid: str | None = Field(default=None)
    status: str | None = Field(default=None)
    start_time: str | None = Field(default=None)
    end_time: str | None = Field(default=None)
    duration: str | None = Field(default=None)
    price: str | None = Field(default=None)
    price_unit: str | None = Field(default=None)
    direction: str | None = Field(default=None)
    answered_by: str | None = Field(default=None)
    annotation: str | None = Field(default=None)
    api_version: str | None = Field(default=None)
    forwarded_from: str | None = Field(default=None)
    group_sid: str | None = Field(default=None)
    caller_name: str | None = Field(default=None)
    queue_time: str | None = Field(default=None)
    trunk_sid: str | None = Field(default=None)
    uri: str | None = Field(default=None)
    subresource_uris: dict[str, Any] | None = Field(default=None)

class CallsList(BaseModel):
    """Paginated list of calls"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls: list[Call] | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    next_page_uri: str | None = Field(default=None)
    previous_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)
    uri: str | None = Field(default=None)

class Message(BaseModel):
    """A Twilio message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: str | None = Field(default=None)
    api_version: str | None = Field(default=None)
    body: str | None = Field(default=None)
    date_created: str | None = Field(default=None)
    date_sent: str | None = Field(default=None)
    date_updated: str | None = Field(default=None)
    direction: str | None = Field(default=None)
    error_code: str | None = Field(default=None)
    error_message: str | None = Field(default=None)
    from_: str | None = Field(default=None, alias="from")
    messaging_service_sid: str | None = Field(default=None)
    num_media: str | None = Field(default=None)
    num_segments: str | None = Field(default=None)
    price: str | None = Field(default=None)
    price_unit: str | None = Field(default=None)
    sid: str | None
    status: str | None = Field(default=None)
    subresource_uris: dict[str, Any] | None = Field(default=None)
    to: str | None = Field(default=None)
    uri: str | None = Field(default=None)

class MessagesList(BaseModel):
    """Paginated list of messages"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    messages: list[Message] | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    next_page_uri: str | None = Field(default=None)
    previous_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)
    uri: str | None = Field(default=None)

class IncomingPhoneNumberCapabilities(BaseModel):
    """Capabilities of this phone number"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    voice: bool | None | None = Field(default=None)
    sms: bool | None | None = Field(default=None)
    mms: bool | None | None = Field(default=None)
    fax: bool | None | None = Field(default=None)

class IncomingPhoneNumber(BaseModel):
    """A Twilio incoming phone number"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    sid: str | None
    account_sid: str | None = Field(default=None)
    friendly_name: str | None = Field(default=None)
    phone_number: str | None = Field(default=None)
    voice_url: str | None = Field(default=None)
    voice_method: str | None = Field(default=None)
    voice_fallback_url: str | None = Field(default=None)
    voice_fallback_method: str | None = Field(default=None)
    voice_caller_id_lookup: bool | None = Field(default=None)
    date_created: str | None = Field(default=None)
    date_updated: str | None = Field(default=None)
    sms_url: str | None = Field(default=None)
    sms_method: str | None = Field(default=None)
    sms_fallback_url: str | None = Field(default=None)
    sms_fallback_method: str | None = Field(default=None)
    address_requirements: str | None = Field(default=None)
    beta: bool | None = Field(default=None)
    capabilities: IncomingPhoneNumberCapabilities | None = Field(default=None)
    voice_receive_mode: str | None = Field(default=None)
    status_callback: str | None = Field(default=None)
    status_callback_method: str | None = Field(default=None)
    api_version: str | None = Field(default=None)
    voice_application_sid: str | None = Field(default=None)
    sms_application_sid: str | None = Field(default=None)
    origin: str | None = Field(default=None)
    trunk_sid: str | None = Field(default=None)
    emergency_status: str | None = Field(default=None)
    emergency_address_sid: str | None = Field(default=None)
    emergency_address_status: str | None = Field(default=None)
    address_sid: str | None = Field(default=None)
    identity_sid: str | None = Field(default=None)
    bundle_sid: str | None = Field(default=None)
    uri: str | None = Field(default=None)
    status: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    subresource_uris: dict[str, Any] | None = Field(default=None)

class IncomingPhoneNumbersList(BaseModel):
    """Paginated list of incoming phone numbers"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    incoming_phone_numbers: list[IncomingPhoneNumber] | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    next_page_uri: str | None = Field(default=None)
    previous_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)
    uri: str | None = Field(default=None)

class Recording(BaseModel):
    """A Twilio recording"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: str | None = Field(default=None)
    api_version: str | None = Field(default=None)
    call_sid: str | None = Field(default=None)
    conference_sid: str | None = Field(default=None)
    date_created: str | None = Field(default=None)
    date_updated: str | None = Field(default=None)
    start_time: str | None = Field(default=None)
    duration: str | None = Field(default=None)
    sid: str | None
    price: str | None = Field(default=None)
    price_unit: str | None = Field(default=None)
    status: str | None = Field(default=None)
    channels: int | None = Field(default=None)
    source: str | None = Field(default=None)
    error_code: str | None = Field(default=None)
    media_url: str | None = Field(default=None)
    uri: str | None = Field(default=None)
    encryption_details: dict[str, Any] | None = Field(default=None)
    subresource_uris: dict[str, Any] | None = Field(default=None)

class RecordingsList(BaseModel):
    """Paginated list of recordings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    recordings: list[Recording] | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    next_page_uri: str | None = Field(default=None)
    previous_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)
    uri: str | None = Field(default=None)

class Conference(BaseModel):
    """A Twilio conference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: str | None = Field(default=None)
    date_created: str | None = Field(default=None)
    date_updated: str | None = Field(default=None)
    api_version: str | None = Field(default=None)
    friendly_name: str | None = Field(default=None)
    region: str | None = Field(default=None)
    sid: str | None
    status: str | None = Field(default=None)
    uri: str | None = Field(default=None)
    reason_conference_ended: str | None = Field(default=None)
    call_sid_ending_conference: str | None = Field(default=None)
    subresource_uris: dict[str, Any] | None = Field(default=None)

class ConferencesList(BaseModel):
    """Paginated list of conferences"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    conferences: list[Conference] | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    next_page_uri: str | None = Field(default=None)
    previous_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)
    uri: str | None = Field(default=None)

class UsageRecord(BaseModel):
    """A Twilio usage record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: str | None = Field(default=None)
    api_version: str | None = Field(default=None)
    as_of: str | None = Field(default=None)
    category: str | None = Field(default=None)
    count: str | None = Field(default=None)
    count_unit: str | None = Field(default=None)
    description: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    price: str | None = Field(default=None)
    price_unit: str | None = Field(default=None)
    start_date: str | None = Field(default=None)
    subresource_uris: dict[str, Any] | None = Field(default=None)
    usage: str | None = Field(default=None)
    usage_unit: str | None = Field(default=None)
    uri: str | None = Field(default=None)

class UsageRecordsList(BaseModel):
    """Paginated list of usage records"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    usage_records: list[UsageRecord] | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    next_page_uri: str | None = Field(default=None)
    previous_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)
    uri: str | None = Field(default=None)

class Address(BaseModel):
    """A Twilio address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: str | None = Field(default=None)
    city: str | None = Field(default=None)
    customer_name: str | None = Field(default=None)
    date_created: str | None = Field(default=None)
    date_updated: str | None = Field(default=None)
    emergency_enabled: bool | None = Field(default=None)
    friendly_name: str | None = Field(default=None)
    iso_country: str | None = Field(default=None)
    postal_code: str | None = Field(default=None)
    region: str | None = Field(default=None)
    sid: str | None
    street: str | None = Field(default=None)
    street_secondary: str | None = Field(default=None)
    validated: bool | None = Field(default=None)
    verified: bool | None = Field(default=None)
    uri: str | None = Field(default=None)

class AddressesList(BaseModel):
    """Paginated list of addresses"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    addresses: list[Address] | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    next_page_uri: str | None = Field(default=None)
    previous_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)
    uri: str | None = Field(default=None)

class Queue(BaseModel):
    """A Twilio queue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: str | None = Field(default=None)
    average_wait_time: int | None = Field(default=None)
    current_size: int | None = Field(default=None)
    date_created: str | None = Field(default=None)
    date_updated: str | None = Field(default=None)
    friendly_name: str | None = Field(default=None)
    max_size: int | None = Field(default=None)
    sid: str | None
    uri: str | None = Field(default=None)
    subresource_uris: dict[str, Any] | None = Field(default=None)

class QueuesList(BaseModel):
    """Paginated list of queues"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    queues: list[Queue] | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    next_page_uri: str | None = Field(default=None)
    previous_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)
    uri: str | None = Field(default=None)

class Transcription(BaseModel):
    """A Twilio transcription"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: str | None = Field(default=None)
    api_version: str | None = Field(default=None)
    date_created: str | None = Field(default=None)
    date_updated: str | None = Field(default=None)
    duration: str | None = Field(default=None)
    price: str | None = Field(default=None)
    price_unit: str | None = Field(default=None)
    recording_sid: str | None = Field(default=None)
    sid: str | None
    status: str | None = Field(default=None)
    transcription_text: str | None = Field(default=None)
    type_: str | None = Field(default=None, alias="type")
    uri: str | None = Field(default=None)

class TranscriptionsList(BaseModel):
    """Paginated list of transcriptions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transcriptions: list[Transcription] | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    next_page_uri: str | None = Field(default=None)
    previous_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)
    uri: str | None = Field(default=None)

class OutgoingCallerId(BaseModel):
    """A Twilio outgoing caller ID"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: str | None = Field(default=None)
    date_created: str | None = Field(default=None)
    date_updated: str | None = Field(default=None)
    friendly_name: str | None = Field(default=None)
    phone_number: str | None = Field(default=None)
    sid: str | None
    uri: str | None = Field(default=None)

class OutgoingCallerIdsList(BaseModel):
    """Paginated list of outgoing caller IDs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    outgoing_caller_ids: list[OutgoingCallerId] | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    next_page_uri: str | None = Field(default=None)
    previous_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)
    uri: str | None = Field(default=None)

class MessageCreateParams(BaseModel):
    """Parameters for sending a new SMS/MMS/WhatsApp message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    to: str | None = Field(default=None, alias="To")
    from_: str | None = Field(default=None, alias="From")
    messaging_service_sid: str | None = Field(default=None, alias="MessagingServiceSid")
    body: str | None = Field(default=None, alias="Body")
    media_url: list[str] | None = Field(default=None, alias="MediaUrl")
    status_callback: str | None = Field(default=None, alias="StatusCallback")
    validity_period: int | None = Field(default=None, alias="ValidityPeriod")

class CallCreateParams(BaseModel):
    """Parameters for placing an outbound call"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    to: str | None = Field(default=None, alias="To")
    from_: str | None = Field(default=None, alias="From")
    url: str | None = Field(default=None, alias="Url")
    twiml: str | None = Field(default=None, alias="Twiml")
    application_sid: str | None = Field(default=None, alias="ApplicationSid")
    method: str | None = Field(default=None, alias="Method")
    status_callback: str | None = Field(default=None, alias="StatusCallback")
    status_callback_method: str | None = Field(default=None, alias="StatusCallbackMethod")
    timeout: int | None = Field(default=None, alias="Timeout")
    record: bool | None = Field(default=None, alias="Record")
    machine_detection: str | None = Field(default=None, alias="MachineDetection")
    send_digits: str | None = Field(default=None, alias="SendDigits")

class IncomingPhoneNumberCreateParams(BaseModel):
    """Parameters for provisioning a new phone number"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    phone_number: str | None = Field(default=None, alias="PhoneNumber")
    area_code: str | None = Field(default=None, alias="AreaCode")
    friendly_name: str | None = Field(default=None, alias="FriendlyName")
    voice_url: str | None = Field(default=None, alias="VoiceUrl")
    voice_method: str | None = Field(default=None, alias="VoiceMethod")
    sms_url: str | None = Field(default=None, alias="SmsUrl")
    sms_method: str | None = Field(default=None, alias="SmsMethod")
    status_callback: str | None = Field(default=None, alias="StatusCallback")
    voice_application_sid: str | None = Field(default=None, alias="VoiceApplicationSid")
    sms_application_sid: str | None = Field(default=None, alias="SmsApplicationSid")

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class AccountsListResultMeta(BaseModel):
    """Metadata for accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: str | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)

class CallsListResultMeta(BaseModel):
    """Metadata for calls.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: str | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)

class MessagesListResultMeta(BaseModel):
    """Metadata for messages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: str | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)

class IncomingPhoneNumbersListResultMeta(BaseModel):
    """Metadata for incoming_phone_numbers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: str | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)

class RecordingsListResultMeta(BaseModel):
    """Metadata for recordings.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: str | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)

class ConferencesListResultMeta(BaseModel):
    """Metadata for conferences.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: str | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)

class UsageRecordsListResultMeta(BaseModel):
    """Metadata for usage_records.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: str | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)

class AddressesListResultMeta(BaseModel):
    """Metadata for addresses.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: str | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)

class QueuesListResultMeta(BaseModel):
    """Metadata for queues.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: str | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)

class TranscriptionsListResultMeta(BaseModel):
    """Metadata for transcriptions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: str | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)

class OutgoingCallerIdsListResultMeta(BaseModel):
    """Metadata for outgoing_caller_ids.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: str | None = Field(default=None)
    first_page_uri: str | None = Field(default=None)
    page: int | None = Field(default=None)
    page_size: int | None = Field(default=None)

# ===== CHECK RESULT MODEL =====

class TwilioCheckResult(BaseModel):
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


class TwilioExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class TwilioExecuteResultWithMeta(TwilioExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AccountsSearchData(BaseModel):
    """Search result data for accounts entity."""
    model_config = ConfigDict(extra="allow")

    sid: str | None = None
    """The unique identifier for the account"""
    friendly_name: str | None = None
    """A user-defined friendly name for the account"""
    status: str | None = None
    """The current status of the account"""
    type_: str | None = None
    """The type of the account"""
    owner_account_sid: str | None = None
    """The SID of the owner account"""
    date_created: str | None = None
    """The timestamp when the account was created"""
    date_updated: str | None = None
    """The timestamp when the account was last updated"""
    uri: str | None = None
    """The URI for accessing the account resource"""


class CallsSearchData(BaseModel):
    """Search result data for calls entity."""
    model_config = ConfigDict(extra="allow")

    sid: str | None = None
    """The unique identifier for the call"""
    account_sid: str | None = None
    """The unique identifier for the account associated with the call"""
    to: str | None = None
    """The phone number that received the call"""
    from_: str | None = None
    """The phone number that made the call"""
    status: str | None = None
    """The current status of the call"""
    direction: str | None = None
    """The direction of the call (inbound or outbound)"""
    duration: str | None = None
    """The duration of the call in seconds"""
    price: str | None = None
    """The cost of the call"""
    price_unit: str | None = None
    """The currency unit of the call cost"""
    start_time: str | None = None
    """The date and time when the call started"""
    end_time: str | None = None
    """The date and time when the call ended"""
    date_created: str | None = None
    """The date and time when the call record was created"""
    date_updated: str | None = None
    """The date and time when the call record was last updated"""


class MessagesSearchData(BaseModel):
    """Search result data for messages entity."""
    model_config = ConfigDict(extra="allow")

    sid: str | None = None
    """The unique identifier for this message"""
    account_sid: str | None = None
    """The unique identifier for the account associated with this message"""
    to: str | None = None
    """The phone number or recipient ID the message was sent to"""
    from_: str | None = None
    """The phone number or sender ID that sent the message"""
    body: str | None = None
    """The text body of the message"""
    status: str | None = None
    """The status of the message"""
    direction: str | None = None
    """The direction of the message"""
    price: str | None = None
    """The cost of the message"""
    price_unit: str | None = None
    """The currency unit used for pricing"""
    date_created: str | None = None
    """The date and time when the message was created"""
    date_sent: str | None = None
    """The date and time when the message was sent"""
    error_code: str | None = None
    """The error code associated with the message if any"""
    error_message: str | None = None
    """The error message description if the message failed"""
    num_segments: str | None = None
    """The number of message segments"""
    num_media: str | None = None
    """The number of media files included in the message"""


class IncomingPhoneNumbersSearchData(BaseModel):
    """Search result data for incoming_phone_numbers entity."""
    model_config = ConfigDict(extra="allow")

    sid: str | None = None
    """The SID of this phone number"""
    account_sid: str | None = None
    """The SID of the account that owns this phone number"""
    phone_number: str | None = None
    """The phone number in E.164 format"""
    friendly_name: str | None = None
    """A user-assigned friendly name for this phone number"""
    status: str | None = None
    """Status of the phone number"""
    capabilities: dict[str, Any] | None = None
    """Capabilities of this phone number"""
    date_created: str | None = None
    """When the phone number was created"""
    date_updated: str | None = None
    """When the phone number was last updated"""


class RecordingsSearchData(BaseModel):
    """Search result data for recordings entity."""
    model_config = ConfigDict(extra="allow")

    sid: str | None = None
    """The unique identifier of the recording"""
    account_sid: str | None = None
    """The account SID that owns the recording"""
    call_sid: str | None = None
    """The SID of the associated call"""
    duration: str | None = None
    """Duration in seconds"""
    status: str | None = None
    """The status of the recording"""
    channels: int | None = None
    """Number of audio channels"""
    price: str | None = None
    """The cost of storing the recording"""
    price_unit: str | None = None
    """The currency unit"""
    date_created: str | None = None
    """When the recording was created"""
    start_time: str | None = None
    """When the recording started"""


class ConferencesSearchData(BaseModel):
    """Search result data for conferences entity."""
    model_config = ConfigDict(extra="allow")

    sid: str | None = None
    """The unique identifier of the conference"""
    account_sid: str | None = None
    """The account SID associated with the conference"""
    friendly_name: str | None = None
    """A friendly name for the conference"""
    status: str | None = None
    """The current status of the conference"""
    region: str | None = None
    """The region where the conference is hosted"""
    date_created: str | None = None
    """When the conference was created"""
    date_updated: str | None = None
    """When the conference was last updated"""


class UsageRecordsSearchData(BaseModel):
    """Search result data for usage_records entity."""
    model_config = ConfigDict(extra="allow")

    account_sid: str | None = None
    """The account SID associated with this usage record"""
    category: str | None = None
    """The usage category (calls, SMS, recordings, etc.)"""
    description: str | None = None
    """A description of the usage record"""
    usage: str | None = None
    """The total usage value"""
    usage_unit: str | None = None
    """The unit of measurement for usage"""
    count: str | None = None
    """The number of units consumed"""
    count_unit: str | None = None
    """The unit of measurement for count"""
    price: str | None = None
    """The total price for consumed units"""
    price_unit: str | None = None
    """The currency unit"""
    start_date: str | None = None
    """The start date of the usage period"""
    end_date: str | None = None
    """The end date of the usage period"""


class AddressesSearchData(BaseModel):
    """Search result data for addresses entity."""
    model_config = ConfigDict(extra="allow")

    sid: str | None = None
    """The unique identifier of the address"""
    account_sid: str | None = None
    """The account SID associated with this address"""
    customer_name: str | None = None
    """The customer name associated with this address"""
    friendly_name: str | None = None
    """A friendly name for the address"""
    street: str | None = None
    """The street address"""
    city: str | None = None
    """The city of the address"""
    region: str | None = None
    """The region or state"""
    postal_code: str | None = None
    """The postal code"""
    iso_country: str | None = None
    """The ISO 3166-1 alpha-2 country code"""
    validated: bool | None = None
    """Whether the address has been validated"""
    verified: bool | None = None
    """Whether the address has been verified"""


class QueuesSearchData(BaseModel):
    """Search result data for queues entity."""
    model_config = ConfigDict(extra="allow")

    sid: str | None = None
    """The unique identifier for the queue"""
    account_sid: str | None = None
    """The account SID that owns this queue"""
    friendly_name: str | None = None
    """A friendly name for the queue"""
    current_size: int | None = None
    """Current number of callers waiting"""
    max_size: int | None = None
    """Maximum number of callers allowed"""
    average_wait_time: int | None = None
    """Average wait time in seconds"""
    date_created: str | None = None
    """When the queue was created"""
    date_updated: str | None = None
    """When the queue was last updated"""


class TranscriptionsSearchData(BaseModel):
    """Search result data for transcriptions entity."""
    model_config = ConfigDict(extra="allow")

    sid: str | None = None
    """The unique identifier for the transcription"""
    account_sid: str | None = None
    """The account SID"""
    recording_sid: str | None = None
    """The SID of the associated recording"""
    status: str | None = None
    """The status of the transcription"""
    duration: str | None = None
    """Duration of the audio recording in seconds"""
    price: str | None = None
    """The cost of the transcription"""
    price_unit: str | None = None
    """The currency unit"""
    date_created: str | None = None
    """When the transcription was created"""
    date_updated: str | None = None
    """When the transcription was last updated"""


class OutgoingCallerIdsSearchData(BaseModel):
    """Search result data for outgoing_caller_ids entity."""
    model_config = ConfigDict(extra="allow")

    sid: str | None = None
    """The unique identifier"""
    account_sid: str | None = None
    """The account SID"""
    phone_number: str | None = None
    """The phone number"""
    friendly_name: str | None = None
    """A friendly name"""
    date_created: str | None = None
    """When the outgoing caller ID was created"""
    date_updated: str | None = None
    """When the outgoing caller ID was last updated"""


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

AccountsSearchResult = AirbyteSearchResult[AccountsSearchData]
"""Search result type for accounts entity."""

CallsSearchResult = AirbyteSearchResult[CallsSearchData]
"""Search result type for calls entity."""

MessagesSearchResult = AirbyteSearchResult[MessagesSearchData]
"""Search result type for messages entity."""

IncomingPhoneNumbersSearchResult = AirbyteSearchResult[IncomingPhoneNumbersSearchData]
"""Search result type for incoming_phone_numbers entity."""

RecordingsSearchResult = AirbyteSearchResult[RecordingsSearchData]
"""Search result type for recordings entity."""

ConferencesSearchResult = AirbyteSearchResult[ConferencesSearchData]
"""Search result type for conferences entity."""

UsageRecordsSearchResult = AirbyteSearchResult[UsageRecordsSearchData]
"""Search result type for usage_records entity."""

AddressesSearchResult = AirbyteSearchResult[AddressesSearchData]
"""Search result type for addresses entity."""

QueuesSearchResult = AirbyteSearchResult[QueuesSearchData]
"""Search result type for queues entity."""

TranscriptionsSearchResult = AirbyteSearchResult[TranscriptionsSearchData]
"""Search result type for transcriptions entity."""

OutgoingCallerIdsSearchResult = AirbyteSearchResult[OutgoingCallerIdsSearchData]
"""Search result type for outgoing_caller_ids entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

AccountsListResult = TwilioExecuteResultWithMeta[list[Account], AccountsListResultMeta]
"""Result type for accounts.list operation with data and metadata."""

CallsListResult = TwilioExecuteResultWithMeta[list[Call], CallsListResultMeta]
"""Result type for calls.list operation with data and metadata."""

MessagesListResult = TwilioExecuteResultWithMeta[list[Message], MessagesListResultMeta]
"""Result type for messages.list operation with data and metadata."""

IncomingPhoneNumbersListResult = TwilioExecuteResultWithMeta[list[IncomingPhoneNumber], IncomingPhoneNumbersListResultMeta]
"""Result type for incoming_phone_numbers.list operation with data and metadata."""

RecordingsListResult = TwilioExecuteResultWithMeta[list[Recording], RecordingsListResultMeta]
"""Result type for recordings.list operation with data and metadata."""

ConferencesListResult = TwilioExecuteResultWithMeta[list[Conference], ConferencesListResultMeta]
"""Result type for conferences.list operation with data and metadata."""

UsageRecordsListResult = TwilioExecuteResultWithMeta[list[UsageRecord], UsageRecordsListResultMeta]
"""Result type for usage_records.list operation with data and metadata."""

AddressesListResult = TwilioExecuteResultWithMeta[list[Address], AddressesListResultMeta]
"""Result type for addresses.list operation with data and metadata."""

QueuesListResult = TwilioExecuteResultWithMeta[list[Queue], QueuesListResultMeta]
"""Result type for queues.list operation with data and metadata."""

TranscriptionsListResult = TwilioExecuteResultWithMeta[list[Transcription], TranscriptionsListResultMeta]
"""Result type for transcriptions.list operation with data and metadata."""

OutgoingCallerIdsListResult = TwilioExecuteResultWithMeta[list[OutgoingCallerId], OutgoingCallerIdsListResultMeta]
"""Result type for outgoing_caller_ids.list operation with data and metadata."""

