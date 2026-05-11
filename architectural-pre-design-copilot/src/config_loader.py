from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import yaml

REQUIRED_FIELDS = [
    "project_name",
    "site_location",
    "site_area_m2",
    "zoning",
    "building_coverage_ratio",
    "floor_area_ratio",
    "max_height_m",
    "floor_height_m",
    "target_use",
    "target_programs",
    "site_context",
    "client_requests",
    "report_target",
]


class ConfigError(ValueError):
    pass


def load_project_info(config_path: Path) -> Dict[str, Any]:
    if not config_path.exists():
        raise FileNotFoundError(f"project_info.yaml not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    missing = validate_required_fields(data)
    if missing:
        raise ConfigError(f"Missing required fields: {', '.join(missing)}")

    validate_value_ranges(data)
    return data


def validate_required_fields(data: Dict[str, Any]) -> List[str]:
    missing = []
    for field in REQUIRED_FIELDS:
        if field not in data or data[field] in (None, "", []):
            missing.append(field)
    return missing


def validate_value_ranges(data: Dict[str, Any]) -> None:
    site_area = float(data["site_area_m2"])
    bcr = float(data["building_coverage_ratio"])
    far = float(data["floor_area_ratio"])
    floor_height = float(data["floor_height_m"])

    if site_area <= 0:
        raise ConfigError("site_area_m2 must be greater than 0")
    if bcr < 0 or bcr > 100:
        raise ConfigError("building_coverage_ratio must be between 0 and 100")
    if far <= 0:
        raise ConfigError("floor_area_ratio must be greater than 0")
    if floor_height <= 0:
        raise ConfigError("floor_height_m must be greater than 0")
