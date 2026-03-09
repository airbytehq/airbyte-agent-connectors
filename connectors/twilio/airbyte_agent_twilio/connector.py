"""
Twilio connector.
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

from .connector_model import TwilioConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from ._vendored.connector_sdk.types import AirbyteHostedAuthConfig as AirbyteAuthConfig
from .types import (
    AccountsGetParams,
    AccountsListParams,
    AddressesGetParams,
    AddressesListParams,
    CallsGetParams,
    CallsListParams,
    ConferencesGetParams,
    ConferencesListParams,
    IncomingPhoneNumbersGetParams,
    IncomingPhoneNumbersListParams,
    MessagesGetParams,
    MessagesListParams,
    OutgoingCallerIdsGetParams,
    OutgoingCallerIdsListParams,
    QueuesGetParams,
    QueuesListParams,
    RecordingsGetParams,
    RecordingsListParams,
    TranscriptionsGetParams,
    TranscriptionsListParams,
    UsageRecordsListParams,
    AirbyteSearchParams,
    AccountsSearchFilter,
    AccountsSearchQuery,
    CallsSearchFilter,
    CallsSearchQuery,
    MessagesSearchFilter,
    MessagesSearchQuery,
    IncomingPhoneNumbersSearchFilter,
    IncomingPhoneNumbersSearchQuery,
    RecordingsSearchFilter,
    RecordingsSearchQuery,
    ConferencesSearchFilter,
    ConferencesSearchQuery,
    UsageRecordsSearchFilter,
    UsageRecordsSearchQuery,
    AddressesSearchFilter,
    AddressesSearchQuery,
    QueuesSearchFilter,
    QueuesSearchQuery,
    TranscriptionsSearchFilter,
    TranscriptionsSearchQuery,
    OutgoingCallerIdsSearchFilter,
    OutgoingCallerIdsSearchQuery,
)
from .models import TwilioAuthConfig
if TYPE_CHECKING:
    from .models import TwilioReplicationConfig

# Import response models and envelope models at runtime
from .models import (
    TwilioCheckResult,
    TwilioExecuteResult,
    TwilioExecuteResultWithMeta,
    AccountsListResult,
    CallsListResult,
    MessagesListResult,
    IncomingPhoneNumbersListResult,
    RecordingsListResult,
    ConferencesListResult,
    UsageRecordsListResult,
    AddressesListResult,
    QueuesListResult,
    TranscriptionsListResult,
    OutgoingCallerIdsListResult,
    Account,
    Address,
    Call,
    Conference,
    IncomingPhoneNumber,
    Message,
    OutgoingCallerId,
    Queue,
    Recording,
    Transcription,
    UsageRecord,
    AirbyteSearchMeta,
    AirbyteSearchResult,
    AccountsSearchData,
    AccountsSearchResult,
    CallsSearchData,
    CallsSearchResult,
    MessagesSearchData,
    MessagesSearchResult,
    IncomingPhoneNumbersSearchData,
    IncomingPhoneNumbersSearchResult,
    RecordingsSearchData,
    RecordingsSearchResult,
    ConferencesSearchData,
    ConferencesSearchResult,
    UsageRecordsSearchData,
    UsageRecordsSearchResult,
    AddressesSearchData,
    AddressesSearchResult,
    QueuesSearchData,
    QueuesSearchResult,
    TranscriptionsSearchData,
    TranscriptionsSearchResult,
    OutgoingCallerIdsSearchData,
    OutgoingCallerIdsSearchResult,
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




class TwilioConnector:
    """
    Type-safe Twilio API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "twilio"
    connector_version = "1.0.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("accounts", "list"): True,
        ("accounts", "get"): None,
        ("calls", "list"): True,
        ("calls", "get"): None,
        ("messages", "list"): True,
        ("messages", "get"): None,
        ("incoming_phone_numbers", "list"): True,
        ("incoming_phone_numbers", "get"): None,
        ("recordings", "list"): True,
        ("recordings", "get"): None,
        ("conferences", "list"): True,
        ("conferences", "get"): None,
        ("usage_records", "list"): True,
        ("addresses", "list"): True,
        ("addresses", "get"): None,
        ("queues", "list"): True,
        ("queues", "get"): None,
        ("transcriptions", "list"): True,
        ("transcriptions", "get"): None,
        ("outgoing_caller_ids", "list"): True,
        ("outgoing_caller_ids", "get"): None,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('accounts', 'list'): {'page_size': 'PageSize'},
        ('accounts', 'get'): {'sid': 'sid'},
        ('calls', 'list'): {'account_sid': 'AccountSid', 'page_size': 'PageSize'},
        ('calls', 'get'): {'account_sid': 'AccountSid', 'sid': 'sid'},
        ('messages', 'list'): {'account_sid': 'AccountSid', 'page_size': 'PageSize'},
        ('messages', 'get'): {'account_sid': 'AccountSid', 'sid': 'sid'},
        ('incoming_phone_numbers', 'list'): {'account_sid': 'AccountSid', 'page_size': 'PageSize'},
        ('incoming_phone_numbers', 'get'): {'account_sid': 'AccountSid', 'sid': 'sid'},
        ('recordings', 'list'): {'account_sid': 'AccountSid', 'page_size': 'PageSize'},
        ('recordings', 'get'): {'account_sid': 'AccountSid', 'sid': 'sid'},
        ('conferences', 'list'): {'account_sid': 'AccountSid', 'page_size': 'PageSize'},
        ('conferences', 'get'): {'account_sid': 'AccountSid', 'sid': 'sid'},
        ('usage_records', 'list'): {'account_sid': 'AccountSid', 'page_size': 'PageSize'},
        ('addresses', 'list'): {'account_sid': 'AccountSid', 'page_size': 'PageSize'},
        ('addresses', 'get'): {'account_sid': 'AccountSid', 'sid': 'sid'},
        ('queues', 'list'): {'account_sid': 'AccountSid', 'page_size': 'PageSize'},
        ('queues', 'get'): {'account_sid': 'AccountSid', 'sid': 'sid'},
        ('transcriptions', 'list'): {'account_sid': 'AccountSid', 'page_size': 'PageSize'},
        ('transcriptions', 'get'): {'account_sid': 'AccountSid', 'sid': 'sid'},
        ('outgoing_caller_ids', 'list'): {'account_sid': 'AccountSid', 'page_size': 'PageSize'},
        ('outgoing_caller_ids', 'get'): {'account_sid': 'AccountSid', 'sid': 'sid'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (TwilioAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: TwilioAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new twilio connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., TwilioAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `customer_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = TwilioConnector(auth_config=TwilioAuthConfig(account_sid="...", auth_token="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = TwilioConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by customer_name
            connector = TwilioConnector(
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
                connector_definition_id=str(TwilioConnectorModel.id),
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or TwilioAuthConfig for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=TwilioConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.accounts = AccountsQuery(self)
        self.calls = CallsQuery(self)
        self.messages = MessagesQuery(self)
        self.incoming_phone_numbers = IncomingPhoneNumbersQuery(self)
        self.recordings = RecordingsQuery(self)
        self.conferences = ConferencesQuery(self)
        self.usage_records = UsageRecordsQuery(self)
        self.addresses = AddressesQuery(self)
        self.queues = QueuesQuery(self)
        self.transcriptions = TranscriptionsQuery(self)
        self.outgoing_caller_ids = OutgoingCallerIdsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["list"],
        params: "AccountsListParams"
    ) -> "AccountsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["accounts"],
        action: Literal["get"],
        params: "AccountsGetParams"
    ) -> "Account": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls"],
        action: Literal["list"],
        params: "CallsListParams"
    ) -> "CallsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["calls"],
        action: Literal["get"],
        params: "CallsGetParams"
    ) -> "Call": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages"],
        action: Literal["list"],
        params: "MessagesListParams"
    ) -> "MessagesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["messages"],
        action: Literal["get"],
        params: "MessagesGetParams"
    ) -> "Message": ...

    @overload
    async def execute(
        self,
        entity: Literal["incoming_phone_numbers"],
        action: Literal["list"],
        params: "IncomingPhoneNumbersListParams"
    ) -> "IncomingPhoneNumbersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["incoming_phone_numbers"],
        action: Literal["get"],
        params: "IncomingPhoneNumbersGetParams"
    ) -> "IncomingPhoneNumber": ...

    @overload
    async def execute(
        self,
        entity: Literal["recordings"],
        action: Literal["list"],
        params: "RecordingsListParams"
    ) -> "RecordingsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["recordings"],
        action: Literal["get"],
        params: "RecordingsGetParams"
    ) -> "Recording": ...

    @overload
    async def execute(
        self,
        entity: Literal["conferences"],
        action: Literal["list"],
        params: "ConferencesListParams"
    ) -> "ConferencesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["conferences"],
        action: Literal["get"],
        params: "ConferencesGetParams"
    ) -> "Conference": ...

    @overload
    async def execute(
        self,
        entity: Literal["usage_records"],
        action: Literal["list"],
        params: "UsageRecordsListParams"
    ) -> "UsageRecordsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["addresses"],
        action: Literal["list"],
        params: "AddressesListParams"
    ) -> "AddressesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["addresses"],
        action: Literal["get"],
        params: "AddressesGetParams"
    ) -> "Address": ...

    @overload
    async def execute(
        self,
        entity: Literal["queues"],
        action: Literal["list"],
        params: "QueuesListParams"
    ) -> "QueuesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["queues"],
        action: Literal["get"],
        params: "QueuesGetParams"
    ) -> "Queue": ...

    @overload
    async def execute(
        self,
        entity: Literal["transcriptions"],
        action: Literal["list"],
        params: "TranscriptionsListParams"
    ) -> "TranscriptionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["transcriptions"],
        action: Literal["get"],
        params: "TranscriptionsGetParams"
    ) -> "Transcription": ...

    @overload
    async def execute(
        self,
        entity: Literal["outgoing_caller_ids"],
        action: Literal["list"],
        params: "OutgoingCallerIdsListParams"
    ) -> "OutgoingCallerIdsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["outgoing_caller_ids"],
        action: Literal["get"],
        params: "OutgoingCallerIdsGetParams"
    ) -> "OutgoingCallerId": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> TwilioExecuteResult[Any] | TwilioExecuteResultWithMeta[Any, Any] | Any: ...

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
                return TwilioExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return TwilioExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> TwilioCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            TwilioCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return TwilioCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return TwilioCheckResult(
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
            @TwilioConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @TwilioConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    TwilioConnectorModel,
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
        return describe_entities(TwilioConnectorModel)

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
            (e for e in TwilioConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in TwilioConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await TwilioConnector.create(...)
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
        auth_config: "TwilioAuthConfig",
        name: str | None = None,
        replication_config: "TwilioReplicationConfig" | None = None,
        source_template_id: str | None = None,
    ) -> "TwilioConnector":
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
            A TwilioConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await TwilioConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=TwilioAuthConfig(account_sid="...", auth_token="..."),
            )

            # With replication config (required for this connector):
            connector = await TwilioConnector.create(
                airbyte_config=AirbyteAuthConfig(
                    customer_name="my-workspace",
                    organization_id="00000000-0000-0000-0000-000000000123",
                    airbyte_client_id="client_abc",
                    airbyte_client_secret="secret_xyz",
                ),
                auth_config=TwilioAuthConfig(account_sid="...", auth_token="..."),
                replication_config=TwilioReplicationConfig(start_date="..."),
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
                connector_definition_id=str(TwilioConnectorModel.id),
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




class AccountsQuery:
    """
    Query class for Accounts entity operations.
    """

    def __init__(self, connector: TwilioConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        page_size: int | None = None,
        **kwargs
    ) -> AccountsListResult:
        """
        Returns a list of accounts associated with the authenticated account

        Args:
            page_size: Number of items to return per page
            **kwargs: Additional parameters

        Returns:
            AccountsListResult
        """
        params = {k: v for k, v in {
            "PageSize": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "list", params)
        # Cast generic envelope to concrete typed result
        return AccountsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        sid: str,
        **kwargs
    ) -> Account:
        """
        Get a single account by SID

        Args:
            sid: Account SID
            **kwargs: Additional parameters

        Returns:
            Account
        """
        params = {k: v for k, v in {
            "sid": sid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "get", params)
        return result



    async def search(
        self,
        query: AccountsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AccountsSearchResult:
        """
        Search accounts records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AccountsSearchFilter):
        - sid: The unique identifier for the account
        - friendly_name: A user-defined friendly name for the account
        - status: The current status of the account
        - type_: The type of the account
        - owner_account_sid: The SID of the owner account
        - date_created: The timestamp when the account was created
        - date_updated: The timestamp when the account was last updated
        - uri: The URI for accessing the account resource

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AccountsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("accounts", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AccountsSearchResult(
            data=[
                AccountsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class CallsQuery:
    """
    Query class for Calls entity operations.
    """

    def __init__(self, connector: TwilioConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_sid: str,
        page_size: int | None = None,
        **kwargs
    ) -> CallsListResult:
        """
        Returns a list of calls made to and from an account

        Args:
            account_sid: Account SID
            page_size: Number of items to return per page
            **kwargs: Additional parameters

        Returns:
            CallsListResult
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "PageSize": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls", "list", params)
        # Cast generic envelope to concrete typed result
        return CallsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        account_sid: str,
        sid: str,
        **kwargs
    ) -> Call:
        """
        Get a single call by SID

        Args:
            account_sid: Account SID
            sid: Call SID
            **kwargs: Additional parameters

        Returns:
            Call
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "sid": sid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("calls", "get", params)
        return result



    async def search(
        self,
        query: CallsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CallsSearchResult:
        """
        Search calls records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CallsSearchFilter):
        - sid: The unique identifier for the call
        - account_sid: The unique identifier for the account associated with the call
        - to: The phone number that received the call
        - from_: The phone number that made the call
        - status: The current status of the call
        - direction: The direction of the call (inbound or outbound)
        - duration: The duration of the call in seconds
        - price: The cost of the call
        - price_unit: The currency unit of the call cost
        - start_time: The date and time when the call started
        - end_time: The date and time when the call ended
        - date_created: The date and time when the call record was created
        - date_updated: The date and time when the call record was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CallsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("calls", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return CallsSearchResult(
            data=[
                CallsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class MessagesQuery:
    """
    Query class for Messages entity operations.
    """

    def __init__(self, connector: TwilioConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_sid: str,
        page_size: int | None = None,
        **kwargs
    ) -> MessagesListResult:
        """
        Returns a list of messages associated with an account

        Args:
            account_sid: Account SID
            page_size: Number of items to return per page
            **kwargs: Additional parameters

        Returns:
            MessagesListResult
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "PageSize": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages", "list", params)
        # Cast generic envelope to concrete typed result
        return MessagesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        account_sid: str,
        sid: str,
        **kwargs
    ) -> Message:
        """
        Get a single message by SID

        Args:
            account_sid: Account SID
            sid: Message SID
            **kwargs: Additional parameters

        Returns:
            Message
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "sid": sid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("messages", "get", params)
        return result



    async def search(
        self,
        query: MessagesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> MessagesSearchResult:
        """
        Search messages records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (MessagesSearchFilter):
        - sid: The unique identifier for this message
        - account_sid: The unique identifier for the account associated with this message
        - to: The phone number or recipient ID the message was sent to
        - from_: The phone number or sender ID that sent the message
        - body: The text body of the message
        - status: The status of the message
        - direction: The direction of the message
        - price: The cost of the message
        - price_unit: The currency unit used for pricing
        - date_created: The date and time when the message was created
        - date_sent: The date and time when the message was sent
        - error_code: The error code associated with the message if any
        - error_message: The error message description if the message failed
        - num_segments: The number of message segments
        - num_media: The number of media files included in the message

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            MessagesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("messages", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return MessagesSearchResult(
            data=[
                MessagesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class IncomingPhoneNumbersQuery:
    """
    Query class for IncomingPhoneNumbers entity operations.
    """

    def __init__(self, connector: TwilioConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_sid: str,
        page_size: int | None = None,
        **kwargs
    ) -> IncomingPhoneNumbersListResult:
        """
        Returns a list of incoming phone numbers for an account

        Args:
            account_sid: Account SID
            page_size: Number of items to return per page
            **kwargs: Additional parameters

        Returns:
            IncomingPhoneNumbersListResult
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "PageSize": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("incoming_phone_numbers", "list", params)
        # Cast generic envelope to concrete typed result
        return IncomingPhoneNumbersListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        account_sid: str,
        sid: str,
        **kwargs
    ) -> IncomingPhoneNumber:
        """
        Get a single incoming phone number by SID

        Args:
            account_sid: Account SID
            sid: Incoming phone number SID
            **kwargs: Additional parameters

        Returns:
            IncomingPhoneNumber
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "sid": sid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("incoming_phone_numbers", "get", params)
        return result



    async def search(
        self,
        query: IncomingPhoneNumbersSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> IncomingPhoneNumbersSearchResult:
        """
        Search incoming_phone_numbers records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (IncomingPhoneNumbersSearchFilter):
        - sid: The SID of this phone number
        - account_sid: The SID of the account that owns this phone number
        - phone_number: The phone number in E.164 format
        - friendly_name: A user-assigned friendly name for this phone number
        - status: Status of the phone number
        - capabilities: Capabilities of this phone number
        - date_created: When the phone number was created
        - date_updated: When the phone number was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            IncomingPhoneNumbersSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("incoming_phone_numbers", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return IncomingPhoneNumbersSearchResult(
            data=[
                IncomingPhoneNumbersSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class RecordingsQuery:
    """
    Query class for Recordings entity operations.
    """

    def __init__(self, connector: TwilioConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_sid: str,
        page_size: int | None = None,
        **kwargs
    ) -> RecordingsListResult:
        """
        Returns a list of recordings for an account

        Args:
            account_sid: Account SID
            page_size: Number of items to return per page
            **kwargs: Additional parameters

        Returns:
            RecordingsListResult
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "PageSize": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("recordings", "list", params)
        # Cast generic envelope to concrete typed result
        return RecordingsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        account_sid: str,
        sid: str,
        **kwargs
    ) -> Recording:
        """
        Get a single recording by SID

        Args:
            account_sid: Account SID
            sid: Recording SID
            **kwargs: Additional parameters

        Returns:
            Recording
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "sid": sid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("recordings", "get", params)
        return result



    async def search(
        self,
        query: RecordingsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> RecordingsSearchResult:
        """
        Search recordings records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (RecordingsSearchFilter):
        - sid: The unique identifier of the recording
        - account_sid: The account SID that owns the recording
        - call_sid: The SID of the associated call
        - duration: Duration in seconds
        - status: The status of the recording
        - channels: Number of audio channels
        - price: The cost of storing the recording
        - price_unit: The currency unit
        - date_created: When the recording was created
        - start_time: When the recording started

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            RecordingsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("recordings", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return RecordingsSearchResult(
            data=[
                RecordingsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class ConferencesQuery:
    """
    Query class for Conferences entity operations.
    """

    def __init__(self, connector: TwilioConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_sid: str,
        page_size: int | None = None,
        **kwargs
    ) -> ConferencesListResult:
        """
        Returns a list of conferences for an account

        Args:
            account_sid: Account SID
            page_size: Number of items to return per page
            **kwargs: Additional parameters

        Returns:
            ConferencesListResult
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "PageSize": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("conferences", "list", params)
        # Cast generic envelope to concrete typed result
        return ConferencesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        account_sid: str,
        sid: str,
        **kwargs
    ) -> Conference:
        """
        Get a single conference by SID

        Args:
            account_sid: Account SID
            sid: Conference SID
            **kwargs: Additional parameters

        Returns:
            Conference
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "sid": sid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("conferences", "get", params)
        return result



    async def search(
        self,
        query: ConferencesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ConferencesSearchResult:
        """
        Search conferences records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ConferencesSearchFilter):
        - sid: The unique identifier of the conference
        - account_sid: The account SID associated with the conference
        - friendly_name: A friendly name for the conference
        - status: The current status of the conference
        - region: The region where the conference is hosted
        - date_created: When the conference was created
        - date_updated: When the conference was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ConferencesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("conferences", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return ConferencesSearchResult(
            data=[
                ConferencesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class UsageRecordsQuery:
    """
    Query class for UsageRecords entity operations.
    """

    def __init__(self, connector: TwilioConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_sid: str,
        page_size: int | None = None,
        **kwargs
    ) -> UsageRecordsListResult:
        """
        Returns a list of usage records for an account

        Args:
            account_sid: Account SID
            page_size: Number of items to return per page
            **kwargs: Additional parameters

        Returns:
            UsageRecordsListResult
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "PageSize": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("usage_records", "list", params)
        # Cast generic envelope to concrete typed result
        return UsageRecordsListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: UsageRecordsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> UsageRecordsSearchResult:
        """
        Search usage_records records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (UsageRecordsSearchFilter):
        - account_sid: The account SID associated with this usage record
        - category: The usage category (calls, SMS, recordings, etc.)
        - description: A description of the usage record
        - usage: The total usage value
        - usage_unit: The unit of measurement for usage
        - count: The number of units consumed
        - count_unit: The unit of measurement for count
        - price: The total price for consumed units
        - price_unit: The currency unit
        - start_date: The start date of the usage period
        - end_date: The end date of the usage period

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            UsageRecordsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("usage_records", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return UsageRecordsSearchResult(
            data=[
                UsageRecordsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class AddressesQuery:
    """
    Query class for Addresses entity operations.
    """

    def __init__(self, connector: TwilioConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_sid: str,
        page_size: int | None = None,
        **kwargs
    ) -> AddressesListResult:
        """
        Returns a list of addresses for an account

        Args:
            account_sid: Account SID
            page_size: Number of items to return per page
            **kwargs: Additional parameters

        Returns:
            AddressesListResult
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "PageSize": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("addresses", "list", params)
        # Cast generic envelope to concrete typed result
        return AddressesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        account_sid: str,
        sid: str,
        **kwargs
    ) -> Address:
        """
        Get a single address by SID

        Args:
            account_sid: Account SID
            sid: Address SID
            **kwargs: Additional parameters

        Returns:
            Address
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "sid": sid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("addresses", "get", params)
        return result



    async def search(
        self,
        query: AddressesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> AddressesSearchResult:
        """
        Search addresses records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (AddressesSearchFilter):
        - sid: The unique identifier of the address
        - account_sid: The account SID associated with this address
        - customer_name: The customer name associated with this address
        - friendly_name: A friendly name for the address
        - street: The street address
        - city: The city of the address
        - region: The region or state
        - postal_code: The postal code
        - iso_country: The ISO 3166-1 alpha-2 country code
        - validated: Whether the address has been validated
        - verified: Whether the address has been verified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AddressesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("addresses", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return AddressesSearchResult(
            data=[
                AddressesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class QueuesQuery:
    """
    Query class for Queues entity operations.
    """

    def __init__(self, connector: TwilioConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_sid: str,
        page_size: int | None = None,
        **kwargs
    ) -> QueuesListResult:
        """
        Returns a list of queues for an account

        Args:
            account_sid: Account SID
            page_size: Number of items to return per page
            **kwargs: Additional parameters

        Returns:
            QueuesListResult
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "PageSize": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("queues", "list", params)
        # Cast generic envelope to concrete typed result
        return QueuesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        account_sid: str,
        sid: str,
        **kwargs
    ) -> Queue:
        """
        Get a single queue by SID

        Args:
            account_sid: Account SID
            sid: Queue SID
            **kwargs: Additional parameters

        Returns:
            Queue
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "sid": sid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("queues", "get", params)
        return result



    async def search(
        self,
        query: QueuesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> QueuesSearchResult:
        """
        Search queues records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (QueuesSearchFilter):
        - sid: The unique identifier for the queue
        - account_sid: The account SID that owns this queue
        - friendly_name: A friendly name for the queue
        - current_size: Current number of callers waiting
        - max_size: Maximum number of callers allowed
        - average_wait_time: Average wait time in seconds
        - date_created: When the queue was created
        - date_updated: When the queue was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            QueuesSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("queues", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return QueuesSearchResult(
            data=[
                QueuesSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class TranscriptionsQuery:
    """
    Query class for Transcriptions entity operations.
    """

    def __init__(self, connector: TwilioConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_sid: str,
        page_size: int | None = None,
        **kwargs
    ) -> TranscriptionsListResult:
        """
        Returns a list of transcriptions for an account

        Args:
            account_sid: Account SID
            page_size: Number of items to return per page
            **kwargs: Additional parameters

        Returns:
            TranscriptionsListResult
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "PageSize": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transcriptions", "list", params)
        # Cast generic envelope to concrete typed result
        return TranscriptionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        account_sid: str,
        sid: str,
        **kwargs
    ) -> Transcription:
        """
        Get a single transcription by SID

        Args:
            account_sid: Account SID
            sid: Transcription SID
            **kwargs: Additional parameters

        Returns:
            Transcription
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "sid": sid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("transcriptions", "get", params)
        return result



    async def search(
        self,
        query: TranscriptionsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TranscriptionsSearchResult:
        """
        Search transcriptions records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TranscriptionsSearchFilter):
        - sid: The unique identifier for the transcription
        - account_sid: The account SID
        - recording_sid: The SID of the associated recording
        - status: The status of the transcription
        - duration: Duration of the audio recording in seconds
        - price: The cost of the transcription
        - price_unit: The currency unit
        - date_created: When the transcription was created
        - date_updated: When the transcription was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TranscriptionsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("transcriptions", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return TranscriptionsSearchResult(
            data=[
                TranscriptionsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )

class OutgoingCallerIdsQuery:
    """
    Query class for OutgoingCallerIds entity operations.
    """

    def __init__(self, connector: TwilioConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        account_sid: str,
        page_size: int | None = None,
        **kwargs
    ) -> OutgoingCallerIdsListResult:
        """
        Returns a list of outgoing caller IDs for an account

        Args:
            account_sid: Account SID
            page_size: Number of items to return per page
            **kwargs: Additional parameters

        Returns:
            OutgoingCallerIdsListResult
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "PageSize": page_size,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("outgoing_caller_ids", "list", params)
        # Cast generic envelope to concrete typed result
        return OutgoingCallerIdsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        account_sid: str,
        sid: str,
        **kwargs
    ) -> OutgoingCallerId:
        """
        Get a single outgoing caller ID by SID

        Args:
            account_sid: Account SID
            sid: Outgoing caller ID SID
            **kwargs: Additional parameters

        Returns:
            OutgoingCallerId
        """
        params = {k: v for k, v in {
            "AccountSid": account_sid,
            "sid": sid,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("outgoing_caller_ids", "get", params)
        return result



    async def search(
        self,
        query: OutgoingCallerIdsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OutgoingCallerIdsSearchResult:
        """
        Search outgoing_caller_ids records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OutgoingCallerIdsSearchFilter):
        - sid: The unique identifier
        - account_sid: The account SID
        - phone_number: The phone number
        - friendly_name: A friendly name
        - date_created: When the outgoing caller ID was created
        - date_updated: When the outgoing caller ID was last updated

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's meta.cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OutgoingCallerIdsSearchResult with typed records, pagination metadata, and optional search metadata

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

        result = await self._connector.execute("outgoing_caller_ids", "search", params)

        # Parse response into typed result
        meta_data = result.get("meta")
        return OutgoingCallerIdsSearchResult(
            data=[
                OutgoingCallerIdsSearchData(**row)
                for row in result.get("data", [])
                if isinstance(row, dict)
            ],
            meta=AirbyteSearchMeta(
                has_more=meta_data.get("has_more", False) if isinstance(meta_data, dict) else False,
                cursor=meta_data.get("cursor") if isinstance(meta_data, dict) else None,
                took_ms=meta_data.get("took_ms") if isinstance(meta_data, dict) else None,
            ),
        )
