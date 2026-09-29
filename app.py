st.sidebar.title(evaluacion sencilla de lote)
st.sidebar.write(jonathan marea sabado, 371665, grupo 3L, facultad de ciencias quimicas)
import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=6.5
)

temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):

    # Completa aquí la lógica
    if condicion:
          pH < 6.0 or pH > 7.0
    resultado = "revisar ph"
elif otra_condicion:
      pH < 20 or pH > 25
    resultado = "revisar temperatura"
else:
    resultado = "lote aceptable"
    st.write(f"Resultado: {resultado}")
