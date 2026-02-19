"""
Connector model for freshdesk.

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

FreshdeskConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('ec4b9503-13cb-48ab-a4ab-6ade4be46567'),
    name='freshdesk',
    version='1.0.1',
    base_url='https://{subdomain}.freshdesk.com/api/v2',
    auth=AuthConfig(
        type=AuthType.BASIC,
        user_config_spec=AirbyteAuthConfig(
            title='API Key Authentication',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='Your Freshdesk API key (found in Profile Settings)',
                ),
            },
            auth_mapping={'username': '${api_key}', 'password': 'X'},
            replication_auth_key_mapping={'api_key': 'api_key'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='tickets',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/tickets',
                    action=Action.LIST,
                    description='Returns a paginated list of tickets. By default returns tickets created in the past 30 days. Use updated_since to get older tickets.',
                    query_params=[
                        'per_page',
                        'page',
                        'updated_since',
                        'order_by',
                        'order_type',
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
                        'updated_since': {'type': 'string', 'required': False},
                        'order_by': {
                            'type': 'string',
                            'required': False,
                            'default': 'updated_at',
                        },
                        'order_type': {
                            'type': 'string',
                            'required': False,
                            'default': 'desc',
                        },
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A Freshdesk support ticket',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique ticket ID'},
                                'subject': {
                                    'type': ['null', 'string'],
                                    'description': 'Subject of the ticket',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'HTML content of the ticket',
                                },
                                'description_text': {
                                    'type': ['null', 'string'],
                                    'description': 'Plain text content of the ticket',
                                },
                                'status': {
                                    'type': ['null', 'integer'],
                                    'description': 'Status: 2=Open, 3=Pending, 4=Resolved, 5=Closed',
                                },
                                'priority': {
                                    'type': ['null', 'integer'],
                                    'description': 'Priority: 1=Low, 2=Medium, 3=High, 4=Urgent',
                                },
                                'source': {
                                    'type': ['null', 'integer'],
                                    'description': 'Source: 1=Email, 2=Portal, 3=Phone, 7=Chat, 9=Feedback Widget, 10=Outbound Email',
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                    'description': 'Ticket type',
                                },
                                'requester_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the requester',
                                },
                                'responder_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the agent to whom the ticket is assigned',
                                },
                                'company_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Company ID of the requester',
                                },
                                'group_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the group to which the ticket is assigned',
                                },
                                'product_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the product associated with the ticket',
                                },
                                'email_config_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the email config used for the ticket',
                                },
                                'cc_emails': {
                                    'type': ['null', 'array'],
                                    'description': 'CC email addresses',
                                    'items': {'type': 'string'},
                                },
                                'fwd_emails': {
                                    'type': ['null', 'array'],
                                    'description': 'Forwarded email addresses',
                                    'items': {'type': 'string'},
                                },
                                'reply_cc_emails': {
                                    'type': ['null', 'array'],
                                    'description': 'Reply CC email addresses',
                                    'items': {'type': 'string'},
                                },
                                'to_emails': {
                                    'type': ['null', 'array'],
                                    'description': 'To email addresses',
                                    'items': {'type': 'string'},
                                },
                                'spam': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the ticket is marked as spam',
                                },
                                'deleted': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the ticket is deleted',
                                },
                                'fr_escalated': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the first response time was breached',
                                },
                                'is_escalated': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the ticket is escalated',
                                },
                                'fr_due_by': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'First response due by timestamp',
                                },
                                'due_by': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Resolution due by timestamp',
                                },
                                'tags': {
                                    'type': ['null', 'array'],
                                    'description': 'Tags associated with the ticket',
                                    'items': {'type': 'string'},
                                },
                                'custom_fields': {
                                    'type': ['null', 'object'],
                                    'description': 'Custom fields associated with the ticket',
                                },
                                'attachments': {
                                    'type': ['null', 'array'],
                                    'description': 'Ticket attachments',
                                    'items': {'type': 'object'},
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Ticket creation timestamp',
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Ticket last update timestamp',
                                },
                                'association_type': {
                                    'type': ['null', 'integer'],
                                    'description': 'Association type for parent/child tickets',
                                },
                                'associated_tickets_count': {
                                    'type': ['null', 'integer'],
                                    'description': 'Number of associated tickets',
                                },
                                'ticket_cc_emails': {
                                    'type': ['null', 'array'],
                                    'description': 'Ticket CC email addresses',
                                    'items': {'type': 'string'},
                                },
                                'ticket_bcc_emails': {
                                    'type': ['null', 'array'],
                                    'description': 'Ticket BCC email addresses',
                                    'items': {'type': 'string'},
                                },
                                'support_email': {
                                    'type': ['null', 'string'],
                                    'description': 'Support email address used for the ticket',
                                },
                                'source_additional_info': {
                                    'type': ['null', 'object'],
                                    'description': 'Additional information about the ticket source',
                                },
                                'structured_description': {
                                    'type': ['null', 'object'],
                                    'description': 'Structured description of the ticket',
                                },
                                'form_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the ticket form',
                                },
                                'nr_due_by': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Next response due by timestamp',
                                },
                                'nr_escalated': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the next response time was breached',
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'tickets',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/tickets/{id}',
                    action=Action.GET,
                    description='Get a single ticket by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Freshdesk support ticket',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique ticket ID'},
                            'subject': {
                                'type': ['null', 'string'],
                                'description': 'Subject of the ticket',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'HTML content of the ticket',
                            },
                            'description_text': {
                                'type': ['null', 'string'],
                                'description': 'Plain text content of the ticket',
                            },
                            'status': {
                                'type': ['null', 'integer'],
                                'description': 'Status: 2=Open, 3=Pending, 4=Resolved, 5=Closed',
                            },
                            'priority': {
                                'type': ['null', 'integer'],
                                'description': 'Priority: 1=Low, 2=Medium, 3=High, 4=Urgent',
                            },
                            'source': {
                                'type': ['null', 'integer'],
                                'description': 'Source: 1=Email, 2=Portal, 3=Phone, 7=Chat, 9=Feedback Widget, 10=Outbound Email',
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'Ticket type',
                            },
                            'requester_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the requester',
                            },
                            'responder_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the agent to whom the ticket is assigned',
                            },
                            'company_id': {
                                'type': ['null', 'integer'],
                                'description': 'Company ID of the requester',
                            },
                            'group_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the group to which the ticket is assigned',
                            },
                            'product_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the product associated with the ticket',
                            },
                            'email_config_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the email config used for the ticket',
                            },
                            'cc_emails': {
                                'type': ['null', 'array'],
                                'description': 'CC email addresses',
                                'items': {'type': 'string'},
                            },
                            'fwd_emails': {
                                'type': ['null', 'array'],
                                'description': 'Forwarded email addresses',
                                'items': {'type': 'string'},
                            },
                            'reply_cc_emails': {
                                'type': ['null', 'array'],
                                'description': 'Reply CC email addresses',
                                'items': {'type': 'string'},
                            },
                            'to_emails': {
                                'type': ['null', 'array'],
                                'description': 'To email addresses',
                                'items': {'type': 'string'},
                            },
                            'spam': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the ticket is marked as spam',
                            },
                            'deleted': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the ticket is deleted',
                            },
                            'fr_escalated': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the first response time was breached',
                            },
                            'is_escalated': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the ticket is escalated',
                            },
                            'fr_due_by': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'First response due by timestamp',
                            },
                            'due_by': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Resolution due by timestamp',
                            },
                            'tags': {
                                'type': ['null', 'array'],
                                'description': 'Tags associated with the ticket',
                                'items': {'type': 'string'},
                            },
                            'custom_fields': {
                                'type': ['null', 'object'],
                                'description': 'Custom fields associated with the ticket',
                            },
                            'attachments': {
                                'type': ['null', 'array'],
                                'description': 'Ticket attachments',
                                'items': {'type': 'object'},
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Ticket creation timestamp',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Ticket last update timestamp',
                            },
                            'association_type': {
                                'type': ['null', 'integer'],
                                'description': 'Association type for parent/child tickets',
                            },
                            'associated_tickets_count': {
                                'type': ['null', 'integer'],
                                'description': 'Number of associated tickets',
                            },
                            'ticket_cc_emails': {
                                'type': ['null', 'array'],
                                'description': 'Ticket CC email addresses',
                                'items': {'type': 'string'},
                            },
                            'ticket_bcc_emails': {
                                'type': ['null', 'array'],
                                'description': 'Ticket BCC email addresses',
                                'items': {'type': 'string'},
                            },
                            'support_email': {
                                'type': ['null', 'string'],
                                'description': 'Support email address used for the ticket',
                            },
                            'source_additional_info': {
                                'type': ['null', 'object'],
                                'description': 'Additional information about the ticket source',
                            },
                            'structured_description': {
                                'type': ['null', 'object'],
                                'description': 'Structured description of the ticket',
                            },
                            'form_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the ticket form',
                            },
                            'nr_due_by': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Next response due by timestamp',
                            },
                            'nr_escalated': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the next response time was breached',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'tickets',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Freshdesk support ticket',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique ticket ID'},
                    'subject': {
                        'type': ['null', 'string'],
                        'description': 'Subject of the ticket',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'HTML content of the ticket',
                    },
                    'description_text': {
                        'type': ['null', 'string'],
                        'description': 'Plain text content of the ticket',
                    },
                    'status': {
                        'type': ['null', 'integer'],
                        'description': 'Status: 2=Open, 3=Pending, 4=Resolved, 5=Closed',
                    },
                    'priority': {
                        'type': ['null', 'integer'],
                        'description': 'Priority: 1=Low, 2=Medium, 3=High, 4=Urgent',
                    },
                    'source': {
                        'type': ['null', 'integer'],
                        'description': 'Source: 1=Email, 2=Portal, 3=Phone, 7=Chat, 9=Feedback Widget, 10=Outbound Email',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Ticket type',
                    },
                    'requester_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the requester',
                    },
                    'responder_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the agent to whom the ticket is assigned',
                    },
                    'company_id': {
                        'type': ['null', 'integer'],
                        'description': 'Company ID of the requester',
                    },
                    'group_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the group to which the ticket is assigned',
                    },
                    'product_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the product associated with the ticket',
                    },
                    'email_config_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the email config used for the ticket',
                    },
                    'cc_emails': {
                        'type': ['null', 'array'],
                        'description': 'CC email addresses',
                        'items': {'type': 'string'},
                    },
                    'fwd_emails': {
                        'type': ['null', 'array'],
                        'description': 'Forwarded email addresses',
                        'items': {'type': 'string'},
                    },
                    'reply_cc_emails': {
                        'type': ['null', 'array'],
                        'description': 'Reply CC email addresses',
                        'items': {'type': 'string'},
                    },
                    'to_emails': {
                        'type': ['null', 'array'],
                        'description': 'To email addresses',
                        'items': {'type': 'string'},
                    },
                    'spam': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the ticket is marked as spam',
                    },
                    'deleted': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the ticket is deleted',
                    },
                    'fr_escalated': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the first response time was breached',
                    },
                    'is_escalated': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the ticket is escalated',
                    },
                    'fr_due_by': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'First response due by timestamp',
                    },
                    'due_by': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Resolution due by timestamp',
                    },
                    'tags': {
                        'type': ['null', 'array'],
                        'description': 'Tags associated with the ticket',
                        'items': {'type': 'string'},
                    },
                    'custom_fields': {
                        'type': ['null', 'object'],
                        'description': 'Custom fields associated with the ticket',
                    },
                    'attachments': {
                        'type': ['null', 'array'],
                        'description': 'Ticket attachments',
                        'items': {'type': 'object'},
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Ticket creation timestamp',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Ticket last update timestamp',
                    },
                    'association_type': {
                        'type': ['null', 'integer'],
                        'description': 'Association type for parent/child tickets',
                    },
                    'associated_tickets_count': {
                        'type': ['null', 'integer'],
                        'description': 'Number of associated tickets',
                    },
                    'ticket_cc_emails': {
                        'type': ['null', 'array'],
                        'description': 'Ticket CC email addresses',
                        'items': {'type': 'string'},
                    },
                    'ticket_bcc_emails': {
                        'type': ['null', 'array'],
                        'description': 'Ticket BCC email addresses',
                        'items': {'type': 'string'},
                    },
                    'support_email': {
                        'type': ['null', 'string'],
                        'description': 'Support email address used for the ticket',
                    },
                    'source_additional_info': {
                        'type': ['null', 'object'],
                        'description': 'Additional information about the ticket source',
                    },
                    'structured_description': {
                        'type': ['null', 'object'],
                        'description': 'Structured description of the ticket',
                    },
                    'form_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the ticket form',
                    },
                    'nr_due_by': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Next response due by timestamp',
                    },
                    'nr_escalated': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the next response time was breached',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'tickets',
            },
        ),
        EntityDefinition(
            name='contacts',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/contacts',
                    action=Action.LIST,
                    description='Returns a paginated list of contacts',
                    query_params=['per_page', 'page', 'updated_since'],
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
                        'updated_since': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A Freshdesk contact (customer)',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique contact ID'},
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Name of the contact',
                                },
                                'email': {
                                    'type': ['null', 'string'],
                                    'description': 'Primary email address',
                                },
                                'phone': {
                                    'type': ['null', 'string'],
                                    'description': 'Phone number',
                                },
                                'mobile': {
                                    'type': ['null', 'string'],
                                    'description': 'Mobile number',
                                },
                                'active': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the contact has been verified',
                                },
                                'address': {
                                    'type': ['null', 'string'],
                                    'description': 'Address of the contact',
                                },
                                'avatar': {
                                    'type': ['null', 'object'],
                                    'description': 'Avatar of the contact',
                                },
                                'company_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the primary company',
                                },
                                'view_all_tickets': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the contact can see all tickets from the company',
                                },
                                'custom_fields': {
                                    'type': ['null', 'object'],
                                    'description': 'Custom fields associated with the contact',
                                },
                                'deleted': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the contact is deleted',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Description of the contact',
                                },
                                'job_title': {
                                    'type': ['null', 'string'],
                                    'description': 'Job title of the contact',
                                },
                                'language': {
                                    'type': ['null', 'string'],
                                    'description': 'Language of the contact',
                                },
                                'twitter_id': {
                                    'type': ['null', 'string'],
                                    'description': 'Twitter ID',
                                },
                                'unique_external_id': {
                                    'type': ['null', 'string'],
                                    'description': 'External ID of the contact',
                                },
                                'other_emails': {
                                    'type': ['null', 'array'],
                                    'description': 'Additional email addresses',
                                    'items': {'type': 'string'},
                                },
                                'other_companies': {
                                    'type': ['null', 'array'],
                                    'description': 'Additional companies associated with the contact',
                                    'items': {'type': 'object'},
                                },
                                'tags': {
                                    'type': ['null', 'array'],
                                    'description': 'Tags associated with the contact',
                                    'items': {'type': 'string'},
                                },
                                'time_zone': {
                                    'type': ['null', 'string'],
                                    'description': 'Time zone of the contact',
                                },
                                'facebook_id': {
                                    'type': ['null', 'string'],
                                    'description': 'Facebook ID of the contact',
                                },
                                'csat_rating': {
                                    'type': ['null', 'integer'],
                                    'description': 'CSAT rating of the contact',
                                },
                                'preferred_source': {
                                    'type': ['null', 'string'],
                                    'description': 'Preferred contact source',
                                },
                                'first_name': {
                                    'type': ['null', 'string'],
                                    'description': 'First name of the contact',
                                },
                                'last_name': {
                                    'type': ['null', 'string'],
                                    'description': 'Last name of the contact',
                                },
                                'visitor_id': {
                                    'type': ['null', 'string'],
                                    'description': 'Visitor ID',
                                },
                                'org_contact_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'Organization contact ID',
                                },
                                'org_contact_id_str': {
                                    'type': ['null', 'string'],
                                    'description': 'Organization contact ID as string',
                                },
                                'other_phone_numbers': {
                                    'type': ['null', 'array'],
                                    'description': 'Additional phone numbers',
                                    'items': {'type': 'string'},
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Contact creation timestamp',
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Contact last update timestamp',
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'contacts',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/contacts/{id}',
                    action=Action.GET,
                    description='Get a single contact by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Freshdesk contact (customer)',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique contact ID'},
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the contact',
                            },
                            'email': {
                                'type': ['null', 'string'],
                                'description': 'Primary email address',
                            },
                            'phone': {
                                'type': ['null', 'string'],
                                'description': 'Phone number',
                            },
                            'mobile': {
                                'type': ['null', 'string'],
                                'description': 'Mobile number',
                            },
                            'active': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the contact has been verified',
                            },
                            'address': {
                                'type': ['null', 'string'],
                                'description': 'Address of the contact',
                            },
                            'avatar': {
                                'type': ['null', 'object'],
                                'description': 'Avatar of the contact',
                            },
                            'company_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the primary company',
                            },
                            'view_all_tickets': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the contact can see all tickets from the company',
                            },
                            'custom_fields': {
                                'type': ['null', 'object'],
                                'description': 'Custom fields associated with the contact',
                            },
                            'deleted': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the contact is deleted',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Description of the contact',
                            },
                            'job_title': {
                                'type': ['null', 'string'],
                                'description': 'Job title of the contact',
                            },
                            'language': {
                                'type': ['null', 'string'],
                                'description': 'Language of the contact',
                            },
                            'twitter_id': {
                                'type': ['null', 'string'],
                                'description': 'Twitter ID',
                            },
                            'unique_external_id': {
                                'type': ['null', 'string'],
                                'description': 'External ID of the contact',
                            },
                            'other_emails': {
                                'type': ['null', 'array'],
                                'description': 'Additional email addresses',
                                'items': {'type': 'string'},
                            },
                            'other_companies': {
                                'type': ['null', 'array'],
                                'description': 'Additional companies associated with the contact',
                                'items': {'type': 'object'},
                            },
                            'tags': {
                                'type': ['null', 'array'],
                                'description': 'Tags associated with the contact',
                                'items': {'type': 'string'},
                            },
                            'time_zone': {
                                'type': ['null', 'string'],
                                'description': 'Time zone of the contact',
                            },
                            'facebook_id': {
                                'type': ['null', 'string'],
                                'description': 'Facebook ID of the contact',
                            },
                            'csat_rating': {
                                'type': ['null', 'integer'],
                                'description': 'CSAT rating of the contact',
                            },
                            'preferred_source': {
                                'type': ['null', 'string'],
                                'description': 'Preferred contact source',
                            },
                            'first_name': {
                                'type': ['null', 'string'],
                                'description': 'First name of the contact',
                            },
                            'last_name': {
                                'type': ['null', 'string'],
                                'description': 'Last name of the contact',
                            },
                            'visitor_id': {
                                'type': ['null', 'string'],
                                'description': 'Visitor ID',
                            },
                            'org_contact_id': {
                                'type': ['null', 'integer'],
                                'description': 'Organization contact ID',
                            },
                            'org_contact_id_str': {
                                'type': ['null', 'string'],
                                'description': 'Organization contact ID as string',
                            },
                            'other_phone_numbers': {
                                'type': ['null', 'array'],
                                'description': 'Additional phone numbers',
                                'items': {'type': 'string'},
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Contact creation timestamp',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Contact last update timestamp',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'contacts',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Freshdesk contact (customer)',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique contact ID'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the contact',
                    },
                    'email': {
                        'type': ['null', 'string'],
                        'description': 'Primary email address',
                    },
                    'phone': {
                        'type': ['null', 'string'],
                        'description': 'Phone number',
                    },
                    'mobile': {
                        'type': ['null', 'string'],
                        'description': 'Mobile number',
                    },
                    'active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the contact has been verified',
                    },
                    'address': {
                        'type': ['null', 'string'],
                        'description': 'Address of the contact',
                    },
                    'avatar': {
                        'type': ['null', 'object'],
                        'description': 'Avatar of the contact',
                    },
                    'company_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the primary company',
                    },
                    'view_all_tickets': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the contact can see all tickets from the company',
                    },
                    'custom_fields': {
                        'type': ['null', 'object'],
                        'description': 'Custom fields associated with the contact',
                    },
                    'deleted': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the contact is deleted',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Description of the contact',
                    },
                    'job_title': {
                        'type': ['null', 'string'],
                        'description': 'Job title of the contact',
                    },
                    'language': {
                        'type': ['null', 'string'],
                        'description': 'Language of the contact',
                    },
                    'twitter_id': {
                        'type': ['null', 'string'],
                        'description': 'Twitter ID',
                    },
                    'unique_external_id': {
                        'type': ['null', 'string'],
                        'description': 'External ID of the contact',
                    },
                    'other_emails': {
                        'type': ['null', 'array'],
                        'description': 'Additional email addresses',
                        'items': {'type': 'string'},
                    },
                    'other_companies': {
                        'type': ['null', 'array'],
                        'description': 'Additional companies associated with the contact',
                        'items': {'type': 'object'},
                    },
                    'tags': {
                        'type': ['null', 'array'],
                        'description': 'Tags associated with the contact',
                        'items': {'type': 'string'},
                    },
                    'time_zone': {
                        'type': ['null', 'string'],
                        'description': 'Time zone of the contact',
                    },
                    'facebook_id': {
                        'type': ['null', 'string'],
                        'description': 'Facebook ID of the contact',
                    },
                    'csat_rating': {
                        'type': ['null', 'integer'],
                        'description': 'CSAT rating of the contact',
                    },
                    'preferred_source': {
                        'type': ['null', 'string'],
                        'description': 'Preferred contact source',
                    },
                    'first_name': {
                        'type': ['null', 'string'],
                        'description': 'First name of the contact',
                    },
                    'last_name': {
                        'type': ['null', 'string'],
                        'description': 'Last name of the contact',
                    },
                    'visitor_id': {
                        'type': ['null', 'string'],
                        'description': 'Visitor ID',
                    },
                    'org_contact_id': {
                        'type': ['null', 'integer'],
                        'description': 'Organization contact ID',
                    },
                    'org_contact_id_str': {
                        'type': ['null', 'string'],
                        'description': 'Organization contact ID as string',
                    },
                    'other_phone_numbers': {
                        'type': ['null', 'array'],
                        'description': 'Additional phone numbers',
                        'items': {'type': 'string'},
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Contact creation timestamp',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Contact last update timestamp',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'contacts',
            },
        ),
        EntityDefinition(
            name='agents',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/agents',
                    action=Action.LIST,
                    description='Returns a paginated list of agents',
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
                            'description': 'A Freshdesk agent',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique agent ID'},
                                'available': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the agent is available',
                                },
                                'available_since': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Timestamp since the agent has been available',
                                },
                                'occasional': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the agent is an occasional agent',
                                },
                                'signature': {
                                    'type': ['null', 'string'],
                                    'description': 'Signature of the agent (HTML)',
                                },
                                'ticket_scope': {
                                    'type': ['null', 'integer'],
                                    'description': 'Ticket scope: 1=Global, 2=Group, 3=Restricted',
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                    'description': 'Agent type: support_agent, field_agent, collaborator',
                                },
                                'skill_ids': {
                                    'type': ['null', 'array'],
                                    'description': 'Skill IDs associated with the agent',
                                    'items': {'type': 'integer'},
                                },
                                'group_ids': {
                                    'type': ['null', 'array'],
                                    'description': 'Group IDs the agent belongs to',
                                    'items': {'type': 'integer'},
                                },
                                'role_ids': {
                                    'type': ['null', 'array'],
                                    'description': 'Role IDs assigned to the agent',
                                    'items': {'type': 'integer'},
                                },
                                'focus_mode': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether focus mode is enabled',
                                },
                                'contact': {
                                    'type': ['null', 'object'],
                                    'description': 'Contact details of the agent',
                                    'properties': {
                                        'active': {
                                            'type': ['null', 'boolean'],
                                            'description': 'Whether the contact is active',
                                        },
                                        'email': {
                                            'type': ['null', 'string'],
                                            'description': 'Email of the agent',
                                        },
                                        'job_title': {
                                            'type': ['null', 'string'],
                                            'description': 'Job title',
                                        },
                                        'language': {
                                            'type': ['null', 'string'],
                                            'description': 'Language',
                                        },
                                        'last_login_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Last login timestamp',
                                        },
                                        'mobile': {
                                            'type': ['null', 'string'],
                                            'description': 'Mobile number',
                                        },
                                        'name': {
                                            'type': ['null', 'string'],
                                            'description': 'Name of the agent',
                                        },
                                        'phone': {
                                            'type': ['null', 'string'],
                                            'description': 'Phone number',
                                        },
                                        'time_zone': {
                                            'type': ['null', 'string'],
                                            'description': 'Time zone',
                                        },
                                        'created_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Contact creation timestamp',
                                        },
                                        'updated_at': {
                                            'type': ['null', 'string'],
                                            'format': 'date-time',
                                            'description': 'Contact update timestamp',
                                        },
                                    },
                                },
                                'last_active_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Timestamp of last agent activity',
                                },
                                'deactivated': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the agent is deactivated',
                                },
                                'agent_operational_status': {
                                    'type': ['null', 'string'],
                                    'description': 'Operational status of the agent',
                                },
                                'org_agent_id': {
                                    'type': ['null', 'string'],
                                    'description': 'Organization agent ID',
                                },
                                'org_group_ids': {
                                    'type': ['null', 'array'],
                                    'description': 'Organization group IDs',
                                    'items': {'type': 'string'},
                                },
                                'contribution_group_ids': {
                                    'type': ['null', 'array'],
                                    'description': 'Contribution group IDs',
                                    'items': {'type': 'integer'},
                                },
                                'org_contribution_group_ids': {
                                    'type': ['null', 'array'],
                                    'description': 'Organization contribution group IDs',
                                    'items': {'type': 'string'},
                                },
                                'scope': {
                                    'type': ['null', 'integer', 'object'],
                                    'description': 'Agent scope details (integer for scope level or object for detailed scope)',
                                },
                                'availability': {
                                    'type': ['null', 'array', 'object'],
                                    'description': 'Agent availability details',
                                    'items': {'type': 'object'},
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Agent creation timestamp',
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Agent last update timestamp',
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'agents',
                        },
                    },
                    preferred_for_check=True,
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/agents/{id}',
                    action=Action.GET,
                    description='Get a single agent by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Freshdesk agent',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique agent ID'},
                            'available': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the agent is available',
                            },
                            'available_since': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp since the agent has been available',
                            },
                            'occasional': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the agent is an occasional agent',
                            },
                            'signature': {
                                'type': ['null', 'string'],
                                'description': 'Signature of the agent (HTML)',
                            },
                            'ticket_scope': {
                                'type': ['null', 'integer'],
                                'description': 'Ticket scope: 1=Global, 2=Group, 3=Restricted',
                            },
                            'type': {
                                'type': ['null', 'string'],
                                'description': 'Agent type: support_agent, field_agent, collaborator',
                            },
                            'skill_ids': {
                                'type': ['null', 'array'],
                                'description': 'Skill IDs associated with the agent',
                                'items': {'type': 'integer'},
                            },
                            'group_ids': {
                                'type': ['null', 'array'],
                                'description': 'Group IDs the agent belongs to',
                                'items': {'type': 'integer'},
                            },
                            'role_ids': {
                                'type': ['null', 'array'],
                                'description': 'Role IDs assigned to the agent',
                                'items': {'type': 'integer'},
                            },
                            'focus_mode': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether focus mode is enabled',
                            },
                            'contact': {
                                'type': ['null', 'object'],
                                'description': 'Contact details of the agent',
                                'properties': {
                                    'active': {
                                        'type': ['null', 'boolean'],
                                        'description': 'Whether the contact is active',
                                    },
                                    'email': {
                                        'type': ['null', 'string'],
                                        'description': 'Email of the agent',
                                    },
                                    'job_title': {
                                        'type': ['null', 'string'],
                                        'description': 'Job title',
                                    },
                                    'language': {
                                        'type': ['null', 'string'],
                                        'description': 'Language',
                                    },
                                    'last_login_at': {
                                        'type': ['null', 'string'],
                                        'format': 'date-time',
                                        'description': 'Last login timestamp',
                                    },
                                    'mobile': {
                                        'type': ['null', 'string'],
                                        'description': 'Mobile number',
                                    },
                                    'name': {
                                        'type': ['null', 'string'],
                                        'description': 'Name of the agent',
                                    },
                                    'phone': {
                                        'type': ['null', 'string'],
                                        'description': 'Phone number',
                                    },
                                    'time_zone': {
                                        'type': ['null', 'string'],
                                        'description': 'Time zone',
                                    },
                                    'created_at': {
                                        'type': ['null', 'string'],
                                        'format': 'date-time',
                                        'description': 'Contact creation timestamp',
                                    },
                                    'updated_at': {
                                        'type': ['null', 'string'],
                                        'format': 'date-time',
                                        'description': 'Contact update timestamp',
                                    },
                                },
                            },
                            'last_active_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Timestamp of last agent activity',
                            },
                            'deactivated': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the agent is deactivated',
                            },
                            'agent_operational_status': {
                                'type': ['null', 'string'],
                                'description': 'Operational status of the agent',
                            },
                            'org_agent_id': {
                                'type': ['null', 'string'],
                                'description': 'Organization agent ID',
                            },
                            'org_group_ids': {
                                'type': ['null', 'array'],
                                'description': 'Organization group IDs',
                                'items': {'type': 'string'},
                            },
                            'contribution_group_ids': {
                                'type': ['null', 'array'],
                                'description': 'Contribution group IDs',
                                'items': {'type': 'integer'},
                            },
                            'org_contribution_group_ids': {
                                'type': ['null', 'array'],
                                'description': 'Organization contribution group IDs',
                                'items': {'type': 'string'},
                            },
                            'scope': {
                                'type': ['null', 'integer', 'object'],
                                'description': 'Agent scope details (integer for scope level or object for detailed scope)',
                            },
                            'availability': {
                                'type': ['null', 'array', 'object'],
                                'description': 'Agent availability details',
                                'items': {'type': 'object'},
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Agent creation timestamp',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Agent last update timestamp',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'agents',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Freshdesk agent',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique agent ID'},
                    'available': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the agent is available',
                    },
                    'available_since': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp since the agent has been available',
                    },
                    'occasional': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the agent is an occasional agent',
                    },
                    'signature': {
                        'type': ['null', 'string'],
                        'description': 'Signature of the agent (HTML)',
                    },
                    'ticket_scope': {
                        'type': ['null', 'integer'],
                        'description': 'Ticket scope: 1=Global, 2=Group, 3=Restricted',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Agent type: support_agent, field_agent, collaborator',
                    },
                    'skill_ids': {
                        'type': ['null', 'array'],
                        'description': 'Skill IDs associated with the agent',
                        'items': {'type': 'integer'},
                    },
                    'group_ids': {
                        'type': ['null', 'array'],
                        'description': 'Group IDs the agent belongs to',
                        'items': {'type': 'integer'},
                    },
                    'role_ids': {
                        'type': ['null', 'array'],
                        'description': 'Role IDs assigned to the agent',
                        'items': {'type': 'integer'},
                    },
                    'focus_mode': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether focus mode is enabled',
                    },
                    'contact': {
                        'type': ['null', 'object'],
                        'description': 'Contact details of the agent',
                        'properties': {
                            'active': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether the contact is active',
                            },
                            'email': {
                                'type': ['null', 'string'],
                                'description': 'Email of the agent',
                            },
                            'job_title': {
                                'type': ['null', 'string'],
                                'description': 'Job title',
                            },
                            'language': {
                                'type': ['null', 'string'],
                                'description': 'Language',
                            },
                            'last_login_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Last login timestamp',
                            },
                            'mobile': {
                                'type': ['null', 'string'],
                                'description': 'Mobile number',
                            },
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the agent',
                            },
                            'phone': {
                                'type': ['null', 'string'],
                                'description': 'Phone number',
                            },
                            'time_zone': {
                                'type': ['null', 'string'],
                                'description': 'Time zone',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Contact creation timestamp',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Contact update timestamp',
                            },
                        },
                    },
                    'last_active_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Timestamp of last agent activity',
                    },
                    'deactivated': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the agent is deactivated',
                    },
                    'agent_operational_status': {
                        'type': ['null', 'string'],
                        'description': 'Operational status of the agent',
                    },
                    'org_agent_id': {
                        'type': ['null', 'string'],
                        'description': 'Organization agent ID',
                    },
                    'org_group_ids': {
                        'type': ['null', 'array'],
                        'description': 'Organization group IDs',
                        'items': {'type': 'string'},
                    },
                    'contribution_group_ids': {
                        'type': ['null', 'array'],
                        'description': 'Contribution group IDs',
                        'items': {'type': 'integer'},
                    },
                    'org_contribution_group_ids': {
                        'type': ['null', 'array'],
                        'description': 'Organization contribution group IDs',
                        'items': {'type': 'string'},
                    },
                    'scope': {
                        'type': ['null', 'integer', 'object'],
                        'description': 'Agent scope details (integer for scope level or object for detailed scope)',
                    },
                    'availability': {
                        'type': ['null', 'array', 'object'],
                        'description': 'Agent availability details',
                        'items': {'type': 'object'},
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Agent creation timestamp',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Agent last update timestamp',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'agents',
            },
        ),
        EntityDefinition(
            name='groups',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/groups',
                    action=Action.LIST,
                    description='Returns a paginated list of groups',
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
                            'description': 'A Freshdesk group',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique group ID'},
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Name of the group',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Description of the group',
                                },
                                'agent_ids': {
                                    'type': ['null', 'array'],
                                    'description': 'IDs of agents in the group',
                                    'items': {'type': 'integer'},
                                },
                                'auto_ticket_assign': {
                                    'type': ['null', 'integer'],
                                    'description': 'Auto ticket assignment: 0=Disabled, 1=Round Robin, 2=Skill Based, 3=Load Based',
                                },
                                'business_hour_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the associated business hour',
                                },
                                'escalate_to': {
                                    'type': ['null', 'integer'],
                                    'description': 'User ID for escalation',
                                },
                                'unassigned_for': {
                                    'type': ['null', 'string'],
                                    'description': 'Time after which escalation triggers',
                                },
                                'group_type': {
                                    'type': ['null', 'string'],
                                    'description': 'Type of the group (e.g., support_agent_group)',
                                },
                                'allow_agents_to_change_availability': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether agents can change their availability',
                                },
                                'agent_availability_status': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether agent availability status is enabled',
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Group creation timestamp',
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Group last update timestamp',
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'groups',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/groups/{id}',
                    action=Action.GET,
                    description='Get a single group by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Freshdesk group',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique group ID'},
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the group',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Description of the group',
                            },
                            'agent_ids': {
                                'type': ['null', 'array'],
                                'description': 'IDs of agents in the group',
                                'items': {'type': 'integer'},
                            },
                            'auto_ticket_assign': {
                                'type': ['null', 'integer'],
                                'description': 'Auto ticket assignment: 0=Disabled, 1=Round Robin, 2=Skill Based, 3=Load Based',
                            },
                            'business_hour_id': {
                                'type': ['null', 'integer'],
                                'description': 'ID of the associated business hour',
                            },
                            'escalate_to': {
                                'type': ['null', 'integer'],
                                'description': 'User ID for escalation',
                            },
                            'unassigned_for': {
                                'type': ['null', 'string'],
                                'description': 'Time after which escalation triggers',
                            },
                            'group_type': {
                                'type': ['null', 'string'],
                                'description': 'Type of the group (e.g., support_agent_group)',
                            },
                            'allow_agents_to_change_availability': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether agents can change their availability',
                            },
                            'agent_availability_status': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether agent availability status is enabled',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Group creation timestamp',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Group last update timestamp',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'groups',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Freshdesk group',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique group ID'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the group',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Description of the group',
                    },
                    'agent_ids': {
                        'type': ['null', 'array'],
                        'description': 'IDs of agents in the group',
                        'items': {'type': 'integer'},
                    },
                    'auto_ticket_assign': {
                        'type': ['null', 'integer'],
                        'description': 'Auto ticket assignment: 0=Disabled, 1=Round Robin, 2=Skill Based, 3=Load Based',
                    },
                    'business_hour_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the associated business hour',
                    },
                    'escalate_to': {
                        'type': ['null', 'integer'],
                        'description': 'User ID for escalation',
                    },
                    'unassigned_for': {
                        'type': ['null', 'string'],
                        'description': 'Time after which escalation triggers',
                    },
                    'group_type': {
                        'type': ['null', 'string'],
                        'description': 'Type of the group (e.g., support_agent_group)',
                    },
                    'allow_agents_to_change_availability': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether agents can change their availability',
                    },
                    'agent_availability_status': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether agent availability status is enabled',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Group creation timestamp',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Group last update timestamp',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'groups',
            },
        ),
        EntityDefinition(
            name='companies',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/companies',
                    action=Action.LIST,
                    description='Returns a paginated list of companies',
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
                            'description': 'A Freshdesk company',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique company ID'},
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Name of the company',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Description of the company',
                                },
                                'domains': {
                                    'type': ['null', 'array'],
                                    'description': 'Email domains associated with the company',
                                    'items': {'type': 'string'},
                                },
                                'note': {
                                    'type': ['null', 'string'],
                                    'description': 'Notes about the company',
                                },
                                'health_score': {
                                    'type': ['null', 'string'],
                                    'description': 'Health score of the company',
                                },
                                'account_tier': {
                                    'type': ['null', 'string'],
                                    'description': 'Account tier of the company',
                                },
                                'renewal_date': {
                                    'type': ['null', 'string'],
                                    'format': 'date',
                                    'description': 'Renewal date',
                                },
                                'industry': {
                                    'type': ['null', 'string'],
                                    'description': 'Industry of the company',
                                },
                                'custom_fields': {
                                    'type': ['null', 'object'],
                                    'description': 'Custom fields associated with the company',
                                },
                                'org_company_id': {
                                    'type': ['null', 'integer', 'string'],
                                    'description': 'Organization company ID',
                                },
                                'org_company_id_str': {
                                    'type': ['null', 'string'],
                                    'description': 'Organization company ID as string',
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Company creation timestamp',
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Company last update timestamp',
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'companies',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/companies/{id}',
                    action=Action.GET,
                    description='Get a single company by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Freshdesk company',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique company ID'},
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the company',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Description of the company',
                            },
                            'domains': {
                                'type': ['null', 'array'],
                                'description': 'Email domains associated with the company',
                                'items': {'type': 'string'},
                            },
                            'note': {
                                'type': ['null', 'string'],
                                'description': 'Notes about the company',
                            },
                            'health_score': {
                                'type': ['null', 'string'],
                                'description': 'Health score of the company',
                            },
                            'account_tier': {
                                'type': ['null', 'string'],
                                'description': 'Account tier of the company',
                            },
                            'renewal_date': {
                                'type': ['null', 'string'],
                                'format': 'date',
                                'description': 'Renewal date',
                            },
                            'industry': {
                                'type': ['null', 'string'],
                                'description': 'Industry of the company',
                            },
                            'custom_fields': {
                                'type': ['null', 'object'],
                                'description': 'Custom fields associated with the company',
                            },
                            'org_company_id': {
                                'type': ['null', 'integer', 'string'],
                                'description': 'Organization company ID',
                            },
                            'org_company_id_str': {
                                'type': ['null', 'string'],
                                'description': 'Organization company ID as string',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Company creation timestamp',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Company last update timestamp',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'companies',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Freshdesk company',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique company ID'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the company',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Description of the company',
                    },
                    'domains': {
                        'type': ['null', 'array'],
                        'description': 'Email domains associated with the company',
                        'items': {'type': 'string'},
                    },
                    'note': {
                        'type': ['null', 'string'],
                        'description': 'Notes about the company',
                    },
                    'health_score': {
                        'type': ['null', 'string'],
                        'description': 'Health score of the company',
                    },
                    'account_tier': {
                        'type': ['null', 'string'],
                        'description': 'Account tier of the company',
                    },
                    'renewal_date': {
                        'type': ['null', 'string'],
                        'format': 'date',
                        'description': 'Renewal date',
                    },
                    'industry': {
                        'type': ['null', 'string'],
                        'description': 'Industry of the company',
                    },
                    'custom_fields': {
                        'type': ['null', 'object'],
                        'description': 'Custom fields associated with the company',
                    },
                    'org_company_id': {
                        'type': ['null', 'integer', 'string'],
                        'description': 'Organization company ID',
                    },
                    'org_company_id_str': {
                        'type': ['null', 'string'],
                        'description': 'Organization company ID as string',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Company creation timestamp',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Company last update timestamp',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'companies',
            },
        ),
        EntityDefinition(
            name='roles',
            actions=[Action.LIST, Action.GET],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/roles',
                    action=Action.LIST,
                    description='Returns a paginated list of roles',
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
                            'description': 'A Freshdesk role',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique role ID'},
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Name of the role',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Description of the role',
                                },
                                'default': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether this is a default role',
                                },
                                'agent_type': {
                                    'type': ['null', 'integer'],
                                    'description': 'Agent type associated with the role',
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Role creation timestamp',
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Role last update timestamp',
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'roles',
                        },
                    },
                ),
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/roles/{id}',
                    action=Action.GET,
                    description='Get a single role by ID',
                    path_params=['id'],
                    path_params_schema={
                        'id': {'type': 'integer', 'required': True},
                    },
                    response_schema={
                        'type': 'object',
                        'description': 'A Freshdesk role',
                        'properties': {
                            'id': {'type': 'integer', 'description': 'Unique role ID'},
                            'name': {
                                'type': ['null', 'string'],
                                'description': 'Name of the role',
                            },
                            'description': {
                                'type': ['null', 'string'],
                                'description': 'Description of the role',
                            },
                            'default': {
                                'type': ['null', 'boolean'],
                                'description': 'Whether this is a default role',
                            },
                            'agent_type': {
                                'type': ['null', 'integer'],
                                'description': 'Agent type associated with the role',
                            },
                            'created_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Role creation timestamp',
                            },
                            'updated_at': {
                                'type': ['null', 'string'],
                                'format': 'date-time',
                                'description': 'Role last update timestamp',
                            },
                        },
                        'required': ['id'],
                        'x-airbyte-entity-name': 'roles',
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Freshdesk role',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique role ID'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the role',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Description of the role',
                    },
                    'default': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is a default role',
                    },
                    'agent_type': {
                        'type': ['null', 'integer'],
                        'description': 'Agent type associated with the role',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Role creation timestamp',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Role last update timestamp',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'roles',
            },
        ),
        EntityDefinition(
            name='satisfaction_ratings',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/surveys/satisfaction_ratings',
                    action=Action.LIST,
                    description='Returns a paginated list of satisfaction ratings',
                    query_params=['per_page', 'page', 'created_since'],
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
                        'created_since': {'type': 'string', 'required': False},
                    },
                    response_schema={
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'description': 'A Freshdesk satisfaction rating',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique satisfaction rating ID'},
                                'survey_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the survey',
                                },
                                'user_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the user (requester)',
                                },
                                'agent_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the agent',
                                },
                                'group_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the group',
                                },
                                'ticket_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the ticket',
                                },
                                'feedback': {
                                    'type': ['null', 'string'],
                                    'description': 'Feedback text',
                                },
                                'ratings': {
                                    'type': ['null', 'object'],
                                    'description': 'Rating values (question_id to rating mapping)',
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Rating creation timestamp',
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Rating last update timestamp',
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'satisfaction_ratings',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Freshdesk satisfaction rating',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique satisfaction rating ID'},
                    'survey_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the survey',
                    },
                    'user_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the user (requester)',
                    },
                    'agent_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the agent',
                    },
                    'group_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the group',
                    },
                    'ticket_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the ticket',
                    },
                    'feedback': {
                        'type': ['null', 'string'],
                        'description': 'Feedback text',
                    },
                    'ratings': {
                        'type': ['null', 'object'],
                        'description': 'Rating values (question_id to rating mapping)',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Rating creation timestamp',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Rating last update timestamp',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'satisfaction_ratings',
            },
        ),
        EntityDefinition(
            name='surveys',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/surveys',
                    action=Action.LIST,
                    description='Returns a paginated list of surveys',
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
                            'description': 'A Freshdesk survey',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique survey ID'},
                                'title': {
                                    'type': ['null', 'string'],
                                    'description': 'Title of the survey',
                                },
                                'active': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the survey is active',
                                },
                                'questions': {
                                    'type': ['null', 'array'],
                                    'description': 'Survey questions',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': ['null', 'string'],
                                                'description': 'Question ID',
                                            },
                                            'label': {
                                                'type': ['null', 'string'],
                                                'description': 'Question label',
                                            },
                                            'accepted_ratings': {
                                                'type': ['null', 'array'],
                                                'description': 'Accepted rating values',
                                                'items': {'type': 'integer'},
                                            },
                                        },
                                    },
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Survey creation timestamp',
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Survey last update timestamp',
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'surveys',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Freshdesk survey',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique survey ID'},
                    'title': {
                        'type': ['null', 'string'],
                        'description': 'Title of the survey',
                    },
                    'active': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the survey is active',
                    },
                    'questions': {
                        'type': ['null', 'array'],
                        'description': 'Survey questions',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': ['null', 'string'],
                                    'description': 'Question ID',
                                },
                                'label': {
                                    'type': ['null', 'string'],
                                    'description': 'Question label',
                                },
                                'accepted_ratings': {
                                    'type': ['null', 'array'],
                                    'description': 'Accepted rating values',
                                    'items': {'type': 'integer'},
                                },
                            },
                        },
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Survey creation timestamp',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Survey last update timestamp',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'surveys',
            },
        ),
        EntityDefinition(
            name='time_entries',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/time_entries',
                    action=Action.LIST,
                    description='Returns a paginated list of time entries',
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
                            'description': 'A Freshdesk time entry',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique time entry ID'},
                                'agent_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the agent',
                                },
                                'ticket_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the associated ticket',
                                },
                                'company_id': {
                                    'type': ['null', 'integer'],
                                    'description': 'ID of the associated company',
                                },
                                'billable': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the time entry is billable',
                                },
                                'note': {
                                    'type': ['null', 'string'],
                                    'description': 'Description of the time entry',
                                },
                                'time_spent': {
                                    'type': ['null', 'string'],
                                    'description': 'Time spent in hh:mm format',
                                },
                                'timer_running': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the timer is running',
                                },
                                'executed_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Execution timestamp',
                                },
                                'start_time': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Start time of the timer',
                                },
                                'time_spent_in_seconds': {
                                    'type': ['null', 'integer'],
                                    'description': 'Time spent in seconds',
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Time entry creation timestamp',
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Time entry last update timestamp',
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'time_entries',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Freshdesk time entry',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique time entry ID'},
                    'agent_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the agent',
                    },
                    'ticket_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the associated ticket',
                    },
                    'company_id': {
                        'type': ['null', 'integer'],
                        'description': 'ID of the associated company',
                    },
                    'billable': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the time entry is billable',
                    },
                    'note': {
                        'type': ['null', 'string'],
                        'description': 'Description of the time entry',
                    },
                    'time_spent': {
                        'type': ['null', 'string'],
                        'description': 'Time spent in hh:mm format',
                    },
                    'timer_running': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the timer is running',
                    },
                    'executed_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Execution timestamp',
                    },
                    'start_time': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Start time of the timer',
                    },
                    'time_spent_in_seconds': {
                        'type': ['null', 'integer'],
                        'description': 'Time spent in seconds',
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Time entry creation timestamp',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Time entry last update timestamp',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'time_entries',
            },
        ),
        EntityDefinition(
            name='ticket_fields',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/ticket_fields',
                    action=Action.LIST,
                    description='Returns a list of all ticket fields',
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
                            'description': 'A Freshdesk ticket field definition',
                            'properties': {
                                'id': {'type': 'integer', 'description': 'Unique ticket field ID'},
                                'name': {
                                    'type': ['null', 'string'],
                                    'description': 'Name of the field',
                                },
                                'label': {
                                    'type': ['null', 'string'],
                                    'description': 'Display label for agents',
                                },
                                'label_for_customers': {
                                    'type': ['null', 'string'],
                                    'description': 'Display label in the customer portal',
                                },
                                'description': {
                                    'type': ['null', 'string'],
                                    'description': 'Description of the field',
                                },
                                'position': {
                                    'type': ['null', 'integer'],
                                    'description': 'Position of the field in the form',
                                },
                                'type': {
                                    'type': ['null', 'string'],
                                    'description': 'Field type (e.g., custom_dropdown, custom_text)',
                                },
                                'default': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether this is a default (non-custom) field',
                                },
                                'required_for_closure': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the field is required for ticket closure',
                                },
                                'required_for_agents': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the field is required for agents',
                                },
                                'required_for_customers': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the field is required for customers',
                                },
                                'customers_can_edit': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether customers can edit this field',
                                },
                                'displayed_to_customers': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether the field is displayed to customers',
                                },
                                'customers_can_filter': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether customers can use this field as a filter',
                                },
                                'portal_cc': {
                                    'type': ['null', 'boolean'],
                                    'description': 'Whether CC is enabled in the portal',
                                },
                                'portal_cc_to': {
                                    'type': ['null', 'string'],
                                    'description': 'CC recipients scope (all or company)',
                                },
                                'choices': {
                                    'description': 'Available choices for dropdown fields',
                                    'oneOf': [
                                        {'type': 'null'},
                                        {
                                            'type': 'array',
                                            'items': {
                                                'type': ['string', 'object'],
                                            },
                                        },
                                        {'type': 'object'},
                                    ],
                                },
                                'created_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Field creation timestamp',
                                },
                                'updated_at': {
                                    'type': ['null', 'string'],
                                    'format': 'date-time',
                                    'description': 'Field last update timestamp',
                                },
                            },
                            'required': ['id'],
                            'x-airbyte-entity-name': 'ticket_fields',
                        },
                    },
                ),
            },
            entity_schema={
                'type': 'object',
                'description': 'A Freshdesk ticket field definition',
                'properties': {
                    'id': {'type': 'integer', 'description': 'Unique ticket field ID'},
                    'name': {
                        'type': ['null', 'string'],
                        'description': 'Name of the field',
                    },
                    'label': {
                        'type': ['null', 'string'],
                        'description': 'Display label for agents',
                    },
                    'label_for_customers': {
                        'type': ['null', 'string'],
                        'description': 'Display label in the customer portal',
                    },
                    'description': {
                        'type': ['null', 'string'],
                        'description': 'Description of the field',
                    },
                    'position': {
                        'type': ['null', 'integer'],
                        'description': 'Position of the field in the form',
                    },
                    'type': {
                        'type': ['null', 'string'],
                        'description': 'Field type (e.g., custom_dropdown, custom_text)',
                    },
                    'default': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether this is a default (non-custom) field',
                    },
                    'required_for_closure': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the field is required for ticket closure',
                    },
                    'required_for_agents': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the field is required for agents',
                    },
                    'required_for_customers': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the field is required for customers',
                    },
                    'customers_can_edit': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether customers can edit this field',
                    },
                    'displayed_to_customers': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether the field is displayed to customers',
                    },
                    'customers_can_filter': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether customers can use this field as a filter',
                    },
                    'portal_cc': {
                        'type': ['null', 'boolean'],
                        'description': 'Whether CC is enabled in the portal',
                    },
                    'portal_cc_to': {
                        'type': ['null', 'string'],
                        'description': 'CC recipients scope (all or company)',
                    },
                    'choices': {
                        'description': 'Available choices for dropdown fields',
                        'oneOf': [
                            {'type': 'null'},
                            {
                                'type': 'array',
                                'items': {
                                    'type': ['string', 'object'],
                                },
                            },
                            {'type': 'object'},
                        ],
                    },
                    'created_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Field creation timestamp',
                    },
                    'updated_at': {
                        'type': ['null', 'string'],
                        'format': 'date-time',
                        'description': 'Field last update timestamp',
                    },
                },
                'required': ['id'],
                'x-airbyte-entity-name': 'ticket_fields',
            },
        ),
    ],
    search_field_paths={
        'tickets': [
            'id',
            'subject',
            'description',
            'description_text',
            'status',
            'priority',
            'source',
            'type',
            'requester_id',
            'requester',
            'responder_id',
            'group_id',
            'company_id',
            'product_id',
            'email_config_id',
            'cc_emails',
            'cc_emails[]',
            'ticket_cc_emails',
            'ticket_cc_emails[]',
            'to_emails',
            'to_emails[]',
            'fwd_emails',
            'fwd_emails[]',
            'reply_cc_emails',
            'reply_cc_emails[]',
            'tags',
            'tags[]',
            'custom_fields',
            'due_by',
            'fr_due_by',
            'fr_escalated',
            'is_escalated',
            'nr_due_by',
            'nr_escalated',
            'spam',
            'association_type',
            'associated_tickets_count',
            'stats',
            'created_at',
            'updated_at',
        ],
        'agents': [
            'id',
            'available',
            'available_since',
            'contact',
            'occasional',
            'signature',
            'ticket_scope',
            'type',
            'last_active_at',
            'created_at',
            'updated_at',
        ],
        'groups': [
            'id',
            'name',
            'description',
            'auto_ticket_assign',
            'business_hour_id',
            'escalate_to',
            'group_type',
            'unassigned_for',
            'created_at',
            'updated_at',
        ],
    },
)