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

#Ingreso de nuevos datos de vehiculos
st.subheader("Agregar nuevo vehículo")

# Inputs del usuario
nuevo_año = st.number_input("Año del modelo", min_value=2000, max_value=2025, key="anio")
nuevo_precio = st.number_input("Precio base (Base_MSRP)", min_value=0.0, key="precio")
nuevo_rango = st.number_input("Rango eléctrico (Electric_Range)", min_value=0.0, key="rango")

# Botón para agregar
if st.button("Agregar vehículo"):

    nuevo_registro = {
        "Model_Year": nuevo_año,
        "Base_MSRP": nuevo_precio,
        "Electric_Range": nuevo_rango
    }

    nuevo_df = pd.DataFrame([nuevo_registro])

    vehiculos_df = pd.concat([vehiculos_df, nuevo_df], ignore_index=True)

    st.success("Vehículo agregado correctamente")

    st.write("Nuevo dataset actualizado:")
    st.write(vehiculos_df.tail())

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
calorias_minimas = st.number_input("Mostrar sesiones con calorías mayores o iguales a:")

gimnasio_filtrado_calorias = gimnasio_df[gimnasio_df["Calories_Burned"] >= calorias_minimas]

st.write("Resultados por calorías:")
st.write(gimnasio_filtrado_calorias)

# Filtro grasa
grasa_maxima = st.number_input("Mostrar sesiones con grasa menor o igual a:")

gimnasio_filtrado_grasa = gimnasio_df[gimnasio_df["Fat_Percentage"] <= grasa_maxima]

st.write("Resultados por grasa corporal:")
st.write(gimnasio_filtrado_grasa)