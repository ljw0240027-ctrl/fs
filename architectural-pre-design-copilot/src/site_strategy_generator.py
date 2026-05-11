from __future__ import annotations

from typing import Dict


def generate_site_strategy(project_info: Dict) -> str:
    ctx = project_info["site_context"]
    strengths = ctx.get("strengths", [])
    weaknesses = ctx.get("weaknesses", [])
    opportunities = ctx.get("opportunities", [])
    threats = ctx.get("threats", [])

    lines = [
        f"# 04 Site Strategy - {project_info['project_name']}",
        "",
        "## 1) Issues (문제)",
    ]
    lines.extend([f"- {i}" for i in weaknesses + threats] or ["- (입력 필요)"])

    lines += ["", "## 2) Opportunities (기회)"]
    lines.extend([f"- {i}" for i in strengths + opportunities] or ["- (입력 필요)"])

    lines += ["", "## 3) Spatial Strategies (공간 전략)"]
    lines.extend(
        [
            "- 활성 보행축과 접한 저층부를 개방형 공공 프로그램으로 계획한다.",
            "- 소음원 반대 방향으로 주요 업무/주거 체류공간을 배치한다.",
            "- 코너 가시성을 활용해 상징적 진입부와 수직동선을 통합한다.",
            "- 외부공간과 1층 프로그램을 연계한 장소 활성화 전략을 적용한다.",
        ]
    )

    return "\n".join(lines)
