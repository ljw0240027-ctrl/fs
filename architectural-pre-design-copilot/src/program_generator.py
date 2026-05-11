from __future__ import annotations

from typing import Dict, List


def generate_program_table(project_info: Dict, max_gfa_m2: float) -> List[Dict]:
    programs = project_info["target_programs"]
    table = []

    total_ratio = sum(float(item.get("ratio", 0)) for item in programs)
    if total_ratio <= 0:
        raise ValueError("target_programs ratio total must be greater than 0")

    for item in programs:
        name = item.get("name", "Unnamed")
        ratio = float(item.get("ratio", 0))
        normalized_ratio = ratio / total_ratio * 100
        area = max_gfa_m2 * normalized_ratio / 100
        table.append(
            {
                "program": name,
                "ratio_percent": round(normalized_ratio, 2),
                "area_m2": round(area, 2),
            }
        )

    return table
