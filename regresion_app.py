import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Modelo de Regresión Lineal")

# Crear un conjunto de datos de ejemplo
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # Variables independientes
y = 2.5 * X + np.random.randn(100, 1) * 2  # Variable dependiente

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
st.write(f'Error Cuadrático Medio: {mse}')

# Visualizar las predicciones
st.write("Datos Reales y Predicciones")
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(X_test, y_test, label='Datos Reales')
ax.plot(X_test, y_pred, color='red', label='Predicción')
ax.set_title('Modelo de Regresión Lineal')
ax.legend()
st.pyplot(fig)
