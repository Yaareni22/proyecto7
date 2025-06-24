import pandas as pd
import plotly.express as px
import streamlit as st
     

st.header('VENTA DE VEHICULOS')    
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.write('Selecciona una casilla')

# hist_button = st.button('Construir histograma') # crear un botón
# dist_button = st.button('Construir dispersion')

if st.checkbox('Construir histograma'): # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
     
if st.checkbox('Consutruir grafico de dispersion'):
    st.write('Creación de grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

