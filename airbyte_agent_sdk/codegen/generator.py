"""
Code generator for typed connectors from OpenAPI 3.0 specifications.

Generates complete Python packages with type-safe connectors from OpenAPI specs.
"""

import json
import keyword
import re
import shutil
import tempfile
from collections import OrderedDict
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, PackageLoader, select_autoescape
from jsonpath_ng import parse as parse_jsonpath
from pydantic import BaseModel

from ..connector_model_loader import (
    _parse_auth_from_openapi,
    convert_openapi_to_connector_model,
)
from ..constants import SDK_VERSION
from ..introspection import get_cached_search_questions
from ..schema.connector import OpenAPIConnector
from ..types import Action, AuthType
from .filters import mdx_escape, to_pascal_case, to_snake_case
from .serializer import PythonCodeSerializer

LIST_ACTIONS = frozenset({Action.LIST, Action.API_SEARCH})

# Dynamically extract reserved names from Pydantic BaseModel
# These are attributes/methods that would cause field name shadowing if used
PYDANTIC_RESERVED_NAMES = frozenset(
    {
        name
        for name in dir(BaseModel)
        if not name.startswith("_")  # Exclude private/magic methods
    }
)

# Python reserved keywords that need to be escaped when used as identifiers
PYTHON_KEYWORDS = frozenset(keyword.kwlist)

# Python builtin type names that would shadow type annotations in Pydantic models
PYTHON_BUILTIN_TYPE_NAMES = frozenset(
    {"str", "int", "float", "bool", "None", "list", "dict", "set", "tuple", "type", "object"}
)

# Type names from the typing module used in generated code that are not custom types
TYPING_TYPE_NAMES = frozenset({"Any", "Optional", "AsyncIterator", "NotRequired", "TypedDict"})


class ConnectorGenerator:
    """Generates typed connector packages from OpenAPI specifications."""

    # JSON Schema primitive types (used for validation and type checking)
    JSON_SCHEMA_TYPES = frozenset({"null", "string", "integer", "number", "boolean", "array", "object"})

    # JSON Schema primitives (non-null, non-array, non-object)
    JSON_SCHEMA_PRIMITIVES = frozenset({"string", "integer", "number", "boolean"})

    # Mapping from JSON Schema types to Python types
    JSON_TO_PYTHON_TYPE_MAP = {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "null": "None",
    }

    def __init__(self, spec_path: Path):
        """
        Initialize generator with an OpenAPI spec.

        Args:
            spec_path: Path to OpenAPI 3.0 YAML specification
        """
        self.spec_path = Path(spec_path)
        self.spec = OpenAPIConnector.model_validate(self._load_spec())
        self.env = Environment(
            loader=PackageLoader("airbyte_agent_sdk.codegen", "templates"),
            autoescape=select_autoescape(),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.env.filters["snake_case"] = to_snake_case
        self.env.filters["pascal_case"] = to_pascal_case
        self.env.filters["mdx_escape"] = mdx_escape

        # Initialize nested schemas dict for tracking generated nested TypedDicts
        self._nested_schemas = {}  # TypedDict nested schemas for types.py (parameters)
        self._pydantic_nested_schemas = {}  # Pydantic nested models for models.py (responses)

    def _load_spec(self) -> dict[str, Any]:
        """Load and parse OpenAPI specification."""
        with open(self.spec_path) as f:
            return yaml.safe_load(f)

    def generate(self, output_dir: Path, commit_sha: str | None = None) -> None:
        """
        Generate complete typed connector package.

        Args:
            output_dir: Parent directory where package directory will be created
            commit_sha: Git commit SHA of the connector-sdk used for generation

        Creates airbyte_agent_{name}/ directory containing:
            - __init__.py
            - connector.py with typed methods
            - types.py with TypedDict definitions
            - connector.yaml (copy of spec)
            - pyproject.toml
            - README.md
            - tests/ directory with basic tests
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Extract metadata
        connector_name = self.spec.info.x_airbyte_connector_name

        if not connector_name:
            raise ValueError("Connector name is required")

        connector_version = self.spec.info.version
        package_name = f"airbyte_agent_{to_snake_case(connector_name)}"

        # Create package directory
        package_dir = output_dir / package_name
        package_dir.mkdir(exist_ok=True)

        # Extract operations once (used by multiple generators)
        operations = self._extract_operations()

        # Extract auth config once (used by multiple generators)
        auth_config = self._extract_auth_config()

        # Extract search schemas once (used by multiple generators)
        entities_in_operations = {op["entity"] for op in operations}
        search_schemas = self._extract_search_schemas(entities_in_operations)

        # Generate all files
        self._generate_init(package_dir, connector_name, operations, search_schemas)
        self._generate_connector_class(package_dir, connector_name, connector_version, operations, search_schemas)
        self._generate_type_stubs(package_dir, connector_name, operations, search_schemas)
        self._generate_models(package_dir, connector_name, operations, search_schemas)
        self._generate_model(package_dir, connector_name)
        self._generate_pyproject_toml(output_dir, connector_name, connector_version, package_name)
        self._generate_readme(
            output_dir,
            connector_name,
            connector_version,
            operations,
            auth_config,
            commit_sha,
        )
        # Generate envelope types for docs generation
        envelope_types = self._generate_envelope_types(operations)
        self._generate_docs(
            output_dir,
            connector_name,
            connector_version,
            operations,
            envelope_types,
        )
        self._generate_auth_docs(
            output_dir,
            connector_name,
            auth_config,
        )
        self._generate_tests(output_dir, connector_name, package_name)

        print(f"✓ Generated typed connector package at {output_dir}")

    def generate_sdk(self, sdk_package_dir: Path) -> None:
        """Generate a connector module into the SDK package.

        Produces a submodule directory with connector.py, types.py, models.py,
        connector_model.py, and __init__.py that use absolute imports to the SDK
        package. The output is a module within the SDK, not a standalone package.

        Args:
            sdk_package_dir: The root of the SDK package's source, e.g.
                connector-sdk/airbyte_agent_sdk/
        """
        connector_name = self.spec.info.x_airbyte_connector_name
        if not connector_name:
            raise ValueError("Connector name is required")

        connector_version = self.spec.info.version
        standalone_package_name = f"airbyte_agent_{to_snake_case(connector_name)}"

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            package_dir = tmp_path / standalone_package_name
            package_dir.mkdir()

            operations = self._extract_operations()
            entities_in_operations = {op["entity"] for op in operations}
            search_schemas = self._extract_search_schemas(entities_in_operations)

            self._generate_init(package_dir, connector_name, operations, search_schemas)
            self._generate_connector_class(package_dir, connector_name, connector_version, operations, search_schemas)
            self._generate_type_stubs(package_dir, connector_name, operations, search_schemas)
            self._generate_models(package_dir, connector_name, operations, search_schemas)
            self._generate_model(package_dir, connector_name)

            module_name = to_snake_case(connector_name)
            unified_package_name = f"airbyte_agent_sdk.connectors.{module_name}"
            connectors_dir = sdk_package_dir / "connectors"
            connectors_dir.mkdir(parents=True, exist_ok=True)
            (connectors_dir / "__init__.py").write_text("")
            target_dir = connectors_dir / module_name
            if target_dir.exists():
                shutil.rmtree(target_dir)
            target_dir.mkdir(parents=True)

            # Copy connector source files
            for py_file in package_dir.glob("*.py"):
                shutil.copy2(py_file, target_dir / py_file.name)

            # Generate tests into a parallel tests/connectors/ directory
            tests_base = sdk_package_dir.parent / "tests" / "connectors"
            tests_dir = tests_base / module_name
            tests_dir.mkdir(parents=True, exist_ok=True)

            class_name = self._get_class_name(connector_name)
            auth_config = self._extract_auth_config()
            model_constant_name = f"{to_pascal_case(connector_name)}ConnectorModel"

            # test_connector.py — basic creation/metadata tests
            template = self.env.get_template("test_connector.py.jinja2")
            test_content = template.render(
                connector_name=connector_name,
                package_name=unified_package_name,
                class_name=class_name,
                auth_config=auth_config,
                model_constant_name=model_constant_name,
            )
            (tests_dir / f"test_{module_name}_connector.py").write_text(test_content)
            (tests_dir / "__init__.py").write_text("")

            # test_cassettes.py — cassette-based execution tests
            cassettes_dir = self.spec_path.parent / "tests" / "cassettes"
            if cassettes_dir.exists():
                cassette_files = sorted(cassettes_dir.glob("*.yaml"))
                cassette_tests = []
                for cf in cassette_files:
                    ctx = self._prepare_cassette_test_context(cf)
                    if ctx:
                        cassette_tests.append(ctx)
                if cassette_tests:
                    template = self.env.get_template("test_cassettes.py.jinja2")
                    test_content = template.render(
                        connector_name=connector_name,
                        package_name=unified_package_name,
                        class_name=class_name,
                        cassette_tests=cassette_tests,
                        auth_config=auth_config,
                        http_client_patch_path="airbyte_agent_sdk.http_client.HTTPClient.request",
                    )
                    (tests_dir / f"test_{module_name}_cassettes.py").write_text(test_content)

            (tests_base / "__init__.py").write_text("")

        print(f"✓ Generated unified module: {module_name}")

    def _generate_init(self, package_dir: Path, connector_name: str, operations: list, search_schemas: dict[str, dict]):
        """Generate __init__.py that exports the connector class and essential types.

        Only exports user-facing types: auth config, replication config, oauth credentials,
        and search result types. All other types remain importable from .models and .types.
        """
        class_name = self._get_class_name(connector_name)
        auth_config = self._extract_auth_config()
        replication_config = self._extract_replication_config()

        has_search_entities = bool(search_schemas)

        essential_types = []
        if auth_config:
            essential_types.append(auth_config["type_name"])
        if replication_config:
            essential_types.append(replication_config["type_name"])
        oauth_credentials = self._extract_oauth_credentials()
        if oauth_credentials:
            essential_types.append(oauth_credentials["type_name"])

        if has_search_entities:
            essential_types.extend(["AirbyteSearchMeta", "AirbyteSearchResult"])
            for schema in search_schemas.values():
                essential_types.append(schema["data_type_name"])
                essential_types.append(schema["result_type_name"])

        template = self.env.get_template("__init__.py.jinja2")
        content = template.render(
            connector_name=connector_name,
            class_name=class_name,
            essential_types=essential_types,
        )

        (package_dir / "__init__.py").write_text(content)

    def _generate_connector_class(
        self,
        package_dir: Path,
        connector_name: str,
        connector_version: str,
        operations: list,
        search_schemas: dict[str, dict],
    ):
        """Generate connector.py from template."""

        auth_config = self._extract_auth_config()
        replication_config = self._extract_replication_config()

        # Build parameter name mapping for snake_case -> API name conversion
        # This allows TypedDicts with snake_case keys to work correctly with execute()
        param_map = self._build_param_map(operations)

        search_entities = list(search_schemas.keys())

        template = self.env.get_template("connector.py.jinja2")

        # Create connector-specific constant name (e.g., GreenhouseConnectorModel)
        model_constant_name = f"{to_pascal_case(connector_name)}ConnectorModel"

        oauth_credentials = self._extract_oauth_credentials()

        code = template.render(
            connector_name=connector_name,
            connector_version=connector_version,
            sdk_version=SDK_VERSION,
            class_name=self._get_class_name(connector_name),
            envelope_prefix=self._get_envelope_prefix(connector_name),
            operations=operations,
            type_names=self._get_referenced_type_names(operations),
            response_type_names=self._get_referenced_response_types(operations),
            server_variables=self._extract_server_variables(),
            auth_config=auth_config,
            replication_config=replication_config,
            oauth_credentials=oauth_credentials,
            model_constant_name=model_constant_name,
            param_map=param_map,
            search_entities=search_entities,
            search_schemas=search_schemas,
            has_search_entities=bool(search_schemas),
            supports_oauth=self._supports_oauth(),
        )

        (package_dir / "connector.py").write_text(code)

    def _generate_type_stubs(self, package_dir: Path, connector_name: str, operations: list, search_schemas: dict[str, dict]):
        """Generate types.py from OpenAPI schemas."""
        # Only extract nested parameter schemas (not component schemas)
        # Nested schemas are discovered during parameter extraction
        nested_param_schemas = self._nested_schemas if hasattr(self, "_nested_schemas") else {}
        auth_config = self._extract_auth_config()

        # Generate envelope types for operations with both extractors
        envelope_types = self._generate_envelope_types(operations)

        # Find response types referenced by parameter schemas (for TYPE_CHECKING import)
        response_type_names_for_params = self._get_response_types_used_in_params(nested_param_schemas)

        has_search_entities = bool(search_schemas)

        template = self.env.get_template("types.py.jinja2")

        code = template.render(
            connector_name=connector_name,
            schemas=nested_param_schemas,
            operations=operations,
            auth_config=auth_config,
            envelope_types=envelope_types,
            response_type_names_for_params=response_type_names_for_params,
            search_schemas=search_schemas,
            has_search_entities=has_search_entities,
        )

        (package_dir / "types.py").write_text(code)

    def _generate_models(self, package_dir: Path, connector_name: str, operations: list, search_schemas: dict[str, dict]):
        """Generate models.py with Pydantic models for auth config and response envelopes."""
        auth_config = self._extract_auth_config()
        replication_config = self._extract_replication_config()
        # Extract only component schemas (response types), not nested parameter schemas
        component_schemas = self._extract_component_schemas_only()
        envelope_types = self._generate_envelope_types(operations)

        has_search_entities = bool(search_schemas)

        template = self.env.get_template("models.py.jinja2")

        oauth_credentials = self._extract_oauth_credentials()

        code = template.render(
            connector_name=connector_name,
            envelope_prefix=self._get_envelope_prefix(connector_name),
            auth_config=auth_config,
            replication_config=replication_config,
            oauth_credentials=oauth_credentials,
            operations=operations,
            schemas=component_schemas,
            envelope_types=envelope_types,
            search_schemas=search_schemas,
            has_search_entities=has_search_entities,
        )

        (package_dir / "models.py").write_text(code)

    def _generate_model(self, package_dir: Path, connector_name: str) -> None:
        """Generate connector_model.py with embedded ConnectorModel.

        Args:
            package_dir: Package directory where connector_model.py will be created
            connector_name: Name of the connector (for documentation)
        """
        # Convert OpenAPI spec to ConnectorModel
        model = convert_openapi_to_connector_model(self.spec)

        # Serialize to Python code
        serializer = PythonCodeSerializer()
        model_code, imports_by_module = serializer.serialize_connector_model(model)

        # Create connector-specific constant name (e.g., GreenhouseConnectorModel)
        model_constant_name = f"{to_pascal_case(connector_name)}ConnectorModel"

        # Generate connector_model.py from template
        template = self.env.get_template("connector_model.py.jinja2")
        code = template.render(
            connector_name=connector_name,
            model_constant_name=model_constant_name,
            model_python_code=model_code,
            imports_by_module=imports_by_module,
        )

        (package_dir / "connector_model.py").write_text(code)

    def _generate_pyproject_toml(
        self,
        output_dir: Path,
        connector_name: str,
        connector_version: str,
        package_name: str,
    ):
        """Generate pyproject.toml with package metadata."""
        template = self.env.get_template("pyproject.toml.jinja2")
        content = template.render(
            connector_name=connector_name,
            connector_version=connector_version,
            package_name=package_name,
        )

        (output_dir / "pyproject.toml").write_text(content)

    def _generate_readme(
        self,
        output_dir: Path,
        connector_name: str,
        connector_version: str,
        operations: list,
        auth_config: dict[str, Any] | None = None,
        commit_sha: str | None = None,
    ):
        """Generate README.md with usage documentation using Jinja template.

        Also writes README.context.json with the template context for use by
        update-readme.py when updating versions later.
        """
        class_name = self._get_class_name(connector_name)
        module_name = to_snake_case(connector_name)
        package_name = f"airbyte_agent_sdk.connectors.{module_name}"
        install_package = "airbyte-agent-sdk"

        # Use _extract_auth_config() if no auth_config provided
        if auth_config is None:
            auth_config = self._extract_auth_config()

        # Build auth config example using pydantic model
        if auth_config and auth_config.get("options"):
            auth_type_name = auth_config["type_name"]
            fields = auth_config["options"][0].get("fields", [])
            field_args = ", ".join(f'{f["name"]}="..."' for f in fields)
            auth_example = f"{auth_type_name}({field_args})"
            auth_import = f", {auth_type_name}"
        else:
            auth_example = '{"api_key": "your_api_key"}'
            auth_import = ""

        # Extract custom description from OpenAPI spec info.description
        custom_description = self.spec.info.description

        # Extract example questions directly from spec extension
        example_questions = self.spec.info.x_airbyte_example_questions
        supported_questions = None
        unsupported_questions = None
        if example_questions:
            direct_questions = getattr(example_questions, "direct", None)
            search_questions = get_cached_search_questions(example_questions)

            direct_questions = direct_questions if isinstance(direct_questions, list) else []

            combined_supported: list[str] = [*direct_questions, *search_questions]
            if combined_supported:
                supported_questions = "\n".join(f"- {q}" for q in combined_supported)
            if example_questions.unsupported:
                unsupported_questions = "\n".join(f"- {q}" for q in example_questions.unsupported)

        # Extract first api_reference URL from external documentation URLs
        api_reference_url = None
        external_docs = self.spec.info.x_airbyte_external_documentation_urls
        if external_docs:
            for doc in external_docs:
                if doc.type == "api_reference":
                    api_reference_url = doc.url
                    break

        # Get first operation for sample usage in README
        first_operation = operations[0] if operations else None

        # Group operations by entity for supported entities/actions table
        entities_grouped: dict[str, list[dict[str, Any]]] = {}
        for op in operations:
            entity = op.get("entity")
            if not entity:
                continue
            entities_grouped.setdefault(entity, []).append(op)

        # Extract replication config for MULTI mode connectors
        replication_config = self._extract_replication_config()

        # Extract search schemas for entities with x-airbyte-context-store config
        entities_in_operations = set(entities_grouped.keys())
        search_schemas = self._extract_search_schemas(entities_in_operations)

        # Build template context
        context = {
            "connector_name": connector_name,
            "class_name": class_name,
            "package_name": package_name,
            "install_package": install_package,
            "package_version": connector_version,
            "yaml_version": connector_version,
            "api_reference_url": api_reference_url,
            "commit_sha": commit_sha or "unknown",
            "auth_example": auth_example,
            "auth_import": auth_import,
            "auth_config": auth_config,
            "replication_config": replication_config,
            "custom_description": custom_description,
            "supported_questions": supported_questions,
            "unsupported_questions": unsupported_questions,
            "first_operation": first_operation,
            "entities_grouped": entities_grouped,
            "search_schemas": search_schemas,
        }

        # Render README from Jinja template
        template = self.env.get_template("README.md.jinja2")
        content = template.render(**context)
        (output_dir / "README.md").write_text(content)

        # Write context JSON for use by update-readme.py
        (output_dir / "README.context.json").write_text(json.dumps(context, indent=2))

    def _generate_docs(
        self,
        output_dir: Path,
        connector_name: str,
        connector_version: str,
        operations: list,
        envelope_types: list[dict] | None = None,
    ):
        """Generate comprehensive REFERENCE.md with detailed API documentation.

        Args:
            output_dir: Directory to write REFERENCE.md to
            connector_name: Name of connector (e.g., "stripe")
            connector_version: Version string
            operations: List of operation metadata dicts
            envelope_types: List of envelope type definitions (for extractors)
        """
        class_name = self._get_class_name(connector_name)
        connector_instance_name = to_snake_case(connector_name)
        connector_definition_id = self.spec.info.x_airbyte_connector_definition_id or "CONNECTOR_ID"

        # Store envelope types for response schema flattening
        self._envelope_types = {env["name"]: env for env in (envelope_types or [])}

        # Group operations by entity
        entities_grouped = {}
        for op in operations:
            entity = op["entity"]
            if entity not in entities_grouped:
                entities_grouped[entity] = []

            # Process parameters
            params = op.get("parameters", [])

            # Enhance parameters with example values
            enhanced_params = []
            for param in params:
                enhanced_param = param.copy()
                enhanced_param["example_value"] = self._get_example_value_for_param(param, base_indent=4)
                enhanced_param["example_value_json"] = self._get_example_value_for_param(param, base_indent=8)
                enhanced_params.append(enhanced_param)

            # Flatten parameters for documentation table (with dot notation)
            flattened_params = self._flatten_nested_parameters(params)

            # Separate required parameters for SDK/API examples
            required_params = [p for p in enhanced_params if p.get("required", False)]

            # Flatten response schema for documentation table
            response_type = op.get("response_type", "")
            flattened_response = self._flatten_response_schema(response_type)

            # Extract and flatten meta fields if this operation has an envelope
            flattened_meta = []
            if hasattr(self, "_envelope_types") and response_type in self._envelope_types:
                envelope = self._envelope_types[response_type]
                meta_fields = envelope.get("meta_fields")
                if meta_fields:
                    # meta_fields is a list of field dicts with name, type, schema, description
                    for field in meta_fields:
                        field_type = field.get("type", "any")
                        field_name = field["name"]
                        field_schema = field.get("schema")

                        # Get JSON type from schema
                        try:
                            json_type = self._openapi_schema_to_json_type(field_schema)
                        except ValueError as e:
                            # Add context about which operation/field failed
                            raise ValueError(
                                f"Failed to generate JSON type for meta field '{field_name}' "
                                f"in operation '{op.get('entity')}.{op.get('action')}' "
                                f"(response type: {response_type}). "
                                f"Original error: {e}"
                            ) from e

                        # Add the parent field
                        flattened_meta.append(
                            {
                                "name": field_name,
                                "type": json_type,
                                "description": field.get("description", ""),
                            }
                        )

                        # Check if this is a schema reference that should be flattened
                        # Schema references are typically PascalCase names
                        if field_type and field_type[0].isupper() and "[" not in field_type:
                            # This is likely a schema reference - flatten it
                            nested_fields = self._flatten_response_schema(field_type, f"{field_name}.")
                            flattened_meta.extend(nested_fields)

            op_copy = op.copy()
            op_copy["parameters"] = enhanced_params  # For SDK/API examples
            op_copy["flattened_parameters"] = flattened_params  # For params table
            op_copy["required_parameters"] = required_params  # For showing in examples
            op_copy["flattened_response"] = flattened_response  # For records table
            op_copy["flattened_meta"] = flattened_meta  # For meta table
            entities_grouped[entity].append(op_copy)

        # Extract server variables for configuration section
        server_variables = self._extract_server_variables()

        # Extract search schemas for entities with x-airbyte-context-store config
        entities_in_operations = set(entities_grouped.keys())
        search_schemas = self._extract_search_schemas(entities_in_operations)

        # Render template
        template = self.env.get_template("REFERENCE.md.jinja2")
        content = template.render(
            connector_name=connector_name,
            connector_version=connector_version,
            connector_definition_id=connector_definition_id,
            class_name=class_name,
            connector_instance_name=connector_instance_name,
            operations=operations,
            entities_grouped=entities_grouped,
            server_variables=server_variables,
            search_schemas=search_schemas,
            spec_info=self.spec.info,
        )

        (output_dir / "REFERENCE.md").write_text(content)

    def _generate_auth_docs(
        self,
        output_dir: Path,
        connector_name: str,
        auth_config: dict[str, Any] | None = None,
    ):
        """Generate AUTH.md with authentication and configuration documentation.

        Args:
            output_dir: Directory to write AUTH.md to
            connector_name: Name of connector (e.g., "stripe")
            auth_config: Optional auth configuration metadata
        """
        class_name = self._get_class_name(connector_name)
        module_name = to_snake_case(connector_name)
        package_name = f"airbyte_agent_sdk.connectors.{module_name}"

        # Extract server variables for configuration section
        server_variables = self._extract_server_variables()

        # Extract replication config for connectors that support it
        replication_config = self._extract_replication_config()

        # Extract OAuth credentials for credential override section
        oauth_credentials = self._extract_oauth_credentials()

        # Render template
        template = self.env.get_template("AUTH.md.jinja2")
        content = template.render(
            connector_name=connector_name,
            class_name=class_name,
            package_name=package_name,
            auth_config=auth_config,
            server_variables=server_variables,
            replication_config=replication_config,
            oauth_credentials=oauth_credentials,
        )

        (output_dir / "AUTH.md").write_text(content)

    def _generate_tests(self, output_dir: Path, connector_name: str, package_name: str):
        """Generate basic test structure."""
        tests_dir = output_dir / "tests"
        tests_dir.mkdir(exist_ok=True)

        class_name = self._get_class_name(connector_name)

        # Extract auth config to generate tests for each auth option
        auth_config = self._extract_auth_config()

        # Create connector-specific constant name (e.g., GreenhouseConnectorModel)
        model_constant_name = f"{to_pascal_case(connector_name)}ConnectorModel"

        # Render test_connector.py from template
        template = self.env.get_template("test_connector.py.jinja2")
        test_content = template.render(
            connector_name=connector_name,
            package_name=package_name,
            class_name=class_name,
            auth_config=auth_config,
            model_constant_name=model_constant_name,
        )

        (tests_dir / f"test_{connector_name}_connector.py").write_text(test_content)
        (tests_dir / "__init__.py").write_text('"""Tests for typed connector."""\n')

        # Generate cassette-based tests if cassettes exist
        self._generate_cassette_tests(tests_dir, connector_name, package_name, class_name)

    def _extract_path_param_values(self, template_path: str, actual_path: str) -> dict[str, str]:
        """Extract path parameter values by matching actual path against template.

        Args:
            template_path: Path template with {param} placeholders (e.g., '/v1/customers/{id}')
            actual_path: Actual URL path (e.g., '/v1/customers/cus_TLTWhRfiG8of9k')

        Returns:
            Dict of parameter names to values (e.g., {'id': 'cus_TLTWhRfiG8of9k'})
        """
        # Convert template to regex with named capture groups
        # Replace {param_name} with (?P<param_name>[^/]+)
        pattern = template_path
        param_names = re.findall(r"\{(\w+)\}", template_path)

        for param_name in param_names:
            pattern = pattern.replace(f"{{{param_name}}}", f"(?P<{param_name}>[^/]+)")

        # Match against actual path
        match = re.match(f"^{pattern}$", actual_path)
        if match:
            return match.groupdict()

        return {}

    def _find_endpoint_template(self, entity: str, action: str) -> str | None:
        """Find the path template for an entity/action from the spec.

        Args:
            entity: Entity name (e.g., 'customers')
            action: Action name (e.g., 'retrieve')

        Returns:
            Path template string (e.g., '/v1/customers/{id}') or None if not found
        """
        for path, path_item in self.spec.paths.items():
            for method in ["get", "post", "put", "patch", "delete"]:
                operation = getattr(path_item, method, None)
                if not operation:
                    continue
                if operation.x_airbyte_entity == entity and operation.x_airbyte_action == action:
                    return path
        return None

    def _find_operation(self, entity: str, action: str) -> Any | None:
        """Find the operation object for an entity/action from the spec.

        Args:
            entity: Entity name (e.g., 'customers')
            action: Action name (e.g., 'retrieve')

        Returns:
            Operation object or None if not found
        """
        for path, path_item in self.spec.paths.items():
            for method in ["get", "post", "put", "patch", "delete"]:
                operation = getattr(path_item, method, None)
                if not operation:
                    continue
                if operation.x_airbyte_entity == entity and operation.x_airbyte_action == action:
                    return operation
        return None

    def _generate_cassette_tests(self, tests_dir: Path, connector_name: str, package_name: str, class_name: str):
        """Generate tests from cassette YAML files.

        Discovers cassettes from the source connector's tests/cassettes/ directory
        and generates test functions that use mocked HTTP responses.
        """
        # Find cassettes directory relative to spec_path
        # spec_path is like: integrations/stripe/connector.yaml
        # cassettes are at: integrations/stripe/tests/cassettes/
        cassettes_dir = self.spec_path.parent / "tests" / "cassettes"

        if not cassettes_dir.exists():
            return  # No cassettes to generate tests from

        cassette_files = list(cassettes_dir.glob("*.yaml"))
        if not cassette_files:
            return  # No cassette files found

        # Build test context for each cassette
        cassette_tests = []
        for cassette_file in sorted(cassette_files):
            test_context = self._prepare_cassette_test_context(cassette_file)
            if test_context:
                cassette_tests.append(test_context)

        if not cassette_tests:
            return  # No valid cassettes

        # Extract auth config for test generation
        auth_config = self._extract_auth_config()

        # Render test file from template
        template = self.env.get_template("test_cassettes.py.jinja2")
        http_client_patch_path = "airbyte_agent_sdk.http_client.HTTPClient.request"
        test_content = template.render(
            connector_name=connector_name,
            package_name=package_name,
            class_name=class_name,
            cassette_tests=cassette_tests,
            auth_config=auth_config,
            http_client_patch_path=http_client_patch_path,
        )

        cassette_test_file = tests_dir / f"test_{connector_name.replace('-', '_')}_cassettes.py"
        cassette_test_file.write_text(test_content)

    def _strip_nulls_from_dict(self, obj: Any) -> Any:
        """Recursively strip null values from dicts/lists to match Pydantic's missing field behavior.

        Args:
            obj: Object to strip nulls from (dict, list, or other)

        Returns:
            Object with nulls stripped
        """
        if isinstance(obj, dict):
            return {k: self._strip_nulls_from_dict(v) for k, v in obj.items() if v is not None}
        elif isinstance(obj, list):
            return [self._strip_nulls_from_dict(item) for item in obj]
        return obj

    def _prepare_cassette_test_context(self, cassette_file: Path) -> dict[str, Any] | None:
        """Prepare context dict for rendering a cassette test from template.

        Args:
            cassette_file: Path to cassette YAML file

        Returns:
            Dict with test context, or None if invalid cassette
        """
        try:
            with open(cassette_file) as f:
                cassette = yaml.safe_load(f)
        except Exception:
            return None  # Skip invalid cassettes

        # Extract cassette data
        entity = cassette.get("entity")
        action = cassette.get("action")
        test_name = cassette.get("test_name", cassette_file.stem)
        # Sanitize test_name to be a valid Python identifier
        test_name = re.sub(r"[^\w]", "_", test_name)
        description = cassette.get("description", f"Test {entity}/{action}")
        inputs = cassette.get("inputs", {})
        params = inputs.get("params", {}).copy()  # Make a copy to modify
        captured_request = cassette.get("captured_request", {})
        captured_response = cassette.get("captured_response", {})
        response_body = captured_response.get("body", {})

        # Strip nulls from response body to match Pydantic's behavior
        response_body = self._strip_nulls_from_dict(response_body)

        if not entity or not action:
            return None  # Invalid cassette

        # Extract path parameters from captured request path if available
        actual_path = captured_request.get("path", "")
        if actual_path:
            template_path = self._find_endpoint_template(entity, action)
            if template_path:
                path_params = self._extract_path_param_values(template_path, actual_path)
                # Merge path params with existing params (path params take precedence for empty params)
                for key, value in path_params.items():
                    if key not in params or not params[key]:
                        params[key] = value

        # Get secret keys from cassette's auth_config (exclude server variables)
        auth_config = cassette.get("auth_config", {})
        server_variable_names = {var["name"] for var in self._extract_server_variables()}
        auth_secrets = {key: value for key, value in auth_config.items() if key not in server_variable_names}
        server_variables = {key: value for key, value in auth_config.items() if key in server_variable_names}
        secret_keys = list(auth_secrets.keys()) if auth_secrets else ["api_key"]
        secrets_dict = ", ".join(f'"{k}": "test_key"' for k in secret_keys)
        server_vars_kwargs = ", ".join(f'{key}="test_key"' for key in server_variables.keys())

        # For multi-auth connectors, determine which specific auth config class to use
        auth_config_class_name = None
        auth_config_metadata = self._extract_auth_config()
        if auth_config_metadata and auth_config_metadata.get("options"):
            options = auth_config_metadata["options"]
            if len(options) > 1:
                # Multi-auth: match cassette's secret keys to an auth option
                secret_keys_set = set(secret_keys)
                for option in options:
                    option_fields_set = set(f["name"] for f in option["fields"])
                    # Check if the cassette's secret keys match this option's fields
                    if secret_keys_set.issubset(option_fields_set):
                        auth_config_class_name = f"{auth_config_metadata['base_name']}{option['type_suffix']}AuthConfig"
                        break

                # If no match found, use the first option as fallback
                if not auth_config_class_name:
                    auth_config_class_name = f"{auth_config_metadata['base_name']}{options[0]['type_suffix']}AuthConfig"

        # Convert params to kwargs string (sanitize param names for Python)
        # Use repr() for all values to properly escape quotes and special characters
        kwargs_parts = []
        for key, value in params.items():
            python_key = self._sanitize_param_name(key)
            kwargs_parts.append(f"{python_key}={repr(value)}")
        kwargs_str = ", ".join(kwargs_parts)

        # Format response body as Python dict literal
        response_repr = repr(response_body)

        # Check if this is a download operation
        is_download = action == "download" or cassette.get("captured_file_request") is not None

        if is_download:
            # Prepare download-specific test context
            captured_file_response = cassette.get("captured_file_response", {})
            file_body = captured_file_response.get("body", {})

            # Extract base64 data if present
            if isinstance(file_body, dict) and file_body.get("_binary"):
                expected_base64 = file_body.get("_base64", "")
                return {
                    "test_name": test_name,
                    "description": description,
                    "entity": entity,
                    "action": action,
                    "kwargs_str": kwargs_str,
                    "response_repr": response_repr,
                    "secrets_dict": secrets_dict,
                    "is_download": True,
                    "expected_base64": expected_base64,
                    "record_extractor": None,
                    "meta_extractor": {},
                    "needs_envelope": False,
                    "auth_config_class_name": auth_config_class_name,
                    "server_vars_kwargs": server_vars_kwargs,
                }
            else:
                # File data is missing or malformed - this is an error
                raise ValueError(
                    f"Download operation '{test_name}' has incomplete cassette data. "
                    f"Expected captured_file_response.body to be a dict with "
                    f"{{'_binary': True, '_base64': '...'}} but got: {file_body!r}. "
                    f"This usually means the cassette recording didn't capture the file download properly. "
                    f"Please re-record the cassette using the cassette generator."
                )
        else:
            # Prepare regular test context - use connector.entity.action() pattern
            operation = self._find_operation(entity, action)
            # Default record_extractor to "$" (root) if not specified, same as _extract_operations
            record_extractor = (operation.x_airbyte_record_extractor if operation else None) or "$"
            meta_extractor = operation.x_airbyte_meta_extractor if operation else None

            # Determine if this operation needs envelope (same logic as _extract_operations)
            action_enum = Action(action)
            needs_envelope = action_enum in LIST_ACTIONS or bool(meta_extractor)

            return {
                "test_name": test_name,
                "description": description,
                "entity": entity,
                "action": action,
                "kwargs_str": kwargs_str,
                "response_repr": response_repr,
                "secrets_dict": secrets_dict,
                "is_download": False,
                "record_extractor": record_extractor,
                "meta_extractor": meta_extractor or {},
                "needs_envelope": needs_envelope,
                "auth_config_class_name": auth_config_class_name,
                "server_vars_kwargs": server_vars_kwargs,
            }

    def _get_search_entities(self) -> list[str]:
        """Return list of entity names that support search operations.

        Reads from x-airbyte-context-store extension in the info section to determine
        which entities have cache/search support enabled.

        Returns:
            List of entity names that support search.
        """
        if not self.spec.info.x_airbyte_context_store:
            return []
        return [entity_cfg.entity for entity_cfg in self.spec.info.x_airbyte_context_store.entities]

    def _extract_search_schemas(self, entities_in_operations: set[str]) -> dict[str, dict]:
        """Extract search schemas from x-airbyte-context-store config.

        Generates schema metadata for entity-specific search types including:
        - Data Pydantic models (e.g., ChargesSearchData)
        - Filter TypedDicts (e.g., ChargesSearchFilter)
        - Result type aliases (e.g., ChargesSearchResult)

        Args:
            entities_in_operations: Set of entity names that have operations defined.
                Only entities in this set will have search schemas generated.

        Returns:
            Dict mapping entity name to schema metadata:
            {
                "charges": {
                    "entity": "charges",
                    "data_type_name": "ChargesSearchData",
                    "filter_type_name": "ChargesSearchFilter",
                    "result_type_name": "ChargesSearchResult",
                    "fields": [
                        {
                            "name": "amount",
                            "python_name": "amount",
                            "type": "int | None",
                            "description": "Amount in cents"
                        },
                        ...
                    ]
                }
            }
        """
        if not self.spec.info.x_airbyte_context_store:
            return {}

        search_schemas = {}
        for entity_config in self.spec.info.x_airbyte_context_store.entities:
            entity_name = entity_config.entity

            # Only include entities that have operations defined
            if entity_name not in entities_in_operations:
                continue

            fields = []
            for field in entity_config.fields:
                # Reuse existing type conversion by constructing schema dict
                # This handles type: "string" and type: ["null", "string"] formats
                schema_dict = {"type": field.type}
                python_type = self._openapi_type_to_python(schema_dict)
                json_type = self._openapi_schema_to_json_type(schema_dict)

                # Generate example value based on base type (excluding null)
                base_type = field.type
                if isinstance(base_type, list):
                    base_type = next((t for t in base_type if t != "null"), "string")
                example_value_json = self._schema_to_example_value({"type": base_type}, field.name, base_indent=8)

                fields.append(
                    {
                        "name": field.name,
                        "python_name": self._sanitize_field_name(field.name),
                        "type": python_type,
                        "json_type": json_type,
                        "example_value_json": example_value_json,
                        "description": field.description,
                    }
                )

            entity_pascal = to_pascal_case(entity_name)
            search_schemas[entity_name] = {
                "entity": entity_name,
                "data_type_name": f"{entity_pascal}SearchData",
                "filter_type_name": f"{entity_pascal}SearchFilter",
                "in_filter_type_name": f"{entity_pascal}InFilter",
                "any_value_filter_type_name": f"{entity_pascal}AnyValueFilter",
                "string_filter_type_name": f"{entity_pascal}StringFilter",
                "sort_filter_type_name": f"{entity_pascal}SortFilter",
                "result_type_name": f"{entity_pascal}SearchResult",
                "query_type_name": f"{entity_pascal}SearchQuery",
                "condition_prefix": entity_pascal,
                "condition_type_name": f"{entity_pascal}Condition",
                "fields": fields,
            }

        return search_schemas

    def _extract_operations(self) -> list[dict]:
        """Extract operations from OpenAPI paths and build method metadata."""
        operations = []

        for path, path_item in self.spec.paths.items():
            for method in ["get", "post", "put", "patch", "delete"]:
                operation = getattr(path_item, method, None)
                if not operation:
                    continue

                # Build operation metadata
                entity = operation.x_airbyte_entity
                action = Action(operation.x_airbyte_action)
                # Default record_extractor to "$" (root) if not specified
                record_extractor = operation.x_airbyte_record_extractor or "$"
                meta_extractor = operation.x_airbyte_meta_extractor

                # Extract parameters
                parameters = self._extract_parameters(operation, action, entity)

                # Always compute record_type (extractor defaults to "$" for root)
                record_type = None
                response_schema = self._get_response_schema_dict(operation)
                if response_schema:
                    record_type = self._determine_extracted_type(response_schema, record_extractor)

                # Infer meta type if meta extractor present
                meta_fields = None
                if meta_extractor:
                    if response_schema:
                        meta_fields = self._infer_meta_type(response_schema, meta_extractor)

                needs_envelope = action in LIST_ACTIONS or meta_extractor

                # Compute response type (now that we have record_type, meta_fields, and needs_envelope)
                response_type = self._get_response_type(action, entity, record_type, needs_envelope)

                op_data = {
                    "method_name": self._get_method_name(operation, method),
                    "http_method": method,
                    "path": path,
                    "entity": entity,
                    "action": action.value,
                    "parameters": parameters,
                    "params_type_name": self._get_params_type_name(entity, action),
                    "response_type": response_type,
                    "description": operation.description or operation.summary or f"{method.upper()} {path}",
                    "record_extractor": record_extractor,
                    "meta_extractor": meta_extractor,
                    "needs_envelope": needs_envelope,
                    "record_type": record_type,
                    "meta_fields": meta_fields,
                    "is_download": action == Action.DOWNLOAD,
                }
                operations.append(op_data)

        return operations

    def _get_method_name(self, operation: Any, http_method: str) -> str:
        """Generate Python method name from operation."""
        if operation.operation_id:
            return to_snake_case(operation.operation_id)

        # Fallback: use x_action + x_entity
        action = operation.x_airbyte_action
        entity = operation.x_airbyte_entity
        return f"{action}_{entity}"

    def _extract_parameters(self, operation: Any, action: Action, entity: str) -> list[dict]:
        """Extract parameters from operation for method signature."""
        params = []

        # Get request body schema if present
        if operation.request_body and operation.request_body.content:
            content = (
                operation.request_body.content.get("application/json")
                or operation.request_body.content.get("multipart/related")
                or operation.request_body.content.get("multipart/form-data")
            )
            if content and content.schema_:
                schema = content.schema_

                # If it's a reference, resolve it
                if isinstance(schema, dict) and "$ref" in schema:
                    schema_name = schema["$ref"].split("/")[-1]
                    if self.spec.components and self.spec.components.schemas:
                        schema = self.spec.components.schemas.get(schema_name)

                # Extract properties from schema (handle both model objects and dicts)
                properties = None
                required_fields = set()

                if schema:
                    # Handle Schema model objects
                    if hasattr(schema, "properties") and schema.properties:
                        properties = schema.properties
                        required_fields = set(schema.required) if hasattr(schema, "required") and schema.required else set()
                    # Handle dict schemas (inline schemas from requestBody)
                    elif isinstance(schema, dict) and schema.get("properties"):
                        properties = schema.get("properties")
                        required_fields = set(schema.get("required", []))

                if properties:
                    for prop_name, prop_schema in properties.items():
                        # Extract description safely for both dicts and models
                        if isinstance(prop_schema, dict):
                            description = prop_schema.get("description", "")
                        else:
                            description = prop_schema.description if hasattr(prop_schema, "description") else ""

                        params.append(
                            {
                                "name": prop_name,
                                "python_name": self._sanitize_param_name(prop_name),
                                "type": self._openapi_type_to_python(
                                    prop_schema,
                                    parent_name=self._get_params_type_name(entity, action),
                                    field_name=prop_name,
                                    context="param",
                                ),
                                "schema": prop_schema,  # Store original schema for docs
                                "required": prop_name in required_fields,
                                "description": description,
                            }
                        )

        # Add path and query parameters
        if operation.parameters:
            for param in operation.parameters:
                if param.in_ == "path":
                    param_schema = param.schema_ if hasattr(param, "schema_") else None
                    params.append(
                        {
                            "name": param.name,
                            "python_name": self._sanitize_param_name(param.name),
                            "type": "str",  # Path params are usually strings
                            "schema": param_schema,  # Store original schema for docs
                            "required": param.required if hasattr(param, "required") else True,
                            "description": param.description or "",
                        }
                    )
                elif param.in_ == "query":
                    # Extract type from param.schema_ if available
                    param_type = "str"  # Default type for query params
                    is_deep_object = False
                    param_schema = param.schema_ if hasattr(param, "schema_") else None

                    if hasattr(param, "schema_") and param.schema_:
                        # Check if this is a deepObject style parameter
                        if hasattr(param, "style") and param.style == "deepObject":
                            is_deep_object = True

                            # Validate: deepObject params must use inline schemas, not $ref
                            if isinstance(param.schema_, dict) and "$ref" in param.schema_:
                                raise ValueError(
                                    f"DeepObject query parameter '{param.name}' in {entity}.{action.value} "
                                    f"uses a schema reference ($ref: {param.schema_['$ref']}). "
                                    f"DeepObject parameters must use inline schemas. "
                                    f"Please define the schema inline instead of using a $ref."
                                )

                        # Pass parent/field context for proper nested type generation
                        param_type = self._openapi_type_to_python(
                            param.schema_,
                            parent_name=self._get_params_type_name(entity, action),
                            field_name=param.name,
                            context="param",
                        )

                    params.append(
                        {
                            "name": param.name,
                            "python_name": self._sanitize_param_name(param.name),
                            "type": param_type,
                            "schema": param_schema,  # Store original schema for docs
                            "required": param.required if hasattr(param, "required") else False,
                            "description": param.description or "",
                            "is_deep_object": is_deep_object,
                        }
                    )

        # Add download-specific parameter
        if action == Action.DOWNLOAD:
            # Create a simple string schema for this synthetic param
            string_schema = {"type": "string"}
            params.append(
                {
                    "name": "range_header",
                    "python_name": "range_header",  # Already valid Python identifier
                    "type": "str",
                    "schema": string_schema,  # Simple string schema
                    "required": False,
                    "description": "Optional Range header for partial downloads (e.g., 'bytes=0-99')",
                }
            )

        return params

    def _get_response_type(
        self,
        action: Action,
        entity: str,
        record_type: str | None,
        needs_envelope: bool,
    ) -> str:
        """Determine the response type name for an operation.

        This method handles response types based on:
        - Download action: Returns AsyncIterator[bytes]
        - Needs envelope (array type or has meta): Returns envelope type (e.g., UsersListResult)
        - No envelope needed: Returns the record type directly (e.g., User)
        """
        # Handle download action with streaming response
        if action == Action.DOWNLOAD:
            return "AsyncIterator[bytes]"

        # If no record type could be determined, fall back to dict
        if not record_type:
            return "dict[str, Any]"

        # Use envelope for arrays or when meta is present
        if needs_envelope:
            return self._get_envelope_type_name(entity, action)

        # No envelope needed - return the record type directly
        return record_type

    def _get_response_schema_dict(self, operation: Any) -> dict[str, Any] | None:
        """Extract response schema as dict from operation."""
        if not operation.responses:
            return None

        # Get 200/201 response
        success_response = operation.responses.get("200") or operation.responses.get("201")
        if not success_response or not success_response.content:
            return None

        content = success_response.content.get("application/json")
        if not content or not content.schema_:
            return None

        schema = content.schema_

        # Convert schema object to dict if needed
        if hasattr(schema, "model_dump"):
            return schema.model_dump(exclude_none=True)
        elif isinstance(schema, dict):
            return schema

        return None

    def _navigate_schema_with_jsonpath(self, schema: dict[str, Any], jsonpath_expr: str) -> dict[str, Any] | None:
        """Navigate through a resolved schema using JSONPath to find target type.

        Args:
            schema: Resolved OpenAPI schema (all $refs expanded)
            jsonpath_expr: JSONPath expression (e.g., '$.users', '$.data.items')

        Returns:
            Schema dict at the JSONPath location, or None if not found
        """

        # Parse JSONPath expression
        try:
            jsonpath = parse_jsonpath(jsonpath_expr)
        except Exception:
            # Invalid JSONPath - return None
            return None

        # JSONPath match expects dict structure like {"users": [...]}
        # But OpenAPI schema has {"properties": {"users": {...}}}
        # We need to simulate a response structure for JSONPath matching

        # Build a mock response structure from schema to match against
        mock_data = self._build_mock_data_from_schema(schema)

        # Find matches
        matches = jsonpath.find(mock_data)

        if not matches:
            return None

        # Get the first match and trace back to schema
        match = matches[0]

        # Now find the corresponding schema for this path
        return self._find_schema_for_path(schema, match.full_path)

    def _build_mock_data_from_schema(self, schema: dict[str, Any]) -> dict[str, Any]:
        """Build mock data structure from schema for JSONPath matching.

        This creates a minimal structure that matches the response shape
        so JSONPath expressions can be evaluated against it.
        """
        if not isinstance(schema, dict):
            return {}

        schema_type = schema.get("type")

        if schema_type == "object" and "properties" in schema:
            # Build dict with property names
            result = {}
            for prop_name, prop_schema in schema.get("properties", {}).items():
                result[prop_name] = self._build_mock_data_from_schema(prop_schema)
            return result
        elif schema_type == "array":
            # Return single-item array
            items_schema = schema.get("items", {})
            return [self._build_mock_data_from_schema(items_schema)]
        else:
            # Primitive type - return placeholder
            return None

    def _find_schema_for_path(self, schema: dict[str, Any], jsonpath: Any) -> dict[str, Any] | None:
        """Find the schema definition for a JSONPath match.

        Args:
            schema: Root schema
            jsonpath: JSONPath object from match.full_path

        Returns:
            Schema dict at that path
        """
        # Navigate schema following the JSONPath
        current = schema

        # Convert jsonpath to list of property names
        path_parts = []
        for part in str(jsonpath).split("."):
            # Remove array indices [0]
            part = part.replace("[0]", "").replace("$", "").strip(".")
            if part:
                path_parts.append(part)

        # Navigate through schema properties
        for part in path_parts:
            if isinstance(current, dict):
                if "properties" in current and part in current["properties"]:
                    current = current["properties"][part]
                elif "items" in current:
                    # Array schema - go to items
                    current = current["items"]
                else:
                    return None
            else:
                return None

        return current if isinstance(current, dict) else None

    def _resolve_schema_ref(self, schema: dict[str, Any]) -> tuple[dict[str, Any], str | None]:
        """Resolve a $ref in a schema to its actual schema dict.

        Args:
            schema: Schema dict that may contain a $ref

        Returns:
            Tuple of (resolved_schema, ref_name) where ref_name is the original
            reference name if it was a $ref, or None otherwise.
        """
        if not isinstance(schema, dict) or "$ref" not in schema:
            return schema, None

        ref_name = schema["$ref"].split("/")[-1]

        if self.spec.components and self.spec.components.schemas:
            schema_obj = self.spec.components.schemas.get(ref_name)
            if schema_obj:
                if hasattr(schema_obj, "model_dump"):
                    return schema_obj.model_dump(exclude_none=True), ref_name
                elif isinstance(schema_obj, dict):
                    return schema_obj, ref_name

        return schema, ref_name

    def _determine_extracted_type(self, response_schema: dict[str, Any], record_extractor: str) -> str:
        """Determine the Python type of extracted records.

        Args:
            response_schema: Response schema dict (may contain $ref)
            record_extractor: JSONPath expression (e.g., '$.users', '$.list[*].customer', or '$' for root)

        Returns:
            Python type string (e.g., 'list[User]', 'User', 'dict[str, Any]')
        """
        # Parse JSONPath parts (empty for root extraction "$" or "")
        path_parts = [p for p in record_extractor.strip("$").strip(".").split(".") if p]

        # Resolve top-level $ref
        current_schema, ref_name = self._resolve_schema_ref(response_schema)

        # Track whether we traversed an array wildcard [*] — if so, the result is a list
        traversed_array = False

        # Navigate through schema following the path
        for part in path_parts:
            if not isinstance(current_schema, dict):
                return "dict[str, Any]"

            # Strip array wildcard notation (e.g., "list[*]" -> "list")
            # JSONPath uses [*] to denote array traversal, but schema properties use bare names
            has_array_wildcard = "[*]" in part
            property_name = re.sub(r"\[\*\]$", "", part)

            properties = current_schema.get("properties", {})
            if property_name not in properties:
                return "dict[str, Any]"

            current_schema, ref_name = self._resolve_schema_ref(properties[property_name])

            # If the part had [*], descend into array items
            if has_array_wildcard and isinstance(current_schema, dict) and current_schema.get("type") == "array":
                items_schema = current_schema.get("items", {})
                current_schema, ref_name = self._resolve_schema_ref(items_schema)
                traversed_array = True

        # If schema is an array, extract items type
        if isinstance(current_schema, dict) and current_schema.get("type") == "array":
            items_schema = current_schema.get("items", {})
            return f"list[{self._openapi_type_to_python(items_schema)}]"

        # Determine the element type
        element_type = ref_name or self._openapi_type_to_python(current_schema)

        # If we traversed an array wildcard [*], the extractor produces a list of items
        if traversed_array:
            return f"list[{element_type}]"

        return element_type

    def _get_envelope_type_name(self, entity: str, action: Action) -> str:
        """Generate result type name for operations with extractors.

        Args:
            entity: Entity name (e.g., 'users')
            action: Action enum (e.g., Action.LIST)

        Returns:
            Result type name (e.g., 'UsersListResult')
        """
        entity_title = to_pascal_case(entity)
        action_title = to_pascal_case(action)
        return f"{entity_title}{action_title}Result"

    def _infer_meta_type(self, response_schema: dict[str, Any], meta_extractor: dict[str, str]) -> str:
        """Infer the TypedDict structure for metadata from meta extractor config.

        Args:
            response_schema: Response schema dict (may contain $ref)
            meta_extractor: Dict mapping field names to JSONPath expressions

        Returns:
            Meta type name (e.g., 'UsersListMeta') or 'dict[str, Any]' if cannot infer
        """
        if not meta_extractor:
            return "dict[str, Any]"

        # Resolve top-level $ref if present
        if "$ref" in response_schema:
            ref_path = response_schema["$ref"]
            schema_name = ref_path.split("/")[-1]
            if self.spec.components and self.spec.components.schemas:
                schema_obj = self.spec.components.schemas.get(schema_name)
                if schema_obj:
                    if hasattr(schema_obj, "model_dump"):
                        response_schema = schema_obj.model_dump(exclude_none=True)
                    elif isinstance(schema_obj, dict):
                        response_schema = schema_obj

        # Try to infer type for each meta field
        meta_fields = []
        for field_name, extractor_expr in meta_extractor.items():
            # Handle header-based extractors - they extract string values from HTTP headers
            # @link.next extracts from RFC 5988 Link header
            # @header.X-Name extracts raw header value
            if extractor_expr.startswith("@link.") or extractor_expr.startswith("@header."):
                meta_fields.append(
                    {
                        "name": field_name,
                        "python_name": self._sanitize_field_name(field_name),
                        "type": "str | None",
                        "schema": {"type": "string", "nullable": True},
                    }
                )
                continue

            field_type, field_schema = self._infer_type_from_jsonpath(response_schema, extractor_expr)

            # If schema couldn't be inferred, it means the JSONPath doesn't exist in the response schema
            if field_schema is None:
                raise ValueError(
                    f"Meta field '{field_name}' with JSONPath '{extractor_expr}' could not be resolved "
                    f"in the response schema. Verify that the response schema includes all fields "
                    f"referenced by the x-airbyte-meta-extractor JSONPath expressions."
                )

            meta_fields.append(
                {
                    "name": field_name,
                    "python_name": self._sanitize_field_name(field_name),
                    "type": field_type,
                    "schema": field_schema,  # Store original schema for docs
                }
            )

        # Return field information for inline TypedDict generation
        return meta_fields

    def _infer_type_from_jsonpath(self, schema: dict[str, Any], jsonpath_expr: str) -> tuple[str, dict[str, Any] | None]:
        """Infer Python type from a JSONPath expression on a schema.

        Args:
            schema: OpenAPI schema dict
            jsonpath_expr: JSONPath expression (e.g., '$.records', '$.records.cursor')

        Returns:
            Tuple of (Python type string, schema dict or None)
        """
        # Parse JSONPath to get property names
        path_parts = jsonpath_expr.strip("$").strip(".").split(".")

        # Navigate through schema
        current_schema = schema
        for part in path_parts:
            if not part:
                continue

            if isinstance(current_schema, dict):
                properties = current_schema.get("properties", {})
                if part in properties:
                    prop_schema = properties[part]
                    # Check if it's a $ref
                    if isinstance(prop_schema, dict) and "$ref" in prop_schema:
                        ref_name = prop_schema["$ref"].split("/")[-1]
                        # If this is the last part of the path, return the ref name
                        # Otherwise, resolve it to continue navigating
                        is_last_part = path_parts.index(part) == len(path_parts) - 1
                        if is_last_part:
                            # This is the final field - return the ref type name
                            return ref_name, prop_schema
                        else:
                            # Not the last part, need to resolve and continue navigating
                            if self.spec.components and self.spec.components.schemas and ref_name in self.spec.components.schemas:
                                # Get the actual schema from components
                                ref_schema = self.spec.components.schemas[ref_name]
                                # Convert to dict if it's a Pydantic model
                                if hasattr(ref_schema, "model_dump"):
                                    current_schema = ref_schema.model_dump(exclude_none=True)
                                else:
                                    current_schema = ref_schema
                            else:
                                # Can't resolve ref, return what we have
                                return ref_name, prop_schema
                    else:
                        current_schema = prop_schema
                else:
                    # Property not found
                    return "Any", None
            else:
                return "Any", None

        # Convert final schema to Python type
        if isinstance(current_schema, dict):
            return self._openapi_type_to_python(current_schema), current_schema

        return "Any", None

    def _generate_envelope_types(self, operations: list[dict]) -> list[dict]:
        """Generate envelope type definitions for operations with both extractors.

        Args:
            operations: List of operation metadata dicts

        Returns:
            List of envelope type definitions for template rendering
        """
        envelope_types = []
        seen_envelopes = set()

        for op in operations:
            if not op.get("needs_envelope"):
                continue

            # Generate envelope base name from entity and action
            entity = op["entity"]
            action = Action(op["action"])
            envelope_name = self._get_envelope_type_name(entity, action)

            record_type = op.get("record_type", "dict[str, Any]")

            # Infer meta type from meta extractor config
            meta_type = op.get("meta_type", "dict[str, Any]")
            meta_fields = op.get("meta_fields", None)

            # Avoid duplicates
            if envelope_name in seen_envelopes:
                continue

            seen_envelopes.add(envelope_name)

            envelope_types.append(
                {
                    "name": envelope_name,
                    "record_type": record_type,
                    "entity": entity,
                    "action": action,
                    "description": f"Result envelope for {entity}.{action} operation",
                    "meta_type": meta_type,
                    "meta_fields": meta_fields,
                }
            )

        return envelope_types

    def _extract_component_schemas_only(self) -> dict[str, dict]:
        """Extract only component schemas (not nested parameter schemas) for Pydantic models.

        Returns schemas in topologically sorted order so nested schemas are
        defined before their parent schemas.
        """
        schemas = {}

        if not self.spec.components or not self.spec.components.schemas:
            return schemas

        # Track nested schemas discovered while extracting component schemas
        component_nested_schemas = {}

        for name, schema in self.spec.components.schemas.items():
            schemas[name] = {
                "name": name,
                "fields": self._extract_fields(schema, parent_name=name),
                "description": schema.description if hasattr(schema, "description") else "",
                "has_optional_fields": self._has_optional_fields(schema),
            }

        # Add nested Pydantic schemas discovered from component schemas
        # These are nested objects in response schemas (e.g., Customer.address → CustomerAddress)
        schemas.update(self._pydantic_nested_schemas)

        # Recursively find dependencies of Pydantic nested schemas
        visited = set()

        def find_nested_deps(schema_dict: dict):
            """Recursively find all nested schema dependencies."""
            for field in schema_dict["fields"]:
                # Extract all type names from the field type
                for match in re.finditer(r"\b([A-Z][a-zA-Z0-9_]*)\b", field["type"]):
                    dep_name = match.group(1)
                    if dep_name in visited:
                        continue
                    # Check if this is a Pydantic nested schema
                    if dep_name in (self._pydantic_nested_schemas or {}) and dep_name not in component_nested_schemas:
                        visited.add(dep_name)
                        component_nested_schemas[dep_name] = self._pydantic_nested_schemas[dep_name]
                        # Recursively find dependencies of this nested schema
                        find_nested_deps(self._pydantic_nested_schemas[dep_name])

        # Start from all Pydantic nested schemas and find their nested dependencies
        for nested_schema in self._pydantic_nested_schemas.values():
            find_nested_deps(nested_schema)

        schemas.update(component_nested_schemas)

        # Topologically sort schemas so dependencies come before dependents
        return self._topological_sort_schemas(schemas)

    def _extract_schemas(self) -> dict[str, dict]:
        """Extract TypedDict schemas from OpenAPI components.

        This method extracts both top-level schemas and recursively discovers
        nested object schemas, creating separate TypedDict definitions for each.

        Returns schemas in topologically sorted order so nested schemas are
        defined before their parent schemas.
        """
        schemas = {}

        if not self.spec.components or not self.spec.components.schemas:
            return schemas

        # Track nested schemas to avoid duplicates
        # Note: Don't reset if already populated from parameter extraction
        if not hasattr(self, "_nested_schemas"):
            self._nested_schemas = {}

        for name, schema in self.spec.components.schemas.items():
            schemas[name] = {
                "name": name,
                "fields": self._extract_fields(schema, parent_name=name),
                "description": schema.description if hasattr(schema, "description") else "",
                "has_optional_fields": self._has_optional_fields(schema),
            }

        # Add all discovered nested schemas
        schemas.update(self._nested_schemas)

        # Topologically sort schemas so dependencies come before dependents
        return self._topological_sort_schemas(schemas)

    def _topological_sort_schemas(self, schemas: dict[str, dict]) -> dict[str, dict]:
        """Topologically sort schemas so dependencies are defined before dependents.

        Args:
            schemas: Dict mapping schema name to schema metadata

        Returns:
            OrderedDict with schemas in topologically sorted order
        """
        # Build dependency graph: schema_name -> list of schemas it depends on
        dependencies = {}
        for name, schema in schemas.items():
            deps = set()
            for field in schema["fields"]:
                # Extract type names from field types
                field_type = field["type"]
                # Look for references to other TypedDicts (capitalized names)
                # Pattern to find TypedDict references
                for match in re.finditer(r"\b([A-Z][a-zA-Z0-9_]*)\b", field_type):
                    dep_name = match.group(1)
                    # Only add if it's actually a schema we're defining
                    if dep_name in schemas and dep_name != name:
                        deps.add(dep_name)

            dependencies[name] = deps

        # Topological sort using DFS
        sorted_names = []
        visited = set()
        in_progress = set()

        def visit(name: str):
            if name in visited:
                return
            if name in in_progress:
                # Circular dependency - just continue
                return

            in_progress.add(name)
            for dep in dependencies.get(name, []):
                visit(dep)
            in_progress.remove(name)

            visited.add(name)
            sorted_names.append(name)

        for name in schemas.keys():
            visit(name)

        # Return schemas in sorted order
        return OrderedDict((name, schemas[name]) for name in sorted_names)

    def _extract_fields(self, schema: Any, parent_name: str = "", context: str = "response") -> list[dict]:
        """Extract fields from schema for TypedDict.

        Args:
            schema: OpenAPI schema object
            parent_name: Name of parent schema (for generating nested schema names)
            context: Generation context - "param" for parameters, "response" for responses

        Returns:
            List of field metadata dicts
        """
        fields = []

        if not hasattr(schema, "properties") or not schema.properties:
            return fields

        required = set(schema.required) if hasattr(schema, "required") and schema.required else set()

        for field_name, field_schema in schema.properties.items():
            # Check if this is a nested object that should become its own TypedDict
            type_name = self._openapi_type_to_python(
                field_schema,
                parent_name=parent_name,
                field_name=field_name,
                context=context,
            )

            fields.append(
                {
                    "name": field_name,
                    "python_name": self._sanitize_field_name(field_name),
                    "type": type_name,
                    "schema": field_schema,  # Store original schema for docs
                    "required": field_name in required,
                    "description": field_schema.description if hasattr(field_schema, "description") else "",
                }
            )

        return fields

    def _has_optional_fields(self, schema: Any) -> bool:
        """Check if schema has any optional fields."""
        if not hasattr(schema, "properties") or not schema.properties:
            return False

        required = set(schema.required) if hasattr(schema, "required") and schema.required else set()
        return len(schema.properties) > len(required)

    def _openapi_type_to_python(
        self,
        schema: Any,
        parent_name: str = "",
        field_name: str = "",
        context: str = "response",
    ) -> str:
        """Convert OpenAPI type to Python type annotation.

        Args:
            schema: OpenAPI schema object
            parent_name: Name of parent schema (for generating nested schema names)
            field_name: Name of the field this schema belongs to
            context: Generation context - "param" for parameters, "response" for responses

        Returns:
            Python type annotation string
        """
        # Handle dict with $ref (raw reference from spec)
        if isinstance(schema, dict):
            if "$ref" in schema:
                return schema["$ref"].split("/")[-1]
            # Handle inline schema in dict form
            schema_type = schema.get("type")
            if schema_type:
                # Handle nullable types: type: ["object", "null"]
                if isinstance(schema_type, list):
                    non_null_types = [t for t in schema_type if t != "null"]
                    is_nullable = "null" in schema_type
                    if len(non_null_types) == 1:
                        # Create a modified schema with the single type
                        modified_schema = {**schema, "type": non_null_types[0]}
                        base_type = self._openapi_type_to_python(modified_schema, parent_name, field_name, context)
                        return f"{base_type} | None" if is_nullable else base_type
                    elif len(non_null_types) == 0:
                        return "None"
                    else:
                        return "Any"

                if schema_type == "array":
                    items = schema.get("items")
                    if items:
                        # For array items, append "Item" to the parent field name
                        item_field_name = f"{field_name}_item" if field_name else ""
                        items_type = self._openapi_type_to_python(items, parent_name, item_field_name, context)
                        return f"list[{items_type}]"
                    return "list[Any]"
                if schema_type == "object":
                    # Check if this object has properties - if so, create a TypedDict
                    properties = schema.get("properties")
                    if properties and parent_name and field_name:
                        # Generate nested TypedDict
                        return self._create_nested_schema(schema, parent_name, field_name, context)

                    # Otherwise, treat as a dict
                    additional_props = schema.get("additionalProperties")
                    if additional_props is True:
                        return "dict[str, Any]"
                    elif additional_props:
                        value_type = self._openapi_type_to_python(additional_props, parent_name, field_name, context)
                        return f"dict[str, {value_type}]"
                    return "dict[str, Any]"
                return self.JSON_TO_PYTHON_TYPE_MAP.get(schema_type, "Any")
            return "Any"

        # Handle Schema model objects with ref attribute (legacy check)
        if hasattr(schema, "ref") and schema.ref:
            return schema.ref.split("/")[-1]

        if not hasattr(schema, "type"):
            return "Any"

        schema_type = schema.type

        # Handle nullable types: type: ["object", "null"]
        if isinstance(schema_type, list):
            non_null_types = [t for t in schema_type if t != "null"]
            is_nullable = "null" in schema_type
            if len(non_null_types) == 1:
                # Recursively process with the single non-null type
                single_type = non_null_types[0]
                if single_type == "array":
                    if hasattr(schema, "items") and schema.items:
                        item_field_name = f"{field_name}_item" if field_name else ""
                        items_type = self._openapi_type_to_python(schema.items, parent_name, item_field_name, context)
                        base_type = f"list[{items_type}]"
                    else:
                        base_type = "list[Any]"
                elif single_type == "object":
                    # Check if this object has properties
                    if hasattr(schema, "properties") and schema.properties and parent_name and field_name:
                        base_type = self._create_nested_schema(schema, parent_name, field_name, context)
                    elif hasattr(schema, "additional_properties"):
                        if schema.additional_properties is True:
                            base_type = "dict[str, Any]"
                        elif schema.additional_properties:
                            value_type = self._openapi_type_to_python(
                                schema.additional_properties,
                                parent_name,
                                field_name,
                                context,
                            )
                            base_type = f"dict[str, {value_type}]"
                        else:
                            base_type = "dict[str, Any]"
                    else:
                        base_type = "dict[str, Any]"
                else:
                    base_type = self.JSON_TO_PYTHON_TYPE_MAP.get(single_type, "Any")
                return f"{base_type} | None" if is_nullable else base_type
            elif len(non_null_types) == 0:
                return "None"
            else:
                return "Any"

        if schema_type == "array":
            if hasattr(schema, "items") and schema.items:
                item_field_name = f"{field_name}_item" if field_name else ""
                items_type = self._openapi_type_to_python(schema.items, parent_name, item_field_name, context)
                return f"list[{items_type}]"
            return "list[Any]"

        if schema_type == "object":
            # Check if this object has properties - if so, create a TypedDict
            if hasattr(schema, "properties") and schema.properties and parent_name and field_name:
                return self._create_nested_schema(schema, parent_name, field_name, context)

            # Otherwise, treat as a dict
            if hasattr(schema, "additional_properties"):
                if schema.additional_properties is True:
                    return "dict[str, Any]"
                elif schema.additional_properties:
                    value_type = self._openapi_type_to_python(schema.additional_properties, parent_name, field_name, context)
                    return f"dict[str, {value_type}]"
            return "dict[str, Any]"

        return self.JSON_TO_PYTHON_TYPE_MAP.get(schema_type, "Any")

    def _create_nested_schema(self, schema: Any, parent_name: str, field_name: str, context: str = "response") -> str:
        """Create a nested TypedDict schema for an inline object.

        Args:
            schema: OpenAPI schema object with properties
            parent_name: Name of parent schema
            field_name: Name of the field this schema belongs to
            context: Generation context - "param" for parameters, "response" for responses

        Returns:
            Name of the generated TypedDict
        """
        # Generate unique name: ParentNameFieldName
        # Convert field_name to PascalCase
        field_name_pascal = "".join(word.capitalize() for word in field_name.replace("_", " ").split())
        nested_name = f"{parent_name}{field_name_pascal}"

        # Check if we already created this nested schema
        if nested_name in self._nested_schemas:
            return nested_name

        # Extract description
        description = ""
        if isinstance(schema, dict):
            description = schema.get("description", "")
        elif hasattr(schema, "description"):
            description = schema.description or ""

        # Convert schema to a format we can extract fields from
        # Handle both dict and object schemas
        if isinstance(schema, dict):
            properties = schema.get("properties", {})
            required_fields = set(schema.get("required", []))

            # For dict schemas, we need to process properties manually
            fields = []
            for prop_name, prop_schema in properties.items():
                # Recursively process nested properties
                prop_type = self._openapi_type_to_python(
                    prop_schema,
                    parent_name=nested_name,
                    field_name=prop_name,
                    context=context,
                )
                prop_description = ""
                if isinstance(prop_schema, dict):
                    prop_description = prop_schema.get("description", "")
                elif hasattr(prop_schema, "description"):
                    prop_description = prop_schema.description or ""

                fields.append(
                    {
                        "name": prop_name,
                        "python_name": self._sanitize_field_name(prop_name),
                        "type": prop_type,
                        "schema": prop_schema,  # Store original schema for docs
                        "required": prop_name in required_fields,
                        "description": prop_description,
                    }
                )
        else:
            # Schema object with properties attribute
            fields = self._extract_fields(schema, parent_name=nested_name, context=context)

        # Check if has optional fields
        has_optional = any(not field["required"] for field in fields)

        schema_metadata = {
            "name": nested_name,
            "fields": fields,
            "description": description or f"Nested schema for {parent_name}.{field_name}",
            "has_optional_fields": has_optional,
        }

        # Store in appropriate location based on context
        if context == "param":
            # Parameter context: TypedDict for types.py
            self._nested_schemas[nested_name] = schema_metadata
        else:
            # Response context: Pydantic model for models.py
            self._pydantic_nested_schemas[nested_name] = schema_metadata

        return nested_name

    def _get_params_type_name(self, entity: str, action: Action) -> str:
        """Generate TypedDict name for operation parameters."""
        resource_title = to_pascal_case(entity)
        verb_title = to_pascal_case(action.value)
        return f"{resource_title}{verb_title}Params"

    def _get_class_name(self, connector_name: str) -> str:
        """Generate class name from connector name."""
        return to_pascal_case(connector_name) + "Connector"

    def _get_envelope_prefix(self, connector_name: str) -> str:
        """Generate envelope prefix from connector name.

        Used for Pydantic envelope model names:
        - "gong" -> "Gong"
        - "zendesk-support" -> "ZendeskSupport"
        """
        return to_pascal_case(connector_name)

    def _build_param_map(self, operations: list) -> dict:
        """Build parameter name mapping for execute() remapping.

        Creates a nested dict mapping (entity, action) -> {python_name: api_name}
        to convert snake_case TypedDict keys back to original API parameter names.

        Args:
            operations: List of operation dicts with entity, action, and parameters

        Returns:
            Dict like {("entity", "action"): {"python_name": "apiName", ...}}

        Example:
            {
                ("issues", "get"): {
                    "issue_id_or_key": "issueIdOrKey",
                    "fields": "fields"
                }
            }
        """
        param_map = {}
        for op in operations:
            entity = op["entity"]
            action = op["action"]
            parameters = op.get("parameters", [])

            if parameters:
                # Build mapping for this action
                action_map = {}
                for param in parameters:
                    python_name = param["python_name"]
                    api_name = param["name"]
                    action_map[python_name] = api_name

                # Only add operation to map if it has parameter mappings
                if action_map:
                    param_map[(entity, action)] = action_map
        return param_map

    def _sanitize_param_name(self, name: str) -> str:
        """Convert API parameter name to valid Python identifier.

        Args:
            name: Original API parameter name (e.g., 'workspace-id', 'from', 'page[size]')

        Returns:
            Valid Python identifier (e.g., 'workspace_id', 'from_', 'page_size')
        """
        result = to_snake_case(name)

        # Remove any characters that aren't valid for Python identifiers
        # Valid: letters, digits, underscores
        result = re.sub(r"[^a-zA-Z0-9_]", "_", result)

        # Collapse multiple consecutive underscores into one
        result = re.sub(r"_+", "_", result)

        # Remove leading/trailing underscores (unless it's the only char)
        result = result.strip("_") or "_"

        # Ensure it doesn't start with a digit
        if result[0].isdigit():
            result = f"_{result}"

        # Python reserved keywords that need to be escaped
        if result in PYTHON_KEYWORDS:
            result = f"{result}_"

        return result

    def _sanitize_field_name(self, name: str) -> str:
        """Convert schema field name to valid Python identifier that doesn't conflict with Pydantic.

        Args:
            name: Original schema field name (e.g., 'schema', 'model_fields', 'my-field')

        Returns:
            Valid Python identifier that doesn't shadow Pydantic attributes (e.g., 'schema_', 'model_fields_', 'my_field')
        """
        result = to_snake_case(name)

        # Remove any characters that aren't valid for Python identifiers
        # Valid: letters, digits, underscores
        result = re.sub(r"[^a-zA-Z0-9_]", "_", result)

        # Collapse multiple consecutive underscores into one
        result = re.sub(r"_+", "_", result)

        # Remove leading/trailing underscores (unless it's the only char)
        result = result.strip("_") or "_"

        # Ensure it doesn't start with a digit
        if result[0].isdigit():
            result = f"field_{result}"

        # Python reserved keywords that need to be escaped
        if result in PYTHON_KEYWORDS:
            result = f"{result}_"

        # Pydantic reserved names that would cause field shadowing
        if result in PYDANTIC_RESERVED_NAMES:
            result = f"{result}_"

        # Python builtin type names that would shadow type annotations in Pydantic models
        if result in PYTHON_BUILTIN_TYPE_NAMES:
            result = f"{result}_"

        return result

    def _get_example_value_for_param(self, param: dict, base_indent: int = 4) -> str:
        """Generate simple placeholder for a parameter based on OpenAPI schema.

        Args:
            param: Parameter dict with 'name' and 'schema' keys
            base_indent: Base indentation level in spaces (4 for Python, 8 for JSON)

        Returns:
            Simple placeholder string for code examples (e.g., "{}", "[]", "0")

        Raises:
            ValueError: If parameter doesn't have name or schema field
        """
        param_name = param.get("name")
        if not param_name:
            raise ValueError(f"Parameter dict is missing 'name' field. This indicates a bug in parameter extraction. Param: {param}")

        param_schema = param.get("schema")
        if not param_schema:
            raise ValueError(
                f"Parameter '{param_name}' is missing 'schema' field. "
                f"All parameters must include their OpenAPI schema for accurate example generation."
            )

        if not isinstance(param_schema, dict):
            raise ValueError(f"Parameter '{param_name}' has invalid schema (expected dict, got {type(param_schema).__name__})")

        return self._schema_to_example_value(param_schema, param_name, base_indent)

    def _schema_to_example_value(self, schema: dict, field_name: str = "field", base_indent: int = 4) -> str:
        """Recursively generate example value from OpenAPI schema with proper indentation.

        Args:
            schema: OpenAPI schema dict
            field_name: Name of field for error messages
            base_indent: Base indentation level in spaces

        Returns:
            Example value string suitable for code with proper indentation
        """
        schema_type = schema.get("type")

        if schema_type == "object":
            # Check for required nested properties
            properties = schema.get("properties", {})
            required = schema.get("required", [])

            if required and properties:
                # Build object with required fields on separate lines with proper indentation
                nested_examples = []
                content_indent = base_indent + 4  # Content indented 4 spaces from base

                for req_field in required:
                    if req_field in properties:
                        prop_schema = properties[req_field]
                        # Recursively generate nested value with increased indent
                        nested_value = self._schema_to_example_value(prop_schema, req_field, content_indent)
                        # Add field with proper indentation
                        nested_examples.append(f'{" " * content_indent}"{req_field}": {nested_value}')

                # Format: opening brace inline, fields on new lines, closing brace at base indent
                fields = ",\n".join(nested_examples)
                return "{\n" + fields + f"\n{' ' * base_indent}" + "}"
            else:
                return "{}"

        elif schema_type == "array":
            return "[]"
        elif schema_type == "boolean":
            return "True"
        elif schema_type == "integer":
            return "0"
        elif schema_type == "number":
            return "0.0"
        elif schema_type == "string":
            # Check for date-time format to provide better examples
            if schema.get("format") == "date-time":
                return '"2025-01-01T00:00:00Z"'
            return '"<str>"'
        else:
            raise ValueError(f"Field '{field_name}' has unsupported or missing schema type. Schema: {schema}")

    def _flatten_nested_parameters(self, parameters: list[dict], prefix: str = "") -> list[dict]:
        """Flatten nested parameter types into dot notation.

        Args:
            parameters: List of parameter dicts
            prefix: Prefix for nested fields (e.g., "filter.")

        Returns:
            Flattened list of parameters with dot notation and JSON Schema types
        """
        flattened = []

        for param in parameters:
            param_type = param.get("type", "")
            param_name = param.get("name", "")
            param_schema = param.get("schema")

            # Get JSON type from schema
            json_type = self._openapi_schema_to_json_type(param_schema)

            # Check if this is a nested TypedDict (PascalCase type name)
            # Extract base type name (remove list[], dict[], etc.)
            base_type = param_type
            for wrapper in ["list[", "dict[", "Optional[", "NotRequired["]:
                if wrapper in base_type:
                    # Extract type from wrapper
                    start = base_type.find(wrapper) + len(wrapper)
                    end = base_type.rfind("]")
                    if end > start:
                        base_type = base_type[start:end].split(",")[-1].strip()
                        break

            # Check if this type is a nested schema we generated
            nested_schemas = self._nested_schemas if hasattr(self, "_nested_schemas") else {}

            if base_type in nested_schemas:
                # This is a nested type - first add the parent object itself
                parent_param = param.copy()
                if prefix:
                    parent_param["name"] = f"{prefix}{param_name}"
                    parent_param["python_name"] = f"{prefix.replace('.', '_')}{param.get('python_name', param_name)}"
                # Use the JSON type we already computed
                parent_param["json_type"] = json_type
                flattened.append(parent_param)

                # Then recursively flatten nested fields
                nested_schema = nested_schemas[base_type]
                nested_fields = nested_schema.get("fields", [])

                # Convert nested fields to parameter format and flatten recursively
                nested_params = []
                for field in nested_fields:
                    nested_params.append(
                        {
                            "name": field["name"],
                            "python_name": self._sanitize_param_name(field["name"]),
                            "type": field["type"],
                            "schema": field.get("schema"),  # Pass through original schema
                            "required": field["required"],
                            "description": field["description"],
                        }
                    )

                # Recursively flatten with dot notation prefix
                new_prefix = f"{prefix}{param_name}."
                flattened.extend(self._flatten_nested_parameters(nested_params, new_prefix))
            else:
                # Regular parameter - add with prefix
                flattened_param = param.copy()
                if prefix:
                    flattened_param["name"] = f"{prefix}{param_name}"
                    flattened_param["python_name"] = f"{prefix.replace('.', '_')}{param.get('python_name', param_name)}"
                # Use the JSON type we already computed from schema or Python type
                flattened_param["json_type"] = json_type
                flattened.append(flattened_param)

        return flattened

    def _openapi_schema_to_json_type(self, schema: Any) -> str:
        """Convert OpenAPI schema to JSON Schema type string for documentation.

        Args:
            schema: OpenAPI schema object (dict or Pydantic model)

        Returns:
            JSON Schema type string (e.g., "string", "array", "integer | null")

        Raises:
            ValueError: If schema is None or invalid
        """
        if schema is None:
            raise ValueError("Schema is None - all parameters and fields should have OpenAPI schemas.")

        # Convert to dict if it's a Pydantic model
        if hasattr(schema, "model_dump"):
            schema = schema.model_dump(exclude_none=True)
        elif not isinstance(schema, dict):
            raise ValueError(
                f"Schema must be a dict or Pydantic model, got {type(schema).__name__}. "
                f"This indicates malformed OpenAPI spec or bug in schema extraction."
            )

        # Handle reference schemas
        if "allOf" in schema:
            # Check if this is a nullable pattern with allOf
            for item in schema["allOf"]:
                if "$ref" in item:
                    ref_name = item["$ref"].split("/")[-1]
                    if ref_name in (self.spec.components.schemas or {}):
                        return "object"
            return "object"

        # Get base type (can be string or list of strings)
        schema_type = schema.get("type")

        # Handle type as array (e.g., ["string", "null"])
        if isinstance(schema_type, list):
            # Filter for known JSON Schema types
            types = [t for t in schema_type if t in self.JSON_SCHEMA_TYPES]
            return " | ".join(types) if types else "any"

        # Handle arrays with items
        if schema_type == "array":
            if "items" in schema:
                items_type = self._openapi_schema_to_json_type(schema["items"])
                return f"array<{items_type}>"
            return "array"

        # Handle enums
        if "enum" in schema:
            enum_values = schema["enum"]
            # Format enum values as union types (e.g., "value1" | "value2")
            # Quote strings, but not numbers/booleans
            formatted_values = []
            for v in enum_values:
                if isinstance(v, str):
                    formatted_values.append(f'"{v}"')
                else:
                    formatted_values.append(str(v))
            return " | ".join(formatted_values)

        # Handle primitives and object - just return the type directly
        if schema_type in self.JSON_SCHEMA_PRIMITIVES or schema_type == "object":
            return schema_type

        # Handle anyOf/oneOf (union types)
        if "anyOf" in schema:
            types = []
            for item in schema["anyOf"]:
                item_type = self._openapi_schema_to_json_type(item)
                if item_type and item_type not in types:
                    types.append(item_type)
            if types:
                return " | ".join(types)

        if "oneOf" in schema:
            types = []
            for item in schema["oneOf"]:
                item_type = self._openapi_schema_to_json_type(item)
                if item_type and item_type not in types:
                    types.append(item_type)
            if types:
                return " | ".join(types)

        # Check for nullable
        nullable = schema.get("nullable", False)

        # Check for $ref
        if "$ref" in schema:
            return "object"

        # Handle schemas with properties but no explicit type
        if "properties" in schema:
            base = "object"
        else:
            # Empty schema {} means "any value is allowed" in OpenAPI 3.0
            # This is valid but rare - log for debugging if needed
            base = "any"

        if nullable:
            return f"{base} | null"

        return base

    def _flatten_response_schema(self, response_type: str, prefix: str = "") -> list[dict]:
        """Flatten response schema fields into dot notation for documentation.

        Args:
            response_type: Response type name (e.g., "Customer", "list[User]")
            prefix: Prefix for nested fields (e.g., "data.")

        Returns:
            Flattened list of fields with dot notation and JSON Schema types
        """
        # Extract base type from wrappers like list[], dict[], etc.
        base_type = response_type
        for wrapper in ["list[", "dict[", "Optional[", "AsyncIterator["]:
            if wrapper in base_type:
                start = base_type.find(wrapper) + len(wrapper)
                end = base_type.rfind("]")
                if end > start:
                    base_type = base_type[start:end].split(",")[-1].strip()
                    break

        # Check if this is an envelope type (e.g., UsersListResult)
        # If so, use the record_type instead
        if hasattr(self, "_envelope_types") and base_type in self._envelope_types:
            envelope = self._envelope_types[base_type]
            record_type = envelope.get("record_type", "dict[str, Any]")
            # Recursively flatten the record type
            return self._flatten_response_schema(record_type, prefix)

        # Skip primitive types and dict[str, Any]
        if base_type in ["str", "int", "float", "bool", "Any", "bytes"]:
            return []
        if "dict[str, Any]" in response_type:
            return []

        # Look up schema in components
        if not self.spec.components or not self.spec.components.schemas:
            return []

        schema = self.spec.components.schemas.get(base_type)
        if not schema:
            return []

        # Extract fields from schema
        flattened = []
        if hasattr(schema, "properties") and schema.properties:
            required = set(schema.required) if hasattr(schema, "required") and schema.required else set()

            for field_name, field_schema in schema.properties.items():
                # Get JSON Schema type for documentation
                field_type = self._openapi_schema_to_json_type(field_schema)
                description = field_schema.description if hasattr(field_schema, "description") else ""

                # Add this field
                flattened.append(
                    {
                        "name": f"{prefix}{field_name}",
                        "type": field_type,
                        "required": field_name in required,
                        "description": description or "",
                    }
                )

                # Check if we should recursively flatten nested objects
                # Look for $ref or object types in the schema
                nested_schema_name = None
                is_array_of_objects = False

                # Convert to dict if needed for easier access
                field_schema_dict = field_schema
                if hasattr(field_schema, "model_dump"):
                    field_schema_dict = field_schema.model_dump(exclude_none=True)

                # Check for direct $ref
                if isinstance(field_schema_dict, dict):
                    if "$ref" in field_schema_dict:
                        nested_schema_name = field_schema_dict["$ref"].split("/")[-1]
                    # Check for array items with $ref
                    elif "items" in field_schema_dict:
                        items = field_schema_dict["items"]
                        if isinstance(items, dict) and "$ref" in items:
                            nested_schema_name = items["$ref"].split("/")[-1]
                            is_array_of_objects = True
                    # Check for anyOf/oneOf with $ref
                    elif "anyOf" in field_schema_dict:
                        for item in field_schema_dict["anyOf"]:
                            if isinstance(item, dict) and "$ref" in item:
                                nested_schema_name = item["$ref"].split("/")[-1]
                                break

                # Recursively flatten if this references a component schema
                if nested_schema_name and nested_schema_name in (self.spec.components.schemas or {}):
                    # For arrays of objects, use [] notation instead of .
                    if is_array_of_objects:
                        nested_fields = self._flatten_response_schema(nested_schema_name, f"{prefix}{field_name}[].")
                    else:
                        nested_fields = self._flatten_response_schema(nested_schema_name, f"{prefix}{field_name}.")
                    flattened.extend(nested_fields)

        return flattened

    def _get_type_names(self) -> list[str]:
        """Get all type names that will be defined in types.py."""
        if not self.spec.components or not self.spec.components.schemas:
            return []
        return list(self.spec.components.schemas.keys())

    def _get_referenced_type_names(self, operations: list) -> list[str]:
        """Get only the parameter type names that are actually referenced in operations.

        This includes ONLY parameter types (TypedDict) used in type annotations.
        Response types (Pydantic models) are imported from models.py via _get_referenced_response_types.
        Excludes Pydantic envelope models which are imported from models.py.
        """
        referenced_types = set()

        # Pydantic envelope models (imported from models.py, not types.py)
        connector_name = self.spec.info.x_airbyte_connector_name
        envelope_prefix = to_pascal_case(connector_name)
        pydantic_envelope_types = {
            f"{envelope_prefix}ExecuteResult",
            f"{envelope_prefix}ExecuteResultWithMeta",
        }

        # Concrete result type aliases (imported from models.py, not types.py)
        concrete_result_types = set()
        for op in operations:
            if op.get("needs_envelope"):
                concrete_result_types.add(self._get_envelope_type_name(op["entity"], Action(op["action"])))

        for op in operations:
            # NOTE: Response types are now imported from models.py, not types.py
            # They are handled by _get_referenced_response_types instead

            # Add params type name (always referenced in overloads)
            params_type = op.get("params_type_name", "")
            if params_type:
                referenced_types.add(params_type)

            # Extract types from parameter type annotations
            for param in op.get("parameters", []):
                param_type = param.get("type", "")
                if param_type:
                    refs = self._extract_type_refs_from_string(param_type)
                    # Filter out Pydantic envelope models and concrete result types
                    refs = refs - pydantic_envelope_types - concrete_result_types
                    referenced_types.update(refs)

        return sorted(list(referenced_types))

    def _get_referenced_response_types(self, operations: list) -> list[str]:
        """Get only the response type names (Pydantic models) referenced in operations.

        These types should be imported from models.py, not types.py.
        Excludes envelope models which are imported separately.
        """
        referenced_types = set()

        # Pydantic envelope models (imported separately)
        connector_name = self.spec.info.x_airbyte_connector_name or "unknown"
        envelope_prefix = to_pascal_case(connector_name)
        pydantic_envelope_types = {
            f"{envelope_prefix}ExecuteResult",
            f"{envelope_prefix}ExecuteResultWithMeta",
        }

        # Concrete result type aliases (imported separately)
        concrete_result_types = set()
        for op in operations:
            if op.get("needs_envelope"):
                concrete_result_types.add(self._get_envelope_type_name(op["entity"], Action(op["action"])))

        for op in operations:
            # Add response type if it's not dict[str, Any]
            response_type = op.get("response_type", "")
            if response_type and response_type != "dict[str, Any]":
                # Extract type refs from response_type (e.g., "list[Customer]" -> "Customer")
                refs = self._extract_type_refs_from_string(response_type)
                # Filter out Pydantic envelope models and concrete result types
                refs = refs - pydantic_envelope_types - concrete_result_types
                referenced_types.update(refs)

            # For envelope operations, also extract types from record_type
            if op.get("needs_envelope"):
                record_type = op.get("record_type", "")
                if record_type and record_type != "dict[str, Any]":
                    refs = self._extract_type_refs_from_string(record_type)
                    referenced_types.update(refs)

        return sorted(list(referenced_types))

    def _get_response_types_used_in_params(self, nested_param_schemas: dict) -> list[str]:
        """Get response type names (Pydantic models) that are referenced by parameter schemas.

        These types need to be imported from models.py in types.py for TYPE_CHECKING.
        """
        if not nested_param_schemas:
            return []

        referenced_types = set()

        # Get all component schema names (response types in models.py)
        component_schema_names = set()
        if self.spec.components and self.spec.components.schemas:
            component_schema_names = set(self.spec.components.schemas.keys())

        # Extract type references from all nested parameter schemas
        for schema_dict in nested_param_schemas.values():
            for field in schema_dict.get("fields", []):
                field_type = field.get("type", "")
                if field_type:
                    refs = self._extract_type_refs_from_string(field_type)
                    # Only include types that are component schemas (response types)
                    refs = refs & component_schema_names
                    referenced_types.update(refs)

        return sorted(list(referenced_types))

    def _extract_type_refs_from_string(self, type_str: str) -> set[str]:
        """Extract type references from a type annotation string.

        Args:
            type_str: Type annotation string (e.g., "list[Customer]", "dict[str, Item]")

        Returns:
            Set of custom type names found in the string (excluding built-in types)
        """
        non_custom_types = PYTHON_BUILTIN_TYPE_NAMES | TYPING_TYPE_NAMES

        refs = set()

        # Simple pattern to extract type names from brackets
        # Matches things like list[Customer], dict[str, Item], Optional[Foo]
        # Find all potential type names (capitalized words not in brackets context)
        type_pattern = re.compile(r"\b([A-Z][a-zA-Z0-9_]*)\b")

        for match in type_pattern.finditer(type_str):
            type_name = match.group(1)
            if type_name not in non_custom_types:
                refs.add(type_name)

        return refs

    def _extract_server_variables(self) -> list[dict]:
        """Extract server variables from OpenAPI servers."""
        variables = []

        if not self.spec.servers:
            return variables

        # Collect all unique server variables across all servers
        seen_variables = set()

        for server in self.spec.servers:
            if server.variables:
                for var_name, var_def in server.variables.items():
                    # Only add each variable once (use first occurrence)
                    if var_name not in seen_variables:
                        seen_variables.add(var_name)
                        variables.append(
                            {
                                "name": var_name,
                                "default": var_def.default,
                                "description": var_def.description or f"Server variable: {var_name}",
                            }
                        )

        return variables

    def _supports_oauth(self) -> bool:
        """Check if this connector supports OAuth2 authentication.

        Returns:
            True if any auth scheme is OAuth2 type, False otherwise.
        """
        auth_config = _parse_auth_from_openapi(self.spec)

        # Check multi-auth mode
        if auth_config.is_multi_auth():
            return any(option.type == AuthType.OAUTH2 for option in (auth_config.options or []))

        # Check single-auth mode
        return auth_config.type == AuthType.OAUTH2

    def _extract_auth_config(self) -> dict[str, Any] | None:
        """Extract x-airbyte-auth-config from security schemes for auth type generation.

        Uses the shared logic from config_loader._parse_auth_from_openapi to ensure
        consistency between runtime and codegen.

        Returns:
            Dict containing auth config metadata for type generation, or None if not found.
            Structure:
            {
                "type_name": "ConnectorNameAuthConfig",
                "options": [  # List of auth options (1 for simple, 2+ for union types)
                    {
                        "title": "...",
                        "fields": [
                            {
                                "name": "field_name",
                                "type": "str",
                                "required": bool,
                                "description": "..."
                            }
                        ]
                    }
                ]
            }
        """
        # Use the shared auth parsing logic (generates defaults when not explicitly defined)
        auth_config = _parse_auth_from_openapi(self.spec)

        # Collect all auth config options
        all_options = []

        # Check if this is multi-auth (new model with options)
        if auth_config.is_multi_auth():
            # Multi-auth: iterate over options
            for option in auth_config.options:
                x_airbyte_auth_config = option.user_config_spec
                if x_airbyte_auth_config is None:
                    continue

                # Extract fields from this auth option
                fields = self._extract_auth_config_fields_from_config(x_airbyte_auth_config)
                title = x_airbyte_auth_config.title or option.scheme_name or "Authentication"
                all_options.append(
                    {
                        "title": title,
                        "description": x_airbyte_auth_config.description or "",
                        "fields": fields,
                        "type_suffix": self._title_to_type_suffix(title),
                        "scheme_name": option.scheme_name,  # Add scheme name for multi-auth
                    }
                )
        else:
            # Single-auth (backwards compatible)
            x_airbyte_auth_config = auth_config.user_config_spec

            if x_airbyte_auth_config is None:
                # No user config spec - skip
                return None

            # Single auth method
            fields = self._extract_auth_config_fields_from_config(x_airbyte_auth_config)
            title = x_airbyte_auth_config.title or "Authentication"
            all_options.append(
                {
                    "title": title,
                    "description": x_airbyte_auth_config.description or "",
                    "fields": fields,
                    "type_suffix": self._title_to_type_suffix(title),
                }
            )

        # If we didn't find any auth configs, return None
        if not all_options:
            return None

        # Generate type name from connector name
        connector_name = self.spec.info.x_airbyte_connector_name or "connector"
        # Convert kebab-case to PascalCase
        parts = connector_name.replace("_", "-").split("-")
        base_name = "".join(word.capitalize() for word in parts)
        type_name = base_name + "AuthConfig"

        # Check if this is multi-auth (multiple security schemes)
        is_multi_auth = auth_config.is_multi_auth()

        return {
            "type_name": type_name,
            "base_name": base_name,
            "options": all_options,
            "is_multi_auth": is_multi_auth,
        }

    def _title_to_type_suffix(self, title: str) -> str:
        """Convert a title string to PascalCase for use as a type suffix.

        Args:
            title: Title string (e.g., "API Token", "Username & Password")

        Returns:
            PascalCase suffix (e.g., "ApiToken", "UsernamePassword")
        """
        # Remove special characters and split into words
        import re

        # Replace &, -, /, ., and other special chars with spaces
        cleaned = re.sub(r"[&\-/.()]+", " ", title)
        # Split on whitespace and filter out empty strings
        words = [word for word in cleaned.split() if word]
        # Convert to PascalCase
        return "".join(word.capitalize() for word in words)

    def _extract_auth_config_fields_from_config(self, config) -> list[dict]:
        """Extract fields from an AuthConfigSpec object.

        Args:
            config: AuthConfigSpec object with properties and required fields

        Returns:
            List of field metadata dicts
        """

        fields = []
        properties = config.properties or {}
        if not properties:
            return fields

        required = set(config.required or [])

        for field_name, field_def in properties.items():
            if field_def is None:
                continue
            field_type = field_def.type or "string"
            # Convert JSON schema types to Python types
            python_type = self.JSON_TO_PYTHON_TYPE_MAP.get(field_type, "str")

            fields.append(
                {
                    "name": field_name,
                    "type": python_type,
                    "required": field_name in required,
                    "title": field_def.title or "",
                    "description": field_def.description or "",
                }
            )

        return fields

    def _extract_oauth_credentials(self) -> dict[str, Any] | None:
        """Extract x-airbyte-oauth-credentials from security schemes for OAuth override type generation.

        Returns:
            Dict containing OAuth credentials metadata for type generation, or None if not found.
            Structure:
            {
                "type_name": "ConnectorNameOAuthCredentials",
                "title": "...",
                "description": "...",
                "fields": [
                    {
                        "name": "field_name",
                        "type": "str",
                        "required": bool,
                        "title": "...",
                        "description": "..."
                    }
                ]
            }
        """
        if not self.spec.components or not self.spec.components.security_schemes:
            return None

        for _scheme_name, scheme in self.spec.components.security_schemes.items():
            if scheme.type != "oauth2":
                continue
            oauth_creds = scheme.x_airbyte_oauth_credentials
            if oauth_creds is None:
                continue

            fields = []
            properties = oauth_creds.properties or {}
            required = set(oauth_creds.required or [])

            for field_name, field_def in properties.items():
                field_type = field_def.type or "string"
                python_type = self.JSON_TO_PYTHON_TYPE_MAP.get(field_type, "str")
                fields.append(
                    {
                        "name": field_name,
                        "type": python_type,
                        "required": field_name in required,
                        "title": field_def.title or "",
                        "description": field_def.description or "",
                    }
                )

            connector_name = self.spec.info.x_airbyte_connector_name or "Connector"
            type_name = f"{to_pascal_case(connector_name)}OAuthCredentials"

            return {
                "type_name": type_name,
                "title": oauth_creds.title or "OAuth App Credentials",
                "description": oauth_creds.description or "",
                "fields": fields,
            }

        return None

    def _extract_replication_config(self) -> dict[str, Any] | None:
        """Extract x-airbyte-replication-config from the spec for type generation.

        This extension defines replication-specific settings for MULTI mode connectors
        that need to configure the underlying replication connector. It allows users
        who use the direct-style API (credentials + environment) to also specify
        replication settings like start_date, lookback_window, etc.

        Returns:
            Dict containing replication config metadata for type generation, or None if not found.
            Structure:
            {
                "type_name": "ConnectorNameReplicationConfig",
                "title": "Replication Configuration",
                "description": "...",
                "fields": [
                    {
                        "name": "field_name",
                        "type": "str",
                        "required": bool,
                        "title": "...",
                        "description": "...",
                        "format": "date-time" | None,
                        "default": ... | None
                    }
                ]
            }
        """
        replication_config = self.spec.info.x_airbyte_replication_config
        if replication_config is None:
            return None

        fields = []
        properties = replication_config.properties or {}
        if not properties:
            return None

        required = set(replication_config.required or [])

        for field_name, field_def in properties.items():
            field_type = field_def.type or "string"
            # Convert JSON schema types to Python types
            python_type = self.JSON_TO_PYTHON_TYPE_MAP.get(field_type, "str")

            fields.append(
                {
                    "name": field_name,
                    "type": python_type,
                    "required": field_name in required,
                    "title": field_def.title or field_name,
                    "description": field_def.description or "",
                    "format": field_def.format,
                    "default": field_def.default,
                }
            )

        connector_name = self.spec.info.x_airbyte_connector_name or "Connector"
        type_name = f"{to_pascal_case(connector_name)}ReplicationConfig"

        return {
            "type_name": type_name,
            "title": replication_config.title or "Replication Configuration",
            "description": replication_config.description or "",
            "fields": fields,
        }
