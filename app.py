import streamlit as st
import pandas as pd

st.title("Student Mental Health")
st.write("Visualización clara y sencilla sobre la salud mental en estudiantes")

# Cargar datos
data = pd.read_csv("student_mental_health.csv")

st.subheader("Datos del estudio")
st.dataframe(data)

# -------------------------------
# GRÁFICA 1: ANSIEDAD (%)
# -------------------------------
st.subheader("Porcentaje de estudiantes con ansiedad")

ansiedad_pct = (
    data["Do you have Anxiety?"]
    .value_counts(normalize=True) * 100
)

st.bar_chart(ansiedad_pct)

# -------------------------------
# GRÁFICA 2: DEPRESIÓN (conteo)
# -------------------------------
st.subheader("Casos de depresión en estudiantes")

depresion = data["Do you have Depression?"].value_counts()
st.bar_chart(depresion)

# -------------------------------
# GRÁFICA 3: ANSIEDAD POR GÉNERO
# -------------------------------
st.subheader("Ansiedad según género")

ansiedad_genero = (
    data
    .groupby("Choose your gender")["Do you have Anxiety?"]
    .value_counts()
    .unstack()
)

st.bar_chart(ansiedad_genero)

# -------------------------------
# FILTRO POR GÉNERO
# -------------------------------
st.subheader("Filtro por género")

genero = st.selectbox(
    "Selecciona un género",
    data["Choose your gender"].unique()
)

data_filtrada = data[data["Choose your gender"] == genero]

st.dataframe(data_filtrada)
