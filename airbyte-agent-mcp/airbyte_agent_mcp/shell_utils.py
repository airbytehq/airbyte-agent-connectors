"""Shell and command-line utilities."""

import shutil


def find_executable(name: str) -> str | None:
    """Find an executable in the system PATH.

    Args:
        name: Name of the executable to find.

    Returns:
        Full path to the executable, or None if not found.
    """
    return shutil.which(name)


def is_executable_available(name: str) -> bool:
    """Check if an executable is available in the system PATH.

    Args:
        name: Name of the executable to check.

    Returns:
        True if the executable is available, False otherwise.
    """
    return find_executable(name) is not None
