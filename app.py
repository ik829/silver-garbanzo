import streamlit as st
from datetime import datetime
import pytz

# 都市とタイムゾーンの辞書
cities = {
    "東京 (Tokyo)": "Asia/Tokyo",
    "ニューヨーク (New York)": "America/New_York",
    "ロンドン (London)": "Europe/London",
    "パリ (Paris)": "Europe/Paris",
    "シドニー (Sydney)": "Australia/Sydney",
    "ロサンゼルス (Los Angeles)": "America/Los_Angeles",
    "シンガポール (Singapore)": "Asia/Singapore",
    "ドバイ (Dubai)": "Asia/Dubai",
    "ベルリン (Berlin)": "Europe/Berlin",
    "モスクワ (Moscow)": "Europe/Moscow",
}

st.title("🕒 世界の現在時刻をまとめて表示")

# 複数都市を選択
selected_cities = st.multiselect("都市を選択してください：", list(cities.keys()), default=["東京 (Tokyo)", "ニューヨーク (New York)"])

# ボタンで表示
if st.button("現在時刻を表示"):
    for city in selected_cities:
        tz = pytz.timezone(cities[city])
        now = datetime.now(tz)
        st.write(f"🗺️ {city} の現在時刻：**{now.strftime('%Y-%m-%d %H:%M:%S')}**")

