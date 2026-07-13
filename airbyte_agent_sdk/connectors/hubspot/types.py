"""
Type definitions for hubspot connector.
"""
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

class ContactsCreateParamsProperties(TypedDict):
    """Contact properties to set"""
    email: str
    firstname: NotRequired[str]
    lastname: NotRequired[str]
    phone: NotRequired[str]
    company: NotRequired[str]
    website: NotRequired[str]
    lifecyclestage: NotRequired[str]
    jobtitle: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class ContactsUpdateParamsProperties(TypedDict):
    """Contact properties to update"""
    email: NotRequired[str]
    firstname: NotRequired[str]
    lastname: NotRequired[str]
    phone: NotRequired[str]
    company: NotRequired[str]
    website: NotRequired[str]
    lifecyclestage: NotRequired[str]
    jobtitle: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class ContactsApiSearchParamsFiltergroupsItemFiltersItem(TypedDict):
    """Nested schema for ContactsApiSearchParamsFiltergroupsItem.filters_item"""
    operator: NotRequired[str]
    property_name: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[list[str]]

class ContactsApiSearchParamsFiltergroupsItem(TypedDict):
    """Nested schema for ContactsApiSearchParams.filterGroups_item"""
    filters: NotRequired[list[ContactsApiSearchParamsFiltergroupsItemFiltersItem]]

class ContactsApiSearchParamsSortsItem(TypedDict):
    """Nested schema for ContactsApiSearchParams.sorts_item"""
    property_name: NotRequired[str]
    direction: NotRequired[str]

class CompaniesCreateParamsProperties(TypedDict):
    """Company properties to set"""
    name: str
    domain: NotRequired[str]
    description: NotRequired[str]
    phone: NotRequired[str]
    industry: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    country: NotRequired[str]
    zip: NotRequired[str]
    numberofemployees: NotRequired[str]
    annualrevenue: NotRequired[str]
    lifecyclestage: NotRequired[str]
    hubspot_owner_id: NotRequired[str]
    website: NotRequired[str]

class CompaniesUpdateParamsProperties(TypedDict):
    """Company properties to update"""
    name: NotRequired[str]
    domain: NotRequired[str]
    description: NotRequired[str]
    phone: NotRequired[str]
    industry: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    country: NotRequired[str]
    zip: NotRequired[str]
    numberofemployees: NotRequired[str]
    annualrevenue: NotRequired[str]
    lifecyclestage: NotRequired[str]
    hubspot_owner_id: NotRequired[str]
    website: NotRequired[str]

class CompaniesApiSearchParamsFiltergroupsItemFiltersItem(TypedDict):
    """Nested schema for CompaniesApiSearchParamsFiltergroupsItem.filters_item"""
    operator: NotRequired[str]
    property_name: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[list[str]]

class CompaniesApiSearchParamsFiltergroupsItem(TypedDict):
    """Nested schema for CompaniesApiSearchParams.filterGroups_item"""
    filters: NotRequired[list[CompaniesApiSearchParamsFiltergroupsItemFiltersItem]]

class CompaniesApiSearchParamsSortsItem(TypedDict):
    """Nested schema for CompaniesApiSearchParams.sorts_item"""
    property_name: NotRequired[str]
    direction: NotRequired[str]

class DealsCreateParamsProperties(TypedDict):
    """Deal properties to set"""
    dealname: str
    amount: NotRequired[str]
    dealstage: NotRequired[str]
    pipeline: NotRequired[str]
    closedate: NotRequired[str]
    dealtype: NotRequired[str]
    description: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class DealsUpdateParamsProperties(TypedDict):
    """Deal properties to update"""
    dealname: NotRequired[str]
    amount: NotRequired[str]
    dealstage: NotRequired[str]
    pipeline: NotRequired[str]
    closedate: NotRequired[str]
    dealtype: NotRequired[str]
    description: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class DealsApiSearchParamsFiltergroupsItemFiltersItem(TypedDict):
    """Nested schema for DealsApiSearchParamsFiltergroupsItem.filters_item"""
    operator: NotRequired[str]
    property_name: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[list[str]]

class DealsApiSearchParamsFiltergroupsItem(TypedDict):
    """Nested schema for DealsApiSearchParams.filterGroups_item"""
    filters: NotRequired[list[DealsApiSearchParamsFiltergroupsItemFiltersItem]]

class DealsApiSearchParamsSortsItem(TypedDict):
    """Nested schema for DealsApiSearchParams.sorts_item"""
    property_name: NotRequired[str]
    direction: NotRequired[str]

class TicketsCreateParamsProperties(TypedDict):
    """Ticket properties to set"""
    subject: str
    content: NotRequired[str]
    hs_pipeline: str
    hs_pipeline_stage: str
    hs_ticket_priority: NotRequired[str]
    hs_ticket_category: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class TicketsUpdateParamsProperties(TypedDict):
    """Ticket properties to update"""
    subject: NotRequired[str]
    content: NotRequired[str]
    hs_pipeline: NotRequired[str]
    hs_pipeline_stage: NotRequired[str]
    hs_ticket_priority: NotRequired[str]
    hs_ticket_category: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class TicketsApiSearchParamsFiltergroupsItemFiltersItem(TypedDict):
    """Nested schema for TicketsApiSearchParamsFiltergroupsItem.filters_item"""
    operator: NotRequired[str]
    property_name: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[list[str]]

class TicketsApiSearchParamsFiltergroupsItem(TypedDict):
    """Nested schema for TicketsApiSearchParams.filterGroups_item"""
    filters: NotRequired[list[TicketsApiSearchParamsFiltergroupsItemFiltersItem]]

class TicketsApiSearchParamsSortsItem(TypedDict):
    """Nested schema for TicketsApiSearchParams.sorts_item"""
    property_name: NotRequired[str]
    direction: NotRequired[str]

class NotesCreateParamsProperties(TypedDict):
    """Note properties to set"""
    hs_note_body: str
    hs_timestamp: str
    hubspot_owner_id: NotRequired[str]

class NotesCreateParamsAssociationsItemTo(TypedDict):
    """Nested schema for NotesCreateParamsAssociationsItem.to"""
    id: NotRequired[str]

class NotesCreateParamsAssociationsItemTypesItem(TypedDict):
    """Nested schema for NotesCreateParamsAssociationsItem.types_item"""
    association_category: NotRequired[str]
    association_type_id: NotRequired[int]

class NotesCreateParamsAssociationsItem(TypedDict):
    """Nested schema for NotesCreateParams.associations_item"""
    to: NotRequired[NotesCreateParamsAssociationsItemTo]
    types: NotRequired[list[NotesCreateParamsAssociationsItemTypesItem]]

class NotesUpdateParamsProperties(TypedDict):
    """Note properties to update"""
    hs_note_body: NotRequired[str]
    hs_timestamp: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class CallsCreateParamsProperties(TypedDict):
    """Call properties to set"""
    hs_call_body: NotRequired[str]
    hs_call_direction: NotRequired[str]
    hs_call_disposition: NotRequired[str]
    hs_call_duration: NotRequired[str]
    hs_call_from_number: NotRequired[str]
    hs_call_to_number: NotRequired[str]
    hs_call_status: NotRequired[str]
    hs_call_title: NotRequired[str]
    hs_timestamp: str
    hubspot_owner_id: NotRequired[str]

class CallsCreateParamsAssociationsItemTo(TypedDict):
    """Nested schema for CallsCreateParamsAssociationsItem.to"""
    id: NotRequired[str]

class CallsCreateParamsAssociationsItemTypesItem(TypedDict):
    """Nested schema for CallsCreateParamsAssociationsItem.types_item"""
    association_category: NotRequired[str]
    association_type_id: NotRequired[int]

class CallsCreateParamsAssociationsItem(TypedDict):
    """Nested schema for CallsCreateParams.associations_item"""
    to: NotRequired[CallsCreateParamsAssociationsItemTo]
    types: NotRequired[list[CallsCreateParamsAssociationsItemTypesItem]]

class CallsUpdateParamsProperties(TypedDict):
    """Call properties to update"""
    hs_call_body: NotRequired[str]
    hs_call_direction: NotRequired[str]
    hs_call_disposition: NotRequired[str]
    hs_call_duration: NotRequired[str]
    hs_call_from_number: NotRequired[str]
    hs_call_to_number: NotRequired[str]
    hs_call_status: NotRequired[str]
    hs_call_title: NotRequired[str]
    hs_timestamp: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class EmailsCreateParamsProperties(TypedDict):
    """Email properties to set"""
    hs_email_subject: NotRequired[str]
    hs_email_text: NotRequired[str]
    hs_email_html: NotRequired[str]
    hs_email_direction: str
    hs_email_status: NotRequired[str]
    hs_email_sender_email: NotRequired[str]
    hs_email_to_email: NotRequired[str]
    hs_timestamp: str
    hubspot_owner_id: NotRequired[str]

class EmailsCreateParamsAssociationsItemTo(TypedDict):
    """Nested schema for EmailsCreateParamsAssociationsItem.to"""
    id: NotRequired[str]

class EmailsCreateParamsAssociationsItemTypesItem(TypedDict):
    """Nested schema for EmailsCreateParamsAssociationsItem.types_item"""
    association_category: NotRequired[str]
    association_type_id: NotRequired[int]

class EmailsCreateParamsAssociationsItem(TypedDict):
    """Nested schema for EmailsCreateParams.associations_item"""
    to: NotRequired[EmailsCreateParamsAssociationsItemTo]
    types: NotRequired[list[EmailsCreateParamsAssociationsItemTypesItem]]

class EmailsUpdateParamsProperties(TypedDict):
    """Email properties to update"""
    hs_email_subject: NotRequired[str]
    hs_email_text: NotRequired[str]
    hs_email_html: NotRequired[str]
    hs_email_direction: NotRequired[str]
    hs_email_status: NotRequired[str]
    hs_timestamp: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class MeetingsCreateParamsProperties(TypedDict):
    """Meeting properties to set"""
    hs_meeting_title: str
    hs_meeting_body: NotRequired[str]
    hs_meeting_start_time: NotRequired[str]
    hs_meeting_end_time: NotRequired[str]
    hs_meeting_location: NotRequired[str]
    hs_meeting_outcome: NotRequired[str]
    hs_internal_meeting_notes: NotRequired[str]
    hs_timestamp: str
    hubspot_owner_id: NotRequired[str]

class MeetingsCreateParamsAssociationsItemTo(TypedDict):
    """Nested schema for MeetingsCreateParamsAssociationsItem.to"""
    id: NotRequired[str]

class MeetingsCreateParamsAssociationsItemTypesItem(TypedDict):
    """Nested schema for MeetingsCreateParamsAssociationsItem.types_item"""
    association_category: NotRequired[str]
    association_type_id: NotRequired[int]

class MeetingsCreateParamsAssociationsItem(TypedDict):
    """Nested schema for MeetingsCreateParams.associations_item"""
    to: NotRequired[MeetingsCreateParamsAssociationsItemTo]
    types: NotRequired[list[MeetingsCreateParamsAssociationsItemTypesItem]]

class MeetingsUpdateParamsProperties(TypedDict):
    """Meeting properties to update"""
    hs_meeting_title: NotRequired[str]
    hs_meeting_body: NotRequired[str]
    hs_meeting_start_time: NotRequired[str]
    hs_meeting_end_time: NotRequired[str]
    hs_meeting_location: NotRequired[str]
    hs_meeting_outcome: NotRequired[str]
    hs_internal_meeting_notes: NotRequired[str]
    hs_timestamp: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

class TasksCreateParamsProperties(TypedDict):
    """Task properties to set"""
    hs_task_body: NotRequired[str]
    hs_task_subject: str
    hs_task_status: NotRequired[str]
    hs_task_priority: NotRequired[str]
    hs_task_type: NotRequired[str]
    hs_task_reminders: NotRequired[str]
    hs_timestamp: str
    hubspot_owner_id: NotRequired[str]

class TasksCreateParamsAssociationsItemTo(TypedDict):
    """Nested schema for TasksCreateParamsAssociationsItem.to"""
    id: NotRequired[str]

class TasksCreateParamsAssociationsItemTypesItem(TypedDict):
    """Nested schema for TasksCreateParamsAssociationsItem.types_item"""
    association_category: NotRequired[str]
    association_type_id: NotRequired[int]

class TasksCreateParamsAssociationsItem(TypedDict):
    """Nested schema for TasksCreateParams.associations_item"""
    to: NotRequired[TasksCreateParamsAssociationsItemTo]
    types: NotRequired[list[TasksCreateParamsAssociationsItemTypesItem]]

class TasksUpdateParamsProperties(TypedDict):
    """Task properties to update"""
    hs_task_body: NotRequired[str]
    hs_task_subject: NotRequired[str]
    hs_task_status: NotRequired[str]
    hs_task_priority: NotRequired[str]
    hs_task_type: NotRequired[str]
    hs_task_reminders: NotRequired[str]
    hs_timestamp: NotRequired[str]
    hubspot_owner_id: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class ContactsListParams(TypedDict):
    """Parameters for contacts.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class ContactsCreateParams(TypedDict):
    """Parameters for contacts.create operation"""
    properties: ContactsCreateParamsProperties

class ContactsGetParams(TypedDict):
    """Parameters for contacts.get operation"""
    contact_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class ContactsUpdateParams(TypedDict):
    """Parameters for contacts.update operation"""
    properties: ContactsUpdateParamsProperties
    contact_id: str

class ContactsApiSearchParams(TypedDict):
    """Parameters for contacts.api_search operation"""
    filter_groups: NotRequired[list[ContactsApiSearchParamsFiltergroupsItem]]
    properties: NotRequired[list[str]]
    limit: NotRequired[int]
    after: NotRequired[str]
    sorts: NotRequired[list[ContactsApiSearchParamsSortsItem]]
    query: NotRequired[str]

class CompaniesListParams(TypedDict):
    """Parameters for companies.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class CompaniesCreateParams(TypedDict):
    """Parameters for companies.create operation"""
    properties: CompaniesCreateParamsProperties

class CompaniesGetParams(TypedDict):
    """Parameters for companies.get operation"""
    company_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class CompaniesUpdateParams(TypedDict):
    """Parameters for companies.update operation"""
    properties: CompaniesUpdateParamsProperties
    company_id: str

class CompaniesApiSearchParams(TypedDict):
    """Parameters for companies.api_search operation"""
    filter_groups: NotRequired[list[CompaniesApiSearchParamsFiltergroupsItem]]
    properties: NotRequired[list[str]]
    limit: NotRequired[int]
    after: NotRequired[str]
    sorts: NotRequired[list[CompaniesApiSearchParamsSortsItem]]
    query: NotRequired[str]

class DealsListParams(TypedDict):
    """Parameters for deals.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class DealsCreateParams(TypedDict):
    """Parameters for deals.create operation"""
    properties: DealsCreateParamsProperties

class DealsGetParams(TypedDict):
    """Parameters for deals.get operation"""
    deal_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class DealsUpdateParams(TypedDict):
    """Parameters for deals.update operation"""
    properties: DealsUpdateParamsProperties
    deal_id: str

class DealsApiSearchParams(TypedDict):
    """Parameters for deals.api_search operation"""
    filter_groups: NotRequired[list[DealsApiSearchParamsFiltergroupsItem]]
    properties: NotRequired[list[str]]
    limit: NotRequired[int]
    after: NotRequired[str]
    sorts: NotRequired[list[DealsApiSearchParamsSortsItem]]
    query: NotRequired[str]

class TicketsListParams(TypedDict):
    """Parameters for tickets.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class TicketsCreateParams(TypedDict):
    """Parameters for tickets.create operation"""
    properties: TicketsCreateParamsProperties

class TicketsGetParams(TypedDict):
    """Parameters for tickets.get operation"""
    ticket_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class TicketsUpdateParams(TypedDict):
    """Parameters for tickets.update operation"""
    properties: TicketsUpdateParamsProperties
    ticket_id: str

class TicketsApiSearchParams(TypedDict):
    """Parameters for tickets.api_search operation"""
    filter_groups: NotRequired[list[TicketsApiSearchParamsFiltergroupsItem]]
    properties: NotRequired[list[str]]
    limit: NotRequired[int]
    after: NotRequired[str]
    sorts: NotRequired[list[TicketsApiSearchParamsSortsItem]]
    query: NotRequired[str]

class NotesListParams(TypedDict):
    """Parameters for notes.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class NotesCreateParams(TypedDict):
    """Parameters for notes.create operation"""
    properties: NotesCreateParamsProperties
    associations: NotRequired[list[NotesCreateParamsAssociationsItem]]

class NotesGetParams(TypedDict):
    """Parameters for notes.get operation"""
    note_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class NotesUpdateParams(TypedDict):
    """Parameters for notes.update operation"""
    properties: NotesUpdateParamsProperties
    note_id: str

class NotesDeleteParams(TypedDict):
    """Parameters for notes.delete operation"""
    note_id: str

class CallsListParams(TypedDict):
    """Parameters for calls.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class CallsCreateParams(TypedDict):
    """Parameters for calls.create operation"""
    properties: CallsCreateParamsProperties
    associations: NotRequired[list[CallsCreateParamsAssociationsItem]]

class CallsGetParams(TypedDict):
    """Parameters for calls.get operation"""
    call_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class CallsUpdateParams(TypedDict):
    """Parameters for calls.update operation"""
    properties: CallsUpdateParamsProperties
    call_id: str

class CallsDeleteParams(TypedDict):
    """Parameters for calls.delete operation"""
    call_id: str

class EmailsListParams(TypedDict):
    """Parameters for emails.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class EmailsCreateParams(TypedDict):
    """Parameters for emails.create operation"""
    properties: EmailsCreateParamsProperties
    associations: NotRequired[list[EmailsCreateParamsAssociationsItem]]

class EmailsGetParams(TypedDict):
    """Parameters for emails.get operation"""
    email_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class EmailsUpdateParams(TypedDict):
    """Parameters for emails.update operation"""
    properties: EmailsUpdateParamsProperties
    email_id: str

class EmailsDeleteParams(TypedDict):
    """Parameters for emails.delete operation"""
    email_id: str

class MeetingsListParams(TypedDict):
    """Parameters for meetings.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class MeetingsCreateParams(TypedDict):
    """Parameters for meetings.create operation"""
    properties: MeetingsCreateParamsProperties
    associations: NotRequired[list[MeetingsCreateParamsAssociationsItem]]

class MeetingsGetParams(TypedDict):
    """Parameters for meetings.get operation"""
    meeting_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class MeetingsUpdateParams(TypedDict):
    """Parameters for meetings.update operation"""
    properties: MeetingsUpdateParamsProperties
    meeting_id: str

class MeetingsDeleteParams(TypedDict):
    """Parameters for meetings.delete operation"""
    meeting_id: str

class TasksListParams(TypedDict):
    """Parameters for tasks.list operation"""
    limit: NotRequired[int]
    after: NotRequired[str]
    associations: NotRequired[str]
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    archived: NotRequired[bool]

class TasksCreateParams(TypedDict):
    """Parameters for tasks.create operation"""
    properties: TasksCreateParamsProperties
    associations: NotRequired[list[TasksCreateParamsAssociationsItem]]

class TasksGetParams(TypedDict):
    """Parameters for tasks.get operation"""
    task_id: str
    properties: NotRequired[str]
    properties_with_history: NotRequired[str]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    archived: NotRequired[bool]

class TasksUpdateParams(TypedDict):
    """Parameters for tasks.update operation"""
    properties: TasksUpdateParamsProperties
    task_id: str

class TasksDeleteParams(TypedDict):
    """Parameters for tasks.delete operation"""
    task_id: str

class SchemasListParams(TypedDict):
    """Parameters for schemas.list operation"""
    archived: NotRequired[bool]

class SchemasGetParams(TypedDict):
    """Parameters for schemas.get operation"""
    object_type: str

class ObjectsListParams(TypedDict):
    """Parameters for objects.list operation"""
    object_type: str
    limit: NotRequired[int]
    after: NotRequired[str]
    properties: NotRequired[str]
    archived: NotRequired[bool]
    associations: NotRequired[str]
    properties_with_history: NotRequired[str]

class ObjectsGetParams(TypedDict):
    """Parameters for objects.get operation"""
    object_type: str
    object_id: str
    properties: NotRequired[str]
    archived: NotRequired[bool]
    associations: NotRequired[str]
    id_property: NotRequired[str]
    properties_with_history: NotRequired[str]

class AssociationsListParams(TypedDict):
    """Parameters for associations.list operation"""
    from_object_type: str
    from_object_id: str
    to_object_type: str
    after: NotRequired[str]
    limit: NotRequired[int]

class AssociationsCreateParams(TypedDict):
    """Parameters for associations.create operation"""
    association_category: str
    association_type_id: int
    from_object_type: str
    from_object_id: str
    to_object_type: str
    to_object_id: str

class AssociationsDeleteParams(TypedDict):
    """Parameters for associations.delete operation"""
    from_object_type: str
    from_object_id: str
    to_object_type: str
    to_object_id: str

# ===== SEARCH TYPES =====

# Sort specification
AirbyteSortOrder = Literal["asc", "desc"]

# ===== COMPANIES SEARCH TYPES =====

class CompaniesSearchFilter(TypedDict, total=False):
    """Available fields for filtering companies search queries."""
    archived: bool | None
    """Indicates whether the company has been deleted and moved to the recycling bin"""
    contacts: list[Any] | None
    """Associated contact records linked to this company"""
    created_at: str | None
    """Timestamp when the company record was created"""
    id: str | None
    """Unique identifier for the company record"""
    properties: dict[str, Any]
    """Object containing all property values for the company"""
    properties_createdate: str | None
    """Date the company was created"""
    properties_domain: str | None
    """Company domain name"""
    properties_hs_lastmodifieddate: str | None
    """Last modified date of the company"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hubspot_owner_id: str | None
    """ID of the HubSpot owner assigned to this company"""
    properties_name: str | None
    """Company name"""
    updated_at: str | None
    """Timestamp when the company record was last modified"""


class CompaniesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates whether the company has been deleted and moved to the recycling bin"""
    contacts: list[list[Any]]
    """Associated contact records linked to this company"""
    created_at: list[str]
    """Timestamp when the company record was created"""
    id: list[str]
    """Unique identifier for the company record"""
    properties: list[dict[str, Any]]
    """Object containing all property values for the company"""
    properties_createdate: list[str]
    """Date the company was created"""
    properties_domain: list[str]
    """Company domain name"""
    properties_hs_lastmodifieddate: list[str]
    """Last modified date of the company"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hubspot_owner_id: list[str]
    """ID of the HubSpot owner assigned to this company"""
    properties_name: list[str]
    """Company name"""
    updated_at: list[str]
    """Timestamp when the company record was last modified"""


class CompaniesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates whether the company has been deleted and moved to the recycling bin"""
    contacts: Any
    """Associated contact records linked to this company"""
    created_at: Any
    """Timestamp when the company record was created"""
    id: Any
    """Unique identifier for the company record"""
    properties: Any
    """Object containing all property values for the company"""
    properties_createdate: Any
    """Date the company was created"""
    properties_domain: Any
    """Company domain name"""
    properties_hs_lastmodifieddate: Any
    """Last modified date of the company"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hubspot_owner_id: Any
    """ID of the HubSpot owner assigned to this company"""
    properties_name: Any
    """Company name"""
    updated_at: Any
    """Timestamp when the company record was last modified"""


class CompaniesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates whether the company has been deleted and moved to the recycling bin"""
    contacts: str
    """Associated contact records linked to this company"""
    created_at: str
    """Timestamp when the company record was created"""
    id: str
    """Unique identifier for the company record"""
    properties: str
    """Object containing all property values for the company"""
    properties_createdate: str
    """Date the company was created"""
    properties_domain: str
    """Company domain name"""
    properties_hs_lastmodifieddate: str
    """Last modified date of the company"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hubspot_owner_id: str
    """ID of the HubSpot owner assigned to this company"""
    properties_name: str
    """Company name"""
    updated_at: str
    """Timestamp when the company record was last modified"""


class CompaniesSortFilter(TypedDict, total=False):
    """Available fields for sorting companies search results."""
    archived: AirbyteSortOrder
    """Indicates whether the company has been deleted and moved to the recycling bin"""
    contacts: AirbyteSortOrder
    """Associated contact records linked to this company"""
    created_at: AirbyteSortOrder
    """Timestamp when the company record was created"""
    id: AirbyteSortOrder
    """Unique identifier for the company record"""
    properties: AirbyteSortOrder
    """Object containing all property values for the company"""
    properties_createdate: AirbyteSortOrder
    """Date the company was created"""
    properties_domain: AirbyteSortOrder
    """Company domain name"""
    properties_hs_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the company"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hubspot_owner_id: AirbyteSortOrder
    """ID of the HubSpot owner assigned to this company"""
    properties_name: AirbyteSortOrder
    """Company name"""
    updated_at: AirbyteSortOrder
    """Timestamp when the company record was last modified"""


# Entity-specific condition types for companies
class CompaniesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CompaniesSearchFilter


class CompaniesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CompaniesSearchFilter


class CompaniesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CompaniesSearchFilter


class CompaniesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CompaniesSearchFilter


class CompaniesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CompaniesSearchFilter


class CompaniesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CompaniesSearchFilter


class CompaniesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CompaniesStringFilter


class CompaniesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CompaniesStringFilter


class CompaniesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CompaniesStringFilter


class CompaniesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CompaniesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CompaniesInCondition = TypedDict("CompaniesInCondition", {"in": CompaniesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CompaniesNotCondition = TypedDict("CompaniesNotCondition", {"not": "CompaniesCondition"}, total=False)
"""Negates the nested condition."""

CompaniesAndCondition = TypedDict("CompaniesAndCondition", {"and": "list[CompaniesCondition]"}, total=False)
"""True if all nested conditions are true."""

CompaniesOrCondition = TypedDict("CompaniesOrCondition", {"or": "list[CompaniesCondition]"}, total=False)
"""True if any nested condition is true."""

CompaniesAnyCondition = TypedDict("CompaniesAnyCondition", {"any": CompaniesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all companies condition types
CompaniesCondition = (
    CompaniesEqCondition
    | CompaniesNeqCondition
    | CompaniesGtCondition
    | CompaniesGteCondition
    | CompaniesLtCondition
    | CompaniesLteCondition
    | CompaniesInCondition
    | CompaniesLikeCondition
    | CompaniesFuzzyCondition
    | CompaniesKeywordCondition
    | CompaniesContainsCondition
    | CompaniesNotCondition
    | CompaniesAndCondition
    | CompaniesOrCondition
    | CompaniesAnyCondition
)


class CompaniesSearchQuery(TypedDict, total=False):
    """Search query for companies entity."""
    filter: CompaniesCondition
    sort: list[CompaniesSortFilter]


# ===== CONTACTS SEARCH TYPES =====

class ContactsSearchFilter(TypedDict, total=False):
    """Available fields for filtering contacts search queries."""
    archived: bool | None
    """Boolean flag indicating whether the contact has been archived or deleted"""
    companies: list[Any] | None
    """Associated company records linked to this contact"""
    created_at: str | None
    """Timestamp indicating when the contact was first created in the system"""
    id: str | None
    """Unique identifier for the contact record"""
    properties: dict[str, Any]
    """Key-value object storing all contact properties and their values."""
    properties_associatedcompanyid: str | None
    """ID of the associated company"""
    properties_createdate: str | None
    """Date the contact was created"""
    properties_email: str | None
    """Contact email address"""
    properties_firstname: str | None
    """Contact first name"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hubspot_owner_id: str | None
    """ID of the HubSpot owner assigned to this contact"""
    properties_lastmodifieddate: str | None
    """Last modified date of the contact"""
    properties_lastname: str | None
    """Contact last name"""
    updated_at: str | None
    """Timestamp indicating when the contact record was last modified"""


class ContactsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Boolean flag indicating whether the contact has been archived or deleted"""
    companies: list[list[Any]]
    """Associated company records linked to this contact"""
    created_at: list[str]
    """Timestamp indicating when the contact was first created in the system"""
    id: list[str]
    """Unique identifier for the contact record"""
    properties: list[dict[str, Any]]
    """Key-value object storing all contact properties and their values."""
    properties_associatedcompanyid: list[str]
    """ID of the associated company"""
    properties_createdate: list[str]
    """Date the contact was created"""
    properties_email: list[str]
    """Contact email address"""
    properties_firstname: list[str]
    """Contact first name"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hubspot_owner_id: list[str]
    """ID of the HubSpot owner assigned to this contact"""
    properties_lastmodifieddate: list[str]
    """Last modified date of the contact"""
    properties_lastname: list[str]
    """Contact last name"""
    updated_at: list[str]
    """Timestamp indicating when the contact record was last modified"""


class ContactsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Boolean flag indicating whether the contact has been archived or deleted"""
    companies: Any
    """Associated company records linked to this contact"""
    created_at: Any
    """Timestamp indicating when the contact was first created in the system"""
    id: Any
    """Unique identifier for the contact record"""
    properties: Any
    """Key-value object storing all contact properties and their values."""
    properties_associatedcompanyid: Any
    """ID of the associated company"""
    properties_createdate: Any
    """Date the contact was created"""
    properties_email: Any
    """Contact email address"""
    properties_firstname: Any
    """Contact first name"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hubspot_owner_id: Any
    """ID of the HubSpot owner assigned to this contact"""
    properties_lastmodifieddate: Any
    """Last modified date of the contact"""
    properties_lastname: Any
    """Contact last name"""
    updated_at: Any
    """Timestamp indicating when the contact record was last modified"""


class ContactsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Boolean flag indicating whether the contact has been archived or deleted"""
    companies: str
    """Associated company records linked to this contact"""
    created_at: str
    """Timestamp indicating when the contact was first created in the system"""
    id: str
    """Unique identifier for the contact record"""
    properties: str
    """Key-value object storing all contact properties and their values."""
    properties_associatedcompanyid: str
    """ID of the associated company"""
    properties_createdate: str
    """Date the contact was created"""
    properties_email: str
    """Contact email address"""
    properties_firstname: str
    """Contact first name"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hubspot_owner_id: str
    """ID of the HubSpot owner assigned to this contact"""
    properties_lastmodifieddate: str
    """Last modified date of the contact"""
    properties_lastname: str
    """Contact last name"""
    updated_at: str
    """Timestamp indicating when the contact record was last modified"""


class ContactsSortFilter(TypedDict, total=False):
    """Available fields for sorting contacts search results."""
    archived: AirbyteSortOrder
    """Boolean flag indicating whether the contact has been archived or deleted"""
    companies: AirbyteSortOrder
    """Associated company records linked to this contact"""
    created_at: AirbyteSortOrder
    """Timestamp indicating when the contact was first created in the system"""
    id: AirbyteSortOrder
    """Unique identifier for the contact record"""
    properties: AirbyteSortOrder
    """Key-value object storing all contact properties and their values."""
    properties_associatedcompanyid: AirbyteSortOrder
    """ID of the associated company"""
    properties_createdate: AirbyteSortOrder
    """Date the contact was created"""
    properties_email: AirbyteSortOrder
    """Contact email address"""
    properties_firstname: AirbyteSortOrder
    """Contact first name"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hubspot_owner_id: AirbyteSortOrder
    """ID of the HubSpot owner assigned to this contact"""
    properties_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the contact"""
    properties_lastname: AirbyteSortOrder
    """Contact last name"""
    updated_at: AirbyteSortOrder
    """Timestamp indicating when the contact record was last modified"""


# Entity-specific condition types for contacts
class ContactsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: ContactsSearchFilter


class ContactsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: ContactsSearchFilter


class ContactsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: ContactsSearchFilter


class ContactsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: ContactsSearchFilter


class ContactsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: ContactsSearchFilter


class ContactsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: ContactsSearchFilter


class ContactsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: ContactsStringFilter


class ContactsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: ContactsStringFilter


class ContactsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: ContactsStringFilter


class ContactsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: ContactsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
ContactsInCondition = TypedDict("ContactsInCondition", {"in": ContactsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

ContactsNotCondition = TypedDict("ContactsNotCondition", {"not": "ContactsCondition"}, total=False)
"""Negates the nested condition."""

ContactsAndCondition = TypedDict("ContactsAndCondition", {"and": "list[ContactsCondition]"}, total=False)
"""True if all nested conditions are true."""

ContactsOrCondition = TypedDict("ContactsOrCondition", {"or": "list[ContactsCondition]"}, total=False)
"""True if any nested condition is true."""

ContactsAnyCondition = TypedDict("ContactsAnyCondition", {"any": ContactsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all contacts condition types
ContactsCondition = (
    ContactsEqCondition
    | ContactsNeqCondition
    | ContactsGtCondition
    | ContactsGteCondition
    | ContactsLtCondition
    | ContactsLteCondition
    | ContactsInCondition
    | ContactsLikeCondition
    | ContactsFuzzyCondition
    | ContactsKeywordCondition
    | ContactsContainsCondition
    | ContactsNotCondition
    | ContactsAndCondition
    | ContactsOrCondition
    | ContactsAnyCondition
)


class ContactsSearchQuery(TypedDict, total=False):
    """Search query for contacts entity."""
    filter: ContactsCondition
    sort: list[ContactsSortFilter]


# ===== DEALS SEARCH TYPES =====

class DealsSearchFilter(TypedDict, total=False):
    """Available fields for filtering deals search queries."""
    archived: bool | None
    """Indicates whether the deal has been deleted and moved to the recycling bin"""
    companies: list[Any] | None
    """Collection of company records associated with the deal"""
    contacts: list[Any] | None
    """Collection of contact records associated with the deal"""
    created_at: str | None
    """Timestamp when the deal record was originally created"""
    id: str | None
    """Unique identifier for the deal record"""
    line_items: list[Any] | None
    """Collection of product line items associated with the deal"""
    properties: dict[str, Any]
    """Key-value object containing all deal properties and custom fields"""
    properties_amount: str | None
    """Deal amount"""
    properties_closedate: str | None
    """Expected close date of the deal"""
    properties_createdate: str | None
    """Date the deal was created"""
    properties_dealname: str | None
    """Deal name"""
    properties_dealstage: str | None
    """Current deal stage"""
    properties_hs_lastmodifieddate: str | None
    """Last modified date of the deal"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hubspot_owner_id: str | None
    """ID of the HubSpot owner assigned to this deal"""
    properties_pipeline: str | None
    """Deal pipeline"""
    updated_at: str | None
    """Timestamp when the deal record was last modified"""


class DealsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates whether the deal has been deleted and moved to the recycling bin"""
    companies: list[list[Any]]
    """Collection of company records associated with the deal"""
    contacts: list[list[Any]]
    """Collection of contact records associated with the deal"""
    created_at: list[str]
    """Timestamp when the deal record was originally created"""
    id: list[str]
    """Unique identifier for the deal record"""
    line_items: list[list[Any]]
    """Collection of product line items associated with the deal"""
    properties: list[dict[str, Any]]
    """Key-value object containing all deal properties and custom fields"""
    properties_amount: list[str]
    """Deal amount"""
    properties_closedate: list[str]
    """Expected close date of the deal"""
    properties_createdate: list[str]
    """Date the deal was created"""
    properties_dealname: list[str]
    """Deal name"""
    properties_dealstage: list[str]
    """Current deal stage"""
    properties_hs_lastmodifieddate: list[str]
    """Last modified date of the deal"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hubspot_owner_id: list[str]
    """ID of the HubSpot owner assigned to this deal"""
    properties_pipeline: list[str]
    """Deal pipeline"""
    updated_at: list[str]
    """Timestamp when the deal record was last modified"""


class DealsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates whether the deal has been deleted and moved to the recycling bin"""
    companies: Any
    """Collection of company records associated with the deal"""
    contacts: Any
    """Collection of contact records associated with the deal"""
    created_at: Any
    """Timestamp when the deal record was originally created"""
    id: Any
    """Unique identifier for the deal record"""
    line_items: Any
    """Collection of product line items associated with the deal"""
    properties: Any
    """Key-value object containing all deal properties and custom fields"""
    properties_amount: Any
    """Deal amount"""
    properties_closedate: Any
    """Expected close date of the deal"""
    properties_createdate: Any
    """Date the deal was created"""
    properties_dealname: Any
    """Deal name"""
    properties_dealstage: Any
    """Current deal stage"""
    properties_hs_lastmodifieddate: Any
    """Last modified date of the deal"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hubspot_owner_id: Any
    """ID of the HubSpot owner assigned to this deal"""
    properties_pipeline: Any
    """Deal pipeline"""
    updated_at: Any
    """Timestamp when the deal record was last modified"""


class DealsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates whether the deal has been deleted and moved to the recycling bin"""
    companies: str
    """Collection of company records associated with the deal"""
    contacts: str
    """Collection of contact records associated with the deal"""
    created_at: str
    """Timestamp when the deal record was originally created"""
    id: str
    """Unique identifier for the deal record"""
    line_items: str
    """Collection of product line items associated with the deal"""
    properties: str
    """Key-value object containing all deal properties and custom fields"""
    properties_amount: str
    """Deal amount"""
    properties_closedate: str
    """Expected close date of the deal"""
    properties_createdate: str
    """Date the deal was created"""
    properties_dealname: str
    """Deal name"""
    properties_dealstage: str
    """Current deal stage"""
    properties_hs_lastmodifieddate: str
    """Last modified date of the deal"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hubspot_owner_id: str
    """ID of the HubSpot owner assigned to this deal"""
    properties_pipeline: str
    """Deal pipeline"""
    updated_at: str
    """Timestamp when the deal record was last modified"""


class DealsSortFilter(TypedDict, total=False):
    """Available fields for sorting deals search results."""
    archived: AirbyteSortOrder
    """Indicates whether the deal has been deleted and moved to the recycling bin"""
    companies: AirbyteSortOrder
    """Collection of company records associated with the deal"""
    contacts: AirbyteSortOrder
    """Collection of contact records associated with the deal"""
    created_at: AirbyteSortOrder
    """Timestamp when the deal record was originally created"""
    id: AirbyteSortOrder
    """Unique identifier for the deal record"""
    line_items: AirbyteSortOrder
    """Collection of product line items associated with the deal"""
    properties: AirbyteSortOrder
    """Key-value object containing all deal properties and custom fields"""
    properties_amount: AirbyteSortOrder
    """Deal amount"""
    properties_closedate: AirbyteSortOrder
    """Expected close date of the deal"""
    properties_createdate: AirbyteSortOrder
    """Date the deal was created"""
    properties_dealname: AirbyteSortOrder
    """Deal name"""
    properties_dealstage: AirbyteSortOrder
    """Current deal stage"""
    properties_hs_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the deal"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hubspot_owner_id: AirbyteSortOrder
    """ID of the HubSpot owner assigned to this deal"""
    properties_pipeline: AirbyteSortOrder
    """Deal pipeline"""
    updated_at: AirbyteSortOrder
    """Timestamp when the deal record was last modified"""


# Entity-specific condition types for deals
class DealsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: DealsSearchFilter


class DealsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: DealsSearchFilter


class DealsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: DealsSearchFilter


class DealsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: DealsSearchFilter


class DealsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: DealsSearchFilter


class DealsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: DealsSearchFilter


class DealsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: DealsStringFilter


class DealsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: DealsStringFilter


class DealsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: DealsStringFilter


class DealsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: DealsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
DealsInCondition = TypedDict("DealsInCondition", {"in": DealsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

DealsNotCondition = TypedDict("DealsNotCondition", {"not": "DealsCondition"}, total=False)
"""Negates the nested condition."""

DealsAndCondition = TypedDict("DealsAndCondition", {"and": "list[DealsCondition]"}, total=False)
"""True if all nested conditions are true."""

DealsOrCondition = TypedDict("DealsOrCondition", {"or": "list[DealsCondition]"}, total=False)
"""True if any nested condition is true."""

DealsAnyCondition = TypedDict("DealsAnyCondition", {"any": DealsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all deals condition types
DealsCondition = (
    DealsEqCondition
    | DealsNeqCondition
    | DealsGtCondition
    | DealsGteCondition
    | DealsLtCondition
    | DealsLteCondition
    | DealsInCondition
    | DealsLikeCondition
    | DealsFuzzyCondition
    | DealsKeywordCondition
    | DealsContainsCondition
    | DealsNotCondition
    | DealsAndCondition
    | DealsOrCondition
    | DealsAnyCondition
)


class DealsSearchQuery(TypedDict, total=False):
    """Search query for deals entity."""
    filter: DealsCondition
    sort: list[DealsSortFilter]


# ===== TICKETS SEARCH TYPES =====

class TicketsSearchFilter(TypedDict, total=False):
    """Available fields for filtering tickets search queries."""
    archived: bool | None
    """Indicates whether the ticket has been deleted and moved to the recycling bin"""
    companies: list[Any] | None
    """Collection of company records associated with the ticket"""
    contacts: list[Any] | None
    """Collection of contact records associated with the ticket"""
    created_at: str | None
    """Timestamp when the ticket record was originally created"""
    id: str | None
    """Unique identifier for the ticket record"""
    properties: dict[str, Any]
    """Object containing all property values for the ticket"""
    properties_content: str | None
    """Ticket content/description"""
    properties_createdate: str | None
    """Date the ticket was created"""
    properties_hs_lastmodifieddate: str | None
    """Last modified date of the ticket"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hs_pipeline: str | None
    """Ticket pipeline"""
    properties_hs_pipeline_stage: str | None
    """Current pipeline stage of the ticket"""
    properties_hs_ticket_category: str | None
    """Ticket category"""
    properties_hs_ticket_priority: str | None
    """Ticket priority level"""
    properties_subject: str | None
    """Ticket subject line"""
    updated_at: str | None
    """Timestamp when the ticket record was last modified"""


class TicketsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates whether the ticket has been deleted and moved to the recycling bin"""
    companies: list[list[Any]]
    """Collection of company records associated with the ticket"""
    contacts: list[list[Any]]
    """Collection of contact records associated with the ticket"""
    created_at: list[str]
    """Timestamp when the ticket record was originally created"""
    id: list[str]
    """Unique identifier for the ticket record"""
    properties: list[dict[str, Any]]
    """Object containing all property values for the ticket"""
    properties_content: list[str]
    """Ticket content/description"""
    properties_createdate: list[str]
    """Date the ticket was created"""
    properties_hs_lastmodifieddate: list[str]
    """Last modified date of the ticket"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hs_pipeline: list[str]
    """Ticket pipeline"""
    properties_hs_pipeline_stage: list[str]
    """Current pipeline stage of the ticket"""
    properties_hs_ticket_category: list[str]
    """Ticket category"""
    properties_hs_ticket_priority: list[str]
    """Ticket priority level"""
    properties_subject: list[str]
    """Ticket subject line"""
    updated_at: list[str]
    """Timestamp when the ticket record was last modified"""


class TicketsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates whether the ticket has been deleted and moved to the recycling bin"""
    companies: Any
    """Collection of company records associated with the ticket"""
    contacts: Any
    """Collection of contact records associated with the ticket"""
    created_at: Any
    """Timestamp when the ticket record was originally created"""
    id: Any
    """Unique identifier for the ticket record"""
    properties: Any
    """Object containing all property values for the ticket"""
    properties_content: Any
    """Ticket content/description"""
    properties_createdate: Any
    """Date the ticket was created"""
    properties_hs_lastmodifieddate: Any
    """Last modified date of the ticket"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hs_pipeline: Any
    """Ticket pipeline"""
    properties_hs_pipeline_stage: Any
    """Current pipeline stage of the ticket"""
    properties_hs_ticket_category: Any
    """Ticket category"""
    properties_hs_ticket_priority: Any
    """Ticket priority level"""
    properties_subject: Any
    """Ticket subject line"""
    updated_at: Any
    """Timestamp when the ticket record was last modified"""


class TicketsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates whether the ticket has been deleted and moved to the recycling bin"""
    companies: str
    """Collection of company records associated with the ticket"""
    contacts: str
    """Collection of contact records associated with the ticket"""
    created_at: str
    """Timestamp when the ticket record was originally created"""
    id: str
    """Unique identifier for the ticket record"""
    properties: str
    """Object containing all property values for the ticket"""
    properties_content: str
    """Ticket content/description"""
    properties_createdate: str
    """Date the ticket was created"""
    properties_hs_lastmodifieddate: str
    """Last modified date of the ticket"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hs_pipeline: str
    """Ticket pipeline"""
    properties_hs_pipeline_stage: str
    """Current pipeline stage of the ticket"""
    properties_hs_ticket_category: str
    """Ticket category"""
    properties_hs_ticket_priority: str
    """Ticket priority level"""
    properties_subject: str
    """Ticket subject line"""
    updated_at: str
    """Timestamp when the ticket record was last modified"""


class TicketsSortFilter(TypedDict, total=False):
    """Available fields for sorting tickets search results."""
    archived: AirbyteSortOrder
    """Indicates whether the ticket has been deleted and moved to the recycling bin"""
    companies: AirbyteSortOrder
    """Collection of company records associated with the ticket"""
    contacts: AirbyteSortOrder
    """Collection of contact records associated with the ticket"""
    created_at: AirbyteSortOrder
    """Timestamp when the ticket record was originally created"""
    id: AirbyteSortOrder
    """Unique identifier for the ticket record"""
    properties: AirbyteSortOrder
    """Object containing all property values for the ticket"""
    properties_content: AirbyteSortOrder
    """Ticket content/description"""
    properties_createdate: AirbyteSortOrder
    """Date the ticket was created"""
    properties_hs_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the ticket"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hs_pipeline: AirbyteSortOrder
    """Ticket pipeline"""
    properties_hs_pipeline_stage: AirbyteSortOrder
    """Current pipeline stage of the ticket"""
    properties_hs_ticket_category: AirbyteSortOrder
    """Ticket category"""
    properties_hs_ticket_priority: AirbyteSortOrder
    """Ticket priority level"""
    properties_subject: AirbyteSortOrder
    """Ticket subject line"""
    updated_at: AirbyteSortOrder
    """Timestamp when the ticket record was last modified"""


# Entity-specific condition types for tickets
class TicketsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TicketsSearchFilter


class TicketsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TicketsSearchFilter


class TicketsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TicketsSearchFilter


class TicketsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TicketsSearchFilter


class TicketsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TicketsSearchFilter


class TicketsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TicketsSearchFilter


class TicketsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TicketsStringFilter


class TicketsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TicketsStringFilter


class TicketsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TicketsStringFilter


class TicketsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TicketsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TicketsInCondition = TypedDict("TicketsInCondition", {"in": TicketsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TicketsNotCondition = TypedDict("TicketsNotCondition", {"not": "TicketsCondition"}, total=False)
"""Negates the nested condition."""

TicketsAndCondition = TypedDict("TicketsAndCondition", {"and": "list[TicketsCondition]"}, total=False)
"""True if all nested conditions are true."""

TicketsOrCondition = TypedDict("TicketsOrCondition", {"or": "list[TicketsCondition]"}, total=False)
"""True if any nested condition is true."""

TicketsAnyCondition = TypedDict("TicketsAnyCondition", {"any": TicketsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tickets condition types
TicketsCondition = (
    TicketsEqCondition
    | TicketsNeqCondition
    | TicketsGtCondition
    | TicketsGteCondition
    | TicketsLtCondition
    | TicketsLteCondition
    | TicketsInCondition
    | TicketsLikeCondition
    | TicketsFuzzyCondition
    | TicketsKeywordCondition
    | TicketsContainsCondition
    | TicketsNotCondition
    | TicketsAndCondition
    | TicketsOrCondition
    | TicketsAnyCondition
)


class TicketsSearchQuery(TypedDict, total=False):
    """Search query for tickets entity."""
    filter: TicketsCondition
    sort: list[TicketsSortFilter]


# ===== NOTES SEARCH TYPES =====

class NotesSearchFilter(TypedDict, total=False):
    """Available fields for filtering notes search queries."""
    archived: bool | None
    """Indicates whether the note has been archived"""
    created_at: str | None
    """Timestamp when the note was created"""
    id: str | None
    """Unique identifier for the note record"""
    properties: dict[str, Any]
    """Object containing all property values for the note"""
    properties_hs_createdate: str | None
    """Date the note was created"""
    properties_hs_lastmodifieddate: str | None
    """Last modified date of the note"""
    properties_hs_note_body: str | None
    """The body content of the note (supports HTML)"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hs_timestamp: str | None
    """Timestamp when the note activity occurred"""
    properties_hubspot_owner_id: str | None
    """ID of the note owner"""
    updated_at: str | None
    """Timestamp when the note record was last modified"""


class NotesInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates whether the note has been archived"""
    created_at: list[str]
    """Timestamp when the note was created"""
    id: list[str]
    """Unique identifier for the note record"""
    properties: list[dict[str, Any]]
    """Object containing all property values for the note"""
    properties_hs_createdate: list[str]
    """Date the note was created"""
    properties_hs_lastmodifieddate: list[str]
    """Last modified date of the note"""
    properties_hs_note_body: list[str]
    """The body content of the note (supports HTML)"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hs_timestamp: list[str]
    """Timestamp when the note activity occurred"""
    properties_hubspot_owner_id: list[str]
    """ID of the note owner"""
    updated_at: list[str]
    """Timestamp when the note record was last modified"""


class NotesAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates whether the note has been archived"""
    created_at: Any
    """Timestamp when the note was created"""
    id: Any
    """Unique identifier for the note record"""
    properties: Any
    """Object containing all property values for the note"""
    properties_hs_createdate: Any
    """Date the note was created"""
    properties_hs_lastmodifieddate: Any
    """Last modified date of the note"""
    properties_hs_note_body: Any
    """The body content of the note (supports HTML)"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hs_timestamp: Any
    """Timestamp when the note activity occurred"""
    properties_hubspot_owner_id: Any
    """ID of the note owner"""
    updated_at: Any
    """Timestamp when the note record was last modified"""


class NotesStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates whether the note has been archived"""
    created_at: str
    """Timestamp when the note was created"""
    id: str
    """Unique identifier for the note record"""
    properties: str
    """Object containing all property values for the note"""
    properties_hs_createdate: str
    """Date the note was created"""
    properties_hs_lastmodifieddate: str
    """Last modified date of the note"""
    properties_hs_note_body: str
    """The body content of the note (supports HTML)"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hs_timestamp: str
    """Timestamp when the note activity occurred"""
    properties_hubspot_owner_id: str
    """ID of the note owner"""
    updated_at: str
    """Timestamp when the note record was last modified"""


class NotesSortFilter(TypedDict, total=False):
    """Available fields for sorting notes search results."""
    archived: AirbyteSortOrder
    """Indicates whether the note has been archived"""
    created_at: AirbyteSortOrder
    """Timestamp when the note was created"""
    id: AirbyteSortOrder
    """Unique identifier for the note record"""
    properties: AirbyteSortOrder
    """Object containing all property values for the note"""
    properties_hs_createdate: AirbyteSortOrder
    """Date the note was created"""
    properties_hs_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the note"""
    properties_hs_note_body: AirbyteSortOrder
    """The body content of the note (supports HTML)"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hs_timestamp: AirbyteSortOrder
    """Timestamp when the note activity occurred"""
    properties_hubspot_owner_id: AirbyteSortOrder
    """ID of the note owner"""
    updated_at: AirbyteSortOrder
    """Timestamp when the note record was last modified"""


# Entity-specific condition types for notes
class NotesEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: NotesSearchFilter


class NotesNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: NotesSearchFilter


class NotesGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: NotesSearchFilter


class NotesGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: NotesSearchFilter


class NotesLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: NotesSearchFilter


class NotesLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: NotesSearchFilter


class NotesLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: NotesStringFilter


class NotesFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: NotesStringFilter


class NotesKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: NotesStringFilter


class NotesContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: NotesAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
NotesInCondition = TypedDict("NotesInCondition", {"in": NotesInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

NotesNotCondition = TypedDict("NotesNotCondition", {"not": "NotesCondition"}, total=False)
"""Negates the nested condition."""

NotesAndCondition = TypedDict("NotesAndCondition", {"and": "list[NotesCondition]"}, total=False)
"""True if all nested conditions are true."""

NotesOrCondition = TypedDict("NotesOrCondition", {"or": "list[NotesCondition]"}, total=False)
"""True if any nested condition is true."""

NotesAnyCondition = TypedDict("NotesAnyCondition", {"any": NotesAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all notes condition types
NotesCondition = (
    NotesEqCondition
    | NotesNeqCondition
    | NotesGtCondition
    | NotesGteCondition
    | NotesLtCondition
    | NotesLteCondition
    | NotesInCondition
    | NotesLikeCondition
    | NotesFuzzyCondition
    | NotesKeywordCondition
    | NotesContainsCondition
    | NotesNotCondition
    | NotesAndCondition
    | NotesOrCondition
    | NotesAnyCondition
)


class NotesSearchQuery(TypedDict, total=False):
    """Search query for notes entity."""
    filter: NotesCondition
    sort: list[NotesSortFilter]


# ===== CALLS SEARCH TYPES =====

class CallsSearchFilter(TypedDict, total=False):
    """Available fields for filtering calls search queries."""
    archived: bool | None
    """Indicates whether the call has been archived"""
    created_at: str | None
    """Timestamp when the call was created"""
    id: str | None
    """Unique identifier for the call record"""
    properties: dict[str, Any]
    """Object containing all property values for the call"""
    properties_hs_call_body: str | None
    """Description or notes about the call"""
    properties_hs_call_direction: str | None
    """Direction of the call (INBOUND or OUTBOUND)"""
    properties_hs_call_duration: str | None
    """Duration of the call in milliseconds"""
    properties_hs_call_status: str | None
    """Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER)"""
    properties_hs_call_title: str | None
    """Title or subject of the call"""
    properties_hs_createdate: str | None
    """Date the call was created"""
    properties_hs_lastmodifieddate: str | None
    """Last modified date of the call"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hs_timestamp: str | None
    """Timestamp when the call activity occurred"""
    properties_hubspot_owner_id: str | None
    """ID of the call owner"""
    updated_at: str | None
    """Timestamp when the call record was last modified"""


class CallsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates whether the call has been archived"""
    created_at: list[str]
    """Timestamp when the call was created"""
    id: list[str]
    """Unique identifier for the call record"""
    properties: list[dict[str, Any]]
    """Object containing all property values for the call"""
    properties_hs_call_body: list[str]
    """Description or notes about the call"""
    properties_hs_call_direction: list[str]
    """Direction of the call (INBOUND or OUTBOUND)"""
    properties_hs_call_duration: list[str]
    """Duration of the call in milliseconds"""
    properties_hs_call_status: list[str]
    """Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER)"""
    properties_hs_call_title: list[str]
    """Title or subject of the call"""
    properties_hs_createdate: list[str]
    """Date the call was created"""
    properties_hs_lastmodifieddate: list[str]
    """Last modified date of the call"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hs_timestamp: list[str]
    """Timestamp when the call activity occurred"""
    properties_hubspot_owner_id: list[str]
    """ID of the call owner"""
    updated_at: list[str]
    """Timestamp when the call record was last modified"""


class CallsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates whether the call has been archived"""
    created_at: Any
    """Timestamp when the call was created"""
    id: Any
    """Unique identifier for the call record"""
    properties: Any
    """Object containing all property values for the call"""
    properties_hs_call_body: Any
    """Description or notes about the call"""
    properties_hs_call_direction: Any
    """Direction of the call (INBOUND or OUTBOUND)"""
    properties_hs_call_duration: Any
    """Duration of the call in milliseconds"""
    properties_hs_call_status: Any
    """Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER)"""
    properties_hs_call_title: Any
    """Title or subject of the call"""
    properties_hs_createdate: Any
    """Date the call was created"""
    properties_hs_lastmodifieddate: Any
    """Last modified date of the call"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hs_timestamp: Any
    """Timestamp when the call activity occurred"""
    properties_hubspot_owner_id: Any
    """ID of the call owner"""
    updated_at: Any
    """Timestamp when the call record was last modified"""


class CallsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates whether the call has been archived"""
    created_at: str
    """Timestamp when the call was created"""
    id: str
    """Unique identifier for the call record"""
    properties: str
    """Object containing all property values for the call"""
    properties_hs_call_body: str
    """Description or notes about the call"""
    properties_hs_call_direction: str
    """Direction of the call (INBOUND or OUTBOUND)"""
    properties_hs_call_duration: str
    """Duration of the call in milliseconds"""
    properties_hs_call_status: str
    """Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER)"""
    properties_hs_call_title: str
    """Title or subject of the call"""
    properties_hs_createdate: str
    """Date the call was created"""
    properties_hs_lastmodifieddate: str
    """Last modified date of the call"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hs_timestamp: str
    """Timestamp when the call activity occurred"""
    properties_hubspot_owner_id: str
    """ID of the call owner"""
    updated_at: str
    """Timestamp when the call record was last modified"""


class CallsSortFilter(TypedDict, total=False):
    """Available fields for sorting calls search results."""
    archived: AirbyteSortOrder
    """Indicates whether the call has been archived"""
    created_at: AirbyteSortOrder
    """Timestamp when the call was created"""
    id: AirbyteSortOrder
    """Unique identifier for the call record"""
    properties: AirbyteSortOrder
    """Object containing all property values for the call"""
    properties_hs_call_body: AirbyteSortOrder
    """Description or notes about the call"""
    properties_hs_call_direction: AirbyteSortOrder
    """Direction of the call (INBOUND or OUTBOUND)"""
    properties_hs_call_duration: AirbyteSortOrder
    """Duration of the call in milliseconds"""
    properties_hs_call_status: AirbyteSortOrder
    """Status of the call (e.g., COMPLETED, BUSY, NO_ANSWER)"""
    properties_hs_call_title: AirbyteSortOrder
    """Title or subject of the call"""
    properties_hs_createdate: AirbyteSortOrder
    """Date the call was created"""
    properties_hs_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the call"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hs_timestamp: AirbyteSortOrder
    """Timestamp when the call activity occurred"""
    properties_hubspot_owner_id: AirbyteSortOrder
    """ID of the call owner"""
    updated_at: AirbyteSortOrder
    """Timestamp when the call record was last modified"""


# Entity-specific condition types for calls
class CallsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: CallsSearchFilter


class CallsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: CallsSearchFilter


class CallsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: CallsSearchFilter


class CallsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: CallsSearchFilter


class CallsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: CallsSearchFilter


class CallsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: CallsSearchFilter


class CallsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: CallsStringFilter


class CallsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: CallsStringFilter


class CallsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: CallsStringFilter


class CallsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: CallsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
CallsInCondition = TypedDict("CallsInCondition", {"in": CallsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

CallsNotCondition = TypedDict("CallsNotCondition", {"not": "CallsCondition"}, total=False)
"""Negates the nested condition."""

CallsAndCondition = TypedDict("CallsAndCondition", {"and": "list[CallsCondition]"}, total=False)
"""True if all nested conditions are true."""

CallsOrCondition = TypedDict("CallsOrCondition", {"or": "list[CallsCondition]"}, total=False)
"""True if any nested condition is true."""

CallsAnyCondition = TypedDict("CallsAnyCondition", {"any": CallsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all calls condition types
CallsCondition = (
    CallsEqCondition
    | CallsNeqCondition
    | CallsGtCondition
    | CallsGteCondition
    | CallsLtCondition
    | CallsLteCondition
    | CallsInCondition
    | CallsLikeCondition
    | CallsFuzzyCondition
    | CallsKeywordCondition
    | CallsContainsCondition
    | CallsNotCondition
    | CallsAndCondition
    | CallsOrCondition
    | CallsAnyCondition
)


class CallsSearchQuery(TypedDict, total=False):
    """Search query for calls entity."""
    filter: CallsCondition
    sort: list[CallsSortFilter]


# ===== EMAILS SEARCH TYPES =====

class EmailsSearchFilter(TypedDict, total=False):
    """Available fields for filtering emails search queries."""
    archived: bool | None
    """Indicates whether the email has been archived"""
    created_at: str | None
    """Timestamp when the email was created"""
    id: str | None
    """Unique identifier for the email record"""
    properties: dict[str, Any]
    """Object containing all property values for the email"""
    properties_hs_createdate: str | None
    """Date the email was created"""
    properties_hs_email_direction: str | None
    """Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)"""
    properties_hs_email_status: str | None
    """Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)"""
    properties_hs_email_subject: str | None
    """Subject line of the email"""
    properties_hs_email_text: str | None
    """Plain text body of the email"""
    properties_hs_lastmodifieddate: str | None
    """Last modified date of the email"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hs_timestamp: str | None
    """Timestamp when the email activity occurred"""
    properties_hubspot_owner_id: str | None
    """ID of the email owner"""
    updated_at: str | None
    """Timestamp when the email record was last modified"""


class EmailsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates whether the email has been archived"""
    created_at: list[str]
    """Timestamp when the email was created"""
    id: list[str]
    """Unique identifier for the email record"""
    properties: list[dict[str, Any]]
    """Object containing all property values for the email"""
    properties_hs_createdate: list[str]
    """Date the email was created"""
    properties_hs_email_direction: list[str]
    """Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)"""
    properties_hs_email_status: list[str]
    """Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)"""
    properties_hs_email_subject: list[str]
    """Subject line of the email"""
    properties_hs_email_text: list[str]
    """Plain text body of the email"""
    properties_hs_lastmodifieddate: list[str]
    """Last modified date of the email"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hs_timestamp: list[str]
    """Timestamp when the email activity occurred"""
    properties_hubspot_owner_id: list[str]
    """ID of the email owner"""
    updated_at: list[str]
    """Timestamp when the email record was last modified"""


class EmailsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates whether the email has been archived"""
    created_at: Any
    """Timestamp when the email was created"""
    id: Any
    """Unique identifier for the email record"""
    properties: Any
    """Object containing all property values for the email"""
    properties_hs_createdate: Any
    """Date the email was created"""
    properties_hs_email_direction: Any
    """Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)"""
    properties_hs_email_status: Any
    """Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)"""
    properties_hs_email_subject: Any
    """Subject line of the email"""
    properties_hs_email_text: Any
    """Plain text body of the email"""
    properties_hs_lastmodifieddate: Any
    """Last modified date of the email"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hs_timestamp: Any
    """Timestamp when the email activity occurred"""
    properties_hubspot_owner_id: Any
    """ID of the email owner"""
    updated_at: Any
    """Timestamp when the email record was last modified"""


class EmailsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates whether the email has been archived"""
    created_at: str
    """Timestamp when the email was created"""
    id: str
    """Unique identifier for the email record"""
    properties: str
    """Object containing all property values for the email"""
    properties_hs_createdate: str
    """Date the email was created"""
    properties_hs_email_direction: str
    """Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)"""
    properties_hs_email_status: str
    """Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)"""
    properties_hs_email_subject: str
    """Subject line of the email"""
    properties_hs_email_text: str
    """Plain text body of the email"""
    properties_hs_lastmodifieddate: str
    """Last modified date of the email"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hs_timestamp: str
    """Timestamp when the email activity occurred"""
    properties_hubspot_owner_id: str
    """ID of the email owner"""
    updated_at: str
    """Timestamp when the email record was last modified"""


class EmailsSortFilter(TypedDict, total=False):
    """Available fields for sorting emails search results."""
    archived: AirbyteSortOrder
    """Indicates whether the email has been archived"""
    created_at: AirbyteSortOrder
    """Timestamp when the email was created"""
    id: AirbyteSortOrder
    """Unique identifier for the email record"""
    properties: AirbyteSortOrder
    """Object containing all property values for the email"""
    properties_hs_createdate: AirbyteSortOrder
    """Date the email was created"""
    properties_hs_email_direction: AirbyteSortOrder
    """Direction of the email (EMAIL, INCOMING_EMAIL, FORWARDED_EMAIL)"""
    properties_hs_email_status: AirbyteSortOrder
    """Status of the email (BOUNCED, FAILED, SCHEDULED, SENDING, SENT, DRAFT)"""
    properties_hs_email_subject: AirbyteSortOrder
    """Subject line of the email"""
    properties_hs_email_text: AirbyteSortOrder
    """Plain text body of the email"""
    properties_hs_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the email"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hs_timestamp: AirbyteSortOrder
    """Timestamp when the email activity occurred"""
    properties_hubspot_owner_id: AirbyteSortOrder
    """ID of the email owner"""
    updated_at: AirbyteSortOrder
    """Timestamp when the email record was last modified"""


# Entity-specific condition types for emails
class EmailsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: EmailsSearchFilter


class EmailsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: EmailsSearchFilter


class EmailsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: EmailsSearchFilter


class EmailsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: EmailsSearchFilter


class EmailsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: EmailsSearchFilter


class EmailsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: EmailsSearchFilter


class EmailsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: EmailsStringFilter


class EmailsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: EmailsStringFilter


class EmailsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: EmailsStringFilter


class EmailsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: EmailsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
EmailsInCondition = TypedDict("EmailsInCondition", {"in": EmailsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

EmailsNotCondition = TypedDict("EmailsNotCondition", {"not": "EmailsCondition"}, total=False)
"""Negates the nested condition."""

EmailsAndCondition = TypedDict("EmailsAndCondition", {"and": "list[EmailsCondition]"}, total=False)
"""True if all nested conditions are true."""

EmailsOrCondition = TypedDict("EmailsOrCondition", {"or": "list[EmailsCondition]"}, total=False)
"""True if any nested condition is true."""

EmailsAnyCondition = TypedDict("EmailsAnyCondition", {"any": EmailsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all emails condition types
EmailsCondition = (
    EmailsEqCondition
    | EmailsNeqCondition
    | EmailsGtCondition
    | EmailsGteCondition
    | EmailsLtCondition
    | EmailsLteCondition
    | EmailsInCondition
    | EmailsLikeCondition
    | EmailsFuzzyCondition
    | EmailsKeywordCondition
    | EmailsContainsCondition
    | EmailsNotCondition
    | EmailsAndCondition
    | EmailsOrCondition
    | EmailsAnyCondition
)


class EmailsSearchQuery(TypedDict, total=False):
    """Search query for emails entity."""
    filter: EmailsCondition
    sort: list[EmailsSortFilter]


# ===== MEETINGS SEARCH TYPES =====

class MeetingsSearchFilter(TypedDict, total=False):
    """Available fields for filtering meetings search queries."""
    archived: bool | None
    """Indicates whether the meeting has been archived"""
    created_at: str | None
    """Timestamp when the meeting was created"""
    id: str | None
    """Unique identifier for the meeting record"""
    properties: dict[str, Any]
    """Object containing all property values for the meeting"""
    properties_hs_createdate: str | None
    """Date the meeting was created"""
    properties_hs_lastmodifieddate: str | None
    """Last modified date of the meeting"""
    properties_hs_meeting_body: str | None
    """Description or notes about the meeting"""
    properties_hs_meeting_end_time: str | None
    """End time of the meeting"""
    properties_hs_meeting_location: str | None
    """Location of the meeting"""
    properties_hs_meeting_outcome: str | None
    """Outcome of the meeting (e.g., SCHEDULED, COMPLETED, NO_SHOW, CANCELED)"""
    properties_hs_meeting_start_time: str | None
    """Start time of the meeting"""
    properties_hs_meeting_title: str | None
    """Title of the meeting"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hs_timestamp: str | None
    """Timestamp when the meeting activity occurred"""
    properties_hubspot_owner_id: str | None
    """ID of the meeting owner"""
    updated_at: str | None
    """Timestamp when the meeting record was last modified"""


class MeetingsInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates whether the meeting has been archived"""
    created_at: list[str]
    """Timestamp when the meeting was created"""
    id: list[str]
    """Unique identifier for the meeting record"""
    properties: list[dict[str, Any]]
    """Object containing all property values for the meeting"""
    properties_hs_createdate: list[str]
    """Date the meeting was created"""
    properties_hs_lastmodifieddate: list[str]
    """Last modified date of the meeting"""
    properties_hs_meeting_body: list[str]
    """Description or notes about the meeting"""
    properties_hs_meeting_end_time: list[str]
    """End time of the meeting"""
    properties_hs_meeting_location: list[str]
    """Location of the meeting"""
    properties_hs_meeting_outcome: list[str]
    """Outcome of the meeting (e.g., SCHEDULED, COMPLETED, NO_SHOW, CANCELED)"""
    properties_hs_meeting_start_time: list[str]
    """Start time of the meeting"""
    properties_hs_meeting_title: list[str]
    """Title of the meeting"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hs_timestamp: list[str]
    """Timestamp when the meeting activity occurred"""
    properties_hubspot_owner_id: list[str]
    """ID of the meeting owner"""
    updated_at: list[str]
    """Timestamp when the meeting record was last modified"""


class MeetingsAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates whether the meeting has been archived"""
    created_at: Any
    """Timestamp when the meeting was created"""
    id: Any
    """Unique identifier for the meeting record"""
    properties: Any
    """Object containing all property values for the meeting"""
    properties_hs_createdate: Any
    """Date the meeting was created"""
    properties_hs_lastmodifieddate: Any
    """Last modified date of the meeting"""
    properties_hs_meeting_body: Any
    """Description or notes about the meeting"""
    properties_hs_meeting_end_time: Any
    """End time of the meeting"""
    properties_hs_meeting_location: Any
    """Location of the meeting"""
    properties_hs_meeting_outcome: Any
    """Outcome of the meeting (e.g., SCHEDULED, COMPLETED, NO_SHOW, CANCELED)"""
    properties_hs_meeting_start_time: Any
    """Start time of the meeting"""
    properties_hs_meeting_title: Any
    """Title of the meeting"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hs_timestamp: Any
    """Timestamp when the meeting activity occurred"""
    properties_hubspot_owner_id: Any
    """ID of the meeting owner"""
    updated_at: Any
    """Timestamp when the meeting record was last modified"""


class MeetingsStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates whether the meeting has been archived"""
    created_at: str
    """Timestamp when the meeting was created"""
    id: str
    """Unique identifier for the meeting record"""
    properties: str
    """Object containing all property values for the meeting"""
    properties_hs_createdate: str
    """Date the meeting was created"""
    properties_hs_lastmodifieddate: str
    """Last modified date of the meeting"""
    properties_hs_meeting_body: str
    """Description or notes about the meeting"""
    properties_hs_meeting_end_time: str
    """End time of the meeting"""
    properties_hs_meeting_location: str
    """Location of the meeting"""
    properties_hs_meeting_outcome: str
    """Outcome of the meeting (e.g., SCHEDULED, COMPLETED, NO_SHOW, CANCELED)"""
    properties_hs_meeting_start_time: str
    """Start time of the meeting"""
    properties_hs_meeting_title: str
    """Title of the meeting"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hs_timestamp: str
    """Timestamp when the meeting activity occurred"""
    properties_hubspot_owner_id: str
    """ID of the meeting owner"""
    updated_at: str
    """Timestamp when the meeting record was last modified"""


class MeetingsSortFilter(TypedDict, total=False):
    """Available fields for sorting meetings search results."""
    archived: AirbyteSortOrder
    """Indicates whether the meeting has been archived"""
    created_at: AirbyteSortOrder
    """Timestamp when the meeting was created"""
    id: AirbyteSortOrder
    """Unique identifier for the meeting record"""
    properties: AirbyteSortOrder
    """Object containing all property values for the meeting"""
    properties_hs_createdate: AirbyteSortOrder
    """Date the meeting was created"""
    properties_hs_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the meeting"""
    properties_hs_meeting_body: AirbyteSortOrder
    """Description or notes about the meeting"""
    properties_hs_meeting_end_time: AirbyteSortOrder
    """End time of the meeting"""
    properties_hs_meeting_location: AirbyteSortOrder
    """Location of the meeting"""
    properties_hs_meeting_outcome: AirbyteSortOrder
    """Outcome of the meeting (e.g., SCHEDULED, COMPLETED, NO_SHOW, CANCELED)"""
    properties_hs_meeting_start_time: AirbyteSortOrder
    """Start time of the meeting"""
    properties_hs_meeting_title: AirbyteSortOrder
    """Title of the meeting"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hs_timestamp: AirbyteSortOrder
    """Timestamp when the meeting activity occurred"""
    properties_hubspot_owner_id: AirbyteSortOrder
    """ID of the meeting owner"""
    updated_at: AirbyteSortOrder
    """Timestamp when the meeting record was last modified"""


# Entity-specific condition types for meetings
class MeetingsEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: MeetingsSearchFilter


class MeetingsNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: MeetingsSearchFilter


class MeetingsGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: MeetingsSearchFilter


class MeetingsGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: MeetingsSearchFilter


class MeetingsLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: MeetingsSearchFilter


class MeetingsLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: MeetingsSearchFilter


class MeetingsLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: MeetingsStringFilter


class MeetingsFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: MeetingsStringFilter


class MeetingsKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: MeetingsStringFilter


class MeetingsContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: MeetingsAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
MeetingsInCondition = TypedDict("MeetingsInCondition", {"in": MeetingsInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

MeetingsNotCondition = TypedDict("MeetingsNotCondition", {"not": "MeetingsCondition"}, total=False)
"""Negates the nested condition."""

MeetingsAndCondition = TypedDict("MeetingsAndCondition", {"and": "list[MeetingsCondition]"}, total=False)
"""True if all nested conditions are true."""

MeetingsOrCondition = TypedDict("MeetingsOrCondition", {"or": "list[MeetingsCondition]"}, total=False)
"""True if any nested condition is true."""

MeetingsAnyCondition = TypedDict("MeetingsAnyCondition", {"any": MeetingsAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all meetings condition types
MeetingsCondition = (
    MeetingsEqCondition
    | MeetingsNeqCondition
    | MeetingsGtCondition
    | MeetingsGteCondition
    | MeetingsLtCondition
    | MeetingsLteCondition
    | MeetingsInCondition
    | MeetingsLikeCondition
    | MeetingsFuzzyCondition
    | MeetingsKeywordCondition
    | MeetingsContainsCondition
    | MeetingsNotCondition
    | MeetingsAndCondition
    | MeetingsOrCondition
    | MeetingsAnyCondition
)


class MeetingsSearchQuery(TypedDict, total=False):
    """Search query for meetings entity."""
    filter: MeetingsCondition
    sort: list[MeetingsSortFilter]


# ===== TASKS SEARCH TYPES =====

class TasksSearchFilter(TypedDict, total=False):
    """Available fields for filtering tasks search queries."""
    archived: bool | None
    """Indicates whether the task has been archived"""
    created_at: str | None
    """Timestamp when the task was created"""
    id: str | None
    """Unique identifier for the task record"""
    properties: dict[str, Any]
    """Object containing all property values for the task"""
    properties_hs_createdate: str | None
    """Date the task was created"""
    properties_hs_lastmodifieddate: str | None
    """Last modified date of the task"""
    properties_hs_object_id: str | None
    """HubSpot object ID"""
    properties_hs_task_body: str | None
    """Description or notes for the task"""
    properties_hs_task_priority: str | None
    """Priority of the task (LOW, MEDIUM, HIGH)"""
    properties_hs_task_status: str | None
    """Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)"""
    properties_hs_task_subject: str | None
    """Subject or title of the task"""
    properties_hs_task_type: str | None
    """Type of the task (TODO, CALL, EMAIL)"""
    properties_hs_timestamp: str | None
    """Due date / timestamp for the task"""
    properties_hubspot_owner_id: str | None
    """ID of the task owner"""
    updated_at: str | None
    """Timestamp when the task record was last modified"""


class TasksInFilter(TypedDict, total=False):
    """Available fields for 'in' condition (values are lists)."""
    archived: list[bool]
    """Indicates whether the task has been archived"""
    created_at: list[str]
    """Timestamp when the task was created"""
    id: list[str]
    """Unique identifier for the task record"""
    properties: list[dict[str, Any]]
    """Object containing all property values for the task"""
    properties_hs_createdate: list[str]
    """Date the task was created"""
    properties_hs_lastmodifieddate: list[str]
    """Last modified date of the task"""
    properties_hs_object_id: list[str]
    """HubSpot object ID"""
    properties_hs_task_body: list[str]
    """Description or notes for the task"""
    properties_hs_task_priority: list[str]
    """Priority of the task (LOW, MEDIUM, HIGH)"""
    properties_hs_task_status: list[str]
    """Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)"""
    properties_hs_task_subject: list[str]
    """Subject or title of the task"""
    properties_hs_task_type: list[str]
    """Type of the task (TODO, CALL, EMAIL)"""
    properties_hs_timestamp: list[str]
    """Due date / timestamp for the task"""
    properties_hubspot_owner_id: list[str]
    """ID of the task owner"""
    updated_at: list[str]
    """Timestamp when the task record was last modified"""


class TasksAnyValueFilter(TypedDict, total=False):
    """Available fields with Any value type. Used for 'contains' and 'any' conditions."""
    archived: Any
    """Indicates whether the task has been archived"""
    created_at: Any
    """Timestamp when the task was created"""
    id: Any
    """Unique identifier for the task record"""
    properties: Any
    """Object containing all property values for the task"""
    properties_hs_createdate: Any
    """Date the task was created"""
    properties_hs_lastmodifieddate: Any
    """Last modified date of the task"""
    properties_hs_object_id: Any
    """HubSpot object ID"""
    properties_hs_task_body: Any
    """Description or notes for the task"""
    properties_hs_task_priority: Any
    """Priority of the task (LOW, MEDIUM, HIGH)"""
    properties_hs_task_status: Any
    """Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)"""
    properties_hs_task_subject: Any
    """Subject or title of the task"""
    properties_hs_task_type: Any
    """Type of the task (TODO, CALL, EMAIL)"""
    properties_hs_timestamp: Any
    """Due date / timestamp for the task"""
    properties_hubspot_owner_id: Any
    """ID of the task owner"""
    updated_at: Any
    """Timestamp when the task record was last modified"""


class TasksStringFilter(TypedDict, total=False):
    """String fields for text search conditions (like, fuzzy, keyword)."""
    archived: str
    """Indicates whether the task has been archived"""
    created_at: str
    """Timestamp when the task was created"""
    id: str
    """Unique identifier for the task record"""
    properties: str
    """Object containing all property values for the task"""
    properties_hs_createdate: str
    """Date the task was created"""
    properties_hs_lastmodifieddate: str
    """Last modified date of the task"""
    properties_hs_object_id: str
    """HubSpot object ID"""
    properties_hs_task_body: str
    """Description or notes for the task"""
    properties_hs_task_priority: str
    """Priority of the task (LOW, MEDIUM, HIGH)"""
    properties_hs_task_status: str
    """Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)"""
    properties_hs_task_subject: str
    """Subject or title of the task"""
    properties_hs_task_type: str
    """Type of the task (TODO, CALL, EMAIL)"""
    properties_hs_timestamp: str
    """Due date / timestamp for the task"""
    properties_hubspot_owner_id: str
    """ID of the task owner"""
    updated_at: str
    """Timestamp when the task record was last modified"""


class TasksSortFilter(TypedDict, total=False):
    """Available fields for sorting tasks search results."""
    archived: AirbyteSortOrder
    """Indicates whether the task has been archived"""
    created_at: AirbyteSortOrder
    """Timestamp when the task was created"""
    id: AirbyteSortOrder
    """Unique identifier for the task record"""
    properties: AirbyteSortOrder
    """Object containing all property values for the task"""
    properties_hs_createdate: AirbyteSortOrder
    """Date the task was created"""
    properties_hs_lastmodifieddate: AirbyteSortOrder
    """Last modified date of the task"""
    properties_hs_object_id: AirbyteSortOrder
    """HubSpot object ID"""
    properties_hs_task_body: AirbyteSortOrder
    """Description or notes for the task"""
    properties_hs_task_priority: AirbyteSortOrder
    """Priority of the task (LOW, MEDIUM, HIGH)"""
    properties_hs_task_status: AirbyteSortOrder
    """Status of the task (NOT_STARTED, IN_PROGRESS, WAITING, COMPLETED, DEFERRED)"""
    properties_hs_task_subject: AirbyteSortOrder
    """Subject or title of the task"""
    properties_hs_task_type: AirbyteSortOrder
    """Type of the task (TODO, CALL, EMAIL)"""
    properties_hs_timestamp: AirbyteSortOrder
    """Due date / timestamp for the task"""
    properties_hubspot_owner_id: AirbyteSortOrder
    """ID of the task owner"""
    updated_at: AirbyteSortOrder
    """Timestamp when the task record was last modified"""


# Entity-specific condition types for tasks
class TasksEqCondition(TypedDict, total=False):
    """Equal to: field equals value."""
    eq: TasksSearchFilter


class TasksNeqCondition(TypedDict, total=False):
    """Not equal to: field does not equal value."""
    neq: TasksSearchFilter


class TasksGtCondition(TypedDict, total=False):
    """Greater than: field > value."""
    gt: TasksSearchFilter


class TasksGteCondition(TypedDict, total=False):
    """Greater than or equal: field >= value."""
    gte: TasksSearchFilter


class TasksLtCondition(TypedDict, total=False):
    """Less than: field < value."""
    lt: TasksSearchFilter


class TasksLteCondition(TypedDict, total=False):
    """Less than or equal: field <= value."""
    lte: TasksSearchFilter


class TasksLikeCondition(TypedDict, total=False):
    """Partial string match with % wildcards."""
    like: TasksStringFilter


class TasksFuzzyCondition(TypedDict, total=False):
    """Ordered word text match (case-insensitive)."""
    fuzzy: TasksStringFilter


class TasksKeywordCondition(TypedDict, total=False):
    """Keyword text match (any word present)."""
    keyword: TasksStringFilter


class TasksContainsCondition(TypedDict, total=False):
    """Check if value exists in array field. Example: {"contains": {"tags": "premium"}}"""
    contains: TasksAnyValueFilter


# Reserved keyword conditions using functional TypedDict syntax
TasksInCondition = TypedDict("TasksInCondition", {"in": TasksInFilter}, total=False)
"""In list: field value is in list. Example: {"in": {"status": ["active", "pending"]}}"""

TasksNotCondition = TypedDict("TasksNotCondition", {"not": "TasksCondition"}, total=False)
"""Negates the nested condition."""

TasksAndCondition = TypedDict("TasksAndCondition", {"and": "list[TasksCondition]"}, total=False)
"""True if all nested conditions are true."""

TasksOrCondition = TypedDict("TasksOrCondition", {"or": "list[TasksCondition]"}, total=False)
"""True if any nested condition is true."""

TasksAnyCondition = TypedDict("TasksAnyCondition", {"any": TasksAnyValueFilter}, total=False)
"""Match if ANY element in array field matches nested condition. Example: {"any": {"addresses": {"eq": {"state": "CA"}}}}"""

# Union of all tasks condition types
TasksCondition = (
    TasksEqCondition
    | TasksNeqCondition
    | TasksGtCondition
    | TasksGteCondition
    | TasksLtCondition
    | TasksLteCondition
    | TasksInCondition
    | TasksLikeCondition
    | TasksFuzzyCondition
    | TasksKeywordCondition
    | TasksContainsCondition
    | TasksNotCondition
    | TasksAndCondition
    | TasksOrCondition
    | TasksAnyCondition
)


class TasksSearchQuery(TypedDict, total=False):
    """Search query for tasks entity."""
    filter: TasksCondition
    sort: list[TasksSortFilter]



# ===== SEARCH PARAMS =====

class AirbyteSearchParams(TypedDict, total=False):
    """Parameters for Airbyte cache search operations (generic, use entity-specific query types for better type hints)."""
    query: dict[str, Any]
    limit: int
    cursor: str
    fields: list[list[str]]
