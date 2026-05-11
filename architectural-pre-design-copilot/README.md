# architectural-pre-design-copilot

## 1. 프로젝트 개요
`input/project_info.yaml`의 건축 프로젝트 기본 정보를 바탕으로 초기 기획설계 산출물을 자동 생성하는 CLI 도구입니다.

## 2. 설치 방법
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## 3. 실행 방법
```bash
python main.py
```

## 4. project_info.yaml 작성 예시
`input/project_info.yaml`:
```yaml
project_name: "Sample Mixed-use Project"
site_location: "Seoul, Korea"
site_area_m2: 8500
zoning: "General Commercial"
building_coverage_ratio: 60
floor_area_ratio: 550
max_height_m: 120
floor_height_m: 4.2
target_use: "Mixed-use (Office + Retail)"
target_programs:
  - name: "Office"
    ratio: 65
  - name: "Retail"
    ratio: 25
  - name: "Community"
    ratio: 10
site_context:
  strengths: ["Subway station within 300m"]
  weaknesses: ["High noise from main boulevard"]
  opportunities: ["Public plaza linkage potential"]
  threats: ["Competing nearby developments"]
client_requests:
  - "Iconic facade"
report_target: "Executive board"
```

## 5. 출력 파일 설명
- `output/01_project_brief.md`: 프로젝트 개요 및 발주처 요청사항
- `output/02_scale_review.csv`: 규모 검토 결과(건축면적/연면적/가능층수)
- `output/03_program_area_table.csv`: 프로그램 면적 배분표
- `output/04_site_strategy.md`: 대지 조건 분석 및 전략
- `output/05_massing_strategies.md`: 매스 전략 3안
- `output/06_concept_candidates.md`: 컨셉 후보 5개 및 비평
- `output/07_diagram_brief.md`: 다이어그램 구성안
- `output/08_executive_summary.md`: 임원보고용 요약문
- `output/09_gamma_prompt.md`: Gamma/PPT 제작 프롬프트

## 6. 테스트 실행 방법
```bash
pytest -q
```
