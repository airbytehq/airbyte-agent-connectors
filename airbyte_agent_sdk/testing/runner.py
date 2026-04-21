"""
Test runner for executing connector test specifications.

Runs tests in mock mode using HTTP layer interception.
"""

import asyncio
import base64
import time
from pathlib import Path
from typing import Dict, List
from unittest.mock import AsyncMock, Mock, patch

from airbyte_agent_sdk.secrets import SecretStr

from ..executor import ExecutionConfig, LocalExecutor
from ..types import Action
from .models import CapturedRequest, RequestMismatch, TestReport, TestResult, TestSpec
from .spec_loader import load_test_spec, load_test_specs
from .validator import RequestValidator


class TestRunner:
    """
    Executes connector test specifications in mock mode.

    This runner loads test specs, sets up HTTP mocks, executes tests
    using the LocalExecutor, and collects results.
    """

    def __init__(
        self,
        connector_path: Path,
        auth_config: Dict[str, SecretStr] | None = None,
        config_values: Dict[str, str] | None = None,
        verbose: bool = False,
    ):
        """
        Initialize test runner.

        Args:
            connector_path: Path to connector.yaml
            auth_config: Optional dict of user-facing auth config (applies mapping)
            config_values: Optional dict of config values for server variable substitution
                (e.g., {"subdomain": "acme"} for URLs like https://{subdomain}.api.example.com)
            verbose: Enable verbose output
        """
        self.connector_path = Path(connector_path)
        self.auth_config = auth_config
        self.config_values = config_values or {}
        self.verbose = verbose
        self.results: List[TestResult] = []
        self.validator = RequestValidator()

    async def run_tests(self, test_dir: Path | None = None, test_files: List[Path] | None = None) -> TestReport:
        """
        Run all test specifications.

        Args:
            test_dir: Directory containing test specs (if not provided, uses connector_path/tests/verified)
            test_files: Specific test files to run (overrides test_dir)

        Returns:
            TestReport with results and summary
        """
        start_time = time.time()

        # Determine test location
        if test_files:
            specs = []
            for file_path in test_files:
                spec = load_test_spec(Path(file_path), auth_config=self.auth_config)
                specs.append(spec)
        else:
            if test_dir is None:
                # Default: connector_path/tests/verified
                test_dir = self.connector_path.parent / "tests" / "verified"

            specs = load_test_specs(test_dir, auth_config=self.auth_config)

        if not specs:
            raise ValueError(f"No test specs found in {test_dir}")

        # Run tests in mock mode
        await self._run_mock_tests(specs)

        # Calculate total duration
        total_duration = (time.time() - start_time) * 1000  # Convert to ms

        # Create report
        report = TestReport(
            connector_path=str(self.connector_path),
            mode="mock",
            total_duration_ms=total_duration,
            results=self.results,
        )

        return report

    async def _run_mock_tests(self, specs: List[TestSpec]) -> None:
        """
        Run tests in mock mode with HTTP interception.

        Args:
            specs: List of test specifications to execute
        """
        # Run each test with its own executor (each test has its own auth config)
        for spec in specs:
            # Determine which credentials to use
            # Priority: spec.auth_config > self.auth_config
            test_auth_config = spec.auth_config if spec.auth_config else self.auth_config

            executor = LocalExecutor(
                config_path=str(self.connector_path),
                auth_config=test_auth_config,
                auth_scheme=spec.auth_scheme,
                config_values=self.config_values,
                enable_logging=self.verbose,
            )

            try:
                result = await self._run_single_test_with_mock(spec, executor)
                self.results.append(result)
                if self.verbose:
                    status_symbol = "✓" if result.status == "passed" else "✗"
                    print(f"  {status_symbol} {result.test_name} ({result.duration_ms:.1f}ms)")
            finally:
                await executor.close()

    async def _run_single_test_with_mock(self, spec: TestSpec, executor: LocalExecutor) -> TestResult:
        """
        Run a single test with mocked HTTP response.

        Args:
            spec: Test specification
            executor: LocalExecutor instance

        Returns:
            TestResult with execution outcome
        """
        # Check if this is a download test with file request
        is_download = spec.action.lower() == "download" and spec.captured_file_request is not None

        if is_download:
            return await self._run_download_test_with_mock(spec, executor)
        else:
            return await self._run_standard_test_with_mock(spec, executor)

    async def _run_standard_test_with_mock(self, spec: TestSpec, executor: LocalExecutor) -> TestResult:
        """Run a standard (non-download) test with mocked HTTP response."""
        start_time = time.time()

        # Variable to capture the actual request made
        captured_actual_request = None

        # Create mock response based on captured_response
        mock_response = Mock()
        mock_response.status_code = spec.captured_response.status_code
        mock_response.headers = spec.captured_response.headers
        mock_response.json.return_value = spec.captured_response.body
        mock_response.raise_for_status.return_value = None

        # Create async mock for HTTPClient.request that captures the actual request
        async def mock_http_client_request(method, path, params=None, json=None, data=None, headers=None, content=None):  # noqa: ARG001
            nonlocal captured_actual_request

            # Capture the actual request details from HTTPClient.request parameters
            # These are the actual values before they go to httpx
            captured_actual_request = CapturedRequest(
                method=method,
                path=path,
                query_params={k: str(v) for k, v in params.items()} if params else None,
                headers=headers or {},
                body=json or data,
            )

            return (mock_response.json.return_value, dict(mock_response.headers))

        mock_request = AsyncMock(side_effect=mock_http_client_request)

        try:
            # Patch the HTTPClient's request method (not the httpx client)
            with patch.object(executor.http_client, "request", mock_request):
                # Convert action string to Action enum (lowercase)
                action = Action(spec.action.lower())

                # Create execution config
                config = ExecutionConfig(entity=spec.entity, action=action, params=spec.inputs.params)

                # Execute the operation
                await executor.execute(config)

                duration_ms = (time.time() - start_time) * 1000

                # Phase 2: Validate the actual request against expected request
                mismatches = []
                if captured_actual_request:
                    mismatches = self.validator.validate_request(expected=spec.captured_request, actual=captured_actual_request)

                # Determine test status based on validation results
                if mismatches:
                    status = "failed"
                    error_message = f"Request validation failed with {len(mismatches)} mismatch(es)"
                else:
                    status = "passed"
                    error_message = None

                return TestResult(
                    test_name=spec.test_name,
                    entity=spec.entity,
                    action=spec.action,
                    status=status,
                    duration_ms=duration_ms,
                    error_message=error_message,
                    mismatches=mismatches,
                )

        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000

            return TestResult(
                test_name=spec.test_name,
                entity=spec.entity,
                action=spec.action,
                status="error",
                duration_ms=duration_ms,
                error_message=str(e),
            )

    async def _run_download_test_with_mock(self, spec: TestSpec, executor: LocalExecutor) -> TestResult:
        """Run a download test with mocked HTTP responses for both metadata and file."""
        start_time = time.time()

        # Variables to capture actual requests
        captured_metadata_request = None
        captured_file_request = None

        # Get file response body - decode from base64 if needed
        file_body = spec.captured_file_response.body if spec.captured_file_response else b""
        if isinstance(file_body, dict) and file_body.get("_binary"):
            file_body = base64.b64decode(file_body["_base64"])
        elif not isinstance(file_body, bytes):
            # Convert to bytes if it's a string or other type
            file_body = str(file_body).encode("utf-8") if file_body else b""

        # Create mock for file download response (raw response)
        mock_file_response = Mock()
        mock_file_response.status_code = spec.captured_file_response.status_code if spec.captured_file_response else 200
        mock_file_response.headers = {}
        mock_file_response.raise_for_status.return_value = None

        async def mock_aiter_bytes(chunk_size=None):  # noqa: ARG001
            yield file_body

        mock_file_response.aiter_bytes = mock_aiter_bytes

        # Create mock that returns different values based on stream parameter
        call_count = 0

        async def mock_request_with_stream(  # noqa: ARG001
            method,
            path,
            params=None,
            json=None,
            data=None,
            headers=None,
            content=None,  # noqa: ARG001
            stream=False,
        ):
            nonlocal call_count, captured_metadata_request, captured_file_request
            call_count += 1

            # Use stream parameter to decide what to return (not just call count)
            # This handles both 2-step downloads and direct downloads
            if stream:
                # Streaming request: file download
                captured_file_request = CapturedRequest(
                    method=method,
                    path=path,
                    query_params={k: str(v) for k, v in params.items()} if params else None,
                    headers=headers or {},
                    body=None,
                )
                return (mock_file_response, {})
            else:
                # Non-streaming request: metadata request
                captured_metadata_request = CapturedRequest(
                    method=method,
                    path=path,
                    query_params={k: str(v) for k, v in params.items()} if params else None,
                    headers=headers or {},
                    body=json or data,
                )
                return (spec.captured_response.body, dict(spec.captured_response.headers))

        try:
            # Patch request method
            with patch.object(executor.http_client, "request", mock_request_with_stream):
                # Convert action string to Action enum
                action = Action(spec.action.lower())

                # Execute the download operation
                config = ExecutionConfig(entity=spec.entity, action=action, params=spec.inputs.params)
                result = await executor.execute(config)

                # Consume the async iterator to trigger all requests
                chunks = []
                async for chunk in result.data:
                    chunks.append(chunk)

                duration_ms = (time.time() - start_time) * 1000

                # Validate both requests
                mismatches = []

                # Validate metadata request
                if captured_metadata_request:
                    metadata_mismatches = self.validator.validate_request(
                        expected=spec.captured_request,
                        actual=captured_metadata_request,
                    )
                    for m in metadata_mismatches:
                        m.field = f"metadata.{m.field}"
                    mismatches.extend(metadata_mismatches)

                # Validate file request (less strict)
                if captured_file_request and spec.captured_file_request:
                    # For file requests, just check the method
                    if captured_file_request.method != spec.captured_file_request.method:
                        mismatches.append(
                            RequestMismatch(
                                field="file.method",
                                expected=spec.captured_file_request.method,
                                actual=captured_file_request.method,
                                description="File download method mismatch",
                            )
                        )

                # Determine test status
                if mismatches:
                    status = "failed"
                    error_message = f"Request validation failed with {len(mismatches)} mismatch(es)"
                else:
                    status = "passed"
                    error_message = None

                return TestResult(
                    test_name=spec.test_name,
                    entity=spec.entity,
                    action=spec.action,
                    duration_ms=duration_ms,
                    status=status,
                    mismatches=mismatches,
                    error_message=error_message,
                )

        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000

            return TestResult(
                test_name=spec.test_name,
                entity=spec.entity,
                action=spec.action,
                status="error",
                duration_ms=duration_ms,
                error_message=str(e),
            )


async def run_tests_async(
    connector_path: Path,
    test_dir: Path | None = None,
    test_files: List[Path] | None = None,
    auth_config: Dict[str, SecretStr] | None = None,
    verbose: bool = False,
) -> TestReport:
    """
    Async convenience function to run tests.

    Args:
        connector_path: Path to connector.yaml
        test_dir: Directory containing test specs
        test_files: Specific test files to run
        auth_config: Optional user-facing auth config dict
        verbose: Enable verbose output

    Returns:
        TestReport with results
    """
    runner = TestRunner(connector_path, auth_config=auth_config, verbose=verbose)
    return await runner.run_tests(test_dir=test_dir, test_files=test_files)


def run_tests(
    connector_path: Path,
    test_dir: Path | None = None,
    test_files: List[Path] | None = None,
    auth_config: Dict[str, SecretStr] | None = None,
    verbose: bool = False,
) -> TestReport:
    """
    Synchronous convenience function to run tests.

    Args:
        connector_path: Path to connector.yaml
        test_dir: Directory containing test specs
        test_files: Specific test files to run
        auth_config: Optional user-facing auth config dict
        verbose: Enable verbose output

    Returns:
        TestReport with results
    """
    return asyncio.run(
        run_tests_async(
            connector_path,
            test_dir,
            test_files,
            auth_config=auth_config,
            verbose=verbose,
        )
    )
