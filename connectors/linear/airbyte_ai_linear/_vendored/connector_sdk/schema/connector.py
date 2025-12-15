"""
Root OpenAPI 3.1 connector specification model.

References:
- https://spec.openapis.org/oas/v3.1.0#openapi-object
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..constants import OPENAPI_VERSION_PREFIX

from .base import Info, Server
from .components import Components
from .operations import PathItem
from .security import SecurityRequirement


class Tag(BaseModel):
    """
    Tag metadata for grouping operations.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#tag-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    name: str
    description: str | None = None
    external_docs: dict[str, Any] | None = Field(None, alias="externalDocs")


class ExternalDocs(BaseModel):
    """
    External documentation reference.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#external-documentation-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    description: str | None = None
    url: str


class OpenAPIConnector(BaseModel):
    """
    Root OpenAPI 3.1 connector specification.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#openapi-object

    This is the top-level model that represents a complete OpenAPI 3.1 specification
    for an Airbyte connector. It enforces strict validation (extra='forbid') to catch
    typos and unknown extensions.
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid", validate_default=True)

    # Required fields
    openapi: str
    info: Info
    paths: dict[str, PathItem] = Field(default_factory=dict)

    # Optional fields
    servers: list[Server] = Field(default_factory=list)
    components: Components | None = None
    security: list[SecurityRequirement] | None = None
    tags: list[Tag] | None = None
    external_docs: ExternalDocs | None = Field(None, alias="externalDocs")

    @field_validator("openapi")
    @classmethod
    def validate_openapi_version(cls, v: str) -> str:
        """Validate that OpenAPI version is 3.1.x."""
        if not v.startswith(OPENAPI_VERSION_PREFIX):
            raise ValueError(f"OpenAPI version must be {OPENAPI_VERSION_PREFIX}x, got: {v}")
        return v

    def get_entity_operations(self, entity_name: str) -> list[tuple[str, str, Any]]:
        """
        Get all operations for a specific entity.

        Args:
            entity_name: The x-airbyte-entity value to filter by

        Returns:
            List of tuples: (path, method, operation)
        """
        results = []
        for path, path_item in self.paths.items():
            for method in [
                "get",
                "post",
                "put",
                "patch",
                "delete",
                "options",
                "head",
                "trace",
            ]:
                operation = getattr(path_item, method, None)
                if operation and operation.x_airbyte_entity == entity_name:
                    results.append((path, method, operation))
        return results

    def list_entities(self) -> list[str]:
        """
        List all unique entity names defined in x-airbyte-entity extensions.

        Returns:
            Sorted list of unique entity names
        """
        entities = set()
        for path_item in self.paths.values():
            for method in [
                "get",
                "post",
                "put",
                "patch",
                "delete",
                "options",
                "head",
                "trace",
            ]:
                operation = getattr(path_item, method, None)
                if operation and operation.x_airbyte_entity:
                    entities.add(operation.x_airbyte_entity)
        return sorted(entities)
