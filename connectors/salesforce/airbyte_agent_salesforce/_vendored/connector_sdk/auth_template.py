"""
Template engine for auth_mapping in x-airbyte-auth-config.

Handles template substitution for mapping user-provided config values to auth parameters.
"""

import re
from typing import Dict


class MissingVariableError(ValueError):
    """Raised when a template variable is not found in config.

    Extends ValueError for backwards compatibility with code that catches ValueError.
    """

    def __init__(self, var_name: str, available_fields: list):
        self.var_name = var_name
        self.available_fields = available_fields
        super().__init__(f"Template variable '${{{var_name}}}' not found in config. " f"Available fields: {available_fields}")


def apply_template(template: str, values: Dict[str, str]) -> str:
    """
    Apply template substitution for auth_mapping.

    Template syntax:
    - ${variable}: Replaced with value from the values dict
    - Any other text: Used as-is (constants or concatenation)

    Examples:
        >>> apply_template("${api_key}", {"api_key": "abc123"})
        'abc123'

        >>> apply_template("${email}/token", {"email": "user@example.com"})
        'user@example.com/token'

        >>> apply_template("api_token", {})
        'api_token'

        >>> apply_template("", {})
        ''

    Args:
        template: Template string with ${variable} placeholders
        values: Dict of variable names to values

    Returns:
        Resolved template string

    Raises:
        MissingVariableError: If template contains unresolved variables
    """
    if not template:
        return ""

    # Check if it's a pure constant (no variables)
    if "${" not in template:
        return template

    # Find all variable references
    variable_pattern = re.compile(r"\$\{([^}]+)\}")
    matches = variable_pattern.findall(template)

    # Substitute all ${var} with values
    result = template
    for var_name in matches:
        if var_name not in values:
            raise MissingVariableError(var_name, list(values.keys()))
        # Replace the variable with its value
        result = result.replace(f"${{{var_name}}}", values[var_name])

    return result


def apply_auth_mapping(
    auth_mapping: Dict[str, str],
    user_config: Dict[str, str],
    required_fields: list | None = None,
) -> Dict[str, str]:
    """
    Apply auth_mapping templates to user config.

    Takes the auth_mapping from x-airbyte-auth-config and user-provided config,
    and returns the mapped auth parameters. Optional fields (not in required_fields)
    are skipped if their template variables are not provided.

    Example:
        >>> auth_mapping = {
        ...     "username": "${api_key}",
        ...     "password": ""
        ... }
        >>> user_config = {"api_key": "my_key_123"}
        >>> apply_auth_mapping(auth_mapping, user_config)
        {'username': 'my_key_123', 'password': ''}

        >>> # Optional fields are skipped if not provided
        >>> auth_mapping = {
        ...     "access_token": "${access_token}",
        ...     "refresh_token": "${refresh_token}",
        ... }
        >>> user_config = {"access_token": "abc123"}
        >>> apply_auth_mapping(auth_mapping, user_config, required_fields=["access_token"])
        {'access_token': 'abc123'}

    Args:
        auth_mapping: Dict mapping auth parameters to template strings
        user_config: Dict of user-provided field values
        required_fields: List of required field names. If a template references
            a variable not in user_config and that variable is not required,
            the mapping is skipped. Behavior:
            - None: all fields are treated as required (backward compatible)
            - []: no fields are required (all optional)
            - ["foo"]: only "foo" is required

    Returns:
        Dict of resolved auth parameters

    Raises:
        MissingVariableError: If a required template variable is not found
    """
    resolved = {}
    required_set = set(required_fields) if required_fields is not None else None

    for param, template in auth_mapping.items():
        try:
            resolved[param] = apply_template(template, user_config)
        except MissingVariableError as e:
            # If the missing variable is not in required fields, skip this mapping
            if required_set is not None and e.var_name not in required_set:
                continue
            # Otherwise, re-raise the error
            raise

    return resolved
