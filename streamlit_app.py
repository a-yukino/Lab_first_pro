import streamlit as st
import pandas as pd

# CSVファイルの読み込み
@st.cache  # データをキャッシュして高速化
def load_data():
    data = pd.read_csv('pro_1.csv', encoding='utf-8')  # CSVファイルのパスを指定
    return data

data = load_data()

# ボタンの表示
if st.button("データを表示/非表示"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  # 初回クリック時に変数を初期化
    st.session_state.show_data = not st.session_state.show_data  # ステートを切り替え

# データの表示/非表示
if st.session_state.show_data:
    st.write("CSVデータの表示:")
    st.write(data)
else:
    st.write("CSVデータは非表示です。")
