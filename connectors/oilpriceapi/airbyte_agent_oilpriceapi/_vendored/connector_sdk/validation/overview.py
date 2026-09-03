"""
Connector overview for quick status reporting.

Produces a structured summary of a connector's implementation status,
configured exceptions, example questions, and readiness validation results.
Designed to be surfaced as a PR comment for easy review.
"""

import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Dict, List

import yaml

from ..connector_model_loader import (
    ConnectorModelLoaderError,
    load_connector_model,
)
from .readiness import build_cassette_map, validate_connector_readiness

GOLDEN_QUESTIONS_REPORT_FILENAME = "golden_questions_report.yaml"


def _extract_entity_actions(connector_data: Dict[str, Any]) -> List[str]:
    """Extract sorted entity.action pairs from connector.yaml paths.

    Args:
        connector_data: Parsed connector.yaml content

    Returns:
        Sorted list of "entity.action" strings (e.g., ["projects.list", "tasks.get"])
    """
    pairs = set()
    paths = connector_data.get("paths", {})
    for _path, methods in paths.items():
        if not isinstance(methods, dict):
            continue
        for _method, operation in methods.items():
            if not isinstance(operation, dict):
                continue
            entity = operation.get("x-airbyte-entity")
            action = operation.get("x-airbyte-action")
            if entity and action:
                pairs.add(f"{entity}.{action}")
    return sorted(pairs)


def compute_golden_questions_hash(connector_yaml_path: str | Path) -> str:
    """Compute a freshness hash for golden question validation reports.

    The hash covers:
    - Sorted list of direct golden questions
    - Sorted list of entity.action pairs from paths

    This means the hash changes when questions are added/removed/changed,
    or when entities/actions are added/removed, but NOT when unrelated parts
    of the connector.yaml change (descriptions, schemas, etc.).

    Use this to check whether a persisted ``tests/golden_questions_report.yaml``
    is stale relative to the current connector definition::

        from .overview import compute_golden_questions_hash
        import yaml

        with open("tests/golden_questions_report.yaml") as f:
            report = yaml.safe_load(f)
        current = compute_golden_questions_hash("connector.yaml")
        is_stale = report["freshness_hash"] != current

    Args:
        connector_yaml_path: Path to the connector.yaml file

    Returns:
        Hash string in the format ``"sha256:<hex>"``

    Raises:
        FileNotFoundError: If connector.yaml doesn't exist
        ValueError: If connector.yaml can't be parsed
    """
    path = Path(connector_yaml_path)
    if not path.exists():
        raise FileNotFoundError(f"Connector YAML not found: {path}")

    with path.open() as f:
        connector_data = yaml.safe_load(f)

    if not isinstance(connector_data, dict):
        raise ValueError(f"Invalid connector YAML: expected dict, got {type(connector_data)}")

    info = connector_data.get("info", {})
    example_questions = info.get("x-airbyte-example-questions", {})
    direct_questions = example_questions.get("direct", [])
    if not isinstance(direct_questions, list):
        direct_questions = []
    questions_sorted = sorted(str(q) for q in direct_questions)

    entity_actions = _extract_entity_actions(connector_data)

    canonical = json.dumps(
        {"questions": questions_sorted, "entity_actions": entity_actions},
        sort_keys=True,
        separators=(",", ":"),
    )
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def _load_golden_questions_report(connector_path: Path) -> Dict[str, Any] | None:
    """Load the persisted golden questions validation report if it exists."""
    report_file = connector_path / "tests" / GOLDEN_QUESTIONS_REPORT_FILENAME
    if not report_file.exists():
        return None

    try:
        with open(report_file) as f:
            report = yaml.safe_load(f)
        if not isinstance(report, dict) or "summary" not in report:
            return None
        return report
    except Exception:
        return None


def _extract_golden_questions_summary(
    report: Dict[str, Any] | None,
    connector_yaml_path: Path | None = None,
) -> Dict[str, Any]:
    """Extract a compact summary from the golden questions report.

    If *connector_yaml_path* is provided the function also computes the
    current freshness hash and sets ``"stale": True`` when it differs from
    the hash stored in the report.
    """
    if report is None:
        return {"available": False}

    summary = report.get("summary", {})
    results = report.get("results", [])
    coverage = report.get("coverage", {})

    result_map = {}
    for r in results:
        question_text = r.get("question", "")
        if question_text:
            result_map[question_text] = {
                "question_id": r.get("question_id", ""),
                "success": r.get("success", False),
                "answered": r.get("question_answered", False),
                "answer": r.get("answer", ""),
                "entities_used": r.get("entities_used", []),
                "actions_used": r.get("actions_used", []),
            }

    stale: bool | None = None
    report_hash = report.get("freshness_hash")
    if connector_yaml_path is not None and report_hash:
        try:
            current_hash = compute_golden_questions_hash(connector_yaml_path)
            stale = current_hash != report_hash
        except Exception:
            stale = None

    return {
        "available": True,
        "total": summary.get("total_questions", 0),
        "passed": summary.get("successful", 0),
        "failed": summary.get("failed", 0),
        "success_rate": summary.get("success_rate", 0.0),
        "questions_answered": summary.get("questions_answered", 0),
        "entities_tested": coverage.get("entities_tested", []),
        "actions_tested": coverage.get("actions_tested", []),
        "entity_action_pairs": coverage.get("entity_action_pairs", []),
        "result_map": result_map,
        "freshness_hash": report_hash,
        "stale": stale,
        "timestamp": report.get("timestamp"),
    }


def get_connector_overview(connector_dir: str | Path) -> Dict[str, Any]:
    """
    Generate a structured overview of a connector's status.

    Combines static analysis of connector.yaml with readiness validation
    results to produce a reviewer-friendly summary.

    Args:
        connector_dir: Path to the connector directory

    Returns:
        Dict with overview data including entities, exceptions,
        example questions, and readiness validation summary.
    """
    connector_path = Path(connector_dir)

    if not connector_path.exists():
        return {
            "success": False,
            "error": f"Connector directory not found: {connector_dir}",
        }

    config_file = connector_path / "connector.yaml"
    if not config_file.exists():
        return {
            "success": False,
            "error": f"connector.yaml not found in {connector_dir}",
        }

    try:
        config = load_connector_model(config_file)
    except ConnectorModelLoaderError as e:
        return {"success": False, "error": f"Failed to load connector.yaml: {str(e)}"}

    try:
        with open(config_file) as f:
            raw_spec = yaml.safe_load(f)
    except Exception:
        raw_spec = {}

    info = raw_spec.get("info", {})
    cassettes_dir = connector_path / "tests" / "cassettes"
    cassette_map = build_cassette_map(cassettes_dir)

    entities = _extract_entities(config, cassette_map)
    auth_schemes = _extract_auth_schemes(config)
    exceptions = _extract_exceptions(info, config)
    example_questions = _extract_example_questions(info)

    gq_report = _load_golden_questions_report(connector_path)
    golden_questions = _extract_golden_questions_summary(gq_report, connector_yaml_path=config_file)

    readiness_result = validate_connector_readiness(connector_dir)
    readiness = _extract_readiness_summary(readiness_result)

    return {
        "success": True,
        "connector_name": config.name,
        "entities": entities,
        "auth_schemes": auth_schemes,
        "exceptions": exceptions,
        "example_questions": example_questions,
        "golden_questions": golden_questions,
        "readiness": readiness,
    }


def _extract_entities(config, cassette_map) -> List[Dict[str, Any]]:
    entities = []
    for entity in config.entities:
        actions = []
        cassette_counts = {}
        untested_actions = []

        for action in entity.actions:
            action_name = action.value
            actions.append(action_name)

            key = (entity.name, action_name)
            cassette_counts[action_name] = len(cassette_map.get(key, []))

            endpoint = entity.endpoints[action]
            if endpoint.untested:
                untested_actions.append(action_name)

        entities.append(
            {
                "name": entity.name,
                "actions": actions,
                "cassette_counts": cassette_counts,
                "untested_actions": untested_actions,
            }
        )
    return entities


def _extract_auth_schemes(config) -> Dict[str, Any]:
    options = config.auth.options or []
    defined = [opt.scheme_name for opt in options]
    untested = [opt.scheme_name for opt in options if opt.untested]
    tested = [opt.scheme_name for opt in options if not opt.untested]

    return {
        "defined": defined,
        "tested": tested,
        "untested": untested,
    }


def _extract_exceptions(info: dict, config) -> Dict[str, Any]:
    skip_streams = info.get("x-airbyte-skip-suggested-streams", []) or []
    skip_auth = info.get("x-airbyte-skip-auth-methods", []) or []

    untested_ops = []
    for entity in config.entities:
        for action in entity.actions:
            endpoint = entity.endpoints[action]
            if endpoint.untested:
                untested_ops.append(f"{entity.name}.{action.value}")

    untested_auth = [opt.scheme_name for opt in (config.auth.options or []) if opt.untested]

    total = len(skip_streams) + len(skip_auth) + len(untested_ops) + len(untested_auth)

    return {
        "skip_suggested_streams": skip_streams,
        "skip_auth_methods": skip_auth,
        "untested_operations": untested_ops,
        "untested_auth_schemes": untested_auth,
        "total_count": total,
    }


def _extract_example_questions(info: dict) -> Dict[str, Any]:
    questions = info.get("x-airbyte-example-questions", {}) or {}
    direct = questions.get("direct", []) or []
    search = questions.get("search", []) or []
    unsupported = questions.get("unsupported", []) or []

    return {
        "direct": direct,
        "search": search,
        "unsupported": unsupported,
        "counts": {
            "direct": len(direct),
            "search": len(search),
            "unsupported": len(unsupported),
        },
    }


def _extract_readiness_summary(readiness_result: dict) -> Dict[str, Any]:
    if "error" in readiness_result:
        return {
            "success": False,
            "error": readiness_result["error"],
            "summary": {},
            "warnings": [],
            "errors": [],
            "replication_checks": [],
        }

    summary = readiness_result.get("summary", {})
    readiness_warnings_list = list(readiness_result.get("readiness_warnings", []))

    # Collect warnings from validation results (per-cassette)
    for val_result in readiness_result.get("validation_results", []):
        for warning in val_result.get("warnings", []):
            readiness_warnings_list.append(warning)
        for cassette_val in val_result.get("schema_validation", []):
            for warning in cassette_val.get("warnings", []):
                readiness_warnings_list.append(warning)

    # Collect errors from validation results
    errors = []
    for val_result in readiness_result.get("validation_results", []):
        if val_result.get("cassettes_found", 0) == 0 and not val_result.get("untested"):
            errors.append(f"Missing cassettes: {val_result['entity']}.{val_result['action']}")
        for cassette_val in val_result.get("schema_validation", []):
            for error in cassette_val.get("errors", []):
                errors.append(f"{val_result['entity']}.{val_result['action']}: {error}")

    # Auth scheme errors/warnings
    auth_val = readiness_result.get("auth_scheme_validation", {})
    for error in auth_val.get("errors", []):
        errors.append(error)
    for warning in auth_val.get("warnings", []):
        readiness_warnings_list.append(warning)

    # Replication checks
    replication = readiness_result.get("replication_validation", {})
    replication_checks = replication.get("checks", [])
    for error in replication.get("errors", []):
        errors.append(f"Replication: {error}")
    for warning in replication.get("warnings", []):
        readiness_warnings_list.append(f"Replication: {warning}")

    return {
        "success": readiness_result.get("success", False),
        "summary": summary,
        "warnings": readiness_warnings_list,
        "errors": errors,
        "replication_checks": replication_checks,
    }


def get_base_overview(connector_dir: str | Path, git_ref: str) -> Dict[str, Any] | None:
    """
    Get the connector overview as it existed at a given git ref.

    Uses `git show` to extract the connector.yaml and cassette files
    from the base ref into a temp directory, then runs get_connector_overview on it.

    Returns None if the connector didn't exist at that ref.
    """
    connector_path = Path(connector_dir).resolve()

    git_root = _find_git_root(connector_path)
    if not git_root:
        return None

    rel_path = connector_path.relative_to(git_root)
    yaml_git_path = f"{rel_path}/connector.yaml"

    try:
        subprocess.run(
            ["git", "show", f"{git_ref}:{yaml_git_path}"],
            cwd=git_root,
            capture_output=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

    tmp_dir = tempfile.mkdtemp(prefix="connector_base_")
    try:
        tmp_connector = Path(tmp_dir)

        yaml_content = subprocess.run(
            ["git", "show", f"{git_ref}:{yaml_git_path}"],
            cwd=git_root,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        (tmp_connector / "connector.yaml").write_text(yaml_content)

        cassettes_rel = f"{rel_path}/tests/cassettes"
        cassettes_out = tmp_connector / "tests" / "cassettes"
        cassettes_out.mkdir(parents=True, exist_ok=True)

        try:
            ls_result = subprocess.run(
                ["git", "ls-tree", "--name-only", f"{git_ref}:{cassettes_rel}"],
                cwd=git_root,
                capture_output=True,
                text=True,
                check=True,
            )
            for filename in ls_result.stdout.strip().split("\n"):
                filename = filename.strip()
                if not filename or not filename.endswith(".yaml"):
                    continue
                try:
                    file_content = subprocess.run(
                        [
                            "git",
                            "show",
                            f"{git_ref}:{cassettes_rel}/{filename}",
                        ],
                        cwd=git_root,
                        capture_output=True,
                        text=True,
                        check=True,
                    ).stdout
                    (cassettes_out / filename).write_text(file_content)
                except subprocess.CalledProcessError:
                    continue
        except subprocess.CalledProcessError:
            pass

        gq_report_rel = f"{rel_path}/tests/{GOLDEN_QUESTIONS_REPORT_FILENAME}"
        try:
            gq_content = subprocess.run(
                ["git", "show", f"{git_ref}:{gq_report_rel}"],
                cwd=git_root,
                capture_output=True,
                text=True,
                check=True,
            ).stdout
            (cassettes_out.parent / GOLDEN_QUESTIONS_REPORT_FILENAME).write_text(gq_content)
        except subprocess.CalledProcessError:
            pass

        return get_connector_overview(tmp_connector)
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def _find_git_root(path: Path) -> Path | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=path if path.is_dir() else path.parent,
            capture_output=True,
            text=True,
            check=True,
        )
        return Path(result.stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def diff_overviews(base: Dict[str, Any] | None, head: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compute the delta between a base overview and the current (head) overview.

    Returns a dict of changes suitable for rendering in the markdown report.
    """
    if base is None or not base.get("success"):
        return {"is_new_connector": True}

    if not head.get("success"):
        return {}

    changes: Dict[str, Any] = {"is_new_connector": False}

    base_entity_names = {e["name"] for e in base.get("entities", [])}
    head_entity_names = {e["name"] for e in head.get("entities", [])}
    added_entities = head_entity_names - base_entity_names
    removed_entities = base_entity_names - head_entity_names
    if added_entities:
        changes["added_entities"] = sorted(added_entities)
    if removed_entities:
        changes["removed_entities"] = sorted(removed_entities)

    base_ops = _collect_operations(base)
    head_ops = _collect_operations(head)
    added_ops = head_ops - base_ops
    removed_ops = base_ops - head_ops
    net_added = added_ops - {f"{e}.{a}" for e in added_entities for a in _entity_actions(head, e)}
    net_removed = removed_ops - {f"{e}.{a}" for e in removed_entities for a in _entity_actions(base, e)}
    if net_added:
        changes["added_operations"] = sorted(net_added)
    if net_removed:
        changes["removed_operations"] = sorted(net_removed)

    base_q = base.get("example_questions", {})
    head_q = head.get("example_questions", {})
    for category in ("direct", "search", "unsupported"):
        base_set = set(base_q.get(category, []))
        head_set = set(head_q.get(category, []))
        added = head_set - base_set
        removed = base_set - head_set
        if added:
            changes[f"added_{category}_questions"] = sorted(added)
        if removed:
            changes[f"removed_{category}_questions"] = sorted(removed)

    base_exc = base.get("exceptions", {})
    head_exc = head.get("exceptions", {})
    for key in (
        "skip_suggested_streams",
        "skip_auth_methods",
        "untested_operations",
        "untested_auth_schemes",
    ):
        base_set = set(base_exc.get(key, []))
        head_set = set(head_exc.get(key, []))
        added = head_set - base_set
        removed = base_set - head_set
        if added:
            changes[f"added_{key}"] = sorted(added)
        if removed:
            changes[f"removed_{key}"] = sorted(removed)

    base_readiness = base.get("readiness", {}).get("success", False)
    head_readiness = head.get("readiness", {}).get("success", False)
    if base_readiness != head_readiness:
        changes["readiness_changed"] = {
            "from": base_readiness,
            "to": head_readiness,
        }

    base_warnings = len(base.get("readiness", {}).get("warnings", []))
    head_warnings = len(head.get("readiness", {}).get("warnings", []))
    if base_warnings != head_warnings:
        changes["warnings_delta"] = head_warnings - base_warnings

    base_errors = len(base.get("readiness", {}).get("errors", []))
    head_errors = len(head.get("readiness", {}).get("errors", []))
    if base_errors != head_errors:
        changes["errors_delta"] = head_errors - base_errors

    base_gq = base.get("golden_questions", {})
    head_gq = head.get("golden_questions", {})
    if base_gq.get("available") or head_gq.get("available"):
        base_passed = base_gq.get("passed", 0) if base_gq.get("available") else 0
        base_total = base_gq.get("total", 0) if base_gq.get("available") else 0
        head_passed = head_gq.get("passed", 0) if head_gq.get("available") else 0
        head_total = head_gq.get("total", 0) if head_gq.get("available") else 0

        if not base_gq.get("available") and head_gq.get("available"):
            changes["golden_questions_added"] = {
                "passed": head_passed,
                "total": head_total,
            }
        elif base_gq.get("available") and not head_gq.get("available"):
            changes["golden_questions_removed"] = True
        elif (base_passed, base_total) != (head_passed, head_total):
            changes["golden_questions_changed"] = {
                "from": {"passed": base_passed, "total": base_total},
                "to": {"passed": head_passed, "total": head_total},
            }

    return changes


def _collect_operations(overview: dict) -> set:
    ops = set()
    for entity in overview.get("entities", []):
        for action in entity["actions"]:
            ops.add(f"{entity['name']}.{action}")
    return ops


def _entity_actions(overview: dict, entity_name: str) -> List[str]:
    for entity in overview.get("entities", []):
        if entity["name"] == entity_name:
            return entity["actions"]
    return []


def format_overview_as_markdown(overview: dict, diff: Dict[str, Any] | None = None) -> str:
    """
    Format a connector overview dict as GitHub-flavored markdown.

    Designed for use as a PR comment body. Compact, scannable layout
    that leads with what matters for review.
    """
    if not overview.get("success"):
        error = overview.get("error", "Unknown error")
        return f"## Connector Overview\n\n❌ Failed to generate overview: {error}\n"

    name = overview["connector_name"]
    readiness = overview.get("readiness", {})
    success = readiness.get("success", False)
    status_icon = "✅" if success else "❌"

    lines = [f"## {status_icon} `{name}`"]
    lines.append("")
    lines.append(f"Connector implementation status for `{name}`. Auto-generated from `connector.yaml` and test results.")
    lines.append("")
    lines.append(_format_summary_line(overview))

    golden = overview.get("golden_questions", {})
    if golden.get("stale"):
        lines.append("")
        lines.append("> ⚠️ Golden question results predate the latest `connector.yaml` changes — re-run validation to refresh.")

    diff_section = _format_diff_section(diff) if diff else ""
    if diff_section:
        lines.append("")
        lines.append(diff_section)

    exceptions_section = _format_exceptions_section(overview)
    if exceptions_section:
        lines.append("")
        lines.append(exceptions_section)

    lines.append("")
    lines.append(_format_entities_section(overview))

    questions_section = _format_questions_section(overview)
    if questions_section:
        lines.append("")
        lines.append(questions_section)

    readiness_section = _format_readiness_section(overview)
    if readiness_section:
        lines.append("")
        lines.append(readiness_section)

    return "\n".join(lines)


def _format_summary_line(overview: dict) -> str:
    entities = overview.get("entities", [])
    questions = overview.get("example_questions", {})
    readiness = overview.get("readiness", {})
    exceptions = overview.get("exceptions", {})
    auth = overview.get("auth_schemes", {})
    golden = overview.get("golden_questions", {})

    total_actions = sum(len(e["actions"]) for e in entities)
    direct_q = questions.get("counts", {}).get("direct", 0)
    search_q = questions.get("counts", {}).get("search", 0)
    error_count = len(readiness.get("errors", []))
    exception_count = exceptions.get("total_count", 0)
    auth_count = len(auth.get("defined", []))

    parts = [
        f"**{len(entities)}** entities",
        f"**{total_actions}** operations",
    ]
    if auth_count > 1:
        parts.append(f"**{auth_count}** auth schemes")
    if direct_q + search_q:
        parts.append(f"**{direct_q + search_q}** questions")
    if golden.get("available"):
        gq_passed = golden.get("passed", 0)
        gq_total = golden.get("total", 0)
        gq_icon = "✅" if gq_passed == gq_total else "❌"
        gq_label = f"{gq_icon} **{gq_passed}/{gq_total}** golden Qs validated"
        if golden.get("stale"):
            gq_label += " ⚠️ stale"
        parts.append(gq_label)
    if exception_count:
        parts.append(f"⚠️ **{exception_count}** exceptions")
    if error_count:
        parts.append(f"❌ **{error_count}** errors")

    return " · ".join(parts)


def _format_diff_section(diff: Dict[str, Any] | None) -> str:
    if not diff:
        return ""

    if diff.get("is_new_connector"):
        return "> 🆕 **New connector** — not present on base branch"

    items = []

    readiness_change = diff.get("readiness_changed")
    if readiness_change:
        if readiness_change["to"]:
            items.append("✅ Readiness: now **passing**")
        else:
            items.append("❌ Readiness: now **failing**")

    added_entities = diff.get("added_entities", [])
    if added_entities:
        items.append(f"➕ Added entities: {', '.join(f'`{e}`' for e in added_entities)}")
    removed_entities = diff.get("removed_entities", [])
    if removed_entities:
        items.append(f"➖ Removed entities: {', '.join(f'`{e}`' for e in removed_entities)}")

    added_ops = diff.get("added_operations", [])
    if added_ops:
        items.append(f"➕ Added operations: {', '.join(f'`{o}`' for o in added_ops)}")
    removed_ops = diff.get("removed_operations", [])
    if removed_ops:
        items.append(f"➖ Removed operations: {', '.join(f'`{o}`' for o in removed_ops)}")

    for category, label in (
        ("direct", "direct"),
        ("search", "search"),
        ("unsupported", "unsupported"),
    ):
        added_q = diff.get(f"added_{category}_questions", [])
        removed_q = diff.get(f"removed_{category}_questions", [])
        if added_q:
            items.append(f"➕ {len(added_q)} new {label} question{'s' if len(added_q) != 1 else ''}")
        if removed_q:
            items.append(f"➖ {len(removed_q)} {label} question{'s' if len(removed_q) != 1 else ''} removed")

    for key, label, emoji in (
        ("skip_suggested_streams", "skipped streams", "🔇"),
        ("skip_auth_methods", "skipped auth methods", "🔇"),
        ("untested_operations", "untested operations", "🚧"),
        ("untested_auth_schemes", "untested auth schemes", "🚧"),
    ):
        added = diff.get(f"added_{key}", [])
        removed = diff.get(f"removed_{key}", [])
        if added:
            items.append(f"{emoji} Added {label}: {', '.join(f'`{v}`' for v in added)}")
        if removed:
            items.append(f"✅ Removed {label}: {', '.join(f'`{v}`' for v in removed)}")

    errors_delta = diff.get("errors_delta")
    if errors_delta is not None and errors_delta != 0:
        if errors_delta > 0:
            items.append(f"❌ +{errors_delta} new error{'s' if errors_delta != 1 else ''}")
        else:
            items.append(f"✅ {errors_delta} error{'s' if abs(errors_delta) != 1 else ''} fixed")

    warnings_delta = diff.get("warnings_delta")
    if warnings_delta is not None and warnings_delta != 0:
        if warnings_delta > 0:
            items.append(f"+{warnings_delta} warnings")
        else:
            items.append(f"{warnings_delta} warnings")

    gq_added = diff.get("golden_questions_added")
    if gq_added:
        items.append(f"🧪 Golden questions validated: **{gq_added['passed']}/{gq_added['total']}** passing")
    if diff.get("golden_questions_removed"):
        items.append("⚠️ Golden questions report removed")
    gq_changed = diff.get("golden_questions_changed")
    if gq_changed:
        frm = gq_changed["from"]
        to = gq_changed["to"]
        items.append(f"🧪 Golden questions: {frm['passed']}/{frm['total']} → **{to['passed']}/{to['total']}**")

    if not items:
        return ""

    lines = ["> 📋 **Changes from base:**"]
    for item in items:
        lines.append(f"> - {item}")
    return "\n".join(lines)


def _format_exceptions_section(overview: dict) -> str:
    exceptions = overview.get("exceptions", {})
    total = exceptions.get("total_count", 0)

    if total == 0:
        return ""

    lines = [f"> ⚠️ **{total} validation exception{'s' if total != 1 else ''}** — these skip readiness checks and need justification"]

    skip_streams = exceptions.get("skip_suggested_streams", [])
    if skip_streams:
        streams_str = ", ".join(f"`{s}`" for s in skip_streams)
        lines.append(f"> - 🔇 Skipped suggested streams: {streams_str}")

    skip_auth = exceptions.get("skip_auth_methods", [])
    if skip_auth:
        auth_str = ", ".join(f"`{a}`" for a in skip_auth)
        lines.append(f"> - 🔇 Skipped auth methods: {auth_str}")

    untested_ops = exceptions.get("untested_operations", [])
    if untested_ops:
        ops_str = ", ".join(f"`{o}`" for o in untested_ops)
        lines.append(f"> - 🚧 Untested operations: {ops_str}")

    untested_auth = exceptions.get("untested_auth_schemes", [])
    if untested_auth:
        auth_str = ", ".join(f"`{a}`" for a in untested_auth)
        lines.append(f"> - 🚧 Untested auth schemes: {auth_str}")

    return "\n".join(lines)


def _format_entities_section(overview: dict) -> str:
    entities = overview.get("entities", [])
    auth = overview.get("auth_schemes", {})

    if not entities:
        return "_No entities defined._"

    lines = [
        "<details>",
        "<summary>📦 <strong>Entities & Operations</strong></summary>",
        "",
    ]

    for entity in entities:
        name = entity["name"]
        untested_set = set(entity.get("untested_actions", []))
        action_parts = []
        for action in entity["actions"]:
            cassettes = entity["cassette_counts"].get(action, 0)
            if action in untested_set:
                action_parts.append(f"🚧 {action} *(untested)*")
            elif cassettes == 0:
                action_parts.append(f"⚠️ **{action}**")
            else:
                action_parts.append(action)
        lines.append(f"- **{name}** — {', '.join(action_parts)}")

    defined = auth.get("defined", [])
    if defined:
        untested = auth.get("untested", [])
        parts = []
        for scheme in defined:
            if scheme in untested:
                parts.append(f"🚧 {scheme} *(untested)*")
            else:
                parts.append(f"✅ {scheme}")
        label = "🔐 Auth" if len(defined) == 1 else "🔐 Auth schemes"
        lines.append(f"\n{label}: {' · '.join(parts)}")

    lines.extend(["", "</details>"])
    return "\n".join(lines)


def _format_questions_section(overview: dict) -> str:
    questions = overview.get("example_questions", {})
    golden = overview.get("golden_questions", {})
    result_map = golden.get("result_map", {}) if golden.get("available") else {}

    counts = questions.get("counts", {})
    direct_count = counts.get("direct", 0)
    search_count = counts.get("search", 0)
    unsupported_count = counts.get("unsupported", 0)

    total = direct_count + search_count + unsupported_count
    if total == 0:
        return ""

    count_parts = []
    if direct_count:
        count_parts.append(f"{direct_count} direct")
    if search_count:
        count_parts.append(f"{search_count} search")
    if unsupported_count:
        count_parts.append(f"{unsupported_count} unsupported")

    if golden.get("available"):
        gq_passed = golden.get("passed", 0)
        gq_total = golden.get("total", 0)
        gq_icon = "✅" if gq_passed == gq_total else "⚠️"
        gq_label = f"{gq_icon} {gq_passed}/{gq_total} validated"
        if golden.get("stale"):
            gq_label += " — ⚠️ stale"
        count_parts.append(gq_label)

    lines = [
        "<details>",
        f"<summary>💬 <strong>Example Questions</strong> ({', '.join(count_parts)})</summary>",
        "",
    ]

    direct = questions.get("direct", [])
    if direct:
        lines.append("**Direct** (answerable via API):")
        for q in direct:
            result = result_map.get(q)
            if result is not None:
                icon = "✅" if result["success"] else "❌"
                qid = result.get("question_id", "")
                answer = result.get("answer", "")
                entities = result.get("entities_used", [])
                actions = result.get("actions_used", [])
                label = f"{qid}: {q}" if qid else q
                lines.append(f"- {icon} **{label}**")
                if answer:
                    for answer_line in answer.split("\n"):
                        lines.append(f"  > {answer_line}")
                if entities or actions:
                    used_parts = []
                    if entities:
                        used_parts.append(f"entities: {', '.join(entities)}")
                    if actions:
                        used_parts.append(f"actions: {', '.join(actions)}")
                    lines.append(f"  > *{' · '.join(used_parts)}*")
            else:
                lines.append(f"- {q}")

    search = questions.get("search", [])
    if search:
        if direct:
            lines.append("")
        lines.append("**Search** (require cached data):")
        for q in search:
            lines.append(f"- {q}")

    unsupported = questions.get("unsupported", [])
    if unsupported:
        if direct or search:
            lines.append("")
        lines.append("**Unsupported:**")
        for q in unsupported:
            lines.append(f"- {q}")

    lines.extend(["", "</details>"])
    return "\n".join(lines)


def _format_readiness_section(overview: dict) -> str:
    readiness = overview.get("readiness", {})

    if "error" in readiness:
        return f"> ❌ Readiness validation failed: {readiness['error']}"

    warnings = readiness.get("warnings", [])
    errors = readiness.get("errors", [])
    replication_checks = readiness.get("replication_checks", [])

    if not errors and not warnings and not replication_checks:
        return ""

    detail_parts = []
    if errors:
        detail_parts.append(f"❌ {len(errors)} errors")
    if warnings:
        detail_parts.append(f"{len(warnings)} warnings")
    detail_str = ", ".join(detail_parts) if detail_parts else "details"

    lines = [
        "<details>",
        f"<summary>🔍 <strong>Validation Details</strong> ({detail_str})</summary>",
        "",
    ]

    if errors:
        for error in errors:
            lines.append(f"- ❌ {error}")
        lines.append("")

    if warnings:
        for warning in warnings:
            lines.append(f"- {warning}")
        lines.append("")

    if replication_checks:
        failed_checks = [c for c in replication_checks if c.get("status") not in ("pass", "skip")]
        if failed_checks:
            lines.append("**Replication issues:**")
            for check in failed_checks:
                name = check.get("name", "unknown")
                status = check.get("status", "unknown")
                messages = check.get("messages", [])
                msg_str = f" — {messages[0]}" if messages else ""
                lines.append(f"- `{name}`: {status}{msg_str}")
            lines.append("")

    lines.extend(["</details>"])
    return "\n".join(lines)
