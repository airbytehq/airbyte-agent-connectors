"""
intercom connector.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .connector_model import IntercomConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities

from .types import (
    AdminsGetParams,
    AdminsListParams,
    CompaniesGetParams,
    CompaniesListParams,
    ContactsGetParams,
    ContactsListParams,
    ConversationsGetParams,
    ConversationsListParams,
    SegmentsGetParams,
    SegmentsListParams,
    TagsGetParams,
    TagsListParams,
    TeamsGetParams,
    TeamsListParams,
)

if TYPE_CHECKING:
    from .models import IntercomAuthConfig
# Import response models and envelope models at runtime
from .models import (
    IntercomExecuteResult,
    IntercomExecuteResultWithMeta,
    ContactsListResult,
    ConversationsListResult,
    CompaniesListResult,
    TeamsListResult,
    AdminsListResult,
    TagsListResult,
    SegmentsListResult,
    Admin,
    Company,
    Contact,
    Conversation,
    Segment,
    Tag,
    Team,
)


class IntercomConnector:
    """
    Type-safe Intercom API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "intercom"
    connector_version = "0.1.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("contacts", "list"): True,
        ("contacts", "get"): False,
        ("conversations", "list"): True,
        ("conversations", "get"): False,
        ("companies", "list"): True,
        ("companies", "get"): False,
        ("teams", "list"): True,
        ("teams", "get"): False,
        ("admins", "list"): True,
        ("admins", "get"): False,
        ("tags", "list"): True,
        ("tags", "get"): False,
        ("segments", "list"): True,
        ("segments", "get"): False,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('contacts', 'list'): {'per_page': 'per_page', 'starting_after': 'starting_after'},
        ('contacts', 'get'): {'id': 'id'},
        ('conversations', 'list'): {'per_page': 'per_page', 'starting_after': 'starting_after'},
        ('conversations', 'get'): {'id': 'id'},
        ('companies', 'list'): {'per_page': 'per_page', 'starting_after': 'starting_after'},
        ('companies', 'get'): {'id': 'id'},
        ('teams', 'get'): {'id': 'id'},
        ('admins', 'get'): {'id': 'id'},
        ('tags', 'get'): {'id': 'id'},
        ('segments', 'list'): {'include_count': 'include_count'},
        ('segments', 'get'): {'id': 'id'},
    }

    def __init__(
        self,
        auth_config: IntercomAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new intercom connector instance.

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
            connector = IntercomConnector(auth_config=IntercomAuthConfig(access_token="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = IntercomConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = IntercomConnector(
                auth_config=IntercomAuthConfig(access_token="...", refresh_token="..."),
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
                connector_definition_id=str(IntercomConnectorModel.id),
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
                model=IntercomConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.contacts = ContactsQuery(self)
        self.conversations = ConversationsQuery(self)
        self.companies = CompaniesQuery(self)
        self.teams = TeamsQuery(self)
        self.admins = AdminsQuery(self)
        self.tags = TagsQuery(self)
        self.segments = SegmentsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["list"],
        params: "ContactsListParams"
    ) -> "ContactsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["contacts"],
        action: Literal["get"],
        params: "ContactsGetParams"
    ) -> "Contact": ...

    @overload
    async def execute(
        self,
        entity: Literal["conversations"],
        action: Literal["list"],
        params: "ConversationsListParams"
    ) -> "ConversationsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["conversations"],
        action: Literal["get"],
        params: "ConversationsGetParams"
    ) -> "Conversation": ...

    @overload
    async def execute(
        self,
        entity: Literal["companies"],
        action: Literal["list"],
        params: "CompaniesListParams"
    ) -> "CompaniesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["companies"],
        action: Literal["get"],
        params: "CompaniesGetParams"
    ) -> "Company": ...

    @overload
    async def execute(
        self,
        entity: Literal["teams"],
        action: Literal["list"],
        params: "TeamsListParams"
    ) -> "TeamsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["teams"],
        action: Literal["get"],
        params: "TeamsGetParams"
    ) -> "Team": ...

    @overload
    async def execute(
        self,
        entity: Literal["admins"],
        action: Literal["list"],
        params: "AdminsListParams"
    ) -> "AdminsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["admins"],
        action: Literal["get"],
        params: "AdminsGetParams"
    ) -> "Admin": ...

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
        entity: Literal["tags"],
        action: Literal["get"],
        params: "TagsGetParams"
    ) -> "Tag": ...

    @overload
    async def execute(
        self,
        entity: Literal["segments"],
        action: Literal["list"],
        params: "SegmentsListParams"
    ) -> "SegmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["segments"],
        action: Literal["get"],
        params: "SegmentsGetParams"
    ) -> "Segment": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> IntercomExecuteResult[Any] | IntercomExecuteResultWithMeta[Any, Any] | Any: ...

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
                return IntercomExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return IntercomExecuteResult[Any](data=result.data)
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
        return describe_entities(IntercomConnectorModel)

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
            (e for e in IntercomConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in IntercomConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None



class ContactsQuery:
    """
    Query class for Contacts entity operations.
    """

    def __init__(self, connector: IntercomConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        starting_after: str | None = None,
        **kwargs
    ) -> ContactsListResult:
        """
        Returns a paginated list of contacts in the workspace

        Args:
            per_page: Number of contacts to return per page
            starting_after: Cursor for pagination - get contacts after this ID
            **kwargs: Additional parameters

        Returns:
            ContactsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "starting_after": starting_after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "list", params)
        # Cast generic envelope to concrete typed result
        return ContactsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Contact:
        """
        Get a single contact by ID

        Args:
            id: Contact ID
            **kwargs: Additional parameters

        Returns:
            Contact
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "get", params)
        return result



class ConversationsQuery:
    """
    Query class for Conversations entity operations.
    """

    def __init__(self, connector: IntercomConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        starting_after: str | None = None,
        **kwargs
    ) -> ConversationsListResult:
        """
        Returns a paginated list of conversations

        Args:
            per_page: Number of conversations to return per page
            starting_after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            ConversationsListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "starting_after": starting_after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("conversations", "list", params)
        # Cast generic envelope to concrete typed result
        return ConversationsListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Conversation:
        """
        Get a single conversation by ID

        Args:
            id: Conversation ID
            **kwargs: Additional parameters

        Returns:
            Conversation
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("conversations", "get", params)
        return result



class CompaniesQuery:
    """
    Query class for Companies entity operations.
    """

    def __init__(self, connector: IntercomConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        starting_after: str | None = None,
        **kwargs
    ) -> CompaniesListResult:
        """
        Returns a paginated list of companies

        Args:
            per_page: Number of companies to return per page
            starting_after: Cursor for pagination
            **kwargs: Additional parameters

        Returns:
            CompaniesListResult
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "starting_after": starting_after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("companies", "list", params)
        # Cast generic envelope to concrete typed result
        return CompaniesListResult(
            data=result.data,
            meta=result.meta        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Company:
        """
        Get a single company by ID

        Args:
            id: Company ID
            **kwargs: Additional parameters

        Returns:
            Company
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("companies", "get", params)
        return result



class TeamsQuery:
    """
    Query class for Teams entity operations.
    """

    def __init__(self, connector: IntercomConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> TeamsListResult:
        """
        Returns a list of all teams in the workspace

        Returns:
            TeamsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "list", params)
        # Cast generic envelope to concrete typed result
        return TeamsListResult(
            data=result.data        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Team:
        """
        Get a single team by ID

        Args:
            id: Team ID
            **kwargs: Additional parameters

        Returns:
            Team
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("teams", "get", params)
        return result



class AdminsQuery:
    """
    Query class for Admins entity operations.
    """

    def __init__(self, connector: IntercomConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> AdminsListResult:
        """
        Returns a list of all admins in the workspace

        Returns:
            AdminsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("admins", "list", params)
        # Cast generic envelope to concrete typed result
        return AdminsListResult(
            data=result.data        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Admin:
        """
        Get a single admin by ID

        Args:
            id: Admin ID
            **kwargs: Additional parameters

        Returns:
            Admin
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("admins", "get", params)
        return result



class TagsQuery:
    """
    Query class for Tags entity operations.
    """

    def __init__(self, connector: IntercomConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> TagsListResult:
        """
        Returns a list of all tags in the workspace

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



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Tag:
        """
        Get a single tag by ID

        Args:
            id: Tag ID
            **kwargs: Additional parameters

        Returns:
            Tag
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "get", params)
        return result



class SegmentsQuery:
    """
    Query class for Segments entity operations.
    """

    def __init__(self, connector: IntercomConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        include_count: bool | None = None,
        **kwargs
    ) -> SegmentsListResult:
        """
        Returns a list of all segments in the workspace

        Args:
            include_count: Include count of contacts in each segment
            **kwargs: Additional parameters

        Returns:
            SegmentsListResult
        """
        params = {k: v for k, v in {
            "include_count": include_count,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segments", "list", params)
        # Cast generic envelope to concrete typed result
        return SegmentsListResult(
            data=result.data        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Segment:
        """
        Get a single segment by ID

        Args:
            id: Segment ID
            **kwargs: Additional parameters

        Returns:
            Segment
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segments", "get", params)
        return result


