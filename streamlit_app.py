import streamlit as st

# セッション変数を初期化
if 'button1_clicked' not in st.session_state:
    st.session_state.button1_clicked = False

if 'button2_clicked' not in st.session_state:
    st.session_state.button2_clicked = False

# ボタン1
if st.button("ボタン1"):
    st.session_state.button1_clicked = not st.session_state.button1_clicked

# ボタン2
if st.button("ボタン2"):
    st.session_state.button2_clicked = not st.session_state.button2_clicked

# ボタンのクリック状態を表示
st.write(f"ボタン1のクリック状態: {st.session_state.button1_clicked}")
st.write(f"ボタン2のクリック状態: {st.session_state.button2_clicked}")
