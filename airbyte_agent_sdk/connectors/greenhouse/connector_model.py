"""
Connector model for greenhouse.

This file is auto-generated from the connector definition at build time.
DO NOT EDIT MANUALLY - changes will be overwritten on next generation.
"""
# ruff: noqa: E501

from __future__ import annotations

from airbyte_agent_sdk.types import (
    Action,
    AuthConfig,
    AuthType,
    ConnectorModel,
    EndpointDefinition,
    EntityDefinition,
)
from airbyte_agent_sdk.schema.security import (
    AuthConfigFieldSpec,
    AuthConfigSpec,
)
from airbyte_agent_sdk.schema.extensions import (
    CacheConfig,
    CacheEntityConfig,
    CacheFieldConfig,
    CacheFieldProperty,
    SemanticEmbedding,
    SemanticMetadataField,
    SemanticSample,
    SemanticSampling,
    SemanticSearchConfig,
    SemanticWindowing,
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from airbyte_agent_sdk.schema.components import (
    PathOverrideConfig,
)
from uuid import (
    UUID,
)

GreenhouseConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('59f1e50a-331f-4f09-b3e8-2e8d4d355f44'),
    name='greenhouse',
    version='0.2.0',
    base_url='https://harvest.greenhouse.io/v3',
    auth=AuthConfig(
        type=AuthType.OAUTH2,
        config={
            'header': 'Authorization',
            'prefix': 'Bearer',
            'refresh_url': 'https://auth.greenhouse.io/token',
            'auth_style': 'basic',
            'body_format': 'form',
        },
        user_config_spec=AuthConfigSpec(
            title='Greenhouse OAuth 2.0',
            type='object',
            required=['client_id', 'client_secret', 'refresh_token'],
            properties={
                'client_id': AuthConfigFieldSpec(
                    title='Client ID',
                    description='Client ID from the Greenhouse OAuth application',
                ),
                'client_secret': AuthConfigFieldSpec(
                    title='Client Secret',
                    description='Client secret from the Greenhouse OAuth application',
                ),
                'refresh_token': AuthConfigFieldSpec(
                    title='Refresh Token',
                    description='Refresh token generated through the Greenhouse OAuth consent flow',
                ),
                'access_token': AuthConfigFieldSpec(
                    title='Access Token',
                    description='Access token generated through the Greenhouse OAuth consent flow (optional if refresh_token is provided)',
                ),
            },
            auth_mapping={
                'client_id': '${client_id}',
                'client_secret': '${client_secret}',
                'refresh_token': '${refresh_token}',
                'access_token': '${access_token}',
            },
            replication_auth_key_mapping={
                'credentials.client_id': 'client_id',
                'credentials.client_secret': 'client_secret',
                'credentials.refresh_token': 'refresh_token',
                'credentials.access_token': 'access_token',
            },
            replication_auth_key_constants={'credentials.auth_type': 'Client'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='applications',
            stream_name='applications',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/applications',
                    action=Action.LIST,
                    description='Returns a cursor-paginated list of applications.',
                    query_params=[
                        'cursor',
                        'per_page',
                        'ids',
                        'updated_at',
                    ],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                        'updated_at': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse application object',
                            'properties': {
                                'agency_note_id': {
                                    'description': 'Id of the note created when the candidate was submitted by an agency, or `null` if the application did not come through an agency.',
                                    'type': ['null', 'integer'],
                                },
                                'answers': {
                                    'description': "Free-text answers the candidate provided on the job post application form. Each entry pairs the question text with the candidate's answer.",
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'answer': {
                                                'description': "Candidate's free-text answer to the question.",
                                                'type': ['null', 'string'],
                                            },
                                            'question': {
                                                'description': 'Application-form question the candidate answered.',
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'candidate_id': {
                                    'description': 'Id of the candidate (person) this application belongs to.',
                                    'type': ['null', 'integer'],
                                },
                                'coordinator_id': {
                                    'description': "Id of the user assigned as coordinator on the application's job, or `null` when unassigned.",
                                    'type': ['null', 'integer'],
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'custom_fields': {
                                    'description': "Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                                    'type': ['null', 'object'],
                                    'additionalProperties': {
                                        'type': 'object',
                                        'properties': {
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'type': {
                                                'type': ['null', 'string'],
                                            },
                                            'value': {
                                                'type': [
                                                    'null',
                                                    'string',
                                                    'number',
                                                    'integer',
                                                    'boolean',
                                                    'object',
                                                    'array',
                                                ],
                                            },
                                        },
                                    },
                                },
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'job_id': {
                                    'description': 'Id of the job this application is on. `null` for jobless prospect applications.',
                                    'type': ['null', 'integer'],
                                },
                                'job_interview_stage_id': {
                                    'description': 'Id of the job interview stage definition (see `GET /v3/job_interview_stages`) the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state.',
                                    'type': ['null', 'integer'],
                                },
                                'job_post_id': {
                                    'description': 'Id of the job post the candidate applied through, or `null` if the application was created internally rather than from a posted role.',
                                    'type': ['null', 'integer'],
                                },
                                'last_activity_at': {
                                    'description': 'Timestamp of the most recent activity on this application (notes, emails, stage changes, etc.), in ISO 8601.',
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'location_address': {
                                    'description': "Free-form location string captured on the application (typically from the job post's location question).",
                                    'type': ['null', 'string'],
                                },
                                'needs_decision': {
                                    'description': '`true` when the application is waiting on a hiring-team decision (scorecard completion, advance/reject, etc.) in its current stage.',
                                    'type': ['null', 'boolean'],
                                },
                                'prospect': {
                                    'description': '`true` for prospect applications (sourced candidates not yet attached to a single job), `false` for candidate applications on a specific job.',
                                    'type': ['null', 'boolean'],
                                },
                                'prospective_job_ids': {
                                    'description': 'For prospect applications, the ids of jobs the prospect is being considered for. Empty for non-prospect applications and for jobless prospects.',
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'recruiter_id': {
                                    'description': "Id of the user assigned as recruiter on the application's job, or `null` when unassigned.",
                                    'type': ['null', 'integer'],
                                },
                                'referrer_id': {
                                    'description': 'Id of the referrer who credited this application, or `null` if there was no referral. References a referrer, not a Greenhouse user.',
                                    'type': ['null', 'integer'],
                                },
                                'rejected_at': {
                                    'description': 'Timestamp the application was rejected, in ISO 8601. `null` for applications that have not been rejected.',
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'rejection_reason_id': {
                                    'description': 'Id of the rejection reason selected for the application. References a `/v3/rejection_reasons` row scoped to the organization. `null` when the application was rejected without a reason, or has not been rejected.',
                                    'type': ['null', 'integer'],
                                },
                                'source_id': {
                                    'description': 'Id of the source the application is attributed to (e.g. a job board, an event, an employee referral source). `null` if no source is set.',
                                    'type': ['null', 'integer'],
                                },
                                'stage_id': {
                                    'description': 'Id of the interview stage the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state.',
                                    'type': ['null', 'integer'],
                                },
                                'stage_name': {
                                    'description': "Display name of the candidate's current interview stage on this application.",
                                    'type': ['null', 'string'],
                                },
                                'status': {
                                    'description': 'Lifecycle status of the application. `in_process` for active candidates, `rejected` for rejected applications, `hired` once an offer is closed and the hire endpoint has fired, and `converted` for prospect applications that have been promoted to a candidate application via `convert_to_candidate`.',
                                    'type': ['null', 'string'],
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                            },
                            'x-airbyte-entity-name': 'applications',
                            'x-airbyte-stream-name': 'applications',
                            'x-airbyte-ai-hints': {
                                'summary': 'Job applications with stage, status, and interview details',
                                'when_to_use': 'Questions about application status or hiring pipeline progress',
                                'trigger_phrases': ['application status', 'hiring stage', 'interview status'],
                                'freshness': 'live',
                                'example_questions': ['What stage is an application in?'],
                                'search_strategy': 'Filter by candidate, job, or status',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse application object',
                'properties': {
                    'agency_note_id': {
                        'description': 'Id of the note created when the candidate was submitted by an agency, or `null` if the application did not come through an agency.',
                        'type': ['null', 'integer'],
                    },
                    'answers': {
                        'description': "Free-text answers the candidate provided on the job post application form. Each entry pairs the question text with the candidate's answer.",
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'answer': {
                                    'description': "Candidate's free-text answer to the question.",
                                    'type': ['null', 'string'],
                                },
                                'question': {
                                    'description': 'Application-form question the candidate answered.',
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'candidate_id': {
                        'description': 'Id of the candidate (person) this application belongs to.',
                        'type': ['null', 'integer'],
                    },
                    'coordinator_id': {
                        'description': "Id of the user assigned as coordinator on the application's job, or `null` when unassigned.",
                        'type': ['null', 'integer'],
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'custom_fields': {
                        'description': "Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                        'type': ['null', 'object'],
                        'additionalProperties': {
                            'type': 'object',
                            'properties': {
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'value': {
                                    'type': [
                                        'null',
                                        'string',
                                        'number',
                                        'integer',
                                        'boolean',
                                        'object',
                                        'array',
                                    ],
                                },
                            },
                        },
                    },
                    'id': {
                        'type': ['null', 'integer'],
                    },
                    'job_id': {
                        'description': 'Id of the job this application is on. `null` for jobless prospect applications.',
                        'type': ['null', 'integer'],
                    },
                    'job_interview_stage_id': {
                        'description': 'Id of the job interview stage definition (see `GET /v3/job_interview_stages`) the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state.',
                        'type': ['null', 'integer'],
                    },
                    'job_post_id': {
                        'description': 'Id of the job post the candidate applied through, or `null` if the application was created internally rather than from a posted role.',
                        'type': ['null', 'integer'],
                    },
                    'last_activity_at': {
                        'description': 'Timestamp of the most recent activity on this application (notes, emails, stage changes, etc.), in ISO 8601.',
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'location_address': {
                        'description': "Free-form location string captured on the application (typically from the job post's location question).",
                        'type': ['null', 'string'],
                    },
                    'needs_decision': {
                        'description': '`true` when the application is waiting on a hiring-team decision (scorecard completion, advance/reject, etc.) in its current stage.',
                        'type': ['null', 'boolean'],
                    },
                    'prospect': {
                        'description': '`true` for prospect applications (sourced candidates not yet attached to a single job), `false` for candidate applications on a specific job.',
                        'type': ['null', 'boolean'],
                    },
                    'prospective_job_ids': {
                        'description': 'For prospect applications, the ids of jobs the prospect is being considered for. Empty for non-prospect applications and for jobless prospects.',
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'recruiter_id': {
                        'description': "Id of the user assigned as recruiter on the application's job, or `null` when unassigned.",
                        'type': ['null', 'integer'],
                    },
                    'referrer_id': {
                        'description': 'Id of the referrer who credited this application, or `null` if there was no referral. References a referrer, not a Greenhouse user.',
                        'type': ['null', 'integer'],
                    },
                    'rejected_at': {
                        'description': 'Timestamp the application was rejected, in ISO 8601. `null` for applications that have not been rejected.',
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'rejection_reason_id': {
                        'description': 'Id of the rejection reason selected for the application. References a `/v3/rejection_reasons` row scoped to the organization. `null` when the application was rejected without a reason, or has not been rejected.',
                        'type': ['null', 'integer'],
                    },
                    'source_id': {
                        'description': 'Id of the source the application is attributed to (e.g. a job board, an event, an employee referral source). `null` if no source is set.',
                        'type': ['null', 'integer'],
                    },
                    'stage_id': {
                        'description': 'Id of the interview stage the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state.',
                        'type': ['null', 'integer'],
                    },
                    'stage_name': {
                        'description': "Display name of the candidate's current interview stage on this application.",
                        'type': ['null', 'string'],
                    },
                    'status': {
                        'description': 'Lifecycle status of the application. `in_process` for active candidates, `rejected` for rejected applications, `hired` once an offer is closed and the hire endpoint has fired, and `converted` for prospect applications that have been promoted to a candidate application via `convert_to_candidate`.',
                        'type': ['null', 'string'],
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                },
                'x-airbyte-entity-name': 'applications',
                'x-airbyte-stream-name': 'applications',
                'x-airbyte-ai-hints': {
                    'summary': 'Job applications with stage, status, and interview details',
                    'when_to_use': 'Questions about application status or hiring pipeline progress',
                    'trigger_phrases': ['application status', 'hiring stage', 'interview status'],
                    'freshness': 'live',
                    'example_questions': ['What stage is an application in?'],
                    'search_strategy': 'Filter by candidate, job, or status',
                },
            },
            ai_hints={
                'summary': 'Job applications with stage, status, and interview details',
                'when_to_use': 'Questions about application status or hiring pipeline progress',
                'trigger_phrases': ['application status', 'hiring stage', 'interview status'],
                'freshness': 'live',
                'example_questions': ['What stage is an application in?'],
                'search_strategy': 'Filter by candidate, job, or status',
            },
        ),
        EntityDefinition(
            name='candidates',
            stream_name='candidates',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/candidates',
                    action=Action.LIST,
                    description='Returns a cursor-paginated list of candidates.',
                    query_params=[
                        'cursor',
                        'per_page',
                        'ids',
                        'updated_at',
                    ],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                        'updated_at': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse candidate object',
                            'properties': {
                                'addresses': {
                                    'description': "Postal addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `home`, `work`, or `other`.",
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'type': {
                                                'type': ['null', 'string'],
                                            },
                                            'value': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'can_email': {
                                    'description': 'Whether this candidate has consented to receive email communication from your organization.',
                                    'type': ['null', 'boolean'],
                                },
                                'company': {
                                    'description': "Candidate's current company, as entered on their profile.",
                                    'type': ['null', 'string'],
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'custom_fields': {
                                    'description': "Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                                    'type': ['null', 'object'],
                                    'additionalProperties': {
                                        'type': 'object',
                                        'properties': {
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'type': {
                                                'type': ['null', 'string'],
                                            },
                                            'value': {
                                                'type': [
                                                    'null',
                                                    'string',
                                                    'number',
                                                    'integer',
                                                    'boolean',
                                                    'object',
                                                    'array',
                                                ],
                                            },
                                        },
                                    },
                                },
                                'email_addresses': {
                                    'description': "Email addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `work`, or `other`.",
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'type': {
                                                'type': ['null', 'string'],
                                            },
                                            'value': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'first_name': {
                                    'type': ['null', 'string'],
                                },
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'last_activity_at': {
                                    'description': "Timestamp of the most recent activity on any of the candidate's applications (notes, emails, stage changes, etc.), in ISO 8601.",
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'last_name': {
                                    'type': ['null', 'string'],
                                },
                                'linked_user_ids': {
                                    'description': 'Ids of Greenhouse users linked to this candidate (employees represented by both a user record and a candidate record).',
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'phone_numbers': {
                                    'description': "Phone numbers on the candidate's profile. Each entry pairs the `value` with a `type` such as `mobile`, `home`, `work`, `skype`, or `other`.",
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'type': {
                                                'type': ['null', 'string'],
                                            },
                                            'value': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'preferred_name': {
                                    'description': 'Preferred or chosen name the candidate goes by, when different from their legal first name.',
                                    'type': ['null', 'string'],
                                },
                                'private': {
                                    'description': 'If true, the candidate is restricted to users with `View Private Candidates` access. Defaults to `false`.',
                                    'type': ['null', 'boolean'],
                                },
                                'social_media_addresses': {
                                    'description': "Social media handles or URLs on the candidate's profile. Social entries are untyped — only the `value` is returned.",
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'value': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'tags': {
                                    'description': 'Candidate tag names applied to this candidate within your organization.',
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'string'],
                                    },
                                },
                                'time_zone': {
                                    'description': "Candidate's time zone as a Rails-style identifier (for example `Eastern Time (US & Canada)`).",
                                    'type': ['null', 'string'],
                                },
                                'title': {
                                    'description': "Candidate's current job title, as entered on their profile.",
                                    'type': ['null', 'string'],
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'website_addresses': {
                                    'description': "Personal websites or portfolio URLs on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `company`, `portfolio`, `blog`, or `other`.",
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'type': {
                                                'type': ['null', 'string'],
                                            },
                                            'value': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                            },
                            'x-airbyte-entity-name': 'candidates',
                            'x-airbyte-stream-name': 'candidates',
                            'x-airbyte-ai-hints': {
                                'summary': 'Job candidates with application history and contact details',
                                'when_to_use': 'Looking up candidate information or hiring pipeline data',
                                'trigger_phrases': ['greenhouse candidate', 'applicant', 'who applied'],
                                'freshness': 'live',
                                'example_questions': ['Find a candidate in Greenhouse', 'List recent candidates'],
                                'search_strategy': 'Search by name or email',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
                    preferred_for_check=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse candidate object',
                'properties': {
                    'addresses': {
                        'description': "Postal addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `home`, `work`, or `other`.",
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'value': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'can_email': {
                        'description': 'Whether this candidate has consented to receive email communication from your organization.',
                        'type': ['null', 'boolean'],
                    },
                    'company': {
                        'description': "Candidate's current company, as entered on their profile.",
                        'type': ['null', 'string'],
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'custom_fields': {
                        'description': "Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                        'type': ['null', 'object'],
                        'additionalProperties': {
                            'type': 'object',
                            'properties': {
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'value': {
                                    'type': [
                                        'null',
                                        'string',
                                        'number',
                                        'integer',
                                        'boolean',
                                        'object',
                                        'array',
                                    ],
                                },
                            },
                        },
                    },
                    'email_addresses': {
                        'description': "Email addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `work`, or `other`.",
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'value': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'first_name': {
                        'type': ['null', 'string'],
                    },
                    'id': {
                        'type': ['null', 'integer'],
                    },
                    'last_activity_at': {
                        'description': "Timestamp of the most recent activity on any of the candidate's applications (notes, emails, stage changes, etc.), in ISO 8601.",
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'last_name': {
                        'type': ['null', 'string'],
                    },
                    'linked_user_ids': {
                        'description': 'Ids of Greenhouse users linked to this candidate (employees represented by both a user record and a candidate record).',
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'phone_numbers': {
                        'description': "Phone numbers on the candidate's profile. Each entry pairs the `value` with a `type` such as `mobile`, `home`, `work`, `skype`, or `other`.",
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'value': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'preferred_name': {
                        'description': 'Preferred or chosen name the candidate goes by, when different from their legal first name.',
                        'type': ['null', 'string'],
                    },
                    'private': {
                        'description': 'If true, the candidate is restricted to users with `View Private Candidates` access. Defaults to `false`.',
                        'type': ['null', 'boolean'],
                    },
                    'social_media_addresses': {
                        'description': "Social media handles or URLs on the candidate's profile. Social entries are untyped — only the `value` is returned.",
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'value': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'tags': {
                        'description': 'Candidate tag names applied to this candidate within your organization.',
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'string'],
                        },
                    },
                    'time_zone': {
                        'description': "Candidate's time zone as a Rails-style identifier (for example `Eastern Time (US & Canada)`).",
                        'type': ['null', 'string'],
                    },
                    'title': {
                        'description': "Candidate's current job title, as entered on their profile.",
                        'type': ['null', 'string'],
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'website_addresses': {
                        'description': "Personal websites or portfolio URLs on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `company`, `portfolio`, `blog`, or `other`.",
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'value': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'candidates',
                'x-airbyte-stream-name': 'candidates',
                'x-airbyte-ai-hints': {
                    'summary': 'Job candidates with application history and contact details',
                    'when_to_use': 'Looking up candidate information or hiring pipeline data',
                    'trigger_phrases': ['greenhouse candidate', 'applicant', 'who applied'],
                    'freshness': 'live',
                    'example_questions': ['Find a candidate in Greenhouse', 'List recent candidates'],
                    'search_strategy': 'Search by name or email',
                },
            },
            ai_hints={
                'summary': 'Job candidates with application history and contact details',
                'when_to_use': 'Looking up candidate information or hiring pipeline data',
                'trigger_phrases': ['greenhouse candidate', 'applicant', 'who applied'],
                'freshness': 'live',
                'example_questions': ['Find a candidate in Greenhouse', 'List recent candidates'],
                'search_strategy': 'Search by name or email',
            },
        ),
        EntityDefinition(
            name='departments',
            stream_name='departments',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/departments',
                    action=Action.LIST,
                    description='Returns a cursor-paginated list of departments.',
                    query_params=['cursor', 'per_page', 'ids'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse department object',
                            'properties': {
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'external_id': {
                                    'description': 'Partner-supplied identifier for the department, typically the matching id from an HRIS or other external system. Free-form string and `null` when no external id has been set.',
                                    'type': ['null', 'string'],
                                },
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'description': 'Display name of the department (e.g. `Engineering`, `Marketing`).',
                                    'type': ['null', 'string'],
                                },
                                'parent_id': {
                                    'description': "Id of the parent department in the organization's department tree. `null` for top-level departments. References another `/v3/departments` row.",
                                    'type': ['null', 'integer'],
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                            },
                            'x-airbyte-entity-name': 'departments',
                            'x-airbyte-stream-name': 'departments',
                            'x-airbyte-ai-hints': {
                                'summary': 'Departments in the organization for job categorization',
                                'when_to_use': 'Questions about department structure or hiring by department',
                                'trigger_phrases': ['department', 'hiring department'],
                                'freshness': 'static',
                                'example_questions': ['What departments are in Greenhouse?'],
                                'search_strategy': 'Search by name',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse department object',
                'properties': {
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'external_id': {
                        'description': 'Partner-supplied identifier for the department, typically the matching id from an HRIS or other external system. Free-form string and `null` when no external id has been set.',
                        'type': ['null', 'string'],
                    },
                    'id': {
                        'type': ['null', 'integer'],
                    },
                    'name': {
                        'description': 'Display name of the department (e.g. `Engineering`, `Marketing`).',
                        'type': ['null', 'string'],
                    },
                    'parent_id': {
                        'description': "Id of the parent department in the organization's department tree. `null` for top-level departments. References another `/v3/departments` row.",
                        'type': ['null', 'integer'],
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                },
                'x-airbyte-entity-name': 'departments',
                'x-airbyte-stream-name': 'departments',
                'x-airbyte-ai-hints': {
                    'summary': 'Departments in the organization for job categorization',
                    'when_to_use': 'Questions about department structure or hiring by department',
                    'trigger_phrases': ['department', 'hiring department'],
                    'freshness': 'static',
                    'example_questions': ['What departments are in Greenhouse?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Departments in the organization for job categorization',
                'when_to_use': 'Questions about department structure or hiring by department',
                'trigger_phrases': ['department', 'hiring department'],
                'freshness': 'static',
                'example_questions': ['What departments are in Greenhouse?'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='interviews',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/interviews',
                    action=Action.LIST,
                    description='Returns a cursor-paginated list of interviews.',
                    query_params=[
                        'cursor',
                        'per_page',
                        'ids',
                        'updated_at',
                    ],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                        'updated_at': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse interview object',
                            'properties': {
                                'all_day_end_on': {
                                    'description': 'End date of an all-day interview, in `YYYY-MM-DD`. Set instead of `starts_at`/`ends_at` when the underlying calendar event is an all-day event. `null` for time-bounded interviews.',
                                    'type': ['null', 'string'],
                                    'format': 'date',
                                },
                                'all_day_start_on': {
                                    'description': 'Start date of an all-day interview, in `YYYY-MM-DD`. Set instead of `starts_at`/`ends_at` when the underlying calendar event is an all-day event. `null` for time-bounded interviews.',
                                    'type': ['null', 'string'],
                                    'format': 'date',
                                },
                                'application_id': {
                                    'description': 'Id of the application this interview is scheduled against. Use it to look up the candidate.',
                                    'type': ['null', 'integer'],
                                },
                                'availability_received_at': {
                                    'description': "Timestamp Greenhouse first recorded availability for this interview's stage on this application (used to compute time-to-schedule), in ISO 8601. `null` if availability has not been collected for the stage.",
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'ends_at': {
                                    'description': 'Interview end time, in ISO 8601. `null` when `starts_at` is also `null`, and for all-day events — see `all_day_end_on`.',
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'external_event_id': {
                                    'description': "Id of the calendar event on the organizer's calendar (Google Calendar event id, Outlook event id, etc.). Use this to correlate an interview with the event on the external calendar. `null` for interviews not yet pushed to an external calendar.",
                                    'type': ['null', 'string'],
                                },
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'job_id': {
                                    'description': 'Id of the job this interview is on.',
                                    'type': ['null', 'integer'],
                                },
                                'job_interview_id': {
                                    'description': "Id of the job interview slot on the job's interview plan that this interview fulfills. Distinct from this interview's own `id`.",
                                    'type': ['null', 'integer'],
                                },
                                'location': {
                                    'description': "Free-form location string copied from the calendar event (a room name, an address, or a meeting URL when the customer puts it in the location field). Use `video_conferencing_url` for the link generated by Greenhouse's video integrations.",
                                    'type': ['null', 'string'],
                                },
                                'organizer_id': {
                                    'description': 'Id of the Greenhouse user who scheduled the interview (the organizer on the underlying calendar event). `null` for interviews not yet scheduled through a calendar integration.',
                                    'type': ['null', 'integer'],
                                },
                                'scheduled_at': {
                                    'description': 'Timestamp the interview was first placed on a calendar through a Greenhouse calendaring integration (Google, Outlook, or Greenhouse Schedule), in ISO 8601. `null` for interviews that have never been scheduled via the calendar pipeline.',
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'starts_at': {
                                    'description': 'Interview start time, in ISO 8601. `null` for interviews that have not yet been scheduled (for example, assigned take-home tests or interviews awaiting candidate availability) and for all-day events — see `all_day_start_on`.',
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'status': {
                                    'description': 'Lifecycle status of the interview. `to_be_scheduled` is the pre-schedule placeholder; `scheduled` is on the calendar; `awaiting_feedback` is past with scorecards outstanding; `complete` is past with all scorecards in; `collect_feedback` and `skipped` are alternative terminal states; `to_be_sent`, `sent`, and `received` are used for take-home tests sent through Greenhouse.',
                                    'type': ['null', 'string'],
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'video_conferencing_url': {
                                    'description': "Join URL for the interview's video conference, auto-populated by Greenhouse's Zoom, Google Meet, or Microsoft Teams integrations when one is attached during scheduling. `null` when no video conferencing was added.",
                                    'type': ['null', 'string'],
                                },
                            },
                            'x-airbyte-entity-name': 'interviews',
                            'x-airbyte-ai-hints': {
                                'summary': 'Interviews with time, interviewer, and stage details',
                                'when_to_use': 'Questions about upcoming interviews or interview schedules',
                                'trigger_phrases': ['interview schedule', 'upcoming interview', 'interview'],
                                'freshness': 'live',
                                'example_questions': ['What interviews are scheduled?'],
                                'search_strategy': 'Filter by date or candidate',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse interview object',
                'properties': {
                    'all_day_end_on': {
                        'description': 'End date of an all-day interview, in `YYYY-MM-DD`. Set instead of `starts_at`/`ends_at` when the underlying calendar event is an all-day event. `null` for time-bounded interviews.',
                        'type': ['null', 'string'],
                        'format': 'date',
                    },
                    'all_day_start_on': {
                        'description': 'Start date of an all-day interview, in `YYYY-MM-DD`. Set instead of `starts_at`/`ends_at` when the underlying calendar event is an all-day event. `null` for time-bounded interviews.',
                        'type': ['null', 'string'],
                        'format': 'date',
                    },
                    'application_id': {
                        'description': 'Id of the application this interview is scheduled against. Use it to look up the candidate.',
                        'type': ['null', 'integer'],
                    },
                    'availability_received_at': {
                        'description': "Timestamp Greenhouse first recorded availability for this interview's stage on this application (used to compute time-to-schedule), in ISO 8601. `null` if availability has not been collected for the stage.",
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'ends_at': {
                        'description': 'Interview end time, in ISO 8601. `null` when `starts_at` is also `null`, and for all-day events — see `all_day_end_on`.',
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'external_event_id': {
                        'description': "Id of the calendar event on the organizer's calendar (Google Calendar event id, Outlook event id, etc.). Use this to correlate an interview with the event on the external calendar. `null` for interviews not yet pushed to an external calendar.",
                        'type': ['null', 'string'],
                    },
                    'id': {
                        'type': ['null', 'integer'],
                    },
                    'job_id': {
                        'description': 'Id of the job this interview is on.',
                        'type': ['null', 'integer'],
                    },
                    'job_interview_id': {
                        'description': "Id of the job interview slot on the job's interview plan that this interview fulfills. Distinct from this interview's own `id`.",
                        'type': ['null', 'integer'],
                    },
                    'location': {
                        'description': "Free-form location string copied from the calendar event (a room name, an address, or a meeting URL when the customer puts it in the location field). Use `video_conferencing_url` for the link generated by Greenhouse's video integrations.",
                        'type': ['null', 'string'],
                    },
                    'organizer_id': {
                        'description': 'Id of the Greenhouse user who scheduled the interview (the organizer on the underlying calendar event). `null` for interviews not yet scheduled through a calendar integration.',
                        'type': ['null', 'integer'],
                    },
                    'scheduled_at': {
                        'description': 'Timestamp the interview was first placed on a calendar through a Greenhouse calendaring integration (Google, Outlook, or Greenhouse Schedule), in ISO 8601. `null` for interviews that have never been scheduled via the calendar pipeline.',
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'starts_at': {
                        'description': 'Interview start time, in ISO 8601. `null` for interviews that have not yet been scheduled (for example, assigned take-home tests or interviews awaiting candidate availability) and for all-day events — see `all_day_start_on`.',
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'status': {
                        'description': 'Lifecycle status of the interview. `to_be_scheduled` is the pre-schedule placeholder; `scheduled` is on the calendar; `awaiting_feedback` is past with scorecards outstanding; `complete` is past with all scorecards in; `collect_feedback` and `skipped` are alternative terminal states; `to_be_sent`, `sent`, and `received` are used for take-home tests sent through Greenhouse.',
                        'type': ['null', 'string'],
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'video_conferencing_url': {
                        'description': "Join URL for the interview's video conference, auto-populated by Greenhouse's Zoom, Google Meet, or Microsoft Teams integrations when one is attached during scheduling. `null` when no video conferencing was added.",
                        'type': ['null', 'string'],
                    },
                },
                'x-airbyte-entity-name': 'interviews',
                'x-airbyte-ai-hints': {
                    'summary': 'Interviews with time, interviewer, and stage details',
                    'when_to_use': 'Questions about upcoming interviews or interview schedules',
                    'trigger_phrases': ['interview schedule', 'upcoming interview', 'interview'],
                    'freshness': 'live',
                    'example_questions': ['What interviews are scheduled?'],
                    'search_strategy': 'Filter by date or candidate',
                },
            },
            ai_hints={
                'summary': 'Interviews with time, interviewer, and stage details',
                'when_to_use': 'Questions about upcoming interviews or interview schedules',
                'trigger_phrases': ['interview schedule', 'upcoming interview', 'interview'],
                'freshness': 'live',
                'example_questions': ['What interviews are scheduled?'],
                'search_strategy': 'Filter by date or candidate',
            },
        ),
        EntityDefinition(
            name='job_posts',
            stream_name='job_posts',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/job_posts',
                    action=Action.LIST,
                    description='Returns a cursor-paginated list of job posts.',
                    query_params=[
                        'cursor',
                        'per_page',
                        'ids',
                        'updated_at',
                        'active',
                    ],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                        'updated_at': {'type': 'string', 'required': False},
                        'active': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse job post object',
                            'properties': {
                                'active': {
                                    'description': 'If `true`, the post has not been deleted. Deleted posts are excluded by default; pass `active=false` on the list endpoint to retrieve them.',
                                    'type': ['null', 'boolean'],
                                },
                                'content': {
                                    'description': 'HTML body of the post shown to candidates on the job board. For internal posts this returns the `internal_content` instead. Sanitized server-side — only a limited element/attribute allowlist (including `iframe`, `video`, `source`) survives. `null` while the post is still being scaffolded.',
                                    'type': ['null', 'string'],
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'demographic_question_set_id': {
                                    'description': 'Id of the demographic question set surfaced to candidates on this post for diversity, equity, and inclusion (DE&I) reporting. `null` when the post does not collect demographic data.',
                                    'type': ['null', 'integer'],
                                },
                                'featured': {
                                    'description': "If `true`, the post is currently featured on the organization's internal job board and surfaces in the weekly internal-jobs email. Only internal posts can be featured, and at most three can be featured at a time.",
                                    'type': ['null', 'boolean'],
                                },
                                'first_published_at': {
                                    'description': 'Timestamp the post first transitioned to `live`, in ISO 8601. `null` for posts that have never been published.',
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'internal': {
                                    'description': 'If `true`, the post lives on an internal job board and is visible only to existing employees signed in to the internal board. If `false`, the post is external and lives on a public-facing `job_board`. Set by the board the post is associated with at create time.',
                                    'type': ['null', 'boolean'],
                                },
                                'internal_content': {
                                    'description': 'HTML body shown on the internal job board when the post is also configured as internal. `null` for external-only posts. Same sanitization rules as `content`.',
                                    'type': ['null', 'string'],
                                },
                                'job_board_id': {
                                    'description': 'Id of the `job_board` this post is published to. Resolves to either an external (careers site, syndicated board) or internal job board depending on `internal`. Each post belongs to exactly one board at a time.',
                                    'type': ['null', 'integer'],
                                },
                                'job_id': {
                                    'description': 'Id of the parent job (requisition) this post belongs to. A single job can have multiple posts; the job is the source of truth for the hiring team, openings, and interview plan.',
                                    'type': ['null', 'integer'],
                                },
                                'language': {
                                    'description': 'ISO 639-1 locale of the post, used to render the candidate-facing application form in the matching language (e.g. `en`, `fr`, `ja`). `null` when no locale has been chosen.',
                                    'type': ['null', 'string'],
                                },
                                'live': {
                                    'description': 'If `true`, the post is published (`job_application_status` is `live`) and its job board is also live. A post on an unpublished board is **not** `live` — its `public_url` returns a 404 until the board is enabled.',
                                    'type': ['null', 'boolean'],
                                },
                                'public_url': {
                                    'description': 'Canonical public URL of the post on its job board, including the `gh_jid` tracking parameter. `null` when the post has no associated job board or the board has no public URL configured.',
                                    'type': ['null', 'string'],
                                    'format': 'uri',
                                },
                                'questions': {
                                    'description': 'Application form questions presented to candidates on this post, including default questions (resume, cover letter, basic info) and any custom questions configured by the hiring team. Ordered as they appear on the form.',
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'answer_type': {
                                                'description': 'Input type the candidate uses to answer. `short_text` and `long_text` are free-text inputs, `single_select` and `multi_select` use the `options` array, `boolean` is a yes/no, `attachment` accepts a file upload, and `hidden` is set programmatically without rendering a field.',
                                                'type': ['null', 'string'],
                                            },
                                            'description': {
                                                'description': 'Help text shown below the question label to give candidates additional context. `null` when no help text is set.',
                                                'type': ['null', 'string'],
                                            },
                                            'id': {
                                                'description': 'Id of the question. `null` for default questions that are rendered from configuration rather than persisted per post (e.g. the built-in `first_name` field).',
                                                'type': ['null', 'integer'],
                                            },
                                            'label': {
                                                'description': 'Human-readable label rendered above the input on the application form.',
                                                'type': ['null', 'string'],
                                            },
                                            'name': {
                                                'description': 'Stable form-field name used when submitting an application (e.g. `question_42` for a custom question, `first_name` for a default field). Use this when mapping responses back to a question.',
                                                'type': ['null', 'string'],
                                            },
                                            'options': {
                                                'description': 'Selectable answer options for `single_select` and `multi_select` questions. Empty for other answer types.',
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'id': {
                                                            'description': 'Id of the option, stable across edits to the option label.',
                                                            'type': ['null', 'integer'],
                                                        },
                                                        'label': {
                                                            'description': 'Human-readable text shown to the candidate for this option.',
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                            'private': {
                                                'description': 'If `true`, answers to this question are visible only to users with explicit access (e.g. private notes, API-only questions). Defaults to `false`.',
                                                'type': ['null', 'boolean'],
                                            },
                                            'required': {
                                                'description': 'If `true`, the candidate must answer this question to submit the application. `null` for default questions whose required-ness is driven by board-level configuration.',
                                                'type': ['null', 'boolean'],
                                            },
                                        },
                                    },
                                },
                                'title': {
                                    'description': 'Public-facing title shown to candidates on the job board (e.g. `Senior Backend Engineer, Remote`). Distinct from the internal `job.name` — a single job can have several posts with different titles, one per board, language, or geography.',
                                    'type': ['null', 'string'],
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                            },
                            'x-airbyte-entity-name': 'job_posts',
                            'x-airbyte-stream-name': 'job_posts',
                            'x-airbyte-ai-hints': {
                                'summary': 'Published job postings visible on the careers page',
                                'when_to_use': 'Questions about live job postings or careers page content',
                                'trigger_phrases': ['job post', 'careers page', 'published job'],
                                'freshness': 'live',
                                'example_questions': ['What jobs are posted on the careers page?'],
                                'search_strategy': 'Search by title',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse job post object',
                'properties': {
                    'active': {
                        'description': 'If `true`, the post has not been deleted. Deleted posts are excluded by default; pass `active=false` on the list endpoint to retrieve them.',
                        'type': ['null', 'boolean'],
                    },
                    'content': {
                        'description': 'HTML body of the post shown to candidates on the job board. For internal posts this returns the `internal_content` instead. Sanitized server-side — only a limited element/attribute allowlist (including `iframe`, `video`, `source`) survives. `null` while the post is still being scaffolded.',
                        'type': ['null', 'string'],
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'demographic_question_set_id': {
                        'description': 'Id of the demographic question set surfaced to candidates on this post for diversity, equity, and inclusion (DE&I) reporting. `null` when the post does not collect demographic data.',
                        'type': ['null', 'integer'],
                    },
                    'featured': {
                        'description': "If `true`, the post is currently featured on the organization's internal job board and surfaces in the weekly internal-jobs email. Only internal posts can be featured, and at most three can be featured at a time.",
                        'type': ['null', 'boolean'],
                    },
                    'first_published_at': {
                        'description': 'Timestamp the post first transitioned to `live`, in ISO 8601. `null` for posts that have never been published.',
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'id': {
                        'type': ['null', 'integer'],
                    },
                    'internal': {
                        'description': 'If `true`, the post lives on an internal job board and is visible only to existing employees signed in to the internal board. If `false`, the post is external and lives on a public-facing `job_board`. Set by the board the post is associated with at create time.',
                        'type': ['null', 'boolean'],
                    },
                    'internal_content': {
                        'description': 'HTML body shown on the internal job board when the post is also configured as internal. `null` for external-only posts. Same sanitization rules as `content`.',
                        'type': ['null', 'string'],
                    },
                    'job_board_id': {
                        'description': 'Id of the `job_board` this post is published to. Resolves to either an external (careers site, syndicated board) or internal job board depending on `internal`. Each post belongs to exactly one board at a time.',
                        'type': ['null', 'integer'],
                    },
                    'job_id': {
                        'description': 'Id of the parent job (requisition) this post belongs to. A single job can have multiple posts; the job is the source of truth for the hiring team, openings, and interview plan.',
                        'type': ['null', 'integer'],
                    },
                    'language': {
                        'description': 'ISO 639-1 locale of the post, used to render the candidate-facing application form in the matching language (e.g. `en`, `fr`, `ja`). `null` when no locale has been chosen.',
                        'type': ['null', 'string'],
                    },
                    'live': {
                        'description': 'If `true`, the post is published (`job_application_status` is `live`) and its job board is also live. A post on an unpublished board is **not** `live` — its `public_url` returns a 404 until the board is enabled.',
                        'type': ['null', 'boolean'],
                    },
                    'public_url': {
                        'description': 'Canonical public URL of the post on its job board, including the `gh_jid` tracking parameter. `null` when the post has no associated job board or the board has no public URL configured.',
                        'type': ['null', 'string'],
                        'format': 'uri',
                    },
                    'questions': {
                        'description': 'Application form questions presented to candidates on this post, including default questions (resume, cover letter, basic info) and any custom questions configured by the hiring team. Ordered as they appear on the form.',
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'answer_type': {
                                    'description': 'Input type the candidate uses to answer. `short_text` and `long_text` are free-text inputs, `single_select` and `multi_select` use the `options` array, `boolean` is a yes/no, `attachment` accepts a file upload, and `hidden` is set programmatically without rendering a field.',
                                    'type': ['null', 'string'],
                                },
                                'description': {
                                    'description': 'Help text shown below the question label to give candidates additional context. `null` when no help text is set.',
                                    'type': ['null', 'string'],
                                },
                                'id': {
                                    'description': 'Id of the question. `null` for default questions that are rendered from configuration rather than persisted per post (e.g. the built-in `first_name` field).',
                                    'type': ['null', 'integer'],
                                },
                                'label': {
                                    'description': 'Human-readable label rendered above the input on the application form.',
                                    'type': ['null', 'string'],
                                },
                                'name': {
                                    'description': 'Stable form-field name used when submitting an application (e.g. `question_42` for a custom question, `first_name` for a default field). Use this when mapping responses back to a question.',
                                    'type': ['null', 'string'],
                                },
                                'options': {
                                    'description': 'Selectable answer options for `single_select` and `multi_select` questions. Empty for other answer types.',
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'id': {
                                                'description': 'Id of the option, stable across edits to the option label.',
                                                'type': ['null', 'integer'],
                                            },
                                            'label': {
                                                'description': 'Human-readable text shown to the candidate for this option.',
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'private': {
                                    'description': 'If `true`, answers to this question are visible only to users with explicit access (e.g. private notes, API-only questions). Defaults to `false`.',
                                    'type': ['null', 'boolean'],
                                },
                                'required': {
                                    'description': 'If `true`, the candidate must answer this question to submit the application. `null` for default questions whose required-ness is driven by board-level configuration.',
                                    'type': ['null', 'boolean'],
                                },
                            },
                        },
                    },
                    'title': {
                        'description': 'Public-facing title shown to candidates on the job board (e.g. `Senior Backend Engineer, Remote`). Distinct from the internal `job.name` — a single job can have several posts with different titles, one per board, language, or geography.',
                        'type': ['null', 'string'],
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                },
                'x-airbyte-entity-name': 'job_posts',
                'x-airbyte-stream-name': 'job_posts',
                'x-airbyte-ai-hints': {
                    'summary': 'Published job postings visible on the careers page',
                    'when_to_use': 'Questions about live job postings or careers page content',
                    'trigger_phrases': ['job post', 'careers page', 'published job'],
                    'freshness': 'live',
                    'example_questions': ['What jobs are posted on the careers page?'],
                    'search_strategy': 'Search by title',
                },
            },
            ai_hints={
                'summary': 'Published job postings visible on the careers page',
                'when_to_use': 'Questions about live job postings or careers page content',
                'trigger_phrases': ['job post', 'careers page', 'published job'],
                'freshness': 'live',
                'example_questions': ['What jobs are posted on the careers page?'],
                'search_strategy': 'Search by title',
            },
        ),
        EntityDefinition(
            name='jobs',
            stream_name='jobs',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/jobs',
                    action=Action.LIST,
                    description='Returns a cursor-paginated list of jobs.',
                    query_params=[
                        'cursor',
                        'per_page',
                        'ids',
                        'updated_at',
                    ],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                        'updated_at': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse job object',
                            'properties': {
                                'closed_at': {
                                    'description': 'Timestamp the job most recently transitioned to `closed`, in ISO 8601. `null` for jobs that are still `open` or `draft`.',
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'confidential': {
                                    'description': 'If `true`, the job is restricted to users explicitly granted access on the Hiring Team. The legacy Confidential Jobs feature has been sunset — this flag cannot be set on new jobs and is preserved for jobs that already had it enabled.',
                                    'type': ['null', 'boolean'],
                                },
                                'copied_from_id': {
                                    'description': 'Id of the job (typically a template) this job was copied from on creation. `null` when the job was not created from another job.',
                                    'type': ['null', 'integer'],
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'custom_fields': {
                                    'description': "Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                                    'type': ['null', 'object'],
                                    'additionalProperties': {
                                        'type': 'object',
                                        'properties': {
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'type': {
                                                'type': ['null', 'string'],
                                            },
                                            'value': {
                                                'type': [
                                                    'null',
                                                    'string',
                                                    'number',
                                                    'integer',
                                                    'boolean',
                                                    'object',
                                                    'array',
                                                ],
                                            },
                                        },
                                    },
                                },
                                'department_id': {
                                    'description': 'Id of the department this job is assigned to. `null` when no department is set.',
                                    'type': ['null', 'integer'],
                                },
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'is_template': {
                                    'description': 'If `true`, this job is a template used as the source for new jobs rather than a real requisition. Templates do not accept applications; reference them via `template_job_id` on `POST /v3/jobs`.',
                                    'type': ['null', 'boolean'],
                                },
                                'name': {
                                    'description': 'Internal job title shown to the hiring team in Greenhouse (e.g. `Senior Backend Engineer`). Distinct from the external-facing title on each `job_post`.',
                                    'type': ['null', 'string'],
                                },
                                'notes': {
                                    'description': 'Internal HTML notes about the job, surfaced to the hiring team in the Greenhouse UI. Not exposed on public job posts.',
                                    'type': ['null', 'string'],
                                },
                                'office_ids': {
                                    'description': 'Ids of the offices this job is assigned to. A job can span multiple offices; empty array or `null` when no offices are set.',
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'opened_at': {
                                    'description': 'Timestamp the job first transitioned to `open`, in ISO 8601. `null` while the job is still in `draft`.',
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'requisition_id': {
                                    'description': 'Partner-supplied external identifier for the requisition (e.g. an HRIS or ATS code). Free-form string, not unique across the organization, and `null` when no external id has been set.',
                                    'type': ['null', 'string'],
                                },
                                'status': {
                                    'description': 'Lifecycle status of the job. `draft` while it is being scaffolded, `open` once it has at least one open opening, and `closed` after every opening is closed. A job moves to `closed` automatically when its last open opening is closed via `PATCH /v3/openings/{id}`.',
                                    'type': ['null', 'string'],
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                            },
                            'x-airbyte-entity-name': 'jobs',
                            'x-airbyte-stream-name': 'jobs',
                            'x-airbyte-ai-hints': {
                                'summary': 'Job positions with status, department, and hiring plan',
                                'when_to_use': 'Questions about open positions or job details',
                                'trigger_phrases': ['greenhouse job', 'open position', 'job opening'],
                                'freshness': 'live',
                                'example_questions': ['What jobs are open in Greenhouse?'],
                                'search_strategy': 'Search by title or filter by department and status',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse job object',
                'properties': {
                    'closed_at': {
                        'description': 'Timestamp the job most recently transitioned to `closed`, in ISO 8601. `null` for jobs that are still `open` or `draft`.',
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'confidential': {
                        'description': 'If `true`, the job is restricted to users explicitly granted access on the Hiring Team. The legacy Confidential Jobs feature has been sunset — this flag cannot be set on new jobs and is preserved for jobs that already had it enabled.',
                        'type': ['null', 'boolean'],
                    },
                    'copied_from_id': {
                        'description': 'Id of the job (typically a template) this job was copied from on creation. `null` when the job was not created from another job.',
                        'type': ['null', 'integer'],
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'custom_fields': {
                        'description': "Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                        'type': ['null', 'object'],
                        'additionalProperties': {
                            'type': 'object',
                            'properties': {
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'value': {
                                    'type': [
                                        'null',
                                        'string',
                                        'number',
                                        'integer',
                                        'boolean',
                                        'object',
                                        'array',
                                    ],
                                },
                            },
                        },
                    },
                    'department_id': {
                        'description': 'Id of the department this job is assigned to. `null` when no department is set.',
                        'type': ['null', 'integer'],
                    },
                    'id': {
                        'type': ['null', 'integer'],
                    },
                    'is_template': {
                        'description': 'If `true`, this job is a template used as the source for new jobs rather than a real requisition. Templates do not accept applications; reference them via `template_job_id` on `POST /v3/jobs`.',
                        'type': ['null', 'boolean'],
                    },
                    'name': {
                        'description': 'Internal job title shown to the hiring team in Greenhouse (e.g. `Senior Backend Engineer`). Distinct from the external-facing title on each `job_post`.',
                        'type': ['null', 'string'],
                    },
                    'notes': {
                        'description': 'Internal HTML notes about the job, surfaced to the hiring team in the Greenhouse UI. Not exposed on public job posts.',
                        'type': ['null', 'string'],
                    },
                    'office_ids': {
                        'description': 'Ids of the offices this job is assigned to. A job can span multiple offices; empty array or `null` when no offices are set.',
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'opened_at': {
                        'description': 'Timestamp the job first transitioned to `open`, in ISO 8601. `null` while the job is still in `draft`.',
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'requisition_id': {
                        'description': 'Partner-supplied external identifier for the requisition (e.g. an HRIS or ATS code). Free-form string, not unique across the organization, and `null` when no external id has been set.',
                        'type': ['null', 'string'],
                    },
                    'status': {
                        'description': 'Lifecycle status of the job. `draft` while it is being scaffolded, `open` once it has at least one open opening, and `closed` after every opening is closed. A job moves to `closed` automatically when its last open opening is closed via `PATCH /v3/openings/{id}`.',
                        'type': ['null', 'string'],
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                },
                'x-airbyte-entity-name': 'jobs',
                'x-airbyte-stream-name': 'jobs',
                'x-airbyte-ai-hints': {
                    'summary': 'Job positions with status, department, and hiring plan',
                    'when_to_use': 'Questions about open positions or job details',
                    'trigger_phrases': ['greenhouse job', 'open position', 'job opening'],
                    'freshness': 'live',
                    'example_questions': ['What jobs are open in Greenhouse?'],
                    'search_strategy': 'Search by title or filter by department and status',
                },
            },
            ai_hints={
                'summary': 'Job positions with status, department, and hiring plan',
                'when_to_use': 'Questions about open positions or job details',
                'trigger_phrases': ['greenhouse job', 'open position', 'job opening'],
                'freshness': 'live',
                'example_questions': ['What jobs are open in Greenhouse?'],
                'search_strategy': 'Search by title or filter by department and status',
            },
        ),
        EntityDefinition(
            name='offers',
            stream_name='offers',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/offers',
                    action=Action.LIST,
                    description='Returns a cursor-paginated list of offers.',
                    query_params=[
                        'cursor',
                        'per_page',
                        'ids',
                        'updated_at',
                    ],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                        'updated_at': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse offer object',
                            'properties': {
                                'application_id': {
                                    'description': 'Id of the application this offer is extended on. Every offer belongs to exactly one application; the offer is voided if the application is rejected or deleted.',
                                    'type': ['null', 'integer'],
                                },
                                'candidate_id': {
                                    'description': "Id of the candidate (person) receiving this offer. Resolved through the offer's application.",
                                    'type': ['null', 'integer'],
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'custom_fields': {
                                    'description': "Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                                    'type': ['null', 'object'],
                                    'additionalProperties': {
                                        'type': 'object',
                                        'properties': {
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'type': {
                                                'type': ['null', 'string'],
                                            },
                                            'value': {
                                                'type': [
                                                    'null',
                                                    'string',
                                                    'number',
                                                    'integer',
                                                    'boolean',
                                                    'object',
                                                    'array',
                                                ],
                                            },
                                        },
                                    },
                                },
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'job_id': {
                                    'description': "Id of the job this offer's application is on.",
                                    'type': ['null', 'integer'],
                                },
                                'opening_id': {
                                    'description': 'Id of the specific opening this offer is being extended for. `null` when the offer has not yet been linked to an opening.',
                                    'type': ['null', 'integer'],
                                },
                                'resolved_at': {
                                    'description': 'Timestamp the offer was resolved (`Accepted` or `Rejected`), in ISO 8601. Date updates submitted through `PATCH /v3/offers/{id}` are normalized to noon UTC on the supplied date. `null` while the offer is still `Created` or has been superseded as `Deprecated` without a resolution.',
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'sent_on': {
                                    'description': 'Date the offer was sent to the candidate, in ISO 8601 (YYYY-MM-DD). `null` until the offer has been sent.',
                                    'type': ['null', 'string'],
                                    'format': 'date',
                                },
                                'starts_on': {
                                    'description': "Candidate's proposed start date, in ISO 8601 (YYYY-MM-DD). `null` when no start date has been set on the offer.",
                                    'type': ['null', 'string'],
                                    'format': 'date',
                                },
                                'status': {
                                    'description': 'Lifecycle status of the offer. `Created` for offers still being drafted or pending approval, `Accepted` once the candidate accepts, `Rejected` if declined or withdrawn, and `Deprecated` for superseded prior versions (a new offer version replaces an earlier one with this status).',
                                    'type': ['null', 'string'],
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'version': {
                                    'description': 'Revision number of this offer within its application. Greenhouse creates a new offer row (incrementing `version`) whenever a tracked field on an existing offer changes — typically `starts_on`, `opening_id`, or a custom field configured to trigger a new version. Pair with `current_only=true` to filter the list endpoint down to the latest version per application.',
                                    'type': ['null', 'integer'],
                                },
                            },
                            'x-airbyte-entity-name': 'offers',
                            'x-airbyte-stream-name': 'offers',
                            'x-airbyte-ai-hints': {
                                'summary': 'Job offers extended to candidates with terms and status',
                                'when_to_use': 'Questions about offers made or offer status',
                                'trigger_phrases': ['offer', 'job offer', 'offer status'],
                                'freshness': 'live',
                                'example_questions': ['Show pending offers'],
                                'search_strategy': 'Filter by candidate or status',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse offer object',
                'properties': {
                    'application_id': {
                        'description': 'Id of the application this offer is extended on. Every offer belongs to exactly one application; the offer is voided if the application is rejected or deleted.',
                        'type': ['null', 'integer'],
                    },
                    'candidate_id': {
                        'description': "Id of the candidate (person) receiving this offer. Resolved through the offer's application.",
                        'type': ['null', 'integer'],
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'custom_fields': {
                        'description': "Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                        'type': ['null', 'object'],
                        'additionalProperties': {
                            'type': 'object',
                            'properties': {
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'value': {
                                    'type': [
                                        'null',
                                        'string',
                                        'number',
                                        'integer',
                                        'boolean',
                                        'object',
                                        'array',
                                    ],
                                },
                            },
                        },
                    },
                    'id': {
                        'type': ['null', 'integer'],
                    },
                    'job_id': {
                        'description': "Id of the job this offer's application is on.",
                        'type': ['null', 'integer'],
                    },
                    'opening_id': {
                        'description': 'Id of the specific opening this offer is being extended for. `null` when the offer has not yet been linked to an opening.',
                        'type': ['null', 'integer'],
                    },
                    'resolved_at': {
                        'description': 'Timestamp the offer was resolved (`Accepted` or `Rejected`), in ISO 8601. Date updates submitted through `PATCH /v3/offers/{id}` are normalized to noon UTC on the supplied date. `null` while the offer is still `Created` or has been superseded as `Deprecated` without a resolution.',
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'sent_on': {
                        'description': 'Date the offer was sent to the candidate, in ISO 8601 (YYYY-MM-DD). `null` until the offer has been sent.',
                        'type': ['null', 'string'],
                        'format': 'date',
                    },
                    'starts_on': {
                        'description': "Candidate's proposed start date, in ISO 8601 (YYYY-MM-DD). `null` when no start date has been set on the offer.",
                        'type': ['null', 'string'],
                        'format': 'date',
                    },
                    'status': {
                        'description': 'Lifecycle status of the offer. `Created` for offers still being drafted or pending approval, `Accepted` once the candidate accepts, `Rejected` if declined or withdrawn, and `Deprecated` for superseded prior versions (a new offer version replaces an earlier one with this status).',
                        'type': ['null', 'string'],
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'version': {
                        'description': 'Revision number of this offer within its application. Greenhouse creates a new offer row (incrementing `version`) whenever a tracked field on an existing offer changes — typically `starts_on`, `opening_id`, or a custom field configured to trigger a new version. Pair with `current_only=true` to filter the list endpoint down to the latest version per application.',
                        'type': ['null', 'integer'],
                    },
                },
                'x-airbyte-entity-name': 'offers',
                'x-airbyte-stream-name': 'offers',
                'x-airbyte-ai-hints': {
                    'summary': 'Job offers extended to candidates with terms and status',
                    'when_to_use': 'Questions about offers made or offer status',
                    'trigger_phrases': ['offer', 'job offer', 'offer status'],
                    'freshness': 'live',
                    'example_questions': ['Show pending offers'],
                    'search_strategy': 'Filter by candidate or status',
                },
            },
            ai_hints={
                'summary': 'Job offers extended to candidates with terms and status',
                'when_to_use': 'Questions about offers made or offer status',
                'trigger_phrases': ['offer', 'job offer', 'offer status'],
                'freshness': 'live',
                'example_questions': ['Show pending offers'],
                'search_strategy': 'Filter by candidate or status',
            },
        ),
        EntityDefinition(
            name='offices',
            stream_name='offices',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/offices',
                    action=Action.LIST,
                    description='Returns a cursor-paginated list of offices.',
                    query_params=['cursor', 'per_page', 'ids'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse office object',
                            'properties': {
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'external_id': {
                                    'description': 'Stable identifier supplied by the customer or HRIS for cross-system reconciliation. `null` when no external id has been set. Available when the `org_structure_external_id` product flag is enabled.',
                                    'type': ['null', 'string'],
                                },
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'location': {
                                    'description': 'Free-form physical location string for the office (e.g. `New York, NY, USA`). `null` for offices that have no location set, including most remote offices.',
                                    'type': ['null', 'string'],
                                },
                                'name': {
                                    'description': 'Display name of the office (e.g. `San Francisco`, `Remote (US)`). Unique among active offices in the same organization.',
                                    'type': ['null', 'string'],
                                },
                                'parent_id': {
                                    'description': 'Id of the parent office when offices are organized hierarchically. `null` for top-level offices. References another `/v3/offices` row in the same organization.',
                                    'type': ['null', 'integer'],
                                },
                                'primary_in_house_contact_user_id': {
                                    'description': "Id of the Greenhouse user designated as the office's primary internal contact, typically the local recruiting lead. References a `/v3/users` row. `null` when no contact has been assigned.",
                                    'type': ['null', 'integer'],
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                            },
                            'x-airbyte-entity-name': 'offices',
                            'x-airbyte-stream-name': 'offices',
                            'x-airbyte-ai-hints': {
                                'summary': 'Office locations for job postings and hiring',
                                'when_to_use': 'Questions about office locations or where roles are based',
                                'trigger_phrases': ['office', 'office location', 'job location'],
                                'freshness': 'static',
                                'example_questions': ['What office locations are configured?'],
                                'search_strategy': 'Search by name',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse office object',
                'properties': {
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'external_id': {
                        'description': 'Stable identifier supplied by the customer or HRIS for cross-system reconciliation. `null` when no external id has been set. Available when the `org_structure_external_id` product flag is enabled.',
                        'type': ['null', 'string'],
                    },
                    'id': {
                        'type': ['null', 'integer'],
                    },
                    'location': {
                        'description': 'Free-form physical location string for the office (e.g. `New York, NY, USA`). `null` for offices that have no location set, including most remote offices.',
                        'type': ['null', 'string'],
                    },
                    'name': {
                        'description': 'Display name of the office (e.g. `San Francisco`, `Remote (US)`). Unique among active offices in the same organization.',
                        'type': ['null', 'string'],
                    },
                    'parent_id': {
                        'description': 'Id of the parent office when offices are organized hierarchically. `null` for top-level offices. References another `/v3/offices` row in the same organization.',
                        'type': ['null', 'integer'],
                    },
                    'primary_in_house_contact_user_id': {
                        'description': "Id of the Greenhouse user designated as the office's primary internal contact, typically the local recruiting lead. References a `/v3/users` row. `null` when no contact has been assigned.",
                        'type': ['null', 'integer'],
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                },
                'x-airbyte-entity-name': 'offices',
                'x-airbyte-stream-name': 'offices',
                'x-airbyte-ai-hints': {
                    'summary': 'Office locations for job postings and hiring',
                    'when_to_use': 'Questions about office locations or where roles are based',
                    'trigger_phrases': ['office', 'office location', 'job location'],
                    'freshness': 'static',
                    'example_questions': ['What office locations are configured?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Office locations for job postings and hiring',
                'when_to_use': 'Questions about office locations or where roles are based',
                'trigger_phrases': ['office', 'office location', 'job location'],
                'freshness': 'static',
                'example_questions': ['What office locations are configured?'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='sources',
            stream_name='sources',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/sources',
                    action=Action.LIST,
                    description='Returns a cursor-paginated list of sources.',
                    query_params=['cursor', 'per_page', 'ids'],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse source object',
                            'properties': {
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'description': 'Display name of the source as recruiters see it in Greenhouse (e.g. `LinkedIn (Prospecting)`, `Indeed`, `Referral`, `Internal Applicant`, or a custom agency name). For organization-specific sources this is the label the org configured; for global Greenhouse sources it is the standard public name.',
                                    'type': ['null', 'string'],
                                },
                                'type': {
                                    'description': 'The sourcing strategy this source rolls up to — the broader category used for reporting. Sources are grouped under sourcing strategies such as `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`, `Company marketing`, `In person event`, `MyGreenhouse`, and `Other`. Use the strategy when aggregating candidate volume by channel; use the source itself when reporting on a specific channel within that category.',
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'description': 'Id of the sourcing strategy. References the same strategy across all sources in the organization that roll up to it.',
                                            'type': ['null', 'integer'],
                                        },
                                        'name': {
                                            'description': 'Display name of the sourcing strategy used in Greenhouse reporting (e.g. `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`).',
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                            },
                            'x-airbyte-entity-name': 'sources',
                            'x-airbyte-stream-name': 'sources',
                            'x-airbyte-ai-hints': {
                                'summary': 'Candidate sourcing channels (referrals, job boards, agencies)',
                                'when_to_use': 'Questions about where candidates are coming from',
                                'trigger_phrases': ['candidate source', 'referral', 'sourcing channel'],
                                'freshness': 'static',
                                'example_questions': ['What sourcing channels are tracked in Greenhouse?'],
                                'search_strategy': 'Search by name',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse source object',
                'properties': {
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'id': {
                        'type': ['null', 'integer'],
                    },
                    'name': {
                        'description': 'Display name of the source as recruiters see it in Greenhouse (e.g. `LinkedIn (Prospecting)`, `Indeed`, `Referral`, `Internal Applicant`, or a custom agency name). For organization-specific sources this is the label the org configured; for global Greenhouse sources it is the standard public name.',
                        'type': ['null', 'string'],
                    },
                    'type': {
                        'description': 'The sourcing strategy this source rolls up to — the broader category used for reporting. Sources are grouped under sourcing strategies such as `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`, `Company marketing`, `In person event`, `MyGreenhouse`, and `Other`. Use the strategy when aggregating candidate volume by channel; use the source itself when reporting on a specific channel within that category.',
                        'type': ['null', 'object'],
                        'properties': {
                            'id': {
                                'description': 'Id of the sourcing strategy. References the same strategy across all sources in the organization that roll up to it.',
                                'type': ['null', 'integer'],
                            },
                            'name': {
                                'description': 'Display name of the sourcing strategy used in Greenhouse reporting (e.g. `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`).',
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                },
                'x-airbyte-entity-name': 'sources',
                'x-airbyte-stream-name': 'sources',
                'x-airbyte-ai-hints': {
                    'summary': 'Candidate sourcing channels (referrals, job boards, agencies)',
                    'when_to_use': 'Questions about where candidates are coming from',
                    'trigger_phrases': ['candidate source', 'referral', 'sourcing channel'],
                    'freshness': 'static',
                    'example_questions': ['What sourcing channels are tracked in Greenhouse?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Candidate sourcing channels (referrals, job boards, agencies)',
                'when_to_use': 'Questions about where candidates are coming from',
                'trigger_phrases': ['candidate source', 'referral', 'sourcing channel'],
                'freshness': 'static',
                'example_questions': ['What sourcing channels are tracked in Greenhouse?'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='users',
            stream_name='users',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/users',
                    action=Action.LIST,
                    description='Returns a cursor-paginated list of users.',
                    query_params=[
                        'cursor',
                        'per_page',
                        'ids',
                        'updated_at',
                        'show_service_accounts',
                    ],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                        'updated_at': {'type': 'string', 'required': False},
                        'show_service_accounts': {
                            'type': 'boolean',
                            'required': False,
                            'default': True,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse user object',
                            'properties': {
                                'agency_id': {
                                    'description': 'Id of the staffing agency this user belongs to, when the user is an external agency recruiter rather than an employee of your organization. `null` for in-house users.',
                                    'type': ['null', 'integer'],
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'custom_fields': {
                                    'description': "Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                                    'type': ['null', 'object'],
                                    'additionalProperties': {
                                        'type': 'object',
                                        'properties': {
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                            'type': {
                                                'type': ['null', 'string'],
                                            },
                                            'value': {
                                                'type': [
                                                    'null',
                                                    'string',
                                                    'number',
                                                    'integer',
                                                    'boolean',
                                                    'object',
                                                    'array',
                                                ],
                                            },
                                        },
                                    },
                                },
                                'deactivated': {
                                    'description': 'Whether the user has been deactivated. Deactivated users cannot sign in or be assigned to new jobs, but their historical activity (notes, scorecards, emails) is preserved. Toggle via `POST /v3/users/{id}/deactivate` and `POST /v3/users/{id}/activate`.',
                                    'type': ['null', 'boolean'],
                                },
                                'department_ids': {
                                    'description': 'Ids of the departments this user is assigned to. Used to scope future job permissions and to filter the user list by department. Empty when the user is not pinned to any department.',
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'emails': {
                                    'description': "All email addresses on the user's account, including the primary address and any additional verified addresses.",
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'string'],
                                    },
                                },
                                'employee_id': {
                                    'description': "Partner-supplied external employee identifier, typically the user's HRIS or payroll id. Free-form string; not unique across organizations and `null` when no employee id has been set.",
                                    'type': ['null', 'string'],
                                },
                                'first_name': {
                                    'type': ['null', 'string'],
                                },
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'interviewer_tags': {
                                    'description': "Interviewer tags applied to this user — the labeled skill or panel groupings (e.g. `Senior Engineer`, `Bar Raiser`) used to suggest qualified interviewers when building an interview plan. Each entry pairs the tag's `id` with its `name`.",
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'integer'],
                                            },
                                            'name': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'job_title': {
                                    'description': "Free-form job title set on the user's Greenhouse profile (e.g. `Senior Recruiter`). Not synchronized with any HRIS title.",
                                    'type': ['null', 'string'],
                                },
                                'last_name': {
                                    'type': ['null', 'string'],
                                },
                                'linked_candidate_ids': {
                                    'description': 'Ids of candidate records linked to this user. Populated when an employee is represented by both a user record (for Greenhouse access) and a candidate record (for past or internal applications).',
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'name': {
                                    'description': 'Concatenation of `first_name` and `last_name` rendered as a single display string. Provided for convenience; partners that need either component should read `first_name`/`last_name` directly.',
                                    'type': ['null', 'string'],
                                },
                                'office_ids': {
                                    'description': 'Ids of the offices this user is assigned to. Used to scope future job permissions and to filter the user list by office. Empty when the user is not pinned to any office.',
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'integer'],
                                    },
                                },
                                'primary_email': {
                                    'description': "Primary email address on the user's account. Sign-in identifier and the address Greenhouse uses for outbound mail; additional verified addresses are not surfaced here. Service accounts (integration/ISU users) have no email and are excluded from this endpoint by default; when included via `show_service_accounts=true`, their `primary_email` is an empty string.",
                                    'type': ['null', 'string'],
                                },
                                'site_admin': {
                                    'description': 'Whether the user holds the Site Admin role. Site admins have unrestricted access to every non-confidential job and to organization-level settings. Demote a site admin to a Basic user with `POST /v3/users/{id}/revoke_permissions`.',
                                    'type': ['null', 'boolean'],
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                            },
                            'x-airbyte-entity-name': 'users',
                            'x-airbyte-stream-name': 'users',
                            'x-airbyte-ai-hints': {
                                'summary': 'Greenhouse users (recruiters, coordinators, hiring managers)',
                                'when_to_use': 'Looking up recruiter or hiring team details',
                                'trigger_phrases': ['greenhouse user', 'recruiter', 'hiring manager'],
                                'freshness': 'live',
                                'example_questions': ['Who are the recruiters in Greenhouse?'],
                                'search_strategy': 'Search by name or email',
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse user object',
                'properties': {
                    'agency_id': {
                        'description': 'Id of the staffing agency this user belongs to, when the user is an external agency recruiter rather than an employee of your organization. `null` for in-house users.',
                        'type': ['null', 'integer'],
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                    'custom_fields': {
                        'description': "Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                        'type': ['null', 'object'],
                        'additionalProperties': {
                            'type': 'object',
                            'properties': {
                                'name': {
                                    'type': ['null', 'string'],
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'value': {
                                    'type': [
                                        'null',
                                        'string',
                                        'number',
                                        'integer',
                                        'boolean',
                                        'object',
                                        'array',
                                    ],
                                },
                            },
                        },
                    },
                    'deactivated': {
                        'description': 'Whether the user has been deactivated. Deactivated users cannot sign in or be assigned to new jobs, but their historical activity (notes, scorecards, emails) is preserved. Toggle via `POST /v3/users/{id}/deactivate` and `POST /v3/users/{id}/activate`.',
                        'type': ['null', 'boolean'],
                    },
                    'department_ids': {
                        'description': 'Ids of the departments this user is assigned to. Used to scope future job permissions and to filter the user list by department. Empty when the user is not pinned to any department.',
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'emails': {
                        'description': "All email addresses on the user's account, including the primary address and any additional verified addresses.",
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'string'],
                        },
                    },
                    'employee_id': {
                        'description': "Partner-supplied external employee identifier, typically the user's HRIS or payroll id. Free-form string; not unique across organizations and `null` when no employee id has been set.",
                        'type': ['null', 'string'],
                    },
                    'first_name': {
                        'type': ['null', 'string'],
                    },
                    'id': {
                        'type': ['null', 'integer'],
                    },
                    'interviewer_tags': {
                        'description': "Interviewer tags applied to this user — the labeled skill or panel groupings (e.g. `Senior Engineer`, `Bar Raiser`) used to suggest qualified interviewers when building an interview plan. Each entry pairs the tag's `id` with its `name`.",
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'integer'],
                                },
                                'name': {
                                    'type': ['null', 'string'],
                                },
                            },
                        },
                    },
                    'job_title': {
                        'description': "Free-form job title set on the user's Greenhouse profile (e.g. `Senior Recruiter`). Not synchronized with any HRIS title.",
                        'type': ['null', 'string'],
                    },
                    'last_name': {
                        'type': ['null', 'string'],
                    },
                    'linked_candidate_ids': {
                        'description': 'Ids of candidate records linked to this user. Populated when an employee is represented by both a user record (for Greenhouse access) and a candidate record (for past or internal applications).',
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'name': {
                        'description': 'Concatenation of `first_name` and `last_name` rendered as a single display string. Provided for convenience; partners that need either component should read `first_name`/`last_name` directly.',
                        'type': ['null', 'string'],
                    },
                    'office_ids': {
                        'description': 'Ids of the offices this user is assigned to. Used to scope future job permissions and to filter the user list by office. Empty when the user is not pinned to any office.',
                        'type': ['null', 'array'],
                        'items': {
                            'type': ['null', 'integer'],
                        },
                    },
                    'primary_email': {
                        'description': "Primary email address on the user's account. Sign-in identifier and the address Greenhouse uses for outbound mail; additional verified addresses are not surfaced here. Service accounts (integration/ISU users) have no email and are excluded from this endpoint by default; when included via `show_service_accounts=true`, their `primary_email` is an empty string.",
                        'type': ['null', 'string'],
                    },
                    'site_admin': {
                        'description': 'Whether the user holds the Site Admin role. Site admins have unrestricted access to every non-confidential job and to organization-level settings. Demote a site admin to a Basic user with `POST /v3/users/{id}/revoke_permissions`.',
                        'type': ['null', 'boolean'],
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                    },
                },
                'x-airbyte-entity-name': 'users',
                'x-airbyte-stream-name': 'users',
                'x-airbyte-ai-hints': {
                    'summary': 'Greenhouse users (recruiters, coordinators, hiring managers)',
                    'when_to_use': 'Looking up recruiter or hiring team details',
                    'trigger_phrases': ['greenhouse user', 'recruiter', 'hiring manager'],
                    'freshness': 'live',
                    'example_questions': ['Who are the recruiters in Greenhouse?'],
                    'search_strategy': 'Search by name or email',
                },
            },
            ai_hints={
                'summary': 'Greenhouse users (recruiters, coordinators, hiring managers)',
                'when_to_use': 'Looking up recruiter or hiring team details',
                'trigger_phrases': ['greenhouse user', 'recruiter', 'hiring manager'],
                'freshness': 'live',
                'example_questions': ['Who are the recruiters in Greenhouse?'],
                'search_strategy': 'Search by name or email',
            },
        ),
        EntityDefinition(
            name='attachments',
            actions=[Action.LIST, Action.DOWNLOAD],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/attachments',
                    action=Action.LIST,
                    description='Returns a cursor-paginated list of attachments.',
                    query_params=[
                        'cursor',
                        'per_page',
                        'ids',
                        'updated_at',
                        'application_ids',
                        'candidate_ids',
                        'type',
                    ],
                    query_params_schema={
                        'cursor': {'type': 'string', 'required': False},
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 500,
                            'minimum': 1,
                            'maximum': 500,
                        },
                        'ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                        'updated_at': {'type': 'string', 'required': False},
                        'application_ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                        'candidate_ids': {
                            'type': 'array',
                            'required': False,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                        'type': {
                            'type': 'string',
                            'required': False,
                            'enum': [
                                'resume',
                                'cover_letter',
                                'take_home_test',
                                'offer_packet',
                                'offer_letter',
                                'signed_offer_letter',
                                'other',
                                'form_attachment',
                                'midfunnel_agreement',
                                'automated_agreement',
                            ],
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'File associated with a Greenhouse application',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique attachment identifier'},
                                'application_id': {'type': 'integer', 'description': 'Application this attachment belongs to'},
                                'candidate_id': {
                                    'type': ['integer', 'null'],
                                    'description': 'Candidate resolved through the application, when available',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the attachment was created',
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the attachment was last updated',
                                },
                                'filename': {'type': 'string', 'description': 'Name of the attached file'},
                                'url': {
                                    'type': 'string',
                                    'format': 'uri',
                                    'description': 'Time-limited URL to download the file. The URL expires after seven days,\nso refetch the attachment before downloading when the cached URL is stale.\n',
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'resume',
                                        'cover_letter',
                                        'take_home_test',
                                        'offer_packet',
                                        'offer_letter',
                                        'signed_offer_letter',
                                        'other',
                                        'form_attachment',
                                        'midfunnel_agreement',
                                        'automated_agreement',
                                    ],
                                    'description': 'Type of attachment',
                                },
                            },
                        },
                    },
                    meta_extractor={'next': '@link.next'},
                ),
                Action.DOWNLOAD: EndpointDefinition(
                    method='GET',
                    path='/attachments:download',
                    path_override=PathOverrideConfig(
                        path='/attachments',
                    ),
                    action=Action.DOWNLOAD,
                    description='Looks up an attachment by ID and follows its current time-limited download URL.',
                    query_params=['ids'],
                    query_params_schema={
                        'ids': {
                            'type': 'array',
                            'required': True,
                            'items': {'type': 'integer'},
                            'style': 'form',
                            'explode': False,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'File associated with a Greenhouse application',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique attachment identifier'},
                                'application_id': {'type': 'integer', 'description': 'Application this attachment belongs to'},
                                'candidate_id': {
                                    'type': ['integer', 'null'],
                                    'description': 'Candidate resolved through the application, when available',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the attachment was created',
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the attachment was last updated',
                                },
                                'filename': {'type': 'string', 'description': 'Name of the attached file'},
                                'url': {
                                    'type': 'string',
                                    'format': 'uri',
                                    'description': 'Time-limited URL to download the file. The URL expires after seven days,\nso refetch the attachment before downloading when the cached URL is stale.\n',
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'resume',
                                        'cover_letter',
                                        'take_home_test',
                                        'offer_packet',
                                        'offer_letter',
                                        'signed_offer_letter',
                                        'other',
                                        'form_attachment',
                                        'midfunnel_agreement',
                                        'automated_agreement',
                                    ],
                                    'description': 'Type of attachment',
                                },
                            },
                        },
                    },
                    file_field='[0].url',
                ),
            },
        ),
    ],
    context_store=CacheConfig(
        entities=[
            CacheEntityConfig(
                entity='applications',
                suggested=True,
                x_airbyte_name='applications',
                fields=[
                    CacheFieldConfig(
                        name='agency_note_id',
                        type=['null', 'integer'],
                        description='Id of the note created when the candidate was submitted by an agency, or `null` if the application did not come through an agency.',
                    ),
                    CacheFieldConfig(
                        name='answers',
                        type=['null', 'array'],
                        description="Free-text answers the candidate provided on the job post application form. Each entry pairs the question text with the candidate's answer.",
                    ),
                    CacheFieldConfig(
                        name='candidate_id',
                        type=['null', 'integer'],
                        description='Id of the candidate (person) this application belongs to.',
                    ),
                    CacheFieldConfig(
                        name='coordinator_id',
                        type=['null', 'integer'],
                        description="Id of the user assigned as coordinator on the application's job, or `null` when unassigned.",
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Created at from the Greenhouse v3 applications record.',
                    ),
                    CacheFieldConfig(
                        name='custom_fields',
                        type=['null', 'object'],
                        description="Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Id from the Greenhouse v3 applications record.',
                    ),
                    CacheFieldConfig(
                        name='job_id',
                        type=['null', 'integer'],
                        description='Id of the job this application is on. `null` for jobless prospect applications.',
                    ),
                    CacheFieldConfig(
                        name='job_interview_stage_id',
                        type=['null', 'integer'],
                        description='Id of the job interview stage definition (see `GET /v3/job_interview_stages`) the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state.',
                    ),
                    CacheFieldConfig(
                        name='job_post_id',
                        type=['null', 'integer'],
                        description='Id of the job post the candidate applied through, or `null` if the application was created internally rather than from a posted role.',
                    ),
                    CacheFieldConfig(
                        name='last_activity_at',
                        type=['null', 'string'],
                        description='Timestamp of the most recent activity on this application (notes, emails, stage changes, etc.), in ISO 8601.',
                    ),
                    CacheFieldConfig(
                        name='location_address',
                        type=['null', 'string'],
                        description="Free-form location string captured on the application (typically from the job post's location question).",
                    ),
                    CacheFieldConfig(
                        name='needs_decision',
                        type=['null', 'boolean'],
                        description='`true` when the application is waiting on a hiring-team decision (scorecard completion, advance/reject, etc.) in its current stage.',
                    ),
                    CacheFieldConfig(
                        name='prospect',
                        type=['null', 'boolean'],
                        description='`true` for prospect applications (sourced candidates not yet attached to a single job), `false` for candidate applications on a specific job.',
                    ),
                    CacheFieldConfig(
                        name='prospective_job_ids',
                        type=['null', 'array'],
                        description='For prospect applications, the ids of jobs the prospect is being considered for. Empty for non-prospect applications and for jobless prospects.',
                    ),
                    CacheFieldConfig(
                        name='recruiter_id',
                        type=['null', 'integer'],
                        description="Id of the user assigned as recruiter on the application's job, or `null` when unassigned.",
                    ),
                    CacheFieldConfig(
                        name='referrer_id',
                        type=['null', 'integer'],
                        description='Id of the referrer who credited this application, or `null` if there was no referral. References a referrer, not a Greenhouse user.',
                    ),
                    CacheFieldConfig(
                        name='rejected_at',
                        type=['null', 'string'],
                        description='Timestamp the application was rejected, in ISO 8601. `null` for applications that have not been rejected.',
                    ),
                    CacheFieldConfig(
                        name='rejection_reason_id',
                        type=['null', 'integer'],
                        description='Id of the rejection reason selected for the application. References a `/v3/rejection_reasons` row scoped to the organization. `null` when the application was rejected without a reason, or has not been rejected.',
                    ),
                    CacheFieldConfig(
                        name='source_id',
                        type=['null', 'integer'],
                        description='Id of the source the application is attributed to (e.g. a job board, an event, an employee referral source). `null` if no source is set.',
                    ),
                    CacheFieldConfig(
                        name='stage_id',
                        type=['null', 'integer'],
                        description='Id of the interview stage the candidate is currently in for this application. `null` for prospect applications and applications in a terminal state.',
                    ),
                    CacheFieldConfig(
                        name='stage_name',
                        type=['null', 'string'],
                        description="Display name of the candidate's current interview stage on this application.",
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Lifecycle status of the application. `in_process` for active candidates, `rejected` for rejected applications, `hired` once an offer is closed and the hire endpoint has fired, and `converted` for prospect applications that have been promoted to a candidate application via `convert_to_candidate`.',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='Updated at from the Greenhouse v3 applications record.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='candidates',
                suggested=True,
                x_airbyte_name='candidates',
                fields=[
                    CacheFieldConfig(
                        name='addresses',
                        type=['null', 'array'],
                        description="Postal addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `home`, `work`, or `other`.",
                    ),
                    CacheFieldConfig(
                        name='can_email',
                        type=['null', 'boolean'],
                        description='Whether this candidate has consented to receive email communication from your organization.',
                    ),
                    CacheFieldConfig(
                        name='company',
                        type=['null', 'string'],
                        description="Candidate's current company, as entered on their profile.",
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Created at from the Greenhouse v3 candidates record.',
                    ),
                    CacheFieldConfig(
                        name='custom_fields',
                        type=['null', 'object'],
                        description="Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                    ),
                    CacheFieldConfig(
                        name='email_addresses',
                        type=['null', 'array'],
                        description="Email addresses on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `work`, or `other`.",
                    ),
                    CacheFieldConfig(
                        name='first_name',
                        type=['null', 'string'],
                        description='First name from the Greenhouse v3 candidates record.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Id from the Greenhouse v3 candidates record.',
                    ),
                    CacheFieldConfig(
                        name='last_activity_at',
                        type=['null', 'string'],
                        description="Timestamp of the most recent activity on any of the candidate's applications (notes, emails, stage changes, etc.), in ISO 8601.",
                    ),
                    CacheFieldConfig(
                        name='last_name',
                        type=['null', 'string'],
                        description='Last name from the Greenhouse v3 candidates record.',
                    ),
                    CacheFieldConfig(
                        name='linked_user_ids',
                        type=['null', 'array'],
                        description='Ids of Greenhouse users linked to this candidate (employees represented by both a user record and a candidate record).',
                    ),
                    CacheFieldConfig(
                        name='phone_numbers',
                        type=['null', 'array'],
                        description="Phone numbers on the candidate's profile. Each entry pairs the `value` with a `type` such as `mobile`, `home`, `work`, `skype`, or `other`.",
                    ),
                    CacheFieldConfig(
                        name='preferred_name',
                        type=['null', 'string'],
                        description='Preferred or chosen name the candidate goes by, when different from their legal first name.',
                    ),
                    CacheFieldConfig(
                        name='private',
                        type=['null', 'boolean'],
                        description='If true, the candidate is restricted to users with `View Private Candidates` access. Defaults to `false`.',
                    ),
                    CacheFieldConfig(
                        name='social_media_addresses',
                        type=['null', 'array'],
                        description="Social media handles or URLs on the candidate's profile. Social entries are untyped — only the `value` is returned.",
                    ),
                    CacheFieldConfig(
                        name='tags',
                        type=['null', 'array'],
                        description='Candidate tag names applied to this candidate within your organization.',
                    ),
                    CacheFieldConfig(
                        name='time_zone',
                        type=['null', 'string'],
                        description="Candidate's time zone as a Rails-style identifier (for example `Eastern Time (US & Canada)`).",
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description="Candidate's current job title, as entered on their profile.",
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='Updated at from the Greenhouse v3 candidates record.',
                    ),
                    CacheFieldConfig(
                        name='website_addresses',
                        type=['null', 'array'],
                        description="Personal websites or portfolio URLs on the candidate's profile. Each entry pairs the `value` with a `type` such as `personal`, `company`, `portfolio`, `blog`, or `other`.",
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='departments',
                x_airbyte_name='departments',
                fields=[
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Created at from the Greenhouse v3 departments record.',
                    ),
                    CacheFieldConfig(
                        name='external_id',
                        type=['null', 'string'],
                        description='Partner-supplied identifier for the department, typically the matching id from an HRIS or other external system. Free-form string and `null` when no external id has been set.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Id from the Greenhouse v3 departments record.',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Display name of the department (e.g. `Engineering`, `Marketing`).',
                    ),
                    CacheFieldConfig(
                        name='parent_id',
                        type=['null', 'integer'],
                        description="Id of the parent department in the organization's department tree. `null` for top-level departments. References another `/v3/departments` row.",
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='Updated at from the Greenhouse v3 departments record.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='job_posts',
                suggested=True,
                x_airbyte_name='job_posts',
                fields=[
                    CacheFieldConfig(
                        name='active',
                        type=['null', 'boolean'],
                        description='If `true`, the post has not been deleted. Deleted posts are excluded by default; pass `active=false` on the list endpoint to retrieve them.',
                    ),
                    CacheFieldConfig(
                        name='content',
                        type=['null', 'string'],
                        description='HTML body of the post shown to candidates on the job board. For internal posts this returns the `internal_content` instead. Sanitized server-side — only a limited element/attribute allowlist (including `iframe`, `video`, `source`) survives. `null` while the post is still being scaffolded.',
                        x_airbyte_semantic_search=SemanticSearchConfig(
                            content_type='html',
                            samples=[
                                SemanticSample(
                                    name='title',
                                    path='/title',
                                ),
                                SemanticSample(
                                    name='job_post_content',
                                    windowed=True,
                                    sampling=SemanticSampling(
                                        sample_type='whole',
                                        unit_label='job_post',
                                    ),
                                ),
                            ],
                            windowing=SemanticWindowing(
                                context_max_chars=2048,
                            ),
                            embedding=SemanticEmbedding(
                                model='text-embedding-3-small',
                                template='{title}\n\n{job_post_content}',
                            ),
                            metadata=[
                                SemanticMetadataField(
                                    name='id',
                                    path='/id',
                                ),
                                SemanticMetadataField(
                                    name='updated_at',
                                    path='/updated_at',
                                ),
                                SemanticMetadataField(
                                    name='title',
                                    path='/title',
                                ),
                                SemanticMetadataField(
                                    name='job_id',
                                    path='/job_id',
                                ),
                                SemanticMetadataField(
                                    name='live',
                                    path='/live',
                                ),
                                SemanticMetadataField(
                                    name='internal',
                                    path='/internal',
                                ),
                                SemanticMetadataField(
                                    name='first_published_at',
                                    path='/first_published_at',
                                ),
                                SemanticMetadataField(
                                    name='created_at',
                                    path='/created_at',
                                ),
                            ],
                        ),
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Created at from the Greenhouse v3 job posts record.',
                    ),
                    CacheFieldConfig(
                        name='demographic_question_set_id',
                        type=['null', 'integer'],
                        description='Id of the demographic question set surfaced to candidates on this post for diversity, equity, and inclusion (DE&I) reporting. `null` when the post does not collect demographic data.',
                    ),
                    CacheFieldConfig(
                        name='featured',
                        type=['null', 'boolean'],
                        description="If `true`, the post is currently featured on the organization's internal job board and surfaces in the weekly internal-jobs email. Only internal posts can be featured, and at most three can be featured at a time.",
                    ),
                    CacheFieldConfig(
                        name='first_published_at',
                        type=['null', 'string'],
                        description='Timestamp the post first transitioned to `live`, in ISO 8601. `null` for posts that have never been published.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Id from the Greenhouse v3 job posts record.',
                    ),
                    CacheFieldConfig(
                        name='internal',
                        type=['null', 'boolean'],
                        description='If `true`, the post lives on an internal job board and is visible only to existing employees signed in to the internal board. If `false`, the post is external and lives on a public-facing `job_board`. Set by the board the post is associated with at create time.',
                    ),
                    CacheFieldConfig(
                        name='internal_content',
                        type=['null', 'string'],
                        description='HTML body shown on the internal job board when the post is also configured as internal. `null` for external-only posts. Same sanitization rules as `content`.',
                        x_airbyte_semantic_search=SemanticSearchConfig(
                            content_type='html',
                            samples=[
                                SemanticSample(
                                    name='title',
                                    path='/title',
                                ),
                                SemanticSample(
                                    name='internal_job_post_content',
                                    windowed=True,
                                    sampling=SemanticSampling(
                                        sample_type='whole',
                                        unit_label='internal_job_post',
                                    ),
                                ),
                            ],
                            windowing=SemanticWindowing(
                                context_max_chars=2048,
                            ),
                            embedding=SemanticEmbedding(
                                model='text-embedding-3-small',
                                template='{title}\n\n{internal_job_post_content}',
                            ),
                            metadata=[
                                SemanticMetadataField(
                                    name='id',
                                    path='/id',
                                ),
                                SemanticMetadataField(
                                    name='updated_at',
                                    path='/updated_at',
                                ),
                                SemanticMetadataField(
                                    name='title',
                                    path='/title',
                                ),
                                SemanticMetadataField(
                                    name='job_id',
                                    path='/job_id',
                                ),
                                SemanticMetadataField(
                                    name='live',
                                    path='/live',
                                ),
                                SemanticMetadataField(
                                    name='internal',
                                    path='/internal',
                                ),
                                SemanticMetadataField(
                                    name='first_published_at',
                                    path='/first_published_at',
                                ),
                                SemanticMetadataField(
                                    name='created_at',
                                    path='/created_at',
                                ),
                            ],
                        ),
                    ),
                    CacheFieldConfig(
                        name='job_board_id',
                        type=['null', 'integer'],
                        description='Id of the `job_board` this post is published to. Resolves to either an external (careers site, syndicated board) or internal job board depending on `internal`. Each post belongs to exactly one board at a time.',
                    ),
                    CacheFieldConfig(
                        name='job_id',
                        type=['null', 'integer'],
                        description='Id of the parent job (requisition) this post belongs to. A single job can have multiple posts; the job is the source of truth for the hiring team, openings, and interview plan.',
                    ),
                    CacheFieldConfig(
                        name='language',
                        type=['null', 'string'],
                        description='ISO 639-1 locale of the post, used to render the candidate-facing application form in the matching language (e.g. `en`, `fr`, `ja`). `null` when no locale has been chosen.',
                    ),
                    CacheFieldConfig(
                        name='live',
                        type=['null', 'boolean'],
                        description='If `true`, the post is published (`job_application_status` is `live`) and its job board is also live. A post on an unpublished board is **not** `live` — its `public_url` returns a 404 until the board is enabled.',
                    ),
                    CacheFieldConfig(
                        name='public_url',
                        type=['null', 'string'],
                        description='Canonical public URL of the post on its job board, including the `gh_jid` tracking parameter. `null` when the post has no associated job board or the board has no public URL configured.',
                    ),
                    CacheFieldConfig(
                        name='questions',
                        type=['null', 'array'],
                        description='Application form questions presented to candidates on this post, including default questions (resume, cover letter, basic info) and any custom questions configured by the hiring team. Ordered as they appear on the form.',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='Public-facing title shown to candidates on the job board (e.g. `Senior Backend Engineer, Remote`). Distinct from the internal `job.name` — a single job can have several posts with different titles, one per board, language, or geography.',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='Updated at from the Greenhouse v3 job posts record.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='jobs',
                suggested=True,
                x_airbyte_name='jobs',
                fields=[
                    CacheFieldConfig(
                        name='closed_at',
                        type=['null', 'string'],
                        description='Timestamp the job most recently transitioned to `closed`, in ISO 8601. `null` for jobs that are still `open` or `draft`.',
                    ),
                    CacheFieldConfig(
                        name='confidential',
                        type=['null', 'boolean'],
                        description='If `true`, the job is restricted to users explicitly granted access on the Hiring Team. The legacy Confidential Jobs feature has been sunset — this flag cannot be set on new jobs and is preserved for jobs that already had it enabled.',
                    ),
                    CacheFieldConfig(
                        name='copied_from_id',
                        type=['null', 'integer'],
                        description='Id of the job (typically a template) this job was copied from on creation. `null` when the job was not created from another job.',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Created at from the Greenhouse v3 jobs record.',
                    ),
                    CacheFieldConfig(
                        name='custom_fields',
                        type=['null', 'object'],
                        description="Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                    ),
                    CacheFieldConfig(
                        name='department_id',
                        type=['null', 'integer'],
                        description='Id of the department this job is assigned to. `null` when no department is set.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Id from the Greenhouse v3 jobs record.',
                    ),
                    CacheFieldConfig(
                        name='is_template',
                        type=['null', 'boolean'],
                        description='If `true`, this job is a template used as the source for new jobs rather than a real requisition. Templates do not accept applications; reference them via `template_job_id` on `POST /v3/jobs`.',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Internal job title shown to the hiring team in Greenhouse (e.g. `Senior Backend Engineer`). Distinct from the external-facing title on each `job_post`.',
                    ),
                    CacheFieldConfig(
                        name='notes',
                        type=['null', 'string'],
                        description='Internal HTML notes about the job, surfaced to the hiring team in the Greenhouse UI. Not exposed on public job posts.',
                        x_airbyte_semantic_search=SemanticSearchConfig(
                            content_type='html',
                            samples=[
                                SemanticSample(
                                    name='name',
                                    path='/name',
                                ),
                                SemanticSample(
                                    name='job_notes',
                                    windowed=True,
                                    sampling=SemanticSampling(
                                        sample_type='whole',
                                        unit_label='job',
                                    ),
                                ),
                            ],
                            windowing=SemanticWindowing(
                                context_max_chars=2048,
                            ),
                            embedding=SemanticEmbedding(
                                model='text-embedding-3-small',
                                template='{name}\n\n{job_notes}',
                            ),
                            metadata=[
                                SemanticMetadataField(
                                    name='id',
                                    path='/id',
                                ),
                                SemanticMetadataField(
                                    name='updated_at',
                                    path='/updated_at',
                                ),
                                SemanticMetadataField(
                                    name='name',
                                    path='/name',
                                ),
                                SemanticMetadataField(
                                    name='status',
                                    path='/status',
                                ),
                                SemanticMetadataField(
                                    name='requisition_id',
                                    path='/requisition_id',
                                ),
                                SemanticMetadataField(
                                    name='confidential',
                                    path='/confidential',
                                ),
                                SemanticMetadataField(
                                    name='opened_at',
                                    path='/opened_at',
                                ),
                                SemanticMetadataField(
                                    name='closed_at',
                                    path='/closed_at',
                                ),
                                SemanticMetadataField(
                                    name='created_at',
                                    path='/created_at',
                                ),
                            ],
                        ),
                    ),
                    CacheFieldConfig(
                        name='office_ids',
                        type=['null', 'array'],
                        description='Ids of the offices this job is assigned to. A job can span multiple offices; empty array or `null` when no offices are set.',
                    ),
                    CacheFieldConfig(
                        name='opened_at',
                        type=['null', 'string'],
                        description='Timestamp the job first transitioned to `open`, in ISO 8601. `null` while the job is still in `draft`.',
                    ),
                    CacheFieldConfig(
                        name='requisition_id',
                        type=['null', 'string'],
                        description='Partner-supplied external identifier for the requisition (e.g. an HRIS or ATS code). Free-form string, not unique across the organization, and `null` when no external id has been set.',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Lifecycle status of the job. `draft` while it is being scaffolded, `open` once it has at least one open opening, and `closed` after every opening is closed. A job moves to `closed` automatically when its last open opening is closed via `PATCH /v3/openings/{id}`.',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='Updated at from the Greenhouse v3 jobs record.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='offers',
                suggested=True,
                x_airbyte_name='offers',
                fields=[
                    CacheFieldConfig(
                        name='application_id',
                        type=['null', 'integer'],
                        description='Id of the application this offer is extended on. Every offer belongs to exactly one application; the offer is voided if the application is rejected or deleted.',
                    ),
                    CacheFieldConfig(
                        name='candidate_id',
                        type=['null', 'integer'],
                        description="Id of the candidate (person) receiving this offer. Resolved through the offer's application.",
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Created at from the Greenhouse v3 offers record.',
                    ),
                    CacheFieldConfig(
                        name='custom_fields',
                        type=['null', 'object'],
                        description="Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Id from the Greenhouse v3 offers record.',
                    ),
                    CacheFieldConfig(
                        name='job_id',
                        type=['null', 'integer'],
                        description="Id of the job this offer's application is on.",
                    ),
                    CacheFieldConfig(
                        name='opening_id',
                        type=['null', 'integer'],
                        description='Id of the specific opening this offer is being extended for. `null` when the offer has not yet been linked to an opening.',
                    ),
                    CacheFieldConfig(
                        name='resolved_at',
                        type=['null', 'string'],
                        description='Timestamp the offer was resolved (`Accepted` or `Rejected`), in ISO 8601. Date updates submitted through `PATCH /v3/offers/{id}` are normalized to noon UTC on the supplied date. `null` while the offer is still `Created` or has been superseded as `Deprecated` without a resolution.',
                    ),
                    CacheFieldConfig(
                        name='sent_on',
                        type=['null', 'string'],
                        description='Date the offer was sent to the candidate, in ISO 8601 (YYYY-MM-DD). `null` until the offer has been sent.',
                    ),
                    CacheFieldConfig(
                        name='starts_on',
                        type=['null', 'string'],
                        description="Candidate's proposed start date, in ISO 8601 (YYYY-MM-DD). `null` when no start date has been set on the offer.",
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Lifecycle status of the offer. `Created` for offers still being drafted or pending approval, `Accepted` once the candidate accepts, `Rejected` if declined or withdrawn, and `Deprecated` for superseded prior versions (a new offer version replaces an earlier one with this status).',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='Updated at from the Greenhouse v3 offers record.',
                    ),
                    CacheFieldConfig(
                        name='version',
                        type=['null', 'integer'],
                        description='Revision number of this offer within its application. Greenhouse creates a new offer row (incrementing `version`) whenever a tracked field on an existing offer changes — typically `starts_on`, `opening_id`, or a custom field configured to trigger a new version. Pair with `current_only=true` to filter the list endpoint down to the latest version per application.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='offices',
                x_airbyte_name='offices',
                fields=[
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Created at from the Greenhouse v3 offices record.',
                    ),
                    CacheFieldConfig(
                        name='external_id',
                        type=['null', 'string'],
                        description='Stable identifier supplied by the customer or HRIS for cross-system reconciliation. `null` when no external id has been set. Available when the `org_structure_external_id` product flag is enabled.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Id from the Greenhouse v3 offices record.',
                    ),
                    CacheFieldConfig(
                        name='location',
                        type=['null', 'string'],
                        description='Free-form physical location string for the office (e.g. `New York, NY, USA`). `null` for offices that have no location set, including most remote offices.',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Display name of the office (e.g. `San Francisco`, `Remote (US)`). Unique among active offices in the same organization.',
                    ),
                    CacheFieldConfig(
                        name='parent_id',
                        type=['null', 'integer'],
                        description='Id of the parent office when offices are organized hierarchically. `null` for top-level offices. References another `/v3/offices` row in the same organization.',
                    ),
                    CacheFieldConfig(
                        name='primary_in_house_contact_user_id',
                        type=['null', 'integer'],
                        description="Id of the Greenhouse user designated as the office's primary internal contact, typically the local recruiting lead. References a `/v3/users` row. `null` when no contact has been assigned.",
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='Updated at from the Greenhouse v3 offices record.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='sources',
                x_airbyte_name='sources',
                fields=[
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Created at from the Greenhouse v3 sources record.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Id from the Greenhouse v3 sources record.',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Display name of the source as recruiters see it in Greenhouse (e.g. `LinkedIn (Prospecting)`, `Indeed`, `Referral`, `Internal Applicant`, or a custom agency name). For organization-specific sources this is the label the org configured; for global Greenhouse sources it is the standard public name.',
                    ),
                    CacheFieldConfig(
                        name='type',
                        type=['null', 'object'],
                        description='The sourcing strategy this source rolls up to — the broader category used for reporting. Sources are grouped under sourcing strategies such as `Agencies`, `Referral`, `Third-party boards`, `Prospecting`, `Social media`, `Company marketing`, `In person event`, `MyGreenhouse`, and `Other`. Use the strategy when aggregating candidate volume by channel; use the source itself when reporting on a specific channel within that category.',
                        properties={
                            'id': CacheFieldProperty(
                                type=['null', 'integer'],
                            ),
                            'name': CacheFieldProperty(
                                type=['null', 'string'],
                            ),
                        },
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='Updated at from the Greenhouse v3 sources record.',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='users',
                x_airbyte_name='users',
                fields=[
                    CacheFieldConfig(
                        name='agency_id',
                        type=['null', 'integer'],
                        description='Id of the staffing agency this user belongs to, when the user is an external agency recruiter rather than an employee of your organization. `null` for in-house users.',
                    ),
                    CacheFieldConfig(
                        name='created_at',
                        type=['null', 'string'],
                        description='Created at from the Greenhouse v3 users record.',
                    ),
                    CacheFieldConfig(
                        name='custom_fields',
                        type=['null', 'object'],
                        description="Org-defined custom fields keyed by the field's `name_key`. Each value carries the field's display `name`, its `type`, and its `value`.",
                    ),
                    CacheFieldConfig(
                        name='deactivated',
                        type=['null', 'boolean'],
                        description='Whether the user has been deactivated. Deactivated users cannot sign in or be assigned to new jobs, but their historical activity (notes, scorecards, emails) is preserved. Toggle via `POST /v3/users/{id}/deactivate` and `POST /v3/users/{id}/activate`.',
                    ),
                    CacheFieldConfig(
                        name='department_ids',
                        type=['null', 'array'],
                        description='Ids of the departments this user is assigned to. Used to scope future job permissions and to filter the user list by department. Empty when the user is not pinned to any department.',
                    ),
                    CacheFieldConfig(
                        name='emails',
                        type=['null', 'array'],
                        description="All email addresses on the user's account, including the primary address and any additional verified addresses.",
                    ),
                    CacheFieldConfig(
                        name='employee_id',
                        type=['null', 'string'],
                        description="Partner-supplied external employee identifier, typically the user's HRIS or payroll id. Free-form string; not unique across organizations and `null` when no employee id has been set.",
                    ),
                    CacheFieldConfig(
                        name='first_name',
                        type=['null', 'string'],
                        description='First name from the Greenhouse v3 users record.',
                    ),
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'integer'],
                        description='Id from the Greenhouse v3 users record.',
                    ),
                    CacheFieldConfig(
                        name='interviewer_tags',
                        type=['null', 'array'],
                        description="Interviewer tags applied to this user — the labeled skill or panel groupings (e.g. `Senior Engineer`, `Bar Raiser`) used to suggest qualified interviewers when building an interview plan. Each entry pairs the tag's `id` with its `name`.",
                    ),
                    CacheFieldConfig(
                        name='job_title',
                        type=['null', 'string'],
                        description="Free-form job title set on the user's Greenhouse profile (e.g. `Senior Recruiter`). Not synchronized with any HRIS title.",
                    ),
                    CacheFieldConfig(
                        name='last_name',
                        type=['null', 'string'],
                        description='Last name from the Greenhouse v3 users record.',
                    ),
                    CacheFieldConfig(
                        name='linked_candidate_ids',
                        type=['null', 'array'],
                        description='Ids of candidate records linked to this user. Populated when an employee is represented by both a user record (for Greenhouse access) and a candidate record (for past or internal applications).',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Concatenation of `first_name` and `last_name` rendered as a single display string. Provided for convenience; partners that need either component should read `first_name`/`last_name` directly.',
                    ),
                    CacheFieldConfig(
                        name='office_ids',
                        type=['null', 'array'],
                        description='Ids of the offices this user is assigned to. Used to scope future job permissions and to filter the user list by office. Empty when the user is not pinned to any office.',
                    ),
                    CacheFieldConfig(
                        name='primary_email',
                        type=['null', 'string'],
                        description="Primary email address on the user's account. Sign-in identifier and the address Greenhouse uses for outbound mail; additional verified addresses are not surfaced here. Service accounts (integration/ISU users) have no email and are excluded from this endpoint by default; when included via `show_service_accounts=true`, their `primary_email` is an empty string.",
                    ),
                    CacheFieldConfig(
                        name='site_admin',
                        type=['null', 'boolean'],
                        description='Whether the user holds the Site Admin role. Site admins have unrestricted access to every non-confidential job and to organization-level settings. Demote a site admin to a Basic user with `POST /v3/users/{id}/revoke_permissions`.',
                    ),
                    CacheFieldConfig(
                        name='updated_at',
                        type=['null', 'string'],
                        description='Updated at from the Greenhouse v3 users record.',
                    ),
                ],
            ),
        ],
        disable_compaction=True,
    ),
    search_field_paths={
        'applications': [
            'agency_note_id',
            'answers',
            'answers[]',
            'candidate_id',
            'coordinator_id',
            'created_at',
            'custom_fields',
            'id',
            'job_id',
            'job_interview_stage_id',
            'job_post_id',
            'last_activity_at',
            'location_address',
            'needs_decision',
            'prospect',
            'prospective_job_ids',
            'prospective_job_ids[]',
            'recruiter_id',
            'referrer_id',
            'rejected_at',
            'rejection_reason_id',
            'source_id',
            'stage_id',
            'stage_name',
            'status',
            'updated_at',
        ],
        'candidates': [
            'addresses',
            'addresses[]',
            'can_email',
            'company',
            'created_at',
            'custom_fields',
            'email_addresses',
            'email_addresses[]',
            'first_name',
            'id',
            'last_activity_at',
            'last_name',
            'linked_user_ids',
            'linked_user_ids[]',
            'phone_numbers',
            'phone_numbers[]',
            'preferred_name',
            'private',
            'social_media_addresses',
            'social_media_addresses[]',
            'tags',
            'tags[]',
            'time_zone',
            'title',
            'updated_at',
            'website_addresses',
            'website_addresses[]',
        ],
        'departments': [
            'created_at',
            'external_id',
            'id',
            'name',
            'parent_id',
            'updated_at',
        ],
        'job_posts': [
            'active',
            'content',
            'created_at',
            'demographic_question_set_id',
            'featured',
            'first_published_at',
            'id',
            'internal',
            'internal_content',
            'job_board_id',
            'job_id',
            'language',
            'live',
            'public_url',
            'questions',
            'questions[]',
            'title',
            'updated_at',
        ],
        'jobs': [
            'closed_at',
            'confidential',
            'copied_from_id',
            'created_at',
            'custom_fields',
            'department_id',
            'id',
            'is_template',
            'name',
            'notes',
            'office_ids',
            'office_ids[]',
            'opened_at',
            'requisition_id',
            'status',
            'updated_at',
        ],
        'offers': [
            'application_id',
            'candidate_id',
            'created_at',
            'custom_fields',
            'id',
            'job_id',
            'opening_id',
            'resolved_at',
            'sent_on',
            'starts_on',
            'status',
            'updated_at',
            'version',
        ],
        'offices': [
            'created_at',
            'external_id',
            'id',
            'location',
            'name',
            'parent_id',
            'primary_in_house_contact_user_id',
            'updated_at',
        ],
        'sources': [
            'created_at',
            'id',
            'name',
            'type',
            'type.id',
            'type.name',
            'updated_at',
        ],
        'users': [
            'agency_id',
            'created_at',
            'custom_fields',
            'deactivated',
            'department_ids',
            'department_ids[]',
            'emails',
            'emails[]',
            'employee_id',
            'first_name',
            'id',
            'interviewer_tags',
            'interviewer_tags[]',
            'job_title',
            'last_name',
            'linked_candidate_ids',
            'linked_candidate_ids[]',
            'name',
            'office_ids',
            'office_ids[]',
            'primary_email',
            'site_admin',
            'updated_at',
        ],
    },
    semantic_search_fields={
        'job_posts': {
            'content': SemanticSearchConfig(
                content_type='html',
                samples=[
                    SemanticSample(
                        name='title',
                        path='/title',
                    ),
                    SemanticSample(
                        name='job_post_content',
                        windowed=True,
                        sampling=SemanticSampling(
                            sample_type='whole',
                            unit_label='job_post',
                        ),
                    ),
                ],
                windowing=SemanticWindowing(
                    context_max_chars=2048,
                ),
                embedding=SemanticEmbedding(
                    model='text-embedding-3-small',
                    template='{title}\n\n{job_post_content}',
                ),
                metadata=[
                    SemanticMetadataField(
                        name='id',
                        path='/id',
                    ),
                    SemanticMetadataField(
                        name='updated_at',
                        path='/updated_at',
                    ),
                    SemanticMetadataField(
                        name='title',
                        path='/title',
                    ),
                    SemanticMetadataField(
                        name='job_id',
                        path='/job_id',
                    ),
                    SemanticMetadataField(
                        name='live',
                        path='/live',
                    ),
                    SemanticMetadataField(
                        name='internal',
                        path='/internal',
                    ),
                    SemanticMetadataField(
                        name='first_published_at',
                        path='/first_published_at',
                    ),
                    SemanticMetadataField(
                        name='created_at',
                        path='/created_at',
                    ),
                ],
            ),
            'internal_content': SemanticSearchConfig(
                content_type='html',
                samples=[
                    SemanticSample(
                        name='title',
                        path='/title',
                    ),
                    SemanticSample(
                        name='internal_job_post_content',
                        windowed=True,
                        sampling=SemanticSampling(
                            sample_type='whole',
                            unit_label='internal_job_post',
                        ),
                    ),
                ],
                windowing=SemanticWindowing(
                    context_max_chars=2048,
                ),
                embedding=SemanticEmbedding(
                    model='text-embedding-3-small',
                    template='{title}\n\n{internal_job_post_content}',
                ),
                metadata=[
                    SemanticMetadataField(
                        name='id',
                        path='/id',
                    ),
                    SemanticMetadataField(
                        name='updated_at',
                        path='/updated_at',
                    ),
                    SemanticMetadataField(
                        name='title',
                        path='/title',
                    ),
                    SemanticMetadataField(
                        name='job_id',
                        path='/job_id',
                    ),
                    SemanticMetadataField(
                        name='live',
                        path='/live',
                    ),
                    SemanticMetadataField(
                        name='internal',
                        path='/internal',
                    ),
                    SemanticMetadataField(
                        name='first_published_at',
                        path='/first_published_at',
                    ),
                    SemanticMetadataField(
                        name='created_at',
                        path='/created_at',
                    ),
                ],
            ),
        },
        'jobs': {
            'notes': SemanticSearchConfig(
                content_type='html',
                samples=[
                    SemanticSample(
                        name='name',
                        path='/name',
                    ),
                    SemanticSample(
                        name='job_notes',
                        windowed=True,
                        sampling=SemanticSampling(
                            sample_type='whole',
                            unit_label='job',
                        ),
                    ),
                ],
                windowing=SemanticWindowing(
                    context_max_chars=2048,
                ),
                embedding=SemanticEmbedding(
                    model='text-embedding-3-small',
                    template='{name}\n\n{job_notes}',
                ),
                metadata=[
                    SemanticMetadataField(
                        name='id',
                        path='/id',
                    ),
                    SemanticMetadataField(
                        name='updated_at',
                        path='/updated_at',
                    ),
                    SemanticMetadataField(
                        name='name',
                        path='/name',
                    ),
                    SemanticMetadataField(
                        name='status',
                        path='/status',
                    ),
                    SemanticMetadataField(
                        name='requisition_id',
                        path='/requisition_id',
                    ),
                    SemanticMetadataField(
                        name='confidential',
                        path='/confidential',
                    ),
                    SemanticMetadataField(
                        name='opened_at',
                        path='/opened_at',
                    ),
                    SemanticMetadataField(
                        name='closed_at',
                        path='/closed_at',
                    ),
                    SemanticMetadataField(
                        name='created_at',
                        path='/created_at',
                    ),
                ],
            ),
        },
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all open jobs',
            'Show me recent interviews',
            'Show me recent job offers',
            'List recent applications',
        ],
        context_store_search=[
            'Show me candidates from {company} who applied last month',
            'What are the top 5 sources for our job applications this quarter?',
            'Analyze the interview schedules for our engineering candidates this week',
            'Compare the number of applications across different offices',
            'Identify candidates who have multiple applications in our system',
            'Summarize the candidate pipeline for our latest job posting',
            'Find the most active departments in recruiting this month',
        ],
        search=[
            'Show me candidates from {company} who applied last month',
            'What are the top 5 sources for our job applications this quarter?',
            'Analyze the interview schedules for our engineering candidates this week',
            'Compare the number of applications across different offices',
            'Identify candidates who have multiple applications in our system',
            'Summarize the candidate pipeline for our latest job posting',
            'Find the most active departments in recruiting this month',
        ],
        unsupported=[
            'Create a new job posting for the marketing team',
            'Schedule an interview for {candidate}',
            "Update the status of {candidate}'s application",
            'Delete a candidate profile',
            'Send an offer letter to {candidate}',
            'Edit the details of a job description',
        ],
    ),
)