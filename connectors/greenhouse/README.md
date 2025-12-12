# Airbyte Greenhouse AI Connector

Connector for Greenhouse Harvest API

## Installation

```bash
uv pip install airbyte-ai-greenhouse
```

## Usage

```python
from airbyte_ai_greenhouse import GreenhouseConnector, GreenhouseAuthConfig

connector = GreenhouseConnector(auth_config=GreenhouseAuthConfig(api_key="..."))
result = connector.candidates.list()
```

## Documentation

| Entity | Actions |
|--------|---------|
| Candidates | [List](./REFERENCE.md#candidates-list), [Get](./REFERENCE.md#candidates-get) |
| Applications | [List](./REFERENCE.md#applications-list), [Get](./REFERENCE.md#applications-get) |
| Jobs | [List](./REFERENCE.md#jobs-list), [Get](./REFERENCE.md#jobs-get) |
| Offers | [List](./REFERENCE.md#offers-list), [Get](./REFERENCE.md#offers-get) |
| Users | [List](./REFERENCE.md#users-list), [Get](./REFERENCE.md#users-get) |
| Departments | [List](./REFERENCE.md#departments-list), [Get](./REFERENCE.md#departments-get) |
| Offices | [List](./REFERENCE.md#offices-list), [Get](./REFERENCE.md#offices-get) |
| Job Posts | [List](./REFERENCE.md#job-posts-list), [Get](./REFERENCE.md#job-posts-get) |
| Sources | [List](./REFERENCE.md#sources-list) |
| Scheduled Interviews | [List](./REFERENCE.md#scheduled-interviews-list), [Get](./REFERENCE.md#scheduled-interviews-get) |
| Application Attachment | [Download](./REFERENCE.md#application-attachment-download) |
| Candidate Attachment | [Download](./REFERENCE.md#candidate-attachment-download) |


For detailed documentation on available actions and parameters, see [REFERENCE.md](./REFERENCE.md).

For the service's official API docs, see [Greenhouse API Reference](https://developers.greenhouse.io/harvest.html).

## Version Information

**Package Version:** 0.17.7

**Connector Version:** 0.1.0

**Generated with connector-sdk:** 9f7f8a98389c3775a4d22db1aa81fbb03020a65b