from __future__ import annotations

from dataclasses import dataclass
from math import floor
from typing import Dict


@dataclass
class ScaleReview:
    max_building_area_m2: float
    max_gfa_m2: float
    possible_floor_count: int
    average_floor_area_m2: float



def calculate_scale_review(project_info: Dict) -> ScaleReview:
    site_area = float(project_info["site_area_m2"])
    bcr = float(project_info["building_coverage_ratio"])
    far = float(project_info["floor_area_ratio"])
    max_height = float(project_info["max_height_m"])
    floor_height = float(project_info["floor_height_m"])

    possible_floor_count = max(1, floor(max_height / floor_height))
    max_building_area_m2 = site_area * bcr / 100
    max_gfa_m2 = site_area * far / 100
    average_floor_area_m2 = max_gfa_m2 / possible_floor_count

    return ScaleReview(
        max_building_area_m2=max_building_area_m2,
        max_gfa_m2=max_gfa_m2,
        possible_floor_count=possible_floor_count,
        average_floor_area_m2=average_floor_area_m2,
    )
