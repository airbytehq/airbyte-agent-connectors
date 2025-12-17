"""Load and parse connector YAML definitions into ConnectorModel objects."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any
from uuid import UUID

import jsonref
import yaml
from pydantic import ValidationError

from .constants import (
    OPENAPI_DEFAULT_VERSION,
    OPENAPI_VERSION_PREFIX,
)

from .schema import OpenAPIConnector
from .schema.components import GraphQLBodyConfig, RequestBody
from .schema.security import AirbyteAuthConfig, AuthConfigFieldSpec
from .types import (
    Action,
    AuthConfig,
    AuthOption,
    AuthType,
    ConnectorModel,
    ContentType,
    EndpointDefinition,
    EntityDefinition,
)


class ConnectorModelLoaderError(Exception):
    """Base exception for connector model loading errors."""

    pass


class InvalidYAMLError(ConnectorModelLoaderError):
    """Raised when YAML syntax is invalid."""

    pass


class InvalidOpenAPIError(ConnectorModelLoaderError):
    """Raised when OpenAPI specification is invalid."""

    pass


class DuplicateEntityError(ConnectorModelLoaderError):
    """Raised when duplicate entity names are detected."""

    pass


class TokenExtractValidationError(ConnectorModelLoaderError):
    """Raised when x-airbyte-token-extract references invalid server variables."""

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
        resolved_spec = jsonref.replace_refs(  # type: ignore[union-attr]
            temp_spec,
            base_uri="",
            jsonschema=True,  # Use JSONSchema draft 7 semantics
            lazy_load=False,  # Resolve everything immediately
        )

        # Extract our resolved schema
        resolved_schema = dict(resolved_spec.get("__temp_schema__", {}))

        # Remove any remaining jsonref proxy objects by converting to plain dict
        return _deproxy_schema(resolved_schema)
    except (AttributeError, KeyError, RecursionError, Exception):
        # If resolution fails, return the original schema
        # This allows the system to continue even with malformed $refs
        # AttributeError covers the case where jsonref might be None
        # Exception catches jsonref.JsonRefError and other jsonref exceptions
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
        raise InvalidOpenAPIError(f"Unsupported OpenAPI version: {openapi_version}. Only {OPENAPI_VERSION_PREFIX}x is supported.")

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
            graphql_body = body_type_config.model_dump(exclude_none=True, by_alias=False)
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


def convert_openapi_to_connector_model(spec: OpenAPIConnector) -> ConnectorModel:
    """Convert OpenAPI spec to ConnectorModel format.

    Args:
        spec: OpenAPI connector specification (fully validated)

    Returns:
        ConnectorModel with entities and endpoints
    """
    # Validate x-airbyte-token-extract against server variables
    _validate_token_extract(spec)

    # Convert spec to dict for jsonref resolution
    spec_dict = spec.model_dump(by_alias=True, exclude_none=True)

    # Extract connector name and version
    name = spec.info.x_airbyte_connector_name or spec.info.title.lower().replace(" ", "-")
    version = spec.info.version

    # Parse authentication first to get token_extract fields
    auth_config = _parse_auth_from_openapi(spec)

    # Extract base URL from servers - keep variable placeholders intact
    # Variables will be substituted at runtime by HTTPClient using:
    # - config_values: for user-provided values like subdomain
    # - token_extract: for OAuth dynamic values like instance_url
    # DO NOT substitute defaults here - that would prevent runtime substitution
    base_url = ""
    if spec.servers:
        base_url = spec.servers[0].url

    # Group operations by entity
    entities_map: dict[str, dict[str, EndpointDefinition]] = {}

    for path, path_item in spec.paths.items():
        # Check each HTTP method
        for method_name in ["get", "post", "put", "delete", "patch"]:
            operation = getattr(path_item, method_name, None)
            if not operation:
                continue

            # Extract entity and action from x-airbyte-entity and x-airbyte-action
            entity_name = operation.x_airbyte_entity
            action_name = operation.x_airbyte_action
            path_override = operation.x_airbyte_path_override
            record_extractor = operation.x_airbyte_record_extractor
            meta_extractor = operation.x_airbyte_meta_extractor

            if not entity_name:
                raise InvalidOpenAPIError(
                    f"Missing required x-airbyte-entity in operation {method_name.upper()} {path}. All operations must specify an entity."
                )

            if not action_name:
                raise InvalidOpenAPIError(
                    f"Missing required x-airbyte-action in operation {method_name.upper()} {path}. All operations must specify an action."
                )

            # Convert to Action enum
            try:
                action = Action(action_name)
            except ValueError:
                # Provide clear error for invalid actions
                valid_actions = ", ".join([a.value for a in Action])
                raise InvalidOpenAPIError(
                    f"Invalid action '{action_name}' in operation {method_name.upper()} {path}. Valid actions are: {valid_actions}"
                )

            # Determine content type
            content_type = ContentType.JSON
            if operation.request_body and operation.request_body.content:
                if "application/x-www-form-urlencoded" in operation.request_body.content:
                    content_type = ContentType.FORM_URLENCODED
                elif "multipart/form-data" in operation.request_body.content:
                    content_type = ContentType.FORM_DATA

            # Extract parameters with their schemas (including defaults)
            path_params: list[str] = []
            path_params_schema: dict[str, dict[str, Any]] = {}
            query_params: list[str] = []
            query_params_schema: dict[str, dict[str, Any]] = {}
            deep_object_params: list[str] = []

            if operation.parameters:
                for param in operation.parameters:
                    param_schema = param.schema_ or {}
                    schema_info = {
                        "type": param_schema.get("type", "string"),
                        "required": param.required or False,
                        "default": param_schema.get("default"),
                    }

                    if param.in_ == "path":
                        path_params.append(param.name)
                        # Path params are always required
                        schema_info["required"] = True
                        path_params_schema[param.name] = schema_info
                    elif param.in_ == "query":
                        query_params.append(param.name)
                        query_params_schema[param.name] = schema_info
                        # Check if this is a deepObject style parameter
                        if hasattr(param, "style") and param.style == "deepObject":
                            deep_object_params.append(param.name)

            # Extract body fields from request schema
            body_fields, request_schema, graphql_body = _extract_request_body_config(operation.request_body, spec_dict)

            # Extract response schema
            response_schema = None
            if "200" in operation.responses:
                response = operation.responses["200"]
                if response.content and "application/json" in response.content:
                    media_type = response.content["application/json"]
                    schema = media_type.schema_ if media_type else {}

                    # Resolve all $refs in the response schema using jsonref
                    response_schema = resolve_schema_refs(schema, spec_dict)

            # Extract file_field for download operations
            file_field = getattr(operation, "x_airbyte_file_url", None)

            # Extract untested flag
            untested = getattr(operation, "x_airbyte_untested", None) or False

            # Create endpoint definition
            endpoint = EndpointDefinition(
                method=method_name.upper(),
                action=action,
                path=path,
                path_override=path_override,
                record_extractor=record_extractor,
                meta_extractor=meta_extractor,
                description=operation.description or operation.summary,
                body_fields=body_fields,
                query_params=query_params,
                query_params_schema=query_params_schema,
                deep_object_params=deep_object_params,
                path_params=path_params,
                path_params_schema=path_params_schema,
                content_type=content_type,
                request_schema=request_schema,
                response_schema=response_schema,
                graphql_body=graphql_body,
                file_field=file_field,
                untested=untested,
            )

            # Add to entities map
            if entity_name not in entities_map:
                entities_map[entity_name] = {}
            entities_map[entity_name][action] = endpoint

    # Note: No need to check for duplicate entity names - the dict structure
    # automatically ensures uniqueness. If the OpenAPI spec contains duplicate
    # operationIds, only the last one will be kept.

    # Convert entities map to EntityDefinition list
    entities = []
    for entity_name, endpoints_dict in entities_map.items():
        actions = list(endpoints_dict.keys())

        # Get schema from components if available
        schema = None
        if spec.components:
            # Look for a schema matching the entity name
            for schema_name, schema_def in spec.components.schemas.items():
                if schema_def.x_airbyte_entity_name == entity_name or schema_name.lower() == entity_name.lower():
                    schema = schema_def.model_dump(by_alias=True)
                    break

        entity = EntityDefinition(name=entity_name, actions=actions, endpoints=endpoints_dict, schema=schema)
        entities.append(entity)

    # Extract retry config from x-airbyte-retry-config extension
    retry_config = spec.info.x_airbyte_retry_config
    connector_id = spec.info.x_airbyte_connector_id
    if not connector_id:
        raise InvalidOpenAPIError("Missing required x-airbyte-connector-id field")

    # Create ConnectorModel
    model = ConnectorModel(
        id=connector_id,
        name=name,
        version=version,
        base_url=base_url,
        auth=auth_config,
        entities=entities,
        openapi_spec=spec,
        retry_config=retry_config,
    )

    return model


def _get_attribute_flexible(obj: Any, *names: str) -> Any:
    """Get attribute from object, trying multiple name variants.

    Supports both snake_case and camelCase attribute names.
    Returns None if no variant is found.

    Args:
        obj: Object to get attribute from
        *names: Attribute names to try in order

    Returns:
        Attribute value if found, None otherwise

    Example:
        # Try both "refresh_url" and "refreshUrl"
        url = _get_attribute_flexible(flow, "refresh_url", "refreshUrl")
    """
    for name in names:
        value = getattr(obj, name, None)
        if value is not None:
            return value
    return None


def _select_oauth2_flow(flows: Any) -> Any:
    """Select the best OAuth2 flow from available flows.

    Prefers authorizationCode (most secure for web apps), but falls back
    to other flow types if not available.

    Args:
        flows: OAuth2 flows object from OpenAPI spec

    Returns:
        Selected flow object, or None if no flows available
    """
    # Priority order: authorizationCode > clientCredentials > password > implicit
    flow_names = [
        ("authorization_code", "authorizationCode"),  # Preferred
        ("client_credentials", "clientCredentials"),  # Server-to-server
        ("password", "password"),  # Resource owner
        ("implicit", "implicit"),  # Legacy, less secure
    ]

    for snake_case, camel_case in flow_names:
        flow = _get_attribute_flexible(flows, snake_case, camel_case)
        if flow:
            return flow

    return None


def _parse_oauth2_config(scheme: Any) -> dict[str, str]:
    """Parse OAuth2 authentication configuration from OpenAPI scheme.

    Extracts configuration from standard OAuth2 flows and custom x-airbyte-token-refresh
    extension for additional refresh behavior customization.

    Args:
        scheme: OAuth2 security scheme from OpenAPI spec

    Returns:
        Dictionary with OAuth2 configuration including:
        - header: Authorization header name (default: "Authorization")
        - prefix: Token prefix (default: "Bearer")
        - refresh_url: Token refresh endpoint (from flows)
        - auth_style: How to send credentials (from x-airbyte-token-refresh)
        - body_format: Request encoding (from x-airbyte-token-refresh)
    """
    config: dict[str, str] = {
        "header": "Authorization",
        "prefix": "Bearer",
    }

    # Extract flow information for refresh_url
    if scheme.flows:
        flow = _select_oauth2_flow(scheme.flows)
        if flow:
            # Try to get refresh URL (supports both naming conventions)
            refresh_url = _get_attribute_flexible(flow, "refresh_url", "refreshUrl")
            if refresh_url:
                config["refresh_url"] = refresh_url

    # Extract custom refresh configuration from x-airbyte-token-refresh extension
    x_token_refresh = getattr(scheme, "x_token_refresh", None)
    if x_token_refresh:
        auth_style = getattr(x_token_refresh, "auth_style", None)
        if auth_style:
            config["auth_style"] = auth_style

        body_format = getattr(x_token_refresh, "body_format", None)
        if body_format:
            config["body_format"] = body_format

    # Extract token_extract fields from x-airbyte-token-extract extension
    x_token_extract = getattr(scheme, "x_airbyte_token_extract", None)
    if x_token_extract:
        config["token_extract"] = x_token_extract

    return config


def _validate_token_extract(spec: OpenAPIConnector) -> None:
    """Validate x-airbyte-token-extract against server variables.

    Ensures that fields specified in x-airbyte-token-extract match defined
    server variables. This catches configuration errors at load time rather
    than at runtime during token refresh.

    Args:
        spec: OpenAPI connector specification

    Raises:
        TokenExtractValidationError: If token_extract fields don't match server variables
    """
    # Get server variables
    server_variables: set[str] = set()
    if spec.servers:
        for server in spec.servers:
            if server.variables:
                server_variables.update(server.variables.keys())

    # Get token_extract from security scheme
    if not spec.components or not spec.components.security_schemes:
        return

    for scheme_name, scheme in spec.components.security_schemes.items():
        if scheme.type != "oauth2":
            continue

        token_extract = getattr(scheme, "x_airbyte_token_extract", None)
        if not token_extract:
            continue

        # Validate each field matches a server variable
        for field in token_extract:
            if field not in server_variables:
                raise TokenExtractValidationError(
                    f"x-airbyte-token-extract field '{field}' does not match any defined "
                    f"server variable. Available server variables: {sorted(server_variables) or 'none'}. "
                    f"Please define '{{{field}}}' in your server URL and add a variable definition."
                )


def _generate_default_auth_config(auth_type: AuthType) -> AirbyteAuthConfig:
    """Generate default x-airbyte-auth-config for an auth type.

    When x-airbyte-auth-config is not explicitly defined in the OpenAPI spec,
    we generate a sensible default that maps user-friendly field names to
    the auth scheme's parameters.

    Args:
        auth_type: The authentication type (BEARER, BASIC, API_KEY)

    Returns:
        Default auth config spec with properties and auth_mapping
    """
    if auth_type == AuthType.BEARER:
        return AirbyteAuthConfig(
            title=None,
            description=None,
            type="object",
            required=["token"],
            properties={
                "token": AuthConfigFieldSpec(
                    type="string",
                    title="Bearer Token",
                    description="Authentication bearer token",
                    format=None,
                    pattern=None,
                    airbyte_secret=False,
                    default=None,
                )
            },
            auth_mapping={"token": "${token}"},
            oneOf=None,
        )
    elif auth_type == AuthType.BASIC:
        return AirbyteAuthConfig(
            title=None,
            description=None,
            type="object",
            required=["username", "password"],
            properties={
                "username": AuthConfigFieldSpec(
                    type="string",
                    title="Username",
                    description="Authentication username",
                    format=None,
                    pattern=None,
                    airbyte_secret=False,
                    default=None,
                ),
                "password": AuthConfigFieldSpec(
                    type="string",
                    title="Password",
                    description="Authentication password",
                    format=None,
                    pattern=None,
                    airbyte_secret=False,
                    default=None,
                ),
            },
            auth_mapping={"username": "${username}", "password": "${password}"},
            oneOf=None,
        )
    elif auth_type == AuthType.API_KEY:
        return AirbyteAuthConfig(
            title=None,
            description=None,
            type="object",
            required=["api_key"],
            properties={
                "api_key": AuthConfigFieldSpec(
                    type="string",
                    title="API Key",
                    description="API authentication key",
                    format=None,
                    pattern=None,
                    airbyte_secret=False,
                    default=None,
                )
            },
            auth_mapping={"api_key": "${api_key}"},
            oneOf=None,
        )
    elif auth_type == AuthType.OAUTH2:
        # OAuth2: No fields are strictly required to support both modes:
        # 1. Full token mode: user provides access_token (and optionally refresh credentials)
        # 2. Refresh-token-only mode: user provides refresh_token, client_id, client_secret
        # The auth_mapping includes all fields, but apply_auth_mapping
        # will skip mappings for fields not provided by the user.
        return AirbyteAuthConfig(
            title=None,
            description=None,
            type="object",
            required=[],
            properties={
                "access_token": AuthConfigFieldSpec(
                    type="string",
                    title="Access Token",
                    description="OAuth2 access token",
                    format=None,
                    pattern=None,
                    airbyte_secret=False,
                    default=None,
                ),
                "refresh_token": AuthConfigFieldSpec(
                    type="string",
                    title="Refresh Token",
                    description="OAuth2 refresh token (optional)",
                    format=None,
                    pattern=None,
                    airbyte_secret=False,
                    default=None,
                ),
                "client_id": AuthConfigFieldSpec(
                    type="string",
                    title="Client ID",
                    description="OAuth2 client ID (optional)",
                    format=None,
                    pattern=None,
                    airbyte_secret=False,
                    default=None,
                ),
                "client_secret": AuthConfigFieldSpec(
                    type="string",
                    title="Client Secret",
                    description="OAuth2 client secret (optional)",
                    format=None,
                    pattern=None,
                    airbyte_secret=False,
                    default=None,
                ),
            },
            auth_mapping={
                "access_token": "${access_token}",
                "refresh_token": "${refresh_token}",
                "client_id": "${client_id}",
                "client_secret": "${client_secret}",
            },
            oneOf=None,
        )
    else:
        # Unknown auth type - return minimal config
        return AirbyteAuthConfig(
            title=None,
            description=None,
            type="object",
            required=None,
            properties={},
            auth_mapping={},
            oneOf=None,
        )


def _parse_auth_from_openapi(spec: OpenAPIConnector) -> AuthConfig:
    """Parse authentication configuration from OpenAPI spec.

    Supports both single and multiple security schemes. For backwards compatibility,
    single-scheme connectors continue to use the legacy AuthConfig format.
    If no security schemes are defined, generates a default Bearer auth config.

    Args:
        spec: OpenAPI connector specification

    Returns:
        AuthConfig with either single or multiple auth options
    """
    if not spec.components or not spec.components.security_schemes:
        # Backwards compatibility: generate default Bearer auth when no schemes defined
        default_config = _generate_default_auth_config(AuthType.BEARER)
        return AuthConfig(
            type=AuthType.BEARER,
            config={"header": "Authorization", "prefix": "Bearer"},
            user_config_spec=default_config,
            options=None,
        )

    schemes = spec.components.security_schemes

    # Single scheme: backwards compatible mode
    if len(schemes) == 1:
        scheme_name, scheme = next(iter(schemes.items()))
        return _parse_single_security_scheme(scheme)

    # Multiple schemes: new multi-auth mode
    options = []
    for scheme_name, scheme in schemes.items():
        try:
            auth_option = _parse_security_scheme_to_option(scheme_name, scheme)
            options.append(auth_option)
        except Exception as e:
            # Log warning but continue - skip invalid schemes
            import logging

            logger = logging.getLogger(__name__)
            logger.warning(f"Skipping invalid security scheme '{scheme_name}': {e}")
            continue

    if not options:
        raise InvalidOpenAPIError("No valid security schemes found. Connector must define at least one valid security scheme.")

    return AuthConfig(
        type=None,
        config={},
        user_config_spec=None,
        options=options,
    )


def _parse_single_security_scheme(scheme: Any) -> AuthConfig:
    """Parse a single security scheme into AuthConfig.

    This extracts the existing single-scheme parsing logic for reuse.

    Args:
        scheme: SecurityScheme from OpenAPI spec

    Returns:
        AuthConfig in single-auth mode
    """
    auth_type = AuthType.API_KEY  # Default
    auth_config = {}

    if scheme.type == "http":
        if scheme.scheme == "bearer":
            auth_type = AuthType.BEARER
            auth_config = {"header": "Authorization", "prefix": "Bearer"}
        elif scheme.scheme == "basic":
            auth_type = AuthType.BASIC
            auth_config = {}

    elif scheme.type == "apiKey":
        auth_type = AuthType.API_KEY
        auth_config = {
            "header": scheme.name or "Authorization",
            "in": scheme.in_ or "header",
        }

    elif scheme.type == "oauth2":
        # Parse OAuth2 configuration
        oauth2_config = _parse_oauth2_config(scheme)
        # Use explicit x-airbyte-auth-config if present, otherwise generate default
        auth_config_obj = scheme.x_airbyte_auth_config or _generate_default_auth_config(AuthType.OAUTH2)
        return AuthConfig(
            type=AuthType.OAUTH2,
            config=oauth2_config,
            user_config_spec=auth_config_obj,
            options=None,
        )

    # Use explicit x-airbyte-auth-config if present, otherwise generate default
    auth_config_obj = scheme.x_airbyte_auth_config or _generate_default_auth_config(auth_type)

    return AuthConfig(
        type=auth_type,
        config=auth_config,
        user_config_spec=auth_config_obj,
        options=None,
    )


def _parse_security_scheme_to_option(scheme_name: str, scheme: Any) -> AuthOption:
    """Parse a security scheme into an AuthOption for multi-auth connectors.

    Args:
        scheme_name: Name of the security scheme (e.g., "githubOAuth")
        scheme: SecurityScheme from OpenAPI spec

    Returns:
        AuthOption containing the parsed configuration

    Raises:
        ValueError: If scheme is invalid or unsupported
    """
    # Parse using existing single-scheme logic
    single_auth = _parse_single_security_scheme(scheme)

    # Convert to AuthOption
    return AuthOption(
        scheme_name=scheme_name,
        type=single_auth.type,
        config=single_auth.config,
        user_config_spec=single_auth.user_config_spec,
    )


def load_connector_model(definition_path: str | Path) -> ConnectorModel:
    """Load connector model from YAML definition file.

    Supports both OpenAPI 3.1 format and legacy format.

    Args:
        definition_path: Path to connector.yaml file

    Returns:
        Parsed ConnectorModel

    Raises:
        FileNotFoundError: If definition file doesn't exist
        ValueError: If YAML is invalid
    """
    definition_path = Path(definition_path)

    if not definition_path.exists():
        raise FileNotFoundError(f"Connector definition not found: {definition_path}")

    # Load YAML with error handling
    try:
        with open(definition_path) as f:
            raw_definition = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise InvalidYAMLError(f"Invalid YAML syntax in {definition_path}: {e}")
    except Exception as e:
        raise ConnectorModelLoaderError(f"Error reading definition file {definition_path}: {e}")

    if not raw_definition:
        raise ValueError("Invalid connector.yaml: empty file")

    # Detect format: OpenAPI if 'openapi' key exists
    if "openapi" in raw_definition:
        spec = parse_openapi_spec(raw_definition)
        return convert_openapi_to_connector_model(spec)

    # Legacy format
    if "connector" not in raw_definition:
        raise ValueError("Invalid connector.yaml: missing 'connector' or 'openapi' key")

    # Parse connector metadata
    connector_meta = raw_definition["connector"]

    # Parse auth config
    auth_config = raw_definition.get("auth", {})

    # Parse entities
    entities = []
    for entity_data in raw_definition.get("entities", []):
        # Parse endpoints for each action
        endpoints_dict = {}
        for action_str in entity_data.get("actions", []):
            action = Action(action_str)
            endpoint_data = entity_data["endpoints"].get(action_str)

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
                endpoints_dict[action] = endpoint

        entity = EntityDefinition(
            name=entity_data["name"],
            actions=[Action(a) for a in entity_data["actions"]],
            endpoints=endpoints_dict,
            schema=entity_data.get("schema"),
        )
        entities.append(entity)

    # Get connector ID
    connector_id_value = connector_meta.get("id")
    if connector_id_value:
        # Try to parse as UUID (handles string UUIDs)
        if isinstance(connector_id_value, str):
            connector_id = UUID(connector_id_value)
        else:
            connector_id = connector_id_value
    else:
        raise ValueError

    # Build ConnectorModel
    model = ConnectorModel(
        id=connector_id,
        name=connector_meta["name"],
        version=connector_meta.get("version", OPENAPI_DEFAULT_VERSION),
        base_url=raw_definition.get("base_url", connector_meta.get("base_url", "")),
        auth=auth_config,
        entities=entities,
    )

    return model
