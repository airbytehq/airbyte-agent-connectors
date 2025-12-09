"""Cassette loader for loading and matching cassettes to tool calls."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class CassetteResponse:
    """Represents a captured response from a cassette."""

    status_code: int
    headers: dict[str, str]
    body: Any


@dataclass
class Cassette:
    """Represents a single cassette with request/response data."""

    test_name: str
    description: str
    entity: str
    action: str
    auth_config: dict[str, Any]
    inputs: dict[str, Any]
    captured_request: dict[str, Any]
    captured_response: CassetteResponse

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Cassette":
        """Create a Cassette from a dictionary."""
        response_data = data.get("captured_response", {})
        return cls(
            test_name=data.get("test_name", ""),
            description=data.get("description", ""),
            entity=data.get("entity", ""),
            action=data.get("action", ""),
            auth_config=data.get("auth_config", {}),
            inputs=data.get("inputs", {}),
            captured_request=data.get("captured_request", {}),
            captured_response=CassetteResponse(
                status_code=response_data.get("status_code", 200),
                headers=response_data.get("headers", {}),
                body=response_data.get("body", {}),
            ),
        )


@dataclass
class CassetteLoader:
    """Loads and matches cassettes to tool calls by entity+action+params."""

    cassette_dir: Path
    cassettes: list[Cassette] = field(default_factory=list)
    _cassette_map: dict[tuple[str, str], list[Cassette]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Initialize the cassette map after loading."""
        if isinstance(self.cassette_dir, str):
            self.cassette_dir = Path(self.cassette_dir)

    def load_cassettes(self, cassette_files: list[str] | None = None) -> None:
        """Load cassettes from the cassette directory.

        Args:
            cassette_files: Optional list of specific cassette files to load.
                           If None, loads all .yaml files in the directory.
        """
        self.cassettes = []
        self._cassette_map = {}

        if cassette_files:
            files_to_load = [self.cassette_dir / f for f in cassette_files]
        else:
            files_to_load = list(self.cassette_dir.glob("*.yaml"))

        for cassette_file in files_to_load:
            if not cassette_file.exists():
                continue

            with open(cassette_file) as f:
                data = yaml.safe_load(f)

            if data is None:
                continue

            if isinstance(data, list):
                for item in data:
                    cassette = Cassette.from_dict(item)
                    self._add_cassette(cassette)
            else:
                cassette = Cassette.from_dict(data)
                self._add_cassette(cassette)

    def _add_cassette(self, cassette: Cassette) -> None:
        """Add a cassette to the internal storage."""
        self.cassettes.append(cassette)
        key = (cassette.entity, cassette.action)
        if key not in self._cassette_map:
            self._cassette_map[key] = []
        self._cassette_map[key].append(cassette)

    def get_response(
        self, entity: str, action: str, params: dict[str, Any] | None = None
    ) -> CassetteResponse | None:
        """Get a cassette response matching the entity, action, and params.

        Args:
            entity: The entity name (e.g., "users", "calls")
            action: The action name (e.g., "list", "get")
            params: Optional parameters to match against

        Returns:
            The matching CassetteResponse or None if not found
        """
        key = (entity, action)
        cassettes = self._cassette_map.get(key, [])

        if not cassettes:
            return None

        if params is None or not params:
            return cassettes[0].captured_response

        for cassette in cassettes:
            cassette_params = cassette.inputs.get("params", {})
            if self._params_match(params, cassette_params):
                return cassette.captured_response

        return cassettes[0].captured_response

    def _params_match(
        self, request_params: dict[str, Any], cassette_params: dict[str, Any]
    ) -> bool:
        """Check if request params match cassette params.

        This is a flexible match - cassette params can be a subset of request params.
        """
        if not cassette_params:
            return True

        for key, value in cassette_params.items():
            if key not in request_params:
                return False
            if request_params[key] != value:
                return False

        return True

    def get_all_entities(self) -> list[str]:
        """Get all unique entity names from loaded cassettes."""
        return list(set(c.entity for c in self.cassettes))

    def get_actions_for_entity(self, entity: str) -> list[str]:
        """Get all actions available for a given entity."""
        return list(set(c.action for c in self.cassettes if c.entity == entity))


def load_cassettes_from_files(
    cassette_dir: str | Path, cassette_files: list[str]
) -> CassetteLoader:
    """Convenience function to load cassettes from specific files.

    Args:
        cassette_dir: Directory containing cassette files
        cassette_files: List of cassette file names to load

    Returns:
        A CassetteLoader with the cassettes loaded
    """
    loader = CassetteLoader(cassette_dir=Path(cassette_dir))
    loader.load_cassettes(cassette_files)
    return loader
