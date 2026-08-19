# 데이터 출처

## weather_daily.csv

- 출처: NASA POWER Daily API
- 위치: 울산대학교 인근 격자점
- 기간: 2024-01-01~2024-12-31
- 설명: 위성 관측과 기상 재분석 모형을 이용한 격자 자료이며, 현장 관측소 측정값과는 구분해야 합니다.
- 문서: https://power.larc.nasa.gov/docs/services/api/temporal/daily/

## ulsan_weather_points.csv

- 출처: Open-Meteo Historical Weather API
- 위치: 울산 5개 구·군 안의 대표 연습 좌표
- 기간: 2024-01-01~2024-12-31
- 설명: ERA5·ERA5-Land 계열 재분석 격자값을 연평균기온·연간강수량·일최대풍속 평균으로 요약했습니다. 현장 관측소 측정값과는 구분해야 합니다.
- 문서: https://open-meteo.com/en/docs/historical-weather-api
- 이용조건: CC BY 4.0

## building_energy.csv

- 출처: UCI Machine Learning Repository, Energy Efficiency
- 768개 건물 형상 시뮬레이션의 외피 조건과 냉난방 부하
- DOI: https://doi.org/10.24432/C51307
- 이용조건: CC BY 4.0

## concrete_strength.csv

- 출처: UCI Machine Learning Repository, Concrete Compressive Strength
- 1,030개 배합의 재료량·재령·압축강도
- DOI: https://doi.org/10.24432/C5PK67
- 이용조건: CC BY 4.0

## occupancy_detection.csv

- 출처: UCI Machine Learning Repository, Occupancy Detection
- 온도·습도·조도·CO₂와 사진으로 확인한 실내 재실 상태
- 원자료의 학습·평가 파일 구분을 `source_split` 열에 보존
- DOI: https://doi.org/10.24432/C5X01N
- 이용조건: CC BY 4.0

## korea_adm2_temperature_climatology.csv

- 행정경계 출처: geoBoundaries KOR ADM2, 2020 boundary representation
- 기온 출처: NASA POWER Climatology Regional API, T2M 0.5° 격자
- 설명: 각 시·군·구 대표 중심점에서 가장 가까운 NASA POWER 격자의 연평균기온을 연결했습니다.
- 주의: 행정구역 전체의 지상 관측소 평균이 아니며, 공간통계 계산구조를 익히기 위한 공개자료 결합본입니다.
- NASA POWER 문서: https://power.larc.nasa.gov/docs/services/api/temporal/climatology/

## korea_adm2_simplified.geojson

- 출처: geoBoundaries KOR ADM2, 2020 boundary representation
- 대한민국 시·군·구 228개 단순화 경계
- 이용조건: CC BY 3.0
- API: https://www.geoboundaries.org/api/current/gbOpen/KOR/ADM2/

## ulsan_districts.geojson

- 출처: geoBoundaries KOR ADM2, 2020 boundary representation
- 울산광역시 5개 구·군만 추출한 단순화 경계
- 이용조건: CC BY 3.0
- API: https://www.geoboundaries.org/api/current/gbOpen/KOR/ADM2/

## air_quality.csv

- 결측·중복·필터링을 연습하기 위해 구성한 가상 대기질 표입니다.
- 실제 지역의 대기 상태나 정책 판단에는 사용하지 않습니다.

## kma_ultra_short_forecast_sample.json

- 구조: 기상청 APIHub 초단기예보 조회서비스의 JSON 응답 구조
- 항목: 기온, 습도, 1시간 강수량, 하늘상태, 강수형태, 풍속
- 위치: 울산대학교 인근 기상청 격자 nx=101, ny=84
- 설명: API 키나 네트워크 상태와 관계없이 JSON→표→그래프→웹 화면 변환을 확인하기 위한 샘플 응답입니다. 현재 시각의 실제 예보로 사용하지 않습니다.
- 문서: https://apihub.kma.go.kr/apiList.do?seqApi=10
- 공공데이터포털: https://www.data.go.kr/data/15084084/openapi.do
