"""connect() — one-call factory for a ready-to-use connector."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, overload

from airbyte_agent_sdk.config import resolve_credentials
from airbyte_agent_sdk.connector_model_loader import load_connector_model
from airbyte_agent_sdk.executor.hosted_executor import HostedExecutor
from airbyte_agent_sdk.types import AirbyteAuthConfig

from . import registry

if TYPE_CHECKING:
    from airbyte_agent_sdk.connectors.stripe import StripeConnector


@overload
def connect(
    connector_name: Literal["stripe"],
    *,
    client_id: str | None = ...,
    client_secret: str | None = ...,
    workspace_name: str | None = ...,
    connector_id: str | None = ...,
    organization_id: str | None = ...,
    auth_config: AirbyteAuthConfig | None = ...,
) -> StripeConnector: ...


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
) -> StripeConnector | HostedExecutor:
    """Create a typed connector or `HostedExecutor` for a connector by name.

    When a generated typed connector package exists (e.g. `StripeConnector`),
    returns the typed connector with full IDE autocompletion and type safety.
    Otherwise, falls back to a generic [`HostedExecutor`](#HostedExecutor).

    Example:
        ```python
        import asyncio
        from airbyte_agent_sdk import connect

        async def main():
            stripe = connect(
                "stripe",
                client_id="your_client_id",
                client_secret="your_client_secret",
                connector_id="src_123",
            )
            result = await stripe.execute("customers", "list", params={"limit": 10})
            print(result.data)

        asyncio.run(main())
        ```

    The returned object's `execute()` is `async` — always `await` it from inside a
    coroutine (see `asyncio.run(main())` above).

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

    Raises:
        ValueError: If `connector_name` is not in the bundled registry, or if no
            Airbyte Cloud credentials are provided (neither arguments, env vars,
            nor `auth_config`).

    Note:
        The returned object's `execute()` method may raise exceptions from three
        disjoint families depending on the execution path:

        1. [`AirbyteError`](#AirbyteError) (root of `HTTPClientError` and
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
    registry.get_spec_path(connector_name)

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

    connector_cls = registry._get_connector_class(connector_name)
    if connector_cls is not None:
        if is_hosted_auth_config:
            typed_auth = AirbyteAuthConfig(
                airbyte_client_id=auth_config.airbyte_client_id or resolved_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret or resolved_client_secret,
                connector_id=auth_config.connector_id or connector_id,
                workspace_name=auth_config.workspace_name or resolved_ws,
                organization_id=auth_config.organization_id or resolved_org_id,
            )
        else:
            typed_auth = AirbyteAuthConfig(
                airbyte_client_id=resolved_client_id,
                airbyte_client_secret=resolved_client_secret,
                connector_id=connector_id,
                workspace_name=resolved_ws,
                organization_id=resolved_org_id,
            )
        return connector_cls(auth_config=typed_auth)

    spec_path = registry.get_spec_path(connector_name)
    model = load_connector_model(str(spec_path))
    definition_id = str(model.id)

    if is_hosted_auth_config:
        hosted_client_id = auth_config.airbyte_client_id or resolved_client_id
        hosted_client_secret = auth_config.airbyte_client_secret or resolved_client_secret
        if not hosted_client_id or not hosted_client_secret:
            raise ValueError(
                "client_id and client_secret are required for hosted mode. "
                "Pass them in AirbyteAuthConfig, as keyword arguments, "
                "or set AIRBYTE_CLIENT_ID/AIRBYTE_CLIENT_SECRET."
            )
        return HostedExecutor(
            airbyte_client_id=hosted_client_id,
            airbyte_client_secret=hosted_client_secret,
            connector_id=auth_config.connector_id,
            workspace_name=auth_config.workspace_name or "default",
            organization_id=auth_config.organization_id or resolved_org_id,
            connector_definition_id=definition_id,
            model=model,
        )

    return HostedExecutor(
        airbyte_client_id=resolved_client_id,
        airbyte_client_secret=resolved_client_secret,
        connector_id=connector_id,
        workspace_name=resolved_ws,
        organization_id=resolved_org_id,
        connector_definition_id=definition_id,
        model=model,
    )
