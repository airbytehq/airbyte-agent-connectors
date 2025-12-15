"""Performance instrumentation decorator for async functions."""

import functools
import logging
import time
from typing import Any, Callable, TypeVar

# Type variable for generic function decoration
F = TypeVar("F", bound=Callable[..., Any])

logger = logging.getLogger(__name__)


def instrument(metric_name: str) -> Callable[[F], F]:
    """Decorator to instrument async functions with performance tracking.

    Args:
        metric_name: Name of the metric to track

    Returns:
        Decorator function

    Example:
        @instrument("stripe.customer.list")
        async def list_customers():
            ...
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            success = True
            error = None

            try:
                result = await func(*args, **kwargs)
                return result

            except Exception as e:
                success = False
                error = e
                raise

            finally:
                duration = time.time() - start_time
                duration_ms = duration * 1000

                # Log performance metrics
                if success:
                    logger.debug(f"[{metric_name}] completed in {duration_ms:.2f}ms")
                else:
                    logger.warning(f"[{metric_name}] failed after {duration_ms:.2f}ms: {error}")

        return wrapper  # type: ignore

    return decorator
