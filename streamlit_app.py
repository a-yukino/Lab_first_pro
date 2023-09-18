import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('clean_data.csv',encoding='shift_jis')

st.title('バレーボールW杯出場女子選手のデータ一覧')
st.write(df)

st.write('国別のデータ')

if st.button('ロシア'):
    df = pd.read_csv('pro_1.csv',encoding='shift_jis')
    st.write(df)
if st.button('ブラジル'):
    df = pd.read_csv('pro_2.csv',encoding='shift_jis')
    st.write(df)
if st.button('日本'):
    df = pd.read_csv('pro_3.csv',encoding='shift_jis')
    st.write(df)
if st.button('ブルガリア'):
    df = pd.read_csv('pro_4.csv',encoding='shift_jis')
    st.write(df)
if st.button('セルビア'):
    df = pd.read_csv('pro_5.csv',encoding='shift_jis')
    st.write(df)
if st.button('メキシコ'):
    df = pd.read_csv('pro_6.csv',encoding='shift_jis')
    st.write(df)
if st.button('キューバ'):
    df = pd.read_csv('pro_7.csv',encoding='shift_jis')
    st.write(df)
if st.button('中国'):
    df = pd.read_csv('pro_8.csv',encoding='shift_jis')
    st.write(df)
if st.button('エジプト'):
    df = pd.read_csv('pro_9.csv',encoding='shift_jis')
    st.write(df)
if st.button('ペルー'):
    df = pd.read_csv('pro_10.csv',encoding='shift_jis')
    st.write(df)
if st.button('イタリア'):
    df = pd.read_csv('pro_11.csv',encoding='shift_jis')
    st.write(df)
if st.button('トルコ'):
    df = pd.read_csv('pro_12.csv',encoding='shift_jis')
    st.write(df)

st.markdown("# 国別の身長とスパイクの最高到達点の関係のグラフ")
st.markdown("### グラフデータ")
st.area_chart(data=pd.read_csv('pro_8.csv',encoding='shift_jis'),
              x="height",               # X軸
              y="spike",               # Y軸
              width=0,                     # 表示設定（幅）
              height=0,                    # 表示設定（高さ）
              use_container_width=True,    # True の場合、グラフの幅を列の幅に設定
              )
