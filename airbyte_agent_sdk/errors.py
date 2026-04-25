"""Root exception for the Airbyte Agent SDK.

This module intentionally has zero internal imports so that
``http/exceptions.py`` and ``executor/models.py`` can both import
``AirbyteError`` from it without risking a circular import through the
``exceptions.py`` back-compat shim.

It also defines the connector-lookup exception hierarchy
(``UnknownConnectorError``, ``ConnectorNotFoundError``,
``ConnectorAmbiguityError``) which inherit ``ValueError`` for
backward compatibility with existing ``except ValueError:`` handlers.
"""

from __future__ import annotations


class AirbyteError(Exception):
    """Root of the SDK exception hierarchy.

    Covers SDK-owned I/O error families:

    * ``HTTPClientError`` and subclasses (``HTTPStatusError``,
      ``AuthenticationError``, ``RateLimitError``, ``NetworkError``,
      ``TimeoutError``) raised by ``http_client.py``,
      ``http/adapters/httpx_adapter.py``, ``http/response.py``,
      ``auth_strategies.py``, and ``executor/local_executor.py``.
    * ``ExecutorError`` and subclasses (``EntityNotFoundError``,
      ``ActionNotSupportedError``, ``MissingParameterError``,
      ``InvalidParameterError``) raised by the local executor.

    Not caught by ``AirbyteError``:

    * ``ValueError`` from argument validation at ``connect()``,
      ``Workspace(...)``, ``ask()``/``ask_sync()`` (via
      ``resolve_credentials()``), and ``HostedExecutor(...)``.
    * ``httpx.HTTPStatusError`` / ``httpx.RequestError`` propagated
      unwrapped from the hosted path (``HostedExecutor.execute()`` and
      ``AirbyteCloudClient``).
    * ``RuntimeError`` raised by generated typed connectors when the
      underlying ``ExecutionResult.success`` is ``False``.

    If you use the hosted path or a generated typed connector, catch
    ``AirbyteError`` together with ``httpx.HTTPError`` (and optionally
    ``RuntimeError``) to cover the full failure surface.
    """


class UnknownConnectorError(ValueError):
    """Connector slug is not in the bundled SDK registry."""


class ConnectorNotFoundError(ValueError):
    """Workspace resolves to zero matching connectors."""


class ConnectorAmbiguityError(ValueError):
    """Workspace resolves to more than one matching connector."""
