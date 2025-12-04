# Airbyte Zendesk-Support AI Connector

Type-safe Zendesk-Support API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.9.0

**Connector Version:** 1.0.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-zendesk-support
```

## Usage

```python
from airbyte_ai_zendesk_support import ZendeskSupportConnector

# Create connector
connector = ZendeskSupportConnector(auth_config={"api_key": "your_api_key"})

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Articles Operations
- `list_articles()` - List all articles
- `get_article()` - Get an article by ID

### Article_Attachments Operations
- `list_article_attachments()` - List attachments for an article
- `get_article_attachment_metadata()` - Retrieve attachment metadata
- `download_article_attachment()` - Download attachment file

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_zendesk_support.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
