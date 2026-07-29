"""
Cassette generator for creating test specifications from logged HTTP interactions.

This module provides utilities to transform logged HTTP requests/responses
into YAML-based test specifications (cassettes) for connector testing.
"""

import base64
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List
from urllib.parse import parse_qs, urlparse

import yaml
from pydantic import SecretStr

from airbyte_agent_sdk.logging.types import LogSession, RequestLog
from airbyte_agent_sdk.observability.redactor import DataRedactor
from airbyte_agent_sdk.secrets import get_secret_values
from airbyte_agent_sdk.testing.models import (
    CapturedRequest,
    CapturedResponse,
    TestInputs,
    TestSpec,
    ValidationConfig,
)


def _redact_body_aggressive(body: Any) -> Any:
    """Redact secrets from a request or response body with aggressive mode.

    - dict/list: recursive key-name + value-shape redaction.
    - str: value-shape redaction.
    - bytes / binary wrapper: pass through unchanged.
    """
    if isinstance(body, dict):
        if body.get("_binary"):
            return body
        return DataRedactor.redact_mapping(body, aggressive=True)
    if isinstance(body, list):
        return DataRedactor.redact_mapping({"_list": body}, aggressive=True)["_list"]
    if isinstance(body, str):
        return DataRedactor.redact_string(body, aggressive=True)
    return body


class CassetteGenerator:
    """Generates test cassettes from logged HTTP interactions."""

    def __init__(self, log_session: LogSession):
        """Initialize generator with a log session.

        Args:
            log_session: LogSession containing captured HTTP interactions
        """
        self.log_session = log_session

    @classmethod
    def from_log_file(cls, log_file_path: str) -> "CassetteGenerator":
        """Create generator from a log file.

        Args:
            log_file_path: Path to JSON log file

        Returns:
            CassetteGenerator instance

        Raises:
            FileNotFoundError: If log file doesn't exist
            ValueError: If log file is invalid JSON or doesn't match LogSession schema
        """
        log_path = Path(log_file_path)
        if not log_path.exists():
            raise FileNotFoundError(f"Log file not found: {log_file_path}")

        with open(log_path) as f:
            data = json.load(f)

        try:
            log_session = LogSession(**data)
        except Exception as e:
            raise ValueError(f"Invalid log session format: {e}")

        return cls(log_session)

    @staticmethod
    def _validate_no_hardcoded_secrets(
        secrets: Dict[str, str] | None,
        server_variable_names: set[str] | None = None,
    ) -> None:
        """Validate that secrets use environment variable references, not hardcoded values.

        This prevents accidentally committing real API keys or secrets to version control.
        All secret values must use the ${ENV_VAR_NAME} syntax for environment variable
        substitution.

        Args:
            secrets: Dict of secret names to values
            server_variable_names: Set of server variable names from OpenAPI spec.
                These are non-sensitive config values (e.g., subdomain) that don't
                require ${} syntax.

        Raises:
            ValueError: If any secret appears to be hardcoded (not using ${} syntax)

        Example:
            Valid:   {"token": "${STRIPE_API_KEY}"}
            Invalid: {"token": "sk_test_abc123..."}
        """
        if not secrets:
            return

        server_variable_names = server_variable_names or set()

        for key, value in secrets.items():
            # Skip validation for server variables (non-sensitive config values)
            if key in server_variable_names:
                continue

            # Check if value uses environment variable syntax
            if not (value.startswith("${") and value.endswith("}")):
                # Redact the value in error message for security
                redacted_value = value[:10] + "..." if len(value) > 10 else "[REDACTED]"
                raise ValueError(
                    f"Secret '{key}' appears to be hardcoded (value: {redacted_value}).\n"
                    f"Secrets must use environment variable syntax to prevent accidental exposure.\n"
                    f"Expected format: ${{ENV_VAR_NAME}}\n"
                    f"Example: {{'token': '${{STRIPE_API_KEY}}'}}\n\n"
                    f"This validation prevents secrets from being committed to version control."
                )

    def _extract_captured_request(self, request_log: RequestLog) -> CapturedRequest:
        # Extract query params from URL or params dict
        query_params = self._extract_query_params(request_log)

        # Filter headers (remove auth headers)
        filtered_headers = self._filter_headers(request_log.headers)

        # Redact secrets in all serialized fields (aggressive mode).
        redacted_path = "/".join(DataRedactor.redact_string(segment, aggressive=True) for segment in request_log.path.split("/"))
        redacted_query_params = DataRedactor.redact_mapping(query_params, aggressive=True) if query_params else None
        redacted_body = _redact_body_aggressive(request_log.body) if request_log.body is not None else None

        # Build captured request
        return CapturedRequest(
            method=request_log.method,
            path=redacted_path,
            query_params=redacted_query_params if redacted_query_params else None,
            headers=filtered_headers,
            body=redacted_body,
            validation=ValidationConfig(),
        )

    def _extract_captured_response(self, request_log: RequestLog) -> CapturedResponse:
        # Use captured response headers if available, fall back to empty dict for backward compatibility
        response_headers = getattr(request_log, "response_headers", None) or {}

        # Redact response header values (keep keys, scrub values)
        redacted_response_headers = DataRedactor.redact_headers(response_headers)
        # Redact response body
        redacted_body = _redact_body_aggressive(request_log.response_body) if request_log.response_body is not None else None

        return CapturedResponse(
            status_code=request_log.response_status,
            headers=redacted_response_headers,
            body=redacted_body,
        )

    def generate_test_spec(
        self,
        request_log: RequestLog,
        entity: str,
        action: str,
        params: Dict[str, Any] | None = None,
        test_name: str | None = None,
        description: str | None = None,
        auth_config: Dict[str, str] | None = None,
        server_variable_names: set[str] | None = None,
        file_log: RequestLog | None = None,
    ) -> TestSpec:
        """Generate test specifications.

        Args:
            request_log: The logged HTTP interaction to convert
            file_log: The logged file download HTTP interaction
            entity: Entity name (e.g., 'customers')
            action: Operation action (e.g., 'list', 'get')
            params: Optional dict of original params passed to execute()
            test_name: Optional custom test name (auto-generated if not provided)
            description: Optional test description
            auth_config: Dict of user-facing auth config to environment variable references
                     (e.g., {"api_key": "${STRIPE_API_KEY}"})
            server_variable_names: Optional set of server variable names from OpenAPI spec.
                These are non-sensitive config values that don't require ${} syntax.

        Returns:
            TestSpec instance ready to be saved as YAML

        Raises:
            ValueError: If request_log is missing required fields
        """
        if not request_log.response_status:
            raise ValueError("Request log must have a response status")

        # Generate test name if not provided
        if not test_name:
            params_suffix = ""
            if params:
                key_params = ["limit", "id", "starting_after", "ending_before"]
                relevant_params = {k: v for k, v in params.items() if k in key_params}
                if relevant_params:
                    params_suffix = "_" + "_".join(f"{k}_{v}" for k, v in relevant_params.items())
            test_name = f"{entity}_{action}{params_suffix}"

        # Generate description if not provided
        if not description:
            description = f"Captured from real API call on {datetime.now().strftime('%Y-%m-%d')}"

        # Build captured request
        captured_request = self._extract_captured_request(request_log)

        # Build captured response
        captured_response = self._extract_captured_response(request_log)

        # Handle file downloads logs
        captured_file_request = None
        captured_file_response = None
        if file_log:
            if not file_log.response_status:
                raise ValueError("File request log must have a response status")

            if not self.log_session.chunk_logs:
                raise ValueError("No chunk data captured for download operation. Ensure the download was executed and chunks were logged.")

            # Join all chunks into one file body
            file_body = b"".join(self.log_session.chunk_logs)

            # Store binary content as base64
            file_body = {
                "_binary": True,
                "_base64": base64.b64encode(file_body).decode("utf-8"),
            }

            captured_file_request = self._extract_captured_request(file_log)
            captured_file_request.validation = ValidationConfig(
                query_params_strict=False,
                headers_strict=False,
            )

            captured_file_response = self._extract_captured_response(file_log)
            captured_file_response.body = file_body

        # Build inputs from merged params (path + query/body params)
        inputs = TestInputs(params=params or {})

        # Validate secrets before converting (prevents hardcoded secrets in cassettes)
        self._validate_no_hardcoded_secrets(auth_config, server_variable_names)

        # Convert auth_config to SecretStr for TestSpec
        auth_config_dict: Dict[str, SecretStr] = {}
        if auth_config:
            for key, value in auth_config.items():
                auth_config_dict[key] = SecretStr(value)

        return TestSpec(
            test_name=test_name,
            description=description,
            entity=entity,
            action=action,
            auth_config=auth_config_dict,
            inputs=inputs,
            captured_request=captured_request,
            captured_response=captured_response,
            captured_file_request=captured_file_request,
            captured_file_response=captured_file_response,
        )

    def save_yaml(
        self,
        test_spec: TestSpec,
        output_dir: str,
        filename: str | None = None,
    ) -> Path:
        """Save test spec as YAML file.

        Args:
            test_spec: TestSpec to save
            output_dir: Directory to save the YAML file
            filename: Optional filename (auto-generated if not provided)

        Returns:
            Path to the saved file
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        if not filename:
            # Generate filename from test spec
            # Note: Use only word characters (no hyphens) to ensure the filename
            # can be used as a valid Python identifier for test function names
            safe_name = re.sub(r"[^\w]", "_", test_spec.test_name.lower())
            filename = f"{safe_name}.yaml"

        file_path = output_path / filename

        # Convert to dict and handle SecretStr serialization
        spec_dict = test_spec.model_dump(mode="json")

        # Convert SecretStr values to their actual values for YAML output
        # (they contain environment variable references like "${STRIPE_API_KEY}")
        if "auth_config" in spec_dict and test_spec.auth_config:
            spec_dict["auth_config"] = get_secret_values(test_spec.auth_config)

        # Write YAML with nice formatting
        with open(file_path, "w") as f:
            yaml.dump(
                spec_dict,
                f,
                default_flow_style=False,
                sort_keys=False,
                allow_unicode=True,
            )

        return file_path

    @staticmethod
    def effective_endpoint_path(endpoint: Any) -> str:
        """Get the effective path template for an endpoint.

        For endpoints with x-airbyte-path-override, the actual HTTP request
        uses the override path, not the original endpoint path.

        Args:
            endpoint: EndpointDefinition with path and optional path_override

        Returns:
            The path template to use for parameter extraction
        """
        # Check if endpoint has path_override with a path
        if hasattr(endpoint, "path_override") and endpoint.path_override and hasattr(endpoint.path_override, "path") and endpoint.path_override.path:
            return endpoint.path_override.path
        return endpoint.path

    @staticmethod
    def _extract_path_param_values(template_path: str, actual_path: str) -> Dict[str, str]:
        """Extract path parameter values by matching actual path against template.

        Args:
            template_path: Path template with {param} placeholders (e.g., '/v1/customers/{id}')
            actual_path: Actual path from request (e.g., '/v1/customers/cus_123')

        Returns:
            Dictionary of parameter names to their values (e.g., {'id': 'cus_123'})

        Example:
            >>> CassetteGenerator._extract_path_param_values(
            ...     '/v1/customers/{id}',
            ...     '/v1/customers/cus_123'
            ... )
            {'id': 'cus_123'}
        """
        # Convert template path to regex pattern with named groups
        # /v1/customers/{id} -> /v1/customers/(?P<id>[^/]+)
        pattern = template_path

        # Find all {param} placeholders
        param_names = re.findall(r"\{(\w+)\}", template_path)

        # Replace each {param} with a named regex group that matches non-slash characters
        for param_name in param_names:
            pattern = pattern.replace(f"{{{param_name}}}", f"(?P<{param_name}>[^/]+)")

        # Escape any regex special characters in the static parts of the path
        # But preserve our named groups
        # This is already handled by replacing the exact strings

        # Match the actual path against the pattern
        match = re.match(f"^{pattern}$", actual_path)

        if not match:
            # If no match, return empty dict (paths don't match template)
            return {}

        # Extract all named groups
        return match.groupdict()

    def _extract_query_params(self, request_log: RequestLog) -> Dict[str, str]:
        """Extract query parameters from request log.

        Args:
            request_log: The request log to extract params from

        Returns:
            Dictionary of query parameters as strings
        """
        if urlparse(request_log.path).query:
            return {}

        # First check if params dict is provided
        if request_log.params:
            # Convert all values to strings (API expects strings)
            return {k: str(v) for k, v in request_log.params.items()}

        # Otherwise parse from URL
        parsed_url = urlparse(request_log.url)
        if parsed_url.query:
            params_dict = parse_qs(parsed_url.query)
            # parse_qs returns lists, take first value and convert to string
            return {k: str(v[0]) for k, v in params_dict.items()}

        return {}

    def _filter_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        """Remove authentication headers from captured request.

        Auth headers are dropped entirely (not redacted in place) — this is
        load-bearing for request-validation tests and the cassette contract.
        Non-auth header *values* are scrubbed with aggressive value-shape
        detection.

        Args:
            headers: Original headers dict

        Returns:
            Filtered headers dict without auth headers
        """
        filtered = {}
        for key, value in headers.items():
            key_lower = key.lower()
            # Skip auth headers (using canonical deny-list)
            if any(pattern in key_lower for pattern in DataRedactor.SENSITIVE_HEADER_PATTERNS):
                continue
            # Skip already redacted headers
            if value == "[REDACTED]":
                continue
            # Scrub non-auth header values for secret shapes
            filtered[key] = DataRedactor.redact_value(value, aggressive=True)

        return filtered

    def list_logs(self) -> List[Dict[str, Any]]:
        """List all logs in the session with summary info.

        Returns:
            List of dicts with log summaries for user selection
        """
        summaries = []
        for idx, log in enumerate(self.log_session.logs):
            summaries.append(
                {
                    "index": idx,
                    "method": log.method,
                    "path": log.path,
                    "status": log.response_status,
                    "params": log.params,
                    "timestamp": log.timestamp.isoformat(),
                }
            )
        return summaries
