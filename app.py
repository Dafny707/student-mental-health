import streamlit as st
import pandas as pd

st.title("Student Mental Health")
st.write("Visualización de datos sobre la salud mental en estudiantes")

data = pd.read_csv("student_mental_health.csv")

st.subheader("Datos")
st.dataframe(data)

st.subheader("Filtro por género")
gender = st.selectbox("Selecciona un género", data["Gender"].unique())
filtered_data = data[data["Gender"] == gender]

st.subheader("Nivel de estrés")
stress_counts = filtered_data["Stress Level"].value_counts()
st.bar_chart(stress_counts)
