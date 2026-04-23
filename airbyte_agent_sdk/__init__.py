"""
# Airbyte Agent SDK

A type-safe Python SDK for executing Airbyte connectors from an application
or agent. Point it at an Airbyte Cloud workspace and it exposes every
connected source (Stripe, Zendesk, HubSpot, …) as a typed Python object or
a generic hosted executor — no REST boilerplate, no OAuth plumbing.

## Setup

Supply your Airbyte Cloud credentials in one of three ways:

1. **Env vars** (recommended for apps): set `AIRBYTE_CLIENT_ID` and
   `AIRBYTE_CLIENT_SECRET`. Every entry point below picks them up
   automatically when their `client_id`/`client_secret` kwargs are
   omitted.
2. **Explicit kwargs**: pass `client_id=` and `client_secret=` directly
   to [`connect()`](#connect), [`Workspace`](#Workspace),
   [`ask()`](#ask), or [`ask_sync()`](#ask_sync).
3. **Programmatic**: call [`configure()`](#configure) once at startup to
   set process-wide defaults (useful in notebooks).

## Quickstart

```python
import asyncio
from airbyte_agent_sdk import connect

async def main():
    async with connect(
        "stripe",
        client_id="your_client_id",
        client_secret="your_client_secret",
        connector_id="src_123",
    ) as stripe:
        result = await stripe.execute("customers", "list", params={"limit": 10})
        for row in result.data:
            print(row)

asyncio.run(main())
```

The returned connector is also an async context manager — `async with`
releases the underlying HTTP client automatically. If you need to manage
the lifetime manually, assign the connector and call `await
connector.close()` in a `finally` block.

Use [`ask_sync`](#ask_sync) and direct [`connect()`](#connect) for scripts
and notebooks; use [`ask`](#ask) and [`Workspace`](#Workspace) for async
applications.

## Entry points

- [`connect`](#connect) — one-call factory that returns a typed connector
  or a [`HostedExecutor`](#HostedExecutor).
- [`list_connectors`](#list_connectors) — enumerate connectors bundled
  with this SDK.
- [`ask`](#ask) / [`ask_sync`](#ask_sync) — natural-language query across
  an entire workspace.

## Workspace operations

- [`Workspace`](#Workspace) — async context manager for workspace-level
  operations (list/create/delete connectors, workflows, and automations).
- [`HostedExecutor`](#HostedExecutor) — fallback executor returned by
  [`connect()`](#connect) when no typed connector package exists.

## Results & info

- [`AskResult`](#AskResult), [`ConnectorInfo`](#ConnectorInfo),
  [`WorkflowInfo`](#WorkflowInfo), [`AutomationInfo`](#AutomationInfo),
  [`ExecutionConfig`](#ExecutionConfig),
  [`ExecutionResult`](#ExecutionResult),
  [`AirbyteAuthConfig`](#AirbyteAuthConfig).

## Errors

[`AirbyteError`](#AirbyteError) is the **root of the SDK-defined exception
hierarchy**, covering [`HTTPClientError`](#HTTPClientError) (and its
subclasses [`HTTPStatusError`](#HTTPStatusError),
[`AuthenticationError`](#AuthenticationError),
[`RateLimitError`](#RateLimitError), [`NetworkError`](#NetworkError),
[`TimeoutError`](#TimeoutError)) plus [`ExecutorError`](#ExecutorError)
and its subclasses. It does **not** catch:

- `httpx.HTTPStatusError` / `httpx.RequestError` — the hosted path
  propagates these unwrapped from `HostedExecutor.execute()`.
- `RuntimeError` — generated typed connectors raise this when an
  underlying `ExecutionResult.success` is `False`.
- `ValueError` — argument-validation failures at the entry points.

Catch both SDK-defined and hosted-path errors in one `except`:

```python
import httpx
from airbyte_agent_sdk import AirbyteError, connect

async with connect("stripe", connector_id="src_123") as stripe:
    try:
        result = await stripe.execute("customers", "list")
    except (AirbyteError, httpx.HTTPError) as err:
        # AirbyteError covers SDK-owned paths; httpx.HTTPError covers the
        # hosted path which propagates httpx errors unwrapped.
        print(f"Execution failed: {err!r}")
```

## Advanced

Advanced users who need to inspect a connector's `ConnectorModel` or
traverse tool-call records should import from the submodules directly:
`airbyte_agent_sdk.types` for auth/spec types and
`airbyte_agent_sdk.executor.models` for nested result dataclasses. See
[`docs/CONTRIBUTING.md`](https://github.com/airbytehq/airbyte-embedded/blob/main/connector-sdk/docs/CONTRIBUTING.md)
for the public-API contract.

Anything not listed in `__all__` is internal and may change between
releases without notice.
"""

from __future__ import annotations

from .ask import ask, ask_sync
from .config import configure
from .connect import connect
from .constants import SDK_VERSION
from .errors import AirbyteError
from .executor import (
    ActionNotSupportedError,
    EntityNotFoundError,
    ExecutionConfig,
    ExecutionResult,
    ExecutorError,
    HostedExecutor,
    InvalidParameterError,
    MissingParameterError,
)
from .executor.models import AskResult, AutomationInfo, ConnectorInfo, WorkflowInfo
from .http.exceptions import (
    AuthenticationError,
    ConnectorValidationError,
    HTTPClientError,
    HTTPStatusError,
    NetworkError,
    RateLimitError,
    TimeoutError,
)
from .registry import list_connectors
from .types import AirbyteAuthConfig
from .utils import save_download
from .workspace import Workspace

__version__ = SDK_VERSION

__all__ = [
    # Entry points
    "connect",
    "list_connectors",
    "Workspace",
    "ask",
    "ask_sync",
    # Hosted execution
    "HostedExecutor",
    # Results / info types
    "AskResult",
    "ConnectorInfo",
    "WorkflowInfo",
    "AutomationInfo",
    "ExecutionConfig",
    "ExecutionResult",
    # Configuration types
    "AirbyteAuthConfig",
    # Executor exceptions
    "AirbyteError",
    "ExecutorError",
    "EntityNotFoundError",
    "ActionNotSupportedError",
    "MissingParameterError",
    "InvalidParameterError",
    # HTTP exceptions
    "HTTPClientError",
    "HTTPStatusError",
    "AuthenticationError",
    "ConnectorValidationError",
    "RateLimitError",
    "NetworkError",
    "TimeoutError",
    # Utilities
    "save_download",
    "configure",
]

# Submodules hidden from pdoc output. Add new internal submodules here; see docs/CONTRIBUTING.md for the public-API contract.
__pdoc__ = {
    # Deprecated back-compat shim — canonical source is airbyte_agent_sdk.http.exceptions
    "exceptions": False,
    # AirbyteError root module — the name is surfaced via __all__; no standalone page needed
    "errors": False,
    # Build-time tooling
    "codegen": False,
    "cli": False,
    # Internal runtime helpers surfaced only for SDK-internal consumers
    "introspection": False,
    "extensions": False,
    "auth_template": False,
    "secrets": False,
    "connector_model_loader": False,
    "registry": False,
    # Internal schema / spec parsing
    "schema": False,
    "validation": False,
    "testing": False,
    # Internal instrumentation
    "telemetry": False,
    "observability": False,
    # Implementation subpackages whose public facade is re-exported above
    "http": False,
    "performance": False,
    "logging": False,
    "cloud_utils": False,
}
