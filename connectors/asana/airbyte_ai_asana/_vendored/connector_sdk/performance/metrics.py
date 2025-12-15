"""Performance metrics tracking."""

import time
from contextlib import asynccontextmanager
from typing import Dict, Optional


class PerformanceMonitor:
    """Monitor and track performance metrics for operations."""

    def __init__(self):
        """Initialize performance monitor."""
        self._metrics: Dict[str, Dict[str, float]] = {}

    def record(self, metric_name: str, duration: float):
        """Record a metric.

        Args:
            metric_name: Name of the metric
            duration: Duration in seconds
        """
        if metric_name not in self._metrics:
            self._metrics[metric_name] = {
                "count": 0,
                "total": 0.0,
                "min": float("inf"),
                "max": 0.0,
            }

        metrics = self._metrics[metric_name]
        metrics["count"] += 1
        metrics["total"] += duration
        metrics["min"] = min(metrics["min"], duration)
        metrics["max"] = max(metrics["max"], duration)

    def get_stats(self, metric_name: str) -> Optional[Dict[str, float]]:
        """Get statistics for a metric.

        Args:
            metric_name: Name of the metric

        Returns:
            Dictionary with count, total, mean, min, max or None if metric not found
        """
        if metric_name not in self._metrics:
            return None

        metrics = self._metrics[metric_name]
        return {
            "count": metrics["count"],
            "total": metrics["total"],
            "mean": metrics["total"] / metrics["count"] if metrics["count"] > 0 else 0.0,
            "min": metrics["min"] if metrics["min"] != float("inf") else 0.0,
            "max": metrics["max"],
        }

    def get_all_stats(self) -> Dict[str, Dict[str, float]]:
        """Get statistics for all metrics.

        Returns:
            Dictionary mapping metric names to their statistics
        """
        return {name: self.get_stats(name) for name in self._metrics.keys()}

    def reset(self, metric_name: Optional[str] = None):
        """Reset metrics.

        Args:
            metric_name: Specific metric to reset, or None to reset all
        """
        if metric_name:
            if metric_name in self._metrics:
                del self._metrics[metric_name]
        else:
            self._metrics.clear()

    @asynccontextmanager
    async def track(self, metric_name: str):
        """Context manager for tracking operation duration.

        Args:
            metric_name: Name of the metric to track

        Example:
            async with monitor.track("api_call"):
                result = await some_async_operation()
        """
        start_time = time.time()
        try:
            yield
        finally:
            duration = time.time() - start_time
            self.record(metric_name, duration)
