import streamlit as st
import pandas as pd

st.title("Student Mental Health")
st.write("Visualización sencilla de datos sobre la salud mental en estudiantes")

data = pd.read_csv("student_mental_health.csv")

st.subheader("Datos del estudio")
st.dataframe(data)

# Ansiedad
st.subheader("Ansiedad en estudiantes")
ansiedad = data["Anxiety"].value_counts()
st.bar_chart(ansiedad)

# Depresión
st.subheader("Depresión en estudiantes")
depresion = data["Depression"].value_counts()
st.bar_chart(depresion)

# Ataques de pánico
st.subheader("Ataques de pánico en estudiantes")
panico = data["Panic attack"].value_counts()
st.bar_chart(panico)
