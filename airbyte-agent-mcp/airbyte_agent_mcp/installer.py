"""Connector installation utilities."""

import importlib.metadata
import json
import subprocess
import sys
import tomllib
from pathlib import Path

from .shell_utils import is_executable_available


class ConnectorInstallError(Exception):
    """Exception raised when connector installation fails."""

    pass


def _get_pip_command() -> list[str]:
    """Get the appropriate pip command based on available tools.

    Returns:
        Command list to use for pip operations. Uses 'uv pip' if uv is available,
        otherwise falls back to 'python -m pip'.
    """
    if is_executable_available("uv"):
        return ["uv", "pip"]
    return [sys.executable, "-m", "pip"]


def is_local_path(spec: str) -> bool:
    """Check if a package spec refers to a local file path."""
    return "/" in spec and not spec.startswith("git+")


def is_git_url(spec: str) -> bool:
    """Check if a package spec is a git VCS URL."""
    return spec.startswith("git+")


def get_package_name(spec: str) -> str:
    """Determine the Python package name for a given install spec.

    - PyPI name: the spec itself (minus any ``==version`` suffix)
    - Local path: read from ``pyproject.toml``
    - Git URL: look up via PEP 610 ``direct_url.json`` after installation

    For git URLs, the package must already be installed.

    Args:
        spec: Package specifier (PyPI name, local path, or git URL).

    Returns:
        The Python package name.

    Raises:
        ConnectorInstallError: If the package name cannot be determined.
    """
    if is_local_path(spec):
        return _get_package_name_from_local(spec)
    if is_git_url(spec):
        name = _find_package_by_source_url(spec)
        if name is None:
            raise ConnectorInstallError(f"Could not determine package name for {spec}")
        return name
    # PyPI — strip version specifier if present
    return spec.split("==")[0]


def _get_package_name_from_local(path: str) -> str:
    """Extract package name from local connector's pyproject.toml.

    Args:
        path: Path to local connector directory.

    Returns:
        Package name from pyproject.toml.

    Raises:
        ConnectorInstallError: If pyproject.toml not found or missing package name.
    """
    pyproject_path = Path(path) / "pyproject.toml"
    if not pyproject_path.exists():
        raise ConnectorInstallError(f"pyproject.toml not found at {path}")

    with open(pyproject_path, "rb") as f:
        pyproject = tomllib.load(f)

    package_name = pyproject.get("project", {}).get("name")
    if not package_name:
        raise ConnectorInstallError(f"Package name not found in {pyproject_path}")

    return package_name


def install_package(spec: str) -> None:
    """Install a connector package.

    Accepts anything ``pip install`` understands: a PyPI name (with optional
    ``==version``), a local path, or a VCS URL (``git+https://…``).

    Local paths are always installed in editable mode (``-e``).

    Args:
        spec: Package specifier.

    Raises:
        ConnectorInstallError: If installation fails.
    """
    cmd = [*_get_pip_command(), "install"]

    if is_local_path(spec):
        path = Path(spec).resolve()
        if not path.exists():
            raise ConnectorInstallError(f"Local path does not exist: {spec}")
        if not path.is_dir():
            raise ConnectorInstallError(f"Path is not a directory: {spec}")
        cmd.extend(["-e", str(path)])
    else:
        cmd.append(spec)

    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        raise ConnectorInstallError(f"Failed to install {spec}: {e.stderr}") from e

    # Refresh import machinery so the newly-installed package is visible
    # in this process.  subprocess-based installs modify the venv on disk
    # but Python caches sys.path entries and finder state at startup.
    importlib.invalidate_caches()
    # Re-read site-packages so new .pth / .egg-link entries are picked up.
    import site

    site.main()


def _find_package_by_source_url(url: str) -> str | None:
    """Find the installed package name whose source matches the given URL.

    Uses PEP 610 ``direct_url.json`` metadata written by pip/uv when
    installing from a URL or local path.  Works even if the package was
    already installed.

    Args:
        url: The original install spec (e.g. ``git+https://github.com/org/repo.git``).

    Returns:
        The package name, or None if no match is found.
    """
    normalized = url.replace("git+", "")
    # Strip @branch and #subdirectory fragments for matching
    for sep in ("@", "#"):
        if sep in normalized:
            normalized = normalized[: normalized.index(sep)]
    for dist in importlib.metadata.distributions():
        direct_url_text = dist.read_text("direct_url.json")
        if direct_url_text:
            direct_url = json.loads(direct_url_text)
            if normalized in direct_url.get("url", ""):
                return dist.metadata["Name"]
    return None


def uninstall_package(package_name: str) -> None:
    """Uninstall a connector from the current virtual environment.

    Args:
        package_name: Name of the package to uninstall.

    Raises:
        ConnectorInstallError: If pip uninstall fails.
    """
    try:
        subprocess.run(
            [*_get_pip_command(), "uninstall", "-y", package_name],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise ConnectorInstallError(f"Failed to uninstall {package_name}: {e.stderr}") from e


def is_package_installed(package_name: str) -> bool:
    """Check if a connector package is installed.

    Args:
        package_name: Name of the package to check.

    Returns:
        True if the package is installed, False otherwise.
    """
    try:
        result = subprocess.run(
            [*_get_pip_command(), "show", package_name],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.returncode == 0
    except Exception:
        return False
