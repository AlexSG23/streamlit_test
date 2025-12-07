import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Panel de análisis de vehículos')

if st.button('Construir histograma'):
    st.write('Histograma de precios')
    fig = px.histogram(car_data, x="price")
    st.plotly_chart(fig, use_container_width=True)

if st.button('Construir gráfico de dispersión'):
    st.write('Precio vs Kilometraje')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
