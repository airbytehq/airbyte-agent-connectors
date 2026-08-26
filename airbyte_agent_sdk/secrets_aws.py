"""AWS Secrets Manager hydration for executable bundles (opt-in `secrets-aws` extra).

This module is only reached on the opt-in local execution path -- when
`SECRETS_CONFIGURED_FROM_ENVIRONMENT=true`, the SDK calls
`POST /connectors/{id}/execute/prepare` and resolves the returned bundle's
unhydrated `secret_coordinate::` values against the customer's own AWS Secrets
Manager in their data plane. `boto3` is imported lazily inside
`hydrate_source_config` so the base install (without the `secrets-aws`
extra) never imports boto3 on the hosted path.
"""

from __future__ import annotations

import json
from typing import Any

from airbyte_agent_sdk.config import AWSDataPlaneCredentials, resolve_aws_credentials

_SECRET_COORDINATE_PREFIX = "secret_coordinate::"

_INSTALL_HINT = "Install it with: pip install airbyte-agent-sdk[secrets-aws]"
_AWS_HINT = (
    "Local executable-bundle hydration currently supports AWS and GCP secret managers. "
    "Verify your AWS secret store configuration "
    "(AWS_SECRET_MANAGER_ACCESS_KEY_ID / AWS_SECRET_MANAGER_SECRET_ACCESS_KEY, "
    "optional AWS_SECRET_MANAGER_SESSION_TOKEN, and AWS_SECRET_MANAGER_REGION) "
    "and verify the secret coordinate exists in that AWS account and region. "
    "Execution was NOT sent to Airbyte Cloud."
)


def _is_secret_coordinate(value: Any) -> bool:
    return isinstance(value, str) and value.startswith(_SECRET_COORDINATE_PREFIX)


def _coordinate_secret_id(value: str) -> str:
    """Strip the `secret_coordinate::` prefix to get the AWS SM secret id."""
    return value.split("::", 1)[1]


def hydrate_source_config(
    source_config: dict[str, Any],
    *,
    credentials: AWSDataPlaneCredentials | None = None,
) -> dict[str, Any]:
    """Resolve `secret_coordinate::` values in *source_config* via AWS Secrets Manager.

    Walks nested dicts/lists and replaces every `secret_coordinate::<id>` string
    with the secret value fetched from AWS Secrets Manager, returning a fully
    hydrated config. Fails closed: any credential or fetch failure raises rather
    than falling back to hosted execution.

    Raises:
        ImportError: If boto3 is not installed (missing `secrets-aws` extra).
        ValueError: If AWS credentials are absent or a coordinate cannot be resolved.
    """
    credentials = credentials or resolve_aws_credentials()
    client = _build_secrets_manager_client(credentials)
    resolved_cache: dict[str, str] = {}

    def _resolve(value: Any) -> Any:
        if isinstance(value, dict):
            return {key: _resolve(inner) for key, inner in value.items()}
        if isinstance(value, list):
            return [_resolve(item) for item in value]
        if _is_secret_coordinate(value):
            secret_id = _coordinate_secret_id(value)
            if secret_id not in resolved_cache:
                resolved_cache[secret_id] = _fetch_secret(client, secret_id)
            return resolved_cache[secret_id]
        return value

    return _resolve(source_config)


def _build_secrets_manager_client(credentials: AWSDataPlaneCredentials) -> Any:
    # boto3 is an opt-in dependency (airbyte-agent-sdk[secrets-aws]) needed only on
    # the local hydration path, so it is imported lazily here to keep it off the
    # hosted execution path and out of the base install.
    try:
        import boto3
    except ImportError as exc:
        raise ImportError(f"boto3 is required to hydrate executable bundles from AWS Secrets Manager. {_INSTALL_HINT}") from exc

    client_kwargs: dict[str, Any] = {}
    if credentials.region_name:
        client_kwargs["region_name"] = credentials.region_name
    if credentials.has_explicit_keys:
        client_kwargs["aws_access_key_id"] = credentials.access_key_id
        client_kwargs["aws_secret_access_key"] = credentials.secret_access_key
        if credentials.session_token:
            client_kwargs["aws_session_token"] = credentials.session_token

    return boto3.client("secretsmanager", **client_kwargs)


def _fetch_secret(client: Any, secret_id: str) -> str:
    # botocore ships with boto3; import its exception types lazily alongside the
    # lazy boto3 client so the base install never needs botocore.
    from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

    try:
        response = client.get_secret_value(SecretId=secret_id)
    except NoCredentialsError as exc:
        raise ValueError(
            "AWS credentials are required to hydrate the executable bundle in your data plane, " f"but none were found. {_AWS_HINT}"
        ) from exc
    except ClientError as exc:
        error_code = exc.response.get("Error", {}).get("Code")
        if error_code == "ResourceNotFoundException":
            raise ValueError(f"Secret coordinate '{secret_id}' was not found in AWS Secrets Manager. {_AWS_HINT}") from exc
        raise ValueError(f"Failed to resolve secret coordinate '{secret_id}' from AWS Secrets Manager. {_AWS_HINT} Details: {exc}") from exc
    except BotoCoreError as exc:
        raise ValueError(f"AWS Secrets Manager request failed while resolving '{secret_id}': {exc}") from exc

    secret_string = response.get("SecretString")
    if secret_string is None:
        raise ValueError(
            f"Secret coordinate '{secret_id}' resolved to a binary AWS Secrets Manager value. "
            "Store the connector credential as a plaintext SecretString."
        )

    try:
        parsed = json.loads(secret_string)
    except json.JSONDecodeError:
        return secret_string

    if isinstance(parsed, dict | list):
        raise ValueError(
            f"Secret coordinate '{secret_id}' resolved to a JSON AWS Secrets Manager value. "
            "Store the connector credential as a plaintext SecretString, not a JSON object."
        )
    return secret_string
