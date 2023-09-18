import streamlit as st
import pandas as pd
import numpy as np

df_1 = pd.read_csv('clean_data.csv',encoding='shift_jis')
df_2 = pd.read_csv('pro1.csv',encoding='shift_jis')
df_3 = pd.read_csv('pro2.csv',encoding='shift_jis')
df_4 = pd.read_csv('pro3.csv',encoding='shift_jis')
df_5 = pd.read_csv('pro4.csv',encoding='shift_jis')
df_6 = pd.read_csv('pro5.csv',encoding='shift_jis')
df_7 = pd.read_csv('pro6.csv',encoding='shift_jis')
df_8 = pd.read_csv('pro7.csv',encoding='shift_jis')
df_9 = pd.read_csv('pro8.csv',encoding='shift_jis')
df_10 = pd.read_csv('pro9.csv',encoding='shift_jis')
df_11 = pd.read_csv('pro10.csv',encoding='shift_jis')
df_12 = pd.read_csv('pro11.csv',encoding='shift_jis')
df_13 = pd.read_csv('pro12.csv',encoding='shift_jis')

st.title('バレーボールW杯出場女子選手のデータ一覧')
st.write(df_1)

st.write('国別のデータ')

st.button('ロシア')
st.button('ブラジル')
st.button('日本')
st.button('ブルガリア')
st.button('セルビア')
st.button('メキシコ')
st.button('キューバ')
st.button('中国')
st.button('エジプト')
st.button('ペルー')
st.button('イタリア')
st.button('トルコ')
          
if st.button('ロシア'):
   st.write(df_2)
if st.button('ブラジル'):
   st.write(df_3)
if st.button('日本'):
   st.write(df_4)
if st.button('ブルガリア'):
   st.write(df_5)
if st.button('セルビア'):
   st.write(df_6)
if st.button('メキシコ'):
   st.write(df_7)
if st.button('キューバ'):
   st.write(df_8)
if st.button('中国'):
   st.write(df_9)
if st.button('エジプト'):
   st.write(df_10)
if st.button('ペルー'):
   st.write(df_11)
if st.button('イタリア'):
   st.write(df_12)
if st.button('トルコ'):
   st.write(df_13)
