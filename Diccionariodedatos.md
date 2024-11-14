# **Diccionario de datos**

## **Combined taxi data**
Este diccionario de datos corresponde al conjunto de datos recuperados de la página web de la comisión de taxis y limusinas de New York City tras haber pasado por el proceso de ETL con la función implementada para ello en Google Cloud Storage. Está compuesto por 18 columnas, las cuales son:

**VendorID**:
Proveedor de servicios de telefonía móvil. 1 corresponde a Creative Mobile Technologies, LLC. 2 corresponde a Verifone Inc. Es de tipo int32. 

**Date**:
Fecha en la que se dió el servicio. Indica año, mes y dia, en formato AAAA-MM-DD. Es de tipo object. 

**Year**:
Año en el que se dió el servicio. Es de tipo int32. 

**Month**:
Mes en el que se dió el servicio. Es de tipo object. 

**Day_name**:
Día de la semana correspondiente a cada fecha. Es de tipo object. 

**pickup_datetime**:
Fecha y hora en la que se recogió al usuario de taxi. Es de tipo datetime64[us].

**PULocationID**:
Zona de taxi según la taxi and limousine commission en la que se activó el servicio. Es de tipo int32.

**Time_slot**: 
Rango horario en que se dió el servicio de taxis. Presentó errores durante la normalización. Es de tipo int32.

**Dropoff_datetime**:
Fecha y hora en la que se dejó al usuario de taxi en su destino. Es de tipo datetime64[us].

**DOLocationID**:
Zona de taxi según la taxi and limousine commission en la que se finalizó el servicio. Es de tipo int32.

**Tolls**:
Variable dummy que indica la presencia o ausencia de peajes en el trayecto en que se dió el servicio. 1 indica presencia de peajes, 0 indica ausencia. Es de tipo int64.

**Total_amount**:
Tarifa total que el usuario pagó al finalizar el servicio. Es de tipo float64.

**Payment_type**:
Medio de pago que empleó el usuario. 1 indica Tarjeta de Crédito, 2 indica pago en efectivo, 3 indica que no se hizo cargo, 4 indica que existió disputa en la tarifa, 5 indica medio de pago desconocido y 6 indica que se anuló el viaje. Es de tipo float64.

**Travel_time_min**:
Indica la duración del viaje en minutos. Es de tipo float64.

**Price_min**:
Indica el precio por minuto dentro de cada viaje. Es de tipo float64.

**Trip_distance**:
Indica la distancia en millas de cada servicio. Es de tipo float64.

**Price_mile**:
Indica el precio por milla dentro de cada viaje. Es de tipo float64.

**Speed_ml/min**:
Indica la velocidad dentro del viaje en millas por minuto. Es de tipo float64. 
