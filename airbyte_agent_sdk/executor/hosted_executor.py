"""Hosted executor for proxying operations through the cloud API."""

from __future__ import annotations

import os
from typing import Any, overload

from opentelemetry import trace

from airbyte_agent_sdk.cloud_utils import AirbyteCloudClient

from .models import (
    ExecutionConfig,
    ExecutionResult,
    find_check_operation,
)


class HostedExecutor:
    """Executor that proxies execution through the Airbyte Cloud API.

    This is the "hosted mode" executor that makes HTTP calls to the cloud API
    instead of directly calling external services. The cloud API handles all
    connector logic, secrets management, and execution.

    The executor uses the AirbyteCloudClient to:
    1. Authenticate with the Airbyte Platform (bearer token with caching)
    2. Look up the user's connector (if connector_id not provided)
    3. Execute the connector operation via the cloud API

    Implements ExecutorProtocol.

    Example:
        # Create executor with explicit connector_id (no lookup needed)
        executor = HostedExecutor(
            airbyte_client_id="client_abc123",
            airbyte_client_secret="secret_xyz789",
            connector_id="existing-source-uuid",
        )

        # Or create executor with workspace_name for lookup
        executor = HostedExecutor(
            airbyte_client_id="client_abc123",
            airbyte_client_secret="secret_xyz789",
            workspace_name="user-123",
            organization_id="00000000-0000-0000-0000-000000000123",
            connector_definition_id="abc123-def456-ghi789",
        )

        # Execute an operation
        execution_config = ExecutionConfig(
            entity="customers",
            action="list",
            params={"limit": 10}
        )

        result = await executor.execute(execution_config)
        if result.success:
            print(f"Data: {result.data}")
        else:
            print(f"Error: {result.error}")
    """

    def __init__(
        self,
        airbyte_client_id: str,
        airbyte_client_secret: str,
        connector_id: str | None = None,
        workspace_name: str | None = None,
        connector_definition_id: str | None = None,
        organization_id: str | None = None,
        model: Any | None = None,
    ):
        """Initialize hosted executor.

        Either provide `connector_id` directly OR (`workspace_name` +
        `connector_definition_id`) for lookup. When neither `connector_id`
        nor `workspace_name` is provided, `workspace_name` defaults to
        `"default"`, so the lookup resolves against the workspace literally
        named "default" as long as `connector_definition_id` is supplied.

        Args:
            airbyte_client_id: Airbyte client ID for authentication
            airbyte_client_secret: Airbyte client secret for authentication
            connector_id: Direct connector/source ID (skips lookup if provided)
            workspace_name: Workspace name for connector lookup. Defaults to
                `"default"` when neither this nor `connector_id` is provided.
            connector_definition_id: Connector definition ID (for lookup)
            organization_id: Optional Airbyte organization ID for multi-org request routing
            model: Optional ConnectorModel for health check operation selection

        Raises:
            ValueError: If neither `connector_id` nor `connector_definition_id` is provided
                (a missing `workspace_name` alone no longer raises, since it now
                defaults to `"default"`).

        Example:
            # With explicit connector_id (no lookup)
            executor = HostedExecutor(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid",
            )

            # With lookup by workspace_name + definition
            executor = HostedExecutor(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                workspace_name="user-123",
                organization_id="00000000-0000-0000-0000-000000000123",
                connector_definition_id="abc123-def456-ghi789",
            )
        """
        # When neither a direct connector_id nor a workspace_name is supplied,
        # fall back to the workspace literally named "default" so callers like
        # `LinearConnector(auth_config=AirbyteAuthConfig(client_id, secret))`
        # do not have to pass workspace_name explicitly.
        if not connector_id and not workspace_name:
            workspace_name = "default"

        resolved_workspace_name = workspace_name

        # Validate: either connector_id OR (workspace_name + connector_definition_id) required
        if not connector_id and not (resolved_workspace_name and connector_definition_id):
            raise ValueError("Either connector_id OR (workspace_name + connector_definition_id) must be provided")

        resolved_organization_id = organization_id or os.environ.get("AIRBYTE_ORGANIZATION_ID")

        self._connector_id = connector_id
        self._workspace_name = resolved_workspace_name
        self._organization_id = resolved_organization_id
        self._connector_definition_id = connector_definition_id
        self._connector_model = model

        # Create AirbyteCloudClient for API interactions
        self._cloud_client = AirbyteCloudClient(
            client_id=airbyte_client_id,
            client_secret=airbyte_client_secret,
            organization_id=resolved_organization_id,
        )

    async def _resolve_connector_id(self) -> str:
        if self._connector_id is not None:
            return self._connector_id
        connector_id = await self._cloud_client.get_connector_id(
            workspace_name=self._workspace_name,  # type: ignore[arg-type]
            connector_definition_id=self._connector_definition_id,  # type: ignore[arg-type]
        )
        self._connector_id = connector_id
        return connector_id

    @overload
    async def execute(self, config_or_entity: ExecutionConfig) -> ExecutionResult: ...

    @overload
    async def execute(self, *, config: ExecutionConfig) -> ExecutionResult: ...

    @overload
    async def execute(self, *, config_or_entity: ExecutionConfig) -> ExecutionResult: ...

    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        *,
        params: dict[str, Any] | None = None,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True,
        intent: str | None = None,
    ) -> ExecutionResult: ...

    @overload
    async def execute(
        self,
        *,
        config_or_entity: str,
        action: str,
        params: dict[str, Any] | None = None,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True,
        intent: str | None = None,
    ) -> ExecutionResult: ...

    @overload
    async def execute(
        self,
        *,
        entity: str,
        action: str,
        params: dict[str, Any] | None = None,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True,
        intent: str | None = None,
    ) -> ExecutionResult: ...

    async def execute(
        self,
        *args: ExecutionConfig | str,
        config_or_entity: ExecutionConfig | str | None = None,
        config: ExecutionConfig | None = None,
        params: dict[str, Any] | None = None,
        entity: str | None = None,
        action: str | None = None,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True,
        intent: str | None = None,
    ) -> ExecutionResult:
        """Execute connector via cloud API (ExecutorProtocol implementation).

        Accepts either an :class:`ExecutionConfig`, positional ``(entity, action)``
        strings, or keyword ``entity=...``/``action=...`` strings.

        Flow:
        1. Use provided connector_id or look up from workspace_name + definition_id
        2. Execute the connector operation via the cloud API
        3. Parse the response into ExecutionResult

        Args:
            config_or_entity: Backward-compatible alias for either an
                ExecutionConfig object or entity name string.
            config: ExecutionConfig object
            entity: Entity name string, or an ExecutionConfig when passed positionally
            action: Action string (required when entity is a string)
            params: Optional parameters dict (only with string form)
            select_fields: Optional allowlist of dot-notation fields to include
                (only with string form)
            exclude_fields: Optional blocklist of dot-notation fields to remove
                (only with string form)
            skip_truncation: Disable long-text truncation for collection actions
                (only with string form)
            intent: Optional short description of why this execution is being
                performed, max 512 chars (only with string form)

        Returns:
            ExecutionResult with success/failure status

        Raises:
            TypeError: If action/params are passed together with an ExecutionConfig,
                or if action is omitted when using the string form
            ValueError: If no connector or multiple connectors found for user (when doing lookup)
            AuthenticationError: If API returns 401/403
            RateLimitError: If API returns 429
            ConnectorValidationError: If API returns 400/422 (retryable by LLM)
            HTTPStatusError: If API returns any other 4xx/5xx status code
            httpx.RequestError: If network request fails

        Example:
            config = ExecutionConfig(
                entity="customers",
                action="list",
                params={"limit": 10}
            )
            result = await executor.execute(config)

            # Shorthand form:
            result = await executor.execute("customers", "list", params={"limit": 10})
        """
        if len(args) > 2:
            raise TypeError("execute accepts at most two positional arguments")
        keyword_selector_count = sum(value is not None for value in (config_or_entity, config, entity))
        if args and keyword_selector_count:
            raise TypeError("Pass either positional arguments or config_or_entity/config/entity keywords, not both")
        if len(args) == 2:
            selected_config_or_entity = args[0]
            if action is not None:
                raise TypeError("Pass action either positionally or by keyword, not both")
            if not isinstance(args[1], str):
                raise TypeError("action must be a string")
            action = args[1]
        elif len(args) == 1:
            selected_config_or_entity = args[0]
            if not isinstance(selected_config_or_entity, str) and action is not None:
                raise TypeError("Cannot pass action, params, field selection, truncation, or intent options when using ExecutionConfig")
        else:
            if keyword_selector_count > 1:
                raise TypeError("Pass only one of config_or_entity, config, or entity")
            selected_config_or_entity = config_or_entity if config_or_entity is not None else config if config is not None else entity
        if selected_config_or_entity is None:
            raise TypeError("Either config_or_entity, config, or entity is required")
        if isinstance(selected_config_or_entity, str):
            if action is None:
                raise TypeError("action is required when passing entity as a string")
            execution_config = ExecutionConfig(
                entity=selected_config_or_entity,
                action=action,
                params=params,
                select_fields=select_fields,
                exclude_fields=exclude_fields,
                skip_truncation=skip_truncation,
                intent=intent,
            )
        else:
            if (
                action is not None
                or params is not None
                or select_fields is not None
                or exclude_fields is not None
                or skip_truncation is not True
                or intent is not None
            ):
                raise TypeError("Cannot pass action, params, field selection, truncation, or intent options when using ExecutionConfig")
            execution_config = selected_config_or_entity
        tracer = trace.get_tracer("airbyte.connector-sdk.executor.hosted")

        with tracer.start_as_current_span("airbyte.hosted_executor.execute") as span:
            # Add span attributes for observability
            if self._connector_definition_id:
                span.set_attribute("connector.definition_id", self._connector_definition_id)
            span.set_attribute("connector.entity", execution_config.entity)
            span.set_attribute("connector.action", execution_config.action)
            if self._workspace_name:
                span.set_attribute("workspace.name", self._workspace_name)
            if self._organization_id:
                span.set_attribute("organization.id", self._organization_id)
            if execution_config.params:
                # Only add non-sensitive param keys
                span.set_attribute("connector.param_keys", list(execution_config.params.keys()))

            try:
                connector_id = await self._resolve_connector_id()

                span.set_attribute("connector.connector_id", connector_id)

                # Step 3: Execute the connector via the cloud API
                response = await self._cloud_client.execute_connector(
                    connector_id=connector_id,
                    entity=execution_config.entity,
                    action=execution_config.action,
                    params=execution_config.params,
                    select_fields=execution_config.select_fields,
                    exclude_fields=execution_config.exclude_fields,
                    skip_truncation=execution_config.skip_truncation,
                    intent=execution_config.intent,
                )

                # Step 4: Parse the response into ExecutionResult
                result = self._parse_execution_result(response)

                # Mark span as successful
                span.set_attribute("connector.success", result.success)

                return result

            except Exception as e:
                span.set_attribute("connector.success", False)
                span.set_attribute("connector.error_type", type(e).__name__)
                span.record_exception(e)
                raise

    async def inspect_connector(self) -> dict[str, Any]:
        """Inspect hosted connector metadata and readiness."""
        connector_id = await self._resolve_connector_id()
        return await self._cloud_client.inspect_connector(connector_id)

    async def read_skill_docs(self, id: str, section: str | None = None) -> dict[str, Any]:
        """Read hosted skill docs by skill ID."""
        return await self._cloud_client.read_skill_docs(id=id, section=section)

    async def check(self) -> ExecutionResult:
        """Perform a health check by executing a lightweight operation.

        Uses the shared find_check_operation() logic (same as LocalExecutor and the
        platform backend) to find a valid entity/action pair, then executes it
        through the normal hosted execute() path.

        Falls back to credential verification if no model is available.
        """
        if self._connector_model is not None:
            check_op = find_check_operation(self._connector_model)
            if check_op:
                entity, action, params = check_op
                try:
                    await self.execute(ExecutionConfig(entity=entity, action=action.value, params=params))
                    return ExecutionResult(
                        success=True,
                        data={
                            "status": "healthy",
                            "checked_entity": entity,
                            "checked_action": action.value,
                        },
                    )
                except Exception as e:
                    return ExecutionResult(
                        success=False,
                        data={
                            "status": "unhealthy",
                            "error": str(e),
                            "checked_entity": entity,
                            "checked_action": action.value,
                        },
                        error=str(e),
                    )

        # Fallback: verify credentials are valid
        try:
            await self._cloud_client.get_bearer_token()
            return ExecutionResult(
                success=True,
                data={"status": "healthy"},
            )
        except Exception as e:
            return ExecutionResult(
                success=False,
                data={"status": "unhealthy", "error": str(e)},
                error=str(e),
            )

    def _parse_execution_result(self, response: dict) -> ExecutionResult:
        """Parse API response into ExecutionResult.

        Args:
            response_data: Raw JSON response from the cloud API

        Returns:
            ExecutionResult with parsed data
        """

        return ExecutionResult(
            success=True,
            data=response["result"],
            meta=response.get("connector_metadata"),
            error=None,
        )

    async def close(self):
        """Close the cloud client and cleanup resources.

        Call this when you're done using the executor to clean up HTTP connections.

        Example:
            executor = HostedExecutor(...)
            try:
                result = await executor.execute(config)
            finally:
                await executor.close()
        """
        await self._cloud_client.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()
