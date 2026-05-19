import streamlit as st
import pandas as pd

# -------------------------------
# TÍTULO
# -------------------------------
st.title("Student Mental Health")
st.write("Visualización clara y sencilla sobre la salud mental en estudiantes")

# -------------------------------
# CARGA DE DATOS
# -------------------------------
data = pd.read_csv("student_mental_health.csv")

# -------------------------------
# MOSTRAR DATOS
# -------------------------------
st.subheader("Datos del estudio")
st.dataframe(data)

# -------------------------------
# GRÁFICA 1: ANSIEDAD (PORCENTAJE)
# -------------------------------
st.subheader("Porcentaje de estudiantes con ansiedad")

ansiedad_pct = (
    data["Do you have Anxiety?"]
    .value_counts(normalize=True) * 100
)

st.bar_chart(ansiedad_pct)

# -------------------------------
# GRÁFICA 2: DEPRESIÓN (CONTEO)
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
    .groupby("Gender")["Do you have Anxiety?"]
    .value_counts()
    .unstack()
)

st.bar_chart(ansiedad_genero)

# -------------------------------
# FILTRO INTERACTIVO
# -------------------------------
st.subheader("Filtro por género")

genero = st.selectbox(
    "Selecciona un género",
    data["Gender"].unique()
)

data_filtrada = data[data["Gender"] == genero]

st.write("Datos filtrados")
st.dataframe(data_filtrada)
