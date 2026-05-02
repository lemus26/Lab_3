#Alma Iris López soto 26826
# PROGRA_netflix
import streamlit as st 
import pandas as pd
st.header("Datos de Netflix")

# Cargar datos
netflix_df = pd.read_csv("netflix_titles.csv")

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

# -----------------------
# ANÁLISIS AGRUPADO
# -----------------------
st.subheader("Análisis Agrupado")

analisis_netflix = netflix_df.groupby("TipoAudiencia").agg({
    "duration_num": "mean"
})

st.write(analisis_netflix)

# -----------------------
# GUARDAR
# -----------------------
if st.button("Guardar Netflix Actualizado"):
    netflix_df.to_csv("netflix_titles_Actualizado.csv", index=False)
    st.success("Archivo guardado correctamente")