"""
Operation and PathItem models for OpenAPI 3.1.

References:
- https://spec.openapis.org/oas/v3.1.0#operation-object
- https://spec.openapis.org/oas/v3.1.0#path-item-object
"""

from typing import Any, Dict, List

from pydantic import BaseModel, ConfigDict, Field, model_validator

from ..extensions import ActionTypeLiteral
from .components import Parameter, PathOverrideConfig, RequestBody, Response
from .security import SecurityRequirement


class Operation(BaseModel):
    """
    Single API operation (GET, POST, PUT, PATCH, DELETE, etc.).

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#operation-object

    Extensions:
    - x-airbyte-entity: Entity name (Airbyte extension)
    - x-airbyte-action: Semantic action (Airbyte extension)
    - x-airbyte-path-override: Path override (Airbyte extension)
    - x-airbyte-record-extractor: JSONPath to extract records from response (Airbyte extension)

    Future extensions (not yet active):
    - x-airbyte-pagination: Pagination configuration for list operations
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    # Standard OpenAPI fields
    tags: List[str] | None = None
    summary: str | None = None
    description: str | None = None
    external_docs: Dict[str, Any] | None = Field(None, alias="externalDocs")
    operation_id: str | None = Field(None, alias="operationId")
    parameters: List[Parameter] | None = None
    request_body: RequestBody | None = Field(None, alias="requestBody")
    responses: Dict[str, Response] = Field(default_factory=dict)
    callbacks: Dict[str, Any] | None = None
    deprecated: bool | None = None
    security: List[SecurityRequirement] | None = None
    servers: List[Any] | None = None  # Can override root servers

    # Airbyte extensions
    x_airbyte_entity: str = Field(..., alias="x-airbyte-entity")
    x_airbyte_action: ActionTypeLiteral = Field(..., alias="x-airbyte-action")
    x_airbyte_path_override: PathOverrideConfig | None = Field(
        None,
        alias="x-airbyte-path-override",
        description=("Override path for HTTP requests when OpenAPI path differs from actual endpoint"),
    )
    x_airbyte_record_extractor: str | None = Field(
        None,
        alias="x-airbyte-record-extractor",
        description=(
            "JSONPath expression to extract records from API response envelopes. "
            "When specified, executor extracts data at this path instead of returning "
            "full response. Returns array for list/api_search actions, single record for "
            "get/create/update/delete actions."
        ),
    )
    x_airbyte_meta_extractor: Dict[str, str] | None = Field(
        None,
        alias="x-airbyte-meta-extractor",
        description=(
            "Dictionary mapping field names to JSONPath expressions for extracting "
            "metadata (pagination info, request IDs, etc.) from API response envelopes. "
            "Each key becomes a field in ExecutionResult.meta with the value extracted "
            "using the corresponding JSONPath expression. "
            "Example: {'pagination': '$.pagination', 'request_id': '$.requestId'}"
        ),
    )
    x_airbyte_file_url: str | None = Field(None, alias="x-airbyte-file-url")
    x_airbyte_untested: bool | None = Field(
        None,
        alias="x-airbyte-untested",
        description=(
            "Mark operation as untested to skip cassette validation in readiness checks. "
            "Use this for operations that cannot be recorded (e.g., webhooks, real-time streams). "
            "Validation will generate a warning instead of an error when cassettes are missing."
        ),
    )
    x_airbyte_preferred_for_check: bool | None = Field(
        None,
        alias="x-airbyte-preferred-for-check",
        description=(
            "Mark this list operation as the preferred operation for health checks. "
            "When the CHECK action is executed, this operation will be used instead of "
            "falling back to the first available list operation. Choose a lightweight, "
            "always-available endpoint (e.g., users, accounts)."
        ),
    )

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
                raise ValueError("x-airbyte-file-url must be non-empty when provided for download operations")
        else:
            # Non-download actions cannot have file_url
            if file_url is not None:
                raise ValueError(f"x-airbyte-file-url can only be used with x-airbyte-action: download, but action is '{action}'")

        return self


class PathItem(BaseModel):
    """
    Path item containing operations for different HTTP methods.

    OpenAPI Reference: https://spec.openapis.org/oas/v3.1.0#path-item-object
    """

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    # Common fields for all operations
    summary: str | None = None
    description: str | None = None
    servers: List[Any] | None = None
    parameters: List[Parameter] | None = None

    # HTTP methods (all optional)
    get: Operation | None = None
    put: Operation | None = None
    post: Operation | None = None
    delete: Operation | None = None
    options: Operation | None = None
    head: Operation | None = None
    patch: Operation | None = None
    trace: Operation | None = None

    # Reference support
    ref: str | None = Field(None, alias="$ref")
