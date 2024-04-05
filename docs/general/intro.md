# Estructura de Carpetas

<img src="../../images/folders.png" width="600" >

## Estructura Propuesta

La estructura de proyecto propuesta sigue una organización cuidadosamente planificada para facilitar
el desarrollo, la colaboración y la mantenibilidad del proyecto.

```
├───.github
│   └───workflows
│       └───ci.yml
├───data
│   ├───final
│   ├───procesed
│   └───raw
├───docs
├───models
├───pipeline
├───src
│   ├───_notebooks
│   ├───data
│   ├───preprocessing
│   ├───models
│   └───metrics
├───tests
│
├───.env
├───.gitignore
├───.pre-commit-config.yaml
├───LICENSE
├───mkdocs.yml
├───poetry.lock
├───pyproject.toml
└───README.md
```

### Carpetas

* **.github**: Contiene archivos y carpetas relacionados con la integración y la implementación continua (CI/CD) utilizando GitHub Actions u otras herramientas similares.
* **src**: Carpeta con el código fuente del proyecto organizado en subcarpetas según su funcionalidad
      * `_notebooks`: carpeta con archivos Jupyter Notebook, utilizados para el análisis exploratorio y experimentación de modelos.
      * `data`: Carpeta con las funciones relacionadas con la manipulación de datos.
      * `preprocessing`: Carpeta con las funciones de preprocesamiento de datos.
      * `models`: Carpeta con las funciones asociados a los modelos de Machine Learning (ML).
      * `metrics`: Carpeta con las funciones de evaluación de modelos ML.
* **tests**: Contiene archivos de pruebas unitarias y de integración para el código fuente del proyecto, organizados en subcarpetas según la funcionalidad a la que se refieren, como `data`, `metrics`, `models` y `preprocessing`. También contiene la carpeta `__pycache__` que almacena archivos de caché de las pruebas.
* **models**: Almacena modelos de aprendizaje automático entrenados durante el proyecto.
* **data**: Carpeta con los  datos utilizados en el proyecto, divididos en subcarpetas según su estado de procesamiento:
      * `raw`: carpeta para los datos sin procesar.
      * `procesed`: carpeta para los datos procesados .
      * `final`: carpeta para los datos finales.
* **pipeline**: Contiene archivos relacionados con el flujo de trabajo del proyecto, como cuadernos Jupyter (`*.ipynb`) utilizados para desarrollar y probar el pipeline, y la carpeta `.ipynb_checkpoints` que puede contener archivos de respaldo generados por Jupyter.
* **docs**: Contiene documentación relacionada con el proyecto, organizada en subcarpetas como `general` para documentación general, `images` para imágenes utilizadas en la documentación, `project` para documentación específica del proyecto, y `_others_` para otros documentos como diagramas y gráficos.

### Archivos

* **.env**: Archivo de configuración que se utilizan comúnmente en el desarrollo de software para almacenar variables de entorno.
* **.gitignore**: Archivo para especificar qué archivos y carpetas no deben ser rastreados por Git, como archivos binarios o locales y otros generados automáticamente que no deben compartirse.
* **.pre-commit-config.yaml**: Configura ganchos pre-commit para ejecutarse automáticamente antes de cada confirmación en Git, usando la herramienta `pre-commit`.
* **LICENSE**: Contiene los términos y condiciones de la licencia del proyecto, especificando cómo se puede utilizar, distribuir y modificar el código y otros recursos.
* **mkdocs.yml**: Configuración para `MkDocs`, una herramienta que genera documentación estática desde archivos Markdown, definiendo la estructura de la documentación y otras opciones.
* **poetry.lock**: Generado por Poetry, gestor de dependencias de Python, contiene una lista precisa de todas las dependencias y sus versiones exactas para garantizar la consistencia en diferentes entornos.
* **pyproject.toml**: Configuración de Poetry para definir información del proyecto, dependencias, opciones de empaquetado y otras configuraciones relacionadas.
* **README.md**: Principal archivo de markdown del proyecto que proporciona una descripción general, instrucciones de instalación, ejemplos de uso y otra información relevante para los usuarios y colaboradores.

## Aclaraciones sobre la estructura de carpetas

### Sobre los archivos y carpetas

**Carpeta `data`:**

* La carpeta `data` contiene una referencia del trabajo en local de los datos.
* Se recomienda **no versionar** los archivos dentro de esta carpeta.
* En su lugar, se sugiere utilizar herramientas de gestión de datos como **DVC** o **Git LFS** para versionar y controlar las modificaciones a los conjuntos de datos.

**Archivo `.env`:**

* El archivo `.env` contiene variables de entorno sensibles o específicas del entorno local, como claves de API o rutas de acceso a archivos.
* **No se debe versionar** este archivo en el repositorio de código, ya que podría exponer información confidencial o generar errores en otros entornos.
* Se recomienda utilizar herramientas como dotenv o python-dotenv para cargar las variables de entorno desde un archivo `.env` al ejecutar el código del proyecto.
* **Alternativas:**
    * **Herramientas de gestión de secretos**: Almacenar las variables de entorno en un servicio de gestión de secretos como *Azure Key Vault*, *Google Cloud Secret Manager*, *AWS Secrets Manager*.
    * **Entornos virtuales**: Crear diferentes entornos virtuales para cada tipo de entorno (desarrollo, producción, etc.) con sus propias variables de entorno específicas.


### Consideraciones adicionales

* La estructura de carpetas propuesta es una guía flexible que puede adaptarse a las necesidades específicas de cada proyecto.
* Se recomienda revisar y actualizar la estructura de carpetas a medida que el proyecto avanza y las necesidades cambian.
* Es importante mantener la documentación actualizada con información sobre la estructura de carpetas, las herramientas utilizadas y las prácticas recomendadas para el desarrollo del proyecto.
* Si el proyecto se desarrolla en equipo, es importante establecer reglas claras sobre la gestión de archivos, la versionación del código y la configuración del entorno de desarrollo.
