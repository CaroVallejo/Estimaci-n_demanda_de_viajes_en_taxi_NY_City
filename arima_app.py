import streamlit as st
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Modelo ARIMA para 100 Periodos")

# Crear una serie de tiempo de ejemplo
np.random.seed(42)
data = np.random.randn(200).cumsum()
date_range = pd.date_range(start='2020-01-01', periods=200, freq='D')
series = pd.Series(data, index=date_range)

# Ajustar el modelo ARIMA
model = ARIMA(series, order=(5,1,0))  # Orden (p,d,q)
model_fit = model.fit()

# Realizar predicciones para 100 periodos
forecast = model_fit.forecast(steps=100)

# Visualizar las predicciones
st.write("Datos Históricos y Predicciones")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(series, label='Datos Históricos')
ax.plot(forecast, label='Predicción', color='red')
ax.set_title('Predicción con ARIMA')
ax.legend()
st.pyplot(fig)
