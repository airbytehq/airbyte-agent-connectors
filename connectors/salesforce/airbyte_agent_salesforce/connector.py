"""
Salesforce connector.
"""

from __future__ import annotations

import inspect
import json
import logging
from functools import wraps
from typing import TYPE_CHECKING, Any, Callable, Mapping, TypeVar, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .connector_model import SalesforceConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    AccountsApiSearchParams,
    AccountsGetParams,
    AccountsListParams,
    AttachmentsDownloadParams,
    AttachmentsGetParams,
    AttachmentsListParams,
    CampaignsApiSearchParams,
    CampaignsGetParams,
    CampaignsListParams,
    CasesApiSearchParams,
    CasesGetParams,
    CasesListParams,
    ContactsApiSearchParams,
    ContactsGetParams,
    ContactsListParams,
    ContentVersionsDownloadParams,
    ContentVersionsGetParams,
    ContentVersionsListParams,
    EventsApiSearchParams,
    EventsGetParams,
    EventsListParams,
    LeadsApiSearchParams,
    LeadsGetParams,
    LeadsListParams,
    NotesApiSearchParams,
    NotesGetParams,
    NotesListParams,
    OpportunitiesApiSearchParams,
    OpportunitiesGetParams,
    OpportunitiesListParams,
    QueryListParams,
    TasksApiSearchParams,
    TasksGetParams,
    TasksListParams,
    AirbyteSearchParams,
    AccountsSearchFilter,
    AccountsSearchQuery,
    ContactsSearchFilter,
    ContactsSearchQuery,
    LeadsSearchFilter,
    LeadsSearchQuery,
    OpportunitiesSearchFilter,
    OpportunitiesSearchQuery,
    TasksSearchFilter,
    TasksSearchQuery,
)
if TYPE_CHECKING:
    from .models import SalesforceAuthConfig

# Import response models and envelope models at runtime
from .models import (
    SalesforceCheckResult,
    SalesforceExecuteResult,
    SalesforceExecuteResultWithMeta,
    AccountsListResult,
    AccountsApiSearchResult,
    ContactsListResult,
    ContactsApiSearchResult,
    LeadsListResult,
    LeadsApiSearchResult,
    OpportunitiesListResult,
    OpportunitiesApiSearchResult,
    TasksListResult,
    TasksApiSearchResult,
    EventsListResult,
    EventsApiSearchResult,
    CampaignsListResult,
    CampaignsApiSearchResult,
    CasesListResult,
    CasesApiSearchResult,
    NotesListResult,
    NotesApiSearchResult,
    ContentVersionsListResult,
    AttachmentsListResult,
    QueryListResult,
    Account,
    Attachment,
    Campaign,
    Case,
    Contact,
    ContentVersion,
    Event,
    Lead,
    Note,
    Opportunity,
    SearchResult,
    Task,
    AirbyteSearchHit,
    AirbyteSearchResult,
    AccountsSearchData,
    AccountsSearchResult,
    ContactsSearchData,
    ContactsSearchResult,
    LeadsSearchData,
    LeadsSearchResult,
    OpportunitiesSearchData,
    OpportunitiesSearchResult,
    TasksSearchData,
    TasksSearchResult,
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




class SalesforceConnector:
    """
    Type-safe Salesforce API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "salesforce"
    connector_version = "1.0.8"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("accounts", "list"): True,
        ("accounts", "get"): None,
        ("accounts", "api_search"): True,
        ("contacts", "list"): True,
        ("contacts", "get"): None,
        ("contacts", "api_search"): True,
        ("leads", "list"): True,
        ("leads", "get"): None,
        ("leads", "api_search"): True,
        ("opportunities", "list"): True,
        ("opportunities", "get"): None,
        ("opportunities", "api_search"): True,
        ("tasks", "list"): True,
        ("tasks", "get"): None,
        ("tasks", "api_search"): True,
        ("events", "list"): True,
        ("events", "get"): None,
        ("events", "api_search"): True,
        ("campaigns", "list"): True,
        ("campaigns", "get"): None,
        ("campaigns", "api_search"): True,
        ("cases", "list"): True,
        ("cases", "get"): None,
        ("cases", "api_search"): True,
        ("notes", "list"): True,
        ("notes", "get"): None,
        ("notes", "api_search"): True,
        ("content_versions", "list"): True,
        ("content_versions", "get"): None,
        ("content_versions", "download"): None,
        ("attachments", "list"): True,
        ("attachments", "get"): None,
        ("attachments", "download"): None,
        ("query", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('accounts', 'list'): {'q': 'q'},
        ('accounts', 'get'): {'id': 'id', 'fields': 'fields'},
        ('accounts', 'api_search'): {'q': 'q'},
        ('contacts', 'list'): {'q': 'q'},
        ('contacts', 'get'): {'id': 'id', 'fields': 'fields'},
        ('contacts', 'api_search'): {'q': 'q'},
        ('leads', 'list'): {'q': 'q'},
        ('leads', 'get'): {'id': 'id', 'fields': 'fields'},
        ('leads', 'api_search'): {'q': 'q'},
        ('opportunities', 'list'): {'q': 'q'},
        ('opportunities', 'get'): {'id': 'id', 'fields': 'fields'},
        ('opportunities', 'api_search'): {'q': 'q'},
        ('tasks', 'list'): {'q': 'q'},
        ('tasks', 'get'): {'id': 'id', 'fields': 'fields'},
        ('tasks', 'api_search'): {'q': 'q'},
        ('events', 'list'): {'q': 'q'},
        ('events', 'get'): {'id': 'id', 'fields': 'fields'},
        ('events', 'api_search'): {'q': 'q'},
        ('campaigns', 'list'): {'q': 'q'},
        ('campaigns', 'get'): {'id': 'id', 'fields': 'fields'},
        ('campaigns', 'api_search'): {'q': 'q'},
        ('cases', 'list'): {'q': 'q'},
        ('cases', 'get'): {'id': 'id', 'fields': 'fields'},
        ('cases', 'api_search'): {'q': 'q'},
        ('notes', 'list'): {'q': 'q'},
        ('notes', 'get'): {'id': 'id', 'fields': 'fields'},
        ('notes', 'api_search'): {'q': 'q'},
        ('content_versions', 'list'): {'q': 'q'},
        ('content_versions', 'get'): {'id': 'id', 'fields': 'fields'},
        ('content_versions', 'download'): {'id': 'id', 'range_header': 'range_header'},
        ('attachments', 'list'): {'q': 'q'},
        ('attachments', 'get'): {'id': 'id', 'fields': 'fields'},
        ('attachments', 'download'): {'id': 'id', 'range_header': 'range_header'},
        ('query', 'list'): {'q': 'q'},
    }

    def __init__(
        self,
        auth_config: SalesforceAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        connector_id: str | None = None,
        on_token_refresh: Any | None = None,
        instance_url: str | None = None    ):
        """
        Initialize a new salesforce connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `auth_config` for direct API calls
        - Hosted mode: Provide Airbyte credentials with either `connector_id` or `external_user_id`

        Args:
            auth_config: Typed authentication configuration (required for local mode)
            external_user_id: External user ID (for hosted mode lookup)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
            connector_id: Specific connector/source ID (for hosted mode, skips lookup)
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)            instance_url: Your Salesforce instance URL (e.g., https://na1.salesforce.com)
        Examples:
            # Local mode (direct API calls)
            connector = SalesforceConnector(auth_config=SalesforceAuthConfig(refresh_token="...", client_id="...", client_secret="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = SalesforceConnector(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid"
            )

            # Hosted mode with lookup by external_user_id
            connector = SalesforceConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = SalesforceConnector(
                auth_config=SalesforceAuthConfig(access_token="...", refresh_token="..."),
                on_token_refresh=save_tokens
            )
        """
        # Hosted mode: Airbyte credentials + either connector_id OR external_user_id
        is_hosted = airbyte_client_id and airbyte_client_secret and (connector_id or external_user_id)

        if is_hosted:
            from ._vendored.connector_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                connector_id=connector_id,
                external_user_id=external_user_id,
                connector_definition_id=str(SalesforceConnectorModel.id) if not connector_id else None,
            )
        else:
            # Local mode: auth_config required
            if not auth_config:
                raise ValueError(
                    "Either provide Airbyte credentials (airbyte_client_id, airbyte_client_secret) with "
                    "connector_id or external_user_id for hosted mode, or auth_config for local mode"
                )

            from ._vendored.connector_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values: dict[str, str] = {}
            if instance_url:
                config_values["instance_url"] = instance_url

            self._executor = LocalExecutor(
                model=SalesforceConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if instance_url:
                base_url = base_url.replace("{instance_url}", instance_url)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.accounts = AccountsQuery(self)
        self.contacts = ContactsQuery(self)
        self.leads = LeadsQuery(self)
        self.opportunities = OpportunitiesQuery(self)
        self.tasks = TasksQuery(self)
        self.events = EventsQuery(self)
        self.campaigns = CampaignsQuery(self)
        self.cases = CasesQuery(self)
        self.notes = NotesQuery(self)
        self.content_versions = ContentVersionsQuery(self)
        self.attachments = AttachmentsQuery(self)
        self.query = QueryQuery(self)

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
        entity: Literal["accounts"],
        action: Literal["api_search"],
        params: "AccountsApiSearchParams"
    ) -> "AccountsApiSearchResult": ...

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
        entity: Literal["contacts"],
        action: Literal["api_search"],
        params: "ContactsApiSearchParams"
    ) -> "ContactsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["list"],
        params: "LeadsListParams"
    ) -> "LeadsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["get"],
        params: "LeadsGetParams"
    ) -> "Lead": ...

    @overload
    async def execute(
        self,
        entity: Literal["leads"],
        action: Literal["api_search"],
        params: "LeadsApiSearchParams"
    ) -> "LeadsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunities"],
        action: Literal["list"],
        params: "OpportunitiesListParams"
    ) -> "OpportunitiesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunities"],
        action: Literal["get"],
        params: "OpportunitiesGetParams"
    ) -> "Opportunity": ...

    @overload
    async def execute(
        self,
        entity: Literal["opportunities"],
        action: Literal["api_search"],
        params: "OpportunitiesApiSearchParams"
    ) -> "OpportunitiesApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["list"],
        params: "TasksListParams"
    ) -> "TasksListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["get"],
        params: "TasksGetParams"
    ) -> "Task": ...

    @overload
    async def execute(
        self,
        entity: Literal["tasks"],
        action: Literal["api_search"],
        params: "TasksApiSearchParams"
    ) -> "TasksApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["list"],
        params: "EventsListParams"
    ) -> "EventsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["get"],
        params: "EventsGetParams"
    ) -> "Event": ...

    @overload
    async def execute(
        self,
        entity: Literal["events"],
        action: Literal["api_search"],
        params: "EventsApiSearchParams"
    ) -> "EventsApiSearchResult": ...

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
        entity: Literal["campaigns"],
        action: Literal["get"],
        params: "CampaignsGetParams"
    ) -> "Campaign": ...

    @overload
    async def execute(
        self,
        entity: Literal["campaigns"],
        action: Literal["api_search"],
        params: "CampaignsApiSearchParams"
    ) -> "CampaignsApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["cases"],
        action: Literal["list"],
        params: "CasesListParams"
    ) -> "CasesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["cases"],
        action: Literal["get"],
        params: "CasesGetParams"
    ) -> "Case": ...

    @overload
    async def execute(
        self,
        entity: Literal["cases"],
        action: Literal["api_search"],
        params: "CasesApiSearchParams"
    ) -> "CasesApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["list"],
        params: "NotesListParams"
    ) -> "NotesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["get"],
        params: "NotesGetParams"
    ) -> "Note": ...

    @overload
    async def execute(
        self,
        entity: Literal["notes"],
        action: Literal["api_search"],
        params: "NotesApiSearchParams"
    ) -> "NotesApiSearchResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["content_versions"],
        action: Literal["list"],
        params: "ContentVersionsListParams"
    ) -> "ContentVersionsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["content_versions"],
        action: Literal["get"],
        params: "ContentVersionsGetParams"
    ) -> "ContentVersion": ...

    @overload
    async def execute(
        self,
        entity: Literal["content_versions"],
        action: Literal["download"],
        params: "ContentVersionsDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["list"],
        params: "AttachmentsListParams"
    ) -> "AttachmentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["get"],
        params: "AttachmentsGetParams"
    ) -> "Attachment": ...

    @overload
    async def execute(
        self,
        entity: Literal["attachments"],
        action: Literal["download"],
        params: "AttachmentsDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["query"],
        action: Literal["list"],
        params: "QueryListParams"
    ) -> "QueryListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "api_search", "download", "search"],
        params: Mapping[str, Any]
    ) -> SalesforceExecuteResult[Any] | SalesforceExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "api_search", "download", "search"],
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
                return SalesforceExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return SalesforceExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> SalesforceCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            SalesforceCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return SalesforceCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return SalesforceCheckResult(
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
            @SalesforceConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @SalesforceConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    SalesforceConnectorModel,
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
        return describe_entities(SalesforceConnectorModel)

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
            (e for e in SalesforceConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in SalesforceConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await SalesforceConnector.create_hosted(...)
            print(f"Created connector: {connector.connector_id}")
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== HOSTED MODE FACTORY =====

    @classmethod
    async def create_hosted(
        cls,
        *,
        external_user_id: str,
        airbyte_client_id: str,
        airbyte_client_secret: str,
        auth_config: "SalesforceAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
    ) -> "SalesforceConnector":
        """
        Create a new hosted connector on Airbyte Cloud.

        This factory method:
        1. Creates a source on Airbyte Cloud with the provided credentials
        2. Returns a connector configured with the new connector_id

        Args:
            external_user_id: Workspace identifier in Airbyte Cloud
            airbyte_client_id: Airbyte OAuth client ID
            airbyte_client_secret: Airbyte OAuth client secret
            auth_config: Typed auth config (same as local mode)
            name: Optional source name (defaults to connector name + external_user_id)
            replication_config: Optional replication settings dict.
                Required for connectors with x-airbyte-replication-config (REPLICATION mode sources).

        Returns:
            A SalesforceConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await SalesforceConnector.create_hosted(
                external_user_id="my-workspace",
                airbyte_client_id="client_abc",
                airbyte_client_secret="secret_xyz",
                auth_config=SalesforceAuthConfig(refresh_token="...", client_id="...", client_secret="..."),
            )

            # Use the connector
            result = await connector.execute("entity", "list", {})
        """
        from ._vendored.connector_sdk.cloud_utils import AirbyteCloudClient

        client = AirbyteCloudClient(
            client_id=airbyte_client_id,
            client_secret=airbyte_client_secret,
        )

        try:
            # Build credentials from auth_config
            credentials = auth_config.model_dump(exclude_none=True)
            replication_config_dict = replication_config.model_dump(exclude_none=True) if replication_config else None

            # Create source on Airbyte Cloud
            source_name = name or f"{cls.connector_name} - {external_user_id}"
            source_id = await client.create_source(
                name=source_name,
                connector_definition_id=str(SalesforceConnectorModel.id),
                external_user_id=external_user_id,
                credentials=credentials,
                replication_config=replication_config_dict,
            )
        finally:
            await client.close()

        # Return connector configured with the new connector_id
        return cls(
            airbyte_client_id=airbyte_client_id,
            airbyte_client_secret=airbyte_client_secret,
            connector_id=source_id,
        )



class AccountsQuery:
    """
    Query class for Accounts entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> AccountsListResult:
        """
        Returns a list of accounts via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for accounts. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Account ORDER BY LastModifiedDate DESC LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            AccountsListResult
        """
        params = {k: v for k, v in {
            "q": q,
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
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Account:
        """
        Get a single account by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Account ID (18-character ID starting with '001')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,Industry,AnnualRevenue,Website"

            **kwargs: Additional parameters

        Returns:
            Account
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "get", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> AccountsApiSearchResult:
        """
        Search for accounts using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields and objects.
Use SOQL (list action) for structured queries with specific field conditions.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} IN scope RETURNING Object(fields) [LIMIT n]
Examples:
- "FIND {Acme} IN ALL FIELDS RETURNING Account(Id,Name)"
- "FIND {tech*} IN NAME FIELDS RETURNING Account(Id,Name,Industry) LIMIT 50"
- "FIND {\"exact phrase\"} RETURNING Account(Id,Name,Website)"

            **kwargs: Additional parameters

        Returns:
            AccountsApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("accounts", "api_search", params)
        # Cast generic envelope to concrete typed result
        return AccountsApiSearchResult(
            data=result.data
        )



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
        - id: Unique identifier for the account record
        - name: Name of the account or company
        - account_source: Source of the account record (e.g., Web, Referral)
        - billing_address: Complete billing address as a compound field
        - billing_city: City portion of the billing address
        - billing_country: Country portion of the billing address
        - billing_postal_code: Postal code portion of the billing address
        - billing_state: State or province portion of the billing address
        - billing_street: Street address portion of the billing address
        - created_by_id: ID of the user who created this account
        - created_date: Date and time when the account was created
        - description: Text description of the account
        - industry: Primary business industry of the account
        - is_deleted: Whether the account has been moved to the Recycle Bin
        - last_activity_date: Date of the last activity associated with this account
        - last_modified_by_id: ID of the user who last modified this account
        - last_modified_date: Date and time when the account was last modified
        - number_of_employees: Number of employees at the account
        - owner_id: ID of the user who owns this account
        - parent_id: ID of the parent account, if this is a subsidiary
        - phone: Primary phone number for the account
        - shipping_address: Complete shipping address as a compound field
        - shipping_city: City portion of the shipping address
        - shipping_country: Country portion of the shipping address
        - shipping_postal_code: Postal code portion of the shipping address
        - shipping_state: State or province portion of the shipping address
        - shipping_street: Street address portion of the shipping address
        - type: Type of account (e.g., Customer, Partner, Competitor)
        - website: Website URL for the account
        - system_modstamp: System timestamp when the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            AccountsSearchResult with hits (list of AirbyteSearchHit[AccountsSearchData]) and pagination info

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
        return AccountsSearchResult(
            hits=[
                AirbyteSearchHit[AccountsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=AccountsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class ContactsQuery:
    """
    Query class for Contacts entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> ContactsListResult:
        """
        Returns a list of contacts via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for contacts. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Contact WHERE AccountId = '001xx...' LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            ContactsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "list", params)
        # Cast generic envelope to concrete typed result
        return ContactsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Contact:
        """
        Get a single contact by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Contact ID (18-character ID starting with '003')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,FirstName,LastName,Email,Phone,AccountId"

            **kwargs: Additional parameters

        Returns:
            Contact
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "get", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> ContactsApiSearchResult:
        """
        Search for contacts using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Contact(fields) [LIMIT n]
Examples:
- "FIND {John} IN NAME FIELDS RETURNING Contact(Id,FirstName,LastName,Email)"
- "FIND {*@example.com} IN EMAIL FIELDS RETURNING Contact(Id,Name,Email) LIMIT 25"

            **kwargs: Additional parameters

        Returns:
            ContactsApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contacts", "api_search", params)
        # Cast generic envelope to concrete typed result
        return ContactsApiSearchResult(
            data=result.data
        )



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
        - id: Unique identifier for the contact record
        - account_id: ID of the account this contact is associated with
        - created_by_id: ID of the user who created this contact
        - created_date: Date and time when the contact was created
        - department: Department within the account where the contact works
        - email: Email address of the contact
        - first_name: First name of the contact
        - is_deleted: Whether the contact has been moved to the Recycle Bin
        - last_activity_date: Date of the last activity associated with this contact
        - last_modified_by_id: ID of the user who last modified this contact
        - last_modified_date: Date and time when the contact was last modified
        - last_name: Last name of the contact
        - lead_source: Source from which this contact originated
        - mailing_address: Complete mailing address as a compound field
        - mailing_city: City portion of the mailing address
        - mailing_country: Country portion of the mailing address
        - mailing_postal_code: Postal code portion of the mailing address
        - mailing_state: State or province portion of the mailing address
        - mailing_street: Street address portion of the mailing address
        - mobile_phone: Mobile phone number of the contact
        - name: Full name of the contact (read-only, concatenation of first and last name)
        - owner_id: ID of the user who owns this contact
        - phone: Business phone number of the contact
        - reports_to_id: ID of the contact this contact reports to
        - title: Job title of the contact
        - system_modstamp: System timestamp when the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ContactsSearchResult with hits (list of AirbyteSearchHit[ContactsSearchData]) and pagination info

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
        return ContactsSearchResult(
            hits=[
                AirbyteSearchHit[ContactsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ContactsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class LeadsQuery:
    """
    Query class for Leads entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> LeadsListResult:
        """
        Returns a list of leads via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for leads. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Lead WHERE Status = 'Open' LIMIT 100"

            **kwargs: Additional parameters

        Returns:
            LeadsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "list", params)
        # Cast generic envelope to concrete typed result
        return LeadsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Lead:
        """
        Get a single lead by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Lead ID (18-character ID starting with '00Q')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,FirstName,LastName,Email,Company,Status,LeadSource"

            **kwargs: Additional parameters

        Returns:
            Lead
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "get", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> LeadsApiSearchResult:
        """
        Search for leads using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Lead(fields) [LIMIT n]
Examples:
- "FIND {Smith} IN NAME FIELDS RETURNING Lead(Id,FirstName,LastName,Company,Status)"
- "FIND {marketing} IN ALL FIELDS RETURNING Lead(Id,Name,LeadSource) LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            LeadsApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("leads", "api_search", params)
        # Cast generic envelope to concrete typed result
        return LeadsApiSearchResult(
            data=result.data
        )



    async def search(
        self,
        query: LeadsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> LeadsSearchResult:
        """
        Search leads records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (LeadsSearchFilter):
        - id: Unique identifier for the lead record
        - address: Complete address as a compound field
        - city: City portion of the address
        - company: Company or organization the lead works for
        - converted_account_id: ID of the account created when lead was converted
        - converted_contact_id: ID of the contact created when lead was converted
        - converted_date: Date when the lead was converted
        - converted_opportunity_id: ID of the opportunity created when lead was converted
        - country: Country portion of the address
        - created_by_id: ID of the user who created this lead
        - created_date: Date and time when the lead was created
        - email: Email address of the lead
        - first_name: First name of the lead
        - industry: Industry the lead's company operates in
        - is_converted: Whether the lead has been converted to an account, contact, and opportunity
        - is_deleted: Whether the lead has been moved to the Recycle Bin
        - last_activity_date: Date of the last activity associated with this lead
        - last_modified_by_id: ID of the user who last modified this lead
        - last_modified_date: Date and time when the lead was last modified
        - last_name: Last name of the lead
        - lead_source: Source from which this lead originated
        - mobile_phone: Mobile phone number of the lead
        - name: Full name of the lead (read-only, concatenation of first and last name)
        - number_of_employees: Number of employees at the lead's company
        - owner_id: ID of the user who owns this lead
        - phone: Phone number of the lead
        - postal_code: Postal code portion of the address
        - rating: Rating of the lead (e.g., Hot, Warm, Cold)
        - state: State or province portion of the address
        - status: Current status of the lead in the sales process
        - street: Street address portion of the address
        - title: Job title of the lead
        - website: Website URL for the lead's company
        - system_modstamp: System timestamp when the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            LeadsSearchResult with hits (list of AirbyteSearchHit[LeadsSearchData]) and pagination info

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

        result = await self._connector.execute("leads", "search", params)

        # Parse response into typed result
        return LeadsSearchResult(
            hits=[
                AirbyteSearchHit[LeadsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=LeadsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class OpportunitiesQuery:
    """
    Query class for Opportunities entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> OpportunitiesListResult:
        """
        Returns a list of opportunities via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for opportunities. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Opportunity WHERE StageName = 'Closed Won' LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            OpportunitiesListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunities", "list", params)
        # Cast generic envelope to concrete typed result
        return OpportunitiesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Opportunity:
        """
        Get a single opportunity by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Opportunity ID (18-character ID starting with '006')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,Amount,StageName,CloseDate,AccountId"

            **kwargs: Additional parameters

        Returns:
            Opportunity
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunities", "get", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> OpportunitiesApiSearchResult:
        """
        Search for opportunities using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Opportunity(fields) [LIMIT n]
Examples:
- "FIND {Enterprise} IN NAME FIELDS RETURNING Opportunity(Id,Name,Amount,StageName)"
- "FIND {renewal} IN ALL FIELDS RETURNING Opportunity(Id,Name,CloseDate) LIMIT 25"

            **kwargs: Additional parameters

        Returns:
            OpportunitiesApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("opportunities", "api_search", params)
        # Cast generic envelope to concrete typed result
        return OpportunitiesApiSearchResult(
            data=result.data
        )



    async def search(
        self,
        query: OpportunitiesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> OpportunitiesSearchResult:
        """
        Search opportunities records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (OpportunitiesSearchFilter):
        - id: Unique identifier for the opportunity record
        - account_id: ID of the account associated with this opportunity
        - amount: Estimated total sale amount
        - campaign_id: ID of the campaign that generated this opportunity
        - close_date: Expected close date for the opportunity
        - contact_id: ID of the primary contact for this opportunity
        - created_by_id: ID of the user who created this opportunity
        - created_date: Date and time when the opportunity was created
        - description: Text description of the opportunity
        - expected_revenue: Expected revenue based on amount and probability
        - forecast_category: Forecast category for this opportunity
        - forecast_category_name: Name of the forecast category
        - is_closed: Whether the opportunity is closed
        - is_deleted: Whether the opportunity has been moved to the Recycle Bin
        - is_won: Whether the opportunity was won
        - last_activity_date: Date of the last activity associated with this opportunity
        - last_modified_by_id: ID of the user who last modified this opportunity
        - last_modified_date: Date and time when the opportunity was last modified
        - lead_source: Source from which this opportunity originated
        - name: Name of the opportunity
        - next_step: Description of the next step in closing the opportunity
        - owner_id: ID of the user who owns this opportunity
        - probability: Likelihood of closing the opportunity (percentage)
        - stage_name: Current stage of the opportunity in the sales process
        - type: Type of opportunity (e.g., New Business, Existing Business)
        - system_modstamp: System timestamp when the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            OpportunitiesSearchResult with hits (list of AirbyteSearchHit[OpportunitiesSearchData]) and pagination info

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

        result = await self._connector.execute("opportunities", "search", params)

        # Parse response into typed result
        return OpportunitiesSearchResult(
            hits=[
                AirbyteSearchHit[OpportunitiesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=OpportunitiesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class TasksQuery:
    """
    Query class for Tasks entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> TasksListResult:
        """
        Returns a list of tasks via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for tasks. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Task WHERE Status = 'Not Started' LIMIT 100"

            **kwargs: Additional parameters

        Returns:
            TasksListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "list", params)
        # Cast generic envelope to concrete typed result
        return TasksListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Task:
        """
        Get a single task by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Task ID (18-character ID starting with '00T')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Subject,Status,Priority,ActivityDate,WhoId,WhatId"

            **kwargs: Additional parameters

        Returns:
            Task
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "get", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> TasksApiSearchResult:
        """
        Search for tasks using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Task(fields) [LIMIT n]
Examples:
- "FIND {follow up} IN ALL FIELDS RETURNING Task(Id,Subject,Status,Priority)"
- "FIND {call} IN NAME FIELDS RETURNING Task(Id,Subject,ActivityDate) LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            TasksApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tasks", "api_search", params)
        # Cast generic envelope to concrete typed result
        return TasksApiSearchResult(
            data=result.data
        )



    async def search(
        self,
        query: TasksSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TasksSearchResult:
        """
        Search tasks records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TasksSearchFilter):
        - id: Unique identifier for the task record
        - account_id: ID of the account associated with this task
        - activity_date: Due date for the task
        - call_disposition: Result of the call, if this task represents a call
        - call_duration_in_seconds: Duration of the call in seconds
        - call_type: Type of call (Inbound, Outbound, Internal)
        - completed_date_time: Date and time when the task was completed
        - created_by_id: ID of the user who created this task
        - created_date: Date and time when the task was created
        - description: Text description or notes about the task
        - is_closed: Whether the task has been completed
        - is_deleted: Whether the task has been moved to the Recycle Bin
        - is_high_priority: Whether the task is marked as high priority
        - last_modified_by_id: ID of the user who last modified this task
        - last_modified_date: Date and time when the task was last modified
        - owner_id: ID of the user who owns this task
        - priority: Priority level of the task (High, Normal, Low)
        - status: Current status of the task
        - subject: Subject or title of the task
        - task_subtype: Subtype of the task (e.g., Call, Email, Task)
        - type: Type of task
        - what_id: ID of the related object (Account, Opportunity, etc.)
        - who_id: ID of the related person (Contact or Lead)
        - system_modstamp: System timestamp when the record was last modified

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TasksSearchResult with hits (list of AirbyteSearchHit[TasksSearchData]) and pagination info

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

        result = await self._connector.execute("tasks", "search", params)

        # Parse response into typed result
        return TasksSearchResult(
            hits=[
                AirbyteSearchHit[TasksSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TasksSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class EventsQuery:
    """
    Query class for Events entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> EventsListResult:
        """
        Returns a list of events via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for events. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Event WHERE StartDateTime > TODAY LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            EventsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "list", params)
        # Cast generic envelope to concrete typed result
        return EventsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Event:
        """
        Get a single event by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Event ID (18-character ID starting with '00U')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Subject,StartDateTime,EndDateTime,Location,WhoId,WhatId"

            **kwargs: Additional parameters

        Returns:
            Event
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "get", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> EventsApiSearchResult:
        """
        Search for events using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Event(fields) [LIMIT n]
Examples:
- "FIND {meeting} IN ALL FIELDS RETURNING Event(Id,Subject,StartDateTime,Location)"
- "FIND {demo} IN NAME FIELDS RETURNING Event(Id,Subject,EndDateTime) LIMIT 25"

            **kwargs: Additional parameters

        Returns:
            EventsApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("events", "api_search", params)
        # Cast generic envelope to concrete typed result
        return EventsApiSearchResult(
            data=result.data
        )



class CampaignsQuery:
    """
    Query class for Campaigns entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> CampaignsListResult:
        """
        Returns a list of campaigns via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for campaigns. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Campaign WHERE IsActive = true LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "list", params)
        # Cast generic envelope to concrete typed result
        return CampaignsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Campaign:
        """
        Get a single campaign by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Campaign ID (18-character ID starting with '701')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,Type,Status,StartDate,EndDate,IsActive"

            **kwargs: Additional parameters

        Returns:
            Campaign
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "get", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> CampaignsApiSearchResult:
        """
        Search for campaigns using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Campaign(fields) [LIMIT n]
Examples:
- "FIND {webinar} IN ALL FIELDS RETURNING Campaign(Id,Name,Type,Status)"
- "FIND {2024} IN NAME FIELDS RETURNING Campaign(Id,Name,StartDate,IsActive) LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            CampaignsApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "api_search", params)
        # Cast generic envelope to concrete typed result
        return CampaignsApiSearchResult(
            data=result.data
        )



class CasesQuery:
    """
    Query class for Cases entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> CasesListResult:
        """
        Returns a list of cases via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for cases. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Case WHERE Status = 'New' LIMIT 100"

            **kwargs: Additional parameters

        Returns:
            CasesListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cases", "list", params)
        # Cast generic envelope to concrete typed result
        return CasesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Case:
        """
        Get a single case by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Case ID (18-character ID starting with '500')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,CaseNumber,Subject,Status,Priority,ContactId,AccountId"

            **kwargs: Additional parameters

        Returns:
            Case
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cases", "get", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> CasesApiSearchResult:
        """
        Search for cases using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Case(fields) [LIMIT n]
Examples:
- "FIND {login issue} IN ALL FIELDS RETURNING Case(Id,CaseNumber,Subject,Status)"
- "FIND {urgent} IN NAME FIELDS RETURNING Case(Id,Subject,Priority) LIMIT 25"

            **kwargs: Additional parameters

        Returns:
            CasesApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("cases", "api_search", params)
        # Cast generic envelope to concrete typed result
        return CasesApiSearchResult(
            data=result.data
        )



class NotesQuery:
    """
    Query class for Notes entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> NotesListResult:
        """
        Returns a list of notes via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query for notes. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT FIELDS(STANDARD) FROM Note WHERE ParentId = '001xx...' LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            NotesListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "list", params)
        # Cast generic envelope to concrete typed result
        return NotesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Note:
        """
        Get a single note by ID. Returns all accessible fields by default.
Use the `fields` parameter to retrieve only specific fields for better performance.


        Args:
            id: Salesforce Note ID (18-character ID starting with '002')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Title,Body,ParentId,OwnerId"

            **kwargs: Additional parameters

        Returns:
            Note
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "get", params)
        return result



    async def api_search(
        self,
        q: str,
        **kwargs
    ) -> NotesApiSearchResult:
        """
        Search for notes using SOSL (Salesforce Object Search Language).
SOSL is optimized for text-based searches across multiple fields.


        Args:
            q: SOSL search query. Format: FIND {searchTerm} RETURNING Note(fields) [LIMIT n]
Examples:
- "FIND {important} IN ALL FIELDS RETURNING Note(Id,Title,ParentId)"
- "FIND {action items} IN NAME FIELDS RETURNING Note(Id,Title,Body) LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            NotesApiSearchResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("notes", "api_search", params)
        # Cast generic envelope to concrete typed result
        return NotesApiSearchResult(
            data=result.data
        )



class ContentVersionsQuery:
    """
    Query class for ContentVersions entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> ContentVersionsListResult:
        """
        Returns a list of content versions (file metadata) via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.
Note: ContentVersion does not support FIELDS(STANDARD), so specific fields must be listed.


        Args:
            q: SOQL query for content versions. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT Id, Title, FileExtension, ContentSize FROM ContentVersion WHERE IsLatest = true LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            ContentVersionsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("content_versions", "list", params)
        # Cast generic envelope to concrete typed result
        return ContentVersionsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> ContentVersion:
        """
        Get a single content version's metadata by ID. Returns file metadata, not the file content.
Use the download action to retrieve the actual file binary.


        Args:
            id: Salesforce ContentVersion ID (18-character ID starting with '068')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Title,FileExtension,ContentSize,ContentDocumentId,IsLatest"

            **kwargs: Additional parameters

        Returns:
            ContentVersion
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("content_versions", "get", params)
        return result



    async def download(
        self,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the binary file content of a content version.
First use the list or get action to retrieve the ContentVersion ID and file metadata (size, type, etc.),
then use this action to download the actual file content.
The response is the raw binary file data.


        Args:
            id: Salesforce ContentVersion ID (18-character ID starting with '068').
Obtain this ID from the list or get action.

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "id": id,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("content_versions", "download", params)
        return result


    async def download_local(
        self,
        path: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the binary file content of a content version.
First use the list or get action to retrieve the ContentVersion ID and file metadata (size, type, etc.),
then use this action to download the actual file content.
The response is the raw binary file data.
 and save to file.

        Args:
            id: Salesforce ContentVersion ID (18-character ID starting with '068').
Obtain this ID from the list or get action.

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            id=id,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class AttachmentsQuery:
    """
    Query class for Attachments entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> AttachmentsListResult:
        """
        Returns a list of attachments (legacy) via SOQL query. Default returns up to 200 records.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.
Note: Attachments are a legacy feature; consider using ContentVersion (Salesforce Files) for new implementations.


        Args:
            q: SOQL query for attachments. Default returns up to 200 records.
To change the limit, provide your own query with a LIMIT clause.
Example: "SELECT Id, Name, ContentType, BodyLength, ParentId FROM Attachment WHERE ParentId = '001xx...' LIMIT 50"

            **kwargs: Additional parameters

        Returns:
            AttachmentsListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "list", params)
        # Cast generic envelope to concrete typed result
        return AttachmentsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        id: str | None = None,
        fields: str | None = None,
        **kwargs
    ) -> Attachment:
        """
        Get a single attachment's metadata by ID. Returns file metadata, not the file content.
Use the download action to retrieve the actual file binary.
Note: Attachments are a legacy feature; consider using ContentVersion for new implementations.


        Args:
            id: Salesforce Attachment ID (18-character ID starting with '00P')
            fields: Comma-separated list of fields to retrieve. If omitted, returns all accessible fields.
Example: "Id,Name,ContentType,BodyLength,ParentId"

            **kwargs: Additional parameters

        Returns:
            Attachment
        """
        params = {k: v for k, v in {
            "id": id,
            "fields": fields,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "get", params)
        return result



    async def download(
        self,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads the binary file content of an attachment (legacy).
First use the list or get action to retrieve the Attachment ID and file metadata,
then use this action to download the actual file content.
Note: Attachments are a legacy feature; consider using ContentVersion for new implementations.


        Args:
            id: Salesforce Attachment ID (18-character ID starting with '00P').
Obtain this ID from the list or get action.

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "id": id,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("attachments", "download", params)
        return result


    async def download_local(
        self,
        path: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads the binary file content of an attachment (legacy).
First use the list or get action to retrieve the Attachment ID and file metadata,
then use this action to download the actual file content.
Note: Attachments are a legacy feature; consider using ContentVersion for new implementations.
 and save to file.

        Args:
            id: Salesforce Attachment ID (18-character ID starting with '00P').
Obtain this ID from the list or get action.

            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            path: File path to save downloaded content
            **kwargs: Additional parameters

        Returns:
            str: Path to the downloaded file
        """
        from ._vendored.connector_sdk import save_download

        # Get the async iterator
        content_iterator = await self.download(
            id=id,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class QueryQuery:
    """
    Query class for Query entity operations.
    """

    def __init__(self, connector: SalesforceConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        q: str,
        **kwargs
    ) -> QueryListResult:
        """
        Execute a custom SOQL query and return results. Use this for querying any Salesforce object.
For pagination, check the response: if `done` is false, use `nextRecordsUrl` to fetch the next page.


        Args:
            q: SOQL query string. Include LIMIT clause to control the number of records returned.
Examples:
- "SELECT Id, Name FROM Account LIMIT 100"
- "SELECT FIELDS(STANDARD) FROM Contact WHERE AccountId = '001xx...' LIMIT 50"
- "SELECT Id, Subject, Status FROM Case WHERE CreatedDate = TODAY"

            **kwargs: Additional parameters

        Returns:
            QueryListResult
        """
        params = {k: v for k, v in {
            "q": q,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("query", "list", params)
        # Cast generic envelope to concrete typed result
        return QueryListResult(
            data=result.data,
            meta=result.meta
        )


