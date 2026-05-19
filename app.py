import streamlit as st
import pandas as pd

st.title("Student Mental Health")
st.write("Visualización de datos sobre la salud mental en estudiantes")

data = pd.read_csv("Student Mental health.csv")

st.subheader("Datos")
st.dataframe(data)
