from __future__ import annotations

from typing import Dict


def generate_project_brief(project_info: Dict) -> str:
    return "\n".join(
        [
            f"# 01 Project Brief - {project_info['project_name']}",
            "",
            f"- 위치: {project_info['site_location']}",
            f"- 용도지역: {project_info['zoning']}",
            f"- 목표 용도: {project_info['target_use']}",
            f"- 보고 대상: {project_info['report_target']}",
            "",
            "## Client Requests",
            *[f"- {req}" for req in project_info.get("client_requests", [])],
        ]
    )


def generate_executive_summary(project_info: Dict) -> str:
    return "\n".join(
        [
            f"# 08 Executive Summary - {project_info['project_name']}",
            "",
            f"본 기획설계 초안은 {project_info['site_location']} 대지를 대상으로 하며, "
            f"{project_info['target_use']} 개발을 목표로 한다.",
            "입력 수치 기준 규모 검토 결과를 바탕으로 프로그램 배분, 대지 대응, "
            "매스 대안 및 컨셉 후보를 도출하였다.",
            "해당 문서는 의사결정용 초안이며, 상세 법규 검토 및 사업성 검토는 후속 단계에서 수행한다.",
        ]
    )


def generate_gamma_prompt(project_info: Dict) -> str:
    return "\n".join(
        [
            f"# 09 Gamma/PPT Prompt - {project_info['project_name']}",
            "",
            "다음 내용을 바탕으로 임원 보고용 12장 분량의 프레젠테이션을 생성하라.",
            "톤앤매너: 전문적, 간결, 시각 중심.",
            "",
            "포함 슬라이드:",
            "1) 프로젝트 개요",
            "2) 대지 및 맥락 분석",
            "3) 규모 검토",
            "4) 프로그램 면적 배분",
            "5) 대지 전략",
            "6) 매스 전략 3안",
            "7) 컨셉 후보 5개 비교",
            "8) 추천안 및 기대효과",
            "9) 향후 검토 과제",
        ]
    )
