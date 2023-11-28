# SISTEMA DE RECOMENDACION DE VIDEOJUEGOS PARA LA PLATAFORMA STEAM
## Análisis Exploratorio de Datos (EDA) - Resultados Principales:

### Calidad de Datos:

- Se identificaron valores nulos, duplicados y columnas anidadas en los archivos `steam_games`, `user_items`, y `user_reviews`.
- Se llevó a cabo un proceso de limpieza para abordar estos problemas y garantizar la integridad de los datos.

### Valores Atípicos y Distribución de Datos:

- Se observó una distribución sesgada hacia la izquierda, con una concentración significativa de valores cercanos a 0 en diversas variables.
- Se realizaron análisis de outliers en `user_items`, identificando y tratando los valores atípicos para mejorar la precisión del modelo.

### Sentimiento de Usuarios:

- Se determinó que aproximadamente el 65% de las reseñas en Steam son positivas y un 12% son negativas, lo que proporciona una visión clave sobre la satisfacción general de los usuarios.

### Géneros y Sentimientos:

- Los géneros de juegos con mejor sentimiento positivo fueron acción, indie y free to play. Este hallazgo puede ser esencial para estrategias de desarrollo y marketing.

### Distribución de Géneros:

- Los géneros más abundantes en Steam son indie, acción, casual, aventura, estrategia, simulación y RPG.

### Tiempo de Juego a lo Largo de los Años:

- Se notó un aumento significativo en el tiempo de juego a partir de 2003, alcanzando su punto máximo en 2012. Sin embargo, después de 2012, se observa una disminución en el tiempo de juego.

### Principales Desarrolladores:

- Ubisoft y Smiteworks fueron identificados como los principales desarrolladores con una gran cantidad de juegos en la plataforma.

### Nubes de Palabras:

- Se crearon nubes de palabras para las categorías "recomendados" y "no recomendados" en las reseñas de usuarios, proporcionando una representación visual de términos clave asociados con cada categoría.

## Transformaciones de Datos:

### Limpieza de Datos:

- Se llevó a cabo un proceso exhaustivo de limpieza de datos en el notebook `Feature_engineering.ipynb`.
- Se eliminaron duplicados y valores nulos, mejorando la calidad general de los conjuntos de datos.

### Preprocesamiento de Columnas:

- En las columnas `playtime_forgenre`, se eliminaron valores con 0 para mejorar la coherencia de los datos.
- Las columnas de puntuaciones de reviews y fechas se transformaron en formato de año, facilitando análisis temporales y correlaciones.

### Transformaciones Eficientes:

- Se aplicaron transformaciones específicas para reducir el uso de memoria, convirtiendo ciertos datos en tablas pivote. Esta optimización contribuyó a la eficiencia de los endpoints.

## Sentiment Analysis:

### Procesamiento de Sentimientos:

- El análisis de sentimientos se implementó en el notebook `Feature_engineering.ipynb` utilizando la biblioteca NLTK.
- Las reseñas de usuarios se clasificaron como positivas, neutrales o negativas, proporcionando una perspectiva valiosa sobre la percepción de los usuarios hacia los videojuegos.

## Modelo de Sistema de Recomendación:

### Desarrollo del Modelo:

- Se logró con éxito la creación de un modelo de recomendación de videojuegos en base a un ID proporcionado.
- El modelo se basó en las columnas de género y utilizó la técnica de similitud del coseno, generando matrices de similitud para identificar y devolver los 5 juegos más similares.

## API REST:

- Se desarrolló una API REST en el framework FastAPI, que ofrece diversos endpoints para proporcionar información y recomendaciones a los usuarios. A continuación, se describen brevemente los endpoints disponibles:

  - **PlayTimeGenre:**
    - Endpoint: `/playtimegenre/{genero}`
    - Descripción: Devuelve el año con más horas jugadas para un género específico.

  - **UserForGenre:**
    - Endpoint: `/userforgenre/{genero}`
    - Descripción: Devuelve el usuario que acumula más horas jugadas para el género dado, junto con una lista de la acumulación de horas jugadas por año.

  - **UsersRecommend:**
    - Endpoint: `/usersrecommend/{anio}`
    - Descripción: Devuelve el top 3 de juegos más recomendados por usuarios para el año dado, considerando solo reseñas positivas o neutrales.

  - **UsersWorstDeveloper:**
    - Endpoint: `/usersworstdeveloper/{anio}`
    - Descripción: Devuelve el top 3 de desarrolladoras con juegos menos recomendados por usuarios para el año dado, considerando solo reseñas negativas.

  - **Sentiment Analysis:**
    - Endpoint: `/sentimentanalysis/{desarrolladora}`
    - Descripción: Según la empresa desarrolladora, devuelve un diccionario con el nombre de la desarrolladora como clave y una lista con la cantidad total de registros de reseñas de usuarios categorizados con análisis de sentimiento como valor.

  - **Recomendacion Juego:**
    - Endpoint: `/recomendacionjuego/{id_juego}`
    - Descripción: Ingresando el ID de un producto, devuelve una lista con 5 juegos recomendados similares al ingresado.

## Deployment en Render:

- La API REST se ha implementado en la plataforma Render y está disponible en [este enlace](https://soyhenrymlops.onrender.com/).

## Video Tutorial del Proceso:

- Se ha grabado un video que detalla todo el proceso, desde el desarrollo de la API hasta su implementación en Render. Puedes ver el video en [este enlace](https://youtu.be/hRcgjhE19oY).
