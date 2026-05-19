import streamlit as st
import pandas as pd

st.title("Student Mental Health")
st.write("Visualización de datos sobre la salud mental en estudiantes")

data = pd.read_csv("student_mental_health.csv")

st.subheader("Datos")
st.dataframe(data)
