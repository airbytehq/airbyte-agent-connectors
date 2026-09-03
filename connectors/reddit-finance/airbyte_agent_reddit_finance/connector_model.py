"""
Connector model for reddit-finance.

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
from uuid import (
    UUID,
)

RedditFinanceConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('30116aef-e047-41ed-8a09-348734afcaf1'),
    name='reddit-finance',
    version='0.1.0',
    base_url='https://www.reddit.com',
    auth=AuthConfig(
        type=AuthType.API_KEY,
        config={
            'header': 'User-Agent',
            'prefix': '',
        },
    ),
    entities=[
        EntityDefinition(
            name='subreddit_posts',
            actions=[
                Action.LIST,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/r/{subreddit}/{sort}.json',
                    action=Action.LIST,
                    description='Returns posts from a subreddit sorted by hot, new, or top',
                    path_params=['subreddit', 'sort'],
                    query_params=[
                        'limit',
                        'after',
                        'raw_json',
                    ],
                    query_params_schema={
                        'limit': {'type': 'integer', 'required': False, 'default': 100},
                        'after': {'type': 'string', 'required': False},
                        'raw_json': {'type': 'string', 'required': False, 'default': '1'},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'after': {'type': ['string', 'null']},
                                    'children': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'data': {'type': 'object'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.children[*].data',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Reddit post ID'},
                    'subreddit': {'type': ['string', 'null'], 'description': 'Subreddit name'},
                    'selftext': {'type': ['string', 'null'], 'description': 'Post body text'},
                    'author_fullname': {'type': ['string', 'null'], 'description': 'Author unique ID'},
                    'title': {'type': ['string', 'null'], 'description': 'Post title'},
                    'subreddit_name_prefixed': {'type': ['string', 'null'], 'description': 'Subreddit name with r/ prefix'},
                    'name': {'type': ['string', 'null'], 'description': 'Full name (kind_id)'},
                    'upvote_ratio': {'type': ['number', 'null'], 'description': 'Ratio of upvotes to total votes'},
                    'ups': {'type': ['number', 'null'], 'description': 'Number of upvotes'},
                    'score': {'type': ['number', 'null'], 'description': 'Post score'},
                    'created': {'type': ['number', 'null'], 'description': 'Creation timestamp (epoch)'},
                    'created_utc': {'type': ['number', 'null'], 'description': 'Creation timestamp UTC (epoch)'},
                    'num_comments': {'type': ['number', 'null'], 'description': 'Number of comments'},
                    'permalink': {'type': ['string', 'null'], 'description': 'Permalink to post'},
                    'url': {'type': ['string', 'null'], 'description': 'URL of the post or linked content'},
                    'is_self': {'type': ['boolean', 'null'], 'description': 'Whether the post is a self-post'},
                    'over_18': {'type': ['boolean', 'null'], 'description': 'Whether the post is NSFW'},
                    'author': {'type': ['string', 'null'], 'description': 'Author username'},
                    'link_flair_text': {'type': ['string', 'null'], 'description': 'Link flair text'},
                    'domain': {'type': ['string', 'null'], 'description': 'Domain of linked content'},
                    'saved': {'type': ['boolean', 'null'], 'description': 'Whether the post is saved'},
                    'gilded': {'type': ['number', 'null'], 'description': 'Number of times gilded'},
                    'clicked': {'type': ['boolean', 'null'], 'description': 'Whether the post was clicked'},
                    'hidden': {'type': ['boolean', 'null'], 'description': 'Whether the post is hidden'},
                    'pinned': {'type': ['boolean', 'null'], 'description': 'Whether the post is pinned'},
                    'stickied': {'type': ['boolean', 'null'], 'description': 'Whether the post is stickied'},
                    'num_crossposts': {'type': ['number', 'null'], 'description': 'Number of crossposts'},
                    'total_awards_received': {'type': ['number', 'null'], 'description': 'Total awards received'},
                    'subreddit_subscribers': {'type': ['number', 'null'], 'description': 'Number of subreddit subscribers'},
                },
                'required': ['id'],
            },
        ),
        EntityDefinition(
            name='subreddit_search',
            actions=[
                Action.LIST,
            ],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='GET',
                    path='/r/{subreddit}/search.json',
                    action=Action.LIST,
                    description='Search for posts in a subreddit matching a query (e.g. ticker symbols)',
                    path_params=['subreddit'],
                    query_params=[
                        'q',
                        'restrict_sr',
                        'sort',
                        'limit',
                        'after',
                        'raw_json',
                    ],
                    query_params_schema={
                        'q': {'type': 'string', 'required': True},
                        'restrict_sr': {'type': 'string', 'required': False, 'default': 'true'},
                        'sort': {'type': 'string', 'required': False, 'default': 'relevance', 'enum': ['relevance', 'hot', 'top', 'new', 'comments']},
                        'limit': {'type': 'integer', 'required': False, 'default': 100},
                        'after': {'type': 'string', 'required': False},
                        'raw_json': {'type': 'string', 'required': False, 'default': '1'},
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {
                                'type': 'object',
                                'properties': {
                                    'after': {'type': ['string', 'null']},
                                    'children': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'data': {'type': 'object'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.data.children[*].data',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'id': {'type': 'string', 'description': 'Reddit post ID'},
                    'subreddit': {'type': ['string', 'null'], 'description': 'Subreddit name'},
                    'selftext': {'type': ['string', 'null'], 'description': 'Post body text'},
                    'author_fullname': {'type': ['string', 'null'], 'description': 'Author unique ID'},
                    'title': {'type': ['string', 'null'], 'description': 'Post title'},
                    'subreddit_name_prefixed': {'type': ['string', 'null'], 'description': 'Subreddit name with r/ prefix'},
                    'name': {'type': ['string', 'null'], 'description': 'Full name (kind_id)'},
                    'upvote_ratio': {'type': ['number', 'null'], 'description': 'Ratio of upvotes to total votes'},
                    'ups': {'type': ['number', 'null'], 'description': 'Number of upvotes'},
                    'score': {'type': ['number', 'null'], 'description': 'Post score'},
                    'created': {'type': ['number', 'null'], 'description': 'Creation timestamp (epoch)'},
                    'created_utc': {'type': ['number', 'null'], 'description': 'Creation timestamp UTC (epoch)'},
                    'num_comments': {'type': ['number', 'null'], 'description': 'Number of comments'},
                    'permalink': {'type': ['string', 'null'], 'description': 'Permalink to post'},
                    'url': {'type': ['string', 'null'], 'description': 'URL of the post or linked content'},
                    'is_self': {'type': ['boolean', 'null'], 'description': 'Whether the post is a self-post'},
                    'over_18': {'type': ['boolean', 'null'], 'description': 'Whether the post is NSFW'},
                    'author': {'type': ['string', 'null'], 'description': 'Author username'},
                    'link_flair_text': {'type': ['string', 'null'], 'description': 'Link flair text'},
                    'domain': {'type': ['string', 'null'], 'description': 'Domain of linked content'},
                },
                'required': ['id'],
            },
        ),
        EntityDefinition(
            name='subreddit_info',
            actions=[
                Action.GET,
            ],
            endpoints={
                Action.GET: EndpointDefinition(
                    method='GET',
                    path='/r/{subreddit}/about.json',
                    action=Action.GET,
                    description='Returns information about a subreddit including subscriber count and description',
                    path_params=['subreddit'],
                    query_params=[],
                    query_params_schema={},
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'data': {'type': 'object'},
                        },
                    },
                    record_extractor='$.data',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'display_name': {'type': 'string', 'description': 'Subreddit display name'},
                    'title': {'type': ['string', 'null'], 'description': 'Subreddit title'},
                    'display_name_prefixed': {'type': ['string', 'null'], 'description': 'Subreddit name with r/ prefix'},
                    'public_description': {'type': ['string', 'null'], 'description': 'Public description text'},
                    'subscribers': {'type': ['number', 'null'], 'description': 'Number of subscribers'},
                    'accounts_active': {'type': ['number', 'null'], 'description': 'Number of active accounts'},
                    'created': {'type': ['number', 'null'], 'description': 'Creation timestamp (epoch)'},
                    'created_utc': {'type': ['number', 'null'], 'description': 'Creation timestamp UTC (epoch)'},
                    'over18': {'type': ['boolean', 'null'], 'description': 'Whether subreddit is NSFW'},
                    'wiki_enabled': {'type': ['boolean', 'null'], 'description': 'Whether wiki is enabled'},
                    'icon_img': {'type': ['string', 'null'], 'description': 'Subreddit icon image URL'},
                    'header_img': {'type': ['string', 'null'], 'description': 'Subreddit header image URL'},
                    'primary_color': {'type': ['string', 'null'], 'description': 'Primary theme color'},
                    'key_color': {'type': ['string', 'null'], 'description': 'Key theme color'},
                    'url': {'type': ['string', 'null'], 'description': 'Subreddit URL path'},
                    'subreddit_type': {'type': ['string', 'null'], 'description': 'Subreddit type'},
                    'lang': {'type': ['string', 'null'], 'description': 'Subreddit language'},
                    'allow_galleries': {'type': ['boolean', 'null'], 'description': 'Whether galleries are allowed'},
                    'restrict_posting': {'type': ['boolean', 'null'], 'description': 'Whether posting is restricted'},
                },
                'required': ['display_name'],
            },
        ),
    ],
)
