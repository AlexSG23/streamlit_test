import streamlit as st

st.header('Lanzar una moneda')
st.write('Esta aplicación aún no es funcional. En construcción.')
num_lanzamientos = st.slider(
    "¿Cuántas veces quieres lanzar la moneda?",
    min_value=1,
    max_value=100,
    value=10,
    step=1
)
