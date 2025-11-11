# app.py
import streamlit as st
import pandas as pd
import numpy as np

# Cargar matriz W entrenada
W_df = pd.read_excel(r"C:\Users\USUARIO\OneDrive\Documentos\Vainas de Santiago\Matriz_W_resultado.xlsx", index_col=0)
W = W_df.to_numpy()
materias = list(W_df.index)
carreras = list(W_df.columns)

st.title("🎓 Sistema de Recomendación de Carreras Universitarias")
st.markdown("Por favor, califica cuánto te gustaban las siguientes materias en el colegio (1 = nada, 5 = mucho):")

# Entrada del usuario
z_input = []
for materia in materias:
    score = st.slider(materia, 1, 5, 3)
    z_input.append(score)

# Botón para generar predicción
if st.button("Recomendar carreras"):
    z_nuevo = np.array(z_input).reshape(1, -1)
    x_pred = z_nuevo @ W
    recomendaciones = pd.DataFrame(x_pred, columns=carreras)
    st.subheader("🎯 Carreras recomendadas (de mayor afinidad a menor):")
    st.dataframe(recomendaciones.T.sort_values(by=0, ascending=False).rename(columns={0: "Afinidad"}))

    # Gráfico opcional
    st.subheader("📊 Visualización de afinidades")
    st.bar_chart(recomendaciones.T.sort_values(by=0, ascending=False))

