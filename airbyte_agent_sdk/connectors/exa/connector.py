"""
Exa connector.
"""

from __future__ import annotations

import logging
from typing import Any, Callable, Mapping, TypeVar, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pydantic import BaseModel

from .connector_model import ExaConnectorModel
from airbyte_agent_sdk.introspection import describe_entities, generate_tool_description
from airbyte_agent_sdk.translation import DEFAULT_MAX_OUTPUT_CHARS, FrameworkName, translate_exceptions
from airbyte_agent_sdk.types import AirbyteAuthConfig
from .types import (
    ContentsListParams,
    ContentsListParamsSummary,
    SearchResultsListParams,
    SearchResultsListParamsContents,
    SimilarResultsListParams,
    SimilarResultsListParamsContents,
)
from .models import ExaAuthConfig

# Import response models and envelope models at runtime
from .models import (
    ExaCheckResult,
    ExaExecuteResult,
    ExaExecuteResultWithMeta,
    SearchResultsListResult,
    ContentsListResult,
    SimilarResultsListResult,
    SearchResult,
)

# TypeVar for decorator type preservation
_F = TypeVar("_F", bound=Callable[..., Any])




class ExaConnector:
    """
    Type-safe Exa API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "exa"
    connector_version = "1.0.0"
    sdk_version = "0.1.287"

    # Map of (entity, action) -> needs_envelope for envelope wrapping decision
    _ENVELOPE_MAP = {
        ("search_results", "list"): True,
        ("contents", "list"): True,
        ("similar_results", "list"): True,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('search_results', 'list'): {'query': 'query', 'type': 'type', 'category': 'category', 'num_results': 'numResults', 'include_domains': 'includeDomains', 'exclude_domains': 'excludeDomains', 'start_published_date': 'startPublishedDate', 'end_published_date': 'endPublishedDate', 'start_crawl_date': 'startCrawlDate', 'end_crawl_date': 'endCrawlDate', 'contents': 'contents', 'moderation': 'moderation'},
        ('contents', 'list'): {'urls': 'urls', 'text': 'text', 'highlights': 'highlights', 'summary': 'summary'},
        ('similar_results', 'list'): {'url': 'url', 'num_results': 'numResults', 'include_domains': 'includeDomains', 'exclude_domains': 'excludeDomains', 'start_published_date': 'startPublishedDate', 'end_published_date': 'endPublishedDate', 'start_crawl_date': 'startCrawlDate', 'end_crawl_date': 'endCrawlDate', 'contents': 'contents'},
    }

    # Accepted auth_config types for isinstance validation
    _ACCEPTED_AUTH_TYPES = (ExaAuthConfig, AirbyteAuthConfig)

    def __init__(
        self,
        auth_config: ExaAuthConfig | AirbyteAuthConfig | BaseModel | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new exa connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide connector-specific auth config (e.g., ExaAuthConfig)
        - Hosted mode: Provide `AirbyteAuthConfig` with client credentials and either `connector_id` or `workspace_name`

        Args:
            auth_config: Either connector-specific auth config for local mode, or AirbyteAuthConfig for hosted mode
            on_token_refresh: Optional callback for OAuth2 token refresh persistence.
                Called with new_tokens dict when tokens are refreshed. Can be sync or async.
                Example: lambda tokens: save_to_database(tokens)
        Examples:
            # Local mode (direct API calls)
            connector = ExaConnector(auth_config=ExaAuthConfig(api_key="..."))
            # Hosted mode with explicit connector_id (no lookup needed)
            connector = ExaConnector(
                auth_config=AirbyteAuthConfig(
                    airbyte_client_id="client_abc123",
                    airbyte_client_secret="secret_xyz789",
                    connector_id="existing-source-uuid"
                )
            )

            # Hosted mode with lookup by workspace_name
            connector = ExaConnector(
                auth_config=AirbyteAuthConfig(
                    workspace_name="user-123",
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
            from airbyte_agent_sdk.executor import HostedExecutor
            self._executor = HostedExecutor(
                airbyte_client_id=auth_config.airbyte_client_id,
                airbyte_client_secret=auth_config.airbyte_client_secret,
                connector_id=auth_config.connector_id,
                workspace_name=auth_config.workspace_name or "default",
                organization_id=auth_config.organization_id,
                connector_definition_id=str(ExaConnectorModel.id),
                model=ExaConnectorModel,
            )
        else:
            # Local mode: auth_config required (must be connector-specific auth type)
            if not auth_config:
                raise ValueError(
                    "Either provide AirbyteAuthConfig with client credentials for hosted mode, "
                    "or ExaAuthConfig for local mode"
                )

            from airbyte_agent_sdk.executor import LocalExecutor

            # Build config_values dict from server variables
            config_values = None

            self._executor = LocalExecutor(
                model=ExaConnectorModel,
                auth_config=auth_config.model_dump() if auth_config else None,
                config_values=config_values,
                on_token_refresh=on_token_refresh
            )

            # Update base_url with server variables if provided

        # Initialize entity query objects
        self.search_results = SearchResultsQuery(self)
        self.contents = ContentsQuery(self)
        self.similar_results = SimilarResultsQuery(self)

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["search_results"],
        action: Literal["list"],
        params: "SearchResultsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SearchResultsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["contents"],
        action: Literal["list"],
        params: "ContentsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "ContentsListResult": ...

    @overload
    async def execute(
        self,
        entity: Literal["similar_results"],
        action: Literal["list"],
        params: "SimilarResultsListParams",
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> "SimilarResultsListResult": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: Literal["list"],
        params: Mapping[str, Any],
        *,
        select_fields: list[str] | None = ...,
        exclude_fields: list[str] | None = ...,
        skip_truncation: bool = ...
    ) -> ExaExecuteResult[Any] | ExaExecuteResultWithMeta[Any, Any] | Any: ...

    async def execute(
        self,
        entity: str,
        action: Literal["list"],
        params: Mapping[str, Any] | None = None,
        *,
        select_fields: list[str] | None = None,
        exclude_fields: list[str] | None = None,
        skip_truncation: bool = True
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
            select_fields: Optional allowlist of dot-notation fields to include
            exclude_fields: Optional blocklist of dot-notation fields to remove
            skip_truncation: Disable long-text truncation for collection actions

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                entity="customers",
                action="get",
                params={"id": "cus_123"}
            )
        """
        from airbyte_agent_sdk.executor import ExecutionConfig

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
            params=resolved_params,
            select_fields=select_fields,
            exclude_fields=exclude_fields,
            skip_truncation=skip_truncation
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        # Check if this operation has extractors configured
        has_extractors = self._ENVELOPE_MAP.get((entity, action), False)

        if has_extractors:
            # With extractors - return Pydantic envelope with data and meta
            if result.meta is not None:
                return ExaExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return ExaExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data

    # ===== HEALTH CHECK METHOD =====

    async def check(self) -> ExaCheckResult:
        """
        Perform a health check to verify connectivity and credentials.

        Executes a lightweight list operation (limit=1) to validate that
        the connector can communicate with the API and credentials are valid.

        Returns:
            ExaCheckResult with status ("healthy" or "unhealthy") and optional error message

        Example:
            result = await connector.check()
            if result.status == "healthy":
                print("Connection verified!")
            else:
                print(f"Check failed: {result.error}")
        """
        result = await self._executor.check()

        if result.success and isinstance(result.data, dict):
            return ExaCheckResult(
                status=result.data.get("status", "unhealthy"),
                error=result.data.get("error"),
                checked_entity=result.data.get("checked_entity"),
                checked_action=result.data.get("checked_action"),
            )
        else:
            return ExaCheckResult(
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
        max_output_chars: int | None = DEFAULT_MAX_OUTPUT_CHARS,
        framework: FrameworkName | None = None,
        internal_retries: int = 0,
        should_internal_retry: Callable[[Exception, tuple[Any, ...], dict[str, Any]], bool] | None = None,
        exhausted_runtime_failure_message: Callable[[Exception, tuple[Any, ...], dict[str, Any]], str | None] | None = None,
    ) -> _F | Callable[[_F], _F]:
        """
        Add connector-specific documentation and runtime safeguards to one tool.

        For new agents, prefer `build_connector_tools`. It returns progressive
        `inspect_connector`, `read_skill_docs`, and `execute` tools so the agent
        can load only the connector guidance it needs:

        ```python
        from airbyte_agent_sdk import build_connector_tools
        from pydantic_ai import Agent

        tools = build_connector_tools(connector, framework="pydantic_ai")
        agent = Agent("openai:gpt-4o", tools=tools.as_list())
        ```

        ### Legacy: one generated-description tool

        Existing integrations can keep using `tool_utils` for one broad
        `execute` tool with the connector's full generated catalog in its
        description:

        ```python
        from fastmcp import FastMCP

        connector = ExaConnector()
        mcp = FastMCP("Connector Agent")

        @mcp.tool()
        @ExaConnector.tool_utils
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        Configure documentation, output limits, framework translation, and
        retries when needed:

        ```python
        @mcp.tool()
        @ExaConnector.tool_utils(update_docstring=False, max_output_chars=None)
        async def execute(entity: str, action: str, params: dict):
            ...

        @mcp.tool()
        @ExaConnector.tool_utils(framework="pydantic_ai", internal_retries=2)
        async def execute(entity: str, action: str, params: dict):
            ...
        ```

        This decorator composes `translate_exceptions` for runtime wrapping,
        output-size checks, framework signal translation, and optional internal
        retries, then adds connector-specific docstring augmentation.

        Args:
            update_docstring: When True, append connector capabilities to `__doc__`.
            max_output_chars: Max serialized output size before raising. Use `None` to disable.
            framework: One of `"pydantic_ai" | "langchain" | "openai_agents" | "mcp"`.
                Defaults to `None`, which auto-detects each framework's canonical
                import in order. Explicit always wins.
            internal_retries: How many transient runtime failures (429/5xx, network,
                timeout) to retry silently before surfacing. Default 0. Forwarded to
                `airbyte_agent_sdk.translation.translate_exceptions`.
            should_internal_retry: Optional predicate `(error, args, kwargs) -> bool`
                further restricting which retryable errors are safe for this specific
                tool. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
            exhausted_runtime_failure_message: Optional callback
                `(error, args, kwargs) -> str | None`. Invoked after internal retries
                are exhausted or were skipped because `should_internal_retry` returned
                `False`. Forwarded to `airbyte_agent_sdk.translation.translate_exceptions`.
        """

        def decorate(inner: _F) -> _F:
            if update_docstring:
                description = generate_tool_description(
                    ExaConnectorModel,
                )
                original_doc = inner.__doc__ or ""
                if original_doc.strip():
                    full_doc = f"{original_doc.strip()}\n{description}"
                else:
                    full_doc = description
            else:
                full_doc = ""

            wrapped = translate_exceptions(
                inner,
                framework=framework,
                max_output_chars=max_output_chars,
                internal_retries=internal_retries,
                should_internal_retry=should_internal_retry,
                exhausted_runtime_failure_message=exhausted_runtime_failure_message,
            )

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
        return describe_entities(ExaConnectorModel)

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
            (e for e in ExaConnectorModel.entities if e.name == entity),
            None
        )
        if entity_def is None:
            logging.getLogger(__name__).warning(
                f"Entity '{entity}' not found. Available entities: "
                f"{[e.name for e in ExaConnectorModel.entities]}"
            )
        return entity_def.entity_schema if entity_def else None

    @property
    def connector_id(self) -> str | None:
        """Get the connector/source ID (only available in hosted mode).

        Returns:
            The connector ID if in hosted mode, None if in local mode.
        """
        if hasattr(self, '_executor') and hasattr(self._executor, '_connector_id'):
            return self._executor._connector_id
        return None

    # ===== RESOURCE MANAGEMENT =====

    async def close(self):
        """Close the connector and release resources."""
        await self._executor.close()

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()



class SearchResultsQuery:
    """
    Query class for SearchResults entity operations.
    """

    def __init__(self, connector: ExaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        query: str,
        type: str | None = None,
        category: str | None = None,
        num_results: int | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        start_published_date: str | None = None,
        end_published_date: str | None = None,
        start_crawl_date: str | None = None,
        end_crawl_date: str | None = None,
        contents: SearchResultsListParamsContents | None = None,
        moderation: bool | None = None,
        **kwargs
    ) -> SearchResultsListResult:
        """
        Perform a search with an Exa prompt-engineered query and retrieve a list
of relevant results. Optionally request contents (text, highlights, summary)
inline with the search results. Supports filtering by domain, date, category,
and number of results.


        Args:
            query: The search query string.
            type: The type of search. auto intelligently selects the best mode, instant provides lowest latency, fast uses lower-latency models, deep-lite provides lightweight synthesis, deep performs in-depth research with synthesis, and deep-reasoning adds more reasoning for complex searches.
            category: A data category to focus on for improved result quality.
            num_results: Number of results to return (max 100).
            include_domains: List of domains to include. If specified, results will only come from these domains.
            exclude_domains: List of domains to exclude. If specified, no results will be returned from these domains.
            start_published_date: Only return links published after this date. ISO 8601 format.
            end_published_date: Only return links published before this date. ISO 8601 format.
            start_crawl_date: Only return links crawled by Exa after this date. ISO 8601 format.
            end_crawl_date: Only return links crawled by Exa before this date. ISO 8601 format.
            contents: Options for requesting page contents inline with search results.
            moderation: Enable content moderation to filter unsafe content.
            **kwargs: Additional parameters

        Returns:
            SearchResultsListResult
        """
        params = {k: v for k, v in {
            "query": query,
            "type": type,
            "category": category,
            "numResults": num_results,
            "includeDomains": include_domains,
            "excludeDomains": exclude_domains,
            "startPublishedDate": start_published_date,
            "endPublishedDate": end_published_date,
            "startCrawlDate": start_crawl_date,
            "endCrawlDate": end_crawl_date,
            "contents": contents,
            "moderation": moderation,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("search_results", "list", params)
        # Cast generic envelope to concrete typed result
        return SearchResultsListResult(
            data=result.data
        )



class ContentsQuery:
    """
    Query class for Contents entity operations.
    """

    def __init__(self, connector: ExaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        urls: list[str],
        text: Any | None = None,
        highlights: Any | None = None,
        summary: ContentsListParamsSummary | None = None,
        **kwargs
    ) -> ContentsListResult:
        """
        Get the full page contents, summaries, and metadata for a list of URLs.
Returns instant results from Exa's cache, with automatic live crawling
as fallback for uncached pages. Use this to retrieve text, highlights,
and summaries for specific URLs.


        Args:
            urls: Array of URLs to retrieve contents for.
            text: Text extraction options. Pass true for defaults or an object for advanced options.
            highlights: Highlight extraction options. Pass true for defaults or an object for advanced options.
            summary: Summary generation options.
            **kwargs: Additional parameters

        Returns:
            ContentsListResult
        """
        params = {k: v for k, v in {
            "urls": urls,
            "text": text,
            "highlights": highlights,
            "summary": summary,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("contents", "list", params)
        # Cast generic envelope to concrete typed result
        return ContentsListResult(
            data=result.data
        )



class SimilarResultsQuery:
    """
    Query class for SimilarResults entity operations.
    """

    def __init__(self, connector: ExaConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        url: str,
        num_results: int | None = None,
        include_domains: list[str] | None = None,
        exclude_domains: list[str] | None = None,
        start_published_date: str | None = None,
        end_published_date: str | None = None,
        start_crawl_date: str | None = None,
        end_crawl_date: str | None = None,
        contents: SimilarResultsListParamsContents | None = None,
        **kwargs
    ) -> SimilarResultsListResult:
        """
        Find web pages similar to a given URL. Uses Exa's embeddings to find
semantically similar content. Supports filtering by domains and dates.


        Args:
            url: The URL to find similar pages for.
            num_results: Number of similar results to return (max 100).
            include_domains: List of domains to include. If specified, results will only come from these domains.
            exclude_domains: List of domains to exclude. If specified, no results will be returned from these domains.
            start_published_date: Only return links published after this date. ISO 8601 format.
            end_published_date: Only return links published before this date. ISO 8601 format.
            start_crawl_date: Only return links crawled by Exa after this date. ISO 8601 format.
            end_crawl_date: Only return links crawled by Exa before this date. ISO 8601 format.
            contents: Options for requesting page contents inline with similar page results.
            **kwargs: Additional parameters

        Returns:
            SimilarResultsListResult
        """
        params = {k: v for k, v in {
            "url": url,
            "numResults": num_results,
            "includeDomains": include_domains,
            "excludeDomains": exclude_domains,
            "startPublishedDate": start_published_date,
            "endPublishedDate": end_published_date,
            "startCrawlDate": start_crawl_date,
            "endCrawlDate": end_crawl_date,
            "contents": contents,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("similar_results", "list", params)
        # Cast generic envelope to concrete typed result
        return SimilarResultsListResult(
            data=result.data
        )


