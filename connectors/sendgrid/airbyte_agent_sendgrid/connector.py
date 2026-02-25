"""
Sendgrid connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import SendgridConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    BlocksListParams,
    BouncesListParams,
    CampaignsListParams,
    ContactsGetParams,
    ContactsListParams,
    GlobalSuppressionsListParams,
    InvalidEmailsListParams,
    ListsGetParams,
    ListsListParams,
    SegmentsGetParams,
    SegmentsListParams,
    SinglesendStatsListParams,
    SinglesendsGetParams,
    SinglesendsListParams,
    SpamReportsListParams,
    SuppressionGroupMembersListParams,
    SuppressionGroupsGetParams,
    SuppressionGroupsListParams,
    TemplatesGetParams,
    TemplatesListParams,
    AirbyteSearchParams,
    BouncesSearchFilter,
    BouncesSearchQuery,
    BlocksSearchFilter,
    BlocksSearchQuery,
    CampaignsSearchFilter,
    CampaignsSearchQuery,
    ContactsSearchFilter,
    ContactsSearchQuery,
    GlobalSuppressionsSearchFilter,
    GlobalSuppressionsSearchQuery,
    InvalidEmailsSearchFilter,
    InvalidEmailsSearchQuery,
    ListsSearchFilter,
    ListsSearchQuery,
    SegmentsSearchFilter,
    SegmentsSearchQuery,
    SinglesendStatsSearchFilter,
    SinglesendStatsSearchQuery,
    SinglesendsSearchFilter,
    SinglesendsSearchQuery,
    SuppressionGroupMembersSearchFilter,
    SuppressionGroupMembersSearchQuery,
    SuppressionGroupsSearchFilter,
    SuppressionGroupsSearchQuery,
    TemplatesSearchFilter,
    TemplatesSearchQuery,
)
from .models import SendgridAuthConfig
if TYPE_CHECKING:
    from .models import SendgridReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    SendgridCheckResult,
    SendgridExecuteResult,
    SendgridExecuteResultWithMeta,
    ContactsListResult,
    ListsListResult,
    SegmentsListResult,
    CampaignsListResult,
    SinglesendsListResult,
    TemplatesListResult,
    SinglesendStatsListResult,
    BouncesListResult,
    BlocksListResult,
    SpamReportsListResult,
    InvalidEmailsListResult,
    GlobalSuppressionsListResult,
    SuppressionGroupsListResult,
    SuppressionGroupMembersListResult,
    Block,
    Bounce,
    Campaign,
    Contact,
    GlobalSuppression,
    InvalidEmail,
    List,
    Segment,
    SingleSend,
    SingleSendStats,
    SpamReport,
    SuppressionGroup,
    SuppressionGroupMember,
    Template,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    BouncesSearchData,
    BouncesSearchResult,
    BlocksSearchData,
    BlocksSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    ContactsSearchData,
    ContactsSearchResult,
    GlobalSuppressionsSearchData,
    GlobalSuppressionsSearchResult,
    InvalidEmailsSearchData,
    InvalidEmailsSearchResult,
    ListsSearchData,
    ListsSearchResult,
    SegmentsSearchData,
    SegmentsSearchResult,
    SinglesendStatsSearchData,
    SinglesendStatsSearchResult,
    SinglesendsSearchData,
    SinglesendsSearchResult,
    SuppressionGroupMembersSearchData,
    SuppressionGroupMembersSearchResult,
    SuppressionGroupsSearchData,
    SuppressionGroupsSearchResult,
    TemplatesSearchData,
    TemplatesSearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])

DEFAULT_MAX_OUTPUT_CHARS = 50_000  # ~50KB default, configurable per-tool


def _raise_output_too_large(message: str) -> None:
    try:
        from pydantic_ai import ModelRetry  # type: ignore[import-not-found]
    except Exception as exc:
        raise RuntimeError(message) from exc
    raise ModelRetry(message)


def _check_output_size(result: Any, max_chars: int | None, tool_name: str) -> Any:
    if max_chars is None or max_chars <= 0:
        return result

    try:
        serialized = json.dumps(result, default=str)
    except (TypeError, ValueError):
        return result

    if len(serialized) > max_chars:
        truncated_preview = serialized[:500] + "..." if len(serialized) > 500 else serialized
        _raise_output_too_large(
            f"Tool '{tool_name}' output too large ({len(serialized):,} chars, limit {max_chars:,}). "
            "Please narrow your query by: using the 'fields' parameter to select only needed fields, "
            "adding filters, or reducing the 'limit'. "
            f"Preview: {truncated_preview}"
        )

    return result




class SendgridConnector:
    """
    Type-safe Sendgrid API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "sendgrid"
    connector_version = "1.0.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("contacts", "list"): True,
        ("contacts", "get"): None,
        ("lists", "list"): True,
        ("lists", "get"): None,
        ("segments", "list"): True,
        ("segments", "get"): None,
        ("campaigns", "list"): True,
        ("singlesends", "list"): True,
        ("singlesends", "get"): None,
        ("templates", "list"): True,
        ("templates", "get"): None,
        ("singlesend_stats", "list"): True,
        ("bounces", "list"): True,
        ("blocks", "list"): True,
        ("spam_reports", "list"): True,
        ("invalid_emails", "list"): True,
        ("global_suppressions", "list"): True,
        ("suppression_groups", "list"): True,
        ("suppression_groups", "get"): None,
        ("suppression_group_members", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('contacts', 'get'): {'id': 'id'},
        ('lists', 'list'): {'page_size': 'page_size'},
        ('lists', 'get'): {'id': 'id'},
        ('segments', 'get'): {'segment_id': 'segment_id'},
        ('campaigns', 'list'): {'page_size': 'page_size'},
        ('singlesends', 'list'): {'page_size': 'page_size'},
        ('singlesends', 'get'): {'id': 'id'},
        ('templates', 'list'): {'generations': 'generations', 'page_size': 'page_size'},
        ('templates', 'get'): {'template_id': 'template_id'},
        ('singlesend_stats', 'list'): {'page_size': 'page_size'},
        ('bounces', 'list'): {'limit': 'limit', 'offset': 'offset'},
        ('blocks', 'list'): {'limit': 'limit', 'offset': 'offset'},
        ('spam_reports', 'list'): {'limit': 'limit', 'offset': 'offset'},
        ('invalid_emails', 'list'): {'limit': 'limit', 'offset': 'offset'},
        ('global_suppressions', 'list'): {'limit': 'limit', 'offset': 'offset'},
        ('suppression_groups', 'get'): {'group_id': 'group_id'},
        ('suppression_group_members', 'list'): {'limit': 'limit', 'offset': 'offset'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (SendgridAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: SendgridAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new sendgrid connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., SendgridAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = SendgridConnector(auth_config=SendgridAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = SendgridConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = SendgridConnector(
                auth_config=AirbyteAuthConfig(
                    customer_name="user-123",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789"
                )
            )
        """
        # Accept AirbyteAuthConfig from any vendored SDK version
        if (
            auth_config is not None
            and not isinstance(auth_config, AirbyteAuthConfig)
            and type(auth_config).__name__ == AirbyteAuthConfig.__name__
        ):
            auth_config = AirbyteAuthConfig(**auth_config.model_dump())

        # Validate auth_config type
        if auth_config is not None and not isinstance(auth_config, self._ACCEPTED_AUTH_TYPES):
            raise TypeError(
                f"Unsupported auth_config type: {type(auth_config).__name__}. "
                f"Expected one of: {', '.join(t.__name__ for t in self._ACCEPTED_AUTH_TYPES)}"
            )

        # Hosted mode: auth_config is AirbyteAuthConfig
        is_hosted = isinstance(auth_config, AirbyteAuthConfig)

        if is_hosted:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                customer_name=auth_config.customer_name,
                organization_id=auth_config.organization_id,
                connector_definition_id=str(SendgridConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or SendgridAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=SendgridConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.contacts = ContactsQuery(self)
        self.lists = ListsQuery(self)
        self.segments = SegmentsQuery(self)
        self.campaigns = CampaignsQuery(self)
        self.singlesends = SinglesendsQuery(self)
        self.templates = TemplatesQuery(self)
        self.singlesend_stats = SinglesendStatsQuery(self)
        self.bounces = BouncesQuery(self)
        self.blocks = BlocksQuery(self)
        self.spam_reports = SpamReportsQuery(self)
        self.invalid_emails = InvalidEmailsQuery(self)
        self.global_suppressions = GlobalSuppressionsQuery(self)
        self.suppression_groups = SuppressionGroupsQuery(self)
        self.suppression_group_members = SuppressionGroupMembersQuery(self)

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
        entity: Literal["lists"],
        action: Literal["list"],
        params: "ListsListParams"
    ) -> "ListsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["lists"],
        action: Literal["get"],
        params: "ListsGetParams"
    ) -> "List": ...

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
        entity: Literal["campaigns"],
        action: Literal["list"],
        params: "CampaignsListParams"
    ) -> "CampaignsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["singlesends"],
        action: Literal["list"],
        params: "SinglesendsListParams"
    ) -> "SinglesendsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["singlesends"],
        action: Literal["get"],
        params: "SinglesendsGetParams"
    ) -> "SingleSend": ...

    @overload
    async def execute(
        self,
        entity: Literal["templates"],
        action: Literal["list"],
        params: "TemplatesListParams"
    ) -> "TemplatesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["templates"],
        action: Literal["get"],
        params: "TemplatesGetParams"
    ) -> "Template": ...

    @overload
    async def execute(
        self,
        entity: Literal["singlesend_stats"],
        action: Literal["list"],
        params: "SinglesendStatsListParams"
    ) -> "SinglesendStatsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["bounces"],
        action: Literal["list"],
        params: "BouncesListParams"
    ) -> "BouncesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["blocks"],
        action: Literal["list"],
        params: "BlocksListParams"
    ) -> "BlocksListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["spam_reports"],
        action: Literal["list"],
        params: "SpamReportsListParams"
    ) -> "SpamReportsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["invalid_emails"],
        action: Literal["list"],
        params: "InvalidEmailsListParams"
    ) -> "InvalidEmailsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["global_suppressions"],
        action: Literal["list"],
        params: "GlobalSuppressionsListParams"
    ) -> "GlobalSuppressionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["suppression_groups"],
        action: Literal["list"],
        params: "SuppressionGroupsListParams"
    ) -> "SuppressionGroupsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["suppression_groups"],
        action: Literal["get"],
        params: "SuppressionGroupsGetParams"
    ) -> "SuppressionGroup": ...

    @overload
    async def execute(
        self,
        entity: Literal["suppression_group_members"],
        action: Literal["list"],
        params: "SuppressionGroupMembersListParams"
    ) -> "SuppressionGroupMembersListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> SendgridExecuteResult[Any] | SendgridExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any] | None = None
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
        resolved_params = dict(params) if params is not None else None
        if resolved_params:
            param_map = self._PARAM_MAP.get((entity, action), {})
            if param_map:
                resolved_params = {param_map.get(k, k): v for k, v in resolved_params.items()}

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            entity=entity,
            action=action,
            params=resolved_params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._ENVELOPE_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return SendgridExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return SendgridExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> SendgridCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            SendgridCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return SendgridCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return SendgridCheckResult(
                status="unhealthy",
                error=result.error or "Unknown error during health check",
            )

    # ===== INTROSPECTION METHODS =====

    @classmethod
    def tool_utils(
        cls,
        func: _F | None = None,
        *,
        update_docstring: bool = True,
        enable_hosted_mode_features: bool = True,
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
    ) -> _F | Callable[[_F], _F]:
        """
        Decorator that adds tool utilities like docstring augmentation and output limits.

        Usage:
            @mcp.tool()
            @SendgridConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @SendgridConnector.tool_utils(update_docstring=False, max_output_chars=None)
            async def execute(entity: str, action: str, params: dict):
                ...

        Args:
            update_docstring: When True, append connector capabilities to __doc__.
            enable_hosted_mode_features: When False, omit hosted-mode search sections from docstrings.
            max_output_chars: Max serialized output size before raising. Use None to disable.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    SendgridConnectorModel,
                    enable_hosted_mode_features=enable_hosted_mode_features,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            if inspect.iscoroutinefunction(inner):

                @wraps(inner)
                async def aw(*args: Any, **kwargs: Any) -> Any:
                    result = await inner(*args, **kwargs)
                    return _check_output_size(result, max_output_chars, inner.__name__)

                wrapped = aw
            else:

                @wraps(inner)
                def sw(*args: Any, **kwargs: Any) -> Any:
                    result = inner(*args, **kwargs)
                    return _check_output_size(result, max_output_chars, inner.__name__)

                wrapped = sw

            if update_docstring:
                wrapped.__doc__ = full_doc
            return wrapped  # type: ignore[return-value]

        if func is not None:
            return decorate(func)
        return decorate

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
        return describe_entities(SendgridConnectorModel)

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
            (e for e in SendgridConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in SendgridConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await SendgridConnector.create(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def create(
        cls,
        *,
        airbyte_config: AirbyteAuthConfig,
        auth_config: "SendgridAuthConfig",
        name: str | None = None,
        replication_config: "SendgridReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "SendgridConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            airbyte_config: Airbyte hosted auth config with client credentials and customer_name.
                Optionally include organization_id for multi-org request routing.
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + customer_name)
            replication_config: Typed replication settings.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).
            source_template_id: Source template ID. Required when organization has
                multiple source templates for this connector type.

        Returns:
            A SendgridConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await SendgridConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=SendgridAuthConfig(api_key="..."),
            )

            # With replication config (required for this connector):
            connector = await SendgridConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=SendgridAuthConfig(api_key="..."),
                replication_config=SendgridReplicationConfig(start_date="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        if not airbyte_config.customer_name:
            raise ValueError("airbyte_config.customer_name is required for create()")


        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient
        from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as _AirbyteAuthConfig

        client = AirbyteCloudClient(
            client_id=airbyte_config.airbyte_client_id,
            client_secret=airbyte_config.airbyte_client_secret,
            organization_id=airbyte_config.organization_id,
        )

        try:
            # Build credentials from auth_config (if provided)
            credentials = auth_config.model_dump(exclude_none=True) if auth_config else None
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {airbyte_config.customer_name}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(SendgridConnectorModel.id),
                customer_name=airbyte_config.customer_name,
                credentials=credentials,
                replication_config=replication_config_dict,
                source_template_id=source_template_id,
            )
        finally:
            await client.close()

        # Return connector configured with the new connector_id
        return cls(
            auth_config=_AirbyteAuthConfig(
                airbyte_client_id=airbyte_config.airbyte_client_id,
                airbyte_client_secret=airbyte_config.airbyte_client_secret,
                organization_id=airbyte_config.organization_id,
                connector_id=source_id,
            ),
        )




class ContactsQuery:
    """
    Query class for Contacts entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> ContactsListResult:
        """
        Returns a sample of contacts. Use the export endpoint for full lists.

        Returns:
            ContactsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "list", params)
        # Cast generic envelope to concrete typed result
        return ContactsListResult(
            data=result.data
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Contact:
        """
        Returns the full details and all fields for the specified contact.

        Args:
            id: The ID of the contact
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



    async def search(
        self,
        query: ContactsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ContactsSearchResult:
        """
        Search contacts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ContactsSearchFilter):
        - address_line_1: Address line 1
        - address_line_2: Address line 2
        - alternate_emails: Alternate email addresses
        - city: City
        - contact_id: Unique contact identifier used by Airbyte
        - country: Country
        - created_at: When the contact was created
        - custom_fields: Custom field values
        - email: Contact email address
        - facebook: Facebook ID
        - first_name: Contact first name
        - last_name: Contact last name
        - line: LINE ID
        - list_ids: IDs of lists the contact belongs to
        - phone_number: Phone number
        - postal_code: Postal code
        - state_province_region: State, province, or region
        - unique_name: Unique name for the contact
        - updated_at: When the contact was last updated
        - whatsapp: WhatsApp number

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ContactsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("contacts", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ContactsSearchResult(
            data=[
                ContactsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ListsQuery:
    """
    Query class for Lists entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        **kwargs
    ) -> ListsListResult:
        """
        Returns all marketing contact lists.

        Args:
            page_size: Maximum number of lists to return
            **kwargs: Additional parameters

        Returns:
            ListsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("lists", "list", params)
        # Cast generic envelope to concrete typed result
        return ListsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> List:
        """
        Returns a specific marketing list by ID.

        Args:
            id: The ID of the list
            **kwargs: Additional parameters

        Returns:
            List
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("lists", "get", params)
        return result



    async def search(
        self,
        query: ListsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ListsSearchResult:
        """
        Search lists records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ListsSearchFilter):
        - metadata: Metadata about the list resource
        - contact_count: Number of contacts in the list
        - id: Unique list identifier
        - name: Name of the list

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ListsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("lists", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ListsSearchResult(
            data=[
                ListsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SegmentsQuery:
    """
    Query class for Segments entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> SegmentsListResult:
        """
        Returns all segments (v2).

        Returns:
            SegmentsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segments", "list", params)
        # Cast generic envelope to concrete typed result
        return SegmentsListResult(
            data=result.data
        )



    async def get(
        self,
        segment_id: str,
        **kwargs
    ) -> Segment:
        """
        Returns a specific segment by ID.

        Args:
            segment_id: The ID of the segment
            **kwargs: Additional parameters

        Returns:
            Segment
        """
        params = {k: v for k, v in {
            "segment_id": segment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segments", "get", params)
        return result



    async def search(
        self,
        query: SegmentsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SegmentsSearchResult:
        """
        Search segments records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SegmentsSearchFilter):
        - contacts_count: Number of contacts in the segment
        - created_at: When the segment was created
        - id: Unique segment identifier
        - name: Segment name
        - next_sample_update: When the next sample update will occur
        - parent_list_ids: IDs of parent lists
        - query_version: Query version used
        - sample_updated_at: When the sample was last updated
        - status: Segment status details
        - updated_at: When the segment was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SegmentsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("segments", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SegmentsSearchResult(
            data=[
                SegmentsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CampaignsQuery:
    """
    Query class for Campaigns entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        **kwargs
    ) -> CampaignsListResult:
        """
        Returns all marketing campaigns.

        Args:
            page_size: Maximum number of campaigns to return per page
            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: CampaignsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CampaignsSearchResult:
        """
        Search campaigns records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CampaignsSearchFilter):
        - channels: Channels for this campaign
        - created_at: When the campaign was created
        - id: Unique campaign identifier
        - is_abtest: Whether this campaign is an A/B test
        - name: Campaign name
        - status: Campaign status
        - updated_at: When the campaign was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CampaignsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("campaigns", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CampaignsSearchResult(
            data=[
                CampaignsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SinglesendsQuery:
    """
    Query class for Singlesends entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        **kwargs
    ) -> SinglesendsListResult:
        """
        Returns all single sends.

        Args:
            page_size: Maximum number of single sends to return per page
            **kwargs: Additional parameters

        Returns:
            SinglesendsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("singlesends", "list", params)
        # Cast generic envelope to concrete typed result
        return SinglesendsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> SingleSend:
        """
        Returns details about one single send.

        Args:
            id: The ID of the single send
            **kwargs: Additional parameters

        Returns:
            SingleSend
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("singlesends", "get", params)
        return result



    async def search(
        self,
        query: SinglesendsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SinglesendsSearchResult:
        """
        Search singlesends records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SinglesendsSearchFilter):
        - categories: Categories associated with this single send
        - created_at: When the single send was created
        - id: Unique single send identifier
        - is_abtest: Whether this is an A/B test
        - name: Single send name
        - send_at: Scheduled send time
        - status: Current status: draft, scheduled, or triggered
        - updated_at: When the single send was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SinglesendsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("singlesends", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SinglesendsSearchResult(
            data=[
                SinglesendsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TemplatesQuery:
    """
    Query class for Templates entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        generations: str | None = None,
        page_size: int | None = None,
        **kwargs
    ) -> TemplatesListResult:
        """
        Returns paged transactional templates (legacy and dynamic).

        Args:
            generations: Template generations to return
            page_size: Number of templates per page
            **kwargs: Additional parameters

        Returns:
            TemplatesListResult
        """
        params = {k: v for k, v in {
            "generations": generations,
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("templates", "list", params)
        # Cast generic envelope to concrete typed result
        return TemplatesListResult(
            data=result.data
        )



    async def get(
        self,
        template_id: str,
        **kwargs
    ) -> Template:
        """
        Returns a single transactional template.

        Args:
            template_id: The ID of the template
            **kwargs: Additional parameters

        Returns:
            Template
        """
        params = {k: v for k, v in {
            "template_id": template_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("templates", "get", params)
        return result



    async def search(
        self,
        query: TemplatesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TemplatesSearchResult:
        """
        Search templates records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TemplatesSearchFilter):
        - generation: Template generation (legacy or dynamic)
        - id: Unique template identifier
        - name: Template name
        - updated_at: When the template was last updated
        - versions: Template versions

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TemplatesSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("templates", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TemplatesSearchResult(
            data=[
                TemplatesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SinglesendStatsQuery:
    """
    Query class for SinglesendStats entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        **kwargs
    ) -> SinglesendStatsListResult:
        """
        Returns stats for all single sends.

        Args:
            page_size: Maximum number of stats to return per page
            **kwargs: Additional parameters

        Returns:
            SinglesendStatsListResult
        """
        params = {k: v for k, v in {
            "page_size": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("singlesend_stats", "list", params)
        # Cast generic envelope to concrete typed result
        return SinglesendStatsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: SinglesendStatsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SinglesendStatsSearchResult:
        """
        Search singlesend_stats records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SinglesendStatsSearchFilter):
        - ab_phase: The A/B test phase
        - ab_variation: The A/B test variation
        - aggregation: The aggregation type
        - id: The single send ID
        - stats: Email statistics for the single send

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SinglesendStatsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("singlesend_stats", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SinglesendStatsSearchResult(
            data=[
                SinglesendStatsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class BouncesQuery:
    """
    Query class for Bounces entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs
    ) -> BouncesListResult:
        """
        Returns all bounced email records.

        Args:
            limit: Number of records to return
            offset: Number of records to skip for pagination
            **kwargs: Additional parameters

        Returns:
            BouncesListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("bounces", "list", params)
        # Cast generic envelope to concrete typed result
        return BouncesListResult(
            data=result.data
        )



    async def search(
        self,
        query: BouncesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BouncesSearchResult:
        """
        Search bounces records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BouncesSearchFilter):
        - created: Unix timestamp when the bounce occurred
        - email: The email address that bounced
        - reason: The reason for the bounce
        - status: The enhanced status code for the bounce

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BouncesSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("bounces", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return BouncesSearchResult(
            data=[
                BouncesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class BlocksQuery:
    """
    Query class for Blocks entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs
    ) -> BlocksListResult:
        """
        Returns all blocked email records.

        Args:
            limit: Number of records to return
            offset: Number of records to skip for pagination
            **kwargs: Additional parameters

        Returns:
            BlocksListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("blocks", "list", params)
        # Cast generic envelope to concrete typed result
        return BlocksListResult(
            data=result.data
        )



    async def search(
        self,
        query: BlocksSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> BlocksSearchResult:
        """
        Search blocks records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (BlocksSearchFilter):
        - created: Unix timestamp when the block occurred
        - email: The blocked email address
        - reason: The reason for the block
        - status: The status code for the block

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            BlocksSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("blocks", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return BlocksSearchResult(
            data=[
                BlocksSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SpamReportsQuery:
    """
    Query class for SpamReports entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs
    ) -> SpamReportsListResult:
        """
        Returns all spam report records.

        Args:
            limit: Number of records to return
            offset: Number of records to skip for pagination
            **kwargs: Additional parameters

        Returns:
            SpamReportsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("spam_reports", "list", params)
        # Cast generic envelope to concrete typed result
        return SpamReportsListResult(
            data=result.data
        )



class InvalidEmailsQuery:
    """
    Query class for InvalidEmails entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs
    ) -> InvalidEmailsListResult:
        """
        Returns all invalid email records.

        Args:
            limit: Number of records to return
            offset: Number of records to skip for pagination
            **kwargs: Additional parameters

        Returns:
            InvalidEmailsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("invalid_emails", "list", params)
        # Cast generic envelope to concrete typed result
        return InvalidEmailsListResult(
            data=result.data
        )



    async def search(
        self,
        query: InvalidEmailsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> InvalidEmailsSearchResult:
        """
        Search invalid_emails records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (InvalidEmailsSearchFilter):
        - created: Unix timestamp when the invalid email was recorded
        - email: The invalid email address
        - reason: The reason the email is invalid

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            InvalidEmailsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("invalid_emails", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return InvalidEmailsSearchResult(
            data=[
                InvalidEmailsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class GlobalSuppressionsQuery:
    """
    Query class for GlobalSuppressions entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs
    ) -> GlobalSuppressionsListResult:
        """
        Returns all globally unsubscribed email addresses.

        Args:
            limit: Number of records to return
            offset: Number of records to skip for pagination
            **kwargs: Additional parameters

        Returns:
            GlobalSuppressionsListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("global_suppressions", "list", params)
        # Cast generic envelope to concrete typed result
        return GlobalSuppressionsListResult(
            data=result.data
        )



    async def search(
        self,
        query: GlobalSuppressionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> GlobalSuppressionsSearchResult:
        """
        Search global_suppressions records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (GlobalSuppressionsSearchFilter):
        - created: Unix timestamp when the global suppression was created
        - email: The globally suppressed email address

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            GlobalSuppressionsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("global_suppressions", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return GlobalSuppressionsSearchResult(
            data=[
                GlobalSuppressionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SuppressionGroupsQuery:
    """
    Query class for SuppressionGroups entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        **kwargs
    ) -> SuppressionGroupsListResult:
        """
        Returns all suppression (unsubscribe) groups.

        Returns:
            SuppressionGroupsListResult
        """
        params = {k: v for k, v in {
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("suppression_groups", "list", params)
        # Cast generic envelope to concrete typed result
        return SuppressionGroupsListResult(
            data=result.data
        )



    async def get(
        self,
        group_id: str,
        **kwargs
    ) -> SuppressionGroup:
        """
        Returns information about a single suppression group.

        Args:
            group_id: The ID of the suppression group
            **kwargs: Additional parameters

        Returns:
            SuppressionGroup
        """
        params = {k: v for k, v in {
            "group_id": group_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("suppression_groups", "get", params)
        return result



    async def search(
        self,
        query: SuppressionGroupsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SuppressionGroupsSearchResult:
        """
        Search suppression_groups records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SuppressionGroupsSearchFilter):
        - description: Description of the suppression group
        - id: Unique suppression group identifier
        - is_default: Whether this is the default suppression group
        - name: Suppression group name
        - unsubscribes: Number of unsubscribes in this group

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SuppressionGroupsSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("suppression_groups", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SuppressionGroupsSearchResult(
            data=[
                SuppressionGroupsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class SuppressionGroupMembersQuery:
    """
    Query class for SuppressionGroupMembers entity operations.
    """

    def __init__(self, connector: SendgridConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs
    ) -> SuppressionGroupMembersListResult:
        """
        Returns all suppressions across all groups.

        Args:
            limit: Number of records to return
            offset: Number of records to skip for pagination
            **kwargs: Additional parameters

        Returns:
            SuppressionGroupMembersListResult
        """
        params = {k: v for k, v in {
            "limit": limit,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("suppression_group_members", "list", params)
        # Cast generic envelope to concrete typed result
        return SuppressionGroupMembersListResult(
            data=result.data
        )



    async def search(
        self,
        query: SuppressionGroupMembersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> SuppressionGroupMembersSearchResult:
        """
        Search suppression_group_members records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (SuppressionGroupMembersSearchFilter):
        - created_at: Unix timestamp when the suppression was created
        - email: The suppressed email address
        - group_id: ID of the suppression group
        - group_name: Name of the suppression group

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            SuppressionGroupMembersSearchResult with typed records, pagination metadata, and optional search metadata

        Raises:
            NotImplementedError: If called in local execution mode
        """
        params: dict[str, Any] = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor
        if fields is not None:
            params["fields"] = fields

        result = await self._connector.execute("suppression_group_members", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return SuppressionGroupMembersSearchResult(
            data=[
                SuppressionGroupMembersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
