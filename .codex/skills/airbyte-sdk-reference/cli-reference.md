# Airbyte Agent SDK — CLI Reference

Command-line tools shipped with `airbyte-agent-sdk`. Run any subcommand with `--help` for the full option list.

## Subcommands

### cassette

Record HTTP interactions against a live API and generate YAML cassette test specifications.

Use `cassette record` after writing or modifying a connector spec to capture real request/response pairs. The resulting YAML files serve as the golden fixtures for `test run` and for schema inference via the MCP `infer_schema_from_cassette` tool.

```bash
uv run airbyte-agent-sdk cassette record integrations/stripe/ \
  --entity customers --action list \
  --params '{"limit": 5}' \
  --auth-config '{"api_key": "${STRIPE_API_KEY}"}' \
  --output integrations/stripe/tests/cassettes
```

### generate-docs

Generate `REFERENCE.md`, `AUTH.md`, and `README.md` from a connector's OpenAPI spec.

Use this after finalizing a connector's `connector.yaml` to produce the standard documentation set that accompanies every published connector.

```bash
uv run airbyte-agent-sdk generate-docs integrations/stripe/connector.yaml \
  --output integrations/stripe/docs
```

### generate-sdk

Generate a typed Python connector module from a connector's OpenAPI spec.

Use this to (re-)generate the typed SDK wrapper whenever you add a new connector or change an existing connector's spec. The output module provides typed methods, entity schemas, and `tool_utils` integration for AI frameworks.

```bash
uv run airbyte-agent-sdk generate-sdk integrations/stripe/connector.yaml \
  --output airbyte_agent_sdk/connectors
```

### test

Run connector tests or validate test specification files.

Use `test run` to execute cassette-based tests against a connector and verify that responses match the declared schemas. Use `test validate-spec` to check that a YAML test specification file is structurally valid before recording or running.

```bash
# Run all cassette tests for a connector
uv run airbyte-agent-sdk test run integrations/stripe/ \
  --test-dir integrations/stripe/tests/cassettes --verbose

# Validate a single test spec file
uv run airbyte-agent-sdk test validate-spec integrations/stripe/tests/cassettes/customers_list.yaml
```

### validate

Validate connector configurations and readiness for shipping.

Use `validate readiness` as the final gate before considering a connector complete. It checks that `connector.yaml` is valid, every entity/action has a corresponding cassette, and response schemas match recorded responses.

```bash
uv run airbyte-agent-sdk validate readiness integrations/stripe/ --json-output
```
