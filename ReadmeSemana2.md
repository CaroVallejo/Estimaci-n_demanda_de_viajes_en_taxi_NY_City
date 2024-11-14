# Semana 2 (Proyecto Final taxis_NY)

<div style="display: flex; justify-content:space-between;">
        <img src="src/WhatsApp Image 2024-11-14 at 13.42.47.jpeg" alt="Imagen 3" width="800" height="350">
</div>
</br>

## 📋 Indice.

1.Descripcion general

2.Diagrama E-R

3.Diccionario de Datos

4.Pipelines ETL

5.Flujo de trabajo

6.Demostracion de carga incremental

7.Minimun Viable Product (MVP) de dashboard

8.Herramientas para el Stack Tecnlogico


## 1. Descripcion General.

Durante la segunda semana del proyecto, el equipo se dedicó a las labores de ingeniería de datos. Se procedió a la extracción de datos desde múltiples fuentes, las cuales fueron sometidas a un riguroso proceso de depuración para garantizar su calidad. Tambien se ha impulsado la implementación de un almacén de datos (Data Warehouse) automatizado, aprovechando las capacidades de la plataforma Google Cloud Platform (GCP). Mediante la integración de servicios como Google Storage, Google BigQuery y la orquestación de Apache Airflow, se ha diseñado una infraestructura robusta para la carga, transformación y análisis de grandes volúmenes de datos. Esta solución innovadora permite procesar información de manera eficiente y escalable, optimizando los flujos de trabajo de ETL.


## 2. Diagrama Entidad Relacion (DER).

Con el propósito de visualizar la arquitectura de la información, se ha elaborado un diagrama Entidad-Relación. El mismo define las relaciones entre las distintas tablas en el Data Warehouse. Este modelo asegura que los datos se organicen de manera eficiente y facilita la realización de consultas complejas en BigQuery.

## 3. Diccionario de Datos.

Con el objetivo de fomentar una interpretación unívoca de los datos, se ha creado un diccionario de datos que sirva como referente terminológico, al cual se puede acceder mediante el siguiente link: [Diccionariodedatos.md](https://github.com/jdbaquero84/NY_cabs_consultant/blob/ae71847920692e146845ccd6fe6ac24f9a926a62/Diccionariodedatos.md)

## 4. Pipelines ETL. 

La presente ilustración gráfica detalla el flujo de trabajo ETL desarrollado. Se observa una pluralidad de fuentes de datos que, mediante la aplicación de técnicas de limpieza y transformación, son integradas en la base de datos de Google BigQuery.


<div style="display: flex; justify-content:space-between;">
        <img src="src/WhatsApp Image 2024-11-14 at 13.42.02.jpeg" alt="Imagen 3" width="800" height="350">
</div>
</br>


## 5. Flujo de Trabajo.

El flujo de trabajo propuesto se fundamenta en el empleo de tecnologías para el manejo y análisis de grandes volúmenes de datos. Inicialmente, se llevará a cabo la ingesta y transformación de los datos, los cuales serán almacenados en un Data Warehouse. Posteriormente, se aplicarán técnicas de Machine Learning para desarrollar modelos predictivos y descriptivos. Finalmente, se utilizará la herramienta PowerBI para construir un panel de control interactivo, que permitirá visualizar los resultados de manera clara y concisa.

<div style="display: flex; justify-content:space-between;">
        <img src="src/WhatsApp Image 2024-11-14 at 13.41.39.jpeg" alt="Imagen 3" width="800" height="350">
</div>
</br>


## 6. Carga incremental automatizada.

Se presentará una descripción detallada de los procesos llevados a cabo. Se invita al lector a complementar esta información visualizando el video adjunto = ...

## 7. Minimun Viable Product (MVP) de dashboard.

Se elaboró un prototipo de tablero de control que materializó visualmente una selección de los insights más relevantes extraídos del análisis de datos. Este MVP proporcionó un primer acercamiento a las funcionalidades y estética del producto definitivo.

## 8. Herramientas para el Stack Tecnológico

### Exploración y Transformación de Datos (EDA y ETL)

- **VSCode**
  - Visual Studio Code es un entorno de desarrollo ligero, modular y con soporte para múltiples lenguajes y extensiones. Su integración con herramientas de control de versiones y sus capacidades de depuración lo convierten en una herramienta esencial para desarrollar scripts de análisis y transformación de datos en Python.

- **Python**
  - Python es el lenguaje principal en ciencia de datos debido a su simplicidad, extensa comunidad y amplia colección de bibliotecas de análisis y machine learning. Su versatilidad permite tanto la manipulación de datos como el desarrollo de modelos de machine learning y la creación de visualizaciones, todo en un mismo entorno.

- **Pandas y NumPy**
  - Pandas es la biblioteca de referencia para la manipulación y análisis de datos en Python. Por otro lado, NumPy es una biblioteca fundamental para el cálculo numérico en Python, especialmente en el ámbito de la ciencia de datos, la estadística y el machine learning.

- **Matplotlib y Seaborn**
  - Estas bibliotecas de visualización son fundamentales para explorar patrones y relaciones en los datos durante el análisis exploratorio de datos (EDA). Matplotlib ofrece una personalización detallada de gráficos, mientras que Seaborn facilita la creación de gráficos estadísticos atractivos y permite obtener insights visuales que ayudan a tomar decisiones informadas durante el procesamiento y análisis.

 - **Google Colab** 
    - Google Colab es una plataforma ideal para el trabajo colaborativo en ciencia de datos y machine learning, ya que permite a equipos desarrollar proyectos de manera conjunta y eficiente. Al estar basado en la nube, facilita que varios miembros del equipo accedan y trabajen en el mismo notebook desde cualquier ubicación, simplemente utilizando un navegador web.

### Machine Learning

- **Scikit-Learn**

  - Scikit-Learn es una biblioteca de machine learning en Python que ofrece algoritmos eficientes y bien documentados para clasificación, regresión y clustering, entre otros. Su simplicidad y versatilida permite construir y evaluar modelos de manera rápida y confiable. Además, es una biblioteca abierta y altamente extensible, lo cual la convierte en una herramienta ideal para nuestra solución de machine learning.

### Visualización

- **Power BI**

  - Es una herramienta de visualización y análisis de datos de Microsoft que permite transformar datos en información visual e interactiva. Herramienta conocida y ampliamente usada por nuestro equipo ya que permite la creación de dashboards, reportes y análisis de forma versátil.

### Automatización

- **Google Cloud Platform (GCP)**
  - GCP proporciona una infraestructura escalable y segura que permite almacenar y procesar grandes volúmenes de datos sin necesidad de invertir en infraestructura física. Su conjunto de servicios administrados que pretendemos utilizar, como BigQuery para análisis de datos y Cloud Storage para almacenamiento, reduce significativamente los costos y la complejidad de manejar grandes volúmenes de datos. Además, GCP ofrece herramientas avanzadas de machine learning y soporte para entornos híbridos y multicloud, lo cual facilita la integración y despliegue de aplicaciones en un ecosistema más amplio.

- **GitHub**
  - GitHub es esencial para el control de versiones de código, permitiendo un trabajo colaborativo y organizado en el equipo. Su capacidad para gestionar versiones de scripts y documentación asegura que cualquier cambio pueda ser rastreado y revertido si es necesario, lo cual es crucial para mantener la integridad del proyecto y facilitar la colaboración entre los miembros del equipo.

- **Docker**
  - Docker permite crear entornos de ejecución consistentes, independientemente del sistema operativo o las dependencias de software. Esto garantiza que los scripts de ETL, los modelos de machine learning y las aplicaciones puedan desplegarse de manera uniforme y reproducible. La contenedorización también simplifica la escalabilidad y el mantenimiento de los entornos, especialmente en proyectos que requieren múltiples versiones de dependencias.

- **Apache Airflow**
  - Airflow es una herramienta de orquestación de flujos de trabajo que permite automatizar los procesos ETL y el despliegue de modelos de machine learning de forma estructurada y controlada. Su capacidad para gestionar dependencias, programar tareas y monitorear el estado de los procesos hace que sea una herramienta esencial en entornos de producción. Esto garantiza que las tareas se ejecuten en el orden correcto y proporciona alertas en caso de errores o fallos en el flujo de trabajo.

### Conclusión
Cada una de estas herramientas cumple un rol específico dentro del flujo de trabajo del proyecto, desde la ingesta de datos hasta la automatización de tareas. Al combinar estas tecnologías, se crea una infraestructura robusta, eficiente y escalable, que no solo facilita el análisis y el procesamiento de grandes volúmenes de datos, sino que también asegura que el proceso sea sostenible, reproducible y fácil de gestionar a largo plazo.
