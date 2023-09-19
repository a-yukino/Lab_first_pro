import streamlit as st
import pandas as pd

# CSVファイルの読み込み
@st.cache
def load_data():
    data = pd.read_csv('pro_1.csv', encoding='utf-8')
    return data
data = load_data()
show_data = False
if st.button("ロシア"):
    show_data = not show_data  
if show_data:
    st.write("CSVデータの表示:")
    st.write(data)
else:
    st.write("CSVデータは非表示です。")
