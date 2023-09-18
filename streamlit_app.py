import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('clean_data.csv',encoding='shift_jis')

st.title('バレーボールW杯出場女子選手のデータ一覧')
st.write(df)

st.write('国別のデータ')

if st.button('ロシア'):
    df = pd.read_csv('pro1.csv',encoding='shift_jis')
    st.write(df)
if st.button('ブラジル'):
    df = pd.read_csv('pro2.csv',encoding='shift_jis')
    st.write(df)
if st.button('日本'):
    df = pd.read_csv('pro3.csv',encoding='shift_jis')
    st.write(df)
if st.button('ブルガリア'):
    df = pd.read_csv('pro4.csv',encoding='shift_jis')
    st.write(df)
if st.button('セルビア'):
    df = pd.read_csv('pro5.csv',encoding='shift_jis')
    st.write(df)
if st.button('メキシコ'):
    df = pd.read_csv('pro6.csv',encoding='shift_jis')
    st.write(df)
if st.button('キューバ'):
    df = pd.read_csv('pro7.csv',encoding='shift_jis')
    st.write(df)
if st.button('中国'):
    df = pd.read_csv('pro8.csv',encoding='shift_jis')
    st.write(df)
if st.button('エジプト'):
    df = pd.read_csv('pro9.csv',encoding='shift_jis')
    st.write(df)
if st.button('ペルー'):
    df = pd.read_csv('pro10.csv',encoding='shift_jis')
    st.write(df)
if st.button('イタリア'):
    df = pd.read_csv('pro11.csv',encoding='shift_jis')
    st.write(df)
if st.button('トルコ'):
    df = pd.read_csv('pro12.csv',encoding='shift_jis')
    st.write(df)
