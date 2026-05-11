from __future__ import annotations

from typing import Dict


def generate_diagram_brief(project_info: Dict) -> str:
    return "\n".join(
        [
            f"# 07 Diagram Brief - {project_info['project_name']}",
            "",
            "## 필수 다이어그램 구성",
            "1. 광역-도시 맥락 다이어그램 (접근성, 랜드마크, 보행축)",
            "2. 대지 분석 다이어그램 (일조, 소음, 조망, 진입체계)",
            "3. 프로그램 조닝 다이어그램 (수직/수평 배분)",
            "4. 매스 생성 프로세스 다이어그램 (3안 비교)",
            "5. 동선/피난 개념 다이어그램",
            "6. 오픈스페이스 및 공공성 전략 다이어그램",
        ]
    )
