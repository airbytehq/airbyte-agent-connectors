"""Utility functions for working with connectors."""

from collections.abc import AsyncIterator
from pathlib import Path


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
