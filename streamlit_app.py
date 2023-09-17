import streamlit as st

st.title("女子FIVB選手のデータ分析ツール") # タイトル

st.write("分析したいファイルをアップロードしてください。")
st.file_uploader("Choose file") # ファイルアップロード
