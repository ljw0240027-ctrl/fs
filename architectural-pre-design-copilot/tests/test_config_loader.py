from pathlib import Path

import pytest

from src.config_loader import ConfigError, load_project_info, validate_required_fields


def test_validate_required_fields_missing():
    missing = validate_required_fields({"project_name": "A"})
    assert "site_location" in missing


def test_load_project_info_not_found(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        load_project_info(tmp_path / "missing.yaml")


def test_invalid_value_range(tmp_path: Path):
    p = tmp_path / "project_info.yaml"
    p.write_text(
        """
project_name: A
site_location: B
site_area_m2: -1
zoning: C
building_coverage_ratio: 60
floor_area_ratio: 300
max_height_m: 50
floor_height_m: 4
target_use: U
target_programs:
  - name: O
    ratio: 100
site_context: {}
client_requests: [x]
report_target: y
""",
        encoding="utf-8",
    )
    with pytest.raises(ConfigError):
        load_project_info(p)
