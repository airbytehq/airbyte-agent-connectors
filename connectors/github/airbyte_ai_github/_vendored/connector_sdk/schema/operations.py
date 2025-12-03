"""
Operation and PathItem models for OpenAPI 3.1.

References:
- https://spec.openapis.org/oas/v3.1.0#operation-object
- https://spec.openapis.org/oas/v3.1.0#path-item-object
"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict, model_validator

from .components import Parameter, RequestBody, Response, PathOverrideConfig
from .security import SecurityRequirement
from ..extensions import ActionTypeLiteral


class Operation(BaseModel):
    """
    Single API operation (GET, POST, PUT, PATCH, DELETE, etc.).

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#operation-object

    Extensions:
    - x-airbyte-entity: Entity name (Airbyte extension)
    - x-airbyte-action: Semantic action (Airbyte extension)
    - x-airbyte-path-override: Path override (Airbyte extension)

    Future extensions (not yet active):
    - x-airbyte-pagination: Pagination configuration for list operations
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    # Standard OpenAPI fields
    tags: Optional[List[str]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    external_docs: Optional[Dict[str, Any]] = Field(None, alias="externalDocs")
    operation_id: Optional[str] = Field(None, alias="operationId")
    parameters: Optional[List[Parameter]] = None
    request_body: Optional[RequestBody] = Field(None, alias="requestBody")
    responses: Dict[str, Response] = Field(default_factory=dict)
    callbacks: Optional[Dict[str, Any]] = None
    deprecated: Optional[bool] = None
    security: Optional[List[SecurityRequirement]] = None
    servers: Optional[List[Any]] = None  # Can override root servers

    # Airbyte extensions
    x_airbyte_entity: str = Field(..., alias="x-airbyte-entity")
    x_airbyte_action: ActionTypeLiteral = Field(..., alias="x-airbyte-action")
    x_airbyte_path_override: Optional[PathOverrideConfig] = Field(
        None,
        alias="x-airbyte-path-override",
        description=(
            "Override path for HTTP requests when OpenAPI path "
            "differs from actual endpoint"
        ),
    )
    x_airbyte_file_url: Optional[str] = Field(None, alias="x-airbyte-file-url")

    # Future extensions (commented out, defined for future use)
    # from .extensions import PaginationConfig
    # x_pagination: Optional[PaginationConfig] = Field(None, alias="x-airbyte-pagination")

    @model_validator(mode="after")
    def validate_download_action_requirements(self) -> "Operation":
        """
        Validate download operation requirements.

        Rules:
        - If x-airbyte-action is "download":
          - x-airbyte-file-url must be non-empty if provided
        - If x-airbyte-action is not "download":
          - x-airbyte-file-url must not be present
        """
        action = self.x_airbyte_action
        file_url = self.x_airbyte_file_url

        if action == "download":
            # If file_url is provided, it must be non-empty
            if file_url is not None and not file_url.strip():
                raise ValueError(
                    "x-airbyte-file-url must be non-empty when provided for download operations"
                )
        else:
            # Non-download actions cannot have file_url
            if file_url is not None:
                raise ValueError(
                    f"x-airbyte-file-url can only be used with x-airbyte-action: download, but action is '{action}'"
                )

        return self


class PathItem(BaseModel):
    """
    Path item containing operations for different HTTP methods.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#path-item-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    # Common fields for all operations
    summary: Optional[str] = None
    description: Optional[str] = None
    servers: Optional[List[Any]] = None
    parameters: Optional[List[Parameter]] = None

    # HTTP methods (all optional)
    get: Optional[Operation] = None
    put: Optional[Operation] = None
    post: Optional[Operation] = None
    delete: Optional[Operation] = None
    options: Optional[Operation] = None
    head: Optional[Operation] = None
    patch: Optional[Operation] = None
    trace: Optional[Operation] = None

    # Reference support
    ref: Optional[str] = Field(None, alias="$ref")
