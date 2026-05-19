import streamlit as st
import os
import pandas as pd

st.write("Archivos en la carpeta:")
st.write(os.listdir())

data = pd.read_csv("student_mental_health.csv")
st.dataframe(data)
