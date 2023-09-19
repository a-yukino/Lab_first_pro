import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('clean_data.csv',encoding='shift_jis')

st.title('バレーボールW杯出場女子選手のデータ一覧')
st.write(df)

st.write('国別のデータ')

if 'button1_clicked' not in st.session_state:
    st.session_state.button1_clicked = pd.read_csv('pro_1.csv',encoding='utf-8')
    if st.button("ロシア"):
        st.session_state.button1_clicked = not st.session_state.button1_clicked
    st.write(f"ロシアの代表選手のデータ: {st.session_state.button1_clicked}")
    
if 'button2_clicked' not in st.session_state:
    st.session_state.button2_clicked = pd.read_csv('pro_2.csv',encoding='utf-8')
    if st.button("ブラジル"):
        st.session_state.button2_clicked = not st.session_state.button2_clicked
    st.write(f"ブラジルの代表選手のデータ: {st.session_state.button2_clicked}")
