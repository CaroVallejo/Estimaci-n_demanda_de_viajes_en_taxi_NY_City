from google.cloud import storage
from datetime import datetime
import pandas as pd

def get_latest_file(bucket_name, base_prefix):
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    # Listar todas las subcarpetas de año dentro de base_prefix (ej., "yellow/" o "green/")
    years = []
    blobs = bucket.list_blobs(prefix=base_prefix, delimiter="/")
    
    for page in blobs.pages:
        for prefix in page.prefixes:
            try:
                year = int(prefix.split("/")[-2])
                years.append(year)
            except ValueError:
                continue

    if not years:
        print("No se encontraron carpetas de años.")
        return None

    # Encontrar el año más reciente
    latest_year = max(years)
    year_prefix = f"{base_prefix}{latest_year}/"
    year_blobs = bucket.list_blobs(prefix=year_prefix)
    
    dates = []
    for blob in year_blobs:
        file_name = blob.name.split("/")[-1]
        try:
            date = datetime.strptime(file_name[:7], "%Y-%m")
            dates.append((date, blob.name))
        except ValueError:
            continue

    if dates:
        latest_file = max(dates, key=lambda x: x[0])[1]
        return latest_file

    print("No se encontraron archivos en el año más reciente.")
    return None

def ETL_green_function(df):
    # Selección y procesamiento de columnas para taxi verde
    posiciones = [0, 1, 2, 5, 6, 8, 13, 16, 17]
    df = df.iloc[:, posiciones]
    df = df.dropna()
    df = df[(df['total_amount'] < 70) & (df['total_amount'] > 4)]
    df = df[df['trip_distance'] > 0.2]
    pd.set_option('display.float_format', '{:.2f}'.format)

    # Calcular tiempo de viaje y variables adicionales
    df['travel_time_min'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60
    df['date'] = df['pickup_datetime'].dt.date
    df['year'] = df['pickup_datetime'].dt.year
    df['month'] = df['pickup_datetime'].dt.strftime('%B')
    df['day_name'] = df['pickup_datetime'].dt.strftime('%A')
    df['time_slot'] = df['pickup_datetime'].dt.hour

    df = df[(df['travel_time_min'] > 0) & (df['travel_time_min'] < 120)]
    df['speed_ml_min'] = df['trip_distance'] / df['travel_time_min']
    df['price_min'] = df['total_amount'] / df['travel_time_min']
    df['price_mile'] = df['total_amount'] / df['trip_distance']
    df['taxi_type'] = 1
    df['tolls'] = df['tolls_amount'].apply(lambda x: 1 if x > 0 else 0)
    df = df.drop(columns=['tolls_amount'])

    convenient_order = ['VendorID', 'date', 'year', 'month', 'day_name', 'taxi_type', 'pickup_datetime',
                        'PULocationID', 'time_slot', 'dropoff_datetime', 'DOLocationID', 'tolls',
                        'total_amount', 'payment_type', 'travel_time_min', 'price_min', 'trip_distance',
                        'price_mile', 'speed_ml_min']
    df = df[convenient_order]
    return df

def ETL_yellow_function(df):
    # Selección y procesamiento de columnas para taxi amarillo
    posiciones = [0, 1, 2, 4, 7, 8, 9, 14, 16]
    df = df.iloc[:, posiciones]
    df = df.dropna()
    df = df[(df['total_amount'] < 70) & (df['total_amount'] > 4)]
    df = df[df['trip_distance'] > 0.2]
    pd.set_option('display.float_format', '{:.2f}'.format)

    df['travel_time_min'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60
    df['date'] = df['pickup_datetime'].dt.date
    df['year'] = df['pickup_datetime'].dt.year
    df['month'] = df['pickup_datetime'].dt.strftime('%B')
    df['day_name'] = df['pickup_datetime'].dt.strftime('%A')
    df['time_slot'] = df['pickup_datetime'].dt.hour

    df = df[(df['travel_time_min'] > 0) & (df['travel_time_min'] < 120)]
    df['speed_ml_min'] = df['trip_distance'] / df['travel_time_min']
    df['price_min'] = df['total_amount'] / df['travel_time_min']
    df['price_mile'] = df['total_amount'] / df['trip_distance']
    df['taxi_type'] = 0
    df['tolls'] = df['tolls_amount'].apply(lambda x: 1 if x > 0 else 0)
    df = df.drop(columns=['tolls_amount'])

    convenient_order = ['VendorID', 'date', 'year', 'month', 'day_name', 'taxi_type', 'pickup_datetime',
                        'PULocationID', 'time_slot', 'dropoff_datetime', 'DOLocationID', 'tolls',
                        'total_amount', 'payment_type', 'travel_time_min', 'price_min', 'trip_distance',
                        'price_mile', 'speed_ml_min']
    df = df[convenient_order]
    return df

def etl_process_taxi_data(request):
    """
    Proceso ETL que aplica transformaciones de datos a taxis amarillos y verdes, y concatena los resultados.
    """
    bucket_name = "bucket_de_ejemplo1982"
    
    latest_yellow_file = get_latest_file(bucket_name, "yellow/")
    latest_green_file = get_latest_file(bucket_name, "green/")
    if not latest_yellow_file or not latest_green_file:
        return "No se encontraron archivos en las carpetas de yellow o green.", 400

    # Descargar archivos desde GCS
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    
    yellow_path = "/tmp/yellow_data.parquet"
    green_path = "/tmp/green_data.parquet"
    try:
        bucket.blob(latest_yellow_file).download_to_filename(yellow_path)
        bucket.blob(latest_green_file).download_to_filename(green_path)
        print("Archivos de taxis amarillos y verdes descargados con éxito.")
    except Exception as e:
        print(f"Error al descargar archivos: {e}")
        return f"Error al descargar archivos: {e}"

    # Leer y procesar datos
    try:
        df_yellow = pd.read_parquet(yellow_path)
        df_green = pd.read_parquet(green_path)

        # Unificar nombres de columnas antes de procesar
        rename_columns = {
            'tpep_pickup_datetime': 'pickup_datetime',
            'tpep_dropoff_datetime': 'dropoff_datetime',
            'lpep_pickup_datetime': 'pickup_datetime',
            'lpep_dropoff_datetime': 'dropoff_datetime'
        }
        df_yellow.rename(columns=rename_columns, inplace=True)
        df_green.rename(columns=rename_columns, inplace=True)

        # Aplicar ETL específico para cada tipo de taxi
        df_yellow_processed = ETL_yellow_function(df_yellow)
        df_green_processed = ETL_green_function(df_green)

        # Concatenar DataFrames procesados
        df_combined = pd.concat([df_yellow_processed, df_green_processed], ignore_index=True)

        # Guardar y cargar archivo procesado a GCS
        latest_date = datetime.strptime(latest_yellow_file.split('/')[-1][:7], "%Y-%m")
        processed_output = f"Procesados/combined_taxi_data/{latest_date.year}/{latest_date.strftime('%Y-%m')}.parquet"
        processed_path = "/tmp/processed_taxi_data.parquet"
        df_combined.to_parquet(processed_path, index=False)
        bucket.blob(processed_output).upload_from_filename(processed_path)
        print("Archivo combinado y procesado subido con éxito a GCS.")
    except Exception as e:
        print(f"Error al procesar los datos: {e}")
        return f"Error al procesar los datos: {e}"

    return "Proceso ETL completado y archivo subido a GCS"




