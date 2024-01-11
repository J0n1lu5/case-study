import streamlit as st
<<<<<<< HEAD
=======
import numpy as np

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)
>>>>>>> 6ba6f5071872222f4615c631bda67a5de246536f
