from datetime import datetime, timedelta
import requests
from google.cloud import storage

def download_file(url):
    """
    Descarga un archivo desde una URL y devuelve su contenido.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el archivo: {url} - {e}")
        return None

def upload_to_gcs(bucket, object_name, file_content):
    """
    Sube un archivo a un cubo de Google Cloud Storage (GCS).
    """
    try:
        client = storage.Client()
        bucket = client.bucket(bucket)
        blob = bucket.blob(object_name)
        blob.upload_from_string(file_content)
        print(f"Archivo subido a GCS: {object_name}")
    except Exception as e:
        print(f"Error al subir el archivo a GCS: {object_name} - {e}")

def get_latest_date_in_folder(bucket, folder_prefix):
    """
    Busca el archivo de mes más reciente dentro de una carpeta específica de año.
    
    Args:
        bucket (str): El nombre del bucket.
        folder_prefix (str): El prefijo de la carpeta (ej. "yellow/2023" o "green/2023").
    
    Returns:
        datetime: El último mes y año en formato datetime, o None si no hay archivos.
    """
    client = storage.Client()
    bucket = client.bucket(bucket)
    blobs = bucket.list_blobs(prefix=folder_prefix)

    # Extraer las fechas de los nombres de archivos en el formato "YYYY-MM.parquet"
    dates = []
    for blob in blobs:
        file_name = blob.name.split("/")[-1]
        try:
            date = datetime.strptime(file_name[:7], "%Y-%m")  # Extrae el año-mes del nombre del archivo
            dates.append(date)
        except ValueError:
            continue  # Ignora archivos que no sigan el formato esperado

    # Encuentra la fecha más reciente
    latest_date = max(dates) if dates else None
    return latest_date

def get_most_recent_year_folder(bucket, base_prefix):
    """
    Encuentra el año más reciente que tiene una carpeta en el bucket.

    Args:
        bucket (str): El nombre del bucket.
        base_prefix (str): El prefijo base (ej. "yellow/" o "green/").
    
    Returns:
        str: El prefijo completo de la carpeta del año más reciente (ej. "yellow/2023").
    """
    client = storage.Client()
    bucket = client.bucket(bucket)
    blobs = bucket.list_blobs(prefix=base_prefix, delimiter="/")

    # Extraer años de las subcarpetas
    years = []
    for page in blobs.pages:
        for prefix in page.prefixes:
            year = prefix.split("/")[-2]  # Extrae el año del nombre de la carpeta
            try:
                years.append(int(year))
            except ValueError:
                continue  # Ignora carpetas que no sigan el formato de año

    # Encontrar el año más reciente
    latest_year = max(years) if years else None
    return f"{base_prefix}{latest_year}" if latest_year else None

def main_flow(request):
    """
    Realiza el flujo principal del script, descargando y cargando archivos Parquet de taxis amarillos y verdes
    en un depósito de Google Cloud Storage (GCS) con una estructura de directorios específica.
    """
    base_url_yellow = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"
    base_url_green = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_"
    bucket_name = "bucket_de_ejemplo1982"
    
    # Obtener la carpeta de año más reciente para yellow y green
    latest_yellow_year_folder = get_most_recent_year_folder(bucket_name, "yellow/")
    latest_green_year_folder = get_most_recent_year_folder(bucket_name, "green/")
    
    if not latest_yellow_year_folder or not latest_green_year_folder:
        return "No se encontraron carpetas de año en el bucket.", 400

    # Obtener la fecha más reciente dentro de la carpeta de año más reciente para yellow y green
    latest_yellow_date = get_latest_date_in_folder(bucket_name, latest_yellow_year_folder)
    latest_green_date = get_latest_date_in_folder(bucket_name, latest_green_year_folder)
    latest_date = max(latest_yellow_date, latest_green_date)

    # Calcular la fecha para el siguiente mes al último dataset cargado
    next_month_date = latest_date + timedelta(days=32)
    next_month = next_month_date.strftime("%Y-%m")
    next_year = next_month_date.strftime("%Y")

    # Construir el nombre de objetos para el siguiente mes, organizados por año
    yellow_object_name_next_month = f"yellow/{next_year}/{next_month}.parquet"
    green_object_name_next_month = f"green/{next_year}/{next_month}.parquet"

    # Descargar y cargar el siguiente mes si no existe en el depósito de GCS
    response_message = ""
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    if not bucket.blob(yellow_object_name_next_month).exists(client) or not bucket.blob(green_object_name_next_month).exists(client):
        yellow_parquet_url = f"{base_url_yellow}{next_month}.parquet"
        green_parquet_url = f"{base_url_green}{next_month}.parquet"

        yellow_file_content = download_file(yellow_parquet_url)
        green_file_content = download_file(green_parquet_url)

        if yellow_file_content is not None:
            upload_to_gcs(bucket_name, yellow_object_name_next_month, yellow_file_content)
            response_message += f"Subiendo archivo amarillo: {yellow_object_name_next_month}\n"
        else:
            response_message += f"El mes {next_month} no está disponible para amarillo. Terminando.\n"

        if green_file_content is not None:
            upload_to_gcs(bucket_name, green_object_name_next_month, green_file_content)
            response_message += f"Subiendo archivo verde: {green_object_name_next_month}\n"
        else:
            response_message += f"El mes {next_month} no está disponible para verde. Terminando.\n"
    else:
        response_message = f"Los archivos para {next_month} ya existen en el depósito de GCS. No es necesario cargarlos."

    # Devolver un mensaje de respuesta
    return response_message, 200
