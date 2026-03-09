"""
Pydantic models for twilio connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

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

    auth_token: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_updated: Union[str | None, Any] = Field(default=None)
    friendly_name: Union[str | None, Any] = Field(default=None)
    owner_account_sid: Union[str | None, Any] = Field(default=None)
    sid: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    subresource_uris: Union[dict[str, Any] | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    uri: Union[str | None, Any] = Field(default=None)

class AccountsList(BaseModel):
    """Paginated list of accounts"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    accounts: Union[list[Account], Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    next_page_uri: Union[str | None, Any] = Field(default=None)
    previous_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class Call(BaseModel):
    """A Twilio call"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    sid: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_updated: Union[str | None, Any] = Field(default=None)
    parent_call_sid: Union[str | None, Any] = Field(default=None)
    account_sid: Union[str | None, Any] = Field(default=None)
    to: Union[str | None, Any] = Field(default=None)
    to_formatted: Union[str | None, Any] = Field(default=None)
    from_: Union[str | None, Any] = Field(default=None, alias="from")
    from_formatted: Union[str | None, Any] = Field(default=None)
    phone_number_sid: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    start_time: Union[str | None, Any] = Field(default=None)
    end_time: Union[str | None, Any] = Field(default=None)
    duration: Union[str | None, Any] = Field(default=None)
    price: Union[str | None, Any] = Field(default=None)
    price_unit: Union[str | None, Any] = Field(default=None)
    direction: Union[str | None, Any] = Field(default=None)
    answered_by: Union[str | None, Any] = Field(default=None)
    annotation: Union[str | None, Any] = Field(default=None)
    api_version: Union[str | None, Any] = Field(default=None)
    forwarded_from: Union[str | None, Any] = Field(default=None)
    group_sid: Union[str | None, Any] = Field(default=None)
    caller_name: Union[str | None, Any] = Field(default=None)
    queue_time: Union[str | None, Any] = Field(default=None)
    trunk_sid: Union[str | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)
    subresource_uris: Union[dict[str, Any] | None, Any] = Field(default=None)

class CallsList(BaseModel):
    """Paginated list of calls"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls: Union[list[Call], Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    next_page_uri: Union[str | None, Any] = Field(default=None)
    previous_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class Message(BaseModel):
    """A Twilio message"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: Union[str | None, Any] = Field(default=None)
    api_version: Union[str | None, Any] = Field(default=None)
    body: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_sent: Union[str | None, Any] = Field(default=None)
    date_updated: Union[str | None, Any] = Field(default=None)
    direction: Union[str | None, Any] = Field(default=None)
    error_code: Union[str | None, Any] = Field(default=None)
    error_message: Union[str | None, Any] = Field(default=None)
    from_: Union[str | None, Any] = Field(default=None, alias="from")
    messaging_service_sid: Union[str | None, Any] = Field(default=None)
    num_media: Union[str | None, Any] = Field(default=None)
    num_segments: Union[str | None, Any] = Field(default=None)
    price: Union[str | None, Any] = Field(default=None)
    price_unit: Union[str | None, Any] = Field(default=None)
    sid: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    subresource_uris: Union[dict[str, Any] | None, Any] = Field(default=None)
    to: Union[str | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class MessagesList(BaseModel):
    """Paginated list of messages"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    messages: Union[list[Message], Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    next_page_uri: Union[str | None, Any] = Field(default=None)
    previous_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class IncomingPhoneNumberCapabilities(BaseModel):
    """Capabilities of this phone number"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    voice: Union[bool | None, Any] = Field(default=None)
    sms: Union[bool | None, Any] = Field(default=None)
    mms: Union[bool | None, Any] = Field(default=None)
    fax: Union[bool | None, Any] = Field(default=None)

class IncomingPhoneNumber(BaseModel):
    """A Twilio incoming phone number"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    sid: Union[str | None, Any] = Field(default=None)
    account_sid: Union[str | None, Any] = Field(default=None)
    friendly_name: Union[str | None, Any] = Field(default=None)
    phone_number: Union[str | None, Any] = Field(default=None)
    voice_url: Union[str | None, Any] = Field(default=None)
    voice_method: Union[str | None, Any] = Field(default=None)
    voice_fallback_url: Union[str | None, Any] = Field(default=None)
    voice_fallback_method: Union[str | None, Any] = Field(default=None)
    voice_caller_id_lookup: Union[bool | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_updated: Union[str | None, Any] = Field(default=None)
    sms_url: Union[str | None, Any] = Field(default=None)
    sms_method: Union[str | None, Any] = Field(default=None)
    sms_fallback_url: Union[str | None, Any] = Field(default=None)
    sms_fallback_method: Union[str | None, Any] = Field(default=None)
    address_requirements: Union[str | None, Any] = Field(default=None)
    beta: Union[bool | None, Any] = Field(default=None)
    capabilities: Union[IncomingPhoneNumberCapabilities | None, Any] = Field(default=None)
    voice_receive_mode: Union[str | None, Any] = Field(default=None)
    status_callback: Union[str | None, Any] = Field(default=None)
    status_callback_method: Union[str | None, Any] = Field(default=None)
    api_version: Union[str | None, Any] = Field(default=None)
    voice_application_sid: Union[str | None, Any] = Field(default=None)
    sms_application_sid: Union[str | None, Any] = Field(default=None)
    origin: Union[str | None, Any] = Field(default=None)
    trunk_sid: Union[str | None, Any] = Field(default=None)
    emergency_status: Union[str | None, Any] = Field(default=None)
    emergency_address_sid: Union[str | None, Any] = Field(default=None)
    emergency_address_status: Union[str | None, Any] = Field(default=None)
    address_sid: Union[str | None, Any] = Field(default=None)
    identity_sid: Union[str | None, Any] = Field(default=None)
    bundle_sid: Union[str | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    subresource_uris: Union[dict[str, Any] | None, Any] = Field(default=None)

class IncomingPhoneNumbersList(BaseModel):
    """Paginated list of incoming phone numbers"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    incoming_phone_numbers: Union[list[IncomingPhoneNumber], Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    next_page_uri: Union[str | None, Any] = Field(default=None)
    previous_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class Recording(BaseModel):
    """A Twilio recording"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: Union[str | None, Any] = Field(default=None)
    api_version: Union[str | None, Any] = Field(default=None)
    call_sid: Union[str | None, Any] = Field(default=None)
    conference_sid: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_updated: Union[str | None, Any] = Field(default=None)
    start_time: Union[str | None, Any] = Field(default=None)
    duration: Union[str | None, Any] = Field(default=None)
    sid: Union[str | None, Any] = Field(default=None)
    price: Union[str | None, Any] = Field(default=None)
    price_unit: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    channels: Union[int | None, Any] = Field(default=None)
    source: Union[str | None, Any] = Field(default=None)
    error_code: Union[str | None, Any] = Field(default=None)
    media_url: Union[str | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)
    encryption_details: Union[dict[str, Any] | None, Any] = Field(default=None)
    subresource_uris: Union[dict[str, Any] | None, Any] = Field(default=None)

class RecordingsList(BaseModel):
    """Paginated list of recordings"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    recordings: Union[list[Recording], Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    next_page_uri: Union[str | None, Any] = Field(default=None)
    previous_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class Conference(BaseModel):
    """A Twilio conference"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_updated: Union[str | None, Any] = Field(default=None)
    api_version: Union[str | None, Any] = Field(default=None)
    friendly_name: Union[str | None, Any] = Field(default=None)
    region: Union[str | None, Any] = Field(default=None)
    sid: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)
    reason_conference_ended: Union[str | None, Any] = Field(default=None)
    call_sid_ending_conference: Union[str | None, Any] = Field(default=None)
    subresource_uris: Union[dict[str, Any] | None, Any] = Field(default=None)

class ConferencesList(BaseModel):
    """Paginated list of conferences"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    conferences: Union[list[Conference], Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    next_page_uri: Union[str | None, Any] = Field(default=None)
    previous_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class UsageRecord(BaseModel):
    """A Twilio usage record"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: Union[str | None, Any] = Field(default=None)
    api_version: Union[str | None, Any] = Field(default=None)
    as_of: Union[str | None, Any] = Field(default=None)
    category: Union[str | None, Any] = Field(default=None)
    count: Union[str | None, Any] = Field(default=None)
    count_unit: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    end_date: Union[str | None, Any] = Field(default=None)
    price: Union[str | None, Any] = Field(default=None)
    price_unit: Union[str | None, Any] = Field(default=None)
    start_date: Union[str | None, Any] = Field(default=None)
    subresource_uris: Union[dict[str, Any] | None, Any] = Field(default=None)
    usage: Union[str | None, Any] = Field(default=None)
    usage_unit: Union[str | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class UsageRecordsList(BaseModel):
    """Paginated list of usage records"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    usage_records: Union[list[UsageRecord], Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    next_page_uri: Union[str | None, Any] = Field(default=None)
    previous_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class Address(BaseModel):
    """A Twilio address"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: Union[str | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    customer_name: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_updated: Union[str | None, Any] = Field(default=None)
    emergency_enabled: Union[bool | None, Any] = Field(default=None)
    friendly_name: Union[str | None, Any] = Field(default=None)
    iso_country: Union[str | None, Any] = Field(default=None)
    postal_code: Union[str | None, Any] = Field(default=None)
    region: Union[str | None, Any] = Field(default=None)
    sid: Union[str | None, Any] = Field(default=None)
    street: Union[str | None, Any] = Field(default=None)
    street_secondary: Union[str | None, Any] = Field(default=None)
    validated: Union[bool | None, Any] = Field(default=None)
    verified: Union[bool | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class AddressesList(BaseModel):
    """Paginated list of addresses"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    addresses: Union[list[Address], Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    next_page_uri: Union[str | None, Any] = Field(default=None)
    previous_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class Queue(BaseModel):
    """A Twilio queue"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: Union[str | None, Any] = Field(default=None)
    average_wait_time: Union[int | None, Any] = Field(default=None)
    current_size: Union[int | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_updated: Union[str | None, Any] = Field(default=None)
    friendly_name: Union[str | None, Any] = Field(default=None)
    max_size: Union[int | None, Any] = Field(default=None)
    sid: Union[str | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)
    subresource_uris: Union[dict[str, Any] | None, Any] = Field(default=None)

class QueuesList(BaseModel):
    """Paginated list of queues"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    queues: Union[list[Queue], Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    next_page_uri: Union[str | None, Any] = Field(default=None)
    previous_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class Transcription(BaseModel):
    """A Twilio transcription"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: Union[str | None, Any] = Field(default=None)
    api_version: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_updated: Union[str | None, Any] = Field(default=None)
    duration: Union[str | None, Any] = Field(default=None)
    price: Union[str | None, Any] = Field(default=None)
    price_unit: Union[str | None, Any] = Field(default=None)
    recording_sid: Union[str | None, Any] = Field(default=None)
    sid: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    transcription_text: Union[str | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    uri: Union[str | None, Any] = Field(default=None)

class TranscriptionsList(BaseModel):
    """Paginated list of transcriptions"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    transcriptions: Union[list[Transcription], Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    next_page_uri: Union[str | None, Any] = Field(default=None)
    previous_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class OutgoingCallerId(BaseModel):
    """A Twilio outgoing caller ID"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_sid: Union[str | None, Any] = Field(default=None)
    date_created: Union[str | None, Any] = Field(default=None)
    date_updated: Union[str | None, Any] = Field(default=None)
    friendly_name: Union[str | None, Any] = Field(default=None)
    phone_number: Union[str | None, Any] = Field(default=None)
    sid: Union[str | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

class OutgoingCallerIdsList(BaseModel):
    """Paginated list of outgoing caller IDs"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    outgoing_caller_ids: Union[list[OutgoingCallerId], Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    next_page_uri: Union[str | None, Any] = Field(default=None)
    previous_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)
    uri: Union[str | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class AccountsListResultMeta(BaseModel):
    """Metadata for accounts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: Union[str | None, Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)

class CallsListResultMeta(BaseModel):
    """Metadata for calls.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: Union[str | None, Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)

class MessagesListResultMeta(BaseModel):
    """Metadata for messages.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: Union[str | None, Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)

class IncomingPhoneNumbersListResultMeta(BaseModel):
    """Metadata for incoming_phone_numbers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: Union[str | None, Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)

class RecordingsListResultMeta(BaseModel):
    """Metadata for recordings.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: Union[str | None, Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)

class ConferencesListResultMeta(BaseModel):
    """Metadata for conferences.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: Union[str | None, Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)

class UsageRecordsListResultMeta(BaseModel):
    """Metadata for usage_records.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: Union[str | None, Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)

class AddressesListResultMeta(BaseModel):
    """Metadata for addresses.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: Union[str | None, Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)

class QueuesListResultMeta(BaseModel):
    """Metadata for queues.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: Union[str | None, Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)

class TranscriptionsListResultMeta(BaseModel):
    """Metadata for transcriptions.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: Union[str | None, Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)

class OutgoingCallerIdsListResultMeta(BaseModel):
    """Metadata for outgoing_caller_ids.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page_uri: Union[str | None, Any] = Field(default=None)
    first_page_uri: Union[str | None, Any] = Field(default=None)
    page: Union[int | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)

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

