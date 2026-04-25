"""Connector registry: name -> YAML spec path mapping."""

from __future__ import annotations

import importlib
from pathlib import Path

from airbyte_agent_sdk.errors import UnknownConnectorError

_SDK_DIR = Path(__file__).parent

# In a published wheel, specs are bundled at airbyte_agent_sdk/specs/.
# In local development, fall back to integrations/ at the repo root.
_SPECS_DIR = _SDK_DIR / "specs"
if not _SPECS_DIR.is_dir():
    _REPO_ROOT = _SDK_DIR.parent.parent  # airbyte_agent_sdk -> connector-sdk -> repo root
    _SPECS_DIR = _REPO_ROOT / "integrations"

_CONNECTORS: list[str] = sorted(d.name for d in _SPECS_DIR.iterdir() if d.is_dir() and (d / "connector.yaml").exists()) if _SPECS_DIR.is_dir() else []

_CONNECTOR_SET: set[str] = set(_CONNECTORS)


def get_spec_path(name: str) -> Path:
    """Return the path to a connector's connector.yaml.

    Args:
        name: Connector slug, e.g. "stripe" or "zendesk-support".

    Raises:
        UnknownConnectorError: If the connector name is not found.
    """
    if name not in _CONNECTOR_SET:
        raise UnknownConnectorError(f"Unknown connector: {name!r}. Available connectors: {', '.join(_CONNECTORS)}")
    return _SPECS_DIR / name / "connector.yaml"


def list_connectors() -> list[str]:
    """Return a sorted list of all available connector names."""
    return list(_CONNECTORS)


_CLASS_CACHE: dict[str, type | None] = {}


def _get_connector_class(name: str) -> type | None:
    """Lazily look up the typed connector class for a connector name.

    Returns the class (e.g., StripeConnector) if a generated package exists,
    or None if the connector only has a YAML spec.
    Results are cached (both hits and misses).
    """
    if name in _CLASS_CACHE:
        return _CLASS_CACHE[name]
    try:
        module_name = name.replace("-", "_")
        mod = importlib.import_module(f"airbyte_agent_sdk.connectors.{module_name}")
        # Convention: PascalCase + "Connector" (e.g., stripe -> StripeConnector)
        class_name = "".join(w.capitalize() for w in module_name.split("_")) + "Connector"
        cls = getattr(mod, class_name, None)
        _CLASS_CACHE[name] = cls
        return cls
    except ImportError:
        _CLASS_CACHE[name] = None
        return None
