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

#parte 2 vehiculos
#Ahora colocare la filtración para los vehiculos
st.subheader("Filtros - Vehículos")

# Filtro por año
anio_limite = st.number_input("Mostrar vehículos con año menor a:", min_value=2000, max_value=2025)

vehiculos_filtrados_anio = vehiculos_df[vehiculos_df["Model_Year"] < anio_limite]

st.write("Resultados por año:")
st.write(vehiculos_filtrados_anio)

# Filtro por precio
precio_limite = st.number_input("Mostrar vehículos con precio menor a:")

vehiculos_filtrados_precio = vehiculos_df[vehiculos_df["Base_MSRP"] < precio_limite]

st.write("Resultados por precio:")
st.write(vehiculos_filtrados_precio)

# PROGRA_gimnasio
st.header("Datos de Gimnasio")

# Cargar datos
gimnasio_df = pd.read_csv("GIMNASIO.csv")

st.subheader("Exploración Inicial")

# Tamaño del dataset
filas_columnas_gimnasio = gimnasio_df.shape
st.write("Número de filas y columnas:", filas_columnas_gimnasio)

# Nombres de columnas
columnas_gimnasio = gimnasio_df.columns
st.write("Nombres de columnas:")
st.write(columnas_gimnasio)

# Primeras 6 filas
primeras_filas_gimnasio = gimnasio_df.head(6)
st.write("Primeras 6 filas:")
st.write(primeras_filas_gimnasio)

# Estadísticas generales
estadisticas_gimnasio = gimnasio_df.describe()
st.write("Estadísticas de variables numéricas:")
st.write(estadisticas_gimnasio)