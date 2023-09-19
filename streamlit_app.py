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
    if 'show_data1' not in st.session_state:
        st.session_state.show_data1 = True  
    st.session_state.show_data1 = not st.session_state.show_data1  
if st.session_state.show_data1:
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
    if 'show_data2' not in st.session_state:
        st.session_state.show_data2 = True  
    st.session_state.show_data2 = not st.session_state.show_data2  
if st.session_state.show_data2:
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
    if 'show_data3' not in st.session_state:
        st.session_state.show_data3 = True  
    st.session_state.show_data3 = not st.session_state.show_data3  
if st.session_state.show_data3:
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
    if 'show_data4' not in st.session_state:
        st.session_state.show_data4 = True  
    st.session_state.show_data4 = not st.session_state.show_data4  
if st.session_state.show_data4:
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
    if 'show_data5' not in st.session_state:
        st.session_state.show_data5 = True  
    st.session_state.show_data5 = not st.session_state.show_data5  
if st.session_state.show_data5:
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
    if 'show_data6' not in st.session_state:
        st.session_state.show_data6 = True  
    st.session_state.show_data6 = not st.session_state.show_data6 
if st.session_state.show_data6:
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
    if 'show_data7' not in st.session_state:
        st.session_state.show_data7 = True  
    st.session_state.show_data7 = not st.session_state.show_data7  
if st.session_state.show_data7:
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
    if 'show_data8' not in st.session_state:
        st.session_state.show_data8 = True  
    st.session_state.show_data8 = not st.session_state.show_data8  
if st.session_state.show_data8:
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
    if 'show_data9' not in st.session_state:
        st.session_state.show_data9 = True  
    st.session_state.show_data9 = not st.session_state.show_data9  
if st.session_state.show_data9:
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
    if 'show_data10' not in st.session_state:
        st.session_state.show_data10 = True  
    st.session_state.show_data10 = not st.session_state.show_data10  
if st.session_state.show_data10:
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
    if 'show_data11' not in st.session_state:
        st.session_state.show_data11 = True  
    st.session_state.show_data11 = not st.session_state.show_data11  
if st.session_state.show_data11:
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
    if 'show_data12' not in st.session_state:
        st.session_state.show_data12 = True  
    st.session_state.show_data12 = not st.session_state.show_data12  
if st.session_state.show_data12:
    st.write("トルコの代表選手のデータ")
    st.write(data)
else:
    st.write("　")
