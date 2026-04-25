"""connect() — one-call factory for a ready-to-use connector."""

from __future__ import annotations

import asyncio
import concurrent.futures
from typing import overload

from airbyte_agent_sdk.cloud_utils import AirbyteCloudClient
from airbyte_agent_sdk.config import resolve_credentials
from airbyte_agent_sdk.connector_model_loader import load_connector_model
from airbyte_agent_sdk.executor.hosted_executor import HostedExecutor
from airbyte_agent_sdk.types import AirbyteAuthConfig

from . import registry


def _resolve_connector_id_sync(
    client_id: str,
    client_secret: str,
    organization_id: str | None,
    workspace_name: str,
    connector_definition_id: str,
) -> str:
    """Synchronously resolve a connector ID via the cloud API.

    Uses the same loop-detection pattern as `ask_sync`: `asyncio.run()`
    when no loop is running, otherwise dispatches to a worker thread.
    """

    async def _probe() -> str:
        client = AirbyteCloudClient(
            client_id=client_id,
            client_secret=client_secret,
            organization_id=organization_id,
        )
        try:
            return await client.get_connector_id(
                workspace_name=workspace_name,
                connector_definition_id=connector_definition_id,
            )
        finally:
            await client.close()

    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(_probe())
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        return pool.submit(asyncio.run, _probe()).result()


@overload
def connect(
    connector_name: str,
    *,
    client_id: str | None = ...,
    client_secret: str | None = ...,
    workspace_name: str | None = ...,
    connector_id: str | None = ...,
    organization_id: str | None = ...,
    auth_config: AirbyteAuthConfig | None = ...,
) -> HostedExecutor: ...


def connect(
    connector_name: str,
    *,
    client_id: str | None = None,
    client_secret: str | None = None,
    workspace_name: str | None = None,
    connector_id: str | None = None,
    organization_id: str | None = None,
    auth_config: AirbyteAuthConfig | None = None,
) -> HostedExecutor:
    """Create a typed connector or `HostedExecutor` for a connector by name.

    When a generated typed connector package exists (e.g. `StripeConnector`),
    returns the typed connector with full IDE autocompletion and type safety.
    Otherwise, falls back to a generic [`HostedExecutor`](#HostedExecutor).

    Connector-ID resolution is performed eagerly: if `connector_id` is not
    supplied and credentials are available, `connect()` resolves the
    workspace + definition pair to a concrete connector ID up front so that
    `ConnectorNotFoundError` and `ConnectorAmbiguityError` surface at the
    call site rather than being deferred to the first `execute()` call.

    Example:
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
                print(result.data)

        asyncio.run(main())
        ```

    The returned object's `execute()` is `async` — always `await` it from inside a
    coroutine (see `asyncio.run(main())` above). The returned connector is also an
    async context manager, so `async with connect(...) as connector:` releases the
    underlying HTTP client automatically. If you prefer manual lifecycle management,
    assign the connector and `await connector.close()` when done.

    Args:
        connector_name: Connector slug, e.g. `"stripe"` or `"zendesk-support"`.
        client_id: Airbyte OAuth client ID (falls back to `AIRBYTE_CLIENT_ID`).
        client_secret: Airbyte OAuth client secret (falls back to `AIRBYTE_CLIENT_SECRET`).
        workspace_name: Workspace name for connector lookup. Defaults to `"default"`.
        connector_id: Direct connector/source ID — skips lookup.
        organization_id: Airbyte organization ID for multi-org routing.
        auth_config: [`AirbyteAuthConfig`](#AirbyteAuthConfig) with hosted credentials.

    Returns:
        A typed connector (e.g. `StripeConnector`) if a generated package exists,
        or a [`HostedExecutor`](#HostedExecutor) for connectors with only a YAML spec.
        Static type checkers see the narrowed return type via the generated
        `connect.pyi` stub (one `Literal["<slug>"]` overload per connector); the
        `-> HostedExecutor` annotation on this runtime `def` is the fallback used
        in dev checkouts where `connect.pyi` has not been generated yet.

    Raises:
        UnknownConnectorError: If `connector_name` is not in the bundled registry.
        ConnectorNotFoundError: If the workspace has no connector matching
            the requested definition.
        ConnectorAmbiguityError: If the workspace has more than one connector
            matching the requested definition.
        ValueError: If no Airbyte Cloud credentials are provided (neither
            arguments, env vars, nor `auth_config`).
        httpx.HTTPStatusError: If the eager connector-ID probe receives an
            HTTP error (e.g. 401 Unauthorized).
        httpx.RequestError: If the probe encounters a transport-level error
            (DNS failure, timeout, etc.).
        AuthenticationError: If the token exchange during the eager probe
            fails (e.g. invalid client credentials).

    Note:
        Because `connect()` now performs an eager network call to resolve the
        connector ID, callers should be prepared for the HTTP error families
        listed above in addition to the typed SDK exceptions.

        The returned object's `execute()` method may raise exceptions from three
        disjoint families depending on the execution path:

        1. `AirbyteError` (root of `HTTPClientError` and
           `ExecutorError` families) — raised by SDK-owned paths such as the
           local executor, HTTP client, and auth strategies.
        2. `httpx.HTTPStatusError` / `httpx.RequestError` — propagated **unwrapped**
           from `HostedExecutor.execute()`; not covered by `AirbyteError`.
        3. `RuntimeError` — raised by generated typed connectors when the
           underlying `ExecutionResult.success` is `False`; not covered by
           `AirbyteError`.

        See the module-level `## Errors` section for a compound `try`/`except`
        pattern that catches both SDK-defined and hosted-path errors.
    """
    spec_path = registry.get_spec_path(connector_name)

    is_hosted_auth_config = isinstance(auth_config, AirbyteAuthConfig)

    try:
        resolved_client_id, resolved_client_secret, resolved_org_id, resolved_ws = resolve_credentials(
            client_id=client_id,
            client_secret=client_secret,
            organization_id=organization_id,
            workspace_name=workspace_name,
        )
    except ValueError:
        if not is_hosted_auth_config:
            raise ValueError(
                "connect() requires Airbyte Cloud credentials. "
                "Pass client_id/client_secret, set AIRBYTE_CLIENT_ID/AIRBYTE_CLIENT_SECRET "
                "env vars, or provide AirbyteAuthConfig. "
                "For direct API access, use LocalExecutor directly."
            )
        resolved_client_id = None
        resolved_client_secret = None
        resolved_org_id = organization_id
        resolved_ws = workspace_name or "default"

    if is_hosted_auth_config:
        effective_client_id = auth_config.airbyte_client_id or resolved_client_id
        effective_client_secret = auth_config.airbyte_client_secret or resolved_client_secret
        effective_connector_id = auth_config.connector_id or connector_id
        effective_ws = auth_config.workspace_name or resolved_ws
        effective_org = auth_config.organization_id or resolved_org_id
    else:
        effective_client_id = resolved_client_id
        effective_client_secret = resolved_client_secret
        effective_connector_id = connector_id
        effective_ws = resolved_ws
        effective_org = resolved_org_id

    model = load_connector_model(str(spec_path))
    definition_id = str(model.id)

    if not effective_connector_id and effective_client_id and effective_client_secret:
        effective_connector_id = _resolve_connector_id_sync(
            client_id=effective_client_id,
            client_secret=effective_client_secret,
            organization_id=effective_org,
            workspace_name=effective_ws,
            connector_definition_id=definition_id,
        )

    connector_cls = registry._get_connector_class(connector_name)
    if connector_cls is not None:
        typed_auth = AirbyteAuthConfig(
            airbyte_client_id=effective_client_id,
            airbyte_client_secret=effective_client_secret,
            connector_id=effective_connector_id,
            workspace_name=effective_ws,
            organization_id=effective_org,
        )
        return connector_cls(auth_config=typed_auth)

    if is_hosted_auth_config and (not effective_client_id or not effective_client_secret):
        raise ValueError(
            "client_id and client_secret are required for hosted mode. "
            "Pass them in AirbyteAuthConfig, as keyword arguments, "
            "or set AIRBYTE_CLIENT_ID/AIRBYTE_CLIENT_SECRET."
        )

    return HostedExecutor(
        airbyte_client_id=effective_client_id,
        airbyte_client_secret=effective_client_secret,
        connector_id=effective_connector_id,
        workspace_name=effective_ws,
        organization_id=effective_org,
        connector_definition_id=definition_id,
        model=model,
    )
