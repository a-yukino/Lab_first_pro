import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('clean_data.csv',encoding='shift_jis')

st.title('バレーボールW杯出場女子選手のデータ一覧')
st.write(df)

st.write('国別のデータ')

# セッション変数を初期化
if 'button1_clicked' not in st.session_state:
    st.session_state.button1_clicked = False
if 'button2_clicked' not in st.session_state:
    st.session_state.button2_clicked = False
if 'button3_clicked' not in st.session_state:
    st.session_state.button3_clicked = False
if 'butto4_clicked' not in st.session_state:
    st.session_state.button4_clicked = False
if 'button5_clicked' not in st.session_state:
    st.session_state.button5_clicked = False
if 'button6_clicked' not in st.session_state:
    st.session_state.button6_clicked = False
if 'button7_clicked' not in st.session_state:
    st.session_state.button7_clicked = False
if 'button8_clicked' not in st.session_state:
    st.session_state.button8_clicked = False
if 'button9_clicked' not in st.session_state:
    st.session_state.button9_clicked = False
if 'button10_clicked' not in st.session_state:
    st.session_state.button10_clicked = False
if 'button11_clicked' not in st.session_state:
    st.session_state.button11_clicked = False
if 'button12_clicked' not in st.session_state:
    st.session_state.button12_clicked = False


if st.button("ロシア"):
    df = pd.read_csv('pro_1.csv',encoding='utf-8')
    st.session_state.button1_clicked = st.write(df)
if st.button("ブラジル"):
    df = pd.read_csv('pro_2.csv',encoding='utf-8')
    st.session_state.button2_clicked = st.write(df)
if st.button("日本"):
    df = pd.read_csv('pro_3.csv',encoding='utf-8')
    st.session_state.button3_clicked = st.write(df)
if st.button("ブルガリア"):
    df = pd.read_csv('pro_4.csv',encoding='utf-8')
    st.session_state.button4_clicked = st.write(df)
if st.button("セルビア"):
    df = pd.read_csv('pro_5.csv',encoding='utf-8')
    st.session_state.button5_clicked = st.write(df)
if st.button("メキシコ"):
    df = pd.read_csv('pro_6.csv',encoding='utf-8')
    st.session_state.button6_clicked = st.write(df)
if st.button("キューバ"):
    df = pd.read_csv('pro_7.csv',encoding='utf-8')
    st.session_state.button7_clicked = st.write(df)
if st.button("中国"):
    df = pd.read_csv('pro_8.csv',encoding='utf-8')
    st.session_state.button8_clicked = st.write(df)
if st.button("エジプト"):
    df = pd.read_csv('pro_9.csv',encoding='utf-8')
    st.session_state.button9_clicked = st.write(df)
if st.button("ペルー"):
    df = pd.read_csv('pro_10.csv',encoding='utf-8')
    st.session_state.button10_clicked = st.write(df)
if st.button("イタリア"):
    df = pd.read_csv('pro_11.csv',encoding='utf-8')
    st.session_state.button11_clicked = st.write(df)
if st.button("トルコ"):
    df = pd.read_csv('pro_12.csv',encoding='utf-8')
    st.session_state.button12_clicked = st.write(df)
