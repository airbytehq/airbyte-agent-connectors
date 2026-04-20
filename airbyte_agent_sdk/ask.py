"""ask() — one-call natural language query across all workspace connectors."""

from __future__ import annotations

import asyncio
import concurrent.futures

from airbyte_agent_sdk.cloud_utils import AirbyteCloudClient
from airbyte_agent_sdk.config import resolve_credentials
from airbyte_agent_sdk.executor.models import AskResult


async def ask(
    prompt: str,
    *,
    client_id: str | None = None,
    client_secret: str | None = None,
    workspace_name: str | None = None,
    organization_id: str | None = None,
) -> AskResult:
    """Ask a natural-language question across all connectors in a workspace.

    Simplest entry point — no [`Workspace`](#Workspace) or
    [`connect()`](#connect) needed. Credentials are read from
    `AIRBYTE_CLIENT_ID` / `AIRBYTE_CLIENT_SECRET` if not supplied.

    Example:
        ```python
        import os
        import asyncio
        from airbyte_agent_sdk import ask

        os.environ["AIRBYTE_CLIENT_ID"] = "your_client_id"
        os.environ["AIRBYTE_CLIENT_SECRET"] = "your_client_secret"

        async def main():
            result = await ask("list my 5 most recent Stripe customers")
            print(result.outcome, result.answer)
            for call in result.results:
                print(call.entity, call.action, call.status)

        asyncio.run(main())
        ```

    Args:
        prompt: Natural-language question to dispatch across the workspace.
        client_id: Airbyte OAuth client ID (falls back to `AIRBYTE_CLIENT_ID`).
        client_secret: Airbyte OAuth client secret (falls back to
            `AIRBYTE_CLIENT_SECRET`).
        workspace_name: Workspace to query. Defaults to `"default"`.
        organization_id: Optional organization ID for multi-org routing.

    Returns:
        An [`AskResult`](#AskResult) with `outcome`, optional `answer`, and a
        `results` list of per-tool-call records. Check `outcome == "success"`
        before trusting `answer`.

    Raises:
        ValueError: If no credentials are supplied and no env vars are set.
        httpx.HTTPStatusError: If the backend returns a 4xx/5xx response.

    See also:
        [`ask_sync`](#ask_sync) — blocking wrapper for scripts and notebooks.
    """
    resolved_id, resolved_secret, resolved_org_id, resolved_ws = resolve_credentials(
        client_id=client_id,
        client_secret=client_secret,
        organization_id=organization_id,
        workspace_name=workspace_name,
    )
    client = AirbyteCloudClient(client_id=resolved_id, client_secret=resolved_secret, organization_id=resolved_org_id)
    try:
        response = await client.ask_workspace(resolved_ws, prompt)
        return AskResult.from_response(response)
    finally:
        await client.close()


def ask_sync(
    prompt: str,
    *,
    client_id: str | None = None,
    client_secret: str | None = None,
    workspace_name: str | None = None,
    organization_id: str | None = None,
) -> AskResult:
    """Blocking variant of [`ask`](#ask). Works in scripts and notebooks.

    In a plain script (no running event loop) this uses `asyncio.run()`.
    Inside a Jupyter notebook or other environment that already has a running
    loop, it dispatches the coroutine to a background thread so it does not
    block the existing loop.

    Example:
        ```python
        from airbyte_agent_sdk import ask_sync

        result = ask_sync(
            "list my 5 most recent Stripe customers",
            client_id="your_client_id",
            client_secret="your_client_secret",
        )
        print(result.outcome, result.answer)
        ```

    Args:
        prompt: Natural-language question to dispatch across the workspace.
        client_id: Airbyte OAuth client ID (falls back to `AIRBYTE_CLIENT_ID`).
        client_secret: Airbyte OAuth client secret (falls back to
            `AIRBYTE_CLIENT_SECRET`).
        workspace_name: Workspace to query. Defaults to `"default"`.
        organization_id: Optional organization ID for multi-org routing.

    Returns:
        An [`AskResult`](#AskResult) — same shape as [`ask`](#ask).

    Raises:
        ValueError: If no credentials are supplied and no env vars are set.
        httpx.HTTPStatusError: If the backend returns a 4xx/5xx response.

    See also:
        [`ask`](#ask) — the async version for use in async applications.
    """
    coro = ask(
        prompt,
        client_id=client_id,
        client_secret=client_secret,
        workspace_name=workspace_name,
        organization_id=organization_id,
    )
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        return pool.submit(asyncio.run, coro).result()
