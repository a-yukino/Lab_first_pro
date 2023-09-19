import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('clean_data.csv',encoding='shift_jis')

st.title('バレーボールW杯出場女子選手のデータ一覧')
st.write(df)

st.write('国別のデータ')

@st.cache
def load_data1():
    data1 = pd.read_csv('pro_1.csv', encoding='utf-8')
    return data1
data1 = load_data1()
if 'show_data1' not in st.session_state:
    st.session_state.show_data1 = False
if st.button("ロシア"):
    st.session_state.show_data1 = not st.session_state.show_data1  # クリックごとに表示状態をトグル
if st.session_state.show_data1:
    st.write("ロシア代表のデータ")
    st.write(data1)
else:
    st.write("")
    
@st.cache
def load_data2():
    data2 = pd.read_csv('pro_2.csv', encoding='utf-8')
    return data2
data = load_data2()
if 'show_data2' not in st.session_state:
    st.session_state.show_data2 = False
if st.button("ブラジル"):
    st.session_state.show_data2 = not st.session_state.show_data2  # クリックごとに表示状態をトグル
if st.session_state.show_data2:
    st.write("ブラジル代表のデータ")
    st.write(data2)
else:
    st.write("")
