import streamlit as st
import pandas as pd

# CSVファイルの読み込み
@st.cache
def load_data():
    data = pd.read_csv('pro_1.csv', encoding='utf-8')
    return data

data = load_data()

# ボタンのクリック状態を管理する変数
if 'show_data' not in st.session_state:
    st.session_state.show_data = False

# ボタンでデータの表示/非表示を切り替え
if st.button("ロシア"):
    st.session_state.show_data = not st.session_state.show_data  # クリックごとに表示状態をトグル

# データの表示/非表示
if st.session_state.show_data:
    st.write("ロシア代表のデータ")
    st.write(data)
else:
    st.write("")
