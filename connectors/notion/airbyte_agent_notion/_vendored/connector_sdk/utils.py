"""Utility functions for working with connectors."""

from __future__ import annotations

from collections.abc import AsyncIterator
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .types import AuthOption


async def save_download(
    download_iterator: AsyncIterator[bytes],
    path: str | Path,
    *,
    overwrite: bool = False,
) -> Path:
    """Save a download iterator to a file.

    Args:
        download_iterator: AsyncIterator[bytes] from a download operation
        path: File path where content should be saved
        overwrite: Whether to overwrite existing file (default: False)

    Returns:
        Absolute Path to the saved file

    Raises:
        FileExistsError: If file exists and overwrite=False
        OSError: If file cannot be written

    Example:
        >>> from .utils import save_download
        >>>
        >>> # Download and save a file
        >>> result = await connector.download_article_attachment(id="123")
        >>> file_path = await save_download(result, "./downloads/attachment.pdf")
        >>> print(f"Downloaded to {file_path}")
        Downloaded to /absolute/path/to/downloads/attachment.pdf
        >>>
        >>> # Overwrite existing file
        >>> file_path = await save_download(result, "./downloads/attachment.pdf", overwrite=True)
    """
    # Convert to Path object
    file_path = Path(path).expanduser().resolve()

    # Check if file exists
    if file_path.exists() and not overwrite:
        raise FileExistsError(f"File already exists: {file_path}. Use overwrite=True to replace it.")

    # Create parent directories if needed
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Stream content to file
    try:
        with open(file_path, "wb") as f:
            async for chunk in download_iterator:
                f.write(chunk)
    except Exception as e:
        # Clean up partial file on error
        if file_path.exists():
            file_path.unlink()
        raise OSError(f"Failed to write file {file_path}: {e}") from e

    return file_path


def find_matching_auth_options(
    provided_keys: set[str],
    auth_options: list[AuthOption],
) -> list[AuthOption]:
    """Find auth options that match the provided credential keys.

    This is the single source of truth for auth scheme inference logic,
    used by both the executor (at runtime) and validation (for cassettes).

    Matching logic:
    - An option matches if all its required fields are present in provided_keys
    - Options with no required fields match any credentials

    Args:
        provided_keys: Set of credential/auth_config keys
        auth_options: List of AuthOption from the connector model

    Returns:
        List of AuthOption that match the provided keys
    """
    matching_options: list[AuthOption] = []

    for option in auth_options:
        if option.user_config_spec and option.user_config_spec.required:
            required_fields = set(option.user_config_spec.required)
            if required_fields.issubset(provided_keys):
                matching_options.append(option)
        elif not option.user_config_spec or not option.user_config_spec.required:
            # Option has no required fields - it matches any credentials
            matching_options.append(option)

    return matching_options


def infer_auth_scheme_name(
    provided_keys: set[str],
    auth_options: list[AuthOption],
) -> str | None:
    """Infer the auth scheme name from provided credential keys.

    Uses find_matching_auth_options to find matches, then returns
    the scheme name only if exactly one option matches.

    Args:
        provided_keys: Set of credential/auth_config keys
        auth_options: List of AuthOption from the connector model

    Returns:
        The scheme_name if exactly one match, None otherwise
    """
    if not provided_keys or not auth_options:
        return None

    matching = find_matching_auth_options(provided_keys, auth_options)

    if len(matching) == 1:
        return matching[0].scheme_name

    return None
