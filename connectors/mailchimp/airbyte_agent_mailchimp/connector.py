"""
Mailchimp connector.
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

from .connector_model import MailchimpConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
from .types import (
    AutomationsListParams,
    CampaignsGetParams,
    CampaignsListParams,
    EmailActivityListParams,
    InterestCategoriesGetParams,
    InterestCategoriesListParams,
    InterestsGetParams,
    InterestsListParams,
    ListMembersGetParams,
    ListMembersListParams,
    ListsGetParams,
    ListsListParams,
    ReportsGetParams,
    ReportsListParams,
    SegmentMembersListParams,
    SegmentsGetParams,
    SegmentsListParams,
    TagsListParams,
    UnsubscribesListParams,
    AirbyteSearchParams,
    CampaignsSearchFilter,
    CampaignsSearchQuery,
    EmailActivitySearchFilter,
    EmailActivitySearchQuery,
    ListsSearchFilter,
    ListsSearchQuery,
    ReportsSearchFilter,
    ReportsSearchQuery,
)
if TYPE_CHECKING:
    from .models import MailchimpAuthConfig

# Import response models and envelope models at runtime
from .models import (
    MailchimpCheckResult,
    MailchimpExecuteResult,
    MailchimpExecuteResultWithMeta,
    CampaignsListResult,
    ListsListResult,
    ListMembersListResult,
    ReportsListResult,
    EmailActivityListResult,
    AutomationsListResult,
    TagsListResult,
    InterestCategoriesListResult,
    InterestsListResult,
    SegmentsListResult,
    SegmentMembersListResult,
    UnsubscribesListResult,
    Automation,
    Campaign,
    EmailActivity,
    Interest,
    InterestCategory,
    List,
    ListMember,
    Report,
    Segment,
    SegmentMember,
    Tag,
    Unsubscribe,
    AirbyteSearchHit,
    AirbyteSearchResult,
    CampaignsSearchData,
    CampaignsSearchResult,
    EmailActivitySearchData,
    EmailActivitySearchResult,
    ListsSearchData,
    ListsSearchResult,
    ReportsSearchData,
    ReportsSearchResult,
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




class MailchimpConnector:
    """
    Type-safe Mailchimp API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "mailchimp"
    connector_version = "1.0.5"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("campaigns", "list"): True,
        ("campaigns", "get"): None,
        ("lists", "list"): True,
        ("lists", "get"): None,
        ("list_members", "list"): True,
        ("list_members", "get"): None,
        ("reports", "list"): True,
        ("reports", "get"): None,
        ("email_activity", "list"): True,
        ("automations", "list"): True,
        ("tags", "list"): True,
        ("interest_categories", "list"): True,
        ("interest_categories", "get"): None,
        ("interests", "list"): True,
        ("interests", "get"): None,
        ("segments", "list"): True,
        ("segments", "get"): None,
        ("segment_members", "list"): True,
        ("unsubscribes", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('campaigns', 'list'): {'count': 'count', 'offset': 'offset', 'type': 'type', 'status': 'status', 'before_send_time': 'before_send_time', 'since_send_time': 'since_send_time', 'before_create_time': 'before_create_time', 'since_create_time': 'since_create_time', 'list_id': 'list_id', 'folder_id': 'folder_id', 'sort_field': 'sort_field', 'sort_dir': 'sort_dir'},
        ('campaigns', 'get'): {'campaign_id': 'campaign_id'},
        ('lists', 'list'): {'count': 'count', 'offset': 'offset', 'before_date_created': 'before_date_created', 'since_date_created': 'since_date_created', 'before_campaign_last_sent': 'before_campaign_last_sent', 'since_campaign_last_sent': 'since_campaign_last_sent', 'email': 'email', 'sort_field': 'sort_field', 'sort_dir': 'sort_dir'},
        ('lists', 'get'): {'list_id': 'list_id'},
        ('list_members', 'list'): {'list_id': 'list_id', 'count': 'count', 'offset': 'offset', 'email_type': 'email_type', 'status': 'status', 'since_timestamp_opt': 'since_timestamp_opt', 'before_timestamp_opt': 'before_timestamp_opt', 'since_last_changed': 'since_last_changed', 'before_last_changed': 'before_last_changed', 'unique_email_id': 'unique_email_id', 'vip_only': 'vip_only', 'interest_category_id': 'interest_category_id', 'interest_ids': 'interest_ids', 'interest_match': 'interest_match', 'sort_field': 'sort_field', 'sort_dir': 'sort_dir'},
        ('list_members', 'get'): {'list_id': 'list_id', 'subscriber_hash': 'subscriber_hash'},
        ('reports', 'list'): {'count': 'count', 'offset': 'offset', 'type': 'type', 'before_send_time': 'before_send_time', 'since_send_time': 'since_send_time'},
        ('reports', 'get'): {'campaign_id': 'campaign_id'},
        ('email_activity', 'list'): {'campaign_id': 'campaign_id', 'count': 'count', 'offset': 'offset', 'since': 'since'},
        ('automations', 'list'): {'count': 'count', 'offset': 'offset', 'before_create_time': 'before_create_time', 'since_create_time': 'since_create_time', 'before_start_time': 'before_start_time', 'since_start_time': 'since_start_time', 'status': 'status'},
        ('tags', 'list'): {'list_id': 'list_id', 'name': 'name'},
        ('interest_categories', 'list'): {'list_id': 'list_id', 'count': 'count', 'offset': 'offset'},
        ('interest_categories', 'get'): {'list_id': 'list_id', 'interest_category_id': 'interest_category_id'},
        ('interests', 'list'): {'list_id': 'list_id', 'interest_category_id': 'interest_category_id', 'count': 'count', 'offset': 'offset'},
        ('interests', 'get'): {'list_id': 'list_id', 'interest_category_id': 'interest_category_id', 'interest_id': 'interest_id'},
        ('segments', 'list'): {'list_id': 'list_id', 'count': 'count', 'offset': 'offset', 'type': 'type', 'since_created_at': 'since_created_at', 'before_created_at': 'before_created_at', 'since_updated_at': 'since_updated_at', 'before_updated_at': 'before_updated_at'},
        ('segments', 'get'): {'list_id': 'list_id', 'segment_id': 'segment_id'},
        ('segment_members', 'list'): {'list_id': 'list_id', 'segment_id': 'segment_id', 'count': 'count', 'offset': 'offset'},
        ('unsubscribes', 'list'): {'campaign_id': 'campaign_id', 'count': 'count', 'offset': 'offset'},
    }

    def __init__(
        self,
        auth_config: MailchimpAuthConfig | None = None,
        external_user_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        connector_id: str | None = None,
        on_token_refresh: Any | None = None,
        data_center: str | None = None    ):
        """
        Initialize a new mailchimp connector instance.

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
                Example: lambda tokens: save_to_database(tokens)            data_center: The data center for your Mailchimp account (e.g., us1, us2, us6)
        Examples:
            # Local mode (direct API calls)
            connector = MailchimpConnector(auth_config=MailchimpAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = MailchimpConnector(
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789",
                connector_id="existing-source-uuid"
            )

            # Hosted mode with lookup by external_user_id
            connector = MailchimpConnector(
                external_user_id="user-123",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = MailchimpConnector(
                auth_config=MailchimpAuthConfig(access_token="...", refresh_token="..."),
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
                connector_definition_id=str(MailchimpConnectorModel.id) if not connector_id else None,
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
            if data_center:
                config_values["data_center"] = data_center

            self._executor = LocalExecutor(
                model=MailchimpConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided
            base_url = self._executor.http_client.base_url
            if data_center:
                base_url = base_url.replace("{data_center}", data_center)
            self._executor.http_client.base_url = base_url

        # Initialize entity query objects
        self.campaigns = CampaignsQuery(self)
        self.lists = ListsQuery(self)
        self.list_members = ListMembersQuery(self)
        self.reports = ReportsQuery(self)
        self.email_activity = EmailActivityQuery(self)
        self.automations = AutomationsQuery(self)
        self.tags = TagsQuery(self)
        self.interest_categories = InterestCategoriesQuery(self)
        self.interests = InterestsQuery(self)
        self.segments = SegmentsQuery(self)
        self.segment_members = SegmentMembersQuery(self)
        self.unsubscribes = UnsubscribesQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

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
        entity: Literal["list_members"],
        action: Literal["list"],
        params: "ListMembersListParams"
    ) -> "ListMembersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["list_members"],
        action: Literal["get"],
        params: "ListMembersGetParams"
    ) -> "ListMember": ...

    @overload
    async def execute(
        self,
        entity: Literal["reports"],
        action: Literal["list"],
        params: "ReportsListParams"
    ) -> "ReportsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["reports"],
        action: Literal["get"],
        params: "ReportsGetParams"
    ) -> "Report": ...

    @overload
    async def execute(
        self,
        entity: Literal["email_activity"],
        action: Literal["list"],
        params: "EmailActivityListParams"
    ) -> "EmailActivityListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["automations"],
        action: Literal["list"],
        params: "AutomationsListParams"
    ) -> "AutomationsListResult": ...

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
        entity: Literal["interest_categories"],
        action: Literal["list"],
        params: "InterestCategoriesListParams"
    ) -> "InterestCategoriesListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["interest_categories"],
        action: Literal["get"],
        params: "InterestCategoriesGetParams"
    ) -> "InterestCategory": ...

    @overload
    async def execute(
        self,
        entity: Literal["interests"],
        action: Literal["list"],
        params: "InterestsListParams"
    ) -> "InterestsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["interests"],
        action: Literal["get"],
        params: "InterestsGetParams"
    ) -> "Interest": ...

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
        entity: Literal["segment_members"],
        action: Literal["list"],
        params: "SegmentMembersListParams"
    ) -> "SegmentMembersListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["unsubscribes"],
        action: Literal["list"],
        params: "UnsubscribesListParams"
    ) -> "UnsubscribesListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> MailchimpExecuteResult[Any] | MailchimpExecuteResultWithMeta[Any, Any] | Any: ...

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
                return MailchimpExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return MailchimpExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> MailchimpCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            MailchimpCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return MailchimpCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return MailchimpCheckResult(
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
            @MailchimpConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @MailchimpConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    MailchimpConnectorModel,
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
        return describe_entities(MailchimpConnectorModel)

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
            (e for e in MailchimpConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in MailchimpConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.

        Example:
            connector = await MailchimpConnector.create_hosted(...)
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
        auth_config: "MailchimpAuthConfig",
        name: str | None = None,
        replication_config: dict[str, Any] | None = None,
    ) -> "MailchimpConnector":
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
            A MailchimpConnector instance configured in hosted mode

        Example:
            # Create a new hosted connector with API key auth
            connector = await MailchimpConnector.create_hosted(
                external_user_id="my-workspace",
                airbyte_client_id="client_abc",
                airbyte_client_secret="secret_xyz",
                auth_config=MailchimpAuthConfig(api_key="..."),
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
                connector_definition_id=str(MailchimpConnectorModel.id),
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



class CampaignsQuery:
    """
    Query class for Campaigns entity operations.
    """

    def __init__(self, connector: MailchimpConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        count: int | None = None,
        offset: int | None = None,
        type: str | None = None,
        status: str | None = None,
        before_send_time: str | None = None,
        since_send_time: str | None = None,
        before_create_time: str | None = None,
        since_create_time: str | None = None,
        list_id: str | None = None,
        folder_id: str | None = None,
        sort_field: str | None = None,
        sort_dir: str | None = None,
        **kwargs
    ) -> CampaignsListResult:
        """
        Get all campaigns in an account

        Args:
            count: The number of records to return. Default is 10. Maximum is 1000.
            offset: Used for pagination, this is the number of records from a collection to skip.
            type: The campaign type
            status: The status of the campaign
            before_send_time: Restrict the response to campaigns sent before the set time
            since_send_time: Restrict the response to campaigns sent after the set time
            before_create_time: Restrict the response to campaigns created before the set time
            since_create_time: Restrict the response to campaigns created after the set time
            list_id: The unique id for the list
            folder_id: The unique folder id
            sort_field: Returns files sorted by the specified field
            sort_dir: Determines the order direction for sorted results
            **kwargs: Additional parameters

        Returns:
            CampaignsListResult
        """
        params = {k: v for k, v in {
            "count": count,
            "offset": offset,
            "type": type,
            "status": status,
            "before_send_time": before_send_time,
            "since_send_time": since_send_time,
            "before_create_time": before_create_time,
            "since_create_time": since_create_time,
            "list_id": list_id,
            "folder_id": folder_id,
            "sort_field": sort_field,
            "sort_dir": sort_dir,
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
        campaign_id: str,
        **kwargs
    ) -> Campaign:
        """
        Get information about a specific campaign

        Args:
            campaign_id: The unique id for the campaign
            **kwargs: Additional parameters

        Returns:
            Campaign
        """
        params = {k: v for k, v in {
            "campaign_id": campaign_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("campaigns", "get", params)
        return result



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
        - ab_split_opts: [A/B Testing](https://mailchimp.com/help/about-ab-testing-campaigns/) options for a campaign.
        - archive_url: The link to the campaign's archive version in ISO 8601 format.
        - content_type: How the campaign's content is put together.
        - create_time: The date and time the campaign was created in ISO 8601 format.
        - delivery_status: Updates on campaigns in the process of sending.
        - emails_sent: The total number of emails sent for this campaign.
        - id: A string that uniquely identifies this campaign.
        - long_archive_url: The original link to the campaign's archive version.
        - needs_block_refresh: Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor. D...
        - parent_campaign_id: If this campaign is the child of another campaign, this identifies the parent campaign. For Examp...
        - recipients: List settings for the campaign.
        - report_summary: For sent campaigns, a summary of opens, clicks, and e-commerce data.
        - resendable: Determines if the campaign qualifies to be resent to non-openers.
        - rss_opts: [RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options for a campaign.
        - send_time: The date and time a campaign was sent.
        - settings: The settings for your campaign, including subject, from name, reply-to address, and more.
        - social_card: The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more]...
        - status: The current status of the campaign.
        - tracking: The tracking options for a campaign.
        - type: There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) y...
        - variate_settings: The settings specific to A/B test campaigns.
        - web_id: The ID used in the Mailchimp web application. View this campaign in your Mailchimp account at `ht...

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CampaignsSearchResult with hits (list of AirbyteSearchHit[CampaignsSearchData]) and pagination info

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
        return CampaignsSearchResult(
            hits=[
                AirbyteSearchHit[CampaignsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=CampaignsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class ListsQuery:
    """
    Query class for Lists entity operations.
    """

    def __init__(self, connector: MailchimpConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        count: int | None = None,
        offset: int | None = None,
        before_date_created: str | None = None,
        since_date_created: str | None = None,
        before_campaign_last_sent: str | None = None,
        since_campaign_last_sent: str | None = None,
        email: str | None = None,
        sort_field: str | None = None,
        sort_dir: str | None = None,
        **kwargs
    ) -> ListsListResult:
        """
        Get information about all lists in the account

        Args:
            count: The number of records to return
            offset: Used for pagination
            before_date_created: Restrict response to lists created before the set date
            since_date_created: Restrict response to lists created after the set date
            before_campaign_last_sent: Restrict results to lists created before the last campaign send date
            since_campaign_last_sent: Restrict results to lists created after the last campaign send date
            email: Restrict results to lists that include a specific subscriber's email address
            sort_field: Returns files sorted by the specified field
            sort_dir: Determines the order direction for sorted results
            **kwargs: Additional parameters

        Returns:
            ListsListResult
        """
        params = {k: v for k, v in {
            "count": count,
            "offset": offset,
            "before_date_created": before_date_created,
            "since_date_created": since_date_created,
            "before_campaign_last_sent": before_campaign_last_sent,
            "since_campaign_last_sent": since_campaign_last_sent,
            "email": email,
            "sort_field": sort_field,
            "sort_dir": sort_dir,
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
        list_id: str,
        **kwargs
    ) -> List:
        """
        Get information about a specific list in your Mailchimp account

        Args:
            list_id: The unique ID for the list
            **kwargs: Additional parameters

        Returns:
            List
        """
        params = {k: v for k, v in {
            "list_id": list_id,
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
        - beamer_address: The list's Email Beamer address.
        - campaign_defaults: Default values for campaigns created for this list.
        - contact: Contact information displayed in campaign footers to comply with international spam laws.
        - date_created: The date and time that this list was created in ISO 8601 format.
        - double_optin: Whether or not to require the subscriber to confirm subscription via email.
        - email_type_option: Whether the list supports multiple formats for emails. When set to `true`, subscribers can choose...
        - has_welcome: Whether or not this list has a welcome automation connected.
        - id: A string that uniquely identifies this list.
        - list_rating: An auto-generated activity score for the list (0-5).
        - marketing_permissions: Whether or not the list has marketing permissions (eg. GDPR) enabled.
        - modules: Any list-specific modules installed for this list.
        - name: The name of the list.
        - notify_on_subscribe: The email address to send subscribe notifications to.
        - notify_on_unsubscribe: The email address to send unsubscribe notifications to.
        - permission_reminder: The permission reminder for the list.
        - stats: Stats for the list. Many of these are cached for at least five minutes.
        - subscribe_url_long: The full version of this list's subscribe form (host will vary).
        - subscribe_url_short: Our EepURL shortened version of this list's subscribe form.
        - use_archive_bar: Whether campaigns for this list use the Archive Bar in archives by default.
        - visibility: Whether this list is public or private.
        - web_id: The ID used in the Mailchimp web application. View this list in your Mailchimp account at `https:...

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ListsSearchResult with hits (list of AirbyteSearchHit[ListsSearchData]) and pagination info

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
        return ListsSearchResult(
            hits=[
                AirbyteSearchHit[ListsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ListsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class ListMembersQuery:
    """
    Query class for ListMembers entity operations.
    """

    def __init__(self, connector: MailchimpConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        list_id: str,
        count: int | None = None,
        offset: int | None = None,
        email_type: str | None = None,
        status: str | None = None,
        since_timestamp_opt: str | None = None,
        before_timestamp_opt: str | None = None,
        since_last_changed: str | None = None,
        before_last_changed: str | None = None,
        unique_email_id: str | None = None,
        vip_only: bool | None = None,
        interest_category_id: str | None = None,
        interest_ids: str | None = None,
        interest_match: str | None = None,
        sort_field: str | None = None,
        sort_dir: str | None = None,
        **kwargs
    ) -> ListMembersListResult:
        """
        Get information about members in a specific Mailchimp list

        Args:
            list_id: The unique ID for the list
            count: The number of records to return
            offset: Used for pagination
            email_type: The email type
            status: The subscriber's status
            since_timestamp_opt: Restrict results to subscribers who opted-in after the set timeframe
            before_timestamp_opt: Restrict results to subscribers who opted-in before the set timeframe
            since_last_changed: Restrict results to subscribers whose information changed after the set timeframe
            before_last_changed: Restrict results to subscribers whose information changed before the set timeframe
            unique_email_id: A unique identifier for the email address across all Mailchimp lists
            vip_only: A filter to return only the list's VIP members
            interest_category_id: The unique id for the interest category
            interest_ids: Used to filter list members by interests
            interest_match: Used to filter list members by interests
            sort_field: Returns files sorted by the specified field
            sort_dir: Determines the order direction for sorted results
            **kwargs: Additional parameters

        Returns:
            ListMembersListResult
        """
        params = {k: v for k, v in {
            "list_id": list_id,
            "count": count,
            "offset": offset,
            "email_type": email_type,
            "status": status,
            "since_timestamp_opt": since_timestamp_opt,
            "before_timestamp_opt": before_timestamp_opt,
            "since_last_changed": since_last_changed,
            "before_last_changed": before_last_changed,
            "unique_email_id": unique_email_id,
            "vip_only": vip_only,
            "interest_category_id": interest_category_id,
            "interest_ids": interest_ids,
            "interest_match": interest_match,
            "sort_field": sort_field,
            "sort_dir": sort_dir,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("list_members", "list", params)
        # Cast generic envelope to concrete typed result
        return ListMembersListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        list_id: str,
        subscriber_hash: str,
        **kwargs
    ) -> ListMember:
        """
        Get information about a specific list member

        Args:
            list_id: The unique ID for the list
            subscriber_hash: The MD5 hash of the lowercase version of the list member's email address
            **kwargs: Additional parameters

        Returns:
            ListMember
        """
        params = {k: v for k, v in {
            "list_id": list_id,
            "subscriber_hash": subscriber_hash,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("list_members", "get", params)
        return result



class ReportsQuery:
    """
    Query class for Reports entity operations.
    """

    def __init__(self, connector: MailchimpConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        count: int | None = None,
        offset: int | None = None,
        type: str | None = None,
        before_send_time: str | None = None,
        since_send_time: str | None = None,
        **kwargs
    ) -> ReportsListResult:
        """
        Get campaign reports

        Args:
            count: The number of records to return
            offset: Used for pagination
            type: The campaign type
            before_send_time: Restrict the response to campaigns sent before the set time
            since_send_time: Restrict the response to campaigns sent after the set time
            **kwargs: Additional parameters

        Returns:
            ReportsListResult
        """
        params = {k: v for k, v in {
            "count": count,
            "offset": offset,
            "type": type,
            "before_send_time": before_send_time,
            "since_send_time": since_send_time,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("reports", "list", params)
        # Cast generic envelope to concrete typed result
        return ReportsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        campaign_id: str,
        **kwargs
    ) -> Report:
        """
        Get report details for a specific sent campaign

        Args:
            campaign_id: The unique id for the campaign
            **kwargs: Additional parameters

        Returns:
            Report
        """
        params = {k: v for k, v in {
            "campaign_id": campaign_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("reports", "get", params)
        return result



    async def search(
        self,
        query: ReportsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ReportsSearchResult:
        """
        Search reports records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ReportsSearchFilter):
        - ab_split: General stats about different groups of an A/B Split campaign. Does not return information about ...
        - abuse_reports: The number of abuse reports generated for this campaign.
        - bounces: An object describing the bounce summary for the campaign.
        - campaign_title: The title of the campaign.
        - clicks: An object describing the click activity for the campaign.
        - delivery_status: Updates on campaigns in the process of sending.
        - ecommerce: E-Commerce stats for a campaign.
        - emails_sent: The total number of emails sent for this campaign.
        - facebook_likes: An object describing campaign engagement on Facebook.
        - forwards: An object describing the forwards and forward activity for the campaign.
        - id: A string that uniquely identifies this campaign.
        - industry_stats: The average campaign statistics for your industry.
        - list_id: The unique list id.
        - list_is_active: The status of the list used, namely if it's deleted or disabled.
        - list_name: The name of the list.
        - list_stats: The average campaign statistics for your list. This won't be present if we haven't calculated i...
        - opens: An object describing the open activity for the campaign.
        - preview_text: The preview text for the campaign.
        - rss_last_send: For RSS campaigns, the date and time of the last send in ISO 8601 format.
        - send_time: The date and time a campaign was sent in ISO 8601 format.
        - share_report: The url and password for the VIP report.
        - subject_line: The subject line for the campaign.
        - timeseries: An hourly breakdown of the performance of the campaign over the first 24 hours.
        - timewarp: An hourly breakdown of sends, opens, and clicks if a campaign is sent using timewarp.
        - type: The type of campaign (regular, plain-text, ab_split, rss, automation, variate, or auto).
        - unsubscribed: The total number of unsubscribed members for this campaign.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ReportsSearchResult with hits (list of AirbyteSearchHit[ReportsSearchData]) and pagination info

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

        result = await self._connector.execute("reports", "search", params)

        # Parse response into typed result
        return ReportsSearchResult(
            hits=[
                AirbyteSearchHit[ReportsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ReportsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class EmailActivityQuery:
    """
    Query class for EmailActivity entity operations.
    """

    def __init__(self, connector: MailchimpConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        campaign_id: str,
        count: int | None = None,
        offset: int | None = None,
        since: str | None = None,
        **kwargs
    ) -> EmailActivityListResult:
        """
        Get a list of member's subscriber activity in a specific campaign

        Args:
            campaign_id: The unique id for the campaign
            count: The number of records to return
            offset: Used for pagination
            since: Restrict results to email activity events that occur after a specific time
            **kwargs: Additional parameters

        Returns:
            EmailActivityListResult
        """
        params = {k: v for k, v in {
            "campaign_id": campaign_id,
            "count": count,
            "offset": offset,
            "since": since,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("email_activity", "list", params)
        # Cast generic envelope to concrete typed result
        return EmailActivityListResult(
            data=result.data,
            meta=result.meta
        )



    async def search(
        self,
        query: EmailActivitySearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> EmailActivitySearchResult:
        """
        Search email_activity records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (EmailActivitySearchFilter):
        - action: One of the following actions: 'open', 'click', or 'bounce'
        - campaign_id: The unique id for the campaign.
        - email_address: Email address for a subscriber.
        - email_id: The MD5 hash of the lowercase version of the list member's email address.
        - ip: The IP address recorded for the action.
        - list_id: The unique id for the list.
        - list_is_active: The status of the list used, namely if it's deleted or disabled.
        - timestamp: The date and time recorded for the action in ISO 8601 format.
        - type: If the action is a 'bounce', the type of bounce received: 'hard', 'soft'.
        - url: If the action is a 'click', the URL on which the member clicked.

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            EmailActivitySearchResult with hits (list of AirbyteSearchHit[EmailActivitySearchData]) and pagination info

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

        result = await self._connector.execute("email_activity", "search", params)

        # Parse response into typed result
        return EmailActivitySearchResult(
            hits=[
                AirbyteSearchHit[EmailActivitySearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=EmailActivitySearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

class AutomationsQuery:
    """
    Query class for Automations entity operations.
    """

    def __init__(self, connector: MailchimpConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        count: int | None = None,
        offset: int | None = None,
        before_create_time: str | None = None,
        since_create_time: str | None = None,
        before_start_time: str | None = None,
        since_start_time: str | None = None,
        status: str | None = None,
        **kwargs
    ) -> AutomationsListResult:
        """
        Get a summary of an account's classic automations

        Args:
            count: The number of records to return
            offset: Used for pagination
            before_create_time: Restrict the response to automations created before this time
            since_create_time: Restrict the response to automations created after this time
            before_start_time: Restrict the response to automations started before this time
            since_start_time: Restrict the response to automations started after this time
            status: Restrict the results to automations with the specified status
            **kwargs: Additional parameters

        Returns:
            AutomationsListResult
        """
        params = {k: v for k, v in {
            "count": count,
            "offset": offset,
            "before_create_time": before_create_time,
            "since_create_time": since_create_time,
            "before_start_time": before_start_time,
            "since_start_time": since_start_time,
            "status": status,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("automations", "list", params)
        # Cast generic envelope to concrete typed result
        return AutomationsListResult(
            data=result.data,
            meta=result.meta
        )



class TagsQuery:
    """
    Query class for Tags entity operations.
    """

    def __init__(self, connector: MailchimpConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        list_id: str,
        name: str | None = None,
        **kwargs
    ) -> TagsListResult:
        """
        Search for tags on a list by name

        Args:
            list_id: The unique ID for the list
            name: The search query used to filter tags
            **kwargs: Additional parameters

        Returns:
            TagsListResult
        """
        params = {k: v for k, v in {
            "list_id": list_id,
            "name": name,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("tags", "list", params)
        # Cast generic envelope to concrete typed result
        return TagsListResult(
            data=result.data,
            meta=result.meta
        )



class InterestCategoriesQuery:
    """
    Query class for InterestCategories entity operations.
    """

    def __init__(self, connector: MailchimpConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        list_id: str,
        count: int | None = None,
        offset: int | None = None,
        **kwargs
    ) -> InterestCategoriesListResult:
        """
        Get information about a list's interest categories

        Args:
            list_id: The unique ID for the list
            count: The number of records to return
            offset: Used for pagination
            **kwargs: Additional parameters

        Returns:
            InterestCategoriesListResult
        """
        params = {k: v for k, v in {
            "list_id": list_id,
            "count": count,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("interest_categories", "list", params)
        # Cast generic envelope to concrete typed result
        return InterestCategoriesListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        list_id: str,
        interest_category_id: str,
        **kwargs
    ) -> InterestCategory:
        """
        Get information about a specific interest category

        Args:
            list_id: The unique ID for the list
            interest_category_id: The unique ID for the interest category
            **kwargs: Additional parameters

        Returns:
            InterestCategory
        """
        params = {k: v for k, v in {
            "list_id": list_id,
            "interest_category_id": interest_category_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("interest_categories", "get", params)
        return result



class InterestsQuery:
    """
    Query class for Interests entity operations.
    """

    def __init__(self, connector: MailchimpConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        list_id: str,
        interest_category_id: str,
        count: int | None = None,
        offset: int | None = None,
        **kwargs
    ) -> InterestsListResult:
        """
        Get a list of this category's interests

        Args:
            list_id: The unique ID for the list
            interest_category_id: The unique ID for the interest category
            count: The number of records to return
            offset: Used for pagination
            **kwargs: Additional parameters

        Returns:
            InterestsListResult
        """
        params = {k: v for k, v in {
            "list_id": list_id,
            "interest_category_id": interest_category_id,
            "count": count,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("interests", "list", params)
        # Cast generic envelope to concrete typed result
        return InterestsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        list_id: str,
        interest_category_id: str,
        interest_id: str,
        **kwargs
    ) -> Interest:
        """
        Get interests or group names for a specific category

        Args:
            list_id: The unique ID for the list
            interest_category_id: The unique ID for the interest category
            interest_id: The specific interest or group name
            **kwargs: Additional parameters

        Returns:
            Interest
        """
        params = {k: v for k, v in {
            "list_id": list_id,
            "interest_category_id": interest_category_id,
            "interest_id": interest_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("interests", "get", params)
        return result



class SegmentsQuery:
    """
    Query class for Segments entity operations.
    """

    def __init__(self, connector: MailchimpConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        list_id: str,
        count: int | None = None,
        offset: int | None = None,
        type: str | None = None,
        since_created_at: str | None = None,
        before_created_at: str | None = None,
        since_updated_at: str | None = None,
        before_updated_at: str | None = None,
        **kwargs
    ) -> SegmentsListResult:
        """
        Get information about all available segments for a specific list

        Args:
            list_id: The unique ID for the list
            count: The number of records to return
            offset: Used for pagination
            type: Limit results based on segment type
            since_created_at: Restrict results to segments created after the set time
            before_created_at: Restrict results to segments created before the set time
            since_updated_at: Restrict results to segments updated after the set time
            before_updated_at: Restrict results to segments updated before the set time
            **kwargs: Additional parameters

        Returns:
            SegmentsListResult
        """
        params = {k: v for k, v in {
            "list_id": list_id,
            "count": count,
            "offset": offset,
            "type": type,
            "since_created_at": since_created_at,
            "before_created_at": before_created_at,
            "since_updated_at": since_updated_at,
            "before_updated_at": before_updated_at,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segments", "list", params)
        # Cast generic envelope to concrete typed result
        return SegmentsListResult(
            data=result.data,
            meta=result.meta
        )



    async def get(
        self,
        list_id: str,
        segment_id: str,
        **kwargs
    ) -> Segment:
        """
        Get information about a specific segment

        Args:
            list_id: The unique ID for the list
            segment_id: The unique id for the segment
            **kwargs: Additional parameters

        Returns:
            Segment
        """
        params = {k: v for k, v in {
            "list_id": list_id,
            "segment_id": segment_id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segments", "get", params)
        return result



class SegmentMembersQuery:
    """
    Query class for SegmentMembers entity operations.
    """

    def __init__(self, connector: MailchimpConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        list_id: str,
        segment_id: str,
        count: int | None = None,
        offset: int | None = None,
        **kwargs
    ) -> SegmentMembersListResult:
        """
        Get information about members in a saved segment

        Args:
            list_id: The unique ID for the list
            segment_id: The unique id for the segment
            count: The number of records to return
            offset: Used for pagination
            **kwargs: Additional parameters

        Returns:
            SegmentMembersListResult
        """
        params = {k: v for k, v in {
            "list_id": list_id,
            "segment_id": segment_id,
            "count": count,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("segment_members", "list", params)
        # Cast generic envelope to concrete typed result
        return SegmentMembersListResult(
            data=result.data,
            meta=result.meta
        )



class UnsubscribesQuery:
    """
    Query class for Unsubscribes entity operations.
    """

    def __init__(self, connector: MailchimpConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        campaign_id: str,
        count: int | None = None,
        offset: int | None = None,
        **kwargs
    ) -> UnsubscribesListResult:
        """
        Get information about members who have unsubscribed from a specific campaign

        Args:
            campaign_id: The unique id for the campaign
            count: The number of records to return
            offset: Used for pagination
            **kwargs: Additional parameters

        Returns:
            UnsubscribesListResult
        """
        params = {k: v for k, v in {
            "campaign_id": campaign_id,
            "count": count,
            "offset": offset,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("unsubscribes", "list", params)
        # Cast generic envelope to concrete typed result
        return UnsubscribesListResult(
            data=result.data,
            meta=result.meta
        )


