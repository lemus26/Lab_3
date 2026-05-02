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
anio_limite = st.number_input(
    "Mostrar vehículos con año menor a:",
    min_value=2000,
    max_value=2025,
    value=2020,
    key="vehiculos_anio"
)

vehiculos_filtrados_anio = vehiculos_df[vehiculos_df["Model_Year"] < anio_limite]

st.write("Resultados por año:")
st.dataframe(vehiculos_filtrados_anio)

# Filtro por precio
precio_limite = st.number_input(
    "Mostrar vehículos con precio menor a:",
    min_value=0.0,
    max_value=845000.0,
    value=50000.0,
    key="vehiculos_precio"
)

vehiculos_filtrados_precio = vehiculos_df[vehiculos_df["Base_MSRP"] < precio_limite]

st.write("Resultados por precio:")
st.dataframe(vehiculos_filtrados_precio)

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



#parte 2 gimnasio
#Ahora colocare la filtración para el gimnasio
st.subheader("Filtros - Gimnasio")

# Filtro calorías
calorias_minimas = st.number_input(
    "Mostrar sesiones con calorías mayores o iguales a:",
    min_value=0.0,
    value=200.0,
    key="gym_calorias"
)

gimnasio_filtrado_calorias = gimnasio_df[gimnasio_df["Calories_Burned"] >= calorias_minimas]

st.write("Resultados por calorías:")
st.dataframe(gimnasio_filtrado_calorias)

# Filtro grasa
grasa_maxima = st.number_input(
    "Mostrar sesiones con grasa menor o igual a:",
    min_value=0.0,
    max_value=100.0,
    value=25.0,
    key="gym_grasa"
)

gimnasio_filtrado_grasa = gimnasio_df[gimnasio_df["Fat_Percentage"] <= grasa_maxima]

st.write("Resultados por grasa corporal:")
st.dataframe(gimnasio_filtrado_grasa)