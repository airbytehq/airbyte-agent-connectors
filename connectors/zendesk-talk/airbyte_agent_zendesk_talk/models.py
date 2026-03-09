"""
Pydantic models for zendesk-talk connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any
from typing import Optional

# Authentication configuration - multiple options available

class ZendeskTalkOauth20AuthConfig(BaseModel):
    """OAuth 2.0 - Zendesk OAuth 2.0 authentication"""

    model_config = ConfigDict(extra="forbid")

    access_token: str
    """OAuth 2.0 access token"""
    refresh_token: Optional[str] = None
    """OAuth 2.0 refresh token (optional)"""
    client_id: Optional[str] = None
    """OAuth client ID"""
    client_secret: Optional[str] = None
    """OAuth client secret"""

class ZendeskTalkApiTokenAuthConfig(BaseModel):
    """API Token - Authenticate using email and API token"""

    model_config = ConfigDict(extra="forbid")

    email: str
    """Your Zendesk account email address"""
    api_token: str
    """Your Zendesk API token from Admin Center"""

ZendeskTalkAuthConfig = ZendeskTalkOauth20AuthConfig | ZendeskTalkApiTokenAuthConfig

# Replication configuration

class ZendeskTalkReplicationConfig(BaseModel):
    """Replication Configuration - Settings for data replication from Zendesk Talk."""

    model_config = ConfigDict(extra="forbid")

    start_date: str
    """UTC date and time in the format YYYY-MM-DDT00:00:00Z from which to start replicating data."""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class PhoneNumberCapabilities(BaseModel):
    """Phone number capabilities (sms, mms, voice)"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    sms: Union[bool | None, Any] = Field(default=None)
    mms: Union[bool | None, Any] = Field(default=None)
    voice: Union[bool | None, Any] = Field(default=None)
    emergency_address: Union[bool | None, Any] = Field(default=None)

class PhoneNumber(BaseModel):
    """PhoneNumber type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    brand_id: Union[int | None, Any] = Field(default=None)
    call_recording_consent: Union[str | None, Any] = Field(default=None)
    capabilities: Union[PhoneNumberCapabilities | None, Any] = Field(default=None)
    categorised_greetings: Union[dict[str, Any] | None, Any] = Field(default=None)
    categorised_greetings_with_sub_settings: Union[dict[str, Any] | None, Any] = Field(default=None)
    country_code: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    default_greeting_ids: Union[list[str] | None, Any] = Field(default=None)
    default_group_id: Union[int | None, Any] = Field(default=None)
    display_number: Union[str | None, Any] = Field(default=None)
    external: Union[bool | None, Any] = Field(default=None)
    failover_number: Union[str | None, Any] = Field(default=None)
    greeting_ids: Union[list[int] | None, Any] = Field(default=None)
    group_ids: Union[list[int] | None, Any] = Field(default=None)
    ivr_id: Union[int | None, Any] = Field(default=None)
    line_type: Union[str | None, Any] = Field(default=None)
    location: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    nickname: Union[str | None, Any] = Field(default=None)
    number: Union[str | None, Any] = Field(default=None)
    outbound_enabled: Union[bool | None, Any] = Field(default=None)
    priority: Union[int | None, Any] = Field(default=None)
    recorded: Union[bool | None, Any] = Field(default=None)
    schedule_id: Union[int | None, Any] = Field(default=None)
    sms_enabled: Union[bool | None, Any] = Field(default=None)
    sms_group_id: Union[int | None, Any] = Field(default=None)
    token: Union[str | None, Any] = Field(default=None)
    toll_free: Union[bool | None, Any] = Field(default=None)
    transcription: Union[bool | None, Any] = Field(default=None)
    voice_enabled: Union[bool | None, Any] = Field(default=None)

class PhoneNumbersList(BaseModel):
    """PhoneNumbersList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    phone_numbers: Union[list[PhoneNumber], Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

class PhoneNumberWrapper(BaseModel):
    """PhoneNumberWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    phone_number: Union[PhoneNumber, Any] = Field(default=None)

class Address(BaseModel):
    """Address type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    city: Union[str | None, Any] = Field(default=None)
    country_code: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    provider_reference: Union[str | None, Any] = Field(default=None)
    province: Union[str | None, Any] = Field(default=None)
    state: Union[str | None, Any] = Field(default=None)
    street: Union[str | None, Any] = Field(default=None)
    zip: Union[str | None, Any] = Field(default=None)

class AddressesList(BaseModel):
    """AddressesList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    addresses: Union[list[Address], Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

class AddressWrapper(BaseModel):
    """AddressWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address: Union[Address, Any] = Field(default=None)

class Greeting(BaseModel):
    """Greeting type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    active: Union[bool | None, Any] = Field(default=None)
    audio_name: Union[str | None, Any] = Field(default=None)
    audio_url: Union[str | None, Any] = Field(default=None)
    category_id: Union[int | None, Any] = Field(default=None)
    default: Union[bool | None, Any] = Field(default=None)
    default_lang: Union[bool | None, Any] = Field(default=None)
    has_sub_settings: Union[bool | None, Any] = Field(default=None)
    ivr_ids: Union[list[Any] | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    pending: Union[bool | None, Any] = Field(default=None)
    phone_number_ids: Union[list[Any] | None, Any] = Field(default=None)
    upload_id: Union[int | None, Any] = Field(default=None)

class GreetingsList(BaseModel):
    """GreetingsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    greetings: Union[list[Greeting], Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

class GreetingWrapper(BaseModel):
    """GreetingWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    greeting: Union[Greeting, Any] = Field(default=None)

class GreetingCategory(BaseModel):
    """GreetingCategory type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class GreetingCategoriesList(BaseModel):
    """GreetingCategoriesList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    greeting_categories: Union[list[GreetingCategory], Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

class GreetingCategoryWrapper(BaseModel):
    """GreetingCategoryWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    greeting_category: Union[GreetingCategory, Any] = Field(default=None)

class IvrMenusItemRoutesItem(BaseModel):
    """Nested schema for IvrMenusItem.routes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    action: Union[str | None, Any] = Field(default=None)
    greeting: Union[str | None, Any] = Field(default=None)
    keypress: Union[str | None, Any] = Field(default=None)
    option_text: Union[str | None, Any] = Field(default=None)
    options: Union[dict[str, Any] | None, Any] = Field(default=None)
    overflow_options: Union[list[Any] | None, Any] = Field(default=None)

class IvrMenusItem(BaseModel):
    """Nested schema for Ivr.menus_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    default: Union[bool | None, Any] = Field(default=None)
    greeting_id: Union[int | None, Any] = Field(default=None)
    routes: Union[list[IvrMenusItemRoutesItem] | None, Any] = Field(default=None)

class Ivr(BaseModel):
    """Ivr type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    phone_number_ids: Union[list[Any] | None, Any] = Field(default=None)
    phone_number_names: Union[list[Any] | None, Any] = Field(default=None)
    menus: Union[list[IvrMenusItem] | None, Any] = Field(default=None)

class IvrsList(BaseModel):
    """IvrsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ivrs: Union[list[Ivr], Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

class IvrWrapper(BaseModel):
    """IvrWrapper type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ivr: Union[Ivr, Any] = Field(default=None)

class AgentActivity(BaseModel):
    """AgentActivity type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    agent_id: Union[int | None, Any] = Field(default=None)
    agent_state: Union[str | None, Any] = Field(default=None)
    available_time: Union[int | None, Any] = Field(default=None)
    avatar_url: Union[str | None, Any] = Field(default=None)
    away_time: Union[int | None, Any] = Field(default=None)
    call_status: Union[str | None, Any] = Field(default=None)
    calls_accepted: Union[int | None, Any] = Field(default=None)
    calls_denied: Union[int | None, Any] = Field(default=None)
    calls_missed: Union[int | None, Any] = Field(default=None)
    forwarding_number: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    online_time: Union[int | None, Any] = Field(default=None)
    total_call_duration: Union[int | None, Any] = Field(default=None)
    total_talk_time: Union[int | None, Any] = Field(default=None)
    total_wrap_up_time: Union[int | None, Any] = Field(default=None)
    transfers_only_time: Union[int | None, Any] = Field(default=None)
    via: Union[str | None, Any] = Field(default=None)
    accepted_third_party_conferences: Union[int | None, Any] = Field(default=None)
    accepted_transfers: Union[int | None, Any] = Field(default=None)
    average_hold_time: Union[int | None, Any] = Field(default=None)
    average_talk_time: Union[int | None, Any] = Field(default=None)
    average_wrap_up_time: Union[int | None, Any] = Field(default=None)
    calls_put_on_hold: Union[int | None, Any] = Field(default=None)
    started_third_party_conferences: Union[int | None, Any] = Field(default=None)
    started_transfers: Union[int | None, Any] = Field(default=None)
    total_hold_time: Union[int | None, Any] = Field(default=None)

class AgentsActivityList(BaseModel):
    """AgentsActivityList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    agents_activity: Union[list[AgentActivity], Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    previous_page: Union[str | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

class AgentsOverview(BaseModel):
    """AgentsOverview type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    average_calls_accepted: Union[int | None, Any] = Field(default=None)
    average_calls_denied: Union[int | None, Any] = Field(default=None)
    average_calls_missed: Union[int | None, Any] = Field(default=None)
    average_wrap_up_time: Union[int | None, Any] = Field(default=None)
    total_calls_accepted: Union[int | None, Any] = Field(default=None)
    total_calls_denied: Union[int | None, Any] = Field(default=None)
    total_calls_missed: Union[int | None, Any] = Field(default=None)
    total_talk_time: Union[int | None, Any] = Field(default=None)
    total_wrap_up_time: Union[int | None, Any] = Field(default=None)
    average_accepted_transfers: Union[int | None, Any] = Field(default=None)
    average_available_time: Union[int | None, Any] = Field(default=None)
    average_away_time: Union[int | None, Any] = Field(default=None)
    average_calls_put_on_hold: Union[int | None, Any] = Field(default=None)
    average_hold_time: Union[int | None, Any] = Field(default=None)
    average_online_time: Union[int | None, Any] = Field(default=None)
    average_started_transfers: Union[int | None, Any] = Field(default=None)
    average_talk_time: Union[int | None, Any] = Field(default=None)
    average_transfers_only_time: Union[int | None, Any] = Field(default=None)
    current_timestamp: Union[int | None, Any] = Field(default=None)
    total_accepted_transfers: Union[int | None, Any] = Field(default=None)
    total_calls_put_on_hold: Union[int | None, Any] = Field(default=None)
    total_hold_time: Union[int | None, Any] = Field(default=None)
    total_started_transfers: Union[int | None, Any] = Field(default=None)

class AgentsOverviewResponse(BaseModel):
    """AgentsOverviewResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    agents_overview: Union[AgentsOverview, Any] = Field(default=None)

class AccountOverview(BaseModel):
    """AccountOverview type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    average_call_duration: Union[int | None, Any] = Field(default=None)
    average_callback_wait_time: Union[int | None, Any] = Field(default=None)
    average_hold_time: Union[int | None, Any] = Field(default=None)
    average_queue_wait_time: Union[int | None, Any] = Field(default=None)
    average_time_to_answer: Union[int | None, Any] = Field(default=None)
    average_wrap_up_time: Union[int | None, Any] = Field(default=None)
    current_timestamp: Union[int | None, Any] = Field(default=None)
    max_calls_waiting: Union[int | None, Any] = Field(default=None)
    max_queue_wait_time: Union[int | None, Any] = Field(default=None)
    total_call_duration: Union[int | None, Any] = Field(default=None)
    total_callback_calls: Union[int | None, Any] = Field(default=None)
    total_calls: Union[int | None, Any] = Field(default=None)
    total_calls_abandoned_in_queue: Union[int | None, Any] = Field(default=None)
    total_calls_outside_business_hours: Union[int | None, Any] = Field(default=None)
    total_calls_with_exceeded_queue_wait_time: Union[int | None, Any] = Field(default=None)
    total_calls_with_requested_voicemail: Union[int | None, Any] = Field(default=None)
    total_embeddable_callback_calls: Union[int | None, Any] = Field(default=None)
    total_hold_time: Union[int | None, Any] = Field(default=None)
    total_inbound_calls: Union[int | None, Any] = Field(default=None)
    total_outbound_calls: Union[int | None, Any] = Field(default=None)
    total_textback_requests: Union[int | None, Any] = Field(default=None)
    total_voicemails: Union[int | None, Any] = Field(default=None)
    total_wrap_up_time: Union[int | None, Any] = Field(default=None)

class AccountOverviewResponse(BaseModel):
    """AccountOverviewResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_overview: Union[AccountOverview, Any] = Field(default=None)

class CurrentQueueActivity(BaseModel):
    """CurrentQueueActivity type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    agents_online: Union[int | None, Any] = Field(default=None)
    average_wait_time: Union[int | None, Any] = Field(default=None)
    callbacks_waiting: Union[int | None, Any] = Field(default=None)
    calls_waiting: Union[int | None, Any] = Field(default=None)
    current_timestamp: Union[int | None, Any] = Field(default=None)
    embeddable_callbacks_waiting: Union[int | None, Any] = Field(default=None)
    longest_wait_time: Union[int | None, Any] = Field(default=None)
    ai_agent_calls: Union[int | None, Any] = Field(default=None)

class CurrentQueueActivityResponse(BaseModel):
    """CurrentQueueActivityResponse type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    current_queue_activity: Union[CurrentQueueActivity, Any] = Field(default=None)

class Call(BaseModel):
    """Call type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    agent_id: Union[int | None, Any] = Field(default=None)
    call_charge: Union[str | None, Any] = Field(default=None)
    call_group_id: Union[int | None, Any] = Field(default=None)
    call_recording_consent: Union[str | None, Any] = Field(default=None)
    call_recording_consent_action: Union[str | None, Any] = Field(default=None)
    call_recording_consent_keypress: Union[str | None, Any] = Field(default=None)
    callback: Union[bool | None, Any] = Field(default=None)
    callback_source: Union[str | None, Any] = Field(default=None)
    completion_status: Union[str | None, Any] = Field(default=None)
    consultation_time: Union[int | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    customer_requested_voicemail: Union[bool | None, Any] = Field(default=None)
    default_group: Union[bool | None, Any] = Field(default=None)
    direction: Union[str | None, Any] = Field(default=None)
    duration: Union[int | None, Any] = Field(default=None)
    exceeded_queue_time: Union[bool | None, Any] = Field(default=None)
    exceeded_queue_wait_time: Union[bool | None, Any] = Field(default=None)
    hold_time: Union[int | None, Any] = Field(default=None)
    ivr_action: Union[str | None, Any] = Field(default=None)
    ivr_destination_group_name: Union[str | None, Any] = Field(default=None)
    ivr_hops: Union[int | None, Any] = Field(default=None)
    ivr_routed_to: Union[str | None, Any] = Field(default=None)
    ivr_time_spent: Union[int | None, Any] = Field(default=None)
    minutes_billed: Union[int | None, Any] = Field(default=None)
    not_recording_time: Union[int | None, Any] = Field(default=None)
    outside_business_hours: Union[bool | None, Any] = Field(default=None)
    overflowed: Union[bool | None, Any] = Field(default=None)
    overflowed_to: Union[str | None, Any] = Field(default=None)
    phone_number: Union[str | None, Any] = Field(default=None)
    phone_number_id: Union[int | None, Any] = Field(default=None)
    quality_issues: Union[list[str] | None, Any] = Field(default=None)
    recording_control_interactions: Union[int | None, Any] = Field(default=None)
    recording_time: Union[int | None, Any] = Field(default=None)
    talk_time: Union[int | None, Any] = Field(default=None)
    ticket_id: Union[int | None, Any] = Field(default=None)
    time_to_answer: Union[int | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    voicemail: Union[bool | None, Any] = Field(default=None)
    wait_time: Union[int | None, Any] = Field(default=None)
    wrap_up_time: Union[int | None, Any] = Field(default=None)
    customer_id: Union[int | None, Any] = Field(default=None)
    line: Union[str | None, Any] = Field(default=None)
    line_id: Union[int | None, Any] = Field(default=None)
    line_type: Union[str | None, Any] = Field(default=None)
    call_channel: Union[str | None, Any] = Field(default=None)
    post_call_transcription_created: Union[bool | None, Any] = Field(default=None)
    post_call_summary_created: Union[bool | None, Any] = Field(default=None)

class CallsList(BaseModel):
    """CallsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    calls: Union[list[Call], Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)
    end_time: Union[int | None, Any] = Field(default=None)

class CallLeg(BaseModel):
    """CallLeg type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[int | None, Any] = Field(default=None)
    type_: Union[str | None, Any] = Field(default=None, alias="type")
    agent_id: Union[int | None, Any] = Field(default=None)
    available_via: Union[str | None, Any] = Field(default=None)
    call_charge: Union[str | None, Any] = Field(default=None)
    call_id: Union[int | None, Any] = Field(default=None)
    completion_status: Union[str | None, Any] = Field(default=None)
    conference_from: Union[int | None, Any] = Field(default=None)
    conference_time: Union[int | None, Any] = Field(default=None)
    conference_to: Union[int | None, Any] = Field(default=None)
    consultation_from: Union[int | None, Any] = Field(default=None)
    consultation_time: Union[int | None, Any] = Field(default=None)
    consultation_to: Union[int | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    duration: Union[int | None, Any] = Field(default=None)
    forwarded_to: Union[str | None, Any] = Field(default=None)
    hold_time: Union[int | None, Any] = Field(default=None)
    minutes_billed: Union[int | None, Any] = Field(default=None)
    quality_issues: Union[list[str] | None, Any] = Field(default=None)
    talk_time: Union[int | None, Any] = Field(default=None)
    transferred_from: Union[int | None, Any] = Field(default=None)
    transferred_to: Union[int | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    user_id: Union[int | None, Any] = Field(default=None)
    wrap_up_time: Union[int | None, Any] = Field(default=None)

class CallLegsList(BaseModel):
    """CallLegsList type definition"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    legs: Union[list[CallLeg], Any] = Field(default=None)
    next_page: Union[str | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)
    end_time: Union[int | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class PhoneNumbersListResultMeta(BaseModel):
    """Metadata for phone_numbers.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)

class AddressesListResultMeta(BaseModel):
    """Metadata for addresses.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)

class GreetingsListResultMeta(BaseModel):
    """Metadata for greetings.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)

class GreetingCategoriesListResultMeta(BaseModel):
    """Metadata for greeting_categories.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)

class IvrsListResultMeta(BaseModel):
    """Metadata for ivrs.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)

class AgentsActivityListResultMeta(BaseModel):
    """Metadata for agents_activity.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)

class CallsListResultMeta(BaseModel):
    """Metadata for calls.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

class CallLegsListResultMeta(BaseModel):
    """Metadata for call_legs.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    next_page: Union[str | None, Any] = Field(default=None)
    count: Union[int | None, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class ZendeskTalkCheckResult(BaseModel):
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


class ZendeskTalkExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class ZendeskTalkExecuteResultWithMeta(ZendeskTalkExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class AddressesSearchData(BaseModel):
    """Search result data for addresses entity."""
    model_config = ConfigDict(extra="allow")

    city: str | None = None
    """City of the address"""
    country_code: str | None = None
    """ISO country code"""
    id: int | None = None
    """Unique address identifier"""
    name: str | None = None
    """Name of the address"""
    provider_reference: str | None = None
    """Provider reference of the address"""
    province: str | None = None
    """Province of the address"""
    state: str | None = None
    """State of the address"""
    street: str | None = None
    """Street of the address"""
    zip: str | None = None
    """Zip code of the address"""


class AgentsActivitySearchData(BaseModel):
    """Search result data for agents_activity entity."""
    model_config = ConfigDict(extra="allow")

    accepted_third_party_conferences: int | None = None
    """Accepted third party conferences"""
    accepted_transfers: int | None = None
    """Total transfers accepted"""
    agent_id: int | None = None
    """Agent ID"""
    agent_state: str | None = None
    """Agent state: online, offline, away, or transfers_only"""
    available_time: int | None = None
    """Total time agent was available to answer calls"""
    avatar_url: str | None = None
    """URL to agent avatar"""
    average_hold_time: int | None = None
    """Average hold time per call"""
    average_talk_time: int | None = None
    """Average talk time per call"""
    average_wrap_up_time: int | None = None
    """Average wrap-up time per call"""
    away_time: int | None = None
    """Total time agent was set to away"""
    call_status: str | None = None
    """Agent call status: on_call, wrap_up, or null"""
    calls_accepted: int | None = None
    """Total calls accepted"""
    calls_denied: int | None = None
    """Total calls denied"""
    calls_missed: int | None = None
    """Total calls missed"""
    calls_put_on_hold: int | None = None
    """Total calls placed on hold"""
    forwarding_number: str | None = None
    """Forwarding number set by the agent"""
    name: str | None = None
    """Agent name"""
    online_time: int | None = None
    """Total online time"""
    started_third_party_conferences: int | None = None
    """Started third party conferences"""
    started_transfers: int | None = None
    """Total transfers started"""
    total_call_duration: int | None = None
    """Total call duration"""
    total_hold_time: int | None = None
    """Total hold time across all calls"""
    total_talk_time: int | None = None
    """Total talk time (excludes hold)"""
    total_wrap_up_time: int | None = None
    """Total wrap-up time"""
    transfers_only_time: int | None = None
    """Total time in transfers-only mode"""
    via: str | None = None
    """Channel the agent is registered on"""


class AgentsOverviewSearchData(BaseModel):
    """Search result data for agents_overview entity."""
    model_config = ConfigDict(extra="allow")

    average_accepted_transfers: int | None = None
    """Average accepted transfers"""
    average_available_time: int | None = None
    """Average available time"""
    average_away_time: int | None = None
    """Average away time"""
    average_calls_accepted: int | None = None
    """Average calls accepted"""
    average_calls_denied: int | None = None
    """Average calls denied"""
    average_calls_missed: int | None = None
    """Average calls missed"""
    average_calls_put_on_hold: int | None = None
    """Average calls put on hold"""
    average_hold_time: int | None = None
    """Average hold time"""
    average_online_time: int | None = None
    """Average online time"""
    average_started_transfers: int | None = None
    """Average started transfers"""
    average_talk_time: int | None = None
    """Average talk time"""
    average_transfers_only_time: int | None = None
    """Average transfers-only time"""
    average_wrap_up_time: int | None = None
    """Average wrap-up time"""
    current_timestamp: int | None = None
    """Current timestamp"""
    total_accepted_transfers: int | None = None
    """Total accepted transfers"""
    total_calls_accepted: int | None = None
    """Total calls accepted"""
    total_calls_denied: int | None = None
    """Total calls denied"""
    total_calls_missed: int | None = None
    """Total calls missed"""
    total_calls_put_on_hold: int | None = None
    """Total calls put on hold"""
    total_hold_time: int | None = None
    """Total hold time"""
    total_started_transfers: int | None = None
    """Total started transfers"""
    total_talk_time: int | None = None
    """Total talk time"""
    total_wrap_up_time: int | None = None
    """Total wrap-up time"""


class GreetingCategoriesSearchData(BaseModel):
    """Search result data for greeting_categories entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """Greeting category ID"""
    name: str | None = None
    """Name of the greeting category"""


class GreetingsSearchData(BaseModel):
    """Search result data for greetings entity."""
    model_config = ConfigDict(extra="allow")

    active: bool | None = None
    """Whether the greeting is associated with phone numbers"""
    audio_name: str | None = None
    """Audio file name"""
    audio_url: str | None = None
    """Path to the greeting sound file"""
    category_id: int | None = None
    """ID of the greeting category"""
    default: bool | None = None
    """Whether this is a system default greeting"""
    default_lang: bool | None = None
    """Whether the greeting has a default language"""
    has_sub_settings: bool | None = None
    """Sub-settings for categorized greetings"""
    id: str | None = None
    """Greeting ID"""
    ivr_ids: list[Any] | None = None
    """IDs of IVRs associated with the greeting"""
    name: str | None = None
    """Name of the greeting"""
    pending: bool | None = None
    """Whether the greeting is pending"""
    phone_number_ids: list[Any] | None = None
    """IDs of phone numbers associated with the greeting"""
    upload_id: int | None = None
    """Upload ID associated with the greeting"""


class PhoneNumbersSearchData(BaseModel):
    """Search result data for phone_numbers entity."""
    model_config = ConfigDict(extra="allow")

    call_recording_consent: str | None = None
    """What call recording consent is set to"""
    capabilities: dict[str, Any] | None = None
    """Phone number capabilities (sms, mms, voice)"""
    categorised_greetings: dict[str, Any] | None = None
    """Greeting category IDs and names"""
    categorised_greetings_with_sub_settings: dict[str, Any] | None = None
    """Greeting categories with associated settings"""
    country_code: str | None = None
    """ISO country code for the number"""
    created_at: str | None = None
    """Date and time the phone number was created"""
    default_greeting_ids: list[Any] | None = None
    """Names of default system greetings"""
    default_group_id: int | None = None
    """Default group ID"""
    display_number: str | None = None
    """Formatted phone number"""
    external: bool | None = None
    """Whether this is an external caller ID number"""
    failover_number: str | None = None
    """Failover number associated with the phone number"""
    greeting_ids: list[Any] | None = None
    """Custom greeting IDs associated with the phone number"""
    group_ids: list[Any] | None = None
    """Array of associated group IDs"""
    id: int | None = None
    """Unique phone number identifier"""
    ivr_id: int | None = None
    """ID of IVR associated with the phone number"""
    line_type: str | None = None
    """Type of line (phone or digital)"""
    location: str | None = None
    """Geographical location of the number"""
    name: str | None = None
    """Nickname if set, otherwise the display number"""
    nickname: str | None = None
    """Nickname of the phone number"""
    number: str | None = None
    """Phone number digits"""
    outbound_enabled: bool | None = None
    """Whether outbound calls are enabled"""
    priority: int | None = None
    """Priority level of the phone number"""
    recorded: bool | None = None
    """Whether calls are recorded"""
    schedule_id: int | None = None
    """ID of schedule associated with the phone number"""
    sms_enabled: bool | None = None
    """Whether SMS is enabled"""
    sms_group_id: int | None = None
    """Group associated with SMS"""
    token: str | None = None
    """Generated token unique for the phone number"""
    toll_free: bool | None = None
    """Whether the number is toll-free"""
    transcription: bool | None = None
    """Whether voicemail transcription is enabled"""
    voice_enabled: bool | None = None
    """Whether voice is enabled"""


class CallLegsSearchData(BaseModel):
    """Search result data for call_legs entity."""
    model_config = ConfigDict(extra="allow")

    agent_id: int | None = None
    """Agent ID"""
    available_via: str | None = None
    """Channel agent was available through"""
    call_charge: str | None = None
    """Call charge amount"""
    call_id: int | None = None
    """Associated call ID"""
    completion_status: str | None = None
    """Completion status"""
    conference_from: int | None = None
    """Conference from time"""
    conference_time: int | None = None
    """Conference duration"""
    conference_to: int | None = None
    """Conference to time"""
    consultation_from: int | None = None
    """Consultation from time"""
    consultation_time: int | None = None
    """Consultation duration"""
    consultation_to: int | None = None
    """Consultation to time"""
    created_at: str | None = None
    """Creation timestamp"""
    duration: int | None = None
    """Duration in seconds"""
    forwarded_to: str | None = None
    """Number forwarded to"""
    hold_time: int | None = None
    """Hold time in seconds"""
    id: int | None = None
    """Call leg ID"""
    minutes_billed: int | None = None
    """Minutes billed"""
    quality_issues: list[Any] | None = None
    """Quality issues detected"""
    talk_time: int | None = None
    """Talk time in seconds"""
    transferred_from: int | None = None
    """Transferred from agent ID"""
    transferred_to: int | None = None
    """Transferred to agent ID"""
    type_: str | None = None
    """Type of call leg"""
    updated_at: str | None = None
    """Last update timestamp"""
    user_id: int | None = None
    """User ID"""
    wrap_up_time: int | None = None
    """Wrap-up time in seconds"""


class CallsSearchData(BaseModel):
    """Search result data for calls entity."""
    model_config = ConfigDict(extra="allow")

    agent_id: int | None = None
    """Agent ID"""
    call_charge: str | None = None
    """Call charge amount"""
    call_group_id: int | None = None
    """Call group ID"""
    call_recording_consent: str | None = None
    """Call recording consent status"""
    call_recording_consent_action: str | None = None
    """Recording consent action"""
    call_recording_consent_keypress: str | None = None
    """Recording consent keypress"""
    callback: bool | None = None
    """Whether this was a callback"""
    callback_source: str | None = None
    """Source of the callback"""
    completion_status: str | None = None
    """Call completion status"""
    consultation_time: int | None = None
    """Consultation time"""
    created_at: str | None = None
    """Creation timestamp"""
    customer_requested_voicemail: bool | None = None
    """Whether customer requested voicemail"""
    default_group: bool | None = None
    """Whether default group was used"""
    direction: str | None = None
    """Call direction (inbound/outbound)"""
    duration: int | None = None
    """Call duration in seconds"""
    exceeded_queue_time: bool | None = None
    """Whether queue time was exceeded"""
    exceeded_queue_wait_time: bool | None = None
    """Whether max queue wait time was exceeded"""
    hold_time: int | None = None
    """Hold time in seconds"""
    id: int | None = None
    """Call ID"""
    ivr_action: str | None = None
    """IVR action taken"""
    ivr_destination_group_name: str | None = None
    """IVR destination group name"""
    ivr_hops: int | None = None
    """Number of IVR hops"""
    ivr_routed_to: str | None = None
    """Where IVR routed the call"""
    ivr_time_spent: int | None = None
    """Time spent in IVR"""
    minutes_billed: int | None = None
    """Minutes billed"""
    not_recording_time: int | None = None
    """Time not recording"""
    outside_business_hours: bool | None = None
    """Whether call was outside business hours"""
    overflowed: bool | None = None
    """Whether call overflowed"""
    overflowed_to: str | None = None
    """Where call overflowed to"""
    phone_number: str | None = None
    """Phone number used"""
    phone_number_id: int | None = None
    """Phone number ID"""
    quality_issues: list[Any] | None = None
    """Quality issues detected"""
    recording_control_interactions: int | None = None
    """Recording control interactions count"""
    recording_time: int | None = None
    """Recording time"""
    talk_time: int | None = None
    """Talk time in seconds"""
    ticket_id: int | None = None
    """Associated ticket ID"""
    time_to_answer: int | None = None
    """Time to answer in seconds"""
    updated_at: str | None = None
    """Last update timestamp"""
    voicemail: bool | None = None
    """Whether it was a voicemail"""
    wait_time: int | None = None
    """Wait time in seconds"""
    wrap_up_time: int | None = None
    """Wrap-up time in seconds"""


class CurrentQueueActivitySearchData(BaseModel):
    """Search result data for current_queue_activity entity."""
    model_config = ConfigDict(extra="allow")

    agents_online: int | None = None
    """Current number of agents online"""
    average_wait_time: int | None = None
    """Average wait time for callers in queue (seconds)"""
    callbacks_waiting: int | None = None
    """Number of callers in callback queue"""
    calls_waiting: int | None = None
    """Number of callers waiting in queue"""
    current_timestamp: int | None = None
    """Current timestamp"""
    embeddable_callbacks_waiting: int | None = None
    """Number of Web Widget callback requests waiting"""
    longest_wait_time: int | None = None
    """Longest wait time for any caller (seconds)"""


class AccountOverviewSearchData(BaseModel):
    """Search result data for account_overview entity."""
    model_config = ConfigDict(extra="allow")

    average_call_duration: int | None = None
    """Average call duration"""
    average_callback_wait_time: int | None = None
    """Average callback wait time"""
    average_hold_time: int | None = None
    """Average hold time per call"""
    average_queue_wait_time: int | None = None
    """Average queue wait time"""
    average_time_to_answer: int | None = None
    """Average time to answer"""
    average_wrap_up_time: int | None = None
    """Average wrap-up time"""
    current_timestamp: int | None = None
    """Current timestamp"""
    max_calls_waiting: int | None = None
    """Max calls waiting in queue"""
    max_queue_wait_time: int | None = None
    """Max queue wait time"""
    total_call_duration: int | None = None
    """Total call duration"""
    total_callback_calls: int | None = None
    """Total callback calls"""
    total_calls: int | None = None
    """Total calls"""
    total_calls_abandoned_in_queue: int | None = None
    """Total calls abandoned in queue"""
    total_calls_outside_business_hours: int | None = None
    """Total calls outside business hours"""
    total_calls_with_exceeded_queue_wait_time: int | None = None
    """Total calls exceeding max queue wait time"""
    total_calls_with_requested_voicemail: int | None = None
    """Total calls requesting voicemail"""
    total_embeddable_callback_calls: int | None = None
    """Total embeddable callback calls"""
    total_hold_time: int | None = None
    """Total hold time"""
    total_inbound_calls: int | None = None
    """Total inbound calls"""
    total_outbound_calls: int | None = None
    """Total outbound calls"""
    total_textback_requests: int | None = None
    """Total textback requests"""
    total_voicemails: int | None = None
    """Total voicemails"""
    total_wrap_up_time: int | None = None
    """Total wrap-up time"""


class IvrsSearchData(BaseModel):
    """Search result data for ivrs entity."""
    model_config = ConfigDict(extra="allow")

    id: int | None = None
    """IVR ID"""
    menus: list[Any] | None = None
    """List of IVR menus"""
    name: str | None = None
    """Name of the IVR"""
    phone_number_ids: list[Any] | None = None
    """IDs of phone numbers configured with this IVR"""
    phone_number_names: list[Any] | None = None
    """Names of phone numbers configured with this IVR"""


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

AddressesSearchResult = AirbyteSearchResult[AddressesSearchData]
"""Search result type for addresses entity."""

AgentsActivitySearchResult = AirbyteSearchResult[AgentsActivitySearchData]
"""Search result type for agents_activity entity."""

AgentsOverviewSearchResult = AirbyteSearchResult[AgentsOverviewSearchData]
"""Search result type for agents_overview entity."""

GreetingCategoriesSearchResult = AirbyteSearchResult[GreetingCategoriesSearchData]
"""Search result type for greeting_categories entity."""

GreetingsSearchResult = AirbyteSearchResult[GreetingsSearchData]
"""Search result type for greetings entity."""

PhoneNumbersSearchResult = AirbyteSearchResult[PhoneNumbersSearchData]
"""Search result type for phone_numbers entity."""

CallLegsSearchResult = AirbyteSearchResult[CallLegsSearchData]
"""Search result type for call_legs entity."""

CallsSearchResult = AirbyteSearchResult[CallsSearchData]
"""Search result type for calls entity."""

CurrentQueueActivitySearchResult = AirbyteSearchResult[CurrentQueueActivitySearchData]
"""Search result type for current_queue_activity entity."""

AccountOverviewSearchResult = AirbyteSearchResult[AccountOverviewSearchData]
"""Search result type for account_overview entity."""

IvrsSearchResult = AirbyteSearchResult[IvrsSearchData]
"""Search result type for ivrs entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

PhoneNumbersListResult = ZendeskTalkExecuteResultWithMeta[list[PhoneNumber], PhoneNumbersListResultMeta]
"""Result type for phone_numbers.list operation with data and metadata."""

AddressesListResult = ZendeskTalkExecuteResultWithMeta[list[Address], AddressesListResultMeta]
"""Result type for addresses.list operation with data and metadata."""

GreetingsListResult = ZendeskTalkExecuteResultWithMeta[list[Greeting], GreetingsListResultMeta]
"""Result type for greetings.list operation with data and metadata."""

GreetingCategoriesListResult = ZendeskTalkExecuteResultWithMeta[list[GreetingCategory], GreetingCategoriesListResultMeta]
"""Result type for greeting_categories.list operation with data and metadata."""

IvrsListResult = ZendeskTalkExecuteResultWithMeta[list[Ivr], IvrsListResultMeta]
"""Result type for ivrs.list operation with data and metadata."""

AgentsActivityListResult = ZendeskTalkExecuteResultWithMeta[list[AgentActivity], AgentsActivityListResultMeta]
"""Result type for agents_activity.list operation with data and metadata."""

AgentsOverviewListResult = ZendeskTalkExecuteResult[AgentsOverview]
"""Result type for agents_overview.list operation."""

AccountOverviewListResult = ZendeskTalkExecuteResult[AccountOverview]
"""Result type for account_overview.list operation."""

CurrentQueueActivityListResult = ZendeskTalkExecuteResult[CurrentQueueActivity]
"""Result type for current_queue_activity.list operation."""

CallsListResult = ZendeskTalkExecuteResultWithMeta[list[Call], CallsListResultMeta]
"""Result type for calls.list operation with data and metadata."""

CallLegsListResult = ZendeskTalkExecuteResultWithMeta[list[CallLeg], CallLegsListResultMeta]
"""Result type for call_legs.list operation with data and metadata."""

