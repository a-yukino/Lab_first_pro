import streamlit as st

st.title("女子FIVB選手のデータ分析ツール") # タイトル

uploaded_file = st.file_uploader("アクセスログをアップロードしてください。")

st.markdown('### アクセスログ（先頭5件）')
st.write(df.head(5))
