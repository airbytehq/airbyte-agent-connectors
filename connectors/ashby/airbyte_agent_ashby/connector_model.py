"""
Connector model for ashby.

This file is auto-generated from the connector definition at build time.
DO NOT EDIT MANUALLY - changes will be overwritten on next generation.
"""

from __future__ import annotations

from ._vendored.connector_sdk.types import (
    Action,
    AuthConfig,
    AuthType,
    ConnectorModel,
    EndpointDefinition,
    EntityDefinition,
)
from ._vendored.connector_sdk.schema.security import (
    AirbyteAuthConfig,
    AuthConfigFieldSpec,
)
from uuid import (
    UUID,
)

AshbyConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('4e8c9fa0-3634-499b-b948-11581b5c3efa'),
    name='ashby',
    version='0.1.2',
    base_url='https://api.ashbyhq.com',
    auth=AuthConfig(
        type=AuthType.BASIC,
        user_config_spec=AirbyteAuthConfig(
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
            },
        ),
    ],
)