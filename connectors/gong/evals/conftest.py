"""Pytest fixtures for Gong connector evaluations."""

from __future__ import annotations

import pytest


@pytest.fixture
def current_test_name(request: pytest.FixtureRequest) -> str:
    """Get the current test name for reporting."""
    return request.node.name
