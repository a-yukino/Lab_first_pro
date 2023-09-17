import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('clean_data.csv',encoding='shift_jis')

st.title('バレーボールW杯出場女子選手のデータ一覧')
st.write(df)
