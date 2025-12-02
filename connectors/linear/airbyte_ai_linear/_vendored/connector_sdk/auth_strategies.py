"""Authentication strategy pattern implementation for HTTP client."""

import base64
from abc import ABC, abstractmethod
from typing import Any, TypedDict

from .secrets import SecretStr

from .exceptions import AuthenticationError
from .types import AuthType


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

        Args:
            headers: Existing request headers
            config: Authentication configuration from AuthConfig.config
            secrets: Secret credentials dictionary (SecretStr or plain str values)

        Returns:
            Headers dictionary with authentication injected

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


class APIKeyAuthStrategy(AuthStrategy):
    """Strategy for API key authentication."""

    def inject_auth(
        self,
        headers: dict[str, str],
        config: APIKeyAuthConfig,
        secrets: APIKeyAuthSecrets,
    ) -> dict[str, str]:
        """Inject API key into headers.

        Args:
            headers: Existing request headers
            config: API key authentication configuration
            secrets: API key credentials

        Returns:
            Headers with API key authentication injected
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
        api_key_value = (
            api_key.get_secret_value() if isinstance(api_key, SecretStr) else api_key
        )

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

        Args:
            headers: Existing request headers
            config: Bearer authentication configuration
            secrets: Bearer token credentials

        Returns:
            Headers with Bearer token authentication injected
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
        token_value = (
            token.get_secret_value() if isinstance(token, SecretStr) else token
        )

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

        Args:
            headers: Existing request headers
            config: Basic authentication configuration (unused)
            secrets: Basic auth credentials

        Returns:
            Headers dictionary with Authorization header added
        """
        headers = headers.copy()

        # Validate credentials are present (None check only, empty strings are allowed)
        username = secrets.get("username")
        password = secrets.get("password")

        if username is None or password is None:
            raise AuthenticationError("Missing 'username' or 'password' in secrets")

        # Extract secret values (handle both SecretStr and plain str)
        username_value = (
            username.get_secret_value() if isinstance(username, SecretStr) else username
        )
        password_value = (
            password.get_secret_value() if isinstance(password, SecretStr) else password
        )

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


class AuthStrategyFactory:
    """Factory for creating authentication strategies."""

    # Create singleton instances
    _api_key_strategy = APIKeyAuthStrategy()
    _bearer_strategy = BearerAuthStrategy()
    _basic_strategy = BasicAuthStrategy()

    # Strategy registry mapping AuthType to strategy instances
    _strategies: dict[AuthType, AuthStrategy] = {
        AuthType.API_KEY: _api_key_strategy,
        AuthType.BEARER: _bearer_strategy,
        AuthType.BEARER_TOKEN: _bearer_strategy,  # Alias for BEARER (same instance)
        AuthType.BASIC: _basic_strategy,
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
