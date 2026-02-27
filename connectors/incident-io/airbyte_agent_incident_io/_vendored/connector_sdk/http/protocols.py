"""HTTP client and response protocols for abstracting HTTP client implementations."""

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class HTTPResponseProtocol(Protocol):
    """Protocol defining the interface for HTTP responses.

    This protocol abstracts the response interface, allowing different HTTP clients
    to provide responses that work with the SDK.
    """

    @property
    def status_code(self) -> int:
        """The HTTP status code of the response."""
        ...

    @property
    def headers(self) -> dict[str, str]:
        """The response headers as a dictionary."""
        ...

    async def json(self) -> Any:
        """Parse the response body as JSON.

        Returns:
            The parsed JSON data (dict, list, or primitive).

        Raises:
            ValueError: If the response body is not valid JSON.
        """
        ...

    async def text(self) -> str:
        """Get the response body as text.

        Returns:
            The response body decoded as a string.
        """
        ...

    def raise_for_status(self) -> None:
        """Raise an exception if the response status indicates an error.

        Raises:
            Exception: For 4xx or 5xx status codes.
        """
        ...


@runtime_checkable
class HTTPClientProtocol(Protocol):
    """Protocol defining the interface for HTTP clients.

    This protocol abstracts the HTTP client interface, allowing the SDK to work with
    different HTTP client implementations (httpx, aiohttp, etc.).
    """

    async def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        data: dict[str, Any] | str | None = None,
        headers: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> HTTPResponseProtocol:
        """Execute an HTTP request.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            url: The URL to request
            params: Query parameters to append to the URL
            json: JSON data to send in the request body
            data: Form data or raw string to send in the request body
            headers: HTTP headers to include in the request
            **kwargs: Additional client-specific parameters

        Returns:
            An HTTPResponseProtocol implementation with the response data.

        Raises:
            Exception: For network errors, timeouts, or other request failures.
        """
        ...

    async def aclose(self) -> None:
        """Close the HTTP client and cleanup resources.

        This should be called when the client is no longer needed to properly
        cleanup connections and resources.
        """
        ...

    async def __aenter__(self) -> "HTTPClientProtocol":
        """Enter async context manager.

        Returns:
            The client instance.
        """
        ...

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Exit async context manager and cleanup resources.

        Args:
            exc_type: Exception type if an exception occurred
            exc_val: Exception value if an exception occurred
            exc_tb: Exception traceback if an exception occurred
        """
        ...
