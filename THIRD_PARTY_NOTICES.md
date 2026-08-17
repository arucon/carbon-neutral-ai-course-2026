# 데이터 출처와 제3자 자료 고지

이 문서는 `offline_data.zip`에 포함된 공개자료의 출처, 이용조건과 수업용 변환을 기록합니다. 과정 자체의 CC BY 4.0 라이선스가 아래 제3자 자료의 원래 이용조건을 대체하지 않습니다.

## UCI Machine Learning Repository

다음 세 데이터셋은 UCI 페이지에서 CC BY 4.0으로 제공됩니다. 배포본에는 공식 압축파일에서 추출한 CSV를 내용 변경 없이 포함했습니다.

| 포함 경로 | 데이터셋 | 공식 페이지 |
|---|---|---|
| `data/bike/hour.csv` | Bike Sharing | https://doi.org/10.24432/C5W894 |
| `data/steel/Steel_industry_data.csv` | Steel Industry Energy Consumption | https://doi.org/10.24432/C52G8C |
| `data/ai4i/ai4i2020.csv` | AI4I 2020 Predictive Maintenance | https://doi.org/10.24432/C5HS5C |

License: https://creativecommons.org/licenses/by/4.0/

## CO₂와 STIRPAT snapshot

- 포함 경로: `data/co2/owid_co2_sample.csv`, `data/methods/stirpat_panel.csv`
- CO₂ 원자료: Global Carbon Project, Global Carbon Budget; Our World in Data 가공
- 경제지표: World Bank, World Development Indicators; Our World in Data의 열 이름·국가코드 정리
- 수업용 처리: 지정 국가·연도 선택, canonical 열 이름 적용, 총배출량 단위를 tonnes로 통일, STIRPAT 분석용 국가–연도 결합
- 공식 자료: https://github.com/owid/co2-data
- Global Carbon Budget: https://globalcarbonbudget.org/
- World Bank 이용조건: https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets
- OWID 재사용 안내: https://ourworldindata.org/how-to-use-our-world-in-data

보고서나 논문에서는 OWID뿐 아니라 표의 각 지표를 생산한 Global Carbon Project와 World Bank도 함께 인용해야 합니다.

## Kaya–LMDI snapshot

- 포함 경로: `data/methods/kaya_lmdi_sample.csv`
- 범위: Germany, Japan, South Korea, United States; 1990–2024; 140 country-year rows
- CO₂ 총량·1인당 CO₂: Global Carbon Project/OWID
- 1인당 GDP: World Bank/OWID, constant 2021 international dollars
- 1차에너지 소비량: U.S. Energy Information Administration International Energy Data
- EIA 변환: 연간 `Total energy consumption`을 TJ에서 TWh로 변환 (`TWh = TJ / 3600`)
- 독일 1990년: EIA 통합 독일 계열의 결측을 보간하지 않고 EIA East Germany(`DDR`)와 West Germany(`DEUW`) 1990년 값을 합산
- EIA 계열: `INTL.44-2-DEU-TJ.A`, `INTL.44-2-JPN-TJ.A`, `INTL.44-2-KOR-TJ.A`, `INTL.44-2-USA-TJ.A`, `INTL.44-2-DDR-TJ.A`, `INTL.44-2-DEUW-TJ.A`
- EIA 공식 bulk archive: https://www.eia.gov/opendata/bulk/INTL.zip
- EIA 재사용 정책: https://www.eia.gov/about/copyrights_reuse.php

선택한 EIA 계열은 bulk metadata에서 `copyright: None`, `source: EIA, U.S. Energy Information Administration`으로 표시됩니다. EIA가 직접 생산한 미국 정부 데이터는 public domain이며, EIA는 출처와 게시시점 표기를 권장합니다. EIA 로고는 포함하거나 재사용하지 않았습니다.

## 생성 기록

- source access date: 2026-08-17
- `kaya_lmdi_sample.csv` SHA-256: `e1de73357bba5340342c51d33ec2040db2fdd6902c2a36cf52894b57805f105f`
- EIA `INTL.zip` SHA-256 at access: `6e7878db3fa961f71dcb10d10104a499536a5dfcfe6af1918c9672f18806151d`

공개자료의 최신 버전은 시간이 지나며 바뀔 수 있습니다. 수업 재현에는 배포본의 고정 snapshot을 사용하고, 최신 자료로 갱신했다면 접근일과 변경된 결과를 별도로 기록합니다.
