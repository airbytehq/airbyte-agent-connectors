"""
Connector model for commonroom.

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

CommonroomConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('152171eb-bedf-46d7-b2c9-c8a91b9fd5b4'),
    name='commonroom',
    version='0.1.0',
    base_url='https://api.commonroom.io/community/v1',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AirbyteAuthConfig(
            title='API Token Authentication',
            type='object',
            required=['api_token'],
            properties={
                'api_token': AuthConfigFieldSpec(
                    title='API Token',
                    description='API token for authenticating with CommonRoom API. Create a token at https://app.commonroom.io/ under Settings | API tokens.',
                    airbyte_secret=True,
                ),
            },
            auth_mapping={'token': '${api_token}'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='api_token_status',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/api-token-status',
                    action=Action.LIST,
                    description='Returns the status and metadata of the current API token',
                    response_schema={
                        'type': 'object',
                        'description': 'API token status information',
                        'properties': {
                            'jti': {
                                'type': ['string', 'null'],
                                'description': 'JWT ID - unique identifier for the token',
                            },
                            'iat': {
                                'type': ['integer', 'null'],
                                'description': 'Issued at timestamp',
                            },
                            'exp': {
                                'type': ['integer', 'null'],
                                'description': 'Expiration timestamp',
                            },
                            'sub': {
                                'type': ['string', 'null'],
                                'description': 'Subject (user/service identifier)',
                            },
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='contact_custom_fields',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/members/customFields',
                    action=Action.LIST,
                    description='Returns all custom fields defined for contacts/members',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Custom field definition for contacts',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique identifier for the custom field'},
                                'type': {
                                    'type': ['string', 'null'],
                                    'description': 'Field type (e.g., text, number, date)',
                                },
                                'name': {
                                    'type': ['string', 'null'],
                                    'description': 'Display name of the field',
                                },
                                'values': {
                                    'type': ['array', 'null'],
                                    'items': {'type': 'string'},
                                    'description': 'Possible values for enum-type fields',
                                },
                                'multivalue': {
                                    'type': ['boolean', 'null'],
                                    'description': 'Whether the field accepts multiple values',
                                },
                            },
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='activity_types',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/activityTypes',
                    action=Action.LIST,
                    description='Returns all activity types in the community',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Activity type definition',
                            'properties': {
                                'id': {'type': 'string', 'description': 'Unique identifier for the activity type'},
                                'displayName': {
                                    'type': ['string', 'null'],
                                    'description': 'Display name of the activity type',
                                },
                            },
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='segments',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/segments',
                    action=Action.LIST,
                    description='Returns all segments in the community',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'Segment definition',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique identifier for the segment'},
                                'name': {
                                    'type': ['string', 'null'],
                                    'description': 'Name of the segment',
                                },
                            },
                        },
                    },
                ),
            },
        ),
        EntityDefinition(
            name='tags',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/tags',
                    action=Action.LIST,
                    description='Returns all tags in the community',
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'labels': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Tag definition',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'Unique identifier for the tag'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'Name of the tag',
                                        },
                                        'description': {
                                            'type': ['string', 'null'],
                                            'description': 'Description of the tag',
                                        },
                                        'createdAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'When the tag was created',
                                        },
                                        'deletedAt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'When the tag was deleted (if applicable)',
                                        },
                                        'entityTypes': {
                                            'type': ['array', 'null'],
                                            'items': {'type': 'string'},
                                            'description': 'Entity types this tag can be applied to',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.labels',
                ),
            },
        ),
    ],
)