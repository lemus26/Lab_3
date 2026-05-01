#El  codigo lo hice con ayuda de Chat porque con la clase no me quedó claro y no entendí
#como programar la base de datos
import streamlit as st
import pandas as pd

st.title("LAB 3 - Exploración de Datos")

# Carros
st.header("Vehículos Eléctricos")

# Cargar datos
vehiculos_df = pd.read_csv("VEHICULOS.csv")

st.subheader("Exploración Inicial")

# Tamaño del dataset
filas_columnas_vehiculos = vehiculos_df.shape
st.write("Número de filas y columnas:", filas_columnas_vehiculos)

# Nombres de columnas
columnas_vehiculos = vehiculos_df.columns
st.write("Nombres de columnas:")
st.write(columnas_vehiculos)

# Primeras 6 filas
primeras_filas_vehiculos = vehiculos_df.head(6)
st.write("Primeras 6 filas:")
st.write(primeras_filas_vehiculos)

# Estadísticas generales
estadisticas_vehiculos = vehiculos_df.describe()
st.write("Estadísticas de variables numéricas:")
st.write(estadisticas_vehiculos)