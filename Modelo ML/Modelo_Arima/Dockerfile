# Usar una imagen base ligera de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el archivo de credenciales y el código
COPY credenciales.json /app/credenciales.json
COPY . .

# Exponer el puerto usado por Streamlit
EXPOSE 8501

# Ejecutar la aplicación
CMD ["streamlit", "run", "app.py", "--server.port=8501"]







