"""Retryable-runtime-error predicates used by `translate_exceptions`.

This module replaces the backend-only predicate that lived at
`backend/app/agents/util.py:_is_retryable_runtime_error`. The SDK cannot depend
on `fastapi`, so the previous direct `isinstance(error, HTTPException)` branch
is replaced with a narrowed duck-type check on `status_code` (see comment in
`_is_retryable_runtime_error` for the exact contract).
"""

from __future__ import annotations

import httpx

from airbyte_agent_sdk.http.exceptions import (
    NetworkError as SDKNetworkError,
)
from airbyte_agent_sdk.http.exceptions import (
    RateLimitError,
)
from airbyte_agent_sdk.http.exceptions import (
    TimeoutError as SDKTimeoutError,
)


def _looks_like_http_exception_with_retryable_status(error: Exception) -> bool:
    """Narrowed duck-type recognition for `fastapi.HTTPException`-like objects.

    The SDK does not depend on FastAPI, so we cannot use `isinstance(error,
    HTTPException)`. The contract here is intentionally narrow: an object
    qualifies only when it has an integer `status_code` attribute meeting the
    "429 or >= 500" threshold. Future maintainers should NOT widen this — for
    example, a `SimpleNamespace(status_code="500")` (string) must NOT match,
    because non-`HTTPException` callers may legitimately attach a `status_code`
    attribute that is not an HTTP code.
    """
    status_code = getattr(error, "status_code", None)
    if not isinstance(status_code, int):
        return False
    return status_code == 429 or status_code >= 500


def _is_retryable_runtime_error(error: Exception) -> bool:
    """Return True when `error` is a transient runtime failure worth retrying.

    Mirrors `backend/app/agents/util.py:_is_retryable_runtime_error` exactly,
    with the FastAPI `HTTPException` branch replaced by a narrowed duck-type
    check (see `_looks_like_http_exception_with_retryable_status`).

    `ConnectorValidationError` is intentionally NOT retryable: validation
    failures are deterministic (same bad payload always fails), so retrying
    would burn attempts without progress. The translator's fallback path
    surfaces it to the LLM via the framework signal so the LLM can self-correct.
    """
    if _looks_like_http_exception_with_retryable_status(error):
        return True

    if isinstance(error, RateLimitError | SDKNetworkError | SDKTimeoutError):
        return True

    # Defence in depth for callers that surface raw httpx HTTPStatusError
    # without the SDK's adapter translating to RateLimitError / NetworkError.
    if isinstance(error, httpx.HTTPStatusError):
        status_code = error.response.status_code
        return status_code == 429 or status_code >= 500

    return isinstance(error, httpx.ConnectError | httpx.TimeoutException | TimeoutError)
