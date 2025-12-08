"""
github connector.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from .types import (
    RepositoriesGetParams,
    RepositoriesListParams,
    RepositoriesSearchParams,
)

if TYPE_CHECKING:
    from .models import GithubAuthConfig

# Import response models and envelope models at runtime
from .models import (
    GithubExecuteResult,
    GithubExecuteResultWithMeta,
)


class GithubConnector:
    """
    Type-safe Github API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "github"
    connector_version = "0.1.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("repositories", "get"): False,
        ("repositories", "list"): False,
        ("repositories", "search"): False,
    }

    def __init__(
        self,
        auth_config: GithubAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new github connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide `connector_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            config_path: Optional path to connector config (uses bundled default if None)
            connector_id: Connector ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            airbyte_connector_api_url: Airbyte connector API URL (defaults to Airbyte Cloud API URL)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = GithubConnector(auth_config=GithubAuthConfig(access_token="...", refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = GithubConnector(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = GithubConnector(
                auth_config=GithubAuthConfig(access_token="...", refresh_token="..."),
                on_token_refresh=save_tokens
            )
        """
        # Hosted mode: connector_id, airbyte_client_id, and airbyte_client_secret provided
        if connector_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                connector_id=connector_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                api_url=airbyte_connector_api_url,
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide (connector_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                    "or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            if not config_path:
                config_path = str(self.get_default_config_path())

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                config_path=config_path,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.repositories = RepositoriesQuery(self)

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["repositories"],
        action: Literal["get"],
        params: "RepositoriesGetParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["repositories"],
        action: Literal["list"],
        params: "RepositoriesListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["repositories"],
        action: Literal["search"],
        params: "RepositoriesSearchParams"
    ) -> "dict[str, Any]": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> GithubExecuteResult[Any] | GithubExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any] | None = None
    ) -> Any:
        """
        Execute an entity operation with full type safety.

        This is the recommended interface for blessed connectors as it:
        - Uses the same signature as non-blessed connectors
        - Provides full IDE autocomplete for entity/action/params
        - Makes migration from generic to blessed connectors seamless

        Args:
            entity: Entity name (e.g., "customers")
            action: Operation action (e.g., "create", "get", "list")
            params: Operation parameters (typed based on entity+action)

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from ._vendored.connector_sdk.executor import ExecutionConfig

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._EXTRACTOR_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return GithubExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GithubExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data



class RepositoriesQuery:
    """
    Query class for Repositories entity operations.
    """

    def __init__(self, connector: GithubConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def get(
        self,
        owner: str,
        repo: str,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Gets information about a specific GitHub repository using GraphQL

        Args:
            owner: The account owner of the repository (username or organization)
            repo: The name of the repository
            fields: Optional array of field names to select.
If not provided, uses default fields.

            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "owner": owner,
            "repo": repo,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("repositories", "get", params)
        return result



    async def list(
        self,
        username: str,
        per_page: int | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a list of repositories for the specified user using GraphQL

        Args:
            username: The username of the user whose repositories to list
            per_page: The number of results per page
            fields: Optional array of field names to select.
If not provided, uses default fields.

            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "username": username,
            "per_page": per_page,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("repositories", "list", params)
        return result



    async def search(
        self,
        query: str,
        limit: int | None = None,
        fields: list[str] | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Search for GitHub repositories using GitHub's powerful search syntax.
Examples: "language:python stars:>1000", "topic:machine-learning", "org:facebook is:public"


        Args:
            query: GitHub repository search query. Examples:
- "language:python stars:>1000"
- "topic:machine-learning"
- "org:facebook is:public"

            limit: Number of results to return
            fields: Optional array of field names to select.
If not provided, uses default fields.

            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "query": query,
            "limit": limit,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("repositories", "search", params)
        return result


