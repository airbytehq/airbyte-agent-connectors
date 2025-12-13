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

from .config_loader import ConfigLoaderError, load_connector_config
from .testing.spec_loader import load_test_spec
from .types import Action


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


def validate_response_against_schema(
    response_body: Any, schema: Dict[str, Any]
) -> Tuple[bool, List[str]]:
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


def find_undeclared_fields(
    response_body: Any, schema: Dict[str, Any], path: str = ""
) -> List[str]:
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
                    nested_undeclared = find_undeclared_fields(
                        value, additional_properties, field_path
                    )
                    undeclared_fields.extend(nested_undeclared)
            else:
                property_schema = schema_properties[key]
                nested_undeclared = find_undeclared_fields(
                    value, property_schema, field_path
                )
                undeclared_fields.extend(nested_undeclared)

    elif isinstance(response_body, list) and schema.get("type") == "array":
        items_schema = schema.get("items", {})
        if response_body:
            item_path = f"{path}[]"
            nested_undeclared = find_undeclared_fields(
                response_body[0], items_schema, item_path
            )
            undeclared_fields.extend(nested_undeclared)

    elif "anyOf" in schema or "oneOf" in schema or "allOf" in schema:
        union_key = (
            "anyOf" if "anyOf" in schema else "oneOf" if "oneOf" in schema else "allOf"
        )
        all_undeclared = []

        for sub_schema in schema[union_key]:
            sub_undeclared = find_undeclared_fields(response_body, sub_schema, path)
            all_undeclared.append(set(sub_undeclared))

        if all_undeclared:
            common_undeclared = set.intersection(*all_undeclared)
            undeclared_fields.extend(list(common_undeclared))

    return undeclared_fields


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
        config = load_connector_config(config_file)
    except ConfigLoaderError as e:
        return {"success": False, "error": f"Failed to load connector.yaml: {str(e)}"}

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
                                f"Operation {entity.name}.{action.value} is marked as untested (x-airbyte-untested: true) and has no cassettes. Validation skipped."
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

            schema_validation = []
            for cassette_path in cassette_paths:
                try:
                    spec = load_test_spec(cassette_path, auth_config={})

                    # For download actions, validate that captured_file_request/response exist
                    if is_download:
                        has_file_request = (
                            hasattr(spec, "captured_file_request")
                            and spec.captured_file_request is not None
                        )
                        has_file_response = (
                            hasattr(spec, "captured_file_response")
                            and spec.captured_file_response is not None
                        )

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
                                errors.append(
                                    "Missing captured_file_request for download action"
                                )
                            elif not has_file_response:
                                errors.append(
                                    "Missing captured_file_response for download action"
                                )
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
                        is_valid, errors = validate_response_against_schema(
                            response_body, response_schema
                        )

                        undeclared_fields = find_undeclared_fields(
                            response_body, response_schema
                        )

                        warnings = []
                        if undeclared_fields:
                            warnings = [
                                f"Undeclared field in response: {field}"
                                for field in undeclared_fields
                            ]

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
                                "errors": [
                                    "No response schema defined in connector.yaml"
                                ],
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

    success = (
        operations_missing_cassettes == 0
        and cassettes_invalid == 0
        and total_operations > 0
    )

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
