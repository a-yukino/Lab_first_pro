import streamlit as st
import pandas as pd

# CSVファイルの読み込み
@st.cache
def load_data():
    data = pd.read_csv('pro_1.csv', encoding='utf-8')
    return data

data = load_data()

# ボタンと表示状態を格納する辞書
button_states = {}

# ボタンと表示状態の対応を作成
for column in data.columns:
    button_states[column] = st.button(f"表示/非表示: {column}", key=column)

# データの表示/非表示
for column, show_data in button_states.items():
    if show_data:
        st.write(f"CSVデータの表示: {column}")
        st.write(data[column])
