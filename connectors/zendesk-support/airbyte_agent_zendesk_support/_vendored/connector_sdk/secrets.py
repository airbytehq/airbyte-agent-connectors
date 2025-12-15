"""Secret handling utilities for the Airbyte SDK.

This module provides utilities for handling sensitive data like API keys, tokens,
and passwords. It uses Pydantic's SecretStr to ensure secrets are obfuscated in
logs, error messages, and string representations.

Example:
    >>> from .secrets import SecretStr
    >>> api_key = SecretStr("my-secret-key")
    >>> print(api_key)  # Outputs: **********
    >>> print(repr(api_key))  # Outputs: SecretStr('**********')
    >>> api_key.get_secret_value()  # Returns: 'my-secret-key'
"""

import os
import re
from typing import Any, Dict, Optional

from pydantic import SecretStr

__all__ = [
    "SecretStr",
    "convert_to_secret_dict",
    "get_secret_values",
    "resolve_env_var_references",
]


def convert_to_secret_dict(secrets: Dict[str, str]) -> Dict[str, SecretStr]:
    """Convert a dictionary of plain string secrets to SecretStr values.

    Args:
        secrets: Dictionary with string keys and plain string secret values

    Returns:
        Dictionary with string keys and SecretStr values

    Example:
        >>> plain_secrets = {"api_key": "secret123", "token": "token456"}
        >>> secret_dict = convert_to_secret_dict(plain_secrets)
        >>> print(secret_dict["api_key"])  # Outputs: **********
    """
    return {key: SecretStr(value) for key, value in secrets.items()}


def get_secret_values(secrets: Dict[str, SecretStr]) -> Dict[str, str]:
    """Extract plain string values from a dictionary of SecretStr values.

    Args:
        secrets: Dictionary with string keys and SecretStr values

    Returns:
        Dictionary with string keys and plain string values

    Warning:
        Use with caution. This exposes the actual secret values.

    Example:
        >>> secret_dict = {"api_key": SecretStr("secret123")}
        >>> plain_dict = get_secret_values(secret_dict)
        >>> print(plain_dict["api_key"])  # Outputs: secret123
    """
    return {key: value.get_secret_value() for key, value in secrets.items()}


class SecretResolutionError(Exception):
    """Raised when environment variable resolution fails."""

    pass


def resolve_env_var_references(
    secret_mappings: Dict[str, Any],
    strict: bool = True,
    env_vars: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    """Resolve environment variable references in secret values.

    This function processes a dictionary of secret mappings and resolves any
    environment variable references using the ${ENV_VAR_NAME} syntax. All
    environment variable references in the values will be replaced with their
    actual values from the provided environment variable map or os.environ.

    Args:
        secret_mappings: Dictionary mapping secret keys to values that may contain
                        environment variable references (e.g., {"token": "${API_KEY}"})
        strict: If True, raises SecretResolutionError when a referenced environment
               variable is not found. If False, leaves unresolved references as-is.
        env_vars: Optional dictionary of environment variables to use for resolution.
                 If None, uses os.environ.

    Returns:
        Dictionary with the same keys but environment variable references resolved
        to their actual values as plain strings

    Raises:
        SecretResolutionError: When strict=True and a referenced environment variable
                              is not found or is empty
        ValueError: When an environment variable name doesn't match valid naming
                   conventions (must start with letter or underscore, followed by
                   alphanumeric characters or underscores)

    Example:
        >>> import os
        >>> os.environ["MY_TOKEN"] = "secret_value_123"
        >>> mappings = {"token": "${MY_TOKEN}", "literal": "plain_value"}
        >>> resolved = resolve_env_var_references(mappings)
        >>> print(resolved)
        {'token': 'secret_value_123', 'literal': 'plain_value'}

        >>> # Using custom env_vars dict
        >>> custom_env = {"CUSTOM_TOKEN": "my_secret"}
        >>> mappings = {"token": "${CUSTOM_TOKEN}"}
        >>> resolved = resolve_env_var_references(mappings, env_vars=custom_env)
        >>> print(resolved)
        {'token': 'my_secret'}

        >>> # Multiple references in one value
        >>> mappings = {"combined": "${PREFIX}_${SUFFIX}"}
        >>> os.environ["PREFIX"] = "api"
        >>> os.environ["SUFFIX"] = "key"
        >>> resolved = resolve_env_var_references(mappings)
        >>> print(resolved["combined"])
        'api_key'

        >>> # Missing variable with strict=True (raises error)
        >>> try:
        ...     resolve_env_var_references({"token": "${MISSING_VAR}"})
        ... except SecretResolutionError as e:
        ...     print(f"Error: {e}")
        Error: Environment variable 'MISSING_VAR' not found or empty

        >>> # Missing variable with strict=False (keeps reference)
        >>> resolved = resolve_env_var_references(
        ...     {"token": "${MISSING_VAR}"},
        ...     strict=False
        ... )
        >>> print(resolved["token"])
        ${MISSING_VAR}
    """
    resolved = {}

    # Use provided env_vars or default to os.environ
    env_source = env_vars if env_vars is not None else os.environ

    # Environment variable name pattern: starts with letter or underscore,
    # followed by alphanumeric or underscores
    env_var_pattern = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}")

    for key, value in secret_mappings.items():
        if isinstance(value, str):

            def replacer(match: re.Match) -> str:
                """Replace a single ${ENV_VAR} reference with its value."""
                env_var_name = match.group(1)

                # Validate environment variable name format
                if not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", env_var_name):
                    raise ValueError(
                        f"Invalid environment variable name: '{env_var_name}'. "
                        "Must start with a letter or underscore, followed by "
                        "alphanumeric characters or underscores."
                    )

                env_value = env_source.get(env_var_name)

                if env_value is None or env_value == "":
                    if strict:
                        raise SecretResolutionError(f"Environment variable '{env_var_name}' not found or empty")
                    # In non-strict mode, keep the original reference
                    return match.group(0)

                return env_value

            # Replace all ${ENV_VAR} references in the value
            resolved_value = env_var_pattern.sub(replacer, value)
            resolved[key] = resolved_value
        else:
            # Non-string values are converted to strings
            resolved[key] = str(value)

    return resolved
