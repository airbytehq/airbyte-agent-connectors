"""
greenhouse connector.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, AsyncIterator, overload
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pathlib import Path

from .types import (
    ApplicationAttachmentDownloadParams,
    ApplicationsGetParams,
    ApplicationsListParams,
    CandidateAttachmentDownloadParams,
    CandidatesGetParams,
    CandidatesListParams,
    DepartmentsGetParams,
    DepartmentsListParams,
    JobPostsGetParams,
    JobPostsListParams,
    JobsGetParams,
    JobsListParams,
    OffersGetParams,
    OffersListParams,
    OfficesGetParams,
    OfficesListParams,
    ScheduledInterviewsGetParams,
    ScheduledInterviewsListParams,
    SourcesListParams,
    UsersGetParams,
    UsersListParams,
)

if TYPE_CHECKING:
    from .models import GreenhouseAuthConfig
# Import response models and envelope models at runtime
from .models import (
    GreenhouseExecuteResult,
    GreenhouseExecuteResultWithMeta,
    Application,
    Candidate,
    Department,
    Job,
    JobPost,
    Offer,
    Office,
    ScheduledInterview,
    User,
)


class GreenhouseConnector:
    """
    Type-safe Greenhouse API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "greenhouse"
    connector_version = "0.1.1"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    # Map of (entity, action) -> has_extractors for envelope wrapping decision
    _EXTRACTOR_MAP = {
        ("candidates", "list"): False,
        ("candidates", "get"): False,
        ("applications", "list"): False,
        ("applications", "get"): False,
        ("jobs", "list"): False,
        ("jobs", "get"): False,
        ("offers", "list"): False,
        ("offers", "get"): False,
        ("users", "list"): False,
        ("users", "get"): False,
        ("departments", "list"): False,
        ("departments", "get"): False,
        ("offices", "list"): False,
        ("offices", "get"): False,
        ("job_posts", "list"): False,
        ("job_posts", "get"): False,
        ("sources", "list"): False,
        ("scheduled_interviews", "list"): False,
        ("scheduled_interviews", "get"): False,
        ("application_attachment", "download"): False,
        ("candidate_attachment", "download"): False,
    }

    # Map of (entity, action) -> {python_param_name: api_param_name}
    # Used to convert snake_case TypedDict keys to API parameter names in execute()
    _PARAM_MAP = {
        ('candidates', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('candidates', 'get'): {'id': 'id'},
        ('applications', 'list'): {'per_page': 'per_page', 'page': 'page', 'created_before': 'created_before', 'created_after': 'created_after', 'last_activity_after': 'last_activity_after', 'job_id': 'job_id', 'status': 'status'},
        ('applications', 'get'): {'id': 'id'},
        ('jobs', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('jobs', 'get'): {'id': 'id'},
        ('offers', 'list'): {'per_page': 'per_page', 'page': 'page', 'created_before': 'created_before', 'created_after': 'created_after', 'resolved_after': 'resolved_after'},
        ('offers', 'get'): {'id': 'id'},
        ('users', 'list'): {'per_page': 'per_page', 'page': 'page', 'created_before': 'created_before', 'created_after': 'created_after', 'updated_before': 'updated_before', 'updated_after': 'updated_after'},
        ('users', 'get'): {'id': 'id'},
        ('departments', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('departments', 'get'): {'id': 'id'},
        ('offices', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('offices', 'get'): {'id': 'id'},
        ('job_posts', 'list'): {'per_page': 'per_page', 'page': 'page', 'live': 'live', 'active': 'active'},
        ('job_posts', 'get'): {'id': 'id'},
        ('sources', 'list'): {'per_page': 'per_page', 'page': 'page'},
        ('scheduled_interviews', 'list'): {'per_page': 'per_page', 'page': 'page', 'created_before': 'created_before', 'created_after': 'created_after', 'updated_before': 'updated_before', 'updated_after': 'updated_after', 'starts_after': 'starts_after', 'ends_before': 'ends_before'},
        ('scheduled_interviews', 'get'): {'id': 'id'},
        ('application_attachment', 'download'): {'id': 'id', 'attachment_index': 'attachment_index', 'range_header': 'range_header'},
        ('candidate_attachment', 'download'): {'id': 'id', 'attachment_index': 'attachment_index', 'range_header': 'range_header'},
    }

    def __init__(
        self,
        auth_config: GreenhouseAuthConfig | None = None,
        config_path: str | None = None,
        connector_id: str | None = None,
        airbyte_client_id: str | None = None,
        airbyte_client_secret: str | None = None,
        airbyte_connector_api_url: str | None = None,
        on_token_refresh: Any | None = None    ):
        """
        Initialize a new greenhouse connector instance.

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
            connector = GreenhouseConnector(auth_config=GreenhouseAuthConfig(api_key="..."))
            # Hosted mode (executed on Airbyte cloud)
            connector = GreenhouseConnector(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )

            # Local mode with OAuth2 token refresh callback
            def save_tokens(new_tokens: dict) -> None:
                # Persist updated tokens to your storage (file, database, etc.)
                with open("tokens.json", "w") as f:
                    json.dump(new_tokens, f)

            connector = GreenhouseConnector(
                auth_config=GreenhouseAuthConfig(access_token="...", refresh_token="..."),
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
        self.candidates = CandidatesQuery(self)
        self.applications = ApplicationsQuery(self)
        self.jobs = JobsQuery(self)
        self.offers = OffersQuery(self)
        self.users = UsersQuery(self)
        self.departments = DepartmentsQuery(self)
        self.offices = OfficesQuery(self)
        self.job_posts = JobPostsQuery(self)
        self.sources = SourcesQuery(self)
        self.scheduled_interviews = ScheduledInterviewsQuery(self)
        self.application_attachment = ApplicationAttachmentQuery(self)
        self.candidate_attachment = CandidateAttachmentQuery(self)

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====

    @overload
    async def execute(
        self,
        entity: Literal["candidates"],
        action: Literal["list"],
        params: "CandidatesListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["candidates"],
        action: Literal["get"],
        params: "CandidatesGetParams"
    ) -> "Candidate": ...

    @overload
    async def execute(
        self,
        entity: Literal["applications"],
        action: Literal["list"],
        params: "ApplicationsListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["applications"],
        action: Literal["get"],
        params: "ApplicationsGetParams"
    ) -> "Application": ...

    @overload
    async def execute(
        self,
        entity: Literal["jobs"],
        action: Literal["list"],
        params: "JobsListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["jobs"],
        action: Literal["get"],
        params: "JobsGetParams"
    ) -> "Job": ...

    @overload
    async def execute(
        self,
        entity: Literal["offers"],
        action: Literal["list"],
        params: "OffersListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["offers"],
        action: Literal["get"],
        params: "OffersGetParams"
    ) -> "Offer": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["list"],
        params: "UsersListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["users"],
        action: Literal["get"],
        params: "UsersGetParams"
    ) -> "User": ...

    @overload
    async def execute(
        self,
        entity: Literal["departments"],
        action: Literal["list"],
        params: "DepartmentsListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["departments"],
        action: Literal["get"],
        params: "DepartmentsGetParams"
    ) -> "Department": ...

    @overload
    async def execute(
        self,
        entity: Literal["offices"],
        action: Literal["list"],
        params: "OfficesListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["offices"],
        action: Literal["get"],
        params: "OfficesGetParams"
    ) -> "Office": ...

    @overload
    async def execute(
        self,
        entity: Literal["job_posts"],
        action: Literal["list"],
        params: "JobPostsListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["job_posts"],
        action: Literal["get"],
        params: "JobPostsGetParams"
    ) -> "JobPost": ...

    @overload
    async def execute(
        self,
        entity: Literal["sources"],
        action: Literal["list"],
        params: "SourcesListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["scheduled_interviews"],
        action: Literal["list"],
        params: "ScheduledInterviewsListParams"
    ) -> "dict[str, Any]": ...

    @overload
    async def execute(
        self,
        entity: Literal["scheduled_interviews"],
        action: Literal["get"],
        params: "ScheduledInterviewsGetParams"
    ) -> "ScheduledInterview": ...

    @overload
    async def execute(
        self,
        entity: Literal["application_attachment"],
        action: Literal["download"],
        params: "ApplicationAttachmentDownloadParams"
    ) -> "AsyncIterator[bytes]": ...

    @overload
    async def execute(
        self,
        entity: Literal["candidate_attachment"],
        action: Literal["download"],
        params: "CandidateAttachmentDownloadParams"
    ) -> "AsyncIterator[bytes]": ...


    @overload
    async def execute(
        self,
        entity: str,
        action: str,
        params: dict[str, Any]
    ) -> GreenhouseExecuteResult[Any] | GreenhouseExecuteResultWithMeta[Any, Any] | Any: ...

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
                return GreenhouseExecuteResultWithMeta[Any, Any](
                    data=result.data,
                    meta=result.meta
                )
            else:
                return GreenhouseExecuteResult[Any](data=result.data)
        else:
            # No extractors - return raw response data
            return result.data



class CandidatesQuery:
    """
    Query class for Candidates entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a paginated list of all candidates in the organization

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("candidates", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Candidate:
        """
        Get a single candidate by ID

        Args:
            id: Candidate ID
            **kwargs: Additional parameters

        Returns:
            Candidate
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("candidates", "get", params)
        return result



class ApplicationsQuery:
    """
    Query class for Applications entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        last_activity_after: str | None = None,
        job_id: int | None = None,
        status: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a paginated list of all applications

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            created_before: Filter by applications created before this timestamp
            created_after: Filter by applications created after this timestamp
            last_activity_after: Filter by applications with activity after this timestamp
            job_id: Filter by job ID
            status: Filter by application status
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "created_before": created_before,
            "created_after": created_after,
            "last_activity_after": last_activity_after,
            "job_id": job_id,
            "status": status,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("applications", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Application:
        """
        Get a single application by ID

        Args:
            id: Application ID
            **kwargs: Additional parameters

        Returns:
            Application
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("applications", "get", params)
        return result



class JobsQuery:
    """
    Query class for Jobs entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a paginated list of all jobs in the organization

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("jobs", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Job:
        """
        Get a single job by ID

        Args:
            id: Job ID
            **kwargs: Additional parameters

        Returns:
            Job
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("jobs", "get", params)
        return result



class OffersQuery:
    """
    Query class for Offers entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        resolved_after: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a paginated list of all offers

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            created_before: Filter by offers created before this timestamp
            created_after: Filter by offers created after this timestamp
            resolved_after: Filter by offers resolved after this timestamp
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "created_before": created_before,
            "created_after": created_after,
            "resolved_after": resolved_after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("offers", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Offer:
        """
        Get a single offer by ID

        Args:
            id: Offer ID
            **kwargs: Additional parameters

        Returns:
            Offer
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("offers", "get", params)
        return result



class UsersQuery:
    """
    Query class for Users entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        updated_before: str | None = None,
        updated_after: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a paginated list of all users

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            created_before: Filter by users created before this timestamp
            created_after: Filter by users created after this timestamp
            updated_before: Filter by users updated before this timestamp
            updated_after: Filter by users updated after this timestamp
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "created_before": created_before,
            "created_after": created_after,
            "updated_before": updated_before,
            "updated_after": updated_after,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> User:
        """
        Get a single user by ID

        Args:
            id: User ID
            **kwargs: Additional parameters

        Returns:
            User
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("users", "get", params)
        return result



class DepartmentsQuery:
    """
    Query class for Departments entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a paginated list of all departments

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("departments", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Department:
        """
        Get a single department by ID

        Args:
            id: Department ID
            **kwargs: Additional parameters

        Returns:
            Department
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("departments", "get", params)
        return result



class OfficesQuery:
    """
    Query class for Offices entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a paginated list of all offices

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("offices", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> Office:
        """
        Get a single office by ID

        Args:
            id: Office ID
            **kwargs: Additional parameters

        Returns:
            Office
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("offices", "get", params)
        return result



class JobPostsQuery:
    """
    Query class for JobPosts entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        live: bool | None = None,
        active: bool | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a paginated list of all job posts

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            live: Filter by live status
            active: Filter by active status
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "live": live,
            "active": active,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("job_posts", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> JobPost:
        """
        Get a single job post by ID

        Args:
            id: Job Post ID
            **kwargs: Additional parameters

        Returns:
            JobPost
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("job_posts", "get", params)
        return result



class SourcesQuery:
    """
    Query class for Sources entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a paginated list of all sources

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("sources", "list", params)
        return result



class ScheduledInterviewsQuery:
    """
    Query class for ScheduledInterviews entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: int | None = None,
        page: int | None = None,
        created_before: str | None = None,
        created_after: str | None = None,
        updated_before: str | None = None,
        updated_after: str | None = None,
        starts_after: str | None = None,
        ends_before: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Returns a paginated list of all scheduled interviews

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            created_before: Filter by interviews created before this timestamp
            created_after: Filter by interviews created after this timestamp
            updated_before: Filter by interviews updated before this timestamp
            updated_after: Filter by interviews updated after this timestamp
            starts_after: Filter by interviews starting after this timestamp
            ends_before: Filter by interviews ending before this timestamp
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "created_before": created_before,
            "created_after": created_after,
            "updated_before": updated_before,
            "updated_after": updated_after,
            "starts_after": starts_after,
            "ends_before": ends_before,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("scheduled_interviews", "list", params)
        return result



    async def get(
        self,
        id: str | None = None,
        **kwargs
    ) -> ScheduledInterview:
        """
        Get a single scheduled interview by ID

        Args:
            id: Scheduled Interview ID
            **kwargs: Additional parameters

        Returns:
            ScheduledInterview
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("scheduled_interviews", "get", params)
        return result



class ApplicationAttachmentQuery:
    """
    Query class for ApplicationAttachment entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def download(
        self,
        attachment_index: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads an attachment (resume, cover letter, etc.) for an application by index.
The attachment URL is a temporary signed AWS S3 URL that expires within 7 days.
Files should be downloaded immediately after retrieval.


        Args:
            id: Application ID
            attachment_index: Index of the attachment to download (0-based)
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "id": id,
            "attachment_index": attachment_index,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("application_attachment", "download", params)
        return result


    async def download_local(
        self,
        attachment_index: str,
        path: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads an attachment (resume, cover letter, etc.) for an application by index.
The attachment URL is a temporary signed AWS S3 URL that expires within 7 days.
Files should be downloaded immediately after retrieval.
 and save to file.

        Args:
            id: Application ID
            attachment_index: Index of the attachment to download (0-based)
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
            attachment_index=attachment_index,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)


class CandidateAttachmentQuery:
    """
    Query class for CandidateAttachment entity operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def download(
        self,
        attachment_index: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> AsyncIterator[bytes]:
        """
        Downloads an attachment (resume, cover letter, etc.) for a candidate by index.
The attachment URL is a temporary signed AWS S3 URL that expires within 7 days.
Files should be downloaded immediately after retrieval.


        Args:
            id: Candidate ID
            attachment_index: Index of the attachment to download (0-based)
            range_header: Optional Range header for partial downloads (e.g., 'bytes=0-99')
            **kwargs: Additional parameters

        Returns:
            AsyncIterator[bytes]
        """
        params = {k: v for k, v in {
            "id": id,
            "attachment_index": attachment_index,
            "range_header": range_header,
            **kwargs
        }.items() if v is not None}

        result = await self._connector.execute("candidate_attachment", "download", params)
        return result


    async def download_local(
        self,
        attachment_index: str,
        path: str,
        id: str | None = None,
        range_header: str | None = None,
        **kwargs
    ) -> Path:
        """
        Downloads an attachment (resume, cover letter, etc.) for a candidate by index.
The attachment URL is a temporary signed AWS S3 URL that expires within 7 days.
Files should be downloaded immediately after retrieval.
 and save to file.

        Args:
            id: Candidate ID
            attachment_index: Index of the attachment to download (0-based)
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
            attachment_index=attachment_index,
            range_header=range_header,
            **kwargs
        )

        return await save_download(content_iterator, path)

