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

#analisis y exploracion de vehiculos
st.subheader("Exploración Avanzada - Vehículos")

#variable de categorías
def clasificar_rango(rango):
    if rango < 100:
        return "Bajo"
    elif rango <= 250:
        return "Medio"
    else:
        return "Alto"

vehiculos_df["RangoCategoria"] = vehiculos_df["Electric_Range"].apply(clasificar_rango)

st.write("Dataset con nueva categoría:")
st.dataframe(vehiculos_df.head())

# conteo por categoría
conteo_rango = vehiculos_df["RangoCategoria"].value_counts()

st.write("Cantidad de vehículos por categoría:")
st.write(conteo_rango)

# graficos
import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots()
conteo_rango.plot(kind="bar", ax=ax1)

ax1.set_title("Vehículos por rango eléctrico")
ax1.set_xlabel("Categoría")
ax1.set_ylabel("Cantidad")

st.pyplot(fig1)

# los analisis por grupo
analisis_vehiculos = vehiculos_df.groupby("RangoCategoria").agg({
    "Base_MSRP": "mean",
    "Model_Year": "mean",
    "Electric_Range": "std"
})

st.write("Análisis agrupado:")
st.write(analisis_vehiculos)

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

#analisis y exploracion de gimnasio

st.subheader("Exploración Avanzada - Gimnasio")

# agregamos una variable para las categorias
def clasificar_frecuencia(freq):
    if freq < 3:
        return "Baja"
    elif freq <= 5:
        return "Moderada"
    else:
        return "Alta"

gimnasio_df["NivelFrecuencia"] = gimnasio_df["Workout_Frequency (days/week)"].apply(clasificar_frecuencia)

st.write("Dataset con nueva categoría:")
st.dataframe(gimnasio_df.head())

# hacemos el conteo por categoria 
conteo_frecuencia = gimnasio_df["NivelFrecuencia"].value_counts()

st.write("Cantidad de usuarios por frecuencia:")
st.write(conteo_frecuencia)

# grafcos
fig2, ax2 = plt.subplots()
conteo_frecuencia.plot(kind="bar", ax=ax2)

ax2.set_title("Frecuencia de entrenamiento")
ax2.set_xlabel("Nivel")
ax2.set_ylabel("Cantidad")

st.pyplot(fig2)

# el analisis por grupos
analisis_gimnasio = gimnasio_df.groupby("NivelFrecuencia").agg({
    "Session_Duration": "mean",
    "Experience_Level": "mean",
    "BMI": "std"
})

st.write("Análisis agrupado:")
st.write(analisis_gimnasio)
st.subheader("Guardar resultados")

if st.button("Guardar archivos CSV", key="guardar_vehiculos_gimnasio"):

    vehiculos_df.to_csv("Electric_Vehicle_Population_Actualizado.csv", index=False)
    gimnasio_df.to_csv("GymExerciseTracking_Actualizado.csv", index=False)

    st.success("Archivos guardados correctamente")

#Resumen de los resultados con ayuda de Chat-Gpt 
st.subheader("Resumen datos")

# VEHICULOS
corr1 = vehiculos_df["Electric_Range"].corr(vehiculos_df["Model_Year"])
st.write("Rango vs Año:", corr1)

corr2 = vehiculos_df["Electric_Range"].corr(vehiculos_df["Base_MSRP"])
st.write("Rango vs Precio:", corr2)

# GIMNASIO
corr3 = gimnasio_df["Calories_Burned"].corr(gimnasio_df["Session_Duration"])
st.write("Calorías vs Duración:", corr3)

corr4 = gimnasio_df["Fat_Percentage"].corr(gimnasio_df["Experience_Level"])
st.write("Grasa vs Experiencia:", corr4)

#Alma Iris López soto 26826
# PROGRA_netflix

st.header("Datos de Netflix")

# Cargar datos
netflix_df = pd.read_csv("netflix_titles (1).csv")

st.subheader("Exploración Inicial")

# Tamaño del dataset
filas_columnas_netflix = netflix_df.shape
st.write("Número de filas y columnas:", filas_columnas_netflix)

# Nombres de columnas
columnas_netflix = netflix_df.columns
st.write("Nombres de columnas:")
st.write(columnas_netflix)

# Primeras 6 filas
primeras_filas_netflix = netflix_df.head(6)
st.write("Primeras 6 filas:")
st.write(primeras_filas_netflix)

# Estadísticas generales
estadisticas_netflix = netflix_df.describe()
st.write("Estadísticas de variables numéricas:")
st.write(estadisticas_netflix)

# -----------------------
# FILTROS NETFLIX
# -----------------------
st.subheader("Filtros - Netflix")

# Convertir duración a número (ej: "90 min" → 90)
netflix_df["duration_num"] = netflix_df["duration"].str.extract('(\d+)').astype(float)

# Filtro por duración
duracion_min = st.number_input("Mostrar contenido con duración mayor a (min):", min_value=0.0)

netflix_filtrado_duracion = netflix_df[netflix_df["duration_num"] > duracion_min]

st.write("Resultados por duración:")
st.write(netflix_filtrado_duracion)

# Convertir fecha a año
netflix_df["year_added"] = pd.to_datetime(netflix_df["date_added"], errors='coerce').dt.year

# Filtro por año
anio_max = st.number_input("Mostrar contenido añadido antes del año:", min_value=1900, max_value=2025)

netflix_filtrado_anio = netflix_df[netflix_df["year_added"] < anio_max]

st.write("Resultados por año:")
st.write(netflix_filtrado_anio)

# -----------------------
# VARIABLE CATEGÓRICA
# -----------------------
st.subheader("Clasificación de Audiencia")

def clasificar_audiencia(rating):
    if rating in ["G", "TV-Y", "TV-G", "TV-Y7", "TV-Y7-FV"]:
        return "Niños"
    elif rating in ["PG", "TV-PG"]:
        return "Adolescentes"
    elif rating in ["PG-13", "TV-14"]:
        return "Adultos Jóvenes"
    else:
        return "Adultos"

netflix_df["TipoAudiencia"] = netflix_df["rating"].apply(clasificar_audiencia)

# Conteo
conteo_netflix = netflix_df["TipoAudiencia"].value_counts()
st.write("Cantidad por tipo de audiencia:")
st.write(conteo_netflix)

# 
# ANÁLISIS AGRUPADO
st.subheader("Análisis Agrupado")

analisis_netflix = netflix_df.groupby("TipoAudiencia").agg({
    "duration_num": "mean"
})

st.write(analisis_netflix)

# GUARDAR

if st.button("Guardar Netflix", key="guardar_netflix"):

    netflix_df.to_csv("netflix_titles_Actualizado.csv", index=False)

    st.success("Archivos guardados correctamente")

#Alma Iris López Soto 26826
# PROGRA_steam
st.header("Datos de Videojuegos (Steam)")

# Cargar datos
steam_df = pd.read_csv("steam_store_data_2024 (1).csv")
steam_df["price"] = pd.to_numeric(steam_df["price"], errors="coerce")

# LIMPIAR Y CONVERTIR PRECIO A NÚMERO
steam_df["price"] = steam_df["price"].astype(str)  # asegurar que es texto
steam_df["price"] = steam_df["price"].str.replace("$", "", regex=False)
steam_df["price"] = steam_df["price"].str.replace(",", "", regex=False)
steam_df["price"] = pd.to_numeric(steam_df["price"], errors="coerce")
# LIMPIAR Y CONVERTIR DESCUENTO A NÚMERO
steam_df["salePercentage"] = steam_df["salePercentage"].astype(str)
steam_df["salePercentage"] = steam_df["salePercentage"].str.replace("%", "", regex=False)
steam_df["salePercentage"] = pd.to_numeric(steam_df["salePercentage"], errors="coerce")

st.subheader("Exploración Inicial")

# Tamaño del dataset
filas_columnas_steam = steam_df.shape
st.write("Número de filas y columnas:", filas_columnas_steam)

# Nombres de columnas
columnas_steam = steam_df.columns
st.write("Nombres de columnas:")
st.write(columnas_steam)

# Primeras 6 filas
primeras_filas_steam = steam_df.head(6)
st.write("Primeras 6 filas:")
st.write(primeras_filas_steam)

# Estadísticas generales
estadisticas_steam = steam_df.describe()
st.write("Estadísticas de variables numéricas:")
st.write(estadisticas_steam)

# -----------------------
# FILTROS STEAM
# -----------------------
st.subheader("Filtros - Videojuegos")

# Filtro por precio
precio_min = st.number_input("Mostrar juegos con precio mayor a:", min_value=0.0)

steam_filtrado_precio = steam_df[steam_df["price"] > precio_min]

st.write("Resultados por precio:")
st.write(steam_filtrado_precio)

# Filtro por descuento
descuento_max = st.number_input("Mostrar juegos con descuento menor a (%):", min_value=0.0)

steam_filtrado_desc = steam_df[steam_df["salePercentage"] < descuento_max]

st.write("Resultados por descuento:")
st.write(steam_filtrado_desc)

# -----------------------
# VARIABLE CATEGÓRICA
# -----------------------
st.subheader("Clasificación de Juegos")

def clasificar_juego(precio):
    if precio < 10:
        return "Baja"
    elif precio <= 24:
        return "Media"
    else:
        return "Alta"

steam_df["GamaJuego"] = steam_df["price"].apply(clasificar_juego)

# Conteo
conteo_juegos = steam_df["GamaJuego"].value_counts()
st.write("Cantidad de juegos por categoría:")
st.write(conteo_juegos)

# -----------------------
# ANÁLISIS AGRUPADO
# -----------------------
st.subheader("Análisis Agrupado")

analisis_steam = steam_df.groupby("GamaJuego").agg({
    "price": "mean",
    "salePercentage": "mean"
})

st.write(analisis_steam)

# -----------------------
# GUARDAR
# -----------------------
if st.button("Guardar Steam Actualizado"):
    steam_df.to_csv("steam_store_data_2024_Actualizado.csv", index=False)
    st.success("Archivo guardado correctamente")
    
