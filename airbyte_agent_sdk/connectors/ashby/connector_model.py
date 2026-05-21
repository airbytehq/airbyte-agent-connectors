"""
Connector model for ashby.

This file is auto-generated from the connector definition at build time.
DO NOT EDIT MANUALLY - changes will be overwritten on next generation.
"""

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
)
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

AshbyConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('4e8c9fa0-3634-499b-b948-11581b5c3efa'),
    name='ashby',
    version='0.1.4',
    base_url='https://api.ashbyhq.com',
    auth=AuthConfig(
        type=AuthType.BASIC,
        user_config_spec=AuthConfigSpec(
            title='API Key Authentication',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='Your Ashby API key',
                ),
            },
            auth_mapping={'username': '${api_key}', 'password': ''},
            replication_auth_key_mapping={'api_key': 'api_key'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='candidates',
            stream_name='candidates',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/candidate.list',
                    action=Action.LIST,
                    description='Lists all candidates in the organization',
                    body_fields=['cursor', 'limit'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'cursor': {'type': 'string', 'description': 'Pagination cursor for next page'},
                            'limit': {'type': 'integer', 'description': 'Maximum number of records to return per page'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Candidate object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique candidate identifier'},
                                        'createdAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Last update timestamp',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Full name of the candidate',
                                        },
                                        'emailAddresses': {
                                            'type': ['array', 'null'],
                                            'description': 'List of email addresses',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'isPrimary': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                },
                                            },
                                        },
                                        'phoneNumbers': {
                                            'type': ['array', 'null'],
                                            'description': 'List of phone numbers',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'isPrimary': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                },
                                            },
                                        },
                                        'socialLinks': {
                                            'type': ['array', 'null'],
                                            'description': 'Social media links',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'url': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                        },
                                        'tags': {
                                            'type': ['array', 'null'],
                                            'description': 'Tags associated with the candidate',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'isArchived': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                },
                                            },
                                        },
                                        'applicationIds': {
                                            'type': ['array', 'null'],
                                            'description': 'List of application IDs',
                                            'items': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                        'fileHandles': {
                                            'type': ['array', 'null'],
                                            'description': 'Associated file handles',
                                        },
                                        'customFields': {
                                            'type': ['array', 'null'],
                                            'description': 'Custom field values',
                                        },
                                        'profileUrl': {
                                            'type': ['string', 'null'],
                                            'description': 'URL to candidate profile',
                                        },
                                        'source': {
                                            'oneOf': [
                                                {'type': 'object'},
                                                {'type': 'null'},
                                            ],
                                            'description': 'Candidate source',
                                        },
                                        'creditedToUser': {
                                            'oneOf': [
                                                {'type': 'object'},
                                                {'type': 'null'},
                                            ],
                                            'description': 'User credited for the candidate',
                                        },
                                        'timezone': {
                                            'type': ['string', 'null'],
                                            'description': 'Candidate timezone',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'candidates',
                                    'x-airbyte-stream-name': 'candidates',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Job candidates in the Ashby ATS with application history',
                                        'when_to_use': 'Looking up candidate information or hiring pipeline status',
                                        'trigger_phrases': [
                                            'ashby candidate',
                                            'applicant',
                                            'hiring candidate',
                                            'who applied',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Find candidate details in Ashby', 'List recent candidates'],
                                        'search_strategy': 'Search by name or email',
                                    },
                                },
                            },
                            'moreDataAvailable': {'type': 'boolean'},
                            'nextCursor': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'cursor': '$.nextCursor', 'has_more': '$.moreDataAvailable'},
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/candidate.info',
                    action=Action.GET,
                    description='Get a single candidate by ID',
                    body_fields=['id'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Candidate ID'},
                        },
                        'required': ['id'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'object',
                                'description': 'Candidate object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique candidate identifier'},
                                    'createdAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Creation timestamp',
                                    },
                                    'updatedAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Last update timestamp',
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'Full name of the candidate',
                                    },
                                    'emailAddresses': {
                                        'type': ['array', 'null'],
                                        'description': 'List of email addresses',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'value': {
                                                    'type': ['string', 'null'],
                                                },
                                                'type': {
                                                    'type': ['string', 'null'],
                                                },
                                                'isPrimary': {
                                                    'type': ['boolean', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'phoneNumbers': {
                                        'type': ['array', 'null'],
                                        'description': 'List of phone numbers',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'value': {
                                                    'type': ['string', 'null'],
                                                },
                                                'type': {
                                                    'type': ['string', 'null'],
                                                },
                                                'isPrimary': {
                                                    'type': ['boolean', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'socialLinks': {
                                        'type': ['array', 'null'],
                                        'description': 'Social media links',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                },
                                                'url': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'tags': {
                                        'type': ['array', 'null'],
                                        'description': 'Tags associated with the candidate',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'title': {
                                                    'type': ['string', 'null'],
                                                },
                                                'isArchived': {
                                                    'type': ['boolean', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'applicationIds': {
                                        'type': ['array', 'null'],
                                        'description': 'List of application IDs',
                                        'items': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'fileHandles': {
                                        'type': ['array', 'null'],
                                        'description': 'Associated file handles',
                                    },
                                    'customFields': {
                                        'type': ['array', 'null'],
                                        'description': 'Custom field values',
                                    },
                                    'profileUrl': {
                                        'type': ['string', 'null'],
                                        'description': 'URL to candidate profile',
                                    },
                                    'source': {
                                        'oneOf': [
                                            {'type': 'object'},
                                            {'type': 'null'},
                                        ],
                                        'description': 'Candidate source',
                                    },
                                    'creditedToUser': {
                                        'oneOf': [
                                            {'type': 'object'},
                                            {'type': 'null'},
                                        ],
                                        'description': 'User credited for the candidate',
                                    },
                                    'timezone': {
                                        'type': ['string', 'null'],
                                        'description': 'Candidate timezone',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'candidates',
                                'x-airbyte-stream-name': 'candidates',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Job candidates in the Ashby ATS with application history',
                                    'when_to_use': 'Looking up candidate information or hiring pipeline status',
                                    'trigger_phrases': [
                                        'ashby candidate',
                                        'applicant',
                                        'hiring candidate',
                                        'who applied',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['Find candidate details in Ashby', 'List recent candidates'],
                                    'search_strategy': 'Search by name or email',
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Candidate object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique candidate identifier'},
                    'createdAt': {
                        'type': ['string', 'null'],
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': ['string', 'null'],
                        'description': 'Last update timestamp',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Full name of the candidate',
                    },
                    'emailAddresses': {
                        'type': ['array', 'null'],
                        'description': 'List of email addresses',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'value': {
                                    'type': ['string', 'null'],
                                },
                                'type': {
                                    'type': ['string', 'null'],
                                },
                                'isPrimary': {
                                    'type': ['boolean', 'null'],
                                },
                            },
                        },
                    },
                    'phoneNumbers': {
                        'type': ['array', 'null'],
                        'description': 'List of phone numbers',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'value': {
                                    'type': ['string', 'null'],
                                },
                                'type': {
                                    'type': ['string', 'null'],
                                },
                                'isPrimary': {
                                    'type': ['boolean', 'null'],
                                },
                            },
                        },
                    },
                    'socialLinks': {
                        'type': ['array', 'null'],
                        'description': 'Social media links',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'type': {
                                    'type': ['string', 'null'],
                                },
                                'url': {
                                    'type': ['string', 'null'],
                                },
                            },
                        },
                    },
                    'tags': {
                        'type': ['array', 'null'],
                        'description': 'Tags associated with the candidate',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['string', 'null'],
                                },
                                'title': {
                                    'type': ['string', 'null'],
                                },
                                'isArchived': {
                                    'type': ['boolean', 'null'],
                                },
                            },
                        },
                    },
                    'applicationIds': {
                        'type': ['array', 'null'],
                        'description': 'List of application IDs',
                        'items': {
                            'type': ['string', 'null'],
                        },
                    },
                    'fileHandles': {
                        'type': ['array', 'null'],
                        'description': 'Associated file handles',
                    },
                    'customFields': {
                        'type': ['array', 'null'],
                        'description': 'Custom field values',
                    },
                    'profileUrl': {
                        'type': ['string', 'null'],
                        'description': 'URL to candidate profile',
                    },
                    'source': {
                        'oneOf': [
                            {'type': 'object'},
                            {'type': 'null'},
                        ],
                        'description': 'Candidate source',
                    },
                    'creditedToUser': {
                        'oneOf': [
                            {'type': 'object'},
                            {'type': 'null'},
                        ],
                        'description': 'User credited for the candidate',
                    },
                    'timezone': {
                        'type': ['string', 'null'],
                        'description': 'Candidate timezone',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'candidates',
                'x-airbyte-stream-name': 'candidates',
                'x-airbyte-ai-hints': {
                    'summary': 'Job candidates in the Ashby ATS with application history',
                    'when_to_use': 'Looking up candidate information or hiring pipeline status',
                    'trigger_phrases': [
                        'ashby candidate',
                        'applicant',
                        'hiring candidate',
                        'who applied',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Find candidate details in Ashby', 'List recent candidates'],
                    'search_strategy': 'Search by name or email',
                },
            },
            ai_hints={
                'summary': 'Job candidates in the Ashby ATS with application history',
                'when_to_use': 'Looking up candidate information or hiring pipeline status',
                'trigger_phrases': [
                    'ashby candidate',
                    'applicant',
                    'hiring candidate',
                    'who applied',
                ],
                'freshness': 'live',
                'example_questions': ['Find candidate details in Ashby', 'List recent candidates'],
                'search_strategy': 'Search by name or email',
            },
        ),
        EntityDefinition(
            name='applications',
            stream_name='applications',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/application.list',
                    action=Action.LIST,
                    description='Gets all applications in the organization',
                    body_fields=['cursor', 'limit'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'cursor': {'type': 'string', 'description': 'Pagination cursor for next page'},
                            'limit': {'type': 'integer', 'description': 'Maximum number of records to return per page'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Application object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique application identifier'},
                                        'createdAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Last update timestamp',
                                        },
                                        'archivedAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Archived timestamp',
                                        },
                                        'candidate': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'name': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Associated candidate object',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'Application status',
                                        },
                                        'customFields': {
                                            'type': ['array', 'null'],
                                            'description': 'Custom field values',
                                        },
                                        'currentInterviewStage': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'title': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'type': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'interviewPlanId': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'orderInInterviewPlan': {
                                                            'type': ['integer', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Current interview stage',
                                        },
                                        'source': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'title': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'isArchived': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'sourceType': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'id': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'title': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'isArchived': {
                                                                            'type': ['boolean', 'null'],
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Application source',
                                        },
                                        'creditedToUser': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'firstName': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'lastName': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'email': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'globalRole': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'isEnabled': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'updatedAt': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'User credited for this application',
                                        },
                                        'archiveReason': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'text': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'reasonType': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'isArchived': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'customFields': {
                                                            'type': ['array', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Reason for archiving',
                                        },
                                        'job': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'title': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'locationId': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'departmentId': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'brandId': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Associated job object',
                                        },
                                        'hiringTeam': {
                                            'type': ['array', 'null'],
                                            'description': 'Hiring team members',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'userId': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'firstName': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'lastName': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'role': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                        },
                                        'appliedViaJobPostingId': {
                                            'type': ['string', 'null'],
                                            'description': 'Job posting ID applied via',
                                        },
                                        'submitterClientIp': {
                                            'type': ['string', 'null'],
                                            'description': 'Submitter client IP',
                                        },
                                        'submitterUserAgent': {
                                            'type': ['string', 'null'],
                                            'description': 'Submitter user agent',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'applications',
                                    'x-airbyte-stream-name': 'applications',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Job applications linking candidates to specific positions',
                                        'when_to_use': 'Questions about application status, stage, or hiring pipeline',
                                        'trigger_phrases': [
                                            'application status',
                                            'applied for',
                                            'hiring stage',
                                            'application',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What is the status of an application?', 'Show applications for a job'],
                                        'search_strategy': 'Filter by candidate, job, or status',
                                    },
                                },
                            },
                            'moreDataAvailable': {'type': 'boolean'},
                            'nextCursor': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'cursor': '$.nextCursor', 'has_more': '$.moreDataAvailable'},
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/application.info',
                    action=Action.GET,
                    description='Get a single application by ID',
                    body_fields=['applicationId'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'applicationId': {'type': 'string', 'description': 'Application ID'},
                        },
                        'required': ['applicationId'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'object',
                                'description': 'Application object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique application identifier'},
                                    'createdAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Creation timestamp',
                                    },
                                    'updatedAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Last update timestamp',
                                    },
                                    'archivedAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Archived timestamp',
                                    },
                                    'candidate': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Associated candidate object',
                                    },
                                    'status': {
                                        'type': ['string', 'null'],
                                        'description': 'Application status',
                                    },
                                    'customFields': {
                                        'type': ['array', 'null'],
                                        'description': 'Custom field values',
                                    },
                                    'currentInterviewStage': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'interviewPlanId': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'orderInInterviewPlan': {
                                                        'type': ['integer', 'null'],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Current interview stage',
                                    },
                                    'source': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'isArchived': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'sourceType': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'id': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'title': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'isArchived': {
                                                                        'type': ['boolean', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Application source',
                                    },
                                    'creditedToUser': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'firstName': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'lastName': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'globalRole': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'isEnabled': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'updatedAt': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'User credited for this application',
                                    },
                                    'archiveReason': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'text': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'reasonType': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'isArchived': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'customFields': {
                                                        'type': ['array', 'null'],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Reason for archiving',
                                    },
                                    'job': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'locationId': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'departmentId': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'brandId': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Associated job object',
                                    },
                                    'hiringTeam': {
                                        'type': ['array', 'null'],
                                        'description': 'Hiring team members',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'userId': {
                                                    'type': ['string', 'null'],
                                                },
                                                'firstName': {
                                                    'type': ['string', 'null'],
                                                },
                                                'lastName': {
                                                    'type': ['string', 'null'],
                                                },
                                                'email': {
                                                    'type': ['string', 'null'],
                                                },
                                                'role': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'appliedViaJobPostingId': {
                                        'type': ['string', 'null'],
                                        'description': 'Job posting ID applied via',
                                    },
                                    'submitterClientIp': {
                                        'type': ['string', 'null'],
                                        'description': 'Submitter client IP',
                                    },
                                    'submitterUserAgent': {
                                        'type': ['string', 'null'],
                                        'description': 'Submitter user agent',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'applications',
                                'x-airbyte-stream-name': 'applications',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Job applications linking candidates to specific positions',
                                    'when_to_use': 'Questions about application status, stage, or hiring pipeline',
                                    'trigger_phrases': [
                                        'application status',
                                        'applied for',
                                        'hiring stage',
                                        'application',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What is the status of an application?', 'Show applications for a job'],
                                    'search_strategy': 'Filter by candidate, job, or status',
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Application object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique application identifier'},
                    'createdAt': {
                        'type': ['string', 'null'],
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': ['string', 'null'],
                        'description': 'Last update timestamp',
                    },
                    'archivedAt': {
                        'type': ['string', 'null'],
                        'description': 'Archived timestamp',
                    },
                    'candidate': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'name': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Associated candidate object',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'Application status',
                    },
                    'customFields': {
                        'type': ['array', 'null'],
                        'description': 'Custom field values',
                    },
                    'currentInterviewStage': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                    },
                                    'type': {
                                        'type': ['string', 'null'],
                                    },
                                    'interviewPlanId': {
                                        'type': ['string', 'null'],
                                    },
                                    'orderInInterviewPlan': {
                                        'type': ['integer', 'null'],
                                    },
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Current interview stage',
                    },
                    'source': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                    },
                                    'isArchived': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'sourceType': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'isArchived': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Application source',
                    },
                    'creditedToUser': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'firstName': {
                                        'type': ['string', 'null'],
                                    },
                                    'lastName': {
                                        'type': ['string', 'null'],
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                    },
                                    'globalRole': {
                                        'type': ['string', 'null'],
                                    },
                                    'isEnabled': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'updatedAt': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'User credited for this application',
                    },
                    'archiveReason': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'text': {
                                        'type': ['string', 'null'],
                                    },
                                    'reasonType': {
                                        'type': ['string', 'null'],
                                    },
                                    'isArchived': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'customFields': {
                                        'type': ['array', 'null'],
                                    },
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Reason for archiving',
                    },
                    'job': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                    },
                                    'locationId': {
                                        'type': ['string', 'null'],
                                    },
                                    'departmentId': {
                                        'type': ['string', 'null'],
                                    },
                                    'brandId': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Associated job object',
                    },
                    'hiringTeam': {
                        'type': ['array', 'null'],
                        'description': 'Hiring team members',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'userId': {
                                    'type': ['string', 'null'],
                                },
                                'firstName': {
                                    'type': ['string', 'null'],
                                },
                                'lastName': {
                                    'type': ['string', 'null'],
                                },
                                'email': {
                                    'type': ['string', 'null'],
                                },
                                'role': {
                                    'type': ['string', 'null'],
                                },
                            },
                        },
                    },
                    'appliedViaJobPostingId': {
                        'type': ['string', 'null'],
                        'description': 'Job posting ID applied via',
                    },
                    'submitterClientIp': {
                        'type': ['string', 'null'],
                        'description': 'Submitter client IP',
                    },
                    'submitterUserAgent': {
                        'type': ['string', 'null'],
                        'description': 'Submitter user agent',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'applications',
                'x-airbyte-stream-name': 'applications',
                'x-airbyte-ai-hints': {
                    'summary': 'Job applications linking candidates to specific positions',
                    'when_to_use': 'Questions about application status, stage, or hiring pipeline',
                    'trigger_phrases': [
                        'application status',
                        'applied for',
                        'hiring stage',
                        'application',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What is the status of an application?', 'Show applications for a job'],
                    'search_strategy': 'Filter by candidate, job, or status',
                },
            },
            ai_hints={
                'summary': 'Job applications linking candidates to specific positions',
                'when_to_use': 'Questions about application status, stage, or hiring pipeline',
                'trigger_phrases': [
                    'application status',
                    'applied for',
                    'hiring stage',
                    'application',
                ],
                'freshness': 'live',
                'example_questions': ['What is the status of an application?', 'Show applications for a job'],
                'search_strategy': 'Filter by candidate, job, or status',
            },
        ),
        EntityDefinition(
            name='jobs',
            stream_name='jobs',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/job.list',
                    action=Action.LIST,
                    description='List all open, closed, and archived jobs',
                    body_fields=['cursor', 'limit'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'cursor': {'type': 'string', 'description': 'Pagination cursor for next page'},
                            'limit': {'type': 'integer', 'description': 'Maximum number of records to return per page'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Job object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique job identifier'},
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Job title',
                                        },
                                        'confidential': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the job is confidential',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'Job status',
                                        },
                                        'employmentType': {
                                            'type': ['string', 'null'],
                                            'description': 'Employment type',
                                        },
                                        'locationId': {
                                            'type': ['string', 'null'],
                                            'description': 'Location identifier',
                                        },
                                        'departmentId': {
                                            'type': ['string', 'null'],
                                            'description': 'Department identifier',
                                        },
                                        'defaultInterviewPlanId': {
                                            'type': ['string', 'null'],
                                            'description': 'Default interview plan identifier',
                                        },
                                        'interviewPlanIds': {
                                            'type': ['array', 'null'],
                                            'description': 'Interview plan identifiers',
                                            'items': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                        'jobPostingIds': {
                                            'type': ['array', 'null'],
                                            'description': 'Job posting identifiers',
                                            'items': {
                                                'type': ['string', 'null'],
                                            },
                                        },
                                        'customFields': {
                                            'type': ['array', 'null'],
                                            'description': 'Custom field values',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'isPrivate': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'title': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'value': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'valueLabel': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                        },
                                        'hiringTeam': {
                                            'type': ['array', 'null'],
                                            'description': 'Hiring team members',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'userId': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'firstName': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'lastName': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'role': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                        },
                                        'customRequisitionId': {
                                            'type': ['string', 'null'],
                                            'description': 'Custom requisition identifier',
                                        },
                                        'brandId': {
                                            'type': ['string', 'null'],
                                            'description': 'Brand identifier',
                                        },
                                        'author': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'firstName': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'lastName': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'email': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'globalRole': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'isEnabled': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                        'updatedAt': {
                                                            'type': ['string', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Job author',
                                        },
                                        'createdAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Last update timestamp',
                                        },
                                        'openedAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Opened timestamp',
                                        },
                                        'closedAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Closed timestamp',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'jobs',
                                    'x-airbyte-stream-name': 'jobs',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Open and closed job positions in Ashby',
                                        'when_to_use': 'Questions about job openings, roles, or positions',
                                        'trigger_phrases': [
                                            'ashby job',
                                            'open position',
                                            'job opening',
                                            'role',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What jobs are open in Ashby?', 'Show engineering positions'],
                                        'search_strategy': 'Search by title or department',
                                    },
                                },
                            },
                            'moreDataAvailable': {'type': 'boolean'},
                            'nextCursor': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'cursor': '$.nextCursor', 'has_more': '$.moreDataAvailable'},
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/job.info',
                    action=Action.GET,
                    description='Get a single job by ID',
                    body_fields=['id'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string', 'description': 'Job ID'},
                        },
                        'required': ['id'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'object',
                                'description': 'Job object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique job identifier'},
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'Job title',
                                    },
                                    'confidential': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the job is confidential',
                                    },
                                    'status': {
                                        'type': ['string', 'null'],
                                        'description': 'Job status',
                                    },
                                    'employmentType': {
                                        'type': ['string', 'null'],
                                        'description': 'Employment type',
                                    },
                                    'locationId': {
                                        'type': ['string', 'null'],
                                        'description': 'Location identifier',
                                    },
                                    'departmentId': {
                                        'type': ['string', 'null'],
                                        'description': 'Department identifier',
                                    },
                                    'defaultInterviewPlanId': {
                                        'type': ['string', 'null'],
                                        'description': 'Default interview plan identifier',
                                    },
                                    'interviewPlanIds': {
                                        'type': ['array', 'null'],
                                        'description': 'Interview plan identifiers',
                                        'items': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'jobPostingIds': {
                                        'type': ['array', 'null'],
                                        'description': 'Job posting identifiers',
                                        'items': {
                                            'type': ['string', 'null'],
                                        },
                                    },
                                    'customFields': {
                                        'type': ['array', 'null'],
                                        'description': 'Custom field values',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'id': {
                                                    'type': ['string', 'null'],
                                                },
                                                'isPrivate': {
                                                    'type': ['boolean', 'null'],
                                                },
                                                'title': {
                                                    'type': ['string', 'null'],
                                                },
                                                'value': {
                                                    'type': ['string', 'null'],
                                                },
                                                'valueLabel': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'hiringTeam': {
                                        'type': ['array', 'null'],
                                        'description': 'Hiring team members',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'userId': {
                                                    'type': ['string', 'null'],
                                                },
                                                'firstName': {
                                                    'type': ['string', 'null'],
                                                },
                                                'lastName': {
                                                    'type': ['string', 'null'],
                                                },
                                                'email': {
                                                    'type': ['string', 'null'],
                                                },
                                                'role': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                    'customRequisitionId': {
                                        'type': ['string', 'null'],
                                        'description': 'Custom requisition identifier',
                                    },
                                    'brandId': {
                                        'type': ['string', 'null'],
                                        'description': 'Brand identifier',
                                    },
                                    'author': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'firstName': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'lastName': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'email': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'globalRole': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'isEnabled': {
                                                        'type': ['boolean', 'null'],
                                                    },
                                                    'updatedAt': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Job author',
                                    },
                                    'createdAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Creation timestamp',
                                    },
                                    'updatedAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Last update timestamp',
                                    },
                                    'openedAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Opened timestamp',
                                    },
                                    'closedAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Closed timestamp',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'jobs',
                                'x-airbyte-stream-name': 'jobs',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Open and closed job positions in Ashby',
                                    'when_to_use': 'Questions about job openings, roles, or positions',
                                    'trigger_phrases': [
                                        'ashby job',
                                        'open position',
                                        'job opening',
                                        'role',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What jobs are open in Ashby?', 'Show engineering positions'],
                                    'search_strategy': 'Search by title or department',
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Job object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique job identifier'},
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Job title',
                    },
                    'confidential': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the job is confidential',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'Job status',
                    },
                    'employmentType': {
                        'type': ['string', 'null'],
                        'description': 'Employment type',
                    },
                    'locationId': {
                        'type': ['string', 'null'],
                        'description': 'Location identifier',
                    },
                    'departmentId': {
                        'type': ['string', 'null'],
                        'description': 'Department identifier',
                    },
                    'defaultInterviewPlanId': {
                        'type': ['string', 'null'],
                        'description': 'Default interview plan identifier',
                    },
                    'interviewPlanIds': {
                        'type': ['array', 'null'],
                        'description': 'Interview plan identifiers',
                        'items': {
                            'type': ['string', 'null'],
                        },
                    },
                    'jobPostingIds': {
                        'type': ['array', 'null'],
                        'description': 'Job posting identifiers',
                        'items': {
                            'type': ['string', 'null'],
                        },
                    },
                    'customFields': {
                        'type': ['array', 'null'],
                        'description': 'Custom field values',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['string', 'null'],
                                },
                                'isPrivate': {
                                    'type': ['boolean', 'null'],
                                },
                                'title': {
                                    'type': ['string', 'null'],
                                },
                                'value': {
                                    'type': ['string', 'null'],
                                },
                                'valueLabel': {
                                    'type': ['string', 'null'],
                                },
                            },
                        },
                    },
                    'hiringTeam': {
                        'type': ['array', 'null'],
                        'description': 'Hiring team members',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'userId': {
                                    'type': ['string', 'null'],
                                },
                                'firstName': {
                                    'type': ['string', 'null'],
                                },
                                'lastName': {
                                    'type': ['string', 'null'],
                                },
                                'email': {
                                    'type': ['string', 'null'],
                                },
                                'role': {
                                    'type': ['string', 'null'],
                                },
                            },
                        },
                    },
                    'customRequisitionId': {
                        'type': ['string', 'null'],
                        'description': 'Custom requisition identifier',
                    },
                    'brandId': {
                        'type': ['string', 'null'],
                        'description': 'Brand identifier',
                    },
                    'author': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'firstName': {
                                        'type': ['string', 'null'],
                                    },
                                    'lastName': {
                                        'type': ['string', 'null'],
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                    },
                                    'globalRole': {
                                        'type': ['string', 'null'],
                                    },
                                    'isEnabled': {
                                        'type': ['boolean', 'null'],
                                    },
                                    'updatedAt': {
                                        'type': ['string', 'null'],
                                    },
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Job author',
                    },
                    'createdAt': {
                        'type': ['string', 'null'],
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': ['string', 'null'],
                        'description': 'Last update timestamp',
                    },
                    'openedAt': {
                        'type': ['string', 'null'],
                        'description': 'Opened timestamp',
                    },
                    'closedAt': {
                        'type': ['string', 'null'],
                        'description': 'Closed timestamp',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'jobs',
                'x-airbyte-stream-name': 'jobs',
                'x-airbyte-ai-hints': {
                    'summary': 'Open and closed job positions in Ashby',
                    'when_to_use': 'Questions about job openings, roles, or positions',
                    'trigger_phrases': [
                        'ashby job',
                        'open position',
                        'job opening',
                        'role',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What jobs are open in Ashby?', 'Show engineering positions'],
                    'search_strategy': 'Search by title or department',
                },
            },
            ai_hints={
                'summary': 'Open and closed job positions in Ashby',
                'when_to_use': 'Questions about job openings, roles, or positions',
                'trigger_phrases': [
                    'ashby job',
                    'open position',
                    'job opening',
                    'role',
                ],
                'freshness': 'live',
                'example_questions': ['What jobs are open in Ashby?', 'Show engineering positions'],
                'search_strategy': 'Search by title or department',
            },
        ),
        EntityDefinition(
            name='departments',
            stream_name='departments',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/department.list',
                    action=Action.LIST,
                    description='List all departments',
                    body_fields=['cursor', 'limit'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'cursor': {'type': 'string', 'description': 'Pagination cursor for next page'},
                            'limit': {'type': 'integer', 'description': 'Maximum number of records to return per page'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Department object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique department identifier'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Department name',
                                        },
                                        'externalName': {
                                            'type': ['string', 'null'],
                                            'description': 'External department name',
                                        },
                                        'isArchived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the department is archived',
                                        },
                                        'parentId': {
                                            'type': ['string', 'null'],
                                            'description': 'Parent department identifier',
                                        },
                                        'createdAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Creation timestamp',
                                        },
                                        'updatedAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Last update timestamp',
                                        },
                                        'extraData': {
                                            'oneOf': [
                                                {'type': 'object'},
                                                {'type': 'null'},
                                            ],
                                            'description': 'Extra data',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'departments',
                                    'x-airbyte-stream-name': 'departments',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Departments or divisions in the organization',
                                        'when_to_use': 'Questions about organizational structure or department hierarchy',
                                        'trigger_phrases': ['department', 'division', 'org structure'],
                                        'freshness': 'static',
                                        'example_questions': ['What departments are in Ashby?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                            'moreDataAvailable': {'type': 'boolean'},
                            'nextCursor': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'cursor': '$.nextCursor', 'has_more': '$.moreDataAvailable'},
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/department.info',
                    action=Action.GET,
                    description='Get a single department by ID',
                    body_fields=['departmentId'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'departmentId': {'type': 'string', 'description': 'Department ID'},
                        },
                        'required': ['departmentId'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'object',
                                'description': 'Department object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique department identifier'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'Department name',
                                    },
                                    'externalName': {
                                        'type': ['string', 'null'],
                                        'description': 'External department name',
                                    },
                                    'isArchived': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the department is archived',
                                    },
                                    'parentId': {
                                        'type': ['string', 'null'],
                                        'description': 'Parent department identifier',
                                    },
                                    'createdAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Creation timestamp',
                                    },
                                    'updatedAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Last update timestamp',
                                    },
                                    'extraData': {
                                        'oneOf': [
                                            {'type': 'object'},
                                            {'type': 'null'},
                                        ],
                                        'description': 'Extra data',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'departments',
                                'x-airbyte-stream-name': 'departments',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Departments or divisions in the organization',
                                    'when_to_use': 'Questions about organizational structure or department hierarchy',
                                    'trigger_phrases': ['department', 'division', 'org structure'],
                                    'freshness': 'static',
                                    'example_questions': ['What departments are in Ashby?'],
                                    'search_strategy': 'Search by name',
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Department object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique department identifier'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Department name',
                    },
                    'externalName': {
                        'type': ['string', 'null'],
                        'description': 'External department name',
                    },
                    'isArchived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the department is archived',
                    },
                    'parentId': {
                        'type': ['string', 'null'],
                        'description': 'Parent department identifier',
                    },
                    'createdAt': {
                        'type': ['string', 'null'],
                        'description': 'Creation timestamp',
                    },
                    'updatedAt': {
                        'type': ['string', 'null'],
                        'description': 'Last update timestamp',
                    },
                    'extraData': {
                        'oneOf': [
                            {'type': 'object'},
                            {'type': 'null'},
                        ],
                        'description': 'Extra data',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'departments',
                'x-airbyte-stream-name': 'departments',
                'x-airbyte-ai-hints': {
                    'summary': 'Departments or divisions in the organization',
                    'when_to_use': 'Questions about organizational structure or department hierarchy',
                    'trigger_phrases': ['department', 'division', 'org structure'],
                    'freshness': 'static',
                    'example_questions': ['What departments are in Ashby?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Departments or divisions in the organization',
                'when_to_use': 'Questions about organizational structure or department hierarchy',
                'trigger_phrases': ['department', 'division', 'org structure'],
                'freshness': 'static',
                'example_questions': ['What departments are in Ashby?'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='locations',
            stream_name='locations',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/location.list',
                    action=Action.LIST,
                    description='List all locations',
                    body_fields=['cursor', 'limit'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'cursor': {'type': 'string', 'description': 'Pagination cursor for next page'},
                            'limit': {'type': 'integer', 'description': 'Maximum number of records to return per page'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Location object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique location identifier'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Location name',
                                        },
                                        'externalName': {
                                            'type': ['string', 'null'],
                                            'description': 'External location name',
                                        },
                                        'isArchived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the location is archived',
                                        },
                                        'address': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'postalAddress': {
                                                            'oneOf': [
                                                                {
                                                                    'type': 'object',
                                                                    'properties': {
                                                                        'addressRegion': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'addressCountry': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                        'addressLocality': {
                                                                            'type': ['string', 'null'],
                                                                        },
                                                                    },
                                                                },
                                                                {'type': 'null'},
                                                            ],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Location address',
                                        },
                                        'isRemote': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the location is remote',
                                        },
                                        'workplaceType': {
                                            'type': ['string', 'null'],
                                            'description': 'Workplace type',
                                        },
                                        'parentLocationId': {
                                            'type': ['string', 'null'],
                                            'description': 'Parent location identifier',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'Location type',
                                        },
                                        'extraData': {
                                            'oneOf': [
                                                {'type': 'object'},
                                                {'type': 'null'},
                                            ],
                                            'description': 'Extra data',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'locations',
                                    'x-airbyte-stream-name': 'locations',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Office locations configured in Ashby',
                                        'when_to_use': 'Questions about office locations or where jobs are based',
                                        'trigger_phrases': ['office location', 'where is', 'job location'],
                                        'freshness': 'static',
                                        'example_questions': ['What office locations are configured?'],
                                        'search_strategy': 'Search by name or city',
                                    },
                                },
                            },
                            'moreDataAvailable': {'type': 'boolean'},
                            'nextCursor': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'cursor': '$.nextCursor', 'has_more': '$.moreDataAvailable'},
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/location.info',
                    action=Action.GET,
                    description='Get a single location by ID',
                    body_fields=['locationId'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'locationId': {'type': 'string', 'description': 'Location ID'},
                        },
                        'required': ['locationId'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'object',
                                'description': 'Location object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique location identifier'},
                                    'name': {
                                        'type': ['string', 'null'],
                                        'description': 'Location name',
                                    },
                                    'externalName': {
                                        'type': ['string', 'null'],
                                        'description': 'External location name',
                                    },
                                    'isArchived': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the location is archived',
                                    },
                                    'address': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'postalAddress': {
                                                        'oneOf': [
                                                            {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'addressRegion': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'addressCountry': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                    'addressLocality': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                            {'type': 'null'},
                                                        ],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Location address',
                                    },
                                    'isRemote': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the location is remote',
                                    },
                                    'workplaceType': {
                                        'type': ['string', 'null'],
                                        'description': 'Workplace type',
                                    },
                                    'parentLocationId': {
                                        'type': ['string', 'null'],
                                        'description': 'Parent location identifier',
                                    },
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'Location type',
                                    },
                                    'extraData': {
                                        'oneOf': [
                                            {'type': 'object'},
                                            {'type': 'null'},
                                        ],
                                        'description': 'Extra data',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'locations',
                                'x-airbyte-stream-name': 'locations',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Office locations configured in Ashby',
                                    'when_to_use': 'Questions about office locations or where jobs are based',
                                    'trigger_phrases': ['office location', 'where is', 'job location'],
                                    'freshness': 'static',
                                    'example_questions': ['What office locations are configured?'],
                                    'search_strategy': 'Search by name or city',
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Location object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique location identifier'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'Location name',
                    },
                    'externalName': {
                        'type': ['string', 'null'],
                        'description': 'External location name',
                    },
                    'isArchived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the location is archived',
                    },
                    'address': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'postalAddress': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'addressRegion': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'addressCountry': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'addressLocality': {
                                                        'type': ['string', 'null'],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                    },
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Location address',
                    },
                    'isRemote': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the location is remote',
                    },
                    'workplaceType': {
                        'type': ['string', 'null'],
                        'description': 'Workplace type',
                    },
                    'parentLocationId': {
                        'type': ['string', 'null'],
                        'description': 'Parent location identifier',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'Location type',
                    },
                    'extraData': {
                        'oneOf': [
                            {'type': 'object'},
                            {'type': 'null'},
                        ],
                        'description': 'Extra data',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'locations',
                'x-airbyte-stream-name': 'locations',
                'x-airbyte-ai-hints': {
                    'summary': 'Office locations configured in Ashby',
                    'when_to_use': 'Questions about office locations or where jobs are based',
                    'trigger_phrases': ['office location', 'where is', 'job location'],
                    'freshness': 'static',
                    'example_questions': ['What office locations are configured?'],
                    'search_strategy': 'Search by name or city',
                },
            },
            ai_hints={
                'summary': 'Office locations configured in Ashby',
                'when_to_use': 'Questions about office locations or where jobs are based',
                'trigger_phrases': ['office location', 'where is', 'job location'],
                'freshness': 'static',
                'example_questions': ['What office locations are configured?'],
                'search_strategy': 'Search by name or city',
            },
        ),
        EntityDefinition(
            name='users',
            stream_name='users',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/user.list',
                    action=Action.LIST,
                    description='List all users in the organization',
                    body_fields=['cursor', 'limit'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'cursor': {'type': 'string', 'description': 'Pagination cursor for next page'},
                            'limit': {'type': 'integer', 'description': 'Maximum number of records to return per page'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'User object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique user identifier'},
                                        'firstName': {
                                            'type': ['string', 'null'],
                                            'description': 'First name',
                                        },
                                        'lastName': {
                                            'type': ['string', 'null'],
                                            'description': 'Last name',
                                        },
                                        'email': {
                                            'type': ['string', 'null'],
                                            'description': 'Email address',
                                        },
                                        'globalRole': {
                                            'type': ['string', 'null'],
                                            'description': 'Global role',
                                        },
                                        'isEnabled': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the user is enabled',
                                        },
                                        'updatedAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Last update timestamp',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'users',
                                    'x-airbyte-stream-name': 'users',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Ashby users (recruiters, hiring managers, interviewers)',
                                        'when_to_use': 'Looking up recruiter or hiring manager details',
                                        'trigger_phrases': ['ashby user', 'recruiter', 'hiring manager'],
                                        'freshness': 'live',
                                        'example_questions': ['Who are the recruiters in Ashby?'],
                                        'search_strategy': 'Search by name or email',
                                    },
                                },
                            },
                            'moreDataAvailable': {'type': 'boolean'},
                            'nextCursor': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'cursor': '$.nextCursor', 'has_more': '$.moreDataAvailable'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/user.info',
                    action=Action.GET,
                    description='Get a single user by ID',
                    body_fields=['userId'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'userId': {'type': 'string', 'description': 'User ID'},
                        },
                        'required': ['userId'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'object',
                                'description': 'User object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique user identifier'},
                                    'firstName': {
                                        'type': ['string', 'null'],
                                        'description': 'First name',
                                    },
                                    'lastName': {
                                        'type': ['string', 'null'],
                                        'description': 'Last name',
                                    },
                                    'email': {
                                        'type': ['string', 'null'],
                                        'description': 'Email address',
                                    },
                                    'globalRole': {
                                        'type': ['string', 'null'],
                                        'description': 'Global role',
                                    },
                                    'isEnabled': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the user is enabled',
                                    },
                                    'updatedAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Last update timestamp',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'users',
                                'x-airbyte-stream-name': 'users',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Ashby users (recruiters, hiring managers, interviewers)',
                                    'when_to_use': 'Looking up recruiter or hiring manager details',
                                    'trigger_phrases': ['ashby user', 'recruiter', 'hiring manager'],
                                    'freshness': 'live',
                                    'example_questions': ['Who are the recruiters in Ashby?'],
                                    'search_strategy': 'Search by name or email',
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'User object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique user identifier'},
                    'firstName': {
                        'type': ['string', 'null'],
                        'description': 'First name',
                    },
                    'lastName': {
                        'type': ['string', 'null'],
                        'description': 'Last name',
                    },
                    'email': {
                        'type': ['string', 'null'],
                        'description': 'Email address',
                    },
                    'globalRole': {
                        'type': ['string', 'null'],
                        'description': 'Global role',
                    },
                    'isEnabled': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the user is enabled',
                    },
                    'updatedAt': {
                        'type': ['string', 'null'],
                        'description': 'Last update timestamp',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'users',
                'x-airbyte-stream-name': 'users',
                'x-airbyte-ai-hints': {
                    'summary': 'Ashby users (recruiters, hiring managers, interviewers)',
                    'when_to_use': 'Looking up recruiter or hiring manager details',
                    'trigger_phrases': ['ashby user', 'recruiter', 'hiring manager'],
                    'freshness': 'live',
                    'example_questions': ['Who are the recruiters in Ashby?'],
                    'search_strategy': 'Search by name or email',
                },
            },
            ai_hints={
                'summary': 'Ashby users (recruiters, hiring managers, interviewers)',
                'when_to_use': 'Looking up recruiter or hiring manager details',
                'trigger_phrases': ['ashby user', 'recruiter', 'hiring manager'],
                'freshness': 'live',
                'example_questions': ['Who are the recruiters in Ashby?'],
                'search_strategy': 'Search by name or email',
            },
        ),
        EntityDefinition(
            name='job_postings',
            stream_name='job_postings',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/jobPosting.list',
                    action=Action.LIST,
                    description='List all job postings',
                    body_fields=['cursor', 'limit'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'cursor': {'type': 'string', 'description': 'Pagination cursor for next page'},
                            'limit': {'type': 'integer', 'description': 'Maximum number of records to return per page'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Job posting object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique job posting identifier'},
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Job posting title',
                                        },
                                        'jobId': {
                                            'type': ['string', 'null'],
                                            'description': 'Associated job identifier',
                                        },
                                        'departmentName': {
                                            'type': ['string', 'null'],
                                            'description': 'Department name',
                                        },
                                        'teamName': {
                                            'type': ['string', 'null'],
                                            'description': 'Team name',
                                        },
                                        'locationName': {
                                            'type': ['string', 'null'],
                                            'description': 'Location name',
                                        },
                                        'locationExternalName': {
                                            'type': ['string', 'null'],
                                            'description': 'External location name',
                                        },
                                        'workplaceType': {
                                            'type': ['string', 'null'],
                                            'description': 'Workplace type',
                                        },
                                        'employmentType': {
                                            'type': ['string', 'null'],
                                            'description': 'Employment type',
                                        },
                                        'isListed': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the posting is listed',
                                        },
                                        'publishedDate': {
                                            'type': ['string', 'null'],
                                            'description': 'Published date',
                                        },
                                        'applicationDeadline': {
                                            'type': ['string', 'null'],
                                            'description': 'Application deadline',
                                        },
                                        'externalLink': {
                                            'type': ['string', 'null'],
                                            'description': 'External link',
                                        },
                                        'applyLink': {
                                            'type': ['string', 'null'],
                                            'description': 'Apply link',
                                        },
                                        'locationIds': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'primaryLocationId': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'secondaryLocationIds': {
                                                            'type': ['array', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Location identifiers',
                                        },
                                        'compensationTierSummary': {
                                            'type': ['string', 'null'],
                                            'description': 'Compensation tier summary',
                                        },
                                        'shouldDisplayCompensationOnJobBoard': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether to display compensation on job board',
                                        },
                                        'updatedAt': {
                                            'type': ['string', 'null'],
                                            'description': 'Last update timestamp',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'job_postings',
                                    'x-airbyte-stream-name': 'job_postings',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Published job postings visible to external candidates',
                                        'when_to_use': 'Questions about published job listings or career page postings',
                                        'trigger_phrases': [
                                            'job posting',
                                            'job listing',
                                            'career page',
                                            'published job',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['What job postings are live?'],
                                        'search_strategy': 'Search by title',
                                    },
                                },
                            },
                            'moreDataAvailable': {'type': 'boolean'},
                            'nextCursor': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'cursor': '$.nextCursor', 'has_more': '$.moreDataAvailable'},
                ),
                Action.GET: EndpointDefinition(
                    method='POST',
                    path='/jobPosting.info',
                    action=Action.GET,
                    description='Get a single job posting by ID',
                    body_fields=['jobPostingId'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'jobPostingId': {'type': 'string', 'description': 'Job posting ID'},
                        },
                        'required': ['jobPostingId'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'object',
                                'description': 'Job posting object',
                                'properties': {
                                    'id': {'type': 'string', 'description': 'Unique job posting identifier'},
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'Job posting title',
                                    },
                                    'jobId': {
                                        'type': ['string', 'null'],
                                        'description': 'Associated job identifier',
                                    },
                                    'departmentName': {
                                        'type': ['string', 'null'],
                                        'description': 'Department name',
                                    },
                                    'teamName': {
                                        'type': ['string', 'null'],
                                        'description': 'Team name',
                                    },
                                    'locationName': {
                                        'type': ['string', 'null'],
                                        'description': 'Location name',
                                    },
                                    'locationExternalName': {
                                        'type': ['string', 'null'],
                                        'description': 'External location name',
                                    },
                                    'workplaceType': {
                                        'type': ['string', 'null'],
                                        'description': 'Workplace type',
                                    },
                                    'employmentType': {
                                        'type': ['string', 'null'],
                                        'description': 'Employment type',
                                    },
                                    'isListed': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the posting is listed',
                                    },
                                    'publishedDate': {
                                        'type': ['string', 'null'],
                                        'description': 'Published date',
                                    },
                                    'applicationDeadline': {
                                        'type': ['string', 'null'],
                                        'description': 'Application deadline',
                                    },
                                    'externalLink': {
                                        'type': ['string', 'null'],
                                        'description': 'External link',
                                    },
                                    'applyLink': {
                                        'type': ['string', 'null'],
                                        'description': 'Apply link',
                                    },
                                    'locationIds': {
                                        'oneOf': [
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'primaryLocationId': {
                                                        'type': ['string', 'null'],
                                                    },
                                                    'secondaryLocationIds': {
                                                        'type': ['array', 'null'],
                                                    },
                                                },
                                            },
                                            {'type': 'null'},
                                        ],
                                        'description': 'Location identifiers',
                                    },
                                    'compensationTierSummary': {
                                        'type': ['string', 'null'],
                                        'description': 'Compensation tier summary',
                                    },
                                    'shouldDisplayCompensationOnJobBoard': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether to display compensation on job board',
                                    },
                                    'updatedAt': {
                                        'type': ['string', 'null'],
                                        'description': 'Last update timestamp',
                                    },
                                },
                                'required': ['id'],
                                'x-airbyte-entity-name': 'job_postings',
                                'x-airbyte-stream-name': 'job_postings',
                                'x-airbyte-ai-hints': {
                                    'summary': 'Published job postings visible to external candidates',
                                    'when_to_use': 'Questions about published job listings or career page postings',
                                    'trigger_phrases': [
                                        'job posting',
                                        'job listing',
                                        'career page',
                                        'published job',
                                    ],
                                    'freshness': 'live',
                                    'example_questions': ['What job postings are live?'],
                                    'search_strategy': 'Search by title',
                                },
                            },
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Job posting object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique job posting identifier'},
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Job posting title',
                    },
                    'jobId': {
                        'type': ['string', 'null'],
                        'description': 'Associated job identifier',
                    },
                    'departmentName': {
                        'type': ['string', 'null'],
                        'description': 'Department name',
                    },
                    'teamName': {
                        'type': ['string', 'null'],
                        'description': 'Team name',
                    },
                    'locationName': {
                        'type': ['string', 'null'],
                        'description': 'Location name',
                    },
                    'locationExternalName': {
                        'type': ['string', 'null'],
                        'description': 'External location name',
                    },
                    'workplaceType': {
                        'type': ['string', 'null'],
                        'description': 'Workplace type',
                    },
                    'employmentType': {
                        'type': ['string', 'null'],
                        'description': 'Employment type',
                    },
                    'isListed': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the posting is listed',
                    },
                    'publishedDate': {
                        'type': ['string', 'null'],
                        'description': 'Published date',
                    },
                    'applicationDeadline': {
                        'type': ['string', 'null'],
                        'description': 'Application deadline',
                    },
                    'externalLink': {
                        'type': ['string', 'null'],
                        'description': 'External link',
                    },
                    'applyLink': {
                        'type': ['string', 'null'],
                        'description': 'Apply link',
                    },
                    'locationIds': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'primaryLocationId': {
                                        'type': ['string', 'null'],
                                    },
                                    'secondaryLocationIds': {
                                        'type': ['array', 'null'],
                                    },
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Location identifiers',
                    },
                    'compensationTierSummary': {
                        'type': ['string', 'null'],
                        'description': 'Compensation tier summary',
                    },
                    'shouldDisplayCompensationOnJobBoard': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether to display compensation on job board',
                    },
                    'updatedAt': {
                        'type': ['string', 'null'],
                        'description': 'Last update timestamp',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'job_postings',
                'x-airbyte-stream-name': 'job_postings',
                'x-airbyte-ai-hints': {
                    'summary': 'Published job postings visible to external candidates',
                    'when_to_use': 'Questions about published job listings or career page postings',
                    'trigger_phrases': [
                        'job posting',
                        'job listing',
                        'career page',
                        'published job',
                    ],
                    'freshness': 'live',
                    'example_questions': ['What job postings are live?'],
                    'search_strategy': 'Search by title',
                },
            },
            ai_hints={
                'summary': 'Published job postings visible to external candidates',
                'when_to_use': 'Questions about published job listings or career page postings',
                'trigger_phrases': [
                    'job posting',
                    'job listing',
                    'career page',
                    'published job',
                ],
                'freshness': 'live',
                'example_questions': ['What job postings are live?'],
                'search_strategy': 'Search by title',
            },
        ),
        EntityDefinition(
            name='sources',
            stream_name='sources',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/source.list',
                    action=Action.LIST,
                    description='List all candidate sources',
                    body_fields=['cursor', 'limit'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'cursor': {'type': 'string', 'description': 'Pagination cursor for next page'},
                            'limit': {'type': 'integer', 'description': 'Maximum number of records to return per page'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Candidate source object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique source identifier'},
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Source title',
                                        },
                                        'isArchived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the source is archived',
                                        },
                                        'sourceType': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'title': {
                                                            'type': ['string', 'null'],
                                                        },
                                                        'isArchived': {
                                                            'type': ['boolean', 'null'],
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Source type',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'sources',
                                    'x-airbyte-stream-name': 'sources',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Candidate sources tracking where applicants originate',
                                        'when_to_use': 'Questions about recruitment channels or sourcing analytics',
                                        'trigger_phrases': ['candidate source', 'referral', 'where did they apply'],
                                        'freshness': 'static',
                                        'example_questions': ['What candidate sources are tracked?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                            'moreDataAvailable': {'type': 'boolean'},
                            'nextCursor': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'cursor': '$.nextCursor', 'has_more': '$.moreDataAvailable'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Candidate source object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique source identifier'},
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Source title',
                    },
                    'isArchived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the source is archived',
                    },
                    'sourceType': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'id': {
                                        'type': ['string', 'null'],
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                    },
                                    'isArchived': {
                                        'type': ['boolean', 'null'],
                                    },
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Source type',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'sources',
                'x-airbyte-stream-name': 'sources',
                'x-airbyte-ai-hints': {
                    'summary': 'Candidate sources tracking where applicants originate',
                    'when_to_use': 'Questions about recruitment channels or sourcing analytics',
                    'trigger_phrases': ['candidate source', 'referral', 'where did they apply'],
                    'freshness': 'static',
                    'example_questions': ['What candidate sources are tracked?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Candidate sources tracking where applicants originate',
                'when_to_use': 'Questions about recruitment channels or sourcing analytics',
                'trigger_phrases': ['candidate source', 'referral', 'where did they apply'],
                'freshness': 'static',
                'example_questions': ['What candidate sources are tracked?'],
                'search_strategy': 'Search by name',
            },
        ),
        EntityDefinition(
            name='archive_reasons',
            stream_name='archive_reasons',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/archiveReason.list',
                    action=Action.LIST,
                    description='List all archive reasons',
                    body_fields=['cursor', 'limit'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'cursor': {'type': 'string', 'description': 'Pagination cursor for next page'},
                            'limit': {'type': 'integer', 'description': 'Maximum number of records to return per page'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Archive reason object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique archive reason identifier'},
                                        'text': {
                                            'type': ['string', 'null'],
                                            'description': 'Archive reason text',
                                        },
                                        'reasonType': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of archive reason',
                                        },
                                        'isArchived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the archive reason is archived',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'archive_reasons',
                                    'x-airbyte-stream-name': 'archive_reasons',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Reasons for archiving or rejecting candidates',
                                        'when_to_use': 'Questions about rejection reasons or archive categories',
                                        'trigger_phrases': ['archive reason', 'rejection reason', 'why rejected'],
                                        'freshness': 'static',
                                        'example_questions': ['What archive reasons are configured in Ashby?'],
                                        'search_strategy': 'Search by name or text',
                                    },
                                },
                            },
                            'moreDataAvailable': {'type': 'boolean'},
                            'nextCursor': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'cursor': '$.nextCursor', 'has_more': '$.moreDataAvailable'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Archive reason object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique archive reason identifier'},
                    'text': {
                        'type': ['string', 'null'],
                        'description': 'Archive reason text',
                    },
                    'reasonType': {
                        'type': ['string', 'null'],
                        'description': 'Type of archive reason',
                    },
                    'isArchived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the archive reason is archived',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'archive_reasons',
                'x-airbyte-stream-name': 'archive_reasons',
                'x-airbyte-ai-hints': {
                    'summary': 'Reasons for archiving or rejecting candidates',
                    'when_to_use': 'Questions about rejection reasons or archive categories',
                    'trigger_phrases': ['archive reason', 'rejection reason', 'why rejected'],
                    'freshness': 'static',
                    'example_questions': ['What archive reasons are configured in Ashby?'],
                    'search_strategy': 'Search by name or text',
                },
            },
            ai_hints={
                'summary': 'Reasons for archiving or rejecting candidates',
                'when_to_use': 'Questions about rejection reasons or archive categories',
                'trigger_phrases': ['archive reason', 'rejection reason', 'why rejected'],
                'freshness': 'static',
                'example_questions': ['What archive reasons are configured in Ashby?'],
                'search_strategy': 'Search by name or text',
            },
        ),
        EntityDefinition(
            name='candidate_tags',
            stream_name='candidate_tags',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/candidateTag.list',
                    action=Action.LIST,
                    description='List all candidate tags',
                    body_fields=['cursor', 'limit'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'cursor': {'type': 'string', 'description': 'Pagination cursor for next page'},
                            'limit': {'type': 'integer', 'description': 'Maximum number of records to return per page'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Candidate tag object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique tag identifier'},
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Tag title',
                                        },
                                        'isArchived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the tag is archived',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'candidate_tags',
                                    'x-airbyte-stream-name': 'candidate_tags',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Tags applied to candidates for categorization',
                                        'when_to_use': 'Looking up or filtering candidates by tags',
                                        'trigger_phrases': ['candidate tag', 'tagged candidate'],
                                        'freshness': 'live',
                                        'example_questions': ['What candidate tags exist?'],
                                        'search_strategy': 'Search by tag name',
                                    },
                                },
                            },
                            'moreDataAvailable': {'type': 'boolean'},
                            'nextCursor': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'cursor': '$.nextCursor', 'has_more': '$.moreDataAvailable'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Candidate tag object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique tag identifier'},
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Tag title',
                    },
                    'isArchived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the tag is archived',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'candidate_tags',
                'x-airbyte-stream-name': 'candidate_tags',
                'x-airbyte-ai-hints': {
                    'summary': 'Tags applied to candidates for categorization',
                    'when_to_use': 'Looking up or filtering candidates by tags',
                    'trigger_phrases': ['candidate tag', 'tagged candidate'],
                    'freshness': 'live',
                    'example_questions': ['What candidate tags exist?'],
                    'search_strategy': 'Search by tag name',
                },
            },
            ai_hints={
                'summary': 'Tags applied to candidates for categorization',
                'when_to_use': 'Looking up or filtering candidates by tags',
                'trigger_phrases': ['candidate tag', 'tagged candidate'],
                'freshness': 'live',
                'example_questions': ['What candidate tags exist?'],
                'search_strategy': 'Search by tag name',
            },
        ),
        EntityDefinition(
            name='custom_fields',
            stream_name='custom_fields',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/customField.list',
                    action=Action.LIST,
                    description='List all custom fields',
                    body_fields=['cursor', 'limit'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'cursor': {'type': 'string', 'description': 'Pagination cursor for next page'},
                            'limit': {'type': 'integer', 'description': 'Maximum number of records to return per page'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Custom field definition',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique custom field identifier'},
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Custom field title',
                                        },
                                        'objectType': {
                                            'type': ['string', 'null'],
                                            'description': 'Object type this field applies to',
                                        },
                                        'isArchived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the custom field is archived',
                                        },
                                        'isPrivate': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the custom field is private',
                                        },
                                        'fieldType': {
                                            'type': ['string', 'null'],
                                            'description': 'Field type',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'custom_fields',
                                    'x-airbyte-stream-name': 'custom_fields',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Custom field definitions in Ashby',
                                        'when_to_use': 'Questions about custom data fields or metadata configuration',
                                        'trigger_phrases': ['custom field', 'field definition', 'metadata field'],
                                        'freshness': 'static',
                                        'example_questions': ['What custom fields are defined in Ashby?'],
                                        'search_strategy': 'Search by field name',
                                    },
                                },
                            },
                            'moreDataAvailable': {'type': 'boolean'},
                            'nextCursor': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'cursor': '$.nextCursor', 'has_more': '$.moreDataAvailable'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Custom field definition',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique custom field identifier'},
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Custom field title',
                    },
                    'objectType': {
                        'type': ['string', 'null'],
                        'description': 'Object type this field applies to',
                    },
                    'isArchived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the custom field is archived',
                    },
                    'isPrivate': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the custom field is private',
                    },
                    'fieldType': {
                        'type': ['string', 'null'],
                        'description': 'Field type',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'custom_fields',
                'x-airbyte-stream-name': 'custom_fields',
                'x-airbyte-ai-hints': {
                    'summary': 'Custom field definitions in Ashby',
                    'when_to_use': 'Questions about custom data fields or metadata configuration',
                    'trigger_phrases': ['custom field', 'field definition', 'metadata field'],
                    'freshness': 'static',
                    'example_questions': ['What custom fields are defined in Ashby?'],
                    'search_strategy': 'Search by field name',
                },
            },
            ai_hints={
                'summary': 'Custom field definitions in Ashby',
                'when_to_use': 'Questions about custom data fields or metadata configuration',
                'trigger_phrases': ['custom field', 'field definition', 'metadata field'],
                'freshness': 'static',
                'example_questions': ['What custom fields are defined in Ashby?'],
                'search_strategy': 'Search by field name',
            },
        ),
        EntityDefinition(
            name='feedback_form_definitions',
            stream_name='feedback_form_definitions',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/feedbackFormDefinition.list',
                    action=Action.LIST,
                    description='List all feedback form definitions',
                    body_fields=['cursor', 'limit'],
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'cursor': {'type': 'string', 'description': 'Pagination cursor for next page'},
                            'limit': {'type': 'integer', 'description': 'Maximum number of records to return per page'},
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'success': {'type': 'boolean'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Feedback form definition',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique feedback form definition identifier'},
                                        'organizationId': {
                                            'type': ['string', 'null'],
                                            'description': 'Organization identifier',
                                        },
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'Form title',
                                        },
                                        'isArchived': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the form is archived',
                                        },
                                        'isDefaultForm': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether this is the default form',
                                        },
                                        'formDefinition': {
                                            'oneOf': [
                                                {
                                                    'type': 'object',
                                                    'properties': {
                                                        'sections': {
                                                            'type': ['array', 'null'],
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'fields': {
                                                                        'type': ['array', 'null'],
                                                                        'items': {
                                                                            'type': 'object',
                                                                            'properties': {
                                                                                'isRequired': {
                                                                                    'type': ['boolean', 'null'],
                                                                                },
                                                                                'field': {
                                                                                    'oneOf': [
                                                                                        {
                                                                                            'type': 'object',
                                                                                            'properties': {
                                                                                                'id': {
                                                                                                    'type': ['string', 'null'],
                                                                                                },
                                                                                                'type': {
                                                                                                    'type': ['string', 'null'],
                                                                                                },
                                                                                                'path': {
                                                                                                    'type': ['string', 'null'],
                                                                                                },
                                                                                                'humanReadablePath': {
                                                                                                    'type': ['string', 'null'],
                                                                                                },
                                                                                                'title': {
                                                                                                    'type': ['string', 'null'],
                                                                                                },
                                                                                                'isNullable': {
                                                                                                    'type': ['boolean', 'null'],
                                                                                                },
                                                                                                'selectableValues': {
                                                                                                    'type': ['array', 'null'],
                                                                                                    'items': {
                                                                                                        'type': 'object',
                                                                                                        'properties': {
                                                                                                            'label': {
                                                                                                                'type': ['string', 'null'],
                                                                                                            },
                                                                                                            'value': {
                                                                                                                'type': ['string', 'null'],
                                                                                                            },
                                                                                                        },
                                                                                                    },
                                                                                                },
                                                                                            },
                                                                                        },
                                                                                        {'type': 'null'},
                                                                                    ],
                                                                                },
                                                                                'descriptionHtml': {
                                                                                    'type': ['string', 'null'],
                                                                                },
                                                                                'descriptionPlain': {
                                                                                    'type': ['string', 'null'],
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                    'title': {
                                                                        'type': ['string', 'null'],
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                {'type': 'null'},
                                            ],
                                            'description': 'Form definition with sections and fields',
                                        },
                                        'interviewId': {
                                            'type': ['string', 'null'],
                                            'description': 'Associated interview identifier',
                                        },
                                    },
                                    'required': ['id'],
                                    'x-airbyte-entity-name': 'feedback_form_definitions',
                                    'x-airbyte-stream-name': 'feedback_form_definitions',
                                    'x-airbyte-ai-hints': {
                                        'summary': 'Interview feedback form templates in Ashby',
                                        'when_to_use': 'Questions about feedback forms or interview evaluation templates',
                                        'trigger_phrases': ['feedback form', 'interview form', 'evaluation template'],
                                        'freshness': 'static',
                                        'example_questions': ['What feedback forms are available?'],
                                        'search_strategy': 'Search by name',
                                    },
                                },
                            },
                            'moreDataAvailable': {'type': 'boolean'},
                            'nextCursor': {
                                'type': ['string', 'null'],
                            },
                        },
                    },
                    record_extractor='$.results',
                    meta_extractor={'cursor': '$.nextCursor', 'has_more': '$.moreDataAvailable'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Feedback form definition',
                'properties': {
                    'id': {'type': 'string', 'description': 'Unique feedback form definition identifier'},
                    'organizationId': {
                        'type': ['string', 'null'],
                        'description': 'Organization identifier',
                    },
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'Form title',
                    },
                    'isArchived': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the form is archived',
                    },
                    'isDefaultForm': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether this is the default form',
                    },
                    'formDefinition': {
                        'oneOf': [
                            {
                                'type': 'object',
                                'properties': {
                                    'sections': {
                                        'type': ['array', 'null'],
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'fields': {
                                                    'type': ['array', 'null'],
                                                    'items': {
                                                        'type': 'object',
                                                        'properties': {
                                                            'isRequired': {
                                                                'type': ['boolean', 'null'],
                                                            },
                                                            'field': {
                                                                'oneOf': [
                                                                    {
                                                                        'type': 'object',
                                                                        'properties': {
                                                                            'id': {
                                                                                'type': ['string', 'null'],
                                                                            },
                                                                            'type': {
                                                                                'type': ['string', 'null'],
                                                                            },
                                                                            'path': {
                                                                                'type': ['string', 'null'],
                                                                            },
                                                                            'humanReadablePath': {
                                                                                'type': ['string', 'null'],
                                                                            },
                                                                            'title': {
                                                                                'type': ['string', 'null'],
                                                                            },
                                                                            'isNullable': {
                                                                                'type': ['boolean', 'null'],
                                                                            },
                                                                            'selectableValues': {
                                                                                'type': ['array', 'null'],
                                                                                'items': {
                                                                                    'type': 'object',
                                                                                    'properties': {
                                                                                        'label': {
                                                                                            'type': ['string', 'null'],
                                                                                        },
                                                                                        'value': {
                                                                                            'type': ['string', 'null'],
                                                                                        },
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                    {'type': 'null'},
                                                                ],
                                                            },
                                                            'descriptionHtml': {
                                                                'type': ['string', 'null'],
                                                            },
                                                            'descriptionPlain': {
                                                                'type': ['string', 'null'],
                                                            },
                                                        },
                                                    },
                                                },
                                                'title': {
                                                    'type': ['string', 'null'],
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            {'type': 'null'},
                        ],
                        'description': 'Form definition with sections and fields',
                    },
                    'interviewId': {
                        'type': ['string', 'null'],
                        'description': 'Associated interview identifier',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'feedback_form_definitions',
                'x-airbyte-stream-name': 'feedback_form_definitions',
                'x-airbyte-ai-hints': {
                    'summary': 'Interview feedback form templates in Ashby',
                    'when_to_use': 'Questions about feedback forms or interview evaluation templates',
                    'trigger_phrases': ['feedback form', 'interview form', 'evaluation template'],
                    'freshness': 'static',
                    'example_questions': ['What feedback forms are available?'],
                    'search_strategy': 'Search by name',
                },
            },
            ai_hints={
                'summary': 'Interview feedback form templates in Ashby',
                'when_to_use': 'Questions about feedback forms or interview evaluation templates',
                'trigger_phrases': ['feedback form', 'interview form', 'evaluation template'],
                'freshness': 'static',
                'example_questions': ['What feedback forms are available?'],
                'search_strategy': 'Search by name',
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
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the application',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Current application status (e.g. active, archived, hired)',
                    ),
                    CacheFieldConfig(
                        name='archiveReason',
                        type=['null', 'string'],
                        description='Reason the application was archived, if applicable',
                    ),
                    CacheFieldConfig(
                        name='createdAt',
                        type=['null', 'string'],
                        description='Timestamp when the application was created, in ISO 8601 format',
                    ),
                    CacheFieldConfig(
                        name='updatedAt',
                        type=['null', 'string'],
                        description='Timestamp when the application was last updated, in ISO 8601 format',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='candidates',
                suggested=True,
                x_airbyte_name='candidates',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the candidate',
                    ),
                    CacheFieldConfig(
                        name='name',
                        type=['null', 'string'],
                        description='Full name of the candidate',
                    ),
                    CacheFieldConfig(
                        name='company',
                        type=['null', 'string'],
                        description="Candidate's current company",
                    ),
                    CacheFieldConfig(
                        name='position',
                        type=['null', 'string'],
                        description="Candidate's current position or title",
                    ),
                    CacheFieldConfig(
                        name='school',
                        type=['null', 'string'],
                        description="School associated with the candidate's education",
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='job_postings',
                suggested=True,
                x_airbyte_name='job_postings',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the job posting',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='Title of the job posting',
                    ),
                    CacheFieldConfig(
                        name='isListed',
                        type=['null', 'boolean'],
                        description='Whether the job posting is currently published/listed',
                    ),
                    CacheFieldConfig(
                        name='jobId',
                        type=['null', 'string'],
                        description='Identifier of the job this posting belongs to',
                    ),
                    CacheFieldConfig(
                        name='locationName',
                        type=['null', 'string'],
                        description='Name of the location associated with the posting',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='jobs',
                suggested=True,
                x_airbyte_name='jobs',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the job',
                    ),
                    CacheFieldConfig(
                        name='title',
                        type=['null', 'string'],
                        description='Title of the job',
                    ),
                    CacheFieldConfig(
                        name='status',
                        type=['null', 'string'],
                        description='Current status of the job (e.g. open, closed, draft)',
                    ),
                    CacheFieldConfig(
                        name='departmentId',
                        type=['null', 'string'],
                        description='Identifier of the department the job belongs to',
                    ),
                    CacheFieldConfig(
                        name='locationId',
                        type=['null', 'string'],
                        description='Identifier of the primary location of the job',
                    ),
                ],
            ),
            CacheEntityConfig(
                entity='users',
                suggested=True,
                x_airbyte_name='users',
                fields=[
                    CacheFieldConfig(
                        name='id',
                        type=['null', 'string'],
                        description='Unique identifier for the user',
                    ),
                    CacheFieldConfig(
                        name='firstName',
                        type=['null', 'string'],
                        description='First name of the user',
                    ),
                    CacheFieldConfig(
                        name='lastName',
                        type=['null', 'string'],
                        description='Last name of the user',
                    ),
                    CacheFieldConfig(
                        name='email',
                        type=['null', 'string'],
                        description='Primary email address of the user',
                    ),
                ],
            ),
        ],
    ),
    search_field_paths={
        'applications': [
            'id',
            'status',
            'archiveReason',
            'createdAt',
            'updatedAt',
        ],
        'candidates': [
            'id',
            'name',
            'company',
            'position',
            'school',
        ],
        'job_postings': [
            'id',
            'title',
            'isListed',
            'jobId',
            'locationName',
        ],
        'jobs': [
            'id',
            'title',
            'status',
            'departmentId',
            'locationId',
        ],
        'users': [
            'id',
            'firstName',
            'lastName',
            'email',
        ],
    },
    example_questions=ExampleQuestions(
        direct=[
            'List all open jobs',
            'Show me all candidates',
            'List recent applications',
            'List all departments',
            'Show me all job postings',
            'List all users in the organization',
        ],
        context_store_search=[
            'Show me candidates who applied last month',
            'What are the top sources for job applications?',
            'Compare the number of applications across different departments',
            'Find candidates with multiple applications',
            'Summarize the candidate pipeline for our latest job posting',
            'Find the most active departments in recruiting this month',
        ],
        search=[
            'Show me candidates who applied last month',
            'What are the top sources for job applications?',
            'Compare the number of applications across different departments',
            'Find candidates with multiple applications',
            'Summarize the candidate pipeline for our latest job posting',
            'Find the most active departments in recruiting this month',
        ],
        unsupported=[
            'Create a new job posting',
            'Schedule an interview for a candidate',
            'Update a candidates application status',
            'Delete a candidate profile',
            'Send an offer letter to a candidate',
        ],
    ),
)