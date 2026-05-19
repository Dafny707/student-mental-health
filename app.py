import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Student Mental Health")
st.write("Visualización sencilla de datos sobre la salud mental en estudiantes")

# Cargar los datos
data = pd.read_csv("student_mental_health.csv")

# Mostrar los datos
st.subheader("Datos del estudio")
st.dataframe(data)

# ---- VISUALIZACIONES ----

# Ansiedad
st.subheader("Ansiedad en estudiantes")
ansiedad = data["Do you have Anxiety?"].value_counts()
st.bar_chart(ansiedad)

# Depresión
st.subheader("Depresión en estudiantes")
depresion = data["Do you have Depression?"].value_counts()
st.bar_chart(depresion)

# Ataques de pánico
st.subheader("Ataques de pánico en estudiantes")
panico = data["Do you have Panic attack?"].value_counts()
st.bar_chart(panico)

# Estrés académico
st.subheader("Estrés académico")
estres = data["Do you have Academic Stress?"].value_counts()
st.bar_chart(estres)
