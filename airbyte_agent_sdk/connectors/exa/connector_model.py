"""
Connector model for exa.

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
from airbyte_agent_sdk.schema.base import (
    ExampleQuestions,
)
from uuid import (
    UUID,
)

ExaConnectorModel: ConnectorModel = ConnectorModel(
    id=UUID('7c3acca3-8781-4a4b-bb10-fd2e4500da18'),
    name='exa',
    base_url='https://api.exa.ai',
    auth=AuthConfig(
        type=AuthType.API_KEY,
        config={'header': 'x-api-key', 'in': 'header'},
        user_config_spec=AuthConfigSpec(
            title='API Key Authentication',
            type='object',
            required=['api_key'],
            properties={
                'api_key': AuthConfigFieldSpec(
                    title='API Key',
                    description='Your Exa API key from dashboard.exa.ai/api-keys',
                    airbyte_secret=True,
                ),
            },
            auth_mapping={'api_key': '${api_key}'},
        ),
    ),
    entities=[
        EntityDefinition(
            name='search_results',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/search',
                    action=Action.LIST,
                    description='Perform a search with an Exa prompt-engineered query and retrieve a list\nof relevant results. Optionally request contents (text, highlights, summary)\ninline with the search results. Supports filtering by domain, date, category,\nand number of results.\n',
                    body_fields=[
                        'query',
                        'type',
                        'category',
                        'numResults',
                        'includeDomains',
                        'excludeDomains',
                        'startPublishedDate',
                        'endPublishedDate',
                        'startCrawlDate',
                        'endCrawlDate',
                        'contents',
                        'moderation',
                    ],
                    request_body_defaults={
                        'query': 'latest news on Airbyte',
                        'type': 'auto',
                        'numResults': 10,
                        'moderation': False,
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'query': {
                                'type': 'string',
                                'default': 'latest news on Airbyte',
                                'description': 'The search query string.',
                            },
                            'type': {
                                'type': 'string',
                                'enum': [
                                    'auto',
                                    'instant',
                                    'fast',
                                    'deep-lite',
                                    'deep',
                                    'deep-reasoning',
                                ],
                                'default': 'auto',
                                'description': 'The type of search. auto intelligently selects the best mode, instant provides lowest latency, fast uses lower-latency models, deep-lite provides lightweight synthesis, deep performs in-depth research with synthesis, and deep-reasoning adds more reasoning for complex searches.',
                            },
                            'category': {
                                'type': 'string',
                                'enum': [
                                    'company',
                                    'research paper',
                                    'news',
                                    'personal site',
                                    'financial report',
                                    'people',
                                ],
                                'description': 'A data category to focus on for improved result quality.',
                            },
                            'numResults': {
                                'type': 'integer',
                                'minimum': 1,
                                'maximum': 100,
                                'default': 10,
                                'description': 'Number of results to return (max 100).',
                            },
                            'includeDomains': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'List of domains to include. If specified, results will only come from these domains.',
                            },
                            'excludeDomains': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'List of domains to exclude. If specified, no results will be returned from these domains.',
                            },
                            'startPublishedDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Only return links published after this date. ISO 8601 format.',
                            },
                            'endPublishedDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Only return links published before this date. ISO 8601 format.',
                            },
                            'startCrawlDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Only return links crawled by Exa after this date. ISO 8601 format.',
                            },
                            'endCrawlDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Only return links crawled by Exa before this date. ISO 8601 format.',
                            },
                            'contents': {
                                'type': 'object',
                                'description': 'Options for requesting page contents inline with search results.',
                                'properties': {
                                    'text': {
                                        'oneOf': [
                                            {'type': 'boolean'},
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'maxCharacters': {
                                                        'type': 'integer',
                                                        'minimum': 1,
                                                        'maximum': 10000,
                                                        'description': 'Maximum character limit for the text.',
                                                    },
                                                    'includeHtmlTags': {
                                                        'type': 'boolean',
                                                        'default': False,
                                                        'description': 'Include lightweight HTML tags in returned text.',
                                                    },
                                                },
                                            },
                                        ],
                                        'description': 'Text extraction options. Pass true for defaults or an object for advanced options.',
                                    },
                                    'highlights': {
                                        'oneOf': [
                                            {'type': 'boolean'},
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'query': {'type': 'string', 'description': 'Custom query to guide highlight selection.'},
                                                    'maxCharacters': {
                                                        'type': 'integer',
                                                        'minimum': 1,
                                                        'maximum': 10000,
                                                        'description': 'Maximum characters for highlights.',
                                                    },
                                                },
                                            },
                                        ],
                                        'description': 'Highlight extraction options. Pass true for defaults or an object for advanced options.',
                                    },
                                    'summary': {
                                        'type': 'object',
                                        'properties': {
                                            'query': {'type': 'string', 'description': 'Custom query for the LLM-generated summary.'},
                                        },
                                        'description': 'Summary generation options.',
                                    },
                                },
                            },
                            'moderation': {
                                'type': 'boolean',
                                'default': False,
                                'description': 'Enable content moderation to filter unsafe content.',
                            },
                        },
                        'required': ['query'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Unique identifier for the request.'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'title': {'type': 'string', 'description': 'The title of the search result.'},
                                        'url': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'The URL of the search result.',
                                        },
                                        'id': {'type': 'string', 'description': 'Temporary document ID. Useful for the /contents endpoint.'},
                                        'publishedDate': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Estimated creation date of the content, in ISO 8601 format.',
                                        },
                                        'author': {
                                            'type': ['string', 'null'],
                                            'description': 'The author of the content, if available.',
                                        },
                                        'image': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'URL of an image associated with the result, if available.',
                                        },
                                        'favicon': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': "URL of the favicon for the result's domain.",
                                        },
                                        'text': {'type': 'string', 'description': 'Full content text of the result. Only present when contents.text is requested.'},
                                        'highlights': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                            'description': 'Highlighted text snippets from the result. Only present when contents.highlights is requested.',
                                        },
                                        'highlightScores': {
                                            'type': 'array',
                                            'items': {'type': 'number'},
                                            'description': 'Cosine similarity scores for each highlighted snippet.',
                                        },
                                        'summary': {'type': 'string', 'description': 'LLM-generated summary of the page. Only present when contents.summary is requested.'},
                                        'score': {'type': 'number', 'description': 'Relevance score for the result.'},
                                    },
                                    'x-airbyte-entity-name': 'search_results',
                                    'x-airbyte-ai-hints': {
                                        'summary': "Web search results from Exa's embeddings-based search engine",
                                        'when_to_use': 'When the user wants to search the web for information, articles, research papers, or news',
                                        'trigger_phrases': [
                                            'search the web for',
                                            'find articles about',
                                            'look up',
                                            'search for',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Search for recent articles about large language models', 'Find research papers about transformer architectures', 'Search for AI startup company pages'],
                                        'search_strategy': "Use natural language queries describing what you're looking for",
                                    },
                                },
                                'description': 'List of search results.',
                            },
                            'resolvedSearchType': {'type': 'string', 'description': 'Deprecated legacy field. May return an empty string.'},
                            'searchTime': {'type': 'number', 'description': 'Time taken for the search in milliseconds.'},
                            'costDollars': {
                                'type': 'object',
                                'description': 'Estimated cost breakdown for the request.',
                                'properties': {
                                    'total': {'type': 'number', 'description': 'Estimated total dollar cost for the request.'},
                                    'search': {
                                        'type': 'object',
                                        'properties': {
                                            'neural': {'type': 'number', 'description': 'Cost for neural search.'},
                                        },
                                    },
                                    'contents': {
                                        'type': 'object',
                                        'description': 'Cost breakdown for contents retrieval.',
                                        'properties': {
                                            'text': {'type': 'number', 'description': 'Cost for text extraction.'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    no_pagination='Search endpoint returns all results in a single response controlled by numResults parameter',
                    preferred_for_check=True,
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'title': {'type': 'string', 'description': 'The title of the search result.'},
                    'url': {
                        'type': 'string',
                        'format': 'uri',
                        'description': 'The URL of the search result.',
                    },
                    'id': {'type': 'string', 'description': 'Temporary document ID. Useful for the /contents endpoint.'},
                    'publishedDate': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Estimated creation date of the content, in ISO 8601 format.',
                    },
                    'author': {
                        'type': ['string', 'null'],
                        'description': 'The author of the content, if available.',
                    },
                    'image': {
                        'type': 'string',
                        'format': 'uri',
                        'description': 'URL of an image associated with the result, if available.',
                    },
                    'favicon': {
                        'type': 'string',
                        'format': 'uri',
                        'description': "URL of the favicon for the result's domain.",
                    },
                    'text': {'type': 'string', 'description': 'Full content text of the result. Only present when contents.text is requested.'},
                    'highlights': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Highlighted text snippets from the result. Only present when contents.highlights is requested.',
                    },
                    'highlightScores': {
                        'type': 'array',
                        'items': {'type': 'number'},
                        'description': 'Cosine similarity scores for each highlighted snippet.',
                    },
                    'summary': {'type': 'string', 'description': 'LLM-generated summary of the page. Only present when contents.summary is requested.'},
                    'score': {'type': 'number', 'description': 'Relevance score for the result.'},
                },
                'x-airbyte-entity-name': 'search_results',
                'x-airbyte-ai-hints': {
                    'summary': "Web search results from Exa's embeddings-based search engine",
                    'when_to_use': 'When the user wants to search the web for information, articles, research papers, or news',
                    'trigger_phrases': [
                        'search the web for',
                        'find articles about',
                        'look up',
                        'search for',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Search for recent articles about large language models', 'Find research papers about transformer architectures', 'Search for AI startup company pages'],
                    'search_strategy': "Use natural language queries describing what you're looking for",
                },
            },
            ai_hints={
                'summary': "Web search results from Exa's embeddings-based search engine",
                'when_to_use': 'When the user wants to search the web for information, articles, research papers, or news',
                'trigger_phrases': [
                    'search the web for',
                    'find articles about',
                    'look up',
                    'search for',
                ],
                'freshness': 'live',
                'example_questions': ['Search for recent articles about large language models', 'Find research papers about transformer architectures', 'Search for AI startup company pages'],
                'search_strategy': "Use natural language queries describing what you're looking for",
            },
        ),
        EntityDefinition(
            name='contents',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/contents',
                    action=Action.LIST,
                    description="Get the full page contents, summaries, and metadata for a list of URLs.\nReturns instant results from Exa's cache, with automatic live crawling\nas fallback for uncached pages. Use this to retrieve text, highlights,\nand summaries for specific URLs.\n",
                    body_fields=[
                        'urls',
                        'text',
                        'highlights',
                        'summary',
                    ],
                    request_body_probe_defaults={
                        'urls': ['https://airbyte.io'],
                    },
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'urls': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'minItems': 1,
                                'maxItems': 100,
                                'description': 'Array of URLs to retrieve contents for.',
                                'x-airbyte-probe-default': ['https://airbyte.io'],
                            },
                            'text': {
                                'oneOf': [
                                    {'type': 'boolean'},
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'maxCharacters': {
                                                'type': 'integer',
                                                'minimum': 1,
                                                'maximum': 10000,
                                                'description': 'Maximum character limit for the text.',
                                            },
                                            'includeHtmlTags': {
                                                'type': 'boolean',
                                                'default': False,
                                                'description': 'Include lightweight HTML tags in returned text.',
                                            },
                                        },
                                    },
                                ],
                                'description': 'Text extraction options. Pass true for defaults or an object for advanced options.',
                            },
                            'highlights': {
                                'oneOf': [
                                    {'type': 'boolean'},
                                    {
                                        'type': 'object',
                                        'properties': {
                                            'query': {'type': 'string', 'description': 'Custom query to guide highlight selection.'},
                                            'maxCharacters': {
                                                'type': 'integer',
                                                'minimum': 1,
                                                'maximum': 10000,
                                                'description': 'Maximum characters for highlights.',
                                            },
                                        },
                                    },
                                ],
                                'description': 'Highlight extraction options. Pass true for defaults or an object for advanced options.',
                            },
                            'summary': {
                                'type': 'object',
                                'properties': {
                                    'query': {'type': 'string', 'description': 'Custom query for the LLM-generated summary.'},
                                },
                                'description': 'Summary generation options.',
                            },
                        },
                        'required': ['urls'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Unique identifier for the request.'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'title': {'type': 'string', 'description': 'The title of the search result.'},
                                        'url': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'The URL of the search result.',
                                        },
                                        'id': {'type': 'string', 'description': 'Temporary document ID. Useful for the /contents endpoint.'},
                                        'publishedDate': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Estimated creation date of the content, in ISO 8601 format.',
                                        },
                                        'author': {
                                            'type': ['string', 'null'],
                                            'description': 'The author of the content, if available.',
                                        },
                                        'image': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'URL of an image associated with the result, if available.',
                                        },
                                        'favicon': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': "URL of the favicon for the result's domain.",
                                        },
                                        'text': {'type': 'string', 'description': 'Full content text of the result. Only present when contents.text is requested.'},
                                        'highlights': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                            'description': 'Highlighted text snippets from the result. Only present when contents.highlights is requested.',
                                        },
                                        'highlightScores': {
                                            'type': 'array',
                                            'items': {'type': 'number'},
                                            'description': 'Cosine similarity scores for each highlighted snippet.',
                                        },
                                        'summary': {'type': 'string', 'description': 'LLM-generated summary of the page. Only present when contents.summary is requested.'},
                                        'score': {'type': 'number', 'description': 'Relevance score for the result.'},
                                    },
                                    'x-airbyte-entity-name': 'search_results',
                                    'x-airbyte-ai-hints': {
                                        'summary': "Web search results from Exa's embeddings-based search engine",
                                        'when_to_use': 'When the user wants to search the web for information, articles, research papers, or news',
                                        'trigger_phrases': [
                                            'search the web for',
                                            'find articles about',
                                            'look up',
                                            'search for',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Search for recent articles about large language models', 'Find research papers about transformer architectures', 'Search for AI startup company pages'],
                                        'search_strategy': "Use natural language queries describing what you're looking for",
                                    },
                                },
                                'description': 'List of content results.',
                            },
                            'statuses': {
                                'type': 'array',
                                'description': 'Status information for each requested URL.',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'id': {'type': 'string', 'description': 'The URL or document ID that was requested.'},
                                        'status': {
                                            'type': 'string',
                                            'enum': ['success', 'error'],
                                            'description': 'Status of the content fetch.',
                                        },
                                        'source': {
                                            'type': 'string',
                                            'enum': ['cached', 'crawled'],
                                            'description': 'Where the content was sourced from.',
                                        },
                                    },
                                },
                            },
                            'searchTime': {'type': 'number', 'description': 'Time taken in milliseconds.'},
                            'costDollars': {
                                'type': 'object',
                                'description': 'Estimated cost breakdown for the request.',
                                'properties': {
                                    'total': {'type': 'number', 'description': 'Estimated total dollar cost for the request.'},
                                    'search': {
                                        'type': 'object',
                                        'properties': {
                                            'neural': {'type': 'number', 'description': 'Cost for neural search.'},
                                        },
                                    },
                                    'contents': {
                                        'type': 'object',
                                        'description': 'Cost breakdown for contents retrieval.',
                                        'properties': {
                                            'text': {'type': 'number', 'description': 'Cost for text extraction.'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    no_pagination='Contents endpoint returns all requested URLs in a single response',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'title': {'type': 'string', 'description': 'The title of the page.'},
                    'url': {
                        'type': 'string',
                        'format': 'uri',
                        'description': 'The URL of the page.',
                    },
                    'id': {'type': 'string', 'description': 'Temporary document ID.'},
                    'publishedDate': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Estimated creation date of the content, in ISO 8601 format.',
                    },
                    'author': {
                        'type': ['string', 'null'],
                        'description': 'The author of the content, if available.',
                    },
                    'image': {
                        'type': 'string',
                        'format': 'uri',
                        'description': 'URL of an image associated with the page, if available.',
                    },
                    'favicon': {
                        'type': 'string',
                        'format': 'uri',
                        'description': "URL of the favicon for the page's domain.",
                    },
                    'text': {'type': 'string', 'description': 'Full content text of the page.'},
                    'highlights': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Highlighted text snippets from the page.',
                    },
                    'highlightScores': {
                        'type': 'array',
                        'items': {'type': 'number'},
                        'description': 'Cosine similarity scores for each highlighted snippet.',
                    },
                    'summary': {'type': 'string', 'description': 'LLM-generated summary of the page.'},
                    'score': {'type': 'number', 'description': 'Relevance score for the result.'},
                },
                'x-airbyte-entity-name': 'contents',
                'x-airbyte-ai-hints': {
                    'summary': 'Full page contents, text, and metadata for given URLs',
                    'when_to_use': 'When the user wants to get the full text, highlights, or summary of specific web pages by URL',
                    'trigger_phrases': [
                        'get the contents of',
                        'extract text from',
                        'read this page',
                        'get page content',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Get the full text of this web page', 'Extract highlights from this blog post'],
                    'search_strategy': 'Provide URLs to retrieve their contents',
                },
            },
            ai_hints={
                'summary': 'Full page contents, text, and metadata for given URLs',
                'when_to_use': 'When the user wants to get the full text, highlights, or summary of specific web pages by URL',
                'trigger_phrases': [
                    'get the contents of',
                    'extract text from',
                    'read this page',
                    'get page content',
                ],
                'freshness': 'live',
                'example_questions': ['Get the full text of this web page', 'Extract highlights from this blog post'],
                'search_strategy': 'Provide URLs to retrieve their contents',
            },
        ),
        EntityDefinition(
            name='similar_results',
            actions=[Action.LIST],
            endpoints={
                Action.LIST: EndpointDefinition(
                    method='POST',
                    path='/findSimilar',
                    action=Action.LIST,
                    description="Find web pages similar to a given URL. Uses Exa's embeddings to find\nsemantically similar content. Supports filtering by domains and dates.\n",
                    body_fields=[
                        'url',
                        'numResults',
                        'includeDomains',
                        'excludeDomains',
                        'startPublishedDate',
                        'endPublishedDate',
                        'startCrawlDate',
                        'endCrawlDate',
                        'contents',
                    ],
                    request_body_defaults={'numResults': 10},
                    request_body_probe_defaults={'url': 'https://airbyte.io'},
                    request_schema={
                        'type': 'object',
                        'properties': {
                            'url': {
                                'type': 'string',
                                'description': 'The URL to find similar pages for.',
                                'x-airbyte-probe-default': 'https://airbyte.io',
                            },
                            'numResults': {
                                'type': 'integer',
                                'minimum': 1,
                                'maximum': 100,
                                'default': 10,
                                'description': 'Number of similar results to return (max 100).',
                            },
                            'includeDomains': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'List of domains to include. If specified, results will only come from these domains.',
                            },
                            'excludeDomains': {
                                'type': 'array',
                                'items': {'type': 'string'},
                                'description': 'List of domains to exclude. If specified, no results will be returned from these domains.',
                            },
                            'startPublishedDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Only return links published after this date. ISO 8601 format.',
                            },
                            'endPublishedDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Only return links published before this date. ISO 8601 format.',
                            },
                            'startCrawlDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Only return links crawled by Exa after this date. ISO 8601 format.',
                            },
                            'endCrawlDate': {
                                'type': 'string',
                                'format': 'date-time',
                                'description': 'Only return links crawled by Exa before this date. ISO 8601 format.',
                            },
                            'contents': {
                                'type': 'object',
                                'description': 'Options for requesting page contents inline with similar page results.',
                                'properties': {
                                    'text': {
                                        'oneOf': [
                                            {'type': 'boolean'},
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'maxCharacters': {
                                                        'type': 'integer',
                                                        'minimum': 1,
                                                        'maximum': 10000,
                                                        'description': 'Maximum character limit for the text.',
                                                    },
                                                    'includeHtmlTags': {
                                                        'type': 'boolean',
                                                        'default': False,
                                                        'description': 'Include lightweight HTML tags in returned text.',
                                                    },
                                                },
                                            },
                                        ],
                                        'description': 'Text extraction options. Pass true for defaults or an object for advanced options.',
                                    },
                                    'highlights': {
                                        'oneOf': [
                                            {'type': 'boolean'},
                                            {
                                                'type': 'object',
                                                'properties': {
                                                    'query': {'type': 'string', 'description': 'Custom query to guide highlight selection.'},
                                                    'maxCharacters': {
                                                        'type': 'integer',
                                                        'minimum': 1,
                                                        'maximum': 10000,
                                                        'description': 'Maximum characters for highlights.',
                                                    },
                                                },
                                            },
                                        ],
                                        'description': 'Highlight extraction options. Pass true for defaults or an object for advanced options.',
                                    },
                                    'summary': {
                                        'type': 'object',
                                        'properties': {
                                            'query': {'type': 'string', 'description': 'Custom query for the LLM-generated summary.'},
                                        },
                                        'description': 'Summary generation options.',
                                    },
                                },
                            },
                        },
                        'required': ['url'],
                    },
                    response_schema={
                        'type': 'object',
                        'properties': {
                            'requestId': {'type': 'string', 'description': 'Unique identifier for the request.'},
                            'results': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'title': {'type': 'string', 'description': 'The title of the search result.'},
                                        'url': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'The URL of the search result.',
                                        },
                                        'id': {'type': 'string', 'description': 'Temporary document ID. Useful for the /contents endpoint.'},
                                        'publishedDate': {
                                            'type': 'string',
                                            'format': 'date-time',
                                            'description': 'Estimated creation date of the content, in ISO 8601 format.',
                                        },
                                        'author': {
                                            'type': ['string', 'null'],
                                            'description': 'The author of the content, if available.',
                                        },
                                        'image': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': 'URL of an image associated with the result, if available.',
                                        },
                                        'favicon': {
                                            'type': 'string',
                                            'format': 'uri',
                                            'description': "URL of the favicon for the result's domain.",
                                        },
                                        'text': {'type': 'string', 'description': 'Full content text of the result. Only present when contents.text is requested.'},
                                        'highlights': {
                                            'type': 'array',
                                            'items': {'type': 'string'},
                                            'description': 'Highlighted text snippets from the result. Only present when contents.highlights is requested.',
                                        },
                                        'highlightScores': {
                                            'type': 'array',
                                            'items': {'type': 'number'},
                                            'description': 'Cosine similarity scores for each highlighted snippet.',
                                        },
                                        'summary': {'type': 'string', 'description': 'LLM-generated summary of the page. Only present when contents.summary is requested.'},
                                        'score': {'type': 'number', 'description': 'Relevance score for the result.'},
                                    },
                                    'x-airbyte-entity-name': 'search_results',
                                    'x-airbyte-ai-hints': {
                                        'summary': "Web search results from Exa's embeddings-based search engine",
                                        'when_to_use': 'When the user wants to search the web for information, articles, research papers, or news',
                                        'trigger_phrases': [
                                            'search the web for',
                                            'find articles about',
                                            'look up',
                                            'search for',
                                        ],
                                        'freshness': 'live',
                                        'example_questions': ['Search for recent articles about large language models', 'Find research papers about transformer architectures', 'Search for AI startup company pages'],
                                        'search_strategy': "Use natural language queries describing what you're looking for",
                                    },
                                },
                                'description': 'List of similar page results.',
                            },
                            'searchTime': {'type': 'number', 'description': 'Time taken in milliseconds.'},
                            'costDollars': {
                                'type': 'object',
                                'description': 'Estimated cost breakdown for the request.',
                                'properties': {
                                    'total': {'type': 'number', 'description': 'Estimated total dollar cost for the request.'},
                                    'search': {
                                        'type': 'object',
                                        'properties': {
                                            'neural': {'type': 'number', 'description': 'Cost for neural search.'},
                                        },
                                    },
                                    'contents': {
                                        'type': 'object',
                                        'description': 'Cost breakdown for contents retrieval.',
                                        'properties': {
                                            'text': {'type': 'number', 'description': 'Cost for text extraction.'},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    record_extractor='$.results',
                    no_pagination='FindSimilar endpoint returns all results in a single response controlled by numResults parameter',
                ),
            },
            entity_schema={
                'type': 'object',
                'properties': {
                    'title': {'type': 'string', 'description': 'The title of the similar page.'},
                    'url': {
                        'type': 'string',
                        'format': 'uri',
                        'description': 'The URL of the similar page.',
                    },
                    'id': {'type': 'string', 'description': 'Temporary document ID.'},
                    'publishedDate': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'Estimated creation date of the content, in ISO 8601 format.',
                    },
                    'author': {
                        'type': ['string', 'null'],
                        'description': 'The author of the content, if available.',
                    },
                    'image': {
                        'type': 'string',
                        'format': 'uri',
                        'description': 'URL of an image associated with the page, if available.',
                    },
                    'favicon': {
                        'type': 'string',
                        'format': 'uri',
                        'description': "URL of the favicon for the page's domain.",
                    },
                    'text': {'type': 'string', 'description': 'Full content text of the page.'},
                    'highlights': {
                        'type': 'array',
                        'items': {'type': 'string'},
                        'description': 'Highlighted text snippets from the page.',
                    },
                    'highlightScores': {
                        'type': 'array',
                        'items': {'type': 'number'},
                        'description': 'Cosine similarity scores for each highlighted snippet.',
                    },
                    'summary': {'type': 'string', 'description': 'LLM-generated summary of the page.'},
                    'score': {'type': 'number', 'description': 'Similarity score for the result.'},
                },
                'x-airbyte-entity-name': 'similar_results',
                'x-airbyte-ai-hints': {
                    'summary': 'Web pages semantically similar to a given URL',
                    'when_to_use': 'When the user wants to find pages similar to a specific URL',
                    'trigger_phrases': [
                        'find similar pages',
                        'pages like this',
                        'related to this URL',
                        'similar websites',
                    ],
                    'freshness': 'live',
                    'example_questions': ['Find pages similar to airbyte.com', 'What websites are related to this blog post?'],
                    'search_strategy': 'Provide a URL to find semantically similar pages',
                },
            },
            ai_hints={
                'summary': 'Web pages semantically similar to a given URL',
                'when_to_use': 'When the user wants to find pages similar to a specific URL',
                'trigger_phrases': [
                    'find similar pages',
                    'pages like this',
                    'related to this URL',
                    'similar websites',
                ],
                'freshness': 'live',
                'example_questions': ['Find pages similar to airbyte.com', 'What websites are related to this blog post?'],
                'search_strategy': 'Provide a URL to find semantically similar pages',
            },
        ),
    ],
    example_questions=ExampleQuestions(
        direct=[
            'Search for latest news on Airbyte',
            'Find web pages similar to https://airbyte.com',
            'Get the full text content of https://airbyte.com',
            'Search for AI research papers published this year',
            'Find company pages related to data integration startups',
        ],
    ),
)