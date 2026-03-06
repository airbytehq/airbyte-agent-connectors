"""
Connector model for typeform.

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

TypeformConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('e7eff203-90bf-43e5-a240-19ea3056c474'),
    name='typeform',
    version='1.0.1',
    base_url='https://api.typeform.com',
    auth=AuthConfig(
        type=AuthType.BEARER,
        config={'header': 'Authorization', 'prefix': 'Bearer'},
        user_config_spec=AirbyteAuthConfig(
            title='Access Token Authentication',
            type='object',
            required=['access_token'],
            properties={
                'access_token': AuthConfigFieldSpec(
                    title='Access Token',
                    description='Personal access token from your Typeform account settings',
                ),
            },
            auth_mapping={'token': '${access_token}'},
            replication_auth_key_mapping={'credentials.access_token': 'access_token'},
            replication_auth_key_constants={'credentials.auth_type': 'access_token'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='forms',
            stream_name='forms',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/forms',
                    action=Action.LIST,
                    description='Returns a paginated list of forms in the account',
                    query_params=['page', 'page_size'],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of forms',
                        'properties': {
                            'total_items': {
                                'type': ['null', 'integer'],
                                'description': 'Total number of forms',
                            },
                            'page_count': {
                                'type': ['null', 'integer'],
                                'description': 'Total number of pages',
                            },
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A Typeform form with its fields, settings, and logic',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique identifier of the form',
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                            'description': 'Type of the form',
                                        },
                                        'title': {
                                            'type': ['null', 'string'],
                                            'description': 'Title of the form',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Date and time when the form was created',
                                        },
                                        'last_updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Date and time when the form was last updated',
                                        },
                                        'published_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Date and time when the form was published',
                                        },
                                        'workspace': {
                                            'type': ['null', 'object'],
                                            'description': 'Workspace details where the form belongs',
                                            'properties': {
                                                'href': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL of the workspace',
                                                },
                                            },
                                        },
                                        'theme': {
                                            'type': ['null', 'object'],
                                            'description': 'Theme settings for the form',
                                            'properties': {
                                                'href': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL of the theme',
                                                },
                                            },
                                        },
                                        'settings': {
                                            'type': ['null', 'object'],
                                            'description': 'Settings and configurations for the form',
                                            'properties': {
                                                'language': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Language of the form',
                                                },
                                                'progress_bar': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Progress bar settings',
                                                },
                                                'meta': {
                                                    'type': ['null', 'object'],
                                                    'description': 'Meta information',
                                                    'properties': {
                                                        'allow_indexing': {
                                                            'type': ['null', 'boolean'],
                                                        },
                                                        'title': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'description': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'image': {
                                                            'type': ['null', 'object'],
                                                            'properties': {
                                                                'href': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'hide_navigation': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'is_public': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'is_trial': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'show_progress_bar': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'show_typeform_branding': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'are_uploads_public': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'show_time_to_complete': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'redirect_after_submit_url': {
                                                    'type': ['null', 'string'],
                                                },
                                                'google_analytics': {
                                                    'type': ['null', 'string'],
                                                },
                                                'facebook_pixel': {
                                                    'type': ['null', 'string'],
                                                },
                                                'google_tag_manager': {
                                                    'type': ['null', 'string'],
                                                },
                                                'capabilities': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'e2e_encryption': {
                                                            'type': ['null', 'object'],
                                                            'properties': {
                                                                'enabled': {
                                                                    'type': ['null', 'boolean'],
                                                                },
                                                                'modifiable': {
                                                                    'type': ['null', 'boolean'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'notifications': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'self': {
                                                            'type': ['null', 'object'],
                                                            'properties': {
                                                                'enabled': {
                                                                    'type': ['null', 'boolean'],
                                                                },
                                                                'recipients': {
                                                                    'type': ['null', 'array'],
                                                                    'items': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                },
                                                                'subject': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'message': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'reply_to': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                            },
                                                        },
                                                        'respondent': {
                                                            'type': ['null', 'object'],
                                                            'properties': {
                                                                'enabled': {
                                                                    'type': ['null', 'boolean'],
                                                                },
                                                                'recipients': {
                                                                    'type': ['null', 'array'],
                                                                    'items': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                },
                                                                'subject': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'message': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'reply_to': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                                'cui_settings': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'avatar': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'is_typing_emulation_disabled': {
                                                            'type': ['null', 'boolean'],
                                                        },
                                                        'typing_emulation_speed': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'welcome_screens': {
                                            'type': ['null', 'array'],
                                            'description': 'Welcome screen configurations',
                                            'items': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'ref': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'title': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'properties': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'show_button': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'share_icons': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'button_mode': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'button_text': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'redirect_url': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                    'attachment': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'placement': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                    'layout': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'placement': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'attachment': {
                                                                'type': ['null', 'object'],
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                    'href': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                    'scale': {
                                                                        'type': ['null', 'number'],
                                                                    },
                                                                },
                                                            },
                                                            'properties': {
                                                                'type': ['null', 'object'],
                                                                'properties': {
                                                                    'brightness': {
                                                                        'type': ['null', 'number'],
                                                                    },
                                                                    'description': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                    'focal_point': {
                                                                        'type': ['null', 'object'],
                                                                        'properties': {
                                                                            'x': {
                                                                                'type': ['null', 'number'],
                                                                            },
                                                                            'y': {
                                                                                'type': ['null', 'number'],
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'thankyou_screens': {
                                            'type': ['null', 'array'],
                                            'description': 'Thank you screen configurations',
                                            'items': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'ref': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'title': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'properties': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'show_button': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'share_icons': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'button_mode': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'button_text': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'redirect_url': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                    'attachment': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'placement': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                    'layout': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'placement': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'attachment': {
                                                                'type': ['null', 'object'],
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                    'href': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                    'scale': {
                                                                        'type': ['null', 'number'],
                                                                    },
                                                                },
                                                            },
                                                            'properties': {
                                                                'type': ['null', 'object'],
                                                                'properties': {
                                                                    'brightness': {
                                                                        'type': ['null', 'number'],
                                                                    },
                                                                    'description': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                    'focal_point': {
                                                                        'type': ['null', 'object'],
                                                                        'properties': {
                                                                            'x': {
                                                                                'type': ['null', 'number'],
                                                                            },
                                                                            'y': {
                                                                                'type': ['null', 'number'],
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'logic': {
                                            'type': ['null', 'array'],
                                            'description': 'Logic rules applied to form fields',
                                            'items': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'type': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'ref': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'actions': {
                                                        'type': ['null', 'array'],
                                                        'items': {
                                                            'type': ['null', 'object'],
                                                            'properties': {
                                                                'action': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                                'details': {
                                                                    'type': ['null', 'object'],
                                                                    'properties': {
                                                                        'to': {
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
                                                                        'target': {
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
                                                                        'value': {
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
                                                                'condition': {
                                                                    'type': ['null', 'object'],
                                                                    'properties': {
                                                                        'op': {
                                                                            'type': ['null', 'string'],
                                                                        },
                                                                        'vars': {
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
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'fields': {
                                            'type': ['null', 'array'],
                                            'description': 'List of fields within the form',
                                            'items': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'title': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'ref': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'type': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'properties': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'randomize': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'allow_multiple_selection': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'allow_other_choice': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'vertical_alignment': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                            'choices': {
                                                                'type': ['null', 'array'],
                                                                'items': {
                                                                    'type': ['null', 'object'],
                                                                    'properties': {
                                                                        'id': {
                                                                            'type': ['null', 'string'],
                                                                        },
                                                                        'ref': {
                                                                            'type': ['null', 'string'],
                                                                        },
                                                                        'label': {
                                                                            'type': ['null', 'string'],
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                    'validations': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'required': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                        },
                                                    },
                                                    'attachment': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'href': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                    'layout': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'placement': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'attachment': {
                                                                'type': ['null', 'object'],
                                                                'properties': {
                                                                    'type': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                    'href': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                    'scale': {
                                                                        'type': ['null', 'number'],
                                                                    },
                                                                },
                                                            },
                                                            'properties': {
                                                                'type': ['null', 'object'],
                                                                'properties': {
                                                                    'brightness': {
                                                                        'type': ['null', 'number'],
                                                                    },
                                                                    'description': {
                                                                        'type': ['null', 'string'],
                                                                    },
                                                                    'focal_point': {
                                                                        'type': ['null', 'object'],
                                                                        'properties': {
                                                                            'x': {
                                                                                'type': ['null', 'number'],
                                                                            },
                                                                            'y': {
                                                                                'type': ['null', 'number'],
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'self': {
                                            'type': ['null', 'object'],
                                            'description': 'Self-referential link to this form',
                                            'properties': {
                                                'href': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL of this form resource',
                                                },
                                            },
                                        },
                                        '_links': {
                                            'type': ['null', 'object'],
                                            'description': 'Links to related resources',
                                            'properties': {
                                                'display': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'forms',
                                    'x-airbyte-stream-name': 'forms',
                                },
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'total_items': '$.total_items', 'page_count': '$.page_count'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/forms/{form_id}',
                    action=Action.GET,
                    description='Retrieves a single form by its ID, including fields, settings, and logic',
                    path_params=['form_id'],
                    path_params_schema={
                        'form_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Typeform form with its fields, settings, and logic',
                        'properties': {
                            'id': {
                                'type': ['null', 'string'],
                                'description': 'Unique identifier of the form',
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'Type of the form',
                            },
                            'title': {
                                'type': ['null', 'string'],
                                'description': 'Title of the form',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Date and time when the form was created',
                            },
                            'last_updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Date and time when the form was last updated',
                            },
                            'published_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Date and time when the form was published',
                            },
                            'workspace': {
                                'type': ['null', 'object'],
                                'description': 'Workspace details where the form belongs',
                                'properties': {
                                    'href': {
                                        'type': ['null', 'string'],
                                        'description': 'URL of the workspace',
                                    },
                                },
                            },
                            'theme': {
                                'type': ['null', 'object'],
                                'description': 'Theme settings for the form',
                                'properties': {
                                    'href': {
                                        'type': ['null', 'string'],
                                        'description': 'URL of the theme',
                                    },
                                },
                            },
                            'settings': {
                                'type': ['null', 'object'],
                                'description': 'Settings and configurations for the form',
                                'properties': {
                                    'language': {
                                        'type': ['null', 'string'],
                                        'description': 'Language of the form',
                                    },
                                    'progress_bar': {
                                        'type': ['null', 'string'],
                                        'description': 'Progress bar settings',
                                    },
                                    'meta': {
                                        'type': ['null', 'object'],
                                        'description': 'Meta information',
                                        'properties': {
                                            'allow_indexing': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'title': {
                                                'type': ['null', 'string'],
                                            },
                                            'description': {
                                                'type': ['null', 'string'],
                                            },
                                            'image': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'href': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'hide_navigation': {
                                        'type': ['null', 'boolean'],
                                    },
                                    'is_public': {
                                        'type': ['null', 'boolean'],
                                    },
                                    'is_trial': {
                                        'type': ['null', 'boolean'],
                                    },
                                    'show_progress_bar': {
                                        'type': ['null', 'boolean'],
                                    },
                                    'show_typeform_branding': {
                                        'type': ['null', 'boolean'],
                                    },
                                    'are_uploads_public': {
                                        'type': ['null', 'boolean'],
                                    },
                                    'show_time_to_complete': {
                                        'type': ['null', 'boolean'],
                                    },
                                    'redirect_after_submit_url': {
                                        'type': ['null', 'string'],
                                    },
                                    'google_analytics': {
                                        'type': ['null', 'string'],
                                    },
                                    'facebook_pixel': {
                                        'type': ['null', 'string'],
                                    },
                                    'google_tag_manager': {
                                        'type': ['null', 'string'],
                                    },
                                    'capabilities': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'e2e_encryption': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'enabled': {
                                                        'type': ['null', 'boolean'],
                                                    },
                                                    'modifiable': {
                                                        'type': ['null', 'boolean'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'notifications': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'self': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'enabled': {
                                                        'type': ['null', 'boolean'],
                                                    },
                                                    'recipients': {
                                                        'type': ['null', 'array'],
                                                        'items': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                    'subject': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'message': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'reply_to': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                            'respondent': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'enabled': {
                                                        'type': ['null', 'boolean'],
                                                    },
                                                    'recipients': {
                                                        'type': ['null', 'array'],
                                                        'items': {
                                                            'type': ['null', 'string'],
                                                        },
                                                    },
                                                    'subject': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'message': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'reply_to': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'cui_settings': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'avatar': {
                                                'type': ['null', 'string'],
                                            },
                                            'is_typing_emulation_disabled': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'typing_emulation_speed': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                            },
                            'welcome_screens': {
                                'type': ['null', 'array'],
                                'description': 'Welcome screen configurations',
                                'items': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'ref': {
                                            'type': ['null', 'string'],
                                        },
                                        'title': {
                                            'type': ['null', 'string'],
                                        },
                                        'properties': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'show_button': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'share_icons': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'button_mode': {
                                                    'type': ['null', 'string'],
                                                },
                                                'button_text': {
                                                    'type': ['null', 'string'],
                                                },
                                                'redirect_url': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'attachment': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'type': {
                                                    'type': ['null', 'string'],
                                                },
                                                'placement': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'layout': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'type': {
                                                    'type': ['null', 'string'],
                                                },
                                                'placement': {
                                                    'type': ['null', 'string'],
                                                },
                                                'attachment': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'type': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'href': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'scale': {
                                                            'type': ['null', 'number'],
                                                        },
                                                    },
                                                },
                                                'properties': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'brightness': {
                                                            'type': ['null', 'number'],
                                                        },
                                                        'description': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'focal_point': {
                                                            'type': ['null', 'object'],
                                                            'properties': {
                                                                'x': {
                                                                    'type': ['null', 'number'],
                                                                },
                                                                'y': {
                                                                    'type': ['null', 'number'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'thankyou_screens': {
                                'type': ['null', 'array'],
                                'description': 'Thank you screen configurations',
                                'items': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'ref': {
                                            'type': ['null', 'string'],
                                        },
                                        'title': {
                                            'type': ['null', 'string'],
                                        },
                                        'properties': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'show_button': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'share_icons': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'button_mode': {
                                                    'type': ['null', 'string'],
                                                },
                                                'button_text': {
                                                    'type': ['null', 'string'],
                                                },
                                                'redirect_url': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'attachment': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'type': {
                                                    'type': ['null', 'string'],
                                                },
                                                'placement': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'layout': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'type': {
                                                    'type': ['null', 'string'],
                                                },
                                                'placement': {
                                                    'type': ['null', 'string'],
                                                },
                                                'attachment': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'type': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'href': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'scale': {
                                                            'type': ['null', 'number'],
                                                        },
                                                    },
                                                },
                                                'properties': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'brightness': {
                                                            'type': ['null', 'number'],
                                                        },
                                                        'description': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'focal_point': {
                                                            'type': ['null', 'object'],
                                                            'properties': {
                                                                'x': {
                                                                    'type': ['null', 'number'],
                                                                },
                                                                'y': {
                                                                    'type': ['null', 'number'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'logic': {
                                'type': ['null', 'array'],
                                'description': 'Logic rules applied to form fields',
                                'items': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'type': {
                                            'type': ['null', 'string'],
                                        },
                                        'ref': {
                                            'type': ['null', 'string'],
                                        },
                                        'actions': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'action': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'details': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'to': {
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
                                                            'target': {
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
                                                            'value': {
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
                                                    'condition': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'op': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'vars': {
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
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'fields': {
                                'type': ['null', 'array'],
                                'description': 'List of fields within the form',
                                'items': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'title': {
                                            'type': ['null', 'string'],
                                        },
                                        'ref': {
                                            'type': ['null', 'string'],
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                        },
                                        'properties': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'randomize': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'allow_multiple_selection': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'allow_other_choice': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'vertical_alignment': {
                                                    'type': ['null', 'boolean'],
                                                },
                                                'choices': {
                                                    'type': ['null', 'array'],
                                                    'items': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'ref': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'label': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'validations': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'required': {
                                                    'type': ['null', 'boolean'],
                                                },
                                            },
                                        },
                                        'attachment': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'type': {
                                                    'type': ['null', 'string'],
                                                },
                                                'href': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'layout': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'type': {
                                                    'type': ['null', 'string'],
                                                },
                                                'placement': {
                                                    'type': ['null', 'string'],
                                                },
                                                'attachment': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'type': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'href': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'scale': {
                                                            'type': ['null', 'number'],
                                                        },
                                                    },
                                                },
                                                'properties': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'brightness': {
                                                            'type': ['null', 'number'],
                                                        },
                                                        'description': {
                                                            'type': ['null', 'string'],
                                                        },
                                                        'focal_point': {
                                                            'type': ['null', 'object'],
                                                            'properties': {
                                                                'x': {
                                                                    'type': ['null', 'number'],
                                                                },
                                                                'y': {
                                                                    'type': ['null', 'number'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                            'self': {
                                'type': ['null', 'object'],
                                'description': 'Self-referential link to this form',
                                'properties': {
                                    'href': {
                                        'type': ['null', 'string'],
                                        'description': 'URL of this form resource',
                                    },
                                },
                            },
                            '_links': {
                                'type': ['null', 'object'],
                                'description': 'Links to related resources',
                                'properties': {
                                    'display': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'forms',
                        'x-airbyte-stream-name': 'forms',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Typeform form with its fields, settings, and logic',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier of the form',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Type of the form',
                    },
                    'title': {
                        'type': ['null', 'string'],
                        'description': 'Title of the form',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Date and time when the form was created',
                    },
                    'last_updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Date and time when the form was last updated',
                    },
                    'published_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Date and time when the form was published',
                    },
                    'workspace': {
                        'type': ['null', 'object'],
                        'description': 'Workspace details where the form belongs',
                        'properties': {
                            'href': {
                                'type': ['null', 'string'],
                                'description': 'URL of the workspace',
                            },
                        },
                    },
                    'theme': {
                        'type': ['null', 'object'],
                        'description': 'Theme settings for the form',
                        'properties': {
                            'href': {
                                'type': ['null', 'string'],
                                'description': 'URL of the theme',
                            },
                        },
                    },
                    'settings': {
                        'type': ['null', 'object'],
                        'description': 'Settings and configurations for the form',
                        'properties': {
                            'language': {
                                'type': ['null', 'string'],
                                'description': 'Language of the form',
                            },
                            'progress_bar': {
                                'type': ['null', 'string'],
                                'description': 'Progress bar settings',
                            },
                            'meta': {
                                'type': ['null', 'object'],
                                'description': 'Meta information',
                                'properties': {
                                    'allow_indexing': {
                                        'type': ['null', 'boolean'],
                                    },
                                    'title': {
                                        'type': ['null', 'string'],
                                    },
                                    'description': {
                                        'type': ['null', 'string'],
                                    },
                                    'image': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'href': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                            },
                            'hide_navigation': {
                                'type': ['null', 'boolean'],
                            },
                            'is_public': {
                                'type': ['null', 'boolean'],
                            },
                            'is_trial': {
                                'type': ['null', 'boolean'],
                            },
                            'show_progress_bar': {
                                'type': ['null', 'boolean'],
                            },
                            'show_typeform_branding': {
                                'type': ['null', 'boolean'],
                            },
                            'are_uploads_public': {
                                'type': ['null', 'boolean'],
                            },
                            'show_time_to_complete': {
                                'type': ['null', 'boolean'],
                            },
                            'redirect_after_submit_url': {
                                'type': ['null', 'string'],
                            },
                            'google_analytics': {
                                'type': ['null', 'string'],
                            },
                            'facebook_pixel': {
                                'type': ['null', 'string'],
                            },
                            'google_tag_manager': {
                                'type': ['null', 'string'],
                            },
                            'capabilities': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'e2e_encryption': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'enabled': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'modifiable': {
                                                'type': ['null', 'boolean'],
                                            },
                                        },
                                    },
                                },
                            },
                            'notifications': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'self': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'enabled': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'recipients': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                            'subject': {
                                                'type': ['null', 'string'],
                                            },
                                            'message': {
                                                'type': ['null', 'string'],
                                            },
                                            'reply_to': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                    'respondent': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'enabled': {
                                                'type': ['null', 'boolean'],
                                            },
                                            'recipients': {
                                                'type': ['null', 'array'],
                                                'items': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                            'subject': {
                                                'type': ['null', 'string'],
                                            },
                                            'message': {
                                                'type': ['null', 'string'],
                                            },
                                            'reply_to': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                            },
                            'cui_settings': {
                                'type': ['null', 'object'],
                                'properties': {
                                    'avatar': {
                                        'type': ['null', 'string'],
                                    },
                                    'is_typing_emulation_disabled': {
                                        'type': ['null', 'boolean'],
                                    },
                                    'typing_emulation_speed': {
                                        'type': ['null', 'string'],
                                    },
                                },
                            },
                        },
                    },
                    'welcome_screens': {
                        'type': ['null', 'array'],
                        'description': 'Welcome screen configurations',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'ref': {
                                    'type': ['null', 'string'],
                                },
                                'title': {
                                    'type': ['null', 'string'],
                                },
                                'properties': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'show_button': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'share_icons': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'button_mode': {
                                            'type': ['null', 'string'],
                                        },
                                        'button_text': {
                                            'type': ['null', 'string'],
                                        },
                                        'redirect_url': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'attachment': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'type': {
                                            'type': ['null', 'string'],
                                        },
                                        'placement': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'layout': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'type': {
                                            'type': ['null', 'string'],
                                        },
                                        'placement': {
                                            'type': ['null', 'string'],
                                        },
                                        'attachment': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'type': {
                                                    'type': ['null', 'string'],
                                                },
                                                'href': {
                                                    'type': ['null', 'string'],
                                                },
                                                'scale': {
                                                    'type': ['null', 'number'],
                                                },
                                            },
                                        },
                                        'properties': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'brightness': {
                                                    'type': ['null', 'number'],
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                },
                                                'focal_point': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'x': {
                                                            'type': ['null', 'number'],
                                                        },
                                                        'y': {
                                                            'type': ['null', 'number'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'thankyou_screens': {
                        'type': ['null', 'array'],
                        'description': 'Thank you screen configurations',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'ref': {
                                    'type': ['null', 'string'],
                                },
                                'title': {
                                    'type': ['null', 'string'],
                                },
                                'properties': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'show_button': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'share_icons': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'button_mode': {
                                            'type': ['null', 'string'],
                                        },
                                        'button_text': {
                                            'type': ['null', 'string'],
                                        },
                                        'redirect_url': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'attachment': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'type': {
                                            'type': ['null', 'string'],
                                        },
                                        'placement': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'layout': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'type': {
                                            'type': ['null', 'string'],
                                        },
                                        'placement': {
                                            'type': ['null', 'string'],
                                        },
                                        'attachment': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'type': {
                                                    'type': ['null', 'string'],
                                                },
                                                'href': {
                                                    'type': ['null', 'string'],
                                                },
                                                'scale': {
                                                    'type': ['null', 'number'],
                                                },
                                            },
                                        },
                                        'properties': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'brightness': {
                                                    'type': ['null', 'number'],
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                },
                                                'focal_point': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'x': {
                                                            'type': ['null', 'number'],
                                                        },
                                                        'y': {
                                                            'type': ['null', 'number'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'logic': {
                        'type': ['null', 'array'],
                        'description': 'Logic rules applied to form fields',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'ref': {
                                    'type': ['null', 'string'],
                                },
                                'actions': {
                                    'type': ['null', 'array'],
                                    'items': {
                                        'type': ['null', 'object'],
                                        'properties': {
                                            'action': {
                                                'type': ['null', 'string'],
                                            },
                                            'details': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'to': {
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
                                                    'target': {
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
                                                    'value': {
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
                                            'condition': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'op': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'vars': {
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
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'fields': {
                        'type': ['null', 'array'],
                        'description': 'List of fields within the form',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                },
                                'title': {
                                    'type': ['null', 'string'],
                                },
                                'ref': {
                                    'type': ['null', 'string'],
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'properties': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'randomize': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'allow_multiple_selection': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'allow_other_choice': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'vertical_alignment': {
                                            'type': ['null', 'boolean'],
                                        },
                                        'choices': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'id': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'ref': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'label': {
                                                        'type': ['null', 'string'],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'validations': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'required': {
                                            'type': ['null', 'boolean'],
                                        },
                                    },
                                },
                                'attachment': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'type': {
                                            'type': ['null', 'string'],
                                        },
                                        'href': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'layout': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'type': {
                                            'type': ['null', 'string'],
                                        },
                                        'placement': {
                                            'type': ['null', 'string'],
                                        },
                                        'attachment': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'type': {
                                                    'type': ['null', 'string'],
                                                },
                                                'href': {
                                                    'type': ['null', 'string'],
                                                },
                                                'scale': {
                                                    'type': ['null', 'number'],
                                                },
                                            },
                                        },
                                        'properties': {
                                            'type': ['null', 'object'],
                                            'properties': {
                                                'brightness': {
                                                    'type': ['null', 'number'],
                                                },
                                                'description': {
                                                    'type': ['null', 'string'],
                                                },
                                                'focal_point': {
                                                    'type': ['null', 'object'],
                                                    'properties': {
                                                        'x': {
                                                            'type': ['null', 'number'],
                                                        },
                                                        'y': {
                                                            'type': ['null', 'number'],
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'self': {
                        'type': ['null', 'object'],
                        'description': 'Self-referential link to this form',
                        'properties': {
                            'href': {
                                'type': ['null', 'string'],
                                'description': 'URL of this form resource',
                            },
                        },
                    },
                    '_links': {
                        'type': ['null', 'object'],
                        'description': 'Links to related resources',
                        'properties': {
                            'display': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'forms',
                'x-airbyte-stream-name': 'forms',
            },
        ),
        EntityDefinition(
            name='responses',
            stream_name='responses',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/forms/{form_id}/responses',
                    action=Action.LIST,
                    description='Returns a paginated list of responses for a given form',
                    query_params=[
                        'page_size',
                        'since',
                        'until',
                        'after',
                        'before',
                        'sort',
                        'completed',
                        'query',
                    ],
                    query_params_schema={
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 25,
                        },
                        'since': {'type': 'string', 'required': False},
                        'until': {'type': 'string', 'required': False},
                        'after': {'type': 'string', 'required': False},
                        'before': {'type': 'string', 'required': False},
                        'sort': {'type': 'string', 'required': False},
                        'completed': {'type': 'boolean', 'required': False},
                        'query': {'type': 'string', 'required': False},
                    },
                    path_params=['form_id'],
                    path_params_schema={
                        'form_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of responses',
                        'properties': {
                            'total_items': {
                                'type': ['null', 'integer'],
                                'description': 'Total number of responses',
                            },
                            'page_count': {
                                'type': ['null', 'integer'],
                                'description': 'Total number of pages',
                            },
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A single form response/submission',
                                    'properties': {
                                        'response_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique identifier of the response',
                                        },
                                        'response_type': {
                                            'type': ['null', 'string'],
                                            'description': 'Type of the response',
                                        },
                                        'landed_at': {
                                            'type': ['null', 'string'],
                                            'description': 'Timestamp when the respondent landed on the form',
                                        },
                                        'landing_id': {
                                            'type': ['null', 'string'],
                                            'description': 'ID of the landing page',
                                        },
                                        'submitted_at': {
                                            'type': ['null', 'string'],
                                            'description': 'Timestamp when the response was submitted',
                                        },
                                        'token': {
                                            'type': ['null', 'string'],
                                            'description': 'Token associated with the response',
                                        },
                                        'form_id': {
                                            'type': ['null', 'string'],
                                            'description': 'ID of the form',
                                        },
                                        'metadata': {
                                            'type': ['null', 'object'],
                                            'description': 'Metadata related to the response',
                                            'properties': {
                                                'user_agent': {
                                                    'type': ['null', 'string'],
                                                },
                                                'platform': {
                                                    'type': ['null', 'string'],
                                                },
                                                'referer': {
                                                    'type': ['null', 'string'],
                                                },
                                                'network_id': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'variables': {
                                            'type': ['null', 'array'],
                                            'description': 'Variables associated with the response',
                                            'items': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'key': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'type': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'text': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'number': {
                                                        'type': ['null', 'number'],
                                                    },
                                                },
                                            },
                                        },
                                        'hidden': {
                                            'type': ['null', 'object'],
                                            'description': 'Hidden fields in the response',
                                        },
                                        'calculated': {
                                            'type': ['null', 'object'],
                                            'description': 'Calculated data related to the response',
                                            'properties': {
                                                'score': {
                                                    'type': ['null', 'integer'],
                                                },
                                            },
                                        },
                                        'answers': {
                                            'type': ['null', 'array'],
                                            'description': 'Response data for each question in the form',
                                            'items': {
                                                'type': ['null', 'object'],
                                                'properties': {
                                                    'field': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'ref': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'type': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                    'type': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'text': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'choice': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'id': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'label': {
                                                                'type': ['null', 'string'],
                                                            },
                                                        },
                                                    },
                                                    'choices': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'ids': {
                                                                'type': ['null', 'array'],
                                                                'items': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                            },
                                                            'labels': {
                                                                'type': ['null', 'array'],
                                                                'items': {
                                                                    'type': ['null', 'string'],
                                                                },
                                                            },
                                                        },
                                                    },
                                                    'number': {
                                                        'type': ['null', 'number'],
                                                    },
                                                    'date': {
                                                        'type': ['null', 'string'],
                                                        'format': 'date-time',
                                                    },
                                                    'email': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'phone_number': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'boolean': {
                                                        'type': ['null', 'boolean'],
                                                    },
                                                    'file_url': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'url': {
                                                        'type': ['null', 'string'],
                                                    },
                                                    'payment': {
                                                        'type': ['null', 'object'],
                                                        'properties': {
                                                            'amount': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'last4': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'name': {
                                                                'type': ['null', 'string'],
                                                            },
                                                            'success': {
                                                                'type': ['null', 'boolean'],
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'responses',
                                    'x-airbyte-stream-name': 'responses',
                                },
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'total_items': '$.total_items', 'page_count': '$.page_count'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A single form response/submission',
                'properties': {
                    'response_id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier of the response',
                    },
                    'response_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of the response',
                    },
                    'landed_at': {
                        'type': ['null', 'string'],
                        'description': 'Timestamp when the respondent landed on the form',
                    },
                    'landing_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the landing page',
                    },
                    'submitted_at': {
                        'type': ['null', 'string'],
                        'description': 'Timestamp when the response was submitted',
                    },
                    'token': {
                        'type': ['null', 'string'],
                        'description': 'Token associated with the response',
                    },
                    'form_id': {
                        'type': ['null', 'string'],
                        'description': 'ID of the form',
                    },
                    'metadata': {
                        'type': ['null', 'object'],
                        'description': 'Metadata related to the response',
                        'properties': {
                            'user_agent': {
                                'type': ['null', 'string'],
                            },
                            'platform': {
                                'type': ['null', 'string'],
                            },
                            'referer': {
                                'type': ['null', 'string'],
                            },
                            'network_id': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'variables': {
                        'type': ['null', 'array'],
                        'description': 'Variables associated with the response',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'key': {
                                    'type': ['null', 'string'],
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'text': {
                                    'type': ['null', 'string'],
                                },
                                'number': {
                                    'type': ['null', 'number'],
                                },
                            },
                        },
                    },
                    'hidden': {
                        'type': ['null', 'object'],
                        'description': 'Hidden fields in the response',
                    },
                    'calculated': {
                        'type': ['null', 'object'],
                        'description': 'Calculated data related to the response',
                        'properties': {
                            'score': {
                                'type': ['null', 'integer'],
                            },
                        },
                    },
                    'answers': {
                        'type': ['null', 'array'],
                        'description': 'Response data for each question in the form',
                        'items': {
                            'type': ['null', 'object'],
                            'properties': {
                                'field': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'ref': {
                                            'type': ['null', 'string'],
                                        },
                                        'type': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                },
                                'text': {
                                    'type': ['null', 'string'],
                                },
                                'choice': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                        },
                                        'label': {
                                            'type': ['null', 'string'],
                                        },
                                    },
                                },
                                'choices': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'ids': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                        'labels': {
                                            'type': ['null', 'array'],
                                            'items': {
                                                'type': ['null', 'string'],
                                            },
                                        },
                                    },
                                },
                                'number': {
                                    'type': ['null', 'number'],
                                },
                                'date': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                },
                                'email': {
                                    'type': ['null', 'string'],
                                },
                                'phone_number': {
                                    'type': ['null', 'string'],
                                },
                                'boolean': {
                                    'type': ['null', 'boolean'],
                                },
                                'file_url': {
                                    'type': ['null', 'string'],
                                },
                                'url': {
                                    'type': ['null', 'string'],
                                },
                                'payment': {
                                    'type': ['null', 'object'],
                                    'properties': {
                                        'amount': {
                                            'type': ['null', 'string'],
                                        },
                                        'last4': {
                                            'type': ['null', 'string'],
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                        },
                                        'success': {
                                            'type': ['null', 'boolean'],
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'responses',
                'x-airbyte-stream-name': 'responses',
            },
        ),
        EntityDefinition(
            name='webhooks',
            stream_name='webhooks',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/forms/{form_id}/webhooks',
                    action=Action.LIST,
                    description='Returns webhooks configured for a given form',
                    path_params=['form_id'],
                    path_params_schema={
                        'form_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'List of webhooks',
                        'properties': {
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A webhook configured for a form',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique identifier of the webhook',
                                        },
                                        'form_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique identifier of the form associated with the webhook',
                                        },
                                        'tag': {
                                            'type': ['null', 'string'],
                                            'description': 'A tag to categorize or label the webhook',
                                        },
                                        'url': {
                                            'type': ['null', 'string'],
                                            'description': 'The URL where webhook data is sent',
                                        },
                                        'enabled': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Indicates if the webhook is currently enabled',
                                        },
                                        'verify_ssl': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether SSL verification is enforced for the webhook URL',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'description': 'Timestamp when the webhook was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'description': 'Timestamp when the webhook was last updated',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'webhooks',
                                    'x-airbyte-stream-name': 'webhooks',
                                },
                            },
                        },
                    },
                    record_extractor='$.items',
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A webhook configured for a form',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier of the webhook',
                    },
                    'form_id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier of the form associated with the webhook',
                    },
                    'tag': {
                        'type': ['null', 'string'],
                        'description': 'A tag to categorize or label the webhook',
                    },
                    'url': {
                        'type': ['null', 'string'],
                        'description': 'The URL where webhook data is sent',
                    },
                    'enabled': {
                        'type': ['null', 'boolean'],
                        'description': 'Indicates if the webhook is currently enabled',
                    },
                    'verify_ssl': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether SSL verification is enforced for the webhook URL',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'description': 'Timestamp when the webhook was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'description': 'Timestamp when the webhook was last updated',
                    },
                },
                'x-airbyte-entity-name': 'webhooks',
                'x-airbyte-stream-name': 'webhooks',
            },
        ),
        EntityDefinition(
            name='workspaces',
            stream_name='workspaces',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/workspaces',
                    action=Action.LIST,
                    description='Returns a paginated list of workspaces in the account',
                    query_params=['page', 'page_size'],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of workspaces',
                        'properties': {
                            'total_items': {
                                'type': ['null', 'integer'],
                                'description': 'Total number of workspaces',
                            },
                            'page_count': {
                                'type': ['null', 'integer'],
                                'description': 'Total number of pages',
                            },
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A workspace containing forms',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique identifier of the workspace',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the workspace',
                                        },
                                        'account_id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique identifier of the account associated with the workspace',
                                        },
                                        'default': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this is the default workspace',
                                        },
                                        'shared': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether this workspace is shared with other users',
                                        },
                                        'forms': {
                                            'type': ['null', 'object'],
                                            'description': 'Information about forms in the workspace',
                                            'properties': {
                                                'count': {
                                                    'type': ['null', 'number'],
                                                    'description': 'Total number of forms in this workspace',
                                                },
                                                'href': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL to retrieve the forms',
                                                },
                                            },
                                        },
                                        'self': {
                                            'type': ['null', 'object'],
                                            'description': 'Self-referential link',
                                            'properties': {
                                                'href': {
                                                    'type': ['null', 'string'],
                                                    'description': 'URL to this workspace',
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'workspaces',
                                    'x-airbyte-stream-name': 'workspaces',
                                },
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'total_items': '$.total_items', 'page_count': '$.page_count'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A workspace containing forms',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier of the workspace',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the workspace',
                    },
                    'account_id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier of the account associated with the workspace',
                    },
                    'default': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is the default workspace',
                    },
                    'shared': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this workspace is shared with other users',
                    },
                    'forms': {
                        'type': ['null', 'object'],
                        'description': 'Information about forms in the workspace',
                        'properties': {
                            'count': {
                                'type': ['null', 'number'],
                                'description': 'Total number of forms in this workspace',
                            },
                            'href': {
                                'type': ['null', 'string'],
                                'description': 'URL to retrieve the forms',
                            },
                        },
                    },
                    'self': {
                        'type': ['null', 'object'],
                        'description': 'Self-referential link',
                        'properties': {
                            'href': {
                                'type': ['null', 'string'],
                                'description': 'URL to this workspace',
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'workspaces',
                'x-airbyte-stream-name': 'workspaces',
            },
        ),
        EntityDefinition(
            name='images',
            stream_name='images',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/images',
                    action=Action.LIST,
                    description='Returns a list of images in the account',
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'An image in the account',
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                    'description': 'Unique identifier of the image',
                                },
                                'file_name': {
                                    'type': ['null', 'string'],
                                    'description': 'Name of the image file',
                                },
                                'src': {
                                    'type': ['null', 'string'],
                                    'description': 'URL to access the image',
                                },
                                'width': {
                                    'type': ['null', 'integer'],
                                    'description': 'Width of the image in pixels',
                                },
                                'height': {
                                    'type': ['null', 'integer'],
                                    'description': 'Height of the image in pixels',
                                },
                                'media_type': {
                                    'type': ['null', 'string'],
                                    'description': 'MIME type of the image (e.g. image/jpeg)',
                                },
                                'avg_color': {
                                    'type': ['null', 'string'],
                                    'description': 'Average color of the image',
                                },
                                'has_alpha': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the image has an alpha channel',
                                },
                                'upload_source': {
                                    'type': ['null', 'string'],
                                    'description': 'Source from which the image was uploaded',
                                },
                            },
                            'x-airbyte-entity-name': 'images',
                            'x-airbyte-stream-name': 'images',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'An image in the account',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier of the image',
                    },
                    'file_name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the image file',
                    },
                    'src': {
                        'type': ['null', 'string'],
                        'description': 'URL to access the image',
                    },
                    'width': {
                        'type': ['null', 'integer'],
                        'description': 'Width of the image in pixels',
                    },
                    'height': {
                        'type': ['null', 'integer'],
                        'description': 'Height of the image in pixels',
                    },
                    'media_type': {
                        'type': ['null', 'string'],
                        'description': 'MIME type of the image (e.g. image/jpeg)',
                    },
                    'avg_color': {
                        'type': ['null', 'string'],
                        'description': 'Average color of the image',
                    },
                    'has_alpha': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the image has an alpha channel',
                    },
                    'upload_source': {
                        'type': ['null', 'string'],
                        'description': 'Source from which the image was uploaded',
                    },
                },
                'x-airbyte-entity-name': 'images',
                'x-airbyte-stream-name': 'images',
            },
        ),
        EntityDefinition(
            name='themes',
            stream_name='themes',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/themes',
                    action=Action.LIST,
                    description='Returns a paginated list of themes in the account',
                    query_params=['page', 'page_size'],
                    query_params_schema={
                        'page': {
                            'type': 'integer',
                            'required': False,
                            'default': 1,
                        },
                        'page_size': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Paginated list of themes',
                        'properties': {
                            'total_items': {
                                'type': ['null', 'integer'],
                                'description': 'Total number of themes',
                            },
                            'page_count': {
                                'type': ['null', 'integer'],
                                'description': 'Total number of pages',
                            },
                            'items': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A theme used for styling forms',
                                    'properties': {
                                        'id': {
                                            'type': ['null', 'string'],
                                            'description': 'Unique identifier of the theme',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the theme',
                                        },
                                        'visibility': {
                                            'type': ['null', 'string'],
                                            'description': 'Visibility setting of the theme',
                                        },
                                        'font': {
                                            'type': ['null', 'string'],
                                            'description': 'Font used in the theme',
                                        },
                                        'has_transparent_button': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the theme has a transparent button',
                                        },
                                        'rounded_corners': {
                                            'type': ['null', 'string'],
                                            'description': 'Rounded corners setting',
                                        },
                                        'colors': {
                                            'type': ['null', 'object'],
                                            'description': 'Color settings',
                                            'properties': {
                                                'answer': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Color of answer text',
                                                },
                                                'background': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Background color',
                                                },
                                                'button': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Color of buttons',
                                                },
                                                'question': {
                                                    'type': ['null', 'string'],
                                                    'description': 'Color of question text',
                                                },
                                            },
                                        },
                                        'background': {
                                            'type': ['null', 'object'],
                                            'description': 'Background settings',
                                            'properties': {
                                                'brightness': {
                                                    'type': ['null', 'number'],
                                                },
                                                'href': {
                                                    'type': ['null', 'string'],
                                                },
                                                'layout': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'fields': {
                                            'type': ['null', 'object'],
                                            'description': 'Field display settings',
                                            'properties': {
                                                'alignment': {
                                                    'type': ['null', 'string'],
                                                },
                                                'font_size': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'screens': {
                                            'type': ['null', 'object'],
                                            'description': 'Screen display settings',
                                            'properties': {
                                                'alignment': {
                                                    'type': ['null', 'string'],
                                                },
                                                'font_size': {
                                                    'type': ['null', 'string'],
                                                },
                                            },
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the theme was created',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Timestamp when the theme was last updated',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'themes',
                                    'x-airbyte-stream-name': 'themes',
                                },
                            },
                        },
                    },
                    record_extractor='$.items',
                    meta_extractor={'total_items': '$.total_items', 'page_count': '$.page_count'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A theme used for styling forms',
                'properties': {
                    'id': {
                        'type': ['null', 'string'],
                        'description': 'Unique identifier of the theme',
                    },
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the theme',
                    },
                    'visibility': {
                        'type': ['null', 'string'],
                        'description': 'Visibility setting of the theme',
                    },
                    'font': {
                        'type': ['null', 'string'],
                        'description': 'Font used in the theme',
                    },
                    'has_transparent_button': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the theme has a transparent button',
                    },
                    'rounded_corners': {
                        'type': ['null', 'string'],
                        'description': 'Rounded corners setting',
                    },
                    'colors': {
                        'type': ['null', 'object'],
                        'description': 'Color settings',
                        'properties': {
                            'answer': {
                                'type': ['null', 'string'],
                                'description': 'Color of answer text',
                            },
                            'background': {
                                'type': ['null', 'string'],
                                'description': 'Background color',
                            },
                            'button': {
                                'type': ['null', 'string'],
                                'description': 'Color of buttons',
                            },
                            'question': {
                                'type': ['null', 'string'],
                                'description': 'Color of question text',
                            },
                        },
                    },
                    'background': {
                        'type': ['null', 'object'],
                        'description': 'Background settings',
                        'properties': {
                            'brightness': {
                                'type': ['null', 'number'],
                            },
                            'href': {
                                'type': ['null', 'string'],
                            },
                            'layout': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'fields': {
                        'type': ['null', 'object'],
                        'description': 'Field display settings',
                        'properties': {
                            'alignment': {
                                'type': ['null', 'string'],
                            },
                            'font_size': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'screens': {
                        'type': ['null', 'object'],
                        'description': 'Screen display settings',
                        'properties': {
                            'alignment': {
                                'type': ['null', 'string'],
                            },
                            'font_size': {
                                'type': ['null', 'string'],
                            },
                        },
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the theme was created',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp when the theme was last updated',
                    },
                },
                'x-airbyte-entity-name': 'themes',
                'x-airbyte-stream-name': 'themes',
            },
        ),
    ],
    search_field_paths={
        'forms': [
            '_links',
            '_links.display',
            'created_at',
            'fields',
            'fields[]',
            'id',
            'last_updated_at',
            'logic',
            'logic[]',
            'published_at',
            'settings',
            'settings.language',
            'settings.progress_bar',
            'settings.meta',
            'settings.meta.allow_indexing',
            'settings.meta.title',
            'settings.meta.description',
            'settings.meta.image',
            'settings.meta.image.href',
            'settings.hide_navigation',
            'settings.is_public',
            'settings.is_trial',
            'settings.show_progress_bar',
            'settings.show_typeform_branding',
            'settings.are_uploads_public',
            'settings.show_time_to_complete',
            'settings.redirect_after_submit_url',
            'settings.google_analytics',
            'settings.facebook_pixel',
            'settings.google_tag_manager',
            'settings.capabilities',
            'settings.capabilities.e2e_encryption',
            'settings.capabilities.e2e_encryption.enabled',
            'settings.capabilities.e2e_encryption.modifiable',
            'settings.notifications',
            'settings.notifications.self',
            'settings.notifications.self.enabled',
            'settings.notifications.self.recipients',
            'settings.notifications.self.recipients[]',
            'settings.notifications.self.subject',
            'settings.notifications.self.message',
            'settings.notifications.self.reply_to',
            'settings.notifications.respondent',
            'settings.notifications.respondent.enabled',
            'settings.notifications.respondent.recipients',
            'settings.notifications.respondent.recipients[]',
            'settings.notifications.respondent.subject',
            'settings.notifications.respondent.message',
            'settings.notifications.respondent.reply_to',
            'settings.cui_settings',
            'settings.cui_settings.avatar',
            'settings.cui_settings.is_typing_emulation_disabled',
            'settings.cui_settings.typing_emulation_speed',
            'thankyou_screens',
            'thankyou_screens[]',
            'theme',
            'theme.href',
            'title',
            'type',
            'welcome_screens',
            'welcome_screens[]',
            'workspace',
            'workspace.href',
        ],
        'responses': [
            'answers',
            'answers[]',
            'calculated',
            'calculated.score',
            'form_id',
            'hidden',
            'landed_at',
            'landing_id',
            'metadata',
            'metadata.user_agent',
            'metadata.platform',
            'metadata.referer',
            'metadata.network_id',
            'response_id',
            'response_type',
            'submitted_at',
            'token',
            'variables',
            'variables[]',
        ],
        'webhooks': [
            'created_at',
            'enabled',
            'form_id',
            'id',
            'tag',
            'updated_at',
            'url',
            'verify_ssl',
        ],
        'workspaces': [
            'account_id',
            'default',
            'forms',
            'forms.count',
            'forms.href',
            'id',
            'name',
            'self',
            'self.href',
            'shared',
        ],
        'images': [
            'avg_color',
            'file_name',
            'has_alpha',
            'height',
            'id',
            'media_type',
            'src',
            'width',
        ],
        'themes': [
            'background',
            'background.brightness',
            'background.href',
            'background.layout',
            'colors',
            'colors.answer',
            'colors.background',
            'colors.button',
            'colors.question',
            'created_at',
            'fields',
            'fields.alignment',
            'fields.font_size',
            'font',
            'has_transparent_button',
            'id',
            'name',
            'rounded_corners',
            'screens',
            'screens.alignment',
            'screens.font_size',
            'updated_at',
            'visibility',
        ],
    },
)