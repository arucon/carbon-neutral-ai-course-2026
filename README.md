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
4. Day 1·2는 `follow`를 먼저 열고 완료 후 `practice`로 이동합니다.
5. 초급 확장 과정은 `day3_beginner/notebooks/00_start_here.ipynb`부터 번호 순서대로 실행합니다.

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

## Day 3 초급 데이터 분석 22시간 과정

데이터 분석 경험이 적은 수강생을 위한 셀 단위 실습 과정입니다. 코드 셀 하나에서 한 가지 작업을 수행하고, 바로 다음 셀에서 표나 그림을 확인합니다. 데이터 읽기부터 통계, 회귀·분류, 기상자료와 지도, 종합 프로젝트까지 순서대로 이어집니다. 마지막에는 기상청 초단기예보 JSON을 pandas 표와 그래프로 바꾸고 로컬 Streamlit 웹앱에 연결합니다.

| 순서 | 주제 | Notebook |
|---:|---|---|
| 00 | Python 도구와 데이터 파일 확인 | [00_start_here.ipynb](day3_beginner/notebooks/00_start_here.ipynb) |
| 01 | CSV와 DataFrame | [01_csv_dataframe.ipynb](day3_beginner/notebooks/01_csv_dataframe.ipynb) |
| 02 | 조건에 맞는 데이터 선택 | [02_filter.ipynb](day3_beginner/notebooks/02_filter.ipynb) |
| 03 | 결측·중복·날짜 확인 | [03_cleaning.ipynb](day3_beginner/notebooks/03_cleaning.ipynb) |
| 04 | 이름별·월별 데이터 요약 | [04_groupby.ipynb](day3_beginner/notebooks/04_groupby.ipynb) |
| 05 | 막대·선·산점도와 분포 그림 | [05_visualization.ipynb](day3_beginner/notebooks/05_visualization.ipynb) |
| 06 | 위치 데이터와 지도 | [06_gis_basic.ipynb](day3_beginner/notebooks/06_gis_basic.ipynb) |
| 07 | 전공 연계 미니 프로젝트 | [07_project.ipynb](day3_beginner/notebooks/07_project.ipynb) |
| 08 | 상관관계와 산점도 | [08_correlation.ipynb](day3_beginner/notebooks/08_correlation.ipynb) |
| 09 | 반복 추출과 평균의 불확실성 | [09_bootstrap_uncertainty.ipynb](day3_beginner/notebooks/09_bootstrap_uncertainty.ipynb) |
| 10 | 두 집단 비교 | [10_two_group_comparison.ipynb](day3_beginner/notebooks/10_two_group_comparison.ipynb) |
| 11 | 여러 집단 비교 | [11_multiple_group_comparison.ipynb](day3_beginner/notebooks/11_multiple_group_comparison.ipynb) |
| 12 | 다중회귀 | [12_multiple_regression.ipynb](day3_beginner/notebooks/12_multiple_regression.ipynb) |
| 13 | 회귀 결과 점검 | [13_regression_diagnostics.ipynb](day3_beginner/notebooks/13_regression_diagnostics.ipynb) |
| 14 | 교차검증과 모형 비교 | [14_cross_validation.ipynb](day3_beginner/notebooks/14_cross_validation.ipynb) |
| 15 | 랜덤포레스트 결과 해석 | [15_random_forest_interpretation.ipynb](day3_beginner/notebooks/15_random_forest_interpretation.ipynb) |
| 16 | 로지스틱 회귀와 확률 | [16_logistic_probability.ipynb](day3_beginner/notebooks/16_logistic_probability.ipynb) |
| 17 | 분류 결과와 오류 확인 | [17_classification_evaluation.ipynb](day3_beginner/notebooks/17_classification_evaluation.ipynb) |
| 18 | PCA와 군집분석 | [18_pca_clustering.ipynb](day3_beginner/notebooks/18_pca_clustering.ipynb) |
| 19 | 기상자료의 시간 패턴 | [19_weather_time_patterns.ipynb](day3_beginner/notebooks/19_weather_time_patterns.ipynb) |
| 20 | 공간적으로 가까운 지역 비교 | [20_spatial_autocorrelation.ipynb](day3_beginner/notebooks/20_spatial_autocorrelation.ipynb) |
| 21 | 전공 데이터 분석 프로젝트 | [21_final_project.ipynb](day3_beginner/notebooks/21_final_project.ipynb) |
| 22 | 기상청 API에서 로컬 웹앱까지 | [22_kma_weather_local_webapp.ipynb](day3_beginner/notebooks/22_kma_weather_local_webapp.ipynb) |

사용 데이터의 출처와 이용조건은 [Day 3 데이터 출처](day3_beginner/data/DATA_SOURCES.md)에서 확인할 수 있습니다.

22번 프로젝트의 설치·실행 명령은 [로컬 웹앱 안내](day3_beginner/apps/kma_weather_local/README.md)에 정리되어 있습니다.

## 폴더에서 직접 열 파일

- `00_setup.ipynb`: 최초 1회 실행
- `day1/*_follow.ipynb`, `day2/*_follow.ipynb`: 강사의 시연과 같은 순서로 실행하는 파일
- `day1/*_practice.ipynb`, `day2/*_practice.ipynb`: 다른 데이터·조건으로 직접 적용하는 파일
- `day3_beginner/notebooks/*.ipynb`: 초급 확장 과정의 셀 단위 실습 파일
- `day3_beginner/data`: 초급 확장 과정에서 바로 읽는 데이터 파일
- `day3_beginner/apps/kma_weather_local`: 기상청 예보를 표시하는 로컬 Streamlit 웹앱
- `requirements.txt`: Python package 목록
- `offline_data.zip`: 인터넷 장애 시 0교시가 자동으로 사용하는 예비자료. 직접 열지 않습니다.
- `LICENSE`, `THIRD_PARTY_NOTICES.md`: 강의자료 라이선스와 공개 데이터의 출처·이용조건

0교시 실행 후 생성되는 `data` 폴더는 Notebook이 자동으로 사용합니다.
