import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="EDA de Vehículos", layout="wide")
st.header("Exploración interactiva de anuncios de vehículos 🚗")

# --- Cargar datos (archivo junto a app.py)
CSV_PATH = "vehicles_us.csv"   # <-- aquí el cambio clave
try:
    df = pd.read_csv(CSV_PATH)
except FileNotFoundError:
    st.error(f"No pude encontrar {CSV_PATH}. Ponlo junto a app.py o ajusta la ruta.")
    st.stop()

st.write("Vista previa:")
st.dataframe(df.head())
st.divider()

# --- Controles
st.subheader("Generar gráficos")
col1, col2, col3 = st.columns(3)
with col1:
    hist_button = st.button("Construir histograma")
with col2:
    scatter_button = st.button("Construir diagrama de dispersión")
with col3:
    use_checkboxes = st.checkbox("Usar casillas en lugar de botones")

# --- Parámetros
numeric_cols = df.select_dtypes(include="number").columns.tolist()
default_x = "odometer" if "odometer" in numeric_cols else numeric_cols[0]
default_y = "price"    if "price" in numeric_cols else numeric_cols[min(1, len(numeric_cols)-1)]

# --- Versión con casillas
if use_checkboxes:
    build_hist = st.checkbox("Construir un histograma")
    build_scatter = st.checkbox("Construir un diagrama de dispersión")

    if build_hist:
        col = st.selectbox("Columna para el histograma", numeric_cols,
                           index=numeric_cols.index(default_x))
        st.write(f"Creación de un histograma para **{col}**")
        fig = go.Figure(data=[go.Histogram(x=df[col])])
        fig.update_layout(title_text=f"Distribución de {col}")
        st.plotly_chart(fig, use_container_width=True)

    if build_scatter:
        c1, c2 = st.columns(2)
        with c1:
            xcol = st.selectbox("Eje X", numeric_cols, index=numeric_cols.index(default_x))
        with c2:
            ycol = st.selectbox("Eje Y", numeric_cols, index=numeric_cols.index(default_y))
        st.write(f"Diagrama de dispersión **{xcol} vs {ycol}**")
        fig2 = px.scatter(df, x=xcol, y=ycol, title=f"{ycol} vs {xcol}", opacity=0.6)
        st.plotly_chart(fig2, use_container_width=True)

# --- Versión con botones
if hist_button and not use_checkboxes:
    st.write("Creación de un histograma para la columna **odometer**")
    fig = go.Figure(data=[go.Histogram(x=df[default_x])])
    fig.update_layout(title_text="Distribución del Odómetro")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button and not use_checkboxes:
    st.write("Creación de un diagrama de dispersión **price vs odometer**")
    fig2 = px.scatter(df, x=default_x, y=default_y, title=f"{ycol if use_checkboxes else default_y} vs {xcol if use_checkboxes else default_x}", opacity=0.6)
    st.plotly_chart(fig2, use_container_width=True)
