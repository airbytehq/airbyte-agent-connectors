# Airbyte Zendesk-Support AI Connector

Type-safe Zendesk-Support API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.11.0

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
- `list_articles()` - Returns a list of all articles in the Help Center
- `get_article()` - Retrieves the details of a specific article

### Article_Attachments Operations
- `list_article_attachments()` - Returns a list of all attachments for a specific article
- `get_article_attachment_metadata()` - Retrieves the metadata of a specific attachment for a specific article
- `download_article_attachment()` - Downloads the file content of a specific attachment

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_zendesk_support.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
