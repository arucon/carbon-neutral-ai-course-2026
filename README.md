# Python 기반 탄소중립 데이터·AI 연구 실습

## GitHub에서 내려받기

1. [최신 배포본](https://github.com/arucon/carbon-neutral-ai-course-2026/releases/latest)을 엽니다.
2. **Assets**에서 `carbon-neutral-ai-course-2026.zip`을 내려받습니다.
3. ZIP 파일의 압축을 완전히 푼 뒤, 생성된 과정 폴더 전체를 IDE에서 엽니다.

GitHub의 **Code → Download ZIP**도 사용할 수 있지만, 수업에서는 버전이 고정된 Releases 배포본을 권장합니다.

## 프로그램을 처음 설치하는 경우

Python **3.12**를 권장합니다. IDE는 아래에서 **하나만 선택**합니다. 처음 사용하는 경우 PyCharm을 권장합니다.

- [PyCharm 다운로드](https://www.jetbrains.com/pycharm/download/) - 기본 권장
- [VS Code 다운로드](https://code.visualstudio.com/download) - 기존 사용자를 위한 대안
- [Python 다운로드](https://www.python.org/downloads/) - Python이 설치되어 있지 않을 때
- VS Code 선택 시: [Python 확장](https://marketplace.visualstudio.com/items?itemName=ms-python.python) · [Jupyter 확장](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

설치 화면과 Python 환경 선택 방법은 `00_setup.ipynb`의 첫 부분에 순서대로 적혀 있습니다.

`offline_data.zip`은 수업 데이터의 네트워크 장애에 대비한 파일입니다. Python package를 처음 설치하려면 인터넷 연결 또는 강사가 미리 준비한 환경이 필요합니다.

## 시작 방법

1. 배포 ZIP 파일의 압축을 완전히 풉니다.
2. PyCharm 또는 VS Code에서 압축을 푼 과정 폴더 전체를 엽니다.
3. `00_setup.ipynb`를 실행해 Python package·데이터·ChatGPT 설정을 마칩니다.
4. 각 교시에는 `follow`를 먼저 열고, 완료 후 `practice`로 이동합니다.

각 교시는 강의를 보며 실행하는 `follow`와 같은 방법을 다른 데이터·조건에 적용하는 `practice` 순서로 진행합니다.

| 교시 | 주제 | 강의를 보며 따라 하기 | 독립 실습 |
|---:|---|---|---|
| 1교시 | pandas와 연구 데이터셋 | [01_pandas_research_data_follow.ipynb](day1/01_pandas_research_data_follow.ipynb) | [01_pandas_research_data_practice.ipynb](day1/01_pandas_research_data_practice.ipynb) |
| 2교시 | Tidy Data와 연구 시각화 | [02_tidy_data_visualization_follow.ipynb](day1/02_tidy_data_visualization_follow.ipynb) | [02_tidy_data_visualization_practice.ipynb](day1/02_tidy_data_visualization_practice.ipynb) |
| 3교시 | Kaya Identity와 LMDI 분해분석 | [03_kaya_lmdi_follow.ipynb](day1/03_kaya_lmdi_follow.ipynb) | [03_kaya_lmdi_practice.ipynb](day1/03_kaya_lmdi_practice.ipynb) |
| 4교시 | STIRPAT과 로그회귀 | [04_stirpat_regression_follow.ipynb](day1/04_stirpat_regression_follow.ipynb) | [04_stirpat_regression_practice.ipynb](day1/04_stirpat_regression_practice.ipynb) |
| 5교시 | scikit-learn과 예측 Pipeline | [05_sklearn_pipeline_follow.ipynb](day1/05_sklearn_pipeline_follow.ipynb) | [05_sklearn_pipeline_practice.ipynb](day1/05_sklearn_pipeline_practice.ipynb) |
| 6교시 | 모델 평가와 Random Forest | [06_model_evaluation_random_forest_follow.ipynb](day1/06_model_evaluation_random_forest_follow.ipynb) | [06_model_evaluation_random_forest_practice.ipynb](day1/06_model_evaluation_random_forest_practice.ipynb) |
| 7교시 | 시계열 검증과 정보 누수 | [07_time_series_validation_follow.ipynb](day2/07_time_series_validation_follow.ipynb) | [07_time_series_validation_practice.ipynb](day2/07_time_series_validation_practice.ipynb) |
| 8교시 | Gradient Boosting 시계열 예측 | [08_gradient_boosting_forecasting_follow.ipynb](day2/08_gradient_boosting_forecasting_follow.ipynb) | [08_gradient_boosting_forecasting_practice.ipynb](day2/08_gradient_boosting_forecasting_practice.ipynb) |
| 9교시 | 예지보전 자료를 이용한 상태 분류 | [09_predictive_maintenance_classification_follow.ipynb](day2/09_predictive_maintenance_classification_follow.ipynb) | [09_predictive_maintenance_classification_practice.ipynb](day2/09_predictive_maintenance_classification_practice.ipynb) |
| 10교시 | 불균형 데이터·임계값·모델 설명 | [10_imbalanced_threshold_explanation_follow.ipynb](day2/10_imbalanced_threshold_explanation_follow.ipynb) | [10_imbalanced_threshold_explanation_practice.ipynb](day2/10_imbalanced_threshold_explanation_practice.ipynb) |
| 11교시 | 연구 문제 정의와 분석 스프린트 | [11_research_sprint_follow.ipynb](day2/11_research_sprint_follow.ipynb) | [11_research_sprint_practice.ipynb](day2/11_research_sprint_practice.ipynb) |
| 12교시 | 연구 결과 보고와 재현성 | [12_reporting_reproducibility_follow.ipynb](day2/12_reporting_reproducibility_follow.ipynb) | [12_reporting_reproducibility_practice.ipynb](day2/12_reporting_reproducibility_practice.ipynb) |

## 폴더에서 직접 열 파일

- `00_setup.ipynb`: 최초 1회 실행
- `day1/*_follow.ipynb`, `day2/*_follow.ipynb`: 강사의 시연과 같은 순서로 실행하는 파일
- `day1/*_practice.ipynb`, `day2/*_practice.ipynb`: 다른 데이터·조건으로 직접 적용하는 파일
- `requirements.txt`: Python package 목록
- `offline_data.zip`: 인터넷 장애 시 0교시가 자동으로 사용하는 예비자료. 직접 열지 않습니다.
- `LICENSE`, `THIRD_PARTY_NOTICES.md`: 강의자료 라이선스와 공개 데이터의 출처·이용조건

0교시 실행 후 생성되는 `data` 폴더는 Notebook이 자동으로 사용합니다.
