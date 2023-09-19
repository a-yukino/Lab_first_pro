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
if st.button("ロシア"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  
    st.session_state.show_data = not st.session_state.show_data  
if st.session_state.show_data:
    st.write("ロシアの代表選手のデータ")
    st.write(data)
else:
    st.write("　")

@st.cache  
def load_data():
    data = pd.read_csv('pro_2.csv', encoding='utf-8')  
    return data
data = load_data()
if st.button("ブラジル"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  
    st.session_state.show_data = not st.session_state.show_data  
if st.session_state.show_data:
    st.write("ブラジルの代表選手のデータ")
    st.write(data)
else:
    st.write("　")
    
@st.cache  
def load_data():
    data = pd.read_csv('pro_3.csv', encoding='utf-8')  
    return data
data = load_data()
if st.button("日本"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  
    st.session_state.show_data = not st.session_state.show_data  
if st.session_state.show_data:
    st.write("日本の代表選手のデータ")
    st.write(data)
else:
    st.write("　")

@st.cache  
def load_data():
    data = pd.read_csv('pro_4.csv', encoding='utf-8')  
    return data
data = load_data()
if st.button("ブルガリア"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  
    st.session_state.show_data = not st.session_state.show_data  
if st.session_state.show_data:
    st.write("ブルガリアの代表選手のデータ")
    st.write(data)
else:
    st.write("　")
    
@st.cache  
def load_data():
    data = pd.read_csv('pro_5.csv', encoding='utf-8')  
    return data
data = load_data()
if st.button("セルビア"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  
    st.session_state.show_data = not st.session_state.show_data  
if st.session_state.show_data:
    st.write("セルビアの代表選手のデータ")
    st.write(data)
else:
    st.write("　")
    
@st.cache  
def load_data():
    data = pd.read_csv('pro_6.csv', encoding='utf-8')  
    return data
data = load_data()
if st.button("メキシコ"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  
    st.session_state.show_data = not st.session_state.show_data  
if st.session_state.show_data:
    st.write("メキシコの代表選手のデータ")
    st.write(data)
else:
    st.write("　")
    
@st.cache  
def load_data():
    data = pd.read_csv('pro_7.csv', encoding='utf-8')  
    return data
data = load_data()
if st.button("キューバ"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  
    st.session_state.show_data = not st.session_state.show_data  
if st.session_state.show_data:
    st.write("キューバの代表選手のデータ")
    st.write(data)
else:
    st.write("　")

@st.cache  
def load_data():
    data = pd.read_csv('pro_8.csv', encoding='utf-8')  
    return data
data = load_data()
if st.button("中国"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  
    st.session_state.show_data = not st.session_state.show_data  
if st.session_state.show_data:
    st.write("中国の代表選手のデータ")
    st.write(data)
else:
    st.write("　")
    
@st.cache  
def load_data():
    data = pd.read_csv('pro_9.csv', encoding='utf-8')  
    return data
data = load_data()
if st.button("エジプト"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  
    st.session_state.show_data = not st.session_state.show_data  
if st.session_state.show_data:
    st.write("エジプトの代表選手のデータ")
    st.write(data)
else:
    st.write("　")

@st.cache  
def load_data():
    data = pd.read_csv('pro_10.csv', encoding='utf-8')  
    return data
data = load_data()
if st.button("ペルー"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  
    st.session_state.show_data = not st.session_state.show_data  
if st.session_state.show_data:
    st.write("ペルーの代表選手のデータ")
    st.write(data)
else:
    st.write("　")

@st.cache  
def load_data():
    data = pd.read_csv('pro_11.csv', encoding='utf-8')  
    return data
data = load_data()
if st.button("イタリア"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  
    st.session_state.show_data = not st.session_state.show_data  
if st.session_state.show_data:
    st.write("イタリアの代表選手のデータ")
    st.write(data)
else:
    st.write("　")

@st.cache  
def load_data():
    data = pd.read_csv('pro_12.csv', encoding='utf-8')  
    return data
data = load_data()
if st.button("トルコ"):
    if 'show_data' not in st.session_state:
        st.session_state.show_data = True  
    st.session_state.show_data = not st.session_state.show_data  
if st.session_state.show_data:
    st.write("トルコの代表選手のデータ")
    st.write(data)
else:
    st.write("　")
