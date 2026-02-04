"""Utilities for exploring and introspecting connector packages."""

from __future__ import annotations

import importlib
import inspect
import typing
from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel, Field

from .airbyte_api import AirbyteApi, fetch_registry
from .installer import get_package_name, install_package, is_local_path
from .models.connector_config import (
    CloudSource,
    ConnectorConfig,
    PackageSource,
    resolve_credentials,
)


@dataclass
class ConnectorParam:
    """A connector parameter definition."""

    name: str
    annotation: str | None
    required: bool


# Parameters that are always present in connector __init__ and should be excluded
_STANDARD_CONNECTOR_PARAMS = frozenset(
    {
        "self",
        "auth_config",
        "on_token_refresh",
    }
)


class AirbyteCloudAuthConfig(BaseModel):
    """Authentication configuration for Airbyte Cloud hosted execution."""

    airbyte_external_user_id: str = Field(description="External user ID for hosted execution")
    airbyte_client_id: str = Field(description="Airbyte OAuth client ID")
    airbyte_client_secret: str = Field(description="Airbyte OAuth client secret")


def _package_to_module_name(package_name: str) -> str:
    """Convert a package name to a Python module name."""
    return package_name.replace("-", "_")


def _load_connector_module(package_name: str) -> Any:
    """Load a connector module by package name."""
    module_name = _package_to_module_name(package_name)
    return importlib.import_module(module_name)


def get_cloud_auth_config_type() -> type[BaseModel]:
    """Get the AuthConfig type for Airbyte Cloud hosted execution.

    Returns:
        The AirbyteCloudAuthConfig model class.
    """
    return AirbyteCloudAuthConfig


def get_auth_config_types(package_name: str) -> list[type[BaseModel]]:
    """Get the AuthConfig types from a connector package.

    Args:
        package_name: PyPI package name (e.g., "airbyte-agent-gong").

    Returns:
        List of Pydantic model classes for each auth method.

    Raises:
        ModuleNotFoundError: If the package is not installed.
        ValueError: If the module doesn't have an AuthConfig export.
    """
    module = _load_connector_module(package_name)
    module_name = _package_to_module_name(package_name)

    auth_config_names = [name for name in dir(module) if name.endswith("AuthConfig")]
    if not auth_config_names:
        raise ValueError(f"No AuthConfig type found in {module_name}")

    auth_type = getattr(module, auth_config_names[0])
    auth_options = typing.get_args(auth_type)

    if not auth_options:
        # Not a Union, single auth type
        return [auth_type]

    return list(auth_options)


def _get_connector_class(package_name: str) -> type:
    """Get the Connector class from a package."""
    module = _load_connector_module(package_name)
    connector_names = [name for name in dir(module) if name.endswith("Connector")]
    if not connector_names:
        module_name = _package_to_module_name(package_name)
        raise ValueError(f"No Connector class found in {module_name}")
    return getattr(module, connector_names[0])


def get_additional_connector_params(package_name: str) -> list[ConnectorParam]:
    """Get additional (non-auth) parameters for a connector.

    Args:
        package_name: PyPI package name (e.g., "airbyte-agent-zendesk-support").

    Returns:
        List of ConnectorParam for parameters beyond the standard auth params.

    Raises:
        ModuleNotFoundError: If the package is not installed.
        ValueError: If the module doesn't have a Connector class.
    """
    connector_class = _get_connector_class(package_name)
    sig = inspect.signature(connector_class.__init__)

    params = []
    for name, param in sig.parameters.items():
        if name in _STANDARD_CONNECTOR_PARAMS:
            continue

        # Get the type annotation as string
        annotation = None
        if param.annotation != inspect.Parameter.empty:
            ann = param.annotation
            # Convert to string, stripping Optional/None for cleaner output
            if isinstance(ann, str):
                # Already a string annotation (forward reference)
                annotation = ann.replace(" | None", "").replace("None | ", "")
            else:
                # Actual type - get string representation
                annotation = getattr(ann, "__name__", str(ann))

        # Determine if required (no default value)
        required = param.default == inspect.Parameter.empty

        params.append(ConnectorParam(name=name, annotation=annotation, required=required))

    return params


class ConnectorLoadError(Exception):
    """Exception raised when connector loading fails."""

    pass


def get_connector_name(config: ConnectorConfig) -> str:
    """Get the connector name by installing the package and reading the class attribute.

    This does NOT instantiate the connector (no credentials needed).

    Args:
        config: ConnectorConfig with source info.

    Returns:
        The connector name (e.g. "gong", "zendesk-support").

    Raises:
        ConnectorLoadError: If the connector package cannot be installed or loaded.
    """
    source = config.connector

    if isinstance(source, PackageSource):
        spec = f"{source.package}=={source.version}" if source.version and not is_local_path(source.package) else source.package
        install_package(spec)
        package_name = get_package_name(spec)
    elif isinstance(source, CloudSource):
        raise ConnectorLoadError("Cannot determine connector name from CloudSource without credentials")
    else:
        raise ConnectorLoadError(f"Unknown source type: {type(source)}")

    try:
        connector_class = _get_connector_class(package_name)
    except ValueError as e:
        raise ConnectorLoadError(str(e)) from e

    name = getattr(connector_class, "connector_name", None)
    if not name:
        raise ConnectorLoadError(f"Connector class {connector_class.__name__} has no connector_name attribute")
    return name


def _find_matching_auth_config(package_name: str, credentials: dict[str, str]) -> BaseModel:
    """Find the auth config type that matches the provided credentials.

    Args:
        package_name: PyPI package name.
        credentials: Resolved credentials dict.

    Returns:
        Instantiated auth config object.

    Raises:
        ConnectorLoadError: If no matching auth config is found.
    """
    auth_config_types = get_auth_config_types(package_name)

    # Try each auth config type
    for auth_class in auth_config_types:
        try:
            return auth_class(**credentials)
        except Exception:
            continue

    auth_names = [t.__name__ for t in auth_config_types]
    raise ConnectorLoadError(f"Credentials do not match any AuthConfig in {package_name}. Available configs: {auth_names}")


def load_connector(config: ConnectorConfig) -> Any:
    """Load and instantiate a connector from configuration.

    Args:
        config: ConnectorConfig with source, credentials, and config.

    Returns:
        Instantiated connector object.

    Raises:
        ConnectorLoadError: If connector cannot be loaded or instantiated.
    """
    source = config.connector

    # Determine package name and install if needed
    if isinstance(source, PackageSource):
        spec = f"{source.package}=={source.version}" if source.version and not is_local_path(source.package) else source.package
        install_package(spec)
        package_name = get_package_name(spec)

    elif isinstance(source, CloudSource):
        # Resolve credentials early — needed for API lookup
        try:
            resolved_credentials = resolve_credentials(config.credentials)
        except ValueError as e:
            raise ConnectorLoadError(str(e)) from e

        # Derive package name from connector ID via Airbyte API
        required_cred_keys = ["airbyte_client_id", "airbyte_client_secret"]
        missing_cred_keys = [k for k in required_cred_keys if k not in resolved_credentials]
        if missing_cred_keys:
            raise ConnectorLoadError(f"CloudSource requires credentials: {required_cred_keys}. Missing: {missing_cred_keys}")

        try:
            api = AirbyteApi(
                client_id=resolved_credentials["airbyte_client_id"],
                client_secret=resolved_credentials["airbyte_client_secret"],
            )
            connector_source = api.get_connector(source.connector_id)
        except Exception as e:
            raise ConnectorLoadError(f"Failed to fetch connector source: {e}") from e

        defn_id = connector_source.get("source_template", {}).get("source_definition_id", "")

        try:
            registry_entries = fetch_registry()
        except Exception as e:
            raise ConnectorLoadError(f"Failed to fetch connector registry: {e}") from e

        registry = {e["connector_id"]: e for e in registry_entries if "connector_id" in e}
        reg = registry.get(defn_id, {})
        connector_name = reg.get("connector_name")
        if not connector_name:
            raise ConnectorLoadError(f"Could not determine connector type for ID: {source.connector_id}")

        package_name = f"airbyte-agent-{connector_name}"
        install_package(package_name)

    else:
        raise ConnectorLoadError(f"Unknown source type: {type(source)}")

    # Resolve environment variables in credentials
    try:
        resolved_credentials = resolve_credentials(config.credentials)
    except ValueError as e:
        raise ConnectorLoadError(str(e)) from e

    # Get connector class
    try:
        connector_class = _get_connector_class(package_name)
    except ValueError as e:
        raise ConnectorLoadError(str(e)) from e

    # Build connector kwargs based on source type
    connector_kwargs: dict[str, Any] = {}

    if isinstance(source, CloudSource):
        required_keys = ["airbyte_external_user_id", "airbyte_client_id", "airbyte_client_secret"]
        missing_keys = [k for k in required_keys if k not in resolved_credentials]
        if missing_keys:
            raise ConnectorLoadError(f"CloudSource requires credentials: {required_keys}. Missing: {missing_keys}")

        # Import AirbyteHostedAuthConfig from the connector's vendored SDK
        # Pass AirbyteHostedAuthConfig via auth_config parameter for hosted mode
        vendored_types = importlib.import_module(f"{_package_to_module_name(package_name)}._vendored.connector_sdk.types")
        AirbyteHostedAuthConfig = vendored_types.AirbyteHostedAuthConfig

        connector_kwargs["auth_config"] = AirbyteHostedAuthConfig(
            external_user_id=resolved_credentials["airbyte_external_user_id"],
            airbyte_client_id=resolved_credentials["airbyte_client_id"],
            airbyte_client_secret=resolved_credentials["airbyte_client_secret"],
            connector_id=source.connector_id,
        )
    else:
        auth_config = _find_matching_auth_config(package_name, resolved_credentials)
        connector_kwargs["auth_config"] = auth_config

    # Add any additional config params
    for key, value in config.config.items():
        connector_kwargs[key] = value

    try:
        return connector_class(**connector_kwargs)
    except Exception as e:
        raise ConnectorLoadError(f"Failed to instantiate connector: {e}") from e
