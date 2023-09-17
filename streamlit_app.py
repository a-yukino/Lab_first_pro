import streamlit as st
import pandas as pd
import numpy as np

df1 = pd.read_csv('clean_data.csv',encoding='shift_jis')
df2 = pd.read_csv('pro1.csv',encoding='shift_jis')
df3 = pd.read_csv('pro2.csv',encoding='shift_jis')
df4 = pd.read_csv('pro3.csv',encoding='shift_jis')
df5 = pd.read_csv('pro4.csv',encoding='shift_jis')
df6 = pd.read_csv('pro5.csv',encoding='shift_jis')
df7 = pd.read_csv('pro6.csv',encoding='shift_jis')
df8 = pd.read_csv('pro7.csv',encoding='shift_jis')
df9 = pd.read_csv('pro8.csv',encoding='shift_jis')
df10 = pd.read_csv('pro9.csv',encoding='shift_jis')
df11 = pd.read_csv('pro10.csv',encoding='shift_jis')
df12 = pd.read_csv('pro11.csv',encoding='shift_jis')
df13 = pd.read_csv('pro12.csv',encoding='shift_jis')

st.title('バレーボールW杯出場女子選手のデータ一覧')
st.write(df1)

st.write('国別のデータ')
if st.button('ロシア'):
  st.write(df2)
if st.button('ブラジル'):
  st.write(df3)
if st.button('日本'):
  st.write(df4)
if st.button('ブルガリア'):
  st.write(df5)
if st.button('セルビア'):
  st.write(df6)
if st.button('メキシコ'):
  st.write(df7)
if st.button('キューバ'):
  st.write(df8)
if st.button('中国'):
  st.write(df9)
if st.button('エジプト'):
  st.write(df10)
if st.button('ペルー'):
  st.write(df11)
if st.button('イタリア'):
  st.write(df12)
if st.button('トルコ'):
  st.write(df13)
