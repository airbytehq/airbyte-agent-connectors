"""
Pydantic models for incident-io connector.

This module contains Pydantic models used for authentication configuration
and response envelope types.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import TypeVar, Generic, Union, Any

# Authentication configuration

class IncidentIoAuthConfig(BaseModel):
    """API Key Authentication"""

    model_config = ConfigDict(extra="forbid")

    api_key: str
    """Your incident.io API key. Create one at https://app.incident.io/settings/api-keys"""

# ===== RESPONSE TYPE DEFINITIONS (PYDANTIC) =====

class PaginationMeta(BaseModel):
    """Cursor-based pagination metadata"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    after: Union[str | None, Any] = Field(default=None)
    page_size: Union[int | None, Any] = Field(default=None)

class IncidentSeverity(BaseModel):
    """Severity of the incident"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    rank: Union[float | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class IncidentCreatorUser(BaseModel):
    """Nested schema for IncidentCreator.user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)
    slack_user_id: Union[str | None, Any] = Field(default=None)

class IncidentCreator(BaseModel):
    """The user who created the incident"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user: Union[IncidentCreatorUser | None, Any] = Field(default=None)

class IncidentIncidentRoleAssignmentsItemAssignee(BaseModel):
    """Nested schema for IncidentIncidentRoleAssignmentsItem.assignee"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)
    slack_user_id: Union[str | None, Any] = Field(default=None)

class IncidentIncidentRoleAssignmentsItemRole(BaseModel):
    """Nested schema for IncidentIncidentRoleAssignmentsItem.role"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    instructions: Union[str | None, Any] = Field(default=None)
    required: Union[bool | None, Any] = Field(default=None)
    role_type: Union[str | None, Any] = Field(default=None)
    shortform: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class IncidentIncidentRoleAssignmentsItem(BaseModel):
    """Nested schema for Incident.incident_role_assignments_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assignee: Union[IncidentIncidentRoleAssignmentsItemAssignee | None, Any] = Field(default=None)
    role: Union[IncidentIncidentRoleAssignmentsItemRole | None, Any] = Field(default=None)

class IncidentCustomFieldEntriesItemCustomField(BaseModel):
    """Nested schema for IncidentCustomFieldEntriesItem.custom_field"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    field_type: Union[str | None, Any] = Field(default=None)
    options: Union[list[Any] | None, Any] = Field(default=None)

class IncidentCustomFieldEntriesItem(BaseModel):
    """Nested schema for Incident.custom_field_entries_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    custom_field: Union[IncidentCustomFieldEntriesItemCustomField | None, Any] = Field(default=None)
    values: Union[list[Any] | None, Any] = Field(default=None)

class IncidentIncidentType(BaseModel):
    """Type of the incident"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    create_in_triage: Union[str | None, Any] = Field(default=None)
    is_default: Union[bool | None, Any] = Field(default=None)
    private_incidents_only: Union[bool | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class IncidentIncidentTimestampValuesItemValue(BaseModel):
    """Nested schema for IncidentIncidentTimestampValuesItem.value"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: Union[str | None, Any] = Field(default=None)

class IncidentIncidentTimestampValuesItemIncidentTimestamp(BaseModel):
    """Nested schema for IncidentIncidentTimestampValuesItem.incident_timestamp"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    rank: Union[float | None, Any] = Field(default=None)

class IncidentIncidentTimestampValuesItem(BaseModel):
    """Nested schema for Incident.incident_timestamp_values_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    incident_timestamp: Union[IncidentIncidentTimestampValuesItemIncidentTimestamp | None, Any] = Field(default=None)
    value: Union[IncidentIncidentTimestampValuesItemValue | None, Any] = Field(default=None)

class IncidentDurationMetricsItemDurationMetric(BaseModel):
    """Nested schema for IncidentDurationMetricsItem.duration_metric"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class IncidentDurationMetricsItem(BaseModel):
    """Nested schema for Incident.duration_metrics_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    duration_metric: Union[IncidentDurationMetricsItemDurationMetric | None, Any] = Field(default=None)

class IncidentIncidentStatus(BaseModel):
    """Current status of the incident"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    category: Union[str | None, Any] = Field(default=None)
    rank: Union[float | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class Incident(BaseModel):
    """An incident tracked in incident.io"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    reference: Union[str | None, Any] = Field(default=None)
    summary: Union[str | None, Any] = Field(default=None)
    mode: Union[str | None, Any] = Field(default=None)
    visibility: Union[str | None, Any] = Field(default=None)
    permalink: Union[str | None, Any] = Field(default=None)
    call_url: Union[str | None, Any] = Field(default=None)
    slack_channel_id: Union[str | None, Any] = Field(default=None)
    slack_channel_name: Union[str | None, Any] = Field(default=None)
    slack_team_id: Union[str | None, Any] = Field(default=None)
    has_debrief: Union[bool | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    creator: Union[IncidentCreator | None, Any] = Field(default=None)
    incident_status: Union[IncidentIncidentStatus | None, Any] = Field(default=None)
    severity: Union[IncidentSeverity | None, Any] = Field(default=None)
    incident_type: Union[IncidentIncidentType | None, Any] = Field(default=None)
    incident_role_assignments: Union[list[IncidentIncidentRoleAssignmentsItem] | None, Any] = Field(default=None)
    custom_field_entries: Union[list[IncidentCustomFieldEntriesItem] | None, Any] = Field(default=None)
    duration_metrics: Union[list[IncidentDurationMetricsItem] | None, Any] = Field(default=None)
    incident_timestamp_values: Union[list[IncidentIncidentTimestampValuesItem] | None, Any] = Field(default=None)
    workload_minutes_late: Union[float | None, Any] = Field(default=None)
    workload_minutes_sleeping: Union[float | None, Any] = Field(default=None)
    workload_minutes_total: Union[float | None, Any] = Field(default=None)
    workload_minutes_working: Union[float | None, Any] = Field(default=None)

class AlertAttributesItemAttribute(BaseModel):
    """Nested schema for AlertAttributesItem.attribute"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    array: Union[bool | None, Any] = Field(default=None)

class AlertAttributesItemValueCatalogEntry(BaseModel):
    """Nested schema for AlertAttributesItemValue.catalog_entry"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    catalog_type_id: Union[str | None, Any] = Field(default=None)

class AlertAttributesItemValue(BaseModel):
    """Nested schema for AlertAttributesItem.value"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    literal: Union[str | None, Any] = Field(default=None)
    label: Union[str | None, Any] = Field(default=None)
    catalog_entry: Union[AlertAttributesItemValueCatalogEntry | None, Any] = Field(default=None)

class AlertAttributesItem(BaseModel):
    """Nested schema for Alert.attributes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    attribute: Union[AlertAttributesItemAttribute | None, Any] = Field(default=None)
    value: Union[AlertAttributesItemValue | None, Any] = Field(default=None)

class Alert(BaseModel):
    """An alert ingested from an alert source"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    alert_source_id: Union[str | None, Any] = Field(default=None)
    deduplication_key: Union[str | None, Any] = Field(default=None)
    source_url: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    resolved_at: Union[str | None, Any] = Field(default=None)
    attributes: Union[list[AlertAttributesItem] | None, Any] = Field(default=None)

class EscalationCreatorAlert(BaseModel):
    """Nested schema for EscalationCreator.alert"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)

class EscalationCreatorWorkflow(BaseModel):
    """Nested schema for EscalationCreator.workflow"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class EscalationCreatorUser(BaseModel):
    """Nested schema for EscalationCreator.user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)
    slack_user_id: Union[str | None, Any] = Field(default=None)

class EscalationCreator(BaseModel):
    """The creator of this escalation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    alert: Union[EscalationCreatorAlert | None, Any] = Field(default=None)
    user: Union[EscalationCreatorUser | None, Any] = Field(default=None)
    workflow: Union[EscalationCreatorWorkflow | None, Any] = Field(default=None)

class EscalationRelatedIncidentsItem(BaseModel):
    """Nested schema for Escalation.related_incidents_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    reference: Union[str | None, Any] = Field(default=None)
    summary: Union[str | None, Any] = Field(default=None)
    external_id: Union[int | None, Any] = Field(default=None)
    status_category: Union[str | None, Any] = Field(default=None)
    visibility: Union[str | None, Any] = Field(default=None)

class EscalationRelatedAlertsItem(BaseModel):
    """Nested schema for Escalation.related_alerts_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    alert_source_id: Union[str | None, Any] = Field(default=None)
    deduplication_key: Union[str | None, Any] = Field(default=None)
    source_url: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    resolved_at: Union[str | None, Any] = Field(default=None)

class EscalationEventsItemUsersItem(BaseModel):
    """Nested schema for EscalationEventsItem.users_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)
    slack_user_id: Union[str | None, Any] = Field(default=None)

class EscalationEventsItemChannelsItem(BaseModel):
    """Nested schema for EscalationEventsItem.channels_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    slack_channel_id: Union[str | None, Any] = Field(default=None)
    slack_team_id: Union[str | None, Any] = Field(default=None)
    microsoft_teams_channel_id: Union[str | None, Any] = Field(default=None)
    microsoft_teams_team_id: Union[str | None, Any] = Field(default=None)

class EscalationEventsItem(BaseModel):
    """Nested schema for Escalation.events_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    event: Union[str | None, Any] = Field(default=None)
    occurred_at: Union[str | None, Any] = Field(default=None)
    urgency: Union[str | None, Any] = Field(default=None)
    users: Union[list[EscalationEventsItemUsersItem] | None, Any] = Field(default=None)
    channels: Union[list[EscalationEventsItemChannelsItem] | None, Any] = Field(default=None)

class EscalationPriority(BaseModel):
    """Priority of the escalation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Union[str | None, Any] = Field(default=None)

class Escalation(BaseModel):
    """An escalation that pages people via escalation paths"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    title: Union[str | None, Any] = Field(default=None)
    status: Union[str | None, Any] = Field(default=None)
    escalation_path_id: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    creator: Union[EscalationCreator | None, Any] = Field(default=None)
    priority: Union[EscalationPriority | None, Any] = Field(default=None)
    events: Union[list[EscalationEventsItem] | None, Any] = Field(default=None)
    related_incidents: Union[list[EscalationRelatedIncidentsItem] | None, Any] = Field(default=None)
    related_alerts: Union[list[EscalationRelatedAlertsItem] | None, Any] = Field(default=None)

class UserBaseRole(BaseModel):
    """Base role assigned to the user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    slug: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)

class User(BaseModel):
    """A user in the incident.io organisation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)
    slack_user_id: Union[str | None, Any] = Field(default=None)
    base_role: Union[UserBaseRole | None, Any] = Field(default=None)
    custom_roles: Union[list[Any] | None, Any] = Field(default=None)

class IncidentUpdateNewSeverity(BaseModel):
    """New severity set by this update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    rank: Union[float | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class IncidentUpdateNewIncidentStatus(BaseModel):
    """New incident status set by this update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    category: Union[str | None, Any] = Field(default=None)
    rank: Union[float | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class IncidentUpdateUpdaterUser(BaseModel):
    """Nested schema for IncidentUpdateUpdater.user"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    email: Union[str | None, Any] = Field(default=None)
    role: Union[str | None, Any] = Field(default=None)
    slack_user_id: Union[str | None, Any] = Field(default=None)

class IncidentUpdateUpdater(BaseModel):
    """Who made this update"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    user: Union[IncidentUpdateUpdaterUser | None, Any] = Field(default=None)

class IncidentUpdate(BaseModel):
    """An update posted to an incident"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    incident_id: Union[str | None, Any] = Field(default=None)
    message: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    new_incident_status: Union[IncidentUpdateNewIncidentStatus | None, Any] = Field(default=None)
    new_severity: Union[IncidentUpdateNewSeverity | None, Any] = Field(default=None)
    updater: Union[IncidentUpdateUpdater | None, Any] = Field(default=None)

class IncidentRole(BaseModel):
    """A role that can be assigned during an incident"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    instructions: Union[str | None, Any] = Field(default=None)
    shortform: Union[str | None, Any] = Field(default=None)
    role_type: Union[str | None, Any] = Field(default=None)
    required: Union[bool | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class IncidentStatus(BaseModel):
    """A status that an incident can be in"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    category: Union[str | None, Any] = Field(default=None)
    rank: Union[float | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class IncidentTimestamp(BaseModel):
    """A timestamp definition for incidents"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    rank: Union[float | None, Any] = Field(default=None)

class Severity(BaseModel):
    """A severity level for incidents"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    rank: Union[float | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class CustomField(BaseModel):
    """A custom field definition for incidents"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    field_type: Union[str | None, Any] = Field(default=None)
    catalog_type_id: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)

class CatalogTypeSchemaAttributesItem(BaseModel):
    """Nested schema for CatalogTypeSchema.attributes_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    type: Union[str | None, Any] = Field(default=None)
    array: Union[bool | None, Any] = Field(default=None)
    mode: Union[str | None, Any] = Field(default=None)

class CatalogTypeSchema(BaseModel):
    """Schema definition for the catalog type"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    version: Union[float | None, Any] = Field(default=None)
    attributes: Union[list[CatalogTypeSchemaAttributesItem] | None, Any] = Field(default=None)

class CatalogType(BaseModel):
    """A catalog type defining a category of catalog entries"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    description: Union[str | None, Any] = Field(default=None)
    type_name: Union[str | None, Any] = Field(default=None)
    color: Union[str | None, Any] = Field(default=None)
    icon: Union[str | None, Any] = Field(default=None)
    ranked: Union[bool | None, Any] = Field(default=None)
    is_editable: Union[bool | None, Any] = Field(default=None)
    registry_type: Union[str | None, Any] = Field(default=None)
    semantic_type: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    last_synced_at: Union[str | None, Any] = Field(default=None)
    annotations: Union[dict[str, Any] | None, Any] = Field(default=None)
    categories: Union[list[str] | None, Any] = Field(default=None)
    required_integrations: Union[list[str] | None, Any] = Field(default=None)
    schema_: Union[CatalogTypeSchema | None, Any] = Field(default=None, alias="schema")

class ScheduleCurrentShiftsItem(BaseModel):
    """Nested schema for Schedule.current_shifts_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rotation_id: Union[str | None, Any] = Field(default=None)
    fingerprint: Union[str | None, Any] = Field(default=None)
    start_at: Union[str | None, Any] = Field(default=None)
    end_at: Union[str | None, Any] = Field(default=None)

class ScheduleConfigRotationsItemHandoversItem(BaseModel):
    """Nested schema for ScheduleConfigRotationsItem.handovers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    interval: Union[float | None, Any] = Field(default=None)
    interval_type: Union[str | None, Any] = Field(default=None)

class ScheduleConfigRotationsItemLayersItem(BaseModel):
    """Nested schema for ScheduleConfigRotationsItem.layers_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)

class ScheduleConfigRotationsItem(BaseModel):
    """Nested schema for ScheduleConfig.rotations_item"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str | None, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    handover_start_at: Union[str | None, Any] = Field(default=None)
    handovers: Union[list[ScheduleConfigRotationsItemHandoversItem] | None, Any] = Field(default=None)
    layers: Union[list[ScheduleConfigRotationsItemLayersItem] | None, Any] = Field(default=None)

class ScheduleConfig(BaseModel):
    """Schedule configuration with rotations"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    rotations: Union[list[ScheduleConfigRotationsItem] | None, Any] = Field(default=None)

class Schedule(BaseModel):
    """An on-call schedule"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Union[str, Any] = Field(default=None)
    name: Union[str | None, Any] = Field(default=None)
    timezone: Union[str | None, Any] = Field(default=None)
    created_at: Union[str | None, Any] = Field(default=None)
    updated_at: Union[str | None, Any] = Field(default=None)
    annotations: Union[dict[str, Any] | None, Any] = Field(default=None)
    config: Union[ScheduleConfig | None, Any] = Field(default=None)
    team_ids: Union[list[str] | None, Any] = Field(default=None)
    holidays_public_config: Union[dict[str, Any] | None, Any] = Field(default=None)
    current_shifts: Union[list[ScheduleCurrentShiftsItem] | None, Any] = Field(default=None)

# ===== METADATA TYPE DEFINITIONS (PYDANTIC) =====
# Meta types for operations that extract metadata (e.g., pagination info)

class IncidentsListResultMeta(BaseModel):
    """Metadata for incidents.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationMeta, Any] = Field(default=None)

class AlertsListResultMeta(BaseModel):
    """Metadata for alerts.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationMeta, Any] = Field(default=None)

class EscalationsListResultMeta(BaseModel):
    """Metadata for escalations.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationMeta, Any] = Field(default=None)

class UsersListResultMeta(BaseModel):
    """Metadata for users.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationMeta, Any] = Field(default=None)

class IncidentUpdatesListResultMeta(BaseModel):
    """Metadata for incident_updates.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationMeta, Any] = Field(default=None)

class SchedulesListResultMeta(BaseModel):
    """Metadata for schedules.Action.LIST operation"""
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    pagination: Union[PaginationMeta, Any] = Field(default=None)

# ===== CHECK RESULT MODEL =====

class IncidentIoCheckResult(BaseModel):
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


class IncidentIoExecuteResult(BaseModel, Generic[T]):
    """Response envelope with data only.

    Used for actions that return data without metadata.
    """
    model_config = ConfigDict(extra="forbid")

    data: T
    """Response data containing the result of the action."""


class IncidentIoExecuteResultWithMeta(IncidentIoExecuteResult[T], Generic[T, S]):
    """Response envelope with data and metadata.

    Used for actions that return both data and metadata (e.g., pagination info).
    """
    meta: S
    """Metadata about the response (e.g., pagination cursors, record counts)."""

# ===== SEARCH DATA MODELS =====
# Entity-specific Pydantic models for search result data

# Type variable for search data generic
D = TypeVar('D')

class IncidentsSearchData(BaseModel):
    """Search result data for incidents entity."""
    model_config = ConfigDict(extra="allow")

    call_url: str | None = None
    """URL of the call associated with the incident"""
    created_at: str | None = None
    """When the incident was created"""
    creator: dict[str, Any] | None = None
    """The user who created the incident"""
    custom_field_entries: list[Any] | None = None
    """Custom field values for the incident"""
    duration_metrics: list[Any] | None = None
    """Duration metrics associated with the incident"""
    has_debrief: bool | None = None
    """Whether the incident has had a debrief"""
    id: str | None = None
    """Unique identifier for the incident"""
    incident_role_assignments: list[Any] | None = None
    """Role assignments for the incident"""
    incident_status: dict[str, Any] | None = None
    """Current status of the incident"""
    incident_timestamp_values: list[Any] | None = None
    """Timestamp values for the incident"""
    incident_type: dict[str, Any] | None = None
    """Type of the incident"""
    mode: str | None = None
    """Mode of the incident: standard, retrospective, test, or tutorial"""
    name: str | None = None
    """Name/title of the incident"""
    permalink: str | None = None
    """Link to the incident in the dashboard"""
    reference: str | None = None
    """Human-readable reference (e.g. INC-123)"""
    severity: dict[str, Any] | None = None
    """Severity of the incident"""
    slack_channel_id: str | None = None
    """Slack channel ID for the incident"""
    slack_channel_name: str | None = None
    """Slack channel name for the incident"""
    slack_team_id: str | None = None
    """Slack team/workspace ID"""
    summary: str | None = None
    """Detailed summary of the incident"""
    updated_at: str | None = None
    """When the incident was last updated"""
    visibility: str | None = None
    """Whether the incident is public or private"""
    workload_minutes_late: float | None = None
    """Minutes of workload classified as late"""
    workload_minutes_sleeping: float | None = None
    """Minutes of workload classified as sleeping"""
    workload_minutes_total: float | None = None
    """Total workload minutes"""
    workload_minutes_working: float | None = None
    """Minutes of workload classified as working"""


class AlertsSearchData(BaseModel):
    """Search result data for alerts entity."""
    model_config = ConfigDict(extra="allow")

    alert_source_id: str | None = None
    """ID of the alert source that generated this alert"""
    attributes: list[Any] | None = None
    """Structured alert attributes"""
    created_at: str | None = None
    """When the alert was created"""
    deduplication_key: str | None = None
    """Deduplication key uniquely referencing this alert"""
    description: str | None = None
    """Description of the alert"""
    id: str | None = None
    """Unique identifier for the alert"""
    resolved_at: str | None = None
    """When the alert was resolved"""
    source_url: str | None = None
    """Link to the alert in the upstream system"""
    status: str | None = None
    """Status of the alert: firing or resolved"""
    title: str | None = None
    """Title of the alert"""
    updated_at: str | None = None
    """When the alert was last updated"""


class UsersSearchData(BaseModel):
    """Search result data for users entity."""
    model_config = ConfigDict(extra="allow")

    base_role: dict[str, Any] | None = None
    """Base role assigned to the user"""
    custom_roles: list[Any] | None = None
    """Custom roles assigned to the user"""
    email: str | None = None
    """Email address of the user"""
    id: str | None = None
    """Unique identifier for the user"""
    name: str | None = None
    """Full name of the user"""
    role: str | None = None
    """Deprecated role field"""
    slack_user_id: str | None = None
    """Slack user ID"""


class IncidentUpdatesSearchData(BaseModel):
    """Search result data for incident_updates entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """When the update was created"""
    id: str | None = None
    """Unique identifier for the incident update"""
    incident_id: str | None = None
    """ID of the incident this update belongs to"""
    message: str | None = None
    """Update message content"""
    new_incident_status: dict[str, Any] | None = None
    """New incident status set by this update"""
    new_severity: dict[str, Any] | None = None
    """New severity set by this update"""
    updater: dict[str, Any] | None = None
    """Who made this update"""


class IncidentRolesSearchData(BaseModel):
    """Search result data for incident_roles entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """When the role was created"""
    description: str | None = None
    """Description of the role"""
    id: str | None = None
    """Unique identifier for the incident role"""
    instructions: str | None = None
    """Instructions for the role holder"""
    name: str | None = None
    """Name of the role"""
    required: bool | None = None
    """Whether this role must be assigned"""
    role_type: str | None = None
    """Type of role"""
    shortform: str | None = None
    """Short form label for the role"""
    updated_at: str | None = None
    """When the role was last updated"""


class IncidentStatusesSearchData(BaseModel):
    """Search result data for incident_statuses entity."""
    model_config = ConfigDict(extra="allow")

    category: str | None = None
    """Category: triage, active, post-incident, closed, etc."""
    created_at: str | None = None
    """When the status was created"""
    description: str | None = None
    """Description of the status"""
    id: str | None = None
    """Unique identifier for the status"""
    name: str | None = None
    """Name of the status"""
    rank: float | None = None
    """Rank for ordering"""
    updated_at: str | None = None
    """When the status was last updated"""


class IncidentTimestampsSearchData(BaseModel):
    """Search result data for incident_timestamps entity."""
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    """Unique identifier for the timestamp"""
    name: str | None = None
    """Name of the timestamp"""
    rank: float | None = None
    """Rank for ordering"""


class SeveritiesSearchData(BaseModel):
    """Search result data for severities entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """When the severity was created"""
    description: str | None = None
    """Description of the severity"""
    id: str | None = None
    """Unique identifier for the severity"""
    name: str | None = None
    """Name of the severity"""
    rank: float | None = None
    """Rank for ordering"""
    updated_at: str | None = None
    """When the severity was last updated"""


class CustomFieldsSearchData(BaseModel):
    """Search result data for custom_fields entity."""
    model_config = ConfigDict(extra="allow")

    catalog_type_id: str | None = None
    """ID of the catalog type associated with this custom field"""
    created_at: str | None = None
    """When the custom field was created"""
    description: str | None = None
    """Description of the custom field"""
    field_type: str | None = None
    """Type of field"""
    id: str | None = None
    """Unique identifier for the custom field"""
    name: str | None = None
    """Name of the custom field"""
    updated_at: str | None = None
    """When the custom field was last updated"""


class CatalogTypesSearchData(BaseModel):
    """Search result data for catalog_types entity."""
    model_config = ConfigDict(extra="allow")

    annotations: dict[str, Any] | None = None
    """Annotations metadata"""
    categories: list[Any] | None = None
    """Categories this type belongs to"""
    color: str | None = None
    """Display color"""
    created_at: str | None = None
    """When the catalog type was created"""
    description: str | None = None
    """Description of the catalog type"""
    icon: str | None = None
    """Display icon"""
    id: str | None = None
    """Unique identifier for the catalog type"""
    is_editable: bool | None = None
    """Whether entries can be edited"""
    last_synced_at: str | None = None
    """When the catalog type was last synced"""
    name: str | None = None
    """Name of the catalog type"""
    ranked: bool | None = None
    """Whether entries are ranked"""
    registry_type: str | None = None
    """Registry type if synced from an integration"""
    required_integrations: list[Any] | None = None
    """Integrations required for this type"""
    schema_: dict[str, Any] | None = None
    """Schema definition for the catalog type"""
    semantic_type: str | None = None
    """Semantic type for special behavior"""
    type_name: str | None = None
    """Programmatic type name"""
    updated_at: str | None = None
    """When the catalog type was last updated"""


class SchedulesSearchData(BaseModel):
    """Search result data for schedules entity."""
    model_config = ConfigDict(extra="allow")

    annotations: dict[str, Any] | None = None
    """Annotations metadata"""
    config: dict[str, Any] | None = None
    """Schedule configuration with rotations"""
    created_at: str | None = None
    """When the schedule was created"""
    current_shifts: list[Any] | None = None
    """Currently active shifts"""
    holidays_public_config: dict[str, Any] | None = None
    """Public holiday configuration for the schedule"""
    id: str | None = None
    """Unique identifier for the schedule"""
    name: str | None = None
    """Name of the schedule"""
    team_ids: list[Any] | None = None
    """IDs of teams associated with this schedule"""
    timezone: str | None = None
    """Timezone for the schedule"""
    updated_at: str | None = None
    """When the schedule was last updated"""


class EscalationsSearchData(BaseModel):
    """Search result data for escalations entity."""
    model_config = ConfigDict(extra="allow")

    created_at: str | None = None
    """When the escalation was created"""
    creator: dict[str, Any] | None = None
    """The creator of this escalation"""
    escalation_path_id: str | None = None
    """ID of the escalation path used"""
    events: list[Any] | None = None
    """History of escalation events"""
    id: str | None = None
    """Unique identifier for the escalation"""
    priority: dict[str, Any] | None = None
    """Priority of the escalation"""
    related_alerts: list[Any] | None = None
    """Alerts related to this escalation"""
    related_incidents: list[Any] | None = None
    """Incidents related to this escalation"""
    status: str | None = None
    """Status: pending, triggered, acked, resolved, expired, cancelled"""
    title: str | None = None
    """Title of the escalation"""
    updated_at: str | None = None
    """When the escalation was last updated"""


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

IncidentsSearchResult = AirbyteSearchResult[IncidentsSearchData]
"""Search result type for incidents entity."""

AlertsSearchResult = AirbyteSearchResult[AlertsSearchData]
"""Search result type for alerts entity."""

UsersSearchResult = AirbyteSearchResult[UsersSearchData]
"""Search result type for users entity."""

IncidentUpdatesSearchResult = AirbyteSearchResult[IncidentUpdatesSearchData]
"""Search result type for incident_updates entity."""

IncidentRolesSearchResult = AirbyteSearchResult[IncidentRolesSearchData]
"""Search result type for incident_roles entity."""

IncidentStatusesSearchResult = AirbyteSearchResult[IncidentStatusesSearchData]
"""Search result type for incident_statuses entity."""

IncidentTimestampsSearchResult = AirbyteSearchResult[IncidentTimestampsSearchData]
"""Search result type for incident_timestamps entity."""

SeveritiesSearchResult = AirbyteSearchResult[SeveritiesSearchData]
"""Search result type for severities entity."""

CustomFieldsSearchResult = AirbyteSearchResult[CustomFieldsSearchData]
"""Search result type for custom_fields entity."""

CatalogTypesSearchResult = AirbyteSearchResult[CatalogTypesSearchData]
"""Search result type for catalog_types entity."""

SchedulesSearchResult = AirbyteSearchResult[SchedulesSearchData]
"""Search result type for schedules entity."""

EscalationsSearchResult = AirbyteSearchResult[EscalationsSearchData]
"""Search result type for escalations entity."""



# ===== OPERATION RESULT TYPE ALIASES =====

# Concrete type aliases for each operation result.
# These provide simpler, more readable type annotations than using the generic forms.

IncidentsListResult = IncidentIoExecuteResultWithMeta[list[Incident], IncidentsListResultMeta]
"""Result type for incidents.list operation with data and metadata."""

AlertsListResult = IncidentIoExecuteResultWithMeta[list[Alert], AlertsListResultMeta]
"""Result type for alerts.list operation with data and metadata."""

EscalationsListResult = IncidentIoExecuteResultWithMeta[list[Escalation], EscalationsListResultMeta]
"""Result type for escalations.list operation with data and metadata."""

UsersListResult = IncidentIoExecuteResultWithMeta[list[User], UsersListResultMeta]
"""Result type for users.list operation with data and metadata."""

IncidentUpdatesListResult = IncidentIoExecuteResultWithMeta[list[IncidentUpdate], IncidentUpdatesListResultMeta]
"""Result type for incident_updates.list operation with data and metadata."""

IncidentRolesListResult = IncidentIoExecuteResult[list[IncidentRole]]
"""Result type for incident_roles.list operation."""

IncidentStatusesListResult = IncidentIoExecuteResult[list[IncidentStatus]]
"""Result type for incident_statuses.list operation."""

IncidentTimestampsListResult = IncidentIoExecuteResult[list[IncidentTimestamp]]
"""Result type for incident_timestamps.list operation."""

SeveritiesListResult = IncidentIoExecuteResult[list[Severity]]
"""Result type for severities.list operation."""

CustomFieldsListResult = IncidentIoExecuteResult[list[CustomField]]
"""Result type for custom_fields.list operation."""

CatalogTypesListResult = IncidentIoExecuteResult[list[CatalogType]]
"""Result type for catalog_types.list operation."""

SchedulesListResult = IncidentIoExecuteResultWithMeta[list[Schedule], SchedulesListResultMeta]
"""Result type for schedules.list operation with data and metadata."""

