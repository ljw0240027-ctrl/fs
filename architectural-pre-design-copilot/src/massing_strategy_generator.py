from __future__ import annotations

from typing import Dict


def generate_massing_strategies(project_info: Dict) -> str:
    return "\n".join(
        [
            f"# 05 Massing Strategies - {project_info['project_name']}",
            "",
            "## Option A: Podium + Tower",
            "- 저층부 포디움으로 도시 활성화 기능을 집중하고 상부를 슬림 타워로 구성.",
            "- 장점: 명확한 조닝, 상업 가시성 우수.",
            "",
            "## Option B: Terraced Volume",
            "- 중고층부를 단계적으로 셋백하여 외부 테라스와 친환경 이미지를 강화.",
            "- 장점: 스카이라인 대응, 입면 다양성.",
            "",
            "## Option C: Courtyard Slab",
            "- 중정을 중심으로 한 판상형 매스로 채광과 커뮤니티 결절점을 확보.",
            "- 장점: 내부 환경 품질 향상, 명확한 동선 구조.",
        ]
    )
