import streamlit as st
import pandas as pd
import numpy as np

page = st.sidebar.selectbox("ページを選択", ("データセット", "戦略考察"))

def home_page():
    df = pd.read_csv('clean_data.csv',encoding='shift_jis')
    
    st.title('バレーボールW杯出場女子選手のデータ一覧')

    st.write(df)
    st.write('国別のデータ')
    
    @st.cache
    def load_data1():
        data1 = pd.read_csv('pro_1.csv', encoding='utf-8')
        return data1
    data1 = load_data1()    
    if 'show_data1' not in st.session_state:
        st.session_state.show_data1 = False
    if st.button("ロシア"):
        st.session_state.show_data1 = not st.session_state.show_data1  # クリックごとに表示状態をトグル
    if st.session_state.show_data1:
        st.write("ロシア代表のデータ")
        st.write(data1)
    else:
        st.write("")
    @st.cache
    def load_data2():
        data2 = pd.read_csv('pro_2.csv', encoding='utf-8')
        return data2
    data2 = load_data2()
    if 'show_data2' not in st.session_state:
        st.session_state.show_data2 = False
    if st.button("ブラジル"):
        st.session_state.show_data2 = not st.session_state.show_data2  # クリックごとに表示状態をトグル
    if st.session_state.show_data2:
        st.write("ブラジル代表のデータ")
        st.write(data2)
    else:
        st.write("")

    @st.cache
    def load_data3():
        data3 = pd.read_csv('pro_3.csv', encoding='utf-8')
        return data3
    data3 = load_data3()
    if 'show_data3' not in st.session_state:
        st.session_state.show_data3 = False
    if st.button("日本"):
        st.session_state.show_data3 = not st.session_state.show_data3  # クリックごとに表示状態をトグル
    if st.session_state.show_data3:
        st.write("日本代表のデータ")
        st.write(data3)
    else:
        st.write("")
    
    @st.cache
    def load_data4():
        data4 = pd.read_csv('pro_4.csv', encoding='utf-8')
        return data4
    data4 = load_data4()
    if 'show_data4' not in st.session_state:
        st.session_state.show_data4 = False
    if st.button("ブルガリア"):
        st.session_state.show_data4 = not st.session_state.show_data4  # クリックごとに表示状態をトグル
    if st.session_state.show_data4:
        st.write("ブルガリア代表のデータ")
        st.write(data4)
    else:
        st.write("")

    @st.cache
    def load_data5():
        data5 = pd.read_csv('pro_5.csv', encoding='utf-8')
        return data5
    data5 = load_data5()
    if 'show_data5' not in st.session_state:
        st.session_state.show_data5 = False
    if st.button("セルビア"):
        st.session_state.show_data5 = not st.session_state.show_data5  # クリックごとに表示状態をトグル
    if st.session_state.show_data5:
        st.write("セルビア代表のデータ")
        st.write(data5)
    else:
        st.write("")
    
    @st.cache
    def load_data6():
        data6 = pd.read_csv('pro_6.csv', encoding='utf-8')
        return data6
    data6 = load_data6()
    if 'show_data6' not in st.session_state:
        st.session_state.show_data6 = False
    if st.button("メキシコ"):
        st.session_state.show_data6 = not st.session_state.show_data6  # クリックごとに表示状態をトグル
    if st.session_state.show_data6:
        st.write("メキシコ代表のデータ")
        st.write(data6)
    else:
        st.write("")

    @st.cache
    def load_data7():
        data7 = pd.read_csv('pro_7.csv', encoding='utf-8')
        return data7
    data7 = load_data7()
    if 'show_data7' not in st.session_state:
        st.session_state.show_data7 = False
    if st.button("キューバ"):
        st.session_state.show_data7 = not st.session_state.show_data7  # クリックごとに表示状態をトグル
    if st.session_state.show_data7:
        st.write("キューバ代表のデータ")
        st.write(data7)
    else:
        st.write("")
    
    @st.cache
    def load_data8():
        data8 = pd.read_csv('pro_8.csv', encoding='utf-8')
        return data8
    data8 = load_data8()
    if 'show_data8' not in st.session_state:
        st.session_state.show_data8 = False
    if st.button("中国"):
        st.session_state.show_data8 = not st.session_state.show_data8  # クリックごとに表示状態をトグル
    if st.session_state.show_data8:
        st.write("中国代表のデータ")
        st.write(data8)
    else:
        st.write("")

    @st.cache
    def load_data9():
        data9 = pd.read_csv('pro_9.csv', encoding='utf-8')
        return data9
    data9 = load_data9()
    if 'show_data9' not in st.session_state:
        st.session_state.show_data9 = False
    if st.button("エジプト"):
        st.session_state.show_data9 = not st.session_state.show_data9  # クリックごとに表示状態をトグル
    if st.session_state.show_data9:
        st.write("エジプト代表のデータ")
        st.write(data9)
    else:
        st.write("")
    
    @st.cache
    def load_data10():
        data10 = pd.read_csv('pro_10.csv', encoding='utf-8')
        return data10
    data10 = load_data10()
    if 'show_data10' not in st.session_state:
        st.session_state.show_data10 = False
    if st.button("ペルー"):
        st.session_state.show_data10 = not st.session_state.show_data10  # クリックごとに表示状態をトグル
    if st.session_state.show_data10:
        st.write("ペルー代表のデータ")
        st.write(data10)
    else:
        st.write("")

    @st.cache
    def load_data11():
        data11 = pd.read_csv('pro_11.csv', encoding='utf-8')
        return data11
    data11 = load_data11()
    if 'show_data11' not in st.session_state:
        st.session_state.show_data11 = False
    if st.button("イタリア"):
        st.session_state.show_data11 = not st.session_state.show_data11  # クリックごとに表示状態をトグル
    if st.session_state.show_data11:
        st.write("イタリア代表のデータ")
        st.write(data11)
    else:
        st.write("")
    
    @st.cache
    def load_data12():
        data12 = pd.read_csv('pro_12.csv', encoding='utf-8')
        return data12
    data12 = load_data12()
    if 'show_data12' not in st.session_state:
        st.session_state.show_data12 = False
    if st.button("トルコ"):
        st.session_state.show_data12 = not st.session_state.show_data12  # クリックごとに表示状態をトグル
    if st.session_state.show_data12:
        st.write("トルコ代表のデータ")
        st.write(data12)
    else:
        st.write("")

def about_page():
    st.title("戦略考察")
    st.write("選手のスパイクの最高到達点、ブロックの高さのデータより、攻撃力が上がるフォーメーションの提案をします。")

    st.write("下の図はバレーボールにおける基本的なスタートポジションです。")
    
    st.image("position.jpg", caption="画像のキャプション", use_column_width=True)

    st.write("※ポジションとスパイクの最高到達点とブロックの高さの関係を見たい場合は以下のボタンを押してください。")
    if st.button("関係性についてはこのボタンをクリック"):
        selected_item = st.selectbox("ポジションの選択をしてください", ["セッター", "アウトサイドヒッター", "ミドルブロッカー","オポジット","リベロ"])
        data = {
            "セッター": pd.read_csv("spike1.csv"),
            "アウトサイドヒッター": pd.read_csv("spike2.csv"),
            "ミドルブロッカー": pd.read_csv("spike3.csv"),
            "オポジット":pd.read_csv("spike4.csv"),
            "リベロ":pd.read_csv("spike6.csv"),
        }
        if selected_item in data:
            data_path = data[selected_item]
            df = pd.read_csv(data_path, encoding='utf-8')  # 正しいencodingを指定する
            st.write("選択されたアイテム:", selected_item)
            st.write("アイテムのデータ:")
            st.write(df)
        else:
            st.warning("アイテムが選択されていません")
        
    selected_option = st.selectbox("勝たせたい国を選択", ("ロシア", "ブラジル", "日本","ブルガリア","セルビア","メキシコ","キューバ","中国","エジプト","ペルー","イタリア","トルコ"))
    st.write("選択されたオプション:", selected_option)

if page == "データセット":
    home_page()
elif page == "戦略考察":
    about_page()
