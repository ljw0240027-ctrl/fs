from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.config_loader import ConfigError, load_project_info
from src.concept_critic import generate_concept_candidates
from src.diagram_brief_generator import generate_diagram_brief
from src.massing_strategy_generator import generate_massing_strategies
from src.program_generator import generate_program_table
from src.report_generator import (
    generate_executive_summary,
    generate_gamma_prompt,
    generate_project_brief,
)
from src.scale_calculator import calculate_scale_review
from src.site_strategy_generator import generate_site_strategy
from src.utils import ensure_directory, write_text_utf8


def run() -> int:
    root = Path(__file__).resolve().parent
    input_file = root / "input" / "project_info.yaml"
    output_dir = root / "output"

    try:
        project_info = load_project_info(input_file)
    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
        return 1
    except ConfigError as e:
        print(f"[ERROR] {e}")
        return 1

    ensure_directory(output_dir)

    scale = calculate_scale_review(project_info)
    program_table = generate_program_table(project_info, scale.max_gfa_m2)

    write_text_utf8(output_dir / "01_project_brief.md", generate_project_brief(project_info))

    pd.DataFrame(
        [
            {
                "max_building_area_m2": round(scale.max_building_area_m2, 2),
                "max_gfa_m2": round(scale.max_gfa_m2, 2),
                "possible_floor_count": scale.possible_floor_count,
                "average_floor_area_m2": round(scale.average_floor_area_m2, 2),
            }
        ]
    ).to_csv(output_dir / "02_scale_review.csv", index=False, encoding="utf-8")

    pd.DataFrame(program_table).to_csv(output_dir / "03_program_area_table.csv", index=False, encoding="utf-8")
    write_text_utf8(output_dir / "04_site_strategy.md", generate_site_strategy(project_info))
    write_text_utf8(output_dir / "05_massing_strategies.md", generate_massing_strategies(project_info))
    write_text_utf8(output_dir / "06_concept_candidates.md", generate_concept_candidates(project_info))
    write_text_utf8(output_dir / "07_diagram_brief.md", generate_diagram_brief(project_info))
    write_text_utf8(output_dir / "08_executive_summary.md", generate_executive_summary(project_info))
    write_text_utf8(output_dir / "09_gamma_prompt.md", generate_gamma_prompt(project_info))

    print("[INFO] Outputs generated in output/")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
