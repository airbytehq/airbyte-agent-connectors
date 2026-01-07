"""
linear connector.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .connector_model import LinearConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities

from .types import (
    IssuesGetParams,
    IssuesListParams,
    ProjectsGetParams,
    ProjectsListParams,
    TeamsGetParams,
    TeamsListParams,
)

if TYPE_CHECKING:
    from .models import LinearAuthConfig
# Import response models and envelope models at runtime
from .models import (
    LinearExecuteResult,
    LinearExecuteResultWithMeta,
    IssueResponse,
    IssuesListResponse,
    ProjectResponse,
    ProjectsListResponse,
    TeamResponse,
    TeamsListResponse,
)


class LinearConnector:
    """
    Type-safe Linear API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "linear"
    connector_version = "0.1.2"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("issues", "list"): False,
        ("issues", "get"): False,
        ("projects", "list"): False,
        ("projects", "get"): False,
        ("teams", "list"): False,
        ("teams", "get"): False,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('issues', 'list'): {'first': 'first', 'after': 'after'},
        ('issues', 'get'): {'id': 'id'},
        ('projects', 'list'): {'first': 'first', 'after': 'after'},
        ('projects', 'get'): {'id': 'id'},
        ('teams', 'list'): {'first': 'first', 'after': 'after'},
        ('teams', 'get'): {'id': 'id'},
    }

    def __init__(
        self,
        auth_config: LinearAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new linear connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide `external_user_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            external_user_id: External user ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = LinearConnector(auth_config=LinearAuthConfig(api_key="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = LinearConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = LinearConnector(
                auth_config=LinearAuthConfig(access_token="...", refresh_token="..."),
                on_token_refresh=save_tokens
            )
        """
        # Hosted mode: external_user_id, airbyte_client_id, and airbyte_client_secret provided
        if external_user_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                external_user_id=external_user_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                connector_definition_id=str(LinearConnectorModel.id),
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide (external_user_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                    "or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=LinearConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.issues = IssuesQuery(self)
        self.projects = ProjectsQuery(self)
        self.teams = TeamsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["list"],
        params: "IssuesListParams"
    ) -> "IssuesListResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["issues"],
        action: Literal["get"],
        params: "IssuesGetParams"
    ) -> "IssueResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["list"],
        params: "ProjectsListParams"
    ) -> "ProjectsListResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["projects"],
        action: Literal["get"],
        params: "ProjectsGetParams"
    ) -> "ProjectResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["teams"],
        action: Literal["list"],
        params: "TeamsListParams"
    ) -> "TeamsListResponse": ...

    @overload
    async def execute(
        self,
        entity: Literal["teams"],
        action: Literal["get"],
        params: "TeamsGetParams"
    ) -> "TeamResponse": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> LinearExecuteResult[Any] | LinearExecuteResultWithMeta[Any, Any] | Any: ...

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

        # Remap parameter names from snake_case (TypedDict keys) to API parameter names
        if params:
            param_map = self._PARAM_MAP.get((entity, action), {})
            if param_map:
                params = {param_map.get(k, k): v for k, v in params.items()}

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
                return LinearExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return LinearExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== INTROSPECTION METHODS =====

    def describe(self) -> list[dict[str, Any]]:
        """
        Describe available entities, actions, and parameters.

        Returns a list of entity descriptions with:
        - entity_name: Name of the entity (e.g., "contacts", "deals")
        - description: Entity description from the first endpoint
        - available_actions: List of actions (e.g., ["list", "get", "create"])
        - parameters: Dict mapping action -> list of parameter dicts

        Example:
            entities = connector.describe()
            for entity in entities:
                print(f"{entity['entity_name']}: {entity['available_actions']}")
        """
        return describe_entities(LinearConnectorModel)

    def entity_schema(self, entity: str) -> dict[str, Any] | None:
        """
        Get the JSON schema for an entity.

        Args:
            entity: Entity name (e.g., "contacts", "companies")

        Returns:
            JSON schema dict describing the entity structure, or None if not found.

        Example:
            schema = connector.entity_schema("contacts")
            if schema:
                print(f"Contact properties: {list(schema.get('properties', {}).keys())}")
        """
        entity_def = next(
            (e for e in LinearConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in LinearConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None



class IssuesQuery:
    """
    Query class for Issues entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> IssuesListResponse:
        """
        Returns a paginated list of issues via GraphQL with pagination support

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            IssuesListResponse
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> IssueResponse:
        """
        Get a single issue by ID via GraphQL

        Args:
            id: Issue ID
            **kwargs: Additional parameters

        Returns:
            IssueResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("issues", "get", params)
        return result



class ProjectsQuery:
    """
    Query class for Projects entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> ProjectsListResponse:
        """
        Returns a paginated list of projects via GraphQL with pagination support

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            ProjectsListResponse
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ProjectResponse:
        """
        Get a single project by ID via GraphQL

        Args:
            id: Project ID
            **kwargs: Additional parameters

        Returns:
            ProjectResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("projects", "get", params)
        return result



class TeamsQuery:
    """
    Query class for Teams entity operations.
    """

    def __init__(self, connector: LinearConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        first: int | None = None,
        after: str | None = None,
        **kwargs
    ) -> TeamsListResponse:
        """
        Returns a list of teams via GraphQL with pagination support

        Args:
            first: Number of items to return (max 250)
            after: Cursor to start after (for pagination)
            **kwargs: Additional parameters

        Returns:
            TeamsListResponse
        """
        params = {k: v for k, v in {
            "first": first,
            "after": after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> TeamResponse:
        """
        Get a single team by ID via GraphQL

        Args:
            id: Team ID
            **kwargs: Additional parameters

        Returns:
            TeamResponse
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "get", params)
        return result


