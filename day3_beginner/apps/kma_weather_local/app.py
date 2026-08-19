from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

from kma_client import (
    load_sample_payload,
    load_weather_or_sample,
    long_to_wide_frame,
    payload_to_long_frame,
    read_auth_key,
)


APP_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = APP_DIR.parents[1]
SAMPLE_PATH = PACKAGE_DIR / "data" / "kma_ultra_short_forecast_sample.json"
ENV_PATH = APP_DIR / ".env"

LOCATIONS = {
    "울산대학교": {"nx": 101, "ny": 84},
    "울산광역시 중심": {"nx": 102, "ny": 84},
    "서울광역시 중심": {"nx": 60, "ny": 127},
    "부산광역시 중심": {"nx": 98, "ny": 76},
}


@st.cache_data(ttl=600, show_spinner=False)
def get_weather(auth_key: str, nx: int, ny: int, use_sample: bool):
    if use_sample:
        payload = load_sample_payload(SAMPLE_PATH)
        first_item = payload["response"]["body"]["items"]["item"][0]
        return {
            "payload": payload,
            "source": "기상청 응답 형식 샘플",
            "base_date": str(first_item["baseDate"]),
            "base_time": str(first_item["baseTime"]),
            "message": "샘플 응답으로 화면 구성을 확인하고 있습니다.",
        }

    result = load_weather_or_sample(auth_key, nx, ny, SAMPLE_PATH)
    return {
        "payload": result.payload,
        "source": result.source,
        "base_date": result.base_date,
        "base_time": result.base_time,
        "message": result.message,
    }


st.set_page_config(page_title="기상청 초단기예보", page_icon="🌦️", layout="wide")
st.title("기상청 초단기예보 확인")
st.caption("격자 위치를 고르면 시간별 기온·습도·바람·강수 정보를 표와 그래프로 보여 줍니다.")

auth_key = read_auth_key(ENV_PATH)
location_name = st.sidebar.selectbox("확인할 위치", list(LOCATIONS))
selected_location = LOCATIONS[location_name]
use_sample = st.sidebar.checkbox("샘플 응답 사용", value=not bool(auth_key))

st.sidebar.write(
    {
        "nx": selected_location["nx"],
        "ny": selected_location["ny"],
        "API 키 저장 여부": bool(auth_key),
    }
)

weather = get_weather(
    auth_key,
    selected_location["nx"],
    selected_location["ny"],
    use_sample,
)
long_frame = payload_to_long_frame(weather["payload"])
forecast = long_to_wide_frame(long_frame)

st.info(f"{weather['source']} · 기준 {weather['base_date']} {weather['base_time']} · {weather['message']}")

first = forecast.iloc[0]
metric_columns = st.columns(4)
metric_columns[0].metric("기온", f"{first['기온(°C)']:.1f} °C")
metric_columns[1].metric("습도", f"{first['습도(%)']:.0f} %")
metric_columns[2].metric("풍속", f"{first['풍속(m/s)']:.1f} m/s")
metric_columns[3].metric("강수", str(first["1시간 강수량"]))

left, middle, right = st.columns(3)
with left:
    st.subheader("기온")
    st.line_chart(forecast.set_index("예보 시각")[["기온(°C)"]])
with middle:
    st.subheader("습도")
    st.line_chart(forecast.set_index("예보 시각")[["습도(%)"]])
with right:
    st.subheader("풍속")
    st.line_chart(forecast.set_index("예보 시각")[["풍속(m/s)"]])

st.subheader("시간별 예보표")
st.dataframe(forecast, width="stretch", hide_index=True)

csv_bytes = forecast.to_csv(index=False).encode("utf-8-sig")
st.download_button(
    "현재 표를 CSV로 저장",
    data=csv_bytes,
    file_name="kma_ultra_short_forecast.csv",
    mime="text/csv",
)

with st.expander("원래 API 항목 확인"):
    st.dataframe(
        long_frame[["forecast_at", "category", "항목", "fcstValue", "nx", "ny"]],
        width="stretch",
        hide_index=True,
    )

st.caption("자료: 기상청 APIHub 초단기예보 조회서비스")
