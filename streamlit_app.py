import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import streamlit as st
import matplotlib.pyplot as plt

# Matplotlibでグラフを作成
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])

# Streamlitに表示
st.pyplot(fig)
