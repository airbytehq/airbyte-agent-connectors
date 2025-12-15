"""
Validation tools for connector readiness and schema compliance.

These tools help ensure that connectors are ready to ship by:
- Checking that all entity/action operations have corresponding test cassettes
- Validating that response schemas match the actual cassette responses
- Detecting fields present in responses but not declared in schemas
"""

from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

import jsonschema
import yaml
from jsonpath_ng import parse as parse_jsonpath

from .connector_model_loader import (
    ConnectorModelLoaderError,
    load_connector_model,
)
from .testing.spec_loader import load_test_spec
from .types import Action, EndpointDefinition


def build_cassette_map(cassettes_dir: Path) -> Dict[Tuple[str, str], List[Path]]:
    """Build a map of (entity, action) -> list of cassette paths.

    Reads the entity/action from TestSpec.entity and TestSpec.action fields,
    not from the filename.

    Args:
        cassettes_dir: Directory containing cassette YAML files

    Returns:
        Dictionary mapping (entity, action) tuples to lists of cassette file paths
    """
    cassette_map: Dict[Tuple[str, str], List[Path]] = defaultdict(list)

    if not cassettes_dir.exists() or not cassettes_dir.is_dir():
        return {}

    for cassette_file in cassettes_dir.glob("*.yaml"):
        try:
            spec = load_test_spec(cassette_file, auth_config={})
            key = (spec.entity, spec.action)
            cassette_map[key].append(cassette_file)
        except Exception:
            continue

    return dict(cassette_map)


def validate_response_against_schema(response_body: Any, schema: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate a response body against a JSON schema.

    Args:
        response_body: The response body to validate (usually a dict or list)
        schema: JSON schema to validate against

    Returns:
        Tuple of (is_valid, list_of_error_messages)
    """
    if not schema:
        return True, []

    try:
        jsonschema.validate(instance=response_body, schema=schema)
        return True, []
    except jsonschema.ValidationError as e:
        errors = [f"{e.message} at path: {'.'.join(str(p) for p in e.path)}"]
        return False, errors
    except jsonschema.SchemaError as e:
        return False, [f"Invalid schema: {e.message}"]
    except Exception as e:
        return False, [f"Validation error: {str(e)}"]


def find_undeclared_fields(response_body: Any, schema: Dict[str, Any], path: str = "") -> List[str]:
    """Find fields present in response but not declared in schema.

    Args:
        response_body: The response body to check
        schema: JSON schema to check against
        path: Current path in the object (for recursive calls)

    Returns:
        List of paths to undeclared fields with array indices normalized
        (e.g., ["data.items[].extra_field"] instead of reporting for each element)
    """
    if not schema:
        return []

    undeclared_fields = []

    if isinstance(response_body, dict) and schema.get("type") == "object":
        schema_properties = schema.get("properties", {})
        additional_properties = schema.get("additionalProperties", True)

        for key, value in response_body.items():
            field_path = f"{path}.{key}" if path else key

            if key not in schema_properties:
                if additional_properties is False:
                    undeclared_fields.append(field_path)
                elif additional_properties is True or additional_properties == {}:
                    undeclared_fields.append(field_path)
                elif isinstance(additional_properties, dict):
                    nested_undeclared = find_undeclared_fields(value, additional_properties, field_path)
                    undeclared_fields.extend(nested_undeclared)
            else:
                property_schema = schema_properties[key]
                nested_undeclared = find_undeclared_fields(value, property_schema, field_path)
                undeclared_fields.extend(nested_undeclared)

    elif isinstance(response_body, list) and schema.get("type") == "array":
        items_schema = schema.get("items", {})
        if response_body:
            item_path = f"{path}[]"
            nested_undeclared = find_undeclared_fields(response_body[0], items_schema, item_path)
            undeclared_fields.extend(nested_undeclared)

    elif "anyOf" in schema or "oneOf" in schema or "allOf" in schema:
        union_key = "anyOf" if "anyOf" in schema else "oneOf" if "oneOf" in schema else "allOf"
        all_undeclared = []

        for sub_schema in schema[union_key]:
            sub_undeclared = find_undeclared_fields(response_body, sub_schema, path)
            all_undeclared.append(set(sub_undeclared))

        if all_undeclared:
            common_undeclared = set.intersection(*all_undeclared)
            undeclared_fields.extend(list(common_undeclared))

    return undeclared_fields


def _extract_field_from_jsonpath(jsonpath_expr: str) -> str | None:
    """Extract the full field path from a JSONPath expression.

    Examples:
        $.users -> "users"
        $.data -> "data"
        $.data.items -> "data.items" (returns full path)
        $.data.repository -> "data.repository" (returns full path)
        $.calls[0] -> "calls"

    Args:
        jsonpath_expr: JSONPath expression (e.g., "$.users" or "$.data.repository")

    Returns:
        Full field path or None if cannot parse
    """
    # Remove leading $. or $
    expr = jsonpath_expr.strip()
    if expr.startswith("$."):
        expr = expr[2:]
    elif expr.startswith("$"):
        expr = expr[1:]

    # Remove array indices and wildcards
    expr = expr.replace("[0]", "").replace("[]", "").replace("[*]", "")

    # Return the full path (not just the first segment)
    return expr if expr else None


def _is_dynamic_object(schema: Dict[str, Any]) -> bool:
    """Check if a schema is a dynamic object (inline object with no declared properties).

    Dynamic objects are flexible schemas that allow arbitrary keys, indicated by:
    - type: object
    - No properties defined (or empty properties)
    - This pattern is used for custom objects, arbitrary key-value stores, etc.

    Args:
        schema: Schema to check

    Returns:
        True if schema is a dynamic object (no declared properties)
    """
    if not isinstance(schema, dict):
        return False

    # Must be an object type
    if schema.get("type") != "object":
        return False

    # Check if properties are missing or empty
    properties = schema.get("properties", {})
    return not properties


def _schema_has_ref_or_dynamic(field_schema: Dict[str, Any]) -> bool:
    """Check if a schema field uses $ref or is a dynamic object.

    For array fields, checks if the array items use $ref or are dynamic objects.
    For object fields, checks if the field itself uses $ref or is a dynamic object.

    Args:
        field_schema: Schema to check

    Returns:
        True if field uses $ref, is a dynamic object, or contains items with $ref/dynamic objects
    """
    # If the field itself has a $ref, that's good
    if "$ref" in field_schema:
        return True

    # If the field is a dynamic object (no declared properties), that's also acceptable
    if _is_dynamic_object(field_schema):
        return True

    # If the field is an array, check if items have a $ref or are dynamic objects
    if field_schema.get("type") == "array" and "items" in field_schema:
        items_schema = field_schema["items"]
        return "$ref" in items_schema or _is_dynamic_object(items_schema)

    return False


def _check_field_has_ref_or_dynamic(field_path: str, schema: Dict[str, Any]) -> bool:
    """Check if a field in the schema uses $ref or is a dynamic object.

    For array fields, checks if the array items use $ref or are dynamic objects.
    For object fields, checks if the field itself uses $ref or is a dynamic object.

    Dynamic objects (inline objects with no declared properties) are allowed because
    they represent flexible schemas like custom objects or arbitrary key-value stores.

    Args:
        field_path: Field path (e.g., "users" or "data")
        schema: Response schema (unresolved, to check for $ref presence)

    Returns:
        True if field uses $ref, is a dynamic object, or contains items with $ref/dynamic objects
    """
    if not schema or not isinstance(schema, dict):
        return False

    # For simple field (e.g., "users")
    if "." not in field_path:
        if "properties" in schema:
            field_schema = schema["properties"].get(field_path, {})
            return _schema_has_ref_or_dynamic(field_schema)
        return False

    # For nested field (e.g., "data.items"), traverse
    parts = field_path.split(".")
    current = schema

    for part in parts:
        if not isinstance(current, dict):
            return False

        # Handle array types by descending into items first
        if current.get("type") == "array" and "items" in current:
            current = current["items"]
            if not isinstance(current, dict):
                return False

        if "properties" in current:
            current = current["properties"].get(part, {})
        else:
            return False

    # Check if the final field has a $ref, is a dynamic object, or is an array with items that qualify
    return _schema_has_ref_or_dynamic(current)


def _check_field_in_schema(jsonpath_expr: str, schema: Dict[str, Any]) -> bool:
    """Check if a JSONPath expression corresponds to fields in schema.

    Args:
        jsonpath_expr: JSONPath (e.g., "$.records", "$.pagination.cursor")
        schema: Response schema

    Returns:
        True if path exists in schema, False otherwise
    """
    field_path = _extract_field_from_jsonpath(jsonpath_expr)

    if not field_path or not schema:
        return False

    # Navigate schema to check field exists
    current = schema
    parts = field_path.split(".")

    for part in parts:
        if not isinstance(current, dict):
            return False

        # Check in properties
        if "properties" in current and part in current["properties"]:
            current = current["properties"][part]
            continue

        # Check in additionalProperties (for dynamic schemas)
        if "additionalProperties" in current:
            return True  # Can't validate further for dynamic schemas

        # Field not found
        return False

    return True


def validate_record_extractor_has_ref(
    endpoint: EndpointDefinition,
    raw_spec: Dict[str, Any],
    entity_name: str,
    action: str,
) -> Tuple[bool, List[str], List[str]]:
    """
    Validate that x-airbyte-record-extractor points to a field with a $ref or dynamic object.

    When an operation defines x-airbyte-record-extractor, the JSONPath should point
    to a field in the response schema that either:
    1. Uses a $ref for proper typing with named schemas, OR
    2. Is a dynamic object (type: object with no declared properties) for flexible schemas

    Dynamic objects are acceptable for cases like custom objects or arbitrary key-value
    stores where the schema is intentionally flexible.

    Args:
        endpoint: The endpoint definition with response_schema
        raw_spec: Raw OpenAPI spec dict (unresolved) to check for $refs
        entity_name: Entity name (for error messages)
        action: Action name (for error messages)

    Returns:
        Tuple of (is_valid, errors, warnings)
        - is_valid: False if extractor points to inline schema with declared properties
        - errors: List of error messages
        - warnings: List of warning messages

    Example:
        Good: x-airbyte-record-extractor: $.users
              Response schema has: users: { $ref: "#/components/schemas/User" }

        Good: x-airbyte-record-extractor: $.custom_fields
              Response schema has: custom_fields: { type: object, additionalProperties: true }
              (no properties declared = dynamic schema)

        Bad:  x-airbyte-record-extractor: $.data
              Response schema has: data: { type: object, properties: { id: {...}, name: {...} } }
              (inline schema with declared properties)
    """
    errors = []
    warnings = []

    if not endpoint.record_extractor:
        return True, errors, warnings

    if not endpoint.response_schema:
        warnings.append(f"{entity_name}.{action}: Has x-airbyte-record-extractor but no response schema defined")
        return True, errors, warnings

    # Parse JSONPath to find target field
    extractor_path = endpoint.record_extractor

    try:
        # Extract the field name from JSONPath (e.g., "$.users" -> "users")
        target_field = _extract_field_from_jsonpath(extractor_path)

        if not target_field:
            warnings.append(f"{entity_name}.{action}: Cannot parse x-airbyte-record-extractor JSONPath: {extractor_path}")
            return True, errors, warnings

        # Find the unresolved response schema in the raw spec to check for $ref
        unresolved_schema = _find_unresolved_response_schema(raw_spec, endpoint.path, endpoint.method)

        if not unresolved_schema:
            # If we can't find the unresolved schema, skip validation
            return True, errors, warnings

        # Check if the target field has a $ref or is a dynamic object in the unresolved schema
        has_ref_or_dynamic = _check_field_has_ref_or_dynamic(target_field, unresolved_schema)

        if not has_ref_or_dynamic:
            errors.append(
                f"{entity_name}.{action}: x-airbyte-record-extractor '{extractor_path}' points to field "
                f"'{target_field}' which uses an inline schema with declared properties. Records should "
                f"reference a named schema (e.g., $ref: '#/components/schemas/{target_field.title()}') for proper typing."
            )
            return False, errors, warnings

    except Exception as e:
        warnings.append(f"{entity_name}.{action}: Error validating x-airbyte-record-extractor: {str(e)}")
        return True, errors, warnings

    return True, errors, warnings


def _find_unresolved_response_schema(raw_spec: Dict[str, Any], path: str, method: str) -> Dict[str, Any] | None:
    """Find the unresolved response schema from the raw OpenAPI spec.

    If the response schema itself is a $ref, resolves it once to get the actual schema.
    This allows us to check the properties within that schema for nested $refs.

    Args:
        raw_spec: Raw OpenAPI spec dict
        path: API path (e.g., "/v1/users")
        method: HTTP method (e.g., "GET")

    Returns:
        Unresolved response schema dict or None if not found
    """
    try:
        paths = raw_spec.get("paths", {})
        if path not in paths:
            return None

        path_item = paths[path]
        operation = path_item.get(method.lower())
        if not operation:
            return None

        responses = operation.get("responses", {})
        response_200 = responses.get("200")
        if not response_200:
            return None

        content = response_200.get("content", {})
        json_content = content.get("application/json")
        if not json_content:
            return None

        schema = json_content.get("schema")

        # If the schema itself is a $ref, resolve it once to get to the actual schema
        # This is needed for cases like: schema: { $ref: "#/components/schemas/UsersResponse" }
        # We want to check the properties inside UsersResponse
        if schema and "$ref" in schema:
            ref_path = schema["$ref"]
            # Parse the reference (e.g., "#/components/schemas/UsersResponse")
            if ref_path.startswith("#/"):
                parts = ref_path[2:].split("/")
                resolved = raw_spec
                for part in parts:
                    resolved = resolved.get(part, {})
                    if not resolved:
                        return None
                return resolved

        return schema
    except Exception:
        return None


def validate_meta_extractor_fields(
    endpoint: EndpointDefinition,
    cassette_path: Path,
    entity_name: str,
    action: str,
) -> Tuple[bool, List[str], List[str]]:
    """
    Validate x-airbyte-meta-extractor fields exist in cassettes and schema.

    Checks that:
    1. Fields extracted by meta-extractor exist in actual cassette responses
    2. Those fields are declared in the response schema

    Args:
        endpoint: Endpoint definition with meta_extractor and response_schema
        cassette_path: Path to cassette file
        entity_name: Entity name (for error messages)
        action: Action name (for error messages)

    Returns:
        Tuple of (is_valid, errors, warnings)
        - is_valid: Always True (missing fields are warnings, not errors)
        - errors: Empty (meta-extractor issues are non-blocking)
        - warnings: List of warning messages
    """
    errors = []
    warnings = []

    if not endpoint.meta_extractor:
        return True, errors, warnings

    try:
        # Load cassette to get actual response
        spec = load_test_spec(cassette_path, auth_config={})
        response_body = spec.captured_response.body

        # Validate each meta extractor field
        for field_name, jsonpath_expr in endpoint.meta_extractor.items():
            # Check 1: Does the JSONPath find data in the actual response?
            try:
                parsed_expr = parse_jsonpath(jsonpath_expr)
                matches = [match.value for match in parsed_expr.find(response_body)]

                if not matches:
                    warnings.append(
                        f"{entity_name}.{action}: x-airbyte-meta-extractor field '{field_name}' "
                        f"with JSONPath '{jsonpath_expr}' found no matches in cassette response"
                    )
            except Exception as e:
                warnings.append(
                    f"{entity_name}.{action}: x-airbyte-meta-extractor field '{field_name}' has invalid JSONPath '{jsonpath_expr}': {str(e)}"
                )

            # Check 2: Is this field path declared in the response schema?
            if endpoint.response_schema:
                field_in_schema = _check_field_in_schema(jsonpath_expr, endpoint.response_schema)

                if not field_in_schema:
                    warnings.append(
                        f"{entity_name}.{action}: x-airbyte-meta-extractor field '{field_name}' "
                        f"extracts from '{jsonpath_expr}' but this path is not declared in response schema"
                    )

    except Exception as e:
        warnings.append(f"{entity_name}.{action}: Error validating x-airbyte-meta-extractor: {str(e)}")

    return True, errors, warnings


def validate_connector_readiness(connector_dir: str | Path) -> Dict[str, Any]:
    """
    Validate that a connector is ready to ship.

    Checks that:
    - connector.yaml exists and is valid
    - For each entity/action defined, corresponding cassette(s) exist
    - Response schemas in connector.yaml match cassette responses
    - Detects fields in responses that are not declared in the schema (as warnings)

    Args:
        connector_dir: Path to the connector directory (e.g., "/path/to/integrations/stripe")

    Returns:
        Dict with validation results including:
        - success: Overall success status
        - connector_name: Name of the connector
        - validation_results: List of results for each entity/action
        - summary: Summary statistics

    Each validation result includes:
        - warnings: Human-readable warnings (e.g., "Undeclared field in response: data[].extra_field")
        - errors: Actual schema validation errors (e.g., missing required fields, type mismatches)

    Note: Undeclared fields are surfaced as warnings, not errors. This allows connectors
    with dynamic/flexible schemas (like custom objects) to pass validation while still
    highlighting fields that could be added to the schema. Non-dynamic schemas are expected
    to have all fields in the schema.

    Example:
        validate_connector_readiness("/path/to/integrations/stripe")
    """
    connector_path = Path(connector_dir)

    if not connector_path.exists():
        return {
            "success": False,
            "error": f"Connector directory not found: {connector_dir}",
        }

    config_file = connector_path / "connector.yaml"
    if not config_file.exists():
        return {
            "success": False,
            "error": f"connector.yaml not found in {connector_dir}",
        }

    try:
        config = load_connector_model(config_file)
    except ConnectorModelLoaderError as e:
        return {"success": False, "error": f"Failed to load connector.yaml: {str(e)}"}

    # Load the raw spec for extractor validation
    try:
        with open(config_file) as f:
            raw_spec = yaml.safe_load(f)
    except Exception:
        raw_spec = {}

    cassettes_dir = connector_path / "tests" / "cassettes"
    cassette_map = build_cassette_map(cassettes_dir)

    validation_results = []
    total_operations = 0
    operations_with_cassettes = 0
    operations_missing_cassettes = 0
    total_cassettes = 0
    cassettes_valid = 0
    cassettes_invalid = 0
    total_warnings = 0
    total_errors = 0

    for entity in config.entities:
        for action in entity.actions:
            total_operations += 1

            key = (entity.name, action.value)
            cassette_paths = cassette_map.get(key, [])

            endpoint = entity.endpoints[action]
            # Check if this is a download action
            is_download = action == Action.DOWNLOAD
            # Check if operation is marked as untested
            is_untested = endpoint.untested

            if not cassette_paths:
                # For untested operations, add a warning instead of an error
                if is_untested:
                    total_warnings += 1
                    validation_results.append(
                        {
                            "entity": entity.name,
                            "action": action.value,
                            "cassettes_found": 0,
                            "cassette_paths": [],
                            "schema_defined": endpoint.response_schema is not None,
                            "is_download": is_download,
                            "untested": True,
                            "schema_validation": [],
                            "warnings": [
                                f"Operation {entity.name}.{action.value} is marked as untested "
                                f"(x-airbyte-untested: true) and has no cassettes. Validation skipped."
                            ],
                        }
                    )
                    continue

                # For tested operations, this is an error
                operations_missing_cassettes += 1
                validation_results.append(
                    {
                        "entity": entity.name,
                        "action": action.value,
                        "cassettes_found": 0,
                        "cassette_paths": [],
                        "schema_defined": endpoint.response_schema is not None,
                        "is_download": is_download,
                        "schema_validation": [],
                    }
                )
                continue

            operations_with_cassettes += 1
            total_cassettes += len(cassette_paths)

            response_schema = endpoint.response_schema
            schema_defined = response_schema is not None

            # Validate x-airbyte-record-extractor (once per endpoint, not per cassette)
            if endpoint.record_extractor and not is_download:
                is_valid, extractor_errors, extractor_warnings = validate_record_extractor_has_ref(
                    endpoint=endpoint,
                    raw_spec=raw_spec,
                    entity_name=entity.name,
                    action=action.value,
                )

                if not is_valid:
                    cassettes_invalid += len(cassette_paths)
                    total_errors += len(extractor_errors) * len(cassette_paths)

                total_warnings += len(extractor_warnings)

                # If record extractor validation fails, add error to all cassettes for this endpoint
                if not is_valid:
                    schema_validation = [
                        {
                            "cassette": str(p.name),
                            "valid": False,
                            "errors": extractor_errors,
                            "warnings": extractor_warnings,
                        }
                        for p in cassette_paths
                    ]
                    validation_results.append(
                        {
                            "entity": entity.name,
                            "action": action.value,
                            "cassettes_found": len(cassette_paths),
                            "cassette_paths": [str(p.name) for p in cassette_paths],
                            "schema_defined": schema_defined,
                            "is_download": is_download,
                            "schema_validation": schema_validation,
                        }
                    )
                    continue

            schema_validation = []
            for cassette_path in cassette_paths:
                try:
                    spec = load_test_spec(cassette_path, auth_config={})

                    # For download actions, validate that captured_file_request/response exist
                    if is_download:
                        has_file_request = hasattr(spec, "captured_file_request") and spec.captured_file_request is not None
                        has_file_response = hasattr(spec, "captured_file_response") and spec.captured_file_response is not None

                        if has_file_request and has_file_response:
                            cassettes_valid += 1
                            schema_validation.append(
                                {
                                    "cassette": str(cassette_path.name),
                                    "valid": True,
                                    "errors": [],
                                    "warnings": [],
                                }
                            )
                        else:
                            cassettes_invalid += 1
                            total_errors += 1
                            errors = []
                            if not has_file_request:
                                errors.append("Missing captured_file_request for download action")
                            elif not has_file_response:
                                errors.append("Missing captured_file_response for download action")
                            schema_validation.append(
                                {
                                    "cassette": str(cassette_path.name),
                                    "valid": False,
                                    "errors": errors,
                                    "warnings": [],
                                }
                            )
                        continue

                    # For non-download actions, validate response schema
                    response_body = spec.captured_response.body

                    if response_schema:
                        is_valid, errors = validate_response_against_schema(response_body, response_schema)

                        undeclared_fields = find_undeclared_fields(response_body, response_schema)

                        warnings = []
                        if undeclared_fields:
                            warnings = [f"Undeclared field in response: {field}" for field in undeclared_fields]

                        # Validate x-airbyte-meta-extractor fields
                        if endpoint.meta_extractor:
                            (
                                _,
                                meta_errors,
                                meta_warnings,
                            ) = validate_meta_extractor_fields(
                                endpoint=endpoint,
                                cassette_path=cassette_path,
                                entity_name=entity.name,
                                action=action.value,
                            )
                            warnings.extend(meta_warnings)
                            # Meta extractor errors are also treated as warnings (non-blocking)
                            warnings.extend(meta_errors)

                        if is_valid:
                            cassettes_valid += 1
                        else:
                            cassettes_invalid += 1

                        total_warnings += len(warnings)
                        total_errors += len(errors)

                        schema_validation.append(
                            {
                                "cassette": str(cassette_path.name),
                                "valid": is_valid,
                                "errors": errors,
                                "warnings": warnings,
                            }
                        )
                    else:
                        total_errors += 1
                        schema_validation.append(
                            {
                                "cassette": str(cassette_path.name),
                                "valid": None,
                                "errors": ["No response schema defined in connector.yaml"],
                                "warnings": [],
                            }
                        )

                except Exception as e:
                    cassettes_invalid += 1
                    total_errors += 1
                    schema_validation.append(
                        {
                            "cassette": str(cassette_path.name),
                            "valid": False,
                            "errors": [f"Failed to load/validate cassette: {str(e)}"],
                            "warnings": [],
                        }
                    )

            validation_results.append(
                {
                    "entity": entity.name,
                    "action": action.value,
                    "cassettes_found": len(cassette_paths),
                    "cassette_paths": [str(p.name) for p in cassette_paths],
                    "schema_defined": schema_defined,
                    "is_download": is_download,
                    "schema_validation": schema_validation,
                }
            )

    success = operations_missing_cassettes == 0 and cassettes_invalid == 0 and total_operations > 0

    return {
        "success": success,
        "connector_name": config.name,
        "connector_path": str(connector_path),
        "validation_results": validation_results,
        "summary": {
            "total_operations": total_operations,
            "operations_with_cassettes": operations_with_cassettes,
            "operations_missing_cassettes": operations_missing_cassettes,
            "total_cassettes": total_cassettes,
            "cassettes_valid": cassettes_valid,
            "cassettes_invalid": cassettes_invalid,
            "total_warnings": total_warnings,
            "total_errors": total_errors,
        },
    }
