import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('clean_data.csv',encoding='shift_jis')

st.title('バレーボールW杯出場女子選手のデータ一覧')
st.write(df)

st.write('国別のデータ')

@st.cache
def load_data():
    data = pd.read_csv('pro_1.csv', encoding='utf-8')
    return data
data = load_data()
if 'show_data' not in st.session_state:
    st.session_state.show_data = False
if st.button("ロシア"):
    st.session_state.show_data = not st.session_state.show_data  # クリックごとに表示状態をトグル
if st.session_state.show_data:
    st.write("ロシア代表のデータ")
    st.write(data)
else:
    st.write("")

@st.cache
def load_data():
    data = pd.read_csv('pro_2.csv', encoding='utf-8')
    return data
data = load_data()
if 'show_data' not in st.session_state:
    st.session_state.show_data = False
if st.button("ブラジル"):
    st.session_state.show_data = not st.session_state.show_data  # クリックごとに表示状態をトグル
if st.session_state.show_data:
    st.write("ブラジル代表のデータ")
    st.write(data)
else:
    st.write("")
