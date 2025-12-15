"""Authentication strategy pattern implementation for HTTP client."""

from __future__ import annotations

import base64
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Literal, TypedDict

import httpx
from jinja2 import Template

from .secrets import SecretStr

from .exceptions import AuthenticationError
from .types import AuthType

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)


def extract_secret_value(value: SecretStr | str | None) -> str:
    """Extract the actual value from SecretStr or return plain string.

    This utility function handles the common pattern of extracting secret values
    that can be either SecretStr (wrapped) or plain str values.

    Note:
        Accepts None and returns empty string for convenience when accessing
        optional TypedDict fields. This avoids repetitive None checks in callers
        when building headers/bodies where missing optional fields should use "".

    Args:
        value: A SecretStr, plain string, or None

    Returns:
        The unwrapped string value, or empty string if None

    Examples:
        >>> extract_secret_value(SecretStr("my_secret"))
        'my_secret'
        >>> extract_secret_value("plain_value")
        'plain_value'
        >>> extract_secret_value(None)
        ''
    """
    if isinstance(value, SecretStr):
        return value.get_secret_value()
    return str(value) if value else ""


# TypedDict definitions for auth strategy configurations and secrets


class APIKeyAuthConfig(TypedDict, total=False):
    """Configuration for API key authentication.

    Attributes:
        header: Header name to use (default: "Authorization")
        prefix: Prefix for the header value (default: "Bearer")
    """

    header: str
    prefix: str


class APIKeyAuthSecrets(TypedDict):
    """Required secrets for API key authentication.

    Attributes:
        api_key: The API key credential
    """

    api_key: SecretStr | str


class BearerAuthConfig(TypedDict, total=False):
    """Configuration for Bearer token authentication.

    Attributes:
        header: Header name to use (default: "Authorization")
        prefix: Prefix for the header value (default: "Bearer")
    """

    header: str
    prefix: str


class BearerAuthSecrets(TypedDict, total=False):
    """Required secrets for Bearer authentication.

    Attributes:
        token: The bearer token (can be SecretStr or plain str, will be converted as needed)
    """

    token: SecretStr | str


class BasicAuthSecrets(TypedDict):
    """Required secrets for HTTP Basic authentication.

    Attributes:
        username: The username credential
        password: The password credential
    """

    username: SecretStr | str
    password: SecretStr | str


# Type aliases for OAuth2 configuration options
AuthStyle = Literal["basic", "body", "none"]
BodyFormat = Literal["form", "json"]


class OAuth2AuthConfig(TypedDict, total=False):
    """Configuration for OAuth 2.0 authentication.

    All fields are optional with sensible defaults. Used to customize OAuth2
    authentication behavior for different APIs.

    Attributes:
        header: Header name to use (default: "Authorization")
            Example: "X-OAuth-Token" for custom header names

        prefix: Prefix for the header value (default: "Bearer")
            Example: "Token" for APIs that use "Token {access_token}"

        refresh_url: Token refresh endpoint URL (supports Jinja2 {{templates}})
            Required for token refresh functionality.
            Example: "https://{{subdomain}}.zendesk.com/oauth/tokens"
            If template variables are used but not provided, they render as empty strings.

        auth_style: How to send client credentials during token refresh
            - "basic": client_id:client_secret in Basic Auth header (RFC 6749 compliant)
            - "body": credentials in request body (default, widely supported)
            - "none": no client credentials sent (public clients)
            Default: "body"

        body_format: Request body encoding for token refresh
            - "form": application/x-www-form-urlencoded (default, RFC 6749 standard)
            - "json": application/json (some APIs prefer this)
            Default: "form"

        subdomain: Template variable for multi-tenant APIs (e.g., Zendesk)
            Used in refresh_url templates like "https://{{subdomain}}.example.com"
            If not provided and used in template, renders as empty string.

            Note: Any config key can be used as a template variable in refresh_url.
            Common patterns: subdomain (Zendesk), shop (Shopify), region (AWS-style APIs).

    Examples:
        GitHub (simple):
            {"header": "Authorization", "prefix": "Bearer"}

        Zendesk (with subdomain):
            {
                "refresh_url": "https://{{subdomain}}.zendesk.com/oauth/tokens",
                "subdomain": "mycompany",
                "auth_style": "body"
            }

        Custom API (JSON body, basic auth):
            {
                "refresh_url": "https://api.example.com/token",
                "auth_style": "basic",
                "body_format": "json"
            }
    """

    header: str
    prefix: str
    refresh_url: str
    auth_style: AuthStyle
    body_format: BodyFormat
    subdomain: str


class OAuth2AuthSecrets(TypedDict):
    """Required secrets for OAuth 2.0 authentication.

    Minimum secrets needed to make authenticated requests. The access_token
    is the only required field for basic OAuth2 authentication.

    Attributes:
        access_token: The OAuth2 access token (REQUIRED)
            This is the credential used to authenticate API requests.
            Can be either a SecretStr (recommended) or plain string.

    Examples:
        Basic usage with string:
            {"access_token": "gho_abc123xyz..."}

        Secure usage with SecretStr:
            {"access_token": SecretStr("gho_abc123xyz...")}
    """

    access_token: SecretStr | str


class OAuth2RefreshSecrets(OAuth2AuthSecrets, total=False):
    """Extended OAuth2 secrets including optional refresh-related fields.

    Inherits the required access_token from OAuth2AuthSecrets and adds
    optional fields needed for automatic token refresh when access_token expires.

    Note on typing:
        This class uses `total=False` which makes all fields defined HERE optional.
        The inherited `access_token` from OAuth2AuthSecrets remains REQUIRED.
        Optional fields may be absent from the dict entirely (checked via `.get()`).
        TypedDict is a static typing construct only - runtime validation uses `.get()`.

    Token refresh will be attempted automatically on 401 errors if:
    1. refresh_token is provided
    2. refresh_url is configured in OAuth2AuthConfig
    3. The API returns a 401 Unauthorized response

    Attributes:
        refresh_token (optional): Token used to obtain new access_token.
            Required for automatic token refresh functionality.
            Some OAuth2 flows (e.g., client_credentials) don't provide this.

        client_id (optional): OAuth2 client ID for refresh requests.
            Required for most token refresh requests.
            How it's sent depends on auth_style config.

        client_secret (optional): OAuth2 client secret for refresh requests.
            Required for confidential clients.
            Public clients (mobile apps, SPAs) may not have this.

        token_type (optional): Token type, defaults to "Bearer".
            Usually "Bearer" per RFC 6750.
            Some APIs use different types like "Token" or "MAC".

    Examples:
        Full refresh capability:
            {
                "access_token": "eyJhbGc...",
                "refresh_token": "def502...",
                "client_id": "my_client_id",
                "client_secret": SecretStr("my_secret"),
                "token_type": "Bearer"
            }

        Public client (no secret):
            {
                "access_token": "eyJhbGc...",
                "refresh_token": "def502...",
                "client_id": "mobile_app_id"
            }

        No refresh (access_token only):
            {
                "access_token": "long_lived_token"
            }
    """

    refresh_token: SecretStr | str
    client_id: SecretStr | str
    client_secret: SecretStr | str
    token_type: str


@dataclass
class TokenRefreshResult:
    """Result of an OAuth2 token refresh operation.

    Attributes:
        tokens: Dictionary containing access_token, refresh_token, token_type
        extracted_values: Optional dictionary of values extracted from token response
            for server variable substitution (e.g., instance_url for Salesforce)
    """

    tokens: dict[str, str]
    extracted_values: dict[str, str] | None = None


class AuthStrategy(ABC):
    """Abstract base class for authentication strategies."""

    @abstractmethod
    def inject_auth(
        self,
        headers: dict[str, str],
        config: dict[str, Any],
        secrets: dict[str, SecretStr | str],
    ) -> dict[str, str]:
        """
        Inject authentication credentials into request headers.

        This method creates a copy of the headers dict and adds authentication.
        The original headers dict is not modified.

        Args:
            headers: Existing request headers (will not be modified)
            config: Authentication configuration from AuthConfig.config
            secrets: Secret credentials dictionary (SecretStr or plain str values)

        Returns:
            New headers dictionary with authentication injected (original unchanged)

        Raises:
            AuthenticationError: If required credentials are missing
        """
        pass

    @abstractmethod
    def validate_credentials(self, secrets: dict[str, SecretStr | str]) -> None:
        """
        Validate that required credentials are present.

        Args:
            secrets: Secret credentials dictionary with SecretStr values

        Raises:
            AuthenticationError: If required credentials are missing
        """
        pass

    async def handle_auth_error(
        self,
        status_code: int,
        config: dict[str, Any],
        secrets: dict[str, Any],
        config_values: dict[str, str] | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> TokenRefreshResult | None:
        """
        Handle authentication error and attempt recovery (e.g., token refresh).

        This method is called by HTTPClient when an authentication error occurs.
        Strategies that support credential refresh (like OAuth2) can override this
        to implement their refresh logic.

        Args:
            status_code: HTTP status code of the auth error (e.g., 401, 403)
            config: Authentication configuration from AuthConfig.config
            secrets: Secret credentials dictionary (may be updated)
            config_values: Non-secret configuration values (e.g., {"subdomain": "mycompany"})
                Used for template variable substitution in refresh URLs.
            http_client: Optional httpx.AsyncClient for making refresh requests.
                If provided, will be reused; otherwise a new client is created.

        Returns:
            TokenRefreshResult with new credentials if refresh successful, None otherwise.
            The tokens dict will be merged into the secrets dict by the caller.

        Note:
            Default implementation returns None (no refresh capability).
            Strategies with refresh capability should override this method.
        """
        return None

    async def ensure_credentials(
        self,
        config: dict[str, Any],
        secrets: dict[str, Any],
        config_values: dict[str, str] | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> TokenRefreshResult | None:
        """
        Ensure credentials are ready for authentication.

        This method is called before the first API request to allow
        strategies to proactively obtain credentials (e.g., OAuth2 token refresh
        when starting with only a refresh_token).

        Args:
            config: Authentication configuration from AuthConfig.config
            secrets: Secret credentials dictionary (may be updated by caller)
            config_values: Non-secret configuration values for template substitution
            http_client: Optional httpx.AsyncClient for making requests

        Returns:
            TokenRefreshResult with new/updated credentials if changes were made, None otherwise.
            The tokens dict should be merged into the secrets dict by the caller.

        Note:
            Default implementation returns None (no initialization needed).
            Strategies like OAuth2 can override this for proactive token refresh.
        """
        return None


class APIKeyAuthStrategy(AuthStrategy):
    """Strategy for API key authentication."""

    def inject_auth(
        self,
        headers: dict[str, str],
        config: APIKeyAuthConfig,
        secrets: APIKeyAuthSecrets,
    ) -> dict[str, str]:
        """Inject API key into headers.

        Creates a copy of the headers dict with the API key added.
        The original headers dict is not modified.

        Args:
            headers: Existing request headers (will not be modified)
            config: API key authentication configuration
            secrets: API key credentials

        Returns:
            New headers dict with API key authentication injected
        """
        headers = headers.copy()

        # Get configuration with defaults
        header_name = config.get("header", "Authorization")
        prefix = config.get("prefix", "")

        # Get API key from secrets
        api_key = secrets.get("api_key")
        if not api_key:
            raise AuthenticationError("Missing 'api_key' in secrets")

        # Extract secret value (handle both SecretStr and plain str)
        api_key_value = extract_secret_value(api_key)

        # Inject into headers
        if prefix:
            headers[header_name] = f"{prefix} {api_key_value}"
        else:
            headers[header_name] = api_key_value
        return headers

    def validate_credentials(self, secrets: APIKeyAuthSecrets) -> None:  # type: ignore[override]
        """Validate API key is present.

        Args:
            secrets: API key credentials to validate
        """
        if not secrets.get("api_key"):
            raise AuthenticationError("Missing 'api_key' in secrets")


class BearerAuthStrategy(AuthStrategy):
    """Strategy for Bearer token authentication."""

    def inject_auth(
        self,
        headers: dict[str, str],
        config: BearerAuthConfig,
        secrets: BearerAuthSecrets,
    ) -> dict[str, str]:
        """Inject Bearer token into headers.

        Creates a copy of the headers dict with the Bearer token added.
        The original headers dict is not modified.

        Args:
            headers: Existing request headers (will not be modified)
            config: Bearer authentication configuration
            secrets: Bearer token credentials

        Returns:
            New headers dict with Bearer token authentication injected
        """
        headers = headers.copy()

        # Get configuration with defaults
        header_name = config.get("header", "Authorization")
        prefix = config.get("prefix", "Bearer")

        # Get token from secrets
        token = secrets.get("token")
        if not token:
            raise AuthenticationError("Missing 'token' in secrets")

        # Extract secret value (handle both SecretStr and plain str)
        token_value = extract_secret_value(token)

        # Inject into headers
        headers[header_name] = f"{prefix} {token_value}"
        return headers

    def validate_credentials(self, secrets: BearerAuthSecrets) -> None:  # type: ignore[override]
        """Validate token is present.

        Args:
            secrets: Bearer token credentials to validate
        """
        if not secrets.get("token"):
            raise AuthenticationError("Missing 'token' in secrets")


class BasicAuthStrategy(AuthStrategy):
    """Strategy for HTTP Basic authentication."""

    def inject_auth(
        self,
        headers: dict[str, str],
        config: dict[str, Any],
        secrets: BasicAuthSecrets,
    ) -> dict[str, str]:
        """Inject Basic auth credentials into Authorization header.

        Creates a copy of the headers dict with Basic auth added.
        The original headers dict is not modified.

        Args:
            headers: Existing request headers (will not be modified)
            config: Basic authentication configuration (unused)
            secrets: Basic auth credentials

        Returns:
            New headers dict with Authorization header added
        """
        headers = headers.copy()

        # Validate credentials are present (None check only, empty strings are allowed)
        username = secrets.get("username")
        password = secrets.get("password")

        if username is None or password is None:
            raise AuthenticationError("Missing 'username' or 'password' in secrets")

        # Extract secret values (handle both SecretStr and plain str)
        username_value = extract_secret_value(username)
        password_value = extract_secret_value(password)

        # Inject Basic auth header
        credentials = f"{username_value}:{password_value}"
        encoded = base64.b64encode(credentials.encode()).decode()
        headers["Authorization"] = f"Basic {encoded}"

        return headers

    def validate_credentials(self, secrets: BasicAuthSecrets) -> None:  # type: ignore[override]
        """Validate username and password are present.

        Args:
            secrets: Basic auth credentials to validate
        """
        username = secrets.get("username")
        password = secrets.get("password")

        if username is None or password is None:
            raise AuthenticationError("Missing 'username' or 'password' in secrets")


class OAuth2AuthStrategy(AuthStrategy):
    """Strategy for OAuth 2.0 authentication with token refresh support."""

    def inject_auth(
        self,
        headers: dict[str, str],
        config: OAuth2AuthConfig,
        secrets: OAuth2AuthSecrets,
    ) -> dict[str, str]:
        """Inject OAuth2 access token into headers.

        Creates a copy of the headers dict with the OAuth2 token added.
        The original headers dict is not modified.

        Args:
            headers: Existing request headers (will not be modified)
            config: OAuth2 authentication configuration
            secrets: OAuth2 credentials including access_token

        Returns:
            New headers dict with OAuth2 token authentication injected

        Raises:
            AuthenticationError: If access_token is missing
        """
        headers = headers.copy()

        # Get configuration with defaults
        header_name = config.get("header", "Authorization")
        prefix = config.get("prefix", "Bearer")

        # Get access token from secrets
        access_token = secrets.get("access_token")
        if not access_token:
            # Provide helpful error for refresh-token-only scenario
            if secrets.get("refresh_token"):
                raise AuthenticationError(
                    "Missing 'access_token' in secrets. "
                    "When using refresh-token-only mode, ensure HTTPClient.request() "
                    "is called (it handles proactive token refresh automatically)."
                )
            raise AuthenticationError("Missing 'access_token' in secrets")

        # Extract secret value (handle both SecretStr and plain str)
        token_value = extract_secret_value(access_token)

        # Inject into headers
        headers[header_name] = f"{prefix} {token_value}"
        return headers

    def validate_credentials(self, secrets: OAuth2AuthSecrets) -> None:  # type: ignore[override]
        """Validate OAuth2 credentials are valid for authentication.

        Validates that either:
        1. access_token is present, OR
        2. refresh_token is present (for refresh-token-only mode)

        Args:
            secrets: OAuth2 credentials to validate

        Raises:
            AuthenticationError: If neither access_token nor refresh_token is present
        """
        has_access_token = bool(secrets.get("access_token"))
        has_refresh_token = bool(secrets.get("refresh_token"))

        if not has_access_token and not has_refresh_token:
            raise AuthenticationError(
                "Missing OAuth2 credentials. Provide either 'access_token' " "or 'refresh_token' (for refresh-token-only mode)."
            )

    def can_refresh(self, secrets: OAuth2RefreshSecrets) -> bool:
        """Check if token refresh is possible.

        Args:
            secrets: OAuth2 credentials (including optional refresh fields)

        Returns:
            True if refresh_token is available, False otherwise
        """
        return bool(secrets.get("refresh_token"))

    async def handle_auth_error(
        self,
        status_code: int,
        config: dict[str, Any],
        secrets: dict[str, Any],
        config_values: dict[str, str] | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> TokenRefreshResult | None:
        """
        Handle OAuth2 authentication error by refreshing tokens.

        This method is called when a 401 error occurs. It attempts to refresh
        the access_token using the refresh_token if available.

        Args:
            status_code: HTTP status code (only 401 triggers refresh)
            config: OAuth2 authentication configuration
            secrets: OAuth2 credentials including refresh_token
            config_values: Non-secret configuration values for template substitution
            http_client: Optional httpx.AsyncClient for making refresh requests

        Returns:
            TokenRefreshResult with new tokens if refresh successful, None otherwise.

        Note:
            Only attempts refresh on 401 (Unauthorized) errors with valid refresh_token.
            Other status codes (403, etc.) return None immediately.
        """
        # Only handle 401 Unauthorized errors
        if status_code != 401:
            return None

        # Check if we have refresh capability
        if not self.can_refresh(secrets):  # type: ignore[arg-type]
            return None

        # Check if refresh_url is configured
        if not config.get("refresh_url"):
            return None

        try:
            # Create a token refresher
            # Pass None for http_client - let refresher create its own
            token_refresher = OAuth2TokenRefresher(None, config_values)

            # Attempt to refresh the token
            return await token_refresher.refresh_token(
                config=config,  # type: ignore[arg-type]
                secrets=secrets,  # type: ignore[arg-type]
            )

        except Exception as e:
            # Token refresh failed - log the error and return None
            # HTTPClient will raise the original auth error
            logger.warning("OAuth2 token refresh failed: %s", str(e))
            return None

    def needs_proactive_refresh(self, secrets: dict[str, Any]) -> bool:
        """Check if proactive token refresh is needed.

        Returns True if:
        - access_token is missing (None, empty, or not present)
        - refresh_token is present

        This indicates "refresh-token-only" mode where we need to obtain
        an access_token before making API requests.

        Args:
            secrets: OAuth2 credentials

        Returns:
            True if proactive refresh should be attempted, False otherwise
        """
        has_access_token = bool(secrets.get("access_token"))
        has_refresh_token = bool(secrets.get("refresh_token"))

        return not has_access_token and has_refresh_token

    async def ensure_credentials(
        self,
        config: dict[str, Any],
        secrets: dict[str, Any],
        config_values: dict[str, str] | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> TokenRefreshResult | None:
        """
        Proactively refresh OAuth2 tokens if access_token is missing.

        Called before the first API request. If access_token is missing
        but refresh credentials are available, attempts to obtain an
        access_token via token refresh.

        Args:
            config: OAuth2 authentication configuration
            secrets: OAuth2 credentials (may be missing access_token)
            config_values: Non-secret config values for URL templates
            http_client: Optional httpx.AsyncClient for refresh request (unused)

        Returns:
            TokenRefreshResult with new tokens if refresh successful, None otherwise

        Raises:
            AuthenticationError: If refresh fails and no access_token available
        """
        if not self.needs_proactive_refresh(secrets):
            return None

        # Check if refresh_url is configured
        if not config.get("refresh_url"):
            raise AuthenticationError(
                "Missing 'access_token' in secrets and 'refresh_url' in config. "
                "Either provide access_token or configure refresh_url for "
                "proactive token refresh."
            )

        try:
            logger.info("Proactively refreshing OAuth2 token (no access_token provided)")

            # Create token refresher and attempt refresh
            # Pass None for http_client - let refresher create its own
            token_refresher = OAuth2TokenRefresher(None, config_values)
            result = await token_refresher.refresh_token(
                config=config,  # type: ignore[arg-type]
                secrets=secrets,  # type: ignore[arg-type]
            )

            logger.info("Proactive token refresh successful")
            return result

        except Exception as e:
            # Proactive refresh failed - this is fatal since we have no access_token
            msg = f"Failed to obtain access_token via token refresh: {e!s}"
            logger.error(msg)
            raise AuthenticationError(msg) from e


class OAuth2TokenRefresher:
    """Handles OAuth2 token refresh HTTP requests.

    Separated from OAuth2AuthStrategy to maintain single responsibility
    and make testing easier.

    Attributes:
        _http_client: Optional httpx.AsyncClient for making HTTP requests.
                      If None, creates a new client for each refresh request.
        _config_values: Non-secret configuration values for template substitution.
    """

    # Maximum length for error response text to avoid exposing large bodies
    MAX_ERROR_RESPONSE_LENGTH = 500

    def __init__(
        self,
        http_client: httpx.AsyncClient | None = None,
        config_values: dict[str, str] | None = None,
    ):
        """Initialize the token refresher.

        Args:
            http_client: Optional httpx.AsyncClient instance. If provided,
                        will be used for token refresh requests. If None,
                        a new client will be created for each request.
            config_values: Non-secret configuration values (e.g., {"subdomain": "mycompany"})
                          for template variable substitution in refresh URLs.
        """
        self._http_client = http_client
        self._config_values = config_values or {}

    async def refresh_token(
        self,
        config: OAuth2AuthConfig,
        secrets: OAuth2RefreshSecrets,
    ) -> TokenRefreshResult:
        """Refresh the OAuth2 access token using the refresh token.

        This method orchestrates the token refresh flow by:
        1. Validating required configuration and secrets
        2. Building the refresh request (URL, headers, body)
        3. Executing the HTTP request
        4. Parsing and validating the response

        Args:
            config: OAuth2 configuration with refresh_url and auth_style
            secrets: OAuth2 credentials including refresh_token and client credentials

        Returns:
            TokenRefreshResult containing:
                - tokens: dict with access_token, refresh_token (if provided), token_type
                - extracted_values: dict of fields extracted via x-airbyte-token-extract

        Raises:
            AuthenticationError: If refresh fails or required fields missing
        """
        self._validate_refresh_requirements(config, secrets)

        url = self._render_refresh_url(config, secrets)
        headers, body_params = self._build_refresh_request(config, secrets)

        response = await self._execute_refresh_request(url, headers, body_params, config)

        # Get token_extract config if present
        token_extract: list[str] | None = config.get("token_extract")  # type: ignore[assignment]

        return self._parse_refresh_response(response, token_extract)

    def _validate_refresh_requirements(
        self,
        config: OAuth2AuthConfig,
        secrets: OAuth2RefreshSecrets,
    ) -> None:
        """Validate that required fields are present for token refresh.

        Args:
            config: OAuth2 configuration
            secrets: OAuth2 credentials (must include refresh_token)

        Raises:
            AuthenticationError: If refresh_token or refresh_url is missing
        """
        if not secrets.get("refresh_token"):
            raise AuthenticationError("Missing 'refresh_token' in secrets")

        if not config.get("refresh_url"):
            raise AuthenticationError("Missing 'refresh_url' in config")

    def _render_refresh_url(
        self,
        config: OAuth2AuthConfig,
        secrets: OAuth2RefreshSecrets,
    ) -> str:
        """Render the refresh URL with template variables.

        Supports Jinja2 template syntax for dynamic URLs. Template variables can come from:
        1. config_values (non-secret config like subdomain, region, etc.)
        2. config dict (auth configuration)
        3. secrets (client_id only, for convenience)

        Common template variables:
        - {{subdomain}}: For multi-tenant APIs (Zendesk, Slack, etc.)
        - {{shop}}: For Shopify-style APIs
        - {{region}}: For multi-region APIs
        - {{client_id}}: OAuth2 client ID from secrets

        Args:
            config: OAuth2 configuration containing refresh_url
            secrets: OAuth2 credentials (client_id may be used in templates)

        Returns:
            Rendered URL string with variables substituted

        Examples:
            With config_values={"subdomain": "mycompany"}:
            refresh_url: "https://{{subdomain}}.zendesk.com/oauth/tokens"
            # Returns: "https://mycompany.zendesk.com/oauth/tokens"

            With config_values={"shop": "my-store"}:
            refresh_url: "https://{{shop}}.myshopify.com/admin/oauth/access_token"
            # Returns: "https://my-store.myshopify.com/admin/oauth/access_token"
        """
        refresh_url = config["refresh_url"]  # Already validated

        # Build template context with priority: config_values > config > secrets
        template_context = dict(config)  # Auth config values
        template_context.update(self._config_values)  # Non-secret config (higher priority)

        # Add commonly needed secret values (but not sensitive tokens)
        template_context["client_id"] = extract_secret_value(secrets.get("client_id", ""))

        return Template(refresh_url).render(template_context)

    def _build_refresh_request(
        self,
        config: OAuth2AuthConfig,
        secrets: OAuth2RefreshSecrets,
    ) -> tuple[dict[str, str], dict[str, str]]:
        """Build headers and body for the token refresh request.

        Args:
            config: OAuth2 configuration with auth_style
            secrets: OAuth2 credentials (including refresh_token and client credentials)

        Returns:
            Tuple of (headers dict, body params dict)
        """
        auth_style = config.get("auth_style", "body")

        # Extract secret values once
        refresh_token_value = extract_secret_value(
            secrets["refresh_token"]  # Already validated
        )
        client_id_value = extract_secret_value(secrets.get("client_id", ""))
        client_secret_value = extract_secret_value(secrets.get("client_secret", ""))

        # Build base request body
        body_params = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token_value,
        }

        # Build headers based on auth style
        headers = self._build_auth_headers(auth_style, client_id_value, client_secret_value)

        # Add client credentials to body if using body auth style
        if auth_style == "body":
            body_params["client_id"] = client_id_value
            body_params["client_secret"] = client_secret_value

        return headers, body_params

    def _build_auth_headers(
        self,
        auth_style: AuthStyle,
        client_id: str,
        client_secret: str,
    ) -> dict[str, str]:
        """Build authentication headers based on the auth style.

        Args:
            auth_style: One of "basic", "body", or "none"
            client_id: OAuth2 client ID
            client_secret: OAuth2 client secret

        Returns:
            Dictionary of HTTP headers
        """
        headers: dict[str, str] = {}

        if auth_style == "basic":
            # Client credentials in Basic Auth header
            credentials = f"{client_id}:{client_secret}"
            encoded = base64.b64encode(credentials.encode()).decode()
            headers["Authorization"] = f"Basic {encoded}"
        # auth_style == "body" or "none": no auth headers needed

        return headers

    async def _execute_refresh_request(
        self,
        url: str,
        headers: dict[str, str],
        body_params: dict[str, str],
        config: OAuth2AuthConfig,
    ) -> dict[str, Any]:
        """Execute the HTTP request to refresh the token.

        Args:
            url: Token refresh endpoint URL
            headers: HTTP headers (may include Authorization)
            body_params: Request body parameters
            config: OAuth2 configuration (for body_format)

        Returns:
            Parsed JSON response from the token endpoint

        Raises:
            AuthenticationError: If request fails or returns non-200 status
        """
        body_format = config.get("body_format", "form")

        # Use injected client or create a new one
        if self._http_client is not None:
            client = self._http_client
            close_client = False
        else:
            client = httpx.AsyncClient()
            close_client = True

        try:
            # Set content type and make request based on body format
            if body_format == "json":
                headers["Content-Type"] = "application/json"
                response = await client.post(url, json=body_params, headers=headers)
            else:  # form (default)
                headers["Content-Type"] = "application/x-www-form-urlencoded"
                response = await client.post(url, data=body_params, headers=headers)

            # Check for successful response
            if response.status_code != 200:
                response_text = response.text[: self.MAX_ERROR_RESPONSE_LENGTH]
                msg = f"Token refresh failed: {response.status_code} {response_text}"
                raise AuthenticationError(msg)

            # Parse JSON response
            try:
                return response.json()
            except Exception as e:
                msg = f"Token refresh response invalid JSON: {str(e)}"
                raise AuthenticationError(msg)
        finally:
            # Only close if we created the client
            if close_client:
                await client.aclose()

    def _parse_refresh_response(
        self,
        response_data: dict[str, Any],
        token_extract: list[str] | None = None,
    ) -> TokenRefreshResult:
        """Parse and validate the token refresh response.

        Args:
            response_data: Parsed JSON response from token endpoint
            token_extract: Optional list of fields to extract from response
                and use as server variables (e.g., ["instance_url"])

        Returns:
            TokenRefreshResult with tokens and optional extracted values

        Raises:
            AuthenticationError: If access_token is missing from response
        """
        new_access_token = response_data.get("access_token")
        if not new_access_token:
            msg = "Token refresh response missing 'access_token'"
            raise AuthenticationError(msg)

        tokens = {
            "access_token": new_access_token,
            "token_type": response_data.get("token_type", "Bearer"),
        }

        # Include new refresh_token if provided by the server
        if "refresh_token" in response_data:
            tokens["refresh_token"] = response_data["refresh_token"]

        # Extract fields specified by x-airbyte-token-extract
        extracted_values: dict[str, str] | None = None
        if token_extract:
            extracted = {}
            for field in token_extract:
                if field in response_data:
                    value = response_data[field]
                    if isinstance(value, str):
                        extracted[field] = value
                    else:
                        # Convert non-string values to string for server variables
                        extracted[field] = str(value)
                    logger.debug(
                        "Extracted '%s' from token response for server variable",
                        field,
                    )
            if extracted:
                extracted_values = extracted

        return TokenRefreshResult(tokens=tokens, extracted_values=extracted_values)


class AuthStrategyFactory:
    """Factory for creating authentication strategies."""

    # Create singleton instances
    _api_key_strategy = APIKeyAuthStrategy()
    _bearer_strategy = BearerAuthStrategy()
    _basic_strategy = BasicAuthStrategy()
    _oauth2_strategy = OAuth2AuthStrategy()

    # Strategy registry mapping AuthType to strategy instances
    _strategies: dict[AuthType, AuthStrategy] = {
        AuthType.API_KEY: _api_key_strategy,
        AuthType.BEARER: _bearer_strategy,
        AuthType.BASIC: _basic_strategy,
        AuthType.OAUTH2: _oauth2_strategy,
    }

    @classmethod
    def get_strategy(cls, auth_type: AuthType) -> AuthStrategy:
        """
        Get authentication strategy for the given auth type.

        Args:
            auth_type: Authentication type from AuthConfig

        Returns:
            Appropriate AuthStrategy instance

        Raises:
            AuthenticationError: If auth type is not implemented
        """
        strategy = cls._strategies.get(auth_type)
        if strategy is None:
            raise AuthenticationError(
                f"Authentication type '{auth_type.value}' is not implemented. "
                f"Supported types: {', '.join(s.value for s in cls._strategies.keys())}"
            )
        return strategy

    @classmethod
    def register_strategy(cls, auth_type: AuthType, strategy: AuthStrategy) -> None:
        """
        Register a custom authentication strategy.

        Args:
            auth_type: Authentication type to register
            strategy: Strategy instance to use for this auth type
        """
        cls._strategies[auth_type] = strategy
