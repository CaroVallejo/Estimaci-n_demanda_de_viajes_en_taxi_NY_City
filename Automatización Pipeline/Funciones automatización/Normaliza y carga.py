from google.cloud import storage, bigquery
import re

def normalize_taxi_data(event=None, context=None):
    # Parámetros de bucket y carpeta
    bucket_name = "bucket_de_ejemplo1982"  # Reemplaza con el nombre de tu bucket
    folder_path = "Procesados/combined_taxi_data"  # Carpeta donde están los archivos

    # Inicializar el cliente de Cloud Storage
    storage_client = storage.Client()
    
    # Obtener la lista de archivos en la carpeta especificada
    blobs = list(storage_client.list_blobs(bucket_name, prefix=folder_path))
    parquet_files = [blob for blob in blobs if re.match(r'^Procesados/combined_taxi_data/\d{4}/.*\.parquet$', blob.name)]
    
    # Ordenar archivos por fecha de actualización y seleccionar el más reciente
    if parquet_files:
        recent_file = sorted(parquet_files, key=lambda x: x.updated, reverse=True)[0]
        recent_file_uri = f"gs://{bucket_name}/{recent_file.name}"
    else:
        print("No se encontraron archivos recientes en la estructura especificada.")
        return "No se encontraron archivos relevantes.", 400

    # Inicializar el cliente de BigQuery
    client = bigquery.Client()

    # Reemplazar el URI en la consulta SQL con el archivo más reciente
    query = f"""
    -- Paso 1: Crear la Tabla Calendario en BigQuery
    CREATE TABLE IF NOT EXISTS taxi_dataset.Calendar AS
    WITH date_range AS (
        SELECT 
            DATE_ADD('2020-01-01', INTERVAL day_number DAY) AS date
        FROM 
            UNNEST(GENERATE_ARRAY(0, DATE_DIFF(CURRENT_DATE(), '2020-01-01', DAY))) AS day_number
    )
    SELECT 
        ROW_NUMBER() OVER () AS calendar_id,
        date,
        FORMAT_DATE('%Y', date) AS year,
        FORMAT_DATE('%m', date) AS month,
        FORMAT_DATE('%B', date) AS month_name,
        FORMAT_DATE('%d', date) AS day,
        FORMAT_DATE('%A', date) AS day_name,
        EXTRACT(WEEK FROM date) AS week,
        CASE 
            WHEN FORMAT_DATE('%A', date) IN ('Saturday', 'Sunday') THEN TRUE 
            ELSE FALSE 
        END AS is_weekend
    FROM date_range;

    -- Paso 2: Crear la Tabla Externa Temporal para Datos Incrementales
    CREATE OR REPLACE EXTERNAL TABLE taxi_dataset.TaxiTrip_Incremental_Temp
    OPTIONS (
      format = 'PARQUET',
      uris = ['{recent_file_uri}']
    );

    -- Paso 3: Crear Tabla Normalizada con calendar_id y trip_id
    CREATE OR REPLACE TABLE taxi_dataset.Normalized_Incremental AS
    WITH Normalized_Incremental AS (
        SELECT 
            GENERATE_UUID() AS trip_id,  -- Genera un ID único para cada viaje
            temp.*,  -- Todos los campos del archivo incremental
            cal.calendar_id  -- ID de la tabla calendario
        FROM taxi_dataset.TaxiTrip_Incremental_Temp AS temp
        LEFT JOIN taxi_dataset.Calendar AS cal
        ON DATE(temp.pickup_datetime) = cal.date
    )
    SELECT * FROM Normalized_Incremental;

    -- Paso 4: Crear la tabla TaxiTrip_Normalized si no existe
    CREATE TABLE IF NOT EXISTS taxi_dataset.TaxiTrip_Normalized AS
    SELECT * FROM taxi_dataset.Normalized_Incremental WHERE FALSE;

    -- Paso 5: Insertar los datos normalizados en TaxiTrip_Normalized
    INSERT INTO taxi_dataset.TaxiTrip_Normalized
    SELECT * FROM taxi_dataset.Normalized_Incremental;

    -- Paso 6: Eliminar la Tabla Externa Temporal
    DROP EXTERNAL TABLE IF EXISTS taxi_dataset.TaxiTrip_Incremental_Temp;

    -- Paso 7: Eliminar la Tabla Temporal Normalized_Incremental
    DROP TABLE IF EXISTS taxi_dataset.Normalized_Incremental;
    """

    try:
        # Ejecutar la consulta SQL en BigQuery
        job = client.query(query)
        job.result()  # Esperar a que se complete la ejecución
        print("Carga incremental y normalización ejecutadas exitosamente.")
        
        # Retornar una respuesta de éxito para evitar el error de Flask
        return "Proceso completado exitosamente.", 200
    except Exception as e:
        # Manejar errores y mostrar información útil
        print(f"Error al ejecutar la consulta: {e}")
        # Retornar una respuesta de error para Flask
        return f"Error al ejecutar la consulta: {e}", 500





functions-framework==3.*
google-cloud-bigquery
google-cloud-storage