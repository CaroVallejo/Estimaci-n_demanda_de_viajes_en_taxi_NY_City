# Protección y validación de datos en GCP

## Validaciones ETL en Google Cloud Storage

En el proceso de ETL, se llevaron a cabo las siguientes validaciones de datos, previo a su carga en BigQuery.

1. **Filtrado de columnas:** Se seleccionan columnas específicas para taxis amarillos y verdes según índices predeterminados.
2. **Eliminación de valores nulos:** Se eliminan filas con valores faltantes (`dropna()`).
3. **Establecer Formato de columnas de fecha:** Se asegura que las columnas de tiempo sean reconocidas como `datetime`.
4. **Establecer Rango de precios totales (`total_amount`):** Debe estar entre 4 y 70.
5. **Establecer Distancia del viaje (`trip_distance`):** Debe ser mayor a 0.2 millas.
6. **Establecer Duración del viaje (`travel_time_min`):** Calculada como la diferencia entre las fechas de recogida y destino (`dropoff_datetime - pickup_datetime`). Debe ser mayor a 0 minutos y menor a 120 minutos.
7. **Columnas calculadas:**
   - `travel_time_min`: Duración del viaje en minutos.
   - `speed_ml_min`: Velocidad promedio en millas por minuto.
   - `price_min`: Precio total dividido por tiempo de viaje.
   - `price_mile`: Precio total dividido por distancia recorrida.
8. **Clasificación de tipo de taxi:**
   - `taxi_type = 0` para taxis amarillos.
   - `taxi_type = 1` para taxis verdes.
9. **Presencia de peajes (`tolls_amount`):** Convertida a una columna binaria `tolls`: 1 si el monto de peajes es mayor a 0, 0 si no.

---
## Protección y validación en BigQuery


Se utilizaron las siguientes opciones que permite BigQuery para proteger y asegurar una correcta administración de los datos normalizados y transformados en la plataforma.

## 1. Restricción de permisos de escritura de datos

Se deben usar **IAM Roles (Identity and Access Management)** para otorgar acceso granular. Por ejemplo:
- Para usuarios que solo consultan datos, otorgar permisos de solo lectura: `roles/bigquery.dataViewer`.
- Evitar permisos como `bigquery.dataEditor` o `bigquery.dataOwner` para usuarios que no deberían cargar datos.

---

## 2. Crear vista autorizada

Se creó una vista autorizada para que el usuario `mirta.llancaman@gmail.com` accediera a columnas específicas de la tabla `TaxiTrip_Normalized`:

```bash
CREATE OR REPLACE VIEW `noted-palisade-441212-j4.taxi_dataset.TaxiTrip_AuthorizedView` AS
SELECT 
  trip_id, 
  date, 
  total_amount
FROM 
  `noted-palisade-441212-j4.taxi_dataset.TaxiTrip_Normalized`;
```


## 3. Aplicar políticas a nivel de filas (filtrado dinámico de datos)

Se aplicó restricción de acceso a celdas específicas, en este caso a la columna `date`, como ejemplo, usando BigQuery Row-Level Security (RLS):

```bash
CREATE ROW ACCESS POLICY date_range_access_policy
ON `noted-palisade-441212-j4.taxi_dataset.TaxiTrip_Normalized`
GRANT TO "mirta.llancaman@gmail.com"
FILTER USING (date BETWEEN DATE('2024-11-01') AND DATE('2024-11-30'));
```

## 4. Habilitación de auditoría

El servicio de registros de auditoría permite monitorear inserciones en BigQuery con **Cloud Audit Logs**.

### Paso 1: Habilitar los registros de auditoría
1. Ir a la consola de Google Cloud: [Google Cloud Console](https://console.cloud.google.com).
2. Navegar a **IAM y administración > Logs de auditoría**.
3. Asegurarse de que la auditoría de BigQuery esté habilitada para eventos de tipo `DATA_WRITE`.

### Paso 2: Consulta los registros
1. Ve a **Logging > Explorador de registros**.
2. Usa este filtro para encontrar eventos de inserción:
   ```bash
   resource.type="bigquery_table"
   protoPayload.methodName="tabledata.insertAll"
   ```

Esto mostrará las inserciones recientes. Se puede consultar con detalle:
- Usuario que realizó la inserción.
- Tabla afectada.
- Fecha y hora del evento.

---

### Paso 3: Configura una alerta automática

1. Ir a **Monitoring > Alertas**.
2. Crear una nueva política de alerta.
3. Usar la métrica **Log-based Metric** basada en el filtro anterior para recibir notificaciones por correo o SMS.

---

## 5. Implementación de Scripts en SQL para validación de datos

Se implementaron las siguientes validaciones usando script de SQL:

1. Verificar valores nulos.
2. Validación de valores duplicados.
3. Validación de valores en columnas con valores esperados (p.ej., `vendor_id`, `payment_type`).
4. Validación de valores en `date` (fechas).
5. Validación de rangos en:
   - `total_amount`
   - `travel_time_min`
   - `price_min`
   - `trip_distance`
   - `price_mile`
   - `speed_ml/min`
6. Validación de valores en `PULocationID` y `time_slot`.
7. Validación de `dropoff_datetime` (fecha de finalización).
8. Validación de peajes (`tolls`): Verifica si los valores de esta columna están fuera de los valores esperados (0 o 1).
9. Validación de `day_name`: Verifica si el valor corresponde a un día válido de la semana.
10. Validación de `speed_ml/min` (velocidad): Esta no debe ser demasiado alta o baja para un viaje normal, lo cual podría indicar error de captura.
11. Validación de `price_min`, `price_mile` y otros costos relacionados.
12. Validación de relaciones entre columnas:
    - La duración del viaje (`travel_time_min`) y la distancia del viaje (`trip_distance`) deberían estar relacionadas con la velocidad (`speed_ml/min`). Estas relaciones fueron verificadas para garantizar coherencia.   
