# *Diccionario de datos*


## *TaxiTrip_Normalized*
Este diccionario de datos corresponde al conjunto de datos recuperados de la página web de la comisión de taxis y limusinas de New York City tras haber pasado por el proceso de ETL con la función implementada para ello en Google Cloud Storage. Está compuesto por 18 columnas, las cuales son:

**Trip_id**: 
Id único que identifica cada uno de los viajes de la base de datos. Es de tipo string.

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

**Calendar_id**:
Código único que enlaza con la tabla calendario. Es de tipo integer.

## **Energía USA**
Este diccionario de datos corresponde al conjunto de datos proveniente de la Administración de Energía de EE.UU y abarca de 1980 a 2020, focalizado sólo en Estados Unidos. 

**Country**:
Indica el país del que se toman los datos. Es de tipo object.

**Energy_type**:
Indica la fuente de energía. Es de tipo object.

**Year**:
Indica el año en que se tomó la información. Es de tipo int64

**Energy_consumption**: 
Indica la cantidad de consumo de la fuente de energía que se está midiendo. Se mide en Quad BTU. Es de tipo float64.

**Energy_production**:
Indica la cantidad de energía que se produce de la fuente de energía que se está midiendo. Se mide en Quad BTU. Es de tipo float64.

**GDP**:
Indica Producto Interno Bruto expresado en miles de millones de dólares de 2015. Es de tipo float64. 

**Population**:
Indica la población del país expresado en millones. Es de tipo float64.

**Energy_intensity_per_capita**:
Muestra cuánta energía se consume por persona. Se mide en millones de BTU por persona. Es de tipo float64.

**Energy_intensity_by_GDP**:
Muestra el gasto de energia en relación con el Producto Interno Bruto. Se mide en 1000 BTU por dólar en el Producto Interno Bruto. Es de tipo float64.

**CO2_emission**: 
Muestra la cantidad de CO2 que se emite, medido en millones de toneladas métricas. Es de tipo float64. 

## *Ruido modificado*
Este dataset retoma SONYC Urban Sound Tagging (SONYC-UST), que es un conjunto de datos multietiqueta creado a partir de una red de sensores acústicos urbanos, desarrollado por un equipo de investigadores, incluyendo a Mark Cartwright, Jason Cramer, Ana Elisa Mendez Mendez, Yu Wang, Ho-Hsiang Wu, Vincent Lostanlen, Magdalena Fuentes, Graham Dove, Charlie Mydlarz, Justin Salamon, Oded Nov y Juan Pablo Bello.

**Borough**:
Indica el barrio de Nueva York en el que se encuentra el sensor. 1 corresponde a Manhattan, 3 a Brooklyn, 4 a Queens. Es de tipo int64.

**Block**: 
El bloque de Nueva York en el que se encuentra el sensor. Es de tipo int64.

**Latitude**: 
La latitud de la coordenada del bloque donde se encuentra el sensor. Es de tipo float64.

**Longitude**:
La longitud de la coordenada del bloque donde se encuentra el sensor. Es de tipo float64.

**Year**:
El año en el que se hizo la medición. Es de tipo int64.

**Week**:
La semana en la que se hizo la medición. Es de tipo int64.

**Day**: 
El día en que se hizo la medición. Es de tipo int64. 

**Hour**: 
La hora en que se hizo la medición. Es de tipo int64.

**5-1_car-horn_presence**:
Variable dummy que indica presencia de bocinas de autos en la medición. 1 indica presencia del sonido y 0 indica ausencia. Es de tipo int64.

**5-2_car-alarm_presence**:
Variable dummy que indica presencia de alarmas de autos en la medición. 1 indica presencia del sonido y 0 indica ausencia. Es de tipo int64.

**5-3_siren_presence**: 
Variable dummy que indica presencia de sirenas de vehículos en la medición. 1 indica presencia del sonido y 0 indica ausencia. Es de tipo int64.

**5-4_reverse-beeper_presence**: 
Variable dummy que indica presencia de alarmas de reversa de vehículos en la medición. 1 indica presencia del sonido y 0 indica ausencia. Es de tipo int64.

**5-X_other-unknown-alert-signal_presence**: 
Variable dummy que indica presencia alertas de presencia posiblemente atribuibles a autos en la medición. 1 indica presencia del sonido y 0 indica ausencia. Es de tipo int64.

**6-2_mobile-music_presence**: 
Variable dummy que indica presencia de autos reproduciendo música a alto volumen en la medición. 1 indica presencia del sonido y 0 indica ausencia. Es de tipo int64.

**6-3_ice-cream-truck_presence**:
Variable dummy que indica presencia de sonidos del camión de helados en la medición. 1 indica presencia del sonido y 0 indica ausencia. Es de tipo int64.

**Distritos**: 
Indica el nombre del distrito en el que se hizo la medición. Es de tipo object. 

**Unique_id**:
ID único de cada registro existente en la base de datos.


## *Location*
Este dataset incluye los datos relacionados con lugares, y enlaza con el resto de datasets.

**LocationID**:
ID único que indica las ubicaciones de los datasets. Es de tipo integer.

**Borough**:
Indica el distrito de Nueva York. Es de tipo string.

**Zone**:
Indica la zona de la ciudad de Nueva York. Es de tipo string.

**Service_Zone**:
Indica las zonas de servicio de taxi de la ciudad de Nueva York. Es de tipo string.

**Shape_leng**:
Brinda información respecto a la ubicación. Es de tipo integer. 

**Shape_Area**:
Brinda información respecto a la ubicación. Es de tipo integer.

## *Calendar*
Este dataset incluye los datos relacionados con fechas y enlaza con el resto de datasets.

**CalendarID**: 
Código identificador de registros que permite enlazar con las demás tablas. Es de tipo integer.

**Date**: 
Fecha. Está en formato datetime. 

**Year**: 
Año. Está en formato string.

**Unique_id**:
ID único de cada registro existente en la base de datos.


## **Location**
Este dataset incluye los datos relacionados con lugares, y enlaza con el resto de datasets.

**LocationID**:
ID único que indica las ubicaciones de los datasets. Es de tipo integer.

**Borough**
Indica el distrito de Nueva York. Es de tipo string.

**Zone**:
Indica la zona de la ciudad de Nueva York. Es de tipo string.

**Service_Zone**:
Indica las zonas de servicio de taxi de la ciudad de Nueva York. Es de tipo string.

**Shape_leng**:
Brinda información respecto a la ubicación. Es de tipo integer. 

**Shape_Area**:
Brinda información respecto a la ubicación. Es de tipo integer.

## **Calendar**
Este dataset incluye los datos relacionados con fechas y enlaza con el resto de datasets.

**CalendarID**: 
Código identificador de registros que permite enlazar con las demás tablas. Es de tipo integer.

**Date**: 
Fecha. Está en formato datetime. 

**Year**: 
Año. Está en formato string. 

**Month**: 
Mes. Está en formato string. 

**Month_name**: 
Nombre del mes. Está en formato string. 

**Day**: 
Dia. Está en formato string. 

**Day_name**: 
Nombre del día. Está en formato string. 

**Week**:
Número de semana. Está en formato integer.

**Is_weekend**: 
Variable dummy que indica con 0 si no es fin de semana y con 1 si es fin de semana. Está en formato boolean. 
