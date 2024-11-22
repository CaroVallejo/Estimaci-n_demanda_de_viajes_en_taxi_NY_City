# Consultoría a empresa CityFlow

### ¿Quiénes son Datalk?

Datalk es una empresa especializada en transformar datos en conocimiento accionable. Su equipo multidisciplinario de expertos en ciencia de datos, machine learning e inteligencia artificial ofrece un portafolio completo de servicios de tratamiento de datos. Ayudan a las organizaciones a optimizar sus procesos, mejorar la toma de decisiones y alcanzar sus objetivos estratégicos.

<p align="center">
    <img src="https://github.com/jdbaquero84/NY_cabs_consultant/blob/7107c08ca7e260eb2952ba3be2c6aeb543567935/src/LogoDatalk.JPG" width="250">
</p>

### El Cliente: CityFlow

CityFlow es una empresa de tecnología de transporte con un enfoque en sostenibilidad y cuidado del medio ambiente. Buscan brindar servicios de transporte eficientes y reducir la huella de carbono y la contaminación auditiva en los mercados donde operan. Para su expansión en Nueva York, CityFlow solicitó a Datalk una consultoría para analizar patrones de movilidad y preferencias de usuarios, con el fin de generar una estrategia de ingreso al mercado que satisfaga la demanda de viajes individuales.

<p align="center">
    <img src="https://github.com/jdbaquero84/NY_cabs_consultant/blob/5c3715b4213d875ec668c934e4023d3737c85d59/src/CityFlow.jpeg" width="250">
</p>

### Alcance y Objetivos del Proyecto

**El alcance del proyecto incluyó:**

*   Análisis de datos del servicio de transporte individual en Nueva York entre 2021 y 2024 para estimar la demanda de servicios de taxi según la ubicación.
*   Diseño e implementación de una solución tecnológica basada en datos para optimizar la operación del servicio de transporte individual.
*   Estimación de la cantidad óptima de vehículos necesarios para satisfacer la demanda.

**Los objetivos del proyecto fueron:**

*   Diseñar una estrategia integral para CityFlow para determinar la demanda de viajes individuales en Nueva York.
*   Analizar la relación entre los servicios de taxis (verdes y amarillos) y variables ambientales como emisiones de CO2 y contaminación auditiva.
*   Evaluar la huella de carbono y los niveles de contaminación auditiva en Nueva York para identificar el tipo de vehículo más adecuado.
*   Implementar un modelo de Machine Learning que pronostique la demanda futura.
*   Diseñar un dashboard interactivo para la visualización y comprensión de datos para la toma de decisiones.
*   Proporcionar conclusiones y recomendaciones.

### Propuesta y Entregables

Datalk propuso los siguientes entregables para el proyecto:

*   Dashboard interactivo en línea para visualizar y analizar datos del mercado de transporte individual de Nueva York.
*   Modelo de Machine Learning para pronosticar la demanda.
*   Definición y cálculo de 3 KPIs.

### KPIs

Se definieron los siguientes KPIs para el proyecto, junto con sus fórmulas de cálculo:

*   **KPI 1:** Proporción de viajes en taxi verde en un período específico.
    *   Fórmula:  $\frac{PG_{t+1} - PG_t}{PG_t} > M$
    *   Donde:
        *   PG: Proporción de viajes en taxi verde.
        *   M: Meta o umbral de crecimiento deseado.
        *   t: Período actual.

*   **KPI 2:** Comparación de tarifas promedio de taxi tradicional (amarillo) y taxi ecológico.
    *   Fórmula: $\overline{TY}_t > \overline{TG}_t$
    *   Donde:
        *   $\overline{TY}_t$: Tarifa promedio de taxi tradicional (amarillo) en el período t.
        *   $\overline{TG}_t$: Tarifa promedio de taxi ecológico en el período t.

*   **KPI 3:** Velocidad promedio en relación con la velocidad máxima permitida.
    *   Fórmula:  $M < \left( \overline{V} + SD_V \right)$
    *   Donde:
        *   M: Promedio de velocidad máximo permitido.
        *   $\overline{V}$: Velocidad promedio.
        *   $SD_V$: Desviación estándar de la velocidad.

### Metodología y Planificación

**Metodología:** Se utilizó SCRUM, un marco de trabajo ágil, para abordar el proyecto. Este enfoque flexible e iterativo permitió al equipo adaptarse continuamente al entorno para construir el mejor producto final para el cliente.

**Planificación:** Se diseñó un plan detallado mediante una carta Gantt, contemplando las actividades futuras para los próximos sprints, plazos y recursos disponibles.

### Desarrollo del Proyecto

**Semana 1:**

*   Se realizó un análisis EDA inicial utilizando datasets de muestra de servicios de taxis amarillos y verdes, combinados con datos de emisiones de CO2, niveles de ruido y otras bases de datos relevantes.
*   Se identificó la problemática y se establecieron objetivos, alcances y entregables.
*   Se elaboró un plan para las siguientes etapas del proyecto.

**Semana 2:**

*   El equipo se enfocó en la ingeniería de datos, incluyendo la extracción, depuración e integración de datos de múltiples fuentes.
*   Se implementó un Data Warehouse automatizado en Google Cloud Platform (GCP) utilizando Google Storage, Google BigQuery y Apache Airflow.
*   Se diseñó un diagrama Entidad-Relación (DER) para visualizar la arquitectura de la información y definir las relaciones entre las tablas en el Data Warehouse.
*   Se creó un diccionario de datos para asegurar una interpretación unívoca de los datos.
*   Se desarrollaron pipelines ETL para la limpieza y transformación de datos.
*   Se definió un flujo de trabajo basado en tecnologías para el manejo y análisis de grandes volúmenes de datos.
*   Se implementó una carga incremental automatizada.
*   Se elaboró un MVP (Minimum Viable Product) del dashboard.

**Semana 3:**

*   Se seleccionó, preparó y entrenó un modelo de Machine Learning para predecir la demanda de taxis ecológicos y tradicionales.
*   Se realizó un preprocesamiento de datos que incluyó la recopilación, limpieza, transformación y análisis exploratorio de una base de datos variada.
*   Se implementó el modelo de Machine Learning para predecir la cantidad de viajes diarios.
*   Se desarrolló un dashboard interactivo con KPIs para monitorear la demanda de taxis ecológicos y tradicionales.
*   Se puso a disposición el modelo en línea a través de una plataforma web.
*   Se elaboró un diagrama Entidad-Relación (DER) para el diseño de la base de datos. 

### Stack Tecnológico

El proyecto utilizó las siguientes herramientas:

*   **Exploración y Transformación de Datos (EDA y ETL):** VSCode, Python, Pandas, NumPy, Matplotlib, Seaborn, Google Colab.
*   **Machine Learning:** Scikit-Learn.
*   **Visualización:** Power BI.
*   **Automatización:** Google Cloud Platform (GCP), GitHub, Docker, Apache Airflow.

<p align="center">
    <img src="https://github.com/jdbaquero84/NY_cabs_consultant/blob/5c3715b4213d875ec668c934e4023d3737c85d59/src/stack_tecnologico.png" width="250">
</p>

### Conclusiones

El proyecto de consultoría para CityFlow permitió a Datalk aplicar su experiencia en ciencia de datos y análisis de datos para ayudar a la empresa a tomar decisiones estratégicas para su expansión en el mercado de Nueva York. Se desarrolló un modelo de Machine Learning para predecir la demanda de taxis, se diseñó un dashboard interactivo para el monitoreo de KPIs y se implementó una plataforma web para acceder al modelo en línea. El uso de un stack tecnológico robusto y una metodología ágil permitió al equipo de Datalk entregar un proyecto exitoso que cumplió con los objetivos y expectativas del cliente.
Las conclusiones del proyecto se pueden analizar desde diferentes perspectivas:
#### 1. Éxito en el cumplimiento de los objetivos:
* El proyecto logró cumplir con los objetivos planteados, tanto generales como específicos.
* Se diseñó una estrategia integral para la entrada de CityFlow al mercado de Nueva York, basada en un análisis exhaustivo de datos de movilidad y preferencias de usuarios.
* Se desarrolló un modelo de Machine Learning capaz de predecir la demanda futura de viajes, lo que permite a CityFlow optimizar la cantidad de vehículos en operación y mejorar la eficiencia de sus servicios.
* El dashboard interactivo proporciona una herramienta valiosa para la visualización y análisis de datos, facilitando la toma de decisiones informadas.
#### 2. Impacto del enfoque en sostenibilidad:
* El proyecto se centró en el compromiso de CityFlow con la sostenibilidad y el cuidado del medio ambiente.
* Se analizó la relación entre los diferentes tipos de taxis (verdes y amarillos) y variables ambientales como las emisiones de CO2 y la contaminación auditiva.
* Esta información permite a CityFlow tomar decisiones informadas sobre la composición de su flota, favoreciendo vehículos más sostenibles y contribuyendo a la reducción de la huella de carbono en la ciudad de Nueva York.
#### 3. Valor de la solución tecnológica:
* La solución tecnológica implementada, que incluye el modelo de Machine Learning, el dashboard interactivo y la plataforma web para acceder al modelo en línea, aporta un valor significativo a CityFlow.
* Permite a la empresa optimizar sus operaciones, tomar decisiones basadas en datos y diferenciarse en el mercado por su enfoque en la sostenibilidad.
#### 4. Importancia del trabajo en equipo y la metodología ágil:
* El éxito del proyecto se debe en gran medida al trabajo en equipo y la aplicación de la metodología SCRUM.
* El equipo multidisciplinario de Datalk, con experiencia en ciencia de datos, machine learning e inteligencia artificial, trabajó de manera colaborativa y adaptativa para abordar los desafíos del proyecto.
* La metodología ágil permitió responder a los cambios y ajustar el plan de trabajo según las necesidades del proyecto.
#### 5. Potencial de crecimiento y desarrollo futuro:
* El proyecto sienta las bases para un futuro desarrollo y crecimiento de la solución tecnológica.
* La plataforma web puede ser ampliada con nuevas funcionalidades y el modelo de Machine Learning puede ser mejorado con la incorporación de nuevos datos y variables.
* La experiencia adquirida en este proyecto servirá como base para futuros proyectos de Datalk en el sector de la movilidad sostenible.
