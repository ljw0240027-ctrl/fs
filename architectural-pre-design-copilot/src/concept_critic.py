from __future__ import annotations

from typing import Dict, List

CRITERIA = ["장소성", "프로그램성", "도면화 가능성", "차별성", "심사 전달력"]


def generate_concept_candidates(project_info: Dict) -> str:
    candidates: List[str] = [
        "Urban Lantern: 야간 경관과 공공성을 강화하는 빛의 랜드마크",
        "Layered Commons: 저층 공공 프로그램과 상부 업무영역의 수평적 레이어",
        "Green Terraces: 입체적 외부공간을 통한 친환경 업무/상업 복합체",
        "Porous Ground: 관통형 저층부로 도시 보행 흐름을 내부로 연계",
        "Civic Spine: 수직 코어를 공공 동선과 결합한 상징적 공간축",
    ]

    lines = [f"# 06 Concept Candidates - {project_info['project_name']}", ""]
    for i, candidate in enumerate(candidates, start=1):
        lines.append(f"## Concept {i}: {candidate}")
        lines.append("- 비평")
        for c in CRITERIA:
            lines.append(f"  - {c}: 중상 수준(초안) - 프로젝트 맥락 반영 가능")
        lines.append("")

    return "\n".join(lines)
