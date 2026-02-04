# Troubleshooting

This guide covers common errors and solutions when working with Airbyte Agent Connectors.

## HTTP Errors

### 401 Unauthorized

**Symptoms:**
- `HTTP 401` error
- "Unauthorized" or "Invalid credentials" message
- `AuthenticationError` exception

**Causes:**
- Invalid API key or token
- Expired OAuth access token
- Wrong credentials for the environment (test vs. production)

**Solutions:**

1. **Verify credentials are correct:**
   ```python
   import os
   print(f"Token starts with: {os.environ.get('GITHUB_TOKEN', 'NOT SET')[:10]}...")
   ```

2. **Check for expired OAuth tokens:**
   - OAuth access tokens typically expire after 1-2 hours
   - Ensure refresh token is configured for automatic renewal
   ```python
   # Salesforce with refresh token
   connector = SalesforceConnector(
       auth_config=SalesforceOAuthConfig(
           client_id=os.environ["SF_CLIENT_ID"],
           client_secret=os.environ["SF_CLIENT_SECRET"],
           refresh_token=os.environ["SF_REFRESH_TOKEN"]  # Required for auto-refresh
       )
   )
   ```

3. **Regenerate credentials:**
   - GitHub: [Settings > Developer settings > Tokens](https://github.com/settings/tokens)
   - Stripe: [Dashboard > Developers > API keys](https://dashboard.stripe.com/apikeys)
   - Check connector's AUTH.md for credential setup

### 403 Forbidden

**Symptoms:**
- `HTTP 403` error
- "Forbidden" or "Insufficient permissions" message
- Operation fails despite valid credentials

**Causes:**
- Token lacks required scopes/permissions
- IP restrictions or firewall rules
- Resource-level access denied

**Solutions:**

1. **Check token scopes:**
   - GitHub PAT: Ensure `repo`, `read:org` scopes for repository access
   - Slack Bot: Verify required OAuth scopes in app settings
   - Stripe: API keys have full access; check for restricted keys

2. **Verify resource access:**
   ```python
   # Test basic access first
   result = await connector.execute("viewer", "get", {})  # GitHub
   result = await connector.execute("balance", "get", {})  # Stripe
   ```

3. **Check organization/workspace permissions:**
   - Some resources require admin access
   - Organization owners may need to approve OAuth apps

### 429 Too Many Requests

**Symptoms:**
- `HTTP 429` error
- "Rate limit exceeded" message
- `RateLimitError` exception

**Causes:**
- Exceeded API rate limits
- Too many concurrent requests
- Burst of requests in short time

**Solutions:**

1. **Wait and retry:**
   - Connectors have built-in retry with exponential backoff
   - Default configuration handles most rate limiting automatically

2. **Check rate limit headers:**
   ```python
   # Many APIs return rate limit info in response headers
   # Check connector logs for rate limit details
   ```

3. **Reduce request frequency:**
   ```python
   # Add delays between requests
   import asyncio

   for item in items:
       result = await connector.execute("entity", "get", {"id": item})
       await asyncio.sleep(0.5)  # 500ms delay
   ```

4. **Use bulk operations:**
   ```python
   # Instead of multiple get requests
   # Use list with filters when possible
   result = await connector.execute("customers", "list", {
       "limit": 100,
       "email": "pattern@example.com"
   })
   ```

### 5xx Server Errors

**Symptoms:**
- `HTTP 500`, `502`, `503`, or `504` errors
- "Internal Server Error" or "Service Unavailable"
- Intermittent failures

**Causes:**
- Third-party API outage
- Temporary server issues
- Timeout on long operations

**Solutions:**

1. **Check service status:**
   - [GitHub Status](https://www.githubstatus.com/)
   - [Stripe Status](https://status.stripe.com/)
   - [Salesforce Status](https://status.salesforce.com/)

2. **Built-in retry handles transient errors:**
   - Default retry config: 5 attempts with exponential backoff
   - Retries on: 408, 429, 500, 502, 503, 504

3. **Wait and retry manually if needed:**
   ```python
   import asyncio

   async def execute_with_retry(connector, entity, action, params, max_retries=3):
       for attempt in range(max_retries):
           result = await connector.execute(entity, action, params)
           if result.success:
               return result
           if "5" in str(result.error)[:3]:  # 5xx error
               await asyncio.sleep(2 ** attempt)  # Exponential backoff
           else:
               break
       return result
   ```

## Retry Configuration

Connectors use automatic retry for transient failures. Default settings:

```python
# Default retry configuration
max_attempts: 5
retry_on_status_codes: [408, 429, 500, 502, 503, 504]
initial_backoff_seconds: 1.0
max_backoff_seconds: 60.0
backoff_multiplier: 2.0
jitter_ratio: 0.1
```

**Retry timeline example:**
- Attempt 1: Immediate
- Attempt 2: ~1 second delay
- Attempt 3: ~2 seconds delay
- Attempt 4: ~4 seconds delay
- Attempt 5: ~8 seconds delay

## OAuth Token Refresh Issues

### Refresh Token Expired

**Symptoms:**
- Token refresh fails
- "Invalid grant" or "Refresh token expired" error

**Solutions:**

1. **Re-authorize the application:**
   - OAuth refresh tokens can expire after extended periods of inactivity
   - Complete the OAuth flow again to get new tokens

2. **Check token lifetime settings:**
   - Salesforce: Refresh tokens expire based on Connected App settings
   - Google: Refresh tokens may expire if unused for 6 months

### Missing Refresh Token

**Symptoms:**
- Initial requests work
- Requests fail after access token expires (~1 hour)

**Solutions:**

1. **Include offline access scope:**
   - Salesforce: Add `offline_access` to scopes
   - Google: Add `access_type=offline` to authorization URL

2. **Store refresh token from initial OAuth:**
   ```python
   # Ensure refresh_token is captured during OAuth callback
   # Store it securely for use in connector configuration
   ```

## Common Setup Mistakes

### Environment Variables Not Loaded

**Symptoms:**
- `KeyError` when accessing `os.environ`
- Empty or `None` credential values

**Solutions:**

1. **Load .env file explicitly:**
   ```python
   from dotenv import load_dotenv

   load_dotenv()  # Must be called before accessing env vars

   # Or specify path
   load_dotenv("/path/to/.env")
   ```

2. **Check .env file location:**
   ```python
   import os
   print(f"Current directory: {os.getcwd()}")
   print(f".env exists: {os.path.exists('.env')}")
   ```

3. **Verify variable names match:**
   ```bash
   # .env
   GITHUB_TOKEN=ghp_xxx  # Note: no quotes needed

   # Python
   os.environ["GITHUB_TOKEN"]  # Must match exactly
   ```

### Wrong Connector Import

**Symptoms:**
- `ModuleNotFoundError` or `ImportError`
- Attribute errors on connector

**Solutions:**

1. **Check package is installed:**
   ```bash
   pip list | grep airbyte-agent
   # or
   uv pip list | grep airbyte-agent
   ```

2. **Use correct import pattern:**
   ```python
   # Correct
   from airbyte_agent_github import GithubConnector
   from airbyte_agent_github.models import GithubPersonalAccessTokenAuthConfig

   # Wrong (common mistakes)
   from airbyte_agent.github import GithubConnector  # Wrong path
   from github_connector import GithubConnector  # Wrong module
   ```

### Async/Await Missing

**Symptoms:**
- `RuntimeWarning: coroutine was never awaited`
- Returns coroutine object instead of result

**Solutions:**

1. **Always await connector operations:**
   ```python
   # Wrong
   result = connector.execute("customers", "list", {})

   # Correct
   result = await connector.execute("customers", "list", {})
   ```

2. **Run in async context:**
   ```python
   import asyncio

   async def main():
       result = await connector.execute("customers", "list", {})
       print(result.data)

   asyncio.run(main())
   ```

### Entity/Action Name Errors

**Symptoms:**
- `EntityNotFoundError`
- `ActionNotSupportedError`

**Solutions:**

1. **Check exact names in REFERENCE.md:**
   ```python
   # Entity names are typically lowercase with underscores
   "customers"      # Correct
   "Customers"      # Wrong (case sensitive)
   "customer"       # Wrong (singular vs plural)
   "pull_requests"  # Correct
   "pullRequests"   # Wrong (camelCase)
   ```

2. **List available entities:**
   ```python
   entities = connector.list_entities()
   print(entities)
   ```

## MCP Server Issues

### Server Not Starting

**Symptoms:**
- Claude shows "MCP server not available"
- Connection refused errors

**Solutions:**

1. **Check uv/Python installation:**
   ```bash
   uv --version
   python --version
   which uv
   ```

2. **Test server manually:**
   ```bash
   cd /path/to/airbyte-agent-mcp
   uv run airbyte_agent_mcp
   ```

3. **Verify configuration file paths:**
   ```bash
   ls -la /path/to/airbyte-agent-mcp/configured_connectors.yaml
   ls -la /path/to/airbyte-agent-mcp/.env
   ```

### Connector Not Found in MCP

**Symptoms:**
- "Connector not found" errors
- Connector missing from discovery

**Solutions:**

1. **Check configured_connectors.yaml:**
   ```yaml
   connectors:
     - id: stripe  # This ID is used in execute calls
       type: local
       connector_name: stripe
       secrets:
         api_key: STRIPE_API_KEY
   ```

2. **Verify environment variables are set:**
   ```bash
   # Check .env has the required variables
   cat /path/to/airbyte-agent-mcp/.env | grep STRIPE
   ```

3. **Restart MCP server after config changes**

## Debugging Tips

### Enable Verbose Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)

# Or for specific connector
logging.getLogger("airbyte_agent_github").setLevel(logging.DEBUG)
```

### Inspect Result Objects

```python
result = await connector.execute("customers", "list", {"limit": 1})

print(f"Success: {result.success}")
print(f"Error: {result.error}")
print(f"Data type: {type(result.data)}")
print(f"Data: {result.data}")
print(f"Meta: {result.meta}")
```

### Test Credentials Independently

```python
# Test authentication before complex operations
async def test_auth(connector):
    """Test basic connectivity."""
    try:
        # Use a simple, low-impact operation
        result = await connector.execute("viewer", "get", {})  # GitHub
        # or
        result = await connector.execute("balance", "get", {})  # Stripe

        if result.success:
            print("Authentication successful!")
            return True
        else:
            print(f"Auth failed: {result.error}")
            return False
    except Exception as e:
        print(f"Auth error: {e}")
        return False
```

## SDK Known Issues

### `create_hosted()` Returns 404

**Symptom:** Calling `create_hosted()` fails with HTTP 404.

**Cause:** SDK bug - uses `/v1/integrations/connectors` instead of `/api/v1/integrations/connectors`.

**Workaround:** Use HTTP API directly:
```bash
curl -X POST 'https://api.airbyte.ai/api/v1/integrations/connectors' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "workspace_name": "<WORKSPACE_NAME>",
    "connector_definition_id": "<DEFINITION_ID>",
    "name": "my-connector",
    "credentials": {...}
  }'
```

**Status:** Bug reported upstream. Check SDK version for fix.

---

### "Workspace not found" with external_user_id

**Symptom:** Error "Workspace not found" when using `external_user_id`.

**Cause:** `external_user_id` must match an existing workspace NAME (not a custom identifier you create).

**Fix:**
1. List workspaces: `GET /api/v1/workspaces`
2. Use the `name` field from an existing workspace
3. Or create a new workspace first

---

### API Rejects Credentials with auth_type

**Symptom:** 400 error when creating connector with `auth_type` in credentials.

**Cause:** The API infers auth type from credentials structure. Including `auth_type` causes validation failure.

**Fix:** Remove `auth_type` from credentials:
```json
// WRONG
{"auth_type": "APIKey", "access_key": "...", "access_key_secret": "..."}

// CORRECT
{"access_key": "...", "access_key_secret": "..."}
```

---

## Getting Help

If you're still experiencing issues:

1. **Check connector-specific docs:**
   - `connectors/{connector}/README.md`
   - `connectors/{connector}/AUTH.md`

2. **Search existing issues:**
   - [GitHub Issues](https://github.com/airbytehq/airbyte-agent-connectors/issues)

3. **Join the community:**
   - [Airbyte Slack](https://slack.airbyte.com/)

4. **Report a bug:**
   - Include: connector name, operation attempted, error message, Python version
   - [Create an issue](https://github.com/airbytehq/airbyte-agent-connectors/issues/new)
