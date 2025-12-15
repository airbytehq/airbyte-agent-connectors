"""
Connector model for greenhouse.

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
from ._vendored.connector_sdk.schema.components import (
    PathOverrideConfig,
)

GreenhouseConnectorModel: ConnectorModel = ConnectorModel(
    name='greenhouse',
    version='0.1.1',
    base_url='https://harvest.greenhouse.io/v1',
    auth=AuthConfig(
        type=AuthType.BASIC,
        user_config_spec=AirbyteAuthConfig(
            title='Harvest API Key Authentication',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='Harvest API Key',
                    description='Your Greenhouse Harvest API Key from the Dev Center',
                    airbyte_secret=True,
                ),
            },
            auth_mapping={'username': '${api_key}', 'password': ''},
        ),
    ),
    entities=[
        EntityDefinition(
            name='candidates',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/candidates',
                    action=Action.LIST,
                    description='Returns a paginated list of all candidates in the organization',
                    query_params=['per_page', 'page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse candidate object',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique candidate identifier'},
                                'first_name': {'type': 'string', 'description': "Candidate's first name"},
                                'last_name': {'type': 'string', 'description': "Candidate's last name"},
                                'company': {
                                    'type': ['string', 'null'],
                                    'description': "Candidate's current company",
                                },
                                'title': {
                                    'type': ['string', 'null'],
                                    'description': "Candidate's current title",
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the candidate was created',
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the candidate was last updated',
                                },
                                'last_activity': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the last activity occurred',
                                },
                                'is_private': {'type': 'boolean', 'description': 'Whether the candidate is private'},
                                'photo_url': {
                                    'type': ['string', 'null'],
                                    'description': "URL to candidate's photo",
                                },
                                'attachments': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'description': 'File attachment (resume, cover letter, etc.)',
                                        'properties': {
                                            'filename': {'type': 'string', 'description': 'Name of the attached file'},
                                            'url': {
                                                'type': 'string',
                                                'format': 'uri',
                                                'description': 'Temporary signed AWS S3 URL to download the file.\nThis URL expires within 7 days - download immediately after retrieval.\n',
                                            },
                                            'type': {
                                                'type': 'string',
                                                'enum': [
                                                    'resume',
                                                    'cover_letter',
                                                    'admin_only',
                                                    'take_home_test',
                                                    'offer_packet',
                                                    'offer_letter',
                                                    'signed_offer_letter',
                                                    'other',
                                                ],
                                                'description': 'Type of attachment',
                                            },
                                            'created_at': {
                                                'type': 'string',
                                                'format': 'date-time',
                                                'description': 'When the attachment was uploaded',
                                            },
                                        },
                                    },
                                    'description': 'Candidate attachments (resumes, cover letters, etc.)',
                                },
                                'application_ids': {
                                    'type': 'array',
                                    'items': {'type': 'integer'},
                                    'description': "IDs of candidate's applications",
                                },
                                'phone_numbers': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Candidate phone numbers',
                                },
                                'addresses': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Candidate addresses',
                                },
                                'email_addresses': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Candidate email addresses',
                                },
                                'website_addresses': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Candidate website addresses',
                                },
                                'social_media_addresses': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Candidate social media addresses',
                                },
                                'recruiter': {
                                    'type': ['object', 'null'],
                                    'description': 'Recruiter information',
                                },
                                'coordinator': {
                                    'type': ['object', 'null'],
                                    'description': 'Coordinator information',
                                },
                                'can_email': {'type': 'boolean', 'description': 'Whether the candidate can be emailed'},
                                'tags': {
                                    'type': 'array',
                                    'items': {'type': 'string'},
                                    'description': 'Candidate tags',
                                },
                                'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                            },
                            'x-airbyte-entity-name': 'candidates',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/candidates/{id}',
                    action=Action.GET,
                    description='Get a single candidate by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Greenhouse candidate object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique candidate identifier'},
                            'first_name': {'type': 'string', 'description': "Candidate's first name"},
                            'last_name': {'type': 'string', 'description': "Candidate's last name"},
                            'company': {
                                'type': ['string', 'null'],
                                'description': "Candidate's current company",
                            },
                            'title': {
                                'type': ['string', 'null'],
                                'description': "Candidate's current title",
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the candidate was created',
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the candidate was last updated',
                            },
                            'last_activity': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the last activity occurred',
                            },
                            'is_private': {'type': 'boolean', 'description': 'Whether the candidate is private'},
                            'photo_url': {
                                'type': ['string', 'null'],
                                'description': "URL to candidate's photo",
                            },
                            'attachments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'File attachment (resume, cover letter, etc.)',
                                    'properties': {
                                        'filename': {'type': 'string', 'description': 'Name of the attached file'},
                                        'url': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'Temporary signed AWS S3 URL to download the file.\nThis URL expires within 7 days - download immediately after retrieval.\n',
                                        },
                                        'type': {
                                            'type': 'string',
                                            'enum': [
                                                'resume',
                                                'cover_letter',
                                                'admin_only',
                                                'take_home_test',
                                                'offer_packet',
                                                'offer_letter',
                                                'signed_offer_letter',
                                                'other',
                                            ],
                                            'description': 'Type of attachment',
                                        },
                                        'created_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When the attachment was uploaded',
                                        },
                                    },
                                },
                                'description': 'Candidate attachments (resumes, cover letters, etc.)',
                            },
                            'application_ids': {
                                'type': 'array',
                                'items': {'type': 'integer'},
                                'description': "IDs of candidate's applications",
                            },
                            'phone_numbers': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Candidate phone numbers',
                            },
                            'addresses': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Candidate addresses',
                            },
                            'email_addresses': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Candidate email addresses',
                            },
                            'website_addresses': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Candidate website addresses',
                            },
                            'social_media_addresses': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Candidate social media addresses',
                            },
                            'recruiter': {
                                'type': ['object', 'null'],
                                'description': 'Recruiter information',
                            },
                            'coordinator': {
                                'type': ['object', 'null'],
                                'description': 'Coordinator information',
                            },
                            'can_email': {'type': 'boolean', 'description': 'Whether the candidate can be emailed'},
                            'tags': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Candidate tags',
                            },
                            'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                        },
                        'x-airbyte-entity-name': 'candidates',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse candidate object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique candidate identifier'},
                    'first_name': {'type': 'string', 'description': "Candidate's first name"},
                    'last_name': {'type': 'string', 'description': "Candidate's last name"},
                    'company': {
                        'type': ['string', 'null'],
                        'description': "Candidate's current company",
                    },
                    'title': {
                        'type': ['string', 'null'],
                        'description': "Candidate's current title",
                    },
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the candidate was created',
                    },
                    'updated_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the candidate was last updated',
                    },
                    'last_activity': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the last activity occurred',
                    },
                    'is_private': {'type': 'boolean', 'description': 'Whether the candidate is private'},
                    'photo_url': {
                        'type': ['string', 'null'],
                        'description': "URL to candidate's photo",
                    },
                    'attachments': {
                        'type': 'array',
                        'items': {'$ref': '#/components/schemas/Attachment'},
                        'description': 'Candidate attachments (resumes, cover letters, etc.)',
                    },
                    'application_ids': {
                        'type': 'array',
                        'items': {'type': 'integer'},
                        'description': "IDs of candidate's applications",
                    },
                    'phone_numbers': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Candidate phone numbers',
                    },
                    'addresses': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Candidate addresses',
                    },
                    'email_addresses': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Candidate email addresses',
                    },
                    'website_addresses': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Candidate website addresses',
                    },
                    'social_media_addresses': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Candidate social media addresses',
                    },
                    'recruiter': {
                        'type': ['object', 'null'],
                        'description': 'Recruiter information',
                    },
                    'coordinator': {
                        'type': ['object', 'null'],
                        'description': 'Coordinator information',
                    },
                    'can_email': {'type': 'boolean', 'description': 'Whether the candidate can be emailed'},
                    'tags': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Candidate tags',
                    },
                    'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                },
                'x-airbyte-entity-name': 'candidates',
            },
        ),
        EntityDefinition(
            name='applications',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/applications',
                    action=Action.LIST,
                    description='Returns a paginated list of all applications',
                    query_params=[
                        'per_page',
                        'page',
                        'created_before',
                        'created_after',
                        'last_activity_after',
                        'job_id',
                        'status',
                    ],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'created_before': {'type': 'string', 'required': False},
                        'created_after': {'type': 'string', 'required': False},
                        'last_activity_after': {'type': 'string', 'required': False},
                        'job_id': {'type': 'integer', 'required': False},
                        'status': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse application object',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique application identifier'},
                                'candidate_id': {'type': 'integer', 'description': 'ID of the associated candidate'},
                                'prospect': {'type': 'boolean', 'description': 'Whether this is a prospect application'},
                                'applied_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the application was submitted',
                                },
                                'rejected_at': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'When the application was rejected',
                                },
                                'last_activity_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the last activity occurred',
                                },
                                'location': {
                                    'type': ['object', 'null'],
                                    'description': 'Application location',
                                },
                                'source': {'type': 'object', 'description': 'Application source'},
                                'credited_to': {'type': 'object', 'description': 'User credited with the application'},
                                'rejection_reason': {
                                    'type': ['object', 'null'],
                                    'description': 'Rejection reason if rejected',
                                },
                                'rejection_details': {
                                    'type': ['object', 'null'],
                                    'description': 'Additional rejection details',
                                },
                                'jobs': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Jobs associated with the application',
                                },
                                'job_post_id': {
                                    'type': ['integer', 'null'],
                                    'description': 'ID of the job post',
                                },
                                'status': {'type': 'string', 'description': 'Application status'},
                                'current_stage': {
                                    'type': ['object', 'null'],
                                    'description': 'Current stage of the application',
                                },
                                'answers': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Application question answers',
                                },
                                'prospective_office': {
                                    'type': ['object', 'null'],
                                    'description': 'Prospective office',
                                },
                                'prospective_department': {
                                    'type': ['object', 'null'],
                                    'description': 'Prospective department',
                                },
                                'prospect_detail': {'type': 'object', 'description': 'Prospect details'},
                                'attachments': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'description': 'File attachment (resume, cover letter, etc.)',
                                        'properties': {
                                            'filename': {'type': 'string', 'description': 'Name of the attached file'},
                                            'url': {
                                                'type': 'string',
                                                'format': 'uri',
                                                'description': 'Temporary signed AWS S3 URL to download the file.\nThis URL expires within 7 days - download immediately after retrieval.\n',
                                            },
                                            'type': {
                                                'type': 'string',
                                                'enum': [
                                                    'resume',
                                                    'cover_letter',
                                                    'admin_only',
                                                    'take_home_test',
                                                    'offer_packet',
                                                    'offer_letter',
                                                    'signed_offer_letter',
                                                    'other',
                                                ],
                                                'description': 'Type of attachment',
                                            },
                                            'created_at': {
                                                'type': 'string',
                                                'format': 'date-time',
                                                'description': 'When the attachment was uploaded',
                                            },
                                        },
                                    },
                                    'description': 'Application attachments (resumes, cover letters, etc.)',
                                },
                                'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                            },
                            'x-airbyte-entity-name': 'applications',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/applications/{id}',
                    action=Action.GET,
                    description='Get a single application by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Greenhouse application object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique application identifier'},
                            'candidate_id': {'type': 'integer', 'description': 'ID of the associated candidate'},
                            'prospect': {'type': 'boolean', 'description': 'Whether this is a prospect application'},
                            'applied_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the application was submitted',
                            },
                            'rejected_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'When the application was rejected',
                            },
                            'last_activity_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the last activity occurred',
                            },
                            'location': {
                                'type': ['object', 'null'],
                                'description': 'Application location',
                            },
                            'source': {'type': 'object', 'description': 'Application source'},
                            'credited_to': {'type': 'object', 'description': 'User credited with the application'},
                            'rejection_reason': {
                                'type': ['object', 'null'],
                                'description': 'Rejection reason if rejected',
                            },
                            'rejection_details': {
                                'type': ['object', 'null'],
                                'description': 'Additional rejection details',
                            },
                            'jobs': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Jobs associated with the application',
                            },
                            'job_post_id': {
                                'type': ['integer', 'null'],
                                'description': 'ID of the job post',
                            },
                            'status': {'type': 'string', 'description': 'Application status'},
                            'current_stage': {
                                'type': ['object', 'null'],
                                'description': 'Current stage of the application',
                            },
                            'answers': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Application question answers',
                            },
                            'prospective_office': {
                                'type': ['object', 'null'],
                                'description': 'Prospective office',
                            },
                            'prospective_department': {
                                'type': ['object', 'null'],
                                'description': 'Prospective department',
                            },
                            'prospect_detail': {'type': 'object', 'description': 'Prospect details'},
                            'attachments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'File attachment (resume, cover letter, etc.)',
                                    'properties': {
                                        'filename': {'type': 'string', 'description': 'Name of the attached file'},
                                        'url': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'Temporary signed AWS S3 URL to download the file.\nThis URL expires within 7 days - download immediately after retrieval.\n',
                                        },
                                        'type': {
                                            'type': 'string',
                                            'enum': [
                                                'resume',
                                                'cover_letter',
                                                'admin_only',
                                                'take_home_test',
                                                'offer_packet',
                                                'offer_letter',
                                                'signed_offer_letter',
                                                'other',
                                            ],
                                            'description': 'Type of attachment',
                                        },
                                        'created_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When the attachment was uploaded',
                                        },
                                    },
                                },
                                'description': 'Application attachments (resumes, cover letters, etc.)',
                            },
                            'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                        },
                        'x-airbyte-entity-name': 'applications',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse application object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique application identifier'},
                    'candidate_id': {'type': 'integer', 'description': 'ID of the associated candidate'},
                    'prospect': {'type': 'boolean', 'description': 'Whether this is a prospect application'},
                    'applied_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the application was submitted',
                    },
                    'rejected_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the application was rejected',
                    },
                    'last_activity_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the last activity occurred',
                    },
                    'location': {
                        'type': ['object', 'null'],
                        'description': 'Application location',
                    },
                    'source': {'type': 'object', 'description': 'Application source'},
                    'credited_to': {'type': 'object', 'description': 'User credited with the application'},
                    'rejection_reason': {
                        'type': ['object', 'null'],
                        'description': 'Rejection reason if rejected',
                    },
                    'rejection_details': {
                        'type': ['object', 'null'],
                        'description': 'Additional rejection details',
                    },
                    'jobs': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Jobs associated with the application',
                    },
                    'job_post_id': {
                        'type': ['integer', 'null'],
                        'description': 'ID of the job post',
                    },
                    'status': {'type': 'string', 'description': 'Application status'},
                    'current_stage': {
                        'type': ['object', 'null'],
                        'description': 'Current stage of the application',
                    },
                    'answers': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Application question answers',
                    },
                    'prospective_office': {
                        'type': ['object', 'null'],
                        'description': 'Prospective office',
                    },
                    'prospective_department': {
                        'type': ['object', 'null'],
                        'description': 'Prospective department',
                    },
                    'prospect_detail': {'type': 'object', 'description': 'Prospect details'},
                    'attachments': {
                        'type': 'array',
                        'items': {'$ref': '#/components/schemas/Attachment'},
                        'description': 'Application attachments (resumes, cover letters, etc.)',
                    },
                    'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                },
                'x-airbyte-entity-name': 'applications',
            },
        ),
        EntityDefinition(
            name='jobs',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/jobs',
                    action=Action.LIST,
                    description='Returns a paginated list of all jobs in the organization',
                    query_params=['per_page', 'page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse job object',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique job identifier'},
                                'name': {'type': 'string', 'description': 'Job name'},
                                'requisition_id': {
                                    'type': ['string', 'null'],
                                    'description': 'Job requisition ID',
                                },
                                'notes': {
                                    'type': ['string', 'null'],
                                    'description': 'Job notes',
                                },
                                'confidential': {'type': 'boolean', 'description': 'Whether the job is confidential'},
                                'status': {'type': 'string', 'description': 'Job status'},
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the job was created',
                                },
                                'opened_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the job was opened',
                                },
                                'closed_at': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'When the job was closed',
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the job was last updated',
                                },
                                'departments': {
                                    'type': 'array',
                                    'items': {
                                        'type': ['object', 'null'],
                                    },
                                    'description': 'Departments associated with the job',
                                },
                                'offices': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Offices associated with the job',
                                },
                                'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                                'hiring_team': {'type': 'object', 'description': 'Hiring team information'},
                                'openings': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Job openings',
                                },
                            },
                            'x-airbyte-entity-name': 'jobs',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/jobs/{id}',
                    action=Action.GET,
                    description='Get a single job by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Greenhouse job object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique job identifier'},
                            'name': {'type': 'string', 'description': 'Job name'},
                            'requisition_id': {
                                'type': ['string', 'null'],
                                'description': 'Job requisition ID',
                            },
                            'notes': {
                                'type': ['string', 'null'],
                                'description': 'Job notes',
                            },
                            'confidential': {'type': 'boolean', 'description': 'Whether the job is confidential'},
                            'status': {'type': 'string', 'description': 'Job status'},
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the job was created',
                            },
                            'opened_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the job was opened',
                            },
                            'closed_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'When the job was closed',
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the job was last updated',
                            },
                            'departments': {
                                'type': 'array',
                                'items': {
                                    'type': ['object', 'null'],
                                },
                                'description': 'Departments associated with the job',
                            },
                            'offices': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Offices associated with the job',
                            },
                            'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                            'hiring_team': {'type': 'object', 'description': 'Hiring team information'},
                            'openings': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Job openings',
                            },
                        },
                        'x-airbyte-entity-name': 'jobs',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse job object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique job identifier'},
                    'name': {'type': 'string', 'description': 'Job name'},
                    'requisition_id': {
                        'type': ['string', 'null'],
                        'description': 'Job requisition ID',
                    },
                    'notes': {
                        'type': ['string', 'null'],
                        'description': 'Job notes',
                    },
                    'confidential': {'type': 'boolean', 'description': 'Whether the job is confidential'},
                    'status': {'type': 'string', 'description': 'Job status'},
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the job was created',
                    },
                    'opened_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the job was opened',
                    },
                    'closed_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the job was closed',
                    },
                    'updated_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the job was last updated',
                    },
                    'departments': {
                        'type': 'array',
                        'items': {
                            'type': ['object', 'null'],
                        },
                        'description': 'Departments associated with the job',
                    },
                    'offices': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Offices associated with the job',
                    },
                    'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                    'hiring_team': {'type': 'object', 'description': 'Hiring team information'},
                    'openings': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Job openings',
                    },
                },
                'x-airbyte-entity-name': 'jobs',
            },
        ),
        EntityDefinition(
            name='offers',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/offers',
                    action=Action.LIST,
                    description='Returns a paginated list of all offers',
                    query_params=[
                        'per_page',
                        'page',
                        'created_before',
                        'created_after',
                        'resolved_after',
                    ],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'created_before': {'type': 'string', 'required': False},
                        'created_after': {'type': 'string', 'required': False},
                        'resolved_after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse offer object',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique offer identifier'},
                                'version': {'type': 'integer', 'description': 'Offer version number'},
                                'application_id': {'type': 'integer', 'description': 'Associated application ID'},
                                'job_id': {'type': 'integer', 'description': 'Associated job ID'},
                                'candidate_id': {'type': 'integer', 'description': 'Associated candidate ID'},
                                'opening': {
                                    'type': ['object', 'null'],
                                    'description': 'Associated job opening',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the offer was created',
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the offer was last updated',
                                },
                                'sent_at': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'When the offer was sent',
                                },
                                'resolved_at': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'When the offer was resolved',
                                },
                                'starts_at': {
                                    'type': ['string', 'null'],
                                    'description': 'Employment start date',
                                },
                                'status': {'type': 'string', 'description': 'Offer status'},
                                'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                            },
                            'x-airbyte-entity-name': 'offers',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/offers/{id}',
                    action=Action.GET,
                    description='Get a single offer by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Greenhouse offer object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique offer identifier'},
                            'version': {'type': 'integer', 'description': 'Offer version number'},
                            'application_id': {'type': 'integer', 'description': 'Associated application ID'},
                            'job_id': {'type': 'integer', 'description': 'Associated job ID'},
                            'candidate_id': {'type': 'integer', 'description': 'Associated candidate ID'},
                            'opening': {
                                'type': ['object', 'null'],
                                'description': 'Associated job opening',
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the offer was created',
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the offer was last updated',
                            },
                            'sent_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'When the offer was sent',
                            },
                            'resolved_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'When the offer was resolved',
                            },
                            'starts_at': {
                                'type': ['string', 'null'],
                                'description': 'Employment start date',
                            },
                            'status': {'type': 'string', 'description': 'Offer status'},
                            'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                        },
                        'x-airbyte-entity-name': 'offers',
                    },
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse offer object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique offer identifier'},
                    'version': {'type': 'integer', 'description': 'Offer version number'},
                    'application_id': {'type': 'integer', 'description': 'Associated application ID'},
                    'job_id': {'type': 'integer', 'description': 'Associated job ID'},
                    'candidate_id': {'type': 'integer', 'description': 'Associated candidate ID'},
                    'opening': {
                        'type': ['object', 'null'],
                        'description': 'Associated job opening',
                    },
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the offer was created',
                    },
                    'updated_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the offer was last updated',
                    },
                    'sent_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the offer was sent',
                    },
                    'resolved_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the offer was resolved',
                    },
                    'starts_at': {
                        'type': ['string', 'null'],
                        'description': 'Employment start date',
                    },
                    'status': {'type': 'string', 'description': 'Offer status'},
                    'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                },
                'x-airbyte-entity-name': 'offers',
            },
        ),
        EntityDefinition(
            name='users',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/users',
                    action=Action.LIST,
                    description='Returns a paginated list of all users',
                    query_params=[
                        'per_page',
                        'page',
                        'created_before',
                        'created_after',
                        'updated_before',
                        'updated_after',
                    ],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'created_before': {'type': 'string', 'required': False},
                        'created_after': {'type': 'string', 'required': False},
                        'updated_before': {'type': 'string', 'required': False},
                        'updated_after': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse user object',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique user identifier'},
                                'name': {'type': 'string', 'description': "User's full name"},
                                'first_name': {'type': 'string', 'description': "User's first name"},
                                'last_name': {'type': 'string', 'description': "User's last name"},
                                'primary_email_address': {
                                    'type': 'string',
                                    'format': 'email',
                                    'description': "User's primary email address",
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the user was last updated',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the user was created',
                                },
                                'disabled': {'type': 'boolean', 'description': 'Whether the user is disabled'},
                                'site_admin': {'type': 'boolean', 'description': 'Whether the user is a site admin'},
                                'emails': {
                                    'type': 'array',
                                    'items': {'type': 'string'},
                                    'description': 'All user email addresses',
                                },
                                'employee_id': {
                                    'type': ['string', 'null'],
                                    'description': 'Employee ID',
                                },
                                'linked_candidate_ids': {
                                    'type': 'array',
                                    'items': {'type': 'integer'},
                                    'description': 'IDs of linked candidates',
                                },
                                'offices': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Associated offices',
                                },
                                'departments': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Associated departments',
                                },
                            },
                            'x-airbyte-entity-name': 'users',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/users/{id}',
                    action=Action.GET,
                    description='Get a single user by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Greenhouse user object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique user identifier'},
                            'name': {'type': 'string', 'description': "User's full name"},
                            'first_name': {'type': 'string', 'description': "User's first name"},
                            'last_name': {'type': 'string', 'description': "User's last name"},
                            'primary_email_address': {
                                'type': 'string',
                                'format': 'email',
                                'description': "User's primary email address",
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the user was last updated',
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the user was created',
                            },
                            'disabled': {'type': 'boolean', 'description': 'Whether the user is disabled'},
                            'site_admin': {'type': 'boolean', 'description': 'Whether the user is a site admin'},
                            'emails': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'All user email addresses',
                            },
                            'employee_id': {
                                'type': ['string', 'null'],
                                'description': 'Employee ID',
                            },
                            'linked_candidate_ids': {
                                'type': 'array',
                                'items': {'type': 'integer'},
                                'description': 'IDs of linked candidates',
                            },
                            'offices': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Associated offices',
                            },
                            'departments': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Associated departments',
                            },
                        },
                        'x-airbyte-entity-name': 'users',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse user object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique user identifier'},
                    'name': {'type': 'string', 'description': "User's full name"},
                    'first_name': {'type': 'string', 'description': "User's first name"},
                    'last_name': {'type': 'string', 'description': "User's last name"},
                    'primary_email_address': {
                        'type': 'string',
                        'format': 'email',
                        'description': "User's primary email address",
                    },
                    'updated_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the user was last updated',
                    },
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the user was created',
                    },
                    'disabled': {'type': 'boolean', 'description': 'Whether the user is disabled'},
                    'site_admin': {'type': 'boolean', 'description': 'Whether the user is a site admin'},
                    'emails': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'All user email addresses',
                    },
                    'employee_id': {
                        'type': ['string', 'null'],
                        'description': 'Employee ID',
                    },
                    'linked_candidate_ids': {
                        'type': 'array',
                        'items': {'type': 'integer'},
                        'description': 'IDs of linked candidates',
                    },
                    'offices': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Associated offices',
                    },
                    'departments': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Associated departments',
                    },
                },
                'x-airbyte-entity-name': 'users',
            },
        ),
        EntityDefinition(
            name='departments',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/departments',
                    action=Action.LIST,
                    description='Returns a paginated list of all departments',
                    query_params=['per_page', 'page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse department object',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique department identifier'},
                                'name': {'type': 'string', 'description': 'Department name'},
                                'parent_id': {
                                    'type': ['integer', 'null'],
                                    'description': 'Parent department ID',
                                },
                                'parent_department_external_id': {
                                    'type': ['string', 'null'],
                                    'description': 'Parent department external ID',
                                },
                                'child_ids': {
                                    'type': 'array',
                                    'items': {'type': 'integer'},
                                    'description': 'Child department IDs',
                                },
                                'child_department_external_ids': {
                                    'type': 'array',
                                    'items': {'type': 'string'},
                                    'description': 'Child department external IDs',
                                },
                                'external_id': {
                                    'type': ['string', 'null'],
                                    'description': 'External ID',
                                },
                            },
                            'x-airbyte-entity-name': 'departments',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/departments/{id}',
                    action=Action.GET,
                    description='Get a single department by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Greenhouse department object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique department identifier'},
                            'name': {'type': 'string', 'description': 'Department name'},
                            'parent_id': {
                                'type': ['integer', 'null'],
                                'description': 'Parent department ID',
                            },
                            'parent_department_external_id': {
                                'type': ['string', 'null'],
                                'description': 'Parent department external ID',
                            },
                            'child_ids': {
                                'type': 'array',
                                'items': {'type': 'integer'},
                                'description': 'Child department IDs',
                            },
                            'child_department_external_ids': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Child department external IDs',
                            },
                            'external_id': {
                                'type': ['string', 'null'],
                                'description': 'External ID',
                            },
                        },
                        'x-airbyte-entity-name': 'departments',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse department object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique department identifier'},
                    'name': {'type': 'string', 'description': 'Department name'},
                    'parent_id': {
                        'type': ['integer', 'null'],
                        'description': 'Parent department ID',
                    },
                    'parent_department_external_id': {
                        'type': ['string', 'null'],
                        'description': 'Parent department external ID',
                    },
                    'child_ids': {
                        'type': 'array',
                        'items': {'type': 'integer'},
                        'description': 'Child department IDs',
                    },
                    'child_department_external_ids': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Child department external IDs',
                    },
                    'external_id': {
                        'type': ['string', 'null'],
                        'description': 'External ID',
                    },
                },
                'x-airbyte-entity-name': 'departments',
            },
        ),
        EntityDefinition(
            name='offices',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/offices',
                    action=Action.LIST,
                    description='Returns a paginated list of all offices',
                    query_params=['per_page', 'page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse office object',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique office identifier'},
                                'name': {'type': 'string', 'description': 'Office name'},
                                'location': {
                                    'type': ['object', 'null'],
                                    'description': 'Office location details',
                                },
                                'primary_contact_user_id': {
                                    'type': ['integer', 'null'],
                                    'description': 'Primary contact user ID',
                                },
                                'parent_id': {
                                    'type': ['integer', 'null'],
                                    'description': 'Parent office ID',
                                },
                                'parent_office_external_id': {
                                    'type': ['string', 'null'],
                                    'description': 'Parent office external ID',
                                },
                                'child_ids': {
                                    'type': 'array',
                                    'items': {'type': 'integer'},
                                    'description': 'Child office IDs',
                                },
                                'child_office_external_ids': {
                                    'type': 'array',
                                    'items': {'type': 'string'},
                                    'description': 'Child office external IDs',
                                },
                                'external_id': {
                                    'type': ['string', 'null'],
                                    'description': 'External ID',
                                },
                            },
                            'x-airbyte-entity-name': 'offices',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/offices/{id}',
                    action=Action.GET,
                    description='Get a single office by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Greenhouse office object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique office identifier'},
                            'name': {'type': 'string', 'description': 'Office name'},
                            'location': {
                                'type': ['object', 'null'],
                                'description': 'Office location details',
                            },
                            'primary_contact_user_id': {
                                'type': ['integer', 'null'],
                                'description': 'Primary contact user ID',
                            },
                            'parent_id': {
                                'type': ['integer', 'null'],
                                'description': 'Parent office ID',
                            },
                            'parent_office_external_id': {
                                'type': ['string', 'null'],
                                'description': 'Parent office external ID',
                            },
                            'child_ids': {
                                'type': 'array',
                                'items': {'type': 'integer'},
                                'description': 'Child office IDs',
                            },
                            'child_office_external_ids': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Child office external IDs',
                            },
                            'external_id': {
                                'type': ['string', 'null'],
                                'description': 'External ID',
                            },
                        },
                        'x-airbyte-entity-name': 'offices',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse office object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique office identifier'},
                    'name': {'type': 'string', 'description': 'Office name'},
                    'location': {
                        'type': ['object', 'null'],
                        'description': 'Office location details',
                    },
                    'primary_contact_user_id': {
                        'type': ['integer', 'null'],
                        'description': 'Primary contact user ID',
                    },
                    'parent_id': {
                        'type': ['integer', 'null'],
                        'description': 'Parent office ID',
                    },
                    'parent_office_external_id': {
                        'type': ['string', 'null'],
                        'description': 'Parent office external ID',
                    },
                    'child_ids': {
                        'type': 'array',
                        'items': {'type': 'integer'},
                        'description': 'Child office IDs',
                    },
                    'child_office_external_ids': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Child office external IDs',
                    },
                    'external_id': {
                        'type': ['string', 'null'],
                        'description': 'External ID',
                    },
                },
                'x-airbyte-entity-name': 'offices',
            },
        ),
        EntityDefinition(
            name='job_posts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/job_posts',
                    action=Action.LIST,
                    description='Returns a paginated list of all job posts',
                    query_params=[
                        'per_page',
                        'page',
                        'live',
                        'active',
                    ],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'live': {'type': 'boolean', 'required': False},
                        'active': {'type': 'boolean', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse job post object',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique job post identifier'},
                                'title': {'type': 'string', 'description': 'Job post title'},
                                'location': {
                                    'type': ['object', 'null'],
                                    'description': 'Job post location',
                                },
                                'internal': {'type': 'boolean', 'description': 'Whether this is an internal job post'},
                                'external': {'type': 'boolean', 'description': 'Whether this is an external job post'},
                                'active': {'type': 'boolean', 'description': 'Whether the job post is active'},
                                'live': {'type': 'boolean', 'description': 'Whether the job post is live'},
                                'first_published_at': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'When the job post was first published',
                                },
                                'job_id': {'type': 'integer', 'description': 'Associated job ID'},
                                'content': {
                                    'type': ['string', 'null'],
                                    'description': 'Job post content/description',
                                },
                                'internal_content': {
                                    'type': ['string', 'null'],
                                    'description': 'Internal job post content',
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the job post was last updated',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the job post was created',
                                },
                                'demographic_question_set_id': {
                                    'type': ['integer', 'null'],
                                    'description': 'Demographic question set ID',
                                },
                                'questions': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'Application questions',
                                },
                            },
                            'x-airbyte-entity-name': 'job_posts',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/job_posts/{id}',
                    action=Action.GET,
                    description='Get a single job post by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Greenhouse job post object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique job post identifier'},
                            'title': {'type': 'string', 'description': 'Job post title'},
                            'location': {
                                'type': ['object', 'null'],
                                'description': 'Job post location',
                            },
                            'internal': {'type': 'boolean', 'description': 'Whether this is an internal job post'},
                            'external': {'type': 'boolean', 'description': 'Whether this is an external job post'},
                            'active': {'type': 'boolean', 'description': 'Whether the job post is active'},
                            'live': {'type': 'boolean', 'description': 'Whether the job post is live'},
                            'first_published_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'When the job post was first published',
                            },
                            'job_id': {'type': 'integer', 'description': 'Associated job ID'},
                            'content': {
                                'type': ['string', 'null'],
                                'description': 'Job post content/description',
                            },
                            'internal_content': {
                                'type': ['string', 'null'],
                                'description': 'Internal job post content',
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the job post was last updated',
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the job post was created',
                            },
                            'demographic_question_set_id': {
                                'type': ['integer', 'null'],
                                'description': 'Demographic question set ID',
                            },
                            'questions': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Application questions',
                            },
                        },
                        'x-airbyte-entity-name': 'job_posts',
                    },
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse job post object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique job post identifier'},
                    'title': {'type': 'string', 'description': 'Job post title'},
                    'location': {
                        'type': ['object', 'null'],
                        'description': 'Job post location',
                    },
                    'internal': {'type': 'boolean', 'description': 'Whether this is an internal job post'},
                    'external': {'type': 'boolean', 'description': 'Whether this is an external job post'},
                    'active': {'type': 'boolean', 'description': 'Whether the job post is active'},
                    'live': {'type': 'boolean', 'description': 'Whether the job post is live'},
                    'first_published_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'When the job post was first published',
                    },
                    'job_id': {'type': 'integer', 'description': 'Associated job ID'},
                    'content': {
                        'type': ['string', 'null'],
                        'description': 'Job post content/description',
                    },
                    'internal_content': {
                        'type': ['string', 'null'],
                        'description': 'Internal job post content',
                    },
                    'updated_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the job post was last updated',
                    },
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the job post was created',
                    },
                    'demographic_question_set_id': {
                        'type': ['integer', 'null'],
                        'description': 'Demographic question set ID',
                    },
                    'questions': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'Application questions',
                    },
                },
                'x-airbyte-entity-name': 'job_posts',
            },
        ),
        EntityDefinition(
            name='sources',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/sources',
                    action=Action.LIST,
                    description='Returns a paginated list of all sources',
                    query_params=['per_page', 'page'],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse source object',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique source identifier'},
                                'name': {'type': 'string', 'description': 'Source name'},
                                'type': {
                                    'type': ['object', 'null'],
                                    'description': 'Source type information',
                                },
                            },
                            'x-airbyte-entity-name': 'sources',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse source object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique source identifier'},
                    'name': {'type': 'string', 'description': 'Source name'},
                    'type': {
                        'type': ['object', 'null'],
                        'description': 'Source type information',
                    },
                },
                'x-airbyte-entity-name': 'sources',
            },
        ),
        EntityDefinition(
            name='scheduled_interviews',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/scheduled_interviews',
                    action=Action.LIST,
                    description='Returns a paginated list of all scheduled interviews',
                    query_params=[
                        'per_page',
                        'page',
                        'created_before',
                        'created_after',
                        'updated_before',
                        'updated_after',
                        'starts_after',
                        'ends_before',
                    ],
                    query_params_schema={
                        'per_page': {
                            'type': 'integer',
                            'required': False,
                            'default': 100,
                        },
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'created_before': {'type': 'string', 'required': False},
                        'created_after': {'type': 'string', 'required': False},
                        'updated_before': {'type': 'string', 'required': False},
                        'updated_after': {'type': 'string', 'required': False},
                        'starts_after': {'type': 'string', 'required': False},
                        'ends_before': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Greenhouse scheduled interview object',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique scheduled interview identifier'},
                                'application_id': {'type': 'integer', 'description': 'Associated application ID'},
                                'external_event_id': {
                                    'type': ['string', 'null'],
                                    'description': 'External calendar event ID',
                                },
                                'created_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the interview was created',
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'format': 'date-time',
                                    'description': 'When the interview was last updated',
                                },
                                'start': {
                                    'type': ['object', 'null'],
                                    'description': 'Interview start time details',
                                },
                                'end': {
                                    'type': ['object', 'null'],
                                    'description': 'Interview end time details',
                                },
                                'location': {
                                    'type': ['string', 'null'],
                                    'description': 'Interview location',
                                },
                                'video_conferencing_url': {
                                    'type': ['string', 'null'],
                                    'description': 'Video conferencing URL',
                                },
                                'status': {'type': 'string', 'description': 'Interview status'},
                                'interview': {
                                    'type': ['object', 'null'],
                                    'description': 'Interview details',
                                },
                                'organizer': {
                                    'type': ['object', 'null'],
                                    'description': 'Interview organizer',
                                },
                                'interviewers': {
                                    'type': 'array',
                                    'items': {'type': 'object'},
                                    'description': 'List of interviewers',
                                },
                            },
                            'x-airbyte-entity-name': 'scheduled_interviews',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/scheduled_interviews/{id}',
                    action=Action.GET,
                    description='Get a single scheduled interview by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Greenhouse scheduled interview object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique scheduled interview identifier'},
                            'application_id': {'type': 'integer', 'description': 'Associated application ID'},
                            'external_event_id': {
                                'type': ['string', 'null'],
                                'description': 'External calendar event ID',
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the interview was created',
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the interview was last updated',
                            },
                            'start': {
                                'type': ['object', 'null'],
                                'description': 'Interview start time details',
                            },
                            'end': {
                                'type': ['object', 'null'],
                                'description': 'Interview end time details',
                            },
                            'location': {
                                'type': ['string', 'null'],
                                'description': 'Interview location',
                            },
                            'video_conferencing_url': {
                                'type': ['string', 'null'],
                                'description': 'Video conferencing URL',
                            },
                            'status': {'type': 'string', 'description': 'Interview status'},
                            'interview': {
                                'type': ['object', 'null'],
                                'description': 'Interview details',
                            },
                            'organizer': {
                                'type': ['object', 'null'],
                                'description': 'Interview organizer',
                            },
                            'interviewers': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'List of interviewers',
                            },
                        },
                        'x-airbyte-entity-name': 'scheduled_interviews',
                    },
                    untested=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Greenhouse scheduled interview object',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique scheduled interview identifier'},
                    'application_id': {'type': 'integer', 'description': 'Associated application ID'},
                    'external_event_id': {
                        'type': ['string', 'null'],
                        'description': 'External calendar event ID',
                    },
                    'created_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the interview was created',
                    },
                    'updated_at': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'When the interview was last updated',
                    },
                    'start': {
                        'type': ['object', 'null'],
                        'description': 'Interview start time details',
                    },
                    'end': {
                        'type': ['object', 'null'],
                        'description': 'Interview end time details',
                    },
                    'location': {
                        'type': ['string', 'null'],
                        'description': 'Interview location',
                    },
                    'video_conferencing_url': {
                        'type': ['string', 'null'],
                        'description': 'Video conferencing URL',
                    },
                    'status': {'type': 'string', 'description': 'Interview status'},
                    'interview': {
                        'type': ['object', 'null'],
                        'description': 'Interview details',
                    },
                    'organizer': {
                        'type': ['object', 'null'],
                        'description': 'Interview organizer',
                    },
                    'interviewers': {
                        'type': 'array',
                        'items': {'type': 'object'},
                        'description': 'List of interviewers',
                    },
                },
                'x-airbyte-entity-name': 'scheduled_interviews',
            },
        ),
        EntityDefinition(
            name='application_attachment',
            actions=[Action.DOWNLOAD],
            endpoints={
                Action.DOWNLOAD: EndpointDefinition(
                    method='GET',
                    path='/applications/{id}/attachment:download/{attachment_index}',
                    path_override=PathOverrideConfig(
                        path='/applications/{id}',
                    ),
                    action=Action.DOWNLOAD,
                    description='Downloads an attachment (resume, cover letter, etc.) for an application by index.\nThe attachment URL is a temporary signed AWS S3 URL that expires within 7 days.\nFiles should be downloaded immediately after retrieval.\n',
                    path_params=['id', 'attachment_index'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                        'attachment_index': {
                            'type': 'integer',
                            'required': True,
                            'default': 0,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Greenhouse application object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique application identifier'},
                            'candidate_id': {'type': 'integer', 'description': 'ID of the associated candidate'},
                            'prospect': {'type': 'boolean', 'description': 'Whether this is a prospect application'},
                            'applied_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the application was submitted',
                            },
                            'rejected_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'When the application was rejected',
                            },
                            'last_activity_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the last activity occurred',
                            },
                            'location': {
                                'type': ['object', 'null'],
                                'description': 'Application location',
                            },
                            'source': {'type': 'object', 'description': 'Application source'},
                            'credited_to': {'type': 'object', 'description': 'User credited with the application'},
                            'rejection_reason': {
                                'type': ['object', 'null'],
                                'description': 'Rejection reason if rejected',
                            },
                            'rejection_details': {
                                'type': ['object', 'null'],
                                'description': 'Additional rejection details',
                            },
                            'jobs': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Jobs associated with the application',
                            },
                            'job_post_id': {
                                'type': ['integer', 'null'],
                                'description': 'ID of the job post',
                            },
                            'status': {'type': 'string', 'description': 'Application status'},
                            'current_stage': {
                                'type': ['object', 'null'],
                                'description': 'Current stage of the application',
                            },
                            'answers': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Application question answers',
                            },
                            'prospective_office': {
                                'type': ['object', 'null'],
                                'description': 'Prospective office',
                            },
                            'prospective_department': {
                                'type': ['object', 'null'],
                                'description': 'Prospective department',
                            },
                            'prospect_detail': {'type': 'object', 'description': 'Prospect details'},
                            'attachments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'File attachment (resume, cover letter, etc.)',
                                    'properties': {
                                        'filename': {'type': 'string', 'description': 'Name of the attached file'},
                                        'url': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'Temporary signed AWS S3 URL to download the file.\nThis URL expires within 7 days - download immediately after retrieval.\n',
                                        },
                                        'type': {
                                            'type': 'string',
                                            'enum': [
                                                'resume',
                                                'cover_letter',
                                                'admin_only',
                                                'take_home_test',
                                                'offer_packet',
                                                'offer_letter',
                                                'signed_offer_letter',
                                                'other',
                                            ],
                                            'description': 'Type of attachment',
                                        },
                                        'created_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When the attachment was uploaded',
                                        },
                                    },
                                },
                                'description': 'Application attachments (resumes, cover letters, etc.)',
                            },
                            'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                        },
                        'x-airbyte-entity-name': 'applications',
                    },
                    file_field='attachments[{attachment_index}].url',
                ),
            },
        ),
        EntityDefinition(
            name='candidate_attachment',
            actions=[Action.DOWNLOAD],
            endpoints={
                Action.DOWNLOAD: EndpointDefinition(
                    method='GET',
                    path='/candidates/{id}/attachment:download/{attachment_index}',
                    path_override=PathOverrideConfig(
                        path='/candidates/{id}',
                    ),
                    action=Action.DOWNLOAD,
                    description='Downloads an attachment (resume, cover letter, etc.) for a candidate by index.\nThe attachment URL is a temporary signed AWS S3 URL that expires within 7 days.\nFiles should be downloaded immediately after retrieval.\n',
                    path_params=['id', 'attachment_index'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                        'attachment_index': {
                            'type': 'integer',
                            'required': True,
                            'default': 0,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Greenhouse candidate object',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique candidate identifier'},
                            'first_name': {'type': 'string', 'description': "Candidate's first name"},
                            'last_name': {'type': 'string', 'description': "Candidate's last name"},
                            'company': {
                                'type': ['string', 'null'],
                                'description': "Candidate's current company",
                            },
                            'title': {
                                'type': ['string', 'null'],
                                'description': "Candidate's current title",
                            },
                            'created_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the candidate was created',
                            },
                            'updated_at': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the candidate was last updated',
                            },
                            'last_activity': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'When the last activity occurred',
                            },
                            'is_private': {'type': 'boolean', 'description': 'Whether the candidate is private'},
                            'photo_url': {
                                'type': ['string', 'null'],
                                'description': "URL to candidate's photo",
                            },
                            'attachments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'File attachment (resume, cover letter, etc.)',
                                    'properties': {
                                        'filename': {'type': 'string', 'description': 'Name of the attached file'},
                                        'url': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'Temporary signed AWS S3 URL to download the file.\nThis URL expires within 7 days - download immediately after retrieval.\n',
                                        },
                                        'type': {
                                            'type': 'string',
                                            'enum': [
                                                'resume',
                                                'cover_letter',
                                                'admin_only',
                                                'take_home_test',
                                                'offer_packet',
                                                'offer_letter',
                                                'signed_offer_letter',
                                                'other',
                                            ],
                                            'description': 'Type of attachment',
                                        },
                                        'created_at': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'When the attachment was uploaded',
                                        },
                                    },
                                },
                                'description': 'Candidate attachments (resumes, cover letters, etc.)',
                            },
                            'application_ids': {
                                'type': 'array',
                                'items': {'type': 'integer'},
                                'description': "IDs of candidate's applications",
                            },
                            'phone_numbers': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Candidate phone numbers',
                            },
                            'addresses': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Candidate addresses',
                            },
                            'email_addresses': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Candidate email addresses',
                            },
                            'website_addresses': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Candidate website addresses',
                            },
                            'social_media_addresses': {
                                'type': 'array',
                                'items': {'type': 'object'},
                                'description': 'Candidate social media addresses',
                            },
                            'recruiter': {
                                'type': ['object', 'null'],
                                'description': 'Recruiter information',
                            },
                            'coordinator': {
                                'type': ['object', 'null'],
                                'description': 'Coordinator information',
                            },
                            'can_email': {'type': 'boolean', 'description': 'Whether the candidate can be emailed'},
                            'tags': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'Candidate tags',
                            },
                            'custom_fields': {'type': 'object', 'description': 'Custom field values'},
                        },
                        'x-airbyte-entity-name': 'candidates',
                    },
                    file_field='attachments[{attachment_index}].url',
                ),
            },
        ),
    ],
)