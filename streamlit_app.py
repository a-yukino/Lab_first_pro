import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データの読み込み
@st.cache  # データをキャッシュして高速化
def load_data():
    data = pd.read_csv('pro_1.csv')  # データファイルのパスを指定
    return data

data = load_data()

# サイドバーにタイトルを表示
st.sidebar.title('データ分析アプリ')

# サイドバーでデータの表示/非表示を制御
if st.sidebar.checkbox('データを表示'):
    st.subheader('データの概要')
    st.write(data)

# サイドバーで散布図の表示/非表示を制御
if st.sidebar.checkbox('散布図を表示'):
    st.subheader('散布図')
    x_axis = st.selectbox('X軸を選択', data.columns)
    y_axis = st.selectbox('Y軸を選択', data.columns)

    # 散布図の作成
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_axis], data[y_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(plt)
