"""Load and parse connector YAML configuration."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import jsonref
import yaml
from pydantic import ValidationError

from .constants import (
    OPENAPI_DEFAULT_VERSION,
    OPENAPI_VERSION_PREFIX,
)

from .types import (
    AuthConfig,
    AuthType,
    ConnectorConfig,
    ContentType,
    EndpointDefinition,
    ResourceDefinition,
    Verb,
)
from .schema import OpenAPIConnector
from .schema.components import RequestBody, GraphQLBodyConfig


class ConfigLoaderError(Exception):
    """Base exception for configuration loading errors."""

    pass


class InvalidYAMLError(ConfigLoaderError):
    """Raised when YAML syntax is invalid."""

    pass


class InvalidOpenAPIError(ConfigLoaderError):
    """Raised when OpenAPI specification is invalid."""

    pass


class DuplicateResourceError(ConfigLoaderError):
    """Raised when duplicate resource names are detected."""

    pass


def extract_path_params(path: str) -> list[str]:
    """Extract parameter names from path template.

    Example: '/v1/customers/{id}/invoices/{invoice_id}' -> ['id', 'invoice_id']
    """
    return re.findall(r"\{(\w+)\}", path)


def resolve_schema_refs(schema: Any, spec_dict: dict) -> dict[str, Any]:
    """Resolve all $ref references in a schema using jsonref.

    This handles:
    - Simple $refs to components/schemas
    - Nested $refs within schemas
    - Circular references (jsonref handles these gracefully)

    Args:
        schema: The schema that may contain $refs (can be dict or Pydantic model)
        spec_dict: The full OpenAPI spec as a dict (for reference resolution)

    Returns:
        Resolved schema as a dictionary with all $refs replaced by their definitions
    """
    if not schema:
        return {}

    # Convert schema to dict if it's a Pydantic model
    if hasattr(schema, "model_dump"):
        schema_dict = schema.model_dump(by_alias=True, exclude_none=True)
    elif isinstance(schema, dict):
        schema_dict = schema
    else:
        return {}

    # If there are no $refs, return as-is
    if "$ref" not in str(schema_dict):
        return schema_dict

    # Use jsonref to resolve all references
    # We need to embed the schema in the spec for proper reference resolution
    temp_spec = spec_dict.copy()
    temp_spec["__temp_schema__"] = schema_dict

    try:
        # Resolve all references
        resolved_spec = jsonref.replace_refs(
            temp_spec,
            base_uri="",
            jsonschema=True,  # Use JSONSchema draft 7 semantics
            lazy_load=False,  # Resolve everything immediately
        )

        # Extract our resolved schema
        resolved_schema = dict(resolved_spec.get("__temp_schema__", {}))

        # Remove any remaining jsonref proxy objects by converting to plain dict
        return _deproxy_schema(resolved_schema)
    except (jsonref.JsonRefError, KeyError, RecursionError):
        # If resolution fails, return the original schema
        # This allows the system to continue even with malformed $refs
        return schema_dict


def _deproxy_schema(obj: Any) -> Any:
    """Recursively convert jsonref proxy objects to plain dicts/lists.

    jsonref returns proxy objects that behave like dicts but aren't actual dicts.
    This converts them to plain Python objects for consistent behavior.
    """
    if isinstance(obj, dict) or (hasattr(obj, "__subject__") and hasattr(obj, "keys")):
        # Handle both dicts and jsonref proxy objects
        try:
            return {str(k): _deproxy_schema(v) for k, v in obj.items()}
        except (AttributeError, TypeError):
            return obj
    elif isinstance(obj, (list, tuple)):
        return [_deproxy_schema(item) for item in obj]
    else:
        return obj


def parse_openapi_spec(raw_config: dict) -> OpenAPIConnector:
    """Parse OpenAPI specification from YAML.

    Args:
        raw_config: Raw YAML configuration

    Returns:
        Parsed OpenAPIConnector with full validation

    Raises:
        InvalidOpenAPIError: If OpenAPI spec is invalid or missing required fields
    """
    # Validate OpenAPI version
    openapi_version = raw_config.get("openapi", "")
    if not openapi_version:
        raise InvalidOpenAPIError("Missing required field: 'openapi' version")

    # Check if version is 3.1.x (we don't support 2.x or 3.0.x)
    if not openapi_version.startswith(OPENAPI_VERSION_PREFIX):
        raise InvalidOpenAPIError(
            f"Unsupported OpenAPI version: {openapi_version}. Only {OPENAPI_VERSION_PREFIX}x is supported."
        )

    # Validate required top-level fields
    if "info" not in raw_config:
        raise InvalidOpenAPIError("Missing required field: 'info'")

    if "paths" not in raw_config:
        raise InvalidOpenAPIError("Missing required field: 'paths'")

    # Validate paths is not empty
    if not raw_config["paths"]:
        raise InvalidOpenAPIError("OpenAPI spec must have at least one path definition")

    # Parse with Pydantic validation
    try:
        spec = OpenAPIConnector(**raw_config)
    except ValidationError as e:
        raise InvalidOpenAPIError(f"OpenAPI validation failed: {e}")

    return spec


def _extract_request_body_config(
    request_body: RequestBody | None, spec_dict: dict[str, Any]
) -> tuple[list[str], dict[str, Any] | None, dict[str, Any] | None]:
    """Extract request body configuration (GraphQL or standard).

    Args:
        request_body: RequestBody object from OpenAPI operation
        spec_dict: Full OpenAPI spec dict for $ref resolution

    Returns:
        Tuple of (body_fields, request_schema, graphql_body)
        - body_fields: List of field names for standard JSON/form bodies
        - request_schema: Resolved request schema dict (for standard bodies)
        - graphql_body: GraphQL body configuration dict (for GraphQL bodies)
    """
    body_fields: list[str] = []
    request_schema: dict[str, Any] | None = None
    graphql_body: dict[str, Any] | None = None

    if not request_body:
        return body_fields, request_schema, graphql_body

    # Check for GraphQL extension and extract GraphQL body configuration
    if request_body.x_airbyte_body_type:
        body_type_config = request_body.x_airbyte_body_type

        # Check if it's GraphQL type (it's a GraphQLBodyConfig Pydantic model)
        if isinstance(body_type_config, GraphQLBodyConfig):
            # Convert Pydantic model to dict, excluding None values
            graphql_body = body_type_config.model_dump(
                exclude_none=True, by_alias=False
            )
            return body_fields, request_schema, graphql_body

    # Parse standard request body
    for content_type_key, media_type in request_body.content.items():
        # media_type is now a MediaType object with schema_ field
        schema = media_type.schema_ or {}

        # Resolve all $refs in the schema using jsonref
        request_schema = resolve_schema_refs(schema, spec_dict)

        # Extract body field names from resolved schema
        if isinstance(request_schema, dict) and "properties" in request_schema:
            body_fields = list(request_schema["properties"].keys())

    return body_fields, request_schema, graphql_body


def convert_openapi_to_connector_config(spec: OpenAPIConnector) -> ConnectorConfig:
    """Convert OpenAPI spec to ConnectorConfig format.

    Args:
        spec: OpenAPI connector specification (fully validated)

    Returns:
        ConnectorConfig with resources and endpoints
    """
    # Convert spec to dict for jsonref resolution
    spec_dict = spec.model_dump(by_alias=True, exclude_none=True)

    # Extract connector name and version
    name = spec.info.x_airbyte_connector_name or spec.info.title.lower().replace(
        " ", "-"
    )
    version = spec.info.version

    # Extract base URL from servers
    base_url = spec.servers[0].url if spec.servers else ""

    # Parse authentication
    auth_config = _parse_auth_from_openapi(spec)

    # Group operations by resource
    resources_map: dict[str, dict[str, EndpointDefinition]] = {}

    for path, path_item in spec.paths.items():
        # Check each HTTP method
        for method_name in ["get", "post", "put", "delete", "patch"]:
            operation = getattr(path_item, method_name, None)
            if not operation:
                continue

            # Extract resource and verb from x-resource and x-verb
            resource_name = operation.x_airbyte_resource
            verb_name = operation.x_airbyte_verb
            path_override = operation.x_airbyte_path_override

            if not resource_name:
                raise InvalidOpenAPIError(
                    f"Missing required x-airbyte-resource in operation {method_name.upper()} {path}. "
                    f"All operations must specify a resource."
                )

            if not verb_name:
                raise InvalidOpenAPIError(
                    f"Missing required x-airbyte-verb in operation {method_name.upper()} {path}. "
                    f"All operations must specify a verb."
                )

            # Convert to Verb enum
            try:
                verb = Verb(verb_name)
            except ValueError:
                # Provide clear error for invalid verbs
                valid_verbs = ", ".join([v.value for v in Verb])
                raise InvalidOpenAPIError(
                    f"Invalid verb '{verb_name}' in operation {method_name.upper()} {path}. "
                    f"Valid verbs are: {valid_verbs}"
                )

            # Determine content type
            content_type = ContentType.JSON
            if operation.request_body and operation.request_body.content:
                if (
                    "application/x-www-form-urlencoded"
                    in operation.request_body.content
                ):
                    content_type = ContentType.FORM_URLENCODED
                elif "multipart/form-data" in operation.request_body.content:
                    content_type = ContentType.FORM_DATA

            # Extract parameters
            path_params = []
            query_params = []
            if operation.parameters:
                for param in operation.parameters:
                    if param.in_ == "path":
                        path_params.append(param.name)
                    elif param.in_ == "query":
                        query_params.append(param.name)

            # Extract body fields from request schema
            body_fields, request_schema, graphql_body = _extract_request_body_config(
                operation.request_body, spec_dict
            )

            # Extract response schema
            response_schema = None
            if "200" in operation.responses:
                response = operation.responses["200"]
                if response.content and "application/json" in response.content:
                    media_type = response.content["application/json"]
                    schema = media_type.schema_ if media_type else {}

                    # Resolve all $refs in the response schema using jsonref
                    response_schema = resolve_schema_refs(schema, spec_dict)

            # Create endpoint definition
            endpoint = EndpointDefinition(
                method=method_name.upper(),
                path=path,
                path_override=path_override,
                description=operation.description or operation.summary,
                body_fields=body_fields,
                query_params=query_params,
                path_params=path_params,
                content_type=content_type,
                request_schema=request_schema,
                response_schema=response_schema,
                graphql_body=graphql_body,
            )

            # Add to resources map
            if resource_name not in resources_map:
                resources_map[resource_name] = {}
            resources_map[resource_name][verb] = endpoint

    # Note: No need to check for duplicate resource names - the dict structure
    # automatically ensures uniqueness. If the OpenAPI spec contains duplicate
    # operationIds, only the last one will be kept.

    # Convert resources map to ResourceDefinition list
    resources = []
    for resource_name, endpoints_dict in resources_map.items():
        verbs = list(endpoints_dict.keys())

        # Get schema from components if available
        schema = None
        if spec.components:
            # Look for a schema matching the resource name
            for schema_name, schema_def in spec.components.schemas.items():
                if (
                    schema_def.x_airbyte_resource_name == resource_name
                    or schema_name.lower() == resource_name.lower()
                ):
                    schema = schema_def.model_dump(by_alias=True)
                    break

        resource = ResourceDefinition(
            name=resource_name, verbs=verbs, endpoints=endpoints_dict, schema=schema
        )
        resources.append(resource)

    # Create ConnectorConfig
    config = ConnectorConfig(
        name=name,
        version=version,
        base_url=base_url,
        auth=auth_config,
        resources=resources,
        openapi_spec=spec,
    )

    return config


def _parse_auth_from_openapi(spec: OpenAPIConnector) -> AuthConfig:
    """Parse authentication configuration from OpenAPI spec.

    Args:
        spec: OpenAPI connector specification

    Returns:
        AuthConfig
    """
    if not spec.components or not spec.components.security_schemes:
        return AuthConfig(type=AuthType.API_KEY, config={})

    # Get the first security scheme
    scheme_name, scheme = next(iter(spec.components.security_schemes.items()))

    if scheme.type == "http":
        if scheme.scheme == "bearer":
            return AuthConfig(
                type=AuthType.BEARER,
                config={"header": "Authorization", "prefix": "Bearer"},
            )
        elif scheme.scheme == "basic":
            return AuthConfig(type=AuthType.BASIC, config={})

    elif scheme.type == "apiKey":
        return AuthConfig(
            type=AuthType.API_KEY,
            config={
                "header": scheme.name or "Authorization",
                "in": scheme.in_ or "header",
            },
        )

    # Default fallback
    return AuthConfig(type=AuthType.API_KEY, config={})


def load_connector_config(config_path: str | Path) -> ConnectorConfig:
    """Load connector configuration from YAML file.

    Supports both OpenAPI 3.1 format and legacy format.

    Args:
        config_path: Path to connector.yaml file

    Returns:
        Parsed ConnectorConfig

    Raises:
        FileNotFoundError: If config file doesn't exist
        ValueError: If YAML is invalid
    """
    config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Connector config not found: {config_path}")

    # Load YAML with error handling
    try:
        with open(config_path) as f:
            raw_config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise InvalidYAMLError(f"Invalid YAML syntax in {config_path}: {e}")
    except Exception as e:
        raise ConfigLoaderError(f"Error reading config file {config_path}: {e}")

    if not raw_config:
        raise ValueError("Invalid connector.yaml: empty file")

    # Detect format: OpenAPI if 'openapi' key exists
    if "openapi" in raw_config:
        spec = parse_openapi_spec(raw_config)
        return convert_openapi_to_connector_config(spec)

    # Legacy format
    if "connector" not in raw_config:
        raise ValueError("Invalid connector.yaml: missing 'connector' or 'openapi' key")

    # Parse connector metadata
    connector_meta = raw_config["connector"]

    # Parse auth config
    auth_config = raw_config.get("auth", {})

    # Parse resources
    resources = []
    for resource_data in raw_config.get("resources", []):
        # Parse endpoints for each verb
        endpoints_dict = {}
        for verb_str in resource_data.get("verbs", []):
            verb = Verb(verb_str)
            endpoint_data = resource_data["endpoints"].get(verb_str)

            if endpoint_data:
                # Extract path parameters from the path template
                path_params = extract_path_params(endpoint_data["path"])

                endpoint = EndpointDefinition(
                    method=endpoint_data["method"],
                    path=endpoint_data["path"],
                    description=endpoint_data.get("description"),
                    body_fields=endpoint_data.get("body_fields", []),
                    query_params=endpoint_data.get("query_params", []),
                    path_params=path_params,
                    graphql_body=None,  # GraphQL only supported in OpenAPI format (via x-airbyte-body-type)
                )
                endpoints_dict[verb] = endpoint

        resource = ResourceDefinition(
            name=resource_data["name"],
            verbs=[Verb(v) for v in resource_data["verbs"]],
            endpoints=endpoints_dict,
            schema=resource_data.get("schema"),
        )
        resources.append(resource)

    # Build ConnectorConfig
    config = ConnectorConfig(
        name=connector_meta["name"],
        version=connector_meta.get("version", OPENAPI_DEFAULT_VERSION),
        base_url=raw_config.get("base_url", connector_meta.get("base_url", "")),
        auth=auth_config,
        resources=resources,
    )

    return config
