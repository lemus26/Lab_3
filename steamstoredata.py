# PROGRA_steam
import streamlit as st 
import pandas as pd
st.header("Datos de Videojuegos (Steam)")

# Cargar datos
steam_df = pd.read_csv("steam_store_data_2024.csv")

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