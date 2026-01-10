"""
commonroom connector.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, Callable, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .connector_model import CommonroomConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    ActivityTypesListParams,
    ApiTokenStatusListParams,
    ContactCustomFieldsListParams,
    SegmentsListParams,
    TagsListParams,
)
if TYPE_CHECKING:
    from .models import CommonroomAuthConfig
# Import response models and envelope models at runtime
from .models import (
    CommonroomExecuteResult,
    CommonroomExecuteResultWithMeta,
    TagsListResult,
    ApiTokenStatus,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])


class CommonroomConnector:
    """
    Type-safe Commonroom API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "commonroom"
    connector_version = "0.1.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("api_token_status", "list"): False,
        ("contact_custom_fields", "list"): False,
        ("activity_types", "list"): False,
        ("segments", "list"): False,
        ("tags", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
    }

    def __init__(
        self,
        auth_config: CommonroomAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new commonroom connector instance.

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
            connector = CommonroomConnector(auth_config=CommonroomAuthConfig(api_token="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = CommonroomConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = CommonroomConnector(
                auth_config=CommonroomAuthConfig(access_token="...", refresh_token="..."),
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
                connector_definition_id=str(CommonroomConnectorModel.id),
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
                model=CommonroomConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.api_token_status = ApiTokenStatusQuery(self)
        self.contact_custom_fields = ContactCustomFieldsQuery(self)
        self.activity_types = ActivityTypesQuery(self)
        self.segments = SegmentsQuery(self)
        self.tags = TagsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["api_token_status"],
        action: Literal["list"],
        params: "ApiTokenStatusListParams"
    ) -> "ApiTokenStatus": ...

    @overload
    async def execute(
        self,
        entity: Literal["contact_custom_fields"],
        action: Literal["list"],
        params: "ContactCustomFieldsListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["activity_types"],
        action: Literal["list"],
        params: "ActivityTypesListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["segments"],
        action: Literal["list"],
        params: "SegmentsListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["tags"],
        action: Literal["list"],
        params: "TagsListParams"
    ) -> "TagsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> CommonroomExecuteResult[Any] | CommonroomExecuteResultWithMeta[Any, Any] | Any: ...

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
                return CommonroomExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return CommonroomExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== INTROSPECTION METHODS =====

    @classmethod
    def describe(cls, func: _F) -> _F:
        """
        Decorator that populates a function's docstring with connector capabilities.

        This class method can be used as a decorator to automatically generate
        comprehensive documentation for AI tool functions.

        Usage:
            @mcp.tool()
            @CommonroomConnector.describe
            async def execute(entity: str, action: str, params: dict):
                '''Execute operations.'''
                ...

        The decorated function's __doc__ will be updated with:
        - Available entities and their actions
        - Parameter signatures with required (*) and optional (?) markers
        - Response structure documentation
        - Example questions (if available in OpenAPI spec)

        Args:
            func: The function to decorate

        Returns:
            The same function with updated __doc__
        """
        description = generate_tool_description(CommonroomConnectorModel)

        original_doc = func.__doc__ or ""
        if original_doc.strip():
            func.__doc__ = f"{original_doc.strip()}\n\n{description}"
        else:
            func.__doc__ = description

        return func

    def list_entities(self) -> list[dict[str, Any]]:
        """
        Get structured data about available entities, actions, and parameters.

        Returns a list of entity descriptions with:
        - entity_name: Name of the entity (e.g., "contacts", "deals")
        - description: Entity description from the first endpoint
        - available_actions: List of actions (e.g., ["list", "get", "create"])
        - parameters: Dict mapping action -> list of parameter dicts

        Example:
            entities = connector.list_entities()
            for entity in entities:
                print(f"{entity['entity_name']}: {entity['available_actions']}")
        """
        return describe_entities(CommonroomConnectorModel)

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
            (e for e in CommonroomConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in CommonroomConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None



class ApiTokenStatusQuery:
    """
    Query class for ApiTokenStatus entity operations.
    """

    def __init__(self, connector: CommonroomConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> ApiTokenStatus:
        """
        Returns the status and metadata of the current API token

        Returns:
            ApiTokenStatus
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("api_token_status", "list", params)
        return result



class ContactCustomFieldsQuery:
    """
    Query class for ContactCustomFields entity operations.
    """

    def __init__(self, connector: CommonroomConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns all custom fields defined for contacts/members

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contact_custom_fields", "list", params)
        return result



class ActivityTypesQuery:
    """
    Query class for ActivityTypes entity operations.
    """

    def __init__(self, connector: CommonroomConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns all activity types in the community

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("activity_types", "list", params)
        return result



class SegmentsQuery:
    """
    Query class for Segments entity operations.
    """

    def __init__(self, connector: CommonroomConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns all segments in the community

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segments", "list", params)
        return result



class TagsQuery:
    """
    Query class for Tags entity operations.
    """

    def __init__(self, connector: CommonroomConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> TagsListResult:
        """
        Returns all tags in the community

        Returns:
            TagsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "list", params)
        # Cast generic envelope to concrete typed result
        return TagsListResult(
            data=result.data        )


