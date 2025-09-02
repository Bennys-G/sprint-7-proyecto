# Sprint 7 – App Streamlit: EDA de vehículos

Aplicación web en **Streamlit** para un análisis exploratorio del dataset `vehicles_us.csv`.
link de render: https://sprint-7-proyecto-1-usdn.onrender.com 
## Funcionalidades
- Encabezado y vista previa del dataset.
- Botones para:
  - **Histograma** (Plotly) de una variable numérica (por defecto `odometer`).
  - **Dispersión** (Plotly) `price` vs `odometer`.
- (Opcional) **Casillas de verificación** para activar/desactivar gráficos y elegir columnas.

## Cómo ejecutar
```bash
pip install -r requirements.txt
streamlit run app.py