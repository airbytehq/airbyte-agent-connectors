"""
Pydantic 2 schema models for OpenAPI 3.0 connector specifications.

This package provides strongly-typed Pydantic models that mirror the OpenAPI 3.0
specification while supporting Airbyte-specific extensions.

Usage:
    import yaml
    from . import OpenAPIConnector

    with open('connector.yaml') as f:
        data = yaml.safe_load(f)

    connector = OpenAPIConnector(**data)
    print(connector.list_resources())
"""

from .base import Contact, Info, License, Server, ServerVariable
from .components import (
    Components,
    Header,
    MediaType,
    Parameter,
    RequestBody,
    Response,
    Schema,
)
from .connector import ExternalDocs, OpenAPIConnector, Tag
from .extensions import PaginationConfig, RateLimitConfig, RetryConfig
from .operations import Operation, PathItem
from .security import (
    AirbyteAuthConfig,
    AuthConfigFieldSpec,
    AuthConfigOption,
    OAuth2Flow,
    OAuth2Flows,
    SecurityRequirement,
    SecurityScheme,
)

__all__ = [
    # Root model
    "OpenAPIConnector",
    "Tag",
    "ExternalDocs",
    # Base models
    "Info",
    "Server",
    "ServerVariable",
    "Contact",
    "License",
    # Security models
    "SecurityScheme",
    "SecurityRequirement",
    "OAuth2Flow",
    "OAuth2Flows",
    "AirbyteAuthConfig",
    "AuthConfigOption",
    "AuthConfigFieldSpec",
    # Component models
    "Components",
    "Schema",
    "Parameter",
    "RequestBody",
    "Response",
    "MediaType",
    "Header",
    # Operation models
    "PathItem",
    "Operation",
    # Extension models (for future use)
    "PaginationConfig",
    "RateLimitConfig",
    "RetryConfig",
]
