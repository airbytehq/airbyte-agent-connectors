"""HTTP-related exceptions for the Airbyte SDK."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .response import HTTPResponse


class HTTPClientError(Exception):
    """Base exception for HTTP client errors."""

    pass


class HTTPStatusError(HTTPClientError):
    """Raised when an HTTP response has a 4xx or 5xx status code.

    This is the base exception for status code errors and is raised by
    HTTPResponse.raise_for_status().
    """

    def __init__(
        self,
        status_code: int,
        message: str,
        response: "HTTPResponse | None" = None,
    ) -> None:
        """Initialize HTTP status error.

        Args:
            status_code: The HTTP status code (e.g., 404, 500)
            message: Error message describing the issue
            response: Optional HTTPResponse object for accessing details
        """
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class AuthenticationError(HTTPStatusError):
    """Raised when authentication credentials are missing or invalid (401, 403)."""

    def __init__(
        self,
        message: str,
        status_code: int = 401,
        response: "HTTPResponse | None" = None,
    ) -> None:
        """Initialize authentication error.

        Args:
            message: Error message describing the authentication issue
            status_code: HTTP status code (401 or 403)
            response: Optional HTTPResponse object for accessing details
        """
        super().__init__(status_code=status_code, message=message, response=response)


class RateLimitError(HTTPStatusError):
    """Raised when API rate limit is exceeded (429 response)."""

    def __init__(
        self,
        message: str,
        retry_after: int | None = None,
        response: "HTTPResponse | None" = None,
    ) -> None:
        """Initialize rate limit error.

        Args:
            message: Error message describing the rate limit
            retry_after: Seconds to wait before retrying (from Retry-After header)
            response: Optional HTTPResponse object for accessing details
        """
        super().__init__(status_code=429, message=message, response=response)
        self.retry_after = retry_after


class NetworkError(HTTPClientError):
    """Raised when network connection fails.

    This includes connection errors, DNS resolution failures, and other
    network-level issues.
    """

    def __init__(self, message: str, original_error: Exception | None = None) -> None:
        """Initialize network error.

        Args:
            message: Error message describing the network issue
            original_error: Optional original exception from the HTTP client
        """
        super().__init__(message)
        self.original_error = original_error


class TimeoutError(HTTPClientError):
    """Raised when a request times out.

    This can occur during connection establishment, reading the response,
    or writing the request.
    """

    def __init__(
        self,
        message: str,
        timeout_type: str | None = None,
        original_error: Exception | None = None,
    ) -> None:
        """Initialize timeout error.

        Args:
            message: Error message describing the timeout
            timeout_type: Optional type of timeout (connect, read, write, pool)
            original_error: Optional original exception from the HTTP client
        """
        super().__init__(message)
        self.timeout_type = timeout_type
        self.original_error = original_error
