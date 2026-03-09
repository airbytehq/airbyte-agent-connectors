<!-- AUTO-GENERATED from connectors/twilio/ -- do not edit manually -->
<!-- Source format: v1 | Generated: 2026-03-09 -->

# Twilio

The Twilio agent connector is a Python package that equips AI agents to interact with Twilio through strongly typed, well-documented tools. It's ready to use directly in your Python app, in an agent framework, or exposed through an MCP.

**Key metadata:**

- **Package:** `airbyte-agent-twilio` v0.1.1
- **Auth:** Token
- **Docs:** [Official API docs](https://www.twilio.com/docs/usage/api)
- **Status:** complete

## Example Prompts

- List all calls from the last 7 days
- Show me recent inbound SMS messages
- List all active phone numbers on my account
- Show me details for a specific call
- List all recordings
- Show me conference calls
- List usage records for my account
- Show me all queues
- List outgoing caller IDs
- Show me addresses on my account
- List transcriptions
- What are my top 10 most expensive calls this month?
- How many SMS messages did I send vs receive in the last 30 days?
- Summarize my usage costs by category
- Which phone numbers have the most incoming calls?
- Show me all failed messages and their error codes
- What is the average call duration for outbound calls?

## Unsupported

- Send a new SMS message
- Make a phone call
- Purchase a new phone number
- Delete a recording
- Create a new queue

## Quick Start

### Installation

```bash
uv pip install airbyte-agent-twilio
```

### OSS Mode

```python
from airbyte_agent_twilio import TwilioConnector
from airbyte_agent_twilio.models import TwilioAuthConfig

connector = TwilioConnector(
    auth_config=TwilioAuthConfig(
        account_sid="<Your Twilio Account SID (starts with AC)>",
        auth_token="<Your Twilio Auth Token>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@TwilioConnector.tool_utils
async def twilio_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

### Hosted Mode

```python
from airbyte_agent_twilio import TwilioConnector, AirbyteAuthConfig

connector = TwilioConnector(
    auth_config=AirbyteAuthConfig(
        customer_name="<your_customer_name>",
        organization_id="<your_organization_id>",  # Optional for multi-org clients
        airbyte_client_id="<your-client-id>",
        airbyte_client_secret="<your-client-secret>"
    )
)

@agent.tool_plain # assumes you're using Pydantic AI
@TwilioConnector.tool_utils
async def twilio_execute(entity: str, action: str, params: dict | None = None):
    return await connector.execute(entity, action, params or {})
```

## Entities and Actions

| Entity | Actions |
|--------|---------|
| Accounts | List, Get, Search |
| Calls | List, Get, Search |
| Messages | List, Get, Search |
| Incoming Phone Numbers | List, Get, Search |
| Recordings | List, Get, Search |
| Conferences | List, Get, Search |
| Usage Records | List, Search |
| Addresses | List, Get, Search |
| Queues | List, Get, Search |
| Transcriptions | List, Get, Search |
| Outgoing Caller Ids | List, Get, Search |

## Authentication

For all authentication options, see the connector's [authentication documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/twilio/AUTH.md).

## API Reference

For the full API reference with parameters and examples, see the connector's [reference documentation](https://github.com/airbytehq/airbyte-agent-connectors/blob/main/connectors/twilio/REFERENCE.md).

---

*[Full docs on GitHub](https://github.com/airbytehq/airbyte-agent-connectors/tree/main/connectors/twilio)*
