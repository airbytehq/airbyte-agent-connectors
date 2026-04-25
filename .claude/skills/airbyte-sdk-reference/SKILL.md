---
name: airbyte-sdk-reference
description: Reference documentation for the Airbyte per-connector typed SDK packages
---

# Airbyte SDK Reference

Reference documentation for the Airbyte per-connector typed SDK packages. Use for SDK API details, PydanticAI patterns, and Claude SDK patterns.

## Contents

- [SDK API](./sdk-api.md) — public API surface: `configure()`, `connect()`, `Workspace`, `tool_utils`, `list_entities()`, `entity_schema()`.
- [Connector discovery](./connector-discovery.md) — enumerating available connectors and locating per-connector documentation.
- [PydanticAI patterns](./pydantic-ai.md) — wiring typed connectors into PydanticAI agents.
- [Claude SDK patterns](./claude-sdk.md) — wiring typed connectors into the Anthropic Python SDK.
- [CLI reference](./cli-reference.md) — `cassette`, `generate-docs`, `generate-sdk`, `test`, and `validate` subcommands.
