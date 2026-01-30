"""
Connector model for mailchimp.

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

MailchimpConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('b03a9f3e-22a5-11eb-adc1-0242ac120002'),
    name='mailchimp',
    version='1.0.5',
    base_url='https://{data_center}.api.mailchimp.com/3.0',
    auth=AuthConfig(
        type=AuthType.BASIC,
        user_config_spec=AirbyteAuthConfig(
            title='API Key Authentication',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='Your Mailchimp API key. You can find this in your Mailchimp account under Account > Extras > API keys.',
                ),
            },
            auth_mapping={'username': 'anystring', 'password': '${api_key}'},
            replication_auth_key_mapping={'credentials.apikey': 'api_key'},
            replication_auth_key_constants={'credentials.auth_type': 'apikey'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='campaigns',
            stream_name='campaigns',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/campaigns',
                    action=Action.LIST,
                    description='Get all campaigns in an account',
                    query_params=[
                        'count',
                        'offset',
                        'type',
                        'status',
                        'before_send_time',
                        'since_send_time',
                        'before_create_time',
                        'since_create_time',
                        'list_id',
                        'folder_id',
                        'sort_field',
                        'sort_dir',
                    ],
                    query_params_schema={
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'type': {'type': 'string', 'required': False},
                        'status': {'type': 'string', 'required': False},
                        'before_send_time': {'type': 'string', 'required': False},
                        'since_send_time': {'type': 'string', 'required': False},
                        'before_create_time': {'type': 'string', 'required': False},
                        'since_create_time': {'type': 'string', 'required': False},
                        'list_id': {'type': 'string', 'required': False},
                        'folder_id': {'type': 'string', 'required': False},
                        'sort_field': {'type': 'string', 'required': False},
                        'sort_dir': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A collection of campaigns',
                        'properties': {
                            'campaigns': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': "A summary of an individual campaign's settings and content",
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'A string that uniquely identifies this campaign'},
                                        'web_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'The ID used in the Mailchimp web application',
                                        },
                                        'parent_campaign_id': {
                                            'type': ['string', 'null'],
                                            'description': 'If this campaign is the child of another campaign',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'The type of campaign',
                                            'enum': [
                                                'regular',
                                                'plaintext',
                                                'absplit',
                                                'rss',
                                                'variate',
                                                'automation-email',
                                                None,
                                            ],
                                        },
                                        'create_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time the campaign was created',
                                        },
                                        'archive_url': {
                                            'type': ['string', 'null'],
                                            'description': "The link to the campaign's archive version",
                                        },
                                        'long_archive_url': {
                                            'type': ['string', 'null'],
                                            'description': "The original link to the campaign's archive version",
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'The current status of the campaign',
                                            'enum': [
                                                'save',
                                                'paused',
                                                'schedule',
                                                'sending',
                                                'sent',
                                                None,
                                            ],
                                        },
                                        'emails_sent': {
                                            'type': ['integer', 'null'],
                                            'description': 'The total number of emails sent for this campaign',
                                        },
                                        'send_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time a campaign was sent',
                                        },
                                        'content_type': {
                                            'type': ['string', 'null'],
                                            'description': "How the campaign's content is put together",
                                        },
                                        'needs_block_refresh': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor',
                                        },
                                        'resendable': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Determines if the campaign qualifies to be resent to non-openers',
                                        },
                                        'recipients': {
                                            'type': ['object', 'null'],
                                            'description': 'List settings for the campaign',
                                            'properties': {
                                                'list_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The unique list id',
                                                },
                                                'list_is_active': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'The status of the list used',
                                                },
                                                'list_name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The name of the list',
                                                },
                                                'segment_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'A description of the segment used for the campaign',
                                                },
                                                'recipient_count': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'Count of the recipients on the associated list',
                                                },
                                            },
                                        },
                                        'settings': {
                                            'type': ['object', 'null'],
                                            'description': 'The settings for your campaign',
                                            'properties': {
                                                'subject_line': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The subject line for the campaign',
                                                },
                                                'preview_text': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The preview text for the campaign',
                                                },
                                                'title': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The title of the campaign',
                                                },
                                                'from_name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The from name on the campaign',
                                                },
                                                'reply_to': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The reply-to email address for the campaign',
                                                },
                                                'use_conversation': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Use Mailchimp Conversation feature to manage out-of-office replies',
                                                },
                                                'to_name': {
                                                    'type': ['string', 'null'],
                                                    'description': "The campaign's custom to name",
                                                },
                                                'folder_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'If the campaign is listed in a folder',
                                                },
                                                'authenticate': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether Mailchimp authenticated the campaign',
                                                },
                                                'auto_footer': {
                                                    'type': ['boolean', 'null'],
                                                    'description': "Automatically append Mailchimp's default footer to the campaign",
                                                },
                                                'inline_css': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Automatically inline the CSS included with the campaign content',
                                                },
                                                'auto_tweet': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Automatically tweet a link to the campaign archive page when the campaign is sent',
                                                },
                                                'fb_comments': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Allows Facebook comments on the campaign',
                                                },
                                                'timewarp': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Send this campaign using Timewarp',
                                                },
                                                'template_id': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The id for the template used in this campaign',
                                                },
                                                'drag_and_drop': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether the campaign uses the drag-and-drop editor',
                                                },
                                            },
                                        },
                                        'tracking': {
                                            'type': ['object', 'null'],
                                            'description': 'The tracking options for a campaign',
                                            'properties': {
                                                'opens': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether to track opens',
                                                },
                                                'html_clicks': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether to track clicks in the HTML version of the campaign',
                                                },
                                                'text_clicks': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether to track clicks in the plain-text version of the campaign',
                                                },
                                                'goal_tracking': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether to enable Goal tracking',
                                                },
                                                'ecomm360': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether to enable eCommerce360 tracking',
                                                },
                                                'google_analytics': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The custom slug for Google Analytics tracking',
                                                },
                                                'clicktale': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The custom slug for ClickTale tracking',
                                                },
                                            },
                                        },
                                        'report_summary': {
                                            'type': ['object', 'null'],
                                            'description': 'For sent campaigns, a summary of opens, clicks, and e-commerce data',
                                            'properties': {
                                                'opens': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of opens for a campaign',
                                                },
                                                'unique_opens': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of unique opens',
                                                },
                                                'open_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The number of unique opens divided by the total number of successful deliveries',
                                                },
                                                'clicks': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of clicks for an campaign',
                                                },
                                                'subscriber_clicks': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of unique clicks',
                                                },
                                                'click_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The number of unique clicks divided by the total number of successful deliveries',
                                                },
                                                'ecommerce': {
                                                    'type': ['object', 'null'],
                                                    'description': 'E-Commerce stats for a campaign',
                                                    'properties': {
                                                        'total_orders': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'The total orders for a campaign',
                                                        },
                                                        'total_spent': {
                                                            'type': ['number', 'null'],
                                                            'description': 'The total spent for a campaign',
                                                        },
                                                        'total_revenue': {
                                                            'type': ['number', 'null'],
                                                            'description': 'The total revenue for a campaign',
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'delivery_status': {
                                            'type': ['object', 'null'],
                                            'description': 'Updates on campaigns in the process of sending',
                                            'properties': {
                                                'enabled': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether Campaign Delivery Status is enabled for this account and target campaign',
                                                },
                                                'can_cancel': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether a campaign send can be canceled',
                                                },
                                                'status': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The current state of a campaign delivery',
                                                },
                                                'emails_sent': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of emails confirmed sent for this campaign so far',
                                                },
                                                'emails_canceled': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of emails canceled for this campaign',
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'campaigns',
                                    'x-airbyte-stream-name': 'campaigns',
                                },
                            },
                            'total_items': {'type': 'integer', 'description': 'The total number of items matching the query regardless of pagination'},
                        },
                    },
                    record_extractor='$.campaigns',
                    meta_extractor={'total_items': '$.total_items'},
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/campaigns/{campaign_id}',
                    action=Action.GET,
                    description='Get information about a specific campaign',
                    path_params=['campaign_id'],
                    path_params_schema={
                        'campaign_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': "A summary of an individual campaign's settings and content",
                        'properties': {
                            'id': {'type': 'string', 'description': 'A string that uniquely identifies this campaign'},
                            'web_id': {
                                'type': ['integer', 'null'],
                                'description': 'The ID used in the Mailchimp web application',
                            },
                            'parent_campaign_id': {
                                'type': ['string', 'null'],
                                'description': 'If this campaign is the child of another campaign',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'The type of campaign',
                                'enum': [
                                    'regular',
                                    'plaintext',
                                    'absplit',
                                    'rss',
                                    'variate',
                                    'automation-email',
                                    None,
                                ],
                            },
                            'create_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time the campaign was created',
                            },
                            'archive_url': {
                                'type': ['string', 'null'],
                                'description': "The link to the campaign's archive version",
                            },
                            'long_archive_url': {
                                'type': ['string', 'null'],
                                'description': "The original link to the campaign's archive version",
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'The current status of the campaign',
                                'enum': [
                                    'save',
                                    'paused',
                                    'schedule',
                                    'sending',
                                    'sent',
                                    None,
                                ],
                            },
                            'emails_sent': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of emails sent for this campaign',
                            },
                            'send_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time a campaign was sent',
                            },
                            'content_type': {
                                'type': ['string', 'null'],
                                'description': "How the campaign's content is put together",
                            },
                            'needs_block_refresh': {
                                'type': ['boolean', 'null'],
                                'description': 'Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor',
                            },
                            'resendable': {
                                'type': ['boolean', 'null'],
                                'description': 'Determines if the campaign qualifies to be resent to non-openers',
                            },
                            'recipients': {
                                'type': ['object', 'null'],
                                'description': 'List settings for the campaign',
                                'properties': {
                                    'list_id': {
                                        'type': ['string', 'null'],
                                        'description': 'The unique list id',
                                    },
                                    'list_is_active': {
                                        'type': ['boolean', 'null'],
                                        'description': 'The status of the list used',
                                    },
                                    'list_name': {
                                        'type': ['string', 'null'],
                                        'description': 'The name of the list',
                                    },
                                    'segment_text': {
                                        'type': ['string', 'null'],
                                        'description': 'A description of the segment used for the campaign',
                                    },
                                    'recipient_count': {
                                        'type': ['integer', 'null'],
                                        'description': 'Count of the recipients on the associated list',
                                    },
                                },
                            },
                            'settings': {
                                'type': ['object', 'null'],
                                'description': 'The settings for your campaign',
                                'properties': {
                                    'subject_line': {
                                        'type': ['string', 'null'],
                                        'description': 'The subject line for the campaign',
                                    },
                                    'preview_text': {
                                        'type': ['string', 'null'],
                                        'description': 'The preview text for the campaign',
                                    },
                                    'title': {
                                        'type': ['string', 'null'],
                                        'description': 'The title of the campaign',
                                    },
                                    'from_name': {
                                        'type': ['string', 'null'],
                                        'description': 'The from name on the campaign',
                                    },
                                    'reply_to': {
                                        'type': ['string', 'null'],
                                        'description': 'The reply-to email address for the campaign',
                                    },
                                    'use_conversation': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Use Mailchimp Conversation feature to manage out-of-office replies',
                                    },
                                    'to_name': {
                                        'type': ['string', 'null'],
                                        'description': "The campaign's custom to name",
                                    },
                                    'folder_id': {
                                        'type': ['string', 'null'],
                                        'description': 'If the campaign is listed in a folder',
                                    },
                                    'authenticate': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether Mailchimp authenticated the campaign',
                                    },
                                    'auto_footer': {
                                        'type': ['boolean', 'null'],
                                        'description': "Automatically append Mailchimp's default footer to the campaign",
                                    },
                                    'inline_css': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Automatically inline the CSS included with the campaign content',
                                    },
                                    'auto_tweet': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Automatically tweet a link to the campaign archive page when the campaign is sent',
                                    },
                                    'fb_comments': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Allows Facebook comments on the campaign',
                                    },
                                    'timewarp': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Send this campaign using Timewarp',
                                    },
                                    'template_id': {
                                        'type': ['integer', 'null'],
                                        'description': 'The id for the template used in this campaign',
                                    },
                                    'drag_and_drop': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether the campaign uses the drag-and-drop editor',
                                    },
                                },
                            },
                            'tracking': {
                                'type': ['object', 'null'],
                                'description': 'The tracking options for a campaign',
                                'properties': {
                                    'opens': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether to track opens',
                                    },
                                    'html_clicks': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether to track clicks in the HTML version of the campaign',
                                    },
                                    'text_clicks': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether to track clicks in the plain-text version of the campaign',
                                    },
                                    'goal_tracking': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether to enable Goal tracking',
                                    },
                                    'ecomm360': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether to enable eCommerce360 tracking',
                                    },
                                    'google_analytics': {
                                        'type': ['string', 'null'],
                                        'description': 'The custom slug for Google Analytics tracking',
                                    },
                                    'clicktale': {
                                        'type': ['string', 'null'],
                                        'description': 'The custom slug for ClickTale tracking',
                                    },
                                },
                            },
                            'report_summary': {
                                'type': ['object', 'null'],
                                'description': 'For sent campaigns, a summary of opens, clicks, and e-commerce data',
                                'properties': {
                                    'opens': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total number of opens for a campaign',
                                    },
                                    'unique_opens': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of unique opens',
                                    },
                                    'open_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The number of unique opens divided by the total number of successful deliveries',
                                    },
                                    'clicks': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total number of clicks for an campaign',
                                    },
                                    'subscriber_clicks': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of unique clicks',
                                    },
                                    'click_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The number of unique clicks divided by the total number of successful deliveries',
                                    },
                                    'ecommerce': {
                                        'type': ['object', 'null'],
                                        'description': 'E-Commerce stats for a campaign',
                                        'properties': {
                                            'total_orders': {
                                                'type': ['integer', 'null'],
                                                'description': 'The total orders for a campaign',
                                            },
                                            'total_spent': {
                                                'type': ['number', 'null'],
                                                'description': 'The total spent for a campaign',
                                            },
                                            'total_revenue': {
                                                'type': ['number', 'null'],
                                                'description': 'The total revenue for a campaign',
                                            },
                                        },
                                    },
                                },
                            },
                            'delivery_status': {
                                'type': ['object', 'null'],
                                'description': 'Updates on campaigns in the process of sending',
                                'properties': {
                                    'enabled': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether Campaign Delivery Status is enabled for this account and target campaign',
                                    },
                                    'can_cancel': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether a campaign send can be canceled',
                                    },
                                    'status': {
                                        'type': ['string', 'null'],
                                        'description': 'The current state of a campaign delivery',
                                    },
                                    'emails_sent': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total number of emails confirmed sent for this campaign so far',
                                    },
                                    'emails_canceled': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total number of emails canceled for this campaign',
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'campaigns',
                        'x-airbyte-stream-name': 'campaigns',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': "A summary of an individual campaign's settings and content",
                'properties': {
                    'id': {'type': 'string', 'description': 'A string that uniquely identifies this campaign'},
                    'web_id': {
                        'type': ['integer', 'null'],
                        'description': 'The ID used in the Mailchimp web application',
                    },
                    'parent_campaign_id': {
                        'type': ['string', 'null'],
                        'description': 'If this campaign is the child of another campaign',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'The type of campaign',
                        'enum': [
                            'regular',
                            'plaintext',
                            'absplit',
                            'rss',
                            'variate',
                            'automation-email',
                            None,
                        ],
                    },
                    'create_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time the campaign was created',
                    },
                    'archive_url': {
                        'type': ['string', 'null'],
                        'description': "The link to the campaign's archive version",
                    },
                    'long_archive_url': {
                        'type': ['string', 'null'],
                        'description': "The original link to the campaign's archive version",
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'The current status of the campaign',
                        'enum': [
                            'save',
                            'paused',
                            'schedule',
                            'sending',
                            'sent',
                            None,
                        ],
                    },
                    'emails_sent': {
                        'type': ['integer', 'null'],
                        'description': 'The total number of emails sent for this campaign',
                    },
                    'send_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time a campaign was sent',
                    },
                    'content_type': {
                        'type': ['string', 'null'],
                        'description': "How the campaign's content is put together",
                    },
                    'needs_block_refresh': {
                        'type': ['boolean', 'null'],
                        'description': 'Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor',
                    },
                    'resendable': {
                        'type': ['boolean', 'null'],
                        'description': 'Determines if the campaign qualifies to be resent to non-openers',
                    },
                    'recipients': {
                        'type': ['object', 'null'],
                        'description': 'List settings for the campaign',
                        'properties': {
                            'list_id': {
                                'type': ['string', 'null'],
                                'description': 'The unique list id',
                            },
                            'list_is_active': {
                                'type': ['boolean', 'null'],
                                'description': 'The status of the list used',
                            },
                            'list_name': {
                                'type': ['string', 'null'],
                                'description': 'The name of the list',
                            },
                            'segment_text': {
                                'type': ['string', 'null'],
                                'description': 'A description of the segment used for the campaign',
                            },
                            'recipient_count': {
                                'type': ['integer', 'null'],
                                'description': 'Count of the recipients on the associated list',
                            },
                        },
                    },
                    'settings': {
                        'type': ['object', 'null'],
                        'description': 'The settings for your campaign',
                        'properties': {
                            'subject_line': {
                                'type': ['string', 'null'],
                                'description': 'The subject line for the campaign',
                            },
                            'preview_text': {
                                'type': ['string', 'null'],
                                'description': 'The preview text for the campaign',
                            },
                            'title': {
                                'type': ['string', 'null'],
                                'description': 'The title of the campaign',
                            },
                            'from_name': {
                                'type': ['string', 'null'],
                                'description': 'The from name on the campaign',
                            },
                            'reply_to': {
                                'type': ['string', 'null'],
                                'description': 'The reply-to email address for the campaign',
                            },
                            'use_conversation': {
                                'type': ['boolean', 'null'],
                                'description': 'Use Mailchimp Conversation feature to manage out-of-office replies',
                            },
                            'to_name': {
                                'type': ['string', 'null'],
                                'description': "The campaign's custom to name",
                            },
                            'folder_id': {
                                'type': ['string', 'null'],
                                'description': 'If the campaign is listed in a folder',
                            },
                            'authenticate': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether Mailchimp authenticated the campaign',
                            },
                            'auto_footer': {
                                'type': ['boolean', 'null'],
                                'description': "Automatically append Mailchimp's default footer to the campaign",
                            },
                            'inline_css': {
                                'type': ['boolean', 'null'],
                                'description': 'Automatically inline the CSS included with the campaign content',
                            },
                            'auto_tweet': {
                                'type': ['boolean', 'null'],
                                'description': 'Automatically tweet a link to the campaign archive page when the campaign is sent',
                            },
                            'fb_comments': {
                                'type': ['boolean', 'null'],
                                'description': 'Allows Facebook comments on the campaign',
                            },
                            'timewarp': {
                                'type': ['boolean', 'null'],
                                'description': 'Send this campaign using Timewarp',
                            },
                            'template_id': {
                                'type': ['integer', 'null'],
                                'description': 'The id for the template used in this campaign',
                            },
                            'drag_and_drop': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the campaign uses the drag-and-drop editor',
                            },
                        },
                    },
                    'tracking': {
                        'type': ['object', 'null'],
                        'description': 'The tracking options for a campaign',
                        'properties': {
                            'opens': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to track opens',
                            },
                            'html_clicks': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to track clicks in the HTML version of the campaign',
                            },
                            'text_clicks': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to track clicks in the plain-text version of the campaign',
                            },
                            'goal_tracking': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to enable Goal tracking',
                            },
                            'ecomm360': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to enable eCommerce360 tracking',
                            },
                            'google_analytics': {
                                'type': ['string', 'null'],
                                'description': 'The custom slug for Google Analytics tracking',
                            },
                            'clicktale': {
                                'type': ['string', 'null'],
                                'description': 'The custom slug for ClickTale tracking',
                            },
                        },
                    },
                    'report_summary': {
                        'type': ['object', 'null'],
                        'description': 'For sent campaigns, a summary of opens, clicks, and e-commerce data',
                        'properties': {
                            'opens': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of opens for a campaign',
                            },
                            'unique_opens': {
                                'type': ['integer', 'null'],
                                'description': 'The number of unique opens',
                            },
                            'open_rate': {
                                'type': ['number', 'null'],
                                'description': 'The number of unique opens divided by the total number of successful deliveries',
                            },
                            'clicks': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of clicks for an campaign',
                            },
                            'subscriber_clicks': {
                                'type': ['integer', 'null'],
                                'description': 'The number of unique clicks',
                            },
                            'click_rate': {
                                'type': ['number', 'null'],
                                'description': 'The number of unique clicks divided by the total number of successful deliveries',
                            },
                            'ecommerce': {
                                'type': ['object', 'null'],
                                'description': 'E-Commerce stats for a campaign',
                                'properties': {
                                    'total_orders': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total orders for a campaign',
                                    },
                                    'total_spent': {
                                        'type': ['number', 'null'],
                                        'description': 'The total spent for a campaign',
                                    },
                                    'total_revenue': {
                                        'type': ['number', 'null'],
                                        'description': 'The total revenue for a campaign',
                                    },
                                },
                            },
                        },
                    },
                    'delivery_status': {
                        'type': ['object', 'null'],
                        'description': 'Updates on campaigns in the process of sending',
                        'properties': {
                            'enabled': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether Campaign Delivery Status is enabled for this account and target campaign',
                            },
                            'can_cancel': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether a campaign send can be canceled',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': 'The current state of a campaign delivery',
                            },
                            'emails_sent': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of emails confirmed sent for this campaign so far',
                            },
                            'emails_canceled': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of emails canceled for this campaign',
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'campaigns',
                'x-airbyte-stream-name': 'campaigns',
            },
        ),
        EntityDefinition(
            name='lists',
            stream_name='lists',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/lists',
                    action=Action.LIST,
                    description='Get information about all lists in the account',
                    query_params=[
                        'count',
                        'offset',
                        'before_date_created',
                        'since_date_created',
                        'before_campaign_last_sent',
                        'since_campaign_last_sent',
                        'email',
                        'sort_field',
                        'sort_dir',
                    ],
                    query_params_schema={
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'before_date_created': {'type': 'string', 'required': False},
                        'since_date_created': {'type': 'string', 'required': False},
                        'before_campaign_last_sent': {'type': 'string', 'required': False},
                        'since_campaign_last_sent': {'type': 'string', 'required': False},
                        'email': {'type': 'string', 'required': False},
                        'sort_field': {'type': 'string', 'required': False},
                        'sort_dir': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A collection of subscriber lists for this account',
                        'properties': {
                            'lists': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Information about a specific list',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'A string that uniquely identifies this list'},
                                        'web_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'The ID used in the Mailchimp web application',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the list',
                                        },
                                        'contact': {
                                            'type': ['object', 'null'],
                                            'description': 'Contact information displayed in campaign footers to comply with international spam laws',
                                            'properties': {
                                                'company': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The company name for the list',
                                                },
                                                'address1': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The street address for the list contact',
                                                },
                                                'address2': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The street address for the list contact',
                                                },
                                                'city': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The city for the list contact',
                                                },
                                                'state': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The state for the list contact',
                                                },
                                                'zip': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The postal or zip code for the list contact',
                                                },
                                                'country': {
                                                    'type': ['string', 'null'],
                                                    'description': 'A two-character ISO3166 country code',
                                                },
                                                'phone': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The phone number for the list contact',
                                                },
                                            },
                                        },
                                        'permission_reminder': {
                                            'type': ['string', 'null'],
                                            'description': 'The permission reminder for the list',
                                        },
                                        'use_archive_bar': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether campaigns for this list use the Archive Bar in archives by default',
                                        },
                                        'campaign_defaults': {
                                            'type': ['object', 'null'],
                                            'description': 'Default values for campaigns created for this list',
                                            'properties': {
                                                'from_name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The default from name for campaigns sent to this list',
                                                },
                                                'from_email': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The default from email for campaigns sent to this list',
                                                },
                                                'subject': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The default subject line for campaigns sent to this list',
                                                },
                                                'language': {
                                                    'type': ['string', 'null'],
                                                    'description': "The default language for this list's forms",
                                                },
                                            },
                                        },
                                        'notify_on_subscribe': {
                                            'type': ['string', 'null'],
                                            'description': 'The email address to send subscribe notifications to',
                                        },
                                        'notify_on_unsubscribe': {
                                            'type': ['string', 'null'],
                                            'description': 'The email address to send unsubscribe notifications to',
                                        },
                                        'date_created': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time that this list was created',
                                        },
                                        'list_rating': {
                                            'type': ['integer', 'null'],
                                            'description': 'An auto-generated activity score for the list (0-5)',
                                        },
                                        'email_type_option': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether the list supports multiple formats for emails',
                                        },
                                        'subscribe_url_short': {
                                            'type': ['string', 'null'],
                                            'description': "Our EepURL shortened version of this list's subscribe form",
                                        },
                                        'subscribe_url_long': {
                                            'type': ['string', 'null'],
                                            'description': "The full version of this list's subscribe form",
                                        },
                                        'beamer_address': {
                                            'type': ['string', 'null'],
                                            'description': "The list's Email Beamer address",
                                        },
                                        'visibility': {
                                            'type': ['string', 'null'],
                                            'description': 'Whether this list is public or private',
                                            'enum': ['pub', 'prv', None],
                                        },
                                        'double_optin': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether or not to require the subscriber to confirm subscription via email',
                                        },
                                        'has_welcome': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether or not this list has a welcome automation connected',
                                        },
                                        'marketing_permissions': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Whether or not the list has marketing permissions enabled',
                                        },
                                        'stats': {
                                            'type': ['object', 'null'],
                                            'description': 'Stats for the list',
                                            'properties': {
                                                'member_count': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of active members in the list',
                                                },
                                                'total_contacts': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of contacts in the list, including subscribed, unsubscribed, pending, cleaned, deleted, transactional, and those that need to be reconfirmed',
                                                },
                                                'unsubscribe_count': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of members who have unsubscribed from the list',
                                                },
                                                'cleaned_count': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of members cleaned from the list',
                                                },
                                                'member_count_since_send': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of active members in the list since the last campaign was sent',
                                                },
                                                'unsubscribe_count_since_send': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of members who have unsubscribed since the last campaign was sent',
                                                },
                                                'cleaned_count_since_send': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of members cleaned from the list since the last campaign was sent',
                                                },
                                                'campaign_count': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of campaigns in any status that use this list',
                                                },
                                                'campaign_last_sent': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'The date and time the last campaign was sent to this list',
                                                },
                                                'merge_field_count': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of merge fields for this list',
                                                },
                                                'avg_sub_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The average number of subscriptions per month for the list',
                                                },
                                                'avg_unsub_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The average number of unsubscriptions per month for the list',
                                                },
                                                'target_sub_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The target number of subscriptions per month for the list to keep it growing',
                                                },
                                                'open_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The average open rate for campaigns sent to this list',
                                                },
                                                'click_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The average click rate for campaigns sent to this list',
                                                },
                                                'last_sub_date': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'The date and time of the last time someone subscribed to this list',
                                                },
                                                'last_unsub_date': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'The date and time of the last time someone unsubscribed from this list',
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'lists',
                                    'x-airbyte-stream-name': 'lists',
                                },
                            },
                            'total_items': {'type': 'integer', 'description': 'The total number of items matching the query regardless of pagination'},
                        },
                    },
                    record_extractor='$.lists',
                    meta_extractor={'total_items': '$.total_items'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/lists/{list_id}',
                    action=Action.GET,
                    description='Get information about a specific list in your Mailchimp account',
                    path_params=['list_id'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Information about a specific list',
                        'properties': {
                            'id': {'type': 'string', 'description': 'A string that uniquely identifies this list'},
                            'web_id': {
                                'type': ['integer', 'null'],
                                'description': 'The ID used in the Mailchimp web application',
                            },
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The name of the list',
                            },
                            'contact': {
                                'type': ['object', 'null'],
                                'description': 'Contact information displayed in campaign footers to comply with international spam laws',
                                'properties': {
                                    'company': {
                                        'type': ['string', 'null'],
                                        'description': 'The company name for the list',
                                    },
                                    'address1': {
                                        'type': ['string', 'null'],
                                        'description': 'The street address for the list contact',
                                    },
                                    'address2': {
                                        'type': ['string', 'null'],
                                        'description': 'The street address for the list contact',
                                    },
                                    'city': {
                                        'type': ['string', 'null'],
                                        'description': 'The city for the list contact',
                                    },
                                    'state': {
                                        'type': ['string', 'null'],
                                        'description': 'The state for the list contact',
                                    },
                                    'zip': {
                                        'type': ['string', 'null'],
                                        'description': 'The postal or zip code for the list contact',
                                    },
                                    'country': {
                                        'type': ['string', 'null'],
                                        'description': 'A two-character ISO3166 country code',
                                    },
                                    'phone': {
                                        'type': ['string', 'null'],
                                        'description': 'The phone number for the list contact',
                                    },
                                },
                            },
                            'permission_reminder': {
                                'type': ['string', 'null'],
                                'description': 'The permission reminder for the list',
                            },
                            'use_archive_bar': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether campaigns for this list use the Archive Bar in archives by default',
                            },
                            'campaign_defaults': {
                                'type': ['object', 'null'],
                                'description': 'Default values for campaigns created for this list',
                                'properties': {
                                    'from_name': {
                                        'type': ['string', 'null'],
                                        'description': 'The default from name for campaigns sent to this list',
                                    },
                                    'from_email': {
                                        'type': ['string', 'null'],
                                        'description': 'The default from email for campaigns sent to this list',
                                    },
                                    'subject': {
                                        'type': ['string', 'null'],
                                        'description': 'The default subject line for campaigns sent to this list',
                                    },
                                    'language': {
                                        'type': ['string', 'null'],
                                        'description': "The default language for this list's forms",
                                    },
                                },
                            },
                            'notify_on_subscribe': {
                                'type': ['string', 'null'],
                                'description': 'The email address to send subscribe notifications to',
                            },
                            'notify_on_unsubscribe': {
                                'type': ['string', 'null'],
                                'description': 'The email address to send unsubscribe notifications to',
                            },
                            'date_created': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time that this list was created',
                            },
                            'list_rating': {
                                'type': ['integer', 'null'],
                                'description': 'An auto-generated activity score for the list (0-5)',
                            },
                            'email_type_option': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether the list supports multiple formats for emails',
                            },
                            'subscribe_url_short': {
                                'type': ['string', 'null'],
                                'description': "Our EepURL shortened version of this list's subscribe form",
                            },
                            'subscribe_url_long': {
                                'type': ['string', 'null'],
                                'description': "The full version of this list's subscribe form",
                            },
                            'beamer_address': {
                                'type': ['string', 'null'],
                                'description': "The list's Email Beamer address",
                            },
                            'visibility': {
                                'type': ['string', 'null'],
                                'description': 'Whether this list is public or private',
                                'enum': ['pub', 'prv', None],
                            },
                            'double_optin': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether or not to require the subscriber to confirm subscription via email',
                            },
                            'has_welcome': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether or not this list has a welcome automation connected',
                            },
                            'marketing_permissions': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether or not the list has marketing permissions enabled',
                            },
                            'stats': {
                                'type': ['object', 'null'],
                                'description': 'Stats for the list',
                                'properties': {
                                    'member_count': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of active members in the list',
                                    },
                                    'total_contacts': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of contacts in the list, including subscribed, unsubscribed, pending, cleaned, deleted, transactional, and those that need to be reconfirmed',
                                    },
                                    'unsubscribe_count': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of members who have unsubscribed from the list',
                                    },
                                    'cleaned_count': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of members cleaned from the list',
                                    },
                                    'member_count_since_send': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of active members in the list since the last campaign was sent',
                                    },
                                    'unsubscribe_count_since_send': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of members who have unsubscribed since the last campaign was sent',
                                    },
                                    'cleaned_count_since_send': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of members cleaned from the list since the last campaign was sent',
                                    },
                                    'campaign_count': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of campaigns in any status that use this list',
                                    },
                                    'campaign_last_sent': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'The date and time the last campaign was sent to this list',
                                    },
                                    'merge_field_count': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of merge fields for this list',
                                    },
                                    'avg_sub_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The average number of subscriptions per month for the list',
                                    },
                                    'avg_unsub_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The average number of unsubscriptions per month for the list',
                                    },
                                    'target_sub_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The target number of subscriptions per month for the list to keep it growing',
                                    },
                                    'open_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The average open rate for campaigns sent to this list',
                                    },
                                    'click_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The average click rate for campaigns sent to this list',
                                    },
                                    'last_sub_date': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'The date and time of the last time someone subscribed to this list',
                                    },
                                    'last_unsub_date': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'The date and time of the last time someone unsubscribed from this list',
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'lists',
                        'x-airbyte-stream-name': 'lists',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Information about a specific list',
                'properties': {
                    'id': {'type': 'string', 'description': 'A string that uniquely identifies this list'},
                    'web_id': {
                        'type': ['integer', 'null'],
                        'description': 'The ID used in the Mailchimp web application',
                    },
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the list',
                    },
                    'contact': {
                        'type': ['object', 'null'],
                        'description': 'Contact information displayed in campaign footers to comply with international spam laws',
                        'properties': {
                            'company': {
                                'type': ['string', 'null'],
                                'description': 'The company name for the list',
                            },
                            'address1': {
                                'type': ['string', 'null'],
                                'description': 'The street address for the list contact',
                            },
                            'address2': {
                                'type': ['string', 'null'],
                                'description': 'The street address for the list contact',
                            },
                            'city': {
                                'type': ['string', 'null'],
                                'description': 'The city for the list contact',
                            },
                            'state': {
                                'type': ['string', 'null'],
                                'description': 'The state for the list contact',
                            },
                            'zip': {
                                'type': ['string', 'null'],
                                'description': 'The postal or zip code for the list contact',
                            },
                            'country': {
                                'type': ['string', 'null'],
                                'description': 'A two-character ISO3166 country code',
                            },
                            'phone': {
                                'type': ['string', 'null'],
                                'description': 'The phone number for the list contact',
                            },
                        },
                    },
                    'permission_reminder': {
                        'type': ['string', 'null'],
                        'description': 'The permission reminder for the list',
                    },
                    'use_archive_bar': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether campaigns for this list use the Archive Bar in archives by default',
                    },
                    'campaign_defaults': {
                        'type': ['object', 'null'],
                        'description': 'Default values for campaigns created for this list',
                        'properties': {
                            'from_name': {
                                'type': ['string', 'null'],
                                'description': 'The default from name for campaigns sent to this list',
                            },
                            'from_email': {
                                'type': ['string', 'null'],
                                'description': 'The default from email for campaigns sent to this list',
                            },
                            'subject': {
                                'type': ['string', 'null'],
                                'description': 'The default subject line for campaigns sent to this list',
                            },
                            'language': {
                                'type': ['string', 'null'],
                                'description': "The default language for this list's forms",
                            },
                        },
                    },
                    'notify_on_subscribe': {
                        'type': ['string', 'null'],
                        'description': 'The email address to send subscribe notifications to',
                    },
                    'notify_on_unsubscribe': {
                        'type': ['string', 'null'],
                        'description': 'The email address to send unsubscribe notifications to',
                    },
                    'date_created': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time that this list was created',
                    },
                    'list_rating': {
                        'type': ['integer', 'null'],
                        'description': 'An auto-generated activity score for the list (0-5)',
                    },
                    'email_type_option': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether the list supports multiple formats for emails',
                    },
                    'subscribe_url_short': {
                        'type': ['string', 'null'],
                        'description': "Our EepURL shortened version of this list's subscribe form",
                    },
                    'subscribe_url_long': {
                        'type': ['string', 'null'],
                        'description': "The full version of this list's subscribe form",
                    },
                    'beamer_address': {
                        'type': ['string', 'null'],
                        'description': "The list's Email Beamer address",
                    },
                    'visibility': {
                        'type': ['string', 'null'],
                        'description': 'Whether this list is public or private',
                        'enum': ['pub', 'prv', None],
                    },
                    'double_optin': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether or not to require the subscriber to confirm subscription via email',
                    },
                    'has_welcome': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether or not this list has a welcome automation connected',
                    },
                    'marketing_permissions': {
                        'type': ['boolean', 'null'],
                        'description': 'Whether or not the list has marketing permissions enabled',
                    },
                    'stats': {
                        'type': ['object', 'null'],
                        'description': 'Stats for the list',
                        'properties': {
                            'member_count': {
                                'type': ['integer', 'null'],
                                'description': 'The number of active members in the list',
                            },
                            'total_contacts': {
                                'type': ['integer', 'null'],
                                'description': 'The number of contacts in the list, including subscribed, unsubscribed, pending, cleaned, deleted, transactional, and those that need to be reconfirmed',
                            },
                            'unsubscribe_count': {
                                'type': ['integer', 'null'],
                                'description': 'The number of members who have unsubscribed from the list',
                            },
                            'cleaned_count': {
                                'type': ['integer', 'null'],
                                'description': 'The number of members cleaned from the list',
                            },
                            'member_count_since_send': {
                                'type': ['integer', 'null'],
                                'description': 'The number of active members in the list since the last campaign was sent',
                            },
                            'unsubscribe_count_since_send': {
                                'type': ['integer', 'null'],
                                'description': 'The number of members who have unsubscribed since the last campaign was sent',
                            },
                            'cleaned_count_since_send': {
                                'type': ['integer', 'null'],
                                'description': 'The number of members cleaned from the list since the last campaign was sent',
                            },
                            'campaign_count': {
                                'type': ['integer', 'null'],
                                'description': 'The number of campaigns in any status that use this list',
                            },
                            'campaign_last_sent': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time the last campaign was sent to this list',
                            },
                            'merge_field_count': {
                                'type': ['integer', 'null'],
                                'description': 'The number of merge fields for this list',
                            },
                            'avg_sub_rate': {
                                'type': ['number', 'null'],
                                'description': 'The average number of subscriptions per month for the list',
                            },
                            'avg_unsub_rate': {
                                'type': ['number', 'null'],
                                'description': 'The average number of unsubscriptions per month for the list',
                            },
                            'target_sub_rate': {
                                'type': ['number', 'null'],
                                'description': 'The target number of subscriptions per month for the list to keep it growing',
                            },
                            'open_rate': {
                                'type': ['number', 'null'],
                                'description': 'The average open rate for campaigns sent to this list',
                            },
                            'click_rate': {
                                'type': ['number', 'null'],
                                'description': 'The average click rate for campaigns sent to this list',
                            },
                            'last_sub_date': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time of the last time someone subscribed to this list',
                            },
                            'last_unsub_date': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time of the last time someone unsubscribed from this list',
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'lists',
                'x-airbyte-stream-name': 'lists',
            },
        ),
        EntityDefinition(
            name='list_members',
            stream_name='list_members',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/lists/{list_id}/members',
                    action=Action.LIST,
                    description='Get information about members in a specific Mailchimp list',
                    query_params=[
                        'count',
                        'offset',
                        'email_type',
                        'status',
                        'since_timestamp_opt',
                        'before_timestamp_opt',
                        'since_last_changed',
                        'before_last_changed',
                        'unique_email_id',
                        'vip_only',
                        'interest_category_id',
                        'interest_ids',
                        'interest_match',
                        'sort_field',
                        'sort_dir',
                    ],
                    query_params_schema={
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'email_type': {'type': 'string', 'required': False},
                        'status': {'type': 'string', 'required': False},
                        'since_timestamp_opt': {'type': 'string', 'required': False},
                        'before_timestamp_opt': {'type': 'string', 'required': False},
                        'since_last_changed': {'type': 'string', 'required': False},
                        'before_last_changed': {'type': 'string', 'required': False},
                        'unique_email_id': {'type': 'string', 'required': False},
                        'vip_only': {'type': 'boolean', 'required': False},
                        'interest_category_id': {'type': 'string', 'required': False},
                        'interest_ids': {'type': 'string', 'required': False},
                        'interest_match': {'type': 'string', 'required': False},
                        'sort_field': {'type': 'string', 'required': False},
                        'sort_dir': {'type': 'string', 'required': False},
                    },
                    path_params=['list_id'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Manage members of a specific Mailchimp list',
                        'properties': {
                            'members': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Individuals who are currently or have been previously subscribed to this list',
                                    'properties': {
                                        'id': {'type': 'string', 'description': "The MD5 hash of the lowercase version of the list member's email address"},
                                        'email_address': {
                                            'type': ['string', 'null'],
                                            'description': 'Email address for a subscriber',
                                        },
                                        'unique_email_id': {
                                            'type': ['string', 'null'],
                                            'description': 'An identifier for the address across all of Mailchimp',
                                        },
                                        'contact_id': {
                                            'type': ['string', 'null'],
                                            'description': 'As Mailchimp evolves beyond email, you may eventually have contacts without email addresses',
                                        },
                                        'full_name': {
                                            'type': ['string', 'null'],
                                            'description': "The contact's full name",
                                        },
                                        'web_id': {
                                            'type': ['integer', 'null'],
                                            'description': 'The ID used in the Mailchimp web application',
                                        },
                                        'email_type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of email this member asked to get',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': "Subscriber's current status",
                                            'enum': [
                                                'subscribed',
                                                'unsubscribed',
                                                'cleaned',
                                                'pending',
                                                'transactional',
                                                'archived',
                                                None,
                                            ],
                                        },
                                        'unsubscribe_reason': {
                                            'type': ['string', 'null'],
                                            'description': "A subscriber's reason for unsubscribing",
                                        },
                                        'consents_to_one_to_one_messaging': {
                                            'type': ['boolean', 'null'],
                                            'description': 'Indicates whether a contact consents to 1:1 messaging',
                                        },
                                        'merge_fields': {
                                            'type': ['object', 'null'],
                                            'description': 'A dictionary of merge fields where the keys are the merge tags',
                                            'additionalProperties': True,
                                        },
                                        'interests': {
                                            'type': ['object', 'null'],
                                            'description': "The key of this object's properties is the ID of the interest in question",
                                            'additionalProperties': {'type': 'boolean'},
                                        },
                                        'stats': {
                                            'type': ['object', 'null'],
                                            'description': 'Open and click rates for this subscriber',
                                            'properties': {
                                                'avg_open_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': "A subscriber's average open rate",
                                                },
                                                'avg_click_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': "A subscriber's average clickthrough rate",
                                                },
                                                'ecommerce_data': {
                                                    'type': ['object', 'null'],
                                                    'description': 'Ecommerce stats for the list member if the list is attached to a store',
                                                    'properties': {
                                                        'total_revenue': {
                                                            'type': ['number', 'null'],
                                                            'description': 'The total revenue the list member has brought in',
                                                        },
                                                        'number_of_orders': {
                                                            'type': ['number', 'null'],
                                                            'description': 'The total number of orders placed by the list member',
                                                        },
                                                        'currency_code': {
                                                            'type': ['string', 'null'],
                                                            'description': 'The three-letter ISO 4217 code for the currency that the store accepts',
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        'ip_signup': {
                                            'type': ['string', 'null'],
                                            'description': 'IP address the subscriber signed up from',
                                        },
                                        'timestamp_signup': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time the subscriber signed up for the list',
                                        },
                                        'ip_opt': {
                                            'type': ['string', 'null'],
                                            'description': 'The IP address the subscriber used to confirm their opt-in status',
                                        },
                                        'timestamp_opt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time the subscriber confirmed their opt-in status',
                                        },
                                        'member_rating': {
                                            'type': ['integer', 'null'],
                                            'description': 'Star rating for this member, between 1 and 5',
                                        },
                                        'last_changed': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': "The date and time the member's info was last changed",
                                        },
                                        'language': {
                                            'type': ['string', 'null'],
                                            'description': "If set/detected, the subscriber's language",
                                        },
                                        'vip': {
                                            'type': ['boolean', 'null'],
                                            'description': 'VIP status for subscriber',
                                        },
                                        'email_client': {
                                            'type': ['string', 'null'],
                                            'description': "The list member's email client",
                                        },
                                        'location': {
                                            'type': ['object', 'null'],
                                            'description': 'Subscriber location information',
                                            'properties': {
                                                'latitude': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The location latitude',
                                                },
                                                'longitude': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The location longitude',
                                                },
                                                'gmtoff': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The time difference in hours from GMT',
                                                },
                                                'dstoff': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The offset for timezones where daylight saving time is observed',
                                                },
                                                'country_code': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The unique code for the location country',
                                                },
                                                'timezone': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The timezone for the location',
                                                },
                                                'region': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The region for the location',
                                                },
                                            },
                                        },
                                        'source': {
                                            'type': ['string', 'null'],
                                            'description': 'The source from which the subscriber was added to this list',
                                        },
                                        'tags_count': {
                                            'type': ['integer', 'null'],
                                            'description': 'The number of tags applied to this member',
                                        },
                                        'tags': {
                                            'type': ['array', 'null'],
                                            'description': 'Returns up to 50 tags applied to this member',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'id': {
                                                        'type': ['integer', 'null'],
                                                        'description': 'The tag id',
                                                    },
                                                    'name': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The name of the tag',
                                                    },
                                                },
                                            },
                                        },
                                        'list_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The list id',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'list_members',
                                    'x-airbyte-stream-name': 'list_members',
                                },
                            },
                            'list_id': {
                                'type': ['string', 'null'],
                                'description': 'The list id',
                            },
                            'total_items': {'type': 'integer', 'description': 'The total number of items matching the query regardless of pagination'},
                        },
                    },
                    record_extractor='$.members',
                    meta_extractor={'total_items': '$.total_items'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/lists/{list_id}/members/{subscriber_hash}',
                    action=Action.GET,
                    description='Get information about a specific list member',
                    path_params=['list_id', 'subscriber_hash'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                        'subscriber_hash': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Individuals who are currently or have been previously subscribed to this list',
                        'properties': {
                            'id': {'type': 'string', 'description': "The MD5 hash of the lowercase version of the list member's email address"},
                            'email_address': {
                                'type': ['string', 'null'],
                                'description': 'Email address for a subscriber',
                            },
                            'unique_email_id': {
                                'type': ['string', 'null'],
                                'description': 'An identifier for the address across all of Mailchimp',
                            },
                            'contact_id': {
                                'type': ['string', 'null'],
                                'description': 'As Mailchimp evolves beyond email, you may eventually have contacts without email addresses',
                            },
                            'full_name': {
                                'type': ['string', 'null'],
                                'description': "The contact's full name",
                            },
                            'web_id': {
                                'type': ['integer', 'null'],
                                'description': 'The ID used in the Mailchimp web application',
                            },
                            'email_type': {
                                'type': ['string', 'null'],
                                'description': 'Type of email this member asked to get',
                            },
                            'status': {
                                'type': ['string', 'null'],
                                'description': "Subscriber's current status",
                                'enum': [
                                    'subscribed',
                                    'unsubscribed',
                                    'cleaned',
                                    'pending',
                                    'transactional',
                                    'archived',
                                    None,
                                ],
                            },
                            'unsubscribe_reason': {
                                'type': ['string', 'null'],
                                'description': "A subscriber's reason for unsubscribing",
                            },
                            'consents_to_one_to_one_messaging': {
                                'type': ['boolean', 'null'],
                                'description': 'Indicates whether a contact consents to 1:1 messaging',
                            },
                            'merge_fields': {
                                'type': ['object', 'null'],
                                'description': 'A dictionary of merge fields where the keys are the merge tags',
                                'additionalProperties': True,
                            },
                            'interests': {
                                'type': ['object', 'null'],
                                'description': "The key of this object's properties is the ID of the interest in question",
                                'additionalProperties': {'type': 'boolean'},
                            },
                            'stats': {
                                'type': ['object', 'null'],
                                'description': 'Open and click rates for this subscriber',
                                'properties': {
                                    'avg_open_rate': {
                                        'type': ['number', 'null'],
                                        'description': "A subscriber's average open rate",
                                    },
                                    'avg_click_rate': {
                                        'type': ['number', 'null'],
                                        'description': "A subscriber's average clickthrough rate",
                                    },
                                    'ecommerce_data': {
                                        'type': ['object', 'null'],
                                        'description': 'Ecommerce stats for the list member if the list is attached to a store',
                                        'properties': {
                                            'total_revenue': {
                                                'type': ['number', 'null'],
                                                'description': 'The total revenue the list member has brought in',
                                            },
                                            'number_of_orders': {
                                                'type': ['number', 'null'],
                                                'description': 'The total number of orders placed by the list member',
                                            },
                                            'currency_code': {
                                                'type': ['string', 'null'],
                                                'description': 'The three-letter ISO 4217 code for the currency that the store accepts',
                                            },
                                        },
                                    },
                                },
                            },
                            'ip_signup': {
                                'type': ['string', 'null'],
                                'description': 'IP address the subscriber signed up from',
                            },
                            'timestamp_signup': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time the subscriber signed up for the list',
                            },
                            'ip_opt': {
                                'type': ['string', 'null'],
                                'description': 'The IP address the subscriber used to confirm their opt-in status',
                            },
                            'timestamp_opt': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time the subscriber confirmed their opt-in status',
                            },
                            'member_rating': {
                                'type': ['integer', 'null'],
                                'description': 'Star rating for this member, between 1 and 5',
                            },
                            'last_changed': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': "The date and time the member's info was last changed",
                            },
                            'language': {
                                'type': ['string', 'null'],
                                'description': "If set/detected, the subscriber's language",
                            },
                            'vip': {
                                'type': ['boolean', 'null'],
                                'description': 'VIP status for subscriber',
                            },
                            'email_client': {
                                'type': ['string', 'null'],
                                'description': "The list member's email client",
                            },
                            'location': {
                                'type': ['object', 'null'],
                                'description': 'Subscriber location information',
                                'properties': {
                                    'latitude': {
                                        'type': ['number', 'null'],
                                        'description': 'The location latitude',
                                    },
                                    'longitude': {
                                        'type': ['number', 'null'],
                                        'description': 'The location longitude',
                                    },
                                    'gmtoff': {
                                        'type': ['integer', 'null'],
                                        'description': 'The time difference in hours from GMT',
                                    },
                                    'dstoff': {
                                        'type': ['integer', 'null'],
                                        'description': 'The offset for timezones where daylight saving time is observed',
                                    },
                                    'country_code': {
                                        'type': ['string', 'null'],
                                        'description': 'The unique code for the location country',
                                    },
                                    'timezone': {
                                        'type': ['string', 'null'],
                                        'description': 'The timezone for the location',
                                    },
                                    'region': {
                                        'type': ['string', 'null'],
                                        'description': 'The region for the location',
                                    },
                                },
                            },
                            'source': {
                                'type': ['string', 'null'],
                                'description': 'The source from which the subscriber was added to this list',
                            },
                            'tags_count': {
                                'type': ['integer', 'null'],
                                'description': 'The number of tags applied to this member',
                            },
                            'tags': {
                                'type': ['array', 'null'],
                                'description': 'Returns up to 50 tags applied to this member',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {
                                            'type': ['integer', 'null'],
                                            'description': 'The tag id',
                                        },
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the tag',
                                        },
                                    },
                                },
                            },
                            'list_id': {
                                'type': ['string', 'null'],
                                'description': 'The list id',
                            },
                        },
                        'x-airbyte-entity-name': 'list_members',
                        'x-airbyte-stream-name': 'list_members',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Individuals who are currently or have been previously subscribed to this list',
                'properties': {
                    'id': {'type': 'string', 'description': "The MD5 hash of the lowercase version of the list member's email address"},
                    'email_address': {
                        'type': ['string', 'null'],
                        'description': 'Email address for a subscriber',
                    },
                    'unique_email_id': {
                        'type': ['string', 'null'],
                        'description': 'An identifier for the address across all of Mailchimp',
                    },
                    'contact_id': {
                        'type': ['string', 'null'],
                        'description': 'As Mailchimp evolves beyond email, you may eventually have contacts without email addresses',
                    },
                    'full_name': {
                        'type': ['string', 'null'],
                        'description': "The contact's full name",
                    },
                    'web_id': {
                        'type': ['integer', 'null'],
                        'description': 'The ID used in the Mailchimp web application',
                    },
                    'email_type': {
                        'type': ['string', 'null'],
                        'description': 'Type of email this member asked to get',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': "Subscriber's current status",
                        'enum': [
                            'subscribed',
                            'unsubscribed',
                            'cleaned',
                            'pending',
                            'transactional',
                            'archived',
                            None,
                        ],
                    },
                    'unsubscribe_reason': {
                        'type': ['string', 'null'],
                        'description': "A subscriber's reason for unsubscribing",
                    },
                    'consents_to_one_to_one_messaging': {
                        'type': ['boolean', 'null'],
                        'description': 'Indicates whether a contact consents to 1:1 messaging',
                    },
                    'merge_fields': {
                        'type': ['object', 'null'],
                        'description': 'A dictionary of merge fields where the keys are the merge tags',
                        'additionalProperties': True,
                    },
                    'interests': {
                        'type': ['object', 'null'],
                        'description': "The key of this object's properties is the ID of the interest in question",
                        'additionalProperties': {'type': 'boolean'},
                    },
                    'stats': {
                        'type': ['object', 'null'],
                        'description': 'Open and click rates for this subscriber',
                        'properties': {
                            'avg_open_rate': {
                                'type': ['number', 'null'],
                                'description': "A subscriber's average open rate",
                            },
                            'avg_click_rate': {
                                'type': ['number', 'null'],
                                'description': "A subscriber's average clickthrough rate",
                            },
                            'ecommerce_data': {
                                'type': ['object', 'null'],
                                'description': 'Ecommerce stats for the list member if the list is attached to a store',
                                'properties': {
                                    'total_revenue': {
                                        'type': ['number', 'null'],
                                        'description': 'The total revenue the list member has brought in',
                                    },
                                    'number_of_orders': {
                                        'type': ['number', 'null'],
                                        'description': 'The total number of orders placed by the list member',
                                    },
                                    'currency_code': {
                                        'type': ['string', 'null'],
                                        'description': 'The three-letter ISO 4217 code for the currency that the store accepts',
                                    },
                                },
                            },
                        },
                    },
                    'ip_signup': {
                        'type': ['string', 'null'],
                        'description': 'IP address the subscriber signed up from',
                    },
                    'timestamp_signup': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time the subscriber signed up for the list',
                    },
                    'ip_opt': {
                        'type': ['string', 'null'],
                        'description': 'The IP address the subscriber used to confirm their opt-in status',
                    },
                    'timestamp_opt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time the subscriber confirmed their opt-in status',
                    },
                    'member_rating': {
                        'type': ['integer', 'null'],
                        'description': 'Star rating for this member, between 1 and 5',
                    },
                    'last_changed': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': "The date and time the member's info was last changed",
                    },
                    'language': {
                        'type': ['string', 'null'],
                        'description': "If set/detected, the subscriber's language",
                    },
                    'vip': {
                        'type': ['boolean', 'null'],
                        'description': 'VIP status for subscriber',
                    },
                    'email_client': {
                        'type': ['string', 'null'],
                        'description': "The list member's email client",
                    },
                    'location': {
                        'type': ['object', 'null'],
                        'description': 'Subscriber location information',
                        'properties': {
                            'latitude': {
                                'type': ['number', 'null'],
                                'description': 'The location latitude',
                            },
                            'longitude': {
                                'type': ['number', 'null'],
                                'description': 'The location longitude',
                            },
                            'gmtoff': {
                                'type': ['integer', 'null'],
                                'description': 'The time difference in hours from GMT',
                            },
                            'dstoff': {
                                'type': ['integer', 'null'],
                                'description': 'The offset for timezones where daylight saving time is observed',
                            },
                            'country_code': {
                                'type': ['string', 'null'],
                                'description': 'The unique code for the location country',
                            },
                            'timezone': {
                                'type': ['string', 'null'],
                                'description': 'The timezone for the location',
                            },
                            'region': {
                                'type': ['string', 'null'],
                                'description': 'The region for the location',
                            },
                        },
                    },
                    'source': {
                        'type': ['string', 'null'],
                        'description': 'The source from which the subscriber was added to this list',
                    },
                    'tags_count': {
                        'type': ['integer', 'null'],
                        'description': 'The number of tags applied to this member',
                    },
                    'tags': {
                        'type': ['array', 'null'],
                        'description': 'Returns up to 50 tags applied to this member',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['integer', 'null'],
                                    'description': 'The tag id',
                                },
                                'name': {
                                    'type': ['string', 'null'],
                                    'description': 'The name of the tag',
                                },
                            },
                        },
                    },
                    'list_id': {
                        'type': ['string', 'null'],
                        'description': 'The list id',
                    },
                },
                'x-airbyte-entity-name': 'list_members',
                'x-airbyte-stream-name': 'list_members',
            },
        ),
        EntityDefinition(
            name='reports',
            stream_name='reports',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/reports',
                    action=Action.LIST,
                    description='Get campaign reports',
                    query_params=[
                        'count',
                        'offset',
                        'type',
                        'before_send_time',
                        'since_send_time',
                    ],
                    query_params_schema={
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'type': {'type': 'string', 'required': False},
                        'before_send_time': {'type': 'string', 'required': False},
                        'since_send_time': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A list of reports containing campaigns marked as Sent',
                        'properties': {
                            'reports': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Report details about a sent campaign',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'A string that uniquely identifies this campaign'},
                                        'campaign_title': {
                                            'type': ['string', 'null'],
                                            'description': 'The title of the campaign',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'The type of campaign',
                                        },
                                        'list_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The unique list id',
                                        },
                                        'list_is_active': {
                                            'type': ['boolean', 'null'],
                                            'description': 'The status of the list used',
                                        },
                                        'list_name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the list',
                                        },
                                        'subject_line': {
                                            'type': ['string', 'null'],
                                            'description': 'The subject line for the campaign',
                                        },
                                        'preview_text': {
                                            'type': ['string', 'null'],
                                            'description': 'The preview text for the campaign',
                                        },
                                        'emails_sent': {
                                            'type': ['integer', 'null'],
                                            'description': 'The total number of emails sent for this campaign',
                                        },
                                        'abuse_reports': {
                                            'type': ['integer', 'null'],
                                            'description': 'The number of abuse reports generated for this campaign',
                                        },
                                        'unsubscribed': {
                                            'type': ['integer', 'null'],
                                            'description': 'The total number of unsubscribed members for this campaign',
                                        },
                                        'send_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time a campaign was sent',
                                        },
                                        'rss_last_send': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'For RSS campaigns, the date and time of the last send',
                                        },
                                        'bounces': {
                                            'type': ['object', 'null'],
                                            'description': 'An object describing the bounce summary for the campaign',
                                            'properties': {
                                                'hard_bounces': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of hard bounced email addresses',
                                                },
                                                'soft_bounces': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of soft bounced email addresses',
                                                },
                                                'syntax_errors': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of addresses that were syntax-related bounces',
                                                },
                                            },
                                        },
                                        'forwards': {
                                            'type': ['object', 'null'],
                                            'description': 'An object describing the forwards and forward activity for the campaign',
                                            'properties': {
                                                'forwards_count': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'How many times the campaign has been forwarded',
                                                },
                                                'forwards_opens': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'How many times the forwarded campaign has been opened',
                                                },
                                            },
                                        },
                                        'opens': {
                                            'type': ['object', 'null'],
                                            'description': 'An object describing the open activity for the campaign',
                                            'properties': {
                                                'opens_total': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of opens for a campaign',
                                                },
                                                'unique_opens': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of unique opens',
                                                },
                                                'open_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The number of unique opens divided by the total number of successful deliveries',
                                                },
                                                'last_open': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'The date and time of the last recorded open',
                                                },
                                            },
                                        },
                                        'clicks': {
                                            'type': ['object', 'null'],
                                            'description': 'An object describing the click activity for the campaign',
                                            'properties': {
                                                'clicks_total': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of clicks for the campaign',
                                                },
                                                'unique_clicks': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of unique clicks for links across a campaign',
                                                },
                                                'unique_subscriber_clicks': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of subscribers who clicked on a campaign',
                                                },
                                                'click_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The number of unique clicks divided by the total number of successful deliveries',
                                                },
                                                'last_click': {
                                                    'type': ['string', 'null'],
                                                    'format': 'date-time',
                                                    'description': 'The date and time of the last recorded click for the campaign',
                                                },
                                            },
                                        },
                                        'facebook_likes': {
                                            'type': ['object', 'null'],
                                            'description': 'An object describing campaign engagement on Facebook',
                                            'properties': {
                                                'recipient_likes': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of recipients who liked the campaign on Facebook',
                                                },
                                                'unique_likes': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of unique likes',
                                                },
                                                'facebook_likes': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of Facebook likes for the campaign',
                                                },
                                            },
                                        },
                                        'industry_stats': {
                                            'type': ['object', 'null'],
                                            'description': 'The average campaign statistics for your industry',
                                            'properties': {
                                                'type': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The type of business industry associated with your account',
                                                },
                                                'open_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The industry open rate',
                                                },
                                                'click_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The industry click rate',
                                                },
                                                'bounce_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The industry bounce rate',
                                                },
                                                'unopen_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The industry unopened rate',
                                                },
                                                'unsub_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The industry unsubscribe rate',
                                                },
                                                'abuse_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The industry abuse rate',
                                                },
                                            },
                                        },
                                        'list_stats': {
                                            'type': ['object', 'null'],
                                            'description': 'The average campaign statistics for your list',
                                            'properties': {
                                                'sub_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The average number of subscriptions per month for the list',
                                                },
                                                'unsub_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The average number of unsubscriptions per month for the list',
                                                },
                                                'open_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The average open rate for campaigns sent to this list',
                                                },
                                                'click_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The average click rate for campaigns sent to this list',
                                                },
                                            },
                                        },
                                        'ecommerce': {
                                            'type': ['object', 'null'],
                                            'description': 'E-Commerce stats for a campaign',
                                            'properties': {
                                                'total_orders': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total orders for a campaign',
                                                },
                                                'total_spent': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The total spent for a campaign',
                                                },
                                                'total_revenue': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The total revenue for a campaign',
                                                },
                                            },
                                        },
                                        'delivery_status': {
                                            'type': ['object', 'null'],
                                            'description': 'Updates on campaigns in the process of sending',
                                            'properties': {
                                                'enabled': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether Campaign Delivery Status is enabled for this account and target campaign',
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'reports',
                                    'x-airbyte-stream-name': 'reports',
                                },
                            },
                            'total_items': {'type': 'integer', 'description': 'The total number of items matching the query regardless of pagination'},
                        },
                    },
                    record_extractor='$.reports',
                    meta_extractor={'total_items': '$.total_items'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/reports/{campaign_id}',
                    action=Action.GET,
                    description='Get report details for a specific sent campaign',
                    path_params=['campaign_id'],
                    path_params_schema={
                        'campaign_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Report details about a sent campaign',
                        'properties': {
                            'id': {'type': 'string', 'description': 'A string that uniquely identifies this campaign'},
                            'campaign_title': {
                                'type': ['string', 'null'],
                                'description': 'The title of the campaign',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'The type of campaign',
                            },
                            'list_id': {
                                'type': ['string', 'null'],
                                'description': 'The unique list id',
                            },
                            'list_is_active': {
                                'type': ['boolean', 'null'],
                                'description': 'The status of the list used',
                            },
                            'list_name': {
                                'type': ['string', 'null'],
                                'description': 'The name of the list',
                            },
                            'subject_line': {
                                'type': ['string', 'null'],
                                'description': 'The subject line for the campaign',
                            },
                            'preview_text': {
                                'type': ['string', 'null'],
                                'description': 'The preview text for the campaign',
                            },
                            'emails_sent': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of emails sent for this campaign',
                            },
                            'abuse_reports': {
                                'type': ['integer', 'null'],
                                'description': 'The number of abuse reports generated for this campaign',
                            },
                            'unsubscribed': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of unsubscribed members for this campaign',
                            },
                            'send_time': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time a campaign was sent',
                            },
                            'rss_last_send': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'For RSS campaigns, the date and time of the last send',
                            },
                            'bounces': {
                                'type': ['object', 'null'],
                                'description': 'An object describing the bounce summary for the campaign',
                                'properties': {
                                    'hard_bounces': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total number of hard bounced email addresses',
                                    },
                                    'soft_bounces': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total number of soft bounced email addresses',
                                    },
                                    'syntax_errors': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total number of addresses that were syntax-related bounces',
                                    },
                                },
                            },
                            'forwards': {
                                'type': ['object', 'null'],
                                'description': 'An object describing the forwards and forward activity for the campaign',
                                'properties': {
                                    'forwards_count': {
                                        'type': ['integer', 'null'],
                                        'description': 'How many times the campaign has been forwarded',
                                    },
                                    'forwards_opens': {
                                        'type': ['integer', 'null'],
                                        'description': 'How many times the forwarded campaign has been opened',
                                    },
                                },
                            },
                            'opens': {
                                'type': ['object', 'null'],
                                'description': 'An object describing the open activity for the campaign',
                                'properties': {
                                    'opens_total': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total number of opens for a campaign',
                                    },
                                    'unique_opens': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total number of unique opens',
                                    },
                                    'open_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The number of unique opens divided by the total number of successful deliveries',
                                    },
                                    'last_open': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'The date and time of the last recorded open',
                                    },
                                },
                            },
                            'clicks': {
                                'type': ['object', 'null'],
                                'description': 'An object describing the click activity for the campaign',
                                'properties': {
                                    'clicks_total': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total number of clicks for the campaign',
                                    },
                                    'unique_clicks': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total number of unique clicks for links across a campaign',
                                    },
                                    'unique_subscriber_clicks': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total number of subscribers who clicked on a campaign',
                                    },
                                    'click_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The number of unique clicks divided by the total number of successful deliveries',
                                    },
                                    'last_click': {
                                        'type': ['string', 'null'],
                                        'format': 'date-time',
                                        'description': 'The date and time of the last recorded click for the campaign',
                                    },
                                },
                            },
                            'facebook_likes': {
                                'type': ['object', 'null'],
                                'description': 'An object describing campaign engagement on Facebook',
                                'properties': {
                                    'recipient_likes': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of recipients who liked the campaign on Facebook',
                                    },
                                    'unique_likes': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of unique likes',
                                    },
                                    'facebook_likes': {
                                        'type': ['integer', 'null'],
                                        'description': 'The number of Facebook likes for the campaign',
                                    },
                                },
                            },
                            'industry_stats': {
                                'type': ['object', 'null'],
                                'description': 'The average campaign statistics for your industry',
                                'properties': {
                                    'type': {
                                        'type': ['string', 'null'],
                                        'description': 'The type of business industry associated with your account',
                                    },
                                    'open_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The industry open rate',
                                    },
                                    'click_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The industry click rate',
                                    },
                                    'bounce_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The industry bounce rate',
                                    },
                                    'unopen_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The industry unopened rate',
                                    },
                                    'unsub_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The industry unsubscribe rate',
                                    },
                                    'abuse_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The industry abuse rate',
                                    },
                                },
                            },
                            'list_stats': {
                                'type': ['object', 'null'],
                                'description': 'The average campaign statistics for your list',
                                'properties': {
                                    'sub_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The average number of subscriptions per month for the list',
                                    },
                                    'unsub_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The average number of unsubscriptions per month for the list',
                                    },
                                    'open_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The average open rate for campaigns sent to this list',
                                    },
                                    'click_rate': {
                                        'type': ['number', 'null'],
                                        'description': 'The average click rate for campaigns sent to this list',
                                    },
                                },
                            },
                            'ecommerce': {
                                'type': ['object', 'null'],
                                'description': 'E-Commerce stats for a campaign',
                                'properties': {
                                    'total_orders': {
                                        'type': ['integer', 'null'],
                                        'description': 'The total orders for a campaign',
                                    },
                                    'total_spent': {
                                        'type': ['number', 'null'],
                                        'description': 'The total spent for a campaign',
                                    },
                                    'total_revenue': {
                                        'type': ['number', 'null'],
                                        'description': 'The total revenue for a campaign',
                                    },
                                },
                            },
                            'delivery_status': {
                                'type': ['object', 'null'],
                                'description': 'Updates on campaigns in the process of sending',
                                'properties': {
                                    'enabled': {
                                        'type': ['boolean', 'null'],
                                        'description': 'Whether Campaign Delivery Status is enabled for this account and target campaign',
                                    },
                                },
                            },
                        },
                        'x-airbyte-entity-name': 'reports',
                        'x-airbyte-stream-name': 'reports',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Report details about a sent campaign',
                'properties': {
                    'id': {'type': 'string', 'description': 'A string that uniquely identifies this campaign'},
                    'campaign_title': {
                        'type': ['string', 'null'],
                        'description': 'The title of the campaign',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'The type of campaign',
                    },
                    'list_id': {
                        'type': ['string', 'null'],
                        'description': 'The unique list id',
                    },
                    'list_is_active': {
                        'type': ['boolean', 'null'],
                        'description': 'The status of the list used',
                    },
                    'list_name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the list',
                    },
                    'subject_line': {
                        'type': ['string', 'null'],
                        'description': 'The subject line for the campaign',
                    },
                    'preview_text': {
                        'type': ['string', 'null'],
                        'description': 'The preview text for the campaign',
                    },
                    'emails_sent': {
                        'type': ['integer', 'null'],
                        'description': 'The total number of emails sent for this campaign',
                    },
                    'abuse_reports': {
                        'type': ['integer', 'null'],
                        'description': 'The number of abuse reports generated for this campaign',
                    },
                    'unsubscribed': {
                        'type': ['integer', 'null'],
                        'description': 'The total number of unsubscribed members for this campaign',
                    },
                    'send_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time a campaign was sent',
                    },
                    'rss_last_send': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'For RSS campaigns, the date and time of the last send',
                    },
                    'bounces': {
                        'type': ['object', 'null'],
                        'description': 'An object describing the bounce summary for the campaign',
                        'properties': {
                            'hard_bounces': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of hard bounced email addresses',
                            },
                            'soft_bounces': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of soft bounced email addresses',
                            },
                            'syntax_errors': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of addresses that were syntax-related bounces',
                            },
                        },
                    },
                    'forwards': {
                        'type': ['object', 'null'],
                        'description': 'An object describing the forwards and forward activity for the campaign',
                        'properties': {
                            'forwards_count': {
                                'type': ['integer', 'null'],
                                'description': 'How many times the campaign has been forwarded',
                            },
                            'forwards_opens': {
                                'type': ['integer', 'null'],
                                'description': 'How many times the forwarded campaign has been opened',
                            },
                        },
                    },
                    'opens': {
                        'type': ['object', 'null'],
                        'description': 'An object describing the open activity for the campaign',
                        'properties': {
                            'opens_total': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of opens for a campaign',
                            },
                            'unique_opens': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of unique opens',
                            },
                            'open_rate': {
                                'type': ['number', 'null'],
                                'description': 'The number of unique opens divided by the total number of successful deliveries',
                            },
                            'last_open': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time of the last recorded open',
                            },
                        },
                    },
                    'clicks': {
                        'type': ['object', 'null'],
                        'description': 'An object describing the click activity for the campaign',
                        'properties': {
                            'clicks_total': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of clicks for the campaign',
                            },
                            'unique_clicks': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of unique clicks for links across a campaign',
                            },
                            'unique_subscriber_clicks': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of subscribers who clicked on a campaign',
                            },
                            'click_rate': {
                                'type': ['number', 'null'],
                                'description': 'The number of unique clicks divided by the total number of successful deliveries',
                            },
                            'last_click': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time of the last recorded click for the campaign',
                            },
                        },
                    },
                    'facebook_likes': {
                        'type': ['object', 'null'],
                        'description': 'An object describing campaign engagement on Facebook',
                        'properties': {
                            'recipient_likes': {
                                'type': ['integer', 'null'],
                                'description': 'The number of recipients who liked the campaign on Facebook',
                            },
                            'unique_likes': {
                                'type': ['integer', 'null'],
                                'description': 'The number of unique likes',
                            },
                            'facebook_likes': {
                                'type': ['integer', 'null'],
                                'description': 'The number of Facebook likes for the campaign',
                            },
                        },
                    },
                    'industry_stats': {
                        'type': ['object', 'null'],
                        'description': 'The average campaign statistics for your industry',
                        'properties': {
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'The type of business industry associated with your account',
                            },
                            'open_rate': {
                                'type': ['number', 'null'],
                                'description': 'The industry open rate',
                            },
                            'click_rate': {
                                'type': ['number', 'null'],
                                'description': 'The industry click rate',
                            },
                            'bounce_rate': {
                                'type': ['number', 'null'],
                                'description': 'The industry bounce rate',
                            },
                            'unopen_rate': {
                                'type': ['number', 'null'],
                                'description': 'The industry unopened rate',
                            },
                            'unsub_rate': {
                                'type': ['number', 'null'],
                                'description': 'The industry unsubscribe rate',
                            },
                            'abuse_rate': {
                                'type': ['number', 'null'],
                                'description': 'The industry abuse rate',
                            },
                        },
                    },
                    'list_stats': {
                        'type': ['object', 'null'],
                        'description': 'The average campaign statistics for your list',
                        'properties': {
                            'sub_rate': {
                                'type': ['number', 'null'],
                                'description': 'The average number of subscriptions per month for the list',
                            },
                            'unsub_rate': {
                                'type': ['number', 'null'],
                                'description': 'The average number of unsubscriptions per month for the list',
                            },
                            'open_rate': {
                                'type': ['number', 'null'],
                                'description': 'The average open rate for campaigns sent to this list',
                            },
                            'click_rate': {
                                'type': ['number', 'null'],
                                'description': 'The average click rate for campaigns sent to this list',
                            },
                        },
                    },
                    'ecommerce': {
                        'type': ['object', 'null'],
                        'description': 'E-Commerce stats for a campaign',
                        'properties': {
                            'total_orders': {
                                'type': ['integer', 'null'],
                                'description': 'The total orders for a campaign',
                            },
                            'total_spent': {
                                'type': ['number', 'null'],
                                'description': 'The total spent for a campaign',
                            },
                            'total_revenue': {
                                'type': ['number', 'null'],
                                'description': 'The total revenue for a campaign',
                            },
                        },
                    },
                    'delivery_status': {
                        'type': ['object', 'null'],
                        'description': 'Updates on campaigns in the process of sending',
                        'properties': {
                            'enabled': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether Campaign Delivery Status is enabled for this account and target campaign',
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'reports',
                'x-airbyte-stream-name': 'reports',
            },
        ),
        EntityDefinition(
            name='email_activity',
            stream_name='email_activity',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/reports/{campaign_id}/email-activity',
                    action=Action.LIST,
                    description="Get a list of member's subscriber activity in a specific campaign",
                    query_params=['count', 'offset', 'since'],
                    query_params_schema={
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'since': {'type': 'string', 'required': False},
                    },
                    path_params=['campaign_id'],
                    path_params_schema={
                        'campaign_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': "A list of member's subscriber activity in a specific campaign",
                        'properties': {
                            'emails': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A summary of the email activity for a campaign',
                                    'properties': {
                                        'campaign_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The unique id for the campaign',
                                        },
                                        'list_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The unique id for the list',
                                        },
                                        'list_is_active': {
                                            'type': ['boolean', 'null'],
                                            'description': 'The status of the list used',
                                        },
                                        'email_id': {
                                            'type': ['string', 'null'],
                                            'description': "The MD5 hash of the lowercase version of the list member's email address",
                                        },
                                        'email_address': {
                                            'type': ['string', 'null'],
                                            'description': 'Email address for a subscriber',
                                        },
                                        'activity': {
                                            'type': ['array', 'null'],
                                            'description': 'An array of objects, each showing an interaction with the email',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'action': {
                                                        'type': ['string', 'null'],
                                                        'description': 'One of the following actions open, click, or bounce',
                                                    },
                                                    'timestamp': {
                                                        'type': ['string', 'null'],
                                                        'format': 'date-time',
                                                        'description': 'The date and time recorded for the action',
                                                    },
                                                    'url': {
                                                        'type': ['string', 'null'],
                                                        'description': 'If the action is a click, the URL on which the member clicked',
                                                    },
                                                    'type': {
                                                        'type': ['string', 'null'],
                                                        'description': 'If the action is a bounce, the type of bounce received hard, soft, or blocked',
                                                    },
                                                    'ip': {
                                                        'type': ['string', 'null'],
                                                        'description': 'The IP address recorded for the action',
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'email_activity',
                                    'x-airbyte-stream-name': 'email_activity',
                                },
                            },
                            'campaign_id': {
                                'type': ['string', 'null'],
                                'description': 'The unique id for the campaign',
                            },
                            'total_items': {'type': 'integer', 'description': 'The total number of items matching the query regardless of pagination'},
                        },
                    },
                    record_extractor='$.emails',
                    meta_extractor={'total_items': '$.total_items'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A summary of the email activity for a campaign',
                'properties': {
                    'campaign_id': {
                        'type': ['string', 'null'],
                        'description': 'The unique id for the campaign',
                    },
                    'list_id': {
                        'type': ['string', 'null'],
                        'description': 'The unique id for the list',
                    },
                    'list_is_active': {
                        'type': ['boolean', 'null'],
                        'description': 'The status of the list used',
                    },
                    'email_id': {
                        'type': ['string', 'null'],
                        'description': "The MD5 hash of the lowercase version of the list member's email address",
                    },
                    'email_address': {
                        'type': ['string', 'null'],
                        'description': 'Email address for a subscriber',
                    },
                    'activity': {
                        'type': ['array', 'null'],
                        'description': 'An array of objects, each showing an interaction with the email',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'action': {
                                    'type': ['string', 'null'],
                                    'description': 'One of the following actions open, click, or bounce',
                                },
                                'timestamp': {
                                    'type': ['string', 'null'],
                                    'format': 'date-time',
                                    'description': 'The date and time recorded for the action',
                                },
                                'url': {
                                    'type': ['string', 'null'],
                                    'description': 'If the action is a click, the URL on which the member clicked',
                                },
                                'type': {
                                    'type': ['string', 'null'],
                                    'description': 'If the action is a bounce, the type of bounce received hard, soft, or blocked',
                                },
                                'ip': {
                                    'type': ['string', 'null'],
                                    'description': 'The IP address recorded for the action',
                                },
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'email_activity',
                'x-airbyte-stream-name': 'email_activity',
            },
        ),
        EntityDefinition(
            name='automations',
            stream_name='automations',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/automations',
                    action=Action.LIST,
                    description="Get a summary of an account's classic automations",
                    query_params=[
                        'count',
                        'offset',
                        'before_create_time',
                        'since_create_time',
                        'before_start_time',
                        'since_start_time',
                        'status',
                    ],
                    query_params_schema={
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'before_create_time': {'type': 'string', 'required': False},
                        'since_create_time': {'type': 'string', 'required': False},
                        'before_start_time': {'type': 'string', 'required': False},
                        'since_start_time': {'type': 'string', 'required': False},
                        'status': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A summary of the Automations for an account',
                        'properties': {
                            'automations': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': "A summary of an individual Automation workflow's settings and content",
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'A string that uniquely identifies an Automation workflow'},
                                        'create_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time the Automation was created',
                                        },
                                        'start_time': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time the Automation was started',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': 'The current status of the Automation',
                                            'enum': [
                                                'save',
                                                'paused',
                                                'sending',
                                                None,
                                            ],
                                        },
                                        'emails_sent': {
                                            'type': ['integer', 'null'],
                                            'description': 'The total number of emails sent for the Automation',
                                        },
                                        'recipients': {
                                            'type': ['object', 'null'],
                                            'description': 'List settings for the Automation',
                                            'properties': {
                                                'list_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The unique list id',
                                                },
                                                'list_is_active': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'The status of the list used',
                                                },
                                                'list_name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The name of the list',
                                                },
                                                'segment_opts': {
                                                    'type': ['object', 'null'],
                                                    'description': 'An object representing all segmentation options',
                                                    'properties': {
                                                        'saved_segment_id': {
                                                            'type': ['integer', 'null'],
                                                            'description': 'The id for an existing saved segment',
                                                        },
                                                        'match': {
                                                            'type': ['string', 'null'],
                                                            'description': 'Segment match type',
                                                        },
                                                        'conditions': {
                                                            'type': ['array', 'null'],
                                                            'description': 'Segment match conditions',
                                                            'items': {'type': 'object', 'additionalProperties': True},
                                                        },
                                                    },
                                                },
                                                'store_id': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The id of the store',
                                                },
                                            },
                                        },
                                        'settings': {
                                            'type': ['object', 'null'],
                                            'description': 'The settings for the Automation workflow',
                                            'properties': {
                                                'title': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The title of the Automation',
                                                },
                                                'from_name': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The from name for the Automation',
                                                },
                                                'reply_to': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The reply-to email address for the Automation',
                                                },
                                                'use_conversation': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether to use Mailchimp Conversation feature',
                                                },
                                                'to_name': {
                                                    'type': ['string', 'null'],
                                                    'description': "The Automation's custom to name",
                                                },
                                                'authenticate': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether Mailchimp authenticated the Automation',
                                                },
                                                'auto_footer': {
                                                    'type': ['boolean', 'null'],
                                                    'description': "Whether to automatically append Mailchimp's default footer",
                                                },
                                                'inline_css': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether to automatically inline the CSS',
                                                },
                                            },
                                        },
                                        'tracking': {
                                            'type': ['object', 'null'],
                                            'description': 'The tracking options for the Automation',
                                            'properties': {
                                                'opens': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether to track opens',
                                                },
                                                'html_clicks': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether to track clicks in the HTML version',
                                                },
                                                'text_clicks': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether to track clicks in the plain-text version',
                                                },
                                                'goal_tracking': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether to enable Goal tracking',
                                                },
                                                'ecomm360': {
                                                    'type': ['boolean', 'null'],
                                                    'description': 'Whether to enable eCommerce360 tracking',
                                                },
                                                'google_analytics': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The custom slug for Google Analytics tracking',
                                                },
                                                'clicktale': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The custom slug for ClickTale tracking',
                                                },
                                            },
                                        },
                                        'report_summary': {
                                            'type': ['object', 'null'],
                                            'description': 'A summary of opens and clicks for sent campaigns',
                                            'properties': {
                                                'opens': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of opens for a campaign',
                                                },
                                                'unique_opens': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of unique opens',
                                                },
                                                'open_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The number of unique opens divided by the total number of successful deliveries',
                                                },
                                                'clicks': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The total number of clicks for an campaign',
                                                },
                                                'subscriber_clicks': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The number of unique clicks',
                                                },
                                                'click_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The number of unique clicks divided by the total number of successful deliveries',
                                                },
                                            },
                                        },
                                    },
                                    'x-airbyte-entity-name': 'automations',
                                    'x-airbyte-stream-name': 'automations',
                                },
                            },
                            'total_items': {'type': 'integer', 'description': 'The total number of items matching the query regardless of pagination'},
                        },
                    },
                    record_extractor='$.automations',
                    meta_extractor={'total_items': '$.total_items'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': "A summary of an individual Automation workflow's settings and content",
                'properties': {
                    'id': {'type': 'string', 'description': 'A string that uniquely identifies an Automation workflow'},
                    'create_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time the Automation was created',
                    },
                    'start_time': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time the Automation was started',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': 'The current status of the Automation',
                        'enum': [
                            'save',
                            'paused',
                            'sending',
                            None,
                        ],
                    },
                    'emails_sent': {
                        'type': ['integer', 'null'],
                        'description': 'The total number of emails sent for the Automation',
                    },
                    'recipients': {
                        'type': ['object', 'null'],
                        'description': 'List settings for the Automation',
                        'properties': {
                            'list_id': {
                                'type': ['string', 'null'],
                                'description': 'The unique list id',
                            },
                            'list_is_active': {
                                'type': ['boolean', 'null'],
                                'description': 'The status of the list used',
                            },
                            'list_name': {
                                'type': ['string', 'null'],
                                'description': 'The name of the list',
                            },
                            'segment_opts': {
                                'type': ['object', 'null'],
                                'description': 'An object representing all segmentation options',
                                'properties': {
                                    'saved_segment_id': {
                                        'type': ['integer', 'null'],
                                        'description': 'The id for an existing saved segment',
                                    },
                                    'match': {
                                        'type': ['string', 'null'],
                                        'description': 'Segment match type',
                                    },
                                    'conditions': {
                                        'type': ['array', 'null'],
                                        'description': 'Segment match conditions',
                                        'items': {'type': 'object', 'additionalProperties': True},
                                    },
                                },
                            },
                            'store_id': {
                                'type': ['string', 'null'],
                                'description': 'The id of the store',
                            },
                        },
                    },
                    'settings': {
                        'type': ['object', 'null'],
                        'description': 'The settings for the Automation workflow',
                        'properties': {
                            'title': {
                                'type': ['string', 'null'],
                                'description': 'The title of the Automation',
                            },
                            'from_name': {
                                'type': ['string', 'null'],
                                'description': 'The from name for the Automation',
                            },
                            'reply_to': {
                                'type': ['string', 'null'],
                                'description': 'The reply-to email address for the Automation',
                            },
                            'use_conversation': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to use Mailchimp Conversation feature',
                            },
                            'to_name': {
                                'type': ['string', 'null'],
                                'description': "The Automation's custom to name",
                            },
                            'authenticate': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether Mailchimp authenticated the Automation',
                            },
                            'auto_footer': {
                                'type': ['boolean', 'null'],
                                'description': "Whether to automatically append Mailchimp's default footer",
                            },
                            'inline_css': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to automatically inline the CSS',
                            },
                        },
                    },
                    'tracking': {
                        'type': ['object', 'null'],
                        'description': 'The tracking options for the Automation',
                        'properties': {
                            'opens': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to track opens',
                            },
                            'html_clicks': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to track clicks in the HTML version',
                            },
                            'text_clicks': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to track clicks in the plain-text version',
                            },
                            'goal_tracking': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to enable Goal tracking',
                            },
                            'ecomm360': {
                                'type': ['boolean', 'null'],
                                'description': 'Whether to enable eCommerce360 tracking',
                            },
                            'google_analytics': {
                                'type': ['string', 'null'],
                                'description': 'The custom slug for Google Analytics tracking',
                            },
                            'clicktale': {
                                'type': ['string', 'null'],
                                'description': 'The custom slug for ClickTale tracking',
                            },
                        },
                    },
                    'report_summary': {
                        'type': ['object', 'null'],
                        'description': 'A summary of opens and clicks for sent campaigns',
                        'properties': {
                            'opens': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of opens for a campaign',
                            },
                            'unique_opens': {
                                'type': ['integer', 'null'],
                                'description': 'The number of unique opens',
                            },
                            'open_rate': {
                                'type': ['number', 'null'],
                                'description': 'The number of unique opens divided by the total number of successful deliveries',
                            },
                            'clicks': {
                                'type': ['integer', 'null'],
                                'description': 'The total number of clicks for an campaign',
                            },
                            'subscriber_clicks': {
                                'type': ['integer', 'null'],
                                'description': 'The number of unique clicks',
                            },
                            'click_rate': {
                                'type': ['number', 'null'],
                                'description': 'The number of unique clicks divided by the total number of successful deliveries',
                            },
                        },
                    },
                },
                'x-airbyte-entity-name': 'automations',
                'x-airbyte-stream-name': 'automations',
            },
        ),
        EntityDefinition(
            name='tags',
            stream_name='tags',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/lists/{list_id}/tag-search',
                    action=Action.LIST,
                    description='Search for tags on a list by name',
                    query_params=['name'],
                    query_params_schema={
                        'name': {'type': 'string', 'required': False},
                    },
                    path_params=['list_id'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A list of tags assigned to a list',
                        'properties': {
                            'tags': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A tag that can be assigned to a list member',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'The unique id for the tag'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the tag',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'tags',
                                    'x-airbyte-stream-name': 'tags',
                                },
                            },
                            'total_items': {'type': 'integer', 'description': 'The total number of items matching the query regardless of pagination'},
                        },
                    },
                    record_extractor='$.tags',
                    meta_extractor={'total_items': '$.total_items'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A tag that can be assigned to a list member',
                'properties': {
                    'id': {'type': 'integer', 'description': 'The unique id for the tag'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the tag',
                    },
                },
                'x-airbyte-entity-name': 'tags',
                'x-airbyte-stream-name': 'tags',
            },
        ),
        EntityDefinition(
            name='interest_categories',
            stream_name='interest_categories',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/lists/{list_id}/interest-categories',
                    action=Action.LIST,
                    description="Get information about a list's interest categories",
                    query_params=['count', 'offset'],
                    query_params_schema={
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    path_params=['list_id'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': "Information about this list's interest categories",
                        'properties': {
                            'list_id': {
                                'type': ['string', 'null'],
                                'description': 'The ID for the list that this category belongs to',
                            },
                            'categories': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Interest categories organize interests, which are used to group subscribers based on their preferences',
                                    'properties': {
                                        'list_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The unique list id for the category',
                                        },
                                        'id': {'type': 'string', 'description': 'The id for the interest category'},
                                        'title': {
                                            'type': ['string', 'null'],
                                            'description': 'The text description of this category',
                                        },
                                        'display_order': {
                                            'type': ['integer', 'null'],
                                            'description': 'The order that the categories are displayed in the list',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': "Determines how this category's interests appear on signup forms",
                                            'enum': [
                                                'checkboxes',
                                                'dropdown',
                                                'radio',
                                                'hidden',
                                                None,
                                            ],
                                        },
                                    },
                                    'x-airbyte-entity-name': 'interest_categories',
                                    'x-airbyte-stream-name': 'interest_categories',
                                },
                            },
                            'total_items': {'type': 'integer', 'description': 'The total number of items matching the query regardless of pagination'},
                        },
                    },
                    record_extractor='$.categories',
                    meta_extractor={'total_items': '$.total_items'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/lists/{list_id}/interest-categories/{interest_category_id}',
                    action=Action.GET,
                    description='Get information about a specific interest category',
                    path_params=['list_id', 'interest_category_id'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                        'interest_category_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Interest categories organize interests, which are used to group subscribers based on their preferences',
                        'properties': {
                            'list_id': {
                                'type': ['string', 'null'],
                                'description': 'The unique list id for the category',
                            },
                            'id': {'type': 'string', 'description': 'The id for the interest category'},
                            'title': {
                                'type': ['string', 'null'],
                                'description': 'The text description of this category',
                            },
                            'display_order': {
                                'type': ['integer', 'null'],
                                'description': 'The order that the categories are displayed in the list',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': "Determines how this category's interests appear on signup forms",
                                'enum': [
                                    'checkboxes',
                                    'dropdown',
                                    'radio',
                                    'hidden',
                                    None,
                                ],
                            },
                        },
                        'x-airbyte-entity-name': 'interest_categories',
                        'x-airbyte-stream-name': 'interest_categories',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Interest categories organize interests, which are used to group subscribers based on their preferences',
                'properties': {
                    'list_id': {
                        'type': ['string', 'null'],
                        'description': 'The unique list id for the category',
                    },
                    'id': {'type': 'string', 'description': 'The id for the interest category'},
                    'title': {
                        'type': ['string', 'null'],
                        'description': 'The text description of this category',
                    },
                    'display_order': {
                        'type': ['integer', 'null'],
                        'description': 'The order that the categories are displayed in the list',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': "Determines how this category's interests appear on signup forms",
                        'enum': [
                            'checkboxes',
                            'dropdown',
                            'radio',
                            'hidden',
                            None,
                        ],
                    },
                },
                'x-airbyte-entity-name': 'interest_categories',
                'x-airbyte-stream-name': 'interest_categories',
            },
        ),
        EntityDefinition(
            name='interests',
            stream_name='interests',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/lists/{list_id}/interest-categories/{interest_category_id}/interests',
                    action=Action.LIST,
                    description="Get a list of this category's interests",
                    query_params=['count', 'offset'],
                    query_params_schema={
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    path_params=['list_id', 'interest_category_id'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                        'interest_category_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A list of interests for a specific list',
                        'properties': {
                            'interests': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Assign subscribers to interests to group them together',
                                    'properties': {
                                        'category_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The id for the interest category',
                                        },
                                        'list_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The ID for the list that this interest belongs to',
                                        },
                                        'id': {'type': 'string', 'description': 'The ID for the interest'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the interest',
                                        },
                                        'subscriber_count': {
                                            'type': ['string', 'null'],
                                            'description': 'The number of subscribers associated with this interest',
                                        },
                                        'display_order': {
                                            'type': ['integer', 'null'],
                                            'description': 'The display order for interests',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'interests',
                                    'x-airbyte-stream-name': 'interests',
                                },
                            },
                            'list_id': {
                                'type': ['string', 'null'],
                                'description': 'The unique list id',
                            },
                            'category_id': {
                                'type': ['string', 'null'],
                                'description': 'The id for the interest category',
                            },
                            'total_items': {'type': 'integer', 'description': 'The total number of items matching the query regardless of pagination'},
                        },
                    },
                    record_extractor='$.interests',
                    meta_extractor={'total_items': '$.total_items'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/lists/{list_id}/interest-categories/{interest_category_id}/interests/{interest_id}',
                    action=Action.GET,
                    description='Get interests or group names for a specific category',
                    path_params=['list_id', 'interest_category_id', 'interest_id'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                        'interest_category_id': {'type': 'string', 'required': True},
                        'interest_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Assign subscribers to interests to group them together',
                        'properties': {
                            'category_id': {
                                'type': ['string', 'null'],
                                'description': 'The id for the interest category',
                            },
                            'list_id': {
                                'type': ['string', 'null'],
                                'description': 'The ID for the list that this interest belongs to',
                            },
                            'id': {'type': 'string', 'description': 'The ID for the interest'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The name of the interest',
                            },
                            'subscriber_count': {
                                'type': ['string', 'null'],
                                'description': 'The number of subscribers associated with this interest',
                            },
                            'display_order': {
                                'type': ['integer', 'null'],
                                'description': 'The display order for interests',
                            },
                        },
                        'x-airbyte-entity-name': 'interests',
                        'x-airbyte-stream-name': 'interests',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Assign subscribers to interests to group them together',
                'properties': {
                    'category_id': {
                        'type': ['string', 'null'],
                        'description': 'The id for the interest category',
                    },
                    'list_id': {
                        'type': ['string', 'null'],
                        'description': 'The ID for the list that this interest belongs to',
                    },
                    'id': {'type': 'string', 'description': 'The ID for the interest'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the interest',
                    },
                    'subscriber_count': {
                        'type': ['string', 'null'],
                        'description': 'The number of subscribers associated with this interest',
                    },
                    'display_order': {
                        'type': ['integer', 'null'],
                        'description': 'The display order for interests',
                    },
                },
                'x-airbyte-entity-name': 'interests',
                'x-airbyte-stream-name': 'interests',
            },
        ),
        EntityDefinition(
            name='segments',
            stream_name='segments',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/lists/{list_id}/segments',
                    action=Action.LIST,
                    description='Get information about all available segments for a specific list',
                    query_params=[
                        'count',
                        'offset',
                        'type',
                        'since_created_at',
                        'before_created_at',
                        'since_updated_at',
                        'before_updated_at',
                    ],
                    query_params_schema={
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                        'type': {'type': 'string', 'required': False},
                        'since_created_at': {'type': 'string', 'required': False},
                        'before_created_at': {'type': 'string', 'required': False},
                        'since_updated_at': {'type': 'string', 'required': False},
                        'before_updated_at': {'type': 'string', 'required': False},
                    },
                    path_params=['list_id'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A list of available segments',
                        'properties': {
                            'segments': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Information about a specific segment',
                                    'properties': {
                                        'id': {'type': 'integer', 'description': 'The unique id for the segment'},
                                        'name': {
                                            'type': ['string', 'null'],
                                            'description': 'The name of the segment',
                                        },
                                        'member_count': {
                                            'type': ['integer', 'null'],
                                            'description': 'The number of active subscribers currently included in the segment',
                                        },
                                        'type': {
                                            'type': ['string', 'null'],
                                            'description': 'The type of segment',
                                            'enum': [
                                                'saved',
                                                'static',
                                                'fuzzy',
                                                None,
                                            ],
                                        },
                                        'created_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time the segment was created',
                                        },
                                        'updated_at': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time the segment was last updated',
                                        },
                                        'options': {
                                            'type': ['object', 'null'],
                                            'description': 'The conditions of the segment',
                                            'properties': {
                                                'match': {
                                                    'type': ['string', 'null'],
                                                    'description': 'Match type',
                                                },
                                                'conditions': {
                                                    'type': ['array', 'null'],
                                                    'description': 'Segment match conditions',
                                                    'items': {'type': 'object', 'additionalProperties': True},
                                                },
                                            },
                                        },
                                        'list_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The list id',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'segments',
                                    'x-airbyte-stream-name': 'segments',
                                },
                            },
                            'list_id': {
                                'type': ['string', 'null'],
                                'description': 'The list id',
                            },
                            'total_items': {'type': 'integer', 'description': 'The total number of items matching the query regardless of pagination'},
                        },
                    },
                    record_extractor='$.segments',
                    meta_extractor={'total_items': '$.total_items'},
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/lists/{list_id}/segments/{segment_id}',
                    action=Action.GET,
                    description='Get information about a specific segment',
                    path_params=['list_id', 'segment_id'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                        'segment_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'Information about a specific segment',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'The unique id for the segment'},
                            'name': {
                                'type': ['string', 'null'],
                                'description': 'The name of the segment',
                            },
                            'member_count': {
                                'type': ['integer', 'null'],
                                'description': 'The number of active subscribers currently included in the segment',
                            },
                            'type': {
                                'type': ['string', 'null'],
                                'description': 'The type of segment',
                                'enum': [
                                    'saved',
                                    'static',
                                    'fuzzy',
                                    None,
                                ],
                            },
                            'created_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time the segment was created',
                            },
                            'updated_at': {
                                'type': ['string', 'null'],
                                'format': 'date-time',
                                'description': 'The date and time the segment was last updated',
                            },
                            'options': {
                                'type': ['object', 'null'],
                                'description': 'The conditions of the segment',
                                'properties': {
                                    'match': {
                                        'type': ['string', 'null'],
                                        'description': 'Match type',
                                    },
                                    'conditions': {
                                        'type': ['array', 'null'],
                                        'description': 'Segment match conditions',
                                        'items': {'type': 'object', 'additionalProperties': True},
                                    },
                                },
                            },
                            'list_id': {
                                'type': ['string', 'null'],
                                'description': 'The list id',
                            },
                        },
                        'x-airbyte-entity-name': 'segments',
                        'x-airbyte-stream-name': 'segments',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Information about a specific segment',
                'properties': {
                    'id': {'type': 'integer', 'description': 'The unique id for the segment'},
                    'name': {
                        'type': ['string', 'null'],
                        'description': 'The name of the segment',
                    },
                    'member_count': {
                        'type': ['integer', 'null'],
                        'description': 'The number of active subscribers currently included in the segment',
                    },
                    'type': {
                        'type': ['string', 'null'],
                        'description': 'The type of segment',
                        'enum': [
                            'saved',
                            'static',
                            'fuzzy',
                            None,
                        ],
                    },
                    'created_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time the segment was created',
                    },
                    'updated_at': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time the segment was last updated',
                    },
                    'options': {
                        'type': ['object', 'null'],
                        'description': 'The conditions of the segment',
                        'properties': {
                            'match': {
                                'type': ['string', 'null'],
                                'description': 'Match type',
                            },
                            'conditions': {
                                'type': ['array', 'null'],
                                'description': 'Segment match conditions',
                                'items': {'type': 'object', 'additionalProperties': True},
                            },
                        },
                    },
                    'list_id': {
                        'type': ['string', 'null'],
                        'description': 'The list id',
                    },
                },
                'x-airbyte-entity-name': 'segments',
                'x-airbyte-stream-name': 'segments',
            },
        ),
        EntityDefinition(
            name='segment_members',
            stream_name='segment_members',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/lists/{list_id}/segments/{segment_id}/members',
                    action=Action.LIST,
                    description='Get information about members in a saved segment',
                    query_params=['count', 'offset'],
                    query_params_schema={
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    path_params=['list_id', 'segment_id'],
                    path_params_schema={
                        'list_id': {'type': 'string', 'required': True},
                        'segment_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'View members in a specific list segment',
                        'properties': {
                            'members': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'Individuals who are currently or have been previously subscribed to this list',
                                    'properties': {
                                        'id': {'type': 'string', 'description': "The MD5 hash of the lowercase version of the list member's email address"},
                                        'email_address': {
                                            'type': ['string', 'null'],
                                            'description': 'Email address for a subscriber',
                                        },
                                        'unique_email_id': {
                                            'type': ['string', 'null'],
                                            'description': 'An identifier for the address across all of Mailchimp',
                                        },
                                        'email_type': {
                                            'type': ['string', 'null'],
                                            'description': 'Type of email this member asked to get',
                                        },
                                        'status': {
                                            'type': ['string', 'null'],
                                            'description': "Subscriber's current status",
                                            'enum': [
                                                'subscribed',
                                                'unsubscribed',
                                                'cleaned',
                                                'pending',
                                                'transactional',
                                                'archived',
                                                None,
                                            ],
                                        },
                                        'merge_fields': {
                                            'type': ['object', 'null'],
                                            'description': 'A dictionary of merge fields where the keys are the merge tags',
                                            'additionalProperties': True,
                                        },
                                        'interests': {
                                            'type': ['object', 'null'],
                                            'description': "The key of this object's properties is the ID of the interest in question",
                                            'additionalProperties': {'type': 'boolean'},
                                        },
                                        'stats': {
                                            'type': ['object', 'null'],
                                            'description': 'Open and click rates for this subscriber',
                                            'properties': {
                                                'avg_open_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': "A subscriber's average open rate",
                                                },
                                                'avg_click_rate': {
                                                    'type': ['number', 'null'],
                                                    'description': "A subscriber's average clickthrough rate",
                                                },
                                            },
                                        },
                                        'ip_signup': {
                                            'type': ['string', 'null'],
                                            'description': 'IP address the subscriber signed up from',
                                        },
                                        'timestamp_signup': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time the subscriber signed up for the list',
                                        },
                                        'ip_opt': {
                                            'type': ['string', 'null'],
                                            'description': 'The IP address the subscriber used to confirm their opt-in status',
                                        },
                                        'timestamp_opt': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time the subscriber confirmed their opt-in status',
                                        },
                                        'member_rating': {
                                            'type': ['integer', 'null'],
                                            'description': 'Star rating for this member, between 1 and 5',
                                        },
                                        'last_changed': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': "The date and time the member's info was last changed",
                                        },
                                        'language': {
                                            'type': ['string', 'null'],
                                            'description': "If set/detected, the subscriber's language",
                                        },
                                        'vip': {
                                            'type': ['boolean', 'null'],
                                            'description': 'VIP status for subscriber',
                                        },
                                        'email_client': {
                                            'type': ['string', 'null'],
                                            'description': "The list member's email client",
                                        },
                                        'location': {
                                            'type': ['object', 'null'],
                                            'description': 'Subscriber location information',
                                            'properties': {
                                                'latitude': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The location latitude',
                                                },
                                                'longitude': {
                                                    'type': ['number', 'null'],
                                                    'description': 'The location longitude',
                                                },
                                                'gmtoff': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The time difference in hours from GMT',
                                                },
                                                'dstoff': {
                                                    'type': ['integer', 'null'],
                                                    'description': 'The offset for timezones where daylight saving time is observed',
                                                },
                                                'country_code': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The unique code for the location country',
                                                },
                                                'timezone': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The timezone for the location',
                                                },
                                                'region': {
                                                    'type': ['string', 'null'],
                                                    'description': 'The region for the location',
                                                },
                                            },
                                        },
                                        'list_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The list id',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'segment_members',
                                    'x-airbyte-stream-name': 'segment_members',
                                },
                            },
                            'total_items': {'type': 'integer', 'description': 'The total number of items matching the query regardless of pagination'},
                        },
                    },
                    record_extractor='$.members',
                    meta_extractor={'total_items': '$.total_items'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'Individuals who are currently or have been previously subscribed to this list',
                'properties': {
                    'id': {'type': 'string', 'description': "The MD5 hash of the lowercase version of the list member's email address"},
                    'email_address': {
                        'type': ['string', 'null'],
                        'description': 'Email address for a subscriber',
                    },
                    'unique_email_id': {
                        'type': ['string', 'null'],
                        'description': 'An identifier for the address across all of Mailchimp',
                    },
                    'email_type': {
                        'type': ['string', 'null'],
                        'description': 'Type of email this member asked to get',
                    },
                    'status': {
                        'type': ['string', 'null'],
                        'description': "Subscriber's current status",
                        'enum': [
                            'subscribed',
                            'unsubscribed',
                            'cleaned',
                            'pending',
                            'transactional',
                            'archived',
                            None,
                        ],
                    },
                    'merge_fields': {
                        'type': ['object', 'null'],
                        'description': 'A dictionary of merge fields where the keys are the merge tags',
                        'additionalProperties': True,
                    },
                    'interests': {
                        'type': ['object', 'null'],
                        'description': "The key of this object's properties is the ID of the interest in question",
                        'additionalProperties': {'type': 'boolean'},
                    },
                    'stats': {
                        'type': ['object', 'null'],
                        'description': 'Open and click rates for this subscriber',
                        'properties': {
                            'avg_open_rate': {
                                'type': ['number', 'null'],
                                'description': "A subscriber's average open rate",
                            },
                            'avg_click_rate': {
                                'type': ['number', 'null'],
                                'description': "A subscriber's average clickthrough rate",
                            },
                        },
                    },
                    'ip_signup': {
                        'type': ['string', 'null'],
                        'description': 'IP address the subscriber signed up from',
                    },
                    'timestamp_signup': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time the subscriber signed up for the list',
                    },
                    'ip_opt': {
                        'type': ['string', 'null'],
                        'description': 'The IP address the subscriber used to confirm their opt-in status',
                    },
                    'timestamp_opt': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time the subscriber confirmed their opt-in status',
                    },
                    'member_rating': {
                        'type': ['integer', 'null'],
                        'description': 'Star rating for this member, between 1 and 5',
                    },
                    'last_changed': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': "The date and time the member's info was last changed",
                    },
                    'language': {
                        'type': ['string', 'null'],
                        'description': "If set/detected, the subscriber's language",
                    },
                    'vip': {
                        'type': ['boolean', 'null'],
                        'description': 'VIP status for subscriber',
                    },
                    'email_client': {
                        'type': ['string', 'null'],
                        'description': "The list member's email client",
                    },
                    'location': {
                        'type': ['object', 'null'],
                        'description': 'Subscriber location information',
                        'properties': {
                            'latitude': {
                                'type': ['number', 'null'],
                                'description': 'The location latitude',
                            },
                            'longitude': {
                                'type': ['number', 'null'],
                                'description': 'The location longitude',
                            },
                            'gmtoff': {
                                'type': ['integer', 'null'],
                                'description': 'The time difference in hours from GMT',
                            },
                            'dstoff': {
                                'type': ['integer', 'null'],
                                'description': 'The offset for timezones where daylight saving time is observed',
                            },
                            'country_code': {
                                'type': ['string', 'null'],
                                'description': 'The unique code for the location country',
                            },
                            'timezone': {
                                'type': ['string', 'null'],
                                'description': 'The timezone for the location',
                            },
                            'region': {
                                'type': ['string', 'null'],
                                'description': 'The region for the location',
                            },
                        },
                    },
                    'list_id': {
                        'type': ['string', 'null'],
                        'description': 'The list id',
                    },
                },
                'x-airbyte-entity-name': 'segment_members',
                'x-airbyte-stream-name': 'segment_members',
            },
        ),
        EntityDefinition(
            name='unsubscribes',
            stream_name='unsubscribes',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/reports/{campaign_id}/unsubscribed',
                    action=Action.LIST,
                    description='Get information about members who have unsubscribed from a specific campaign',
                    query_params=['count', 'offset'],
                    query_params_schema={
                        'count': {
                            'type': 'integer',
                            'required': False,
                            'default': 10,
                        },
                        'offset': {
                            'type': 'integer',
                            'required': False,
                            'default': 0,
                        },
                    },
                    path_params=['campaign_id'],
                    path_params_schema={
                        'campaign_id': {'type': 'string', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A list of members who have unsubscribed from a specific campaign',
                        'properties': {
                            'unsubscribes': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'description': 'A member who unsubscribed from a specific campaign',
                                    'properties': {
                                        'email_id': {
                                            'type': ['string', 'null'],
                                            'description': "The MD5 hash of the lowercase version of the list member's email address",
                                        },
                                        'email_address': {
                                            'type': ['string', 'null'],
                                            'description': 'Email address for a subscriber',
                                        },
                                        'merge_fields': {
                                            'type': ['object', 'null'],
                                            'description': 'A dictionary of merge fields where the keys are the merge tags',
                                            'additionalProperties': True,
                                        },
                                        'vip': {
                                            'type': ['boolean', 'null'],
                                            'description': 'VIP status for subscriber',
                                        },
                                        'timestamp': {
                                            'type': ['string', 'null'],
                                            'format': 'date-time',
                                            'description': 'The date and time the member opted-out',
                                        },
                                        'reason': {
                                            'type': ['string', 'null'],
                                            'description': 'If available, the reason listed by the member for unsubscribing',
                                        },
                                        'campaign_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The campaign id',
                                        },
                                        'list_id': {
                                            'type': ['string', 'null'],
                                            'description': 'The list id',
                                        },
                                        'list_is_active': {
                                            'type': ['boolean', 'null'],
                                            'description': 'The status of the list used',
                                        },
                                    },
                                    'x-airbyte-entity-name': 'unsubscribes',
                                    'x-airbyte-stream-name': 'unsubscribes',
                                },
                            },
                            'campaign_id': {
                                'type': ['string', 'null'],
                                'description': 'The campaign id',
                            },
                            'total_items': {'type': 'integer', 'description': 'The total number of items matching the query regardless of pagination'},
                        },
                    },
                    record_extractor='$.unsubscribes',
                    meta_extractor={'total_items': '$.total_items'},
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A member who unsubscribed from a specific campaign',
                'properties': {
                    'email_id': {
                        'type': ['string', 'null'],
                        'description': "The MD5 hash of the lowercase version of the list member's email address",
                    },
                    'email_address': {
                        'type': ['string', 'null'],
                        'description': 'Email address for a subscriber',
                    },
                    'merge_fields': {
                        'type': ['object', 'null'],
                        'description': 'A dictionary of merge fields where the keys are the merge tags',
                        'additionalProperties': True,
                    },
                    'vip': {
                        'type': ['boolean', 'null'],
                        'description': 'VIP status for subscriber',
                    },
                    'timestamp': {
                        'type': ['string', 'null'],
                        'format': 'date-time',
                        'description': 'The date and time the member opted-out',
                    },
                    'reason': {
                        'type': ['string', 'null'],
                        'description': 'If available, the reason listed by the member for unsubscribing',
                    },
                    'campaign_id': {
                        'type': ['string', 'null'],
                        'description': 'The campaign id',
                    },
                    'list_id': {
                        'type': ['string', 'null'],
                        'description': 'The list id',
                    },
                    'list_is_active': {
                        'type': ['boolean', 'null'],
                        'description': 'The status of the list used',
                    },
                },
                'x-airbyte-entity-name': 'unsubscribes',
                'x-airbyte-stream-name': 'unsubscribes',
            },
        ),
    ],
    search_field_paths={
        'campaigns': [
            'ab_split_opts',
            'ab_split_opts.from_name_a',
            'ab_split_opts.from_name_b',
            'ab_split_opts.pick_winner',
            'ab_split_opts.reply_email_a',
            'ab_split_opts.reply_email_b',
            'ab_split_opts.send_time_a',
            'ab_split_opts.send_time_b',
            'ab_split_opts.send_time_winner',
            'ab_split_opts.split_size',
            'ab_split_opts.split_test',
            'ab_split_opts.subject_a',
            'ab_split_opts.subject_b',
            'ab_split_opts.wait_time',
            'ab_split_opts.wait_units',
            'archive_url',
            'content_type',
            'create_time',
            'delivery_status',
            'delivery_status.can_cancel',
            'delivery_status.emails_canceled',
            'delivery_status.emails_sent',
            'delivery_status.enabled',
            'delivery_status.status',
            'emails_sent',
            'id',
            'long_archive_url',
            'needs_block_refresh',
            'parent_campaign_id',
            'recipients',
            'recipients.list_id',
            'recipients.list_is_active',
            'recipients.list_name',
            'recipients.recipient_count',
            'recipients.segment_opts',
            'recipients.segment_text',
            'report_summary',
            'report_summary.click_rate',
            'report_summary.clicks',
            'report_summary.ecommerce',
            'report_summary.open_rate',
            'report_summary.opens',
            'report_summary.subscriber_clicks',
            'report_summary.unique_opens',
            'resendable',
            'rss_opts',
            'rss_opts.constrain_rss_img',
            'rss_opts.feed_url',
            'rss_opts.frequency',
            'rss_opts.last_sent',
            'rss_opts.schedule',
            'send_time',
            'settings',
            'settings.authenticate',
            'settings.auto_fb_post',
            'settings.auto_fb_post[]',
            'settings.auto_footer',
            'settings.auto_tweet',
            'settings.drag_and_drop',
            'settings.fb_comments',
            'settings.folder_id',
            'settings.from_name',
            'settings.inline_css',
            'settings.preview_text',
            'settings.reply_to',
            'settings.subject_line',
            'settings.template_id',
            'settings.timewarp',
            'settings.title',
            'settings.to_name',
            'settings.use_conversation',
            'social_card',
            'social_card.description',
            'social_card.image_url',
            'social_card.title',
            'status',
            'tracking',
            'tracking.capsule',
            'tracking.clicktale',
            'tracking.ecomm360',
            'tracking.goal_tracking',
            'tracking.google_analytics',
            'tracking.html_clicks',
            'tracking.opens',
            'tracking.salesforce',
            'tracking.text_clicks',
            'type',
            'variate_settings',
            'variate_settings.combinations',
            'variate_settings.combinations[]',
            'variate_settings.contents',
            'variate_settings.contents[]',
            'variate_settings.from_names',
            'variate_settings.from_names[]',
            'variate_settings.reply_to_addresses',
            'variate_settings.reply_to_addresses[]',
            'variate_settings.send_times',
            'variate_settings.send_times[]',
            'variate_settings.subject_lines',
            'variate_settings.subject_lines[]',
            'variate_settings.test_size',
            'variate_settings.wait_time',
            'variate_settings.winner_criteria',
            'variate_settings.winning_campaign_id',
            'variate_settings.winning_combination_id',
            'web_id',
        ],
        'email_activity': [
            'action',
            'campaign_id',
            'email_address',
            'email_id',
            'ip',
            'list_id',
            'list_is_active',
            'timestamp',
            'type',
            'url',
        ],
        'lists': [
            'beamer_address',
            'campaign_defaults',
            'campaign_defaults.from_email',
            'campaign_defaults.from_name',
            'campaign_defaults.language',
            'campaign_defaults.subject',
            'contact',
            'contact.address1',
            'contact.address2',
            'contact.city',
            'contact.company',
            'contact.country',
            'contact.phone',
            'contact.state',
            'contact.zip',
            'date_created',
            'double_optin',
            'email_type_option',
            'has_welcome',
            'id',
            'list_rating',
            'marketing_permissions',
            'modules',
            'modules[]',
            'name',
            'notify_on_subscribe',
            'notify_on_unsubscribe',
            'permission_reminder',
            'stats',
            'stats.avg_sub_rate',
            'stats.avg_unsub_rate',
            'stats.campaign_count',
            'stats.campaign_last_sent',
            'stats.cleaned_count',
            'stats.cleaned_count_since_send',
            'stats.click_rate',
            'stats.last_sub_date',
            'stats.last_unsub_date',
            'stats.member_count',
            'stats.member_count_since_send',
            'stats.merge_field_count',
            'stats.open_rate',
            'stats.target_sub_rate',
            'stats.total_contacts',
            'stats.unsubscribe_count',
            'stats.unsubscribe_count_since_send',
            'subscribe_url_long',
            'subscribe_url_short',
            'use_archive_bar',
            'visibility',
            'web_id',
        ],
        'reports': [
            'ab_split',
            'ab_split.a',
            'ab_split.b',
            'abuse_reports',
            'bounces',
            'bounces.hard_bounces',
            'bounces.soft_bounces',
            'bounces.syntax_errors',
            'campaign_title',
            'clicks',
            'clicks.click_rate',
            'clicks.clicks_total',
            'clicks.last_click',
            'clicks.unique_clicks',
            'clicks.unique_subscriber_clicks',
            'delivery_status',
            'delivery_status.can_cancel',
            'delivery_status.emails_canceled',
            'delivery_status.emails_sent',
            'delivery_status.enabled',
            'delivery_status.status',
            'ecommerce',
            'ecommerce.currency_code',
            'ecommerce.total_orders',
            'ecommerce.total_revenue',
            'ecommerce.total_spent',
            'emails_sent',
            'facebook_likes',
            'facebook_likes.facebook_likes',
            'facebook_likes.recipient_likes',
            'facebook_likes.unique_likes',
            'forwards',
            'forwards.forwards_count',
            'forwards.forwards_opens',
            'id',
            'industry_stats',
            'industry_stats.abuse_rate',
            'industry_stats.bounce_rate',
            'industry_stats.click_rate',
            'industry_stats.open_rate',
            'industry_stats.type',
            'industry_stats.unopen_rate',
            'industry_stats.unsub_rate',
            'list_id',
            'list_is_active',
            'list_name',
            'list_stats',
            'list_stats.click_rate',
            'list_stats.open_rate',
            'list_stats.sub_rate',
            'list_stats.unsub_rate',
            'opens',
            'opens.last_open',
            'opens.open_rate',
            'opens.opens_total',
            'opens.unique_opens',
            'preview_text',
            'rss_last_send',
            'send_time',
            'share_report',
            'share_report.share_password',
            'share_report.share_url',
            'subject_line',
            'timeseries',
            'timeseries[]',
            'timewarp',
            'timewarp[]',
            'type',
            'unsubscribed',
        ],
    },
)