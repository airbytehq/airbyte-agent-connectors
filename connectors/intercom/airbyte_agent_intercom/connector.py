"""
Intercom connector.
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

from .connector_model import IntercomConnectorModel
from ._vendored.connector_sdk.introspection import describe_entities, generate_tool_description
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
    AirbyteSearchParams,
    CompaniesSearchFilter,
    CompaniesSearchQuery,
    ContactsSearchFilter,
    ContactsSearchQuery,
    ConversationsSearchFilter,
    ConversationsSearchQuery,
    TeamsSearchFilter,
    TeamsSearchQuery,
)
if TYPE_CHECKING:
    from .models import IntercomAuthConfig
# Import response models and envelope models at runtime
from .models import (
    IntercomCheckResult,
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
    AirbyteSearchHit,
    AirbyteSearchResult,
    CompaniesSearchData,
    CompaniesSearchResult,
    ContactsSearchData,
    ContactsSearchResult,
    ConversationsSearchData,
    ConversationsSearchResult,
    TeamsSearchData,
    TeamsSearchResult,
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




class IntercomConnector:
    """
    Type-safe Intercom API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "intercom"
    connector_version = "0.1.6"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("contacts", "list"): True,
        ("contacts", "get"): None,
        ("conversations", "list"): True,
        ("conversations", "get"): None,
        ("companies", "list"): True,
        ("companies", "get"): None,
        ("teams", "list"): True,
        ("teams", "get"): None,
        ("admins", "list"): True,
        ("admins", "get"): None,
        ("tags", "list"): True,
        ("tags", "get"): None,
        ("segments", "list"): True,
        ("segments", "get"): None,
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
        action: Literal["list", "get", "search"],
        params: Mapping[str, Any]
    ) -> IntercomExecuteResult[Any] | IntercomExecuteResultWithMeta[Any, Any] | Any: ...

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
                return IntercomExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return IntercomExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> IntercomCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            IntercomCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return IntercomCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return IntercomCheckResult(
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
            @IntercomConnector.tool_utils
            async def execute(entity: str, action: str, params: dict):
                ...

            @mcp.tool()
            @IntercomConnector.tool_utils(update_docstring=False, max_output_chars=None)
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
                    IntercomConnectorModel,
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
            meta=result.meta
        )



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
        - android_app_name: The name of the Android app associated with the contact.
        - android_app_version: The version of the Android app associated with the contact.
        - android_device: The device used by the contact for Android.
        - android_last_seen_at: The date and time when the contact was last seen on Android.
        - android_os_version: The operating system version of the Android device.
        - android_sdk_version: The SDK version of the Android device.
        - avatar: URL pointing to the contact's avatar image.
        - browser: The browser used by the contact.
        - browser_language: The language preference set in the contact's browser.
        - browser_version: The version of the browser used by the contact.
        - companies: Companies associated with the contact.
        - created_at: The date and time when the contact was created.
        - custom_attributes: Custom attributes defined for the contact.
        - email: The email address of the contact.
        - external_id: External identifier for the contact.
        - has_hard_bounced: Flag indicating if the contact has hard bounced.
        - id: The unique identifier of the contact.
        - ios_app_name: The name of the iOS app associated with the contact.
        - ios_app_version: The version of the iOS app associated with the contact.
        - ios_device: The device used by the contact for iOS.
        - ios_last_seen_at: The date and time when the contact was last seen on iOS.
        - ios_os_version: The operating system version of the iOS device.
        - ios_sdk_version: The SDK version of the iOS device.
        - language_override: Language override set for the contact.
        - last_contacted_at: The date and time when the contact was last contacted.
        - last_email_clicked_at: The date and time when the contact last clicked an email.
        - last_email_opened_at: The date and time when the contact last opened an email.
        - last_replied_at: The date and time when the contact last replied.
        - last_seen_at: The date and time when the contact was last seen overall.
        - location: Location details of the contact.
        - marked_email_as_spam: Flag indicating if the contact's email was marked as spam.
        - name: The name of the contact.
        - notes: Notes associated with the contact.
        - opted_in_subscription_types: Subscription types the contact opted into.
        - opted_out_subscription_types: Subscription types the contact opted out from.
        - os: Operating system of the contact's device.
        - owner_id: The unique identifier of the contact's owner.
        - phone: The phone number of the contact.
        - referrer: Referrer information related to the contact.
        - role: Role or position of the contact.
        - signed_up_at: The date and time when the contact signed up.
        - sms_consent: Consent status for SMS communication.
        - social_profiles: Social profiles associated with the contact.
        - tags: Tags associated with the contact.
        - type: Type of contact.
        - unsubscribed_from_emails: Flag indicating if the contact unsubscribed from emails.
        - unsubscribed_from_sms: Flag indicating if the contact unsubscribed from SMS.
        - updated_at: The date and time when the contact was last updated.
        - utm_campaign: Campaign data from UTM parameters.
        - utm_content: Content data from UTM parameters.
        - utm_medium: Medium data from UTM parameters.
        - utm_source: Source data from UTM parameters.
        - utm_term: Term data from UTM parameters.
        - workspace_id: The unique identifier of the workspace associated with the contact.

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
            meta=result.meta
        )



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



    async def search(
        self,
        query: ConversationsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> ConversationsSearchResult:
        """
        Search conversations records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (ConversationsSearchFilter):
        - admin_assignee_id: The ID of the administrator assigned to the conversation
        - ai_agent: Data related to AI Agent involvement in the conversation
        - ai_agent_participated: Indicates whether AI Agent participated in the conversation
        - assignee: The assigned user responsible for the conversation.
        - contacts: List of contacts involved in the conversation.
        - conversation_message: The main message content of the conversation.
        - conversation_rating: Ratings given to the conversation by the customer and teammate.
        - created_at: The timestamp when the conversation was created
        - custom_attributes: Custom attributes associated with the conversation
        - customer_first_reply: Timestamp indicating when the customer first replied.
        - customers: List of customers involved in the conversation
        - first_contact_reply: Timestamp indicating when the first contact replied.
        - id: The unique ID of the conversation
        - linked_objects: Linked objects associated with the conversation
        - open: Indicates if the conversation is open or closed
        - priority: The priority level of the conversation
        - read: Indicates if the conversation has been read
        - redacted: Indicates if the conversation is redacted
        - sent_at: The timestamp when the conversation was sent
        - sla_applied: Service Level Agreement details applied to the conversation.
        - snoozed_until: Timestamp until the conversation is snoozed
        - source: Source details of the conversation.
        - state: The state of the conversation (e.g., new, in progress)
        - statistics: Statistics related to the conversation.
        - tags: Tags applied to the conversation.
        - team_assignee_id: The ID of the team assigned to the conversation
        - teammates: List of teammates involved in the conversation.
        - title: The title of the conversation
        - topics: Topics associated with the conversation.
        - type: The type of the conversation
        - updated_at: The timestamp when the conversation was last updated
        - user: The user related to the conversation.
        - waiting_since: Timestamp since waiting for a response

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            ConversationsSearchResult with hits (list of AirbyteSearchHit[ConversationsSearchData]) and pagination info

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

        result = await self._connector.execute("conversations", "search", params)

        # Parse response into typed result
        return ConversationsSearchResult(
            hits=[
                AirbyteSearchHit[ConversationsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=ConversationsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            meta=result.meta
        )



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



    async def search(
        self,
        query: CompaniesSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> CompaniesSearchResult:
        """
        Search companies records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (CompaniesSearchFilter):
        - app_id: The ID of the application associated with the company
        - company_id: The unique identifier of the company
        - created_at: The date and time when the company was created
        - custom_attributes: Custom attributes specific to the company
        - id: The ID of the company
        - industry: The industry in which the company operates
        - monthly_spend: The monthly spend of the company
        - name: The name of the company
        - plan: Details of the company's subscription plan
        - remote_created_at: The remote date and time when the company was created
        - segments: Segments associated with the company
        - session_count: The number of sessions related to the company
        - size: The size of the company
        - tags: Tags associated with the company
        - type: The type of the company
        - updated_at: The date and time when the company was last updated
        - user_count: The number of users associated with the company
        - website: The website of the company

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            CompaniesSearchResult with hits (list of AirbyteSearchHit[CompaniesSearchData]) and pagination info

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

        result = await self._connector.execute("companies", "search", params)

        # Parse response into typed result
        return CompaniesSearchResult(
            hits=[
                AirbyteSearchHit[CompaniesSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=CompaniesSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            data=result.data
        )



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



    async def search(
        self,
        query: TeamsSearchQuery,
        limit: int | None = None,
        cursor: str | None = None,
        fields: list[list[str]] | None = None,
    ) -> TeamsSearchResult:
        """
        Search teams records from Airbyte cache.

        This operation searches cached data from Airbyte syncs.
        Only available in hosted execution mode.

        Available filter fields (TeamsSearchFilter):
        - admin_ids: Array of user IDs representing the admins of the team.
        - id: Unique identifier for the team.
        - name: Name of the team.
        - type: Type of team (e.g., 'internal', 'external').

        Args:
            query: Filter and sort conditions. Supports operators like eq, neq, gt, gte, lt, lte,
                   in, like, fuzzy, keyword, not, and, or. Example: {"filter": {"eq": {"status": "active"}}}
            limit: Maximum results to return (default 1000)
            cursor: Pagination cursor from previous response's next_cursor
            fields: Field paths to include in results. Each path is a list of keys for nested access.
                    Example: [["id"], ["user", "name"]] returns id and user.name fields.

        Returns:
            TeamsSearchResult with hits (list of AirbyteSearchHit[TeamsSearchData]) and pagination info

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

        result = await self._connector.execute("teams", "search", params)

        # Parse response into typed result
        return TeamsSearchResult(
            hits=[
                AirbyteSearchHit[TeamsSearchData](
                    id=hit.get("id"),
                    score=hit.get("score"),
                    data=TeamsSearchData(**hit.get("data", {}))
                )
                for hit in result.get("hits", [])
            ],
            next_cursor=result.get("next_cursor"),
            took_ms=result.get("took_ms")
        )

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
            data=result.data
        )



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
            data=result.data
        )



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
            data=result.data
        )



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


